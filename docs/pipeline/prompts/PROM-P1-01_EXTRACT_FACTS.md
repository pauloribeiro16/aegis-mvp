---
ficha_id: PROM-P1-01
title: 'Extract Company Facts'
phase_step: 'Phase 1 · P1 (SPEC §5)'
pattern: 'single structured call'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §4 (input contract), §5 P1, §7 R6'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-01 — Extract Company Facts

## Metadata

| Field | Content |
|---|---|
| Role | Compliance requirements analyst; extracts only what is written |
| Mission | Build the internal fact sheet that every later Phase 1 step consumes |
| Inputs | `input/<company>/company_input.md` (5 sections) |
| Output | Fact sheet (schema below), written to `output/<company>/packs/pack-p2.md` head |
| Human gate | **G-P1-A** — reviewer confirms the fact sheet is faithful and complete |
| Failure mode | Stop condition (see Failure handling) |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `input/<company>/company_input.md` | primary and only factual source |
| 2 | `templates/company_input.md` | section definitions and filling rules |

## Output schema

```yaml
company: <name>
sector: <text>
size_employees: <N>
jurisdictions: [<list>]
legal_form: <text>
product_summary: <2-5 sentences, verbatim-faithful>
develops_software: <true|false|unclear>   # decides CRA scope later
data_categories: [<list>]
data_subjects: [<list>]
sensitive_data: [<list>]                   # health, payment, minors...
data_scale: <rough figure as stated>
hosting: <in-house | managed cloud | mixed, as stated>
access_model: <as stated>
third_party_processing: [<list>]
assumed_regulations: [<REG, justification as written in §5>]
open_questions: [<field, what is missing>]
```

## Prompt body

> You are a compliance requirements analyst. Read `input/<company>/company_input.md` — sections §1 Company Profile, §2 Product/Service, §3 Data Handled, §4 Operational & Service Model — and produce the fact sheet exactly in the schema above.
>
> Rules:
> 1. Extract only what the text states. Do not infer, complete, or interpret (rule R6).
> 2. `develops_software` must be answered strictly from §2's statement of whether the company develops or only uses software; if §2 does not say, write `unclear` and add it to `open_questions`.
> 3. Copy §5 Regulations Assumed verbatim into `assumed_regulations` — list them, do not judge them (judging happens in the next step).
> 4. If any of §1–§4 is empty or unusable, STOP and report which section is empty — the input contract requires the executor to stop (SPEC §4). Do not fill gaps.
> 5. Every value that is not literally in the input becomes an `open_questions` entry, never a guess.

## Self-checks (L2)

- Every field traces to a specific input line (spot-check 3 fields at random and cite them).
- No field contains interpretation beyond the input's own words.
- `assumed_regulations` matches §5 exactly (count and identifiers).
- `open_questions` non-empty iff something is genuinely missing.

## Guard hooks (L0/L1)

- SPEC §8 item 1 (5 sections present; §5 ≥1 regulation with justification) is verifiable from this step's inputs.
- Fact sheet format is parseable — later fichas reference fields by name.

## Failure handling

- Empty/unusable section → stop, report to the human, request a corrected `company_input.md`.
- Ambiguous statement → copy verbatim + `open_questions` entry; flag-not-drop.

## Human gate

**G-P1-A:** present the fact sheet; the reviewer confirms or corrects per field. Corrections are applied to the fact sheet (the input file is never edited by the pipeline).
