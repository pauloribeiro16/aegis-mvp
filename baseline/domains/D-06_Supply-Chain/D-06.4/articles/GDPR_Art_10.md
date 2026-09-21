---
document_id: AEGIS-PREPROC-GDPR-ART-10
title: GDPR Art. 10 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 10
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---

# GDPR Art. 10

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

