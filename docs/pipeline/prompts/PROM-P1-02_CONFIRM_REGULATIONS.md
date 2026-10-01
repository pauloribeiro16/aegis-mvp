---
ficha_id: PROM-P1-02
title: 'Confirm Applicable Regulations'
phase_step: 'Phase 1 · P2 (SPEC §5)'
pattern: 'routing (one scope test per regulation)'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P2, §7 R8'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-02 — Confirm Applicable Regulations

## Metadata

| Field | Content |
|---|---|
| Role | Regulatory scope analyst |
| Mission | Decide, for each of the 5 candidate regulations, applies / does not apply / flagged — grounded in the fact sheet |
| Inputs | P1 fact sheet (approved at G-P1-A); input §5 assumptions |
| Output | §2 verdict table (5 rows, pre-seeded IDs) |
| Human gate | **G-P1-B** — reviewer confirms or corrects each verdict |
| Failure mode | Assumed-but-failing regulation → `flagged`, never dropped |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `output/<company>/packs/pack-p2.md` | fact sheet (P1 output) |
| 2 | `input/<company>/company_input.md` §5 | assumed regulations + justifications |
| 3 | `templates/phase1_output.md` §2 | verdict table format |

Scope criteria are embedded below (from SPEC §5 P2) — no corpus files are needed at this step.

## Output schema

| Regulation | Verdict | Rationale |
|---|---|---|
| GDPR | `**applies**` / `does not apply` / `flagged` | one line, citing fact-sheet fields |
| CRA | … | … |
| NIS2 | … | … |
| DORA | … | … |
| AI_Act | … | … |

## Prompt body

> You are a regulatory scope analyst. Using the fact sheet, evaluate each of the five candidate regulations against its scope test and produce the §2 verdict table.
>
> Scope tests:
> - **GDPR** — applies when the company is established in a jurisdiction covered by the input and processes personal data (establishment + processing).
> - **CRA** — applies when the company develops or supplies products with digital elements that are placed on the market; use `develops_software` from the fact sheet. A company that only uses software does not, by that fact alone, place products with digital elements on the market.
> - **NIS2** — applies when the company falls in an essential/important entity sector and meets the size threshold; state sector and size explicitly.
> - **DORA** — applies to financial entities; check the sector field.
> - **AI_Act** — applies when the company places AI systems on the market or deploys high-risk AI systems; an ordinary product without AI functionality does not trigger it.
>
> Rules:
> 1. Every rationale cites the fact-sheet field(s) it rests on.
> 2. Every regulation listed in input §5 must appear in the table. If an assumed regulation fails its scope test, verdict = `flagged` with the failing criterion — it is flagged, never silently dropped.
> 3. Do not derive any obligation here; this step only decides scope (R8).
> 4. If a scope test cannot be decided from the fact sheet, verdict = `flagged` + `open question`, never a guess.

## Self-checks (L2)

- Table has exactly 5 rows with the canonical regulation IDs.
- Every input §5 entry is present (count match).
- Every `applies` verdict's rationale names at least one fact-sheet field.
- No obligation language leaked into §2 (scope only).

## Guard hooks (L0/L1)

- SPEC §8 item 2 (coverage, none silently missing).
- Verdicts feed the P3 pre-filter — canonical spelling of regulation IDs is required downstream.

## Failure handling

- Un-decidable scope → `flagged` + open question; resolve at G-P1-B (reviewer may correct the input file's §5 with a justification).

## Human gate

**G-P1-B:** present the 5 verdicts; reviewer confirms/corrects each. Confirmed verdicts become the regulation set for the rest of the pipeline.
