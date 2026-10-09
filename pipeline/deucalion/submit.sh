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

STAGE="${1:?stage required: p1|p2|p3|p3f|p4|p4t|p5|phase2|p4p5|all|agentic}"
# MVP_CASE is honoured so every driver knob is an env var (MODEL, RUN_TAG and
# the sampler knobs already are). A resumed run that forgets $2 used to fall
# back to Case_01 silently: the stage then assembled the deliverable from the
# WRONG company while the run directory still said Case_02 — a mismatch visible
# only in the document. It is now impossible to express, and the echo below
# prints the resolved case on every submission.
CASE="${2:-${MVP_CASE:-Case_01_TinyTask_SaaS}}"
case "$CASE" in
  Case_*) ;;
  *) echo "FATAL: case '$CASE' does not name a pipeline/cases/Case_* binding" >&2; exit 2 ;;
esac
MODEL="${MVP_MODEL:-qwen3.8:27b}"
RUN_TAG="${MVP_RUN_TAG:?set MVP_RUN_TAG=<short tag> (e.g. case01)}"

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
mkdir -p runs

# Validate before queueing: an unknown stage would otherwise start a GPU job
# (and an Ollama server) only for run_pipeline.py's argparse to reject it.
case "$STAGE" in
  p1|p2|p3|p3f|p4|p4t|p5|phase2|p4p5|all|agentic) ;;
  *) echo "FATAL: unknown stage '$STAGE' (expected: p1|p2|p3|p3f|p4|p4t|p5|phase2|p4p5|all|agentic)" >&2
     exit 2 ;;
esac

# --- model preflight (login node, before any GPU slot is spent) -------------
# The compute node re-checks the manifest (phase1.sbatch) but only AFTER the job
# is scheduled and the GPU is allocated. This preflight costs a stat() instead of
# a queue wait, and it is the guard against a silently mangled tag: the model
# tags carry a colon (glm-4.7-flash:latest, nemotron-3.5-lightning:30b) and every
# `${VAR%%:*}` shortcut truncates them into a name that does not exist — which is
# how jobs 1979339/1979340 died 19s in with "manifest not in shared cache".
# Resolve the tag from its own parts; never substring it.
MODEL_NAME="${MODEL%%:*}"
MODEL_TAG="${MODEL##*:}"
[ "$MODEL_NAME" = "$MODEL" ] && MODEL_TAG="latest"   # bare name -> implicit :latest
MANIFEST="${OLLAMA_MODELS:-/projects/F202512235CPCAA1/CyberMetric_Deucalion/ollama_data/models}/manifests/registry.ollama.ai/library/${MODEL_NAME}/${MODEL_TAG}"
if [ ! -e "$MANIFEST" ]; then
  # A model namespace with a dot (library/... is the flat namespace) or a
  # non-library repo would live elsewhere; list what IS there rather than guess.
  echo "FATAL: model '${MODEL}' -> no manifest at ${MANIFEST}" >&2
  echo "       available in the shared cache:" >&2
  CACHE="${OLLAMA_MODELS:-/projects/F202512235CPCAA1/CyberMetric_Deucalion/ollama_data/models}/manifests/registry.ollama.ai/library"
  ls -1 "$CACHE" 2>/dev/null | sed 's/^/         /' >&2 || echo "         (cache unreadable from here)" >&2
  echo "       (pull it on the login node with the graphify 0.32.13 binary)" >&2
  exit 2
fi
echo "preflight: model '${MODEL}' -> manifest present"

TIME=00:30:00
case "$STAGE" in
  p3|p3f) TIME=00:45:00 ;;
  p4t)    TIME=00:45:00 ;;
  p4|p4p5) TIME=03:00:00 ;;  # 1 call per selected sub-domain, sequential + render
  phase2)  TIME=00:30:00 ;;  # Doc01 is deterministic; p2d is ONE call per run
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
for env_name in MVP_TEMPERATURE MVP_SEED MVP_TOP_P MVP_TOP_K MVP_ARM MVP_REPEAT MVP_P4_ADJUSTMENT MVP_P3_INSTRUCTION MVP_P4_INSTRUCTION MVP_P4_IMPLICATION; do
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
# Echo the exact tag back so a mangled submission is visible in the submitter's
# own terminal, not only 19 seconds later inside the job log.
echo "submitted: stage=${STAGE} case=${CASE} model=${MODEL} tag=${RUN_TAG}${EXTRA_RUN_ID:+ run=${MVP_RUN_ID}}"
echo "monitor: squeue -u \$USER ; then tail the run log under runs/run_${RUN_TAG}_<JOB>/logs/"
