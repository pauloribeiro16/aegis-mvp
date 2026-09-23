---
document_id: AEGIS-P2-RICH-07c
title: Adjusted Goals per Sub-Domain (SecureBorder Solutions)
phase: 1
version: 1.0
created: 2026-09-23
updated: 2026-09-23
author: aegis-mvp executor
status: COMPLETE
id_format: AG-D-XX.Y-NNN (canonical Phase 1)
ag_canonical_ids_count: 100
status_history:
  - { date: 2026-09-23, status: COMPLETE, sprint: 1, by: 'aegis-mvp executor — Case_02 Phase 1 adjusted goals' }
active_subdomains_mapped: 35
active_subdomains: 35
not_addressed_subdomains: [D-07.4, D-08.3, D-09.3]
ag_count: 100
ag_rows_per_regulation:
  GDPR: 29
  CRA: 34
  NIS2: 22
  AI_Act: 15
tensions_expanded_count: 4
track_b_rows: 38
track_b_distribution:
  RIGOROUS: 8
  STANDARD: 27
  NOT_ADDRESSED: 3
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS2, AI_Act]
inputs: [Doc01_INTAKE_FORM.md, baseline/domains/, baseline/CONTROLS/, baseline/MAPPINGS/]
outputs: [02_PHASE2_RULES/Doc01_Operational_Objectives.md]
related_documents: [Doc01_INTAKE_FORM.md, baseline/00_Taxonomy_Reference.md, baseline/01_Ambiguity_Registry.md]
cross_checked_against: [Doc01_INTAKE_FORM.md, baseline/00_Taxonomy_Reference.md]
frozen: false
---

# Adjusted Goals per Sub-Domain (SecureBorder Solutions)

---

## §0 Document Purpose

This document is the **Phase 1 Adjusted Goals layer** of the SecureBorder Solutions case — the Fase 0 → Fase 1 exchange of the pipeline I/O contract (ADR-004): the frozen corpus **Baseline Goals** (high-level goal `SG-D-XX.Y.HL` + per-regulation baseline goals) restated against one company. It binds every ACTIVE sub-domain to:

1. A **regulatory floor** — the corpus Baseline Goals, consumed by reference.
2. A **framing** — the company context that conditions every goal: size/tier, area of operation, regulatory roles, inherited capabilities (§2).
3. **Adjusted Goals** — one D1 card per goal (ADR-003): company-proportional, regulation-anchored, slot 001 GDPR / slot 002 CRA / slot 003 NIS 2 / slot 004 AI Act (§3).
4. **Resolutions** for the 4 strategic tensions (T-001..T-004), in §4.
5. A **Track B tier** per sub-domain, in §5.
6. The **NIST controls mapping** per sub-domain, in §6.

## §1 Regulatory Floor (corpus, by reference)

The baseline floor for goals is consumed by reference from `baseline/domains/` and `baseline/MAPPINGS/traceability/` per rule R9.

## §2 Framing (SecureBorder Solutions)

| Dimension | Framing |
|---|---|
| Size | 450-person workforce, ~€120M revenue, MEDIUM scale — tiers RIGOROUS/STANDARD (no INHERITABLE rows; DEFERRED unavailable at security staffing > 1 FTE). Consequences: a certified ISMS is the governance vehicle for every policy-bearing goal (D-09.1); a 24/7 in-house SOC is the operating vehicle for detection and response (D-04.1, D-10.1); dedicated CISO, DPO and AI Governance Lead roles carry the accountability chain (D-09.x). |
| Area of operation | Supplier of automated border-control gates (eGate) with on-board biometric verification AI, deployed at Schengen border crossings and airports across multiple Member States; EU-region cloud back-office; processes personal data of travellers and employees on a continuous, large-scale basis. |
| Regulatory roles | Data controller (employee data, audit logs) and data processor (traveller biometric data, on behalf of government authorities); manufacturer of a product with digital elements in the CRA **Critical Class**; essential-entity supplier under NIS 2; **provider and deployer** of a high-risk AI system (Annex III border control). |
| Inherited capabilities | Certified information-security and privacy management system (ISMS) with annual external audit; 24/7 SOC; hardware-security-module key custody; per-airport physically isolated deployments; signed-release pipeline for firmware and model updates. |

## §3 Adjusted Goals

### §3.0 Structure and Interpretation Guide

Each active sub-domain presents:
1. **High-Level Security Goal (`SG-D-XX.Y.HL`):** The common, regulation-neutral baseline objective inherited from the methodology corpus (`baseline/domains/`).
2. **Regulation-Specific Adjusted Goals:** Company-proportional restatements for each confirmed applicable regulation (slot 001 for GDPR, slot 002 for CRA, slot 003 for NIS 2, slot 004 for AI Act).
3. **Adjustment Column (`Adjustment`):**
   - **`—` (Standard Proportionality):** Indicates that the goal follows the overarching company proportionality defined in **§2 Framing** (MEDIUM scale, certified ISMS, 24/7 SOC, Critical-Class manufacturer, essential-entity supplier, high-risk-AI provider) without requiring sub-domain-specific legal exceptions or procedural deviations.
   - **Explicit Notes:** Document specific regulatory boundary conditions, statutory exceptions, or interpretation baselines that apply uniquely to that sub-domain (e.g. active special-category biometric provisions, Critical-Class notified-body assessment, essential-entity scope, four-regulation notification surface), including the **RIGOROUS** tier overrides of §5.

---

### D-01.1 — Data at Rest Encryption

**High-Level Security Goal (SG-D-01.1.HL):** Data held at rest in storage is protected against unauthorised access through appropriate technical measures — primarily encryption with appropriate key custody — calibrated to the risks identified in the entity's risk assessment and commensurate with the state of the art.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.1-001` | Personal data at rest is processed in a manner that ensures appropriate security — including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage — using appropriate technical or organisational measures, with the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (Art. 5(1)(f) + Art. 32(1)(b); the `appropriate` threshold is anchored by the five Art. 32(1) preamble factors — state of the art, costs of implementation, nature, scope, context, purposes, risks). | maintain | Confidentiality & Integrity | SG-D-01.1.HL | GDPR | Art. 5(1)(f) + Art. 32(1)(b) | PR.DS-01, PR.DS-10 | At MEDIUM scale with a certified ISMS, the encryption capability is operated on the company's EU-hosted platform with hardware-security-module key custody; biometric capture keeps raw images off the persistent store (RIGOROUS tier). |
| `AG-D-01.1-002` | Where a product with digital elements stores data — personal or other — the confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms (Annex I Part I (2)(e)). | maintain | Confidentiality & Integrity | SG-D-01.1.HL | CRA | Annex I Part I (2)(e) | PR.DS-01 | Critical Class product: state-of-the-art evidence forms part of the technical documentation submitted to the notified body (RIGOROUS tier). |
| `AG-D-01.1-003` | Essential and important entities establish policies and procedures regarding the use of cryptography and, where appropriate, encryption, covering the confidentiality, integrity, and authenticity of data stored, transmitted, and processed by network and information systems (Art. 21(2)(h)). | maintain | Confidentiality & Integrity | SG-D-01.1.HL | NIS 2 | Art. 21(2)(h) | PR.DS-01, PR.DS-02, GV.RM-04 | Essential-entity scope: the cryptography policy covers every network and information system supporting the eGate service across all per-airport deployments, not only personal-data stores; the `where appropriate` hedge is resolved by the entity risk assessment (RIGOROUS tier). |

### D-01.2 — Data in Transit Encryption

**High-Level Security Goal (SG-D-01.2.HL):** Data in transit — across network paths, inter-service calls, and third-party APIs — is protected against unauthorised disclosure and alteration through cryptographic confidentiality and integrity controls (mutual authentication, encryption, integrity verification).

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.2-001` | Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted) (Art. 32(1)(b) + Art. 32(2)). | maintain | Confidentiality & Integrity | SG-D-01.2.HL | GDPR | Art. 32(1)(b) + Art. 32(2) | PR.DS-02, PR.IR-01 | — |
| `AG-D-01.2-002` | Where data is transmitted by a product with digital elements — personal or other — the confidentiality of the data in transit is protected by encrypting relevant data using state-of-the-art mechanisms, with the Annex I (2)(j) attack-surface-limitation leg constraining the exposed interfaces through which the data could otherwise leak (Annex I Part I (2)(e) + (2)(j)). | maintain | Confidentiality & Integrity | SG-D-01.2.HL | CRA | Annex I Part I (2)(e) | PR.DS-02, PR.IR-01 | — |

### D-01.3 — Cryptographic Key Management

**High-Level Security Goal (SG-D-01.3.HL):** Cryptographic keys and related authentication material are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it; the key custodian and the data consumer are distinct roles under distinct technical and organisational control, with the cryptographic key (not the storage medium) as the necessary condition for intelligibility of the protected data.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.3-001` | Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject (the cryptographic key, the mapping table, or the tokenisation seed) is kept separately and is subject to appropriate technical and organisational measures that prevent attribution (Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility carve-out + Art. 32(1)(a) pseudonymisation/ encryption anchor). | maintain | Confidentiality | SG-D-01.3.HL | GDPR | Art. 32(1)(a) + Art. 4(5) + Art. 34(3)(a) | PR.DS-01, PR.IR-03 | — |
| `AG-D-01.3-002` | Cryptographic keys and related authentication material used to protect the confidentiality and integrity of stored, transmitted or otherwise processed data by a product with digital elements — personal or other — are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it (Annex I Part I (2)(d) access-control + (2)(e) "other technical means" reading per `SR-CRA-004` ambiguity_notes; the Annex I text does not mention key management explicitly — the synthesis catalogue `99_CRA_Synthesis.md` §4 flags this as a T2-vs-text gap — so the key-separation reading rests on the combination of Annex I (2)(d) access-control duty with the Annex I (2)(e) "other technical means" residual). | maintain | Confidentiality | SG-D-01.3.HL | CRA | Annex I Part I (2)(d) | PR.DS-01, PR.AA-05, GV.OV-01 | The Annex I text does not mention key management explicitly; the key-separation reading combines the access-control duty with the `other technical means` residual — a text-versus-interpretation gap flagged in the corpus synthesis catalogue. Biometric-template keys are custodied in hardware security modules under documented key ceremonies (RIGOROUS tier). |

### D-01.4 — Data Integrity Mechanisms

**High-Level Security Goal (SG-D-01.4.HL):** Data integrity is preserved against unauthorised modification across the data lifecycle — at rest, in transit, and in use — with corruption detected, logged, and reported, and with semantic accuracy maintained as the workflow leg of the personal-data principle.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.4-001` | Personal data are accurate and, where necessary, kept up to date; every reasonable step is taken to ensure that personal data that are inaccurate are erased or rectified without delay (Art. 5(1)(d) accuracy principle), with the integrity property anchored to two further legs — storage integrity (Art. 5(1)(f)) and the Art. 16 rectification cascade with Art. 19 recipient-cascade duty. | maintain | Integrity | SG-D-01.4.HL | GDPR | Art. 5(1)(d) + Art. 5(1)(f) + Art. 16 + Art. 19 | PR.DS-01, ID.AM-08, PR.DS-10 | — |
| `AG-D-01.4-002` | The integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, is protected against any manipulation or modification not authorised by the user (Annex I Part I (2)(f) — the universal-quantifier `any` makes the integrity protection unconditional); corruption is reported to the user / administering party (Annex I Part I (2)(f) `report on corruptions` + (2)(l) logging + monitoring). | maintain | Integrity | SG-D-01.4.HL | CRA | Annex I Part I (2)(f) | PR.DS-01, PR.DS-10, PR.PS-04 | The universal quantifier `any` makes this integrity protection unconditional — it admits no risk-based relaxation at any scale. |
| `AG-D-01.4-004` | High-risk AI systems are as resilient as possible regarding errors, faults, or inconsistencies that may occur within the system or the environment (Art. 15(3)); the robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. | maintain | Integrity | SG-D-01.4.HL | AI Act | Art. 15(3) | PR.IR-03, PR.IR-04, PR.DS-11 | Decision-record and model-artefact integrity underpins the Art. 12 logging and Art. 15 robustness duties; the redundancy legs (backup or fail-safe plans) align with the existing business-continuity capability. |

### D-02.1 — Vulnerability Identification

**High-Level Security Goal (SG-D-02.1.HL):** Vulnerabilities — including, where in scope, AI-system-specific attack surfaces (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) — are identified on a continuing basis across the system, product, ICT asset, or AI system that an entity operates, manufactures, deploys, or processes, with the resulting identification artefact (vulnerability register, risk-scenario catalogue, SBOM, or risk-management file) feeding the entity's testing, remediation, and notification cascades.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.1-001` | A controller or processor operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures for ensuring the security of the processing (Art. 32(1)(d)); the data-protection impact assessment under Art. 35 is reviewed when there is a change of the risk represented by processing operations (Art. 35(11)). | achieve | Confidentiality | SG-D-02.1.HL | GDPR | Art. 32(1)(d) + Art. 35(11) | ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02 | — |
| `AG-D-02.1-002` | A product with digital elements is made available on the market without known exploitable vulnerabilities (Annex I Part I (2)(a)), and vulnerabilities contained in the product — including the components listed in an SBOM — are identified and documented on a continuing basis throughout the support period (Annex I Part II (1) + Art. 13(3) + Art. 13(7)). | achieve | Confidentiality | SG-D-02.1.HL | CRA | Annex I Part I (2)(a) + Annex I Part II (1) + Art. 13(7) | ID.RA-01, ID.AM-02, PR.PS-02 | The support-period floor binds the manufacturer for the full deployed eGate fleet, including already-installed per-airport instances. |
| `AG-D-02.1-003` | Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle (Art. 21(2)(e)). | achieve | Confidentiality | SG-D-02.1.HL | NIS 2 | Art. 21(2)(e) | ID.RA-01, GV.SC-04 | Coordinated handling covers the entity's own attack surface with the disclosed route to the national CSIRT; the 24/7 SOC is the operating vehicle. |
| `AG-D-02.1-004` | A risk-management system is established, implemented, documented, and maintained for high-risk AI systems throughout their lifecycle, comprising a continuous iterative process of (a) identification and analysis of known and reasonably foreseeable risks, (b) estimation and evaluation of risks emerging from use under conditions of reasonably foreseeable misuse, (c) evaluation of other risks arising from analysis of post-market monitoring data, and (d) adoption of appropriate and targeted risk-management measures (Art. 9(2)); the high-risk AI system is designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and is resilient against errors, faults, or inconsistencies that may occur within the system or the environment, with appropriate technical and organisational measures to prevent, detect, respond to, resolve, and control for attacks trying to manipulate the training data set (data poisoning), pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks, or model flaws (Art. 15(1)/(4)–(5)). | achieve | Confidentiality | SG-D-02.1.HL | AI Act | Art. 9(1) + Art. 9(2)(a)–(d) + Art. 15(4)–(5) | — | The Art. 9(2) iterative loop is instantiated as the risk-management file for the border-control AI system and feeds the notified-body conformity assessment. |

