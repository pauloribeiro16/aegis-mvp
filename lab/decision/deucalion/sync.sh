#!/usr/bin/env bash
# sync.sh — push the lab/decision lane to the Deucalion project dir.
#
# Run from the workstation:
#   bash lab/decision/deucalion/sync.sh
#
# The payload goes through the NFS project dir, never through /tmp: Deucalion
# has several login nodes and /tmp is per-node, so a file staged there can
# land on a different ln node than the ssh that reads it -- the failure is
# silent (tar: cannot open: no such file or directory, scp exited 0).
# One tar, one scp, one extract: two scp calls with the same basename would
# overwrite each other.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
BD="${MVP_BD:-/projects/F202512235CPCAA1/CyberMetric_Deucalion}"
DEST="${MVP_DEST:-$BD/aegis-d1-exp}"

cd "$REPO_ROOT"
REV="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"

TAR="$(mktemp /tmp/d1_lane_XXXX.tgz)"
tar --exclude='__pycache__' --exclude='*.pyc' -czf "$TAR" lab/decision
echo "payload: $(du -h "$TAR" | cut -f1) (rev $REV)"

ssh -o LogLevel=ERROR "$HOST" "mkdir -p '$DEST' '$DEST/logs'"
scp -q "$TAR" "$HOST:$DEST/_sync_incoming.tgz"
# --strip-components=2 drops the leading lab/decision/ so the lane lands flat
# in $DEST (deucalion/*.sbatch, *.py, cases/*.json).
ssh -o LogLevel=ERROR "$HOST" "tar -xzf '$DEST/_sync_incoming.tgz' -C '$DEST' --strip-components=2 && rm -f '$DEST/_sync_incoming.tgz' && echo 'synced to $DEST'"
rm -f "$TAR"
