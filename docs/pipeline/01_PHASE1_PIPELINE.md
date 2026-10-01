---
document_id: AEGIS-PIPE-01
title: 'Phase 1 Pipeline — Contextual Definition (P1–P5)'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
upstream:
  - SPEC.md
  - templates/company_input.md
  - templates/phase1_output.md
  - example/
fichas:
  - prompts/PROM-P1-01_EXTRACT_FACTS.md
  - prompts/PROM-P1-02_CONFIRM_REGULATIONS.md
  - prompts/PROM-P1-03_SELECT_SUBDOMAINS.md
  - prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md
  - prompts/PROM-P1-05_RENDER_VALIDATE.md
---

# Phase 1 Pipeline — Contextual Definition

## 1. Scope & contracts

- **Input contract (SPEC §4):** `input/<company>/company_input.md`, 5 plain-prose sections; §5 must list ≥1 regulation with a one-line justification; regulation identifiers `GDPR | CRA | NIS2 | DORA | AI_Act`.
- **Output contract (SPEC §6):** `output/<company>/phase1_output.md`, 6 sections — §1 profile echo, §2 applicable regulations, §3 sub-domain subset, §4 adjusted goals (+ §4.1 anchor mapping), §5 ambiguities & assumptions, §6 handoff notes.
- **Normative procedure:** SPEC §5 (P1–P5); rules R1–R8 (SPEC §7); checklist §8. This document organizes the same procedure into executable steps; the fichas are the executable artifacts.

## 2. Step sequence

| Step | Ficha | Pattern | Consumes | Produces | Gate after |
|---|---|---|---|---|---|
| P1 | [PROM-P1-01](prompts/PROM-P1-01_EXTRACT_FACTS.md) | single structured call | company_input §1–§4 (+ §5 read) | internal fact sheet | G-P1-A |
| P2 | [PROM-P1-02](prompts/PROM-P1-02_CONFIRM_REGULATIONS.md) | routing per regulation | fact sheet + §5 assumptions | §2 verdict table (applies / does not apply / flagged) | G-P1-B |
| P3 | [PROM-P1-03](prompts/PROM-P1-03_SELECT_SUBDOMAINS.md) | deterministic pre-filter + LLM trigger judgment | verdicts + domains index | §3 subset table + exclusion list | G-P1-C |
| P4 | [PROM-P1-04](prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md) | parallelization per D-XX.Y | subset + context packs | §4 goal tables + §4.1 anchors + §5 entries | G-P1-D |
| P5 | [PROM-P1-05](prompts/PROM-P1-05_RENDER_VALIDATE.md) | render + layered validation | all step outputs | `phase1_output.md` (DRAFT→ACTIVE) + `RUN_NOTES.md` | sign-off |

## 3. Step cards (summary — full execution detail lives in the fichas)

### P1 — Extract facts
Fact sheet with fixed fields (sector, size, jurisdictions, legal form, product summary, `develops_software`, data categories, subjects, sensitive data, scale, hosting, access model, third parties, assumed regulations) + `open_questions`. Every field traces to input text (R6); gaps become `open_questions`, never guesses. Input §5 is read but **not judged** here (that is P2).

### P2 — Confirm applicable regulations
Evaluate each of the 5 candidate regulations against the fact sheet using the scope criteria embedded in the ficha (GDPR establishment/processing; CRA products with digital elements placed on the market; NIS2 sector+size essential/important entity; DORA financial entity; AI Act placing on the market / deploying high-risk AI). Verdicts: `**applies**`, `does not apply`, `flagged` (assumed in §5 but failing the scope test — flagged, never silently dropped). All 5 rows are rendered; every §5 assumption appears.

### P3 — Select the sub-domain subset
**Deterministic pre-filter:** candidate set = sub-domains whose `regs/` directory contains ≥1 confirmed regulation (from `baseline/domains/index.md` module maps). **LLM judgment:** for each candidate, does an obligation of a confirmed regulation match the sub-domain subject matter AND trigger on company facts? One-line trigger rationale per selection (fact → duty form). Excluded candidates are recorded with a why-not line. Canonical IDs only (R1).

### P4 — Derive adjusted goals
One invocation per selected sub-domain (parallelizable). Context pack per D-XX.Y (exact paths in the ficha): `objective.md`, `regs/<REG>.md` for each confirmed regulation present in the module, `regs/<REG>.ambiguity.md`, `cross/<R1>-<R2>.md` + `cross/_interactions.md` only when ≥2 confirmed regulations apply, and the anchor slice from `baseline/MAPPINGS/sr_control_mappings/<REG>.json`. Output: the 8-column §4 table per sub-domain, §4.1 anchor rows (Source = `SR-<REG>-NNN`), §5 card/assumption entries. Anchors are **copied from pre-verified surfaces only** — Sub-SO anchor blocks, requirement YAML `nist_csf`/`nist_pf`/`nist_airmf`, mapping-store JSON — max 1–2 per goal, `—` rather than a stretch (R2). Axis discipline: PF 1.1 only on GDPR rows, AI RMF only on AI_Act rows (R8).

