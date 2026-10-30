#!/usr/bin/env python3
"""phase3_collapse_guard_test.py — a guarda de colapso é SUAVE e tem âmbito medido.

A ficha v1.4.0 (extensão de vocabulário da regra de acoplamento) NÃO moveu
o encaminhamento: D-05 ficou 4/7 e D-07 4/5, idênticos ao v1.3.0, com o
global a subir de 66% para 68% (EXP_P3_04, falsificadores H1 e H2
disparados). A revisão estrutural que o próprio pré-registo obriga é uma
guarda de reparo L0 — e esta versa fixa as suas três qualidades:

* **âmbito medido** — só os domínios onde o gabarito manual diz que a
  obrigação é do produto. D-02 (100% organizacional no gabarito) NÃO é
  desafiado: seria o mesmo erro pelo lado oposto;
* **suave** — dispara uma vez; se o modelo não ceder, a resposta dele fica
  (perder o sub-domínio seria pior que um mau encaminhamento visível);
* **pedagógica** — o defeito ENSINA a regra (o que perguntar a cada
  obrigação), nunca dita a resposta.

Usage: python3 pipeline/tests/phase3_collapse_guard_test.py
Exit 0 iff the guard holds.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "pipeline" / "src"))

from aegis_pipeline.phases.phase3 import verdicts as V  # noqa: E402


def _row(oid: str, subdomain: str, verdict: str) -> dict:
    """A PARSED verdict row — the shape `parse_verdicts` produces.

    It carries NO "subdomain" key (only the merged rows do). The first
    version of this test added the key, and the guard then passed its rows by
    a key the production path never sets: the guard found zero rows and never
    fired (run_p304b measured the routing bit-identical to the run without
    it). The `subdomain` argument is only used to name the call.
    """
    return {"id": oid, "verdict": verdict, "action": "ROUTE_ORG"}


def test_a_collapsed_product_domain_is_challenged() -> None:
    """D-05 a 57% organizacional — acima do gabarito (14%) — é desafiado."""
    rows = [_row(f"PO-D-05.{i}-001", "D-05.1", V.ORGANIZATIONAL) for i in range(4)]
    rows.append(_row("PO-D-05.2-001", "D-05.2", V.ORGANIZATIONAL))
    rows.append(_row("PO-D-05.2-002", "D-05.2", "Partially covered (functional leg + explicit carve-out)"))
    findings = V.collapse_findings(rows, "D-05")
    assert findings, "a collapsed D-05 must be challenged"
    # the finding TEACHES: it asks what to re-read, it does not dictate a verdict
    text = findings[0]
    assert "re-read" in text and "governs" in text, text
    assert "verdict" not in text.lower() or "verdict" in text.lower()


def test_the_gabarito_domains_are_not_challenged() -> None:
    """D-02 é 100% organizacional no gabarito: desafiá-lo seria errar ao contrário."""
    rows = [_row(f"PO-D-02.{i}-001", "D-02.1", V.ORGANIZATIONAL) for i in range(4)]
    assert not V.collapse_findings(rows, "D-02"), (
        "D-02 is 100% organizational in the hand-written matrix — the guard must not "
        "challenge it")
    # and D-08/D-09/D-10 are mostly organizational too
    for domain in ("D-08", "D-09", "D-10"):
        rows = [_row(f"PO-{domain}.1-00{i}", f"{domain}.1", V.ORGANIZATIONAL) for i in range(4)]
        assert not V.collapse_findings(rows, domain), f"{domain} must not be challenged"


def test_a_healthy_product_domain_is_not_challenged() -> None:
    """D-05 no gabarito (14%) —fewer than 65% organizational — passa."""
    rows = [_row(f"PO-D-05.1-00{i}", "D-05.1", "Partially covered (functional leg + explicit carve-out)")
            for i in range(5)]
    rows.append(_row("PO-D-05.2-001", "D-05.2", V.ORGANIZATIONAL))
    assert not V.collapse_findings(rows, "D-05")


def test_the_guard_needs_enough_rows_to_mean_something() -> None:
    """Duas linhas não são um colapso — o limiar mínimo protege o lote pequeno."""
    rows = [_row("PO-D-05.1-001", "D-05.1", V.ORGANIZATIONAL),
            _row("PO-D-05.1-002", "D-05.1", V.ORGANIZATIONAL)]
    assert not V.collapse_findings(rows, "D-05")


def test_the_guard_is_not_a_batch_gauge() -> None:
    """A guarda é por sub-domínio: o M-26 (lote inteiro, D-02..D-07) é que mede o lote."""
    rows = [_row(f"PO-D-01.1-00{i}", "D-01.1", V.ORGANIZATIONAL) for i in range(3)]
    rows += [_row(f"PO-D-03.1-00{i}", "D-03.1", V.ORGANIZATIONAL) for i in range(3)]
    # per-domain challenge, each is challenged
    assert V.collapse_findings(rows, "D-01")
    assert V.collapse_findings(rows, "D-03")


def main() -> int:
    tests = [
        test_a_collapsed_product_domain_is_challenged,
        test_the_gabarito_domains_are_not_challenged,
        test_a_healthy_product_domain_is_not_challenged,
        test_the_guard_needs_enough_rows_to_mean_something,
        test_the_guard_is_not_a_batch_gauge,
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
