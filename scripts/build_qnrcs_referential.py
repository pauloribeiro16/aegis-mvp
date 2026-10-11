#!/usr/bin/env python3
"""build_qnrcs_referential.py — derive baseline/CONTROLS/QNRCS/ from the extract.

Deterministic build from `docs/research/qnrcs/QNRCS_Reg756_2026_extract.json`
(the investigator's QNRCS dashboard, Regulamento n.º 756/2026). Produces the
ENISA-format advisory referential plus the tier sidecar that makes QNRCS the
maturity reference: measures per entity tier (básico/substancial/elevado) and
the risk matrix that selects the tier from a company profile.

Idempotent: re-running rebuilds the tree. Ids stay in their national form
(`DE.AE-1`) — the NIST CSF bridge lives in the normalized `mapped_nist_csf`
field, never in a rename.

Usage: python3 scripts/build_qnrcs_referential.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXTRACT = REPO / "docs/research/qnrcs/QNRCS_Reg756_2026_extract.json"
OUT = REPO / "baseline" / "CONTROLS" / "QNRCS"
CSF_UNIVERSE = REPO / "baseline" / "CONTROLS" / "NIST_CSF_2.0" / "CSF_2.0.json"

# ruído do parser do dashboard nas colunas ISO/CIS que vazou para nistcsf
NOISE_TOKENS = {"1", "3", "4", "8", "CIS", "CSC", "V8.1", "—", ""}
# códigos apresentados como nistcsf que são do CyFun nacional (sem zero-padding no CSF 2.0)
CYFUN_CODES = {"GV.CO-03", "RC.PR-03"}


def normalize_csf(tokens: list[str], csf_ids: set[str]) -> list[str]:
    """Zero-pad to CSF 2.0 form and drop parser noise / CyFun-only codes."""
    out: list[str] = []
    for token in tokens:
        t = str(token).strip()
        if not t or t.upper() in {n.upper() for n in NOISE_TOKENS}:
            continue
        if t in CYFUN_CODES:
            continue
        m = re.match(r"^([A-Z]{2})\.([A-Z]{2})-(\d+)$", t)
        if not m:
            print(f"  [aviso] token nistcsf não reconhecido, descartado: {t!r}")
            continue
        fn, cat, num = m.groups()
        normalized = f"{fn}.{cat}-{num.zfill(2)}"
        if normalized not in csf_ids:
            print(f"  [aviso] {t} → {normalized} não existe no CSF 2.0, descartado")
            continue
        if normalized not in out:
            out.append(normalized)
    return out


def main() -> int:
    extract = json.loads(EXTRACT.read_text(encoding="utf-8"))
    csf = json.loads(CSF_UNIVERSE.read_text(encoding="utf-8"))
    csf_ids = {s["id"] if isinstance(s, dict) else s for s in csf["subcategories"]}

    objectives = {o["id"]: o for o in extract["objetivos"]}
    categories = {c["code"]: c for c in extract["categorias"]}
    controls = extract["controlos"]
    tiers = extract["medidas_essenciais_importantes"]
    risk = extract["matriz_risco"]

    if OUT.exists():
        for child in OUT.iterdir():
            if child.is_dir():
                for f in child.iterdir():
                    f.unlink()
                child.rmdir()
            else:
                child.unlink()

    warnings = 0
    ids_written: list[str] = []
    for control in controls:
        oid = control["objetivo"]
        obj = objectives[oid]
        cat = categories[control["categoria"]]
        refs = control.get("refs") or {}
        mapped = normalize_csf(list(refs.get("nistcsf") or []), csf_ids)
        warnings += len(refs.get("nistcsf") or []) - len(mapped)
        doc = {
            "control_id": control["id"],
            "framework": "QNRCS",
            "version": "Regulamento n.º 756/2026 (DR 2.ª série 118, 22-06-2026)",
            "function": f"{oid} — {obj['nome']}",
            "category": f"{control['categoria']} — {cat['nome']}",
            "subcategory_id": control["id"],
            "subcategory_text": control["titulo"],
            "description": control["descricao"],
            "informative_references": sorted(
                {f"ISO/IEC 27001:{x}" for x in refs.get("iso27001") or []}
                | {f"ISO/IEC 27002:{x}" for x in refs.get("iso27002") or []}
                | {f"NIST SP 800-53:{x}" for x in refs.get("nist80053") or []}
            ),
            "mapped_nist_csf": mapped,
            "mapped_cyfun": sorted(refs.get("cyfun") or []),
            "mapped_cis": sorted(str(x) for x in refs.get("cis") or []),
            "implementation_examples": [],
            "assessment_objectives": [],
            "related_controls": [],
            "source_url": "https://www.cncs.gov.pt/pt/quadro-nacional",
            "source_version": "QNRCS (Regulamento n.º 756/2026; base: DL 125/2025 — RJC, transposição NIS 2)",
        }
        target = OUT / oid
        target.mkdir(parents=True, exist_ok=True)
        (target / f"{control['id']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        ids_written.append(control["id"])

    manifest = {
        "referential": "QNRCS — Quadro Nacional de Referência de Cibersegurança",
        "version": "Regulamento n.º 756/2026 (DR 2.ª série 118, 22-06-2026; base legal DL 125/2025 — RJC, transposição NIS 2)",
        "subcategories": len(ids_written),
        "expected_total": len(controls),
        "unverified_entries": [],
        "advisory": True,
        "enforced_by_verify_no_loss": False,
        "tier": "T2 (ADR-001 D2 — operationalization of a national regulator)",
        "objectives": {o["id"]: {"nome": o["nome"], "categorias": o["categorias"]} for o in extract["objetivos"]},
        "maturity_note": "QNRCS é o referencial de maturidade do projecto: cada controlo tem medidas escalonadas por tier de entidade (básico/substancial/elevado) em _tiers.json, e a matriz de risco que escolhe o tier a partir do perfil da empresa.",
        "built_from": "docs/research/qnrcs/QNRCS_Reg756_2026_extract.json",
        "built_by": "scripts/build_qnrcs_referential.py",
    }
    (OUT / "_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (OUT / "QNRCS.json").write_text(
        json.dumps(
            {
                "framework": "QNRCS",
                "version": manifest["version"],
                "note": "advisory referential; ids authoritative; not enforced by scripts/verify_no_loss.py; the maturity reference of the project (tiers + risk matrix in _tiers.json)",
                "subcategories": ids_written,
                "objectives": manifest["objectives"],
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    (OUT / "_tiers.json").write_text(
        json.dumps(
            {
                "note": "medidas escalonadas por tier de entidade — o mecanismo de maturidade do QNRCS; o tier escolhe-se pela matriz_risco (dimensões G/M/P, sectores, limiares)",
                "tiers": tiers,
                "matriz_risco": risk,
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    n_mapped = sum(
        len(json.loads(p.read_text(encoding="utf-8")).get("mapped_nist_csf") or [])
        for p in OUT.rglob("*.json")
        if p.name not in ("_MANIFEST.json", "QNRCS.json", "_tiers.json")
    )
    print(f"referencial construído: {len(ids_written)} controlos em {OUT}")
    print(f"mapeamentos nistcsf normalizados: {n_mapped} (avisos de descarte: {warnings})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
