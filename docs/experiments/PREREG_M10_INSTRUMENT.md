# PREREG_M10 — Is the instrument measuring anything? A validity test, not an ablation

Version: 1.0.0
Status: FROZEN 2026-10-08, before any measurement code was run.
Frozen by: aegis-mvp executor, at the researcher's instruction, following the
LLM Council verdict of 2026-10-07.
Matrix id: M10.

---

## 1. The question

Every calibration claim in this programme rests on one number: the
`(unchanged + verbatim)` share of the Adjustment column. M07 measured it at
**0.86–1.00, median 0.99**, across 6 models and 3 cases, with zero `proportional`
and zero `inherited` rows in the entire matrix. M09 then varied the instruction
and the number moved the wrong way.

The Council's convergent finding was that **this number is not measuring the
construct**. Two independent reasons:

1. **Dimensional blindness.** Both gates — the 0.30 retention floor and the 0.88
   near-verbatim ceiling — are functions of a single pair: the row against its
   *own* Sub-SO. Neither references the company. Compliance theatre is by
   definition a *cross-sectional* property: does the row for company A read
   like the row for company B? An instrument that only compares a row to its
   source has no dimension on which to see it.
2. **Self-report.** The badge is a word the writing model emits about its own
   text, in the same pass that writes the text. Nobody has ever checked whether
   the classifier agrees with the prose it labels.

M10 tests the instrument, not the prompt. **It is designed to be decisive in
both directions and to spend zero cluster time.**

## 2. Why this needs no Deucalion submission — and what would

The Council's First Principles advisor proposed a company-holdout probe and the
Executor objected that it costs N companies × N generations. **That objection is
wrong here, and the reason is in the data we already have:** the three cases are
three different companies (TinyTask — 8-person MICRO SaaS; SecureBorder — 450
employees; OmniBank — a LARGE bank), and the strong runs carry **38/38
sub-domains on all three**. So for every sub-domain there are already goals
written by different companies, and in M08 two replicates exist for several
company/model cells.

The cross-sectional comparison is therefore **already paid for**. This is
re-scoring, not generation — the Executor's H1, but with the between/within
decomposition attached instead of only an obligation-recall recall.

## 3. What is measured

Population: every `steps/goals/*.json` row in `~/Work/aegis-runs/run_m07_*`,
`run_m08_*`, `run_m09_*` — the runs already delivered, read from artefacts, no
model called.

**Leg A — badge known-answer.** `adjustment_kind` is fed strings whose correct
class is known by construction, one per legal value plus adversarial cases
(empty, `—`, out-of-vocabulary prose, a badge word appearing mid-sentence).
Falsifier: any string whose emitted class ≠ its constructed class.

**Leg B — badge informativeness.** Across all delivered rows: the number of
distinct adjustment strings, the share byte-identical to the modal string, and
whether `unchanged` ever appears as a *prefix* of a longer string the model
wrote (which would mean the classifier is bucketing free prose, not reading a
choice).

**Leg C — cross-sectional divergence (decisive).** For each cell
(model, sub-domain) present in ≥2 cases, on the `Adjusted goal` text:

| quantity | definition | what it means |
|---|---|---|
| `replicate` | similarity of the same SD, same case, two runs | the floor: two copies of one deterministic output |
| `cross_company` | similarity of the same SD, **different** cases | does the company move the text at all |
| `diff_sd` | similarity of **different** SDs, same case | the placebo the Council demanded: how alike are unrelated duties |

All three are medians of pairwise `SequenceMatcher` ratios on the normalised
goal text, cells with n≥2 only.

## 4. Predictions, frozen

- **P1 (badge mechanism).** `adjustment_kind` emits the constructed class for
  every Leg-A vector. *Falsifier: any mismatch.*
- **P2 (badge informativeness).** In every run, the share of adjustment strings
  byte-identical to that run's modal string is **> 0.80**.
  *Falsifier: any run at or below 0.80.*
- **P3 (decisive).** `cross_company` is **not materially below** `replicate`.
  In numbers: median `cross_company` − median `replicate` **> −0.05**.
  *Falsifier: the difference is ≤ −0.05 — i.e. writing the same duty for a
  different company produces materially different text, which would mean the
  goals DO respond to the company and the 0.99 badge is a classifier artefact
  rather than theatre.*
- **P4 (placebo, decisive).** `cross_company` is **not materially above**
  `diff_sd` — a row for a sub-domain under one company is no more like the same
  sub-domain under another company than it is like an unrelated duty.
  *Falsifier: median `cross_company` − median `diff_sd` **> +0.05**.*

## 5. Decision rule, fixed in advance

- **P1 falsified** → the classifier is broken as a reader; the badge is
  withdrawn as evidence and every calibration claim that cites it is
  re-labelled `instrument-unverified`. **No cluster run.**
- **P3 falsified and P4 holds** → the goals *do* respond to the company; the
  0.99 is a badge artefact. The fix is the badge and the prompt vocabulary.
  **No cluster run.**
- **P3 holds and P4 holds** → theatre confirmed at the text level, and the
  badge's 0.99 is measuring something real. **This is the only branch that
  authorises a Deucalion submission**, and what gets submitted is an
  *intervention* arm with a preregistered prediction of cross-sectional
  divergence ≥ +0.10 against the control — not another measurement.
- **Both hold but P2 fails** → the badge carries more information than M07
  concluded; the M07 collapse claim needs restating before anything ships.

Nothing here is contingent on the other branch first. The whole test is
re-scoring and costs one afternoon.

## 6. Declared limitations, so the verdict is not read for more than it is

1. **Similarity is lexical, not semantic.** Two goals can say the same thing in
   different words and score low. That biases `cross_company` **upward** — it
   makes the theatre verdict harder to reach, not easier. The direction is
   recorded because it matters for reading a null.
2. **The three cases differ in more than company identity** — jurisdiction,
   regulation set, case framing. A cross-company difference could come from any
   of those, so a P3 falsification would not isolate company identity alone.
3. **`diff_sd` compares different duties**, which are less similar for trivial
   reasons. That biases `diff_sd` **downward** and makes P4 harder to satisfy.
   The two biases point in opposite directions, so neither leg is free.
4. **Replicate similarity is only available for cells M08 ran twice.** Where it
   is missing, P3 falls back to `cross_company` vs `diff_sd` alone and is
   reported as such rather than silently pooled.
5. **This says nothing about whether the surviving rows are good.** It says
   whether they differ by company. The blind L2 rubric
   (`PLANO_FECHO.md` §4.1) is still the only thing that can answer the first
   question, and this test cannot substitute for it.

## 7. Script

`scripts/exp_m10_instrument.py` — reads artefacts only, writes nothing, prints
all three legs. Reproducible: same inputs, same numbers.

    python3 scripts/exp_m10_instrument.py
    python3 scripts/exp_m10_instrument.py --json /tmp/m10.json