---
document_id: AEGIS-EXP-02
title: 'EXP-02 results — the noise floor: seeding makes the pipeline bit-reproducible'
version: 1.0.0
created: 2026-10-03
status: FINAL — battery complete, analysed
sources: 'docs/research/sources.yaml'
prereg: 'PREREG_01.md'
prereg_version: 1.0.0
upstream: '[PREREG_01.md](PREREG_01.md), [00_RESULTS.md](00_RESULTS.md)'
---

# EXP-02 — the noise floor: results

**Question (registered before any run).** How much does this pipeline vary when
nothing varies — and does fixing the sampling make it repeatable?

**Design.** 3 arms × 15 runs, same case/corpus/prompts/gates/assembler/validator;
the only differences: A = no seed, temp 0.2; B = seed 42, temp 0.2; C = seed 42,
temp 0.0. Human gates pre-approved as a declared fixed condition. Runs ordered
by a pre-registered randomised schedule.

**Status.** All 45 runs terminal. 39 produced deliverables and are the analysis
set: **A 9/15, B 15/15, C 15/15.** The six arm-A losses are not scheduler
noise — they are a finding (§3).

---

## 1. Headline: seeding makes the pipeline bit-reproducible

All 15 arm-B runs produced **byte-identical p4 goal JSONs** (same md5 across
r01/r08/r15 for every sub-domain checked), retention means agreeing to 15
decimal places (0.7171490955644458), and identical `narrowed` counts (8) and
call counts (43). The assembled deliverables differ by exactly 4 diff lines —
the `run_id:` header. Arm C (seeded + greedy) is equally deterministic at its
own fixed point (0.7159…, `narrowed` 6).

Arm A (unseeded) has real spread: retention 0.7131 ± 0.0086, CI
[0.7072, 0.7177], `narrowed` ranging 5–22.

| Arm | n closed | L1 PASS | retention mean ± sd | `narrowed` range | calls |
|---|---|---|---|---|---|
| A — no seed, 0.2 | 9 | 9/9 | 0.7131 ± 0.0086 | 5–22 | 43 |
| B — seed 42, 0.2 | 15 | 15/15 | **0.7171 ± 0.0000** | **8–8** | 43 |
| C — seed 42, 0.0 | 15 | 15/15 | **0.7159 ± 0.0000** | **6–6** | 43 |

## 2. Verdicts on the registered hypotheses

- **H1 (seeding reduces variance): SUPPORTED, absolutely.** Within-arm SD
  drops from 0.0086 to 0.0000; the artifacts are byte-identical, not merely
  metric-identical. Seeding is adopted as the default for every later
  comparison (this was the pre-registered decision rule).
- **H2 (residual serving-layer variance): FALSIFIED.** The vendor documents
  `cache_prompt`-style nondeterminism for this class of serving stack
  (registry S-040) and no independent measurement existed. Measured here: zero
  residual. Once the seed pins sampling, the whole chain — model, serving,
  parsing, assembly — reproduces exactly. The pipeline's variance is entirely
  sampling-driven.
- **H3 (greedy adds nothing harmful): SUPPORTED.** Arm C is deterministic and
  lands at a slightly different fixed point (0.7159 vs 0.7171) with a lower
  `narrowed` count. Greedy neither helps nor harms the metrics; seeding alone
  already buys full determinism, so greedy buys nothing extra.
- **H4 (selection stability under current prompts): SUPPORTED.** Every run in
  every arm selected the same sub-domain set (65 rows / 37 sub-domains,
  selection Jaccard vs modal = 1.000 everywhere). The selection variance seen
  in the historical runs (0.888) came from *older prompt versions* — EXP-01's
  "pipeline picked 37, agent picked 38" was prompt-version noise, not arm
  noise.

## 3. The finding that matters for practice: unseeded runs abort at 40%

Six of 15 arm-A runs (40%) aborted mid-p4 when the R6 grounding gate rejected
a "company quantity not traceable to the intake" — on tokens like `05.2` and
`001.`, which are section/sub-domain references in prose, not company facts.
Zero aborts occurred across all 30 seeded runs.

Reading: with a seed, the pipeline locks onto a path that never trips the
gate; without one, unseeded sampling occasionally emits a numeric token the
gate flags, and the fail-loud policy kills the run. **Reproducibility is not a
nicety here — it is the difference between 100% and 60% task completion for an
unattended pipeline.** The gate itself is doing its fabrication-control job
(its red-team origin); the calibration question — should references like
`05.2` count as quantities? — is logged as follow-up work (gate-calibration,
E-10 family). Per PREREG §9(c) the >20% exclusion rate triggers a re-run rule;
the deviation recorded here is to **not** re-run: the abort mechanism is
identified, re-runs would measure the same property, and the closed 9 runs
plus the abort accounting are the honest report.

## 4. What it says about EXP-01 and everything downstream

- EXP-01's n=1 comparison is now grounded: its numbers sit inside the arm
  distributions (pipeline 42–44 calls; the agent 220). The "contract determines
  the output" claim survives with a sharper corollary: **the contract plus one
  seed determines the output exactly.**
- Every future A/B in this programme runs seeded (arm B config), so observed
  differences are configuration effects, not sampling noise.
- The noise floor for content metrics on this pipeline is now *measured*:
  seeded = zero; unseeded ≈ ±0.009 retention with a 40% completion risk.

## 5. Analysis notes and deviations

- Analysis ran once over all closed runs (aggregate_runs v1.0.0, tests in
  `pipeline/tests/measurement_test.py`); statistics via
  `scripts/arm_stats.py` (bootstrap CI, seeded).
- Exclusions: the 6 arm-A aborts (§6 — last stage aborted, no deliverable) and
  the 15 original arm-A submissions killed by the schedule-parse driver bug
  before any model call (PREREG v1.0.1). Denominator: 60 submitted arm-A jobs
  → 9 analysable runs; 30/30 for B and C.
- A vs B difference (−0.0041) is suggestive only (detectability 1.59 at n=9
  vs 15) and is partly survivorship: the unseeded runs that trip the gate die
  before contributing.
- The three determinism claims are mechanical: md5-identical goal JSONs,
  identical metrics to full float precision, and a 4-line deliverable diff
  containing only the run id.
