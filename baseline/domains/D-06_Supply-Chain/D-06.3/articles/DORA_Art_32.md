---
document_id: AEGIS-PREPROC-DORA-ART-32
title: DORA Art. 32 — SecurityObjectives & SecurityRules
regulation: DORA
article: Art. 32
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
status: DRAFT
---

# DORA Art. 32

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-014
  title: "BC implementation arrangements with independent audit review"
  source_clauses:
    - { clause_id: DORA-C23, article_ref: "Art. 11(2) — `implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e)`" }
    - { clause_id: DORA-C24, article_ref: "Art. 11(3) — `associated ICT response and recovery plans … shall be subject to independent internal audit reviews` (non-microenterprises)" }
  linked_objectives: [SO-DORA-010]
  sub_domain: [D-04.2, D-04.4]
  nist_csf_mapping:
    - { id: RC.RP-04, title: "Critical mission functions and services are restored through the implementation of the recovery plan" }
    - { id: PR.IR-04, title: "Adequate resource capacity to ensure availability is maintained" }
  applies_to_role: [FINANCIAL_ENTITY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 11(2) requires financial entities to implement the ICT
    business continuity policy through dedicated, appropriate and
    documented arrangements, plans, procedures and mechanisms
    aiming to (a) continue critical operations, (b) recover from
    ICT-related incidents, (c) manage crises, (d) protect
    stakeholders, and (e) comply with regulatory obligations. Art.
    11(3) requires ICT response and recovery plans to be subject
    to independent internal audit reviews for non-microenterprises.
    The five-objective list (a)–(e) is functionally distinct from
    the three Cs of generic BC (continuity, recovery, crisis) —
    the addition of stakeholder protection and regulatory
    compliance reflects the cross-stakeholder dimension of
    ICT-related disruption in financial entities (NIS 2 Art.
    21(2)(c) on continuity parallels the first three objectives;
    GDPR Art. 32 security-of-processing converges on stakeholder-
    protection (d) for personal-data cases).
    [OJ-corrective note (v0.2 audit, material): Art. 11(2)(c)/(d)/(e) — BCP objectives mislabelled. OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) (manage crises, protect stakeholders, comply with regulatory obligations) do NOT match the OJ items.]
  security_rationale: |
    The obligation in Art. 11(2)+(3) for BC-implementation
    arrangements and independent internal audit review is
    operationalised in NIST CSF 2.0 through **RC.RP-04 (Critical
    mission functions and services are restored through the
    implementation of the recovery plan)** and **PR.IR-04 (Adequate
    resource capacity to ensure availability is maintained)**.
    RC.RP-04 anchors the recovery-execution layer: the documented
    arrangements, plans, procedures, and mechanisms (the four-
    artefact AND) operationalise the five-objective Art. 11(2)(a)–(e)
    list into concrete recovery capability — continuity of critical
    functions, rapid response-and-resolution, plan activation for
    containment, impact-and-loss estimation, and crisis-communication
    plus CA reporting. PR.IR-04 supplies the resource-capacity
    substrate — redundant compute, storage, network, and
    alternative-site capacity — without which recovery plans are
    paper artefacts. The OJ Art. 11(3) audit-review obligation
    (non-microenterprises) maps onto RC.RP-04's recovery-execution
    verification dimension, ensuring the arrangements are subject
    to second-line assurance rather than self-attestation. The
    accountability link under Art. 5(2): the recovery-plan
    inventory, resource-capacity attestation, audit-review records,
    and findings-to-improvement-cycle documentation produce the
    documented evidence trail the management body can present to
    competent authorities demonstrating that BC arrangements are
    operationally substantive, audit-verified, and continuously
    resourced rather than nominal.
  ambiguity_notes: |
    Source clause DORA-C23 carries S2 on the 3-way AND of
    adjectives (`dedicated, appropriate, documented`) and the
    4-way AND of artefact types (`arrangements, plans,
    procedures, mechanisms`); reading chosen: R1 cumulative
    (all four artefacts + all three qualities required). DORA-C24
    `response AND recovery plans` (COORD S2) — R1 distinct plans
    / R2 composite plan; R1 literal (the OJ enjoins two plan
    types). `associated` (VAG S2 — Art. 11(3) refers back to
    Art. 11(1) BC policy). `independent internal audit reviews`
    (POLY S2) — R1 third-line assurance / R2 second-line review
    with independence / R3 any internal audit with independence;
    R3 literal. The microenterprise carve-out is preserved in
    `applies_to_role` per the OJ scope. A contrasting reading of
    `response AND recovery plans` would treat them as a single
    composite plan, but the OJ enumeration with `AND` and the
    operational difference between response (triage, containment)
    and recovery (service restoration) justifies the distinct
    reading. An open question is whether `independent internal
    audit` permits internal-audit-function co-sourcing under
    external-lead assurance terms, or restricts to in-house
    audit function with documented independence.
