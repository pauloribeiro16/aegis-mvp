---
document_id: AEGIS-EXP-03
title: 'EXP-03 results — pipeline vs agent at n=15: same structure, different document, half the termination rate'
version: 1.0.0
created: 2026-10-04
status: OBJECTIVE PART COMPLETE — primary metric (blind rubric) pending researcher scoring
sources: 'docs/research/sources.yaml'
upstream: '[PREREG_01.md](PREREG_01.md), [EXP02_results.md](EXP02_results.md)'
---

# EXP-03 — pipeline vs agent, at n=15

**Question (registered before any run).** Can a tool-calling *agent* do the same
job as the fixed pipeline, and does the agent's 5× cost buy quality?

**Design.** 15 runs per arm, both seeded (42) per the EXP-02 decision rule, same
case, corpus, prompts, gates, assembler, validator. The pipeline arm is EXP-02's
arm B — the same configuration, already measured, reused rather than re-run
(identical configuration, so the reuse is a save, not a shortcut). The agent arm
is 15 fresh `agentic` runs. Declared asymmetry kept: the agent may see L1
findings and repair before finishing; the pipeline has no post-assembly loop.

**Headline: at n=15 the two arms do not produce the same document, and the
agent fails to terminate cleanly in over half its runs.**

## 1. The two arms

| | **PIPELINE** (n=15) | **AGENT** (n=15) |
|---|---|---|
| clean completion (L1 PASS) | **15/15** | **7/15** |
| retention mean ± sd | 0.7171 ± **0.0000** | 0.7851 ± 0.0182 |
| goal rows | 65 in every run | 65 in every run |
| LLM calls | **43** | **208** (4.8×) |
| context tokens | **0.75 M** | **4.79 M** (6.4×) |
| LLM seconds | **1,299** | **3,421** (2.6×) |
| `narrowed` (of 65) | 8 in every run | **0–2** |

## 2. What the 8 agent "failures" actually are

Not bad documents and not missing documents — **complete documents that never
terminated**. All eight runs (r08–r15) produced a full 236 KB deliverable with
65 goal rows and 37 sub-domains, then hit the agent's own watchdog:
`no artifact progress in 12 turns (degenerate loop?)`. The runs are byte-for-byte
identical to each other, because they are seeded.

So the honest statement is two numbers, not one:

- **7/15 agent runs completed cleanly** (L1 PASS).
- **15/15 produced a complete 65-row document**; in 8 of them the agent kept
  working after the work was done and had to be stopped by the watchdog.

An unattended agent pipeline therefore has a **53% clean-termination rate**; the
fixed pipeline has **100%**, and never needed a resume.

## 3. The behavioural difference (this is the finding)

The two arms are not "the same output at different prices". They produce
**systematically different documents**:

- The agent **retains more** of the regulatory baseline obligation: 0.785–0.801
  versus the pipeline's 0.717. Against a pipeline whose within-arm sd is exactly
  zero, that difference is far outside noise.
- The agent **barely calibrates**: `narrowed` on 0–2 rows, versus the pipeline's
  8 — and, uniquely, the pipeline's 8 is *identical in all 15 runs* (it is a
  deterministic output, not a sample).

Read together these are one coherent failure mode: **the agent restates the
obligation faithfully and does not restate it in the company's terms.** It keeps
the duty and drops the calibration. That is precisely the failure the near-
verbatim gate and the R3 proportionality rule exist to catch, and it is the
mirror image of gemma4 in the model matrix (which calibrated hard, 40–43
`narrowed`, and retained least, 0.653).

Which one is *better* is not answerable from these numbers. Retention measures
how much of the baseline survives, not whether the surviving text is calibrated
or merely copied. **That is the pre-registered primary metric** — the blind
human rubric — and it has not been run yet.

## 4. Verdicts on the registered hypotheses

- **H5 (orchestration does not change the substance): FALSIFIED as stated.** The
  arms differ in retention and calibration by far more than the noise floor. The
  weaker claim EXP-01 made at n=1 — *the contract determines the structure* —
  survives: both arms produce 65 rows, 37 sub-domains, and the same document
  skeleton. But the *content* of the rows is not the same, and EXP-01 could not
  see it.
- **H6 (the pipeline remains materially cheaper): SUPPORTED, amplified.** 4.8×
  the calls, 6.4× the context tokens, 2.6× the wall time — and 2.1× the failure
  rate to terminate.
- **New finding (not registered):** the agent's cost is not only higher, it is
  *less predictable* — 8 of 15 runs entering a degenerate loop after completing
  the work is a reliability property the n=1 comparison could not exhibit.

## 5. What is still missing

The pre-registered **primary metric for EXP-03 is the blind human rubric**
(`L2_RUBRIC.md`): the researcher scores 8 sampled goal rows + 7 document-level
items per document, blind to arm, order randomised with a registered seed. Until
that is done, §3's "which is better" is open, and this document reports only the
objective half.

The scoring pack for the 30 documents (15 pipeline + 15 agent) is prepared
separately; the retention/calibration divergence above is the finding the
scoring will adjudicate.

## 6. Honest notes

- The pipeline arm reuses EXP-02's arm B. Same configuration, same case, same
  seed — the runs are the comparison, not a shortcut. Its determinism (sd = 0)
  means its 15 runs are one outcome observed 15 times, not 15 samples: treat
  the pipeline column as a point estimate, not a distribution.
- The 8 non-terminating runs are counted in the L1 column as failures (the strict
  reading) and re-counted in §2 (the generous reading). Both are reported
  because the choice changes the headline from "47% worse" to "identical
  documents, half the reliability".
- The agent arm's `narrowed` spread (0–2) is wider than the pipeline's exact 8,
  but with a mean that low the distribution is dominated by the runs that
  calibrated not at all.
