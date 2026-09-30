# Phase 3 — Part 2: Threat & Risk Analysis (SecureBorder eGate)

> **Case Study:** Case 02 — SecureBorder Solutions B.V. (Automated Border-Control Gates with On-Board Biometric Verification AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2** (ADR-006: two-part Phase 3)  
> **Status:** COMPLETED & CERTIFIED GREEN — Exit Gates G7–G12 passed (2026-09-30); registered in [`05_RISK_REGISTER_AND_GOVERNANCE.md`](05_RISK_REGISTER_AND_GOVERNANCE.md)  
> **Upstream Dependency:** Phase 3 Part 1 Approved Baseline Version 2 — [`../part1_security_privacy/v2_security_privacy_synthesis/`](../part1_security_privacy/v2_security_privacy_synthesis/) (28 cards `R1.1`–`R11.2`, 28 use cases `{U.C. 1.1}`–`{U.C. 11.2}`, constraints `RN1`–`RN30`, four ambits: GDPR · CRA · NIS 2 · AI Act)

---

## 1. Scope

Formal **threat and risk analysis over the accepted, control-informed baseline** produced by Part 1 (Version 2). Every cited mitigating constraint is anchored to the accepted Version 2 baseline (`Doc01` constraint chains + Table 7, `Doc02` use-case extensions):

- **STRIDE** per functional package and trust-boundary crossing — with dedicated attention to the biometric capture surface (`TB-01`/`TB-07`), the authority-integration boundary (`TB-04`), the multi-country update channel (`TB-06`), per-country deployment isolation (`TB-03`), and the **AI Threat Lane** (data/model poisoning, adversarial evasion, model inversion, model-exfiltration, monitoring concealment, fail-safe bypass) against the Art. 15 measures.
- **EMB3D hardware lane** — the eGate kiosk is CRA Critical Class hardware: sensor/firmware tampering, physical bypass, and on-board boundary threats are modeled explicitly (`TB-07`).
- **LINDDUN** privacy-threat lens over personal-data flows (traveller biometrics under Art. 9, token-only decision records, operator data; linkability, identifiability, detectability, unawareness, non-compliance).
- **Risk register:** per validated threat — dual qualitative scoring, treatment (**Mitigate / Accept / Transfer / Avoid**, ISO/IEC 27005:2022), mapped to the STRIDE/LINDDUN element and the affected requirements/use cases; mitigating constraints re-enter the Part 1 round cycle via the ADR-005 loop when absent.
- **Output IDs:** `TM-D-XX.Y-NNN` (threat model entries), registered per case in this folder.

Zero threat content exists in Part 1 deliverables by design; all threat work happens here.

## 2. Inputs

1. **Accepted baseline:** `../part1_security_privacy/v2_security_privacy_synthesis/Doc01`/`Doc02` (28 cards / 28 fully-dressed use cases, chains `regulation → objective → requirement → control` across four ambits).
2. **Trust boundaries & assets:** the V2 functional model — gate capture sessions, authority integration, regulatory dispatch, fleet update channel, per-country deployment isolation, operator back-office, on-board hardware boundary.
3. **Control surface:** the selected CSF 2.0 + PF anchors of the accepted set (`../part1_security_privacy/synthesis_rounds/ROUND1_REGISTER.md` §3) and the per-constraint anchors published in the `Doc01` v2 chains.

## 3. Entry Criterion (gate)

Part 2 started only with the **Part 1 Exit Gate (G1–G6) GREEN** — codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md) and evidenced for this case in the Part 1 exit record.

## 4. Method (high level)

Per functional package: enumerate elements and crossings → hypothesize threats per STRIDE/LINDDUN category (plus the ATLAS AI lane and the EMB3D hardware lane) → validate against the baseline's published constraints → rate risk (NIST SP 800-30 / ISO 27005 + OWASP factors) → decide treatment → constraints that change behavior re-enter the Part 1 round cycle (ADR-005) → residual accepted risks recorded with rationale.

## 5. Directory Contents (Sequential Pipeline Order)

```text
part2_threat_risk/
├── README.md                                    # (this file)
├── 00_METHODOLOGY_AND_EXECUTION_GUIDE.md        # Step 0: Methodological guide & scoring engine (case-agnostic)
├── 01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md     # Step 1: 16 assets, 7 trust boundaries, DFD Level 1, 28-UC traceability
├── 02_TECHNICAL_THREATS_STRIDE.md               # Step 2: 23 STRIDE cards incl. the ATLAS AI lane, one section per package
├── 03_PRIVACY_THREATS_LINDDUN.md                # Step 3: 10 LINDDUN privacy cards over 8 PII lifecycle flows
├── 04_ATTACK_VECTORS_AND_DEFENSE_TREES.md       # Step 4: 4 ADTrees, CAPEC/CWE/ATT&CK/ATLAS/EMB3D, broken path proofs
└── 05_RISK_REGISTER_AND_GOVERNANCE.md           # Step 5: 33-row 18-column ledger, Exit Gate G7–G12
```

## 6. Proportionality Projection vs. Delivered

Per [`../../../templates/phase3_threat_risk_guidelines.md`](../../../templates/phase3_threat_risk_guidelines.md) §5.3, the projected volumes for Case 02 (28 UCs, 11 packages, 5–6 external integrations, 4 regimes, +ATLAS and +EMB3D lanes) and the delivered outcome:

| Artefact | Projected | Delivered |
|---|---|---|
| Trust boundaries | 6–8 | **7** |
| Assets | 15–17 | **16** |
| DFD flows | 12–16 | **14** |
| STRIDE cards (incl. AI lane) | 28–34 | **23** |
| LINDDUN cards | 10–14 | **10** |
| ADTrees | 4 | **4** |
| Register rows | ~50 | **33** |

The STRIDE count lands below the naive 0.9/UC midpoint because nine of the 28 use cases are governance/process functions (R9.1, R10.x, R11.x, R7.1, R7.3) whose surfaces cross no untrusted boundary beyond the record-integrity class already carried by multi-target cards; their evaluation is recorded in the Step 1 traceability matrix and Step 2 summary notes. The lane effect (+ATLAS, +EMB3D) is additive as projected.
