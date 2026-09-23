# Version 1: Security & Privacy Synthesis (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 1 (V1) — Security & Privacy Synthesis  
> **Upstream Inputs:** Phase 2 Operational Objectives (`Doc01`) & Secure Design Principles (`Doc02`)  
> **Functional Base:** Phase 3 Version 0 (`v0_functional_baseline/`)  
> **Status:** APPROVED  

---

## 1. Scope & Purpose of Version 1

Version 1 represents the **formal synthesis of cybersecurity and personal data protection obligations into the functional requirements baseline**.

While Version 0 established what the business and users need to accomplish in purely functional, technology-neutral terms, Version 1 specifies **how the system protects its assets, users, and boundaries**, directly addressing:
1. **EU Cyber Resilience Act (CRA) Annex I:** Product cybersecurity requirements, multi-tenant isolation, memory-hard credential hashing, token-based session expiration, strict MIME validation, context-aware output encoding, cryptographic webhook signatures, API throttling, and immutable audit trails.
2. **EU General Data Protection Regulation (GDPR):** Data minimization by default (Art. 5(1)(c)), data subject access and structured portability (Art. 15/20), right to erasure and pseudonymization (Art. 17), purpose limitation on timesheets (Art. 5(1)(b)), encryption at rest and in transit (Art. 32), automated orphan file cleanup (Art. 5(1)(e)), and privacy audit logging (Art. 30).
3. **AEGIS 7 Secure Design Principles (`PRIN-ENG-01` to `PRIN-ENG-07`):** Explicit trust boundaries, fail-safe defaults, least privilege, complete mediation, and non-repudiable observability.

---

## 2. Directory Contents

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/v1_security_privacy_synthesis/
├── README.md                                    # (This file) Overview of Version 1 synthesis and delta from V0
├── Doc01_Requirements_Elicitation_and_PUC.md    # Augmented Doc01: Functional Cards + Non-Functional Security/Privacy Table 7b
├── Doc02_System_Use_Cases.md                    # Augmented Doc02: 18 Sea-Level Use Cases with Security Preconditions, Extensions, & Guarantees
└── Doc03_Security_Privacy_Requirements.md       # The Master Security & Privacy Specification (10 CRA REQ-SEC + 8 GDPR REQ-PRIV)
```

---

## 3. The 3 Artifacts of Version 1

### 3.1 [`Doc03_Security_Privacy_Requirements.md`](Doc03_Security_Privacy_Requirements.md)
The cornerstone deliverable of Version 1. It provides:
- **Master Bidirectional Traceability Matrix:** Mapping each security/privacy requirement to its upstream Phase 2 Operational Objective (`PO-` or `SO-`), engineering principle (`PRIN-ENG-`), bound functional requirement (`R...`), and bound system use case (`{U.C. ...}`).
- **10 CRA Product Security Requirements (`REQ-SEC-01` to `REQ-SEC-10`):** Authored using strict EARS sentence templates (Ubiquitous, Event-Driven, State-Driven, and Unwanted Behavior).
- **8 GDPR Personal Data Protection Requirements (`REQ-PRIV-01` to `REQ-PRIV-08`):** Specifying concrete personal data rights, encryption standards, retention limits, and data subject access flows.
- **Empirical ISO/IEC/IEEE 29148 Verification Bindings:** Assigning each requirement a concrete, testable Volere Fit Criterion and one of the four empirical evaluation methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`).

### 3.2 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
Preserves the 18 atomic functional requirement cards (`R1.1` to `R8.2`) and 18 Product Use Cases (`PUC 1.1` to `PUC 8.2`) while adding:
- **Section 2.3 Table 7b:** Master synthesis cross-reference linking general operational quality attributes to the formal EARS requirements in `Doc03`.

### 3.3 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
Maintains Cockburn's Sea-Level granularity (Level 1) across the 18 System Use Cases (`{U.C. 1.1}` to `{U.C. 8.2}`) while augmenting each card with:
- **Security & Privacy Traces:** Direct references to `REQ-SEC-*` and `REQ-PRIV-*`.
- **Security Preconditions:** Requiring TLS 1.3, authenticated tenant-scoped sessions, and verified RBAC permissions prior to execution.
- **Threat Extensions (Alternative Flows):** Explicit branching for authentication lockouts, authorization rejections, tampered webhook signatures, rate-limit throttling, and malicious file uploads.
- **Enhanced Minimal Guarantees:** Mandating fail-safe rollback, zero data leakage, and non-repudiable audit logging (`REQ-SEC-10`).

---

## 4. Key Advancements Over Version 0

| Dimension | Version 0 (Baseline) | Version 1 (Synthesis) |
|---|---|---|
| **Scope** | Pure Functional Scope | Functional + Regulatory Security & Privacy Constraints |
| **Security Coverage** | Zero (intentionally excluded) | 10 CRA Product Security + 8 GDPR Privacy Specifications |
| **Use Case Extensions** | Functional errors only (bad format, missing fields) | Threat and security exception flows (auth brute force, XSS injection, forged webhooks, tenant bypass) |
| **Audit & Logging** | Business activity history only | Forensic, immutable security audit logging (`REQ-SEC-10`) |
| **Traceability** | Business Goals -> Functional Cards -> Use Cases | Phase 2 Objectives <-> Functional Reqs <-> Use Cases <-> Test Methods |
| **Verification Gate** | User acceptance of business flow | ISO 29148 verification methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) |
