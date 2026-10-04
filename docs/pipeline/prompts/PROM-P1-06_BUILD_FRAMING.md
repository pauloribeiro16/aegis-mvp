---
ficha_id: PROM-P1-06
title: 'Build §2 Framing'
phase_step: 'Phase 1 · between P2 and P4 (pipeline-layer step)'
pattern: 'single structured call'
version: 1.1.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'templates/doc02_adjusted_goals.md §2 (framing table contract)'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-06 — Build §2 Framing

> **v1.1.0 change (2026-10-01):** the deliverable is now the Doc02 case format,
> whose §2 is a **4-row table** (Size / Area of operation / Regulatory roles /
> Inherited capabilities) — the output contract changes from a blockquote to
> exactly that table.

## Metadata

| Field | Content |
|---|---|
| Role | Compliance context writer |
| Mission | Write the §2 Framing table that conditions every Adjusted Goal of the run |
| Inputs | P1 fact sheet; P2 verdict table; template §2 framing contract |
| Output | `steps/framing.md` — the 4-row table, attached to every P4 pack and rendered verbatim in the deliverable |
| Human gate | none (reviewed within G-P1-C/G-P1-D) |
| Failure mode | Stop condition if the fact sheet lacks size/roles fields |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `steps/fact_sheet.yaml` | size, sector, roles, hosting, exclusions |
| 2 | `steps/verdicts.md` | confirmed regulations for the roles row |
| 3 | `templates/doc02_adjusted_goals.md` §2 (framing contract) | the exact table the output must carry |

## Output schema

```markdown
| Dimension | Framing |
|---|---|
| Size | <size + tier consequence> |
| Area of operation | <what the company operates, for whom, where> |
| Regulatory roles | <controller / processor / manufacturer / … per confirmed regulation> |
| Inherited capabilities | <supplier-managed capabilities; explicit exclusions> |
```

## Prompt body

> You are a compliance context writer. Using the fact sheet and the confirmed
> regulation verdicts, fill the §2 Framing table exactly per the template's
> framing contract: Size (size + tier consequence), Area of operation,
> Regulatory roles (per confirmed regulation), Inherited capabilities
> (supplier-managed capabilities and explicit exclusions).
>
> Rules:
> 1. Every statement traces to the fact sheet or the verdict table (R6).
> 2. Technology-neutral wording (R5); proportionality wording only (R3).
> 3. Exactly 4 rows, 1–3 sentences per cell; no per-goal content — that stays in the goal rows.

## Self-checks (L2)

- Every cell traces to fact-sheet fields or verdicts.
- No tools/vendors; no goal content; exactly the 4 canonical dimensions.

## Guard hooks (L0/L1)

- L0: 2-column table with exactly the 4 dimensions, all cells non-empty; stored as `steps/framing.md`.

## Failure handling

- Missing size/roles fields → stop, report; the fact sheet gate (G-P1-A) should have caught it.

## Human gate

Reviewed inside G-P1-C (subset) and G-P1-D (final sign-off) — the framing
precedes every goal table in the rendered document.
