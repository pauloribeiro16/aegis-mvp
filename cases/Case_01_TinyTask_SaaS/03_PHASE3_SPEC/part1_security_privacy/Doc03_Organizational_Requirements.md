# Doc03 — Organizational Requirements (TinyTask SaaS)

> **Charter.** PROCESS-lane requirements of Phase 3 Part 1 (ADR-008 D1) — obligations whose realization class is PROCESS/CAPABILITY (ADR-003), routed from objectives verdicted `No functional carrier (organizational)` in [`synthesis_rounds/OBJECTIVE_MAPPING.md`](synthesis_rounds/OBJECTIVE_MAPPING.md) and from carve-outs recorded there. The technology legs of the same capabilities remain in `Doc01`.
>
> **Scope and proportionality.** Company profile: **8 employees, micro-enterprise, hosted B2B SaaS; GDPR and CRA confirmed applicable, NIS2 below the size threshold.** Every requirement below is written to be operable by two people wearing two hats. The proportionality basis per objective is recorded in [`analysis_v0_to_v1/PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md`](analysis_v0_to_v1/PROPORTIONALITY_AUDIT_ORGANIZATIONAL_LANE.md), which also names the six duties whose proportional form is not yet decided and therefore do not yet appear here.

## 1. Derivation contract

| Element | Rule |
|---|---|
| Subject | EARS with organizational subject: `The organization shall …` |
| Atomicity | One congruent demand set per requirement (ADR-007 D1) |
| Acceptance | Volere fit criterion — deterministic pass/fail (PRIN-ENG-05) |
| Verification | `INSPECT` / `DEMONSTRATE` / `ANALYZE` dominant |
| Owner | From Phase 2 `Doc01` — Governance & Stakeholder Matrix |
| Chain | `regulation article → Phase 2 objective → organizational control anchor` |
| Anchors (primary) | NIST CSF 2.0 — `baseline/CONTROLS/NIST_CSF_2.0/` |
| Specificity | L2 ceiling (guidelines §2.5) — no invented operational parameters |
| Rounds | ADR-005 per-item verdicts; recorded in [`synthesis_rounds/ROUND2_REGISTER.md`](synthesis_rounds/ROUND2_REGISTER.md) |

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

## 3. Requirements

### D-01 — Data Protection

| Requirement |
|---|
| **ID:** ORG-D-01.4-001 **Name:** Route detected corruption of stored commercial state to an accountable owner |
| **Statement (EARS):** Where the organization detects corruption or unauthorised modification of stored billing or subscription state, the organization shall record the detection and route it to a named owner for assessment. |
| **Requirement Origin:** TinyTask SaaS founders' commercial subscription model — the corruption-reporting leg of data integrity, carved out of the product lane by Round 2 P4(a) |
| **Fit Criterion:** every detected corruption or unauthorised modification of billing or subscription state produces a retrievable record naming the detecting party and a named owner; a detection with no owner record does not close. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 33(1) — accuracy of records on request → D-01.4 objectives
| **Control Anchors:** NIST CSF 2.0 `DE.CM-09`, `GV.RR-02` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; support contact • **Owner:** Product owner (founder) • **Cadence:** on detection • **Information Systems / Databases:** Internal Application Database (commercial state records); Security Audit Subsystem |
| **Priority:** Must |

### D-02 — Vulnerability Management

