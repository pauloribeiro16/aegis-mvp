# Version 2: Security & Privacy Synthesis (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, Part 1: Security & Compliance  
> **Version:** Version 2 (V2) — Round 2 convergence  
> **Functional Base:** Phase 3 Version 1 (`../v1_security_privacy_synthesis/`)  
> **Status:** APPROVED — Round 2 converged by client directive (2026-09-29); register: [`../synthesis_rounds/ROUND2_REGISTER.md`](../synthesis_rounds/ROUND2_REGISTER.md)

---

## 1. Scope & Purpose of Version 2

Version 2 is the **Round-2 evolution of the Round-1-converged V1**: the sufficiency assessment's MoSCoW posture review elevated `R9.3` (adversarial testing of the high-risk verification AI) from SHOULD to **MUST** per `AI Act Art. 9(6)-(7)` (D3, driver `SO-D-02.4-004`), and the Doc02 traceability matrix was aligned (`R7.3` MUST). The constraint set, chains and use-case behavior are otherwise those of the Round-1-converged V1.

The top-level `Doc01`/`Doc02` in `03_PHASE3_SPEC/` are kept as synced copies of this version (the active working set).

## 2. Directory Contents

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/v2_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 2 and delta from V1
├── Doc01_Requirements_Elicitation_and_PUC.md    # 28 cards, RN11–RN30, R9.3 MUST (3.0.0)
└── Doc02_System_Use_Cases.md                    # 28 Fully-Dressed Use Cases, matrix aligned (3.0.0)
```

## 3. Key Advancements Over Version 1

| Dimension | Version 1 (Round 1) | Version 2 (Round 2) |
|---|---|---|
| AI testing posture | `R9.3` SHOULD | `R9.3` **MUST** (AI Act Art. 9(6)-(7)) |
| Matrix consistency | Doc02 `R7.3` row stale (SHOULD) | Aligned to MUST |
| Coverage | 92/100 carried | unchanged (elevation, not coverage) |
