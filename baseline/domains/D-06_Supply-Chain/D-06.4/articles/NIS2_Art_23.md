---
document_id: AEGIS-PREPROC-NIS2-ART-23
title: NIS2 Art. 23 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 23
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
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# NIS2 Art. 23

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-005 | An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents, including those with significant impact on the provision of services. | `NIS2-CL11` (Art. 21(2)(b) — incident handling); `NIS2-CL26` (Art. 23(1) ¶1 — significant-incident notification core); `NIS2-CL09` (Art. 21(2) chapeau — all-hazards approach); `NIS2-CL12` (Art. 21(2)(c) — BC/DR/CM, for the recovery dimension) | D-04.1, D-04.2, D-04.4 |
| SO-NIS2-006 | Significant incidents are notified to the CSIRT or, where applicable, the competent authority without undue delay, with an early warning submitted in any event within 24 hours of becoming aware of the significant incident and an incident notification submitted in any event within 72 hours of becoming aware, including severity, impact, and (where available) indicators of compromise. | `NIS2-CL26` (Art. 23(1) ¶1 — notification core); `NIS2-CL35` (Art. 23(4)(a) — 24h early warning); `NIS2-CL36` (Art. 23(4)(b) — 72h incident notification); `NIS2-CL28` (Art. 23(1) ¶1 — cross-border info); `NIS2-CL29` (Art. 23(1) ¶1 — no-increased-liability shield); `NIS2-CL30` (Art. 23(1) ¶2 — CA→CSIRT forwarding); `NIS2-CL31` (Art. 23(1) ¶3 — SPOC cross-border); `NIS2-CL45` (Art. 23(9) — ENISA quarterly, institutional — referenced for propagation) | D-04.3 |
| SO-NIS2-006 | D-04.3 | Art. 23(1) + Art. 23(4)(a)/(b) | 24h early warning + 72h incident notification (twin-trigger) |
| SO-NIS2-007 | A final incident report is submitted to the CSIRT or competent authority not later than one month after the incident notification, including a detailed description of the incident, the type of threat or root cause, applied and ongoing mitigation measures, and (where applicable) the cross-border impact. | `NIS2-CL38` (Art. 23(4)(d) — 1m final report) | D-04.3 |
| SO-NIS2-007 | D-04.3 | Art. 23(4)(d) | Final report not later than 1 month after notification |
| SO-NIS2-008 | Where an incident is ongoing at the time of the final report, a progress report is provided at that time and a closing final report is submitted within one month of the entity's handling of the incident. | `NIS2-CL39` (Art. 23(4)(e) — ongoing incident progress + closing final) | D-04.3 |
| SO-NIS2-008 | D-04.3 | Art. 23(4)(e) | Ongoing incident progress report + closing final report within 1 month of handling |
| SO-NIS2-009 | Trust service providers notify the CSIRT or competent authority without undue delay and in any event within 24 hours of becoming aware of a significant incident affecting the provision of their trust services (the TSP derogation, applicable regardless of the 72h/1m tier structure of the general notification flow). | `NIS2-CL40` (Art. 23(4) ¶2 — TSP 24h derogation) | D-04.3 |
| SO-NIS2-009 | D-04.3 | Art. 23(4) ¶2 | TSP 24h notification regardless of tier (derogation) |
| SO-NIS2-010 | An intermediate report on relevant status updates is provided on the request of a CSIRT or competent authority. | `NIS2-CL37` (Art. 23(4)(c) — intermediate report) | D-04.3 |
| SO-NIS2-010 | D-04.3 | Art. 23(4)(c) | Intermediate report on CSIRT/CA request |
| SO-NIS2-011 | Recipients of services that are potentially affected by a significant incident or by a significant cyber threat are notified of the incident or threat and informed of measures or remedies they can take in response. | `NIS2-CL27` (Art. 23(1) ¶1 — recipient notification of significant incidents); `NIS2-CL32` (Art. 23(2) — recipient notification of significant cyber threats + countermeasures) | D-04.3 |
| SO-NIS2-011 | D-04.3 | Art. 23(1) ¶1 + Art. 23(2) | Recipient notification of significant incidents + significant cyber threats |
| SO-NIS2-012 | Cross-MS notification: where a significant incident concerns two or more Member States, the CSIRT, competent authority, or single point of contact informs other affected Member States and ENISA without undue delay. | `NIS2-CL42` (Art. 23(6) — cross-MS notification); `NIS2-CL44` (Art. 23(8) — SPOC forwarding); `NIS2-CL46` (Art. 23(10) — CER cross-sharing, institutional — referenced for propagation); `NIS2-CL43` (Art. 23(7) — public disclosure if in public interest; authority-initiated) | D-04.3 |
| SO-NIS2-012 | D-04.3 | Art. 23(6)/(8)/(10)/(7) | Cross-MS notification, SPOC forwarding, CER cross-sharing, public disclosure |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-010
  title: "24-hour early-warning notification upon incident awareness"
  source_clauses:
    - { clause_id: NIS2-CL35, article_ref: "Art. 23(4)(a) — 24h early warning" }
    - { clause_id: NIS2-CL26, article_ref: "Art. 23(1) ¶1 — notification core" }
    - { clause_id: NIS2-CL33, article_ref: "Art. 23(3)(a) — significant-incident test A" }
    - { clause_id: NIS2-CL34, article_ref: "Art. 23(3)(b) — significant-incident test B" }
  linked_objectives: [SO-NIS2-006]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-02, title: "Incident reports are triaged and validated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4)(a) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact (OJ L 333, 27.12.2022, p. 129). Article 23(1) paragraph 1 anchors the notification core: essential and important entities notify the CSIRT or competent authority of any significant incident without undue delay, in accordance with Article 23(4). Article 23(3) defines `significant incident` via two alternative tests — test A (severe operational disruption or financial loss for the entity concerned) or test B (considerable material or non-material damage to other natural or legal persons). The 24-hour clock is the hard ceiling; `without undue delay` is the primary trigger that may require earlier notification depending on incident characteristics. The Article 23(11) implementing acts mandate (NIS2-CL47) for the 10 digital-infrastructure categories (DNS service providers, TLD name registries, cloud computing, data centre, CDN, MSP, MSSP, online marketplaces, search engines, social-networking platforms) is pending and may close the definitional regress on `severe` and `considerable` for those categories.
  security_rationale: |
    The Article 23(4)(a) obligation to submit a 24-hour early warning to the CSIRT or competent authority upon becoming aware of a significant incident is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RS.MA-02 (Incident reports are triaged and validated)**. RS.CO-04 specifies the coordination discipline: the 24-hour window is a regulatory clock, the CSIRT or competent authority is the regulatory stakeholder, and the entity's notification procedure must integrate that clock into its incident lifecycle so that the early-warning leaves the entity within the ceiling, with the cross-border-impact and suspected-unlawful-act indicators the Article 23(4)(a) text requires. RS.MA-02 supplies the upstream triage discipline: the entity cannot submit a defensible early warning without first triaging the event against the Article 23(3) test-A and test-B significant-incident criteria and validating the assessment internally. The two subcategories together address the two distinct demands the 24-hour clock places on the entity — coordination under the regulatory clock and triage under uncertainty. The resulting early-warning records, triage decisions and awareness timestamps constitute the accountability evidence under Article 21(1) and the foundation on which the downstream 72h and 1m notifications rest.
  ambiguity_notes: |
    `Without undue delay and in any event within 24 hours` is an S3 twin-trigger pattern: `without undue delay` is the primary trigger (some incidents may justify earlier notification — e.g. active data exfiltration); 24 hours is the hard ceiling. The chosen reading is R1 (primary trigger with hard ceiling). `Becoming aware` is an S3 polysemy: actual awareness (R1, the literal OJ reading — the moment an employee or system records the incident), constructive awareness (R2, the dominant CJEU reading — what a properly-organised entity should have known), or either (R3). R1 is the literal OJ reading; R2 is the dominant CJEU reading and is the basis for supervisory enforcement. `Severe operational disruption` and `considerable material or non-material damage` are S3 vague terms — both `severe` and `considerable` are undefined; this is the definitional regress flagged in the synthesis §4.5 and the Commission implementing-acts mandate under Article 23(11) is the closing mechanism (currently pending). Member State transposition divergence may apply; national CSAs may pre-publish thresholds (e.g. France ANSSI's incident-classification matrix; Germany BSI's significant-incident catalogue under §8b BSIG). Remain open: (a) whether the Article 23(11) implementing acts will set quantitative thresholds for `severe` and `considerable` across the 10 digital-infrastructure categories — the directive is silent on operationalisation and the pending acts were due 17 October 2024; (b) whether Member State national transposition will tighten or relax the `becoming aware` construct (e.g. German BSI may adopt constructive-awareness for the federal sector; other MS may stay with literal OJ actual-awareness).
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-011
  title: "72-hour incident notification with initial assessment"
  source_clauses:
    - { clause_id: NIS2-CL36, article_ref: "Art. 23(4)(b) — 72h incident notification" }
    - { clause_id: NIS2-CL26, article_ref: "Art. 23(1) ¶1 — notification core" }
    - { clause_id: NIS2-CL33, article_ref: "Art. 23(3)(a) — significant-incident test A" }
    - { clause_id: NIS2-CL34, article_ref: "Art. 23(3)(b) — significant-incident test B" }
  linked_objectives: [SO-NIS2-006]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4)(b) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 72 hours of becoming aware of the significant incident, an incident notification which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise (OJ L 333, 27.12.2022, p. 129). The 72-hour notification updates the 24-hour early warning and provides the substantive incident assessment — severity, impact, and (where available) indicators of compromise (IoCs). The Article 23(3) significant-incident definition via test A or test B is the gating condition. Article 23(1) paragraph 1 anchors the notification core. The Article 23(11) implementing-acts mandate applies (same as SR-NIS2-010) for the 10 digital-infrastructure categories.
  security_rationale: |
    The Article 23(4)(b) obligation to submit a 72-hour incident notification updating the 24-hour early warning with an initial assessment — including severity, impact and, where available, indicators of compromise — is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RS.MA-03 (Incidents are categorized, prioritized, and scoped)**. RS.CO-04 anchors the regulatory-clock discipline: the 72-hour window is the second tier of the Article 23 reporting cascade, and the entity's procedure must ensure the notification updates rather than duplicates the 24-hour submission, transmits through the CSIRT or competent-authority channel, and supplies the cross-border and suspected-unlawful-act context where applicable. RS.MA-03 supplies the categorisation substrate on which the substantive content depends: severity, impact, scope and prioritisation must each be defensible, with the indicators of compromise (where available) drawn from a validated analysis pipeline. The two subcategories together address the regulatory-clock dimension and the substantive-content dimension of the 72-hour obligation. The resulting notification records, categorisation outputs and IoC artefacts support the cross-border coordination under Article 23(6) and constitute the accountability evidence the Article 21(1) framework requires.
  ambiguity_notes: |
    Same S3 twin-trigger pattern as SR-NIS2-010 at 72 hours; the chosen reading is R1 (primary trigger `without undue delay`, hard ceiling 72 hours). `Becoming aware` (S3 POLY+SCOPE-Q) carries the same R1 literal / R2 dominant-CJEU readings as SR-NIS2-010. `Indicators of compromise` is an S2 polysemy (technical indicators — hashes, IPs, domains; behavioural indicators — TTPs; or any); the chosen reading is R3 (mechanism-agnostic per the OJ). `Where available` is a soft hedge on IoC inclusion — best-effort, not exhaustive. Member State transposition divergence may apply on IoC granularity and on national incident-classification matrices. Remain open: (a) whether the Article 23(11) implementing acts will specify minimum IoC-disclosure granularity for the 10 digital-infrastructure categories; (b) whether the `where available` hedge will be operationalised by national supervisory authorities as a duty to disclose when in possession of IoCs, or as a permissive allowance to withhold incomplete data — the directive is silent.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-012
  title: "One-month final report closing the regulatory loop"
  source_clauses:
    - { clause_id: NIS2-CL38, article_ref: "Art. 23(4)(d) — 1m final report" }
    - { clause_id: NIS2-CL36, article_ref: "Art. 23(4)(b) — 72h notification (anchor for the 1m clock)" }
  linked_objectives: [SO-NIS2-007]
  sub_domain: [D-04.3, D-04.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RC.RP-06, title: "End of incident recovery declared based on established criteria, and after-action review completed" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4)(d) of Directive (EU) 2022/2555 requires the entity to submit a final report not later than one month after the submission of the incident notification under point (b), including: (i) a detailed description of the incident, including its severity and impact; (ii) the type of threat or root cause that is likely to have triggered the incident; (iii) applied and ongoing mitigation measures; (iv) where applicable, the cross-border impact of the incident (OJ L 333, 27.12.2022, p. 129). The 1-month clock runs from the submission of the Article 23(4)(b) 72-hour notification, not from incident detection or from the 24-hour early warning.
    [OJ-corrective note (v0.2 audit, cosmetic): the OJ text reads verbatim — Art. 23(4)(d) requires a final report including (i) a detailed description of the incident, including its severity and impact; (ii) the type of threat or root cause that is likely to have triggered the incident; (iii) applied and ongoing mitigation measures; (iv) where applicable, the cross-border impact of the incident.]
  security_rationale: |
    The Article 23(4)(d) obligation to submit a final report within one month of the 72-hour notification, including detailed description, likely threat or root cause, applied and ongoing mitigation measures, and cross-border impact where applicable, is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RC.RP-06 (The end of incident recovery is declared based on established criteria, and after-action review is completed)**. RS.CO-04 anchors the regulatory-clock discipline: the one-month clock runs from the 72-hour notification submission, and the entity's procedure must ensure the final report lands within the ceiling and follows the four-part structure the Article 23(4)(d) text prescribes. RC.RP-06 supplies the recovery-completion discipline on which the report's substantive content depends: the entity cannot declare the incident closed in regulatory terms until the recovery criteria are met and an after-action review has been completed, ensuring the final report reflects a defended closure rather than a calendar deadline. The two subcategories together address the regulatory-clock dimension and the substantive-recovery dimension of the 1-month obligation. The resulting report, alongside the after-action review record, supplies the supervisory aggregation work under Article 23(9) and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `One month` admits calendar-month (R1, literal OJ), 30-day (R2), and working-month (R3) readings; the chosen reading is R1 calendar-month per the literal OJ. `Detailed description` admits comprehensive (R1) and sufficient-for-CSIRT (R2) readings; R1 preferred because the four sub-points structure provides the minimum content. `Root cause` admits technical (R1), organisational (R2), and procedural (R3) readings; the chosen reading is mechanism-agnostic (any) per the literal OJ. Member State transposition divergence may apply on the clock interpretation (calendar vs. 30-day). Remain open: whether the Commission's Article 23(11) implementing acts will standardise the final-report format across the 10 digital-infrastructure categories.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-013
  title: "Progress and closing reports for ongoing incidents"
  source_clauses:
    - { clause_id: NIS2-CL39, article_ref: "Art. 23(4)(e) — ongoing incident progress report + closing final report" }
  linked_objectives: [SO-NIS2-008]
  sub_domain: [D-04.3, D-04.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RC.RP-06, title: "End of incident recovery declared based on established criteria, and after-action review completed" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4)(e) of Directive (EU) 2022/2555 requires the entity, in the event of an ongoing incident at the time of the submission of the final report referred to in point (d), to provide a progress report at that time and a final report within one month of the entity's handling of the incident (OJ L 333, 27.12.2022, p. 129). The provision preserves the reporting obligation while acknowledging that the incident has not concluded; the 1-month clock restarts on `handling` — the moment the entity's incident-handling process under Article 6(8) concludes.
  security_rationale: |
    The Article 23(4)(e) obligation to provide a progress report at the time the 1-month final report is due when the incident is still ongoing, and a closing final report within one month of the entity's handling of the incident, is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RC.RP-06 (The end of incident recovery is declared based on established criteria, and after-action review is completed)**. RS.CO-04 anchors the regulatory-cadence discipline: the progress report preserves the notification cadence while acknowledging that the substantive incident has not concluded, and the entity's procedure must specify who decides, on the basis of which incident-state evidence, that an incident is `ongoing` for Article 23(4)(e) purposes. RC.RP-06 supplies the closure discipline on which the second, closing final report depends: the one-month clock for the closing report runs from the entity's completion of its handling of the incident, and the report must reflect an after-action review that has actually been performed. The two subcategories together address the cadence-preservation dimension and the closure-discipline dimension of the ongoing-incident obligation. The resulting progress reports and closing report, with their after-action records, supply the supervisory aggregation work and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Ongoing incident` admits still-under-containment (R1), recovery-phase (R2), and either (R3) readings; the chosen reading is R3 (literal OJ — the directive does not distinguish containment from recovery as gating conditions). `Within one month of their handling of the incident` — the 1-month clock restarts on `handling`, which is an S2 polysemy inheriting the Article 6(8) process/team/capability readings; the chosen reading is process-completion per the literal `handling` anchor. Member State transposition divergence may apply on the criteria for declaring an incident `ongoing` versus `closed` — some MS require the CSIRT to acknowledge closure; others accept entity-self-determination. Remain open: whether the Commission's Article 23(11) implementing acts will specify closure criteria for ongoing incidents across the 10 digital-infrastructure categories.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-014
  title: "24-hour derogation notification for trust service providers"
  source_clauses:
    - { clause_id: NIS2-CL40, article_ref: "Art. 23(4) ¶2 — TSP 24h derogation" }
    - { clause_id: NIS2-D02, article_ref: "Art. 6(24) — trust service (eIDAS cross-reference)" }
  linked_objectives: [SO-NIS2-009]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.MA-03, title: "Incidents are categorized, prioritized, and scoped" }
  applies_to_role: [ESSENTIAL_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4) paragraph 2 of Directive (EU) 2022/2555 derogates from the Article 23(4)(b) 72-hour notification tier: a trust service provider shall, with regard to significant incidents that have an impact on the provision of its trust services, notify the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident (OJ L 333, 27.12.2022, p. 129). The Article 6(24) definition of `trust service` references Regulation (EU) No 910/2014 (eIDAS), so the derogation applies to eIDAS-defined trust service providers and qualified trust service providers. Annex I of NIS 2 includes eIDAS qualified trust service providers as essential entities; Annex II includes digital providers as important entities, but the substantive eIDAS obligations attach to the QTSP designation regardless of the Annex II classification. The `applies_to_role: ESSENTIAL_ENTITY` reflects the Annex I/QTSP designation. The twin-trigger pattern (`without undue delay and in any event within 24 hours`) is identical to SR-NIS2-010 (same reading structure).
  security_rationale: |
    The Article 23(4) paragraph 2 derogation requiring trust service providers (per Article 6(24) and the eIDAS cross-reference) to submit a 24-hour notification for significant incidents affecting the provision of their trust services, derogating from the Article 23(4)(b) 72-hour tier, is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RS.MA-03 (Incidents are categorized, prioritized, and scoped)**. RS.CO-04 anchors the regulatory-clock discipline: the 24-hour tier is shorter than the 72-hour tier it derogates from, and the entity's procedure must ensure the trust-service-provision scope is correctly identified and the notification channel is the one designated for the TSP's national supervisory body and CSIRT. RS.MA-03 supplies the categorisation discipline on which the substantive content depends: the entity must distinguish trust-service-affecting incidents from non-trust-service incidents, and apply the more stringent tier only to the former, so that the derogation is targeted rather than generalised. The two subcategories together address the regulatory-clock dimension and the scope-discipline dimension of the TSP derogation. The resulting notification records and categorisation outputs supply the supervisory feed on which the cross-border eIDAS coordination depends and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    The TSP derogation applies only to trust service providers as defined in Article 6(24) (the eIDAS cross-reference). The chosen reading is that the derogation applies to QTSPs (qualified trust service providers per Annex I) and to TSPs in scope of Article 6(24) more broadly (non-qualified trust service providers may be subject to the derogation if they meet the eIDAS trust-service definition). Member State transposition divergence may apply; national supervisory authorities may publish sector-specific guidance. Remain open: whether non-qualified TSPs in Annex II (important entity classification) can opt into the 24-hour derogation by agreement with the national CSIRT, or whether the derogation is reserved to Annex I QTSPs.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-015
  title: "On-demand intermediate status reports to the CSIRT"
  source_clauses:
    - { clause_id: NIS2-CL37, article_ref: "Art. 23(4)(c) — intermediate report on CSIRT request" }
  linked_objectives: [SO-NIS2-010]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: RS.AN-07, title: "Incident data and metadata are collected, and their integrity and provenance are preserved" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(4)(c) of Directive (EU) 2022/2555 requires the entity, upon the request of a CSIRT or, where applicable, the competent authority, to provide an intermediate report on relevant status updates (OJ L 333, 27.12.2022, p. 129). The intermediate report is on-demand; no fixed schedule applies. The CSIRT or competent authority sets the cadence. The obligation is independent of the 24h/72h/1m tier structure (SR-NIS2-010, SR-NIS2-011, SR-NIS2-012): the intermediate report may be requested at any time during the incident lifecycle.
  security_rationale: |
    The Article 23(4)(c) obligation to provide, on the request of the CSIRT or competent authority, an intermediate report on relevant status updates is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **RS.AN-07 (Incident data and metadata are collected, and their integrity and provenance are preserved)**. RS.CO-04 anchors the on-demand coordination discipline: the CSIRT or competent authority sets the cadence and the entity must respond within it, so the procedure must keep an incident-state record current enough to support an intermediate report at any point in the lifecycle, independent of the 24h/72h/1m tier structure. RS.AN-07 supplies the data-integrity discipline on which the intermediate report's evidential value depends: the report draws on incident data and metadata whose integrity and provenance are preserved from the moment of capture, so the regulator can rely on the timeline, scope and indicators reported without an independent forensic check. The two subcategories together address the on-demand dimension and the evidence-integrity dimension of the intermediate-report obligation. The resulting status snapshots, backed by preserved incident records, supply the supervisory situational-awareness feed and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Relevant status updates` admits technical (R1), impact (R2), and both (R3) readings; the chosen reading is R3 (literal OJ — `relevant` is mechanism-agnostic). `Upon the request` is on-demand with no temporal anchor; the regulator sets the cadence. Member State transposition divergence may apply on the requesting authority's discretion (some MS may publish criteria for when intermediate reports are requested). Remain open: whether the Commission's Article 23(11) implementing acts will specify a minimum cadence or trigger conditions for intermediate-report requests.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-016
  title: "Recipient notification of significant service-affecting incidents"
  source_clauses:
    - { clause_id: NIS2-CL27, article_ref: "Art. 23(1) ¶1 — recipient notification of significant incidents" }
    - { clause_id: NIS2-CL26, article_ref: "Art. 23(1) ¶1 — significant-incident trigger" }
  linked_objectives: [SO-NIS2-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(1) paragraph 1 second sentence of Directive (EU) 2022/2555 requires entities, where appropriate, to notify without undue delay the recipients of their services of significant incidents that are likely to adversely affect the provision of those services (OJ L 333, 27.12.2022, p. 128). The recipient-notification flow is the user-facing twin of the CSIRT-side notification (SR-NIS2-010 / SR-NIS2-011). The Article 23(3) significant-incident definition applies. The `where appropriate` hedge and the `without undue delay` standard are softer than the CSIRT-side 24-hour hard ceiling.
  security_rationale: |
    The Article 23(1) paragraph 1 second-sentence obligation to notify, where appropriate and without undue delay, the recipients of services of significant incidents likely to adversely affect the provision of those services is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules)** and **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)**. RS.CO-03 supplies the information-sharing discipline: the entity's procedure must define which recipients receive which artefacts under which triggering conditions, with the recipient-notification channel separated from the regulator-side flow and from any service-affecting public statement. RS.CO-04 anchors the regulatory-compliance dimension: the recipient notification must respect the Article 23(3) significant-incident test, the `where appropriate` and `without undue delay` qualifiers, and the supervisory-side rules the entity operates under, so that recipient messaging does not undercut the regulator-side coordination. The two subcategories together address the information-sharing dimension and the regulatory-alignment dimension of the recipient-notification obligation. The resulting notification records and message-routing evidence supply the accountability base on which the entity demonstrates, ex post under Article 21(1), that its recipient-side communication was timely, targeted and coordinated.
  ambiguity_notes: |
    `Where appropriate` (S2 VAG hedge) admits system (R1), user (R2), risk (R3), and cost (R4) readings; R3 is dominant per the Article 21(1) factors propagation. `Without undue delay` (S2 VAG) admits 24h (R1) and reasonable-time (R2) readings; R2 is dominant per Recital 60 and standard EU drafting. `Likely to adversely affect` (S2 VAG) admits >50% (R1), >10% (R2), and any-non-zero-probability (R3) readings; R3 is literal. Member State transposition divergence may apply on the threshold for recipient notification. Remain open: whether the Commission's Article 23(11) implementing acts will specify a minimum recipient-notification timeline or rely on the soft `without undue delay` standard.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-017
  title: "Proactive threat and remedy communication to recipients"
  source_clauses:
    - { clause_id: NIS2-CL32, article_ref: "Art. 23(2) — recipient notification of significant cyber threats + countermeasures" }
  linked_objectives: [SO-NIS2-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated internal and external stakeholders consistent with the established information-sharing rules" }
    - { id: RS.MI-01, title: "Incidents are contained" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(2) of Directive (EU) 2022/2555 requires entities, where applicable, to communicate without undue delay to the recipients of their services that are potentially affected by a significant cyber threat any measures or remedies that those recipients are able to take in response to that threat; where appropriate, the entities shall also inform those recipients of the significant cyber threat itself (OJ L 333, 27.12.2022, p. 128). The threat-communication flow is the upstream twin of the incident-notification flow (SR-NIS2-016) — entities communicate about a threat before it materialises as an incident. The `significant cyber threat` definition inherits the `severe`/`considerable` definitional regress from Article 23(3) (synthesis §4.5) and the Article 6(11) cross-reference to Regulation (EU) 2019/881.
  security_rationale: |
    The Article 23(2) obligation to communicate, where applicable and without undue delay, to potentially affected recipients the measures or remedies they may take in response to a significant cyber threat, and where appropriate the threat itself, is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information is shared with designated internal and external stakeholders consistent with the established information-sharing rules)** and **RS.MI-01 (Incidents are contained)**. RS.CO-03 supplies the proactive-information-sharing discipline: the entity's procedure must define which recipients are in scope of the threat-communication flow, which messages are sent under which triggering conditions, and how the threat information travels separately from any service-affecting public statement. RS.MI-01 supplies the upstream containment-discipline framing on which the threat communication depends: by telling recipients what to do (patch, configuration change, monitoring uplift), the entity is in effect extending the containment perimeter to the recipient side, so the message content must be evidence-based and actionable. The two subcategories together address the proactive-sharing dimension and the recipient-side containment dimension of the threat-communication obligation. The resulting threat messages, with the triggering-evidence record, supply the supervisory feed on proactive disclosure and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `Significant cyber threat` inherits the `severe`/`considerable` definitional regress from Article 23(3); the literal OJ reading is preserved. `Measures or remedies` admits technical / corrective readings; the chosen reading is both (literal OR). `Where appropriate` for the threat-disclosure dimension is an S2 VAG hedge; the chosen reading is risk-based (R3) per Article 21(1) factors. Member State transposition divergence may apply on the criteria for proactive threat disclosure. Remain open: whether the Commission's Article 23(11) implementing acts will specify a baseline threat-disclosure framework for the 10 digital-infrastructure categories.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-018
  title: "Cross-border notification across Member States and ENISA"
  source_clauses:
    - { clause_id: NIS2-CL42, article_ref: "Art. 23(6) — cross-MS notification + ENISA" }
    - { clause_id: NIS2-CL44, article_ref: "Art. 23(8) — SPOC forwarding" }
    - { clause_id: NIS2-CL31, article_ref: "Art. 23(1) ¶3 — SPOC cross-border (entity-side)" }
  linked_objectives: [SO-NIS2-012]
  sub_domain: [D-04.3, D-06.4]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: GV.SC-05, title: "Response and recovery planning and testing are conducted with suppliers and other third parties" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY, SINGLE_POINT_OF_CONTACT]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(6) of Directive (EU) 2022/2555 requires the CSIRT, the competent authority or the single point of contact, where appropriate and in particular where the significant incident concerns two or more Member States, to inform without undue delay the other affected Member States and ENISA of the significant incident (OJ L 333, 27.12.2022, p. 129). Article 23(8) requires the single point of contact, at the request of the CSIRT or the competent authority, to forward notifications received under Article 23(1) to the single points of contact of other affected Member States. Article 23(1) paragraph 3 requires that, for cross-border or cross-sectoral significant incidents, Member States ensure that their single points of contact are provided in due time with relevant information notified under Article 23(4). The SPOC is MS-designated under Article 8 (national framework). The cross-regulation propagation to the CER Directive under Article 23(10) is institutional — the CER authority is informed through the CSIRT/CA, not directly by the entity.
  security_rationale: |
    The Article 23(6) and 23(8) and 23(1) paragraph 3 obligations on cross-border notification, single-point-of-contact forwarding, and cross-border/cross-sectoral incident handling are operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **GV.SC-05 (Response and recovery planning and testing are conducted with suppliers and other third parties)**. RS.CO-04 anchors the multi-stakeholder coordination discipline: the cross-border flow involves the affected Member States' SPOCs, ENISA and, where relevant, the EU-CyCLONe network under Article 16, and the entity's procedure must ensure the cross-MS escalation triggers are defined and the SPOC forwarding under Article 23(8) is executable on CSIRT request. GV.SC-05 supplies the third-party-response discipline: cross-border incident handling involves suppliers and peer entities (Article 6(7) large-scale incident framing), and the response-and-recovery planning and testing the entity conducts with them is what allows the cross-MS flow to operate against rehearsed rather than improvised procedures. The two subcategories together address the multi-stakeholder coordination dimension and the third-party-response dimension of the cross-MS obligation. The resulting SPOC records, forwarding logs and cross-border test evidence supply the Union-level situational-awareness feed and the accountability evidence under Article 21(1).
  ambiguity_notes: |
    `In due time` (S2 VAG) admits reasonable-time (R1, literal), tighter-than-`without undue delay` (R2), and tied-to-processing (R3) readings; R1 is literal. `Two or more Member States` (S2 SCOPE-Q) admits specific pre-identified (R1) and any-combination (R2) readings; R2 is dominant per standard EU drafting practice. `Cross-border OR cross-sectoral` (S2 COORD) admits either (R3) reading; R3 is literal. Member State transposition divergence may apply on the SPOC designation and on the criteria for cross-MS escalation. Remain open: whether the Commission's Article 23(11) implementing acts will specify escalation criteria across the 10 digital-infrastructure categories for cross-MS notification.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-041
  title: "Physical-environment protection ensures NIS substrate resilience"
  source_clauses:
    - { clause_id: NIS2-CL09, article_ref: "Art. 21(2) chapeau — protection of the physical environment of those systems" }
  linked_objectives: [SO-NIS2-022]
  sub_domain: [D-09.1]
  nist_csf_mapping:
    - { id: GV.RM-06, title: "Standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 21(2) chapeau second clause of Directive (EU) 2022/2555 extends the all-hazards approach of SR-NIS2-040 to `the physical environment of those systems`, capturing the physical substrate (server rooms, data centres, network equipment closets, edge facilities) that hosts the NIS and whose physical compromise propagates to NIS availability, integrity and confidentiality. The Article 21(1) appropriate-and-proportionate qualifier propagates and governs the physical-environment scope. The SR is structurally a carve-out flag: it captures the physical-security dimension explicitly in scope of Article 21 but out-of-scope for the software-compliance track of AEGIS, since the obligation is a physical-security obligation rather than a software-security obligation.
  security_rationale: |
    The obligation in Art. 21(2) chapeau second clause that the all-hazards approach extends to the physical environment of network and information systems is operationalised in NIST CSF 2.0 through **GV.RM-06 (Standardised method for calculating, documenting, categorising, and prioritising cybersecurity risks is established and communicated)** and, by extension, **PR.IR-02 (The organisation's technology assets are protected from environmental threats)** as the closest CSF control for the physical substrate. GV.RM-06 anchors the meta-methodology that captures the physical-environment dimension: the entity's risk-calibration methodology enumerates physical-environment hazards (intrusion, theft, sabotage, fire, flooding, environmental-control failure) and assigns them to the NIS-availability and NIS-integrity dimensions. Because the SR is structurally a carve-out flag for the physical-security dimension (out-of-scope for the software-compliance track of AEGIS), the mapping is meta-methodological rather than software-security specific. The control set enables ex-post demonstration that the entity considered the physical substrate as an integral element of the all-hazards methodology rather than as a separable concern.
  ambiguity_notes: |
    The compound `physical environment of those systems` carries a SCOPE-Q S2 ambiguity with three readings: a narrow reading (server rooms, data centres, network equipment closets), a medium reading (buildings including offices and call centres that host NIS-supporting staff), or a broad reading (surrounding critical infrastructure including power, cooling and telecoms). The narrow reading is the chosen OJ-literal reading because the qualifier `of those systems` anchors the physical environment to the NIS rather than to the entity's broader footprint. The SR is OUT-OF-SCOPE for the software-compliance track: it captures a physical-security requirement, not a software requirement, and Layer 3 (inference-trust) must adjudicate whether software-software integration controls are needed for the physical-environment dimension (e.g. environmental sensors feeding into security monitoring tooling, physical-access-control-system event correlation with identity governance). The SR maps to GV.RM-06 as a meta-methodology reference and does not generate software-security rules for downstream phases. Member State transposition divergence may apply on whether national supervisory authorities expect a documented physical-environment risk assessment as a sub-component of the all-hazards methodology. Remain open: (a) whether the narrow reading requires a separate physical-environment risk-assessment document or whether the all-hazards methodology under SR-NIS2-040 covers it implicitly; (b) whether the broad-reading interpretation applies to NIS-supporting critical infrastructure operators under the CER Directive cross-link (Art. 23(10) CER cross-sharing), which would couple this SR with the CER resilience obligation.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-044
  title: "Notification routing between competent authorities and CSIRTs"
  source_clauses:
    - { clause_id: NIS2-CL30, article_ref: "Art. 23(1) ¶2 — CA forwards notification to CSIRT upon receipt" }
    - { clause_id: NIS2-CL26, article_ref: "Art. 23(1) ¶1 — CSIRT or competent authority routing" }
  linked_objectives: [SO-NIS2-006]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-04, title: "Coordination with stakeholders occurs consistent with applicable rules and regulations" }
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [COMPETENT_AUTHORITY, CSIRT]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Article 23(1) ¶2 of Directive (EU) 2022/2555 requires that, where the entity notifies the competent authority, the Member State shall ensure that the competent authority forwards the notification to the CSIRT upon receipt. The routing is an authority-side obligation rather than an entity-side obligation; the entity-side counterpart (notifying the appropriate authority) is captured by SR-NIS2-010/011. The Article 23(1) ¶1 chapeau establishes the MS-determined routing architecture (`CSIRT or, where applicable, its competent authority`), so that the entity directs the initial notification to the entry-point authority determined by the Member State structure, and the entry-point authority performs the CSIRT-forwarding obligation under SR-NIS2-044 when the entry point is the competent authority.
  security_rationale: |
    The obligation in Art. 23(1) paragraph 2 that, where the entity notifies the competent authority, the competent authority forwards the notification to the CSIRT upon receipt is operationalised in NIST CSF 2.0 through **RS.CO-04 (Coordination with stakeholders occurs consistent with applicable rules and regulations)** and **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed)**. RS.CO-04 anchors the routing architecture: the authority-side forwarding rule is the operational instrument that converts an entry-point notification into the operational coordination with the CSIRT (incident handling, cross-border cascade under Article 23(3), ENISA quarterly aggregation under Article 23(9)). GV.OC-03 anchors the legal-frame substrate: the authority maintains a current register of the Member-State-determined routing architecture (CSIRT as single-entry-point, or competent authority as entry point with CSIRT as operational coordinator). Together, RS.CO-04 and GV.OC-03 close the parallel-and-complementary CSIRT-CA architecture that Articles 8 and 9 establish. The control set enables ex-post demonstration that notifications reached the operational CSIRT irrespective of the entry-point authority, with documented forwarding evidence.
  ambiguity_notes: |
    The temporal anchor `upon receipt` admits three readings: an immediate-reading (within minutes or hours of receipt), a same-day reading (within 24 hours of receipt), or a within-24h reading (parallel to the Article 23(5) CSIRT-response deadline), with the chosen reading being the immediate reading because `upon receipt` is a literal temporal anchor that admits no scheduling delay. The CSIRT-CA routing is Member-State-determined (Article 23(1) ¶1 `CSIRT or, where applicable, its competent authority`), so the entity's notification routing depends on the MS-determined structure; some Member States designate the CSIRT as the single-entry-point, while others designate the competent authority with the CSIRT as the operational coordinator that receives the forwarded notification under SR-NIS2-044. The SR's `applies_to_role` is COMPETENT_AUTHORITY and CSIRT — the forwarding is an authority-side obligation; the entity-side counterpart (notifying the appropriate authority per the MS-determined routing) is captured by SR-NIS2-010/011. Member State transposition divergence may apply on the routing architecture and on the documentation expected to evidence the forwarding. Remain open: whether Member State supervisory authorities will adopt a uniform CSIRT-CA routing convention that converts the routing-discretion interpretation into a conformance baseline, or whether each Member State retains full architectural discretion and the divergence compounds over the 27 implementations.
