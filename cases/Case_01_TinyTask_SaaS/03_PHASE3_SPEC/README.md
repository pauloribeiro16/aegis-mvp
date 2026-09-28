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
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Master normative guide: RE literature, iterative risk-acceptance rounds, and EARS rules
│
├── synthesis_rounds/                            # [ROUND CYCLE] Objective/principle mappings + round documentation (ADR-005)
│
├── analysis_v0_to_v1/                           # [COGNITIVE TRAJECTORY] Step-by-Step Synthesis Dossier (AI Training Corpus)
│   ├── README.md                                # Overview of cognitive trajectory and synthesis pipeline
│   ├── STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md        # Step 1: Functional audit, assets, and boundaries
│   ├── STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md                # Step 2: Phase 2 rules mapping (threat analysis out of Phase 3 — Phase 4, ADR-005)
│   ├── STEP3_EARS_REQUIREMENT_FORMULATION_AND_FIT_CRITERIA.md    # Step 3: EARS formulation & Volere fit criteria
│   ├── STEP4_FUNCTIONAL_AUGMENTATION_AND_TRACEABILITY_WEAVING.md # Step 4: Use case Cockburn extensions & diffs
│   ├── STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md                    # Step 5b: Functional Evolution Register (D1–D4 changes)
│   └── V0_V1_V2_ANALYSIS_TABLES.md                               # Version ladder, per-requirement absorption, and register summary
│
├── v0_functional_baseline/                      # [VERSION 0] Pure Functional Baseline (LOCKED)
│   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 18 Functional Requirements & 18 PUCs (Pure Functional GPTools E1.1)
│   └── Doc02_System_Use_Cases.md                # 18 Sea-Level System Use Cases (Cockburn Level-1 MSS GPTools E1.2)
│
└── v1_security_privacy_synthesis/               # [VERSION 1] Security & Privacy Synthesis + Functional Refinement Pass (APPROVED)
    ├── README.md                                # V1 Synthesis Scope, Absorbed Constraints, and Refinement Pass
    ├── Doc01_Requirements_Elicitation_and_PUC.md# 19 Functional Cards (incl. derived R1.3) + Absorbed Security/Privacy Constraints
    └── Doc02_System_Use_Cases.md                # 19 Sea-Level Use Cases with Security Preconditions & Extensions
```

---

## 2. Methodology & Literature Foundation

All specifications in this directory are governed by [`PHASE3_PROCESS_AND_METHODOLOGY.md`](PHASE3_PROCESS_AND_METHODOLOGY.md), which synthesizes:
- **Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed.):** 3-level requirements architecture, EARS syntax patterns, and segregation of functional behavior from quality attributes.
- **Suzanne & James Robertson (*Mastering the Requirements Process / Volere*, 3rd ed.):** Work context modeling, Product Use Cases (PUC), Snow Cards, and verifiable non-functional Fit Criteria.
- **Alistair Cockburn (*Writing Effective Use Cases*):** Sea-Level (User Goal / Level 1) granularity, fully dressed behavioral format, and extension branches for security behavior.
- **ISO/IEC/IEEE 29148:2018:** Mandatory quality characteristics and empirical verification methods (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`).

---

## 3. Version Roadmap

### Version 0: Pure Functional Baseline (`v0_functional_baseline/`)
- **Status:** Locked.
- **Content:** 18 atomic business requirements (`R1.1` to `R8.2`), 18 Product Use Cases (`PUC 1.1` to `PUC 8.2`), and 18 Sea-Level System Use Cases (`{U.C. 1.1}` to `{U.C. 8.2}`).
- **Key Invariant:** Strictly pure functional, zero pre-baked security/privacy mechanisms, and 100% technology neutral (zero database/framework/cloud vendor names).

### Cognitive Trajectory & Synthesis Analysis (`analysis_v0_to_v1/`)
- **Status:** Complete AI Training & Research Corpus.
- **Content:** 5-step detailed breakdown deconstructing every decision, regulatory mapping, EARS syntactic pattern, use case transformation, and functional evolution from V0 to V1:
  - [`STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md`](analysis_v0_to_v1/STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md)
  - [`STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md`](analysis_v0_to_v1/STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md)
  - [`STEP3_EARS_REQUIREMENT_FORMULATION_AND_FIT_CRITERIA.md`](analysis_v0_to_v1/STEP3_EARS_REQUIREMENT_FORMULATION_AND_FIT_CRITERIA.md)
  - [`STEP4_FUNCTIONAL_AUGMENTATION_AND_TRACEABILITY_WEAVING.md`](analysis_v0_to_v1/STEP4_FUNCTIONAL_AUGMENTATION_AND_TRACEABILITY_WEAVING.md)
  - [`STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`](analysis_v0_to_v1/STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md) — Functional Refinement Pass register (D1–D4 taxonomy)

### Version 1: Security & Privacy Synthesis (`v1_security_privacy_synthesis/`)
- **Status:** Approved.
- **Content:** Synthesis of Phase 2 GDPR/CRA Operational Objectives (`PO-` and `SO-`) and 7 Secure Design Principles (`PRIN-ENG-01` to `PRIN-ENG-07`) against the V0 functional baseline, plus the **Functional Refinement Pass (Step 4b)** that evolved the functional set where the synthesis revealed genuine gaps: derived `R1.3` (locked-account recovery), refined `R7.2`/`R8.2`, `R1.2` elevated to Must — registered in the STEP5 Functional Evolution Register.
- **Deliverables:** `Doc01` (19 requirement cards with absorbed `Security & Privacy Constraints` rows carrying the full `regulation → Phase 2 rule → PRIN-ENG → control anchor` chain; `RN9`–`RN26`, 10 CRA Product Security + 8 GDPR Privacy in EARS syntax) and `Doc02` (19 use cases with security preconditions, security extensions, and minimal guarantees). Per the absorption rule (2026-09-23) there is no standalone `Doc03` catalog.

---

## 4. Downstream Lifecycle Progression

The outputs of **Version 1** serve as the direct inputs to:
1. **Phase 4 (Analysis — deferred, ADR-005):** Formal threat modeling (STRIDE / LINDDUN) over the accepted, control-informed baseline, seeded by the asset and trust-boundary maps produced in Step 2. Triggered when the researcher judges the baseline robust and concrete.
2. **Phase 5 (Verification & Assurance):** Transforming the ISO 29148 verification bindings (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) and the Phase 4 threat model into automated CI/CD test suites, security probes, and compliance audit dossiers.

Future baseline revisions (e.g., the chain-recalibration backlog) run through the **iterative risk-acceptance cycle** — see [`synthesis_rounds/README.md`](synthesis_rounds/README.md).
