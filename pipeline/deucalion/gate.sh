#!/usr/bin/env bash
# gate.sh — record a human gate verdict locally and push it to the cluster run.
# Usage: bash pipeline/deucalion/gate.sh <RUN_ID> <GATE> "<review note>"
#   GATE: G-P1-A | G-P1-B | G-P1-C | G-P1-D
# Writes pipeline/runs/<RUN_ID>/steps/gates/<GATE>.approved (the marker file
# the pipeline requires before the next stage) and scp's it up.
set -euo pipefail

RUN_ID="${1:?usage: gate.sh <RUN_ID> <GATE> \"<note>\"}"
GATE="${2:?gate: G-P1-A|G-P1-B|G-P1-C|G-P1-D}"
NOTE="${3:?a review note is required — under AGENTS.md R10b it must state the stress-tests and friction points analyzed; an 'all good' sign-off is INVALID}"
# R10b floor: reject rubber-stamp notes. ponytail: a length floor is a laziness
# floor, not a substance guarantee — boilerplate defeats it; the real check is
# the human reading the note against the artifact.
if [ "${#NOTE}" -lt 200 ]; then
  echo "refused: review note is ${#NOTE} chars; R10b requires the adversarial-council" >&2
  echo "  summary (Contrarian / First Principles / Outsider / Executor lenses) with the" >&2
  echo "  actual friction points found — not a sign-off. Write the substantive note." >&2
  exit 1
fi
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
