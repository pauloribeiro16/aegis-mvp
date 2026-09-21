---
document_id: AEGIS-PREPROC-GDPR-ART-55
title: GDPR Art. 55 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 55
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

# GDPR Art. 55

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

