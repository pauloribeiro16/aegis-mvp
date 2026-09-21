---
document_id: AEGIS-PREPROC-CRA-ART-16
title: CRA Art. 16 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 16
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 16

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-012 | The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for its products with digital elements, and — once a security update has been made available — shares and publicly discloses information about fixed vulnerabilities, including description, affected-product identification, impacts, severity, and remediation guidance, subject to a duly-justified delay exception where security risks of publication outweigh security benefits. | `CRA-CL147` (Annex I Part II (5) — CVD policy); `CRA-CL146` (Annex I Part II (4) — public disclosure of fixed vulnerabilities); `CRA-CL75` (Art. 16(2) — CSIRT dissemination with delay grounds); `CRA-CL31` (Art. 13(8) sentence 5 — documentation of support period factors); `CRA-CL32` (Art. 13(8) sentence 6 — CVD policy) | D-02.3, D-09.1 |
| SO-CRA-012 | D-02.3, D-09.1 | Annex I Part II (4)/(5) + Art. 13(8) sentence 6 + Art. 16(2) | CVD policy + public disclosure with duly-justified delay exception |
| SO-CRA-023 | An actively exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified simultaneously to the CSIRT designated as coordinator of the Member State of the manufacturer's main establishment and to ENISA, via the single reporting platform established under Art. 16. | `CRA-CL51` (Art. 14(1) sentence 1 — AEV notification to CSIRT + ENISA); `CRA-CL52` (Art. 14(1) sentence 2 — single reporting platform); `CRA-CL64` (Art. 14(7) — main-establishment routing) | D-04.3, D-09.4 |
| SO-CRA-025 | A severe incident having an impact on the security of a product with digital elements that the manufacturer becomes aware of is notified simultaneously to the CSIRT designated as coordinator of the Member State of the manufacturer's main establishment and to ENISA, via the single reporting platform established under Art. 16. | `CRA-CL56` (Art. 14(3) sentence 1 — SI notification to CSIRT + ENISA); `CRA-CL57` (Art. 14(3) sentence 2 — single reporting platform); `CRA-CL64` (Art. 14(7) — main-establishment routing) | D-04.3 |
| SO-CRA-032 | Notifications received by a CSIRT designated as coordinator are disseminated via the single reporting platform to the CSIRTs designated as coordinators of the Member States in which the manufacturer has indicated the product has been made available; in exceptional circumstances, on cybersecurity-related grounds, dissemination may be delayed strictly as necessary (including where a vulnerability is subject to a coordinated vulnerability disclosure procedure). | `CRA-CL75` (Art. 16(2) — CSIRT dissemination + delay grounds); `CRA-CL74` (Art. 16(1) — ENISA single reporting platform); `CRA-CL76` (Art. 16(3) — market-surveillance sharing) | D-04.3 |
| SO-CRA-032 | D-04.3 | Art. 16(2)/(3) | CSIRT dissemination via single platform + delay grounds |
| SO-CRA-073 | ENISA establishes and maintains the single reporting platform via which the notifications of Arts. 14 and 15 are submitted, and takes appropriate and proportionate measures to secure the platform; the platform supports electronic notification end-points of CSIRTs designated as coordinators and ENISA, and is accessible simultaneously to ENISA when notification is submitted via a CSIRT end-point. | `CRA-CL74` (Art. 16(1) — ENISA single reporting platform); `CRA-CL77` (Art. 16(4) — platform security); `CRA-CL82` (Art. 17(5) — EU vulnerability database integration with NIS 2 Art. 12(2)); `CRA-CL78` (Art. 17(1) — EU-CyCLONe submission); `CRA-CL80` (Art. 17(3) — ENISA biennial report on cybersecurity risks) | D-09.4 |
| SO-CRA-073 | D-09.4 | Art. 16(1)/(4) + Art. 17(1)/(3)/(5) | ENISA single reporting platform security + EU-CyCLONe submission + biennial report |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-020
  title: "Public disclosure of fixed vulnerabilities with delay exception"
  source_clauses:
    - { clause_id: CRA-CL146, article_ref: "Annex I Part II (4) — public vulnerability disclosure with delay exception" }
    - { clause_id: CRA-CL75, article_ref: "Art. 16(2) — CSIRT dissemination with delay grounds" }
    - { clause_id: CRA-CL67, article_ref: "Art. 14(9) — delegated acts on delay grounds" }
  linked_objectives: [SO-CRA-012]
  sub_domain: [D-02.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (4) requires that once a security update has been made available, the manufacturer share and publicly disclose information about the fixed vulnerabilities, including a description of the vulnerability, the affected products, the impacts, the severity, and the remediation guidance — subject to a duly justified delay exception where the security risks of publication outweigh the security benefits. Art. 16(2) permits CSIRT dissemination to be delayed on the same grounds, with CVD-in-progress as the illustrative case. Art. 14(9) authorises the Commission to adopt delegated acts further specifying the delay grounds, so the criteria are anchored in the OJ with harmonised-standards support downstream. For a compliance officer the operational reading is: the disclosure happens; the delay, if any, must be documented with a per-decision justification that aligns with the Art. 14(9) categories.
  security_rationale: |
    The Annex I Part II (4) public-disclosure obligation is operationalised in NIST CSF 2.0 through **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)** and **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)**. RS.CO-03 captures the downstream-information-sharing leg: once a security update has been made available, information about the fixed vulnerabilities flows to designated stakeholders -- users, integrators, the broader security community -- consistent with the established information-sharing rules (the CVD policy under SR-CRA-019, the public-disclosure lever under Art. 17(2) where applicable, and the EU vulnerability database under Art. 17(5)). GV.SC-04 anchors the third-party-assessment dimension: the disclosure package itself is a contractual-equivalent artefact that downstream integrators and procurement authorities consume, and the per-decision justification for any delay operates as a documented assessment record consistent with the Annex I Part II (4) "duly justified" threshold. Together RS.CO-03 and GV.SC-04 enable the manufacturer to demonstrate ex post, through documented disclosure records, Art. 14(9) categories-based delay justifications, and EU vulnerability database population evidence, that the Annex I Part II (4) public-disclosure duty has been exercised within the CVD-respectful envelope the regulation intends.
  ambiguity_notes: |
    The phrase "duly justified cases, where manufacturers consider the security risks of publication to outweigh the security benefits" is VAG+SCOPE-Q S3 because the manufacturer is the sole judge of the balancing test, and no objective threshold is provided in the OJ text. Reading chosen: R2, treating CVD-in-progress per Art. 16(2) as the dominant illustrative example, with R1 (active exploitation) and R3 (national security grounds) following from the Art. 14(9) delegated-acts category set. Alternative reading: R4 (a vague "the risks are too high") is rejected as not a "duly justified" case because the word "duly" imports a documentary-evidence threshold that the manufacturer must meet. An additional reading, R5, would treat "duly justified" as requiring third-party validation (CSIRT or peer-manufacturer attestation) before the delay can be invoked, effectively institutionalising the balancing test rather than leaving it to manufacturer judgement; R5 is rejected because Annex I Part II (4) places the duty on the manufacturer and the harmonised-standards interpretation would have to operationalise validation — but R5 would be the natural next step if harmonised standards choose to specify it. Remain open: (a) does the manufacturer have to share the disclosure-after-delay basis with the CSIRT or keep it internal, and what audit trails apply; (b) how does the public-disclosure duty under Annex I Part II (4) interact with a coordinated disclosure timeline that the researcher agreed to, when the agreed window has lapsed but the patch is still in QA.
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
- sr_id: SR-CRA-031
  title: "Simultaneous severe-incident notification to CSIRT and ENISA"
  source_clauses:
    - { clause_id: CRA-CL56, article_ref: "Art. 14(3) sentence 1 — severe-incident notification to CSIRT + ENISA" }
    - { clause_id: CRA-CL64, article_ref: "Art. 14(7) — routing" }
    - { clause_id: CRA-CL57, article_ref: "Art. 14(3) sentence 2 — single platform" }
    - { clause_id: CRA-CL61, article_ref: "Art. 14(5)(a) — SI test A: CIA of sensitive/important" }
    - { clause_id: CRA-CL62, article_ref: "Art. 14(5)(b) — SI test B: malicious code" }
  linked_objectives: [SO-CRA-025, SO-CRA-027]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.AN-03, title: "Analysis is performed to establish what has occurred during an event and the root cause of the event" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(3) requires the manufacturer to notify any severe incident having an impact on the security of the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) and to ENISA, via the single reporting platform. Art. 14(5) defines severe incident through the disjunctive tests A and B: test A captures CIA impact on sensitive or important data or functions; test B captures the introduction or execution of malicious code in the product or in a user's NIS. The two tests are alternatives, so satisfying either one is sufficient to qualify as severe. For a compliance officer the rule frames the higher-severity reporting track of the Art. 14 dual-track architecture, with severity categorisation determining which chain to start.
  security_rationale: |
    The Art. 14(3) severe-incident notification obligation is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident management plan executed in coordination with relevant third parties once an incident is declared)** and **RS.AN-03 (analysis performed to establish what has occurred during an event and the root cause of the event)**. RS.MA-01 captures the third-party-coordination leg: once a severe incident is declared, the manufacturer executes its incident-management plan in concert with the CSIRT coordinator (the CSIRT of the Member State where the manufacturer has its main establishment), ENISA, and downstream market-surveillance authorities in other Member States -- the orchestrator-coordination role is the operative duty, and the single reporting platform under Art. 14(3) sentence 2 + Art. 16 is the instrument through which the coordination is delivered. RS.AN-03 anchors the impact-and-scope dimension: the Art. 14(5)(a)/(b) disjunctive tests require the manufacturer to estimate impact and scope across the four CIA dimensions (confidentiality, integrity, availability, authenticity) or across the malicious-code-introduction vector, with the Subcategory providing the analytical framework. Together RS.MA-01 and RS.AN-03 enable the manufacturer to demonstrate ex post, through single-platform submission timestamps, CSIRT acknowledgement records, incident-management plan execution evidence, and impact-estimation artefacts in the technical documentation under Annex VII, that the severe-incident notification has been delivered within the regulatory envelope and that ENISA's biennial synthesis pipeline receives severity-distinct inputs.
  ambiguity_notes: |
    The phrase "severe incident having an impact on the security of the product" is VAG+SCOPE-Q S2 (severity threshold inherited from Art. 14(5)) nested with VAG+POLY+COORD S3 (the disjunctive tests under Art. 14(5)(a) and (b)). Reading chosen: R3, applying the Art. 14(5)(a) and (b) literal disjunctive tests — either test triggers severity. The "simultaneously" qualifier inherits the SR-CRA-028 reading. The "becomes aware of" trigger inherits the SR-CRA-028 trigger ambiguity (CJEU IAB Baltic C-394/21 reasonable-certainty framing). An additional reading, R4-aggregated, would aggregate the Art. 14(5)(a) and (b) tests into a single composite trigger that requires both CIA impact AND malicious-code consequences to qualify as severe, raising the threshold substantially; R4 is rejected because the OJ literal "or" makes the tests disjunctive and the higher threshold would defeat the upstream Art. 14(3) duty to report on severe incidents as defined. Remain open: (a) does the "capable of affecting" gate in Art. 14(5)(a) require the manufacturer to forecast rather than observe, and where is the evidential threshold for the capability claim; (b) does the malicious-code test under Art. 14(5)(b) include legitimate but unauthorised code modifications (e.g., supply-chain backdoors not classified as malware) or strictly code with malicious intent.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-040
  title: "CSIRT cross-border incident dissemination via single platform"
  source_clauses:
    - { clause_id: CRA-CL75, article_ref: "Art. 16(2) — CSIRT dissemination + delay grounds" }
    - { clause_id: CRA-CL74, article_ref: "Art. 16(1) — ENISA single reporting platform" }
  linked_objectives: [SO-CRA-032]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 16(2) requires the CSIRT designated as coordinator that initially receives a notification under Article 14 to disseminate that notification — without delay — via the single reporting platform established under Article 16(1) to the CSIRTs designated as coordinators of the Member States in which the manufacturer has indicated that the product with digital elements has been made available on the market. The provision operationalises cross-border coordination: once a notification enters the platform in one Member State, it must reach the affected CSIRTs in every other Member State where the product is on the market, so that downstream market surveillance authorities (Article 52 et seq.) can begin their own activities. Article 16(2) qualifies that — in exceptional circumstances and on justified cybersecurity-related grounds — dissemination may be delayed for the strictly necessary period, expressly including situations where a vulnerability is subject to a coordinated vulnerability disclosure procedure under Article 12(1) of NIS 2 (Directive (EU) 2022/2555). This carve-out preserves CVD confidentiality during the active remediation window. The duty of timeliness flows jointly from Article 14(2) (the manufacturer's notification tiers) and Article 16(2) (the CSIRT's dissemination tier).
  security_rationale: |
    The Article 16(2) cross-border dissemination duty is operationalised in NIST CSF 2.0 through **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. RS.CO-04 captures the horizontal coordination function between CSIRTs across Member States — the single platform is the regulated coordination channel, and the receiving CSIRT must propagate the notification to destination CSIRTs in every market where the product is on the maker's own attestation, with timing aligned to the rules-of-the-platform. GV.SC-04 anchors the platform as a regulated supplier-of-service to MSAs: the platform's operating procedures and the cybersecurity-related delay carve-out are themselves auditable against documented platform rules, with the CVD-in-progress exception representing a contractual-equivalent relief mechanism. Together RS.CO-04 and GV.SC-04 enable the receiving CSIRT to demonstrate ex post, through platform-log records and dissemination timestamps, that the Article 16(2) duty has been discharged within the strictly-necessary period and that the cybersecurity-related delay grounds have been documented consistent with NIS 2 Article 12(1).
  ambiguity_notes: |
    `Justified cybersecurity-related grounds` carries VAG-S3 ambiguity — the phrase is Berry-classic vague with no OJ-literal definition. The illustration in Article 16(2) itself (CVD-in-progress under NIS 2 Article 12(1)) is operative: R2 (CVD-in-progress is the literal illustration but is illustrative — the grounds are not exhaustively enumerated). R1 (only CVD-in-progress) is rejected as over-narrow; R3 (any cybersecurity ground the CSIRT considers sufficient) is rejected as over-broad. The chosen reading is R2 supplemented by an analogue extrapolation to other in-confidence disclosure contexts (active exploitation where premature detail would aid the attacker, or coordinated patch-rollout windows). `Strictly necessary` is VAG-S2: R1 — minimum time required to address the cybersecurity ground. Remain open: (a) whether the platform operator (ENISA, per Article 16(1)) will issue procedural guidance limiting the categories of accepted cybersecurity grounds, in light of CSIRT heterogeneity across Member States; (b) whether the delay carve-out is asymmetric — i.e. whether the initially-receiving CSIRT's ground suffices, or whether all destination CSIRTs must concur — pending harmonised practice.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-112
  title: "ENISA single reporting platform with proportionate security"
  source_clauses:
    - { clause_id: CRA-CL74, article_ref: "Art. 16(1) — ENISA single reporting platform" }
    - { clause_id: CRA-CL77, article_ref: "Art. 16(4) — ENISA platform security measures" }
  linked_objectives: [SO-CRA-073]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: PR.IR-01, title: "Networks and environments are protected from unauthorized logical access and usage" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 16(1) requires ENISA to establish and maintain a single
    reporting platform for the notifications submitted under Articles
    14 and 15. Article 16(4) requires ENISA to take appropriate and
    proportionate measures to ensure the security of the platform
    itself [Recital 38, Recital 39].
  security_rationale: |
    The Art. 16(1)/(4) ENISA single reporting platform is operationalised
    in NIST CSF 2.0 through PR.IR-01 and GV.SC-04. PR.IR-01 (Networks
    and environments are protected from unauthorized logical access and
    usage) anchors the platform's network-and-environment security
    posture — the platform is exposed to manufacturers, CSIRTs, ENISA,
    and potentially MSAs, so the network layer must be hardened against
    unauthorised logical access. GV.SC-04 (Suppliers and other third
    parties are routinely assessed using audits, test results, or other
    forms of evaluation) anchors the third-party-assessable layer —
    ENISA's platform is itself an inter-institutional surface, and its
    security baseline is auditable. Together, PR.IR-01 and GV.SC-04
    give the platform a network-and-third-party-evaluation control set
    that lets the manufacturer and the CSA-EU rely on the platform's
    trustworthiness when transmitting Art. 14/15 notifications.
  ambiguity_notes: |
    "Appropriate and proportionate measures" reads as anchored in
    harmonised standards and ENISA's own risk assessment — the duty is
    calibrated, not maximalist. The substantive security baseline is
    the platform's threat model rather than an abstract ceiling.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-114
  title: "ENISA biennial report, EU vulnerability database, CSIRT helpdesk"
  source_clauses:
    - { clause_id: CRA-CL76, article_ref: "Art. 16(3) — CSIRT provides notification info to market-surveillance authorities" }
    - { clause_id: CRA-CL80, article_ref: "Art. 17(3) — ENISA biennial report on cybersecurity risks in products" }
    - { clause_id: CRA-CL82, article_ref: "Art. 17(5) — EU vulnerability database (writes back to NIS 2 Art. 12(2))" }
    - { clause_id: CRA-CL83, article_ref: "Art. 17(6) — CSIRT helpdesk for manufacturers on reporting obligations" }
  linked_objectives: [SO-CRA-073, SO-CRA-074]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 16(3) provides that CSIRTs designated as coordinators shall
    provide notification information to the relevant market-surveillance
    authorities. Article 17(3) requires ENISA to prepare a biennial
    report on cybersecurity risks in products with digital elements.
    Article 17(5) requires ENISA to add publicly known vulnerabilities
    to the EU vulnerability database established under NIS 2 Article
    12(2). Article 17(6) requires CSIRTs designated as coordinators to
    provide helpdesk support to manufacturers on the reporting
    obligations under Articles 14 and 15 [Recital 38, Recital 39].
  security_rationale: |
    The Art. 16(3)/17(3)/(5)/(6) ENISA-CSIRT coordination cluster is
    operationalised in NIST CSF 2.0 through RS.CO-04 and ID.IM-04.
    RS.CO-04 (Coordination with stakeholders occurs consistent with
    applicable rules and regulations) anchors the multi-institutional
    coordination posture — CSIRTs pass notification information to
    MSAs (Art. 16(3)) and ENISA populates the EU vulnerability database
    (Art. 17(5)). ID.IM-04 (Cybersecurity risk management improvements
    are informed by awareness of related developments and context)
    anchors the improvement-loop input that the biennial report
    (Art. 17(3)) and the vulnerability database provide — the
    manufacturer's risk-assessment refresh can cite ENISA's outputs
    as evidence of current threat context. Together, RS.CO-04 and
    ID.IM-04 give the cluster a coordination-and-improvement control
    set that lets the manufacturer consume ENISA outputs in its own
    Art. 13(2) risk picture and demonstrate ex post that those outputs
    were considered.
  ambiguity_notes: |
    "Biennial" reads literally as every two years. "Publicly known
    vulnerabilities" reads as already publicly disclosed vulnerabilities
    — the database is curation rather than original publication; the
    threshold is ENISA's curated-vs-undisclosed judgement. The
    helpdesk support is a guidance channel rather than a binding
    interpretation service: written ENISA guidance and the formal
    Regulation text remain the controlling sources.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

