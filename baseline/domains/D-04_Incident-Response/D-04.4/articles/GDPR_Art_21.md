---
document_id: AEGIS-PREPROC-GDPR-ART-21
title: GDPR Art. 21 — SecurityObjectives & SecurityRules
regulation: GDPR
article: Art. 21
applicable: true
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ../02_SecurityRules_NIST.md
related_documents:
  - ../01_SecurityObjectives.md
  - ../02_SecurityRules_NIST.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md
  - ../../CrossRegulation/DomainAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md
  - ../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md
  - ../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md
  - ../../CrossRegulation/DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
  - ../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---

# GDPR Art. 21

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

_No standalone SO row cites this article directly (covered via the rules below)._

## Security Rules (from 02_SecurityRules_NIST.md)

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-001
  title: "CIA + resilience baseline for personal data processing"
  source_clauses:
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f)" }
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(b)" }
    - { clause_id: GDPR-C01, article_ref: "Art. 4(1) — personal data definition" }
  linked_objectives: [SO-GDPR-001]
  sub_domain: [D-01.1, D-01.4]
  nist_csf_mapping:
    - { id: PR.DS-01, title: "Data-at-rest protected" }
    - { id: PR.DS-10, title: "Data-in-use protected" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 5(1)(f) establishes integrity and confidentiality as one of the six principles relating to processing of personal data, requiring that personal data be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures. Art. 32(1)(b) operationalises this by listing the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services among the measures that the controller and processor must implement under the Art. 32(1) risk-based preamble. Read together, the two provisions establish a continuous obligation to maintain the CIA triad, augmented by an explicit resilience dimension, across the entire processing surface. Two textual points warrant attention for compliance scoping. First, "appropriate" in Art. 5(1)(f) is anchored by the Art. 32(1) preamble to a risk-based test (state of the art, costs of implementation, nature, scope, context and purposes of processing, risks of varying likelihood and severity), meaning the controller must justify the chosen security level ex post rather than declaring it ex ante. Second, the disjunction "technical or organisational measures" admits both an inclusive reading (at least one category suffices) and a strict reading (both required); the parallel wording of Art. 24(1) written with "and" pulls toward the strict reading, which is also the dominant position under ISO 27001-aligned compliance programmes.
  security_rationale: |
    The obligation in Art. 5(1)(f) and Art. 32(1)(b) to maintain the confidentiality, integrity, availability and resilience of personal data is operationalised in NIST CSF 2.0 through **PR.DS-01 (Data-at-rest protected)** and **PR.DS-10 (Data-in-use protected)**.
    PR.DS-01 anchors the protection of stored personal data against unauthorised or unlawful processing and against accidental loss, destruction or damage, satisfying the Art. 5(1)(f) integrity-and-confidentiality principle at the storage layer where the dominant exfiltration surface sits.
    PR.DS-10 extends that protection to data undergoing query, transformation and join operations inside application processes, closing the gap that at-rest controls alone leave open and covering the full data lifecycle that the Art. 32(1)(b) ongoing-confidentiality duty references, including the explicit resilience dimension that signals graceful degradation and recovery to a known-good state.
    A controller that documents PR.DS-01 and PR.DS-10 coverage, key-custodian assignments and the irreversibility properties of the chosen primitives can demonstrate ex post, against the Art. 5(2) accountability threshold, that the risk-based level of security chosen under the Art. 32(1) preamble was actually delivered.
  ambiguity_notes: |
    Art. 5(1)(f) and Art. 4(1) carry S3 ambiguity. On "appropriate" (VAG), the chosen reading anchors the term to the Art. 32(1) risk-based test: the controller documents the chosen security level against the five risk factors in the Art. 32(1) preamble and refreshes this assessment when material change occurs. An alternative reading, supported by industry practice under ISO 27001 and SOC 2 frameworks, treats "appropriate technical and organisational measures" as requiring both control families in parallel, regardless of risk; this is the more conservative reading and is the de facto baseline for any organisation holding formal certification. A third, looser reading treats "appropriate" as whatever the controller self-declares, which does not survive supervisory inspection but is sometimes observed in pre-DPO controllers. The chosen reading here is the inclusive risk-anchored reading, which is consistent with EDPB Guidelines on accountability 07/2019. On "personal data" (POLY/SCOPE-Q per Art. 4(1)), the scope of "identifiable" is read in line with CJEU Breyer C-582/14 §45, which adopts a "means likely reasonably to be used" test. This reading brings pseudonymous data into scope where re-identification is operationally feasible, but leaves genuinely anonymous data outside. EDPB Guidelines 05/2020 on consent §3.4 reinforce this position. A broader reading, extending to inferred and derived data subject to algorithmic singling-out, has been gaining traction post-IAB Europe C-604/22 but is not yet definitively settled. On the "technical or organisational" disjunction (COORD), the chosen reading treats the OR as inclusive, in line with the dominant grammatical reading and consistent with EDPB Guidelines on Art. 32; controllers following the strict reading are equally compliant. Remain open: (a) whether forward-looking cryptographic-agility (quantum-readiness) is required by "state of the art" under Art. 32(1), pending EDPB clarification and ENISA post-quantum guidance; and (b) how the resilience dimension of Art. 32(1)(b) interacts with separate BCDR obligations, pending cross-regulation alignment with DORA Art. 11–12 and NIS 2 Art. 21(2)(c).
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-024
  title: "Timely availability restoration after physical or technical incident"
  source_clauses:
    - { clause_id: GDPR-CP15, article_ref: "Art. 32(1)(c) — timely restore" }
    - { clause_id: GDPR-CL06, article_ref: "Art. 5(1)(f) — integrity & confidentiality (cross)" }
    - { clause_id: GDPR-CP16, article_ref: "Art. 32(2) — risk enumeration" }
  linked_objectives: [SO-GDPR-014]
  sub_domain: [D-04.4]
  nist_csf_mapping:
    - { id: PR.IR-04, title: "Adequate resource capacity to ensure availability maintained" }
    - { id: PR.DS-11, title: "Backups created, protected, maintained, tested" }
    - { id: RC.RP-04, title: "Critical mission functions restored through recovery plan" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [CONTINUOUS]
  regulatory_rationale: |
    Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident. Art. 5(1)(f) supplies the integrity-and-confidentiality cross-reference, and Art. 32(2) anchors the five-event risk enumeration underlying the trigger assessment. Read together, the provisions establish a recovery-and-restore obligation: the controller and processor must be able to bring availability and access back to a defined state within a timeframe appropriate to the processing context, and the ability must be tested.
  security_rationale: |
    The obligation in Art. 32(1)(c), read with Art. 5(1)(f) and Art. 32(2), to restore the availability of and access to personal data in a timely manner after a physical or technical incident is operationalised in NIST CSF 2.0 through **PR.IR-04 (Adequate resource capacity to ensure availability)**, **PR.DS-11 (Backups created, protected, maintained, and tested)** and **RC.RP-04 (Critical mission functions restored through recovery plan)**.
    PR.IR-04 anchors the capacity dimension that the Art. 32(1)(c) timely-restoration duty presupposes: adequate resource headroom to absorb the incident and recover availability within the documented Recovery Time Objective.
    PR.DS-11 captures the backup foundation — created, integrity-protected, maintained and tested — that makes restoration possible at all, satisfying the recovery-from-known-good-state requirement and aligning with the EDPB evidence expectation for Art. 32(1)(c).
    RC.RP-04 closes the cycle by executing the tested recovery plan that restores critical processing functions, with documented Recovery Point Objectives per activity.
    A controller documenting PR.IR-04 capacity evidence, PR.DS-11 backup-test results and RC.RP-04 recovery-exercise records can demonstrate ex post, under Art. 5(2), that timely restoration was not aspirational but tested, resourced and deliverable.
  ambiguity_notes: |
    `in a timely manner` (Art. 32(1)(c)) carries POLY+VAG-S3. Operational reading chosen: RTO defined per processing activity, as an objective measure documented in the controller's business continuity policy. An alternative reading treating timely as as-soon-as-practicable for the specific incident is operationally similar but framing-different; the chosen reading ties timeliness to a documented and testable metric. Recital 49 (non-binding) attempts to fix `timely manner` as "as soon as possible", which is directionally useful but does not bind the controller. EDPB Guidelines 7/2019 on certification treat tested backups and recovery plans as evidence of Art. 32(1)(c) compliance. Remain open: (a) whether the Art. 32(1)(c) `timely manner` threshold differs across processing contexts (e.g. real-time processing vs batch processing), pending EDPB clarification; and (b) how the recovery obligation interacts with separate BCDR obligations under DORA Art. 11–12 and NIS 2 Art. 21(2)(c), pending cross-regulation alignment.
```

### SO-GDPR-001 / SO-GDPR-014 (CIA + resilience)

```yaml
- sr_id: SR-GDPR-057
  title: "Derogation-based transfer fallback under strict preconditions"
  source_clauses:
    - { clause_id: GDPR-TR08, article_ref: "Art. 49(1)(a) — explicit consent" }
    - { clause_id: GDPR-TR09, article_ref: "Art. 49(1)(d) — important public interest" }
    - { clause_id: GDPR-TR10, article_ref: "Art. 49(1) second subparagraph — catch-all" }
  linked_objectives: [SO-GDPR-033]
  sub_domain: [D-06.3, D-09.1]
  nist_csf_mapping:
    - { id: GV.OC-03, title: "Legal/regulatory/contractual requirements understood and managed" }
    - { id: UNMAPPED_CSF, title: "Derogation under Art. 49 is GDPR-specific with no clean CSF 2.0 mapping" }
  applies_to_role: [CONTROLLER, PROCESSOR]
  obligation_type: [PER-TRANSFER, ONE_TIME]
  regulatory_rationale: |
    Art. 49 derogations apply only in the absence of an adequacy decision under Art. 45(3) and of appropriate safeguards under Art. 46, including binding corporate rules. Art. 49(1) lists seven disjunctive grounds: explicit consent after being informed of possible risks; necessity for the performance of a contract between the data subject and the controller or implementation of pre-contractual measures at the data subject's request; necessity for a contract concluded in the interest of the data subject between the controller and another natural or legal person; important reasons of public interest; establishment, exercise or defence of legal claims; protection of the vital interests of the data subject or other persons where the data subject is physically or legally incapable of giving consent; transfer from a register intended to provide information to the public (Recital 111–115). The second subparagraph of Art. 49(1) adds a catch-all: transfers may take place where the transfer is not repetitive, concerns a limited number of data subjects, is necessary for compelling legitimate interests of the controller which are not overridden by the interests, rights or freedoms of the data subject, and the controller has assessed all the circumstances and put in place suitable safeguards (Recital 113).
  security_rationale: |
    The obligation in Art. 49(1)(a), Art. 49(1)(d) and Art. 49(1) second
    subparagraph has no clean NIST CSF 2.0 subcategory and is anchored on the
    closest fit **GV.OC-03 (Legal, regulatory, and contractual requirements
    regarding cybersecurity — including privacy and civil liberties obligations —
    are understood and managed)** within the broader **GV.OC — Organizational
    Context** category; the residual gap is noted as UNMAPPED_CSF.

    GV.OC-03 controls the controller's understanding of the regulatory
    preconditions on which any Art. 49 derogation depends — absence of an
    adequacy decision under Art. 45(3), absence of Art. 46 appropriate
    safeguards, and satisfaction of one of the seven enumerated grounds or the
    catch-all (not repetitive, limited number of data subjects, compelling
    legitimate interests, suitable safeguards). CSF 2.0 does not enumerate
    derogation-availability analysis and GV.OC-03 is a poor fit because it is
    designed for ongoing regulatory understanding rather than exception-
    availability gating, but it is the closest available anchor.

    Because the CSF gap is documented, the controller must supplement GV.OC-03
    with a GDPR-specific derogation-use register that records each catch-all
    reliance, the compelling-interests analysis, and the suitable safeguards
    deployed. Accountability is sustained through the documented gap
    (UNMAPPED_CSF + unmapped_csf_justification) and through GV.OC-03's
    regulatory-understanding trail that demonstrates the derogation fallback was
    used only where adequacy and Art. 46 safeguards were unavailable.
  ambiguity_notes: |
    Explicitly (Art. 49(1)(a)) carries POLY-S3 against the specific qualifier of Art. 4(11) and the explicit qualifier of Art. 9(2)(a); reading chosen: the strongest consent form, risk-informed and documented, building on EDPB Guidelines 05/2020 §3.4 and the Schrems II framing of risk disclosure. The catch-all qualifiers not repetitive, limited number, compelling legitimate interests, suitable safeguards carry VAG-S3 and SCOPE-Q-S3 because none of them is quantitatively bounded in the OJ text; compelling in particular carries POLY-S3 across Art. 21(1) and Art. 49(1) (Recital 47 cross-reference), and the EDPB Guidelines 2/2018 emphasise that compelling means more than legitimate and approaches necessity. An alternative reading confines the catch-all to transfers that are truly exceptional and treats recurring or systematic reliance on it as a structural misuse of the derogation; this reading is consistent with that framing and operationally shifts the burden onto the controller to demonstrate the exceptional nature of each catch-all reliance. A second alternative reading treats not repetitive as a per-data-subject test rather than per-data-flow; this reading is harder to operationalise and is inconsistent with the structural purpose of the catch-all. Remain open: (a) whether repetitive in the catch-all should be measured per data subject, per transfer, or per data flow, given that no OJ anchor specifies the unit; (b) whether suitable safeguards in the catch-all may be purely contractual or must include technical measures (encryption, pseudonymisation) per Schrems II §134.
  unmapped_csf_justification: |
    The four Art. 49 catch-all conjunctive qualifiers and the
    `compelling legitimate interests` qualifier have no clean CSF 2.0
    Subcategory. The closest mapping GV.OC-03 is a poor fit.
```

---

> **Cross-regulation:** for each sub-domain below, see the Domain/Deep analysis counterparts listed in `related_documents`.

