---
document_id: AEGIS-MVP-ADR-003
title: 'Goal vs Objective structure — literature-grounded card schemas for Phase 1 and Phase 2'
status: 'PROPOSED — awaiting human ratification (P7); MVP-side application pre-approved by the researcher'
date: 2026-09-22
phase: 'Phase 1 + Phase 2 (cross-repo: aegis-mvp applied; Methodology_compact deferred)'
author: 'Decision: PhD researcher (scope + depth, 2026-09-22); analysis + literature: Executor session'
---

# ADR-003 — What a Goal is, what an Objective is: literature-grounded structures for Phases 1–2

> **Why this document exists.** The researcher asked (2026-09-22): *"Como deve ser a estrutura de um goal, a estrutura de um objective? A literatura diz como se escrevem goals e objectives de segurança? A fase 1 é goals e a fase 2 é objectives — investiga a fundo."* This ADR registers the literature findings, the proposed canonical structures, and the terminology resolutions. The **aegis-mvp side is applied immediately** (researcher pre-approval, same day); the **Methodology_compact side is registered as deferred campaigns** awaiting ratification.

---

## 1. Status

**PROPOSED** for the methodology-level definitions (P7); the aegis-mvp application (template, golden example, SPEC) was explicitly approved by the researcher on 2026-09-22 and is **already applied** in this same commit series. Ratification checklist in §9.

---

## 2. Current state — what the repositories hold today (evidence)

### 2.1 The layers as they exist

| Layer | Artifact | Anatomy today |
|---|---|---|
| Phase 0 (frozen) | `D-XX.Y/objective.md` — HSO `SO-D-XX.Y.HL` | YAML block (`id`, `subdomain`, `applies_to`, `status`, `derivation_source`, `verified_relationship_basis`, `emergent_tensions`) + `**Objective.**` prose statement |
| Phase 1 (MVP) | `templates/phase1_output.md` §4 — AG `AG-D-XX.Y-NNN` | 4-column table row: ID, Adjusted goal (free prose), Regulatory source, Control anchor (+ §4.1 anchor-mapping row). No rationale/adjustment/parent fields — proportionality lives only in phrasing; ambiguity links live in §5 |
| Phase 1 (case) | `Case_01/01_PHASE1_CONTEXT_RICH/Doc13_Adjusted_Goals.md` | 6-column rows: Sub-Domain, AO ID (uses **AG-**), statement + inline `*Adjustment (TinyTask): …*`, Tier, Priority, Source |
| Phase 2 (case) | `Case_01/02_PHASE2_RULES_RICH/Doc16_…Objectives.md` — PO/SO `PO-/SO-D-XX.Y-NNN` | Cards with **20 numbered fields** while the document itself declares **15**; header carries ~26 lines of per-card audit residue ("Fase de Especificação 5 …") |

### 2.2 The structural defects the re-specification resolves

1. **No statement-quality standard anywhere** above the frozen corpus `fit_criterion` (Volere): no measurability, verifiability, or writing rules for AG or PO/SO. Measurability was pushed entirely to Phase 3 ("translate 'appropriate technical measures' → 'AES-256'"), contradicting ISO 27001 6.2, which demands measurability at the *objective* layer.
2. **Schema drift**: Doc16 says 15 fields, carries 20; AG has 4 columns with no parent link, no adjustment record, no classification.
3. **Terminology divergence at every seam**: prefix `AG-` (cases, de-facto canonical, P7-arbitrated 2026-08-27) vs `AO-` (MC canon: `AGENTS.md` corr-008, `dependency_graph.yaml`); flow doc `phase2c_goals_and_rules.md` is 100% "goal"-speak (95 vs 0) while Doc16 is "objective"-speak (161 vs 67); Phase-2 class model says `PrivacyGoal`/`SecurityGoal` (3 thin attributes) while the case artifact says "Privacy/Security Operational Objectives" (20-field cards); "objective" is overloaded between the frozen Phase-0 HSO and the Phase-2 output unit; `SPEC.md` R5 = Language vs `AGENTS.md` R5 = Technology Neutrality (rule-number collision).
4. **No `AdjustedGoal` class** exists in the Phase 1 class model (only a "AdjustedGoal pool" flow node).

