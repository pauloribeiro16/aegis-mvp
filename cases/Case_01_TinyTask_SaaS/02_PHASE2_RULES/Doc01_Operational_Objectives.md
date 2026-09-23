---
document_id: AEGIS-P2-DOC01
title: Privacy and Security Operational Objectives Catalog (Case 01 — TinyTask SaaS)
phase: 2
version: 1.1
date: 2026-09-22
case: Case_01_TinyTask_SaaS
tier: MICRO
applicable_regulations: [GDPR, CRA]
total_active_subdomains: 35
realization_class: TECHNOLOGY
status: APPROVED
---

# Privacy & Security Operational Objectives — Case 01 (TinyTask SaaS)

> **Document Purpose:** Defines the Operational Objectives for TinyTask SaaS across all 35 active sub-domains, organised domain by domain. Each sub-domain establishes the baseline High-Level Goal (`SG-D-XX.Y.HL`), its high-level Operational Translation for TinyTask, and a structured tabular specification separating the distinct operational scopes of GDPR (Personal Data protection) and CRA (Product & Software Security).

---

## §1 Governance & Structure Guide

### 1.1 Separation of Regulatory Ambits (GDPR vs CRA)
Where both GDPR and CRA apply to the same sub-domain, they bind **distinct operational ambits** and cannot be conflated into a single objective:
- **GDPR Operational Objectives (`PO-` or `SO-` with GDPR scope):** Focus on the confidentiality, integrity, availability, and rights of **natural persons and personal data** (e.g. clinic staff and patient records), under GDPR Art. 5, 25, 32, and Chapter III.
- **CRA Operational Objectives (`SO-` with CRA scope):** Focus on the security, tamper-resistance, and cyber-resilience of the **software product, system interfaces, configurations, and supply-chain components** against unauthorized exploitation, under CRA Annex I and Art. 13.

### 1.2 High-Level Goal Operational Translation
In accordance with ISO/IEC 27001:2022 clause 6.2 and ISO 29148, each sub-domain begins by restating the common Baseline Goal (`SG-D-XX.Y.HL`) and providing its **Operational Translation** — the high-level system principle that explains *how* the organization satisfies the goal before descending into testable criteria.

### 1.3 Empirical Verification Methods
Every operational objective is evaluated via one of four empirical methods (INCOSE / ISO 29148):
- `TEST`: Automated assertion, continuous integration test, or runtime security probe.
- `INSPECT`: Systematic review of configuration files, infrastructure-as-code scripts, or audit logs.
- `DEMONSTRATE`: Walkthrough or observable execution of an end-to-end operational flow.
- `ANALYZE`: Systematic risk examination, architectural boundary review, or gap analysis.

---

## §2 Harmonisation of Strategic Tensions

When dual regulations apply, operational tensions are harmonized as follows:

| Tension ID | Sub-Domain | Conflicting Mandates | Resolution Strategy | Operational Impact |
|---|---|---|---|---|
| **T-001** | `D-04.3` | **Incident Notification Timing:** CRA Art. 14 mandates a 24-hour early warning to ENISA/CSIRT for exploited vulnerabilities; GDPR Art. 33 mandates a 72-hour notification to CNPD for personal data breaches. | **Max-SLA Unified Triage:** A single incident triage pipeline routes concurrent alerts: early warning to ENISA within 24 hours, and supervisory/controller notification within 72 hours. | Bound in `SO-D-04.3-001` (GDPR) and `SO-D-04.3-002` (CRA). |
| **T-M-001** | `D-09.2` | **Risk Assessment Cadence:** GDPR requires risk assessment prior to high-risk processing (DPIA); CRA Art. 13 requires continuous risk management over the 5-year support lifecycle. | **Unified Lifecycle Risk Assessment:** Integrate privacy and cybersecurity risk reviews into a single pre-release assessment gate, updated annually or upon material code change. | Bound in `PO-D-09.2-001` (GDPR) and `SO-D-09.2-002` (CRA). |
| **T-M-002** | `D-07.1` | **Secure-by-Design Scope:** GDPR prioritises data-subject rights; CRA mandates systemic resistance against software exploitation. | **Integrated Security & Privacy by Design:** Architectural boundary checks mandate both privacy data minimization and software attack surface reduction in development pipelines. | Bound in `PO-D-07.1-001` (GDPR) and `SO-D-07.1-002` (CRA). |

---

## §3 Domain D-01 — Data Protection & Encryption
> **Domain Lead:** `CTO` | **Supporting Roles:** `Lead Dev` | **Active Sub-Domains:** 4

### D-01.1 — Data at Rest Encryption

