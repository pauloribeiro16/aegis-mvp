"""A regra de níveis de maturidade do QNRCS, partilhada pelo script e por quem
mais a consuma. Extracção da lógica que estava só em scripts/qnrcs_maturity.py
para poder ser testada e reusada (o Inspector pode vir a consumi-la)."""

from __future__ import annotations

import json
import re
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
        # The attained level is capped by the tier the entity is actually
        # assessed at: an entity at "Básico" (level 2) can reach level 2, not 4,
        # however well anchored its controls are. Uncapped, this reported 4 for
        # a Básico assessment — the instrument over-reporting attainment.
        ceiling = LEVEL_OF_TIER[tier]
        for lv in (4, 3, 2):
            if lv > ceiling:
                continue
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

def run_anchors_of(run_dir: Path) -> set[str]:
    """The NIST CSF ids this run carries.

    The union of two sources: the anchors the Phase 3 chain selected (the
    model's `Chain anchors`, which are what the run actually committed to) and
    the anchors Phase 2 published for the objectives the run selected (the
    control footprint the run was built on).
    """
    out: set[str] = set()
    for path in sorted((run_dir / "steps" / "phase3").glob("proposals_*.json")):
        try:
            blob = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for proposal in blob.get("proposals") or []:
            for a in proposal.get("anchors") or []:
                a = str(a).strip().strip("`")
                if a:
                    out.add(a)
    doc01 = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
    if doc01.is_file():
        for line in doc01.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
            if len(cells) >= 9 and re.match(r"(?:PO|SO)-D-\d{2}\.\d-\d{3}", cells[0]):
                for a in cells[8].split(","):
                    a = a.strip()
                    if a and a != "—":
                        out.add(a)
    return out


def qnrcs_controls(repo: Path) -> list[dict]:
    """The QNRCS measures, as the leaves carry them."""
    out: list[dict] = []
    root = repo / "baseline" / "CONTROLS" / "QNRCS"
    for path in sorted(root.rglob("*.json")):
        if path.name in ("_MANIFEST.json", "_tiers.json", "QNRCS.json"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("control_id"):
            out.append(data)
    return out


def run_maturity(repo: Path, run_dir: Path, tier: str = "basico") -> dict:
    """The QNRCS maturity the run attains, per objective.

    The QNRCS is the national maturity reference and, with NIST CSF 2.0, NIST
    PF and NIST AI RMF, one of the four active referentials (ADR-015 §5). This
    is the number the referential exists to produce, and until this wiring it
    had no producer in the pipeline at all.
    """
    extract = repo / "docs" / "research" / "qnrcs" / "QNRCS_Reg756_2026_extract.json"
    if not extract.is_file():
        return {}
    controls = qnrcs_controls(repo)
    if not controls:
        return {}
    return maturity_levels(extract, controls, tier, run_anchors_of(run_dir))


def render_maturity(report: dict) -> str:
    """The maturity deliverable: one row per objective."""
    if not report:
        return ""
    lines = [
        "---",
        "title: 'QNRCS maturity — the level this run attains'",
        "---",
        "",
        f"Scale: {report.get('escala', '0-4')}. Expected at the entity's tier: "
        f"{report.get('nivel_esperado', '—')}.",
        "",
        "| Objective | Level attained | Coverage by level (2 / 3 / 4) | Controls expected |",
        "|---|---|---|---|",
    ]
    for oid, d in sorted(report.get("objectivos", {}).items()):
        cov = d.get("cobertura_cumulativa", {})
        exp = d.get("controlos_esperados", {})
        lines.append(
            f"| `{oid}` | {d.get('nivel_atingido', 0)} | "
            f"{cov.get('2', 0)}% / {cov.get('3', 0)}% / {cov.get('4', 0)}% | "
            f"{exp.get('2', 0)} / {exp.get('3', 0)} / {exp.get('4', 0)} |"
        )
    if report.get("nota"):
        lines += ["", f"_{report['nota']}_"]
    lines.append("")
    return "\n".join(lines) + "\n"
