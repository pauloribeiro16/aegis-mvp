#!/usr/bin/env python3
"""phase3_onda_c_test.py — the Onda C guards refuse what run_p2enr_c1 shipped.

Three guards, each against a measured failure:

* `check_fit_criterion_observable` — the proposal stage pre-baked mechanisms
  ("MFA", "static analysis", "encryption") into the acceptance bar; a
  criterion that names the implementation is not a black-box test.
* `check_no_invented_identifiers` — the principle call invented permission
  names (`key_management`, `operational_execution`) that exist in no corpus.
* the mode-collapse alert — 52 of 65 objectives routed organizational in one
  run and nothing said so; >65% organizational across D-02..D-07 is that
  failure recurring.

Usage: python3 pipeline/tests/phase3_onda_c_test.py
Exit 0 iff every guard holds.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.guards.quality_gates import (  # noqa: E402
    check_fit_criterion_observable,
    check_no_invented_identifiers,
)
from aegis_pipeline.phases.phase3 import proposals as p3p  # noqa: E402
from aegis_pipeline.phases.phase3 import verdicts as p3vd  # noqa: E402

HEADER = ("| Objective | Summary | Functional carrier | Skill | State | VC discharge | Action |\n"
          "|---|---|---|---|---|---|---|\n")


def test_a_black_box_criterion_passes() -> None:
    assert check_fit_criterion_observable(
        "An expired session fails; a request without valid credentials is rejected before "
        "any payload is processed") == []


def test_a_mechanism_in_the_criterion_is_rejected() -> None:
    for bad in ("Access requires MFA and a strong password",
                "The payload is encrypted at rest with an approved cipher",
                "Static analysis blocks the release until clean",
                "A firewall rule denies unknown origins"):
        findings = check_fit_criterion_observable(bad)
        assert findings, bad
        assert "mechanism" in findings[0], (bad, findings)


def test_a_short_criterion_is_not_a_test() -> None:
    findings = check_fit_criterion_observable("Sessions work")
    assert findings and "too short" in findings[0]


def test_the_constraint_may_keep_the_neutral_property_wording() -> None:
    """The guard judges the CRITERION only — the constraint keeps the ADR-009
    neutral vocabulary ("authenticated and encrypted channel"), which is the
    property, not the mechanism."""
    assert check_fit_criterion_observable(
        "A connection that cannot present valid credentials is rejected before any "
        "payload is processed") == []


def test_invented_identifiers_are_rejected_against_the_pack() -> None:
    pack = ("`key_rotation` appears here; so does `task_data` and the anchor `PR.DS-02` "
            "and the card `R1.1`")
    answer = "The system shall enforce `key_rotation` and honour `task_data` boundaries."
    assert check_no_invented_identifiers(answer, pack) == []
    invented = check_no_invented_identifiers(
        "The system shall enforce `key_management` per `operational_execution`.", pack)
    assert len(invented) == 2 and "key_management" in invented[0]


def test_the_proposal_parser_enforces_the_observable_criterion() -> None:
    """The guard lives inside parse_proposals — a repair round cannot ship it."""
    target = [{"id": "SO-D-01.1-001", "subdomain": "D-01.1"}]
    answer = """```markdown
### SO-D-01.1-001

**Constraint (EARS):** Where a session is established, the system shall expire it after inactivity.
**Fit criterion:** Access requires MFA.
**Risk addressed:** session hijack
**Chain anchors:** `GV.RR-02`
**Proposed carrier:** `R1.1`
```"""
    try:
        p3p.parse_proposals(answer, target)
    except ValueError as e:
        assert "mechanism" in str(e)
    else:
        raise AssertionError("a mechanism-baked fit criterion must fail L0")


def test_mode_collapse_above_the_threshold_is_a_finding() -> None:
    rows = [{"id": f"SO-D-0{n}.{k}-001", "subdomain": f"D-0{n}.{k}",
             "verdict": "No functional carrier (organizational)",
             "discharge": "x", "anchors_cited": []}
            for n in range(2, 8) for k in (1, 2)]
    objectives = [{"id": r["id"], "anchors": set(), "subdomain": r["subdomain"]} for r in rows]
    findings = p3vd.check_verdicts(rows, objectives, [])
    assert any("mode collapse" in f for f in findings), findings


def test_a_mixed_matrix_raises_no_mode_collapse() -> None:
    rows = []
    for i, (n, k) in enumerate([(n, k) for n in range(2, 8) for k in (1, 2)]):
        rows.append({"id": f"SO-D-0{n}.{k}-001", "subdomain": f"D-0{n}.{k}",
                     "verdict": ("No functional carrier (organizational)" if i % 2
                                 else "Partially covered (functional leg + explicit carve-out)"),
                     "discharge": "x", "anchors_cited": []})
    objectives = [{"id": r["id"], "anchors": {"GV.RR-02"}, "subdomain": r["subdomain"]} for r in rows]
    findings = p3vd.check_verdicts(rows, objectives, [])
    assert not any("mode collapse" in f for f in findings), findings


def test_small_tech_batches_do_not_trigger_the_alert() -> None:
    """The alert needs a batch: 4 technical rows are noise, not collapse."""
    rows = [{"id": f"SO-D-0{n}.1-001", "subdomain": f"D-0{n}.1",
             "verdict": "No functional carrier (organizational)",
             "discharge": "x", "anchors_cited": []}
            for n in range(2, 6)]
    objectives = [{"id": r["id"], "anchors": set(), "subdomain": r["subdomain"]} for r in rows]
    assert not any("mode collapse" in f for f in p3vd.check_verdicts(rows, objectives, []))


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
