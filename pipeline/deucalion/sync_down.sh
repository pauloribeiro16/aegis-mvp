#!/usr/bin/env bash
# sync_down.sh — puxar uma corrida do cluster para a workstation.
#
# As corridas NÃO vivem dentro do repositório: o destino local é
# $AEGIS_RUNS_DIR (omissão: ~/Work/aegis-runs), ao lado do repo. No cluster
# também vivem fora do checkout: /projects/.../mvp-pipeline/aegis-runs/.
#
# Usage: bash pipeline/deucalion/sync_down.sh <RUN_ID> [company_id]
set -euo pipefail

RUN_ID="${1:?usage: sync_down.sh <RUN_ID> [company_id] (e.g. run_case01_<JOBID>)}"
COMPANY="${2:-}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
RUNS_DIR="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"

mkdir -p "$RUNS_DIR"
scp -q -r "$HOST:$PROJ/aegis-runs/$RUN_ID" "$RUNS_DIR/"
echo "synced to $RUNS_DIR/$RUN_ID"

# O deliverable é o produto, não a pasta da corrida: o P5 exporta-o para
# output/<empresa>/<run_id>/ no compute node, e tem de vir à parte.
if [ -n "$COMPANY" ] && [ -d "$REPO_ROOT/output/$COMPANY/$RUN_ID" ]; then
  mkdir -p "$REPO_ROOT/output/$COMPANY/$RUN_ID"
  scp -q "$HOST:$PROJ/aegis-mvp/output/$COMPANY/$RUN_ID/"'*' "$REPO_ROOT/output/$COMPANY/$RUN_ID/"
  echo "synced to $REPO_ROOT/output/$COMPANY/$RUN_ID"
else
  echo "note: sem company_id (ou corrida ainda sem export) — output/ não puxado"
fi
