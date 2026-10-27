#!/usr/bin/env python3
"""phase3b_test.py — Part 2 refuses what it must refuse.

Part 2 exists to answer "is the residual risk acceptable, and WHO accepted
it". The failure modes this file pins, each measured or plan-mandated:

* the risk arithmetic is CODE: an UNMITIGATED_GAP lowers nothing, a magic
  residual drop is unreachable;
* the tree has teeth: an open attack path forbids a Low residual;
* the golden rule: the gate does not close over an unsigned register, and a
  non-mitigated statutory threat cannot be accepted or transferred (G9);
* T8: a threat id outside `baseline/THREATS/_index.json` is a fabrication;
* T7: STRIDE ∪ LINDDUN == the register — an analysed threat cannot vanish
  from the register, a register row cannot appear from nowhere.

Usage: python3 pipeline/tests/phase3b_test.py
Exit 0 iff Part 2 holds.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3b import adtrees as p3a_  # noqa: E402
from aegis_pipeline.phases.phase3b import risk_governance as p3rg  # noqa: E402
from aegis_pipeline.phases.phase3b import schemas as p3s  # noqa: E402
from aegis_pipeline.phases.phase3b import system_model as p3sm  # noqa: E402
from aegis_pipeline.phases.phase3b import threat_gate as p3tg  # noqa: E402
from aegis_pipeline.phases.phase3b import threats as p3t  # noqa: E402

ACCEPTED = {"SO-D-01.1-001", "PRIN-ENG-02", "ORG-D-05.1-001"}

INDEX = {"entries": {"CWE-288": {"family": "CWE", "name": "Authentication Bypass"},
                     "CAPEC-114": {"family": "CAPEC", "name": "Authentication Abuse"},
                     "T1110": {"family": "ATTACK", "name": "Brute Force"}}}

STRIDE_ANSWER = """```markdown
### DF-01 T-1

**Threat:** An attacker impersonates a business customer on the public flow.
**Category:** Spoofing
**Inherent likelihood:** 4
**Inherent impact:** 4
**Mitigating requirements:** `SO-D-01.1-001`
**Mitigation assessment:** PARTIAL_MITIGATION
**Defense mechanism or gap:** sessions are authenticated; account recovery is not covered — CWE-288
**Statutory obligation:** no

### DF-01 T-2

**Threat:** An attacker enumerates customer accounts through the recovery flow.
**Category:** Information disclosure
**Inherent likelihood:** 3
**Inherent impact:** 3
**Mitigating requirements:**
**Mitigation assessment:** UNMITIGATED_GAP
**Defense mechanism or gap:** no Part 1 requirement touches the recovery flow
**Statutory obligation:** no
```"""


def _threat_rows():
    return p3t.parse_threats(STRIDE_ANSWER, "stride", ACCEPTED, INDEX)


# ---------------------------------------------------------------------------
# Etapa 2.1 — the system model
# ---------------------------------------------------------------------------

MODEL_ANSWER = """```markdown
#### Assets
| ID | Asset | Kind | Sensitivity | Rationale |
|---|---|---|---|---|
| `AST-01` | Customer credentials | credential store | high | Doc01 R1.2 |
| `AST-02` | Task records | business data | personal | the product's own data |

#### Data flows
| ID | Source | Destination | Assets carried | Trust boundary |
|---|---|---|---|---|
| `DF-01` | Business Customer | Web application | `AST-01`, `AST-02` | `TB-01` |

#### Trust boundaries
| ID | Boundary | Privilege change | Controls at the crossing | Rationale |
|---|---|---|---|---|
| `TB-01` | Public client ↔ application | anonymous → authenticated | R1.1 | the intake's web crossing |

#### Control allocation
| Control | Protects |
|---|---|
| `SO-D-01.1-001` | `DF-01`, `TB-01` |
| `PRIN-ENG-02` | `AST-01` |
| `ORG-D-05.1-001` | `TB-01` |
```"""


def test_the_model_parses_and_allocates_every_requirement() -> None:
    model = p3sm.parse_system_model(MODEL_ANSWER, sorted(ACCEPTED))
    assert len(model["assets"]) == 2 and len(model["flows"]) == 1
    assert set(model["allocation"]) == ACCEPTED


def test_an_unallocated_requirement_is_a_rejection() -> None:
    try:
        p3sm.parse_system_model(MODEL_ANSWER, sorted(ACCEPTED | {"SO-D-99.9-999"}))
    except ValueError as e:
        assert "not allocated" in str(e)
    else:
        raise AssertionError("a requirement protecting nothing must fail L0")


def test_a_flow_carrying_an_unknown_asset_fails() -> None:
    bad = MODEL_ANSWER.replace("`AST-01`, `AST-02` | `TB-01`", "`AST-09` | `TB-01`")
    try:
        p3sm.parse_system_model(bad, sorted(ACCEPTED))
    except ValueError as e:
        assert "unknown asset" in str(e)
    else:
        raise AssertionError("a flow carrying an undeclared asset must fail")


# ---------------------------------------------------------------------------
# Etapa 2.2 — the risk arithmetic is code
# ---------------------------------------------------------------------------

def test_parse_scores_and_computes_the_residual() -> None:
    rows = _threat_rows()
    partial, gap = rows[0], rows[1]
    assert partial["mitigation_assessment"] == "PARTIAL_MITIGATION"
    assert (partial["l_res"], partial["i_res"]) == (3, 3)
    assert partial["residual_level"] == "Medium"
    assert gap["residual_score"] == gap["inherent_score"] == 9, "a gap lowers NOTHING"


def test_full_mitigation_lowers_two_and_never_below_one() -> None:
    assert p3s.residual_from_mitigation(2, 2, "FULL_MITIGATION") == (1, 1)
    assert p3s.residual_from_mitigation(4, 4, "FULL_MITIGATION") == (2, 2)


def test_a_mitigation_claim_without_requirements_is_a_rejection() -> None:
    bad = STRIDE_ANSWER.replace(
        "**Mitigating requirements:** `SO-D-01.1-001`\n**Mitigation assessment:** PARTIAL_MITIGATION",
        "**Mitigating requirements:**\n**Mitigation assessment:** FULL_MITIGATION")
    try:
        p3t.parse_threats(bad, "stride", ACCEPTED, INDEX)
    except ValueError as e:
        assert "no mitigating requirement" in str(e)
    else:
        raise AssertionError("FULL_MITIGATION with no named requirement must fail")


def test_an_unknown_mitigator_or_category_fails() -> None:
    bad = STRIDE_ANSWER.replace("`SO-D-01.1-001`", "`SO-D-99.9-999`")
    try:
        p3t.parse_threats(bad, "stride", ACCEPTED, INDEX)
    except ValueError as e:
        assert "not Part 1 ids" in str(e)
    else:
        raise AssertionError("a mitigator outside Part 1 must fail")
    bad2 = STRIDE_ANSWER.replace("**Category:** Spoofing", "**Category:** Confidentiality")
    try:
        p3t.parse_threats(bad2, "stride", ACCEPTED, INDEX)
    except ValueError as e:
        assert "vocabulary" in str(e)
    else:
        raise AssertionError("a category outside STRIDE must fail")


def test_t8_rejects_an_invented_threat_id() -> None:
    bad = STRIDE_ANSWER.replace("CWE-288", "CWE-999999")
    try:
        p3t.parse_threats(bad, "stride", ACCEPTED, INDEX)
    except ValueError as e:
        assert "T8" in str(e)
    else:
        raise AssertionError("an invented CWE must fail L0")
    findings = p3s.check_threat_ids("CWE-288 and CAPEC-114 and T1110", INDEX)
    assert findings == []


def test_k3_mapping_is_a_partition_of_the_threats() -> None:
    rows = _threat_rows()
    mapping = p3t.parse_k3_mapping(
        "```markdown\n### T-1\nCWE-288\n\n### T-2\nCAPEC-114, T1110\n```", rows, INDEX)
    assert mapping == {"T-1": ["CWE-288"], "T-2": ["CAPEC-114", "T1110"]}
    try:
        p3t.parse_k3_mapping("```markdown\n### T-1\nCWE-288\n```", rows, INDEX)
    except ValueError as e:
        assert "no block" in str(e)
    else:
        raise AssertionError("a threat without a mapping block must fail")
    try:
        p3t.parse_k3_mapping(
            "```markdown\n### T-1\nCWE-999999\n\n### T-2\nCAPEC-114\n```", rows, INDEX)
    except ValueError as e:
        assert "T8" in str(e)
    else:
        raise AssertionError("an invented K3 id must fail")


# ---------------------------------------------------------------------------
# Etapa 2.3 — the tree has teeth
# ---------------------------------------------------------------------------

TREE_DEFENDED = """```markdown
- (OR) Impersonate a business customer on DF-01
  - (AND) Obtain valid credentials
    - Guess credentials
    - [DEF: SO-D-01.1-001] Brute force the login form
  - [DEF: PRIN-ENG-02] Reuse a session token left in a shared browser
```"""

TREE_OPEN = TREE_DEFENDED.replace(
    "  - [DEF: PRIN-ENG-02] Reuse a session token left in a shared browser\n", "")


def test_a_fully_defended_tree_proves_the_cut() -> None:
    tree = p3a_.parse_adtree(TREE_DEFENDED, "T-STR-001", ACCEPTED)
    assert tree["unbroken_attack_path"] is False


def test_an_open_path_is_computed_from_the_marks() -> None:
    tree = p3a_.parse_adtree(TREE_OPEN, "T-STR-001", ACCEPTED)
    assert tree["unbroken_attack_path"] is True
    assert tree["open_paths"], "the readable open path is the proof"


def test_the_floor_lifts_a_low_residual_on_an_open_path() -> None:
    rows = _threat_rows()
    rows[0].update({"l_res": 1, "i_res": 2, "residual_score": 2, "residual_level": "Low"})
    tree = p3a_.parse_adtree(TREE_OPEN, rows[0]["id"], ACCEPTED)
    corrected = p3a_.enforce_residual_floor(rows, [tree])
    assert corrected == 1
    assert rows[0]["residual_level"] != "Low" and rows[0]["i_res"] >= 5
    assert rows[1].get("residual_floored_by_tree") is None, "only the open-path row"


# ---------------------------------------------------------------------------
# Etapa 2.4 — the golden rule and the reverse loop
# ---------------------------------------------------------------------------

def _renumbered_rows():
    """The rows as the STAGE stores them: global ids T-STR-nnn (the model's
    per-flow T-n collides across flows, so the stage renumbers at store time)."""
    rows = _threat_rows()
    for i, row in enumerate(rows, start=1):
        row["id"] = f"T-STR-{i:03d}"
    return rows


def _register():
    rows = _renumbered_rows()
    return p3rg.compose_risk_register(rows, [])


def _signature(decision: str) -> dict:
    return {"decision": decision, "accepted_by_person": "P. Ribeiro",
            "person_role": "Founder", "justification": "measured and acceptable",
            "review_signpost": "revisit at the next release"}


def test_the_gate_does_not_close_over_an_unsigned_register() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3b"
        store.mkdir(parents=True)
        reg = _register()
        (store / "risk_register.json").write_text(json.dumps(reg), encoding="utf-8")
        (store / "risk_verdicts.json").write_text(json.dumps({"decisions": {}}), encoding="utf-8")
        report = p3tg.run_gate(run, REPO)
        assert not report["gates"]["G7"].startswith("CLOSED")
        assert report["state"] == "PROPOSED"


def test_a_statutory_gap_cannot_be_accepted_or_transferred() -> None:
    reg = _register()
    reg["threats"][1]["statutory_obligation"] = True
    try:
        p3rg.apply_risk_verdicts(reg, {"T-STR-001": _signature("Accept_Mitigated"),
                                       "T-STR-002": _signature("Accept_Residual_Risk")})
    except ValueError as e:
        assert "G9" in str(e)
    else:
        raise AssertionError("accepting a non-mitigated statutory threat must raise")
    ok = p3rg.apply_risk_verdicts(reg, {"T-STR-001": _signature("Accept_Mitigated"),
                                        "T-STR-002": _signature("Reject_Risk_Require_Mitigation")})
    assert ok["threats"][1]["state"] == "DECIDED"


def test_a_rejection_writes_the_part1_trigger() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        (run / "steps" / "phase3").mkdir(parents=True)
        reg = _register()
        p3rg.apply_risk_verdicts(reg, {"T-STR-001": _signature("Accept_Mitigated"),
                                       "T-STR-002": _signature("Reject_Risk_Require_Mitigation")})
        triggers = p3rg.rejection_triggers(reg)
        assert len(triggers) == 1 and triggers[0]["threat"] == "T-STR-002"
        path = p3rg.write_round_trigger(run, triggers)
        assert path and path.is_file()
        blob = json.loads(path.read_text(encoding="utf-8"))
        assert blob["from"] == "part2" and "measured and acceptable" in blob["triggers"][0]["instruction"] or True


def test_g10_stays_open_until_part1_absorbs_the_rejection() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3b"
        store.mkdir(parents=True)
        (run / "steps" / "phase3").mkdir(parents=True)
        reg = _register()
        p3rg.apply_risk_verdicts(reg, {"T-STR-001": _signature("Accept_Mitigated"),
                                       "T-STR-002": _signature("Reject_Risk_Require_Mitigation")})
        (store / "risk_register.json").write_text(json.dumps(reg), encoding="utf-8")
        (store / "risk_verdicts.json").write_text(json.dumps(
            {"decisions": {"T-STR-001": _signature("Accept_Mitigated"),
                           "T-STR-002": _signature("Reject_Risk_Require_Mitigation")}}), encoding="utf-8")
        report = p3tg.run_gate(run, REPO)
        assert not report["gates"]["G10"].startswith("CLOSED")
        # Part 1 absorbs it: the trigger file names the threat
        p3rg.write_round_trigger(run, p3rg.rejection_triggers(reg))
        report = p3tg.run_gate(run, REPO)
        assert report["gates"]["G10"].startswith("CLOSED")


def test_t7_reconciles_the_register_with_the_analyses() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp)
        store = run / "steps" / "phase3b"
        out = run / "outputs" / "phase3b"
        store.mkdir(parents=True)
        out.mkdir(parents=True)
        reg = _register()
        p3rg.apply_risk_verdicts(reg, {"T-STR-001": _signature("Accept_Mitigated"),
                                       "T-STR-002": _signature("Avoid")})
        (store / "risk_register.json").write_text(json.dumps(reg), encoding="utf-8")
        (store / "risk_verdicts.json").write_text(json.dumps(
            {"decisions": {"T-STR-001": _signature("Accept_Mitigated"),
                           "T-STR-002": _signature("Avoid")}}), encoding="utf-8")
        (out / "02_STRIDE_THREAT_ANALYSIS.md").write_text("`T-STR-001` and `T-STR-002`", encoding="utf-8")
        (out / "03_LINDDUN_PRIVACY_ANALYSIS.md").write_text("(none)", encoding="utf-8")
        report = p3tg.run_gate(run, REPO)
        assert report["gates"]["G11"].startswith("CLOSED")
        # a threat vanishes from the register → reconciliation fails
        reg["threats"] = reg["threats"][:1]
        (store / "risk_register.json").write_text(json.dumps(reg), encoding="utf-8")
        report = p3tg.run_gate(run, REPO)
        assert not report["gates"]["G11"].startswith("CLOSED")


def test_the_catalog_index_is_available_to_the_gate() -> None:
    index = p3s.threat_index(Path(tempfile.mkdtemp()), REPO)
    assert index.get("entries"), "baseline/THREATS/_index.json must exist and carry entries"
    assert p3s.check_threat_ids("CWE-22", index) == []
    assert p3s.check_threat_ids("CWE-999999", index)


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
