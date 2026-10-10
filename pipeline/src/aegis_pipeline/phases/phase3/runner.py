"""aegis_pipeline.phases.phase3.runner — Phase 3 Part 1 CLI entrypoint and orchestrator.

Builds OBJECTIVE_MAPPING.md and PRINCIPLE_MAPPING.md from Phase 2 deliverables.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from aegis_pipeline.phases.phase3.schemas import (
    ORGANIZATIONAL,
    UNSET,
)
from aegis_pipeline.phases.phase3.skeleton import (
    build,
    domain_names_from,
    load_objectives,
    render_matrix,
    render_principles,
)

REPO = Path(__file__).resolve().parents[5]

S_UNSET = UNSET


def check(rows: list[dict], objectives: list[dict]) -> list[str]:
    """The gates this stage can decide on its own. Empty list = pass."""
    findings = []
    ids = [r["id"] for r in rows]
    expected = [o["id"] for o in objectives]

    missing = set(expected) - set(ids)
    if missing:
        findings.append(f"matrix drops {len(missing)} objective(s): {sorted(missing)[:5]}")
    extra = set(ids) - set(expected)
    if extra:
        findings.append(f"matrix invents {len(extra)} objective(s): {sorted(extra)[:5]}")
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        findings.append(f"matrix repeats {len(dupes)} objective id(s): {dupes[:5]}")

    return findings


def check_anchors(rows: list[dict]) -> list[str]:
    """Post-verdict gate: a row claiming a product carrier must carry anchors."""
    findings = []
    for r in rows:
        claiming = r["verdict"] not in (S_UNSET, ORGANIZATIONAL)
        if claiming and not r["anchors"]:
            findings.append(f"{r['id']} claims a functional carrier but carries no published anchor set")
        if not claiming and r["verdict"] == ORGANIZATIONAL and r["anchors"]:
            continue
    return findings


def resolve_source(args) -> Path:
    if args.source:
        return Path(args.source)
    if args.case:
        return REPO / "cases" / args.case / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md"
    raise SystemExit("one of --source or --case is required")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Phase 3 Part 1: Coverage Skeleton")
    ap.add_argument("--source", help="a Phase 2 Doc01_Operational_Objectives.md")
    ap.add_argument("--case", help="read the hand-authored deliverable of this case")
    ap.add_argument("--out", required=True, help="directory to write the skeleton into")
    args = ap.parse_args(argv)

    source = resolve_source(args)
    if not source.is_file():
        print(f"no Phase 2 deliverable at {source}", file=sys.stderr)
        return 2

    objectives = load_objectives(source)
    if not objectives:
        print(f"no objective rows parsed from {source}", file=sys.stderr)
        return 2

    rows = build(objectives)
    findings = check(rows, objectives)
    if findings:
        for f in findings:
            print(f"  [FAIL] {f}", file=sys.stderr)
        print(f"{len(findings)} finding(s) — skeleton not written", file=sys.stderr)
        return 1

    by_domain: dict[str, list[dict]] = {}
    for r in rows:
        by_domain.setdefault(r["domain"], []).append(r)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "OBJECTIVE_MAPPING.md").write_text(
        render_matrix(rows, by_domain, domain_names_from(REPO / "baseline/domains/index.md")),
        encoding="utf-8",
    )
    (out / "PRINCIPLE_MAPPING.md").write_text(render_principles(), encoding="utf-8")

    sds = sorted({r["subdomain"] for r in rows})
    templated = sum(1 for r in rows if r["criterion_is_template"])
    anchored = sum(1 for r in rows if r["anchors"])
    unanchored = [r["id"] for r in rows if not r["anchors"]]
    print(f"skeleton: {len(rows)} objectives across {len(by_domain)} domains / {len(sds)} sub-domains")
    print(f"  published anchor set: {anchored}/{len(rows)}"
          + (f" — unanchored (process obligations): {', '.join(unanchored)}" if unanchored else ""))
    print(f"  Phase 2 criteria that are the generic template: {templated}/{len(rows)}")
    print(f"  wrote {out/'OBJECTIVE_MAPPING.md'}")
    print(f"  wrote {out/'PRINCIPLE_MAPPING.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
