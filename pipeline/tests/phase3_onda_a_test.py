#!/usr/bin/env python3
"""phase3_onda_a_test.py — the Wave A repairs hold, and fail when they must.

Every assertion here is a regression against a defect that was either measured
on a real run or found by direct inspection of the Wave A diff:

* S20 — `render_doc03` joined duties to cards positionally; one failed call
  rendered duty N with card N+1's statement. And the first repair attempt
  joined on `d["id"]`, a key duty dicts do not carry (they carry `slug`).
* S5/S6 — `anchors_used` inherited the objective's full published set, so T3
  compared the objective's anchors with themselves and could never find an
  invented one. A silent row must cite nothing, not everything.
* S7/S8 — the sufficiency line carries five verdict buckets; a renderer that
  prints three and a gate that demands identical counts on a GDPR-only case
  are both wrong in different directions.
* A.3 — the V2 Doc01 dropped the `Identified Problems` row and the V2 Doc02
  fabricated a canned use case ("User is authenticated", a 3-step scenario)
  for cards allocated from proposals — invented behaviour in a deliverable (R6).
* A.2 — `--v0-source` makes the baseline choice explicit; `generated` must
  never fall back to the frozen corpus, and `frozen` must ignore a generated
  baseline that happens to sit in the run.
* Export — the deliverable leaves the run only on CONCLUDED, and the exported
  folder is the specification plus the verdict that closed it.

Usage: python3 pipeline/tests/phase3_onda_a_test.py
Exit 0 iff every repair holds.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3 import cards as p3c  # noqa: E402
from aegis_pipeline.phases.phase3 import org as p3o  # noqa: E402
from aegis_pipeline.phases.phase3 import v0_cards as p3v  # noqa: E402
from aegis_pipeline.phases.phase3 import verdicts as p3vd  # noqa: E402
from aegis_pipeline.phases.phase3 import weave as p3w  # noqa: E402

DUTY = {
    "duty": "Review access rights periodically",
    "objectives": ["SO-D-05.1-001"],
    "dispositions": {"ORG": 1},
    "warrants": ["8-person company; quarterly review is proportionate"],
    "subdomain": "D-05.1",
    "slug": "duty_01",
}

ORG_CARD = {
    "duty": "duty_01",
    "Statement (EARS)": "The organization shall review user access rights every quarter.",
    "Requirement Origin": "Access control duty",
    "Fit Criterion": "A dated review record exists for each quarter.",
    "Verification Method": "INSPECT",
    "Chain": "GDPR Art. 32",
    "Control Anchors": "`GV.RR-02`",
    "Dependencies": "—",
    "Priority": "Must",
}

WRONG_DUTY_CARD = dict(ORG_CARD, duty="duty_02",
                       **{"Statement (EARS)": "A different duty's statement that must not leak."})


# ---------------------------------------------------------------------------
# S20 — the duty↔card join
# ---------------------------------------------------------------------------

def test_render_doc03_joins_by_call_slug_not_position() -> None:
    text = p3o.render_doc03([DUTY], [ORG_CARD], "TinyTask", ["GDPR"])
    assert "Review access rights periodically" in text
    assert ORG_CARD["Statement (EARS)"] in text


def test_render_doc03_never_renders_another_dutys_statement() -> None:
    """The positional zip's failure mode: two duties, one card."""
    duty2 = dict(DUTY, duty="Approve processor contracts", slug="duty_02",
                 objectives=["SO-D-05.1-002"], subdomain="D-05.1")
    text = p3o.render_doc03([DUTY, duty2], [ORG_CARD], "TinyTask", ["GDPR"])
    assert "Review access rights periodically" in text
    assert "Approve processor contracts" in text
    # the one card's statement appears exactly once, under its own duty
    assert text.count(ORG_CARD["Statement (EARS)"]) == 1
    assert "A different duty's statement" not in text


def test_render_doc03_names_duties_whose_card_call_failed() -> None:
    duty2 = dict(DUTY, duty="Approve processor contracts", slug="duty_02",
                 objectives=["SO-D-05.1-002"], subdomain="D-05.1")
    text = p3o.render_doc03([DUTY, duty2], [ORG_CARD], "TinyTask", ["GDPR"])
    assert "## §6 Duties whose card call failed" in text
    assert "`duty_02`" in text and "re-run p3a_org" in text
    # and the converged duty is still rendered with its own statement
    assert ORG_CARD["Statement (EARS)"] in text


# ---------------------------------------------------------------------------
# S5/S6 — the anchor citation set
# ---------------------------------------------------------------------------

