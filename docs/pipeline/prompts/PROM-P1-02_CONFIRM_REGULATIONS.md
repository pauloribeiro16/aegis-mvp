---
ficha_id: PROM-P1-02
title: 'Confirm Applicable Regulations'
phase_step: 'Phase 1 · P2 (SPEC §5)'
pattern: 'routing (one scope test per regulation)'
version: 1.1.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P2, §7 R8'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-02 — Confirm Applicable Regulations

> **v1.1.0 change (2026-10-01):** scope tests carry the concrete thresholds
> (NIS2 size classes, DORA Art. 2(1) entity list, CRA "placed on the market"
> edge for SaaS-style delivery) so verdicts never rest on the model's memory
> of parameters. Genuine edge cases become `flagged` + open question, never a
> guess.

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
| 1 | `steps/fact_sheet.yaml` | fact sheet (P1 output) |
| 2 | `input/<company>/company_input.md` §5 | assumed regulations + justifications |
| 3 | the P2 output contract (verdict table `Regulation | Verdict | Rationale`) | in this ficha |

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
> - **CRA** — applies when the company develops or supplies products with digital elements that are **placed on the market**; use `develops_software` from the fact sheet. A company that only uses software does not, by that fact alone, place products with digital elements on the market. Edge: software delivered purely as a remote service (the customer never receives the software) is a genuine CRA boundary case — if the input's delivery model does not clearly state placement on the market, verdict = `flagged` + open question; if the input §5 explicitly asserts placement as manufacturer, record `applies` citing that statement.
> - **NIS2** — applies only if BOTH a sector test and a size test pass. Size classes: medium = ≥50 employees or >€10M turnover; large = ≥250 employees or >€50M turnover (and >€43M balance sheet). Essential entity = Annex I sector + large; important entity = Annex I sector + medium, or Annex II sector + medium-or-larger. Below medium in an Annex I/II sector → `does not apply` by size (state the numbers). DNS/TLD/cloud/data-centre-type providers can be designated regardless of size → `flagged` if plausible from the input.
> - **DORA** — applies to financial entities as listed in DORA Art. 2(1) (credit institutions, payment/e-money institutions, insurance/reinsurance, investment firms, crypto-asset service providers, ICT third-party service providers serving financial entities, among others). Check the sector field and `third_party_processing`: a company providing ICT services TO financial entities may be in scope → `flagged` if plausible, `does not apply` if the sector excludes it.
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
- NIS2/DORA rationales state the size/sector numbers used.
- No obligation language leaked into §2 (scope only).

## Guard hooks (L0/L1)

- SPEC §8 item 2 (coverage, none silently missing).
- Verdicts feed the P3 pre-filter — canonical spelling of regulation IDs is required downstream.

## Failure handling

- Un-decidable scope → `flagged` + open question; resolve at G-P1-B (reviewer may correct the input file's §5 with a justification).

## Human gate

**G-P1-B:** present the 5 verdicts; reviewer confirms/corrects each. Confirmed verdicts become the regulation set for the rest of the pipeline.