```

### SO-DORA-001 (CIA + A maintained across data states)

```yaml
- sr_id: SR-DORA-020
  title: "Information-security standards compliance for ICT third-party contracts"
  source_clauses:
    - { clause_id: DORA-C36, article_ref: "Art. 28(5) — `financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards`" }
  linked_objectives: [SO-DORA-011]
  sub_domain: [D-06.3]
  nist_csf_mapping:
    - { id: GV.SC-01, title: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" }
    - { id: GV.SC-03, title: "Contracts with suppliers and other third parties are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program" }
  applies_to_role: [FINANCIAL_ENTITY, ICT_THIRD_PARTY]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 28(5) requires financial entities to enter only into contractual
    arrangements with ICT third-party service providers that comply with
    appropriate information security standards; for contractual arrangements
    concerning critical or important functions, the financial entity shall
    take due consideration of the use by providers of the most up-to-date and
    highest quality information security standards. The clause carries the
    central DORA ambiguity flagged in `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the OJ text does not
    name a specific standard — ISO/IEC 27001, SOC 2, NIST CSF, CIS Controls,
    and ENISA guidance are all plausible reference points, and EBA Guidelines
    on outsourcing arrangements provide the supervisory-recognised floor for
    critical or important functions outsourcing. The clause co-exists with
    CRA Art. 24 conformity-assessment duties for ICT products supplied under
    contract (Regulation (EU) 2024/2847) and with the GDPR Art. 32 security-
    of-processing baseline. An EBA RTS under Art. 28(9) is expected to refine
    the standards-set for CTPPs but has not closed the open-naming question.
  security_rationale: |
    The Art. 28(5) standards-compliance duty is operationalised in NIST CSF
    2.0 through **GV.SC-01 (A cybersecurity supply chain risk management
    program, strategy, objectives, policies, and processes are established
    and agreed to by organizational stakeholders)** and **GV.SC-03 (Contracts
    with suppliers and other third parties are used to implement appropriate
    measures designed to meet the objectives of an organization's cybersecurity
    program)**. GV.SC-01 establishes the entity-wide supply-chain cybersecurity
    governance that articulates which information-security standards the entity
    treats as acceptable baselines — the very `appropriate information security
    standards` that the OJ text leaves POLY — and the criteria for distinguishing
    between routine and critical-or-important-function contracts. GV.SC-03
    converts that governance into enforceable contract terms, ensuring that
    the `most up-to-date and highest quality` anchor for critical-or-important
    functions is reflected in measurable contract clauses (certification
    evidence, audit-rights linkage to Art. 30(3)(e), sub-outsourcing
    transparency). Together these two subcategories close the gap between an
    entity's stated standards-set and the contractual surface with third-party
    providers, allowing ex-post demonstration under Art. 28(5) that every
    ICT-service contract was anchored in a documented program-level standards
    framework and tied back through enforceable contract terms — satisfying
    both the general `appropriate` floor and the critical-or-important
    `most up-to-date AND highest quality` escalator.
  ambiguity_notes: |
    S3 POLY on `information security standards` — the central DORA ambiguity
    per `../Regulation/DORA/Ambiguity/05_DORA.md` §3.5: the clause names no specific standard. The chosen
    reading is entity-selected standards with supervisory-recognised standards
    (ISO/IEC 27001, SOC 2 Type 2, NIST CSF, ENISA guidance, EBA Guidelines)
    as the EU-acceptable floor. S3 POLY on `most up-to-date` is read against
    alternatives of current published version, state-of-the-art, or frontier
    practice. S3 VAG on `highest quality` is read at the literal most-
    rigorous, comprehensive, industry-leading end of the spectrum. S3 COORD
    on `most up-to-date AND highest quality` — both anchors required
    cumulatively. S2 POLY on `critical or important functions` — the
    undefined distinction propagates from `../Regulation/DORA/Ambiguity/05_DORA.md` §3.4. Compliance-
    framework note: ISO 27001, NIST 800-53, and EBA Guidelines function as
    reference frameworks rather than technology selections and are not part
    of the tech-stack exemption. Remain open: identification of the binding
    standards-set for CTPP designation remains subject to EBA RTS under
    Art. 28(9) and to the Joint Committee oversight of CTPPs at Ch. V Sec. 2.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

