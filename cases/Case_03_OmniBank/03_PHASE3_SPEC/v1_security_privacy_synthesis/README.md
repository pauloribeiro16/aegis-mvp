# Version 1: Security & Privacy Synthesis (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, Part 1: Security & Compliance
> **Version:** Version 1 (V1) — Round-Converged Security & Privacy Synthesis (ADR-005: rounds from the start)
> **Functional Base:** Phase 3 Version 0 (`../v0_functional_baseline/`)
> **Status:** APPROVED — Round 1 converged 16/16 + 92/92 accepts by client directive (2026-09-29); register: [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md)

---

## 1. Scope & Purpose of Version 1

Version 1 is the **round-converged security & privacy synthesis** of the V0 functional baseline: all 134 Phase 2 objectives and the 7 principles were mapped against the functional model, the gaps became proposals, the client accepted all five plain-language batches by directive, controls were explicitly selected post-convergence, and the accepted set was absorbed.

The top-level `Doc01`/`Doc02` in `03_PHASE3_SPEC/` are kept as synced copies of this version.

## 2. Directory Contents

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/v1_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 1 and delta from V0
├── Doc01_Requirements_Elicitation_and_PUC.md    # 43 Functional Cards + absorbed constraints RN11–RN26 + 92 chain rows
└── Doc02_System_Use_Cases.md                    # 43 Fully-Dressed Sea-Level Use Cases with accepted security behavior
```

## 3. The 2 Artifacts of Version 1

### 3.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
- **Absorbed `Security & Privacy Constraints` rows on 36 of 43 cards:** 16 new constraints (`RN11`–`RN26` — OmniScore decision/model integrity, scoring minimization, transit, at-rest field-level encryption, key custody separation, rights-requester verification, token-only retention, unified notification clock, privileged MFA, secure defaults, AI-platform least privilege, human oversight, AI logging, post-market monitoring, adversarial robustness, ICT third-party register) + 92 chain rows; multi-regulation chains cite all demanding objectives on one line.
- **Table 7** gains the cross-cutting transport row `RN13`.
- **Functional Evolution Register:** evaluated, no change (STEP5).

### 3.2 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
All 43 use cases elaborated to the **fully-dressed Cockburn anatomy** with the accepted security behavior; traceability matrix with bound NFRs; T-001..T-005 harmonizations realized ({U.C. 5.2} unified clock, {U.C. 6.3} token-only erasure, {U.C. 10.2} unified assessments, {U.C. 7.1} register).

## 4. Key Advancements Over Version 0

| Dimension | Version 0 | Version 1 (Round 1) |
|---|---|---|
| Objective coverage | functions elicited without chains | 128/134 carried (36 RN + 92 chain); 2 DPO organizational + 4 N/A recorded |
| Constraint set | `RN1`–`RN10` | `RN1`–`RN13` (+`RN11`–`RN26` in-card) across five regulatory ambits |
| Use cases | light format | fully-dressed Cockburn with accepted security behavior |
| Control selection | none | explicit Step-4 selections from published sets + store |
| Client decisions | functional acceptance only | per-batch verdicts (16/16 + 92/92) |
