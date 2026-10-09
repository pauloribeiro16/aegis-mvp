# PREREG_P2_02 — Phase 2 enriched: do the four increments hold in production?

Version: 1.0.0
Status: FROZEN 2026-10-09, before the first enriched Phase 2 job is submitted.
Frozen by: aegis-mvp executor, after the hardening commit `3ea5f38` and before any GPU time.
Matrix id: P2-02. No arms — one configuration, three cases, n=1 each.
Run tags: `p2c_c1`, `p2c_c2`, `p2c_c3`.
Upstream prereg: [PREREG_P2_01.md](PREREG_P2_01.md) v1.0.0 (its results: [EXP_PHASE2_results.md](EXP_PHASE2_results.md), SUPPORTED).

---

## 1. What this tests, and why it is not a tuning exercise

Phase 2 ran end to end once (P2-01, jobs 1996446/1996447) as a minimal phase:
Doc01 fully deterministic with `criteria`/`method`/`owner` as UNSET seams, Doc02
the only generative surface. AEGIS-P2-ENRICH (researcher-approved plan,
2026-10-09) turns the phase into systems engineering per ISO/IEC/IEEE 29148 /
INCOSE through four increments, implemented in `748b8ec..3ea5f38` and never yet
executed:

1. **Empirical methods & falsifiable criteria** — every objective classified
   into one of `TEST` / `INSPECT` / `DEMONSTRATE` / `ANALYZE` with a criteria
   naming measurable evidence (per-objective LLM cell `p2o`, ficha
   `PROM-P2-01` v1.0.0).
2. **Operational translation** — one contextual paragraph per active
   sub-domain explaining how THIS company operationalizes it, grounded in the
   fact sheet.
3. **Strategic tensions** — §2 of Doc01 harmonises the multi-regulation
   tensions Phase 1 already recorded (`steps/tensions.json` from `p4t`;
   deterministic re-render, no new model call).
4. **The `RULE-*` tail** — 1–2 EARS/RFC 2119 operational engineering rules per
   objective, the bridge to Phase 3 that SPEC §6 assigns to this phase.

This experiment asks whether the enriched phase produces that substance on real
runs: seams actually filled, methods genuinely distributed rather than
collapsed to one default, rules that are imperative and unique, translations
that are this company's and not another's. It is not a prompt-tuning matrix:
the fichas are frozen, the validators were built before the first run, and the
failure modes this measures are the ones the plan named (vague criteria, method
collapse, cross-case contamination, an empty catalogue).

## 2. Inputs, cases, and the Case_01 repair

Phase 2 consumes a completed Phase 1 run directory. As in P2-01 (deviation D1,
accepted), each cell is a **copy** of the M07 run directory, not a fresh Phase 1
run — the goal sets are the registered evidence and re-deriving them adds GPU
cost without adding information. The copies are new directories
(`run_p2c_c1/c2/c3`); the P2-01 directories (`run_p2b_*`) are untouched as the
v1 record. Originals: `run_m07_qwen3_8_27b_c{1,2,3}_{1983781,1983783,1983785}`,
`qwen3.8:27b`, seed 42, temperature 0.2.

| Case | Phase 1 evidence | Note |
|---|---|---|
| `Case_02_SecureBorder_Solutions` | 38/38 goals, passed G0 in P2-01 | 99 objectives |
| `Case_03_OmniBank` | 38/38 goals, passed G0 in P2-01 | 129 objectives |
| `Case_01_TinyTask_SaaS` | 37/38 goals; `D-08.3` empty | see below |

**Case_01 and the X1 override.** PREREG_P2_01 §2 registered Case_01 as excluded
(X1) because `steps/goals/D-08_3.json` carries an empty `goals` array. The
researcher rejected that exclusion on 2026-10-09: all three cases are attempted,
and a case that does not complete is a result, not a reason to swap it. The
repair attempted here is upstream and honest: on the `run_p2c_c1` **fork only**,
the empty D-08.3 goal artifacts (`D-08_3.json`/`D-08_3.md`) are deleted and
stage `p4` re-run — per-sub-domain resume skips the 37 complete sub-domains and
re-derives exactly D-08.3 (one model call). **D1 (registered deviation): if the
repaired `p4` call again derives zero goals, phase2 aborts at G0 and that is
the recorded outcome for this cell** — the gate is not weakened to let the run
through (the working-tree attempt to make G0 file-count-based was reverted in
`3ea5f38` for precisely this reason).

## 3. Held fixed

Model `qwen3.8:27b`, seed `42`, temperature `0.2`, no top_p/top_k override
(AGENTS.md §-1 measured defaults). Fichas `PROM-P2-01` v1.0.0 (p2o, one call
per active sub-domain) and `PROM-P2-03` v1.0.0 (p2d, one transversal call),
frozen before submission. Pipeline rev `3ea5f38` (enrichment
`748b8ec..85fa795` + hardening), corpus unchanged from P2-01. Gates
pre-approved (unattended experimental run, PREREG_01 fixed condition); G-P2-A
reviewed after the fact from the artefacts. Walltime 2h per job (39 sequential
calls). Validators frozen with the code: method vocabulary and EARS/RFC 2119
syntax per rule (parse-time), G0–G4 (Doc01), G5–G7 (Doc02), the 60%
mode-collapse ceiling on the method distribution (R10b), the non-empty
`RULE-*` tail per objective, criteria ≥ 8 words and unique per sub-domain.

## 4. Metrics

