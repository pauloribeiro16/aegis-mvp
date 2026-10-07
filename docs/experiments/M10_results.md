---
document_id: AEGIS-M10
title: 'M10 results — the goals carry the company; the column built to carry it does not'
version: 1.0.0
created: 2026-10-08
status: COMPLETE — instrument valid for the goal column, empty for the implication column
prereg: 'PREREG_M10_INSTRUMENT.md'
prereg_version: 1.0.0
upstream: '[PREREG_M10_INSTRUMENT.md](PREREG_M10_INSTRUMENT.md), [M09_results.md](M09_results.md), [00_RESULTS.md](00_RESULTS.md)'
---

# M10 — Is the instrument measuring anything?

**Results for [PREREG_M10](PREREG_M10_INSTRUMENT.md), frozen 2026-10-08 before any
measurement code ran.** Re-scoring only: no model called, no cluster time, one
afternoon. Population: every goal row of the delivered M07 matrix, read from
artefacts.

---

## Headline

**The `Adjusted goal` column carries the company. The `Company implication` —
the one column that exists to carry it — is statistically indistinguishable from
unrelated text.**

Measured inside the M07 matrix so the instrument is constant, against a
cross-sectional placebo (same model, same company, a genuinely different duty):

| column | cross-company | placebo | difference | n |
|---|---|---|---|---|
| **Adjusted goal** | 0.249 | 0.061 | **+0.188** | 821 / 51838 |
| **Company implication** | 0.062 | 0.061 | **+0.002** | 821 / 51838 |

For context, the median similarity of the same model writing the same sub-domain
and case **twice** is 0.295. The ordering is exactly what a working column looks
like — same duty same company (0.295) > same duty other company (0.249) ≫
different duty (0.061) — for the goal column, and flat at the placebo for the
implication column.

## Verdicts as preregistered

| # | Prediction | Outcome |
|---|---|---|
| **P1** | `adjustment_kind` emits the constructed class on every Leg-A vector | **HOLDS — 15/15**, including the adversarial rows (empty, `—`, out-of-vocabulary prose) |
| **P2** | modal-string share > 80% in every run | **FALSIFIED by 7 runs.** Six are the nemotron cells at 5–12% and one muse-C1 at 72%; the qwen3.8 and gemma4 reference cells sit at 96–100% |
| **P3** | `cross_company` not materially below the replicate floor | not decidable inside M07 (no cell ran the same model+case twice); the floor from M08 is 0.295 |
| **P4** | `cross_company` not materially above the placebo | **HOLDS for the implication column (+0.002), FALSIFIED for the goal column (+0.188)** |

P2's falsification is not a defect of the badge — it is the over-compressed runs
that died early emitting a wide spread of strings before failing. The reference
cells, which are the ones that carry the collapse claim, sit at 96–100%.

## A recorded deviation

**The first pass of this script reported theatre confirmed on both columns.
That was wrong, twice, and the corrected numbers reverse the verdict on the goal
column.** The first pass:

1. **Pooled M07 and M08.** Their `replicate` floor therefore compared two
   *different instruments* (M08 is the researcher's soft-gate iteration under a
   new golden) and measured cross-revision drift, not run-to-run noise. The
   floor it produced, 0.032, was meaningless, and it dragged `cross_company`
   down with it.
2. **Used a near-neighbour placebo.** It compared one regulation of a
   sub-domain against another. That is not "a different duty", and it made
   cross-company similarity look flat.

The shipped script computes inside a single matrix and builds the placebo
*across* cells — same model, same company, different `(sub-domain, regulation)`.
Both errors were mine and both were found by reading the first output closely
enough to notice that a floor of 0.03 across 684 supposedly-replicated cells was
implausible. The prereg is unchanged; §6.2's declared confound (the three cases
carry different regulation sets) is why the cross-company cells are keyed by
regulation as well as company.

## What this retires

**The 0.99 badge panic, without a parser story.** M07 read `unchanged` at a
median 0.99 and concluded the model would not personalise. P1 says the
classifier is sound — 15/15, including on prose that is not a badge word at all.
So the badge is reading something real. What it is reading is this: the model
writes `unchanged` **when it has nothing company-specific to say about that
duty**, and the column where that nothing would have surfaced is empty to within
0.002 of unrelated text.

That is a different and more actionable failure than "the model collapses". The
goal text is doing the work. The implication column is decoration.

## What this does not show

- **The divergence gap is measured by lexical similarity.** Two texts saying the
  same thing in different words score low, which biases the implication number
  **downward**. The test is harder to pass than it looks; a null would not have
  been proof of emptiness.
- **The cross-company pair varies more than company identity** — jurisdiction,
  regulation set, case framing (PREREG_M10 §6.2). A rise in divergence is
  evidence that the column became company-specific, not that it became
  company-IDENTITY-specific.
- **Nothing here says whether the goal text is good.** Divergence is a proxy for
  specificity. The blind L2 rubric (`PLANO_FECHO.md` §4.1) is still the only
  thing that can answer that, and it is still pending.
- **The 0.88 ceiling never bit** (`nv_over_limit = 0` in all four M09 cells) and
  the 0.30 floor has 58 points of unused headroom. Neither is a safety property
  today. Suspending them was proposed by the council chairman and **not acted
  on**: `METRICS.md` M-05b already records an identical judgement as a
  behavioural change that affects aborts, registered and not executed without an
  experiment. Changing the rule after seeing the notes is the error M10 exists to
  catch.

## Decision

Per §5, the implication branch authorises an intervention aimed at that column
and nothing else. **[PREREG_M11](PREREG_M11_IMPLICATION.md)** is frozen: one
clause changes, requiring a named checkable artefact from the fact sheet, with an
explicit escape for duties that touch none. Q4 tests the downside the clause
invites — asking for a named artefact is exactly the move that invites inventing
one.

The two M07/M08 gates stay as they are until that runs.