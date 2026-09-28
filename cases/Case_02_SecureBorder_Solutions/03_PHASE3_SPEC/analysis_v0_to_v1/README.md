# Cognitive Trajectory & Step-by-Step Synthesis Analysis (V0 to V1) — SecureBorder eGate

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 1: Security & Compliance**  
> **Purpose:** step-by-step cognitive trace of the transition from Version 0 (pure functional baseline) to Version 1 (round-converged security & privacy synthesis), run through the iterative risk-acceptance cycle from the start (ADR-005).  
> **Ledger:** [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) — authoritative per-item proposals, verdicts and control selections.

---

## 1. Directory Map

```text
cases/Case_02_SecureBorder_Solutions/03_PHASE3_SPEC/analysis_v0_to_v1/
├── README.md                                        # (this file) overview + Part 1 Exit Gate record
├── STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md   # V0 audit: 11 areas, assets, trust boundaries, ingress points
├── STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md           # 4-ambit juxtaposition → RN11–RN30 candidates + 51 chain bindings
├── STEP3_EARS_FORMULATION_AND_ACCEPTANCE.md             # (post-convergence) accepted formulations & verdict trace
├── STEP4_ABSORPTION_AND_TRACEABILITY_WEAVING.md         # (post-convergence) V1 absorption, UC upgrade, control selection
└── STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md               # (post-convergence) D1–D4 changes + evaluated-no-change rows
```

## 2. Synthesis Shape (from STEP2)

- **20 new constraints (RN11–RN30)** proposed from the four regulatory ambits — 39 objective rows carried.
- **51 chain bindings** on existing V0 functional cards (the V0 already elicits the operational capabilities of a RIGOROUS-tier essential entity).
- **2 transversal umbrellas** (DPbD, CRA Annex I) · **2 organizational non-carriers** (DPO activities, recorded) · **6 N/A** (recorded).
- **T-001..T-004** harmonizations realized by RN21 (unified notification timelines), RN24+RN28 (erasure vs AI-log retention), and the R10.1/R10.2 unified-assessment and vendor families.

## 3. Part 1 Exit Gate (Critérios de Paragem) — record

Gate codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md). Evidence filled at Part 1 closure:

| # | Criterion | Evidence | State |
|---|---|---|---|
| G1 | Exhaustive mapping 100% verdicted | `synthesis_rounds/OBJECTIVE_MAPPING.md` 100/100 + `PRINCIPLE_MAPPING.md` 7/7 | — |
| G2 | Rounds converged | `ROUND1_REGISTER.md` verdict ledger | — |
| G3 | Control selection complete | `ROUND1_REGISTER.md` §3 | — |
| G4 | Deliverables at current version; checklist + `doc_lint --strict` | `v1_security_privacy_synthesis/` 2.0.0 | — |
| G5 | Sufficiency assessment produced | `synthesis_rounds/SUFFICIENCY_ASSESSMENT.md` | — |
| G6 | Transition dossier complete | STEP1–STEP5 of this directory | — |
