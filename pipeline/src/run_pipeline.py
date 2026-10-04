#!/usr/bin/env python3
"""run_pipeline.py — stage driver for the AEGIS-MVP Phase 1 pipeline.

Stages (each normally one SLURM job, stopped at its human gate):
  p1   extract facts                       -> steps/fact_sheet.yaml      (gate G-P1-A)
  p2   confirm regulations                 -> steps/verdicts.*           (gate G-P1-B)
  p3   select sub-domain subset            -> steps/selection.*          (gate G-P1-C)
  p3f  build the §2 framing table          -> steps/framing.md
  p4   derive adjusted goals (1 call/sub-domain; anchors code-derived)
  p4t  resolve strategic tensions          -> steps/tensions.* (multi-reg only)
  p5   zero-LLM assembly + validate        -> doc02_adjusted_goals.md, RUN_NOTES.md (gate G-P1-D)

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
import runconfig  # noqa: E402
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
    # The cluster checkout is NOT a git tree (tarball transport, no .git) —
    # that is why EXP-01's arms recorded an empty rev. sync_up.sh stamps the
    # workstation's rev into the payload (.cluster_sync_rev), and that stamp is
    # the authoritative record of which code produced the run.
    rev = (args.git_rev or "").strip()
    if not rev:
        try:
            proc = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo,
                                  capture_output=True, text=True, timeout=10)
            rev = proc.stdout.strip()
        except Exception as e:
            raise SystemExit(
                f"cannot record the code version for this run: git rev-parse failed ({e}).\n"
                f"A run whose aegis_git_rev is blank cannot be reproduced or refuted. "
                f"Pass --git-rev (or sync via pipeline/deucalion/sync_up.sh, which "
                f"stamps .cluster_sync_rev) before starting a run.")
    if not rev:
        # NOT an exception: git on a non-repo directory exits 0 with empty
        # stdout. Silently recording "" produced two uninterpretable runs.
        stamp = repo / ".cluster_sync_rev"
        if stamp.is_file():
            rev = stamp.read_text(encoding="utf-8").strip()
    if not rev:
        raise SystemExit(
            f"no code revision available for {repo}: not a git working tree and "
            f"no .cluster_sync_rev stamp (sync with pipeline/deucalion/sync_up.sh "
            f"first, or pass --git-rev). A run without a recorded rev is not "
            f"evidence-grade.")

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
    # config.json is the run's single declaration of how it was sampled. It is
    # written before any call so that a run that dies at p1 is still
    # self-describing, and it is echoed into the manifest so the setting travels
    # with the artefacts through sync_down.
    cfg = runconfig.write(run_dir, runconfig.DEFAULTS | {
        "model": args.model,
        "ollama_base": args.base,
        "temperature": args.temperature,
        "seed": None if args.seed in ("none", "", None) else int(args.seed),
        "top_p": args.top_p,
        "top_k": args.top_k,
        "arm": args.arm,
        "repeat": args.repeat,
        "preapprove_gates": args.preapprove_gates,
        "case": args.case,
        # EXP-04: per-run prompt variant, recorded with the run so the ablation
        # arm is self-describing rather than inferred from the run name
        "ficha_overrides": {
            k: v for k, v in (
                ("p4_adjustment", args.p4_adjustment),
                ("p3_instruction", args.p3_instruction),
            ) if v
        },
        "aegis_git_rev": rev,
        "created": now_iso(),
    })
    update_manifest(run_dir, run_config=json.loads(cfg.read_text(encoding="utf-8")))
    print(f"run initialised: {run_dir}")
    print(f"config: {runconfig.describe(runconfig.load(run_dir))}")
    print(json.dumps({k: manifest[k] for k in ("run_id", "case_id", "model", "aegis_git_rev")}, indent=1))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    repo: Path = args.repo.resolve()
    run_dir: Path = args.run_dir.resolve()
    if not (run_dir / "manifest.json").exists():
        raise SystemExit(f"not a run directory (manifest.json missing): {run_dir}")

    manifest = json.loads((run_dir / "manifest.json").read_text())
    model = args.model or manifest["model"]

    if args.stage == "agentic":
        from agent.loop import AgentRunner
        runner = AgentRunner(repo, run_dir, model, args.base,
                             transport=os.environ.get("AEGIS_AGENT_TRANSPORT", "tools"),
                             max_turns=int(os.environ.get("AEGIS_AGENT_MAX_TURNS", "80")),
                             dry_run=args.dry_run)
        n_calls_before = count_calls(run_dir)
        print(f"=== stage agentic (model={model}, transport={runner.transport}, "
              f"max_turns={runner.max_turns}, dry_run={args.dry_run}) ===", flush=True)
        try:
            n = runner.stage_agentic()
        except Exception as e:
            update_manifest(
                run_dir, mode="agentic",
                stage_history={"stage": "agentic", "ts": now_iso(),
                               "job_id": os.environ.get("SLURM_JOB_ID"),
                               "node": os.environ.get("SLURM_NODELIST"),
                               "n_calls": count_calls(run_dir) - n_calls_before,
                               "status": "aborted",
                               "error": f"{type(e).__name__}: {e}"[:500]},
                n_calls_total=count_calls(run_dir), model=model)
            raise
        update_manifest(
            run_dir, mode="agentic",
            stage_history={"stage": "agentic", "ts": now_iso(),
                           "job_id": os.environ.get("SLURM_JOB_ID"),
                           "node": os.environ.get("SLURM_NODELIST"),
                           "n_calls": n, "status": "ok"},
            n_calls_total=count_calls(run_dir), model=model)
        print(f"=== stage agentic done: {n} turn(s); run total "
              f"{count_calls(run_dir)} ===", flush=True)
        return 0

    runner = StepRunner(repo, run_dir, model, args.base, dry_run=args.dry_run)

    combos = {"p4p5": ["p4", "p4t", "p5"], "p4tp5": ["p4t", "p5"],
              # every stage after the one that creates the run directory.
              # p1 stays separate because it is what writes the manifest and
              # config.json; everything else is a pure function of those.
              "all": ["p2", "p3", "p3f", "p4", "p4t", "p5"]}
    stages = combos.get(args.stage, [args.stage])
    # Unattended mode: the gate check is an existence test on a marker file
    # whose content is never parsed, so writing the markers up front is three
    # touches. That turns a human quality control into a rubber stamp and must
    # be declared as a fixed, identical experimental condition — never used
    # silently, and never for the golden run.
    if runconfig.load(run_dir).get("preapprove_gates"):
        gates_dir = run_dir / "steps" / "gates"
        gates_dir.mkdir(parents=True, exist_ok=True)
        for g in ("G-P1-A", "G-P1-B", "G-P1-C"):
            marker = gates_dir / f"{g}.approved"
            if not marker.exists():
                marker.write_text(
                    "preapproved: unattended experimental run "
                    "(PREREG_01 fixed condition — identical across all arms)\n",
                    encoding="utf-8")
        print(f"[gates] pre-approved A/B/C for unattended run in {run_dir}", flush=True)
    n_calls_before = count_calls(run_dir)
    for stage in stages:
        print(f"=== stage {stage} (model={model}, dry_run={args.dry_run}) ===", flush=True)
        try:
            n = getattr(runner, f"stage_{stage}")()
        except Exception as e:
            # record the abort: without this the manifest claims the run only
            # ever contained stages that succeeded, and the failed one is
            # visible only in the run log
            update_manifest(
                run_dir,
                stage_history={"stage": stage, "ts": now_iso(),
                               "job_id": os.environ.get("SLURM_JOB_ID"),
                               "node": os.environ.get("SLURM_NODELIST"),
                               "n_calls": count_calls(run_dir) - n_calls_before,
                               "status": "aborted",
                               "error": f"{type(e).__name__}: {e}"[:500]},
                n_calls_total=count_calls(run_dir),
                model=model,
            )
            raise
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
              f"{count_calls(run_dir)} ===", flush=True)
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
    p_new.add_argument("--temperature", type=float, default=0.2,
                       help="sampling temperature; recorded per run (EXP-02 arm C uses 0.0)")
    p_new.add_argument("--seed", default="42",
                       help="RNG seed, or the literal 'none' to run UNSEEDED. "
                            "Seeded is the default because EXP-02 measured the "
                            "pipeline as bit-reproducible under a fixed seed "
                            "(and ~40% abort-prone without one); 'no seed sent' "
                            "must therefore be explicit, never accidental")
    p_new.add_argument("--top-p", type=float, default=None)
    p_new.add_argument("--top-k", type=int, default=None)
    p_new.add_argument("--arm", default=None,
                       help="experimental arm label, e.g. A/B/C — lets the "
                            "aggregator group runs without parsing run ids")
    p_new.add_argument("--repeat", type=int, default=None,
                       help="repeat index within the arm")
    p_new.add_argument("--p4-adjustment", default=None, choices=["menu"],
                       help="EXP-04 arm: swap the P4 adjustment decision rule for "
                            "the closed 3-value menu")
    p_new.add_argument("--p3-instruction", default=None, choices=["clarified"],
                       help="EXP-M01: p3 prompt-engineered variant for the models "
                            "that failed the selection contract (glm, nemotron)")
    p_new.add_argument("--git-rev", default=None,
                       help="code revision override (the cluster checkout has "
                            "no .git; sync_up.sh stamps .cluster_sync_rev)")
    p_new.add_argument("--preapprove-gates", action="store_true",
                       help="write the G-P1-A/B/C markers so the run proceeds "
                            "unattended. Fixed experimental condition, not a "
                            "convenience for ordinary runs.")

    p_run = sub.add_parser("run", help="execute one stage")
    p_run.add_argument("--stage", required=True,
                       choices=["p1", "p2", "p3f", "p3", "p4", "p4t", "p5",
                                "p4p5", "p4tp5", "all", "agentic"])
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
