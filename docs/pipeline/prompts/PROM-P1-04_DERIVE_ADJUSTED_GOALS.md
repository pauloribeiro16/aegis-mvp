---
ficha_id: PROM-P1-04
title: 'Derive Adjusted Goals'
phase_step: 'Phase 1 · P4 (SPEC §5)'
pattern: 'parallelization — one invocation per selected sub-domain'
version: 1.0.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P4, §7 R2, R3, R4, R7, R8'
  - 'AGENTS.md §4 P4, §5 R13 (altitude discipline)'
  - 'docs/decisions/ADR-2026-09-22_goal-objective-structure.md (ADR-003 card schema)'
---

# PROM-P1-04 — Derive Adjusted Goals

## Metadata

| Field | Content |
|---|---|
| Role | Security & privacy goals engineer (KAOS/GORE refinement) |
| Mission | Restate each selected sub-domain's Baseline Goals as company-proportional Adjusted Goals, anchored and traceable |
| Inputs | Confirmed regulation set; sub-domain selection (G-P1-C); fact sheet |
| Output | Per sub-domain: §4 goal table (8 columns); global: §4.1 anchor rows + §5 ambiguity/assumption entries |
| Human gate | **G-P1-D (partial)** — reviewer walks the goal tables per sub-domain batch |
| Failure mode | Unresolvable anchor → `—` + note; never invented (R2) |

## Context pack — one pack per selected sub-domain (`pack-p4-<D-XX.Y>.md`)

| # | File | Use |
|---|---|---|
| 1 | `baseline/domains/<D-XX_Name>/<D-XX.Y>/objective.md` | the regulation-neutral Baseline Goal (`SO-D-XX.Y.HL`) |
| 2 | `…/<D-XX.Y>/regs/<REG>.md` — **only for regulations confirmed at G-P1-B that are present in the module** | Sub-SO card + requirements + verbatim regulatory basis |
| 3 | `…/<D-XX.Y>/regs/<REG>.ambiguity.md` | ambiguity cards for the clauses cited |
| 4 | `…/<D-XX.Y>/cross/<R1>-<R2>.md` + `cross/_interactions.md` — **only when ≥2 confirmed regulations are present** | aggregation, tensions |
| 5 | `baseline/MAPPINGS/sr_control_mappings/<REG>.json` (anchor slice) | pre-verified control anchors per SR |
| 6 | `templates/phase1_output.md` §4 (incl. HTML comment) | KAOS pattern semantics, property taxonomy, column contract |
| 7 | `output/<company>/packs/pack-p2.md` | fact sheet (proportionality source) |

## Output schema

Per sub-domain, a `### D-XX.Y — <canonical name>` table, columns exactly:

`ID | Adjusted goal | Pattern | Property | Parent goal | Regulatory source | Control anchor | Adjustment`

- `ID`: `AG-D-XX.Y-NNN`, zero-padded, sequential per sub-domain within the run (R4).
- `Pattern`: one of `achieve | cease | maintain | avoid | optimize`.
- `Property`: one of `C | I | A | privacy-right | accountability`.
- `Parent goal`: `SO-D-XX.Y.HL` (the corpus module's `objective.md` YAML id `SG-D-XX.Y.HL` is the same entity under the frozen alias — ADR-004 D2; render the `SO-` form).
- `Regulatory source`: article citations resolving to the module's `articles/` or quotable verbatim from `regs/<REG>.md` (R2a); multi-article joined with `; `.
- `Control anchor`: max 1–2 control IDs, **copied** from the module's pre-verified anchor surfaces (Sub-SO anchor blocks, requirement YAML `nist_csf`/`nist_pf`/`nist_airmf`, mapping-store JSON); `—` when none fits cleanly (R2b).
- `Adjustment`: one auditable sentence stating what was adapted and why (R3; never silently relaxed — ADR-003 D1).

Plus §4.1 rows: `ID | Regulation | CSF 2.0 | NIST PF 1.1 | NIST AI RMF | Source` — one row per (goal, confirmed regulation) pair, `Source` = `SR-<REG>-NNN` from the mapping store.

Plus §5 entries: ambiguity card citations + `> ASSUMPTION:` blockquotes produced by this step.

## Prompt body

> You are a security & privacy goals engineer. For the sub-domain `D-XX.Y` (pack attached):
>
> 1. Read the Baseline Goal (`objective.md`) and, for each confirmed regulation present in the pack, its `regs/<REG>.md` module. Consult `cross/` files when two or more confirmed regulations apply. Ignore any regulation module not confirmed at G-P1-B (R8).
> 2. Keep only the Sub-SO goals and requirements of confirmed regulations; drop nothing silently — if a baseline goal has no confirmed-regulation carrier, record that in the Adjustment column or as an open question.
> 3. Restate each as a company-proportional goal using the fact sheet: wording fits the company's scale and operational reality (R3). Use the KAOS pattern semantics from the template's §4 comment. Do not add owner/verification fields (ADR-003 D3).
> 4. Assign `AG-D-XX.Y-NNN` sequentially from 001 (R4).
> 5. Anchor: cite regulatory sources that resolve in the module's `articles/` or are quotable verbatim from `regs/<REG>.md` (R2a). Copy control anchors only from the pack's pre-verified surfaces — never re-derive, never invent (R2b); max 2 per goal; use `—` rather than a stretch.
> 6. Axis discipline: `nist_pf` anchors only accompany GDPR-derived obligations; `nist_airmf` only AI_Act-derived obligations (R8).
> 7. If a cited clause has an ambiguity card in the pack, cite the card ID in §5 and follow its canonical resolution — do not re-interpret (R7).
> 8. Technology neutrality: state what must be achieved, never tools, vendors, or implementations (R5). Same altitude as the source module; a quantitative fit criterion is allowed, a mechanism prescription is not (R13 altitude discipline).
> 9. Produce the §4 table, the §4.1 rows, and the §5 entries in the output schema above.

## Self-checks (L2)

- Every `applies`-confirmed regulation present in the module was read; nothing from a non-confirmed regulation leaked in (R8).
- Every regulatory source string resolves to a file in `…/<D-XX.Y>/articles/` or verbatim text in `regs/<REG>.md` (R2a).
- Every control anchor string was copied from a surface in the pack and exists in the corresponding referential (R2b).
- IDs unique and sequential; every row has pattern, property, parent, non-empty Adjustment (§8 items 4, 9).
- Wording is company-proportional and technology-neutral (R3, R5).
- Every ambiguity encounter produced a §5 card citation, not a private interpretation (R7).

## Guard hooks (L0/L1)

- SPEC §8 items 3–6, 9 (scriptable parse: ID format/uniqueness, source resolution via `ls articles/`, anchor resolution against `CONTROLS/` + mapping store, enum validity).
- `doc_lint.py --strict` over the rendered output (item 10).

## Failure handling

- Anchor unresolvable → `—` in the anchor column + Adjustment note (or drop the anchor); record in `RUN_NOTES.md` (the golden-run precedent: `PR.DS-12` was excluded for exactly this reason).
- Module/regulation mismatch (e.g., regulation confirmed but absent from the module) → note in §5, flag at G-P1-D.

## Human gate

**G-P1-D (partial):** per sub-domain batch, the reviewer walks each goal row — confirm / adjust wording / reject with reason. Business language; IDs stay in the artifacts.
