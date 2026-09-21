---
document_id: AEGIS-PREPROC-GDPR-ART-5
title: GDPR Art. 5 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 5
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
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
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
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
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

# GDPR Art. 5

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-001 | Personal data remains confidential while at rest, in storage, and during processing, against unauthorised or unlawful processing. | `GDPR-CL06` (Art. 5(1)(f)); `GDPR-CP15` (Art. 32(1)(a)/(b)) | D-01.1 |
| SO-GDPR-001 | D-01.1, D-01.4 | Art. 5(1)(f), Art. 32(1)(a)/(b) | Personal data confidentiality at rest and in processing |
| SO-GDPR-003 | Personal data are accurate and, where necessary, kept up to date; every reasonable step is taken to erase or rectify inaccurate personal data without delay. | `GDPR-CL04` (Art. 5(1)(d)); `GDPR-RT12` (Art. 16) | D-01.4, D-04.4 |
| SO-GDPR-003 | D-01.4, D-04.4 | Art. 5(1)(d), Art. 16 | Accurate personal data; inaccurate erased/rectified without delay |
| SO-GDPR-015 | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed; further processing is compatible with the original purposes per the Art. 6(4) compatibility test. | `GDPR-CL03` (Art. 5(1)(c)); `GDPR-CL14` (Art. 6(4)) | D-05.1 |
| SO-GDPR-015 | D-05.1 | Art. 5(1)(c), Art. 6(4) | Data minimisation — adequate, relevant, necessary |
| SO-GDPR-016 | Personal data are processed lawfully, fairly, and in a transparent manner, on the basis of one of the six Art. 6(1) lawfulness bases (or one of the Art. 9(2) bases for special categories). | `GDPR-CL01` (Art. 5(1)(a)/(b)); `GDPR-CL08–CL13` (Art. 6(1)(a)–(f)); `GDPR-CL21` (Art. 9(1) prohibition + exceptions) | D-05.1, D-09.1 |
| SO-GDPR-016 (cross-ref) | Personal data are processed lawfully, fairly, and in a transparent manner — relates policy content to the Art. 5(1)(a) principle. | `GDPR-CL01` (Art. 5(1)(a)) | D-09.1, D-05.1 |
| SO-GDPR-016 | D-05.1, D-09.1 | Art. 5(1)(a)/(b), Art. 6(1)(a)–(f), Art. 9(1) | Lawfulness, fairness, transparency; legal-basis selection |
| SO-GDPR-017 | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; longer retention is permitted only where lawful and subject to the appropriate Art. 89(1) safeguards. | `GDPR-CL05` (Art. 5(1)(e)); `GDPR-CP12` (Art. 30(1)(f)) | D-05.2 |
| SO-GDPR-017 | D-05.2 | Art. 5(1)(e), Art. 30(1)(f) | Storage limitation — no longer than necessary |
| SO-GDPR-018 | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds applies; erasure is operationally defined as making the data inaccessible to the controller for normal processing paths. | `GDPR-C06` (Art. 4(12) breach-related — operational deletion overlap); `GDPR-CL03` (Art. 5(1)(c) — data-minimisation, downstream of erasure); `GDPR-CL05` (Art. 5(1)(e) — storage limitation), `GDPR-CP10` (Art. 28(3)(g) — deletion polysemy) | D-05.3 |
| SO-GDPR-018 | D-05.3 | Art. 17, Art. 5(1)(c)/(e) | Erasure without undue delay on Art. 17(1) grounds |
| SO-GDPR-024 | Personal-data processing implements data-protection principles (such as data minimisation) in an effective manner at the time of means-determination and at the time of processing itself, integrating necessary safeguards (including pseudonymisation, encryption, by-default limits) at state-of-the-art level. | `GDPR-CP02` (Art. 25(1)); `GDPR-CP03` (Art. 25(2)); `GDPR-CL06` (Art. 5(1)(f)) | D-07.1, D-05.1, D-01.1 |
| SO-GDPR-024 | D-07.1, D-05.1, D-01.1 | Art. 25(1), Art. 25(2), Art. 5(1)(f) | Data protection by design and by default |
| SO-GDPR-027 | The controller is responsible for, and is able to demonstrate, compliance with the Art. 5(1) personal-data processing principles. | `GDPR-CL07` (Art. 5(2)) | D-09.1 |
| SO-GDPR-027 | D-09.1 | Art. 5(2) | Controller responsible for, and able to demonstrate, compliance |
| SO-GDPR-031 | Compliance records (records of processing, consent records, processor contract records, breach notification records, DPIA records) are maintained in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections. | `GDPR-CP12` (Art. 30(3)); `GDPR-CL07` (Art. 5(2) — accountability / demonstrability); `GDPR-CP14` (Art. 31 — SA cooperation) | D-10.2, D-09.4 |
| SO-GDPR-031 | D-10.2, D-09.4 | Art. 30(3), Art. 5(2), Art. 31 | Audit-grade records integrity and traceability |

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
- sr_id: SR-GDPR-005
  title: "Accuracy and currency of stored personal data"
  source_clauses:
    - { clause_id: GDPR-CL04, article_ref: "Art. 5(1)(d) — accuracy" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — integrity (cross-reference)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-003]
  sub_domain: [D-01.4]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(d) requires personal data to be accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay. Art. 5(1)(f) reinforces this through the integrity dimension of the appropriate-security principle. Art. 4(1) defines the material scope: personal data is any information relating to an identified or identifiable natural person. Read together, the three provisions establish that accuracy is both a substantive principle (Art. 5(1)(d)) and a security-quality property (Art. 5(1)(f) integrity), and that both obligations attach whenever the data in scope meets the Art. 4(1) identifiability test. The "without delay" wording in Art. 5(1)(d) is the operative temporal anchor and is read against the Art. 16 rectification-right mechanism, which carries its own "without undue delay" obligation.
  security_rationale: |
    The obligation in Art. 5(1)(d), reinforced by the Art. 5(1)(f) integrity dimension, to keep personal data accurate and up to date is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.DS-01 anchors the storage-layer integrity controls — immutability, write-audit logging and tamper-evidence — that prevent unauthorised alteration and preserve the trusted state of stored records, satisfying the Art. 5(1)(f) integrity leg on which accuracy depends.
    PR.DS-12 captures the policy-level data-management discipline that the accuracy principle requires: a documented risk strategy governing data-quality monitoring, periodic refresh cadence and the feedback loop between the data-quality function and the rectification workflow under Art. 16.
    The two subcategories together cover both the technical integrity property (PR.DS-01) and the governance property (PR.DS-12) that the Art. 5(1)(d) 'without delay' rectification duty presupposes.
    A controller documenting PR.DS-01 immutability controls, PR.DS-12 data-quality policy and the refresh cadence per dataset can demonstrate ex post, under the Art. 5(2) accountability burden, that reasonable steps to ensure accuracy were actually taken and were proportionate to the harm of inaccuracy for the processing purpose.
  ambiguity_notes: |
    GDPR-CL04 (Art. 5(1)(d)) carries S3 VAG ambiguity on `accurate` and `reasonable step`. Reading chosen: output-accuracy, meaning accuracy measured against the data subject's current real-world state at time of processing, because it harmonises with Art. 16 right-to-rectification: if accuracy were only input-accuracy, the rectification right would be redundant. An alternative reading treats accuracy as input-accuracy only and is supported under narrower interpretations but yields weaker downstream data quality and is the position that supervisory authorities routinely penalise. A third reading distinguishes "factually inaccurate" from "comprehensively incomplete", treating the latter as outside the accuracy principle; this is rejected because Recital 39 (non-binding) treats both under the accuracy umbrella. On "reasonable step", the chosen reading operationalises the Art. 5(2) accountability burden: the controller documents the steps (data-quality monitoring, periodic refresh, complaint-driven review) and demonstrates they are proportionate to the harm of inaccuracy for the processing purpose. Remain open: (a) whether inferred data (algorithmic scoring outputs) is subject to the accuracy principle or treated as a derivative outside scope, pending EDPB guidance on AI Act interaction; and (b) whether the "reasonable step" extends to proactive discovery of inaccuracy or only to complaint-driven correction, pending CJEU clarification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-006
  title: "Rectification workflow with downstream cascade propagation"
  source_clauses:
    - { clause_id: GDPR-RT12, article_ref: "Art. 16 — rectification right" }
    - { clause_id: GDPR-CL04, article_ref: "Art. 5(1)(d)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
    - { clause_id: GDPR-RT15, article_ref: "Art. 19 — cascade notification (cross)" }
  linked_objectives: [SO-GDPR-003, SO-GDPR-012]
  sub_domain: [D-01.4, D-04.3, D-05.1]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 16 grants the data subject the right to obtain from the controller without undue delay the rectification of inaccurate personal data concerning him or her. Art. 5(1)(d) requires the controller to erase or rectify inaccurate data without delay as part of the accuracy principle. Art. 5(1)(c) data minimisation interacts with the rectification workflow by limiting the additional information collected to verify the contested fact (no over-collection). Art. 19 requires the controller to communicate any rectification to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort, and to inform the data subject about those recipients if the data subject requests it. Read together, the provisions establish a four-stage workflow: data-subject request → verification under Art. 12(6) (proportionate) → rectification in primary systems → cascade to recipients under Art. 19. The "supplementary statement" mechanism in Art. 16 (where the controller disagrees on fact) is the recognition that not all contested data is inaccurate; the controller may attach a statement rather than erase.
  security_rationale: |
    The obligation in Art. 16, read with the Art. 19 cascade duty, to rectify inaccurate personal data and propagate the correction to every recipient is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.DS-10 anchors the controlled-write integrity check that the rectification workflow performs on data in process: it preserves the prior state for audit, secures the new write against unauthorised override, and ensures that the rectification endpoint is itself subject to authentication and authorisation.
    PR.DS-12 captures the policy-level data-management discipline that the Art. 19 cascade requires: a recipient register mapping each processing activity to its known recipients, a propagation procedure, and documentation of impossible-or-disproportionate justifications where propagation fails.
    The two subcategories together operationalise the four-stage rectification workflow (request, verify, rectify, cascade) that Arts. 16 and 19 establish, treating rectification as a controlled integrity event rather than a silent overwrite.
    A controller documenting PR.DS-10 write-control evidence, PR.DS-12 recipient register and the propagation log per rectification event can demonstrate ex post, under Art. 5(2), that the rectification right was honoured across the full processing chain rather than only at the primary system.
  ambiguity_notes: |
    GDPR-RT12 (Art. 16) carries POLY-S3 ambiguity on `supplementary statement`. The rule covers both reading branches. Reading chosen: the controller either rectifies or attaches a supplementary statement, depending on whether the contested fact is verifiable as inaccurate, with the choice exercised under Art. 12(6) reasonable-doubts discipline. An alternative reading holds that the statement must be attached whenever the data subject requests it, even if the controller disputes accuracy; this is supported by some DPAs but creates record-bloat, and the chosen reading treats the statement as a fallback when verification is inconclusive. An alternative reading treats the statement as merely informational and waivable by the controller; this is rejected because it would make the right illusory. On Art. 19 cascade, the OR in the OJ text "impossible or involves disproportionate effort" is inclusive, so either escape clause suffices (see SR-GDPR-022). Remain open: (a) whether rectification applies to derived data (model weights trained on inaccurate inputs), pending EDPB AI Act interaction guidance; and (b) the operational definition of "without undue delay" for rectification (24 hours vs 7 days vs 30 days), pending EDPB Guidelines 5/2019 revision.
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
- sr_id: SR-GDPR-010
  title: "Minimised collection of identity verification data"
  source_clauses:
    - { clause_id: GDPR-RT04, article_ref: "Art. 12(6)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-005]
  sub_domain: [D-03.1, D-05.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 12(6) imposes identity-verification scope limitation through the general GDPR principle of data minimisation (Art. 5(1)(c)). The controller must request only the additional information necessary to confirm identity, not arbitrary identity documents. Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. The verification purpose is to confirm identity, so the data-minimisation test is calibrated to the identity-confirmation purpose: collect only what is necessary to confirm identity, not what would be ideal in a hypothetical stronger verification. The Art. 5(2) accountability burden shifts the demonstration duty to the controller: the controller must be able to justify the chosen verification scope.
  security_rationale: |
    The obligation in Art. 12(6), read with the Art. 5(1)(c) data-minimisation principle, to collect only the identity-verification information necessary to confirm the data subject is operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.AA-02 anchors the context-bound identity proofing that limits credential collection to what the interaction risk actually warrants, satisfying the Art. 5(1)(c) necessity test at the rights-request endpoint and preventing the verification step from accumulating identity documents that would enlarge the breach blast-radius.
    PR.DS-12 captures the policy-level data-management discipline that bounds the retention and scope of any verification artefact collected: a documented risk strategy governing how long verification data is held, who can access it, and when it is purged.
    The two subcategories together operationalise the graduated verification standard — low-risk requests with no additional collection, high-risk with bounded retention — that Art. 5(1)(c) imposes on Art. 12(6).
    A controller documenting PR.AA-02 proofing decisions, PR.DS-12 retention limits and the necessity justification per verification scope can demonstrate ex post, under the Art. 5(2) accountability burden, that identity-verification data collection was proportionate and minimised rather than opportunistically over-collected.
  ambiguity_notes: |
    `necessary` inherits VAG-S3 ambiguity from Art. 5(1)(c). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. The rule preserves the proportionate-necessary interpretation. An alternative reading treats necessity as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring the least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs (notably the CNIL) for sensitive-data contexts. The Art. 5(1)(c) necessary threshold varies with data sensitivity and breach impact; for Art. 9 special-category data, the controller may need stronger verification than for ordinary personal data. Remain open: whether automated identity-verification services (e.g. Jumio, Onfido) are themselves in scope as joint controllers under Art. 26, pending CJEU and EDPB guidance on AI-driven verification.
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
- sr_id: SR-GDPR-013
  title: "Privacy-by-default across collection, retention, and exposure"
  source_clauses:
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — privacy by default" }
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — privacy by design (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-007, SO-GDPR-024]
  sub_domain: [D-03.4, D-05.1]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices established and applied" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 25(2) obliges the controller to implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons. Art. 25(1) supplies the design-time counterpart (privacy by design) and Art. 5(1)(c) data minimisation supplies the underlying principle. Read together, the provisions establish that the default configuration of any processing system must minimise on four dimensions simultaneously: amount (collect only what is needed), extent (process only the operations needed), period (retain only as long as needed), accessibility (do not expose beyond the intended recipients).
  security_rationale: |
    The obligation in Art. 25(2), read with Art. 25(1) and Art. 5(1)(c), to configure processing systems so that by default only necessary personal data is processed is operationalised in NIST CSF 2.0 through **PR.PS-01 (Configuration management practices established and applied)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.PS-01 anchors the configuration-management baseline that sets the four default dimensions — amount collected, extent processed, retention period and accessibility — to their minimum-necessary values, satisfying the Art. 25(2) AND-coordinated default and ensuring the minimum is enforced as a system property rather than left to operator judgement.
    PR.DS-12 captures the policy-level data-management strategy that the defaults express: a documented risk-strategy positioning opt-in collection, opt-out for out-of-purpose operations, minimum-necessary retention and no public access unless explicitly granted.
    The two subcategories together operationalise the privacy-by-default pattern across all four Art. 25(2) dimensions simultaneously, so that relaxation requires affirmative data-subject intervention.
    A controller documenting PR.PS-01 default configurations, PR.DS-12 data-strategy and the per-system minimisation evidence can demonstrate ex post, under Art. 5(2), that the default state of every processing system was the minimum-necessary setting required by Art. 25(2).
  ambiguity_notes: |
    GDPR-CP03 (Art. 25(2)) carries VAG+COORD-S3 on `necessary for each specific purpose` and the four-element AND. Reading chosen: all four dimensions must individually be minimised and AND-coordinated. An alternative reading allowing some dimensions to be relaxed if others are tightened would weaken the default and is rejected. The AND reading is anchored to EDPB Guidelines 04/2019 on Article 25, which treat the four dimensions as independent minima. On "without the individual's intervention", the chosen reading treats the intervention requirement as the opt-in gate: the controller must not bypass the data subject's affirmative action to expose data. Remain open: (a) whether privacy-by-default applies to AI model defaults (e.g. opt-in vs opt-out for training-data inclusion), pending EDPB AI Act interaction guidance; and (b) whether the four-dimensional test applies per data subject or per processing activity, pending alignment with Art. 35 DPIA granularity.
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
- sr_id: SR-GDPR-017
  title: "Processor-to-controller breach notification without undue delay"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(2) — processor-to-controller notification" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3, D-06.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: RS.MA-02, title: "Incident reports triaged and validated" }
  applies_to_role: [PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(2) requires the processor to notify the controller without undue delay after becoming aware of a personal data breach. Art. 4(12) defines the trigger event. Read together, the two provisions establish the upstream trigger for the controller's Art. 33(1) 72-hour clock: the processor's awareness moment starts the chain that culminates in the controller's notification to the supervisory authority. The processor's `without undue delay` obligation is not the same as the controller's 72-hour clock; the processor must notify the controller as soon as it becomes aware, and the controller then has its own 72-hour window from receipt of the processor's notification (or from independent awareness) to notify the supervisory authority.
  security_rationale: |
    The obligation in Art. 33(2), read with Art. 4(12), for the processor to notify the controller without undue delay after becoming aware of a personal data breach is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)** and **RS.MA-02 (Incident reports triaged and validated)**.
    RS.MA-02 anchors the triage that the processor performs on detecting a breach, supplying the validated incident report that Art. 33(2) requires and establishing the awareness moment that starts the upstream chain toward the controller's own Art. 33(1) 72-hour clock.
    RS.CO-02 captures the reporting channel itself: the notification path from processor to controller, typically contractually defined under Art. 28(3)(f), through which the triaged report is escalated within the same operational shift rather than held for a deferred batch.
    The two subcategories together operationalise the processor-side leg of the breach-notification chain, recognising that processors, owning the infrastructure layer, frequently detect breaches first.
    A controller documenting, against its Art. 28(3) processor contracts, RS.MA-02 triage evidence and RS.CO-02 notification timestamps from each processor can demonstrate ex post, under Art. 5(2), that the processor-to-controller link operated without undue delay and that its own 72-hour clock was started from a genuine upstream report.
  ambiguity_notes: |
    `without undue delay` inherits S3 VAG ambiguity (Berry §5.1). Reading chosen: action on the same operational shift or business day, with hard escalation channels documented in the Art. 28(3) processor contract. An alternative reading fixing the window at 24 hours is acceptable but operationally narrower. A third reading extending the window to 72 hours (mirroring the controller's clock) is rejected because it would compress the controller's own window to zero in practice. The chosen reading aligns with EDPB Guidelines 9/2022 §3.4 and ISO 27001 A.16.1.2 reporting expectations. Remain open: whether AI-driven detection by the processor that flags a probable breach without confirmation triggers the `without undue delay` clock, or whether confirmation is required, pending EDPB guidance on probabilistic detection.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-018
  title: "Structured four-element breach notification content"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(3)(a)/(b)/(c)/(d) — notification content" }
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — overall 72h envelope" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3, D-09.4]
  nist_csf_mapping:
    - { id: RS.AN-03, title: "Analysis performed to determine what occurred and root cause" }
    - { id: RS.AN-07, title: "Incident data and metadata collected with integrity preserved" }
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(3) requires the controller's breach notification to the supervisory authority to describe at minimum: (a) the nature of the personal data breach including, where possible, the categories and approximate number of data subjects concerned and the categories and approximate number of personal data records concerned; (b) the name and contact details of the data protection officer or other contact point where more information can be obtained; (c) the likely consequences of the personal data breach; (d) the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 33(1) provides the overall 72-hour envelope. Read together, the provisions establish a four-element content requirement with the recognition that initial notification operates under uncertainty; the controller supplements as investigation proceeds.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — describe the nature of the personal data breach including where possible, the categories and approximate number of data subjects concerned and the categories and approximate number of personal data records concerned]
  security_rationale: |
    The obligation in Art. 33(3), read with the Art. 33(1) 72-hour envelope, to deliver a four-element breach notification (nature, contact, consequences, measures) is operationalised in NIST CSF 2.0 through **RS.AN-03 (Analysis performed to determine what occurred and root cause)**, **RS.AN-07 (Incident data and metadata collected with integrity preserved)** and **RS.CO-02 (Incidents reported internally to appropriate stakeholders)**.
    RS.AN-03 anchors the root-cause analysis that produces the Art. 33(3)(a) nature description and the Art. 33(3)(c) likely-consequences assessment, satisfying the content requirement even where the investigation is still incomplete at the 72-hour mark.
    RS.AN-07 captures the evidence-integrity discipline — chain of custody, provenance preservation, metadata collection — that makes the notification defensible under supervisory scrutiny and supports the phased-disclosure model under Art. 33(4).
    RS.CO-02 closes the loop by routing the structured content to the internal stakeholders who approve and dispatch the notification.
    A controller documenting RS.AN-03 analysis records, RS.AN-07 evidence-preservation logs and RS.CO-02 internal-approval trail can demonstrate ex post, under Art. 5(2), that the notification content met the Art. 33(3) standard and that subsequent supplements were grounded in preserved, integrity-checked evidence.
  ambiguity_notes: |
    `where possible`, `approximate number`, `likely consequences` are acknowledged VAG-S2. Reading chosen: best-effort reporting at the time of notification, with subsequent updates as investigation proceeds. The Art. 33(4) phased-disclosure mechanism supports this: the controller can provide initial incomplete information and supplement as it becomes available, provided the reasons for incompleteness are documented. An alternative reading requiring precise reporting at 72 hours is rejected: the OJ text explicitly softens with `where possible` and `approximate`. Remain open: (a) whether the phased-disclosure model applies to each Art. 33(3) element independently or only to elements (a), (c), and (d), pending EDPB Guidelines 9/2022 revision; and (b) how the controller documents the boundary between initial notification and supplemental disclosure in audit defensible form, pending alignment with ISO 27035 incident-management practice.
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
- sr_id: SR-GDPR-020
  title: "Cryptographic and mitigation carve-outs for data-subject notification"
  source_clauses:
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a) — encryption/unintelligibility exception" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(b) — subsequent-measures exception" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk trigger" }
  linked_objectives: [SO-GDPR-011, SO-GDPR-002]
  sub_domain: [D-04.3, D-01.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.IR-03, title: "Mechanisms to achieve resilience in normal and adverse situations" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(3)(a) provides that the data-subject notification under Art. 34(1) is not required if the controller has implemented appropriate technical and organisational protection measures, and those measures were applied to the personal data affected by the personal data breach, in particular those that render the personal data unintelligible to any person who is not authorised to access it, such as encryption. Art. 34(3)(b) provides a parallel exception if the controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise. Art. 34(1) supplies the high-risk trigger that the exceptions modify. Read together, the provisions establish two paths to eliminate the data-subject notification duty despite a high-risk breach: cryptographic protection at the time of breach, or subsequent mitigation that neutralises the high risk.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — the controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise]
  security_rationale: |
    The obligation in Art. 34(3)(a) and (b), read with the Art. 34(1) high-risk trigger, to eliminate the data-subject notification duty through cryptographic protection or subsequent mitigation is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.IR-03 (Resilience requirements in normal and adverse situations)**.
    PR.DS-01 anchors the Art. 34(3)(a) cryptographic carve-out: the encryption, applied to the data actually affected by the breach, that renders the personal data unintelligible to any unauthorised person, with the key separation that makes the carve-out auditable rather than merely asserted.
    PR.IR-03 captures the Art. 34(3)(b) subsequent-measures path: the resilience mechanisms — key rotation, credential reset, vulnerability patch, compensating controls — that together ensure the high risk is no longer likely to materialise, satisfying the higher threshold that demands demonstrated risk neutralisation rather than mere mitigation effort.
    The two subcategories together operationalise the two distinct paths the regulation offers for eliminating the notification duty despite a high-risk breach.
    A controller documenting PR.DS-01 key-state evidence on the affected dataset and PR.IR-03 mitigation-effect demonstration can demonstrate ex post, under Art. 5(2), which carve-out applied and that its conditions were genuinely met on the day of the breach.
  ambiguity_notes: |
    Both exceptions carry VAG-S3 (see SR-GDPR-004 for `unintelligible` reading chosen). The `no longer likely to materialise` wording in Art. 34(3)(b) is read as a high threshold: the controller must demonstrate that the mitigation has materially reduced the risk below the Art. 34(1) threshold, not merely that mitigation was attempted. The Art. 34(3)(a) operational condition `those measures were applied to the personal data affected by the personal data breach` requires the controller to demonstrate that the encryption protected the actual affected dataset, not merely that encryption was deployed on the dataset generally. Rule preserves the cryptographic-reading exception. Remain open: (a) whether rotation of cryptographic keys after the breach (treating the old keys as compromised) satisfies the Art. 34(3)(a) carve-out when the controller retains access to old keys for legitimate purposes, pending EDPB clarification; and (b) how the Art. 34(3)(b) `subsequent measures` carve-out interacts with the Art. 33 supervisory-authority notification (which is not carved out), pending alignment with EDPB Guidelines 9/2022.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-021
  title: "Disproportionate-effort public-communication substitute for notification"
  source_clauses:
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(c) — disproportionate effort exception" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk trigger" }
  linked_objectives: [SO-GDPR-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated stakeholders per information-sharing rules" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(3)(c) provides that the data-subject notification under Art. 34(1) is not required where it would involve disproportionate effort. In such cases, there shall instead be a public communication or similar measure whereby the data subjects are informed in an equally effective manner. Art. 34(1) supplies the high-risk trigger. Read together, the provisions establish that the data-subject notification is the default for high-risk breaches, but where direct notification is operationally disproportionate (e.g. legacy data without contact details, very large data-subject populations, encrypted contact channels unavailable), the controller may substitute a public communication that achieves equally effective notice. Recital 62 (non-binding) anchors the disproportionate-effort test as a cost-vs-risk assessment.
  security_rationale: |
    The obligation in Art. 34(3)(c), read with the Art. 34(1) high-risk trigger, to substitute a public communication for direct data-subject notification where direct notification involves disproportionate effort is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information shared with designated stakeholders per information-sharing rules)**.
    RS.CO-03 anchors the information-sharing discipline that the substitute communication must satisfy: the public communication or similar measure must achieve equally effective reach, so that data subjects are informed in a manner that preserves their ability to take protective action despite the absence of direct contact.
    Although only one CSF subcategory is mapped, RS.CO-03 carries the full weight of the substitute-notification pattern, covering the design of the alternative channel (prominent website notice, press release, social-media post), the documentation of the disproportionate-effort justification, and the reach-effectiveness evidence that the substitute must produce.
    The subcategory presupposes the cost-vs-risk assessment that Recital 62 anchors, treating the exception as a high bar rather than a routine opt-out from direct notification.
    A controller documenting RS.CO-03 substitute-communication records, the disproportionate-effort analysis and the reach evidence can demonstrate ex post, under Art. 5(2), that direct notification was genuinely infeasible and that the substitute achieved equally effective notice rather than serving as a weaker exemption.
  ambiguity_notes: |
    `disproportionate effort` carries S3 VAG (Recital 62 non-binding anchor to cost-vs-risk assessment). Reading chosen: the exception applies narrowly, and the controller must demonstrate efforts. The chosen reading treats disproportionate effort as a high bar: the controller must show that direct notification would impose costs grossly disproportionate to the protective benefit, considering the data-subject population, the availability of contact details, and the operational disruption. An alternative reading allowing the exception whenever direct notification is operationally inconvenient is rejected: it would make the exception the rule. A third reading admitting the exception for breaches affecting only legacy data without contact details is acceptable as a special case but should be documented as such. Recital 62 enumerates cost factors (number of data subjects, contact-channel availability) but does not bind the controller. Remain open: whether the `public communication or similar measure` requires multi-language coverage for cross-border data-subject populations, pending EDPB Guidelines 9/2022 clarification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-022
  title: "Downstream-recipient cascade for rectification and erasure"
  source_clauses:
    - { clause_id: GDPR-RT15, article_ref: "Art. 19 — cascade notification" }
    - { clause_id: GDPR-RT12, article_ref: "Art. 16 — rectification" }
    - { clause_id: GDPR-RT11, article_ref: "Art. 15(4) — third-party-rights limit" }
    - { clause_id: GDPR-CL26, article_ref: "Art. 11(2) — identification-exemption (cross)" }
  linked_objectives: [SO-GDPR-012]
  sub_domain: [D-04.3, D-05.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 19 requires the controller to communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Art. 16, Art. 17(1) or Art. 18 to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller must inform the data subject about those recipients if the data subject requests it. Art. 16 supplies the rectification mechanism, Art. 15(4) caps the disclosure obligation to recipients known to the controller, and Art. 11(2) preserves the identification precondition for the data-subject rights endpoint. Read together, the provisions establish a downstream-integrity obligation: when the controller corrects, erases, or restricts personal data, the correction must propagate to all known recipients or the controller must demonstrate that propagation is impossible or disproportionate, and the controller must be able to enumerate those recipients on request.
  security_rationale: |
    The obligation in Art. 19, read with Art. 16 and Art. 15(4), to cascade rectifications and erasures to every recipient of the personal data is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.DS-12 anchors the data-management foundation that the cascade requires: a recipient register mapping each processing activity to its known recipients, including processors and joint controllers, and a propagation procedure that issues the rectification or erasure event through that register, satisfying the Art. 19 downstream-integrity duty at the policy layer.
    RS.CO-02 captures the reporting dimension that gives the cascade operational force: routing each correction event to the internal stakeholders responsible for recipient notification, documenting the impossible-or-disproportionate justifications where propagation fails, and retaining the evidence needed to answer a data-subject recipient-list request under Art. 19.
    The two subcategories together operationalise the propagation chain that prevents the rectification right from becoming illusory across a distributed processing ecosystem.
    A controller documenting PR.DS-12 recipient register, RS.CO-02 propagation logs and the per-event justification evidence can demonstrate ex post, under Art. 5(2), that corrections reached every known recipient or that the documented exception genuinely applied.
  ambiguity_notes: |
    `impossible` OR `disproportionate effort` (Art. 19) carries COORD-S3. Reading chosen: either escape clause suffices, as a logical inclusive OR. An alternative reading requiring both to hold is rejected: the stricter reading would impose undue compliance burden without policy justification. The OJ text uses `or`, the English-language UN-style drafting convention for an inclusive disjunction; EDPB Guidelines treat this consistently. On the Art. 15(4) cap (third-party-rights limit), the disclosure to the data subject about recipients is bounded to recipients known to the controller; the controller is not required to investigate recipients beyond its own records. Remain open: (a) whether the `recipient` definition includes processors (under Art. 28) and joint controllers (under Art. 26) or only independent third-party controllers, pending EDPB Guidelines 5/2019 revision; and (b) how the recipient-list request interacts with confidentiality obligations (e.g. trade-secret-protected recipients), pending alignment with Charter Art. 7 and CJEU jurisprudence on commercial confidentiality.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-023
  title: "Pre-launch supervisory consultation on residual high risk"
  source_clauses:
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation" }
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — high-risk DPIA" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
  linked_objectives: [SO-GDPR-013, SO-GDPR-028]
  sub_domain: [D-04.3, D-09.2]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: ID.RA-06, title: "Risk responses chosen, prioritized, planned, tracked, communicated" }
  applies_to_role: [CONTROLLER, SUPERVISORY_AUTHORITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 36(1) requires the controller to consult the supervisory authority prior to processing where a data protection impact assessment under Art. 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk. Art. 35(1) supplies the DPIA trigger (high-risk processing), and Art. 35(7) supplies the DPIA content requirement (systematic description, necessity and proportionality assessment, risk assessment, mitigation measures). Art. 36(2) defines the supervisory authority's 8-week response obligation. Read together, the provisions establish a pre-launch gate: where DPIA identifies residual high risk after mitigation, the controller must consult the supervisory authority before launching the processing.
  security_rationale: |
    The obligation in Art. 36(1), read with Art. 35(1) and Art. 35(7), to consult the supervisory authority before launching processing that retains residual high risk after DPIA mitigation is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements understood and managed)** and **ID.RA-06 (Risk responses chosen, prioritized, planned, tracked, and communicated)**.
    GV.OC-03 anchors the governance layer that recognises the prior-consultation duty as a legal-regulatory requirement to be managed, satisfying the Art. 36(1) pre-launch-gate status and ensuring the consultation is scheduled into the launch timeline rather than treated as optional, with the Art. 36(2) eight-week supervisory window accommodated.
    ID.RA-06 captures the risk-response leg: the residual risk that survives the Art. 35(7) DPIA mitigation assessment is explicitly chosen, prioritised, planned, tracked and communicated to the authority, with the DPIA content (systematic description, necessity and proportionality, risk assessment, mitigation measures) supplying the evidence base.
    The two subcategories together operationalise the structured risk-response communication that the prior-consultation gate represents, distinguishing it from post-launch incident reporting.
    A controller documenting GV.OC-03 consultation records and ID.RA-06 residual-risk decisions can demonstrate ex post, under Art. 5(2), that the pre-launch engagement occurred before processing began and that the residual-risk justification was transparent.
  ambiguity_notes: |
    `high risk in the absence of measures` is the same `high risk` POLY family as Arts. 34 and 35. Readings converge via the Art. 35(1) threshold inheritance. The `prior to processing` wording is read strictly: the controller must consult before launching, not after, and the supervisory authority's 8-week window under Art. 36(2) must be accommodated in the launch timeline. EDPB Guidelines 4/2019 on DPIA provide factors for high-risk classification but do not bind the controller. Remain open: (a) whether iterative processing activities (e.g. machine-learning model updates) trigger fresh Art. 36(1) consultations on each iteration or whether a single consultation covers the iterative cycle, pending EDPB AI Act interaction guidance; and (b) how the consultation interacts with the Art. 27 representative designation for non-EU controllers, pending alignment with international supervisory cooperation.
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
- sr_id: SR-GDPR-025
  title: "Purpose-bound data minimisation with compatibility assessment"
  source_clauses:
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation" }
    - { clause_id: GDPR-CL14, article_ref: "Art. 6(4) — compatibility test" }
    - { clause_id: GDPR-CL02, article_ref: "Art. 5(1)(b) — purpose limitation (cross)" }
  linked_objectives: [SO-GDPR-015]
  sub_domain: [D-05.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: ID.AM-03, title: "Inventories of data and metadata for designated data types" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. Art. 6(4) provides the compatibility test for further processing beyond the original purposes, requiring the controller to take into account, inter alia, (a) any link between the purposes, (b) the context of collection, (c) the nature of the personal data (especially special categories), (d) the possible consequences for data subjects, and (e) the existence of appropriate safeguards. Art. 5(1)(b) purpose limitation supplies the upstream anchor. Read together, the three provisions establish that data minimisation is calibrated to the purpose, that any change of purpose triggers a compatibility assessment, and that the purpose itself is bound by specification, explicitness, and legitimacy.
  security_rationale: |
    The obligation in Art. 5(1)(c), read with the Art. 6(4) compatibility test and Art. 5(1)(b) purpose limitation, to keep personal data adequate, relevant and limited to what is necessary is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data managed consistent with risk strategy)** and **ID.AM-03 (Inventories of data and metadata for designated data types)**.
    ID.AM-03 anchors the data-inventory foundation that minimisation requires: knowing what data is held, for which declared purpose, and with which metadata, supplying the asset record without which the Art. 5(1)(c) necessity test cannot be applied and the Art. 6(4) compatibility assessment cannot be run on a change of purpose.
    PR.DS-12 captures the policy-level data-management strategy that the inventory enables: per-purpose collection limits, retention schedules that delete at purpose-end, and the documented compatibility assessment for any further processing, satisfying the proportionality-to-purpose standard.
    The two subcategories together operationalise minimisation as both a knowledge property (what is held) and a discipline (how it is bounded), reducing attack surface and breach impact as security side-effects.
    A controller documenting ID.AM-03 data inventory and PR.DS-12 retention-and-compatibility decisions can demonstrate ex post, under Art. 5(2), that each dataset was necessary for its purpose and that any purpose-change survived the Art. 6(4) test.
  ambiguity_notes: |
    `adequate, relevant, and limited to what is necessary` carries VAG-S3 (three conjunctive vague adjectives). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. An alternative reading treats adequacy as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs for sensitive-data contexts. The Art. 6(4) compatibility test is the procedural mechanism for any change of purpose; the five factors are conjunctive in the sense that all must be considered, but the test is qualitative and the controller exercises judgement. Remain open: (a) whether machine-learning model training purposes are compatible with the original collection purpose under Art. 6(4), or require fresh consent, pending EDPB AI Act interaction guidance and CJEU jurisprudence on inferred-data compatibility; and (b) whether the data-minimisation threshold differs for secondary processing for fraud-prevention or IT-security purposes under Art. 6(1)(f), pending alignment with the legitimate-interests balancing test.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-026
  title: "Lawful, fair, and transparent processing on documented Art. 6 basis"
  source_clauses:
    - { clause_id: GDPR-CL01, article_ref: "Art. 5(1)(a) — lawfulness, fairness, transparency" }
    - { clause_id: GDPR-CL08, article_ref: "Art. 6(1)(a) — consent" }
    - { clause_id: GDPR-CL02, article_ref: "Art. 5(1)(b) — purpose limitation (cross)" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy established, communicated, enforced" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    The lawful/fair/transparent obligation in Art. 5(1)(a) is the gateway
    principle: every personal-data processing operation must satisfy all
    three conjunctive conditions, regardless of which Art. 6(1) lawfulness
    base the controller relies on (Recital 39). Lawfulness anchors
    processing in a recognised legal basis, and for consent specifically
    Art. 6(1)(a) couples with the Art. 4(11) freely-given, specific,
    informed and unambiguous definition; for the other five bases the
    controller relies on the relevant sub-clause of Art. 6(1)(b)–(f). Fairness,
    as developed by the EDPB, looks at the balance of power between data
    subject and controller and forbids deceptive or unexpectedly
    detrimental processing. Transparency, anchored in Arts. 12–14, requires
    that information about the processing be intelligible, easily
    accessible, and provided in clear and plain language. Art. 5(1)(b)
    purpose limitation binds all three by requiring that purposes be
    specified, explicit and legitimate before processing begins.
  security_rationale: |
    The obligation in Art. 5(1)(a), read with Art. 6(1)(a) and Art. 5(1)(b), to ensure that every personal-data processing operation is anchored in a specified purpose and a traceable Art. 6(1) lawfulness basis is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **GV.PO-01 (Organizational cybersecurity policy is established, communicated, and enforced)**.
    GV.OC-03 is the regulatory-translation discipline: it forces the controller to inventory the Art. 6(1) bases on which each data flow depends, to characterise the lawfulness, fairness and transparency obligations that flow from Art. 5(1)(a), and to keep that inventory current as purposes or bases change — directly satisfying the substantively fair and procedurally transparent posture that Art. 5(1)(a) imposes.
    GV.PO-01 translates the same requirements into a communicated, enforced organisational policy layer: every deployment of a personal-data pipeline must carry a documented, auditable link from the data flow to its specified purpose and Art. 6 basis, with security controls inheriting their scope from that upstream lawful-purpose layer rather than substituting for it.
    A controller that documents GV.OC-03 inventory coverage and GV.PO-01 policy enforcement on every data flow can demonstrate ex post, against the Art. 5(2) accountability threshold, that no production processing operated outside an identifiable Art. 6 basis on the day of any supervisory inspection.
  ambiguity_notes: |
    `lawful, fair, transparent` carries three conjunctive vague adjectives,
    each a Berry-flagged open-texture term (Berry §5.1), and the
    relationship between them is multiplicative rather than additive:
    failure of any one vitiates the Art. 5(1)(a) obligation. The reading
    adopted for this SR combines the substantive interpretation of
    fairness, namely no deception about purpose or use combined with a
    balance-of-interests test on data-subject impact, with the procedural
    interpretation grounded in notice, consent and complaint-channel
    availability, and aligns with EDPB Guidelines 05/2020 on consent
    (EDPB Guidelines 05/2020 §3). Two alternative readings remain on the
    table. The consequentialist reading, under which fairness is measured
    by the absence of significant detrimental consequence to the data
    subject unless proportionate, shifts the analysis away from process
    quality and towards outcome harm and weakens the ex-ante compliance
    posture. The procedural-only reading restricts fairness to the
    existence of notice, consent and complaint channels and effectively
    collapses fairness into transparency, leaving substantive data-subject
    harm outside the scope of Art. 5(1)(a). Remain open: (a) whether
    `fairness` requires substantive balance-of-interests or only
    procedural safeguards in cross-border employment-data contexts; (b)
    whether AI-driven profiling that respects transparency obligations can
    nevertheless fail Art. 5(1)(a) on substantive fairness grounds even
    where the data subject has consented.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-027
  title: "Six documented lawfulness bases with necessity gating per purpose"
  source_clauses:
    - { clause_id: GDPR-CL09, article_ref: "Art. 6(1)(b) — contract" }
    - { clause_id: GDPR-CL10, article_ref: "Art. 6(1)(c) — legal obligation" }
    - { clause_id: GDPR-CL11, article_ref: "Art. 6(1)(d) — vital interests" }
    - { clause_id: GDPR-CL12, article_ref: "Art. 6(1)(e) — public interest" }
    - { clause_id: GDPR-CL13, article_ref: "Art. 6(1)(f) — legitimate interests" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-PURPOSE]
  regulatory_rationale: |
    Art. 6(1) lists six lawfulness bases for processing personal data,
    namely (a) consent, (b) contract, (c) legal obligation, (d) vital
    interests, (e) public interest and (f) legitimate interests, and the
    same Article applies, via Art. 9(2), to special categories (Recital
    40). Each processing purpose must be supported by at least one
    identifiable base, and the basis must be documented at the time of
    determination of the means and re-evaluated when the purpose changes.
    Bases (b) through (d) carry their own qualifiers, with `necessary`
    gating performance of a contract under (b), `necessary for compliance
    with a legal obligation` under (c) and `necessary to protect vital
    interests` under (d), while (e) requires a Union or Member State law
    basis and (f) requires the legitimate-interest balancing test
    (Recital 47; Recital 49). The EDPB Guidelines 02/2019 on Art. 6(1)(b)
    interpret `necessary` strictly, and the EDPB Guidelines on legitimate
    interests develop the (f) balancing test (purpose test, necessity
    test, balancing test).
  security_rationale: |
    The obligation in Art. 6(1)(b)–(f), read with Art. 5(1)(b) and Art. 5(1)(c), to record and refresh an identifiable lawfulness basis for every processing purpose is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)**.
    GV.OC-03 captures the regulatory-translation layer: the controller must inventory the six Art. 6(1) bases against the five `necessary` qualifiers (contract, legal obligation, vital interests, public-interest law, and the legitimate-interest balancing test) and re-evaluate that inventory each time the purpose evolves, satisfying the upstream anchor that any personal-data flow must be traceable to a named basis before processing begins.
    GV.PO-02 turns that inventory into enforced process: documented procedure for selecting a base, recording the necessity and (where applicable) balancing-test evidence, and refreshing the record on purpose change, so that security controls scope themselves from a defensible lawful-purpose classification rather than from an undocumented controller assertion.
    A controller that documents GV.OC-03 basis-to-purpose coverage and GV.PO-02 review cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection each processing operation was operating within an identifiable Art. 6 basis with the appropriate `necessary` threshold documented at the time of determination of the means.
  ambiguity_notes: |
    Each of bases (b) through (f) carries Berry-flagged VAG-S3
    open-texture on `necessary`. Base (e) carries POLY+VAG-S3 on the scope
    of `public interest` and on the law-by-law requirement, and base (f)
    carries POLY+VAG-S3 on what counts as a `legitimate interest`. The
    reading adopted for this SR follows the EDPB Guidelines 02/2019
    interpretation for (b), Art. 6(3) for (c), Recital 46 for (d), the
    EDPB reading on (e) under which Union or Member State law must provide
    the basis, and the EDPB Guidelines on legitimate interests for (f).
    All five non-consent sub-bases are preserved as distinct. Two
    alternative readings remain on the table. First, an expansive reading
    of `necessary` in (b) that treats any commercial reliance on the data
    subject as automatically satisfying necessity would weaken the
    data-minimisation correlate of Art. 5(1)(c) and is rejected. Second,
    a controller-discretion reading of (f) that downplays the balancing
    test in favour of a procedural documented-assessment step would lose
    the substantive protection the test provides. Remain open: (a)
    whether AI-training pipelines using contractual necessity under (b)
    can satisfy the `necessary` threshold when alternative, less-
    intrusive legal bases exist; (b) whether public-interest bases under
    (e) require sector-specific Member State law or accept cross-sector
    horizontal law.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-028
  title: "Heightened handling for nine special-category personal-data classes"
  source_clauses:
    - { clause_id: GDPR-CL21, article_ref: "Art. 9(1) — special-category prohibition" }
    - { clause_id: GDPR-CL22, article_ref: "Art. 9(2)(a) — explicit consent" }
    - { clause_id: GDPR-C23, article_ref: "Art. 9(2)(g) — substantial public interest (cross)" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CATEGORY]
  regulatory_rationale: |
    Art. 9(1) prohibits processing of the nine enumerated special
    categories of personal data, namely racial or ethnic origin,
    political opinions, religious or philosophical beliefs, trade union
    membership, genetic data, biometric data for the unique identification
    of a natural person, health data and data concerning sex life or
    sexual orientation, unless and until one of the ten Art. 9(2)
    exceptions applies (Recital 51; Recital 52). The Art. 9(2)(a)
    exception requires explicit consent, the Art. 9(2)(g) exception
    requires a substantial public-interest basis grounded in Union or
    Member State law, and the Art. 9(2)(j) statistical and archiving
    exception is bounded by Art. 89(1) safeguards. Each special category
    is distinct and conjunctive — the nine prohibited categories each
    independently trigger Art. 9(1). The Art. 9(2)(a) `explicit` qualifier
    on consent sits in addition to the Art. 4(11) `specific, informed,
    freely given and unambiguous` baseline.
  security_rationale: |
    The obligation in Art. 9(1), Art. 9(2)(a) and Art. 9(2)(g) to gate the nine special-category data classes behind one of ten enumerated exceptions, with heightened handling for biometric-for-unique-identification and other intrinsically sensitive classes, is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    GV.OC-03 captures the per-class exception-tracking discipline: the controller must record which of the ten Art. 9(2) exceptions underpins each special-category flow, treating the nine Art. 9(1) categories as independently gated, and must hold the Art. 9(2)(a) explicit-consent artefact to the heightened standard that sits above the Art. 4(11) baseline.
    PR.DS-12 captures the differentiated-handling posture that special-category data warrants: narrower access permissions, stronger purpose-binding, enhanced logging, additional encryption or pseudonymisation layer, and stricter retention, all aligned with a risk strategy that weights each of the nine classes against the elevated harm envelope the Art. 9 prohibition presupposes.
    A controller that documents GV.OC-03 exception-per-class coverage and PR.DS-12 risk-stratified handling for each category can demonstrate ex post, against the Art. 5(2) accountability duty, that no special-category flow operated without an identified Art. 9(2) exception and the heightened controls the category warrants on the day of any supervisory inspection.
  ambiguity_notes: |
    Source clause GDPR-CL21 carries Berry-flagged POLY+COORD-S3 because
    nine special categories are conjunctive, each category independently
    engaging Art. 9(1) and each exception in Art. 9(2) being read in light
    of every category it is invoked for. The Art. 9(2)(a) `explicit
    consent` qualifier carries POLY-S3 against the Art. 4(11) `specific`
    consent baseline, since explicit adds a written or equally
    unambiguous formal-act requirement on top of the freely-given,
    specific, informed and unambiguous quartet. The reading adopted for
    this SR treats the nine Art. 9(1) categories as distinct (each
    independently engages Art. 9(1)) and treats `explicit consent` for
    special categories as requiring a written, separately captured
    consent under EDPB Guidelines 05/2020 on consent (strict reading).
    Two alternative readings remain. First, an integrative reading that
    bundles all nine categories into a single `sensitive-data` flag would
    lose the biometric-for-unique-identification nuance (which excludes
    ordinary biometric verification). Second, a functional reading of
    `explicit` that accepts an electronic confirmation as equivalent to
    written consent without distinguishing the special-category context
    would weaken the heightened standard the Art. 9(2)(a) qualifier
    imposes. Remain open: (a) whether biometric processing for security
    authentication (not unique identification) is captured by Art. 9(1);
    (b) whether `explicit consent` requires a paper signature or accepts
    a recorded electronic confirmation for online special-category
    collection.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-029
  title: "Documented retention limits with erasure at purpose end"
  source_clauses:
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation" }
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(1)(f) — retention time limits" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-017]
  sub_domain: [D-05.2, D-10.2]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: ID.AM-03, title: "Inventories of data and metadata for designated data types" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(e) requires that personal data be kept in a form which
    permits identification of data subjects for no longer than is
    necessary for the purposes for which the personal data are processed;
    longer retention is permitted only for archiving purposes in the
    public interest, scientific or historical research purposes, or
    statistical purposes, in each case subject to the Art. 89(1)
    safeguards (pseudonymisation, aggregation, access limitation). Art.
    30(1)(f) requires the records of processing to document, where
    possible, the envisaged time limits for erasure of the different
    categories of data. Art. 5(1)(c) data minimisation reinforces
    storage limitation upstream by limiting the categories of data
    collected. The three provisions operate as a chain: minimisation at
    collection (Art. 5(1)(c)), retention-period setting (Art. 5(1)(e)),
    and retention-period documentation in the RoPA (Art. 30(1)(f)).
  security_rationale: |
    The obligation in Art. 5(1)(e), Art. 30(1)(f) and Art. 5(1)(c) to bound identification-allowing retention to what is necessary for the declared purpose, with documented time limits and Art. 89(1) safeguards for the public-interest carve-outs, is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)** and **ID.AM-03 (Inventories of data and corresponding metadata for designated data types are maintained)**.
    PR.DS-12 captures the per-dataset risk-and-purpose binding: the controller defines and documents a retention period for each category, resets the clock when the underlying purpose changes, and pairs long-term Archiving or research-only retention with the Art. 89(1) pseudonymisation, aggregation and access-limitation safeguards so that the residual data set at any moment is the smallest the purpose permits.
    ID.AM-03 captures the data-inventory substrate without which retention cannot be enforced: every personal-data category must appear in an inventory tagged with declared purpose, lawful basis and envisaged erasure time, so that periodic review can decide to retain, anonymise or delete against a documented clock rather than against an undocumented assumption.
    A controller that documents PR.DS-12 retention schedules per category and ID.AM-03 inventory entries per data flow can demonstrate ex post, against the Art. 5(2) accountability duty, that no personal data was retained beyond the period necessary for its declared purpose on the day of any supervisory inspection.
  ambiguity_notes: |
    `no longer than is necessary` carries Berry-flagged VAG-S3 on the
    temporal open-texture. The reading adopted for this SR is the
    risk-based reading: indefinite retention is allowed only with
    adequate safeguards such as pseudonymisation, aggregation or full
    anonymisation, and the retention period must be reset whenever the
    underlying purpose changes. This reading aligns with EDPB Guidelines
    05/2020 on storage limitation. Two alternative readings remain. First,
    the strict-purpose-bound reading would set retention to the minimum
    required to complete the immediate purpose and disregard the Art.
    89(1) carve-out; this reading collapses the archiving, research and
    statistical exception and conflicts with the OJ text. Second, the
    indefinite-retention reading would allow retention to persist beyond
    purpose completion whenever the controller asserts that the data
    might become useful again; this reading conflicts with Art. 5(1)(e)
    directly. Remain open: (a) whether the Art. 89(1) safeguards suffice
    to support indefinite retention of pseudonymised special-category
    data in research repositories; (b) how retention clocks should be
    defined when the purpose evolves incrementally, with each new purpose
    resetting the clock versus the original clock being preserved.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-030
  title: "Right-to-erasure with cryptographic key-destruction deletion path"
  source_clauses:
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
    - { clause_id: GDPR-CP10, article_ref: "Art. 28(3)(g) — delete polysemy" }
  linked_objectives: [SO-GDPR-018, SO-GDPR-019]
  sub_domain: [D-05.3]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 17 grants the data subject the right to erasure (the right to be
    forgotten) where the conditions listed in Art. 17(1)(a)–(f) apply; the
    corresponding controller-side duties flow from Art. 5(1)(c) data
    minimisation and Art. 5(1)(e) storage limitation, which together
    require erasure once the purpose no longer applies. Art. 28(3)(g)
    imposes a processor-side mirror obligation: at the choice of the
    controller, the processor must delete or return all the personal data
    after the end of the provision of services relating to processing,
    and must delete existing copies unless Union or Member State law
    requires storage. The three provisions operate jointly: Art. 17
    supplies the data-subject trigger, Art. 5(1)(c)/(e) supply the
    controller principle, and Art. 28(3)(g) supplies the processor
    instrument.
  security_rationale: |
    The obligation in Art. 17, Art. 5(1)(c), Art. 5(1)(e) and Art. 28(3)(g) to render personal data unattainable once the data subject's erasure conditions are met or the storage purpose has run its course is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.DS-10 captures the runtime-protection layer that erasure must extend through: protection against residual exposure during query and join operations is the prerequisite for a defensible cryptographic-erasure posture, because if the in-use protections fail the controller cannot claim the additional information held under separate technical and organisational control was effective.
    PR.DS-12 captures the lifecycle-management layer: a documented deletion procedure keyed to the Art. 17 trigger conditions and the Art. 5(1)(e) purpose-end moment, with cryptographic key destruction as the operational realisation of `deletes` for any system where per-copy destruction is not feasible across backups and replicas.
    A controller that documents PR.DS-10 in-use key-custody discipline and PR.DS-12 deletion-procedure coverage, including key-destruction for backups, can demonstrate ex post, against the Art. 5(2) accountability duty, that the Art. 17 trigger conditions and Art. 28(3)(g) processor-side mirror were honoured at the cryptographic layer on the day of any supervisory inspection.
  ambiguity_notes: |
    `deletes` in Art. 28(3)(g) carries Berry-flagged POLY-S3 (Berry
    §3.3.1) with three operational senses — physical destruction of the
    storage medium, logical deletion (recoverable through file-system or
    forensic tools), and cryptographic erasure (destruction of the
    cryptographic key rendering the underlying data unintelligible). The
    reading adopted for this SR is the cryptographic-erasure reading:
    key destruction, with the key held outside the data substrate, is the
    most defensible interpretation because it scales across backups and
    replicas without per-copy destruction and aligns with EDPB Guidelines
    5/2020 on storage limitation. Two alternative readings remain. First,
    the strict physical-destruction reading would require shredding of
    every storage medium that ever held the data; this conflicts with
    modern cloud-architecture realities where data is replicated across
    many media. Second, the logical-deletion reading would accept
    file-system-level deletion as sufficient; this conflicts with EDPB
    guidance because forensic recovery remains feasible. Remain open:
    (a) whether cryptographic erasure satisfies Art. 17(1) where the
    controller still holds the encryption key (likely not); (b) whether
    backup tapes with deleted-file markers are erased under Art. 28(3)(g)
    when full tape overwrite has not occurred.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-031
  title: "Processor erasure or return at end of processing services"
  source_clauses:
    - { clause_id: GDPR-CP10, article_ref: "Art. 28(3)(g)" }
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-019]
  sub_domain: [D-05.3, D-06.3]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-CONTRACT-END]
  regulatory_rationale: |
    Art. 28(3)(g) requires the processor, at the choice of the
    controller, to delete or return all the personal data after the end
    of the provision of services relating to processing, and to delete
    existing copies unless Union or Member State law requires storage of
    the personal data. The provision operates at the contract-end moment
    and binds the processor directly without requiring a separate
    data-subject request. Art. 5(1)(e) storage limitation and Art. 5(1)(c)
    data minimisation provide the upstream principles that justify the
    contract-end cleanup. The processor is the operational agent; the
    controller chooses between deletion and return; backup copies are
    within scope unless protected by separate Union or Member State law.
  security_rationale: |
    The obligation in Art. 28(3)(g), Art. 5(1)(e) and Art. 5(1)(c) to erase or return every copy of personal data at the contract-end moment, unless Union or Member State law mandates continued storage, is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**, with PR.DS-10 as the substrate protection.
    PR.DS-10 captures the runtime-protection precondition: any contract-end erasure must be capable of extending through in-use data paths (active replicas, query caches, processing pipelines), which is the operational substrate on which the cryptographic key-destruction choice for `deletes` rests.
    GV.SC-04 anchors the processor-side third-party-evidence practice: erasure must be verifiable — confirmable by audit, test result, or independent inspection — so that the controller can demonstrate, against Art. 5(2), that the post-contract data residue on processor systems was actually removed on the documented date.
    A processor that documents PR.DS-10 in-use data-path coverage and GV.SC-04 evidentiary confirmation of the contract-end deletion can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day any supervisory inspection occurs the personal data under its custody no longer exists in any backup or replica beyond the carved-out legal retention sets.
  ambiguity_notes: |
    The same Berry-flagged POLY-S3 on `deletes` attaches here as in
    SR-GDPR-030 (Berry §3.3.1), and the cryptographic-erasure reading is
    preserved. `all the personal data` and `existing copies` together
    carry SCOPE-Q S2 because both are universal quantifiers (Berry &
    Kamsties 2000): do backups count, do derived datasets count, do audit
    logs count. The reading adopted for this SR treats backups as in
    scope unless protected by a separate legal storage obligation, and
    treats audit logs as out of scope to the extent they are needed for
    legal-accountability purposes. Two alternative readings remain.
    First, the controller-absolute reading would require the processor
    to erase even logs that the controller might need for accountability;
    this conflicts with Art. 28(3)(g)'s exception for storage required by
    Union or Member State law. Second, the processor-discretion reading
    would allow the processor to retain backups indefinitely on the
    grounds of operational convenience; this conflicts with Art. 5(1)(e).
    Remain open: (a) whether immutable audit logs (WORM) escape the
    erasure obligation or must be technically erasable from inception; (b)
    whether derived datasets (aggregated analytics) fall under `all the
    personal data` when the underlying records are pseudonymised.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-032
  title: "Structured electronic access copy in commonly used format"
  source_clauses:
    - { clause_id: GDPR-RT09, article_ref: "Art. 15(1)/(3) — copy provision and format" }
    - { clause_id: GDPR-RT10, article_ref: "Art. 15(3) — commonly used electronic form" }
  linked_objectives: [SO-GDPR-020]
  sub_domain: [D-05.4]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 15(1) grants the data subject the right to obtain from the
    controller confirmation as to whether personal data concerning them
    is being processed and access to that data. Art. 15(3) requires the
    controller to provide a copy of the personal data undergoing
    processing and, where the request is by electronic means, to provide
    the information in a commonly used electronic form unless the data
    subject requests otherwise. The controller may charge a reasonable
    fee based on administrative costs for any further copies. The
    provision is the data-subject-facing access right; the Art. 20
    portability right is distinct and broader in scope.
  security_rationale: |
    The obligation in Art. 15(1) and Art. 15(3) to deliver a copy of personal data undergoing processing in a commonly used electronic form, on request and without undue delay, is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.DS-10 captures the runtime integrity posture: any export pipeline must be able to read live data under controlled exposure so that the copy delivered reflects current processing truth rather than stale snapshot drift, with proper handling for partial-views derived from the same in-use data set.
    PR.DS-12 captures the data-management posture: the export pipeline is governed by the same risk strategy as the data it is exposing, with structured, commonly used formats (JSON, CSV, XML) layered into the data-handling substrate rather than treated as ad-hoc report outputs, ensuring the copy is machine-readable and downstream-tool-friendly without sacrificing security classification discipline.
    A controller that documents PR.DS-10 in-use export controls and PR.DS-12 format-selection policy can demonstrate ex post, against the Art. 5(2) accountability duty, that any Art. 15(3) export request was honoured at the data-handling quality and at the format-quality the provision requires on the day of any data-subject complaint or supervisory inspection.
  ambiguity_notes: |
    `commonly used electronic form` carries Berry-flagged VAG-S3 on
    format open-texture. The reading adopted for this SR is the
    structured-interoperable reading: JSON, CSV or XML, in line with
    EDPB Guidelines 06/2020 on data portability (which interpret the
    parallel Art. 20 phrase). The structured-interoperable reading is
    preferred over a PDF-style free-text rendering because it preserves
    machine-readability and aligns with the practical purpose of
    cross-provider migration. Two alternative readings remain. First, a
    print-ready rendering (PDF or scanned image) of the data would
    satisfy the literal text but defeat the purpose of the access right
    and the EDPB guidance. Second, a controller-preferred proprietary
    format that the data subject cannot easily open would technically
    comply but functionally obstruct; EDPB Guidelines 06/2020 reject
    this. Remain open: (a) whether open formats like Parquet or NDJSON
    count as `commonly used` for non-technical data subjects; (b) whether
    the obligation extends to inferred data (scores, profiles) or only to
    data the data subject explicitly provided.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-033
  title: "Processor due diligence with documented sufficient guarantees"
  source_clauses:
    - { clause_id: GDPR-CP07, article_ref: "Art. 28(1) — processor selection" }
    - { clause_id: GDPR-CP08, article_ref: "Art. 28(2) — sub-processor authorisation" }
    - { clause_id: GDPR-C03, article_ref: "Art. 4(7)/(8) — controller/processor" }
  linked_objectives: [SO-GDPR-021]
  sub_domain: [D-06.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-PROCESSOR]
  regulatory_rationale: |
    Art. 28(1) requires the controller to use only processors providing
    sufficient guarantees to implement appropriate technical and
    organisational measures in such a manner that processing will meet
    the requirements of GDPR and ensure the protection of data-subject
    rights. Art. 28(2) requires processor authorisation for any
    sub-processor. Art. 4(7) and 4(8) supply the controller and processor
    definitions on which Art. 28 rests.
  security_rationale: |
    The obligation in Art. 28(1), Art. 28(2) and Art. 4(7)/(8) to engage only processors offering sufficient guarantees and to authorise each sub-processor engagement is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-02 is the due-diligence discipline: the controller prioritises processors against risk, applies a documented evaluation (questionnaire, certifications review, security-measures audit, sub-processor inventory) and records the sufficient-guarantees evidence before engagement so the threshold is verifiable rather than self-declared.
    GV.SC-03 is the contractual-realisation discipline: the Art. 28(3) clauses become the formal instrument through which the controller binds the processor — and through which the processor is required to bind its sub-processors — so that the guarantees assessed at selection survive into the operational relationship and through any subsequent processor change.
    A controller that documents GV.SC-02 evidence-of-sufficient-guarantees per processor and GV.SC-03 sub-processor authorisation discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that every processor relationship in force on the day of any supervisory inspection had been selected against a defensible sufficient-guarantees threshold and conducted through an enforceable contractual instrument.
  ambiguity_notes: |
    `sufficient guarantees` carries Berry-flagged VAG-S2 (Berry §5.1);
    EDPB Guidelines 07/2020 propose factors, including commitment to
    GDPR, technical and organisational measures, transparency and
    ability to assist the controller, but the threshold is qualitative.
    The reading adopted for this SR is the documented-due-diligence
    practice: written due-diligence questionnaire, certifications
    review, security-measures audit, sub-processor inventory, and
    contractual Art. 28(3) clauses. An alternative reading under which
    controller self-attestation without independent verification is
    sufficient would lose the substantive protection the threshold is
    meant to provide. Remain open: whether certification schemes (ISO
    27701, SOC 2) on their own satisfy `sufficient guarantees` or
    whether the controller must layer additional assessment.
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
- sr_id: SR-GDPR-036
  title: "Sub-processor authorisation with controller change-notification"
  source_clauses:
    - { clause_id: GDPR-CP08, article_ref: "Art. 28(2) — sub-processor authorisation" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(d) — sub-processor conditions (cross)" }
  linked_objectives: [SO-GDPR-022]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-SUB-PROCESSOR]
  regulatory_rationale: |
    Art. 28(2) requires the processor not to engage another processor
    without prior specific or general written authorisation of the
    controller. In the case of general written authorisation, the
    processor must inform the controller of any intended changes
    concerning the addition or replacement of other processors,
    thereby giving the controller the opportunity to object to such
    changes. Art. 28(3)(d) requires the contract to respect the
    conditions for engaging another processor (i.e., flow the (2) and
    (4) rules into the processor contract).
  security_rationale: |
    The obligation in Art. 28(2) and Art. 28(3)(d) to obtain the controller's prior written authorisation before engaging another processor, and to notify the controller of any change in the case of general authorisation so that the controller has an opportunity to object, is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-02 captures the prioritisation and assessment discipline: every sub-processor must be known, prioritised against the data it will touch, and assessed using the SCRM process before it is engaged, so that the full chain of entities with personal-data access is visible to and acceptable to the controller.
    GV.SC-03 captures the contract-flowing discipline: the sub-processor authorisation requirement is not merely a one-time notice — it must appear on the face of the contract between controller and processor, with the same written-authorisation and notification-of-change mechanics that the substantive provision requires, so that the controller's object right is exercisable throughout the relationship rather than only at onboarding.
    A processor that documents GV.SC-02 sub-processor assessment on each engagement and GV.SC-03 contract-anchored authorisation plus change-notification discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the personal-data access chain was complete, documented and within the controller's objectable scope.
  ambiguity_notes: |
    `prior specific or general written authorisation` carries VAG+SCOPE-Q
    S2 (Berry §5.1): the `specific` versus `general` distinction is the
    same as the Art. 6(1)(a) consent-specificity question. The reading
    adopted for this SR is that written authorisation in either form is
    acceptable, with notification-on-changes required in the general case
    (EDPB Guidelines 07/2020). An alternative reading under which only
    `specific` authorisation suffices for sensitive data flows would
    tighten the obligation but conflicts with the OJ text, which makes
    the general authorisation path explicit. Remain open: whether
    `opportunity to object` requires a reasonable objection window (e.g.,
    30 days) or whether silent acquiescence suffices.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-037
  title: "Controller-evidenced processor erasure on contract end"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(g) — return or deletion" }
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation" }
  linked_objectives: [SO-GDPR-022, SO-GDPR-019]
  sub_domain: [D-06.3, D-05.3]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits and test results" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-CONTRACT-END]
  regulatory_rationale: |
    Art. 28(3)(g) duplicates the processor-end-of-services obligation
    already captured under SR-GDPR-031, and is included here as a
    contract-obligations-cluster rule to support controller-side
    contract drafting. The substantive obligation is identical: at the
    choice of the controller, the processor must delete or return all
    the personal data after the end of the provision of services
    relating to processing, and must delete existing copies unless
    Union or Member State law requires storage. Art. 5(1)(e) storage
    limitation provides the upstream principle. This rule anchors the
    controller-side audit-and-evidence obligation: the controller must
    verify, at contract end and periodically, that the processor has
    in fact deleted or returned the data and has documented the basis
    for any continued retention.
  security_rationale: |
    The obligation in Art. 28(3)(g) and Art. 5(1)(e), approached from the controller-side audit-and-evidence angle, to verify that the processor has honoured its contract-end erasure-or-return duty and to hold evidence supporting any continued retention claim is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**.
    PR.DS-12 captures the data-management spine on which the controller's evidence pack rests: the controller treats the post-contract residual data set as a discrete risk-strategy object whose erasure or continued-retention status must be documented per category, including the legal-storage carve-out justifications.
    GV.SC-04 captures the routine third-party assessment posture: contract-end erasure is one instance of an ongoing third-party-evaluation cadence, and the controller must be able to call on audit, test result, or independent inspection evidence at the moment of any data-subject or supervisory query — not merely at the moment of contract end.
    A controller that documents PR.DS-12 per-category erasure evidence and GV.SC-04 periodic third-party-verification cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the processor's contract-end deletion or return was both verified and recorded.
  ambiguity_notes: |
    No new ambiguity beyond the SR-GDPR-030 POLY-S3 on `deletes`
    (Berry §3.3.1), and the cryptographic-erasure reading is preserved.
    The reading adopted here is the same: cryptographic erasure,
    understood as destruction of the cryptographic key held outside the
    data substrate, is the most defensible operational interpretation
    because it scales to backups and replicas without per-copy
    destruction, in line with EDPB Guidelines 5/2020 on storage
    limitation. Two alternative readings — strict physical destruction,
    which conflicts with cloud-architecture realities, and logical
    deletion, which conflicts with EDPB guidance — are preserved here
    for symmetry with SR-GDPR-030. The substantive novelty at
    SR-GDPR-037 is the controller-side audit-and-evidence obligation
    rather than the deletion mechanics. Remain open: (a) whether the
    controller must obtain affirmative evidence-of-erasure certificates
    per data category or whether a single processor attestation
    suffices; (b) how the controller should handle the gap between
    contract end and the processor's actual deletion confirmation.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-038
  title: "Written EU representative for non-EU controllers and processors"
  source_clauses:
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(1) — designate in writing" }
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(2)(a) — occasional exception" }
  linked_objectives: [SO-GDPR-023]
  sub_domain: [D-06.4, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-02, title: "Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
  applies_to_role: [NON_EU_CONTROLLER, NON_EU_PROCESSOR]
  obligation_type: [CONTINUOUS, PER-PROCESSING-ACTIVITY]
  regulatory_rationale: |
    Art. 27(1) requires, where Art. 3(2) applies (offering goods or
    services to EU data subjects, or monitoring their behaviour,
    regardless of whether the processing takes place in the Union), the
    controller or processor to designate in writing a representative in
    the Union. Art. 27(2)(a) provides the exception for processing which
    is occasional, does not include, on a large scale, processing of
    special categories of data as referred to in Art. 9(1) or processing
    of personal data relating to criminal convictions and offences
    referred to in Art. 10, and is unlikely to result in a risk to the
    rights and freedoms of natural persons, taking into account the
    nature, context, scope and purposes of the processing. Art. 27(2)(b)
    carves out public authorities or bodies.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or processing of personal data relating to criminal convictions and offences referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons]
  security_rationale: |
    The obligation in Art. 27(1) and Art. 27(2)(a) for any non-EU controller or processor covered by Art. 3(2) to designate in writing a Union-based representative, unless the conjunctive occasional, small-scale, low-risk exception is satisfied, is operationalised in NIST CSF 2.0 through **GV.OC-02 (Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered)** and **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced)**.
    GV.OC-02 captures the stakeholder-recognition discipline: the non-EU controller treats EU data subjects, supervisory authorities and the designated representative as standing stakeholders whose needs (point of contact, address for enforcement, language of communication) must be understood and documented before processing begins, so that the representative function is operationally real rather than a paper address.
    GV.RR-02 captures the role-accountability discipline: the representative role carries authorities and responsibilities for handling supervisory-authority correspondence, data-subject requests and incident notifications, with the mandate of Art. 27(1) made enforceable through documented communication channels and refusal-to-act safeguards.
    A non-EU controller that documents GV.OC-02 stakeholder identification and GV.RR-02 representative-mandate clarity can demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 3(2) jurisdictional anchor, that on the day of any supervisory action the designated representative was operationally present and properly authorised.
  ambiguity_notes: |
    `occasional`, `large scale` and `unlikely to result in a risk` (Art.
    27(2)(a)) carry VAG+SCOPE-Q S3 (Berry §5.1): three inquiry-resistant
    qualifiers combined with AND. The exception requires all three to be
    in the controller's favour for the exception to apply — i.e.,
    occasional AND small-scale AND low-risk — and the OJ additionally
    ties `large scale` to the special-category and criminal-conviction
    carve-outs. The reading adopted for this SR is the conjunctive
    reading: each qualifier must hold individually; `occasional` is read
    as not regular or periodic (EDPB Guidelines 3/2018); `large scale`
    follows the EDPB Guidelines 9/2022 factors (number of data subjects,
    volume of data, geographic range, duration); and `unlikely` is read
    as non-negligible risk absent. Two alternative readings remain.
    First, a disjunctive reading under which any one of the three would
    suffice to trigger the exception would conflict with the OJ text,
    which is conjunctive (the negative construction `shall not apply`
    applies only when all three conditions hold). Second, a literal-
    procedural reading that treats `unlikely` as `more probable than
    not` would expand the exception inappropriately. Remain open: (a)
    whether a SaaS offering with a freemium tier counts as `occasional`
    when only a small fraction of EU users sign up; (b) whether
    behavioural monitoring of EU employees of a non-EU employer triggers
    Art. 27 irrespective of the exception's `risk` prong.
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
- sr_id: SR-GDPR-041
  title: "Privacy by default across four coordinated minimisation dimensions"
  source_clauses:
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — by-default limits" }
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — by-design (cross)" }
  linked_objectives: [SO-GDPR-024, SO-GDPR-007]
  sub_domain: [D-07.1, D-03.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.PS-06, title: "Secure software development practices integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 25(2) is the privacy-by-default mandate: only personal data
    which are necessary for each specific purpose of the processing are
    processed, with no indefinite accessibility absent data-subject
    intervention. That obligation applies to four coordinated
    dimensions: the amount of personal data collected, the extent of
    their processing, the period of their storage, and their
    accessibility. In particular, the measures shall ensure that by
    default personal data are not made accessible without the
    individual's intervention to an indefinite number of natural
    persons. Art. 25(1) by-design is the upstream obligation; Art.
    25(2) by-default is its operational manifestation at configuration
    time.
  security_rationale: |
    The obligation in Art. 25(2), read with Art. 25(1), to bind each personal-data collection to what is necessary for each specific purpose and to ensure that, by default, personal data are not made accessible without the data subject's intervention to an indefinite number of natural persons — across the four coordinated dimensions of amount, extent, period and accessibility — is operationalised in NIST CSF 2.0 through **PR.PS-01 (Configuration management practices are established, documented, and applied to assets)** and **PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the SDLC)**.
    PR.PS-01 captures the by-default configuration discipline: every default setting that affects personal-data exposure — collection scope, processing extent, retention horizon, accessibility — must be set to the least-intrusive option, with configuration changes rather than per-transaction decisions altering the posture.
    PR.PS-06 captures the upstream design-time anchor: the four coordinated dimensions are not all reachable by configuration alone, because the design of the data flow itself constrains what the configuration can do. Art. 25(1) by-design must therefore establish the architecture in which PR.PS-01 by-default configurations can operate.
    A controller that documents PR.PS-01 default-closed configuration per dimension and PR.PS-06 design-time alignment of those defaults to the four coordinated dimensions can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any processing operation the by-default posture was actually the least-intrusive posture the specific purpose permitted.
  ambiguity_notes: |
    GDPR-CP03 (Art. 25(2)) carries Berry-flagged S3 VAG+COORD on
    `necessary for each specific purpose` combined with four coordinated
    dimensions (amount, extent, period, accessibility). The reading
    adopted for this SR is the all-four-dimensions-individually-
    minimised reading (per EDPB Guidelines 04/2019): each dimension is
    independently bounded to what is necessary for the specific purpose,
    and the four constraints are AND-coordinated minima. Two
    alternative readings remain. First, a trade-off reading under which
    some dimensions can be relaxed if others are tightened would
    conflict with the OJ text, which lists the dimensions as
    AND-coordinated minima. Second, a single-purpose reading that
    treats the four dimensions as a single obligation would lose the
    granular controls each dimension provides. Remain open: (a) whether
    `accessibility` requires default-deny-on-API or accepts default-
    allow-with-policy; (b) how `extent of processing` is operationalised
    for AI-training pipelines where the necessary extent cannot be
    specified in advance.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-042
  title: "DPO-driven GDPR awareness and role-specific training"
  source_clauses:
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(b) — awareness and training" }
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(a) — inform and advise" }
  linked_objectives: [SO-GDPR-025]
  sub_domain: [D-08.1, D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics" }
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
  applies_to_role: [DPO, CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 39(1)(b) requires the DPO to monitor compliance with GDPR,
    including the assignment of responsibilities, awareness-raising, and
    training of staff involved in processing operations. Art. 39(1)(a)
    requires the DPO to inform and advise the controller or processor
    and the employees who carry out processing of their obligations
    pursuant to GDPR and to other Union or Member State data protection
    provisions. The two sub-paragraphs together establish the DPO's
    role as the internal awareness and training catalyst, distinct
    from the controller's substantive training obligation.
  security_rationale: |
    The obligation in Art. 39(1)(a) and Art. 39(1)(b), on the DPO acting as the internal advisor and awareness-and-training catalyst for staff involved in processing, is operationalised in NIST CSF 2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity topics, e.g. recognition of phishing, social engineering, and other relevant risks)** and **PR.AT-02 (All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives)**.
    PR.AT-01 captures the broad-coverage discipline: the DPO's awareness-raising obligation is structurally a general-population training duty covering all personnel involved in processing, on a recurring cadence and with content that updates to reflect emerging threats and the changing data flows of the organisation.
    PR.AT-02 captures the role-specific layer that PR.AT-01 cannot cover: personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities need role-specific reinforcement of their GDPR and cybersecurity obligations, distinct from the general awareness programme.
    A controller or processor that documents PR.AT-01 general-population awareness cadence and PR.AT-02 role-specific training records can demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 39(1) DPO mandate, that the DPO's awareness-and-training function was operationally exercised and recorded on the day of any supervisory inspection.
  ambiguity_notes: |
    `awareness-raising` and `training` carry Berry-flagged POLY+VAG-S2
    (Berry §5.1): both terms have a recurrent GDPR polysemy. The
    reading adopted for this SR splits the obligation into two: (1)
    general awareness training on GDPR for all personnel involved in
    processing, on an annual basis; and (2) role-specific training for
    personnel with data-subject-facing or access-management
    responsibilities, on a quarterly or event-triggered basis. An
    alternative reading under which one-off induction training
    suffices would conflict with the `awareness-raising` qualifier,
    which implies ongoing reinforcement. Remain open: whether `staff
    involved in processing` includes board members and senior
    management in the awareness scope, or only operational personnel.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-043
  title: "Appropriate technical and organisational measures under Art. 24(1)"
  source_clauses:
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(1) — appropriate measures" }
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(2) — appropriate data-protection policies" }
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability (cross)" }
  linked_objectives: [SO-GDPR-026]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.RM-04, title: "Strategic direction that describes how to identify and respond to risks is established and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 24(1) requires the controller, taking into account the nature,
    scope, context and purposes of processing as well as the risks of
    varying likelihood and severity for the rights and freedoms of
    natural persons, to implement appropriate technical and
    organisational measures to ensure and to be able to demonstrate
    that processing is performed in accordance with GDPR; those
    measures shall be reviewed and updated where necessary. Art. 24(2)
    further requires, where proportionate in relation to processing
    activities, the implementation of appropriate data-protection
    policies by the controller. Art. 5(2) accountability anchors the
    demonstrability requirement. The Article is the operational-
    responsibility centrepiece: it sets the controller's overarching
    obligation and ties it to demonstrability.
  security_rationale: |
    The obligation in Art. 24(1), Art. 24(2) and Art. 5(2) to implement appropriate technical and organisational measures, supported by proportionate data-protection policies and reviewed and updated where necessary, so that processing is performed in accordance with GDPR and the controller can demonstrate compliance, is operationalised in NIST CSF 2.0 through **GV.PO-01 (Organizational cybersecurity policy is established, communicated, and enforced)**, **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.RM-04 (Strategic direction that describes how to identify and respond to risks is established and communicated)**.
    GV.PO-01 captures the policy-document discipline: every controller has a communicated, current, enforced cybersecurity-and-data-protection policy anchored on the Art. 24(2) proportionality test, without which the controller cannot demonstrate either the existence or the enforcement of its overall posture.
    GV.PO-02 captures the operational-procedure layer: each policy must be backed by documented processes and procedures — incident response, breach notification, data-subject rights, retention, processor onboarding — so that the policy is real rather than paper.
    GV.RM-04 captures the strategic-direction and review obligation in Art. 24(1) "where necessary": the controller must communicate how it identifies and responds to risks, including the cadence and triggers for policy and procedure refresh, which is precisely the strategic-direction and update-coupling that GV.RM-04 prescribes.
    A controller that documents GV.PO-01 policy coverage, GV.PO-02 process coverage and GV.RM-04 review cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the controller's overall cybersecurity-and-data-protection posture was both current and proportionate to the risks.
  ambiguity_notes: |
    `where necessary` (review cadence) carries Berry-flagged VAG-S3
    (Berry §5.1). The reading adopted for this SR is the
    material-change-of-risk trigger supplemented by annual periodic
    review (EDPB Guidelines 07/2019 on accountability). The trigger
    threshold is qualitative — change in processing, change in risk
    landscape, change in legal environment — but the EDPB Guidelines
    07/2019 suggest materiality as the operative threshold. Two
    alternative readings remain. First, a periodic-only reading would
    set an annual review and lose the material-change responsiveness;
    this reading is acceptable as a minimum but insufficient for
    high-risk processing. Second, a continuous-review reading would be
    impractical for most controllers and would not add substantive
    protection beyond the material-change trigger. Remain open: (a)
    whether the `where necessary` review obligation creates a per-
    incident trigger (post-incident review) or only an aggregate-change
    trigger; (b) whether `appropriate data-protection policies` (Art.
    24(2)) requires a single umbrella policy or can be split across
    operational policies.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-044
  title: "Continuous evidence-of-compliance with performance review"
  source_clauses:
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability" }
    - { clause_id: GDPR-CP01, article_ref: "Art. 24(1) — demonstrate compliance (cross)" }
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(1) — records of processing (cross)" }
  linked_objectives: [SO-GDPR-027]
  sub_domain: [D-09.1, D-10.2]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(2) requires the controller to be responsible for, and able to
    demonstrate, compliance with the Art. 5(1) principles (lawfulness,
    fairness and transparency; purpose limitation; data minimisation;
    accuracy; storage limitation; integrity and confidentiality; and
    accountability). Art. 24(1) extends the demonstrability requirement
    to all GDPR compliance, not just Art. 5(1). Art. 30(1) supplies the
    supporting evidence instrument in the form of the records of
    processing. The three provisions together create the accountability-
    and-evidence chain that grounds the entire supervisory-authority
    enforcement regime (Art. 58 powers of investigation; Art. 83
    administrative fines).
  security_rationale: |
    The obligation in Art. 5(2), Art. 24(1) and Art. 30(1) to be able to demonstrate, on a continuous basis, that the controller is complying with the Art. 5(1) principles and with the rest of GDPR, and to maintain the records of processing as the supporting evidence instrument, is operationalised in NIST CSF 2.0 through **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.OV-03 (Organizational cybersecurity performance is evaluated and reviewed for needed adjustments)**.
    GV.PO-02 captures the procedural-evidence backbone: the controller must maintain evidence-generating processes — RoPA entries, DPIA artefacts, audit logs, training records, breach-response records — on a continuous basis, because the demonstrability threshold set by Art. 5(2) and Art. 24(1) is not a point-in-time promise but a standing capability.
    GV.OV-03 captures the evaluated-and-reviewed-correction dimension that converts raw evidence into accountability: the controller's performance against the cybersecurity and data-protection objectives must be measured and adjusted, with the adjustments materialising as refreshed policies, processes and procedures rather than as isolated interventions.
    A controller that documents GV.PO-02 continuous-evidence processes and GV.OV-03 performance-evaluation-and-correction cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the controller could produce evidence of compliance across the entire Art. 5(1) principles chain and the broader GDPR surface that Art. 24(1) reaches.
  ambiguity_notes: |
    `able to demonstrate` carries Berry-flagged VAG-S3 (Berry §5.1) on
    the threshold of evidence sufficient. The reading adopted for this
    SR is the continuous-evidentiary-trail reading: logs, audit reports,
    certifications, DPIA artefacts, RoPA entries, training records and
    breach-response records, all preserved on a continuous basis per
    EDPB Guidelines on accountability 07/2019. Two alternative readings
    remain. First, a point-in-time reading that treats `able to
    demonstrate` as satisfied by the existence of policies without
    evidence of operation would lose the substantive protection the
    accountability principle is meant to provide. Second, an annual-
    evidence reading that aggregates evidence only at supervisory-
    authority-request time would conflict with the continuous-monitoring
    expectations of EDPB Guidelines 07/2019. Remain open: (a) whether
    internal audit reports fall under legal-professional privilege for
    accountability purposes or must be disclosed to supervisory
    authorities on request; (b) whether the demonstrability threshold
    differs between Art. 5(2) (principles compliance) and Art. 24(1)
    (full GDPR compliance).
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-045
  title: "Pre-launch DPIA with risk treatment and prior-consultation trigger"
  source_clauses:
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — DPIA trigger" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation (cross)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-028]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED, PERIODIC]
  regulatory_rationale: |
    Art. 35(1) requires the controller to carry out an assessment of
    the impact of the envisaged processing operations on the protection
    of personal data, prior to processing, where the processing is
    likely to result in a high risk to the rights and freedoms of
    natural persons, in particular using new technologies. Art. 35(7)
    specifies the four content items: a systematic description of the
    processing and purposes; an assessment of necessity and
    proportionality; an assessment of the risks to data-subject
    rights; and the measures envisaged to address the risks. Art. 36(1)
    requires prior consultation with the supervisory authority where
    the DPIA indicates that processing would result in a high risk in
    the absence of mitigation measures. Art. 4(1) supplies the personal-
    data definition on which the DPIA scope rests.
  security_rationale: |
    The obligation in Art. 35(1), Art. 35(7) and Art. 36(1) to carry out a pre-launch data-protection impact assessment for processing likely to result in a high risk, covering the four Art. 35(7) content items, and to consult the supervisory authority where the residual risk remains high, is operationalised in NIST CSF 2.0 through **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)**, **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated)**.
    ID.RA-01 captures the asset-level vulnerability-recording discipline: the DPIA's systematic-description requirement (Art. 35(7)(a)) is operationally the same as the vulnerability-recording posture that the controller maintains for the data, processing and supporting assets under assessment.
    ID.RA-05 captures the inherent-risk understanding requirement in Art. 35(7)(c): threats (including new-technology exposures), vulnerabilities, likelihoods and impacts must be brought together to understand the inherent risk envelope of the processing, before any risk-response measure is layered on top.
    ID.RA-06 captures the risk-response layer in Art. 35(7)(d) and Art. 36(1): the controller must choose, prioritise, plan and track the measures that address the identified risks, and where residual risk stays high the prior-consultation obligation under Art. 36(1) is triggered, with the supervisory authority becoming the next-step risk-response stakeholder.
    A controller that documents ID.RA-01 vulnerability coverage, ID.RA-05 inherent-risk assessment and ID.RA-06 risk-response selection plus Art. 36(1) consultation trigger can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any high-risk processing the controller had performed and refreshed the four-part DPIA and consulted the supervisory authority where the threshold was met.
  ambiguity_notes: |
    Source clause GDPR-CP21 carries Berry-flagged S3 POLY+VAG on `new
    technologies` and `high risk` (Berry §5.1, §3.3.1). `New
    technologies` is the recurring time-dependent phrase — was cloud
    `new` in 2018, is generative AI `new` in 2026. The reading adopted
    for this SR is that `new technologies` means technologies not
    widely deployed in the industry at the time of assessment (EDPB
    Guidelines 4/2019). `High risk` inherits the Art. 35(1) threshold,
    with the EDPB Guidelines 4/2019 nine-criteria list as the
    operational anchor (evaluation and scoring, automated decision-
    making with legal effect, systematic monitoring, sensitive data or
    data of a vulnerable nature, data processed on a large scale,
    combination of data, data concerning vulnerable data subjects,
    innovative use or applying new technological or organisational
    solutions, and processing that prevents data subjects from
    exercising a right or using a service). Two alternative readings
    remain. First, a strict supervisory-list reading would limit DPIA
    triggers to those listed by the national supervisory authority
    under Art. 35(4); this conflicts with Art. 35(1), which is open-
    textured. Second, a controller-discretion reading that treats the
    EDPB criteria as illustrative would weaken the high-risk threshold.
    Remain open: (a) whether generative-AI model training falls inside
    or outside `new technologies` in 2026; (b) whether a single DPIA
    may legitimately cover a set of similar processing operations per
    Art. 35(1) when the operations span multiple controllers in a
    joint-controllership arrangement.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-046
  title: "Four-element DPIA content with necessity and proportionality test"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7)(a)–(d) — DPIA content" }
  linked_objectives: [SO-GDPR-028]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-DPIA]
  regulatory_rationale: |
    Art. 35(7) requires the DPIA to contain at least: (a) a systematic
    description of the envisaged processing operations and the purposes
    of the processing, including, where applicable, the legitimate
    interest pursued by the controller; (b) an assessment of the
    necessity and proportionality of the processing operations in
    relation to the purposes; (c) an assessment of the risks to the
    rights and freedoms of data subjects referred to in paragraph 1;
    (d) the measures envisaged to address the risks, including
    safeguards, security measures and mechanisms to ensure the
    protection of personal data and to demonstrate compliance with this
    Regulation taking into account the rights and legitimate interests
    of data subjects and other persons concerned.
  security_rationale: |
    The obligation in Art. 35(7)(a)–(d) to construct each DPIA on the four mandated elements — systematic description, necessity and proportionality assessment, risks-to-data-subjects assessment, and measures-envisaged — is operationalised in NIST CSF 2.0 through **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **RS.AN-03 (Analysis is performed to determine what has occurred during an event and the root cause of the event)**.
    ID.RA-05 captures the structured-risk-assessment spine of Art. 35(7)(b) and (c): the controller must assemble threats, vulnerabilities, likelihoods and impacts into a coherent inherent-risk picture before designing measures, which is precisely the necessity-and-proportionality analysis and the risks-to-data-subjects assessment that the two sub-letters require.
    RS.AN-03 captures the measures-envisaged discipline in Art. 35(7)(d): the documentation of safeguards, security measures and mechanisms to demonstrate compliance is operationally a structured analysis of what each measure is designed to address and how it traces to a specific identified risk, with the trace preserved for inspection and for after-the-fact learning.
    A controller that documents ID.RA-05 threat-vulnerability-likelihood-impact assembly and RS.AN-03 measure-by-measure analysis linkage can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any high-risk processing the DPIA's four Art. 35(7) elements were each substantively populated and trace-linked rather than merely listed.
  ambiguity_notes: |
    `necessity and proportionality` carries Berry-flagged POLY-S2 — three
    different `necessity` senses appear across GDPR (Art. 5(1)(c) data
    minimisation, Art. 6(1)(b) contract, Art. 35(7)(b) DPIA) and the
    same term is operationalised differently in each. The reading
    adopted for this SR is the Art. 35(7)(b)-internal reading:
    necessity means no less-intrusive alternative achieves the purpose;
    proportionality means the processing's benefits justify its
    intrusiveness on data-subject rights. An alternative reading that
    imports the Art. 6(1)(b) contract-necessity standard would conflict
    with the DPIA-specific framing. Remain open: whether the
    proportionality prong requires quantified trade-off analysis (e.g.,
    cost-benefit) or accepts qualitative judgement.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-047
  title: "Risk-change-triggered DPIA review with periodic cadence"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(11) — DPIA review" }
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — DPIA trigger" }
  linked_objectives: [SO-GDPR-028, SO-GDPR-004]
  sub_domain: [D-09.2, D-10.3]
  nist_csf_mapping:
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PERIODIC, TRIGGERED]
  regulatory_rationale: |
    Art. 35(11) requires the controller, where necessary, to carry out
    a review to assess whether processing is performed in accordance
    with the data protection impact assessment at least when there is a
    change of the risk represented by processing operations. The
    provision triggers DPIA re-review on material risk change and links
    back to Art. 35(1)'s DPIA-trigger framework.
  security_rationale: |
    The obligation in Art. 35(11), read with Art. 35(1), to carry out a DPIA review where necessary, and at least when there is a change of the risk represented by the processing operations, is operationalised in NIST CSF 2.0 through **ID.IM-04 (Cybersecurity risk management improvements are informed by awareness of related developments and context, e.g. threat intelligence, incidents, technology evolution)** and **ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated)**.
    ID.IM-04 captures the forward-looking-improvement discipline: DPIA review is triggered not only by the controller's static risk picture but by contextual changes — threat-intelligence shifts, incidents in the wider environment, technology evolution — that the controller must bring into its improvement process and reflect in the DPIA's risk assessment.
    ID.RA-06 captures the risk-response-rerun layer: when a material change in risk is detected, the controller's risk-response set must be revisited — chosen, re-prioritised, re-planned, tracked against the new risk picture and communicated — so that the DPIA's measures-envisaged section stays current with the live risk envelope of the processing.
    A controller that documents ID.IM-04 contextual-change monitoring and ID.RA-06 risk-response-rerun cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any material change in the risk the DPIA had been refreshed and the measures it envisages had been re-evaluated rather than carried over unchanged.
  ambiguity_notes: |
    `where necessary` carries Berry-flagged VAG without an explicit S3
    tag in the chapter-4 analysis, and the same compliance practice
    applies across readings. The reading adopted for this SR treats
    material change in risk as the primary trigger, supplemented by
    periodic review (annual). An alternative reading under which only
    annual review applies would satisfy the periodic-review obligation
    but lose responsiveness to material change. Remain open: whether
    the change-of-risk trigger requires the controller to re-perform
    the full Art. 35(7) content set or to update only the changed
    dimensions.
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

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-050
  title: "Integrity-preserved RoPA records available to supervisory authority"
  source_clauses:
    - { clause_id: GDPR-CP12, article_ref: "Art. 30(3) — in writing/electronic form" }
    - { clause_id: GDPR-CL07, article_ref: "Art. 5(2) — accountability (cross)" }
    - { clause_id: GDPR-CP14, article_ref: "Art. 31 — supervisory authority cooperation" }
  linked_objectives: [SO-GDPR-031]
  sub_domain: [D-10.2, D-09.4]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.AE-03, title: "Event data are collected and correlated from multiple sources and sensors" }
    - { id: RS.AN-07, title: "Incident data and metadata are collected, and their integrity and provenance are preserved" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 30(3) requires the records referred to in paragraphs 1 and 2
    to be in writing, including in electronic form. Art. 5(2)
    accountability requires the controller to demonstrate compliance;
    the records are the primary evidence. Art. 31 requires cooperation
    with the supervisory authority, on request, in the performance of
    its tasks, including on inspection. The three provisions together
    set the integrity and availability baseline for the RoPA itself.
  security_rationale: |
    The obligation in Art. 30(3), Art. 5(2) and Art. 31 to keep the records of processing in writing (including in electronic form), to treat them as the primary evidence supporting the Art. 5(2) accountability duty, and to make them available to the supervisory authority on request under the Art. 31 cooperation duty, is operationalised in NIST CSF 2.0 through **PR.PS-04 (Log records are generated and made available for continuous monitoring and analysis)**, **DE.AE-03 (Event data are collected and correlated from multiple sources and sensors)** and **RS.AN-07 (Incident data and metadata are collected, and their integrity and provenance are preserved)**.
    PR.PS-04 captures the record-generation discipline: each RoPA entry must be generated and made available as log-grade record material, with continuous monitoring and analysis over it, rather than as a static document that ages between inspections.
    DE.AE-03 captures the multi-source correlation discipline: where the RoPA is maintained across multiple systems, the records must be collectable and correlatable into a single supervisory-authority-presentable view, so that Art. 31 cooperation does not stall on data-source fragmentation.
    RS.AN-07 captures the integrity-and-provenance discipline: records that the supervisory authority relies on must be tamper-evident and provenance-preserving, so that any update between inspections leaves a chain that supports the Art. 5(2) demonstrability requirement rather than weakens it.
    A controller or processor that documents PR.PS-04 log-grade RoPA generation, DE.AE-03 cross-source correlation and RS.AN-07 integrity-preservation discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the records were complete, current and integrity-preserved, satisfying the Art. 31 cooperation duty without reconstruction effort.
  ambiguity_notes: |
    `in writing, including in electronic form` is unambiguous; no S3
    ambiguity registered.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-065
  title: "Plain-language transparent privacy notice design"
  source_clauses:
    - { clause_id: GDPR-RT01, article_ref: "Art. 12(1) — transparency modalities" }
    - { clause_id: GDPR-CL01, article_ref: "Art. 5(1)(a) — transparency (cross)" }
  linked_objectives: [SO-GDPR-038]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-INTERACTION]
  regulatory_rationale: |
    Art. 12(1) requires the controller to take appropriate measures to provide any information referred to in Art. 13 and 14 and any communication under Arts. 15 to 22 and 34 relating to processing to the data subject in a concise, transparent, intelligible and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child; the information shall be provided in writing or by other means, including, where appropriate, by electronic means, and where requested by the data subject may be provided orally, provided that the identity of the data subject is proven by other means. Art. 5(1)(a) anchors transparency as one of the principles relating to processing.
  security_rationale: |
    The obligation in Art. 12(1) and Art. 5(1)(a) is operationalised in NIST CSF
    2.0 through **GV.PO-02 (Cybersecurity processes and procedures established,
    communicated, and enforced)** and **PR.AA-02 (Identities proofed and bound to
    credentials based on the context of interactions)**.

    GV.PO-02 controls the notice-design process: the controller must establish
    and enforce a documented procedure that produces layered, accessible notices
    meeting the six conjunctive Art. 12(1) form qualifiers — concise,
    transparent, intelligible, easily accessible, clear, and plain — with the
    child-specific heightened readability standard reflected in the design process
    for any service that targets or is likely to attract child users. PR.AA-02
    controls the identity-proofing dimension that Art. 12(1) introduces for
    oral-information provision: where the data subject requests information
    orally, the controller must proof the requester's identity by means other
    than the requested communication channel, treating the proofing step as a
    context-sensitive identity-binding.

    Together the two subcategories embed privacy-notice design in a documented,
    enforced process (GV.PO-02) backed by identity-proofing controls for
    non-written channels (PR.AA-02), enabling ex-post demonstration to the
    supervisory authority that the notice content met the Art. 12(1) form
    qualifiers and that any oral-information provision was preceded by adequate
    identity confirmation.
  ambiguity_notes: |
    The six conjunctive qualifiers on information form — concise, transparent, intelligible, easily accessible, clear, plain — are all open-textured and the article does not quantify any of them. Reading chosen: layered notices meeting accessibility standards (WCAG 2.1 AA or equivalent), in line with EDPB Guidelines on transparency. No explicit Berry severity tag in the source analysis; treated here as light (S1/none) because the operational practice has converged on layered-notice templates and the residual ambiguity is presentation-tier rather than substantive.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

