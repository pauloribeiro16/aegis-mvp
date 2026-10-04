#!/usr/bin/env python3
"""steps.py — Phase 1 step execution: compose → call → L0 validate → store.

Each step = one ficha (generic) + one deterministic pack. The L0 parser checks
the model's answer against the ficha's output contract; on failure the call is
retried once with the validator errors appended (flag-not-drop), then the stage
aborts with forensics on disk.

The final deliverable (doc02_adjusted_goals.md, Doc02 case format) is assembled
deterministically: goals/framing/tensions come from L0-validated artifacts,
controls and tiers are DERIVED by code (controls.py) — the deliverable step p5
makes no LLM call.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from pathlib import Path

from compose import (REGULATIONS, SD_RE, anchor_slice, carries_reg_card,
                     compose_call, confirmed_regulations, domain_dir, load_case,
                     load_selection, objective_paragraph, parse_simple_yaml,
                     sub_so_objective)
from controls import (goal_anchors, parse_overrides, sd_control_sections,
                      track_b_rows)
import quality
import runconfig
from llm import LLMError, OllamaClient
from trace import Trace, count_calls, now_iso, update_manifest

NUM_CTX = {"p1": 16384, "p2": 16384, "p3": 32768, "p3f": 16384, "p4": 32768,
           "p4t": 32768}
# output budget per step (P4 tables are the largest model output)
# P4 emits a 9-column table for every Sub-SO of a module: at 8192 the answer
# was truncated mid-table and the L0 repair hit the same cap (job 1969983,
# D-08.3). The budget is the table, not a sentence.
NUM_PREDICT = {"p1": 4096, "p2": 2048, "p3": 12288, "p3f": 2048, "p4": 16384,
               "p4t": 4096}

PATTERNS = {"achieve", "cease", "maintain", "avoid", "optimize"}
# template §3 renders long-form property names; normalize to the enum codes
PROPERTY_ALIASES = {
    "confidentiality": "c", "integrity": "i", "availability": "a",
    "privacy right": "privacy-right", "privacy-right": "privacy-right",
    "accountability": "accountability", "c": "c", "i": "i", "a": "a",
}
PROPERTY_LONG = {"c": "Confidentiality", "i": "Integrity", "a": "Availability",
                 "privacy-right": "Privacy Right", "accountability": "Accountability"}
FRAMING_DIMENSIONS = ["Size", "Area of operation", "Regulatory roles",
                      "Inherited capabilities"]


# --------------------------------------------------------------------------
# fenced-block extraction helpers
# --------------------------------------------------------------------------

def extract_fenced(text: str, lang: str | None = None) -> str:
    """First fenced block (optionally with a given info string)."""
    pattern = rf"```{lang}[^\n]*\n(.*?)```" if lang else r"```[^\n]*\n(.*?)```"
    m = re.search(pattern, text, re.S)
    if not m:
        raise ValueError(f"no {'```' + lang + ' ' if lang else ''}fenced block found in answer")
    return m.group(1).strip()


def parse_md_table(text: str) -> list[list[str]]:
    """Parse a markdown table into rows of cells (separator rows dropped)."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


#: Spellings models reach for when a regulation id is written inline, mapped to
#: the canonical token. Observed in the field: qwen3.8 wrote "AIACT" for
#: AI_Act on a 4-regulation case (Case_02, job 1979399) and qwen3.5 wrote the
#: same class of mangling at the smoke. This is a SPELLING map, not a
#: tolerance: only the regulation token is normalised, the sub-domain part
#: must still match exactly, and the row is still rejected downstream if the
#: regulation is not one this module actually carries (check_subso_coverage /
#: the L1 phantom-regulation check). A model that names the wrong regulation
#: still fails; one that misspells the right one no longer costs a whole run.
_REG_SPELLING = {
    "aiact": "AI_Act", "aiacts": "AI_Act", "ai act": "AI_Act", "ai-act": "AI_Act",
    "aia": "AI_Act", "ai": "AI_Act",
    "nis2": "NIS2", "nis 2": "NIS2", "nis-2": "NIS2", "nisii": "NIS2",
    "gdpr": "GDPR",
    "cra": "CRA",
    "dora": "DORA",
    "doraia": "DORA",
}


def _canonical_reg(token: str) -> str:
    """Canonical regulation token, or '' when the spelling is unrecognisable."""
    t = token.strip().strip("` ").strip()
    if t in REGULATIONS:
        return t
    return _REG_SPELLING.get(re.sub(r"[\s\-_]+", "", t).lower(), "")


def _one_reg(bs: str, sd_id: str) -> str:
    """The single regulation a Baseline source cites (SG-D-XX.Y.<REG>).

    The sub-domain part must match EXACTLY — a row that points at a different
    sub-domain is a real error and stays an error. Only the regulation token is
    spelling-normalised, because that is the half models get wrong (see
    _REG_SPELLING). An unrecognisable regulation token is still rejected here.
    """
    raw = bs.strip("` ")
    m = re.fullmatch(rf"SG-{re.escape(sd_id)}\.(\S+)", raw)
    if not m:
        raise ValueError(f"Baseline source {bs!r} must cite exactly one Sub-SO id "
                         f"SG-{sd_id}.<REG> (one regulation per goal row)")
    reg = _canonical_reg(m.group(1))
    if not reg:
        raise ValueError(f"Baseline source {bs!r} has regulation {m.group(1)!r}, "
                         f"which is not one of {'/'.join(REGULATIONS)}")
    return reg


# --------------------------------------------------------------------------
# per-step L0 parsers (output contract = ficha Output schema)
# --------------------------------------------------------------------------

def parse_p1(answer: str) -> dict:
    yaml_text = extract_fenced(answer, "yaml")
    fact = parse_simple_yaml(yaml_text)
    required = ["company", "sector", "size_employees", "jurisdictions", "legal_form",
                "product_summary", "develops_software", "data_categories",
                "data_subjects", "hosting", "assumed_regulations", "open_questions"]
    missing = [k for k in required if k not in fact]
    if missing:
        raise ValueError(f"fact sheet missing required fields: {missing}")
    if fact["develops_software"] not in ("true", "false", "unclear", True, False):
        raise ValueError(f"develops_software must be true|false|unclear, got {fact['develops_software']!r}")
    regs = fact.get("assumed_regulations")
    if not isinstance(regs, list) or not regs:
        raise ValueError("assumed_regulations must be a non-empty list (input §5)")
    if not isinstance(fact.get("jurisdictions"), list):
        raise ValueError("jurisdictions must be a list")
    return {"yaml_text": yaml_text, "fact": fact}


def parse_p2(answer: str) -> dict:
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    if not rows:
        raise ValueError("no table found in P2 answer")
    body = rows[1:] if rows[0] and rows[0][0].lower().startswith("regulation") else rows
    verdicts = []
    for cells in body:
        if len(cells) < 3:
            raise ValueError(f"P2 table row has {len(cells)} columns, expected >=3: {cells}")
        reg = cells[0].replace("*", "").replace("`", "").strip()
        verdict = cells[1].replace("*", "").replace("`", "").strip().lower()
        if verdict not in ("applies", "does not apply", "flagged"):
            raise ValueError(f"invalid verdict {verdict!r} for {reg}")
        if reg not in REGULATIONS:
            raise ValueError(f"non-canonical regulation id: {reg!r}")
        verdicts.append({"regulation": reg, "verdict": verdict, "rationale": cells[2]})
    got = [v["regulation"] for v in verdicts]
    if sorted(got) != sorted(REGULATIONS):
        raise ValueError(f"§2 must cover exactly the 5 candidate regulations; got {got}")
    return {"md": md, "verdicts": verdicts}