```

### SO-NIS2-001 (cryptography policies and procedures)

```yaml
- sr_id: SR-NIS2-045
  title: "Good-faith incident notification shielded from increased liability exposure"
  source_clauses:
    - { clause_id: NIS2-CL29, article_ref: "Art. 23(1) ¶1 — mere act of notification shall not subject the notifying entity to increased liability" }
  linked_objectives: [SO-NIS2-006]
  sub_domain: [D-04.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed" }
  applies_to_role: [ESSENTIAL_ENTITY, IMPORTANT_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Article 23(1) ¶1 fourth sentence of Directive (EU) 2022/2555 establishes that the mere act of notification shall not subject the notifying entity to increased liability. The clause is the liability-shield instrument of the Article 23 reporting architecture: the entity that notifies in good faith is protected against liability escalation that could otherwise attach to the act of disclosure (e.g. contractual liability to customers for breach of confidentiality, regulatory liability for late notification under other instruments, criminal liability under national cybersecurity-offence statutes). The shield is the legal-incentive instrument that encourages prompt notification and prevents the chilling effect that would otherwise undermine the entire reporting architecture.
  security_rationale: |
    The obligation in Art. 23(1) paragraph 1 fourth sentence that the mere act of notification shall not subject the notifying entity to increased liability is operationalised in NIST CSF 2.0 through **GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed)**. GV.OC-03 anchors the liability-shield register: the entity maintains a current register of the Member-State-defined shield scope (administrative, civil, criminal liability types shielded) and the operational trigger conditions under which the shield attaches (good-faith notification, Article 23 routing, time-of-notification). The register converts the OJ's liability-shield instrument from an abstract legal protection into an operational compliance-management artefact that the entity can demonstrate to supervisory authorities. GV.OC-03 is also the substrate for the cross-regulation propagation: the register distinguishes the Article 23 NIS2 shield from adjacent notification regimes (GDPR Art. 33 personal-data-breach notification, DORA Art. 19 major ICT-related incident notification) that may carry their own shield arrangements. The control set enables ex-post demonstration that the entity notified in good faith and that the shield applied to the notification as filed, with the entity's good-faith posture evidenced by the notification contents and timing.
  ambiguity_notes: |
    The compound `mere act of notification` admits three readings: a filing reading (the act of submitting the notification form), a communication reading (the act of communicating the incident to the recipient authority), or an all-reading (both filing and recipient communication), with the chosen reading being the all-reading because Article 23(1) ¶1 covers both the CSIRT notification and the recipient notification (`recipients of their services where appropriate`). The compound `increased liability` admits two readings: a relative-to-non-notifying-baseline reading or a relative-to-peer-entity reading, with the chosen reading being the relative-to-non-notifying-baseline reading because the shield's structural purpose is to protect the notifying entity from the liability differential that the act of notification would otherwise create. Member State transposition divergence may apply on the specific scope of the shield: some Member States extend the shield to administrative liability (no fine escalation), some to civil liability (no contractual liability to customers), and some to criminal liability (no criminal exposure under national cybersecurity-offence statutes). The shield is not absolute: it does not protect the entity from liability for the underlying incident itself, only from liability for the act of notification. Remain open: (a) whether Member State supervisory authorities will codify a maximum-shield-scope that converts the shield-scope discretion into a conformance baseline (e.g. all three liability types shielded, or only administrative and civil); (b) whether the shield extends to liability under adjacent regulatory regimes (e.g. GDPR Article 33 personal-data-breach notification, DORA Article 19 major ICT-related incident notification), since the shield's literal scope is limited to Article 23 NIS2 notification and does not automatically extend to cross-regulation notification regimes.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