| Requirement |
|---|
| **ID:** ORG-D-02.1-001 **Name:** Assess components and dependencies before use |
| **Statement (EARS):** Where the organization adds a third-party service or incorporates an external software component into the product, the organization shall assess its known vulnerabilities and record the decision to accept or reject it. |
| **Requirement Origin:** TinyTask SaaS platform build — manufacturer obligations for a product with digital elements |
| **Fit Criterion:** every external component in a released build has a recorded assessment of known exploitable vulnerabilities and a recorded accept/reject decision; no component reaches a release without both records. |
| **Verification Method:** INSPECT |
| **Chain:** CRA Annex I Part I (2)(b) + Annex II → D-02.1 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.SC-05`, `PR.PS-02` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; engineering • **Owner:** Product owner (founder) • **Cadence:** on each release • **Information Systems / Databases:** Internal Application Database (dependency and component inventory) |
| **Priority:** Must |

| Requirement |
|---|
| **ID:** ORG-D-02.3-001 **Name:** Publish a vulnerability disclosure contact |
| **Statement (EARS):** The organization shall publish a contact point that a third party can use to report a security defect in the product, and shall acknowledge each report. |
| **Requirement Origin:** TinyTask SaaS platform build — coordinated vulnerability disclosure duty for a manufacturer placing a product with digital elements on the market |
| **Fit Criterion:** a published contact point exists and is reachable from the product documentation; every report received has a retrievable acknowledgement. |
| **Verification Method:** INSPECT |
| **Chain:** CRA Art. 14 — coordinated vulnerability disclosure → D-02.3 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.SC-01`, `GV.OC-03` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Reporters; founders • **Owner:** Product owner (founder) • **Cadence:** continuous; reviewed on each release • **Information Systems / Databases:** — |
| **Priority:** Must |

### D-03 — Access Control

| Requirement |
|---|
| **ID:** ORG-D-03.2-001 **Name:** Issue and maintain documented processing instructions |
| **Statement (EARS):** The organization shall issue written instructions to every person acting on its behalf or on its behalf as a processor, and shall keep those instructions retrievable for as long as the person acts. |
| **Requirement Origin:** TinyTask SaaS customer relationships — controller and processor duties over customer account metadata and customer end-user task data |
| **Fit Criterion:** every person acting for the organization has a retrievable written instruction set covering confidentiality and the processing scope they are authorised for; no person acts without one. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 29 + Art. 28(3)(b),(f) — documented instructions → D-03.2 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.RR-02`, `GV.OC-03` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** All staff; customers as data subjects • **Owner:** Founders • **Cadence:** on joining; reviewed annually • **Information Systems / Databases:** — |
| **Priority:** Must |

### D-04 — Incident Response

| Requirement |
|---|
| **ID:** ORG-D-04.1-001 **Name:** Operate the breach detection, containment and notification runbook |
| **Statement (EARS):** When the organization becomes aware of a personal data breach or of an actively exploited vulnerability in the product, the organization shall execute the documented runbook covering detection and triage, containment, notification to the supervisory authority within the applicable statutory period, notification to affected data subjects where the duty applies, and CRA reporting of actively exploited vulnerabilities. |
| **Requirement Origin:** TinyTask SaaS hosted service — breach notification duties and manufacturer reporting duties |
| **Fit Criterion:** for each qualifying event a retrievable record shows the awareness moment, the containment action, and the notification decision with its date; where notification was due, the record shows it was made within the statutory period; where it was not, the record shows the basis for that determination. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 33 + CRA Art. 14 — breach and vulnerability reporting → D-04.1 objectives
| **Control Anchors:** NIST CSF 2.0 `RS.CO-02`, `ID.IM-04`, `GV.OC-03` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; affected data subjects; supervisory authority; recipients of the product • **Owner:** Founders • **Cadence:** on awareness; runbook reviewed annually • **Information Systems / Databases:** Security Audit Subsystem (detection record) |
| **Priority:** Must |

### D-06 — Supply Chain & Third-Party Security

| Requirement |
|---|
| **ID:** ORG-D-06.1-001 **Name:** Secure processor agreements and the sub-processor chain |
| **Statement (EARS):** Where the organization engages a sub-processor, the organization shall ensure a written agreement carries the processor terms and shall maintain a retrievable list of the sub-processors in use. |
| **Requirement Origin:** TinyTask SaaS payment gateway and messaging service relationships — processor-side contractual floor |
| **Fit Criterion:** each sub-processor in use has a retrievable written agreement carrying the required terms; the sub-processor list names every current sub-processor and the data categories each handles. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 28(3) + Art. 28(4) — processor terms and sub-processors → D-06.1 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.SC-04`, `GV.SC-05` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Sub-processors; customers as controllers; founders • **Owner:** Founders • **Cadence:** on engagement; reviewed annually • **Information Systems / Databases:** — |
| **Priority:** Must |

