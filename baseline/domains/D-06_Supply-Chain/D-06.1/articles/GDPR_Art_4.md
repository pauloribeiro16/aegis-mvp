---
document_id: AEGIS-PREPROC-GDPR-ART-4
title: GDPR Art. 4 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 4
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
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# GDPR Art. 4

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-002 (cross-ref) | When pseudonymisation or encryption is applied, the additional information required to re-identify the data subject is kept separately and is subject to technical and organisational measures that prevent attribution. | `GDPR-C02` (Art. 4(5) — pseudonymisation definition); `GDPR-CP20` (Art. 34(3)(a)) | D-01.3 |
| SO-GDPR-002 | D-01.3, D-01.1 | Art. 4(5), Art. 32(1)(a), Art. 34(3)(a) | Pseudonymisation/encrypted data unintelligible post-breach |
| SO-GDPR-008 | Personal data breaches are detected and triaged; the moment of "becoming aware" is documented to anchor the 72-hour notification clock. | `GDPR-CP17` (Art. 33(1)); `GDPR-C06` (Art. 4(12) — breach definition) | D-04.1 |
| SO-GDPR-008 | D-04.1, D-10.1 | Art. 4(12), Art. 33(1) | Breach detection and "becoming aware" anchoring |
| SO-GDPR-010 | Personal data breaches are notified to the supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware, unless the breach is unlikely to result in a risk to data subjects' rights and freedoms. | `GDPR-CP17` (Art. 33(1)); `GDPR-C06` (Art. 4(12)) | D-04.3 |
| SO-GDPR-010 | D-04.3 | Art. 33(1), Art. 4(12) | 72h notification to supervisory authority |
| SO-GDPR-018 | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds applies; erasure is operationally defined as making the data inaccessible to the controller for normal processing paths. | `GDPR-C06` (Art. 4(12) breach-related — operational deletion overlap); `GDPR-CL03` (Art. 5(1)(c) — data-minimisation, downstream of erasure); `GDPR-CL05` (Art. 5(1)(e) — storage limitation), `GDPR-CP10` (Art. 28(3)(g) — deletion polysemy) | D-05.3 |
| SO-GDPR-021 | The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights. | `GDPR-CP07` (Art. 28(1)); `GDPR-CP08` (Art. 28(2)); `GDPR-C03` (Art. 4(7)/(8) — controller/processor) | D-06.1 |
| SO-GDPR-021 | D-06.1 | Art. 28(1)/(2), Art. 4(7)/(8) | Sufficient guarantees from processors |
| SO-GDPR-033 | Cross-border transfer of personal data takes place only where the conditions laid down in Chapter V are complied with (Art. 44); where no Commission adequacy decision exists (Art. 45), appropriate safeguards (Art. 46) are in place; absent both, derogations under Art. 49 are used only as narrowly-defined conditions, with the catch-all applying only when transfers are not repetitive, concern a limited number of data subjects, are necessary for compelling legitimate interests, and are accompanied by suitable safeguards. | `GDPR-TR01` (Art. 44); `GDPR-TR02` (Art. 45(1)); `GDPR-TR03` (Art. 45(3) — periodic review); `GDPR-TR04` (Art. 46(1)); `GDPR-TR05` (Art. 46(2)); `GDPR-TR08`–`GDPR-TR10` (Art. 49(1)(a)/(d) and catch-all); `GDPR-C07` (Art. 4(16) — main establishment) | D-06.3, D-09.1, D-05.1 |
| SO-GDPR-033 | D-06.3, D-09.1, D-05.1 | Art. 44, Art. 45, Art. 46, Art. 49, Art. 4(16) | Cross-border transfers maintain GDPR protection level |
| SO-GDPR-036 | Where two or more controllers jointly determine purposes and means of processing, they determine their respective responsibilities for GDPR compliance in a transparent manner by means of an arrangement reflecting the roles of the joint controllers, made available to data subjects; data subjects may exercise their rights against each controller irrespective of the arrangement. | `GDPR-CP04` (Art. 26(1)); `GDPR-CP05` (Art. 26(2)); `GDPR-C03` (Art. 4(7) — controller/joint controllers) | D-09.2, D-06.3 |
| SO-GDPR-036 | D-09.2, D-06.3 | Art. 26(1)/(2), Art. 4(7) | Joint-controller arrangement transparency |
| SO-GDPR-032 | Consent to personal-data processing is freely given, specific, informed, and unambiguous; the controller demonstrates the data subject's consent on request; withdrawal of consent is as easy as giving; bundled consent requests are presented in a clearly distinguishable form; conditional consent (bundled with contract) is presumed non-compliant unless processing is strictly necessary for contract performance; special-category consent is at the higher `explicit` standard; child consent (information-society services) is gated by Art. 8 age thresholds and parental-responsibility verification; transfer consent (Art. 49(1)(a)) is `explicit` and risk-informed. | `GDPR-C05` (Art. 4(11) — consent definition); `GDPR-CL08` (Art. 6(1)(a)); `GDPR-CL15` (Art. 7(1)); `GDPR-CL16` (Art. 7(2)); `GDPR-CL17` (Art. 7(3)); `GDPR-CL18` (Art. 7(4)); `GDPR-CL19` (Art. 8(1) — age threshold); `GDPR-CL20` (Art. 8(2) — reasonable verification); `GDPR-CL22` (Art. 9(2)(a) — explicit consent for special categories); `GDPR-TR08` (Art. 49(1)(a) — explicit transfer consent) | D-09.1, D-03.1 |
| SO-GDPR-032 | D-09.1, D-03.1 | Art. 4(11), Art. 6(1)(a), Art. 7, Art. 8, Art. 9(2)(a), Art. 49(1)(a) | Consent lifecyle: specific, informed, demonstrable, withdrawable |
| SO-GDPR-034 | Binding corporate rules for intra-group transfers (Art. 47) are approved by the competent supervisory authority via the consistency mechanism, confer enforceable rights on data subjects, and contain the 14 Art. 47(2) content items — including acceptance of liability by the EU controller/processor for breaches by non-EU members (subject to the `proves not responsible` rebuttal standard). | `GDPR-C08` (Art. 4(20) — BCR definition); `GDPR-TR06` (Art. 47(2)(f) and full 14-item list) | D-09.1, D-06.3 |
| SO-GDPR-034 | D-09.1, D-06.3 | Art. 4(20), Art. 47(1)/(2) | Binding corporate rules with Art. 47(2) content |

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
- sr_id: SR-GDPR-051
  title: "Demonstrable consent with equally accessible withdrawal path"
  source_clauses:
    - { clause_id: GDPR-C05, article_ref: "Art. 4(11) — consent definition" }
    - { clause_id: GDPR-CL08, article_ref: "Art. 6(1)(a) — consent as lawfulness base" }
    - { clause_id: GDPR-CL15, article_ref: "Art. 7(1) — demonstrability" }
    - { clause_id: GDPR-CL17, article_ref: "Art. 7(3) — withdrawal" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CONSENT-COLLECTION, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(11) defines consent as any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. Art. 6(1)(a) anchors that consent as one of six alternative lawfulness bases, meaning that any single processing operation relying on consent must satisfy the Art. 4(11) elements in full. Art. 7(1) shifts the evidentiary burden onto the controller, which must be able to demonstrate that the data subject has consented. Art. 7(3) then grants the data subject the right to withdraw consent at any time, requires withdrawal to be as easy as giving consent, requires the data subject to be informed of that right before giving consent, and obliges the controller to cease processing based on consent upon withdrawal without affecting the lawfulness of processing carried out before withdrawal (Recital 65).
  security_rationale: |
    The obligation in Art. 4(11), Art. 6(1)(a), Art. 7(1) and Art. 7(3) is
    operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and
    bound to credentials based on the context of interactions)** and **GV.OC-03
    (Legal, regulatory, and contractual requirements regarding cybersecurity —
    including privacy and civil liberties obligations — are understood and
    managed)**.

    PR.AA-02 controls the binding of the data subject's identity to the consent
    artefact: because the consent act functions as an authentication of intent,
    the controller must proof the identity of the consenting party and bind that
    proof to a credential-like consent record that is reproducible on demand.
    GV.OC-03 captures the broader legal-basis frame: the controller's
    organisation must understand and manage the conditions under which consent
    remains valid, the demonstrability threshold imposed by Art. 7(1), and the
    operational withdrawal mechanism that Art. 7(3) requires to be as accessible
    as the original consent collection.

    Together the two subcategories give the controller an auditable consent
    ledger (identity-bound artefacts under PR.AA-02) embedded in a managed
    regulatory-compliance process (under GV.OC-03), enabling ex-post
    demonstration to the supervisory authority that each Art. 4(11) qualifier was
    satisfied and that withdrawal was honoured without retroactive lawfulness
    collapse.
  ambiguity_notes: |
    The four Art. 4(11) qualifiers — freely given, specific, informed, unambiguous — are each open-textured and together carry the highest coordination risk because they are conjunctive, so failure of any one defeats the consent. Reading chosen: the four qualifiers must all be present simultaneously, as anchored by EDPB Guidelines 05/2020 §3.1 (consent must be a freely given, specific, informed and unambiguous indication, with each element assessed independently). An alternative reading limits the assessment to the absence of clear duress or deception, treating specific and unambiguous as formal rather than substantive qualifiers; this narrower reading is plausible for low-risk processing but is inconsistent with EDPB §3.1 and with CJEU Planet49 (C-673/17 §73), which held that pre-ticked boxes do not constitute unambiguous consent. A second alternative would treat specific as a granularity requirement separate from informed, requiring a separate consent per processing purpose even where the data subject is fully informed of all purposes, which is consistent with EDPB §3.4 but operationally costly and not always demanded by supervisory authorities in practice. Remain open: (a) whether the four qualifiers admit a sliding-scale intensity test proportionate to the sensitivity of the data and the purpose, or whether each must always be satisfied at uniform intensity; (b) whether Art. 7(3) as easy as giving consent applies only to the withdrawal mechanism proper, or extends to the procedural difficulty of locating that mechanism within the wider user interface.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-052
  title: "Unbundled and non-conditional consent collection"
  source_clauses:
    - { clause_id: GDPR-CL16, article_ref: "Art. 7(2) — bundled consent" }
    - { clause_id: GDPR-CL18, article_ref: "Art. 7(4) — conditional consent" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CONSENT-COLLECTION]
  regulatory_rationale: |
    Art. 7(2) requires that, if the data subject's consent is given in the context of a written declaration which also concerns other matters, the request for consent shall be presented in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language. Recital 32 reinforces this by requiring the request to be unambiguous. Art. 7(4) then states that when assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is not necessary for the performance of that contract (Recital 43). The two articles together form the unbundling rule: separate consent UI for separate processing purposes, and no conditioning of contract performance on consent for unrelated processing. Recital 43 anchors the practical effect by clarifying that consent should not provide a blanket gateway to all processing the controller may wish to perform.
  security_rationale: |
    The obligation in Art. 7(2) and Art. 7(4) is operationalised in NIST CSF 2.0
    through **GV.PO-02 (Cybersecurity processes and procedures established,
    communicated, and enforced)** and **PR.AA-02 (Identities proofed and bound to
    credentials based on the context of interactions)**.

    GV.PO-02 controls the documented consent-flow process: the controller must
    establish and enforce a written consent-collection procedure that physically
    or logically separates each purpose's consent UI, uses plain-language
    labelling, and prohibits the conditioning of contract performance on consent
    for processing that is not strictly necessary to the contract. The CJEU
    Bundeskartellamt line (C-252/21) and Planet49 (C-673/17) confirm that this
    process discipline is the principal defence against consent-coercion
    patterns. PR.AA-02 captures each consent act as an authentication of intent,
    with the consent artefact treated like a credential whose issuance is
    purpose-scoped and whose withdrawal path mirrors the issuance path in
    accessibility.

    Together the two subcategories translate the Art. 7 unbundling rule into a
    documented, enforced process (GV.PO-02) backed by identity-bound consent
    records (PR.AA-02), enabling the controller to demonstrate ex-post at
    supervisory-authority review that no consent was coerced, bundled, or
    improperly conditioned.
  ambiguity_notes: |
    Clearly distinguishable, intelligible and easily accessible, and clear and plain language carry VAG-S3 because none of them specifies an objective threshold that an auditor or supervisory authority could apply uniformly. Reading chosen: a visible, separate consent UI per purpose, with no pre-ticked boxes and layered notices following EDPB Guidelines 05/2020 §3.6, which treats physical separation of consent from other matters as a condition for the consent to be clearly distinguishable. The Art. 7(4) reading chosen: bundling per se is non-compliant unless the unrelated processing is strictly necessary for the contract, per the CJEU Bundeskartellamt ruling (C-252/21), which treated Facebook's combined-terms consent as coercive. An alternative reading would permit softer bundling where the data subject can in practice decline without losing access to the core service, on the rationale that effective choice rather than physical separation is the substance of the requirement; this conditional-permissibility reading is inconsistent with the Bundeskartellamt precedent but has been raised in national-court proceedings and remains litigated. A second alternative would treat the requirement as satisfied by any technically distinguishable mechanism, including a default-accept button paired with an opt-out link, which is rejected by supervisory practice because default-accept configurations cannot satisfy the freely-given qualifier of Art. 4(11). Remain open: (a) whether Art. 7(2) requires physical separation (separate button or checkbox on the same screen) or merely logical separation (same screen, clearly labelled section) when consent is collected in a multi-purpose form; (b) whether a single consent artefact that bundles consent for a core service with consent for an ancillary feature (analytics, personalisation) is per se non-compliant under Art. 7(4) when the ancillary feature is genuinely optional and not technically integrated with the core.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-053
  title: "Explicit elevated consent for special-category processing"
  source_clauses:
    - { clause_id: GDPR-CL22, article_ref: "Art. 9(2)(a) — explicit consent for special categories" }
    - { clause_id: GDPR-CL21, article_ref: "Art. 9(1) — special-category prohibition (cross)" }
    - { clause_id: GDPR-C05, article_ref: "Art. 4(11) — consent definition (cross)" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: UNMAPPED_CSF, title: "Special-category consent is a GDPR-specific construct; nearest reference is NIST Privacy Framework Category-P" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CATEGORY-CONSENT]
  regulatory_rationale: |
    Art. 9(1) prohibits the processing of special categories of personal data unless one of the Art. 9(2) grounds applies. Art. 9(2)(a) lifts the prohibition where the data subject has given explicit consent to the processing of those personal data for one or more specified purposes, unless Union or Member State law provides that the Art. 9(1) prohibition may not be lifted by the data subject. The explicit qualifier is stronger than the Art. 4(11) specific qualifier and operates on top of the Art. 4(11) four-element test rather than replacing it (Recital 32; EDPB Guidelines 05/2020 §3.4 on the explicit-versus-specific escalation). Art. 9 also prohibits processing of data relating to criminal convictions and offences except under Member State law with specific safeguards (Art. 10), and the explicit-consent route under Art. 9(2)(a) is generally not available for criminal-conviction data, which must rely on Art. 10 Member State law instead. The result is a two-track special-category regime: explicit consent for sensitive personal data under Art. 9(2)(a), and statutory authorisation for criminal-conviction data under Art. 10, with no overlap.
  security_rationale: |
    The obligation in Art. 9(2)(a) has no direct NIST CSF 2.0 subcategory and is
    anchored on the closest fit **PR.AA-02 (Identities proofed and bound to
    credentials based on the context of interactions)** within the broader
    **PR.AA — Identity, Authentication, and Access Control** category; the
    residual gap is noted as UNMAPPED_CSF.

    PR.AA-02 controls risk-stratified identity proofing: higher-assurance
    contexts warrant stronger proofing, in the same way that high-value
    transactions warrant multi-factor authentication rather than password-only
    proofing. Special-category consent is the GDPR's strongest data-subject-
    intent authentication, and PR.AA-02's context-sensitive proofing model
    captures the engineering pattern even though no CSF subcategory enumerates
    the Art. 4(11)-vs-Art. 9(2)(a) escalation ladder. The natural broader
    reference for consent-as-control is the NIST Privacy Framework
    (Category-P), which is outside this pre-processing pass.

    Because the CSF gap is documented, the controller must supplement PR.AA-02
    with a GDPR-specific consent-artefact design: a separate, uncombined,
    express-statement consent record for each special-category purpose, retained
    for supervisory-authority inspection. Accountability is sustained through the
    documented gap (UNMAPPED_CSF + unmapped_csf_justification) plus the PR.AA-02
    identity-binding trail that proves each special-category consent was
    collected above the Art. 4(11) baseline.
  ambiguity_notes: |
    Explicit versus specific carries POLY-S3 because the OJ text of Art. 9(2)(a) does not define explicit and Art. 4(11) does not define specific, leaving the boundary unclear. Reading chosen: explicit requires a separate, unambiguous statement on the special-category processing, not bundled with any other consent and not satisfied by inference or pre-ticked boxes, per EDPB Guidelines 05/2020 §3.4 (which interprets explicit as an additional layer on top of the Art. 4(11) specific requirement, requiring that the data subject gives the consent by means of an express statement). An alternative reading treats explicit as a synonym for specific, in which case any Art. 4(11)-compliant consent would suffice for special-category processing; this reading is rejected because it would render Art. 9(2)(a) redundant and is inconsistent with EDPB §3.4. A second alternative reading limits the Art. 9(2)(a) consent to a written-and-signed declaration, excluding electronic confirmations; this reading is rejected because Art. 9(2)(a) does not impose a form requirement and EDPB §3.4 treats electronic confirmation as equally valid provided the explicit-statement condition is met. Remain open: (a) whether a written declaration signed in advance and explicitly invoking special-category processing satisfies Art. 9(2)(a) without a fresh per-purpose confirmation; (b) whether Member State law that purports to make the Art. 9(1) prohibition non-liftable by consent (per the Art. 9(2)(a) proviso) applies symmetrically across Member States or only within the Member State that enacted it.
  unmapped_csf_justification: |
    Special-category consent is a GDPR-specific construct (Art. 9
    vs Art. 4(11)) with no direct CSF 2.0 Subcategory. Closest
    CSF match is PR.AA-02; NIST Privacy Framework is the natural
    broader reference. Marked UNMAPPED_CSF.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-054
  title: "Verified consent for child and transfer-risk contexts"
  source_clauses:
    - { clause_id: GDPR-CL19, article_ref: "Art. 8(1) — age threshold" }
    - { clause_id: GDPR-CL20, article_ref: "Art. 8(2) — reasonable verification efforts" }
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit transfer consent" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-OFFERING, PER-TRANSFER]
  regulatory_rationale: |
    Art. 8(1) sets a default age of 16 for consent in information-society services offered directly to a child, with Member States permitted to lower the threshold by law provided it is not below 13 (Recital 38); the threshold governs only consent and not the other Art. 6 lawfulness bases. Art. 8(2) requires the controller to make reasonable efforts to verify that parental responsibility is held in respect of any child below the threshold, taking into consideration available technology, which is a process obligation rather than an outcome guarantee. Art. 49(1)(a) requires, as a derogation for international transfers in the absence of adequacy and appropriate safeguards, that the data subject has explicitly consented to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and of appropriate safeguards (Recital 49). The three articles together form a single rule on consent validity for vulnerable contexts: child consent requires parental verification (Art. 8) and transfer consent requires informed risk acknowledgement (Art. 49(1)(a)), both layered on top of the Art. 4(11) baseline.
  security_rationale: |
    The obligation in Art. 8(1)–(2) and Art. 49(1)(a) is operationalised in NIST
    CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials based
    on the context of interactions)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    PR.AA-02 controls the identity-proofing step that Art. 8(2) requires: the
    controller must make reasonable efforts to verify that the consenting party
    holds parental responsibility for a child below the age threshold, and the
    available-technology standard operates as a rolling baseline that the
    proofing mechanism must track. The same subcategory controls the stronger
    transfer-risk-informed consent that Art. 49(1)(a) requires, layered on top of
    the Art. 4(11) baseline with explicit risk acknowledgement. GV.OC-03 captures
    the wider regulatory frame across Member-State age-threshold variations
    (which span 13 to 16) and across the transfer-restriction regime under which
    Art. 49(1)(a) sits as a narrow derogation rather than a general mechanism.

    Together the two subcategories embed age and transfer-risk verification in a
    documented identity-proofing process (PR.AA-02) within a managed
    regulatory-compliance frame (GV.OC-03), enabling the controller to
    demonstrate ex-post that the Art. 8 verification effort was reasonable in its
    technological context and that Art. 49(1)(a) consent was collected with
    informed risk acknowledgement.
  ambiguity_notes: |
    Art. 8(1) parental-responsibility carries POLY-S3 because Member State legal definitions diverge (some treat only biological parents as holders of parental responsibility, others include guardians and educational institutions). Art. 8(2) reasonable efforts carries VAG-S3 because the available-technology standard is a rolling benchmark and no supervisory authority has published a hard test. Art. 49(1)(a) explicitly consented carries POLY-S3 against the Art. 4(11) unambiguous standard and the Art. 9(2)(a) explicit standard. The rule preserves the EDPB Guidelines 05/2020 reading that the derogation consent must be explicit, specific to the transfer, and documented as risk-informed, so the controller cannot rely on the same consent artefact used for the underlying Art. 6(1)(a) basis. An alternative reading confines Art. 8(2) reasonable efforts to a one-time check at the moment of consent collection; this reading is rejected because EDPB Guidelines on Art. 8(2) treat the obligation as continuing for as long as the child uses the service. A second alternative reading treats the Art. 49(1)(a) explicit consent as a one-time event that survives subsequent changes in the destination regime; this reading is rejected because the risk-informed nature of the consent requires re-confirmation when the destination regime materially changes. Remain open: (a) whether reasonable efforts under Art. 8(2) includes reliance on the data subject's self-declaration of age or whether a positive verification step (credit-card verification, ID upload, knowledge-based authentication) is required; (b) whether Art. 49(1)(a) explicit consent can be combined with Art. 6(1)(a) consent in a single transaction or must be collected through a separate user journey that highlights the transfer-risk information.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-055
  title: "Adequacy-governed cross-border transfer inventory and review"
  source_clauses:
    - { clause_id: GDPR-TR01, article_ref: "Art. 44 — general transfer principle" }
    - { clause_id: GDPR-TR02, article_ref: "Art. 45(1) — adequacy-based transfer" }
    - { clause_id: GDPR-TR03, article_ref: "Art. 45(3) — periodic review of adequacy" }
    - { clause_id: GDPR-C07, article_ref: "Art. 4(16) — main establishment (cross)" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER]
  regulatory_rationale: |
    Art. 44 establishes the umbrella principle for cross-border transfers: any transfer of personal data to a third country or international organisation shall take place only if the Chapter V conditions are complied with by the controller and processor, including for onward transfers, and the level of protection of natural persons guaranteed by GDPR is not undermined (Recital 6). Art. 45(1) exempts transfers covered by a Commission adequacy decision from any specific authorisation requirement, on the basis that the third country, territory, sector or international organisation ensures an adequate level of protection. Art. 45(3) requires the Commission to specify, in its implementing decision, the mechanism for a periodic review of that adequacy assessment, at least every four years, and to amend, suspend or repeal the decision where the available information reveals that the third country or international organisation no longer ensures an adequate level of protection. Art. 4(16) anchors the main-establishment concept used in Art. 44 for determining which supervisory authority has jurisdiction over the cross-border processing.
  security_rationale: |
    The obligation in Art. 44, Art. 45(1) and Art. 45(3) is operationalised in
    NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties known,
    prioritized, and assessed using a cybersecurity supply chain risk management
    process)**, **GV.SC-03 (Contracts with suppliers and other third parties used
    to implement appropriate measures)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    GV.SC-02 controls the inventory and prioritisation of cross-border data
    flows: the controller must maintain a transfer register that maps every
    outbound flow to its destination, its legal mechanism, and its assessed risk
    under the Schrems II substantial-equivalence test. GV.SC-03 controls the
    contractual articulation of each transfer's safeguards, including
    onward-transfer clauses that bind downstream recipients to equivalent
    protection. GV.OC-03 controls the legal-basis frame, including the temporal
    stability of adequacy decisions and the trigger for re-assessment whenever
    the Commission adopts, suspends or repeals an Art. 45(3) decision.

    Together the three subcategories give the controller a SCRM-style governance
    of cross-border data flows embedded in a managed regulatory frame, enabling
    ex-post demonstration to the supervisory authority that every transfer is
    inventoried, contractually anchored, and reassessed against the latest
    adequacy posture.
  ambiguity_notes: |
    The not undermined qualifier of Art. 44 carries VAG-S3 because the OJ text does not fix a metric for the level of protection and supervisory authorities have not published a quantitative threshold. Reading chosen: the substantial-equivalence reading from CJEU Schrems II (C-311/18 §96), under which the essential content of EU protection must be preserved in the third country, with the EDPB Recommendations 01/2020 supplementary-measures framework operating as the operational remediation path when the destination regime falls short. An alternative reading would treat not undermined as a procedural rather than substantive requirement, satisfied by the existence of any lawful basis for the transfer; this reading is rejected because Schrems II §96 held that procedural legality does not compensate for substantive deficiencies in the destination regime, and the EDPB Recommendations 01/2020 §B.1 make the essential-equivalence test binding for transfers to third countries whose domestic law permits extensive public-authority access. A second alternative reading focuses on the foreseeability of the third-country practice at the time of transfer rather than on the essential equivalence at the time of assessment; this reading is consistent with Schrems II §94 but operationally difficult because it requires the controller to predict regulatory drift in the destination jurisdiction. Remain open: (a) whether the Schrems II essential-equivalence test applies equally to processors and to controllers or whether a processor-tier standard may be lower given that the processor is itself bound by Art. 28; (b) whether supplementary measures (encryption, pseudonymisation, contractual minimisation) can rescue transfers to regimes where the public-authority access regime is materially deficient, or whether the Schrems II ruling forecloses supplementary measures in such cases.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-057
  title: "Derogation-based transfer fallback under strict preconditions"
  source_clauses:
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit consent" }
    - { clause_id: GDPR-TR09, article_ref: "Art. 49(1)(d) — important public interest" }
    - { clause_id: GDPR-TR10, article_ref: "Art. 49(1) second subparagraph — catch-all" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: UNMAPPED_CSF, title: "Derogation under Art. 49 is GDPR-specific with no clean CSF 2.0 mapping" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER, ONE_TIME]
  regulatory_rationale: |
    Art. 49 derogations apply only in the absence of an adequacy decision under Art. 45(3) and of appropriate safeguards under Art. 46, including binding corporate rules. Art. 49(1) lists seven disjunctive grounds: explicit consent after being informed of possible risks; necessity for the performance of a contract between the data subject and the controller or implementation of pre-contractual measures at the data subject's request; necessity for a contract concluded in the interest of the data subject between the controller and another natural or legal person; important reasons of public interest; establishment, exercise or defence of legal claims; protection of the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent; transfer from a register intended to provide information to the public (Recital 111–115). The second subparagraph of Art. 49(1) adds a catch-all: transfers may take place where the transfer is not repetitive, concerns a limited number of data subjects, is necessary for compelling legitimate interests of the controller which are not overridden by the interests, rights or freedoms of the data subject, and the controller has assessed all the circumstances and put in place suitable safeguards (Recital 113).
  security_rationale: |
    The obligation in Art. 49(1)(a), Art. 49(1)(d) and Art. 49(1) second
    subparagraph has no clean NIST CSF 2.0 subcategory and is anchored on the
    closest fit **GV.OC-03 (Legal, regulatory, and contractual requirements
    regarding cybersecurity — including privacy and civil liberties obligations —
    are understood and managed)** within the broader **GV.OC — Organizational
    Context** category; the residual gap is noted as UNMAPPED_CSF.

    GV.OC-03 controls the controller's understanding of the regulatory
    preconditions on which any Art. 49 derogation depends — absence of an
    adequacy decision under Art. 45(3), absence of Art. 46 appropriate
    safeguards, and satisfaction of one of the seven enumerated grounds or the
    catch-all (not repetitive, limited number of data subjects, compelling
    legitimate interests, suitable safeguards). CSF 2.0 does not enumerate
    derogation-availability analysis and GV.OC-03 is a poor fit because it is
    designed for ongoing regulatory understanding rather than exception-
    availability gating, but it is the closest available anchor.

    Because the CSF gap is documented, the controller must supplement GV.OC-03
    with a GDPR-specific derogation-use register that records each catch-all
    reliance, the compelling-interests analysis, and the suitable safeguards
    deployed. Accountability is sustained through the documented gap
    (UNMAPPED_CSF + unmapped_csf_justification) and through GV.OC-03's
    regulatory-understanding trail that demonstrates the derogation fallback was
    used only where adequacy and Art. 46 safeguards were unavailable.
  ambiguity_notes: |
    Explicitly (Art. 49(1)(a)) carries POLY-S3 against the specific qualifier of Art. 4(11) and the explicit qualifier of Art. 9(2)(a); reading chosen: the strongest consent form, risk-informed and documented, building on EDPB Guidelines 05/2020 §3.4 and the Schrems II framing of risk disclosure. The catch-all qualifiers not repetitive, limited number, compelling legitimate interests, suitable safeguards carry VAG-S3 and SCOPE-Q-S3 because none of them is quantitatively bounded in the OJ text; compelling in particular carries POLY-S3 across Art. 21(1) and Art. 49(1) (Recital 47 cross-reference), and the EDPB Guidelines 2/2018 emphasise that compelling means more than legitimate and approaches necessity. An alternative reading confines the catch-all to transfers that are truly exceptional and treats recurring or systematic reliance on it as a structural misuse of the derogation; this reading is consistent with that framing and operationally shifts the burden onto the controller to demonstrate the exceptional nature of each catch-all reliance. A second alternative reading treats not repetitive as a per-data-subject test rather than per-data-flow; this reading is harder to operationalise and is inconsistent with the structural purpose of the catch-all. Remain open: (a) whether repetitive in the catch-all should be measured per data subject, per transfer, or per data flow, given that no OJ anchor specifies the unit; (b) whether suitable safeguards in the catch-all may be purely contractual or must include technical measures (encryption, pseudonymisation) per Schrems II §134.
  unmapped_csf_justification: |
    The four Art. 49 catch-all conjunctive qualifiers and the
    `compelling legitimate interests` qualifier have no clean CSF 2.0
    Subcategory. The closest mapping GV.OC-03 is a poor fit.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-058
  title: "Binding corporate rules for intragroup transfers"
  source_clauses:
    - { clause_id: GDPR-C08, article_ref: "Art. 4(20) — BCR definition" }
    - { clause_id: GDPR-TR06, article_ref: "Art. 47(2)(a)–(n) — 14 content items" }
  linked_objectives: [SO-GDPR-034]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "Cybersecurity supply chain risk management program/strategy established" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-BCR, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(20) defines binding corporate rules (BCRs) as personal data protection policies which are adhered to by a controller or processor established on the territory of a Member State for transfers or a set of transfers of personal data to a controller or processor in one or more third countries within a group of undertakings, or group of enterprises engaged in a joint economic activity. Art. 47(1) requires the competent supervisory authority to approve BCRs in accordance with the consistency mechanism, provided they are legally binding and applied by every member concerned of the group, expressly confer enforceable rights on data subjects, and fulfil the requirements laid down in Art. 47(2). Art. 47(2) enumerates 14 mandatory content items: structure and contact details of the group; data transfers and processing categories; legally binding nature; application of general data protection principles; data subject rights; controller or processor responsibilities; data protection officer; complaint mechanisms; cooperation with supervisory authorities; training; audit procedures; reporting and recording of changes; cooperation procedure with the supervisory authority. The list is closed and all 14 items must be present (Recital 108).
  security_rationale: |
    The obligation in Art. 4(20) and Art. 47(2)(a)–(n) is operationalised in NIST
    CSF 2.0 through **GV.SC-01 (Cybersecurity supply chain risk management
    program, strategy, objectives, policies, and processes established and agreed
    to by organizational stakeholders)** and **GV.SC-03 (Contracts with suppliers
    and other third parties used to implement appropriate measures)**.

    GV.SC-01 controls the group-level SCRM programme within which binding
    corporate rules sit: the BCR is the group-wide data-policy instrument that
    every member of the undertaking adheres to, supervised by the competent
    authority under the Art. 47(1) consistency mechanism. GV.SC-03 controls the
    binding contractual nature of the BCR itself, with the 14 mandatory Art.
    47(2) content items — group structure, transfer categories, legal binding
    force, principle application, data-subject rights, controller responsibility,
    DPO, complaint mechanism, supervisory cooperation, training, audit, change
    reporting — articulated as SCRM contractual clauses.

    Together the two subcategories embed the BCR within an established
    group-level programme (GV.SC-01) backed by an enforceable intra-group
    contract (GV.SC-03), enabling ex-post demonstration to the supervisory
    authority that all 14 Art. 47(2) items are present, that every group member
    is bound, and that data-subject rights are enforceable against any member of
    the undertaking.
  ambiguity_notes: |
    The 14-element AND-list is COORD-S2: all 14 items are mandatory, the list is closed, and a BCR that omits any item cannot be approved by the competent supervisory authority. Art. 47(2)(f) on demonstrating not being responsible for the event giving rise to the damage carries VAG-S3 because the OJ text does not fix the standard of proof; reading chosen: the controller demonstrates on a balance of probabilities that the damage did not arise from its act or omission, which is the civil-law burden-of-proof convention and is consistent with EDPB BCR guidance on the operation of the joint-controller regime within the group. An alternative reading would treat the 14-element list as enumerative rather than closed, allowing the controller to substitute equivalent provisions for selected items; this reading is rejected because Art. 47(2) presents the list as a closed set and the supervisory-authority approval under Art. 47(1) requires full coverage. A second alternative reading would treat Art. 47(2)(f) on the balance-of-proof question as applying the higher criminal-law standard; this reading is rejected because the article is silent on the standard and the EDPB BCR guidance treats it as a civil-law matter. Remain open: (a) whether the 14-element list permits Member State-specific additions for sectors with stricter national rules, or whether the closed-list reading precludes any national-layer expansion; (b) whether BCRs approved under the predecessor Directive 95/46/EC remain valid post-GDPR entry into force or must be re-approved under the Art. 63 consistency mechanism.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-060
  title: "Joint-controller role allocation through binding arrangement"
  source_clauses:
    - { clause_id: GDPR-CP04, article_ref: "Art. 26(1) — joint-controller determination" }
    - { clause_id: GDPR-C03, article_ref: "Art. 4(7) — controller definition" }
  linked_objectives: [SO-GDPR-036]
  sub_domain: [D-09.2, D-06.3]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles/responsibilities/accountabilities established and communicated" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER_JOINT]
  obligation_type: [PER-ARRANGEMENT, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(7) defines a controller as the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data. Art. 26(1) requires that where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers, and they shall in a transparent manner determine their respective responsibilities for compliance with the obligations under the Regulation, in particular as regards the exercising of the rights of the data subject and their respective duties to provide the information referred to in Arts. 13 and 14, by means of an arrangement between them unless, and in so far as, the respective responsibilities of the controllers are determined by Union or Member State law to which they are subject. The arrangement may designate a contact point for data subjects (Recital 79). The CJEU IAB Europe ruling (C-604/22) interpreted jointly determine to include parties with determinative influence on purposes or means even where they do not themselves process the data, extending joint-controller status to industry-association-managed consent frameworks.
  security_rationale: |
    The obligation in Art. 4(7) and Art. 26(1) is operationalised in NIST CSF 2.0
    through **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities
    related to cybersecurity risk management established, communicated,
    understood, and enforced)** and **GV.SC-03 (Contracts with suppliers and other
    third parties used to implement appropriate measures)**.

    GV.RR-02 controls the explicit allocation of joint-controller roles: absent
    an Art. 26 arrangement, the data subject faces a fragmented accountability
    surface and the controller's organisation cannot discharge its compliance
    duties through a single accountable unit. The CJEU IAB Europe ruling
    (C-604/22) extends joint-controller status to parties with determinative
    influence on the consent mechanism even where that party does not itself
    process the data, so GV.RR-02 requires that the arrangement identify all
    parties meeting the influence test, not only parties operating processing
    operations. GV.SC-03 controls the contractual articulation of the
    arrangement, including the allocation of data-subject-facing duties (Arts.
    13/14 information, Arts. 15–22 rights-handling) and the designation of a
    single contact point.

    Together the two subcategories translate the Art. 26 arrangement into an
    established role allocation (GV.RR-02) backed by a multi-party contractual
    instrument (GV.SC-03), enabling ex-post demonstration to the supervisory
    authority and to data subjects that responsibility for every processing
    operation is traceable to a named accountable controller.
  ambiguity_notes: |
    Jointly determine in Art. 4(7) and Art. 26(1) carries POLY-S3 because the OJ text does not fix the threshold at which influence on purposes or means becomes joint determination. Reading chosen: the CJEU IAB Europe ruling (C-604/22), under which a party with determinative influence on purposes and means qualifies as a joint controller even where that party does not itself process the data, on the basis that the TCF (Transparency and Consent Framework) gave IAB Europe decisive influence over the consent collection mechanism. An alternative reading confines joint controllership to parties that share actual decision-making on processing operations, excluding parties whose influence is limited to the consent-mechanism layer; this narrower reading is rejected post-IAB Europe. A second alternative reading treats joint controllership as requiring converging rather than identical purposes, so that parties with diverging but complementary purposes remain separate controllers; this reading is consistent with the Wirtschaftsakademie ruling (C-210/16) but creates a fact-intensive boundary that is hard to operationalise. Remain open: (a) whether a processor that designs processing operations on behalf of a controller can become a joint controller by virtue of the design influence, or whether the processor-controller distinction is preserved; (b) whether joint-controller status attaches per processing operation or per overall data flow, on the question of whether one joint controller for consent collection implies joint-controller status for downstream processing.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