**High-Level Baseline Goal (SG-D-01.1.HL):** Data held at rest in storage is protected against unauthorised access through appropriate technical measures — primarily encryption with appropriate key custody — calibrated to the risks identified in the entity's risk assessment and commensurate with the state of the art.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-01.1` requires establishing verifiable system controls that enforce data at rest encryption across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-01.1-001` | Personal data at rest is processed in a manner that ensures appropriate security — including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage — using appropriat... | `AG-D-01.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms data at rest encryption is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.DS-01, PR.DS-10` |
| `SO-D-01.1-002` | Where the product stores data — personal or other — the confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms. | `AG-D-01.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms data at rest encryption is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.DS-01` |

---

### D-01.2 — Data in Transit Encryption

**High-Level Baseline Goal (SG-D-01.2.HL):** Data in transit — across network paths, inter-service calls, and third-party APIs — is protected against unauthorised disclosure and alteration through cryptographic confidentiality and integrity controls (mutual authentication, encryption, integrity verification).

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-01.2` requires establishing verifiable system controls that enforce data in transit encryption across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-01.2-001` | Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) ris... | `AG-D-01.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms data in transit encryption is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.DS-02, PR.IR-01` |
| `SO-D-01.2-002` | Where data is transmitted by the product — personal or other — the confidentiality of the data in transit is protected by encrypting relevant data using state-of-the-art mechanisms, with the attack-surface-limitation ... | `AG-D-01.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms data in transit encryption is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.DS-02, PR.IR-01` |

---

### D-01.3 — Key Management

**High-Level Baseline Goal (SG-D-01.3.HL):** Cryptographic keys and related authentication material are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it; the key custodian and the data consumer are distinct roles under distinct technical and organisational control, with the cryptographic key (not the storage medium) as the necessary condition for intelligibility of the protected data.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-01.3` requires establishing verifiable system controls that enforce key management across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-01.3-001` | Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject — the key, the mapping table, or the tokenisation seed — is kept separately and is ... | `AG-D-01.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms key management is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.DS-01, PR.IR-03` |
| `SO-D-01.3-002` | Cryptographic keys and related authentication material used to protect the confidentiality and integrity of data stored, transmitted or otherwise processed by the product are managed with separation of roles, so that ... | `AG-D-01.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms key management is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.DS-01, PR.AA-05, GV.OV-01` |

---

### D-01.4 — Data Integrity

**High-Level Baseline Goal (SG-D-01.4.HL):** Data integrity is preserved against unauthorised modification across the data lifecycle — at rest, in transit, and in use — with corruption detected, logged, and reported, and with semantic accuracy maintained as the workflow leg of the personal-data principle.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-01.4` requires establishing verifiable system controls that enforce data integrity across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-01.4-001` | Personal data are accurate and, where necessary, kept up to date, and inaccurate data are erased or rectified without delay, with the integrity property anchored to two further legs — storage integrity and the rectifi... | `AG-D-01.4-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms data integrity is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.DS-01, PR.DS-10, PR.DS-10` |
| `SO-D-01.4-002` | The integrity of stored, transmitted, or otherwise processed data — as well as the integrity of commands, programs, and configuration — is protected against any manipulation or modification not authorised by the user,... | `AG-D-01.4-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms data integrity is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.DS-01, PR.DS-10, PR.PS-04` |

---

## §4 Domain D-02 — Vulnerability Management
> **Domain Lead:** `Lead Dev` | **Supporting Roles:** `CTO` | **Active Sub-Domains:** 3

### D-02.1 — Vulnerability Identification

**High-Level Baseline Goal (SG-D-02.1.HL):** Vulnerabilities — including, where in scope, AI-system-specific attack surfaces (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) — are identified on a continuing basis across the system, product, ICT asset, or AI system that an entity operates, manufactures, deploys, or processes, with the resulting identification artefact (vulnerability register, risk-scenario catalogue, SBOM, or risk-management file) feeding the entity's testing, remediation, and notification cascades.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-02.1` requires establishing verifiable system controls that enforce vulnerability identification across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-02.1-001` | The company operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment when the risk r... | `AG-D-02.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms vulnerability identification is enforced for all personal data flows. | `INSPECT` | Lead Dev + CTO | `ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02` |
| `SO-D-02.1-002` | The product is made available on the market without known exploitable vulnerabilities, and vulnerabilities contained in it — including those in the components listed in the software bill of materials — are identified ... | `AG-D-02.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms vulnerability identification is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `ID.RA-01, ID.AM-02, PR.PS-02` |

---

### D-02.2 — Patch Management

**High-Level Baseline Goal (SG-D-02.2.HL):** Vulnerabilities identified in the upstream identification pipeline are addressed and remediated through security updates that are distributed via a secure, separated channel, with the entity-side policy governing patch deployment (severity-classified deployment windows, automated isolation of affected information assets in the event of a cyber-attack) forming a layered patch-management workflow on the asset.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-02.2` requires establishing verifiable system controls that enforce patch management across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-02.2-002` | Vulnerabilities are addressed and remediated through security updates without delay, provided separately from functionality updates where technically feasible, and disseminated to users via mechanisms ensuring secure ... | `AG-D-02.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms patch management is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.PS-02, PR.IR-03, ID.RA-01, PR.PS-01` |

---

### D-02.3 — Coordinated Vulnerability Disclosure

**High-Level Baseline Goal (SG-D-02.3.HL):** A coordinated vulnerability disclosure (CVD) ecosystem is maintained, covering the manufacturer-side CVD policy (intake, triage, publication, post-disclosure verification), a publicly identifiable contact address for vulnerability reporting, and — when the manufacturer also operates as a NIS 2 essential entity in a Member State — the institutional CSIRT-coordinated pathway under Art. 12(1) that integrates the manufacturer-side CVD with the Member-State-level disclosure coordination.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-02.3` requires establishing verifiable system controls that enforce coordinated vulnerability disclosure across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-02.3-002` | The company puts in place, documents and enforces a coordinated vulnerability disclosure policy, publicly discloses information about fixed vulnerabilities once an update is available, facilitates the sharing of infor... | `AG-D-02.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms coordinated vulnerability disclosure is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `GV.PO-01, GV.SC-04, RS.CO-03` |

