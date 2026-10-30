#!/usr/bin/env python3
"""phase3_rounds_test.py — the multi-round engine (Onda B, Etapa 1.6/1.6.b).

The measured defect this file pins: an all-`Adjust` round counted as CONVERGED
(`converged = not open`), the weave absorbed proposals no human ever approved,
and nothing told the model to rewrite the adjusted items. The assertions here
hold the opposite contract:

* an `Adjust` verdict puts the item in `pending_adjustment[]` with the human's
  note, and the round does NOT converge;
* convergence ⇔ no open AND no pending adjustment;
* a D3 functional change retires the item; a bad kind or an unknown item raises;
* the repropose stage rewrites exactly the pending items and opens round N+1.

Usage: python3 pipeline/tests/phase3_rounds_test.py
Exit 0 iff the engine holds.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3 import proposals as p3p  # noqa: E402
from aegis_pipeline.phases.phase3 import verdicts as p3vd  # noqa: E402

PROPOSALS = [
    {"objective": "SO-D-01.1-001", "subdomain": "D-01.1", "constraint": "the system shall constrain sessions",
     "fit_criterion": "an expired session fails", "risk": "session hijack",
     "anchors": ["GV.RR-02"], "rules": [], "carrier": "`R1.1`"},
    {"objective": "SO-D-05.1-001", "subdomain": "D-05.1", "constraint": "the system shall enforce least privilege",
     "fit_criterion": "a role outside its scope fails", "risk": "privilege creep",
     "anchors": ["PR.AA-05"], "rules": [], "carrier": "`R1.2`"},
]

VERDICT_TABLE_HEADER = (
    "| Objective | Summary | Functional carrier | Skill | State | VC discharge | Action |\n"
    "|---|---|---|---|---|---|---|\n")


def test_adjust_blocks_convergence_and_carries_the_note() -> None:
    state = p3p.apply_round_verdicts(
        PROPOSALS, {"SO-D-01.1-001": "Adjust"}, notes={"SO-D-01.1-001": "Separate the lock from the notification"})
    assert not state["converged"], "an all-Adjust round must NOT converge"
    assert len(state["pending_adjustment"]) == 1
    pending = state["pending_adjustment"][0]
    assert pending["adjust_note"] == "Separate the lock from the notification"
    assert pending["objective"] == "SO-D-01.1-001"
    assert state["adjusted"] == state["pending_adjustment"] or state["adjusted"], "the raw adjusted list stays"


def test_converged_iff_no_open_and_no_pending() -> None:
    ok = p3p.apply_round_verdicts(PROPOSALS, {"SO-D-01.1-001": "Accept", "SO-D-05.1-001": "Reject"})
    assert ok["converged"] and ok["rejected"][0]["objective"] == "SO-D-05.1-001"
    open_item = p3p.apply_round_verdicts(PROPOSALS, {"SO-D-01.1-001": "Accept"})
    assert not open_item["converged"] and open_item["open"] == ["SO-D-05.1-001"]


def test_reject_carries_its_note() -> None:
    state = p3p.apply_round_verdicts(
        PROPOSALS, {"SO-D-01.1-001": "Accept", "SO-D-05.1-001": "Reject"},
        notes={"SO-D-05.1-001": "risk accepted for this version"})
    assert state["rejected"][0]["reject_note"] == "risk accepted for this version"


def test_a_d3_change_retires_the_item_and_skips_the_repropose() -> None:
    state = p3p.apply_round_verdicts(
        PROPOSALS, {"SO-D-01.1-001": "Adjust", "SO-D-05.1-001": "Accept"},
        notes={"SO-D-01.1-001": "the surface goes away"},
        functional_changes=[{"item": "SO-D-01.1-001", "kind": "D3", "target": "R1.1", "note": "retire"}])
    assert state["retired"] and state["retired"][0]["objective"] == "SO-D-01.1-001"
    assert not state["pending_adjustment"], "a retired item is not rewritten"
    assert state["converged"], "retire + accept = nothing open, nothing pending"


def test_a_bad_change_kind_or_unknown_item_raises() -> None:
    for bad in ({"item": "SO-D-01.1-001", "kind": "D9"}, {"item": "SO-D-99.9-999", "kind": "D1"}):
        try:
            p3p.apply_round_verdicts(PROPOSALS, {}, functional_changes=[bad])
        except ValueError as e:
            assert "functional change" in str(e) or "not an item" in str(e)
        else:
            raise AssertionError(f"{bad} must raise")


def test_latest_round_and_paths_discover_the_round_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        assert p3p.latest_round(run) == 1  # no round files yet
        (run / "steps" / "phase3").mkdir(parents=True)
        p3p.round_verdicts_path(run, 1).write_text("{}", encoding="utf-8")
        assert p3p.latest_round(run) == 1
        p3p.round_state_path(run, 2).write_text("{}", encoding="utf-8")
        assert p3p.latest_round(run) == 2


def _runner_stub(run: Path, responses: dict[str, str]):
    """A StepRunner-shaped stub: _call writes what the model would store."""

    class _Stub:
        run_dir = run
        repo = REPO
        dry_run = False

        def _call(self, step: str, subdomain):
            _, round_no, key = step.split(":", 2)
            out = run / "steps" / "phase3" / "repropose" / f"r{round_no}" / f"{key}.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            # store_parsed writes the bare revised proposal (parsed["proposals"][0])
            out.write_text(json.dumps(json.loads(responses[key])["proposals"][0]),
                           encoding="utf-8")

        def _write_stage_result(self, name, payload):
            (run / "steps" / "stage_results").mkdir(parents=True, exist_ok=True)
            (run / "steps" / "stage_results" / f"{name}.json").write_text(
                json.dumps(payload, indent=1), encoding="utf-8")

    return _Stub()


def test_the_repropose_stage_rewrites_exactly_the_pending_items() -> None:
    """The full 1.6.b loop with the model stubbed at the store boundary."""
    from aegis_pipeline.phases.phase1.runner import StepRunner

    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3"
        store.mkdir(parents=True)
        n = 1
        p3p.round_state_path(run, n).write_text(json.dumps({
            "accepted": [], "rejected": [], "adjusted": PROPOSALS[:1],
            "pending_adjustment": [{**PROPOSALS[0], "adjust_note": "split the lock out"}],
            "retired": [], "open": [], "converged": False, "round": 1,
            "functional_changes": [],
        }), encoding="utf-8")
        revised = {"SO-D-01.1-001": json.dumps(
            {"proposals": [{**PROPOSALS[0], "constraint": "the system shall lock the account",
                            "fit_criterion": "a third consecutive failure locks"}]})}
        StepRunner.stage_p3a_repropose(_runner_stub(run, revised))

        blob = json.loads(p3p.round_proposals_path(run, 2).read_text(encoding="utf-8"))
        assert blob["from_round"] == 1 and blob["round"] == 2
        assert len(blob["proposals"]) == 1
        assert blob["proposals"][0]["constraint"] == "the system shall lock the account"
        assert blob["carried"] == {"accepted": [], "rejected": [], "retired": []}
        assert p3p.round_verdicts_path(run, 2).is_file(), "round 2 verdicts scaffolded"
        assert (run / "outputs" / "phase3" / "synthesis_rounds" / "ROUND2_REGISTER.md").is_file()


def test_the_repropose_stage_refuses_without_pending_items() -> None:
    from aegis_pipeline.phases.phase1.runner import StepRunner

    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3"
        store.mkdir(parents=True)
        p3p.round_state_path(run, 1).write_text(json.dumps({
            "accepted": PROPOSALS, "rejected": [], "adjusted": [],
            "pending_adjustment": [], "open": [], "converged": True,
        }), encoding="utf-8")
        try:
            StepRunner.stage_p3a_repropose(_runner_stub(run, {}))
        except ValueError as e:
            assert "no pending adjustment" in str(e)
        else:
            raise AssertionError("a converged round must not repropose")


def test_the_round_stage_accumulates_carried_decisions() -> None:
    """Round 2's ledger shows the carried accepted/rejected plus the revisions."""
    from aegis_pipeline.phases.phase1.runner import StepRunner

    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3"
        store.mkdir(parents=True)
        (run / "steps" / "gates").mkdir(parents=True)
        (run / "steps" / "gates" / "G-P3-A.approved").write_text("round 2 review", encoding="utf-8")
        p3p.round_proposals_path(run, 2).write_text(json.dumps({
            "from_round": 1, "round": 2, "proposals": PROPOSALS[:1],
            "carried": {"accepted": PROPOSALS[1:], "rejected": [], "retired": []},
        }), encoding="utf-8")
        verdicts = p3p.round_verdicts_path(run, 2)
        verdicts.write_text(json.dumps({"verdicts": {"SO-D-01.1-001": "Accept"}, "notes": {}}),
                            encoding="utf-8")

        class _Stub:
            run_dir = run
            repo = REPO
            dry_run = False

            def _call(self, step, subdomain):
                raise AssertionError("p3a_round makes no model call")

            def _write_stage_result(self, name, payload):
                (run / "steps" / "stage_results").mkdir(parents=True, exist_ok=True)
                (run / "steps" / "stage_results" / f"{name}.json").write_text(
                    json.dumps(payload, indent=1), encoding="utf-8")

        StepRunner.stage_p3a_round(_Stub())
        state = json.loads(p3p.round_state_path(run, 2).read_text(encoding="utf-8"))
        assert state["converged"]
        assert {p["objective"] for p in state["accepted"]} == {
            "SO-D-01.1-001", "SO-D-05.1-001"}, "carried + newly accepted"
        assert state["round"] == 2


