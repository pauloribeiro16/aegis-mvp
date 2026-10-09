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
                     p4t_blocks, sub_so_objective)
from controls import (goal_anchors, parse_overrides, sd_control_sections,
                      track_b_rows)
import quality
import runconfig
from llm import LLMError, OllamaClient
from phase2 import PRINCIPLE_IDS
from trace import Trace, count_calls, now_iso, update_manifest

NUM_CTX = {"p1": 16384, "p2": 16384, "p3": 32768, "p3f": 16384, "p4": 32768,
           "p4t": 32768, "p2o": 32768, "p2d": 32768}
# output budget per step (P4 tables are the largest model output)
# P4 emits a 9-column table for every Sub-SO of a module: at 8192 the answer
# was truncated mid-table and the L0 repair hit the same cap (job 1969983,
# D-08.3). The budget is the table, not a sentence.
# p2d emits 7 JSON objects of three prose fields — roughly a tenth of a P4
# table, and the whole answer must land in one block, so 4096 has headroom.
NUM_PREDICT = {"p1": 4096, "p2": 2048, "p3": 12288, "p3f": 2048, "p4": 16384,
               "p4t": 4096, "p2o": 4096, "p2d": 4096}

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

# The goal table has two shapes and exactly one written-down source: the EMIT
# shape, which is what the model writes and what `parse_p4` validates. The
# DELIVERED shape is derived from it, because two of its columns are filled by
# code from the mapping store and the model is explicitly forbidden to emit them
# (`_p4_instruction`): `Regulation` comes off `Baseline source`, `Regulatory
# source` is rendered as `Articles`, and `Control Anchors` is spliced in front
# of `Adjustment`.
#
# These shapes used to be written out by hand in four places — the p4 wrapper
# instruction, the L0 error message, the assembler's header row and template §3
# — and commit c2745f6 migrated two of them and left the others: the prompt was
# left showing a worked example whose shape its own gate rejected, on the two
# columns where they disagreed most. `test_goal_columns_antidrift.py` fails if
# they ever drift apart again.
GOAL_COLUMNS_EMIT = (
    "ID", "Adjusted goal", "Company implication", "Pattern", "Property",
    "Parent goal", "Baseline source", "Regulatory source", "Adjustment",
)
GOAL_COLUMNS_DOC = (
    "AG ID", "Adjusted Goal", "Company implication", "Pattern", "Property",
    "Parent Goal", "Regulation", "Articles", "Control Anchors", "Adjustment",
)


