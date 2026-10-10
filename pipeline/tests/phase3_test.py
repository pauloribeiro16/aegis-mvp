#!/usr/bin/env python3
"""phase3_test.py — the coverage skeleton's guarantees may not drift.

`pipeline/src/phase3.py` turns a Phase 2 deliverable into `OBJECTIVE_MAPPING.md`
and `PRINCIPLE_MAPPING.md` with every row present and every judgement column
unset, without a model. That is worth having only if the guarantees it buys are
real, which is what these assertions check.

The guarantees, and why each is asserted rather than assumed:

  * **Exhaustiveness.** G1 asks for exhaustive mapping with zero silent
    objectives. When the rows are generated the check becomes a set comparison,
    and that only helps if a dropped row actually fails. `test_dropped_row_fails`
    removes one and requires the gate to fire.
  * **Anchors resolve.** The anchor cell is Phase 2's ninth column — the same
    surface `check_traceability.py` T6 reads. A skeleton that carries an
    unresolvable anchor is worse than one that carries none, because it looks
    anchored.
  * **The verdict column is a pure enum.** R10b invariant 2 requires a
    categorical field to be a mutually exclusive enum; the skeleton emits the
    five ADR-007 D4 verdicts and nothing else, and never a hybrid
    `enum: <explanation>`.
  * **The reconstruction claim stays unclaimed.** ADR-007 D2 cannot be executed
    on template Verification Criteria, and the matrix says `anchored` rather
    than `discharge-verified`. A test pins the wording so a later change cannot
    quietly upgrade the claim.

These assertions read only committed files and need no model and no GPU.

Usage: python3 pipeline/tests/phase3_test.py
Exit 0 iff every guarantee holds.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

import phase3  # noqa: E402
import phase3_schemas as S  # noqa: E402

CASES = [
    "Case_01_TinyTask_SaaS",
    "Case_02_SecureBorder_Solutions",
    "Case_03_OmniBank",
]


def _source(case: str) -> Path:
    return REPO / "cases" / case / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md"


def _rows(case: str) -> tuple[list[dict], list[dict]]:
    objs = phase3.load_objectives(_source(case))
    return phase3.build(objs), objs


def test_every_objective_gets_exactly_one_row() -> None:
    """62 / 100 / 134 — the count is the Phase 2 count, not a derived one."""
    expected = {"Case_01_TinyTask_SaaS": 62,
                "Case_02_SecureBorder_Solutions": 100,
                "Case_03_OmniBank": 134}
    for case, n in expected.items():
        rows, objs = _rows(case)
        assert len(objs) == n, f"{case}: parsed {len(objs)} objectives, expected {n}"
        assert len(rows) == n, f"{case}: built {len(rows)} rows, expected {n}"
        assert not phase3.check(rows, objs), f"{case}: gate fired on a clean build"


def test_dropped_row_fails() -> None:
    """The exhaustiveness guarantee only helps if a drop is loud."""
    rows, objs = _rows("Case_01_TinyTask_SaaS")
    assert not phase3.check(rows, objs), "clean build must be silent"
    dropped = rows[:-1]
    findings = phase3.check(dropped, objs)
    assert findings, "a dropped objective must fail the gate"
    assert any("drops" in f for f in findings), findings
    assert objs[-1]["id"] in " ".join(findings), findings


def test_invented_and_repeated_rows_fail() -> None:
    rows, objs = _rows("Case_01_TinyTask_SaaS")
    invented = list(rows) + [dict(rows[0], id="PO-D-99.9-999")]
    assert any("invents" in f for f in phase3.check(invented, objs))
    repeated = list(rows) + [dict(rows[0])]
    assert any("repeats" in f for f in phase3.check(repeated, objs))


def test_anchors_resolve() -> None:
    """R2b: every anchor the skeleton carries exists under `baseline/CONTROLS/`.

    Anchors are checked for resolution, not for presence. A contractual
    obligation carries none by construction — measured, every unanchored
    objective across the three cases is a PROCESS-lane contract or procurement
    duty — and the skeleton does not yet know the verdict that would exempt it.
    """
    for case in CASES:
        rows, _ = _rows(case)
        for r in rows:
            for a in r["anchors"]:
                hits = list((REPO / "baseline" / "CONTROLS").glob(f"**/{a}.json"))
                assert hits, f"{case} {r['id']}: anchor {a} resolves to no file"


def test_anchor_gating_is_post_verdict() -> None:
    """The skeleton does not gate anchors; the verdict stage does.

    Case 01's Phase 2 deliverable has two unanchored objectives, both Art. 28(3)
    contract duties verified by `INSPECT`. Gating presence in the skeleton made
    a clean build fail — the test caught a rule that was wrong, not a document
    that was.
    """
    rows, objs = _rows("Case_01_TinyTask_SaaS")
    unanchored = [r["id"] for r in rows if not r["anchors"]]
    assert unanchored == ["SO-D-06.3-001", "SO-D-06.3-002"], unanchored
    assert not phase3.check(rows, objs), "the skeleton must not gate anchor presence"
    assert phase3.check_anchors(rows) == [], "no row claims a carrier yet, so nothing fires"

    claiming = [dict(r, verdict=S.VERDICTS[0]) for r in rows]
    firing = phase3.check_anchors(claiming)
    assert len(firing) == len(unanchored), firing

    exempt = [dict(r, verdict=S.ORGANIZATIONAL if not r["anchors"] else r["verdict"])
              for r in rows]
    assert phase3.check_anchors(exempt) == [], "an organizational verdict is exempt"


def test_unanchored_rows_are_dominated_by_process_obligations() -> None:
    """Pin the shape of the exemption without over-claiming it.

    Measured: Case 01 has 2 unanchored objectives (both `INSPECT` contract
    duties), Case 02 has 14 (8 `INSPECT`, 6 `TEST`), Case 03 has 8 (all
    `INSPECT`). So "unanchored means process" is true for Case 01 and Case 03
    and only mostly true for Case 02 — which is precisely why the gate is
    post-verdict rather than a rule about the anchor column.
    """
    measured = {"Case_01_TinyTask_SaaS": 2, "Case_02_SecureBorder_Solutions": 14,
                "Case_03_OmniBank": 8}
    for case, n in measured.items():
        rows, _ = _rows(case)
        unanchored = [r for r in rows if not r["anchors"]]
        assert len(unanchored) == n, f"{case}: {len(unanchored)} unanchored, expected {n}"
        inspect = sum(1 for r in unanchored if "INSPECT" in r["method"])
        assert inspect >= len(unanchored) * 0.5, \
            f"{case}: only {inspect}/{len(unanchored)} unanchored are INSPECT"


def test_verdict_column_is_a_pure_enum() -> None:
    """R10b invariant 2 — no `enum: <explanation>` hybrids."""
    assert len(S.VERDICTS) == 5
    assert len(set(S.VERDICTS)) == len(S.VERDICTS)
    for v in S.VERDICTS:
        assert v == v.strip()
        assert ":" not in v, f"hybrid verdict field: {v!r}"
    rows, _ = _rows("Case_01_TinyTask_SaaS")
    for r in rows:
        assert r["verdict"] in (S.UNSET,) + S.VERDICTS, r["verdict"]


def test_skeleton_leaves_judgement_columns_unset() -> None:
    """A skeleton that guesses is worse than one that is blank."""
    rows, _ = _rows("Case_01_TinyTask_SaaS")
    for r in rows:
        for col in ("carrier", "skill", "verdict", "discharge", "action"):
            assert r[col] == S.UNSET, f"{r['id']}: {col} is {r[col]!r}, not unset"


def test_reconstruction_claim_stays_unclaimed() -> None:
    """ADR-007 D2 is not executable on template criteria; the wording must not drift."""
    rows, _ = _rows("Case_01_TinyTask_SaaS")
    templated = [r for r in rows if r["criterion_is_template"]]
    assert len(templated) == len(rows), (
        "every Case 01 Verification Criterion is the generic template — if this "
        "assertion now fails, the Phase 2 data improved and the ADR-007 D2 "
        "reconstruction test may have become executable after all")
    out = phase3.render_matrix(
        rows,
        {"D-01": [r for r in rows if r["domain"] == "D-01"]},
        {"D-01": "Data Protection"},
    )
    assert not [v for v in S.VERDICTS if "discharge" in v], S.VERDICTS
    assert "| Fully covered (anchored) | 0 |" in out
    assert "does not claim a reconstruction" in out


def test_template_ratio_is_measured_not_assumed() -> None:
    """The template is the majority everywhere, not universal — pin the real numbers."""
    ratios = {}
    for case in CASES:
        rows, _ = _rows(case)
        ratios[case] = sum(1 for r in rows if r["criterion_is_template"]) / len(rows)
    assert ratios["Case_01_TinyTask_SaaS"] == 1.0
    # Case 02 and Case 03 carry bespoke criteria for part of their objectives;
    # the reconstruction is still not executable, but not because every row is
    # a template. Recorded so the distinction is not flattened later.
    assert 0.4 < ratios["Case_02_SecureBorder_Solutions"] < 0.7, ratios
    assert 0.4 < ratios["Case_03_OmniBank"] < 0.6, ratios


def test_domain_titles_come_from_the_corpus() -> None:
    names = phase3.domain_names_from(REPO / "baseline" / "domains" / "index.md")
    assert len(names) == 10, names
    assert names["D-03"] == "Access Control", names


def test_principle_skeleton_lists_all_seven() -> None:
    out = phase3.render_principles()
    for i in range(1, 8):
        assert f"PRIN-ENG-0{i}" in out
    assert "7/7" in out


def test_end_to_end_cli() -> None:
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run(
            [sys.executable, str(REPO / "pipeline" / "src" / "phase3.py"),
             "--case", CASES[0], "--out", td],
            capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        matrix = (Path(td) / "OBJECTIVE_MAPPING.md").read_text(encoding="utf-8")
        rows = [l for l in matrix.splitlines() if l.startswith("| `")]
        assert len(rows) == 62, len(rows)
        assert "| **Total objectives** | **62** |" in matrix
        assert (Path(td) / "PRINCIPLE_MAPPING.md").is_file()


def test_id_helpers() -> None:
    assert S.subdomain_of("SO-D-03.2-001") == "D-03.2"
    assert S.domain_of("D-03.2") == "D-03"
    assert S.org_id("D-04.1", 1) == "ORG-D-04.1-001"
    assert S.anchor_set("`PR.DS-01, PR.DS-10`") == ["PR.DS-01", "PR.DS-10"]
    assert S.anchor_set(S.UNSET) == []
    for bad in ("PO-D-3.2-001", "R1.1", "", "ORG-D-03.2-001"):
        try:
            S.subdomain_of(bad)
        except ValueError:
            continue
        raise AssertionError(f"{bad!r} should not parse as an objective id")



# ---------------------------------------------------------------- verdicts

def _subdomain_rows(case: str, sd: str) -> tuple[list[dict], list[dict], list[str]]:
    objs = phase3.load_objectives(_source(case))
    rows = phase3.build(objs)
    sub = [r for r in rows if r["subdomain"] == sd]
    cards = phase3.load_v0_cards(
        REPO / "cases" / case / "03_PHASE3_SPEC" / "part1_security_privacy"
        / "v0_functional_baseline" / "Doc01_Requirements_Elicitation_and_PUC.md")
    return sub, [o for o in objs if o["subdomain"] == sd], [c["id"] for c in cards]


def _answer(rows: list[dict], **over) -> str:
    """A well-formed answer for these rows, so each gate can be broken singly."""
    out = ["| Objective | Summary | Functional carrier | Skill | State | VC discharge | Action |",
           "|---|---|---|---|---|---|---|"]
    for r in rows:
        v = over.get(r["id"], {
            "carrier": "—", "skill": "—",
            "verdict": S.ORGANIZATIONAL,
            "discharge": "recorded decision on the ticket; the founders own it",
        })
        out.append(f"| `{r['id']}` | {r['summary'][:40]} | {v['carrier']} | {v['skill']} "
                   f"| **{v['verdict']}** | {v['discharge']} | — |")
    return "\n".join(out)


def test_parse_accepts_a_well_formed_table() -> None:
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    parsed = phase3.parse_verdicts(_answer(rows))
    assert [p["id"] for p in parsed] == [r["id"] for r in rows]
    assert not phase3.check_verdicts(phase3.apply_verdicts(rows, parsed), objs, pool)


def test_a_dropped_row_is_a_gate_finding() -> None:
    """Same split as the carrier: the parser has no view of what is expected."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    dropped = rows[-1]["id"]
    parsed = phase3.parse_verdicts(_answer(rows[:-1]))
    merged = phase3.apply_verdicts(rows, parsed)
    assert merged[-1]["verdict"] == S.UNSET, "the dropped row must stay unset, not inherited"
    findings = phase3.check_verdicts(merged, objs, pool)
    assert any(dropped in f for f in findings), findings


