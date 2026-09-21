---
document_id: AEGIS-PREPROC-AI_Act-ART-64
title: AI_Act Art. 64 — SecurityObjectives & SecurityRules
regulation: AI_Act
article: Art. 64
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---

# AI_Act Art. 64

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-AIACT-001 (AI risk management lifecycle)

```yaml
- sr_id: SR-AIACT-024
  title: "GPAI serious incident reporting to the AI Office"
  source_clauses:
    - { clause_id: AIA-C29, article_ref: "Art. 55(1)(c) — `keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them`" }
  linked_objectives: [SO-AIACT-014]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
    - { id: RS.AN-03, title: "Analysis is performed to determine what has occurred during an event and the root cause of the event" }
  applies_to_role: [PROVIDER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 55(1)(c) of Regulation (EU) 2024/1689 requires
    providers of general-purpose AI models with systemic
    risk to keep track of, document, and report, without
    undue delay, to the AI Office and, as appropriate, to
    national competent authorities, relevant information
    about serious incidents and possible corrective
    measures to address them. The recipient differs from
    the high-risk AI obligation of Art. 73 — the GPAI
    report goes to the AI Office (an EU-level body
    established by Art. 64), not the market surveillance
    authorities of the Member States. Recital 110
    clarifies the GPAI-specific nature of the obligation
    and the upstream nature of the reporting (foundation
    model vs. downstream application). A compliance officer
    at a GPAI provider should treat Art. 55(1)(c) as the
    upstream companion to the high-risk Art. 73 obligation,
    with a separate recipient and a separate (open-text)
    timeline.
  security_rationale: |
    The Art. 55(1)(c) GPAI serious-incident reporting duty
    is operationalised in NIST CSF 2.0 through **RS.CO-02
    (Incidents reported internally to executive leadership
    and legal counsel)**, **RS.MA-03 (Incidents
    categorised, prioritised, scoped)**, and **RS.AN-03
    (Root-cause analysis)**, with supplementary alignment
    to **GV.OC-03 (Legal, regulatory, contractual
    requirements understood and managed)**, **GV.PO-01
    (Organisational cybersecurity policy established,
    communicated, enforced)**, and **RS.CO-04
    (Coordination with stakeholders consistent with
    applicable rules and regulations)**. RS.CO-02 is the
    internal-reporting arm: the GPAI provider must route
    incident awareness to leadership and legal counsel so
    the AI Office report can be reviewed and the
    `without undue delay` clock is controlled. RS.MA-03
    binds the reporting to a categorised scope so the
    `serious incidents AND possible corrective measures`
    elements are both addressed. RS.AN-03 enforces the
    root-cause analysis that the report must carry to
    satisfy the `relevant information` element of
    Art. 55(1)(c). Supplementary GV.OC-03 ensures the
    GPAI provider understands the cross-regulation
    reporting regime (Art. 55 GPAI + Art. 73 high-risk
    + NIS 2 C30 + DORA Art. 19, with the Art. 55 vs.
    Art. 73 boundary per the SR-AIACT-022 ambiguity
    note). GV.PO-01 anchors the reporting workflow in
    a top-level policy; and RS.CO-04 ensures
    coordination with the AI Office and national
    competent authorities is consistent with applicable
    rules. The combined control set yields a categorised
    incident register, a root-cause analysis pipeline,
    internal-reporting records, AI Office transmissions,
    a top-level policy, a cross-regulation obligations
    register, and a coordination procedure — the
    evidentiary substrate for ex post demonstration of
    compliance with the Art. 55(1)(c) reporting duty
    under the Art. 9 risk-management + Art. 55(1)(a)
    model-evaluation + Art. 55(1)(c) GPAI incident
    reporting + Art. 72 PMM accountability chain.
  ambiguity_notes: |
    Source clause AIA-C29 carries three **S3** features
    (per `../Regulation/AI_Act/Ambiguity/06_AI_Act.md` §2.29). `without undue delay`
    is VAG-3 (Berry classic; cf. NIS 2 C30 on `without
    undue delay`). `relevant information` is VAG-3
    (the OJ does not enumerate what is `relevant`).
    `as appropriate` is POLY-3 (R1 mandatory / R2
    optional / R3 case-by-case). The `serious incidents`
    term is **POLY-3** for GPAI models — distinct from
    `serious incidents` for high-risk AI systems (Art. 73)
    but the cross-reference is implicit; the boundary
    (when does a GPAI incident trigger Art. 55 reporting
    vs. Art. 73 reporting vs. both?) is undefined
    (Berry §3.3.1 cross-article polysemy). The 3-way
    verb AND `keep track of, document, AND report` and
    the AND `serious incidents AND possible corrective
    measures` are COORD-2. Remain open: (a) whether
    `without undue delay` imposes a numeric clock (and
    if so, what number — 72h? 7d?) or is unbounded;
    (b) whether the `as appropriate` axis is mandatory
    when the national competent authority requests
    the report; (c) whether the AI Office will issue
    a unified incident-reporting template that
    resolves the Art. 55 vs. Art. 73 boundary.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

