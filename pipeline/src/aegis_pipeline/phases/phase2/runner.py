#!/usr/bin/env python3
"""aegis_pipeline.phases.phase2.runner — CLI entrypoint and runner for Phase 2."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Ensure pipeline/src is importable
_src = Path(__file__).resolve().parents[3]
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from compose import confirmed_regulations
from aegis_pipeline.phases.phase2.principles import (
    UNSET,
    grounding_ratio,
    principles_for,
)
from aegis_pipeline.phases.phase2.derivation import (
    build,
    check,
    check_doc02,
)
from aegis_pipeline.phases.phase2.renderers import (
    _case_id,
    _fact_sheet,
    render_doc01,
    render_doc02,
)

REPO_DEFAULT = Path(__file__).resolve().parents[5]


def _confirmed(run_dir: Path) -> list[str]:
    try:
        return confirmed_regulations(run_dir)
    except (FileNotFoundError, OSError, ValueError, KeyError):
        return []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Phase 2: Operationalization & Engineering Rules")
    ap.add_argument("--run-dir", required=True, type=Path, help="a Phase 1 run directory (steps/goals/*.json)")
    ap.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    ap.add_argument("--out", type=Path, help="write Doc01/Doc02 here (default: stdout summary only)")
    ap.add_argument("--json", action="store_true", help="emit derived rows as JSON")
    args = ap.parse_args(argv)

    repo, run_dir = args.repo.resolve(), args.run_dir.resolve()
    if not (run_dir / "steps" / "goals").is_dir():
        print(f"error: {run_dir} has no steps/goals/ — not a Phase 1 run dir", file=sys.stderr)
        return 2

    rows = build(repo, run_dir)
    findings = check(rows, run_dir)

    principles = principles_for(run_dir)
    findings += check_doc02(repo, run_dir, principles)
    ratio = grounding_ratio(principles, _fact_sheet(run_dir))

    if args.json:
        print(json.dumps(
            {"objectives": rows, "principles": principles, "grounding_ratio": ratio},
            indent=1, ensure_ascii=False,
        ))
        return 1 if findings else 0

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "Doc01_Operational_Objectives.md").write_text(
            render_doc01(repo, run_dir, rows), encoding="utf-8"
        )
        (args.out / "Doc02_Secure_Design_Principles.md").write_text(
            render_doc02(repo, run_dir, principles), encoding="utf-8"
        )

    seams = {
        c: sum(1 for r in rows if r[c] == UNSET)
        for c in ("scope", "criteria", "method", "owner", "anchors")
    }
    unseamed_prin = sum(1 for p in principles if str(p.get("constraint", "")) in ("", UNSET))
    print(f"objectives: {len(rows)}   sub-domains: {len({r['subdomain'] for r in rows})}")
    print(f"confirmed regulations: {_confirmed(run_dir) or 'not recorded in this run'}")
    print(f"unseamed cells: {seams}")
    print(f"doc02 constraints unseamed: {unseamed_prin}/7   grounding_ratio: {ratio}")
    if findings:
        print(f"GATE FAIL ({len(findings)}):")
        for f in findings[:20]:
            print(f"  - {f}")
        return 1
    print("gates: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
