#!/usr/bin/env bash
# resume_cases.sh — land the two remaining case runs, then watch and sync.
#
# Case_02: p4 completed all 13 remaining sub-domains and p4t completed; p5 was
#          the stage that failed, on the SR-token bug now fixed.
# Case_03: p3f was never run (framing.md missing), so the chain restarts at p3f.
#
# The local <-> cluster link drops intermittently, so every step retries and a
# step is only considered landed once the JOB LOG confirms the right stage.
set -uo pipefail

IP=194.210.49.25
PROJ=/projects/F202512235CPCAA1/mvp-pipeline
REPO=/home/paulinho/Work/aegis-mvp
LOG=/tmp/cases_resume.log
say() { echo "[$(date +%H:%M)] $*" >> "$LOG"; }

S() {
  local out
  out=$(ssh -n -o BatchMode=yes -o ConnectTimeout=60 -o HostName=login.deucalion.mcc.fccn.pt \
        "paulinho@$IP" "$1" 2>/dev/null)
  echo "$out"
}

submit() { # 1=tag 2=run_id 3=case 4=stage
  S "cd $PROJ/aegis-mvp && env MVP_RUN_TAG=$1 MVP_RUN_ID=$2 MVP_SEED=42 \
     MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1 \
     bash pipeline/deucalion/submit.sh $4 '$3'" | awk '/Submitted batch job/{print $4; exit}'
}

confirm() { # 1=run_dir 2=job 3=expected stage substring
  S "grep -c 'stage=$3' $PROJ/aegis-runs/$1/logs/${2:+$2}_*.log 2>/dev/null | head -1"
}

wait_terminal() {
  local i
  for i in $(seq 1 90); do
    local st
    st=$(S "sacct -X -n -j $1 --format=State" | head -1 | tr -d ' ')
    case "$st" in COMPLETED|FAILED|CANCELLED*) echo "$st"; return ;; esac
    sleep 420
  done
  echo TIMEOUT
}

# ---- Case 03: p3f, then the rest -----------------------------------------
J3F=""
for i in $(seq 1 30); do
  J3F=$(submit sec03_p1 run_sec03_p1_1979371 Case_03_OmniBank p3f)
  [ -n "$J3F" ] && { say "case03 p3f submitted: $J3F"; break; }
  sleep 60
done
if [ -z "$J3F" ]; then say "case03 p3f: could not submit"; exit 1; fi
say "case03 p3f: $(wait_terminal "$J3F")"

J3=""
for i in $(seq 1 30); do
  J3=$(submit sec03_p1 run_sec03_p1_1979371 Case_03_OmniBank p4p5)
  [ -n "$J3" ] && { say "case03 p4p5 submitted: $J3"; break; }
  sleep 60
done
[ -z "$J3" ] && { say "case03 p4p5: could not submit"; exit 1; }

# ---- Case 02: p5 only (p4 and p4t already completed) -----------------------
J2=""
for i in $(seq 1 30); do
  J2=$(submit sec02_p1 run_sec02_p1_1979370 Case_02_SecureBorder_Solutions p5)
  [ -n "$J2" ] && { say "case02 p5 submitted: $J2"; break; }
  sleep 60
done
[ -z "$J2" ] && { say "case02 p5: could not submit"; exit 1; }

# ---- watch both, then sync --------------------------------------------------
for i in $(seq 1 90); do
  sleep 420
  LINE=$(S "sacct -X -n -j $J3,$J2 --format=JobID%10,State%10 | tr '\n' ' '")
  [ -z "$LINE" ] && { say "watch: no response"; continue; }
  say "$LINE"
  DONE=$(echo "$LINE" | grep -oE "COMPLETED|FAILED|CANCELLED" | wc -l)
  if [ "$DONE" -ge 2 ]; then
    say "both terminal"
    for R in run_sec02_p1_1979370 run_sec03_p1_1979371; do
      bash "$REPO/pipeline/deucalion/sync_down.sh" "$R" >/dev/null 2>&1 && say "synced $R"
    done
    python3 "$REPO/scripts/aggregate_runs.py" ~/Work/aegis-runs \
      --json ~/Work/aegis-runs/_aggregate_cache.json >/dev/null 2>&1 && say "cache refreshed"
    exit 0
  fi
done
say "watch window ended"
