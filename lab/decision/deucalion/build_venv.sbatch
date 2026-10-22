#!/usr/bin/env bash
# build_venv.sbatch — build the vLLM 0.32.0 venv the d1 decision models need.
#
# Why a NEW venv and not the existing one:
#   aegis-vllm-venv/venv holds vLLM 0.10.0 (torch 2.7.1+cu126, transformers 4.55.2).
#   Its registry has neither Lfm2VlForConditionalGeneration nor D1OmniModel, and
#   its transformers has only the text-only Lfm2ForCausalLM. `vllm serve` on
#   LiquidAI/d1-3B would die with "unsupported architecture".
#   vLLM 0.32.0 is the first release with the `LiquidStrategy` decision frontend
#   (POST /v1/systemone) and it pins torch==2.13.0 + transformers>=5.16.1.
#   The old venv is the only working vLLM on the cluster (it serves the Qwen FP8
#   scout), so it stays exactly as it is. Two venvs, side by side, never mixed.
#
# Cluster constraints this script respects:
#   - Rule 1 of the hpc-deucalion skill: no heavy work on the login node. The
#     pip install runs inside this sbatch job on the CPU partition.
#   - Compute nodes have no egress; pip resolves from the INTERNAL mirror
#     http://sn02:9191/index/ (already exported as PIP_INDEX_URL cluster-wide).
#   - /home/paulinho is quota-limited (8.7/20 GB used, file count already over
#     its soft limit) -> the venv lives on /projects, and the pip cache is
#     discarded rather than stored (TMPDIR on the node's local /tmp).
#   - `set +u` around any profile/module sourcing: Deucalion's profile.d
#     scripts expand unset variables and kill a non-interactive bash fatally.
#
# Usage: sbatch build_venv.sbatch

#SBATCH --job-name=d1_build_venv
#SBATCH --account=F202512235CPCAA1X
#SBATCH --partition=dev-x86
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --chdir=/projects/F202512235CPCAA1/CyberMetric_Deucalion
#SBATCH --output=/projects/F202512235CPCAA1/CyberMetric_Deucalion/slurm-d1-build-venv-%j.out
#SBATCH --error=/projects/F202512235CPCAA1/CyberMetric_Deucalion/slurm-d1-build-venv-%j.err

set -uo pipefail
umask 077

BD="/projects/F202512235CPCAA1/CyberMetric_Deucalion"
NEW="${D1_VENV_ROOT:-$BD/aegis-vllm-v2}"
VENV="$NEW/venv"
LOG_DIR="$BD/aegis-d1-exp/logs"
mkdir -p "$LOG_DIR" "$NEW"
RUN_LOG="$LOG_DIR/build_venv_${SLURM_JOB_ID}.log"
exec 3>&1
exec >>"$RUN_LOG" 2>&1
echo "=== build_venv job ${SLURM_JOB_ID} on $(hostname) ==="

cleanup() {
  local code=$?
  echo "END=$(date -Is) EXIT_CODE=$code" >&3
  exit "$code"
}
trap cleanup EXIT

echo "--- disk ---"
df -h /projects/F202512235CPCAA1 /tmp 2>&1 | tail -3

# --- interpreter -------------------------------------------------------------
# The EB interpreter runs standalone; no module load needed (and loading CUDA
# modules risks clashing with the cu13 wheels that ship inside the venv).
PY="/eb/x86_64/software/Python/3.12.3-GCCcore-13.3.0/bin/python"
if [[ ! -x "$PY" ]]; then
  echo "FATAL: EB python 3.12.3 not found at $PY" >&3
  exit 3
fi
"$PY" --version

# --- internal pip mirror -----------------------------------------------------
export PIP_INDEX_URL="${PIP_INDEX_URL:-http://sn02:9191/index/}"
export PIP_TRUSTED_HOST="${PIP_TRUSTED_HOST:-sn02}"
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_NO_CACHE_DIR=1
export TMPDIR="/tmp/d1-build-${SLURM_JOB_ID}"
mkdir -p "$TMPDIR"

