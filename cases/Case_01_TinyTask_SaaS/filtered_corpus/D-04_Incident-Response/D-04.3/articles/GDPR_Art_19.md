---
document_id: AEGIS-PREPROC-GDPR-ART-19
title: GDPR Art. 19 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 19
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---

# GDPR Art. 19

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-012 | Rectification, erasure, or restriction of processing is cascaded to each recipient to whom the personal data have been disclosed, unless impossible or involving disproportionate effort; the data subject is informed of those recipients on request. | `GDPR-RT15` (Art. 19) | D-04.3 |
| SO-GDPR-012 | D-04.3 | Art. 19 | Cascade rectification/erasure/restriction notification |

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