### D-02.2 — Patch Management & Updates

**High-Level Security Goal (SG-D-02.2.HL):** Vulnerabilities identified in the upstream identification pipeline are addressed and remediated through security updates that are distributed via a secure, separated channel, with the entity-side policy governing patch deployment (severity-classified deployment windows, automated isolation of affected information assets in the event of a cyber-attack) forming a layered patch-management workflow on the asset.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.2-002` | Vulnerabilities of a product with digital elements are addressed and remediated through security updates without delay, including — where technically feasible — through security updates provided separately from functionality updates (Annex I Part II (2) + Annex I Part I (2)(c)); security updates are disseminated without delay to users via mechanisms that ensure the secure distribution of updates, accompanied by advisory messages describing the action users can take (Annex I Part II (7) + (8)); vulnerabilities — including those of integrated components — are handled effectively and in accordance with the Annex I Part II vulnerability-handling requirements throughout the support period determined by the manufacturer (minimum 5 years, or the expected use time if shorter — Art. 13(8)); each security update made available during the support period remains available after it has been issued for at least 10 years or for the remainder of the support period, whichever is longer (Art. 13(9)). | achieve | Confidentiality | SG-D-02.2.HL | CRA | Annex I Part II (2) + Annex I Part I (2)(c) + Annex I Part II (7) + Art. 13(9) | — | The 10-year (or remainder-of-support-period) update-availability floor is absolute; signed-update distribution is verified at the notified-body assessment. |

### D-02.3 — Coordinated Vulnerability Disclosure

**High-Level Security Goal (SG-D-02.3.HL):** A coordinated vulnerability disclosure (CVD) ecosystem is maintained, covering the manufacturer-side CVD policy (intake, triage, publication, post-disclosure verification), a publicly identifiable contact address for vulnerability reporting, and — when the manufacturer also operates as a NIS 2 essential entity in a Member State — the institutional CSIRT-coordinated pathway under Art. 12(1) that integrates the manufacturer-side CVD with the Member-State-level disclosure coordination.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.3-002` | The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for its products with digital elements (Annex I Part II (5) + Art. 13(8) sentence 6); once a security update has been made available, the manufacturer shares and publicly discloses information about the fixed vulnerabilities, including a description of the vulnerability, the affected products, the impacts, the severity, and the remediation guidance — subject to a duly justified delay exception where security risks of publication outweigh security benefits (Annex I Part II (4)); the manufacturer facilitates the sharing of information about potential vulnerabilities in its products and in third-party components contained therein, including by providing a publicly identifiable contact address for the reporting of vulnerabilities (Annex I Part II (6)); the manufacturer designates a single point of contact to enable users — including security researchers — to communicate directly and rapidly with the manufacturer (Art. 13(17) + Annex II §2). | achieve | Confidentiality | SG-D-02.3.HL | CRA | Annex I Part II (5) + Art. 13(8) sentence 6 + Annex I Part II (4) + Annex I Part II (6) | — | The publicly identifiable contact address and the single point of contact are discharged through the coordinated vulnerability disclosure policy required for the Critical Class assessment. |
| `AG-D-02.3-003` | Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle (Art. 21(2)(e)). | achieve | Confidentiality | SG-D-02.3.HL | NIS 2 | Art. 21(2)(e) | ID.RA-01, GV.SC-04 | — |

### D-02.4 — Threat-Led Penetration Testing

**High-Level Security Goal (SG-D-02.4.HL):** The security of the asset — product with digital elements, ICT-supported business functions / information assets / ICT assets, or high-risk AI system — is tested on a continuing basis, with a layered testing architecture combining conventional product-security testing, ICT defensive-capability testing (portfolio of testing modalities with periodic advanced TLPT), and AI-specific risk-management-measure testing plus real-world conditions.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.4-002` | Effective and regular tests and reviews of the security of a product with digital elements are applied on a continuing basis throughout the support period, with the tests and reviews producing evidence of conformity with the Annex I Part I cybersecurity requirements (Annex I Part II (3) + Annex VII §6); reports of the tests carried out to verify conformity are part of the technical documentation (Annex VII §6); the testing programme itself is audited under Module B periodic audits of the vulnerability-handling processes (Annex VIII Part II (8)). | achieve | Confidentiality | SG-D-02.4.HL | CRA | Annex I Part II (3) + Annex VII §6 + Annex VIII Part II (8) | ID.RA-01, PR.PS-06, DE.CM-09 | — |
| `AG-D-02.4-004` | High-risk AI systems are tested to ensure that they perform consistently for their intended purpose (Art. 9(6)) and tested in real-world conditions in accordance with the detailed rules of Art. 60 (Art. 9(7)). | achieve | Confidentiality | SG-D-02.4.HL | AI Act | Art. 9(6) + Art. 9(7) | ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 | Adversarial testing — biometric presentation-attack red-team — runs quarterly and feeds the Art. 9(6)–(7) testing leg of the risk-management system. |

### D-03.1 — Identity Lifecycle Management

**High-Level Security Goal (SG-D-03.1.HL):** Identities of principals that interact with the entity's systems, products, services, components and data are managed in a verifiable, lifecycle-aware manner with documented boundaries between identity types and explicit hand-off protocols at boundary surfaces.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.1-001` | The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification, before action is taken; the controller may request additional information necessary to confirm the identity, and the data subject must supply enough information to enable identification if they wish to exercise the rights (Art. 12(6) + Art. 11(2); the verification scope is constrained by Art. 5(1)(c) data minimisation). | maintain | Confidentiality | SG-D-03.1.HL | GDPR | Art. 12(6) + Art. 11(2) + Art. 5(1)(c) | PR.AA-03, PR.AA-02, ID.AM-08 | — |
| `AG-D-03.1-002` | Identities, credentials, and access entitlements for users, services, and integrated components of the product with digital elements are managed in a verifiable manner throughout the operational lifetime of the product (Annex I Part I (2)(d) + Art. 13(15) type/batch/serial unique identification + Art. 13(17) single point of contact; backed by Annex II §3 unique-identification user information). | maintain | Confidentiality | SG-D-03.1.HL | CRA | Annex I Part I (2)(d) + Art. 13(15) + Annex II §3 | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | — |
| `AG-D-03.1-003` | Identities of the workforce — employees, contractors and other authorised personnel with access to network and information systems — are managed throughout the employment lifecycle, with provisioning on induction, entitlement review on role change, and revocation on separation, integrated into the entity's access-control policy and asset-management discipline (Art. 21(2)(i) HR-security dimension, coordinated by the literal AND with access-control policies and asset management). | maintain | Confidentiality | SG-D-03.1.HL | NIS 2 | Art. 21(2)(i) | PR.AA-01, PR.AA-05, PR.AT-02 | Provisioning, review and revocation are integrated with the government identity systems for border-officer accounts; deprovisioning on separation is contractual with the employing authorities. |

### D-03.2 — Multi-Factor Authentication

**High-Level Security Goal (SG-D-03.2.HL):** Authentication of users, services, and hardware that interact with the entity's systems, products, services, components and data operates through an authentication mechanism of sufficient strength for the risk in scope, with the strictest applicable floor discharging the most permissive on the same authentication event when both apply.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.2-001` | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality (Art. 28(3)(b) + Art. 29 + Art. 32(4) instruction-only processing); the identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification (Art. 12(6) + Art. 11(2)). | maintain | Confidentiality | SG-D-03.2.HL | GDPR | Art. 29 + Art. 32(4) + Art. 28(3)(b) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.2-002` | Protection from unauthorised access uses appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product (Annex I Part I (2)(d) — "including but not limited to" + 3-way OR). | maintain | Confidentiality | SG-D-03.2.HL | CRA | Annex I Part I (2)(d) | PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09 | The non-exhaustive three-way disjunction is discharged by the multi-factor mechanisms already operated under the certified ISMS. |
| `AG-D-03.2-003` | Multi-factor authentication or continuous authentication solutions are used where appropriate, and secured voice, video and text communications as well as secured emergency communication systems are deployed within the entity (Art. 21(2)(j)). | maintain | Confidentiality | SG-D-03.2.HL | NIS 2 | Art. 21(2)(j) | PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03 | Multi-factor authentication applies to all remote access to the eGate management plane and back-office; `where appropriate` is resolved affirmatively for privileged roles. |

### D-03.3 — Authorisation & Least Privilege

**High-Level Security Goal (SG-D-03.3.HL):** The entitlement to perform actions on the entity's systems, products, services, components, and data is managed per least privilege with explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between access surfaces.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.3-001` | Persons authorised to process personal data act only on documented instructions from the controller (or processor), and are bound by confidentiality or an appropriate statutory obligation of confidentiality, with documented instructions binding the controller → processor → authorised-persons chain of authority under Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) and Art. 4(7) + Art. 4(8) anchoring controller and processor definitions. | maintain | Confidentiality | SG-D-03.3.HL | GDPR | Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.3-002` | Access to the product with digital elements, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported (Annex I Part I (2)(d) `protection from unauthorised access through appropriate control mechanisms` + `possible unauthorised access reported` — R1 inclusive reading on `possible`) and attack surfaces including external interfaces limited (Annex I Part I (2)(j)). | maintain | Confidentiality | SG-D-03.3.HL | CRA | Annex I Part I (2)(d) + Annex I Part I (2)(j) | PR.AA-05, PR.AA-06, DE.CM-09 | — |
| `AG-D-03.3-003` | Access-control policies are established and applied at the entity level for the entity's network and information systems, covering access limited to authorised users, services, and hardware on a least-privilege basis, with the literal AND binding access-control + HR-security + asset-management together (Art. 21(2)(i)). | maintain | Confidentiality | SG-D-03.3.HL | NIS 2 | Art. 21(2)(i) | PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02 | The literal AND binds access-control policy, HR security and asset management into one operating discipline across all per-airport deployments. |

### D-03.4 — Secure System Defaults

**High-Level Security Goal (SG-D-03.4.HL):** The default disposition of the entity's data-centric processing systems and the product's product-centric configuration is managed so that the baseline state of every processing system and every product configuration is the minimum-necessary / secure configuration, with relaxation requiring affirmative data-subject or user intervention.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.4-001` | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed — across the four AND-coordinated dimensions of amount of data collected, extent of their processing, period of their storage, and their accessibility — with the additional constraint that personal data are not made accessible without the individual's intervention to an indefinite number of natural persons (Art. 25(2) + Art. 25(1) privacy-by-design cross-anchor + Art. 5(1)(c) data minimisation underlying principle). | maintain | Confidentiality & Privacy Right | SG-D-03.4.HL | GDPR | Art. 25(2) + Art. 25(1) + Art. 5(1)(c) | PR.PS-01, ID.AM-08 | — |
| `AG-D-03.4-002` | Products with digital elements are made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements (Annex I Part I (2)(b)), and the secure-by-default configuration ensures that vulnerabilities can be addressed through security updates — automatic security updates installed within an appropriate timeframe, enabled by default, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them (Annex I Part I (2)(c)). | maintain | Confidentiality & Privacy Right | SG-D-03.4.HL | CRA | Annex I Part I (2)(b) + Annex I Part I (2)(c) | PR.PS-01, ID.AM-08, GV.SC-03 | Secure-by-default covers the shipped kiosk configuration: no default credentials, unused interfaces disabled, and a documented operator reset to the original state. |

### D-04.1 — Incident Detection & Triage

**High-Level Security Goal (SG-D-04.1.HL):** Security-relevant events affecting the entity's systems, products, services, components and data are detected and triaged with documented trigger moments that anchor the downstream notification and response pipelines.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.1-001` | Personal-data breaches are detected and triaged, and the moment of "becoming aware" is documented to anchor the 72-hour notification clock (Art. 33(1) + Art. 4(12) breach definition). | achieve | Availability | SG-D-04.1.HL | GDPR | Art. 33(1) + Art. 4(12) | DE.CM-01, DE.CM-09, RS.MA-02 | — |
| `AG-D-04.1-002` | Relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported (Annex I Part I (2)(l)). | achieve | Availability | SG-D-04.1.HL | CRA | Annex I Part I (2)(l) | PR.PS-04, DE.AE-08, DE.CM-09, DE.CM-01 | — |
| `AG-D-04.1-003` | An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) + Art. 6(8) six-action `incident handling` definition), with the detection dimension operationalised as all-hazards entity-level monitoring that surfaces adverse events affecting service continuity (Art. 21(2) chapeau + Recital 56). | achieve | Availability | SG-D-04.1.HL | NIS 2 | Art. 21(2)(b) + Art. 6(8) + Art. 21(2) chapeau | RS.MA-01, RS.AN-03, DE.CM-01, DE.CM-09 | The all-hazards detection dimension is operated by the 24/7 SOC across kiosk, network, cloud and AI-service telemetry. |

### D-04.2 — Incident Containment & Response

