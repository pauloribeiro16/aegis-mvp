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
*Direct 1:1 structural fidelity with **GPTools E1.1 — AS-IS / TO-BE Model & Requirements Elicitation***:
- **Part I – Scope:** Objective, Problem Description, Product Position Statement, Expected Impact, Key Features, Stakeholders, System Users, and Constraints.
- **Part II – As-Is:** Business Roles in Context, Manual Workflow Processes with 3-column data tables (`['Data Field', 'Data Type', 'Mandatory']`), and IT Support.
- **Part III – To-Be:**
  - Initial Customer Expectations (`['Initial Expectations', 'Description']`).
  - System Actors (`['Actor', 'Description']`).
  - Summary Table of Functional Requirements MoSCoW (`['ID', 'ID', 'Requirement', 'Priority', 'Restrictions']`).
  - **Individual Requirement Cards (R1 to R12)** formatted with the exact 7-row single-column card structure from Word:
    `ID: R... Name: <Action Verb Phrase>`, `Description`, `Requirement Origin`, `Interfaces`, `Dependencies`, `Identified Problems`, `Priority`.
  - Non-Functional Requirements (`['ID', 'Requirement', 'Priority', 'Type']`).
  - Summary Table of Product Use Cases (PUC) (`['PUC', 'PUC Name', 'Actors / Users', 'Input and Output']`).
  - System Use Case Model with Level-0 Mermaid diagram and Level-1 descriptions.

### 2.2 [`Doc02_System_Use_Cases.md`](file:///c:/Users/paulo.ribeiro/OneDrive%20-%20Instituto%20CCG%20ZGDV/Ambiente%20de%20Trabalho/Projetos_PhD/aegis-mvp/cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/Doc02_System_Use_Cases.md)
*Direct 1:1 structural fidelity with **GPTools E1.2 — Requirements Analysis & Use Cases***:
- **Methodological Framework:** Volere Approach and Triangular Functional Decomposition.
- **Work Context Model:** Mermaid context diagram with human actors, core platform services, and external integrations.
- **Summary Table of Product Use Cases (PUC):** Input (`in`) and output (`out`) payloads for each interaction.
- **Domain Application Use Cases (`{U.C. 1}` to `{U.C. 8}`):** Detailed strictly up to **Level 1** (`{U.C.n.m}`), purely functional.
- **Granularity Discipline:** Refinement strictly up to Level 1. **Zero leaf nodes** (`{U.C.n.m.k}`) and **zero step-by-step procedural execution sequences**.
- **Action Verb Phrasing:** All requirement titles, sub-requirement names, and use case names use active verbs (e.g. "Manage...", "Authenticate...", "Configure...").

---

## 3. Downstream Phase 3 Synthesis

Once the functional baseline is locked, the next step in Phase 3 is synthesizing **Security & Privacy Requirements** (`Doc03_Security_Privacy_Requirements.md`). 

This synthesis will cross-cut these functional capabilities with:
1. **Phase 2 Operational Objectives (`Doc01_Operational_Objectives.md`):** Dual GDPR/CRA operational rules (`PO-D-XX.Y-NNN` and `SO-D-XX.Y-NNN`).
2. **Phase 2 Secure Design Principles (`Doc02_Secure_Design_Principles.md`):** 7 foundational engineering principles (`PRIN-ENG-01` through `PRIN-ENG-07`).
3. **AEGIS Autonomous Skills (`baseline/skills/`):** Automated auditing across Attack Surface Analysis, Trust Boundary Analysis, Least Privilege, Data Minimization, and Secure Defaults.
