#!/usr/bin/env bash
# run_lab.sh — build a lab payload, apply one overlay, ship and submit on Deucalion.
# Usage:
#   bash lab/run_lab.sh <variant> <model> <case>   # submit (p1 + chained all)
#   bash lab/run_lab.sh pull <variant>             # pull that variant's runs locally
# Production pipeline is never modified: the overlay applies to a copy shipped to
# $PROJ/mvp-lab/<variant>/, runs land in $PROJ/mvp-lab/aegis-runs/ (cluster) and
# ~/Work/aegis-runs-lab/ (local).
set -euo pipefail

VARIANT="${1:?usage: run_lab.sh <variant> <model> <case> | pull <variant>}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
LAB_ROOT="$PROJ/mvp-lab"
LAB_RUNS="$LAB_ROOT/aegis-runs"

if [ "$VARIANT" = "pull" ]; then
  PULL_V="${2:?usage: run_lab.sh pull <variant>}"
  mkdir -p "$HOME/Work/aegis-runs-lab"
  for R in $(ssh "$HOST" "ls -1 '$LAB_RUNS' 2>/dev/null | grep '^run_lab_${PULL_V}_' || true"); do
    echo "pulling $R"
    scp -q -r "$HOST:$LAB_RUNS/$R" "$HOME/Work/aegis-runs-lab/"
  done
  echo "done — runs under ~/Work/aegis-runs-lab/"
  exit 0
fi

MODEL="${2:?model tag required}"
CASE="${3:?case name required}"
# variant tag uses dashes (lab01-qwen35-fence); overlay files use underscores
BUILD="/tmp/aegis-lab/$VARIANT"
# variant ending in -schema uses the E-01 serving-layer patch instead of a text overlay
case "$VARIANT" in
  *-schema|*-json)
    E01=1
    ;;
  *-cardsplit* | lab02-*)
    E01=0
    CARDSPLIT=1
    ;;
  *)
    E01=0
    CARDSPLIT=0
    OVERLAY="lab/overlays/$(echo "$VARIANT" | tr '-' '_').py"
    [ -f "$OVERLAY" ] || { echo "no overlay for variant $VARIANT (looked for $OVERLAY)"; exit 1; }
    ;;
esac

rm -rf "$BUILD"; mkdir -p "$BUILD"
cd "$REPO_ROOT"
cp -r pipeline docs/pipeline baseline/domains baseline/MAPPINGS baseline/CONTROLS \
   templates example SPEC.md config.yaml "$BUILD/"
rm -rf "$BUILD/pipeline/runs" "$BUILD/pipeline/src/__pycache__"

if [ "$E01" = 1 ]; then
  cp lab/e01_schema.py "$BUILD/pipeline/src/e01_schema.py"
  python3 lab/apply_e01.py "$BUILD/pipeline/src"
elif [ "$CARDSPLIT" = 1 ]; then
  python3 lab/apply_lab02_cardsplit.py "$BUILD/pipeline/src"
else
  python3 lab/apply_overlay.py "$OVERLAY" "$BUILD/pipeline/src/steps.py"
fi

REV="$(git rev-parse --short HEAD)"
echo "${REV}-lab-${VARIANT}" > "$BUILD/.cluster_sync_rev"

TAR="$(mktemp /tmp/aegis_lab_${VARIANT}_XXXX.tgz)"
tar -czf "$TAR" -C "$BUILD" .
ssh "$HOST" "mkdir -p '$LAB_ROOT/$VARIANT'"
scp -q "$TAR" "$HOST:$LAB_ROOT/$VARIANT.tgz"
ssh "$HOST" "tar -xzf '$LAB_ROOT/$VARIANT.tgz' -C '$LAB_ROOT/$VARIANT' && rm '$LAB_ROOT/$VARIANT.tgz' && echo 'lab payload at $LAB_ROOT/$VARIANT'"
rm -f "$TAR"

SUBMIT="cd $LAB_ROOT/$VARIANT && env MVP_RUN_TAG=lab_$VARIANT MVP_MODEL=$MODEL \
  MVP_RUNS_ROOT=$LAB_RUNS MVP_SEED=42 MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1 \
  bash pipeline/deucalion/submit.sh p1 '$CASE'"
J1=$(ssh "$HOST" "$SUBMIT" 2>/dev/null | awk '/Submitted batch job/{print $4; exit}')
if [ -z "$J1" ]; then echo "p1 submit FAILED for $VARIANT"; exit 1; fi
sleep 3
CHAIN="cd $LAB_ROOT/$VARIANT && env MVP_RUN_TAG=lab_$VARIANT MVP_MODEL=$MODEL \
  MVP_RUN_ID=run_lab_${VARIANT}_${J1} MVP_DEPENDENCY=afterok:${J1} \
  MVP_RUNS_ROOT=$LAB_RUNS MVP_SEED=42 MVP_TEMPERATURE=0.2 MVP_PREAPPROVE_GATES=1 \
  bash pipeline/deucalion/submit.sh all '$CASE'"
J2=$(ssh "$HOST" "$CHAIN" 2>/dev/null | awk '/Submitted batch job/{print $4; exit}')
echo -e "lab_${VARIANT}\t$MODEL\t$CASE\tp1=$J1\tall=${J2:-FAIL}"
