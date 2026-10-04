#!/usr/bin/env bash
# submit_case03.sh — retry Case_03's p4p5 submission until the network lets it
# through, then watch it. The local <-> cluster link has been intermittently
# dropping, and a submission that "failed" with no output is usually the link,
# not Slurm.
set -uo pipefail

IP=194.210.49.25
PROJ=/projects/F202512235CPCAA1/mvp-pipeline
LOG=/tmp/case03_submit.log

say() { echo "[$(date +%H:%M)] $*" >> "$LOG"; }

submit() {
  local out
  out=$(ssh -n -o BatchMode=yes -o ConnectTimeout=60 -o HostName=login.deucalion.macc.fccn.pt \
        "paulinho@$IP" \
        "cd $PROJ/aegis-mvp && env MVP_RUN_TAG=sec03_p1 MVP_RUN_ID=run_sec03_p1_1979371 \
         MVP_SEED=42 MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1 \
         bash pipeline/deucalion/submit.sh p4p5 'Case_03_OmniBank'" 2>/dev/null)
  echo "$out" | awk '/Submitted batch job/{print $4; exit}'
}

# --- land the submission (up to ~40 min of retries) -------------------------
JOB=""
for i in $(seq 1 40); do
  JOB=$(submit)
  if [ -n "$JOB" ]; then say "case03 p4p5 submitted: $JOB"; break; fi
  sleep 60
done
if [ -z "$JOB" ]; then say "case03: could not submit after 40 attempts — giving up"; exit 1; fi

# --- watch both case runs, then sync and aggregate ---------------------------
for i in $(seq 1 60); do
  sleep 420
  LINE=$(ssh -n -o BatchMode=yes -o ConnectTimeout=60 -o HostName=login.deucalion.macc.fccn.pt \
         "paulinho@$IP" \
         "sacct -X -n -j 1979948,$JOB --format=JobID%10,State%10 | tr '\n' ' '" 2>/dev/null)
  [ -z "$LINE" ] && { say "watch: no response"; continue; }
  say "$LINE"
  DONE=$(echo "$LINE" | grep -oE "COMPLETED|FAILED|CANCELLED" | wc -l)
  if [ "$DONE" -ge 2 ]; then
    say "both terminal"
    for R in run_sec02_p1_1979370 run_sec03_p1_1979371; do
      bash /home/paulinho/Work/aegis-mvp/pipeline/deucalion/sync_down.sh "$R" >/dev/null 2>&1 \
        && say "synced $R"
    done
    python3 /home/paulinho/Work/aegis-mvp/scripts/aggregate_runs.py ~/Work/aegis-runs \
      --json ~/Work/aegis-runs/_aggregate_cache.json >/dev/null 2>&1 && say "cache refreshed"
    exit 0
  fi
done
say "watch window ended"