---

## §5 Domain D-03 — Access Control & Identity Management
> **Domain Lead:** `CTO` | **Supporting Roles:** `Lead Dev` | **Active Sub-Domains:** 4

### D-03.1 — Identity Lifecycle

**High-Level Baseline Goal (SG-D-03.1.HL):** Identities of principals that interact with the entity's systems, products, services, components and data are managed in a verifiable, lifecycle-aware manner with documented boundaries between identity types and explicit hand-off protocols at boundary surfaces.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-03.1` requires establishing verifiable system controls that enforce identity lifecycle across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-03.1-001` | The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification before action is taken; the company may request add... | `AG-D-03.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms identity lifecycle is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.AA-03, PR.AA-02, PR.DS-10` |
| `SO-D-03.1-002` | Identities, credentials, and access entitlements for users, services, and integrated components of the product are managed in a verifiable manner throughout the operational lifetime of the product, backed by unique pr... | `AG-D-03.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms identity lifecycle is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09` |

---

### D-03.2 — Authentication Strength

**High-Level Baseline Goal (SG-D-03.2.HL):** Authentication of users, services, and hardware that interact with the entity's systems, products, services, components and data operates through an authentication mechanism of sufficient strength for the risk in scope, with the strictest applicable floor discharging the most permissive on the same authentication event when both apply.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-03.2` requires establishing verifiable system controls that enforce authentication strength across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-03.2-001` | Persons authorised to process personal data act only on documented instructions from the company and are bound by confidentiality or an appropriate statutory obligation of confidentiality; the identity of data subject... | `AG-D-03.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms authentication strength is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.AA-05, PR.AA-06, PR.AT-02` |
| `SO-D-03.2-002` | Protection from unauthorised access uses appropriate control mechanisms — which may include authentication, identity, or access-management systems — appropriate to the identified cybersecurity risk of the product. | `AG-D-03.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms authentication strength is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09` |

---

### D-03.3 — Authorisation & Least Privilege

**High-Level Baseline Goal (SG-D-03.3.HL):** The entitlement to perform actions on the entity's systems, products, services, components, and data is managed per least privilege with explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between access surfaces.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-03.3` requires establishing verifiable system controls that enforce authorisation & least privilege across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-03.3-001` | Persons authorised to process personal data act only on documented instructions and are bound by confidentiality, with the documented instructions binding the controller → processor → authorised-persons chain of autho... | `AG-D-03.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms authorisation & least privilege is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.AA-05, PR.AA-06, PR.AT-02` |
| `SO-D-03.3-002` | Access to the product, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported, and attack surfaces including external int... | `AG-D-03.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms authorisation & least privilege is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.AA-05, PR.AA-06, DE.CM-09` |

---

### D-03.4 — Secure System Defaults

**High-Level Baseline Goal (SG-D-03.4.HL):** The default disposition of the entity's data-centric processing systems and the product's product-centric configuration is managed so that the baseline state of every processing system and every product configuration is the minimum-necessary / secure configuration, with relaxation requiring affirmative data-subject or user intervention.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-03.4` requires establishing verifiable system controls that enforce secure system defaults across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-03.4-001` | Processing systems ensure that, by default, only personal data necessary for each specific purpose are processed — across the four AND-coordinated dimensions of amount collected, extent of processing, period of storag... | `AG-D-03.4-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms secure system defaults is enforced for all personal data flows. | `TEST` | CTO + Lead Dev | `PR.PS-01, PR.DS-10, GV.PO-01` |
| `SO-D-03.4-002` | The product is made available on the market with a secure-by-default configuration, including the possibility for the user to reset it to its original state, and that configuration ensures vulnerabilities can be addre... | `AG-D-03.4-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms secure system defaults is enforced across product components and release artifacts. | `TEST` | CTO + Lead Dev | `PR.PS-01, PR.DS-10, GV.SC-03` |

---

