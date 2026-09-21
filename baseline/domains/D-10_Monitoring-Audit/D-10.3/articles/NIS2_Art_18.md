---
document_id: AEGIS-PREPROC-NIS2-ART-18
title: NIS2 Art. 18 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 18
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.3.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.3.md
status: DRAFT
---

# NIS2 Art. 18

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-037
  title: "Policy framework for assessing cybersecurity risk-management measure effectiveness"
  source_clauses:
    - { clause_id: NIS2-CL15, article_ref: "Art. 21(2)(f) — policies and procedures to assess effectiveness of cybersecurity risk-management measures" }
    - { clause_id: NIS2-CL07, article_ref: "Art. 21(1) — appropriate and proportionate (propagates)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art (cross)" }
  linked_objectives: [SO-NIS2-023]
  sub_domain: [D-09.1, D-09.3, D-10.3]
  nist_csf_mapping:
    - { id: GV.PO-01, title: "Organizational cybersecurity policy is established, communicated, and enforced" }
    - { id: ID.IM-01, title: "Improvement processes across cybersecurity risk management are identified and used" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS, PERIODIC]
  regulatory_rationale: |
    Article 21(2)(f) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding policies and procedures to assess the effectiveness of cybersecurity risk-management measures. The `effectiveness assessment` is the operational feedback loop for the Article 21 measures and is structurally distinct from the corrective-measures obligation of Article 21(4) (SR-NIS2-042): effectiveness assessment is the forward-looking measurement of whether the measures achieve their intended outcome, while corrective measures are the triggered response when assessment identifies non-compliance. The Article 21(1) appropriate-and-proportionate qualifier and Article 21(1) sentence 2 state-of-the-art and cost-of-implementation anchor propagate, with Recital 56 proportionality factors governing the assessment depth. The literal AND coordination of `policies and procedures` is read as requiring both a policy artefact and procedural operationalisation (NIST CSF 2.0 GV.PO-01 + GV.PO-02). The synthesis §3 mark identifies this sub-point as the Article 21 effectiveness POLY hotspot because the OJ uses the open-textured `effectiveness` term without defining the assessment object.
  security_rationale: |
    The obligation in Art. 21(2)(f) to take measures regarding policies and procedures to assess the effectiveness of cybersecurity risk-management measures is operationalised in NIST CSF 2.0 through **GV.PO-01 (Organisational cybersecurity policy is established, communicated, and enforced)**, **ID.IM-01 (Improvement processes across cybersecurity risk management are identified and used)**, and **GV.OV-03 (Organisational cybersecurity performance is evaluated and reviewed for needed adjustments)**. GV.PO-01 anchors the policy artefact: the entity maintains a documented effectiveness-assessment policy with named owners and a re-review cadence. ID.IM-01 anchors the improvement-process substrate: assessment findings feed the plan-do-check-act cycle and trigger measurable improvement actions that close identified gaps. GV.OV-03 anchors the performance-evaluation dimension: the policy defines metrics, review cadence, and the criteria for declaring an assessment finding material. Together, the three control elements close the effectiveness loop. The control set enables ex-post demonstration that the entity measures whether the Article 21 measures achieve their intended outcomes rather than treating compliance as a one-time check, and that the assessment outputs drive documented improvement actions.
  ambiguity_notes: |
    The compound `effectiveness` carries the Article 21(2)(f) POLY hotspot ambiguity with three operative readings: a control-effectiveness reading (does the control work as designed), a risk-effectiveness reading (does the control reduce risk to acceptable level), or an outcome-effectiveness reading (does the measure achieve its intended outcome), with the chosen reading being the outcome-effectiveness reading because the OJ is outcome-oriented (the assessment object is `cybersecurity risk-management measures` rather than specific controls), and Recital 56 framing supports outcome-measurement as the natural reading of `effectiveness of measures`. The AND coordination of `policies and procedures` admits a two-distinct-artefacts reading or a hendiadys (single artefact with two labels) reading, with the two-distinct reading being dominant because the OJ coordinates two governance terms that NIST CSF 2.0 treats as distinct sub-categories (GV.PO-01 policy and GV.PO-02 processes and procedures). The T3-vs-text gap awareness (synthesis §8) imports ISO 27004 measurement vocabulary not present in the OJ, and the SR preserves OJ-literal language while mapping to ID.IM-01 + GV.OV-03 (improvement + performance evaluation) by meaning-alignment rather than literal-import. Member State transposition divergence may apply on whether national supervisory authorities require specific effectiveness-assessment metrics (e.g. MTTD, MTTR, control-coverage percentage) or accept entity-discretionary metrics under the proportionality discipline. Remain open: (a) whether the Commission will adopt implementing acts under Article 21(5) that specify effectiveness-assessment metrics, which would convert the methodology-discretion interpretation into a metrics-conformance baseline; (b) whether the outcome-effectiveness reading requires the entity to demonstrate contribution-to-risk-reduction evidence under DORA Art. 18 testing parallel, or whether residual-risk-acceptance documentation suffices.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-038
  title: "Scheduled procedures operationalise cybersecurity effectiveness measurement"
  source_clauses:
    - { clause_id: NIS2-CL15, article_ref: "Art. 21(2)(f) — procedures (procedural dimension of effectiveness assessment, cross)" }
    - { clause_id: NIS2-CL08, article_ref: "Art. 21(1) sentence 2 — state-of-the-art (cross)" }
  linked_objectives: [SO-NIS2-023]
  sub_domain: [D-09.3, D-10.3]
  nist_csf_mapping:
    - { id: GV.PO-02, title: "Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced" }
    - { id: GV.OV-03, title: "Organizational cybersecurity performance is evaluated and reviewed for needed adjustments" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [PERIODIC]
  regulatory_rationale: |
    Article 21(2)(f) second limb of Directive (EU) 2022/2555 captures the procedural dimension of effectiveness assessment, with the policy dimension captured in SR-NIS2-037. Procedures operationalise the policies with concrete assessment cadence (audit frequency, test frequency, review frequency), evidence requirements (documentation, log retention, attestation), and the responsible-function allocation (CISO, internal audit, external auditor). The Article 21(1) sentence 2 state-of-the-art anchor propagates and is operationalised by Recital 56 proportionality. The SR captures the procedural half of the `policies and procedures` AND coordination in Article 21(2)(f), and is structurally lighter than SR-NIS2-037 because the substantive ambiguity lives in the policy half (the `effectiveness` POLY hotspot).
  security_rationale: |
    The obligation in Art. 21(2)(f) procedural limb to operationalise the effectiveness-assessment policy is operationalised in NIST CSF 2.0 through **GV.PO-02 (Cybersecurity processes and procedures for implementing the cybersecurity policy are established, communicated, and enforced)** and **GV.OV-03 (Organisational cybersecurity performance is evaluated and reviewed for needed adjustments)**. GV.PO-02 anchors the procedural artefact: documented procedures specify assessment cadence (internal audit, penetration test, control-effectiveness review, management-body dashboard review), evidence requirements (documentation, log retention, attestation), and responsible-function allocation (CISO, internal audit, external auditor) with named owners. GV.OV-03 anchors the evaluation discipline: each procedure generates performance evidence that the management body reviews against the policy of SR-NIS2-037 on a recurring cadence. Together, GV.PO-02 and GV.OV-03 connect procedural implementation to performance evaluation. The control set enables ex-post demonstration that the effectiveness assessment runs on a scheduled cadence and produces auditable evidence rather than ad-hoc reviews, with the cadence proportionate to the entity's exposure.
  ambiguity_notes: |
    The same `effectiveness` POLY hotspot ambiguity as SR-NIS2-037 propagates into this SR (the procedural half inherits the substantive reading of the policy half); the chosen outcome-effectiveness reading is preserved. The same T3-vs-text gap awareness (synthesis §8) applies: the OJ does not mention ISO 27004 measurement vocabulary, and the SR maps to GV.PO-02 + GV.OV-03 by meaning-alignment. The assessment cadence is not specified by the Directive (no analogue to GDPR Article 35(11) `at least when there is a change of the risk presented by processing operations`); the cadence is entity-discretionary under Recital 56 proportionality. Member State transposition divergence may apply on whether national supervisory authorities require specific procedural artefacts (e.g. annual external audit, semi-annual internal audit, quarterly management review) that convert the cadence-discretion interpretation into a procedural baseline. Remain open: whether Member State supervisory authorities will align their national effectiveness-assessment procedural expectations with the DORA Art. 18 ICT risk-management framework testing cadence (annual for significant ICT-risk-driven entities), which would create a cross-regulation cadence alignment.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

