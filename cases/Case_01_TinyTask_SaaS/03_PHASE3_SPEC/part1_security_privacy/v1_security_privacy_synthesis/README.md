# Version 1: Security & Privacy Synthesis (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 1 (V1) — Security & Privacy Synthesis  
> **Upstream Inputs:** Phase 2 Operational Objectives (`Doc01`) & Secure Design Principles (`Doc02`)  
> **Functional Base:** Phase 3 Version 0 (`part1_security_privacy/v0_functional_baseline/`)  
> **Status:** APPROVED  

---

## 1. Scope & Purpose of Version 1

Version 1 represents the **formal synthesis of cybersecurity and personal data protection obligations into the functional requirements baseline**.

While Version 0 established what the business and users need to accomplish in purely functional, technology-neutral terms, Version 1 specifies **how the system protects its assets, users, and boundaries**, directly addressing:
1. **EU Cyber Resilience Act (CRA) Annex I:** Product cybersecurity requirements, multi-tenant isolation, credential protection using state-of-the-art mechanisms, session expiration, strict file-type validation, untrusted content neutralization, cryptographic webhook signatures, API throttling, and immutable audit trails.
2. **EU General Data Protection Regulation (GDPR):** Data minimization by default (Art. 5(1)(c)), data subject access and structured portability (Art. 15/20), right to erasure and pseudonymization (Art. 17), purpose limitation on timesheets (Art. 5(1)(b)), encryption at rest and in transit (Art. 32), automated orphan file cleanup (Art. 5(1)(e)), and privacy audit logging (Art. 30).
3. **AEGIS 7 Secure Design Principles (`PRIN-ENG-01` to `PRIN-ENG-07`):** Explicit trust boundaries, fail-safe defaults, least privilege, complete mediation, and non-repudiable observability.

---

## 2. Directory Contents

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/v1_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 1 synthesis and delta from V0
├── ../Doc01_Requirements_Elicitation_and_PUC.md    # 19 Functional Cards (18 elicited + R1.3 derived) + absorbed Security/Privacy Constraints + Quality Attributes
└── ../Doc02_System_Use_Cases.md                    # 19 Sea-Level Use Cases with Security Preconditions, Extensions, & Guarantees
```

---

## 3. The 2 Artifacts of Version 1

Security & privacy NFRs (`RN9`–`RN26`) are **absorbed directly into the functional cards** they apply to (absorption rule, 2026-09-23); there is no standalone catalog document.

### 3.1 [`../Doc01_Requirements_Elicitation_and_PUC.md`](../Doc01_Requirements_Elicitation_and_PUC.md)
Carries the evolved functional baseline — 19 requirement cards (`R1.1` to `R8.2`, including `R1.3` derived in the Functional Refinement Pass) and 19 Product Use Cases (`PUC 1.1` to `PUC 8.2`) — with:
- **Absorbed `Security & Privacy Constraints` rows** (15 cards): each NFR line carries the full `regulation → Phase 2 rule → PRIN-ENG → control anchor` chain.
- **Quality Attributes table (Table 7):** 8 operational NFRs (`RN1`–`RN8`) plus the 3 cross-cutting security NFRs (`RN17`, `RN18`, `RN24`).
- **Functional Refinement Pass deltas (Step 4b):** derived `R1.3` (locked-account recovery), refined `R7.2`/`R8.2` descriptions, `R1.2` elevated to Must — registered in [`../analysis_v0_to_v1/STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`](../analysis_v0_to_v1/STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md).

### 3.2 [`../Doc02_System_Use_Cases.md`](../Doc02_System_Use_Cases.md)
Maintains Cockburn's Sea-Level granularity (Level 1) across the 19 System Use Cases (`{U.C. 1.1}` to `{U.C. 8.2}`) while augmenting each card with:
- **Security & Privacy Traces:** Direct references to the security & privacy NFRs (`RN9`–`RN26`).
- **Security Preconditions:** Requiring secure encrypted channels, authenticated tenant-scoped sessions, and verified RBAC permissions prior to execution.
- **Security Extensions (Alternative Flows):** Explicit branching for authentication lockouts, authorization rejections, tampered webhook signatures, rate-limit throttling, and malicious file uploads.
- **Enhanced Minimal Guarantees:** Mandating fail-safe rollback, zero data leakage, and non-repudiable audit logging (`RN18`).

---

## 4. Key Advancements Over Version 0

| Dimension | Version 0 (Baseline) | Version 1 (Synthesis) |
|---|---|---|
| **Scope** | Pure Functional Scope | Functional + Regulatory Security & Privacy Constraints + registered functional evolution (Step 5b) |
| **Functional Set** | 18 elicited cards (locked) | 19 cards: `R1.3` derived, `R7.2`/`R8.2` refined, `R1.2` re-prioritized to Must (STEP5 register) |
| **Security Coverage** | Zero (intentionally excluded) | 10 CRA Product Security + 8 GDPR Privacy Specifications |
| **Use Case Extensions** | Functional errors only (bad format, missing fields) | Security exception flows (auth brute force, script injection, forged webhooks, tenant bypass) |
| **Audit & Logging** | Business activity history only | Forensic, immutable security audit logging (`RN18`) |
| **Traceability** | Business Goals -> Functional Cards -> Use Cases | Phase 2 Objectives <-> Functional Reqs <-> Use Cases <-> Test Methods |
| **Verification Gate** | User acceptance of business flow | ISO 29148 verification methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) |
