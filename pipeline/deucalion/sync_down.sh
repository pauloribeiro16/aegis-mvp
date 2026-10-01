#!/usr/bin/env bash
# sync_down.sh — pull one run directory back to the workstation.
# Usage: bash pipeline/deucalion/sync_down.sh <RUN_ID>
set -euo pipefail

RUN_ID="${1:?usage: sync_down.sh <RUN_ID> (e.g. run_case01_<JOBID>)}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"

mkdir -p "$REPO_ROOT/pipeline/runs"
scp -q -r "$HOST:$PROJ/aegis-mvp/runs/$RUN_ID" "$REPO_ROOT/pipeline/runs/"
echo "synced to $REPO_ROOT/pipeline/runs/$RUN_ID"
