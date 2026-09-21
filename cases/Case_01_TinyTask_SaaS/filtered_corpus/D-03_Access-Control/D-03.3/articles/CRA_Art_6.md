---
document_id: AEGIS-PREPROC-CRA-ART-6
title: CRA Art. 6 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 6
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---

# CRA Art. 6

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-018 | A product with digital elements is made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. | `CRA-CL131` (Annex I Part I (2)(b) — secure by default + tailor-made exception + reset to original); `CRA-CL2` (Art. 6(a) proviso — properly installed, intended purpose, reasonably foreseeable use, necessary security updates installed) | D-03.4 (CRA sole authority per taxonomy §4.1) |
| SO-CRA-018 | D-03.4 (CRA sole authority) | Annex I Part I (2)(b) + Art. 6(a) proviso | Secure-by-default configuration + tailor-made exception + reset |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-004
  title: "Cryptographic key separation from operational environment"
  source_clauses:
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — `and by using other technical means`" }
    - { clause_id: CRA-CL133, article_ref: "Annex I Part I (2)(d) — access control" }
    - { clause_id: CRA-CL2, article_ref: "Art. 6(a) proviso — installation/conditions" }
  linked_objectives: [SO-CRA-004]
  sub_domain: [D-01.3, D-01.1, D-03.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.AA-05, title: "Access permissions, entitlements, and authorizations are defined and managed in accordance with the principle of least privilege" }
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Annex I Part I (2)(e) attaches the state-of-the-art encryption obligation to the relevant data — not to the storage medium — such that possession of the cryptographic key is the necessary condition for intelligibility; the residual "or by using other technical means" extends the toolbox beyond pure cryptography into access-control, tokenisation, and segregation patterns. Annex I Part I (2)(d) imposes the access-control duty that determines which actors may reach the key or the encrypted blob: the engineer and the operator do not need the same level of access. Combined with the Art. 6(a) proviso — requiring the product to be properly installed, maintained, and used in accordance with its intended purpose — the implication is that the key-handling environment must be separable from the operational environment that consumes the protected data, otherwise the access-control duty is rendered moot by the colocation of custodian and consumer.
  security_rationale: |
    The combined Annex I (2)(d)+(2)(e) + Art. 6(a) duty is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)**, **PR.AA-05 (access permissions, entitlements, and authorisations managed in accordance with the principle of least privilege)**, and **GV.OV-01 (cybersecurity risk-management strategy outcomes reviewed and adjusted to address organisational risks)**. PR.DS-01 anchors the cryptographic protection of stored data so that possession of the key is the necessary condition for intelligibility -- the colocation of data store and key server collapses this property into a speed-bump, while separation preserves it as a boundary. PR.AA-05 captures the access-control dimension: distinct role-based credentials, distinct custodians for key-material and operational environments, and least-privilege entitlements that the Annex I (2)(d) duty requires. GV.OV-01 ensures the key-separation policy is reviewed across the support period under the manufacturer's broader risk-management strategy, so that the separation invariant remains in force as deployment patterns and integration topologies evolve. Together PR.DS-01, PR.AA-05, and GV.OV-01 enable the manufacturer to demonstrate ex post, through documented key-handling evidence, role-separation policy records, and governance-review minutes in the technical documentation under Annex VII sections 2/3, that the cryptographic key environment is operationally separable from the data-consuming environment in the sense Annex I requires.
  ambiguity_notes: |
    The Annex I text does not mention key management explicitly — the synthesis catalogue (99_CRA_Synthesis.md §4) flags this as a T2-vs-text gap — so the key-separation reading rests on the combination of Annex I (2)(d) access-control duty with the Annex I (2)(e) "other technical means" residual. Reading chosen: R2, anchoring separation in functional role-based access control rather than in physical separation, so that the key-material custodian and the operational-environment custodian are distinct roles with distinct credentials. No S3 instance is introduced directly on this rule; the S2 ambiguity on "relevant data" is inherited from SR-CRA-002 and applies in the same way.
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
- sr_id: SR-CRA-025
  title: "Secure-by-default configuration with reset capability"
  source_clauses:
    - { clause_id: CRA-CL131, article_ref: "Annex I Part I (2)(b) — secure by default configuration" }
    - { clause_id: CRA-CL2, article_ref: "Art. 6(a) proviso — properly installed, intended purpose, reasonably foreseeable" }
    - { clause_id: CRA-CL3, article_ref: "Art. 3(23) — intended purpose" }
  linked_objectives: [SO-CRA-018, SO-CRA-045]
  sub_domain: [D-03.4]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Annex I Part I (2)(b) requires products to be made available on the market with a secure-by-default configuration — including the possibility to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. Art. 6(a) proviso anchors the configuration to intended purpose and reasonably foreseeable use, framing "secure" against the operational context the manufacturer reasonably anticipated. Art. 3(23) defines the intended purpose, providing the lexical anchor for what counts as "use" in the proviso. The combination addresses three obligations in one clause: default configuration, reset capability, and tailor-made carve-out.
  security_rationale: |
    The Annex I Part I (2)(b) + Art. 6(a) + Art. 3(23) secure-by-default obligation is operationalised in NIST CSF 2.0 through **PR.PS-01 (configuration management practices established, documented, and applied to assets)** and **PR.DS-12 (data managed consistent with the organisation's risk strategy to protect the confidentiality, integrity, and availability of data)**. PR.PS-01 anchors the configuration-baseline leg: the secure-by-default configuration is itself a documented configuration baseline, applied at first power-up to every unit leaving the manufacturing pipeline, with the configuration-change history auditable as part of the broader configuration-management practice. PR.DS-12 captures the data-management side: the secure-by-default configuration is the protective posture that determines which data CIA properties hold by default, with the reset-to-original-state capability providing the recovery path when a user has driven the configuration away from the secure baseline. Together PR.PS-01 and PR.DS-12 enable the manufacturer to demonstrate ex post, through documented baseline-configuration records, configuration-change audit trails, and reset-capability evidence in the technical documentation under Annex VII sections 2/6, that the secure-by-default floor has been applied at the point of market placement and that the reset capability has been preserved as the recovery path.
  ambiguity_notes: |
    The phrase "secure by default configuration" is VAG-S3 because three materially distinct configurations produce materially different compliance populations. Reading chosen: R2 — the security features (authentication, access control, audit logging, network segmentation, secure-update mechanism) are enabled by default at first power-up. Alternative readings: R1 (deny-all initial state, with the user explicitly enabling required services) and R3 (zero-config security, the product works securely without any user configuration) are operationally convergent with R2: all three require security features on at delivery, and only the configuration-management user-experience differs. An additional reading, R4, would extend the "secure by default" floor to the post-deployment configuration surface: any change the user makes from the default is documented and reversible through the reset mechanism; R4 is admitted as a strengthening of the chosen R2 reading and is rejected where it would conflict with the tailor-made carve-out, which permits negotiated non-default configurations in business-user settings. Remain open: (a) when a user explicitly changes a setting from the secure default and a subsequent vulnerability surfaces, does the manufacturer retain responsibility for the as-configured state or does the configuration shift break the Art. 13(2) risk-assessment chain; (b) does the "reset to original state" obligation require preserving user data through the reset (R3) or wiping it (R1/R2).
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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

