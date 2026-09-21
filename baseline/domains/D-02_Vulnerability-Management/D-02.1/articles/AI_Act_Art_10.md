---
document_id: AEGIS-PREPROC-AI_Act-ART-10
title: AI_Act Art. 10 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 10
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
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---

# AI_Act Art. 10

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-AIACT-003 | High-risk AI systems which make use of techniques involving the training of AI models with data are developed on the basis of training, validation and testing data sets that meet quality criteria, supported by data governance practices that detect, prevent and mitigate possible biases and that allow the detection of biases in view of the intended purpose. | `AIA-C05` (Art. 10(1) `quality criteria` + 3-way dataset AND); `AIA-C06` (Art. 10(2) 8-element list of data governance practices + 3-way AND of bias activities + `biases` POLY); `AIA-C08` (Art. 10(5) special-category data + `strictly necessary` + `state-of-the-art` + 6 cumulative conditions (a)–(f)) | D-05.1, D-05.2 |
| SO-AIACT-003 | D-05.1, D-05.2 | Art. 10(1)+(2)+(3) | Data governance practices + dataset quality + bias detection |
| SO-AIACT-004 | Where strictly necessary for the purpose of ensuring bias detection and correction in high-risk AI systems, providers may exceptionally process special categories of personal data subject to appropriate safeguards and six cumulative conditions, including state-of-the-art security and privacy-preserving measures. | `AIA-C08` (Art. 10(5) — exception to GDPR Art. 9 prohibition; 6 cumulative conditions (a)–(f) all required; cross-regulation borrow from GDPR) | D-05.1 |
| SO-AIACT-004 | D-05.1 | Art. 10(5) | Special-category data for bias detection with 6 cumulative conditions |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-004
  title: "Closed-list data-governance practice with bias examination and mitigation"
  source_clauses:
    - { clause_id: AIA-C05, article_ref: "Art. 10(1) — `High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used`" }
    - { clause_id: AIA-C06, article_ref: "Art. 10(2) — 8-element closed list (a)–(h) of data governance practices, including (f) examination in view of possible biases … and (g) appropriate measures to detect, prevent and mitigate possible biases" }
  linked_objectives: [SO-AIACT-003]
  sub_domain: [D-05.1, D-05.2]
  nist_csf_mapping:
    - { id: ID.AM-03, title: "Inventories of data and corresponding metadata for designated data types are maintained" }
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Article 10(1) of the AI Act requires that high-risk AI systems
    making use of techniques involving the training of AI models
    with data be developed on the basis of training, validation and
    testing data sets that meet the quality criteria laid down in
    paragraphs (2) to (5) whenever those data sets are used. Article
    10(2) operationalises this requirement through an eight-element
    closed list of data-governance practices covering
    data-collection processes, data-preparation operations,
    assumption-formulation, relevance-assessment, bias examination,
    and bias detection, prevention and mitigation. Sub-points (f)
    and (g) carry particular weight because they translate the
    upstream data-governance duty into operational bias-handling
    obligations: (f) requires examination of training, validation
    and testing data sets in view of possible biases, and (g)
    requires appropriate measures to detect, prevent and mitigate
    those biases. The cumulative eight-element structure means
    providers must address all eight practices; partial compliance
    with a subset does not satisfy Article 10. The exception in
    Article 10(5), linked from SR-AIACT-006, exceptionally permits
    processing of special-category personal data within tightly
    bounded conditions and operates within the GDPR Article 9
    prohibition.
  security_rationale: |
    The obligation in Art. 10(1)–(2) is operationalised in NIST
    CSF 2.0 through **ID.AM-03 (Inventories of data and
    corresponding metadata for designated data types are
    maintained)**, **PR.DS-12 (Data is managed consistent with the
    organization's risk strategy to protect the confidentiality,
    integrity, and availability of data)**, and **PR.PS-06 (Secure
    software development practices are integrated, and their
    performance is monitored throughout the SDLC)**. ID.AM-03
    supplies the dataset-inventory substrate for traceability from
    data sources through preparation operations to deployed model.
    PR.DS-12 binds dataset management to the organisation's risk
    strategy, the upstream control that the bias-examination
    (sub-point f) and bias-detection/prevention/mitigation
    (sub-point g) duties operationalise — bias in training data
    propagates into the deployed system and creates both
    discriminatory outcomes and poisoned-data attack surface.
    PR.PS-06 integrates secure development throughout the SDLC,
    embedding data-collection, preparation and bias-mitigation
    practices in the secure engineering pipeline. A provider
    evidencing ID.AM-03 inventories, PR.DS-12 risk-aligned
    management and PR.PS-06 SDLC integration demonstrates ex post
    that the Art. 10(1)–(2) cumulative eight-element duty —
    including the bias examination and mitigation in (f) and (g)
    — is audit-traceable from data source to deployed model.
  ambiguity_notes: |
    The clause carries the central S3 poly-semous ambiguity on the
    term `biases`, which is undefined in the Act and admits three
    distinct readings: statistical bias understood as sampling error
    producing unequal distribution of features, algorithmic bias
    understood as model architecture or training producing unequal
    performance across subgroups, and societal bias understood as
    deployed system producing discriminatory real-world outcomes.
    The chosen reading is cumulative, with all three senses in
    scope, because the `examination in view of possible biases`
    opening together with the `detect, prevent AND mitigate` verb
    chain implicates upstream, model-level and downstream bias
    treatment. As an alternative, providers could focus on
    statistical bias only, since it is the most readily measurable
    sense. As a second alternative, providers could focus on
    societal bias only, since the Act frames the risk-management
    duty as protecting fundamental rights under the Charter. The
    eight-element closed list is AND-coordinated, so partial
    compliance of six of eight does not satisfy Article 10; within
    sub-point (g), the verbs `detect, prevent AND mitigate` form a
    further three-way AND of distinct activities, all of which must
    be operationalised. The phrase `techniques involving the
    training of AI models` is itself poly-semous, with possible
    readings including fine-tuning, transfer learning and
    reinforcement learning from human feedback; the chosen reading
    is broad, since the cross-reference to training, validation
    and testing datasets implies a comprehensive scope. Remain
    open: (a) whether `biases` in sub-points (f) and (g) encompasses
    both unintentional demographic bias and intentional
    backdoor-style data-poisoning vectors that AI-Act Article 15(5)
    addresses separately; (b) whether the eight-element list admits
    any proportional scaling based on the size of the dataset or
    the risk class of the high-risk system per Annex III.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-005
  title: "Dataset fitness benchmark across relevance representativeness and completeness"
  source_clauses:
    - { clause_id: AIA-C07, article_ref: "Art. 10(3) — `Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose`" }
  linked_objectives: [SO-AIACT-003]
  sub_domain: [D-05.1, D-05.2]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS, ONE_TIME]
  regulatory_rationale: |
    Article 10(3) of the AI Act imposes a dataset-quality
    requirement on providers of high-risk AI systems: training,
    validation and testing data sets shall be relevant, sufficiently
    representative, and to the best extent possible, free of errors
    and complete in view of the intended purpose. The clause
    functions as the substantive quality benchmark referenced by
    the umbrella duty in Article 10(1) and the data-governance
    practices listed in Article 10(2). The five-criteria structure
    — relevance, representativeness, error-freeness, completeness,
    plus the modifier `sufficiently` and the hedge `to the best
    extent possible` — is bound together with the soft hedge placed
    at the third coordinator, which affects the parse of what is
    hedged. The clause is the principal locus where dataset quality
    is operationalised for the high-risk-AI domain, and it
    interacts with the AI-Office guidance on dataset quality that is
    expected to be issued under Article 56 codes of practice. The
    `in view of the intended purpose` qualifier ties dataset
    quality back to the scope-determiner concept that recurs
    throughout Article 10 and the broader Act.
  security_rationale: |
    The obligation in Art. 10(3) is operationalised in NIST CSF 2.0
    through **PR.DS-12 (Data is managed consistent with the
    organization's risk strategy to protect the confidentiality,
    integrity, and availability of data)** and **PR.DS-01 (The
    confidentiality, integrity, and availability of data-at-rest
    are protected)**. PR.DS-12 supplies the risk-aligned
    data-management substrate that the five quality criteria
    (relevant, sufficiently representative, free of errors,
    complete, and the soft-hedge qualifier) require for
    fitness-for-purpose — dataset quality must be tied to the
    organisation's documented risk strategy rather than treated as
    a free-standing metric. PR.DS-01 anchors the integrity
    dimension that the `free of errors and complete` criteria
    operationalise, protecting data-at-rest from corruption, label
    noise, missingness, and systematic measurement error that
    would otherwise produce downstream model failures or
    data-poisoning attack surface. Together, the two PR.DS
    sub-categories ensure that dataset quality is treated as a
    data-security property bound to the organisation's risk
    strategy. A provider documenting PR.DS-12 risk-aligned data
    management and PR.DS-01 data-at-rest integrity controls
    demonstrates ex post that the Art. 10(3) five-criteria
    benchmark — including the strict-literal hedge binding on
    `free of errors and complete` — is evidence-based and
    supervisory-auditable, with documented thresholds for each
    criterion.
  ambiguity_notes: |
    The clause carries the central S3 ambiguity on five vague
    determiners in one sentence: `relevant`, `sufficiently
    representative`, `to the best extent possible`, `free of
    errors`, `complete`. None of the five is anchored in the OJ.
    The hedge-AND coordination problem is the dominant unresolved
    parse-tree issue: the third coordinator `and to the best extent
    possible` introduces a soft hedge on what would otherwise be
    hard requirements, with two competing readings — either all
    five criteria are hedged under a permissive reading, or only
    the last two are hedged under a strict reading. The chosen
    reading is strict literal: the hedge binds only the last two
    criteria (`free of errors` and `complete`), so the first three
    (`relevant`, `sufficiently representative`, plus the structural
    `training, validation and testing data sets`) remain hard
    requirements. As an alternative, providers could read the hedge
    as binding all five criteria uniformly, relaxing the burden of
    strict representativeness. As a second alternative, the hedge
    could be read as binding only `free of errors`, with `complete`
    remaining a hard requirement. The poly-semous `representative`
    admits demographic, statistical and contextual senses; the
    chosen reading is literal and framework-agnostic, leaving the
    sense to provider interpretation. Remain open: (a) whether
    `free of errors` permits a residual error-rate budget (a small
    percentage of mislabelled examples) or requires zero-error
    perfect datasets that would be operationally infeasible at
    scale; (b) whether `complete` requires temporal completeness
    (full event coverage over time) or feature completeness (full
    population coverage across protected attributes).
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-006
  title: "Exceptional special-category data processing for bias correction"
  source_clauses:
    - { clause_id: AIA-C08, article_ref: "Art. 10(5) — `To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction … the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards … all the following conditions must be met: (a) … (f)`" }
  linked_objectives: [SO-AIACT-004]
  sub_domain: [D-05.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data" }
    - { id: PR.DS-01, title: "The confidentiality, integrity, and availability of data-at-rest are protected" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [PROVIDER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 10(5) of the AI Act creates an exceptional gateway that
    permits providers of high-risk AI systems to process special
    categories of personal data, as defined in Article 9(1) of
    Regulation (EU) 2016/679 (GDPR), to the extent strictly
    necessary for the purpose of ensuring bias detection and bias
    correction in their training, validation and testing data sets.
    The exception operates subject to appropriate safeguards for
    the rights and freedoms of natural persons, and is conditioned
    on the satisfaction of all six cumulative sub-conditions (a)
    through (f), which address necessity, scope, anonymisation,
    technical and organisational safeguards, supervisory oversight
    and a documentation duty. The clause is the principal locus
    where the AI Act deliberately crosses into GDPR territory, since
    the GDPR Article 9 general prohibition on processing
    special-category personal data would otherwise bar the data
    flows that AI bias-detection and correction require. The
    exception is narrow in formal terms but each of the six
    sub-conditions is qualitatively specified, leaving providers
    wide practical discretion on how to evidence compliance.
  security_rationale: |
    The obligation in Art. 10(5) is operationalised in NIST CSF
    2.0 through **PR.DS-12 (Data is managed consistent with the
    organization's risk strategy to protect the confidentiality,
    integrity, and availability of data)**, **PR.DS-01 (The
    confidentiality, integrity, and availability of data-at-rest
    are protected)**, and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including
    privacy and civil liberties obligations — are understood and
    managed)**. PR.DS-12 supplies the risk-aligned data-management
    substrate that the strict-necessity qualifier and the six
    cumulative sub-conditions require for lawful processing under
    the gateway. PR.DS-01 anchors data-at-rest integrity controls
    — including the pseudonymisation, differential-privacy and
    federated-learning techniques that constitute the
    state-of-the-art privacy-preserving measures referenced by the
    safeguards clause. GV.OC-03 supplies the legal-and-regulatory
    understanding substrate that the cross-regulation GDPR
    Article 9 interaction requires, ensuring that the
    strict-necessity and appropriate-safeguards qualifiers are
    operationalised against an understood legal baseline rather
    than as free-standing engineering decisions. A provider
    evidencing PR.DS-12 risk-aligned management, PR.DS-01
    data-at-rest integrity controls (including
    pseudonymisation/differential-privacy techniques) and
    GV.OC-03 legal-and-regulatory understanding demonstrates ex
    post that the Art. 10(5) exception is operationalised within
    the GDPR Article 9 boundary, with each of the six cumulative
    sub-conditions satisfied and the cross-regulation interplay
    documented for supervisory review.
  ambiguity_notes: |
    The clause carries the central S3 ambiguity on the phrase
    `strictly necessary`, which is a Berry-classic vague term
    familiar from GDPR Article 9(2) jurisprudence, and on
    `appropriate safeguards`, which is again undefined. The phrase
    `state-of-the-art security and privacy-preserving measures` is
    poly-semous, with possible readings as best practice,
    published standards or frontier research; the chosen reading
    is published standards, since that aligns with EU supervisory
    practice under GDPR and the EDPB guidance on state-of-the-art
    security measures. The six sub-conditions are AND-coordinated,
    so all six must be satisfied for the exception to apply.
    As an alternative reading, providers could interpret `strictly
    necessary` more permissively, allowing the exception where the
    bias-detection need is strong but not strictly indispensable.
    As a second alternative, `appropriate safeguards` could be
    read narrowly to require state-of-the-art pseudonymisation and
    differential-privacy techniques specifically, rather than any
    reasonable safeguard combination. The escape-clause qualifier
    `unless provided otherwise in the applicable Union or national
    law, in particular Union law on the protection of personal
    data` creates cross-regulation scope ambiguity with GDPR,
    since the GDPR's own Article 9(2) lawful bases continue to
    apply in parallel. Remain open: (a) whether the six
    sub-conditions are jointly exhaustive or whether additional
    procedural safeguards such as explicit data-subject
    notification or separate consent can be required by national
    supervisory authorities; (b) whether the phrase `state-of-the-art`
    aligns with the equivalent GDPR concept or diverges into a
    stricter AI-specific interpretation requiring frontier
    techniques such as differential privacy.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-014
  title: "Accuracy robustness and cybersecurity baseline across AI lifecycle"
  source_clauses:
    - { clause_id: AIA-C16, article_ref: "Art. 15(1) — `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle`" }
  linked_objectives: [SO-AIACT-009]
  sub_domain: [D-07.1, D-02.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.IR-03, title: "Mechanisms are put in place to achieve resilience requirements in normal and adverse situations" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 15(1) of Regulation (EU) 2024/1689 is the single provision
    that fuses three AI-technical properties — accuracy, robustness,
    and cybersecurity — into one continuous, lifecycle-wide duty of
    the high-risk AI provider. The provision applies from design
    through decommissioning and is read together with Recital 66,
    which clarifies that the three properties are to be interpreted
    in light of the system's intended purpose and the state of the
    art. The duty is articulated in 3-way AND form (the OJ does not
    contemplate partial compliance with two of the three properties),
    and is anchored in Title III Chapter 2 (Section 2 — Requirements
    for High-Risk AI Systems), placing it on the same legal plane as
    the data-governance, documentation, transparency, human-oversight
    and risk-management obligations of Arts. 10–14. The combined
    reading with the cross-cutting post-market monitoring obligation
    of Art. 72(1) means the provider must demonstrate — ex-ante
    (conformity assessment) and ex-post (post-market surveillance)
    — that the three properties are not merely aspirational at
    design time but are maintained throughout the AI system's
    lifecycle. A compliance officer should treat Art. 15(1) as the
    corner-stone substantive duty of the high-risk AI title, on par
    with Art. 9 (risk management) and Art. 10 (data governance).
  security_rationale: |
    The Art. 15(1) three-property duty is operationalised in NIST
    CSF 2.0 through **PR.PS-06 (Secure software development
    practices integrated across the SDLC)**, **PR.IR-03
    (Resilience mechanisms in normal and adverse situations)**,
    and **ID.RA-04 (Threat-impact prioritisation)**, with
    supplementary alignment to **GV.OV-02 (Strategy review
    against changing risk landscape)**, **PR.DS-02
    (Data-in-transit confidentiality, integrity, availability)**,
    and **ID.RA-01 (Vulnerability identification, validation,
    recording)**. PR.PS-06 anchors the SDLC substrate — secure
    coding, threat modelling, verification, change control — on
    which the three properties rest: an accuracy, robustness, or
    cybersecurity defect is most often a defect of process rigour.
    PR.IR-03 enforces the resilience dimension of robustness:
    failure-mode envelopes, graceful degradation, fail-safe
    patterns. ID.RA-04 supplies the risk-prioritisation
    discipline that converts the abstract duty into a ranked
    treatment set. GV.OV-02 closes the loop by requiring the
    provider to revisit the strategy when the threat landscape,
    the regulatory baseline, or the technology stack shifts,
    satisfying the lifecycle-consistency clause. PR.DS-02
    reinforces the cybersecurity property by binding data-in-
    transit CIA to the substrate, and ID.RA-01 records each
    identified vulnerability as evidence. Together these
    subcategories produce auditable artefacts — SDLC records,
    resilience test reports, risk register, strategy-review
    minutes — that enable the provider to demonstrate ex post
    to the conformity-assessment body and the market-
    surveillance authority that the three properties were
    maintained throughout the system lifecycle (Art. 9 + Art. 15
    + Art. 72 accountability chain).
  ambiguity_notes: |
    Source clause AIA-C16 carries three **S3** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.16). First, `appropriate level of accuracy,
    robustness, and cybersecurity` is VAG-3 — the three properties
    are each inquiry-resistant (Berry §5.1): `accuracy` has no OJ
    anchor for metric, threshold, or confidence level; `robustness`
    has no OJ anchor for the perturbation class; `cybersecurity`
    inherits the EU-level definitional gap that CRA C07
    (`cybersecurity` POLY) and NIS 2 C01 (`cybersecurity` POLY)
    also fail to close. Second, **POLY-S3** decomposes `accuracy`
    into R1 precision / R2 recall / R3 F1 / R4 calibration, and
    `robustness` into R1 distributional shift / R2 adversarial /
    R3 operational — the OJ does not pick. Third, **COORD-S2** on
    `accuracy, robustness AND cybersecurity` admits no partial
    compliance (2 of 3) reading, so the provider must address all
    three in parallel. The lifecycle-consistency clause
    (`perform consistently in those respects throughout their
    lifecycle`) is itself VAG+POLY: `consistently` is POLY between
    R1 same-as-design-time / R2 monotonic improvement / R3 no-
    degradation, and the OJ does not say which sense binds.
    Practical reading chosen (Berry §3.3.1): the three properties
    form an integrated engineering envelope, with the metric-set
    and the threshold-set disclosed in the technical documentation
    (Annex IV §2) and justified in the risk-management file
    (Art. 9). Remain open: (a) whether the supervisory authorities
    will accept any one of the four accuracy metrics in lieu of a
    metric-set, or require the full vector; (b) whether the
    `perform consistently` sense binds at design-time parity or at
    a no-degradation floor; (c) whether partial compliance (2 of 3
    properties) is ever tolerated in conformity-assessment practice.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

