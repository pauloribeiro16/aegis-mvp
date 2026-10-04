# Run Notes — golden example (VetCare Connect)

| Field | Value |
|---|---|
| Run date | 2026-09-17 |
| Executor | ZCode agent (LLM-assisted procedure, SPEC v0.1.0) |
| Input | `example/company_input.md` (fictional company) |
| Output | `example/doc02_adjusted_goals.md` |
| Corpus | Methodology_compact `PREPROCESSING_by_domain` (build E3, frozen) |

Steps executed: P1 fact sheet → P2 regulation scope check (5/5 with verdicts)
→ P3 subset selection (4 of 38 sub-domains) → P4 corpus-grounded derivation
(Part 1 HSO/Sub-SO read for each of D-01.1, D-03.2, D-05.3, D-09.4; anchors
picked from `articles/` copies and corpus-convergent NIST IDs) → P5 render +
checklist below.

## SPEC §8 checklist — evidence

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Input: 5 sections, §5 ≥1 regulation w/ justification | PASS | 5 sections filled; §5 lists GDPR + 4 considered-and-excluded |
| 2 | §2 covers every input §5 regulation | PASS | GDPR + CRA + NIS2 + DORA + AI_Act all verdict-ed |
| 3 | Sub-domain codes exist in corpus | PASS | `domains/D-01_Data-Protection/D-01.1/`, `…/D-03.2/`, `…/D-05.3/`, `…/D-09.4/` all present |
| 4 | AG IDs unique, match §3 rows | PASS | 6 IDs, AG-D-XX.Y prefix matches each §3 row |
| 5 | Regulatory sources resolve (R2a) | PASS | D-01.1: `GDPR_Art_32.md`, `GDPR_Art_5.md` in `articles/`; D-03.2: no GDPR copies → **verbatim arm** (Art. 28(3)(b)+Art. 29 quoted in merged file, GDPR↔NIS2 pair section); D-05.3: `GDPR_Art_17/7/28.md`; D-09.4: `GDPR_Art_30.md` |
| 6 | Control anchors resolve in referential (R2b) | PASS | `PR.DS-01`, `PR.AA-03`, `PR.DS-10`, `GV.PO-02`, `ID.AM-08` all members of `NIST_CSF_2.0/CSF_2.0.json` subcategories. **Catch:** `PR.DS-12` is cited inside `D-05.3.md`/`D-09.4.md` but does **not** resolve in the referential JSON → excluded per R2b (PR.DS-10 used instead for D-05.3) |
| 7 | No untraced company statements (R6) | PASS | No `ASSUMPTION` blocks owed |
| 8 | Frontmatter complete; `status: ACTIVE` post-checklist | PASS | 8 fields set |

## Ambiguity registry integration (rule R7)

`GDPR-CP15` (Art. 32(1) "state of the art", VAG/S3) found in
`AMBIGUITY_REGISTRY/registry.csv` for D-01.1 → cited in output §5, canonical
resolution followed (closed-list reading of the four Art. 32(1) measures).

## Lessons recorded for future runs

1. The corpus's own NIST mentions are not always referential-clean
   (PR.DS-12) — always resolve anchors against `CONTROLS/`, never trust a
   sub-domain file's mention alone (rule R2b exists for this).
2. Sub-domains without GDPR `articles/` copies (D-03.2) still support R2a via
   the merged file's verbatim pair sections — check both arms before dropping
   a goal.
3. The corpus's per-regulation Sub-SOs encode honest scope nuance (D-03.2:
   "no explicit MFA mandate" under GDPR) — goals inherit that nuance
   instead of overclaiming.

## Post-modularization note (2026-09-21, after M1/M2)

This run predates the modular corpus (`baseline/domains/` per-regulation
layout, commits M1–M2). Reading notes for re-runs under the modular layout:

- Checklist item 5 (R2a verbatim arm): D-03.2's Art. 28(3)(b) + Art. 29 quote
  now lives in `D-03.2/regs/GDPR.md` → "Verbatim regulatory basis (GDPR)"
  (extracted verbatim from the former GDPR↔NIS2 pair section). A single-reg
  run no longer needs any cross-regulation pair file for anchoring.
- Checklist item 6 / anchor choice: `PR.AA-03` (AG-D-03.2-001) was sourced
  from the **NIS 2** Sub-SO card of the merged file — under the modular
  corpus a GDPR-only run reads `D-03.2/regs/GDPR.md`, whose own CSF anchors
  are `PR.AA-05, PR.AA-06, PR.AT-02`; a GDPR-only re-run would anchor there
  (regulation discipline R8 is enforced by construction). The historical
  output above is left as-run.
- "Read Part 1 HSO/Sub-SO" in the procedure description maps to:
  `objective.md` + `regs/<REG>.md` per confirmed regulation
  (SPEC §5 P4, AGENTS.md §4).
