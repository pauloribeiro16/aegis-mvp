---
document_id: AEGIS-PREPROC-CRA-ART-14
title: CRA Art. 14 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 14
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.2.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.2.md
status: DRAFT
---

# CRA Art. 14

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-023 | An actively exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified simultaneously to the CSIRT designated as coordinator of the Member State of the manufacturer's main establishment and to ENISA, via the single reporting platform established under Art. 16. | `CRA-CL51` (Art. 14(1) sentence 1 — AEV notification to CSIRT + ENISA); `CRA-CL52` (Art. 14(1) sentence 2 — single reporting platform); `CRA-CL64` (Art. 14(7) — main-establishment routing) | D-04.3, D-09.4 |
| SO-CRA-023 | D-04.3, D-09.4 | Art. 14(1) + (7) | AEV notification simultaneously to CSIRT + ENISA |
| SO-CRA-024 | The Art. 14(1) AEV notification follows a three-tier temporal pattern — an early warning within 24 hours of the manufacturer becoming aware, a vulnerability notification within 72 hours, and a final report within 14 days of a corrective or mitigating measure being available — each reporting tier providing progressively richer content about the affected product, the vulnerability, and the corrective or mitigating measures available to users. | `CRA-CL53` (Art. 14(2)(a) — 24h early warning); `CRA-CL54` (Art. 14(2)(b) — 72h vulnerability notification); `CRA-CL55` (Art. 14(2)(c) — 14-day final report) | D-04.3, D-09.4 |
| SO-CRA-024 | D-04.3, D-09.4 | Art. 14(2)(a)/(b)/(c) | AEV notification 24h/72h/14d three-tier pattern |
| SO-CRA-025 | A severe incident having an impact on the security of a product with digital elements that the manufacturer becomes aware of is notified simultaneously to the CSIRT designated as coordinator of the Member State of the manufacturer's main establishment and to ENISA, via the single reporting platform established under Art. 16. | `CRA-CL56` (Art. 14(3) sentence 1 — SI notification to CSIRT + ENISA); `CRA-CL57` (Art. 14(3) sentence 2 — single reporting platform); `CRA-CL64` (Art. 14(7) — main-establishment routing) | D-04.3 |
| SO-CRA-025 | D-04.3 | Art. 14(3) + (7) | Severe-incident notification to CSIRT + ENISA |
| SO-CRA-026 | The Art. 14(3) severe-incident notification follows a three-tier temporal pattern — an early warning within 24 hours of the manufacturer becoming aware, an incident notification within 72 hours, and a final report within one month of the submission of the 72-hour incident notification — each tier providing progressively richer content including severity, root-cause type, and ongoing mitigation measures. | `CRA-CL58` (Art. 14(4)(a) — 24h early warning (SI)); `CRA-CL59` (Art. 14(4)(b) — 72h incident notification); `CRA-CL60` (Art. 14(4)(c) — 1-month final report (SI)) | D-04.3 |
| SO-CRA-026 | D-04.3 | Art. 14(4)(a)/(b)/(c) | Severe-incident notification 24h/72h/1m three-tier pattern |
| SO-CRA-027 | An incident having an impact on the security of a product with digital elements is considered severe where it negatively affects (or is capable of negatively affecting) the ability of the product to protect the availability, authenticity, integrity, or confidentiality of sensitive or important data or functions; OR where it has led (or is capable of leading) to the introduction or execution of malicious code in the product or in the network and information systems of a user of the product. | `CRA-CL61` (Art. 14(5)(a) — SI test A: CIA of sensitive/important data/functions); `CRA-CL62` (Art. 14(5)(b) — SI test B: malicious code); `CRA-CL44` (Art. 3(44) — incident definition) | D-04.3 |
| SO-CRA-027 | D-04.3 | Art. 14(5)(a)/(b) | Severe-incident definition: CIA of sensitive/important OR malicious code |
| SO-CRA-028 | After becoming aware of an actively exploited vulnerability or a severe incident, the manufacturer informs the impacted users — and where appropriate all users — of the vulnerability or incident and of any risk-mitigation and corrective measures that the users can deploy, where appropriate in a structured, machine-readable and easily-automatically-processable format; where the manufacturer fails to inform users in a timely manner, the CSIRTs designated as coordinators may provide such information. | `CRA-CL65` (Art. 14(8) sentence 1 — user notification + machine-readable format); `CRA-CL66` (Art. 14(8) sentence 2 — CSIRT fallback) | D-04.3, D-09.4 |
| SO-CRA-028 | D-04.3, D-09.4 | Art. 14(8) | User notification + machine-readable format + CSIRT fallback |
| SO-CRA-029 | Upon CSIRT request, the manufacturer provides an intermediate report on relevant status updates about the actively exploited vulnerability or severe incident. | `CRA-CL63` (Art. 14(6) — intermediate report on CSIRT request) | D-04.3 |
| SO-CRA-029 | D-04.3 | Art. 14(6) | Intermediate report on CSIRT request |
| SO-CRA-031 | An open-source software steward shall — to the extent the steward is involved in the development of the products with digital elements — notify actively exploited vulnerabilities of such products to the CSIRT designated as coordinator and to ENISA via the single reporting platform; and — to the extent severe incidents affect network and information systems provided by the steward for the development of such products — apply the severe-incident and user-notification obligations of Art. 14(3)/(8). | `CRA-CL103` (Art. 24(3) — OSS steward Art. 14(1)/(3)/(8) extension); `CRA-CL44` (Art. 3(44) — incident definition) | D-04.3, D-09.1 |
| SO-CRA-031 | D-04.3, D-09.1 | Art. 24(3) | OSS steward Art. 14 notification extension (with involvement threshold) |
| SO-CRA-067 | The Commission may adopt implementing acts specifying the format and elements of the software bill of materials referred to in Annex I Part II (1); ADCO may conduct a Union-wide dependency assessment on the Union's dependence on software components (in particular FOSS components) for specific categories of products with digital elements. | `CRA-CL49` (Art. 13(24) — SBOM implementing acts); `CRA-CL50` (Art. 13(25) — Union-wide dependency assessment by ADCO); `CRA-CL67` (Art. 14(9) — delegated acts on delay-dissemination grounds); `CRA-CL68` (Art. 14(10) — implementing acts on notification format/procedures); `CRA-CL8` (Art. 7(3) — delegated acts amending Annex III); `CRA-CL9` (Art. 7(4) — implementing acts specifying technical descriptions); `CRA-CL119` (Art. 30(6) — implementing acts on labels/pictograms) | D-09.4 |
| SO-CRA-067 | D-09.4 | Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6) | Commission implementing / delegated acts (SBOM, delay grounds, labels, technical descriptions) |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-005
  title: "Data integrity protection and corruption reporting"
  source_clauses:
    - { clause_id: CRA-CL135, article_ref: "Annex I Part I (2)(f) — integrity + report on corruptions" }
    - { clause_id: CRA-CL141, article_ref: "Annex I Part I (2)(l) — logging + monitoring" }
  linked_objectives: [SO-CRA-005]
  sub_domain: [D-01.4, D-10.2]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.DS-10, title: "The confidentiality, integrity, and availability of data-in-use are protected" }
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(f) requires the manufacturer to protect the integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, against any manipulation or modification not authorised by the user; the clause additionally obliges the manufacturer to report on corruptions, transforming silent-tampering failures into observable events. Annex I Part I (2)(l) carries the same data into a recording and monitoring duty, so that any integrity event has a corresponding audit-trail record (further developed in SR-CRA-027). The two clauses together map to NIST CSF PR.DS-01 (data-at-rest integrity), PR.DS-10 (data-in-use integrity), and PR.PS-04 (log records made available for continuous monitoring).
  security_rationale: |
    The Annex I Part I (2)(f)+(l) integrity duty is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest CIA protected)**, **PR.DS-10 (data-in-use CIA protected)**, and **PR.PS-04 (log records generated and made available for continuous monitoring and analysis)**. PR.DS-01 captures the data-at-rest integrity leg: cryptographic hashes, MACs, and integrity-checked storage ensure that an adversary cannot silently tamper with stored data, commands, programs, or configuration without invalidating the integrity check on the next read. PR.DS-10 anchors the data-in-use leg -- runtime integrity controls such as signed firmware, control-flow integrity, and tamper-detection instrumentation -- covering the firmware implants, command injection, configuration drift, and supply-chain backdoors that have dominated real-world incident data. PR.PS-04 closes the detection loop by ensuring that the integrity events become observable log records suitable for continuous monitoring, so that the "report on corruptions" obligation transforms silent tampering into observable events rather than silent failures. Together PR.DS-01, PR.DS-10, and PR.PS-04 enable the manufacturer to demonstrate ex post, through documented integrity-check evidence, log-records in the technical documentation under Annex VII sections 2/6, and corruption-report records to users, that the Annex I (2)(f)+(l) integrity duty -- including the universal-quantifier "any manipulation or modification not authorised by the user" -- has been met across the support period under Art. 13(8).
  ambiguity_notes: |
    The compound "data, personal or other, commands, programs and configuration" is COORD-S2 — a four-element list with nested OR/AND — and admits materially distinct protection scopes; Reading chosen: R1, treating the conjunction as inclusive of all four classes, in line with the OJ-literal listing. The "report on corruptions" phrase is VAG-S2; Reading chosen: R1, where the report goes to the device user or administering party in a manner proportionate to severity, rather than to an external authority (the integrity-breach case differs from the actively-exploited-vulnerability case under Art. 14). The phrase "any manipulation or modification not authorised by the user" is POLY-S2 with the "any" universal-quantifier meaning, and the literal reading is preserved — integrity protection is unconditional.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-007
  title: "Vulnerability and component identification with SBOM"
  source_clauses:
    - { clause_id: CRA-CL143, article_ref: "Annex I Part II (1) — identify and document vulnerabilities and components + SBOM" }
    - { clause_id: CRA-CL26, article_ref: "Art. 13(7) — systematically document relevant cybersecurity aspects" }
    - { clause_id: CRA-CL18, article_ref: "Art. 13(3) sentence 1 — risk assessment documented and updated" }
  linked_objectives: [SO-CRA-006, SO-CRA-007]
  sub_domain: [D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.AM-02, title: "Inventories of software, services, and systems managed by the organization are maintained" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (1) requires manufacturers of products with digital elements to identify and document the vulnerabilities and components contained in the product, including by drawing up a software bill of materials in a commonly used and machine-readable format covering at least the top-level dependencies of the product. Art. 13(7) extends the documentation duty to all relevant cybersecurity aspects observed by the manufacturer, including vulnerabilities that surface after market placement. Art. 13(3) sentence 1 imposes a separate, parallel duty to document and keep up-to-date the risk assessment itself, so the SBOM and the risk record sit in the same documentation bundle but as two distinct artefacts.
  security_rationale: |
    The Annex I Part II (1) identification-and-documentation duty is operationalised in NIST CSF 2.0 through **ID.RA-01 (vulnerabilities in assets identified, validated, and recorded)** and **ID.AM-02 (inventories of software, services, and systems managed by the organisation are maintained)**. ID.RA-01 captures the upstream discovery and recording leg: vulnerabilities -- whether surfaced by internal testing, third-party research, or Art. 14 reporting triggers -- are identified, validated (exploitable or merely theoretical), and recorded in a queryable form that survives across the support period under Art. 13(8) and the 10-year update-availability tail under Art. 13(9). ID.AM-02 anchors the component inventory: software, services, and systems are maintained as a current inventory -- the SBOM is the operational instantiation of this Subcategory -- without which "is this product affected by CVE-X published in year three?" cannot be answered by automated lookup. Together ID.RA-01 and ID.AM-02 form the precondition for every downstream control (patching under PR.PS-02, supply-chain risk management under GV.SC-02, coordinated vulnerability disclosure under SR-CRA-019), and they enable the manufacturer to demonstrate ex post, through documented vulnerability records, SBOM artefacts in the technical documentation under Annex VII section 2(b), and Art. 13(7) cybersecurity-aspects registers, that the Annex I Part II (1) identification duty has been discharged across the support period.
  ambiguity_notes: |
    The phrase "top-level dependencies" in Annex I Part II (1) is POLY-S2, because depth admits at least three materially distinct readings. Reading chosen: R1, where "top-level" maps to first-level direct dependencies with depth-1 look-through; this honours the OJ literal "at the very least the top-level dependencies" without forbidding deeper SBOMs at the manufacturer's discretion. Alternative readings: R2 (full transitive closure) is operationally heavier and not strictly required by the OJ text, though some sector profiles (medical devices, automotive) may exceed this baseline; R3 (critical-path-only) would let vendors omit categories that may matter under coordinated vulnerability disclosure timelines. The "commonly used and machine-readable" VAG+POLY S3 ambiguity is carried up into SR-CRA-008.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-017
  title: "Free-of-charge update dissemination with advisory messages"
  source_clauses:
    - { clause_id: CRA-CL150, article_ref: "Annex I Part II (8) — disseminate without delay, free of charge" }
    - { clause_id: CRA-CL132, article_ref: "Annex I Part I (2)(c) — notification of available updates" }
  linked_objectives: [SO-CRA-009]
  sub_domain: [D-02.2]
  nist_csf_mapping:
    - { id: PR.PS-02, title: "Software is maintained, replaced, and removed commensurate with risk" }
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Annex I Part II (8) requires that, where security updates are available to address identified security issues, they are disseminated without delay, free of charge — unless otherwise agreed for a tailor-made product — accompanied by advisory messages providing users with the relevant information, including on potential action to be taken. Annex I Part I (2)(c) provides the symmetric counterpart on the user-facing notification side: vulnerabilities must be addressed through security updates, including — where applicable — through automatic security updates and through notification of available updates. For a compliance officer the dual architecture (Part II dissemination + Part I notification) means that the release process must publish both the binary artefact and the user-readable advisory, with the tailor-made carve-out documented at the contractual level.
  security_rationale: |
    The Annex I Part II (8) + Annex I Part I (2)(c) dissemination-with-advisory obligation is operationalised in NIST CSF 2.0 through **PR.PS-02 (software maintained, replaced, and removed commensurate with risk)** and **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)**. PR.PS-02 anchors the binary-artefact side: the security update itself is maintained in a form that is ready for dissemination (signed, packaged, integrity-protected) and the availability tail under Art. 13(9) covers it across the post-support window. RS.CO-03 captures the advisory-message leg: dissemination is not silent patch deployment but information-sharing with designated stakeholders -- users, integrators, downstream operators -- consistent with established sharing rules (CVD timelines, tailored-free dissemination rules, confidentiality of pre-disclosure information). Together PR.PS-02 and RS.CO-03 enable the manufacturer to demonstrate ex post, through documented dissemination records, advisory-archive evidence in the technical documentation under Annex VII, and information-sharing logs consistent with the CVD policy under SR-CRA-019, that the binary-and-advisory pair has been delivered without delay and free of charge across the user population subject to the tailor-made exception.
  ambiguity_notes: |
    The phrase "without delay" inherits the S3 ambiguity addressed in SR-CRA-010 and is treated identically — action commences immediately on awareness, with the ceiling set by the technical pipeline. The "unless otherwise agreed" carve-out in Annex I Part II (8) is POLY-S2 because "agreed" admits at least two materially distinct populations: Reading chosen: R1, the literal tailor-made product business-user agreement is the dominant reading, and consumer-product updates cannot be subject to charge under the carve-out. An additional reading, R3, would treat "without delay" as beginning at the moment the security update is technically ready, independent of any corporate release-cycle cadence — a stricter reading that effectively bans bundling security updates with feature releases; R3 is rejected where Annex I Part II (2) explicitly permits bundling under the "where technically feasible" qualifier, but the literal "without delay" from awareness remains the operative anchor. Remain open: (a) does "tailor-made" map onto the same Art. 6(a) proviso population used in SR-CRA-026, or is Annex I Part II (8) carving out a wider product class that lets enterprises negotiate subscription-based security-update access; (b) does Annex I Part II (8) require the advisory message to mention the option to file an Art. 14(8) user notification independently of the manufacturer's dissemination.
