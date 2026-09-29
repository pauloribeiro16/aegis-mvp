# Phase 3 — Part 2: Threat & Risk Analysis (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2** (ADR-006: two-part Phase 3)  
> **Status:** NOT STARTED — entry gate GREEN and evidenced; launch on the researcher's order.

---

## 1. Scope

Formal **threat and risk analysis over the accepted, control-informed baseline** produced by Part 1 (Version 1, `../part1_security_privacy/v1_security_privacy_synthesis/`):

- **STRIDE** per functional area and trust-boundary crossing — with particular attention to the biometric capture surface, the authority-integration boundary, the multi-country update channel, and AI-specific attacks (data/model poisoning, adversarial examples/model evasion, confidentiality attacks, model flaws) against the Art. 15 measures.
- **LINDDUN** privacy-threat lens over personal-data flows (traveller biometrics, employee data; linkability, identifiability, denyability/unawareness, disclosure, non-compliance).
- **Risk register:** per validated threat — severity, likelihood, risk level, treatment (mitigate via new/changed constraints re-entering the Part 1 round cycle, transfer, accept explicitly, or defer), mapped to the STRIDE/LINDDUN element and to the affected requirements/use cases.
- **Output IDs:** `TM-D-XX.Y-NNN` (threat model entries), registered per case in this folder.

Zero threat content exists in Part 1 deliverables by design; all threat work happens here.

## 2. Inputs

1. **Accepted baseline:** `../part1_security_privacy/v1_security_privacy_synthesis/Doc01`/`Doc02` (28 cards / 28 fully-dressed use cases, chains `regulation → objective → requirement → control` across four ambits).
2. **Trust boundaries & assets:** the V1 functional model — gate capture sessions, authority integration, regulatory dispatch, update channel, per-country deployment isolation (V0 RN10), operator back-office.
3. **Control surface:** the selected CSF 2.0 + PF anchors of the accepted set (`../part1_security_privacy/synthesis_rounds/ROUND1_REGISTER.md` §3).

## 3. Entry Criterion (gate)

Part 2 starts only with the **Part 1 Exit Gate (G1–G6) GREEN** — codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md) and evidenced for this case in [`../part1_security_privacy/analysis_v0_to_v1/README.md`](../part1_security_privacy/analysis_v0_to_v1/README.md).

## 4. Method (high level)

Per functional area: enumerate elements and crossings → hypothesize threats per STRIDE/LINDDUN category → validate against the baseline's controls → rate risk → decide treatment → constraints that change behavior re-enter the Part 1 round cycle (propose → verdict → converge → version evolves) → residual accepted risks recorded with rationale.

## 5. Directory Plan (to be created at launch)

```text
part2_threat_risk/
├── README.md                # (this file)
├── TM_ASSETS_AND_BOUNDARIES.md   # assets, trust boundaries, data flows (from the V1 functional model)
├── TM_STRIDE_PER_AREA.md         # threat enumeration & validation, one section per functional area
├── TM_LINDDUN_DATA_FLOWS.md      # privacy-threat lens over personal-data flows
└── RISK_REGISTER.md              # rated risks, treatments, residual acceptances
```
