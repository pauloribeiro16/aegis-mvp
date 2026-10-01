#!/usr/bin/env bash
# sync_up.sh — push the pipeline + the corpus subset it reads to Deucalion.
# Preserves the repo layout under /projects/F202512235CPCAA1/mvp-pipeline/aegis-mvp
# so all relative paths (docs/pipeline/prompts, baseline/, templates/) work
# identically to the workstation. Excludes local run artifacts (they only go up
# via gate pushes).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"

cd "$REPO_ROOT"
TAR="$(mktemp /tmp/aegis_mvp_sync_XXXX.tgz)"
tar --exclude='__pycache__' --exclude='*.pyc' --exclude='pipeline/runs' \
    -czf "$TAR" \
    pipeline docs/pipeline baseline/domains baseline/MAPPINGS \
    templates example SPEC.md config.yaml
echo "payload: $(du -h "$TAR" | cut -f1)"
# Stage through the NFS project dir — Deucalion login nodes do NOT share /tmp
# (scp and ssh can land on different ln nodes; /tmp staging breaks silently).
scp -q "$TAR" "$HOST:$PROJ/aegis-mvp/_sync_incoming.tgz"
ssh "$HOST" "tar -xzf '$PROJ/aegis-mvp/_sync_incoming.tgz' -C '$PROJ/aegis-mvp' && rm '$PROJ/aegis-mvp/_sync_incoming.tgz' && echo 'synced to $PROJ/aegis-mvp'"
rm -f "$TAR"
