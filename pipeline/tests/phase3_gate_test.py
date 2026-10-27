#!/usr/bin/env python3
"""phase3_gate_test.py — the exit gate has to FAIL when it should.

The gate said `CONCLUDED` with all six G1–G6 CLOSED on `run_p2enr_c1` while the
run's own `round1_state.json` read `converged: false` with seven open verdicts,
`PRINCIPLE_MAPPING.md` read "Bound 0 / Pending 7", and the SUFFICIENCY file
printed the same per-regulation line twice. Every one of those passed.

So the assertion that matters for a gate is not "it passes on a good run" — it
is **"it refuses on a bad one"**. Each test here builds the run that shipped and
requires the gate to reject it. They need no model and no GPU: the gate is a
pure function of the artifacts on disk.

Usage: python3 pipeline/tests/phase3_gate_test.py
Exit 0 iff every gate fails when it must.
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

import phase3  # noqa: E402
import phase3_schemas as S  # noqa: E402
from aegis_pipeline.phases.phase3 import weave  # noqa: E402

CASE = "Case_01_TinyTask_SaaS"


def _build_run(tmp: Path, *, open_items: list[str], converged: bool) -> Path:
    """A run with a verdict per objective, a round, and two Phase 3 deliverables."""
    run_dir = tmp / "run"
    (run_dir / "steps" / "phase3").mkdir(parents=True)
    (run_dir / "outputs" / "phase2").mkdir(parents=True)
    (run_dir / "outputs" / "phase3" / "synthesis_rounds").mkdir(parents=True)
    (run_dir / "steps" / "gates").mkdir(parents=True)
    shutil.copy(
        REPO / "cases" / CASE / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md",
        run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md",
    )
    (run_dir / "manifest.json").write_text(json.dumps({"case_id": CASE}), encoding="utf-8")

    objs = phase3.load_objectives(run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md")
    anchored = {o["id"] for o in objs if o.get("anchors")}
    by_sd: dict[str, list[str]] = {}
    for obj in objs:
        by_sd.setdefault(obj["subdomain"].replace(".", "_"), []).append(obj["id"])
    for sd, ids in by_sd.items():
        # Technical domains D-02..D-07 route partially covered — an all-org
        # matrix there IS the mode-collapse state the Onda C guard blocks, and
        # this fixture is the CONTROL the other tests isolate against. Only
        # ANCHORED objectives may route partial: a process obligation with no
        # published anchor claiming a carrier is a T6 finding of its own.
        partial = sd[:4] in {f"D-0{n}" for n in range(2, 8)}
        (run_dir / "steps" / "phase3" / f"verdicts_{sd}.json").write_text(json.dumps([
            {"id": i,
             "verdict": ("Partially covered (functional leg + explicit carve-out)"
                         if partial and i in anchored else S.ORGANIZATIONAL),
             "carrier": "`—`", "skill": "`—`",
             "discharge": "the named obligation; the carve-out is recorded",
             "action": "ROUTE_ORG"}
            for i in ids
        ]), encoding="utf-8")

    (run_dir / "steps" / "phase3" / "round1_state.json").write_text(json.dumps({
        "accepted": [{"objective": "SO-D-01.1-001", "constraint": "c", "risk": "r", "carrier": "R1.1"}],
        "rejected": [], "adjusted": [], "open": open_items, "converged": converged,
    }), encoding="utf-8")
    (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "ROUND1_REGISTER.md").write_text(
        "scaffold", encoding="utf-8")
    (run_dir / "steps" / "gates" / "G-P3-A.approved").write_text("human verdict", encoding="utf-8")
    # run_gate refuses to build rows without the rendered matrix present; the
    # verdicts themselves are read from steps/phase3/verdicts_*.json.
    (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "OBJECTIVE_MAPPING.md").write_text(
        "# Objective mapping\n\n| Id | Sub-domain | Verdict |\n|---|---|---|\n", encoding="utf-8")

    # STEP4 with exactly one absorption row for the one accepted constraint.
    (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "STEP4_CONSTRAINT_ABSORPTION.md").write_text(
        "---\ntitle: 'STEP4'\n---\n\n"
        "| Objective | Constraint | Carrier card | In pool? |\n|---|---|---|---|\n"
        "| `SO-D-01.1-001` | c | R1.1 | yes |\n", encoding="utf-8")
    # SUFFICIENCY with two genuinely different per-regulation verdicts.
    (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md").write_text(
        "---\ntitle: 'SUFFICIENCY_ASSESSMENT'\n---\n\n"
        "## Compliance verdict per regulation\n\n"
        f"- **GDPR:** {len(objs)} fully covered, 0 partial, 0 organizational\n"
        f"- **CRA:** 0 fully covered, 0 partial, {len(objs)} organizational\n", encoding="utf-8")
    return run_dir


def _gates(run_dir: Path) -> dict:
    return weave.run_gate(run_dir, REPO)["gates"]


def test_a_converged_objective_round_with_unplaced_principles_is_not_closed() -> None:
    """The shipped defect. Every objective was verdicted and the round had
    converged, so G1 said CLOSED — while seven principles sat at "Pending".
    ADR-006 puts the principles inside G1, not only inside G2."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        assert _gates(run_dir)["G1"].startswith("CLOSED"), "control: clean run must close G1"
        # now what actually shipped: seven principle verdicts appeared later
        (run_dir / "steps" / "phase3" / "round1_state.json").write_text(json.dumps({
            "accepted": [{"objective": "SO-D-01.1-001", "constraint": "c", "risk": "r", "carrier": "R1.1"}],
            "rejected": [], "adjusted": [],
            "open": [f"PRIN-ENG-0{i}" for i in range(1, 8)], "converged": True,
        }), encoding="utf-8")
        gates = _gates(run_dir)
        assert not gates["G1"].startswith("CLOSED"), f"7 unplaced principles passed G1: {gates['G1']}"
        assert "7 principle(s) unplaced" in gates["G1"], gates["G1"]