## §6 Domain D-04 — Incident Response & Business Continuity
> **Domain Lead:** `CTO` | **Supporting Roles:** `DPO + Compliance Lead` | **Active Sub-Domains:** 4

### D-04.1 — Incident Detection & Triage

**High-Level Baseline Goal (SG-D-04.1.HL):** Security-relevant events affecting the entity's systems, products, services, components and data are detected and triaged with documented trigger moments that anchor the downstream notification and response pipelines.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-04.1` requires establishing verifiable system controls that enforce incident detection & triage across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-04.1-001` | Personal-data breaches are detected and triaged, and the moment of becoming aware is documented so as to anchor the 72-hour notification clock. | `AG-D-04.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms incident detection & triage is enforced for all personal data flows. | `INSPECT` | CTO + DPO + Compliance Lead | `DE.AE-02, PR.PS-04, DE.CM-01` |
| `SO-D-04.1-002` | Relevant internal activity of the product — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption ... | `AG-D-04.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms incident detection & triage is enforced across product components and release artifacts. | `INSPECT` | CTO + DPO + Compliance Lead | `DE.CM-09, PR.PS-04, RS.MA-02` |

---

### D-04.2 — Containment & Mitigation

**High-Level Baseline Goal (SG-D-04.2.HL):** Security incidents affecting the entity's systems, products, services, components and data are contained and mitigated through appropriate measures that address the incident's impact and reduce the probability of further damage.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-04.2` requires establishing verifiable system controls that enforce containment & mitigation across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-04.2-001` | Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including measures rendering the personal data unintelligible to any unauthorised person and subsequent mea... | `AG-D-04.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms containment & mitigation is enforced for all personal data flows. | `INSPECT` | CTO + DPO + Compliance Lead | `PR.DS-10, PR.IR-04, RC.RP-04` |
| `SO-D-04.2-002` | The availability of essential and basic functions is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks; the negative impac... | `AG-D-04.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms containment & mitigation is enforced across product components and release artifacts. | `INSPECT` | CTO + DPO + Compliance Lead | `PR.IR-04, PR.IR-03, DE.CM-09` |

---

### D-04.3 — Regulatory Notification

**High-Level Baseline Goal (SG-D-04.3.HL):** A major security incident is notified to the applicable recipients within the regulatory timelines applicable to the event's material scope.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-04.3` requires establishing verifiable system controls that enforce regulatory notification across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-04.3-001` | A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the company becomes aware of it — unless the breach is unlikely to result... | `AG-D-04.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms regulatory notification is enforced for all personal data flows. | `INSPECT` | CTO + DPO + Compliance Lead | `RS.CO-02, RS.MA-01, RS.MA-03` |
| `SO-D-04.3-002` | An actively-exploited vulnerability contained in the product that the company becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours; vulnerability notification within 72 hours wi... | `AG-D-04.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms regulatory notification is enforced across product components and release artifacts. | `INSPECT` | CTO + DPO + Compliance Lead | `RS.MA-02, RS.CO-02` |

---

### D-04.4 — Restoration & Recovery

**High-Level Baseline Goal (SG-D-04.4.HL):** Systems, products, services, components and data are restored and recovered with documented recovery evidence applicable to the recovery dimensions of all four participating regulators on the same party.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-04.4` requires establishing verifiable system controls that enforce restoration & recovery across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-04.4-001` | The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and the availability of and access to personal data is restored in a timely m... | `AG-D-04.4-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms restoration & recovery is enforced for all personal data flows. | `INSPECT` | CTO + DPO + Compliance Lead | `PR.IR-04, PR.DS-01, RC.RP-04` |
| `SO-D-04.4-002` | The availability of essential and basic functions is protected also after an incident through resilience and recovery measures, with exploitation-mitigation mechanisms and techniques reducing incident impact and corre... | `AG-D-04.4-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms restoration & recovery is enforced across product components and release artifacts. | `INSPECT` | CTO + DPO + Compliance Lead | `PR.IR-03, PR.DS-10` |

---

## §7 Domain D-05 — Data Subject Rights & Privacy Lifecycle
> **Domain Lead:** `DPO` | **Supporting Roles:** `Lead Dev` | **Active Sub-Domains:** 4

### D-05.1 — Data Minimisation

**High-Level Baseline Goal (SG-D-05.1.HL):** Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the purpose for which it is processed, with a documented necessity assessment and, where the underlying purpose changes, a compatibility assessment confirming that the new use is consistent with the original. Special-category data is processed only where a narrow exception applies and is documented to that effect.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-05.1` requires establishing verifiable system controls that enforce data minimisation across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-05.1-001` | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed; further processing is compatible with the original purposes per ... | `AG-D-05.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms data minimisation is enforced for all personal data flows. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, ID.AM-03, GV.OC-03, GV.PO-01` |
| `SO-D-05.1-002` | Data processed by the product — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with the risk assessment and the intended purpose plus re... | `AG-D-05.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms data minimisation is enforced across product components and release artifacts. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, ID.AM-03` |

---

### D-05.2 — Retention & Archiving

**High-Level Baseline Goal (SG-D-05.2.HL):** Data — across the data classes in scope — is retained for the period required to satisfy its declared purpose, with documented retention rationale and, where the underlying purpose changes, a reset of the retention clock. Long-term archiving or research-only retention is paired with safeguards proportional to the residual identifiability.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-05.2` requires establishing verifiable system controls that enforce retention & archiving across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-05.2-001` | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes processed; longer retention is permitted only where lawful and subject to Art. 89(1) safe... | `AG-D-05.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms retention & archiving is enforced for all personal data flows. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, ID.AM-03` |
| `SO-D-05.2-002` | Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail, and the support-period end-date is provi... | `AG-D-05.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms retention & archiving is enforced across product components and release artifacts. | `INSPECT` | DPO + Lead Dev | `PR.PS-02, GV.OV-02, GV.OC-04` |