def parse_p3(answer: str, candidates: list[str]) -> dict:
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    selected, seen = [], set()
    for cells in rows:
        if not cells:
            continue
        m = SD_RE.match(cells[0].replace("`", "").strip())
        if m:
            if len(cells) < 3 or not cells[1] or not cells[2]:
                raise ValueError(f"selection row incomplete for {cells[0]}: {cells}")
            sid = cells[0].replace("`", "").strip()
            if sid in seen:
                raise ValueError(f"duplicate selection row: {sid}")
            if sid not in candidates:
                raise ValueError(f"selected sub-domain {sid} is not in the candidate set")
            seen.add(sid)
            selected.append({"id": sid, "name": cells[1], "rationale": cells[2]})
    exc_match = re.search(r"Excluded candidates:?\s*(.*)$", md, re.S | re.I)
    excluded, exc_seen = [], set()
    if exc_match:
        for line in exc_match.group(1).splitlines():
            line = line.strip().lstrip("-").strip()
            m = re.match(r"`?(D-\d{2}\.\d)`?\s*[—:-]\s*(.+)", line)
            if m:
                sid, why = m.group(1), m.group(2).strip()
                if sid in exc_seen:
                    raise ValueError(f"duplicate exclusion: {sid}")
                if sid in seen:
                    raise ValueError(f"sub-domain {sid} appears both selected and excluded")
                if sid not in candidates:
                    raise ValueError(f"excluded sub-domain {sid} is not in the candidate set")
                exc_seen.add(sid)
                excluded.append({"id": sid, "why": why})
    got = seen | exc_seen
    missing = sorted(set(candidates) - got)
    if missing:
        raise ValueError(f"candidates neither selected nor excluded (silent drop): {missing}")
    if not selected:
        raise ValueError("empty selection — the pipeline cannot continue")
    return {"md": md, "selected": selected, "excluded": excluded}


def parse_p3f(answer: str) -> dict:
    """§2 Framing: a 2-column table with exactly the four canonical dimensions."""
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    dims: dict[str, str] = {}
    for cells in rows:
        if len(cells) != 2:
            raise ValueError(f"framing table row must have 2 columns: {cells}")
        key = " ".join(cells[0].split()).lower().rstrip(":")
        if key == "dimension":  # header row
            continue
        dims[key] = cells[1]
    missing = [d for d in FRAMING_DIMENSIONS
               if d.lower() not in dims or not dims[d.lower()].strip()]
    if missing:
        raise ValueError(f"framing table missing or empty dimension(s): {missing} "
                         f"(expected exactly: {', '.join(FRAMING_DIMENSIONS)})")
    extra = [k for k in dims if k not in [d.lower() for d in FRAMING_DIMENSIONS]]
    if extra:
        raise ValueError(f"framing table has unexpected dimension(s): {extra}")
    return {"framing": md.strip()}


def parse_p4(answer: str, sd_id: str, expect_id: bool = True) -> dict:
    md = extract_fenced(answer, "markdown")
    m5 = re.search(r"^##\s+§5\b", md, re.M)
    if not m5:
        raise ValueError("P4 answer missing the '## §5' section (assumptions/open questions)")
    goals_part, assum_part = md[:m5.start()], md[m5.start():]

    rows = parse_md_table(goals_part)
    goals = []
    seq = 0
    last_reg_idx = -1
    for cells in rows:
        if not cells:
            continue
        idm = re.match(r"`?(AG-D-\d{2}\.\d-\d{3})`?", cells[0].replace("*", "").strip())
        if not idm:
            if expect_id:
                continue
            # per-row agent submission: the caller supplies 9 cells whose first
            # cell is a placeholder; the id is assigned on persist, so only the
            # column count and the field rules apply here
            gid = f"AG-{sd_id}-NNN"
        else:
            gid = idm.group(1)
        if len(cells) != 9:
            raise ValueError(f"goal row {gid} has {len(cells)} columns, expected 9 "
                             "(ID | Adjusted goal | Company implication | Pattern | Property | "
                             "Parent goal | Baseline source | Regulatory source | Adjustment) — "
                             "control anchors are derived by code, not emitted")
        seq += 1
        if expect_id:
            gid = idm.group(1)
            expected = f"AG-{sd_id}-{seq:03d}"
            if gid != expected:
                raise ValueError(f"goal IDs must be sequential from 001: expected {expected}, got {gid}")
        # a bare pipe inside a cell splits the row and breaks the column
        # contract; reject it here rather than failing the whole stage later
        if any("|" in c for c in cells):
            raise ValueError(f"{gid}: a cell contains a literal '|' — markdown tables "
                             "cannot carry it; rephrase using commas or semicolons")
        pattern = cells[3].strip().lower()
        if pattern not in PATTERNS:
            raise ValueError(f"invalid pattern {pattern!r} on {gid}")
        prop_raw = " ".join(cells[4].strip().lower().split())
        prop = PROPERTY_ALIASES.get(prop_raw) or PROPERTY_ALIASES.get(prop_raw.replace(" ", "-"))
        if prop is None:
            raise ValueError(f"invalid property {cells[4]!r} on {gid}")
        parent = cells[5].replace("`", "").strip()
        if not re.fullmatch(rf"SO-{re.escape(sd_id)}\.HL", parent):
            raise ValueError(f"invalid parent goal {parent!r} on {gid} (expected SO-{sd_id}.HL)")
        reg = _one_reg(cells[6], sd_id)
        reg_idx = REGULATIONS.index(reg)
        if reg_idx < last_reg_idx:
            raise ValueError(f"{gid}: regulation slots must follow the canonical order "
                             f"{' → '.join(REGULATIONS)} (got {REGULATIONS[last_reg_idx]} "
                             f"before {reg})")
        last_reg_idx = reg_idx
        if not cells[7].strip():
            raise ValueError(f"empty regulatory source on {gid} (R2a)")
        if not cells[8].strip():
            raise ValueError(f"empty adjustment record on {gid} (R3/ADR-003 D1)")
        goals.append({
            "id": gid, "goal": cells[1], "implication": cells[2], "pattern": pattern,
            "property": prop, "parent": parent,
            # the CANONICAL id, not the raw text: baseline_source is what the
            # anchor derivation and the L1 validator key on, so leaving the
            # mangled spelling here would break them downstream of the gate
            "baseline_source": f"SG-{sd_id}.{reg}",
            "regulation": reg, "source": cells[7].strip(), "adjustment": cells[8].strip(),
        })
    if not goals:
        # a module may legitimately carry no Sub-SO for the confirmed
        # regulations (e.g. D-02.2 GDPR: partial via SG-D-02.1.GDPR; D-08.3 both)
        if re.search(r"(?i)none\s*[—-]\s*no sub-so", md):
            assumptions = []
            for line in assum_part.splitlines():
                s = line.strip()
                if s.startswith(">") or s.startswith("- "):
                    if s.lower().rstrip(".") not in ("- none", "> none"):
                        assumptions.append(s)
            return {"md": md, "goals": [], "assumptions": assumptions}
        raise ValueError(f"no AG-D-{sd_id}-NNN rows found in P4 answer (if this module "
                         f"carries no Sub-SO for the confirmed regulations, answer with "
                         f"the marker 'None — no Sub-SO for the confirmed regulations.')")

    assumptions = []
    for line in assum_part.splitlines():
        s = line.strip()
        if s.startswith(">") or s.startswith("- "):
            if s.lower().rstrip(".") not in ("- none", "> none"):
                assumptions.append(s)

    return {"md": md, "goals": goals, "assumptions": assumptions}


