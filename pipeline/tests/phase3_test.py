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