def test_a_repeated_row_is_a_parse_error() -> None:
    """Two rows for one objective is a contract breach, not a judgement."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    answer = _answer(rows) + "\n| `" + rows[0]["id"] + "` | dup | — | — | **" + S.ORGANIZATIONAL + "** | dup | — |"
    try:
        phase3.parse_verdicts(answer)
    except ValueError as e:
        assert "repeats" in str(e), e
        return
    raise AssertionError("a repeated objective must fail the parse")


def test_unknown_carrier_is_a_gate_not_a_parse_error() -> None:
    """Structure and substance fail in different places, deliberately.

    The parser cannot know the carrier pool — it runs inside `_call`, which has
    no view of the V0 cards. The gate can, so the carrier check lives there and a
    fabricated card is reported rather than raised.
    """
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    bad = _answer(rows, **{rows[0]["id"]: {
        "carrier": "`R9.9`", "skill": "V",
        "verdict": S.VERDICTS[0], "discharge": "carried leg"}})
    parsed = phase3.parse_verdicts(bad)
    findings = phase3.check_verdicts(phase3.apply_verdicts(rows, parsed), objs, pool)
    assert any("not in the candidate pool" in f for f in findings), findings


def test_parse_rejects_a_verdict_outside_the_vocabulary() -> None:
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    bad = _answer(rows, **{rows[0]["id"]: {
        "carrier": "—", "skill": "—", "verdict": "mostly covered",
        "discharge": "partly"}})
    try:
        phase3.parse_verdicts(bad)
    except ValueError as e:
        assert "vocabulary" in str(e), e
        return
    raise AssertionError("a verdict outside the vocabulary must fail the parse")


def test_fully_covered_without_a_discharge_fails() -> None:
    """The absence this stage exists to prevent, and the one that reads as coverage."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    bad = _answer(rows, **{rows[0]["id"]: {
        "carrier": "`R2.2`", "skill": "LP", "verdict": S.VERDICTS[0], "discharge": "—"}})
    findings = phase3.check_verdicts(phase3.apply_verdicts(rows, phase3.parse_verdicts(bad)), objs, pool)
    assert any("Fully covered with no discharge" in f for f in findings), findings


