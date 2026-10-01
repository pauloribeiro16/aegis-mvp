# E1.1b – SecureBorder eGate: Requirements Specification (Functional Cards & Security/Privacy Constraints)

## Executive Summary

This deliverable establishes the formal, verifiable requirements specification for the **SecureBorder eGate** platform, providing the authoritative contractual baseline for software engineering, quality assurance, and automated verification.

In accordance with software and systems engineering literature (Robertson & Robertson, Cockburn, Wiegers & Beatty, and IEEE 29148), this specification models the static, verifiable properties of the system. Operational processes, As-Is/To-Be workflows, and Product Use Cases (*PUC*) are decoupled into upstream deliverable [Doc00_Process_and_Operational_Workflows.md](Doc00_Process_and_Operational_Workflows.md). Every functional requirement card in this catalog explicitly traces back to the operational PUC it realizes.

Security, privacy, and regulatory constraints derived from the AEGIS methodology (GDPR, CRA, NIS2, and AI Act) are systematically integrated into each requirement card using the Easy Approach to Requirements Syntax (EARS) pattern — catalogued as full requirement statements in §3.2 — complete with full traceability to Phase 2 operational objectives and published control anchors (NIST CSF 2.0, NIST Privacy Framework 1.1, and NIST AI RMF).

---

## Table of Contents

