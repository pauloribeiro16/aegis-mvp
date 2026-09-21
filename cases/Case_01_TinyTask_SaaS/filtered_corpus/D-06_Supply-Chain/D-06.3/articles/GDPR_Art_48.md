---
document_id: AEGIS-PREPROC-GDPR-ART-48
title: GDPR Art. 48 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 48
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
status: DRAFT
---

# GDPR Art. 48

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-035 | Court or administrative-authority decisions of a third country requiring a controller or processor to transfer or disclose personal data are recognised or enforceable only if based on an international agreement (such as a mutual legal assistance treaty) in force between the requesting third country and the Union or a Member State. | `GDPR-TR07` (Art. 48) | D-06.3 |
| SO-GDPR-035 | D-06.3 | Art. 48 | Third-country legal requests only on international agreement |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-059
  title: "Third-country legal-request recognition filter via international agreements"
  source_clauses:
    - { clause_id: GDPR-TR07, article_ref: "Art. 48 — third-country legal-request filter" }
  linked_objectives: [SO-GDPR-035]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-REQUEST]
  regulatory_rationale: |
    Art. 48 provides that judgments or administrative decisions of third countries requiring a controller or processor to transfer or disclose personal data may only be recognised or enforced in any manner on the basis of an international agreement, such as a mutual legal assistance treaty (MLAT), in force between the requesting third country and the Union or a Member State, without prejudice to other grounds for transfer pursuant to Chapter V. The provision is the GDPR's response to the risk of extra-territorial legal-process demands that bypass the EU's cooperation regime, and it does not preclude transfers under the Chapter V mechanisms but rather adds a recognition-and-enforcement filter on the receiving-side process (Recital 6 on international cooperation). The scope of Art. 48 extends to any third-country administrative or judicial decision that compels transfer or disclosure, regardless of whether the decision names the controller or addresses it indirectly, so the controller cannot rely on a narrow reading that excludes indirect orders. The interplay with the U.S. CLOUD Act is the canonical operational example: an MLAT-based request from a U.S. authority is enforceable on Art. 48 grounds, while an extraterritorial CLOUD Act order directed at an EU-headquartered provider is not.
  security_rationale: |
    The obligation in Art. 48 is operationalised in NIST CSF 2.0 through
    **GV.OC-03 (Legal, regulatory, and contractual requirements regarding
    cybersecurity — including privacy and civil liberties obligations — are
    understood and managed)** and **GV.SC-03 (Contracts with suppliers and other
    third parties used to implement appropriate measures)**.

    GV.OC-03 controls the controller's understanding of the international-
    agreement filter that Art. 48 imposes: third-country judgments or
    administrative decisions compelling transfer or disclosure may be recognised
    or enforced only on the basis of a binding international agreement (such as a
    mutual legal assistance treaty) in force between the requesting third country
    and the Union or a Member State. GV.SC-03 controls the contractual
    articulation of this filter in processor agreements, requiring that any
    third-country legal request be escalated to the controller before disclosure
    and that the recognition-and-enforcement gate be documented in the
    data-processing agreement.

    Together the two subcategories embed extra-territorial legal-request
    resistance in a managed regulatory-understanding frame (GV.OC-03) backed by
    contractual escalation clauses (GV.SC-03), enabling ex-post demonstration to
    the supervisory authority that no third-country order was honoured without an
    international-agreement basis and that the refusal-and-escalation chain is
    auditable through a designated accountable owner.
  ambiguity_notes: |
    Such as a mutual legal assistance treaty carries POLY-S3 because the OJ text uses a non-exemplifying list and the term itself is undefined in GDPR. Reading chosen: the broad reading, in which any binding international agreement between the third country and the EU or a Member State qualifies, on the practical ground that the CLOUD Act conflict demonstrates that formal MLATs are too narrow a vehicle for the volume and velocity of contemporary cross-border legal-process traffic; EDPB Guidelines 5/2022 on the interplay with the CLOUD Act adopt a similar practical reading. An alternative reading limits the qualifier to formal MLATs and excludes unilateral instruments such as executive agreements or executive orders; this reading is rejected because it would render Art. 48 largely ineffective against the practical pattern it was meant to address. A second alternative reading treats Art. 48 as covering only the recognition and enforcement of foreign judgments, not the underlying transfer obligation; this reading is consistent with the text of Art. 48 but operationally creates a loophole where a transfer can occur in compliance with Chapter V while the third-country legal-process filter applies only to recognition of the resulting judgment. Remain open: (a) whether a transfer pursuant to a valid Chapter V mechanism (adequacy, Art. 46 safeguards, Art. 49 derogation) is itself the relevant compliance anchor even where the third-country request lacks an international-agreement basis, on the view that Art. 48 regulates recognition and enforcement of the request rather than the underlying transfer; (b) whether the controller must challenge the third-country legal request in the third-country courts before refusing disclosure, or whether refusal grounded in Art. 48 alone discharges the obligation.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