def test_a_verdict_that_outlives_its_inputs_is_visible_as_stale() -> None:
    """The verdict that shipped was correct when written at 16:36 and wrong by
    21:00. The report has to say which inputs it judged, so a reader can tell."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        first = weave.run_gate(run_dir, REPO)
        assert first["inputs_digest"]
        report_path = run_dir / "steps" / "phase3" / "gate_report.md"
        report_path.write_text(weave.render_gate_report(first), encoding="utf-8")
        assert weave.previous_digest(run_dir) == first["inputs_digest"]
        assert not weave.gate_report_is_stale(run_dir), "control: a fresh report is not stale"

        state = json.loads((run_dir / "steps" / "phase3" / "round1_state.json").read_text())
        state["open"] = ["PRIN-ENG-01"]
        state["converged"] = False
        (run_dir / "steps" / "phase3" / "round1_state.json").write_text(
            json.dumps(state), encoding="utf-8")

        second = weave.run_gate(run_dir, REPO)
        assert second["inputs_digest"] != first["inputs_digest"], "digest did not move"
        assert second["state"] == "PROPOSED", second["state"]
        assert weave.previous_digest(run_dir) == first["inputs_digest"], \
            "the report on disk must still carry the verdict it was written with"
        # ... and the report on disk must be recognisable as overtaken. Before
        # this, the plumbing existed on both sides and nothing joined them:
        # the digest moved and no reader could act on it.
        assert weave.gate_report_is_stale(run_dir), \
            "the report on disk still reads as current after its inputs changed"
        assert second["previous_verdict_stale"], \
            "run_gate did not notice that the verdict it replaces was already stale"


def test_the_report_file_is_marked_stale_when_a_stage_writes_after_the_gate() -> None:
    """The report file is what a reader opens. The stage record is what a
    script reads. Both have to say the verdict is overtaken — otherwise the
    file still says CONCLUDED over a run that is PROPOSED."""
    from aegis_pipeline.phases.phase1.runner import StepRunner

    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        report = weave.run_gate(run_dir, REPO)
        report_path = run_dir / "steps" / "phase3" / "gate_report.md"
        report_path.write_text(weave.render_gate_report(report), encoding="utf-8")
        assert "state: CONCLUDED" in report_path.read_text(encoding="utf-8")

        class _Runner:
            pass

        stub = _Runner()
        stub.run_dir = run_dir
        StepRunner._write_stage_result(stub, "p3a_round", {
            "status": "partial", "carried": 12, "selected": 25, "failed": 0, "summary": "7 open",
        })

        text = report_path.read_text(encoding="utf-8")
        assert "state: STALE" in text, "the report on disk still claims to be current"
        assert "stale_since: p3a_round" in text, text
        # the digest it judged is kept: that is the record of what it was about
        assert f"inputs_digest: {report['inputs_digest']}" in text, text
        # and marking it twice is not an error
        assert weave.invalidate_gate_report(run_dir, "p3a_org") is False


def test_a_hand_edit_to_an_input_is_detected_without_a_stage_running() -> None:
    """The choke point catches a stage writing. A human editing a file is not
    a stage — the reader-side check is what catches that."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        report = weave.run_gate(run_dir, REPO)
        (run_dir / "steps" / "phase3" / "gate_report.md").write_text(
            weave.render_gate_report(report), encoding="utf-8")
        assert not weave.gate_report_is_stale(run_dir), "control: a fresh report is not stale"

        mapping = run_dir / "outputs" / "phase3" / "synthesis_rounds" / "OBJECTIVE_MAPPING.md"
        mapping.write_text(mapping.read_text(encoding="utf-8") + "\nan extra row\n", encoding="utf-8")
        assert weave.gate_report_is_stale(run_dir), \
            "a hand edit to a gate input left the report reading as current"