---

### D-05.3 — Right to Erasure

**High-Level Baseline Goal (SG-D-05.3.HL):** Data held about a person is rendered inaccessible to the controller on the data subject's election, and data held by a product with digital elements is rendered inaccessible to the manufacturer on the user's election, by whichever mechanism — the controller-side policy execution or the manufacturer-side product affordance — applies to the data object. Erasure is performed without undue delay and is documented to demonstrate compliance; where a processor is involved, the processor-side mirror ensures deletion-or-return at contract end.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-05.3` requires establishing verifiable system controls that enforce right to erasure across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-05.3-001` | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds (a)–(f) applies; on processor contract end, the processor deletes or returns all personal data and exi... | `AG-D-05.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms right to erasure is enforced for all personal data flows. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, PR.DS-10, GV.SC-04` |
| `SO-D-05.3-002` | The user of the product can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure man... | `AG-D-05.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms right to erasure is enforced across product components and release artifacts. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, PR.DS-10, PR.DS-02` |

---

### D-05.4 — Data Portability

**High-Level Baseline Goal (SG-D-05.4.HL):** Personal data are exported to the data subject in a structured, commonly used, machine-readable format, and the data subject can transmit those data to another controller without hindrance, subject to the qualifying conditions and exclusions that scope the right.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-05.4` requires establishing verifiable system controls that enforce data portability across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-05.4-001` | The data subject receives personal data in a structured, commonly used, machine-readable format, supplied without undue delay and free of charge, and can transmit those data to another controller without hindrance; wh... | `AG-D-05.4-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms data portability is enforced for all personal data flows. | `INSPECT` | DPO + Lead Dev | `PR.DS-10, PR.DS-10` |

---

## §8 Domain D-06 — Supply Chain & Third-Party Security
> **Domain Lead:** `CTO` | **Supporting Roles:** `Lead Dev + Procurement` | **Active Sub-Domains:** 3

### D-06.1 — Vendor Risk Assessment

**High-Level Baseline Goal (SG-D-06.1.HL):** Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-06.1` requires establishing verifiable system controls that enforce vendor risk assessment across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-06.1-001` | The company engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures such that processing meets the Regulation's requirements and protects data-subject rig... | `AG-D-06.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms vendor risk assessment is enforced for all personal data flows. | `INSPECT` | CTO + Lead Dev + Procurement | `GV.SC-02, GV.SC-04, ID.AM-04` |
| `SO-D-06.1-002` | The company exercises due diligence when integrating components sourced from third parties — including free and open-source software components not made available on the market in the course of a commercial activity —... | `AG-D-06.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms vendor risk assessment is enforced across product components and release artifacts. | `INSPECT` | CTO + Lead Dev + Procurement | `GV.SC-01, GV.SC-02, ID.RA-02` |

---

### D-06.2 — Software Bill of Materials

**High-Level Baseline Goal (SG-D-06.2.HL):** The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-06.2` requires establishing verifiable system controls that enforce software bill of materials across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-06.2-002` | The company draws up and maintains a software bill of materials covering the components and dependencies contained in the product, in a commonly used and machine-readable format that includes at minimum the top-level ... | `AG-D-06.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms software bill of materials is enforced across product components and release artifacts. | `INSPECT` | CTO + Lead Dev + Procurement | `ID.AM-02, GV.SC-02, GV.SC-03` |

---

### D-06.3 — Contractual Security Obligations

**High-Level Baseline Goal (SG-D-06.3.HL):** Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, as appropriate to the regulatory perspective and the actor involved.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-06.3` requires establishing verifiable system controls that enforce contractual security obligations across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-06.3-001` | Controller/processor contracts and related transfer instruments include the eight-element Art. 28(3)(a)–(h) floor, sub-processor authorisation and change-notification, processor security-measure commitments, audit and... | `AG-D-06.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms contractual security obligations is enforced for all personal data flows. | `INSPECT` | CTO + Lead Dev + Procurement | `—` |
| `SO-D-06.3-002` | Contractual security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place the product on the Union market only after verifying conformity assessment, technic... | `AG-D-06.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms contractual security obligations is enforced across product components and release artifacts. | `INSPECT` | CTO + Lead Dev + Procurement | `—` |

