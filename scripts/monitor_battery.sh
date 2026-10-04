#!/usr/bin/env bash
# monitor_battery.sh — the pipeline from Deucalion to the results page.
#
# One cycle, every POLL_SECONDS while any job is in flight:
#   1. sync down every run_exp02_*/run_m0* directory that has a deliverable on
#      the cluster and does not exist locally yet (the completed-battery pipe);
#   2. refresh _aggregate_cache.json, which the inspector's Experiments page
#      reads (fresh cache -> page renders in ms; stale -> the backend recomputes);
#   3. collect any finished model smokes;
#   4. log queue depth + state counts, and exit when the queue drains.
#
# Usage: bash scripts/monitor_battery.sh [max_cycles]
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
POLL_SECONDS="${POLL_SECONDS:-300}"
MAX_CYCLES="${1:-400}"

sh_quiet() { ssh -n -o BatchMode=yes "$HOST" "$@" 2>/dev/null; }

mkdir -p "$RUNS"

cycle=0
while [ "$cycle" -lt "$MAX_CYCLES" ]; do
  cycle=$((cycle + 1))
  queue=$(sh_quiet "squeue -u paulinho -h | wc -l")
  states=$(sh_quiet "sacct -X -n --starttime=2026-10-03 --format=State -u paulinho | sort | uniq -c | tr '\n' ' '")
  echo "[cycle $cycle $(date +%H:%M)] queue=$queue | $states"

  # ---- 1. pull completed runs not yet local ---------------------------------
  remote_done=$(sh_quiet "for d in $PROJ/aegis-runs/run_exp02_* $PROJ/aegis-runs/run_m0*; do
    [ -f \"\$d/doc02_adjusted_goals.md\" ] && basename \"\$d\"
  done" 2>/dev/null)
  for run_id in $remote_done; do
    if [ ! -d "$RUNS/$run_id" ]; then
      echo "  syncing $run_id"
      bash "$REPO/pipeline/deucalion/sync_down.sh" "$run_id" >/dev/null 2>&1
      # the deliverable export lives under output/<company>/<run_id> on the
      # cluster; pull it flat (the scp nesting quirk sync_down.sh skips)
      mkdir -p "$REPO/output/TinyTask/$run_id"
      scp -q -r "$HOST:$PROJ/aegis-mvp/output/TinyTask/$run_id/" "$REPO/output/TinyTask/$run_id/" 2>/dev/null
      if [ -d "$REPO/output/TinyTask/$run_id/$run_id" ]; then
        mv "$REPO/output/TinyTask/$run_id/$run_id/"* "$REPO/output/TinyTask/$run_id/" 2>/dev/null
        rmdir "$REPO/output/TinyTask/$run_id/$run_id" 2>/dev/null
      fi
    fi
  done

  # ---- 2. refresh the aggregate cache the site reads ------------------------
  python3 "$REPO/scripts/aggregate_runs.py" "$RUNS" --json "$RUNS/_aggregate_cache.json" >/dev/null 2>&1 \
    && echo "  aggregate cache refreshed" || echo "  aggregate cache refresh FAILED (kept previous)"

  # ---- 3. collect finished smokes -------------------------------------------
  python3 "$HOME/Work/aegis-models/deucalion/collect_smoke.py" 2>/dev/null | grep -v "still running" | sed 's/^/  /'

  # ---- 4. drain check --------------------------------------------------------
  if [ "$queue" = "0" ]; then
    echo "QUEUE DRAINED at cycle $cycle — all jobs terminal"
    exit 0
  fi

  sleep "$POLL_SECONDS"
done

echo "monitor window ended after $MAX_CYCLES cycles (queue not drained)"
