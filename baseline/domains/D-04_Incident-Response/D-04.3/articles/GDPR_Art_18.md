---
document_id: AEGIS-PREPROC-GDPR-ART-18
title: GDPR Art. 18 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 18
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---

# GDPR Art. 18

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

