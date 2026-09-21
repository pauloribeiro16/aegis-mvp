---
document_id: AEGIS-PREPROC-GDPR-ART-28
title: GDPR Art. 28 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 28
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md
  - ../../CrossRegulation/DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DomainAnalysis/D-10_Monitoring-Audit/D-10.1.md
  - ../../CrossRegulation/DeepAnalysis/D-10_Monitoring-Audit/D-10.1.md
status: DRAFT
---

# GDPR Art. 28

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality. | `GDPR-CP11` (Art. 29); `GDPR-CP09` (Art. 28(3)(a)/(b)); `GDPR-CP15` (Art. 32(4)) | D-03.3 |
| SO-GDPR-006 | D-03.3 | Art. 28(3)(a)/(b), Art. 29, Art. 32(4) | Authorised persons act on instructions + confidentiality |
| SO-GDPR-018 | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds applies; erasure is operationally defined as making the data inaccessible to the controller for normal processing paths. | `GDPR-C06` (Art. 4(12) breach-related — operational deletion overlap); `GDPR-CL03` (Art. 5(1)(c) — data-minimisation, downstream of erasure); `GDPR-CL05` (Art. 5(1)(e) — storage limitation), `GDPR-CP10` (Art. 28(3)(g) — deletion polysemy) | D-05.3 |
| SO-GDPR-019 | On end of the provision of processor services, the processor deletes or returns all personal data to the controller (at the controller's choice) and deletes existing copies, unless Union or Member State law requires storage. | `GDPR-CP10` (Art. 28(3)(g)) | D-05.3, D-06.3 |
| SO-GDPR-019 | D-05.3, D-06.3 | Art. 28(3)(g) | Processor data return / deletion on contract end |
| SO-GDPR-020 | Where processing is based on consent (Art. 6(1)(a)) or on a contract (Art. 6(1)(b)) and carried out by automated means, the data subject receives the personal data concerning him or her in a structured, commonly used, machine-readable format and can transmit those data to another controller. | `GDPR-RT10` (Art. 15(3) — copy); `GDPR-CP09` (Art. 28(3)(g) — return/deletion); informed by Art. 20 (cross-chapter inheritance) | D-05.4 |
| SO-GDPR-021 | The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights. | `GDPR-CP07` (Art. 28(1)); `GDPR-CP08` (Art. 28(2)); `GDPR-C03` (Art. 4(7)/(8) — controller/processor) | D-06.1 |
| SO-GDPR-021 | D-06.1 | Art. 28(1)/(2), Art. 4(7)/(8) | Sufficient guarantees from processors |
| SO-GDPR-022 | Contracts (or other legal acts) between controller and processor contain the eight Art. 28(3) mandatory clauses covering subject-matter, type of data, obligations, rights, deletion/return, audit, sub-processor conditions, and confidentiality. | `GDPR-CP09` (Art. 28(3)(a)–(h)); `GDPR-CP08` (Art. 28(2) — sub-processor authorisation) | D-06.3 |
| SO-GDPR-022 | D-06.3 | Art. 28(3)(a)–(h), Art. 28(2) | DPA mandatory clauses; sub-processor authorisation |

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-011
  title: "Instruction-bound processing under least-privilege authorisation"
  source_clauses:
    - { clause_id: GDPR-CP11, article_ref: "Art. 29 — processing under authority" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(4)" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(a)/(b)" }
    - { clause_id: GDPR-C03, article_ref: "Art. 4(7)/(8) — controller/processor definitions" }
  linked_objectives: [SO-GDPR-006]
  sub_domain: [D-03.3]
  nist_csf_mapping:
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
    - { id: PR.AA-06, title: "Access limited to authorized users/services/hardware" }
  applies_to_role: [PROCESSOR, AUTHORISED_PERSONNEL]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 29 requires the processor and any person acting under the authority of the controller or of the processor, who has access to personal data, not to process those data except on instructions from the controller, unless required to do so by Union or Member State law. Art. 32(4) reinforces this for natural persons acting under controller or processor authority by requiring the controller and processor to take steps to ensure that any such natural person does not process the data except on instructions. Art. 28(3)(a) and (b) provide the contractual foundation, requiring the processor contract to stipulate that the processor processes the personal data only on documented instructions from the controller and that persons authorised to process the personal data have committed themselves to confidentiality. Art. 4(7) and 4(8) define controller and processor, anchoring who is subject to whom. Read together, the provisions establish a chain-of-authority pattern: controller → processor → authorised persons, with documented instructions binding each link and Union or Member State law as the only exception.
  security_rationale: |
    The obligation in Art. 29, read with Art. 32(4) and Art. 28(3)(a)/(b), to restrict processing by natural persons under the controller's or processor's authority to documented instructions is operationalised in NIST CSF 2.0 through **PR.AA-05 (Access permissions managed per least privilege)** and **PR.AA-06 (Access limited to authorized users, services, and hardware)**.
    PR.AA-05 anchors the least-privilege authorisation model that maps each authorised person to a scope defined by documented instructions, satisfying the Art. 29 instruction-only rule at the access-control layer and making every act of processing traceable to an instruction in the Art. 28(3)(a) contract.
    PR.AA-06 captures the boundary-enforcement leg: physical and logical access limited to those authorised users, services and hardware, closing the gap that least-privilege definitions alone leave open by ensuring the scope is actually enforced rather than merely declared.
    The two subcategories together operationalise the chain-of-authority pattern (controller to processor to authorised persons) that Arts. 29 and 28(3) establish, with Union or Member State law as the only exception.
    A controller documenting PR.AA-05 permission assignments, PR.AA-06 access-enforcement evidence and the instructions register can demonstrate ex post, under Art. 5(2), that processing outside documented authority was technically prevented and auditably detectable.
  ambiguity_notes: |
    `instructions` is POLY-S2 (formal written vs verbal vs workflow-implied). Reading chosen: instructions must be documented in a form sufficient for audit and supervisory-authority inspection, at minimum the documented instruction in the Art. 28(3)(a) processor contract and any operational instructions issued under it. An alternative reading allowing verbal instructions (provided they are recorded contemporaneously) is acceptable but operationally weaker. A third reading permitting workflow-implied instructions (e.g. processing required by the controller's API) is rejected: workflows are evidence of processing but not a substitute for the documented instruction; controllers must translate workflow-level processing into documented instructions for Art. 28(3)(a) compliance. The Union or Member State law carve-out is narrow and typically arises in law-enforcement, tax, and social-security contexts.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-012
  title: "Confidentiality undertakings for authorised personnel"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(b) — confidentiality obligation" }
    - { clause_id: GDPR-CP11, article_ref: "Art. 29" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(4)" }
  linked_objectives: [SO-GDPR-006]
  sub_domain: [D-03.3, D-08.1]
  nist_csf_mapping:
    - { id: PR.AA-05, title: "Access permissions managed per least privilege" }
    - { id: PR.AT-02, title: "Workforce understands their role-specific security responsibilities" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(3)(b) requires the processor contract to ensure that persons authorised to process personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality. Art. 29 reinforces this by binding natural persons acting under the authority of controller or processor to instruction-only processing. Art. 32(4) reinforces this for natural persons acting under controller/processor authority. Read together, the provisions create a confidentiality ring around any natural person who accesses personal data on behalf of the controller or processor, with contractual or statutory confidentiality as the binding mechanism. The confidentiality obligation is independent of the instruction obligation: a person acting on instructions still owes confidentiality, and breach of confidentiality is breach of the Art. 28(3)(b) contract term.
  security_rationale: |
    The obligation in Art. 28(3)(b), read with Art. 29 and Art. 32(4), to bind every natural person accessing personal data to a confidentiality undertaking is operationalised in NIST CSF 2.0 through **PR.AA-05 (Access permissions managed per least privilege)** and **PR.AT-02 (Workforce understands role-specific security responsibilities)**.
    PR.AA-05 anchors the access-permission layer that enforces the scope each confidentiality undertaking covers, ensuring the contractual or statutory duty is backed by a technical control preventing access beyond the documented need rather than resting on trust alone.
    PR.AT-02 captures the awareness dimension: workforce members understanding their specific confidentiality and security responsibilities, which maps directly onto the onboarding, register and refresh cycle that Art. 28(3)(b) imposes and that gives the undertaking operational substance.
    The two subcategories together operationalise the confidentiality ring that Arts. 28(3)(b) and 32(4) create around any natural person handling personal data, combining the legal-policy lever with the technical-enforcement lever.
    A controller documenting PR.AA-05 scope assignments, PR.AT-02 signed-undertaking register and the refresh cadence per authorised person can demonstrate ex post, under Art. 5(2), that the confidentiality obligation was both contractually imposed and operationally reinforced.
  ambiguity_notes: |
    `appropriate statutory obligation of confidentiality` is VAG-S2. Reading chosen: an obligation equivalent in scope to a contractual NDA covering the personal data scope. An alternative reading accepting any pre-existing statutory professional-secrecy obligation (e.g. medical or legal privilege) is acceptable where the person actually operates under such an obligation. A third reading that no obligation is required where the person is a public-sector employee with existing secrecy duties under Member State law is acceptable in narrow contexts. The "appropriate" qualifier is calibrated to the data sensitivity and the role's exposure.
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

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-031
  title: "Processor erasure or return at end of processing services"
  source_clauses:
    - { clause_id: GDPR-CP10, article_ref: "Art. 28(3)(g)" }
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation (cross)" }
    - { clause_id: GDPR-CL03, article_ref: "Art. 5(1)(c) — data minimisation (cross)" }
  linked_objectives: [SO-GDPR-019]
  sub_domain: [D-05.3, D-06.3]
  nist_csf_mapping:
    - { id: PR.DS-10, title: "Data-in-use protected" }
    - { id: GV.SC-04, title: "Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-CONTRACT-END]
  regulatory_rationale: |
    Art. 28(3)(g) requires the processor, at the choice of the
    controller, to delete or return all the personal data after the end
    of the provision of services relating to processing, and to delete
    existing copies unless Union or Member State law requires storage of
    the personal data. The provision operates at the contract-end moment
    and binds the processor directly without requiring a separate
    data-subject request. Art. 5(1)(e) storage limitation and Art. 5(1)(c)
    data minimisation provide the upstream principles that justify the
    contract-end cleanup. The processor is the operational agent; the
    controller chooses between deletion and return; backup copies are
    within scope unless protected by separate Union or Member State law.
  security_rationale: |
    The obligation in Art. 28(3)(g), Art. 5(1)(e) and Art. 5(1)(c) to erase or return every copy of personal data at the contract-end moment, unless Union or Member State law mandates continued storage, is operationalised in NIST CSF 2.0 through **PR.DS-10 (Data-in-use protected)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**, with PR.DS-10 as the substrate protection.
    PR.DS-10 captures the runtime-protection precondition: any contract-end erasure must be capable of extending through in-use data paths (active replicas, query caches, processing pipelines), which is the operational substrate on which the cryptographic key-destruction choice for `deletes` rests.
    GV.SC-04 anchors the processor-side third-party-evidence practice: erasure must be verifiable — confirmable by audit, test result, or independent inspection — so that the controller can demonstrate, against Art. 5(2), that the post-contract data residue on processor systems was actually removed on the documented date.
    A processor that documents PR.DS-10 in-use data-path coverage and GV.SC-04 evidentiary confirmation of the contract-end deletion can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day any supervisory inspection occurs the personal data under its custody no longer exists in any backup or replica beyond the carved-out legal retention sets.
  ambiguity_notes: |
    The same Berry-flagged POLY-S3 on `deletes` attaches here as in
    SR-GDPR-030 (Berry §3.3.1), and the cryptographic-erasure reading is
    preserved. `all the personal data` and `existing copies` together
    carry SCOPE-Q S2 because both are universal quantifiers (Berry &
    Kamsties 2000): do backups count, do derived datasets count, do audit
    logs count. The reading adopted for this SR treats backups as in
    scope unless protected by a separate legal storage obligation, and
    treats audit logs as out of scope to the extent they are needed for
    legal-accountability purposes. Two alternative readings remain.
    First, the controller-absolute reading would require the processor
    to erase even logs that the controller might need for accountability;
    this conflicts with Art. 28(3)(g)'s exception for storage required by
    Union or Member State law. Second, the processor-discretion reading
    would allow the processor to retain backups indefinitely on the
    grounds of operational convenience; this conflicts with Art. 5(1)(e).
    Remain open: (a) whether immutable audit logs (WORM) escape the
    erasure obligation or must be technically erasable from inception; (b)
    whether derived datasets (aggregated analytics) fall under `all the
    personal data` when the underlying records are pseudonymised.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-033
  title: "Processor due diligence with documented sufficient guarantees"
  source_clauses:
    - { clause_id: GDPR-CP07, article_ref: "Art. 28(1) — processor selection" }
    - { clause_id: GDPR-CP08, article_ref: "Art. 28(2) — sub-processor authorisation" }
    - { clause_id: GDPR-C03, article_ref: "Art. 4(7)/(8) — controller/processor" }
  linked_objectives: [SO-GDPR-021]
  sub_domain: [D-06.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER]
  obligation_type: [PER-PROCESSOR]
  regulatory_rationale: |
    Art. 28(1) requires the controller to use only processors providing
    sufficient guarantees to implement appropriate technical and
    organisational measures in such a manner that processing will meet
    the requirements of GDPR and ensure the protection of data-subject
    rights. Art. 28(2) requires processor authorisation for any
    sub-processor. Art. 4(7) and 4(8) supply the controller and processor
    definitions on which Art. 28 rests.
  security_rationale: |
    The obligation in Art. 28(1), Art. 28(2) and Art. 4(7)/(8) to engage only processors offering sufficient guarantees and to authorise each sub-processor engagement is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-02 is the due-diligence discipline: the controller prioritises processors against risk, applies a documented evaluation (questionnaire, certifications review, security-measures audit, sub-processor inventory) and records the sufficient-guarantees evidence before engagement so the threshold is verifiable rather than self-declared.
    GV.SC-03 is the contractual-realisation discipline: the Art. 28(3) clauses become the formal instrument through which the controller binds the processor — and through which the processor is required to bind its sub-processors — so that the guarantees assessed at selection survive into the operational relationship and through any subsequent processor change.
    A controller that documents GV.SC-02 evidence-of-sufficient-guarantees per processor and GV.SC-03 sub-processor authorisation discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that every processor relationship in force on the day of any supervisory inspection had been selected against a defensible sufficient-guarantees threshold and conducted through an enforceable contractual instrument.
  ambiguity_notes: |
    `sufficient guarantees` carries Berry-flagged VAG-S2 (Berry §5.1);
    EDPB Guidelines 07/2020 propose factors, including commitment to
    GDPR, technical and organisational measures, transparency and
    ability to assist the controller, but the threshold is qualitative.
    The reading adopted for this SR is the documented-due-diligence
    practice: written due-diligence questionnaire, certifications
    review, security-measures audit, sub-processor inventory, and
    contractual Art. 28(3) clauses. An alternative reading under which
    controller self-attestation without independent verification is
    sufficient would lose the substantive protection the threshold is
    meant to provide. Remain open: whether certification schemes (ISO
    27701, SOC 2) on their own satisfy `sufficient guarantees` or
    whether the controller must layer additional assessment.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-034
  title: "Eight-element processor contract with audit and instruction clauses"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(a)–(h) — 8 mandatory clauses" }
  linked_objectives: [SO-GDPR-022]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-CONTRACT]
  regulatory_rationale: |
    Art. 28(3) requires the processor contract (or other legal act under
    Union or Member State law, binding on the processor with regard to
    the controller) to set out the subject-matter and duration of the
    processing, the nature and purpose of the processing, the type of
    personal data and categories of data subjects, and the obligations
    and rights of the controller. That contract or other legal act shall
    stipulate, in particular, that the processor complies with the eight
    sub-clauses: (a) documented instructions, (b) confidentiality of
    authorised persons, (c) Art. 32 measures, (d) sub-processor
    conditions, (e) assistance with data-subject rights, (f) assistance
    with Arts. 32–36, (g) return or deletion on contract end, and (h)
    audits and inspections.
  security_rationale: |
    The obligation in Art. 28(3)(a)–(h) to bind every processor relationship to a contract (or other binding legal act) that stipulates eight concrete duties — documented instructions, personnel confidentiality, Art. 32 measures, sub-processor conditions, data-subject-rights assistance, Arts. 32–36 assistance, return-or-deletion on contract end, and audit access — is operationalised in NIST CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-03 is precisely the vehicle for translating processor-side obligations into contractually binding form; the eight sub-clauses map one-to-one to the implementation measures GV.SC-03 expects an organisation to embed in third-party contracts, from instruction-following (Art. 28(3)(a)) through confidentiality of personnel (Art. 28(3)(b)) to evidence-and-audit access (Art. 28(3)(h)).
    The mapping is structural: GV.SC-03 treats every cybersecurity-relevant third-party commitment as something that must appear on the face of the contract, with sub-clause-by-sub-clause enforcement rather than high-level promises, which matches the closed AND-list reading of the Art. 28(3) duty.
    A controller or processor that documents GV.SC-03 contract-clause coverage at the eight-element level can demonstrate ex post, against the Art. 5(2) accountability duty, that every processor relationship in force on the day of any supervisory inspection was operating under an enforceable Art. 28(3) contract satisfying the eight-sub-clause floor.
  ambiguity_notes: |
    The 8-element list is Berry-flagged COORD-S2 (Berry §5.4.7 closed
    AND-list): all sub-clauses are mandatory and omitting any one puts
    the controller and processor in Art. 28 non-compliance. The reading
    adopted for this SR is the closed-AND-list reading: each sub-clause
    must appear in the contract. An alternative reading under which some
    sub-clauses can be omitted when covered by other legal instruments
    would conflict with the OJ text, which requires the contract itself
    to stipulate the eight elements. Remain open: whether `other legal
    act under Union or Member State law` (e.g., a sectoral regulation)
    can substitute for the Art. 28(3) contract in toto, or whether each
    sub-clause must still appear somewhere in the chain.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-035
  title: "Processor auditability with continuous external-activity monitoring"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(c) — Article 32 measures" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(h) — audits and inspections" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1) cross-reference" }
  linked_objectives: [SO-GDPR-022, SO-GDPR-021]
  sub_domain: [D-06.3, D-10.1]
  nist_csf_mapping:
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits and test results" }
    - { id: DE.CM-06, title: "External service provider activities and services monitored to find potentially adverse events" }
  applies_to_role: [PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(3)(c) requires the processor contract to stipulate that the
    processor takes all measures required pursuant to Art. 32 — the full
    Art. 32 chain covering state-of-the-art assessment, the appropriate-
    level-of-security test, the four-element list (pseudonymisation and
    encryption; ongoing CIA+R; timely restoration; and regular testing).
    Art. 28(3)(h) requires the processor to make available to the
    controller all information necessary to demonstrate compliance with
    the obligations laid down in Art. 28 and to allow for and contribute
    to audits, including inspections, conducted by the controller or
    another auditor mandated by the controller. The two sub-clauses are
    the controller's principal levers into processor security: (c) sets
    the substantive standard by reference and (h) sets the evidentiary
    and audit-access standard. Art. 32(1) in turn cross-references back,
    anchoring the four-element list and the state-of-the-art qualifier.
  security_rationale: |
    The obligation in Art. 28(3)(c), Art. 28(3)(h) and Art. 32(1) to give the controller substantive access to the processor's Art. 32 measure set and to make all information necessary available for audit or inspection is operationalised in NIST CSF 2.0 through **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**, **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)** and **DE.CM-06 (External service provider activities and services are monitored to find potentially adverse events)**.
    GV.SC-03 captures the contractual-vehicle discipline that makes Art. 28(3)(c) enforceable — the full Art. 32 catalogue becomes part of the contract rather than remaining an unrecorded expectation.
    GV.SC-04 captures the periodic-recurrence posture of Art. 28(3)(h): audits, test results and inspections must be a continuous routine rather than a one-off onboarding check, so that the processor's measure set is checked against operational reality at a cadence that survives change.
    DE.CM-06 captures the day-to-day monitoring counterpart that complements periodic audit — adverse events at the processor surface must be observable to the controller in real time, not merely discoverable through annual audit sampling.
    A processor that documents GV.SC-03 contract-level Art. 32 clause coverage, GV.SC-04 routine-assessment cadence, and DE.CM-06 monitoring hand-over can demonstrate ex post, against the Art. 5(2) accountability duty, that the controller's principal levers into processor security were continuously exercisable on the day of any supervisory inspection.
  ambiguity_notes: |
    `all measures required pursuant to Art. 32` is VAG-S3 indirect
    because the chain inherits the Art. 32 ambiguities (state of the
    art, appropriate, the four-element list). The reading adopted for
    this SR is the Art. 32 reading chain: the controller's processor
    contract must reflect the full Art. 32 catalogue, and the
    processor's auditability extends to demonstrating how each Art. 32
    element is implemented. The audit clause itself is largely
    unambiguous (Art. 28(3)(h)) but the substantive scope of what counts
    as `all information necessary` is qualitative. Two alternative
    readings remain. First, a narrow reading of `all measures` that
    limits the contract to a subset of Art. 32 measures (only encryption
    and access control, for instance) would conflict with the Art.
    28(3)(c) text. Second, a controller-discretion reading of the audit
    clause that allows the processor to scope the audit downward would
    conflict with the EDPB Guidelines 07/2020 expectation that audits
    be substantive. Remain open: (a) whether remote audits
    (questionnaire-based) satisfy `audits and inspections` under Art.
    28(3)(h) or whether on-site inspections are required; (b) how
    frequently the controller may audit without becoming a de facto
    shadow-controller.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-036
  title: "Sub-processor authorisation with controller change-notification"
  source_clauses:
    - { clause_id: GDPR-CP08, article_ref: "Art. 28(2) — sub-processor authorisation" }
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(d) — sub-processor conditions (cross)" }
  linked_objectives: [SO-GDPR-022]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-SUB-PROCESSOR]
  regulatory_rationale: |
    Art. 28(2) requires the processor not to engage another processor
    without prior specific or general written authorisation of the
    controller. In the case of general written authorisation, the
    processor must inform the controller of any intended changes
    concerning the addition or replacement of other processors,
    thereby giving the controller the opportunity to object to such
    changes. Art. 28(3)(d) requires the contract to respect the
    conditions for engaging another processor (i.e., flow the (2) and
    (4) rules into the processor contract).
  security_rationale: |
    The obligation in Art. 28(2) and Art. 28(3)(d) to obtain the controller's prior written authorisation before engaging another processor, and to notify the controller of any change in the case of general authorisation so that the controller has an opportunity to object, is operationalised in NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties are known, prioritized, and assessed using a cybersecurity supply chain risk management process)** and **GV.SC-03 (Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and the organization's Cybersecurity Supply Chain Risk Management Plan)**.
    GV.SC-02 captures the prioritisation and assessment discipline: every sub-processor must be known, prioritised against the data it will touch, and assessed using the SCRM process before it is engaged, so that the full chain of entities with personal-data access is visible to and acceptable to the controller.
    GV.SC-03 captures the contract-flowing discipline: the sub-processor authorisation requirement is not merely a one-time notice — it must appear on the face of the contract between controller and processor, with the same written-authorisation and notification-of-change mechanics that the substantive provision requires, so that the controller's object right is exercisable throughout the relationship rather than only at onboarding.
    A processor that documents GV.SC-02 sub-processor assessment on each engagement and GV.SC-03 contract-anchored authorisation plus change-notification discipline can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the personal-data access chain was complete, documented and within the controller's objectable scope.
  ambiguity_notes: |
    `prior specific or general written authorisation` carries VAG+SCOPE-Q
    S2 (Berry §5.1): the `specific` versus `general` distinction is the
    same as the Art. 6(1)(a) consent-specificity question. The reading
    adopted for this SR is that written authorisation in either form is
    acceptable, with notification-on-changes required in the general case
    (EDPB Guidelines 07/2020). An alternative reading under which only
    `specific` authorisation suffices for sensitive data flows would
    tighten the obligation but conflicts with the OJ text, which makes
    the general authorisation path explicit. Remain open: whether
    `opportunity to object` requires a reasonable objection window (e.g.,
    30 days) or whether silent acquiescence suffices.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-037
  title: "Controller-evidenced processor erasure on contract end"
  source_clauses:
    - { clause_id: GDPR-CP09, article_ref: "Art. 28(3)(g) — return or deletion" }
    - { clause_id: GDPR-CL05, article_ref: "Art. 5(1)(e) — storage limitation" }
  linked_objectives: [SO-GDPR-022, SO-GDPR-019]
  sub_domain: [D-06.3, D-05.3]
  nist_csf_mapping:
    - { id: PR.DS-12, title: "Data managed consistent with risk strategy" }
    - { id: GV.SC-04, title: "Suppliers routinely assessed using audits and test results" }
  applies_to_role: [PROCESSOR]
  obligation_type: [PER-CONTRACT-END]
  regulatory_rationale: |
    Art. 28(3)(g) duplicates the processor-end-of-services obligation
    already captured under SR-GDPR-031, and is included here as a
    contract-obligations-cluster rule to support controller-side
    contract drafting. The substantive obligation is identical: at the
    choice of the controller, the processor must delete or return all
    the personal data after the end of the provision of services
    relating to processing, and must delete existing copies unless
    Union or Member State law requires storage. Art. 5(1)(e) storage
    limitation provides the upstream principle. This rule anchors the
    controller-side audit-and-evidence obligation: the controller must
    verify, at contract end and periodically, that the processor has
    in fact deleted or returned the data and has documented the basis
    for any continued retention.
  security_rationale: |
    The obligation in Art. 28(3)(g) and Art. 5(1)(e), approached from the controller-side audit-and-evidence angle, to verify that the processor has honoured its contract-end erasure-or-return duty and to hold evidence supporting any continued retention claim is operationalised in NIST CSF 2.0 through **PR.DS-12 (Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of data)** and **GV.SC-04 (Suppliers and other third parties are routinely assessed using audits, test results, or other forms of evaluation to confirm they are meeting their contractual obligations)**.
    PR.DS-12 captures the data-management spine on which the controller's evidence pack rests: the controller treats the post-contract residual data set as a discrete risk-strategy object whose erasure or continued-retention status must be documented per category, including the legal-storage carve-out justifications.
    GV.SC-04 captures the routine third-party assessment posture: contract-end erasure is one instance of an ongoing third-party-evaluation cadence, and the controller must be able to call on audit, test result, or independent inspection evidence at the moment of any data-subject or supervisory query — not merely at the moment of contract end.
    A controller that documents PR.DS-12 per-category erasure evidence and GV.SC-04 periodic third-party-verification cadence can demonstrate ex post, against the Art. 5(2) accountability duty, that on the day of any supervisory inspection the processor's contract-end deletion or return was both verified and recorded.
  ambiguity_notes: |
    No new ambiguity beyond the SR-GDPR-030 POLY-S3 on `deletes`
    (Berry §3.3.1), and the cryptographic-erasure reading is preserved.
    The reading adopted here is the same: cryptographic erasure,
    understood as destruction of the cryptographic key held outside the
    data substrate, is the most defensible operational interpretation
    because it scales to backups and replicas without per-copy
    destruction, in line with EDPB Guidelines 5/2020 on storage
    limitation. Two alternative readings — strict physical destruction,
    which conflicts with cloud-architecture realities, and logical
    deletion, which conflicts with EDPB guidance — are preserved here
    for symmetry with SR-GDPR-030. The substantive novelty at
    SR-GDPR-037 is the controller-side audit-and-evidence obligation
    rather than the deletion mechanics. Remain open: (a) whether the
    controller must obtain affirmative evidence-of-erasure certificates
    per data category or whether a single processor attestation
    suffices; (b) how the controller should handle the gap between
    contract end and the processor's actual deletion confirmation.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-055
  title: "Adequacy-governed cross-border transfer inventory and review"
  source_clauses:
    - { clause_id: GDPR-TR01, article_ref: "Art. 44 — general transfer principle" }
    - { clause_id: GDPR-TR02, article_ref: "Art. 45(1) — adequacy-based transfer" }
    - { clause_id: GDPR-TR03, article_ref: "Art. 45(3) — periodic review of adequacy" }
    - { clause_id: GDPR-C07, article_ref: "Art. 4(16) — main establishment (cross)" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.SC-02, title: "Suppliers prioritized and assessed using SCRM processes" }
    - { id: GV.SC-03, title: "Contracts used to implement SCRM" }
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER]
  regulatory_rationale: |
    Art. 44 establishes the umbrella principle for cross-border transfers: any transfer of personal data to a third country or international organisation shall take place only if the Chapter V conditions are complied with by the controller and processor, including for onward transfers, and the level of protection of natural persons guaranteed by GDPR is not undermined (Recital 6). Art. 45(1) exempts transfers covered by a Commission adequacy decision from any specific authorisation requirement, on the basis that the third country, territory, sector or international organisation ensures an adequate level of protection. Art. 45(3) requires the Commission to specify, in its implementing decision, the mechanism for a periodic review of that adequacy assessment, at least every four years, and to amend, suspend or repeal the decision where the available information reveals that the third country or international organisation no longer ensures an adequate level of protection. Art. 4(16) anchors the main-establishment concept used in Art. 44 for determining which supervisory authority has jurisdiction over the cross-border processing.
  security_rationale: |
    The obligation in Art. 44, Art. 45(1) and Art. 45(3) is operationalised in
    NIST CSF 2.0 through **GV.SC-02 (Suppliers and other third parties known,
    prioritized, and assessed using a cybersecurity supply chain risk management
    process)**, **GV.SC-03 (Contracts with suppliers and other third parties used
    to implement appropriate measures)** and **GV.OC-03 (Legal, regulatory, and
    contractual requirements regarding cybersecurity — including privacy and
    civil liberties obligations — are understood and managed)**.

    GV.SC-02 controls the inventory and prioritisation of cross-border data
    flows: the controller must maintain a transfer register that maps every
    outbound flow to its destination, its legal mechanism, and its assessed risk
    under the Schrems II substantial-equivalence test. GV.SC-03 controls the
    contractual articulation of each transfer's safeguards, including
    onward-transfer clauses that bind downstream recipients to equivalent
    protection. GV.OC-03 controls the legal-basis frame, including the temporal
    stability of adequacy decisions and the trigger for re-assessment whenever
    the Commission adopts, suspends or repeals an Art. 45(3) decision.

    Together the three subcategories give the controller a SCRM-style governance
    of cross-border data flows embedded in a managed regulatory frame, enabling
    ex-post demonstration to the supervisory authority that every transfer is
    inventoried, contractually anchored, and reassessed against the latest
    adequacy posture.
  ambiguity_notes: |
    The not undermined qualifier of Art. 44 carries VAG-S3 because the OJ text does not fix a metric for the level of protection and supervisory authorities have not published a quantitative threshold. Reading chosen: the substantial-equivalence reading from CJEU Schrems II (C-311/18 §96), under which the essential content of EU protection must be preserved in the third country, with the EDPB Recommendations 01/2020 supplementary-measures framework operating as the operational remediation path when the destination regime falls short. An alternative reading would treat not undermined as a procedural rather than substantive requirement, satisfied by the existence of any lawful basis for the transfer; this reading is rejected because Schrems II §96 held that procedural legality does not compensate for substantive deficiencies in the destination regime, and the EDPB Recommendations 01/2020 §B.1 make the essential-equivalence test binding for transfers to third countries whose domestic law permits extensive public-authority access. A second alternative reading focuses on the foreseeability of the third-country practice at the time of transfer rather than on the essential equivalence at the time of assessment; this reading is consistent with Schrems II §94 but operationally difficult because it requires the controller to predict regulatory drift in the destination jurisdiction. Remain open: (a) whether the Schrems II essential-equivalence test applies equally to processors and to controllers or whether a processor-tier standard may be lower given that the processor is itself bound by Art. 28; (b) whether supplementary measures (encryption, pseudonymisation, contractual minimisation) can rescue transfers to regimes where the public-authority access regime is materially deficient, or whether the Schrems II ruling forecloses supplementary measures in such cases.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

