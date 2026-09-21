---
document_id: AEGIS-PREPROC-GDPR-ART-15
title: GDPR Art. 15 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 15
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 15

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-020 | Where processing is based on consent (Art. 6(1)(a)) or on a contract (Art. 6(1)(b)) and carried out by automated means, the data subject receives the personal data concerning him or her in a structured, commonly used, machine-readable format and can transmit those data to another controller. | `GDPR-RT10` (Art. 15(3) — copy); `GDPR-CP09` (Art. 28(3)(g) — return/deletion); informed by Art. 20 (cross-chapter inheritance) | D-05.4 |
| SO-GDPR-020 | D-05.4 | Art. 20, Art. 15(3) | Portable data in commonly used machine-readable form |
| SO-GDPR-038 | The controller provides transparent, concise, intelligible, easily accessible information in clear and plain language to data subjects on processing operations (Art. 13/14 collection notices), supports the exercise of data-subject rights (Art. 15–22), verifies identity on reasonable doubt, responds to rights requests within one month (extendable by two further months where necessary), and acts free of charge except in defined exception cases. | `GDPR-RT01` (Art. 12(1)); `GDPR-RT02` (Art. 12(3)); `GDPR-RT03` (Art. 12(5)); `GDPR-RT04` (Art. 12(6)); `GDPR-RT05` (Art. 13(1)); `GDPR-RT06` (Art. 13(2)(f)); `GDPR-RT07` (Art. 14(1)/(2)); `GDPR-RT08` (Art. 14(5)(b)) | D-09.4, D-05.4 |

## Security Rules (from 02_SecurityRules_NIST.md)

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
- sr_id: SR-GDPR-061
  title: "Essence disclosure of joint-controller arrangement"
  source_clauses:
    - { clause_id: GDPR-CP05, article_ref: "Art. 26(2) — arrangement essentials" }
    - { clause_id: GDPR-CP04, article_ref: "Art. 26(1) (cross)" }
  linked_objectives: [SO-GDPR-036]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy established, communicated, enforced" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance evaluated and reviewed" }
  applies_to_role: [CONTROLLER_JOINT]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 26(2) requires that the joint-controller arrangement referred to in Art. 26(1) shall duly reflect the respective roles and relationships of the joint controllers vis-à-vis the data subjects, and the essence of the arrangement shall be made available to the data subject. Art. 26(3) preserves the data subject's right to exercise the rights under the Regulation in respect of and against each of the controllers, irrespective of the terms of the arrangement. The data subject therefore retains the full set of Art. 15–22 rights against every joint controller even where the arrangement allocates operational handling to a single point of contact.
  security_rationale: |
    The obligation in Art. 26(2) and Art. 26(3) is operationalised in NIST CSF 2.0
    through **GV.PO-01 (Organizational cybersecurity policy established,
    communicated, and enforced)** and **GV.OV-03 (Organizational cybersecurity
    performance evaluated and reviewed for needed adjustments)**.

    GV.PO-01 controls the communication of the joint-controller arrangement's
    essence to data subjects: the substantive role allocation must be made
    available in a form intelligible to the data subject, whether published on a
    website, embedded in the privacy notice, or provided on request. GV.PO-01
    applies here to the joint-controller policy that translates the Art. 26(1)
    arrangement into a communicated, enforced organisational instrument. GV.OV-03
    controls the periodic reassessment of whether the disclosed essence remains
    accurate against actual practice, because Art. 26(2) requires the arrangement
    to duly reflect the respective roles and relationships of the joint
    controllers vis-à-vis data subjects as those relationships evolve.

    Together the two subcategories embed the essence-of-arrangement disclosure in
    an established organisational policy (GV.PO-01) backed by a performance-
    review cycle (GV.OV-03), enabling ex-post demonstration to the supervisory
    authority that the disclosed essence was kept current with actual processing
    operations and that data subjects retained the full Art. 15–22 rights against
    every joint controller under Art. 26(3).
  ambiguity_notes: |
    Duly in Art. 26(2) and essence of the arrangement carry VAG-S2; the two readings converge on the practical obligation that the substantive role allocation must be made available in a form intelligible to the data subject, without requiring the full contractual text of the arrangement. The choice between publishing the arrangement on a website, embedding it in the privacy notice, or providing it on request is operational and does not change the compliance posture. Remain open: whether the essence disclosure can be deferred to the data subject's request or must be proactive (placed in the privacy notice from the outset).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

