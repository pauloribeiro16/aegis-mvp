# Version 0: Pure Functional Baseline (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 0 (V0) — Pure Functional Baseline  
> **Reference Standard:** Volere Requirements Process (Robertson & Robertson), Cockburn Sea-Level Use Cases, GPTools Standards (E1.1 / E1.2)  
> **Status:** Locked Functional Baseline  

---

## 1. Scope & Purpose of Version 0

Version 0 represents the **pure, unpolluted functional baseline** of TinyTask SaaS. 

In accordance with foundational requirements engineering literature:
- **Suzanne & James Robertson (*Mastering the Requirements Process / Volere*):** Functional requirements specify what the system must do to support business work and satisfy stakeholder goals, without conflating quality attributes, security mechanisms, or technical implementations.
- **Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed.):** Separating user requirements from non-functional constraints prevents premature architectural locking and ensures that business functionalities are verified against operational realities before security constraints are imposed.
- **Alistair Cockburn (*Writing Effective Use Cases*):** Use cases in V0 operate at the *Sea Level* (User Goal level), detailing the core behavioral interaction between system actors and the system black-box to deliver measurable business value.

Version 0 contains **zero pre-baked security or privacy controls** (no artificial 2FA, session timeout, or encryption injected directly into functional requirements), and adheres strictly to **technology neutrality** (zero references to specific database engines, frameworks, or cloud vendors).

---

## 2. Directory Contents

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/v0_functional_baseline/
├── README.md                                    # (This file) Overview and scope of Version 0
├── ../Doc01_Requirements_Elicitation_and_PUC.md    # GPTools E1.1 standard: 18 Functional Requirements (R1.1 to R8.2) & 18 PUCs
└── ../Doc02_System_Use_Cases.md                    # GPTools E1.2 standard: 18 Level-1 Sea-Level Use Cases ({U.C. 1.1} to {U.C. 8.2})
```

---

## 3. Structural Summary of Deliverables

### 3.1 [`../Doc01_Requirements_Elicitation_and_PUC.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/v0_functional_baseline/Doc01_Requirements_Elicitation_and_PUC.md)
- **18 Atomic Business Requirements:** Formatted using the exact 7-row GPTools Table 22 card anatomy across 8 functional areas:
  - `R1.1` & `R1.2`: Manage User Accounts & Manage Workspace Profiles
  - `R2.1` & `R2.2`: Create Project Workspaces & Configure Project Metadata
  - `R3.1` & `R3.2`: Create Workspace Tasks & Organize Tasks via Kanban Boards
  - `R4.1` & `R4.2`: Attach Task Documentation & Manage File Assets
  - `R5.1` & `R5.2`: Manage Task Comments & Broadcast In-App Activity Notifications
  - `R6.1` & `R6.2`: Log Billable Hours & Generate Timesheet Summaries
  - `R7.1` & `R7.2`: Select Subscription Plan & Record Subscription Invoices
  - `R8.1` & `R8.2`: Dispatch Webhook Notifications & Consume External Productivity APIs
- **18 Product Use Cases (PUC):** Mapping business events to system boundary inputs and outputs.

### 3.2 [`../Doc02_System_Use_Cases.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/v0_functional_baseline/Doc02_System_Use_Cases.md)
- **8 Functional Areas:** Each containing an error-free Mermaid UML Use Case diagram (`flowchart LR`).
- **18 Fully Dressed Level-1 Use Cases:** Adhering to Cockburn's template (Primary & Supporting Actors, Preconditions, Trigger, Main Success Scenario, Extensions, and Postconditions) strictly at the sea level.
- **Clean Action Verb Conjugations:** Every requirement and use case uses an active verb in the infinitive (e.g. "Manage...", "Configure...", "Log...").
