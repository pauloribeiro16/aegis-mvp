#!/usr/bin/env bash
# launch_exp02.sh — submit the EXP-02 battery on the Deucalion LOGIN node.
#
# For each schedule entry: submit p1 (creates the run dir + config.json), parse
# the job id, then submit `all` (p2→…→p5) with --dependency=afterok:<p1job> so
# the two jobs of one run can never interleave. Gates are pre-approved per
# PREREG_01 §3 (declared fixed condition); the runner writes the markers.
#
# Usage:  bash pipeline/deucalion/launch_exp02.sh [--limit N] [--from N]
#   --limit N   submit only the first N pending entries (default: all pending)
#   --from N    start at schedule order N (default 1)
#   Entries already recorded in the submissions log are skipped, so the driver
#   is resumable: re-running it never duplicates a run. The log line is written
#   with all=pending the moment p1 is accepted, so a failure in between costs
#   an `all` resubmission, never a duplicate p1.
set -euo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
SCHEDULE="$(cd "$(dirname "$0")" && pwd)/exp02_schedule.tsv"
# Driver state lives on the WORKSTATION (the driver is the only writer, and it
# only runs from here). The evidence of what was submitted lives in each run's
# manifest and in the schedule file; this log is just the resume cursor.
LOG="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}/exp02_submissions.log"

LIMIT=999
FROM=1
while [ $# -gt 0 ]; do
  case "$1" in
    --limit) LIMIT="$2"; shift 2 ;;
    --from)  FROM="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$(dirname "$LOG")"
touch "$LOG"

submitted=0
skipped=0
# IFS=tab is REQUIRED: arm A's seed field is EMPTY, and with default
# whitespace-IFS consecutive delimiters collapse, shifting every later field
# left — the temperature landed in --seed and killed all 15 arm-A p1 jobs
# (a_r01..a_r15, job range 1978599-1978673). Found by their job logs.
while IFS=$'\t' read -r order arm repeat seed temp; do
  case "$order" in ''|\#*) continue ;; esac
  # 'none' is the schedule's explicit no-seed marker ('' cannot survive bash read)
  [ "$seed" = "none" ] && seed=""
  [ "$order" -lt "$FROM" ] && continue
  [ "$submitted" -ge "$LIMIT" ] && break
  tag="exp02_${arm,,}_r$(printf '%02d' "$repeat")"
  if grep -q "^${order} ${tag} p1=" "$LOG"; then
    skipped=$((skipped + 1))
    continue
  fi

  # ---- p1: create the run (config.json is written here) ---------------------
  exports="MVP_RUN_TAG=${tag} MVP_ARM=${arm} MVP_REPEAT=${repeat} MVP_PREAPPROVE_GATES=1"
  [ -n "$seed" ] && exports="$exports MVP_SEED=${seed}"
  exports="$exports MVP_TEMPERATURE=${temp}"
  p1_out=$(ssh -n "$HOST" "cd '$PROJ/aegis-mvp' && env $exports bash pipeline/deucalion/submit.sh p1") || true
  p1_job=$(echo "$p1_out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$p1_job" ]; then
    echo "FATAL: order $order ($tag): p1 submission failed:" >&2
    echo "$p1_out" >&2
    exit 1
  fi
  echo "${order} ${tag} p1=${p1_job} all=pending seed=${seed:-none} temp=${temp}" >> "$LOG"

  # ---- all: the rest of the pipeline, only after p1 succeeded ---------------
  all_out=$(ssh -n "$HOST" "cd '$PROJ/aegis-mvp' && env $exports MVP_RUN_ID=run_${tag}_${p1_job} MVP_DEPENDENCY=afterok:${p1_job} bash pipeline/deucalion/submit.sh all") || true
  all_job=$(echo "$all_out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$all_job" ]; then
    sed -i "s|^${order} ${tag} p1=${p1_job} all=pending|${order} ${tag} p1=${p1_job} all=failed|" "$LOG"
    echo "FATAL: order $order ($tag): 'all' submission failed:" >&2
    echo "$all_out" >&2
    exit 1
  fi
  sed -i "s|^${order} ${tag} p1=${p1_job} all=pending|${order} ${tag} p1=${p1_job} all=${all_job}|" "$LOG"
  submitted=$((submitted + 1))
  echo "submitted: order=$order $tag (p1=$p1_job, all=$all_job dep=afterok:$p1_job)"
done < "$SCHEDULE"

echo
echo "done: $submitted submitted, $skipped already logged (total in log: $(wc -l < "$LOG"))"
