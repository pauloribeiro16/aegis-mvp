# PREREG_M09 — Calibration instruction: literal exemplars in, literal exemplars out

Version: 1.0.0
Status: FROZEN 2026-10-07, before the first run of any arm.
Frozen by: aegis-mvp executor, on the researcher's instruction.
Matrix id: M09 (2 arms × 2 cases). Run tags: `m09_c2_ctrl`,
`m09_c2_meta`, `m09_c3_ctrl`, `m09_c3_meta`.

---

## 1. The question

The p4 instruction ends in a *style tail* that shows the model three verbatim
goal sentences and three verbatim adjustment rationales, all of them drawn from
the same corpus the model is being asked to restate. S-296 names this as the
wrong place for a requirement: what a demonstration actually supplies is the
format and the label space, not the content, so a compliance requirement
encoded in an exemplar is both misplaced and unreliable.

M07 then measured the consequence on the reference model: the
`(unchanged+verbatim)` ratio ran **0.86–1.00 across all 18 cells (median 0.99),
with zero `proportional` and zero `inherited` rows in the entire matrix**. The
instrument's own words at the time were "the same explicit restatement
instruction that helps rows pass the L0 gates also invites verbatim
restatement".

**M09 asks which half of the prompt carries that.** The exemplar and the
instruction are the two places a literal restatement style can enter from, and
M07 did not separate them. This matrix varies only the instruction.

**It does not test the exemplar.** That question has two recorded answers and
is not re-litigated here: PE-004 / S-294 (*selection by similarity works and
beats random selection*) and M07 H1 (a richer classification vocabulary changed
nothing about default collapse).

## 2. Arms

| Arm | `ficha_overrides` | p4 style tail |
|---|---|---|
| **A — ctrl** | `{}` | shipped: two literal goal exemplars + three literal adjustment rationales |
| **B — meta** | `{"p4_instruction": "meta"}` | `steps.P4_STYLE_META`: structural criteria, zero literal exemplars |

The replacement spans from the marker `Express the goal objectively and
impersonally` to the end of the instruction string (`steps.P4_STYLE_MARKER`).
Verified mechanically: the head is byte-identical between arms, so the wrap
instruction, the TERMINATION clause, the column contract, the Sub-SO enumeration
and the AI-Act stub warning are untouched. Literal `e.g. '…'` exemplars: **2 → 0**.
The arms are distinguishable by the `p4_instruction` digest in each run's
`manifest.json` (`compose.prompt_digests`), which hashes `P4_STYLE_VARIANTS`.

## 3. Held fixed

Seed 42, temperature 0.2 (`AGENTS.md §-1`; EXP-02 measured both). Model
`qwen3.8:27b` — the M07 reference, the only model that delivered all three
cases. Gates pre-approved. The exemplar is pinned (`compose.golden_text` → the
committed `example/doc02_adjusted_goals.md`), the corpus is read-only, and the
column contract (`GOAL_COLUMNS_EMIT`) is the one unified in `ba7bd7b`. **Both
arms run the same commit.** The arm is read from `config.json`
`ficha_overrides`, never from the run tag.

Cases: `Case_02_SecureBorder_Solutions` (450 employees, GDPR+CRA+NIS2+AI_Act) and
`Case_03_OmniBank` (GDPR+CRA+NIS2+DORA+AI_Act). Both LARGE. The leakage the
treatment targets is scale-specific — the shipped exemplars describe an
8-person MICRO company inheriting hosting — so the cases where it would bite
hardest are the two large ones.

n = 1 per cell. Justification: under a fixed seed EXP-02 established the
pipeline is bit-reproducible (15 seeded runs, byte-identical goal sets,
retention sd 0.0000), so within-arm variance is ~0 and one run per cell carries
the arm's whole distribution. This is the same logic as M07's n=1 cells.

## 4. Metrics (all computed by `quality.score_run`, all thresholds already declared in `METRICS.md`)

| # | Metric | Source | Reading |
|---|---|---|---|
| D | delivery: sub-domains carried / selected, L1 verdict | `validate.py` | safety |
| R | `retention`, mean over rows | M-02, floor 0.30 | obligation kept |
| V | `near_verbatim` similarity, share of rows > 0.88 | M-03 | restatement, not copy |
| X | `ratio_verbatim` = (unchanged+verbatim)/n | M-14, WARN at 0.70 | default collapse |
| P | `max_peer_similarity`, median over rows | M-16 (new, declared below) | implication diversity |

## 5. Predictions, frozen

- **P1 (safety).** Arm B delivers no fewer sub-domains than arm A on either
  case. *Falsifier: B < A on either case.*
- **P2 (the hypothesis).** Arm B's median `max_peer_similarity` is lower than
  arm A's on both cases. *Falsifier: P ≥ B on either case.*
- **P3.** Arm B's `ratio_verbatim` is no higher than arm A's on either case.
  *Falsifier: X > B on either case.*
- **P4 (registered downside, declared before the data).** The shipped goal
  exemplars are what model "keep the Sub-SO's own obligation vocabulary,
  restructure the sentence". Removing them may therefore cost retention.
  Arm B's mean `retention` stays within **0.05** of arm A's.
  *Falsifier: B mean retention < A mean retention − 0.05 on either case.*

## 6. Decision rule, fixed in advance

- **H1 SUPPORTED** — P1 and P4 hold on both cases AND P2 and P3 both move in
  the predicted direction.
- **H1 REFUTED** — P1 or P4 fails on either case. A safety or retention
  regression is a refutation regardless of what P2 and P3 do.
- **INCONCLUSIVE** — P1 and P4 hold but P2/P3 do not move. At n=1 on one model
  that is the expected outcome of a screening experiment, not a null result.

Whatever the outcome, it is recorded in `docs/experiments/M09_results.md` in the
same session as the analysis and enters `00_RESULTS.md` with the same weight as
a positive (§-2.4). A refutation is a result, not an inconvenience.

## 7. Declared limitations, so the verdict is not read for more than it is

1. **n = 1, one model, one seed.** This separates the two prompt locations from
   each other *for this model*. It cannot separate them in general, and it does
   not replicate the M07 finding — M07's own falsifier was a between-model
   criterion.
2. **Two changes in one arm.** Both exemplar sets live in the same contiguous
   span, so arm B removes the goal-style exemplars *and* the adjustment
   exemplars together. If B moves, this matrix does not say which half did it.
   Splitting them is the obvious next cell, not a result of this one.
3. **The diversity metric under-reports on short rows.** `cached_ratio` returns
   `0.0` for any pair whose length ceiling cannot reach M-07 (0.95), so
   `max_peer_similarity` is a lower bound on short implications. The bias is
   identical in both arms, so the comparison stands, but the absolute values do
   not mean "this much duplication".
4. **L2 blind scoring is still pending** (`PLANO_FECHO.md` §4.1). Every metric
   here is mechanical. Whether the rows that survive the gates are faithful
   restatements or compliance theatre remains a human judgement that no number
   in this matrix settles.

## 8. Instruments recorded

| Surface | How the two arms are told apart |
|---|---|
| code | `steps.P4_STYLE_VARIANTS`, selected by `ficha_overrides.p4_instruction` |
| config | `config.json` → `ficha_overrides` |
| manifest | `prompt_digests.p4_instruction` (hashes the variant table) |
| env | `MVP_P4_INSTRUCTION=meta` → `phase1.sbatch` → `--p4-instruction` |

The `p4_adjustment` slot is deliberately left unset in both arms: its marker no
longer exists in the shipped base text, so any value would raise rather than run.
Reported separately, not exercised here.