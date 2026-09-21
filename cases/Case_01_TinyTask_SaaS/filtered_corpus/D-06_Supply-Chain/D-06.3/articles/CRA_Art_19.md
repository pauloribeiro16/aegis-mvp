---
document_id: AEGIS-PREPROC-CRA-ART-19
title: CRA Art. 19 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 19
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 19

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-039 | An importer places a product with digital elements on the Union market only where the product has undergone the applicable conformity assessment, bears the CE marking, is accompanied by the required documentation, and identifies the manufacturer; the importer performs pre-market checks and — where the importer has reason to believe the product is not in conformity — informs the manufacturer and the market surveillance authority of significant risk and immediately takes corrective measures. | `CRA-CL87` (Art. 19(1) — importer only places compliant products); `CRA-CL88` (Art. 19(2) — importer pre-market checks: conformity assessment + CE + tech docs + contact info); `CRA-CL89` (Art. 19(3) — non-conformity); `CRA-CL90` (Art. 19(5) — importer corrective measures); `CRA-CL91` (Art. 19(6) — importer 10-year retention) | D-06.3, D-09.4 |
| SO-CRA-039 | D-06.3, D-09.4 | Art. 19(1)/(2)/(3)/(5)/(6) | Importer pre-market checks, non-conformity, corrective measures, retention |
| SO-CRA-057 | The manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer. | `CRA-CL38` (Art. 13(13) — 10-year documentation retention); `CRA-CL91` (Art. 19(6) — importer 10-year retention); `CRA-CL100` (Art. 23(2) — supply-chain 10-year retention) | D-09.4 |
| SO-CRA-057 | D-09.4 | Art. 13(13) + Art. 19(6) + Art. 23(2) | 10-year technical documentation + EU declaration retention |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-054
  title: "Importer pre-market documentary verification gate"
  source_clauses:
    - { clause_id: CRA-CL87, article_ref: "Art. 19(1) — importer only places compliant products" }
    - { clause_id: CRA-CL88, article_ref: "Art. 19(2) — importer pre-market checks" }
  linked_objectives: [SO-CRA-039]
  sub_domain: [D-06.3, D-09.4]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [IMPORTER]
  obligation_type: [TRIGGERED, CONTINUOUS]
  regulatory_rationale: |
    Article 19(1) requires the importer to place a product with digital elements on the Union market only where the product complies with the essential cybersecurity requirements set out in Annex I and the applicable conformity-assessment procedures have been carried out. Article 19(2) requires the importer — before placing the product on the market — to verify that: (a) the conformity-assessment procedure has been carried out; (b) technical documentation has been drawn up; (c) the CE marking has been affixed; (d) documentation identifying the manufacturer and contact details is provided with the product. The four pre-market checks position the importer as the EU-side gatekeeper for non-conforming products, mirroring the manufacturer's Article 13 obligations but at a documentary rather than technical level — the importer does not re-verify the product's technical conformity, only the conformity-assessment evidentiary record.
  security_rationale: |
    The Article 19(1)/(2) importer pre-market duty is operationalised in NIST CSF 2.0 through **GV.SC-02 (suppliers and other third parties known, prioritised, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.SC-02 captures the upstream-supplier-assessment dimension: the importer — being the entity closest to the EU border — treats the non-EU manufacturer as a supplier in the supply chain risk management process, applying the documentary-verification lens that operationalises the Article 19(2) check list. GV.SC-04 anchors the contractual-obligation-confirmation dimension: each of the four Article 19(2) checks (conformity-assessment procedure, technical documentation, CE marking, manufacturer identification) is a contractual-obligation confirmation point that the importer records as evidence of discharge. Together GV.SC-02 and GV.SC-04 enable the importer to demonstrate ex post, through documented supplier-assessment records and per-check confirmation logs, that the (1)/(2) pre-market duty has been discharged and that no non-conforming product has been placed on the Union market.
  ambiguity_notes: |
    `Only where` (Article 19(1)) is the necessary-condition reading: R1 (literal — no market placement without Annex I conformity). The four pre-market checks (Article 19(2)(a)–(d)) are coordinately enumerated — each is independently required before the product is placed on the market. The substantive threshold for `placed on the market` (Article 3(27)) is inherited and the importing activity is judged by reference to that definition. Remain open: (a) the operational demarcation between Article 19(1) importer duty and Article 21 manufacturer-equivalent trigger when the importer substantially modifies or re-brands the product — i.e. whether the importer retains the importer duty throughout or becomes the manufacturer under SR-CRA-061; (b) the documentary depth of `technical documentation` that the importer must verify — whether the Annex VII full bundle or a summary sufficient to confirm attestation.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-055
  title: "Importer non-conformity and vulnerability escalation pathway"
  source_clauses:
    - { clause_id: CRA-CL89, article_ref: "Art. 19(3) — importer non-conformity + MSA notification of significant risk" }
    - { clause_id: CRA-CL90, article_ref: "Art. 19(5) — importer corrective measures + inform manufacturer of vulnerability" }
  linked_objectives: [SO-CRA-039]
  sub_domain: [D-06.3, D-04.2]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents are contained" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [IMPORTER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 19(3) requires the importer — where they have reason to believe that a product is not in conformity with the essential cybersecurity requirements or with the procedural obligations — not to place the product on the market until conformity is restored, and to inform the manufacturer and the market surveillance authority of the significant risk. Article 19(5) requires the importer — if a vulnerability is identified in the product they have placed on the market — to inform the manufacturer and to take immediate corrective measures. The two paragraphs operate at different points of the product's market lifetime: Article 19(3) is pre-placement (or alternatively upon later discovery), and Article 19(5) is post-placement upon identified vulnerability. The escalation pathway to the manufacturer and the MSA closes the cross-border supply-chain loop without which a non-conforming product detected at import could remain on the market while the manufacturer remains unaware.
  security_rationale: |
    The Article 19(3)/(5) importer escalation duty is operationalised in NIST CSF 2.0 through **RS.MI-01 (incidents contained)** and **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)**. RS.MI-01 captures the containment dimension: where the importer has reason to believe a product is non-conforming, the product is held back from the market (or withdrawn if already placed) until conformity is restored — the corrective-measure set is the same as the manufacturer's Article 13(21), applied at the importer boundary. RS.CO-04 anchors the cross-border coordination function: the importer informs both the manufacturer and the MSA, closing the cross-border supply-chain loop without which a non-conforming product detected at import could remain on the market while the manufacturer remains unaware. Together RS.MI-01 and RS.CO-04 enable the importer to demonstrate ex post, through documented hold-and-withdraw records and notification logs, that the (3)/(5) escalation duty has been discharged and that the manufacturer-MSA coordination has been maintained.
  ambiguity_notes: |
    `Significant risk` carries VAG-S3 ambiguity (cf. CRA-D38 in the synthesis): R2 — qualitative judgment (importer's assessment of plausible non-conformity impact on users). R1 (risk-borne-out by incident) is rejected as too late to discharge the prevention duty; R3 (any non-conformity counts as significant risk) is rejected as over-broad. `Corrective measures` is POLY-S2 — R1 (the same set as Article 13(21) for the manufacturer: fix, withdraw, recall — applied at the importer boundary). The interplay with the manufacturer's Article 13(21) duty (SR-CRA-045) is residual: the importer takes the appropriate corrective measure within their power; the manufacturer remains responsible for the underlying conformity. Remain open: (a) the calibrated threshold for `significant risk` — i.e. whether harmonised criteria will be issued under Article 27 or Article 56 (MSA cooperation) that effectively constrain the importer's discretionary judgment; (b) the operational interaction with the manufacturer's Article 14 reporting where the importer-identified vulnerability materialises into an active-exploitation or severe-incident scenario.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-056
  title: "Importer 10-year retention of conformity documentation"
  source_clauses:
    - { clause_id: CRA-CL91, article_ref: "Art. 19(6) — importer 10-year retention" }
  linked_objectives: [SO-CRA-039, SO-CRA-057]
  sub_domain: [D-06.3, D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [IMPORTER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 19(6) requires the importer to keep a copy of the EU declaration of conformity and the technical documentation at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer. The retention obligation parallels the manufacturer's under Article 13(13) and ensures that the importer — as the closer-to-EU economic operator — remains the audit point after the manufacturer may have ceased operations. The Article 13(23) cessation-of-operations duty (SR-CRA-076) reinforces this by requiring the manufacturer to notify MSAs of impending cessation, enabling the importer (or designated responsible person) to assume retention responsibility.
  security_rationale: |
    The Article 19(6) importer retention duty is operationalised in NIST CSF 2.0 through **GV.OC-03 (legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — understood and managed)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. GV.OC-03 captures the compliance-evidence-retention dimension: the importer maintains a managed set of regulatory requirements, with the EU declaration of conformity and the technical documentation as the two operative artefacts retained for the 10-year-or-support-period tail. GV.SC-04 anchors the operational-handoff dimension: the importer, being the closer-to-EU economic operator, remains the audit point after the manufacturer may have ceased operations or become non-responsive, with the Article 13(23) cessation notification (SR-CRA-076) supplying the operational-handoff trigger. Together GV.OC-03 and GV.SC-04 enable the importer to demonstrate ex post, through the documented retention record and the operational-handoff evidence, that the (6) retention duty has been discharged and that the MSA audit point remains available across the retention tail.
  ambiguity_notes: |
    `10 years or support period, whichever is longer` carries VAG-S2 twin-anchor ambiguity: R2 — literal — the longer of the two periods applies. The `at the disposal of` qualifier expresses availability-on-demand rather than physical custody — the importer is not required to maintain originals; copies or controlled digital access suffice, providing the MSA can retrieve them within a reasonable window. Remain open: (a) whether the retention period for importers whose manufacturer has ceased operations (cf. Article 13(23)) is extended beyond the literal 10-year/support-period floor — i.e. whether designating a successor responsible person or transferring the documents to the MSA is required; (b) the operational handling of EU declaration of conformity updates during the support period when harmonised standards are revised — whether prior versions must be retained, or only the current version at the time of MSA request.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-084
  title: "Ten-year documentation retention for economic operators"
  source_clauses:
    - { clause_id: CRA-CL38, article_ref: "Art. 13(13) — 10-year documentation retention" }
    - { clause_id: CRA-CL91, article_ref: "Art. 19(6) — importer 10-year retention" }
    - { clause_id: CRA-CL100, article_ref: "Art. 23(2) — economic-operator 10-year retention" }
  linked_objectives: [SO-CRA-057]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER, IMPORTER, DISTRIBUTOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(13) requires the manufacturer to keep the technical
    documentation and the EU declaration of conformity at the disposal of
    the market-surveillance authorities for at least 10 years after the
    product has been placed on the market, or for the support period,
    whichever is longer. Article 19(6) applies the same retention duty to
    the importer — Art. 19(6) covers the EU declaration + technical
    documentation, anchored to the manufacturer's package. Article 23(2)
    applies a parallel 10-year retention to economic operators for
    supply-chain identification information (their suppliers and
    recipients).
  security_rationale: |
    The Art. 13(13)/19(6)/23(2) 10-year retention is operationalised in
    NIST CSF 2.0 through GV.OC-03 and GV.SC-04. GV.OC-03 anchors the
    legal-recordkeeping posture: the manufacturer, importer, and
    distributor each know which artefacts they must hold for the
    retention window and can produce them on a reasoned MSA request.
    GV.SC-04 (Suppliers and other third parties are routinely assessed
    using audits, test results, or other forms of evaluation to confirm
    they are meeting their contractual obligations) anchors the
    cross-economic-operator chain — the importer's and distributor's
    recordkeeping is treated as a third-party evidence base that the
    manufacturer can rely on for its own retention duty, and vice versa.
    Together, GV.OC-03 and GV.SC-04 give each economic operator a clear
    accountability line for the documents in their possession and let
    the chain as a whole demonstrate ex post that conformity evidence
    remained available across the full 10-year (or longer) window
    regardless of which entity ceased operations first.
  ambiguity_notes: |
    "Whichever is longer" resolves to the longer of the two periods (the
    10-year floor or the support period). "At the disposal of the market
    surveillance authorities" means available on request — not necessarily
    pre-submitted, but retrievable on a reasoned request. The Article
    19(6) importer retention covers the manufacturer's documentation
    chain; Article 23(2) covers the importer's own supply-chain
    identification record (different artefact, same 10-year floor).
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-113
  title: "ENISA-EU-CyCLONe large-scale incident hand-off"
  source_clauses:
    - { clause_id: CRA-CL78, article_ref: "Art. 17(1) — ENISA submits to EU-CyCLONe for large-scale incident management" }
  linked_objectives: [SO-CRA-073]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 17(1) provides that ENISA may submit notifications received
    via the single reporting platform to the EU-CyCLONe — the EU Cyber
    Crisis Liaison Network established under NIS 2 — for large-scale
    incident management. The submission is ENISA's discretion; the
    manufacturer has no direct submission authority to EU-CyCLONe
    [Recital 39].
  security_rationale: |
    The Art. 17(1) ENISA-to-EU-CyCLONe hand-off is operationalised in
    NIST CSF 2.0 through RS.CO-04. RS.CO-04 (Coordination with
    stakeholders occurs consistent with applicable rules and
    regulations) anchors the multi-institutional coordination posture:
    ENISA's hand-off to EU-CyCLONe follows the NIS 2 governance rules
    for large-scale incident management, with the manufacturer
    remaining a third-party recipient of the coordinated response. The
    single-Subcategory mapping reflects that the obligation is a
    coordination-procedure control, not a new technical surface.
    RS.CO-04 lets ENISA and the manufacturer both demonstrate ex post
    that the hand-off was triggered consistent with the NIS 2 Art. 19
    large-scale-incident criteria and routed through the appropriate
    cross-Member-State coordination channel.
  ambiguity_notes: |
    "May submit" reads as ENISA's discretion — the manufacturer cannot
    directly route a notification to EU-CyCLONe. "Large-scale incident
    management" reads in line with NIS 2 Article 19, which sets the
    EU-CyCLONe mandate and its scope; the boundary is drawn by the
    cross-border or cross-sector reach of the incident.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