def test_the_action_column_is_a_pure_enum() -> None:
    row = ("| `SO-D-01.1-001` | s | `R1.1` | TB | Fully covered (anchored) "
           "| cites `GV.RR-02` | PROPOSE_PRODUCT |")
    rows = p3vd.parse_verdicts(VERDICT_TABLE_HEADER + row)
    assert rows[0]["action"] == "PROPOSE_PRODUCT"

    free_text = row.replace("PROPOSE_PRODUCT", "Propose for Round 2: needs a constraint")
    try:
        p3vd.parse_verdicts(VERDICT_TABLE_HEADER + free_text)
    except ValueError as e:
        assert "routing enum" in str(e)
    else:
        raise AssertionError("free-text Action must fail L0 — it is the mode the plan retires")


def test_select_proposal_targets_reads_the_enum_and_not_free_text() -> None:
    enum_rows = [{"id": "A", "action": "PROPOSE_PRODUCT"},
                 {"id": "B", "action": "ROUTE_ORG"},
                 {"id": "C", "action": "CARRIED"}]
    assert [r["id"] for r in p3p.select_proposal_targets(enum_rows)] == ["A"]
    legacy = [{"id": "D", "action": "Propose for Round 2: pending"}]
    assert p3p.select_proposal_targets(legacy) == [], "legacy free text is visible, never mined"


