---
document_id: AEGIS-PREPROC-GDPR-ART-33
title: GDPR Art. 33 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 33
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.4.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# GDPR Art. 33

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-008 | Personal data breaches are detected and triaged; the moment of "becoming aware" is documented to anchor the 72-hour notification clock. | `GDPR-CP17` (Art. 33(1)); `GDPR-C06` (Art. 4(12) — breach definition) | D-04.1 |
| SO-GDPR-008 | D-04.1, D-10.1 | Art. 4(12), Art. 33(1) | Breach detection and "becoming aware" anchoring |
| SO-GDPR-009 | Personal data breaches are contained and mitigated through appropriate technical and organisational measures (including, where applicable, measures rendering the data unintelligible to unauthorised parties, and subsequent measures that ensure the high risk no longer materialises). | `GDPR-CP18` (Art. 33(3)(d)); `GDPR-CP20` (Art. 34(3)(a)/(b)) | D-04.2 |
| SO-GDPR-009 | D-04.2 | Art. 33(3)(d), Art. 34(3)(a)/(b) | Containment and mitigation of breaches |
| SO-GDPR-010 | Personal data breaches are notified to the supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware, unless the breach is unlikely to result in a risk to data subjects' rights and freedoms. | `GDPR-CP17` (Art. 33(1)); `GDPR-C06` (Art. 4(12)) | D-04.3 |
| SO-GDPR-010 | D-04.3 | Art. 33(1), Art. 4(12) | 72h notification to supervisory authority |
| SO-GDPR-011 | Personal data breaches likely to result in a high risk to data subjects are communicated to the affected data subjects without undue delay, in clear and plain language, unless one of the three Art. 34(3) exceptions applies. | `GDPR-CP19` (Art. 34(1)/(2)/(3)); `GDPR-CP18` (Art. 33(3)(b)/(c)/(d)) | D-04.3 |
| SO-GDPR-030 | Personal-data processing systems and services are monitored for adverse events covering the five Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), with a clear definition of the moment of "becoming aware of" a breach to anchor the Art. 33(1) notification clock. | `GDPR-CP16` (Art. 32(2)); `GDPR-CP17` (Art. 33(1) — `becoming aware`); `GDPR-CP15` (Art. 32(1)(b)) | D-10.1, D-04.1 |
| SO-GDPR-030 | D-10.1, D-04.1 | Art. 32(2), Art. 33(1), Art. 32(1)(b) | Monitoring the five Art. 32(2) risk types |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-014
  title: "Continuous breach detection enabling the 72-hour clock"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — 72-hour notification trigger" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b) — confidentiality of processing systems" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach definition" }
  linked_objectives: [SO-GDPR-008]
  sub_domain: [D-04.1, D-10.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks monitored for potentially adverse events" }
    - { id: DE.CM-09, title: "Computing hardware/software/runtime/data monitored" }
    - { id: RS.MA-02, title: "Incident reports triaged and validated" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services, which is achieved only if monitoring is in place to detect personal data breaches (Art. 4(12) defines a personal data breach as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed). Art. 33(1) creates the 72-hour clock from the moment of becoming aware; awareness requires detection capability. Read together, the provisions establish that continuous security monitoring is the regulatory foundation for the entire incident-response chain: no detection, no awareness, no notification, and no compliance with the 72-hour clock. The obligation is continuous because the threat surface is continuous; the obligation is on the controller and processor, jointly, because detection is layered.
  security_rationale: |
    The obligation in Art. 32(1)(b), read with Art. 33(1) and Art. 4(12), to detect personal data breaches and so start the 72-hour awareness clock is operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks monitored for potentially adverse events)**, **DE.CM-09 (Computing hardware, software, runtime and data monitored)** and **RS.MA-02 (Incident reports triaged and validated)**.
    DE.CM-01 anchors the network-layer monitoring that surfaces unauthorised disclosure and exfiltration, the most frequent breach vectors in published incident data, satisfying the Art. 4(12) disclosure and access events at the transport layer.
    DE.CM-09 captures the host-and-data monitoring that detects the remaining Art. 4(12) events — alteration via integrity monitoring, destruction and loss via availability monitoring — across the runtime environments where personal data actually resides.
    RS.MA-02 closes the chain by triaging and validating detected events into declared incidents, supplying the documented awareness moment that Art. 33(1) requires for the clock to start.
    A controller documenting DE.CM-01 and DE.CM-09 coverage tuned to the five Art. 4(12) events and RS.MA-02 triage records can demonstrate ex post, under Art. 5(2), that the 72-hour clock was started from a genuine, auditable detection event rather than from informal awareness.
  ambiguity_notes: |
    `becoming aware` (Art. 33(1)) carries POLY-S3. Reading chosen: documented awareness by a controller employee with delegated breach-handling responsibility, the moment the breach is captured by the controller's detection capability. An alternative reading that awareness attaches whenever any employee becomes aware, including informally, is rejected because it would force an unreasonably early clock and is inconsistent with how organisations actually triage. A third reading that awareness occurs only when senior management is formally briefed is too late and creates compliance risk. The chosen reading is consistent with EDPB Guidelines 9/2022 §3.4 and aligns with the controller's documented incident-response procedure. Operationally, controllers designate a breach-handling role, document the awareness moment, and timestamp detection events to support the 72-hour clock calculation. Remain open: (a) whether AI-driven anomaly detection that flags a breach but does not escalate within the controller's documented procedure still constitutes "awareness", pending EDPB guidance on automated detection; and (b) how the awareness moment is established when the breach is detected by a sub-processor rather than the controller, pending alignment with Art. 33(2) processor notification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-015
  title: "Post-breach containment, mitigation, and remediation runbooks"
  source_clauses:
    - { clause_id: GDPR-CP18, article_ref: "Art. 33(3)(d) — measures taken or proposed" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a)/(b) — measures to render data unintelligible / subsequent measures" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(d) — testing" }
  linked_objectives: [SO-GDPR-009]
  sub_domain: [D-04.2]
  nist_csf_mapping:
    - { id: RS.MI-01, title: "Incidents contained" }
    - { id: RS.MI-02, title: "Incidents mitigated" }
    - { id: PR.DS-01, title: "Data-at-rest protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 34(3)(a) and (b) provide that subsequent measures rendering the personal data unintelligible or eliminating the high risk are valid exceptions to the data-subject notification under Art. 34(1). Art. 32(1)(d) reinforces the testing and evaluating discipline. Read together, the provisions operationalise defence-in-depth after a breach: short-term containment, mid-term mitigation, and long-term remediation, with the reporting obligation under Art. 33(3)(d) covering both taken and proposed measures, and the Art. 34(3) exceptions providing notification carve-outs where mitigation is sufficient.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects]
  security_rationale: |
    The obligation in Art. 33(3)(d), read with Art. 34(3)(a)/(b) and Art. 32(1)(d), to contain, mitigate and remediate a personal data breach is operationalised in NIST CSF 2.0 through **RS.MI-01 (Incidents contained)**, **RS.MI-02 (Incidents mitigated)** and **PR.DS-01 (Data-at-rest protected)**.
    RS.MI-01 anchors the short-term containment runbook — isolating affected systems, revoking credentials, blocking exfiltration paths — that Art. 33(3)(d) requires the controller to report as measures taken, satisfying the operational halt of active harm.
    RS.MI-02 captures the mid-term mitigation that Art. 34(3)(b) presupposes: re-encrypting data under new keys, resetting affected credentials, patching the exploited vulnerability, and demonstrating that the high risk is no longer likely to materialise.
    PR.DS-01 supplies the cryptographic foundation that makes both containment and mitigation auditable, by ensuring that the post-breach state of the affected dataset is itself protected against re-compromise.
    A controller documenting RS.MI-01 containment actions, RS.MI-02 mitigation evidence and PR.DS-01 post-remediation key state can demonstrate ex post, under Art. 5(2), that the Art. 33(3)(d) measures were actually taken and that any Art. 34(3) carve-out was genuinely earned.
  ambiguity_notes: |
    Art. 34(3)(a) carries VAG-S3 on `unintelligible` (see SR-GDPR-004 for chosen reading). All readings converge on the operational containment and mitigation obligation. The `where appropriate` hedge in Art. 33(3)(d) is read as the controller's reasonable judgement on whether mitigation measures exist and are material; it is not a discretion to omit the field. Art. 34(3)(b) `subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise` is the harder threshold: the controller must demonstrate that mitigation actually neutralises the high risk, not merely that mitigation was attempted. Remain open: (a) whether the controller's notification to the supervisory authority under Art. 33(3)(d) must include proposed measures when containment is still in progress, or only taken measures with a separate proposed-measures addendum, pending EDPB guidance; and (b) how the mitigation obligation applies to breaches that originate at a sub-processor, pending alignment with Art. 33(2) processor notification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-016
  title: "72-hour breach notification to the supervisory authority"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — 72-hour notification" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
    - { clause_id: GDPR-C09, article_ref: "Art. 4(22) — supervisory authority concerned" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: RS.CO-04, title: "Coordination with stakeholders consistent with applicable rules" }
    - { id: RS.MA-03, title: "Incidents categorized, prioritized, and scoped" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons. Art. 4(12) defines the trigger event (personal data breach), Art. 32(2) anchors the five-event risk enumeration underlying the risk assessment, and Art. 4(22) anchors which supervisory authority is "competent" (the lead authority under Art. 56 one-stop-shop, or the local authority where the controller's main establishment is located). Read together, the provisions establish a twin temporal anchor (without undue delay + 72 hours) with a risk-based carve-out, directed to the competent supervisory authority. Where the notification is made after the 72-hour window, Art. 33(1) requires reasons for the delay.
  security_rationale: |
    The obligation in Art. 33(1), read with Art. 4(12), Art. 32(2) and Art. 4(22), to notify the competent supervisory authority within 72 hours of awareness is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)**, **RS.CO-04 (Coordination with stakeholders consistent with applicable rules)** and **RS.MA-03 (Incidents categorized, prioritized, and scoped)**.
    RS.MA-03 anchors the triage that establishes whether the Art. 4(12) breach definition is met and whether the risk threshold engages the notification duty, supplying the categorised and scoped incident record that the 72-hour clock depends on.
    RS.CO-02 captures the internal escalation to executive leadership and legal counsel that precedes the external notification, ensuring the controller's decision chain is documented and defensible.
    RS.CO-04 closes the loop with the coordination to the competent supervisory authority under Art. 55, consistent with the applicable rules and the Art. 4(22) one-stop-shop determination.
    A controller documenting RS.MA-03 triage, RS.CO-02 escalation and RS.CO-04 authority coordination can demonstrate ex post, under Art. 5(2), that the notification was timely, addressed to the correct authority, and supported by reason-for-delay evidence where the window was exceeded.
  ambiguity_notes: |
    `without undue delay and, where feasible, not later than 72 hours` carries S3 VAG+SCOPE on the double temporal anchor. Reading chosen: 72 hours is the hard ceiling; `without undue delay` requires action immediately upon awareness; `where feasible` is a narrow, technical-feasibility exception (e.g. forensic preservation in progress, key personnel unavailable through the night). The threshold `unlikely to result in a risk` is interpreted via EDPB Guidelines 9/2022 as the precautionary principle: notification is required unless the controller can demonstrate that the breach is unlikely to result in a risk, and the demonstration burden rests with the controller. An alternative reading that controller judgement suffices with no demonstration required is rejected because it inverts the burden and is inconsistent with EDPB practice. Remain open: (a) whether the 72-hour clock resets on material new information about the same breach, or runs continuously from initial awareness, pending EDPB clarification; and (b) how the `where feasible` exception applies when the controller is in a multi-jurisdictional incident with different working hours, pending alignment with NIS 2 incident-handling timelines.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-017
  title: "Processor-to-controller breach notification without undue delay"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(2) — processor-to-controller notification" }
    - { clause_id: GDPR-C06, article_ref: "Art. 4(12) — personal data breach" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3, D-06.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: RS.MA-02, title: "Incident reports triaged and validated" }
  applies_to_role: [PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(2) requires the processor to notify the controller without undue delay after becoming aware of a personal data breach. Art. 4(12) defines the trigger event. Read together, the two provisions establish the upstream trigger for the controller's Art. 33(1) 72-hour clock: the processor's awareness moment starts the chain that culminates in the controller's notification to the supervisory authority. The processor's `without undue delay` obligation is not the same as the controller's 72-hour clock; the processor must notify the controller as soon as it becomes aware, and the controller then has its own 72-hour window from receipt of the processor's notification (or from independent awareness) to notify the supervisory authority.
  security_rationale: |
    The obligation in Art. 33(2), read with Art. 4(12), for the processor to notify the controller without undue delay after becoming aware of a personal data breach is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)** and **RS.MA-02 (Incident reports triaged and validated)**.
    RS.MA-02 anchors the triage that the processor performs on detecting a breach, supplying the validated incident report that Art. 33(2) requires and establishing the awareness moment that starts the upstream chain toward the controller's own Art. 33(1) 72-hour clock.
    RS.CO-02 captures the reporting channel itself: the notification path from processor to controller, typically contractually defined under Art. 28(3)(f), through which the triaged report is escalated within the same operational shift rather than held for a deferred batch.
    The two subcategories together operationalise the processor-side leg of the breach-notification chain, recognising that processors, owning the infrastructure layer, frequently detect breaches first.
    A controller documenting, against its Art. 28(3) processor contracts, RS.MA-02 triage evidence and RS.CO-02 notification timestamps from each processor can demonstrate ex post, under Art. 5(2), that the processor-to-controller link operated without undue delay and that its own 72-hour clock was started from a genuine upstream report.
  ambiguity_notes: |
    `without undue delay` inherits S3 VAG ambiguity (Berry §5.1). Reading chosen: action on the same operational shift or business day, with hard escalation channels documented in the Art. 28(3) processor contract. An alternative reading fixing the window at 24 hours is acceptable but operationally narrower. A third reading extending the window to 72 hours (mirroring the controller's clock) is rejected because it would compress the controller's own window to zero in practice. The chosen reading aligns with EDPB Guidelines 9/2022 §3.4 and ISO 27001 A.16.1.2 reporting expectations. Remain open: whether AI-driven detection by the processor that flags a probable breach without confirmation triggers the `without undue delay` clock, or whether confirmation is required, pending EDPB guidance on probabilistic detection.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-018
  title: "Structured four-element breach notification content"
  source_clauses:
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(3)(a)/(b)/(c)/(d) — notification content" }
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — overall 72h envelope" }
  linked_objectives: [SO-GDPR-010]
  sub_domain: [D-04.3, D-09.4]
  nist_csf_mapping:
    - { id: RS.AN-03, title: "Analysis performed to determine what occurred and root cause" }
    - { id: RS.AN-07, title: "Incident data and metadata collected with integrity preserved" }
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 33(3) requires the controller's breach notification to the supervisory authority to describe at minimum: (a) the nature of the personal data breach including, where possible, the categories and approximate number of data subjects concerned and the categories and approximate number of personal data records concerned; (b) the name and contact details of the data protection officer or other contact point where more information can be obtained; (c) the likely consequences of the personal data breach; (d) the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 33(1) provides the overall 72-hour envelope. Read together, the provisions establish a four-element content requirement with the recognition that initial notification operates under uncertainty; the controller supplements as investigation proceeds.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — describe the nature of the personal data breach including where possible, the categories and approximate number of data subjects concerned and the categories and approximate number of personal data records concerned]
  security_rationale: |
    The obligation in Art. 33(3), read with the Art. 33(1) 72-hour envelope, to deliver a four-element breach notification (nature, contact, consequences, measures) is operationalised in NIST CSF 2.0 through **RS.AN-03 (Analysis performed to determine what occurred and root cause)**, **RS.AN-07 (Incident data and metadata collected with integrity preserved)** and **RS.CO-02 (Incidents reported internally to appropriate stakeholders)**.
    RS.AN-03 anchors the root-cause analysis that produces the Art. 33(3)(a) nature description and the Art. 33(3)(c) likely-consequences assessment, satisfying the content requirement even where the investigation is still incomplete at the 72-hour mark.
    RS.AN-07 captures the evidence-integrity discipline — chain of custody, provenance preservation, metadata collection — that makes the notification defensible under supervisory scrutiny and supports the phased-disclosure model under Art. 33(4).
    RS.CO-02 closes the loop by routing the structured content to the internal stakeholders who approve and dispatch the notification.
    A controller documenting RS.AN-03 analysis records, RS.AN-07 evidence-preservation logs and RS.CO-02 internal-approval trail can demonstrate ex post, under Art. 5(2), that the notification content met the Art. 33(3) standard and that subsequent supplements were grounded in preserved, integrity-checked evidence.
  ambiguity_notes: |
    `where possible`, `approximate number`, `likely consequences` are acknowledged VAG-S2. Reading chosen: best-effort reporting at the time of notification, with subsequent updates as investigation proceeds. The Art. 33(4) phased-disclosure mechanism supports this: the controller can provide initial incomplete information and supplement as it becomes available, provided the reasons for incompleteness are documented. An alternative reading requiring precise reporting at 72 hours is rejected: the OJ text explicitly softens with `where possible` and `approximate`. Remain open: (a) whether the phased-disclosure model applies to each Art. 33(3) element independently or only to elements (a), (c), and (d), pending EDPB Guidelines 9/2022 revision; and (b) how the controller documents the boundary between initial notification and supplemental disclosure in audit defensible form, pending alignment with ISO 27035 incident-management practice.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-019
  title: "High-risk breach communication to affected data subjects"
  source_clauses:
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk breach communication to data subject" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(2) — content of communication" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration (cross)" }
  linked_objectives: [SO-GDPR-011]
  sub_domain: [D-04.3]
  nist_csf_mapping:
    - { id: RS.CO-03, title: "Information shared with designated stakeholders per information-sharing rules" }
    - { id: RS.CO-04, title: "Coordination with stakeholders consistent with applicable rules" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(1) requires the controller to communicate a personal data breach to the data subject without undue delay when the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons. Art. 34(2) requires the communication to describe in clear and plain language the nature of the personal data breach and contain at least the information and measures referred to in points (b), (c) and (d) of Art. 33(3). Art. 32(2) anchors the risk-enumeration vocabulary (destruction, loss, alteration, unauthorised disclosure of, or access to) underlying the high-risk assessment. Read together, the provisions establish a higher threshold (high risk to data subjects' rights) than the supervisory-authority notification (Art. 33, risk to data subjects' rights), and a content requirement scoped to the data subject rather than the supervisory authority.
  security_rationale: |
    The obligation in Art. 34(1), read with Art. 34(2) and Art. 32(2), to communicate a high-risk breach to affected data subjects in clear and plain language is operationalised in NIST CSF 2.0 through **RS.CO-03 (Information shared with designated stakeholders per information-sharing rules)** and **RS.CO-04 (Coordination with stakeholders consistent with applicable rules)**.
    RS.CO-03 anchors the information-sharing mechanism that delivers the Art. 34(2) content — nature of the breach, likely consequences, measures taken — to the data subjects whom the rules designate as the entitled stakeholders, satisfying the higher Art. 34 threshold that sits above the Art. 33 supervisory-notification trigger.
    RS.CO-04 captures the coordination discipline that multi-channel notification (direct communication, prominent website notice and, where appropriate, public communication) requires, ensuring the communication achieves equally effective reach and that the high-risk classification decision tree is documented.
    The two subcategories together operationalise the data-subject-facing leg of breach response, distinct from the authority-facing leg, enabling individual protective action such as account rotation and fraud-alert subscription.
    A controller documenting RS.CO-03 notification records, RS.CO-04 channel-choice evidence and the high-risk assessment per EDPB Guidelines 9/2022 can demonstrate ex post, under Art. 5(2), that affected data subjects received timely, intelligible notice enabling protective action.
  ambiguity_notes: |
    `likely to result in a high risk` carries POLY+VAG-S3 (the three-tier `risk`/`high risk`/`high risk` architecture across Arts. 33, 34, 35). Reading chosen: the Art. 34 threshold is higher than the Art. 33 threshold — objectively elevated above ordinary processing risk, per EDPB Guidelines 9/2022. An alternative reading treating the threshold as severe impact on data subject's rights, per CNIL guidance, is operationally similar but framing-different. The chosen reading treats the threshold as risk-of-significant-harm, not merely risk-of-any-harm; the controller documents the risk assessment with reference to the data categories (Art. 9 special categories raise the threshold), the data-subject population (vulnerable populations raise the threshold), and the breach characteristics (encrypted vs plaintext, contained vs ongoing). Remain open: (a) whether `clear and plain language` requires a CEFR B1 reading-age standard or whether national DPA guidance is acceptable, pending EDPB harmonisation; and (b) whether the Art. 34 communication can be combined with Art. 33 notification to the supervisory authority, or must be a separate communication, pending EDPB Guidelines 9/2022 clarification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-020
  title: "Cryptographic and mitigation carve-outs for data-subject notification"
  source_clauses:
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(a) — encryption/unintelligibility exception" }
    - { clause_id: GDPR-CP20, article_ref: "Art. 34(3)(b) — subsequent-measures exception" }
    - { clause_id: GDPR-CP19, article_ref: "Art. 34(1) — high-risk trigger" }
  linked_objectives: [SO-GDPR-011, SO-GDPR-002]
  sub_domain: [D-04.3, D-01.3]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.IR-03, title: "Mechanisms to achieve resilience in normal and adverse situations" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 34(3)(a) provides that the data-subject notification under Art. 34(1) is not required if the controller has implemented appropriate technical and organisational protection measures, and those measures were applied to the personal data affected by the personal data breach, in particular those that render the personal data unintelligible to any person who is not authorised to access it, such as encryption. Art. 34(3)(b) provides a parallel exception if the controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise. Art. 34(1) supplies the high-risk trigger that the exceptions modify. Read together, the provisions establish two paths to eliminate the data-subject notification duty despite a high-risk breach: cryptographic protection at the time of breach, or subsequent mitigation that neutralises the high risk.
    [OJ-corrective note (v0.2 audit): the OJ text reads verbatim — the controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialise]
  security_rationale: |
    The obligation in Art. 34(3)(a) and (b), read with the Art. 34(1) high-risk trigger, to eliminate the data-subject notification duty through cryptographic protection or subsequent mitigation is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.IR-03 (Resilience requirements in normal and adverse situations)**.
    PR.DS-01 anchors the Art. 34(3)(a) cryptographic carve-out: the encryption, applied to the data actually affected by the breach, that renders the personal data unintelligible to any unauthorised person, with the key separation that makes the carve-out auditable rather than merely asserted.
    PR.IR-03 captures the Art. 34(3)(b) subsequent-measures path: the resilience mechanisms — key rotation, credential reset, vulnerability patch, compensating controls — that together ensure the high risk is no longer likely to materialise, satisfying the higher threshold that demands demonstrated risk neutralisation rather than mere mitigation effort.
    The two subcategories together operationalise the two distinct paths the regulation offers for eliminating the notification duty despite a high-risk breach.
    A controller documenting PR.DS-01 key-state evidence on the affected dataset and PR.IR-03 mitigation-effect demonstration can demonstrate ex post, under Art. 5(2), which carve-out applied and that its conditions were genuinely met on the day of the breach.
  ambiguity_notes: |
    Both exceptions carry VAG-S3 (see SR-GDPR-004 for `unintelligible` reading chosen). The `no longer likely to materialise` wording in Art. 34(3)(b) is read as a high threshold: the controller must demonstrate that the mitigation has materially reduced the risk below the Art. 34(1) threshold, not merely that mitigation was attempted. The Art. 34(3)(a) operational condition `those measures were applied to the personal data affected by the personal data breach` requires the controller to demonstrate that the encryption protected the actual affected dataset, not merely that encryption was deployed on the dataset generally. Rule preserves the cryptographic-reading exception. Remain open: (a) whether rotation of cryptographic keys after the breach (treating the old keys as compromised) satisfies the Art. 34(3)(a) carve-out when the controller retains access to old keys for legitimate purposes, pending EDPB clarification; and (b) how the Art. 34(3)(b) `subsequent measures` carve-out interacts with the Art. 33 supervisory-authority notification (which is not carved out), pending alignment with EDPB Guidelines 9/2022.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-049
  title: "Five-event threat model with monitoring and event analysis"
  source_clauses:
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
    - { clause_id: GDPR-CP17, article_ref: "Art. 33(1) — breach awareness (cross)" }
  linked_objectives: [SO-GDPR-030]
  sub_domain: [D-10.1, D-04.1]
  nist_csf_mapping:
    - { id: DE.CM-01, title: "Networks and network services are monitored to find potentially adverse events" }
    - { id: DE.CM-03, title: "Personnel activity and technology usage are monitored to find potentially adverse events" }
    - { id: DE.AE-02, title: "Detected events are analyzed to understand attack targets and methods" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(2) requires that, in assessing the appropriate level of
    security, account shall be taken in particular of the risks that are
    presented by processing, in particular from accidental or unlawful
    destruction, loss, alteration, unauthorised disclosure of, or
    access to, personal data transmitted, stored or otherwise
    processed. Art. 33(1) cross-references back through the breach-
    awareness trigger. The five-event risk enumeration — accidental or
    unlawful destruction, loss, alteration, unauthorised disclosure
    and unauthorised access — anchors the controller's and processor's
    threat-modelling scope.
  security_rationale: |
    The obligation in Art. 32(2), read with Art. 33(1), to take into account in the appropriate-level-of-security assessment the five enumerated risks (accidental or unlawful destruction, loss, alteration, unauthorised disclosure, and unauthorised access) and to anchor the breach-awareness trigger on those risks, is operationalised in NIST CSF 2.0 through **DE.CM-01 (Networks and network services are monitored to find potentially adverse events)**, **DE.CM-03 (Personnel activity and technology usage are monitored to find potentially adverse events)** and **DE.AE-02 (Detected events are analyzed to understand attack targets and methods)**.
    DE.CM-01 captures the network-layer monitoring that addresses the `transmitted` events of the Art. 32(2) list, particularly unauthorised disclosure and unauthorised access along the transport surface, with adverse-event detection tuned to the five-event enumerator.
    DE.CM-03 captures the personnel-activity and technology-usage monitoring that addresses the `otherwise processed` events of the Art. 32(2) list, including alteration and unauthorised access from inside the trust boundary.
    DE.AE-02 captures the analysis layer that converts raw monitoring output into breach-relevant signal: events across all five Art. 32(2) categories must be analysed to understand attack targets and methods so that the Art. 33(1) breach-awareness trigger fires only when it should and with the right context.
    A controller or processor that documents DE.CM-01 network monitoring, DE.CM-03 personnel-and-technology monitoring and DE.AE-02 event analysis against the five-event enumeration can demonstrate ex post, against the Art. 5(2) accountability duty, that the threat-modelling scope from Art. 32(2) was operationally covered on the day of any incident or supervisory inspection.
  ambiguity_notes: |
    The 5-way OR is Berry-flagged COORD-S3 (Berry §5.4.7 menu-card
    pattern): each OR is inclusive, and the OR-chain admits at least
    five distinct threat-model scopes. The reading adopted for this SR
    is the strict inclusive reading: any of the five events triggers
    the security-assessment and monitoring obligation, and the OR is
    inclusive rather than illustrative. Two alternative readings
    remain. First, an illustrative-list reading under which the
    controller determines the in-scope events would weaken the threat-
    modelling baseline and allow cherry-picking. Second, a destruction-
    only reading that limits scope to `destruction` would conflict with
    the OJ text, which lists five distinct events. Remain open: (a)
    whether `loss` requires proof of exfiltration or covers any data-set
    unavailability event including accidental loss; (b) whether
    `unauthorised access` includes authorised-but-internal misuse, where
    the CJEU language suggests yes but the operational detection scope
    is debated.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

