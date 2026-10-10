#!/usr/bin/env python3
"""aegis_pipeline.phases.phase1.runner — Orchestrator for Phase 1 steps and sweeps."""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import (
    REGULATIONS,
    SD_RE,
    anchor_slice,
    carries_reg_card,
    compose_call,
    confirmed_regulations,
    domain_dir,
    load_case,
    load_selection,
    objective_paragraph,
    parse_simple_yaml,
    p4t_blocks,
    sub_so_objective,
)
from aegis_pipeline.core import (
    LLMError,
    OllamaClient,
    Trace,
    config as runconfig,
    count_calls,
    now_iso,
    update_manifest,
)
from aegis_pipeline.guards.controls import (
    goal_anchors,
    parse_overrides,
    sd_control_sections,
    track_b_rows,
)
from aegis_pipeline.phases.phase1.assembly import (
    assemble_doc,
    build_run_notes,
)
from aegis_pipeline.phases.phase1.common import (
    canonical_reg,
    extract_fenced,
    one_reg,
    parse_md_table,
)
from aegis_pipeline.phases.phase1.facts import parse_p1
from aegis_pipeline.phases.phase1.framing import parse_p3f
from aegis_pipeline.phases.phase1.goals import (
    _p4_instruction,
    check_p4_quality,
    parse_p4,
)
from aegis_pipeline.phases.phase1.regulations import parse_p2
from aegis_pipeline.phases.phase1.selection import parse_p3
from aegis_pipeline.phases.phase1.tensions import (
    load_tension_slices,
    merge_tensions,
    p4t_extra_instruction,
    parse_p4t,
    store_tension_slice,
)

NUM_CTX = {
    "p1": 16384,
    "p2": 16384,
    "p3": 32768,
    "p3f": 16384,
    "p4": 32768,
    "p4t": 32768,
    "p2o": 32768,
    "p2d": 32768,
    "p3a_map": 16384,
}

NUM_PREDICT = {
    "p1": 4096,
    "p2": 2048,
    "p3": 12288,
    "p3f": 2048,
    "p4": 16384,
    "p4t": 4096,
    "p2o": 4096,
    "p2d": 4096,
    "p3a_map": 4096,
}

EXTRA_INSTRUCTION = {
    "p3a_map": "Wrap your answer: return ONLY one ```markdown fenced block containing the verdict table, one row per objective, header row included.",
    "p1": "Wrap your answer: return ONLY one ```yaml fenced block with the fact sheet.",
    "p2": "Wrap your answer: return ONLY one ```markdown fenced block containing the 5-row §2 verdict table (header + 5 rows, nothing else).",
    "p2o": 'Wrap your answer: return ONLY one ```json fenced block shaped {"subdomain": "...", "operational_translation": "...", "methods": [{"id": "RULE-...", "method": "TEST|INSPECT|DEMONSTRATE|ANALYZE", "criteria": "...", "owner": "..."}], "principles": [{"id": "P-...", "rationale": "..."}]}.',
    "p2d": "Wrap your answer: return ONLY one ```json fenced block containing the 7 architectural principles.",
    "p3": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing (a) a markdown "
        "table `| Sub-domain | Name | Operational trigger |` of the selected sub-domains "
        "(header row included; canonical codes `D-XX.Y` from the candidate set; one row per "
        "selected sub-domain), and (b) a section `## Excluded candidates` listing each omitted "
        "candidate as `- `D-XX.Y` — <1-line justification>`. Every candidate in the prompt "
        "MUST appear in either the table or the excluded list; silent omission of any "
        "candidate fails the output contract. Technology-neutral: state what is governed, "
        "never tools or vendors (R5). Nothing else."
    ),
    "p3_clarified": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing (a) a markdown "
        "table `| Sub-domain | Name | Operational trigger |` of the selected sub-domains "
        "(header row included; canonical codes `D-XX.Y` from the candidate set; one row per "
        "selected sub-domain), and (b) a section `## Excluded candidates` listing each omitted "
        "candidate as `- `D-XX.Y` — <1-line justification>`. Candidate handling: every candidate "
        "in the prompt MUST appear in either the table or the excluded list; silent omission of "
        "any candidate fails the output contract. Selection criteria: select a candidate only "
        "when the fact sheet provides a concrete operational basis for it (data handled, hosting, "
        "software development, third-party processing) — general applicability of a regulation "
        "to the company does NOT make every sub-domain active. Exclude candidates that belong to "
        "the general compliance baseline or whose operational triggers are absent from the intake. "
        "Technology-neutral: state what is governed, never tools or vendors (R5). Nothing else."
    ),
    "p3f": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing the 4-row §2 "
        "framing table `| Dimension | Impact on proportionality |` with the four canonical "
        "dimensions in order: Size, Area of operation, Regulatory roles, Inherited capabilities. "
        "Ground every statement strictly in the fact sheet and intake prose (R6). "
        "Technology-neutral (R5). Nothing else."
    ),
    "p4t": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing the "
        "tension-resolution table `| ID | Sub-domains | Tension | Conflict | Resolution |`, "
        "one row per tension identified in the attached module text that is active for this company, "
        "or ONLY the line `None.` inside the fence when the attached text surfaces no active "
        "tension for this profile. If this module carries no tension analysis for the "
        "confirmed regulations, return ONLY the line `None.` inside the fence. "
        "Technology-neutral (R5). Nothing else."
    ),
}

