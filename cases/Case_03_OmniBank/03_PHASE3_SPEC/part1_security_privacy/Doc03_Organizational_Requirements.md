# Doc03 — Organizational Requirements (OmniBank Financial Systems)

> **Status:** DERIVED — the organizational lane is activated in this case: the two Phase 2 objectives carrying no functional carrier (`PO-D-08.1-001`, `PO-D-08.2-001`) are specified here as organizational requirements with fit criteria, verification methods and owners. The product requirements of the same capabilities remain in `Doc01`/`Doc02` (`R9.1` awareness training, `R9.2` role-specific competence programmes).
> **Charter:** PROCESS-lane requirements of Phase 3 Part 1 (ADR-008 D1) — obligations whose realization class is PROCESS/CAPABILITY (ADR-003), routed from the objectives verdicted `No functional carrier (organizational)` in [`part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md`](part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md) and from carve-outs recorded in the objective-mapping discharge records (ADR-007 D4). The technology legs of the same capabilities remain in `Doc01`.

## 1. Derivation contract

| Element | Rule |
|---|---|
| Subject | EARS with organizational subject: `The organization shall …` · `When …, the organization shall …` · `While …, the organization shall …` · `If …, then the organization shall …` · `Where …, the organization shall …` |
| Atomicity | One congruent demand set per requirement (ADR-007 D1) |
| Acceptance | Volere fit criterion — deterministic pass/fail (PRIN-ENG-05) |
| Verification | `INSPECT` / `DEMONSTRATE` / `ANALYZE` (dominant); `TEST` where automated evidence exists |
| Owner | From the Phase 2 `Doc01` responsible-owner column of the driving objective (D-08 rows: `DPO + HR`) |
| Chain | `regulation article → Phase 2 objective → (principle) → organizational control anchor` |
| Anchors (primary) | NIST CSF 2.0 GOVERN — `baseline/CONTROLS/NIST_CSF_2.0/GOVERN/` |
| Anchors (advisory, R2b) | ISO/IEC 27001:2022 A.5.x — `baseline/CONTROLS/ISO_27001_2022/A5_ORGANIZATIONAL/` · ENISA NIS2 baseline — `baseline/CONTROLS/ENISA/NIS2_BASELINE/` · BSI IT-Grundschutz OPS layer |
| Specificity | L2 ceiling (guidelines §2.5) — no invented operational parameters |
| Rounds & gate | ADR-005 per-item verdicts govern any change to this lane; the Part 1 Exit Gate G1 evidence surface extends to the organizational mapping (ADR-008 D7) |

## 2. Requirement card template

| Requirement |
|---|
| **ID:** ORG-D-XX.Y-NNN **Name:** — |
| **Statement (EARS):** — |
| **Requirement Origin:** — |
| **Fit Criterion:** — |
| **Verification Method:** — |
| **Dependencies:** • **Stakeholders:** — • **Owner:** — • **Cadence:** — • **Information Systems / Databases:** — |
| **Priority:** — |

## 3. Requirements by domain

### D-08 — General Security Awareness

| Requirement |
|---|
| **ID:** ORG-D-08.1-001 **Name:** Advise the controller and the workforce on data-protection obligations |
| **Statement (EARS):** The organization shall ensure that its data protection officer informs and advises the controller, the processor function it discharges for employment data, and the employees who carry out processing of their obligations under the applicable data-protection regulation — across the customer account and transaction, credit-scoring and employment processing scopes — and communicates those obligations in a form each audience can act on. |
| **Requirement Origin:** Data Protection Policy & Processing Register — the group data protection policy's mandate for the data protection officer to advise the controller and the workforce on the personal-data obligations recorded in the processing register |
| **Fit Criterion:** every request for data-protection advice raised by a business line, an internal function or an individual employee carries a recorded data protection officer response naming the applicable obligation and the action expected of the addressee; the resulting written guidance is issued to that addressee and is retrievable on request; the advice record spans every processing scope registered for the bank, and a scope with no advice record for a review period is raised as an open item in the processing register. |
| **Verification Method:** INSPECT |
| **Dependencies:** • **Stakeholders:** Data Protection Officer, HR, CISO, Compliance Analyst, business-line data owners, management body • **Owner:** DPO + HR • **Cadence:** on request; consolidated review each supervisory cycle and on material change to the processing register • **Information Systems / Databases:** Internal Application Database (data-protection advice register) |
| **Priority:** Must |

