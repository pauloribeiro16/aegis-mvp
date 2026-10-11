#!/usr/bin/env python3
"""extract_qnrcs_maturity_tool.py — o QNRCS no formato do Maturity Tool.

O QNRCS (Regulamento n.º 756/2026, transposição da NIS 2) é o mesmo
framework do NIST CSF 2.0 com os códigos e a escala de níveis próprios: seis
objectivos, 22 categorias, 107 controlos. Este script escreve
`docs/research/qnrcs/qnrcs_maturity_tool.json` no **mesmo formato** que
`scripts/extract_csf_maturity_tool.py` produz para o workbook NIST, para que o
Inspector sirva os dois com o mesmo componente de página.

Determinístico, stdlib-only, zero chamadas ao modelo. A fonte é
`docs/research/qnrcs/QNRCS_Reg756_2026_extract.json` (extraído do dashboard do
investigador, ver `docs/research/qnrcs/README.md`).

O que difere do workbook NIST, e porquê:
  - **Sem notas de demonstração.** O NIST traz valores inventados para mostrar
    o gráfico; o QNRCS é um regulamento e não traz nada. Todos os controlos
    entram por pontuar — o estado inicial correcto para uma auto-avaliação.
  - **A escala NÃO é a mesma** (Inicial → Otimizado), com os textos do
    workbook. O que muda são os *níveis* do QNRCS: três tiers cumulativos
    (Básico ⊂ Substancial ⊂ Elevado) que fixam o que se espera de cada
    controlo. Ambos são emitidos.

Uso: python3 scripts/extract_qnrcs_maturity_tool.py [--repo <repo>] [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_DEFAULT = Path(__file__).resolve().parents[1]
EXTRACT_REL = "docs/research/qnrcs/QNRCS_Reg756_2026_extract.json"
OUT_REL = "docs/research/qnrcs/qnrcs_maturity_tool.json"

TIER_ORDER = ("basico", "substancial", "elevado")

# O nome que o Regulamento usa tem acento (`Básico`) e é assim que aparece tanto
# em `medidas[].nivel` como nos thresholds da matriz de risco. Derivar o nome com
# `capitalize()` produzia `Basico` e o cruzamento com os thresholds falhava em
# silêncio — o tier BASICo ficava com 0 medidas e sem intervalo de risco.
TIER_NAMES = {"basico": "Básico", "substancial": "Substancial", "elevado": "Elevado"}

# A escala do QNRCS é a DO QNRCS — não a 1–5 do workbook NIST.
#
# A escala 1–5 mede um grau de maturidade *de uma medida que já existe*
# (a política está escrita? o processo é documentado?). O QNRCS não mede isso:
# pergunta que medidas do Anexo III estão implementadas, e as medidas estão
# escalonadas por tier. Projectar os tiers na escala 1–5 obrigava a um mapeamento
# que não tem fonte nenhuma (foi registado em METRICS.md como M-25 e retirado).
# O estado de um controlo é o tier mais alto cujas medidas a entidade cumpre,
# mais um estado para "não implementada" — que a escala 1–5 não tinha lugar para.
TIER_TO_STATE = {"basico": 1, "substancial": 2, "elevado": 3}

# Como o `refs` do extract está organized, e por que ordem se apresenta.
REF_LABELS = (
    ("nistcsf", "NIST CSF 2.0"),
    ("nist80053", "NIST SP 800-53"),
    ("iso27001", "ISO/IEC 27001"),
    ("iso27002", "ISO/IEC 27002"),
    ("cyfun", "CYFUN"),
    ("cis", "CIS Controls"),
)


def _fmt_refs(refs: dict) -> list[str]:
    """`{'nistcsf': ['DE.AE-02']}` → `['NIST CSF 2.0: DE.AE-02']`.

    O NIST traz duas colunas separadas (exemplos de implementação e referências
    informativas); o QNRCS só tem referências, por isso a lista devolvida é só
    a segunda — a folha de subcategorias diz-o onde se vê.
    """
    out: list[str] = []
    for key, label in REF_LABELS:
        values = refs.get(key) or []
        for v in values:
            out.append(f"{label}: {v}")
    return out


def _tier_doc(measures: list[dict], thresholds: list[dict]) -> list[dict]:
    by_level = {t["nivel"]: t for t in thresholds}
    counts = defaultdict(int)
    for m in measures:
        counts[m["nivel"]] += 1
    out = []
    for tier in TIER_ORDER:
        nome = TIER_NAMES[tier]
        thr = by_level.get(nome, {})
        out.append(
            {
                "id": tier,
                "nome": nome,
                "state": TIER_TO_STATE[tier],
                "risco_min": thr.get("min"),
                "risco_max": thr.get("max"),
                "n_medidas": counts.get(nome, 0),
            }
        )
    return out


def build(repo: Path) -> dict:
    extract_path = repo / EXTRACT_REL
    if not extract_path.exists():
        raise SystemExit(f"missing {extract_path}")
    src = json.loads(extract_path.read_text(encoding="utf-8"))

    measures_by_control: dict[str, dict[str, dict]] = defaultdict(dict)
    for tier in TIER_ORDER:
        for m in src["medidas_essenciais_importantes"].get(tier, []):
            measures_by_control[m["control_id"]][tier] = {
                "medida": m.get("medida", ""),
                "criterio": m.get("criterio", ""),
                "nivel": m.get("nivel", ""),
            }

    thresholds = src["matriz_risco"].get("thresholds", [])
    tier_doc = _tier_doc(src["medidas_essenciais_importantes"].get("basico", [])
                         + src["medidas_essenciais_importantes"].get("substancial", [])
                         + src["medidas_essenciais_importantes"].get("elevado", []),
                         thresholds)

    # Contagem de medidas por categoria — é o «# Controlos» desta folha: o que
    # distingue uma categoria é quantas medidas o regulador pede nela.
    cat_of = {c["id"]: c["categoria"] for c in src["controlos"]}
    per_cat: dict[str, dict[str, int]] = defaultdict(lambda: {t: 0 for t in TIER_ORDER})
    for cid, tiers in measures_by_control.items():
        cat = cat_of.get(cid)
        if not cat:
            continue
        for tier in tiers:
            per_cat[cat][tier] += 1

    functions = [
        {"id": o["id"], "name": f"{o['id']} — {o['nome']}", "text": f"{o['id']} — {o['nome']}"}
        for o in src["objetivos"]
    ]
    categories = [
        {
            "id": c["code"],
            "name": c["nome"],
            "description": c.get("intro", ""),
            "function": c["objetivo"],
        }
        for c in src["categorias"]
    ]
    subcategories = [
        {
            "id": c["id"],
            "text": c["titulo"],
            "description": c.get("descricao", ""),
            "category": c["categoria"],
            "function": c["objetivo"],
            "refs": _fmt_refs(c.get("refs") or {}),
            "measures": measures_by_control.get(c["id"], {}),
            # Sem nota de demonstração: um regulamento não as traz. O alvo por
            # omissão é o estado do tier básico — a entidade pode mudá-lo.
            "policy_score": None,
            "policy_reasoning": "",
            "practice_score": None,
            "practice_reasoning": "",
        }
        for c in src["controlos"]
    ]

    summary = []
    for cat in categories:
        counts = per_cat[cat["id"]]
        summary.append(
            {
                "id": cat["id"],
                "name": cat["name"],
                "n_controls": cat_counts(src, cat["id"]),
                "n_medidas": counts,
                "target": TIER_TO_STATE["basico"],
                "policy": None,
                "practice": None,
            }
        )

    track = {
        "scale": {
            "kind": "qnrcs",
            "max": 3,
            "na_label": "Sem medida",
            "states": [
                {"value": 0, "label": "Não implementado",
                 "description": "A entidade não cumpre nenhuma medida do Anexo III para este controlo."},
                {"value": 1, "label": "Básico",
                 "description": "Cumpre as medidas essenciais do tier básico."},
                {"value": 2, "label": "Substancial",
                 "description": "Cumpre o básico e as medidas acrescidas do tier substancial."},
                {"value": 3, "label": "Elevado",
                 "description": "Cumpre o básico, o substancial e as medidas acrescidas do tier elevado."},
            ],
        },
        "core_sheet": "QNRCS — Anexo III",
        "summary_sheet": "QNRCS por categoria",
        "summary_label": "QNRCS — Regulamento n.º 756/2026",
        "summary_date": src["meta"]["diario"],
        "overall_average": {"target": None, "policy": None, "practice": None},
        "functions": functions,
        "categories": categories,
        "subcategories": subcategories,
        "summary": summary,
        "n_measures": sum(t["n_medidas"] for t in tier_doc),
        "n_controls_with_measures": len(measures_by_control),
        "escalating_controls": sum(1 for m in measures_by_control.values() if len(m) == 3),
    }

    return {
        "meta": {
            "title": "QNRCS — Quadro Nacional de Referência de Cibersegurança",
            "fonte": src["meta"]["fonte"],
            "diario": src["meta"]["diario"],
            "base_legal": src["meta"]["base_legal"],
            "gerado_em": src["meta"]["gerado_em"],
            "author": "Regulamento n.º 756/2026 — fonte primária, não ferramenta",
            "is_nist_publication": False,
            "preamble": (
                "O QNRCS é a transposição da NIS 2 em Portugal (DL 125/2025, "
                "Regulamento n.º 756/2026). Tem a mesma forma do NIST CSF 2.0 — "
                "seis funções, categorias e controlos — com códigos próprios e "
                "medidas agrupadas em três níveis de exigência."
            ),
            "changelog": [],
            "directions": [
                "Pontue cada controlo nos dois eixos da escala 1–5, como no workbook NIST.",
                "As medidas do Anexo III dizem o que o regulador exige em cada tier; o painel de níveis mostra a escada.",
                "O alvo por omissão de cada categoria é o nível do tier básico — ajuste-o ao tier da entidade.",
            ],
            "demo_values_notice": "",
            "warnings": src["meta"].get("warnings", []),
            "source": EXTRACT_REL,
            "source_id": "QNRCS-756/2026",
            "evidence": "PRIMARY",
        },
        "tiers": tier_doc,
        "scale_note": (
            "Escala própria do QNRCS: não implementado · Básico · Substancial · "
            "Elevado. O estado de um controlo é o tier mais alto cujas medidas do "
            "Anexo III a entidade cumpre. Não há nível 5 (Otimizado) nem "
            "certificação: o art. 27.º trata de certificação externa, que não é "
            "um estado de implementação."
        ),
        "risk_matrix": src["matriz_risco"],
        "public_measures": src["medidas_publicas_relevantes"],
        "tracks": [track],
    }


def cat_counts(src: dict, code: str) -> int:
    return sum(1 for c in src["controlos"] if c["categoria"] == code)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    ap.add_argument("--check", action="store_true",
                    help="falha se o JSON em disco não bater com o que o extract produz")
    args = ap.parse_args()

    doc = build(args.repo)
    out = args.repo / OUT_REL
    payload = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"

    if args.check:
        if not out.exists():
            print(f"CHECK FAIL: {out} não existe")
            return 1
        if out.read_text(encoding="utf-8") != payload:
            print(f"CHECK FAIL: {OUT_REL} diverge do extract")
            return 1
        print(f"CHECK OK: {OUT_REL} reproduce-se byte a byte")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload, encoding="utf-8")

    t = doc["tracks"][0]
    print(f"wrote {out.relative_to(args.repo)}")
    print(f"  escala própria: " + " · ".join(
        f"{s['value']}={s['label']}" for s in doc["tracks"][0]["scale"]["states"]))
    print(f"  {len(doc['tiers'])} tiers: " + " · ".join(
        f"{x['nome']} {x['n_medidas']} medidas (risco {x['risco_min']}–{x['risco_max']} → estado {x['state']})"
        for x in doc["tiers"]))
    print(f"  {len(t['functions'])} objectivos · {len(t['categories'])} categorias · "
          f"{len(t['subcategories'])} controlos")
    print(f"  {t['n_measures']} medidas no Anexo III · {t['n_controls_with_measures']} controlos "
          f"com pelo menos uma · {t['escalating_controls']} escalam pelos 3 tiers")
    print(f"  {len(doc['public_measures'].get('B', []))} medidas públicas B · "
          f"{len(doc['public_measures'].get('A', []))} medidas públicas A")
    return 0


if __name__ == "__main__":
    sys.exit(main())