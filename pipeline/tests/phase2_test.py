#!/usr/bin/env python3
"""phase2_test.py — the Phase 2 prototype's derivations may not drift.

`pipeline/src/phase2.py` turns a Phase 1 run directory into the two Phase 2
deliverables without a model. That is only worth anything if the derivations are
anchored to the corpus rather than to whatever the last run happened to contain,
which is what these assertions check.

Three of them exist because hand-authoring got them wrong in cases 01-03 and the
ledger recorded it (docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §4):

  * §4.2 — an `Operational Statement` cell swallowed raw baseline YAML in four
    Case 03 rows. A code path cannot produce that, and the gate must prove it.
  * §4.4 — Case 01 put 16 GDPR rows under the `SO-` prefix. The prefix is a
    function of the regulation, or it is a convention nobody can reproduce.
  * §4.8 — one Case 03 row carried `—` where Phase 1 had anchors, so control
    anchoring was lost silently. Anchors are re-derived here, never inherited.

The fourth is R2b: every anchor the prototype emits must resolve to a real file
under `baseline/CONTROLS/`. A derived-but-unresolvable anchor is worse than a
missing one, because it looks anchored.

These assertions read only committed files and need no model and no GPU.

Usage: python3 pipeline/tests/phase2_test.py
Exit 0 iff every derivation holds.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

import phase2  # noqa: E402

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def synth_run(tmp: Path, goals: list[dict], selected: list[str]) -> Path:
    """A minimal Phase 1 run dir: the prototype's only input contract."""
    gdir = tmp / "steps" / "goals"
    gdir.mkdir(parents=True)
    by_sd: dict[str, list[dict]] = {}
    for g in goals:
        by_sd.setdefault(phase2.subdomain_of(g["id"]), []).append(g)
    for sd, gs in by_sd.items():
        (gdir / f"{sd.replace('.', '_')}.json").write_text(
            json.dumps({"subdomain": sd, "goals": gs}), encoding="utf-8")
    (tmp / "steps" / "selection.json").write_text(
        json.dumps({"selected": [{"id": s, "name": s} for s in selected]}),
        encoding="utf-8")
    (tmp / "manifest.json").write_text(json.dumps({"case_id": "synthetic"}),
                                       encoding="utf-8")
    return tmp


def goal(gid: str, reg: str, sd_source: str = "SG-D-01.1.GDPR") -> dict:
    return {"id": gid, "goal": f"statement for {gid}", "regulation": reg,
            "baseline_source": sd_source, "pattern": "maintain",
            "property": "c", "parent": f"SG-{phase2.subdomain_of(gid)}.HL",
            "source": "some article", "adjustment": "unchanged — fits as stated",
            "implication": "n/a"}


def test_id_derivation() -> None:
    print("\nid derivation")
    rows = [
        phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR")),
        phase2.derive_objective(REPO, goal("AG-D-01.1-002", "CRA")),
        phase2.derive_objective(REPO, goal("AG-D-01.1-003", "NIS2")),
    ]
    check("GDPR takes the PO- prefix", rows[0]["objective_id"] == "PO-D-01.1-001",
          rows[0]["objective_id"])
    check("CRA takes SO-", rows[1]["objective_id"] == "SO-D-01.1-002",
          rows[1]["objective_id"])
    check("NIS2 takes SO-", rows[2]["objective_id"] == "SO-D-01.1-003",
          rows[2]["objective_id"])
    # the regression that produced `POD-01.1-001`
    check("the canonical D- axis survives the prefix swap",
          all(r["objective_id"].count("-") == 3 for r in rows),
          rows[0]["objective_id"])


def test_slot_inherited() -> None:
    print("\nslot inheritance")
    # D-01.1 carries CRA for real; a slot the golden does not use (003) proves
    # the slot is carried rather than recomputed from a canonical regulation
    # order. Using a pair the corpus does not carry would make controls.py
    # refuse the row, which is the correct behaviour and not what is under test.
    g = goal("AG-D-01.1-003", "CRA", sd_source="SG-D-01.1.CRA")
    r = phase2.derive_objective(REPO, g)
    check("the Phase 1 slot is carried verbatim", r["objective_id"] == "SO-D-01.1-003",
          r["objective_id"])
    check("the regulation is read from the goal, never from the slot",
          r["regulation"] == "CRA", r["regulation"])


