#!/usr/bin/env python3
"""agent/loop.py — the directed agent runner.

One process drives the whole Phase 1 task as a tool-calling conversation with
qwen (multi-turn /api/chat, `tools:` schema). Design invariants:

- State on disk is authoritative (ADR-010): every accepted submission is a
  steps/ artifact written by the pipeline's own store_parsed; the conversation
  transcript (agent_conversation.jsonl) is a checkpoint, not the state.
- The context window cannot hold 22 corpus modules, so after each turn the
  oldest LARGE tool observations are elided from the working history (they can
  always be re-read); submissions and errors stay.
- Every turn leaves the same forensics as a pipeline call: inputs/, outputs/,
  one trace.jsonl record, manifest counters. The inspector shows agent turns
  and pipeline calls in the same table.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from llm import LLMError, OllamaClient  # noqa: E402
import runconfig  # noqa: E402
from steps import build_run_notes  # noqa: E402
from trace import Trace, count_calls, now_iso, update_manifest  # noqa: E402

from .prompt import SYSTEM_BRIEF, user_opener  # noqa: E402
from .tools import AgentToolbox, execute_tool, tool_schemas  # noqa: E402

NUM_CTX = 32768
# 65536 was an arithmetic wall for late-stage conversations: loading a ~30k
# pack (D-09.4) on top of ~200 turns of history degraded the model into
# tool-less prose (EXP-03 r01, 2026-10-03: 12 turns with no tool calls, 4
# goals never written). The pipeline arm never hits this because each of its
# calls is context-independent. Raised for the agent arm only; every agent
# run gets the same ceiling.
# raised to the models' declared native max (ollama api/show: qwen3.8 and
# gemma4 = 262144, muse-glimmer = 131072 — researcher instruction, 2026-10-03);
# the gradual escalation below only ever requests what the conversation needs
NUM_CTX_MAX = 262144
NUM_PREDICT = 8192
# tokens above which a tool observation is eligible for history elision
ELIDE_THRESHOLD_CHARS = 4_000


def _msg_tokens(messages: list[dict]) -> int:
    return sum(len(json.dumps(m, ensure_ascii=False)) for m in messages) // 4


def _elide(messages: list[dict], budget_tokens: int) -> int:
    """Shrink the working history until it fits the context budget.
    Pass 1 elides the oldest large tool RESULTS; pass 2 elides old assistant
    tool_call ARGUMENTS (submitted tables live in steps/ artifacts — the
    conversation copy is disposable). The last 8 messages are never touched.
    Returns the number of elisions."""
    elided = 0
    while _msg_tokens(messages) > budget_tokens:
        victim = None
        for m in messages:
            if m.get("role") == "tool" and not m.get("_elided") \
                    and len(m.get("content", "")) > ELIDE_THRESHOLD_CHARS:
                victim = m
        if victim is None:
            break
        name = victim.get("tool_name", "read")
        victim["content"] = (f"[elided {name} result — too large to keep in history; "
                             f"state is on disk, call the read tool again if needed]")
        victim["_elided"] = True
        elided += 1
    # pass 2: compress old SUBMISSION turns entirely — tool_calls in history are
    # imitation bait (qwen re-emits what it sees, including elision markers, and
    # a half-imitated tool call 400s the server). Replace the assistant turn
    # with a plain-text note and drop its tool result: nothing left to imitate.
    i = 0
    while _msg_tokens(messages) > budget_tokens and i < len(messages) - 8:
        m = messages[i]
        if m.get("role") == "assistant" and m.get("tool_calls"):
            names = ", ".join(tc.get("function", {}).get("name", "?")
                              for tc in m["tool_calls"])
            m.pop("tool_calls")
            m["content"] = (m.get("content", "") +
                            f"\n[{names}: earlier submission elided — it is stored as a "
                            f"steps/ artifact]").strip()
            j = i + 1
            while j < len(messages) and messages[j].get("role") == "tool":
                messages.pop(j)
            elided += 1
            continue
        i += 1
    return elided


class AgentRunner:
    def __init__(self, repo: Path, run_dir: Path, model: str, base: str,
                 transport: str = "tools", max_turns: int = 80,
                 dry_run: bool = False):
        self._call_counts: dict[tuple, int] = {}
        self.repo = repo
        self.run_dir = run_dir
        self.model = model
        self.base = base
        self.transport = transport
        self.max_turns = max_turns
        self.dry_run = dry_run
        # Same config.json, same sampler plumbing as the pipeline arm. EXP-03
        # compares the two, so a difference in how they are sampled would be
        # indistinguishable from a difference in how they are orchestrated.
        self.config = runconfig.load(run_dir)
        self.temperature = float(self.config.get("temperature", 0.2))
        self.sampler = runconfig.sampler_options(self.config)
        manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
        self.case_id = manifest["case_id"]
        self.trace = Trace(run_dir)
        self._client: OllamaClient | None = None
        self.toolbox = AgentToolbox(repo, self.case_id, run_dir)
        self.schemas = tool_schemas()
        self.messages: list[dict] = []
        self.transcript = run_dir / "agent_conversation.jsonl"

    def client(self) -> OllamaClient:
        if self._client is None:
            self._client = OllamaClient(self.base)
        return self._client

    # ---- conversation persistence -------------------------------------------

    def _load_conversation(self) -> bool:
        if not self.transcript.exists():
            return False
        for line in self.transcript.read_text(encoding="utf-8").splitlines():
            if line.strip():
                self.messages.append(json.loads(line))
        return len(self.messages) > 0

    def _checkpoint(self, *msgs: dict) -> None:
        with self.transcript.open("a", encoding="utf-8") as f:
            for m in msgs:
                f.write(json.dumps(m, ensure_ascii=False) + "\n")

    # ---- one turn --------------------------------------------------------------

    def _call_llm(self) -> tuple[dict, dict]:
        """One LLM turn: returns (raw_response, assistant_message). Retries once
        on transport failure or truncation (same policy as the pipeline)."""
        client = self.client()
        client.ensure_model_cached(self.model)
        # Phase-scoped tool surface: the planner knows the phase, so expose only
        # that phase's tools. Feeding all 13 every turn measurably degrades tool
        # selection for this model class; the hot path needs 4-6.
        phase, _d = self._plan()
        self._tools_phase = phase
        # elide BEFORE the fit checks: freeing old read observations is how a
        # 22-sub-domain conversation stays inside one context window
        num_ctx = NUM_CTX
        _elide(self.messages, num_ctx - NUM_PREDICT - 2000)
        est = _msg_tokens(self.messages)
        # gradual escalation: double the window until the conversation fits,
        # capped at the models' declared native max (262144 for qwen3.8 /
        # gemma4; 131072 for muse-glimmer — Ollama serves the request, the
        # model's own limit governs). A single jump to the max would allocate
        # a 262k KV cache for calls that only need 64k.
        while est * 1.15 + NUM_PREDICT + 2000 > num_ctx and num_ctx < NUM_CTX_MAX:
            num_ctx = min(num_ctx * 2, NUM_CTX_MAX)
            _elide(self.messages, num_ctx - NUM_PREDICT - 2000)
            est = _msg_tokens(self.messages)
        if est * 1.15 + NUM_PREDICT + 2000 > num_ctx:
            raise LLMError(f"conversation ~{est} tokens does not fit even {NUM_CTX_MAX} ctx")

        raw, answer = None, None
        for attempt in (1, 2):
            seq = self.trace.next_seq()
            t0 = time.time()
            try:
                raw = client.chat_messages(
                    self.model, self.messages, num_ctx,
                    temperature=self.temperature,
                    num_predict=NUM_PREDICT,
                    sampler=self.sampler,
                    tools=self._active_schemas() if self.transport == "tools" else None)
                msg = raw.get("message", {})
                answer = msg.get("content", "")
                dr = raw.get("done_reason")
                n_tools = len(msg.get("tool_calls") or [])
                ok = dr == "stop" and (answer.strip() or n_tools)
                rec = {
                    "seq": seq, "step": f"turn{self._turn_no()}", "mode": "agentic",
                    "model": self.model, "num_ctx": num_ctx, "num_predict": NUM_PREDICT,
                    "temperature": self.temperature,
                    **{f"sampler_{k}": self.sampler.get(k) for k in runconfig.SAMPLER_KEYS},
                    "ts_start": now_iso(),
                    "transport": self.transport,
                    "history_msgs": len(self.messages),
                    "history_est_tokens": est,
                    "attempt": attempt,
                    "attempt1_done_reason": dr,
                    "attempt1_eval_tokens": raw.get("eval_count"),
                    "attempt1_prompt_tokens": raw.get("prompt_eval_count"),
                    "attempt1_latency_s": round(time.time() - t0, 1),
                }
                in_dir = self.run_dir / "inputs"
                out_dir = self.run_dir / "outputs"
                if not ok:
                    rec["attempt1_error"] = (
                        f"empty turn (done_reason={dr}, {n_tools} tool_calls)" if not answer.strip()
                        else f"truncated turn (done_reason={dr})")
                    self._write_raw(out_dir, seq, raw)
                    self.trace.append({**rec, "status": "failed", "ts_end": now_iso()})
                    continue
                # conversation snapshot only for accepted turns: the L1 trace
                # check counts *_messages.json == *_turn_output.md == ok records
                rec["system_path"] = str(self._write_system_brief(in_dir))
                rec["user_path"] = str(self._write_history(in_dir, seq))
                rec["output_path"] = str(self._write_output(out_dir, seq, msg))
                rec["raw_path"] = str(self._write_raw(out_dir, seq, raw))
                rec["response_chars"] = len(answer)
                rec["tool_calls"] = n_tools
                self.trace.append({**rec, "status": "ok", "ts_end": now_iso()})
                return raw, msg
            except LLMError as e:
                self.trace.append({
                    "seq": seq, "step": f"turn{self._turn_no()}", "mode": "agentic",
                    "status": "failed", "attempt": attempt,
                    "attempt1_error": str(e)[:500], "ts_start": now_iso(),
                    "ts_end": now_iso(),
                })
                if attempt == 2:
                    raise
        raise LLMError("turn failed twice")

    # which tools each phase may call (a tool outside the set is refused with
    # the phase directive, so an illegal call costs one turn, not a loop)
    PHASE_TOOLS = {
        "brief": {"get_company_brief", "read_output_contract", "submit_fact_sheet", "get_state"},
        "verdicts": {"read_output_contract", "submit_verdicts", "get_state"},
        "selection": {"list_candidate_subdomains", "read_output_contract",
                      "submit_selection", "get_state"},
        "framing": {"read_output_contract", "submit_framing", "get_state"},
        "goals": {"read_regulation_module", "read_output_contract", "get_subso_objective",
                  "submit_goal", "get_state"},
        "tensions": {"read_regulation_module", "list_corpus_tensions",
                     "submit_tensions", "get_state"},
        "render": {"finalize", "get_state"},
        "done": {"finalize", "get_state"},
    }

    def _active_schemas(self) -> list[dict]:
        allowed = self.PHASE_TOOLS.get(getattr(self, "_tools_phase", ""), None)
        if allowed is None:
            return self.schemas
        return [s for s in self.schemas if s["function"]["name"] in allowed]

    def _turn_no(self) -> int:
        return sum(1 for m in self.messages if m.get("role") == "assistant") + 1

    # ---- per-turn forensics (same grammar as pipeline calls) -------------------

    def _write_system_brief(self, in_dir: Path) -> Path:
        p = in_dir / "000_agent_system_brief.md"
        if not p.exists():
            p.write_text(SYSTEM_BRIEF, encoding="utf-8")
        return p

    def _write_history(self, in_dir: Path, seq: int) -> Path:
        p = in_dir / f"{seq:03d}_messages.json"
        slim = [{k: v for k, v in m.items() if not k.startswith("_")} for m in self.messages]
        p.write_text("```json\n" + json.dumps(slim, indent=1, ensure_ascii=False) + "\n```\n",
                     encoding="utf-8")
        return p

    def _write_output(self, out_dir: Path, seq: int, msg: dict) -> Path:
        p = out_dir / f"{seq:03d}_turn_output.md"
        body = msg.get("content", "")
        calls = msg.get("tool_calls") or []
        if calls:
            body = (body + "\n\n" + "\n".join(
                f"> tool_call: {c.get('function', {}).get('name')}("
                f"{json.dumps(c.get('function', {}).get('arguments'), ensure_ascii=False)[:600]})"
                for c in calls)).strip()
        p.write_text(body + "\n", encoding="utf-8")
        return p

    def _write_raw(self, out_dir: Path, seq: int, raw: dict) -> Path:
        p = out_dir / f"{seq:03d}_response.json"
        p.write_text(json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8")
        return p

    # ---- tool dispatch -----------------------------------------------------------

    def _run_tool_calls(self, msg: dict) -> bool:
        """Execute every tool_call in the assistant message, append the results.
        Returns True when the run finished (finish accepted)."""
        finished = False
        for call in msg.get("tool_calls") or []:
            fn = call.get("function", {})
            name = fn.get("name", "")
            args = fn.get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args or "{}")
                except json.JSONDecodeError:
                    args = {}
            if isinstance(args, dict):
                args = {k: v for k, v in args.items() if not str(k).startswith("_")}
            # anti-loop guard: an exact repeat returns ONLY the refusal — a
            # warning appended to a 12K result drowns and qwen re-latches
            key = (name, json.dumps(args, sort_keys=True, ensure_ascii=False))
            self._call_counts[key] = self._call_counts.get(key, 0) + 1
            repeats = self._call_counts[key]
            if repeats >= 3 and name != "finalize":
                _phase, directive = self._plan()
                result = {"ok": False,
                          "error": f"REFUSED: identical call, already served "
                                   f"{repeats - 1} time(s) with the same result. Repeating it "
                                   f"cannot change anything.",
                          "next_step": directive}
            else:
                try:
                    result = execute_tool(self.toolbox, name, args)
                except Exception as e:  # tool crashed: tell the model, not the void
                    result = {"ok": False,
                              "error": f"tool {name} crashed: {type(e).__name__}: {e}"}
            # finalize assembling + validating cleanly is the run's terminal step
            if name == "finalize" and isinstance(result, dict) and result.get("ok"):
                finished = True
            content = json.dumps(result, ensure_ascii=False)
            if self.transport == "tools":
                self.messages.append({"role": "tool", "content": content[:60_000],
                                      "tool_name": name})
            else:
                self.messages.append({
                    "role": "user",
                    "content": f"TOOL RESULT ({name}):\n{content[:60_000]}"})
            self._checkpoint(self.messages[-1])
        return finished


    # ---- planner: the committed work list, owned by code, not by the model --
    #
    # Prompt instructions to stop repeating are unreliable (openclaw#78865:
    # "the model ignored them because in the moment it genuinely believes the
    # next retry might work"). With an enumerable plan we have ground truth
    # about what remains, so a repeat is refused with the NEXT step, not a
    # warning — and the step is placed at the END of the context, where
    # long-context models attend best (Lost in the Middle, TACL 2024).

    def _plan(self) -> tuple[str, str]:
        """(phase, directive) — the single next thing to do."""
        tb = self.toolbox
        steps = self.run_dir / "steps"
        if not (steps / "fact_sheet.yaml").exists():
            return "brief", ("Call get_company_brief, then read_output_contract step=p1, "
                             "then submit_fact_sheet.")
        if not (steps / "verdicts.json").exists():
            return "verdicts", ("Call read_output_contract step=p2, then submit_verdicts "
                                "(all 5 candidate regulations).")
        if not (steps / "selection.json").exists():
            return "selection", ("Call list_candidate_subdomains, then "
                                 "read_output_contract step=p3, then submit_selection.")
        if not (steps / "framing.md").exists():
            return "framing", ("Call read_output_contract step=p3f, then submit_framing.")
        sel_path = steps / "selection.json"
        if sel_path.exists():
            sel = json.loads(sel_path.read_text(encoding="utf-8"))
            remaining = [s["id"] for s in sel["selected"]
                         if not (steps / "goals" / f"{s['id'].replace('.', '_')}.json").exists()]
            if remaining:
                sd = remaining[0]
                regs = tb._expected_regs(sd) if sd else []
                if not regs:
                    # nothing to restate: do NOT send the model off to read the
                    # module — that is the dead end it looped on (D-08.3)
                    return "goals", (f"Work on {sd} ONLY ({len(remaining)} sub-domain(s) left). "
                                     f"This module carries NO Sub-SO for the confirmed "
                                     f"regulations, so it has no goal rows. Call submit_goal "
                                     f"once for {sd} (any short placeholder values are accepted) "
                                     f"to record the empty marker, then move on. Do NOT call "
                                     f"read_regulation_module for {sd}.")
                return "goals", (f"Work on {sd} ONLY ({len(remaining)} sub-domain(s) left, "
                                 f"this is {sd}). Call read_regulation_module subdomain={sd} "
                                 f"part=objective and part=regs, then submit_goal ONCE per "
                                 f"Sub-SO ({', '.join(regs)}). "
                                 f"If the job restarted you may skip reads you already did.")
        if not (steps / "tensions.json").exists():
            return "tensions", ("Call list_corpus_tensions to read the Emergent-tensions "
                                "passages, then submit_tensions with a T-NNN table for the "
                                "tensions that activate (or `None.` WITH none_reason naming "
                                "why none activates).")
        if not (self.run_dir / "doc02_adjusted_goals.md").exists():
            return "render", "Call finalize to assemble, validate and finish the run."
        return "done", "Call finalize to assemble, validate and finish the run."

    def _append_next_step(self) -> None:
        phase, directive = self._plan()
        self.messages.append({
            "role": "user",
            "content": f"[NEXT STEP — phase {phase}] {directive} Make this ONE tool call now."})
        self._checkpoint(self.messages[-1])

    # ---- finalize -------------------------------------------------------------------

    def _finalize(self, n_calls: int) -> None:
        doc = self.run_dir / "doc02_adjusted_goals.md"
        if not doc.exists():
            raise LLMError("finish accepted but doc02_adjusted_goals.md missing")
        (self.run_dir / "RUN_NOTES.md").write_text(build_run_notes(self.run_dir),
                                                   encoding="utf-8")
        # per-run export, same convention as stage_p5
        out_dir = (Path(os.environ.get("AEGIS_EXPORT_DIR", str(self.repo / "output")))
                   / self.toolbox.case["company_id"] / "phase1" / self.run_dir.name)
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(doc, out_dir / "doc02_adjusted_goals.md")
        shutil.copy(self.run_dir / "RUN_NOTES.md", out_dir / "RUN_NOTES.md")
        update_manifest(self.run_dir, mode="agentic",
                        n_calls_total=count_calls(self.run_dir))
        print(f"[agentic] L1 PASS; deliverable exported to {out_dir} "
              f"({n_calls} turns)", flush=True)

    # ---- main loop ---------------------------------------------------------------------

    def stage_agentic(self) -> int:
        if self.dry_run:
            print(f"[agentic] dry-run: {len(self.schemas)} tools registered, "
                  f"transport={self.transport} — no model calls")
            return 0
        resumed = self._load_conversation()
        if resumed:
            # re-anchor: after a crash/resume the model's last context may be a
            # degenerate read-loop — restate the on-disk state and the next move
            state = self.toolbox.get_state()
            self.messages.append({
                "role": "user",
                "content": "RESUME BRIEFING — the job was restarted; the conversation above "
                           "may contain repeated dead-end reads (they are refused now). "
                           f"Authoritative state on disk: {json.dumps(state)}. "
                           "Continue the working order from the state: verdicts done → "
                           "list_candidate_subdomains → submit_selection → submit_framing → "
                           "read each selected module ONCE → submit_goals per sub-domain → "
                           "submit_tensions → render_document → self_validate → finish. "
                           "Make the next move NOW with one tool call."})
            self._checkpoint(self.messages[-1])
            print(f"[agentic] resuming conversation with {len(self.messages)} message(s); "
                  f"state: {state['artifacts_present']}", flush=True)
        else:
            self.messages = [
                {"role": "system", "content": SYSTEM_BRIEF},
                {"role": "user", "content": user_opener(
                    [s["function"]["name"] for s in self.schemas],
                    self.max_turns, self.transport)},
            ]
            self._checkpoint(*self.messages)

        client = self.client()
        client.ensure_model_cached(self.model)
        client.warm_up(self.model, NUM_CTX)
        turn = 0
        stagnant = 0
        malformed = 0
        last_progress = self._progress_signature()
        while True:
            turn += 1
            if turn > self.max_turns:
                raise LLMError(f"turn budget exhausted ({self.max_turns}) — "
                               f"state is on disk; fix the blocker and re-enter stage agentic")
            try:
                raw, msg = self._call_llm()
            except LLMError as e:
                # qwen sometimes emits a tool_call whose arguments JSON the
                # server cannot parse (HTTP 400). Dropping the turn and asking
                # for a re-emit usually recovers; two in a row → abort.
                if "HTTP 400" in str(e) and malformed < 2:
                    malformed += 1
                    self.messages.append({
                        "role": "user",
                        "content": "NOTE: your previous tool call had malformed JSON "
                                   "arguments and the server rejected it. Re-emit the SAME "
                                   "tool call with valid, complete JSON arguments."})
                    self._checkpoint(self.messages[-1])
                    continue
                raise
            malformed = 0
            asst = {"role": "assistant", "content": msg.get("content", "")}
            if msg.get("tool_calls"):
                asst["tool_calls"] = msg["tool_calls"]
            self.messages.append(asst)
            self._checkpoint(asst)
            if self._run_tool_calls(msg):
                self._finalize(count_calls(self.run_dir))
                return turn
            self._append_next_step()
            # progress watchdog: no new artifact for N turns = degenerate loop;
            # abort cleanly so a resume re-anchors with the state briefing
            sig = self._progress_signature()
            if sig != last_progress:
                last_progress, stagnant = sig, 0
            else:
                stagnant += 1
                if stagnant >= 12:
                    raise LLMError(
                        f"no artifact progress in {stagnant} turns (degenerate loop?) — "
                        f"aborting; the resume briefing will re-anchor the model")

    def _progress_signature(self) -> tuple:
        """Cheap fingerprint of on-disk progress: artifacts present + goal counts."""
        tb = self.toolbox
        state = tb.get_state()
        return (tuple(state["artifacts_present"]),
                tuple(sorted(state["goals_per_subdomain"].items())))
