---
document_id: AEGIS-PREPROC-GDPR-ART-30
title: GDPR Art. 30 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 30
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# GDPR Art. 30

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-017 | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed; longer retention is permitted only where lawful and subject to the appropriate Art. 89(1) safeguards. | `GDPR-CL05` (Art. 5(1)(e)); `GDPR-CP12` (Art. 30(1)(f)) | D-05.2 |
| SO-GDPR-017 | D-05.2 | Art. 5(1)(e), Art. 30(1)(f) | Storage limitation — no longer than necessary |
| SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations and on the controller's or processor's data-protection policies applicable to their role. | `GDPR-CP28` (Art. 39(1)(b) — DPO tasks on awareness/training); `GDPR-CP28` (Art. 39(1)(a)); `GDPR-CP12` (Art. 30 — awareness of staff); `GDPR-TR06` (Art. 47(2)(n) — BCR training) | D-08.1, D-08.2 |
| SO-GDPR-025 | D-08.1, D-08.2 | Art. 39(1)(a)/(b), Art. 30(4), Art. 47(2)(n) | Staff informed and trained on data-protection obligations |
| SO-GDPR-029 | Each controller and processor maintains records of processing activities, in writing or electronic form, containing the Art. 30(1)/(2) content items, made available to the supervisory authority on request. | `GDPR-CP12` (Art. 30(1)/(2)/(3)/(4)); `GDPR-CP13` (Art. 30(5) — 250-employee exception) | D-09.4, D-10.2 |
| SO-GDPR-029 | D-09.4, D-10.2 | Art. 30(1)–(5) | Records of processing activities (RoPA) |
| SO-GDPR-031 | Compliance records (records of processing, consent records, processor contract records, breach notification records, DPIA records) are maintained in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections. | `GDPR-CP12` (Art. 30(3)); `GDPR-CL07` (Art. 5(2) — accountability / demonstrability); `GDPR-CP14` (Art. 31 — SA cooperation) | D-10.2, D-09.4 |
| SO-GDPR-031 | D-10.2, D-09.4 | Art. 30(3), Art. 5(2), Art. 31 | Audit-grade records integrity and traceability |

## Security Rules (from 02_SecurityRules_NIST.md)

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