VERDICT_ROW = (
    "| `SO-D-01.1-001` | Session rule per `GV.RR-02` | `R1.1` | TB "
    "| Fully covered (anchored) | Discharged by the session rule citing `GV.RR-02` "
    "| PROPOSE_PRODUCT |"
)

PUB = {"SO-D-01.1-001": {"GV.RR-02"}}


def _rows(answer: str) -> list[dict]:
    return p3vd.parse_verdicts(
        "| Objective | Summary | Functional carrier | Skill | State | VC discharge | Action / Round |\n"
        "|---|---|---|---|---|---|---|\n" + answer + "\n")


def test_anchors_cited_come_from_summary_and_discharge() -> None:
    rows = _rows(VERDICT_ROW)
    assert rows[0]["anchors_cited"] == ["GV.RR-02"]


def test_a_silent_row_cites_nothing_and_not_the_published_set() -> None:
    """The merge's regression: inheritance made T3 a tautology."""
    skeleton = [{"id": "SO-D-01.1-001", "anchors": ["GV.RR-02"], "carrier": "`—`",
                 "skill": "`—`", "verdict": "—", "discharge": "—", "action": "—"}]
    rows = _rows(VERDICT_ROW)
    for row in rows:
        row["anchors_cited"] = []  # the model named no anchor anywhere
    merged = p3vd.apply_verdicts(skeleton, rows)
    assert merged[0]["anchors_used"] == [], (
        "a row that cited nothing must not inherit the published set"
    )


def test_t3_catches_an_anchor_invented_in_the_summary() -> None:
    """The citation lives in the summary cell; the discharge is clean."""
    sneaky = VERDICT_ROW.replace("Session rule per `GV.RR-02`", "Session rule per `PR.AC-03`")
    rows = _rows(sneaky)
    findings = p3vd.anchor_findings(rows, PUB)
    assert findings and "PR.AC-03" in findings[0]


def test_fully_covered_without_any_citation_is_a_finding() -> None:
    no_citation = VERDICT_ROW.replace(
        "Session rule per `GV.RR-02`", "Sessions are constrained").replace(
        "Discharged by the session rule citing `GV.RR-02`", "Sessions are constrained")
    rows = _rows(no_citation)
    assert rows[0]["anchors_cited"] == [], "the fixture row must cite nothing at all"
    objectives = [{"id": "SO-D-01.1-001", "anchors": ["GV.RR-02"], "subdomain": "D-01.1"}]
    findings = p3vd.check_verdicts(rows, objectives, ["R1.1"])
    assert any("cites no anchor" in f for f in findings), findings


def test_a_genuine_citation_produces_no_anchor_findings() -> None:
    rows = _rows(VERDICT_ROW)
    objectives = [{"id": "SO-D-01.1-001", "anchors": ["GV.RR-02"], "subdomain": "D-01.1"}]
    assert p3vd.check_verdicts(rows, objectives, ["R1.1"]) == []


# ---------------------------------------------------------------------------
# S7/S8 — the sufficiency line, five buckets
# ---------------------------------------------------------------------------

def _suff(path: Path, lines: list[str], n_rows: int) -> list[str]:
    path.write_text(
        "---\ntitle: 'SUFFICIENCY_ASSESSMENT'\n---\n\n"
        "## Compliance verdict per regulation\n\n" + "\n".join(lines) + "\n",
        encoding="utf-8")
    return p3w._sufficiency_findings(path, n_rows)


def test_five_bucket_lines_pass_and_are_not_flagged_as_relabelled() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "s.md"
        assert _suff(f, [
            "- **GDPR:** 3 fully covered, 1 partial, 2 organizational, 1 design guidance, 0 N/A (7 objective(s) under this regulation)",
            "- **CRA:** 2 fully covered, 2 partial, 3 organizational, 0 design guidance, 0 N/A (7 objective(s) under this regulation)",
        ], 7) == []


def test_identical_counts_across_two_regulations_are_still_relabelled() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "s.md"
        findings = _suff(f, [
            "- **GDPR:** 7 fully covered, 0 partial, 0 organizational, 0 design guidance, 0 N/A (7 objective(s) under this regulation)",
            "- **CRA:** 7 fully covered, 0 partial, 0 organizational, 0 design guidance, 0 N/A (7 objective(s) under this regulation)",
        ], 7)
        assert findings and "relabelled" in findings[0]


def test_a_gdpr_only_case_with_one_line_is_not_a_relabel() -> None:
    """The pre-repair check demanded ≥2 distinct lines; a single-regulation
    case is legitimate and must not fail forever."""
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "s.md"
        assert _suff(f, [
            "- **GDPR:** 7 fully covered, 0 partial, 0 organizational, 0 design guidance, 0 N/A (7 objective(s) under this regulation)",
        ], 7) == []


