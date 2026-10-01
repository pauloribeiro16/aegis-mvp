#!/usr/bin/env python3
"""local_e2e_test.py — exhaustive local test of the Phase 1 pipeline.

Runs the FULL pipeline (p1→p5) against a Fake Ollama HTTP server (no model
needed — the workstation cannot run one). Covers:
  1. llm.py HTTP path (tags / warm-up / chat) against a real socket
  2. L0 validator + one repair-retry path (first p2 answer malformed)
  3. gate enforcement (stage refuses without approved gate file)
  4. state-on-disk re-entry across processes (CLI subprocess per stage)
  5. trace.jsonl seq continuation across stages + manifest counters
  6. validate.py L1 green on the finished run + red on a corrupted copy
  7. stage abort forensics (persistent garbage → exit 1, artifacts kept)

Usage: python3 pipeline/tests/local_e2e_test.py
Exit 0 iff every check passes.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "pipeline" / "src"
sys.path.insert(0, str(SRC))

from compose import candidate_subdomains, load_case  # noqa: E402

MODEL = "qwen3.8:27b"
TMP = Path("/tmp/mvp_e2e_test")
CONFIRMED = ["GDPR", "CRA"]
SELECTED = ["D-01.1", "D-03.1", "D-06.3", "D-09.1"]

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# canned answers
# ---------------------------------------------------------------------------

FACT_SHEET = """company: TinyTask Lda.
sector: Technology / Software (B2B SaaS productivity tools)
size_employees: 8
jurisdictions: [Portugal (EU)]
legal_form: Private Limited Company (Lda.)
product_summary: B2B SaaS rule-based task management platform developed and placed on the EU market by the company.
develops_software: true
data_categories: [customer account metadata, clinic task data]
data_subjects: [clinic customers, clinic staff]
sensitive_data: []
data_scale: not stated in intake
hosting: hosted SaaS operated by TinyTask
access_model: individual customer accounts
third_party_processing: [external payment provider]
assumed_regulations: [GDPR — controller+processor, CRA — manufacturer, NIS2 — excluded, DORA — excluded, AI_Act — excluded]
open_questions: [data_scale]
"""

VERDICT_TABLE = """| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | **applies** | processes EU personal data as controller and processor |
| CRA | **applies** | manufacturer placing products with digital elements on the EU market |
| NIS2 | does not apply | below size thresholds, non-Annex I/II sector |
| DORA | does not apply | not a financial entity |
| AI_Act | does not apply | rule-based platform, no AI systems |"""


def selection_answer() -> str:
    cands = [c["id"] for c in candidate_subdomains(REPO, CONFIRMED)]
    rows = ""
    names = {c["id"]: c["name"] for c in candidate_subdomains(REPO, CONFIRMED)}
    for sd in SELECTED:
        rows += f"| {sd} | {names[sd]} | company PII/tasks on managed SaaS → {'GDPR' if sd != 'D-09.1' else 'GDPR+CRA'} duty |\n"
    excl = "\n".join(f"{c} — no company fact triggers it" for c in cands if c not in SELECTED)
    return ("```markdown\n| Sub-domain | Name | Trigger rationale |\n|---|---|---|\n"
            + rows + "\nExcluded candidates:\n" + excl + "\n```")


def goals_answer(sd: str, user_prompt: str) -> str:
    """Build a contract-valid P4 answer using article numbers actually present
    in the attached regs modules AND resolvable against the corpus (R2a)."""
    sys.path.insert(0, str(REPO / "pipeline" / "src"))
    from validate import resolve_reg_source
    arts: dict[str, str] = {}
    for reg in CONFIRMED:
        m = re.search(rf"----- BEGIN FILE: (.*/regs/{reg}\.md) -{{2,}}\n(.*?)----- END FILE", user_prompt, re.S)
        if not m:
            continue
        body = m.group(2)
        for num in re.findall(r"Art(?:icle)?\.?\s*(\d+)", body):
            cand = f"{reg} Art. {num}"
            if resolve_reg_source(REPO, sd, cand)[0]:
                arts[reg] = cand
                break
    rows = ""
    for i in range(1, 3):
        reg = CONFIRMED[i % 2]
        src = arts.get(reg, arts.get(CONFIRMED[0], "GDPR Art. 5"))
        rows += (f"| AG-{sd}-{i:03d} | Company-proportional restatement of the {reg} baseline goal "
                 f"for {sd} at micro scale. | maintain | {'C' if i == 1 else 'I'} | SO-{sd}.HL | "
                 f"{src} | {'PR.DS-01' if i == 1 else '—'} | Scope narrowed to the "
                 f"hosted SaaS context per fact sheet. |\n")
    m41 = "".join(
        f"| AG-{sd}-{i:03d} | {CONFIRMED[i % 2]} | PR.DS-01 | PR.DS-P1 | — | `SR-{CONFIRMED[i % 2]}-001` |\n"
        for i in range(1, 3))
    return ("```markdown\n### " + sd + " — Test Sub-domain\n\n"
            "| ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment |\n"
            "|---|---|---|---|---|---|---|---|\n" + rows +
            "\n## §4.1 Control Anchor Mapping\n\n"
            "| ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source |\n|---|---|---|---|---|---|\n"
            + m41 + "\n## §5\n\n- None.\n```")


P5_INTRO = """```markdown
## §1 Company Profile Echo

TinyTask Lda., 8 employees (micro-enterprise), Portugal (EU), B2B SaaS
productivity tools. Develops and operates a rule-based task management
platform as manufacturer; processes EU personal data as controller (customer
accounts) and processor (customer task data) on hosted SaaS.

## §4 Framing

> 8-person micro-enterprise, non-critical B2B SaaS. Roles: GDPR controller +
> processor, CRA manufacturer (default class, self-assessment). Exclusions:
> NIS2, DORA, AI_Act.

## §6 Handoff Notes to Phase 2

Applicable regulations: GDPR, CRA. Sub-domain scope: """ + ", ".join(SELECTED) + """. Open
questions: data_scale not stated in intake.
```"""


# ---------------------------------------------------------------------------
# fake ollama server
# ---------------------------------------------------------------------------

class FakeOllama(ThreadingHTTPServer):
    def __init__(self):
        super().__init__(("127.0.0.1", 0), Handler)
        self.requests: list[tuple[str, str]] = []  # (step_tag, prompt head)
        self.garbage_mode = False
        self.p2_seen = 0


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
            user = payload["messages"][-1]["content"]  # warm-up sends a single message
            step = re.search(r"Task — (PROM-P1-0\d)", user)
            tag = step.group(1) if step else "?"
            sd = re.search(r"PROM-P1-04 — (D-\d{2}\.\d)", user)
            content: str
            if self.server.garbage_mode:
                content = "I am sorry, I cannot comply."
            elif tag == "PROM-P1-01":
                content = f"Here is the fact sheet:\n```yaml\n{FACT_SHEET}\n```"
            elif tag == "PROM-P1-02":
                self.server.p2_seen += 1
                if self.server.p2_seen == 1:  # retry-path: first attempt malformed
                    content = "verdicts: GDPR applies, CRA applies, others no"
                else:
                    content = f"```markdown\n{VERDICT_TABLE}\n```"
            elif tag == "PROM-P1-03":
                content = selection_answer()
            elif tag == "PROM-P1-04" and sd:
                content = goals_answer(sd.group(1), user)
            elif tag == "PROM-P1-05":
                content = P5_INTRO
            else:
                content = "unknown step"
            self._json({"model": MODEL, "message": {"role": "assistant", "content": content},
                        "eval_count": 128, "total_duration": 1_000_000_000})
        else:
            self._json({}, 404)


# ---------------------------------------------------------------------------
# test flow
# ---------------------------------------------------------------------------

def run_cli(*args: str, expect_rc: int = 0) -> subprocess.CompletedProcess:
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "run_pipeline.py"), *args],
                          capture_output=True, text=True)
    if proc.returncode != expect_rc:
        print(proc.stdout[-2000:], proc.stderr[-2000:])
        check(f"cli {' '.join(args[:3])} rc={expect_rc}", False, f"got rc={proc.returncode}")
    return proc


def main() -> int:
    print("== local E2E: fake-ollama pipeline test ==")
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True)
    srv = FakeOllama()
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    run_dir = TMP / "run_case01_TEST_000001"

    print("-- 1. new-run + stage refusal without gate --")
    run_cli("new-run", "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(run_dir), "--model", MODEL)
    run_dir.mkdir(exist_ok=True)  # new-run may not pre-create until manifest written
    proc = run_cli("run", "--stage", "p2", "--run-dir", str(run_dir), "--base", base, expect_rc=1)
    check("p2 refuses without G-P1-A", "G-P1-A not approved" in proc.stderr + proc.stdout)
    proc = run_cli("run", "--stage", "p1", "--run-dir", str(run_dir), "--base", base)
    check("p1 completes (1 call)", "stage p1 done: 1 call" in proc.stdout)

    print("-- 2. gate file required between stages (state on disk) --")
    (run_dir / "steps" / "gates").mkdir(parents=True, exist_ok=True)
    (run_dir / "steps" / "gates" / "G-P1-A.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p2", "--run-dir", str(run_dir), "--base", base)
    check("p2 completes with repair retry", "stage p2 done: 1 call" in proc.stdout)
    trace = [json.loads(l) for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()]
    p2 = [t for t in trace if t["step"] == "p2"][-1]
    check("retry recorded (l0_retried)", p2.get("l0_retried") is True and p2.get("l0_first_error"))
    check("inputs contain BOTH p2 attempts", len(list((run_dir / "inputs").glob("002_p2_*"))) == 2,
          "system+user x2 attempts share files; outputs must have attempt2")
    check("attempt2 output kept", (run_dir / "outputs" / "002_p2_output_attempt2.md").exists())

    print("-- 3. p3 + gates --")
    (run_dir / "steps" / "gates" / "G-P1-B.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p3", "--run-dir", str(run_dir), "--base", base)
    sel = json.loads((run_dir / "steps" / "selection.json").read_text())
    check("p3 selection == 4 sub-domains", sorted(s["id"] for s in sel["selected"]) == sorted(SELECTED),
          f"{[s['id'] for s in sel['selected']]}")

    print("-- 4. p4+p5 combined stage --")
    (run_dir / "steps" / "gates" / "G-P1-C.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p4p5", "--run-dir", str(run_dir), "--base", base)
    check("p5 deliverable written", (run_dir / "phase1_output.md").exists())
    check("RUN_NOTES written", (run_dir / "RUN_NOTES.md").exists())
    goals = sorted(p.name for p in (run_dir / "steps" / "goals").glob("D-*.md"))
    check("4 goal artifacts", len(goals) == 4, str(goals))

    print("-- 5. trace/manifest consistency --")
    manifest = json.loads((run_dir / "manifest.json").read_text())
    n_trace = len([l for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()])
    n_in = len(list((run_dir / "inputs").glob("*_user.md")))
    check("trace==inputs==manifest", n_trace == n_in == manifest["n_calls_total"] == 8,
          f"trace={n_trace} inputs={n_in} manifest={manifest['n_calls_total']}")
    seqs = [json.loads(l)["seq"] for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()]
    check("seq strictly increasing across processes", seqs == sorted(seqs) and len(set(seqs)) == len(seqs))

    print("-- 6. validate.py green --")
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "validate.py"),
                           "--run-dir", str(run_dir)], capture_output=True, text=True)
    check("validate.py PASS", proc.returncode == 0 and "RESULT: PASS" in proc.stdout,
          proc.stdout.splitlines()[-1] if proc.stdout else "")

    print("-- 7. validate.py red on corrupted copy --")
    corrupt = TMP / "run_corrupt"
    shutil.copytree(run_dir, corrupt)
    gjson = next((corrupt / "steps" / "goals").glob("*.json"))
    data = json.loads(gjson.read_text())
    data["goals"][0]["anchor"] = "PR.FAKE-99"
    gjson.write_text(json.dumps(data))
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "validate.py"),
                           "--run-dir", str(corrupt)], capture_output=True, text=True)
    check("validate.py FAIL on fake anchor", proc.returncode == 1 and "PR.FAKE-99" in proc.stdout)

    print("-- 8. stage abort forensics on persistent garbage --")
    srv.garbage_mode = True
    bad_dir = TMP / "run_garbage"
    run_cli("new-run", "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(bad_dir), "--model", MODEL)
    proc = run_cli("run", "--stage", "p1", "--run-dir", str(bad_dir), "--base", base, expect_rc=1)
    check("p1 aborts on garbage", "STAGE ABORTED" in proc.stderr)
    check("forensics kept", (bad_dir / "outputs" / "001_p1_output.md").exists()
          and (bad_dir / "outputs" / "001_p1_output_attempt2.md").exists())
    btrace = [json.loads(l) for l in (bad_dir / "trace.jsonl").read_text().splitlines() if l.strip()]
    check("failed call recorded", btrace[-1]["status"] == "failed" and "l0_first_error" in btrace[-1])

    srv.shutdown()
    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — local E2E green (no real model calls)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
