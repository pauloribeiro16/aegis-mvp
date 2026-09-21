---
document_id: AEGIS-PREPROC-CRA-ART-17
title: CRA Art. 17 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 17
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
status: DRAFT
---

# CRA Art. 17

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-030 | Any natural or legal person may voluntarily notify vulnerabilities or incidents (including near misses) of products with digital elements to the CSIRT designated as coordinator or to ENISA, and a CSIRT initially receiving a notification that does not originate from the manufacturer informs the manufacturer; the mere act of notification does not subject the notifying natural or legal person to increased liability. | `CRA-CL69` (Art. 15(1) — voluntary AEV reporting); `CRA-CL70` (Art. 15(2) — voluntary SI / near-miss reporting); `CRA-CL72` (Art. 15(4) — third-party notification + CSIRT-informs-manufacturer); `CRA-CL81` (Art. 17(4) — liability shield) | D-04.3, D-09.4 |
| SO-CRA-030 | D-04.3, D-09.4 | Art. 15(1)/(2)/(4) + Art. 17(4) | Voluntary vulnerability/incident/near-miss reporting + liability shield |
| SO-CRA-033 | Public awareness necessary to prevent or mitigate a severe incident, or where disclosure is otherwise in the public interest, may be served by the CSIRT designated as coordinator (after consulting the manufacturer concerned and, where appropriate, in cooperation with ENISA) informing the public about the incident or requiring the manufacturer to do so. | `CRA-CL79` (Art. 17(2) — public disclosure option) | D-04.3, D-09.1 |
| SO-CRA-033 | D-04.3, D-09.1 | Art. 17(2) | Public disclosure option by CSIRT |
| SO-CRA-073 | ENISA establishes and maintains the single reporting platform via which the notifications of Arts. 14 and 15 are submitted, and takes appropriate and proportionate measures to secure the platform; the platform supports electronic notification end-points of CSIRTs designated as coordinators and ENISA, and is accessible simultaneously to ENISA when notification is submitted via a CSIRT end-point. | `CRA-CL74` (Art. 16(1) — ENISA single reporting platform); `CRA-CL77` (Art. 16(4) — platform security); `CRA-CL82` (Art. 17(5) — EU vulnerability database integration with NIS 2 Art. 12(2)); `CRA-CL78` (Art. 17(1) — EU-CyCLONe submission); `CRA-CL80` (Art. 17(3) — ENISA biennial report on cybersecurity risks) | D-09.4 |
| SO-CRA-073 | D-09.4 | Art. 16(1)/(4) + Art. 17(1)/(3)/(5) | ENISA single reporting platform security + EU-CyCLONe submission + biennial report |
| SO-CRA-074 | ENISA prepares a biennial report on cybersecurity risks in products with digital elements and maintains the EU vulnerability database (Art. 12(2) NIS 2); CSIRTs designated as coordinators provide helpdesk support to manufacturers on the reporting obligations. | `CRA-CL80` (Art. 17(3) — ENISA biennial report); `CRA-CL82` (Art. 17(5) — EU vulnerability database — writes back to NIS 2 Art. 12(2)); `CRA-CL83` (Art. 17(6) — CSIRT helpdesk for manufacturers) | D-09.4 |
| SO-CRA-074 | D-09.4 | Art. 17(3)/(5)/(6) | ENISA biennial report + EU vuln DB + CSIRT helpdesk |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-019
  title: "Coordinated vulnerability disclosure policy publication"
  source_clauses:
    - { clause_id: CRA-CL147, article_ref: "Annex I Part II (5) — CVD policy" }
    - { clause_id: CRA-CL32, article_ref: "Art. 13(8) sentence 6 — CVD policy" }
    - { clause_id: CRA-CL103, article_ref: "Art. 24(3) — OSS steward Art. 14 extension cross-ref to CVD" }
  linked_objectives: [SO-CRA-012, SO-CRA-049]
  sub_domain: [D-02.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (5) requires manufacturers to put in place and enforce a policy on coordinated vulnerability disclosure. Art. 13(8) sentence 6 lists the CVD policy among the appropriate policies a manufacturer shall have, integrating it with the wider support-period duty. OSS-steward policies under Art. 24(1) include CVD aspects per Art. 24(3), which extends the same architecture to stewards of open-source projects in scope. For a compliance officer this means a published, enforceable CVD policy that names intake channels, triage SLAs, disclosure expectations, and post-disclosure verification — typically aligned with ISO 29147 / ISO 30111 conventions or with sector-specific variants.
  security_rationale: |
    The Annex I Part II (5) + Art. 13(8) sentence 6 CVD policy obligation is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.SC-04 (suppliers and other third parties routinely assessed using audits, test results, or other forms of evaluation to confirm contractual obligations are met)**. GV.PO-01 captures the published-and-enforced dimension: the CVD policy is a documented organisational cybersecurity policy that is communicated to researchers, integrators, and downstream operators, and the enforcement leg is what differentiates a real CVD programme from a static disclosure page. GV.SC-04 anchors the third-party-interaction leg: researcher interactions are a third-party channel that benefits from contractual clarity, and the CVD architecture (intake to triage to publication to verification) is the assessment pathway that confirms researcher-side expectations are met consistently with manufacturer-side commitments. Together GV.PO-01 and GV.SC-04 enable the manufacturer to demonstrate ex post, through a documented CVD policy, intake-channel evidence, triage-log records, and post-disclosure verification artefacts, that the Annex I Part II (5) policy-on-CVD duty has been put in place and enforced across the support period and that the policy meets the upstream enablement needs of the SR-CRA-021 contact-address and SR-CRA-020 public-disclosure rules.
  ambiguity_notes: |
    The phrase "policy on coordinated vulnerability disclosure" is POLY-S2 because three materially distinct policy architectures are admissible. Reading chosen: R3, a structured receive + triage + publish + post-disclosure verification pipeline, anchored in the implementing acts under Art. 14(9) and in Art. 17(5) EU vulnerability database integration. Alternative readings: R1 (ISO 29147 + ISO 30111-style structured policy, which is admissible) is a non-strict equivalent to R3; R2 (lighter disclosure-statement policy) is rejected because it fails the "enforce" element by omitting the triage and verification phases. The downstream contact-address expectation is developed separately in SR-CRA-021.
```

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
- sr_id: SR-CRA-038
  title: "Voluntary third-party vulnerability reporting with CSIRT bridge"
  source_clauses:
    - { clause_id: CRA-CL69, article_ref: "Art. 15(1) — voluntary AEV reporting by any person" }
    - { clause_id: CRA-CL70, article_ref: "Art. 15(2) — voluntary SI / near-miss reporting by any person" }
    - { clause_id: CRA-CL72, article_ref: "Art. 15(4) — third-party notification + CSIRT informs manufacturer" }
    - { clause_id: CRA-CL81, article_ref: "Art. 17(4) — no increased liability for mere notification" }
  linked_objectives: [SO-CRA-030]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 15(1) and Art. 15(2) allow any natural or legal person to voluntarily notify vulnerabilities or incidents (including near misses) to the CSIRT designated as coordinator or to ENISA. Art. 15(4) requires that, where a third party notifies the CSIRT of an AEV or severe incident, the CSIRT informs the manufacturer concerned, closing the loop. Art. 17(4) provides that the mere act of notification does not subject the notifying natural or legal person to increased liability — a structural shield against chilling effects. For a compliance officer the rule sets up the regulator-side intake from non-manufacturer parties (researchers, integrators, users) and the CSIRT-side bridge back to the manufacturer.
  security_rationale: |
    The Art. 15 voluntary-reporting architecture is operationalised in NIST CSF 2.0 through **RS.CO-03 (information shared with designated internal and external stakeholders consistent with established information-sharing rules)** and **GV.SC-01 (a cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders)**. RS.CO-03 captures the upstream-input leg: any natural or legal person -- researchers, integrators, users, journalists -- may voluntarily notify vulnerabilities or incidents (including near misses) to the CSIRT designated as coordinator or to ENISA, and the Subcategory's voluntary-shared-rules framework supplies the interpretive context for what counts as "voluntary" under Art. 15. GV.SC-01 anchors the supply-chain-risk-management-program dimension: the manufacturer-side mirror of the reporting architecture must integrate the third-party intake under Art. 15(4) (CSIRT informs manufacturer concerned) and the Art. 17(4) liability shield into the supply-chain risk-management programme so that downstream vulnerability research is not chilled by disclosure-risk concerns. Together RS.CO-03 and GV.SC-01 enable the manufacturer and the wider reporting ecosystem to demonstrate ex post, through documented third-party-intake records, CSIRT-bridge evidence under Art. 15(4), and supply-chain risk-management programme records, that the voluntary-reporting architecture has remained viable and that the liability-shield under Art. 17(4) has been honoured as a structural feature of the policy regime.
  ambiguity_notes: |
    The phrase "any natural or legal person" is SCOPE-Q S2 with R1 (anyone who has information, including researchers, journalists, concerned users) as the literal reading. The phrase "near miss" inherits the Art. 3(45) definition, which in turn imports from NIS 2 Art. 6(5) — POLY+S2 with R1 (event that could have caused harm), R2 (event that caused no harm), and R3 (partial-success event) as the three admissible readings; the Annex level reading does not pick one and lets the harmonised-standards layer modulate.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-041
  title: "CSIRT public-disclosure option and EU vulnerability database population"
  source_clauses:
    - { clause_id: CRA-CL79, article_ref: "Art. 17(2) — public disclosure option by CSIRT" }
    - { clause_id: CRA-CL82, article_ref: "Art. 17(5) — EU vulnerability database" }
  linked_objectives: [SO-CRA-033]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 17(2) provides that where public awareness is necessary to prevent or mitigate a severe incident, or to handle an ongoing incident, or where disclosure is otherwise in the public interest, the CSIRT designated as coordinator of the relevant Member State may — after consulting the manufacturer and, where appropriate, in cooperation with ENISA — inform the public about the incident or require the manufacturer to do so. Article 17(5) requires ENISA — after consulting the manufacturer and the relevant CSIRT — to add publicly-known vulnerabilities to the EU vulnerability database established under Article 12(2) of NIS 2. The two provisions together articulate the public-disclosure lever of the reporting architecture: Article 17(2) is the real-time disclosure tool for severe or ongoing incidents, while Article 17(5) is the durable, queryable record that downstream defenders, integrators, and procurement authorities consult when assessing product cyber posture.
  security_rationale: |
    The Article 17(2)/(5) public-disclosure architecture is operationalised in NIST CSF 2.0 through **RS.CO-03 (information shared with designated internal and external stakeholders consistent with established information-sharing rules)** and **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)**. RS.CO-03 captures the public-side coordination function: once the CSIRT determines that public awareness is necessary to prevent or mitigate harm, the manufacturer (and ENISA where appropriate) shares the incident information externally with users, integrators, and the wider public, with the consultation step preserving the manufacturer's right to be heard before disclosure. GV.SC-04 anchors the EU vulnerability database (Article 17(5) read with NIS 2 Article 12(2)) as a regulated-information repository whose population procedure is itself auditable against documented platform rules — the durable, queryable record that downstream defenders, integrators, and procurement authorities consult when assessing product cyber posture. Together RS.CO-03 and GV.SC-04 enable the CSIRT and ENISA to demonstrate ex post, through consultation logs and database-population records, that the public-disclosure lever has been applied proportionately and that the manufacturer's right to be heard has been preserved.
  ambiguity_notes: |
    `Where public awareness is necessary` carries VAG-S2 ambiguity — the threshold is qualitative judgment by the CSIRT, anchored in the prevention or mitigation purpose. R1 (necessary per CSIRT assessment, after consulting the manufacturer — the literal procedural frame) is the chosen reading. `In cooperation with ENISA` is POLY-S2 — the practical division is that the CSIRT leads the disclosure decision and ENISA's role is supportive (cross-border coordination, language coverage, EU-level framing); the chosen reading is R1 (CSIRT-led with ENISA in a cooperative support capacity). Remain open: (a) whether ENISA's database population will be near-real-time or batched, and whether CSIRTs retain discretion to delay population beyond the manufacturer's consultation horizon; (b) whether the public-disclosure lever will be used sparingly (preserving manufacturer primacy) or as a routine backstop, and how Recital 50's proportionality framing will be operationalised in practice.
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

