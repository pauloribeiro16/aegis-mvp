---
document_id: AEGIS-PREPROC-CRA-ART-27
title: CRA Art. 27 — SecurityObjectives & SecurityRules
regulation: CRA
article: Art. 27
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
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.2.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# CRA Art. 27

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-CRA-052 | A product with digital elements is presumed to be in conformity with the essential cybersecurity requirements set out in Annex I where the product and the manufacturer's processes conform to harmonised standards, common specifications, or European cybersecurity certification schemes adopted pursuant to Regulation (EU) 2019/881 at the assurance level specified by Art. 8(1) or Art. 32(2)/(3). | `CRA-CL108` (Art. 27(1) — presumption of conformity (harmonised standards)); `CRA-CL109` (Art. 27(2) — common specifications); `CRA-CL110` (Art. 27(5) — common-specs presumption); `CRA-CL111` (Art. 27(8) — CSA-certification presumption); `CRA-CL112` (Art. 27(9) — delegated acts specifying CSA schemes) | D-09.1 |
| SO-CRA-052 | D-09.1 | Art. 27(1)/(2)/(5)/(8)/(9) | Presumption of conformity (harmonised standards / common specs / CSA certification) |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-001
  title: "State-of-the-art cryptographic confidentiality baseline"
  source_clauses:
    - { clause_id: CRA-CL129, article_ref: "Annex I Part I (1) — chapeau" }
    - { clause_id: CRA-CL134, article_ref: "Annex I Part I (2)(e) — confidentiality + encryption" }
    - { clause_id: CRA-CL14, article_ref: "Art. 13(1) — design/development/production duty" }
  linked_objectives: [SO-CRA-001, SO-CRA-045]
  sub_domain: [D-01.1, D-01.2]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: PR.DS-02, title: "The confidentiality, integrity, and availability of data-in-transit are protected" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(1) lays the umbrella design-and-development duty on manufacturers, executed in the three sequenced phases described in CRA-CL14 (designed, developed, produced) and tied to the Annex I risk-based baseline through Recital 49. On top of that umbrella, Annex I Part I (1) requires that products with digital elements ensure an appropriate level of cybersecurity based on the risks presented by the product across its life cycle, and Annex I Part I (2)(e) carries that umbrella into a concrete property: stored, transmitted, or otherwise processed data — personal or other — must be protected in its confidentiality by state-of-the-art mechanisms, illustrated as encrypting relevant data at rest or in transit, "or by using other technical means." The triangular architecture — chapeau, Art. 13 umbrella, sub-clause property — is what makes (2)(e) operationally actionable; the manufacturer cannot meet "appropriate cybersecurity" without addressing confidentiality, and cannot address confidentiality without choosing a recognised cryptographic baseline. For a compliance officer this means documenting the cryptographic choice and the underlying risk rationale in the conformity dossier under Annex VII §3, retaining that justification for the support period established under Art. 13(8)–(9) (cf. Recital 49 for the support-period rationale).
  security_rationale: |
    The obligation in Annex I Part I (1)+(2)(e) is operationalised in NIST CSF 2.0 through **PR.DS-01 (data-at-rest confidentiality, integrity, and availability protected)** and **PR.DS-02 (data-in-transit confidentiality, integrity, and availability protected)**. PR.DS-01 anchors the cryptographic protection of stored data -- keys, certificates, key-management material -- so that an attacker who bypasses storage-layer controls (insider access, lost device, misconfigured bucket) still meets ciphertext without the corresponding key, the structural defence against offline exfiltration and ransomware plaintext-theft. PR.DS-02 anchors the in-transit leg: end-to-end confidentiality on data flowing across network paths, service-to-service calls, and external APIs, where network-position adversaries and misconfigured peering make the in-transit stratum the most frequently observed breach vector in published incident telemetry. Together PR.DS-01 and PR.DS-02 form the substrate on which every other Annex I Part I control is laid -- without them, authentication tokens can be intercepted, audit logs exfiltrated, and incident forensics become inadmissible -- and they enable the manufacturer to demonstrate ex post, through documented cipher-suite choices, key-handling evidence in the technical documentation under Annex VII sections 2/3, and conformity-assessment records under Art. 13, that the state-of-the-art baseline required by (2)(e) has been met across the support period under Art. 13(8).
  ambiguity_notes: |
    The source clause carries two distinct ambiguity stacks. First, the term state of the art is VAG-S3 in the Berry-classic sense — temporal and benchmark-relative, much like "state of the art" in GDPR Art. 32(1). Reading chosen: R2, anchoring the benchmark to harmonised standards adopted under Art. 27 (when present) and, in their absence, to industry-standard cryptographic mechanisms as of the product's support-period commencement date. Alternative readings: R1 would require continuous R&D reassessment on a literal "instant of evaluation" basis, generating unbounded compliance churn and effectively compelling a never-finished redesign cycle; R3 (any mechanism chosen by the manufacturer) would dilute the floor to "any algorithm that compiles," breaking the cross-Member-State level playing field that Annex I is designed to deliver. An additional reading, R0, would treat state-of-the-art as a forward-looking duty that anticipates the next regulatory or standards step beyond support-period commencement, structurally similar to R2 but materially more demanding; R0 is rejected on the literal bench-anchored reading preserved by Annex I. Second, the phrase at rest or in transit is POLY-S2 because the boundary between persistent storage, transient caches, and inter-process transfers is technical rather than legal; Reading chosen: R3 — both contexts are protected, with the Art. 13(2) risk assessment selecting the appropriate primitive for each technical layer. Remain open: (a) when harmonised cryptography standards under Art. 27 are slow to be adopted, can a manufacturer rely on industry-led profiles (NIST SP 800-131A, BSI TR-02102) without violating the "state of the art" baseline; (b) does post-quantum migration obligation attach to legacy products within their support period, or only to newly placed-on-the-market versions after a determined cut-over date?
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-013
  title: "Support-period determination using eight-factor methodology"
  source_clauses:
    - { clause_id: CRA-CL28, article_ref: "Art. 13(8) sentence 2 — support-period determination factors" }
    - { clause_id: CRA-CL29, article_ref: "Art. 13(8) sentence 3 — 5-year minimum" }
    - { clause_id: CRA-CL163, article_ref: "Annex VII §4 — support-period determination info" }
  linked_objectives: [SO-CRA-010, SO-CRA-061]
  sub_domain: [D-02.2, D-09.4]
  nist_csf_mapping:
    - { id: ID.IM-02, title: "Improvement processes for cybersecurity risk management are implemented across organizational tiers" }
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape (e.g., the threat environment, technology, regulations, standards)" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 13(8) sentence 2 requires manufacturers to determine the support period so that it reflects the length of time the product is expected to be in use, taking into account reasonable user expectations, the nature of the product including its intended purpose, relevant Union law determining the lifetime of products with digital elements, support periods of similar products by other manufacturers, the availability of the operating environment, the support periods of integrated components that provide core functions and are sourced from third parties, ADCO guidance, and Commission guidance. Art. 13(8) sentence 3 sets a hard minimum of five years, and Annex VII §4 carries the determination into the technical documentation so that the rationale is auditable. For a compliance officer this means a written support-period methodology that walks through each factor and lands on a documented number that meets or exceeds the 5-year floor.
  security_rationale: |
    The Art. 13(8) sentence 2/3 support-period determination obligation is operationalised in NIST CSF 2.0 through **ID.IM-02 (improvement processes for cybersecurity risk management implemented across organisational tiers)** and **GV.OV-02 (organisational cybersecurity risk-management strategy reviewed and adjusted to address changes in the risk landscape -- threat environment, technology, regulations, standards)**. ID.IM-02 captures the methodology-as-process leg: the support-period determination is not a snapshot but an institutionalised improvement process -- the eight factors in Art. 13(8) sentence 2 are a deliberation set rather than a checklist, and the methodology itself is reviewed across organisational tiers so that the determination remains defensible as deployment patterns evolve. GV.OV-02 anchors the strategic-review dimension: the support period interacts with the broader risk-management strategy, and as the threat landscape, technology baseline, regulatory environment, and standards posture change -- including the 10-year update-availability tail under Art. 13(9) -- the determination must remain aligned with the strategy. Together ID.IM-02 and GV.OV-02 enable the manufacturer to demonstrate ex post, through a written support-period methodology that walks through each factor, and through ongoing strategy-review records in the technical documentation under Annex VII section 4, that the determination meets or exceeds the 5-year floor and that the methodology has been exercised across the support period itself.
  ambiguity_notes: |
    The phrase "reasonable user expectations" is VAG-S3 because the criterion is case-law-laden and Berry-classic (cf. CRA-C28 in the v0.1 ambiguity catalogue, §3.2). Reading chosen: R2, anchoring expectations to what a reasonable user in the same product sector would expect, with the harmonised-standards layer and ADCO guidance as the structural benchmark. Alternative readings: R1 (subjective to the specific user) is rejected because it makes the obligation unenforceable; R3 (industry-standard) is materially equivalent to R2 and is admitted as a non-strict alternative under the same OJ literal. An additional reading, R4, would anchor expectations to the consumer-warranty norms of the relevant Member State, importing consumer-protection vocabulary into a cybersecurity obligation; R4 is rejected because consumer-warranty law varies across the Union and would compromise the level playing field that Annex I plus the support-period minimum is designed to deliver; harmonised standards and ADCO guidance remain the structurally sound anchor. Remain open: (a) where Art. 27 harmonised standards specify a category-specific support-period baseline (e.g., a 7-year default for industrial control), does the manufacturer's shorter determination bind or does the standard override; (b) does the support-period determination need to be re-justified at each substantial-modification event under Art. 13(10), or is the initial determination sufficient for the product family.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-022
  title: "Effective and regular security tests with evidence retention"
  source_clauses:
    - { clause_id: CRA-CL145, article_ref: "Annex I Part II (3) — effective and regular tests and reviews" }
    - { clause_id: CRA-CL165, article_ref: "Annex VII §6 — test reports in technical documentation" }
    - { clause_id: CRA-CL174, article_ref: "Annex VIII Part II (8) — Module B periodic audits of vuln handling" }
  linked_objectives: [SO-CRA-014, SO-CRA-069]
  sub_domain: [D-02.4, D-10.3, D-09.4]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: DE.CM-09, title: "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [PERIODIC, CONTINUOUS]
  regulatory_rationale: |
    Annex I Part II (3) requires manufacturers to apply effective and regular tests and reviews of the security of the product with digital elements. Annex VII §6 requires reports of the tests carried out to verify conformity with Annex I Part I and Part II to be part of the technical documentation — so testing produces not just a verdict but an evidence record. Annex VIII Part II (8) provides for periodic audits of the vulnerability-handling processes under Module B, in the conformity-assessment layer. The three anchors together establish that the testing is performed, that the results are recorded, and that the testing programme itself is audited as part of the conformity assessment.
  security_rationale: |
    The Annex I Part II (3) + Annex VII section 6 + Annex VIII Part II (8) testing-and-review obligation is operationalised in NIST CSF 2.0 through **ID.RA-01 (vulnerabilities in assets identified, validated, and recorded)**, **PR.PS-06 (secure software development practices integrated, and their performance monitored throughout the SDLC)**, and **DE.CM-09 (computing hardware and software, runtime environments, and their data monitored to find potentially adverse events)**. ID.RA-01 anchors the vulnerability-discovery leg of testing: each test cycle must produce identified, validated, and recorded vulnerabilities in a form that can be ingested by the Annex I Part II (1) identification pipeline, so the testing infrastructure remains the upstream source of new SBOM entries. PR.PS-06 captures the SDLC-integration dimension: secure software development practices (static analysis, dynamic analysis, fuzzing, integration testing, penetration testing, threat-modelling reviews) are integrated into the SDLC and their performance is monitored -- the "regular" leg of the obligation operates through continuous integration rather than a pre-release gate only. DE.CM-09 closes the monitoring loop, ensuring that the runtime environment and its data are continuously monitored for adverse events that complement the scheduled test cycles. Together ID.RA-01, PR.PS-06, and DE.CM-09 enable the manufacturer to demonstrate ex post, through documented test reports in the technical documentation under Annex VII section 6, scheduled SDLC-pipeline evidence, and Annex VIII Part II (8) Module B audit records, that the testing duty has been exercised continuously and reviewed periodically across the support period.
  ambiguity_notes: |
    The phrase "effective and regular tests and reviews" is VAG+COORD S3 with two stacked ambiguities. Reading chosen: R1 + R1, where "effective" means a test that detects real vulnerabilities with documented coverage and acceptable false-positive rates, and "regular" means a periodic cadence with the record under Annex VII §6. Alternative readings: R2 (comprehensive across all attack surfaces plus ad-hoc in response to specific threats) is admitted as a non-strict alternative under the same OJ literal; R3 (test-once-before-release only) is rejected as failing both the "regular" and the periodic-audit anchor under Annex VIII Part II (8). An additional reading, R3-as-composite, would interpret "effective and regular" as a single integrated quality criterion — tests are evaluated on the combined effect of cadence plus coverage — rather than two separate gates; this reading is admitted as a non-strict equivalent and rejected only where the Annex VIII Part II (8) Module B periodic audits require separate evidence of each dimension, which keeps the two-criterion reading operative in practice. Remain open: (a) when harmonised standards under Art. 27 specify a category-specific testing baseline, does that baseline set the floor or merely a default that manufacturers can replace with documented equivalents; (b) how does Annex VII §6 interact with the Module B periodic audit — is the test report the audit's input, or does the audit produce an independent verification.
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
- sr_id: SR-CRA-077
  title: "Presumption of conformity via harmonised standards or common specifications"
  source_clauses:
    - { clause_id: CRA-CL108, article_ref: "Art. 27(1) — presumption of conformity via harmonised standards" }
    - { clause_id: CRA-CL109, article_ref: "Art. 27(2) — common specifications via implementing acts" }
    - { clause_id: CRA-CL110, article_ref: "Art. 27(5) — presumption via common specifications" }
  linked_objectives: [SO-CRA-052]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 27(1) gives manufacturers a presumption-route into Annex I
    conformity: where a product with digital elements and the manufacturer's
    processes conform to harmonised standards — or parts thereof — whose
    references have been published in the Official Journal, conformity with
    the Annex I requirements is presumed to the extent that those standards
    cover those requirements [Recital 50]. The rule is rebuttable: the
    presumption can be displaced by evidence that the product does not
    actually meet Annex I despite applying the cited standards. Article 27(2)
    authorises the Commission to adopt implementing acts establishing common
    specifications when harmonised standards are unavailable or insufficient,
    and Article 27(5) extends the same presumption to products and processes
    conforming to those common specifications [Recital 51].
  security_rationale: |
    The Art. 27(1) presumption of conformity is operationalised in NIST CSF 2.0
    through GV.OC-03 and GV.PO-02. GV.OC-03 (Legal, regulatory, and contractual
    requirements regarding cybersecurity are understood and managed) anchors the
    manufacturer's standing duty to track the Official Journal list of
    harmonised standards and to know which Annex I requirements each cited
    standard covers. GV.PO-02 (Cybersecurity processes and procedures for
    implementing the cybersecurity policy are established, communicated, and
    enforced) translates the Art. 27(2)/(5) common-specification fallback into a
    documented process that the SDLC executes when no harmonised standard
    exists, and that records the alternative solution adopted. Together,
    GV.OC-03 and GV.PO-02 let the manufacturer demonstrate ex post that the
    Art. 27(1) presumption was not invoked on stale or out-of-scope citations
    and that the Art. 27(5) common-specification route was followed where the
    harmonised-standards list was silent.
  ambiguity_notes: |
    The phrase "presumed to be in conformity" carries a structural ambiguity
    on whether the presumption is conclusive or rebuttable. The literal text
    uses "presumed", which — read with general EU product-safety case law —
    signals a rebuttable presumption rather than a binding acquittal: a
    market-surveillance authority remains free to verify Annex I compliance
    on substance. The coverage qualifier "to the extent that the standards
    cover those requirements" means that an Annex I requirement not
    addressed by the cited standard is not swept into the presumption and
    must be demonstrated by the manufacturer. Partial-standard coverage
    therefore shifts the burden back onto the manufacturer for the
    un-addressed elements.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-078
  title: "CSA certification presumption at substantial assurance level"
  source_clauses:
    - { clause_id: CRA-CL111, article_ref: "Art. 27(8) — CSA-certification presumption" }
    - { clause_id: CRA-CL112, article_ref: "Art. 27(9) — delegated acts specifying CSA schemes" }
    - { clause_id: CRA-CL10, article_ref: "Art. 8(1) — assurance level at least `substantial`" }
  linked_objectives: [SO-CRA-052]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [CONTINUOUS, TRIGGERED]
  regulatory_rationale: |
    Article 27(8) presumes that a product with digital elements and the
    manufacturer's processes for which the manufacturer has obtained an EU
    statement of conformity or an EU certificate under a European
    cybersecurity certification scheme adopted pursuant to Regulation (EU)
    2019/881 — at assurance level at least "substantial" — are in
    conformity with the Annex I cybersecurity requirements, to the extent
    that the certification covers those requirements [Recital 53]. Article
    27(9) authorises the Commission to adopt delegated acts specifying which
    CSA schemes and which product categories are eligible to demonstrate
    Annex I conformity through this route. Article 8(1) sets the assurance-
    level floor for critical-product certification at "at least substantial".
  security_rationale: |
    The Art. 27(8) certification-presumption is operationalised in NIST CSF
    2.0 through GV.OC-03 and GV.SC-04. GV.OC-03 anchors the manufacturer's
    duty to identify which CSA scheme, which assurance level (at least
    "substantial" per Art. 8(1)), and which Annex I requirements are
    actually covered by the issued certificate, and to keep that mapping
    current against the Commission's Art. 27(9) delegated acts. GV.SC-04
    (Suppliers and other third parties are routinely assessed using audits,
    test results, or other forms of evaluation to confirm they are meeting
    their contractual obligations) extends the third-party-assessment
    posture to the certification body itself, treating the CSA certificate
    as ongoing auditable evidence rather than a one-time artefact. Together,
    GV.OC-03 and GV.SC-04 let the manufacturer document ex post that the
    Art. 27(8) presumption covers each Annex I requirement it claims
    coverage for, and that the certificate is renewed within the scheme's
    surveillance window.
  ambiguity_notes: |
    The qualifier "at least substantial" is a floor that higher assurance
    levels (e.g. "high") satisfy automatically, but the practical
    availability of CSA schemes that cover CRA critical-product categories
    is the hard constraint. As of mid-2025, no CSA scheme has been adopted
    under Article 27(9) that covers the Annex IV critical-product
    catalogue, so the certification-presumption path is effectively dormant
    for critical products. The text directs such products to the Article
    32(4) fallback — the substantial-level certificate of Regulation (EU)
    2019/881 or, in its absence, the Article 32(3) third-party route of
    Module B+C, H, or certification. The open operational question is
    whether ENISA will deliver a critical-product CSA scheme aligned with
    Regulation (EU) 2019/881 before the Commission's delegated acts under
    Article 27(9) materially shape the certification landscape.
