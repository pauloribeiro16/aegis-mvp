#!/usr/bin/env bash
# run_post_round_cycle.sh — Bloco 1.2 do handoff (2026-10-29): o 1.º ciclo
# pós-ronda da Fase 3 Parte 1 até CONCLUDED, sobre o braço vencedor de Caso 01.
#
# A assinatura da ronda é MECÂNICA e está delegada no handoff do investigador:
# 1.ª proposta de objectivo = Adjust (nota do handoff), 2.ª = Reject (nota do
# handoff), todas as restantes = Accept. Nada de conteúdo inventado.
#
# Usage: bash scripts/run_post_round_cycle.sh <run_id> [--go]
#   sem --go: mostra o que faria (veredictos construídos, sem escrever/submit)
set -euo pipefail

RUN_ID="${1:?usage: run_post_round_cycle.sh <run_id> [--go]}"
GO="${2:-}"
HOST="${MVP_HOST:-paulinho@login.deucalion.macc.fccn.pt}"
PROJ="${MVP_PROJ:-/projects/F202512235CPCAA1/mvp-pipeline}"
LOCAL_RUNS="${AEGIS_RUNS_DIR:-$HOME/Work/aegis-runs}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODEL="${MVP_MODEL:-}"   # overridden by the run config below (the run knows its model)
CASE="${MVP_CASE:-Case_01_TinyTask_SaaS}"

ADJUST_NOTE="Tighten the fit criterion so the refusal response and audit record fields are observable at the workspace API boundary without referencing internal implementation."
REJECT_NOTE="Discharged proportionally by the existing workspace boundary check and organizational review duty for an 8-person single-product SaaS team."
ACCEPT_NOTE="Proportional and black-box verifiable constraint aligned with V0 functional carriers."
GATE_NOTE="Operator-approved mechanical exercise of the G-P3-A round cycle delegated in the handoff of 2026-10-29: one Adjust to exercise p3a_repropose, one explicit Reject (= recorded risk acceptance) and Accept on all remaining items. No substantive re-judgement of proposal content is claimed here."

say() { echo "[cycle] $*"; }
die() { echo "[cycle] FATAL: $*" >&2; exit 1; }

# 0. pull the run
say "sync_down $RUN_ID"
bash "$REPO_ROOT/pipeline/deucalion/sync_down.sh" "$RUN_ID"
RUN="$LOCAL_RUNS/$RUN_ID"

# 0b. the run's own config is the authority on which model and case this is
MODEL=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('model') or '')" "$RUN/config.json" 2>/dev/null || true)
CASE=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('case_id') or 'Case_01_TinyTask_SaaS')" "$RUN/manifest.json" 2>/dev/null || echo "$CASE")
[ -n "$MODEL" ] || die "the run config has no model — refusing to guess"
say "run model=$MODEL case=$CASE"

# 1. build round1 verdicts in the REAL schema (proposals.py: apply_round_verdicts)
python3 - "$RUN" "$GO" "$ADJUST_NOTE" "$REJECT_NOTE" "$ACCEPT_NOTE" "$GATE_NOTE" <<'PYEOF'
import json, sys
from pathlib import Path

run, go = Path(sys.argv[1]), sys.argv[2] == "--go"
adjust_note, reject_note, accept_note, gate_note = sys.argv[3:7]

props = []
for pattern in ("proposals_*.json",):  # proposals_prin_* is already matched here
    for p in sorted((run / "steps" / "phase3").glob(pattern)):
        props.extend(json.loads(p.read_text(encoding="utf-8"))["proposals"])
if not props:
    raise SystemExit("no round-1 proposals on disk")

# objective-driven first (the handoff slots Adjust/Reject on the first two),
# principle-derived after — keys are the round_key the verdicts file uses
objective_driven = [p for p in props if not p.get("principle")]
principle_driven = [p for p in props if p.get("principle")]
ordered = objective_driven + principle_driven