### P5 — Render and validate
Assemble §1–§6 per `templates/phase1_output.md`; run the §8 checklist; write `RUN_NOTES.md` with per-item evidence; `doc_lint.py --strict`. Status becomes `ACTIVE` only after every item passes and the human signs off (G-P1-D).

## 4. SPEC §8 checklist → guard mapping

| §8 item | Check | Guard layer |
|---|---|---|
| 1. Input: 5 sections present; §5 ≥1 regulation + justification | stop condition at P1 | L2 (ficha 01) + human |
| 2. §2 covers every regulation in input §5, none silently missing | row-coverage check | L2 (ficha 02) + L1 scriptable (row count) |
| 3. §3 codes exist in the corpus | `grep -r "D-XX.Y" baseline/domains` / index | L1 deterministic |
| 4. AG IDs unique; sub-domain part matches §3 row | ID table diff | L1 deterministic (simple parse) |
| 5. Regulatory sources resolve in `articles/` (R2a) | `ls <subdomain>/articles/ \| grep <REG>` spot-check | L1 deterministic |
| 6. Control anchors resolve in the referential (R2b) | resolve against `CONTROLS/` + mapping store | L1 deterministic |
| 7. No company statement without input trace or ASSUMPTION mark | trace-back pass | L2 (fichas 01/02/04) + L4 human |
| 8. Frontmatter complete; `status: ACTIVE` only after pass | render rule | L2 (ficha 05) + L4 gate G-P1-D |
| 9. Every goal: valid pattern, property, parent `SO-D-XX.Y.HL`, non-empty Adjustment | enum + field check | L1 deterministic (parseable) |
| 10. `doc_lint.py --strict` zero findings | run the script | L1 deterministic |

## 5. Human gates

| Gate | When | Reviewer decides | Record |
|---|---|---|---|
| **G-P1-A** | after P1 | fact sheet is faithful and complete; resolve `open_questions` | fact sheet approval note in `RUN_NOTES.md` |
| **G-P1-B** | after P2 | each of the 5 verdicts (confirm / correct); flagged assumptions accepted or input corrected | §2 review note |
| **G-P1-C** | after P3 | subset composition; exclusions accepted | §3 review note |
| **G-P1-D** | after P5 | sign-off → `status: ACTIVE` | `RUN_NOTES.md` final entry |

Gate reviews are business-language, per-item (the ADR-005 round convention, applied in miniature); IDs live in the artifacts, not in the questions.

## 6. Context-pack builder (spec)

A deterministic helper — direct heir of `scripts/generate_case_corpus_slice.py`, scoped to one Phase 1 run:

- **Inputs:** company id; P2 verdicts (confirmed regulations); P3 selection (sub-domain list).
- **Output:** `output/<company>/packs/` — per step, the exact file list the ficha declares:
  - `pack-p2.md` — fact sheet + scope criteria (no corpus files needed);
  - `pack-p3.md` — `baseline/domains/index.md` + candidate `_index.md` files (participant rows only);
  - `pack-p4-<D-XX.Y>.md` — `objective.md` + `regs/<REG>.md` (confirmed regs present in module) + `regs/<REG>.ambiguity.md` + `cross/` pair files (both regs confirmed) + `cross/_interactions.md` + anchor slice from `sr_control_mappings/<REG>.json`;
  - `pack-p5.md` — template + all step outputs.
- **Guarantees:** file list is a pure function of (company, verdicts, selection); no summarization, verbatim copies or references only; every path in a pack must resolve before the step starts (fail loudly, flag-not-drop).
- **Implementation:** may be a script (Increment-safe) or a manual checklist the agent executes; determinism matters, automation does not (ADR-010).

## 7. Runbook — executing one Phase 1 run

1. Create `output/<company>/`; copy nothing from other companies' runs.
2. Run **P1** (ficha 01) → fact sheet → **G-P1-A**.
3. Run **P2** (ficha 02) → §2 table → **G-P1-B**.
4. Build pack-p3; run **P3** (ficha 03) → §3 table + exclusions → **G-P1-C**.
5. Build pack-p4-*; run **P4** (ficha 04) per sub-domain (batch order D-01.1 → D-10.3) → §4/§4.1/§5 fragments → **G-P1-D (partial)**.
6. Run **P5** (ficha 05): render document, write `RUN_NOTES.md`, run `doc_lint.py --strict`, resolve §8 items → **G-P1-D (final)**.
7. Only after G-P1-D passes: set frontmatter `status: ACTIVE`; hand off §6 to Phase 2.

Re-entry rule: any failed gate re-enters at the producing step with the gate's recorded corrections; earlier artifacts are amended in place with the document's own changelog entry (R11).

## 8. Artifacts written per run

```text
output/<company>/
├── phase1_output.md          # the deliverable (SPEC §6 template)
├── RUN_NOTES.md              # §8 evidence table + gate review notes
└── packs/                    # context packs (deterministic, re-buildable)
    ├── pack-p2.md
    ├── pack-p3.md
    ├── pack-p4-<D-XX.Y>.md   # one per selected sub-domain
    └── pack-p5.md
```
