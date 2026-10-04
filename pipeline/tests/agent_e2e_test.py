#!/usr/bin/env python3
"""agent_e2e_test.py — full agent-loop test against a scripted fake Ollama.

Covers, with NO real model:
  1. llm.chat_messages tool-calling path (tools schema in, tool_calls out)
  2. the directed loop end-to-end: brief → fact sheet → verdicts → selection →
     framing → goals per sub-domain (FIRST submission defective: technology
     leakage rejected by the content gate, repaired on the named error) →
     tensions → render → self-validate → finish
  3. finish-gate rejections (finish before render is refused with findings)
  4. checkpoint/resume: a transport crash mid-loop aborts the stage; re-entering
     stage agentic reloads agent_conversation.jsonl and completes the task
  5. trace/manifest accounting for agent runs + L1 PASS on the final run dir
  6. export to AEGIS_EXPORT_DIR

Usage: python3 pipeline/tests/agent_e2e_test.py
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import threading
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from local_e2e_test import (CONFIRMED, FACT_SHEET, FRAMING_TABLE, MODEL,  # noqa: E402
                            SELECTED, TENSIONS_TABLE, VERDICT_TABLE, goals_answer,
                            selection_answer)
from compose import REGULATIONS, domain_dir  # noqa: E402


def REGULATIONS_IN(sd: str) -> list[str]:
    """The confirmed regulations whose Sub-SO card this module carries."""
    return [r for r in CONFIRMED
            if (domain_dir(REPO, sd) / "regs" / f"{r}.md").exists()
            and f"SG-{sd}.{r}" in
            (domain_dir(REPO, sd) / "regs" / f"{r}.md").read_text(encoding="utf-8")]

TMP = Path("/tmp/mvp_agent_e2e")
EXPORT_DIR = TMP / "export"
FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(name)


def unfence(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1].rsplit("```", 1)[0]
    return s.strip()


def fake_pack(sd: str) -> str:
    chunks = []
    for reg in CONFIRMED:
        p = domain_dir(REPO, sd) / "regs" / f"{reg}.md"
        if p.exists():
            chunks.append(f"----- BEGIN FILE: {p} -----\n"
                          f"{p.read_text(encoding='utf-8')}\n----- END FILE")
    return "\n".join(chunks)


def leak_cell(goal: str) -> str:
    """Inject a technology term — check_no_technology must reject it, giving the
    loop its repair scenario."""
    return goal + " The data is encrypted with AES-256 and transported over TLS 1.3."


_sent_rows: list = []


def tool_msg(name: str, args: dict) -> dict:
    return {"message": {"role": "assistant", "content": "",
                        "tool_calls": [{"function": {"name": name, "arguments": args}}]},
            "done_reason": "stop", "eval_count": 128, "total_duration": 1_000_000_000}


class FakeOllama(ThreadingHTTPServer):
    """Serves the next scripted tool call; inspects the conversation to decide
    repair branches. crash_mode returns HTTP 500s to force a stage abort."""

    def __init__(self):
        super().__init__(("127.0.0.1", 0), Handler)
        self.crash_mode = False
        self.chat_requests = 0
        self.script: list[dict] = []
        self.reads: set[str] = set()

    def build_script(self) -> list[dict]:
        """The exact tool-call sequence the fake model will emit, in order.
        Scripted, not derived from the conversation: this fixture tests the
        harness (transport, per-row flow, repair, planner, finalize), so its
        model side must not re-implement the state tracking under test."""
        script = [
            tool_msg("get_company_brief", {}),
            tool_msg("submit_fact_sheet", {"yaml_text": FACT_SHEET}),
            tool_msg("submit_verdicts", {"markdown_table": VERDICT_TABLE}),
            tool_msg("submit_selection", {"markdown": unfence(selection_answer())}),
            tool_msg("submit_framing", {"markdown_table": unfence(FRAMING_TABLE)}),
            tool_msg("read_output_contract", {"step": "p4"}),
        ]
        n = 0
        for sd in SELECTED:
            script.append(tool_msg("read_regulation_module",
                                   {"subdomain": sd, "part": "regs"}))
            tbl = unfence(goals_answer(sd, fake_pack(sd)))
            rows = [[x.strip().replace("|", "/") for x in l.split(" | ")]
                    for l in tbl.splitlines() if l.startswith(f"| AG-{sd}-")]
            if not rows:
                script.append(tool_msg("submit_goal", {
                    "subdomain": sd, "baseline_source": f"SG-{sd}.GDPR",
                    "goal": "no Sub-SO in this module", "implication": "n/a",
                    "pattern": "maintain", "property_name": "Confidentiality",
                    "source": "n/a", "adjustment": "unchanged — fits as stated"}))
                continue
            for r in rows:
                args = {"subdomain": sd, "baseline_source": r[6], "goal": r[1],
                        "implication": r[2], "pattern": r[3], "property_name": r[4],
                        "source": r[7], "adjustment": r[8]}
                if n == 0:
                    # first goal row of the run: defective on purpose, then the
                    # clean retry — the rejection is the repair signal
                    bad = dict(args)
                    bad["goal"] = leak_cell(r[1])
                    script.append(tool_msg("submit_goal", bad))
                n += 1
                script.append(tool_msg("submit_goal", args))
        script.append(tool_msg("list_corpus_tensions", {}))
        script.append(tool_msg("submit_tensions", {"markdown": unfence(TENSIONS_TABLE)}))
        script.append(tool_msg("finalize", {}))
        return script

    def next_call(self, messages: list[dict]) -> dict:
        n_assistant = sum(1 for m in messages if m.get("role") == "assistant")
        script = self.script
        if n_assistant < len(script):
            return script[n_assistant]
        # script exhausted: emit a repeat, then the planner's refusal must
        # eventually break the loop — echo the first goal read forever so the
        # watchdog/repetition guard is exercised, never finalize again
        return script[6]


class Handler(BaseHTTPRequestHandler):
    server: FakeOllama

    def log_message(self, *a):  # silence
        pass

    def _json(self, payload: dict, code: int = 200):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/tags":
            self._json({"models": [{"name": MODEL}]})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length))
        if self.path == "/api/chat":
            self.server.chat_requests += 1
            if self.server.crash_mode:
                self._json({"error": "cuda error: device-side assert"}, 500)
                return
            # warm-up: single "ping" message → tiny answer, no tools
            if len(payload.get("messages", [])) <= 2 and \
                    payload["messages"][-1]["content"] == "ping":
                self._json({"model": MODEL, "message": {"role": "assistant", "content": "ok"},
                            "done_reason": "stop", "eval_count": 1,
                            "total_duration": 100_000_000})
                return
            self._json(self.server.next_call(payload["messages"]))
        else:
            self._json({}, 404)


def run_cli(*args: str, expect_rc: int = 0) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ, AEGIS_EXPORT_DIR=str(EXPORT_DIR))
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "run_pipeline.py"), *args],
                          capture_output=True, text=True, env=env, timeout=600)
    if proc.returncode != expect_rc:
        print(proc.stdout[-1500:], proc.stderr[-1500:])
        check(f"cli {' '.join(args[:4])} rc={expect_rc}", False, f"got rc={proc.returncode}")
    return proc


def main() -> int:
    print("== agent e2e: scripted tool-calling loop (no real model) ==")
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True)
    srv = FakeOllama()
    srv.script = srv.build_script()
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    run_dir = TMP / "run_agent_TEST_000001"

    print("-- 1. new-run + dry-run schema check --")
    run_cli("new-run", "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(run_dir), "--model", MODEL)
    proc = run_cli("run", "--stage", "agentic", "--run-dir", str(run_dir),
                   "--base", base, "--dry-run")
    check("dry-run registers tools without calls", "tools registered" in proc.stdout)

    print("-- 2. crash mid-loop → abort with forensics, then resume --")
    srv.crash_mode = True
    proc = run_cli("run", "--stage", "agentic", "--run-dir", str(run_dir),
                   "--base", base, expect_rc=1)
    check("transport crash aborts the stage", "STAGE ABORTED" in proc.stderr)
    check("aborted stage recorded in manifest",
          any(s.get("status") == "aborted" for s in
              json.loads((run_dir / "manifest.json").read_text())["stage_history"]))
    check("conversation checkpoint survives the crash",
          (run_dir / "agent_conversation.jsonl").exists())

    srv.crash_mode = False
    # resume: the script continues where the conversation left off
    n_assistant = sum(1 for l in (run_dir / "agent_conversation.jsonl").read_text().splitlines()
                      if l.strip() and json.loads(l).get("role") == "assistant")
    srv.script = srv.script[n_assistant:]
    run_cli("run", "--stage", "agentic", "--run-dir", str(run_dir), "--base", base)
    man = json.loads((run_dir / "manifest.json").read_text())
    check("manifest mode=agentic", man.get("mode") == "agentic")
    check("final stage ok", man["stage_history"][-1]["status"] == "ok")

    print("-- 3. the full contract actually ran --")
    conv = [json.loads(l) for l in (run_dir / "agent_conversation.jsonl").read_text().splitlines()]
    tool_names = [m.get("tool_name") for m in conv if m.get("role") == "tool"]
    for t in ("get_company_brief", "submit_fact_sheet", "submit_verdicts",
              "submit_selection", "submit_framing", "read_output_contract",
              "submit_goal", "list_corpus_tensions", "submit_tensions", "finalize"):
        check(f"tool used: {t}", t in tool_names)
    n_goal_calls = len([t for t in tool_names if t == "submit_goal"])
    n_expected = sum(max(1, len(REGULATIONS_IN(sd))) for sd in SELECTED) + 1
    check("one submit_goal per Sub-SO (plus the rejected attempt)",
          n_goal_calls == n_expected, f"{n_goal_calls} vs {n_expected}")

    # the repair loop: the leak()ed first submission must appear as a rejection
    goal_results = [json.loads(m["content"]) for m in conv
                    if m.get("role") == "tool" and m.get("tool_name") == "submit_goal"]
    rejects = [g for g in goal_results if not g.get("ok")]
    check("defective submission was rejected by the content gate", len(rejects) >= 1,
          json.dumps(rejects[:1])[:200])
    check("rejection names the technology gate",
          any("technolog" in json.dumps(r).lower() or "L4" in json.dumps(r)
              for r in rejects))

    print("-- 4. deliverable + validation + export --")
    check("doc02 written in run dir", (run_dir / "doc02_adjusted_goals.md").exists())
    check("RUN_NOTES written", (run_dir / "RUN_NOTES.md").exists())
    exported = EXPORT_DIR / "TinyTask" / run_dir.name / "doc02_adjusted_goals.md"
    check("deliverable exported (AEGIS_EXPORT_DIR)", exported.exists())
    if exported.exists():
        check("run copy == exported copy",
              exported.read_bytes() == (run_dir / "doc02_adjusted_goals.md").read_bytes())

    from validate import validate_run
    findings = validate_run(REPO, run_dir)
    check("L1 PASS on the agent run dir", not findings, str(findings[:4]))

    print("-- 5. agent trace accounting --")
    trace = [json.loads(l) for l in (run_dir / "trace.jsonl").read_text().splitlines()]
    ok = [t for t in trace if t.get("status") == "ok"]
    n_in = len(list((run_dir / "inputs").glob("*_messages.json")))
    n_out = len(list((run_dir / "outputs").glob("*_turn_output.md")))
    check("ok turns == inputs == outputs", len(ok) == n_in == n_out,
          f"{len(ok)}/{n_in}/{n_out}")
    check("manifest total == trace lines", man["n_calls_total"] == len(trace))
    check("trace has done_reason + tokens", all(
        t.get("attempt1_done_reason") == "stop" and t.get("attempt1_eval_tokens")
        for t in ok))

    srv.shutdown()
    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — agent loop end-to-end green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