P3_INSTRUCTION_VARIANTS = {"clarified": EXTRA_INSTRUCTION["p3_clarified"]}


def _assert_wrap_instruction(step: str, extra: str) -> None:
    if not extra.startswith("Wrap your answer"):
        return
    stripped = extra.rstrip().rstrip("`").rstrip()
    if stripped.split()[-1] in {"containing", "with", "of", "and", "the", "a", "to", "is"}:
        raise ValueError(
            f"step {step}: the wrap instruction ends on '{stripped.split()[-1]!r}' — it "
            f"promises a payload and then stops. Text was almost certainly lost from "
            f"EXTRA_INSTRUCTION[{step!r}]. Full instruction: {extra!r}"
        )


def parse_p2d(answer: str) -> dict:
    from phase2 import PRINCIPLE_IDS

    raw = extract_fenced(answer, "json").strip()
    data = json.loads(raw)
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
            raise ValueError(f"p2d: principle {i} has id {pid!r}, not one of {PRINCIPLE_IDS}")
        if pid in seen:
            raise ValueError(f"p2d: {pid} appears more than once")
        seen.add(pid)
        for f in ("constraint", "method_lead", "eval_scope"):
            if not str(r.get(f, "") or "").strip():
                raise ValueError(f"p2d: {pid} has an empty {f!r}")
    missing = [p for p in PRINCIPLE_IDS if p not in seen]
    if missing:
        raise ValueError(f"p2d: no row for {', '.join(missing)}")
    return {"principles": rows}


def parse_p2o(answer: str, subdomain: str | None = None) -> dict:
    import phase2 as _p2
    return _p2.parse_p2o(answer, subdomain)


PARSERS = {
    "p1": parse_p1,
    "p2": parse_p2,
    "p3": parse_p3,
    "p3f": parse_p3f,
    "p4t": parse_p4t,
    "p2o": parse_p2o,
    "p2d": parse_p2d,
}