def parse_p4t(answer: str) -> dict:
    """Tension resolutions: a 5-column table, or the single line `None.`."""
    md = extract_fenced(answer, "markdown")
    if md.strip().lower().rstrip(".") == "none":
        return {"md": md, "tensions": []}
    tensions = []
    seq = 0
    for cells in parse_md_table(md):
        if not cells:
            continue
        idm = re.match(r"`?(T-\d{3})`?", cells[0].replace("*", "").strip())
        if not idm:
            continue
        if len(cells) != 5:
            raise ValueError(f"tension row {idm.group(1)} has {len(cells)} columns, "
                             "expected 5 (ID | Sub-domains | Tension | Conflict | Resolution)")
        seq += 1
        if idm.group(1) != f"T-{seq:03d}":
            raise ValueError(f"tension IDs must be sequential from T-001: got {idm.group(1)}")
        for i, name in ((2, "Tension"), (3, "Conflict"), (4, "Resolution")):
            if not cells[i].strip():
                raise ValueError(f"empty {name} cell on {idm.group(1)}")
        tensions.append({"id": idm.group(1), "subdomains": cells[1],
                         "tension": cells[2], "conflict": cells[3],
                         "resolution": cells[4]})
    if not tensions:
        raise ValueError("no T-NNN rows and no `None.` marker in the p4t answer")
    return {"md": md, "tensions": tensions}


PARSERS = {"p1": parse_p1, "p2": parse_p2, "p3": parse_p3, "p3f": parse_p3f,
           "p4t": parse_p4t}


# --------------------------------------------------------------------------
# shared persistence + content gates (pipeline steps AND agent tools)
# --------------------------------------------------------------------------

def store_parsed(run_dir: Path, step: str, subdomain: str | None, parsed: dict) -> None:
    """Persist one validated step artifact in the run's steps/ layout."""
    steps_dir = run_dir / "steps"
    if step == "p1":
        (steps_dir / "fact_sheet.yaml").write_text(parsed["yaml_text"], encoding="utf-8")
    elif step == "p2":
        (steps_dir / "verdicts.md").write_text(parsed["md"], encoding="utf-8")
        (steps_dir / "verdicts.json").write_text(
            json.dumps({"verdicts": parsed["verdicts"]}, indent=1, ensure_ascii=False),
            encoding="utf-8")
    elif step == "p3":
        (steps_dir / "selection.md").write_text(parsed["md"], encoding="utf-8")
        (steps_dir / "selection.json").write_text(
            json.dumps({"selected": parsed["selected"], "excluded": parsed["excluded"]},
                       indent=1, ensure_ascii=False), encoding="utf-8")
    elif step == "p3f":
        (steps_dir / "framing.md").write_text(parsed["framing"] + "\n", encoding="utf-8")
    elif subdomain is not None:
        goals_dir = steps_dir / "goals"
        goals_dir.mkdir(exist_ok=True)
        fname = subdomain.replace(".", "_")
        (goals_dir / f"{subdomain}.md").write_text(parsed["md"], encoding="utf-8")
        (goals_dir / f"{fname}.json").write_text(
            json.dumps({"subdomain": subdomain, "goals": parsed["goals"],
                        "assumptions": parsed["assumptions"]},
                       indent=1, ensure_ascii=False), encoding="utf-8")
    elif step == "p4t":
        (steps_dir / "tensions.md").write_text(parsed["md"] + "\n", encoding="utf-8")
        (steps_dir / "tensions.json").write_text(
            json.dumps({"tensions": parsed["tensions"]}, indent=1, ensure_ascii=False),
            encoding="utf-8")


def check_p4_quality(repo: Path, run_dir: Path, parsed: dict, sd_id: str) -> dict:
    """Content gates: the Sub-SO must exist for each confirmed regulation the
    module carries, and the rows must retain the obligation, stay grounded
    in the intake, avoid technology, and be specific (quality.run_all)."""
    goals = parsed["goals"]
    sd_dir = domain_dir(repo, sd_id)
    confirmed = confirmed_regulations(run_dir)

    # every Sub-SO card this module carries for a confirmed regulation must
    # be restated exactly once (no silent drop, no duplicate, no phantom reg)
    # The `.exists()` guard matches the one in _call: without it, a confirmed
    # regulation whose module file is absent raised FileNotFoundError here.
    # That path is only reachable at 4+ applicable regulations — TinyTask
    # (GDPR+CRA) never reached it, and no run did until Case_02 confirmed
    # AI_Act against a module (D-06.4) that ships no AI_Act card.
    expected_regs = [reg for reg in confirmed if carries_reg_card(repo, sd_id, reg)]
    coverage = quality.check_subso_coverage(goals, expected_regs)
    if coverage:
        raise ValueError("; ".join(coverage))

    baselines = {reg: sub_so_objective(repo, sd_id, reg) for reg in expected_regs}
    steps_dir = run_dir / "steps"
    sources = [baselines[r] for r in expected_regs]
    for name in ("fact_sheet.yaml", "framing.md"):
        f = steps_dir / name
        if f.exists():
            sources.append(f.read_text(encoding="utf-8"))
    # implications already stored for OTHER sub-domains: the cheapest way to
    # satisfy the column is one sentence pasted everywhere, so each row is
    # compared against every OTHER row (this sub-domain's and previous ones')
    other = [g["implication"] for jf in sorted((steps_dir / "goals").glob("*.json"))
             for g in json.loads(jf.read_text()).get("goals", [])]
    for g in goals:
        peers = other + [o["implication"] for o in goals
                         if o["id"] != g["id"]]
        findings = quality.run_row(g, baselines, sources, peers)
        if findings:
            raise ValueError("; ".join(f"{g['id']}: {m}" for m in findings))
    coverage = quality.check_subso_coverage(goals, expected_regs)
    if coverage:
        raise ValueError("; ".join(coverage))
    return parsed


