---
document_id: AEGIS-PREPROC-DORA-ART-24
title: DORA Art. 24 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 24
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
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# DORA Art. 24

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
- sr_id: SR-DORA-020
  title: "Information-security standards compliance for ICT third-party contracts"
  source_clauses:
    - { clause_id: DORA-C36, article_ref: "Art. 28(5) — `financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards`" }
  linked_objectives: [SO-DORA-011]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(5) requires financial entities to enter only into contractual
    arrangements with ICT third-party service providers that comply with
    appropriate information security standards; for contractual arrangements
    concerning critical or important functions, the financial entity shall
    take due consideration of the use by providers of the most up-to-date and
    highest quality information security standards. The clause carries the
    central DORA ambiguity flagged in `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the OJ text does not
    name a specific standard — ISO/IEC 27001, SOC 2, NIST CSF, CIS Controls,
    and ENISA guidance are all plausible reference points, and EBA Guidelines
    on outsourcing arrangements provide the supervisory-recognised floor for
    critical or important functions outsourcing. The clause co-exists with
    CRA Art. 24 conformity-assessment duties for ICT products supplied under
    contract (Regulation (EU) 2024/2847) and with the GDPR Art. 32 security-
    of-processing baseline. An EBA RTS under Art. 28(9) is expected to refine
    the standards-set for CTPPs but has not closed the open-naming question.
  security_rationale: |
    The Art. 28(5) standards-compliance duty is operationalised in NIST CSF
    2.0 through **GV.SC-01 (A cybersecurity supply chain risk management
    program, strategy, objectives, policies, and processes are established
    and agreed to by organizational stakeholders)** and **GV.SC-03 (Contracts
    with suppliers and other third parties are used to implement appropriate
    measures designed to meet the objectives of an organization's cybersecurity
    program)**. GV.SC-01 establishes the entity-wide supply-chain cybersecurity
    governance that articulates which information-security standards the entity
    treats as acceptable baselines — the very `appropriate information security
    standards` that the OJ text leaves POLY — and the criteria for distinguishing
    between routine and critical-or-important-function contracts. GV.SC-03
    converts that governance into enforceable contract terms, ensuring that
    the `most up-to-date and highest quality` anchor for critical-or-important
    functions is reflected in measurable contract clauses (certification
    evidence, audit-rights linkage to Art. 30(3)(e), sub-outsourcing
    transparency). Together these two subcategories close the gap between an
    entity's stated standards-set and the contractual surface with third-party
    providers, allowing ex-post demonstration under Art. 28(5) that every
    ICT-service contract was anchored in a documented program-level standards
    framework and tied back through enforceable contract terms — satisfying
    both the general `appropriate` floor and the critical-or-important
    `most up-to-date AND highest quality` escalator.
  ambiguity_notes: |
    S3 POLY on `information security standards` — the central DORA ambiguity
    per `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the clause names no specific standard. The chosen
    reading is entity-selected standards with supervisory-recognised standards
    (ISO/IEC 27001, SOC 2 Type 2, NIST CSF, ENISA guidance, EBA Guidelines)
    as the EU-acceptable floor. S3 POLY on `most up-to-date` is read against
    alternatives of current published version, state-of-the-art, or frontier
    practice. S3 VAG on `highest quality` is read at the literal most-
    rigorous, comprehensive, industry-leading end of the spectrum. S3 COORD
    on `most up-to-date AND highest quality` — both anchors required
    cumulatively. S2 POLY on `critical or important functions` — the
    undefined distinction propagates from `../Regulation/DORA/Ambiguity/05_DORA.md` §3.4. Compliance-
    framework note: ISO 27001, NIST 800-53, and EBA Guidelines function as
    reference frameworks rather than technology selections and are not part
    of the tech-stack exemption. Remain open: identification of the binding
    standards-set for CTPP designation remains subject to EBA RTS under
    Art. 28(9) and to the Joint Committee oversight of CTPPs at Ch. V Sec. 2.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

