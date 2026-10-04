---
ficha_id: PROM-P1-04
title: 'Derive Adjusted Goals'
phase_step: 'Phase 1 · P4 (SPEC §5)'
pattern: 'parallelization — one invocation per selected sub-domain'
version: 1.5.0
created: 2026-10-01
status: ACTIVE
normative_source:
  - 'SPEC.md §5 P4, §7 R2, R3, R4, R8'
  - 'AGENTS.md §4 P4, §5 R13 (altitude discipline)'
  - 'docs/decisions/ADR-2026-09-22_goal-objective-structure.md (ADR-003 card schema)'
---

# PROM-P1-04 — Derive Adjusted Goals

> **v1.4.0 change (2026-10-01):** the goal table gains the **Company
> implication** column (9 columns) — each row states what the duty concretely
> means for THIS company given the §2 framing. The Adjusted goal column must be
> a full company-proportional RESTATEMENT of the Sub-SO's Objective (2+
> sentences, no meta-language); the L0 rejects thin rows.

> **v1.3.0 change (2026-10-01):** the deliverable is now the Doc02 case format.
> The model emits NO control anchors (they are derived by `controls.py` from
> `Baseline source → source_SR → mapping store`, R2b by construction) and no
> §4.1 table (replaced by the deterministic §6 NIST Controls Mapping). One row
> per Sub-SO of each confirmed regulation, in canonical regulation order
> (slots 001=GDPR, 002=CRA, …).

> **v1.1.0 ruling (2026-10-01):** ambiguity cards do not enter Phase 1 — the
> interpretation was decided in Fase 0; §5 carries only `> ASSUMPTION:`
> blockquotes and open questions (R6).

## Metadata

| Field | Content |
|---|---|
| Role | Security & privacy goals engineer (KAOS/GORE refinement) |
| Mission | Restate each selected sub-domain's Baseline Goals as company-proportional Adjusted Goals, traceable to their corpus Sub-SO, with an explicit per-goal adjustment decision |
| Inputs | Confirmed regulation set; sub-domain selection (G-P1-C); §2 framing table (stage p3f); fact sheet |
| Output | Per sub-domain: §3 goal table (9 columns) + §5 assumption/open-question entries |
| Human gate | **G-P1-D (partial)** — reviewer walks the goal tables per sub-domain batch |
| Failure mode | Unresolvable citation → re-derive or drop the goal; never invent (R2) |

## Context pack — one pack per selected sub-domain (`pack-p4-<D-XX.Y>.md`)

| # | File | Use |
|---|---|---|
| 1 | `baseline/domains/<D-XX_Name>/<D-XX.Y>/objective.md` | the regulation-neutral Baseline Goal (`SO-D-XX.Y.HL`) |
| 2 | `…/<D-XX.Y>/regs/<REG>.md` — **only for regulations confirmed at G-P1-B that are present in the module** | Sub-SO card + requirements + verbatim regulatory basis |
| 3 | `…/<D-XX.Y>/cross/<R1>-<R2>.md` + `cross/_interactions.md` (operative sections) — **only when ≥2 confirmed regulations are present** | aggregation, tensions |
| 4 | `templates/doc02_adjusted_goals.md` §3 | goal table contract, pattern semantics, property enum, adjustment vocabulary |
| 5 | `steps/framing.md` | the §2 framing table produced by PROM-P1-06 — conditions every goal |
| 6 | `steps/fact_sheet.yaml` | company facts (proportionality source) |

## Output schema

Per sub-domain, a `### D-XX.Y — <canonical name>` table, columns exactly:

`ID | Adjusted goal | Company implication | Pattern | Property | Parent goal | Baseline source | Regulatory source | Adjustment`

