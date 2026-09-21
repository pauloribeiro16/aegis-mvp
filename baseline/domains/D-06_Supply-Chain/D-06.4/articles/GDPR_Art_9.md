---
document_id: AEGIS-PREPROC-GDPR-ART-9
title: GDPR Art. 9 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 9
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# GDPR Art. 9

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-016 | Personal data are processed lawfully, fairly, and in a transparent manner, on the basis of one of the six Art. 6(1) lawfulness bases (or one of the Art. 9(2) bases for special categories). | `GDPR-CL01` (Art. 5(1)(a)/(b)); `GDPR-CL08–CL13` (Art. 6(1)(a)–(f)); `GDPR-CL21` (Art. 9(1) prohibition + exceptions) | D-05.1, D-09.1 |
| SO-GDPR-016 | D-05.1, D-09.1 | Art. 5(1)(a)/(b), Art. 6(1)(a)–(f), Art. 9(1) | Lawfulness, fairness, transparency; legal-basis selection |
| SO-GDPR-028 | Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a data-protection impact assessment covering the four Art. 35(7) content items (systematic description, necessity & proportionality, risks, mitigation measures); the assessment is reviewed on change of risk. | `GDPR-CP21` (Art. 35(1)–(4)); `GDPR-CP22` (Art. 35(7)/(11)); `GDPR-C23` (Art. 9(2)(g)); `GDPR-CP23` (Art. 36(1)) | D-09.2 |
| SO-GDPR-028 | D-09.2 | Art. 35(1)–(4)/(7), Art. 9(2)(g), Art. 36(1) | Pre-launch DPIA for high-risk processing |
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
- sr_id: SR-GDPR-019
  title: "High-risk breach communication to affected data subjects"
  source_clauses:
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk breach communication to data subject" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(2) — content of communication" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration (cross)" }
  linked_objectives: [SO-GDPR-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated stakeholders per information-sharing rules" }
    - { id: RS.CO-04, title: "Coordination with stakeholders consistent with applicable rules" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(1) requires the controller to communicate a personal data breach to the data subject without undue delay when the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons. Art. 34(2) requires the communication to describe in clear and plain language the nature of the personal data breach and contain at least the information and measures referred to in points (b), (c) and (d) of Art. 33(3). Art. 32(2) anchors the risk-enumeration vocabulary (destruction, loss, alteration, unauthorised disclosure of, or access to) underlying the high-risk assessment. Read together, the provisions establish a higher threshold (high risk to data subjects' rights) than the supervisory-authority notification (Art. 33, risk to data subjects' rights), and a content requirement scoped to the data subject rather than the supervisory authority.
  security_rationale: |
    The obligation in Art. 34(1), read with Art. 34(2) and Art. 32(2), to communicate a high-risk breach to affected data subjects in clear and plain language is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information shared with designated stakeholders per information-sharing rules)** and **RS.CO-04 (Coordination with stakeholders consistent with applicable rules)**.
    RS.CO-03 anchors the information-sharing mechanism that delivers the Art. 34(2) content — nature of the breach, likely consequences, measures taken — to the data subjects whom the rules designate as the entitled stakeholders, satisfying the higher Art. 34 threshold that sits above the Art. 33 supervisory-notification trigger.
    RS.CO-04 captures the coordination discipline that multi-channel notification (direct communication, prominent website notice and, where appropriate, public communication) requires, ensuring the communication achieves equally effective reach and that the high-risk classification decision tree is documented.
    The two subcategories together operationalise the data-subject-facing leg of breach response, distinct from the authority-facing leg, enabling individual protective action such as account rotation and fraud-alert subscription.
    A controller documenting RS.CO-03 notification records, RS.CO-04 channel-choice evidence and the high-risk assessment per EDPB Guidelines 9/2022 can demonstrate ex post, under Art. 5(2), that affected data subjects received timely, intelligible notice enabling protective action.
  ambiguity_notes: |
    `likely to result in a high risk` carries POLY+VAG-S3 (the three-tier `risk`/`high risk`/`high risk` architecture across Arts. 33, 34, 35). Reading chosen: the Art. 34 threshold is higher than the Art. 33 threshold — objectively elevated above ordinary processing risk, per EDPB Guidelines 9/2022. An alternative reading treating the threshold as severe impact on data subject's rights, per CNIL guidance, is operationally similar but framing-different. The chosen reading treats the threshold as risk-of-significant-harm, not merely risk-of-any-harm; the controller documents the risk assessment with reference to the data categories (Art. 9 special categories raise the threshold), the data-subject population (vulnerable populations raise the threshold), and the breach characteristics (encrypted vs plaintext, contained vs ongoing). Remain open: (a) whether `clear and plain language` requires a CEFR B1 reading-age standard or whether national DPA guidance is acceptable, pending EDPB harmonisation; and (b) whether the Art. 34 communication can be combined with Art. 33 notification to the supervisory authority, or must be a separate communication, pending EDPB Guidelines 9/2022 clarification.
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
- sr_id: SR-GDPR-028
  title: "Heightened handling for nine special-category personal-data classes"
  source_clauses:
    - { clause_id: GDPR-CL21, article_ref: "Art. 9(1) — special-category prohibition" }
    - { clause_id: GDPR-CL22, article_ref: "Art. 9(2)(a) — explicit consent" }
    - { clause_id: GDPR-C23, article_ref: "Art. 9(2)(g) — substantial public interest (cross)" }
  linked_objectives: [SO-GDPR-016]
  sub_domain: [D-09.1, D-05.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CATEGORY]
  regulatory_rationale: |
    Art. 9(1) prohibits processing of the nine enumerated special
    categories of personal data, namely racial or ethnic origin,
    political opinions, religious or philosophical beliefs, trade union
    membership, genetic data, biometric data for the unique identification
    of a natural person, health data and data concerning sex life or
    sexual orientation, unless and until one of the ten Art. 9(2)
    exceptions applies (Recital 51; Recital 52). The Art. 9(2)(a)
    exception requires explicit consent, the Art. 9(2)(g) exception
    requires a substantial public-interest basis grounded in Union or
    Member State law, and the Art. 9(2)(j) statistical and archiving
    exception is bounded by Art. 89(1) safeguards. Each special category
    is distinct and conjunctive — the nine prohibited categories each
    independently trigger Art. 9(1). The Art. 9(2)(a) `explicit` qualifier
    on consent sits in addition to the Art. 4(11) `specific, informed,
    freely given and unambiguous` baseline.
  security_rationale: |
    The obligation in Art. 9(1), Art. 9(2)(a) and Art. 9(2)(g) to gate the nine special-category data classes behind one of ten enumerated exceptions, with heightened handling for biometric-for-unique-identification and other intrinsically sensitive classes, is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    GV.OC-03 captures the per-class exception-tracking discipline: the controller must record which of the ten Art. 9(2) exceptions underpins each special-category flow, treating the nine Art. 9(1) categories as independently gated, and must hold the Art. 9(2)(a) explicit-consent artefact to the heightened standard that sits above the Art. 4(11) baseline.
    PR.DS-12 captures the differentiated-handling posture that special-category data warrants: narrower access permissions, stronger purpose-binding, enhanced logging, additional encryption or pseudonymisation layer, and stricter retention, all aligned with a risk strategy that weights each of the nine classes against the elevated harm envelope the Art. 9 prohibition presupposes.
    A controller that documents GV.OC-03 exception-per-class coverage and PR.DS-12 risk-stratified handling for each category can demonstrate ex post, against the Art. 5(2) accountability duty, that no special-category flow operated without an identified Art. 9(2) exception and the heightened controls the category warrants on the day of any supervisory inspection.
  ambiguity_notes: |
    Source clause GDPR-CL21 carries Berry-flagged POLY+COORD-S3 because
    nine special categories are conjunctive, each category independently
    engaging Art. 9(1) and each exception in Art. 9(2) being read in light
    of every category it is invoked for. The Art. 9(2)(a) `explicit
    consent` qualifier carries POLY-S3 against the Art. 4(11) `specific`
    consent baseline, since explicit adds a written or equally
    unambiguous formal-act requirement on top of the freely-given,
    specific, informed and unambiguous quartet. The reading adopted for
    this SR treats the nine Art. 9(1) categories as distinct (each
    independently engages Art. 9(1)) and treats `explicit consent` for
    special categories as requiring a written, separately captured
    consent under EDPB Guidelines 05/2020 on consent (strict reading).
    Two alternative readings remain. First, an integrative reading that
    bundles all nine categories into a single `sensitive-data` flag would
    lose the biometric-for-unique-identification nuance (which excludes
    ordinary biometric verification). Second, a functional reading of
    `explicit` that accepts an electronic confirmation as equivalent to
    written consent without distinguishing the special-category context
    would weaken the heightened standard the Art. 9(2)(a) qualifier
    imposes. Remain open: (a) whether biometric processing for security
    authentication (not unique identification) is captured by Art. 9(1);
    (b) whether `explicit consent` requires a paper signature or accepts
    a recorded electronic confirmation for online special-category
    collection.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-038
  title: "Written EU representative for non-EU controllers and processors"
  source_clauses:
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(1) — designate in writing" }
    - { clause_id: GDPR-CP06, article_ref: "Art. 27(2)(a) — occasional exception" }
  linked_objectives: [SO-GDPR-023]
  sub_domain: [D-06.4, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-02, title: "Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered" }
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
  applies_to_role: [NON_EU_CONTROLLER, NON_EU_PROCESSOR]
  obligation_type: [CONTINUOUS, PER-PROCESSING-ACTIVITY]
  regulatory_rationale: |
    Art. 27(1) requires, where Art. 3(2) applies (offering goods or
    services to EU data subjects, or monitoring their behaviour,
    regardless of whether the processing takes place in the Union), the
    controller or processor to designate in writing a representative in
    the Union. Art. 27(2)(a) provides the exception for processing which
    is occasional, does not include, on a large scale, processing of
    special categories of data as referred to in Art. 9(1) or processing
    of personal data relating to criminal convictions and offences
    referred to in Art. 10, and is unlikely to result in a risk to the
    rights and freedoms of natural persons, taking into account the
    nature, context, scope and purposes of the processing. Art. 27(2)(b)
    carves out public authorities or bodies.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or processing of personal data relating to criminal convictions and offences referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons]
  security_rationale: |
    The obligation in Art. 27(1) and Art. 27(2)(a) for any non-EU controller or processor covered by Art. 3(2) to designate in writing a Union-based representative, unless the conjunctive occasional, small-scale, low-risk exception is satisfied, is operationalised in NIST CSF 2.0 through **GV.OC-02 (Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risks are understood and considered)** and **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced)**.
    GV.OC-02 captures the stakeholder-recognition discipline: the non-EU controller treats EU data subjects, supervisory authorities and the designated representative as standing stakeholders whose needs (point of contact, address for enforcement, language of communication) must be understood and documented before processing begins, so that the representative function is operationally real rather than a paper address.
    GV.RR-02 captures the role-accountability discipline: the representative role carries authorities and responsibilities for handling supervisory-authority correspondence, data-subject requests and incident notifications, with the mandate of Art. 27(1) made enforceable through documented communication channels and refusal-to-act safeguards.
    A non-EU controller that documents GV.OC-02 stakeholder identification and GV.RR-02 representative-mandate clarity can demonstrate ex post, against the Art. 5(2) accountability duty read with the Art. 3(2) jurisdictional anchor, that on the day of any supervisory action the designated representative was operationally present and properly authorised.
  ambiguity_notes: |
    `occasional`, `large scale` and `unlikely to result in a risk` (Art.
    27(2)(a)) carry VAG+SCOPE-Q S3 (Berry §5.1): three inquiry-resistant
    qualifiers combined with AND. The exception requires all three to be
    in the controller's favour for the exception to apply — i.e.,
    occasional AND small-scale AND low-risk — and the OJ additionally
    ties `large scale` to the special-category and criminal-conviction
    carve-outs. The reading adopted for this SR is the conjunctive
    reading: each qualifier must hold individually; `occasional` is read
    as not regular or periodic (EDPB Guidelines 3/2018); `large scale`
    follows the EDPB Guidelines 9/2022 factors (number of data subjects,
    volume of data, geographic range, duration); and `unlikely` is read
    as non-negligible risk absent. Two alternative readings remain.
    First, a disjunctive reading under which any one of the three would
    suffice to trigger the exception would conflict with the OJ text,
    which is conjunctive (the negative construction `shall not apply`
    applies only when all three conditions hold). Second, a literal-
    procedural reading that treats `unlikely` as `more probable than
    not` would expand the exception inappropriately. Remain open: (a)
    whether a SaaS offering with a freemium tier counts as `occasional`
    when only a small fraction of EU users sign up; (b) whether
    behavioural monitoring of EU employees of a non-EU employer triggers
    Art. 27 irrespective of the exception's `risk` prong.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-053
  title: "Explicit elevated consent for special-category processing"
  source_clauses:
    - { clause_id: GDPR-CL22, article_ref: "Art. 9(2)(a) — explicit consent for special categories" }
    - { clause_id: GDPR-CL21, article_ref: "Art. 9(1) — special-category prohibition (cross)" }
    - { clause_id: GDPR-C05, article_ref: "Art. 4(11) — consent definition (cross)" }
  linked_objectives: [SO-GDPR-032]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: UNMAPPED_CSF, title: "Special-category consent is a GDPR-specific construct; nearest reference is NIST Privacy Framework Category-P" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-CATEGORY-CONSENT]
  regulatory_rationale: |
    Art. 9(1) prohibits the processing of special categories of personal data unless one of the Art. 9(2) grounds applies. Art. 9(2)(a) lifts the prohibition where the data subject has given explicit consent to the processing of those personal data for one or more specified purposes, unless Union or Member State law provides that the Art. 9(1) prohibition may not be lifted by the data subject. The explicit qualifier is stronger than the Art. 4(11) specific qualifier and operates on top of the Art. 4(11) four-element test rather than replacing it (Recital 32; EDPB Guidelines 05/2020 §3.4 on the explicit-versus-specific escalation). Art. 9 also prohibits processing of data relating to criminal convictions and offences except under Member State law with specific safeguards (Art. 10), and the explicit-consent route under Art. 9(2)(a) is generally not available for criminal-conviction data, which must rely on Art. 10 Member State law instead. The result is a two-track special-category regime: explicit consent for sensitive personal data under Art. 9(2)(a), and statutory authorisation for criminal-conviction data under Art. 10, with no overlap.
  security_rationale: |
    The obligation in Art. 9(2)(a) has no direct NIST CSF 2.0 subcategory and is
    anchored on the closest fit **PR.AA-02 (Identities proofed and bound to
    credentials based on the context of interactions)** within the broader
    **PR.AA — Identity, Authentication, and Access Control** category; the
    residual gap is noted as UNMAPPED_CSF.

    PR.AA-02 controls risk-stratified identity proofing: higher-assurance
    contexts warrant stronger proofing, in the same way that high-value
    transactions warrant multi-factor authentication rather than password-only
    proofing. Special-category consent is the GDPR's strongest data-subject-
    intent authentication, and PR.AA-02's context-sensitive proofing model
    captures the engineering pattern even though no CSF subcategory enumerates
    the Art. 4(11)-vs-Art. 9(2)(a) escalation ladder. The natural broader
    reference for consent-as-control is the NIST Privacy Framework
    (Category-P), which is outside this pre-processing pass.

    Because the CSF gap is documented, the controller must supplement PR.AA-02
    with a GDPR-specific consent-artefact design: a separate, uncombined,
    express-statement consent record for each special-category purpose, retained
    for supervisory-authority inspection. Accountability is sustained through the
    documented gap (UNMAPPED_CSF + unmapped_csf_justification) plus the PR.AA-02
    identity-binding trail that proves each special-category consent was
    collected above the Art. 4(11) baseline.
  ambiguity_notes: |
    Explicit versus specific carries POLY-S3 because the OJ text of Art. 9(2)(a) does not define explicit and Art. 4(11) does not define specific, leaving the boundary unclear. Reading chosen: explicit requires a separate, unambiguous statement on the special-category processing, not bundled with any other consent and not satisfied by inference or pre-ticked boxes, per EDPB Guidelines 05/2020 §3.4 (which interprets explicit as an additional layer on top of the Art. 4(11) specific requirement, requiring that the data subject gives the consent by means of an express statement). An alternative reading treats explicit as a synonym for specific, in which case any Art. 4(11)-compliant consent would suffice for special-category processing; this reading is rejected because it would render Art. 9(2)(a) redundant and is inconsistent with EDPB §3.4. A second alternative reading limits the Art. 9(2)(a) consent to a written-and-signed declaration, excluding electronic confirmations; this reading is rejected because Art. 9(2)(a) does not impose a form requirement and EDPB §3.4 treats electronic confirmation as equally valid provided the explicit-statement condition is met. Remain open: (a) whether a written declaration signed in advance and explicitly invoking special-category processing satisfies Art. 9(2)(a) without a fresh per-purpose confirmation; (b) whether Member State law that purports to make the Art. 9(1) prohibition non-liftable by consent (per the Art. 9(2)(a) proviso) applies symmetrically across Member States or only within the Member State that enacted it.
  unmapped_csf_justification: |
    Special-category consent is a GDPR-specific construct (Art. 9
    vs Art. 4(11)) with no direct CSF 2.0 Subcategory. Closest
    CSF match is PR.AA-02; NIST Privacy Framework is the natural
    broader reference. Marked UNMAPPED_CSF.
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

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-057
  title: "Derogation-based transfer fallback under strict preconditions"
  source_clauses:
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit consent" }
    - { clause_id: GDPR-TR09, article_ref: "Art. 49(1)(d) — important public interest" }
    - { clause_id: GDPR-TR10, article_ref: "Art. 49(1) second subparagraph — catch-all" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: UNMAPPED_CSF, title: "Derogation under Art. 49 is GDPR-specific with no clean CSF 2.0 mapping" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER, ONE_TIME]
  regulatory_rationale: |
    Art. 49 derogations apply only in the absence of an adequacy decision under Art. 45(3) and of appropriate safeguards under Art. 46, including binding corporate rules. Art. 49(1) lists seven disjunctive grounds: explicit consent after being informed of possible risks; necessity for the performance of a contract between the data subject and the controller or implementation of pre-contractual measures at the data subject's request; necessity for a contract concluded in the interest of the data subject between the controller and another natural or legal person; important reasons of public interest; establishment, exercise or defence of legal claims; protection of the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent; transfer from a register intended to provide information to the public (Recital 111–115). The second subparagraph of Art. 49(1) adds a catch-all: transfers may take place where the transfer is not repetitive, concerns a limited number of data subjects, is necessary for compelling legitimate interests of the controller which are not overridden by the interests, rights or freedoms of the data subject, and the controller has assessed all the circumstances and put in place suitable safeguards (Recital 113).
  security_rationale: |
    The obligation in Art. 49(1)(a), Art. 49(1)(d) and Art. 49(1) second
    subparagraph has no clean NIST CSF 2.0 subcategory and is anchored on the
    closest fit **GV.OC-03 (Legal, regulatory, and contractual requirements
    regarding cybersecurity — including privacy and civil liberties obligations —
    are understood and managed)** within the broader **GV.OC — Organizational
    Context** category; the residual gap is noted as UNMAPPED_CSF.

    GV.OC-03 controls the controller's understanding of the regulatory
    preconditions on which any Art. 49 derogation depends — absence of an
    adequacy decision under Art. 45(3), absence of Art. 46 appropriate
    safeguards, and satisfaction of one of the seven enumerated grounds or the
    catch-all (not repetitive, limited number of data subjects, compelling
    legitimate interests, suitable safeguards). CSF 2.0 does not enumerate
    derogation-availability analysis and GV.OC-03 is a poor fit because it is
    designed for ongoing regulatory understanding rather than exception-
    availability gating, but it is the closest available anchor.

    Because the CSF gap is documented, the controller must supplement GV.OC-03
    with a GDPR-specific derogation-use register that records each catch-all
    reliance, the compelling-interests analysis, and the suitable safeguards
    deployed. Accountability is sustained through the documented gap
    (UNMAPPED_CSF + unmapped_csf_justification) and through GV.OC-03's
    regulatory-understanding trail that demonstrates the derogation fallback was
    used only where adequacy and Art. 46 safeguards were unavailable.
  ambiguity_notes: |
    Explicitly (Art. 49(1)(a)) carries POLY-S3 against the specific qualifier of Art. 4(11) and the explicit qualifier of Art. 9(2)(a); reading chosen: the strongest consent form, risk-informed and documented, building on EDPB Guidelines 05/2020 §3.4 and the Schrems II framing of risk disclosure. The catch-all qualifiers not repetitive, limited number, compelling legitimate interests, suitable safeguards carry VAG-S3 and SCOPE-Q-S3 because none of them is quantitatively bounded in the OJ text; compelling in particular carries POLY-S3 across Art. 21(1) and Art. 49(1) (Recital 47 cross-reference), and the EDPB Guidelines 2/2018 emphasise that compelling means more than legitimate and approaches necessity. An alternative reading confines the catch-all to transfers that are truly exceptional and treats recurring or systematic reliance on it as a structural misuse of the derogation; this reading is consistent with that framing and operationally shifts the burden onto the controller to demonstrate the exceptional nature of each catch-all reliance. A second alternative reading treats not repetitive as a per-data-subject test rather than per-data-flow; this reading is harder to operationalise and is inconsistent with the structural purpose of the catch-all. Remain open: (a) whether repetitive in the catch-all should be measured per data subject, per transfer, or per data flow, given that no OJ anchor specifies the unit; (b) whether suitable safeguards in the catch-all may be purely contractual or must include technical measures (encryption, pseudonymisation) per Schrems II §134.
  unmapped_csf_justification: |
    The four Art. 49 catch-all conjunctive qualifiers and the
    `compelling legitimate interests` qualifier have no clean CSF 2.0
    Subcategory. The closest mapping GV.OC-03 is a poor fit.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-062
  title: "DPO designation triggered by processing profile"
  source_clauses:
    - { clause_id: GDPR-CP25, article_ref: "Art. 37(1)(a)/(b)/(c) — DPO designation triggers" }
  linked_objectives: [SO-GDPR-037]
  sub_domain: [D-09.1, D-09.2]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles/responsibilities/accountabilities established and communicated" }
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 37(1) requires the controller and the processor to designate a data protection officer in any case where: (a) the processing is carried out by a public authority or body, regardless of the nature of the processing carried out; (b) the core activities of the controller or the processor consist of processing operations which, by virtue of their nature, their scope and/or their purposes, require regular and systematic monitoring of data subjects on a large scale; or (c) the core activities of the controller or the processor consist of processing on a large scale of special categories of data pursuant to Art. 9 or of personal data relating to criminal convictions and offences. The designation is mandatory where any of the three triggers applies; voluntary designation is permitted under Art. 37(4) and is treated equivalently under the WP29 and EDPB Guidelines 3/2018, with the designation made public under Art. 37(7).
  security_rationale: |
    The obligation in Art. 37(1)(a)–(c) is operationalised in NIST CSF 2.0
    through **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities
    related to cybersecurity risk management established, communicated,
    understood, and enforced)** and **GV.SC-02 (Suppliers and other third parties
    known, prioritized, and assessed using a cybersecurity supply chain risk
    management process)**.

    GV.RR-02 controls the designation of the data protection officer as an
    established organisational role with defined responsibilities, reporting line
    and accountability: Art. 37(1) makes designation mandatory where any of the
    three triggers applies — public-authority processing, core-activity regular
    and systematic monitoring of data subjects on a large scale, or core-activity
    large-scale processing of special-category data under Art. 9 or criminal-
    conviction data under Art. 10. GV.SC-02 is applied by analogy to capture the
    controller's self-assessment of whether its processing profile crosses the
    Art. 37(1) thresholds, treated as a risk-based prioritisation of the
    controller's own data-protection exposure.

    Together the two subcategories embed the DPO role in an established
    accountability structure (GV.RR-02) backed by a documented trigger assessment
    (GV.SC-02 analogously), enabling ex-post demonstration to the supervisory
    authority that the designation decision is traceable to the controller's
    processing profile and is updated whenever that profile materially changes.
  ambiguity_notes: |
    Core activities carries VAG-S3; regular and systematic and large scale carry VAG-S3 and POLY-S3; nature, scope and/or purposes contains the Berry §5.1 explicitly-flagged and/or operator. Reading chosen: EDPB Guidelines 3/2018 §3.1, under which core activities are the primary, revenue-driving business activities of the controller and exclude supporting or ancillary functions (HR, IT helpdesk); the and/or in nature, scope and/or purposes is interpreted as inclusive-OR, so that any one of the three dimensions triggering regular and systematic monitoring on a large scale suffices for Art. 37(1)(b). An alternative reading confines core activities to the central business purpose, excluding processing closely related to but not constitutive of that purpose; this reading is narrower than EDPB §3.1 and creates a category of borderline processing that supervisors have generally resolved against the controller. A second alternative reading treats large scale as a hard numeric threshold (for example, the EDPB Guidelines 3/2018 §3.1 reference points of 1000 data subjects for special-category processing); this reading is operationally attractive but the EDPB has declined to fix a universal threshold and treats the assessment as fact-intensive. Remain open: (a) whether a single integrated service that performs both core and ancillary functions can split its processing profile for Art. 37(1)(b) purposes, or whether the controller's overall profile determines designation; (b) whether special-category processing at sub-large-scale on a recurring basis cumulatively reaches the large-scale threshold for Art. 37(1)(c).
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

