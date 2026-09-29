# Phase 3 — Specification Baseline (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Reference Standard:** Volere Requirements Process & GPTools Standards (E1.1 / E1.2)  
> **Status:** Part 1 COMPLETE — V2 approved (Round 1 converged 108/108 by directive, Round 2 1/1; 2026-09-29); Exit Gate GREEN; Part 2 cleared (ADR-006)

---

## 1. Overview & Directory Structure

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/
├── README.md                                    # (This file) Overview and roadmap for Phase 3
├── PHASE3_PROCESS_AND_METHODOLOGY.md            # Normative process manual (Steps 1–5b, rounds, Part 1 Exit Gate)
│
├── v0_functional_baseline/                      # [VERSION 0] Locked Pure Functional Baseline
│   ├── README.md                                # V0 Scope, Rationale, and Architecture
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Functional Requirements & 43 PUCs (Pure Functional)
│   └── Doc02_System_Use_Cases.md                # 43 Level-1 Sea-Level Use Cases
│
├── v1_security_privacy_synthesis/               # [VERSION 1] Round-1-converged synthesis (APPROVED)
│   ├── README.md                                # V1 Scope, Accepted Constraints (RN11–RN26), Round Register
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Cards + Absorbed Constraints + 92 Chain Rows (2.0.0)
│   └── Doc02_System_Use_Cases.md                # 43 Fully-Dressed Use Cases (2.0.0)
│
├── v2_security_privacy_synthesis/               # [VERSION 2] Round-2 convergence — ACTIVE (APPROVED)
│   ├── README.md                                # V2 Scope and Delta from V1
│   ├── Doc01_Requirements_Elicitation_and_PUC.md# 43 Cards, R3.3 MUST (3.0.0)
│   └── Doc02_System_Use_Cases.md                # 43 Fully-Dressed Use Cases, matrix aligned (3.0.0)
│
├── analysis_v0_to_v1/                           # [V0 → V1 TRANSITION] STEP1–STEP5 dossier + Part 1 Exit Gate record (GREEN)
│
├── part2_threat_risk/                           # [PHASE 3 — PART 2] Threat & Risk Analysis (entry gate: G1–G6, ADR-006)
│
├── Doc01_Requirements_Elicitation_and_PUC.md    # Active working copy (synced to V2)
└── Doc02_System_Use_Cases.md                    # Active working copy (synced to V2)
```

---

## 2. Document Map

### 2.1 [`Doc01_Requirements_Elicitation_and_PUC.md`](Doc01_Requirements_Elicitation_and_PUC.md)
GPTools E1.1: Part I Scope, Part II As-Is, Part III To-Be with 11 functional groups, 43 requirement cards (7-row card anatomy), 10 measurable NFRs (Table 7), 43 PUCs (Table 8), and the System Use Case Model.

### 2.2 [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md)
GPTools E1.2: Level-1 Sea-Level discipline (zero leaf nodes, zero procedural scripts), light identification format pending the V1 fully-dressed elaboration.

---

## 3. Phase 3 Part 1 Synthesis

With the functional baseline locked, **Part 1 — Security & Compliance** synthesizes the risk-accepted **Security & Privacy Requirements** through the iterative risk-acceptance round cycle (ADR-005): exhaustive mapping of all 134 Phase 2 objectives and the 7 principles against this functional model → proposals per gap (EARS constraint, risk, altitude, chain) → client verdicts → convergence → only then do the deliverable versions evolve, followed by explicit control selection. The **Part 1 Exit Gate (G1–G6)** then clears **Part 2 — Threat & Risk Analysis** (ADR-006).
