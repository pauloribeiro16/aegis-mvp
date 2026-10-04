---
document_id: AEGIS-EXP-L2-RUBRIC
title: 'L2 human scoring rubric — the two-stage instrument for EXP-03'
version: 1.0.0
created: 2026-10-03
status: ACTIVE
sources: 'docs/research/sources.yaml'
---

# L2 human scoring rubric

This is the measurement instrument EXP-01 §5 designed but never executed. It
replaces EXP-01's empty table: same intent, now with score anchors, a blinding
protocol, a sampling rule, a data format, and the three instrument controls
that a single-rater design owes its reader.

**The instrument's basis.** The registry records why an unanchored rubric is
not an instrument: judges score the rubric as much as the response (S-114), and
a judge's ability to detect success is bounded (S-134). The defences available
to a *human* single-rater design are explicit anchors, blinding, and the three
controls of §6. This document implements them.

**The scale is 1–5 with written anchors.** No score may be assigned that the
anchors do not determine; a judgement the anchors do not cover is recorded as
**0 (undetermined)**, never resolved by preference. Undetermined scores are
reported in the aggregate and are evidence that the anchors need revision —
not noise to be averaged away.

## 1. What is scored, and what is not

Only sections the model writes: **§2** (framing), **§3** (goal rows), **§4**
(tension resolutions). §0, §1, §5 and §6 are code-derived and are excluded —
scoring them would dilute the instrument with content that cannot vary.

Two document-level properties are also scored because no sampled row can
carry them: the **sub-domain selection set** and the **cross-row implication
repetition**.

## 2. Stage 1 — always applied

### 2a. Sampled goal rows (holistic, 1–5)

Per document, sample **8 goal rows**, stratified by sub-domain block: sort the
blocks canonically, split the row list into 8 contiguous strata by row index,
and take the row at a within-stratum position drawn with the registered seed
(§5). Never the first N rows — openers are calibrated differently by every
generator.

Score each sampled row **holistically** against these anchors:

| Score | Anchor (a row earns the score if it is best described by this statement) |
|---|---|
| **5** | The row restates the Sub-SO duty completely in the company's own operational terms: every obligation leg survives, the calibration names a concrete company fact from the intake, the implication could not be pasted into another company's document, and pattern/property/adjustment are not merely in-vocabulary but visibly correct for the duty. |
| **4** | The duty survives and the calibration is real, but one dimension is shallow: the company fact is generic ("as a small company") rather than concrete, or the implication is specific but could fit two duties of the same company. |
| **3** | The duty is recognisable but the calibration is thin: the row is close to a restatement of the Sub-SO with a company name attached, or the implication is true of any small company rather than this one. Legally complete, analytically lazy. |
| **2** | A material defect: an obligation leg is dropped or distorted, the "calibration" contradicts the intake, or the adjustment label is not justified by the row's own text (e.g. `narrowed:` with no warrant). |
| **1** | The row fails its duty: substantively wrong about the obligation, fabricated company facts, technology/vendor leakage, or near-verbatim baseline copy. |
| **0** | Undetermined — the anchors above do not decide this row. Record what is missing from the anchors in the notes column. |

### 2b. Document-level items (1–5 each, same anchors idea)

| # | Item | 5 anchor | 1 anchor |
|---|---|---|---|
| D1 | §2 Size dimension | names employee count/turnover band consistent with the intake | vague or inconsistent with the intake |
| D2 | §2 Area of operation | names the actual product/market | generic sector words |
| D3 | §2 Regulatory roles | names the roles (controller/manufacturer/…) with basis | role words without basis |
| D4 | §2 Inherited capabilities | names what the company already has that helps | empty flattery or invented capability |
| D5 | Tension set (§4) | the tensions that actually interact for this profile are the ones present | missing an obvious interaction, or a fabricated tension |
| D6 | Resolution quality (§4) | each resolution is one auditable binding rule | "monitor and review" filler |
| D7 | Selection set | the selected sub-domain set is defensible for this company and regulations | a clearly inapplicable selection, or an obvious omission |

## 3. Stage 2 — only where Stage 1 scored ≤ 3

The three most discriminating sub-criteria from EXP-01's original table, scored
pass/fail per low-scoring row, so the *reason* a row failed is data and not
impression:

- **Obligation legs retained** (all legs of the Sub-SO duty appear, reworded)
- **Company-proportional** (calibration names this company's scale/reality from the intake)
- **Implication specific** (the implication says something true only of this company and this duty)

## 4. Aggregation (fixed in advance)

- **Row composite** = mean of sampled holistic scores, with the share of rows
  ≥ 4 and the count of rows ≤ 2 reported alongside.
- **Document composite** (the EXP-03 primary) = mean of the 7 document items,
  with D1–D4 (framing) also reported as a sub-composite and D5–D7 as another.
- Stage-2 pass rates are reported per failure cause, never averaged into the
  composite.
- **0 (undetermined) scores** are excluded from means and their count reported.
- No aggregation runs before all scores for the batch are entered (§5).

## 5. Blinding and procedure

1. Documents are exported to plain markdown with **all arm-identifying
   metadata stripped** (no run id, no manifest, no export path, no timestamps,
   §0 removed — it carries no model content anyway).
2. The presentation file pairs documents and randomises order with the
   registered seed (below). The mapping file is written to the runs directory
   and is not opened until scores are entered.
3. Scores are entered into **`L2_SCORES.csv`** with columns:
   `doc_key, unit, item, score, notes` (unit = `row:<AG-ID>` or `doc:D<n>`).
4. Only after the batch is entered is the mapping opened and joined.
5. Registered seeds: row sampling `20261003`, presentation order `20261004`,
   retest re-sampling `20261005`.

## 6. Instrument controls (single-rater design)

1. **Test–retest.** After ≥ 7 days, 4 documents (2 per arm, sampled with the
   retest seed) are re-scored blind. Report weighted Cohen's κ on the 1–5 row
   scores and per-item exact agreement on the document items. **Interpretation
   fixed now:** κ ≥ 0.7 the instrument is usable for group comparison;
   0.4–0.7 usable with caveats stated in every result; < 0.4 the instrument
   fails and EXP-03's primary reverts to the objective metrics with the rubric
   reported as exploratory only.
2. **Criterion independence.** Pairwise correlations among D1–D7 across all
   scored documents. If the off-diagonal mass sits near 1, the rubric measures
   one thing, and the composite is reported as a single dimension with that
   stated.
3. **Anchor sufficiency.** The count and content of 0 (undetermined) scores is
   the audit of the anchors themselves: any recurring undetermined pattern
   becomes an anchor revision in the next rubric version, never a silent
   judgement call.

## 7. Relation to EXP-01's table

EXP-01 §5 proposed per-row criteria (obligation legs, proportionality,
implication specificity, pattern/property correctness, adjustment honesty) and
document-level items (framing, tensions, selection). All of them survive here:
the row criteria collapsed into the holistic anchors (Stage 1) and reappear
analytically as Stage-2 sub-criteria on low scorers; the document items are D1–
D7. The 1–5 scale, the aggregates (mean, share ≥ 4, worst-5, reusable-sentence
count) and the blind requirement are carried over unchanged. The reusable-
sentence count is now measured mechanically as well
(`quality.implication_reuse`), so the human judgement and the number can be
compared — one more place where the instrument validates itself.
