---
document_id: AEGIS-MVP-ADR-013
title: 'Phase 2 objective bridge — the RULE-* tail is not emitted, and where Phase 2 earns its keep'
status: 'ACCEPTED — decided by the researcher, 2026-10-09'
date: 2026-10-09
phase: 'Fase 2 (Operationalization)'
author: 'Decision: PhD researcher; formalization + record: Executor session'
upstream: 'ADR-004 §1; docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §1, §3.2, §3.3, §4.1, §6'
---

# ADR-013 — Phase 2 objective bridge (the `RULE-*` tail)

> Registered decision (2026-10-09), stated by the researcher, on reading
> `docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md` §4.1: the `RULE-*` tail is
> **not emitted** in Doc01 v0.1; it is de-scoped with a signpost, not left as an
> undocumented seam. The three unseamed Doc01 columns are resolved by offline
> measurement before any code claims them. Doc01 keeps the 9-column case schema.

---

## 1. The decision

**D1 — No `RULE-*` tail in Doc01 v0.1.** The Phase 2 catalogue emits
`PO-/SO-D-XX.Y-NNN` operational objectives and nothing else. The
objective→testable-rule bridge that ADR-004 §1 assigns to Phase 2 is **not**
emitted until a RULE row schema exists.

**D2 — Doc01's generative work is Doc02's per-case constraint.** The ledger
measured which cells actually carry company-specific content, and §3.3 names the
answer: `PRIN-ENG-06` and `PRIN-ENG-07` are the two principles whose
definition text differs across three unrelated companies, because they name the
company's own data-projection and erasure surfaces. That difference — a
principle bound to *this* architecture rather than restated from the baseline —
is the shape a real Phase 2 column has, and it is what the Doc02 generation step
produces.

**D3 — Unseamed columns are resolved by measurement, never by prompt.** For
`Verification Criteria`, `Method` and `Responsible Owner`, a candidate
derivation rule is tested offline against the three hand-authored case
deliverables *before* any code claims the column. A column is promoted from `—`
only by a rule that reproduces; a column that no rule reproduces **stays `—`**
and the non-reproduction is recorded as a result (AGENTS.md §-2 rule 4). No
column is ever backfilled with plausible filler.

**D4 — Doc01 keeps the 9-column case schema.** Un-derivable cells render as `—`.
The column order is load-bearing: `scripts/check_traceability.py` T6 reads the
published anchor set from column 8 of the Phase 2 matrix, so narrowing the table
would silently break an existing check.

## 2. Why

The ledger's §1 findings, all measured by `scripts/phase2_ledger_scan.py`:

1. **`Operational Statement` is a byte-for-byte transcript of Phase 1's
   `Adjusted Goal`.** Multiset md5 `bc33181d` (Case 01) and `3474612a` (Case 02)
   match on both sides. The column carrying the phase's semantic payload carries
   the *previous* phase's payload.
2. **The `RULE-*` tail has 0 occurrences across 6 hand-authored Phase 2
   documents.** Three deliverables, written by the same executor, under the same
   conventions, agree on omitting it.
3. **§3.2 locates the one genuinely generative cell.** Of Doc02's columns, the
   `Definition` is a baseline asset (identical across cases for 5 of 7
   principles), while `Constraint` is where the cases diverge. Reading a
   company's architecture off its intake is an LLM job; everything else is
   lookup.

**Why not emit the tail anyway.** ADR-004 assigns it to Phase 2, and that
assignment stands — this ADR defers it, it does not delete it. But emitting it
requires a RULE row's columns, its anchor derivation, and its verification
method, and **no artefact in the corpus defines any of the three**. Writing that
schema inside a pipeline would promote an executor's invention to frozen
methodology, and Phase 3 already owns the layer where a testable rule becomes a
requirement (`REQ-`/`ORG-`, ADR-006/ADR-008). The tail's absence across three
independent hand-authorings is evidence that the shape is genuinely undetermined,
not evidence that a fourth author can invent it safely.

