---
document_id: AEGIS-PREPROC-GDPR-ART-13
title: GDPR Art. 13 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 13
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# GDPR Art. 13

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-038 | The controller provides transparent, concise, intelligible, easily accessible information in clear and plain language to data subjects on processing operations (Art. 13/14 collection notices), supports the exercise of data-subject rights (Art. 15–22), verifies identity on reasonable doubt, responds to rights requests within one month (extendable by two further months where necessary), and acts free of charge except in defined exception cases. | `GDPR-RT01` (Art. 12(1)); `GDPR-RT02` (Art. 12(3)); `GDPR-RT03` (Art. 12(5)); `GDPR-RT04` (Art. 12(6)); `GDPR-RT05` (Art. 13(1)); `GDPR-RT06` (Art. 13(2)(f)); `GDPR-RT07` (Art. 14(1)/(2)); `GDPR-RT08` (Art. 14(5)(b)) | D-09.4, D-05.4 |
| SO-GDPR-038 | D-09.4, D-05.4 | Art. 12, Art. 13, Art. 14 | Information duties and rights-exercise support |

## Security Rules (from 02_SecurityRules_NIST.md)

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

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-067
  title: "Anti-abuse controls for manifestly unfounded rights requests"
  source_clauses:
    - { clause_id: GDPR-RT03, article_ref: "Art. 12(5) — manifestly unfounded or excessive" }
    - { clause_id: GDPR-RT04, article_ref: "Art. 12(6) — identity verification (cross-ref)" }
  linked_objectives: [SO-GDPR-038]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-REQUEST]
  regulatory_rationale: |
    Art. 12(5) provides that information under Art. 13 and 14 and any communication and any actions taken under Arts. 15 to 22 and 34 shall be provided free of charge. Where requests from a data subject are manifestly unfounded or excessive, in particular because of their repetitive character, the controller may either (a) charge a reasonable fee taking into account the administrative costs of providing the information or communication or taking the action requested, or (b) refuse to act on the request. The controller shall bear the burden of demonstrating the manifestly unfounded or excessive character of the request. Art. 12(6) permits the controller, where there are reasonable doubts concerning the identity of the natural person making a request under Arts. 15 to 21, to request the provision of additional information necessary to confirm the identity of the data subject, but does not permit the controller to retain the additional information longer than needed for identity confirmation.
  security_rationale: |
    The obligation in Art. 12(5) and Art. 12(6) is operationalised in NIST CSF 2.0
    through **GV.PO-02 (Cybersecurity processes and procedures established,
    communicated, and enforced)**.

    GV.PO-02 controls the documented anti-abuse process for rights-exercise
    channels: the controller must establish and enforce a written procedure that
    defines the thresholds for treating a request as manifestly unfounded or
    excessive — particularly the repetitive-character trigger — and that
    articulates the identity-verification step under Art. 12(6) where reasonable
    doubts exist, including the rule that additional information collected for
    verification is not retained beyond the confirmation purpose. The procedure
    must also record the controller's demonstrative burden: under Art. 12(5) the
    controller must produce evidence that the request is manifestly unfounded or
    excessive, and refusal cannot rest on general suspicion. The response-channel
    integrity dimension maps onto the broader NIST CSF authorisation-channel
    family, with GV.PO-02 as the anchor subcategory.

    Embedded in an established, enforced process, GV.PO-02 enables ex-post
    demonstration to the supervisory authority — through a rights-request
    register that captures refusal-and-fee decisions alongside successful
    responses, with documented thresholds and demonstrative evidence — that the
    anti-abuse powers were exercised only where the Art. 12(5) burden was met and
    that identity verification under Art. 12(6) did not exceed its purpose.
  ambiguity_notes: |
    Manifestly unfounded or excessive carries VAG-S3 because the OJ text does not fix a quantitative threshold. Reading chosen: clearly frivolous on the face of the request, such that automated rejection on the basis of documented criteria is acceptable; the controller bears the burden of demonstrating the request is manifestly unfounded or excessive, per the second sentence of Art. 12(5), and the demonstrative burden is not satisfied by the controller's general suspicion. An alternative reading would allow refusal whenever the controller has any doubt about the request's purpose; this reading is rejected as incompatible with the demonstrative burden and with Art. 12(6) which addresses identity verification as a separate channel rather than as a refusal ground. A second alternative reading confines manifestly unfounded to requests the controller considers pointless and excludes repetitive-but-not-frivolous requests from the refusal grounds; this reading is consistent with the OJ text but operationally narrows the controller's protective scope. Remain open: (a) whether repetitive character requires a pattern of requests from the same data subject or includes patterns of requests across data subjects coordinated against the same controller; (b) whether the Art. 12(6) additional-information request is itself subject to the Art. 12(3) 1-month response window or whether the clock pauses until identity is confirmed.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-068
  title: "Collection-time data-disclosure with documented source triggers"
  source_clauses:
    - { clause_id: GDPR-RT05, article_ref: "Art. 13(1) — collection-time information" }
    - { clause_id: GDPR-RT07, article_ref: "Art. 14(1)/(2) — third-party-source information" }
  linked_objectives: [SO-GDPR-038]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: ID.AM-03, title: "Inventories of data and metadata for designated data types" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-COLLECTION]
  regulatory_rationale: |
    Art. 13(1) requires the controller, at the time when personal data are obtained from the data subject, to provide the data subject with the identity and contact details of the controller, the contact details of the data protection officer, the purposes of the processing, the legal basis for the processing, the recipients or categories of recipients of the personal data, and where applicable the fact that the controller intends to transfer personal data to a third country or international organisation and the existence or absence of an adequacy decision or reference to the appropriate or suitable safeguards and the means by which to obtain a copy of them or where they have been made available. Art. 13(2) requires further information where the controller intends further processing for a purpose other than that for which the personal data were collected. Art. 14(1) and (2) require the same set, plus the source of the data, where the personal data have not been obtained from the data subject, and the controller shall provide that information within a reasonable period after obtaining the personal data, but at the latest within one month, having regard to the specific circumstances in which the personal data are processed.
  security_rationale: |
    The obligation in Art. 13(1) and Art. 14(1)/(2) is operationalised in NIST CSF
    2.0 through **ID.AM-03 (Inventories of data and corresponding metadata for
    designated data types maintained)** and **PR.DS-12 (Data managed consistent
    with the organization's risk strategy to protect the confidentiality,
    integrity, and availability of data)**.

    ID.AM-03 controls the data inventory that underpins collection-time
    disclosure: the controller must maintain records of data categories,
    recipients and recipient categories, and transfer destinations, so that the
    Art. 13/14 notice content can be generated from the inventory rather than
    reconstructed per request. The metadata dimension captures the source-
    disclosure trigger under Art. 14(3), which runs from the moment of obtaining
    third-party-source data and expires at the latest within one month. PR.DS-12
    controls the data-management discipline that translates the inventory into
    consistent notice content: legal-basis labelling, transfer-mechanism
    referencing, and the linkage between the Art. 30 internal records and the
    Art. 13/14 data-subject-readable notices.

    Together the two subcategories embed collection-time disclosure in a
    maintained data-and-metadata inventory (ID.AM-03) backed by risk-strategy-
    consistent data management (PR.DS-12), enabling ex-post demonstration to the
    supervisory authority that the notice content was accurate at the time of
    collection and that the Art. 14(3) source-disclosure clock was triggered and
    discharged within the one-month ceiling.
  ambiguity_notes: |
    Categories of recipients and categories of personal data under Art. 13/14 carry POLY-S2 because the OJ text does not fix the granularity of the categories; both readings converge on a closed-list privacy-notice template that names the recipient categories (processors, group entities, public authorities where applicable) and the data categories (contact data, behavioural data, special-category data where applicable) without enumerating every individual recipient or data field. Reasonable period and within one month under Art. 14(3) carry VAG-S3 as a twin temporal pair: the 1-month hard ceiling is binding and reasonable period is read as a direction toward earlier disclosure where practicable. An alternative reading would treat categories of recipients as requiring named third-country recipients rather than category-level disclosure; this reading increases transparency but is not consistently required by supervisory authorities and conflicts with the privacy-by-design principle where named-recipient lists are operationally fragile (recipients change frequently). A second alternative reading treats reasonable period as a separate qualifier that may extend beyond the 1-month ceiling in narrow circumstances; this reading is rejected because the article states within one month as a binding ceiling rather than as a default that can be extended. Remain open: (a) whether categories of recipients must name specific named recipients in third-country destinations or whether region-level granularity (for example, US-based processors) satisfies the disclosure duty; (b) whether the Art. 14(5)(b) disproportionate-effort exception applies to first-party recipients or only to the source-disclosure component of Art. 14.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