def test_buckets_summing_below_the_matrix_rows_is_a_finding() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "s.md"
        findings = _suff(f, [
            "- **GDPR:** 3 fully covered, 1 partial, 2 organizational, 0 design guidance, 0 N/A (6 objective(s) under this regulation)",
        ], 7)
        assert any("below the 7 matrix rows" in f_ for f_ in findings), findings


def test_a_declared_total_that_disagrees_with_its_buckets_is_a_finding() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "s.md"
        findings = _suff(f, [
            "- **GDPR:** 3 fully covered, 1 partial, 2 organizational, 0 design guidance, 0 N/A (9 objective(s) under this regulation)",
        ], 6)
        assert any("declares 9" in f_ for f_ in findings), findings


# ---------------------------------------------------------------------------
# A.3 — the V2 renders
# ---------------------------------------------------------------------------

V2_CARD = {
    "id": "R1.1", "name": "Manage Tasks",
    "description": "A business customer creates and tracks tasks.",
    "origin": "Founders business case",
    "interfaces": "Web workspace",
    "dependencies": "Internal Application Database",
    "problems": "manual tracking today",
    "priority": "Must",
}


def test_v2_doc01_keeps_the_identified_problems_row() -> None:
    text = p3c.render_v2_doc01([V2_CARD], {"R1.1": [
        {"objective": "SO-D-01.1-001", "constraint": "the system shall constrain sessions",
         "fit_criterion": "an expired session fails", "anchors": ["GV.RR-02"]}]},
        "TinyTask")
    for row in ("| 4 | Security & Privacy Constraints |", "| 7 | Identified Problems |",
                "| 8 | Priority |", "manual tracking today"):
        assert row in text, row
    assert "From `SO-D-01.1-001`" in text


def test_v2_doc02_does_not_fabricate_a_use_case() -> None:
    """A card allocated from an accepted proposal has no V0 use case; the
    canned scenario was invented behaviour in a deliverable (R6)."""
    allocated = dict(V2_CARD, id="R10.1",
                     origin="Round 1 accepted proposal for `SO-D-01.1-001`")
    text = p3c.render_v2_doc02([allocated], {}, "TinyTask")
    assert "no V0 use case" in text
    assert "Round 1 accepted proposal" in text
    assert "User is authenticated" not in text
    assert "**Main Success Scenario:** —" in text
    # a card that HAS a use case is rendered in full, woven
    real = dict(V2_CARD, usecase={"uc_id": "{U.C. 1.1}", "Traceability": "R1.1",
                                  "Preconditions": "Customer is signed in.",
                                  "Extensions": "—"})
    text2 = p3c.render_v2_doc02(
        [real], {"R1.1": {"Preconditions": "Sessions expire after inactivity", "Extensions": ""}},
        "TinyTask")
    assert "Security: Sessions expire after inactivity" in text2
    assert "no V0 use case" not in text2


# ---------------------------------------------------------------------------
# A.2 — the single V0 source
# ---------------------------------------------------------------------------

FROZEN_DOC = "| **ID:** R1.1 **Name:** Manage Tasks |\n| **Description:** frozen baseline card |\n"
GENERATED_DOC = "| **ID:** R1.1 **Name:** Manage Tasks |\n| **Description:** generated baseline card |\n"


def _run_with_baselines(tmp: Path) -> tuple[Path, Path]:
    run = tmp / "run"
    gen_dir = run / "outputs" / "phase3" / "v0_functional_baseline"
    gen_dir.mkdir(parents=True)
    (gen_dir / "Doc01_Requirements_Specification.md").write_text(GENERATED_DOC, encoding="utf-8")
    case = tmp / "cases" / "Case_X" / "03_PHASE3_SPEC" / "part1_security_privacy" / "v0_functional_baseline"
    case.mkdir(parents=True)
    (case / "Doc01_Requirements_Elicitation_and_PUC.md").write_text(FROZEN_DOC, encoding="utf-8")
    return run, tmp


def test_frozen_source_ignores_the_generated_baseline() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run, repo = _run_with_baselines(Path(tmp))
        doc = p3v.resolve_v0_doc(run, repo, "Case_X", source="frozen")
        assert "frozen baseline card" in doc.read_text(encoding="utf-8")


def test_generated_source_resolves_the_run_local_baseline() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run, repo = _run_with_baselines(Path(tmp))
        doc = p3v.resolve_v0_doc(run, repo, "Case_X", source="generated")
        assert "generated baseline card" in doc.read_text(encoding="utf-8")


