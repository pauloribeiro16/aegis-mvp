---
document_id: AEGIS-PREPROC-GDPR-ART-46
title: GDPR Art. 46 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 46
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

# GDPR Art. 46

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-033 | Cross-border transfers of personal data to third countries or international organisations maintain the GDPR's level of protection and rely on the Art. 46 appropriate-safeguards mechanism (including SCCs, BCRs, codes of conduct, or certification), where no Art. 45 adequacy decision applies. | `GDPR-TR04` (Art. 46(1)); `GDPR-TR05` (Art. 46(2)); `GDPR-TR01` (Art. 44) | D-06.3, D-05.1 |
| SO-GDPR-033 | Cross-border transfer of personal data takes place only where the conditions laid down in Chapter V are complied with (Art. 44); where no Commission adequacy decision exists (Art. 45), appropriate safeguards (Art. 46) are in place; absent both, derogations under Art. 49 are used only as narrowly-defined conditions, with the catch-all applying only when transfers are not repetitive, concern a limited number of data subjects, are necessary for compelling legitimate interests, and are accompanied by suitable safeguards. | `GDPR-TR01` (Art. 44); `GDPR-TR02` (Art. 45(1)); `GDPR-TR03` (Art. 45(3) — periodic review); `GDPR-TR04` (Art. 46(1)); `GDPR-TR05` (Art. 46(2)); `GDPR-TR08`–`GDPR-TR10` (Art. 49(1)(a)/(d) and catch-all); `GDPR-C07` (Art. 4(16) — main establishment) | D-06.3, D-09.1, D-05.1 |
| SO-GDPR-033 | D-06.3, D-09.1, D-05.1 | Art. 44, Art. 45, Art. 46, Art. 49, Art. 4(16) | Cross-border transfers maintain GDPR protection level |

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
- sr_id: SR-GDPR-057
  title: "Derogation-based transfer fallback under strict preconditions"
  source_clauses:
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit consent" }
    - { clause_id: GDPR-TR09, article_ref: "Art. 49(1)(d) — important public interest" }
    - { clause_id: GDPR-TR10, article_ref: "Art. 49(1) second subparagraph — catch-all" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: UNMAPPED_CSF, title: "Derogation under Art. 49 is GDPR-specific with no clean CSF 2.0 mapping" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER, ONE_TIME]
  regulatory_rationale: |
    Art. 49 derogations apply only in the absence of an adequacy decision under Art. 45(3) and of appropriate safeguards under Art. 46, including binding corporate rules. Art. 49(1) lists seven disjunctive grounds: explicit consent after being informed of possible risks; necessity for the performance of a contract between the data subject and the controller or implementation of pre-contractual measures at the data subject's request; necessity for a contract concluded in the interest of the data subject between the controller and another natural or legal person; important reasons of public interest; establishment, exercise or defence of legal claims; protection of the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent; transfer from a register intended to provide information to the public (Recital 111–115). The second subparagraph of Art. 49(1) adds a catch-all: transfers may take place where the transfer is not repetitive, concerns a limited number of data subjects, is necessary for compelling legitimate interests of the controller which are not overridden by the interests, rights or freedoms of the data subject, and the controller has assessed all the circumstances and put in place suitable safeguards (Recital 113).
  security_rationale: |
    The obligation in Art. 49(1)(a), Art. 49(1)(d) and Art. 49(1) second
    subparagraph has no clean NIST CSF 2.0 subcategory and is anchored on the
    closest fit **GV.OC-03 (Legal, regulatory, and contractual requirements
    regarding cybersecurity — including privacy and civil liberties obligations —
    are understood and managed)** within the broader **GV.OC — Organizational
    Context** category; the residual gap is noted as UNMAPPED_CSF.

    GV.OC-03 controls the controller's understanding of the regulatory
    preconditions on which any Art. 49 derogation depends — absence of an
    adequacy decision under Art. 45(3), absence of Art. 46 appropriate
    safeguards, and satisfaction of one of the seven enumerated grounds or the
    catch-all (not repetitive, limited number of data subjects, compelling
    legitimate interests, suitable safeguards). CSF 2.0 does not enumerate
    derogation-availability analysis and GV.OC-03 is a poor fit because it is
    designed for ongoing regulatory understanding rather than exception-
    availability gating, but it is the closest available anchor.

    Because the CSF gap is documented, the controller must supplement GV.OC-03
    with a GDPR-specific derogation-use register that records each catch-all
    reliance, the compelling-interests analysis, and the suitable safeguards
    deployed. Accountability is sustained through the documented gap
    (UNMAPPED_CSF + unmapped_csf_justification) and through GV.OC-03's
    regulatory-understanding trail that demonstrates the derogation fallback was
    used only where adequacy and Art. 46 safeguards were unavailable.
  ambiguity_notes: |
    Explicitly (Art. 49(1)(a)) carries POLY-S3 against the specific qualifier of Art. 4(11) and the explicit qualifier of Art. 9(2)(a); reading chosen: the strongest consent form, risk-informed and documented, building on EDPB Guidelines 05/2020 §3.4 and the Schrems II framing of risk disclosure. The catch-all qualifiers not repetitive, limited number, compelling legitimate interests, suitable safeguards carry VAG-S3 and SCOPE-Q-S3 because none of them is quantitatively bounded in the OJ text; compelling in particular carries POLY-S3 across Art. 21(1) and Art. 49(1) (Recital 47 cross-reference), and the EDPB Guidelines 2/2018 emphasise that compelling means more than legitimate and approaches necessity. An alternative reading confines the catch-all to transfers that are truly exceptional and treats recurring or systematic reliance on it as a structural misuse of the derogation; this reading is consistent with that framing and operationally shifts the burden onto the controller to demonstrate the exceptional nature of each catch-all reliance. A second alternative reading treats not repetitive as a per-data-subject test rather than per-data-flow; this reading is harder to operationalise and is inconsistent with the structural purpose of the catch-all. Remain open: (a) whether repetitive in the catch-all should be measured per data subject, per transfer, or per data flow, given that no OJ anchor specifies the unit; (b) whether suitable safeguards in the catch-all may be purely contractual or must include technical measures (encryption, pseudonymisation) per Schrems II §134.
  unmapped_csf_justification: |
    The four Art. 49 catch-all conjunctive qualifiers and the
    `compelling legitimate interests` qualifier have no clean CSF 2.0
    Subcategory. The closest mapping GV.OC-03 is a poor fit.
```

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