| Requirement |
|---|
| **ID:** ORG-D-08.2-001 **Name:** Monitor data-protection compliance, responsibilities and training |
| **Statement (EARS):** The organization shall ensure that its data protection officer monitors compliance with the applicable data-protection regulation, including the assignment of responsibilities, awareness-raising and the training of staff involved in processing operations. |
| **Requirement Origin:** Regulatory Reporting Calendar — the periodic data-protection compliance review cycle established for ECB supervision and the DORA and NIS 2 ICT risk framework |
| **Fit Criterion:** a monitoring record exists for each review period naming the responsibilities assigned to each processing activity and their holders, the awareness-raising and role-specific training delivered in the period with their attendance and completion, and the findings raised with the corrective action agreed; the record is reported to the management body; a processing activity whose assigned responsibilities are unrecorded, or whose role holders' training is not current, is not treated as covered for that period. |
| **Verification Method:** INSPECT |
| **Dependencies:** • **Stakeholders:** Data Protection Officer, HR, CISO, Compliance Analyst, business-line data owners, management body • **Owner:** DPO + HR • **Cadence:** per review period, with the outcome reported within the management body's ICT risk oversight cycle • **Information Systems / Databases:** Internal Application Database (data-protection compliance monitoring register) |
| **Priority:** Must |

## 4. Coverage linkage (objective / carve-out → ORG requirement)

| Phase 2 objective | Leg / carve-out | ORG requirement | Verification method | Owner |
|---|---|---|---|---|
| `PO-D-08.1-001` | GDPR Art. 39(1)(a) — the DPO informs and advises the controller or processor and the employees who carry out processing | `ORG-D-08.1-001` | INSPECT | DPO + HR |
| `PO-D-08.2-001` | GDPR Art. 39(1)(b) — the DPO monitors compliance, including the assignment of responsibilities, awareness-raising and training of staff involved in processing | `ORG-D-08.2-001` | INSPECT | DPO + HR |

**Derivation record.** Both requirements are the technology-leg-free residue of the D-08 awareness capabilities whose product leg is carried in `Doc01` as `R9.1` (awareness training delivery) and `R9.2` (role-specific competence programmes); the training-delivery surface and its record substrate stay in `Doc01`, while the data protection officer's advisory and monitoring activity has no product surface and is specified here. The chain terminates in organizational anchors: `GDPR Art. 39(1)(a)` → `PO-D-08.1-001` → NIST CSF 2.0 **GV.OC-03** ("legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed") and **GV.RR-02** ("roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced"); `GDPR Art. 39(1)(b)` → `PO-D-08.2-001` → NIST CSF 2.0 **GV.RR-02**, **GV.OV-03** ("organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed") and **GV.RR-03** ("adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies"). Specificity stays at L2 — no invented parameters; the owner is the Phase 2 responsible owner of the driving row, and the review cadence follows the bank's supervisory and management-body oversight cycle rather than an invented interval.

## 5. MoSCoW summary

| ID | Name | Priority | Restrictions |
|---|---|---|---|
| `ORG-D-08.1-001` | Advise the controller and the workforce on data-protection obligations | Must | — |
| `ORG-D-08.2-001` | Monitor data-protection compliance, responsibilities and training | Must | — |

## 6. Version History

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-05 | Organizational lane activated for this case (ADR-008): `ORG-D-08.1-001` and `ORG-D-08.2-001` derived from `PO-D-08.1-001` and `PO-D-08.2-001` — the two Phase 2 objectives with no functional carrier — with fit criteria, verification methods, owners and CSF 2.0 GOVERN anchors. |
