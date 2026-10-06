#!/usr/bin/env bash
# spend_cpu_budget.sh — spend a fraction of the project's CPU budget (CPU-hours).
# Run ON the Deucalion login node (or: ssh login 'bash -s' < pipeline/deucalion/spend_cpu_budget.sh).
#
# The CPU budget lives in Slurm as an enforced cap on the CPU account:
#   scontrol show assoc ... GrpTRESMins=cpu=LIMIT(CONSUMED)   [CPU-minutes]
# The script reads both numbers live, computes what is still missing to reach
# the target fraction (default 30% of the cap), and submits waves of array jobs
# (1 full x86 node of N cores per array task) chained with afterany. The last
# wave's walltime is exact to the minute, so the total lands just AT the target
# (ceil overshoot < one wave-minute per wave). Without --go it only prints the
# plan and runs sbatch --test-only as preflight — nothing is submitted.
#
# Usage: bash pipeline/deucalion/spend_cpu_budget.sh [--go]
#          [--frac 0.30] [--nodes 64] [--account ACCT] [--partition normal-x86]
#          [--max-hours H]        # per-wave walltime cap (default: MaxTime-1h)
#          [--total-hours N]      # only if the account has no cap in Slurm
#          [--cmdfile PATH]       # run real work instead of the CPU burn loop
# Cancel everything:  scancel -n budget_spend
# Live consumption:   scontrol show assoc user $USER account ACCT | grep GrpTRESMins
set -euo pipefail

FRAC=0.30; NODES=64; PART=normal-x86; ACCT=""; MAX_H=""; TOTAL_H=""; CMD=""; GO=0
while [ $# -gt 0 ]; do case "$1" in
  --go) GO=1 ;;
  --frac) FRAC="$2"; shift ;;
  --nodes) NODES="$2"; shift ;;
  --account) ACCT="$2"; shift ;;
  --partition) PART="$2"; shift ;;
  --max-hours) MAX_H="$2"; shift ;;
  --total-hours) TOTAL_H="$2"; shift ;;
  --cmdfile) CMD="$2"; shift ;;
  *) echo "FATAL: unknown arg '$1'" >&2; exit 2 ;;
esac; shift; done
if [ -n "$CMD" ] && [ ! -e "$CMD" ]; then
  echo "FATAL: --cmdfile '$CMD' not visible from the login node" >&2; exit 2
fi

# --- account (default: the user's Slurm default account) ---------------------
if [ -z "$ACCT" ]; then
  ACCT=$(sacctmgr -nP show user "$USER" format=DefaultAccount 2>/dev/null | head -1)
  [ -n "$ACCT" ] || ACCT=$(scontrol show assoc user="$USER" | sed -n 's/.*DefAccount=\([^ ]*\).*/\1/p' | head -1)
fi
[ -n "$ACCT" ] || { echo "FATAL: could not determine the account; pass --account" >&2; exit 2; }
# The GPU account (suffix 'g') is rejected by the x86 partitions (KG gotcha);
# catch the mix-up before Slurm does.
case "$PART" in *x86*) case "$ACCT" in *x) ;; *)
  echo "WARN: account '$ACCT' does not end in 'x' — GPU accounts are rejected on $PART" >&2 ;; esac ;; esac

# --- budget cap + consumption (CPU-minutes) ----------------------------------
ASSOC=$(scontrol show assoc user="$USER" account="$ACCT" 2>/dev/null | grep -m1 'GrpTRESMins=' || true)
LIMIT_MIN=$(sed -n 's/.*[ =]cpu=\([0-9]*\)([0-9]*).*/\1/p' <<< "${ASSOC:-}")
CONS_MIN=$(sed -n 's/.*[ =]cpu=[0-9]*(\([0-9]*\)).*/\1/p' <<< "${ASSOC:-}"); CONS_MIN=${CONS_MIN:-0}
if [ -n "$LIMIT_MIN" ] && [ "$LIMIT_MIN" != "N" ]; then
  SRC="Slurm cap on account $ACCT (GrpTRESMins)"
elif [ -n "$TOTAL_H" ]; then
  LIMIT_MIN=$(( TOTAL_H * 60 )); SRC="--total-hours $TOTAL_H (no cap visible in Slurm)"
else
  echo "FATAL: no budget cap visible for account '$ACCT'; pass --total-hours N" >&2; exit 2
fi

CPUS=$(sinfo -h -p "$PART" -o %c | head -1)
case "$CPUS" in ''|*[!0-9]*) echo "FATAL: bad cores-per-node '$CPUS' for partition $PART" >&2; exit 2 ;; esac
if [ -z "$MAX_H" ]; then
  MAXT=$(sinfo -h -p "$PART" -o %l | head -1)   # e.g. 2-00:00:00
  MAX_MIN=$(echo "$MAXT" | awk -F'[-:]' '{if(NF==4)print $1*1440+$2*60+$3;else print $1*60+$2}')
  MAX_MIN=$(( MAX_MIN - 60 )); [ "$MAX_MIN" -lt 1 ] && MAX_MIN=1
