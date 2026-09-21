---
document_id: AEGIS-PREPROC-NIS2-ART-20
title: NIS2 Art. 20 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 20
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.3.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
status: DRAFT
---

# NIS2 Art. 20

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-019 | Employees are offered similar cybersecurity training on a regular basis, enabling them to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity. | `NIS2-CL05` (Art. 20(2) sentence 2 — employee training encouraged); `NIS2-CL04` (Art. 20(2) sentence 1 — purpose clause: `sufficient knowledge and skills` to `identify risks and assess`) | D-08.1, D-08.2 |
| SO-NIS2-019 | D-08.1, D-08.2 | Art. 20(2) sentence 2 | Employees offered similar training on a regular basis |
| SO-NIS2-020 | Members of the management bodies of essential and important entities follow cybersecurity training, gaining sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity. | `NIS2-CL03` (Art. 20(2) sentence 1 — management-body training mandatory); `NIS2-CL04` (Art. 20(2) sentence 1 — purpose clause: `sufficient knowledge and skills`) | D-08.3, D-09.1 |
| SO-NIS2-020 | D-08.3, D-09.1 | Art. 20(2) sentence 1 | Management body members follow cybersecurity training |
| SO-NIS2-021 | The management body of essential and important entities approves the cybersecurity risk-management measures taken to comply with Art. 21, oversees their implementation, and can be held liable for infringements of that Article by the entity. | `NIS2-CL01` (Art. 20(1) sentence 1 — approve + oversee + held liable); `NIS2-CL02` (Art. 20(1) sentence 2 — public-institution carve-out); `NIS2-CL06` (Art. 20 chapeau — proportionality hook via Art. 3 classification) | D-09.1, D-09.3 |
| SO-NIS2-021 | D-09.1, D-09.3 | Art. 20(1) | Management body approves + oversees + bears liability for Art. 21 measures |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-030
  title: "Recurring employee cybersecurity training on risk identification and assessment"
  source_clauses:
    - { clause_id: NIS2-CL05, article_ref: "Art. 20(2) sentence 2 — employee training encouraged, similar training on a regular basis" }
    - { clause_id: NIS2-CL04, article_ref: "Art. 20(2) sentence 1 — purpose clause (cross)" }
  linked_objectives: [SO-NIS2-019]
  sub_domain: [D-08.1, D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics" }
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Article 20(2) sentence 2 of Directive (EU) 2022/2555 requires Member States to encourage essential and important entities to offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices. The verb `encourage` is the binding force on the Member State; the entity-side obligation is correspondingly encouraged-only, with the entity-side SR applying only where the entity adopts the encouragement (orchestrator-recommended treatment). The cross-link to Article 20(2) sentence 1 anchors the purpose clause: training must equip employees to identify risks and assess cybersecurity risk-management practices, the same purpose clause that governs the management-body training in SR-NIS2-031.
  security_rationale: |
    The obligation in Art. 20(2) sentence 2 for Member States to encourage essential and important entities to offer similar training to their employees on a regular basis is operationalised in NIST CSF 2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity topics)** and **PR.AT-02 (All members of the workforce understand their roles and responsibilities in achieving the organisation's cybersecurity objectives)**. PR.AT-01 anchors the recurring training content: phishing, social engineering, password discipline, and the threat-recognition capability that the OJ's purpose clause requires employees to possess. PR.AT-02 anchors the role-specific dimension: each employee understands how their own role contributes to the entity's cybersecurity objectives, supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`. Together, PR.AT-01 and PR.AT-02 operationalise the workforce-literacy substrate. The control set enables ex-post demonstration that the OJ's `regular basis` anchor is discharged against a documented training curriculum anchored in the NIST NICE Workforce Framework and proportionate to the entity's exposure.
  ambiguity_notes: |
    The verb `shall encourage` admits four readings (national policy, financial incentives, sectoral guidance, or all) with the chosen reading being the cumulative reading since the OJ is silent on the encouragement mechanism. The compound `similar training` admits a parallel-to-management-training reading or a peer-entity-comparability reading; the literal reading is parallel-to-management-training because the OJ coordinates sentence 2 with sentence 1 within the same paragraph. The temporal anchor `on a regular basis` admits annual, biannual, or ad-hoc cadences; the chosen reading is entity-discretionary under Recital 56. The Orchestrator-recommended treatment is that the entity-side SR applies to entities that adopt the encouragement, since the Article 20(2) sentence 2 binding force is on the Member State rather than directly on the entity. Remain open: whether Member State supervisory authorities will codify a minimum training-hours-per-year threshold that converts the encouragement into a measurable expectation, as Germany BSI has signalled in its national transposition.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-031
  title: "Management body cybersecurity literacy prerequisite for governance duties"
  source_clauses:
    - { clause_id: NIS2-CL03, article_ref: "Art. 20(2) sentence 1 — management body training mandatory" }
    - { clause_id: NIS2-CL04, article_ref: "Art. 20(2) sentence 1 — purpose clause: sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices" }
  linked_objectives: [SO-NIS2-020]
  sub_domain: [D-08.3, D-09.1]
  nist_csf_mapping:
    - { id: PR.AT-03, title: "All senior executives understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: GV.RR-01, title: "Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 20(2) sentence 1 of Directive (EU) 2022/2555 requires Member States to ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity. The training obligation is structurally the literacy prerequisite for the Article 20(1) management-body obligations (approve, oversee, can be held liable under SR-NIS2-032/033/034): without trained members, the management body cannot meaningfully discharge the approve-and-oversee obligations or be held accountable for infringements. The purpose clause anchors two distinct knowledge objects (identify risks; assess cybersecurity risk-management practices) and a third impact object (impact on the services provided), which together define the syllabus scope without prescribing specific content. The Member-State implementation determines whether the training is statutory (statute-imposed curriculum), entity-internal (entity's own programme), or both; the chosen reading is the both reading as the standard MS-implementation pattern.
  security_rationale: |
    The obligation in Art. 20(2) sentence 1 for Member States to ensure that members of the management bodies of essential and important entities are required to follow training is operationalised in NIST CSF 2.0 through **PR.AT-03 (All senior executives understand their roles and responsibilities in achieving the organisation's cybersecurity objectives)** and **GV.RR-01 (Organisational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture)**. PR.AT-03 anchors the executive-literacy substrate: management-body members individually possess sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion. GV.RR-01 anchors the leadership-culture substrate: trained members exercise the approve-and-oversee obligations of Article 20(1) with informed judgement and accept personal liability exposure under Article 20(1) sentence 1 third clause on a substantively-informed basis. Together, PR.AT-03 and GV.RR-01 connect management-body literacy to the wider accountability architecture. The control set enables ex-post demonstration that the management body could meaningfully interrogate the CISO's risk register, ask the right questions, and weight competing strategic trade-offs.
  ambiguity_notes: |
    The construction `are required to follow training` carries an S3 ambiguity on the binding-force locus: a statutory reading (training is required by national statute), an entity-internal reading (the entity itself requires the training), or a both reading (statute mandates, entity operationalises), with the chosen reading being the both reading since the OJ's literal `are required to follow` is compatible with either locus and the standard MS-implementation pattern combines them. The compound `training` admits three operative readings (formal certified programme, awareness briefing, or tabletop exercise), with the chosen reading being entity-discretionary, with formal certified training preferred where the entity seeks documented compliance evidence. The scope `members of the management bodies` admits three readings (every member individually, the body collectively, or a designated subset), with the literal reading being every member individually because the OJ does not provide a designation carve-out; the definition of `management body` is Member-State-determined under Article 6 (recital 75). The qualifier `sufficient knowledge and skills` admits a general-management or cybersecurity-specific reading, with the cybersecurity-specific reading being dominant because the OJ coordinates it with `cybersecurity risk-management practices`. Member State transposition divergence is highest on the `members of the management bodies` definition, with some Member States anchoring on the company-law board concept and others extending to executive committees. Remain open: (a) whether Member State supervisory authorities will publish a minimum-content syllabus or competency framework for management-body training under Article 4 implementing acts; (b) whether the cybersecurity-specific reading of `sufficient knowledge and skills` extends to AI-system risk literacy, which would couple this SR with AI Act Article 4 literacy obligations for entities that deploy AI in NIS-critical functions.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-032
  title: "Management body formally approves Article 21 risk-management measures"
  source_clauses:
    - { clause_id: NIS2-CL01, article_ref: "Art. 20(1) sentence 1 — management body approves" }
    - { clause_id: NIS2-CL02, article_ref: "Art. 20(1) sentence 2 — public-institution carve-out (cross)" }
  linked_objectives: [SO-NIS2-021]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.RR-02, title: "Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced" }
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 20(1) sentence 1 first clause of Directive (EU) 2022/2555 requires Member States to ensure that the management bodies of essential and important entities approve the cybersecurity risk-management measures taken by those entities in order to comply with Article 21. The verb `approve` is the upstream governance gate for the Article 21 measures: without documented management-body approval, the measures lack executive sponsorship, resource allocation, and the standing required to be enforced across the entity. The cross-link to Article 20(1) sentence 2 preserves the public-institution carve-out (Member States must ensure that the obligations also apply to public-institution equivalents, with the constitutional-impediment deference to national law), which is a structural commitment that the management-body accountability architecture extends to the public sector where the Member State's constitutional order permits. The `in order to comply with Article 21` qualifier anchors the approval object to the Article 21 measures rather than to a free-standing entity cybersecurity strategy, which is the deliberate coupling of governance to the substantive Article 21 obligation.
  security_rationale: |
    The obligation in Art. 20(1) sentence 1 first clause for the management body of essential and important entities to approve the cybersecurity risk-management measures is operationalised in NIST CSF 2.0 through **GV.RR-02 (Roles, responsibilities, authorities, and accountabilities related to cybersecurity risk management are established, communicated, understood, and enforced)** and **GV.PO-01 (Organisational cybersecurity policy is established, communicated, and enforced)**. GV.RR-02 anchors the approval as a documented governance act: the approval minute records the management body's reading of the measures, acceptance of residual risk, and resource commitment, creating the executive sponsorship without which the Article 21 measures are operationally orphaned, susceptible to budget reallocation, and unable to demonstrate the strategic-priority status required by Recital 75. GV.PO-01 anchors the downstream enforceability: the approved measures become the binding organisational cybersecurity policy. Together, GV.RR-02 and GV.PO-01 connect the approval act to the policy-enforcement consequence. The control set enables ex-post demonstration that the management body has read, accepted, and committed to the Article 21 measures through a documented minute, with re-approval triggers when material changes occur.
  ambiguity_notes: |
    The compound `cybersecurity risk-management measures` carries an S3 ambiguity on the approval object: an Article 21(2)(a)–(j) sub-point list reading, an Article 21(1) chapeau-and-Article 21(5) implementing-act reading, or a free-standing entity-cybersecurity-strategy reading, with the chosen reading being the literal-and-broad interpretation that `measures` covers both the Article 21(2) sub-points and any entity-discretionary measures adopted under Article 21(1). The qualifier `in order to comply with Article 21` carries an indicative-versus-restrictive ambiguity on whether the approval is for Article 21 measures specifically or for any measures that contribute to compliance, with the indicative reading being dominant since the OJ uses the qualifier to anchor the approval object rather than to constrain it. The `public institutions` carve-out (Article 20(1) sentence 2) carries a SCOPE-Q ambiguity on whether `public` tracks the Article 6(35) public-administration definition, the broader State-controlled entity definition, or only constitutional bodies, with the chosen reading being the Article 6(35) anchor because that is the OJ's defined-term anchor. Member State transposition divergence may apply on the public-institution carve-out implementation. Remain open: (a) whether the documented approval minute must enumerate each Article 21(2)(a)–(j) sub-point individually or whether a single omnibus-approval minute suffices, with national supervisory practice likely to diverge; (b) whether the Article 20(1) sentence 1 first-clause approval extends to NIS2-derived implementing acts adopted under Article 21(5), which would convert approval from a one-off minute into a recurring governance burden.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-033
  title: "Management body continuously oversees Article 21 implementation"
  source_clauses:
    - { clause_id: NIS2-CL01, article_ref: "Art. 20(1) sentence 1 — management body oversees" }
  linked_objectives: [SO-NIS2-021]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.OV-01, title: "Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organizational risks" }
    - { id: GV.RM-05, title: "Lines of communication across the organization are established for cybersecurity risks, including risks from suppliers and other third parties" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 20(1) sentence 1 second clause of Directive (EU) 2022/2555 requires Member States to ensure that the management bodies of essential and important entities oversee the implementation of the cybersecurity risk-management measures taken to comply with Article 21. The verb `oversees` is the active-monitoring dimension of the management-body governance architecture and operates continuously after the SR-NIS2-032 approval minute: oversight converts the one-time approval into a recurring governance activity that catches control erosion, evolving threat landscape and residual-risk drift before they accumulate into incidents. The three-verb coordination in Article 20(1) sentence 1 (`approve, oversee, and can be held liable`) carries an S3 ambiguity on whether the three verbs are three distinct obligations, one composite obligation, or two distinct obligations plus a liability consequence; Recital 75 implies three distinct obligations, and the chosen reading treats them as three distinct governance activities. The cross-link to SR-NIS2-031 establishes that oversight is meaningless without trained management-body members (Article 20(2) sentence 1 training obligation).
  security_rationale: |
    The obligation in Art. 20(1) sentence 1 second clause for the management body to oversee the implementation of the cybersecurity risk-management measures is operationalised in NIST CSF 2.0 through **GV.OV-01 (Cybersecurity risk management strategy outcomes are reviewed and adjusted to ensure they adequately address organisational risks)** and **GV.RM-05 (Lines of communication across the organisation are established for cybersecurity risks, including risks from suppliers and other third parties)**. GV.OV-01 anchors the active-monitoring dimension: the management body reviews implementation status, receives exception reports, interrogates the CISO on residual-risk drift, and authorises adjustments to the Article 21 measures as the threat landscape and entity exposure evolve. GV.RM-05 anchors the upward-channel substrate that makes oversight operational: the CISO and relevant functions have documented escalation paths to the management body, including exception and incident reporting. Together, GV.OV-01 and GV.RM-05 connect oversight to the communication infrastructure that feeds it. The control set enables ex-post demonstration that the management body exercised the oversight duty on a recurring cadence, not as a one-time approval act, with documented decisions on identified drift.
  ambiguity_notes: |
    The three-verb coordination carries an S3 COORD ambiguity: three-distinct-obligations reading, one-composite-obligation reading, or two-distinct-plus-liability-consequence reading, with the chosen reading being the three-distinct reading because the OJ coordinates three verbs with commas and the conjunction `and`, and Recital 75 frames them as three substantive obligations rather than one. The `oversees` obligation is continuous by construction (no terminal-event qualifier), so the management body reviews implementation status and adjusts as needed on an entity-discretionary cadence. The oversight-object ambiguity (whether oversight covers implementation status only, or also threat-landscape evolution and risk-register currency) is resolved by Recital 75 toward the broader reading, since the recital positions management-body engagement as a strategic discipline rather than a procedural checkpoint. Member State transposition divergence may apply on the documentation expected to evidence oversight (board minutes, dashboard reviews, exception registers). Remain open: (a) whether Member State supervisory authorities will define a minimum oversight cadence (quarterly, semi-annual, annual) under Article 4 implementing acts; (b) whether the oversight obligation extends to the AI-system risk dimension under AI Act Article 4 for entities that deploy AI in NIS-critical functions, since AI risk literacy may be a gap in management-body cybersecurity training under SR-NIS2-031.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-034
  title: "Management body personal liability for Article 21 infringements"
  source_clauses:
    - { clause_id: NIS2-CL01, article_ref: "Art. 20(1) sentence 1 — management body can be held liable for infringements" }
    - { clause_id: NIS2-CL02, article_ref: "Art. 20(1) sentence 2 — public-institution carve-out" }
  linked_objectives: [SO-NIS2-021]
  sub_domain: [D-09.1, D-09.3]
  nist_csf_mapping:
    - { id: GV.RR-01, title: "Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 20(1) sentence 1 third clause of Directive (EU) 2022/2555 requires Member States to ensure that the management bodies of essential and important entities can be held liable for infringements by the entities of Article 21. The `can be held liable` clause is the accountability instrument that anchors the SR-NIS2-032 approve and SR-NIS2-033 oversee obligations: without liability exposure, the upstream obligations would lack enforcement teeth and the management body could treat Article 21 compliance as a CISO-level concern rather than a board-level accountability. The Article 20(1) sentence 2 carve-out for public institutions explicitly defers the liability architecture for public-institution management bodies to national law, which is a structural signal that the Member States otherwise have full latitude to attach the four liability types (civil, criminal, administrative, all). The `infringements of that Article` qualifier anchors the liability trigger to infringements of Article 21, with the purposive reading extending the trigger to the full Article 21 obligation (chapeau + sub-points) rather than only the chapeau opening of Article 21(1).
  security_rationale: |
    The obligation in Art. 20(1) sentence 1 third clause that management bodies of essential and important entities can be held liable for infringements of Article 21 is operationalised in NIST CSF 2.0 through **GV.RR-01 (Organisational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture)** and **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed)**. GV.RR-01 anchors the personal-accountability dimension: management-body members have an individual stake in the Article 21 measures, which converts the upstream approve-and-oversee obligations of SR-NIS2-032 and SR-NIS2-033 from procedural compliance into substantively-informed decision-making. GV.OC-03 anchors the legal-frame substrate: the entity maintains a current register of the civil, administrative and (where applicable) criminal liability regimes that the Member State has attached to Article 20(1) sentence 1 third clause, including the available defences (reasonable-reliance-on-CISO, documented-oversight-minute). Together, GV.RR-01 and GV.OC-03 connect the personal-liability exposure to the compliance-management register. The control set enables ex-post demonstration that the management body was on notice of its liability exposure under the OJ and the relevant Member State transposition.
  ambiguity_notes: |
    The construction `can be held liable` carries an S3 POLY ambiguity on liability type: a civil-only, criminal-only, administrative-only, or all-types reading, with the chosen reading being the all-types reading because the Article 20(1) sentence 2 carve-out's explicit deference to national law for public institutions signals that the Member States otherwise have full latitude and the OJ imposes no carve-out from the broader all-types architecture. The compound `infringements of that Article` carries an S3 ambiguity on whether the liability trigger is the Article 21(1) chapeau opening, any Article 21(2) sub-point, or Article 21 plus the incident-reporting obligations of Article 23, with the chosen reading being the purposive R2 reading (any Article 21 sub-point) since the literal `of that Article` would support a narrower reading but the purposive reading captures the full Article 21 obligation as the Recital 75 framing intends. Member State transposition divergence is highest on this SR: national implementations (e.g. Belgium's NIS2 transposition, France's transposition with the AMF/ANSSI joint-oversight architecture for certain sectors) have begun diverging on which liability types attach, the standard of care expected of management-body members, and the available defences (reasonable-reliance-on-CISO, documented-oversight-minute). The German BSI signals an administrative-fine-only model; Italian ACN signals a civil-plus-administrative model with potential criminal exposure under the Italian criminal code for gross negligence. Remain open: (a) whether the European Commission will publish a non-binding interpretation of Article 20(1) sentence 1 third clause to align Member State transposition divergence, or whether national divergence will compound; (b) whether the `infringements of that Article` reading extends to incident-reporting infringements under Article 23, which would couple this SR with the SR-NIS2-013 to SR-NIS2-019 reporting-flow SRs at the management-body-liability layer.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

