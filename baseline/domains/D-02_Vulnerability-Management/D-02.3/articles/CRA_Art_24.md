---
document_id: AEGIS-PREPROC-CRA-ART-24
title: CRA Art. 24 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 24
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
status: DRAFT
---

# CRA Art. 24

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-031 | An open-source software steward shall — to the extent the steward is involved in the development of the products with digital elements — notify actively exploited vulnerabilities of such products to the CSIRT designated as coordinator and to ENISA via the single reporting platform; and — to the extent severe incidents affect network and information systems provided by the steward for the development of such products — apply the severe-incident and user-notification obligations of Art. 14(3)/(8). | `CRA-CL103` (Art. 24(3) — OSS steward Art. 14(1)/(3)/(8) extension); `CRA-CL44` (Art. 3(44) — incident definition) | D-04.3, D-09.1 |
| SO-CRA-031 | D-04.3, D-09.1 | Art. 24(3) | OSS steward Art. 14 notification extension (with involvement threshold) |
| SO-CRA-049 | An open-source software steward puts in place and documents in a verifiable manner a cybersecurity policy fostering the secure development of products with digital elements and the effective handling of vulnerabilities by the developers of those products, including aspects related to documenting, addressing, and remediating vulnerabilities, and the sharing of information concerning discovered vulnerabilities within the open-source community; the policy takes into account the specific nature of the open-source software steward and the legal and organisational arrangements to which it is subject. | `CRA-CL101` (Art. 24(1) — OSS steward policy); `CRA-CL14` (Art. 3(14) — open-source software steward definition); `CRA-CL48` (Art. 3(48) — free and open-source software definition) | D-09.1 |
| SO-CRA-049 | D-09.1 | Art. 24(1) + Art. 3(14)/(48) | OSS steward cybersecurity policy (verifiable) |
| SO-CRA-050 | An open-source software steward cooperates with market surveillance authorities and provides documentation on request. | `CRA-CL102` (Art. 24(2) — OSS steward cooperation with MSAs) | D-09.1 |
| SO-CRA-050 | D-09.1 | Art. 24(2) | OSS steward cooperation with MSAs |

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
- sr_id: SR-CRA-072
  title: "OSS steward verifiable cybersecurity policy and CVD enablement"
  source_clauses:
    - { clause_id: CRA-CL101, article_ref: "Art. 24(1) — OSS steward cybersecurity policy" }
    - { clause_id: CRA-CL14, article_ref: "Art. 3(14) — open-source software steward definition" }
    - { clause_id: CRA-CL48, article_ref: "Art. 3(48) — free and open-source software definition" }
  linked_objectives: [SO-CRA-049]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 24(1) requires open-source software stewards to put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product. The policy shall: (i) foster the voluntary reporting of vulnerabilities as laid down in Article 15 by the developers of that product; (ii) take into account the specific nature of the open-source software steward and the legal and organisational arrangements to which it is subject; (iii) include aspects related to documenting, addressing, and remediating vulnerabilities; (iv) promote the sharing of information concerning discovered vulnerabilities within the open-source community. The four sub-elements together define the minimum content of the cybersecurity policy — verifiable documentation, voluntary-reporting enablement, nature-aware proportionality, and remediation-practice coverage.
  security_rationale: |
    The Article 24(1) OSS-steward cybersecurity policy duty is operationalised in NIST CSF 2.0 through **GV.PO-01 (organisational cybersecurity policy established, communicated, and enforced)** and **GV.SC-01 (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed)**. GV.PO-01 captures the policy-instrument layer: the cybersecurity policy is established, communicated (across the steward's maintainer base, contributors, and downstream dependents), and enforced through the documented four sub-elements (i)–(iv), with the verifiable-documentation character of the policy supplying the auditability anchor under Article 24(2) MSA cooperation (SR-CRA-073). GV.SC-01 anchors the supply-chain-risk-management dimension: the policy is positioned as the entry point of the steward's supply-chain risk management programme, with the upstream-coverage of OSS contributors and the downstream-coverage of dependents integrated into the programme. Together GV.PO-01 and GV.SC-01 enable the steward to demonstrate ex post, through the documented policy and the supply-chain-programme evidence, that the Article 24(1) duty has been discharged consistent with the proportionality principle preserved by Recital 18 and the steward definition under Article 3(14).
  ambiguity_notes: |
    `Documented in a verifiable manner` carries VAG-S3 ambiguity — the operational threshold is supplied by Article 24(2) (cf. SR-CRA-073): R1 (self-verification — the steward can demonstrate the policy on request), R2 (third-party-attested), R3 (MSA-verified on demand). Reading chosen: R1 (literal — `verifiable manner` = the steward can demonstrate the policy on request, with Article 24(2) MSA cooperation providing external verification on demand). R2 (third-party attestation) is rejected as over-prescriptive for OSS stewards; R3 (MSA-verified) is rejected as over-restrictive, since Article 24(2) only triggers on reasoned request. `Foster` (VAG+POLY-S3): R1 (encourage — literal). `Systematically providing support on a sustained basis` inherits Article 3(14) D14 — R3 (both — regular + ongoing). Remain open: (a) whether the voluntary-reporting enablement under (i) requires a published CVD coordinator email / signed PGP key / security.txt — analogous to RFC 9116 — or whether softer enablement suffices; (b) the operational handling of `verifiable` at enforcement — i.e. whether MSAs will accept a steward's self-attestation or will look for an external anchor.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-073
  title: "OSS steward cooperation with market surveillance authorities"
  source_clauses:
    - { clause_id: CRA-CL102, article_ref: "Art. 24(2) — OSS steward cooperation with MSAs" }
  linked_objectives: [SO-CRA-050]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role:
    - OSS_STEWARD  # Exception per Orchestrator brief — not in strict enum
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 24(2) requires open-source software stewards to cooperate with the market surveillance authorities and — upon reasoned request — provide documentation of their cybersecurity policy and the relevant security aspects of the products they steward. The duty is request-triggered: there is no standing reporting or audit obligation; the cooperation obligation fires only upon an MSA request that is reasoned (specific operational cause). The requested documentation can include both the policy itself (Article 24(1)) and the technical security aspects of the stewarded products.
  security_rationale: |
    The Article 24(2) OSS-steward cooperation duty is operationalised in NIST CSF 2.0 through **GV.SC-04 (suppliers and other third parties routinely assessed against contractual obligations)** and **GV.OC-03 (legal, regulatory, and contractual requirements regarding cybersecurity understood and managed)**. GV.SC-04 captures the third-party-assessment dimension: the MSA is treated as a regulated assessor, and the steward's cooperation duty operationalises the third-party-assessment-on-request function, with the documentation of policy + security aspects supplying the assessment record. GV.OC-03 anchors the legal-and-regulatory-requirements-managed dimension: the steward's regulatory requirements (Article 24(1) policy maintenance + Article 24(2) cooperation duty) are managed, with the request-triggered nature of the duty preserved (no standing reporting or audit). Together GV.SC-04 and GV.OC-03 enable the steward to demonstrate ex post, through documented cooperation logs and request-response records, that the Article 24(2) duty has been discharged and that the MSA has been provided with the documentation required to verify the Article 24(1) policy.
  ambiguity_notes: |
    No major S2/S3. POLY-S2 on `upon reasoned request`: R1 (literal — request with specific operational cause, mirroring the Article 23(1) reading for economic operators). Remain open: (a) the operational interface between Article 24(2) (steward cooperation) and Article 24(3) (steward severe-incident reporting) — i.e. whether a steward's Article 24(2) cooperation on a reported incident triggers any parallel Article 24(3) duty; (b) the procedural details of the `relevant security aspects of the products they steward` — i.e. whether MSAs may request vulnerability-handling records, CVD statistics, or maintainer-supplier relationships.
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

