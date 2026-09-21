---
document_id: AEGIS-PREPROC-GDPR-ART-47
title: GDPR Art. 47 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 47
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

# GDPR Art. 47

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations and on the controller's or processor's data-protection policies applicable to their role. | `GDPR-CP28` (Art. 39(1)(b) — DPO tasks on awareness/training); `GDPR-CP28` (Art. 39(1)(a)); `GDPR-CP12` (Art. 30 — awareness of staff); `GDPR-TR06` (Art. 47(2)(n) — BCR training) | D-08.1, D-08.2 |
| SO-GDPR-025 | D-08.1, D-08.2 | Art. 39(1)(a)/(b), Art. 30(4), Art. 47(2)(n) | Staff informed and trained on data-protection obligations |
| SO-GDPR-034 | Binding corporate rules for intra-group transfers (Art. 47) are approved by the competent supervisory authority via the consistency mechanism, confer enforceable rights on data subjects, and contain the 14 Art. 47(2) content items — including acceptance of liability by the EU controller/processor for breaches by non-EU members (subject to the `proves not responsible` rebuttal standard). | `GDPR-C08` (Art. 4(20) — BCR definition); `GDPR-TR06` (Art. 47(2)(f) and full 14-item list) | D-09.1, D-06.3 |
| SO-GDPR-034 | D-09.1, D-06.3 | Art. 4(20), Art. 47(1)/(2) | Binding corporate rules with Art. 47(2) content |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-056
  title: "Appropriate-safeguards mechanism selection for third-country transfers"
  source_clauses:
    - { clause_id: GDPR-TR04, article_ref: "Art. 46(1)" }
    - { clause_id: GDPR-TR05, article_ref: "Art. 46(2)(a)–(f) — six mechanism types" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits and test results" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER]
  regulatory_rationale: |
    Art. 46(1) requires that, in the absence of an Art. 45(3) adequacy decision, the controller or processor may transfer personal data to a third country or international organisation only if it has provided appropriate safeguards, and on condition that enforceable data subject rights and effective legal remedies for data subjects are available. Art. 46(2) enumerates six mutually exclusive appropriate-safeguards mechanisms: (a) a legally binding and enforceable instrument between public authorities or bodies; (b) binding corporate rules in accordance with Art. 47; (c) Commission-adopted standard data protection clauses; (d) supervisory-authority-adopted standard data protection clauses approved by the Commission; (e) approved codes of conduct with binding and enforceable commitments; (f) approved certification mechanisms with binding and enforceable commitments. The list is closed and the controller selects one mechanism per transfer or set of transfers (Recital 116). The Schrems II ruling (C-311/18) confirmed that appropriate safeguards must produce essentially equivalent protection to the EU baseline and that pre-existing Commission SCCs adopted under Directive 95/46/EC require supplementary measures to cure Schrems II deficiencies.
  security_rationale: |
    The obligation in Art. 46(1) and Art. 46(2)(a)–(f) is operationalised in NIST
    CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third parties
    used to implement appropriate measures)** and **GV.SC-04 (Suppliers and other
    third parties routinely assessed using audits, test results, or other forms
    of evaluation)**.

    GV.SC-03 controls the contractual vehicle for each transfer: the controller
    must select one of the six closed-list Art. 46(2) mechanisms — binding
    instrument, BCRs, Commission SCCs, supervisory-authority SCCs, codes of
    conduct, or certification — and embed it in the processor or recipient
    contract as the SCRM-implementing instrument. The Schrems II ruling
    (C-311/18 §96) requires that the selected mechanism produce essential
    equivalence with EU protection, supplemented where the destination regime is
    deficient. GV.SC-04 controls the routine assessment of suppliers and
    recipients through audits and test results, which operationalises the
    transfer-impact assessment and the documented supplementary-measures
    analysis.

    Together the two subcategories convert per-transfer safeguard selection from
    ad-hoc negotiation into a documented design choice with an audit trail
    (GV.SC-03) embedded in a routine supplier-assessment cycle (GV.SC-04),
    enabling ex-post demonstration to the supervisory authority that the
    mechanism selection was reasoned and that supplementary measures remain
    adequate as destination conditions evolve.
  ambiguity_notes: |
    Appropriate safeguards and effective legal remedies carry VAG-S3 because the OJ text does not fix quantitative thresholds and the substantive adequacy of any safeguard is contingent on the destination regime. Reading chosen: the safeguards must produce essential equivalence with EU protection, per Schrems II (C-311/18 §96), operationalised through any of the six Art. 46(2) mechanisms and supported by supplementary measures where the destination regime is deficient in a specific respect (EDPB Recommendations 01/2020). The selection among the six mechanisms is OR (COORD-S3): the controller chooses one mechanism per transfer, not a combination, and the choice must be documented and reassessed when circumstances change. An alternative reading would allow combining several Art. 46(2) mechanisms to achieve a layered defence; this reading is inconsistent with the textual structure of Art. 46(2), which presents the six mechanisms as alternatives, and is rejected by EDPB Recommendations 01/2020. A second alternative reading confines the supplementary-measures framework to destinations where the public-authority access regime is materially deficient, allowing the controller to skip supplementary measures where the destination regime is broadly adequate; this narrower reading is consistent with Schrems II §134 but requires the controller to make a documented destination-risk assessment. Remain open: (a) whether BCRs approved before the GDPR entry into force remain valid without re-approval under the GDPR consistency mechanism, given the absence of explicit grandfathering in Art. 46(2)(b); (b) whether Art. 46(2)(c) Commission SCCs adopted before Schrems II (the 2001/915/EC and 2004/915/EC decisions) remain valid or require supplementary measures to cure Schrems II deficiencies.
```

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

