---
document_id: AEGIS-PREPROC-CRA-ART-18
title: CRA Art. 18 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 18
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 18

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-041 | A manufacturer established outside the Union may appoint an authorised representative established in the Union by written mandate to perform specified tasks on behalf of the manufacturer; the manufacturer's obligations under Art. 13(1)–(11), Art. 13(12) first subparagraph, and Art. 13(14) are not delegable to the authorised representative, who retains the technical documentation and cooperates with market surveillance authorities. | `CRA-CL84` (Art. 18(1) — AR appointment); `CRA-CL85` (Art. 18(2) — AR carve-out of non-delegable obligations); `CRA-CL86` (Art. 18(3) — AR tasks); `CRA-CL13` (Art. 3(13) — manufacturer definition) | D-06.4, D-09.4 |
| SO-CRA-041 | D-06.4, D-09.4 | Art. 18(1)/(2)/(3) + Art. 3(13) | Authorised representative appointment + non-delegable obligations |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-059
  title: "Authorised representative appointment with non-delegable carve-out"
  source_clauses:
    - { clause_id: CRA-CL84, article_ref: "Art. 18(1) — AR appointment" }
    - { clause_id: CRA-CL85, article_ref: "Art. 18(2) — AR carve-out of non-delegable obligations" }
  linked_objectives: [SO-CRA-041]
  sub_domain: [D-06.4]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan" }
  applies_to_role: [AUTHORISED_REPRESENTATIVE]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 18(1) provides that a manufacturer established outside the Union may, by written mandate, appoint an authorised representative established in the Union to perform specified tasks on the manufacturer's behalf. Article 18(2) provides that the authorised representative's mandate does not cover the manufacturer's obligations under Article 13(1)–(11) (the design / development / production / risk-assessment / documentation / conformity-assessment cluster), under Article 13(12) first subparagraph (CE marking + EU declaration of conformity), and under Article 13(14) (series-production conformity). The carve-out preserves the manufacturer's primary responsibility for product-design and conformity-assessment activities, while allowing the AR to handle procedural cooperation with market-surveillance authorities (Article 18(3) tasks, treated in SR-CRA-060).
  security_rationale: |
    The Article 18(1)/(2) AR mechanism is operationalised in NIST CSF 2.0 through **GV.RR-02 (roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management established, communicated, understood, and enforced)** and **GV.SC-03 (contracts with suppliers and other third parties used to implement appropriate measures designed to meet the objectives of an organisation's cybersecurity programme and SCRM plan)**. GV.RR-02 anchors the role-and-accountability architecture: the AR is established as a documented role within the manufacturer's governance structure, with the Article 18(2) carve-out making explicit which obligations are non-delegable and which fall within the AR's mandate — the role-and-accountability clarity is the substantive content of the carve-out. GV.SC-03 captures the contractual-coordination layer: the written mandate under Article 18(1) is the contractual instrument that defines the AR's scope of authority, with the contractual mechanism serving as the auditable record of role allocation. Together GV.RR-02 and GV.SC-03 enable the manufacturer and the AR to demonstrate ex post, through documented role-and-accountability records and the written-mandate record, that the (1)/(2) AR architecture has been correctly established and that the non-delegable obligations remain with the manufacturer.
  ambiguity_notes: |
    `By written mandate` is POLY-S2: R1 (a formal written mandate in writing — literal). The Article 3(15) `specified tasks` reading, inherited here, is POLY-S2 — R1 (the tasks enumerated in Article 18(3), bounded by the Article 18(2) carve-out; anything outside the carve-out is non-delegable). The carve-out's reach is the operative point: Article 13(12) first subparagraph includes the CE marking and the EU declaration of conformity under the manufacturer; Article 13(14) includes series-production conformity. Remain open: (a) whether joint AR appointments — multiple ARs per non-EU manufacturer, or shared AR pools — are permissible under Article 18; (b) the operational status of an AR's mandate termination when the manufacturer is acquired by an EU-established entity or establishes a Union subsidiary — whether the AR mandate lapses automatically or requires formal revocation.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-060
  title: "Authorised representative EU-side compliance tasks"
  source_clauses:
    - { clause_id: CRA-CL86, article_ref: "Art. 18(3) — AR tasks" }
  linked_objectives: [SO-CRA-041]
  sub_domain: [D-06.4, D-09.4]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [AUTHORISED_REPRESENTATIVE]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 18(3) provides that the authorised representative performs the tasks specified in the mandate — including: (a) keeping the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for the retention period; (b) providing the authorities with all information and documentation necessary to demonstrate conformity; (c) cooperating with the authorities on action taken to address non-conformity. The three tasks are operationally bounded by the Article 18(2) carve-out (see SR-CRA-059): the AR holds the technical documentation, but does not draw it up; the AR provides information, but the manufacturer authorises the conformity attestation; the AR cooperates on action, but does not unilaterally issue corrective measures.
  security_rationale: |
    The Article 18(3) AR tasks duty is operationalised in NIST CSF 2.0 through **GV.SC-03 (contracts with suppliers and other third parties used to implement appropriate measures)** and **GV.OC-03 (legal, regulatory, and contractual requirements regarding cybersecurity understood and managed)**. GV.SC-03 captures the AR's procedural-cooperation function: the three Article 18(3) tasks (technical-documentation custody, information provision, MSA cooperation on non-conformity action) are operationalised through the contractual mandate under Article 18(1), with the AR acting as the EU-side compliance anchor for non-EU manufacturers. GV.OC-03 anchors the legal-and-regulatory-requirements-managed dimension: the AR maintains a managed set of CRA-imposed regulatory requirements (retention period, MSA-cooperation triggers, conformity-demonstration protocol), with the retention period cross-referencing the manufacturer's obligation under Article 13(13) / Annex VII §4. Together GV.SC-03 and GV.OC-03 enable the AR to demonstrate ex post, through documented technical-documentation custody records and MSA-cooperation logs, that the (3) tasks duty has been discharged and that the AR provides the operational interface that allows MSA recourse against non-EU manufacturers.
  ambiguity_notes: |
    `Tasks specified in the mandate` is POLY-S2 — R1 (the tasks enumerated in the OJ-literal Article 18(3) list, bounded by Article 18(2)). No S3 directly. The retention period in Article 18(3)(a) cross-references the manufacturer's retention obligation under Article 13(13) / Annex VII §4. Remain open: (a) the operational handling of multilingual documentation in the EU technical-dossier — whether the AR must hold translations, or whether the manufacturer's English-language originals suffice; (b) the demarcation between the AR's cooperation duty and the manufacturer's parallel cooperation duty under Article 14 (incident reporting) and Article 13(23) (cessation of operations).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

