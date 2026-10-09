# PREREG_P2_01 — Phase 2 end-to-end: does Doc02 carry the company?

Version: 1.0.0
Status: FROZEN 2026-10-09, before the first Phase 2 job is submitted.
Frozen by: aegis-mvp executor, after ADR-013 and before any GPU time.
Matrix id: P2-01. No arms — one configuration, two cases, n=1 each.
Run tags: `p2_c2`, `p2_c3`.

---

## 1. What this tests, and why it is not a tuning exercise

Phase 2 has never run end to end. ADR-013 settled what the phase is *for*
(§4.1 of the determinism ledger was an open methodology question, now decided):
Doc01 is a deterministic spine of `PO-/SO-` objectives, and the one generative
cell in the whole phase is Doc02's per-company architectural `Constraint`.

The ledger measured, over three hand-authored deliverables, that this column is
where two unrelated companies actually diverge: `PRIN-ENG-06` reads "strictly
scoped DTOs" in one and "strictly scoped data views" in the others;
`PRIN-ENG-07` enumerates different data stores in each. Every other Doc02 column
is identical across companies. This experiment asks whether the pipeline
produces that same kind of divergence, or whether it emits the principle
definition restated with the company name swapped in — the failure the whole
phase has to avoid.

It is not a prompt-tuning matrix. Two interventions on adjacent columns have
already failed (M09, M11), and ADR-013 D3 settled the three unseamed Doc01
columns by offline measurement rather than by asking a model to do better.

## 2. Inputs, cases, and one registered exclusion

Phase 2 consumes a completed Phase 1 run directory. Each cell is a **fresh run
directory** carrying `p1` then `phase2`, chained `afterok` — the repository's own
pattern for every multi-stage matrix since M09. Phase 1 is *not* copied from an
older run: appending Phase 2 artefacts to an M07 run directory would mutate a
closed experiment's provenance, and the evidence that these two cases complete
at full coverage under the registered configuration is already in hand:

| Case | Evidence it completes under the registered config | Model | Seed / temp |
|---|---|---|---|
| `Case_02_SecureBorder_Solutions` | `run_m07_qwen3_8_27b_c2_1983783`, 38/38, passes G0 | `qwen3.8:27b` | 42 / 0.2 |
| `Case_03_OmniBank` | `run_m07_qwen3_8_27b_c3_1983785`, 38/38, passes G0 | `qwen3.8:27b` | 42 / 0.2 |

Under EXP-02 a seeded Phase 1 run is bit-reproducible (15 runs, byte-identical
goal sets, retention sd = 0.0000), so a fresh Phase 1 at the registered
configuration is expected to reproduce the M07 goal set. That expectation is
**not** assumed by any prediction below: Q1 compares each run's Doc01 against
*its own* Phase 1 goals, so a divergence would show up as a Q1 failure rather
than pass unnoticed.

Both cases are multi-regulation and structurally unlike each other — a
border-solutions manufacturer and a bank — which is the minimum needed for a
cross-case claim.

**X1 — registered exclusion: `Case_01_TinyTask_SaaS`.** Its Phase 1 run under the
registered model (`run_m07_qwen3_8_27b_c1_1983781`) carries
`steps/goals/D-08_3.json` with an **empty** `goals` array: D-08.3 was selected,
a file was written, and no goal was derived. Gate G0 refuses the run. Note what
this looks like to a file count — 38 goal files for 38 selected sub-domains, a
clean match — and what it looks like to the gate: 65 objectives over **37**
sub-domains. Including Case_01 would therefore require a Phase 1 re-run whose
completion is not established for this model, and its failure is not specific to
Phase 2. This exclusion is registered, not silent. *Falsifier for the exclusion
itself: a Phase 1 run of Case_01 under `qwen3.8:27b` that passes G0. Should one
appear, Case_01 enters as a third cell and this section is amended **before** its
job is submitted.*

## 3. Held fixed

Model `qwen3.8:27b`, seed `42`, temperature `0.2`, no top_p/top_k override
(AGENTS.md §-1: these are measured defaults, not preferences). Ficha
`PROM-P2-03` v1.0.0, frozen before submission and recorded in
`config.json.prompt_digests`. Corpus revision `e3cb492` plus this change set.
One call per case — the `p2d` step is transversal, never per sub-domain.
No human gate is pre-approved; G-P2-A is reviewed after the fact from the
artefact.

## 4. Metrics, and what each one is measuring

| ID | Metric | Source | Baseline / expectation |
|---|---|---|---|
| `P2-M1` | Doc01 objective count vs Phase 1 goal count | `manifest.stage_result.phase2` | equal, by gate G4's bidirectional assertion |
| `P2-M2` | Gate findings, G0–G4 (Doc01) | `phase2.check` | 0 |
| `P2-M3` | Gate findings, G5–G7 (Doc02) | `phase2.check_doc02` | 0 |
| `P2-M4` | Unresolved control anchors | rglob under `baseline/CONTROLS/` | 0 (R2b) |
| `P2-M5` | **`grounding_ratio`** — share of the 7 constraints containing content present in the fact sheet and absent from all 7 principle definitions | `phase2.grounding_ratio` | no prior; see Q4 |
| `P2-M6` | `L0` repair rounds needed on the `p2d` answer | `trace.jsonl` `l0_first_error` | 0 |
| `P2-M7` | Cross-case constraint divergence — share of constraint pairs that are not near-duplicates | pairwise similarity | see Q6 |
| `P2-M8` | Constraint-vs-definition similarity — mean over the 7 | `quality.near_verbatim_similarity` | low; see Q7 |

