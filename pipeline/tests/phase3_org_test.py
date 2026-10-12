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

from aegis_pipeline.phases.phase3.org import resolve_anchor  # noqa: E402

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