---
document_id: AEGIS-PREPROC-GDPR-ART-52
title: GDPR Art. 52 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 52
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
status: DRAFT
---

# GDPR Art. 52

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-010
  title: "Minimised collection of identity verification data"
  source_clauses:
    - { clause_id: GDPR-RT04, article_ref: "Art. 12(6)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-005]
  sub_domain: [D-03.1, D-05.1]
  nist_csf_mapping:
    - { id: PR.AA-02, title: "Identities proofed and bound to credentials" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 12(6) imposes identity-verification scope limitation through the general GDPR principle of data minimisation (Art. 5(1)(c)). The controller must request only the additional information necessary to confirm identity, not arbitrary identity documents. Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. The verification purpose is to confirm identity, so the data-minimisation test is calibrated to the identity-confirmation purpose: collect only what is necessary to confirm identity, not what would be ideal in a hypothetical stronger verification. The Art. 5(2) accountability burden shifts the demonstration duty to the controller: the controller must be able to justify the chosen verification scope.
  security_rationale: |
    The obligation in Art. 12(6), read with the Art. 5(1)(c) data-minimisation principle, to collect only the identity-verification information necessary to confirm the data subject is operationalised in NIST CSF 2.0 through **PR.AA-02 (Identities proofed and bound to credentials)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.AA-02 anchors the context-bound identity proofing that limits credential collection to what the interaction risk actually warrants, satisfying the Art. 5(1)(c) necessity test at the rights-request endpoint and preventing the verification step from accumulating identity documents that would enlarge the breach blast-radius.
    PR.DS-12 captures the policy-level data-management discipline that bounds the retention and scope of any verification artefact collected: a documented risk strategy governing how long verification data is held, who can access it, and when it is purged.
    The two subcategories together operationalise the graduated verification standard — low-risk requests with no additional collection, high-risk with bounded retention — that Art. 5(1)(c) imposes on Art. 12(6).
    A controller documenting PR.AA-02 proofing decisions, PR.DS-12 retention limits and the necessity justification per verification scope can demonstrate ex post, under the Art. 5(2) accountability burden, that identity-verification data collection was proportionate and minimised rather than opportunistically over-collected.
  ambiguity_notes: |
    `necessary` inherits VAG-S3 ambiguity from Art. 5(1)(c). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. The rule preserves the proportionate-necessary interpretation. An alternative reading treats necessity as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring the least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs (notably the CNIL) for sensitive-data contexts. The Art. 5(1)(c) necessary threshold varies with data sensitivity and breach impact; for Art. 9 special-category data, the controller may need stronger verification than for ordinary personal data. Remain open: whether automated identity-verification services (e.g. Jumio, Onfido) are themselves in scope as joint controllers under Art. 26, pending CJEU and EDPB guidance on AI-driven verification.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-025
  title: "Purpose-bound data minimisation with compatibility assessment"
  source_clauses:
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation" }
    - { clause_id: GDPR-CL14, article_ref: "Art. 6(4) — compatibility test" }
    - { clause_id: GDPR-CL02, article_ref: "Art. 5(1)(b) — purpose limitation (cross)" }
  linked_objectives: [SO-GDPR-015]
  sub_domain: [D-05.1]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: ID.AM-03, title: "Inventories of data and metadata for designated data types" }
  applies_to_role: [CONTROLLER]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed. Art. 6(4) provides the compatibility test for further processing beyond the original purposes, requiring the controller to take into account, inter alia, (a) any link between the purposes, (b) the context of collection, (c) the nature of the personal data (especially special categories), (d) the possible consequences for data subjects, and (e) the existence of appropriate safeguards. Art. 5(1)(b) purpose limitation supplies the upstream anchor. Read together, the three provisions establish that data minimisation is calibrated to the purpose, that any change of purpose triggers a compatibility assessment, and that the purpose itself is bound by specification, explicitness, and legitimacy.
  security_rationale: |
    The obligation in Art. 5(1)(c), read with the Art. 6(4) compatibility test and Art. 5(1)(b) purpose limitation, to keep personal data adequate, relevant and limited to what is necessary is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data managed consistent with risk strategy)** and **ID.AM-03 (Inventories of data and metadata for designated data types)**.
    ID.AM-03 anchors the data-inventory foundation that minimisation requires: knowing what data is held, for which declared purpose, and with which metadata, supplying the asset record without which the Art. 5(1)(c) necessity test cannot be applied and the Art. 6(4) compatibility assessment cannot be run on a change of purpose.
    PR.DS-12 captures the policy-level data-management strategy that the inventory enables: per-purpose collection limits, retention schedules that delete at purpose-end, and the documented compatibility assessment for any further processing, satisfying the proportionality-to-purpose standard.
    The two subcategories together operationalise minimisation as both a knowledge property (what is held) and a discipline (how it is bounded), reducing attack surface and breach impact as security side-effects.
    A controller documenting ID.AM-03 data inventory and PR.DS-12 retention-and-compatibility decisions can demonstrate ex post, under Art. 5(2), that each dataset was necessary for its purpose and that any purpose-change survived the Art. 6(4) test.
  ambiguity_notes: |
    `adequate, relevant, and limited to what is necessary` carries VAG-S3 (three conjunctive vague adjectives). Reading chosen: proportionate to purpose, demonstrable ex ante via Art. 5(2) accountability and Art. 35 DPIA necessity assessment. An alternative reading treats adequacy as satisfied when serving the designed purpose, with necessity presumed by default; this is rejected because it inverts the accountability burden. A third reading requiring least-intrusive among equivalent means under Charter Art. 52(1) is the most restrictive position and is the one adopted by some national DPAs for sensitive-data contexts. The Art. 6(4) compatibility test is the procedural mechanism for any change of purpose; the five factors are conjunctive in the sense that all must be considered, but the test is qualitative and the controller exercises judgement. Remain open: (a) whether machine-learning model training purposes are compatible with the original collection purpose under Art. 6(4), or require fresh consent, pending EDPB AI Act interaction guidance and CJEU jurisprudence on inferred-data compatibility; and (b) whether the data-minimisation threshold differs for secondary processing for fraud-prevention or IT-security purposes under Art. 6(1)(f), pending alignment with the legitimate-interests balancing test.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

