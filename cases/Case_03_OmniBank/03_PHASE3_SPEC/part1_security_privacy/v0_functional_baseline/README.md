# Version 0: Pure Functional Baseline (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 0 (V0) — Pure Functional Baseline  
> **Reference Standard:** Volere Requirements Process (Robertson & Robertson), Cockburn Sea-Level Use Cases, GPTools Standards (E1.1 / E1.2)  
> **Status:** Locked Functional Baseline  

---

## 1. Scope & Purpose of Version 0

Version 0 represents the **pure, unpolluted functional baseline** of the OmniBank platform — the retail banking channels, payment services, and the OmniScore AI credit-scoring operation with its banking-grade operating functions.

Version 0 contains **zero pre-baked security or privacy control parameters** injected into functional requirements, and adheres strictly to **technology neutrality**. Domain-inherent operational capabilities of a five-regulation financial entity (SOC monitoring, vulnerability management, resilience testing, vendor register, AI governance) are elicited here as *business functionality* — their regulatory constraint chains are imposed by the V1 synthesis, never pre-baked.

## 2. Directory Contents

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/v0_functional_baseline/
├── README.md                                    # (This file) Overview and scope of Version 0
├── ../Doc01_Requirements_Elicitation_and_PUC.md    # GPTools E1.1 standard: 43 Functional Requirements (R1.1 to R11.4) & 43 PUCs
└── ../Doc02_System_Use_Cases.md                    # GPTools E1.2 standard: 43 Level-1 Sea-Level Use Cases ({U.C. 1.1} to {U.C. 11.4})
```

## 3. Structural Summary of Deliverables

### 3.1 [`../Doc01_Requirements_Elicitation_and_PUC.md`](../Doc01_Requirements_Elicitation_and_PUC.md)
- **43 Atomic Business Requirements** across 11 functional areas (7-row GPTools Table 22 cards): the customer/AI product core (R1 banking channels, credit scoring, human oversight, model releases) plus the operating functions (R2 crypto, R3 vulnerabilities, R4 identities, R5 incidents, R6 data lifecycle, R7 vendors, R8 development, R9 training, R10 governance, R11 testing).
- **10 measurable Quality Attributes (RN1–RN10)**: performance, availability, scalability, recoverability, privacy responsiveness, auditability, AI quality, AI fairness, interoperability, architectural integrity.
- **43 Product Use Cases (PUC)** mapping business events to boundary inputs and outputs.

### 3.2 [`../Doc02_System_Use_Cases.md`](../Doc02_System_Use_Cases.md)
- **11 Functional Areas** with Sea-Level discipline: zero leaf nodes, zero procedural scripts.
- **43 Level-1 Use Cases** in the light identification format; the fully-dressed Cockburn anatomy is elaborated during the V1 synthesis together with the accepted security behavior.
