#!/usr/bin/env python3
"""phase3_org_cluster_test.py — the automated duty clustering (Onda B, Etapa 1.5).

The manual `duty_audit.md` was Finding F1 of EXP_P3_01: it blocked `p3a_all`
in a single job. The cluster stage replaces it, and the contract it must hold
is the one the audit recorded:

* the proposal is a PARTITION — every organizational objective in exactly one
  duty, no invented id, none duplicated, none dropped;
* a `SCALE` carve-out cites a company fact, or it is a preference;
* the human's `"duties"` overrides win over the model's proposal;
* the downstream join (`render_doc03`) is by slug, so a duty whose card failed
  names the gap instead of shifting every card onto the wrong duty.

Usage: python3 pipeline/tests/phase3_org_cluster_test.py
Exit 0 iff the contract holds.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3 import org as p3o  # noqa: E402

ORG_IDS = {"SO-D-05.1-001", "PO-D-05.2-003", "PO-D-06.1-002"}

GOOD_TABLE = """
```markdown
| Duty | Objectives | Disposition | Scale fact | Warrant |
|---|---|---|---|---|
| Review access rights periodically | `SO-D-05.1-001`, `PO-D-05.2-003` | ORG | — | duty exists at any size |
| Approve processor contracts | `PO-D-06.1-002` | SCALE | 8 employees, hosted managed cloud | the provider holds the contracts |
```
"""


def _parse(answer: str) -> list[dict]:
    return p3o.parse_duty_proposals(answer, ORG_IDS)


def test_a_well_formed_partition_parses() -> None:
    proposals = _parse(GOOD_TABLE)
    assert len(proposals) == 2
    assert proposals[0]["objectives"] == ["SO-D-05.1-001", "PO-D-05.2-003"]
    assert proposals[1]["disposition"] == "SCALE"
    assert "8 employees" in proposals[1]["scale_fact"]


def test_a_dropped_objective_is_not_a_partition() -> None:
    dropped = GOOD_TABLE.replace(", `PO-D-05.2-003`", "")
    try:
        _parse(dropped)
    except ValueError as e:
        assert "not clustered" in str(e) and "PO-D-05.2-003" in str(e)
    else:
        raise AssertionError("a dropped objective must fail the partition check")


def test_an_invented_or_duplicated_id_raises() -> None:
    invented = GOOD_TABLE.replace("`PO-D-06.1-002`", "`PO-D-06.1-999`")
    try:
        _parse(invented)
    except ValueError as e:
        assert "not routed organizational" in str(e)
    else:
        raise AssertionError("an invented id must raise")
    duplicated = GOOD_TABLE.replace(
        "| Approve processor contracts | `PO-D-06.1-002` |",
        "| Approve processor contracts | `PO-D-06.1-002`, `SO-D-05.1-001` |")
    try:
        _parse(duplicated)
    except ValueError as e:
        assert "more than one duty" in str(e)
    else:
        raise AssertionError("a duplicated assignment must raise")


def test_scale_without_a_company_fact_is_a_preference_and_fails() -> None:
    no_fact = GOOD_TABLE.replace("8 employees, hosted managed cloud", "best practice")
    try:
        _parse(no_fact)
    except ValueError as e:
        assert "SCALE" in str(e) and "scale fact" in str(e)
    else:
        raise AssertionError("SCALE without a fact must raise")


def test_human_overrides_win_and_validate() -> None:
    proposals = _parse(GOOD_TABLE)
    overridden = p3o.apply_duty_overrides(proposals, {"Approve processor contracts": "ORG"})
    assert overridden[1]["disposition"] == "ORG"
    assert overridden[1]["overridden_by_human"] is True
    assert overridden[0]["disposition"] == "ORG" and "overridden_by_human" not in overridden[0]
    try:
        p3o.apply_duty_overrides(proposals, {"No such duty": "ORG"})
    except ValueError as e:
        assert "No such duty" in str(e)
    else:
        raise AssertionError("an override for an unknown duty must raise")
    try:
        p3o.apply_duty_overrides(proposals, {"Approve processor contracts": "MAYBE"})
    except ValueError as e:
        assert "MAYBE" in str(e)
    else:
        raise AssertionError("an override outside the vocabulary must raise")


def test_the_map_feeds_group_duties_and_doc03_joins_by_slug() -> None:
    """The full deterministic chain: proposals → map → duties → Doc03."""
    proposals = p3o.apply_duty_overrides(_parse(GOOD_TABLE), {})
    duties = p3o.group_duties([], p3o.duty_proposal_map(proposals)) if False else None
    # group_duties needs the verdict rows; fabricate them from the partition.
    rows = [{"id": oid, "verdict": p3o.ORG_VERDICT}
            for oid in sorted(ORG_IDS)]
    duties = p3o.group_duties(rows, p3o.duty_proposal_map(proposals))
    assert len(duties) == 2
    for index, duty in enumerate(duties, start=1):
        duty["slug"] = f"duty_{index:02d}"

    cards = [{
        "duty": duties[0]["slug"],
        "Statement (EARS)": "The organization shall review user access rights every quarter.",
        "Requirement Origin": "Access control duty",
        "Fit Criterion": "A dated review record exists.",
        "Verification Method": "INSPECT",
        "Chain": "GDPR Art. 32",
        "Control Anchors": "`GV.RR-02`",
        "Dependencies": "—",
        "Priority": "Must",
    }]
    text = p3o.render_doc03(duties, cards, "TinyTask", ["GDPR"])
    assert "Review access rights periodically" in text
    assert text.count("The organization shall review user access rights every quarter.") == 1
    assert "## §6 Duties whose card call failed" in text
    assert "`duty_02`" in text, "the duty with no card is named, not shifted"


def test_the_clustering_deliverable_renders_both_sides() -> None:
    proposals = _parse(GOOD_TABLE)
    rows = [{"id": oid, "summary": f"objective {oid}"} for oid in sorted(ORG_IDS)]
    text = p3o.render_duty_clustering(proposals, rows)
    assert "## §1 Duty proposals" in text
    assert "Review access rights periodically" in text
    assert "8 employees, hosted managed cloud" in text
    assert "## §2 The rows each duty carries" in text
    assert "objective SO-D-05.1-001" in text


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
