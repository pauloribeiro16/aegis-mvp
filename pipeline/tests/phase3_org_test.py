#!/usr/bin/env python3
"""phase3_org_test.py — the organizational anchor gate may not lose its teeth.

The first `p3a_org` run returned carried=0/21. Nineteen anchors failed to
resolve, and they were two different failures wearing one message:

  * nine were single-digit suffixes (`GV.RR-2`, `DE.CM-9`) — the model copied
    the worked example, which itself was written with one digit;
  * ten were CSF 1.1 categories (`PR.IP-1`, `PR.AC-5`, `PR.PT-3`) that CSF 2.0
    renamed, which no amount of zero-padding can fix.

`resolve_anchor` therefore pads a suffix only when the padded form exists as a
file. That distinction is the whole content of this file: a tolerant lookup
that resolves `GV.RR-2` and still rejects `PR.IP-1`, because padding the second
would dress a wrong-framework id as a typo and wave it through R2.

These assertions read only committed files and need no model and no GPU.

Usage: python3 pipeline/tests/phase3_org_test.py
Exit 0 iff the gate holds both halves.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3.org import check_org_chain_laws, resolve_anchor  # noqa: E402

CONTROLS = REPO / "baseline" / "CONTROLS"


def test_well_formed_anchors_resolve_unchanged() -> None:
    for a in ("GV.RR-02", "GV.OC-03", "PR.AA-05", "DE.CM-09", "ID.AM-08"):
        assert resolve_anchor(CONTROLS, a) == a, a


def test_single_digit_suffix_resolves_to_its_padded_form() -> None:
    """The format habit the model actually has. Padded, because the file exists."""
    for written, real in (("GV.RR-2", "GV.RR-02"), ("DE.CM-9", "DE.CM-09"),
                          ("GV.OC-4", "GV.OC-04"), ("PR.AA-1", "PR.AA-01")):
        assert resolve_anchor(CONTROLS, written) == real, written


def test_csf_1_1_categories_are_still_rejected() -> None:
    """Padding must not become a disguise.

    `PR.IP`, `PR.AC` and `PR.PT` are CSF 1.1. CSF 2.0 renamed them, so no
    padded form exists and the gate has to fail loudly — a fabricated anchor
    dressed as a typo is worse than a missing one, because it looks anchored.
    """
    for wrong in ("PR.IP-1", "PR.IP-12", "PR.AC-1", "PR.AC-4", "PR.AC-5", "PR.PT-3"):
        assert resolve_anchor(CONTROLS, wrong) is None, wrong


def test_nonsense_is_rejected() -> None:
    for junk in ("GV.RR-99", "PR.ZZ-1", "NOT-AN-ANCHOR", "GV.RR-2x", ""):
        assert resolve_anchor(CONTROLS, junk) is None, junk


def test_every_csf_2_0_id_in_the_corpus_is_two_digit() -> None:
    """The premise the padding rests on. If this changes, padding is wrong."""
    short = [p.stem for p in (CONTROLS / "NIST_CSF_2.0").rglob("*.json")
             if p.name != "_MANIFEST.json" and len(p.stem.rsplit("-", 1)[-1]) < 2]
    assert not short, f"CSF 2.0 ids with a short suffix: {sorted(short)[:8]}"


def test_the_org_ficha_example_is_two_digit() -> None:
    """The example is what the model copies. A regression here is silent.

    Scoped to the worked example and the rules, not the whole file: the
    changelog names the old one-digit values on purpose, and R11 puts
    supersession history there.
    """
    import re

    ficha = (REPO / "docs" / "pipeline" / "prompts"
             / "PROM-P3A-05_ORG.md").read_text(encoding="utf-8")
    # Output schema, rules and self-checks — everything the model reads. The
    # changelog is excluded on purpose: it names the old one-digit values,
    # which is what a changelog is for, and R11 puts history there.
    body = ficha[ficha.index("## Output schema"):ficha.index("## Human gate")]
    cited = set(re.findall(r"`((?:GV|PR|DE|ID|RS|RC)[A-Z]{0,2}\.[A-Z]{2})-(\d+)`", body))
    assert cited, "the model-facing sections should carry at least one anchor"
    bad = [f"{c[0]}-{c[1]}" for c in cited if len(c[1]) != 2]
    assert not bad, f"anchor suffix is not zero-padded to two digits: {bad}"


def test_the_duty_pack_carries_the_published_anchors() -> None:
    """The root cause. A pack with no anchors on it is a fabrication prompt.

    `duties.json` held zero anchors across all 37 duties while the pack comment
    claimed it carried them; the model filled the gap from memory.
    """
    import json

    run = Path.home() / "Work" / "aegis-runs" / "run_p2enr_c1"
    duties_path = run / "steps" / "phase3" / "duties.json"
    if not duties_path.is_file():
        print("  (skipped: no local run_p2enr_c1)")
        return
    duties = json.loads(duties_path.read_text(encoding="utf-8"))
    org = [d for d in duties if d.get("dispositions", {}).get("ORG")]
    assert org, "no ORG duties to check"

    import phase3

    objs = {o["id"]: o for o in phase3.load_objectives(
        run / "outputs" / "phase2" / "Doc01_Operational_Objectives.md")}
    total = sum(len(d["objectives"]) for d in org)
    with_anchors = sum(1 for d in org for oid in d["objectives"]
                       if objs.get(oid, {}).get("anchors"))
    assert total > 0
    assert with_anchors == total, (
        f"{total - with_anchors} of {total} ORG objectives carry no published "
        f"anchor — the pack would hand the model a gap to guess into")


# ---------------------------------------------------------------------------
# Doc00 — the business context document `p3a_org` composes.
#
# It shipped with four bullets permanently reading `—` because it asked the
# fact sheet for `size`, `jurisdiction`, `products_services` and
# `infrastructure`, none of which exist in the Phase 1 schema. The data was in
# the file the whole time, under `size_employees`, `jurisdictions`,
# `product_summary` and `hosting`. A document that renders `—` where it holds
# the fact is worse than no document: it reads as an absence of information
# rather than an absence of code.
# ---------------------------------------------------------------------------

FACT_SHEET_REAL = {
    "company": "TinyTask Lda.",
    "sector": "Technology / Software (B2B SaaS productivity tools)",
    "size_employees": 8,
    "jurisdictions": ["Portugal (EU)"],
    "legal_form": "Private Limited Company (Lda.)",
    "product_summary": "rule-based task management platform sold by subscription",
    "develops_software": True,
    "data_categories": ["customer account metadata", "task data"],
    "data_subjects": ["business customers"],
    "sensitive_data": [],
    "data_scale": "not stated",
    "hosting": "unclear",
    "access_model": "customer accounts with individual logins",
    "third_party_processing": ["external payment provider"],
    "assumed_regulations": ["GDPR — commercial B2B SaaS processing EU personal data"],
    "open_questions": ["hosting: the intake does not say whether it is managed cloud"],
}

PUC_CARD = {
    "id": "R1.1",
    "name": "Manage Tasks",
    "puc": {
        "puc_id": "PUC 1.1",
        "trigger": "A customer creates a task",
        "actor": "Business Customer",
        "boundary": "the task workspace",
        "outputs": "a stored task record",
    },
}
# The shape `p3a_weave` writes when it allocates a carrier for an accepted
# constraint: an objective and a constraint, and no product use case at all.
WEAVE_CARD = {
    "id": "R10.1",
    "objective": "SO-D-01.2-002",
    "constraint": "the system shall authenticate every crossing flow",
    "fit_criterion": "a bypass attempt fails",
    "anchors": ["PR.DS-02"],
    "carrier": "new",
}


def test_doc00_renders_every_fact_that_the_sheet_carries() -> None:
    """The four fields that always read `—` must now carry their values."""
    from aegis_pipeline.phases.phase3.doc00 import render_doc00

    text = render_doc00("TinyTask", FACT_SHEET_REAL, [PUC_CARD], [])
    for expected in ("8", "Portugal (EU)", "Private Limited Company (Lda.)",
                     "rule-based task management platform", "customer accounts with individual logins",
                     "external payment provider", "GDPR — commercial B2B SaaS"):
        assert expected in text, f"{expected!r} is in the fact sheet but not in Doc00"
    # The assertion that kills the defect directly: no bullet may read `—`
    # while the sheet carries the fact behind it.
    for line in text.splitlines():
        if line.startswith("- **") and line.rstrip().endswith("—"):
            key = line.split(":**")[0].removeprefix("- **").lower()
            assert any(k in key for k in ("sensitive", "third-party")), \
                f"empty bullet for a fact the sheet carries: {line}"


def test_doc00_states_what_the_intake_does_not_say() -> None:
    """`open_questions` is where the honest gap lives; dropping it is how a
    document comes to assert more than the evidence supports."""
    from aegis_pipeline.phases.phase3.doc00 import render_doc00

    text = render_doc00("TinyTask", FACT_SHEET_REAL, [PUC_CARD], [])
    assert "What the intake does not say" in text
    assert "does not say whether it is managed cloud" in text


def test_doc00_survives_cards_that_carry_no_product_use_case() -> None:
    """Reading `card["puc"]` unguarded crashed the renderer whenever p3a_org
    ran after p3a_weave, which is the order the chain now runs in."""
    from aegis_pipeline.phases.phase3.doc00 import render_doc00

    text = render_doc00("TinyTask", FACT_SHEET_REAL, [PUC_CARD, WEAVE_CARD], [])
    assert "PUC 1.1" in text
    assert "R10.1" not in text, "a constraint-absorption card is not a product use case"


def test_doc00_with_an_empty_sheet_states_the_gaps_rather_than_omitting_them() -> None:
    """A missing fact must render as a visible `—`, never as a line that is not
    there — an absent bullet is indistinguishable from an absent fact."""
    from aegis_pipeline.phases.phase3.doc00 import render_doc00

    text = render_doc00("TinyTask", {}, [], [])
    for label in ("**Sector:**", "**Size (employees):**", "**Jurisdiction:**", "**Hosting:**"):
        assert f"- {label} —" in text, f"{label} is missing rather than declared empty"
    assert "No product use case cards were produced" in text
    assert "## Part II" in text and "## Part III" in text and "## Part IV" in text


def test_doc00_declares_the_as_is_model_absent_rather_than_filling_it() -> None:
    """There is no machine source for roles-in-context, workflow steps or
    inefficiencies. The document says so instead of estimating."""
    from aegis_pipeline.phases.phase3.doc00 import render_doc00

    text = render_doc00("TinyTask", FACT_SHEET_REAL, [PUC_CARD], [])
    scope = text.split("## Part I")[0]
    assert "As-Is operational model" in scope
    assert "absent rather than estimated" in scope



def test_the_chain_law_guard_refuses_a_law_without_a_driver() -> None:
    """T2 as L0: the qwen3.8 arm cited CRA with GDPR-only drivers twice — the
    prose rule in the ficha did not move the model, the refusal does."""
    parsed = {"Chain": "GDPR Art. 32 → `PO-D-08.1-001` → `PR.DS-01`; CRA Art. 13(6) → `PO-D-08.1-001` → `GV.PO-01`"}
    try:
        check_org_chain_laws(parsed, {"GDPR"})
        raise AssertionError("CRA with GDPR-only drivers passed")
    except ValueError as e:
        assert "chain-law rule" in str(e) and "driver" in str(e), e


def test_the_chain_law_guard_passes_set_based_citations() -> None:
    check_org_chain_laws(
        {"Chain": "GDPR Art. 32 → `PO-D-08.1-001` → `PR.DS-01`; CRA Art. 13(6) → `SO-D-09.3-001` → `GV.PO-01`"},
        {"GDPR", "CRA"})


def test_the_chain_law_guard_normalises_ai_act() -> None:
    check_org_chain_laws(
        {"Chain": "AI Act Art. 15 → `PO-D-05.1-001` → `GV.AI-01`"}, {"AI_Act"})


def test_the_chain_law_guard_skips_without_context() -> None:
    check_org_chain_laws({"Chain": "CRA Art. 13(6) → `PO-D-08.1-001`"}, set())


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