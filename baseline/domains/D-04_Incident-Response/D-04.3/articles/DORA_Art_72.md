---
document_id: AEGIS-PREPROC-DORA-ART-72
title: DORA Art. 72 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 72
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

# DORA Art. 72

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-017
  title: "Major-ICT-incident notification to supervisor and affected clients"
  source_clauses:
    - { clause_id: DORA-C31, article_ref: "Art. 19(1) — `Financial entities shall report major ICT-related incidents to the relevant competent authority`" }
    - { clause_id: DORA-C31, article_ref: "Art. 19(3) — `financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident`" }
  linked_objectives: [SO-DORA-008]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents are reported internally to the appropriate stakeholders, including executive leadership and legal counsel" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 19(1) imposes on financial entities a hard duty to notify the relevant
    competent authority of any major ICT-related incident, operating in parallel
    with — and not substituting for — the GDPR Art. 72-hour personal data breach
    notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-
    notification workflow under Directive (EU) 2022/2555 Art. 23, both of which
    must be triggered under their own criteria where applicable. The OJ Art. 19(1)
    trigger is the moment of classification as `major`, not the moment of awareness,
    while Art. 19(3) operates on a separate clock — `without undue delay as soon as
    they become aware` — which is direct client-facing disclosure. The threshold
    classification itself (Art. 18) delegates the criteria combination and
    materiality thresholds to an EBA/ESMA/EIOPA RTS under Art. 18(3), with
    Implementing Regulation (EU) 2024/2956 partially addressing reporting templates
    in Annex I to IV. The recital frame (recital 56) confirms the sector-differentiated
    hour-anchors and the recital frame on all-hazards coverage supports the
    classification-as-trigger reading.
    [OJ-corrective note (v0.2 audit, material): Art. 19(3) — trigger condition dropped. OJ Art. 19(3) conditions client notification: `Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident and about the measures that have been taken to mitigate the adverse effects of such incident.` The SR drops the trigger condition `and has an impact on the financial interests of clients` — converting a conditional obligation into an unconditional one. Every major incident would trigger client notification under the SR; OJ scopes to those with client-financial-impact.]
  security_rationale: |
    The Art. 19 major-incident notification duty is operationalised in NIST CSF
    2.0 through **RS.CO-02 (Incidents are reported internally to the appropriate
    stakeholders, including executive leadership and legal counsel)** and
    **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable
    rules and regulations)**. RS.CO-02 anchors the internal escalation path
    that must execute before any external notification — the supervisor-bound
    Art. 19(1) report is only as trustworthy as the internal chain that
    validated classification as `major`, escalated to executive leadership,
    and engaged legal counsel for regulatory-construction review. RS.CO-04
    governs the external notification layer itself, including the pre-approved
    supervisor contact route, the evidence-trail format aligned with the EBA/
    ESMA/EIOPA RTS templates (Implementing Regulation (EU) 2024/2956 Annex
    I–IV), and the parallel client-disclosure leg under Art. 19(3). Together
    these two subcategories convert reactive disclosure into a rehearsed
    communication run-book, and a documented RS.CO-02 + RS.CO-04 control set
    lets the entity demonstrate ex-post to competent authority review that
    the Art. 19(1)+(3) clocks were respected and the Art. 17 incident-
    management process fed the supervisory and client disclosure channels
    in the required sequence.
  ambiguity_notes: |
    S3 (Berry §5.7) on `major ICT-related incident` — the Art. 18(1) criteria are
    multiplicative and residually vague; the chosen reading is that any one criterion
    surpassing its materiality threshold (RTS-defined) triggers classification, with
    the supervisor adjudicating borderline cases. S3 POLY+COORD on the twin temporal
    trigger `without undue delay AS SOON AS they become aware` — the chosen reading
    is that `as soon as they become aware` is the moment the clock starts and
    `without undue delay` anchors the supervisory-side tempo. S3 POLY+SCOPE-Q on
    `becoming aware` — alternatives include actual knowledge, constructive knowledge,
    or either, with the dominant CJEU reading favouring constructive knowledge. S3
    on the Art. 18 implementing acts dependency, which remain pending and may close
    the threshold regress; the SR preserves the OJ-literal `major ICT-related
    incident` wording pending implementing acts. Remain open: pending EBA/ESMA/
    EIOPA technical standards under Art. 18(3), entities should adopt a written
    interpretive position on borderline cases and document it for supervisory
    review. Remain open: (a) whether `without undue delay AS SOON AS they become
    aware` admits an early-warning mini-notification (analogous to NIS 2 Art. 23(4)
    24-hour early warning) before the full Art. 19(4) intermediate report at 72 hours,
    pending EBA/ESMA/EIOPA technical-standards clarification; (b) the carve-out, if
    any, for payment-related incidents under Art. 23 (operational or security
    payment-related incidents) vis-à-vis the Art. 19(3) client-notification trigger,
    pending EBA Guidelines on operational or security payment-related incidents.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