### D-09 — Governance & Documentation

| Requirement |
|---|
| **ID:** ORG-D-09.1-001 **Name:** Maintain the data-protection accountability policy set |
| **Statement (EARS):** The organization shall maintain a written statement of how it implements the data-protection principles for its own processing, and shall review it whenever its processing, systems, or suppliers change. |
| **Requirement Origin:** TinyTask SaaS founders' business case — accountability for the data-protection principles, at the minimum scope this company operates |
| **Fit Criterion:** a retrievable written statement exists covering each principle the company relies on; the statement records the date of its last review and the change that prompted it, or states that no triggering change has occurred since the last review. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 5(2) + Art. 24 — accountability → D-09.1 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.PO-01`, `GV.OC-03` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; customers as data subjects • **Owner:** Founders • **Cadence:** on change; reviewed at least annually • **Information Systems / Databases:** — |
| **Priority:** Must |

| Requirement |
|---|
| **ID:** ORG-D-09.2-001 **Name:** Assess high-risk processing before it begins |
| **Statement (EARS):** Where the organization intends to introduce processing that is likely to result in a high risk to individuals, the organization shall assess that risk before the processing begins and record whether the processing may proceed. |
| **Requirement Origin:** TinyTask SaaS feature development — the assessment duty that binds before high-risk processing starts |
| **Fit Criterion:** for each processing activity classified as likely high risk, a retrievable assessment predates the start of the processing and records the decision to proceed or not to; no activity classified as high risk begins without that record. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 35 — assessment before high-risk processing → D-09.2 objectives
| **Control Anchors:** NIST CSF 2.0 `ID.RA-04`, `GV.RM-01` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; affected data subjects • **Owner:** Founders • **Cadence:** on introducing a new processing activity; reviewed on material change • **Information Systems / Databases:** — |
| **Priority:** Should |

| Requirement |
|---|
| **ID:** ORG-D-09.4-001 **Name:** Maintain the record of processing activities |
| **Statement (EARS):** The organization shall maintain a retrievable record of each processing activity it carries out, naming for each the purposes, the categories of personal data, the recipients, and the retention period. |
| **Requirement Origin:** TinyTask SaaS controller and processor roles over customer account metadata and customer task data |
| **Fit Criterion:** every processing activity the organization carries out appears in the record with the four named elements populated; the record and the data actually held agree. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 30 — records of processing activities → D-09.4 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.OC-01`, `GV.RR-02` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; customers as controllers • **Owner:** Founders • **Cadence:** continuous; reviewed on introducing a new activity • **Information Systems / Databases:** Internal Application Database (privacy event trail) |
| **Priority:** Must |

### D-10 — Monitoring & Audit

| Requirement |
|---|
| **ID:** ORG-D-10.2-001 **Name:** Retain compliance and technical records |
| **Statement (EARS):** The organization shall retain, for the period stated in the record, each record of the assessments, decisions, notifications and audit entries it produces in the course of its compliance and product operations, in a form that remains retrievable and attributable.
| **Requirement Origin:** TinyTask SaaS accountability for its compliance position and for the technical state of the product |
| **Fit Criterion:** each record class named in the statement has a retrievable copy for the retention period stated, and the copy is the one produced at the time the event occurred. |
| **Verification Method:** INSPECT |
| **Chain:** GDPR Art. 5(2) + CRA Art. 13 — retained compliance and technical records → D-10.2 objectives
| **Control Anchors:** NIST CSF 2.0 `GV.PO-02`, `DE.CM-09` (`baseline/CONTROLS/NIST_CSF_2.0/`)
| **Dependencies:** • **Stakeholders:** Founders; supervisory authority • **Owner:** Founders • **Cadence:** continuous • **Information Systems / Databases:** Security Audit Subsystem |
| **Priority:** Must |

## 4. Coverage linkage

