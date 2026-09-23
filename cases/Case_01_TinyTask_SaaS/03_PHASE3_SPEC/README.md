# Phase 3 — Specification Baseline (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** Functional Baseline Active  

---

## 1. Overview & Directory Structure

This directory houses the formal **Functional Requirements and System Use Cases Baseline** for TinyTask SaaS, structured following the proven methodology of GPTools:

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/
├── README.md                                    # (This file) Overview and roadmap for Phase 3
├── Doc01_Requirements_Elicitation_and_PUC.md    # GPTools E1.1 standard: Context, Data, Actors, PUCs, & MoSCoW Requirements
└── Doc02_System_Use_Cases.md                    # GPTools E1.2 standard: Level-0 & Level-1 System Use Cases ({U.C.1} .. {U.C.6})
```

---

## 2. Document Map

### 2.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/Doc01_Requirements_Elicitation_and_PUC.md)
*Mirrors **GPTools E1.1 — Modelo AS-IS / TO-BE & Levantamento de Requisitos***:
- **Work Context Model:** Defines system boundaries, external services (Stripe API, transactional email, cloud storage), and communication channels.
- **Data Entities & Data Flow Specifications:** Formal schema definitions for User Accounts, Workspaces, Projects, Tasks, Attachments, Subscriptions, and Audit Logs.
- **System Actors:** Comprehensive definitions of all human roles (`Workspace Owner`, `Workspace Admin`, `Workspace Member`, `Workspace Viewer`) and automated actors (`Payment Gateway`, `System Scheduler`).
- **Product Use Case (PUC) Summary Table:** 22 business-level use cases (`PUC 1.1` to `PUC 6.4`) detailing participating actors, inputs (`in`), and outputs (`out`).
- **Exhaustive Functional Requirements Catalog:** 38 atomic functional requirements (`FR-01` to `FR-38` with 45 sub-items) classified with **MoSCoW** priorities (`34 MUST`, `6 SHOULD`, `5 COULD`, `3 WON'T`).

### 2.2 [`Doc02_System_Use_Cases.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/Doc02_System_Use_Cases.md)
*Mirrors **GPTools E1.2 — Análise de Requisitos & Casos de Uso***:
- **Methodological Framework:** Volere and Triangular Functional Decomposition.
- **Level-0 System Use Case Diagram:** Architectural Mermaid diagram illustrating the 6 primary capability domains.
- **High-Level System Use Cases (`{U.C.1}` to `{U.C.6}`):** Context, business objectives, and Level-1 refinement diagrams.
- **Level-1 System Sub-Cases (`{U.C.n.m}`):** 22 Level-1 sub-cases providing scope, pre-conditions, triggers, in/out payloads, and bidirectional traceability to `FR-XX`.
- **Scoping Discipline:** Strictly scoped to Level 1. **No leaf nodes** or step-by-step execution sequences are defined in this baseline; they are reserved for interactive co-design.

---

## 3. Downstream Phase 3 Synthesis

Once the functional baseline is locked, the next step in Phase 3 is synthesizing **Security & Privacy Requirements** (`Doc03_Security_Privacy_Requirements.md`). 

This synthesis will cross-cut these functional capabilities with:
1. **Phase 2 Operational Objectives (`Doc01_Operational_Objectives.md`):** Dual GDPR/CRA operational rules (`PO-D-XX.Y-NNN` and `SO-D-XX.Y-NNN`).
2. **Phase 2 Secure Design Principles (`Doc02_Secure_Design_Principles.md`):** 7 foundational engineering principles (`PRIN-ENG-01` through `PRIN-ENG-07`).
3. **AEGIS Autonomous Skills (`baseline/skills/`):** Automated auditing across Attack Surface Analysis, Trust Boundary Analysis, Least Privilege, Data Minimization, and Secure Defaults.