EXTRA_INSTRUCTION = {
    "p1": "Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.",
    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),
    # The default p3 wrap instruction was left as a dangling stub
    # ("...fenced block containing ") by an earlier prompt-engineering pass that
    # meant to replace it wholesale. The truncation is silent — the composed
    # prompt is still well-formed, just missing its payload — and it is
    # catastrophic: told to return one fenced block "containing" nothing, four of
    # five models echoed the context pack back instead of answering
    # (run_m02_glm47_r01_1979986 and its siblings, all aborting with "candidates
    # neither selected nor excluded"). A composed prompt is asserted to end with
    # its own instruction; see _assert_wrap_instruction.
    "p3": ("Wrap your answer: return ONLY one ```markdown fenced block containing "
           "(a) the §3 selection table `| Sub-domain | Name | Trigger rationale |` "
           "with no preamble line, and "
           "(b) a line `Excluded candidates:` followed by one line per excluded "
           "candidate in the form `<D-XX.Y> — <why-not>`, or the word `none`. "
           "The table and the exclusion list partition the candidate set: every "
           "candidate appears in exactly one of them. Nothing else."),
    # PROMPT-ENGINEERED VARIANT (2026-10-04, after glm-4.7-flash and
    # nemotron-3.5 both failed 5/5 screening runs here). The original asked for
    # a table PLUS the complement of it in a second section — a shape that
    # invites both observed failures: listing an id in both parts (glm) and
    # inventing an exclusion id once the candidate list is far back in the
    # prompt (nemotron). This variant fixes the ORDER OF OPERATIONS: decide the
    # exclusion first, then build the table from what is left, which makes an
    # overlap structurally impossible, and it forbids invented identifiers.
    # It is the EXP-04 arm (--p3-instruction clarified), not the default: with
    # the default itself truncated, an ablation run would have compared a broken
    # control against a working treatment and concluded the variant fixed it.
    "p3_clarified": ("WORK IN THIS ORDER — it is not a suggestion, it is the whole task. "
           "STEP 1: look at the candidate set below and pick AT MOST ONE "
           "sub-domain to exclude, copying its identifier character-for-character "
           "from that set. If you cannot justify excluding any, exclude none. "
           "STEP 2: build the selection table from the remaining candidates. "
           "A sub-domain can NEVER appear in both parts: if you excluded it, it "
           "does not go in the table, and vice-versa. "
           "Do NOT invent, guess, complete or 'fix' an identifier: every id you "
           "write, in either part, must already exist in the candidate set. "
           "Then return ONLY one ```markdown fenced block containing "
           "(a) the §3 selection table `| Sub-domain | Name | Trigger rationale |` "
           "with no preamble line, and "
           "(b) a line `Excluded candidates:` followed by one line per excluded "
           "candidate in the form `<D-XX.Y> — <why-not>`, or the word `none`. "
           "Before you answer, check: every candidate appears in exactly one part."),


    "p3f": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
            "§2 framing table: header `| Dimension | Framing |` and exactly 4 rows — "
            "Size, Area of operation, Regulatory roles, Inherited capabilities — each "
            "framing cell 1–3 sentences traced to the fact sheet/verdicts (R6), "
            "technology-neutral (R5). Nothing else."),
    "p4t": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
            "tension-resolution table `| ID | Sub-domains | Tension | Conflict | "
            "Resolution |` with one row per corpus tension among the confirmed "
            "regulations (IDs sequential T-001…; resolution states the binding rule, "
            "e.g. strictest-SLA routing). If the corpus surfaces no tension among the "
            "confirmed regulations, return ONLY the line `None.` inside the fence. "
            "Technology-neutral (R5). Nothing else."),
}


# Per-run prompt variants. The shipped EXTRA_INSTRUCTION above is the reference
# behaviour — it is what the EXP-02/EXP-03 baseline ran on. A variant is
# selected per run via config.json `ficha_overrides: {"<key>": "<variant>"}`, so
# a prompt change is a measured arm rather than a silent redefinition of the
# baseline.
P3_INSTRUCTION_VARIANTS = {"clarified": EXTRA_INSTRUCTION["p3_clarified"]}


def _assert_wrap_instruction(step: str, extra: str) -> None:
    """A wrap instruction that states no payload is worse than none at all.

    Every step's instruction ends by naming what the fenced block must contain.
    When that clause was lost — as it was for p3, leaving the literal
    "...fenced block containing " — the composed prompt is still syntactically
    fine, passes every linter, and reaches the model as an instruction to return
    a block containing nothing. Four of five models in run_m02_* answered by
    echoing the context pack; the gate reported "candidates neither selected nor
    excluded", a symptom four causal steps from the actual defect.

    A dangling preposition is the signature, so it is what is checked: a wrap
    instruction must not end on a word that promises something after it.
    """
    if not extra.startswith("Wrap your answer"):
        return
    stripped = extra.rstrip().rstrip("`").rstrip()
    if stripped.split()[-1] in {"containing", "with", "of", "and", "the", "a", "to", "is"}:
        raise ValueError(
            f"step {step}: the wrap instruction ends on '{stripped.split()[-1]!r}' — it "
            f"promises a payload and then stops. Text was almost certainly lost from "
            f"EXTRA_INSTRUCTION[{step!r}]. Full instruction: {extra!r}")


def p4_extra_instruction(sd_id: str, subso_ids: list[str] | None = None) -> str:
    if subso_ids is None:
        subso_ids = []
    if not subso_ids:
        # A module whose Sub-SO cards all belong to NON-confirmed regulations has
        # no duty to restate (D-08.3 for a GDPR+CRA run carries only DORA/NIS2).
        # The model kept inventing rows with an `SG-<sd>.HL` baseline and failed
        # L0 twice per call; state the valid answer explicitly.
        return (
            f"Wrap your answer: return ONLY one ```markdown fenced block containing "
            f"(a) the heading `### {sd_id} — <canonical name>` followed by the single line "
            f"`None — no Sub-SO for the confirmed regulations.`, and (b) a heading `## §5` "
            f"with `None.` READ THIS: the module header saying a regulation 'applies' means "
            f"the regulation is IN SCOPE for the company — NOT that this sub-domain restates "
            f"a duty under it. 11 of the 38 sub-domains carry such a module with NO Sub-SO "
            f"card (the file ends with '(no ... Sub-SO or requirements in this sub-domain)'). "
            f"Therefore this module has NO goal rows. Do not invent one, and do not cite "
            f"`SG-{sd_id}.HL` as a baseline source. Nothing else."
        )
    return (
        f"Wrap your answer: return ONLY one ```markdown fenced block containing "
        f"(a) the heading `### {sd_id} — <canonical name>` and the 9-column goal table "
        f"(`ID | Adjusted goal | Company implication | Pattern | Property | Parent goal | "
        f"Baseline source | Regulatory source | Adjustment`), and (b) a heading `## §5` "
        f"listing only `> ASSUMPTION:` blockquotes and open questions this sub-domain owes "
        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "
        f"TERMINATION: after the `## §5` section the answer is COMPLETE — emit the "
        f"closing fence on the next line and stop. No table continuation, no notes, no "
        f"second §5, no text of any kind after the closing fence; an answer that keeps "
        f"writing past §5 hits the output cap and is discarded whole. Column rules: this module "
        f"declares EXACTLY {len(subso_ids)} Sub-SO(s) to restate — "
        f"{', '.join(subso_ids)} — and no others; write one row per listed id, in that "
        f"order. A regulation whose module is attached but which is NOT in that list has no "
        f"duty here. Adjusted goal = a full company-"
        f"proportional RESTATEMENT of that Sub-SO's Objective (2+ sentences, same "
        f"obligation content, no meta-language like 'restatement of the baseline'); "
        f"Company implication = what this duty concretely means for THIS company given "
        f"the §2 framing and fact sheet (1-2 sentences, name the company's actual "
        f"situation); Baseline source = the single corpus Sub-SO id the row restates "
        f"(e.g. `SG-{sd_id}.GDPR`); Property MUST be one of C, I, A, privacy-right, "
        f"accountability. Control anchors are derived by code — do NOT emit any. "
        f"ADJUSTMENT — a decision rule, not a menu. `unchanged — fits as stated` is "
        f"correct ONLY when the duty applies to this company verbatim with no scope "
        f"change. Otherwise: `narrowed: <the surface/role/system it is scoped to> — "
        f"because <a fact from the intake>`. Use `flagged: <question>` when the answer "
        f"depends on something not yet reviewed (an unreviewed contract, an unstated "
        f"scale). Calibration test: would this row read exactly the same for a different "
        f"company of your size? If yes, you have not calibrated it — it is `narrowed` or "
        f"`flagged`. A micro-enterprise almost never satisfies a duty that presupposes "
        f"dedicated infrastructure, in-house staff or a board: those narrow to a "
        f"contractual-confirmation duty on the supplier, or to a question. `unchanged` "
        f"belongs to the minority of rows that need no scoping at all. "
        f"Nothing else."
    )


