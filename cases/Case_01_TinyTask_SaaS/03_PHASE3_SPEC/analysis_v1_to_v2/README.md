# Cognitive Trajectory & Step-by-Step Synthesis Analysis (V1 to V2)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 1: Security & Compliance**  
> **Purpose:** step-by-step cognitive trace of the transition from Version 1 (approved synthesis) to Version 2 (risk-accepted baseline) through the first full round of the iterative risk-acceptance cycle (ADR-005).  
> **Companion of:** [`../analysis_v0_to_v1/`](../analysis_v0_to_v1/README.md) (V0 → V1 trace)  
> **Ledger:** [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) — the authoritative per-item verdict and control-selection ledger; this dossier narrates how the steps were executed.

---

## 1. Directory Map

```text
cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/analysis_v1_to_v2/
├── README.md                                        # (this file) overview + Part 1 Exit Gate record
├── STEP1_V1_BASELINE_AUDIT.md                       # V1 state vs the exhaustive coverage matrix (Round 0 inputs)
├── STEP2_ROUND1_PROPOSAL_DERIVATION.md              # derivation of ADJ-1…ADJ-9 + P-01…P-04
├── STEP3_CLIENT_VERDICTS_AND_CONVERGENCE.md         # per-item verdicts and convergence
├── STEP4_CONTROL_SELECTION.md                       # Step 4 — control selection over the accepted set
└── STEP5_ABSORPTION_AND_V2_EVOLUTION.md             # absorption into Doc01/Doc02 4.0.0 + version ladder
```

---

## 2. Transition Summary

| Aspect | V1 (approved) | V2 (Round 1) |
|---|---|---|
| Objective coverage | 14 covered · 9 re-drive proposals · 4 new proposals · 31 no-carrier · 2 design guidance · 3 N/A | **26 covered** · 31 organizational (recorded) · 2 design guidance · 3 N/A |
| Chains | several constraints driven by organizational-lane objectives; anchors outside published sets | 11 chains re-anchored (ADJ-1…9); all anchors ∈ published sets |
| Constraints | RN1–RN26 | RN1–RN30 |
| Functional set | 19 cards / 19 PUCs / 19 UCs | 20 cards / 20 PUCs / 20 UCs (`R8.3` D1) |
| Round state | Round 1 open (13 items) | Converged 13/13 accepts (2026-09-28) |

Round 2 update (2026-09-28, ADR-007): the Round-1 coverage verdicts were re-audited under the fulfillment semantics — **6 fully covered / 19 partially covered** (explicit carve-outs) / **32 organizational**; record corrections in [`../synthesis_rounds/ROUND2_REGISTER.md`](../synthesis_rounds/ROUND2_REGISTER.md), improvement proposals P1–P4 pending client verdicts (accepted baseline unchanged).

---

## 3. Part 1 Exit Gate (Critérios de Paragem) — record

Gate codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md) §"Part 1 Exit Gate". Evidence per criterion:

| # | Criterion | Evidence | State |
|---|---|---|---|
| G1 | Exhaustive mapping 100% verdicted (objectives + principles), zero silent | `synthesis_rounds/OBJECTIVE_MAPPING.md` 62/62 + totals; `PRINCIPLE_MAPPING.md` 7/7 bound, 0 pending gaps. R2 re-audit (ADR-007, 2026-09-28): 6 fully / 19 partially covered with discharge records, 32 organizational — totals sum 62 | **GREEN** |
| G2 | Rounds converged; zero open verdicts; rejections recorded as risk acceptances | `ROUND1_REGISTER.md` §1: 13/13 accepts, 0 reject, 0 adjust; `synthesis_rounds/README.md` state. Round 2 applied record corrections only (ADR-007); improvement proposals P1–P4 pending — accepted baseline unchanged | **GREEN** |
| G3 | Control selection complete; anchors ∈ published sets | `ROUND1_REGISTER.md` §3 (per-constraint selection + sources); no out-of-set anchor without W4 | **GREEN** |
| G4 | Deliverables at current version; §6 checklist; `doc_lint.py --strict` = 0 | `v2_security_privacy_synthesis/` 4.0.0; lint run 2026-09-28: 1650 files, 0 findings | **GREEN** |
| G5 | Sufficiency assessment with verdict + explicit residuals | `synthesis_rounds/SUFFICIENCY_ASSESSMENT.md` (compliance + security verdicts; residuals: organizational lane, RN29 SHOULD, threat validation) | **GREEN** |
| G6 | Transition dossier complete | This dossier (STEP1–STEP5) | **GREEN** |

**Gate verdict: GREEN — Part 2 (Threat & Risk Analysis) is cleared to launch** (`../part2_threat_risk/`), on the researcher's order.
