---
document_id: AEGIS-PREPROC-DORA-ART-91
title: DORA Art. 91 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 91
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.3.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.3.md
status: DRAFT
---

# DORA Art. 91

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-024
  title: "Management-body ICT-risk literacy maintained through regular training"
  source_clauses:
    - { clause_id: DORA-C02, article_ref: "Art. 5(4) — `Members of the management body … shall actively keep up to date with sufficient knowledge and skills … including by following specific training on a regular basis, commensurate to the ICT risk being managed`" }
  linked_objectives: [SO-DORA-014]
  sub_domain: [D-08.3]
  nist_csf_mapping:
    - { id: PR.AT-03, title: "All senior executives understand their roles and responsibilities in achieving the organization's cybersecurity objectives" }
    - { id: GV.RR-01, title: "Organizational leadership is responsible and accountable for cybersecurity risk and promotes a risk-aware ethical culture" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(4) requires members of the management body of the financial entity
    to actively keep up to date with sufficient knowledge and skills to enable
    them to understand and assess ICT risk and its impact on the operations of
    the financial entity, including by following specific training on a
    regular basis, commensurate to the ICT risk being managed. The clause is
    the literacy underpinning of Art. 5(2) management-body responsibility and
    defines the personal-capacity threshold for Art. 5(2) to operate
    meaningfully. The clause co-exists with EBA Guidelines on Internal
    Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II
    Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4
    proportionality, training evidence can be proportionate to risk exposure.
  security_rationale: |
    The Art. 5(4) management-body literacy duty is operationalised in NIST
    CSF 2.0 through **PR.AT-03 (All senior executives understand their roles
    and responsibilities in achieving the organization's cybersecurity
    objectives)** and **GV.RR-01 (Organizational leadership is responsible
    and accountable for cybersecurity risk and promotes a risk-aware ethical
    culture)**. PR.AT-03 anchors the training-and-knowledge component — the
    `sufficient knowledge and skills` OJ phrase operationalised as documented
    role-and-responsibility literacy, evidence of `actively keep up to date`,
    and training records calibrated to the ICT risk being managed. GV.RR-01
    layers the accountability-and-culture dimension, ensuring that the
    management body's literacy is not decorative but tied to the personal-
    capacity prerequisite for the Art. 5(2) oversight-and-liability regime
    and to the broader fit-and-proper expectations under EBA Guidelines on
    Internal Governance, CRD Art. 91, and MiFID II Art. 4(1)(36)/(37). Together
    these two subcategories close the gap between training-attendance
    evidence and demonstrable governance competence, and an entity
    evidencing PR.AT-03 senior-executive literacy plus GV.RR-01 leadership
    accountability can demonstrate ex-post to supervisory review that the
    Art. 5(4) `sufficient knowledge and skills` obligation was met at
    personal-capacity level and that the management body was structurally
    positioned to discharge Art. 5(2) oversight responsibilities with
    informed judgement rather than ceremonial sign-off.
  ambiguity_notes: |
    S2 VAG on `sufficient` is read at the role-relevant-competency end of the
    spectrum per the `commensurate to the ICT risk` qualifier. S2 VAG on
    `regular basis` is read as risk-driven cadence per the literal
    `actively keep up to date` formulation (alternatives include scheduled or
    ongoing). S2 VAG on `commensurate to the ICT risk` — the chosen reading
    is risk-proportional rather than risk-quantified. S2 POLY on `actively
    keep up to date` — alternatives include self-study, formal training, or
    both; the chosen reading is the literal AND. Remain open: evidence
    forms for `actively keep up to date` (training-attendance logs,
    assessment scores, peer-benchmark exercises) remain for entity policy.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

