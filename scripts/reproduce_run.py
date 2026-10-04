#!/usr/bin/env python3
"""reproduce_run.py — re-execute a recorded pipeline run from its own state.

The repo's internal artifact badge (AGENTS.md §-2; SM-003 / ACM functional
badge): reads a run's manifest.json + config.json, re-creates the run with the
same case/model/seed/temperature, re-executes p1..p5, and diffs the
deterministic artifacts byte a byte against the original.

Requires a serving stack — this script does NOT start Ollama. Point
--base at a running server (local `ollama serve`, or a cluster job's
OLLAMA_BASE from the original run's logs). Gates are pre-approved on the
reproduction (declared condition, as in every preregistered battery).

Usage::

    python scripts/reproduce_run.py --run-dir ~/Work/aegis-runs/run_exp02_b_r01_1978488 \\
        --base http://127.0.0.1:11434

Exit 0 iff every compared artifact is byte-identical; 2 if any differs; 1 on
setup failure. Reproduction runs live OUTSIDE the repo (aegis-runs convention).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

COMPARE = ["doc02_adjusted_goals.md",
           "steps/fact_sheet.yaml", "steps/verdicts.json",
           "steps/selection.json", "steps/tensions.json"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def run_stage(stage: str, run_dir: Path, base: str, repo: Path) -> int:
    cmd = [sys.executable, "pipeline/src/run_pipeline.py", "run",
           "--stage", stage, "--repo", str(repo),
           "--run-dir", str(run_dir), "--base", base]
    print(f"[reproduce] stage {stage} …", flush=True)
    r = subprocess.run(cmd, cwd=repo)
    return r.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run-dir", required=True, type=Path, help="original run directory")
    ap.add_argument("--base", required=True, help="Ollama base URL (script does not serve the model)")
    ap.add_argument("--repo", type=Path, default=REPO)
    ap.add_argument("--keep", action="store_true", help="keep the reproduction run dir")
    args = ap.parse_args()

    orig = args.run_dir.resolve()
    manifest_path = orig / "manifest.json"
    config_path = orig / "config.json"
    if not manifest_path.exists() or not config_path.exists():
        print(f"FATAL: {orig} has no manifest.json/config.json", file=sys.stderr)
        return 1
    manifest = json.loads(manifest_path.read_text())
    config = json.loads(config_path.read_text())
    case_id = manifest.get("case_id")
    model = manifest.get("model")
    seed = config.get("sampler_seed")
    temperature = config.get("sampler_temperature")
    if not case_id or not model:
        print("FATAL: manifest missing case_id/model", file=sys.stderr)
        return 1
    if seed is None:
        print("FATAL: original run was UNSEEDED — reproduction is meaningless "
              "without a fixed seed (AGENTS.md §-1)", file=sys.stderr)
        return 1

    git_rev = manifest.get("aegis_git_rev", "")
    if git_rev:
        try:
            current = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                     cwd=args.repo, capture_output=True, text=True).stdout.strip()
            if current and current != git_rev:
                print(f"WARN: original run built from {git_rev}, repo is at {current} "
                      f"— a diff may be the code, not the method")
        except Exception:
            pass

    tag = f"repro_{orig.name}_{int(time.time())}"
    repro_root = orig.parent
    repro_dir = repro_root / tag
    print(f"[reproduce] case={case_id} model={model} seed={seed} temp={temperature}")
    print(f"[reproduce] new run: {repro_dir}")

    new_run = subprocess.run(
        [sys.executable, "pipeline/src/run_pipeline.py", "new-run",
         "--repo", str(args.repo), "--case", str(case_id),
         "--run-dir", str(repro_dir), "--model", str(model), "--base", args.base,
         "--seed", str(seed), "--temperature", str(temperature),
         "--preapprove-gates"],
        cwd=args.repo)
    if new_run.returncode != 0:
        print("FATAL: new-run failed", file=sys.stderr)
        return 1

    for stage in ("p1", "p2", "p3", "p3f", "p4", "p4t", "p5"):
        rc = run_stage(stage, repro_dir, args.base, args.repo)
        if rc != 0:
            print(f"FATAL: stage {stage} exited {rc} — reproduction aborted; "
                  f"run dir kept: {repro_dir}", file=sys.stderr)
            return 1

    print("\n== diff ==")
    all_ok = True
    rows = []
    for rel in COMPARE:
        a, b = orig / rel, repro_dir / rel
        if not a.exists() or not b.exists():
            rows.append((rel, "MISSING", "", ""))
            all_ok = False
            continue
        sa, sb = sha(a), sha(b)
        rows.append((rel, "identical" if sa == sb else "DIFFERS", sa, sb))
        if sa != sb:
            all_ok = False
    goals_ok = True
    if (orig / "steps/goals").exists() and (repro_dir / "steps/goals").exists():
        for jf in sorted((orig / "steps/goals").glob("*.json")):
            other = repro_dir / "steps/goals" / jf.name
            sa = sha(jf)
            sb = sha(other) if other.exists() else "—"
            rows.append((f"steps/goals/{jf.name}", "identical" if sa == sb else "DIFFERS", sa, sb))
            if sa != sb:
                goals_ok = False
    all_ok = all_ok and goals_ok
    for rel, verdict, sa, sb in rows:
        print(f"  {verdict:<9} {rel}  {sa} / {sb}")
    print(f"\nRESULT: {'REPRODUCED — byte-identical' if all_ok else 'NOT REPRODUCED'}")

    if not args.keep:
        shutil.rmtree(repro_dir, ignore_errors=True)
        print("(reproduction run dir removed; --keep to retain)")
    else:
        print(f"(kept: {repro_dir})")
    return 0 if all_ok else 2


if __name__ == "__main__":
    sys.exit(main())
