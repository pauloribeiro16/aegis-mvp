#!/usr/bin/env python3
"""phase3_pack_test.py — every Phase 3 step builds a pack the model can read.

Six calibration jobs on Deucalion died at `p3a_org_cluster` with
`ValueError: unknown step`: the pack builders for the Onda B/D steps had been
written into `compose_call` instead of `build_pack`, and `build_pack` — the
only place that knows how to build a pack — raised for every step the new
code was supposed to add. The six jobs produced zero proposals.

The parsers had unit tests with fabricated strings; `compose_call` was never
called on the new steps. This file calls it on EVERY Phase 3 step, against a
run directory built from the real Case 01 artefacts, and pins three things per
step:

* the call does not raise — no unknown step, no missing fixture;
* the PACK reaches the model — the user message carries the pack files, not
  only the output schema (the pack text is rendered inside `build_pack`, so
  files appended after that never arrived);
* the ficha's CONTRACT reaches the model — the body sections, not only the
  prompt body. Six of the fifteen Phase 3 fichas have an empty prompt body,
  and the model was asked to judge coverage without ever being told what the
  five verdicts mean, or that a product-behaviour restriction MUST be
  `PROPOSE_PRODUCT`.

Usage: python3 pipeline/tests/phase3_pack_test.py
Exit 0 iff every Phase 3 step is buildable and readable.
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

import compose  # noqa: E402

CASE = "Case_01_TinyTask_SaaS"

FACT_SHEET = """company_id: TinyTask
employees: 8
hosting: managed cloud
third_parties: an external payment gateway
personal_data: customer account identifiers
"""

CARD = {
    "id": "R1.1", "name": "Manage User Accounts",
    "description": "The system shall authenticate every account before granting access.",
    "constraints": [{"id": "RN-1", "text": "the system shall authenticate every account",
                     "fit_criterion": "an unauthenticated request is refused",
                     "chain": ["PR.AA-01"]}],
    "priority": "Must", "objectives": ["SO-D-01.1-001"], "subdomain": "D-01.1",
}

OBJECTIVE = "PO-D-01.1-001"

PROPOSAL = {
    "objective": OBJECTIVE, "subdomain": "D-01.1",
    "constraint": "the system shall authenticate every account before granting access",
    "fit_criterion": "an unauthenticated request is refused with an authorisation error",
    "risk": "an unauthorised actor reaches a personal-data record",
    "anchors": ["PR.AA-01"], "rules": [], "carrier": "R1.1",
}

#: (step, subdomain, the pack file that must reach the model, a string that
#: only the ficha's CONTRACT can carry).
STEPS: list[tuple[str, str | None, str, str]] = [
    ("p3a_map:D-01.1", "D-01.1", "VERDICT_PACK.md", "The five verdicts"),
    ("p3a_cards", None, "PHASE2_OBJECTIVES.md", "Rules the output must obey"),
    ("p3a_card:R1.1", "R1.1", "INVENTORY.md", "Rules the output must obey"),
    ("p3a_prin:PRIN-ENG-01", "PRIN-ENG-01", "PRINCIPLE_PACK.md", "Rules the output must obey"),
    ("p3a_propose:D-01.1", "D-01.1", "PROPOSAL_PACK.md", "Rules the output must obey"),
    ("p3a_org:access-rights", "access-rights", "DUTY.md", "Rules the output must obey"),
    ("p3a_weave:R1.1", "R1.1", "CARD.json", "Rules the output must obey"),
    ("p3a_repropose:2:" + OBJECTIVE, None, "ITEM.json", "Rules the output must obey"),
    ("p3a_org_cluster", None, "ORG_ROWS.md", "The grouping rule"),
    ("p3b_model", None, "Doc01_Requirements_Specification.md", "Rules the output must obey"),
    ("p3b_stride:DF-01", "DF-01", "FLOW.md", "Rules the output must obey"),
    ("p3b_linddun", None, "MODEL.md", "Rules the output must obey"),
    ("p3b_k3", None, "MAPPING_PACK.md", "Rules the output must obey"),
    ("p3b_tree:T-STR-001", "T-STR-001", "THREAT.md", "Rules the output must obey"),
]


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, blob) -> None:
    _write(path, json.dumps(blob, indent=1, ensure_ascii=False))


def _run_dir(tmp: Path) -> Path:
    """A run directory holding the artefacts the Phase 3 packs read."""
    run = tmp / "run"
    _write_json(run / "manifest.json", {"case_id": CASE})
    _write(run / "steps" / "fact_sheet.yaml", FACT_SHEET)

    phase2 = REPO / "cases" / CASE / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md"
    (run / "outputs" / "phase2").mkdir(parents=True, exist_ok=True)
    shutil.copy(phase2, run / "outputs" / "phase2" / "Doc01_Operational_Objectives.md")

    # the V0 candidate pool
    _write_json(run / "steps" / "phase3" / "cards" / "R1_1.json", {"card": CARD})
    _write_json(run / "steps" / "phase3" / "cards" / "inventory.json",
                {"cards": [{"id": "R1.1", "name": CARD["name"]}]})

    # the verdicts p3a_map produced: one organizational row, one covered row
    _write_json(run / "steps" / "phase3" / "verdicts_D-01_1.json", [
        {"id": OBJECTIVE, "verdict": "No functional carrier (organizational)",
         "carrier": "`—`", "skill": "`—`",
         "discharge": "the named organizational obligation",
         "action": "ROUTE_ORG"},
    ])
    _write_json(run / "steps" / "phase3" / "verdicts_D-01_2.json", [
        {"id": "PO-D-01.2-001", "verdict": "Partially covered (functional leg + explicit carve-out)",
         "carrier": "`R1.1`", "skill": "`AS`",
         "discharge": "the card carries the access leg; the rest goes to design guidance",
         "action": "PROPOSE_PRODUCT"},
    ])

    # the acceptance round: one accepted item and one pending adjustment
    _write_json(run / "steps" / "phase3" / "round1_state.json", {
        "accepted": [PROPOSAL], "rejected": [], "adjusted": [],
        "pending_adjustment": [{**PROPOSAL, "adjust_note": "split the lock out"}],
        "retired": [], "open": [], "converged": False, "round": 1,
        "functional_changes": [],
    })

    # the organizational duty the cluster stage will group
    _write_json(run / "steps" / "phase3" / "duties.json", [{
        "slug": "access-rights", "duty": "Review access rights periodically",
        "objectives": [OBJECTIVE], "disposition": "ORG",
    }])

    # Part 1's accepted package, as the Part 2 model stage reads it
    v2 = run / "outputs" / "phase3" / "part1_security_privacy"
    for name in ("Doc01_Requirements_Specification.md", "Doc02_System_Use_Cases.md",
                 "Doc03_Organizational_Requirements.md"):
        _write(v2 / name, f"# {name}\n\nthe accepted Part 1 package\n")

    # the system model and the threats Part 2 derives from it
    _write_json(run / "steps" / "phase3b" / "system_model.json", {"model": {
        "assets": [{"id": "AST-01", "name": "Customer credentials",
                    "kind": "credential store", "sensitivity": "high"}],
        "flows": [{"id": "DF-01", "source": "Business customer",
                   "destination": "Web application",
                   "assets_carried": ["AST-01"], "trust_boundary": "TB-01"}],
        "trust_boundaries": [{"id": "TB-01", "privilege_change": "anonymous → authenticated"}],
        "allocation": {"SO-D-01.1-001": ["DF-01", "AST-01"]},
    }})
    threat = {
        "id": "T-STR-001", "target": "DF-01", "method": "stride",
        "threat": "an actor intercepts the credentials in transit",
        "category": "Information disclosure",
        "l_inh": 4, "i_inh": 4, "inherent_score": 16, "inherent_level": "Critical",
        "mitigating_requirements": ["SO-D-01.1-001"],
        "mitigation_assessment": "FULL_MITIGATION",
        "defense": "the accepted requirement authenticates the account",
        "statutory_obligation": False,
        "l_res": 2, "i_res": 2, "residual_score": 4, "residual_level": "Low",
    }
    _write_json(run / "steps" / "phase3b" / "stride_DF_01.json", {"threats": [threat]})
    _write_json(run / "steps" / "phase3b" / "linddun.json", {"threats": []})
    return run


def test_every_phase3_step_builds_a_pack_the_model_reads() -> None:
    """The call does not raise, the pack arrives, the contract arrives."""
    with tempfile.TemporaryDirectory() as tmp:
        run = _run_dir(Path(tmp))
        case = compose.load_case(REPO, CASE)
        failures: list[str] = []
        for step, subdomain, pack_file, contract_probe in STEPS:
            try:
                call = compose.compose_call(REPO, case, run, step, subdomain)
            except Exception as e:  # noqa: BLE001 — the failure IS the finding
                failures.append(f"{step}: {type(e).__name__}: {e}")
                continue
            user = call["user"]
            if pack_file not in user:
                failures.append(f"{step}: the pack file {pack_file!r} did not reach the model")
            if "----- BEGIN FILE:" not in user:
                failures.append(f"{step}: no pack file reached the model at all")
            if contract_probe not in user:
                failures.append(
                    f"{step}: the ficha's contract did not reach the model "
                    f"({contract_probe!r} missing)")
            if not call["system"].strip():
                failures.append(f"{step}: no system message")
        assert not failures, "\n".join(failures)


def test_no_phase3_ficha_sends_an_empty_instruction() -> None:
    """The six Phase 3 fichas whose prompt body was empty still instruct."""
    for name in sorted(p.name for p in (REPO / "docs" / "pipeline" / "prompts").glob("PROM-P3*.md")):
        ficha = compose.parse_ficha(REPO / "docs" / "pipeline" / "prompts" / name)
        assert ficha["body_is_instruction"], (
            f"{name}: a Phase 3 ficha must declare `body_is_instruction: true`")
        assert ficha["instruction_text"].strip(), f"{name}: empty instruction"
        assert len(ficha["instruction_text"]) > len(ficha["prompt_body"]), (
            f"{name}: the instruction must carry the ficha's body sections, "
            "not only the prompt body")


def test_the_phase1_and_phase2_prompts_are_untouched() -> None:
    """Phase 1/2 prompts are measured and frozen: their bytes do not move.

    The Phase 3 fichas opt in to the contract picker; the older ones do not,
    so `compose_call` keeps sending them exactly what it sent before.
    """
    for path in sorted((REPO / "docs" / "pipeline" / "prompts").glob("PROM-*.md")):
        if path.name.startswith("PROM-P3"):
            continue
        ficha = compose.parse_ficha(path)
        assert not ficha["body_is_instruction"], (
            f"{path.name}: only the Phase 3 fichas may change what the model reads")
        assert ficha["prompt_body"] == ficha["prompt_body"].strip(), path.name


def test_the_phase3_shim_carries_every_name_the_pipeline_uses() -> None:
    """The cluster imports the SHIM (`pipeline/src/phase3.py`), not the package.

    The shim re-exports names explicitly; a new `phase3.<name>` call in the
    runner or compose that is not added to the shim is an AttributeError one
    minute into a 4-hour GPU job — jobs 2160351-2160356 died exactly there,
    and job 2166344 (the collapse guard) the same way.

    The check is EXHAUSTIVE, not a hand-written list: the list was itself the
    defect (it did not name `collapse_findings`, so it stayed green while the
    job died). The shim must export everything the package exports.
    """
    import phase3  # the shim, resolved through pipeline/src on sys.path
    import aegis_pipeline.phases.phase3 as pkg

    missing = [name for name in pkg.__all__ if not hasattr(phase3, name)]
    assert not missing, (
        f"the phase3 shim does not export {missing} — add them to "
        "pipeline/src/phase3.py or the cluster dies on `import phase3` "
        "AttributeError one minute into the job")

    # and the names the runner/compose actually call, spelled out so the
    # intent survives a refactor of the package's export list
    names = [
        "load_objectives", "build", "check", "check_verdicts", "verdict_defects",
        "collapse_findings", "apply_verdicts", "render_matrix", "render_principles",
        "domain_names_from", "ensure_v0_pool", "v0_source", "VERDICTS",
        "ORGANIZATIONAL", "build_verdict_pack", "load_rule_catalogue",
    ]
    absent = [n for n in names if not hasattr(phase3, n)]
    assert not absent, f"the phase3 shim is missing {absent}"


def main() -> int:
    tests = [
        test_every_phase3_step_builds_a_pack_the_model_reads,
        test_no_phase3_ficha_sends_an_empty_instruction,
        test_the_phase1_and_phase2_prompts_are_untouched,
        test_the_phase3_shim_carries_every_name_the_pipeline_uses,
    ]
    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            failures += 1
            print(f"  [FAIL] {test.__name__}: {e}")
        except Exception as e:  # noqa: BLE001
            failures += 1
            print(f"  [FAIL] {test.__name__}: {type(e).__name__}: {e}")
        else:
            print(f"  [OK ] {test.__name__}")
    print(f"\n{'FAIL' if failures else 'OK'} — {len(tests)} ran, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
