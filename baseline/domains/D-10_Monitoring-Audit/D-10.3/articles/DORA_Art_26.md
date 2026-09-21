---
document_id: AEGIS-PREPROC-DORA-ART-26
title: DORA Art. 26 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 26
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DeepAnalysis/D-02_Vulnerability-Management/D-02.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# DORA Art. 26

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-DORA-005 | A sound and comprehensive digital operational resilience testing programme is established, maintained and reviewed as an integral part of the ICT risk-management framework, drawing on a portfolio of testing modalities (vulnerability assessments, scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing) and including advanced testing by means of TLPT at least every three years, with frequency adjustments at the competent authority's request. | `DORA-C32` (Art. 24(1) testing programme as integral part of framework); `DORA-C33` (Art. 25(1) portfolio of testing modalities — 12-way open list); `DORA-C34` (Art. 26(1) TLPT — 3-year anchor + CA frequency adjustment) | D-02.4, D-10.3 |
| SO-DORA-005 | D-02.4, D-10.3 | Art. 24 + Art. 25 + Art. 26 | Testing programme + testing modalities + TLPT |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-008
  title: "Multi-modality resilience testing programme as framework component"
  source_clauses:
    - { clause_id: DORA-C32, article_ref: "Art. 24(1) — `establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`" }
    - { clause_id: DORA-C33, article_ref: "Art. 25(1) — testing modalities portfolio (12-way open list)" }
  linked_objectives: [SO-DORA-005]
  sub_domain: [D-10.3, D-02.4]
  nist_csf_mapping:
    - { id: GV.OV-02, title: "The organizational cybersecurity risk management strategy is reviewed and adjusted to address changes in the organization's risk landscape" }
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: PR.PS-06, title: "Secure software development practices are integrated, and their performance is monitored throughout the SDLC" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Art. 24(1) requires financial entities to establish, maintain and
    review a sound and comprehensive digital operational resilience
    testing programme as an integral part of the ICT risk-management
    framework. Art. 25(1) operationalises this through a portfolio of
    testing modalities — vulnerability assessments, scans, open source
    analyses, network security assessments, gap analyses, physical
    security reviews, questionnaires, source code reviews where
    feasible, scenario-based tests, compatibility testing, performance
    testing, end-to-end testing and penetration testing. Chapter IV
    is dedicated to the testing programme, with Art. 26 (TLPT) and
    Art. 27 (advanced testing for significant entities) imposing
    higher-tier obligations alongside Art. 24–25 baseline (NIS 2
    Art. 21(2)(f) on basic cyber-hygiene and policy review imposes
    a parallel periodic-test expectation on NSIEs that DORA NSIEs
    retain as joint obligation). The Art. 24(7) RTS mandate is the
    principal pending source of measurability for the `sound and
    comprehensive` qualifier.
    [OJ-corrective note (v0.2 audit, material): Art. 25(1) — 12 OJ items miscounted (split + omission). OJ Art. 25(1) lists 12 comma-separated testing modalities: (1) vulnerability assessments and scans, (2) open source analyses, (3) network security assessments, (4) gap analyses, (5) physical security reviews, (6) questionnaires and scanning software solutions, (7) source code reviews where feasible, (8) scenario-based tests, (9) compatibility testing, (10) performance testing, (11) end-to-end testing, (12) penetration testing. The SR splits chunk #1 into 2 items and omits `scanning software solutions` from chunk #6.]
  security_rationale: |
    The obligation in Art. 24(1)/Art. 25(1) for a sound and
    comprehensive digital operational resilience testing programme is
    operationalised in NIST CSF 2.0 through **GV.OV-02 (The
    organizational cybersecurity risk management strategy is reviewed
    and adjusted to address changes in the organization's risk
    landscape)**, **ID.RA-01 (Vulnerabilities in assets are
    identified, validated, and recorded)**, and **PR.PS-06 (Secure
    software development practices are integrated, and their
    performance is monitored throughout the SDLC)**. GV.OV-02 anchors
    the testing programme as a strategic-review instrument whose
    findings must feed strategy adjustment, ensuring the programme
    is integral to the framework rather than parallel. ID.RA-01
    supplies the validated vulnerability substrate that the twelve-
    modality portfolio in Art. 25(1) — vulnerability assessments,
    scans, source-code reviews, scenario tests, penetration testing —
    operationalises into concrete testing outputs traceable to known
    vulnerabilities. PR.PS-06 closes the SDLC dimension by ensuring
    secure-development controls are themselves tested rather than
    assumed, completing the modality coverage on the
    application-layer side. The OJ `sound and comprehensive`
    qualifier is delivered by the multi-modality coverage plus
    strategic-feedback loop. The accountability link under Art. 5(2):
    the testing-programme charter, modality-coverage matrix,
    test-execution records, and findings-to-strategy-adjustment logs
    produce the documented evidence trail the management body can
    present to competent authorities demonstrating that resilience
    testing is structurally embedded and strategy-influencing rather
    than incident-driven.
  ambiguity_notes: |
    Source clause DORA-C32 carries S2 on `sound` and `comprehensive`
    (VAG), S2 on `testing programme` (POLY — single programme vs.
    portfolio of tests), and S2 on `establish, maintain AND review`
    (COORD 3-way verb coordination; reading chosen: R1 all three
    activities required). DORA-C33 carries S3 on the 12-way open
    list (`such as` pattern, COORD S3 — the `such as` softens the
    list to illustrative; reading chosen: R2 illustrative-with-
    floor — the entity selects from the list appropriate to its
    risk profile, with the modalities collectively covering the
    ICT-system attack surface). `where feasible` (VAG S2) — R1
    technically achievable / R2 cost-effective / R3 either; R3
    literal. The dominance of `R2 illustrative-with-floor` over
    pure-illustrative reflects the supervisory expectation that an
    entity running none of the twelve modalities would fail to
    establish a `sound and comprehensive` testing programme. A
    contrasting reading treats the `such as` clause as strictly
    illustrative with no floor, leaving the entity entirely free
    to select any testing modalities; this reading is consistent
    with the OJ literal text but inconsistent with the supervisory
    expectation in EBA Guidelines on ICT and security risk
    management §208–§212. A third constructed reading would impose
    all twelve modalities as an enumerated floor — supported by
    the structural formality of the twelve-item list in OJ but
    unsupported by the `such as` pattern's softening language. The
    Art. 24(7) RTS mandate is pending and may close the modality-
    selection question. Remain open: (a) whether the ESAs Joint
    Committee RTS under Art. 24(7) will impose a quantified
    baseline-modality floor for specific entity classes; (b) whether
    `where feasible` will be interpreted by supervisory practice as
    R1 (technically achievable) or R2 (cost-effective), with the
    distinction materially affecting the supervisory treatment of
    closed-source third-party components.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-009
  title: "Threat-led penetration testing on triennial supervisory cycle"
  source_clauses:
    - { clause_id: DORA-C34, article_ref: "Art. 26(1) — `shall carry out at least every 3 years advanced testing by means of TLPT`" }
  linked_objectives: [SO-DORA-005]
  sub_domain: [D-02.4]
  nist_csf_mapping:
    - { id: ID.RA-01, title: "Vulnerabilities in assets are identified, validated, and recorded" }
    - { id: ID.RA-04, title: "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified, recorded, and prioritized" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Art. 26(1) requires financial entities to carry out at least every
    3 years advanced testing by means of TLPT. The competent authority
    may, where necessary, request a reduction or increase in this
    frequency based on the entity's risk profile and operational
    circumstances. The provision sits inside Chapter IV with scope
    limitations dependent on entity significance (Art. 26(8)–(11)):
    the TLPT obligation applies to entities identified as significant
    under Art. 26(8) on the basis of size, interconnectedness,
    complexity, and risk profile. Art. 26(11) defines TLPT by
    reference to the TIBER-EU framework or equivalent, which
    incorporates ISO/IEC 33069 and threat-intelligence-led
    methodology (cf. ESAs Joint Committee TIBER-EU Knowledge Hub).
    Recital 65 sets the policy rationale: TLPT bridges the gap
    between compliance-driven testing and real-world adversarial
    capability.
  security_rationale: |
    The obligation in Art. 26(1) for threat-led penetration testing
    on a triennial cycle is operationalised in NIST CSF 2.0 through
    **ID.RA-01 (Vulnerabilities in assets are identified, validated,
    and recorded)** and **ID.RA-04 (Potential impacts and likelihoods
    of threats exploiting vulnerabilities are identified, recorded,
    and prioritized)**. ID.RA-01 supplies the validated-vulnerability
    substrate that TLPT exercises: identified vulnerabilities are re-
    tested under adversarial conditions to verify remediation efficacy
    and detect regression. ID.RA-04 supplies the threat-likelihood-
    impact framing that TLPT's threat-intelligence-led methodology
    depends on — TIBER-EU scenarios are constructed from current
    campaigns whose impact-likelihood must be quantified to scope
    the test realistically and prioritised so test-team effort
    targets the most consequential threat paths. The OJ `at least
    every 3 years` hard anchor maps to a supervisory-cycle rather
    than operational-cadence frame, ensuring TLPT findings are
    reviewed in light of contemporary threat-actor capability at a
    frequency aligned to strategic-risk reassessment. The
    accountability link under Art. 5(2): the TLPT charter, threat-
    scenario justifications, test-execution records, and remediation-
    traceability documentation produce the documented evidence trail
    the management body can present to competent authorities
    demonstrating that adversarial-defence verification is performed
    at supervisory-relevant cadence with documented findings-to-
    remediation closure.
  ambiguity_notes: |
    Source clause DORA-C34 carries S2 on `risk profile` (POLY —
    entity-internal vs. sectoral; R1 entity-internal literal), S2 on
    `operational circumstances` (VAG — entity-context dependent),
    and S2 on `where necessary` (VAG — CA judgment). The hard
    numeric anchor (3 years) closes the temporal ambiguity. `TLPT`
    (POLY S2) — defined by reference to the TIBER-EU framework
    (Art. 26(11) — non-binding ESA guidance); R1 TIBER-EU, R2
    equivalent framework accepted; R1 dominant. `reduce or
    increase` (COORD S2) — R1 either direction authorised; R1
    literal. The dominant TIBER-EU reading is anchored in the
    ESAs Joint Committee TIBER-EU Knowledge Hub, which converges
    on the ECB-led methodology; equivalent framework acceptance
    is contingent on competent-authority recognition (an
    AOFIRST-only entity operating in France would still satisfy
    TLPT under national recognition even without TIBER-EU
    certification). An open question remains the scope of
    `significant` under Art. 26(8): the OJ text references
    Art. 26(8) criteria but defers the operational scope
    determination to the supervisory authority.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

