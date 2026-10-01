---
ficha_id: PROM-P1-06
title: 'Build §4 Framing'
phase_step: 'Phase 1 · between P2 and P4 (pipeline-layer step)'
pattern: 'single structured call'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'templates/phase1_output.md §4 (framing blockquote contract)'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-06 — Build §4 Framing

## Metadata

| Field | Content |
|---|---|
| Role | Compliance context writer |
| Mission | Write the single §4 Framing blockquote that conditions every Adjusted Goal of the run |
| Inputs | P1 fact sheet; P2 verdict table; template §4 framing contract |
| Output | One blockquote (`> ...`), max 8 lines, saved to `steps/framing.md` and attached to every P4 pack |
| Human gate | none (reviewed within G-P1-C/G-P1-D) |
| Failure mode | Stop condition if the fact sheet lacks size/roles fields |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `steps/fact_sheet.yaml` | size, sector, roles, hosting, exclusions |
| 2 | `steps/verdicts.md` | confirmed regulations for the roles line |
| 3 | `templates/phase1_output.md` §4 (framing contract) | the exact content the blockquote must carry |

## Output schema

One markdown blockquote: company size consequence; area of operation;
regulatory roles (controller, processor, manufacturer, ...); inherited or
managed capabilities; explicit exclusions. No per-goal content — that stays in
the goal rows.

## Prompt body

> You are a compliance context writer. Using the fact sheet and the confirmed
> regulation verdicts, write the §4 Framing blockquote exactly per the
> template's framing contract: company size + tier consequence; area of
> operation; regulatory roles; inherited/managed capabilities; explicit
> exclusions.
>
> Rules:
> 1. Every statement traces to the fact sheet or the verdict table (R6).
> 2. Technology-neutral wording (R5); proportionality wording only (R3).
> 3. One blockquote, max 8 lines; no per-goal repetition.

## Self-checks (L2)

- Every line traces to fact-sheet fields or verdicts.
- No tools/vendors; no goal content.

## Guard hooks (L0/L1)

- Output is a single blockquote; parsed and stored as `steps/framing.md`.

## Failure handling

- Missing size/roles fields → stop, report; the fact sheet gate (G-P1-A)
  should have caught it.

## Human gate

Reviewed inside G-P1-C (subset) and G-P1-D (final sign-off) — the framing
precedes every goal table in the rendered document.
