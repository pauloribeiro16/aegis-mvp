---
document_id: AEGIS-PREPROC-GDPR-ART-17
title: GDPR Art. 17 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 17
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
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---

# GDPR Art. 17

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-018 | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds applies; erasure is operationally defined as making the data inaccessible to the controller for normal processing paths. | `GDPR-C06` (Art. 4(12) breach-related — operational deletion overlap); `GDPR-CL03` (Art. 5(1)(c) — data-minimisation, downstream of erasure); `GDPR-CL05` (Art. 5(1)(e) — storage limitation), `GDPR-CP10` (Art. 28(3)(g) — deletion polysemy) | D-05.3 |
| SO-GDPR-018 | D-05.3 | Art. 17, Art. 5(1)(c)/(e) | Erasure without undue delay on Art. 17(1) grounds |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-022
  title: "Downstream-recipient cascade for rectification and erasure"
  source_clauses:
    - { clause_id: GDPR-RT15, article_ref: "Art. 19 — cascade notification" }
    - { clause_id: GDPR-RT12, article_ref: "Art. 16 — rectification" }
    - { clause_id: GDPR-RT11, article_ref: "Art. 15(4) — third-party-rights limit" }
    - { clause_id: GDPR-CL26, article_ref: "Art. 11(2) — identification-exemption (cross)" }
  linked_objectives: [SO-GDPR-012]
  sub_domain: [D-04.3, D-05.3]
  nist_csf_mapping:
    - { id: RS.CO-02, title: "Incidents reported internally to appropriate stakeholders" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 19 requires the controller to communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Art. 16, Art. 17(1) or Art. 18 to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller must inform the data subject about those recipients if the data subject requests it. Art. 16 supplies the rectification mechanism, Art. 15(4) caps the disclosure obligation to recipients known to the controller, and Art. 11(2) preserves the identification precondition for the data-subject rights endpoint. Read together, the provisions establish a downstream-integrity obligation: when the controller corrects, erases, or restricts personal data, the correction must propagate to all known recipients or the controller must demonstrate that propagation is impossible or disproportionate, and the controller must be able to enumerate those recipients on request.
  security_rationale: |
    The obligation in Art. 19, read with Art. 16 and Art. 15(4), to cascade rectifications and erasures to every recipient of the personal data is operationalised in NIST CSF 2.0 through **RS.CO-02 (Incidents reported internally to appropriate stakeholders)** and **PR.DS-12 (Data managed consistent with risk strategy)**.
    PR.DS-12 anchors the data-management foundation that the cascade requires: a recipient register mapping each processing activity to its known recipients, including processors and joint controllers, and a propagation procedure that issues the rectification or erasure event through that register, satisfying the Art. 19 downstream-integrity duty at the policy layer.
    RS.CO-02 captures the reporting dimension that gives the cascade operational force: routing each correction event to the internal stakeholders responsible for recipient notification, documenting the impossible-or-disproportionate justifications where propagation fails, and retaining the evidence needed to answer a data-subject recipient-list request under Art. 19.
    The two subcategories together operationalise the propagation chain that prevents the rectification right from becoming illusory across a distributed processing ecosystem.
    A controller documenting PR.DS-12 recipient register, RS.CO-02 propagation logs and the per-event justification evidence can demonstrate ex post, under Art. 5(2), that corrections reached every known recipient or that the documented exception genuinely applied.
  ambiguity_notes: |
    `impossible` OR `disproportionate effort` (Art. 19) carries COORD-S3. Reading chosen: either escape clause suffices, as a logical inclusive OR. An alternative reading requiring both to hold is rejected: the stricter reading would impose undue compliance burden without policy justification. The OJ text uses `or`, the English-language UN-style drafting convention for an inclusive disjunction; EDPB Guidelines treat this consistently. On the Art. 15(4) cap (third-party-rights limit), the disclosure to the data subject about recipients is bounded to recipients known to the controller; the controller is not required to investigate recipients beyond its own records. Remain open: (a) whether the `recipient` definition includes processors (under Art. 28) and joint controllers (under Art. 26) or only independent third-party controllers, pending EDPB Guidelines 5/2019 revision; and (b) how the recipient-list request interacts with confidentiality obligations (e.g. trade-secret-protected recipients), pending alignment with Charter Art. 7 and CJEU jurisprudence on commercial confidentiality.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-030
  title: "Right-to-erasure with cryptographic key-destruction deletion path"
  source_clauses:
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
    - { clause_id: GDPR-CP10, article_ref: "Art. 28(3)(g) — delete polysemy" }
  linked_objectives: [SO-GDPR-018, SO-GDPR-019]
  sub_domain: [D-05.3]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [TRIGGERED]
  regulatory_rationale: |
    Art. 17 grants the data subject the right to erasure (the right to be
    forgotten) where the conditions listed in Art. 17(1)(a)–(f) apply; the
    corresponding controller-side duties flow from Art. 5(1)(c) data
    minimisation and Art. 5(1)(e) storage limitation, which together
    require erasure once the purpose no longer applies. Art. 28(3)(g)
    imposes a processor-side mirror obligation: at the choice of the
    controller, the processor must delete or return all the personal data
    after the end of the provision of services relating to processing,
    and must delete existing copies unless Union or Member State law
    requires storage. The three provisions operate jointly: Art. 17
    supplies the data-subject trigger, Art. 5(1)(c)/(e) supply the
    controller principle, and Art. 28(3)(g) supplies the processor
    instrument.
  security_rationale: |
    The obligation in Art. 17, Art. 5(1)(c), Art. 5(1)(e) and Art. 28(3)(g) to render personal data unattainable once the data subject's erasure conditions are met or the storage purpose has run its course is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)**.
    PR.DS-10 captures the runtime-protection layer that erasure must extend through: protection against residual exposure during query and join operations is the prerequisite for a defensible cryptographic-erasure posture, because if the in-use protections fail the controller cannot claim the additional information held under separate technical and organisational control was effective.
    PR.DS-12 captures the lifecycle-management layer: a documented deletion procedure keyed to the Art. 17 trigger conditions and the Art. 5(1)(e) purpose-end moment, with cryptographic key destruction as the operational realisation of `deletes` for any system where per-copy destruction is not feasible across backups and replicas.
    A controller that documents PR.DS-10 in-use key-custody discipline and PR.DS-12 deletion-procedure coverage, including key-destruction for backups, can demonstrate ex post, against the Art. 5(2) accountability duty, that the Art. 17 trigger conditions and Art. 28(3)(g) processor-side mirror were honoured at the cryptographic layer on the day of any supervisory inspection.
  ambiguity_notes: |
    `deletes` in Art. 28(3)(g) carries Berry-flagged POLY-S3 (Berry
    §3.3.1) with three operational senses — physical destruction of the
    storage medium, logical deletion (recoverable through file-system or
    forensic tools), and cryptographic erasure (destruction of the
    cryptographic key rendering the underlying data unintelligible). The
    reading adopted for this SR is the cryptographic-erasure reading:
    key destruction, with the key held outside the data substrate, is the
    most defensible interpretation because it scales across backups and
    replicas without per-copy destruction and aligns with EDPB Guidelines
    5/2020 on storage limitation. Two alternative readings remain. First,
    the strict physical-destruction reading would require shredding of
    every storage medium that ever held the data; this conflicts with
    modern cloud-architecture realities where data is replicated across
    many media. Second, the logical-deletion reading would accept
    file-system-level deletion as sufficient; this conflicts with EDPB
    guidance because forensic recovery remains feasible. Remain open:
    (a) whether cryptographic erasure satisfies Art. 17(1) where the
    controller still holds the encryption key (likely not); (b) whether
    backup tapes with deleted-file markers are erased under Art. 28(3)(g)
    when full tape overwrite has not occurred.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