---

## §9 Domain D-07 — Secure Development & Testing
> **Domain Lead:** `Lead Dev` | **Supporting Roles:** `CTO` | **Active Sub-Domains:** 4

### D-07.1 — Secure-by-Design Principles

**High-Level Baseline Goal (SG-D-07.1.HL):** Security is integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-07.1` requires establishing verifiable system controls that enforce secure-by-design principles across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-07.1-001` | The company implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement data-protection principles in an effective manner and to integrate the necessary safeguards i... | `AG-D-07.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms secure-by-design principles is enforced for all personal data flows. | `INSPECT` | Lead Dev + CTO | `PR.PS-06, PR.DS-10` |
| `SO-D-07.1-002` | When placing the product on the market, the company ensures it has been designed, developed and produced in accordance with the essential cybersecurity requirements of Annex I Part I, with the cybersecurity risk asses... | `AG-D-07.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms secure-by-design principles is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.PS-06, PR.PS-01` |

---

### D-07.2 — Secure Coding Practices

**High-Level Baseline Goal (SG-D-07.2.HL):** Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system attack-defence under an appropriate coding-practice evidence base.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-07.2` requires establishing verifiable system controls that enforce secure coding practices across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-07.2-002` | The company designs, develops, and produces the product so as to limit its attack surfaces, including the attack surfaces of external interfaces, and to reduce the impact of an incident using appropriate exploitation-... | `AG-D-07.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms secure coding practices is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.PS-06, PR.PS-02` |

---

### D-07.3 — Build & Update Distribution Security

**High-Level Baseline Goal (SG-D-07.3.HL):** CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-agent integrity, ephemeral build environments) and update-distribution delivery-path security.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-07.3` requires establishing verifiable system controls that enforce build & update distribution security across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-07.3-002` | The company securely distributes updates for the product in a timely manner, including through automatic updates where appropriate, and ensures that updates are disseminated free of charge, are clearly described, and ... | `AG-D-07.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms build & update distribution security is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.PS-06, PR.PS-02` |

---

### D-07.4 — Change Management

**High-Level Baseline Goal (SG-D-07.4.HL):** Change management delivers documented change-management procedures (manufacturer-side series-production conformity + entity-side change-management six-step), risk-assessment-approach, controlled-manner, and substantial-modification assessment with manufacturer-equivalent status consequences where applicable.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-07.4` requires establishing verifiable system controls that enforce change management across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-07.4-002` | The company ensures that procedures are in place for products that are part of a series of production to remain in conformity with the Regulation. | `AG-D-07.4-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms change management is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04` |

---

## §10 Domain D-08 — Human Factors & Personnel Security
> **Domain Lead:** `HR` | **Supporting Roles:** `CTO + DPO` | **Active Sub-Domains:** 2

### D-08.1 — General Security Awareness

**High-Level Baseline Goal (SG-D-08.1.HL):** General security awareness is established through a documented training programme with population-wide coverage, audience-routing, and governance hooks.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-08.1` requires establishing verifiable system controls that enforce general security awareness across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-08.1-001` | The data protection officer informs and advises the company and the employees who carry out processing of their obligations under the Regulation, and monitors compliance including the assignment of responsibilities an... | `AG-D-08.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms general security awareness is enforced for all personal data flows. | `INSPECT` | HR + CTO + DPO | `PR.AT-01, PR.AT-02` |
| `SO-D-08.1-002` | The product is accompanied by detailed instructions — or an internet address referring to such instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ... | `AG-D-08.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms general security awareness is enforced across product components and release artifacts. | `INSPECT` | HR + CTO + DPO | `PR.AT-01` |

---

### D-08.2 — Role-Specific Competence

**High-Level Baseline Goal (SG-D-08.2.HL):** Role-specific competence is established through a function-specific depth, audience-routing, competence-criteria-anchored training, and governance hooks architecture.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-08.2` requires establishing verifiable system controls that enforce role-specific competence across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-08.2-001` | The data protection officer monitors compliance including the assignment of responsibilities and the awareness-raising and training of staff involved in processing operations — the role-specific layer of the DPO-catal... | `AG-D-08.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms role-specific competence is enforced for all personal data flows. | `INSPECT` | HR + CTO + DPO | `PR.AT-01, PR.AT-02` |
| `SO-D-08.2-002` | Where the product is intended for integration into other products, the company provides the information necessary for the integrator to comply with the essential cybersecurity requirements of Annex I Part I and the do... | `AG-D-08.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms role-specific competence is enforced across product components and release artifacts. | `INSPECT` | HR + CTO + DPO | `PR.AT-02, GV.SC-03` |

---

## §11 Domain D-09 — Governance, Risk & Compliance
> **Domain Lead:** `Compliance Lead` | **Supporting Roles:** `CTO + DPO` | **Active Sub-Domains:** 4

### D-09.1 — Information Security Policies

**High-Level Baseline Goal (SG-D-09.1.HL):** Information security policies are established through a **documented policy architecture** with **governance hooks** and an **accountability chain** that anchor the entity's cybersecurity posture.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-09.1` requires establishing verifiable system controls that enforce information security policies across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-09.1-001` | The company implements appropriate technical and organisational measures, such as policies, which are designed to implement data-protection principles in an effective manner, carrying the Art. 5(2) accountability burd... | `AG-D-09.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms information security policies is enforced for all personal data flows. | `INSPECT` | Compliance Lead + CTO + DPO | `GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02` |
| `SO-D-09.1-002` | The company establishes the policies, processes and procedures necessary to implement its product-security obligations, including the coordinated vulnerability disclosure policy, secure-update distribution, support-pe... | `AG-D-09.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms information security policies is enforced across product components and release artifacts. | `INSPECT` | Compliance Lead + CTO + DPO | `GV.PO-01, GV.PO-02` |

---

### D-09.2 — Impact & Risk Assessments

**High-Level Baseline Goal (SG-D-09.2.HL):** Impact and risk assessments are established through a **documented assessment** of identified risks and mitigation measures, with a **review cadence** calibrated to the lifecycle phase of the assessment object.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-09.2` requires establishing verifiable system controls that enforce impact & risk assessments across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-09.2-001` | Prior to processing likely to result in a high risk to the rights and freedoms of natural persons, the company carries out a data-protection impact assessment covering the four Art. 35(7) content items, reviewed when ... | `AG-D-09.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms impact & risk assessments is enforced for all personal data flows. | `INSPECT` | Compliance Lead + CTO + DPO | `ID.RA-05, ID.RA-04` |
| `SO-D-09.2-002` | The company documents the cybersecurity risk assessment and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use and indicating the applicab... | `AG-D-09.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms impact & risk assessments is enforced across product components and release artifacts. | `INSPECT` | Compliance Lead + CTO + DPO | `ID.RA-05, GV.SC-07` |

---

### D-09.3 — Asset Inventories

**High-Level Baseline Goal (SG-D-09.3.HL):** Asset inventories are established through a **documented entity-level asset inventory** with **identification + classification + documentation** of ICT supported business functions, information assets, ICT assets, and their roles and dependencies.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-09.3` requires establishing verifiable system controls that enforce asset inventories across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-09.3-002` | The company draws up technical documentation containing at least a general description of the product and a description of the design, development, production and vulnerability-handling processes including the system ... | `AG-D-09.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms asset inventories is enforced across product components and release artifacts. | `INSPECT` | Compliance Lead + CTO + DPO | `ID.AM-01, ID.AM-02` |

