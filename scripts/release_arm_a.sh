#!/usr/bin/env bash
# release_arm_a.sh — the staged-release gate for EXP-02 arm A.
#
# Waits for the single validator run (a_r12) to produce a deliverable, syncs
# it, runs the pre-registered integrity controls, and ONLY IF ALL GREEN
# resubmits the 14 remaining arm-A 'all' jobs (their p1 stages already ran and
# their configs are on disk — nothing is recomputed). If validation fails, it
# stops, logs, and releases nothing.
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
VALIDATOR_RUN="run_exp02_a_r12_1978923"
LOG="$RUNS/release_arm_a.log"

echo "[release $(date +%H:%M)] waiting for validator $VALIDATOR_RUN" >> "$LOG"

# ---- 1. wait for the validator's deliverable (up to 3 h) --------------------
for i in $(seq 1 36); do
  if ssh -n -o BatchMode=yes "$HOST" "[ -f $PROJ/aegis-runs/$VALIDATOR_RUN/doc02_adjusted_goals.md ]" 2>/dev/null; then
    echo "[release $(date +%H:%M)] validator deliverable detected" >> "$LOG"
    break
  fi
  if [ "$i" = "36" ]; then
    echo "[release $(date +%H:%M)] TIMEOUT: validator did not finish in 3 h — releasing nothing" >> "$LOG"
    exit 1
  fi
  sleep 300
done

# ---- 2. sync + validate ------------------------------------------------------
bash "$REPO/pipeline/deucalion/sync_down.sh" "$VALIDATOR_RUN" >/dev/null 2>&1
CHECKS=$(python3 "$REPO/scripts/aggregate_runs.py" "$RUNS/$VALIDATOR_RUN" --checks 2>&1)
echo "$CHECKS" >> "$LOG"

GREEN=true
echo "$CHECKS" | grep -q "runs without aegis_git_rev : 0" || GREEN=false
echo "$CHECKS" | grep -q "runs without config.json   : 0" || GREEN=false
echo "$CHECKS" | grep -q "runs with an aborted stage  : 0" || GREEN=false
L1=$(python3 -c "
import json,sys
d=json.load(open('$RUNS/_aggregate_cache.json')) if False else None
" 2>/dev/null)
if ! echo "$CHECKS" | grep -q "PASS"; then GREEN=false; fi

if [ "$GREEN" != "true" ]; then
  echo "[release $(date +%H:%M)] VALIDATION FAILED — releasing nothing; inspect $LOG" >> "$LOG"
  exit 1
fi
echo "[release $(date +%H:%M)] validator GREEN — releasing the 14 remaining arm-A runs" >> "$LOG"

# ---- 3. resubmit the 14 'all' jobs (p1 stages already complete) -------------
released=0
while IFS=$'\t' read -r order arm repeat seed temp; do
  case "$order" in ''|'#'*) continue ;; esac
  [ "$arm" = "A" ] || continue
  [ "$order" = "34" ] && continue   # r12 is the validator, already done
  tag="exp02_a_r$(printf '%02d' "$repeat")"
  # submissions-log lines are SPACE-separated: "34 exp02_a_r01 p1=... all=..."
  p1_job=$(grep "^${order} ${tag} p1=" "$RUNS/exp02_submissions.log" | head -1 | sed 's/.*p1=\([0-9]*\).*/\1/')
  [ -z "$p1_job" ] && { echo "[release] no p1 job for $tag — skipped" >> "$LOG"; continue; }
  out=$(ssh -n -o BatchMode=yes "$HOST" "cd '$PROJ/aegis-mvp' && env MVP_RUN_TAG=$tag MVP_RUN_ID=run_${tag}_${p1_job} MVP_ARM=A MVP_REPEAT=$repeat MVP_PREAPPROVE_GATES=1 MVP_TEMPERATURE=0.2 MVP_DEPENDENCY=afterok:${p1_job} bash pipeline/deucalion/submit.sh all" 2>/dev/null | awk '/Submitted batch job/{print $4}')
  if [ -n "$out" ]; then
    echo "[release $(date +%H:%M)] $tag all=$out (dep afterok:$p1_job)" >> "$LOG"
    released=$((released + 1))
  else
    echo "[release $(date +%H:%M)] $tag SUBMISSION FAILED" >> "$LOG"
  fi
done < "$REPO/pipeline/deucalion/exp02_schedule.tsv"

echo "[release $(date +%H:%M)] done: $released arm-A runs released" >> "$LOG"
