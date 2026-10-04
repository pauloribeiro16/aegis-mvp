---
ficha_id: PROM-P1-07
title: 'Resolve Strategic Tensions'
phase_step: 'Phase 1 · P4t (after P4; multi-regulation runs only)'
pattern: 'single structured call per run'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P4 (cross/ aggregation), §7 R5, R8'
  - 'cases/*/01_PHASE1_CONTEXT/Doc02_Adjusted_Goals.md §4 (T-NNN format, max-SLA routing precedent)'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-07 — Resolve Strategic Tensions

## Metadata

| Field | Content |
|---|---|
| Role | Regulatory interaction analyst |
| Mission | For each corpus tension among the confirmed regulations, record the operational conflict and adopt the binding resolution rule for this company |
| Inputs | Selected sub-domains (G-P1-C); fact sheet; corpus `cross/_interactions.md` Emergent-tensions sections |
| Output | `steps/tensions.json` + `tensions.md` — the §4 Tensions Resolved block of the deliverable |
| Human gate | **G-P1-D** — resolutions reviewed with the rendered document |
| Failure mode | A corpus tension that activates but gets no resolution → L0 failure; never silently dropped |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `pack-p4t/tensions.md` | deterministic extraction of the Emergent-tensions sections of every selected sub-domain's `cross/_interactions.md` |
| 2 | `steps/fact_sheet.yaml` | company facts grounding the resolutions |

## Output schema

```markdown
| ID | Sub-domains | Tension | Conflict | Resolution |
|---|---|---|---|---|
| T-001 | D-04.3 | <tension title> | <the operational conflict> | <the binding rule adopted> |
```

…or the single line `None.` when no corpus tension activates on the confirmed regulation pairing.

## Prompt body

> You are a regulatory interaction analyst. The pack lists the corpus's
> Emergent-tensions sections for the selected sub-domains under the confirmed
> regulations (R8). For each tension that activates on this company:
>
> 1. Name it concisely and state the operational conflict in one sentence —
>    which duties collide and on what operational dimension (clock, recipient,
>    scope, competence).
> 2. Adopt the binding resolution rule for this company — one auditable
>    sentence (e.g. "strictest timeline binds per recipient; parallel
>    recipients keep their own clocks" — the max-SLA routing convention).
> 3. Skip tensions whose triggering condition does not hold for this company
>    (e.g. a 5-regulation divergence when 2 are confirmed) — they are not
>    silent drops, they do not activate.
>
> Rules:
> 1. IDs sequential `T-001…`; Sub-domains column cites canonical `D-XX.Y` ids (R1).
> 2. Technology-neutral wording (R5); no obligation invented beyond the corpus tensions (R8).
> 3. Every resolution is company-proportional and traceable to the fact sheet (R3, R6).

## Self-checks (L2)

- Every activating corpus tension has a row; non-activating ones are excluded by stated condition, not silently.
- Every resolution names a binding rule (not "TBD").
- Technology-neutral; canonical IDs only.

## Guard hooks (L0/L1)

- L0: 5-column contract, sequential T-NNN, non-empty Tension/Conflict/Resolution — or `None.`.
- L1 (`validate.py`): §4 present with resolutions on multi-regulation runs.

## Failure handling

- No LLM call on single-regulation runs (stage writes `tensions.json` with an empty list deterministically).

## Human gate

Reviewed inside **G-P1-D** — each resolution is a company decision record.
