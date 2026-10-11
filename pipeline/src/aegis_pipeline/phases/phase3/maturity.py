"""A regra de níveis de maturidade do QNRCS, partilhada pelo script e por quem
mais a consuma. Extracção da lógica que estava só em scripts/qnrcs_maturity.py
para poder ser testada e reusada (o Inspector pode vir a consumi-la)."""

from __future__ import annotations

import json
from pathlib import Path

LEVEL_OF_TIER = {"basico": 2, "substancial": 3, "elevado": 4}
TIERS_CUMULATIVE = (("basico", 2), ("substancial", 3), ("elevado", 4))


def maturity_levels(
    extract_path: Path,
    controls: list[dict],
    tier: str,
    run_anchors: set[str],
) -> dict:
    """Nível de maturidade 0–4 por objectivo, da semântica cumulativa do QNRCS.

    Os tiers são cumulativos (Básico ⊂ Substancial ⊂ Elevado, com exigência
    escalada por controlo): o nível atingido de um objectivo é o maior k tal que
    TODOS os controlos exigidos até k estão ancorados pela corrida. O 5 fica
    reservado a certificação externa (art. 27.º do Reg. 756/2026).
    """
    data = json.loads(extract_path.read_text(encoding="utf-8"))
    obj_of = {c["control_id"]: str(c["function"]).split(" — ")[0] for c in controls}
    mapped = {c["control_id"]: set(c.get("mapped_nist_csf") or []) for c in controls}
    tier_measures = data["medidas_essenciais_importantes"]

    expected: dict[str, dict[int, set[str]]] = {}
    for tier_name, _ in TIERS_CUMULATIVE:
        level = LEVEL_OF_TIER[tier_name]
        for m in tier_measures[tier_name]:
            cid = m.get("control_id")
            oid = obj_of.get(cid)
            if not oid or not cid:
                continue
            expected.setdefault(oid, {2: set(), 3: set(), 4: set()})
            for lv in TIERS_CUMULATIVE:
                if level >= lv[1]:
                    expected[oid][lv[1]].add(cid)

    out: dict[str, dict] = {}
    for oid, lv_sets in sorted(expected.items()):
        cov = {
            lv: round(100 * len({c for c in ids if mapped.get(c, set()) & run_anchors}) / max(len(ids), 1), 1)
            for lv, ids in lv_sets.items()
        }
        level = 0
        for lv in (4, 3, 2):
            if cov[lv] >= 100:
                level = lv
                break
        if level == 0 and cov[2] > 0:
            level = 1
        out[oid] = {
            "nivel_atingido": level,
            "cobertura_cumulativa": cov,
            "controlos_esperados": {str(lv): len(ids) for lv, ids in lv_sets.items()},
        }
    return {
        "objectivos": out,
        "escala": "0–4 (+5 reservado a certificação externa, art. 27.º)",
        "nota": "nível atingido = o maior k cujo conjunto cumulativo de controlos (Básico → B∪S → B∪S∪E) está 100% ancorado pela corrida",
        "nivel_esperado": LEVEL_OF_TIER[tier],
    }
