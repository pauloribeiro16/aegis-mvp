---
document_id: AEGIS-PREPROC-GDPR-ART-44
title: GDPR Art. 44 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 44
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

# GDPR Art. 44

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

