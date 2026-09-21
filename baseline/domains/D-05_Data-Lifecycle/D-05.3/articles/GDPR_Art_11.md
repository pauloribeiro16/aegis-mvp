---
document_id: AEGIS-PREPROC-GDPR-ART-11
title: GDPR Art. 11 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 11
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
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---

# GDPR Art. 11

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-005 | The identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification, before action is taken. | `GDPR-RT04` (Art. 12(6)); `GDPR-CL26` (Art. 11(2)) | D-03.1, D-09.4 |
| SO-GDPR-005 | D-03.1, D-09.4 | Art. 12(6), Art. 11(2) | Reasonable identity verification for rights requests |

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

