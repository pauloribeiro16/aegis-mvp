---
document_id: AEGIS-PREPROC-GDPR-ART-12
title: GDPR Art. 12 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 12
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# GDPR Art. 12

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-005 | The identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification, before action is taken. | `GDPR-RT04` (Art. 12(6)); `GDPR-CL26` (Art. 11(2)) | D-03.1, D-09.4 |
| SO-GDPR-005 | D-03.1, D-09.4 | Art. 12(6), Art. 11(2) | Reasonable identity verification for rights requests |
| SO-GDPR-038 | The controller provides transparent, concise, intelligible, easily accessible information in clear and plain language to data subjects on processing operations (Art. 13/14 collection notices), supports the exercise of data-subject rights (Art. 15–22), verifies identity on reasonable doubt, responds to rights requests within one month (extendable by two further months where necessary), and acts free of charge except in defined exception cases. | `GDPR-RT01` (Art. 12(1)); `GDPR-RT02` (Art. 12(3)); `GDPR-RT03` (Art. 12(5)); `GDPR-RT04` (Art. 12(6)); `GDPR-RT05` (Art. 13(1)); `GDPR-RT06` (Art. 13(2)(f)); `GDPR-RT07` (Art. 14(1)/(2)); `GDPR-RT08` (Art. 14(5)(b)) | D-09.4, D-05.4 |
| SO-GDPR-038 | D-09.4, D-05.4 | Art. 12, Art. 13, Art. 14 | Information duties and rights-exercise support |

## Security Rules (from 02_SecurityRules_NIST.md)

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
- sr_id: SR-GDPR-066
  title: "One-month SLA on data-subject rights requests"
  source_clauses:
    - { clause_id: GDPR-RT02, article_ref: "Art. 12(3) — 1-month response" }
  linked_objectives: [SO-GDPR-038]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: RS.MA-02, title: "Incident reports triaged and validated" }
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-REQUEST]
  regulatory_rationale: |
    Art. 12(3) requires the controller to provide information on action taken on a request under Arts. 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. That period may be extended by two further months where necessary, taking into account the complexity and number of the requests. The controller shall inform the data subject of any such extension within one month of receipt of the request, together with the reasons for the delay. When the controller does not act on the request, the controller shall inform the data subject without delay and at the latest within one month of receipt of the request of the reasons for not taking action and on the possibility of lodging a complaint with a supervisory authority and seeking a judicial remedy. Art. 12(4) applies where the controller has reasonable doubts concerning the identity of the natural person making the request, allowing the controller to request additional information necessary to confirm identity.
  security_rationale: |
    The obligation in Art. 12(3) and Art. 12(4) is operationalised in NIST CSF 2.0
    through **RS.MA-02 (Incident reports triaged and validated)** and **RS.CO-02
    (Incidents reported internally to the appropriate stakeholders, including
    executive leadership and legal counsel)**.

    RS.MA-02 controls the triage and validation of incoming data-subject rights
    requests under Arts. 15–22: the controller must log each request on receipt,
    validate its admissibility (including identity verification under Art. 12(6)
    where reasonable doubts exist), and track it against the 1-month deadline or
    the justified 3-month extension where complexity or request volume requires.
    RS.CO-02 controls the internal escalation chain: the rights-handling
    function must report to the appropriate internal stakeholders — including the
    DPO, legal counsel and operational owners of the affected processing — so
    that the response meets the deadline or that the Art. 12(3) decline-and-
    reason obligation is discharged within the same window.

    Together the two subcategories embed the Art. 12(3) SLA in an incident-
    management-style triage and escalation cycle (RS.MA-02 + RS.CO-02), enabling
    ex-post demonstration through a rights-request register — capturing receipt
    date, request type, extension decision and notification, response date and
    substantive action — that no deadline was missed without justification.
  ambiguity_notes: |
    Without undue delay and where necessary (extension) carry VAG-S3 because the OJ text does not fix quantitative thresholds for either. Reading chosen: 1 month is the hard ceiling and the extension to 3 months requires demonstrated complexity (multiple data subjects, multi-source data, third-party coordination), with notification of the extension to be issued within the original 1-month window. An alternative reading would treat without undue delay as an independent shorter-than-1-month trigger that applies alongside the 1-month ceiling; this alternative is rejected by EDPB Guidelines on Art. 12, which treat the 1-month ceiling as the binding deadline and undue delay as a directional qualifier rather than a separate deadline. A second alternative reading treats the 2-month extension as available for any reason, with where necessary interpreted as a permissive trigger; this reading is rejected because the Article ties the extension to complexity and number of requests. Remain open: (a) whether the extension notification must be issued at the time of extension decision or at the latest at the 1-month mark, and which supervisory authority practice applies where the two diverge; (b) whether the controller's failure to act under Art. 12(3) triggers separate Art. 12(4) reasoning obligations with their own 1-month deadline running in parallel.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

