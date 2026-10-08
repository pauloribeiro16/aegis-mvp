---
document_id: AEGIS-M11
title: 'M11 results — asking for a named artefact does not make the implication column carry the company'
version: 1.0.0
created: 2026-10-08
status: COMPLETE — REFUTED (Q1 did not fire; Q3 and Q4 both held)
prereg: 'PREREG_M11_IMPLICATION.md'
prereg_version: 1.0.0
upstream: '[PREREG_M11_IMPLICATION.md](PREREG_M11_IMPLICATION.md), [M10_results.md](M10_results.md), [00_RESULTS.md](00_RESULTS.md)'
---

# M11 — the Company implication intervention

**Results for [PREREG_M11](PREREG_M11_IMPLICATION.md), frozen 2026-10-08 before
the first run of either arm.** Deucalion, rev `7a39c9d`, `qwen3.8:27b`, seed 42,
n=1 per cell. Runs `run_m11_{c2,c3}_{ctrl,concrete}`, jobs 1991408–1991416.

---

## Verdict: **REFUTED**

Q1 — the primary prediction — did not fire. The intervention did not make the
`Company implication` column carry more company signal; it left it where it was,
if anything marginally lower. The two predictions that guarded against harm both
held, and delivery actually improved.

## The numbers

| | ctrl | concrete |
|---|---|---|
| **implication** cross-company − placebo | **+0.042** | **+0.031** |
| goal cross-company − placebo | +0.507 | +0.471 |
| Adjustment modal-string share | 97% (7 distinct) | 96% (9 distinct) |
| sub-domains carried, C2 / C3 | 36 / 34 | **37 / 36** |
| `check_grounded` fabrications, C2 / C3 | 0 / 1 | 0 / 1 |

| # | Prediction | Outcome |
|---|---|---|
| **Q1** | implication divergence ≥ +0.10 on ≥1 case | **DID NOT FIRE** (+0.031 against its own control's +0.042) |
| **Q2** | modal-string share < 0.80 on ≥1 case | **DID NOT FIRE** (96% vs 97%) |
| **Q3** | concrete carries no fewer sub-domains | **HOLDS** — carried **more** on both cases (+1 C2, +2 C3) |
| **Q4** | no more fabrications than ctrl | **HOLDS** — identical (0 C2, 1 C3) |

## What it says

**Q4 is the finding that matters most, and it is a relief.** The obvious risk of
a clause that says *name a checkable artefact from the fact sheet* is that it
invents one. It did not: fabrication counts are identical, 0 on C2 and 1 on C3
in both arms. The escape clause the prereg insisted on — *if no artefact is
touched, write that it is not* — appears verbatim in all four concrete prompts
and did not become a loophole the model exploited to empty the column further.

**The intervention simply does not work, and Q3 says it is not the column's
fault for being unwritable.** The model delivered two more sub-domains with the
concrete clause than without it. It read the clause, complied with it, and the
company-signal measurement did not move.

Taken with M10, the picture is now consistent and specific:

- the `Adjusted goal` column carries the company strongly — **+0.507** here,
  **+0.188** on the M07 mixture;
- the `Company implication` carries almost none — **+0.042** as shipped,
  **+0.031** after being told to name an artefact;
- the `unchanged` badge sits at 96–97% either way, and M10 established the
  classifier is sound.

So the badge is reporting an **accurate** observation about a column that
genuinely has little company-specific content, and telling the model to try
harder did not change the content. That points away from the prompt and at one
of two things, neither of which this matrix tested: either the company signal
is already fully carried by the goal column and the implication is *meant* to be
a short gloss that restates it, in which case M10's "+0.002" is a measurement of
the wrong thing; or the implication is supposed to carry signal and the clause
is the wrong lever.

## A mis-specified threshold, recorded

Q1's +0.10 was anchored in §4 to M07's measured **+0.002**. That baseline was
computed across **six models**; this matrix is **one model** writing under a
newer instrument, and its own control reads **+0.042**. So the prereg's absolute
threshold was anchored to a number that is not comparable to the arm it gates.

**The verdict does not depend on this.** Q1 asks whether the treatment reaches
+0.10, and it did not; and the treatment also failed to beat *its own control*
(+0.031 vs +0.042). Both readings say the same thing. But the threshold's basis
was wrong, and per AGENTS.md §-2.2 a threshold without a declared basis cannot be
cited as quality evidence — it is recorded here rather than quietly used.

## A watcher false alarm, recorded

`watch_m11.sh` reported `FAIL — concrete arm still carries the shipped clause —
override did not land` on both cases. **The override did land**, verified against
the prompt bytes of all four runs: the shipped clause is present in both controls
and absent in both concrete runs, and the escape clause is present in both
concrete runs.

The watcher's discriminator was the phrase `Company implication = what this duty
concretely means for THIS company` — which is a prefix of *both* clauses, so it
matched the treatment too. The right suspicion for the wrong reason. Fixed to
discriminate on `explaining operational impact, roles and scope`, which is
present only in the shipped clause.

This is the third time this machinery has caught something, and the first time
it caught itself. That is the argument for keeping it.

## What this does not show

- **n=1, one model, one seed.** The primary metric is a median over ~90 cross
  pairs, less noisy than the delivery counts but still one run per arm.
- **Similarity is lexical**, so a divergence undercount is possible. That biases
  against the intervention passing — the test was harder than it looks, and it
  still failed.
- **The cross-company pair varies more than company identity** (jurisdiction,
  regulation set, case framing). A rise would have shown company-*specific*,
  not company-*identity*-specific.
- **Nothing here says whether the goal text is good.** Both matrices measure
  divergence, not quality. The blind L2 rubric (`PLANO_FECHO.md` §4.1) is still
  pending and still the only thing that can answer that.

## Decision

**The `concrete` variant does not ship.** Q1 did not fire, and §6 is explicit
that a failure of the primary prediction is a refutation regardless of the
safety predictions.

**The next cell is not another prompt clause.** Two prompt interventions on this
column have now failed to move it (M09 removed the exemplars; M11 demanded a
named artefact). The remaining hypotheses are structural, and none of them is a
prompt experiment:

1. **Does the implication need to carry signal at all?** If the goal column
   already does the work, M10's "+0.002" may be measuring a column that was
   never meant to vary. That is a specification question, not a measurement one,
   and it is the researcher's to answer.
2. **Is the implication being measured on the right text?** It is one sentence
   by contract. A lexical comparison of one sentence against a 38-sub-domain
   placebo may simply lack the resolution to see specificity that is present.
3. **Finish the L2 rubric.** Two matrices have now measured proxies. The
   question they keep dancing around — are these rows faithful restatements or
   theatre — has a method written and no raters.