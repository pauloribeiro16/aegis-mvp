#!/usr/bin/env python3
"""steps.py — Phase 1 step execution: compose → call → L0 validate → store.

Each step = one ficha (generic) + one deterministic pack. The L0 parser checks
the model's answer against the ficha's output contract; on failure the call is
retried once with the validator errors appended (flag-not-drop), then the stage
aborts with forensics on disk.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from compose import (REGULATIONS, SD_RE, compose_call, confirmed_regulations,
                     extract_markdown_section, load_case, load_selection)
from llm import LLMError, OllamaClient
from trace import Trace, now_iso

NUM_CTX = {"p1": 16384, "p2": 16384, "p3": 32768, "p3f": 16384, "p4": 32768, "p5": 32768}
# output budget per step (P5 renders the whole document: 22 goal tables
# exceeded the 8192 default — done_reason=length truncation, job 1963648)
NUM_PREDICT = {"p1": 4096, "p2": 2048, "p3": 8192, "p3f": 2048, "p4": 8192, "p5": 16384}

PATTERNS = {"achieve", "cease", "maintain", "avoid", "optimize"}
# template §4 renders long-form property names; normalize to the enum codes
PROPERTY_ALIASES = {
    "confidentiality": "c", "integrity": "i", "availability": "a",
    "privacy right": "privacy-right", "privacy-right": "privacy-right",
    "accountability": "accountability", "c": "c", "i": "i", "a": "a",
}


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


# --------------------------------------------------------------------------
# per-step L0 parsers (output contract = ficha Output schema)
# --------------------------------------------------------------------------

def parse_p1(answer: str) -> dict:
    yaml_text = extract_fenced(answer, "yaml")
    from compose import parse_simple_yaml
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


def parse_p4(answer: str, sd_id: str) -> dict:
    md = extract_fenced(answer, "markdown")
    rows = parse_md_table(md)
    goals = []
    seq = 0
    for cells in rows:
        if len(cells) != 8:
            continue  # §4.1 rows have 6 columns; only the goal table has 8
        idm = re.match(r"`?(AG-D-\d{2}\.\d-\d{3})`?", cells[0].replace("*", "").strip())
        if not idm:
            continue
        seq += 1
        gid = idm.group(1)
        expected = f"AG-{sd_id}-{seq:03d}"
        if gid != expected:
            raise ValueError(f"goal IDs must be sequential from 001: expected {expected}, got {gid}")
        if len(cells) < 8:
            raise ValueError(f"goal row {gid} has {len(cells)} columns, expected 8")
        pattern = cells[2].strip().lower()
        if pattern not in PATTERNS:
            raise ValueError(f"invalid pattern {pattern!r} on {gid}")
        prop_raw = " ".join(cells[3].strip().lower().split())
        prop = PROPERTY_ALIASES.get(prop_raw) or PROPERTY_ALIASES.get(prop_raw.replace(" ", "-"))
        if prop is None:
            raise ValueError(f"invalid property {cells[3]!r} on {gid}")
        parent = cells[4].replace("`", "").strip()
        if not re.fullmatch(rf"SO-{re.escape(sd_id)}\.HL", parent):
            raise ValueError(f"invalid parent goal {parent!r} on {gid} (expected SO-{sd_id}.HL)")
        if not cells[5].strip():
            raise ValueError(f"empty regulatory source on {gid} (R2a)")
        if not cells[7].strip():
            raise ValueError(f"empty adjustment record on {gid} (R3/ADR-003 D1)")
        goals.append({
            "id": gid, "goal": cells[1], "pattern": pattern, "property": prop,
            "parent": parent, "source": cells[5], "anchor": cells[6].strip(), "adjustment": cells[7],
        })
    if not goals:
        raise ValueError(f"no AG-D-{sd_id}-NNN rows found in P4 answer")
    return {"md": md, "goals": goals}


def parse_p3f(answer: str) -> dict:
    md = extract_fenced(answer, "markdown")
    lines = [l for l in md.strip().splitlines() if l.strip().startswith(">")]
    if not lines:
        raise ValueError("p3f answer must be a single > blockquote")
    return {"framing": "\n".join(lines).strip()}


def parse_p5(answer: str) -> dict:
    """P5 intro call: only the narrative blocks (§1 echo, §4 framing, §6 handoff).
    The full document is assembled deterministically from validated artifacts —
    asking the model to re-render 22 goal tables truncates at any output cap
    (done_reason=length, jobs 1963648/1963810)."""
    md = extract_fenced(answer, "markdown")
    s1 = extract_markdown_section(md, "## §1", ["## §4"])
    framing = extract_markdown_section(md, "## §4", ["## §6"]) or None
    s6 = extract_markdown_section(md, "## §6", [])
    for name, sec in (("§1 Company Profile Echo", s1),
                      ("§6 Handoff Notes to Phase 2", s6)):
        if not sec.strip():
            raise ValueError(f"p5 intro answer missing or empty: {name}")
    # framing is optional in the answer when stage p3f already produced it
    return {"s1": s1.strip(), "framing": (framing.strip() if framing else None),
            "s6": s6.strip()}


def _strip_heading(sec: str) -> str:
    """The LLM sections arrive with their own `## §N` heading — the assembler
    provides the canonical heading, so drop the model's duplicate."""
    lines = sec.strip().splitlines()
    if lines and lines[0].strip().startswith("#"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def assemble_p5(run_dir: Path, case: dict, s1: str, framing: str, s6: str) -> str:
    """Deterministic assembly of phase1_output.md from validated step artifacts
    (verdicts.md, selection.md, goals/D-XX.Y.md fragments)."""
    import datetime as _dt
    steps_dir = run_dir / "steps"
    verdicts = (steps_dir / "verdicts.md").read_text(encoding="utf-8").strip()
    selection_md = (steps_dir / "selection.md").read_text(encoding="utf-8")
    sel_table = selection_md.split("Excluded candidates:")[0].strip()
    frags = sorted((steps_dir / "goals").glob("D-*.md"))
    if not frags:
        raise ValueError("no goal fragments to assemble")
    goal_blocks, a41_rows, s5_items = [], [], []
    for f in frags:
        t = f.read_text(encoding="utf-8")
        m = re.search(r"(^### D-\d{2}\.\d[^\n]*\n(?:.*?))(?=^## §4\.1|\Z)", t, re.S | re.M)
        if not m:
            raise ValueError(f"goal fragment {f.name} missing the §4 heading+table block")
        goal_blocks.append(m.group(1).strip())
        a41 = re.search(r"^## §4\.1[^\n]*\n(.*?)(?=^## §5|\Z)", t, re.S | re.M)
        if a41:
            for line in a41.group(1).splitlines():
                s = line.strip()
                if s.startswith("|") and not re.fullmatch(r"\|[\s:|-]+\|", s) \
                        and not s.startswith("| ID |"):
                    a41_rows.append(s)
        s5 = re.search(r"^## §5[^\n]*\n(.*?)\Z", t, re.S | re.M)
        if s5:
            for line in s5.group(1).splitlines():
                s = line.strip()
                if s and s.lower() != "none.":
                    s5_items.append(s)
    today = _dt.date.today().isoformat()
    fm = (f"---\ndocument_id: MVP-P1-OUT-001\ntitle: \"Phase 1 Output — "
          f"{case['company_name']} (Contextual Definition, MVP)\"\nversion: 0.1\n"
          f"created: {today}\nstatus: DRAFT\ninput: pipeline/cases/{case['case_id']}/"
          f"company_input.md\ncorpus: baseline\n---\n")
    parts = [
        fm, f"# Phase 1 Output — {case['company_name']}", "",
        "## §1 Company Profile Echo", _strip_heading(s1),
        "## §2 Applicable Regulations", verdicts,
        "## §3 Applicable Sub-domain Subset", sel_table,
        "## §4 Adjusted Goals", "",
        "**Framing (company context conditioning every goal below):**", _strip_heading(framing), "",
    ]
    parts.extend(goal_blocks)
    parts.append("### §4.1 Control Anchor Mapping (applicable regulations only — rule R8)")
    parts.append("| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |")
    parts.append("|---|---|---|---|---|---|")
    parts.extend(a41_rows)
    parts.append("## §5 Ambiguities & Open Questions")
    parts.append("\n".join(s5_items) if s5_items else "None.")
    parts.append("## §6 Handoff Notes to Phase 2")
    parts.append(_strip_heading(s6))
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
| Deliverable | phase1_output.md (DRAFT) |

## SPEC §8 evidence

| # | Item | How verified | Result |
|---|---|---|---|
| 1 | Input contract (5 sections) | validated at P1 (L0 stop condition) | PASS |
| 2 | §2 covers every input §5 regulation | validate.py item 2 | run locally post-sync |
| 3 | §3 codes exist in corpus | validate.py item 3 | run locally post-sync |
| 4 | AG IDs unique, match §3 | validate.py item 4 | run locally post-sync |
| 5 | Regulatory sources resolve (R2a) | validate.py item 5 | run locally post-sync |
| 6 | Control anchors resolve (R2b) | validate.py item 6 | run locally post-sync |
| 7 | No statement without input trace | L0 parsers + gate review | human check |
| 8 | Frontmatter complete; DRAFT | assembly (deterministic) | PASS (DRAFT until G-P1-D) |
| 9 | Pattern/property/parent/adjustment | validate.py item 9 | run locally post-sync |
| 10 | Document hygiene (R11/R12) | validate.py R12-hygiene + doc_lint scope note | run locally post-sync |

## Human gates

| Gate | State | Note |
|---|---|---|
{gate_rows or "| (none yet) | | |"}
"""


PARSERS = {"p1": parse_p1, "p2": parse_p2, "p3": parse_p3, "p3f": parse_p3f,
           "p5": parse_p5}

EXTRA_INSTRUCTION = {
    "p1": "Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.",
    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),
    "p3": ("Wrap your answer: return ONLY one ```markdown fenced block containing "
           "(a) the §3 selection table `| Sub-domain | Name | Trigger rationale |` and "
           "(b) a line `Excluded candidates:` followed by one line per excluded candidate "
           "in the form `<D-XX.Y> — <why-not>`. Nothing else."),
    "p5": ("Wrap your answer: return ONLY one ```markdown fenced block containing exactly "
           "three sections: `## §1 Company Profile Echo` (max 15 lines, verbatim-faithful "
           "condensation of input §1-§4, no new facts), `## §4 Framing` (a single > "
           "blockquote, max 8 lines: company size consequence, area of operation, "
           "regulatory roles, inherited/managed capabilities, explicit exclusions) and "
           "`## §6 Handoff Notes to Phase 2` (max 10 lines: applicable regulations, "
           "sub-domain scope, open questions). Plain markdown prose — never JSON. "
           "Nothing else."),
    "p3f": ("Wrap your answer: return ONLY one ```markdown fenced block containing a "
           "single > blockquote (max 8 lines) with the §4 framing: company size "
           "consequence, area of operation, regulatory roles, inherited/managed "
           "capabilities, explicit exclusions. Plain markdown — never JSON. "
           "Nothing else."),
    "p5_no_framing": ("Wrap your answer: return ONLY one ```markdown fenced block containing "
                      "exactly two sections: `## §1 Company Profile Echo` (max 15 lines, "
                      "verbatim-faithful condensation of input §1-§4, no new facts) and "
                      "`## §6 Handoff Notes to Phase 2` (max 10 lines: applicable "
                      "regulations, sub-domain scope, open questions). The §4 Framing "
                      "block is already provided separately. Plain markdown — never JSON. "
                      "Nothing else."),
}


def p4_extra_instruction(sd_id: str) -> str:
    return (
        f"Wrap your answer: return ONLY one ```markdown fenced block containing "
        f"(a) the heading `### {sd_id} — <canonical name>` and the 8-column goal table "
        f"(`ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | "
        f"Control anchor | Adjustment`), (b) a heading `## §4.1 Control Anchor Mapping` "
        f"with one row per (goal, confirmed regulation) pair "
        f"(`ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source`), and "
        f"(c) a heading `## §5` listing only `> ASSUMPTION:` blockquotes and open "
        f"questions this sub-domain owes (ambiguity interpretation is already decided "
        f"in the corpus — do not cite or re-analyze ambiguity cards; write `None.` if "
        f"empty). The Property column MUST use exactly one of these short codes: "
        f"C, I, A, privacy-right, accountability. Nothing else."
    )


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
        if subdomain is not None:
            extra = p4_extra_instruction(subdomain)
        elif step == "p5" and (self.run_dir / "steps" / "framing.md").exists():
            extra = EXTRA_INSTRUCTION["p5_no_framing"]  # p3f already produced it
        else:
            extra = EXTRA_INSTRUCTION[step]
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
            "num_ctx": num_ctx, "temperature": 0.2,
            "ts_start": now_iso(), "system_path": str(sys_path),
            "user_path": str(user_path), "system_chars": len(call["system"]),
            "user_chars": len(call["user"]), "est_prompt_tokens": len(call["user"]) // 4,
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
                                  num_predict=num_predict)
                answer = raw.get("message", {}).get("content", "")
                if not answer.strip():
                    raise LLMError("empty response content")
                record[f"attempt{attempt}_latency_s"] = round(raw.get("total_duration", 0) / 1e9, 1)
                record[f"attempt{attempt}_eval_tokens"] = raw.get("eval_count")
                break
            except LLMError as e:
                record[f"attempt{attempt}_error"] = str(e)[:500]
                if attempt == 1:
                    call["user"] += (f"\n\nNOTE: your previous response could not be used "
                                     f"({e}). Answer again, complete and correct.")
                    call["system"] = call["system"]  # unchanged
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
            retry_user = (call["user"] + f"\n\nNOTE: your previous answer failed the output "
                          f"contract validation: {e}. Return the corrected answer only, "
                          f"exactly in the requested fenced format.")
            try:
                raw2 = client.chat(self.model, call["system"], retry_user, num_ctx,
                                   num_predict=num_predict)
                answer2 = raw2.get("message", {}).get("content", "")
                retry_out = out_dir / f"{seq:03d}_{tag}_output_attempt2.md"
                retry_out.write_text(answer2, encoding="utf-8")
                record["retry_output_path"] = str(retry_out)
                parsed = self._validate(step, answer2, subdomain)
                answer, raw = answer2, raw2
                record["l0_retried"] = True
            except (ValueError, KeyError, LLMError) as e2:
                record.update({"status": "failed", "ts_end": now_iso(),
                               "l0_final_error": str(e2)[:500]})
                self.trace.append(record)
                raise LLMError(f"step {tag}: L0 validation failed twice "
                               f"({e2}); forensics in {out_dir}") from e2

        record.update({"status": "ok", "ts_end": now_iso()})
        self.trace.append(record)
        self._store(step, subdomain, tag, parsed)

    def _validate(self, step: str, answer: str, subdomain: str | None) -> dict:
        if subdomain is not None:
            return parse_p4(answer, subdomain)
        if step == "p3":
            cands = [c["id"] for c in
                     __import__("compose").candidate_subdomains(self.repo, confirmed_regulations(self.run_dir))]
            return parse_p3(answer, cands)
        return PARSERS[step](answer)

    def _store(self, step: str, subdomain: str | None, tag: str, parsed: dict) -> None:
        steps_dir = self.run_dir / "steps"
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
        elif subdomain is not None:
            goals_dir = steps_dir / "goals"
            goals_dir.mkdir(exist_ok=True)
            fname = subdomain.replace(".", "_")
            (goals_dir / f"{subdomain}.md").write_text(parsed["md"], encoding="utf-8")
            (goals_dir / f"{fname}.json").write_text(
                json.dumps({"subdomain": subdomain, "goals": parsed["goals"]},
                           indent=1, ensure_ascii=False), encoding="utf-8")
        elif step == "p3f":
            (steps_dir / "framing.md").write_text(parsed["framing"] + "\n", encoding="utf-8")
        elif step == "p5":
            framing = parsed.get("framing")
            if not framing:
                f = steps_dir / "framing.md"
                if not f.exists():
                    raise ValueError("no §4 framing: neither the p5 answer nor "
                                     "steps/framing.md (stage p3f) provides it")
                framing = f.read_text(encoding="utf-8").strip()
            doc = assemble_p5(self.run_dir, self.case, parsed["s1"], framing, parsed["s6"])
            (self.run_dir / "phase1_output.md").write_text(doc, encoding="utf-8")
            (self.run_dir / "RUN_NOTES.md").write_text(build_run_notes(self.run_dir),
                                                       encoding="utf-8")

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
        self._require(("steps/selection.json",), "G-P1-C")
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

    def stage_p5(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        goals = sorted((self.run_dir / "steps" / "goals").glob("D-*.md"))
        if not goals:
            raise ValueError("no P4 goal artifacts found — run stage p4 first")
        self._call("p5", None)  # narrative blocks (§1, §6; framing only if p3f absent)
        return 1

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
