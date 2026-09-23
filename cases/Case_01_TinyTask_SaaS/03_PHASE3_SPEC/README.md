# Phase 3 — Specification Baseline (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2), Cockburn Use Cases, ISO/IEC/IEEE 29148  
> **Status:** Active Baseline Iterations (Version 0 and Version 1)  

---

## 1. Overview & Directory Architecture

This directory houses the formal **Requirements Engineering and System Use Cases Specification** for TinyTask SaaS. 

To maintain strict configuration control and prevent confusing mixed revisions, Phase 3 is organized into **versioned baselines** governed by a comprehensive methodological guide:

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/
├── README.md                                    # (This file) Phase 3 Navigation & Executive Index
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Master normative guide: RE literature, 4-step synthesis, and EARS rules
│
├── v0_functional_baseline/                      # [VERSION 0] Pure Functional Baseline (LOCKED)
│   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 18 Functional Requirements & 18 PUCs (Pure Functional GPTools E1.1)
│   └── Doc02_System_Use_Cases.md                # 18 Sea-Level System Use Cases (Cockburn Level-1 MSS GPTools E1.2)
│
└── v1_security_privacy_synthesis/               # [VERSION 1] Security & Privacy Synthesis (APPROVED)
    ├── README.md                                # V1 Synthesis Scope, Added Safeguards, and Traceability
    ├── Doc01_Requirements_Elicitation_and_PUC.md# Augmented Doc01: Functional Cards + Non-Functional Security/Privacy Table 7b
    ├── Doc02_System_Use_Cases.md                # Augmented Doc02: 18 Sea-Level Use Cases with Security Preconditions & Extensions
    └── Doc03_Security_Privacy_Requirements.md   # The Master Security & Privacy Specification (10 CRA REQ-SEC + 8 GDPR REQ-PRIV)
```

---

## 2. Methodology & Literature Foundation

All specifications in this directory are governed by [`PHASE3_PROCESS_AND_METHODOLOGY.md`](PHASE3_PROCESS_AND_METHODOLOGY.md), which synthesizes:
- **Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed.):** 3-level requirements architecture, EARS syntax patterns, and segregation of functional behavior from quality attributes.
- **Suzanne & James Robertson (*Mastering the Requirements Process / Volere*, 3rd ed.):** Work context modeling, Product Use Cases (PUC), Snow Cards, and verifiable non-functional Fit Criteria.
- **Alistair Cockburn (*Writing Effective Use Cases*):** Sea-Level (User Goal / Level 1) granularity, fully dressed behavioral format, and extension branches for threat handling.
- **ISO/IEC/IEEE 29148:2018:** Mandatory quality characteristics and empirical verification methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`).

---

## 3. Version Roadmap

### Version 0: Pure Functional Baseline (`v0_functional_baseline/`)
- **Status:** Locked.
- **Content:** 18 atomic business requirements (`R1.1` to `R8.2`), 18 Product Use Cases (`PUC 1.1` to `PUC 8.2`), and 18 Sea-Level System Use Cases (`{U.C. 1.1}` to `{U.C. 8.2}`).
- **Key Invariant:** Strictly pure functional, zero pre-baked security/privacy mechanisms, and 100% technology neutral (zero database/framework/cloud vendor names).

### Version 1: Security & Privacy Synthesis (`v1_security_privacy_synthesis/`)
- **Status:** Approved.
- **Content:** Synthesis of Phase 2 GDPR/CRA Operational Objectives (`PO-` and `SO-`) and 7 Secure Design Principles (`PRIN-ENG-01` to `PRIN-ENG-07`) against the V0 functional baseline.
- **Deliverables:** Augmented `Doc01` and `Doc02`, plus the new normative specification [`Doc03_Security_Privacy_Requirements.md`](v1_security_privacy_synthesis/Doc03_Security_Privacy_Requirements.md) containing 10 CRA Product Security (`REQ-SEC-*`) and 8 GDPR Privacy (`REQ-PRIV-*`) requirements in EARS syntax.

---

## 4. Downstream Lifecycle Progression

The outputs of **Version 1** serve as the direct inputs to:
1. **Phase 4 (Verification & Assurance):** Transforming the ISO 29148 verification bindings (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) into automated CI/CD test suites, security probes, and compliance audit dossiers.
2. **System Architecture & Threat Modeling:** Consuming the trust boundaries and EARS constraints to generate component topologies and data flow threat models (STRIDE / LINDDUN).
