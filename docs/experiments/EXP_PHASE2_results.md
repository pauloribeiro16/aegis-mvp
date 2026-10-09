---
document_id: AEGIS-EXP-PHASE2
title: 'Phase 2 end-to-end — Doc02 carries the company'
version: 1.0.0
created: 2026-10-09
status: 'COMPLETE — SUPPORTED, with two registered deviations'
prereg: PREREG_P2_01.md
prereg_version: 1.0.0
upstream: 'docs/decisions/ADR-2026-10-09_phase2-objective-bridge.md; docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md'
---

# EXP_PHASE2 — Phase 2 end-to-end

**Results for [PREREG_P2_01.md](PREREG_P2_01.md) v1.0.0, frozen 2026-10-09 before
the first Phase 2 job was submitted.** Deucalion, jobs 1996446 / 1996447,
`qwen3.8:27b`, seed 42, temperature 0.2, pipeline rev `aa2600e`, n=1 per case.
Phase 1 inputs are copies of the M07 runs (rev `b2fe2aa`) — see §4.

---

## Verdict: **SUPPORTED**

All seven predictions passed on both cases. Phase 2 produced, for the first time,
a Doc02 whose `Constraint` column names each company's own architecture rather
than restating the baseline definition.

| ID | Prediction | Preregistered bar | Measured | |
|---|---|---|---|---|
| Q1 | Doc01 is exactly the Phase 1 goal set | equal, 0 G0–G4 findings | 99 and 129 objectives, **0 findings** | pass |
| Q2 | Every control anchor resolves (R2b) | 0 unresolved | **0** | pass |
| Q3 | No technology leakage, no cross-case contamination | 0 G5–G7 findings | **0** | pass |
| Q4 | The constraints carry the company | `grounding_ratio` ≥ 0.50 both | **1.0** and **1.0** | pass |
| Q5 | Strict JSON holds on the first attempt | 0 L0 repairs | **0** (1 call each) | pass |
| Q6 | The two companies differ materially | ≥ 4 of 7 pairs not near-duplicates | **7 of 7** (mean similarity 0.072) | pass |
| Q7 | The constraint is not the definition restated | mean similarity ≤ 0.60 | **0.508** | pass |

## The number the phase existed for

The ledger's §3.3 recorded that in three hand-authored deliverables only
`PRIN-ENG-06` and `-07` diverge between companies, and named the difference as
the shape a real Phase 2 column should have. Measured on the generated output:

- **Case 02** (SecureBorder Solutions): `eGate kiosks`, `24/7 security operations
  centre`, `border control officers`, `traveller biometric templates`, `passport
  data`, `watchlist-derived decisions`.
- **Case 03** (OmniBank): `OmniBank internal application zone`, `managed-cloud
  provider zone`, `OmniScore AI/ML platform`, `retail customers`, `merchants`,
  `payment processing services`, `credit data`.

Per-principle cross-case similarity: 0.018, 0.042, 0.049, 0.037, 0.157, 0.110,
0.088. The invariance test that ADR-013 D2 set as the phase's failure mode does
not fire on any principle.

## Doc01: the three measured columns stayed seams

99 and 129 objectives, with `Criteria`, `Method` and `Responsible Owner` unset in
**every** row. That is the ADR-013 D3 verdict, not an omission: the offline scan
found no rule that reproduces, and the criteria column collapses from 100
distinct values to 4 once the sub-domain slug is normalised. See
`scripts/phase2_rule_discovery.py` and ADR-013 §3.

## What the session actually cost: three Phase 1 mechanisms

Phase 2 did not run for most of this session because Phase 1 does not complete
under the registered model. Three distinct mechanisms, two of them harness
defects rather than model errors. Sub-domains lost, before and after:

| Case | Before | After |
|---|---|---|
| Case_01 | `D-04.1`, `D-06.3`, `D-06.4` | `D-06.1` |
| Case_02 | `D-06.3`, `D-06.4` | `D-06.3` |
| Case_03 | `D-04.3`, `D-04.4`, `D-06.1`, `D-06.3` | `D-06.4` |