**Why the "no rule found" columns are not simply filled.** The ledger is careful
that "no rule found" ≠ "non-derivable" — three cases show a rule was *not
followed*, not that no rule exists. That is an argument for measuring, not for
guessing. It also records (§3.1, R10b challenge) that the mechanically
generated `Verification Criteria` "would read identically for a completely
different company" — compliance theater that happens to be machine-produced.
Generating it at scale would reproduce the finding the ledger documents.

**Why `owner` is the hard case.** D3's scan will test the only plausible
candidate — each case's own §13 Governance & Stakeholder Matrix. But note the
data that would make it work is **not** in the pipeline: `fact_sheet.yaml` has
no governance, role, or tier field. Phase 1's P1 schema requires 12 fields
(`pipeline/src/steps.py:163`) and not one of them is a person, a role, or a
tier; the only proxy is `size_employees`. Extending the Phase 1 schema would
re-open EXP-01..05 and needs its own prereg, so it is out of scope here
(ASSUMPTIONS A9).

## 3. The D3 measurement (run 2026-10-09, `scripts/phase2_rule_discovery.py`)

Four candidate rules, tested against all three hand-authored deliverables
(objective counts 62 / 100 / 134 — matching the ledger). **Nothing ships; all
three columns stay `—`.**

| Rule | Column | Best in-sample | Leave-one-case-out | Verdict |
|---|---|---|---|---|
| `R-METHOD-1` method ← first control-anchor family | Method | 0.66 / 0.60 / 0.67 | 0.57 / 0.60 / 0.63 | stays `—` |
| `R-METHOD-2` method ← regulation | Method | 0.57 / **0.82** / 0.55 | 0.57 / 0.58 / 0.52 | stays `—` |
| `R-OWNER-1` owner ← case §13 governance matrix | Owner | 0.82 / 0.65 / 0.72 (lead + a support) | — | stays `—` |
| `R-CRITERIA-1` criteria ← (regulation, anchor) | Criteria | see below | — | stays `—` |

**The regulation→method rule is the instructive one.** It scores **0.82 on
Case 02 — above the 0.80 threshold — and 0.55/0.57 on the other two.** Had the
rule been "the best candidate", or had it been measured on the case that was
handy, it would have shipped and been wrong on two of three companies. This is
the concrete form of the ledger §2 caveat that three cases show a rule was
*followed*, not that one exists.

**Criteria is confirmed as a template, and the ledger's R10b challenge is now a
number.** Distinct criteria values collapse under sub-domain-slug normalisation:

| Case | rows | distinct (raw) | distinct (slug-normalised) |
|---|---|---|---|
| Case 01 | 62 | 62 | 19 |
| Case 02 | 100 | 100 | **4** |
| Case 03 | 134 | 134 | **5** |

The surviving forms are, verbatim, *"automated check or audit confirms `<slug>`
is enforced for all personal data flows"* and *"security verification confirms
`<slug>` is enforced across product components and release artefacts"* — one
sentence per regulation with the sub-domain name substituted. Unique on every
row, identical for every company. That is precisely the invariance failure the
ledger named, measured rather than asserted, and it is why the column is not
derived: deriving it would ship the theater at scale.

**Owner is reproducible but not derivable, and the three deliverables do not
agree on its granularity.** Cases 01 and 02 ship a §13 matrix keyed on
**sub-domains**; Case 03 ships a 3-column matrix keyed on **domains**
(`(D-01, D-05)`), with one row (*"AI governance (OmniScore, AI Act rows)"*)
carrying no canonical id at all. Even given the matrix, the owner is not a
deterministic function of it: "lead plus **all** supports" reproduces only
65.6% / 10% / 10.6% of rows — the authors picked *some* supporting roles per
row, a judgement no rule reproduces. And the matrix is per-case human input that
`fact_sheet.yaml` does not carry (§2). Recorded as ledger defect §4.9.

## 4. Consequence, falsifiable

