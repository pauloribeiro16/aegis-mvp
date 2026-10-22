---
document_id: AEGIS-MVP-ADR-015
title: 'The RULE-* tail stays — Phase 3 cites the rule it discharges, and the chain is checked'
status: 'ACCEPTED — decided by the researcher, 2026-10-22'
date: 2026-10-22
phase: 'Fase 2 (Operationalization) → Fase 3 Parte 1'
author: 'Decision: PhD researcher; formalization + record: Executor session'
upstream: 'ADR-013 D1 (superseded); ADR-004 §1; docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md §4.1; docs/decisions/ASSUMPTIONS.md A9'
---

# ADR-015 — The `RULE-*` tail stays, and Phase 3 cites it

> Registered decision (2026-10-22), stated by the researcher, on reading the
> adversarial review of the pipeline: the `RULE-*` tail is **kept** in Doc01 and
> **given a consumer**. ADR-013 D1 (which de-scoped it) is superseded. The
> reason is not that the tail became valuable on its own — it is that it now
> carries the one thing the human acceptance round could not otherwise verify:
> which testable rule a proposal discharges.

---

## 1. The decision

**D1 — The `RULE-*` tail stays in Doc01, and ADR-013 D1 is superseded.**
The tail is emitted and rendered as before. What changes is that it stops
being an orphan: it becomes the unit the Phase 3 acceptance round verifies.

**D2 — The rule catalogue is the Phase 2 store, not the rendered markdown.**
`steps/phase2/*.json` holds each rule with its parent objective recoverable
from the `objectives[].rules[]` nesting. The rendered Doc01 loses that
nesting — the parent is injected at render time — so anything that needs the
parent reads the store. The rendered tail remains the human-readable
surface; the store is the machine surface.

**D3 — A proposal declares which rule it discharges.** The proposal block
gains an optional `**Rules discharged:**` field. When the field is present,
every id must belong to **that objective's** rules; a rule of another
objective, or a rule that does not exist, is a fabrication and the proposal
call fails its L0 repair. The field is optional because an objective may carry
no Phase 2 rule.

**D4 — The rule catalogue reaches the model.** The verdict pack — the single
pack builder behind both the coverage-mapping call and the proposal call —
carries each objective's rules next to its published anchors. A model asked to
discharge a rule can only name one it was shown.

**D5 — The chain is checked for real, over the run.** `scripts/check_traceability.py`
gains a `--run-dir` mode and a T1 arm for rule ids, and the exit gate now runs
it over the run it is judging. R12b already said the chains must be
re-anchored "before any coverage verdict is credible"; the gate's own
docstring already claimed it ran T1–T6. Both are now true.

**D6 — A referential finding blocks CONCLUDED.** Not a warning in the report:
the gate does not certify a chain it cannot vouch for.

## 2. Why the decision changed

ADR-013 D1 de-scoped the tail because "no artefact of the corpus defines the
RULE line" and because, at the time, nothing read it. The second half of that
was true and stayed true: the tail was emitted by the P2-ENRICH experiment
without a superseding decision, and **704 rules in the last run had zero
readers**. Phase 3 loaded the Phase 2 document through a 9-cell row filter
keyed on `PO-/SO-` ids; RULE rows have 4 cells and were structurally
invisible.

What changed is the first half. The line now has a schema — four columns, a
rule id allocated in code, a SHALL/MUST form check, a technology-neutrality
check — and the consumer is a *verification* the pipeline could not otherwise
perform: the acceptance round decides per item, and a proposal that names the
rule it discharges lets that decision be checked mechanically instead of
trusted.

The alternative — cutting the tail to conform to ADR-013 D1 — would have
removed the only artefact Phase 2 produces that Phase 1 does not, and left the
acceptance round as a judgement with nothing behind it.

## 3. What this decision does not settle

- **The `criteria`, `method` and `owner` columns stay `—`.** ADR-013 D3
  resolved them by measurement, and the measurement found no rule that
  reproduces them. Nothing here reopens that.
- **The `RULE-*` id space is not the one reserved for the good-practice
  layer.** `docs/decisions/ADR-2026-09-22_best-practice-layer.md` reserves
  `RULE-D-XX.X-NNN` for framework-derived rows at +100; the Phase 2 counter
  restarts at 001 per sub-domain. The collision is latent, not live, and is
  recorded here rather than fixed: the good-practice layer is not built.
- **The Phase 3 Part 2 threat dossier does not cite rules yet.** The Part 2
  contract is `K1 + K3 + system model`; the rule tail is a Part 1 artefact.

## 4. The signal for re-opening

The decision is reviewed, not defended, when **any** of these fires:

- **(a)** The acceptance round's verdicts are found to be reproducible from the
  rule citations alone — i.e. the round becomes a formality, which would mean
  the rules carry no more information than the constraint text.
- **(b)** A proposal is found to cite a rule that the woven card does not
  discharge, in a run where the T1 arm reports clean. That would mean the
  citation is decorative.
- **(c)** The rule ids in the tail are found to be unciteable in a Phase 3
  Part 2 context — the same signal that made ADR-013 D1 necessary in the
  first place, now aimed at the consumer rather than the tail.

## 5. The measurement this rests on

| What | Where | Value |
|---|---|---|
| The tail had no consumer | `grep -rl "RULE-" pipeline/src` | producer only; no `phase3` module |
| The tail is invisible to Phase 3 | `phase3/skeleton.py:36-59` | 9-cell filter keyed on `PO-/SO-`; RULE rows have 4 |
| The rendered tail loses the parent | `phase2/renderers.py:148-149` | `parent_obj` injected at render time only |
| The store keeps it | `steps/phase2/*.json` | `objectives[].rules[]` |
| The gate claimed T1–T6 and did not run them | `phase3/weave.py:202` (before this decision) | `check_traceability.py` rooted at `cases/`, never invoked |
| Pointed at a run, the layer finds what the gate certified | `scripts/check_traceability.py --run-dir run_p2enr_c1` | 2 × T2 (a law cited with a foreign driver), 13 × T5 (objectives the matrix declares covered that no deliverable cites) |

Related: [[phase3-gate-is-a-pure-function-of-disk]], [[phase3-part1-closed-on-cluster]],
[[gates-are-not-goals]], [[false-green-verification-is-worse-than-none]].
