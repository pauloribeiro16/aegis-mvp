---
document_id: AEGIS-EXP-PREREG-01
title: 'Pre-registration EXP-02/03/04 — noise floor, orchestration, and the prompt as a variable'
version: 1.0.0
created: 2026-10-03
status: REGISTERED — before any run
sources: 'docs/research/sources.yaml'
upstream: 'AEGIS-RES-03, AEGIS-RES-04'
---

# Pre-registration — EXP-02, EXP-03, EXP-04

**Registered before any experimental run.** This document fixes the hypotheses,
metrics, analysis plan, exclusions and stopping rule in advance. Nothing here
may be changed after the first run of EXP-02 without a new version and an
explicit note in §11 recording what changed and why. The analysis runs **once**,
over all runs, with the exclusions below and no others.

**The known limitations, stated first because they bound every claim.**

1. **One case** (`Case_01_TinyTask_SaaS`, a fictional 8-person SaaS). Nothing in
   this programme generalises to another company profile. Case binding for
   `Case_02`/`Case_03` is explicitly out of scope (researcher decision, 2026-10-03).
2. **One model** (`qwen3.8:27b` on one A100) and **one corpus, one prompt set**.
3. **One blind rater** for the human rubric (the researcher). No inter-rater
   reliability is claimable; intra-rater test-retest substitutes for it (§7).
4. What *is* transferable despite (1)–(3): the **reproducibility envelope** —
   how much a pipeline of this class varies run-to-run under a fixed
   configuration, and which controls reduce that variance. That is a property
   of the pipeline architecture, not of TinyTask, and it is currently unknown
   in the published literature for the llama.cpp/Ollama stack (registry S-040
   documents the vendor's own nondeterminism admission; no independent
   measurement exists).

---

## 1. Background and motivation

EXP-01 (2026-10-03) compared the fixed-prompt pipeline against a directed agent
on one run per arm and found: identical L1 PASS, identical 65 goal rows, 5.2×
the calls for the agent. Both arms' conclusions rest on **n = 1**: no one has
measured how much the pipeline varies when nothing at all is varied. The
aggregator's first pass over the four historical pipeline runs already shows
why this matters — sub-domain selection differs across runs (Jaccard vs the
modal set: mean 0.888, min 0.579, only 2 of 4 identical), so EXP-01's
"pipeline selected 37, agent selected 38" cannot be read as an arm effect
until the run-to-run distribution of selection is known.

EXP-01's §5 human rubric was designed but never executed. The instrument is now
specified in [L2_RUBRIC.md](L2_RUBRIC.md); EXP-03 is the first experiment
entitled to use it.

## 2. Hypotheses and directional predictions

### EXP-02 — the noise floor (runs first; everything else is read through it)

Design: 3 arms × 15 runs = **45 runs**, same case, same corpus, same prompt
fichas, same parsers/gates/assembler/validator. The only differences:

| Arm | seed | temperature | n |
|---|---|---|---|
| **A** | not sent | 0.2 | 15 |
| **B** | 42 | 0.2 | 15 |
| **C** | 42 | 0.0 | 15 |

**H1 (seeding).** A fixed seed reduces run-to-run variance of the primary
metric. Prediction: SD_B < SD_A.
*Falsified if:* SD_B ≥ SD_A.