---

## 3. Literature findings (what the literature says a security goal / objective is)

### 3.1 Goal-Oriented Requirements Engineering (KAOS — van Lamsweerde)

- A **goal** is a *prescriptive statement of intent*, refined (AND/OR) through sub-goals until it becomes a requirement — *"requirements are goals at the level of the system"*; goals assigned to human agents are *expectations*.
- Goals are classified by **satisfaction pattern**: **achieve** (target condition eventually true), **cease** (bad condition eventually terminated), **maintain** (good condition kept continuously true), **avoid** (bad condition never occurs), **optimize** (maximize/minimize a criterion).
- **Hardgoal** (clear-cut satisfaction criterion) vs **softgoal** (no clear-cut criterion — e.g., "adequate security").

Sources: van Lamsweerde, *Goal-Oriented Requirements Engineering: A Guided Tour* (RE'01); *Requirements Engineering: From System Goals to UML Models to Software Specifications* (Wiley 2009); [Lapouchnian survey 2005](https://www.cs.utoronto.ca/~grandy/papers/surveys.html); [Horkoff et al. 2017 extended survey](https://link.springer.com/article/10.1007/s10606-017-9296-5).

### 3.2 Management science (Doran 1981 — the SMART origin)

- **Goals** = broad, directional aims, *not necessarily quantifiable*; **objectives** = the specific, quantifiable statements to which **S**pecific/**M**easurable/**A**ssignable/**R**ealistic/**T**ime-related applies. Doran's original distinction — "SMART *goals*" is a later conflation; SMART was a discipline for *objectives*.

Sources: Doran, "There's a S.M.A.R.T. Way to Write Management's Goals and Objectives", *Management Review* 70:35–36 (1981); [Bjerke & Renger 2017](https://www.sciencedirect.com/science/article/abs/pii/S0149718916302433).

### 3.3 ISO/IEC 27001:2022 clause 6.2 (normative doctrine for security objectives)

Information security objectives must be **consistent with the policy, measurable (where practicable), take into account applicable requirements and risk-assessment results, be monitored, communicated, updated, and available as documented information**; the organization determines **what** will be done, **what resources**, **who** is responsible, **when** it will be completed, and **how the results will be evaluated**.

Source: [ISO/IEC 27001:2022 clause 6.2](https://www.hightable.io/blog/iso-27001-clause-6-2-information-security-objectives) (and 6.2 in the 2013 edition).

### 3.4 Common Criteria (ISO/IEC 15408) — the structural precedent

PP/ST chain: **Security Problem Definition** (threats `T.*`, organizational security policies `P.*`, assumptions `A.*`) → **Security Objectives** (`O.*` for the TOE, `OE.*` for the operational environment) → **Security Requirements** (SFRs/SARs), with **bidirectional rationale tables** proving every threat/policy/assumption is covered by ≥1 objective and every objective by ≥1 requirement. Objectives are "statements of intent to counter identified threats and/or satisfy identified organizational security policies and assumptions".

Mapping to AEGIS: Phase 0 corpus ≈ PP (reusable, environment-generic); Phase 2 objectives ≈ CC security objectives; Phase 3 rules ≈ SFRs; the gates ≈ CC rationale tables.

Source: ISO/IEC 15408-1:2022 Part 1 (PP/ST model), [commoncriteriaportal.org](https://www.commoncriteriaportal.org).

### 3.5 Secure Tropos (Mouratidis & Giorgini) and SQUARE (CMU SEI)

- Secure Tropos distinguishes **security constraints** (restrictions imposed on an actor/goal — e.g., by law) from **secure goals** (goals *introduced to satisfy* those constraints): exactly the AEGIS derivation step "regulation article → adjusted goal".
- SQUARE makes "identify security goals" an explicit elicitation step before requirements.

Sources: [Mouratidis & Giorgini, Secure Tropos](https://www.researchgate.net/publication/221553550_Secure_Tropos_A_Security-Oriented_Extension_of_the_Tropos_Methodology); [Mead & Stehney, SQUARE (CMU SEI)](https://www.sei.cmu.edu); Firesmith, "Engineering Security Requirements", *JOT* (2003).

### 3.6 NIST SP 800-160 Vol. 1 (systems security engineering)

Hierarchy: protection needs & concerns → **stakeholder security objectives** → stakeholder security requirements → system security requirements. AEGIS Phase 1's company-adapted goal layer plays precisely the "stakeholder security objectives" role; Phase 2 the operational-objective layer; Phase 3 the requirements layer.

Source: [NIST SP 800-160 Vol. 1/2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

### 3.7 Property taxonomy (Avizienis–Laprie–Randell–Landwehr 2004)

Security = composite of **confidentiality, integrity, availability** (against intentional adverse actions); the canonical attribute set for classifying *what a goal protects*. Privacy (data-subject rights) is deliberately **not** in the CIA triad — it is a separate axis, which legitimizes AEGIS's privacy/security split and an explicit property attribute on goal cards.

Source: [Avizienis, Laprie, Randell, Landwehr, "Basic Concepts and Taxonomy of Dependable and Secure Computing", IEEE TDSC 2004](https://ieeexplore.ieee.org/document/1335465).

### 3.8 Statement-writing quality (INCOSE / ISO 29148)

Individual statements should be **Necessary, Appropriate, Singular, Unambiguous, Complete, Feasible, Verifiable** — verifiable via *inspection, analysis, demonstration, test* (the exact four methods AEGIS already uses in Doc16 field 8 and Phase 3). ISO 29148 adds: requirements/constraints state *what*, not *how* (design decisions excluded).

Sources: [INCOSE Guide to Writing Requirements](https://www.incose.org); ISO/IEC/IEEE 29148:2018.

**Convergence summary:** four independent literatures (GORE, management, security engineering, certification) agree on the same two-layer shape: **goal = directional intent, refined downward, not directly verified**; **objective = operationalized, verifiable, owned, measurable intent that counters identified threats/satisfies identified obligations**. AEGIS's Phase 1 = Goals / Phase 2 = Objectives division is therefore literature-correct; what is missing is the explicit schema and writing discipline per layer.

---

## 4. Decision (proposed)

### D1 — Adjusted Goal card structure (Phase 1 — stays deliberately light)

A Phase 1 goal is a **directional, prescriptive statement of intent** introduced to satisfy regulatory security constraints (Secure Tropos sense), proportionally adapted to the company (R3), whose satisfaction is achieved by *refinement into Phase 2 objectives* — never by direct verification (Doran; KAOS softgoal discipline). Per-goal card = table row with **8 columns**:

| # | Column | Content | Source |
|---|---|---|---|
| 1 | ID | `AG-D-XX.Y-NNN` | R4 (unchanged) |
| 2 | Adjusted goal | One directional sentence, technology-neutral, target-state | R3/R5 (unchanged) |
| 3 | Pattern | `achieve \| cease \| maintain \| avoid \| optimize` | KAOS satisfaction patterns (§3.1) |
| 4 | Property | `C \| I \| A \| privacy-right \| accountability` | Avizienis taxonomy + privacy axis (§3.7) |
| 5 | Parent goal | `SO-D-XX.Y.HL` (the frozen sub-domain **Baseline Goal**; legacy "HSO" — ADR-004) | refinement link (KAOS refinement tree) |
| 6 | Regulatory source | `REG Art. N` list | R2a (unchanged) |
| 7 | Control anchor | ≤2 referential IDs or `—` | R2b (unchanged) |
| 8 | Adjustment | One-line explicit record of what was restated vs the corpus HSO — no silent relaxation | R3 made auditable (Doc13's inline `*Adjustment:*` practice, promoted to a field) |

**Deliberately absent**: owner, verification criteria, cadence, status — these belong to objectives (Doran: SMART applies to objectives, not goals; a goal with a verification criterion is a mis-layered objective).

### D2 — Operational Objective card schema (Phase 2 — canonical ~14 fields)

A Phase 2 Privacy/Security Operational Objective is a **verifiable operational statement** derived from ≥1 goal and ≥1 obligation, countering identified threats / satisfying identified obligations (CC sense), written under ISO 27001 6.2 discipline. Canonical schema:

| # | Field | ISO 6.2 / INCOSE determination |
|---|---|---|
| 1 | ID (`PO-/SO-D-XX.Y-NNN`) | — |
| 2 | **Statement** | singular, unambiguous, verifiable (INCOSE); *what*, not *how* (29148) |
| 3 | Parent goal(s) + source obligation(s) | traceability (CC rationale-table discipline) |
| 4 | Scope | what the objective covers |
| 5 | Out of scope | boundary + proportionality exclusions |
| 6 | Regulatory basis | the constraints satisfied (articles; T2/T3 citations per ADR-001 D2) |
| 7 | Anchors | CSF 2.0 / PF 1.1 / AI RMF (pre-verified surfaces only) |
| 8 | **Verification criteria** | *how results will be evaluated* — no vague language ("appropriate" banned at this layer) |
| 9 | **Verification method** | one of `TEST / INSPECT / DEMONSTRATE / ANALYZE` (INCOSE; already AEGIS practice) |
| 10 | **Owner** | *who is responsible* (Doran: assignable) |
| 11 | **Cadence / when** | *when* — review/verification cadence or deadline (Doran: time-related) |
| 12 | Dependencies | related objectives/rules/obligations |
| 13 | Risk if not met | risk-assessment linkage (ISO 6.2: "taking into account risk assessment results") |
| 14 | `realization_class` + posture | enum from REALIZATION_CLASS_RUBRIC; MVP = TECHNOLOGY-only per ADR-002; posture = IMPLEMENTED/PARTIAL/NOT IMPLEMENTED |

Everything else a case needs (affected stakeholders, regulatory reporting, external auditor, supervisory body, implementation examples, Phase-1 controls reference) is an **optional case-annotation block below the schema** — real content, but not schema cells, and never audit-process residue ("Fase de Especificação 5" metadata is banned from the schema).

### D3 — Statement-writing rules per layer

- **Goal (F1)**: one sentence; directional; technology-neutral (no vendor/product/tool); states the protected condition, not the mechanism; ambiguity clauses cited, never re-resolved (R7); the pattern and property columns classify it — they are not prose elements.
- **Objective (F2)**: satisfies the five ISO 6.2 determinations (what / resources / who / when / how evaluated); singular and unambiguous; **"no vague language" descends from Phase 3 to the F2 verification criteria** — a verification criterion containing "appropriate", "reasonable", "adequate" without a measure is a defect. Phase 3 keeps full quantification ("AES-256 for data at rest") — the descent stops at the boundary: F2 says *which property is verified and how*, F3 says *the value*.
- **Rule (F3)**: unchanged — quantified, testable requirements (current Phase 3 criteria already apply).

### D4 — Terminology resolutions

1. **`AG-` is canonical** for Phase 1 IDs (ratifies the de-facto P7 arbitration of 2026-08-27 documented in `phase1_rich_extension.md` open item 2). The MC canon (`AO-D-`) is the deviation to be fixed — campaign C4.
2. **Layer nouns are fixed**: Phase 0 = **Baseline Goals** (concept level, per [ADR-004](ADR-2026-09-22_pipeline-io-contract.md); frozen artifact names/IDs stay — `objective.md`, `SO-D-XX.Y.*` — under ADR-004's alias table); Phase 1 = **Adjusted Goals**; Phase 2 = **Privacy/Security Operational Objectives**; Phase 3 = **Requirements**. *(Amended 2026-09-22: this clause originally documented the F0 "objective" overload as permanent; ADR-004 resolved it — "objective" starts at Fase 2.)*
3. **Phase-2 class model renames**: `PrivacyGoal`/`SecurityGoal` → `PrivacyObjective`/`SecurityObjective`, with the D2 attributes (campaign C4); Phase 1 gains an `AdjustedGoal` class (D1 columns), linked to `HierarchicalSecurityObjective` by refinement.
4. **`phase2c_goals_and_rules.md`** language aligned to "objective" for the PO/SO layer (campaign C4).
5. **R5 collision**: `SPEC.md` R5 (Language) is renumbered in a future SPEC revision; technology neutrality stays `R5` per AGENTS (campaign C5). Until then, any citation of "R5" must name its document.

### Why this decision (the re-readable rationale)

1. **The two-layer division was right before it could be justified.** Four independent literatures converge on goal = directional/soft, objective = verifiable/owned. The re-specification does not invent a structure — it names the one the methodology already implicitly follows (Doc13's inline adjustments, Doc16's SMART-compatible fields) and fixes the seams.
2. **Lightness of the AG card is principled, not laziness.** Doran and KAOS both put verification/ownership *below* the goal layer. Converting AGs into full cards would blur the refinement semantics (a goal with its own test is an objective) and double the maintenance cost without adding regulatory value.
3. **The objective layer was over-built and under-specified at once.** 20 fields with no stated standard; the fix is *fewer* schema fields (14) plus *explicit* writing discipline (ISO 6.2 + INCOSE) — schema shrinks, rigor grows.
4. **KAOS patterns and the property attribute make goals mechanically auditable** (§8 checklist items) while staying one-word cheap; they also pre-dispose Phase 2 verification style (maintain/avoid goals → continuous monitoring objectives; achieve/cease → event-driven objectives).

---

## 5. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| **Unify both layers as full cards (12+ fields each)** | Contradicts Doran (goals are directional; owner/verification is objective-layer discipline) and KAOS (goals are refinement nodes, not verification units). Would double authoring cost per goal and blur the layer semantics the methodology's own ID convention (R4) asserts. |
| **Status quo (4-column AG, 20-field PO/SO, no writing rules)** | Keeps schema drift (15 vs 20), leaves ISO 27001 6.2 unsatisfied at the objective layer, and keeps the terminology divergence that three docs already flag as known debt. |
| **Rename the Phase-0 HSO layer to remove the "objective" overload** | Mutates the frozen read-only corpus for cosmetic gain; the namespaces never collide (`SO-D-XX.Y.HL` vs `PO-/SO-D-XX.Y-NNN`); documented distinction is sufficient. |

---

## 6. Consequences — campaigns

- **C1 (MVP) — EXECUTED 2026-09-22 (researcher pre-approved):** `templates/phase1_output.md` §4 gains the D1 columns (Pattern, Property, Parent HSO, Adjustment); `example/phase1_output.md` regenerated (6 AG rows); `SPEC.md` P4/§6/§8 updated (writing rules + checklist items).
- **C2 (MVP, next run)** — first new Phase 1 run executed on the D1 template end-to-end; golden-example diff reviewed.
- **C3 (MC, after ratification)** — Doc16 PO/SO cards normalized to the D2 schema (14 fields + case-annotation block); audit residue removed from card headers; document's "15 fields" claim corrected.
- **C4 (MC, after ratification)** — terminology sweep: `AO-D-` → `AG-D-` in `00_METHODOLOGY/AGENTS.md` corr-008 table and `dependency_graph.yaml`; class models (add `AdjustedGoal`; rename `PrivacyGoal`/`SecurityGoal` and enrich attributes); `phase2c_goals_and_rules.md` objective-speak. P5 impact check via `scripts/kg.sh` before each ID-namespace edit.
- **C5 (MVP, after ratification)** — SPEC rule renumbering resolving the R5 collision; SPEC §6 absorbs D3 writing rules verbatim.
- **C6 (MC)** — traceability chain vocabulary (`MAPPINGS/traceability/`, README chain diagrams) updated to name the AG node explicitly: regulation → article → ambiguity clause → HSO → Sub-SO → **AG (goal)** → PO/SO (objectives) → RULE → control.

## 7. What this ADR deliberately does not do

No edits to Methodology_compact, `baseline/`, or any case. No changes to Phase 0 HSO cards. No Phase 2 pipeline built. The MC campaigns (C3–C6) start only after §9 ratification.

## 8. Interaction with ADR-001, ADR-002, and the M9 designations campaign

- ADR-001 (best-practice layer): objective regulatory-basis citations follow the ADR-001 tier model (T1/T2/T3 + version).
- ADR-002 (MVP TECHNOLOGY-only): the D2 field 14 `realization_class` will carry only `TECHNOLOGY` in MVP-produced objectives; PROCESS/CAPABILITY remain full-methodology.
- **Designations campaign (M9/M9b/M9c, 2026-09-22, parallel session):** the researcher's own convention — *Phase 1 = Goals (`AG-`), Phase 2 = Objectives, Phase 3 = Requirements; "AO" label retired* — was already applied to repo docs and cases. This **confirms D4.1/D4.2 as decided, not merely proposed**; the residual C4 scope is therefore only the MC methodology-core sweep (`00_METHODOLOGY/AGENTS.md` corr-008 table, `dependency_graph.yaml`, class models, `phase2c` flow doc) — verify current state before executing.
- **ADR-004 (pipeline I/O contract, 2026-09-22):** extends the designation chain to Fase 0 — *regulation in → **Baseline Goals** out* — and makes this ADR's card schemas the format of each phase exchange (D1 columns for F0→F1, D2 schema for F1→F2). D4.2 above is amended accordingly.

## 9. Ratification checklist (P7)

1. Adopt D1 (8-column AG card; no owner/verification at goal layer) — yes / amend: ______
2. Adopt D2 (14-field PO/SO schema + case-annotation block) — yes / amend: ______
3. Adopt D3 (writing rules; vague-language ban at F2 verification criteria) — yes / amend: ______
4. Adopt D4.1 (AG canonical over AO) — yes / amend: ______
5. Adopt D4.3/D4.4 (class-model renames + phase2c sweep) — yes / defer: ______
6. Campaign order (recommended: C3 → C4 → C5 → C6) — order: ______

## 10. References

- van Lamsweerde (2001, 2009) — KAOS; [Lapouchnian survey](https://www.cs.utoronto.ca/~grandy/papers/surveys.html); [Horkoff et al. 2017](https://link.springer.com/article/10.1007/s10606-017-9296-5)
- Doran (1981), *Management Review* 70:35–36; [Bjerke & Renger 2017](https://www.sciencedirect.com/science/article/abs/pii/S0149718916302433)
- [ISO/IEC 27001:2022 §6.2](https://www.hightable.io/blog/iso-27001-clause-6-2-information-security-objectives)
- ISO/IEC 15408-1:2022 (CC Part 1, PP/ST model), [commoncriteriaportal.org](https://www.commoncriteriaportal.org)
- [Mouratidis & Giorgini — Secure Tropos](https://www.researchgate.net/publication/221553550_Secure_Tropos_A_Security-Oriented_Extension_of_the_Tropos_Methodology); [SQUARE (CMU SEI)](https://www.sei.cmu.edu); Firesmith (2003), *JOT*
- [NIST SP 800-160 Vol. 1/2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final)
- [Avizienis, Laprie, Randell, Landwehr (2004), IEEE TDSC](https://ieeexplore.ieee.org/document/1335465)
- [INCOSE Guide to Writing Requirements](https://www.incose.org); ISO/IEC/IEEE 29148:2018
- Repository evidence: §2 of this document, with file citations.