# Every build cache goes to the node's LOCAL /tmp, never to $HOME:
#   - /home/paulinho has a 20 GB quota with 8.7 GB used, and the file-count
#     soft limit is already exceeded.
#   - pip's PEP 517 build env unpacks cargo crates under
#     $XDG_CACHE_HOME/puccinialin/cargo/registry/src; on /home that unpack
#     died with "Disk quota exceeded (os error 122)" and killed the build.
export XDG_CACHE_HOME="$TMPDIR/cache"
export CARGO_HOME="$TMPDIR/cargo"
export PIP_CACHE_DIR="$TMPDIR/pip-cache"
mkdir -p "$XDG_CACHE_HOME" "$CARGO_HOME" "$PIP_CACHE_DIR"
echo "PIP_INDEX_URL=$PIP_INDEX_URL"
echo "CARGO_HOME=$CARGO_HOME"

# --- Rust toolchain ----------------------------------------------------------
# llguidance publishes no manylinux_2_28 wheel (its Linux wheels are
# manylinux_2_31 and this cluster is Rocky 8.5 / glibc 2.28 -- the wheel
# needs GLIBC_2.30 and refuses to load), so pip falls back to the sdist,
# which needs a Rust compiler. The cluster already has one next to the old
# vLLM venv: rustc 1.98.0.
RUST_BIN="${D1_RUST_BIN:-$BD/aegis-vllm-venv/rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin}"
if [[ -x "$RUST_BIN/cargo" ]]; then
  export PATH="$RUST_BIN:$PATH"
  echo "rust: $(cargo --version) / $(rustc --version)"
else
  echo "FATAL: no cargo at $RUST_BIN" >&3
  exit 7
fi
if ! command -v cc >/dev/null 2>&1; then
  echo "FATAL: no C compiler on the compute node (pyo3 needs one)" >&3
  exit 8
fi

# Reuse the crates the previous failed build already downloaded, so the
# llguidance build does not depend on crates.io being reachable from a
# compute node.
SRC_REG="${HOME}/.cache/puccinialin/cargo/registry"
if [[ -d "$SRC_REG" ]]; then
  mkdir -p "$CARGO_HOME/registry"
  cp -rn "$SRC_REG/." "$CARGO_HOME/registry/" 2>/dev/null || true
  echo "reused $(find "$CARGO_HOME/registry" -name '*.crate' 2>/dev/null | wc -l) cached crates"
fi

# --- create the venv ---------------------------------------------------------
if [[ ! -x "$VENV/bin/python" ]]; then
  "$PY" -m venv --system-site-packages "$VENV" || {
    echo "FATAL: venv creation failed" >&3; exit 4; }
fi
VPY="$VENV/bin/python"
"$VPY" -m pip install -U pip wheel setuptools

# --- resolve first, download later -------------------------------------------
# A dry run costs seconds and would have caught the llguidance problem
# before 20 GB of wheels were pulled.
"$VPY" -m pip install --dry-run --report /tmp/d1-build-${SLURM_JOB_ID}/resolve.json \
  "vllm==0.32.0" \
  "transformers==5.16.1" \
  "torch==2.13.0" \
  "torchaudio==2.11.0" \
  "torchvision==0.28.0" \
  "tokenizers>=0.23.2,<0.24.0" \
  "huggingface_hub>=1.31.0,<2.0" \
  "pillow>=12.3.0,<13" \
  "torchcodec>=0.14" \
  soundfile numpy > "$TMPDIR/resolve.log" 2>&1 || {
  echo "FATAL: dependency resolution failed (no wheels downloaded yet)" >&3
  tail -30 "$TMPDIR/resolve.log" >&3
  exit 9; }
echo "resolution OK"

# --- llguidance: build the sdist BEFORE vllm --------------------------------
# Installing it first means the vllm install sees the requirement already
# satisfied and never falls back to the sdist mid-resolution.
"$VPY" -m pip install --no-binary llguidance --no-cache-dir "llguidance==1.7.6" \
  > "$TMPDIR/llguidance.log" 2>&1 || {
  echo "FATAL: llguidance sdist build failed" >&3
  tail -40 "$TMPDIR/llguidance.log" >&3
  exit 10; }
