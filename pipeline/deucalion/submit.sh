#!/usr/bin/env bash
# submit.sh — submit one pipeline stage (run ON the Deucalion login node).
# Usage: bash pipeline/deucalion/submit.sh <stage> [case]
#   stage: p1 | p2 | p3 | p4 | p5 | p4p5
#   case:  pipeline/cases/<case> name (default Case_01_TinyTask_SaaS; only
#          needed when the run directory is created, i.e. stage p1)
# Env overrides: MVP_RUN_TAG (required), MVP_MODEL (default qwen3.8:27b)
set -euo pipefail

STAGE="${1:?stage required: p1|p2|p3|p4|p5|p4p5}"
CASE="${2:-Case_01_TinyTask_SaaS}"
MODEL="${MVP_MODEL:-qwen3.8:27b}"
RUN_TAG="${MVP_RUN_TAG:?set MVP_RUN_TAG=<short tag> (e.g. case01)}"

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
mkdir -p runs

TIME=00:30:00
case "$STAGE" in
  p3) TIME=00:45:00 ;;
  p4|p4p5) TIME=02:00:00 ;;
esac

# Continuing an existing run: export MVP_RUN_ID=run_<tag>_<first-JOBID> so the
# job reuses that run directory; a fresh p1 job derives run_<tag>_<own JOBID>.
EXTRA_RUN_ID=""
[ -n "${MVP_RUN_ID:-}" ] && EXTRA_RUN_ID=",MVP_RUN_ID=${MVP_RUN_ID}"

sbatch -J "mvp_${STAGE}" --time="$TIME" \
  --export=ALL,STAGE="${STAGE}",CASE="${CASE}",MODEL="${MODEL}",RUN_TAG="${RUN_TAG}${EXTRA_RUN_ID}" \
  pipeline/deucalion/phase1.sbatch
echo "monitor: squeue -u \$USER ; then tail the run log under runs/run_${RUN_TAG}_<JOB>/logs/"