```

### SO-CRA-001 / SO-CRA-002 / SO-CRA-003 (confidentiality + state-of-the-art encryption)

```yaml
- sr_id: SR-CRA-097
  title: "Class II conformity routes including CSA certification"
  source_clauses:
    - { clause_id: CRA-CL125, article_ref: "Art. 32(3) — Class II important products: B+C / H / certification at substantial" }
  linked_objectives: [SO-CRA-066]
  sub_domain: [D-09.4, D-10.3]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [MANUFACTURER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 32(3) routes Class II important products — those listed in
    Annex III Class II — to Module B+C, Module H, or — where available
    and applicable — a European cybersecurity certification scheme
    pursuant to Article 27(9) at assurance level at least "substantial".
    The certification path is the third option in Article 32(3), in
    addition to the two notified-body routes inherited from Article 32(2)
    [Recital 58].
  security_rationale: |
    The Art. 32(3) Class II routes are operationalised in NIST CSF 2.0
    through GV.OC-03. GV.OC-03 (Legal, regulatory, and contractual
    requirements regarding cybersecurity are understood and managed)
    anchors the class-identification and procedure-selection content:
    the manufacturer identifies the Annex III Class II classification,
    evaluates whether an Art. 27(9) CSA scheme at "substantial" or
    higher covers the product category, and selects the admissible
    route — Module B+C, Module H, or CSA certification. The
    single-Subcategory mapping reflects that the addition over Class I
    is the certification path rather than a new control surface.
    GV.OC-03 gives the manufacturer a managed-requirements framework
    that can demonstrate ex post that the Class II procedure was
    correctly chosen from the three available options, including the
    CSA certification route when available.
  ambiguity_notes: |
    "At assurance level at least 'substantial'" reads literally: the
    assurance-level floor is "substantial". Higher levels (e.g. "high")
    satisfy the floor by definition. The structural constraint is the
    availability of CSA schemes covering the Class II product category;
    where no such scheme has been adopted under Article 27(9), the
    certification path collapses into the Article 32(2)-equivalent
    Module B+C / H routes.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