def test_g4_lints_this_run_and_not_the_hand_written_corpus() -> None:
    """`doc_lint --strict` walks `cases/ example/ output/` on its own, and
    `output/TinyTask/phase3/` was empty — so G4 passed on 0 bytes of the run."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        assert _gates(run_dir)["G4"].startswith("CLOSED"), "control: clean deliverables close G4"
        broken = run_dir / "outputs" / "phase3" / "synthesis_rounds" / "Doc01_draft.md"
        broken.write_text("# Doc\n\n| Item | Status |\n|---|---|\n| Encryption | ? |\n", encoding="utf-8")
        gate = _gates(run_dir)["G4"]
        assert not gate.startswith("CLOSED"), f"an R12 placeholder in the run passed G4: {gate}"
        assert "placeholder-cell" in gate, gate


def test_g5_rejects_one_total_relabelled_per_regulation() -> None:
    """The shipped defect: GDPR and CRA carried byte-identical counts because the
    renderer printed the whole-matrix total once per regulation."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        assert _gates(run_dir)["G5"].startswith("CLOSED"), "control: distinct counts close G5"
        n = len(phase3.load_objectives(run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"))
        (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md").write_text(
            "## Compliance verdict per regulation\n\n"
            f"- **GDPR:** 0 fully covered, 13 partial, {n - 13} organizational\n"
            f"- **CRA:** 0 fully covered, 13 partial, {n - 13} organizational\n", encoding="utf-8")
        gate = _gates(run_dir)["G5"]
        assert not gate.startswith("CLOSED"), f"identical per-regulation lines passed G5: {gate}"
        assert "same counts" in gate, gate


def test_g5_needs_a_per_regulation_line_at_all() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "SUFFICIENCY_ASSESSMENT.md").write_text(
            "---\ntitle: 'SUFFICIENCY_ASSESSMENT'\n---\n\n## Compliance verdict\n\nAll good.\n", encoding="utf-8")
        gate = _gates(run_dir)["G5"]
        assert not gate.startswith("CLOSED"), gate
        assert "no per-regulation verdict line" in gate, gate


def test_g6_needs_one_absorption_row_per_accepted_constraint() -> None:
    """G6 was `is_file()`. A table that silently drops half the absorbed
    constraints is the failure it was supposed to catch."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        assert _gates(run_dir)["G6"].startswith("CLOSED"), "control: matching rows close G6"
        state = json.loads((run_dir / "steps" / "phase3" / "round1_state.json").read_text())
        state["accepted"].append({"objective": "SO-D-01.2-001", "constraint": "c2",
                                  "risk": "r2", "carrier": "R1.2"})
        (run_dir / "steps" / "phase3" / "round1_state.json").write_text(
            json.dumps(state), encoding="utf-8")
        gate = _gates(run_dir)["G6"]
        assert not gate.startswith("CLOSED"), f"an under-counted absorption table passed G6: {gate}"
        assert "1 absorption row(s) for 2 accepted" in gate, gate


def test_a_p3a_stage_writing_after_the_gate_marks_it_stale_in_the_manifest() -> None:
    """The manifest is the other reader. It carried `p3a_gate: ok` and
    `p3a_round: partial / 7 open` side by side for three days."""
    from aegis_pipeline.phases.phase1.runner import StepRunner

    with tempfile.TemporaryDirectory() as tmp:
        run_dir = Path(tmp) / "run"
        run_dir.mkdir()
        (run_dir / "manifest.json").write_text(json.dumps({"run_id": run_dir.name}), encoding="utf-8")

        class _Runner:
            pass

        stub = _Runner()
        stub.run_dir = run_dir
        StepRunner._write_stage_result(stub, "p3a_gate", {
            "status": "ok", "carried": 1, "selected": 1, "failed": 0,
            "summary": "state=CONCLUDED; G1 CLOSED", "gates": {"G1": "CLOSED"},
        })
        StepRunner._write_stage_result(stub, "p3a_round", {
            "status": "partial", "carried": 12, "selected": 25, "failed": 0, "summary": "7 open",
        })
        stored = json.loads((run_dir / "steps" / "stage_result.json").read_text())["stages"]
        assert stored["p3a_gate"]["status"] == "stale", stored["p3a_gate"]
        assert "p3a_round" in stored["p3a_gate"]["summary"], stored["p3a_gate"]
        # the round's own verdict is untouched
        assert stored["p3a_round"]["status"] == "partial", stored["p3a_round"]
        # and the manifest block carries the staleness too
        manifest = json.loads((run_dir / "manifest.json").read_text())
        assert manifest["stage_result"]["p3a_gate"]["status"] == "stale", manifest["stage_result"]["p3a_gate"]


def test_the_gate_fails_when_the_chain_has_a_referential_finding() -> None:
    """R12b: the chains must be re-anchored "before any coverage verdict is
    credible". The gate's own docstring claimed it ran T1-T6; it did not, and
    on run_p2enr_c1 it reported CONCLUDED over a deliverable whose chain cites
    GDPR while its only driver is a CRA objective."""
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = _build_run(Path(tmp), open_items=[], converged=True)
        report = weave.run_gate(run_dir, REPO)
        assert not report["chain_findings"], report["chain_findings"]
        assert report["state"] == "CONCLUDED", report["state"]

        deliverable = run_dir / "outputs" / "phase3" / "Doc01_Requirements_Specification.md"
        deliverable.write_text(
            "# Requirements\n\n"
            "**Chain:** GDPR Art. 32(1)(a) -> `SO-D-01.2-002` -> `PR.DS-02`\n",
            encoding="utf-8")
        report = weave.run_gate(run_dir, REPO)
        assert report["chain_findings"], "a law cited with a foreign driver passed the gate"
        assert report["state"] != "CONCLUDED", report["state"]


def test_sufficiency_counts_each_regulation_separately() -> None:
    """The renderer is G5's evidence, so it has to compute per regulation. On
    run_p2enr_c1's own matrix that is CRA 0/7/29 over 36 objectives and GDPR
    0/6/23 over 29 — not one total printed twice."""
    objs = phase3.load_objectives(
        REPO / "cases" / CASE / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md")
    rows = phase3.build(objs)
    for row in rows:
        row["verdict"] = S.ORGANIZATIONAL
    text = weave.render_sufficiency(rows, {"accepted": [], "rejected": [], "open": []}, ["GDPR", "CRA"])
    lines = {m["reg"]: m for m in weave.RE_SUFFICIENCY_ROW.finditer(text)}
    assert set(lines) == {"GDPR", "CRA"}, lines
    assert int(lines["GDPR"]["org"]) != int(lines["CRA"]["org"]), \
        f"the two regulations carry the same count: {lines}"
    # every objective lands under exactly one regulation
    assert sum(int(m["org"]) for m in lines.values()) == len(rows), \
        f"per-regulation counts do not sum to {len(rows)} objectives"


if __name__ == "__main__":
    failures = 0
    ran = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_") or not callable(fn):
            continue
        ran += 1
        try:
            fn()
            print(f"  [OK ] {name}")
        except AssertionError as e:
            failures += 1
            print(f"  [FAIL] {name}: {e}")
        except Exception as e:
            failures += 1
            print(f"  [FAIL] {name}: {type(e).__name__}: {e}")
    print(f"\n{'FAIL' if failures else 'OK'} — {ran} ran, {failures} failure(s)")
    sys.exit(1 if failures else 0)