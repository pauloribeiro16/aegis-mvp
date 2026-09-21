---
document_id: AEGIS-PREPROC-CRA-ART-21
title: CRA Art. 21 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 21
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 21

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-042 | An importer or distributor who places a product with digital elements on the market under its own name or trademark, or who carries out a substantial modification of a product with digital elements already placed on the market, is considered to be the manufacturer for the purposes of the Regulation and assumes the manufacturer's obligations under Arts. 13 and 14. | `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL30` (Art. 3(30) — substantial modification definition) | D-06.4, D-07.4 |
| SO-CRA-042 | D-06.4, D-07.4 | Art. 21 + Art. 3(30) | Manufacturer-equivalent trigger (own name/trademark or substantial mod) |
| SO-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations. | `CRA-CL39` (Art. 13(14) — series-of-production conformity); `CRA-CL96` (Art. 21 — manufacturer-equivalent trigger); `CRA-CL97` (Art. 22(1) — third-party substantial modification = manufacturer); `CRA-CL30` (Art. 3(30) — substantial modification definition); `CRA-CL34` (Art. 13(10) — substantial modification compliance for the last-placed version) | D-07.4, D-06.4 |
| SO-CRA-047 | D-07.4, D-06.4 | Art. 13(14) + Art. 21 + Art. 22(1) + Art. 3(30) + Art. 13(10) | Series-production conformity + substantial-modification consequences |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-018
  title: "Automatic security updates with user opt-out capability"
  source_clauses:
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — automatic security updates + opt-out + postponement" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8(e) — how the automatic-update default setting can be turned off" }
  linked_objectives: [SO-CRA-019, SO-CRA-009]
  sub_domain: [D-03.4, D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(c) requires vulnerabilities to be addressed through security updates, including — where applicable — through automatic security updates installed within an appropriate timeframe enabled as a default setting, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them. Annex II §8(e) obliges the manufacturer to inform the user how the automatic-update default can be turned off, lifting the user's path from implication (the setting exists) to discoverability (the setting is documented). For a compliance officer the operational consequence is: auto-update on by default, opt-out discoverable and single-click, postponement available, and Annex II §8(e) disclosure present in the user-facing materials.
  security_rationale: |
    The Annex I Part I (2)(c) + Annex II section 8(e) auto-update-default and opt-out architecture is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-management dimension: the auto-update default is itself a configuration baseline that must be established, documented (in the technical documentation and the Annex II section 8(e) user-facing materials), and applied consistently across deployed instances -- the secure-by-default principle operationalised at the update channel level. PR.DS-12 captures the data-management side: the auto-update mechanism exists to preserve data CIA over time, and the opt-out and postponement options are risk-modulated choices that allow enterprise users and regulated industries to operate within controlled update windows without sacrificing the baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented default configurations, configuration-change audit trails, and Annex II section 8(e) user-information records, that the auto-update default has been implemented consistent with Annex I Part I (2)(c) and that the user-autonomy safeguards (opt-out, postponement) have been preserved.
  ambiguity_notes: |
    The phrase "within an appropriate timeframe" in Annex I Part I (2)(c) is VAG-S3 in the Berry-classic "appropriate" sense (cf. GDPR Art. 32, NIS 2 Art. 21). Reading chosen: R2, anchoring the timeframe to the severity of the addressed vulnerability and the user's operational environment, modulated by the Art. 13(2) risk assessment. Alternative readings: R1 (a single quantitative ceiling for all vulnerabilities) is rejected because severity modulation is the operative sanity check; R3 (manufacturer discretion) is rejected as failing the inquiry-resistant test. The "clear and easy-to-use" qualifier is VAG-S2 with R1 (UI discoverable + single-click) as the literal reading, anchored in harmonised standards and Art. 7(4) Commission implementing acts. An additional reading, R5, would tie the timeframe to harmonised-standards baselines that specify a category-specific deployment window (industrial control, medical device, consumer IoT); R5 is admitted as the long-run consensus direction but is rejected for current OJ reading because Annex I Part I (2)(c) leaves the timeframe to the manufacturer's risk assessment, pending Art. 7(4) implementing acts that may specify defaults. Remain open: (a) does the opt-out obligation require that disabling auto-update also disable any active update channel that could silently re-enable, or merely that the toggle be respected once flipped; (b) when updates are bundled (security + functionality), must Annex I Part II (2)'s "where technically feasible" separation route the entire bundle through opt-in for the functionality part.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-061
  title: "Manufacturer-equivalent status on own-name placement or substantial modification"
  source_clauses:
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger (own name/trademark or substantial modification)" }
    - { clause_id: CRA-CL30, article_ref: "Art. 3(30) — substantial modification" }
  linked_objectives: [SO-CRA-042, SO-CRA-047]
  sub_domain: [D-06.4, D-07.4]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 21 provides that an importer or distributor shall be considered to be a manufacturer for the purposes of this Regulation — and shall be subject to the obligations of Articles 13 and 14 — where that importer or distributor places a product with digital elements on the market under its own name or trademark, or carries out a substantial modification of a product with digital elements already placed on the market. The provision is the accountability transfer at the supply-chain boundary: re-branding or substantially modifying a product makes the economic operator the manufacturer, regardless of their underlying supply relationship. Article 3(30) — cross-referenced — defines `substantial modification` as a modification occurring after the product has been placed on the market, where the manufacturer has not considered it in the conformity assessment, and which affects the compliance of the product with the essential cybersecurity requirements set out in Annex I or which modifies the intended purpose of the product.
  security_rationale: |
    The Article 21 manufacturer-equivalent trigger is operationalised in NIST CSF 2.0 through **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.SC-02 captures the supplier-prioritisation dimension: an importer or distributor that re-brands or substantially modifies a product transitions from being a downstream economic operator to being the manufacturer of record, and the supply chain risk management process re-categorises the entity accordingly. GV.SC-04 anchors the contractual-obligation-confirmation layer: the trigger condition (own-name placement OR substantial modification) is itself a contractual-and-procedural test that the importer/distributor documents in the operational record, with the Article 3(30) substantial-modification test supplying the operative criterion. Together GV.SC-02 and GV.SC-04 enable the importer or distributor to demonstrate ex post, through documented re-branding-decision records and substantial-modification assessments, that the Article 21 trigger has been correctly applied and that the accountability transfer has been executed where the trigger fires.
  ambiguity_notes: |
    `Under its name or trademark` carries VAG+POLY-S3: R3 (either — white-label, co-brand, or repackaged under a distinct trademark). R1 (strictly under one's own trademark) is rejected as narrower than the literal; R2 (only when both name and trademark diverge) is rejected as cumulatively restrictive. `Substantial modification` inherits Article 3(30) D30 — VAG+POLY+COORD-S3 (cf. SR-CRA-061/R-CRA-015 for the full reading). Reading chosen for this SR: R1 + R3 (Article 3(30) disjunctive `affects compliance OR modifies intended purpose` — literal). The interaction with Article 22 (SR-CRA-062) is significant: where the modifier is neither manufacturer nor importer nor distributor, Article 22 applies the manufacturer-equivalent status to that other person — closing a critical loophole. Remain open: (a) the operational demarcation between `intended-purpose modification` (Article 3(30) limb b) and intended-purpose-preserving configuration changes — i.e. whether adding optional features that do not affect Annex I compliance is `substantial`; (b) whether the harmonised standards under Article 27 will specify a baseline technical-modification catalogue for the most common product categories.
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

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-090
  title: "Support-period end-date disclosed to users"
  source_clauses:
    - { clause_id: CRA-CL44, article_ref: "Art. 13(19) — support-period end-date display" }
    - { clause_id: CRA-CL157, article_ref: "Annex II §7 — support-period type + end-date in user info" }
    - { clause_id: CRA-CL61, article_ref: "Art. 21 — manufacturer-equivalent inherits obligation" }
  linked_objectives: [SO-CRA-061]
  sub_domain: [D-09.4, D-05.2]
  nist_csf_mapping:
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(19) requires the manufacturer to ensure that the end date
    of the support period — including at least the month and year — is
    clearly and understandably specified at the time of purchase; the
    manufacturer shall also inform users when the support-period end-date
    approaches. Annex II §7 carries the type of technical security support
    and the end-date into the user-facing information that accompanies the
    product. Article 21 makes any actor that takes on the manufacturer
    role (under its name/trademark or through substantial modification)
    inherit the same end-date display obligation.
  security_rationale: |
    The Art. 13(19)/Annex II §7 support-period end-date disclosure is
    operationalised in NIST CSF 2.0 through GV.OC-04 and GV.PO-01.
    GV.OC-04 (Critical objectives, capabilities, and services that
    stakeholders depend on or expect from the organization are
    understood and communicated) anchors the support-period end-date as
    a critical, expected-to-be-communicated element of the
    manufacturer's stakeholder interface. GV.PO-01 (Organizational
    cybersecurity policy is established, communicated, and enforced)
    anchors the manufacturer-equivalent inheritance (Art. 21) — the
    policy that determines who assumes the display obligation when
    ownership of the product changes hands. Together, GV.OC-04 and
    GV.PO-01 give the manufacturer a communication-and-policy control
    set that the manufacturer (or its Art. 21 successor) can
    demonstrate ex post kept the end-date visible from the time of
    purchase through the approach-and-arrival window.
  ambiguity_notes: |
    "Clearly and understandably" reads as a UI-discoverability,
    plain-language expectation — anchored in the harmonised-standards
    specifications for product marking and in the Article 13(11)
    archives-discoverability baseline.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-092
  title: "Corrective measures, withdrawal, or recall on non-conformity"
  source_clauses:
    - { clause_id: CRA-CL46, article_ref: "Art. 13(21) — corrective measures on non-conformity + withdrawal + recall" }
    - { clause_id: CRA-CL96, article_ref: "Art. 21 — manufacturer-equivalent trigger (cross-ref)" }
  linked_objectives: [SO-CRA-063]
  sub_domain: [D-09.4, D-04.2, D-07.4]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.MI-02, title: "Incidents are mitigated" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 13(21) requires the manufacturer — from the placing on the
    market and for the duration of the support period — who knows or has
    reason to believe that the product or its processes are not in
    conformity with the Annex I cybersecurity requirements to immediately
    take the corrective measures necessary to bring the product or
    processes into conformity, or to withdraw or recall the product, as
    appropriate. Article 21 makes Article 13(21) inheritable by
    manufacturer-equivalents (importer or distributor placing under own
    name, or substantial modifier) [Recital 33].
  security_rationale: |
    The Art. 13(21)/Art. 21 corrective-measures duty is operationalised
    in NIST CSF 2.0 through RS.MI-01, RS.MI-02, and GV.OV-02. RS.MI-01
    (Incidents are contained) and RS.MI-02 (Incidents are mitigated)
    anchor the immediate response: a non-conformity discovered (or
    constructively known) is contained and mitigated, with the
    withdrawal-or-recall option available where mitigation cannot
    restore conformity. GV.OV-02 (The organizational cybersecurity risk
    management strategy is reviewed and adjusted to address changes in
    the organization's risk landscape) anchors the post-response
    re-baselining — the manufacturer updates the risk picture that
    failed to prevent the non-conformity. Together, RS.MI-01, RS.MI-02,
    and GV.OV-02 give the manufacturer a three-stage control set
    (contain, mitigate, re-baseline) that the manufacturer (or its
    Art. 21 successor) can demonstrate ex post was triggered on each
    "knows or has reason to believe" event.
  ambiguity_notes: |
    "Immediately take the corrective measures necessary" reads as
    action upon knowledge (or constructive knowledge) of non-conformity;
    "necessary" measures are the minimum set to restore conformity
    rather than a maximalist clean-sheet re-engineering. Recital 33
    frames the "immediately" bound by what is technically and
    organisationally feasible, not by what is commercially convenient.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