| ID | Metric | Source | Baseline / expectation |
|---|---|---|---|
| `P2M1` | Doc01 objective count vs Phase 1 goal count | `stage_result.phase2` | equal (gate G4) |
| `P2M2` | Gate findings G0–G4 (Doc01) | `phase2.check` | 0 |
| `P2M3` | Gate findings G5–G7 (Doc02) | `phase2.check_doc02` | 0 |
| `P2M4` | Unresolved control anchors | rglob under `baseline/CONTROLS/` | 0 (R2b) |
| `P2M5` | **Seam fill** — objectives whose `method`/`criteria`/`owner` came through | `stage_result.seams_filled` | ≥ 95% per case |
| `P2M6` | Operationalized sub-domains vs selected | `stage_result.operationalized_subdomains` | 38/38 (or 38/38 with the repaired D-08.3 on c1) |
| `P2M7` | **Method distribution** — share of the most-used method | `stage_result.method_distribution` | max share ≤ 0.60 (R10b ceiling) |
| `P2M8` | **RULE-* tail** — rules per objective, mean and share of objectives with ≥ 1 | `steps/phase2/*.json` | ≥ 1 by gate; mean within the ficha's 1–2 (padding bar: mean ≤ 2.5) |
| `P2M9` | `grounding_ratio` on Doc02 (unchanged surface) | `phase2.grounding_ratio` | ≥ 0.50 both multi-regulation cases |
| `P2M10` | **Cross-case divergence of the new cells** — mean pairwise similarity of `operational_translation` (and of RULE statements) across the three cases | token similarity, same instrument as P2-01 Q7 | ≤ 0.60 |
| `P2M11` | L0 repair rounds / skipped sub-domains on `p2o` | `trace.jsonl`, stage log | reported; a skipped sub-domain is a `P2M5`/`P2M6` failure, not a silent gap |

`P2M5`, `P2M7`, `P2M8` and `P2M10` are the new substance; `P2M7` is a gate as
well as a measurement (the batch aborts above the ceiling), which differs from
the P2-01 convention of measure-only — registered here as a deliberate choice
because the plan's Increment 1.3 specifies the validator, and the per-sub-domain
JSONs survive an abort for analysis.

## 5. Predictions, frozen

- **Q1 (decisive) — the deterministic spine is intact.** `P2M1` equal and
  `P2M2` = 0 on c2 and c3.
  *Falsifier: any G0–G4 finding on either case.*
- **Q2 (decisive, R2b) — every control anchor resolves.** `P2M4` = 0.
  *Falsifier: ≥ 1 anchor that does not resolve under `baseline/CONTROLS/`.*
- **Q3 (decisive, R10b) — Doc02 stays clean under the richer pipeline.**
  `P2M3` = 0 and `P2M9` ≥ 0.50 on c2 and c3.
  *Falsifier: any G5/G6/G7 finding, or `P2M9` < 0.50.*
- **Q4 (primary — the phase's new substance).** `P2M5` ≥ 95% and `P2M6` = 38/38
  on c2 and c3.
  *Falsifier: fill rate < 95%, or any selected sub-domain left unoperationalized.*
- **Q5 (primary — methods are classified, not defaulted).** `P2M7` ≤ 0.60 on
  every case, and all methods within the published vocabulary.
  *Falsifier: the diversity gate fires, or a method outside
  {TEST, INSPECT, DEMONSTRATE, ANALYZE} survives to a document.*
- **Q6 (primary — the catalogue exists).** Every operationalized objective
  carries ≥ 1 rule (gate), mean rules/objective between 1.0 and 2.5, rule ids
  unique within each sub-domain, every statement containing SHALL or MUST.
  *Falsifier: a sub-domain skipped for an empty tail, mean > 2.5, or a
  duplicate/imperative-violating id reaching a rendered table.*
- **Q7 (cross-case) — the new cells carry the company, not a template.**
  `P2M10` ≤ 0.60 mean similarity across case pairs, for translations and for
  RULE statements.
  *Falsifier: mean similarity > 0.60 on either cell family.*
- **Q8 (Case_01 outcome, registered either way).** The repaired `p4` call
  derives ≥ 1 goal for D-08.3 and the c1 cell passes Q1–Q3 like the others.
  *Falsifier: the repair again derives zero goals (abort at G0, recorded per
  D1), or any Q1–Q3 falsifier firing on c1. Either way c1's outcome is
  reported as its own cell, never imputed to the pipeline.*

## 6. Decision rule, fixed in advance

| Q1–Q3 (c2, c3) | Q4–Q6 | Outcome recorded |
|---|---|---|
| all pass | all pass | **SUPPORTED** — the enriched phase fills its seams, classifies methods without collapsing, and emits a unique EARS rule catalogue bound to each company. |
| all pass | any fail | **PARTIAL** — the spine holds; the failing increment is recorded with its metric (a result, not a patch-before-writing opportunity). |
| any fail | any | **REFUTED / INCONCLUSIVE** — whichever fired is the recorded falsification. |

**Stopping rule.** If Q1–Q3 fails on the first completed case, the remaining
cases are not submitted: the negative result is recorded with its gate finding.
Q8's failure does **not** stop c2/c3 — Case_01's upstream state is independent
of the enriched phase.

n=1 per cell justified by EXP-02 (seeded runs are bit-reproducible; a second
run measures the sampler, not the pipeline).

## 7. Declared limitations

- The `p2o` cells are one call per sub-domain against the SAME model that
  produced the Phase 1 goals; method-classification quality is bounded by that
  model's judgement. The gates bound syntax and distribution, not
  appropriateness — whether `TEST` was the right method for an objective is a
  G-P2-A human-gate question, reviewed after the fact.
- Cross-case similarity is a token-overlap instrument (same family as P2-01
  Q7): it detects near-verbatim reuse, not paraphrased plagiarism.
- The tension harmonisation (increment 3) re-renders Phase 1's `p4t` output;
  its quality is inherited, not re-measured here — this prereg only asserts the
  §2 tables render from the recorded tensions.