def store_parsed(run_dir: Path, step: str, subdomain: str | None, parsed: dict) -> None:
    steps_dir = run_dir / "steps"
    if step == "p1":
        (steps_dir / "fact_sheet.yaml").write_text(parsed["yaml_text"], encoding="utf-8")
    elif step == "p2":
        (steps_dir / "verdicts.md").write_text(parsed["md"], encoding="utf-8")
        (steps_dir / "verdicts.json").write_text(
            json.dumps({"verdicts": parsed["verdicts"]}, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
    elif step == "p3":
        (steps_dir / "selection.md").write_text(parsed["md"], encoding="utf-8")
        (steps_dir / "selection.json").write_text(
            json.dumps({"selected": parsed["selected"], "excluded": parsed["excluded"]},
                       indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
    elif step == "p3f":
        (steps_dir / "framing.md").write_text(parsed["framing"] + "\n", encoding="utf-8")
    elif step.startswith("p2o") or step == "p2o":
        p2_dir = steps_dir / "phase2"
        p2_dir.mkdir(exist_ok=True)
        fname = subdomain.replace(".", "_") if subdomain else "unknown"
        (p2_dir / f"{fname}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    elif step.startswith("p3a_map"):
        d = steps_dir / "phase3a_map"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{subdomain.replace('.', '_')}.json").write_text(
            json.dumps(parsed, indent=1), encoding="utf-8"
        )
    elif subdomain is not None:
        goals_dir = steps_dir / "goals"
        goals_dir.mkdir(exist_ok=True)
        fname = subdomain.replace(".", "_")
        (goals_dir / f"{subdomain}.md").write_text(parsed["md"], encoding="utf-8")
        (goals_dir / f"{fname}.json").write_text(
            json.dumps(
                {"subdomain": subdomain, "goals": parsed["goals"], "assumptions": parsed["assumptions"]},
                indent=1, ensure_ascii=False,
            ),
            encoding="utf-8",
        )
    elif step == "p4t":
        (steps_dir / "tensions.md").write_text(parsed["md"] + "\n", encoding="utf-8")
        (steps_dir / "tensions.json").write_text(
            json.dumps({"tensions": parsed["tensions"]}, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
    elif step == "p2d":
        (steps_dir / "principles.json").write_text(
            json.dumps({"principles": parsed["principles"]}, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )


class StepRunner:
    def __init__(self, repo: Path, run_dir: Path, model: str, base: str, dry_run: bool = False):
        self.repo = repo
        self.run_dir = run_dir
        self.model = model
        self.base = base
        self.dry_run = dry_run
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
        step_kind = step.split(":", 1)[0]
        tag = (f"{step_kind}_{subdomain.replace('.', '_')}" if subdomain is not None
               else step.replace(":", "_"))
        seq = self.trace.next_seq()
        extra = ""
        if step_kind == "p4t":
            extra = p4t_extra_instruction(subdomain)
        elif step_kind == "p2o":
            extra = EXTRA_INSTRUCTION["p2o"]
        elif step_kind == "p3a_map":
            extra = EXTRA_INSTRUCTION["p3a_map"]
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
                subdomain,
                subso_ids=subso_ids,
                adjustment_variant=(self.config.get("ficha_overrides") or {}).get("p4_adjustment"),
                style_variant=(self.config.get("ficha_overrides") or {}).get("p4_instruction"),
                implication_variant=(self.config.get("ficha_overrides") or {}).get("p4_implication"),
            )
        else:
            extra = EXTRA_INSTRUCTION[step]
            override = (self.config.get("ficha_overrides") or {}).get(f"{step}_instruction")
            if override:
                table = P3_INSTRUCTION_VARIANTS if step == "p3" else None
                if table and override in table:
                    extra = table[override]
        _assert_wrap_instruction(step, extra)
        call = compose_call(
            self.repo, self.case, self.run_dir, step, subdomain, extra_instruction=extra
        )
        num_ctx = NUM_CTX[step_kind]
        num_predict = NUM_PREDICT[step_kind]
        est_tokens = (len(call["system"]) + len(call["user"])) // 4
        needed = est_tokens * 1.15 + num_predict + 2000
        while needed > num_ctx and num_ctx < 131072:
            num_ctx *= 2

        in_dir = self.run_dir / "inputs"
        in_dir.mkdir(parents=True, exist_ok=True)
        sys_path = in_dir / f"{seq:03d}_{tag}_system.md"
        user_path = in_dir / f"{seq:03d}_{tag}_user.md"
        sys_path.write_text(call["system"], encoding="utf-8")
        user_path.write_text(call["user"], encoding="utf-8")

        record = {
            "seq": seq,
            "step": tag,
            "ficha_id": call["ficha"]["id"],
            "ficha_version": call["ficha"]["version"],
            "model": self.model,
            "num_ctx": num_ctx,
            "num_predict": num_predict,
            "temperature": self.temperature,
            **{f"sampler_{k}": self.sampler.get(k) for k in runconfig.SAMPLER_KEYS},
            "ts_start": now_iso(),
            "system_path": str(sys_path),
            "user_path": str(user_path),
            "system_chars": len(call["system"]),
            "user_chars": len(call["user"]),
            "est_prompt_tokens": est_tokens,
            "pack_files": call["files"],
        }

        out_dir = self.run_dir / "outputs"
        raw_path = out_dir / f"{seq:03d}_{tag}_response.json"
        out_path = out_dir / f"{seq:03d}_{tag}_output.md"

        if needed > num_ctx:
            record.update({
                "status": "context-fail",
                "ts_end": now_iso(),
                "output_path": None,
                "raw_path": None,
                "context_ladder_cap": 131072,
                "needed_tokens": int(needed),
                "context_fail_error": (
                    f"prompt ~{est_tokens} tokens needs ~{int(needed)} of context "
                    f"(est x1.15 + num_predict={num_predict} + 2000) after the "
                    f"ladder stopped at num_ctx={num_ctx}, above the 131072 cap"
                ),
            })
            self.trace.append(record)
            raise LLMError(
                f"step {tag}: prompt ~{est_tokens} tokens needs ~{int(needed)} "
                f"of context, above the 131072 ladder cap — trim the pack "
                f"(decompose per Sub-SO card; E-15). Refused call recorded "
                f"in trace.jsonl seq {seq} (status=context-fail); pack kept in {in_dir}"
            )

        if self.dry_run:
            record.update({
                "status": "dry-run",
                "ts_end": now_iso(),
                "latency_s": 0,
                "response_chars": 0,
                "output_path": None,
                "raw_path": None,
            })
            self.trace.append(record)
            return

        client = self.client()
        client.ensure_model_cached(self.model)
        warm = client.warm_up(self.model, num_ctx)
        record["warmup_s"] = round(warm, 1)

        answer, raw = None, None
        for attempt in (1, 2):
            try:
                raw = client.chat(
                    self.model,
                    call["system"],
                    call["user"],
                    num_ctx,
                    temperature=self.temperature,
                    num_predict=num_predict,
                    sampler=self.sampler,
                )
                answer = raw.get("message", {}).get("content", "")
                record[f"attempt{attempt}_done_reason"] = raw.get("done_reason")
                if raw.get("done_reason") == "length":
                    (out_dir / f"{seq:03d}_{tag}_response_truncated.json").write_text(
                        json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8"
                    )
                    (out_dir / f"{seq:03d}_{tag}_output_truncated.md").write_text(answer, encoding="utf-8")
                    record[f"attempt{attempt}_truncated_chars"] = len(answer)
                    raise LLMError(
                        f"response truncated at the num_predict={num_predict} cap "
                        f"(done_reason=length, {raw.get('eval_count')} eval tokens, "
                        f"{len(answer)} chars returned) — answer is incomplete"
                    )
                if not answer.strip():
                    raise LLMError("empty response content")
                record[f"attempt{attempt}_latency_s"] = round(raw.get("total_duration", 0) / 1e9, 1)
                record[f"attempt{attempt}_eval_tokens"] = raw.get("eval_count")
                record[f"attempt{attempt}_prompt_tokens"] = raw.get("prompt_eval_count")
                break
            except LLMError as e:
                record[f"attempt{attempt}_error"] = str(e)[:500]
                if attempt == 1:
                    call["user"] += (
                        f"\n\nNOTE: your previous response could not be used ({e}). "
                        "Answer again, complete and correct."
                    )
        if answer is None:
            record.update({
                "status": "failed",
                "ts_end": now_iso(),
                "output_path": None,
                "raw_path": None,
            })
            self.trace.append(record)
            raise LLMError(f"step {tag}: both attempts failed; forensics in {in_dir}")

        raw_path.write_text(json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8")
        out_path.write_text(answer, encoding="utf-8")
        record.update({
            "response_chars": len(answer),
            "est_output_tokens": raw.get("eval_count"),
            "raw_path": str(raw_path),
            "output_path": str(out_path),
        })

        try:
            parsed = self._validate(step, answer, subdomain)
        except (ValueError, KeyError) as e:
            record["l0_first_error"] = str(e)[:500]
            messages = [
                {"role": "system", "content": call["system"]},
                {"role": "user", "content": call["user"]},
                {"role": "assistant", "content": answer},
                {
                    "role": "user",
                    "content": (
                        f"NOTE: your previous answer failed the output contract validation: {e}.\n"
                        "Re-emit the SAME answer with only that defect corrected. "
                        "Every other row, id, citation and adjustment record stays "
                        "exactly as you wrote it. Do not add material, do not restate "
                        "the baseline, do not elaborate — the answer must come out "
                        "the same length or shorter, in the same fenced format."
                    ),
                },
            ]
            try:
                raw2 = client.chat_messages(
                    self.model,
                    messages,
                    num_ctx,
                    temperature=self.temperature,
                    num_predict=num_predict,
                    sampler=self.sampler,
                )
                answer2 = raw2.get("message", {}).get("content", "")
                record["l0_retry_done_reason"] = raw2.get("done_reason")
                if raw2.get("done_reason") == "length":
                    raise LLMError(
                        f"L0 repair response truncated at the num_predict={num_predict} "
                        f"cap (done_reason=length, {raw2.get('eval_count')} eval tokens)"
                    )
                if not answer2.strip():
                    raise LLMError("L0 repair response was empty")
                retry_out = out_dir / f"{seq:03d}_{tag}_output_attempt2.md"
                retry_out.write_text(answer2, encoding="utf-8")
                record["retry_output_path"] = str(retry_out)
                parsed = self._validate(step, answer2, subdomain)
                answer, raw = answer2, raw2
                retry_raw = out_dir / f"{seq:03d}_{tag}_response_attempt2.json"
                retry_raw.write_text(json.dumps(raw2, indent=1, ensure_ascii=False), encoding="utf-8")
                record["accepted_raw_path"] = str(retry_raw)
                record["accepted_output_path"] = str(retry_out)
                record["response_chars"] = len(answer2)
                record["est_output_tokens"] = raw2.get("eval_count")
                record["l0_retried"] = True
            except (ValueError, KeyError, LLMError) as e2:
                record.update({
                    "status": "failed",
                    "ts_end": now_iso(),
                    "l0_final_error": str(e2)[:500],
                })
                self.trace.append(record)
                raise LLMError(
                    f"step {tag}: L0 validation failed twice.\n"
                    f"  first:  {e}\n"
                    f"  repair: {e2}\n"
                    f"  forensics in {out_dir} (see trace.jsonl l0_first_error)"
                ) from e2

        record.update({"status": "ok", "ts_end": now_iso()})
        self.trace.append(record)
        self._store(step, subdomain, tag, parsed)

    def _validate(self, step: str, answer: str, subdomain: str | None) -> dict:
        if step.startswith("p4t"):
            return parse_p4t(answer, sd_id=subdomain)
        if step.startswith("p2o"):
            return parse_p2o(answer, subdomain)
        if step.startswith("p3a_map"):
            import phase3 as _p3
            return {"verdicts": _p3.parse_verdicts(answer)}
        if subdomain is not None:
            parsed = parse_p4(answer, subdomain)
            return self._check_p4_quality(parsed, subdomain)
        if step == "p3":
            cands = [
                c["id"]
                for c in __import__("compose").candidate_subdomains(
                    self.repo, confirmed_regulations(self.run_dir)
                )
            ]
            return parse_p3(answer, cands)
        return PARSERS[step](answer)

    def _check_p4_quality(self, parsed: dict, sd_id: str) -> dict:
        return check_p4_quality(self.repo, self.run_dir, parsed, sd_id)

    def _store(self, step: str, subdomain: str | None, tag: str, parsed: dict) -> None:
        if step.startswith("p4t"):
            store_tension_slice(self.run_dir, subdomain, parsed)
            return
        store_parsed(self.run_dir, step, subdomain, parsed)

    def _trace_record(self, tag: str) -> dict:
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
        rec = self._trace_record(tag)
        status = rec.get("status")
        kind = (
            "context-fail" if status == "context-fail"
            else "L0" if rec.get("l0_final_error")
            else "transport" if rec.get("attempt2_error")
            else "error"
        )
        out = {
            "subdomain": sd_id,
            "step": tag,
            "kind": kind,
            "seq": rec.get("seq"),
            "ts": rec.get("ts_end") or rec.get("ts_start"),
        }
        for key in (
            "l0_first_error",
            "l0_final_error",
            "attempt1_error",
            "attempt2_error",
            "est_prompt_tokens",
            "needed_tokens",
            "context_ladder_cap",
            "num_ctx",
            "num_predict",
        ):
            if rec.get(key) is not None:
                out[key] = rec[key]
        if not rec:
            out["error"] = f"{type(err).__name__}: {err}"[:500]
        return out

    def _write_stage_result(self, stage: str, summary: dict) -> None:
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
            "records only whether the sweep completed"
        )
        update_manifest(self.run_dir, stage_result=manifest_block)
        print(
            f"AEGIS_STAGE_RESULT stage={stage} status={rec['status']} "
            f"carried={rec.get('carried')}/{rec.get('selected')} "
            f"failed={rec.get('failed')} detail={rec.get('summary', '')!r}",
            flush=True,
        )

    def _raise_if_nothing_carried(self, stage: str, summary: dict, failed_detail: str) -> None:
        if summary.get("carried") or self.dry_run:
            return
        raise LLMError(
            f"stage {stage}: no sub-domain produced a validated artifact — "
            f"0/{summary.get('selected')} carried, {summary.get('failed')} failed. "
            f"{failed_detail} Forensics in {self.run_dir / 'inputs'}, "
            f"{self.run_dir / 'outputs'} and steps/stage_result.json"
        )

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
        carried: list[str] = []
        already: list[str] = []
        failures: list[dict] = []
        calls = 0
        for sd_id in order:
            if done_marker(sd_id):
                print(f"[{stage}] {sd_id} already done (validated artifact on disk) — skipping", flush=True)
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
                print(
                    f"[{stage}] {sd_id} FAILED ({rec['kind']}) — continuing with the "
                    f"remaining sub-domains: {str(e)[:200]}",
                    flush=True,
                )
            calls += 1
        return {"carried": carried, "already": already, "failures": failures, "calls": calls}

    def stage_p4(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        selection = load_selection(self.run_dir)
        order = sorted(s["id"] for s in selection["selected"])
        sw = self._sweep(
            "p4",
            order,
            done_marker=lambda sd: (self.run_dir / "steps" / "goals" / f"{sd}.md").exists(),
            on_call=lambda sd: self._call(f"p4:{sd}", sd),
        )
        n_failed = len(sw["failures"])
        summary = {
            "status": (
                "dry-run" if self.dry_run
                else "ok" if not n_failed
                else "partial" if sw["carried"]
                else "failed"
            ),
            "selected": len(order),
            "carried": len(sw["carried"]),
            "already_done": len(sw["already"]),
            "failed": n_failed,
            "calls": sw["calls"],
            "summary": f"{len(sw['carried'])}/{len(order)} carried" + (f", {n_failed} failed (L0)" if n_failed else ""),
            "artifact": "steps/goals/",
            "failed_subdomains": [f["subdomain"] for f in sw["failures"]],
            "failures": sw["failures"],
        }
        self._write_stage_result("p4", summary)
        self._raise_if_nothing_carried(
            "p4",
            summary,
            "; ".join(f"{f['subdomain']}: {f.get('l0_final_error') or f.get('error', '')}" for f in sw["failures"][:3]),
        )
        return sw["calls"]

    def stage_p4t(self) -> int:
        self._require(("steps/selection.json",), "G-P1-C")
        confirmed = confirmed_regulations(self.run_dir)
        if len(confirmed) < 2:
            (self.run_dir / "steps" / "tensions.json").write_text(
                json.dumps({"tensions": []}, indent=1, ensure_ascii=False),
                encoding="utf-8",
            )
            print("[p4t] single-regulation run — no tensions call needed", flush=True)
            self._write_stage_result("p4t", {
                "status": "ok",
                "selected": len(load_selection(self.run_dir)["selected"]),
                "eligible": 0,
                "no_material": 0,
                "carried": 0,
                "already_done": 0,
                "failed": 0,
                "calls": 0,
                "tensions": 0,
                "summary": "single-regulation run — no tensions call needed",
                "artifact": "steps/tensions.json",
                "failed_subdomains": [],
                "failures": [],
            })
            return 0
        blocks = p4t_blocks(self.repo, self.run_dir)
        eligible = [b["sd_id"] for b in blocks if b["has_tensions"]]
        no_material = [b["sd_id"] for b in blocks if not b["has_tensions"]]
        if no_material:
            print(
                f"[p4t] no Emergent-tensions section for {len(no_material)} selected "
                f"sub-domain(s) — no call, no corpus material to rule on: {', '.join(no_material)}",
                flush=True,
            )
        sw = self._sweep(
            "p4t",
            eligible,
            done_marker=lambda sd: (self.run_dir / "steps" / "tensions" / f"{sd}.json").exists(),
            on_call=lambda sd: self._call(f"p4t:{sd}", sd),
        )
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
            "summary": (
                f"{len(sw['carried'])}/{len(eligible)} carried"
                + (f", {n_failed} failed (L0)" if n_failed else "")
                + (f"; {len(no_material)} of {n_selected} selected sub-domains carry no corpus tension section" if no_material else "")
            ),
            "artifact": "steps/tensions.md (merged) / steps/tensions/ (per sub-domain)",
            "failed_subdomains": [f["subdomain"] for f in sw["failures"]],
            "failures": sw["failures"],
        }
        if not sw["carried"]:
            base["status"] = "failed"
            self._write_stage_result("p4t", dict(base, tensions=0))
            self._raise_if_nothing_carried(
                "p4t",
                base,
                "; ".join(f"{f['subdomain']}: {f.get('l0_final_error') or f.get('error', '')}" for f in sw["failures"][:3]),
            )
        if self.dry_run:
            base["status"] = "dry-run"
            base["tensions"] = None
            self._write_stage_result("p4t", base)
            return sw["calls"]
        merged = merge_tensions(load_tension_slices(self.run_dir, sw["carried"]))
        store_parsed(self.run_dir, "p4t", None, merged)
        base["status"] = "ok" if not n_failed else "partial"
        base["tensions"] = len(merged["tensions"])
        n, rows_by_sd = 0, []
        for sd in sw["carried"]:
            k = len(load_tension_slices(self.run_dir, [sd])[0].get("tensions", []))
            rows_by_sd.append({"subdomain": sd, "n_rows": k, "ids": [f"T-{i:03d}" for i in range(n + 1, n + 1 + k)]})
            n += k
        base["rows_by_subdomain"] = rows_by_sd
        self._write_stage_result("p4t", base)
        return sw["calls"]

    def stage_p3a_map(self) -> int:
        import phase3 as p3

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        phase2_doc = self.run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        if not phase2_doc.is_file():
            raise ValueError(f"no Phase 2 deliverable at {phase2_doc} — run --stage phase2 first")

        objectives = p3.load_objectives(phase2_doc)
        if not objectives:
            raise ValueError("Phase 2 deliverable parsed to zero objectives")
        skeleton = p3.build(objectives)
        skeleton_findings = p3.check(skeleton, objectives)
        if skeleton_findings:
            raise ValueError(f"Phase 3 skeleton gate failed with {len(skeleton_findings)} finding(s): {skeleton_findings}")

        v0 = (
            self.repo / "cases" / self.case["case_id"] / "03_PHASE3_SPEC"
            / "part1_security_privacy" / "v0_functional_baseline"
            / "Doc01_Requirements_Elicitation_and_PUC.md"
        )
        if not v0.is_file():
            raise ValueError(f"no frozen V0 baseline at {v0}")
        cards = p3.load_v0_cards(v0)
        pool = [c["id"] for c in cards]
        if not pool:
            raise ValueError(f"frozen V0 baseline at {v0} yielded no candidate cards")

        by_sd: dict[str, list[dict]] = {}
        for r in skeleton:
            by_sd.setdefault(r["subdomain"], []).append(r)

        store = self.run_dir / "steps" / "phase3"
        store.mkdir(parents=True, exist_ok=True)
        calls = 0
        failures = []

        for sd in sorted(by_sd):
            rows = by_sd[sd]
            sd_objs = [o for o in objectives if o["subdomain"] == sd]
            parsed_path = store / f"verdicts_{sd.replace('.', '_')}.json"
            if parsed_path.is_file():
                verdicts = json.loads(parsed_path.read_text(encoding="utf-8"))
            else:
                (store / f"pack_{sd.replace('.', '_')}.md").write_text(
                    p3.build_verdict_pack(rows, cards), encoding="utf-8"
                )
                try:
                    self._call(f"p3a_map:{sd}", sd)
                    stored = self.run_dir / "steps" / "phase3a_map" / f"{sd.replace('.', '_')}.json"
                    if not stored.is_file():
                        if self.dry_run:
                            continue
                        raise FileNotFoundError(f"{stored} was not written by _call")
                    verdicts = json.loads(stored.read_text(encoding="utf-8"))["verdicts"]
                    sub_findings = p3.check_verdicts(verdicts, sd_objs, pool)
                    if sub_findings:
                        raise ValueError(f"{len(sub_findings)} finding(s): {sub_findings[0]}")
                    if not self.dry_run:
                        calls += 1
                    parsed_path.write_text(json.dumps(verdicts, indent=1), encoding="utf-8")
                except (LLMError, ValueError, KeyError, OSError) as e:
                    failures.append(f"{sd}: {type(e).__name__}: {str(e)[:160]}")
                    print(f"[phase3] {sd} verdicts FAILED — continuing: {str(e)[:160]}", flush=True)
                    continue
            by_sd[sd] = p3.apply_verdicts(rows, verdicts)

        merged = [r for rows in by_sd.values() for r in rows]
        out_dir = self.run_dir / "outputs" / "phase3" / "synthesis_rounds"
        out_dir.mkdir(parents=True, exist_ok=True)
        grouped: dict[str, list[dict]] = {}
        for r in merged:
            grouped.setdefault(r["domain"], []).append(r)
        (out_dir / "OBJECTIVE_MAPPING.md").write_text(
            p3.render_matrix(merged, grouped, p3.domain_names_from(self.repo / "baseline/domains/index.md")),
            encoding="utf-8",
        )
        (out_dir / "PRINCIPLE_MAPPING.md").write_text(p3.render_principles(), encoding="utf-8")

        findings = (
            p3.check_verdicts(merged, [o for o in objectives if o["id"] in {r["id"] for r in merged}], pool)
            + p3.check_anchors(merged)
        )
        if findings:
            print(f"[phase3] {len(findings)} verdict finding(s):", flush=True)
            for f in findings[:12]:
                print(f"    {f}", flush=True)

        carried = len(by_sd) - len({f.split(":")[0] for f in failures})
        self._write_stage_result("p3a_map", {
            "status": "ok" if not failures and not findings else "partial",
            "carried": carried,
            "selected": len(by_sd),
            "failed": len(failures),
            "summary": f"{len(merged)} objectives / {len(by_sd)} sub-domains; {len(findings)} finding(s)",
            "objectives": len(merged),
            "findings": len(findings),
            "failures": failures,
            "verdict_counts": {v: sum(1 for r in merged if r["verdict"] == v) for v in p3.VERDICTS},
        })
        return calls

    def stage_p5(self) -> int:
        self._require(("steps/selection.json", "steps/framing.md"), "G-P1-C")
        goals = sorted((self.run_dir / "steps" / "goals").glob("D-*.md"))
        if not goals:
            raise ValueError("no P4 goal artifacts found — run stage p4 first")
        doc = assemble_doc(self.repo, self.run_dir, self.case)
        (self.run_dir / "doc02_adjusted_goals.md").write_text(doc, encoding="utf-8")
        (self.run_dir / "RUN_NOTES.md").write_text(build_run_notes(self.run_dir), encoding="utf-8")
        if not self.dry_run:
            self._finalize_p5()
        return 0

    def stage_phase2(self) -> int:
        import phase2 as p2

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        if not (self.run_dir / "steps" / "goals").is_dir():
            raise ValueError("no P4 goal artifacts — run stage p4 first")

        rows = p2.build(self.repo, self.run_dir)
        findings = p2.check(rows, self.run_dir)
        if findings:
            raise ValueError(f"Phase 2 Doc01 gate failed with {len(findings)} finding(s): {findings}")

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
            try:
                self._call(f"p2o:{sd}", sd)
                if not self.dry_run:
                    calls += 1
            except (LLMError, ValueError, KeyError) as e:
                print(
                    f"[phase2] {sd} p2o FAILED ({type(e).__name__}) — continuing with "
                    f"remaining sub-domains: {str(e)[:180]}",
                    flush=True,
                )

        op_map = p2.load_operationalizations(self.run_dir)
        dist = p2.method_distribution(op_map)
        diversity = p2.method_diversity_findings(dist)
        if diversity:
            raise ValueError(f"Phase 2 method diversity gate failed with {len(diversity)} finding(s): {diversity}")
        filled, total = p2.seam_fill(rows, op_map)

        (out_dir / "Doc01_Operational_Objectives.md").write_text(
            p2.render_doc01(self.repo, self.run_dir, rows), encoding="utf-8"
        )

        self._call("p2d", None)
        if not self.dry_run:
            calls += 1
            principles = p2.principles_for(self.run_dir)
            doc2_findings = p2.check_doc02(self.repo, self.run_dir, principles)
            if doc2_findings:
                raise ValueError(f"Phase 2 Doc02 gate failed with {len(doc2_findings)} finding(s): {doc2_findings}")
            ratio = p2.grounding_ratio(principles, p2._fact_sheet(self.run_dir))
        else:
            principles, ratio = p2.principles_for(self.run_dir), 0.0

        (out_dir / "Doc02_Secure_Design_Principles.md").write_text(
            p2.render_doc02(self.repo, self.run_dir, principles), encoding="utf-8"
        )

        op_count = len(list(p2_dir.glob("*.json")))
        unseamed = sum(1 for p in principles if str(p.get("constraint", "")) in ("", p2.UNSET))
        self._write_stage_result("phase2", {
            "status": "ok" if (not self.dry_run and unseamed == 0) else "partial",
            "selected": 7,
            "carried": 7 - unseamed,
            "failed": unseamed,
            "objectives": len(rows),
            "subdomains": len(active_sds),
            "operationalized_subdomains": op_count,
            "seams_filled": f"{filled}/{total}",
            "method_distribution": dist,
            "principles": len(principles),
            "principles_unseamed": unseamed,
            "grounding_ratio": ratio,
            "calls": calls,
            "summary": (
                f"{len(rows)} objectives over {len(active_sds)} sub-domains; "
                f"{op_count} operationalized; {filled}/{total} seams filled; "
                f"{7 - unseamed}/7 principles bound to this company"
            ),
            "doc01": str(out_dir / "Doc01_Operational_Objectives.md"),
            "doc02": str(out_dir / "Doc02_Secure_Design_Principles.md"),
        })
        return calls

    def _finalize_p5(self) -> None:
        import validate as validate_mod

        update_manifest(self.run_dir, n_calls_total=count_calls(self.run_dir))
        findings = validate_mod.validate_run(self.repo, self.run_dir)
        if findings:
            raise ValueError(
                f"post-assembly L1 validation failed with {len(findings)} finding(s) "
                f"(doc02_adjusted_goals.md kept on disk for forensics): {findings}"
            )
        out_dir = (
            Path(os.environ.get("AEGIS_EXPORT_DIR", str(self.repo / "output")))
            / self.case["company_id"]
            / "phase1"
            / self.run_dir.name
        )
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(self.run_dir / "doc02_adjusted_goals.md", out_dir / "doc02_adjusted_goals.md")
        shutil.copy(self.run_dir / "RUN_NOTES.md", out_dir / "RUN_NOTES.md")
        print(f"[p5] L1 validation PASS; deliverable exported to {out_dir}", flush=True)

    def _require(self, relpaths: tuple[str, ...], gate: str) -> None:
        for rel in relpaths:
            if not (self.run_dir / rel).exists():
                raise ValueError(
                    f"stage prerequisite missing: {rel} (earlier stage not run or gate {gate} not approved)"
                )
        gate_path = self.run_dir / "steps" / "gates" / f"{gate}.approved"
        if not gate_path.exists():
            raise ValueError(
                f"human gate {gate} not approved: create "
                f"steps/gates/{gate}.approved (with the review note) after local review, "
                "then re-sync this run directory to the cluster."
            )
