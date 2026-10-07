# PREREG_M11 — the Company implication intervention

Version: 1.0.0
Status: FROZEN 2026-10-08, before the first run of either arm.
Frozen by: aegis-mvp executor.
Matrix id: M11. Run tags: `m11_c2_ctrl`, `m11_c2_concrete`,
`m11_c3_ctrl`, `m11_c3_concrete`.

---

## 1. What M10 found, and why this arm exists

M10 (`PREREG_M10_INSTRUMENT.md`, `M10_results.md`) measured the two free-text
columns separately against a cross-sectional placebo — same model, same
company, a genuinely different duty — inside the M07 matrix so the instrument
is constant:

| column | cross-company | placebo | difference |
|---|---|---|---|
| **Adjusted goal** | 0.249 | 0.061 | **+0.188** |
| **Company implication** | 0.062 | 0.061 | **+0.002** |

The goal text carries the company. The `Company implication` — the one column
that exists to carry it, and the one `check_implication_specific` guards — is
**statistically indistinguishable from unrelated text**.

That also retires the standing panic without a parser story. M07's 0.99
`unchanged` ratio is not the model failing to personalise a goal. It is the
model reaching for the passive badge **when it has nothing company-specific to
say about that duty** — and the column where that nothing would have shown is
empty. The badge was reading the emptiness, not manufacturing it (M10 Leg A:
`adjustment_kind` correct on 15/15 constructed vectors).

## 2. The arm

One clause of the p4 instruction changes. Nothing else — same shipped style
tail as both M09 arms, same adjustment rule, same exemplar, same column
contract, same commit.

| Arm | `ficha_overrides` | the `Company implication` clause |
|---|---|---|
| **ctrl** | `{}` | shipped: *"1-2 sentences explaining operational impact, roles and scope"* |
| **concrete** | `{"p4_implication": "concrete"}` | must **name one checkable artefact that appears in the fact sheet** — a named system, supplier, role, volume or site — and say what the duty does to it; and, if no artefact is touched, **say so in one clause and keep it short** |

The escape clause is deliberate. Asking for a named artefact is exactly the
move that invites inventing one, so the arm gives the model a legitimate way to
decline rather than relocating the pressure. That is what Q4 tests.

## 3. Held fixed

Seed 42, temperature 0.2. `qwen3.8:27b` — the M07 reference. Gates
pre-approved. Same commit for both arms; the arm is read from
`config.json` `ficha_overrides`, never from the tag, and both arms necessarily
share the `p4_instruction` digest (it hashes the variant *tables*, not the
selection — the M09 watcher was corrected for exactly this). The arms are told
apart by `ficha_overrides.p4_implication` and by the prompt bytes.

Cases: `Case_02_SecureBorder_Solutions` and `Case_03_OmniBank`. Both carry
regulation sets large enough that several duties per sub-domain exist, which is
what makes the cross-sectional comparison meaningful. n=1 per cell; under a
fixed seed the pipeline is bit-reproducible (EXP-02), so one run carries the
arm's distribution — the same logic as M07 and M09.

## 4. Metrics, and where the baseline number comes from

The primary metric is the one M10 defined: median cross-company similarity of
the `Company implication` for the same `(sub-domain, regulation)`, minus the
median similarity of a different duty under the same company. **Baseline
+0.002**, measured on M07 (n=821 cross pairs, n=51838 placebo pairs).

| # | Metric | Baseline | Reading |
|---|---|---|---|
| Q1 | implication cross-company − placebo | **+0.002** | does the column carry the company |
| Q2 | modal-string share of the Adjustment column | 0.96–0.99 | is `unchanged` still the default |
| Q3 | sub-domains carried / 38 | — | safety |
| Q4 | `check_grounded` findings (R6 fabrications) | — | registered downside |

## 5. Predictions, frozen

- **Q1 (primary).** Arm B raises the implication cross-company difference to
  **≥ +0.10** on at least one case. *Falsifier: < +0.10 on both cases.*
- **Q2.** Arm B's modal-string share falls **below 0.80** on at least one case.
  *Falsifier: ≥ 0.90 on both — the column stayed passive whatever was asked.*
- **Q3 (safety).** Arm B carries no fewer sub-domains than arm A on either
  case. *Falsifier: B < A on either case.*
- **Q4 (registered downside).** Arm B produces **no more** `check_grounded`
  fabrication findings than arm A on either case. *Falsifier: B > A on either
  case — asking for a named artefact invited inventing one.*

## 6. Decision rule, fixed in advance

- **SUPPORTED** — Q1 fires on ≥1 case **and** Q2 fires **and** Q3 and Q4 both
  hold on both cases.
- **REFUTED** — Q1 fails, or Q3 or Q4 fails on any case.
- **INCONCLUSIVE** — Q1 and Q2 fire but Q3 or Q4 fails: the column moved and the
  way it moved is unacceptable, which is a refutation of the intervention even
  though it is evidence about the construct.

## 7. Declared limitations

1. **n=1, one model, one seed.** The primary metric is a median over ~800
   pairs, so it is far less noisy than the delivery counts, but a single run
   still carries the arm.
2. **Similarity is lexical.** Two goals saying the same thing in different
   words score low, which biases the implication divergence **downward** — the
   test is harder to pass than it looks, and a null is not proof of emptiness.
3. **The cross-company pair varies more than company identity** (jurisdiction,
   regulation set, case framing — PREREG_M10 §6.2). A rise in divergence is
   therefore evidence that *the column became company-specific*, not that it
   became *company-IDENTITY-specific*.
4. **Q1 has no external anchor.** +0.10 is derived from the placebo gap the
   goal column already shows (+0.188) as the order of magnitude a working
   column produces, and from the measured +0.002 baseline. It is a
   `convention, unmeasured → E-10`, declared here per AGENTS.md §-2.2.
5. **This says nothing about whether the result is good.** Divergence is a
   proxy for specificity, not a judgement of quality. The blind L2 rubric
   (`PLANO_FECHO.md` §4.1) remains the only thing that can answer that, and it
   is still pending.

## 8. Instruments

| Surface | How the arms are told apart |
|---|---|
| code | `steps.P4_IMPLICATION_VARIANTS`, via `ficha_overrides.p4_implication` |
| config | `config.json` → `ficha_overrides` |
| digest | `prompt_digests.p4_instruction` hashes both variant tables — equal across arms by design |
| bytes | the shipped `Company implication` clause is byte-identical in A and replaced in B |
| env | `MVP_P4_IMPLICATION=concrete` → `phase1.sbatch` → `--p4-implication` |