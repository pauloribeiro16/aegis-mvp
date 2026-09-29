---
id: 'AEGIS-MVP-ADR-007'
date: 2026-09-28
status: ACCEPTED
decided_by: researcher (working session)
amends: 'ADR-2026-09-24_phase4-threat-analysis-and-iterative-risk-acceptance.md (ADR-005, round proposal payload) · ADR-2026-09-22_goal-objective-structure.md (ADR-003, objective/requirement semantics)'
---

# ADR-007 — Requirement→Objective Fulfillment Semantics: congruence, per-objective discharge and explicit carve-outs

## 1. Status

**ACCEPTED** — decided by the researcher on 2026-09-28, following the Round 2 coverage re-audit of Case_01 (mandated by the approved working plan of the same date). Normative for all future Phase 3 synthesis; applied retroactively to Case_01 as record corrections only (no accepted constraint wording changed).

## 2. The question, stated precisely

Phase 3 maps requirements to Phase 2 objectives many-to-many (co-drivers, absorption). What must be true before an objective may be verdicted as fulfilled by one or more carrier requirements — and what happens to the part of an objective that no product requirement carries?

Evidence (Case_01 Round 2 re-audit, 2026-09-28): of 26 rows verdicted "Covered", 4 are FULL, 20 are PARTIAL (named legs uncarried), 2 are MISMATCH. Identical control-anchor sets had been used as evidence of demand equivalence (e.g., a CRA twin's attack-surface leg absorbed "by twin symmetry"); re-anchoring swapped the driver objective under frozen wording without re-examining it; and no artifact joined a Phase 2 Verification Criterion to the carrier fit criteria that supposedly discharge it.

## 3. Decision

### D1 — Congruence rule (when objectives may share one requirement)

A single requirement (one EARS condition→response pair) may cite multiple Phase 2 objectives as drivers **only if every cited objective is satisfied by that same condition→response**. Objectives demanding different system responses get separate requirements. Identical published control-anchor sets do **not** evidence demand equivalence — anchors constrain the fourth chain link (controls), never the first (behavior).

### D2 — Discharge rule (what "covered" means)

An objective is **fully covered** only when the union of its carriers' Volere fit criteria reconstitutes the objective's Phase 2 Verification Criterion, and every demand leg of its Operational Statement is either carried, recorded as out-of-scale (with warrant), or routed by D4. Placement of an RN name next to an objective is not fulfillment. Every coverage verdict in the case's `synthesis_rounds/OBJECTIVE_MAPPING.md` carries a **discharge record**: which carrier fit criteria discharge which legs, and the explicit status of every uncarried leg.

### D3 — The coverage matrix is the authoritative discharge graph; card chains cite primary drivers

The many-to-many graph lives in `synthesis_rounds/OBJECTIVE_MAPPING.md` (and per-principle in `PRINCIPLE_MAPPING.md`). Delivered requirement-card chains continue to cite the card's primary drivers only (card economy: typically 1–3 constraints per card, guidelines §3.3). A carrier serving another objective transversally is recorded as a **cross-reference in the matrix**, not added to every card chain. Re-anchoring a chain to a different driver objective is a baseline change requiring a round verdict (ADR-005) and must re-examine the frozen wording and fit criterion against the new driver's demands — wording is never grandfathered across a driver swap.

### D4 — Explicit carve-outs; the organizational lane is the sink

A leg no product requirement carries is never silently "covered". It is routed, in the discharge record, to exactly one of:

- **a) organizational lane** — becomes an input row of the Phase 3 organizational requirements deliverable (ADR-008) or remains a recorded organizational decision;
- **b) out-of-scale** — recorded interpretation with the company-scale warrant (R13);
- **c) design guidance** — Phase 4 context;
- **d) proposal** — a new or adjusted requirement, tabled in the round register, pending the client verdict (ADR-005).

Matrix verdict vocabulary: `Fully covered` / `Partially covered (functional leg + explicit carve-out)` / `No functional carrier (organizational)` / `Design guidance` / `N/A`.

### D5 — Fit criteria are part of the accepted formulation

Every accepted carrier — including V0-inherited NFRs and functionally elevated cards — must have a Volere fit criterion in the round dossier. Delivered-wording drift between the formulation dossier and the delivered specification is a defect: the register's formulation is authoritative, and repairs go through a round item.

Round proposals gain one mandatory payload field: the **discharge statement** — which legs of each cited driver this requirement's fit criterion discharges.

## 4. Consequences

- "Covered by name" verdicts are no longer legal. Case_01's matrix now separates **6 fully covered**, **19 partially covered** (with named carve-outs) and **32 organizational** rows (including `PO-D-09.4-001`, re-verdicted from Covered: an Art. 30 register is a documentary obligation; the privacy event trail RN26 is supporting evidence, not the register).
- The organizational lane acquires a derived deliverable (ADR-008) instead of verdict strings.
- Phase 4 (Verification & Implementation) inherits a per-objective discharge record — the join between Phase 2 Verification Criteria and requirement fit criteria it would otherwise have to reconstruct.
- Round proposals gain the discharge statement field (D5); re-anchoring gains the re-examination obligation (D3).

## 5. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| One requirement per objective (1:1 mapping) | Inflates the repertoire (62 objectives → 62+ security requirements), contradicts the card anatomy economy and the sea-level granularity rules; congruence + discharge give the same guarantee without the inflation. |
| Keep name-linkage; add a per-objective verification pass in Phase 4 | Defers the guarantee to a phase with no designed verification machinery; the gap is a specification defect, not a test defect. |
| Require every cross-carrier reference inside the delivered card chains | Bloats cards beyond the 1–3-constraint economy and duplicates the matrix; the matrix is the discharge graph of record. |

## 6. References

- `templates/phase3_functional_spec_guidelines.md` §3.5 (codified procedure)
- Case_01 `synthesis_rounds/ROUND2_REGISTER.md` (re-audit record corrections + pending proposals)
- ADR-005 (round semantics), ADR-008 (organizational lane), ADR-003 (objective schema, `realization_class`)
