# Phase 3 — Part 2: Threat & Risk Analysis (OmniBank Financial Systems)

> **Case Study:** Case 03 — OmniBank Financial Systems S.A. (Consumer Banking with In-House High-Risk Credit-Scoring AI)
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2** (ADR-006)
> **Status:** NOT STARTED — entry gate GREEN and evidenced; launch on the researcher's order.

---

## 1. Scope

Formal **threat and risk analysis over the accepted, control-informed baseline** produced by Part 1 (Version 2, `../part1_security_privacy/v2_security_privacy_synthesis/`):

- **STRIDE** per functional area and trust-boundary crossing — with particular attention to the OmniScore scoring surface (data/model poisoning, adversarial examples/model evasion, confidentiality attacks, model flaws), the mainframe/cloud boundary, the authority and registry channels, and the multi-regime notification flows.
- **LINDDUN** privacy-threat lens over personal-data flows (customer PII, financial transactions, credit scores; linkability, identifiability, non-compliance).
- **Risk register:** per validated threat — severity, likelihood, risk level, treatment (mitigate via constraints re-entering the Part 1 round cycle, transfer, accept explicitly, defer), mapped to the STRIDE/LINDDUN element and to the affected requirements/use cases.
- **Output IDs:** `TM-D-XX.Y-NNN`, registered per case in this folder.

## 2. Inputs

1. **Accepted baseline:** `../part1_security_privacy/v2_security_privacy_synthesis/Doc01`/`Doc02` (43 cards / 43 fully-dressed use cases, chains across five ambits).
2. **Trust boundaries & assets:** mainframe core, EU cloud channels, AI/ML platform, HSM custody, authority/registry channels, per-business-line segregation (V0 RN10).
3. **Control surface:** the selected CSF 2.0 + PF anchors (`../part1_security_privacy/synthesis_rounds/ROUND1_REGISTER.md` §3).

## 3. Entry Criterion (gate)

Part 2 starts only with the **Part 1 Exit Gate (G1–G6) GREEN** — evidenced in [`../part1_security_privacy/analysis_v0_to_v1/README.md`](../part1_security_privacy/analysis_v0_to_v1/README.md).

## 4. Method (high level)

Per functional area: enumerate elements and crossings → hypothesize threats per STRIDE/LINDDUN category → validate against the baseline's controls → rate risk → decide treatment → constraints that change behavior re-enter the Part 1 round cycle → residual accepted risks recorded with rationale.

## 5. Directory Plan (to be created at launch)

```text
part2_threat_risk/
├── README.md                # (this file)
├── TM_ASSETS_AND_BOUNDARIES.md   # assets, trust boundaries, data flows (from the V2 functional model)
├── TM_STRIDE_PER_AREA.md         # threat enumeration & validation, one section per functional area
├── TM_LINDDUN_DATA_FLOWS.md      # privacy-threat lens over personal-data flows
└── RISK_REGISTER.md              # rated risks, treatments, residual acceptances
```
