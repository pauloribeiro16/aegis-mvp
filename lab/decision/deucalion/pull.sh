#!/usr/bin/env bash
# pull.sh — bring the results back from the cluster.
#
#   bash lab/decision/deucalion/pull.sh            # everything in results/
#   bash lab/decision/deucalion/pull.sh A2_cases_protocol.jsonl
#
# The results land in lab/decision/results/ on the workstation, one file per
# arm. The logs stay on the cluster (they are large and their home is the
# project dir), but the run log of each arm is small and worth having.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
BD="${MVP_BD:-/projects/F202512235CPCAA1/CyberMetric_Deucalion}"
DEST="${MVP_DEST:-$BD/aegis-d1-exp}"
LOCAL="$REPO_ROOT/lab/decision/results"

mkdir -p "$LOCAL"

if [[ $# -gt 0 ]]; then
  for f in "$@"; do
    scp -q "$HOST:$DEST/results/$f" "$LOCAL/$f" && echo "pulled $f"
  done
else
  scp -q "$HOST:$DEST/results/*.jsonl" "$LOCAL/" && echo "pulled all results"
fi

# The per-arm run logs are small and carry the server's own diagnostics.
for log in "$HOST:$DEST/logs/serve_vllm_*.log" "$HOST:$DEST/logs/inproc_*.log"; do
  : # best-effort; a missing log must not fail the pull
done
ssh -o LogLevel=ERROR "$HOST" \
  "cd '$DEST/logs' && for f in serve_vllm_*.log inproc_*.log; do [ -f \"\$f\" ] && echo \"--- \$f\" && cat \"\$f\"; done" \
  > "$LOCAL/cluster_run_logs.txt" 2>/dev/null || true

ls -la "$LOCAL"
