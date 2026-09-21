---
document_id: AEGIS-PREPROC-AI_Act-ART-43
title: AI_Act Art. 43 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 43
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# AI_Act Art. 43

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-017
  title: "Documented quality management system governing AI compliance"
  source_clauses:
    - { clause_id: AIA-C20, article_ref: "Art. 17(1) — `Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)`" }
    - { clause_id: AIA-C22, article_ref: "Art. 17(1)(g) — `the risk management system referred to in Article 9`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: GV.RM-01, title: "Risk management objectives are established and agreed to by organizational stakeholders" }
    - { id: GV.RM-04, title: "Strategic direction on identifying and responding to risks established and communicated" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1) of Regulation (EU) 2024/1689 requires providers of
    high-risk AI systems to put in place a quality management
    system (QMS) that ensures compliance with the AI Act. The QMS
    must be documented in a systematic and orderly manner as
    written policies, procedures, and instructions, and must
    cover at least the 13 enumerated aspects (a)–(m) of the
    paragraph. Sub-point (g) cross-refers to Art. 9 (the risk
    management system), so the QMS is the governance substrate
    for the substantive Title III obligations. Recital 67
    characterises the QMS as inspired by established quality
    standards (ISO 9001 family) but does not mandate a specific
    standard, leaving the provider to choose. A compliance officer
    should treat the QMS as the umbrella obligation that the
    conformity assessment will examine first.
  security_rationale: |
    The Art. 17(1) QMS duty is operationalised in NIST CSF 2.0
    through **GV.PO-01 (Organisational cybersecurity policy
    established, communicated, enforced)**, **GV.RM-01 (Risk
    management objectives established and agreed)**, and
    **GV.RM-04 (Strategic direction on identifying and
    responding to risks)**, with supplementary alignment to
    **GV.PO-02 (Cybersecurity processes and procedures
    established, communicated, enforced)** and **GV.OC-03
    (Legal, regulatory, contractual requirements understood
    and managed)**. GV.PO-01 is the policy arm of the QMS —
    the top-level written cybersecurity policy that
    operationalises the 13-element list (a)–(m), including the
    policies, procedures, and instructions anchor in Art. 17(1).
    GV.RM-01 binds the QMS to risk-management objectives that
    have been agreed by organisational stakeholders, satisfying
    sub-point (g)'s cross-reference to Art. 9. GV.RM-04 supplies
    the strategic-direction layer (risk appetite, response
    posture, escalation criteria) that connects policy
    formulation (GV.PO-01) and risk-objective setting
    (GV.RM-01) to operational risk-treatment decisions.
    Supplementary GV.PO-02 ensures that the policies are
    accompanied by processes and procedures that are also
    documented, communicated, and enforced — the systematic
    and orderly requirement of Art. 17(1). GV.OC-03 closes the
    loop by ensuring the QMS understands and manages the full
    set of legal, regulatory, and contractual obligations that
    the AI Act adds on top of CRA, NIS 2, GDPR, and DORA. The
    combined control set yields a documented policy stack,
    agreed risk-management objectives, a strategic-direction
    document, process and procedure manuals, and a legal/
    regulatory obligations register — the evidentiary
    substrate for the conformity-assessment body to examine
    the QMS as the umbrella obligation under the Art. 17
    QMS + Art. 9 risk-management + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C20 carries **S2** features (per
    `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.20). `systematic and orderly manner` is
    VAG-2 (Berry §5.1 — the OJ does not anchor the sense).
    `quality management system` is POLY-2 with R1 ISO 9001
    / R2 ISO/IEC 23053 (AI risk management framework
    standard) / R3 internal bespoke; the OJ does not name
    any specific standard (reading chosen: R3 literal). The
    3-way AND of `written policies, procedures AND instructions`
    and the 13-element closed list (a)–(m) are both COORD-2.
    AIA-C22 inherits POLY-2 from AIA-C01 (`risk management
    system` — the central AI Act ambiguity per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md`
    §3.5). Remain open: (a) whether conformity-assessment
    bodies will accept an ISO 9001 certificate as a proxy
    for the QMS or require a stand-alone AI-QMS file; (b)
    whether the 13 elements must be discrete QMS chapters or
    can be embedded into a single integrated management
    system.
```

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-018
  title: "Secure design control and verification integrated into SDLC"
  source_clauses:
    - { clause_id: AIA-C21, article_ref: "Art. 17(1)(c) — `techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system`" }
  linked_objectives: [SO-AIACT-010]
  sub_domain: [D-07.1]
  nist_csf_mapping:
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
    - { id: PR.PS-01, title: "Configuration management practices are established, documented, and applied to assets" }
  applies_to_role: [PROVIDER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 17(1)(c) of Regulation (EU) 2024/1689 requires the QMS
    to include the techniques, procedures, and systematic actions
    used for the design, design control, and design verification
    of the high-risk AI system. This is the secure-development-
    lifecycle anchor of the QMS and is the operational bridge
    between Art. 17(1) (QMS) and Art. 9 (risk management) on
    one side, and Art. 15 (accuracy / robustness / cybersecurity)
    on the other. A compliance officer should treat Art. 17(1)(c)
    as the SDLC sub-process specification that the conformity
    assessment will examine alongside the technical documentation
    (Annex IV).
  security_rationale: |
    The Art. 17(1)(c) SDLC duty is operationalised in NIST CSF
    2.0 through **PR.PS-06 (Secure software development
    practices integrated across the SDLC)** and **PR.PS-01
    (Configuration management practices established,
    documented, applied)**, with supplementary alignment to
    **PR.PS-02 (Software maintenance commensurate with risk)**,
    **ID.RA-01 (Vulnerability identification, validation,
    recording)**, and **GV.PO-02 (Cybersecurity processes and
    procedures established, communicated, enforced)**. PR.PS-06
    is the principal anchor: it directly maps to the
    `techniques, procedures and systematic actions` for
    `design, design control and design verification` of the
    high-risk AI system, covering threat modelling (design),
    code review and change control (design control), and
    testing and review (design verification). PR.PS-01 enforces
    the design-control axis — configuration baselines,
    integrity of design artefacts, controlled changes — so
    that the design can be traced to its source and
    reconstructed. Supplementary PR.PS-02 binds software
    maintenance to the risk picture (patching, replacement,
    removal), closing the post-market SDLC loop. ID.RA-01
    ensures that vulnerabilities identified during design
    verification are recorded, validated, and feed back into
    the risk-management file under Art. 9. GV.PO-02 enforces
    that the SDLC is anchored in documented, communicated, and
    enforced processes. The combined control set yields
    documented design specifications, configuration baselines,
    change-control records, verification reports (test
    results, code-review records), vulnerability register
    entries, and process manuals — the evidentiary substrate
    for ex post demonstration of compliance under the Art. 17
    QMS + Art. 9 risk-management + Art. 15 accuracy-
    robustness-cybersecurity + Art. 43/47 conformity-
    assessment accountability chain.
  ambiguity_notes: |
    Source clause AIA-C21 carries **S2** POLY-2 on
    `design` vs. `design control` vs. `design verification`
    — three engineering terms with overlapping but distinct
    industry meanings (Berry §3.3.1; cf. ISO 9001 §8.3, IEC
    62304, NIST SP 800-218 SSDF PW.4/PW.5/PW.7). The 3-way
    AND of `design, design control AND design verification`
    + 3-way AND of `techniques, procedures AND systematic
    actions` is a twin 3-way AND that compounds the
    cumulative obligation (Berry §5.5). Remain open: (a)
    whether `design verification` requires independent
    verification (i.e. a separate team) or self-verification
    by the design team is acceptable; (b) whether the
    `systematic actions` axis covers post-deployment
    verification or only pre-market verification.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

