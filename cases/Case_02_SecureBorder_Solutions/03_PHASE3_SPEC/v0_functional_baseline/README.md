# Version 0: Pure Functional Baseline (SecureBorder Solutions)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Defense & Critical Infrastructure — Automated Border-Control eGates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 0 (V0) — Pure Functional Baseline  
> **Reference Standard:** Volere Requirements Process (Robertson & Robertson), Cockburn Sea-Level Use Cases, GPTools Standards (E1.1 / E1.2)  
> **Status:** Locked Functional Baseline  

---

## 1. Scope & Purpose of Version 0

Version 0 represents the **pure, unpolluted functional baseline** of the SecureBorder eGate platform and its operating model.

In accordance with foundational requirements engineering literature:
- **Suzanne & James Robertson (*Mastering the Requirements Process / Volere*):** Functional requirements specify what the system must do to support business work and satisfy stakeholder goals, without conflating quality attributes, security mechanisms, or technical implementations.
- **Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed.):** Separating user requirements from non-functional constraints prevents premature architectural locking and ensures that business functionalities are verified against operational realities before security constraints are imposed.
- **Alistair Cockburn (*Writing Effective Use Cases*):** Use cases in V0 operate at the *Sea Level* (User Goal level), detailing the core behavioral interaction between system actors and the system black-box to deliver measurable business value.

Version 0 contains **zero pre-baked security or privacy control parameters** injected into functional requirements, and adheres strictly to **technology neutrality** (zero references to specific database engines, frameworks, or cloud vendors). Domain-inherent operational capabilities of a regulated border-security product (SOC monitoring, vulnerability management, SBOM, AI conformity governance, training) are elicited here as *business functionality* — their regulatory constraint chains are imposed by the V1 synthesis, never pre-baked.

---

## 2. Directory Contents

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/v0_functional_baseline/
├── README.md                                    # (This file) Overview and scope of Version 0
├── Doc01_Requirements_Elicitation_and_PUC.md    # GPTools E1.1 standard: 28 Functional Requirements (R1.1 to R11.2) & 28 PUCs
└── Doc02_System_Use_Cases.md                    # GPTools E1.2 standard: 28 Level-1 Sea-Level Use Cases ({U.C. 1.1} to {U.C. 11.2})
```

---

## 3. Structural Summary of Deliverables

### 3.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
- **28 Atomic Business Requirements:** Formatted using the exact 7-row GPTools Table 22 card anatomy across 11 functional areas:
  - `R1.1`–`R1.3`: Enrol traveller biometric reference, perform biometric verification and gate decision, consult passage decision records
  - `R2.1` & `R2.2`: Review and override automated decisions, manage manual-lane referrals
  - `R3.1`–`R3.3`: Manage operator identity lifecycle, authenticate operators with multi-factor verification, assign and review operational access roles
  - `R4.1` & `R4.2`: Process traveller data-subject requests, maintain records of processing activities
  - `R5.1`–`R5.3`: Collect and correlate fleet security events, triage and manage incidents, recover services and exercise continuity
  - `R6.1`: Execute unified regulatory notifications
  - `R7.1`–`R7.3`: Identify and remediate vulnerabilities, distribute signed software and model updates, operate coordinated vulnerability disclosure
  - `R8.1`–`R8.3`: Enforce release pipeline security gates, maintain software bills of materials, version and roll back AI models
  - `R9.1`–`R9.3`: Maintain AI risk management and conformity documentation, monitor AI accuracy/drift/bias, test AI systems adversarially and explain decisions
  - `R10.1`–`R10.3`: Maintain unified impact and risk assessments, assess vendors and record component provenance, maintain compliance reporting and audits
  - `R11.1` & `R11.2`: Deliver security and privacy awareness training, deliver oversight and AI competence training
- **10 measurable Quality Attributes (RN1–RN10):** performance, availability, scalability, recoverability, privacy responsiveness, auditability, AI quality, AI fairness, interoperability, deployment isolation.
- **28 Product Use Cases (PUC):** Mapping business events to system boundary inputs and outputs.

### 3.2 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
- **11 Functional Areas** with Sea-Level discipline: zero leaf nodes, zero procedural UI scripts.
- **28 Level-1 Use Cases** identified in the light format (Primary Actor / Goal / Operational Scope); the **fully-dressed Cockburn anatomy** (Preconditions, Trigger, Main Success Scenario, Extensions, Guarantees) is elaborated during the V1 synthesis, where security preconditions and extensions are also woven in from the accepted constraint set.
- **Clean Action Verb Conjugations:** Every requirement and use case uses an active verb in the infinitive (e.g. "Enrol...", "Triage...", "Maintain...").