def test_anchors_resolve() -> None:
    print("\nanchors (R2b)")
    r = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    anchors = [a.strip() for a in r["anchors"].split(",") if a.strip() != "—"]
    check("anchors are derived, not inherited", bool(anchors), r["anchors"])
    unresolved = [a for a in anchors
                  if not list((REPO / "baseline" / "CONTROLS").rglob(f"{a}.json"))]
    check("every derived anchor resolves under baseline/CONTROLS/",
          not unresolved, f"{len(anchors)} anchors, unresolved={unresolved}")


def test_pollution_gate() -> None:
    print("\ngate G1 — baseline pollution (§4.2)")
    good = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    bad = dict(good)
    bad["objective_id"] = "PO-D-01.1-999"
    bad["statement"] = "text ```yaml\n- req_id: 1.1.3\n``` --- ## Security Requirements"
    findings = phase2.check([good, bad], run_dir=None)
    check("the clean row raises nothing of its own",
          not any("PO-D-01.1-001" in f for f in findings),
          f"{[f for f in findings if 'PO-D-01.1-001' in f]}")
    check("a row carrying ```yaml + req_id: is caught",
          any("raw baseline" in f and "PO-D-01.1-999" in f for f in findings),
          f"{len(findings)} finding(s)")


def test_prefix_gate() -> None:
    print("\ngate G2 — prefix follows regulation (§4.4)")
    wrong = phase2.derive_objective(REPO, goal("AG-D-03.1-001", "GDPR"))
    wrong["objective_id"] = "SO-D-03.1-001"      # the Case 01 defect, by hand
    findings = phase2.check([wrong], run_dir=None)
    check("an SO- prefix on a GDPR row is caught",
          any("prefix" in f for f in findings), f"{findings}")


def test_coverage_gate() -> None:
    print("\ngate G0 — upstream completeness")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR")], selected=["D-01.1", "D-06.1"])
        rows = phase2.build(REPO, run)
        findings = phase2.check(rows, run)
        check("a selected sub-domain with no goal artifact is caught",
              any("upstream incomplete" in f for f in findings), f"{findings}")
        check("the missing sub-domain is named",
              any("D-06.1" in f for f in findings), "")


def test_seams_stay_unset() -> None:
    print("\nseams")
    r = phase2.derive_objective(REPO, goal("AG-D-01.1-001", "GDPR"))
    unset = [c for c in ("criteria", "method", "owner") if r[c] == phase2.UNSET]
    check("cells with no rule stay UNSET rather than filled",
          len(unset) == 3, f"unset={unset}")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR")], selected=["D-01.1"])
        text = phase2.render_doc01(REPO, run, phase2.build(REPO, run))
        check("the rendered document declares the seams",
              "seam" in text.lower(), "")
        check("no placeholder leaks into the rendered statement",
              "TODO" not in text and "FIXME" not in text and "None" not in text)


def test_end_to_end_cli() -> None:
    print("\nCLI end to end")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        run = synth_run(tmp, [goal("AG-D-01.1-001", "GDPR"),
                              goal("AG-D-01.1-002", "CRA")], selected=["D-01.1"])
        out = tmp / "out"
        proc = subprocess.run(
            [sys.executable, str(REPO / "pipeline" / "src" / "phase2.py"),
             "--run-dir", str(run), "--repo", str(REPO), "--out", str(out)],
            capture_output=True, text=True)
        check("exits 0 on a complete run", proc.returncode == 0,
              proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr[:200])
        doc = out / "Doc01_Operational_Objectives.md"
        check("Doc01 is written", doc.exists())
        text = doc.read_text(encoding="utf-8")
        check("both objectives are rendered",
              "PO-D-01.1-001" in text and "SO-D-01.1-002" in text)
        check("unrendered seams show the UNSET marker",
              text.count("| — |") >= 4, f"{text.count('| — |')} UNSET cells")


def main() -> int:
    print("phase2_test — derivations anchored to Phase 1 and the corpus")
    for fn in (test_id_derivation, test_slot_inherited, test_anchors_resolve,
               test_pollution_gate, test_prefix_gate, test_coverage_gate,
               test_seams_stay_unset, test_end_to_end_cli):
        fn()
    print()
    if FAILURES:
        print(f"FAIL — {len(FAILURES)}: {', '.join(FAILURES)}")
        return 1
    print("PASS — every derivation holds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())