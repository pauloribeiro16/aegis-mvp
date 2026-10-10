# Version 2: Security & Privacy Synthesis (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification (Part 1: Security & Compliance)  
> **Version:** Version 2 (V2) — Security & Privacy Synthesis, Round 1  
> **Upstream Inputs:** Phase 2 Operational Objectives (`Doc01`) & Secure Design Principles (`Doc02`) · exhaustive coverage matrix (`../synthesis_rounds/OBJECTIVE_MAPPING.md`)  
> **Functional Base:** Phase 3 Version 1 (`part1_security_privacy/v1_security_privacy_synthesis/`)  
> **Status:** APPROVED — Round 1 converged with 13/13 client accepts (2026-09-28); register: [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md)

---

## 1. Scope & Purpose of Version 2

Version 2 is the **risk-accepted evolution of the Version 1 synthesis** produced by the first full round of the iterative risk-acceptance cycle (ADR-005): the exhaustive coverage matrix (`62/62` Phase 2 objectives + `7/7` principles) was juxtaposed against the approved V1, every gap became a proposal, the client gave a per-item verdict, controls were explicitly selected post-convergence, and the accepted set was absorbed into the deliverables.

The top-level `Doc01`/`Doc02` in `03_PHASE3_SPEC/` are kept as synced copies of this version (the active working set).

---

## 2. Directory Contents

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/v2_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 2 and delta from V1
├── ../Doc00_Process_and_Operational_Workflows.md # Business context, process model, trust zones, PUC catalog
├── ../Doc01_Requirements_Specification.md       # 20 Functional Cards (19 + R8.3 derived) + realigned constraint chains + RN27–RN30
└── ../Doc02_System_Use_Cases.md                    # 20 Sea-Level Use Cases (incl. {U.C. 8.3}) with identity-verification and secure-default flows
```

---

## 3. The 2 Artifacts of Version 2

### 3.1 [`../Doc01_Requirements_Specification.md`](../Doc01_Requirements_Specification.md)
Carries the accepted baseline — 20 requirement cards (`R1.1` to `R8.3`, including `R8.3` derived in Round 1) — with:
- **Realigned constraint chains (11 RNs):** every absorbed constraint now cites its natural Phase 2 objective, with anchors belonging to that objective's published control set (ADJ-1…ADJ-9).
- **New constraints:** `RN27` requester identity verification for rights exercise (`R8.1`/`R8.2`), `RN28` secure-by-default configuration (`R2.1`/`R3.1`), `RN30` workspace permanent removal (in-card on `R8.3`), `RN29` secure-use instructions (Table 7, SHOULD).
- **Derived requirement `R8.3` (D1):** delete workspace and permanently erase workspace data, with matching `PUC 8.3`.
- Version History 4.0.0.

### 3.2 [`../Doc02_System_Use_Cases.md`](../Doc02_System_Use_Cases.md)
Maintains Cockburn's Sea-Level granularity across 20 System Use Cases (`{U.C. 1.1}` to `{U.C. 8.3}`):
- **`{U.C. 8.3}`** workspace permanent deletion (fully dressed, Owner-only, with identity-verification and partial-erasure failure extensions).
- **Identity-verification steps and refusal flows** in `{U.C. 8.1}`/`{U.C. 8.2}` (RN27).
- **Secure-by-default initialization** in `{U.C. 2.1}`/`{U.C. 3.1}` (RN28).
- Traceability matrix updated to 20 requirements / 20 use cases. Version History 4.0.0.

---

## 4. Key Advancements Over Version 1

| Dimension | Version 1 (Synthesis) | Version 2 (Round 1) |
|---|---|---|
| **Objective coverage** | 14 covered / 9 re-drives pending / 4 proposals pending / 3 phantom drivers | 26 covered, 0 partial, 0 pending — 62/62 placed, chains on natural objectives |
| **Chain integrity** | Several constraints driven by organizational-lane objectives; anchor mismatches | 11 chains re-anchored (ADJ-1…9); all anchors ∈ published sets |
| **Constraint set** | `RN1`–`RN26` | `RN1`–`RN30` (+ identity verification, secure defaults, permanent removal, secure-use docs) |
| **Functional set** | 19 cards / 19 PUCs / 19 UCs | 20 cards / 20 PUCs / 20 UCs (`R8.3` D1) |
| **Control selection** | Anchors embedded, selection implicit | Explicit Step-4 selection with per-item rationale (`ROUND1_REGISTER.md` §3) |
| **Sufficiency** | Not assessed | Assessed — specification-level sufficiency declared; Part 2 (threat & risk) gated and recommended to launch |