**High-Level Security Goal (SG-D-04.2.HL):** Security incidents affecting the entity's systems, products, services, components and data are contained and mitigated through appropriate measures that address the incident's impact and reduce the probability of further damage.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.2-001` | Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk no longer materialises (Art. 34(3)(b)); the controller describes the measures taken or proposed in the Art. 33(3)(d) supervisory-authority notification. | achieve | Availability | SG-D-04.2.HL | GDPR | Art. 33(3)(d) | RS.MI-01, RS.MI-02, PR.DS-01 | — |
| `AG-D-04.2-002` | The availability of essential and basic functions of a product with digital elements is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer minimises the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)). Where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer takes the corrective measures necessary to bring the product into conformity, or to withdraw or recall the product (Art. 13(21)). | achieve | Availability | SG-D-04.2.HL | CRA | Annex I Part I (2)(h) + Annex I Part I (2)(k) + Annex I Part I (2)(i) | PR.IR-03, ID.AM-08, GV.SC-04 | — |
| `AG-D-04.2-003` | The entity operates the incident-handling capability across all six actions of the Art. 6(8) `incident handling` lifecycle (prevent, detect, analyse, contain, respond, recover), with the `contain` action documented in the entity-level response plan as the lifecycle phase that isolates affected systems and prevents further damage (Art. 21(2)(b)). | achieve | Availability | SG-D-04.2.HL | NIS 2 | Art. 21(2)(b) + Art. 6(8) | RS.MA-01, RS.AN-03 | The six-action Art. 6(8) lifecycle is documented in the entity-level response plan; containment runbooks exist per incident class (kiosk tamper, network intrusion, model misbehaviour). |

### D-04.3 — Incident Notification & Reporting

**High-Level Security Goal (SG-D-04.3.HL):** A major security incident is notified to the applicable recipients within the regulatory timelines applicable to the event's material scope.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.3-001` | A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms (Art. 33(1)). | achieve | Availability & Accountability | SG-D-04.3.HL | GDPR | Art. 33(1) | RS.CO-02, RS.MA-04, RS.MA-03 | Processor-role notification runs to the government controller without undue delay; controller-scope breaches (employee data, audit logs) go to the Dutch supervisory authority. |
| `AG-D-04.3-002` | An actively-exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours (Art. 14(2)(a), `SR-CRA-029`); vulnerability notification within 72 hours with general information, nature of exploit, mitigations, and user actions (Art. 14(2)(b), `SR-CRA-030`); final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`). | achieve | Availability & Accountability | SG-D-04.3.HL | CRA | Art. 14(2)(a) | RS.MA-02, RS.CO-02 | — |
| `AG-D-04.3-003` | A significant incident is notified to the CSIRT or, where applicable, the competent authority via a twin-trigger pattern — an early warning within 24 hours of awareness (Art. 23(4)(a), `SR-NIS2-010`) followed by an incident notification within 72 hours with severity, impact, and (where available) indicators of compromise (Art. 23(4)(b), `SR-NIS2-011`). | achieve | Availability & Accountability | SG-D-04.3.HL | NIS 2 | Art. 23(4)(a) | RS.MA-04, RS.MA-02 | The twin-trigger 24h early warning to the CSIRT is the binding max-SLA clock shared with CRA Art. 14 and GDPR Art. 33 — tension T-001. |
| `AG-D-04.3-004` | A serious incident involving a high-risk AI system is reported to the market surveillance authorities of the Member States where the incident occurred under a differentiated 4-timeline × 4-trigger matrix (Art. 73(1)–(4)): 15 days after the provider becomes aware (default); 10 days if the incident results in death; 2 days for widespread infringement; 15 days from reasonable likelihood of causal link (whichever is later with the awareness trigger, per Art. 73(2)). | achieve | Availability & Accountability | SG-D-04.3.HL | AI Act | Art. 73(1)–(4) | RS.CO-02, RS.MA-04, RS.MA-03, RS.MA-01 | Serious-incident reporting runs on the 15-day default with the 10-day and 2-day accelerated triggers, routed through the same unified notification workflow as CRA/NIS 2/GDPR — tension T-001. |

### D-04.4 — Incident Recovery & Lessons Learned

**High-Level Security Goal (SG-D-04.4.HL):** Systems, products, services, components and data are restored and recovered with documented recovery evidence applicable to the recovery dimensions of all four participating regulators on the same party.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.4-001` | The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(b) + Art. 32(1)(c); Art. 5(1)(f) integrity/confidentiality cross-reference; Art. 32(2) five-event risk-enumeration cross). | maintain | Availability | SG-D-04.4.HL | GDPR | Art. 32(1)(c) + Art. 5(1)(f) + Art. 32(2) | PR.IR-04, PR.DS-11, RC.RP-04 | — |
| `AG-D-04.4-002` | The availability of essential and basic functions of a product with digital elements is protected *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques and minimises the negative impact on services of other devices and networks (Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) corrective measures). | maintain | Availability | SG-D-04.4.HL | CRA | Annex I Part I (2)(h) | PR.IR-03, ID.AM-08 | — |
| `AG-D-04.4-003` | Business continuity, backup management, disaster recovery, and crisis management capabilities are maintained, ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents (Art. 21(2)(c); the `business continuity, such as backup management and disaster recovery, and crisis management` structure imposes an AND chain across the BC + backup + DR + CM triad). | maintain | Availability | SG-D-04.4.HL | NIS 2 | Art. 21(2)(c) | RC.RP-04, PR.DS-11 | The business-continuity + backup + disaster-recovery + crisis-management AND chain is exercised annually across all per-airport deployments. |

### D-05.1 — Data Minimisation

**High-Level Security Goal (SG-D-05.1.HL):** Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the purpose for which it is processed, with a documented necessity assessment and, where the underlying purpose changes, a compatibility assessment confirming that the new use is consistent with the original. Special-category data is processed only where a narrow exception applies and is documented to that effect.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.1-001` | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing is compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing. | maintain | Privacy Right | SG-D-05.1.HL | GDPR | Art. 5(1)(c) + Art. 6(4) | — | The Art. 9 special-category leg is ACTIVE for this case: biometric templates are processed under Art. 9(2)(g) (substantial public interest) with a statutory DPIA — no inert-basis note applies. |
| `AG-D-05.1-002` | Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)). | maintain | Privacy Right | SG-D-05.1.HL | CRA | Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) | ID.AM-08, ID.AM-03 | — |
| `AG-D-05.1-004` | High-risk AI systems which make use of techniques involving the training of AI models with data are developed on the basis of training, validation and testing data sets that meet the quality criteria — relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose (Art. 10(3)) — supported by data governance practices that detect, prevent and mitigate possible biases (Art. 10(1) + Art. 10(2) 8-element closed list (a)–(h)). | maintain | Privacy Right | SG-D-05.1.HL | AI Act | Art. 10(1) + Art. 10(2) + Art. 10(3) | — | Training/validation/testing data governance must demonstrate representativeness across Schengen traveller demographics; bias detection and mitigation are conformity-assessment objects. |

### D-05.2 — Retention & Archiving

**High-Level Security Goal (SG-D-05.2.HL):** Data — across the data classes in scope — is retained for the period required to satisfy its declared purpose, with documented retention rationale and, where the underlying purpose changes, a reset of the retention clock. Long-term archiving or research-only retention is paired with safeguards proportional to the residual identifiability.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.2-001` | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)). | maintain | Privacy Right | SG-D-05.2.HL | GDPR | Art. 5(1)(e) + Art. 30(1)(f) | ID.AM-08, ID.AM-03 | — |
| `AG-D-05.2-002` | Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail (Art. 13(9) 10-year update-availability tail + Art. 13(8) 5-year support-period floor + Art. 13(18) 10-year Annex II information accessibility + Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge, with advisory messages); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7). | maintain | Privacy Right | SG-D-05.2.HL | CRA | Art. 13(9) + Annex I Part II (7) + Annex I Part II (8) + Art. 13(18) | — | The 5-year support-period floor and the 10-year availability tail are absolute; they do not scale with company size. |
| `AG-D-05.2-004` | Providers of high-risk AI systems keep the logs referred to in Art. 12(1) — automatically generated by their high-risk AI systems and to the extent such logs are under their control — for a period appropriate to the intended purpose, of at least six months, unless provided otherwise in the applicable Union or national law, in particular Union law on the protection of personal data (Art. 19(1)). | maintain | Privacy Right | SG-D-05.2.HL | AI Act | Art. 19(1) | PR.PS-04, GV.PO-02 | The six-month log-retention floor is a floor, not a ceiling: match-decision audit events are retained 10 years under the controller's border-security legislation — retention prevails per tension T-002. |

### D-05.3 — Right to Erasure

**High-Level Security Goal (SG-D-05.3.HL):** Data held about a person is rendered inaccessible to the controller on the data subject's election, and data held by a product with digital elements is rendered inaccessible to the manufacturer on the user's election, by whichever mechanism — the controller-side policy execution or the manufacturer-side product affordance — applies to the data object. Erasure is performed without undue delay and is documented to demonstrate compliance; where a processor is involved, the processor-side mirror ensures deletion-or-return at contract end.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.3-001` | Personal data are erased without undue delay on the data subject's Art. 17(1) request where one of the six Art. 17(1) grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn (no other Art. 6(1) basis applies); (c) Art. 21(1) objection (no overriding compelling legitimate ground) or Art. 21(2) direct-marketing objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child (Art. 8(1)). On processor contract end, the processor deletes or returns all personal data and existing copies per Art. 28(3)(g). | cease | Privacy Right | SG-D-05.3.HL | GDPR | Art. 28(3)(g) | — | Traveller erasure requests are exercised via the government controller (processor mirror: delete-or-return at contract end); irreversible de-linking of biometric templates is the operative mechanism — tension T-002. |
| `AG-D-05.3-002` | The user of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner (Annex I Part I (2)(m) first limb — terminal deletion on user election — and second limb — secure cross-product transfer). | cease | Privacy Right | SG-D-05.3.HL | CRA | Annex I Part I (2)(m) | PR.DS-10, ID.AM-08, PR.DS-02 | The secure-removal affordance maps to traveller-data purge at gate decommissioning or contract end. |

### D-05.4 — Data Portability

**High-Level Security Goal (SG-D-05.4.HL):** Personal data are exported to the data subject in a structured, commonly used, machine-readable format, and the data subject can transmit those data to another controller without hindrance, subject to the qualifying conditions and exclusions that scope the right.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.4-001` | The data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)). The data subject can transmit those data to another controller without hindrance (Art. 20(1)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2). The right applies where processing is based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) AND processing is carried out by automated means (Art. 20(3)); the right does NOT apply to public-interest-task or legitimate-interest processing (Art. 20(4)), and the controller may refuse an export where it would adversely affect third-party rights. | achieve | Privacy Right | SG-D-05.4.HL | GDPR | Art. 15(3) | PR.DS-10, ID.AM-08 | — |

### D-06.1 — Vendor Risk Assessment

**High-Level Security Goal (SG-D-06.1.HL):** Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.1-001` | The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)); the Art. 28(3) DPA closed-list clauses (a)–(h) are documented and the sub-processor authorisation chain (Art. 28(2)) is material to the due diligence. | achieve | Accountability | SG-D-06.1.HL | GDPR | Art. 28(1) + Art. 28(2) | GV.SC-02, GV.SC-03 | — |
| `AG-D-06.1-002` | The manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity (Art. 3(48) FOSS definition) — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) sentence 1); on becoming aware of a component vulnerability (Art. 13(6) sentence 1), the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier (Art. 13(6) sentence 2). | achieve | Accountability | SG-D-06.1.HL | CRA | Art. 13(5) + Art. 3(48) | GV.SC-01, GV.SC-02, ID.RA-02 | Third-party and open-source component due diligence feeds the SBOM; component vulnerabilities are remediated without delay and shared with the component supplier. |
| `AG-D-06.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational measures across direct supplier and service-provider relationships, including security-related aspects of those relationships (Art. 21(2)(d)), taking into account state of the art (Art. 21(1) sentence 2) and the risks posed to the security of network and information systems; the Art. 21(3) sentence 1 three-prong supplier assessment (supplier-specific vulnerabilities + overall quality of products and cybersecurity practices + supplier secure-development procedures) is performed per direct supplier, with EU-level coordinated risk-propagation inputs (Art. 21(3) sentence 2 → Art. 22) taken into account where available. | achieve | Accountability | SG-D-06.1.HL | NIS 2 | Art. 21(2)(d) + Art. 21(1) + Art. 21(1) sentence 2 | GV.SC-02, GV.SC-03 | The Art. 21(3) three-prong supplier assessment is applied to every direct supplier; hardware suppliers are audited and SBOMs are required contractually (RIGOROUS tier). |

### D-06.2 — Software Bill of Materials (SBOM)

**High-Level Security Goal (SG-D-06.2.HL):** The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.2-002` | The manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)). | achieve | Confidentiality | SG-D-06.2.HL | CRA | Annex I Part II (1) | — | The SBOM is a Critical-Class conformity object: maintained per release and available to the notified body. |

### D-06.3 — Contractual Security Obligations

**High-Level Security Goal (SG-D-06.3.HL):** Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, as appropriate to the regulatory perspective and the actor involved.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.3-001` | Controller/processor contracts and related transfer instruments include the GDPR-specific contractual security obligations required for personal-data processing: the Art. 28(3)(a)–(h) eight-element DPA floor, sub-processor authorisation and change-notification, processor Art. 32 security-measure commitments, audit/inspection access, and contract-end return/deletion; the Art. 46 appropriate-safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA or is exposed to third-country legal-process pressure. | maintain | Accountability | SG-D-06.3.HL | GDPR | Art. 28(3)(a)–(h) + Art. 48 | — | — |
| `AG-D-06.3-002` | CRA contractual-security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place products with digital elements on the Union market only after verifying conformity assessment, technical documentation, CE marking, and manufacturer identification, and escalate significant risk or vulnerabilities to the manufacturer and MSA while taking corrective measures; distributors act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, and escalate non-conformity or vulnerabilities. | maintain | Accountability | SG-D-06.3.HL | CRA | Art. 13(6) sentence 1 + Art. 13(6) sentence 2 + Art. 19(1) + Art. 19(2) | — | The company distributes its own product directly and occupies neither the importer nor the distributor role; this row binds through the manufacturer-side duties those operators verify against. |
| `AG-D-06.3-003` | Essential and important entities manage contractual security for direct supplier and service-provider relationships by documenting the supplier universe under the `direct` scope-limiter, embedding security-related contractual aspects into supplier relationships, and assessing each direct supplier against the Art. 21(3) three-prong supplier-assessment structure (supplier-specific vulnerabilities + overall quality of products/services and cybersecurity practices + supplier secure-development procedures); Art. 22 coordinated supply-chain risk assessments are taken into account where available. | maintain | Accountability | SG-D-06.3.HL | NIS 2 | Art. 21(2)(d) + Art. 21(1) + Art. 21(1) sentence 2 + Art. 21(3) sentence 1 | — | The `direct` supplier scope-limiter bounds the contractual perimeter; Art. 22 coordinated risk-assessment outputs are incorporated where published. |

### D-06.4 — Third-Party Boundary Management

