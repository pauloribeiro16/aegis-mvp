---
ficha_id: PROM-P1-05
title: 'Assemble and Validate the Deliverable'
phase_step: 'Phase 1 · P5 (SPEC §5, §8)'
pattern: 'deterministic assembly + layered validation (no LLM call)'
version: 1.2.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P5, §6 (output contract), §8 (checklist)'
  - 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md §7 (validation layers)'
---

# PROM-P1-05 — Assemble and Validate the Deliverable

> **v1.2.0 change (2026-10-01):** the deliverable is the **Doc02 case format**
> (`doc02_adjusted_goals.md`, §0–§6). The assembly step is now **entirely
> deterministic — zero LLM calls**: §0/§1 are static template text; §2 is the
> p3f framing table; §3 renders the L0-validated goal JSONs with Regulation
> and Control Anchors derived by `controls.py`; §4 renders the p4t tension
> resolutions; §5 applies the deterministic Track B matrix; §6 derives the
> NIST control tables from the mapping store + CONTROLS referential. L1
> validation runs automatically and the deliverable is exported to
> `output/<company>/`.

## Metadata

| Field | Content |
|---|---|
| Role | Assembler + quality gatekeeper (code, not a model) |
| Mission | Stitch the deliverable from validated step artifacts and code-derived data; run the §8 checklist automatically |
| Inputs | Fact sheet; selection; framing (p3f); goal JSONs (P4); tensions (p4t); template; case binding (Track B overrides) |
| Output | `doc02_adjusted_goals.md` (status DRAFT) + `RUN_NOTES.md`, exported to `output/<company>/` |
| Human gate | **G-P1-D (final)** — sign-off flips status to ACTIVE |
| Failure mode | Any validation finding aborts the stage before sign-off; artifacts kept for forensics |

## Assembly contract

| § | Source | Nature |
|---|---|---|
| §0 Document Purpose | template (static, counts parametrized) | code |
| §1 Regulatory Floor | template (static, by-reference text) | code |
| §2 Framing | `steps/framing.md` (p3f, L0-validated 4-row table) | verbatim |
| §3 Adjusted Goals | `steps/goals/*.json` + HL paragraphs verbatim from `objective.md` + anchors via `controls.goal_anchors` | code + artifacts |
| §4 Tensions Resolved | `steps/tensions.json` (p4t); `None` for mono-regulation runs | verbatim |
| §5 Track B | `controls.track_b_rows` (deterministic matrix + case overrides) | code |
| §6 NIST Controls Mapping | `controls.sd_control_sections` (mapping store + CONTROLS JSONs) | code |

## Validation (automatic, before G-P1-D)

- Doc-vs-artifact cell diff: §2 table == framing.md; §3 rows == goal JSONs (incl. derived Regulation and Anchors == `controls.goal_anchors`); §4 ids == tensions.json; §5 rows == matrix derivation; §6 rows == `controls.sd_control_sections` derivation.
- §0–§6 present exactly once, in order; §1–§6 order check.
- SPEC §8 items 2–6, 9 (sources resolve via `articles/`/`regs/`; anchors resolve in `CONTROLS/` — by construction, diff-checked anyway); R12 hygiene; trace/manifest consistency.
- `doc_lint.py --strict` covers the exported copy under `output/<company>/`.

## Failure handling

- Any finding → stage aborts with the finding list; the document is kept on disk for forensics; fix the producing fragment/ficha and re-enter P5.
- `doc_lint` findings are resolved, not waived.

## Human gate

**G-P1-D (final):** reviewer walks `RUN_NOTES.md` evidence + the rendered document (including the §4 tension resolutions and the Track B tiers, which are company decisions); on sign-off, frontmatter `status` is set to `ACTIVE` and the deliverable hands off to Phase 2.
