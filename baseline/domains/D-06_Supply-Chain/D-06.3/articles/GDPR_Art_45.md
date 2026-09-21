---
document_id: AEGIS-PREPROC-GDPR-ART-45
title: GDPR Art. 45 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 45
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

# GDPR Art. 45

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
- sr_id: SR-GDPR-055
  title: "Adequacy-governed cross-border transfer inventory and review"
  source_clauses:
    - { clause_id: GDPR-TR01, article_ref: "Art. 44 — general transfer principle" }
    - { clause_id: GDPR-TR02, article_ref: "Art. 45(1) — adequacy-based transfer" }
    - { clause_id: GDPR-TR03, article_ref: "Art. 45(3) — periodic review of adequacy" }
    - { clause_id: GDPR-C07, article_ref: "Art. 4(16) — main establishment (cross)" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER]
  regulatory_rationale: |
    Art. 44 establishes the umbrella principle for cross-border transfers: any transfer of personal data to a third country or international organisation shall take place only if the Chapter V conditions are complied with by the controller and processor, including for onward transfers, and the level of protection of natural persons guaranteed by GDPR is not undermined (Recital 6). Art. 45(1) exempts transfers covered by a Commission adequacy decision from any specific authorisation requirement, on the basis that the third country, territory, sector or international organisation ensures an adequate level of protection. Art. 45(3) requires the Commission to specify, in its implementing decision, the mechanism for a periodic review of that adequacy assessment, at least every four years, and to amend, suspend or repeal the decision where the available information reveals that the third country or international organisation no longer ensures an adequate level of protection. Art. 4(16) anchors the main-establishment concept used in Art. 44 for determining which supervisory authority has jurisdiction over the cross-border processing.
  security_rationale: |
    The obligation in Art. 44, Art. 45(1) and Art. 45(3) is operationalised in
    NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties known,
    prioritized, and assessed using a cybersecurity supply chain risk management
    process)**, **GV.SC-03 (Contracts with suppliers and other third parties used
    to implement appropriate measures)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    GV.SC-02 controls the inventory and prioritisation of cross-border data
    flows: the controller must maintain a transfer register that maps every
    outbound flow to its destination, its legal mechanism, and its assessed risk
    under the Schrems II substantial-equivalence test. GV.SC-03 controls the
    contractual articulation of each transfer's safeguards, including
    onward-transfer clauses that bind downstream recipients to equivalent
    protection. GV.OC-03 controls the legal-basis frame, including the temporal
    stability of adequacy decisions and the trigger for re-assessment whenever
    the Commission adopts, suspends or repeals an Art. 45(3) decision.

    Together the three subcategories give the controller a SCRM-style governance
    of cross-border data flows embedded in a managed regulatory frame, enabling
    ex-post demonstration to the supervisory authority that every transfer is
    inventoried, contractually anchored, and reassessed against the latest
    adequacy posture.
  ambiguity_notes: |
    The not undermined qualifier of Art. 44 carries VAG-S3 because the OJ text does not fix a metric for the level of protection and supervisory authorities have not published a quantitative threshold. Reading chosen: the substantial-equivalence reading from CJEU Schrems II (C-311/18 §96), under which the essential content of EU protection must be preserved in the third country, with the EDPB Recommendations 01/2020 supplementary-measures framework operating as the operational remediation path when the destination regime falls short. An alternative reading would treat not undermined as a procedural rather than substantive requirement, satisfied by the existence of any lawful basis for the transfer; this reading is rejected because Schrems II §96 held that procedural legality does not compensate for substantive deficiencies in the destination regime, and the EDPB Recommendations 01/2020 §B.1 make the essential-equivalence test binding for transfers to third countries whose domestic law permits extensive public-authority access. A second alternative reading focuses on the foreseeability of the third-country practice at the time of transfer rather than on the essential equivalence at the time of assessment; this reading is consistent with Schrems II §94 but operationally difficult because it requires the controller to predict regulatory drift in the destination jurisdiction. Remain open: (a) whether the Schrems II essential-equivalence test applies equally to processors and to controllers or whether a processor-tier standard may be lower given that the processor is itself bound by Art. 28; (b) whether supplementary measures (encryption, pseudonymisation, contractual minimisation) can rescue transfers to regimes where the public-authority access regime is materially deficient, or whether the Schrems II ruling forecloses supplementary measures in such cases.
```

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