verdicts, notes = {}, {}
for i, p in enumerate(ordered):
    key = p.get("principle") or p["objective"]
    if i == 0:
        verdicts[key] = "Adjust"; notes[key] = adjust_note
    elif i == 1:
        verdicts[key] = "Reject"; notes[key] = reject_note
    else:
        verdicts[key] = "Accept"
        if not p.get("principle"):
            notes[key] = accept_note

print(f"proposals: {len(ordered)} ({len(objective_driven)} objective-driven, "
      f"{len(principle_driven)} principle) -> {sum(v=='Adjust' for v in verdicts.values())} Adjust, "
      f"{sum(v=='Reject' for v in verdicts.values())} Reject, "
      f"{sum(v=='Accept' for v in verdicts.values())} Accept")
print("Adjust item:", next(k for k, v in verdicts.items() if v == "Adjust"))
print("Reject item:", next(k for k, v in verdicts.items() if v == "Reject"))
if not go:
    print("(dry: nothing written)"); raise SystemExit(0)

vf = run / "steps" / "phase3" / "round1_verdicts.json"
vf.write_text(json.dumps({"verdicts": verdicts, "notes": notes},
                         indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
gates = run / "steps" / "gates"
gates.mkdir(parents=True, exist_ok=True)
(gates / "G-P3-A.approved").write_text(gate_note + "\n", encoding="utf-8")
print(f"wrote {vf} and steps/gates/G-P3-A.approved ({len(gate_note)} chars)")
PYEOF
[ "$GO" = "--go" ] || { say "dry run complete — re-run with --go"; exit 0; }

# 2. apply round 1 locally (deterministic, 0 model calls)
say "p3a_round (local, round 1)"
PYTHONPATH="$REPO_ROOT/pipeline/src" python3 "$REPO_ROOT/pipeline/src/run_pipeline.py" run \
  --stage p3a_round --repo "$REPO_ROOT" --run-dir "$RUN" --base http://127.0.0.1:11434
state1=$(python3 -c "import json,sys; s=json.load(open(sys.argv[1])); print(s['pending_adjustment'] and 'PENDING_ADJUSTMENT' or ('CONVERGED' if s.get('converged') else 'OPEN'))" "$RUN/steps/phase3/round1_state.json")
[ "$state1" = "PENDING_ADJUSTMENT" ] || die "round1 state expected pending_adjustment=1, got $state1"

# 3. push round-1 state up, repropose on the cluster
say "scp round1 state + gates -> cluster"
ssh -o LogLevel=ERROR "$HOST" "mkdir -p '$PROJ/aegis-runs/$RUN_ID/steps/gates'"
scp -q "$RUN/steps/phase3/round1_verdicts.json" "$RUN/steps/phase3/round1_state.json" \
  "$HOST:$PROJ/aegis-runs/$RUN_ID/steps/phase3/"
scp -q "$RUN/steps/gates/G-P3-A.approved" "$HOST:$PROJ/aegis-runs/$RUN_ID/steps/gates/"

say "submit p3a_repropose"
SUBMIT_OUT=$(ssh -o LogLevel=ERROR "$HOST" "cd '$PROJ/aegis-mvp' && env MVP_RUN_ID='$RUN_ID' \
  MVP_RUN_TAG='${RUN_ID#run_}_repropose' MVP_MODEL='$MODEL' MVP_CASE='$CASE' \
  bash pipeline/deucalion/submit.sh p3a_repropose" 2>&1) || true
echo "$SUBMIT_OUT" | sed 's/^/[cycle]   /'
JOB=$(echo "$SUBMIT_OUT" | grep -oE 'Submitted batch job [0-9]+' | grep -oE '[0-9]+' | head -1 || true)
[ -n "$JOB" ] || die "could not read the repropose job id (submit output above)"
say "repropose job $JOB — waiting"
while true; do
  ST=$(ssh -o LogLevel=ERROR "$HOST" "sacct -n -X -j $JOB -o State" 2>/dev/null | head -1 | xargs || true)
  case "$ST" in COMPLETED) break;; FAILED|CANCELLED|TIMEOUT) die "repropose job $JOB: $ST";; esac
  sleep 60