def test_the_register_renders_round_notes_and_changes() -> None:
    text = p3p.render_round_register(
        PROPOSALS, {"SO-D-01.1-001": "Adjust"}, converged=False, round_no=2,
        notes={"SO-D-01.1-001": "split the lock"},
        functional_changes=[{"item": "SO-D-01.1-001", "kind": "D1", "target": "R1.1", "note": "x"}],
        duty_proposals=[{"duty": "Review access", "objectives": ["SO-D-05.1-001"],
                         "disposition": "ORG", "scale_fact": ""}],
        carried={"accepted": PROPOSALS[1:], "rejected": [], "retired": []})
    assert "ROUND2_REGISTER" in text
    assert "| P-01 |" in text and "split the lock" in text
    assert "## §2 Functional change register (D1–D4)" in text and "D1" in text
    assert "## §3 Duty dispositions" in text and "Review access" in text
    assert "SO-D-05.1-001" in text and "carried" in text
    assert "round2_verdicts.json" in text


def test_a_rejected_objective_discharges_in_the_matrix() -> None:
    """Onda E fix: a Reject verdict lands in the coverage matrix (T5, 2168120)."""
    from aegis_pipeline.phases.phase3 import weave as p3w
    rows = [
        {"id": "SO-D-01.1-002", "carrier": "`—`", "discharge": "old text", "verdict": "x"},
        {"id": "SO-D-01.1-001", "carrier": "`R1.1`", "discharge": "kept", "verdict": "y"},
    ]
    state = {"round": 1, "rejected": [{"objective": "SO-D-01.1-002",
                                       "risk": "encryption at rest deferred"}]}
    out = p3w.apply_reject_discharge(rows, state)
    assert out[0]["carrier"] == "`RN (a derivar)`", out[0]
    assert "REJECTED" in out[0]["discharge"] and "round-1" in out[0]["discharge"], out[0]
    assert "encryption at rest" in out[0]["discharge"], out[0]
    assert out[1]["carrier"] == "`R1.1`" and out[1]["discharge"] == "kept", out[1]


def test_no_rejections_leaves_the_rows_untouched() -> None:
    from aegis_pipeline.phases.phase3 import weave as p3w
    rows = [{"id": "SO-D-01.1-001", "carrier": "`R1.1`", "discharge": "kept", "verdict": "y"}]
    out = p3w.apply_reject_discharge(rows, {"rejected": []})
    assert out[0]["carrier"] == "`R1.1`" and out[0]["discharge"] == "kept", out[0]


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_") or not callable(fn):
            continue
        try:
            fn()
            print(f"  [OK ] {name}")
        except AssertionError as e:
            failures += 1
            print(f"  [FAIL] {name}: {e}")
        except Exception as e:
            failures += 1
            print(f"  [FAIL] {name}: {type(e).__name__}: {e}")
    print(f"\n{'FAIL' if failures else 'OK'} — {failures} failure(s)")
    sys.exit(1 if failures else 0)
