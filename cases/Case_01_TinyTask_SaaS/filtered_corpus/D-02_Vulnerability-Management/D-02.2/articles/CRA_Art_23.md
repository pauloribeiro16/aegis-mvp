---
document_id: AEGIS-PREPROC-CRA-ART-23
title: CRA Art. 23 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 23
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 23

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-044 | Economic operators provide supplier and recipient identification information to market surveillance authorities on request, and retain supply-chain information for 10 years. | `CRA-CL99` (Art. 23(1) — identification duty); `CRA-CL100` (Art. 23(2) — 10-year retention) | D-06.4, D-09.4 |
| SO-CRA-044 | D-06.4, D-09.4 | Art. 23(1)/(2) | Economic-operator identification + 10-year supply-chain retention |
| SO-CRA-057 | The manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer. | `CRA-CL38` (Art. 13(13) — 10-year documentation retention); `CRA-CL91` (Art. 19(6) — importer 10-year retention); `CRA-CL100` (Art. 23(2) — supply-chain 10-year retention) | D-09.4 |
| SO-CRA-057 | D-09.4 | Art. 13(13) + Art. 19(6) + Art. 23(2) | 10-year technical documentation + EU declaration retention |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-010
  title: "Vulnerability remediation without delay after awareness"
  source_clauses:
    - { clause_id: CRA-CL144, article_ref: "Annex I Part II (2) — address and remediate without delay" }
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — vulnerabilities addressed through security updates" }
    - { clause_id: CRA-CL24, article_ref: "Art. 13(6) sentence 1 — component vulnerability address + remediate" }
  linked_objectives: [SO-CRA-008]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (2) requires manufacturers to address and remediate vulnerabilities without delay in relation to the risks posed to the product, including by providing security updates; the clause further specifies that, where technically feasible, security updates shall be provided separately from functionality updates. Annex I Part I (2)(c) carries the same address-via-updates duty into the part I properties and pairs it with user-facing update notification. Art. 13(6) sentence 1 applies the address-and-remediate duty to component vulnerabilities identified in integrated third-party components, so the obligation is not evaded by externalising components. For a compliance officer the operational reading is: a vulnerability, once identified, triggers a documented timeline running from awareness to remediation and to user-dissemination (the latter covered in SR-CRA-017), with the technical-feasibility carve-out logged in the conformity dossier.
  security_rationale: |
    The Annex I Part II (2) "address and remediate without delay" duty is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **ID.RA-06 (risk responses chosen, prioritised, planned, tracked, and communicated)**. PR.PS-02 captures the maintenance and replacement leg: software is maintained (patched, mitigated, or where necessary replaced) commensurate with the risk that the vulnerability poses, and the address-and-remediate timeline is a sub-stream of the broader software-maintenance lifecycle. ID.RA-06 anchors the response-management dimension: risk responses are chosen (patch versus mitigation), prioritised (by severity and exploit availability), planned (with milestone evidence), tracked (with progress records), and communicated (upstream to the SBOM owners, downstream to users under SR-CRA-017). Together PR.PS-02 and ID.RA-06 enable the manufacturer to demonstrate ex post, through documented remediation timelines, technical-feasibility carve-out records in the conformity dossier under Annex VII, and addressed-component evidence under Art. 13(6), that the "without delay" anchor has been exercised continuously from the awareness moment through to user-dissemination, and that the Art. 13(2) risk-assessment prioritisation remains in force as the pipeline progresses.
  ambiguity_notes: |
    The phrase "without delay" is VAG-S3 in the Berry-classic sense, structurally identical to "without undue delay" in GDPR Art. 33 and NIS 2 Art. 23(4)(a). Reading chosen: R1, where remediation action commences immediately on awareness and the ceiling is determined by the duration of the technical remediation pipeline, with record-keeping and advisory messages to users accompanying each remediation step. Alternative readings: R2 (delay permitted up to a calendar ceiling of N days regardless of pipeline duration) would risk creating a licence to delay beneath the headline obligation; R3 (subjective manufacturer discretion) is rejected as failing the inquiry-resistant test. An additional reading, R4, would characterise "without delay" as beginning at the moment of developer handoff rather than the moment of awareness, shifting the clock upstream to internal triage; R4 is rejected because the OJ text anchors the trigger at the manufacturer's knowledge rather than at developer assignment, but the operational consequence is identical where the manufacturer's process is tightly coupled. The COORD-S2 "address and remediate" conjunction is treated literally as both required, with "address" denoting the acknowledgement, triage, and communication step and "remediate" denoting the patch or mitigation. Remain open: (a) does the awareness clock pause while the manufacturer awaits confirmation from the reporter (CVD step), or does it run continuously from initial receipt; (b) when remediation requires changes that exceed a single release cycle (schema migration, dependency removal), does the literal "without delay" require partial mitigations to be deployed in the interim.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-028
  title: "Simultaneous AEV notification to CSIRT and ENISA"
  source_clauses:
    - { clause_id: CRA-CL51, article_ref: "Art. 14(1) sentence 1 — AEV notification to CSIRT + ENISA" }
    - { clause_id: CRA-CL64, article_ref: "Art. 14(7) — routing through CSIRT of MS of main establishment" }
    - { clause_id: CRA-CL52, article_ref: "Art. 14(1) sentence 2 — single reporting platform" }
    - { clause_id: CRA-CL44, article_ref: "Art. 3(44) — incident definition (imported from Art. 6(6) NIS 2 + CRA add-on)" }
    - { clause_id: CRA-CL42, article_ref: "Art. 3(42) — actively exploited vulnerability" }
  linked_objectives: [SO-CRA-023]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(1) requires a manufacturer to notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) — the CSIRT of the Member State where the manufacturer has its main establishment in the Union — and to ENISA, via the single reporting platform established under Art. 16. Art. 3(44) imports the incident definition from NIS 2 Art. 6(6) with a CRA add-on, and Art. 3(42) defines actively exploited vulnerability. For a compliance officer the operational reading is: an AEV, once known, triggers a same-timestamp dual-channel notification routed through the single platform to the correct CSIRT and ENISA.
  security_rationale: |
    The Art. 14(1) AEV notification obligation is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident management plan executed in coordination with relevant third parties once an incident is declared)** and **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)**. RS.MA-01 captures the third-party-coordination leg: once an AEV is identified and declared, the manufacturer executes its incident-management plan in concert with the CSIRT coordinator (the CSIRT of the Member State where the manufacturer has its main establishment), ENISA, and downstream market-surveillance authorities in other Member States -- the orchestrator-coordination role is the operative duty, and the single reporting platform under Art. 14(1) sentence 2 + Art. 16 is the instrument through which the coordination is delivered. RS.CO-04 anchors the rule-consistent coordination dimension: the simultaneity requirement (Art. 14(1) sentence 1) prevents asymmetric early disclosure where one authority hears first and the other hears later, leaving an information window that adversaries can exploit, and the Subcategory anchors the cross-Member-State coordination in documented platform-mediated records. Together RS.MA-01 and RS.CO-04 enable the manufacturer to demonstrate ex post, through single-platform submission timestamps, dual-channel acknowledgement records, and incident-management plan execution evidence in the technical documentation under Annex VII, that the Art. 14(1) AEV notification has been delivered within the regulatory envelope and that ENISA's biennial synthesis pipeline receives consistent input.
  ambiguity_notes: |
    The phrase "simultaneously" is VAG-S3 because temporal precision is left to interpretation. Reading chosen: R1, treating "simultaneously" as same-timestamp on the single platform under Art. 16, because the platform enforces simultaneity architecturally. R2 (same day) and R3 (short window) are rejected as failing the simultaneity requirement. The "becomes aware of" trigger inherits the GDPR Art. 33 / NIS 2 Art. 23 ambiguity (cf. CJEU IAB Baltic C-394/21 on reasonable certainty of harm), with R1 (actual knowledge) literal and R2 (constructive knowledge through due diligence) admissible. The "actively exploited vulnerability" definition under Art. 3(42) admits R3/R4 (publicly available exploit / researcher-published PoC) as the dominant readings. An additional reading, R3-as-window, would treat "simultaneously" as occurring within a tightly bounded time window (a few hours) rather than at the literal same timestamp, accommodating the practical realities of single-platform queueing; R3-as-window is rejected because the single platform architecture under Art. 16 enforces same-timestamp submission architecturally, making the literal reading the operational reality. Remain open: (a) does a published PoC alone (without observed exploitation) qualify as an AEV, or does the manufacturer require evidence of exploitation in the wild; (b) does constructive knowledge extend to threats described in confidential channels (vendor-to-vendor vulnerability programmes) that the manufacturer has not joined.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-063
  title: "Economic-operator supply-chain identification and 10-year retention"
  source_clauses:
    - { clause_id: CRA-CL99, article_ref: "Art. 23(1) — economic operator identification duty" }
    - { clause_id: CRA-CL100, article_ref: "Art. 23(2) — 10-year retention of supply-chain information" }
  linked_objectives: [SO-CRA-044]
  sub_domain: [D-06.4, D-09.4]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER, AUTHORISED_REPRESENTATIVE, IMPORTER, DISTRIBUTOR]
  obligation_type: [TRIGGERED, CONTINUOUS]
  regulatory_rationale: |
    Article 23(1) requires economic operators, on reasoned request from a market surveillance authority, to identify: (a) any economic operator that has supplied them with a product; and (b) any economic operator to whom they have supplied a product. Article 23(2) requires economic operators to retain this supply-chain information for 10 years after they have been supplied with the product or after they have supplied the product. The two paragraphs operate in tandem — identification is request-triggered; retention is the durational anchor that ensures identification is operationally possible 10 years later. The duty applies to all economic operators in the chain — manufacturer, AR, importer, distributor — preserving a complete upstream-and-downstream audit trail.
  security_rationale: |
    The Article 23 supply-chain identification and retention duty is operationalised in NIST CSF 2.0 through **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)** and **GV.OC-03 (legal, regulatory, and contractual requirements regarding cybersecurity understood and managed)**. GV.SC-04 captures the third-party-assessment dimension: each economic operator maintains a record of upstream suppliers and downstream customers, with the assessment-of-contractual-obligations lens applied at each economic-operator transition. GV.OC-03 anchors the legal-and-regulatory-requirements dimension: the 10-year retention obligation is a managed regulatory requirement, with the upstream-and-downstream identification being a request-triggered (not continuous) duty that the economic operator discharges on demand. Together GV.SC-04 and GV.OC-03 enable the economic operator to demonstrate ex post, through the documented supply-chain record and the on-demand identification response, that the (1)/(2) duty has been discharged and that the upstream-and-downstream audit trail remains available across the 10-year tail.
  ambiguity_notes: |
    `On reasoned request` is VAG-S2: R1 (request with specific operational cause — i.e. a request tied to a market-surveillance activity, not a fishing expedition). `10 years` is a hard anchor with no operative ambiguity. The bilateral identification duty (both upstream — `any economic operator that has supplied them` — and downstream — `any economic operator to whom they have supplied`) is literal and unambiguous. No S3 directly. Remain open: (a) the format and granularity of the retained information — whether harmonised standards under Article 27 will specify minimum data fields (transaction date, quantity, batch/serial number, contact details) that operationalise the duty; (b) the operational interface with the manufacturer's Article 13(23) cessation notification (SR-CRA-076) — i.e. whether the cessation-bound manufacturer must transfer the supply-chain records to the next-in-line economic operator or to the MSA.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

