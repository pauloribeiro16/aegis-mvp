---
document_id: AEGIS-PREPROC-GDPR-ART-35
title: GDPR Art. 35 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 35
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
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# GDPR Art. 35

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-004 | A process is established for regularly testing, assessing, and evaluating the effectiveness of technical and organisational measures for ensuring security of processing. | `GDPR-CP15` (Art. 32(1)(d)); `GDPR-CP22` (Art. 35(11)) | D-02.1, D-10.3 |
| SO-GDPR-004 (cross-ref) | Technical and organisational measures for ensuring security of processing are regularly tested, assessed, and evaluated for effectiveness (Art. 32(1)(d)); the DPIA is reviewed at least when there is a change of risk represented by processing operations (Art. 35(11)). | `GDPR-CP15` (Art. 32(1)(d)); `GDPR-CP22` (Art. 35(11)) | D-02.1, D-10.3 |
| SO-GDPR-004 | D-02.1, D-10.3 | Art. 32(1)(d), Art. 35(11) | Regular testing/assessing/evaluating security measures |
| SO-GDPR-028 | Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a data-protection impact assessment covering the four Art. 35(7) content items (systematic description, necessity & proportionality, risks, mitigation measures); the assessment is reviewed on change of risk. | `GDPR-CP21` (Art. 35(1)–(4)); `GDPR-CP22` (Art. 35(7)/(11)); `GDPR-C23` (Art. 9(2)(g)); `GDPR-CP23` (Art. 36(1)) | D-09.2 |
| SO-GDPR-028 | D-09.2 | Art. 35(1)–(4)/(7), Art. 9(2)(g), Art. 36(1) | Pre-launch DPIA for high-risk processing |

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
- sr_id: SR-GDPR-010
  title: "Minimised collection of identity verification data"
  source_clauses:
    - { clause_id: GDPR-RT04, article_ref: "Art. 12(6)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-005]
  sub_domain: [D-03.1, D-05.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 12(6) imposes identity-verification scope limitation through the general GDPR principle of data minimisation (Art. 5(1)(c)). The controller must request only the additional information necessary to confirm identity, not arbitrary identity documents. Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. The verification purpose is to confirm identity, so the data-minimisation test is calibrated to the identity-confirmation purpose: collect only what is necessary to confirm identity, not what would be ideal in a hypothetical stronger verification. The Art. 5(2) accountability burden shifts the demonstration duty to the controller: the controller must be able to justify the chosen verification scope.
  security_rationale: |
    The obligation in Art. 12(6), read with the Art. 5(1)(c) data-minimisation principle, to collect only the identity-verification information necessary to confirm the data subject is operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.AA-02 anchors the context-bound identity proofing that limits credential collection to what the interaction risk actually warrants, satisfying the Art. 5(1)(c) necessity test at the rights-request endpoint and preventing the verification step from accumulating identity documents that would enlarge the breach blast-radius.
    PR.DS-12 captures the policy-level data-management discipline that bounds the retention and scope of any verification artefact collected: a documented risk strategy governing how long verification data is held, who can access it, and when it is purged.
    The two subcategories together operationalise the graduated verification standard — low-risk requests with no additional collection, high-risk with bounded retention — that Art. 5(1)(c) imposes on Art. 12(6).
    A controller documenting PR.AA-02 proofing decisions, PR.DS-12 retention limits and the necessity justification per verification scope can demonstrate ex post, under the Art. 5(2) accountability burden, that identity-verification data collection was proportionate and minimised rather than opportunistically over-collected.
  ambiguity_notes: |
    `necessary` inherits VAG-S3 ambiguity from Art. 5(1)(c). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. The rule preserves the proportionate-necessary interpretation. An alternative reading treats necessity as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring the least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs (notably the CNIL) for sensitive-data contexts. The Art. 5(1)(c) necessary threshold varies with data sensitivity and breach impact; for Art. 9 special-category data, the controller may need stronger verification than for ordinary personal data. Remain open: whether automated identity-verification services (e.g. Jumio, Onfido) are themselves in scope as joint controllers under Art. 26, pending CJEU and EDPB guidance on AI-driven verification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-013
  title: "Privacy-by-default across collection, retention, and exposure"
  source_clauses:
    - { clause_id: GDPR-CP03, article_ref: "Art. 25(2) — privacy by default" }
    - { clause_id: GDPR-CP02, article_ref: "Art. 25(1) — privacy by design (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-007, SO-GDPR-024]
  sub_domain: [D-03.4, D-05.1]
  nist_csf_mapping:
    - { id: PR.PS-01, title: "Configuration management practices established and applied" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 25(2) obliges the controller to implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons. Art. 25(1) supplies the design-time counterpart (privacy by design) and Art. 5(1)(c) data minimisation supplies the underlying principle. Read together, the provisions establish that the default configuration of any processing system must minimise on four dimensions simultaneously: amount (collect only what is needed), extent (process only the operations needed), period (retain only as long as needed), accessibility (do not expose beyond the intended recipients).
  security_rationale: |
    The obligation in Art. 25(2), read with Art. 25(1) and Art. 5(1)(c), to configure processing systems so that by default only necessary personal data is processed is operationalised in NIST CSF 2.0 through **PR.PS-01 (Configuration management practices established and applied)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.PS-01 anchors the configuration-management baseline that sets the four default dimensions — amount collected, extent processed, retention period and accessibility — to their minimum-necessary values, satisfying the Art. 25(2) AND-coordinated default and ensuring the minimum is enforced as a system property rather than left to operator judgement.
    PR.DS-12 captures the policy-level data-management strategy that the defaults express: a documented risk-strategy positioning opt-in collection, opt-out for out-of-purpose operations, minimum-necessary retention and no public access unless explicitly granted.
    The two subcategories together operationalise the privacy-by-default pattern across all four Art. 25(2) dimensions simultaneously, so that relaxation requires affirmative data-subject intervention.
    A controller documenting PR.PS-01 default configurations, PR.DS-12 data-strategy and the per-system minimisation evidence can demonstrate ex post, under Art. 5(2), that the default state of every processing system was the minimum-necessary setting required by Art. 25(2).
  ambiguity_notes: |
    GDPR-CP03 (Art. 25(2)) carries VAG+COORD-S3 on `necessary for each specific purpose` and the four-element AND. Reading chosen: all four dimensions must individually be minimised and AND-coordinated. An alternative reading allowing some dimensions to be relaxed if others are tightened would weaken the default and is rejected. The AND reading is anchored to EDPB Guidelines 04/2019 on Article 25, which treat the four dimensions as independent minima. On "without the individual's intervention", the chosen reading treats the intervention requirement as the opt-in gate: the controller must not bypass the data subject's affirmative action to expose data. Remain open: (a) whether privacy-by-default applies to AI model defaults (e.g. opt-in vs opt-out for training-data inclusion), pending EDPB AI Act interaction guidance; and (b) whether the four-dimensional test applies per data subject or per processing activity, pending alignment with Art. 35 DPIA granularity.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-023
  title: "Pre-launch supervisory consultation on residual high risk"
  source_clauses:
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation" }
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — high-risk DPIA" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
  linked_objectives: [SO-GDPR-013, SO-GDPR-028]
  sub_domain: [D-04.3, D-09.2]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: ID.RA-06, title: "Risk responses chosen, prioritized, planned, tracked, communicated" }
  applies_to_role: [CONTROLLER, SUPERVISORY_AUTHORITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 36(1) requires the controller to consult the supervisory authority prior to processing where a data protection impact assessment under Art. 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk. Art. 35(1) supplies the DPIA trigger (high-risk processing), and Art. 35(7) supplies the DPIA content requirement (systematic description, necessity and proportionality assessment, risk assessment, mitigation measures). Art. 36(2) defines the supervisory authority's 8-week response obligation. Read together, the provisions establish a pre-launch gate: where DPIA identifies residual high risk after mitigation, the controller must consult the supervisory authority before launching the processing.
  security_rationale: |
    The obligation in Art. 36(1), read with Art. 35(1) and Art. 35(7), to consult the supervisory authority before launching processing that retains residual high risk after DPIA mitigation is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements understood and managed)** and **ID.RA-06 (Risk responses chosen, prioritized, planned, tracked, and communicated)**.
    GV.OC-03 anchors the governance layer that recognises the prior-consultation duty as a legal-regulatory requirement to be managed, satisfying the Art. 36(1) pre-launch-gate status and ensuring the consultation is scheduled into the launch timeline rather than treated as optional, with the Art. 36(2) eight-week supervisory window accommodated.
    ID.RA-06 captures the risk-response leg: the residual risk that survives the Art. 35(7) DPIA mitigation assessment is explicitly chosen, prioritised, planned, tracked and communicated to the authority, with the DPIA content (systematic description, necessity and proportionality, risk assessment, mitigation measures) supplying the evidence base.
    The two subcategories together operationalise the structured risk-response communication that the prior-consultation gate represents, distinguishing it from post-launch incident reporting.
    A controller documenting GV.OC-03 consultation records and ID.RA-06 residual-risk decisions can demonstrate ex post, under Art. 5(2), that the pre-launch engagement occurred before processing began and that the residual-risk justification was transparent.
  ambiguity_notes: |
    `high risk in the absence of measures` is the same `high risk` POLY family as Arts. 34 and 35. Readings converge via the Art. 35(1) threshold inheritance. The `prior to processing` wording is read strictly: the controller must consult before launching, not after, and the supervisory authority's 8-week window under Art. 36(2) must be accommodated in the launch timeline. EDPB Guidelines 4/2019 on DPIA provide factors for high-risk classification but do not bind the controller. Remain open: (a) whether iterative processing activities (e.g. machine-learning model updates) trigger fresh Art. 36(1) consultations on each iteration or whether a single consultation covers the iterative cycle, pending EDPB AI Act interaction guidance; and (b) how the consultation interacts with the Art. 27 representative designation for non-EU controllers, pending alignment with international supervisory cooperation.
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
- sr_id: SR-GDPR-045
  title: "Pre-launch DPIA with risk treatment and prior-consultation trigger"
  source_clauses:
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — DPIA trigger" }
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(7) — DPIA content" }
    - { clause_id: GDPR-CP23, article_ref: "Art. 36(1) — prior consultation (cross)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data" }
  linked_objectives: [SO-GDPR-028]
  sub_domain: [D-09.2]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-05, title: "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED, PERIODIC]
  regulatory_rationale: |
    Art. 35(1) requires the controller to carry out an assessment of
    the impact of the envisaged processing operations on the protection
    of personal data, prior to processing, where the processing is
    likely to result in a high risk to the rights and freedoms of
    natural persons, in particular using new technologies. Art. 35(7)
    specifies the four content items: a systematic description of the
    processing and purposes; an assessment of necessity and
    proportionality; an assessment of the risks to data-subject
    rights; and the measures envisaged to address the risks. Art. 36(1)
    requires prior consultation with the supervisory authority where
    the DPIA indicates that processing would result in a high risk in
    the absence of mitigation measures. Art. 4(1) supplies the personal-
    data definition on which the DPIA scope rests.
  security_rationale: |
    The obligation in Art. 35(1), Art. 35(7) and Art. 36(1) to carry out a pre-launch data-protection impact assessment for processing likely to result in a high risk, covering the four Art. 35(7) content items, and to consult the supervisory authority where the residual risk remains high, is operationalised in NIST CSF 2.0 through **ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded)**, **ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response decisions)** and **ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated)**.
    ID.RA-01 captures the asset-level vulnerability-recording discipline: the DPIA's systematic-description requirement (Art. 35(7)(a)) is operationally the same as the vulnerability-recording posture that the controller maintains for the data, processing and supporting assets under assessment.
    ID.RA-05 captures the inherent-risk understanding requirement in Art. 35(7)(c): threats (including new-technology exposures), vulnerabilities, likelihoods and impacts must be brought together to understand the inherent risk envelope of the processing, before any risk-response measure is layered on top.
    ID.RA-06 captures the risk-response layer in Art. 35(7)(d) and Art. 36(1): the controller must choose, prioritise, plan and track the measures that address the identified risks, and where residual risk stays high the prior-consultation obligation under Art. 36(1) is triggered, with the supervisory authority becoming the next-step risk-response stakeholder.
    A controller that documents ID.RA-01 vulnerability coverage, ID.RA-05 inherent-risk assessment and ID.RA-06 risk-response selection plus Art. 36(1) consultation trigger can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any high-risk processing the controller had performed and refreshed the four-part DPIA and consulted the supervisory authority where the threshold was met.
  ambiguity_notes: |
    Source clause GDPR-CP21 carries Berry-flagged S3 POLY+VAG on `new
    technologies` and `high risk` (Berry §5.1, §3.3.1). `New
    technologies` is the recurring time-dependent phrase — was cloud
    `new` in 2018, is generative AI `new` in 2026. The reading adopted
    for this SR is that `new technologies` means technologies not
    widely deployed in the industry at the time of assessment (EDPB
    Guidelines 4/2019). `High risk` inherits the Art. 35(1) threshold,
    with the EDPB Guidelines 4/2019 nine-criteria list as the
    operational anchor (evaluation and scoring, automated decision-
    making with legal effect, systematic monitoring, sensitive data or
    data of a vulnerable nature, data processed on a large scale,
    combination of data, data concerning vulnerable data subjects,
    innovative use or applying new technological or organisational
    solutions, and processing that prevents data subjects from
    exercising a right or using a service). Two alternative readings
    remain. First, a strict supervisory-list reading would limit DPIA
    triggers to those listed by the national supervisory authority
    under Art. 35(4); this conflicts with Art. 35(1), which is open-
    textured. Second, a controller-discretion reading that treats the
    EDPB criteria as illustrative would weaken the high-risk threshold.
    Remain open: (a) whether generative-AI model training falls inside
    or outside `new technologies` in 2026; (b) whether a single DPIA
    may legitimately cover a set of similar processing operations per
    Art. 35(1) when the operations span multiple controllers in a
    joint-controllership arrangement.
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
- sr_id: SR-GDPR-047
  title: "Risk-change-triggered DPIA review with periodic cadence"
  source_clauses:
    - { clause_id: GDPR-CP22, article_ref: "Art. 35(11) — DPIA review" }
    - { clause_id: GDPR-CP21, article_ref: "Art. 35(1) — DPIA trigger" }
  linked_objectives: [SO-GDPR-028, SO-GDPR-004]
  sub_domain: [D-09.2, D-10.3]
  nist_csf_mapping:
    - { id: ID.IM-04, title: "Cybersecurity risk management improvements are informed by awareness of related developments and context (e.g., threat intelligence, incidents, technology evolution)" }
    - { id: ID.RA-06, title: "Risk responses are chosen, prioritized, planned, tracked, and communicated" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PERIODIC, TRIGGERED]
  regulatory_rationale: |
    Art. 35(11) requires the controller, where necessary, to carry out
    a review to assess whether processing is performed in accordance
    with the data protection impact assessment at least when there is a
    change of the risk represented by processing operations. The
    provision triggers DPIA re-review on material risk change and links
    back to Art. 35(1)'s DPIA-trigger framework.
  security_rationale: |
    The obligation in Art. 35(11), read with Art. 35(1), to carry out a DPIA review where necessary, and at least when there is a change of the risk represented by the processing operations, is operationalised in NIST CSF 2.0 through **ID.IM-04 (Cybersecurity risk management improvements are informed by awareness of related developments and context, e.g. threat intelligence, incidents, technology evolution)** and **ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated)**.
    ID.IM-04 captures the forward-looking-improvement discipline: DPIA review is triggered not only by the controller's static risk picture but by contextual changes — threat-intelligence shifts, incidents in the wider environment, technology evolution — that the controller must bring into its improvement process and reflect in the DPIA's risk assessment.
    ID.RA-06 captures the risk-response-rerun layer: when a material change in risk is detected, the controller's risk-response set must be revisited — chosen, re-prioritised, re-planned, tracked against the new risk picture and communicated — so that the DPIA's measures-envisaged section stays current with the live risk envelope of the processing.
    A controller that documents ID.IM-04 contextual-change monitoring and ID.RA-06 risk-response-rerun cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any material change in the risk the DPIA had been refreshed and the measures it envisages had been re-evaluated rather than carried over unchanged.
  ambiguity_notes: |
    `where necessary` carries Berry-flagged VAG without an explicit S3
    tag in the chapter-4 analysis, and the same compliance practice
    applies across readings. The reading adopted for this SR treats
    material change in risk as the primary trigger, supplemented by
    periodic review (annual). An alternative reading under which only
    annual review applies would satisfy the periodic-review obligation
    but lose responsiveness to material change. Remain open: whether
    the change-of-risk trigger requires the controller to re-perform
    the full Art. 35(7) content set or to update only the changed
    dimensions.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-064
  title: "Advisory, monitoring and assurance delivered by DPO function"
  source_clauses:
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(1)(a)–(e) — DPO tasks" }
    - { clause_id: GDPR-CP28, article_ref: "Art. 39(2) — risk-associated processing" }
  linked_objectives: [SO-GDPR-037, SO-GDPR-025]
  sub_domain: [D-09.1, D-09.2, D-08.1]
  nist_csf_mapping:
    - { id: GV.OV-03, title: "Organizational cybersecurity performance evaluated and reviewed" }
    - { id: PR.AT-02, title: "All workforce understand their role-specific security responsibilities" }
    - { id: ID.IM-02, title: "Improvement processes implemented across organizational tiers" }
  applies_to_role: [DPO]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 39(1) requires the DPO to have at least the following tasks: (a) inform and advise the controller, the processor and employees on their GDPR obligations; (b) monitor compliance, including assignment of responsibilities, awareness-raising and training, and related audits; (c) provide advice where requested on data protection impact assessments and monitor their performance pursuant to Art. 35; (d) cooperate with the supervisory authority; (e) act as the contact point for the supervisory authority on processing issues, including Art. 36 consultation. Art. 39(2) requires that the DPO have due regard to the risk associated with processing operations, taking into account the nature, scope, context and purposes of processing.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — to provide advice where requested as regards the data protection impact assessment and monitor its performance pursuant to Article 35]
  security_rationale: |
    The obligation in Art. 39(1)(a)–(e) and Art. 39(2) is operationalised in NIST
    CSF 2.0 through **GV.OV-03 (Organizational cybersecurity performance evaluated
    and reviewed for needed adjustments)**, **PR.AT-02 (All members of the
    organization's workforce understand their roles and responsibilities in
    achieving the organization's cybersecurity objectives)** and **ID.IM-02
    (Improvement processes for cybersecurity risk management implemented across
    organizational tiers)**.

    GV.OV-03 controls the monitoring and audit dimension of the DPO role under
    Art. 39(1)(b): the DPO evaluates organisational compliance with the GDPR,
    assigns responsibilities, and runs the related audits, with the performance
    review feeding back into management. PR.AT-02 controls the awareness-raising
    and training dimension under Art. 39(1)(b): the workforce must understand its
    role-specific responsibilities, with the DPO orchestrating the curricula.
    ID.IM-02 controls the continuous-improvement dimension under Art. 39(1)(c):
    DPIA advice and monitoring drive improvement processes across organisational
    tiers, scaled to the risk associated with processing operations under Art.
    39(2).

    Together the three subcategories embed the DPO as the privacy-and-security
    assurance function across evaluation (GV.OV-03), awareness (PR.AT-02) and
    improvement (ID.IM-02), enabling ex-post demonstration through an annual
    report to the highest management level that the advisory, monitoring and
    assurance tasks were performed and that the resulting improvements were
    adopted.
  ambiguity_notes: |
    The five-element AND-list under Art. 39(1)(a)–(e) is COORD-S2: all five tasks are mandatory and the DPO must be in a position to perform each of them. The where-requested qualifier on Art. 39(1)(c) is a request-trigger qualifier on the advisory task, while monitor its performance is a continuous obligation; the two are separate and not interchangeable. Due regard to the risk in Art. 39(2) is VAG-S2; both readings converge on a risk-proportionate DPO-task practice in which the DPO prioritises and scales effort according to the assessed risk of the processing operations at issue. Remain open: (a) whether the where-requested qualifier on Art. 39(1)(c) advisory applies per DPIA or per controller; (b) whether awareness-raising under Art. 39(1)(b) must include role-specific curricula per processing role, or whether generic privacy-awareness content satisfies the obligation.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

