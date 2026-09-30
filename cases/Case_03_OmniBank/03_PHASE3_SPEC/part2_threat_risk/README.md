# Phase 3 — Part 2: Threat & Risk Analysis (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2** (ADR-006: two-part Phase 3)  
> **Status:** COMPLETED & CERTIFIED GREEN — Exit Gates G7–G12 passed (2026-09-30); registered in [`05_RISK_REGISTER_AND_GOVERNANCE.md`](05_RISK_REGISTER_AND_GOVERNANCE.md)  
> **Upstream Dependency:** Phase 3 Part 1 Approved Baseline Version 2 — [`../part1_security_privacy/v2_security_privacy_synthesis/`](../part1_security_privacy/v2_security_privacy_synthesis/) (43 cards `R1.1`–`R11.4`, 43 use cases `{U.C. 1.1}`–`{U.C. 11.4}`, constraints `RN1`–`RN26`, five ambits: GDPR · CRA · NIS 2 · DORA · AI Act)

---

## 1. Scope

Formal **threat and risk analysis over the accepted, control-informed baseline** produced by Part 1 (Version 2). Every cited mitigating constraint is anchored to the accepted Version 2 baseline (`Doc01` constraint chains + Table 7, `Doc02` use-case extensions):

- **STRIDE** per functional package and trust-boundary crossing — with dedicated attention to the OmniScore scoring surface (data/model poisoning, adversarial evasion, model inversion, model exfiltration, serving integrity), the **mainframe/cloud segregation boundary**, the **authority and registry channels** (ECB, BSI/CSIRT, market surveillance, AI registry), the ICT third-party estate (DORA register), and the **multi-regime notification flows** (GDPR 72 h ∥ NIS 2 24 h ∥ DORA initial/intermediate/final with a 4 h initial clock ∥ CRA Art. 14 ∥ AI Act serious incidents).
- **AI Threat Lane (ATLAS)** — the OmniScore platform is an AI Act Annex III §5(b) high-risk system with in-house training and serving: poisoning, adversarial evasion, inversion, and robustness-assurance threats are modeled explicitly (`TB-05`).
- **LINDDUN** privacy-threat lens over personal-data flows (applicant financial data, automated credit decisions under Art. 22, token-only decision records, employee data; linkability, identifiability, detectability, unawareness, non-compliance).
- **Risk register:** per validated threat — dual qualitative scoring, treatment (**Mitigate / Accept / Transfer / Avoid**, ISO/IEC 27005:2022), mapped to the STRIDE/LINDDUN element and the affected requirements/use cases; mitigating constraints re-enter the Part 1 round cycle via the ADR-005 loop when absent.
- **Output IDs:** `TM-D-XX.Y-NNN`, registered per case in this folder.

Zero threat content exists in Part 1 deliverables by design; all threat work happens here.

## 2. Inputs

1. **Accepted baseline:** `../part1_security_privacy/v2_security_privacy_synthesis/Doc01`/`Doc02` (43 cards / 43 fully-dressed use cases, chains across five ambits).
2. **Trust boundaries & assets:** the V2 functional model — mainframe core banking, EU cloud customer channels, AI/ML platform (model registry, data platform, serving), Key Custody Service, authority/registry channels, per-business-line segregation.
3. **Control surface:** the selected CSF 2.0 + PF anchors (`../part1_security_privacy/synthesis_rounds/ROUND1_REGISTER.md` §3) and the per-constraint anchors published in the `Doc01` v2 chains.

## 3. Entry Criterion (gate)

Part 2 started only with the **Part 1 Exit Gate (G1–G6) GREEN** — codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md) and evidenced for this case in the Part 1 exit record.

## 4. Method (high level)

Per functional package: enumerate elements and crossings → hypothesize threats per STRIDE/LINDDUN category (plus the ATLAS AI lane) → validate against the baseline's published constraints → rate risk (NIST SP 800-30 / ISO 27005 + OWASP factors) → decide treatment → constraints that change behavior re-enter the Part 1 round cycle (ADR-005) → residual accepted risks recorded with rationale.

## 5. Directory Contents (Sequential Pipeline Order)

```text
part2_threat_risk/
├── README.md                                    # (this file)
├── 00_METHODOLOGY_AND_EXECUTION_GUIDE.md        # Step 0: Methodological guide & scoring engine (case-agnostic)
├── 01_SYSTEM_MODEL_ASSETS_AND_BOUNDARIES.md     # Step 1: 17 assets, 6 trust boundaries, DFD Level 1, 43-UC traceability
├── 02_TECHNICAL_THREATS_STRIDE.md               # Step 2: 25 STRIDE cards incl. the ATLAS AI lane, one section per package
├── 03_PRIVACY_THREATS_LINDDUN.md                # Step 3: 10 LINDDUN privacy cards over 8 PII lifecycle flows
├── 04_ATTACK_VECTORS_AND_DEFENSE_TREES.md       # Step 4: 4 ADTrees, CAPEC/CWE/ATT&CK/ATLAS, broken path proofs
└── 05_RISK_REGISTER_AND_GOVERNANCE.md           # Step 5: 35-row 18-column ledger, Exit Gate G7–G12
```

## 6. Proportionality Projection vs. Delivered

Per [`../../../templates/phase3_threat_risk_guidelines.md`](../../../templates/phase3_threat_risk_guidelines.md) §5.3, the projected volumes for Case 03 (43 UCs, 11 packages, 3 external channel groups + mainframe/cloud segregation, 5 regimes, +ATLAS lane) and the delivered outcome:

| Artefact | Projected | Delivered |
|---|---|---|
| Trust boundaries | 6–8 | **6** |
| Assets | 15–18 | **17** |
| DFD flows | 13–17 | **15** |
| STRIDE cards (incl. AI lane) | 34–42 | **25** |
| LINDDUN cards | 11–14 | **10** |
| ADTrees | 4 | **4** |
| Register rows | ~55 | **35** |

The STRIDE count lands below the naive 0.9/UC projection because **14 of the 43 use cases are process/governance functions** (R3.3, R3.4, R6.1, R7.3, R7.4, R8.1, R9.1–R9.3, R10.1–R10.3, R11.1, R11.3) whose surfaces cross no untrusted boundary beyond the record-integrity and channel classes already carried by multi-target cards; their evaluation is recorded in the Step 1 traceability matrix and Step 2 summary notes. Measured against the product-heavy surface only (29 UCs), the density is 0.90 cards/UC — inside the law's band. The regulatory-regime driver (5 regimes) expresses itself in the **impact ceiling**: 30 of 36 scored rows are governed or co-governed by a statutory dimension, the highest of the three cases.