# EXP-04 arm: the same slot, offered as a closed 3-value MENU with no decision
# procedure behind it. This is the "before" condition the 2026-10-03 EXP-01
# measured once against the rule above (1 -> 17 `narrowed`). The original
# v1.4.0 ficha text was never committed to git, so the arm is reconstructed here
# as a controlled, versioned pair rather than recovered: what is varied is the
# presence of the calibration procedure, not any other wording.
P4_ADJUSTMENT_MENU = (
    "ADJUSTMENT — pick exactly one of three values: `unchanged — fits as stated` | "
    "`narrowed: <what> — because <company fact>` | `flagged: <open question>`. "
    "Choose the value that best describes this row. Nothing else."
)
P4_ADJUSTMENT_VARIANTS = {"menu": P4_ADJUSTMENT_MENU}

#: variant name -> replacement block. Selected per run via config.json
#: `ficha_overrides: {"p4_adjustment": "<name>"}` (see runconfig.DEFAULTS).
#: Absent/unknown => the decision rule above, which is the shipped behaviour.


def _p4_instruction(sd_id: str, subso_ids: list[str] | None = None,
                    adjustment_variant: str | None = None) -> str:
    """p4_extra_instruction with the EXP-04 adjustment slot swapped.

    Kept as a wrapper so the production path (`p4_extra_instruction`) is
    byte-identical to before when no override is set — the ablation must change
    exactly one thing.
    """
    base = p4_extra_instruction(sd_id, subso_ids)
    if not adjustment_variant:
        return base
    replacement = P4_ADJUSTMENT_VARIANTS.get(adjustment_variant)
    if replacement is None:
        return base
    head, sep, _tail = base.partition("ADJUSTMENT — a decision rule, not a menu.")
    if not sep:
        return base
    return f"{head}{replacement}"


# --------------------------------------------------------------------------
# deterministic assembly of the deliverable (Doc02 case format)
# --------------------------------------------------------------------------

def _hl_goal(repo: Path, sd_id: str) -> str:
    """The regulation-neutral Baseline Goal paragraph, verbatim from the corpus."""
    return " ".join(objective_paragraph(domain_dir(repo, sd_id)).split())


def _cell(v: str) -> str:
    return " ".join(str(v).split())


