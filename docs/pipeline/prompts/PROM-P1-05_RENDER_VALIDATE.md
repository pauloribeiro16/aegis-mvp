---
ficha_id: PROM-P1-05
title: 'Render and Validate the Output'
phase_step: 'Phase 1 · P5 (SPEC §5, §8)'
pattern: 'render + layered validation'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P5, §6 (output contract), §8 (checklist)'
  - 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md §7 (validation layers)'
---

# PROM-P1-05 — Render and Validate the Output

## Metadata

| Field | Content |
|---|---|
| Role | Renderer + quality gatekeeper |
| Mission | Assemble the deliverable from approved step outputs; run the full §8 checklist; produce the run evidence |
| Inputs | Fact sheet; §2 verdicts; §3 selection + exclusions; §4/§4.1/§5 fragments; template |
| Output | `output/<company>/phase1_output.md` (status DRAFT) + `output/<company>/RUN_NOTES.md` |
| Human gate | **G-P1-D (final)** — sign-off flips status to ACTIVE |
| Failure mode | Any checklist failure keeps status DRAFT; findings are fixed or flagged, never silenced |

## Context pack (load exactly these)

| # | File | Use |
|---|---|---|
| 1 | `templates/phase1_output.md` | 6-section structure, frontmatter, §4 framing blockquote |
| 2 | All prior step outputs (packs + fragments) | content source |
| 3 | `example/phase1_output.md` + `example/RUN_NOTES.md` | golden reference for shape and evidence style |
| 4 | `SPEC.md` §8 | the checklist being evidenced |

## Output schema

`phase1_output.md` with frontmatter (`document_id: MVP-P1-OUT-<n>`, `version`, `created`, `status: DRAFT`, `input`, `corpus`) and sections §1–§6 per the template:

- §1 Company profile echo (≤15 lines, verbatim-faithful condensation of input §1–§4);
- §2 Applicable regulations (5 pre-seeded rows, verdicts from G-P1-B);
- §3 Applicable sub-domain subset (selection table from G-P1-C);
- §4 Adjusted goals (framing blockquote + one table per sub-domain) + §4.1 control anchor mapping;
- §5 Ambiguities & open questions (card citations + ASSUMPTION blockquotes; `None.` if empty);
- §6 Handoff notes to Phase 2 (≤10 lines).

`RUN_NOTES.md`: one evidence table row per §8 item (1–10): item → how verified → result.

## Prompt body

> You are the renderer and quality gatekeeper for this Phase 1 run.
>
> 1. Assemble `phase1_output.md` strictly per the template's 6-section structure. The §1 echo condenses input §1–§4 without adding anything (R6). §2, §3, §4, §4.1, §5 come from the approved step outputs — render, do not re-decide.
> 2. Open with the §4 framing blockquote (company size/tier, area, regulatory roles, inherited capabilities, exclusions) instead of repeating context per goal.
> 3. Run the §8 checklist item by item; for each, record in `RUN_NOTES.md` how it was verified and the result. Machine-checkable items (3, 4, 5, 6, 9) are verified by direct inspection commands (grep/ls against the corpus paths); item 10 by running `python scripts/doc_lint.py --strict`.
> 4. If any item fails: fix it in the fragment that produced it (not by editing the rendered document into consistency), re-render, and re-check.
> 5. Keep status DRAFT. §6 handoff: applicable regulations, sub-domain scope, open questions — ≤10 lines.

## Self-checks (L2)

- All 6 sections present, in template order, with the template's column contracts.
- §2 covers every input §5 regulation; §3 IDs match the confirmed selection; §4 IDs match §3 rows.
- Frontmatter complete; status DRAFT until G-P1-D final.
- No placeholders (`?`, `TODO`, unfilled `<>`), no editorial meta-commentary (R11, R12).

## Guard hooks (L0/L1)

- `python scripts/doc_lint.py --strict` → zero findings (§8 item 10).
- §8 items 3–6, 9 verifiable by parse/grep (see ficha PROM-P1-04 guard hooks).
- Anchor spot-checks: `ls <subdomain>/articles/ | grep <REG>` per cited source.

## Failure handling

- Checklist failure that cannot be fixed at this step → revert to the producing ficha (P2/P3/P4), fix there, re-enter P5.
- `doc_lint` findings are resolved, not waived.

## Human gate

**G-P1-D (final):** reviewer walks `RUN_NOTES.md` evidence + the rendered document; on sign-off, frontmatter `status` is set to `ACTIVE` and §6 hands off to Phase 2.
