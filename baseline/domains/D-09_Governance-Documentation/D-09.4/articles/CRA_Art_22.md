---
document_id: AEGIS-PREPROC-CRA-ART-22
title: CRA Art. 22 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 22
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 22

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-043 | A natural or legal person, other than the manufacturer, importer, or distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market is considered to be the manufacturer for the purposes of the Regulation, with obligations attaching to the affected part or — where the substantial modification has an impact on the cybersecurity of the product as a whole — to the entire product. | `CRA-CL97` (Art. 22(1) — third-party substantial modification = manufacturer); `CRA-CL98` (Art. 22(2) — scope of obligations) | D-06.4, D-07.4 |
| SO-CRA-043 | D-06.4, D-07.4 | Art. 22(1)/(2) | Third-party substantial modification = manufacturer (part or whole) |
| SO-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations. | `CRA-CL39` (Art. 13(14) — series-of-production conformity); `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL97` (Art. 22(1) — third-party substantial modification = manufacturer); `CRA-CL30` (Art. 3(30) — substantial modification definition); `CRA-CL34` (Art. 13(10) — substantial modification compliance for the last-placed version) | D-07.4, D-06.4 |
| SO-CRA-047 | D-07.4, D-06.4 | Art. 13(14) + Art. 21 + Art. 22(1) + Art. 3(30) + Art. 13(10) | Series-production conformity + substantial-modification consequences |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-045
  title: "Non-conformity corrective measures, withdrawal, or recall"
  source_clauses:
    - { clause_id: CRA-CL46, article_ref: "Art. 13(21) — corrective measures on non-conformity" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification (cross-ref for trigger)" }
  linked_objectives: [SO-CRA-063]
  sub_domain: [D-04.2, D-07.4, D-09.4]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(21) requires manufacturers — from the placing on the market of the product and for the support period — who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the Annex I cybersecurity requirements to immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product, as appropriate. The text expressly covers both product-side and process-side non-conformity, recognising that a product can be Annex-I-conformant on its own merits even where the manufacturer's vulnerability-handling processes are deficient, and vice versa. The `know or have reason to believe` trigger mirrors the Article 14(1) awareness trigger language (cf. SR-CRA-039) — the same constructive-knowledge debate applies. The `or withdraw or recall` formulation gives the manufacturer the choice of remedy, but the choice is governed by the proportionality principle articulated across the Regulation.
  security_rationale: |
    The Article 13(21) non-conformity corrective-measures duty is operationalised in NIST CSF 2.0 through **RS.MI-01 (incidents contained)**, **RS.MI-02 (incidents mitigated)**, and **GV.OV-02 (organisational cybersecurity risk management strategy reviewed and adjusted to address changes in the risk landscape)**. RS.MI-01 captures the immediate-containment response: once non-conformity is known, the manufacturer isolates the affected product or process from further exposure, applying the corrective measure that brings the product or process back to conformity or removes it from the market. RS.MI-02 captures the mitigation dimension: the corrective measure is applied, and the residual risk is brought within acceptable bounds — fix, withdraw, or recall as appropriate, with the proportionality principle setting the choice. GV.OV-02 closes the strategic loop: the manufacturer's risk-management strategy is reviewed and adjusted against the change in circumstances that triggered the non-conformity, ensuring the same root cause does not recur. Together RS.MI-01, RS.MI-02, and GV.OV-02 enable the manufacturer to demonstrate ex post, through documented containment records, mitigation evidence, and strategy-review minutes, that the Article 13(21) duty has been discharged and that the proportionality of the chosen remedy (fix vs. withdraw vs. recall) is evidentially supported.
  ambiguity_notes: |
    `Immediately take the corrective measures necessary` is VAG+POLY-S2 — R1 (`immediately` = upon knowledge of non-conformity, in line with Article 14 awareness trigger; `corrective measures necessary` = the minimum set needed to restore conformity). `Withdraw or recall` is POLY-S2 — R1 (literal OR — either is admissible; the choice is the manufacturer's, governed by proportionality). The cross-reference to Article 3(30) substantial modification is significant: if the corrective measure requires a substantial modification, the Art. 22(1) third-party-modifier trigger may engage as well, transferring liability downstream. Remain open: (a) what regulatory practice crystallises around `have reason to believe` — i.e. whether constructive knowledge attaches upon receipt of an upstream-CVD report from a component supplier (per Article 13(6) in SR-CRA-051) or only upon internal verification of the non-conformity; (b) whether withdrawal versus recall is itself a proportionality determination that must be evidenced ex ante in the technical documentation under Annex VII.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-062
  title: "Third-party substantial modification triggers manufacturer status"
  source_clauses:
    - { clause_id: CRA-CL97, article_ref: "Art. 22(1) — third-party substantial modification = manufacturer" }
    - { clause_id: CRA-CL98, article_ref: "Art. 22(2) — scope of obligations (affected part or whole)" }
  linked_objectives: [SO-CRA-043, SO-CRA-047]
  sub_domain: [D-06.4, D-07.4]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 22(1) provides that a natural or legal person, other than the manufacturer, importer, or distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market shall be considered to be the manufacturer for the purposes of this Regulation. Article 22(2) provides that the obligations apply to the affected part of the product or — where the substantial modification has an impact on the cybersecurity of the product as a whole — to the entire product. The provision closes a critical loophole: an integrator or third-party modifier who is not in the supply chain contract (and thus not classified as importer or distributor under Article 19 / 20) cannot escape manufacturer obligations by literal definitional exclusion.
  security_rationale: |
    The Article 22 third-party-modifier trigger is operationalised in NIST CSF 2.0 through **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.SC-02 captures the supply-chain-classification dimension: a third-party modifier who is not in the importer/distributor supply chain is nevertheless classified into the supply-chain risk management process once the substantial-modification trigger fires, with the supply-chain assessment supplying the documentation that the modifier has become a manufacturer for the purposes of the Regulation. GV.SC-04 anchors the contractual-and-procedural-test dimension: the Article 22(2) scope determination (affected part vs. whole product) is a documented assessment that the modifier records in the operational record, with the per-scope obligation set discharged accordingly. Together GV.SC-02 and GV.SC-04 enable the third-party modifier to demonstrate ex post, through documented substantial-modification assessments and per-scope obligation records, that the Article 22 trigger has been correctly applied and that the manufacturer-equivalent status has been assumed for the affected part or the whole product as appropriate.
  ambiguity_notes: |
    `Other than the manufacturer, importer, or distributor` is POLY-S2: R3 (any person not already classified — third-party integrators, system integrators, vertical-specific modifiers, OEM reconfigurers). `Carries out a substantial modification` is POLY-VAG-S2: R1 (performs — literal; cf. SR-CRA-061 for the Article 3(30) substantial-modification substance). `For the part … OR for the entire product` (Article 22(2)) is COORD-S2: R1 (literal OR — scope depends on impact per Article 22(2) literal; the modifier becomes a manufacturer for the affected part or for the entire product depending on cybersecurity impact). Remain open: (a) the operational assessment of `impact on the cybersecurity of the product as a whole` — whether harmonised standards will provide a methodology or whether it remains a case-by-case modifier-side assessment; (b) the interplay between Article 22(1) and the original manufacturer's parallel liability — i.e. whether the third-party modifier fully assumes manufacturer obligations or whether the original manufacturer remains partially liable.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-070
  title: "Substantial-modification compliance scope across supply chain"
  source_clauses:
    - { clause_id: CRA-CL34, article_ref: "Art. 13(10) — substantial-modification compliance scope" }
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger" }
    - { clause_id: CRA-CL97, article_ref: "Art. 22(1) — third-party substantial modification" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification definition" }
  linked_objectives: [SO-CRA-047, SO-CRA-060]
  sub_domain: [D-07.4, D-06.4]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    The Articles 13(10), 21, and 22 architecture treats substantial modification as the trigger for manufacturer-equivalent status, with the Article 13(10) carve-out allowing compliance with Annex I Part II (2) for the last-placed version of the product where the user-migration conditions are met (i.e. the user is given the choice to migrate to the modified product or to retain the last-placed version). Article 21 (SR-CRA-061) addresses the importer/distributor trigger; Article 22 (SR-CRA-062) addresses the third-party modifier trigger; Article 13(10) provides the manufacturer's own substantial-modification compliance scope.
  security_rationale: |
    The Article 13(10) + 21 + 22 substantial-modification architecture is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. PR.PS-02 captures the version-management dimension: the substantial-modification threshold is the boundary between normal-version-update and manufacturer-equivalent liability transfer, and PR.PS-02 supplies the risk-commensurate maintenance discipline that distinguishes the two. GV.SC-04 anchors the supply-chain-coordination dimension: the importer, distributor, and third-party modifier assessments (Articles 21, 22) are operationalised through the supply-chain contractual-and-procedural tests that determine when the manufacturer-equivalent status fires. Together PR.PS-02 and GV.SC-04 enable the manufacturer, importer, distributor, or third-party modifier to demonstrate ex post, through documented version-management records and supply-chain assessment evidence, that the substantial-modification boundary has been correctly applied and that the manufacturer-equivalent status has been appropriately assumed or retained.
  ambiguity_notes: |
    `Substantial modification` inherits Article 3(30) D30 — VAG+POLY+COORD-S3. See SR-CRA-061/R-CRA-015 for the full reading across this threshold. R1 (any non-compliance change) + R3 (intended-purpose modification) admitted as the disjunctive literal reading. The Article 13(10) carve-out — allowing Annex I Part II (2) compliance for the last-placed version subject to user-migration — is POLY-S2 — R1 (the carve-out is conditional on user choice; the manufacturer cannot unilaterally apply it). Remain open: (a) the operational demarcation between security updates (which rarely meet the substantial-modification threshold) and security features whose modification would meet the substantial-modification threshold — pending harmonised practice; (b) whether the substantial-modification test must be re-run at every release (formal), or only at material risk-relevant changes (substantive) — the BERs harmonised standards under Article 27 will likely converge on the latter.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

