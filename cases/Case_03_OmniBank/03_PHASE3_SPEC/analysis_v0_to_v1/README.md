# Cognitive Trajectory & Step-by-Step Synthesis Analysis (V0 to V1/V2) — OmniBank Financial Systems

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 1: Security & Compliance**  
> **Purpose:** step-by-step cognitive trace of the transition from Version 0 (pure functional baseline) to the round-converged baseline (V1 2.0.0 → V2 3.0.0), run through the iterative risk-acceptance cycle from the start (ADR-005).  
> **Ledger:** [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) + [`ROUND2_REGISTER.md`](../synthesis_rounds/ROUND2_REGISTER.md).

---

## 1. Directory Map

```text
cases/Case_03_OmniBank/03_PHASE3_SPEC/analysis_v0_to_v1/
├── README.md                                        # (this file) overview + Part 1 Exit Gate record
├── STEP1_V0_FUNCTIONAL_AUDIT_AND_BOUNDARY_ANALYSIS.md   # V0 audit: 11 areas, assets, boundaries, ingress points
├── STEP2_REGULATORY_CROSS_CUTTING_ANALYSIS.md           # 5-ambit juxtaposition → RN11–RN26 candidates + 92 chain bindings
├── STEP3_EARS_FORMULATION_AND_ACCEPTANCE.md             # accepted formulations & verdict trace
├── STEP4_ABSORPTION_AND_TRACEABILITY_WEAVING.md         # V1 absorption, UC upgrade, control selection
└── STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md               # D1–D4 changes + evaluated-no-change rows
```

## 2. Synthesis Shape

- **16 new constraints (RN11–RN26)** proposed from the five regulatory ambits — 36 objective rows carried; multi-regulation chains are first-class (the same property demanded by up to five regimes).
- **92 chain bindings** on existing V0 functional cards (the V0 spans the customer/AI product core and the banking-grade operating functions).
- **2 DPO organizational non-carriers** + **4 N/A** (EU-established, series production, integration info) — recorded decisions.
- **T-001..T-005** harmonizations realized: unified notification clock (RN18), token-only erasure vs AI-log/financial-record retention (RN17+RN23), unified lifecycle assessments (R10.2 family), unified vendor pass incl. the DORA register (RN26), provider/deployer duty stacking (T-005).

## 3. Part 1 Exit Gate (Critérios de Paragem) — record

Gate codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md). Evidence:

| # | Criterion | Evidence | State |
|---|---|---|---|
| G1 | Exhaustive mapping 100% verdicted | `synthesis_rounds/OBJECTIVE_MAPPING.md` 134/134 placed (128 covered / 2 organizational / 4 N/A) + `PRINCIPLE_MAPPING.md` 7/7 bound | **GREEN** |
| G2 | Rounds converged | `ROUND1_REGISTER.md` (16/16 + 92/92 accepts by directive, 0 reject) + `ROUND2_REGISTER.md` (1/1 D3 accept) | **GREEN** |
| G3 | Control selection complete | `ROUND1_REGISTER.md` §3 — published sets + store-flagged PF (SR-GDPR-009/030); no out-of-set anchor | **GREEN** |
| G4 | Deliverables at current version; checklist + `doc_lint --strict` + `check_traceability.py` | `v2_security_privacy_synthesis/` 3.0.0; lint run 2026-09-29: 0 findings; referential-integrity run 2026-09-29: T2/T3/T4 clean after chain re-anchoring | **GREEN** |
| G5 | Sufficiency assessment produced | `synthesis_rounds/SUFFICIENCY_ASSESSMENT.md` — five-regulation verdict + explicit residuals | **GREEN** |
| G6 | Transition dossier complete | STEP1 (V0 audit), STEP2 (five-ambit juxtaposition), `STEP3_EARS_FORMULATION_AND_ACCEPTANCE.md`, `STEP4_ABSORPTION_AND_TRACEABILITY_WEAVING.md`, `STEP5_FUNCTIONAL_EVOLUTION_REGISTER.md` of this directory | **GREEN** |

**Gate verdict: GREEN — Part 2 (Threat & Risk Analysis) is cleared to launch** (`../part2_threat_risk/`), on the researcher's order.
