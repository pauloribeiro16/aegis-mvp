#!/usr/bin/env bash
# release_screening.sh — staged release for the model-lab Tier 1.
#
# Waits for the screening validator (m01_gemma4_r01, all job 1978999). If it
# completes green (deliverable + L1 PASS), launches the remaining screening
# runs for the four smoke-pass models (n=5 each via launch_battery.sh, which
# skips already-logged entries). If it fails, releases nothing and logs why.
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LAB="$HOME/Work/aegis-models"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
ALL_JOB="1978999"
LOG="$LAB/results/release_screening.log"

echo "[screening $(date +%H:%M)] waiting for validator m01_gemma4_r01 (all=$ALL_JOB)" >> "$LOG"

for i in $(seq 1 60); do
  STATE=$(ssh -n -o BatchMode=yes "$HOST" "sacct -X -n -j $ALL_JOB --format=State | head -1 | tr -d ' '" 2>/dev/null)
  case "$STATE" in
    COMPLETED|FAILED|CANCELLED*|TIMEOUT|OUT_OF_*) break ;;
  esac
  [ "$i" = "60" ] && { echo "[screening] TIMEOUT after 5 h — releasing nothing" >> "$LOG"; exit 1; }
  sleep 300
done

echo "[screening $(date +%H:%M)] validator terminal: $STATE" >> "$LOG"

if [ "$STATE" != "COMPLETED" ]; then
  ssh -n -o BatchMode=yes "$HOST" "tail -6 $PROJ/aegis-runs/run_m01_gemma4_r01_1978998/logs/run_all_${ALL_JOB}.log" >> "$LOG" 2>/dev/null
  echo "[screening] validator FAILED — releasing nothing; inspect $LOG" >> "$LOG"
  exit 1
fi

# sync + mechanical validation
bash "$REPO/pipeline/deucalion/sync_down.sh" run_m01_gemma4_r01_1978998 >/dev/null 2>&1
python3 "$REPO/scripts/aggregate_runs.py" "$RUNS/run_m01_gemma4_r01_1978998" --checks >> "$LOG" 2>&1
# the L1 verdict shows in the run table's L1 column
GREEN=$(python3 "$REPO/scripts/aggregate_runs.py" "$RUNS/run_m01_gemma4_r01_1978998" 2>/dev/null | grep -cE "run_m01_gemma4_r01_1978998 .*PASS")
if [ "$GREEN" = "0" ]; then
  echo "[screening $(date +%H:%M)] validator ran but L1 did not PASS — releasing nothing" >> "$LOG"
  exit 1
fi
echo "[screening $(date +%H:%M)] validator GREEN (L1 PASS) — releasing remaining screening runs" >> "$LOG"

# remaining 19: gemma4 r02-r05 + 5 each for glm47, muse, nemotron
for MODEL in gemma4:31b glm-4.7-flash:latest muse-glimmer:30b nemotron-3.5-lightning:30b; do
  bash "$LAB/deucalion/launch_battery.sh" "$MODEL" --n 5 >> "$LOG" 2>&1
done
echo "[screening $(date +%H:%M)] release complete — see battery_*_submissions.log" >> "$LOG"
