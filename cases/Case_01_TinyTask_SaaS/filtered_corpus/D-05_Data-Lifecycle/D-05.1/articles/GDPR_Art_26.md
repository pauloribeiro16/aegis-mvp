---
document_id: AEGIS-PREPROC-GDPR-ART-26
title: GDPR Art. 26 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 26
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
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 26

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-036 | Where two or more controllers jointly determine purposes and means of processing, they determine their respective responsibilities for GDPR compliance in a transparent manner by means of an arrangement reflecting the roles of the joint controllers, made available to data subjects; data subjects may exercise their rights against each controller irrespective of the arrangement. | `GDPR-CP04` (Art. 26(1)); `GDPR-CP05` (Art. 26(2)); `GDPR-C03` (Art. 4(7) — controller/joint controllers) | D-09.2, D-06.3 |
| SO-GDPR-036 | D-09.2, D-06.3 | Art. 26(1)/(2), Art. 4(7) | Joint-controller arrangement transparency |

## Security Rules (from 02_SecurityRules_NIST.md)

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