else
  MAX_MIN=$(( MAX_H * 60 ))
fi

TARGET_MIN=$(awk -v l="$LIMIT_MIN" -v f="$FRAC" 'BEGIN{printf "%.0f", l*f}')
TODO_MIN=$(( TARGET_MIN - CONS_MIN ))
h() { awk -v m="$1" 'BEGIN{printf "%.1f", m/60}'; }

echo "=== budget spend — plan $( [ "$GO" = 1 ] || echo '(DRY-RUN, nothing submitted)' ) ==="
echo "account: $ACCT   partition: $PART   cores/node: $CPUS   nodes/wave: $NODES   max wave: $((MAX_MIN/60))h"
echo "budget total: $LIMIT_MIN CPU-min = $(h "$LIMIT_MIN") CPU-h   [$SRC]"
echo "consumed:     $CONS_MIN CPU-min = $(h "$CONS_MIN") CPU-h"
echo "target ($FRAC): $TARGET_MIN CPU-min = $(h "$TARGET_MIN") CPU-h"
if [ "$TODO_MIN" -le 0 ]; then
  echo "nothing to do: consumption already at or above the target fraction"
  exit 0
fi
echo "to spend now: $TODO_MIN CPU-min = $(h "$TODO_MIN") CPU-h"

# --- plan: each array task = 1 whole node for T minutes ----------------------
PERH=$(( NODES * CPUS ))                       # CPU-min per wave-minute
WAVES=$(( (TODO_MIN + PERH*MAX_MIN - 1) / (PERH*MAX_MIN) ))
remaining=$TODO_MIN
for w in $(seq 1 "$WAVES"); do
  T_MIN=$(( (remaining + PERH - 1) / PERH )); if [ "$T_MIN" -gt "$MAX_MIN" ]; then T_MIN=$MAX_MIN; fi
  spend=$(( PERH * T_MIN )); remaining=$(( remaining - spend ))
  echo "wave $w/$WAVES: array=1-${NODES}  --time=${T_MIN}  ->  $(h "$spend") CPU-h"
done
EST=$(( TODO_MIN - remaining ))
echo "estimated total: $(h "$EST") CPU-h  (final fraction: $(awk -v c=$((CONS_MIN + EST)) -v l="$LIMIT_MIN" 'BEGIN{printf "%.2f%%", 100*c/l}'))"
LOGDIR="${SPEND_LOGDIR:-/projects/F202512235CPCAA1/budget_spend_logs}"   # $HOME has a tight quota; use the project NFS space
echo "cancel everything: scancel -n budget_spend   |   logs: $LOGDIR/"
mkdir -p "$LOGDIR" 2>/dev/null || echo "WARN: cannot create $LOGDIR (quota?) — logs will fail, submission continues"

# shared sbatch args; wave 1 doubles as the --test-only preflight
BASE=(--account="$ACCT" --partition="$PART" --job-name=budget_spend
      --nodes=1 --ntasks="$CPUS" --cpus-per-task=1)
if [ -n "$CMD" ]; then WRAP="bash $CMD"; else WRAP='echo "[budget_spend] $(hostname) $(date -Is)"; while :; do :; done'; fi

if [ "$GO" != 1 ]; then
  echo "preflight (sbatch --test-only):"
  sbatch --test-only "${BASE[@]}" --array=1-1 --time="$T_MIN" --wrap="while :; do :; done"
  echo "preflight OK — re-run with --go to submit"
  exit 0
fi

sbatch --test-only "${BASE[@]}" --array=1-1 --time="$T_MIN" --wrap="while :; do :; done"
prev=""; remaining=$TODO_MIN; echo "submitted:"
for w in $(seq 1 "$WAVES"); do
  T_MIN=$(( (remaining + PERH - 1) / PERH )); if [ "$T_MIN" -gt "$MAX_MIN" ]; then T_MIN=$MAX_MIN; fi
  ARGS=(sbatch --parsable "${BASE[@]}" --array=1-${NODES} --time="$T_MIN"
        --output="$LOGDIR/%A_%a.out" --wrap="$WRAP")
  if [ -n "$prev" ]; then ARGS+=(--dependency="afterany:$prev"); fi
  id=$("${ARGS[@]}")
  echo "  wave $w/$WAVES: array=$id time=${T_MIN}min${prev:+ (after $prev)}"
  prev=$id; remaining=$(( remaining - PERH * T_MIN ))
done
echo "all waves queued — follow with: squeue -u \$USER -n budget_spend"