- [1. Operational Actors Reference](#1-operational-actors-reference)
- [2. Functional Requirements Baseline](#2-functional-requirements-baseline)
  - [2.1 MoSCoW Prioritization Method](#21-moscow-prioritization-method)
  - [2.2 Summary Table of Functional Requirements](#22-summary-table-of-functional-requirements)
  - [2.3 Detailed Specification Cards for Functional Requirements](#23-detailed-specification-cards-for-functional-requirements)
- [3. Non-Functional Requirements & Transversal Attributes](#3-non-functional-requirements--transversal-attributes)
  - [3.1 General Operational Quality Attributes (Table 7)](#31-general-operational-quality-attributes-table-7)
- [Bibliography](#bibliography)
- [Version History](#version-history)

---

## 1. Operational Actors Reference

The functional requirements govern interactions initiated by the following operational actors (detailed in [Doc00_Process_and_Operational_Workflows.md](Doc00_Process_and_Operational_Workflows.md)):

*Table 1. Reference Actors*

| Actor | Category | Description |
|---|---|---|
| **Border Control Officer** | External Authority | Government-authority officer reviewing automated decisions and executing real-time overrides. |
| **SOC Analyst** | Internal Operations | SecureBorder security operations staff monitoring fleet telemetry and managing incident response. |
| **Security Engineer** | Internal Engineering | Engineering staff operating vulnerability remediation, updates, and coordinated disclosure. |
| **Release Engineer** | Internal Engineering | Release staff maintaining CI/CD security gates, software bills of materials (SBOM), and AI model rollbacks. |
| **AI Governance Lead** | Internal Governance | Governance staff maintaining AI risk files, conformity documentation, and fairness/bias monitoring. |
| **Privacy Officer (DPO)** | Internal Privacy | Privacy staff handling traveller/operator rights requests, processing records, and impact assessments. |
| **Compliance Analyst** | Internal Compliance | Compliance staff managing statutory reporting, vendor assessments, and notification calendars. |
| **Site Operations Technician** | Field Operations | Field engineering staff performing physical gate hardware maintenance and supervised configuration. |
| **Government Border Authority Integration** | External System | Government authority backend providing identity verification data, watchlist inputs, and referral targets. |
| **Regulatory Dispatch Service** | External System | Official statutory channels for mandatory incident and conformity notifications. |

---

## 2. Functional Requirements Baseline

### 2.1 MoSCoW Prioritization Method
Functional requirements are prioritized using the MoSCoW methodology:
- **MUST:** Mandatory requirement that must be satisfied in the baseline release for the system to be viable.
- **SHOULD:** High-impact requirement that should be satisfied unless critical delivery constraints dictate deferral.
- **COULD:** Desirable capability or enhancement that can be included if schedule and resources permit.
- **WON'T:** Out-of-scope feature that will not be implemented in the initial baseline release, reserved for future iterations.

### 2.2 Summary Table of Functional Requirements

*Table 6. List of functional requirements*

| ID | ID | Requirement | Priority | Restrictions | Realizes PUC |
|---|---|---|---|---|---|
| **R1** | | **Manage Traveller Biometric Verification** | **MUST** | | |
| | R1.1 | Enrol traveller biometric reference | MUST | Raw-capture discard ≤5 s | PUC 1.1 |
| | R1.2 | Perform biometric verification and gate decision | MUST | Decision ≤3 s | PUC 1.2 |
| | R1.3 | Consult traveller passage decision records | SHOULD | Token-only content | PUC 1.3 |
| **R2** | | **Manage Human Oversight and Gate Control** | **MUST** | | |
| | R2.1 | Review and override automated decisions | MUST | Justification recorded | PUC 2.1 |
| | R2.2 | Manage manual-lane referrals | MUST | | PUC 2.2 |
| **R3** | | **Manage Operator Identities and Access** | **MUST** | | |
| | R3.1 | Manage operator identity lifecycle | MUST | 24 h deprovisioning | PUC 3.1 |
| | R3.2 | Authenticate operators with multi-factor verification | MUST | | PUC 3.2 |
| | R3.3 | Assign and review operational access roles | MUST | Quarterly review | PUC 3.3 |
| **R4** | | **Manage Traveller Data Rights** | **MUST** | | |
| | R4.1 | Process traveller data-subject requests | MUST | 30-day statutory window | PUC 4.1 |
| | R4.2 | Maintain records of processing activities | MUST | | PUC 4.2 |
| **R5** | | **Monitor Security and Manage Incidents** | **MUST** | | |
| | R5.1 | Collect and correlate fleet security events | MUST | | PUC 5.1 |
| | R5.2 | Triage and manage incidents | MUST | | PUC 5.2 |
| | R5.3 | Recover services and exercise continuity | MUST | RTO <1 h | PUC 5.3 |
| **R6** | | **Notify Regulatory Authorities** | **MUST** | | |
| | R6.1 | Execute unified regulatory notifications | MUST | 24 h max-SLA clock | PUC 6.1 |
| **R7** | | **Manage Vulnerabilities and Updates** | **MUST** | | |
| | R7.1 | Identify and remediate vulnerabilities | MUST | | PUC 7.1 |
| | R7.2 | Distribute signed software and model updates | MUST | | PUC 7.2 |
| | R7.3 | Operate coordinated vulnerability disclosure | MUST | | PUC 7.3 |
| **R8** | | **Manage Secure Development and Releases** | **MUST** | | |
| | R8.1 | Enforce release pipeline security gates | MUST | | PUC 8.1 |
| | R8.2 | Maintain software bills of materials | MUST | Per release | PUC 8.2 |
| | R8.3 | Version and roll back AI models | MUST | Rollback <30 min | PUC 8.3 |
| **R9** | | **Govern AI Quality and Conformity** | **MUST** | | |
| | R9.1 | Maintain AI risk management and conformity documentation | MUST | | PUC 9.1 |
| | R9.2 | Monitor AI accuracy, drift, and bias | MUST | Quarterly bias cycle | PUC 9.2 |
| | R9.3 | Test AI systems adversarially and explain decisions | MUST | | PUC 9.3 |
| **R10** | | **Manage Governance, Risk, and Vendors** | **MUST** | | |
| | R10.1 | Maintain unified impact and risk assessments | MUST | Annual review | PUC 10.1 |
| | R10.2 | Assess vendors and record component provenance | MUST | | PUC 10.2 |
| | R10.3 | Maintain compliance reporting and audits | SHOULD | | PUC 10.3 |
| **R11** | | **Manage Training and Competence** | **MUST** | | |
| | R11.1 | Deliver security and privacy awareness training | MUST | Annual cadence | PUC 11.1 |
| | R11.2 | Deliver oversight and AI competence training | MUST | | PUC 11.2 |

---

##### 2.2.3 Detailed Specification Cards for Functional Requirements

The detailed functional requirement cards follow the exact 7-row single-column format established in the reference project standard:

#### R1 – Manage Traveller Biometric Verification

##### R1.1 – Enrol traveller biometric reference

| Requirement |
|---|
| **ID:** R1.1 **Name:** Enrol traveller biometric reference |
| **Description:** The system must capture the traveller's facial image at the gate, extract a biometric verification template, apply irreversible de-linking to the template, and discard the raw capture immediately after extraction. |
| **Requirement Origin:** Border Authority Service Contract & Passenger-Flow Programme | (Realizes: PUC 1.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN11** Biometric Template Protection at Rest — `GDPR Art. 32(1)(a)+(b)+Art. 5(1)(f)` → `PO-D-01.1-001` · `CRA Annex I Part I (2)(e)` → `SO-D-01.1-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10<br>**NFR-RN12** Cryptographic Key Custody Separation — `GDPR Art. 4(5)+Art. 32(1)(a)` → `PO-D-01.3-001` · `CRA Annex I Part I (2)(d)+(e)` → `SO-D-01.3-002` → `PRIN-ENG-03` → CSF PR.DS-01, PR.AA-05<br>**Chain** Data Minimization at Enrolment — `GDPR Art. 5(1)(c)` → `PO-D-05.1-001` · `CRA Annex I` → `SO-D-05.1-002` → `PRIN-ENG-06` → CSF ID.AM-08, ID.AM-03<br>**Chain** Retention Limitation — `GDPR Art. 5(1)(e)` → `PO-D-05.2-001` → `PRIN-ENG-07` → CSF ID.AM-08, ID.AM-03 |
| **Interfaces:** Gate capture station; enrolment console; authority enrolment-record channel |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, Airport Operators<br>• **Data Sources:** Gate Capture Session, Authority Enrolment Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R1.2 – Perform biometric verification and gate decision

| Requirement |
|---|
| **ID:** R1.2 **Name:** Perform biometric verification and gate decision |
| **Description:** The system must verify the traveller's live capture against the enrolled template (1:1 match), consult the authority watchlist input, and produce a confidence-scored passage decision (pass or refer) within the statutory service target, opening the gate only on a pass outcome. |
| **Requirement Origin:** Passenger-Flow Programme & Border Authority Service Contract | (Realizes: PUC 1.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN12** Cryptographic Key Custody Separation — `GDPR Art. 4(5)+Art. 32(1)(a)` → `PO-D-01.3-001` · `CRA Annex I Part I (2)(d)+(e)` → `SO-D-01.3-002` → `PRIN-ENG-03` → CSF PR.DS-01, PR.AA-05<br>**NFR-RN13** Data-in-Transit Protection (cross-cutting, Table 7) — `GDPR Art. 32(1)(b)+Art. 32(2)` → `PO-D-01.2-001` · `CRA Annex I Part I (2)(e)+(j)` → `SO-D-01.2-002` → `PRIN-ENG-01` → CSF PR.DS-02, PR.IR-01<br>**NFR-RN14** Record & Command Integrity Protection — `CRA Annex I Part I (2)(f)+(l)` → `SO-D-01.4-002` → `PRIN-ENG-07` → CSF PR.DS-01, PR.DS-10, PR.PS-04<br>**NFR-RN15** AI Model Resilience & Fail-Safe Reversion — `AI Act Art. 15(3)` → `SO-D-01.4-004` → `PRIN-ENG-04` → CSF PR.IR-03, PR.IR-04, PR.DS-11<br>**NFR-RN20** Secure-by-Default Configuration & Reset — `GDPR Art. 25(2)` → `PO-D-03.4-001` · `CRA Annex I 2(b)+(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01<br>**NFR-RN22** Product Activity Recording & Tamper Evidence — `CRA Annex I Part I (2)(l)` → `SO-D-04.1-002`, `SO-D-10.1-002` → `PRIN-ENG-07` → CSF DE.CM-01, DE.CM-09<br>**NFR-RN24** AI Event Logging over Lifetime — `AI Act Art. 12(1)+Art. 19` → `SO-D-10.2-004`, `SO-D-05.2-004` → `PRIN-ENG-07` → CSF PR.PS-04, DE.CM-09, DE.AE-03 |
| **Interfaces:** Gate capture and decision surface; verification service interface; authority decision-record channel |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, Airport Operators, Travellers<br>• **Data Sources:** Enrolment Template, Watchlist Input, Decision Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R1.3 – Consult traveller passage decision records

| Requirement |
|---|
| **ID:** R1.3 **Name:** Consult traveller passage decision records |
| **Description:** The system must allow authorized officers and authority users to consult past passage decisions — token-only entries with timestamp, gate, decision, confidence band, and override status — filtered by traveller token, date range, gate, and outcome. |
| **Requirement Origin:** Authority Audit & Statistics Needs | (Realizes: PUC 1.3) |
| **Security & Privacy Constraints:**<br>**NFR-RN11** Biometric Template Protection at Rest — `GDPR Art. 32(1)(a)+(b)+Art. 5(1)(f)` → `PO-D-01.1-001` · `CRA Annex I Part I (2)(e)` → `SO-D-01.1-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10<br>**NFR-RN14** Record & Command Integrity Protection — `CRA Annex I Part I (2)(f)+(l)` → `SO-D-01.4-002` → `PRIN-ENG-07` → CSF PR.DS-01, PR.DS-10, PR.PS-04<br>**Chain** Retention Limitation on Decision Records — `GDPR Art. 5(1)(e)` → `PO-D-05.2-001` → `PRIN-ENG-07` → CSF ID.AM-08, ID.AM-03 |
| **Interfaces:** Decision-record query console; case audit view |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities<br>• **Data Sources:** Decision Record Store<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Should |

---

#### R2 – Manage Human Oversight and Gate Control

##### R2.1 – Review and override automated decisions

| Requirement |
|---|
| **ID:** R2.1 **Name:** Review and override automated decisions |
| **Description:** The system must present each referred or challenged decision to a border control officer with the decision basis (confidence band and contributing factors) and allow the officer to confirm or override the outcome in real time, recording the justification with the decision entry. |
| **Requirement Origin:** Human-Oversight Obligation & Border Officer Operational Intake | (Realizes: PUC 2.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN19** Authorized-Actor Instruction Mediation — `GDPR Art. 29+Art. 32(4)` → `PO-D-03.2-001`, `PO-D-03.3-001` · `CRA Annex I Part I (2)(d)` → `SO-D-03.3-002` · `NIS 2 Art. 21(2)` → `SO-D-03.3-003` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06<br>**NFR-RN29** Human Oversight Effectiveness — `AI Act Art. 14` → `SO-D-08.2-004` → `PRIN-ENG-01` → CSF PR.AT-02, PR.AT-01, GV.RR-02 |
| **Interfaces:** Oversight worklist; decision-drivers view; override control |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities<br>• **Data Sources:** Decision Queue, Override Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R2.2 – Manage manual-lane referrals

| Requirement |
|---|
| **ID:** R2.2 **Name:** Manage manual-lane referrals |
| **Description:** The system must route referred travellers to the manual lane with a referral ticket, notify the officer desk, and track the referral to closure; on any gate fault the system must fail toward the manual lane automatically. |
| **Requirement Origin:** Border Officer Operational Intake & Site Contingency Procedure | (Realizes: PUC 2.2) |
| **Interfaces:** Referral ticket queue; manual-lane processing station |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, Airport Operators<br>• **Data Sources:** Referral Ticket, Gate Status Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R3 – Manage Operator Identities and Access

##### R3.1 – Manage operator identity lifecycle

| Requirement |
|---|
| **ID:** R3.1 **Name:** Manage operator identity lifecycle |
| **Description:** The system must manage operational identities for officers and SecureBorder staff across their engagement lifecycle — provisioning on induction (verifiable against government identity systems for officers), entitlement review on role change, and revocation within 24 hours of separation. |
| **Requirement Origin:** Government Identity Federation Programme & HR Separation Workflow | (Realizes: PUC 3.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN17** Operator Identity Lifecycle Management — `NIS 2 Art. 21(2)(i)` → `SO-D-03.1-003` · `CRA Annex I Part I (2)(d)+Art. 13(15)` → `SO-D-03.1-002` → `PRIN-ENG-03` → CSF PR.AA-01, PR.AA-05 |
| **Interfaces:** Identity administration console; joiner-mover-leaver intake; entitlement catalogue |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, SecureBorder Operations & Security<br>• **Data Sources:** Authority Identity Record, HR Engagement Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R3.2 – Authenticate operators with multi-factor verification

| Requirement |
|---|
| **ID:** R3.2 **Name:** Authenticate operators with multi-factor verification |
| **Description:** The system must authenticate all operational users — including every remote access to the management plane — using multi-factor verification before granting access, and lock accounts after repeated failed attempts. |
| **Requirement Origin:** Certified Operations Baseline & SOC Access Policy | (Realizes: PUC 3.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN18** Strong Operator Authentication — `NIS 2 Art. 21(2)(j)` → `SO-D-03.2-003` · `CRA Annex I Part I (2)(d)` → `SO-D-03.2-002` → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-05, PR.AA-06 |
| **Interfaces:** Operator sign-in surface; factor challenge; session establishment |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Authentication Event Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R3.3 – Assign and review operational access roles

| Requirement |
|---|
| **ID:** R3.3 **Name:** Assign and review operational access roles |
| **Description:** The system must let administrators assign least-privilege operational roles (oversight, monitoring, engineering, governance, site) and enforce a quarterly access-rights review with recorded outcomes. |
| **Requirement Origin:** Certified Operations Baseline & Access Governance Policy | (Realizes: PUC 3.3) |
| **Security & Privacy Constraints:**<br>**NFR-RN17** Operator Identity Lifecycle Management — `NIS 2 Art. 21(2)(i)` → `SO-D-03.1-003` · `CRA Annex I Part I (2)(d)+Art. 13(15)` → `SO-D-03.1-002` → `PRIN-ENG-03` → CSF PR.AA-01, PR.AA-05<br>**NFR-RN19** Authorized-Actor Instruction Mediation — `GDPR Art. 29+Art. 32(4)` → `PO-D-03.2-001`, `PO-D-03.3-001` · `CRA Annex I Part I (2)(d)` → `SO-D-03.3-002` · `NIS 2 Art. 21(2)` → `SO-D-03.3-003` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06 |
| **Interfaces:** Role assignment console; access-review worklist |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Role Assignment Record, Access Review Record<br>• **Extraction Periodicity:** quarterly<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R4 – Manage Traveller Data Rights

##### R4.1 – Process traveller data-subject requests

| Requirement |
|---|
| **ID:** R4.1 **Name:** Process traveller data-subject requests |
| **Description:** The system must receive traveller rights requests (access, erasure, portability) routed via the government controller, locate all linked biometric material and decision records for the traveller token, irreversibly de-link and purge biometric material on erasure while preserving lawful token-only decision records, and produce the response artefact within the statutory window. |
| **Requirement Origin:** Traveller Rights Requests via Government Controller | (Realizes: PUC 4.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN16** Rights-Requester Identity Verification — `GDPR Art. 12(6)+Art. 11(2)+Art. 5(1)(c)` → `PO-D-03.1-001` → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-02<br>**NFR-RN28** Traveller Erasure & Portability Delivery — `GDPR Art. 17+Art. 20+Art. 15(3)` → `PO-D-05.3-001`, `PO-D-05.4-001` → `PRIN-ENG-07` → CSF PR.DS-10, ID.AM-08 / PF CT.DM-P4<br>**Chain** Rectification Cascade — `GDPR Art. 16+Art. 19` → `PO-D-01.4-001` → `PRIN-ENG-07` → CSF PR.DS-01, ID.AM-08, PR.DS-10<br>**Chain** Permanent Product-Data Removal — `CRA Annex I Part I (2)(m)` → `SO-D-05.3-002` → `PRIN-ENG-07` → CSF PR.DS-10, ID.AM-08, PR.DS-02 |
| **Interfaces:** Data-subject request intake; identity-verification flow; erasure and export flow |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, Travellers<br>• **Data Sources:** Rights Request Record, Enrolment Template Store, Decision Record Store<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R4.2 – Maintain records of processing activities

| Requirement |
|---|
| **ID:** R4.2 **Name:** Maintain records of processing activities |
| **Description:** The system must maintain structured records of processing activities for both processing roles (traveller data on behalf of authorities; employee data under company responsibility), kept current and exportable on authority request. |
| **Requirement Origin:** Statutory Documentation Obligation & Authority Inspection Readiness | (Realizes: PUC 4.2) |
| **Security & Privacy Constraints:**<br>**Chain** Records of Processing Activities — `GDPR Art. 30` → `PO-D-09.4-001` → `PRIN-ENG-05` → CSF ID.AM-03, GV.PO-02, PR.PS-04 |
| **Interfaces:** Records-of-processing register; RoPA maintenance view |
| **Dependencies:**<br>• **Stakeholders:** Government Border Authorities, SecureBorder Executive Leadership<br>• **Data Sources:** Processing Inventory Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R5 – Monitor Security and Manage Incidents

##### R5.1 – Collect and correlate fleet security events

| Requirement |
|---|
| **ID:** R5.1 **Name:** Collect and correlate fleet security events |
| **Description:** The system must collect security-relevant events from all gates, the back-office, and the verification AI — including access events, decision anomalies, integrity warnings, and model-behaviour signals — and correlate them into actionable alerts in the operations centre view. |
| **Requirement Origin:** Security Operations Centre Handover & Fleet Monitoring Programme | (Realizes: PUC 5.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN22** Product Activity Recording & Tamper Evidence — `CRA Annex I Part I (2)(l)` → `SO-D-04.1-002`, `SO-D-10.1-002` → `PRIN-ENG-07` → CSF DE.CM-01, DE.CM-09<br>**NFR-RN25** AI Post-Market Monitoring Integration — `AI Act Art. 72` → `SO-D-10.1-004` → `PRIN-ENG-02` → CSF DE.CM-09, ID.IM-04 |
| **Interfaces:** Fleet event collector; SOC monitoring consoles; correlation view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Gate Event Stream, Back-Office Event Stream, AI Monitoring Stream<br>• **Extraction Periodicity:** continuous<br>• **Information Systems / Databases:** Internal Application Database, Event Store<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R5.2 – Triage and manage incidents

| Requirement |
|---|
| **ID:** R5.2 **Name:** Triage and manage incidents |
| **Description:** The system must classify and prioritize incidents by statutory impact, support containment actions per incident class (gate tamper, network intrusion, model misbehaviour), and maintain the incident record through resolution with response timestamps. |
| **Requirement Origin:** Incident Response Runbook & Statutory Notification Obligation | (Realizes: PUC 5.2) |
| **Security & Privacy Constraints:**<br>**Chain** NIS 2 Art. 21(2)(b) → `SO-D-10.1-003`<br>**Chain** **NFR-RN23** Incident-Handling Lifecycle Closure — `NIS 2 Art. 21(2)(c)` → `SO-D-04.1-003`, `SO-D-04.2-003` → `PRIN-ENG-02` → CSF RS.MA-01, RS.AN-03<br>**NFR-RN26** Breach Awareness & Containment Record — `GDPR Art. 33(1)+Art. 33(5)` → `PO-D-04.1-001`, `PO-D-04.2-001` → `PRIN-ENG-07` → CSF DE.CM-01, RS.MI-01, RS.MA-02|
| **Interfaces:** Incident console; containment controls; notification dispatch interface |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Alert Queue, Incident Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R5.3 – Recover services and exercise continuity

| Requirement |
|---|
| **ID:** R5.3 **Name:** Recover services and exercise continuity |
| **Description:** The system must support service recovery within the continuity targets for the back-office and gate management functions, restore from protected copies, and record continuity exercises (at least annual) with findings. |
| **Requirement Origin:** Business Continuity Programme & Authority Service-Level Commitments | (Realizes: PUC 5.3) |
| **Security & Privacy Constraints:**<br>**Chain** NIS 2 Art. 21(2)(b) → `SO-D-10.1-003`<br>**Chain** **NFR-RN23** Incident-Handling Lifecycle Closure — `NIS 2 Art. 21(2)(c)` → `SO-D-04.1-003`, `SO-D-04.2-003` → `PRIN-ENG-02` → CSF RS.MA-01, RS.AN-03<br>**Chain** Post-Incident Availability Protection — `CRA Annex I Part I (2)` → `SO-D-04.2-002`, `SO-D-04.4-002` → `PRIN-ENG-04` → CSF PR.IR-03, ID.AM-08<br>**Chain** Continuity & Disaster Recovery — `NIS 2 Art. 21(2)(c)` → `SO-D-04.4-003` → `PRIN-ENG-04` → CSF RC.RP-04, PR.DS-11<br>**Chain** Ongoing CIA + Resilience — `GDPR Art. 32(1)(b)` → `PO-D-04.4-001`, `PO-D-10.1-001` → `PRIN-ENG-04` → CSF PR.IR-04, PR.DS-11, RC.RP-04 |
| **Interfaces:** Backup console; recovery runbooks; continuity exercise view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security, Airport Operators<br>• **Data Sources:** Recovery Runbook, Continuity Exercise Record<br>• **Extraction Periodicity:** annual<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R6 – Notify Regulatory Authorities

##### R6.1 – Execute unified regulatory notifications

| Requirement |
|---|
| **ID:** R6.1 **Name:** Execute unified regulatory notifications |
| **Description:** The system must generate and dispatch regulatory notifications from a single incident record — early warnings on the 24-hour clock, follow-up notifications within 72 hours, serious-incident reports per the AI statutory matrix, and conformity reports — tracking each obligation to acknowledgement. |
| **Requirement Origin:** Multi-Regime Notification Obligation & Compliance Calendar | (Realizes: PUC 6.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN21** Unified Regulatory Notification Timeline Enforcement — `GDPR Art. 33(1)` → `PO-D-04.3-001` · `CRA Art. 14` → `SO-D-04.3-002` · `NIS 2 Art. 23` → `SO-D-04.3-003` · `AI Act Art. 73` → `SO-D-04.3-004` → `PRIN-ENG-05` → CSF RS.MA-04, RS.MA-02, RS.CO-02<br>**NFR-RN14** Record & Command Integrity Protection — `CRA Annex I Part I (2)(f)+(l)` → `SO-D-01.4-002` → `PRIN-ENG-07` → CSF PR.DS-01, PR.DS-10, PR.PS-04<br>**NFR-RN26** Breach Awareness & Containment Record — `GDPR Art. 33(1)+Art. 33(5)` → `PO-D-04.1-001`, `PO-D-04.2-001` → `PRIN-ENG-07` → CSF DE.CM-01, RS.MI-01, RS.MA-02<br>**Chain** Cross-Border Incident Routing — `NIS 2 Art. 23` → `SO-D-06.4-003` → `PRIN-ENG-05` → CSF RS.MA-04, RS.CO-02 |
| **Interfaces:** Incident dossier builder; regulatory dispatch channel; notification receipt view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security, Government Border Authorities<br>• **Data Sources:** Incident Record, Notification Obligation Calendar, Notification Receipt<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R7 – Manage Vulnerabilities and Updates

##### R7.1 – Identify and remediate vulnerabilities

| Requirement |
|---|
| **ID:** R7.1 **Name:** Identify and remediate vulnerabilities |
| **Description:** The system must maintain a vulnerability register across gates, back-office, and AI components with risk-based remediation targets (critical items within 24 hours), and support periodic offensive testing of the verification pipeline. |
| **Requirement Origin:** Vulnerability Management Programme & Offensive Testing Cycle | (Realizes: PUC 7.1) |
| **Security & Privacy Constraints:**<br>**Chain** Vulnerability Identification & Testing Family — `CRA Annex I Part I (2)(a)+Part II (1),(3)` → `SO-D-02.1-002`, `SO-D-02.4-002` · `NIS 2 Art. 21(2)(e)` → `SO-D-02.1-003`, `SO-D-07.3-003` · `GDPR Art. 32(1)(d)` → `PO-D-02.1-001` · `CRA Annex I Part II (3)` → `SO-D-10.3-002` (co) → `PRIN-ENG-02` → CSF ID.RA-01, ID.AM-02, PR.PS-02, PR.PS-06, GV.SC-04, DE.CM-09 |
| **Interfaces:** Vulnerability register; scanner and test-report intake |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Vulnerability Register, Test Findings Record<br>• **Extraction Periodicity:** continuous / annual<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R7.2 – Distribute signed software and model updates

| Requirement |
|---|
| **ID:** R7.2 **Name:** Distribute signed software and model updates |
| **Description:** The system must distribute software and AI model updates to the gate fleet only as verifiable signed artefacts, staged per site with automatic rollback on failed health checks, with security updates prioritized over functional releases. |
| **Requirement Origin:** Release Operations Procedure & Field Fleet Programme | (Realizes: PUC 7.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN27** Secure Update Distribution across Support Period — `CRA Annex I Part I (2)(c)+Part II (2),(7),(8)` → `SO-D-07.3-002`, `SO-D-02.2-002`, `SO-D-05.2-002` → `PRIN-ENG-02` → CSF ID.AM-02, GV.SC-03<br>**Chain** Secure-Use Advisories — `CRA Annex II §8` → `SO-D-08.1-002` → `PRIN-ENG-01` → CSF PR.AT-01 |
| **Interfaces:** Update distribution interface; fleet deployment console; advisory notices |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security, Airport Operators<br>• **Data Sources:** Release Calendar, Update Package Record, Deployment Status<br>• **Extraction Periodicity:** per release<br>• **Information Systems / Databases:** Internal Application Database, Release Store<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R7.3 – Operate coordinated vulnerability disclosure

| Requirement |
|---|
| **ID:** R7.3 **Name:** Operate coordinated vulnerability disclosure |
| **Description:** The system must operate a publicly identifiable disclosure intake for security researchers, triage submissions through the vulnerability process, and publish advisories once fixes are available. |
| **Requirement Origin:** Disclosure Policy & Security Researcher Community | (Realizes: PUC 7.3) |
| **Security & Privacy Constraints:**<br>**Chain** Coordinated Vulnerability Disclosure — `CRA Annex I Part II (4)-(6)+Art. 13(8),(17)` → `SO-D-02.3-002` · `NIS 2 Art. 21(2)(e)` → `SO-D-02.3-003` → `PRIN-ENG-02` → CSF ID.RA-01, GV.SC-04 |
| **Interfaces:** Disclosure intake channel; triage queue; publication view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Disclosure Intake Record, Advisory Record<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R8 – Manage Secure Development and Releases

##### R8.1 – Enforce release pipeline security gates

| Requirement |
|---|
| **ID:** R8.1 **Name:** Enforce release pipeline security gates |
| **Description:** The system must enforce blocking security checks on every release candidate — code scanning, dependency analysis, and secret detection — with override restricted to named approvers and every override recorded. |
| **Requirement Origin:** Secure Development Lifecycle Policy & Release Operations Procedure | (Realizes: PUC 8.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN20** Secure-by-Default Configuration & Reset — `GDPR Art. 25(2)` → `PO-D-03.4-001` · `CRA Annex I 2(b)+(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01<br>**Chain** Attack-Surface Limitation in Production — `CRA Annex I Part I (2)(j)` → `SO-D-07.1-002`, `SO-D-07.2-002` → `PRIN-ENG-02` → CSF PR.PS-06, GV.PO-02, PR.PS-01, PR.PS-02 |
| **Interfaces:** Pipeline gate console; build and release record view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Pipeline Gate Record, Override Record<br>• **Extraction Periodicity:** per release<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R8.2 – Maintain software bills of materials

| Requirement |
|---|
| **ID:** R8.2 **Name:** Maintain software bills of materials |
| **Description:** The system must generate and maintain a software bill of materials for every release — including third-party and open-source components — retained per release and producible for conformity assessment. |
| **Requirement Origin:** Conformity Assessment Requirement & Component Governance Programme | (Realizes: PUC 8.2) |
| **Security & Privacy Constraints:**<br>**Chain** SBOM Maintenance — `CRA Annex I Part II (1)+Art. 13(6)` → `SO-D-06.2-002` → `PRIN-ENG-05` → CSF ID.AM-02, GV.SC-04 |
| **Interfaces:** SBOM generation interface; component inventory view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security, Suppliers & Assessors<br>• **Data Sources:** Component Inventory Record<br>• **Extraction Periodicity:** per release<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R8.3 – Version and roll back AI models

| Requirement |
|---|
| **ID:** R8.3 **Name:** Version and roll back AI models |
| **Description:** The system must version every verification model with its lineage (training data reference, evaluation results) and support rollback to the previous model version within 30 minutes of a triggering quality or safety event. |
| **Requirement Origin:** AI Model Lifecycle Procedure & Field Quality Escalations | (Realizes: PUC 8.3) |
| **Security & Privacy Constraints:**<br>**NFR-RN15** AI Model Resilience & Fail-Safe Reversion — `AI Act Art. 15(3)` → `SO-D-01.4-004` → `PRIN-ENG-04` → CSF PR.IR-03, PR.IR-04, PR.DS-11 |
| **Interfaces:** Model registry console; promotion and rollback controls |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Model Version Record, Model Evaluation Record<br>• **Extraction Periodicity:** per model release<br>• **Information Systems / Databases:** Internal Application Database, Release Store<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R9 – Govern AI Quality and Conformity

##### R9.1 – Maintain AI risk management and conformity documentation

| Requirement |
|---|
| **ID:** R9.1 **Name:** Maintain AI risk management and conformity documentation |
| **Description:** The system must maintain the AI risk-management file (continuous identification, evaluation, and treatment of risks across the lifecycle) and the complete conformity documentation set — technical file, instructions, and assessment records — kept current for the statutory retention period. |
| **Requirement Origin:** High-Risk AI Conformity Programme & Notified Body Assessment | (Realizes: PUC 9.1) |
| **Security & Privacy Constraints:**<br>**Chain** AI Risk-Management & Documentation Family — `AI Act Art. 9` → `SO-D-02.1-004`, `SO-D-09.2-004` · `AI Act Art. 10` → `SO-D-05.1-004` · `AI Act Art. 15(1)` → `SO-D-07.1-004` · `AI Act Art. 11+Annex IV` → `SO-D-09.4-004` → `PRIN-ENG-05` → CSF GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, PR.PS-06 |
| **Interfaces:** Risk-management file workspace; conformity documentation repository |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder AI Governance & Privacy, Suppliers & Assessors<br>• **Data Sources:** AI Risk File, Conformity Documentation Set<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R9.2 – Monitor AI accuracy, drift, and bias

| Requirement |
|---|
| **ID:** R9.2 **Name:** Monitor AI accuracy, drift, and bias |
| **Description:** The system must continuously monitor verification accuracy against the quality baseline, alert on degradation beyond the agreed threshold, run quarterly fairness assessments across demographic groups with disparity reporting, and feed post-market data back into the risk file. |
| **Requirement Origin:** Post-Market Monitoring Programme & Fairness Assurance Commitments | (Realizes: PUC 9.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN24** AI Event Logging over Lifetime — `AI Act Art. 12(1)+Art. 19` → `SO-D-10.2-004`, `SO-D-05.2-004` → `PRIN-ENG-07` → CSF PR.PS-04, DE.CM-09, DE.AE-03<br>**NFR-RN25** AI Post-Market Monitoring Integration — `AI Act Art. 72` → `SO-D-10.1-004` → `PRIN-ENG-02` → CSF DE.CM-09, ID.IM-04<br>**NFR-RN15** AI Model Resilience & Fail-Safe Reversion — `AI Act Art. 15(3)` → `SO-D-01.4-004` → `PRIN-ENG-04` → CSF PR.IR-03, PR.IR-04, PR.DS-11 |
| **Interfaces:** Monitoring dashboards; drift and fairness reporting; alerting interface |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder AI Governance & Privacy, Government Border Authorities<br>• **Data Sources:** Decision Metrics Store, Fairness Assessment Record<br>• **Extraction Periodicity:** continuous / quarterly<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R9.3 – Test AI systems adversarially and explain decisions

| Requirement |
|---|
| **ID:** R9.3 **Name:** Test AI systems adversarially and explain decisions |
| **Description:** The system must support scheduled adversarial testing of the verification pipeline (presentation-attack and evasion exercises) and produce per-decision explainability output (confidence band and contributing factors) for officer review and oversight reporting. |
| **Requirement Origin:** Adversarial Testing Cycle & Human-Oversight Obligation | (Realizes: PUC 9.3) |
| **Security & Privacy Constraints:**<br>**NFR-RN30** AI Transparency & Deployer Interpretability — `AI Act Art. 13` → `SO-D-09.1-004` → `PRIN-ENG-05` → CSF GV.OC-03, GV.RM-01<br>**Chain** AI Adversarial & Real-World Testing — `AI Act Art. 9(6)-(7)+Art. 15(4)-(5)+Art. 60` → `SO-D-02.4-004`, `SO-D-07.2-004`, `SO-D-10.3-004` → `PRIN-ENG-02` → CSF ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 |
| **Interfaces:** Adversarial test harness interface; explainability artefact viewer |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder AI Governance & Privacy, SecureBorder Operations & Security<br>• **Data Sources:** Adversarial Test Record, Decision Explainability Record<br>• **Extraction Periodicity:** quarterly<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R10 – Manage Governance, Risk, and Vendors

##### R10.1 – Maintain unified impact and risk assessments

| Requirement |
|---|
| **ID:** R10.1 **Name:** Maintain unified impact and risk assessments |
| **Description:** The system must maintain the unified assessment record — privacy impact, fundamental-rights leg, AI risk file linkage, and enterprise risk analysis — as one evidence base with dual outputs, reviewed on material change and at least annually. |
| **Requirement Origin:** Unified Assessment Approach & Annual Governance Cycle | (Realizes: PUC 10.1) |
| **Security & Privacy Constraints:**<br>**Chain** Unified Lifecycle Assessment Family (T-003) — `GDPR Art. 35` → `PO-D-09.2-001` · `CRA Art. 13(2)` → `SO-D-09.2-002` · `NIS 2 Art. 21(2)(a)` → `SO-D-09.2-003` · `AI Act Art. 9(1)` → `SO-D-09.2-004` → `PRIN-ENG-05` → CSF ID.RA-01, ID.RA-05, ID.RA-06, GV.RM-01, GV.RM-06, RS.AN-03<br>**Chain** Governance Policy Family — `GDPR Art. 24` → `PO-D-09.1-001` · `NIS 2 Art. 20` → `SO-D-09.1-003` · `NIS 2 Art. 21(2)(h)` → `SO-D-01.1-003` → `PRIN-ENG-05` → CSF GV.PO-01, GV.PO-02, GV.RM-04, GV.OV-03, PR.DS-01, PR.DS-02 |
| **Interfaces:** Assessment workbench; evidence collection view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder AI Governance & Privacy, SecureBorder Executive Leadership<br>• **Data Sources:** Assessment Record, Risk Register<br>• **Extraction Periodicity:** annual / on change<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R10.2 – Assess vendors and record component provenance

| Requirement |
|---|
| **ID:** R10.2 **Name:** Assess vendors and record component provenance |
| **Description:** The system must maintain vendor assessments covering security practices and component quality, record provenance for supplied hardware and software components, and track vendor findings to closure. |
| **Requirement Origin:** Supplier Due Diligence Programme & Vendor Assessment Cycle | (Realizes: PUC 10.2) |
| **Security & Privacy Constraints:**<br>**Chain** Vendor & Supply-Chain Family (T-004) — `GDPR Art. 28` → `PO-D-06.1-001`, `PO-D-06.3-001` · `CRA Annex I Part I (2)` → `SO-D-06.1-002` · `NIS 2 Art. 21(2)-(3)` → `SO-D-06.1-003`, `SO-D-06.3-003`, `SO-D-07.1-003` → `PRIN-ENG-05` → CSF GV.SC-01, GV.SC-02, GV.SC-03, ID.RA-02 |
| **Interfaces:** Vendor assessment console; component provenance register |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security, Suppliers & Assessors<br>• **Data Sources:** Vendor Assessment Record, Component Provenance Record<br>• **Extraction Periodicity:** annual / per vendor<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R10.3 – Maintain compliance reporting and audits

| Requirement |
|---|
| **ID:** R10.3 **Name:** Maintain compliance reporting and audits |
| **Description:** The system must produce compliance reports on request within the committed service window and track internal and external audit findings to closure. |
| **Requirement Origin:** Certified Management System Cycle & Authority Inspection Readiness | (Realizes: PUC 10.3) |
| **Security & Privacy Constraints:**<br>**Chain** Documentation & Compliance Family — `CRA Art. 13+Annex VII` → `SO-D-09.4-002`, `SO-D-10.2-002` · `GDPR Art. 5(2)+Art. 24` → `PO-D-10.2-001`, `PO-D-10.3-001` · `NIS 2 Art. 21(2)(f)` → `SO-D-10.3-003` → `PRIN-ENG-05` → CSF GV.OC-03, GV.OV-01, GV.OV-03, GV.PO-02, ID.AM-03, PR.PS-04 |
| **Interfaces:** Compliance dossier builder; audit evidence repository; report submission interface |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Executive Leadership, Suppliers & Assessors<br>• **Data Sources:** Compliance Report Record, Audit Finding Record<br>• **Extraction Periodicity:** on demand / annual<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Should |

---

#### R11 – Manage Training and Competence

##### R11.1 – Deliver security and privacy awareness training

| Requirement |
|---|
| **ID:** R11.1 **Name:** Deliver security and privacy awareness training |
| **Description:** The system must track delivery of the annual security and privacy awareness programme to the whole workforce, recording completion and overdue status per person. |
| **Requirement Origin:** Annual Awareness Programme & Workforce Compliance Tracking | (Realizes: PUC 11.1) |
| **Security & Privacy Constraints:**<br>**Chain** Awareness & Hygiene Training — `NIS 2 Art. 21(2)(g), Art. 21(3)` → `SO-D-08.1-003`, `SO-D-08.2-003` → `PRIN-ENG-01` → CSF PR.AT-01, PR.PS-01 |
| **Interfaces:** Training delivery interface; completion register |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder Operations & Security<br>• **Data Sources:** Training Assignment Record, Completion Record<br>• **Extraction Periodicity:** annual<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R11.2 – Deliver oversight and AI competence training

| Requirement |
|---|
| **ID:** R11.2 **Name:** Deliver oversight and AI competence training |
| **Description:** The system must track role-specific competence delivery — oversight tools and override logic for border control officers, AI limitations and escalation for oversight staff, and board-level briefings — with completion recorded before role activation. |
| **Requirement Origin:** Human-Oversight Obligation & Role Activation Workflow | (Realizes: PUC 11.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN29** Human Oversight Effectiveness — `AI Act Art. 14` → `SO-D-08.2-004` → `PRIN-ENG-01` → CSF PR.AT-02, PR.AT-01, GV.RR-02 |
| **Interfaces:** Competence programme interface; oversight eligibility view |
| **Dependencies:**<br>• **Stakeholders:** SecureBorder AI Governance & Privacy, Government Border Authorities<br>• **Data Sources:** Competence Curriculum Record, Role Activation Record<br>• **Extraction Periodicity:** on assignment<br>• **Information Systems / Databases:** Internal Application Database<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

---

## 3. Non-Functional Requirements & Transversal Attributes

### 3.1 General Operational Quality Attributes (Table 7)

Function-specific security & privacy NFRs are absorbed directly into the corresponding requirement cards as `Security & Privacy Constraints` rows (§2.2.3); only the cross-cutting transport constraint stays in this table.

The non-functional requirements define the platform's performance, availability, and quality targets:

*Table 7. List of non-functional requirements*

| ID | Requirement | Priority | Type |
|---|---|---|---|
| **RN1** | The gate must produce a passage decision within 3 seconds of capture and complete enrolment within 60 seconds. | MUST | Performance & Efficiency |
| **RN2** | The verification service must maintain 99.99% monthly availability during published border-opening hours, excluding announced maintenance. | MUST | Availability |
| **RN3** | The platform must sustain 500 travellers per hour per gate and absorb 3× peak surge without degradation. | MUST | Scalability |
| **RN4** | The back-office must support recovery within 1 hour (RTO) with at most 15 minutes of data loss (RPO). | MUST | Recoverability |
| **RN5** | Raw biometric captures must be discarded within 5 seconds of template extraction; traveller rights responses must complete within the 30-day statutory window. | MUST | Privacy Responsiveness |
| **RN6** | 100% of passage decisions must be recorded as token-only entries in tamper-evident storage retained for the statutory floor (10 years). | MUST | Auditability |
| **RN7** | The verification AI must sustain ≥99.5% measured accuracy with an automatic alert on degradation beyond 1%. | MUST | AI Quality |
| **RN8** | Quarterly fairness assessments must evidence false-accept disparity below 1% and false-reject disparity below 2% across demographic groups. | MUST | AI Fairness |
| **RN9** | All integrations with government authority systems must communicate exclusively over authenticated, integrity-protected channels. | MUST | Interoperability |
| **RN10** | Per-country deployments must remain logically and physically isolated from each other, with no cross-border data commingling. | MUST | Deployment Isolation |
| **RN13** | All data crossing the gate–back-office, back-office–authority, and fleet–update channels shall be cryptographically protected in transit with state-of-the-art mechanisms and integrity verification, refusing unauthenticated channels. | MUST | Security — Transport (GDPR Art. 32(1)(b)+Art. 32(2) → PO-D-01.2-001 · CRA Annex I Part I (2)(e)+(j) → SO-D-01.2-002 → PRIN-ENG-01 → CSF PR.DS-02, PR.IR-01) |

---

---


### 3.2 Security & Privacy Requirements Catalog

The function-specific security & privacy requirements are absorbed in-card as `Security & Privacy Constraints` rows carrying their full tracing chains; this catalog states each of them as a complete, verifiable requirement sentence, so the demanded behavior is readable without following a chain. The cross-cutting transport requirement remains the standalone row of Table 7.

*Table 8. Security & Privacy Requirements (statement catalog; chains live on the absorbing cards)*

| ID | Requirement | Priority | Type | Absorbed In |
|---|---|---|---|---|
| **RN11** | The system shall store traveller biometric templates only in cryptographically protected form under keys held in separated custody, such that compromise of the template store alone does not yield usable biometric identifiers. | MUST | Security — Data at Rest | R1.1, R1.3 |
| **RN12** | The system shall hold cryptographic keys under custody separated from the data and services they protect, executing key lifecycle operations only through verified, separated control. | MUST | Security — Key Management | R1.1, R1.2 |
| **RN14** | The system shall protect security-relevant records and commands against unauthorized alteration or injection across their full path, detecting and refusing any integrity violation. | MUST | Security — Integrity | R1.2, R1.3, R6.1 |
| **RN15** | The verification AI shall sustain its approved operating behavior and, upon anomaly, degradation, or failure, revert to a fail-safe state that refuses passage or refers the traveller to the manual lane rather than defaulting to allow. | MUST | AI — Resilience | R1.2, R8.3, R9.2 |
| **RN16** | The system shall verify the identity of every data-subject requester against verified identifiers before executing any right, delivering outcomes only to the verified titular subject. | MUST | Privacy — Rights | R4.1 |
| **RN17** | The system shall manage operator identities through a governed lifecycle covering creation, mutation, deprovisioning, and periodic review, refusing access without a current, reviewed identity state. | MUST | Security — Identity | R3.1, R3.3 |
| **RN18** | The system shall authenticate operators through multi-factor verification before granting access to operational or administrative functions. | MUST | Security — Authentication | R3.2 |
| **RN19** | The system shall mediate security-relevant instructions through verification that the requesting actor holds authorization for that instruction class, rejecting and recording instructions from unverified actors. | MUST | Security — Authorization | R2.1, R3.3 |
| **RN20** | The system shall initialize every component under a restrictive secure-by-default configuration and refuse or reset weakened configurations to the secure baseline. | MUST | Security — Configuration | R1.2, R8.1 |
| **RN21** | The system shall dispatch every statutory notification through a single unified pipeline whose timeline is enforced across the applicable regimes, so that no notification bypasses or exceeds its regulatory clock. | MUST | Compliance — Notification | R6.1 |
| **RN22** | The system shall record product activity, including security-relevant events and refusals, as tamper-evident entries, such that suppression or alteration is detectable. | MUST | Security — Auditability | R1.2, R5.1 |
| **RN23** | The system shall manage every incident through a handled lifecycle reaching verified closure, such that prematurely or silently abandoned incidents are detectable. | MUST | Compliance — Incident Response | R5.2, R5.3 |
| **RN24** | The system shall log AI events — serving decisions, model state changes, and monitoring signals — over the model lifetime, keeping the behavior of every deployed version evidenced. | MUST | AI — Logging | R1.2, R9.2 |
| **RN25** | The system shall integrate AI performance monitoring into the post-market monitoring pipeline, so that accuracy, drift, and disparity signals reach detection independently of the serving path. | MUST | AI — Monitoring | R5.1, R9.2 |
| **RN26** | The system shall record breach awareness and containment actions as they occur, evidencing the state of every statutory notification obligation. | MUST | Compliance — Breach Records | R5.2, R6.1 |
| **RN27** | The system shall distribute software and model updates only through authenticated, integrity-verified channels for the full support period, installing nothing that fails signature verification. | MUST | Security — Supply Chain | R7.2 |
| **RN28** | The system shall execute traveller erasure and portability through the managed rights pipeline across all stores, delivering outcomes only to the verified titular subject. | MUST | Privacy — Rights | R4.1 |
| **RN29** | The system shall keep human oversight operative for automated decisions, with attribution, rationale, and reviewability, so that oversight effectiveness is evidenced rather than asserted. | MUST | AI — Oversight | R11.2, R2.1 |
| **RN30** | The system shall provide the deployer with the information and interpretability means required to understand and communicate the AI system's capabilities, limitations, and decision basis. | MUST | AI — Transparency | R9.3 |

### 3.3 Requirement Type Coverage

The specification covers the following requirement types. Types recorded as not represented carry no requirement in this specification because no source warrant exists for them (Rule R6); they are candidates for a future round if the client authors them.

*Table 9. Requirement type coverage*

| Requirement Type | Represented By | Coverage |
|---|---|---|
| Functional | 28 requirement cards (§2.2) | Represented |
| Performance & Efficiency | RN1 | Represented |
| Availability | RN2 | Represented |
| Scalability | RN3 | Represented |
| Recoverability | RN4 | Represented |
| Privacy Responsiveness | RN5 | Represented |
| Auditability | RN6, RN22 | Represented |
| AI Quality | RN7 | Represented |
| AI Fairness | RN8 | Represented |
| Interoperability | RN9 | Represented |
| Deployment Isolation | RN10 | Represented |
| Security — Transport | RN13 (Table 7) | Represented |
| Security & Privacy (function-specific) | RN11–RN12, RN14–RN30 (Table 8) | Represented |
| Organizational (PROCESS lane) | `Doc03_Organizational_Requirements.md` (2 DPO requirements) | Represented |
| Usability / Accessibility | — | Not represented — no source warrant in the intake or the Phase 2 objectives (R6); gate-facing interaction is bounded by the statutory service targets (RN1, RN5) |
| Internationalization | — | Not represented — single-language operational context per deployment; a future multi-language deployment would enter through a round |
| Maintainability / Portability | — | Not represented — no source warrant; implementation-era concerns belong to later engineering passes |

---

## Bibliography

- Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
- Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley Professional.
- Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
- ISO/IEC/IEEE. (2018). *ISO/IEC/IEEE 29148: Systems and software engineering — Life cycle processes — Requirements engineering*.
- Mavin, A. et al. (2009). *EARS: Easy Approach to Requirements Syntax*. IEEE International Requirements Engineering Conference.

---

## Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| **3.1.0** | 2026-10-01 | Requirements Engineering Agent | Security & Privacy Requirements catalog added (Table 8: full requirement statements for RN11–RN30 except the cross-cutting RN13, which remains in Table 7); requirement type coverage recorded (Table 9); duplicated bare chain rows removed from R5.2 and R5.3. |
| **1.0.0** | 2026-09-23 | Requirements Engineering Agent | Initial baseline elicitation (GPTools E1.1 structural model). |
| **2.0.0** | 2026-09-28 | Requirements Engineering Agent | Round 1 synthesis (ADR-005): 20 new security & privacy constraints RN11–RN30 absorbed in-card, 51 regulatory chain rows bound to functional cards. |
| **3.0.0** | 2026-09-29 | Requirements Engineering Agent | Round 2 synthesis (ADR-005): R9.3 AI adversarial testing elevated SHOULD → MUST per AI Act Art. 9(6)-(7). |
| **4.0.0** | 2026-10-01 | Requirements Engineering Agent | Modular separation pass: decoupled operational process flows and PUC catalog into [Doc00_Process_and_Operational_Workflows.md](Doc00_Process_and_Operational_Workflows.md). Refocused Doc01 strictly on atomic contractual requirement cards and EARS constraints with bidirectional traceability to PUCs. |
