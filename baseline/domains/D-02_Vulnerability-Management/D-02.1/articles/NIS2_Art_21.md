---
document_id: AEGIS-PREPROC-NIS2-ART-21
title: NIS2 Art. 21 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 21
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# NIS2 Art. 21

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-001 | Policies and procedures are established for the use of cryptography and, where appropriate, encryption, covering confidentiality, integrity, and authenticity of data stored, transmitted, and processed by network and information systems. | `NIS2-CL17` (Art. 21(2)(h)); `NIS2-CL08` (Art. 21(1) state-of-the-art); `NIS2-CL07` (Art. 21(1) appropriate/proportionate) | D-01.1 |
| SO-NIS2-001 | D-01.1 | Art. 21(2)(h) | Cryptography policies and procedures; encryption where appropriate |
| SO-NIS2-002 | Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle. | `NIS2-CL14` (Art. 21(2)(e) — security in acquisition/development/maintenance + vuln handling + disclosure); `NIS2-CL20` (Art. 21(3) sentence 1 — supplier vulnerability assessment) | D-02.1, D-02.3 |
| SO-NIS2-002 | D-02.1, D-02.3 | Art. 21(2)(e) | Vulnerability handling and disclosure in system lifecycle |
| SO-NIS2-003 | Access control policies are established and applied, covering human resources security and asset management, ensuring that access to network and information systems is limited to authorised users, services, and hardware on a least-privilege basis. | `NIS2-CL18` (Art. 21(2)(i) — HR security + AC + AM); `NIS2-CL07` (Art. 21(1) appropriate/proportionate — propagates) | D-03.1, D-03.2, D-03.3, D-03.4 |
| SO-NIS2-003 | D-03.1, D-03.2, D-03.3, D-03.4 | Art. 21(2)(i) | Access control policies + HR security + asset management |
| SO-NIS2-004 | Multi-factor authentication or continuous authentication solutions are used where appropriate, and secured voice, video, and text communications as well as secured emergency communication systems are deployed within the entity. | `NIS2-CL19` (Art. 21(2)(j) — MFA or continuous + secured comms + secured emergency + `where appropriate`) | D-03.2, D-01.2 (partial) |
| SO-NIS2-004 | D-03.2, D-01.2 (partial) | Art. 21(2)(j) | MFA or continuous auth + secured comms + secured emergency |
| SO-NIS2-005 | An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents, including those with significant impact on the provision of services. | `NIS2-CL11` (Art. 21(2)(b) — incident handling); `NIS2-CL26` (Art. 23(1) ¶1 — significant-incident notification core); `NIS2-CL09` (Art. 21(2) chapeau — all-hazards approach); `NIS2-CL12` (Art. 21(2)(c) — BC/DR/CM, for the recovery dimension) | D-04.1, D-04.2, D-04.4 |
| SO-NIS2-005 | D-04.1, D-04.2, D-04.4 | Art. 21(2)(b) | Incident handling capability (prevent, detect, analyse, contain, respond, recover) |
| SO-NIS2-013 | Business continuity, backup management, disaster recovery, and crisis management capabilities are maintained, ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents. | `NIS2-CL12` (Art. 21(2)(c) — BC + backup + DR + CM) | D-04.4, D-09.4 |
| SO-NIS2-013 | D-04.4, D-09.4 | Art. 21(2)(c) | BC, backup, DR, crisis management |
| SO-NIS2-014 | Supply chain security is managed across direct supplier and service-provider relationships, including security-related aspects of those relationships. | `NIS2-CL13` (Art. 21(2)(d) — supply chain security + `direct` scope-limiter); `NIS2-CL07` (Art. 21(1) appropriate/proportionate — propagates) | D-06.1, D-06.3 |
| SO-NIS2-014 | D-06.1, D-06.3 | Art. 21(2)(d) | Supply chain security with direct suppliers and service providers |
| SO-NIS2-015 | Supplier-specific vulnerabilities, overall quality of products and cybersecurity practices, and supplier secure-development procedures are assessed for each direct supplier and service provider. | `NIS2-CL20` (Art. 21(3) sentence 1 — supplier assessment three-prong: vulnerabilities + quality + secure-development procedures); `NIS2-CL13` (Art. 21(2)(d) — `direct` scope-limiter) | D-06.3, D-02.1 |
| SO-NIS2-015 | D-06.3, D-02.1 | Art. 21(3) sentence 1 | Supplier-specific vulnerabilities + product/service quality + supplier SD procedures |
| SO-NIS2-016 | The results of EU-level coordinated security risk assessments of critical supply chains (Cooperation Group + Commission + ENISA under Art. 22(1)) are taken into account in supplier-risk decisions. | `NIS2-CL21` (Art. 21(3) sentence 2 — entity `take into account` Art. 22 results); `NIS2-CL23` (Art. 22(1) — Cooperation Group coordinated assessments); `NIS2-CL24` (Art. 22(1) — technical and, where relevant, non-technical risk factors); `NIS2-CL25` (Art. 22(2) — Commission selection) | D-06.3, D-09.2 |
| SO-NIS2-016 | D-06.3, D-09.2 | Art. 21(3) sentence 2 + Art. 22(1) | Take into account EU-level coordinated supply-chain risk assessments |
| SO-NIS2-017 | Security is integrated into the acquisition, development, and maintenance of network and information systems, including vulnerability handling and disclosure across the system lifecycle. | `NIS2-CL14` (Art. 21(2)(e) — security in acquisition + development + maintenance + vuln handling + disclosure) | D-07.1, D-07.3, D-02.1 |
| SO-NIS2-017 | D-07.1, D-07.3, D-02.1 | Art. 21(2)(e) | Security in acquisition, development, maintenance of NIS |
| SO-NIS2-018 | Basic cyber hygiene practices are established, covering all users of network and information systems with access to entity systems and services. | `NIS2-CL16` (Art. 21(2)(g) — basic cyber hygiene practices); `NIS2-CL07` (Art. 21(1) appropriate/proportionate — propagates) | D-08.1, D-08.2 |
| SO-NIS2-018 | D-08.1, D-08.2 | Art. 21(2)(g) | Basic cyber hygiene practices |
| SO-NIS2-021 | The management body of essential and important entities approves the cybersecurity risk-management measures taken to comply with Art. 21, oversees their implementation, and can be held liable for infringements of that Article by the entity. | `NIS2-CL01` (Art. 20(1) sentence 1 — approve + oversee + held liable); `NIS2-CL02` (Art. 20(1) sentence 2 — public-institution carve-out); `NIS2-CL06` (Art. 20 chapeau — proportionality hook via Art. 3 classification) | D-09.1, D-09.3 |
| SO-NIS2-021 | D-09.1, D-09.3 | Art. 20(1) | Management body approves + oversees + bears liability for Art. 21 measures |
| SO-NIS2-022 | Policies on risk analysis and information system security are established and maintained, documenting the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems. | `NIS2-CL10` (Art. 21(2)(a) — policies on risk analysis + IS security) | D-09.1, D-09.2 |
| SO-NIS2-022 | D-09.1, D-09.2 | Art. 21(2)(a) | Policies on risk analysis + information system security |
| SO-NIS2-023 | Policies and procedures are established to assess the effectiveness of cybersecurity risk-management measures, with results feeding back into the risk-management cycle. | `NIS2-CL15` (Art. 21(2)(f) — policies and procedures to assess effectiveness); `NIS2-CL08` (Art. 21(1) — state-of-the-art baseline) | D-09.1, D-09.3, D-10.3 |
| SO-NIS2-023 | D-09.1, D-09.3, D-10.3 | Art. 21(2)(f) | Policies and procedures to assess effectiveness of risk-management measures |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-001
  title: "Documented cryptography and encryption governance baseline"
  source_clauses:
    - { clause_id: NIS2-CL17, article_ref: "Art. 21(2)(h) — cryptography and, where appropriate, encryption" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art + standards + cost" }
    - { clause_id: NIS2-D01, article_ref: "Art. 6(1) — network and information system (cross)" }
    - { clause_id: NIS2-D02, article_ref: "Art. 6(2) — security of network and information systems" }
  linked_objectives: [SO-NIS2-001]
  sub_domain: [D-01.1]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption. The opening qualifier of Article 21(1) — that the technical, operational and organisational measures taken must be appropriate and proportionate to the risks posed — propagates to this sub-point, and Article 21(1) sentence 2 anchors the baseline against the state of the art, relevant European and international standards, and the cost of implementation (OJ L 333, 27.12.2022, p. 127). The four CIA-A dimensions of Article 6(2) — availability, authenticity, integrity and confidentiality of stored, transmitted or processed data — define what cryptography is to protect. Article 6(1) provides the operational scope by defining network and information systems through three coordinated sub-clauses (electronic communications networks; interconnected devices; digital data stored, processed, retrieved or transmitted). The Directive deliberately fuses cryptography as a discipline (algorithm selection, key management, protocol design) with encryption as a sub-technique applied where the risk assessment demands it, and leaves the application thresholds to the entity under the appropriate-and-proportionate qualifier (Recital 56). For the software-compliance track this means a documented cryptography policy that maps algorithms to data classifications and references the European standards landscape (ETSI TS 103 744 series on quantum-safe migration, ISO/IEC 27001:2022 Annex A.10 Cryptographic controls).
  security_rationale: |
    The obligation in Article 21(2)(h) of Directive (EU) 2022/2555 to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)**, **PR.DS-02 (Data-in-transit protected)** and **GV.RM-04 (Strategic direction on identifying and responding to risks established and communicated)**. PR.DS-01 anchors the cryptographic protection of stored data — algorithm selection, key-management lifecycle (generation, distribution, storage, rotation, revocation, destruction), and decommissioning of deprecated primitives on a known schedule. PR.DS-02 extends the same discipline to data in motion, translating cryptographic policy into mutually-authenticated transport between services, between entity and recipient, and between the entity and the supervisory authority during incident reporting. GV.RM-04 supplies the governance superstructure that converts ad-hoc algorithm choice into a position the entity can defend at audit. Together the three subcategories generate the policy artefacts, key-management records and review-cadence evidence that the Article 21(1) risk-management framework requires an entity to assemble to demonstrate, ex post, that its cryptographic posture is appropriate, proportionate and state-of-the-art.
  ambiguity_notes: |
    Article 21(2)(h) carries two compounding S3 ambiguities that drive materially different compliance obligations. First, the `cryptography and, where appropriate, encryption` conjunction is a hierarchical AND-with-hedge: cryptography is always required (a policy must address cryptographic mechanisms as a discipline) but encryption is additionally required only where the entity's risk assessment indicates it; the alternative reading that cryptography and encryption are synonyms is rejected by the literal text and by the CRA parallel (CRA Art. 13(2) on default passwords, Art. 14(2) on vulnerability remediation, treat cryptography and encryption as distinct concepts). Second, `state of the art` in Article 21(1) sentence 2 admits three readings — current best practice (qualitative), published standards (e.g. ISO/IEC 27001:2022, NIST CSF 2.0), or cutting-edge frontier research — of which the third is rejected by Recital 56 (cost of implementation implies off-the-shelf); the chosen reading accepts both R1 best practice and R2 published standards as operative, with ENISA's 2022 baseline guidance as the practical floor. Member State transposition divergence may apply on `state of the art`: the German BSI standardises the term through BSI TR-02102; French ANSSI requires an independent assessment by a qualified body; Italian ACN publishes annual guidance. The substantive software-compliance consequence is that a 5-FTE SaaS entity and a 500-FTE operator may both satisfy Article 21(2)(h) with materially different documentation depth, provided each documents the proportionality decision. Remain open: (a) whether the European Commission implementing acts under Article 21(5) will specify a baseline cryptography standard or only methodological requirements (the 17 October 2024 deadline has slipped to mid-2025 without publication as of the current reference date); (b) whether Member State national transposition will impose sector-specific cryptography mandates beyond the Directive... (line truncated to 2000 chars)
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-002
  title: "Vulnerability handling and external disclosure lifecycle"
  source_clauses:
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in acquisition/development/maintenance + vuln handling + disclosure" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-002]
  sub_domain: [D-02.1, D-02.3]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities identified, validated, and recorded" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits, test results, or other forms of evaluation" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(e) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure. The clause has two coordinated limbs: security-in-lifecycle (acquisition, development and maintenance) is the process dimension, and vulnerability handling and disclosure is the substantive vulnerability-management dimension. The Article 21(1) appropriate-and-proportionate qualifier propagates. The institutional anchor for the external disclosure pathway is Article 12(1), which designates a CSIRT as coordinator for coordinated vulnerability disclosure at the Member-State level, but the entity-side obligation to operate the pathway is direct under Article 21(2)(e).
  security_rationale: |
    The obligation in Article 21(2)(e) of Directive (EU) 2022/2555 regarding vulnerability handling and disclosure is operationalised in NIST CSF 2.0 through **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**. ID.RA-01 supplies the internal handling substrate — the entity ingests vulnerability signals from internal scanning, vendor advisories, threat-intelligence feeds and coordinated-disclosure submissions, validates each finding against the actual asset population, and records severity, scope and remediation status in a system that survives the audit window. GV.SC-04 closes the supplier loop by ensuring the same intake-triage-remediation-verification cycle operates over third-party advisories and externally-discovered findings, so that disclosure submissions from researchers, CSIRTs or other entities enter a controlled channel rather than a shared inbox. The two subcategories together satisfy the process dimension (handling) and the external-coordination dimension (disclosure) of the Article 21(2)(e) obligation, and produce the intake records, triage decisions and remediation timestamps that constitute the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Vulnerability handling` admits a process/team/programme triad; the chosen reading is process, on which the Article 6(8) `incident handling` parallel supports a process-only interpretation (OJ L 333, 27.12.2022, p. 113). `Handling and disclosure` is read as two distinct activities rather than one composite — the entity maintains an internal handling process AND an external disclosure pathway. T3-vs-text gap awareness (synthesis §8): T3 imports CI/CD pipeline vocabulary not present in the OJ text. Member State transposition divergence may apply on the disclosure pathway (some MS impose a national CSIRT-only channel; others accept direct researcher disclosure). Remain open: whether the Article 12(1) CSIRT-coordinator architecture will be supplemented by Commission guidelines on coordinated vulnerability disclosure under the NIS2 implementing-acts mandate.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-003
  title: "Identity and access-control policy foundation"
  source_clauses:
    - { clause_id: NIS2-CL18, article_ref: "Art. 21(2)(i) — HR security + access control + asset management" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-003]
  sub_domain: [D-03.1, D-03.3]
  nist_csf_mapping:
    - { id: PR.AA-01, title: "Identities and credentials managed by the organization" }
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(i) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding human resources security, access control policies and asset management, coordinated by the conjunction AND. The Article 21(1) appropriate-and-proportionate qualifier propagates to all three sub-domains. Article 6(2) defines the security-of-network-and-information-systems concept against the four CIA-A dimensions — availability, authenticity, integrity and confidentiality — which anchors the access-control objective. The literal text coordinates three independent security disciplines in a single sub-point: ISO 27001:2022 Annex A.6 (people controls) for HR security, Annex A.5.15 (access control) and A.8.2 (privileged access rights) for access-control policy, and Annex A.5.9 (inventory of information and other associated assets) for asset management. The chosen reading is that all three domains are required in cumulative form; the alternative reading that one suffices (pick-one) is rejected by the literal AND conjunction. The access-control-policy reference is model-agnostic — the OJ does not impose RBAC, ABAC, MAC or DAC — so the policy can be implemented under any model that satisfies least-privilege (NIST SP 800-162 on ABAC; ISO 27001:2022 A.5.15). The T3-vs-text gap awareness: T3 imports RBAC + need-to-know + least-privilege vocabulary not in the OJ; the SR preserves model-agnostic OJ language.
  security_rationale: |
    The obligation in Article 21(2)(i) of Directive (EU) 2022/2555 to take measures regarding access-control policies is operationalised in NIST CSF 2.0 through **PR.AA-01 (Identities and credentials for authorized users, services, and hardware are managed by the organization)** and **PR.AA-05 (Access permissions, entitlements, and authorizations are defined and managed in accordance with the principle of least privilege)**. PR.AA-01 establishes the identity substrate — every authorised principal (workforce member, contractor, service account, machine identity) has a managed credential, an accountable owner, and a defined lifecycle. PR.AA-05 then constrains what that identity may do, translating the policy's least-privilege principle into entitlements that are created, reviewed and revoked on a defined cadence. The two subcategories are mutually reinforcing: a permission model without managed identities cannot be enforced, and a managed identity without a least-privilege policy cannot constrain damage from credential compromise. Together they provide the identity-governance evidence base — joiner/mover/leaver records, privilege reviews, role definitions — on which the entity demonstrates, ex post under Article 21(1), that its access-control posture satisfies the appropriate-and-proportionate qualifier.
  ambiguity_notes: |
    The Article 21(2)(i) three-domain AND carries an S3 coordination ambiguity: the literal AND requires all three domains; partial-compliance readings (two-of-three) are rejected by the literal text. The model-agnostic reading of `access control policies` is the chosen interpretation; alternatives are RBAC (ISO 27001:2022 A.5.15 anchor), ABAC (NIST SP 800-162), MAC, and DAC — each of which is operative at the implementation layer but does not constrain the policy. `Human resources security` admits four readings (staff-security, HR-driven, workforce-security, lifecycle-security) of which the chosen reading is lifecycle-security (joiner-mover-leaver) per ISO 27001:2022 A.6 anchor. `Asset management` admits hardware-only, software-only, information-only, and cumulative readings — the chosen reading is cumulative (R4) per Recital 56 proportionality. Member State transposition divergence may apply on national HR-practice compatibility (e.g. French CNIL guidance on employee monitoring; German BfDI on personnel-data proportionality for security logging). Remain open: (a) whether national supervisory authorities will publish binding minimum specifications for access-control models in critical sectors (e.g. energy, transport) under Article 4 implementing acts; (b) whether the cumulative asset-management reading requires separate inventories for ICT hardware, software and information assets, or whether a unified register with classification attributes suffices — the Directive is silent on the register structure.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-004
  title: "Workforce identity lifecycle as HR-security substrate"
  source_clauses:
    - { clause_id: NIS2-CL18, article_ref: "Art. 21(2)(i) — HR security dimension" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-003]
  sub_domain: [D-08.2, D-03.1]
  nist_csf_mapping:
    - { id: PR.AT-02, title: "Workforce understands role-specific security responsibilities" }
    - { id: PR.AA-01, title: "Identities and credentials managed by the organization" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(i) `human resources security` is one of three coordinated sub-domains of the same sub-point (the others being access control policies and asset management, captured in SR-NIS2-003 and SR-NIS2-005). The OJ enjoins entities to manage HR security in coordination with access control and asset management; the cumulative reading is the literal AND. The HR-security dimension covers the workforce identity lifecycle — joiners (vetting, baseline access provisioning, induction), movers (role-change access review), and leavers (access revocation, return of assets, exit interview security clearance) — together with role-based access transitions on role change (ISO 27001:2022 A.6.1–A.6.5 people controls). The Article 21(1) appropriate-and-proportionate qualifier propagates.
  security_rationale: |
    The HR-security dimension of Article 21(2)(i) of Directive (EU) 2022/2555 is operationalised in NIST CSF 2.0 through **PR.AT-02 (All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives)** and **PR.AA-01 (Identities and credentials for authorized users, services, and hardware are managed by the organization)**. PR.AT-02 binds the HR-security lifecycle to the workforce: joiners receive role-specific cybersecurity induction, movers have their role-transition re-trained, and leavers complete the off-boarding security clearance. PR.AA-01 supplies the identity-lifecycle substrate the HR process executes against — provisioning on induction, entitlement review on role change, revocation and return-of-assets on separation. The two subcategories together address the moving parts of the workforce identity flow that the access-control policy and the awareness programme reference as their operational input. Together they generate the lifecycle evidence (induction records, role-change tickets, separation sign-offs) that satisfies the Article 21(1) accountability threshold by demonstrating that the entity can answer, for any current or former principal, when their access was granted, reviewed and revoked.
  ambiguity_notes: |
    `Human resources security` admits four readings (staff-security, HR-driven, workforce-security, lifecycle-security); the chosen reading is lifecycle-security (R4) per the ISO 27001:2022 A.6 anchor and the dominant transposition practice. The alternative workforce-security reading (R3) is rejected because it underweights the joiner-mover-leaver mechanics. Member State transposition divergence may apply on national HR-practice compatibility: French CNIL guidance on employee monitoring requires explicit proportionality assessments for HR-driven security logging; German BfDI on personnel-data proportionality imposes stricter controls on behavioural analytics than the Directive requires. Remain open: whether the Commission implementing acts under Article 21(5) will specify a minimum set of HR-security controls (vetting, induction, separation) or leave the operationalisation entirely to the entity.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-005
  title: "Authoritative hardware, software, and information-asset inventories"
  source_clauses:
    - { clause_id: NIS2-CL18, article_ref: "Art. 21(2)(i) — asset management dimension" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-003]
  sub_domain: [D-09.3, D-03.3]
  nist_csf_mapping:
    - { id: ID.AM-01, title: "Inventories of hardware managed by the organization are maintained" }
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(i) `asset management` is the third coordinated sub-domain of Article 21(2)(i) (the others being HR security and access control policies). The OJ enjoins entities to manage the assets that are subject to access-control policies. The asset-management dimension establishes the inventory that downstream access-control decisions reference — hardware inventory (devices, network equipment, IoT), software inventory (applications, services, libraries), and information-asset inventory (datasets, configurations, credentials) per ISO 27001:2022 A.5.9 inventory of information and other associated assets. The Article 21(1) appropriate-and-proportionate qualifier propagates.
  security_rationale: |
    The asset-management dimension of Article 21(2)(i) of Directive (EU) 2022/2555 is operationalised in NIST CSF 2.0 through **ID.AM-01 (Inventories of hardware managed by the organization are maintained)** and **ID.AM-02 (Inventories of software, services, and systems managed by the organization are maintained)**. ID.AM-01 establishes the hardware-side inventory — endpoints, network equipment, IoT devices, industrial-control components — each item recorded with owner, location, classification and lifecycle status. ID.AM-02 mirrors the discipline on the software side — applications, services, libraries, firmware, cloud workloads — each entry linking to its supply-chain provenance and to the access-control decisions that depend on it. Both inventories are living artefacts: a register that records an acquisition but not its decommission creates a false sense of coverage that audit will surface. The two subcategories together constitute the asset register against which vulnerability scanning, patch management, supply-chain assessment and incident-response capabilities target their actions, and which the Article 21(1) appropriate-and-proportionate analysis presupposes as the precondition for any technical-control decision.
  ambiguity_notes: |
    `Asset management` admits four readings (hardware-only, software-only, information-only, cumulative); the chosen reading is cumulative (R4) per the literal AND of three coordinated sub-domains in Article 21(2)(i). The T3-vs-text gap awareness: T3 reads D-09.3 asset inventories from Article 21(2)(i); the OJ `asset management` is one of three coordinated sub-domains in a single sub-point, not a standalone D-09.3 mandate. Member State transposition divergence may apply on the granularity of asset inventories — French ANSSI requires classified inventories (sensitive, basic) for entities in essential sectors; German BSI recommends a single authoritative register with classification attributes. Remain open: whether the Commission's Article 21(5) implementing acts will specify minimum asset-classification categories or rely on entity-defined taxonomies (the directive is silent on classification granularity).
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-006
  title: "Strong authentication through MFA or continuous alternatives"
  source_clauses:
    - { clause_id: NIS2-CL19, article_ref: "Art. 21(2)(j) — MFA or continuous authentication solutions, `where appropriate`" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-004]
  sub_domain: [D-03.2]
  nist_csf_mapping:
    - { id: PR.AA-03, title: "Users, services, and hardware authenticated" }
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(j) of Directive (EU) 2022/2555, in its first clause, requires essential and important entities to use multi-factor authentication or continuous authentication solutions, where appropriate. The OR admits both MFA and continuous-authentication as alternative authentication paradigms — they are not redundant — and the `where appropriate` hedge closes the sub-point. The Article 21(1) factors (state of the art, relevant European and international standards, cost of implementation, degree of exposure, entity size, likelihood and severity) propagate and operationalise the appropriateness test. Article 6(2) anchors the authentication objective against the four CIA-A dimensions. The CRA parallel is instructive: CRA Article 13(2) on default passwords and Article 14 on vulnerability remediation treat strong authentication as the default for products with digital elements; NIS2 mirrors this posture at the entity level. ENISA's 2022 baseline security recommendations list MFA as a default for all administrative and privileged access.
  security_rationale: |
    The Article 21(2)(j) first-clause obligation to use multi-factor authentication or continuous authentication solutions, where appropriate, is operationalised in NIST CSF 2.0 through **PR.AA-03 (Users, services, and hardware are authenticated)** and **PR.AA-05 (Access permissions, entitlements, and authorizations are defined and managed in accordance with the principle of least privilege)**. PR.AA-03 specifies the authentication event itself: at session establishment the principal must present evidence bound to multiple factors, with factor strength calibrated to the sensitivity of the resource accessed and the entity's risk assessment; where continuous authentication is the chosen paradigm, PR.AA-03 also requires that session-risk signals (behaviour, device posture, geo-velocity) feed a re-validation decision that can step the session up or down. PR.AA-05 then constrains the post-authentication surface — even an authenticated principal receives only the entitlements the least-privilege analysis has identified, with administrative and privileged access held to the smallest population. The two subcategories together address the two distinct failure modes (credential compromise and entitlement over-provisioning) and produce the authentication-strength records and entitlement-review evidence on which the entity demonstrates, ex post under Article 21(1), that its authentication posture is appropriate to the risks.
  ambiguity_notes: |
    `Where appropriate` is an S3 hedge; the chosen reading is risk-based (R3) per Article 21(1) factors. Alternative readings — system-based (R1), user-based (R2), cost-based (R4) — are rejected because they subordinate the appropriateness test to operational criteria rather than to the risk-assessment output the Directive requires. `Multi-factor authentication` is an S2 polysemy with at least five readings (SMS-OTP, TOTP authenticator apps, hardware tokens like FIDO2/YubiKey, platform-authenticated passkeys, mechanism-agnostic); the chosen reading is mechanism-agnostic (R5) per the literal OJ text, with the FIDO2 / WebAuthn posture as the dominant industry-state-of-the-art. The SMS-OTP reading (R1) is rejected for new deployments given the SS7 / SIM-swap attack surface documented by ENISA and NIST SP 800-63B §5.1.5.2. Member State transposition divergence may apply; national authorities may specify acceptable mechanisms (e.g. ANSSI's authentication-factor catalogue in France, BSI's TR-02102 in Germany). Remain open: (a) whether the Commission's Article 21(5) implementing acts will specify a minimum authentication-factor strength (e.g. prohibit SMS-OTP for administrative access in essential entities) or leave the mechanism choice to the entity; (b) whether continuous authentication will be classified by national authorities as equivalent to MFA for compliance purposes — the Directive treats them as alternative paradigms but does not equate them.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-007
  title: "Secured internal and emergency communications channels"
  source_clauses:
    - { clause_id: NIS2-CL19, article_ref: "Art. 21(2)(j) — secured voice, video, text communications + secured emergency communication systems" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-004]
  sub_domain: [D-03.2, D-01.2]
  nist_csf_mapping:
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: PR.IR-03, title: "Mechanisms to achieve resilience requirements in normal and adverse situations" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(j) of Directive (EU) 2022/2555, in its second and third clauses, requires essential and important entities to deploy secured voice, video and text communications and secured emergency communication systems within the entity, where appropriate. The `where appropriate` hedge from the closing of the sub-point applies. The two channels are distinct from the data-in-transit mandate in SR-NIS2-001 (which is the cryptographic-policy obligation under Article 21(2)(h)): the secured voice/video/text concern internal communications channels used by staff, while secured emergency communication systems concern the channels maintained for crisis coordination under the Article 21(2)(c) crisis-management hook. The Article 21(1) factors propagate. T3-vs-text gap awareness: T3 imports audit-logging vocabulary not in the OJ text; the SR preserves the literal `secured communications` language.
  security_rationale: |
    The Article 21(2)(j) second-and-third-clause obligation regarding secured voice, video and text communications and secured emergency communication systems is operationalised in NIST CSF 2.0 through **PR.DS-02 (Data-in-transit protected)** and **PR.IR-03 (Mechanisms are put in place to achieve resilience requirements in normal and adverse situations)**. PR.DS-02 establishes the channel-protection substrate — voice, video and text traffic between staff, between staff and incident-response coordinators, and between the entity and external responders must travel on mutually-authenticated channels whose confidentiality and integrity are protected by approved cryptographic mechanisms. PR.IR-03 then ensures the channels survive the incident itself: alternative routing, infrastructure independence and degraded-mode operation so that the coordination capability does not collapse at the moment the crisis is most acute. The two subcategories together address the two failure modes the secured-communications obligation targets — interception of operational traffic in normal conditions and collapse of the coordination apparatus in adverse conditions. The resulting channel-design evidence, tested under both steady-state and crisis conditions, supplies the accountability artefact the Article 21(1) framework requires.
  ambiguity_notes: |
    `Secured` is an S2 polysemy with at least five readings (encrypted, authenticated, access-controlled, all, any); the chosen reading is mechanism-agnostic (R5) per the literal OJ text, with encryption (R1) as the dominant industry posture and ENISA's 2022 baseline treating end-to-end encryption as the default for internal voice and text. Member State transposition divergence may apply on the minimum security posture for emergency-communication systems — some Member States require dedicated infrastructure independent of commercial telecom providers (per the CER Article 12 model). Remain open: whether the Commission's Article 21(5) implementing acts will specify minimum-security baselines for secured emergency communication systems, including any redundancy requirements (the Directive is silent on infrastructure-isolation requirements).
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-008
  title: "Incident handling as a six-action lifecycle"
  source_clauses:
    - { clause_id: NIS2-CL11, article_ref: "Art. 21(2)(b) — incident handling" }
    - { clause_id: NIS2-D06, article_ref: "Art. 6(8) — incident handling definition (6-action list: prevent, detect, analyse, contain, respond, recover)" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-005, SO-NIS2-013]
  sub_domain: [D-04.1, D-04.2, D-04.4]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "Incident management plan executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.AN-03, title: "Analysis performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident (OJ L 333, 27.12.2022, p. 113) — a six-action process anchored in the Article 21(2) all-hazards approach (Article 21(2) chapeau) and the Article 6(2) CIA-A security-of-NIS definition. The Article 21(1) appropriate-and-proportionate qualifier propagates. The incident-handling capability is the operational substrate of the Article 23 reporting flow (SR-NIS2-010 to SR-NIS2-018) and the Article 21(2)(c) business-continuity hook (SR-NIS2-019). The 24-hour early-warning clock of Article 23(4)(a) starts upon the entity becoming aware of the significant incident; the entity's incident-handling capability is the apparatus that produces the awareness event in a defensible manner.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — Art. 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident; the six actions are listed as gerunds conjunctively coordinated, not as four verbs + OR.]
  security_rationale: |
    The Article 21(2)(b) incident-handling obligation, anchored by the Article 6(8) six-action definition (prevent, detect, analyse, contain, respond, recover), is operationalised in NIST CSF 2.0 through **RS.MA-01 (The incident management plan is executed in coordination with relevant third parties once an incident is declared)** and **RS.AN-03 (Analysis is performed to determine what has occurred during an event and the root cause of the event)**. RS.MA-01 operationalises the coordination dimension — the entity's plan must specify, for each phase of the lifecycle, who executes, who is informed, and how the entity coordinates with the CSIRT, competent authority, single point of contact and any sectoral peers, preventing the plan from collapsing into a unilateral internal exercise. RS.AN-03 operationalises the analysis dimension: root-cause work, scope assessment and indicator-of-compromise extraction produce the evidence base on which both technical containment and the subsequent 24h/72h/1m regulatory reporting flows (SR-NIS2-010, SR-NIS2-011, SR-NIS2-012) depend. Together the two subcategories cover the two distinct cognitive demands of incident handling — coordination under uncertainty and analysis under time pressure — and generate the incident records, triage decisions and post-incident artefacts that constitute the Article 21(1) accountability evidence.
  ambiguity_notes: |
    `Incident handling` admits process/team/capability/programme readings; the chosen reading is process (R1) per the Article 6(8) `actions and procedures` anchor. The `aiming at, where appropriate` qualifier is read as illustrative (the six actions form a floor; the entity may add more — e.g. eradication, post-incident activity) rather than exhaustive. T3-vs-text gap awareness: T3 imports NIST SP 800-61 vocabulary not in the OJ text; the SR preserves the OJ six-action language. The handling capability is operationally triggered (process executed on incident declaration) and continuous (the capability is maintained). Member State transposition divergence may apply on incident-handling scope (whether the capability must operate 24/7; whether it must be staffed by named CSIRT-equivalent personnel or by a function that may include outsourced MSSPs); the Article 21(1) appropriate-and-proportionate qualifier is the basis for national variation. Remain open: whether the Commission's Article 21(5) implementing acts will specify a minimum 24/7 availability requirement for the incident-handling capability of essential entities in critical sectors (energy, transport, health, finance) — the Directive is silent on staffing continuity.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-009
  title: "All-hazards monitoring to surface adverse events"
  source_clauses:
    - { clause_id: NIS2-CL11, article_ref: "Art. 21(2)(b) — incident handling (detection dimension)" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL09, article_ref: "Art. 21(2) chapeau — all-hazards approach" }
  linked_objectives: [SO-NIS2-005]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services monitored to find potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(b) of Directive (EU) 2022/2555 requires incident-handling measures, and the Article 6(8) definition includes `detecting` as one of the six actions; this is the detection dimension of incident handling. The Article 21(2) chapeau introduces the all-hazards approach, which requires the detection capability to cover cybersecurity, operational, and physical-environment hazards affecting network and information systems (Recital 56). The Article 21(1) appropriate-and-proportionate qualifier propagates. For the software-compliance track the cybersecurity and operational dimensions are in scope; the physical-environment dimension is captured by SR-NIS2-041 (out-of-scope flag for software-compliance).
  security_rationale: |
    The detection dimension of the Article 21(2)(b) incident-handling obligation, read against the Article 21(2) chapeau all-hazards approach, is operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks and network services are monitored to find potentially adverse events)** and **DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events)**. DE.CM-01 supplies the network-side detection substrate — traffic baselines, flow analytics, north-south and east-west monitoring, and external-service-provider activity feeds — producing the events on which the awareness of a significant incident (the Article 23(4)(a) 24-hour clock trigger) is built. DE.CM-09 mirrors the discipline at the host, runtime and data tier: endpoint telemetry, process-level behavioural signals and runtime-environment integrity monitoring extend detection into the layers that network monitoring cannot reach. The two subcategories together address the two failure modes the all-hazards detection obligation targets — events that propagate at the network layer and events that manifest only at the host, application or data tier. The resulting detection-coverage evidence and alert-quality records are the artefacts on which the entity demonstrates, ex post under Article 21(1), that its detection capability is appropriate to the risks.
  ambiguity_notes: |
    The all-hazards approach admits three readings (cybersecurity-only, including natural disasters, including physical security); the chosen reading is R3 (the chapeau explicitly extends to the physical environment of network and information systems). For the software-compliance track only the cybersecurity and operational dimensions are in scope; the physical-environment dimension is out-of-scope for software (flagged separately). Member State transposition divergence may apply on the scope of detection obligations across sectors — French ANSSI requires passive DNS monitoring for entities in essential sectors; German BSI requires industrial-control-system monitoring for energy operators. Remain open: whether the Commission's Article 21(5) implementing acts will specify minimum detection-coverage requirements for the 10 digital-infrastructure categories (the Directive is silent on coverage thresholds).
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-019
  title: "Business continuity, backup, recovery, and crisis triad"
  source_clauses:
    - { clause_id: NIS2-CL12, article_ref: "Art. 21(2)(c) — business continuity, such as backup management and disaster recovery, and crisis management" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-013]
  sub_domain: [D-04.4, D-09.4]
  nist_csf_mapping:
    - { id: RC.RP-04, title: "Critical mission functions and services restored through implementation of the recovery plan" }
    - { id: PR.DS-11, title: "Backups of data are created, protected, maintained, and tested" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 21(2)(c) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management (OJ L 333, 27.12.2022, p. 127). The grammatical structure is `business continuity, such as [backup management and disaster recovery], and crisis management` — the `such as` opens an illustrative list inside an AND of `business continuity` and `crisis management`. The Article 21(1) appropriate-and-proportionate qualifier propagates. The CER Directive parallel (Directive (EU) 2022/2557) Article 12 on emergency communication systems and Article 13 on crisis management reinforce the operational-continuity objective for entities identified as critical entities under CER. ENISA's 2022 baseline security recommendations treat BC/DR/CM as a coherent triad that must operate together; ISO 22301 (business continuity management systems) and ISO 22361 (crisis management) provide the recognised methodological anchors.
  security_rationale: |
    The Article 21(2)(c) obligation to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management is operationalised in NIST CSF 2.0 through **RC.RP-04 (Critical mission functions and services are restored through implementation of the recovery plan)** and **PR.DS-11 (Backups of data are created, protected, maintained, and tested)**. RC.RP-04 anchors the recovery-discipline substrate: the entity must maintain, test and execute a recovery plan that restores critical mission functions through defined procedures, with the recovery time and recovery point objectives calibrated to the criticality classification the entity has assigned under the Article 21(1) appropriate-and-proportionate analysis. PR.DS-11 supplies the backup-discipline substrate on which recovery depends: backups must be created on a defined cadence, protected against the threats the entity faces (including ransomware), maintained across the technology lifecycle, and tested for restorability on a schedule the entity can defend at audit. The two subcategories together address the recovery-execution dimension and the backup-discipline dimension of the BC/DR/CM triad. The resulting recovery plan, test records and backup-restore evidence supply the operational-continuity evidence base and the accountability artefact the Article 21(1) framework requires.
  ambiguity_notes: |
    Article 21(2)(c) carries S3 coordination ambiguity on `business continuity, such as backup management and disaster recovery, and crisis management`. The chosen reading is R1 — all three required (literal AND with `and crisis management`); the alternative reading R3 (BC and CM are the two required; backup and DR are floor examples) is rejected because it admits partial compliance. `Business continuity` admits service-continuity (R1), data-continuity (R2), organisational-continuity (R3), and cumulative (R4) readings; the chosen reading is R4 cumulative per Recital 56 proportionality. `Crisis management` admits strategic (R1), tactical (R2), and both (R3) readings; the chosen reading is R3 per Recital 56. `Backup management` admits policy (R1), operations (R2), and recovery-testing (R3) readings; the chosen reading is R3 cumulative. `Disaster recovery` admits IT-DR (R1), site (R2), and both (R3) readings; the chosen reading is R3 cumulative. Member State transposition divergence may apply on the granularity of BC/DR/CM requirements — French ANSSI requires documented continuity plans for essential entities with annual testing; German BSI requires BSI 200-4 compliance for federal-sector entities. Remain open: (a) whether the Commission's Article 21(5) implementing acts will specify a minimum BC/DR/CM testing cadence for the 10 digital-infrastructure categories (e.g. annual tabletop exercise, semi-annual DR test); (b) whether Member State national transposition will require integration of NIS2 BC/DR/CM with CER Directive crisis-management obligations for entities identified as critical entities under both instruments — the cross-regulation harmonisation is not yet specified.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-020
  title: "Direct supplier and service-provider security by contract"
  source_clauses:
    - { clause_id: NIS2-CL13, article_ref: "Art. 21(2)(d) — supply chain security, including security-related aspects concerning relationships between each entity and its direct suppliers or service providers" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art + standards" }
  linked_objectives: [SO-NIS2-014]
  sub_domain: [D-06.1, D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(d) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers (OJ L 333, 27.12.2022, p. 127). Article 21(1) sentence 2 anchors the state-of-the-art + standards + cost baseline. The clause is the entity-facing supply-chain-security mandate; the EU-level apparatus (Article 22 Cooperation Group coordinated assessments) is the institutional counterpart. The CRA parallel is material: CRA Article 13(5) on secure-by-default configuration and Article 13(13) on coordinated vulnerability disclosure apply to manufacturers of products with digital elements; NIS2 Article 21(2)(d) applies to the entity procuring those products. The `direct` scope-limiter is the single most consequential scope-limiting term in Chapter IV — it determines whether the obligation reaches 1-hop (Tier-1 contractual), n-hop (technically integrated), or only contractually bound counter-parties.
  security_rationale: |
    The Article 21(2)(d) obligation to take measures regarding supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers, is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**. GV.SC-02 supplies the assessment discipline: each direct supplier and service provider is identified, prioritised by criticality, and assessed against a defined methodology, with the assessment depth calibrated to the supplier's risk profile under the Article 21(1) appropriate-and-proportionate qualifier. GV.SC-03 converts the assessment output into contractual instruments — incident-notification clauses, audit rights, data-handling obligations, sub-contracting restrictions, exit provisions — that enforce the assessed posture in operation. The two subcategories together address the assessment dimension and the contractual-enforcement dimension of the supply-chain-security obligation. The resulting supplier register, assessment records and contract-clause catalogue supply the accountability evidence under Article 21(1).
  ambiguity_notes: |
    **`direct` SCOPE-Q S3 — the single most consequential scope-limiter in Chapter IV** (per synthesis §6.1). Three materially distinct readings: R1 `direct` = contractually bound (Tier-1); R2 `direct` = technically integrated (API-connected, shared infrastructure); R3 `direct` = operationally dependent (single-point-of-failure). R1 is the dominant reading in Member State transposition practice (it admits paper-based due diligence and is operationally cheaper); R2 requires technical-integration assessment; R3 requires SPOF analysis. The chosen reading is R1 (contractually bound Tier-1) as the minimum; the entity must additionally consider R2 (technically integrated) for technical-integration points and R3 (operationally dependent) for single-points-of-failure, per Recital 56. The Commission's Article 21(5) implementing acts were expected to clarify this but as of mid-2025 are not yet published. Member State transposition divergence may apply: German BSI has published guidance favouring R1 + R3; French ANSSI favours R2 + R3. `Security-related aspects` (VAG S2) admits cybersecurity-only (R1), information-security broader (R2), and any-security-implication (R3) readings; the chosen reading is R3 per the literal `security-related` adjective. `Suppliers or service providers` (POLY S2) admits hendiadys (R1) and distinct (R2) readings; R2 is literal. Remain open: (a) whether the Commission's Article 21(5) implementing acts will specify the `direct` scope across the 10 digital-infrastructure categories (the implementing acts are pending; the 17 October 2024 deadline has slipped to mid-2025); (b) whether Member State national transposition will impose n-hop (Tier-2 / Tier-3) supply-chain assessment obligations on entities in critical sectors beyond the Directive's `direct` floor — German BSI may signal this in forthcoming BSI 200-4 updates; French ANSSI's labelling schemes (SecNumCloud, visa de sécurité) may de facto impose n-hop through certification chains.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-021
  title: "Security-related contractual aspects of supplier relationships"
  source_clauses:
    - { clause_id: NIS2-CL13, article_ref: "Art. 21(2)(d) — security-related aspects (cross)" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-014]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(d) of Directive (EU) 2022/2555, second clause, requires measures on the `security-related aspects concerning the relationships between each entity and its direct suppliers or service providers` (OJ L 333, 27.12.2022, p. 127). The phrase `security-related` qualifies the aspects of supplier relationships that must be secured. Article 21(1) appropriate-and-proportionate propagates. The `direct` scope-limiter carries the same S3 propagation as SR-NIS2-020.
  security_rationale: |
    The Article 21(2)(d) second-clause obligation regarding the security-related aspects of the relationships between each entity and its direct suppliers or service providers is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**. GV.SC-02 establishes the supplier register and the prioritisation methodology on which the security-related-aspects analysis rests: without knowing which suppliers are in scope and what they provide, the security-related analysis cannot be targeted. GV.SC-04 then ensures the security-related aspects are not assessed once at onboarding but re-validated across the supplier lifecycle — audit results, test outcomes, security-incident feeds from the supplier side, certification renewals — so that contractual obligations continue to be met as the supplier's posture evolves. The two subcategories together address the supplier-knowledge dimension and the lifecycle-validation dimension of the security-related-aspects obligation. The resulting supplier register, ongoing assessment records and audit/test evidence supply the entity-side evidence base on which the entity demonstrates, ex post under Article 21(1), that the security-related aspects of its supplier relationships are managed continuously.
  ambiguity_notes: |
    `Security-related aspects` admits cybersecurity-only (R1), information-security broader (R2), and any-security-implication (R3) readings; the chosen reading is R3 (literal `security-related` qualifier). `Direct` SCOPE-Q S3 — same propagation as SR-NIS2-020. Member State transposition divergence may apply on the contractual minimum (some MS publish minimum-clause catalogues for supplier contracts in essential sectors). Remain open: whether the Commission's Article 21(5) implementing acts will specify a minimum contractual-clause set for the 10 digital-infrastructure categories.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-022
  title: "Per-supplier vulnerability intelligence for risk prioritisation"
  source_clauses:
    - { clause_id: NIS2-CL20, article_ref: "Art. 21(3) sentence 1 — supplier vulnerability assessment" }
    - { clause_id: NIS2-CL13, article_ref: "Art. 21(2)(d) — `direct` scope-limiter (cross)" }
  linked_objectives: [SO-NIS2-015]
  sub_domain: [D-06.3, D-02.1]
  nist_csf_mapping:
    - { id: ID.AM-04, title: "Inventories of suppliers and other third parties are maintained" }
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-02, title: "Threat and vulnerability information received from internal and external sources is collected and used to support risk identification" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-SUPPLIER]
  regulatory_rationale: |
    Article 21(3) sentence 1 of Directive (EU) 2022/2555 requires essential and important entities, when considering which Article 21(2)(d) measures are appropriate, to take into account the vulnerabilities specific to each direct supplier and service provider and the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures (OJ L 333, 27.12.2022, p. 127). The clause is the supplier-specific assessment anchor; it operates per-supplier (PER-SUPPLIER obligation type) rather than as a continuous baseline obligation. The Article 6(15) `vulnerability` definition anchors the substantive scope (weakness, susceptibility or flaw of ICT products or services exploitable by a cyber threat).
  security_rationale: |
    The Article 21(3) sentence 1 obligation, when considering which Article 21(2)(d) measures are appropriate, to take into account the vulnerabilities specific to each direct supplier and service provider is operationalised in NIST CSF 2.0 through **ID.AM-04 (Inventories of suppliers and other third parties are maintained)**, **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)** and **ID.RA-02 (Threat and vulnerability information received from internal and external sources is collected and used to support risk identification)**. ID.AM-04 supplies the supplier-register substrate: each direct supplier is recorded with the products and services it provides, so that vulnerability signals can be mapped to a specific supply relationship. ID.RA-01 then drives the per-supplier vulnerability identification: the entity must validate that the vulnerabilities relevant to a given supplier's products are known, current and scoped, with the granularity the `vulnerabilities specific to each` Article 21(3) text requires. ID.RA-02 ensures the intelligence input — vendor advisories, CVE feeds, sectoral CSIRT notifications, threat-intelligence subscriptions — is collected continuously rather than assessed only at onboarding. The three subcategories together address the supplier-knowledge dimension, the per-supplier granularity dimension and the continuous-intelligence dimension. The resulting supplier-vulnerability register and intelligence feed support the Article 21(3) prioritisation and supply accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Vulnerabilities specific to each` (POLY S2 + SCOPE-Q S2) admits each-supplier-entity (R1), each-supplier-product (R2), and each-supplier-service (R3) readings; the chosen reading is R1 (literal `each direct supplier and service provider`). `Direct` SCOPE-Q S3 — same propagation as SR-NIS2-020. `Vulnerabilities` (POLY S2) admits security (CVE-type, R1), business (SPOF, R2), and compliance (R3) readings; the chosen reading is R1 per the Article 6(15) definition. Member State transposition divergence may apply on the granularity of supplier-vulnerability intelligence (some MS may accept CVE-feed-based intelligence; others may require proprietary assessments). Remain open: whether the Commission's Article 21(5) implementing acts will specify a minimum supplier-vulnerability intelligence methodology.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-023
  title: "Supplier product, service, and process quality assessment"
  source_clauses:
    - { clause_id: NIS2-CL20, article_ref: "Art. 21(3) sentence 1 — overall quality of products and cybersecurity practices" }
    - { clause_id: NIS2-CL13, article_ref: "Art. 21(2)(d) — `direct` scope-limiter (cross)" }
  linked_objectives: [SO-NIS2-015]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-SUPPLIER]
  regulatory_rationale: |
    Article 21(3) sentence 1 of Directive (EU) 2022/2555 second clause requires assessment of `the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures` (OJ L 333, 27.12.2022, p. 127). The `overall quality` assessment is one of three coordinated assessment objects in the Article 21(3) supplier-assessment architecture — the others being vulnerabilities specific to each direct supplier (SR-NIS2-022) and supplier secure-development procedures. The `direct` scope-limiter carries the same S3 propagation as SR-NIS2-020. Article 21(3) sentence 2 requires the entity to take into account the results of EU-level coordinated security risk assessments of critical supply chains under Article 22(1).
  security_rationale: |
    The Article 21(3) sentence 1 second-clause obligation to assess the overall quality of products and cybersecurity practices of suppliers and service providers, including their secure development procedures, is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**. GV.SC-02 supplies the assessment-discipline substrate on which the overall-quality analysis rests: the entity must maintain a methodology that covers product quality (conformity-assessment evidence such as CE marking under CRA, ISO/IEC 27001 certification, sectoral certifications), service quality (SLA evidence, historical performance) and process quality (the supplier's cybersecurity practices, including secure development procedures), with the assessment depth calibrated to the supplier's criticality. GV.SC-04 then ensures the assessment is not a one-off onboarding exercise but is re-validated across the supplier lifecycle — re-audits, re-tests, re-certification tracking — so that overall quality is a current rather than a historical measure. The two subcategories together address the methodology dimension and the lifecycle-validation dimension. The resulting assessment records, audit/test outcomes and certification-tracking evidence supply the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Overall quality` (VAG S2) admits product (R1), service (R2), process (R3), and composite (R4) readings; the chosen reading is R4 (literal `overall`). `Direct` SCOPE-Q S3 — same propagation as SR-NIS2-020. Member State transposition divergence may apply on the assessment evidence (some MS may accept self-attestation; others require independent third-party certification). Remain open: whether the Commission's Article 21(5) implementing acts will specify a minimum evidence baseline for `overall quality` assessment across the 10 digital-infrastructure categories — the CRA certification framework (Article 24 et seq.) is the parallel authority for product-quality assessment and may provide the methodological anchor.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-024
  title: "Supplier secure-development procedures assessed per criticality"
  source_clauses:
    - { clause_id: NIS2-CL20, article_ref: "Art. 21(3) sentence 1 — supplier secure-development procedures" }
    - { clause_id: NIS2-CL13, article_ref: "Art. 21(2)(d) — `direct` scope-limiter (cross)" }
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in development (cross)" }
  linked_objectives: [SO-NIS2-015]
  sub_domain: [D-06.3, D-07.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-SUPPLIER]
  regulatory_rationale: |
    Article 21(3) sentence 1 of Directive (EU) 2022/2555 requires essential and important entities, when considering which of the Article 21(2)(d) measures are appropriate, to assess their suppliers' secure development procedures as the third of three coordinated assessment objects, alongside the supplier's overall cybersecurity practices and the secure-development outcome of the products and services procured. The Article 21(1) appropriate-and-proportionate qualifier propagates through the chain (Article 21(2)(d) → Article 21(3) sentence 1) so that the depth of the supplier-side assessment is calibrated to the criticality of the supplier and the entity's exposure (Recital 56). The cross-link to Article 21(2)(e) means that supplier secure-development procedures are the upstream input for the entity's own security-in-acquisition, security-in-development and security-in-maintenance obligations under the same directive.
  security_rationale: |
    The obligation in Art. 21(3) sentence 1 to assess suppliers' secure-development procedures is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers known, prioritised, and assessed using a C-SCRM process)** and **PR.PS-06 (Secure software development practices integrated and monitored throughout the SDLC)**. GV.SC-02 anchors the assessment methodology: the entity maintains a supplier inventory, prioritises suppliers by criticality and exposure, and applies a documented process that ingests supplier-side development evidence at a frequency proportionate to that criticality. PR.PS-06 specifies what the assessment object looks like: the supplier's SDLC must integrate threat modelling, secure coding, code review and security testing under a monitored programme, and the entity evaluates supplier attestation against this expected control shape. Together, GV.SC-02 and PR.PS-06 define both the assessment gate (supplier criticality and prioritisation) and the evidence base (the SDLC control set) that the entity evaluates. The control set enables ex-post demonstration that the Article 21(3) sentence 1 supplier-development assessment was performed against a documented methodology anchored in the NIST SSDF / ENISA secure-development baseline and re-usable across supplier re-assessments.
  ambiguity_notes: |
    The compound `secure development procedures` carries two readings: an internal-only SDLC interpretation (the supplier's own engineering practices) or an externally-assessable interpretation (procedures the entity can audit via questionnaire, contract clause or third-party attestation), with the chosen reading being the externally-assessable interpretation since the obligation is on the entity to assess rather than on the supplier to self-certify. The Article 21(2)(d) `direct` scope-limiter propagated from SR-NIS2-020 carries the same S3 SCOPE-Q ambiguity into this SR, so that not every supplier relationship falls within the Article 21(3) assessment obligation. Member State transposition divergence may apply on the assessment methodology. Remain open: whether Member State supervisory authorities will publish a minimum questionnaire template for supplier secure-development assessment under Article 4 implementing acts, or whether entities retain full methodology discretion under Recital 56.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-025
  title: "Coordinated supply-chain risk assessments integrated into supplier decisions"
  source_clauses:
    - { clause_id: NIS2-CL21, article_ref: "Art. 21(3) sentence 2 — entity `take into account` Art. 22 results" }
    - { clause_id: NIS2-CL23, article_ref: "Art. 22(1) — Cooperation Group coordinated assessments" }
    - { clause_id: NIS2-CL24, article_ref: "Art. 22(1) — technical and, where relevant, non-technical risk factors" }
  linked_objectives: [SO-NIS2-016]
  sub_domain: [D-06.3, D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-02, title: "Threat and vulnerability information received from internal and external sources is collected and used to support risk identification" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-ASSESSMENT]
  regulatory_rationale: |
    Article 21(3) sentence 2 of Directive (EU) 2022/2555 requires essential and important entities, when considering which of the Article 21(2)(d) measures are appropriate, to take into account the results of the coordinated security risk assessments of critical supply chains carried out in accordance with Article 22(1). Article 22(1) enables the Cooperation Group, in cooperation with the Commission and ENISA, to carry out coordinated assessments of specific critical ICT services, ICT systems or ICT products supply chains, taking into account technical and, where relevant, non-technical risk factors. The chain is therefore Article 22(1) institutional → Article 21(3) sentence 2 entity-implementable; the SR captures the entity-side propagation hook.
  security_rationale: |
    The obligation in Art. 21(3) sentence 2 to take into account the results of Article 22(1) coordinated supply-chain risk assessments is operationalised in NIST CSF 2.0 through **ID.RA-02 (Threat and vulnerability information received from internal and external sources is collected and used to support risk identification)** and **GV.SC-02 (Suppliers known, prioritised, and assessed using a C-SCRM process)**. ID.RA-02 anchors the ingestion of Article 22 institutional outputs into the entity's threat-and-vulnerability register: the Cooperation Group's coordinated assessments, in cooperation with the Commission and ENISA, are treated as authoritative external threat intelligence that no individual entity could replicate from internal sources alone. GV.SC-02 then requires that this intelligence propagate into the supplier-risk decisions, so that Article 22 outputs alter the prioritisation, contractual escalation or substitution decisions on assessed suppliers. Together, ID.RA-02 and GV.SC-02 convert a fragmented national view into a harmonised European baseline for supplier remediation. The control set enables ex-post demonstration that the entity's supplier-risk register reflects the latest Union-scale supply-chain threat picture with documented propagation from external intelligence to internal decision.
  ambiguity_notes: |
    The verb `take into account` admits two operative readings: a passive-consideration reading (the entity reviews the assessment and files it) or an active-integration reading (the entity updates its supplier-risk register to reflect the assessment), with the chosen reading being the literal passive-consideration reading since Article 21(3) sentence 2 does not prescribe a specific decision mechanism. The Article 22(1) chapeau `may carry out` carries the same hybrid discretion/conditional pattern, so that the entity's obligation is triggered only when an Article 22(1) assessment actually exists for a relevant supply chain. Member State transposition divergence may apply on the documentation expected to evidence `taken into account`. Remain open: whether the Commission will publish a standardised mechanism under Article 22(2) (NIS2-CL25) for flagging specific critical ICT subject to assessment in a way that makes the entity-side `take into account` check trivially operational, or whether each entity must monitor the Cooperation Group outputs independently.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-026
  title: "Security requirements embedded in NIS acquisition lifecycle"
  source_clauses:
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in acquisition" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-017]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-ACQUISITION]
  regulatory_rationale: |
    Article 21(2)(e) first clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding security in the acquisition of network and information systems. The acquisition phase is the first of three coordinated lifecycle phases (acquisition, development, maintenance) that constitute the substantive limb of Article 21(2)(e), the process limb being the separate vulnerability handling and disclosure obligation under the same sub-point. The Article 21(1) appropriate-and-proportionate qualifier governs both the choice of acquisition controls and their depth, with Recital 56 anchoring the proportionality factors (entity size, exposure, likelihood, severity).
  security_rationale: |
    The obligation in Art. 21(2)(e) first clause to take measures regarding security in the acquisition of network and information systems is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated and monitored throughout the SDLC)** and **GV.SC-02 (Suppliers known, prioritised, and assessed using a C-SRM process)**. PR.PS-06 anchors the substantive security content that the acquisition decision must demand from the supplier: the supplier's SDLC must integrate threat modelling, secure coding, code review and security testing as evidenced by SSDF or equivalent attestation. GV.SC-02 anchors the process: the entity maintains a prioritised supplier inventory and applies a documented assessment that converts the security baseline into procurement acceptance criteria. Together, PR.PS-06 and GV.SC-02 define both the security object and the assessment process that govern the acquisition lifecycle. The control set enables ex-post demonstration that every acquired NIS was admitted against a documented security baseline proportional to Article 21(1) risk exposure, with re-assessment triggers defined in the supplier's C-SCRM record.
  ambiguity_notes: |
    The compound `security in` carries a process-security versus product-security ambiguity, with the chosen reading being the broad-cumulative interpretation that the entity addresses both the procurement process (how the entity buys) and the product security (what the entity buys). The literal OJ text is silent on CI/CD pipeline vocabulary, NIST SSDF attestation, or ISO 27034 alignment; the SR maps to PR.PS-06 by meaning-alignment rather than by literal-import (T3-vs-text gap awareness per synthesis §8). Member State transposition divergence may apply on whether national law requires a minimum set of acquisition-security clauses (e.g. SBOM delivery, vulnerability-disclosure contractual channel). Remain open: whether the Commission implementing acts under Article 21(5) will specify a baseline acquisition-security clause set or leave the methodology to Recital 56 proportionality.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-027
  title: "Secure-by-design controls integrated across NIS development"
  source_clauses:
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in development" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-017]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PER-DEVELOPMENT]
  regulatory_rationale: |
    Article 21(2)(e) second clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding security in the development of network and information systems. The development phase is the second of three coordinated lifecycle phases in Article 21(2)(e), and applies whether development is performed in-house by the entity or outsourced to a third-party developer under the entity's responsibility. The Article 21(1) appropriate-and-proportionate qualifier governs both the depth of the development controls and the scope of in-house versus outsourced coverage.
  security_rationale: |
    The obligation in Art. 21(2)(e) second clause to take measures regarding security in the development of network and information systems is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated and monitored throughout the SDLC)** and **PR.PS-02 (Software is maintained, replaced, and removed commensurate with risk)**. PR.PS-06 anchors the design-time control set: threat modelling, secure-by-design choices, secure coding standards, code review, and security testing all operate before deployment and so before any operational control can compensate for design weaknesses. PR.PS-02 anchors the lifecycle consequence: development-time decisions about component selection, dependency hygiene and update channels determine what the entity must later maintain, replace or remove. Together, PR.PS-06 and PR.PS-02 connect the design-time control set to the maintenance-time residual-risk profile. The control set enables ex-post demonstration that development-time decisions were risk-informed and that the resulting maintenance burden was deliberately accepted under the Article 21(1) proportionality discipline, with CRA Art. 14 vulnerability-handling readiness built in.
  ambiguity_notes: |
    The same `security in` ambiguity as SR-NIS2-026 applies; the chosen reading is broad-cumulative covering both process and product security in development. The T3-vs-text gap awareness import warning applies with equal force: the OJ does not mention NIST SSDF, OWASP SAMM, ISO 27034, or specific secure-coding catalogues, and the SR preserves OJ-literal `development` language while mapping to PR.PS-06 by meaning-alignment (synthesis §8 T3 NIS2-C11). Member State transposition divergence may apply on whether national law distinguishes in-house versus outsourced development for the depth of the obligation. Remain open: whether the Commission will adopt a delegated act under Article 24(2) specifying that development-tooling categories fall within the European cybersecurity certification scheme, which would convert a procedural development-security obligation into a certification-conditional one.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-028
  title: "Maintenance-phase security with coordinated vulnerability disclosure"
  source_clauses:
    - { clause_id: NIS2-CL14, article_ref: "Art. 21(2)(e) — security in maintenance + vulnerability handling and disclosure" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-017, SO-NIS2-002]
  sub_domain: [D-07.1, D-02.1]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed removed commensurate with risk" }
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(e) third clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding security in the maintenance of network and information systems, including vulnerability handling and disclosure. The maintenance phase is the third of three coordinated lifecycle phases in Article 21(2)(e), and the explicit inclusion of `vulnerability handling and disclosure` extends the maintenance obligation beyond patch and configuration management to the coordinated disclosure pathway. The Article 21(1) appropriate-and-proportionate qualifier governs the maintenance cadence and the disclosure scope; the institutional anchor for external disclosure is Article 12(1) which designates a CSIRT as the Member-State coordinator for coordinated vulnerability disclosure.
  security_rationale: |
    The obligation in Art. 21(2)(e) third clause to take measures regarding security in maintenance, including vulnerability handling and disclosure, is operationalised in NIST CSF 2.0 through **PR.PS-02 (Software is maintained, replaced, and removed commensurate with risk)** and **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)**. PR.PS-02 anchors the patch, configuration and replacement cadence: the entity must keep the NIS current against newly-disclosed vulnerabilities on a risk-proportionate schedule, with documented criteria for replacement-or-removal decisions. ID.RA-01 anchors the discovery-to-record pathway: externally-disclosed vulnerabilities (via the CSIRT-coordinated disclosure channel under Article 12(1), or via researcher-to-vendor direct disclosure) enter the entity's validated vulnerability register, which then drives the PR.PS-02 maintenance response. Together, PR.PS-02 and ID.RA-01 close the loop between external vulnerability disclosure and the internal remediation cycle. The control set enables ex-post demonstration that externally-disclosed findings were triaged, recorded, and remediated on a documented cadence, satisfying ISO/IEC 30111 / ISO/IEC 29147 process expectations.
  ambiguity_notes: |
    The compound `vulnerability handling and disclosure` admits a two-distinct-activities reading or a single-composite-process reading; the chosen reading is two-distinct since the OJ coordinates them with AND, separating the internal triage cycle from the external communication channel. The same `security in` broad-cumulative reading applies as in SR-NIS2-026/027. Member State transposition divergence may apply on the disclosure-channel architecture: some Member States route disclosure exclusively through the national CSIRT, while others accept direct researcher-to-vendor disclosure under coordinated vulnerability disclosure policies. Remain open: whether national supervisory authorities will require a documented vulnerability-disclosure policy under the implementing acts that some Member States have signalled, beyond the Article 21(2)(e) generic maintenance obligation.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-029
  title: "Basic cyber-hygiene practices baseline across workforce and systems"
  source_clauses:
    - { clause_id: NIS2-CL16, article_ref: "Art. 21(2)(g) — basic cyber hygiene practices" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-018]
  sub_domain: [D-08.1]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics" }
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(g) first clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding basic cyber hygiene practices, the first of two coordinated sub-domains in Article 21(2)(g), with the second being cybersecurity training covered by SR-NIS2-030. The Article 21(1) appropriate-and-proportionate qualifier propagates and is operationalised by Recital 56 proportionality factors, which leaves the methodology choice (which hygiene practices count as `basic`) to the entity under the proportionality discipline.
  security_rationale: |
    The obligation in Art. 21(2)(g) first clause to take measures regarding basic cyber hygiene practices is operationalised in NIST CSF 2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity topics)** and **PR.PS-01 (Configuration management practices are established, documented, and applied to assets)**. PR.AT-01 anchors the human-side hygiene substrate: phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, and the disciplined use of administrative privileges. PR.PS-01 anchors the system-side hygiene substrate: baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory. Together, PR.AT-01 and PR.PS-01 define the workforce-and-assets hygiene baseline that ENISA, the SANS Top 20 and the Australian Cyber Security Centre Essential Eight converge on. The two controls also propagate into the vulnerability-hygiene loop: hygiene lapses are themselves a recurring source of incidents that ID.RA-01 records and PR.PS-02 remediates. The control set enables ex-post demonstration that the entity operates against a documented hygiene baseline rather than an ad-hoc checklist, with the depth calibrated to Article 21(1) proportionality factors and the baseline re-reviewed when ENISA or national guidance material changes.
  ambiguity_notes: |
    The undefined compound `basic cyber hygiene` admits three operative readings — a minimal-password-patch-antivirus reading, the broader ENISA baseline reading, or a sector-specific reading — with the chosen reading being the entity-discretionary interpretation under Recital 56 proportionality, since the OJ does not enumerate the hygiene practices. The compound `cyber hygiene` admits a technical versus procedural versus cultural reading; the cultural reading is dominant under Recital 50, which positions cyber hygiene as a workforce-and-process concept rather than a checklist. Member State transposition divergence may apply: some Member States publish a national hygiene baseline that entities are expected to meet or exceed. Remain open: whether Member States will align their national hygiene baselines with the European cybersecurity baseline under Article 4 implementing acts, which would convert the methodology-discretion interpretation into a conformance baseline.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-035
  title: "Documented risk-analysis methodology with proportional scope and cadence"
  source_clauses:
    - { clause_id: NIS2-CL10, article_ref: "Art. 21(2)(a) — policies on risk analysis" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-022]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(a) first clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding policies on risk analysis, the first of two coordinated sub-domains in Article 21(2)(a), with the second being policies on information system security captured in SR-NIS2-036. The Article 21(1) appropriate-and-proportionate qualifier propagates and is operationalised by Recital 56 proportionality factors. The Article 21(1) sentence 2 state-of-the-art, standards and cost-of-implementation anchor governs the methodology choice. The `policies on risk analysis` formulation is methodology-agnostic: the OJ does not prescribe qualitative, quantitative or hybrid, nor does it prescribe a specific risk-analysis framework, leaving the methodology to the entity under the proportionality discipline.
  security_rationale: |
    The obligation in Art. 21(2)(a) first clause to take measures regarding policies on risk analysis is operationalised in NIST CSF 2.0 through **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **GV.PO-01 (Organisational cybersecurity policy is established, communicated, and enforced)**. ID.RA-05 anchors the substantive content of the risk-analysis policy: the policy specifies how the entity identifies threats and vulnerabilities, estimates likelihood and impact, and uses these inputs to inform risk response decisions on a documented cadence. GV.PO-01 anchors the policy artefact: the methodology is documented, communicated across the entity, and enforced as binding organisational policy with named owners and re-review triggers. Together, ID.RA-05 and GV.PO-01 connect the substantive methodology to the governance artefact. The control set enables ex-post demonstration that the entity's risk-analysis decisions are repeatable, auditable, and proportionate to the Article 21(1) risk exposure rather than ad-hoc, and that risk-response decisions trace back to the documented analysis.
  ambiguity_notes: |
    The compound `risk analysis` admits three operative readings: a qualitative reading, a quantitative reading, or a hybrid reading, with the chosen reading being the entity-discretionary hybrid because Recital 56 leaves methodology to the entity under the proportionality discipline and most operational risk-analysis practices combine qualitative likelihood-impact matrices with quantitative loss-expectancy calculations for material risks. The compound `policies` admits a formal-versus-informal reading; the formal reading is dominant under Recital 56 since the OJ's policy framing presumes documented, communicated, and enforceable artefacts (NIST CSF 2.0 GV.PO-01). Member State transposition divergence may apply on whether national supervisory authorities require a specific methodology (e.g. France ANSSI's EBIOS RM, Germany BSI's BSI-Standard 200-3). Remain open: whether Member States will publish a national risk-analysis methodology baseline that converts the methodology-discretion interpretation into a conformance expectation under Article 4 implementing acts.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-036
  title: "Information-system-security policy governs NIS configuration and operation"
  source_clauses:
    - { clause_id: NIS2-CL10, article_ref: "Art. 21(2)(a) — policies on information system security" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
  linked_objectives: [SO-NIS2-022]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2)(a) second clause of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding policies on information system security, the second of two coordinated sub-domains in Article 21(2)(a), with the first being policies on risk analysis captured in SR-NIS2-035. The Article 21(1) appropriate-and-proportionate qualifier propagates. The literal AND conjunction between `risk analysis` and `information system security` is read as requiring two distinct policies (one for risk analysis, one for IS security) rather than one composite policy, because the OJ coordinates two semantically distinct objects with the conjunction and Recital 56 framing supports discrete governance artefacts.
  security_rationale: |
    The obligation in Art. 21(2)(a) second clause to take measures regarding policies on information system security is operationalised in NIST CSF 2.0 through **GV.PO-01 (Organisational cybersecurity policy is established, communicated, and enforced)** and **PR.PS-01 (Configuration management practices are established, documented, and applied to assets)**. GV.PO-01 anchors the policy artefact: the IS-security policy is documented, communicated, and enforced as a binding governance instrument distinct from the risk-analysis policy of SR-NIS2-035, with named owners and re-review cadence. PR.PS-01 anchors the operational substrate: the policy specifies baseline configurations, secure configuration standards, change-management discipline, and the audit cadence against the policy. Together, GV.PO-01 and PR.PS-01 connect the policy artefact to the configuration discipline that operationalises it across the NIS inventory. The control set enables ex-post demonstration that the NIS inventory is operated against a documented configuration baseline that anchors downstream monitoring, change management, and patch-cadence decisions, and that drift from the baseline is detected and remediated on a defined schedule.
  ambiguity_notes: |
    The compound `information system security` carries a POLY ambiguity on scope: a cyber-only reading, a cyber-plus-physical reading, or a cyber-plus-operational reading, with the chosen reading being the broader cyber-plus-operational reading because the Article 21(2) chapeau `all-hazards approach` (SR-NIS2-040) explicitly extends the Article 21(2) sub-point architecture to non-cyber hazards that compromise NIS. The AND coordination between `risk analysis` and `information system security` admits a two-distinct-policies reading or a single-composite-policy reading; the literal two-distinct-policies reading is dominant because the OJ coordinates two distinct objects with the conjunction. Member State transposition divergence may apply on whether national supervisory authorities expect the IS-security policy to enumerate specific configuration baselines (e.g. CIS Benchmarks) or to leave the baseline to entity discretion under the proportionality discipline. Remain open: whether Member State supervisory authorities will codify a national IS-security policy baseline template that converts the policy-discretion interpretation into a conformance expectation under Article 4 implementing acts.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-037
  title: "Policy framework for assessing cybersecurity risk-management measure effectiveness"
  source_clauses:
    - { clause_id: NIS2-CL15, article_ref: "Art. 21(2)(f) — policies and procedures to assess effectiveness of cybersecurity risk-management measures" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art (cross)" }
  linked_objectives: [SO-NIS2-023]
  sub_domain: [D-09.1, D-09.3, D-10.3]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: ID.IM-01, title: "Improvement processes across cybersecurity risk management are identified and used" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Article 21(2)(f) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding policies and procedures to assess the effectiveness of cybersecurity risk-management measures. The `effectiveness assessment` is the operational feedback loop for the Article 21 measures and is structurally distinct from the corrective-measures obligation of Article 21(4) (SR-NIS2-042): effectiveness assessment is the forward-looking measurement of whether the measures achieve their intended outcome, while corrective measures are the triggered response when assessment identifies non-compliance. The Article 21(1) appropriate-and-proportionate qualifier and Article 21(1) sentence 2 state-of-the-art and cost-of-implementation anchor propagate, with Recital 56 proportionality factors governing the assessment depth. The literal AND coordination of `policies and procedures` is read as requiring both a policy artefact and procedural operationalisation (NIST CSF 2.0 GV.PO-01 + GV.PO-02). The synthesis §3 mark identifies this sub-point as the Article 21 effectiveness POLY hotspot because the OJ uses the open-textured `effectiveness` term without defining the assessment object.
  security_rationale: |
    The obligation in Art. 21(2)(f) to take measures regarding policies and procedures to assess the effectiveness of cybersecurity risk-management measures is operationalised in NIST CSF 2.0 through **GV.PO-01 (Organisational cybersecurity policy is established, communicated, and enforced)**, **ID.IM-01 (Improvement processes across cybersecurity risk management are identified and used)**, and **GV.OV-03 (Organisational cybersecurity performance is evaluated and reviewed for needed adjustments)**. GV.PO-01 anchors the policy artefact: the entity maintains a documented effectiveness-assessment policy with named owners and a re-review cadence. ID.IM-01 anchors the improvement-process substrate: assessment findings feed the plan-do-check-act cycle and trigger measurable improvement actions that close identified gaps. GV.OV-03 anchors the performance-evaluation dimension: the policy defines metrics, review cadence, and the criteria for declaring an assessment finding material. Together, the three control elements close the effectiveness loop. The control set enables ex-post demonstration that the entity measures whether the Article 21 measures achieve their intended outcomes rather than treating compliance as a one-time check, and that the assessment outputs drive documented improvement actions.
  ambiguity_notes: |
    The compound `effectiveness` carries the Article 21(2)(f) POLY hotspot ambiguity with three operative readings: a control-effectiveness reading (does the control work as designed), a risk-effectiveness reading (does the control reduce risk to acceptable level), or an outcome-effectiveness reading (does the measure achieve its intended outcome), with the chosen reading being the outcome-effectiveness reading because the OJ is outcome-oriented (the assessment object is `cybersecurity risk-management measures` rather than specific controls), and Recital 56 framing supports outcome-measurement as the natural reading of `effectiveness of measures`. The AND coordination of `policies and procedures` admits a two-distinct-artefacts reading or a hendiadys (single artefact with two labels) reading, with the two-distinct reading being dominant because the OJ coordinates two governance terms that NIST CSF 2.0 treats as distinct sub-categories (GV.PO-01 policy and GV.PO-02 processes and procedures). The T3-vs-text gap awareness (synthesis §8) imports ISO 27004 measurement vocabulary not present in the OJ, and the SR preserves OJ-literal language while mapping to ID.IM-01 + GV.OV-03 (improvement + performance evaluation) by meaning-alignment rather than literal-import. Member State transposition divergence may apply on whether national supervisory authorities require specific effectiveness-assessment metrics (e.g. MTTD, MTTR, control-coverage percentage) or accept entity-discretionary metrics under the proportionality discipline. Remain open: (a) whether the Commission will adopt implementing acts under Article 21(5) that specify effectiveness-assessment metrics, which would convert the methodology-discretion interpretation into a metrics-conformance baseline; (b) whether the outcome-effectiveness reading requires the entity to demonstrate contribution-to-risk-reduction evidence under DORA Art. 18 testing parallel, or whether residual-risk-acceptance documentation suffices.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-038
  title: "Scheduled procedures operationalise cybersecurity effectiveness measurement"
  source_clauses:
    - { clause_id: NIS2-CL15, article_ref: "Art. 21(2)(f) — procedures (procedural dimension of effectiveness assessment, cross)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art (cross)" }
  linked_objectives: [SO-NIS2-023]
  sub_domain: [D-09.3, D-10.3]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Article 21(2)(f) second limb of Directive (EU) 2022/2555 captures the procedural dimension of effectiveness assessment, with the policy dimension captured in SR-NIS2-037. Procedures operationalise the policies with concrete assessment cadence (audit frequency, test frequency, review frequency), evidence requirements (documentation, log retention, attestation), and the responsible-function allocation (CISO, internal audit, external auditor). The Article 21(1) sentence 2 state-of-the-art anchor propagates and is operationalised by Recital 56 proportionality. The SR captures the procedural half of the `policies and procedures` AND coordination in Article 21(2)(f), and is structurally lighter than SR-NIS2-037 because the substantive ambiguity lives in the policy half (the `effectiveness` POLY hotspot).
  security_rationale: |
    The obligation in Art. 21(2)(f) procedural limb to operationalise the effectiveness-assessment policy is operationalised in NIST CSF 2.0 through **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.OV-03 (Organisational cybersecurity performance is evaluated and reviewed for needed adjustments)**. GV.PO-02 anchors the procedural artefact: documented procedures specify assessment cadence (internal audit, penetration test, control-effectiveness review, management-body dashboard review), evidence requirements (documentation, log retention, attestation), and responsible-function allocation (CISO, internal audit, external auditor) with named owners. GV.OV-03 anchors the evaluation discipline: each procedure generates performance evidence that the management body reviews against the policy of SR-NIS2-037 on a recurring cadence. Together, GV.PO-02 and GV.OV-03 connect procedural implementation to performance evaluation. The control set enables ex-post demonstration that the effectiveness assessment runs on a scheduled cadence and produces auditable evidence rather than ad-hoc reviews, with the cadence proportionate to the entity's exposure.
  ambiguity_notes: |
    The same `effectiveness` POLY hotspot ambiguity as SR-NIS2-037 propagates into this SR (the procedural half inherits the substantive reading of the policy half); the chosen outcome-effectiveness reading is preserved. The same T3-vs-text gap awareness (synthesis §8) applies: the OJ does not mention ISO 27004 measurement vocabulary, and the SR maps to GV.PO-02 + GV.OV-03 by meaning-alignment. The assessment cadence is not specified by the Directive (no analogue to GDPR Article 35(11) `at least when there is a change of the risk presented by processing operations`); the cadence is entity-discretionary under Recital 56 proportionality. Member State transposition divergence may apply on whether national supervisory authorities require specific procedural artefacts (e.g. annual external audit, semi-annual internal audit, quarterly management review) that convert the cadence-discretion interpretation into a procedural baseline. Remain open: whether Member State supervisory authorities will align their national effectiveness-assessment procedural expectations with the DORA Art. 18 ICT risk-management framework testing cadence (annual for significant ICT-risk-driven entities), which would create a cross-regulation cadence alignment.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-039
  title: "Risk-calibrated technical, operational and organisational measures baseline"
  source_clauses:
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) sentence 1 — appropriate and proportionate technical, operational and organisational measures" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art + standards + cost of implementation" }
  linked_objectives: [SO-NIS2-021, SO-NIS2-022]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "Standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(1) sentence 1 of Directive (EU) 2022/2555 requires Member States to ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems, which the entities use for their operations or for the provision of their services, and to prevent or minimise the impact of incidents on recipients of their services and on other services. Article 21(1) sentence 2 anchors the baseline against the state of the art, relevant European and international standards, and the cost of implementation, and operationalises the proportionality qualifier with four named factors (degree of exposure of the entity to risks; entity size; likelihood of occurrence of incidents and their severity; societal and economic impact). The chapeau is structurally the meta-clause that propagates to every Article 21(2) sub-point; the SR captures the chapeau itself as a cross-cutting governance artefact, distinct from but dependent on each sub-point SR (SR-NIS2-026 through SR-NIS2-038).
  security_rationale: |
    The obligation in Art. 21(1) sentence 1 chapeau that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems is operationalised in NIST CSF 2.0 through **GV.RM-06 (Standardised method for calculating, documenting, categorising, and prioritising cybersecurity risks is established and communicated)** and **ID.RA-06 (Risk responses are chosen, prioritised, planned, tracked, and communicated)**. GV.RM-06 anchors the standardised risk-calibration methodology: the entity uses a documented method to calculate, document, categorise and prioritise risks against the four proportionality factors (exposure, size, likelihood, societal and economic impact). ID.RA-06 anchors the response selection: each Article 21(2) sub-point measure is chosen, prioritised, planned and tracked as a documented risk response with named owners and target completion milestones. Together, GV.RM-06 and ID.RA-06 connect the chapeau's meta-clause to each sub-point in a risk-justified way. The control set enables ex-post demonstration that the Article 21 measure set is risk-calibrated rather than a compliance checklist.
  ambiguity_notes: |
    The compound `appropriate and proportionate` carries the dominant Berry VAG-S3 ambiguity of the Directive with three operative readings: an independent-tests reading (the entity must satisfy both `appropriate` and `proportionate` independently), a hierarchical reading (`appropriate` modifies `proportionate` so that the proportionality is itself subject to an appropriateness qualifier), or a compound-qualifier reading (a fixed phrase that operationalises through Article 21(1) sentence 2's named factors), with the chosen reading being the compound-qualifier reading because sentence 2 explicitly operationalises the chapeau by enumerating four proportionality factors (exposure, size, likelihood and severity, societal and economic impact), which is the structural commitment to the compound interpretation (synthesis §3 marks this as the dominant Berry VAG trigger of NIS2). The compound `technical, operational and organisational` admits three distinct-categories, cumulative, or open-list readings, with the open-list reading being dominant under Recital 56. The compound `state-of-the-art` admits three readings (current best practice qualitative, published standards, or cutting-edge frontier research), with the first two operative and the third rejected by Recital 56 because cost of implementation implies off-the-shelf. The compound `cost of implementation` admits entity-level, national-economy-level, or supply-chain-level readings, with the entity-level reading being literal because the chapeau binds the entity to the cost of its own implementation. The compound `manage the risks` admits an identify-assess-mitigate reading, an ISO 27005 `treat` reading, or a continuous-monitoring reading, with the continuous-monitoring reading being dominant under the all-hazards approach of Article 21(2) chapeau (SR-NIS2-040). The compound `impact on recipients of their services and on other services` admits a single-class or two-class reading; the two-class literal AND reading is dominant. Member State transposition divergence is highest on `state of the art`: Germany BSI standardises through BSI TR-02102 (cryptography), BSI-Standard 200-2 (IT-Grundschutz methodology); France ANSSI requires an independent qualified-body assessment for first-class operators; Italy ACN publishes annual guidance and sectoral decrees. Remain open: (a) whether the Commission will adopt implementing acts under Article 21(5) that specify a baseline state-of-the-art methodology, which would convert the methodology-discretion interpretation into a conformance baseline; (b) whether the proportionality factors will be harmonised at EU level through Article 4 implementing acts, or whether each Member State retains full methodological discretion and the divergence compounds over the 27 implementations.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-040
  title: "All-hazards methodology spanning cyber, physical and operational risks"
  source_clauses:
    - { clause_id: NIS2-CL09, article_ref: "Art. 21(2) chapeau — all-hazards approach" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (cross)" }
  linked_objectives: [SO-NIS2-022]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "Standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and established" }
    - { id: PR.IR-01, title: "Networks and environments are protected from unauthorized logical access and usage" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2) chapeau of Directive (EU) 2022/2555 requires that the measures referred to in paragraph 1 shall be based on an all-hazards approach that aims to protect network and information systems and the physical environment of those systems from incidents. The chapeau is the meta-methodology clause that propagates through the entire Article 21(2) sub-point architecture and converts the cybersecurity-only default reading of the NIS1 Directive into an all-hazards reading that includes non-cyber hazards. The `physical environment of those systems` dimension is captured by SR-NIS2-041 as a separate SR for the physical-security dimension. The Article 21(1) appropriate-and-proportionate qualifier propagates.
  security_rationale: |
    The obligation in Art. 21(2) chapeau that the measures referred to in Article 21(1) shall be based on an all-hazards approach that aims to protect network and information systems and the physical environment of those systems from incidents is operationalised in NIST CSF 2.0 through **GV.RM-06 (Standardised method for calculating, documenting, categorising, and prioritising cybersecurity risks is established and communicated)** and **PR.IR-01 (Networks and environments are protected from unauthorised logical access and usage)**. GV.RM-06 anchors the meta-methodology: the entity's risk-calibration methodology explicitly enumerates non-cyber hazards (operational accidents, environmental disruption, supply-chain physical compromise, natural disasters) alongside cyber hazards, with a documented rationale for the scope chosen. PR.IR-01 anchors the protective-control substrate: the protective controls extend from the logical network perimeter to the physical environment that hosts the NIS. Together, GV.RM-06 and PR.IR-01 prevent the entity from treating cybersecurity as separable from physical and operational security. The control set enables ex-post demonstration that the all-hazards framing is reflected in both the risk methodology and the deployed controls, consistent with the CER Directive parallel on critical-entity resilience.
  ambiguity_notes: |
    The compound `all-hazards approach` admits three operative readings: a cybersecurity-only reading, an inclusive-of-natural-disasters reading, or an inclusive-of-physical-security reading, with the chosen reading being the broadest inclusive reading because the chapeau explicitly extends to `the physical environment of those systems`, which is the textual anchor that the all-hazards scope is not cybersecurity-only. The physical-environment dimension is captured by SR-NIS2-041 as a carve-out for the physical-security sub-domain (out-of-scope for the software-compliance track but in-scope for the entity's overall governance). Member State transposition divergence may apply: some Member States interpret `all-hazards` narrowly (cybersecurity-only) in their national transposition, which would convert the broadest reading into a narrower Member-State-specific obligation. Remain open: whether Member State supervisory authorities will publish a national all-hazards baseline that explicitly enumerates the non-cyber hazards in scope (natural disasters, physical intrusion, supply-chain physical compromise, environmental disruption), which would convert the methodology-discretion interpretation into a national-hazard enumeration baseline.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-041
  title: "Physical-environment protection ensures NIS substrate resilience"
  source_clauses:
    - { clause_id: NIS2-CL09, article_ref: "Art. 21(2) chapeau — protection of the physical environment of those systems" }
  linked_objectives: [SO-NIS2-022]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "Standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2) chapeau second clause of Directive (EU) 2022/2555 extends the all-hazards approach of SR-NIS2-040 to `the physical environment of those systems`, capturing the physical substrate (server rooms, data centres, network equipment closets, edge facilities) that hosts the NIS and whose physical compromise propagates to NIS availability, integrity and confidentiality. The Article 21(1) appropriate-and-proportionate qualifier propagates and governs the physical-environment scope. The SR is structurally a carve-out flag: it captures the physical-security dimension explicitly in scope of Article 21 but out-of-scope for the software-compliance track of AEGIS, since the obligation is a physical-security obligation rather than a software-security obligation.
  security_rationale: |
    The obligation in Art. 21(2) chapeau second clause that the all-hazards approach extends to the physical environment of network and information systems is operationalised in NIST CSF 2.0 through **GV.RM-06 (Standardised method for calculating, documenting, categorising, and prioritising cybersecurity risks is established and communicated)** and, by extension, **PR.IR-02 (The organisation's technology assets are protected from environmental threats)** as the closest CSF control for the physical substrate. GV.RM-06 anchors the meta-methodology that captures the physical-environment dimension: the entity's risk-calibration methodology enumerates physical-environment hazards (intrusion, theft, sabotage, fire, flooding, environmental-control failure) and assigns them to the NIS-availability and NIS-integrity dimensions. Because the SR is structurally a carve-out flag for the physical-security dimension (out-of-scope for the software-compliance track of AEGIS), the mapping is meta-methodological rather than software-security specific. The control set enables ex-post demonstration that the entity considered the physical substrate as an integral element of the all-hazards methodology rather than as a separable concern.
  ambiguity_notes: |
    The compound `physical environment of those systems` carries a SCOPE-Q S2 ambiguity with three readings: a narrow reading (server rooms, data centres, network equipment closets), a medium reading (buildings including offices and call centres that host NIS-supporting staff), or a broad reading (surrounding critical infrastructure including power, cooling and telecoms). The narrow reading is the chosen OJ-literal reading because the qualifier `of those systems` anchors the physical environment to the NIS rather than to the entity's broader footprint. The SR is OUT-OF-SCOPE for the software-compliance track: it captures a physical-security requirement, not a software requirement, and Layer 3 (inference-trust) must adjudicate whether software-software integration controls are needed for the physical-environment dimension (e.g. environmental sensors feeding into security monitoring tooling, physical-access-control-system event correlation with identity governance). The SR maps to GV.RM-06 as a meta-methodology reference and does not generate software-security rules for downstream phases. Member State transposition divergence may apply on whether national supervisory authorities expect a documented physical-environment risk assessment as a sub-component of the all-hazards methodology. Remain open: (a) whether the narrow reading requires a separate physical-environment risk-assessment document or whether the all-hazards methodology under SR-NIS2-040 covers it implicitly; (b) whether the broad-reading interpretation applies to NIS-supporting critical infrastructure operators under the CER Directive cross-link (Art. 23(10) CER cross-sharing), which would couple this SR with the CER resilience obligation.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-042
  title: "Root-cause corrective measures triggered by non-compliance findings"
  source_clauses:
    - { clause_id: NIS2-CL22, article_ref: "Art. 21(4) — without undue delay + necessary, appropriate and proportionate corrective measures" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (cross)" }
  linked_objectives: [SO-NIS2-023]
  sub_domain: [D-09.3, D-09.4]
  nist_csf_mapping:
    - { id: ID.IM-01, title: "Improvement processes across cybersecurity risk management are identified and used" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 21(4) of Directive (EU) 2022/2555 requires Member States to ensure that essential and important entities that find that they do not comply with the Article 21(2) measures take, without undue delay, all necessary, appropriate and proportionate corrective measures. The clause is the triggered-response instrument of the Article 21 architecture: the trigger is the entity's own finding of non-compliance (typically via the SR-NIS2-037 effectiveness assessment, an audit, an incident post-mortem or supervisory-authority finding); the response is the corrective-measures package; the temporal anchor is `without undue delay`. The Article 21(1) appropriate-and-proportionate qualifier propagates and is repeated in the corrective-measures qualifier (`necessary, appropriate and proportionate`), so that the corrective package itself is subject to the same proportionality discipline as the underlying measures.
  security_rationale: |
    The obligation in Art. 21(4) that essential and important entities that find that they do not comply with the Article 21(2) measures take, without undue delay, all necessary, appropriate and proportionate corrective measures is operationalised in NIST CSF 2.0 through **ID.IM-01 (Improvement processes across cybersecurity risk management are identified and used)**, **GV.OV-03 (Organisational cybersecurity performance is evaluated and reviewed for needed adjustments)**, and **RS.MI-02 (Incidents are mitigated)**. ID.IM-01 anchors the root-cause remediation process: corrective measures address the underlying cause of the non-compliance finding rather than the symptom, with documented cause-analysis and verification of remediation effectiveness. GV.OV-03 anchors the performance-review loop: the corrective package is reviewed against the effectiveness-assessment policy of SR-NIS2-037. RS.MI-02 anchors the incident-driven trigger: where the non-compliance finding originates from an incident, the corrective package includes the incident-mitigation response. Together, the three control elements close the gap between detection and remediation. The control set enables ex-post demonstration that non-compliance findings were resolved on a documented, root-cause basis within the OJ's `without undue delay` anchor.
  ambiguity_notes: |
    The temporal anchor `without undue delay` carries an S3 VAG ambiguity with three operative readings: a 24-hour reading (parallel to the Article 23(4)(a) early-warning deadline), a 72-hour reading (parallel to the Article 23(4)(b) incident-notification deadline), or a reasonable-time reading (standard EU drafting convention with no fixed deadline), with the chosen reading being the reasonable-time reading because the OJ does not specify a numeric deadline and Recital 60 confirms the standard EU drafting convention of leaving the temporal anchor to the proportionality discipline. The compound `necessary, appropriate and proportionate` carries an S3 VAG ambiguity with three operative readings: three-independent-qualifiers reading (the corrective package must satisfy all three independently), a synonyms reading (the three terms reinforce each other), or a floor-target-ceiling reading (necessary is the floor, appropriate is the target, proportionate is the ceiling), with the chosen reading being the three-independent-qualifiers reading because the literal AND coordination with three distinct qualifiers is the same Berry pattern as the Article 21(1) opening and Recital 56 framing supports the independent-qualifiers interpretation. The compound `corrective measures` admits a fixes reading, a compensating-controls reading, or a root-cause-remediation reading, with the chosen reading being the root-cause-remediation reading because the ISO 27001:2022 corrective-action concept positions corrective measures as root-cause remediation rather than symptom compensation. Member State transposition divergence may apply on the temporal anchor: Germany BSI requires documented corrective-action timelines (BSI-Standard 200-2 IT-Grundschutz methodology); France ANSSI requires notification of corrective measures to the ANSSI for first-class operators; Italian ACN expects corrective-measures documentation as part of the annual NIS compliance report. Remain open: (a) whether Member State supervisory authorities will codify a maximum-timeline for corrective measures (e.g. 30 days for low-risk non-compliance, 7 days for high-risk non-compliance) under Article 4 implementing acts, which would convert the temporal-discretion interpretation into a conformance baseline; (b) whether the reasonable-time reading of `without undue delay` is aligned with the GDPR Article 33(1) `without undue delay and, where feasible, not later than 72 hours` for personal-data-breach notification, which would create a cross-regulation temporal anchor for entities subject to both GDPR and NIS2.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

