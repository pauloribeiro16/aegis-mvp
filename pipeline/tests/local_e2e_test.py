#!/usr/bin/env python3
"""local_e2e_test.py — exhaustive local test of the Phase 1 pipeline.

Runs the FULL pipeline (p1→p2→p3f→p3→p4→p4t→p5) against a Fake Ollama HTTP
server (no model needed — the workstation cannot run one). Covers:
  1. llm.py HTTP path (tags / warm-up / chat) against a real socket
  2. L0 validator + one repair-retry path (first p2 answer malformed)
  3. gate enforcement (stage refuses without approved gate file)
  4. state-on-disk re-entry across processes (CLI subprocess per stage)
  5. trace.jsonl seq continuation across stages + manifest counters
  6. p5 zero-LLM assembly of the Doc02 deliverable + automatic validate.py
  7. validate.py L1 green on the finished run + red on a corrupted copy
  8. stage abort forensics (persistent garbage → exit 1, artifacts kept)

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

from compose import candidate_subdomains  # noqa: E402

MODEL = "qwen3.8:27b"
TMP = Path("/tmp/mvp_e2e_test")
CONFIRMED = ["GDPR", "CRA"]
# representative subset with genuinely distinct baselines — the full 37-candidate
# sweep is covered by the red-team quality_gate_test; this E2E exercises assembly.
EXCLUDED = [c["id"] for c in candidate_subdomains(REPO, CONFIRMED)
           if c["id"] not in ("D-01.1", "D-03.1", "D-06.3", "D-09.1", "D-02.2")]
SELECTED = ["D-01.1", "D-02.2", "D-03.1", "D-06.3", "D-09.1"]

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
    names = {c["id"]: c["name"] for c in candidate_subdomains(REPO, CONFIRMED)}
    rows = ""
    for sd in SELECTED:
        rows += f"| {sd} | {names[sd]} | company PII/tasks on managed SaaS → GDPR duty |\n"
    excl = "\n".join(f"{c} — no conformity-assessment or market-surveillance exposure declared; self-assessment only" for c in EXCLUDED)
    return ("```markdown\n| Sub-domain | Name | Trigger rationale |\n|---|---|---|\n"
            + rows + "\nExcluded candidates:\n" + excl + "\n```")


FRAMING_TABLE = """```markdown
| Dimension | Framing |
|---|---|
| Size | 8-person micro-enterprise; LIGHTWEIGHT/MINIMAL tier consequences across the board. |
| Area of operation | B2B SaaS task-management platform for clinic customers, EU-domiciled (Portugal). |
| Regulatory roles | GDPR controller (customer accounts) and processor (customer task data); CRA manufacturer (default class, self-assessment). |
| Inherited capabilities | Hosted SaaS operated by the company; no third-party managed security layer declared. |
```"""


def goals_answer(sd: str, user_prompt: str) -> str:
    """Build a contract-valid 9-column P4 answer: one row per (Sub-SO, confirmed
    regulation) pair whose card exists in the attached module. The adjusted goal
    keeps the Sub-SO's obligation terms (the content gates check retention and
    adaptation), and the company implication is specific to the duty."""
    sys.path.insert(0, str(SRC))
    from validate import resolve_reg_source
    from compose import sub_so_objective
    repo = Path(".")
    arts: dict[str, str] = {}
    has_card: dict[str, bool] = {}
    for reg in CONFIRMED:
        m = re.search(rf"----- BEGIN FILE: ([^\n]*/regs/{reg}\.md) -{{2,}}\n(.*?)----- END FILE",
                      user_prompt, re.S)
        if not m:
            continue
        body = m.group(2)
        has_card[reg] = bool(re.search(rf"id:\s*SG-{re.escape(sd)}\.{reg}\b", body))
        for num in re.findall(r"Art(?:icle)?\.?\s*(\d+)", body):
            cand = f"{reg} Art. {num}"
            if resolve_reg_source(repo, sd, cand)[0]:
                arts[reg] = cand
                break
    if not any(has_card.values()):
        return ("```markdown\n### " + sd + " — Test Sub-domain\n\n"
                "None — no Sub-SO for the confirmed regulations.\n\n"
                "## §5\n\n- None.\n```")
    rows = ""
    i = 0
    for reg in CONFIRMED:  # canonical regulation order: GDPR slot, CRA slot
        if not has_card.get(reg):
            continue
        i += 1
        src = arts.get(reg, arts.get("GDPR", "GDPR Art. 5"))
        baseline = " ".join(sub_so_objective(repo, sd, reg).split())
        # a genuine restatement: the obligation's content words are carried
        # over, but the duty is rewritten in the company's own terms rather than
        # pasted from the baseline (the reformulation gate rejects an embed)
        keep = [w for w in baseline.split()
                if w.lower() not in
                ("the", "a", "an", "and", "or", "of", "to", "in", "is", "are",
                 "that", "with", "for", "on", "by", "as", "at", "be", "it",
                 "its", "from", "this", "which", "are", "been", "has", "not",
                 "or", "such", "any", "all", "where", "when", "also", "but",
                 "may", "must", "can", "each", "other", "own", "same", "more")]
        core = " ".join(keep[1:])
        goal = (f"For TinyTask as {reg} controller and manufacturer, the {sd} duty is that "
                f"{core} — held to the {reg} standard in the product TinyTask ships and the "
                f"platform it hosts, at the LIGHTWEIGHT tier the framing fixes for a team of "
                f"eight people with supplier-managed hosting, with the proof kept in the "
                f"contractual position and the runtime record rather than a separate programme.")
        # the implication is specific to this duty and company: it names the
        # obligation's own content words, the company's operating model, and the
        # tier the framing fixes — never a sentence reusable on another row
        fp = [w for w in baseline.split()
              if w.lower() not in
              ("the", "a", "an", "and", "or", "of", "to", "in", "is", "are",
               "that", "with", "for", "on", "by", "as", "at", "be", "it",
               "its", "from", "this", "which", "been", "has", "not", "such",
               "any", "all", "where", "when", "also", "but", "may", "must",
               "can", "each", "other", "own", "same", "more", "most")]
        subj = " ".join(fp[2:9])
        implication = (f"In practice for TinyTask, meeting this {reg} {sd} duty means keeping "
                       f"{subj} demonstrably under control inside the product and the hosting "
                       f"it uses, with the 8-person team able to show the position on request at "
                       f"the LIGHTWEIGHT tier set by the §2 framing.")
        rows += (f"| AG-{sd}-{i:03d} | {goal} | {implication} | maintain | C | SO-{sd}.HL | "
                 f"SG-{sd}.{reg} | {src} | narrowed: scope to the hosted platform — because "
                 f"that is where the company performs the duty. |\n")
    return ("```markdown\n### " + sd + " — Test Sub-domain\n\n"
            "| ID | Adjusted goal | Company implication | Pattern | Property | Parent goal | Baseline source | Regulatory source | Adjustment |\n"
            "|---|---|---|---|---|---|---|---|---|\n" + rows +
            "\n## §5\n\n- None.\n```")


TENSIONS_TABLE = """```markdown
| ID | Sub-domains | Tension | Conflict | Resolution |
|---|---|---|---|---|
| T-001 | D-06.3 | Notification-clock divergence | GDPR and CRA notification duties anchor to different recipients and clocks on the same event. | Strictest timeline binds per recipient; parallel recipients keep their own clocks. |
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
        self.p1_seen = 0
        self.truncate_first_p1 = False
        self.last_think: object = "<unset>"   # last `think` flag seen by the server
        self.last_options: dict = {}


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
            # the step tag can sit in ANY message: the multi-turn repair path
            # (assistant answer + feedback user turn) does not carry it in the
            # last message, so scan the whole conversation
            user = payload["messages"][-1]["content"]  # warm-up sends a single message
            convo = "\n".join(m.get("content", "") for m in payload["messages"])
            step = re.search(r"Task — (PROM-P1-0\d)", convo)
            tag = step.group(1) if step else "?"
            sd = re.search(r"PROM-P1-04 — (D-\d{2}\.\d)", convo)
            self.server.last_think = payload.get("think", "<absent>")
            self.server.last_options = payload.get("options", {})
            content: str
            done_reason = "stop"
            eval_count = 128
            if self.server.garbage_mode:
                content = "I am sorry, I cannot comply."
            elif tag == "PROM-P1-01":
                self.server.p1_seen += 1
                content = f"Here is the fact sheet:\n```yaml\n{FACT_SHEET}\n```"
                if self.server.p1_seen == 1 and self.server.truncate_first_p1:
                    # L0-VALID but incomplete: every field parse_p1 requires is
                    # present and the closing fence is intact, so nothing but an
                    # explicit done_reason check can catch this. This is the
                    # job-1963538 seq-26 defect — D-10.1 was stored cut
                    # mid-sentence at the num_predict cap and became the
                    # artifact of record. The dropped line is an OPTIONAL field
                    # (a real company fact: the external payment processor), so
                    # its absence is a silent content loss, not a parse error.
                    short = "\n".join(l for l in FACT_SHEET.splitlines()
                                      if not l.startswith("third_party_processing"))
                    content = f"Here is the fact sheet:\n```yaml\n{short}\n```"
                    done_reason, eval_count = "length", 8192
            elif tag == "PROM-P1-02":
                self.server.p2_seen += 1
                if self.server.p2_seen == 1:  # retry-path: first attempt malformed
                    content = "verdicts: GDPR applies, CRA applies, others no"
                else:
                    content = f"```markdown\n{VERDICT_TABLE}\n```"
            elif tag == "PROM-P1-03":
                content = selection_answer()
            elif tag == "PROM-P1-06":
                content = FRAMING_TABLE
            elif tag == "PROM-P1-04" and sd:
                content = goals_answer(sd.group(1), user)
            elif tag == "PROM-P1-07":
                content = TENSIONS_TABLE
            else:
                content = "unknown step"
            self._json({"model": MODEL, "message": {"role": "assistant", "content": content},
                        "done_reason": done_reason, "eval_count": eval_count,
                        "total_duration": 1_000_000_000})
        else:
            self._json({}, 404)


# ---------------------------------------------------------------------------
# test flow
# ---------------------------------------------------------------------------

EXPORT_DIR = TMP / "export"


def _output_snapshot(d: Path) -> list[tuple[str, int]]:
    """(relative path, mtime_ns) for every file under d — the fingerprint used
    to prove the test never writes into the repo's real output/ tree. Asserting
    non-existence instead would fail the moment a real deliverable lands there,
    which is the normal state of a finished run."""
    if not d.exists():
        return []
    return sorted((str(p.relative_to(d)), p.stat().st_mtime_ns)
                  for p in d.rglob("*") if p.is_file())


def run_cli(*args: str, expect_rc: int = 0) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ, AEGIS_EXPORT_DIR=str(EXPORT_DIR))
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "run_pipeline.py"), *args],
                          capture_output=True, text=True, env=env)
    if proc.returncode != expect_rc:
        print(proc.stdout[-3000:], proc.stderr[-3000:])
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
    repo_output_before = _output_snapshot(REPO / "output")

    print("-- 1. new-run + stage refusal without gate --")
    run_cli("new-run", "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(run_dir), "--model", MODEL)
    run_dir.mkdir(exist_ok=True)  # new-run may not pre-create until manifest written
    proc = run_cli("run", "--stage", "p2", "--run-dir", str(run_dir), "--base", base, expect_rc=1)
    check("p2 refuses without G-P1-A", "G-P1-A not approved" in proc.stderr + proc.stdout)

    # the first p1 answer comes back cut at the num_predict cap
    srv.truncate_first_p1 = True
    proc = run_cli("run", "--stage", "p1", "--run-dir", str(run_dir), "--base", base)
    check("p1 completes (1 call)", "stage p1 done: 1 call" in proc.stdout)
    check("think=false sent (qwen reasoning must not eat num_predict)",
          srv.last_think is False, f"think={srv.last_think!r}")
    check("num_predict explicit in options", bool(srv.last_options.get("num_predict")),
          f"options={srv.last_options}")
    trace1 = [json.loads(l) for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()]
    p1 = [t for t in trace1 if t["step"] == "p1"][-1]
    check("truncated attempt recorded as done_reason=length",
          p1.get("attempt1_done_reason") == "length" and p1.get("attempt1_truncated_chars"),
          f"attempt1_done_reason={p1.get('attempt1_done_reason')!r}")
    check("truncation was a retryable failure, not silent acceptance",
          "truncated at the num_predict" in (p1.get("attempt1_error") or ""))
    check("truncated answer kept for forensics",
          any(q.name.endswith("_output_truncated.md") for q in (run_dir / "outputs").iterdir()))
    # the decisive assertion: the ARTIFACT is the complete second answer. The
    # truncated answer was L0-valid, so only the done_reason rejection keeps the
    # dropped field out of the artifact.
    fact = (run_dir / "steps" / "fact_sheet.yaml").read_text()
    check("fact_sheet.yaml is the COMPLETE retried answer, not the L0-valid truncated one",
          "third_party_processing" in fact, f"fact_sheet.yaml={fact!r}")

    print("-- 2. gate file required between stages (state on disk) --")
    (run_dir / "steps" / "gates").mkdir(parents=True, exist_ok=True)
    (run_dir / "steps" / "gates" / "G-P1-A.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p2", "--run-dir", str(run_dir), "--base", base)
    check("p2 completes with repair retry", "stage p2 done: 1 call" in proc.stdout)
    trace = [json.loads(l) for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()]
    p2 = [t for t in trace if t["step"] == "p2"][-1]
    check("retry recorded (l0_retried)", p2.get("l0_retried") is True and p2.get("l0_first_error"))
    check("attempt2 output kept", (run_dir / "outputs" / "002_p2_output_attempt2.md").exists())

    print("-- 3. p3f (framing table) + p3 + gates --")
    (run_dir / "steps" / "gates" / "G-P1-B.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p3f", "--run-dir", str(run_dir), "--base", base)
    check("framing.md written from p3f", (run_dir / "steps" / "framing.md").exists()
          and "| Size |" in (run_dir / "steps" / "framing.md").read_text())
    proc = run_cli("run", "--stage", "p3", "--run-dir", str(run_dir), "--base", base)
    sel = json.loads((run_dir / "steps" / "selection.json").read_text())
    check("p3 selection == 4 sub-domains", sorted(s["id"] for s in sel["selected"]) == sorted(SELECTED),
          f"{[s['id'] for s in sel['selected']]}")

    print("-- 4. p4 → p4t → p5 combined stage (Doc02 assembly, zero-LLM p5) --")
    (run_dir / "steps" / "gates" / "G-P1-C.approved").write_text("approved: test")
    proc = run_cli("run", "--stage", "p4p5", "--run-dir", str(run_dir), "--base", base)
    check("p5 deliverable written", (run_dir / "doc02_adjusted_goals.md").exists())
    check("RUN_NOTES written", (run_dir / "RUN_NOTES.md").exists())
    goals = sorted(p.name for p in (run_dir / "steps" / "goals").glob("D-*.md"))
    check("goal artifact per selected sub-domain", len(goals) == len(SELECTED),
          f"{len(goals)} vs {len(SELECTED)}")
    check("tensions.json written by p4t", (run_dir / "steps" / "tensions.json").exists())
    doc = (run_dir / "doc02_adjusted_goals.md").read_text()
    check("doc has §0–§6 in order",
          [m.group(1) for m in re.finditer(r"^## (§\d)", doc, re.M)]
          == ["§0", "§1", "§2", "§3", "§4", "§5", "§6"])
    check("doc §6 control rows derived (PR.DS-01 present)", "| PROTECT | PR.DS-01 |" in doc)
    check("doc §5 Track B rows present", "| D-01.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT |" in doc)
    check("doc §3 covers every selected sub-domain",
          len(re.findall(r"(?m)^### D-\d{2}\.\d ", doc)) == len(SELECTED),
          f"{len(re.findall(r'(?m)^### D-\\d{2}\\.\\d ', doc))} vs {len(SELECTED)}")
    check("doc carries per-regulation baseline objectives",
          "Regulation baseline — `SG-D-01.1.GDPR` (GDPR):" in doc
          and "Regulation baseline — `SG-D-01.1.CRA` (CRA):" in doc)
    exported = EXPORT_DIR / "TinyTask" / run_dir.name / "doc02_adjusted_goals.md"
    check("deliverable exported (AEGIS_EXPORT_DIR)", exported.exists())
    check("repo output/ untouched by tests", repo_output_before == _output_snapshot(REPO / "output"),
          f"{len(repo_output_before)} pre-existing file(s) unchanged by the test")

    print("-- 5. trace/manifest consistency --")
    manifest = json.loads((run_dir / "manifest.json").read_text())
    n_trace = len([l for l in (run_dir / "trace.jsonl").read_text().splitlines() if l.strip()])
    n_in = len(list((run_dir / "inputs").glob("*_user.md")))
    # p1,p2,p3,p3f + one p4 and one p4t call per selected sub-domain
    n_expected = 4 + 2 * len(SELECTED)
    check("trace==inputs==manifest", n_trace == n_in == manifest["n_calls_total"] == n_expected,
          f"trace={n_trace} inputs={n_in} manifest={manifest['n_calls_total']} expected={n_expected}")
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
    data["goals"][0]["source"] = "GDPR Art. 999"
    gjson.write_text(json.dumps(data))
    proc = subprocess.run([sys.executable, str(REPO / "pipeline" / "src" / "validate.py"),
                           "--run-dir", str(corrupt)], capture_output=True, text=True)
    check("validate.py FAIL on unresolvable source", proc.returncode == 1 and "GDPR Art. 999" in proc.stdout)

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
