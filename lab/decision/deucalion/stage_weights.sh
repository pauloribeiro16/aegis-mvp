#!/usr/bin/env bash
# stage_weights.sh — download the two d1 checkpoints into the shared HF cache.
#
# RUN ON THE LOGIN NODE, not with sbatch:
#   bash lab/decision/deucalion/stage_weights.sh
#
# Compute nodes have NO egress to huggingface.co, so the download has to happen
# where egress exists (the login node does; the cluster's own
# stage-hf-model-aegis.sbatch says the same in its header). It is 8 GB of
# I/O and a couple of minutes — the one exception to "no heavy work on the
# login node", and the established practice for weight staging on this cluster.
#
# Naming convention is the cluster's own: <org>_<repo> under
# $HF_STAGING_ROOT (same as stage-hf-model-aegis.sbatch).
#   LiquidAI/d1-3B        -> LiquidAI_d1-3B        (5.8 GB, bf16)
#   LiquidAI/d1-omni-600M -> LiquidAI_d1-omni-600M (2.2 GB, float32)
set -euo pipefail

BD="/projects/F202512235CPCAA1/CyberMetric_Deucalion"
HFB="${HF_STAGING_ROOT:-$BD/models/hf}"
mkdir -p "$HFB"

# `hf` CLI candidates, best first. The new vllm-v2 venv has huggingface_hub
# >=1.31 (and therefore `hf`), but it may not be built yet when this runs.
HF_BIN=""
for cand in \
  "$BD/aegis-vllm-v2/venv/bin/hf" \
  "$BD/aegis-phase1/.venv/bin/hf" \
  "/projects/F202512235CPCAA1/aegis-orchestrator/venv/bin/hf" \
  "$(command -v hf 2>/dev/null || true)"; do
  if [[ -n "$cand" && -x "$cand" ]]; then HF_BIN="$cand"; break; fi
done
if [[ -z "$HF_BIN" ]]; then
  echo "FATAL: no \`hf\` CLI found (looked in aegis-vllm-v2, aegis-phase1, aegis-orchestrator, PATH)" >&2
  exit 3
fi
echo "hf CLI: $HF_BIN"

# HF_TOKEN lives in ~/.aegis_env (mode 600). Neither model is gated, so the
# token is optional -- but passing it when present avoids anonymous rate limits.
# grep -m1 (not `grep | head -1`): head closing the pipe makes grep die on
# SIGPIPE, and with `set -o pipefail` that turns the assignment into a failed
# command, which `set -e` turns into a silent abort of the whole script.
HF_TOKEN="${HF_TOKEN:-}"
if [[ -z "$HF_TOKEN" && -r "$HOME/.aegis_env" ]]; then
  HF_TOKEN="$(grep -m1 -E '^HF_TOKEN=' "$HOME/.aegis_env" 2>/dev/null | cut -d= -f2- | tr -d "\"' " || true)"
fi
echo "HF_TOKEN: ${HF_TOKEN:+set (${#HF_TOKEN} chars)}${HF_TOKEN:-unset (anonymous)}"

export HF_HOME="$HFB/.cache"
export HF_HUB_CACHE="$HF_HOME/hub"
mkdir -p "$HF_HUB_CACHE"

stage() {
  local repo="$1"
  local dir="$HFB/$(echo "${repo}" | tr '/' '_')"
  echo
  echo "=== staging ${repo} -> ${dir} ==="
  if [[ -f "${dir}/config.json" && -f "${dir}/model.safetensors" ]]; then
    echo "already staged: ${dir}"
    du -sh "$dir"
    return 0
  fi
  mkdir -p "$dir"
  local args=(download "${repo}" --local-dir "${dir}" --max-workers 8)
  [[ -n "$HF_TOKEN" ]] && args+=(--token "$HF_TOKEN")
  "$HF_BIN" "${args[@]}" 2>&1 | tail -20
  if [[ ! -f "${dir}/config.json" ]]; then
    echo "FATAL: config.json missing after staging ${repo}" >&2
    return 4
  fi
  du -sh "$dir"
  "$HF_BIN" download "${repo}" --local-dir "${dir}" --include "config.json" >/dev/null 2>&1 || true
  python3 - "$dir" <<'PYEOF' 2>/dev/null || true
import json, sys
from pathlib import Path
d = Path(sys.argv[1])
cfg = json.loads((d / "config.json").read_text())
print("  model_type   =", cfg.get("model_type"))
print("  architectures=", cfg.get("architectures"))
print("  dtype        =", cfg.get("dtype") or cfg.get("torch_dtype"))
print("  max_position =", cfg.get("max_position_embeddings"))
PYEOF
}

stage "LiquidAI/d1-3B"
stage "LiquidAI/d1-omni-600M"

echo
echo "=== staging root ==="
du -sh "$HFB"/* 2>/dev/null || true
df -h /projects/F202512235CPCAA1 | tail -2
echo "=== stage_weights DONE ==="
