#!/usr/bin/env bash
# gate.sh — record a human gate verdict locally and push it to the cluster run.
# Usage: bash pipeline/deucalion/gate.sh <RUN_ID> <GATE> "<review note>"
#   GATE: G-P1-A | G-P1-B | G-P1-C | G-P1-D
# Writes pipeline/runs/<RUN_ID>/steps/gates/<GATE>.approved (the marker file
# the pipeline requires before the next stage) and scp's it up.
set -euo pipefail

RUN_ID="${1:?usage: gate.sh <RUN_ID> <GATE> \"<note>\"}"
GATE="${2:?gate: G-P1-A|G-P1-B|G-P1-C|G-P1-D}"
NOTE="${3:?a review note is required}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"

GATES_DIR="$REPO_ROOT/pipeline/runs/$RUN_ID/steps/gates"
mkdir -p "$GATES_DIR"
printf 'gate: %s\napproved: %s\nreviewer note: %s\n' \
  "$GATE" "$(date -Is)" "$NOTE" > "$GATES_DIR/$GATE.approved"

ssh "$HOST" "mkdir -p '$PROJ/aegis-mvp/runs/$RUN_ID/steps/gates'"
scp -q "$GATES_DIR/$GATE.approved" "$HOST:$PROJ/aegis-mvp/runs/$RUN_ID/steps/gates/"
echo "gate $GATE approved and pushed for $RUN_ID"
