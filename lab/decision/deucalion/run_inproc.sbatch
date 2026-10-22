#!/usr/bin/env bash
# run_inproc.sbatch — arms A1 and A3: load the checkpoint in-process and run
# the suite against model.system_one().
#
# This is the checkpoint's OWN code path: the tree-batched forward pass that
# vLLM's LiquidStrategy only approximates. Arm A1 is d1-3B; arm A3 is
# d1-omni-600M, which has no vLLM route at all (D1OmniModel is in no
# upstream vLLM release).
#
# Usage:
#   sbatch --export=ARM=A1,MODEL_DIR=$BD/models/hf/LiquidAI_d1-3B,DTYPE=bfloat16 \
#          deucalion/run_inproc.sbatch
#   sbatch --export=ARM=A3,MODEL_DIR=$BD/models/hf/LiquidAI_d1-omni-600M,DTYPE=float32,AUDIO_CAPABLE=1 \
#          deucalion/run_inproc.sbatch
#
#SBATCH --job-name=d1_run_inproc
#SBATCH --account=F202512235CPCAA1G
#SBATCH --partition=dev-a100-80
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=96G
#SBATCH --gres=gpu:a100:1
#SBATCH --time=02:00:00
# gnx520's A100 is in an error state (nvidia-smi reports ERR! and 50 GB held
# by a process Slurm has lost track of); every CUDA init fails there.
#SBATCH --exclude=gnx520
#SBATCH --chdir=/projects/F202512235CPCAA1/CyberMetric_Deucalion/aegis-d1-exp
#SBATCH --output=/projects/F202512235CPCAA1/CyberMetric_Deucalion/aegis-d1-exp/logs/slurm-inproc-%j.out
#SBATCH --error=/projects/F202512235CPCAA1/CyberMetric_Deucalion/aegis-d1-exp/logs/slurm-inproc-%j.err

set -uo pipefail
umask 077

BD="/projects/F202512235CPCAA1/CyberMetric_Deucalion"
DEST="$BD/aegis-d1-exp"
VENV="${AEGIS_VLLM_VENV:-$BD/aegis-vllm-v2/venv}"
ARM="${ARM:-A1}"
MODEL_DIR="${MODEL_DIR:-$BD/models/hf/LiquidAI_d1-3B}"
DTYPE="${DTYPE:-bfloat16}"
CASES="${CASES:-cases_protocol.json}"
AUDIO_CAPABLE="${AUDIO_CAPABLE:-0}"
MODEL_LABEL="${MODEL_LABEL:-$(basename "$MODEL_DIR")}"

mkdir -p "$DEST/logs" "$DEST/results"
RUN_LOG="$DEST/logs/inproc_${ARM}_${DTYPE}_${SLURM_JOB_ID}.log"
exec 3>&1
exec >>"$RUN_LOG" 2>&1
echo "=== run_inproc $ARM ($DTYPE) job ${SLURM_JOB_ID} on $(hostname) ==="
echo "model=$MODEL_DIR cases=$CASES audio_capable=$AUDIO_CAPABLE"

cleanup() {
  local code=$?
  echo "END=$(date -Is) EXIT_CODE=$code" >&3
  exit "$code"
}
trap cleanup EXIT

# --- caches off the quota-limited $HOME -------------------------------------
# /home/paulinho is at its quota (20 GB, file count already over the soft
# limit). vLLM writes its model-info cache to ~/.cache/vllm and dies with
# "Disk quota exceeded: '/home/paulinho/.cache/vllm'" before it ever starts.
export VLLM_CACHE_ROOT="${VLLM_CACHE_ROOT:-$DEST/.cache/vllm}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-$DEST/.cache}"
export TRITON_CACHE_DIR="${TRITON_CACHE_DIR:-$DEST/.cache/triton}"
export TORCHINDUCTOR_CACHE_DIR="${TORCHINDUCTOR_CACHE_DIR:-$DEST/.cache/inductor}"
mkdir -p "$VLLM_CACHE_ROOT" "$XDG_CACHE_HOME" "$TRITON_CACHE_DIR" "$TORCHINDUCTOR_CACHE_DIR"

# --- GPU health gate --------------------------------------------------------
# gnx520's A100 reports ERR! in nvidia-smi with 50 GB held by a process Slurm
# has lost track of: torch sees device_count=1 but every CUDA init fails with
# "No CUDA GPUs are available", and vLLM dies with an opaque engine-core
# traceback. Fail fast with the real reason instead.
if ! "$VENV/bin/python" -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "FATAL: CUDA is not usable on $(hostname)." >&3
  nvidia-smi --query-gpu=index,name,memory.used --format=csv,noheader >&3 || true
  echo "       The node's GPU is in an error state; exclude it and resubmit." >&3
  exit 8
fi

if [[ ! -x "$VENV/bin/python" ]]; then
  echo "FATAL: no venv python at $VENV/bin/python" >&3
  exit 3
fi
if [[ ! -f "$MODEL_DIR/config.json" ]]; then
  echo "FATAL: no checkpoint at $MODEL_DIR" >&3
  exit 4
fi

export HF_HOME="$BD/models/hf/.cache"
export HF_HUB_CACHE="$HF_HOME/hub"
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export PYTHONDONTWRITEBYTECODE=1
export TOKENIZERS_PARALLELISM=false
mkdir -p "$HF_HUB_CACHE"

nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader >&3

cd "$DEST"
find "$DEST" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

AUDIO_FLAG=()
if [[ "$AUDIO_CAPABLE" == "1" ]]; then AUDIO_FLAG=(--audio-capable); fi

RC=0
CASES_RESOLVED="${CASES//+/ }"
echo "CASES resolved: [$CASES_RESOLVED]"
for c in $CASES_RESOLVED; do
  echo "--- suite: $c ---"
  "$VENV/bin/python" run_suite.py \
    --backend inproc \
    --checkpoint "$MODEL_DIR" \
    --dtype "$DTYPE" \
    --model-label "$MODEL_LABEL" \
    --cases "$c" \
    --out "results/${ARM}_${DTYPE}_${c%.json}.jsonl" \
    --arm "$ARM" \
    "${AUDIO_FLAG[@]}" || RC=$?
done
echo "suite exit=$RC"
exit $RC
