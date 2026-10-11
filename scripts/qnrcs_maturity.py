#!/usr/bin/env python3
"""qnrcs_maturity.py — the QNRCS maturity comparison for one run.

Deterministic, zero model calls. Reads the run's goals (their baseline sources),
re-derives the published anchor set per goal (CSF 2.0 + PF for GDPR — the same
`goal_anchors()` the pipeline renders), and contrasts it with the QNRCS
(baseline/CONTROLS/QNRCS/) via each control's normalized `mapped_nist_csf`
bridge. The entity tier comes from the fact sheet profile when derivable, or
`--tier` explicitly; default is `basico` (the proportional tier for a
micro-entity).

Outputs (into <run>/outputs/phase3/maturity/):
  qnrcs_maturity.json — the machine report (coverage per objective, gaps, tier)
  qnrcs_maturity.md   — the human table (the Inspector's Documento tab renders it)

Usage: python3 scripts/qnrcs_maturity.py --repo <repo> --run <run_dir> [--tier basico]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_DEFAULT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_DEFAULT / "pipeline" / "src"))

TIERS = ("basico", "substancial", "elevado")


def run_anchor_sets(repo: Path, run: Path) -> dict[str, set[str]]:
    """Goal id → the anchors the pipeline publishes for it (CSF+PF, R8-aware)."""
    from aegis_pipeline.guards.controls import goal_anchors

    out: dict[str, set[str]] = {}
    for path in sorted((run / "steps" / "goals").glob("D-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for goal in data.get("goals") or []:
            source = (goal.get("baseline_source") or "").strip()
            if not source:
                continue
            try:
                out[goal["id"]] = set(goal_anchors(repo, data["subdomain"], [source]))
            except (ValueError, KeyError) as e:
                print(f"  [aviso] {goal['id']}: {e}", file=sys.stderr)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    ap.add_argument("--run", type=Path, required=True)
    ap.add_argument("--tier", choices=TIERS, default=None,
                    help="default: basico (the proportional tier for a micro-entity)")
    args = ap.parse_args()
    repo, run = args.repo.resolve(), args.run.resolve()

    qnrcs_dir = repo / "baseline" / "CONTROLS" / "QNRCS"
    manifest = json.loads((qnrcs_dir / "_MANIFEST.json").read_text(encoding="utf-8"))
    tiers_doc = json.loads((qnrcs_dir / "_tiers.json").read_text(encoding="utf-8"))
    tier = args.tier or "basico"
    tier_measures = tiers_doc["tiers"][tier]

    anchors = run_anchor_sets(repo, run)
    all_anchors: set[str] = set().union(*anchors.values()) if anchors else set()
    csf_anchors = {a for a in all_anchors if not a.endswith(tuple(f"-P{i}" for i in range(1, 20)))}

    controls = []
    for path in sorted(qnrcs_dir.rglob("*.json")):
        if path.name in ("_MANIFEST.json", "QNRCS.json", "_tiers.json"):
            continue
        controls.append(json.loads(path.read_text(encoding="utf-8")))

    covered_by_fn: dict[str, dict] = {}
    gaps: list[dict] = []
    per_control = []
    for control in controls:
        fn = control["function"]
        mapped = control.get("mapped_nist_csf") or []
        hit = bool(mapped) and bool(csf_anchors & set(mapped))
        entry = {"id": control["control_id"], "function": fn, "mapped_nist_csf": mapped, "covered": hit}
        per_control.append(entry)
        fn_key = fn.split(" — ")[0]
        stat = covered_by_fn.setdefault(fn_key, {"n": 0, "covered": 0})
        stat["n"] += 1
        stat["covered"] += int(hit)
        if not hit:
            measure = next(
                (m for m in tiers_doc["tiers"][tier] if m.get("control_id") == control["control_id"]),
                None,
            )
            gaps.append({
                "control": control["control_id"],
                "titulo": control["subcategory_text"],
                "medida": (measure or {}).get("medida", ""),
            })

    objectives = {
        oid: {"nome": meta["nome"],
              "cobertura": round(100 * stat["covered"] / stat["n"], 1),
              "controlos_cobertos": stat["covered"],
              "controlos_total": stat["n"]}
        for oid, meta in manifest["objectives"].items()
        for stat in [covered_by_fn.get(oid, {"n": 0, "covered": 0})]
        if stat["n"] > 0
    }
    n_covered = sum(1 for c in per_control if c["covered"])
    report = {
        "run": run.name,
        "referencial": manifest["version"],
        "tier": tier,
        "tier_note": "o tier define O QUE SE ESPERA atingir; a cobertura mede o que os requisitos publicados já ancoram",
        "resumo": {
            "controlos_qnrcs": len(per_control),
            "cobertos": n_covered,
            "cobertura_geral_pct": round(100 * n_covered / max(len(per_control), 1), 1),
            "objectivos": objectives,
        },
        "gaps_do_tier": gaps,
        "metodo": "um controlo QNRCS conta-se coberto quando algum dos seus mapped_nist_csf está no conjunto de âncoras publicado pela corrida (goal_anchors, CSF+PF)",
    }
    out_dir = run / "outputs" / "phase3" / "maturity"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "qnrcs_maturity.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    lines = [
        "---",
        f"title: 'QNRCS — comparação de maturidade ({run.name})'",
        "generated_by: 'scripts/qnrcs_maturity.py'",
        f"tier: {tier}",
        "---",
        "",
        f"# QNRCS — maturidade da corrida `{run.name}`",
        "",
        f"Tier de entidade: **{tier}** · cobertura geral: **{report['resumo']['cobertura_geral_pct']}%** "
        f"({report['resumo']['cobertos']}/{report['resumo']['controlos_qnrcs']} controlos).",
        "",
        "| Objectivo | Cobertura | Controlos cobertos |",
        "|---|---|---|",
    ]
    for oid, obj in objectives.items():
        lines.append(f"| {oid} — {obj['nome']} | {obj['cobertura']}% | {obj['controlos_cobertos']}/{obj['controlos_total']} |")
    lines += ["", f"## Gaps do tier `{tier}` ({len(gaps)})", ""]
    for gap in gaps:
        medida = f" — medida: {gap['medida']}" if gap["medida"] else ""
        lines.append(f"- `{gap['control']}` — {gap['titulo']}{medida}")
    lines.append("")
    (out_dir / "qnrcs_maturity.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"maturidade: {report['resumo']['cobertura_geral_pct']}% "
          f"({report['resumo']['cobertos']}/{report['resumo']['controlos_qnrcs']}) tier={tier} "
          f"→ {out_dir / 'qnrcs_maturity.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
