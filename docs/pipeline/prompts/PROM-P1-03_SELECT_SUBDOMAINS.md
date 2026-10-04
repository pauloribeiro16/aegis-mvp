---
ficha_id: PROM-P1-03
title: 'Select the Sub-Domain Subset'
phase_step: 'Phase 1 · P3 (SPEC §5)'
pattern: 'deterministic pre-filter + LLM trigger judgment'
version: 1.2.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P3, §7 R1, R8'
  - 'docs/pipeline/01_PHASE1_PIPELINE.md'
---

# PROM-P1-03 — Select the Sub-Domain Subset

> **v1.2.0 change (2026-10-04):** the §3 table and the exclusion list are stated
> as an explicit **partition** of the candidate set, and the exclusion list is
> allowed to be **empty**. v1.1.0 showed only the non-empty form of the
> exclusion line, and never said a sub-domain may not appear in both places.
> Two models filled the slot instead of leaving it empty and died at L0 across
> every repeat: `glm-4.7-flash` put D-02.4 in the table *and* in the exclusion
> list; `nemotron-3.5-lightning` named D-06.5 — an id that does not exist —
> and, on the repair retry, wrote the reason it was wrong inside the very line
> that was wrong ("N/A (no D-06.5 in candidate set)"). The gate was right in
> both cases; the prompt had left an apparently mandatory slot with no legal
> empty value.
>
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
Excluded candidates: (none — every candidate is triggered)
```

Several exclusions are written as several `Excluded candidates:` lines.

**The two lists are a partition of the candidate set.** Every candidate id
appears in exactly one of them: in the §3 table, or in the exclusion list.
Never both, never neither. The exclusion list is a legal empty result — if
every candidate is triggered, write `(none — every candidate is triggered)`
and add no further line. A candidate you name in the exclusion list must be
moved out of the §3 table in the same answer.

## Prompt body

> You are a solution-scope architect. Work only from the candidate set (sub-domains whose module contains a regulation confirmed at G-P1-B).
>
> For each candidate sub-domain:
> 1. Read its participant rows (which confirmed regulations are present) and the sub-domain's subject matter.
> 2. Decide: does an obligation of a confirmed regulation match the sub-domain subject matter AND trigger on a company fact? Write the decision as a one-line trigger rationale in "company fact → regulation duty" form (example: "client PII stored on managed cloud → GDPR Art. 32 security of processing").
> 3. If no company fact triggers it, move the sub-domain to the exclusion list with a why-not line naming the absent fact — not a hunch. "Move" means remove its row from the §3 table in this same answer: a sub-domain is either in the table or in the exclusion list, never in both.
>
> Rules:
> 1. Canonical IDs only, exactly as in `baseline/domains/index.md` — never invent, merge, or reformat (R1). Copy each id from the candidate list above character for character. If you are unsure whether an id exists, do not name it: leave it IN the §3 table and let the reviewer prune at G-P1-C. An invented id (one that is not in the candidate list) is a hard failure, not a near miss.
> 2. Only confirmed regulations generate triggers (R8).
> 3. **Default is INCLUSION.** When a confirmed regulation applies broadly, most sub-domains stay active (the golden case keeps 35/38 under GDPR+CRA). Exclude only when a specific company fact is absent (e.g. "no AI systems placed on the market → D-10.3 compliance testing of AI models not triggered"). A doubt means INCLUDE with an `open question` tag — the reviewer prunes at G-P1-C.
> 4. Do not read goal content or requirements yet — selection only.
> 5. The §3 table and the exclusion list partition the candidate set: every candidate appears in exactly one. Never write a sub-domain in both. An empty exclusion list is a valid answer — write `Excluded candidates: (none — every candidate is triggered)` and stop. Do not invent an exclusion to fill the line.

## Self-checks (L2)

- Every selected ID exists in `baseline/domains/index.md` (canonical spelling).
- Every selection cites ≥1 confirmed regulation + ≥1 company fact.
- Every candidate is either selected or excluded with a grounded why-not line (no silent drops).
- Count reported (selection + exclusions = candidate set).
- No id appears in both the §3 table and the exclusion list; the exclusion list was
  read back to confirm it is either empty or fully grounded — not padded to fill
  the line.

## Guard hooks (L0/L1)

- SPEC §8 item 3 (codes exist in the corpus).
- Selection list feeds P4's per-sub-domain packs — IDs must match module directory names exactly.

## Failure handling

- Ambiguous trigger → keep in selection with an `open question` tag and resolve at G-P1-C (over-inclusion is cheaper than a missed sub-domain; the reviewer prunes).

## Human gate

**G-P1-C:** present the selection with trigger rationales + the exclusion list; reviewer confirms composition. Pruned selections move to the exclusion list with their rationale.
