# Phase 3 — Part 2: Threat & Risk Analysis (TinyTask SaaS)

> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification, **Part 2 of 2** (ADR-006: two-part Phase 3)  
> **Status:** NOT STARTED — entry gate not yet formally exercised (gate defined below; Part 1 evidence in [`../synthesis_rounds/SUFFICIENCY_ASSESSMENT.md`](../synthesis_rounds/SUFFICIENCY_ASSESSMENT.md))

---

## 1. Scope

Formal **threat and risk analysis over the accepted, control-informed baseline** produced by Part 1 (Version 2, `../v2_security_privacy_synthesis/`):

- **STRIDE** per functional area and trust-boundary crossing (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege).
- **LINDDUN** privacy-threat lens over personal-data flows (linkability, identifiability, denyability/unawareness, disclosure, non-compliance).
- **Risk register:** per validated threat — severity, likelihood, risk level, treatment (mitigate via new/changed constraints re-entering the Part 1 round cycle, transfer, accept explicitly, or defer), mapped to the STRIDE/LINDDUN element and to the affected requirements/use cases.
- **Output IDs:** `TM-D-XX.Y-NNN` (threat model entries), registered per case in this folder.

Zero threat content exists in Part 1 deliverables by design; all threat work happens here.

## 2. Inputs

1. **Accepted baseline:** `../v2_security_privacy_synthesis/Doc01`/`Doc02` (20 cards / 20 use cases, chains `regulation → objective → requirement → control`).
2. **Trust boundaries & assets:** functional model of Doc01/Doc02 — actors (Owner, Admin, Member, Viewer), external services (External Payment Gateway, Notification / Email Service), multi-tenant boundary, upload/notification/export-erasure surfaces.
3. **Control surface:** the selected CSF 2.0 + PF anchors of the accepted set (`../synthesis_rounds/ROUND1_REGISTER.md` §3).

## 3. Entry Criterion (gate)

Part 2 starts only with the **Part 1 Exit Gate (G1–G6) green** — codified in [`../PHASE3_PROCESS_AND_METHODOLOGY.md`](../PHASE3_PROCESS_AND_METHODOLOGY.md) and evidenced for this case in [`../analysis_v1_to_v2/README.md`](../analysis_v1_to_v2/README.md).

## 4. Method (high level)

Per functional area: enumerate elements and crossings → hypothesize threats per STRIDE/LINDDUN category → validate against the baseline's controls → rate risk → decide treatment → constraints that change behavior re-enter the Part 1 round cycle (propose → verdict → converge → version evolves) → residual accepted risks recorded with rationale.

## 5. Directory Plan (to be created at launch)

```text
part2_threat_risk/
├── README.md                # (this file)
├── TM_ASSETS_AND_BOUNDARIES.md   # assets, trust boundaries, data flows (from the v2 functional model)
├── TM_STRIDE_PER_AREA.md         # threat enumeration & validation, one section per functional area
├── TM_LINDDUN_DATA_FLOWS.md      # privacy-threat lens over personal-data flows
└── RISK_REGISTER.md              # rated risks, treatments, residual acceptances
```