---

### D-09.4 — Records of Processing

**High-Level Baseline Goal (SG-D-09.4.HL):** Records of processing activities are established through **parallel documentation regimes** that produce records of processing activities, technical documentation, certification records, information security policy documentation, and quality management system documentation serving distinct audit purposes.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-09.4` requires establishing verifiable system controls that enforce records of processing across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `PO-D-09.4-001` | The company maintains a record of processing activities under its responsibility, in writing or electronic form, containing the Art. 30(1) seven-item content list, with a parallel processor-side record, made available... | `AG-D-09.4-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms records of processing is enforced for all personal data flows. | `INSPECT` | Compliance Lead + CTO + DPO | `ID.AM-08, PR.DS-10, GV.PO-02` |
| `SO-D-09.4-002` | The company draws up the technical documentation before placing the product on the market, carries out the conformity assessment procedure, draws up the EU declaration of conformity and affixes the conformity marking,... | `AG-D-09.4-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms records of processing is enforced across product components and release artifacts. | `INSPECT` | Compliance Lead + CTO + DPO | `ID.AM-08, PR.DS-10, ID.RA-05` |

---

## §12 Domain D-10 — Logging, Auditing & Monitoring
> **Domain Lead:** `Lead Dev` | **Supporting Roles:** `CTO` | **Active Sub-Domains:** 3

### D-10.1 — Continuous Security Monitoring

**High-Level Baseline Goal (SG-D-10.1.HL):** Continuous security monitoring is established through a **layered detection-and-monitoring architecture** spanning personal-data processing systems, network and information systems, on-device product activity, ICT systems and tools, and high-risk AI systems, with detection capability feeding the incident-response chain.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-10.1` requires establishing verifiable system controls that enforce continuous security monitoring across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-10.1-001` | The company implements appropriate technical and organisational measures to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services and regularly tests, assesses a... | `AG-D-10.1-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms continuous security monitoring is enforced for all personal data flows. | `TEST` | Lead Dev + CTO | `DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04` |
| `SO-D-10.1-002` | The product provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, with an opt-out mechanism for the user, and... | `AG-D-10.1-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms continuous security monitoring is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `DE.CM-01, DE.CM-09, ID.IM-04` |

---

### D-10.2 — Audit Logging & Traceability

**High-Level Baseline Goal (SG-D-10.2.HL):** Audit logging and traceability are established through a **layered audit-records architecture** spanning compliance records with integrity and traceability, product-level technical documentation traceability, entity-level information security policy documentation, and AI-system event logging with retention floors.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-10.2` requires establishing verifiable system controls that enforce audit logging & traceability across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-10.2-001` | The company maintains compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections — records of processing, con... | `AG-D-10.2-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms audit logging & traceability is enforced for all personal data flows. | `TEST` | Lead Dev + CTO | `PR.DS-01, PR.PS-04, DE.CM-01, GV.PO-02` |
| `SO-D-10.2-002` | The company maintains the technical documentation, preserves the cybersecurity risk-assessment documentation during the support period with updates as appropriate, and ensures that test reports demonstrating verificat... | `AG-D-10.2-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms audit logging & traceability is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.DS-01, PR.PS-02, GV.PO-02, ID.RA-04` |