`P2-M5` and `P2-M7`/`P2-M8` are **measurements with falsifiers, deliberately not
gates.** M11 established that demanding a named artefact from the fact sheet
does not make a column more company-specific (+0.031 against its own control's
+0.042); gating on that would reject a 7-row document into uselessness while
teaching nothing.

## 5. Predictions, frozen

- **Q1 (decisive) — Doc01 is exactly the Phase 1 goal set, once each.**
  `P2-M1` equal and `P2-M2` = 0 for both cases.
  *Falsifier: any G0–G4 finding on either case.*
- **Q2 (decisive, R2b) — every control anchor resolves.** `P2-M4` = 0.
  *Falsifier: ≥ 1 anchor that does not resolve to a file under `baseline/CONTROLS/`.*
- **Q3 (decisive, R10b) — no technology leakage and no cross-case contamination.**
  `P2-M3` = 0 for G5, G6 and G7 on both cases.
  *Falsifier: ≥ 1 G5/G6/G7 finding.*
- **Q4 (primary) — the constraints carry the company.** `P2-M5` ≥ 0.50 on
  **both** cases, i.e. at least 4 of 7 constraints contain company content that
  is absent from the universal definitions.
  *Falsifier: `P2-M5` < 0.50 on either case.*
- **Q5 (format) — the strict JSON schema holds on the first attempt.**
  `P2-M6` = 0 for both cases.
  *Falsifier: any L0 repair round on either case.*
- **Q6 (cross-case) — the two companies get materially different constraints.**
  `P2-M7` ≥ 0.50, i.e. at least 4 of 7 pairs are not near-duplicates.
  *Falsifier: `P2-M7` < 0.50.*
- **Q7 (registered downside) — the constraint is not the definition restated.**
  Mean `P2-M8` similarity ≤ 0.60.
  *Falsifier: mean similarity > 0.60.*

## 6. Decision rule, fixed in advance

| Q1–Q3 | Q4 | Outcome recorded |
|---|---|---|
| all pass | pass | **SUPPORTED** — Phase 2 as built emits objectives that are anchored, complete and technology-neutral, and a constraint that names the company. |
| all pass | **fail** | **PARTIAL** — the deterministic half is sound and the generative half did not differentiate. This is the ledger's §3.3 claim failing for the pipeline, and it is a result, not a defect to be patched before it is written down. |
| any fail | any | **REFUTED / INCONCLUSIVE** — whichever fired is recorded as the falsification. |

**Stopping rule.** If Q1, Q2 or Q3 fails on the **first** case, the second case
is **not** submitted. The negative result is recorded with its gate finding; the
remaining GPU time is not spent producing a second instance of a known failure.
If Q4 alone fails, both cases run — the measurement is the point.

n=1 per cell is justified by EXP-02: 15 seeded runs produced byte-identical
goal sets (retention sd = 0.0000), so a second run measures the sampler, not
the pipeline.

## 7. Declared limitations, so the verdict is not read for more than it is

- **One model, one stack.** `qwen3.8:27b` on an A100 with Ollama 0.32.13. A
  different model may restate the definitions where this one does not. A3
  (one rater) is unaffected here — no LLM judge is involved, so no judge noise
  floor is needed for any metric in §4.
- **The deterministic half is not re-tested by this run.** Q1–Q3 confirm the
  Phase 2 gates over already-existing Phase 1 artefacts; they say nothing about
  Phase 2 applied to a run whose Phase 1 was itself defective.
- **`grounding_ratio` is a lexical measure.** It counts tokens, so it would be
  inflated by a constraint that repeats fact-sheet vocabulary without binding
  it to an architectural boundary. It is a floor on specificity, never a proof
  of it — which is why Q4 is a prediction and not a gate.
- **Cross-case divergence is not evidence of quality.** Two constraints
  differing is consistent with two companies being genuinely different and with
  the model paraphrasing the same text differently. Q6 measures difference, not
  correctness; only a human reviewer applying the Invariance Test can tell them
  apart, and that review is G-P2-A, recorded after the run.
- **Case_01's absence narrows the claim.** The invariance test's most extreme
  case (8-person micro-SaaS against a bank) is unregistered here for the reason
  in §2.

## 8. Instruments recorded

- `pipeline/src/phase2.py` — derivation, Doc01/Doc02 rendering, gates G0–G7.
- `scripts/phase2_rule_discovery.py` — the offline measurement that settled the
  three unseamed Doc01 columns (ADR-013 §3). Zero GPU-h; run before this.
- `pipeline/src/steps.py:parse_p2d` — the L0 contract.
- `docs/pipeline/prompts/PROM-P2-03_SYNTHESIZE_PRINCIPLES.md` v1.0.0 — the ficha.
- `docs/decisions/ADR-2026-10-09_phase2-objective-bridge.md` — what Phase 2 is for.
- `pipeline/tests/phase2_test.py` — 12 test functions, no model, no GPU.
- `trace.jsonl` per call; `steps/stage_result.json` `stages.phase2` per run.