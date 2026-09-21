---
document_id: AEGIS-PREPROC-GDPR-ART-34
title: GDPR Art. 34 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 34
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---

# GDPR Art. 34

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-002 | Personal data protected by pseudonymisation or encryption remains unintelligible to any person who is not authorised to access it, including following a personal data breach. | `GDPR-CP20` (Art. 34(3)(a)); `GDPR-CP15` (Art. 32(1)(a)) | D-01.1, D-01.3 |
| SO-GDPR-002 (cross-ref) | When pseudonymisation or encryption is applied, the additional information required to re-identify the data subject is kept separately and is subject to technical and organisational measures that prevent attribution. | `GDPR-C02` (Art. 4(5) — pseudonymisation definition); `GDPR-CP20` (Art. 34(3)(a)) | D-01.3 |
| SO-GDPR-002 | D-01.3, D-01.1 | Art. 4(5), Art. 32(1)(a), Art. 34(3)(a) | Pseudonymisation/encrypted data unintelligible post-breach |
| SO-GDPR-009 | Personal data breaches are contained and mitigated through appropriate technical and organisational measures (including, where applicable, measures rendering the data unintelligible to unauthorised parties, and subsequent measures that ensure the high risk no longer materialises). | `GDPR-CP18` (Art. 33(3)(d)); `GDPR-CP20` (Art. 34(3)(a)/(b)) | D-04.2 |
| SO-GDPR-009 | D-04.2 | Art. 33(3)(d), Art. 34(3)(a)/(b) | Containment and mitigation of breaches |
| SO-GDPR-011 | Personal data breaches likely to result in a high risk to data subjects are communicated to the affected data subjects without undue delay, in clear and plain language, unless one of the three Art. 34(3) exceptions applies. | `GDPR-CP19` (Art. 34(1)/(2)/(3)); `GDPR-CP18` (Art. 33(3)(b)/(c)/(d)) | D-04.3 |
| SO-GDPR-011 | D-04.3 | Art. 34(1)/(2)/(3) | High-risk breach communication to data subjects |

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