def test_organizational_without_naming_the_obligation_fails() -> None:
    """A routing decision with no content routes the objective into nowhere."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-09.4")
    bad = _answer(rows, **{rows[0]["id"]: {
        "carrier": "—", "skill": "—", "verdict": S.ORGANIZATIONAL, "discharge": "—"}})
    findings = phase3.check_verdicts(phase3.apply_verdicts(rows, phase3.parse_verdicts(bad)), objs, pool)
    assert any("without naming the obligation" in f for f in findings), findings


def test_t6_rejects_an_anchor_outside_the_published_set() -> None:
    rows, objs, _ = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    objs = [dict(o, anchors=["PR.AA-05"]) for o in objs]
    skeleton = phase3.build(objs)
    skeleton[0]["verdict"] = S.VERDICTS[0]
    skeleton[0]["anchors_used"] = ["PR.AA-05", "GV.RR-02"]
    findings = phase3.check_verdicts(skeleton, objs, _)
    assert any("outside the published set" in f for f in findings), findings


def test_pack_carries_every_row_and_the_whole_pool() -> None:
    rows, _, _ = _subdomain_rows("Case_01_TinyTask_SaaS", "D-01.1")
    cards = phase3.load_v0_cards(
        REPO / "cases" / "Case_01_TinyTask_SaaS" / "03_PHASE3_SPEC" / "part1_security_privacy"
        / "v0_functional_baseline" / "Doc01_Requirements_Elicitation_and_PUC.md")
    pack = phase3.build_verdict_pack(rows, cards)
    for r in rows:
        assert f"`{r['id']}`" in pack, r["id"]
    for c in cards:
        assert f"`{c['id']}`" in pack, c["id"]
    for v in S.VERDICTS:
        assert v in pack, v


def test_pack_names_the_published_anchors_so_none_can_be_invented() -> None:
    rows, _, _ = _subdomain_rows("Case_01_TinyTask_SaaS", "D-01.2")
    pack = phase3.build_verdict_pack(rows, [])
    for r in rows:
        for a in r["anchors"]:
            assert a in pack, a


def test_v0_cards_are_read_not_written() -> None:
    """V0 is a human input; this module opens it and never writes it."""
    v0 = REPO / "cases" / "Case_01_TinyTask_SaaS" / "03_PHASE3_SPEC" / "part1_security_privacy" / "v0_functional_baseline"
    before = {p: p.stat().st_mtime_ns for p in v0.rglob("*.md")}
    cards = phase3.load_v0_cards(v0 / "Doc01_Requirements_Elicitation_and_PUC.md")
    assert cards
    after = {p: p.stat().st_mtime_ns for p in v0.rglob("*.md")}
    assert before == after, "the V0 folder was modified"


def test_merge_then_render_totals_sum() -> None:
    """The whole path a run takes: skeleton -> verdicts -> merged matrix."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    parsed = phase3.parse_verdicts(_answer(rows))
    merged = phase3.apply_verdicts(rows, parsed)
    assert not phase3.check_verdicts(merged, objs, pool)
    assert not phase3.check_anchors(merged), phase3.check_anchors(merged)

    by_domain = {"D-03": merged}
    out = phase3.render_matrix(merged, by_domain, {"D-03": "Access Control"})
    assert out.count("| `") == len(merged)
    # every row carries its verdict into the rendered totals
    total = sum(int(l.split("|")[2].strip()) for l in out.splitlines()
                if l.startswith("| ") and l.split("|")[1].strip() in S.VERDICTS)
    assert total == len(merged), f"totals say {total}, rows are {len(merged)}"
    assert "| **Unset** | **0** |" in out, out.splitlines()[-8:]


