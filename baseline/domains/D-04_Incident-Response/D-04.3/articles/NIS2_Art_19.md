---
document_id: AEGIS-PREPROC-NIS2-ART-19
title: NIS2 Art. 19 — SecurityObjectives & SecurityRules
regulation: NIS2
article: Art. 19
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
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# NIS2 Art. 19

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

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