"$VPY" -c "import llguidance; print('llguidance', llguidance.__version__, 'imports OK')" || {
  echo "FATAL: llguidance does not import" >&3; exit 11; }

# --- install -----------------------------------------------------------------
# Pins resolved against the internal mirror's own wheel metadata:
#   vllm 0.32.0        torch==2.13.0 torchaudio==2.11.0 torchvision==0.28.0
#                      transformers>=5.16.1,<5.20.0 tokenizers>=0.23.2
#                      huggingface_hub>=1.31.0 flashinfer-python==0.7.0.post1
#   transformers 5.16.1  huggingface-hub<2.0,>=1.5.0  tokenizers<0.24.0,>=0.23.1
# The two transformers bounds intersect the mirror only at hub 1.31.0-1.33.0
# and tokenizers 0.23.2/0.23.3 -- hub 2.x is excluded by transformers, and the
# mirror has no hub above 1.33.0 in the 1.x line, so the upper bound is
# explicit rather than left to the resolver.
#
# flashinfer-cubin / flashinfer-jit-cache are NOT installed: the mirror's
# flashinfer-jit-cache project page is empty and its newest cubin wheel
# (0.6.13) predates the flashinfer-python 0.7.0.post1 that vllm pins. The
# serving script therefore sets VLLM_USE_FLASHINFER_SAMPLER=0 and
# FLASHINFER_DISABLE_JIT=1 -- the decision endpoint reads logprobs and never
# samples, so it does not need the flashinfer sampler.
"$VPY" -m pip install --no-cache-dir \
  "vllm==0.32.0" \
  "transformers==5.16.1" \
  "torch==2.13.0" \
  "torchaudio==2.11.0" \
  "torchvision==0.28.0" \
  "tokenizers>=0.23.2,<0.24.0" \
  "huggingface_hub>=1.31.0,<2.0" \
  "pillow>=12.3.0,<13" \
  "torchcodec>=0.14" \
  soundfile \
  numpy || {
  echo "FATAL: pip install failed" >&3; exit 5; }

# --- verify ------------------------------------------------------------------
echo "--- installed ---"
"$VPY" -m pip list 2>/dev/null | grep -iE '^(vllm|torch|torchvision|torchaudio|transformers|tokenizers|huggingface|numpy|pillow|soundfile|flashinfer)' || true

"$VPY" - <<'PYEOF' || { echo "FATAL: post-install verification failed" >&3; exit 6; }
import sys
import torch, transformers
print("python      =", sys.version.split()[0])
print("torch       =", torch.__version__, "cuda", torch.version.cuda)
print("transformers=", transformers.__version__)
assert transformers.__version__.startswith("5.16"), transformers.__version__

# vLLM must know the d1-3B architecture.
from vllm.model_executor.models.registry import ModelRegistry
archs = ModelRegistry.get_supported_archs()
for want in ("Lfm2VlForConditionalGeneration",):
    print(f"vllm arch {want}:", want in archs)
    assert want in archs, f"{want} missing from the vLLM registry"
print("D1OmniModel in vllm:", "D1OmniModel" in archs, "(expected False -> d1-omni runs in-process)")

# transformers must know the LFM2-VL config/processor (d1-3B is model_type lfm2_vl).
from transformers.models.lfm2_vl import Lfm2VlConfig, Lfm2VlProcessor
print("transformers Lfm2VlConfig: OK")

# The decision frontend must exist in this vLLM build.
import importlib
for mod in ("vllm.entrypoints.generate.structured_decisions.strategies",
            "vllm.entrypoints.generate.structured_decisions.question_types"):
    try:
        importlib.import_module(mod)
        print("module OK:", mod)
    except Exception as exc:  # noqa: BLE001
        print("module MISSING:", mod, "->", exc)
        raise SystemExit(7)
PYEOF

echo "=== build_venv DONE: $VENV ==="
echo "Point the serving scripts at it with: AEGIS_VLLM_VENV=$VENV"
