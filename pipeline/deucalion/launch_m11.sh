#!/usr/bin/env bash
# launch_m09.sh — the calibration-instruction ablation (PREREG_M09, frozen
# 2026-10-07 before any run of either arm).
#
# Question: does the p4 instruction's COMPANY IMPLICATION CLAUSE — the span carrying two
# literal goal exemplars and three literal adjustment rationales — or the
# worked example, drive the default-collapse M07 measured on the reference
# (ratio 0.99, zero `proportional`, zero `inherited`)? M09 varies only the
# instruction; the exemplar is pinned by compose.golden_text.
#
#   Arm CTRL = shipped style tail                 -> m09_<case>_ctrl
#   Arm META = structural criteria, 0 exemplars   -> m09_<case>_meta
#
# Both arms: qwen3.8:27b, seed 42, temperature 0.2, pre-approved gates, the
# same commit, the same pinned exemplar. The ONLY difference is
# ficha_overrides.p4_instruction, read from config.json — never from the tag.
# The two arms are distinguishable in each run by prompt_digests.p4_instruction.
#
# n=1 per cell: under a fixed seed EXP-02 established bit-reproducibility
# (15 seeded runs byte-identical, retention sd 0.0000), so one run carries the
# arm's whole distribution. Same logic as M07's cells.
#
# Usage: bash pipeline/deucalion/launch_m11.sh            # all four cells
#        bash pipeline/deucalion/launch_m09.sh --check    # dry run, submits nothing
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
LOG="$RUNS/m11_submissions.log"
MODEL="${MVP_MODEL:-qwen3.8:27b}"
DRY="${1:-}"

CASES=("Case_02_SecureBorder_Solutions" "Case_03_OmniBank")

mkdir -p "$(dirname "$LOG")"
touch "$LOG"

short_case() { echo "c${1:6:1}"; }   # Case_02 -> c2, Case_03 -> c3

submit_cell() { # $1=case  $2=arm (ctrl|meta)
  local case_name="$1" arm="$2" exports out job job2
  local tag="m11_$(short_case "$case_name")_${arm}"

  grep -q "^$tag p1=" "$LOG" && { echo "skip $tag (already in $LOG)"; return 0; }
  [ "$DRY" = "--check" ] && { echo "would submit $tag ($case_name, $arm)"; return 0; }

  exports="MVP_RUN_TAG=${tag} MVP_ARM=${arm} MVP_REPEAT=1 MVP_SEED=42"
  exports="$exports MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1 MVP_MODEL=${MODEL}"
  [ "$arm" = "concrete" ] && exports="$exports MVP_P4_IMPLICATION=concrete"

  out=$(ssh -n -o BatchMode=yes "$HOST" "cd '$PROJ/aegis-mvp' && env $exports bash pipeline/deucalion/submit.sh p1 '$case_name'" 2>&1)
  job=$(echo "$out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$job" ]; then
    echo "FATAL: $tag p1 failed:" >&2; echo "$out" | tail -5 >&2; return 1
  fi
  echo "${tag} p1=${job} all=pending case=${case_name} arm=${arm}" >> "$LOG"

  out=$(ssh -n -o BatchMode=yes "$HOST" "cd '$PROJ/aegis-mvp' && env $exports MVP_RUN_ID=run_${tag}_${job} MVP_DEPENDENCY=afterok:${job} bash pipeline/deucalion/submit.sh all '$case_name'" 2>&1)
  job2=$(echo "$out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$job2" ]; then
    sed -i "s|^${tag} p1=${job} all=pending|${tag} p1=${job} all=failed|" "$LOG"
    echo "FATAL: $tag all failed:" >&2; echo "$out" | tail -5 >&2; return 1
  fi
  sed -i "s|^${tag} p1=${job} all=pending|${tag} p1=${job} all=${job2} run=run_${tag}_${job}|" "$LOG"
  echo "submitted $tag  p1=$job  all=$job2  run=run_${tag}_${job}"
  return 0
}

for c in "${CASES[@]}"; do
  for a in ctrl concrete; do
    submit_cell "$c" "$a" || exit 1
  done
done

echo
echo "submission log: $LOG"
[ "$DRY" = "--check" ] && exit 0
echo "watch:  bash pipeline/deucalion/watch_m11.sh"