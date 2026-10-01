#!/usr/bin/env python3
"""run_pipeline.py — stage driver for the AEGIS-MVP Phase 1 pipeline.

Stages (each normally one SLURM job, stopped at its human gate):
  p1   extract facts                       -> steps/fact_sheet.yaml      (gate G-P1-A)
  p2   confirm regulations                 -> steps/verdicts.*           (gate G-P1-B)
  p3   select sub-domain subset            -> steps/selection.*          (gate G-P1-C)
  p4   derive adjusted goals (1 call/sub-domain)
  p5   render + validate                   -> phase1_output.md, RUN_NOTES.md (gate G-P1-D)

State lives on disk (ADR-010 D5): each stage re-enters from the run
directory's recorded predecessors. Human gate approvals are marker files
steps/gates/G-P1-X.approved written during local review and synced up.

Usage:
  python3 run_pipeline.py new-run --repo <aegis-mvp> --case Case_01_TinyTask_SaaS \
      --run-dir <dir> --model qwen3.8:27b --base http://127.0.0.1:11434
  python3 run_pipeline.py run --stage p1 --run-dir <dir> --repo <aegis-mvp> \
      --base http://127.0.0.1:11434 [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from compose import parse_ficha, FICHA_FILES  # noqa: E402
from steps import NUM_CTX, StepRunner  # noqa: E402
from trace import count_calls, now_iso, update_manifest  # noqa: E402

REPO_DEFAULT = Path(__file__).resolve().parents[2]


def cmd_new_run(args: argparse.Namespace) -> int:
    repo: Path = args.repo.resolve()
    run_dir: Path = args.run_dir.resolve()
    case_dir = repo / "pipeline" / "cases" / args.case
    if not (case_dir / "case.yaml").exists():
        raise SystemExit(f"case binding not found: {case_dir / 'case.yaml'}")
    if run_dir.exists() and (run_dir / "manifest.json").exists():
        raise SystemExit(f"run already initialised: {run_dir}")
    for sub in ("inputs", "outputs", "packs", "steps/goals", "steps/gates", "logs"):
        (run_dir / sub).mkdir(parents=True, exist_ok=True)

    import subprocess
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo,
                             capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        rev = "unknown"

    ficha_versions = {}
    for step, fname in FICHA_FILES.items():
        f = parse_ficha(repo / "docs" / "pipeline" / "prompts" / fname)
        ficha_versions[step] = f"{f['id']} v{f['version']}"

    manifest = update_manifest(
        run_dir,
        run_id=run_dir.name,
        case_id=args.case,
        model=args.model,
        ollama_base=args.base,
        num_ctx_policy={k: v for k, v in NUM_CTX.items()},
        ficha_versions=ficha_versions,
        aegis_git_rev=rev,
        hostname=os.uname().nodename,
        stage_history=[],
        n_calls_total=0,
        created=now_iso(),
    )
    print(f"run initialised: {run_dir}")
    print(json.dumps({k: manifest[k] for k in ("run_id", "case_id", "model", "aegis_git_rev")}, indent=1))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    repo: Path = args.repo.resolve()
    run_dir: Path = args.run_dir.resolve()
    if not (run_dir / "manifest.json").exists():
        raise SystemExit(f"not a run directory (manifest.json missing): {run_dir}")

    manifest = json.loads((run_dir / "manifest.json").read_text())
    model = args.model or manifest["model"]
    runner = StepRunner(repo, run_dir, model, args.base, dry_run=args.dry_run)

    stages = ["p4", "p5"] if args.stage == "p4p5" else [args.stage]
    n_calls_before = count_calls(run_dir)
    for stage in stages:
        print(f"=== stage {stage} (model={model}, dry_run={args.dry_run}) ===", flush=True)
        n = getattr(runner, f"stage_{stage}")()
        update_manifest(
            run_dir,
            stage_history={"stage": stage, "ts": now_iso(),
                           "job_id": os.environ.get("SLURM_JOB_ID"),
                           "node": os.environ.get("SLURM_NODELIST"),
                           "n_calls": n,
                           "status": "dry-run" if args.dry_run else "ok"},
            n_calls_total=count_calls(run_dir),
            model=model,
        )
        print(f"=== stage {stage} done: {n} call(s); run total "
              f"{count_calls(run_dir) - n_calls_before + n_calls_before} ===", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new-run", help="initialise a run directory")
    p_new.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    p_new.add_argument("--case", required=True)
    p_new.add_argument("--run-dir", type=Path, required=True)
    p_new.add_argument("--model", default="qwen3.8:27b")
    p_new.add_argument("--base", default="http://127.0.0.1:11434")

    p_run = sub.add_parser("run", help="execute one stage")
    p_run.add_argument("--stage", required=True, choices=["p1", "p2", "p3", "p4", "p5", "p4p5"])
    p_run.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    p_run.add_argument("--run-dir", type=Path, required=True)
    p_run.add_argument("--model", default=None)
    p_run.add_argument("--base", default="http://127.0.0.1:11434")
    p_run.add_argument("--dry-run", action="store_true",
                       help="compose prompts and packs only; no model call")

    args = ap.parse_args()
    if args.cmd == "new-run":
        return cmd_new_run(args)
    return cmd_run(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (SystemExit,):
        raise
    except Exception as e:  # forensics: stage aborts loudly, artifacts stay on disk
        print(f"STAGE ABORTED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