**H2 (the residual).** If H1 fails, the variance source is not sampling but
batching/prefix-reuse composition (S-040's documented `cache_prompt`
nondeterminism) or serving-level state. Prediction: SD_B > 0 despite the fixed
seed, with the §5 control of §6 remaining at exactly zero variance.
*Falsified if:* SD_B ≈ 0 (then the residual variance was sampling-driven after
all, and H1's failure was a measurement error).

**H3 (greedy adds nothing harmful).** temperature=0 with a fixed seed does not
increase variance relative to arm B.
*Falsified if:* SD_C > SD_B materially (which would indicate a configuration
bug, not a result — to be investigated before any further interpretation).

**H4 (selection stability).** The selection Jaccard-vs-modal distribution
under arm B/C is materially tighter than the historical 0.888/0.579.
*Falsified if:* the seeded arms' selection variance is indistinguishable from
arm A's.

### EXP-03 — orchestration (only after EXP-02 is analysed)

Design: pipeline arm vs agent arm, 15 runs each, under whichever arm-B/C
configuration EXP-02 justifies (pre-registered choice: **if H1 passes, arm B's
configuration; if H1 fails, arm A's configuration unchanged** — the
conservative choice, made now, so the data cannot be mined for the cheaper
alternative).

**H5 (orchestration effect on substance).** The arms differ on the rubric
composite by less than the within-arm noise: the EXP-01 "same output, different
cost" result replicates at n=15.
*Falsified if:* the arms' rubric composite differs with detectability ≥ 1.96
(§5) in either direction.

**H6 (cost).** The pipeline's calls-per-run and LLM-seconds remain materially
below the agent's (EXP-01: 42 vs 220 calls; 1,304 vs 3,716 s).
*Falsified if:* the ratio collapses toward 1 (which would mean EXP-01's agent
arm was an unrepresentative draw).

**Fixed declared condition (both arms):** the agent may call `finalize` after
seeing L1 findings and repair; the pipeline has no post-assembly loop. This
asymmetry is part of what is measured and is **declared, not neutralised** —
per EXP-01's original framing.

### EXP-04 — the prompt as a variable (after EXP-02)

Design: `PROM-P1-04` v1.5.0 (decision rule) vs its v1.4.0 predecessor
(3-value menu), 15 runs each, under the EXP-02-informed configuration.

**H7.** The v1.5.0 decision rule increases the `narrowed` share of the
Adjustment mix without harming retention. EXP-01 §1b measured 63→48
`unchanged` and 1→17 `narrowed` in a single run per version; the prediction is
directional replication at n=15.
*Falsified if:* the narrowed-mix difference is within noise, or retention
degrades beyond the noise band.

## 3. Design and fixed conditions

**Held constant across every arm and experiment:** the case
(`pipeline/cases/Case_01_TinyTask_SaaS`), the corpus, the model and quantisation
(`qwen3.8:27b` as served by Ollama 0.32.13), the ficha versions (recorded per
run in `manifest.ficha_versions`), the L0 parsers, the content gates, the
zero-LLM assembler, and the L1 validator. The `num_ctx` policy and the dynamic
escalation rule are unchanged; escalations are counted per run (the aggregator
reports them) because pack size is a consequence of the case, identical across
arms.

**Declared fixed condition — gate pre-approval.** Experimental runs execute
unattended with `--preapprove-gates`: the G-P1-A/B/C markers are written by the
runner with a fixed note. This converts the human quality control into a
rubber stamp, identically in every arm. It is declared because G-P1-C is
precisely the gate where EXP-01 showed arm divergence (37 vs 38): under
pre-approval, selection divergence is *measured* as a dependent variable
(H4) instead of being *suppressed* by a human gate. The golden reference run is
never pre-approved; this condition applies to experimental runs only.

**Randomisation.** Run order across arms is determined by submission order of
an arms file generated once with a registered seed; runs are not interleaved
by the experimenter's judgement.

**Repeats.** n = 15 per arm. Justification: the historical selection-Jaccard
dispersion (0.888 mean) suggests per-run outcome variance is non-trivial; 15
gives a bootstrap CI on the mean of a bounded metric roughly ±0.03–0.05 at
observed dispersions, enough to answer "is the within-arm SD smaller than the
between-arm differences EXP-01 reported", which is the smallest question the
programme needs answered. No formal power analysis is claimed — the cost
ceiling (§9), not precision, is the binding constraint.

## 4. Metrics

All metrics are computed by `scripts/aggregate_runs.py` (frozen at v1.0.0,
tests in `pipeline/tests/measurement_test.py`) over the run directories; the
analysis input is `--json` output, and no metric is computed by hand.

**Primary (EXP-02, H1–H3):** mean per-run **obligation retention**
(`artefact.quality.retention.mean`): for each goal row, the Jaccard-style
ratio `|tokens(goal) ∩ tokens(Sub-SO objective)| / |tokens(Sub-SO objective)|`
over content tokens (len ≥ 3, stopword-filtered — the exact function is
`quality.tokens`), averaged over rows with a defined baseline; the per-run mean
is the unit of analysis.

**Secondary (EXP-02):** L1 PASS rate (Wilson CI); selection Jaccard vs modal
set; `narrowed` share of the Adjustment mix; near-verbatim similarity
distribution (the 0.88 gate's firing rate — closes backlog E-10); max
cross-row implication similarity; L0 repair count; stage aborts; calls;
LLM seconds; prompt tokens (real, `attempt1_prompt_tokens`).

**EXP-03 primary:** the L2 rubric composite per document
([L2_RUBRIC.md](L2_RUBRIC.md) §4), blind and paired. **Secondary:** all
EXP-02 secondary metrics + the rubric's document-level items.

**EXP-04 primary:** `narrowed` share. **Secondary:** retention, findings
count.

**Control (all experiments):** the §5 Track B row count is code-derived —
it must be **identical across all runs of a case**. Any variation voids the
run set (isolation broken) and halts the programme for diagnosis. This control
is checked by `aggregate_runs --checks` before any analysis.

## 5. Analysis plan (fixed in advance)

1. Integrity controls first (`--checks`): git rev present on every run,
   config.json present, §5 control at zero variance, no undocumented exclusions.
   A violation halts analysis.
2. Exclusions applied (§6), and the count of excluded runs is reported.
3. **EXP-02:** per-arm distributions. Primary comparison: arm A vs arm B
   retention means — bootstrap CI (10,000 resamples, seed 20261003) on each
   mean, plus `noise_ratio` (`effect_sd` and `detectability`), plus Welch's t
   reported alongside. Verdict thresholds: H1 supported if SD_B < SD_A *and*
   the arms' means' CIs overlap (a variance reduction, not a mean shift, is
   the claim). H2 assessed only if H1 fails.
4. **EXP-03:** primary is the paired rubric composite; paired analysis across
   the 15 case-matched pairs (Wilcoxon-style sign test on pair differences,
   bootstrap CI on the mean difference). Secondary objective metrics compared
   with `noise_ratio`. The arms' EXP-02-informed configuration is the one
   fixed in §2.
5. **EXP-04:** two-proportion comparison on the `narrowed` share (Wilson CIs),
   retention as a guarded secondary.
6. **Multiplicity:** the primary metric of each experiment is tested at
   α = 0.05 uncorrected. Secondary metrics are Holm-corrected within their
   experiment. No metric may migrate from secondary to primary after seeing
   data.
7. **Reporting:** every reported comparison includes n, the effect
   (`effect_sd`), the detectability, and the CI. A "within noise" verdict is
   reported as a finding with the CI that justifies it — never as a missing
   result. The `EXP02/03/04` documents follow the EXP-01 §8 evidence-table
   convention.

## 6. Exclusions (pre-specified, exhaustive)

A run is excluded only if:
- it has **no manifest** (never started), or
- its **last** recorded stage is `aborted` *and* no deliverable exists, or
- it fails a §4 control (§5 variance, missing git rev), or
- the job was killed by the scheduler before completing its stage
  (visible in `stage_history` / slurm logs).

**Nothing else.** Runs are not excludable for ugly numbers, gate findings,
L0 repairs, truncations (those are recorded metrics), or for being outliers.
Every exclusion is listed, with its cause, in the result document. The
denominator (runs submitted vs runs analysed) appears in every results table.

## 7. The human instrument (EXP-03 only)

Governed by [L2_RUBRIC.md](L2_RUBRIC.md): 8 sampled goal rows per document +
7 document-level items, 1–5 with written anchors, blind to arm, presentation
order randomised with a registered seed, ~16 documents per comparison batch.

Because the rater and the experimenter are the same person, three instrument
controls apply: (a) **test-retest** — 4 documents re-scored ≥ 7 days later,
weighted κ (or weighted agreement) reported; (b) **criterion independence** —
the 7 document items' pairwise correlations reported; if the rubric measures
one thing, that is stated; (c) **anchor sufficiency** — scoring uses only the
written anchors; any judgement the anchors do not determine is recorded as
"undetermined", not resolved by preference. Scores are entered into
`L2_SCORES.csv` (format in the rubric doc) *before* any aggregation script
runs, and the arm identities are unblinded only after entry.

## 8. Confounders and their handling

| Confounder | Handling |
|---|---|
| Ollama warm-up (~67 s) inside job wall-clock | metrics use LLM seconds from trace, not job elapsed; job elapsed reported separately per run |
| Queue contention / different nodes | `stage_history` records node + job id per stage; node is reported per arm; if one node dominates one arm, that is stated in the result |
| Partitions fill; runs delayed | irrelevant to metrics (no time-based dependent variable uses wall-clock across days) |
| Model or Ollama binary drift mid-programme | binary pinned in sbatch (0.32.13); model tag pinned; any forced change mid-experiment voids the affected runs (exclusion §6 applies only if recorded — otherwise the experiment restarts) |
| Prompt exemplar self-reference | the pack's worked example is drawn from the produced TinyTask deliverable when present (`compose.golden_text`). For EXP-02/03 this is constant across arms. For EXP-04 the exemplar is frozen to the **example/** golden text in BOTH arms, so the prompt change is isolated from the exemplar drift. (This override is a code change to be made before EXP-04 and registered in its result doc.) |
| Rater drift / memory (EXP-03) | ≥7 days between scoring batches; test-retest subset; scores entered blind |

## 9. Cost ceiling and stopping rule

Budget, in **requested** Slurm wall-clock (the honest unit: 6.5 h per pipeline
run — p4's 3 h dominates — and 4 h per agent run):

| Experiment | Runs | Ceiling |
|---|---|---|
| EXP-02 | 45 × 6.5 h | ~292 GPU-h |
| EXP-03 | 15 × 6.5 + 15 × 4 | ~157 GPU-h |
| EXP-04 | 30 × 6.5 h | ~195 GPU-h |
| **Total** | **105 runs** | **~644 GPU-h** |

**Stopping rules.** (a) EXP-02 stops early if the §4 control (zero §5
variance) fails — the programme halts for diagnosis, and no arm comparison is
read. (b) Any experiment stops when its registered n is reached; **a
non-significant result is not extended** with more repeats (the
multiple-comparisons trap). (c) If > 20% of an arm's runs are excluded under
§6, the arm is re-run in full and the failure itself is reported as a finding.

## 10. What would change the programme's conclusions

| If this happens | Conclusion changes to |
|---|---|
| SD_B ≈ SD_A > 0 (seeding fails) | the stack cannot claim reproducible runs; every previous single-run comparison, including EXP-01's headline numbers, is reclassified as illustrative; serving-layer work (S-043 batch invariance, or llama.cpp `--parallel 1 --no-cache-prompt`) becomes the next experiment |
| §5 control varies | isolation is broken; all runs void; instrumentation bug hunt |
| EXP-03 arms differ beyond noise on the rubric | EXP-01's "the contract, not the orchestration, determines the output" is falsified at n; the agent arm earns a real evaluation track |
| EXP-04's narrowed-shift does not replicate | EXP-01 §1b was a one-run fluke; the decision rule's effect is not established |

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-03 | Initial registration. No runs executed at registration time. |
| 1.0.1 | 2026-10-03 | Operational note, no design change: staged-release protocol adopted after the arm-A submission incident (a bash `read` collapse of empty schedule fields killed all 15 arm-A p1 jobs before any model call; jobs re-submitted). Rule: for every arm, ONE run is validated end-to-end (config, trace, deliverable, aggregation) before the remaining 14 are released. Also fixed: the schedule now writes the literal `none` for no-seed because bash `read` cannot preserve empty middle fields. |