done

# 4. pull the repropose result BEFORE signing round 2 — the round-2 proposals
#    blob is written by the CLUSTER stage, so the local copy needs a sync_down
say "sync_down (the repropose wrote the round-2 proposals blob)"
bash "$REPO_ROOT/pipeline/deucalion/sync_down.sh" "$RUN_ID"

# 5. sign round 2: Accept the revised item (round-2 proposals blob has it)
python3 - "$RUN" <<'PYEOF'
import json, sys
from pathlib import Path
run = Path(sys.argv[1])
blob = json.loads((run / "steps" / "phase3" / "round2_proposals.json").read_text(encoding="utf-8"))
keys = [(p.get("principle") or p["objective"]) for p in blob["proposals"]]
assert len(keys) >= 1, "round 2 has no revised items"
(run / "steps" / "phase3" / "round2_verdicts.json").write_text(
    json.dumps({"verdicts": {k: "Accept" for k in keys},
                "notes": {k: "Round 2: the tightened fit criterion is accepted." for k in keys}},
               indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"round2 verdicts written for {len(keys)} item(s): {keys}")
PYEOF

say "p3a_round (local, round 2 — must converge)"
PYTHONPATH="$REPO_ROOT/pipeline/src" python3 "$REPO_ROOT/pipeline/src/run_pipeline.py" run \
  --stage p3a_round --repo "$REPO_ROOT" --run-dir "$RUN" --base http://127.0.0.1:11434
conv=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('converged'))" "$RUN/steps/phase3/round2_state.json")
[ "$conv" = "True" ] || die "round 2 did not converge"

# 5. push round-2 state up, run the tail of p3a_all (org -> weave -> gate)
say "scp round2 state -> cluster; submit p3a_all (resumes at org)"
scp -q "$RUN/steps/phase3/round2_verdicts.json" "$RUN/steps/phase3/round2_state.json" \
  "$HOST:$PROJ/aegis-runs/$RUN_ID/steps/phase3/"
SUBMIT_OUT=$(ssh -o LogLevel=ERROR "$HOST" "cd '$PROJ/aegis-mvp' && env MVP_RUN_ID='$RUN_ID' \
  MVP_RUN_TAG='${RUN_ID#run_}_finish' MVP_MODEL='$MODEL' MVP_CASE='$CASE' \
  bash pipeline/deucalion/submit.sh p3a_all" 2>&1) || true
echo "$SUBMIT_OUT" | sed 's/^/[cycle]   /'
JOB=$(echo "$SUBMIT_OUT" | grep -oE 'Submitted batch job [0-9]+' | grep -oE '[0-9]+' | head -1 || true)
[ -n "$JOB" ] || die "could not read the p3a_all job id (submit output above)"
say "p3a_all job $JOB — waiting (org/weave are model calls)"
while true; do
  ST=$(ssh -o LogLevel=ERROR "$HOST" "sacct -n -X -j $JOB -o State" 2>/dev/null | head -1 | xargs || true)
  case "$ST" in COMPLETED) break;; FAILED|CANCELLED|TIMEOUT) die "p3a_all job $JOB: $ST";; esac
  sleep 300
done

# 6. pull the conclusion and verify
say "sync_down final + gate verification"
bash "$REPO_ROOT/pipeline/deucalion/sync_down.sh" "$RUN_ID"
grep -E "^state:" "$RUN/steps/phase3/gate_report.md" || die "no gate report state line"
grep -cE "\| G[1-6] \| CLOSED" "$RUN/steps/phase3/gate_report.md" | xargs -I{} test "{}" -eq 6 \
  || die "not all six Part-1 gates CLOSED — read the report"
say "DONE: $RUN_ID Parte 1 CONCLUDED (G1..G6 CLOSED)"