```

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
- sr_id: SR-CRA-027
  title: "Product internal-activity recording with user opt-out"
  source_clauses:
    - { clause_id: CRA-CL141, article_ref: "Annex I Part I (2)(l) — recording + monitoring + user opt-out" }
    - { clause_id: CRA-CL158, article_ref: "Annex II §8 — detailed instructions" }
  linked_objectives: [SO-CRA-020, SO-CRA-068]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: PR.PS-04, title: "Log records are generated and made available for continuous monitoring and analysis" }
    - { id: DE.AE-08, title: "Incidents are declared when adverse events meet the defined incident criteria" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(l) requires products with digital elements to provide security-related information by recording and monitoring relevant internal activity — including the access to or modification of data, services, or functions — with an opt-out mechanism for the user. The clause is the product-side mirror of the manufacturer-side access reporting under Annex I (2)(d) (SR-CRA-024) and is supported by Annex II §8, which requires the manufacturer to provide the user with detailed instructions on how the product records and monitors activity and how the opt-out can be exercised. For a compliance officer the operational reading is: log generation on by default, opt-out discoverable, instructions published under Annex II §8, and the security-event lifecycle properly interfaced with downstream incident-management obligations under Art. 14.
  security_rationale: |
    The Annex I Part I (2)(l) + Annex II section 8 internal-activity recording obligation is operationalised in NIST CSF 2.0 through **PR.PS-04 (log records generated and made available for continuous monitoring and analysis)** and **DE.AE-08 (incidents declared when adverse events meet the defined incident criteria)**. PR.PS-04 anchors the log-generation leg: the manufacturer instruments the product to generate log records covering the relevant-internal-activity data class identified by the Art. 13(2) risk assessment, with logs made available for the continuous-monitoring pipeline that consumes them. DE.AE-08 captures the incident-declaration dimension: the recorded events feed into the incident-criteria-evaluation pipeline so that events meeting the criteria are declared as incidents and routed into the Art. 14 reporting architecture (SR-CRA-028 / SR-CRA-031), closing the loop from local product-side recording to upstream regulatory notification. Together PR.PS-04 and DE.AE-08 enable the manufacturer to demonstrate ex post, through documented log-retention evidence, monitoring-pipeline records, and incident-declaration timestamps, that the (2)(l) recording duty has been exercised across the support period and that the upstream declaration pathway is operable when the recorded events meet the criteria.
  ambiguity_notes: |
    The phrase "opt-out mechanism for the user" in Annex I Part I (2)(l) is VAG-S2 because "opt-out" admits at least three materially distinct operational readings. Reading chosen: R1 (the user can disable logging entirely), preserving the literal OJ text. The opt-out creates a privacy-by-design tension: GDPR Art. 25 emphasises by-default-on privacy controls under certain readings, but the OJ CRA text on this clause is opt-out; rule preserves the OJ-literal opt-out interpretation rather than importing non-CRA framings. No S3 instance is introduced on this rule.
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
- sr_id: SR-CRA-029
  title: "Twenty-four-hour AEV early-warning notification"
  source_clauses:
    - { clause_id: CRA-CL53, article_ref: "Art. 14(2)(a) — AEV early warning 24h" }
    - { clause_id: CRA-CL51, article_ref: "Art. 14(1) sentence 1 — awareness trigger" }
  linked_objectives: [SO-CRA-024]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-02, title: "Incident reports are triaged and validated" }
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(2)(a) requires the manufacturer to submit an early warning notification of an actively exploited vulnerability, without undue delay and in any event within 24 hours of the manufacturer becoming aware of it, indicating — where applicable — the Member States on the territory of which the manufacturer is aware that the product has been made available. The clause creates a twin-trigger: the soft "without undue delay" and the hard 24-hour ceiling. For a compliance officer the operational reading is: a 24-hour hard clock from the awareness moment, with the indicator-of-territorial-scope field populated to the best of the manufacturer's current knowledge, and the soft duty requiring action to commence immediately rather than be parked at the ceiling.
  security_rationale: |
    The Art. 14(2)(a) early-warning tier is operationalised in NIST CSF 2.0 through **RS.MA-02 (incident reports triaged and validated)** and **RS.CO-02 (incidents reported internally to the appropriate stakeholders, including executive leadership and legal counsel)**. RS.MA-02 captures the triage-and-validation leg: the 24-hour clock starts from the awareness moment and the manufacturer must triage and validate the AEV well enough to populate the early-warning indicator (territorial scope, suspected cause, affected products) before the ceiling closes -- the Subcategory provides the upstream validation backbone that the regulatory tier depends on. RS.CO-02 anchors the internal-reporting dimension: the soft "without undue delay" clause requires the manufacturer to commence action internally (engineering triage, legal review, executive notification, customer-success coordination) immediately upon awareness, with the internal stakeholders prepared to authorise and execute the disclosure at the moment the regulatory tier fires. Together RS.MA-02 and RS.CO-02 enable the manufacturer to demonstrate ex post, through documented triage timestamps, internal-stakeholder records, and single-platform submission evidence, that the 24-hour early-warning duty has been discharged and that the downstream 72-hour and 14-day tiers can build on a triaged-and-validated starting point.
  ambiguity_notes: |
    The phrase "without undue delay AND in any event within 24 hours" creates an S3 twin-trigger pattern requiring both elements to be satisfied. Reading chosen: R1, treating the 24-hour ceiling as the hard outer boundary and "without undue delay" as the duty to commence action immediately upon awareness, with the literal textual conjunction "in any event" reinforcing the ceiling. An additional alternative reading, R3, would treat the dual-trigger pattern as setting a 24-hour floor with the "without undue delay" clause permitting later submission only when full information is not yet available, with partial reports filed at the ceiling; R3 is rejected because the OJ literal "in any event within 24 hours" does not authorise partial-only filings at the ceiling; the early-warning tier is the partial-information mechanism. Remain open: (a) what constitutes "becoming aware" when the awareness surfaces through a third-party researcher disclosure (Annex I Part II (6)) — is the clock running from the researcher's report or from the manufacturer's triage-validated confirmation; (b) does "in any event" preserve any technical-feasibility carve-out for staged reporting where the territorial-scope indicator cannot be populated in 24 hours, or is the indicator permitted to be partial.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-030
  title: "AEV tiered seventy-two-hour and fourteen-day notifications"
  source_clauses:
    - { clause_id: CRA-CL54, article_ref: "Art. 14(2)(b) — AEV vulnerability notification 72h" }
    - { clause_id: CRA-CL55, article_ref: "Art. 14(2)(c) — AEV final report 14d + content (i)(ii)(iii)" }
  linked_objectives: [SO-CRA-024]
  sub_domain: [D-04.3, D-09.4]
  nist_csf_mapping:
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
    - { id: RS.AN-07, title: "Incident data and metadata are collected, and their integrity and provenance are preserved" }
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(2)(b) requires the manufacturer to submit, unless the relevant information has already been provided, a vulnerability notification without undue delay and in any event within 72 hours of becoming aware of the actively exploited vulnerability, providing general information about the product, the nature of the exploit and vulnerability, the corrective or mitigating measures taken, and the actions users can take. Art. 14(2)(c) requires a final report no later than 14 days after a corrective or mitigating measure is available, including a description of the vulnerability (severity, impact), information on the malicious actor where available, and details of the security update or other corrective measures. For a compliance officer the rule frames the progressive-disclosure architecture: brief at 72 hours, rich at 14 days, both grounded in the awareness timeline.
  security_rationale: |
    The Art. 14(2)(b)+(c) progressive-disclosure architecture is operationalised in NIST CSF 2.0 through **RS.AN-03 (analysis performed to determine what has occurred during an event and the root cause of the event)**, **RS.AN-07 (incident data and metadata collected, and their integrity and provenance preserved)**, and **RS.CO-02 (incidents reported internally to the appropriate stakeholders, including executive leadership and legal counsel)**. RS.AN-03 captures the root-cause-analysis leg: the 72-hour notification reports on what is known about the exploit and the vulnerability, and the 14-day final report supplies the closing root-cause analysis as remediation becomes available, ensuring the regulator receives a coherent cause-and-effect narrative across the tiers. RS.AN-07 anchors the evidence-integrity dimension: the incident data and metadata collected to support both notifications must preserve integrity and provenance so that the regulator's tier-to-tier synthesis is auditable rather than narrative-only. RS.CO-02 closes the internal-coordination loop with executive leadership and legal counsel authorising each tier submission. Together RS.AN-03, RS.AN-07, and RS.CO-02 enable the manufacturer to demonstrate ex post, through documented tier-submission timestamps, evidence-chain-of-custody records, and incident-analysis artefacts in the technical documentation under Annex VII, that the 72-hour and 14-day tiers have been discharged with progressive information richness and that the closing tier provides the depth ENISA's biennial synthesis requires.
  ambiguity_notes: |
    The phrase "14 days after a corrective or mitigating measure is available" is VAG-S2 because "available" admits materially different anchor points. Reading chosen: R1, treating "available" as "released / published" — the moment the manufacturer can demonstrably claim the remediation is ready for deployment. The "unless the relevant information has already been provided" qualifier in Art. 14(2)(b) is VAG-S2 with R1 (technical duplicate of an earlier submission) as the literal reading, and R2 (sufficient-information overlap) as the broader Layer-1 reading.
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
- sr_id: SR-CRA-032
  title: "Severe-incident twenty-four-hour and seventy-two-hour notifications"
  source_clauses:
    - { clause_id: CRA-CL58, article_ref: "Art. 14(4)(a) — SI early warning 24h" }
    - { clause_id: CRA-CL59, article_ref: "Art. 14(4)(b) — SI incident notification 72h" }
  linked_objectives: [SO-CRA-026]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-02, title: "Incident reports are triaged and validated" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(4)(a) and (b) require, for severe incidents, an early warning notification within 24 hours of awareness — including suspected unlawful or malicious-actor causation and the Member-State territories where the product has been made available — followed by an incident notification within 72 hours (general nature, initial assessment, corrective or mitigating measures taken, actions users can take, sensitivity assessment). The 24h/72h twin-trigger is structurally identical to the AEV chain but applies to the higher-severity tier, with the assumption that the CSIRT will route severe-incident reports with priority.
  security_rationale: |
    The Art. 14(4)(a)+(b) severe-incident 24h/72h twin-tier reporting obligation is operationalised in NIST CSF 2.0 through **RS.MA-02 (incident reports triaged and validated)** and **RS.MA-03 (incidents categorised, prioritised, and scoped)**. RS.MA-02 captures the triage-and-validation leg: both the 24-hour early-warning notification and the 72-hour incident notification require upstream triage and validation well enough to populate the indicators (territorial scope, suspected unlawful or malicious-actor causation, sensitivity assessment, corrective or mitigating measures taken, actions users can take) before each ceiling closes. RS.MA-03 anchors the categorisation-and-prioritisation dimension: the severe-incident tier implies higher severity under Art. 14(5), so the Subcategory's priority dimension flows from the categorisation upstream, and the CSIRT may treat the severe-incident chain with priority over the AEV chain when both apply. Together RS.MA-02 and RS.MA-03 enable the manufacturer to demonstrate ex post, through documented triage timestamps, categorisation records, and single-platform submission evidence, that the 24h/72h twin-tier has been discharged with severity-distinct priority and that downstream CSIRTs have received the inputs needed for cross-Member-State coordination.
  ambiguity_notes: |
    The phrase "unlawful OR malicious acts" in Art. 14(4)(a) is COORD-S2 with two terms bound by OR. Reading chosen: R2, treating the terms as distinct — unlawful referring to illegal acts generally and malicious referring to acts with adversarial intent — so that both categories are reported independently. The 24h/72h twin-trigger ambiguity is identical to the AEV chain (see SR-CRA-029) and is not duplicated here.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-033
  title: "One-month severe-incident final report"
  source_clauses:
    - { clause_id: CRA-CL60, article_ref: "Art. 14(4)(c) — SI final report 1 month" }
  linked_objectives: [SO-CRA-026]
  sub_domain: [D-04.3, D-09.4]
  nist_csf_mapping:
    - { id: RS.AN-06, title: "Actions performed during an investigation are recorded, and the records' integrity and provenance are preserved" }
    - { id: RS.AN-08, title: "The investigation's findings and the rationale for decisions are recorded" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(4)(c) requires the manufacturer to submit, unless the relevant information has already been provided, a final report within one month after the submission of the 72-hour incident notification under Art. 14(4)(b), including at least: (i) a detailed description of the incident (severity, impact); (ii) the type of threat or root cause likely to have triggered the incident; (iii) applied and ongoing mitigation measures. The one-month clock starts at the 72-hour notification submission, not at the awareness moment, so the practical cadence is 24h / 72h / ~30 days. For a compliance officer the rule closes out the severe-incident reporting chain with an evidence-rich final report that supports ENISA's biennial synthesis.
  security_rationale: |
    The Art. 14(4)(c) one-month severe-incident final-report obligation is operationalised in NIST CSF 2.0 through **RS.AN-06 (actions performed during an investigation are recorded, and the records' integrity and provenance are preserved)** and **RS.AN-08 (the investigation's findings and the rationale for decisions are recorded)**. RS.AN-06 captures the action-recording leg: the one-month final report must record the actions performed during the investigation -- applied mitigation measures, ongoing mitigation measures, corrective measures available -- with chain-of-custody preservation so the regulator receives auditable evidence rather than narrative summary. RS.AN-08 anchors the rationale-recording dimension: the report documents a detailed description of the incident (severity, impact), the type of threat or root cause likely to have triggered the incident, and the rationale for prioritisation decisions, allowing ENISA 's biennial synthesis pipeline to extract comparable trend data. Together RS.AN-06 and RS.AN-08 enable the manufacturer to demonstrate ex post, through documented investigation records, action-recording evidence, and rationale artefacts in the technical documentation under Annex VII, that the one-month cadence has been discharged with the depth required and that the closing tier supports both incident-closure and longer-horizon trend extraction.
  ambiguity_notes: |
    The phrase "one month" is VAG-S2 as a hard temporal — Reading chosen: R1, treating the literal "within one month after the submission of the incident notification under point (b)" as a calendar month measured from the 72-hour-notification submission date. The "applied and ongoing mitigation measures" enumeration is POLY+S2 with R1 (formal applied measures plus still-being-applied measures) as the literal reading, preserving the distinction between completed and in-progress mitigations.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-034
  title: "Severe-incident CIA-of-sensitive-data categorisation test"
  source_clauses:
    - { clause_id: CRA-CL61, article_ref: "Art. 14(5)(a) — severe-incident test A: CIA of sensitive/important data/functions" }
    - { clause_id: CRA-CL45, article_ref: "Art. 6(2) of NIS 2 (cross-ref via CRA Art. 3(43) `incident`) — availability, authenticity, integrity, confidentiality" }
  linked_objectives: [SO-CRA-027]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, validated, and recorded" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(5)(a) provides that an incident having an impact on the security of the product shall be considered severe where it negatively affects — or is capable of negatively affecting — the ability of the product to protect the availability, authenticity, integrity, or confidentiality of sensitive or important data or functions. The four CIA dimensions (availability, authenticity, integrity, confidentiality) are inherited from NIS 2 via the CRA Art. 3(43) incident cross-reference, with authenticity being the NIS-2/CRA-unique addition over the classical CIA triad. The "or is capable of" gate establishes forward-looking severity rather than strictly materialised harm. For a compliance officer the rule provides the categorisation test A under Art. 14(5), which is satisfied if any one CIA dimension is materially impacted on a sensitive or important data or function category.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — The four CIA dimensions (confidentiality, integrity, availability, authenticity) are listed explicitly in CRA Art. 3(44) `incident` definition. Art. 3(43) imports `incident` from NIS 2 Art. 6(6), not from Art. 6(2).]
  security_rationale: |
    The Art. 14(5)(a) severe-incident categorisation test (CIA of sensitive or important data or functions) is operationalised in NIST CSF 2.0 through **ID.RA-04 (potential impacts and likelihoods of threats exploiting vulnerabilities are identified, validated, and recorded)** and **RS.MA-03 (incidents categorised, prioritised, and scoped)**. ID.RA-04 captures the impact-estimation leg: the four CIA dimensions (availability, authenticity, integrity, confidentiality) inherited from the NIS 2 Art. 6(6) cross-reference must be evaluated for impact on sensitive or important data or functions, and the "capable of" gate requires forward-looking severity assessment even when harm has not materialised. RS.MA-03 anchors the categorisation-and-scoping dimension: the incident is categorised as severe under the Art. 14(5)(a) test when any one CIA dimension is materially impacted on a sensitive or important data or function category, with the Subcategory's scoping leg capturing the territorial and data-class scope. Together ID.RA-04 and RS.MA-03 enable the manufacturer to demonstrate ex post, through documented CIA-impact assessments, threshold-of-sensitivity evidence, and categorisation records, that the Art. 14(5)(a) test was applied with the disjunctive-inclusion reading preserved (any CIA dimension triggering severity) and that the "capable of" gate was exercised with appropriate forward-looking rigour.
  ambiguity_notes: |
    The phrase "negatively affects OR is capable of negatively affecting" is VAG+POLY S3 with R3 (literal inclusive OR) as the chosen reading, so capability is sufficient without materialisation. The phrase "sensitive OR important data or functions" is POLY+COORD S3 with materially distinct populations across the OR chain; Reading chosen: R5, treating the qualifier as broadly inclusive (any data or function significant to user operations), anchored in the harmonised-standards layer under Art. 27. An additional alternative reading, R4-closed, would limit "sensitive or important" to a closed list enumerated in the Annex or implementing acts, restoring a positive enumeration that the current OJ leaves open; R4-closed is admitted as the long-run consensus direction through harmonised standards and ADCO guidance and is rejected for current OJ reading because Annex I plus Art. 14(5) do not provide the enumeration, leaving the determination to the risk assessment until the standardisation layer matures. Remain open: (a) what evidential threshold converts "capable of affecting" into a categorisable severity claim when no harm has materialised; (b) does "sensitive" align with sector-specific legal definitions (GDPR special-category data, NIS 2 essential-services data) or is it CRA-autonomous.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-035
  title: "Severe-incident malicious-code-introduction categorisation test"
  source_clauses:
    - { clause_id: CRA-CL62, article_ref: "Art. 14(5)(b) — severe-incident test B: malicious code" }
  linked_objectives: [SO-CRA-027]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.AN-03, title: "Analysis is performed to establish what has occurred during an event and the root cause of the event" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(5)(b) provides that an incident is severe where it has led, or is capable of leading, to the introduction or execution of malicious code in a product with digital elements or in the network and information systems of a user of the product. The clause is the second disjunctive test under Art. 14(5), complementing the CIA-of-sensitive-or-important impact test under SR-CRA-034. Either test satisfied → severe. For a compliance officer the rule provides the categorisation test B, which is satisfied by an incident with a code-level consequence in either the product or the user's NIS.
  security_rationale: |
    The Art. 14(5)(b) severe-incident categorisation test (malicious code introduction or execution) is operationalised in NIST CSF 2.0 through **RS.MA-03 (incidents categorised, prioritised, and scoped)** and **RS.AN-03 (analysis performed to establish what has occurred during an event and the root cause of the event)**. RS.MA-03 captures the categorisation leg: the malicious-code test is the code-level severity trigger, satisfied by an incident with a code-introduction or code-execution consequence in either the product or the user's NIS, and the Subcategory's priority-and-scope dimension provides the categorisation mechanism through which the severity threshold feeds forward into the Art. 14 reporting cascade. RS.AN-03 anchors the investigation-and-root-cause leg: once code-level compromise is identified, an analysis is performed to establish what has occurred -- the introduction vector (supply-chain, post-deployment exploitation, configuration drift), the execution scope (single device, fleet-wide), and the root cause. Together RS.MA-03 and RS.AN-03 enable the manufacturer to demonstrate ex post, through documented categorisation records, investigation artefacts, and root-cause attribution in the technical documentation under Annex VII, that the Art. 14(5)(b) test was applied consistent with the disjunctive-inclusion reading preserved across both Art. 14(5) tests, and that the malicious-code vector received the same severity-and-priority treatment as the CIA-impact vector under SR-CRA-034.
  ambiguity_notes: |
    The phrase "introduction OR execution" is POLY-S2 with R3 (either — presence or activity) as the chosen reading. The phrase "malicious code" is POLY-S2 with R4 (any code with malicious intent — malware / exploit / backdoor / packaged payload) as the chosen reading. The phrase "in a product … OR in the network and information systems of a user" is SCOPE-Q S2 with R3 (literal inclusive OR) as the chosen reading. No S3 instance is introduced on this rule.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-036
  title: "User notification in machine-readable format with CSIRT fallback"
  source_clauses:
    - { clause_id: CRA-CL65, article_ref: "Art. 14(8) sentence 1 — user notification + machine-readable format" }
    - { clause_id: CRA-CL66, article_ref: "Art. 14(8) sentence 2 — CSIRT fallback" }
  linked_objectives: [SO-CRA-028]
  sub_domain: [D-04.3, D-09.4]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: RS.CO-03, title: "Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(8) sentence 1 requires the manufacturer, after becoming aware of an actively exploited vulnerability or a severe incident, to inform the impacted users of the product with digital elements (and where appropriate all users) of the vulnerability or incident and, where necessary, of any risk-mitigation and corrective measures that the users can deploy — where appropriate in a structured, machine-readable format that is easily automatically processable. Sentence 2 provides for a CSIRT fallback where the manufacturer fails to inform users in a timely manner, allowing the regulator to step in. For a compliance officer the rule operationalises the user-side downstream of the Art. 14 reporting chain, with the option for enterprise-grade automated ingestion via the machine-readable-format expectation.
  security_rationale: |
    The Art. 14(8) sentence 1 user-notification and CSIRT-fallback obligation is operationalised in NIST CSF 2.0 through **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)** and **RS.CO-03 (information shared with designated internal and external stakeholders consistent with the established information-sharing rules)**. RS.CO-03 captures the stakeholder-shared-leg: impacted users (and where appropriate all users) are notified of the vulnerability or incident and the mitigation or corrective measures they can deploy, with the Annex II section 8 user-information pathway providing the structural anchor and the CSIRT-fallback under sentence 2 supplying the regulator-as-proxy architecture when the manufacturer's notification pipeline fails. RS.CO-03 anchors the voluntary-external-sharing dimension: where the manufacturer publishes the information in a structured machine-readable format that is easily automatically processable, enterprise security tooling can ingest the notification automatically and act on it within seconds rather than hours. Together RS.CO-03 enables the manufacturer to demonstrate ex post, through documented user-notification records, machine-readable-format artefacts, and CSIRT-fallback activation logs, that the Art. 14(8) downstream-of-the-reporting-chain duty has been exercised and that the user-autonomy-through-information leg has been preserved.
  ambiguity_notes: |
    The phrase "structured, machine-readable format that is easily automatically processable" is VAG+POLY S3 with format families as the operative divergence. Reading chosen: R4 (any format that automated tooling can ingest), pending Art. 14(10) implementing acts. The phrase "impacted users" is SCOPE-Q S3 with materially distinct populations: R1 (users of the affected product version — literal) and R2 (all users of the product — broader) are both admissible. An additional reading, R3-CSAF, would specify CSAF or a similarly structured sector profile as the implementation, treating "machine-readable" as a binding format reference rather than a format family; R3-CSAF is rejected pending Art. 14(10) implementing acts but the admission may converge with whatever format the acts ultimately specify, given that CSAF-type profiles are the de facto EU baseline in adjacent cybersecurity reporting frameworks. Remain open: (a) when the implementing acts specify a single format, do they bind retroactively across previously-published advisories or only prospectively; (b) does the CSIRT fallback under sentence 2 require the CSIRT to repeat the manufacturer-side reporting chain as well as the user notification, or only the user-side output.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-037
  title: "Intermediate status report on CSIRT request"
  source_clauses:
    - { clause_id: CRA-CL63, article_ref: "Art. 14(6) — intermediate report on CSIRT request" }
  linked_objectives: [SO-CRA-029]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.AN-08, title: "The investigation's findings and the rationale for decisions are recorded" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 14(6) provides that, where necessary, the CSIRT designated as coordinator initially receiving the notification may request manufacturers to provide an intermediate report on relevant status updates about the actively exploited vulnerability or severe incident. The rule bridges the gap between the 24h/72h notifications and the 14d / 1-month final reports, ensuring that CSIRTs have progress visibility when an investigation extends past the early-warning tier. For a compliance officer the rule establishes that the CSIRT, not the manufacturer, drives the intermediate-report cadence, and the duty is contingent on a CSIRT request.
  security_rationale: |
    The Art. 14(6) intermediate-report-on-CSIRT-request obligation is operationalised in NIST CSF 2.0 through **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)** and **RS.AN-08 (the investigation's findings and the rationale for decisions are recorded)**. RS.CO-04 captures the coordination leg: the intermediate-report cadence is CSIRT-driven -- the CSIRT designated as coordinator initially receiving the notification determines when intermediate reports are necessary, and the manufacturer's duty is to respond consistent with the regulator's coordination requirements rather than volunteering reports on a manufacturer-side schedule. RS.AN-08 anchors the rationale-recording dimension: the intermediate reports themselves must record the investigation's findings and the rationale for decisions made during the post-72-hour / pre-final-report window, so the CSIRT's cross-Member-State coordination has auditable evidence rather than narrative summary. Together RS.CO-04 and RS.AN-08 enable the manufacturer to demonstrate ex post, through documented CSIRT request records, intermediate-report submission evidence, and rationale artefacts in the technical documentation under Annex VII, that the Art. 14(6) bridge between the 24h/72h notifications and the 14d/1-month final reports has been exercised at the regulator's request, with the CSIRT-side coordination pipeline able to draw on manufacturer-side progress visibility when investigations extend past the early-warning tier.
  ambiguity_notes: |
    The phrase "where necessary" is VAG-S2 with R1 (necessary per CSIRT determination) as the literal reading, since the CSIRT is the party that assesses necessity. The phrase "relevant status updates" is VAG-S2 with R1 (status relevant to the incident's evolution — anchored in the CSIRT's investigation progress) as the literal reading.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-039
  title: "OSS steward actively-exploited-vulnerability reporting extension"
  source_clauses:
    - { clause_id: CRA-CL103, article_ref: "Art. 24(3) — OSS steward Art. 14(1) extension (with involvement threshold)" }
    - { clause_id: CRA-CL14, article_ref: "Art. 3(14) — open-source software steward definition" }
  linked_objectives: [SO-CRA-031]
  sub_domain: [D-04.3, D-09.1]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 24(3) of the Cyber Resilience Act extends the actively-exploited-vulnerability notification architecture of Article 14(1) to open-source software stewards — defined in Article 3(14) as legal persons — other than manufacturers — that systematically provide support on a sustained basis for the development of specific products with digital elements that are intended for commercial use, whether or not they have a commercial interest in those products. The extension operates to the extent that the steward is involved in the development of the products with digital elements, and the steward is treated, for the purposes of Article 14(1), as a manufacturer for the triggering condition. Article 24(3) further provides that — where a severe incident affects network and information systems provided by the steward for the development of such products — the obligations of Article 14(3) (severe-incident notification) and of Article 14(8) (user notification) apply to the steward in respect of those systems. The territorial scope of the Act (Article 2) and the steward definition (Article 3(14)) together define when this extension is operatively engaged — most notably the `systematically … on a sustained basis` requirement, which is the upstream gate for whether the entity is a steward at all. The recitals (notably Recital 18 on OSS) clarify that the steward is not subject to manufacturer obligations beyond the enumerated Article 14 extensions, preserving the proportionality principle articulated across the Regulation.
  security_rationale: |
    The Article 24(3) reporting extension is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident-management plan executed in coordination with relevant third parties)** and **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)**. RS.MA-01 captures the upstream-coordination function the steward is being asked to perform: once an actively-exploited vulnerability is identified, the steward must execute its incident-management plan in concert with the manufacturer, the CSIRT coordinator, and the wider OSS community that depends on the affected component — the orchestrator-coordination role is the operative duty. GV.PO-01 anchors the documentary foundation: the Article 24(1) cybersecurity policy (see SR-CRA-072) is the policy instrument without which the Article 14(1) extension discharge is procedurally incomplete, and the steward's organisational policy must be auditable on a reasoned MSA request. Together RS.MA-01 and GV.PO-01 enable the steward to demonstrate ex post, through documented coordination logs and policy-evidence records, that the Article 24(3) extension duty has been discharged consistent with the proportionality principle preserved by Recital 18.
  ambiguity_notes: |
    The phrase `to the extent that they are involved in the development of the products with digital elements` carries VAG-S3 ambiguity and exposes three live readings: R1 (commit access to a relevant repository — a strict operational threshold), R2 (maintainer or co-maintainer role in the project — an organisational role threshold), R3 (advisory or review contribution without commit rights — a contribution-volume threshold), and R4 (any involvement in the product's software supply chain — the broad literal reading captured by the words `involved` and `development`). The reading chosen is R4 — the literal text `involved` carries the broadest reasonable construction consistent with the OJ-literal purpose of catching supply-chain-attributable incidents at the upstream end. The qualifier `steward's NIS for the development of such products` is SCOPE-Q-S2: R1 (the steward's own network and information systems only — literal scope). The Article 3(14) `systematically providing support on a sustained basis` threshold, inherited from the steward definition, carries a Berry-classic POLY+COORD signature and is treated in SR-CRA-072's record. Remain open: (a) whether the European Commission's forthcoming guidance on Article 24 (signalled in Recital 18) will supply a narrower reading of `involved in the development` than the R4 literal; (b) whether stewards that monetise upstream components via SaaS, dual-licensing, or sponsored-development arrangements are exposed to dual classification — both as stewards under Article 3(14) and as de facto manufacturers under Article 3(13) — and which obligation set governs.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-074
  title: "OSS steward severe-incident reporting and user notification"
  source_clauses:
    - { clause_id: CRA-CL103, article_ref: "Art. 24(3) — OSS steward Art. 14(3)/(8) extension (NIS threshold)" }
    - { clause_id: CRA-CL58, article_ref: "Art. 14(4)(a) — SI early warning 24h" }
    - { clause_id: CRA-CL65, article_ref: "Art. 14(8) sentence 1 — user notification" }
  linked_objectives: [SO-CRA-031]
  sub_domain: [D-09.1, D-04.3]
  nist_csf_mapping:
    - { id: RS.MA-01, title: "The incident management plan is executed in coordination with relevant third parties once an incident is declared" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 24(3) provides that Article 14(3) (severe-incident notification, with the Article 14(2)/(4) tiered timelines of 24h / 72h / 14d / 1m) and Article 14(8) (user notification) apply to open-source software stewards — in addition to the Article 14(1) extension already addressed in SR-CRA-039 — to the extent that severe incidents affect the network and information systems provided by the steward for the development of such products. The double extension (Article 14(1) for AEVs; Article 14(3)/(8) for severe incidents) closes the symmetric gap that the Article 14(1)-only extension would leave, ensuring that stewards face parallel obligations for severe incidents and user notification of those incidents.
  security_rationale: |
    The Article 24(3) severe-incident reporting and user-notification extension is operationalised in NIST CSF 2.0 through **RS.MA-01 (incident-management plan executed in coordination with relevant third parties once an incident is declared)** and **RS.CO-04 (coordination with stakeholders consistent with applicable rules and regulations)**. RS.MA-01 captures the incident-management coordination function: once a severe incident affecting the steward's NIS is declared, the steward executes its incident-management plan in concert with the CSIRT coordinator, the manufacturer, and the wider OSS community, with the Article 14(4) tiered timelines (24h early warning / 72h notification / 14d interim / 1m final) operationalising the reporting cadence. RS.CO-04 anchors the stakeholder-coordination dimension: the user-notification duty under Article 14(8) and the CSIRT coordination under Article 14(3) are both stakeholder-coordination functions, with the proportionality principle preserved by the steward-status qualifier. Together RS.MA-01 and RS.CO-04 enable the steward to demonstrate ex post, through documented incident-management logs and stakeholder-coordination records, that the Article 24(3) severe-incident duty has been discharged and that the symmetric gap with the Article 14(1) extension has been closed.
  ambiguity_notes: |
    `Affect network and information systems provided by the open-source software stewards for the development of such products` is SCOPE-Q-S2: R1 (the steward's own NIS only — literal scope). The interplay with Article 14(5)'s severe-incident definition (cf. CL61/CL62) is inherited — `severe incident` is a Berry-classic definitional regress, and the same reading applies here as in the manufacturer's Article 14(3) obligation. No major S3 in this SR beyond the inherited severe-incident ambiguity. Remain open: (a) the operational interface with the reporting tiers in Article 14(4) — i.e. whether the steward follows the same 24h / 72h / 14d / 1m ladder as the manufacturer, or whether a single notification to the steward's `home` CSIRT suffices; (b) the operational status of `provided by the open-source software stewards for the development of such products` — whether this covers build-system infrastructure, hosting infrastructure, or both.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-083
  title: "Bidirectional product and manufacturer identification"
  source_clauses:
    - { clause_id: CRA-CL40, article_ref: "Art. 13(15) — product identification (type/batch/serial)" }
    - { clause_id: CRA-CL41, article_ref: "Art. 13(16) — manufacturer contact info on product" }
    - { clause_id: CRA-CL151, article_ref: "Annex II §1 — manufacturer contact info" }
    - { clause_id: CRA-CL153, article_ref: "Annex II §3 — product unique identification" }
  linked_objectives: [SO-CRA-056]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: PR.AA-01, title: "Identities and credentials for authorized users, services, and hardware are managed by the organization" }
    - { id: GV.OC-04, title: "Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 13(15) requires products to bear a type, batch, or serial
    number or other element allowing their identification. Article 13(16)
    requires the product to indicate the manufacturer's name, registered
    trade name, or registered trademark, and a postal address, email or
    other digital contact, and — where applicable — a website. Annex II §1
    and §3 carry the same content into the user-facing information that
    accompanies the product, including in the case of software products
    that are delivered without physical media. Together they establish a
    bidirectional identification chain: every unit of the product is
    traceable, and every unit can be traced back to its manufacturer.
  security_rationale: |
    The Art. 13(15)/(16) and Annex II §1/§3 identification chain is
    operationalised in NIST CSF 2.0 through PR.AA-01 and GV.OC-04. PR.AA-01
    (Identities and credentials for authorized users, services, and
    hardware are managed by the organization) anchors the manufacturer's
    duty to maintain a stable, verifiable product identity — type, batch,
    or serial number — that can be referenced in incident reports, recall
    campaigns, and CSA re-certifications. GV.OC-04 (Critical objectives,
    capabilities, and services that stakeholders depend on or expect from
    the organization are understood and communicated) anchors the
    manufacturer-identity leg of the chain — name, trademark, postal and
    digital contact — as a critical, expected-to-be-communicated element
    of the manufacturer's stakeholder interface. Together, PR.AA-01 and
    GV.OC-04 give the manufacturer a bidirectional identification record
    that the CSA-EU or CSIRT can use to route Art. 14 reports and that the
    manufacturer can demonstrate ex post as the source-of-truth for
    supply-chain attribution.
  ambiguity_notes: |
    The coordination "type, batch or serial number or other element"
    admits any one of those identifiers as the minimum, though multiple
    identifiers strengthen forensic traceability. The coordination "name,
    registered trade name or registered trademark" admits any one of the
    three as the legal-identity anchor; the rest are optional supplements.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-099
  title: "Commission implementing and delegated acts operationalisation"
  source_clauses:
    - { clause_id: CRA-CL49, article_ref: "Art. 13(24) — SBOM implementing acts" }
    - { clause_id: CRA-CL67, article_ref: "Art. 14(9) — delegated acts on delay grounds" }
    - { clause_id: CRA-CL68, article_ref: "Art. 14(10) — implementing acts on notification format/procedures" }
    - { clause_id: CRA-CL8, article_ref: "Art. 7(3) — delegated acts amending Annex III" }
    - { clause_id: CRA-CL9, article_ref: "Art. 7(4) — implementing acts on technical descriptions" }
    - { clause_id: CRA-CL119, article_ref: "Art. 30(6) — implementing acts on labels/pictograms" }
    - { clause_id: CRA-CL50, article_ref: "Art. 13(25) — Union-wide dependency assessment by ADCO" }
  linked_objectives: [SO-CRA-067, SO-CRA-070]
  sub_domain: [D-09.4]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 13(24), 13(25), 14(9), 14(10), 7(3), 7(4), and 30(6)
    collectively establish the Commission and ADCO implementing and
    delegated acts machinery that operationalises, refines, and
    supplements the body of the Regulation. Article 13(24) authorises
    implementing acts on the SBOM format and elements; Article 13(25)
    authorises ADCO to conduct a Union-wide dependency assessment on
    the dependence of Member States and the Union on software
    components, in particular on free and open-source software
    components [Recital 25]; Article 14(9) authorises delegated acts on
    cybersecurity-related grounds for delaying notification
    dissemination; Article 14(10) authorises implementing acts on
    notification format and procedures; Article 7(3) authorises
    delegated acts amending Annex III; Article 7(4) authorises
    implementing acts specifying the technical descriptions of Annex III
    and Annex IV product categories; Article 30(6) authorises
    implementing acts on labels and pictograms related to security.
  security_rationale: |
    The Art. 7(3)/(4), 13(24)/(25), 14(9)/(10), 30(6) Commission and ADCO
    acts machinery is operationalised in NIST CSF 2.0 through GV.PO-02
    and GV.OV-01. GV.PO-02 (Cybersecurity processes and procedures for
    implementing the cybersecurity policy are established, communicated,
    and enforced) anchors the process discipline of tracking Commission
    publication cadence and folding each act into the SDLC and
    documentation package as it is adopted. GV.OV-01 (Cybersecurity risk
    management strategy outcomes are reviewed and adjusted to ensure
    they adequately address organizational risks) anchors the
    review-and-adjust loop triggered by each new act. Together, GV.PO-02
    and GV.OV-01 give the manufacturer a tracking-and-incorporation
    control set that can demonstrate ex post that the body of
    implementing and delegated acts in force at the time of placing was
    correctly reflected in the technical documentation and conformity
    posture.
  ambiguity_notes: |
    The implementing acts referenced by Articles 7(4), 13(24), and 14(9)
    — together with the Art. 7(4) technical descriptions and the Art.
    14(9) delegated acts on delay grounds — are scheduled for adoption by
    11 December 2025. As of mid-2025, several of these acts remain
    unpublished. The standing compliance duty attaches once the acts are
    published; manufacturers that have discharged their pre-July
    obligations on the basis of draft technical descriptions should
    re-verify against the adopted text within a reasonable window after
    publication.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

