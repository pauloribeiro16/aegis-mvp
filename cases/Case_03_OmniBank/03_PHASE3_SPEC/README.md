# Phase 3 — Specification Baseline (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** Part 1 COMPLETE — V2 approved (Round 1 converged 108/108 by directive, Round 2 1/1; 2026-09-29); Exit Gate GREEN; Part 2 cleared (ADR-006)

---

## 1. Overview & Directory Structure

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/
├── README.md                                    # (This file) Phase 3 Navigation & Executive Index
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Master normative guide: RE literature, iterative risk-acceptance rounds, and EARS rules
│
├── part1_security_privacy/                        # [PHASE 3 — PART 1] Security & Compliance (ADR-006)
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# Active Doc01 (working copy, synced to the current version folder)
│   ├── Doc02_System_Use_Cases.md                # Active Doc02 (working copy, synced to the current version folder)
│   │
│   ├── v0_functional_baseline/                      # [VERSION 0] Pure Functional Baseline (LOCKED)
│   │   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Functional Requirements & 43 PUCs (Pure Functional GPTools E1.1)
│   │   └── Doc02_System_Use_Cases.md                # 43 Sea-Level System Use Cases (Cockburn Level-1 MSS GPTools E1.2)
│   │
│   ├── v1_security_privacy_synthesis/               # [VERSION 1] Round-converged synthesis (APPROVED)
│   │   ├── README.md                                # V1 Scope, Accepted Constraints (RN11–RN26), Round Register
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Functional Cards + Absorbed Constraints RN11–RN26 + 92 Chain Rows
│   │   └── Doc02_System_Use_Cases.md                # 43 Fully-Dressed Use Cases with Accepted Security Behavior
│   │
│   ├── v2_security_privacy_synthesis/               # [VERSION 2] Round-2 convergence — risk-accepted baseline (APPROVED, ACTIVE)
│   │   ├── README.md                                # V2 Scope and Delta from V1
│   │   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Functional Cards, R3.3 MUST (3.0.0)
│   │   └── Doc02_System_Use_Cases.md                # 43 Fully-Dressed Use Cases, matrix aligned (3.0.0)
│   │
│   ├── analysis_v0_to_v1/                           # [COGNITIVE TRAJECTORY] Step-by-Step Synthesis Dossier
│   │   README.md                                        # Overview, the five steps, and the Exit Gate record
│   │   STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md   # Step 1: Functional audit, assets, boundaries, ingress points
│   │   STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md           # Step 2: Five-ambit juxtaposition → RN11–RN26 + 92 chain bindings
│   │   STEP3_EARS_FORMULATION_AND_ACCEPTANCE.md             # Step 3: Accepted formulations & verdict trace
│   │   STEP4_ABSORPTION_AND_TRACEABILITY_WEAVING.md         # Step 4: V1 absorption, UC upgrade, control selection
│   │   STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md               # Step 5: D1–D4 changes + evaluated-no-change rows
│   │   TRACEABILITY_REPAIR_LEDGER.md                        # Chain re-anchoring ledger (ADR-007 discharge semantics)
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
GPTools E1.1: Part I Scope, Part II As-Is, Part III To-Be with 11 functional groups, 43 requirement cards (7-row card anatomy), 10 measurable NFRs (Table 7), 43 PUCs (Table 8), and the System Use Case Model.

### 2.2 [`part1_security_privacy/Doc02_System_Use_Cases.md`](part1_security_privacy/Doc02_System_Use_Cases.md)
GPTools E1.2: Level-1 Sea-Level discipline (zero leaf nodes, zero procedural scripts) — the active documents carry the fully-dressed Cockburn anatomy synthesized in the V1/V2 rounds.

---

## 3. Phase 3 Part 1 Synthesis

With the functional baseline locked, **Part 1 — Security & Compliance** synthesizes the risk-accepted **Security & Privacy Requirements** through the iterative risk-acceptance round cycle (ADR-005): exhaustive mapping of all 134 Phase 2 objectives and the 7 principles against this functional model → proposals per gap (EARS constraint, risk, altitude, chain) → client verdicts → convergence → only then do the deliverable versions evolve, followed by explicit control selection. The **Part 1 Exit Gate (G1–G6)** then clears **Part 2 — Threat & Risk Analysis** (ADR-006).
