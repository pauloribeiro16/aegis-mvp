#!/usr/bin/env bash
# submit.sh — submit one pipeline stage (run ON the Deucalion login node).
# Usage: bash pipeline/deucalion/submit.sh <stage> [case]
#   stage: p1 | p2 | p3 | p3f | p4 | p4t | p5 | p4p5 | all | agentic
#          p4p5 = p4 -> p4t -> p5 in one job
#          all   = p2 -> p3 -> p3f -> p4 -> p4t -> p5 in one job (gates must be
#                 pre-approved, or the run stops at the first one)
#          agentic = the directed tool-calling agent runs the whole task
#   case:  pipeline/cases/<case> name (default Case_01_TinyTask_SaaS; only
#          needed when the run directory is created, i.e. stage p1)
# Env overrides: MVP_RUN_TAG (required), MVP_RUN_ID (continue an existing run),
#                MVP_MODEL (default qwen3.8:27b),
#                AEGIS_AGENT_TRANSPORT (tools|text), AEGIS_AGENT_MAX_TURNS,
#                MVP_TEMPERATURE, MVP_SEED, MVP_TOP_P, MVP_TOP_K,
#                MVP_ARM, MVP_REPEAT, MVP_PREAPPROVE_GATES
# The MVP_* sampler knobs are consumed by stage p1 (which writes config.json)
# and are ignored on later stages: the config is read back from the run dir, so
# a resumed stage cannot be silently re-sampled with different settings.
set -euo pipefail

STAGE="${1:?stage required: p1|p2|p3|p3f|p4|p4t|p5|p4p5|all|agentic}"
CASE="${2:-Case_01_TinyTask_SaaS}"
MODEL="${MVP_MODEL:-qwen3.8:27b}"
RUN_TAG="${MVP_RUN_TAG:?set MVP_RUN_TAG=<short tag> (e.g. case01)}"

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
mkdir -p runs

# Validate before queueing: an unknown stage would otherwise start a GPU job
# (and an Ollama server) only for run_pipeline.py's argparse to reject it.
case "$STAGE" in
  p1|p2|p3|p3f|p4|p4t|p5|p4p5|all|agentic) ;;
  *) echo "FATAL: unknown stage '$STAGE' (expected: p1|p2|p3|p3f|p4|p4t|p5|p4p5|all|agentic)" >&2
     exit 2 ;;
esac

TIME=00:30:00
case "$STAGE" in
  p3|p3f) TIME=00:45:00 ;;
  p4t)    TIME=00:45:00 ;;
  p4|p4p5) TIME=03:00:00 ;;  # 1 call per selected sub-domain, sequential + render
  all)     TIME=04:00:00 ;;  # partition MaxTime; actual ~40 min (p4 dominates)
  agentic) TIME=04:00:00 ;;  # one long tool-calling conversation; resumable via checkpoint
esac
# Forward the agent knobs when set (phase1.sbatch re-exports ALL)
EXTRA_AGENT=""
[ -n "${AEGIS_AGENT_TRANSPORT:-}" ] && EXTRA_AGENT="${EXTRA_AGENT},AEGIS_AGENT_TRANSPORT=${AEGIS_AGENT_TRANSPORT}"
[ -n "${AEGIS_AGENT_MAX_TURNS:-}" ] && EXTRA_AGENT="${EXTRA_AGENT},AEGIS_AGENT_MAX_TURNS=${AEGIS_AGENT_MAX_TURNS}"
# Sampler + experiment knobs: ONE env var per knob, forwarded through the
# explicit export list below. A composite "--flag value" string cannot ride a
# Slurm --export value (commas separate pairs, and spaces are not safe in all
# Slurm versions), so phase1.sbatch rebuilds the new-run flag list from the
# individual vars. An unset knob stays unset: "no seed was sent" is a fact.
EXTRA_EXPORT=""
for env_name in MVP_TEMPERATURE MVP_SEED MVP_TOP_P MVP_TOP_K MVP_ARM MVP_REPEAT MVP_P4_ADJUSTMENT MVP_P3_INSTRUCTION; do
  if [ -n "${!env_name:-}" ]; then
    EXTRA_EXPORT="${EXTRA_EXPORT},${env_name}=${!env_name}"
  fi
done
if [ "${MVP_PREAPPROVE_GATES:-}" = "1" ]; then
  EXTRA_EXPORT="${EXTRA_EXPORT},MVP_PREAPPROVE_GATES=1"
fi

# Continuing an existing run: export MVP_RUN_ID=run_<tag>_<first-JOBID> so the
# job reuses that run directory; a fresh p1 job derives run_<tag>_<own JOBID>.
EXTRA_RUN_ID=""
[ -n "${MVP_RUN_ID:-}" ] && EXTRA_RUN_ID=",MVP_RUN_ID=${MVP_RUN_ID}"

# Optional Slurm dependency for this submission (e.g. afterok:12345) — the
# experiment driver uses it to chain an `all` job onto its p1 job.
DEPEND_ARGS=""
[ -n "${MVP_DEPENDENCY:-}" ] && DEPEND_ARGS="--dependency=${MVP_DEPENDENCY}"

sbatch -J "mvp_${STAGE}" --time="$TIME" $DEPEND_ARGS \
  --export="ALL,STAGE=${STAGE},CASE=${CASE},MODEL=${MODEL},RUN_TAG=${RUN_TAG}${EXTRA_RUN_ID}${EXTRA_AGENT}${EXTRA_EXPORT}" \
  pipeline/deucalion/phase1.sbatch
echo "monitor: squeue -u \$USER ; then tail the run log under runs/run_${RUN_TAG}_<JOB>/logs/"
