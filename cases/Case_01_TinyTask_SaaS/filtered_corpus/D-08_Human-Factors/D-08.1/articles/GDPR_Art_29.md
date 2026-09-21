---
document_id: AEGIS-PREPROC-GDPR-ART-29
title: GDPR Art. 29 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 29
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
  - ../../CrossRegulation/DomainAnalysis/D-08_Human-Factors/D-08.1.md
  - ../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md
status: DRAFT
---

# GDPR Art. 29

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality. | `GDPR-CP11` (Art. 29); `GDPR-CP09` (Art. 28(3)(a)/(b)); `GDPR-CP15` (Art. 32(4)) | D-03.3 |
| SO-GDPR-006 | D-03.3 | Art. 28(3)(a)/(b), Art. 29, Art. 32(4) | Authorised persons act on instructions + confidentiality |

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

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

