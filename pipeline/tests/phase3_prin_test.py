#!/usr/bin/env python3
"""phase3_prin_test.py — the principle pass must not become a decorative one.

Three defects this pins, all measured on Case_01 run_p2enr_c1:

  * PRINCIPLE_MAPPING was rendered with "Bound 0 / Pending 7" unconditionally —
    the principles never produced a constraint, so transit protection (a
    PRIN-ENG-01 binding in the hand-written case, RN24) had no carrier and
    routed organizational.
  * the coverage matrix was last written by `p3a_map`, before the acceptance
    round; nothing re-rendered it, so the document on disk contradicted the
    round that had already converged.
  * a parser that accepts anything lets a principle constraint name an anchor
    from a different framework version — the exact failure of the first
    `p3a_org` run.

Usage: python3 pipeline/tests/phase3_prin_test.py
Exit 0 iff every guarantee holds. No model, no GPU.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3 import principles_constraints as p3pc  # noqa: E402

ANSWER_TEMPLATE = """```markdown
### `PO_D`

**Constraint (EARS):** Where the system carries personal data across an untrusted
boundary, the system SHALL establish an authenticated and encrypted end-to-end
communication channel.
**Fit criterion:** A connection reaching the backend without an authenticated,
encrypted channel is rejected.
**Risk addressed:** Eavesdropping of customer data in transit.
**Chain anchors:** `PR.DS-02`, `PR.IR-01`
**Proposed carrier:** `NEW`
**Also carries:** `SO-D-01.2-002`
```"""


def answer(objective: str = "PO-D-01.2-001", carrier: str = "new",
           shall: str = "SHALL establish", drop_risk: bool = False) -> str:
    """A fresh copy per test — a module-level constant mutated by one test
    leaks into the next, which is how the SHALL assertion below first failed."""
    out = (ANSWER_TEMPLATE
           .replace("PO_D", objective)
           .replace("`NEW`", f"`{carrier}`")
           .replace("SHALL establish", shall))
    if drop_risk:
        out = "\n".join(l for l in out.splitlines() if "Risk addressed" not in l)
    return out


ROUTED = [
    {"id": "PO-D-01.2-001", "summary": "transit confidentiality",
     "anchors": ["PR.DS-02", "PR.IR-01"]},
    {"id": "SO-D-01.2-002", "summary": "CRA transit twin",
     "anchors": ["PR.DS-02"]},
]


def test_parses_a_well_formed_block() -> None:
    ps = p3pc.parse_principle_proposals(answer(), "PRIN-ENG-01", ROUTED)
    assert len(ps) == 1, ps
    assert ps[0]["principle"] == "PRIN-ENG-01"
    assert ps[0]["carrier"] == "new"
    assert ps[0]["objective"] == "PO-D-01.2-001"
    assert ps[0]["subdomain"] == "D-01.2", "subdomain was truncated to `D` once already"
    assert ps[0]["also_carries"] == ["SO-D-01.2-002"]
    assert not p3pc.check_principle_proposals(ps, ROUTED)


def test_block_id_must_be_a_routed_objective() -> None:
    """A principle constraint discharges routed objectives; it invents no scope."""
    try:
        p3pc.parse_principle_proposals(answer(objective="PO-D-99.9-999"),
                                       "PRIN-ENG-01", ROUTED)
    except ValueError as e:
        assert "routed organizational" in str(e), e
        return
    raise AssertionError("a non-routed block id must fail the parse")


def test_carrier_must_be_new() -> None:
    try:
        p3pc.parse_principle_proposals(answer(carrier="R1.1"), "PRIN-ENG-01", ROUTED)
    except ValueError as e:
        assert "must be `new`" in str(e), e
        return
    raise AssertionError("a borrowed card must fail the parse")


def test_anchor_outside_the_published_union_fails_the_gate() -> None:
    """R2: a principle publishes no anchors, so it may only reuse a routed set."""
    ps = p3pc.parse_principle_proposals(answer(), "PRIN-ENG-01", ROUTED)
    ps[0]["anchors"] = ["PR.IP-1"]          # CSF 1.1 category
    findings = p3pc.check_principle_proposals(ps, ROUTED)
    assert any("published set" in f for f in findings), findings


def test_also_carries_must_be_routed() -> None:
    """Re-routing something the matrix never routed would upgrade a verdict
    the round never saw."""
    ps = p3pc.parse_principle_proposals(answer(), "PRIN-ENG-01", ROUTED)
    ps[0]["also_carries"] = ["PO-D-05.1-001"]
    findings = p3pc.check_principle_proposals(ps, ROUTED)
    assert any("not routed organizational" in f for f in findings), findings


def test_missing_field_fails() -> None:
    try:
        p3pc.parse_principle_proposals(answer(drop_risk=True), "PRIN-ENG-01", ROUTED)
    except ValueError as e:
        assert "missing field" in str(e), e
        return
    raise AssertionError("a missing field must fail the parse")


def test_constraint_without_shall_fails() -> None:
    try:
        p3pc.parse_principle_proposals(answer(shall="establishes"),
                                       "PRIN-ENG-01", ROUTED)
    except ValueError as e:
        assert "SHALL" in str(e), e
        return
    raise AssertionError("a constraint with no SHALL must fail the parse")


def test_reroute_moves_organizational_to_partial_only() -> None:
    rows = [
        {"id": "PO-D-01.2-001", "verdict": "No functional carrier (organizational)"},
        {"id": "SO-D-01.2-002", "verdict": "No functional carrier (organizational)"},
        {"id": "PO-D-03.1-001", "verdict": "Fully covered (anchored)"},
        {"id": "PO-D-05.1-001", "verdict": "Partially covered (functional leg + explicit carve-out)"},
    ]
    accepted = [{"objective": "PO-D-01.2-001", "also_carries": ["SO-D-01.2-002"],
                 "principle": "PRIN-ENG-01", "allocated_card": "R10.1"}]
    out, moved = p3pc.reroute_objectives(rows, accepted)
    assert moved == 2, moved
    by = {r["id"]: r for r in out}
    assert by["PO-D-01.2-001"]["verdict"].startswith("Partially covered")
    assert by["SO-D-01.2-002"]["verdict"].startswith("Partially covered")
    # the two untouched verdicts are untouched, and nothing became Fully covered
    assert by["PO-D-03.1-001"]["verdict"] == "Fully covered (anchored)"
    assert by["PO-D-05.1-001"]["verdict"].startswith("Partially covered")
    assert "PRIN-ENG-01" in by["PO-D-01.2-001"]["discharge"]


def test_reroute_never_creates_a_fully_covered() -> None:
    """M-23: the Fully covered verdict is the round's to give, never code's."""
    rows = [{"id": "PO-D-01.2-001", "verdict": "No functional carrier (organizational)"}]
    accepted = [{"objective": "PO-D-01.2-001", "principle": "PRIN-ENG-01",
                 "allocated_card": "R10.1"}]
    out, _ = p3pc.reroute_objectives(rows, accepted)
    assert "Fully covered" not in out[0]["verdict"]


def test_mapping_reports_real_binding_counts() -> None:
    """The skeleton said "Bound 0 / Pending 7" unconditionally."""
    accepted = [{"objective": "PO-D-01.2-001", "also_carries": ["SO-D-01.2-002"],
                 "principle": "PRIN-ENG-01"}]
    out = p3pc.render_principle_mapping([], accepted)
    assert "Principles bound: 1/7" in out, out[-200:]
    assert "Pending — no constraint proposed" in out


def test_pack_carries_definition_and_published_anchors() -> None:
    """The definition arrives from the phase 2 referential; the anchors from the
    routed objectives. Without either, the call can only invent."""
    prins = p3pc.canonical_principles()
    assert len(prins) == 7
    pack = p3pc.build_principle_pack(prins[0], ROUTED,
                                     [{"id": "R1.1", "name": "Register"}], "company: TinyTask")
    assert "Definition:" in pack
    assert "PR.DS-02" in pack and "PO-D-01.2-001" in pack
    assert prins[0]["source"], "the academic source rides along"


def test_pack_tolerates_a_legacy_card() -> None:
    """A stale card must not kill seven calls.

    The cards on disk carry two shapes: the generated card (`name`) and the
    legacy proposal record `allocate_new_cards` replaced. `KeyError: 'name'` on
    one of them aborted the whole stage before any model call.
    """
    prins = p3pc.canonical_principles()
    legacy = [{"id": "R10.1", "constraint": "Store encrypted at rest",
               "objective": "PO-D-01.1-001"}]
    out = p3pc.build_principle_pack(prins[0], ROUTED, legacy, "company: TinyTask")
    assert "R10.1" in out
    assert "Store encrypted at rest" in out


def test_validate_dispatches_p3a_prin_to_its_own_parser() -> None:
    """`_validate` must not fall through to `parse_p4` for a principle call.

    The principle id travels as `subdomain`, so a step with no branch in the
    dispatch table reaches `if subdomain is not None: parse_p4(...)`, which
    demands a `## §5` section and AG-D-* rows. That is what killed all seven
    calls of job 2023360: the model answered, and the p4 parser rejected the
    answer twice before the stage gave up. Third registration point a new step
    has missed (store_parsed, argparse choices, now this table) — the test is the
    pin, not the fix.
    """
    from aegis_pipeline.phases.phase1.runner import StepRunner  # noqa: PLC0415

    runner = StepRunner.__new__(StepRunner)
    runner._p3a_prin_routed = ROUTED

    parsed = runner._validate("p3a_prin:PRIN-ENG-01", answer(), "PRIN-ENG-01")

    # shape the stage reads back off disk: {"proposals": [...]}
    assert set(parsed) == {"proposals"}, f"unexpected store shape: {sorted(parsed)}"
    assert len(parsed["proposals"]) == 1
    assert parsed["proposals"][0]["principle"] == "PRIN-ENG-01"


def test_validate_p3a_prin_refuses_without_the_routed_set() -> None:
    """A principle call with no routed set must fail loudly, not parse blind.

    Without this the parser would accept any block id the model invents, which
    is exactly the R2 breach the `routed` argument exists to stop.
    """
    from aegis_pipeline.phases.phase1.runner import StepRunner  # noqa: PLC0415

    runner = StepRunner.__new__(StepRunner)
    runner._p3a_prin_routed = []
    try:
        runner._validate("p3a_prin:PRIN-ENG-01", "```markdown\n```", "PRIN-ENG-01")
    except ValueError as e:
        assert "routed" in str(e).lower(), f"unhelpful error: {e}"
    else:
        raise AssertionError("an empty routed set must raise, not parse blind")


def test_one_objective_two_constraints_are_two_verdicts() -> None:
    """A principle constraint and an objective-driven card need separate verdicts.

    `SO-D-07.2-001` carries both in the live run. Keyed by objective alone, one
    "Accept" governed two different constraints — the researcher could neither
    keep the card and drop the principle constraint nor the reverse.
    """
    from aegis_pipeline.phases.phase3 import proposals as p3p  # noqa: PLC0415

    obj = {"objective": "SO-D-07.2-001", "constraint": "objective-driven card"}
    prin = {"objective": "SO-D-07.2-001", "constraint": "PRIN-ENG-02 constraint",
            "principle": "PRIN-ENG-02"}
    state = p3p.apply_round_verdicts([obj, prin],
                                     {"SO-D-07.2-001": "Accept", "PRIN-ENG-02": "Reject"})
    assert [p["constraint"] for p in state["accepted"]] == ["objective-driven card"]
    assert [p["constraint"] for p in state["rejected"]] == ["PRIN-ENG-02 constraint"]
    assert state["converged"], "both keys have verdicts — the round is closed"

    partial = p3p.apply_round_verdicts([obj, prin], {"SO-D-07.2-001": "Accept"})
    assert not partial["converged"]
    assert partial["open"] == ["PRIN-ENG-02"], partial["open"]


def test_principle_round_key_handles_a_proposal_without_a_principle() -> None:
    """An objective-driven proposal has no `principle` key and must not KeyError."""
    from aegis_pipeline.phases.phase3 import proposals as p3p  # noqa: PLC0415

    assert p3p.round_key({"objective": "PO-D-01.2-001"}) == "PO-D-01.2-001"
    assert p3p.round_key({"objective": "PO-D-01.2-001", "principle": "PRIN-ENG-01"}) == "PRIN-ENG-01"


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
    print(f"\n{'FAIL' if failures else 'OK'} — {failures} failure(s)")
    sys.exit(1 if failures else 0)
