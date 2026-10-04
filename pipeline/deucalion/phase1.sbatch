#!/usr/bin/env bash
# phase1.sbatch — one pipeline stage per job on a Deucalion GPU compute node.
# Hardening per my-skills/hpc-deucalion (SKILL.md hard rules + error playbook):
#   RUN_LOG created and stdout/stderr redirected BEFORE the first echo;
#   trap writes END= + EXIT_CODE= forensics; stale __pycache__ wiped and
#   PYTHONDONTWRITEBYTECODE=1; Ollama port derived from the job id (no 11434
#   collisions); the 0.32.13 binary (graphify-methodology) is used because
#   qwen3.8 does not load under 0.31.1; model cache verified before serving;
#   all logs to NFS (run folder), never compute-node scratch.
#SBATCH --job-name=mvp_phase1
#SBATCH --account=f202512235cpcaa1g
#SBATCH --partition=dev-a100-80
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:a100:1
#SBATCH --time=01:00:00
#SBATCH --chdir=/projects/F202512235CPCAA1/mvp-pipeline/aegis-mvp
#SBATCH --output=runs/slurm_%j.out

set -uo pipefail

: "${STAGE:?STAGE not exported (p1|p2|p3|p3f|p4|p4t|p5|p4p5)}"
: "${RUN_TAG:?RUN_TAG not exported (short tag, e.g. case01)}"
: "${CASE:?CASE not exported (pipeline/cases/<case>)}"
: "${MODEL:?MODEL not exported (e.g. qwen3.8:27b)}"

# Continuing an existing run: pass MVP_RUN_ID; a fresh p1 job derives its own.
# Os runs vivem FORA do checkout do repo (../aegis-runs), na mesma NFS — um
# repositório não é arquivo de resultados.
RUNS_ROOT="${MVP_RUNS_ROOT:-$SLURM_SUBMIT_DIR/../aegis-runs}"
RUN_ID="${MVP_RUN_ID:-run_${RUN_TAG}_${SLURM_JOB_ID}}"
mkdir -p "${RUNS_ROOT}/${RUN_ID}/logs"
RUN_LOG="${RUNS_ROOT}/${RUN_ID}/logs/run_${STAGE}_${SLURM_JOB_ID}.log"
touch "$RUN_LOG"
exec 3>&1  # forensics channel: original slurm stdout, survives tee teardown
exec > >(tee -a "$RUN_LOG") 2>&1
trap 'rc=$?; line="END=$(date -Is) EXIT_CODE=$rc"; echo "$line" >&3; echo "$line" >> "$RUN_LOG"' EXIT

echo "=== AEGIS-MVP Phase 1 pipeline | stage=${STAGE} model=${MODEL} job=${SLURM_JOB_ID} node=$(hostname -s) start=$(date -Is) ==="
[ -f "runs/slurm_${SLURM_JOB_ID}.out" ] && mv "runs/slurm_${SLURM_JOB_ID}.out" "${RUNS_ROOT}/${RUN_ID}/logs/" || true

# --- environment ------------------------------------------------------------
# Deucalion profile scripts touch unset vars: NEVER run module/profile under -u
# (2026-10-01 job 1963493: set -u + source /etc/profile killed the shell
# silently — both logs truncated after the first line).
set +u
source /etc/profile 2>/dev/null || true
module purge 2>/dev/null || true
module load Python/3.11.3-GCCcore-12.3.0 2>/dev/null \
  || echo "WARN: python module load failed; falling back to system python3"
set -u

# 0.32.13 binary — the only one that serves qwen3.8 (0.31.1: unknown architecture)
export PATH="/projects/F202512235CPCAA1/graphify-methodology/bin:$PATH"
export LD_LIBRARY_PATH="/projects/F202512235CPCAA1/graphify-methodology/lib/ollama:${LD_LIBRARY_PATH:-}"
export OLLAMA_MODELS="/projects/F202512235CPCAA1/CyberMetric_Deucalion/ollama_data/models"
PORT=$((11434 + SLURM_JOB_ID % 20000))
export OLLAMA_HOST="127.0.0.1:${PORT}"
OLLAMA_BASE="http://127.0.0.1:${PORT}"

# --- stale bytecode (post-sync ImportError class) ---------------------------
find pipeline/src -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find pipeline/src -name "*.pyc" -delete 2>/dev/null || true
export PYTHONDONTWRITEBYTECODE=1