def goal_table_header(columns: tuple[str, ...] = GOAL_COLUMNS_DOC) -> str:
    """A markdown table's header row plus its separator, from a column list."""
    return f"| {' | '.join(columns)} |\n" + f"|{'|'.join('---' for _ in columns)}|"


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
        if len(cells) != len(GOAL_COLUMNS_EMIT):
            raise ValueError(
                f"goal row {gid} has {len(cells)} columns, expected "
                f"{len(GOAL_COLUMNS_EMIT)} ({' | '.join(GOAL_COLUMNS_EMIT)}) — "
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


def parse_p4t(answer: str, sd_id: str | None = None) -> dict:
    """Tension resolutions: a 5-column table, or the single line `None.`.

    `sd_id` is the sub-domain whose call produced this answer (ADR-012 D1 makes
    p4t one call per sub-domain). It does not relax the contract: the ID column
    must still be sequential from T-001, because that is the only cross-row
    invariant in the p4t step — there is no coverage gate over the tension list
    and no peer-similarity gate to satisfy, so a per-call answer is exactly as
    checkable as the monolithic one was. What the global numbering is FOR is the
    merge, which renumbers across the whole selection.

    Each answer is stored as its own slice under `steps/tensions/<sd>.*`, so a
    row is attributable to the call that produced it without the row itself
    carrying a provenance key: `tensions.json` keeps EXACTLY the shape
    assemble_doc and validate.py have always read (agent/tools.py's
    `submit_tensions` writes the same file through the same parser).
    """
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
            raise ValueError(f"tension IDs must be sequential from T-001: got {idm.group(1)}"
                             + (f" (sub-domain {sd_id})" if sd_id else ""))
        for i, name in ((2, "Tension"), (3, "Conflict"), (4, "Resolution")):
            if not cells[i].strip():
                raise ValueError(f"empty {name} cell on {idm.group(1)}")
        tensions.append({"id": idm.group(1), "subdomains": cells[1],
                         "tension": cells[2], "conflict": cells[3],
                         "resolution": cells[4]})
    if not tensions:
        raise ValueError("no T-NNN rows and no `None.` marker in the p4t answer"
                         + (f" (sub-domain {sd_id})" if sd_id else ""))
    return {"md": md, "tensions": tensions}


#: Column order of the merged §4 table, identical to the ficha's Output schema
#: (PROM-P1-07) and to the header the monolithic answer used to carry.
P4T_HEADER = "| ID | Sub-domains | Tension | Conflict | Resolution |"
P4T_SEPARATOR = "|---|---|---|---|---|"


def merge_tensions(per_sd: list[dict]) -> dict:
    """Renumber the per-sub-domain p4t answers into one `T-NNN` sequence.

    ADR-012 D1: p4t is one call per selected sub-domain, so each answer numbers
    its own rows from T-001 and the ids are only unique WITHIN a call. The
    merged artifact is what p5/assemble_doc and validate.py read, and they key
    on the id sequence, so the sequence is renumbered here — over the selection
    in canonical sub-domain order, which is the order the monolithic pack
    presented the blocks in, so a reader sees the same row order as before.

    `per_sd` is the list of stored per-sub-domain artifacts
    (`{"subdomain": …, "tensions": [...]}`), in that canonical order. The return
    value has the same shape `parse_p4t` returns, so `store_parsed` writes
    `steps/tensions.md` / `steps/tensions.json` exactly as the monolithic step
    did. `md` is RENDERED rather than copied from a model answer, which is
    deliberate: the merged table is the only place the global numbering exists,
    so the renderer and the renumberer must be the same code path. The rendered
    table round-trips through `parse_p4t`, which is how the merge is verified.

    Nothing is deduplicated. Two sub-domains that surface the same conflict
    produce two rows with different ids: that is what the corpus said, and
    dropping one would be a silent content loss dressed as cleanup. The row
    shape is untouched too, so `store_parsed` writes `steps/tensions.md` /
    `steps/tensions.json` exactly as the monolithic step did.
    """
    rows: list[dict] = []
    for entry in per_sd:
        rows.extend(dict(t) for t in entry.get("tensions", []))
    for i, t in enumerate(rows, 1):
        t["id"] = f"T-{i:03d}"
    if not rows:
        # the same marker the monolithic answer used, so parse_p4t accepts the
        # merged artifact and assemble_doc/validate see the shape they always did
        md = "None."
    else:
        md = "\n".join([P4T_HEADER, P4T_SEPARATOR] + [
            f"| {t['id']} | {_cell(t['subdomains'])} | {_cell(t['tension'])} | "
            f"{_cell(t['conflict'])} | {_cell(t['resolution'])} |" for t in rows])
    return {"md": md, "tensions": rows, "assumptions": []}


P2D_FIELDS = ("constraint", "method_lead", "eval_scope")


def parse_p2d(answer: str) -> dict:
    """The 7 secure-design principles, as a strict JSON list.

    The one generative step in Phase 2 (ADR-013 D2). L0 is deliberately
    unforgiving: exactly 7 objects, the canonical ids, in order, no duplicates,
    no missing field. A principle dropped "because it does not activate" is a
    silent loss dressed as judgement — the ficha tells the model to say so
    inside the constraint instead.
    """
    import json as _json

    raw = extract_fenced(answer, "json").strip()
    data = _json.loads(raw)
    rows = data.get("principles") if isinstance(data, dict) else data
    if not isinstance(rows, list):
        raise ValueError("p2d: expected a list under 'principles'")
    if len(rows) != 7:
        raise ValueError(f"p2d: expected exactly 7 principles, got {len(rows)}")
    seen = set()
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            raise ValueError(f"p2d: principle {i} is not an object")
        pid = str(r.get("id", "")).strip()
        if pid not in PRINCIPLE_IDS:
            raise ValueError(f"p2d: principle {i} has id {pid!r}, not one of "
                             f"{PRINCIPLE_IDS}")
        if pid in seen:
            raise ValueError(f"p2d: {pid} appears more than once")
        seen.add(pid)
        for f in P2D_FIELDS:
            if not str(r.get(f, "") or "").strip():
                raise ValueError(f"p2d: {pid} has an empty {f!r}")
    missing = [p for p in PRINCIPLE_IDS if p not in seen]
    if missing:
        raise ValueError(f"p2d: no row for {', '.join(missing)}")
    return {"principles": rows}


def parse_p2o(answer: str) -> dict:
    import phase2 as _p2
    return _p2.parse_p2o(answer)


PARSERS = {"p1": parse_p1, "p2": parse_p2, "p3": parse_p3, "p3f": parse_p3f,
           "p4t": parse_p4t, "p2o": parse_p2o, "p2d": parse_p2d}


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
    elif step.startswith("p2o") or step == "p2o":
        p2_dir = steps_dir / "phase2"
        p2_dir.mkdir(exist_ok=True)
        fname = subdomain.replace(".", "_") if subdomain else "unknown"
        (p2_dir / f"{fname}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8")
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
    elif step == "p2d":
        (steps_dir / "principles.json").write_text(
            json.dumps({"principles": parsed["principles"]}, indent=1, ensure_ascii=False),
            encoding="utf-8")


def store_tension_slice(run_dir: Path, sd_id: str, parsed: dict) -> None:
    """One sub-domain's p4t answer, kept apart until the merge renumbers it.

    `steps/tensions.<ext>` is the artifact of record for p5/validate; the
    per-sub-domain slices are its INPUTS and live beside it under
    `steps/tensions/`. Keeping them is what makes the stage resumable (a
    sub-domain that failed is retried on the next invocation, a sub-domain that
    succeeded is not re-asked) and what makes every row of the merged table
    attributable to the call that produced it.
    """
    d = run_dir / "steps" / "tensions"
    d.mkdir(exist_ok=True)
    (d / f"{sd_id}.md").write_text(parsed["md"] + "\n", encoding="utf-8")
    (d / f"{sd_id}.json").write_text(
        json.dumps({"subdomain": sd_id, "tensions": parsed["tensions"]},
                   indent=1, ensure_ascii=False), encoding="utf-8")


def load_tension_slices(run_dir: Path, sd_ids: list[str]) -> list[dict]:
    """The per-sub-domain p4t slices that exist, in canonical sub-domain order."""
    d = run_dir / "steps" / "tensions"
    return [json.loads((d / f"{sd}.json").read_text(encoding="utf-8"))
            for sd in sd_ids if (d / f"{sd}.json").exists()]


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
    all_findings = []
    for g in goals:
        peers = other + [o["implication"] for o in goals
                         if o["id"] != g["id"]]
        findings = quality.run_row(g, baselines, sources, peers)
        if findings:
            all_findings.extend(f"{g['id']}: {m}" for m in findings)
    if all_findings:
        raise ValueError("; ".join(all_findings))
    coverage = quality.check_subso_coverage(goals, expected_regs)
    if coverage:
        raise ValueError("; ".join(coverage))
    return parsed


EXTRA_INSTRUCTION = {
    "p1": "Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.",
    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),
    "p2o": ("Wrap your answer: return ONLY one ```json fenced block shaped "
            "{\"subdomain\": \"...\", \"operational_translation\": \"...\", "
            "\"objectives\": [ ... ]}. No text before or after the block."),
    # p2d is one call per run, and every one of the 7 rows has to survive as one
    # JSON object or L0 rejects the whole answer. "Only" matters more here than
    # anywhere else in the pipeline: a prose preamble is the cheapest way to lose
    # the block, and the repair round costs a whole call.
    "p2d": ("Wrap your answer: return ONLY one ```json fenced block shaped "
            "{\"principles\": [ ... 7 objects ... ]}, each object with exactly the "
            "keys \"id\", \"constraint\", \"method_lead\", \"eval_scope\". The seven "
            "ids must be PRIN-ENG-01 through PRIN-ENG-07 in order, each appearing "
            "exactly once. No text before or after the block."),
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


def p4t_extra_instruction(sd_id: str) -> str:
    """The p4t wrap instruction, scoped to ONE sub-domain (ADR-012 D1).

    The shipped whole-selection instruction above is the reference text; this
    is the same contract narrowed to a single call, and the two differences are
    load-bearing rather than cosmetic:

    * SCOPE. The pack carries this sub-domain's Emergent-tensions sections and
      no other, so a tension the model cannot quote from the attached text does
      not exist for this call. Stating that keeps R8 (no invented obligation)
      checkable against the pack instead of against memory.
    * NUMBERING. The ID column restarts at T-001 per sub-domain and the merged
      artifact renumbers the whole set. Without that sentence a model that
      reasons globally would emit T-004 first and fail a check it cannot see.

    The `None.` path is unchanged and is a real answer, not a skip: the
    sub-domain's corpus tensions were read and none of them activates.
    """
    return (
        f"Wrap your answer: return ONLY one ```markdown fenced block containing the "
        f"tension-resolution table `| ID | Sub-domains | Tension | Conflict | "
        f"Resolution |`, one row per tension of THIS sub-domain that activates on this "
        f"company, or ONLY the line `None.` inside the fence when none of them does. "
        f"SCOPE: this call resolves sub-domain {sd_id} alone — the attached pack carries "
        f"the Emergent-tensions sections of that sub-domain and no other, and every "
        f"selected sub-domain is resolved in its own call. Column rules: `Sub-domains` "
        f"cites the canonical id `{sd_id}` (R1); `ID` restarts at `T-001` and runs "
        f"sequentially, because the delivered table renumbers the whole set at merge — a "
        f"gap or a number above 001 here is a defect. `Tension` names the conflict "
        f"concisely, `Conflict` states which duties collide and on what operational "
        f"dimension (clock, recipient, scope, competence), `Resolution` adopts ONE "
        f"auditable binding rule for this company (e.g. strictest timeline binds per "
        f"recipient; parallel recipients keep their own clocks) — never `TBD`. Skip a "
        f"corpus tension whose triggering condition does not hold for this company: that "
        f"is not a silent drop, it does not activate. Technology-neutral (R5); no "
        f"obligation invented beyond the corpus tensions the pack quotes (R8). "
        f"Nothing else."
    )


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
        f"(a) the heading `### {sd_id} — <canonical name>` and the "
        f"{len(GOAL_COLUMNS_EMIT)}-column goal table "
        f"(`{' | '.join(GOAL_COLUMNS_EMIT)}`), and (b) a heading `## §5` "
        f"listing only `> ASSUMPTION:` blockquotes and open questions this sub-domain owes "
        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "
        f"TERMINATION: after the `## §5` section the answer is COMPLETE — emit the "
        f"closing fence on the next line and stop. No table continuation, no notes, no "
        f"second §5, no text of any kind after the closing fence; an answer that keeps "
        f"writing past §5 hits the output cap and is discarded whole. Column rules: this module "
        f"declares EXACTLY {len(subso_ids)} Sub-SO(s) to restate — "
        f"{', '.join(subso_ids)} — and no others; write one row per listed id, in that "
        f"order. A regulation NOT in that list has no duty here — EVEN IF it is confirmed "
        f"for the company and even if its module file exists: 28 of the 38 sub-domains "
        f"carry an AI_Act file that is only a stub, ending in '(no AI Act Sub-SO or "
        f"requirements in this sub-domain)'. A stub is not a card; writing a row citing "
        f"a regulation absent from the list above is a hard failure (R8), and the stub "
        f"is exactly the trap. Adjusted goal = a declarative, normative security goal restating that Sub-SO's "
        f"Objective (2+ sentences, same obligation content). DO NOT prepend the company name "
        f"(do NOT write '<Company> shall...' or '<Company> must...'). Do NOT paste or embed the "
        f"Sub-SO Objective verbatim as a sentence (do not copy the baseline and append company calibration) — "
        f"reformulate the duty in the company's sentence structure, keeping roughly half the Sub-SO's vocabulary. "
        f"Express the goal objectively and impersonally, as a property the system holds rather than as an instruction issued "
        f"by someone; "
        f"Company implication = what this duty concretely means for THIS company given "
        f"the §2 framing and fact sheet (1-2 sentences explaining operational impact, roles and scope); "
        f"Baseline source = the single corpus Sub-SO id the row restates "
        f"(e.g. `SG-{sd_id}.GDPR`); Property MUST be one of C, I, A, privacy-right, "
        f"accountability. Control anchors are derived by code — do NOT emit any. "
        f"ADJUSTMENT — provide the substantive proportionality justification for THIS duty "
        f"(e.g. 'inherited from supplier-managed hosting under shared responsibility', 'role separation "
        f"achieved via platform IAM roles rather than disjoint full-time personnel', 'minimum 5-year support "
        f"period applies unconditionally per statutory floor'), or use badge `proportional: <rationale>` / "
        f"`inherited: <supplier>` / `flagged: <question>` / '—' if it applies directly under the §2 general "
        f"framing without duty-specific deviations. Do not paste empty 'unchanged' labels without rationale. "
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
P4_ADJUSTMENT_BADGES = (
    "ADJUSTMENT — choose exactly one classification badge: `verbatim` | `proportional` | `inherited` | `flagged`. "
    "Do NOT append explanations here — the justification belongs entirely in the Company implication column. Nothing else."
)
P4_ADJUSTMENT_VARIANTS = {"menu": P4_ADJUSTMENT_MENU, "badges": P4_ADJUSTMENT_BADGES}


# ---------------------------------------------------------------------------
# M09 arm: the STYLE TAIL of the p4 instruction, with its literal exemplars
# replaced by structural criteria.
#
# The shipped tail shows three verbatim goal sentences and three verbatim
# adjustment rationales, all of them drawn from the same corpus the model is
# being asked to restate. That is a compliance requirement encoded outside the
# output contract — the thing S-296 names as the wrong place for it — and it
# points at the failure M07 measured: the reference reached a 0.99
# (unchanged+verbatim) ratio with zero `proportional` and zero `inherited`
# rows. Whether the exemplar TEXT or the instruction TEXT drives that is the
# question M09 exists to answer, so the arm removes the literal exemplars and
# keeps every other word of the instruction identical.
#
# The replacement spans from the goal-style marker to the end of the string:
# both example sets live there and nothing else does, so one partition swaps
# both and leaves the wrap instruction, the TERMINATION clause, the column
# contract and the Sub-SO enumeration byte-identical.
P4_STYLE_MARKER = "Express the goal objectively and impersonally"

P4_STYLE_META = (
    "Express the goal objectively and impersonally: state the duty that must hold "
    "across this entity's operational scope, keeping the Sub-SO's own obligation "
    "vocabulary but rebuilt into this company's sentence structure. Do not paste the "
    "baseline — a goal that is a near-verbatim copy of the Sub-SO objective restates "
    "nothing about this company and is rejected. "
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences explaining operational impact, roles "
    "and scope); Baseline source = the single corpus Sub-SO id the row restates "
    "(e.g. `SG-{sd_id}.GDPR`); Property MUST be one of C, I, A, privacy-right, "
    "accountability. Control anchors are derived by code — do NOT emit any. "
    "ADJUSTMENT — record the decision this duty forces on THIS company and the reason "
    "behind it: whether the duty holds as the baseline states it, is narrowed by a "
    "company fact you can name, or cannot be decided from the input. Justify "
    "proportionality against the §2 framing — the company's scale, its operational "
    "roles, and which capabilities it inherits from others — and never paste a label "
    "without the reasoning behind it. Nothing else."
)

#: variant name -> replacement style tail. Selected per run via config.json
#: `ficha_overrides: {"p4_instruction": "<name>"}`. Absent/unknown => the shipped
#: text above, which is the production path.
P4_STYLE_VARIANTS = {"meta": P4_STYLE_META}

# ---------------------------------------------------------------------------
# M10 intervention: the Company implication column, not the goal.
#
# M10 measured the two columns separately against a cross-sectional placebo
# (same model, same company, a genuinely different duty), inside the M07 matrix
# so the instrument is constant:
#
#     Adjusted goal        cross-company 0.249  placebo 0.061  -> +0.188
#     Company implication  cross-company 0.062  placebo 0.061  -> +0.002
#
# The goal text carries the company. The implication — the one column that
# exists to carry it, and the one `check_implication_specific` guards — is
# indistinguishable from unrelated text. That also explains the 0.99 badge
# without a parser story: `unchanged` is what the model writes when it has
# nothing company-specific to say about a duty.
#
# So the intervention targets that clause alone. It asks for a NAMED, checkable
# artefact from the fact sheet rather than abstract scope language, and it gives
# the model an explicit escape ("the duty is out of scope, say so") so the
# pressure to invent a company fact is not merely relocated.
P4_IMPLICATION_MARKER = (
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences explaining operational impact, "
    "roles and scope)")

P4_IMPLICATION_CONCRETE = (
    "Company implication = what this duty concretely means for THIS company given "
    "the §2 framing and fact sheet (1-2 sentences). Name one checkable artefact "
    "that appears in the fact sheet — a named system, a named supplier, a named "
    "role, a named volume, a named site — and say what this duty does to it. "
    "\"Operational impact, roles and scope\" in the abstract is not an answer: a "
    "sentence that would read the same for a company of any size or sector has "
    "not been written. If no artefact in the fact sheet is touched by this duty, "
    "write that it is not, in one clause, and keep it short")

#: variant name -> replacement clause. Selected per run via config.json
#: `ficha_overrides: {"p4_implication": "<name>"}`.
P4_IMPLICATION_VARIANTS = {"concrete": P4_IMPLICATION_CONCRETE}

#: variant name -> replacement block. Selected per run via config.json
#: `ficha_overrides: {"p4_adjustment": "<name>"}` (see runconfig.DEFAULTS).
#: Absent/unknown => the decision rule above, which is the shipped behaviour.


def _p4_instruction(sd_id: str, subso_ids: list[str] | None = None,
                    adjustment_variant: str | None = None,
                    style_variant: str | None = None,
                    implication_variant: str | None = None) -> str:
    """p4_extra_instruction with the EXP-04 adjustment, M09 style and M10
    implication slots swapped.

    Kept as a wrapper so the production path (`p4_extra_instruction`) is
    byte-identical to before when no override is set — the ablation must change
    exactly one thing.
    """
    base = p4_extra_instruction(sd_id, subso_ids)
    if implication_variant:
        replacement = P4_IMPLICATION_VARIANTS.get(implication_variant)
        if replacement is None:
            raise ValueError(
                f"p4 implication override: unknown variant {implication_variant!r} "
                f"(known: {sorted(P4_IMPLICATION_VARIANTS)})")
        head, sep, _tail = base.partition(P4_IMPLICATION_MARKER)
        if not sep:
            raise ValueError(
                "p4 implication override: the shipped base instruction no longer "
                f"contains the expected marker ({P4_IMPLICATION_MARKER[:48]!r}…) — "
                "refusing to run with a variant that would be silently ignored "
                "(record the instrument, never assume it)")
        base = f"{head}{replacement}" + _tail
    if style_variant:
        replacement = P4_STYLE_VARIANTS.get(style_variant)
        if replacement is None:
            raise ValueError(
                f"p4 instruction override: unknown style variant {style_variant!r} "
                f"(known: {sorted(P4_STYLE_VARIANTS)})")
        head, sep, _tail = base.partition(P4_STYLE_MARKER)
        if not sep:
            raise ValueError(
                "p4 style override: the shipped base instruction no longer contains "
                f"the expected marker {P4_STYLE_MARKER!r} — refusing to run with a "
                "variant that would be silently ignored (record the instrument, "
                "never assume it)")
        base = f"{head}{replacement.format(sd_id=sd_id)}"
    if not adjustment_variant:
        return base
    replacement = P4_ADJUSTMENT_VARIANTS.get(adjustment_variant)
    if replacement is None:
        return base
    # The anchor is the ADJUSTMENT marker of the SHIPPED base text. It moved
    # when the base was rewritten to badge vocabulary ("a decision rule, not a
    # menu" -> "choose exactly one classification badge") and the partition
    # then failed silently — an override run would ship the base unchanged
    # while config.json recorded the variant. m06 (menu) predates that rewrite;
    # anything after it must swap against the current marker or not claim the
    # variant at all.
    head, sep, _tail = base.partition("ADJUSTMENT — choose exactly one classification badge")
    if not sep:
        raise ValueError(
            "p4 adjustment override: the shipped base instruction no longer "
            "contains the expected ADJUSTMENT marker — refusing to run with a "
            "variant that would be silently ignored (record the instrument, "
            "never assume it)")
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
    missing = [sd for sd in sel_ids
               if not (steps_dir / "goals" / f"{sd.replace('.', '_')}.json").exists()]
    for sd in sel_ids:
        jf = steps_dir / "goals" / f"{sd.replace('.', '_')}.json"
        if not jf.exists():
            # Soft fallback: assemble with unvalidated placeholder block rather than
            # aborting the entire run and losing all generated deliverable text.
            goal_blocks.append(
                f"### {sd} — {names[sd]}\n\n"
                f"**High-Level Security Goal (SO-{sd}.HL):** {_cell(_hl_goal(repo, sd))}\n\n"
                f"> **[UNVALIDATED_DRAFT: Stage P4 did not carry this sub-domain — L0 repair failed ({sd})]**\n")
            continue
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
            + goal_table_header() + "\n"
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
        # the step TAG is the forensic key: it names the `inputs/` and `outputs/`
        # files, the trace line, and the resume decision. It is keyed on the step
        # FAMILY plus the sub-domain (`p4:D-01.1` -> `p4_D-01_1`,
        # `p4t:D-04.3` -> `p4t_D-04_3`) so every p4t sub-domain is as
        # attributable as every p4 sub-domain. Keying on the literal "p4" prefix
        # instead would have filed every p4t answer under `p4_*` and made the
        # two indistinguishable in `inputs/`.
        step_kind = step.split(":", 1)[0]
        tag = (f"{step_kind}_{subdomain.replace('.', '_')}" if subdomain is not None
               else step.replace(":", "_"))
        seq = self.trace.next_seq()
        extra = ""
        if step_kind == "p4t":
            extra = p4t_extra_instruction(subdomain)
        elif step_kind == "p2o":
            extra = EXTRA_INSTRUCTION["p2o"]
        elif subdomain is not None:
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
                adjustment_variant=(self.config.get("ficha_overrides") or {}).get("p4_adjustment"),
                style_variant=(self.config.get("ficha_overrides") or {}).get("p4_instruction"),
                implication_variant=(self.config.get("ficha_overrides") or {}).get("p4_implication"))
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
        num_ctx = NUM_CTX[step_kind]
        num_predict = NUM_PREDICT[step_kind]
        # context budget guard (2026-10-01 job 1963648: D-09.4 pack ate the whole
        # 32K ctx, done_reason=length, empty content). est tokens x1.15 safety
        # (chars/4 underestimates the real tokenizer) + real output budget.
        # The ladder doubles like the agent loop's: Case_03's D-07.1 pack is
        # ~42k tokens (5 confirmed regulations), which cleared 64K with the
        # safety margin by 1.4k tokens and died on the guard (job 1980137) —
        # a rung at 131072 covers it with room; beyond that the answer is a
        # pack-composition problem (E-15), not a context problem.
        est_tokens = (len(call["system"]) + len(call["user"])) // 4
        needed = est_tokens * 1.15 + num_predict + 2000
        while needed > num_ctx and num_ctx < 131072:
            num_ctx *= 2

        # ADR-012 D5: the refusal is a MEASURED outcome, not an absence of one.
        # The raise used to sit here — above the `inputs/` write and above the
        # trace record — so an exhausted ladder produced no pack, no trace line
        # and no stage entry, only an exception string that named an estimate
        # and pointed at a mitigation ("trim the pack") which is not the
        # evidence. `PLANO_FECHO.md:124` records a context-fail cell from
        # exactly this state and routes it to E-15, and E-15's traversal pass
        # cannot run on an input that was never written. The decision itself
        # is unchanged — the same estimate, the same 1.15 factor, the same
        # 131072 cap, still a hard refusal — only the forensics come first.
        in_dir = self.run_dir / "inputs"
        # Phase 2 can be run against a Phase 1 run directory whose `inputs/`
        # was never created (a resumed run, or one carried over from an older
        # layout). Every prompt this call composes must land on disk BEFORE any
        # model call, so the directory is created here rather than by `new-run`.
        in_dir.mkdir(parents=True, exist_ok=True)
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

        if needed > num_ctx:
            # `status: context-fail` is the cell label PLANO_FECHO.md:124
            # already uses for this outcome, so the trace is the same record an
            # auditor expects rather than a new vocabulary. `est_prompt_tokens`,
            # `system_chars`, `user_chars`, `pack_files`, `num_ctx` and
            # `num_predict` are the fields a reader needs to place the refusal:
            # how big the pack was, what was in it, what the model would have
            # been asked for, and the ceiling it could not fit under.
            record.update({
                "status": "context-fail", "ts_end": now_iso(),
                "output_path": None, "raw_path": None,
                "context_ladder_cap": 131072,
                "needed_tokens": int(needed),
                "context_fail_error": (
                    f"prompt ~{est_tokens} tokens needs ~{int(needed)} of context "
                    f"(est x1.15 + num_predict={num_predict} + 2000) after the "
                    f"ladder stopped at num_ctx={num_ctx}, above the 131072 cap"),
            })
            self.trace.append(record)
            raise LLMError(f"step {tag}: prompt ~{est_tokens} tokens needs ~{int(needed)} "
                           f"of context, above the 131072 ladder cap — trim the pack "
                           f"(decompose per Sub-SO card; E-15). Refused call recorded "
                           f"in trace.jsonl seq {seq} (status=context-fail); pack kept "
                           f"in {in_dir}")

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
            # Multi-turn repair dialogue: pass previous answer in assistant role
            # and surgical feedback in user role so the model actually sees what to fix.
            messages = [
                {"role": "system", "content": call["system"]},
                {"role": "user", "content": call["user"]},
                {"role": "assistant", "content": answer},
                {"role": "user", "content": (
                    f"NOTE: your previous answer failed the output contract validation: {e}.\n"
                    f"Re-emit the SAME answer with only that defect corrected. "
                    f"Every other row, id, citation and adjustment record stays "
                    f"exactly as you wrote it. Do not add material, do not restate "
                    f"the baseline, do not elaborate — the answer must come out "
                    f"the same length or shorter, in the same fenced format."
                )},
            ]
            try:
                raw2 = client.chat_messages(self.model, messages, num_ctx,
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
        # the step FAMILY routes the parser, not the presence of a sub-domain:
        # both p4 and p4t now take one, and they have different contracts
        if step.startswith("p4t"):
            return parse_p4t(answer, sd_id=subdomain)
        if step.startswith("p2o"):
            return parse_p2o(answer)
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
        # a p4t answer is a SLICE until the merge renumbers it: writing it to
        # steps/tensions.{md,json} per call would make the merged artifact a
        # race between 38 writers and give every sub-domain the whole
        # selection's T-NNN numbering.
        if step.startswith("p4t"):
            store_tension_slice(self.run_dir, subdomain, parsed)
            return
        store_parsed(self.run_dir, step, subdomain, parsed)

    # ---- per-sub-domain fault isolation (ADR-012 D1 / AGENTS.md §-2 rule 4) --

    def _trace_record(self, tag: str) -> dict:
        """The LAST trace line recorded for a step tag, read back from disk.

        The stage summary is assembled from this rather than from the in-memory
        exception so the two records cannot disagree: whatever `trace.jsonl`
        says the L0 failure was, is what the summary reports. A tag with no
        line means the call never reached the trace (a pack-composition error,
        a missing corpus file) — the caller records the exception text then.
        """
        path = self.run_dir / "trace.jsonl"
        if not path.exists():
            return {}
        last: dict = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("step") == tag:
                last = rec
        return last

    def _failure_record(self, tag: str, sd_id: str, err: BaseException) -> dict:
        """One sub-domain's graded failure record.

        A double-L0 failure stays an L0 failure: nothing here relaxes, retries
        or reclassifies it. What changes is that it is no longer the end of the
        stage. AGENTS.md §-2 rule 4 makes a negative result a result, so the
        record carries BOTH L0 strings (the first error is often the real defect
        and the second a symptom of the repair), the sub-domain, the step tag
        and the trace seq to read.
        """
        rec = self._trace_record(tag)
        status = rec.get("status")
        kind = ("context-fail" if status == "context-fail"
                else "L0" if rec.get("l0_final_error")
                else "transport" if rec.get("attempt2_error")
                else "error")
        out = {"subdomain": sd_id, "step": tag, "kind": kind,
               "seq": rec.get("seq"),
               "ts": rec.get("ts_end") or rec.get("ts_start")}
        for key in ("l0_first_error", "l0_final_error", "attempt1_error",
                    "attempt2_error", "est_prompt_tokens", "needed_tokens",
                    "context_ladder_cap", "num_ctx", "num_predict"):
            if rec.get(key) is not None:
                out[key] = rec[key]
        if not rec:
            out["error"] = f"{type(err).__name__}: {err}"[:500]
        return out

    def _write_stage_result(self, stage: str, summary: dict) -> None:
        """Record a stage's GRADED outcome, in the run's own artefacts.

        Three sinks, deliberately redundant, because the consumers differ and
        none of them is guaranteed to read the others:

        * `steps/stage_result.json` — beside the artifacts, survives a run that
          never reaches p5, and is re-read by a resumed stage.
        * `manifest.json` under `stage_result` — travels with the manifest
          through sync_down and is what a matrix row is built from.
        * one canonical stdout line — the run log is the only thing that exists
          even when the run directory is lost.

        `status` is the graded cell: `ok` (everything the stage covers was
        carried), `partial` (a subset failed), `failed` (nothing was carried —
        which raises, so it never gets this far). It is deliberately NOT
        `run_pipeline`'s `stage_history.status`, which records whether the
        sweep itself completed and cannot express 13-of-38.
        """
        rec = dict(summary, stage=stage, ts=now_iso())
        path = self.run_dir / "steps" / "stage_result.json"
        doc: dict = {}
        if path.exists():
            try:
                doc = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                doc = {}
        if not isinstance(doc.get("stages"), dict):
            doc = {"run_id": self.run_dir.name, "stages": {}}
        doc["stages"][stage] = rec
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
        manifest_block = dict(doc["stages"])
        manifest_block["_note"] = (
            "graded per-sub-domain outcome; run_pipeline's stage_history.status "
            "records only whether the sweep completed")
        update_manifest(self.run_dir, stage_result=manifest_block)
        print(f"AEGIS_STAGE_RESULT stage={stage} status={rec['status']} "
              f"carried={rec.get('carried')}/{rec.get('selected')} "
              f"failed={rec.get('failed')} detail={rec.get('summary', '')!r}", flush=True)

    def _raise_if_nothing_carried(self, stage: str, summary: dict,
                                  failed_detail: str) -> None:
        """Total failure raises; partial does not.

        The stage must not report a 0-of-38 run the way it reports a 38-of-38
        one, so `carried == 0` still aborts and takes the process exit code
        with it. A PARTIAL sweep deliberately does not raise: p5 cannot render
        a deliverable that is missing N sub-domains either way, so aborting
        here would destroy the very record the partial outcome is made of. The
        graded cell is carried by the three sinks above instead — that is the
        difference between "delivered 13/38" and "delivered 0/38" being
        distinguishable in the results.
        """
        if summary.get("carried") or self.dry_run:
            return
        raise LLMError(
            f"stage {stage}: no sub-domain produced a validated artifact — "
            f"0/{summary.get('selected')} carried, {summary.get('failed')} failed. "
            f"{failed_detail} Forensics in {self.run_dir / 'inputs'}, "
            f"{self.run_dir / 'outputs'} and steps/stage_result.json")

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

    def _sweep(self, stage: str, order: list[str], done_marker, on_call) -> dict:
        """Run one call per sub-domain, isolating a failure to its sub-domain.

        Both p4 and p4t need the same loop and the same accounting, and the
        accounting is the point: five qwen3.8 runs (jobs 1983224-1983232)
        aborted at `p4_D-03_3` having completed 13 of 38 sub-domains, which the
        M02 matrix — a BINARY cell — could not tell apart from a run that
        completed none. The gates are untouched: a double-L0 failure is still a
        double-L0 failure, still never stored as an artifact, still recorded
        with both error strings. What stops happening is that one sub-domain
        decides the fate of the other 37.

        Resume semantics are the existing ones — a sub-domain with its
        validated artifact on disk is not re-asked — so a resumed run retries
        exactly the sub-domains that failed.
        """
        carried: list[str] = []
        already: list[str] = []
        failures: list[dict] = []
        calls = 0
        for sd_id in order:
            if done_marker(sd_id):
                print(f"[{stage}] {sd_id} already done (validated artifact on disk) — skipping",
                      flush=True)
                already.append(sd_id)
                carried.append(sd_id)
                continue
            print(f"[{stage}] sub-domain {sd_id}", flush=True)
            try:
                on_call(sd_id)
                carried.append(sd_id)
            except (LLMError, ValueError, KeyError) as e:
                rec = self._failure_record(f"{stage}_{sd_id.replace('.', '_')}", sd_id, e)
                failures.append(rec)
                print(f"[{stage}] {sd_id} FAILED ({rec['kind']}) — continuing with the "
                      f"remaining sub-domains: {str(e)[:200]}", flush=True)
            calls += 1
        return {"carried": carried, "already": already, "failures": failures, "calls": calls}

    def stage_p4(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        sw = self._sweep("p4", order,
                         done_marker=lambda sd: (self.run_dir / "steps" / "goals" / f"{sd}.md").exists(),
                         on_call=lambda sd: self._call(f"p4:{sd}", sd))
        n_failed = len(sw["failures"])
        summary = {
            # a dry run composes prompts and writes no artifact, so "carried"
            # there means "the call composed and the context guard passed" —
            # the count is over calls, not over files on disk, and it is
            # labelled as such rather than reported as 0/38
            "status": ("dry-run" if self.dry_run else
                       "ok" if not n_failed else
                       "partial" if sw["carried"] else "failed"),
            "selected": len(order),
            "carried": len(sw["carried"]),
            "already_done": len(sw["already"]),
            "failed": n_failed,
            "calls": sw["calls"],
            "summary": f"{len(sw['carried'])}/{len(order)} carried"
                       + (f", {n_failed} failed (L0)" if n_failed else ""),
            "artifact": "steps/goals/",
            "failed_subdomains": [f["subdomain"] for f in sw["failures"]],
            "failures": sw["failures"],
        }
        self._write_stage_result("p4", summary)
        self._raise_if_nothing_carried(
            "p4", summary,
            "; ".join(f"{f['subdomain']}: {f.get('l0_final_error') or f.get('error', '')}"
                      for f in sw["failures"][:3]))
        return sw["calls"]

    def stage_p4t(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        confirmed = confirmed_regulations(self.run_dir)
        if len(confirmed) < 2:
            (self.run_dir / "steps" / "tensions.json").write_text(
                json.dumps({"tensions": []}, indent=1, ensure_ascii=False),
                encoding="utf-8")
            print("[p4t] single-regulation run — no tensions call needed", flush=True)
            self._write_stage_result("p4t", {
                "status": "ok", "selected": len(load_selection(self.run_dir)["selected"]),
                "eligible": 0, "no_material": 0, "carried": 0, "already_done": 0,
                "failed": 0, "calls": 0, "tensions": 0,
                "summary": "single-regulation run — no tensions call needed",
                "artifact": "steps/tensions.json", "failed_subdomains": [], "failures": []})
            return 0
        # ADR-012 D1: one call per selected sub-domain, over that sub-domain's
        # own Emergent-tensions section. `p4t_blocks` is the single source of
        # truth for which sub-domains carry tension material at all, so the
        # whole-selection view and the per-call views cannot diverge.
        blocks = p4t_blocks(self.repo, self.run_dir)
        eligible = [b["sd_id"] for b in blocks if b["has_tensions"]]
        no_material = [b["sd_id"] for b in blocks if not b["has_tensions"]]
        if no_material:
            print(f"[p4t] no Emergent-tensions section for {len(no_material)} selected "
                  f"sub-domain(s) — no call, no corpus material to rule on: "
                  f"{', '.join(no_material)}", flush=True)
        sw = self._sweep("p4t", eligible,
                         done_marker=lambda sd: (self.run_dir / "steps" / "tensions" / f"{sd}.json").exists(),
                         on_call=lambda sd: self._call(f"p4t:{sd}", sd))
        n_failed = len(sw["failures"])
        n_selected = len(load_selection(self.run_dir)["selected"])
        base = {
            "selected": n_selected,
            "eligible": len(eligible),
            "no_material": len(no_material),
            "no_material_subdomains": no_material,
            "carried": len(sw["carried"]),
            "already_done": len(sw["already"]),
            "failed": n_failed,
            "calls": sw["calls"],
            "summary": f"{len(sw['carried'])}/{len(eligible)} carried"
                       + (f", {n_failed} failed (L0)" if n_failed else "")
                       + (f"; {len(no_material)} of {n_selected} selected sub-domains "
                          f"carry no corpus tension section" if no_material else ""),
            "artifact": "steps/tensions.md (merged) / steps/tensions/ (per sub-domain)",
            "failed_subdomains": [f["subdomain"] for f in sw["failures"]],
            "failures": sw["failures"],
        }
        if not sw["carried"]:
            base["status"] = "failed"
            self._write_stage_result("p4t", dict(base, tensions=0))
            self._raise_if_nothing_carried(
                "p4t", base,
                "; ".join(f"{f['subdomain']}: {f.get('l0_final_error') or f.get('error', '')}"
                          for f in sw["failures"][:3]))
        if self.dry_run:
            # a dry run composed the calls; it must not WRITE the merged
            # artifact, which would replace a real run's tensions.json with the
            # empty result of a sweep that stored nothing
            base["status"] = "dry-run"
            base["tensions"] = None
            self._write_stage_result("p4t", base)
            return sw["calls"]
        # the merge: canonical sub-domain order, T-NNN renumbered across the
        # whole set. Runs whether or not the sweep was partial — a merged
        # artifact built from the sub-domains that DID answer is the only
        # honest §4 available, and the gaps are in the stage record, not hidden
        # inside the table.
        merged = merge_tensions(load_tension_slices(self.run_dir, sw["carried"]))
        store_parsed(self.run_dir, "p4t", None, merged)
        base["status"] = "ok" if not n_failed else "partial"
        base["tensions"] = len(merged["tensions"])
        # the row -> sub-domain map, so a merged row is attributable without
        # replaying the trace (the slices on disk carry the same mapping)
        n, rows_by_sd = 0, []
        for sd in sw["carried"]:
            k = len(load_tension_slices(self.run_dir, [sd])[0].get("tensions", []))
            rows_by_sd.append({"subdomain": sd, "n_rows": k,
                               "ids": [f"T-{i:03d}" for i in range(n + 1, n + 1 + k)]})
            n += k
        base["rows_by_subdomain"] = rows_by_sd
        self._write_stage_result("p4t", base)
        return sw["calls"]

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

    def stage_phase2(self) -> int:
        """Phase 2: Operationalization & Engineering Rules.

        Runs sub-domain operationalization (p2o) across all active sub-domains,
        generating operational translations, ISO 29148 verification methods,
        criteria, and RULE-* catalogue, followed by p2d for the 7 architectural
        principles. Renders Doc01 and Doc02.
        """
        import phase2 as p2

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        if not (self.run_dir / "steps" / "goals").is_dir():
            raise ValueError("no P4 goal artifacts — run stage p4 first")

        rows = p2.build(self.repo, self.run_dir)
        findings = p2.check(rows, self.run_dir)
        if findings:
            raise ValueError(
                f"Phase 2 Doc01 gate failed with {len(findings)} finding(s): {findings}")

        out_dir = self.run_dir / "outputs" / "phase2"
        out_dir.mkdir(parents=True, exist_ok=True)

        active_sds = sorted({r["subdomain"] for r in rows})
        calls = 0
        p2_dir = self.run_dir / "steps" / "phase2"
        p2_dir.mkdir(parents=True, exist_ok=True)

        for sd in active_sds:
            sd_file = p2_dir / f"{sd.replace('.', '_')}.json"
            if sd_file.exists():
                continue
            self._call(f"p2o:{sd}", sd)
            if not self.dry_run:
                calls += 1

        (out_dir / "Doc01_Operational_Objectives.md").write_text(
            p2.render_doc01(self.repo, self.run_dir, rows), encoding="utf-8")

        self._call("p2d", None)
        if not self.dry_run:
            calls += 1
            principles = p2.principles_for(self.run_dir)
            doc2_findings = p2.check_doc02(self.repo, self.run_dir, principles)
            if doc2_findings:
                raise ValueError(
                    f"Phase 2 Doc02 gate failed with {len(doc2_findings)} finding(s): "
                    f"{doc2_findings}")
            ratio = p2.grounding_ratio(principles, p2._fact_sheet(self.run_dir))
        else:
            principles, ratio = p2.principles_for(self.run_dir), 0.0

        (out_dir / "Doc02_Secure_Design_Principles.md").write_text(
            p2.render_doc02(self.repo, self.run_dir, principles), encoding="utf-8")

        op_count = len(list(p2_dir.glob("*.json")))
        unseamed = sum(1 for p in principles
                       if str(p.get("constraint", "")) in ("", p2.UNSET))
        self._write_stage_result("phase2", {
            "status": "ok" if (not self.dry_run and unseamed == 0) else "partial",
            "selected": 7,
            "carried": 7 - unseamed,
            "failed": unseamed,
            "objectives": len(rows),
            "subdomains": len(active_sds),
            "operationalized_subdomains": op_count,
            "principles": len(principles),
            "principles_unseamed": unseamed,
            "grounding_ratio": ratio,
            "calls": calls,
            "summary": (f"{len(rows)} objectives over {len(active_sds)} sub-domains; "
                        f"{op_count} operationalized; "
                        f"{7 - unseamed}/7 principles bound to this company"),
            "doc01": str(out_dir / "Doc01_Operational_Objectives.md"),
            "doc02": str(out_dir / "Doc02_Secure_Design_Principles.md"),
        })
        return calls

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
