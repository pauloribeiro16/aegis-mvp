# Cognitive Trajectory & Step-by-Step Synthesis Analysis (V0 to V1)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Purpose:** Detailed, reproducible step-by-step cognitive analysis of the transition from Version 0 (Pure Functional Baseline) to Version 1 (Security & Privacy Synthesis).  
> **Target Audience:** Systems Architects, Requirements Engineers, PhD Researchers, and Autonomous AI Agents (Training & Fine-Tuning Corpus).  
> **Status:** Normative Reasoning & Process Log  

---

## 1. Objective of this Analysis Dossier

This directory provides the complete **step-by-step cognitive trace** that guided the derivation of Phase 3 Version 1 from Version 0. 

Rather than presenting only the end results (the final documents), this dossier deconstructs:
1. **How each requirement and use case was analyzed.**
2. **What questions and threat hypotheses were raised at each step** (threat hypotheses preserved for Phase 4 in [`THREAT_ANALYSIS_DEFERRED.md`](THREAT_ANALYSIS_DEFERRED.md) — deferred per ADR-005).
3. **How upstream Phase 2 regulatory rules (`PO-` and `SO-`) and design principles (`PRIN-ENG-01` to `PRIN-ENG-07`) were cross-referenced with functional requirements and areas.**
4. **Why specific EARS syntactic patterns and Volere fit criteria were chosen for each requirement.**
5. **How the functional baseline was augmented without corrupting its underlying functional clarity.**

This structured trace serves as a **formal training dataset** for autonomous agents and engineers to repeat the AEGIS specification synthesis across any new domain or software product.

---

## 2. Directory Architecture & Document Map

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/analysis_v0_to_v1/
├── README.md                                                     # (This file) Overview of cognitive trajectory and synthesis pipeline
├── V0_V1_V2_ANALYSIS_TABLES.md                                    # Tabular view: V0 essence | V2 state | V1 RN synthesis per requirement and per use case
├── STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md            # Step 1: Deep audit of V0 pure functional baseline, assets, and boundaries
├── STEP2_REGULATORY_CROSS_CUTTING_AND_THREAT_DERIVATION.md       # Step 2: Juxtaposition of Phase 2 rules against V0 functionalities (threat hypotheses deferred to Phase 4)
├── STEP3_EARS_REQUIREMENT_FORMULATION_AND_FIT_CRITERIA.md        # Step 3: Formulating the security & privacy NFRs (RN9–RN26) using EARS & Volere fit criteria
├── STEP4_FUNCTIONAL_AUGMENTATION_AND_TRACEABILITY_WEAVING.md     # Step 4: Weaving security into Doc01 and Doc02 (Cockburn extensions & diffs)
├── STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md                        # Step 5b: Functional Evolution Register (D1–D4 changes, evaluated-no-change rows)
└── THREAT_ANALYSIS_DEFERRED.md                                   # Phase 4 seed: attack/privacy-threat hypotheses (ADR-005)
```

---

## 3. The 4-Step Synthesis Pipeline Summary

```mermaid
flowchart TD
    subgraph Step1["Step 1: Functional Audit & Asset Identification"]
        V0_In["V0 Functional Baseline<br>(Doc01 & Doc02)"]
        Audit["Audit 18 Reqs & 18 Use Cases<br>Map Assets, Actors, & Ingress Points"]
        V0_In --> Audit
    end

    subgraph Step2["Step 2: Regulatory Cross-Cutting Analysis"]
        P2_In["Phase 2 Rules & Principles<br>(PO-*, SO-*, PRIN-ENG-*)"]
        Juxtapose["Regulatory Rule Juxtaposition<br>Map Rules to Functional Areas"]
        Audit --> Juxtapose
        P2_In --> Juxtapose
    end

    subgraph Step3["Step 3: EARS Formulation & Fit Criteria"]
        EARS_Draft["Synthesize 18 Security & Privacy NFRs (RN9–RN26)<br>Apply EARS Sentence Patterns"]
        Fit_Criteria["Establish Volere Fit Criteria &<br>ISO 29148 Verification Methods"]
        Juxtapose --> EARS_Draft
        EARS_Draft --> Fit_Criteria
    end

    subgraph Step4["Step 4 & 4b: Augmentation & Functional Refinement"]
        Doc01_Aug["Absorb NFRs into R cards<br>(Security & Privacy Constraints rows)"]
        Doc02_Aug["Augment Doc02 Use Cases<br>(Preconditions, Extensions, Minimal Guarantees)"]
        Register["Record Functional Evolution Register<br>(STEP5: D1–D4 changes + evaluated-no-change)"]
        Fit_Criteria --> Doc01_Aug
        Fit_Criteria --> Doc02_Aug
        Fit_Criteria --> Register
    end
```

---

## 4. Key Rules and Methodological Invariants Enforced

Throughout the four steps, the following rules are strictly enforced:
- **Rule R13 (Technology Neutrality):** Zero mention of concrete database engines, web frameworks, cloud providers, or technical protocols (e.g., PostgreSQL, Redis, React, AWS, Stripe). All systems are modeled functionally (e.g., *Internal Application Database*, *External Payment Gateway*, *File Storage Service*).
- **Active Verb Conjugation:** Every requirement and use case name uses active verbs in the infinitive (e.g., *Manage User Accounts*, *Attach Deliverable Files*).
- **Cockburn Sea-Level Granularity:** All use cases describe user goals achieved in a single session delivering business value. Zero micro-UI procedural scripts.
- **EARS Compliance:** All security and privacy requirements adhere to the 5 canonical EARS sentence patterns.
- **Empirical Verifiability:** Every requirement has an objective pass/fail threshold verifiable via `TEST`, `INSPECT`, `DEMONSTRATE`, or `ANALYZE`.

---


## 5. V1 Absorption & Functional Evolution Model (2026-09-23)

Per user rule, **V1 absorbs security & privacy NFRs directly into each functional R<n.m> card** as a `Security & Privacy Constraints` block. The standalone RN catalog (former `Doc03_Security_Privacy_Requirements.md`) is dissolved. The security/privacy RNs (now `RN9`–`RN26`) live in the constraint block of the R cards they apply to, with the full tracing chain `Regulation → Phase 2 rule → PRIN-ENG → CSF/PF/AIRMF anchor`. The 8 standalone operational NFRs (`RN1`–`RN8`) remain in `Doc01` as a quality-attributes table.

On top of absorption, **V1 evolves the functional set through the Step 4b Functional Refinement Pass** (taxonomy D1 derived requirement / D2 description refinement / D3 priority re-evaluation / D4 card split). The applied changes — 1×D1 (`R1.3` locked-account recovery), 2×D2 (`R7.2`, `R8.2`), 1×D3 (`R1.2` → Must) — and the `evaluated, no change` decisions are registered in [`STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md`](STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md); V0 remains untouched.
