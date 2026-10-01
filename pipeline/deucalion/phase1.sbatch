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

: "${STAGE:?STAGE not exported (p1|p2|p3|p4|p5|p4p5)}"
: "${RUN_TAG:?RUN_TAG not exported (short tag, e.g. case01)}"
: "${CASE:?CASE not exported (pipeline/cases/<case>)}"
: "${MODEL:?MODEL not exported (e.g. qwen3.8:27b)}"

# Continuing an existing run: pass MVP_RUN_ID; a fresh p1 job derives its own.
RUN_ID="${MVP_RUN_ID:-run_${RUN_TAG}_${SLURM_JOB_ID}}"
mkdir -p "runs/${RUN_ID}/logs"
RUN_LOG="runs/${RUN_ID}/logs/run_${STAGE}_${SLURM_JOB_ID}.log"
touch "$RUN_LOG"
exec > >(tee -a "$RUN_LOG") 2>&1
trap 'rc=$?; echo "END=$(date -Is) EXIT_CODE=$rc"' EXIT

echo "=== AEGIS-MVP Phase 1 pipeline | stage=${STAGE} model=${MODEL} job=${SLURM_JOB_ID} node=$(hostname -s) start=$(date -Is) ==="
[ -f "runs/slurm_${SLURM_JOB_ID}.out" ] && mv "runs/slurm_${SLURM_JOB_ID}.out" "runs/${RUN_ID}/logs/"

# --- environment -----------------------------------------------------------
source /etc/profile 2>/dev/null || true
module purge 2>/dev/null || true
module load Python/3.11.3-GCCcore-12.3.0 2>/dev/null \
  || echo "WARN: python module load failed; falling back to system python3"

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
MODEL_MANIFEST="${OLLAMA_MODELS}/manifests/registry.ollama.ai/library/${MODEL%%:*}/${MODEL##*:}"
if [ ! -e "$MODEL_MANIFEST" ]; then
  echo "FATAL: model '${MODEL}' manifest not in shared cache (${MODEL_MANIFEST})."
  echo "       Pull it on the login node with the graphify 0.32.13 binary first."
  exit 2
fi
echo "model manifest present: ${MODEL_MANIFEST}"
nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv || true

# --- serve Ollama on the compute node ---------------------------------------
ollama serve > "runs/${RUN_ID}/logs/ollama_serve_${SLURM_JOB_ID}.log" 2>&1 &
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
if [ ! -f "runs/${RUN_ID}/manifest.json" ]; then
  python3 pipeline/src/run_pipeline.py new-run --repo . --case "$CASE" \
    --run-dir "runs/${RUN_ID}" --model "$MODEL" --base "$OLLAMA_BASE"
fi
python3 pipeline/src/run_pipeline.py run --stage "$STAGE" --repo . \
  --run-dir "runs/${RUN_ID}" --base "$OLLAMA_BASE"
RC=$?

kill "$OLLAMA_PID" 2>/dev/null || true
echo "=== stage ${STAGE} finished rc=${RC} at $(date -Is) | run dir: runs/${RUN_ID} ==="
exit "$RC"