---

### D-10.3 — Compliance Testing

**High-Level Baseline Goal (SG-D-10.3.HL):** Compliance testing is established through a **5-parallel-testing-programme architecture** spanning effectiveness-evaluation of security measures, effectiveness-assessment of risk-management measures, product-level conformity-assessment, entity-level digital operational resilience testing with TLPT, and AI-system-level testing for risk management with real-world-conditions and accuracy/robustness/cybersecurity baseline testing.

**Operational Translation (TinyTask Context):** For TinyTask SaaS (8-person cloud-hosted B2B platform), operationalizing `D-10.3` requires establishing verifiable system controls that enforce compliance testing across application interfaces and persistent data stores, leveraging managed cloud provider primitives while maintaining clear separation between personal data safeguards and product cyber-resilience.

| Objective ID | Operational Statement | Parent Goal | Regulation | Operational Scope (Ambit) | Verification Criteria | Method | Responsible Owner | Control Anchors |
|---|---|---|---|---|---|---|---|---|
| `SO-D-10.3-001` | The company implements a process for regularly testing, assessing and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment at least when ... | `AG-D-10.3-001` | **GDPR** | Personal Data Scope (Patient & Staff Data) | Automated check or audit confirms compliance testing is enforced for all personal data flows. | `TEST` | Lead Dev + CTO | `PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03` |
| `SO-D-10.3-002` | The company carries out effective and regular tests and reviews of the product, and the technical documentation contains the reports of the tests carried out to verify the conformity of the product and of the vulnerab... | `AG-D-10.3-002` | **CRA** | Product & Software Security Scope (SaaS System & Assets) | Security verification confirms compliance testing is enforced across product components and release artifacts. | `TEST` | Lead Dev + CTO | `PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03` |

---

## §13 Governance & Stakeholder Matrix

Operational ownership across all operational objectives is distributed across TinyTask's 8-person team to maintain clear accountability without operational drag:

| Operational Domain | Primary Lead | Supporting Roles | Core Sub-Domains Supervised |
|---|---|---|---|
| **Platform & Cryptography** | `CTO` | `Lead Dev` | D-01.1, D-01.2, D-01.3, D-01.4, D-03.4 |
| **Software Security & Release** | `Lead Dev` | `CTO`, Core Dev Team | D-02.1, D-02.2, D-02.3, D-06.2, D-07.1, D-07.2, D-07.3, D-07.4 |
| **Access & Identity Governance** | `CTO` | `Lead Dev` | D-03.1, D-03.2, D-03.3 |
| **Incident Management & Resilience** | `CTO` | `DPO`, `Compliance Lead` | D-04.1, D-04.2, D-04.3, D-04.4 |
| **Data Subject Rights & Lifecycle** | `DPO` | `CTO`, Core Dev Team | D-05.1, D-05.2, D-05.3, D-05.4 |
| **Supply Chain & Processor Due Diligence** | `CTO` | `Compliance Lead`, Core Dev Team | D-06.1, D-06.3 |
| **Personnel Security & Training** | `HR` | `CTO`, `DPO` | D-08.1, D-08.2 |
| **Governance, Risk & Transparency** | `Compliance Lead` | `CTO`, `DPO` | D-09.1, D-09.2, D-09.4 |
| **Security Observability & Testing** | `Lead Dev` | `CTO` | D-10.1, D-10.2, D-10.3 |

---

## §14 Version History

| Version | Date | Author / Role | Changes |
|---|---|---|---|
| `1.1` | 2026-09-22 | Antigravity AI / PhD Pair Session | Structured catalog domain by domain across all 35 sub-domains, adding high-level goal translations and separating GDPR and CRA ambits into distinct operational objectives in clean tabular format. |
