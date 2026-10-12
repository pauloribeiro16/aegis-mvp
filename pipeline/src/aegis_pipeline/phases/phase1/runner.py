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
    "p3a_cards": 32768,
    "p3a_card": 32768,
    "p3a_prin": 16384,
    "p3a_propose": 32768,
    "p3a_org": 32768,
    "p3a_weave": 32768,
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
    "p3a_cards": 8192,
    "p3a_card": 8192,
    "p3a_prin": 4096,
    "p3a_propose": 8192,
    "p3a_org": 8192,
    "p3a_weave": 8192,
}

EXTRA_INSTRUCTION = {
    "p3a_map": "Wrap your answer: return ONLY one ```markdown fenced block containing the verdict table, one row per objective, header row included.",
    "p3a_cards": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing the inventory table "
        "`| Card | Name | Business basis |` (header row included, one row per card you propose, "
        "card ids `R<n>.<m>` starting at R1.1). Nothing else."
    ),
    "p3a_card": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing three sections — "
        "`#### Card <id>` (the 7-row table: ID, Description, Requirement Origin, Interfaces, "
        "Dependencies, Identified Problems, Priority), `#### PUC` (one 5-column row), and "
        "`#### Use case {U.C. n.m}` (the fully-dressed fields including Traceability, Main Success "
        "Scenario with numbered steps, Extensions). Nothing else."
    ),
    "p3a_prin": (
        "Wrap your answer: return ONLY one ```markdown fenced block. One `### <objective-id>` "
        "block per constraint you propose; an empty fenced block is a valid answer when the "
        "principle adds nothing for these objectives."),
    "p3a_propose": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing one `### <objective-id>` "
        "section per target objective, in the order given, each with exactly these bold fields: "
        "**Constraint (EARS)**, **Fit criterion**, **Risk addressed**, **Chain anchors**, "
        "**Proposed carrier**. Nothing else."
    ),
    "p3a_org": (
        "Wrap your answer: return ONLY one ```markdown fenced block containing the organizational "
        "requirement card as bold fields: **Statement (EARS)**, **Requirement Origin**, "
        "**Fit criterion**, **Verification Method**, **Chain**, **Control Anchors**, "
        "**Dependencies**, **Priority**. Do not allocate the ORG id — the pipeline does that. Nothing else."
    ),
    "p3a_weave": (
        "Wrap your answer: return ONLY one ```markdown fenced block starting with `#### Card <id>` "
        "and containing the bold fields **Preconditions**, **Extensions**, **Constraints absorbed** "
        "(the security preconditions and exception extensions the accepted constraints impose on "
        "this card's use case). Nothing else."
    ),
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
    elif step.startswith("p3a_prin"):
        d = steps_dir / "phase3a_prin"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{subdomain or step.split(':', 1)[1]}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8")
    elif step.startswith("p3a_map"):
        d = steps_dir / "phase3a_map"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{subdomain.replace('.', '_')}.json").write_text(
            json.dumps(parsed, indent=1), encoding="utf-8"
        )
    elif step == "p3a_cards":
        d = steps_dir / "phase3" / "cards"
        d.mkdir(parents=True, exist_ok=True)
        (d / "inventory.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    elif step.startswith("p3a_card:"):
        d = steps_dir / "phase3" / "cards"
        d.mkdir(parents=True, exist_ok=True)
        card_id = (subdomain or step.split(":", 1)[1]).replace(".", "_")
        (d / f"{card_id}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    elif step.startswith("p3a_propose:"):
        d = steps_dir / "phase3"
        d.mkdir(parents=True, exist_ok=True)
        sd = (subdomain or step.split(":", 1)[1]).replace(".", "_")
        (d / f"proposals_{sd}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    elif step.startswith("p3a_org:"):
        d = steps_dir / "phase3" / "org"
        d.mkdir(parents=True, exist_ok=True)
        slug = (subdomain or step.split(":", 1)[1]).replace(".", "_")
        (d / f"{slug}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
        )
    elif step.startswith("p3a_weave:"):
        d = steps_dir / "phase3" / "weave"
        d.mkdir(parents=True, exist_ok=True)
        card_id = (subdomain or step.split(":", 1)[1]).replace(".", "_")
        (d / f"{card_id}.json").write_text(
            json.dumps(parsed, indent=1, ensure_ascii=False), encoding="utf-8"
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
        self._p3a_prin_routed: list[dict] = []
        self._p3a_propose_targets: list[dict] = []
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
        elif step_kind.startswith("p3a_"):
            # wave 2/4/5/6 stages: p3a_cards, p3a_card:<id>, p3a_propose:<sd>,
            # p3a_org:<duty>, p3a_weave:<card> — each carries its own wrap
            # instruction and pack; they must NOT fall into the p4 catch-all.
            extra = EXTRA_INSTRUCTION[step_kind]
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
        if step == "p3a_cards":
            from aegis_pipeline.phases.phase3 import cards as _p3c
            return _p3c.parse_inventory(answer)
        if step.startswith("p3a_card:"):
            from aegis_pipeline.phases.phase3 import cards as _p3c
            return _p3c.check_card_quality(_p3c.parse_card(answer))
        if step.startswith("p3a_propose:"):
            from aegis_pipeline.phases.phase3 import proposals as _p3p
            sd = step.split(":", 1)[1]
            targets = [t for t in getattr(self, "_p3a_propose_targets", []) if t["subdomain"] == sd]
            return _p3p.parse_proposals(answer, targets)
        if step.startswith("p3a_org:"):
            from aegis_pipeline.phases.phase3 import org as _p3o
            return _p3o.parse_org_card(answer, duty=str(subdomain or step.split(":", 1)[1]))
        if step.startswith("p3a_weave:"):
            from aegis_pipeline.phases.phase3 import weave as _p3w
            return _p3w.parse_weave(answer)
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

    # ------------------------------------------------------------------
    # Phase 3 Part 1 — waves 2, 4, 5, 6 (PREREG_P3_01)
    # ------------------------------------------------------------------

    def _p3_merged_rows(self) -> tuple[list[dict], list[dict]]:
        import phase3 as p3

        phase2_doc = self.run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        if not phase2_doc.is_file():
            raise ValueError(f"no Phase 2 deliverable at {phase2_doc} — run --stage phase2 first")
        objectives = p3.load_objectives(phase2_doc)
        skeleton = p3.build(objectives)
        verdict_rows: list[dict] = []
        for path in sorted((self.run_dir / "steps" / "phase3").glob("verdicts_*.json")):
            verdict_rows.extend(json.loads(path.read_text(encoding="utf-8")))
        if not verdict_rows:
            raise ValueError("no verdicts stored — run --stage p3a_map first")
        return p3.apply_verdicts(skeleton, verdict_rows), objectives

    def stage_p3a_cards(self) -> int:
        from aegis_pipeline.phases.phase3 import cards as p3c

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        if not (self.run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md").is_file():
            raise ValueError("no Phase 2 deliverable — run --stage phase2 first")

        cards_dir = self.run_dir / "steps" / "phase3" / "cards"
        cards_dir.mkdir(parents=True, exist_ok=True)
        inventory_path = cards_dir / "inventory.json"
        calls = 0
        failures: list[str] = []
        if inventory_path.is_file():
            inventory = json.loads(inventory_path.read_text(encoding="utf-8"))["cards"]
        else:
            self._call("p3a_cards", None)
            if not self.dry_run:
                calls += 1
            if not inventory_path.is_file():
                if self.dry_run:
                    self._write_stage_result("p3a_cards", {
                        "status": "dry-run", "carried": 0, "selected": 0, "failed": 0,
                        "summary": "dry-run: prompts written, no inventory stored",
                    })
                    return calls
                raise FileNotFoundError(f"{inventory_path} was not written by _call")
            inventory = json.loads(inventory_path.read_text(encoding="utf-8"))["cards"]

        accepted: list[dict] = []
        for entry in inventory:
            cid = entry["id"]
            card_path = cards_dir / f"{cid.replace('.', '_')}.json"
            if card_path.is_file():
                accepted.append(json.loads(card_path.read_text(encoding="utf-8"))["card"])
                continue
            try:
                self._call(f"p3a_card:{cid}", cid)
                if not self.dry_run:
                    calls += 1
                if not card_path.is_file():
                    if self.dry_run:
                        continue
                    raise FileNotFoundError(f"{card_path} was not written by _call")
                card = json.loads(card_path.read_text(encoding="utf-8"))["card"]
                if card["id"] != cid:
                    raise ValueError(f"asked for {cid}, the card returned {card['id']}")
                accepted.append(card)
            except (LLMError, ValueError, KeyError, OSError) as e:
                failures.append(f"{cid}: {type(e).__name__}: {str(e)[:160]}")
                print(f"[p3a_cards] {cid} FAILED — continuing: {str(e)[:160]}", flush=True)

        if accepted:
            out_dir = self.run_dir / "outputs" / "phase3" / "v0_functional_baseline"
            out_dir.mkdir(parents=True, exist_ok=True)
            company = self.case.get("company_id", "company")
            (out_dir / "Doc01_Requirements_Elicitation_and_PUC.md").write_text(
                p3c.render_v0_doc01(accepted, company), encoding="utf-8"
            )
            (out_dir / "Doc02_System_Use_Cases.md").write_text(
                p3c.render_v0_doc02(accepted, company), encoding="utf-8"
            )

        # first-attempt acceptance: trace rows for card calls without an L0 repair
        trace_rows = [
            json.loads(line)
            for line in (self.run_dir / "trace.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip().startswith("{")
        ]
        card_calls = [r for r in trace_rows if str(r.get("step", "")).startswith("p3a_card_")]
        first_attempt = sum(
            1 for r in card_calls
            if r.get("status") == "ok" and not r.get("l0_retried")
        )

        summary = {
            "status": "ok" if not failures else "partial",
            "carried": len(accepted),
            "selected": len(inventory),
            "failed": len(failures),
            "summary": (
                f"{len(accepted)}/{len(inventory)} cards; first-attempt "
                f"{first_attempt}/{len(card_calls)} ({(first_attempt / len(card_calls) * 100):.0f}%"
                f" over {len(card_calls)} calls)" if card_calls else "no card calls yet"
            ),
            "first_attempt": first_attempt,
            "n_card_calls": len(card_calls),
            "failures": failures,
        }
        self._write_stage_result("p3a_cards", summary)
        self._raise_if_nothing_carried("p3a_cards", summary, "inventory failed or every card failed")
        return calls

    def stage_p3a_propose(self) -> int:
        from aegis_pipeline.phases.phase3 import proposals as p3p

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        rows, objectives = self._p3_merged_rows()
        targets = p3p.select_proposal_targets(rows)
        if not targets:
            self._write_stage_result("p3a_propose", {
                "status": "ok", "carried": 0, "selected": 0, "failed": 0,
                "summary": "no rows flagged for proposal — nothing to propose",
            })
            return 0
        # _validate filters this list by the step's sub-domain
        self._p3a_propose_targets = targets

        by_sd: dict[str, list[dict]] = {}
        for target in targets:
            by_sd.setdefault(target["subdomain"], []).append(target)

        calls = 0
        failures: list[str] = []
        all_proposals: list[dict] = []
        for sd in sorted(by_sd):
            out_path = self.run_dir / "steps" / "phase3" / f"proposals_{sd.replace('.', '_')}.json"
            if out_path.is_file():
                all_proposals.extend(json.loads(out_path.read_text(encoding="utf-8"))["proposals"])
                continue
            try:
                self._call(f"p3a_propose:{sd}", sd)
                if not self.dry_run:
                    calls += 1
                if not out_path.is_file():
                    if self.dry_run:
                        continue
                    raise FileNotFoundError(f"{out_path} was not written by _call")
                parsed = json.loads(out_path.read_text(encoding="utf-8"))
                expected = {t["id"] for t in by_sd[sd]}
                got = {p["objective"] for p in parsed["proposals"]}
                if got != expected:
                    raise ValueError(f"proposals cover {sorted(got)}, expected {sorted(expected)}")
                findings = p3p.check_proposals(parsed["proposals"], rows, objectives)
                if findings:
                    raise ValueError(f"{len(findings)} finding(s): {findings[0]}")
                all_proposals.extend(parsed["proposals"])
            except (LLMError, ValueError, KeyError, OSError) as e:
                failures.append(f"{sd}: {type(e).__name__}: {str(e)[:160]}")
                print(f"[p3a_propose] {sd} FAILED — continuing: {str(e)[:160]}", flush=True)

        out_dir = self.run_dir / "outputs" / "phase3" / "analysis_v0_to_v1"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "STEP2_ROUND1_PROPOSAL_DERIVATION.md").write_text(
            p3p.render_proposal_derivation(all_proposals), encoding="utf-8"
        )
        summary = {
            "status": "ok" if not failures else "partial",
            "carried": len(all_proposals),
            "selected": len(targets),
            "failed": len(failures),
            "summary": f"{len(all_proposals)}/{len(targets)} proposal(s) valid",
            "failures": failures,
        }
        self._write_stage_result("p3a_propose", summary)
        self._raise_if_nothing_carried("p3a_propose", summary, "every proposal call failed")
        return calls

    def stage_p3a_prin(self) -> int:
        """Principle-seeded constraint synthesis — one call per engineering principle.

        The matrix routes an objective organizational for want of a functional
        carrier, and a principle is what says which of those the PRODUCT must
        carry. Without this pass the principles are decorative: PRINCIPLE_MAPPING
        stays a skeleton, and transport protection (a PRIN-ENG-01 binding in the
        hand-written case, RN24) lands in the organizational lane because nothing
        ever proposed the constraint that would give it a card.

        Proposals join the same human round as the objective-driven ones and are
        stored in the `proposals_*.json` shape `p3a_round` already collects.
        """
        from aegis_pipeline.phases.phase3 import principles_constraints as p3pc

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        rows, _objectives = self._p3_merged_rows()
        # _p3_merged_rows returns the baseline rows with the verdicts applied; the
        # gate check_principle_proposals reads `anchors`, so a row that lost them
        # in the merge would make every anchor look outside the published set.
        routed = [r for r in rows
                  if r["verdict"] == "No functional carrier (organizational)"]
        principles = p3pc.canonical_principles()
        store = self.run_dir / "steps" / "phase3"
        cards = [json.loads(p.read_text(encoding="utf-8"))["card"]
                 for p in sorted((store / "cards").glob("R*.json"))]

        # _validate parses inside _call and has no view of the routed set; the
        # propose stage hands its targets over the same way.
        self._p3a_prin_routed = routed

        calls = 0
        failures: list[str] = []
        proposals: list[dict] = []
        for index, principle in enumerate(principles, start=1):
            out_path = store / f"proposals_prin_{index:02d}.json"
            if out_path.is_file():
                proposals.extend(json.loads(out_path.read_text(encoding="utf-8"))["proposals"])
                continue
            try:
                self._call(f"p3a_prin:{principle['id']}", principle["id"])
                stored = self.run_dir / "steps" / "phase3a_prin" / f"{principle['id']}.json"
                if not stored.is_file():
                    raise FileNotFoundError(f"{stored} was not written by _call")
                parsed = json.loads(stored.read_text(encoding="utf-8"))["proposals"]
                findings = p3pc.check_principle_proposals(parsed, routed)
                if findings:
                    raise ValueError(f"{len(findings)} finding(s): {findings[0]}")
                if not self.dry_run:
                    calls += 1
                proposals.extend(parsed)
                out_path.write_text(json.dumps({"proposals": parsed}, indent=1,
                                               ensure_ascii=False), encoding="utf-8")
            except (LLMError, ValueError, KeyError, OSError) as e:
                failures.append(f"{principle['id']}: {type(e).__name__}: {str(e)[:160]}")
                print(f"[p3a_prin] {principle['id']} FAILED — continuing: {str(e)[:160]}",
                      flush=True)

        self._write_stage_result("p3a_prin", {
            "status": "ok" if not failures else "partial",
            "carried": len(proposals), "selected": len(principles), "failed": len(failures),
            "summary": f"{len(proposals)} principle constraint(s) from "
                       f"{len(principles) - len(failures)}/{len(principles)} principles",
            "principles": [p["id"] for p in principles],
            "proposing": sorted({p["principle"] for p in proposals}),
            "failures": failures,
        })
        return calls

    def stage_p3a_round(self) -> int:
        from aegis_pipeline.phases.phase3 import proposals as p3p

        all_proposals: list[dict] = []
        for path in sorted((self.run_dir / "steps" / "phase3").glob("proposals_*.json")):
            all_proposals.extend(json.loads(path.read_text(encoding="utf-8"))["proposals"])
        if not all_proposals:
            raise ValueError("no proposals stored — run --stage p3a_propose first")

        verdicts_path = self.run_dir / "steps" / "phase3" / "round1_verdicts.json"
        marker = self.run_dir / "steps" / "gates" / "G-P3-A.approved"
        out_dir = self.run_dir / "outputs" / "phase3" / "synthesis_rounds"
        out_dir.mkdir(parents=True, exist_ok=True)

        if not marker.exists() or not verdicts_path.is_file():
            # Sem marcador OU marcador pré-aprovado sem veredictos: o estado é
            # PROPOSTED — nunca CONCLUDED (doc 08, two states; o fecho por
            # construção é o modo de falha que a ronda existe para evitar).
            if not verdicts_path.is_file():
                verdicts_path.write_text(
                    json.dumps(
                        {"verdicts": {},
                         "instructions": "enter Accept|Reject|Adjust per objective id"},
                        indent=1, ensure_ascii=False,
                    ),
                    encoding="utf-8",
                )
            (out_dir / "ROUND1_REGISTER.md").write_text(
                p3p.render_round_register(all_proposals, {}, converged=False),
                encoding="utf-8",
            )
            self._write_stage_result("p3a_round", {
                "status": "partial",
                "carried": 0,
                "selected": len(all_proposals),
                "failed": 0,
                "summary": (
                    f"{len(all_proposals)} proposal(s) recorded — PROPOSED, not concluded: "
                    "enter verdicts in steps/phase3/round1_verdicts.json and create the "
                    "G-P3-A marker, then re-run this stage"
                ),
            })
            return 0

        verdict_map = json.loads(verdicts_path.read_text(encoding="utf-8")).get("verdicts", {})
        state = p3p.apply_round_verdicts(all_proposals, verdict_map)
        (self.run_dir / "steps" / "phase3" / "round1_state.json").write_text(
            json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8"
        )
        (out_dir / "ROUND1_REGISTER.md").write_text(
            p3p.render_round_register(all_proposals, verdict_map, converged=state["converged"]),
            encoding="utf-8",
        )
        self._write_stage_result("p3a_round", {
            "status": "ok" if state["converged"] else "partial",
            "carried": len(state["accepted"]),
            "selected": len(all_proposals),
            "failed": 0,
            "summary": (
                f"{len(state['accepted'])} accepted / {len(state['rejected'])} rejected "
                f"(explicit risk acceptance) / {len(state['adjusted'])} adjusted / "
                f"{len(state['open'])} open"
            ),
            "open": state["open"],
        })
        return 0

    def stage_p3a_org(self) -> int:
        from aegis_pipeline.phases.phase3 import doc00 as p3d
        from aegis_pipeline.phases.phase3 import org as p3o

        self._require(("steps/fact_sheet.yaml",), "G-P1-A")
        state_path = self.run_dir / "steps" / "phase3" / "round1_state.json"
        if not state_path.is_file() or not json.loads(state_path.read_text(encoding="utf-8")).get("converged"):
            raise ValueError(
                "the acceptance round is not converged — the two-states rule blocks routing "
                "until the human verdicts land (run --stage p3a_round after G-P3-A)"
            )
        rows, _ = self._p3_merged_rows()

        audit_local = self.run_dir / "steps" / "phase3" / "duty_audit.md"
        audit_case = (
            self.repo / "cases" / self.case["case_id"] / "03_PHASE3_SPEC"
            / "part1_security_privacy" / "analysis_v0_to_v1"
            / "PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md"
        )
        audit_path = audit_local if audit_local.is_file() else audit_case
        if not audit_path.is_file():
            raise ValueError(
                "no proportionality audit found — the duty grouping is human input "
                "(the 1:1 routing rule is the recorded failure); provide "
                "steps/phase3/duty_audit.md in the Case 01 audit's §3 table format"
            )
        duty_map = p3o.parse_duty_audit(audit_path)
        duties = p3o.group_duties(rows, duty_map)
        dispositions = p3o.count_dispositions(duties)
        for index, duty in enumerate(duties, start=1):
            duty["slug"] = f"duty_{index:02d}"
        (self.run_dir / "steps" / "phase3" / "duties.json").write_text(
            json.dumps(duties, indent=1, ensure_ascii=False), encoding="utf-8"
        )

        org_dir = self.run_dir / "steps" / "phase3" / "org"
        org_dir.mkdir(parents=True, exist_ok=True)
        calls = 0
        failures: list[str] = []
        org_duties = [d for d in duties if "ORG" in d["dispositions"]]

        # The warrants are human input and the pack carries them verbatim, so a
        # warrant that violates R5 hands the model a term the gate will reject
        # on every attempt. `duty_20` failed twice on exactly that: the audit
        # reads "Enforce TLS 1.3 on external interfaces". Checked here rather
        # than in the loop because one bad warrant otherwise costs 20 good
        # calls — the same reason the skeleton is gated before the first call.
        from aegis_pipeline.guards.quality_gates import check_no_technology
        tainted = []
        for duty in org_duties:
            for warrant in duty.get("warrants", []):
                hits = check_no_technology(str(warrant))
                if hits:
                    tainted.append(f"{duty['slug']}: {hits[0][:120]}")
        if tainted:
            raise ValueError(
                f"{len(tainted)} organizational warrant(s) carry technology vocabulary "
                f"(R5). The warrants are the proportionality audit's own wording and "
                f"the pack reproduces them verbatim, so the model cannot produce a "
                f"card the gate would accept. Re-word the warrant in the audit, or "
                f"record the carve-out. First: {tainted[0]}"
            )

        cards: list[dict] = []
        for duty in org_duties:
            out_path = org_dir / f"{duty['slug']}.json"
            if out_path.is_file():
                cards.append(json.loads(out_path.read_text(encoding="utf-8")))
                continue
            try:
                self._call(f"p3a_org:{duty['slug']}", duty["slug"])
                if not self.dry_run:
                    calls += 1
                if not out_path.is_file():
                    if self.dry_run:
                        continue
                    raise FileNotFoundError(f"{out_path} was not written by _call")
                parsed = json.loads(out_path.read_text(encoding="utf-8"))
                p3o.check_org_anchor_files(self.repo, parsed)
                cards.append(parsed)
            except (LLMError, ValueError, KeyError, OSError) as e:
                failures.append(f"{duty['slug']}: {type(e).__name__}: {str(e)[:160]}")
                print(f"[p3a_org] {duty['slug']} FAILED — continuing: {str(e)[:160]}", flush=True)

        company = self.case.get("company_id", "company")
        confirmed = confirmed_regulations(self.run_dir)
        if cards:
            out_dir = self.run_dir / "outputs" / "phase3" / "part1_security_privacy"
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "Doc03_Organizational_Requirements.md").write_text(
                p3o.render_doc03(org_duties, cards, company, confirmed), encoding="utf-8"
            )
            # Doc00 — composed, never generated (doc 08 wave 5)
            v2_dir = self.run_dir / "outputs" / "phase3" / "v2_security_privacy_synthesis"
            v2_dir.mkdir(parents=True, exist_ok=True)
            tb_rows = [r for r in rows if (r.get("skill") or "") == "TB"]
            (v2_dir / "Doc00_Process_and_Operational_Workflows.md").write_text(
                p3d.render_doc00(company, p3d.load_fact_sheet(self.run_dir), p3d.load_cards(self.run_dir), tb_rows),
                encoding="utf-8",
            )
        summary = {
            "status": "ok" if not failures else "partial",
            "carried": len(cards),
            "selected": len(org_duties),
            "failed": len(failures),
            "summary": (
                f"{len(duties)} duties from {sum(1 for r in rows if r['verdict'] == p3o.ORG_VERDICT)} "
                f"organizational rows ({dispositions['ORG']} ORG / {dispositions['SCALE']} SCALE / "
                f"{dispositions['CARRIED']} CARRIED); {len(cards)} ORG cards; "
                "SCALE duties pending the proportionality decision (G-c)"
            ),
            "dispositions": dispositions,
            "failures": failures,
        }
        self._write_stage_result("p3a_org", summary)
        self._raise_if_nothing_carried("p3a_org", summary, "every org card failed")
        return calls

    def stage_p3a_weave(self) -> int:
        from aegis_pipeline.phases.phase3 import weave as p3w

        state_path = self.run_dir / "steps" / "phase3" / "round1_state.json"
        if not state_path.is_file() or not json.loads(state_path.read_text(encoding="utf-8")).get("converged"):
            raise ValueError("the acceptance round is not converged — run --stage p3a_round first")
        state = json.loads(state_path.read_text(encoding="utf-8"))
        accepted = state.get("accepted", [])
        rows, _ = self._p3_merged_rows()

        cards_dir = self.run_dir / "steps" / "phase3" / "cards"
        card_files = sorted(cards_dir.glob("R*.json"))
        if not card_files:
            raise ValueError("no generated cards — run --stage p3a_cards first")

        # Accepted proposals whose carrier is `new` have no card to weave into.
        # They get one each, derived deterministically from the proposal itself —
        # the D1 path the hand-written Round 1 used for R8.3. Allocation, not
        # generation: the constraint is the description, the fit criterion is the
        # acceptance bar, and no model call is involved.
        from aegis_pipeline.phases.phase3.proposals import allocate_new_cards
        new_cards = allocate_new_cards(
            accepted, [p.stem.replace("_", ".") for p in card_files])
        for card in new_cards:
            stem = card["id"].replace(".", "_")
            (cards_dir / f"{stem}.json").write_text(
                json.dumps({"card": card}, indent=1, ensure_ascii=False),
                encoding="utf-8")
        if new_cards:
            card_files = sorted(cards_dir.glob("R*.json"))
            print(f"[p3a_weave] allocated {len(new_cards)} new card(s) from "
                  f"accepted `new` proposals: "
                  f"{', '.join(c['id'] for c in new_cards)}", flush=True)
        # a proposal routed to an existing card carries its real id; the stored
        # `new` ones are now covered by the allocation above
        card_by_objective = {
            obj: card["id"]
            for card in new_cards for obj in card["objectives"]
        }
        for proposal in accepted:
            if (proposal.get("carrier") or "").strip("`") == "new":
                proposal["carrier"] = f"`{card_by_objective[proposal['objective']]}`"
        # Persist the rewrite: the weave pack is built inside `_call` from
        # round1_state.json, and an in-memory-only rewrite meant the stage
        # routed 12 proposals while the pack handed the model zero of them.
        (self.run_dir / "steps" / "phase3" / "round1_state.json").write_text(
            json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")

        card_ids = {p.stem: p.stem.replace("_", ".") for p in card_files}

        calls = 0
        failures: list[str] = []
        woven: dict[str, dict] = {}
        for stem, real_id in card_ids.items():
            routed = [p for p in accepted if (p.get("carrier") or "").strip("`") == real_id]
            if not routed:
                continue
            out_path = self.run_dir / "steps" / "phase3" / "weave" / f"{stem}.json"
            if out_path.is_file():
                woven[real_id] = json.loads(out_path.read_text(encoding="utf-8"))
                continue
            try:
                self._call(f"p3a_weave:{real_id}", real_id)
                if not self.dry_run:
                    calls += 1
                if not out_path.is_file():
                    if self.dry_run:
                        continue
                    raise FileNotFoundError(f"{out_path} was not written by _call")
                woven[real_id] = json.loads(out_path.read_text(encoding="utf-8"))
            except (LLMError, ValueError, KeyError, OSError) as e:
                failures.append(f"{real_id}: {type(e).__name__}: {str(e)[:160]}")
                print(f"[p3a_weave] {real_id} FAILED — continuing: {str(e)[:160]}", flush=True)

        cards = [json.loads(p.read_text(encoding="utf-8"))["card"] for p in card_files]
        out_dir = self.run_dir / "outputs" / "phase3" / "synthesis_rounds"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "STEP4_CONSTRAINT_ABSORPTION.md").write_text(
            p3w.render_step4(accepted, cards), encoding="utf-8"
        )
        uc_lines = ["---", "title: 'UC_OBJECTIVE_CORRESPONDENCE'", "generated_by: 'p3a_weave (wave 6)'", "---", "", "| Objective | Carrier | Use case |", "|---|---|---|"]
        for row in rows:
            carrier = (row.get("carrier") or "—").strip("`")
            uc = next((c["usecase"]["uc_id"] for c in cards if c["id"] == carrier), "—")
            uc_lines.append(f"| `{row['id']}` | {carrier} | {uc} |")
        uc_lines.append("")
        (out_dir / "UC_OBJECTIVE_CORRESPONDENCE.md").write_text("\n".join(uc_lines), encoding="utf-8")

        # Re-routing + matrix re-render, post-allocation and post-round. The
        # matrix on disk was last written by `p3a_map`, before the round — the 12
        # accepted constraints were never reflected in it. Re-routing runs first
        # so the render sees the moved verdicts, and it moves only in one
        # direction: organizational -> partially covered under an accepted
        # constraint. Nothing becomes "Fully covered" by code decision.
        from aegis_pipeline.phases.phase3 import principles_constraints as _p3pc
        principle_accepted = [a for a in accepted if a.get("principle")]
        for a in accepted:
            a.setdefault("allocated_card", card_by_objective.get(a["objective"], "new"))
        rows, moved = _p3pc.reroute_objectives(rows, accepted)
        if moved:
            print(f"[p3a_weave] re-routed {moved} objective(s) to a principle-derived card",
                  flush=True)
        grouped = {d: [r for r in rows if r["subdomain"].startswith(d)] for d in sorted({r["subdomain"][:4] for r in rows})}
        from aegis_pipeline.phases.phase3 import skeleton as _p3sk
        (out_dir / "OBJECTIVE_MAPPING.md").write_text(
            _p3sk.render_matrix(rows, grouped, _p3sk.domain_names_from(self.repo / "baseline/domains/index.md")),
            encoding="utf-8")
        (out_dir / "PRINCIPLE_MAPPING.md").write_text(
            _p3pc.render_principle_mapping(rows, accepted), encoding="utf-8")
        (out_dir / "SUFFICIENCY_ASSESSMENT.md").write_text(
            p3w.render_sufficiency(rows, state, confirmed_regulations(self.run_dir)),
            encoding="utf-8",
        )
        # mechanical injection: the v1 Doc01 carries the accepted constraint blocks
        v1_dir = self.run_dir / "outputs" / "phase3" / "v1_security_privacy_synthesis"
        v1_dir.mkdir(parents=True, exist_ok=True)
        v1 = ["---", "title: 'Doc01 v1 — Requirements Specification (constraints absorbed)'", "generated_by: 'p3a_weave (wave 6)'", "---", ""]
        for proposal in accepted:
            v1 += [
                f"### Constraint from `{proposal['objective']}` → carrier {proposal.get('carrier', '—')}",
                "",
                f"**Constraint (EARS):** {proposal['constraint']}",
                "",
                f"**Fit criterion:** {proposal['fit_criterion']}",
                "",
            ]
        if woven:
            v1 += ["## Use case security preconditions and extensions (woven)", ""]
            for real_id, block in sorted(woven.items()):
                v1 += [f"#### Card {real_id}", "", f"**Preconditions:** {block.get('Preconditions', '—')}", "", f"**Extensions:** {block.get('Extensions', '—')}", ""]
        (v1_dir / "Doc01_Requirements_Specification.md").write_text("\n".join(v1), encoding="utf-8")

        summary = {
            "status": "ok" if not failures else "partial",
            "carried": len(woven),
            "selected": len({(p.get("carrier") or "").strip("`") for p in accepted} - {""}),
            "failed": len(failures),
            "summary": f"{len(woven)} card(s) woven with {len(accepted)} accepted constraint(s)",
            "failures": failures,
        }
        self._write_stage_result("p3a_weave", summary)
        self._raise_if_nothing_carried("p3a_weave", summary, "every weave call failed")
        return calls

    def stage_p3a_gate(self) -> int:
        from aegis_pipeline.phases.phase3 import weave as p3w

        report = p3w.run_gate(self.run_dir, self.repo)
        out_dir = self.run_dir / "steps" / "phase3"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "gate_report.md").write_text(p3w.render_gate_report(report), encoding="utf-8")
        print(f"AEGIS_P3_GATE state={report['state']} " + " ".join(
            f"{g}={'CLOSED' if v.startswith('CLOSED') else 'OPEN'}" for g, v in report["gates"].items()
        ), flush=True)
        self._write_stage_result("p3a_gate", {
            "status": "ok" if report["state"] == "CONCLUDED" else "partial",
            "carried": 1 if report["state"] == "CONCLUDED" else 0,
            "selected": 1,
            "failed": 0,
            "summary": (
                f"state={report['state']}; "
                + "; ".join(f"{g} {v.split(' — ')[0]}" for g, v in report["gates"].items())
            ),
            "gates": report["gates"],
            "findings": report["findings"][:20],
            "n_objectives": report["n_objectives"],
        })
        return 0

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
