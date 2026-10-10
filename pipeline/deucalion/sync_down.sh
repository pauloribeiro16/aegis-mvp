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

# Detetar empresa dinamicamente a partir do manifest caso nao seja passada
if [ -z "$COMPANY" ] && [ -f "$RUNS_DIR/$RUN_ID/manifest.json" ]; then
  COMPANY=$(python3 -c "import json; m=json.load(open('$RUNS_DIR/$RUN_ID/manifest.json')); print(m.get('company_id') or m.get('company') or '')" 2>/dev/null || true)
  if [ -z "$COMPANY" ]; then
    CASE=$(python3 -c "import json; m=json.load(open('$RUNS_DIR/$RUN_ID/manifest.json')); print(m.get('case_id') or m.get('case') or '')" 2>/dev/null || true)
    if [ "$CASE" = "Case_01_TinyTask_SaaS" ]; then COMPANY="TinyTask"; fi
    if [ "$CASE" = "Case_02_SecureBorder_Solutions" ]; then COMPANY="SecureBorder"; fi
    if [ "$CASE" = "Case_03_OmniBank" ]; then COMPANY="OmniBank"; fi
  fi
fi

# O deliverable e o produto, nao a pasta da corrida: o P5 exporta-o para
# output/<empresa>/<fase>/<run_id>/ no compute node, e tem de vir a parte.
if [ -n "$COMPANY" ]; then
  PHASE="phase1"
  if [ -f "$RUNS_DIR/$RUN_ID/Doc01_Operational_Objectives.md" ]; then
    PHASE="phase2"
  elif [ -f "$RUNS_DIR/$RUN_ID/Doc00_Process_and_Operational_Workflows.md" ]; then
    PHASE="phase3"
  fi
  mkdir -p "$REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID"
  if scp -q "$HOST:$PROJ/aegis-mvp/output/$COMPANY/$PHASE/$RUN_ID/"'*' "$REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID/" 2>/dev/null; then
    echo "synced deliverable to $REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID"
  elif scp -q "$HOST:$PROJ/aegis-mvp/output/$COMPANY/$RUN_ID/"'*' "$REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID/" 2>/dev/null; then
    echo "synced deliverable (legacy cluster path) to $REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID"
  elif [ -f "$RUNS_DIR/$RUN_ID/doc02_adjusted_goals.md" ]; then
    cp "$RUNS_DIR/$RUN_ID/doc02_adjusted_goals.md" "$REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID/"
    [ -f "$RUNS_DIR/$RUN_ID/RUN_NOTES.md" ] && cp "$RUNS_DIR/$RUN_ID/RUN_NOTES.md" "$REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID/"
    echo "copied local deliverable to $REPO_ROOT/output/$COMPANY/$PHASE/$RUN_ID"
  fi
else
  echo "note: sem company_id (ou corrida ainda sem export) — output/ nao puxado"
fi