def test_generated_never_falls_back_to_the_frozen_corpus() -> None:
    """A run with NO local baseline and source=generated must raise — falling
    back to the frozen corpus here would mix baselines inside one run."""
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp) / "run"
        (run / "steps").mkdir(parents=True)
        case = (Path(tmp) / "cases" / "Case_X" / "03_PHASE3_SPEC"
                / "part1_security_privacy" / "v0_functional_baseline")
        case.mkdir(parents=True)
        (case / "Doc01_Requirements_Elicitation_and_PUC.md").write_text(FROZEN_DOC, encoding="utf-8")
        try:
            p3v.ensure_v0_pool(run, Path(tmp), "Case_X", source="generated")
        except ValueError as e:
            assert "generated" in str(e)
        else:
            raise AssertionError("generated with no local baseline must raise, not fall back")


def test_a_seeded_store_is_the_only_reader_for_every_stage() -> None:
    """Once the store holds cards, the source knobs cannot change the pool."""
    with tempfile.TemporaryDirectory() as tmp:
        run, repo = _run_with_baselines(Path(tmp))
        first = p3v.ensure_v0_pool(run, repo, "Case_X", source="frozen")
        assert first and first[0]["id"] == "R1.1"
        assert (run / "steps" / "phase3" / "cards" / "R1_1.json").is_file()
        # a later stage with a different knob sees the same store
        again = p3v.ensure_v0_pool(run, repo, "Case_X", source="generated")
        assert [c["id"] for c in again] == [c["id"] for c in first]


def test_the_gate_reads_the_pool_without_seeding_it() -> None:
    """run_gate is a pure function of the disk: it must not create state."""
    with tempfile.TemporaryDirectory() as tmp:
        run, repo = _run_with_baselines(Path(tmp))
        pool = p3v.ensure_v0_pool(run, repo, "Case_X", source="frozen", seed=False)
        assert pool, "read-only pool resolution still finds the frozen baseline"
        assert not (run / "steps" / "phase3" / "cards" / "R1_1.json").is_file()


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------

def test_export_flattens_the_notebooks_and_the_gate_verdict() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        run = root / "run"
        for sub in ("outputs/phase3/part1_security_privacy/v2_security_privacy_synthesis",
                    "outputs/phase3/synthesis_rounds", "steps/phase3"):
            (run / sub).mkdir(parents=True)
        (run / "outputs/phase3/part1_security_privacy/v2_security_privacy_synthesis"
         / "Doc01_Requirements_Specification.md").write_text("# doc01", encoding="utf-8")
        (run / "outputs/phase3/part1_security_privacy"
         / "Doc03_Organizational_Requirements.md").write_text("# doc03", encoding="utf-8")
        (run / "outputs/phase3/synthesis_rounds" / "ROUND1_REGISTER.md").write_text("# r1", encoding="utf-8")
        (run / "steps/phase3" / "gate_report.md").write_text("state: CONCLUDED", encoding="utf-8")
        out = p3w.export_deliverables(run, root, "TinyTask", "run_test_1")
        assert out == root / "output" / "TinyTask" / "phase3" / "run_test_1"
        for name in ("Doc01_Requirements_Specification.md", "Doc03_Organizational_Requirements.md",
                     "ROUND1_REGISTER.md", "gate_report.md"):
            assert (out / name).is_file(), name


def test_a_card_without_a_use_case_does_not_kill_the_weave() -> None:
    """A card allocated from an accepted `new` proposal has NO use case.

    The weave looked up `c["usecase"]["uc_id"]` and the whole stage died with
    `KeyError: 'usecase'` (job 2166550) — the first post-round run that ever
    reached the weave. The lookup must answer "no use case carries this"
    instead of raising.
    """
    from aegis_pipeline.phases.phase3.weave import uc_of_carrier

    cards = [
        {"id": "R1.1", "name": "Manage User Accounts", "usecase": {"uc_id": "UC-001"}},
        {"id": "R9.1", "name": "Apply the D-01.1 security constraint"},  # no use case
    ]
    assert uc_of_carrier(cards, "R1.1") == "UC-001"
    assert uc_of_carrier(cards, "R9.1") == "—"
    assert uc_of_carrier(cards, "R99.9") == "—"


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
        except Exception as e:  # a repair that crashes is a repair that failed
            failures += 1
            print(f"  [FAIL] {name}: {type(e).__name__}: {e}")
    print(f"\n{'FAIL' if failures else 'OK'} — {failures} failure(s)")
    sys.exit(1 if failures else 0)