# --- model cache check (no egress on compute nodes; pull happens on login) --
# A bare name (no colon) means the implicit :latest tag. Without this default,
# `${MODEL##*:}` returns the WHOLE string for a colon-less model, so the probe
# looks for library/glm-4.7-flash/glm-4.7-flash instead of .../latest and kills a
# job that the model in fact has (this is what jobs 1979339/1979340 hit, after a
# truncated tag lost the ":30b"; both models are present in the shared cache).
MODEL_NAME="${MODEL%%:*}"
MODEL_TAG="${MODEL##*:}"
[ "$MODEL_NAME" = "$MODEL" ] && MODEL_TAG="latest"
MODEL_MANIFEST="${OLLAMA_MODELS}/manifests/registry.ollama.ai/library/${MODEL_NAME}/${MODEL_TAG}"
if [ ! -e "$MODEL_MANIFEST" ]; then
  echo "FATAL: model '${MODEL}' -> no manifest at ${MODEL_MANIFEST}"
  echo "       available in the shared cache:"
  ls -1 "${OLLAMA_MODELS}/manifests/registry.ollama.ai/library" 2>/dev/null | sed 's/^/         /'
  echo "       (pull it on the login node with the graphify 0.32.13 binary first)"
  exit 2
fi
echo "model manifest present: ${MODEL_MANIFEST}"
nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv || true

# --- serve Ollama on the compute node ---------------------------------------
ollama serve > "${RUNS_ROOT}/${RUN_ID}/logs/ollama_serve_${SLURM_JOB_ID}.log" 2>&1 &
OLLAMA_PID=$!
UP=0
for _ in $(seq 1 30); do
  if curl -s "http://127.0.0.1:${PORT}/api/tags" > /dev/null; then UP=1; break; fi
  sleep 5
done
if [ "$UP" -ne 1 ]; then
  echo "FATAL: ollama serve did not come up on port ${PORT}; see ollama_serve log"
  kill "$OLLAMA_PID" 2>/dev/null || true
  exit 3
fi
echo "ollama up: ${OLLAMA_BASE}"

# --- initialise the run directory once, then run the stage ------------------
# Sampler / experiment flags arrive as one env var per knob (see submit.sh).
# They are applied ONLY when creating the run: every later stage reads the
# config back from the run directory, so a resumed or re-queued stage cannot be
# silently re-sampled with different settings than the ones on record.
CFG_FLAGS=""
[ -n "${MVP_TEMPERATURE:-}" ] && CFG_FLAGS="${CFG_FLAGS} --temperature=${MVP_TEMPERATURE}"
[ -n "${MVP_SEED:-}" ]        && CFG_FLAGS="${CFG_FLAGS} --seed=${MVP_SEED}"   # "none" opts out
[ -n "${MVP_TOP_P:-}" ]       && CFG_FLAGS="${CFG_FLAGS} --top-p=${MVP_TOP_P}"
[ -n "${MVP_TOP_K:-}" ]       && CFG_FLAGS="${CFG_FLAGS} --top-k=${MVP_TOP_K}"
[ -n "${MVP_ARM:-}" ]         && CFG_FLAGS="${CFG_FLAGS} --arm=${MVP_ARM}"
[ -n "${MVP_REPEAT:-}" ]      && CFG_FLAGS="${CFG_FLAGS} --repeat=${MVP_REPEAT}"
[ -n "${MVP_P4_ADJUSTMENT:-}" ] && CFG_FLAGS="${CFG_FLAGS} --p4-adjustment=${MVP_P4_ADJUSTMENT}"
[ -n "${MVP_P3_INSTRUCTION:-}" ] && CFG_FLAGS="${CFG_FLAGS} --p3-instruction=${MVP_P3_INSTRUCTION}"
[ "${MVP_PREAPPROVE_GATES:-}" = "1" ] && CFG_FLAGS="${CFG_FLAGS} --preapprove-gates"

if [ ! -f "${RUNS_ROOT}/${RUN_ID}/manifest.json" ]; then
  # shellcheck disable=SC2086  (word splitting IS the flag transport here)
  python3 pipeline/src/run_pipeline.py new-run --repo . --case "$CASE" \
    --run-dir "${RUNS_ROOT}/${RUN_ID}" --model "$MODEL" --base "$OLLAMA_BASE" \
    ${CFG_FLAGS:+$CFG_FLAGS}
fi
python3 pipeline/src/run_pipeline.py run --stage "$STAGE" --repo . \
  --run-dir "${RUNS_ROOT}/${RUN_ID}" --base "$OLLAMA_BASE"
RC=$?

kill "$OLLAMA_PID" 2>/dev/null || true
echo "=== stage ${STAGE} finished rc=${RC} at $(date -Is) | run dir: ${RUNS_ROOT}/${RUN_ID} ==="
exit "$RC"
