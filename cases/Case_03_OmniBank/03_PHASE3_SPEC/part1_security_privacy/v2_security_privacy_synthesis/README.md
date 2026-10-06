# Version 2: Security & Privacy Synthesis (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, Part 1: Security & Compliance
> **Version:** Version 2 (V2) — Round 2 convergence
> **Functional Base:** Phase 3 Version 1 (`../v1_security_privacy_synthesis/`)
> **Status:** APPROVED — Round 2 converged by client directive (2026-09-29); register: [`../synthesis_rounds/ROUND2_REGISTER.md`](../synthesis_rounds/ROUND2_REGISTER.md)

---

## 1. Scope & Purpose of Version 2

Version 2 is the **Round-2 evolution of the Round-1-converged V1**: the Part 1 residual review elevated `R3.3` (coordinated vulnerability disclosure) from SHOULD to **MUST** per `CRA Annex I Part II (5)` (D3, drivers `SO-D-02.3-001`/`SO-D-02.3-002`). The constraint set, chains and use-case behavior are otherwise those of the Round-1-converged V1.

The top-level `Doc01`/`Doc02` in `03_PHASE3_SPEC/` are kept as synced copies of this version (the active working set).

## 2. Directory Contents

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/v2_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 2 and delta from V1
├── ../Doc01_Requirements_Elicitation_and_PUC.md    # 43 cards, RN11–RN26 + 92 chain rows, R3.3 MUST (3.0.0)
└── ../Doc02_System_Use_Cases.md                    # 43 Fully-Dressed Use Cases, matrix aligned (3.0.0)
```

## 3. Key Advancements Over Version 1

| Dimension | Version 1 (Round 1) | Version 2 (Round 2) |
|---|---|---|
| CVD posture | `R3.3` SHOULD | `R3.3` **MUST** (CRA Annex I Part II (5)) |
| Coverage | 128/134 carried | unchanged (elevation, not coverage) |