| Phase 2 objective | Leg / carve-out | ORG requirement |
|---|---|---|
| `SO-D-01.4-002` | corruption-reporting leg (Round 2 P4(a)) | `ORG-D-01.4-001` |
| `SO-D-02.1-002` | known exploitable vulnerabilities in the product | `ORG-D-02.1-001` |
| `SO-D-06.1-002` | third-party / open-source component due diligence | `ORG-D-02.1-001` |
| `SO-D-06.2-002` | machine-readable component inventory | `ORG-D-02.1-001` |
| `SO-D-02.3-002` | coordinated vulnerability disclosure policy | `ORG-D-02.3-001` |
| `SO-D-03.2-001` | documented instructions to authorized persons | `ORG-D-03.2-001` |
| `SO-D-03.3-001` | processor-side documented instructions and confidentiality | `ORG-D-03.2-001` |
| `SO-D-04.1-001` | breach detection and triage, awareness moment | `ORG-D-04.1-001` |
| `SO-D-04.2-001` | breach containment | `ORG-D-04.1-001` |
| `SO-D-04.3-001` | supervisory-authority notification | `ORG-D-04.1-001` |
| `SO-D-04.3-002` | actively-exploited-vulnerability reporting | `ORG-D-04.1-001` |
| `SO-D-06.1-001` | processor guarantees | `ORG-D-06.1-001` |
| `SO-D-06.3-001` | contract floor and sub-processor chain | `ORG-D-06.1-001` |
| `PO-D-09.1-001` | accountability policies | `ORG-D-09.1-001` |
| `PO-D-09.2-001` | assessment before high-risk processing | `ORG-D-09.2-001` |
| `PO-D-09.4-001` | records of processing activities | `ORG-D-09.4-001` |
| `SO-D-10.2-001` | compliance records with integrity | `ORG-D-10.2-001` |
| `SO-D-10.2-002` | technical and risk-assessment documentation preserved | `ORG-D-10.2-001` |

## 5. Objectives routed but not yet specified

Sixteen duties were measured across the 32 organizational verdicts; ten are specified above. Six remain **blocked on a proportionality decision** — the duty binds at this scale, but the form the objective implies is disproportionate for an eight-person company, and an EARS statement with a fit criterion cannot be written until the proportional form is fixed. They are listed here so no objective is silently dropped:

| Duty | Objectives | What the decision is |
|---|---|---|
| Ongoing confidentiality, integrity, availability and resilience | `SO-D-04.4-001`, `SO-D-10.1-001`, `PO-D-01.1-001` carve-out | Whether a standing resilience duty exists at this scale or the responsibility split with the hosting provider is the whole of it |
| Testing of measures' effectiveness | `SO-D-02.1-001`, `SO-D-10.3-001` | Whether effectiveness testing is an annual self-review by the founders or something narrower |
| Secure update and advisory distribution | `SO-D-02.2-002`, `SO-D-05.2-002`, `SO-D-07.3-002` | The intake already records a proportional answer (`ORG-INT-02`); whether that closes the three objectives or only one |
| Availability of essential functions after an incident | `SO-D-04.2-002` | Whether this is a product-side property or a process duty at this scale |
| Product testing with written reports | `SO-D-10.3-002` | Whether a written testing regime exists or only the release-check obligation already carried by `ORG-D-02.1-001` |
| Technical documentation and conformity assessment | `SO-D-09.3-002`, `SO-D-09.4-002` | What "technical documentation" means for a hosted SaaS product, where the product is not a physical thing to document |

## 6. Objectives closed without a requirement

| Duty | Objectives | Basis |
|---|---|---|
| Data-protection advisory and monitoring role | `SO-D-08.1-001`, `SO-D-08.2-001` | The intake already accepts a proportional dual-hat advisory role at micro scale (`ORG-INT-03`); a distinct officer function is not what these objectives require here |

## 7. Version history

| Version | Date | Author | Change |
|---|---|---|---|
| **1.0.0** | 2026-10-10 | Requirements Engineering Agent | Organizational lane specified for TinyTask SaaS: 10 requirements across 8 duties, covering 18 of the 32 organizational verdicts plus the Round 2 P4(a) carve-out. Six duties held pending a proportionality decision; one closed against a recorded case decision. |