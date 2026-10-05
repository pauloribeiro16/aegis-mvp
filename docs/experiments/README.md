---
document_id: AEGIS-EXP-IDX
title: 'Experiments — folder index'
version: 1.0.0
created: 2026-10-03
status: ACTIVE
---

# Experiments (`docs/experiments/`)

The experimental layer: what is measured, under what fixed conditions, and
what was found. The design rationale lives in
[`docs/research/`](../research/README.md) (AEGIS-RES-03/04); this folder is
where the programme is registered, instrumented, and reported.

## Index

| Doc | Purpose | Status |
|---|---|---|
| [00_RESULTS.md](00_RESULTS.md) | **The living results panel** — one block per experiment: what it tested / how designed / results so far / what they say. Start here | LIVE |
| [PREREG_01.md](PREREG_01.md) | Formal pre-registration: hypotheses H1–H7, fixed conditions, metrics, analysis plan, exclusions, stopping rules — registered **before any run** | REGISTERED |
| [PREREG_02.md](PREREG_02.md) | Formal pre-registration for the robustness lane (EXP-05a–d): gate mutation taxonomy, pack measurement, matcher-pinned equivalence, metamorphic relations — registered **before any run** | REGISTERED |
| [EXP05_robustness_results.md](EXP05_robustness_results.md) | 05a gates 36/36 · 05b coverage 100%/utilisation 86.4% · 05c falsifier fired (E-08 blocked) · 05d M2 held / M1 falsified at the letter, decisions invariant | COMPLETE |
| [L2_RUBRIC.md](L2_RUBRIC.md) | The human scoring instrument: 1–5 anchors, two stages, blinding protocol, capture format, instrument controls | ACTIVE |
| [EXP01_pipeline_vs_agent.md](EXP01_pipeline_vs_agent.md) | The original n=1 comparison (2026-10-03): both arms L1 PASS, 65 rows, agent 5.2× the calls. Its §5 rubric is superseded by L2_RUBRIC.md | DRAFT (n=1) |
| EXP02_noise_floor.md | The run-to-run variance measurement (3 arms × 15 runs) | running — results doc when analysed |
| EXP03_orchestration.md | Pipeline vs agent at n=15 per arm, rubric-scored blind | not run |
| [EXP04_results.md](EXP04_results.md) | PROM-P1-04 decision rule vs menu, n=5 per arm, seeded — menu 5/5 vs rule 0/5 under the current instrument; the rule arm regressed vs EXP-02-B 15/15 | COMPLETE (decision pending on the shipped arm) |

**Results convention.** When an experiment's battery finishes and is analysed,
its results document lands in this folder (same four-section shape as the
panel) and `00_RESULTS.md` is updated in the same session. The inspector's
*Pesquisa* page serves this folder directly, so results appear on the site the
moment the file exists — no deploy, no commit required.

## The programme in one paragraph

Nobody has measured how much this pipeline varies when nothing varies. EXP-02
measures that noise floor first (45 runs, seeded vs unseeded vs greedy), because
every other comparison is read through it. EXP-03 then re-runs the EXP-01
orchestration question at n=15 per arm with a blind human rubric, and EXP-04
turns EXP-01's single-run prompt observation into a measured effect. One case,
one model, one blind rater — the pre-registration states these limits up front
and defines what survives them: the reproducibility envelope, which is a
property of the pipeline class and is unknown in the literature for this serving
stack.

## Instrumentation (code, already landed)

| Piece | Where | Test |
|---|---|---|
| Per-run `config.json` (temperature/seed/arm/repeat), echoed into the manifest | `pipeline/src/runconfig.py` | `measurement_test.py` |
| Sampler keys in the Ollama payload; unset ≠ default | `pipeline/src/llm.py` | `measurement_test.py` |
| Trace records what was SENT (temperature, per-key sampler values), real `prompt_eval_count` | `pipeline/src/steps.py`, `agent/loop.py` | `measurement_test.py` |
| `git rev` fails loud (the two EXP-01 runs recorded an empty rev) | `pipeline/src/run_pipeline.py` | manual: `new-run` outside a git tree |
| `all` stage combo + `--preapprove-gates` (declared fixed condition, PREREG §3) | `pipeline/src/run_pipeline.py`, `submit.sh`, `phase1.sbatch` | PREREG controls |
| `quality.score_run()` — per-row retention / near-verbatim / reuse numbers | `pipeline/src/quality.py` | `measurement_test.py` |
| Cross-run aggregator (both trace schemas, the dry-run `latency_s` trap, selection divergence) | `scripts/aggregate_runs.py` | `measurement_test.py` |
| Bootstrap CI / Cliff's δ / Wilson / Holm / noise-vs-detectability | `scripts/arm_stats.py` | `--demo` + `measurement_test.py` |

Usage after a batch of runs:

```bash
python3 scripts/aggregate_runs.py ~/Work/aegis-runs/run_exp02_* --arm-summary --checks --json exp02.json
python3 scripts/arm_stats.py --compare retention arm_a.json arm_b.json   # (schema: see --help)
```

## Conventions

- **No result document exists before its runs do.** EXP02/03/04 files are
  created when their data is analysed, following EXP-01's structure (question,
  controlled comparison, declared asymmetries, results, evidence table).
- **The pre-registration outruns the experimenter.** Post-hoc deviations are
  recorded in PREREG §11 with what changed and why — an analysis that quietly
  ignores its own registration is worth less than no analysis.
- **Gate pre-approval is a declared experimental condition**, never a
  convenience: ordinary (non-experiment) runs keep the human gates.
