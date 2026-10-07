#!/usr/bin/env python3
"""assemble_real_test.py — end-to-end assembly with REAL prose.

local_e2e_test.py proves the machinery (parsers, gates, assembly, export) with
a synthetic fixture; quality_gate_test.py proves the content gates reject bad
answers. Neither reads a human-written answer, so neither can show what the
deliverable actually looks like when the goals are real prose.

This test feeds the pipeline the rows from `example/doc02_adjusted_goals.md` —
hand-written, corpus-grounded restatements — projected to the 9-column P4
contract (Control Anchors is derived by code, so it is dropped from the input
and must reappear in the rendered document), then assembles the deliverable and
inspects it.

Usage: python3 pipeline/tests/assemble_real_test.py
Exit 0 iff the assembly succeeds and the rendered goals are the real ones.
"""

from __future__ import annotations

import json
import os
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

from validate import md_table_defects  # noqa: E402

TMP = Path("/tmp/mvp_assemble_real")
RUN = TMP / "run"
SD = "D-01.1"
COMPANY = "TinyTask"  # the case binding's company_id (export path)

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def p4_rows_from_example() -> list[str]:
    """Project the example's reference rows to the P4 input contract.

    The golden carries two shapes. D-01.1 and D-01.2 — the two blocks
    `compose.build_pack` ever slices into a p4 pack — are in the 9-column EMIT
    shape and are already in the contract, so they are read directly. Every
    other block is still in the DELIVERED shape, which has no Company
    implication and carries the code-derived Control Anchors: those rows get a
    synthesised, fact-sheet-grounded implication (the implication-specificity
    gate rejects duplicates) and drop the anchors column, which assemble_doc
    re-derives from the mapping store."""
    text = (REPO / "example" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
    # the reference format's Property vocabulary differs from the pipeline's
    # closed contract (C | I | A | privacy-right | accountability) — map it
    PROP = {"Confidentiality & Integrity": "C", "Confidentiality": "C",
            "Integrity": "I", "Availability": "A",
            "Privacy-right": "privacy-right", "Accountability": "accountability"}
    out = []
    for line in text.splitlines():
        if not line.startswith(f"| `AG-{SD}-"):
            continue
        c = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(c) < 9:
            continue
        # EMIT row: ID | Adjusted goal | Company implication | Pattern |
        #           Property | Parent goal | Baseline source | Regulatory
        #           source | Adjustment
        emit = c[6].startswith(f"SG-{SD}.")
        if emit:
            reg, impl, pat, prop, parent, source, adj = (
                c[6].split(".")[-1], c[2], c[3].lower(),
                PROP.get(c[4], "C"), c[5], c[7], c[8])
        else:
            # DELIVERED row: AG ID | Adjusted Goal | Pattern | Property |
            #               Parent Goal | Regulation | Articles | Control
            #               Anchors | Adjustment
            reg, impl, pat, prop, parent, source, adj = c[5], "", c[2].lower(), c[3], c[4], c[6], c[8]
        if reg != "GDPR":  # the test's fake verdicts confirm GDPR only
            continue
        if pat not in ("achieve", "cease", "maintain", "avoid", "optimize"):
            pat = "maintain"
        if not impl:
            impl = (f"VetCare Connect runs the appointment app on an external software "
                    f"house's EU cloud, so under {reg} this duty binds through the "
                    f"supplier contract plus the configuration the company controls "
                    f"for {c[1][:60]}…")
        out.append("| " + " | ".join([c[0], c[1], impl, pat, prop,
                                      parent.replace("SG-", "SO-", 1),
                                      f"`SG-{SD}.{reg}`", source, adj]) + " |")
    return out


def write_steps() -> None:
    for d in ("gates", "goals"):
        (RUN / "steps" / d).mkdir(parents=True, exist_ok=True)
    (RUN / "steps" / "fact_sheet.yaml").write_text(
        "company: VetCare Connect\nsector: Veterinary services\nsize_employees: 15\n"
        "jurisdictions: [Portugal (EU)]\nlegal_form: Sociedade por Quotas\n"
        "product_summary: Operates four veterinary clinics in the Porto area; runs an "
        "appointment and reminder app developed and hosted by an external software house.\n"
        "develops_software: false\ndata_categories: [client identity, contacts, address, "
        "payment data, animal clinical history]\ndata_subjects: [pet owners, clinic staff]\n"
        "hosting: supplier-managed (external software house, EU cloud)\n"
        "assumed_regulations: [GDPR]\nopen_questions: []\n", encoding="utf-8")
    (RUN / "steps" / "verdicts.json").write_text(json.dumps({"verdicts": [
        {"regulation": r,
         "verdict": "applies" if r == "GDPR" else "does not apply",
         "rationale": "x"} for r in ("GDPR", "CRA", "NIS2", "DORA", "AI_Act")]}),
        encoding="utf-8")
    (RUN / "steps" / "verdicts.md").write_text(
        "| Regulation | Verdict | Rationale |\n|---|---|---|\n", encoding="utf-8")
    (RUN / "steps" / "framing.md").write_text(
        "| Dimension | Framing |\n|---|---|\n"
        "| Size | 15 employees across four clinics — MICRO; LIGHTWEIGHT/MINIMAL tiers. |\n"
        "| Area of operation | Porto-area veterinary clinics; appointment app run by an "
        "external software house. |\n"
        "| Regulatory roles | GDPR controller; the software house is processor, the payment "
        "provider a recipient. |\n"
        "| Inherited capabilities | Hosting, encryption and key custody are supplier-managed; "
        "no MFA on the admin console. |\n", encoding="utf-8")
    for g in ("G-P1-A", "G-P1-B", "G-P1-C"):
        (RUN / "steps" / "gates" / f"{g}.approved").write_text("approved", encoding="utf-8")
    (RUN / "steps" / "selection.json").write_text(json.dumps({"selected": [
        {"id": SD, "name": "Data at Rest Encryption",
         "rationale": "client personal data in the hosted platform → GDPR Art. 32"}],
        "excluded": []}), encoding="utf-8")


def main() -> int:
    print("== assemble a deliverable from REAL prose (the example's own goals) ==")
    rows = p4_rows_from_example()
    if not rows:
        print("  [FAIL] no example rows found for the sub-domain")
        return 1
    check("example rows found", len(rows) >= 1, f"{len(rows)} row(s)")

    answer = ("```markdown\n### D-01.1 — Data at Rest Encryption\n\n"
              "| ID | Adjusted goal | Company implication | Pattern | Property | "
              "Parent goal | Baseline source | Regulatory source | Adjustment |\n"
              "|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) +
              "\n\n## §5\n\n- None.\n```")

    shutil.rmtree(TMP, ignore_errors=True)
    (TMP / "export").mkdir(parents=True)
    os.environ["AEGIS_EXPORT_DIR"] = str(TMP / "export")
    subprocess.run([sys.executable, str(SRC / "run_pipeline.py"), "new-run",
                    "--case", "Case_01_TinyTask_SaaS", "--run-dir", str(RUN),
                    "--model", "qwen3.8:27b"], capture_output=True, check=True)
    write_steps()

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _j(self, payload, code=200):
            b = json.dumps(payload).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            self._j({"models": [{"name": "qwen3.8:27b"}]})

        def do_POST(self):
            n = int(self.headers.get("Content-Length", 0))
            self.rfile.read(n)
            self._j({"model": "qwen3.8:27b",
                     "message": {"role": "assistant", "content": answer},
                     "eval_count": 100, "total_duration": 1_000_000})

    srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    sys.path.insert(0, str(SRC))
    import steps as S
    runner = S.StepRunner(REPO, RUN, "qwen3.8:27b",
                          f"http://127.0.0.1:{srv.server_address[1]}")
    try:
        runner._call(f"p4:{SD}", SD)
        check("real goals pass the content gates", True)
    except Exception as e:  # noqa: BLE001
        check("real goals pass the content gates", False, str(e)[:220])
        srv.shutdown()
        return 1
    runner.stage_p4t()
    try:
        runner.stage_p5()
        check("assembly + L1 validation + export", True)
    except Exception as e:  # noqa: BLE001
        check("assembly + L1 validation + export", False, str(e)[:220])
        srv.shutdown()
        return 1
    srv.shutdown()

    doc = (TMP / "export" / COMPANY / RUN.name / "doc02_adjusted_goals.md")
    check("deliverable exported", doc.exists(), str(doc))
    text = doc.read_text(encoding="utf-8")

    # the rendered goal prose must be the REAL example prose, verbatim
    ex = (REPO / "example" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
    first_goal = next(c.strip() for line in ex.splitlines()
                      if line.startswith(f"| `AG-{SD}-001")
                      for c in [line.strip().strip("|").split("|")[1].strip()])
    check("rendered goal is the real example prose", first_goal[:80] in text,
          f"expected {first_goal[:60]!r}…")
    check("Control Anchors re-derived into the document",
          re.search(rf"`AG-{SD}-001`.*\| PR\.DS-01", text) is not None)
    check("per-regulation baseline present",
          f"Regulation baseline — `SG-{SD}.GDPR` (GDPR):" in text)
    check("§6 controls table present", "NIST CSF 2.0 controls" in text)
    check("Track B row for the sub-domain", f"| {SD} | MICRO |" in text)
    check("no fixture artefacts in the prose",
          "Company-proportional restatement" not in text)

    # Every table must actually RENDER. A header wider than its separator row
    # is invisible to the cell-by-cell content checks (which drop separator
    # rows) yet leaves the table as literal pipe text in the reader — the §3
    # goal tables shipped exactly that way (10-cell header, 9-cell separator).
    defects = md_table_defects(text)
    check("every table in the deliverable renders", not defects,
          f"{len(defects)} defect(s): {defects[:3]}")
    # guard the guard: the detector must still flag the defect it was written for
    broken = "| a | b | c |\n|---|---|\n| 1 | 2 | 3 |\n"
    check("table detector flags a header/separator mismatch",
          len(md_table_defects(broken)) == 1, f"{md_table_defects(broken)}")

    print()
    if FAILURES:
        print(f"RESULT: FAIL — {len(FAILURES)}: {FAILURES}")
        return 1
    print("RESULT: PASS — the deliverable assembles from real prose and keeps it")
    print(f"  deliverable: {doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
