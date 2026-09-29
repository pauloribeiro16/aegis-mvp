# Phase 3 — Specification Baseline (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** Part 1 COMPLETE — V2 approved (Round 1 converged 71/71 on 2026-09-28; Round 2 converged 2026-09-29); Exit Gate GREEN; Part 2 cleared (ADR-006)  

---

## 1. Overview & Directory Structure

This directory houses the formal **Functional Requirements and System Use Cases Baseline** for the SecureBorder eGate platform, structured following the proven methodology of GPTools:

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/
├── README.md                                    # (This file) Phase 3 Navigation & Executive Index
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Master normative guide: RE literature, iterative risk-acceptance rounds, and EARS rules
│
├── part1_security_privacy/                        # [PHASE 3 — PART 1] Security & Compliance (ADR-006)
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# Active Doc01 (working copy, synced to the current version folder)
│   ├── Doc02_System_Use_Cases.md                # Active Doc02 (working copy, synced to the current version folder)
│   ├── Doc03_Organizational_Requirements.md    # Organizational lane (ADR-008 PROCESS carrier)
│   │
│   ├── v0_functional_baseline/                      # [VERSION 0] Pure Functional Baseline (LOCKED)
│   │   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 28 Functional Requirements & 28 PUCs (Pure Functional GPTools E1.1)
│   │   └── Doc02_System_Use_Cases.md                # 28 Sea-Level System Use Cases (Cockburn Level-1 MSS GPTools E1.2)
│   │
│   ├── v1_security_privacy_synthesis/               # [VERSION 1] Round-converged synthesis (APPROVED)
│   │   ├── README.md                                # V1 Synthesis Scope, Accepted Constraints (RN11–RN30), Round Register
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 28 Functional Cards + Absorbed Constraints RN11–RN30 + 92 Chain Rows
│   │   └── Doc02_System_Use_Cases.md                # 28 Fully-Dressed Use Cases with Accepted Security Behavior
│   │
│   ├── v2_security_privacy_synthesis/               # [VERSION 2] Round-2 convergence — risk-accepted baseline (APPROVED, ACTIVE)
│   │   ├── README.md                                # V2 Scope and Delta from V1
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 28 Functional Cards, R9.3 MUST (3.0.0)
│   │   └── Doc02_System_Use_Cases.md                # 28 Fully-Dressed Use Cases, matrix aligned (3.0.0)
│   │
│   ├── analysis_v0_to_v1/                           # [COGNITIVE TRAJECTORY] Step-by-Step Synthesis Dossier
│   │   README.md                                # Overview, the five steps, and the Exit Gate record
│   │   STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md   # Step 1: Functional audit, assets, boundaries, ingress points
│   │   STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md           # Step 2: Four-ambit juxtaposition → RN11–RN30 + 92 chain bindings
│   │   STEP3_EARS_FORMULATION_AND_ACCEPTANCE.md             # Step 3: Accepted formulations & verdict trace
│   │   STEP4_ABSORPTION_AND_TRACEABILITY_WEAVING.md         # Step 4: V1 absorption, UC upgrade, control selection
│   │   STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md               # Step 5: D1–D4 changes + evaluated-no-change rows
│   │
│   └── synthesis_rounds/                            # [ROUND CYCLE] Objective/principle/UC mappings + round registers
│       ├── README.md                                # Navigation, capability-lane rule, current state
│       ├── OBJECTIVE_MAPPING.md                     # Every Phase 2 objective verdicted against the functional model
│       ├── PRINCIPLE_MAPPING.md                    # Principle-centric mirror + per-requirement check
│       ├── UC_OBJECTIVE_CORRESPONDENCE.md          # Use-case-centric view with regulation tags
│       ├── ROUND1_REGISTER.md                      # Round 1: formulations, verdicts, control selections
│       ├── ROUND2_REGISTER.md                      # Round 2: D3 elevation(s) and convergence
│       └── SUFFICIENCY_ASSESSMENT.md               # Compliance + security verdict and residuals
│
├── part2_threat_risk/                           # [PHASE 3 — PART 2] Threat & Risk Analysis (entry gate: Part 1 exit gate G1–G6)
│   └── README.md                                # Part 2 Scope, Inputs, and Entry Criterion (ADR-006)
```
```

---

## 2. Document Map

### 2.1 [`part1_security_privacy/Doc01_Requirements_Elicitation_and_PUC.md`](part1_security_privacy/Doc01_Requirements_Elicitation_and_PUC.md)
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

### 2.2 [`part1_security_privacy/Doc02_System_Use_Cases.md`](part1_security_privacy/Doc02_System_Use_Cases.md)
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
