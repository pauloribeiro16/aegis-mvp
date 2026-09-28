# Version 1: Security & Privacy Synthesis (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 1: Security & Compliance**  
> **Version:** Version 1 (V1) — Round-Converged Security & Privacy Synthesis (ADR-005: rounds from the start)  
> **Upstream Inputs:** Phase 2 Operational Objectives (100: 29 `PO-` GDPR / 34 `SO-` CRA / 22 `SO-` NIS 2 / 15 `SO-` AI Act) & 7 Secure Design Principles · exhaustive coverage matrix (`../synthesis_rounds/OBJECTIVE_MAPPING.md`)  
> **Functional Base:** Phase 3 Version 0 (`v0_functional_baseline/`)  
> **Status:** APPROVED — Round 1 converged with 20/20 constraint accepts + 51/51 chain-binding accepts (2026-09-28); register: [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md)

---

## 1. Scope & Purpose of Version 1

Version 1 is the **round-converged security & privacy synthesis** of the V0 functional baseline: every one of the 100 Phase 2 objectives and all 7 principles was mapped against the functional model, every gap became a proposal, the client gave per-batch verdicts in plain business language, controls were explicitly selected post-convergence, and the accepted set was absorbed into the deliverables. Unlike Case_01 (grandfathered one-shot V1), this V1 was produced by the full ADR-005 round cycle from the start.

The top-level `Doc01`/`Doc02` in `03_PHASE3_SPEC/` are kept as synced copies of this version (the active working set).

---

## 2. Directory Contents

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/v1_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 1 and delta from V0
├── Doc01_Requirements_Elicitation_and_PUC.md    # 28 Functional Cards + absorbed constraints RN11–RN30 + 51 chain rows
└── Doc02_System_Use_Cases.md                    # 28 Fully-Dressed Sea-Level Use Cases with accepted security behavior
```

---

## 3. The 2 Artifacts of Version 1

### 3.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
Carries the accepted baseline — 28 requirement cards and 28 Product Use Cases unchanged in function — with:
- **Absorbed `Security & Privacy Constraints` rows on 27 cards:** 20 new constraints (`RN11`–`RN30`: biometric crypto, key custody, transit, integrity, AI resilience/logging/post-market/oversight/transparency, identity lifecycle, MFA, role mediation, secure defaults, unified notification timelines, tamper-evident recording, incident lifecycle, breach awareness, secure updates, erasure/portability) + 51 chain rows (`**Chain** …`) binding existing functions to their regulatory objectives.
- **Table 7** gains the cross-cutting transport row `RN13`.
- **T-001..T-004** harmonizations realized (unified notification clock, token-only erasure vs AI logs, unified assessments, unified vendor pass).
- **Functional Evolution Register:** evaluated, no change (STEP5) — the functional set already covered the required scope.

### 3.2 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
All 28 use cases elaborated to the **fully-dressed Cockburn anatomy** with the accepted security behavior:
- **Security preconditions** (authenticated sessions, verified models, competence records, protected channels).
- **Security extensions** (fail-closed gate states, rollback, refusal and lockout flows, tamper alerts, clock-start discipline).
- **Guarantees** (non-repudiable records, token-only decision records, no plaintext biometric content).
- Traceability matrix with bound NFRs per requirement.

---

## 4. Key Advancements Over Version 0

| Dimension | Version 0 (Baseline) | Version 1 (Round 1) |
|---|---|---|
| Objective coverage | functions elicited without regulatory chains | 92/100 objectives carried (39 RN + 51 chain + 2 transversal); 2 organizational + 6 N/A recorded |
| Constraint set | `RN1`–`RN10` quality attributes | `RN1`–`RN13` (+`RN11`–`RN30` in-card) across 4 regulatory ambits |
| Use cases | light format (Actor/Goal/Scope) | fully-dressed Cockburn with accepted security behavior |
| Tensions | pre-harmonized upstream | realized: T-001 (RN21), T-002 (RN24+RN28), T-003 (R10.1 family), T-004 (R10.2 family) |
| Control selection | none | explicit Step-4 selections from published sets + store (`ROUND1_REGISTER.md` §3) |
| Client decisions | functional acceptance only | per-batch risk-acceptance verdicts (20/20 + 51/51) |
