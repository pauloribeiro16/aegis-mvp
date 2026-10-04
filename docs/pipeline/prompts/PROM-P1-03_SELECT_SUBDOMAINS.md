---
ficha_id: PROM-P1-03
title: 'Select the Sub-Domain Subset'
phase_step: 'Phase 1 · P3 (SPEC §5)'
pattern: 'deterministic pre-filter + LLM trigger judgment'
version: 1.1.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P3, §7 R1, R8'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-03 — Select the Sub-Domain Subset

> **v1.1.0 change (2026-10-01):** the "4–10 sub-domain target" is removed —
> it over-pruned (the golden case keeps 35/38 sub-domains ACTIVE under
> GDPR+CRA). Every candidate is assessed; a candidate is EXCLUDED only with a
> why-not grounded in a specific company fact. Over-inclusion is cheaper than
> a missed sub-domain; the reviewer prunes at G-P1-C.

## Metadata

| Field | Content |
|---|---|
| Role | Solution-scope architect |
| Mission | From the candidate set, assess every sub-domain against company facts + confirmed regulation duties; exclude only with a grounded why-not |
| Inputs | Confirmed regulation set (G-P1-B); fact sheet |
| Output | §3 subset table + exclusion list (flag-not-drop) |
| Human gate | **G-P1-C** — reviewer confirms composition and exclusions |
| Failure mode | Excluded candidates are recorded with a why-not line, never omitted |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `pack-p3/candidates.md` — deterministic pre-filter result | candidate list |
| 2 | `baseline/domains/index.md` | canonical sub-domain names |
| 3 | candidate sub-domain objective paragraphs + participant rows (embedded in the pre-filter block) | subject matter + which regulations live in the module |
| 4 | `steps/fact_sheet.yaml` + `steps/verdicts.md` | fact sheet + verdicts |

**Deterministic pre-filter (before the LLM step):** candidate set = every sub-domain whose module contains `regs/<REG>.md` for at least one regulation confirmed at G-P1-B. Read from `baseline/domains/index.md` module maps. Everything not in the candidate set is out of scope for the run.

## Output schema

§3 table: `Sub-domain | Name | Trigger rationale` — plus an exclusion list:

```text
Excluded candidates: <D-XX.Y> — <one-line why-not (no company fact triggers it)>
```

## Prompt body

> You are a solution-scope architect. Work only from the candidate set (sub-domains whose module contains a regulation confirmed at G-P1-B).
>
> For each candidate sub-domain:
> 1. Read its participant rows (which confirmed regulations are present) and the sub-domain's subject matter.
> 2. Decide: does an obligation of a confirmed regulation match the sub-domain subject matter AND trigger on a company fact? Write the decision as a one-line trigger rationale in "company fact → regulation duty" form (example: "client PII stored on managed cloud → GDPR Art. 32 security of processing").
> 3. If no company fact triggers it, move the sub-domain to the exclusion list with a why-not line naming the absent fact — not a hunch.
>
> Rules:
> 1. Canonical IDs only, exactly as in `baseline/domains/index.md` — never invent, merge, or reformat (R1).
> 2. Only confirmed regulations generate triggers (R8).
> 3. **Default is INCLUSION.** When a confirmed regulation applies broadly, most sub-domains stay active (the golden case keeps 35/38 under GDPR+CRA). Exclude only when a specific company fact is absent (e.g. "no AI systems placed on the market → D-10.3 compliance testing of AI models not triggered"). A doubt means INCLUDE with an `open question` tag — the reviewer prunes at G-P1-C.
> 4. Do not read goal content or requirements yet — selection only.

## Self-checks (L2)

- Every selected ID exists in `baseline/domains/index.md` (canonical spelling).
- Every selection cites ≥1 confirmed regulation + ≥1 company fact.
- Every candidate is either selected or excluded with a grounded why-not line (no silent drops).
- Count reported (selection + exclusions = candidate set).

## Guard hooks (L0/L1)

- SPEC §8 item 3 (codes exist in the corpus).
- Selection list feeds P4's per-sub-domain packs — IDs must match module directory names exactly.

## Failure handling

- Ambiguous trigger → keep in selection with an `open question` tag and resolve at G-P1-C (over-inclusion is cheaper than a missed sub-domain; the reviewer prunes).

## Human gate

**G-P1-C:** present the selection with trigger rationales + the exclusion list; reviewer confirms composition. Pruned selections move to the exclusion list with their rationale.