1. **The p4 repair had no stopping rule** (jobs 1996170). `AG-D-06.4-002` came
   back at retention 0.161 / similarity 0.012; the repair answered "keep the
   Sub-SO's own obligation vocabulary" by pasting the baseline — 1.000 / 1.000,
   the exact opposite bound. The floor message also appended the baseline with
   "restate (verbatim, do not omit any leg)". Across 642 passing D-06.3/D-06.4
   rows the corridor is wide (retention 0.304–1.000, median 0.619; similarity
   0.004–0.862, median 0.112) — the model crosses it routinely and was never
   told it existed. Fixed in the message. **Thresholds 0.30 and 0.88 untouched.**
2. **The p4 exemplars were baseline prose** (job 1996171). `D-04.4` and
   `D-06.1` copied at 90% and 100% on the *first* attempt, so no repair message
   reaches them. The instruction quoted two D-01.1 Sub-SO excerpts; measured
   against their own baselines one scores 0.669 similarity — 76% of the ceiling
   the same gate enforces — and the other 0.178 retention, i.e. would itself
   fail the floor. Removed; the instruction is now 0.077 max against any Sub-SO.
3. **`check_grounded` read a legal citation as a fabrication** (job 1996171,
   `D-04.3`). The model cited "Implementing Regulation (EU) 2024/2956" correctly;
   the normaliser stripped the year, left `2956`, and failed the row. Fixed in
   the normaliser. Genuine invented quantities still fail.

A fourth defect was mine: **G7 fired on ordinary English** (`boundary`,
`including`, `within`, `flows`) on the first real Phase 2 run, because the
foreign vocabulary was built from other cases' Doc02 prose rather than their
intake forms. A gate that fires on the language is not a gate; fixed, with three
tests pinning it.

## Deviations from the preregistration

- **D1 — the Phase 1 inputs are copies, not fresh runs.** §2 registered a fresh
  `p1` → `phase2` per cell and named `run_m07_qwen3_8_27b_c2/c3` as the evidence
  that those cases complete. Phase 1 did not complete, so the M07 run
  directories were **copied** to `run_p2b_c2` / `run_p2b_c3` on the cluster and
  Phase 2 ran against the copies. The originals are untouched. The consequence
  recorded in §2 does not bite: Q1 compares each run's Doc01 against *its own*
  Phase 1 goals, so a divergence would surface as a Q1 failure rather than pass
  silently.
- **D2 — the pipeline revision is `aa2600e`, not the revision frozen with the
  preregistration.** Three Phase 1 fixes and the G7 fix landed between freezing
  and running. The Phase 1 *inputs* were produced at `b2fe2aa`. Phase 2's own
  code path is unchanged across the last two commits except the G7 vocabulary
  source, which is a gate fix and not a generation change.
- **D3 — Case_01 is absent**, per the registered exclusion X1, whose falsifier
  (a Case_01 Phase 1 that passes G0) did not fire. A Case_01 attempt at rev
  `7d603e8` reduced its failures from three sub-domains to one and still did not
  close.

## What this does not show

- **`grounding_ratio` is lexical.** It counts tokens, so it would be inflated by
  a constraint repeating fact-sheet vocabulary without binding it to a boundary.
  It is a floor on specificity, never a proof of it. 1.0 on both cases should be
  read as "no constraint was pure restatement", not as "perfect calibration".
- **Cross-case divergence is not quality.** Q6 measures difference, not
  correctness. Only a human applying the invariance test per row can tell
  different-and-right from different-and-paraphrased; that review is G-P2-A and
  has not been done.
- **One model, one stack, n=1.** A3 (one rater) does not bind here — no LLM judge
  is involved — but A2 (one model) binds as always.
- **The removal of the p4 exemplars may shift the `adjustment` badge
  distribution** that M07 measured. Nothing here re-measures it; the next
  comparison against M07 needs that first.
- **The three Phase 1 mechanisms are narrowed, not closed.** One sub-domain per
  case still loses every attempt, and the remaining failure is a first-attempt
  copy — a cause the repair messages structurally cannot reach.

## Decision

Phase 2 as built is **released for use on the two registered cases**, with the
seams visible. The three Doc01 columns stay `—` until a rule reproduces them
(ADR-013 D3). G-P2-A review of the two Doc02 documents is the next gate, and it
is a human review of the Constraint column, not of the format.

`scripts/check_results_prereg.py` does **not** scan this file: its
`RESULTS_RE` is `^EXP\d.*results.*\.md$` and this is `EXP_PHASE2_results.md`,
so the check is skipped exactly as it is for the M09/M10/M11 documents. The
`prereg` and `prereg_version` frontmatter is present regardless, so the file
becomes scannable the moment that regex is widened.