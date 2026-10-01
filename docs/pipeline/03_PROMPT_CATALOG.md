---
document_id: AEGIS-PIPE-03
title: 'Prompt Catalog — ficha anatomy and full catalog'
version: 0.1.0
created: 2026-10-01
status: ACTIVE
---

# Prompt Catalog

## 1. Ficha anatomy (the standard)

Every executable prompt is a **ficha** (card) — a versioned markdown file under [prompts/](prompts/). One step = one ficha = one output contract. Fixed anatomy:

| # | Field | Content |
|---|---|---|
| 1 | `ID / Title / Phase-step` | `PROM-<PHASE>-<NN>`; human title; phase and SPEC §5 step |
| 2 | `Workflow pattern` | chaining step / routing / parallelization / evaluator–optimizer round (per master design §3) |
| 3 | `Role` | the persona and discipline the agent must adopt for this step |
| 4 | `Mission` | one paragraph: what this step must accomplish |
| 5 | `Inputs` | contract: files/fields this step consumes |
| 6 | `Context pack` | the deterministic file list (paths) to load — no free-form retrieval |
| 7 | `Procedure` | ordered instructions |
| 8 | `Output schema` | exact tables/columns/enums to produce |
| 9 | `Self-checks (L2)` | checklist the agent runs on its own output, bound to SPEC §7 rules |
| 10 | `Guard hooks (L0/L1)` | what `doc_lint.py` / `check_traceability.py` / §8 items will verify afterwards |
| 11 | `Human gate` | the G-* gate and what the reviewer decides |
| 12 | `Failure handling` | flag-not-drop rules; stop conditions |
| 13 | `Normative source` | SPEC/AGENTS/ADR sections this ficha implements |
| 14 | `Prompt body` | the verbatim instruction block to execute |

Fichas are internal engineering artifacts (R11 does not bind their style, but they still respect R12 hygiene): the *deliverables* they produce must obey R5/R13 neutrality, active-verb titles, card anatomy, and altitude rules.

## 2. Naming and versioning

- `PROM-<PHASE>-<NN>` where `<PHASE>` ∈ `P1`, `P2`, `P3A` (Phase 3 Part 1), `P3B` (Phase 3 Part 2).
- Filename: `PROM-<PHASE>-<NN>_<VERB_PHRASE>.md` (active-verb, underscore-joined).
- Changes to a ficha's prompt body = version bump in its frontmatter + one changelog line; executed runs keep the version they used in `RUN_NOTES.md`.

## 3. Catalog

### Phase 1 — Contextual Definition (detailed; fichas exist)

| ID | Title | Pattern | Ficha |
|---|---|---|---|
| PROM-P1-01 | Extract Company Facts | single structured call | [prompts/PROM-P1-01_EXTRACT_FACTS.md](prompts/PROM-P1-01_EXTRACT_FACTS.md) |
| PROM-P1-02 | Confirm Applicable Regulations | routing (per regulation) | [prompts/PROM-P1-02_CONFIRM_REGULATIONS.md](prompts/PROM-P1-02_CONFIRM_REGULATIONS.md) |
| PROM-P1-03 | Select the Sub-Domain Subset | pre-filter + judgment | [prompts/PROM-P1-03_SELECT_SUBDOMAINS.md](prompts/PROM-P1-03_SELECT_SUBDOMAINS.md) |
| PROM-P1-04 | Derive Adjusted Goals | parallelization (per D-XX.Y) | [prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md](prompts/PROM-P1-04_DERIVE_ADJUSTED_GOALS.md) |
| PROM-P1-05 | Render and Validate the Output | render + layered validation | [prompts/PROM-P1-05_RENDER_VALIDATE.md](prompts/PROM-P1-05_RENDER_VALIDATE.md) |

### Phase 2 — Operationalization (skeleton; fichas in the next pass)

| ID | Title | Mission (one line) |
|---|---|---|
| PROM-P2-01 | Derive Operational Objectives | per sub-domain: AG set → PO-/SO-D-XX.Y-NNN objectives (ISO 27001 6.2 discipline) with `RULE-*` tail |
| PROM-P2-02 | Resolve Obligations and Tensions | obligations/tensions from confirmed regulations → resolution records feeding objectives |
| PROM-P2-03 | Synthesize Secure Design Principles | transversal, technology-agnostic engineering principles (PRIN-ENG-*) |
| PROM-P2-04 | Render and Validate Phase 2 | Doc01/Doc02 per case convention + structure lint + anchor copy-check |

### Phase 3 Part 1 — Security & Compliance (skeleton)

| ID | Title | Mission (one line) |
|---|---|---|
| PROM-P3A-01 | Elicit the Functional Baseline | v0: E1.1 requirement cards + PUCs, pure functional, security-free (guidelines §3) |
| PROM-P3A-02 | Map Objectives to the Functional Model | OBJECTIVE_MAPPING / PRINCIPLE_MAPPING verdicts over the v0 model |
| PROM-P3A-03 | Derive Security & Privacy Constraints | per objective: EARS RN proposals with regulatory chain, altitude level, risk addressed (ADR-005) |
| PROM-P3A-04 | Render the Round Register | `ROUNDn_REGISTER.md` + plain-language client proposals (business terms, not raw IDs) |
| PROM-P3A-05 | Absorb Verdicts into Versions | Accept/Reject/Adjust → v1/v2 deltas + functional change register |
| PROM-P3A-06 | Select Controls and Compile the Exit Gate | explicit control selection (Step 4) + G1–G6 evidence bundle |

### Phase 3 Part 2 — Threat & Risk (skeleton; after K3 ingestion)

| ID | Title | Mission (one line) |
|---|---|---|
| PROM-P3B-01 | Model the System, Assets and Boundaries | DFD-level model, assets, trust boundaries (Part 2 Doc01) |
| PROM-P3B-02 | Identify Technical Threats (STRIDE) | per boundary/element threat catalog (Part 2 Doc02) |
| PROM-P3B-03 | Identify Privacy Threats (LINDDUN) | privacy threat catalog (Part 2 Doc03) |
| PROM-P3B-04 | Derive Attack Vectors and Defense Trees | vectors + defense trees (Part 2 Doc04) |
| PROM-P3B-05 | Map Threats to Knowledge Bases | enrichment pass: CWE/CAPEC (+ATT&CK) ledger columns, match-only (ADR-012) |
| PROM-P3B-06 | Build the Risk Register and Governance | scored register + governance actions (Part 2 Doc05); exit G7–G12 evidence |

## 4. Cross-ficha invariants

- **Flag-not-drop:** every negative finding is recorded in the step's artifact with rationale.
- **Anchors are copied, never re-derived** (R2); only pre-verified surfaces are citation sources.
- **Altitude discipline (R13 §2.5):** a statement's specificity never exceeds its source's without a cited warrant (W1–W5).
- **No technology vocabulary** in anything a ficha produces for Phases 0–3 (R5/R13 §2.1); fichas themselves may reference scripts and paths.
- **Every ficha output names its prompt version** in `RUN_NOTES.md` (eval loop traceability).
