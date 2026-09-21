---
document_id: AEGIS-PREPROC-GDPR-ART-32
title: GDPR Art. 32 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 32
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
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# GDPR Art. 32

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-001 | Personal data remains confidential while at rest, in storage, and during processing, against unauthorised or unlawful processing. | `GDPR-CL06` (Art. 5(1)(f)); `GDPR-CP15` (Art. 32(1)(a)/(b)) | D-01.1 |
| SO-GDPR-001 (cross-ref) | Confidentiality, integrity, and resilience of processing systems and services — implicitly covers data in transit through "processing systems" architecture. | `GDPR-CP15` (Art. 32(1)(b)) | D-01.1, D-01.2, D-01.4 |
| SO-GDPR-001 | D-01.1, D-01.4 | Art. 5(1)(f), Art. 32(1)(a)/(b) | Personal data confidentiality at rest and in processing |
| SO-GDPR-002 | Personal data protected by pseudonymisation or encryption remains unintelligible to any person who is not authorised to access it, including following a personal data breach. | `GDPR-CP20` (Art. 34(3)(a)); `GDPR-CP15` (Art. 32(1)(a)) | D-01.1, D-01.3 |
| SO-GDPR-002 | D-01.3, D-01.1 | Art. 4(5), Art. 32(1)(a), Art. 34(3)(a) | Pseudonymisation/encrypted data unintelligible post-breach |
| SO-GDPR-014 | Availability and access to personal data can be restored in a timely manner following a physical or technical incident. | `GDPR-CP15` (Art. 32(1)(c)) | D-04.4 (covers integrity + availability) |
| SO-GDPR-014 | The ability to ensure the ongoing availability, integrity, and resilience of processing systems and services is maintained, and to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident. | `GDPR-CP15` (Art. 32(1)(b)/(c)) | D-04.4, D-01.4 |
| SO-GDPR-014 | D-04.4, D-01.4 | Art. 32(1)(b)/(c) | Resilience and timely restore of availability |
| SO-GDPR-004 | A process is established for regularly testing, assessing, and evaluating the effectiveness of technical and organisational measures for ensuring security of processing. | `GDPR-CP15` (Art. 32(1)(d)); `GDPR-CP22` (Art. 35(11)) | D-02.1, D-10.3 |
| SO-GDPR-004 (cross-ref) | Technical and organisational measures for ensuring security of processing are regularly tested, assessed, and evaluated for effectiveness (Art. 32(1)(d)); the DPIA is reviewed at least when there is a change of risk represented by processing operations (Art. 35(11)). | `GDPR-CP15` (Art. 32(1)(d)); `GDPR-CP22` (Art. 35(11)) | D-02.1, D-10.3 |
| SO-GDPR-004 | D-02.1, D-10.3 | Art. 32(1)(d), Art. 35(11) | Regular testing/assessing/evaluating security measures |
| SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality. | `GDPR-CP11` (Art. 29); `GDPR-CP09` (Art. 28(3)(a)/(b)); `GDPR-CP15` (Art. 32(4)) | D-03.3 |
| SO-GDPR-006 | D-03.3 | Art. 28(3)(a)/(b), Art. 29, Art. 32(4) | Authorised persons act on instructions + confidentiality |
| SO-GDPR-030 | Personal-data processing systems and services are monitored for adverse events covering the five Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), with a clear definition of the moment of "becoming aware of" a breach to anchor the Art. 33(1) notification clock. | `GDPR-CP16` (Art. 32(2)); `GDPR-CP17` (Art. 33(1) — `becoming aware`); `GDPR-CP15` (Art. 32(1)(b)) | D-10.1, D-04.1 |
| SO-GDPR-030 | D-10.1, D-04.1 | Art. 32(2), Art. 33(1), Art. 32(1)(b) | Monitoring the five Art. 32(2) risk types |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-001
  title: "CIA + resilience baseline for personal data processing"
  source_clauses:
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f)" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data definition" }
  linked_objectives: [SO-GDPR-001]
  sub_domain: [D-01.1, D-01.4]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-10, title: "Data-in-use protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(f) establishes integrity and confidentiality as one of the six principles relating to processing of personal data, requiring that personal data be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures. Art. 32(1)(b) operationalises this by listing the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services among the measures that the controller and processor must implement under the Art. 32(1) risk-based preamble. Read together, the two provisions establish a continuous obligation to maintain the CIA triad, augmented by an explicit resilience dimension, across the entire processing surface. Two textual points warrant attention for compliance scoping. First, "appropriate" in Art. 5(1)(f) is anchored by the Art. 32(1) preamble to a risk-based test (state of the art, costs of implementation, nature, scope, context and purposes of processing, risks of varying likelihood and severity), meaning the controller must justify the chosen security level ex post rather than declaring it ex ante. Second, the disjunction "technical or organisational measures" admits both an inclusive reading (at least one category suffices) and a strict reading (both required); the parallel wording of Art. 24(1) written with "and" pulls toward the strict reading, which is also the dominant position under ISO 27001-aligned compliance programmes.
  security_rationale: |
    The obligation in Art. 5(1)(f) and Art. 32(1)(b) to maintain the confidentiality, integrity, availability and resilience of personal data is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.DS-10 (Data-in-use protected)**.
    PR.DS-01 anchors the protection of stored personal data against unauthorised or unlawful processing and against accidental loss, destruction or damage, satisfying the Art. 5(1)(f) integrity-and-confidentiality principle at the storage layer where the dominant exfiltration surface sits.
    PR.DS-10 extends that protection to data undergoing query, transformation and join operations inside application processes, closing the gap that at-rest controls alone leave open and covering the full data lifecycle that the Art. 32(1)(b) ongoing-confidentiality duty references, including the explicit resilience dimension that signals graceful degradation and recovery to a known-good state.
    A controller that documents PR.DS-01 and PR.DS-10 coverage, key-custodian assignments and the irreversibility properties of the chosen primitives can demonstrate ex post, against the Art. 5(2) accountability threshold, that the risk-based level of security chosen under the Art. 32(1) preamble was actually delivered.
  ambiguity_notes: |
    Art. 5(1)(f) and Art. 4(1) carry S3 ambiguity. On "appropriate" (VAG), the chosen reading anchors the term to the Art. 32(1) risk-based test: the controller documents the chosen security level against the five risk factors in the Art. 32(1) preamble and refreshes this assessment when material change occurs. An alternative reading, supported by industry practice under ISO 27001 and SOC 2 frameworks, treats "appropriate technical and organisational measures" as requiring both control families in parallel, regardless of risk; this is the more conservative reading and is the de facto baseline for any organisation holding formal certification. A third, looser reading treats "appropriate" as whatever the controller self-declares, which does not survive supervisory inspection but is sometimes observed in pre-DPO controllers. The chosen reading here is the inclusive risk-anchored reading, which is consistent with EDPB Guidelines on accountability 07/2019. On "personal data" (POLY/SCOPE-Q per Art. 4(1)), the scope of "identifiable" is read in line with CJEU Breyer C-582/14 §45, which adopts a "means likely reasonably to be used" test. This reading brings pseudonymous data into scope where re-identification is operationally feasible, but leaves genuinely anonymous data outside. EDPB Guidelines 05/2020 on consent §3.4 reinforce this position. A broader reading, extending to inferred and derived data subject to algorithmic singling-out, has been gaining traction post-IAB Europe C-604/22 but is not yet definitively settled. On the "technical or organisational" disjunction (COORD), the chosen reading treats the OR as inclusive, in line with the dominant grammatical reading and consistent with EDPB Guidelines on Art. 32; controllers following the strict reading are equally compliant. Remain open: (a) whether forward-looking cryptographic-agility (quantum-readiness) is required by "state of the art" under Art. 32(1), pending EDPB clarification and ENISA post-quantum guidance; and (b) how the resilience dimension of Art. 32(1)(b) interacts with separate BCDR obligations, pending cross-regulation alignment with DORA Art. 11–12 and NIS 2 Art. 21(2)(c).
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-002
  title: "In-transit confidentiality across networks and inter-service channels"
  source_clauses:
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b)" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-001, SO-GDPR-030]
  sub_domain: [D-01.1, D-01.2, D-10.1]
  nist_csf_mapping:
    - { id: PR.DS-02, title: "Data-in-transit protected" }
    - { id: PR.IR-01, title: "Networks protected from unauthorized logical access" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(b) lists as one of the security measures the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services. The Art. 32(1) preamble anchors this to the risk-based test (state of the art, costs of implementation, nature, scope, context, purposes, and risks of varying likelihood and severity). Art. 32(2) re-anchors the obligation by requiring that, in assessing the appropriate level of security, account shall be taken in particular of the risks that are presented by processing, in particular from accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed. Read together, these provisions extend the Art. 5(1)(f) CIA obligation to the network and transport layers: data that leaves the controller's storage perimeter and traverses third-party infrastructure must remain confidential and unaltered in transit, and the five-event risk enumeration provides a structured threat-modelling checklist against which in-transit controls are assessed. In practice, this is the textual basis for encryption-in-transit (TLS, IPsec, application-layer encryption), network segmentation, and logical-access controls on inter-service communications.
  security_rationale: |
    The obligation in Art. 32(1)(b) and Art. 32(2) to preserve the confidentiality and integrity of personal data as it traverses networks and third-party infrastructure is operationalised in NIST CSF 2.0 through **PR.DS-02 (Data-in-transit protected)** and **PR.IR-01 (Networks protected from unauthorized logical access)**.
    PR.DS-02 anchors the cryptographic and integrity-protection controls applied to data in motion, satisfying the Art. 32(2) risk events of unauthorised disclosure, alteration and access on the transport layer where published incident data shows the most frequent breach vector.
    PR.IR-01 captures the complementary logical-access dimension, recognising that transit-layer confidentiality is meaningless if endpoints are reachable from unauthorised network positions; the two subcategories work in concert to close both the in-flight tampering gap and the lateral-movement gap that the Art. 32(2) five-event enumeration presupposes.
    A controller that documents PR.DS-02 channel coverage and PR.IR-01 segmentation policy can demonstrate ex post, under the Art. 5(2) accountability duty, that the in-transit controls chosen under the Art. 32(1) risk-based preamble were proportionate and actually in force on the day of any incident.
  ambiguity_notes: |
    GDPR-CP16 (Art. 32(2)) carries S3 COORD ambiguity on the five-way OR of risk events. Reading chosen: any of the five events triggers the security assessment and the corresponding in-transit control. An alternative reading, treating the five events as illustrative and letting the controller judge which events trigger obligations, would not change the in-transit confidentiality requirement in practice but would weaken the threat-modelling discipline. The five events (destruction, loss, alteration, unauthorised disclosure, access) overlap with but are not identical to the Art. 4(12) personal-data-breach definition, which adds "disclosure of" as a stand-alone event; controllers should map both lists to ensure no event is dropped from the threat model. On the "as appropriate" hedge in Art. 32(1) ("including inter alia as appropriate"), the chosen reading treats the four sub-letters (a)–(d) as the floor of expected measures rather than a closed list, with controllers free to add further measures proportionate to risk. Remain open: (a) whether end-to-end encryption (originator-to-destination) is required for all intra-processor flows under Art. 32(1)(b) or only link-encryption (hop-by-hop), pending EDPB clarification; and (b) how the "transmitted" wording of Art. 32(2) applies to data-in-use during query execution across microservices, pending alignment with ISO 27018 and ENISA guidance on confidential computing.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-003
  title: "Pseudonymisation and encryption with key separation"
  source_clauses:
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(a)" }
    - { clause_id: GDPR-C02, article_ref: "Art. 4(5) — pseudonymisation definition" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-002]
  sub_domain: [D-01.1, D-01.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(a) names pseudonymisation and encryption of personal data as illustrative appropriate technical measures that the controller and processor shall implement under the Art. 32(1) risk-based preamble. Art. 4(5) defines pseudonymisation as the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to appropriate technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person. Read together, the two provisions establish that pseudonymisation is a recognised security technique and that the de-attribution requirement (plus the additional-information-kept-separately obligation) is the operational test. The definition does not specify which technical mechanisms qualify; the OJ text is silent on tokenisation, deterministic hashing, format-preserving encryption, and other reversible-identification mechanisms.
  security_rationale: |
    The obligation in Art. 32(1)(a), read with the Art. 4(5) pseudonymisation definition, to apply pseudonymisation and encryption with the additional information kept separately is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)**.
    PR.DS-01 anchors the cryptographic and tokenisation controls applied to stored personal data, the dominant attack surface for pseudonymised datasets; it directly satisfies the Art. 4(5) de-attribution requirement because, once the additional information (the mapping table or cryptographic key) is held under separate technical and organisational control, compromise of the storage layer no longer yields re-identifiable plaintext.
    The CSF 2.0 framing treats this as a confidentiality, integrity and availability property of the data-at-rest asset rather than as a point mechanism, which aligns with the Art. 32(1) risk-based preamble: the controller scales the primitive strength and the key-separation rigour to the five risk factors rather than declaring a fixed level ex ante.
    Although only one CSF subcategory is mapped, PR.DS-01 carries the full weight of the blast-radius-reduction pattern that pseudonymisation provides.
    A controller documenting PR.DS-01 coverage, separation-of-duties in key custody and the qualification test applied to each mechanism can demonstrate ex post, under Art. 5(2), that the Art. 32(1)(a) measure was genuinely implemented rather than merely declared.
  ambiguity_notes: |
    Art. 4(5) defines pseudonymisation operationally but does not specify which technical mechanisms count. Reading chosen: any mechanism meeting the Art. 4(5) additional-information-kept-separately test qualifies, including tokenisation, deterministic hashing, format-preserving encryption, and key-segregated encryption where the additional-information-equivalent (the key or mapping table) is stored under separate technical and organisational control. The definition carries S2 POLY; both readings converge on the de-identification requirement. EDPB Guidelines 05/2020 on consent §3.4 treat pseudonymised data as still personal data within scope of GDPR, which the chosen reading incorporates: pseudonymisation is a security measure, not a scope-exclusion technique. Remain open: whether one-way hashing with no realistic pre-image recovery (i.e. effectively anonymous output) falls inside the Art. 4(5) definition or constitutes anonymisation outside GDPR, pending CJEU guidance on the Single-Sign-On cookie cases (IAB Europe C-604/22) and the Breyer line.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-004
  title: "Cryptographic unintelligibility for breach-notification carve-out"
  source_clauses:
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a) — unintelligibility exception" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(a)" }
  linked_objectives: [SO-GDPR-002]
  sub_domain: [D-01.3, D-04.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.IR-03, title: "Resilience requirements in normal and adverse situations" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 34(3)(a) provides that the communication of a personal data breach to the data subject shall not be required if the controller has implemented appropriate technical and organisational protection measures, and those measures were applied to the personal data affected by the personal data breach, in particular those that render the personal data unintelligible to any person who is not authorised to access it, such as encryption. Art. 32(1)(a) supplies the underlying measure, listing pseudonymisation and encryption among the technical measures the controller and processor shall implement. Read together, the two provisions operationalise the cryptographic-protection carve-out from the data-subject notification duty: if the breached data was encrypted with sufficient key separation that the adversary cannot recover plaintext, the high-risk threshold for notification under Art. 34(1) is treated as not materialised. Two textual conditions matter for compliance. First, the protection measures must have been applied to the data actually affected by the breach, not merely to the data generally. Second, "render unintelligible to any person who is not authorised to access it" is the operational standard, which requires that the cryptographic key be unavailable to any party outside the controller's authorised set.
  security_rationale: |
    The obligation in Art. 34(3)(a), read with Art. 32(1)(a), to render breached personal data unintelligible to any unauthorised person through cryptographic key separation is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.IR-03 (Resilience requirements in normal and adverse situations)**.
    PR.DS-01 anchors the cryptographic protection applied to the affected dataset, satisfying the Art. 34(3)(a) unintelligibility standard by making the cryptographic key, rather than the storage layer, the trust anchor that a competent adversary cannot recover within operationally-relevant resources.
    PR.IR-03 captures the resilience dimension that the carve-out presupposes: key-escrow recovery without compromising separation, key rotation without service degradation, and recovery to a known-good state after the adverse event, all of which must hold for the cryptographic protection to remain effective on the day of the breach.
    The two subcategories together operationalise the zero-trust assumption that the storage layer will be breached, so that breach alone is insufficient to cause plaintext exfiltration.
    A controller documenting PR.DS-01 key-custody assignments, PR.IR-03 rotation cadence and the irreversibility of the chosen primitive can demonstrate ex post, under Art. 5(2), that the Art. 34(3)(a) carve-out was genuinely earned rather than asserted.
  ambiguity_notes: |
    Source clause GDPR-CP20 (Art. 34(3)(a)) carries S3 VAG ambiguity on `unintelligible`. Reading chosen: unintelligibility is achieved when a competent cryptographic adversary without the relevant key cannot recover plaintext within operationally-relevant resources. This reading is anchored to Recital 49 (non-binding but directionally useful), to EDPB Guidelines 9/2022 §3.5, and to ISO 27001 A.10.1.2 key-management expectations. An alternative reading treats "unintelligible" as satisfied by any form of access control (including password-protected files), which is incompatible with the Art. 34(3)(a) "such as encryption" anchor and would not survive supervisory inspection. A third reading admits post-quantum-uncertain primitives, which is rejected: the operative standard is present-day cryptanalytic feasibility. Remain open: (a) whether controller-controlled HSMs with key-recovery held by a trustee satisfy the "not authorised to access" condition when the trustee is contractually bound to the controller, pending EDPB clarification; and (b) whether backup tapes encrypted under a long-term key that the controller retains indefinitely fall inside the carve-out or trigger notification under Art. 34(1).
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-007
  title: "Periodic testing of security control effectiveness"
  source_clauses:
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(d)" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — appropriate security" }
  linked_objectives: [SO-GDPR-004]
  sub_domain: [D-10.3, D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities identified, validated, recorded" }
    - { id: PR.PS-02, title: "Software maintained commensurate with risk" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Art. 32(1)(d) requires the controller and processor to implement, among the security measures listed in Art. 32(1), a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing. The Art. 32(1) preamble anchors the choice and cadence of testing to the risk-based factors (state of the art, costs of implementation, nature, scope, context, purposes, risks of varying likelihood and severity). Art. 5(1)(f) supplies the underlying principle. The provision is operational rather than discretionary: the existence of a testing process is the regulatory expectation, and its adequacy is judged against the Art. 32(1) preamble factors.
  security_rationale: |
    The obligation in Art. 32(1)(d), read with Art. 5(1)(f), to operate a process for regularly testing, assessing and evaluating the effectiveness of security measures is operationalised in NIST CSF 2.0 through **ID.RA-01 (Vulnerabilities identified, validated, recorded)** and **PR.PS-02 (Software maintained commensurate with risk)**.
    ID.RA-01 anchors the vulnerability-identification lifecycle — scanning, validation, recording and prioritisation — that the Art. 32(1)(d) testing process must produce, satisfying the regulatory expectation that controls are actively proven rather than assumed.
    PR.PS-02 captures the corrective leg of the same cycle: software and platforms maintained, replaced and removed in step with the risk profile, closing the loop that ID.RA-01 opens and ensuring that detected decay is actually remediated rather than logged and forgotten.
    Together the two subcategories cover the test-assess-evaluate triad in Art. 32(1)(d), with cadence and depth scaled to the five risk factors in the Art. 32(1) preamble rather than fixed by a hard numeric interval.
    A controller documenting ID.RA-01 scan and penetration-test results, PR.PS-02 patch cadence and the control-effectiveness audit trail can demonstrate ex post, under Art. 5(2), that the periodic-testing process required by Art. 32(1)(d) was genuinely operated and remained proportionate to the processing risk.
  ambiguity_notes: |
    Source clause GDPR-CP15 (Art. 32(1)(d)) carries no S3 ambiguity on `regularly` in the operative sense. The rule anchors the operational meaning to period and versioning adequacy rather than to a hard numeric interval: a controller running monthly vulnerability scans and an annual third-party penetration test against critical systems satisfies the obligation, and so does a controller running continuous testing with weekly triage, provided the cadence is documented and proportionate. Both readings (more frequent vs less frequent) converge on the obligation to test periodically. The risk-based preamble handles under- or over-testing for the controller's specific context. EDPB Guidelines 7/2019 on certification provide a non-binding framework for cadence but do not bind the controller.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-008
  title: "DPIA and risk-profile review on material change"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(11) — DPIA review" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(d)" }
  linked_objectives: [SO-GDPR-004, SO-GDPR-028]
  sub_domain: [D-09.2, D-10.3, D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Inherent risk understood via threats/vulnerabilities/likelihood/impact" }
    - { id: ID.IM-02, title: "Improvement processes implemented across organizational tiers" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PERIODIC, TRIGGERED]
  regulatory_rationale: |
    Art. 35(11) requires the controller, where necessary, to carry out a review to assess whether processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations. Combined with Art. 32(1)(d), which mandates the regular testing, assessing and evaluating of the effectiveness of security measures, this creates a continuous-improvement obligation for security-relevant processing: the DPIA is not a one-off deliverable but a living artefact refreshed on material change. The two provisions differ in trigger: Art. 32(1)(d) is periodic (cadence-anchored), Art. 35(11) is triggered (change-anchored), and the controller must operate both in parallel.
  security_rationale: |
    The obligation in Art. 35(11), read with Art. 32(1)(d), to keep the DPIA and the security-control assessment under periodic and triggered review is operationalised in NIST CSF 2.0 through **ID.RA-05 (Inherent risk understood via threats, vulnerabilities, likelihoods, impacts)** and **ID.IM-02 (Improvement processes implemented across organizational tiers)**.
    ID.RA-05 anchors the risk-reassessment method that uses threats, vulnerabilities, likelihoods and impacts to recompute inherent risk, satisfying the Art. 35(11) change-of-risk trigger and supplying the evidence base for the Art. 32(1)(d) periodic evaluation.
    ID.IM-02 captures the continuous-improvement layer: improvement processes implemented across organisational tiers, ensuring that reassessment outputs actually feed back into control updates rather than accumulating as static documents.
    The two subcategories together cover both the periodic (cadence-anchored) and triggered (change-anchored) review modes that Art. 35(11) and Art. 32(1)(d) impose in parallel, with the controller maintaining a living DPIA register rather than a one-off deliverable.
    A controller documenting ID.RA-05 reassessment records, ID.IM-02 improvement-cycle evidence and the change triggers that prompted each review can demonstrate ex post, under Art. 5(2), that the DPIA and the security posture were kept current against the evolving risk landscape.
  ambiguity_notes: |
    GDPR-CP22 (Art. 35(11)) carries no S3 ambiguity in the operative clause. `where necessary` and `change of the risk represented` are acknowledged Berry VAG; both readings converge on the obligation to reassess when the risk profile changes. The triggering "change" is documented in the controller's change-management policy and includes: change in processing purpose (Art. 6(4) compatibility), change in data categories (especially Art. 9 special categories), change in data-subject population (volume or vulnerability), change in technical context (new processor, new third country), and change in regulatory expectation (new EDPB guidance). EDPB Guidelines 4/2019 on DPIA provide non-binding factors for materiality but do not bind the controller.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-009
  title: "Proportionate identity verification for rights requests"
  source_clauses:
    - { clause_id: GDPR-RT04, article_ref: "Art. 12(6) — identity verification" }
    - { clause_id: GDPR-CL26, article_ref: "Art. 11(2) — identification exemption" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data (cross)" }
  linked_objectives: [SO-GDPR-005]
  sub_domain: [D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-03, title: "Users, services, and hardware authenticated" }
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 12(6) permits the controller, where the controller has reasonable doubts concerning the identity of the natural person making a request under Art. 15–22, to request the additional information necessary to confirm the identity of the data subject. Art. 11(2) preserves data-subject rights where the data subject provides additional information enabling identification, anchoring the reciprocal obligation: the data subject must supply enough information to be identified if they wish to exercise the rights. Art. 4(1) defines the data-subject scope (any information relating to an identified or identifiable natural person). Read together, the three provisions establish a proportionate verification standard: the controller may verify, but only to the extent necessary, and the data subject retains the right if they can complete the identification loop.
  security_rationale: |
    The obligation in Art. 12(6), read with Art. 11(2), to verify the identity of a data subject exercising rights only to the extent necessary is operationalised in NIST CSF 2.0 through **PR.AA-03 (Users, services, and hardware authenticated)** and **PR.AA-02 (Identities proofed and bound to credentials)**.
    PR.AA-03 anchors the authentication of the requesting party at the rights-request endpoint, satisfying the Art. 12(6) reasonable-doubts trigger by ensuring that personal data is not released to an imposter — a social-engineering vector that bypasses perimeter controls entirely.
    PR.AA-02 captures the identity-proofing leg, binding the asserted identity to credentials proportionate to the context of the interaction, which maps directly onto the graduated verification standard (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk).
    The two subcategories together operationalise the proportionate verification model that Art. 12(6) imposes, calibrated by Art. 5(1)(c) data minimisation so that the verification step itself does not become a new attack surface of accumulated identity documents.
    A controller documenting PR.AA-03 authentication decisions, PR.AA-02 proofing evidence and the risk-based escalation tree per request type can demonstrate ex post, under Art. 5(2), that identity verification was both sufficient to prevent impersonation and no more intrusive than necessary.
  ambiguity_notes: |
    Source clause GDPR-RT04 (Art. 12(6)) carries S3 VAG on `reasonable doubts` and `additional information`. Reading chosen: the controller may request minimal identity verification proportionate to the risk of misidentification, not arbitrary additional documents. This reading is anchored to Art. 5(1)(c) data minimisation (no over-collection) and to EDPB Guidelines on Art. 12 transparency. An alternative reading requiring full ID-document collection on any doubt is rejected: it creates a new attack surface (the collected ID documents themselves) and is disproportionate under Art. 5(1)(c). A third reading that mandates accepting self-declaration on any doubt is also rejected: it exposes the data-subject rights endpoint to social-engineering attacks and breaches the controller's Art. 32(1)(b) confidentiality obligation. On Art. 11(2), the `additional information` polysemy (information the controller must NOT maintain vs information the data subject must supply) is resolved by treating the data-subject-supply sense as the operative one for rights-exercise workflows. Remain open: (a) whether knowledge-based authentication (KBA) questions over personal-data history are acceptable as `additional information`, pending EDPB guidance post-Schrems II; and (b) how the verification obligation scales with self-service authentication (e.g. OAuth from a verified identity provider), pending alignment with eIDAS 2.0.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-011
  title: "Instruction-bound processing under least-privilege authorisation"
  source_clauses:
    - { clause_id: GDPR-CP11, article_ref: "Art. 29 — processing under authority" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(4)" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(a)/(b)" }
    - { clause_id: GDPR-C03, article_ref: "Art. 4(7)/(8) — controller/processor definitions" }
  linked_objectives: [SO-GDPR-006]
  sub_domain: [D-03.3]
  nist_csf_mapping:
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
    - { id: PR.AA-06, title: "Access limited to authorized users/services/hardware" }
  applies_to_role: [PROCESSOR, AUTHORISED_PERSONNEL]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority by requiring the controller and processor to take steps to ensure that any such natural person does not process the data except on instructions. Art. 28(3)(a) and (b) provide the contractual foundation, requiring the processor contract to stipulate that the processor processes the personal data only on documented instructions from the controller and that persons authorised to process the personal data have committed themselves to confidentiality. Art. 4(7) and 4(8) define controller and processor, anchoring who is subject to whom. Read together, the provisions establish a chain-of-authority pattern: controller → processor → authorised persons, with documented instructions binding each link and Union or Member State law as the only exception.
  security_rationale: |
    The obligation in Art. 29, read with Art. 32(4) and Art. 28(3)(a)/(b), to restrict processing by natural persons under the controller's or processor's authority to documented instructions is operationalised in NIST CSF 2.0 through **PR.AA-05 (Access permissions managed per least privilege)** and **PR.AA-06 (Access limited to authorized users, services, and hardware)**.
    PR.AA-05 anchors the least-privilege authorisation model that maps each authorised person to a scope defined by documented instructions, satisfying the Art. 29 instruction-only rule at the access-control layer and making every act of processing traceable to an instruction in the Art. 28(3)(a) contract.
    PR.AA-06 captures the boundary-enforcement leg: physical and logical access limited to those authorised users, services and hardware, closing the gap that least-privilege definitions alone leave open by ensuring the scope is actually enforced rather than merely declared.
    The two subcategories together operationalise the chain-of-authority pattern (controller to processor to authorised persons) that Arts. 29 and 28(3) establish, with Union or Member State law as the only exception.
    A controller documenting PR.AA-05 permission assignments, PR.AA-06 access-enforcement evidence and the instructions register can demonstrate ex post, under Art. 5(2), that processing outside documented authority was technically prevented and auditably detectable.
  ambiguity_notes: |
    `instructions` is POLY-S2 (formal written vs verbal vs workflow-implied). Reading chosen: instructions must be documented in a form sufficient for audit and supervisory-authority inspection, at minimum the documented instruction in the Art. 28(3)(a) processor contract and any operational instructions issued under it. An alternative reading allowing verbal instructions (provided they are recorded contemporaneously) is acceptable but operationally weaker. A third reading permitting workflow-implied instructions (e.g. processing required by the controller's API) is rejected: workflows are evidence of processing but not a substitute for the documented instruction; controllers must translate workflow-level processing into documented instructions for Art. 28(3)(a) compliance. The Union or Member State law carve-out is narrow and typically arises in law-enforcement, tax, and social-security contexts.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-012
  title: "Confidentiality undertakings for authorised personnel"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(b) — confidentiality obligation" }
    - { clause_id: GDPR-CP11, article_ref: "Art. 29" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(4)" }
  linked_objectives: [SO-GDPR-006]
  sub_domain: [D-03.3, D-08.1]
  nist_csf_mapping:
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
    - { id: PR.AT-02, title: "Workforce understands their role-specific security responsibilities" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality. Art. 29 reinforces this by binding natural persons acting under the authority of controller or processor to instruction-only processing. Art. 32(4) reinforces this for natural persons acting under controller/processor authority. Read together, the provisions create a confidentiality ring around any natural person who accesses personal data on behalf of the controller or processor, with contractual or statutory confidentiality as the binding mechanism. The confidentiality obligation is independent of the instruction obligation: a person acting on instructions still owes confidentiality, and breach of confidentiality is breach of the Art. 28(3)(b) contract term.
  security_rationale: |
    The obligation in Art. 28(3)(b), read with Art. 29 and Art. 32(4), to bind every natural person accessing personal data to a confidentiality undertaking is operationalised in NIST CSF 2.0 through **PR.AA-05 (Access permissions managed per least privilege)** and **PR.AT-02 (Workforce understands role-specific security responsibilities)**.
    PR.AA-05 anchors the access-permission layer that enforces the scope each confidentiality undertaking covers, ensuring the contractual or statutory duty is backed by a technical control preventing access beyond the documented need rather than resting on trust alone.
    PR.AT-02 captures the awareness dimension: workforce members understanding their specific confidentiality and security responsibilities, which maps directly onto the onboarding, register and refresh cycle that Art. 28(3)(b) imposes and that gives the undertaking operational substance.
    The two subcategories together operationalise the confidentiality ring that Arts. 28(3)(b) and 32(4) create around any natural person handling personal data, combining the legal-policy lever with the technical-enforcement lever.
    A controller documenting PR.AA-05 scope assignments, PR.AT-02 signed-undertaking register and the refresh cadence per authorised person can demonstrate ex post, under Art. 5(2), that the confidentiality obligation was both contractually imposed and operationally reinforced.
  ambiguity_notes: |
    `appropriate statutory obligation of confidentiality` is VAG-S2. Reading chosen: an obligation equivalent in scope to a contractual NDA covering the personal data scope. An alternative reading accepting any pre-existing statutory professional-secrecy obligation (e.g. medical or legal privilege) is acceptable where the person actually operates under such an obligation. A third reading that no obligation is required where the person is a public-sector employee with existing secrecy duties under Member State law is acceptable in narrow contexts. The "appropriate" qualifier is calibrated to the data sensitivity and the role's exposure.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-014
  title: "Continuous breach detection enabling the 72-hour clock"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — 72-hour notification trigger" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b) — confidentiality of processing systems" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach definition" }
  linked_objectives: [SO-GDPR-008]
  sub_domain: [D-04.1, D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks monitored for potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware/software/runtime/data monitored" }
    - { id: RS.MA-02, title: "Incident reports triaged and validated" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services, which is achieved only if monitoring is in place to detect personal data breaches (Art. 4(12) defines a personal data breach as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed). Art. 33(1) creates the 72-hour clock from the moment of becoming aware; awareness requires detection capability. Read together, the provisions establish that continuous security monitoring is the regulatory foundation for the entire incident-response chain: no detection, no awareness, no notification, and no compliance with the 72-hour clock. The obligation is continuous because the threat surface is continuous; the obligation is on the controller and processor, jointly, because detection is layered.
  security_rationale: |
    The obligation in Art. 32(1)(b), read with Art. 33(1) and Art. 4(12), to detect personal data breaches and so start the 72-hour awareness clock is operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks monitored for potentially adverse events)**, **DE.CM-09 (Computing hardware, software, runtime and data monitored)** and **RS.MA-02 (Incident reports triaged and validated)**.
    DE.CM-01 anchors the network-layer monitoring that surfaces unauthorised disclosure and exfiltration, the most frequent breach vectors in published incident data, satisfying the Art. 4(12) disclosure and access events at the transport layer.
    DE.CM-09 captures the host-and-data monitoring that detects the remaining Art. 4(12) events — alteration via integrity monitoring, destruction and loss via availability monitoring — across the runtime environments where personal data actually resides.
    RS.MA-02 closes the chain by triaging and validating detected events into declared incidents, supplying the documented awareness moment that Art. 33(1) requires for the clock to start.
    A controller documenting DE.CM-01 and DE.CM-09 coverage tuned to the five Art. 4(12) events and RS.MA-02 triage records can demonstrate ex post, under Art. 5(2), that the 72-hour clock was started from a genuine, auditable detection event rather than from informal awareness.
  ambiguity_notes: |
    `becoming aware` (Art. 33(1)) carries POLY-S3. Reading chosen: documented awareness by a controller employee with delegated breach-handling responsibility, the moment the breach is captured by the controller's detection capability. An alternative reading that awareness attaches whenever any employee becomes aware, including informally, is rejected because it would force an unreasonably early clock and is inconsistent with how organisations actually triage. A third reading that awareness occurs only when senior management is formally briefed is too late and creates compliance risk. The chosen reading is consistent with EDPB Guidelines 9/2022 §3.4 and aligns with the controller's documented incident-response procedure. Operationally, controllers designate a breach-handling role, document the awareness moment, and timestamp detection events to support the 72-hour clock calculation. Remain open: (a) whether AI-driven anomaly detection that flags a breach but does not escalate within the controller's documented procedure still constitutes "awareness", pending EDPB guidance on automated detection; and (b) how the awareness moment is established when the breach is detected by a sub-processor rather than the controller, pending alignment with Art. 33(2) processor notification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-015
  title: "Post-breach containment, mitigation, and remediation runbooks"
  source_clauses:
    - { clause_id: GDPR-CP18, article_ref: "Art. 33(3)(d) — measures taken or proposed" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a)/(b) — measures to render data unintelligible / subsequent measures" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(d) — testing" }
  linked_objectives: [SO-GDPR-009]
  sub_domain: [D-04.2]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents contained" }
    - { id: RS.MI-02, title: "Incidents mitigated" }
    - { id: PR.DS-01, title: "Data-at-rest protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 34(3)(a) and (b) provide that subsequent measures rendering the personal data unintelligible or eliminating the high risk are valid exceptions to the data-subject notification under Art. 34(1). Art. 32(1)(d) reinforces the testing and evaluating discipline. Read together, the provisions operationalise defence-in-depth after a breach: short-term containment, mid-term mitigation, and long-term remediation, with the reporting obligation under Art. 33(3)(d) covering both taken and proposed measures, and the Art. 34(3) exceptions providing notification carve-outs where mitigation is sufficient.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects]
  security_rationale: |
    The obligation in Art. 33(3)(d), read with Art. 34(3)(a)/(b) and Art. 32(1)(d), to contain, mitigate and remediate a personal data breach is operationalised in NIST CSF 2.0 through **RS.MI-01 (Incidents contained)**, **RS.MI-02 (Incidents mitigated)** and **PR.DS-01 (Data-at-rest protected)**.
    RS.MI-01 anchors the short-term containment runbook — isolating affected systems, revoking credentials, blocking exfiltration paths — that Art. 33(3)(d) requires the controller to report as measures taken, satisfying the operational halt of active harm.
    RS.MI-02 captures the mid-term mitigation that Art. 34(3)(b) presupposes: re-encrypting data under new keys, resetting affected credentials, patching the exploited vulnerability, and demonstrating that the high risk is no longer likely to materialise.
    PR.DS-01 supplies the cryptographic foundation that makes both containment and mitigation auditable, by ensuring that the post-breach state of the affected dataset is itself protected against re-compromise.
    A controller documenting RS.MI-01 containment actions, RS.MI-02 mitigation evidence and PR.DS-01 post-remediation key state can demonstrate ex post, under Art. 5(2), that the Art. 33(3)(d) measures were actually taken and that any Art. 34(3) carve-out was genuinely earned.
  ambiguity_notes: |
    Art. 34(3)(a) carries VAG-S3 on `unintelligible` (see SR-GDPR-004 for chosen reading). All readings converge on the operational containment and mitigation obligation. The `where appropriate` hedge in Art. 33(3)(d) is read as the controller's reasonable judgement on whether mitigation measures exist and are material; it is not a discretion to omit the field. Art. 34(3)(b) `subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise` is the harder threshold: the controller must demonstrate that mitigation actually neutralises the high risk, not merely that mitigation was attempted. Remain open: (a) whether the controller's notification to the supervisory authority under Art. 33(3)(d) must include proposed measures when containment is still in progress, or only taken measures with a separate proposed-measures addendum, pending EDPB guidance; and (b) how the mitigation obligation applies to breaches that originate at a sub-processor, pending alignment with Art. 33(2) processor notification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-016
  title: "72-hour breach notification to the supervisory authority"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — 72-hour notification" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
    - { clause_id: GDPR-C09, article_ref: "Art. 4(22) — supervisory authority concerned" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: RS.CO-04, title: "Coordination with stakeholders consistent with applicable rules" }
    - { id: RS.MA-03, title: "Incidents categorized, prioritized, and scoped" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons. Art. 4(12) defines the trigger event (personal data breach), Art. 32(2) anchors the five-event risk enumeration underlying the risk assessment, and Art. 4(22) anchors which supervisory authority is "competent" (the lead authority under Art. 56 one-stop-shop, or the local authority where the controller's main establishment is located). Read together, the provisions establish a twin temporal anchor (without undue delay + 72 hours) with a risk-based carve-out, directed to the competent supervisory authority. Where the notification is made after the 72-hour window, Art. 33(1) requires reasons for the delay.
  security_rationale: |
    The obligation in Art. 33(1), read with Art. 4(12), Art. 32(2) and Art. 4(22), to notify the competent supervisory authority within 72 hours of awareness is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)**, **RS.CO-04 (Coordination with stakeholders consistent with applicable rules)** and **RS.MA-03 (Incidents categorized, prioritized, and scoped)**.
    RS.MA-03 anchors the triage that establishes whether the Art. 4(12) breach definition is met and whether the risk threshold engages the notification duty, supplying the categorised and scoped incident record that the 72-hour clock depends on.
    RS.CO-02 captures the internal escalation to executive leadership and legal counsel that precedes the external notification, ensuring the controller's decision chain is documented and defensible.
    RS.CO-04 closes the loop with the coordination to the competent supervisory authority under Art. 55, consistent with the applicable rules and the Art. 4(22) one-stop-shop determination.
    A controller documenting RS.MA-03 triage, RS.CO-02 escalation and RS.CO-04 authority coordination can demonstrate ex post, under Art. 5(2), that the notification was timely, addressed to the correct authority, and supported by reason-for-delay evidence where the window was exceeded.
  ambiguity_notes: |
    `without undue delay and, where feasible, not later than 72 hours` carries S3 VAG+SCOPE on the double temporal anchor. Reading chosen: 72 hours is the hard ceiling; `without undue delay` requires action immediately upon awareness; `where feasible` is a narrow, technical-feasibility exception (e.g. forensic preservation in progress, key personnel unavailable through the night). The threshold `unlikely to result in a risk` is interpreted via EDPB Guidelines 9/2022 as the precautionary principle: notification is required unless the controller can demonstrate that the breach is unlikely to result in a risk, and the demonstration burden rests with the controller. An alternative reading that controller judgement suffices with no demonstration required is rejected because it inverts the burden and is inconsistent with EDPB practice. Remain open: (a) whether the 72-hour clock resets on material new information about the same breach, or runs continuously from initial awareness, pending EDPB clarification; and (b) how the `where feasible` exception applies when the controller is in a multi-jurisdictional incident with different working hours, pending alignment with NIS 2 incident-handling timelines.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-019
  title: "High-risk breach communication to affected data subjects"
  source_clauses:
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk breach communication to data subject" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(2) — content of communication" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration (cross)" }
  linked_objectives: [SO-GDPR-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated stakeholders per information-sharing rules" }
    - { id: RS.CO-04, title: "Coordination with stakeholders consistent with applicable rules" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(1) requires the controller to communicate a personal data breach to the data subject without undue delay when the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons. Art. 34(2) requires the communication to describe in clear and plain language the nature of the personal data breach and contain at least the information and measures referred to in points (b), (c) and (d) of Art. 33(3). Art. 32(2) anchors the risk-enumeration vocabulary (destruction, loss, alteration, unauthorised disclosure of, or access to) underlying the high-risk assessment. Read together, the provisions establish a higher threshold (high risk to data subjects' rights) than the supervisory-authority notification (Art. 33, risk to data subjects' rights), and a content requirement scoped to the data subject rather than the supervisory authority.
  security_rationale: |
    The obligation in Art. 34(1), read with Art. 34(2) and Art. 32(2), to communicate a high-risk breach to affected data subjects in clear and plain language is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information shared with designated stakeholders per information-sharing rules)** and **RS.CO-04 (Coordination with stakeholders consistent with applicable rules)**.
    RS.CO-03 anchors the information-sharing mechanism that delivers the Art. 34(2) content — nature of the breach, likely consequences, measures taken — to the data subjects whom the rules designate as the entitled stakeholders, satisfying the higher Art. 34 threshold that sits above the Art. 33 supervisory-notification trigger.
    RS.CO-04 captures the coordination discipline that multi-channel notification (direct communication, prominent website notice and, where appropriate, public communication) requires, ensuring the communication achieves equally effective reach and that the high-risk classification decision tree is documented.
    The two subcategories together operationalise the data-subject-facing leg of breach response, distinct from the authority-facing leg, enabling individual protective action such as account rotation and fraud-alert subscription.
    A controller documenting RS.CO-03 notification records, RS.CO-04 channel-choice evidence and the high-risk assessment per EDPB Guidelines 9/2022 can demonstrate ex post, under Art. 5(2), that affected data subjects received timely, intelligible notice enabling protective action.
  ambiguity_notes: |
    `likely to result in a high risk` carries POLY+VAG-S3 (the three-tier `risk`/`high risk`/`high risk` architecture across Arts. 33, 34, 35). Reading chosen: the Art. 34 threshold is higher than the Art. 33 threshold — objectively elevated above ordinary processing risk, per EDPB Guidelines 9/2022. An alternative reading treating the threshold as severe impact on data subject's rights, per CNIL guidance, is operationally similar but framing-different. The chosen reading treats the threshold as risk-of-significant-harm, not merely risk-of-any-harm; the controller documents the risk assessment with reference to the data categories (Art. 9 special categories raise the threshold), the data-subject population (vulnerable populations raise the threshold), and the breach characteristics (encrypted vs plaintext, contained vs ongoing). Remain open: (a) whether `clear and plain language` requires a CEFR B1 reading-age standard or whether national DPA guidance is acceptable, pending EDPB harmonisation; and (b) whether the Art. 34 communication can be combined with Art. 33 notification to the supervisory authority, or must be a separate communication, pending EDPB Guidelines 9/2022 clarification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-024
  title: "Timely availability restoration after physical or technical incident"
  source_clauses:
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(c) — timely restore" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — integrity & confidentiality (cross)" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
  linked_objectives: [SO-GDPR-014]
  sub_domain: [D-04.4]
  nist_csf_mapping:
    - { id: PR.IR-04, title: "Adequate resource capacity to ensure availability maintained" }
    - { id: PR.DS-11, title: "Backups created, protected, maintained, tested" }
    - { id: RC.RP-04, title: "Critical mission functions restored through recovery plan" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident. Art. 5(1)(f) supplies the integrity-and-confidentiality cross-reference, and Art. 32(2) anchors the five-event risk enumeration underlying the trigger assessment. Read together, the provisions establish a recovery-and-restore obligation: the controller and processor must be able to bring availability and access back to a defined state within a timeframe appropriate to the processing context, and the ability must be tested.
  security_rationale: |
    The obligation in Art. 32(1)(c), read with Art. 5(1)(f) and Art. 32(2), to restore the availability of and access to personal data in a timely manner after a physical or technical incident is operationalised in NIST CSF 2.0 through **PR.IR-04 (Adequate resource capacity to ensure availability)**, **PR.DS-11 (Backups created, protected, maintained, and tested)** and **RC.RP-04 (Critical mission functions restored through recovery plan)**.
    PR.IR-04 anchors the capacity dimension that the Art. 32(1)(c) timely-restoration duty presupposes: adequate resource headroom to absorb the incident and recover availability within the documented Recovery Time Objective.
    PR.DS-11 captures the backup foundation — created, integrity-protected, maintained and tested — that makes restoration possible at all, satisfying the recovery-from-known-good-state requirement and aligning with the EDPB evidence expectation for Art. 32(1)(c).
    RC.RP-04 closes the cycle by executing the tested recovery plan that restores critical processing functions, with documented Recovery Point Objectives per activity.
    A controller documenting PR.IR-04 capacity evidence, PR.DS-11 backup-test results and RC.RP-04 recovery-exercise records can demonstrate ex post, under Art. 5(2), that timely restoration was not aspirational but tested, resourced and deliverable.
  ambiguity_notes: |
    `in a timely manner` (Art. 32(1)(c)) carries POLY+VAG-S3. Operational reading chosen: RTO defined per processing activity, as an objective measure documented in the controller's business continuity policy. An alternative reading treating timely as as-soon-as-practicable for the specific incident is operationally similar but framing-different; the chosen reading ties timeliness to a documented and testable metric. Recital 49 (non-binding) attempts to fix `timely manner` as "as soon as possible", which is directionally useful but does not bind the controller. EDPB Guidelines 7/2019 on certification treat tested backups and recovery plans as evidence of Art. 32(1)(c) compliance. Remain open: (a) whether the Art. 32(1)(c) `timely manner` threshold differs across processing contexts (e.g. real-time processing vs batch processing), pending EDPB clarification; and (b) how the recovery obligation interacts with separate BCDR obligations under DORA Art. 11–12 and NIS 2 Art. 21(2)(c), pending cross-regulation alignment.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-034
  title: "Eight-element processor contract with audit and instruction clauses"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(a)–(h) — 8 mandatory clauses" }
  linked_objectives: [SO-GDPR-022]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-CONTRACT]
  regulatory_rationale: |
    Art. 28(3) requires the processor contract (or other legal act under
    Union or Member State law, binding on the processor with regard to
    the controller) to set out the subject-matter and duration of the
    processing, the nature and purpose of the processing, the type of
    personal data and categories of data subjects, and the obligations
    and rights of the controller. That contract or other legal act shall
    stipulate, in particular, that the processor complies with the eight
    sub-clauses: (a) documented instructions, (b) confidentiality of
    authorised persons, (c) Art. 32 measures, (d) sub-processor
    conditions, (e) assistance with data-subject rights, (f) assistance
    with Arts. 32–36, (g) return or deletion on contract end, and (h)
    audits and inspections.
  security_rationale: |
    The obligation in Art. 28(3)(a)–(h) to bind every processor relationship to a contract (or other binding legal act) that stipulates eight concrete duties — documented instructions, personnel confidentiality, Art. 32 measures, sub-processor conditions, data-subject-rights assistance, Arts. 32–36 assistance, return-or-deletion on contract end, and audit access — is operationalised in NIST CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-03 is precisely the vehicle for translating processor-side obligations into contractually binding form; the eight sub-clauses map one-to-one to the implementation measures GV.SC-03 expects an organisation to embed in third-party contracts, from instruction-following (Art. 28(3)(a)) through confidentiality of personnel (Art. 28(3)(b)) to evidence-and-audit access (Art. 28(3)(h)).
    The mapping is structural: GV.SC-03 treats every cybersecurity-relevant third-party commitment as something that must appear on the face of the contract, with sub-clause-by-sub-clause enforcement rather than high-level promises, which matches the closed AND-list reading of the Art. 28(3) duty.
    A controller or processor that documents GV.SC-03 contract-clause coverage at the eight-element level can demonstrate ex post, against the Art. 5(2) accountability duty, that every processor relationship in force on the day of any supervisory inspection was operating under an enforceable Art. 28(3) contract satisfying the eight-sub-clause floor.
  ambiguity_notes: |
    The 8-element list is Berry-flagged COORD-S2 (Berry §5.4.7 closed
    AND-list): all sub-clauses are mandatory and omitting any one puts
    the controller and processor in Art. 28 non-compliance. The reading
    adopted for this SR is the closed-AND-list reading: each sub-clause
    must appear in the contract. An alternative reading under which some
    sub-clauses can be omitted when covered by other legal instruments
    would conflict with the OJ text, which requires the contract itself
    to stipulate the eight elements. Remain open: whether `other legal
    act under Union or Member State law` (e.g., a sectoral regulation)
    can substitute for the Art. 28(3) contract in toto, or whether each
    sub-clause must still appear somewhere in the chain.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-035
  title: "Processor auditability with continuous external-activity monitoring"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(c) — Article 32 measures" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(h) — audits and inspections" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1) cross-reference" }
  linked_objectives: [SO-GDPR-022, SO-GDPR-021]
  sub_domain: [D-06.3, D-10.1]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits and test results" }
    - { id: DE.CM-06, title: "External service provider activities and services monitored to find potentially adverse events" }
  applies_to_role: [PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(3)(c) requires the processor contract to stipulate that the
    processor takes all measures required pursuant to Art. 32 — the full
    Art. 32 chain covering state-of-the-art assessment, the appropriate-
    level-of-security test, the four-element list (pseudonymisation and
    encryption; ongoing CIA+R; timely restoration; and regular testing).
    Art. 28(3)(h) requires the processor to make available to the
    controller all information necessary to demonstrate compliance with
    the obligations laid down in Art. 28 and to allow for and contribute
    to audits, including inspections, conducted by the controller or
    another auditor mandated by the controller. The two sub-clauses are
    the controller's principal levers into processor security: (c) sets
    the substantive standard by reference and (h) sets the evidentiary
    and audit-access standard. Art. 32(1) in turn cross-references back,
    anchoring the four-element list and the state-of-the-art qualifier.
  security_rationale: |
    The obligation in Art. 28(3)(c), Art. 28(3)(h) and Art. 32(1) to give the controller substantive access to the processor's Art. 32 measure set and to make all information necessary available for audit or inspection is operationalised in NIST CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**, **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)** and **DE.CM-06 (External service provider activities and services are monitored to find potentially adverse events)**.
    GV.SC-03 captures the contractual-vehicle discipline that makes Art. 28(3)(c) enforceable — the full Art. 32 catalogue becomes part of the contract rather than remaining an unrecorded expectation.
    GV.SC-04 captures the periodic-recurrence posture of Art. 28(3)(h): audits, test results and inspections must be a continuous routine rather than a one-off onboarding check, so that the processor's measure set is checked against operational reality at a cadence that survives change.
    DE.CM-06 captures the day-to-day monitoring counterpart that complements periodic audit — adverse events at the processor surface must be observable to the controller in real time, not merely discoverable through annual audit sampling.
    A processor that documents GV.SC-03 contract-level Art. 32 clause coverage, GV.SC-04 routine-assessment cadence, and DE.CM-06 monitoring hand-over can demonstrate ex post, against the Art. 5(2) accountability duty, that the controller's principal levers into processor security were continuously exercisable on the day of any supervisory inspection.
  ambiguity_notes: |
    `all measures required pursuant to Art. 32` is VAG-S3 indirect
    because the chain inherits the Art. 32 ambiguities (state of the
    art, appropriate, the four-element list). The reading adopted for
    this SR is the Art. 32 reading chain: the controller's processor
    contract must reflect the full Art. 32 catalogue, and the
    processor's auditability extends to demonstrating how each Art. 32
    element is implemented. The audit clause itself is largely
    unambiguous (Art. 28(3)(h)) but the substantive scope of what counts
    as `all information necessary` is qualitative. Two alternative
    readings remain. First, a narrow reading of `all measures` that
    limits the contract to a subset of Art. 32 measures (only encryption
    and access control, for instance) would conflict with the Art.
    28(3)(c) text. Second, a controller-discretion reading of the audit
    clause that allows the processor to scope the audit downward would
    conflict with the EDPB Guidelines 07/2020 expectation that audits
    be substantive. Remain open: (a) whether remote audits
    (questionnaire-based) satisfy `audits and inspections` under Art.
    28(3)(h) or whether on-site inspections are required; (b) how
    frequently the controller may audit without becoming a de facto
    shadow-controller.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-039
  title: "Privacy by design integrated at means-and-processing determination"
  source_clauses:
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — privacy by design" }
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — privacy by default (cross)" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — integrity & confidentiality (cross)" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1) — security measures (cross)" }
  linked_objectives: [SO-GDPR-024]
  sub_domain: [D-07.1, D-01.1, D-05.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Art. 25(1) requires the controller, both at the time of
    determination of the means for processing and at the time of the
    processing itself, taking into account the state of the art, the
    cost of implementation and the nature, scope, context and purposes
    of processing as well as the risks of varying likelihood and
    severity for the rights and freedoms of natural persons, to
    implement appropriate technical and organisational measures, such
    as pseudonymisation, which are designed to implement data-
    protection principles, such as data minimisation, in an effective
    manner and to integrate the necessary safeguards into the
    processing in order to meet the requirements of this Regulation and
    protect the rights of data subjects. Art. 25(2) is the privacy-by-
    default mandate. Art. 5(1)(f) integrity and confidentiality and Art.
    32(1) security measures provide the cross-clause anchor.
  security_rationale: |
    The obligation in Art. 25(1), read with Art. 25(2), Art. 5(1)(f) and Art. 32(1), to implement appropriate technical and organisational measures (such as pseudonymisation and minimisation) both at the time of determination of the means for processing and at the time of the processing itself is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.PS-06 captures the lifecycle-spanning SDLC discipline: the obligation fires both at means-determination and during ongoing processing, which is structurally the same as the secure-development lifecycle expectation that controls be designed in at architecture and requirements time and continuously validated through later stages.
    PR.DS-12 captures the data-management discipline that turns design-time choices into continuous posture: pseudonymisation, minimisation, integrity and confidentiality safeguards are not one-off architectural decisions but live properties of the data set, maintained against the risk strategy and refreshed as purpose or context evolves.
    A controller that documents PR.PS-06 SDLC integration of by-design measures and PR.DS-12 risk-strategy data-handling discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that the state-of-the-art, cost, nature, scope, context, purposes and risks factors in the Art. 25(1) preamble were actually weight-balanced on the day of any processing operation.
  ambiguity_notes: |
    `state of the art` (Art. 25(1)) carries Berry-flagged VAG-S3 — the
    canonical time-dependent, jurisdiction-dependent, sector-dependent
    vague phrase (cf. Art. 32(1) `state of the art`). The reading
    adopted for this SR is the industry-framework reading: ISO 27001
    and 27002, NIST SP 800-53, and sector-specific certifications
    (PCI-DSS, ISO 27701) constitute the `state of the art` reference
    set at design time. Two alternative readings remain. First, the
    strict reading that anchors `state of the art` to ENISA or
    EDPB-published state-of-the-art guidance would freeze the
    reference to a slowly-updating body of soft law. Second, the loose
    reading that accepts any reasonable technical measure documented
    at design time would weaken the design-time bar and let cost of
    implementation dominate. The industry-framework reading balances
    the two by anchoring on recognised frameworks while allowing
    context-appropriate selection. Remain open: (a) whether `state of
    the art` for AI and ML processing in 2026 should be anchored on the
    EU AI Act risk-management requirements or on the NIST AI RMF; (b)
    whether the by-design obligation requires documented threat
    modelling or accepts generic data-protection-by-design checklists.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-040
  title: "Pseudonymisation-by-design with separation of identifying information"
  source_clauses:
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — pseudonymisation reference" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(a) — pseudonymisation/encryption (cross)" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a) — encryption exception (cross)" }
  linked_objectives: [SO-GDPR-024, SO-GDPR-002]
  sub_domain: [D-07.1, D-01.3]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.DS-01, title: "Data-at-rest protected" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Art. 25(1) cites pseudonymisation as the canonical by-design
    technique. Art. 4(5) defines pseudonymisation as the processing of
    personal data in such a manner that the personal data can no longer
    be attributed to a specific data subject without the use of
    additional information, provided that such additional information is
    kept separately and is subject to technical and organisational
    measures. Art. 32(1)(a) anchors the operational security measure.
    Art. 34(3)(a) recognises the by-design benefit by exempting the
    controller from breach communication when the data was rendered
    unintelligible to unauthorised persons through such means.
  security_rationale: |
    The obligation in Art. 25(1), Art. 32(1)(a) and Art. 4(5) to integrate pseudonymisation into the processing by design — together with the Art. 34(3)(a) recognition that unintelligibility removes the breach-communication trigger — is operationalised in NIST CSF 2.0 through **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)** and **PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected)**.
    PR.PS-06 captures the design-time discipline: pseudonymisation is a design choice, not a runtime patch, so the obligation only fires when it is embedded at means-determination through the SDLC rather than retrofitted after deployment — exactly the lifecycle PR.PS-06 disciplines.
    PR.DS-01 captures the storage-layer protection that pseudonymisation delivers once applied: the underlying data-at-rest benefits from the confidentiality property of the de-attributed form, and the additional-information-equivalent (the mapping table or key) is held under separate technical and organisational control consistent with the Art. 4(5) de-attribution requirement, which preserves the Art. 34(3)(a) unintelligibility carve-out.
    A controller that documents PR.PS-06 SDLC-level pseudonymisation integration and PR.DS-01 separation-of-identifying-information discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that by-design pseudonymisation was genuine on the day of any personal-data breach and that the Art. 34(3)(a) exception conditions were actually met.
  ambiguity_notes: |
    No new ambiguity. The rule preserves the cryptographic and
    irreversible-pseudonymisation reading chain from SR-GDPR-003.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-048
  title: "Records of processing with supervisory-authority access and 250-employee carve-out"
  source_clauses:
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(1) — RoPA content" }
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(4) — supervisory authority access" }
    - { clause_id: GDPR-CP13, article_ref: "Art. 30(5) — 250-employee exception" }
  linked_objectives: [SO-GDPR-029]
  sub_domain: [D-09.4, D-10.2]
  nist_csf_mapping:
    - { id: ID.AM-03, title: "Inventories of data and corresponding metadata for designated data types are maintained" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 30(1) requires each controller (and Art. 30(2) each processor)
    to maintain a record of processing activities under its
    responsibility, containing all of the following information: (a) the
    name and contact details of the controller and, where applicable,
    of the joint controller, the controller's representative and the
    data protection officer; (b) the purposes of the processing; (c) a
    description of the categories of data subjects and of the
    categories of personal data; (d) the categories of recipients to
    whom the personal data have been or will be disclosed, including
    recipients in third countries or international organisations; (e)
    where applicable, transfers of personal data to a third country or
    an international organisation; (f) where possible, the envisaged
    time limits for erasure; (g) where possible, a general description
    of the technical and organisational security measures referred to
    in Art. 32(1). Art. 30(4) makes the record available to the
    supervisory authority on request. Art. 30(5) provides the 250-
    employee exception.
  security_rationale: |
    The obligation in Art. 30(1), Art. 30(4) and Art. 30(5) to maintain records of processing activities covering the seven enumerated content items (controller details, purposes, data-subject and personal-data categories, recipients, third-country transfers, envisaged erasure time limits, and the Art. 32(1) security measures) and to make them available to the supervisory authority on request, subject to the 250-employee exception unless the disjunctive risk/special-category/criminal-conviction trigger applies, is operationalised in NIST CSF 2.0 through **ID.AM-03 (Inventories of data and corresponding metadata for designated data types are maintained)** and **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)**.
    ID.AM-03 captures the data-inventory discipline: each RoPA entry is operationally an inventory record for a designated data type, with metadata for purpose, lawful basis, recipients, transfers and retention, so that the RoPA can serve both the Art. 5(2) accountability duty and the broader ID.AM-03 risk-management posture.
    GV.PO-02 captures the process-and-procedure discipline: maintaining, refreshing and making the RoPA available on supervisory-authority request is itself an enforced process with documented triggers, owners and review cadences, supported by the documented assessment of whether the 250-employee carve-out applies given the organisation's risk, special-category or criminal-conviction footprint.
    A controller or processor that documents ID.AM-03 RoPA-grade data inventory and GV.PO-02 RoPA maintenance and access process can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the records were complete, current and immediately producible.
  ambiguity_notes: |
    `where possible` (Art. 30(1)(f)/(g)) is Berry-flagged VAG-S2, with
    both readings converging on best-effort documentation. Art. 30(5)
    carries Berry-flagged S3 VAG on `likely to result in a risk` and
    `occasional`. The reading adopted for this SR preserves the
    disjunctive (any-of-the-three) reading that triggers the RoPA
    obligation on small organisations: if any of (risk OR not-occasional
    OR special-category OR criminal-conviction) applies, the small-
    organisation exception does not apply and the RoPA must still be
    maintained. Two alternative readings remain. First, a conjunctive
    reading that would require all three triggers to be present would
    expand the small-organisation exception inappropriately. Second, a
    loose reading of `likely` as `non-negligible probability` (R2 per
    the chapter-4 ambiguity analysis) would lower the threshold and
    capture more small organisations within the obligation, which is
    the more protective outcome. Remain open: (a) whether the Art. 30(5)
    `fewer than 250 persons` count includes temporary contractors and
    part-time staff; (b) whether the RoPA `in writing, including in
    electronic form` (Art. 30(3)) requires the RoPA to be a single
    document or accepts a federated set of records.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-049
  title: "Five-event threat model with monitoring and event analysis"
  source_clauses:
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — breach awareness (cross)" }
  linked_objectives: [SO-GDPR-030]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: DE.CM-03, title: "Personnel activity and technology usage are monitored to find potentially adverse events" }
    - { id: DE.AE-02, title: "Detected events are analyzed to understand attack targets and methods" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(2) requires that, in assessing the appropriate level of
    security, account shall be taken in particular of the risks that are
    presented by processing, in particular from accidental or unlawful
    destruction, loss, alteration, unauthorised disclosure of, or
    access to, personal data transmitted, stored or otherwise
    processed. Art. 33(1) cross-references back through the breach-
    awareness trigger. The five-event risk enumeration — accidental or
    unlawful destruction, loss, alteration, unauthorised disclosure
    and unauthorised access — anchors the controller's and processor's
    threat-modelling scope.
  security_rationale: |
    The obligation in Art. 32(2), read with Art. 33(1), to take into account in the appropriate-level-of-security assessment the five enumerated risks (accidental or unlawful destruction, loss, alteration, unauthorised disclosure, and unauthorised access) and to anchor the breach-awareness trigger on those risks, is operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks and network services are monitored to find potentially adverse events)**, **DE.CM-03 (Personnel activity and technology usage are monitored to find potentially adverse events)** and **DE.AE-02 (Detected events are analyzed to understand attack targets and methods)**.
    DE.CM-01 captures the network-layer monitoring that addresses the `transmitted` events of the Art. 32(2) list, particularly unauthorised disclosure and unauthorised access along the transport surface, with adverse-event detection tuned to the five-event enumerator.
    DE.CM-03 captures the personnel-activity and technology-usage monitoring that addresses the `otherwise processed` events of the Art. 32(2) list, including alteration and unauthorised access from inside the trust boundary.
    DE.AE-02 captures the analysis layer that converts raw monitoring output into breach-relevant signal: events across all five Art. 32(2) categories must be analysed to understand attack targets and methods so that the Art. 33(1) breach-awareness trigger fires only when it should and with the right context.
    A controller or processor that documents DE.CM-01 network monitoring, DE.CM-03 personnel-and-technology monitoring and DE.AE-02 event analysis against the five-event enumeration can demonstrate ex post, against the Art. 5(2) accountability duty, that the threat-modelling scope from Art. 32(2) was operationally covered on the day of any incident or supervisory inspection.
  ambiguity_notes: |
    The 5-way OR is Berry-flagged COORD-S3 (Berry §5.4.7 menu-card
    pattern): each OR is inclusive, and the OR-chain admits at least
    five distinct threat-model scopes. The reading adopted for this SR
    is the strict inclusive reading: any of the five events triggers
    the security-assessment and monitoring obligation, and the OR is
    inclusive rather than illustrative. Two alternative readings
    remain. First, an illustrative-list reading under which the
    controller determines the in-scope events would weaken the threat-
    modelling baseline and allow cherry-picking. Second, a destruction-
    only reading that limits scope to `destruction` would conflict with
    the OJ text, which lists five distinct events. Remain open: (a)
    whether `loss` requires proof of exfiltration or covers any data-set
    unavailability event including accidental loss; (b) whether
    `unauthorised access` includes authorised-but-internal misuse, where
    the CJEU language suggests yes but the operational detection scope
    is debated.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

