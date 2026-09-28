---
document_id: AEGIS-MVP-ADR-005
title: 'Phase 3 restructured — iterative risk acceptance and explicit control selection; threat analysis promoted to Phase 4'
status: 'ACCEPTED (researcher decision, 2026-09-24)'
date: 2026-09-24
phase: 'Phase 3 / Phase 4 (methodology architecture)'
author: 'Executor session (analysis + drafting); decision by the PhD researcher'
amends: 'ADR-2026-09-22_pipeline-io-contract.md (ADR-004) — phase chain extended'
---

# ADR-005 — Iterative risk acceptance in Phase 3; threat analysis as Phase 4

## 1. Status

**ACCEPTED** — decided by the researcher in working session on 2026-09-24. This ADR amends the phase I/O contract of ADR-004 and the Phase 3 process of `PHASE3_PROCESS_AND_METHODOLOGY.md`.

## 2. The question, stated precisely

The Phase 3 synthesis process (as executed on Case_01) ran **one-shot**: regulatory juxtaposition + threat derivation (Step 2), EARS formulation (Step 3), and absorption with use-case threat extensions (Step 4) all landed in a single pass, and the client's risk posture entered nowhere. Three activities were conflated that have different clocks:

1. **Risk negotiation** — the client must see each proposed constraint with the risk it addresses and accept, reject, or adjust it. A rejected proposal is an explicit **risk acceptance** by the client, and must be recorded as such — never silently dropped.
2. **Control selection** — once the accepted set exists, the *best* controls for it are identified from the control referentials. This is an expert derivation step in its own right, not a side effect of absorption.
3. **Threat analysis** — formal modeling (STRIDE/LINDDUN, attack surface, abuse scenarios) needs a **robust and concrete target**. Modeling threats against a freshly elicited, still-negotiating functional baseline prematures the result — the same design-independence logic as ADR-001 §3.1 ("a best practice of a design cannot be asserted before the design exists"), applied one stage later.

## 3. Evidence of the conflation (Case_01, 2026-09-23/24)

- Manual Step 2 was titled "Cross-Cutting Regulatory & **Threat** Analysis" — threat derivation sat upstream of any client decision.
- The STEP2 dossier derived threats (STRIDE & privacy threat modeling) that flowed directly into the approved baseline's use-case "Threat Extensions".
- No artifact anywhere recorded a client verdict on a proposed constraint; the first client-visible artifact was the finished V1.

## 4. Decision

### D1 — Phase 3 runs as an iterative risk-acceptance cycle

Synthesis is executed in **rounds**. Each round:

1. **Derive** candidate proposals from the regulatory juxtaposition matrix: one EARS constraint per item, carrying the risk it addresses, its altitude level (guidelines §2.5, L2/L3), and its regulatory chain.
2. **Present** the proposal round to the client stakeholders.
3. **Record the verdict per item**: **Accept** / **Reject** (= explicit risk acceptance — the item and its risk stay in the register as accepted-by-decision, never deleted) / **Adjust** (wording, level, or scope; re-proposed next round).
4. **Iterate** until convergence: a round closes when it produces no new rejections or the client explicitly closes the baseline.

Only after convergence do the deliverable versions (`Doc01`/`Doc02`) evolve. Artifacts: per-case `03_PHASE3_SPEC/synthesis_rounds/` holding the **Risk Acceptance Register** (template: `templates/phase3_risk_acceptance_register.md`). Functional refinement-pass items (Step 5b) enter the cycle as round proposals like any other.

### D2 — Control identification is an explicit step (Step 4)

After convergence, each accepted item gets its **best-matching controls** selected from `baseline/CONTROLS/` (enforced: NIST CSF 2.0, PF 1.1, AI RMF; advisory per ADR-001 tiers), completing the derivation chain `regulation → article → objective → requirement → control` as a deliberate act. Absorption/weaving (Step 5) then materializes the accepted, control-anchored set into V1.

### D3 — Threat analysis is promoted to Phase 4 (own phase)

Formal threat modeling leaves Phase 3 entirely and becomes **Fase 4 — Threat Analysis**: STRIDE/LINDDUN, attack-surface analysis, and abuse scenarios performed over the **accepted, control-informed baseline**. Trigger: researcher judgment that the accepted baseline is robust and concrete. Asset identification and trust-boundary mapping **remain in Phase 3 Step 2** (they are needed to derive proposals) and seed Phase 4.

**ADR-004 contract amended:**

| Phase | Input | Output | IDs |
|---|---|---|---|
| Fase 3 — Specification | Objectives (+ Rules) | Security & Privacy Requirements (**risk-accepted**, control-anchored) | `REQ-D-XX.Y-NNN` (practice: `R<n>`/`RN<n>`) |
| **Fase 4 — Threat Analysis (new)** | Accepted F3 baseline + selected controls | **Threat Model** (threat register mapped to requirements/controls) | naming fixed at phase design (proposed `TM-D-XX.Y-NNN`) |
| Fase 5 — Verification & Assurance (was informally "Phase 4") | F4 Threat Model + F3 baseline | Verification artifacts, assurance case | — |

### D4 — Designation

Fase 4 = **Threat Model**; verification/implementation is referenced as **Fase 5** until formalized. Phase 3 deliverables must contain **zero formal threat modeling** — security behavior lives in use-case extensions and absorbed constraints; attack scenarios belong to Phase 4.

## 5. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Threat analysis as a *deferred stage inside the Phase 3 lane* (Stage T) | Keeps the activity structurally inside the phase that must not contain it; blurs the trigger and the deliverable boundary. |
| Merge threats into verification (informal Phase 5) | Threats must be modeled *before* verification to inform it; verification consumes the threat model, it does not produce it. |
| Package-level (per functional area) instead of per-item verdicts | Risk acceptance is an item-level decision; package verdicts hide rejected constraints inside accepted bundles. |

## 6. Consequences

- **Case_01 is grandfathered**: its APPROVED V1 was produced under the one-shot process. Light retrofit only — "Threat Extensions" renamed "Security Extensions", and `synthesis_rounds/` created for future revisions (e.g., the chain-recalibration backlog runs through the register). **Amended 2026-09-28 (researcher decision):** no threat dossier or threat material is retained under the Phase 3 folder; Phase 4 starts from the accepted, control-informed baseline and the asset/trust-boundary statements of the Phase 3 deliverables.
- **Case_02 and later cases** run the round cycle from the start.
- Phase 4's internal design (threat-register schema, severity model, LINDDUN scope) is **not designed here** — it is built when first triggered.
- The derivation chains (`regulation → article → objective → requirement → control`) remain the derivation spine across rounds; the cycle changes *when* and *in what order* they are exercised, not their structure.

## 7. References

- ADR-001 (best-practice layer — design-independence argument, T2/T3 admission)
- ADR-004 (pipeline I/O contract — amended by D3)
- `templates/phase3_functional_spec_guidelines.md` §2.5 (specificity matching — proposal altitude)
- `cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/PHASE3_PROCESS_AND_METHODOLOGY.md` (restructured §3)
- `templates/phase3_risk_acceptance_register.md` (register mechanics)
