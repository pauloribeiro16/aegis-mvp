#!/usr/bin/env bash
# watch_p2.sh — poll the two P2-01 cells, sync them down, verify the artefacts.
#
# PREREG_P2_01 stopping rule: the §6 verdict is decided from these artefacts, so
# the watcher does NOT interpret. It moves the bytes and reports what arrived;
# the gates and the metrics are recomputed locally from the synced run.
set -uo pipefail

RUNS=(run_p2_c2_1996160 run_p2_c3_1996161)
JOBS=(1996172 1996173)          # the phase2 jobs; each waits afterok on its `all`
ALL_JOBS=(1996170 1996171)      # the Phase 1 sweep they depend on
POLL="${MVP_POLL:-120}"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

# squeue/sacct live on the LOGIN NODE, not here. Running them locally resolves
# to "command not found", which under 2>/dev/null is indistinguishable from an
# empty queue — and an empty queue is read as "both jobs are done". That is
# exactly the false signal watch_m11.sh produced (00_RESULTS.md §M11), and it
# is why every scheduler call below goes through ssh and why a failed ssh is a
# hard error rather than an empty answer.
queue_state() {
  local out
  # LogLevel=ERROR matters: this host emits post-quantum key-exchange warnings on
  # every ssh, and with 2>&1 those warnings land in `state`. They are non-empty
  # text, so an empty queue would never look empty and the loop would never
  # exit. The exit status, not the stderr text, is what decides success.
  if ! out="$(ssh -o BatchMode=yes -o ConnectTimeout=30 -o LogLevel=ERROR "$HOST" \
                "squeue -h -j $* -o '%i %T'" 2>/dev/null)"; then
    echo "WATCH FATAL: could not reach $HOST" >&2
    exit 1
  fi
  printf '%s' "$out"
}

for attempt in $(seq 1 240); do
  state="$(queue_state "$(IFS=,; echo "${JOBS[*]}")")"
  if [ -z "$(printf '%s' "$state" | tr -d '[:space:]')" ]; then
    echo "WATCH: both phase2 jobs have left the queue"
    break
  fi
  echo "WATCH: $(date -Is) — still queued: $(printf '%s' "$state" | tr '\n' ' ')"
  sleep "$POLL"
done

# sacct, not squeue: a job that has left the queue has an outcome, and the
# outcome is what decides whether an empty run dir is a bug or a failure.
sacct_jobs="$(IFS=,; echo "${JOBS[*]},${ALL_JOBS[*]}")"
ssh -o BatchMode=yes -o LogLevel=ERROR "$HOST" \
  "sacct -j '$sacct_jobs' --format=JobID,JobName%14,State,ExitCode --noheader" \
  2>/dev/null || true

for r in "${RUNS[@]}"; do
  echo "=== sync down $r"
  bash pipeline/deucalion/sync_down.sh "$r" || echo "WARN: sync_down $r failed"
done
echo "WATCH: done"