- `ID`: `AG-D-XX.Y-NNN`, zero-padded, sequential per sub-domain (R4).
- `Adjusted goal`: a full company-proportional **restatement of that Sub-SO's Objective** (2+ sentences, same obligation content as the corpus text, calibrated to the company by the framing) — never a meta-line ("restatement of the baseline goal").
- `Company implication`: what this duty concretely means for THIS company given the §2 framing and fact sheet (1–2 sentences naming the company's actual situation, inherited capabilities, or declared gaps).
- `Pattern`: one of `achieve | cease | maintain | avoid | optimize`.
- `Property`: one of `C | I | A | privacy-right | accountability`.
- `Parent goal`: `SO-D-XX.Y.HL` (the corpus module's yaml id `SG-D-XX.Y.HL` is the same entity under the frozen alias — ADR-004 D2; render the `SO-` form).
- `Baseline source`: exactly ONE corpus Sub-SO id — `SG-D-XX.Y.<REG>` — the entity this row restates. Regulation order within the table follows the canonical order (GDPR → CRA → NIS2 → DORA → AI_Act): slot 001 = lowest-order confirmed regulation. The doc's Regulation and Control Anchors columns are DERIVED from this id by code.
- `Regulatory source`: article citations resolving to the module's `articles/` or quotable verbatim from `regs/<REG>.md` (R2a); multi-article joined with `+` or `;`.
- `Adjustment`: exactly one decision record — `unchanged — fits as stated` | `narrowed: <what> — because <company fact>` | `flagged: <open question>`. Never silently relaxed (ADR-003 D1); "no adjustment needed" is an explicit decision, not an invented one.

Granularity: **one row per Sub-SO of each confirmed regulation** — the Sub-SO's requirements fuse into the goal wording; never one row per requirement. A baseline duty with no confirmed-regulation carrier or no company fact triggering it is recorded as an open question in §5 — never dropped silently.

Plus §5 entries: `> ASSUMPTION:` blockquotes and open questions produced by this step (R6). No ambiguity card citations — the interpretation is already decided in Fase 0.

## Prompt body

> You are a security & privacy goals engineer. For the sub-domain `D-XX.Y` (pack attached):
>
> 1. Read the Baseline Goal (`objective.md`), the §2 framing table, and, for each confirmed regulation present in the pack, its `regs/<REG>.md` module. Consult `cross/` files when two or more confirmed regulations apply. Ignore any regulation module not confirmed at G-P1-B (R8).
> 2. Work Sub-SO by Sub-SO of the confirmed regulations: restate each Sub-SO's **Objective** as ONE company-proportional goal (2+ sentences, same obligation content, calibrated by the framing — R3); fuse the Sub-SO's requirements into the wording.
> 3. In the Company implication column, state what the duty concretely means for this company (its actual situation, inherited capabilities, declared gaps — from the framing and fact sheet, R6).
> 4. Decide the Adjustment column per the closed vocabulary. Do not invent adjustments when the baseline already fits — say `unchanged — fits as stated`.
> 5. Assign `AG-D-XX.Y-NNN` sequentially from 001, ordering rows by the canonical regulation order of their Baseline source (R4).
> 6. Cite regulatory sources that resolve in the module's `articles/` or are quotable verbatim from `regs/<REG>.md` (R2a). Do NOT emit control anchors — they are derived by code from the Baseline source (R2b by construction).
> 7. Ambiguity interpretation is already decided in the corpus (Fase 0 baseline) — apply it as written and move on; do not cite or re-analyze ambiguity cards in §5.
> 8. Technology neutrality: state what must be achieved, never tools, vendors, or implementations (R5). Same altitude as the source module; a quantitative fit criterion is allowed, a mechanism prescription is not (R13 altitude discipline).
> 9. Produce the §3 table and the §5 entries in the output schema above.

## Method — how to adapt a Sub-SO into an Adjusted Goal

The operation is **calibration, not rewriting**: the duty keeps its content, the
company changes its wording and precision.

1. **Take the Sub-SO's `**Objective.**` paragraph as the floor.** It is attached
   verbatim. Read what it actually requires — every leg, every article. If the
   objective has two obligations (e.g. confidentiality **and** resilience), the
   adjusted goal must carry both; dropping one is losing the obligation, not
   adapting it.
2. **Narrow to the company's actual situation** using the framing and fact
   sheet: the systems it really runs, the data it really holds, the roles it
   really has, the capabilities it inherits from suppliers. A clause that
   presupposes something the company does not have is narrowed to the
   alternative it does have (e.g. encryption capability inherited from a
   hosting provider becomes a contractual confirmation duty, not an
   in-house key-management programme).
3. **State the company implication** — what this duty concretely demands of
   this company, naming its real situation, inherited capabilities, or declared
   gaps. It must be specific to this duty; a sentence reusable on every row of
   the document is worthless and is rejected.
4. **Decide the adjustment honestly** with the closed vocabulary. Use
   `unchanged — fits as stated` when the baseline already applies as written —
   this is a real answer, not a cop-out. Use `narrowed:` when the company
   context forces a narrower or differently-framed reading, and name the
   company fact that forces it. Use `flagged:` when the duty cannot be judged
   from the input.
5. **When the baseline is simply wrong at this altitude** (it presumes an
   activity the company does not perform), do not silently drop it and do not
   force it: narrow it to the closest thing the company actually does and
   record the residual as `flagged:`.

A worked example (one sub-domain, baseline → adjusted goal → implication) is
attached to the pack. Read it before writing.

## Self-checks (L2)

- Every `applies`-confirmed regulation present in the module was read; nothing from a non-confirmed regulation leaked in (R8).
- Every row cites exactly one Baseline-source Sub-SO id; regulation order is canonical; a reviewer can walk AG → corpus in one step.
- Every Adjustment uses exactly one vocabulary form; no invented adjustments, no silent relaxations.
- Every regulatory source string resolves to a file in `…/<D-XX.Y>/articles/` or verbatim text in `regs/<REG>.md` (R2a).
- IDs unique and sequential; every row has pattern, property, parent, non-empty Adjustment (§8 items 4, 9).
- Wording is company-proportional and technology-neutral (R3, R5).
- §5 contains only `> ASSUMPTION:` blockquotes and open questions — no ambiguity card citations.
- Each adjusted goal still carries the full obligation content of its Sub-SO (no dropped leg, no lost article reference).
- No goal is a near-verbatim copy of the Sub-SO objective — each one says something about this company.
- Each Company implication is specific to its own duty and would not read correctly on another row.
- No company statement (size, vendor, product, location, certification) that is not in the fact sheet or the framing.
- No technology, vendor, framework or protocol is named anywhere.

## Guard hooks (L0/L1)

- L0 (per call): 9-column contract, sequential IDs, canonical regulation order, enum validity, Baseline-source format, plus the content gates in `quality.py` (obligation retention, adaptation, grounding, technology neutrality, per-row specificity, Sub-SO coverage).
- L1 (`validate.py`): source resolution via `articles/`/`regs/` (item 5), derived anchors vs doc diff, item 9.
- `doc_lint.py --strict` over the exported deliverable (item 10).

## Failure handling

- Module/regulation mismatch (e.g., regulation confirmed but absent from the module) → note in §5, flag at G-P1-D.
- A baseline duty with no company-fact trigger → open question in §5, not a silent drop.

## Human gate

**G-P1-D (partial):** per sub-domain batch, the reviewer walks each goal row — confirm / adjust wording / reject with reason. The Adjustment vocabulary makes the review a per-row accept/reject on an explicit decision: `unchanged` rows need no debate; `narrowed` rows state their warrant; `flagged` rows carry the question to resolve. Business language; IDs stay in the artifacts.
