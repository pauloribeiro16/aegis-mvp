---
document_id: AEGIS-PREPROC-DORA-ART-39
title: DORA Art. 39 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 39
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
status: DRAFT
---

# DORA Art. 39

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-025
  title: "Compulsory ICT security awareness and resilience training for staff"
  source_clauses:
    - { clause_id: DORA-C27, article_ref: "Art. 13(6) — `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes`" }
    - { clause_id: DORA-C28, article_ref: "Art. 13(6) same locus — `level of complexity commensurate to the remit of their functions`" }
    - { clause_id: DORA-C26, article_ref: "Art. 13(6) same locus — T4 mapping mismatch per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26" }
  linked_objectives: [SO-DORA-015]
  sub_domain: [D-08.1, D-08.2]
  nist_csf_mapping:
    - { id: PR.AT-01, title: "All users are informed and trained on cybersecurity topics (e.g., recognition of phishing, social engineering, and other relevant risks)" }
    - { id: PR.AT-02, title: "All members of the organization's workforce understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 13(6) requires financial entities to develop ICT security awareness
    programmes and digital operational resilience training as compulsory
    modules in their staff training schemes, with a level of complexity
    commensurate to the remit of staff functions. The clause is the workforce-
    scale counterpart to Art. 5(4) management-body training (governance track)
    and to the digital operational resilience testing duty at Chapter IV. The
    clause co-exists with GDPR Art. 39 staff-awareness duties for personal-
    data processing (Regulation (EU) 2016/679) and with NIS 2 Art. 21(2)(g)
    basic security training baselines (Directive (EU) 2022/2555). EBA
    Guidelines on ICT and security risk management set out the supervisory
    expectation on calibration, and AI Act Art. 4(2) provider-deployer
    literacy duties (Regulation (EU) 2024/1689) intersect where AI systems
    are in scope of the same staff training schemes.
  security_rationale: |
    The Art. 13(6) workforce training duty is operationalised in NIST CSF
    2.0 through **PR.AT-01 (All users are informed and trained on cybersecurity
    topics (e.g., recognition of phishing, social engineering, and other
    relevant risks))** and **PR.AT-02 (All members of the organization's
    workforce understand their roles and responsibilities in achieving the
    organization's cybersecurity objectives)**. PR.AT-01 anchors the baseline
    awareness layer that closes the human-factor gap — phishing recognition,
    social-engineering resistance, password hygiene, incident-reporting
    reflexes — and converts the OJ `ICT security awareness programmes` from
    an opt-in continuing-professional-development activity into a compulsory
    training-module floor across the workforce. PR.AT-02 layers the role-
    specific depth dimension that the OJ `commensurate to the remit of
    their functions` qualifier demands, ensuring that staff in
    security-critical roles (incident response, ICT operations, fraud
    investigation, third-party governance) receive calibrated depth rather
    than a uniform baseline. Together these two subcategories operationalise
    both the `compulsory` and the `commensurate` axes of Art. 13(6), and
    an entity evidencing PR.AT-01 coverage plus PR.AT-02 role-calibrated
    depth can demonstrate ex-post to supervisory review that the Art. 13(6)
    workforce-training obligation was met at both the universal-awareness
    floor and the role-specific depth required by the staff function
    taxonomy, and that completion thresholds were documented as a
    condition of employment rather than as optional professional
    development.
  ambiguity_notes: |
    S2 VAG on `compulsory` is read as completion-mandatory (not mere
    attendance). S2 COORD on `programmes, training, modules` is read
    cumulatively as three artefact types used interchangeably. S2 VAG on
    `level of complexity commensurate to the remit of their functions` is
    read as function-specific calibration per the OJ literal formulation.
    T4-vs-text gap (per `../Regulation/DORA/Ambiguity/05_DORA.md` §2.26): T4 maps DORA-C26 to D-02.2
    `Patch Management & Updates` with description `Learning and evolving:
    post-incident reviews; incorporate findings into patching and update
    processes`, while the OJ Art. 13(6) text is about training programmes
    only — post-incident reviews live in Art. 13(2) and patching lives in
    Art. 9(4)(f). The Executor keeps the OJ-literal locus at D-08.1/D-08.2.
    T4-vs-text gap on DORA-C28: T4 reads `role-specific training` while the
    OJ Art. 13(6) uses only `commensurate to the remit of their functions`.
    Remain open: demonstration thresholds (completion percentages,
    assessment-pass thresholds) for `compulsory` are an entity-policy
    matter awaiting industry convergence.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

