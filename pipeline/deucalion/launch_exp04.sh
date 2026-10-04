#!/usr/bin/env bash
# launch_exp04.sh — the prompt ablation, in the seeded (arm-B) configuration.
#
# Question (PREREG_01 H7): does the P4 adjustment DECISION RULE (shipped,
# v1.5.0) increase calibration relative to a closed 3-value MENU with no
# decision procedure, at n=15 per arm?
#
#   Arm R = rule (shipped behaviour)                      -> exp04_r_NN
#   Arm M = menu  (MVP_P4_ADJUSTMENT=menu)                -> exp04_m_NN
#
# Both arms: seed 42, temperature 0.2, pre-approved gates. The ONLY difference
# is the P4 adjustment instruction block — the exemplar is pinned
# (compose.golden_text), so the prompt is a constant of the design in both arms.
#
# Staged release, per the researcher rule: `--validate` submits ONE run per arm
# and stops; the remaining n-1 release only after both go green.
set -uo pipefail

HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
LOG="$RUNS/exp04_submissions.log"
N="${MVP_N:-15}"
MODE="${1:-all}"

mkdir -p "$(dirname "$LOG")"
touch "$LOG"

submit_one() { # $1=tag $2=repeat-index $3=variant (none|menu)
  local tag="$1" rep="$2" variant="$3" exports out job job2
  exports="MVP_RUN_TAG=${tag} MVP_ARM=${tag#exp04_} MVP_REPEAT=${rep} MVP_SEED=42"
  exports="$exports MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1"
  [ "$variant" = "menu" ] && exports="$exports MVP_P4_ADJUSTMENT=menu"

  out=$(ssh -n -o BatchMode=yes "$HOST" "cd '$PROJ/aegis-mvp' && env $exports bash pipeline/deucalion/submit.sh p1" 2>/dev/null)
  job=$(echo "$out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$job" ]; then echo "FATAL: $tag p1 failed: $out" >&2; return 1; fi
  echo "${tag} p1=${job} all=pending variant=${variant}" >> "$LOG"

  out=$(ssh -n -o BatchMode=yes "$HOST" "cd '$PROJ/aegis-mvp' && env $exports MVP_RUN_ID=run_${tag}_${job} MVP_DEPENDENCY=afterok:${job} bash pipeline/deucalion/submit.sh all" 2>/dev/null)
  job2=$(echo "$out" | awk '/Submitted batch job/{print $4}')
  if [ -z "$job2" ]; then
    sed -i "s|^${tag} p1=${job} all=pending|${tag} p1=${job} all=failed|" "$LOG"
    echo "FATAL: $tag all failed: $out" >&2; return 1
  fi
  sed -i "s|^${tag} p1=${job} all=pending|${tag} p1=${job} all=${job2}|" "$LOG"
  echo "submitted $tag (p1=$job all=$job2, variant=$variant)"
  return 0
}

if [ "$MODE" = "--validate" ]; then
  submit_one exp04_r01 1 none || exit 1
  submit_one exp04_m01 1 menu || exit 1
  echo "validation pair submitted; release the rest only after both go green"
  exit 0
fi

limit="$N"
[ "$MODE" = "--rest" ] && limit=$((N + 1))   # --rest skips run 01
for i in $(seq 1 "$limit"); do
  R=$(printf '%02d' "$i")
  [ "$i" = "1" ] && [ "$MODE" = "--rest" ] && continue
  for spec in "exp04_r_${R} $R none" "exp04_m_${R} $R menu"; do
    set -- $spec
    grep -q "^$1 p1=" "$LOG" && continue
    submit_one "$1" "$2" "$3" || exit 1
  done
done
echo "done — see $LOG"
