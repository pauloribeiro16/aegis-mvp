# Doc03 — Organizational Requirements (SecureBorder Solutions)

> **Status:** DERIVED — Round 1 of the organizational lane converged 2026-09-29 (2/2 accepts); the 2 organizational objectives of the coverage matrix are now specified requirements with verification methods. Product requirements: `Doc01`/`Doc02` (V1 approved; Part 1 Exit Gate GREEN).
> **Charter:** PROCESS-lane requirements of Phase 3 Part 1 (ADR-008 D1) — obligations whose realization class is PROCESS/CAPABILITY (ADR-003), routed from (a) objectives verdicted `No functional carrier (organizational)` in [`synthesis_rounds/OBJECTIVE_MAPPING.md`](synthesis_rounds/OBJECTIVE_MAPPING.md) and (b) carve-outs recorded in the objective-mapping discharge records (ADR-007 D4). The technology legs of the same capabilities remain in `Doc01`.

## 1. Derivation contract

| Element | Rule |
|---|---|
| Subject | EARS with organizational subject: `The organization shall …` · `When …, the organization shall …` · `While …, the organization shall …` · `If …, then the organization shall …` · `Where …, the organization shall …` |
| Atomicity | One congruent demand set per requirement (ADR-007 D1) |
| Acceptance | Volere fit criterion — deterministic pass/fail (PRIN-ENG-05) |
| Verification | `INSPECT` / `DEMONSTRATE` / `ANALYZE` (dominant); `TEST` where automated evidence exists |
| Owner | From Phase 2 `Doc01` — Governance & Stakeholder Matrix |
| Chain | `regulation article → Phase 2 objective → (principle) → organizational control anchor` |
| Anchors (primary) | NIST CSF 2.0 GOVERN — `baseline/CONTROLS/NIST_CSF_2.0/GOVERN/` |
| Anchors (advisory, R2b) | ISO/IEC 27001:2022 A.5.x — `baseline/CONTROLS/ISO_27001_2022/A5_ORGANIZATIONAL/` · ENISA NIS2 baseline — `baseline/CONTROLS/ENISA/NIS2_BASELINE/` · BSI IT-Grundschutz OPS layer |
| Specificity | L2 ceiling (guidelines §2.5) — no invented operational parameters |
| Rounds & gate | ADR-005 per-item verdicts; Part 1 Exit Gate G1 extends to this document's mapping (ADR-008 D7) |

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

### D-08 — Human Factors

| Requirement |
|---|
| **ID:** ORG-D-08.1-001 **Name:** Advise the organization and its staff on data-protection obligations |
| **Statement (EARS):** The organization shall ensure that its data protection officer informs and advises the controller, the processor function, and the employees who carry out processing on their obligations under the applicable data-protection regulation, and communicates those obligations in a form each audience can act on. |
| **Requirement Origin:** Biometric eGate Programme Charter — DPO appointment under the applicable data-protection regulation |
| **Fit Criterion:** every processing function has a recorded request for advice answered by the data protection officer, and the resulting guidance is issued in writing to the employees carrying out that processing; no processing function operates for a review period without a retrievable advice record. |
| **Verification Method:** INSPECT |
| **Dependencies:** • **Stakeholders:** Data Protection Officer, HR, CISO, processing function owners • **Owner:** DPO • **Cadence:** on request; reviewed annually • **Information Systems / Databases:** — |
| **Priority:** Must |

| Requirement |
|---|
| **ID:** ORG-D-08.2-001 **Name:** Monitor data-protection compliance, awareness and training |
| **Statement (EARS):** The organization shall ensure that its data protection officer monitors compliance with the applicable data-protection regulation, covering the assignment of responsibilities, security awareness, and role-specific training of staff involved in processing operations. |
| **Requirement Origin:** Biometric eGate Programme Charter — DPO monitoring duty for the biometric and employee-data processing scope |
| **Fit Criterion:** a monitoring record exists for each review period naming the responsibilities assigned, the awareness sessions delivered with attendance, and the role-specific training completed by each processing role; a role whose training is not current is not assigned to that processing activity. |
| **Verification Method:** INSPECT |
| **Dependencies:** • **Stakeholders:** Data Protection Officer, HR, CISO, processing function owners • **Owner:** DPO • **Cadence:** per review period • **Information Systems / Databases:** — |
| **Priority:** Must |

## 4. Coverage linkage (objective / carve-out → ORG requirement)

| Phase 2 objective | Leg / carve-out | ORG requirement | Verification method | Owner |
|---|---|---|---|---|
| `PO-D-08.1-001` | Art. 39(1)(a) informing and advising the controller/processor and employees | `ORG-D-08.1-001` | INSPECT | DPO |
| `PO-D-08.2-001` | Art. 39(1)(b) monitoring compliance, responsibilities, awareness and training | `ORG-D-08.2-001` | INSPECT | DPO |

**Derivation record.** Both requirements are the technology-leg-free residue of capabilities whose technology leg is carried in `Doc01` (PR.AT-01/PR.AT-02 anchor the training and awareness surface). The chain terminates in organizational anchors: `GDPR Art. 39(1)(a)`/`(b)` → `PO-D-08.1-001`/`PO-D-08.2-001` → NIST CSF 2.0 **GV.OC-03** ("legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed") and **GV.RR-03** ("adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies"). Specificity stays at L2 — no invented parameters; the review cadence comes from the Phase 2 operational scope, not invented here.

## 5. MoSCoW summary

| ID | Name | Priority | Restrictions |
|---|---|---|---|
| `ORG-D-08.1-001` | Advise the organization and its staff on data-protection obligations | Must | — |
| `ORG-D-08.2-001` | Monitor data-protection compliance, awareness and training | Must | — |

## 6. Version History

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-28 | Initial structure created under ADR-008 (organizational lane, Phase 3 Part 1) |
| 0.2.0 | 2026-09-29 | Organizational Round 1 derived: `ORG-D-08.1-001` and `ORG-D-08.2-001` specified with fit criteria, verification methods, owners and CSF GOVERN anchors — the first execution of the ADR-008 lane |