**High-Level Security Goal (SG-D-06.4.HL):** Third-party boundary responsibilities are explicitly allocated so that non-EU representatives, direct-supplier scope, cross-border routing, substantial-modification accountability, economic-operator identification, and audit/access rights remain traceable to the correct actor and recipient.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.4-001` | Non-EU controllers and processors falling under GDPR Art. 3(2) designate a representative in writing in the Union unless the Art. 27(2) exception applies; the representative is the legal-address and accountability anchor for supervisory-authority and data-subject contact. | maintain | Accountability | SG-D-06.4.HL | GDPR | Art. 27(1) + Art. 27(2)(a) | — | — |
| `AG-D-06.4-002` | CRA third-party boundary management preserves product-compliance accountability across EU/non-EU and supply-chain actor boundaries: a non-EU manufacturer may appoint an authorised representative by written mandate, but core manufacturer obligations remain non-delegable; an importer or distributor that places a product under its own name/trademark or substantially modifies it becomes manufacturer-equivalent; a third party that substantially modifies a product becomes the manufacturer for the affected part (or the entire product if the modification affects the whole product's cybersecurity); economic operators maintain upstream/downstream identification records and provide them to MSAs on reasoned request, retaining the supply-chain information for 10 years. | maintain | Accountability | SG-D-06.4.HL | CRA | Art. 18(1) + Art. 18(2) + Art. 18(3) + Art. 21 | — | — |
| `AG-D-06.4-003` | NIS 2 boundary management is split across cross-border notification routing and entity-side supplier-scope control: for incidents affecting two or more Member States, CSIRTs, competent authorities, and SPOCs route information to other affected Member States and ENISA; for supply-chain boundaries, the Art. 21(2)(d) `direct` supplier/service-provider scope-limiter defines which third parties sit inside the entity's NIS 2 supplier-security perimeter, and Art. 22 coordinated supply-chain risk-assessment outputs feed into supplier decisions where available. | maintain | Accountability | SG-D-06.4.HL | NIS 2 | Art. 21(2)(d) | — | Cross-border incident routing engages CSIRT and ENISA channels where incidents affect two or more Member States; the `direct` supplier perimeter defines the third parties inside the supplier-security boundary. |

### D-07.1 — Secure-by-Design Principles

**High-Level Security Goal (SG-D-07.1.HL):** Security is integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.1-001` | The controller implements appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing (Art. 25(1) GDPR), and ensures that by default only personal data which are necessary for each specific purpose are processed (Art. 25(2) GDPR). | maintain | Confidentiality | SG-D-07.1.HL | GDPR | Art. 25(1) + Art. 25(2) | PR.PS-06, ID.AM-08 | — |
| `AG-D-07.1-002` | When placing a product with digital elements on the market, the manufacturer ensures that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I (Art. 13(1) CRA), with the cybersecurity risk assessment propagated across the 6 lifecycle phases (planning, design, development, production, delivery, maintenance) per Art. 13(2) chapeau + sentence 1, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact (Art. 13(2) sentence 2). | maintain | Confidentiality | SG-D-07.1.HL | CRA | Art. 13(1) | PR.PS-06, GV.PO-02 | The six-phase risk propagation (planning, design, development, production, delivery, maintenance) is the lifecycle backbone of the Critical-Class technical file (RIGOROUS tier). |
| `AG-D-07.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) NIS 2). | maintain | Confidentiality | SG-D-07.1.HL | NIS 2 | Art. 21(2)(e) | PR.PS-06, GV.SC-02 | Acquisition, development and maintenance security is delivered through the certified-ISMS secure-SDLC policy extended with AI-specific gates (RIGOROUS tier). |
| `AG-D-07.1-004` | High-risk AI systems are designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle (Art. 15(1) AI Act). | maintain | Confidentiality | SG-D-07.1.HL | AI Act | Art. 15(1) | PR.PS-06, PR.IR-03, ID.RA-04 | The accuracy/robustness/cybersecurity triad of Art. 15(1) is designed into the border-control AI system and evidenced across the lifecycle for the notified body (RIGOROUS tier). |

### D-07.2 — Secure Coding Practices

**High-Level Security Goal (SG-D-07.2.HL):** Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system attack-defence under an appropriate coding-practice evidence base.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.2-002` | The manufacturer designs, develops, and produces the product with digital elements to limit its attack surfaces, including attack surfaces of external interfaces (Annex I Part I (2)(j) CRA), and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k) CRA). | maintain | Confidentiality | SG-D-07.2.HL | CRA | Annex I Part I (2)(j) | PR.PS-01, PR.PS-02 | — |
| `AG-D-07.2-004` | High-risk AI systems are designed and developed with appropriate technical and organisational measures to enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws (Art. 15(4)–(5) AI Act). | maintain | Confidentiality | SG-D-07.2.HL | AI Act | Art. 15(4)–(5) | ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03 | Defence legs cover data poisoning, model poisoning, adversarial examples and model evasion, confidentiality attacks, and model flaws; adversarial testing cadence per D-02.4. |

### D-07.3 — CI/CD Pipeline Security

**High-Level Security Goal (SG-D-07.3.HL):** CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-agent integrity, ephemeral build environments) and update-distribution delivery-path security.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.3-002` | The manufacturer of a product with digital elements shall securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates (Annex I Part II (7) CRA), and ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take (Annex I Part II (8) CRA). | maintain | Confidentiality | SG-D-07.3.HL | CRA | Annex I Part II (1) + Annex VII §2(b) + Annex VII §8 | ID.AM-02, GV.SC-03 | Secure update distribution is free of charge, clearly described, and carries security-improvement and user-action information; automatic update applies where appropriate across the kiosk fleet. |
| `AG-D-07.3-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in the maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) third clause NIS 2). | maintain | Confidentiality | SG-D-07.3.HL | NIS 2 | Art. 21(2)(e) | PR.PS-02, ID.RA-01 | Maintenance security includes the signed-release pipeline for kiosk firmware and model updates (RIGOROUS tier). |

### D-08.1 — General Security Awareness

**High-Level Security Goal (SG-D-08.1.HL):** General security awareness is established through a documented training programme with population-wide coverage, audience-routing, and governance hooks.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.1-001` | The data protection officer informs and advises the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions (Art. 39(1)(a) GDPR), and monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR). | maintain | Accountability | SG-D-08.1.HL | GDPR | Art. 39(1)(b) + Art. 39(1)(a) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.1-002` | A product with digital elements is accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA). | maintain | Accountability | SG-D-08.1.HL | CRA | Annex II §8(a)–(f) + Art. 13(18) | PR.AT-01 | Commissioning and lifetime security instructions accompany every eGate deployment (Annex II §8). |
| `AG-D-08.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure basic cyber hygiene practices and cybersecurity training (Art. 21(2)(g) first clause NIS 2). | maintain | Accountability | SG-D-08.1.HL | NIS 2 | Art. 21(2)(g) | PR.AT-01, PR.PS-01 | Basic cyber hygiene and training run as the certified-ISMS annual awareness programme across the 450-person workforce. |

### D-08.2 — Role-Specific Competence

**High-Level Security Goal (SG-D-08.2.HL):** Role-specific competence is established through a function-specific depth, audience-routing, competence-criteria-anchored training, and governance hooks architecture.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.2-001` | The data protection officer monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR) — the role-specific layer of the DPO-catalysed awareness function. | maintain | Accountability | SG-D-08.2.HL | GDPR | Art. 39(1)(b) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.2-002` | Where the product with digital elements is intended for integration into other products with digital elements, the manufacturer provides the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA). | maintain | Accountability | SG-D-08.2.HL | CRA | Annex II §8(f) | PR.AT-02, GV.SC-03 | — |
| `AG-D-08.2-003` | Member States shall encourage essential and important entities to offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2 NIS 2). | maintain | Accountability | SG-D-08.2.HL | NIS 2 | Art. 20(2) sentence 2 | PR.AT-01, PR.AT-02 | Role-specific curricula cover SOC, engineering and governance functions on a regular cadence per Art. 20(2). |
| `AG-D-08.2-004` | High-risk AI systems are designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use (Art. 14(1) AI Act) — the provider-side design obligation for the human-oversight capability. | maintain | Accountability | SG-D-08.2.HL | AI Act | Art. 14(4) + Art. 26(2) | PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04 | Human-oversight competence: border officers and internal overseers are trained on the oversight tools, the override logic and AI-limitation briefings (Art. 14 design leg + Art. 26 deployer obligations). |

### D-09.1 — Information Security Policies

**High-Level Security Goal (SG-D-09.1.HL):** Information security policies are established through a **documented policy architecture** with **governance hooks** and an **accountability chain** that anchor the entity's cybersecurity posture.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.1-001` | The controller implements **appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner** (Art. 24(1) GDPR), with the Art. 5(2) accountability burden and the DPO as the governance anchor (Art. 37-39). | maintain | Accountability | SG-D-09.1.HL | GDPR | Art. 24(1) + Art. 5(2) | GV.PO-01, GV.PO-02, GV.RM-04, GV.OV-03 | — |
| `AG-D-09.1-002` | An open-source software steward **puts in place and documents in a verifiable manner a cybersecurity policy** (Art. 24(1) CRA) covering vulnerability documentation, remediation, and information-sharing within the open-source community; a manufacturer **establishes policies, processes and procedures necessary to implement its CRA cybersecurity obligations** (Art. 13(8) CRA) including CVD policy, secure-update distribution, support-period determination, and cessation-of-operations communication. | maintain | Accountability | SG-D-09.1.HL | CRA | Art. 24(1) | GV.PO-01, GV.SC-01, GV.PO-02, GV.OC-03 | — |
| `AG-D-09.1-003` | The management body of essential and important entities **approves the cybersecurity risk-management measures, oversees their implementation, and can be held liable for infringements** (Art. 20(1) sentence 1 NIS 2); the entity adopts **policies on risk analysis and information system security** (Art. 21(2)(a)) and **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f)). | maintain | Accountability | SG-D-09.1.HL | NIS 2 | Art. 20(1) sentence 1 + Art. 21(2)(a) + Art. 21(2)(f) | ID.RA-05, GV.PO-01, PR.PS-01, ID.IM-01, GV.OV-03 | Management-body approval, oversight and liability (Art. 20(1)) are anchored in board-level sign-off of the cybersecurity risk-management measures; the certified ISMS is the adopted policy vehicle. |
| `AG-D-09.1-004` | High-risk AI systems are **designed and developed to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately** (Art. 13(1) AI Act), accompanied by **concise, complete, correct and clear instructions for use** (Art. 13(3) AI Act); a provider **puts a quality management system in place** documented in written policies, procedures and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act). | maintain | Accountability | SG-D-09.1.HL | AI Act | Art. 13(1) + Art. 13(3) + Art. 17(1) | GV.PO-01, GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04 | The provider-side quality management system (Art. 17, 13 aspects) is implemented as a dedicated AI annex to the certified ISMS — one policy architecture, four regulatory readings. |

### D-09.2 — Impact & Risk Assessments

**High-Level Security Goal (SG-D-09.2.HL):** Impact and risk assessments are established through a **documented assessment** of identified risks and mitigation measures, with a **review cadence** calibrated to the lifecycle phase of the assessment object.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.2-001` | Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a **data-protection impact assessment** covering the four Art. 35(7) content items and reviewed on change of risk per Art. 35(11) (Art. 35(1) + Art. 35(7) GDPR). | achieve | Accountability | SG-D-09.2.HL | GDPR | Art. 35(1) + Art. 35(7) + Art. 35(11) | ID.RA-01, ID.RA-05, ID.RA-06, RS.AN-03, ID.IM-04 | — |
| `AG-D-09.2-002` | The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2)** and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2) and indicating Annex I Part I (2) applicability (Art. 13(3) sentence 3) — documented in the **Annex VII §3 risk-assessment record** (Art. 13(4) sentence 1 + Annex VII §3 CRA). | achieve | Accountability | SG-D-09.2.HL | CRA | Art. 13(3) sentence 2 + Art. 13(3) sentence 3 + Annex VII §3 + Art. 13(4) sentence 1 | PR.PS-06, GV.PO-02, ID.RA-05, GV.OV-02 | The cybersecurity risk assessment is recorded per Annex VII §3 and updated during the support period; it shares its evidence base with the DPIA — tension T-003. |
| `AG-D-09.2-003` | Essential and important entities establish **policies on risk analysis and information system security** (Art. 21(2)(a) NIS 2) on a continuous basis, taking into account the proportionality factors (degree of exposure, likelihood of incidents, severity, state of the art, costs of implementation per Recital 56); the Cooperation Group may carry out coordinated supply-chain risk assessments under Art. 22(1) NIS 2 that NSIEs take into account per Art. 21(3) sentence 2. | achieve | Accountability | SG-D-09.2.HL | NIS 2 | Art. 21(2)(a) | ID.RA-05, GV.PO-01, GV.RM-06, ID.RA-06, PR.IR-01 | Continuous risk analysis under the proportionality factors (exposure, likelihood, severity, state of the art, cost of implementation); Art. 22 coordinated assessments incorporated where available. |
| `AG-D-09.2-004` | A risk management system is **established, implemented, documented and maintained** in relation to high-risk AI systems (Art. 9(1) AI Act), comprising the four Art. 9(2)(a)-(d) steps: identify and analyse known and reasonably foreseeable risks; estimate and evaluate reasonably-foreseeable-misuse risks; evaluate post-market-monitoring-data risks; and adopt appropriate and targeted risk-management measures. | achieve | Accountability | SG-D-09.2.HL | AI Act | Art. 9(1) + Art. 9(2)(a)–(d) | GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, ID.RA-06 | The Art. 9 risk-management system and the GDPR DPIA run as one unified assessment with dual outputs (fundamental-rights leg included) — tension T-003. |

### D-09.4 — Records of Processing

**High-Level Security Goal (SG-D-09.4.HL):** Records of processing activities are established through **parallel documentation regimes** that produce records of processing activities, technical documentation, certification records, information security policy documentation, and quality management system documentation serving distinct audit purposes.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.4-001` | Each controller and processor **maintains a record of processing activities under its responsibility** (Art. 30(1) GDPR), in writing or electronic form (Art. 30(3) GDPR), containing the Art. 30(1) 7-item content list; the processor maintains a parallel record under Art. 30(2) GDPR; records are made available to the supervisory authority on request (Art. 30(4) GDPR), subject to the Art. 30(5) 250-employee exception. | maintain | Accountability | SG-D-09.4.HL | GDPR | Art. 30(1) + Art. 30(4) + Art. 30(5) + Art. 30(3) | ID.AM-03, GV.PO-02, PR.PS-04, DE.AE-03, RS.AN-07, PR.AA-02 | The Art. 30(5) under-250-employee exception is NOT relied upon: processing is large-scale biometric data on a continuous basis; controller-side and processor-side records are both maintained. |
| `AG-D-09.4-002` | The manufacturer **draws up before placing a product with digital elements on the market the technical documentation referred to in Art. 31** (Art. 13(12) sentence 1 CRA), carries out the conformity assessment procedure referred to in Art. 32, draws up the EU declaration of conformity under Art. 28, and affixes the CE marking under Art. 30 (Art. 13(12) sentence 2); the manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA). | maintain | Accountability | SG-D-09.4.HL | CRA | Art. 13(12) sentence 1 + Art. 13(12) sentence 2 | GV.PO-02, GV.OC-03, ID.AM-02, ID.RA-04, GV.SC-04 | Technical documentation, EU declaration of conformity and conformity marking follow the Critical-Class (notified-body) route; retained at least 10 years. |
| `AG-D-09.4-003` | Member States shall **encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems** (Art. 24(1) sentence 1 NIS 2) and of qualified trust services (Art. 24(1) sentence 2); the Commission may adopt delegated acts specifying entities that must use certified ICT products, services and processes (Art. 24(2) NIS 2), and ENISA may be requested to prepare a candidate European cybersecurity certification scheme (Art. 24(3) NIS 2). | maintain | Accountability | SG-D-09.4.HL | NIS 2 | Art. 24(1) sentence 1 + Art. 24(2) + Art. 24(1) sentence 2 | GV.SC-04, GV.OC-03 | Standards use under Art. 24(1) is presumed via the certified ISMS; delegated-act certification obligations are tracked. |
| `AG-D-09.4-004` | Providers of high-risk AI systems **draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service** (Art. 11(1) AI Act), **keep the logs automatically recorded by the high-risk AI system to the extent under their control** (Art. 19(1) AI Act), and document the **quality management system** in written policies, procedures, and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act). | maintain | Accountability | SG-D-09.4.HL | AI Act | Art. 19(1) + Art. 17(1) | PR.PS-04, GV.PO-02, RC.RP-03, GV.PO-01, GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04 | Annex IV technical documentation is drawn up before placing on the market and kept up to date for 10 years; Art. 12/Art. 19 logs and the Art. 17 quality-management documentation complete the provider record set. |

