#!/usr/bin/env python3
"""phase3_t5_test.py — o T5 conhece o marcador transversal da ficha.

O T5 (simetria do driver) exige que um driver que a matriz liga a um
portador seja citado pelo entregável activo — mas as linhas realizadas
TRANSVERSALMENTE estão registadas na matriz (ADR-007 D3) e não recebem
citação em cada cartão. O check só conhecia a palavra "transversal"; o
marcador que a ficha usa para essas linhas é `RN (a derivar)`
(PROM-P3A-01), pelo que o T5 exigia uma citação que por desenho não
existe. Foi o que fechou a gate da primeira corrida convergida
(run_p302_muse_c1: G1–G6 fechados, T5 em aberto).

Usage: python3 pipeline/tests/phase3_t5_test.py
Exit 0 iff the transversal exemption holds.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))

import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "check_traceability", REPO / "scripts" / "check_traceability.py")
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)


def _matrix(tmp: Path, carrier: str, verdict: str) -> Path:
    mapping = tmp / "OBJECTIVE_MAPPING.md"
    mapping.write_text(
        "| Objective | Summary | Carrier | Skill | Verdict | VC discharge | Action |\n"
        "|---|---|---|---|---|---|---|\n"
        f"| `PO-D-05.1-001` | data at rest | {carrier} | — | {verdict} | "
        "no card carries it alone; requires a new transversal constraint | "
        "PROPOSE_PRODUCT |\n",
        encoding="utf-8")
    return mapping


def test_a_transversal_row_does_not_need_a_card_citation() -> None:
    """`RN (a derivar)` = the ficha's transversal marker → exempt."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        mapping = _matrix(root, "`RN (a derivar)`", "Partially covered (functional leg + explicit carve-out)")
        case = ct.RunCase.__new__(ct.RunCase)
        case.mapping = mapping
        case.active_text = "(no deliverable cites it)"
        findings = ct.check_driver_symmetry(case)
        assert not findings, findings


def test_a_row_that_claims_a_real_carrier_still_needs_the_citation() -> None:
    """The exemption is narrow: a real carrier still has to be cited."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        mapping = _matrix(root, "`R1.2`", "Fully covered (anchored)")
        case = ct.RunCase.__new__(ct.RunCase)
        case.mapping = mapping
        case.active_text = "(no deliverable cites it)"
        findings = ct.check_driver_symmetry(case)
        assert findings, "a row that claims a card carrier must require the citation"
        assert "does not cite the driver" in findings[0].check, findings[0].check


def test_a_cited_row_passes() -> None:
    """The citation present → no finding."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        mapping = _matrix(root, "`R1.2`", "Fully covered (anchored)")
        case = ct.RunCase.__new__(ct.RunCase)
        case.mapping = mapping
        case.active_text = "the chain cites `PO-D-05.1-001` in Doc01"
        findings = ct.check_driver_symmetry(case)
        assert not findings, findings


def main() -> int:
    tests = [
        test_a_transversal_row_does_not_need_a_card_citation,
        test_a_row_that_claims_a_real_carrier_still_needs_the_citation,
        test_a_cited_row_passes,
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
