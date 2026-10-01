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
                     load_case, load_selection)
from llm import LLMError, OllamaClient
from trace import Trace, now_iso

NUM_CTX = {"p1": 16384, "p2": 16384, "p3": 32768, "p4": 32768, "p5": 32768}

PATTERNS = {"achieve", "cease", "maintain", "avoid", "optimize"}


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
        prop = cells[3].strip().lower().replace(" ", "-")
        if prop not in {"c", "i", "a", "privacy-right", "accountability"}:
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


def parse_p5(answer: str) -> dict:
    doc_m = re.search(r"```markdown\n(.*?)```", answer, re.S)
    notes_m = re.search(r"```run_notes\n(.*?)```", answer, re.S)
    if not doc_m or not notes_m:
        raise ValueError("P5 answer must contain one ```markdown block (phase1_output.md) "
                         "and one ```run_notes block (RUN_NOTES.md)")
    doc = doc_m.group(1).strip()
    notes = notes_m.group(1).strip()
    if not doc.startswith("---"):
        raise ValueError("phase1_output.md must open with YAML frontmatter")
    fm, _ = doc.split("---", 2)[1], None
    if not re.search(r"status:\s*DRAFT", fm):
        raise ValueError("frontmatter status must be DRAFT until G-P1-D sign-off")
    for i in range(1, 7):
        if not re.search(rf"^##\s+§{i}\b", doc, re.M):
            raise ValueError(f"missing section §{i} in phase1_output.md")
    if "RUN_NOTES" not in notes and "|" not in notes:
        raise ValueError("RUN_NOTES block must contain the §8 evidence table")
    return {"doc": doc, "notes": notes}


PARSERS = {"p1": parse_p1, "p2": parse_p2, "p3": parse_p3, "p5": parse_p5}

EXTRA_INSTRUCTION = {
    "p1": "Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.",
    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),
    "p3": ("Wrap your answer: return ONLY one ```markdown fenced block containing "
           "(a) the §3 selection table `| Sub-domain | Name | Trigger rationale |` and "
           "(b) a line `Excluded candidates:` followed by one line per excluded candidate "
           "in the form `<D-XX.Y> — <why-not>`. Nothing else."),
    "p5": ("Wrap your answer: return TWO fenced blocks — first ```markdown containing the "
           "complete phase1_output.md (frontmatter + §1–§6), then ```run_notes containing "
           "RUN_NOTES.md (§8 evidence table + gate notes)."),
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
        f"empty). Nothing else."
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
        call = compose_call(self.repo, self.case, self.run_dir, step, subdomain,
                            extra_instruction=p4_extra_instruction(subdomain) if subdomain
                            else EXTRA_INSTRUCTION[step])
        num_ctx = NUM_CTX[step.split(":")[0]]

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
                raw = client.chat(self.model, call["system"], call["user"], num_ctx)
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
                raw2 = client.chat(self.model, call["system"], retry_user, num_ctx)
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
        elif step == "p5":
            (self.run_dir / "phase1_output.md").write_text(parsed["doc"], encoding="utf-8")
            (self.run_dir / "RUN_NOTES.md").write_text(parsed["notes"], encoding="utf-8")

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

    def stage_p4(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        for sd_id in order:
            print(f"[p4] sub-domain {sd_id}", flush=True)
            self._call(f"p4:{sd_id}", sd_id)
        return len(order)

    def stage_p5(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        goals = sorted((self.run_dir / "steps" / "goals").glob("D-*.md"))
        if not goals:
            raise ValueError("no P4 goal artifacts found — run stage p4 first")
        self._call("p5", None)
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