### D-10.1 — Continuous Security Monitoring

**High-Level Security Goal (SG-D-10.1.HL):** Continuous security monitoring is established through a **layered detection-and-monitoring architecture** spanning personal-data processing systems, network and information systems, on-device product activity, ICT systems and tools, and high-risk AI systems, with detection capability feeding the incident-response chain.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.1-001` | The controller and processor implement appropriate technical and organisational measures to ensure the **ongoing confidentiality, integrity, availability and resilience of processing systems and services** (Art. 32(1)(b) GDPR) and **regularly test, assess and evaluate their effectiveness** (Art. 32(1)(d) GDPR); personal-data processing systems and services are monitored for the five Art. 32(2) risk types, with a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock. | maintain | Availability | SG-D-10.1.HL | GDPR | Art. 32(2) | RS.CO-03, RS.MA-04, PR.DS-01, PR.IR-03 | — |
| `AG-D-10.1-002` | A product with digital elements **provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provides an opt-out mechanism for the user** (Annex I Part I (2)(l) CRA); the manufacturer **facilitates the sharing of information about potential vulnerabilities** through a single contact address (Annex I Part II (6) CRA). | maintain | Availability | SG-D-10.1.HL | CRA | Annex I Part I (2)(l) + Annex I Part II (6) | DE.CM-09, DE.CM-01, ID.RA-04, GV.OV-01 | — |
| `AG-D-10.1-003` | Essential and important entities establish an **incident-handling capability** covering prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) NIS 2); the detection dimension is the partial-coverage dimension of D-10.1, operating on an all-hazards basis and feeding the Art. 23(1) significant-incident notification chain. | maintain | Availability | SG-D-10.1.HL | NIS 2 | Art. 21(2)(b) | DE.CM-01, DE.CM-09, RS.MA-04, RS.MA-03 | All-hazards detection is operated by the 24/7 SOC and feeds the Art. 23 significant-incident chain (RIGOROUS tier). |
| `AG-D-10.1-004` | Providers of high-risk AI systems **establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system** (Art. 72(1) AI Act), with the system **actively and systematically collecting, documenting and analysing relevant data** (Art. 72(2) AI Act); market-surveillance cooperation under Regulation (EU) 2019/1020 applies (Art. 74(1) AI Act). | maintain | Availability | SG-D-10.1.HL | AI Act | Art. 74(1) | DE.CM-09, ID.IM-04, GV.OV-03, RS.CO-02, RS.MA-04, RS.MA-03, RS.MA-01 | Post-market monitoring (Art. 72) actively collects and analyses field data — accuracy drift, false-accept and false-reject rates — through the same SOC pipeline (RIGOROUS tier). |

### D-10.2 — Audit Logging & Traceability

**High-Level Security Goal (SG-D-10.2.HL):** Audit logging and traceability are established through a **layered audit-records architecture** spanning compliance records with integrity and traceability, product-level technical documentation traceability, entity-level information security policy documentation, and AI-system event logging with retention floors.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.2-001` | The controller and processor **maintain compliance records in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections** (Art. 30(3) + Art. 5(2) + Art. 31 GDPR), including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — made available to the supervisory authority on request (Art. 30(3)). | maintain | Availability & Accountability | SG-D-10.2.HL | GDPR | Art. 5(2) + Art. 30(3) + Art. 31 | GV.PO-02, GV.OV-03, ID.AM-03, PR.PS-04, DE.AE-03, RS.AN-07 | — |
| `AG-D-10.2-002` | The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmonised standards applied, test reports, copy of the EU declaration of conformity, SBOM on MSA reasoned request), **preserves the cybersecurity risk-assessment documentation** (Annex VII §3 + Art. 13(4) sentence 1) during the support period (10 years or support period, whichever longer) with updates as appropriate, and ensures **test reports demonstrating verification of conformity with Annex I Part I and Part II** are part of the technical documentation and available on reasoned request from market surveillance authorities (Annex VII §6 + Annex I Part II (3) + Art. 13(22) CRA). | maintain | Availability & Accountability | SG-D-10.2.HL | CRA | Annex VII §5 + Annex VII §6 + Annex VII §3 + Art. 13(4) sentence 1 | GV.OC-03, ID.RA-04, GV.SC-04, ID.RA-05, GV.OV-01, GV.PO-02, PR.PS-02 | — |
| `AG-D-10.2-004` | Providers of high-risk AI systems ensure the systems **technically allow for the automatic recording of events (logs) over the lifetime of the system** (Art. 12(1) AI Act) with logging capabilities ensuring a level of traceability of the functioning **appropriate to the intended purpose** (Art. 12(2) AI Act); providers **keep the logs** automatically generated by the high-risk AI system, to the extent under their control, for a period **appropriate to the intended purpose and of at least six months** unless provided otherwise in the applicable Union or national law (Art. 19(1) AI Act). | maintain | Availability & Accountability | SG-D-10.2.HL | AI Act | Art. 12(1) + Art. 12(2) + Art. 19(1) | PR.PS-04, DE.CM-09, DE.AE-03, GV.PO-02, RC.RP-03 | Art. 12 automatic event logging with intended-purpose traceability; logs kept at least six months under provider control, match-decision audit events 10 years per controller policy — tension T-002. |

### D-10.3 — Compliance Testing

**High-Level Security Goal (SG-D-10.3.HL):** Compliance testing is established through a **5-parallel-testing-programme architecture** spanning effectiveness-evaluation of security measures, effectiveness-assessment of risk-management measures, product-level conformity-assessment, entity-level digital operational resilience testing with TLPT, and AI-system-level testing for risk management with real-world-conditions and accuracy/robustness/cybersecurity baseline testing.

| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.3-001` | The controller and processor implement appropriate technical and organisational measures including **a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing** (Art. 32(1)(d) GDPR); the DPIA is **reviewed at least when there is a change of the risk represented by processing operations** (Art. 35(11) GDPR). | maintain | Accountability | SG-D-10.3.HL | GDPR | Art. 34(1) + Art. 34(2) + Art. 32(2) + Art. 34(3)(c) | RS.CO-03, RS.MA-04, RS.CO-02, ID.AM-08 | — |
| `AG-D-10.3-002` | Manufacturers of products with digital elements **carry out effective and regular tests and reviews of the product** (Annex I Part II (3) CRA), and the technical documentation shall contain **the reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I** (Annex VII §6 CRA); conformity is demonstrated via the Annex VIII Part I (Module A internal production control) or Part II (Module B+C and H notified-body EU-type examination) conformity-assessment modules depending on product classification (Class I / Class II / critical per Art. 6 + Annex III). | maintain | Accountability | SG-D-10.3.HL | CRA | Annex VII §6 + Annex I Part II (3) | ID.RA-04, GV.OV-01, GV.PO-02, ID.RA-01, GV.OC-03, GV.SC-04 | Conformity is demonstrated via the notified-body route for Critical Class — the internal-production-control module of default-class products does not apply. |
| `AG-D-10.3-003` | Essential and important entities establish **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f) NIS 2) as part of the all-hazards risk-management framework; the cadence is entity-discretionary under Recital 56 (no quantitative threshold in the OJ). | maintain | Accountability | SG-D-10.3.HL | NIS 2 | Art. 21(2)(f) | GV.PO-01, ID.IM-01, GV.OV-03, GV.PO-02 | Effectiveness-assessment policies under Art. 21(2)(f) with entity-discretionary cadence; annual external audit via the certified ISMS. |
| `AG-D-10.3-004` | Providers of high-risk AI systems ensure the systems are **tested for the purpose of identifying the most appropriate and targeted risk management measures**, and **testing shall ensure that high-risk AI systems perform consistently for their intended purpose** (Art. 9(6) AI Act); testing procedures may include **testing in real-world conditions in accordance with Article 60** (Art. 9(7) AI Act); high-risk AI systems are **designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout their lifecycle** (Art. 15(1) AI Act). | maintain | Accountability | SG-D-10.3.HL | AI Act | Art. 9(6) + Art. 9(7) + Art. 15(1) | ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04, PR.IR-03 | Art. 9(6)–(7) testing (including real-world conditions per Art. 60) evidences consistent performance; results feed the notified-body conformity assessment. |
---

## §4 Tensions Resolved (4 tensions)

### T-001 (D-04.3) — Four-regulation notification timing

**Type:** timing | **Severity:** HIGH

**Root cause.** Four regulations impose notification duties on overlapping events with different clocks and recipients: CRA Art. 14 (24h early warning for actively exploited vulnerabilities), NIS 2 Art. 23 (24h early warning + 72h notification to the CSIRT), GDPR Art. 33 (72h to the supervisory authority, processor-to-controller without undue delay), and AI Act Art. 73 (15-day serious-incident default with 10-day and 2-day accelerated triggers to market surveillance authorities). A single serious incident involving the AI-enabled product can trigger all four simultaneously.

**Resolution.** A single unified notification workflow operates with the **shortest applicable regulatory deadline (max-SLA 24h routing)**: one internal triage pipeline generates per-recipient submissions from one clock-start discipline, so the company bears all four obligations on the same incident record rather than running four divergent workflows.

**Risk if unresolved.** HIGH — administrative fines under all four regimes plus market-surveillance non-conformity; for a critical-infrastructure supplier, notification failure also carries licence-to-operate risk with government customers.

**Anchors:** §3 D-04.3 rows (`AG-D-04.3-001` .. `AG-D-04.3-004`).

### T-002 (D-05.2, D-05.3, D-10.2) — Erasure versus AI log retention

**Type:** requirement | **Severity:** MEDIUM

**Root cause.** GDPR erasure (Art. 17) pulls toward deletion of traveller data, while the AI Act requires event logging and log retention (Art. 12, Art. 19, six-month floor) and border-security legislation requires long retention of match-decision audit records. The same decision event is simultaneously personal data (erasable) and a regulated log record (retainable).

**Resolution.** Token-based separation: biometric templates and raw captures are irreversibly de-linked and purged on erasure, while match-decision audit events carry no biometric content (token-only) and are retained under the longest applicable regulatory floor (10 years). Erasure therefore never destroys a regulated log record, and retention never preserves biometric material.

**Risk if unresolved.** MEDIUM — either a GDPR erasure violation or an AI Act / border-security record-keeping gap. The token-separation design resolves both on the same data model.

**Anchors:** §3 D-05.2 (`AG-D-05.2-004`), D-05.3 (`AG-D-05.3-001`, `AG-D-05.3-002`), D-10.2 (`AG-D-10.2-004`).

### T-003 (D-09.2) — Unified impact and risk assessment (DPIA + FRIA + cybersecurity)

**Type:** trigger | **Severity:** MEDIUM

**Root cause.** GDPR mandates a DPIA before large-scale biometric processing; the AI Act mandates a fundamental-rights impact assessment and a risk-management system for high-risk AI; CRA Art. 13 requires a documented cybersecurity risk assessment maintained over the support period; NIS 2 requires continuous risk analysis. Four assessment regimes with different triggers describe the same system.

**Resolution.** A unified assessment approach with dual/multi outputs: one evidence-gathering pass produces the DPIA, the fundamental-rights leg, the AI risk-management file, the CRA risk-assessment record, and the NIS 2 risk-analysis documentation, reviewed on material change and at least annually.

**Risk if unresolved.** MEDIUM — assessment gaps under one or more regimes; the marginal cost of the unified pass is small once the DPIA exists.

**Anchors:** §3 D-09.2 rows (`AG-D-09.2-001` .. `AG-D-09.2-004`).

### T-004 (D-06.1, D-06.3) — Vendor-management scope across three regimes

**Type:** scope | **Severity:** MEDIUM

**Root cause.** GDPR governs downstream data processors; CRA governs the product supply chain including open-source components; NIS 2 Art. 21(2)-(3) governs direct supplier and service-provider security with a three-prong assessment. The three scopes overlap on the same suppliers but ask different questions of them.

**Resolution.** A single vendor-management template addresses the data-processor obligations, the product supply-chain obligations, and the NIS 2 three-prong supplier assessment, producing multi-output documentation that satisfies all three regulatory scopes from one due-diligence pass.

**Risk if unresolved.** MEDIUM — processor non-compliance plus supply-chain gaps. Mitigation cost is bounded by reuse: the marginal effort of the second and third scopes is small once the first is documented.

**Anchors:** §3 D-06.1 and D-06.3 rows.

---

## §5 Track B Decision Trail (38 rows)

| Sub-Domain | Scale | Inheritability | Priority | Tier | Rationale |
|---|---|---|---|---|---|
| Sub-Domain | Scale | Inheritability | Priority | Tier | Rationale |
|---|---|---|---|---|---|
| D-01.1 Data at Rest Encryption | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — biometric reference data under GDPR Art. 9 — hardware-backed key custody and template-only storage |
| D-01.2 Data in Transit Encryption | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-01.3 Cryptographic Key Management | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — biometric key custody — key-lineage accountability and documented key ceremonies |
| D-01.4 Data Integrity Mechanisms | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-02.1 Vulnerability Identification | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-02.2 Patch Management & Updates | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-02.3 Coordinated Vulnerability Disclosure | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-02.4 Threat-Led Penetration Testing | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-03.1 Identity Lifecycle Management | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-03.2 Multi-Factor Authentication | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-03.3 Authorisation & Least Privilege | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-03.4 Secure System Defaults | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-04.1 Incident Detection & Triage | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-04.2 Incident Containment & Response | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-04.3 Incident Notification & Reporting | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — four-regulation notification surface — max-SLA 24h routing resolves T-001 |
| D-04.4 Incident Recovery & Lessons Learned | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-05.1 Data Minimisation | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-05.2 Retention & Archiving | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-05.3 Right to Erasure | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-05.4 Data Portability | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-06.1 Vendor Risk Assessment | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — NIS 2 Art. 21(2)(d) supply chain + biometric processor chain under GDPR Art. 28 |
| D-06.2 Software Bill of Materials (SBOM) | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-06.3 Contractual Security Obligations | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — multi-tier contractual flowdown across GDPR Art. 28, NIS 2 Art. 21(2)–(3) and the CRA economic-operator chain |
| D-06.4 Third-Party Boundary Management | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-07.1 Secure-by-Design Principles | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — AI Act risk-management system (Art. 9) + CRA secure-by-design lifecycle — one unified SDLC for high-risk AI |
| D-07.2 Secure Coding Practices | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-07.3 CI/CD Pipeline Security | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — NIS 2 maintenance security + supply-chain attack surface — signed-release integrity |
| D-07.4 Change Management | MEDIUM | — | — | NOT_ADDRESSED | DORA-sole-authority sub-domain; DORA is not applicable to this case (R8) — NOT_ADDRESSED. |
| D-08.1 General Security Awareness | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-08.2 Role-Specific Competence | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-08.3 Management Board Training | MEDIUM | — | — | NOT_ADDRESSED | Management-board cybersecurity competence is handled at board-briefing level under NIS 2 Art. 20 governance (carried in D-09.1); no separate training-based competency requirement is retained — NOT_ADDRESSED. |
| D-09.1 Information Security Policies | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-09.2 Impact & Risk Assessments | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-09.3 Asset Inventories | MEDIUM | — | — | NOT_ADDRESSED | DORA-sole-authority sub-domain; DORA is not applicable to this case (R8) — NOT_ADDRESSED. |
| D-09.4 Records of Processing | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-10.1 Continuous Security Monitoring | MEDIUM | BUILD_REQUIRED | MUST | RIGOROUS | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD; RIGOROUS override — NIS 2 Art. 21(2)(b)/(g) + AI Act Art. 72 post-market monitoring — 24/7 SOC with model-drift detection |
| D-10.2 Audit Logging & Traceability | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |
| D-10.3 Compliance Testing | MEDIUM | BUILD_REQUIRED | MUST | STANDARD | §5.1 row MEDIUM col BUILD_REQUIRED = STANDARD |

---

## §6 NIST Controls Mapping

### §6.1 D-01.1 — Data at Rest Encryption

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.1.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |

#### §6.1.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.AC-P5 | Network integrity is protected (e.g., network segregation, network segmentation)... | NIST_PF/PROTECT-P/PR.AC-P5.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |

### §6.2 D-01.2 — Data in Transit Encryption

_Applicable regulations: GDPR, CRA_

#### §6.2.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |

#### §6.2.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.AC-P5 | Network integrity is protected (e.g., network segregation, network segmentation)... | NIST_PF/PROTECT-P/PR.AC-P5.json |

### §6.3 D-01.3 — Cryptographic Key Management

_Applicable regulations: GDPR, CRA_

#### §6.3.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |

#### §6.3.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |

### §6.4 D-01.4 — Data Integrity Mechanisms

_Applicable regulations: GDPR, CRA, AI Act_

#### §6.4.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |

#### §6.4.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| CONTROL-P | CT.DM-P3 | Data elements can be accessed for alteration. | NIST_PF/CONTROL-P/CT.DM-P3.json |
| COMMUNICATE-P | CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organization... | NIST_PF/COMMUNICATE-P/CM.AW-P5.json |

#### §6.4.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-2.6 | AI system is evaluated regularly for safety risks with metrics for system reliab... | NIST_AI_RMF/MEASURE/MEASURE-2.6.json |
| MEASURE | MEASURE-2.7 | AI system security and resilience are evaluated and documented | NIST_AI_RMF/MEASURE/MEASURE-2.7.json |
| MANAGE | MANAGE-2.3 | Procedures are followed to respond to and recover from a previously unknown risk... | NIST_AI_RMF/MANAGE/MANAGE-2.3.json |

### §6.5 D-02.1 — Vulnerability Identification

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.5.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.AM-04 | Inventories of services provided by suppliers are maintained | NIST_CSF/IDENTIFY/ID.AM-04.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |
| IDENTIFY | ID.RA-03 | Internal and external threats to the organization are identified and recorded | NIST_CSF/IDENTIFY/ID.RA-03.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |
| GOVERN | GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizi... | NIST_CSF/GOVERN/GV.RM-06.json |

#### §6.5.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| CONTROL-P | CT.DM-P10 | Stakeholder privacy preferences are included in algorithmic design objectives an... | NIST_PF/CONTROL-P/CT.DM-P10.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| IDENTIFY-P | ID.RA-P5 | Risk responses are identified, prioritized, and implemented. | NIST_PF/IDENTIFY-P/ID.RA-P5.json |

#### §6.5.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GOVERN-1.3 | Risk management processes and procedures | NIST_AI_RMF/GOVERN/GOVERN-1.3.json |
| MAP | MAP-3.1 | Potential benefits of intended functionality and performance are examined and do... | NIST_AI_RMF/MAP/MAP-3.1.json |
| MAP | MAP-3.2 | Potential costs, including non-monetary costs, from expected or realized AI erro... | NIST_AI_RMF/MAP/MAP-3.2.json |
| MAP | MAP-5.1 | Likelihood and magnitude of each identified impact -- based on expected use, pas... | NIST_AI_RMF/MAP/MAP-5.1.json |
| MANAGE | MANAGE-1.2 | Treatment of documented AI risks is prioritized based on impact, likelihood, or ... | NIST_AI_RMF/MANAGE/MANAGE-1.2.json |
| MEASURE | MEASURE-1.1 | Approaches and metrics for measurement of AI risks are selected for implementati... | NIST_AI_RMF/MEASURE/MEASURE-1.1.json |
| MEASURE | MEASURE-2.1 | Test sets, metrics, and details about the tools used during test, evaluation, va... | NIST_AI_RMF/MEASURE/MEASURE-2.1.json |
| MEASURE | MEASURE-2.3 | AI system performance or assurance criteria are measured qualitatively or quanti... | NIST_AI_RMF/MEASURE/MEASURE-2.3.json |
| MAP | MAP-3.3 | Targeted application scope is specified and documented based on a system's capab... | NIST_AI_RMF/MAP/MAP-3.3.json |
| MEASURE | MEASURE-2.5 | AI system to be deployed is demonstrated to be valid and reliable and limitation... | NIST_AI_RMF/MEASURE/MEASURE-2.5.json |
| MEASURE | MEASURE-2.6 | AI system is evaluated regularly for safety risks with metrics for system reliab... | NIST_AI_RMF/MEASURE/MEASURE-2.6.json |
| MEASURE | MEASURE-2.7 | AI system security and resilience are evaluated and documented | NIST_AI_RMF/MEASURE/MEASURE-2.7.json |
| GOVERN | GOVERN-1.2 | Characteristics of trustworthy AI | NIST_AI_RMF/GOVERN/GOVERN-1.2.json |
| MANAGE | MANAGE-2.3 | Procedures are followed to respond to and recover from a previously unknown risk... | NIST_AI_RMF/MANAGE/MANAGE-2.3.json |
| MANAGE | MANAGE-1.3 | Responses to the AI risks deemed high priority are developed, planned, and docum... | NIST_AI_RMF/MANAGE/MANAGE-1.3.json |
| GOVERN | GOVERN-5.1 | Organizational policies and practices are in place to collect, consider, priorit... | NIST_AI_RMF/GOVERN/GOVERN-5.1.json |

### §6.6 D-02.2 — Patch Management & Updates

_Applicable regulations: CRA_

#### §6.6.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| RESPOND | RS.MI-02 | Incidents are eradicated | NIST_CSF/RESPOND/RS.MI-02.json |

### §6.7 D-02.3 — Coordinated Vulnerability Disclosure

_Applicable regulations: CRA, NIS 2_

#### §6.7.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |

### §6.8 D-02.4 — Threat-Led Penetration Testing

_Applicable regulations: CRA, AI Act_

#### §6.8.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |

#### §6.8.2 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-1.1 | Approaches and metrics for measurement of AI risks are selected for implementati... | NIST_AI_RMF/MEASURE/MEASURE-1.1.json |
| MEASURE | MEASURE-2.1 | Test sets, metrics, and details about the tools used during test, evaluation, va... | NIST_AI_RMF/MEASURE/MEASURE-2.1.json |
| MEASURE | MEASURE-2.3 | AI system performance or assurance criteria are measured qualitatively or quanti... | NIST_AI_RMF/MEASURE/MEASURE-2.3.json |
| MAP | MAP-3.3 | Targeted application scope is specified and documented based on a system's capab... | NIST_AI_RMF/MAP/MAP-3.3.json |

### §6.9 D-03.1 — Identity Lifecycle Management

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.9.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-02 | Identities are proofed and bound to credentials based on the context of interact... | NIST_CSF/PROTECT/PR.AA-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AA-06 | Physical access to assets is managed, monitored, and enforced commensurate with ... | NIST_CSF/PROTECT/PR.AA-06.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |

#### §6.9.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| PROTECT-P | PR.AC-P3 | Remote access is managed. | NIST_PF/PROTECT-P/PR.AC-P3.json |
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| CONTROL-P | CT.PO-P3 | Policies, processes, and procedures for enabling individuals’ data processing pr... | NIST_PF/CONTROL-P/CT.PO-P3.json |
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |

### §6.10 D-03.2 — Multi-Factor Authentication

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.10.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |

### §6.11 D-03.3 — Authorisation & Least Privilege

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.11.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AA-06 | Physical access to assets is managed, monitored, and enforced commensurate with ... | NIST_CSF/PROTECT/PR.AA-06.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |

#### §6.11.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| PROTECT-P | PR.AC-P2 | Physical access to data and devices is managed. | NIST_PF/PROTECT-P/PR.AC-P2.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |

### §6.12 D-03.4 — Secure System Defaults

_Applicable regulations: GDPR, CRA_

#### §6.12.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |

#### §6.12.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |

### §6.13 D-04.1 — Incident Detection & Triage

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.13.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| DETECT | DE.CM-03 | Personnel activity and technology usage are monitored to find potentially advers... | NIST_CSF/DETECT/DE.CM-03.json |
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| DETECT | DE.AE-08 | Incidents are declared when adverse events meet the defined incident criteria | NIST_CSF/DETECT/DE.AE-08.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |

#### §6.13.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P5 | Policies, processes, and procedures are established and in place to receive, ana... | NIST_PF/GOVERN-P/GV.MT-P5.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| COMMUNICATE-P | CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or ev... | NIST_PF/COMMUNICATE-P/CM.AW-P7.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |

### §6.14 D-04.2 — Incident Containment & Response

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.14.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MI-02 | Incidents are eradicated | NIST_CSF/RESPOND/RS.MI-02.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |

#### §6.14.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.PO-P7 | Response plans (Incident Response and Business Continuity) and recovery plans (I... | NIST_PF/PROTECT-P/PR.PO-P7.json |
| CONTROL-P | CT.DM-P10 | Stakeholder privacy preferences are included in algorithmic design objectives an... | NIST_PF/CONTROL-P/CT.DM-P10.json |

### §6.15 D-04.3 — Incident Notification & Reporting

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.15.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| RESPOND | RS.CO-02 | Internal and external stakeholders are notified of incidents | NIST_CSF/RESPOND/RS.CO-02.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |
| RESPOND | RS.AN-07 | Incident data and metadata are collected, and their integrity and provenance are... | NIST_CSF/RESPOND/RS.AN-07.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.AN-06 | Actions performed during an investigation are recorded, and the records' integri... | NIST_CSF/RESPOND/RS.AN-06.json |
| RESPOND | RS.AN-08 | An incident's magnitude is estimated and validated | NIST_CSF/RESPOND/RS.AN-08.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| RECOVER | RC.RP-06 | The end of incident recovery is declared based on criteria, and incident-related... | NIST_CSF/RECOVER/RC.RP-06.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| GOVERN | GV.SC-05 | Requirements to address cybersecurity risks in supply chains are established, pr... | NIST_CSF/GOVERN/GV.SC-05.json |

#### §6.15.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| CONTROL-P | CT.DM-P3 | Data elements can be accessed for alteration. | NIST_PF/CONTROL-P/CT.DM-P3.json |
| COMMUNICATE-P | CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organization... | NIST_PF/COMMUNICATE-P/CM.AW-P5.json |
| COMMUNICATE-P | CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or ev... | NIST_PF/COMMUNICATE-P/CM.AW-P7.json |
| COMMUNICATE-P | CM.PO-P2 | Roles and responsibilities (e.g., public relations) for communicating data proce... | NIST_PF/COMMUNICATE-P/CM.PO-P2.json |
| IDENTIFY-P | ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropria... | NIST_PF/IDENTIFY-P/ID.DE-P3.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| COMMUNICATE-P | CM.AW-P8 | Individuals are provided with mitigation mechanisms (e.g., credit monitoring, co... | NIST_PF/COMMUNICATE-P/CM.AW-P8.json |
| IDENTIFY-P | ID.RA-P5 | Risk responses are identified, prioritized, and implemented. | NIST_PF/IDENTIFY-P/ID.RA-P5.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |

#### §6.15.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MANAGE | MANAGE-2.3 | Procedures are followed to respond to and recover from a previously unknown risk... | NIST_AI_RMF/MANAGE/MANAGE-2.3.json |
| MANAGE | MANAGE-4.3 | Incidents and errors are communicated to relevant AI actors including affected c... | NIST_AI_RMF/MANAGE/MANAGE-4.3.json |
| GOVERN | GOVERN-1.1 | Legal and regulatory requirements | NIST_AI_RMF/GOVERN/GOVERN-1.1.json |

### §6.16 D-04.4 — Incident Recovery & Lessons Learned

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.16.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| RECOVER | RC.RP-04 | Critical mission functions and cybersecurity risk management are considered to e... | NIST_CSF/RECOVER/RC.RP-04.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| RECOVER | RC.RP-06 | The end of incident recovery is declared based on criteria, and incident-related... | NIST_CSF/RECOVER/RC.RP-06.json |

#### §6.16.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.17 D-05.1 — Data Minimisation

_Applicable regulations: GDPR, CRA, AI Act_

#### §6.17.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.AA-02 | Identities are proofed and bound to credentials based on the context of interact... | NIST_CSF/PROTECT/PR.AA-02.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |

#### §6.17.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DM-P3 | Data elements can be accessed for alteration. | NIST_PF/CONTROL-P/CT.DM-P3.json |
| COMMUNICATE-P | CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organization... | NIST_PF/COMMUNICATE-P/CM.AW-P5.json |
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |

#### §6.17.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GOVERN-1.4 | Transparent policies, procedures, and other controls for risk management | NIST_AI_RMF/GOVERN/GOVERN-1.4.json |
| MAP | MAP-2.1 | The specific task, and methods used to implement the task, that the AI system wi... | NIST_AI_RMF/MAP/MAP-2.1.json |
| MEASURE | MEASURE-2.11 | Fairness and bias is evaluated and results are documented | NIST_AI_RMF/MEASURE/MEASURE-2.11.json |
| MAP | MAP-2.2 | Documentation of information about a system's knowledge limits and how system ou... | NIST_AI_RMF/MAP/MAP-2.2.json |
| MEASURE | MEASURE-2.10 | Privacy risk of the AI system is examined and documented | NIST_AI_RMF/MEASURE/MEASURE-2.10.json |
| GOVERN | GOVERN-1.1 | Legal and regulatory requirements | NIST_AI_RMF/GOVERN/GOVERN-1.1.json |

### §6.18 D-05.2 — Retention & Archiving

_Applicable regulations: GDPR, CRA, AI Act_

#### §6.18.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |

#### §6.18.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |
| CONTROL-P | CT.DM-P5 | Data are destroyed according to policy. | NIST_PF/CONTROL-P/CT.DM-P5.json |

#### §6.18.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GOVERN-1.4 | Transparent policies, procedures, and other controls for risk management | NIST_AI_RMF/GOVERN/GOVERN-1.4.json |
| MAP | MAP-2.1 | The specific task, and methods used to implement the task, that the AI system wi... | NIST_AI_RMF/MAP/MAP-2.1.json |
| MEASURE | MEASURE-2.11 | Fairness and bias is evaluated and results are documented | NIST_AI_RMF/MEASURE/MEASURE-2.11.json |
| MAP | MAP-2.2 | Documentation of information about a system's knowledge limits and how system ou... | NIST_AI_RMF/MAP/MAP-2.2.json |
| MEASURE | MEASURE-2.4 | Functionality and behavior of the AI system and its components are monitored whe... | NIST_AI_RMF/MEASURE/MEASURE-2.4.json |
| MEASURE | MEASURE-4.2 | Measurement results regarding AI system trustworthiness in deployment context(s)... | NIST_AI_RMF/MEASURE/MEASURE-4.2.json |

### §6.19 D-05.3 — Right to Erasure

_Applicable regulations: GDPR, CRA_

#### §6.19.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| RESPOND | RS.CO-02 | Internal and external stakeholders are notified of incidents | NIST_CSF/RESPOND/RS.CO-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |

#### §6.19.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organization... | NIST_PF/COMMUNICATE-P/CM.AW-P5.json |
| CONTROL-P | CT.DM-P3 | Data elements can be accessed for alteration. | NIST_PF/CONTROL-P/CT.DM-P3.json |
| CONTROL-P | CT.DM-P4 | Data elements can be accessed for deletion. | NIST_PF/CONTROL-P/CT.DM-P4.json |
| CONTROL-P | CT.DM-P5 | Data are destroyed according to policy. | NIST_PF/CONTROL-P/CT.DM-P5.json |
| IDENTIFY-P | ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropria... | NIST_PF/IDENTIFY-P/ID.DE-P3.json |

### §6.20 D-05.4 — Data Portability

_Applicable regulations: GDPR_

#### §6.20.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |

#### §6.20.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| CONTROL-P | CT.DM-P6 | Data are transmitted using standardized formats. | NIST_PF/CONTROL-P/CT.DM-P6.json |

### §6.21 D-06.1 — Vendor Risk Assessment

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.21.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |

#### §6.21.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.DE-P5 | Data processing ecosystem parties are routinely assessed using audits, test resu... | NIST_PF/IDENTIFY-P/ID.DE-P5.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |

### §6.22 D-06.2 — Software Bill of Materials (SBOM)

_Applicable regulations: CRA_

#### §6.22.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |

### §6.23 D-06.3 — Contractual Security Obligations

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.23.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| RESPOND | RS.CO-02 | Internal and external stakeholders are notified of incidents | NIST_CSF/RESPOND/RS.CO-02.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| DETECT | DE.CM-06 | External service provider activities and services are monitored to find potentia... | NIST_CSF/DETECT/DE.CM-06.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| RESPOND | RS.MI-02 | Incidents are eradicated | NIST_CSF/RESPOND/RS.MI-02.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| IDENTIFY | ID.AM-04 | Inventories of services provided by suppliers are maintained | NIST_CSF/IDENTIFY/ID.AM-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §6.23.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or ev... | NIST_PF/COMMUNICATE-P/CM.AW-P7.json |
| IDENTIFY-P | ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropria... | NIST_PF/IDENTIFY-P/ID.DE-P3.json |
| CONTROL-P | CT.DM-P4 | Data elements can be accessed for deletion. | NIST_PF/CONTROL-P/CT.DM-P4.json |
| CONTROL-P | CT.DM-P5 | Data are destroyed according to policy. | NIST_PF/CONTROL-P/CT.DM-P5.json |
| IDENTIFY-P | ID.DE-P5 | Data processing ecosystem parties are routinely assessed using audits, test resu... | NIST_PF/IDENTIFY-P/ID.DE-P5.json |
| CONTROL-P | CT.DM-P9 | Technical measures implemented to manage data processing are tested and assessed... | NIST_PF/CONTROL-P/CT.DM-P9.json |
| IDENTIFY-P | ID.DE-P4 | Interoperability frameworks or similar multi-party approaches are used to manage... | NIST_PF/IDENTIFY-P/ID.DE-P4.json |
| IDENTIFY-P | ID.IM-P7 | The data processing environment is identified (e.g., geographic location, intern... | NIST_PF/IDENTIFY-P/ID.IM-P7.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |

### §6.24 D-06.4 — Third-Party Boundary Management

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.24.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-02 | Internal and external stakeholders are understood, and their needs and expectati... | NIST_CSF/GOVERN/GV.OC-02.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| GOVERN | GV.SC-05 | Requirements to address cybersecurity risks in supply chains are established, pr... | NIST_CSF/GOVERN/GV.SC-05.json |

#### §6.24.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |

### §6.25 D-07.1 — Secure-by-Design Principles

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.25.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.RR-04 | Cybersecurity is included in human resources practices | NIST_CSF/GOVERN/GV.RR-04.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |

#### §6.25.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |

#### §6.25.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MAP | MAP-3.5 | Processes for human oversight are defined, assessed, and documented in accordanc... | NIST_AI_RMF/MAP/MAP-3.5.json |
| GOVERN | GOVERN-2.1 | Roles, responsibilities and lines of communication are documented and clear thro... | NIST_AI_RMF/GOVERN/GOVERN-2.1.json |
| GOVERN | GOVERN-3.1 | Decision-making on risk across the lifecycle is informed by a diverse team | NIST_AI_RMF/GOVERN/GOVERN-3.1.json |
| MEASURE | MEASURE-2.5 | AI system to be deployed is demonstrated to be valid and reliable and limitation... | NIST_AI_RMF/MEASURE/MEASURE-2.5.json |
| MEASURE | MEASURE-2.6 | AI system is evaluated regularly for safety risks with metrics for system reliab... | NIST_AI_RMF/MEASURE/MEASURE-2.6.json |
| MEASURE | MEASURE-2.7 | AI system security and resilience are evaluated and documented | NIST_AI_RMF/MEASURE/MEASURE-2.7.json |
| GOVERN | GOVERN-1.2 | Characteristics of trustworthy AI | NIST_AI_RMF/GOVERN/GOVERN-1.2.json |
| GOVERN | GOVERN-4.1 | Organizational policies, and practices to foster a critical thinking and safety-... | NIST_AI_RMF/GOVERN/GOVERN-4.1.json |
| GOVERN | GOVERN-4.3 | Organizational practices are in place to enable AI testing, identification of in... | NIST_AI_RMF/GOVERN/GOVERN-4.3.json |

### §6.26 D-07.2 — Secure Coding Practices

_Applicable regulations: CRA, AI Act_

#### §6.26.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |

#### §6.26.2 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-2.7 | AI system security and resilience are evaluated and documented | NIST_AI_RMF/MEASURE/MEASURE-2.7.json |
| MAP | MAP-3.2 | Potential costs, including non-monetary costs, from expected or realized AI erro... | NIST_AI_RMF/MAP/MAP-3.2.json |
| MANAGE | MANAGE-1.3 | Responses to the AI risks deemed high priority are developed, planned, and docum... | NIST_AI_RMF/MANAGE/MANAGE-1.3.json |

### §6.27 D-07.3 — CI/CD Pipeline Security

_Applicable regulations: CRA, NIS 2_

#### §6.27.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizi... | NIST_CSF/GOVERN/GV.RM-06.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §6.27.2 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-2.7 | AI system security and resilience are evaluated and documented | NIST_AI_RMF/MEASURE/MEASURE-2.7.json |
| MAP | MAP-5.1 | Likelihood and magnitude of each identified impact -- based on expected use, pas... | NIST_AI_RMF/MAP/MAP-5.1.json |
| GOVERN | GOVERN-5.1 | Organizational policies and practices are in place to collect, consider, priorit... | NIST_AI_RMF/GOVERN/GOVERN-5.1.json |
| MANAGE | MANAGE-1.2 | Treatment of documented AI risks is prioritized based on impact, likelihood, or ... | NIST_AI_RMF/MANAGE/MANAGE-1.2.json |

### §6.28 D-08.1 — General Security Awareness

_Applicable regulations: GDPR, CRA, NIS 2_

#### §6.28.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |

#### §6.28.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |

### §6.29 D-08.2 — Role-Specific Competence

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.29.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.RR-04 | Cybersecurity is included in human resources practices | NIST_CSF/GOVERN/GV.RR-04.json |

#### §6.29.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |

#### §6.29.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MAP | MAP-3.5 | Processes for human oversight are defined, assessed, and documented in accordanc... | NIST_AI_RMF/MAP/MAP-3.5.json |
| GOVERN | GOVERN-2.1 | Roles, responsibilities and lines of communication are documented and clear thro... | NIST_AI_RMF/GOVERN/GOVERN-2.1.json |
| GOVERN | GOVERN-3.1 | Decision-making on risk across the lifecycle is informed by a diverse team | NIST_AI_RMF/GOVERN/GOVERN-3.1.json |
| GOVERN | GOVERN-2.2 | Risk management training for organizational personnel and partners to perform du... | NIST_AI_RMF/GOVERN/GOVERN-2.2.json |

### §6.30 D-09.1 — Information Security Policies

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.30.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| GOVERN | GV.OC-02 | Internal and external stakeholders are understood, and their needs and expectati... | NIST_CSF/GOVERN/GV.OC-02.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| PROTECT | PR.AA-02 | Identities are proofed and bound to credentials based on the context of interact... | NIST_CSF/PROTECT/PR.AA-02.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.RR-01 | Organizational leadership is responsible and accountable for cybersecurity risk ... | NIST_CSF/GOVERN/GV.RR-01.json |
| GOVERN | GV.RR-03 | Adequate resources are allocated commensurate with the cybersecurity risk strate... | NIST_CSF/GOVERN/GV.RR-03.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.RM-05 | Lines of communication across the organization are established for cybersecurity... | NIST_CSF/GOVERN/GV.RM-05.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| IDENTIFY | ID.IM-01 | Improvements are identified from evaluations | NIST_CSF/IDENTIFY/ID.IM-01.json |
| GOVERN | GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizi... | NIST_CSF/GOVERN/GV.RM-06.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| GOVERN | GV.RM-01 | Risk management objectives are established and agreed to by organizational stake... | NIST_CSF/GOVERN/GV.RM-01.json |
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| GOVERN | GV.RR-04 | Cybersecurity is included in human resources practices | NIST_CSF/GOVERN/GV.RR-04.json |

#### §6.30.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| GOVERN-P | GV.PO-P6 | Governance and risk management policies, processes, and procedures address priva... | NIST_PF/GOVERN-P/GV.PO-P6.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| CONTROL-P | CT.PO-P3 | Policies, processes, and procedures for enabling individuals’ data processing pr... | NIST_PF/CONTROL-P/CT.PO-P3.json |
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| IDENTIFY-P | ID.IM-P7 | The data processing environment is identified (e.g., geographic location, intern... | NIST_PF/IDENTIFY-P/ID.IM-P7.json |
| IDENTIFY-P | ID.DE-P5 | Data processing ecosystem parties are routinely assessed using audits, test resu... | NIST_PF/IDENTIFY-P/ID.DE-P5.json |
| IDENTIFY-P | ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropria... | NIST_PF/IDENTIFY-P/ID.DE-P3.json |
| IDENTIFY-P | ID.DE-P4 | Interoperability frameworks or similar multi-party approaches are used to manage... | NIST_PF/IDENTIFY-P/ID.DE-P4.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |

#### §6.30.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GOVERN-1.4 | Transparent policies, procedures, and other controls for risk management | NIST_AI_RMF/GOVERN/GOVERN-1.4.json |
| MAP | MAP-1.1 | Intended purpose, potentially beneficial uses, context-specific laws, norms and ... | NIST_AI_RMF/MAP/MAP-1.1.json |
| MEASURE | MEASURE-2.8 | Risks associated with transparency and accountability are examined and documente... | NIST_AI_RMF/MEASURE/MEASURE-2.8.json |
| MEASURE | MEASURE-2.9 | AI model is explained, validated, and documented, and system output is interpret... | NIST_AI_RMF/MEASURE/MEASURE-2.9.json |
| MAP | MAP-3.4 | Processes for operator and practitioner proficiency with AI system performance a... | NIST_AI_RMF/MAP/MAP-3.4.json |
| GOVERN | GOVERN-1.1 | Legal and regulatory requirements | NIST_AI_RMF/GOVERN/GOVERN-1.1.json |
| GOVERN | GOVERN-1.3 | Risk management processes and procedures | NIST_AI_RMF/GOVERN/GOVERN-1.3.json |
| GOVERN | GOVERN-1.6 | Mechanisms and resources to inventory AI systems | NIST_AI_RMF/GOVERN/GOVERN-1.6.json |
| GOVERN | GOVERN-2.1 | Roles, responsibilities and lines of communication are documented and clear thro... | NIST_AI_RMF/GOVERN/GOVERN-2.1.json |
| GOVERN | GOVERN-2.2 | Risk management training for organizational personnel and partners to perform du... | NIST_AI_RMF/GOVERN/GOVERN-2.2.json |
| GOVERN | GOVERN-3.1 | Decision-making on risk across the lifecycle is informed by a diverse team | NIST_AI_RMF/GOVERN/GOVERN-3.1.json |

### §6.31 D-09.2 — Impact & Risk Assessments

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.31.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |
| GOVERN | GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizi... | NIST_CSF/GOVERN/GV.RM-06.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| GOVERN | GV.RM-01 | Risk management objectives are established and agreed to by organizational stake... | NIST_CSF/GOVERN/GV.RM-01.json |
| IDENTIFY | ID.RA-03 | Internal and external threats to the organization are identified and recorded | NIST_CSF/IDENTIFY/ID.RA-03.json |

#### §6.31.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| IDENTIFY-P | ID.RA-P5 | Risk responses are identified, prioritized, and implemented. | NIST_PF/IDENTIFY-P/ID.RA-P5.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| IDENTIFY-P | ID.RA-P4 | Problematic data actions, likelihoods, and impacts are used to determine and pri... | NIST_PF/IDENTIFY-P/ID.RA-P4.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| IDENTIFY-P | ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropria... | NIST_PF/IDENTIFY-P/ID.DE-P3.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |

#### §6.31.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GOVERN-1.1 | Legal and regulatory requirements | NIST_AI_RMF/GOVERN/GOVERN-1.1.json |
| GOVERN | GOVERN-1.3 | Risk management processes and procedures | NIST_AI_RMF/GOVERN/GOVERN-1.3.json |
| GOVERN | GOVERN-1.5 | Ongoing monitoring and review of risk management | NIST_AI_RMF/GOVERN/GOVERN-1.5.json |
| MAP | MAP-5.1 | Likelihood and magnitude of each identified impact -- based on expected use, pas... | NIST_AI_RMF/MAP/MAP-5.1.json |
| MAP | MAP-3.1 | Potential benefits of intended functionality and performance are examined and do... | NIST_AI_RMF/MAP/MAP-3.1.json |
| MAP | MAP-3.2 | Potential costs, including non-monetary costs, from expected or realized AI erro... | NIST_AI_RMF/MAP/MAP-3.2.json |
| MANAGE | MANAGE-1.2 | Treatment of documented AI risks is prioritized based on impact, likelihood, or ... | NIST_AI_RMF/MANAGE/MANAGE-1.2.json |

### §6.32 D-09.4 — Records of Processing

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.32.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |
| RESPOND | RS.AN-07 | Incident data and metadata are collected, and their integrity and provenance are... | NIST_CSF/RESPOND/RS.AN-07.json |
| RESPOND | RS.CO-02 | Internal and external stakeholders are notified of incidents | NIST_CSF/RESPOND/RS.CO-02.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| DETECT | DE.AE-03 | Information is correlated from multiple sources | NIST_CSF/DETECT/DE.AE-03.json |
| PROTECT | PR.AA-02 | Identities are proofed and bound to credentials based on the context of interact... | NIST_CSF/PROTECT/PR.AA-02.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| RESPOND | RS.AN-06 | Actions performed during an investigation are recorded, and the records' integri... | NIST_CSF/RESPOND/RS.AN-06.json |
| RESPOND | RS.AN-08 | An incident's magnitude is estimated and validated | NIST_CSF/RESPOND/RS.AN-08.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MI-02 | Incidents are eradicated | NIST_CSF/RESPOND/RS.MI-02.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| RECOVER | RC.RP-04 | Critical mission functions and cybersecurity risk management are considered to e... | NIST_CSF/RECOVER/RC.RP-04.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| IDENTIFY | ID.IM-01 | Improvements are identified from evaluations | NIST_CSF/IDENTIFY/ID.IM-01.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |

#### §6.32.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or ev... | NIST_PF/COMMUNICATE-P/CM.AW-P7.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| IDENTIFY-P | ID.IM-P1 | Systems/products/services that process data are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P1.json |
| IDENTIFY-P | ID.IM-P4 | Data actions of the systems/products/services are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P4.json |
| IDENTIFY-P | ID.IM-P6 | Data elements within the data actions are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P6.json |
| IDENTIFY-P | ID.IM-P8 | Data processing is mapped, illustrating the data actions and associated data ele... | NIST_PF/IDENTIFY-P/ID.IM-P8.json |
| CONTROL-P | CT.DM-P9 | Technical measures implemented to manage data processing are tested and assessed... | NIST_PF/CONTROL-P/CT.DM-P9.json |
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.AW-P3 | System/product/service design enables data processing visibility. | NIST_PF/COMMUNICATE-P/CM.AW-P3.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| CONTROL-P | CT.DM-P2 | Data elements can be accessed for transmission or disclosure. | NIST_PF/CONTROL-P/CT.DM-P2.json |
| COMMUNICATE-P | CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organization... | NIST_PF/COMMUNICATE-P/CM.AW-P5.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| IDENTIFY-P | ID.IM-P5 | The purposes for the data actions are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P5.json |

### §6.33 D-10.1 — Continuous Security Monitoring

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.33.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| DETECT | DE.CM-06 | External service provider activities and services are monitored to find potentia... | NIST_CSF/DETECT/DE.CM-06.json |
| DETECT | DE.CM-03 | Personnel activity and technology usage are monitored to find potentially advers... | NIST_CSF/DETECT/DE.CM-03.json |
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| DETECT | DE.AE-08 | Incidents are declared when adverse events meet the defined incident criteria | NIST_CSF/DETECT/DE.AE-08.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |

#### §6.33.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.AC-P5 | Network integrity is protected (e.g., network segregation, network segmentation)... | NIST_PF/PROTECT-P/PR.AC-P5.json |
| GOVERN-P | GV.MT-P5 | Policies, processes, and procedures are established and in place to receive, ana... | NIST_PF/GOVERN-P/GV.MT-P5.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| COMMUNICATE-P | CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or ev... | NIST_PF/COMMUNICATE-P/CM.AW-P7.json |
| IDENTIFY-P | ID.DE-P5 | Data processing ecosystem parties are routinely assessed using audits, test resu... | NIST_PF/IDENTIFY-P/ID.DE-P5.json |
| CONTROL-P | CT.DM-P9 | Technical measures implemented to manage data processing are tested and assessed... | NIST_PF/CONTROL-P/CT.DM-P9.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |

#### §6.33.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MANAGE | MANAGE-4.1 | Post-deployment AI system monitoring plans are implemented | NIST_AI_RMF/MANAGE/MANAGE-4.1.json |
| MEASURE | MEASURE-3.1 | Approaches, personnel, and documentation are in place to regularly identify and ... | NIST_AI_RMF/MEASURE/MEASURE-3.1.json |
| MEASURE | MEASURE-4.1 | Measurement approaches for identifying AI risks are documented and connected to ... | NIST_AI_RMF/MEASURE/MEASURE-4.1.json |
| GOVERN | GOVERN-1.5 | Ongoing monitoring and review of risk management | NIST_AI_RMF/GOVERN/GOVERN-1.5.json |

### §6.34 D-10.2 — Audit Logging & Traceability

_Applicable regulations: GDPR, CRA, AI Act_

#### §6.34.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| DETECT | DE.AE-03 | Information is correlated from multiple sources | NIST_CSF/DETECT/DE.AE-03.json |
| RESPOND | RS.AN-07 | Incident data and metadata are collected, and their integrity and provenance are... | NIST_CSF/RESPOND/RS.AN-07.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| RECOVER | RC.RP-03 | The integrity of backups and other restoration assets is verified before using t... | NIST_CSF/RECOVER/RC.RP-03.json |

#### §6.34.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system deve... | NIST_PF/CONTROL-P/CT.PO-P4.json |
| CONTROL-P | CT.DM-P5 | Data are destroyed according to policy. | NIST_PF/CONTROL-P/CT.DM-P5.json |
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| IDENTIFY-P | ID.IM-P1 | Systems/products/services that process data are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P1.json |
| IDENTIFY-P | ID.IM-P4 | Data actions of the systems/products/services are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P4.json |
| IDENTIFY-P | ID.IM-P6 | Data elements within the data actions are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P6.json |
| IDENTIFY-P | ID.IM-P8 | Data processing is mapped, illustrating the data actions and associated data ele... | NIST_PF/IDENTIFY-P/ID.IM-P8.json |
| CONTROL-P | CT.DM-P9 | Technical measures implemented to manage data processing are tested and assessed... | NIST_PF/CONTROL-P/CT.DM-P9.json |

#### §6.34.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-2.4 | Functionality and behavior of the AI system and its components are monitored whe... | NIST_AI_RMF/MEASURE/MEASURE-2.4.json |
| MEASURE | MEASURE-3.1 | Approaches, personnel, and documentation are in place to regularly identify and ... | NIST_AI_RMF/MEASURE/MEASURE-3.1.json |
| GOVERN | GOVERN-1.6 | Mechanisms and resources to inventory AI systems | NIST_AI_RMF/GOVERN/GOVERN-1.6.json |
| MEASURE | MEASURE-4.2 | Measurement results regarding AI system trustworthiness in deployment context(s)... | NIST_AI_RMF/MEASURE/MEASURE-4.2.json |
| GOVERN | GOVERN-1.4 | Transparent policies, procedures, and other controls for risk management | NIST_AI_RMF/GOVERN/GOVERN-1.4.json |
| GOVERN | GOVERN-2.1 | Roles, responsibilities and lines of communication are documented and clear thro... | NIST_AI_RMF/GOVERN/GOVERN-2.1.json |

### §6.35 D-10.3 — Compliance Testing

_Applicable regulations: GDPR, CRA, NIS 2, AI Act_

#### §6.35.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| IDENTIFY | ID.IM-01 | Improvements are identified from evaluations | NIST_CSF/IDENTIFY/ID.IM-01.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |

#### §6.35.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirem... | NIST_PF/GOVERN-P/GV.MT-P3.json |
| CONTROL-P | CT.DM-P10 | Stakeholder privacy preferences are included in algorithmic design objectives an... | NIST_PF/CONTROL-P/CT.DM-P10.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| IDENTIFY-P | ID.RA-P5 | Risk responses are identified, prioritized, and implemented. | NIST_PF/IDENTIFY-P/ID.RA-P5.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |

#### §6.35.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MEASURE | MEASURE-1.1 | Approaches and metrics for measurement of AI risks are selected for implementati... | NIST_AI_RMF/MEASURE/MEASURE-1.1.json |
| MEASURE | MEASURE-2.1 | Test sets, metrics, and details about the tools used during test, evaluation, va... | NIST_AI_RMF/MEASURE/MEASURE-2.1.json |
| MEASURE | MEASURE-2.3 | AI system performance or assurance criteria are measured qualitatively or quanti... | NIST_AI_RMF/MEASURE/MEASURE-2.3.json |
| MAP | MAP-3.3 | Targeted application scope is specified and documented based on a system's capab... | NIST_AI_RMF/MAP/MAP-3.3.json |

### §6.36 Provenance

- **Source files:** Baseline controls at `baseline/CONTROLS/` (NIST CSF 2.0, NIST PF 1.0, NIST AI RMF) and modular sub-domain corpora at `baseline/domains/D-XX_*/D-XX.Y/`
- **Mapping date:** 2026-09-23
- **Coverage scope:** 35 ACTIVE sub-domains (D-01.1..D-10.3 minus D-07.4, D-08.3, D-09.3 NOT_ADDRESSED).
- **Controls total:** 400 NIST CSF 2.0 + 162 NIST PF 1.0 + 90 NIST AI RMF rows across 35 sub-domains.
- Per-control JSONs: `baseline/CONTROLS/<framework>/<function>/<control_id>.json`
- Per-subdomain corpus: `baseline/domains/D-XX_*/D-XX.Y/` (source-of-truth for control derivation)
- Traceability mappings: `baseline/MAPPINGS/`

---

## §7 Cross-References

- **`Doc01_INTAKE_FORM.md`**: Company context intake form (profile, operational reality, MEDIUM-scale tiers, regulatory applicability).
- **`baseline/00_Taxonomy_Reference.md`**: Sub-domain canonical taxonomy (D-01.1 .. D-10.3).
- **`baseline/01_Ambiguity_Registry.md`**: Ambiguity registry cards informing disambiguation of regulatory clauses.
- **`baseline/domains/`**: Modular per-regulation corpus for Baseline Goals (`SG-D-XX.Y.HL` and per-regulation `regs/<REG>.md`).
- **`baseline/CONTROLS/`**: NIST CSF 2.0, NIST PF 1.1, and NIST AI RMF control referentials.
- **`baseline/MAPPINGS/`**: Traceability chain and SR control mapping store.
- **Strategic Tensions**: 4 tensions (T-001..T-004) resolved with max-SLA routing in §4.

---

## §8 Validation

- **35 ACTIVE sub-domains** mapped to Adjusted Goals in §3.
- Distinct AG IDs used in main tables: **29 slot 001 (GDPR) + 34 slot 002 (CRA) + 22 slot 003 (NIS 2) + 15 slot 004 (AI Act) = 100 rows**.
- **§2 / §3 / §4 / §5 are technology-free** — no vendor, product, or tool named (verified by blocklist scan and by inspection).
- **Baseline Goal wording inherited from the corpus unchanged.** Any technology tokens in that wording come from the frozen Phase 0 Baseline Goal prose and are retained as inherited corpus wording (ADR-004 D2). Technology-neutrality applies to the Adjusted Goals layer (§3), not to the inherited Baseline Goal wording.
- **Track B decision table: 38 rows** in §5 (35 ACTIVE + D-07.4 + D-08.3 + D-09.3 documented NOT_ADDRESSED).
- **Distribution (35 tiered rows): 8 RIGOROUS + 27 STANDARD = 35.** No INHERITABLE rows exist (every applicable regulation binds the company directly); DEFERRED is unavailable (security staffing > 1 FTE).
- **4 tensions resolved** with max-SLA routing in §4 (T-001..T-004).
- Floor rule preserved: every MUST ≥ STANDARD per the proportionality model floor (no row below the floor; RIGOROUS overrides documented).

---

## §9 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-09-23 | aegis-mvp executor | Initial Case_02 release — 100 adjusted goals across 35 active sub-domains (GDPR/CRA/NIS 2/AI Act), 4 tensions resolved, 38-row Track B decision trail, NIST CSF 2.0 / PF 1.0 / AI RMF controls mapping. |

---

## §10 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | aegis-mvp executor | | 2026-09-23 |
| Business Review (CEO) | | | |
| Technical Review (CTO) | | | |
| AEGIS Methodology Review | | | |

**Next documents that consume this profile:**
- Phase 2 `Doc01_Operational_Objectives.md` (objectives consume the adjusted goals in §3)
- Phase 3 functional specification (architecture consumes the tier from §5)

---

