#!/usr/bin/env python3
"""quality_gate_test.py — red-team the Phase 1 content gates.

The previous E2E proved assembly integrity only: a red-team injected meta-goals,
verbatim Sub-SO copies, technology leakage, fabricated company facts, phantom
regulations and silent Sub-SO drops, and every one of them passed with
"RESULT: PASS — all L1 checks green". This test injects the same defect classes
and requires the pipeline to REJECT each one, naming the gate that caught it.

Usage: python3 pipeline/tests/quality_gate_test.py
Exit 0 iff every defect class is caught and every good answer is accepted.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "pipeline" / "src"
TMP = Path("/tmp/mvp_quality_test")
RUN = TMP / "run"
STATE: dict[str, str] = {}  # the fake server's canned answer
PORT = [0]  # filled in once the fake server binds

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SRC / "run_pipeline.py"), *args],
                          capture_output=True, text=True)


def p4_call(answer_text: str) -> str:
    """Drive one P4 sub-domain call in-process; returns the error text ('' if
    the answer was accepted and stored)."""
    sys.path.insert(0, str(SRC))
    import importlib
    steps = importlib.import_module("steps")
    STATE["answer"] = answer_text
    (RUN / "steps" / "goals" / "D-01.1.md").unlink(missing_ok=True)
    (RUN / "steps" / "goals" / "D-01_1.json").unlink(missing_ok=True)
    runner = steps.StepRunner(REPO, RUN, "qwen3.8:27b", f"http://127.0.0.1:{PORT[0]}")
    try:
        runner._call("p4:D-01.1", "D-01.1")
        return ""
    except Exception as e:  # noqa: BLE001 — the failure text IS the assertion
        return f"{type(e).__name__}: {e}"


def write_steps() -> None:
    """A minimal completed run: p1/p2/p3/p3f artifacts + gates, no P4 yet."""
    (RUN / "steps" / "gates").mkdir(parents=True, exist_ok=True)
    (RUN / "steps" / "goals").mkdir(parents=True, exist_ok=True)
    (RUN / "steps" / "fact_sheet.yaml").write_text(
        "company: TinyTask Lda.\nsize_employees: 8\nhosting: hosted SaaS\n"
        "data_categories: [customer account metadata]\n"
        "data_subjects: [clinic customers]\n", encoding="utf-8")
    (RUN / "steps" / "verdicts.json").write_text(json.dumps({"verdicts": [
        {"regulation": "GDPR", "verdict": "applies", "rationale": "x"},
        {"regulation": "CRA", "verdict": "applies", "rationale": "x"},
        {"regulation": "NIS2", "verdict": "does not apply", "rationale": "x"},
        {"regulation": "DORA", "verdict": "does not apply", "rationale": "x"},
        {"regulation": "AI_Act", "verdict": "does not apply", "rationale": "x"},
    ]}), encoding="utf-8")
    (RUN / "steps" / "verdicts.md").write_text("| Regulation | Verdict | Rationale |\n|---|---|---|\n",
                                              encoding="utf-8")
    (RUN / "steps" / "framing.md").write_text(
        "| Dimension | Framing |\n|---|---|\n"
        "| Size | 8-person micro-enterprise; LIGHTWEIGHT tier. |\n"
        "| Area of operation | B2B SaaS task platform for clinics, Portugal. |\n"
        "| Regulatory roles | GDPR controller and processor; CRA manufacturer. |\n"
        "| Inherited capabilities | Hosted SaaS operated by the company. |\n",
        encoding="utf-8")
    for gate in ("G-P1-A", "G-P1-B", "G-P1-C"):
        (RUN / "steps" / "gates" / f"{gate}.approved").write_text("approved: test",
                                                                  encoding="utf-8")


GOOD_ROWS = (
    "| AG-D-01.1-001 | Client personal data held at rest in the appointment platform "
    "database and its backups is processed so as to ensure appropriate security, "
    "protecting it against unauthorised or unlawful processing and against accidental "
    "loss, destruction or damage, with the ability to ensure the ongoing confidentiality, "
    "integrity, availability and resilience of the processing systems (GDPR Art. 5(1)(f) + Art. 32(1)(b)). | The platform "
    "database runs in the company's own hosted SaaS, so TinyTask must be able to show "
    "which protection applies there and to keep that statement current as the hosting "
    "arrangement changes. | maintain | C | SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | "
    "narrowed: scope to the platform database and its backups — because those are the "
    "stores the company operates. |\n"
    "| AG-D-01.1-002 | Where the product stores data at rest, the confidentiality of "
    "that data is protected by encrypting the relevant data at rest using "
    "state-of-the-art mechanisms, including the data the company holds for clinic "
    "customers. | TinyTask ships this protection inside the product itself, so the duty "
    "sits with the release process rather than with a separate infrastructure project. | "
    "maintain | C | SO-D-01.1.HL | SG-D-01.1.CRA | CRA Annex I Part I (2)(e) | "
    "unchanged — fits as stated |\n")


def answer(rows: str) -> str:
    return ("```markdown\n### D-01.1 — Data at Rest Encryption\n\n"
            "| ID | Adjusted goal | Company implication | Pattern | Property | Parent goal "
            "| Baseline source | Regulatory source | Adjustment |\n"
            "|---|---|---|---|---|---|---|---|---|\n" + rows +
            "\n## §5\n\n- None.\n```")


CASES = [
    # (name, answer, substring that must appear in the rejection)
    ("meta-goal that restates nothing", answer(
        "| AG-D-01.1-001 | The GDPR baseline goal for D-01.1 restated for the company "
        "in business terms. | Applies to the company. | maintain | C | SO-D-01.1.HL | "
        "SG-D-01.1.GDPR | GDPR Art. 32 | unchanged — fits as stated |\n"
        + GOOD_ROWS.split("\n", 1)[1]),
     "obligation terms"),
    ("verbatim copy of the Sub-SO objective", answer(
        "| AG-D-01.1-001 | Personal data at rest is processed in a manner that ensures "
        "appropriate security — including protection against unauthorised or unlawful "
        "processing and against accidental loss, destruction or damage — using appropriate "
        "technical or organisational measures, with the ability to ensure the ongoing "
        "confidentiality, integrity, availability and resilience of processing systems and "
        "services (Art. 5(1)(f) + Art. 32(1)(b); the appropriate threshold is anchored by "
        "the five Art. 32(1) preamble factors — state of the art, costs of implementation, "
        "nature, scope, context, purposes, risks). | Applies to the company. | maintain | C "
        "| SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | unchanged — fits as stated |\n"
        + GOOD_ROWS.split("\n", 1)[1]),
     "near-verbatim copy"),
    ("technology leakage", answer(
        "| AG-D-01.1-001 | Client personal data at rest in the appointment platform "
        "database and its backups is processed with appropriate security against "
        "unauthorised or unlawful processing and accidental loss, destruction or damage, "
        "maintaining the ongoing confidentiality, integrity, availability and resilience "
        "of the processing systems through encryption at rest and key custody. | TinyTask "
        "runs this on hosted SaaS with encryption at rest held in AWS S3 and keys managed "
        "in HashiCorp Vault, so the evidence must come from the hosting configuration. | "
        "maintain | C | SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | "
        "narrowed: scope — because hosted SaaS. |\n"
        + GOOD_ROWS.split("\n", 1)[1]),
     "technology leakage"),
    ("fabricated company facts", answer(
        "| AG-D-01.1-001 | Client personal data at rest in the appointment platform "
        "database and its backups is processed with appropriate security against "
        "unauthorised or unlawful processing and accidental loss, destruction or damage, "
        "maintaining the ongoing confidentiality, integrity, availability and resilience "
        "of the processing systems. | The 1200 employees in the Frankfurt office review "
        "the encryption posture quarterly against the ISO 27001 certification. | maintain "
        "| C | SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | narrowed: scope — because "
        "hosted SaaS. |\n"
        + GOOD_ROWS.split("\n", 1)[1]),
     "not traceable"),
    ("phantom regulation (NIS2 not confirmed)", answer(
        GOOD_ROWS + "| AG-D-01.1-003 | Notification duties for significant incidents are "
        "met through a single channel that serves the supervisory authority within the "
        "statutory window for personal data breaches. | TinyTask has no NIS2 obligation, "
        "so this row is invented. | achieve | A | SO-D-01.1.HL | SG-D-01.1.NIS2 | "
        "NIS2 Art. 23 | flagged: question. |\n"),
     "no Sub-SO in this module for a confirmed regulation"),
    ("silent Sub-SO drop (CRA row missing)", answer(
        "| AG-D-01.1-001 | Client personal data held at rest in the appointment platform "
        "database and its backups is processed so as to ensure appropriate security, "
        "protecting it against unauthorised or unlawful processing and against accidental "
        "loss, destruction or damage, with the ability to ensure the ongoing confidentiality, "
        "integrity, availability and resilience of the processing systems (GDPR Art. 5(1)(f) + Art. 32(1)(b)). | The platform "
        "database runs in the company's own hosted SaaS, so TinyTask must show which "
        "protection applies and keep it current. | maintain | C | SO-D-01.1.HL | "
        "SG-D-01.1.GDPR | GDPR Art. 32 | narrowed: scope — because those are the stores "
        "the company operates. |\n"),
     "not restated"),
    ("duplicate Sub-SO row", answer(
        "| AG-D-01.1-001 | Client personal data held at rest in the appointment platform "
        "database and its backups is processed so as to ensure appropriate security against "
        "unauthorised processing and accidental loss, maintaining the ongoing "
        "confidentiality, integrity, availability and resilience of the processing systems "
        "(GDPR Art. 5(1)(f) + Art. 32(1)(b)). | The platform database runs in the company's "
        "hosted SaaS, so the protection statement must be kept current there. | maintain | C "
        "| SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | unchanged — fits as stated |\n"
        "| AG-D-01.1-002 | Client personal data held at rest is processed with appropriate "
        "security against unauthorised processing, maintaining confidentiality, integrity, "
        "availability and resilience of the processing systems (GDPR Art. 5(1)(f) + "
        "Art. 32(1)(b)). | A second GDPR row restating the same Sub-SO a different way. | "
        "maintain | C | SO-D-01.1.HL | SG-D-01.1.GDPR | GDPR Art. 32 | "
        "unchanged — fits as stated |\n"
        "| AG-D-01.1-003 | Where the product stores data at rest, the confidentiality of "
        "that data is protected by encrypting it using state-of-the-art mechanisms (CRA "
        "Annex I Part I (2)(e)). | The release process carries this duty for the product. | "
        "maintain | C | SO-D-01.1.HL | SG-D-01.1.CRA | CRA Annex I Part I (2)(e) | "
        "unchanged — fits as stated |\n"),
     "2 times"),
    ("adjustment record too brief or invalid", answer(
        GOOD_ROWS.split("\n", 1)[0].replace("narrowed: scope to the platform database and "
                                           "its backups — because those are the stores the "
                                           "company operates.",
                                           "relaxed.")
        + "\n" + GOOD_ROWS.split("\n", 1)[1]),
     "too brief or invalid"),
    ("literal pipe inside a cell", answer(
        GOOD_ROWS.replace("The platform database runs in the company's own hosted SaaS, so "
                         "TinyTask must be able to show which protection applies there and to "
                         "keep that statement current as the hosting arrangement changes.",
                         "Protection is delivered by policy | process | people.")),
     "11 columns"),
]


def test_candidate_filter_requires_a_sub_so() -> None:
    """The P3 pre-filter must exclude a sub-domain the baseline cannot ground.

    D-08.3 has a `regs/GDPR.md` module file but declares no `SG-D-08.3.GDPR`.
    File-presence filtering offered it as a GDPR candidate to TinyTask (whose
    only confirmed regulations are GDPR and CRA), the p4 model correctly
    answered "None — no Sub-SO for the confirmed regulations", and G0 refused
    the run twice (run_p2c1). The filter now requires a Sub-SO card.
    """
    sys.path.insert(0, str(SRC))
    from compose import carries_reg_card, candidate_subdomains  # noqa: PLC0415

    cands = {c["id"] for c in candidate_subdomains(REPO, ["GDPR", "CRA"])}
    check("D-08.3 is not offered as a GDPR/CRA candidate (no Sub-SO card)",
          "D-08.3" not in cands,
          "module file exists but declares no SG-D-08.3.GDPR")
    check("D-08.3 does carry a DORA Sub-SO, so it is reachable there",
          carries_reg_card(REPO, "D-08.3", "DORA"))
    check("every offered candidate carries a card for a confirmed regulation",
          all(any(carries_reg_card(REPO, c, r) for r in ("GDPR", "CRA"))
              for c in cands if c in ("D-01.1", "D-03.1", "D-08.1")))
    check("the GDPR+CRA filter keeps the other 37 sub-domains",
          len(cands) == 37, f"{len(cands)} candidates")


def main() -> int:
    print("== red-team: do the content gates reject what passed before? ==")
    test_candidate_filter_requires_a_sub_so()
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True)
    cli("new-run", "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(RUN),
        "--model", "qwen3.8:27b")
    write_steps()
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    STATE["answer"] = ""

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _json(self, payload, code=200):
            import json as _j
            b = _j.dumps(payload).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            self._json({"models": [{"name": "qwen3.8:27b"}]})

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            self._json({"model": "qwen3.8:27b",
                        "message": {"role": "assistant", "content": STATE["answer"]},
                        "eval_count": 100, "total_duration": 1_000_000})

        def handle_one_request(self):
            try:
                BaseHTTPRequestHandler.handle_one_request(self)
            except Exception:
                pass

    srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
    PORT[0] = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    print("-- a good answer must be ACCEPTED --")
    err = p4_call(answer(GOOD_ROWS))
    check("good P4 answer accepted", err == "", err[:160])

    print("-- each defect class must be REJECTED --")
    for name, ans, expect in CASES:
        err = p4_call(ans)
        check(f"rejects: {name}", err != "" and expect in err,
              "" if (err and expect in err) else f"got: {err[:200]!r}")

    srv.shutdown()
    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — every injected defect class is rejected by a named gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
