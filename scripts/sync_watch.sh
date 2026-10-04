#!/usr/bin/env bash
# sync_watch.sh — poll the cluster, pull finished runs down, report deltas.
#
# The site reads $AEGIS_RUNS_DIR on the workstation. A run that closed on the
# cluster but was never pulled down is invisible there, which is how 50 runs
# (including the whole glm47 and nemotron batteries) went missing from the view
# while existing on the cluster. This is the tube that fills the page.
#
# Usage: bash scripts/sync_watch.sh [rounds] [sleep_seconds]
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
RUNS_DIR="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
ROUNDS="${1:-40}"
SLEEP="${2:-120}"
LOG="/tmp/sync_watch.log"

stamp() { date -Is; }

for i in $(seq 1 "$ROUNDS"); do
  q=$(ssh -n -o ConnectTimeout=20 "$HOST" "squeue -u \$USER -h | wc -l" 2>/dev/null | tr -d ' ')
  remote=$(ssh -n -o ConnectTimeout=20 "$HOST" \
    "ls -1 '$PROJ/aegis-runs/'" 2>/dev/null | grep '^run_')
  local=$(ls -1 "$RUNS_DIR" 2>/dev/null | grep '^run_')
  missing=$(comm -23 <(echo "$remote" | sort) <(echo "$local" | sort))

  # Only pull runs whose job has actually ended. The trap in phase1.sbatch
  # writes "END=… EXIT_CODE=" once, at job end; a "stage finished rc=" line
  # appears at EVERY stage boundary, and matching it pulled mid-flight runs
  # (four, on 2026-10-04) that the inspector then read as aborted.
  pulled=0
  for r in $missing; do
    done_marker=$(ssh -n -o ConnectTimeout=20 "$HOST" \
      "grep -l '^END=.*EXIT_CODE=' '$PROJ/aegis-runs/$r'/logs/*.log 2>/dev/null | head -1" 2>/dev/null)
    [ -z "$done_marker" ] && continue
    # a run whose LAST stage ended in a failure is still evidence — pull it too,
    # but only once the job is no longer in the queue (checked below)
    rsync -a -e "ssh" "$HOST:$PROJ/aegis-runs/$r" "$RUNS_DIR/" >/dev/null 2>&1 && pulled=$((pulled + 1))
  done

  echo "$(stamp) round $i/$ROUNDS queue=${q:-?} missing=${missing:+$(echo $missing | wc -w)} pulled=$pulled" >> "$LOG"
  tail -3 "$LOG"

  [ "${q:-1}" = "0" ] && [ -z "$missing" ] && { echo "$(stamp) queue empty and nothing outstanding — done" >> "$LOG"; break; }
  sleep "$SLEEP"
done
