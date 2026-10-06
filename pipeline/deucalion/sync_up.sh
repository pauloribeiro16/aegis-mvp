#!/usr/bin/env bash
# sync_up.sh — push the pipeline + the corpus subset it reads to Deucalion.
# Preserves the repo layout under /projects/F202512235CPCAA1/mvp-pipeline/aegis-mvp
# so all relative paths (docs/pipeline/prompts, baseline/, templates/) work
# identically to the workstation. Excludes local run artifacts (they only go up
# via gate pushes).
#
# baseline/CONTROLS is REQUIRED: controls.py derives every Regulation/Control
# Anchor in §3 and every §6 control row from baseline/CONTROLS/<FW>/<ID>.json
# (R2b by construction). Without it P5 aborts with
# "control PR.DS-01 not found under CONTROLS/NIST_CSF_2.0/ (R2b)" — which is
# what job 1964272 did, because the anchor derivation is code-side and the
# referential was never part of this payload.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"

cd "$REPO_ROOT"
# Stamp the workstation's code revision INTO the payload: the cluster checkout
# has no .git, so without this stamp every run would record an empty
# aegis_git_rev (what happened to both EXP-01 arms). new-run reads the stamp
# when git is unavailable.
REV="$(git rev-parse --short HEAD)"
echo "$REV" > .cluster_sync_rev
TAR="$(mktemp /tmp/aegis_mvp_sync_XXXX.tgz)"
tar --exclude='__pycache__' --exclude='*.pyc' --exclude='pipeline/runs' \
    -czf "$TAR" \
    pipeline docs/pipeline baseline/domains baseline/MAPPINGS baseline/CONTROLS \
    templates example SPEC.md config.yaml .cluster_sync_rev cases
echo "payload: $(du -h "$TAR" | cut -f1) (rev $REV)"
# Stage through the NFS project dir — Deucalion login nodes do NOT share /tmp
# (scp and ssh can land on different ln nodes; /tmp staging breaks silently).
scp -q "$TAR" "$HOST:$PROJ/aegis-mvp/_sync_incoming.tgz"
ssh "$HOST" "tar -xzf '$PROJ/aegis-mvp/_sync_incoming.tgz' -C '$PROJ/aegis-mvp' && rm '$PROJ/aegis-mvp/_sync_incoming.tgz' && echo 'synced to $PROJ/aegis-mvp'"
rm -f "$TAR"
