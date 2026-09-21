---
document_id: AEGIS-PREPROC-GDPR-ART-6
title: GDPR Art. 6 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 6
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.1.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# GDPR Art. 6

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-015 | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed; further processing is compatible with the original purposes per the Art. 6(4) compatibility test. | `GDPR-CL03` (Art. 5(1)(c)); `GDPR-CL14` (Art. 6(4)) | D-05.1 |
| SO-GDPR-015 | D-05.1 | Art. 5(1)(c), Art. 6(4) | Data minimisation — adequate, relevant, necessary |
| SO-GDPR-016 | Personal data are processed lawfully, fairly, and in a transparent manner, on the basis of one of the six Art. 6(1) lawfulness bases (or one of the Art. 9(2) bases for special categories). | `GDPR-CL01` (Art. 5(1)(a)/(b)); `GDPR-CL08–CL13` (Art. 6(1)(a)–(f)); `GDPR-CL21` (Art. 9(1) prohibition + exceptions) | D-05.1, D-09.1 |
| SO-GDPR-016 | D-05.1, D-09.1 | Art. 5(1)(a)/(b), Art. 6(1)(a)–(f), Art. 9(1) | Lawfulness, fairness, transparency; legal-basis selection |
| SO-GDPR-020 | Where processing is based on consent (Art. 6(1)(a)) or on a contract (Art. 6(1)(b)) and carried out by automated means, the data subject receives the personal data concerning him or her in a structured, commonly used, machine-readable format and can transmit those data to another controller. | `GDPR-RT10` (Art. 15(3) — copy); `GDPR-CP09` (Art. 28(3)(g) — return/deletion); informed by Art. 20 (cross-chapter inheritance) | D-05.4 |
| SO-GDPR-032 | Consent to personal-data processing is freely given, specific, informed, and unambiguous; the controller demonstrates the data subject's consent on request; withdrawal of consent is as easy as giving; bundled consent requests are presented in a clearly distinguishable form; conditional consent (bundled with contract) is presumed non-compliant unless processing is strictly necessary for contract performance; special-category consent is at the higher `explicit` standard; child consent (information-society services) is gated by Art. 8 age thresholds and parental-responsibility verification; transfer consent (Art. 49(1)(a)) is `explicit` and risk-informed. | `GDPR-C05` (Art. 4(11) — consent definition); `GDPR-CL08` (Art. 6(1)(a)); `GDPR-CL15` (Art. 7(1)); `GDPR-CL16` (Art. 7(2)); `GDPR-CL17` (Art. 7(3)); `GDPR-CL18` (Art. 7(4)); `GDPR-CL19` (Art. 8(1) — age threshold); `GDPR-CL20` (Art. 8(2) — reasonable verification); `GDPR-CL22` (Art. 9(2)(a) — explicit consent for special categories); `GDPR-TR08` (Art. 49(1)(a) — explicit transfer consent) | D-09.1, D-03.1 |
| SO-GDPR-032 | D-09.1, D-03.1 | Art. 4(11), Art. 6(1)(a), Art. 7, Art. 8, Art. 9(2)(a), Art. 49(1)(a) | Consent lifecyle: specific, informed, demonstrable, withdrawable |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-008
  title: "DPIA and risk-profile review on material change"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(11) — DPIA review" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(d)" }
  linked_objectives: [SO-GDPR-004, SO-GDPR-028]
  sub_domain: [D-09.2, D-10.3, D-02.1]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Inherent risk understood via threats/vulnerabilities/likelihood/impact" }
    - { id: ID.IM-02, title: "Improvement processes implemented across organizational tiers" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PERIODIC, TRIGGERED]
  regulatory_rationale: |
    Art. 35(11) requires the controller, where necessary, to carry out a review to assess whether processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations. Combined with Art. 32(1)(d), which mandates the regular testing, assessing and evaluating of the effectiveness of security measures, this creates a continuous-improvement obligation for security-relevant processing: the DPIA is not a one-off deliverable but a living artefact refreshed on material change. The two provisions differ in trigger: Art. 32(1)(d) is periodic (cadence-anchored), Art. 35(11) is triggered (change-anchored), and the controller must operate both in parallel.
  security_rationale: |
    The obligation in Art. 35(11), read with Art. 32(1)(d), to keep the DPIA and the security-control assessment under periodic and triggered review is operationalised in NIST CSF 2.0 through **ID.RA-05 (Inherent risk understood via threats, vulnerabilities, likelihoods, impacts)** and **ID.IM-02 (Improvement processes implemented across organizational tiers)**.
    ID.RA-05 anchors the risk-reassessment method that uses threats, vulnerabilities, likelihoods and impacts to recompute inherent risk, satisfying the Art. 35(11) change-of-risk trigger and supplying the evidence base for the Art. 32(1)(d) periodic evaluation.
    ID.IM-02 captures the continuous-improvement layer: improvement processes implemented across organisational tiers, ensuring that reassessment outputs actually feed back into control updates rather than accumulating as static documents.
    The two subcategories together cover both the periodic (cadence-anchored) and triggered (change-anchored) review modes that Art. 35(11) and Art. 32(1)(d) impose in parallel, with the controller maintaining a living DPIA register rather than a one-off deliverable.
    A controller documenting ID.RA-05 reassessment records, ID.IM-02 improvement-cycle evidence and the change triggers that prompted each review can demonstrate ex post, under Art. 5(2), that the DPIA and the security posture were kept current against the evolving risk landscape.
  ambiguity_notes: |
    GDPR-CP22 (Art. 35(11)) carries no S3 ambiguity in the operative clause. `where necessary` and `change of the risk represented` are acknowledged Berry VAG; both readings converge on the obligation to reassess when the risk profile changes. The triggering "change" is documented in the controller's change-management policy and includes: change in processing purpose (Art. 6(4) compatibility), change in data categories (especially Art. 9 special categories), change in data-subject population (volume or vulnerability), change in technical context (new processor, new third country), and change in regulatory expectation (new EDPB guidance). EDPB Guidelines 4/2019 on DPIA provide non-binding factors for materiality but do not bind the controller.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-025
  title: "Purpose-bound data minimisation with compatibility assessment"
  source_clauses:
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation" }
    - { clause_id: GDPR-CL14, article_ref: "Art. 6(4) — compatibility test" }
    - { clause_id: GDPR-CL02, article_ref: "Art. 5(1)(b) — purpose limitation (cross)" }
  linked_objectives: [SO-GDPR-015]
  sub_domain: [D-05.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: ID.AM-03, title: "Inventories of data and metadata for designated data types" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. Art. 6(4) provides the compatibility test for further processing beyond the original purposes, requiring the controller to take into account, inter alia, (a) any link between the purposes, (b) the context of collection, (c) the nature of the personal data (especially special categories), (d) the possible consequences for data subjects, and (e) the existence of appropriate safeguards. Art. 5(1)(b) purpose limitation supplies the upstream anchor. Read together, the three provisions establish that data minimisation is calibrated to the purpose, that any change of purpose triggers a compatibility assessment, and that the purpose itself is bound by specification, explicitness, and legitimacy.
  security_rationale: |
    The obligation in Art. 5(1)(c), read with the Art. 6(4) compatibility test and Art. 5(1)(b) purpose limitation, to keep personal data adequate, relevant and limited to what is necessary is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data managed consistent with risk strategy)** and **ID.AM-03 (Inventories of data and metadata for designated data types)**.
    ID.AM-03 anchors the data-inventory foundation that minimisation requires: knowing what data is held, for which declared purpose, and with which metadata, supplying the asset record without which the Art. 5(1)(c) necessity test cannot be applied and the Art. 6(4) compatibility assessment cannot be run on a change of purpose.
    PR.DS-12 captures the policy-level data-management strategy that the inventory enables: per-purpose collection limits, retention schedules that delete at purpose-end, and the documented compatibility assessment for any further processing, satisfying the proportionality-to-purpose standard.
    The two subcategories together operationalise minimisation as both a knowledge property (what is held) and a discipline (how it is bounded), reducing attack surface and breach impact as security side-effects.
    A controller documenting ID.AM-03 data inventory and PR.DS-12 retention-and-compatibility decisions can demonstrate ex post, under Art. 5(2), that each dataset was necessary for its purpose and that any purpose-change survived the Art. 6(4) test.
  ambiguity_notes: |
    `adequate, relevant, and limited to what is necessary` carries VAG-S3 (three conjunctive vague adjectives). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. An alternative reading treats adequacy as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs for sensitive-data contexts. The Art. 6(4) compatibility test is the procedural mechanism for any change of purpose; the five factors are conjunctive in the sense that all must be considered, but the test is qualitative and the controller exercises judgement. Remain open: (a) whether machine-learning model training purposes are compatible with the original collection purpose under Art. 6(4), or require fresh consent, pending EDPB AI Act interaction guidance and CJEU jurisprudence on inferred-data compatibility; and (b) whether the data-minimisation threshold differs for secondary processing for fraud-prevention or IT-security purposes under Art. 6(1)(f), pending alignment with the legitimate-interests balancing test.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-026
  title: "Lawful, fair, and transparent processing on documented Art. 6 basis"
  source_clauses:
    - { clause_id: GDPR-CL01, article_ref: "Art. 5(1)(a) — lawfulness, fairness, transparency" }
    - { clause_id: GDPR-CL08, article_ref: "Art. 6(1)(a) — consent" }
    - { clause_id: GDPR-CL02, article_ref: "Art. 5(1)(b) — purpose limitation (cross)" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy established, communicated, enforced" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    The lawful/fair/transparent obligation in Art. 5(1)(a) is the gateway
    principle: every personal-data processing operation must satisfy all
    three conjunctive conditions, regardless of which Art. 6(1) lawfulness
    base the controller relies on (Recital 39). Lawfulness anchors
    processing in a recognised legal basis, and for consent specifically
    Art. 6(1)(a) couples with the Art. 4(11) freely-given, specific,
    informed and unambiguous definition; for the other five bases the
    controller relies on the relevant sub-clause of Art. 6(1)(b)–(f). Fairness,
    as developed by the EDPB, looks at the balance of power between data
    subject and controller and forbids deceptive or unexpectedly
    detrimental processing. Transparency, anchored in Arts. 12–14, requires
    that information about the processing be intelligible, easily
    accessible, and provided in clear and plain language. Art. 5(1)(b)
    purpose limitation binds all three by requiring that purposes be
    specified, explicit and legitimate before processing begins.
  security_rationale: |
    The obligation in Art. 5(1)(a), read with Art. 6(1)(a) and Art. 5(1)(b), to ensure that every personal-data processing operation is anchored in a specified purpose and a traceable Art. 6(1) lawfulness basis is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **GV.PO-01 (Organizational cybersecurity policy is established, communicated, and enforced)**.
    GV.OC-03 is the regulatory-translation discipline: it forces the controller to inventory the Art. 6(1) bases on which each data flow depends, to characterise the lawfulness, fairness and transparency obligations that flow from Art. 5(1)(a), and to keep that inventory current as purposes or bases change — directly satisfying the substantively fair and procedurally transparent posture that Art. 5(1)(a) imposes.
    GV.PO-01 translates the same requirements into a communicated, enforced organisational policy layer: every deployment of a personal-data pipeline must carry a documented, auditable link from the data flow to its specified purpose and Art. 6 basis, with security controls inheriting their scope from that upstream lawful-purpose layer rather than substituting for it.
    A controller that documents GV.OC-03 inventory coverage and GV.PO-01 policy enforcement on every data flow can demonstrate ex post, against the Art. 5(2) accountability threshold, that no production processing operated outside an identifiable Art. 6 basis on the day of any supervisory inspection.
  ambiguity_notes: |
    `lawful, fair, transparent` carries three conjunctive vague adjectives,
    each a Berry-flagged open-texture term (Berry §5.1), and the
    relationship between them is multiplicative rather than additive:
    failure of any one vitiates the Art. 5(1)(a) obligation. The reading
    adopted for this SR combines the substantive interpretation of
    fairness, namely no deception about purpose or use combined with a
    balance-of-interests test on data-subject impact, with the procedural
    interpretation grounded in notice, consent and complaint-channel
    availability, and aligns with EDPB Guidelines 05/2020 on consent
    (EDPB Guidelines 05/2020 §3). Two alternative readings remain on the
    table. The consequentialist reading, under which fairness is measured
    by the absence of significant detrimental consequence to the data
    subject unless proportionate, shifts the analysis away from process
    quality and towards outcome harm and weakens the ex-ante compliance
    posture. The procedural-only reading restricts fairness to the
    existence of notice, consent and complaint channels and effectively
    collapses fairness into transparency, leaving substantive data-subject
    harm outside the scope of Art. 5(1)(a). Remain open: (a) whether
    `fairness` requires substantive balance-of-interests or only
    procedural safeguards in cross-border employment-data contexts; (b)
    whether AI-driven profiling that respects transparency obligations can
    nevertheless fail Art. 5(1)(a) on substantive fairness grounds even
    where the data subject has consented.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-027
  title: "Six documented lawfulness bases with necessity gating per purpose"
  source_clauses:
    - { clause_id: GDPR-CL09, article_ref: "Art. 6(1)(b) — contract" }
    - { clause_id: GDPR-CL10, article_ref: "Art. 6(1)(c) — legal obligation" }
    - { clause_id: GDPR-CL11, article_ref: "Art. 6(1)(d) — vital interests" }
    - { clause_id: GDPR-CL12, article_ref: "Art. 6(1)(e) — public interest" }
    - { clause_id: GDPR-CL13, article_ref: "Art. 6(1)(f) — legitimate interests" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures established and enforced" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-PURPOSE]
  regulatory_rationale: |
    Art. 6(1) lists six lawfulness bases for processing personal data,
    namely (a) consent, (b) contract, (c) legal obligation, (d) vital
    interests, (e) public interest and (f) legitimate interests, and the
    same Article applies, via Art. 9(2), to special categories (Recital
    40). Each processing purpose must be supported by at least one
    identifiable base, and the basis must be documented at the time of
    determination of the means and re-evaluated when the purpose changes.
    Bases (b) through (d) carry their own qualifiers, with `necessary`
    gating performance of a contract under (b), `necessary for compliance
    with a legal obligation` under (c) and `necessary to protect vital
    interests` under (d), while (e) requires a Union or Member State law
    basis and (f) requires the legitimate-interest balancing test
    (Recital 47; Recital 49). The EDPB Guidelines 02/2019 on Art. 6(1)(b)
    interpret `necessary` strictly, and the EDPB Guidelines on legitimate
    interests develop the (f) balancing test (purpose test, necessity
    test, balancing test).
  security_rationale: |
    The obligation in Art. 6(1)(b)–(f), read with Art. 5(1)(b) and Art. 5(1)(c), to record and refresh an identifiable lawfulness basis for every processing purpose is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)**.
    GV.OC-03 captures the regulatory-translation layer: the controller must inventory the six Art. 6(1) bases against the five `necessary` qualifiers (contract, legal obligation, vital interests, public-interest law, and the legitimate-interest balancing test) and re-evaluate that inventory each time the purpose evolves, satisfying the upstream anchor that any personal-data flow must be traceable to a named basis before processing begins.
    GV.PO-02 turns that inventory into enforced process: documented procedure for selecting a base, recording the necessity and (where applicable) balancing-test evidence, and refreshing the record on purpose change, so that security controls scope themselves from a defensible lawful-purpose classification rather than from an undocumented controller assertion.
    A controller that documents GV.OC-03 basis-to-purpose coverage and GV.PO-02 review cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection each processing operation was operating within an identifiable Art. 6 basis with the appropriate `necessary` threshold documented at the time of determination of the means.
  ambiguity_notes: |
    Each of bases (b) through (f) carries Berry-flagged VAG-S3
    open-texture on `necessary`. Base (e) carries POLY+VAG-S3 on the scope
    of `public interest` and on the law-by-law requirement, and base (f)
    carries POLY+VAG-S3 on what counts as a `legitimate interest`. The
    reading adopted for this SR follows the EDPB Guidelines 02/2019
    interpretation for (b), Art. 6(3) for (c), Recital 46 for (d), the
    EDPB reading on (e) under which Union or Member State law must provide
    the basis, and the EDPB Guidelines on legitimate interests for (f).
    All five non-consent sub-bases are preserved as distinct. Two
    alternative readings remain on the table. First, an expansive reading
    of `necessary` in (b) that treats any commercial reliance on the data
    subject as automatically satisfying necessity would weaken the
    data-minimisation correlate of Art. 5(1)(c) and is rejected. Second,
    a controller-discretion reading of (f) that downplays the balancing
    test in favour of a procedural documented-assessment step would lose
    the substantive protection the test provides. Remain open: (a)
    whether AI-training pipelines using contractual necessity under (b)
    can satisfy the `necessary` threshold when alternative, less-
    intrusive legal bases exist; (b) whether public-interest bases under
    (e) require sector-specific Member State law or accept cross-sector
    horizontal law.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-036
  title: "Sub-processor authorisation with controller change-notification"
  source_clauses:
    - { clause_id: GDPR-CP08, article_ref: "Art. 28(2) — sub-processor authorisation" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(d) — sub-processor conditions (cross)" }
  linked_objectives: [SO-GDPR-022]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-SUB-PROCESSOR]
  regulatory_rationale: |
    Art. 28(2) requires the processor not to engage another processor
    without prior specific or general written authorisation of the
    controller. In the case of general written authorisation, the
    processor must inform the controller of any intended changes
    concerning the addition or replacement of other processors,
    thereby giving the controller the opportunity to object to such
    changes. Art. 28(3)(d) requires the contract to respect the
    conditions for engaging another processor (i.e., flow the (2) and
    (4) rules into the processor contract).
  security_rationale: |
    The obligation in Art. 28(2) and Art. 28(3)(d) to obtain the controller's prior written authorisation before engaging another processor, and to notify the controller of any change in the case of general authorisation so that the controller has an opportunity to object, is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-02 captures the prioritisation and assessment discipline: every sub-processor must be known, prioritised against the data it will touch, and assessed using the SCRM process before it is engaged, so that the full chain of entities with personal-data access is visible to and acceptable to the controller.
    GV.SC-03 captures the contract-flowing discipline: the sub-processor authorisation requirement is not merely a one-time notice — it must appear on the face of the contract between controller and processor, with the same written-authorisation and notification-of-change mechanics that the substantive provision requires, so that the controller's object right is exercisable throughout the relationship rather than only at onboarding.
    A processor that documents GV.SC-02 sub-processor assessment on each engagement and GV.SC-03 contract-anchored authorisation plus change-notification discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the personal-data access chain was complete, documented and within the controller's objectable scope.
  ambiguity_notes: |
    `prior specific or general written authorisation` carries VAG+SCOPE-Q
    S2 (Berry §5.1): the `specific` versus `general` distinction is the
    same as the Art. 6(1)(a) consent-specificity question. The reading
    adopted for this SR is that written authorisation in either form is
    acceptable, with notification-on-changes required in the general case
    (EDPB Guidelines 07/2020). An alternative reading under which only
    `specific` authorisation suffices for sensitive data flows would
    tighten the obligation but conflicts with the OJ text, which makes
    the general authorisation path explicit. Remain open: whether
    `opportunity to object` requires a reasonable objection window (e.g.,
    30 days) or whether silent acquiescence suffices.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-046
  title: "Four-element DPIA content with necessity and proportionality test"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7)(a)–(d) — DPIA content" }
  linked_objectives: [SO-GDPR-028]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-DPIA]
  regulatory_rationale: |
    Art. 35(7) requires the DPIA to contain at least: (a) a systematic
    description of the envisaged processing operations and the purposes
    of the processing, including, where applicable, the legitimate
    interest pursued by the controller; (b) an assessment of the
    necessity and proportionality of the processing operations in
    relation to the purposes; (c) an assessment of the risks to the
    rights and freedoms of data subjects referred to in paragraph 1;
    (d) the measures envisaged to address the risks, including
    safeguards, security measures and mechanisms to ensure the
    protection of personal data and to demonstrate compliance with this
    Regulation taking into account the rights and legitimate interests
    of data subjects and other persons concerned.
  security_rationale: |
    The obligation in Art. 35(7)(a)–(d) to construct each DPIA on the four mandated elements — systematic description, necessity and proportionality assessment, risks-to-data-subjects assessment, and measures-envisaged — is operationalised in NIST CSF 2.0 through **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **RS.AN-03 (Analysis is performed to determine what has occurred during an event and the root cause of the event)**.
    ID.RA-05 captures the structured-risk-assessment spine of Art. 35(7)(b) and (c): the controller must assemble threats, vulnerabilities, likelihoods and impacts into a coherent inherent-risk picture before designing measures, which is precisely the necessity-and-proportionality analysis and the risks-to-data-subjects assessment that the two sub-letters require.
    RS.AN-03 captures the measures-envisaged discipline in Art. 35(7)(d): the documentation of safeguards, security measures and mechanisms to demonstrate compliance is operationally a structured analysis of what each measure is designed to address and how it traces to a specific identified risk, with the trace preserved for inspection and for after-the-fact learning.
    A controller that documents ID.RA-05 threat-vulnerability-likelihood-impact assembly and RS.AN-03 measure-by-measure analysis linkage can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any high-risk processing the DPIA's four Art. 35(7) elements were each substantively populated and trace-linked rather than merely listed.
  ambiguity_notes: |
    `necessity and proportionality` carries Berry-flagged POLY-S2 — three
    different `necessity` senses appear across GDPR (Art. 5(1)(c) data
    minimisation, Art. 6(1)(b) contract, Art. 35(7)(b) DPIA) and the
    same term is operationalised differently in each. The reading
    adopted for this SR is the Art. 35(7)(b)-internal reading:
    necessity means no less-intrusive alternative achieves the purpose;
    proportionality means the processing's benefits justify its
    intrusiveness on data-subject rights. An alternative reading that
    imports the Art. 6(1)(b) contract-necessity standard would conflict
    with the DPIA-specific framing. Remain open: whether the
    proportionality prong requires quantified trade-off analysis (e.g.,
    cost-benefit) or accepts qualitative judgement.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-051
  title: "Demonstrable consent with equally accessible withdrawal path"
  source_clauses:
    - { clause_id: GDPR-C05, article_ref: "Art. 4(11) — consent definition" }
    - { clause_id: GDPR-CL08, article_ref: "Art. 6(1)(a) — consent as lawfulness base" }
    - { clause_id: GDPR-CL15, article_ref: "Art. 7(1) — demonstrability" }
    - { clause_id: GDPR-CL17, article_ref: "Art. 7(3) — withdrawal" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CONSENT-COLLECTION, CONTINUOUS]
  regulatory_rationale: |
    Art. 4(11) defines consent as any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. Art. 6(1)(a) anchors that consent as one of six alternative lawfulness bases, meaning that any single processing operation relying on consent must satisfy the Art. 4(11) elements in full. Art. 7(1) shifts the evidentiary burden onto the controller, which must be able to demonstrate that the data subject has consented. Art. 7(3) then grants the data subject the right to withdraw consent at any time, requires withdrawal to be as easy as giving consent, requires the data subject to be informed of that right before giving consent, and obliges the controller to cease processing based on consent upon withdrawal without affecting the lawfulness of processing carried out before withdrawal (Recital 65).
  security_rationale: |
    The obligation in Art. 4(11), Art. 6(1)(a), Art. 7(1) and Art. 7(3) is
    operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and
    bound to credentials based on the context of interactions)** and **GV.OC-03
    (Legal, regulatory, and contractual requirements regarding cybersecurity —
    including privacy and civil liberties obligations — are understood and
    managed)**.

    PR.AA-02 controls the binding of the data subject's identity to the consent
    artefact: because the consent act functions as an authentication of intent,
    the controller must proof the identity of the consenting party and bind that
    proof to a credential-like consent record that is reproducible on demand.
    GV.OC-03 captures the broader legal-basis frame: the controller's
    organisation must understand and manage the conditions under which consent
    remains valid, the demonstrability threshold imposed by Art. 7(1), and the
    operational withdrawal mechanism that Art. 7(3) requires to be as accessible
    as the original consent collection.

    Together the two subcategories give the controller an auditable consent
    ledger (identity-bound artefacts under PR.AA-02) embedded in a managed
    regulatory-compliance process (under GV.OC-03), enabling ex-post
    demonstration to the supervisory authority that each Art. 4(11) qualifier was
    satisfied and that withdrawal was honoured without retroactive lawfulness
    collapse.
  ambiguity_notes: |
    The four Art. 4(11) qualifiers — freely given, specific, informed, unambiguous — are each open-textured and together carry the highest coordination risk because they are conjunctive, so failure of any one defeats the consent. Reading chosen: the four qualifiers must all be present simultaneously, as anchored by EDPB Guidelines 05/2020 §3.1 (consent must be a freely given, specific, informed and unambiguous indication, with each element assessed independently). An alternative reading limits the assessment to the absence of clear duress or deception, treating specific and unambiguous as formal rather than substantive qualifiers; this narrower reading is plausible for low-risk processing but is inconsistent with EDPB §3.1 and with CJEU Planet49 (C-673/17 §73), which held that pre-ticked boxes do not constitute unambiguous consent. A second alternative would treat specific as a granularity requirement separate from informed, requiring a separate consent per processing purpose even where the data subject is fully informed of all purposes, which is consistent with EDPB §3.4 but operationally costly and not always demanded by supervisory authorities in practice. Remain open: (a) whether the four qualifiers admit a sliding-scale intensity test proportionate to the sensitivity of the data and the purpose, or whether each must always be satisfied at uniform intensity; (b) whether Art. 7(3) as easy as giving consent applies only to the withdrawal mechanism proper, or extends to the procedural difficulty of locating that mechanism within the wider user interface.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-054
  title: "Verified consent for child and transfer-risk contexts"
  source_clauses:
    - { clause_id: GDPR-CL19, article_ref: "Art. 8(1) — age threshold" }
    - { clause_id: GDPR-CL20, article_ref: "Art. 8(2) — reasonable verification efforts" }
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit transfer consent" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1, D-03.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-OFFERING, PER-TRANSFER]
  regulatory_rationale: |
    Art. 8(1) sets a default age of 16 for consent in information-society services offered directly to a child, with Member States permitted to lower the threshold by law provided it is not below 13 (Recital 38); the threshold governs only consent and not the other Art. 6 lawfulness bases. Art. 8(2) requires the controller to make reasonable efforts to verify that parental responsibility is held in respect of any child below the threshold, taking into consideration available technology, which is a process obligation rather than an outcome guarantee. Art. 49(1)(a) requires, as a derogation for international transfers in the absence of adequacy and appropriate safeguards, that the data subject has explicitly consented to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and of appropriate safeguards (Recital 49). The three articles together form a single rule on consent validity for vulnerable contexts: child consent requires parental verification (Art. 8) and transfer consent requires informed risk acknowledgement (Art. 49(1)(a)), both layered on top of the Art. 4(11) baseline.
  security_rationale: |
    The obligation in Art. 8(1)–(2) and Art. 49(1)(a) is operationalised in NIST
    CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials based
    on the context of interactions)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    PR.AA-02 controls the identity-proofing step that Art. 8(2) requires: the
    controller must make reasonable efforts to verify that the consenting party
    holds parental responsibility for a child below the age threshold, and the
    available-technology standard operates as a rolling baseline that the
    proofing mechanism must track. The same subcategory controls the stronger
    transfer-risk-informed consent that Art. 49(1)(a) requires, layered on top of
    the Art. 4(11) baseline with explicit risk acknowledgement. GV.OC-03 captures
    the wider regulatory frame across Member-State age-threshold variations
    (which span 13 to 16) and across the transfer-restriction regime under which
    Art. 49(1)(a) sits as a narrow derogation rather than a general mechanism.

    Together the two subcategories embed age and transfer-risk verification in a
    documented identity-proofing process (PR.AA-02) within a managed
    regulatory-compliance frame (GV.OC-03), enabling the controller to
    demonstrate ex-post that the Art. 8 verification effort was reasonable in its
    technological context and that Art. 49(1)(a) consent was collected with
    informed risk acknowledgement.
  ambiguity_notes: |
    Art. 8(1) parental-responsibility carries POLY-S3 because Member State legal definitions diverge (some treat only biological parents as holders of parental responsibility, others include guardians and educational institutions). Art. 8(2) reasonable efforts carries VAG-S3 because the available-technology standard is a rolling benchmark and no supervisory authority has published a hard test. Art. 49(1)(a) explicitly consented carries POLY-S3 against the Art. 4(11) unambiguous standard and the Art. 9(2)(a) explicit standard. The rule preserves the EDPB Guidelines 05/2020 reading that the derogation consent must be explicit, specific to the transfer, and documented as risk-informed, so the controller cannot rely on the same consent artefact used for the underlying Art. 6(1)(a) basis. An alternative reading confines Art. 8(2) reasonable efforts to a one-time check at the moment of consent collection; this reading is rejected because EDPB Guidelines on Art. 8(2) treat the obligation as continuing for as long as the child uses the service. A second alternative reading treats the Art. 49(1)(a) explicit consent as a one-time event that survives subsequent changes in the destination regime; this reading is rejected because the risk-informed nature of the consent requires re-confirmation when the destination regime materially changes. Remain open: (a) whether reasonable efforts under Art. 8(2) includes reliance on the data subject's self-declaration of age or whether a positive verification step (credit-card verification, ID upload, knowledge-based authentication) is required; (b) whether Art. 49(1)(a) explicit consent can be combined with Art. 6(1)(a) consent in a single transaction or must be collected through a separate user journey that highlights the transfer-risk information.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

