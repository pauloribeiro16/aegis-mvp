---
document_id: AEGIS-PREPROC-GDPR-ART-63
title: GDPR Art. 63 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 63
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# GDPR Art. 63

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-058
  title: "Binding corporate rules for intragroup transfers"
  source_clauses:
    - { clause_id: GDPR-C08, article_ref: "Art. 4(20) — BCR definition" }
    - { clause_id: GDPR-TR06, article_ref: "Art. 47(2)(a)–(n) — 14 content items" }
  linked_objectives: [SO-GDPR-034]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "Cybersecurity supply chain risk management program/strategy established" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-BCR, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(20) defines binding corporate rules (BCRs) as personal data protection policies which are adhered to by a controller or processor established on the territory of a Member State for transfers or a set of transfers of personal data to a controller or processor in one or more third countries within a group of undertakings, or group of enterprises engaged in a joint economic activity. Art. 47(1) requires the competent supervisory authority to approve BCRs in accordance with the consistency mechanism, provided they are legally binding and applied by every member concerned of the group, expressly confer enforceable rights on data subjects, and fulfil the requirements laid down in Art. 47(2). Art. 47(2) enumerates 14 mandatory content items: structure and contact details of the group; data transfers and processing categories; legally binding nature; application of general data protection principles; data subject rights; controller or processor responsibilities; data protection officer; complaint mechanisms; cooperation with supervisory authorities; training; audit procedures; reporting and recording of changes; cooperation procedure with the supervisory authority. The list is closed and all 14 items must be present (Recital 108).
  security_rationale: |
    The obligation in Art. 4(20) and Art. 47(2)(a)–(n) is operationalised in NIST
    CSF 2.0 through **GV.SC-01 (Cybersecurity supply chain risk management
    program, strategy, objectives, policies, and processes established and agreed
    to by organizational stakeholders)** and **GV.SC-03 (Contracts with suppliers
    and other third parties used to implement appropriate measures)**.

    GV.SC-01 controls the group-level SCRM programme within which binding
    corporate rules sit: the BCR is the group-wide data-policy instrument that
    every member of the undertaking adheres to, supervised by the competent
    authority under the Art. 47(1) consistency mechanism. GV.SC-03 controls the
    binding contractual nature of the BCR itself, with the 14 mandatory Art.
    47(2) content items — group structure, transfer categories, legal binding
    force, principle application, data-subject rights, controller responsibility,
    DPO, complaint mechanism, supervisory cooperation, training, audit, change
    reporting — articulated as SCRM contractual clauses.

    Together the two subcategories embed the BCR within an established
    group-level programme (GV.SC-01) backed by an enforceable intra-group
    contract (GV.SC-03), enabling ex-post demonstration to the supervisory
    authority that all 14 Art. 47(2) items are present, that every group member
    is bound, and that data-subject rights are enforceable against any member of
    the undertaking.
  ambiguity_notes: |
    The 14-element AND-list is COORD-S2: all 14 items are mandatory, the list is closed, and a BCR that omits any item cannot be approved by the competent supervisory authority. Art. 47(2)(f) on demonstrating not being responsible for the event giving rise to the damage carries VAG-S3 because the OJ text does not fix the standard of proof; reading chosen: the controller demonstrates on a balance of probabilities that the damage did not arise from its act or omission, which is the civil-law burden-of-proof convention and is consistent with EDPB BCR guidance on the operation of the joint-controller regime within the group. An alternative reading would treat the 14-element list as enumerative rather than closed, allowing the controller to substitute equivalent provisions for selected items; this reading is rejected because Art. 47(2) presents the list as a closed set and the supervisory-authority approval under Art. 47(1) requires full coverage. A second alternative reading would treat Art. 47(2)(f) on the balance-of-proof question as applying the higher criminal-law standard; this reading is rejected because the article is silent on the standard and the EDPB BCR guidance treats it as a civil-law matter. Remain open: (a) whether the 14-element list permits Member State-specific additions for sectors with stricter national rules, or whether the closed-list reading precludes any national-layer expansion; (b) whether BCRs approved under the predecessor Directive 95/46/EC remain valid post-GDPR entry into force or must be re-approved under the Art. 63 consistency mechanism.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

