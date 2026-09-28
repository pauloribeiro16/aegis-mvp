# Phase 3 — Specification Baseline (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** V0 Locked — V1 round-converged synthesis in progress (ADR-005 rounds; two-part Phase 3 per ADR-006)  

---

## 1. Overview & Directory Structure

This directory houses the formal **Functional Requirements and System Use Cases Baseline** for the SecureBorder eGate platform, structured following the proven methodology of GPTools:

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/
├── README.md                                    # (This file) Overview and roadmap for Phase 3
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Normative process manual (Steps 1–5b, rounds, Part 1 Exit Gate)
│
├── v0_functional_baseline/                      # [VERSION 0] Locked Pure Functional Baseline
│   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 28 Functional Requirements & 28 PUCs (Pure Functional)
│   └── Doc02_System_Use_Cases.md                # 28 Level-1 Sea-Level Use Cases
│
├── Doc01_Requirements_Elicitation_and_PUC.md    # Active working copy (synced to the current version folder)
└── Doc02_System_Use_Cases.md                    # Active working copy (synced to the current version folder)
```

---

## 2. Document Map

### 2.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
*Direct 1:1 structural fidelity with **GPTools E1.1 — AS-IS / TO-BE Model & Requirements Elicitation***:
- **Part I – Scope:** Objective, Problem Description, Product Position Statement, Expected Impact, Key Features, Stakeholders, System Users, and Constraints.
- **Part II – As-Is:** Business Roles in Context, Manual Border-Control Workflow Processes with inefficiency tables, and IT Support.
- **Part III – To-Be:**
  - Initial Customer Expectations (`['Expectation ID', 'Operational Expectation', 'Target Impact']`).
  - System Actors (`['Actor', 'Description']`).
  - Summary Table of Functional Requirements MoSCoW (`['ID', 'ID', 'Requirement', 'Priority', 'Restrictions']`).
  - **Individual Requirement Cards (R1 to R11)** formatted with the exact 7-row single-column card structure:
    `ID: R... Name: <Action Verb Phrase>`, `Description`, `Requirement Origin`, `Interfaces`, `Dependencies`, `Identified Problems`, `Priority`.
  - Non-Functional Requirements (`['ID', 'Requirement', 'Priority', 'Type']`) — 10 measurable targets.
  - Summary Table of Product Use Cases (PUC) — 28 business-triggered use cases.
  - System Use Case Model with Level-0 Mermaid diagram.

### 2.2 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
*Direct 1:1 structural fidelity with **GPTools E1.2 — Requirements Analysis & Use Cases***:
- **Methodological Framework:** Volere Approach and Triangular Functional Decomposition.
- **Work Context Model:** Mermaid context diagram with human actors, the platform, and external integrations.
- **Summary Table of Product Use Cases (PUC):** mapping each business trigger to its Level-1 System Use Case.
- **Domain Application Use Cases (`{U.C. 1}` to `{U.C. 11}`):** Detailed strictly up to **Level 1** (`{U.C.n.m}`), purely functional — 28 Sea-Level use cases.
- **Granularity Discipline:** Refinement strictly up to Level 1. **Zero leaf nodes** (`{U.C.n.m.k}`) and **zero step-by-step procedural execution sequences**.
- **Action Verb Phrasing:** All requirement titles, sub-requirement names, and use case names use active verbs (e.g. "Manage...", "Enrol...", "Notify...", "Govern...").

---

## 3. Downstream Phase 3 Synthesis

With the functional baseline locked, **Part 1 — Security & Compliance** synthesizes the risk-accepted **Security & Privacy Requirements** through the iterative risk-acceptance round cycle (ADR-005): exhaustive mapping of every Phase 2 objective and principle against this functional model → proposals per gap (EARS constraint, risk, altitude, chain) → client verdicts → convergence → only then does the deliverable version evolve, followed by explicit control selection. The **Part 1 Exit Gate (G1–G6)** then clears **Part 2 — Threat & Risk Analysis** (ADR-006).

The synthesis cross-cuts the functional capabilities with:
1. **Phase 2 Operational Objectives (`Doc01_Operational_Objectives.md`):** Multi-regulation operational rules (`PO-D-XX.Y-NNN` and `SO-D-XX.Y-NNN`) across GDPR, CRA, NIS 2, and AI Act ambits.
2. **Phase 2 Secure Design Principles (`Doc02_Secure_Design_Principles.md`):** 7 foundational engineering principles (`PRIN-ENG-01` through `PRIN-ENG-07`).
3. **AEGIS Autonomous Skills (`baseline/skills/`):** Automated auditing across Attack Surface Analysis, Trust Boundary Analysis, Least Privilege, Data Minimization, Fail-Safe Defaults, Verifiability, and Lifecycle Erasure.