def test_unfilled_subdomain_stays_unset_not_half_filled() -> None:
    """A sub-domain the model never answered must read as unset, not as decided."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    partial = phase3.apply_verdicts(rows, [])
    assert all(r["verdict"] == S.UNSET for r in partial)
    findings = phase3.check_verdicts(partial, objs, pool)
    assert len(findings) == len(rows), findings


def test_store_parsed_routes_p3a_map_above_the_p4_catch_all() -> None:
    """A named step that carries a sub-domain is swallowed by the p4 branch.

    `store_parsed` ends in `elif subdomain is not None:` — the p4 store. Any
    step that passes a sub-domain lands there unless it is matched ABOVE that
    line, and p4 reads `parsed["md"]`, which a verdict table does not have. This
    cost one cluster run: every sub-domain that parsed cleanly still failed with
    `KeyError: 'md'`, and the trace said `ok` because the parser had passed —
    the failure was in the store, after the record was already written.
    """
    import steps
    with tempfile.TemporaryDirectory() as td:
        run = Path(td)
        payload = {"verdicts": [{"id": "SO-D-01.1-001", "verdict": S.ORGANIZATIONAL,
                                 "discharge": "d", "carrier": "—", "skill": "—",
                                 "summary": "s", "action": "—",
                                 "carriers_cited": []}]}
        steps.store_parsed(run, "p3a_map:D-01.1", "D-01.1", payload)
        out = run / "steps" / "phase3a_map" / "D-01_1.json"
        assert out.is_file(), "the verdict slice was not stored"
        assert json.loads(out.read_text())["verdicts"][0]["id"] == "SO-D-01.1-001"


def test_verdict_cell_accepts_backticks_or_bold() -> None:
    """The model used both in one batch. Only the wording is compared."""
    rows, objs, pool = _subdomain_rows("Case_01_TinyTask_SaaS", "D-03.2")
    for marks in ("**%s**", "`%s`", "**`%s`**", "%s"):
        answer = _answer(rows, **{rows[0]["id"]: {
            "carrier": "—", "skill": "—",
            "verdict": marks % S.ORGANIZATIONAL,
            "discharge": "named organizational obligation"}})
        parsed = phase3.parse_verdicts(answer)
        assert parsed[0]["verdict"] == S.ORGANIZATIONAL, marks


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


# ===========================================================================
# Waves 2/4/5/6 — PREREG_P3_01 (frozen 2026-10-10, before any GPU time)
# ===========================================================================

def _wave_modules():
    from aegis_pipeline.phases.phase3 import cards, org, proposals, weave
    return cards, org, proposals, weave


_AUDIT = REPO / "cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/analysis_v0_to_v1/PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md"


def _org_rows_for_grouping() -> list[dict]:
    """32 organizational rows in the measured Case 01 shape."""
    objs = phase3.load_objectives(_source("Case_01_TinyTask_SaaS"))
    rows = phase3.build(objs)
    audit_rows = [
        {"id": r["id"], "verdict": S.ORGANIZATIONAL,
         "subdomain": r["subdomain"], "domain": r["domain"],
         "discharge": "named organizational obligation"}
        for r in rows
    ]
    # the audit covers exactly the 32 rows the matrix verdicts organizational
    assert len(audit_rows) == 32, f"expected the measured 32 org rows, got {len(audit_rows)}"
    return audit_rows


def test_duty_grouping_reproduces_the_measured_32_to_16_shape() -> None:
    """H3 (PREREG_P3_01): the audited duty map collapses 32 rows to 16 duties."""
    _, org, _, _ = _wave_modules()
    duty_map = org.parse_duty_audit(_AUDIT)
    assert len(duty_map) == 32, f"audit parses {len(duty_map)} assignments, expected 32"
    duties = org.group_duties(_org_rows_for_grouping(), duty_map)
    assert len(duties) == 16, f"expected the measured 16 duties, got {len(duties)}"
    dispositions = org.count_dispositions(duties)
    assert dispositions == {"ORG": 17, "SCALE": 13, "CARRIED": 2}, dispositions


def test_duty_grouping_refuses_an_unmapped_row() -> None:
    """A row the audit does not know about is a finding, never a silent drop."""
    _, org, _, _ = _wave_modules()
    duty_map = org.parse_duty_audit(_AUDIT)
    rows = _org_rows_for_grouping()
    del duty_map[rows[0]["id"]]
    try:
        org.group_duties(rows, duty_map)
    except ValueError as e:
        assert rows[0]["id"] in str(e)
    else:
        raise AssertionError("unmapped organizational row did not fail the grouping")


def test_org_card_parse_accepts_well_formed_and_rejects_defects() -> None:
    _, org, _, _ = _wave_modules()
    good = "\n".join([
        "```markdown",
        "**Statement (EARS):** Where the organization detects a breach of stored billing state, the organization shall record the detection and route it to a named owner for assessment.",
        "**Requirement Origin:** GDPR Art. 33(1); proportionality audit warrant",
        "**Fit Criterion:** A detection with no owner record does not close.",
        "**Verification Method:** INSPECT",
        "**Chain:** GDPR Art. 33(1) → SO-D-04.1-001 → DE.CM-9",
        "**Control Anchors:** `DE.CM-9`, `GV.RR-2`",
        "**Dependencies:** Stakeholders: founders",
        "**Priority:** Must",
        "```",
    ])
    parsed = org.parse_org_card(good, duty="duty_01")
    assert parsed["Verification Method"] == "INSPECT"
    assert parsed["_anchor_list"] == ["DE.CM-9", "GV.RR-2"]
    # non-EARS
    bad = good.replace("the organization shall record", "the organization records")
    try:
        org.parse_org_card(bad, duty="duty_01")
    except ValueError as e:
        assert "EARS" in str(e)
    else:
        raise AssertionError("non-EARS statement accepted")
    # unknown method
    try:
        org.parse_org_card(good.replace("INSPECT", "SOMETIMES"), duty="duty_01")
    except ValueError as e:
        assert "Verification Method" in str(e)
    else:
        raise AssertionError("unknown verification method accepted")


def test_inventory_parse_roundtrip_and_rejects() -> None:
    cards, _, _, _ = _wave_modules()
    good = "\n".join([
        "```markdown",
        "| Card | Name | Business basis |",
        "|---|---|---|",
        "| R1.1 | Register and authenticate user accounts | Customer accounts are core |",
        "| R2.1 | Track billable tasks | The intake's core workflow |",
        "| R3.1 | Manage team workspaces | Team plan tier |",
        "| R4.1 | Export task reports | Customer ask |",
        "| R5.1 | Attach files to tasks | Stated need |",
        "```",
    ])
    parsed = cards.parse_inventory(good)
    assert [c["id"] for c in parsed["cards"]] == ["R1.1", "R2.1", "R3.1", "R4.1", "R5.1"]
    # duplicate id fails
    dup = good.replace("R5.1 | Export", "R1.1 | Export")
    try:
        cards.parse_inventory(dup)
    except ValueError as e:
        assert "more than once" in str(e)
    else:
        raise AssertionError("duplicate card id accepted")
    # bad id format fails
    try:
        cards.parse_inventory(good.replace("R3.1", "card-three"))
    except ValueError as e:
        assert "R<n>.<m>" in str(e)
    else:
        raise AssertionError("malformed card id accepted")


def test_card_parse_rejects_nominalization_and_technology() -> None:
    cards, _, _, _ = _wave_modules()
    base = "\n".join([
        "```markdown",
        "#### Card R1.1",
        "",
        "| # | Row | Content |",
        "|---|---|---|",
        "| 1 | ID | R1.1 — Manage user accounts |",
        "| 2 | Description | The system must allow users to register and authenticate. |",
        "| 3 | Requirement Origin | Founders Business Case |",
        "| 4 | Interfaces | Registration form; login form |",
        "| 5 | Dependencies | Stakeholders: customers; Data Sources: —; Extraction Periodicity: on demand; Information Systems / Databases: ; Preceding Requirements: |",
        "| 6 | Identified Problems | — |",
        "| 7 | Priority | Must |",
        "",
        "#### PUC",
        "",
        "| PUC ID | Business Trigger | Primary Actor | System Operational Boundary | Deliverables & Outputs |",
        "|---|---|---|---|---|",
        "| PUC 1.1 | Visitor signs up | Visitor | Provision account | Created account |",
        "",
        "#### Use case {U.C. 1.1}",
        "",
        "**Traceability:** Requirement `R1.1` | PUC `1.1`",
        "**Primary Actor:** Visitor",
        "**Preconditions:** The visitor has an email address.",
        "**Trigger:** The visitor submits the registration form.",
        "**Main Success Scenario:** 1. The visitor submits the form. 2. The system validates the data. 3. The system creates the account. 4. The system confirms to the visitor.",
        "**Extensions:** 2a. The email is already registered: the system says so.",
        "**Success Guarantees:** The account exists.",
        "**Minimal Guarantees:** No partial account is left.",
        "```",
    ])
    parsed = cards.parse_card(base)
    assert parsed["card"]["id"] == "R1.1"
    # nominalization (R13 anti-pattern 7)
    try:
        cards.parse_card(base.replace("Manage user accounts", "User account management"))
    except ValueError as e:
        assert "nominalization" in str(e)
    else:
        raise AssertionError("nominalized name accepted")
    # technology leakage (R5) — checked by check_card_quality
    try:
        cards.check_card_quality(cards.parse_card(base.replace("Registration form; login form", "Registration form; PostgreSQL database")))
    except ValueError as e:
        assert "technology" in str(e).lower()
    else:
        raise AssertionError("technology vocabulary accepted")
    # priority enum
    try:
        cards.parse_card(base.replace("| 7 | Priority | Must |", "| 7 | Priority | Maybe |"))
    except ValueError as e:
        assert "Priority" in str(e)
    else:
        raise AssertionError("non-MoSCoW priority accepted")
    # scenario too short
    try:
        cards.parse_card(base.replace("2. The system validates the data. 3. The system creates the account. 4. The system confirms to the visitor.", "2. The system creates the account."))
    except ValueError as e:
        assert "Main Success Scenario" in str(e)
    else:
        raise AssertionError("two-step scenario accepted")


def test_proposal_targets_come_from_the_actions_not_a_new_judgement() -> None:
    _, _, proposals, _ = _wave_modules()
    rows = [
        {"id": "SO-D-01.1-001", "subdomain": "D-01.1", "action": "Propose for Round 2: assign to security", "discharge": "x"},
        {"id": "PO-D-01.2-001", "subdomain": "D-01.2", "action": "—", "discharge": "pending proposal: encryption leg"},
        {"id": "SO-D-01.3-001", "subdomain": "D-01.3", "action": "—", "discharge": "fully routed to the organizational lane"},
    ]
    targets = proposals.select_proposal_targets(rows)
    assert [t["id"] for t in targets] == ["SO-D-01.1-001", "PO-D-01.2-001"]


def test_proposal_parse_and_published_anchor_gate() -> None:
    _, _, proposals, _ = _wave_modules()
    targets = [{"id": "SO-D-01.1-001", "subdomain": "D-01.1"}]
    good = "\n".join([
        "```markdown",
        "### SO-D-01.1-001",
        "",
        "**Constraint (EARS):** Where the system stores personal data at rest, the system shall encrypt the stored data.",
        "**Fit criterion:** A raw dump of the store is unreadable without the key.",
        "**Risk addressed:** Personal data readable by an attacker with disk access.",
        "**Chain anchors:** `PR.DS-1`, `PR.AC-1`",
        "**Proposed carrier:** new",
        "```",
    ])
    parsed = proposals.parse_proposals(good, targets)
    assert parsed["proposals"][0]["objective"] == "SO-D-01.1-001"
    # invented target rejected
    try:
        proposals.parse_proposals(good, [{"id": "SO-D-09.9-001", "subdomain": "D-09.9"}])
    except ValueError as e:
        assert "no block" in str(e)
    else:
        raise AssertionError("proposal for a non-target accepted")
    # non-EARS
    try:
        proposals.parse_proposals(good.replace("the system shall encrypt", "the system encrypts"), targets)
    except ValueError as e:
        assert "EARS" in str(e)
    else:
        raise AssertionError("non-EARS constraint accepted")
    # T6: anchor outside the published set
    rows = [{"id": "SO-D-01.1-001"}]
    objectives = [{"id": "SO-D-01.1-001", "anchors": "`PR.AC-1`"}]
    findings = proposals.check_proposals(parsed["proposals"], rows, objectives)
    assert any("PR.DS-1" in f and "T6" not in f or "published set" in f for f in findings), findings


def test_round_verdicts_split_and_two_states() -> None:
    _, _, proposals, _ = _wave_modules()
    props = [
        {"objective": "SO-D-01.1-001", "subdomain": "D-01.1", "constraint": "c", "fit_criterion": "f", "risk": "r", "anchors": ["PR.AC-1"], "carrier": "new"},
        {"objective": "SO-D-01.2-001", "subdomain": "D-01.2", "constraint": "c", "fit_criterion": "f", "risk": "r", "anchors": ["PR.AC-1"], "carrier": "new"},
    ]
    state = proposals.apply_round_verdicts(props, {"SO-D-01.1-001": "Accept", "SO-D-01.2-001": "Reject"})
    assert state["converged"] and len(state["accepted"]) == 1 and len(state["rejected"]) == 1
    state_open = proposals.apply_round_verdicts(props, {"SO-D-01.1-001": "Accept"})
    assert not state_open["converged"] and state_open["open"] == ["SO-D-01.2-001"]
    try:
        proposals.apply_round_verdicts(props, {"SO-D-01.1-001": "Sure"})
    except ValueError as e:
        assert "not in" in str(e)
    else:
        raise AssertionError("verdict outside the vocabulary accepted")


def test_exit_gate_is_proposed_without_verdicts_and_concluded_with_them() -> None:
    """H5 (PREREG_P3_01): the gate does not close G2 on a round with open items."""
    import shutil

    _, _, _, weave = _wave_modules()
    case = "Case_01_TinyTask_SaaS"
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = Path(tmp) / "run"
        (run_dir / "steps" / "phase3").mkdir(parents=True)
        (run_dir / "outputs" / "phase2").mkdir(parents=True)
        (run_dir / "steps" / "gates").mkdir(parents=True)
        shutil.copy(_source(case), run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md")
        (run_dir / "manifest.json").write_text(json.dumps({"case_id": case}), encoding="utf-8")
        # two verdicts, one per objective — enough to exercise the machinery
        objs = phase3.load_objectives(run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md")
        sample = objs[:2]
        for obj in sample:
            sd = obj["subdomain"].replace(".", "_")
            (run_dir / "steps" / "phase3" / f"verdicts_{sd}.json").write_text(json.dumps([{
                "id": obj["id"], "verdict": S.ORGANIZATIONAL,
                "carrier": "`—`", "skill": "`—`",
                "discharge": "the named organizational obligation",
                "action": "Propose for Round 2",
            }]), encoding="utf-8")
        # round recorded but not converged → PROPOSED
        (run_dir / "steps" / "phase3" / "round1_state.json").write_text(json.dumps(
            {"accepted": [], "rejected": [], "adjusted": [], "open": [o["id"] for o in sample], "converged": False},
        ), encoding="utf-8")
        (run_dir / "outputs" / "phase3" / "synthesis_rounds").mkdir(parents=True)
        (run_dir / "outputs" / "phase3" / "synthesis_rounds" / "ROUND1_REGISTER.md").write_text("scaffold")
        report = weave.run_gate(run_dir, REPO)
        assert report["state"] == "PROPOSED", report
        assert not report["gates"]["G2"].startswith("CLOSED")
        assert "not concluded" in report["gates"]["G2"] or "no human marker" in report["gates"]["G2"]
        # converged + marker → G2 closes
        (run_dir / "steps" / "phase3" / "round1_state.json").write_text(json.dumps(
            {"accepted": [], "rejected": [{"objective": "x", "risk": "r"}], "adjusted": [], "open": [], "converged": True},
        ), encoding="utf-8")
        (run_dir / "steps" / "gates" / "G-P3-A.approved").write_text("review note", encoding="utf-8")
        report = weave.run_gate(run_dir, REPO)
        assert report["gates"]["G2"].startswith("CLOSED"), report


def test_doc00_is_composed_from_the_run_artifacts() -> None:
    from aegis_pipeline.phases.phase3 import doc00

    card = {
        "id": "R1.1", "name": "Manage user accounts", "description": "d", "origin": "o",
        "interfaces": "i", "dependencies": "dep", "problems": "—", "priority": "Must",
        "puc": {"puc_id": "PUC 1.1", "trigger": "t", "actor": "a", "boundary": "b", "outputs": "o"},
        "usecase": {"uc_id": "{U.C. 1.1}", "Traceability": "R1.1", "Primary Actor": "a",
                     "Preconditions": "p", "Trigger": "t", "Main Success Scenario": "1. x 2. y 3. z",
                     "Extensions": "2a. e", "Success Guarantees": "s", "Minimal Guarantees": "m"},
    }
    doc = doc00.render_doc00(
        "TinyTask", {"sector": "SaaS", "size": "8"}, [card],
        [{"seq": 1, "skill": "TB", "objective": "SO-D-01.1-001", "summary": "s"}],
    )
    assert "| PUC 1.1 |" in doc and "R1.1" in doc
    assert "TZ-1" in doc and "TB" in doc
    assert "8" in doc  # size from the fact sheet
