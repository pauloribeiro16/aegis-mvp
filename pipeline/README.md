# Phase 1 Pipeline — Deucalion execution layer

Executes the Phase 1 pipeline (SPEC §5 P1–P5) as staged SLURM jobs on the
Deucalion supercomputer, using the generic prompt fichas under
[`docs/pipeline/prompts/`](../docs/pipeline/prompts/) as the single source of
prompt text (ADR-010 D2) — the fichas are case-agnostic; a case only enters
through its binding in [`cases/`](cases/).

Implements ADR-010 D4 (orchestration runtime). Workflow, not agent (ADR-010 D1):
fixed P1→P5 chain, deterministic context packs, a human gate between stages.

## Layout

| Path | Role |
|---|---|
| `src/compose.py` | ficha parser + deterministic context packs (pure function of case + verdicts + selection) |
| `src/llm.py` | stdlib Ollama HTTP client (compute node, no pip egress) |
| `src/steps.py` | per-step execution: compose → call → L0 validate (1 repair retry) → store |
| `src/trace.py` | `trace.jsonl` call ledger + `manifest.json` |
| `src/validate.py` | local L1 validator (SPEC §8 items 2–6, 9 + R12 hygiene + trace consistency) |
| `src/run_pipeline.py` | stage driver (`new-run`, `run --stage`) |
| `deucalion/` | `phase1.sbatch` (hardened), `submit.sh`, `sync_up.sh`, `sync_down.sh`, `gate.sh` |
| `cases/<Case>/` | case binding: `case.yaml` + `company_input.md` (SPEC §4 contract) |
| `runs/<RUN_ID>/` | run artifacts (see below) |

## Run folder — what was sent vs what the model produced

```
runs/run_<tag>_<JOBID>/
├── manifest.json        # case, model, job id, node, ficha versions, call counts
├── trace.jsonl          # ONE line per LLM call: seq, step, ficha, num_ctx,
│                        #   timestamps, latency, tokens, status, file paths
├── inputs/              # WHAT WAS SENT — exact system+user per call (001_P1_*, …)
├── outputs/             # WHAT THE MODEL PRODUCED — raw JSON + text per call
├── packs/               # (reserved) context packs are also embedded in inputs/
├── steps/               # validated step artifacts (fact sheet, verdicts,
│                        #   selection, goals/<D-XX.Y>.md, gates/)
├── phase1_output.md     # the deliverable (DRAFT until G-P1-D)
├── RUN_NOTES.md         # §8 evidence table
└── logs/                # run log, slurm out, ollama serve log
```

## Runbook — 4 cycles, one human gate each

Stage → gate mapping: `p1`→**G-P1-A**, `p2`→**G-P1-B**, `p3`→**G-P1-C**,
`p4+p5`→**G-P1-D**. The pipeline refuses to run a stage whose gate file
(`steps/gates/<GATE>.approved`) is missing — state on disk is the only
carrier (ADR-010 D5).

```bash
# 0. one-time per workstation session
bash pipeline/deucalion/sync_up.sh                       # repo subset -> cluster

# 1. stage p1 (job 1)
ssh paulinho@login.deucalion.macc.fccn.pt
cd /projects/F202512235CPCAA1/mvp-pipeline/aegis-mvp
MVP_RUN_TAG=case01 bash pipeline/deucalion/submit.sh p1  # -> JOBID
squeue -u $USER                                          # monitor
exit
RUN_ID=run_case01_<JOBID>
bash pipeline/deucalion/sync_down.sh $RUN_ID
python3 pipeline/src/validate.py --run-dir pipeline/runs/$RUN_ID || true

# 2. human gate review (local): read steps/fact_sheet.yaml, then record + push
bash pipeline/deucalion/gate.sh $RUN_ID G-P1-A "fact sheet faithful; no corrections"

# 3. stage p2 (job 2) ... repeat: submit -> sync_down -> review -> gate
MVP_RUN_TAG=case01 bash pipeline/deucalion/submit.sh p2   # on cluster, same RUN_TAG
bash pipeline/deucalion/gate.sh $RUN_ID G-P1-B "verdicts confirmed"
MVP_RUN_TAG=case01 bash pipeline/deucalion/submit.sh p3
bash pipeline/deucalion/gate.sh $RUN_ID G-P1-C "subset + exclusions accepted"
MVP_RUN_TAG=case01 bash pipeline/deucalion/submit.sh p4p5
bash pipeline/deucalion/gate.sh $RUN_ID G-P1-D "sign-off"
```

All jobs of one run use the **same `MVP_RUN_TAG`**. The run directory name
embeds the *first* job id, so stage jobs after the first must target the
existing run directory by exporting the full run id:

```bash
MVP_RUN_TAG=case01 MVP_RUN_ID=run_case01_123456 bash pipeline/deucalion/submit.sh p2
```

`submit.sh` forwards `MVP_RUN_ID`; `phase1.sbatch` uses it verbatim when set,
and only derives `run_<tag>_<JOBID>` for a fresh run (stage p1, no
`MVP_RUN_ID`).

## Validation layers

| Layer | When | What |
|---|---|---|
| L0 (cluster, in-call) | after each LLM call | output contract: fenced format, table shape, enums, ID sequences; 1 repair retry, then stage aborts with forensics |
| L1 (local, `validate.py`) | after each sync_down | SPEC §8 items 2–6, 9 (article/anchor resolution against `baseline/`), R12 hygiene over the run folder, trace consistency |
| L4 (human gates) | between stages | G-P1-A..D verdicts recorded via `gate.sh` |

`phase1_output.md` stays `DRAFT`; promotion to `ACTIVE` is the G-P1-D
sign-off decision (human edit after review).