**C1.** Doc01 v0.1 emits `N` objectives where `N` equals the Phase 1 goal count
for the run — one objective per adjusted goal, no drops, no additions (gate G4
in `pipeline/src/phase2.py` asserts this bidirectionally). *Falsifier: any row
whose `parent_goal` is not an `AG-` id of the same run, or any `AG-` id of the
same run with no `PO-`/`SO-` row.*

**C2.** Every control anchor resolves to a file under `baseline/CONTROLS/`.
Anchors are re-derived via `controls.goal_anchors()`, never copied from Phase 1
— reading them back would make the check circular. *Falsifier: any anchor that
does not resolve to a real file (R2b).*

**C3.** The Doc02 constraint passes the invariance test — it would **not** read
identically for a company of a different architecture. Measured as
`grounding_ratio` (share of constraints containing company-specific content
absent from the universal definitions) and recorded in the run's stage result.
*Falsifier: the constraint column carrying Case 02's architecture into Case 03,
the contamination the ledger records at §4.6.*

C3 is **measured, not gated**, deliberately. M11 established that demanding a
named artefact from the fact sheet does not make a column more company-specific
(+0.031 against its own control's +0.042); turning that into a hard gate would
reject a 7-row document into uselessness while teaching nothing. The falsifier
is registered as a prediction in `PREREG_P2_01.md`, where a failed prediction is
a result.

## 5. Signpost — when this decision reopens

Per AGENTS.md §-2 rule 5 and the RAND Assumption-Based Planning pattern
(MR-114), a signpost firing means the decision is *revisited, never silently
defended*. Any one of these reopens D1:

- A RULE row schema is defined anywhere in the methodology (columns, anchor
  derivation, verification method) — the decision was taken because none
  existed.
- Phase 3 declares it cannot cite a rule-level artefact, i.e. the
  objective→requirement step needs an intermediate the pipeline does not emit.
- The ledger's §3.3 pattern turns out not to generalise: a Doc02 constraint
  generated for a fourth, structurally different company comes out generic.

Registered as **A9** in `docs/decisions/ASSUMPTIONS.md`.

## 6. What this decision does not settle

- It does **not** retire the case deliverables as id goldens (ledger §5.1
  records that their slot numbering disagrees with the pipeline's; the pipeline
  convention is in force and the deliverables are valid for content, invalid for
  ids). Retiring them is still open.
- It does **not** repair the ledger's §4.2/§4.4/§4.6/§4.7 defects in the
  hand-authored case documents. Those are frozen reference artefacts; the
  pipeline's own gates catch the same classes on generated output.
- It does **not** extend the Phase 1 fact sheet. `owner` stays derived from
  what exists or stays `—`.
- It does **not** claim Phase 2 is complete. It fixes what Phase 2 is *for*, so
  the remaining columns can be measured rather than invented.

## 7. Linked evidence

| Claim | Source |
|---|---|
| `Operational Statement` is byte-identical to Phase 1's `Adjusted Goal` | ledger §1 finding 1; `scripts/phase2_ledger_scan.py` (md5 `bc33181d` C01, `3474612a` C02) |
| `RULE-*` has 0 occurrences in 6 documents | ledger §1 finding 2; ledger §3.1 tail row ("Absent") |
| `Constraint` is the genuine Phase 2 work | ledger §3.2, §3.3 (`PRIN-ENG-06` DTOs vs data views; `PRIN-ENG-07` three data-store enumerations) |
| `Definition` is a baseline asset to be copied, not regenerated | ledger §3.2; settled here by D2 — the definitions live in the `PROM-P2-03` ficha, not in `baseline/` (AGENTS.md §3 keeps the baseline read-only) |
| `Verification Criteria` is compliance theater | ledger §3.1, R10b challenge |
| Phase 2 has no pipeline stage, prompt, or ficha | ledger §6 — recorded scope fence, discharged by this ADR's implementation |
| Fact sheet carries no governance, roles, or tier | `pipeline/src/steps.py:163` (P1 schema, 12 required fields); observed `steps/fact_sheet.yaml` in the M08/M11 runs |