def _run_identity(run_dir: Path) -> str:
    """run_id and mode of the run that is assembling this document."""
    mf = run_dir / "manifest.json"
    if not mf.exists():
        return run_dir.name
    try:
        m = json.loads(mf.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return run_dir.name
    return f"{m.get('run_id', run_dir.name)} ({m.get('mode', 'pipeline')})"


def assemble_doc(repo: Path, run_dir: Path, case: dict) -> str:
    """Deterministic assembly of doc02_adjusted_goals.md (Doc02 case format).

    §0/§1 static template text; §2 the p3f framing table; §3 per sub-domain:
    HL goal (corpus, verbatim) + the goal table from the L0-validated JSONs
    with Regulation and Control Anchors DERIVED by code; §4 the p4t tension
    resolutions (None for mono-regulation runs); §5 the deterministic Track B
    matrix; §6 the NIST control tables derived from the mapping store +
    CONTROLS referential."""
    import datetime as _dt
    steps_dir = run_dir / "steps"
    fact = parse_simple_yaml((steps_dir / "fact_sheet.yaml").read_text(encoding="utf-8"))
    selection = json.loads((steps_dir / "selection.json").read_text(encoding="utf-8"))
    confirmed = confirmed_regulations(run_dir)
    sel_ids = sorted(s["id"] for s in selection["selected"])
    names = {s["id"]: s["name"] for s in selection["selected"]}
    framing = (steps_dir / "framing.md").read_text(encoding="utf-8").strip()
    tpath = steps_dir / "tensions.json"
    tensions = json.loads(tpath.read_text(encoding="utf-8")).get("tensions", []) \
        if tpath.exists() else []
    overrides = parse_overrides(case.get("track_b_overrides"))

    today = _dt.date.today().isoformat()
    n_goals = 0
    goal_blocks: list[str] = []
    for sd in sel_ids:
        jf = steps_dir / "goals" / f"{sd.replace('.', '_')}.json"
        data = json.loads(jf.read_text(encoding="utf-8"))
        gs = data["goals"]
        if not gs:
            goal_blocks.append(
                f"### {sd} — {names[sd]}\n\n"
                f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
                "_None — no Sub-SO for the confirmed regulations in this module._")
            continue
        # one verbatim baseline paragraph per confirmed regulation the module carries
        regs_present = sorted({g["regulation"] for g in gs}, key=REGULATIONS.index)
        baselines = [f"**Regulation baseline — `SG-{sd}.{reg}` ({reg}):** "
                     f"{_cell(sub_so_objective(repo, sd, reg))}" for reg in regs_present]
        rows = []
        for g in gs:
            anchors = goal_anchors(repo, sd, [g["baseline_source"]])
            rows.append(
                f"| `{g['id']}` | {_cell(g['goal'])} | {_cell(g['implication'])} | "
                f"{g['pattern']} | {PROPERTY_LONG[g['property']]} | {g['parent']} | "
                f"{g['regulation']} | {_cell(g['source'])} | "
                f"{', '.join(anchors) if anchors else '—'} | {_cell(g['adjustment'])} |")
        n_goals += len(rows)
        goal_blocks.append(
            f"### {sd} — {names[sd]}\n\n"
            f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
            + "\n\n".join(baselines) + "\n\n"
            f"| AG ID | Adjusted Goal | Company implication | Pattern | Property "
            f"| Parent Goal | Regulation | Articles | Control Anchors | Adjustment |\n"
            f"|---|---|---|---|---|---|---|---|---|---|\n"
            + "\n".join(rows))

    if len(confirmed) >= 2 and tensions:
        t_parts = [f"### {t['id']} ({t['subdomains']}) — {_cell(t['tension'])}\n\n"
                   f"**Conflict:** {_cell(t['conflict'])}\n\n"
                   f"**Resolution:** {_cell(t['resolution'])}" for t in tensions]
        s4 = "\n\n".join(t_parts)
    elif len(confirmed) >= 2:
        s4 = "None — the confirmed regulation pairing surfaces no strategic tension in the corpus."
    else:
        s4 = "None — single-regulation run."

    tb_rows = track_b_rows(fact, sel_ids, overrides)
    s5_table = ("| Sub-Domain | Scale | Inheritability | Priority | Tier | Rationale |\n"
                "|---|---|---|---|---|---|\n"
                + "\n".join(f"| {r['subdomain']} | {r['scale']} | {r['inheritability']} "
                            f"| {r['priority']} | {r['tier']} | {_cell(r['rationale'])} |"
                            for r in tb_rows))

    s6_parts: list[str] = []
    for i, sd in enumerate(sel_ids, 1):
        secs = sd_control_sections(repo, sd, confirmed)
        body = [f"### §6.{i} {sd} — {names[sd]}\n\n_Applicable regulations: "
                f"{', '.join(confirmed)}_"]
        for sec in secs:
            if not sec["rows"]:
                continue
            body.append(f"#### {sec['title']}\n\n"
                        "| Function | Control ID | Description (1-liner) | Path |\n"
                        "|---|---|---|---|\n"
                        + "\n".join(f"| {r['function']} | {r['id']} | {_cell(r['text'])} "
                                    f"| {r['path']} |" for r in sec["rows"]))
        s6_parts.append("\n\n".join(body))

    doc_id = "MVP-P1-DOC02-001"
    parts = [
        f"---\ndocument_id: {doc_id}\ntitle: \"Adjusted Goals per Sub-Domain — "
        f"{case['company_name']}\"\nversion: 0.1\ncreated: {today}\nstatus: DRAFT\n"
        f"input: pipeline/cases/{case['case_id']}/company_input.md\ncorpus: baseline\n"
        # the document declares its own producer: output/ is keyed by company,
        # so two runs of one case export to the same path and the newest
        # silently replaces the oldest
        f"run_id: {_run_identity(run_dir)}\n---\n",
        f"# Adjusted Goals per Sub-Domain — {case['company_name']}",
        "## §0 Document Purpose",
        f"This document is the **Phase 1 Adjusted Goals layer** of the "
        f"{case['company_name']} run — the Fase 0 → Fase 1 exchange of the pipeline "
        f"I/O contract (ADR-004): the frozen corpus **Baseline Goals** (high-level "
        f"goal `SO-D-XX.Y.HL` + per-regulation Sub-SOs) restated against one "
        f"company. It binds every ACTIVE sub-domain to: 1. a **regulatory floor** — "
        f"the corpus Baseline Goals, consumed by reference (§1); 2. a **framing** — "
        f"the company context conditioning every goal (§2); 3. **Adjusted Goals** — "
        f"one company-proportional row per Sub-SO of each confirmed regulation, "
        f"with code-derived control anchors (§3); 4. **resolutions** for the "
        f"strategic tensions surfaced by the confirmed regulation pairings (§4); "
        f"5. a **Track B tier** per sub-domain from the deterministic matrix (§5); "
        f"6. the **NIST controls mapping** per sub-domain (§6).",
        "## §1 Regulatory Floor (corpus, by reference)",
        "The baseline floor for goals is consumed by reference from `baseline/domains/` "
        "and `baseline/MAPPINGS/` per rule R9. The only baseline text reproduced here "
        "is each sub-domain's High-Level Security Goal paragraph and each confirmed "
        "regulation's Sub-SO objective, both verbatim — the rest is by reference.",
        "## §2 Framing (company context conditioning every goal below)",
        framing,
        "## §3 Adjusted Goals",
        "### §3.0 Structure and Interpretation Guide",
        "Each active sub-domain presents:\n"
        "1. **High-Level Security Goal (`SO-D-XX.Y.HL`):** the regulation-neutral "
        "baseline objective, verbatim from the corpus module (`objective.md`).\n"
        "2. **Regulation baseline (`SG-D-XX.Y.<REG>`):** each confirmed regulation's "
        "Sub-SO objective, verbatim from the corpus module — the floor the adjusted "
        "goal restates.\n"
        "3. **Regulation-specific Adjusted Goals:** one row per Sub-SO of each "
        "confirmed regulation, in canonical order (slot 001 = GDPR, 002 = CRA, …), "
        "each with the **Company implication** — what the duty concretely means for "
        "this company.\n"
        "4. **Property:** one protected property per row (Confidentiality, "
        "Integrity, Availability, Privacy Right, Accountability).\n"
        "5. **Control Anchors:** NIST CSF 2.0 ids derived by code from the row's "
        "Baseline source (`source_SR` → mapping store); the full per-axis mapping "
        "lives in §6.\n"
        "6. **Adjustment (closed vocabulary):** `unchanged — fits as stated` | "
        "`narrowed: … — because …` | `flagged: …` — never silently relaxed (R3).",
    ]
    parts.extend(goal_blocks)
    parts.append("## §4 Tensions Resolved")
    parts.append(s4)
    parts.append(f"## §5 Track B Decision Trail ({len(tb_rows)} rows)")
    parts.append(s5_table)
    parts.append("## §6 NIST Controls Mapping")
    parts.extend(s6_parts)
    return "\n\n".join(parts) + "\n"


def build_run_notes(run_dir: Path) -> str:
    """Deterministic RUN_NOTES.md: run meta, §8 evidence plan, gate ledger."""
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    gates = sorted((run_dir / "steps" / "gates").glob("G-P1-*.approved")) \
        if (run_dir / "steps" / "gates").exists() else []
    gate_rows = "\n".join(f"| {g.stem} | approved | {g.read_text(encoding='utf-8').strip().splitlines()[-1][:80]} |"
                          for g in gates)
    n_calls = sum(1 for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()) \
        if (run_dir / "trace.jsonl").exists() else 0
    return f"""# RUN_NOTES — {manifest['run_id']}

## Run meta

| Field | Value |
|---|---|
| Case | {manifest['case_id']} |
| Model | {manifest['model']} |
| LLM calls (trace.jsonl) | {n_calls} |
| Fichas | {', '.join(f"{k}={v}" for k, v in manifest['ficha_versions'].items())} |
| Deliverable | doc02_adjusted_goals.md (DRAFT) |

## SPEC §8 evidence

| # | Item | How verified | Result |
|---|---|---|---|
| 1 | Input contract (5 sections) | validated at P1 (L0 stop condition) | PASS |
| 2 | Confirmed regulation set (§2 verdicts) | validate.py item 2 (verdicts.json) | run locally post-sync |
| 3 | §3 codes exist in corpus | validate.py item 3 | run locally post-sync |
| 4 | AG IDs unique, match selection | validate.py item 4 | run locally post-sync |
| 5 | Regulatory sources resolve (R2a) | validate.py item 5 | run locally post-sync |
| 6 | Control anchors resolve (R2b) | derived by controls.py + validate.py diff | PASS by construction |
| 7 | No statement without input trace | L0 parsers + gate review | human check |
| 8 | Frontmatter complete; DRAFT | assembly (deterministic) | PASS (DRAFT until G-P1-D) |
| 9 | Pattern/property/parent/baseline source/adjustment | validate.py item 9 | run locally post-sync |
| 10 | Document hygiene (R11/R12) | validate.py R12-hygiene + doc_lint scope note | run locally post-sync |

## Human gates

| Gate | State | Note |
|---|---|---|
{gate_rows or "| (none yet) | | |"}
"""


# --------------------------------------------------------------------------
# execution
# --------------------------------------------------------------------------

class StepRunner:
    def __init__(self, repo: Path, run_dir: Path, model: str, base: str,
                 dry_run: bool = False):
        self.repo = repo
        self.run_dir = run_dir
        self.model = model
        self.base = base
        self.dry_run = dry_run
        # Sampler settings come from the run's config.json, never from a literal
        # in this file: the trace records what was sent, and a record that
        # disagrees with the payload makes the run uninterpretable (the failure
        # that produced aegis_git_rev="" and a trace with no seed at all).
        self.config = runconfig.load(run_dir)
        self.temperature = float(self.config.get("temperature", 0.2))
        self.sampler = runconfig.sampler_options(self.config)
        self.case = load_case(repo, self._case_id())
        self.trace = Trace(run_dir)
        self._client: OllamaClient | None = None

    def _case_id(self) -> str:
        manifest_path = self.run_dir / "manifest.json"
        if manifest_path.exists():
            return json.loads(manifest_path.read_text())["case_id"]
        raise ValueError("manifest.json missing — start the run with stage p1")

    def client(self) -> OllamaClient:
        if self._client is None:
            self._client = OllamaClient(self.base)
        return self._client

    def _call(self, step: str, subdomain: str | None) -> None:
        tag = step.replace(":", "_") if subdomain is None else f"p4_{subdomain.replace('.', '_')}"
        seq = self.trace.next_seq()
        extra = ""
        if subdomain is not None:
            sd_dir = domain_dir(self.repo, subdomain)
            confirmed = confirmed_regulations(self.run_dir) if (
                self.run_dir / "steps" / "verdicts.json").exists() else []
            subso_ids = []
            for reg in confirmed:
                rf = sd_dir / "regs" / f"{reg}.md"
                if rf.exists() and f"SG-{subdomain}.{reg}" in rf.read_text(encoding="utf-8"):
                    subso_ids.append(f"SG-{subdomain}.{reg}")
            extra = _p4_instruction(
                subdomain, subso_ids=subso_ids,
                adjustment_variant=(self.config.get("ficha_overrides") or {}).get("p4_adjustment"))
        else:
            extra = EXTRA_INSTRUCTION[step]
            override = (self.config.get("ficha_overrides") or {}).get(f"{step}_instruction")
            if override:
                table = P3_INSTRUCTION_VARIANTS if step == "p3" else None
                if table and override in table:
                    extra = table[override]
        _assert_wrap_instruction(step, extra)
        call = compose_call(self.repo, self.case, self.run_dir, step, subdomain,
                            extra_instruction=extra)
        num_ctx = NUM_CTX[step.split(":")[0]]
        num_predict = NUM_PREDICT[step.split(":")[0]]
        # context budget guard (2026-10-01 job 1963648: D-09.4 pack ate the whole
        # 32K ctx, done_reason=length, empty content). est tokens x1.15 safety
        # (chars/4 underestimates the real tokenizer) + real output budget.
        est_tokens = (len(call["system"]) + len(call["user"])) // 4
        if est_tokens * 1.15 + num_predict + 2000 > num_ctx:
            num_ctx = 65536
        if est_tokens * 1.15 + num_predict + 2000 > num_ctx:
            raise LLMError(f"step {tag}: prompt ~{est_tokens} tokens does not fit "
                           f"even a 64K context — trim the pack")

        in_dir = self.run_dir / "inputs"
        sys_path = in_dir / f"{seq:03d}_{tag}_system.md"
        user_path = in_dir / f"{seq:03d}_{tag}_user.md"
        sys_path.write_text(call["system"], encoding="utf-8")
        user_path.write_text(call["user"], encoding="utf-8")

        record = {
            "seq": seq, "step": tag, "ficha_id": call["ficha"]["id"],
            "ficha_version": call["ficha"]["version"], "model": self.model,
            # the EFFECTIVE num_ctx, after the escalation above, not the policy
            # value in manifest.num_ctx_policy — the two legitimately differ and
            # only this one describes what the model actually saw
            "num_ctx": num_ctx, "num_predict": num_predict,
            "temperature": self.temperature,
            # sampler keys are recorded individually, including as null: "we sent
            # no seed" is a fact about the run, and it is the fact EXP-02 tests
            **{f"sampler_{k}": self.sampler.get(k) for k in runconfig.SAMPLER_KEYS},
            "ts_start": now_iso(), "system_path": str(sys_path),
            "user_path": str(user_path), "system_chars": len(call["system"]),
            "user_chars": len(call["user"]), "est_prompt_tokens": est_tokens,
            "pack_files": call["files"],
        }

        out_dir = self.run_dir / "outputs"
        raw_path = out_dir / f"{seq:03d}_{tag}_response.json"
        out_path = out_dir / f"{seq:03d}_{tag}_output.md"

        if self.dry_run:
            record.update({"status": "dry-run", "ts_end": now_iso(),
                           "latency_s": 0, "response_chars": 0,
                           "output_path": None, "raw_path": None})
            self.trace.append(record)
            return

        client = self.client()
        client.ensure_model_cached(self.model)
        warm = client.warm_up(self.model, num_ctx)
        record["warmup_s"] = round(warm, 1)

        answer, raw = None, None
        for attempt in (1, 2):
            try:
                raw = client.chat(self.model, call["system"], call["user"], num_ctx,
                                  temperature=self.temperature,
                                  num_predict=num_predict, sampler=self.sampler)
                answer = raw.get("message", {}).get("content", "")
                record[f"attempt{attempt}_done_reason"] = raw.get("done_reason")
                if raw.get("done_reason") == "length":
                    # A truncated answer is NOT a valid artifact: it can still
                    # parse as L0 and be stored as the artifact of record
                    # (seq 26 of job 1963538: D-10.1 cut mid-sentence at the
                    # 8192-token cap and passed). Keep it for forensics, then
                    # make it a retryable failure like any other.
                    (out_dir / f"{seq:03d}_{tag}_response_truncated.json").write_text(
                        json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8")
                    (out_dir / f"{seq:03d}_{tag}_output_truncated.md").write_text(
                        answer, encoding="utf-8")
                    record[f"attempt{attempt}_truncated_chars"] = len(answer)
                    raise LLMError(
                        f"response truncated at the num_predict={num_predict} cap "
                        f"(done_reason=length, {raw.get('eval_count')} eval tokens, "
                        f"{len(answer)} chars returned) — answer is incomplete")
                if not answer.strip():
                    raise LLMError("empty response content")
                record[f"attempt{attempt}_latency_s"] = round(raw.get("total_duration", 0) / 1e9, 1)
                record[f"attempt{attempt}_eval_tokens"] = raw.get("eval_count")
                # the tokenizer's own prompt count. est_prompt_tokens is a
                # chars/4 heuristic kept for continuity with older runs; this is
                # the number cost accounting and context-budget decisions need,
                # and it is the one that reveals a pack that actually overflowed.
                record[f"attempt{attempt}_prompt_tokens"] = raw.get("prompt_eval_count")
                break
            except LLMError as e:
                record[f"attempt{attempt}_error"] = str(e)[:500]
                if attempt == 1:
                    call["user"] += (f"\n\nNOTE: your previous response could not be used "
                                     f"({e}). Answer again, complete and correct.")
        if answer is None:
            record.update({"status": "failed", "ts_end": now_iso(),
                           "output_path": None, "raw_path": None})
            self.trace.append(record)
            raise LLMError(f"step {tag}: both attempts failed; forensics in {in_dir}")

        raw_path.write_text(json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8")
        out_path.write_text(answer, encoding="utf-8")
        record.update({"response_chars": len(answer),
                       "est_output_tokens": raw.get("eval_count"),
                       "raw_path": str(raw_path), "output_path": str(out_path)})

        # L0 validation with one repair retry
        try:
            parsed = self._validate(step, answer, subdomain)
        except (ValueError, KeyError) as e:
            record["l0_first_error"] = str(e)[:500]
            # The repair must be a repair, not a rewrite. "Return the corrected
            # answer" alone was read as "write it all again, thoroughly": on
            # p4_D-03_2 of run_sec03_p1_1979371 (job 1979981) qwen3.8 answered
            # 843 tokens, was told one row was a 93% near-verbatim copy of the
            # Sub-SO, and returned 12,500 tokens — 15x the original — which hit
            # the num_predict cap with the closing fence unwritten and killed
            # the run. The diagnosis was right and the answer was otherwise
            # sound; the repair destroyed it.
            retry_user = (call["user"] + f"\n\nNOTE: your previous answer failed the output "
                          f"contract validation: {e}.\n"
                          f"Re-emit the SAME answer with only that defect corrected. "
                          f"Every other row, id, citation and adjustment record stays "
                          f"exactly as you wrote it. Do not add material, do not restate "
                          f"the baseline, do not elaborate — the answer must come out "
                          f"the same length or shorter, in the same fenced format.")
            try:
                raw2 = client.chat(self.model, call["system"], retry_user, num_ctx,
                                   temperature=self.temperature,
                                   num_predict=num_predict, sampler=self.sampler)
                answer2 = raw2.get("message", {}).get("content", "")
                record["l0_retry_done_reason"] = raw2.get("done_reason")
                if raw2.get("done_reason") == "length":
                    raise LLMError(
                        f"L0 repair response truncated at the num_predict={num_predict} "
                        f"cap (done_reason=length, {raw2.get('eval_count')} eval tokens)")
                if not answer2.strip():
                    raise LLMError("L0 repair response was empty")
                retry_out = out_dir / f"{seq:03d}_{tag}_output_attempt2.md"
                retry_out.write_text(answer2, encoding="utf-8")
                record["retry_output_path"] = str(retry_out)
                parsed = self._validate(step, answer2, subdomain)
                answer, raw = answer2, raw2
                # `raw_path`/`response_chars` must describe the answer that
                # was ACCEPTED, not the one L0 rejected — otherwise the trace
                # points at forensics that contradict steps/
                retry_raw = out_dir / f"{seq:03d}_{tag}_response_attempt2.json"
                retry_raw.write_text(json.dumps(raw2, indent=1, ensure_ascii=False),
                                     encoding="utf-8")
                record["accepted_raw_path"] = str(retry_raw)
                record["accepted_output_path"] = str(retry_out)
                record["response_chars"] = len(answer2)
                record["est_output_tokens"] = raw2.get("eval_count")
                record["l0_retried"] = True
            except (ValueError, KeyError, LLMError) as e2:
                record.update({"status": "failed", "ts_end": now_iso(),
                               "l0_final_error": str(e2)[:500]})
                self.trace.append(record)
                # Both errors, because the second is often a symptom: a repair
                # that ran past num_predict reports "no fenced block" for a run
                # whose actual defect was a calibration failure on row 3. Naming
                # only the final error is what made job 1979981 look like a
                # format-contract failure instead of a lazy restatement.
                raise LLMError(
                    f"step {tag}: L0 validation failed twice.\n"
                    f"  first:  {e}\n"
                    f"  repair: {e2}\n"
                    f"  forensics in {out_dir} (see trace.jsonl l0_first_error)") from e2

        record.update({"status": "ok", "ts_end": now_iso()})
        self.trace.append(record)
        self._store(step, subdomain, tag, parsed)

    def _validate(self, step: str, answer: str, subdomain: str | None) -> dict:
        if subdomain is not None:
            parsed = parse_p4(answer, subdomain)
            return self._check_p4_quality(parsed, subdomain)
        if step == "p3":
            cands = [c["id"] for c in
                     __import__("compose").candidate_subdomains(self.repo, confirmed_regulations(self.run_dir))]
            return parse_p3(answer, cands)
        return PARSERS[step](answer)

    def _check_p4_quality(self, parsed: dict, sd_id: str) -> dict:
        return check_p4_quality(self.repo, self.run_dir, parsed, sd_id)

    def _store(self, step: str, subdomain: str | None, tag: str, parsed: dict) -> None:
        store_parsed(self.run_dir, step, subdomain, parsed)

    # ---- public stage API -------------------------------------------------

    def stage_p1(self) -> int:
        self._call("p1", None)
        return 1

    def stage_p2(self) -> int:
        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        self._call("p2", None)
        return 1

    def stage_p3(self) -> int:
        self._require(("steps/verdicts.json",), "G-P1-B")
        self._call("p3", None)
        return 1

    def stage_p3f(self) -> int:
        self._require(("steps/verdicts.json",), "G-P1-B")
        self._call("p3f", None)
        return 1

    def stage_p4(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        done = 0
        for sd_id in order:
            if (self.run_dir / "steps" / "goals" / f"{sd_id}.md").exists():
                print(f"[p4] {sd_id} already done (validated artifact on disk) — skipping", flush=True)
                continue
            print(f"[p4] sub-domain {sd_id}", flush=True)
            self._call(f"p4:{sd_id}", sd_id)
            done += 1
        return done

    def stage_p4t(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        confirmed = confirmed_regulations(self.run_dir)
        if len(confirmed) < 2:
            (self.run_dir / "steps" / "tensions.json").write_text(
                json.dumps({"tensions": []}, indent=1, ensure_ascii=False),
                encoding="utf-8")
            print("[p4t] single-regulation run — no tensions call needed", flush=True)
            return 0
        self._call("p4t", None)
        return 1

    def stage_p5(self) -> int:
        """Zero-LLM assembly: Doc02 deliverable from validated artifacts +
        code-derived controls/tiers, then L1 validation and export."""
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        goals = sorted((self.run_dir / "steps" / "goals").glob("D-*.md"))
        if not goals:
            raise ValueError("no P4 goal artifacts found — run stage p4 first")
        doc = assemble_doc(self.repo, self.run_dir, self.case)
        (self.run_dir / "doc02_adjusted_goals.md").write_text(doc, encoding="utf-8")
        (self.run_dir / "RUN_NOTES.md").write_text(build_run_notes(self.run_dir),
                                                   encoding="utf-8")
        if not self.dry_run:
            self._finalize_p5()
        return 0

    def _finalize_p5(self) -> None:
        """Post-assembly gate: L1 validation runs NOW (before G-P1-D), and the
        deliverable is exported to the repo's output/<company>/ convention."""
        import validate as validate_mod
        # the manifest's call counter is updated by run_pipeline AFTER the stage
        # returns — bring it current before validating trace consistency
        update_manifest(self.run_dir, n_calls_total=count_calls(self.run_dir))
        findings = validate_mod.validate_run(self.repo, self.run_dir)
        if findings:
            raise ValueError(
                f"post-assembly L1 validation failed with {len(findings)} finding(s) "
                f"(doc02_adjusted_goals.md kept on disk for forensics): {findings}")
        # one export directory per RUN: output/ keyed only by company means two
        # runs of one case overwrite each other and the newest silently wins
        out_dir = (Path(os.environ.get("AEGIS_EXPORT_DIR", str(self.repo / "output")))
                   / self.case["company_id"] / self.run_dir.name)
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(self.run_dir / "doc02_adjusted_goals.md",
                    out_dir / "doc02_adjusted_goals.md")
        shutil.copy(self.run_dir / "RUN_NOTES.md", out_dir / "RUN_NOTES.md")
        print(f"[p5] L1 validation PASS; deliverable exported to {out_dir}", flush=True)

    def _require(self, relpaths: tuple[str, ...], gate: str) -> None:
        for rel in relpaths:
            if not (self.run_dir / rel).exists():
                raise ValueError(f"stage prerequisite missing: {rel} "
                                 f"(earlier stage not run or gate {gate} not approved)")
        gate_path = self.run_dir / "steps" / "gates" / f"{gate}.approved"
        if not gate_path.exists():
            raise ValueError(
                f"human gate {gate} not approved: create "
                f"steps/gates/{gate}.approved (with the review note) after local review, "
                f"then re-sync this run directory to the cluster.")
