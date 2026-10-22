# Labelling sheet — LAB03 (d1 decision models)

Two families of case in this lane cannot be labelled by a machine, because the
label is a **judgement** and not a derivation. Everything else already has a
label that comes from the corpus or from a deterministic pipeline artefact.

Fill in the right-hand column, then re-run `check_suite.py` with the labels
applied (see §4). It takes minutes, not hours: the prior study of a hosted
System-1 API failed on exactly this step, so the step is kept short.

---

## 1. Tension activation — the two judgement cases

The corpus declares each tension's activation condition. For five of the ten
tensions the condition is a clean boolean and the label follows. For these
two it does not, because the condition and the negation are entangled.

The pipeline's own resolution for T-003 says: *"The tension does not activate
for this company because the fact sheet confirms zero AI/ML systems … and the
product is in the default class with self-assessment conformity … therefore,
no binding resolution rule is adopted as the triggering condition … is not
met."* — but it still emitted a **row** for it, where the p4t contract says to
skip the tension entirely.

| case | corpus condition (abridged) | pipeline's row | **your label: activates?** | note |
|---|---|---|---|---|
| `domain.tension.t-003` | engages only when a CRA update log or an AI log contains personal data, or a single data flow crosses regime boundaries | row present, resolution says "does not activate" | ☐ yes ☐ no | |
| `domain.tension.t-004` | a non-EU provider or manufacturer may simultaneously require a GDPR Union representative, a CRA authorised representative, NIS 2 cross-MS routing and DORA audit/access rights | row present, resolution says "does not activate" | ☐ yes ☐ no | |

The other three (`t-001`, `t-002`, `t-005`) are pre-labelled in
`cases_domain.json` from the corpus condition; their warrants are in each
case's `provenance` field.

## 2. Adjustment classification — needs the L2 rubric

The pipeline's own instrument for this is the *adjustment badge*, and the
prior study of it (M07/M09) measured a **0.99 ratio of `unchanged`** — a
collapse, not a measurement. The honest adjudicator for "is this adjusted
goal a proportional restatement or a copy?" has never existed. The rubric
below is the missing instrument; if it is worth having, it is worth writing.

Three pairs are staged. For each, the baseline and the adjusted goal are
quoted verbatim in the case state.

| case | pair | your label | your note |
|---|---|---|---|
| `domain.adjustment.verbatim_d10_1_cra` | AG-D-10.1-002 (CRA) | ☐ verbatim ☐ proportional ☐ narrowed | |
| `domain.adjustment.proportional_d10_1_gdpr` | AG-D-10.1-001 (GDPR) | ☐ verbatim ☐ proportional ☐ narrowed | |
| `domain.adjustment.narrowed_d02_2_cra` | AG-D-02.2-002 (CRA) | ☐ verbatim ☐ proportional ☐ narrowed | |

**Proposed rubric** (for the three above; the instrument, not the labels):

- **verbatim** — the adjusted goal asserts the same obligations as the
  baseline, with no leg added, dropped, moved or narrowed. Paraphrase,
  pronoun swap and article citation are not differences.
- **proportional** — the same obligations, restated at a scale the company
  can actually operate, with every leg still present in the goal text.
- **narrowed** — at least one mandatory leg of the baseline is absent from
  the goal text, whether or not it survives in an `Adjustment` or `Articles`
  column.

Note what this rubric cannot settle, and say so if it matters: whether a leg
demoted to the `Adjustment` column is still *discharged*. `AG-D-02.2-002`
keeps the Art. 13(8)/(9) legs out of the goal text while citing them in
`Articles` — that is a narrowing under this rubric, and the question of
whether it is a *legitimate* one is a Phase-1 conformance question, not a
labelling question.

## 3. Contested sub-domains — declared, not labelled

Three sub-domains are in dispute between two of the project's own artefacts:
the pipeline run selected all 38 candidates, while the hand-written Case_01
deliverable lists 35 active and names `D-02.4`, `D-06.4` and `D-08.3` as not
addressed.

The suite carries these three as `contested`: they are measured and reported,
and they never enter the accuracy figure. If you want them scored, the
adjudication is a question about which artefact is authoritative for Phase 1
selection — a pipeline question, not a labelling one.

## 4. Applying the labels

The labels live next to the cases, in the case file, so the checker picks them
up without a second mechanism:

```bash
# 1. write the label into the case's expect block
#    "expect": {..., "labels": {"activates": false}}
#
# 2. re-score the existing records — no model calls needed
python3 lab/decision/check_suite.py results/A2_cases_protocol.jsonl \
    --out results/summary.json
```

The checker reads the labels from the **records**, so the labels have to be
present when the suite runs. To score already-collected records against new
labels, edit the case file and re-run the checker with `--labels-from
<case file>`; the case file's `expect.labels` wins over the record's.
