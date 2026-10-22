#!/usr/bin/env bash
# serve_vllm.sbatch — arm A2: serve d1-3B with vLLM and run the suite
# against the decision endpoint.
#
# One job does both: start the server, wait for it, run the suite, shut it
# down. A server that outlives its job would need a port negotiated with
# every other job on the node; inside one job the port is ours alone.
#
# Usage:
#   sbatch --export=ARM=A2,CASES=cases_protocol.json \
#          deucalion/serve_vllm.sbatch
#
# Notes:
#   - Weights are staged on the login node (compute nodes have no egress) at
#     $BD/models/hf/LiquidAI_d1-3B. HF_HUB_OFFLINE=1 keeps the server from
#     trying to reach the hub at all.
#   - The server rebuilds the checkpoint's prompt and reads next-token
#     logprobs over the label tokens (vLLM's LiquidStrategy). That is an
#     APPROXIMATION of the checkpoint's own tree-batched forward pass, which
#     is why arm A1 exists.
#   - VLLM_USE_FLASHINFER_SAMPLER=0: flashinfer has no matching cubin wheel
#     for this cluster's glibc and the decision endpoint reads logprobs
#     instead of sampling, so the flashinfer sampler is not needed.
#SBATCH --job-name=d1_serve_vllm
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
#SBATCH --output=/projects/F202512235CPCAA1/CyberMetric_Deucalion/aegis-d1-exp/logs/slurm-serve-vllm-%j.out
#SBATCH --error=/projects/F202512235CPCAA1/CyberMetric_Deucalion/aegis-d1-exp/logs/slurm-serve-vllm-%j.err

set -uo pipefail
umask 077

BD="/projects/F202512235CPCAA1/CyberMetric_Deucalion"
DEST="$BD/aegis-d1-exp"
VENV="${AEGIS_VLLM_VENV:-$BD/aegis-vllm-v2/venv}"
MODEL_DIR="${MODEL_DIR:-$BD/models/hf/LiquidAI_d1-3B}"
PORT="${VLLM_PORT:-$((8100 + SLURM_JOB_ID % 1000))}"
ARM="${ARM:-A2}"
CASES="${CASES:-cases_protocol.json}"
SERVED_NAME="${SERVED_NAME:-d1-3B}"

mkdir -p "$DEST/logs" "$DEST/results"
RUN_LOG="$DEST/logs/serve_vllm_${ARM}_${SLURM_JOB_ID}.log"
exec 3>&1
exec >>"$RUN_LOG" 2>&1
echo "=== serve_vllm $ARM job ${SLURM_JOB_ID} on $(hostname) ==="
echo "model=$MODEL_DIR port=$PORT cases=$CASES"

VLLM_PID=""
cleanup() {
  local code=$?
  if [[ -n "${VLLM_PID:-}" ]] && kill -0 "$VLLM_PID" 2>/dev/null; then
    kill "$VLLM_PID" 2>/dev/null || true
    wait "$VLLM_PID" 2>/dev/null || true
  fi
  echo "END=$(date -Is) EXIT_CODE=$code" >&3
  exit "$code"
}
trap cleanup EXIT SIGTERM SIGINT

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

if [[ ! -x "$VENV/bin/vllm" ]]; then
  echo "FATAL: no vllm at $VENV/bin/vllm" >&3
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
export VLLM_USE_FLASHINFER_SAMPLER=0
export FLASHINFER_DISABLE_JIT=1
export VLLM_LOGGING_LEVEL=INFO
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$HF_HUB_CACHE"

nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader >&3

VLLM_LOG="$DEST/logs/vllm_${ARM}_${SLURM_JOB_ID}.log"
"$VENV/bin/vllm" serve "$MODEL_DIR" \
  --served-model-name "$SERVED_NAME" \
  --host 127.0.0.1 \
  --port "$PORT" \
  --tensor-parallel-size 1 \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.90 \
  --enforce-eager \
  > "$VLLM_LOG" 2>&1 &
VLLM_PID=$!
echo "vllm pid=$VLLM_PID log=$VLLM_LOG"

READY=0
for i in $(seq 1 90); do
  if curl -sf "http://127.0.0.1:${PORT}/v1/models" >/dev/null 2>&1; then
    echo "[vllm] HTTP ready after ${i} polls (~$(($i * 10))s)"
    READY=1
    break
  fi
  if ! kill -0 "$VLLM_PID" 2>/dev/null; then
    echo "FATAL: vllm died during startup" >&3
    tail -60 "$VLLM_LOG" >&3
    exit 5
  fi
  sleep 10
done
if [[ "$READY" -ne 1 ]]; then
  echo "FATAL: vllm not ready after 15 min" >&3
  tail -60 "$VLLM_LOG" >&3
  exit 6
fi

# --- what does the server actually expose? --------------------------------
echo "--- /v1/models ---"
curl -s "http://127.0.0.1:${PORT}/v1/models" >&3 || true
echo
echo "--- one decision call (smoke) ---"
curl -s -X POST "http://127.0.0.1:${PORT}/v1/systemone" \
  -H "Content-Type: application/json" \
  -d '{"state":"I was charged twice this month, please refund one of them.","questions":{"refund":{"type":"noul","instructions":"Is the customer asking for a refund?"}}}' >&3 || true
echo

# --- the suite -------------------------------------------------------------
cd "$DEST"
RC=0
CASES_RESOLVED="${CASES//+/ }"
echo "CASES resolved: [$CASES_RESOLVED]"
for c in $CASES_RESOLVED; do
  echo "--- suite: $c ---"
  "$VENV/bin/python" run_suite.py \
    --backend http \
    --base "http://127.0.0.1:${PORT}" \
    --model "$SERVED_NAME" \
    --cases "$c" \
    --out "results/${ARM}_${c%.json}.jsonl" \
    --arm "$ARM" \
    --model-label "LiquidAI/d1-3B" || RC=$?
done
echo "suite exit=$RC"
exit $RC
