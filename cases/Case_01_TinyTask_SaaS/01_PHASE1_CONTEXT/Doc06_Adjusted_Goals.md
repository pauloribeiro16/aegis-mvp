---
document_id: AEGIS-P1-RICH-07c
title: Adjusted Goals per Sub-Domain (Rich Mode)
phase: 1
version: 7.0
created: 2026-08-06
updated: 2026-08-14
author: Executor (tech-free-restructure)
status: COMPLETE
id_format: AG-D-XX.X-NNN (canonical Phase 1)
ao_canonical_ids_count: 35
ao_driven_total_count: 62
status_history:
  - { date: 2026-08-06, status: DRAFT, sprint: 0, by: 'Fase de Especificação 0 skeleton' }
  - { date: 2026-08-06, status: RECONCILED, sprint: 1, by: 'Fase de Especificação 1 reconciliation' }
  - { date: 2026-08-06, status: CORPUS_ENRICHED, sprint: 2, by: 'Fase de Especificação 2 corpus enrichment' }
  - { date: 2026-08-06, status: ADJUSTED_GOALS, sprint: 4, by: 'Fase de Especificação 4 adjusted goals' }
  - { date: 2026-08-06, status: DEEP_ENRICHED, sprint: 5, by: 'Fase de Especificação 5 DEEP enrichment' }
  - { date: 2026-08-10, status: TECH_FREE_PHASE1, sprint: 7, by: 'Fase de Especificação 7 tech-free restructure' }
  - { date: 2026-08-10, status: AG_MIGRATED, sprint: 8, by: 'Fase de Especificação 8 Executor' }
  - { date: 2026-08-10, status: AG_CANONICAL_IDS, sprint: 9, by: 'Fase de Especificação 9 Executor' }
  - { date: 2026-08-13, status: NIST_CONTROLS_LAYER_PILOT, sprint: 10, by: 'Fase de Especificação 10 Executor' }
  - { date: 2026-08-14, status: NIST_CONTROLS_FULL_COVERAGE, sprint: 11, by: 'Fase de Especificação 11 Executor (§3 expansion)' }
tech_free_restructure_date: 2026-08-10
tech_free_sections: ['§2', '§3', '§4', '§5', '§6']
nist_controls_mapping_date: 2026-08-13
nist_controls_mapping_contract: corr-016-nist-controls-layer
nist_controls_full_coverage: true
active_subdomains_mapped: 35
active_subdomains: 35
not_addressed_subdomains: [D-02.4, D-06.4, D-08.3]
appendix_a_status: PARTIAL_LEGACY
appendix_a_cards_count: 66
detail_cards_count: 66
appendix_a_legacy_cards: 66
appendix_a_migrated_to_deprecated: 8
appendix_a_migrated_d01_cards:
  - 'AG-D-01.1-001'
  - 'AG-D-01.2-001'
  - 'AG-D-01.3-001'
  - 'AG-D-01.4-001'
  - 'AG-D-01.1-002'
  - 'AG-D-01.2-002'
  - 'AG-D-01.3-002'
  - 'AG-D-01.4-002'
former_pg_sg_count: 74
former_pg_count: 37
former_sg_count: 37
ag_count: 66
ag_count_includes_deprecated: 8
ag_count_in_main: 66
tensions_expanded_count: 4
case: Case_01_TinyTask_SaaS
applicable_regs: [GDPR, CRA]
cross_checked_against: [07_Structured_Compliance_Matrix.md, 07b_Proportionality_Profile.md, 10_Privacy_Security_Objectives.md, proportionality_model.md, phase1_ontology.yaml]
inputs: [Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md, Doc11_Structured_Compliance_Matrix.md, Doc12_Proportionality_Profile.md, phase1_ontology.yaml, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md]
outputs: [11_Rules_Catalog.md]
related_documents: [07b_Proportionality_Profile.md, 04_Company_Context_Assessment.md, phase1_ontology.yaml, 02_PHASE2_RULES/10_Privacy_Security_Goals.md, 02_PHASE2_RULES/09_Strategic_Tensions_Report.md, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md]
frozen: false
supersedes: 02_PHASE2_RULES/10_Privacy_Security_Goals.md §3-§4
---

# Adjusted Goals per Sub-Domain (Rich Mode)

---

## §0 Document Purpose

This document is the **Phase 1 Adjusted Goals layer** of the TinyTask SaaS case — the Fase 0 → Fase 1 exchange of the pipeline I/O contract (ADR-004): the frozen corpus **Baseline Goals** (high-level goal `SO-D-XX.Y.HL` + per-regulation baseline goals) restated against one company. It binds every ACTIVE sub-domain to:

1. A **regulatory floor** — the corpus Baseline Goals, consumed by reference.
2. A **framing** — the company context that conditions every goal: size/tier, area of operation, regulatory roles, inherited capabilities (§2).
3. **Adjusted Goals** — one D1 card per goal (ADR-003): company-proportional, regulation-anchored, slot 001 GDPR / slot 002 CRA (§3).
4. **Resolutions** for the 4 strategic tensions (T-001..T-004), in §4.
5. A **Track B tier** per sub-domain, in §5.
6. The **NIST controls mapping** per sub-domain, in §6.

## §1 Regulatory Floor (corpus, by reference)

> The floor for every goal below is the corpus-frozen **Baseline Goal** of each sub-domain — the high-level baseline goal (`SG-D-XX.Y.HL`; legacy expansion "High-Level Security Objective") and the regulation-specific baseline goals (legacy "Sub-SO") — in `baseline/domains/<D-XX_Dir>/<D-XX.Y>/objective.md` + `regs/<REG>.md`, consumed by reference (rule R9). Full chain: `baseline/MAPPINGS/traceability/`.

## §2 Framing (TinyTask SaaS)

| Dimension | Framing |
|---|---|
| Size | 8-person team, MICRO scale — tiers LIGHTWEIGHT/MINIMAL. Consequences: security-awareness training runs as a single documented cycle (D-08.1); custodian/consumer key-role separation is achieved at the platform-role level, not by disjoint individuals (D-01.3); recovery evidence collapses to a single dual-purpose artefact for both regulators (D-04.4). |
| Area of operation | B2B SaaS appointment platform for psychology clinics (EU-domiciled, Portugal); processes personal data of patients and clinic staff on a continuous, non-occasional basis. |
| Regulatory roles | Data controller (GDPR) and manufacturer of a product with digital elements (CRA); the company distributes its own product and occupies neither the importer nor the distributor role. |
| Inherited capabilities | Supplier-managed hosting: at-rest encryption capability and key custody are inherited from a supplier-managed layer rather than operated in-house (D-01.1, D-01.3). |

## §3 Adjusted Goals

> One row per goal (D1 card, ADR-003): slot `001` = GDPR-driven, slot `002` = CRA-driven. The former high-level table is not duplicated — the refinement floor of every goal is its **Parent goal** (`SO-D-XX.Y.HL`). Tier/Priority live in §4 (Track B decision trail). `Pattern` and `Property` are draft classifications awaiting researcher review (P7). Goal-specific adjustments stay inline; scale/hosting generics live in §2 Framing.


### D-01.1 — Data at Rest Encryption

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.1-001` | Personal data at rest is processed in a manner that ensures appropriate security — including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage — using appropriate technical or organisational measures, with the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services. | maintain | C|I | `SG-D-01.1.HL` | GDPR | Art. 5(1)(f) + Art. 32(1)(b) | PR.DS-01, PR.DS-10 | The `appropriate` threshold is anchored by the five Art. 32(1) preamble factors; at MICRO scale, cost of implementation and state of the art jointly justify inheriting the encryption capability from the hosting layer. |
| `AG-D-01.1-002` | Where the product stores data — personal or other — the confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms. | maintain | C|I | `SG-D-01.1.HL` | CRA | Annex I Part I (2)(e) | PR.DS-01 | The state-of-the-art anchor is the stricter of the two floors on this subdomain; meeting it discharges the data-protection `appropriate` obligation on the same datastore. |

### D-01.2 — Data in Transit Encryption

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.2-001` | Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration — accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted. | maintain | C|I | `SG-D-01.2.HL` | GDPR | Art. 32(1)(b) + Art. 32(2) | PR.DS-02, PR.IR-01 | — |
| `AG-D-01.2-002` | Where data is transmitted by the product — personal or other — the confidentiality of the data in transit is protected by encrypting relevant data using state-of-the-art mechanisms, with the attack-surface-limitation leg constraining the exposed interfaces through which the data could otherwise leak. | maintain | C|I | `SG-D-01.2.HL` | CRA | Annex I Part I (2)(e) + (2)(j) | PR.DS-02, PR.IR-01 | — |

### D-01.3 — Key Management

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.3-001` | Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject — the key, the mapping table, or the tokenisation seed — is kept separately and is subject to appropriate technical and organisational measures that prevent attribution. | maintain | C | `SG-D-01.3.HL` | GDPR | Art. 4(5) + Art. 34(3)(a) + Art. 32(1)(a) | PR.DS-01, PR.IR-03 | — |
| `AG-D-01.3-002` | Cryptographic keys and related authentication material used to protect the confidentiality and integrity of data stored, transmitted or otherwise processed by the product are managed with separation of roles, so that possession of the key material is not bundled with possession of the operational environment that uses it. | maintain | C | `SG-D-01.3.HL` | CRA | Annex I Part I (2)(d) + (2)(e) | PR.DS-01, PR.AA-05, GV.OV-01 | The Annex I text does not mention key management explicitly; the key-separation reading rests on combining the access-control duty with the `other technical means` residual, flagged as a text-versus-interpretation gap in the corpus synthesis catalogue. |

### D-01.4 — Data Integrity

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.4-001` | Personal data are accurate and, where necessary, kept up to date, and inaccurate data are erased or rectified without delay, with the integrity property anchored to two further legs — storage integrity and the rectification cascade carrying the Art. 19 recipient-notification duty. | maintain | I | `SG-D-01.4.HL` | GDPR | Art. 5(1)(d) + Art. 5(1)(f) + Art. 16 + Art. 19 | PR.DS-01, PR.DS-10, PR.DS-10 | — |
| `AG-D-01.4-002` | The integrity of stored, transmitted, or otherwise processed data — as well as the integrity of commands, programs, and configuration — is protected against any manipulation or modification not authorised by the user, and corruption is reported to the user or administering party. | maintain | I | `SG-D-01.4.HL` | CRA | Annex I Part I (2)(f) + (2)(l) | PR.DS-01, PR.DS-10, PR.PS-04 | The universal quantifier `any` makes this integrity protection unconditional — it admits no risk-based relaxation at MICRO scale. |

### D-02.1 — Vulnerability Identification

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.1-001` | The company operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment when the risk represented by processing operations changes. | achieve | C | `SG-D-02.1.HL` | GDPR | Art. 32(1)(d) + Art. 35(11) | ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02 | — |
| `AG-D-02.1-002` | The product is made available on the market without known exploitable vulnerabilities, and vulnerabilities contained in it — including those in the components listed in the software bill of materials — are identified and documented on a continuing basis throughout the support period. | achieve | C | `SG-D-02.1.HL` | CRA | Annex I Part I (2)(a) + Annex I Part II (1) + Art. 13(3) + Art. 13(7) | ID.RA-01, ID.AM-02, PR.PS-02 | — |

### D-02.2 — Patch Management

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.2-002` | Vulnerabilities are addressed and remediated through security updates without delay, provided separately from functionality updates where technically feasible, and disseminated to users via mechanisms ensuring secure distribution together with advisory messages describing the action users can take. | achieve | C | `SG-D-02.2.HL` | CRA | Annex I Part II (2) + (7) + (8) + Annex I Part I (2)(c) + Art. 13(8) + Art. 13(9) | PR.PS-02, PR.IR-03, ID.RA-01, PR.PS-01 | Each security update remains available for at least 10 years or the remainder of the support period, whichever is longer — a retention floor that outlasts the company's current planning horizon. |

### D-02.3 — Coordinated Vulnerability Disclosure

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.3-002` | The company puts in place, documents and enforces a coordinated vulnerability disclosure policy, publicly discloses information about fixed vulnerabilities once an update is available, facilitates the sharing of information about potential vulnerabilities through a publicly identifiable contact address, and designates a single point of contact for users including security researchers. | achieve | C | `SG-D-02.3.HL` | CRA | Annex I Part II (4) + (5) + (6) + Art. 13(8) + Art. 13(17) + Annex II §2 | GV.PO-01, GV.SC-04, RS.CO-03 | — |

### D-03.1 — Identity Lifecycle

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.1-001` | The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification before action is taken; the company may request additional information necessary to confirm identity, and the verification scope is itself constrained by data minimisation. | maintain | C | `SG-D-03.1.HL` | GDPR | Art. 12(6) + Art. 11(2) + Art. 5(1)(c) | PR.AA-03, PR.AA-02, PR.DS-10 | — |
| `AG-D-03.1-002` | Identities, credentials, and access entitlements for users, services, and integrated components of the product are managed in a verifiable manner throughout the operational lifetime of the product, backed by unique product identification and a designated single point of contact. | maintain | C | `SG-D-03.1.HL` | CRA | Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3 | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | — |

### D-03.2 — Authentication Strength

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.2-001` | Persons authorised to process personal data act only on documented instructions from the company and are bound by confidentiality or an appropriate statutory obligation of confidentiality; the identity of data subjects making rights-exercise requests is verified proportionately to the risk of mis-identification. | maintain | C | `SG-D-03.2.HL` | GDPR | Art. 28(3)(b) + Art. 29 + Art. 32(4) + Art. 12(6) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.2-002` | Protection from unauthorised access uses appropriate control mechanisms — which may include authentication, identity, or access-management systems — appropriate to the identified cybersecurity risk of the product. | maintain | C | `SG-D-03.2.HL` | CRA | Annex I Part I (2)(d) | PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09 | The Annex I formulation is a non-exhaustive three-way disjunction, so the obligation is discharged by any mechanism proportionate to the assessed risk. |

### D-03.3 — Authorisation & Least Privilege

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.3-001` | Persons authorised to process personal data act only on documented instructions and are bound by confidentiality, with the documented instructions binding the controller → processor → authorised-persons chain of authority. | maintain | C | `SG-D-03.3.HL` | GDPR | Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) + Art. 4(7) + Art. 4(8) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.3-002` | Access to the product, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported, and attack surfaces including external interfaces limited. | maintain | C | `SG-D-03.3.HL` | CRA | Annex I Part I (2)(d) + (2)(j) | PR.AA-05, PR.AA-06, DE.CM-09 | — |

### D-03.4 — Secure System Defaults

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.4-001` | Processing systems ensure that, by default, only personal data necessary for each specific purpose are processed — across the four AND-coordinated dimensions of amount collected, extent of processing, period of storage, and accessibility — and personal data are not made accessible without the individual's intervention to an indefinite number of natural persons. | maintain | C|privacy-right | `SG-D-03.4.HL` | GDPR | Art. 25(2) + Art. 25(1) + Art. 5(1)(c) | PR.PS-01, PR.DS-10, GV.PO-01 | — |
| `AG-D-03.4-002` | The product is made available on the market with a secure-by-default configuration, including the possibility for the user to reset it to its original state, and that configuration ensures vulnerabilities can be addressed through security updates installed automatically within an appropriate timeframe, enabled by default, with a clear opt-out and a postponement option. | maintain | C|privacy-right | `SG-D-03.4.HL` | CRA | Annex I Part I (2)(b) + (2)(c) | PR.PS-01, PR.DS-10, GV.SC-03 | — |

### D-04.1 — Incident Detection & Triage

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.1-001` | Personal-data breaches are detected and triaged, and the moment of becoming aware is documented so as to anchor the 72-hour notification clock. | achieve | A | `SG-D-04.1.HL` | GDPR | Art. 33(1) + Art. 4(12) | DE.AE-02, PR.PS-04, DE.CM-01 | — |
| `AG-D-04.1-002` | Relevant internal activity of the product — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported. | achieve | A | `SG-D-04.1.HL` | CRA | Annex I Part I (2)(l) | DE.CM-09, PR.PS-04, RS.MA-02 | — |

### D-04.2 — Containment & Mitigation

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.2-001` | Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including measures rendering the personal data unintelligible to any unauthorised person and subsequent measures ensuring the high risk no longer materialises; the measures taken or proposed are described in the supervisory-authority notification. | achieve | A | `SG-D-04.2.HL` | GDPR | Art. 34(3)(a) + Art. 34(3)(b) + Art. 33(3)(d) | PR.DS-10, PR.IR-04, RC.RP-04 | — |
| `AG-D-04.2-002` | The availability of essential and basic functions is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks; the negative impact on the availability of services provided by other devices or networks is minimised; and where the product or processes are not in conformity, corrective measures are taken or the product is withdrawn or recalled. | achieve | A | `SG-D-04.2.HL` | CRA | Annex I Part I (2)(h) + (2)(i) + (2)(k) + Art. 13(21) | PR.IR-04, PR.IR-03, DE.CM-09 | — |

### D-04.3 — Regulatory Notification

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.3-001` | A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the company becomes aware of it — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms. | achieve | A|accountability | `SG-D-04.3.HL` | GDPR | Art. 33(1) | RS.CO-02, RS.MA-01, RS.MA-03 | — |
| `AG-D-04.3-002` | An actively-exploited vulnerability contained in the product that the company becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours; vulnerability notification within 72 hours with general information, nature of the exploit, mitigations and user actions; and a final report within 14 days of a corrective or mitigating measure being available. | achieve | A|accountability | `SG-D-04.3.HL` | CRA | Art. 14(2)(a) + Art. 14(2)(b) + Art. 14(2)(c) | RS.MA-02, RS.CO-02 | — |

### D-04.4 — Restoration & Recovery

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.4-001` | The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and the availability of and access to personal data is restored in a timely manner in the event of a physical or technical incident. | maintain | A | `SG-D-04.4.HL` | GDPR | Art. 32(1)(b) + Art. 32(1)(c) + Art. 5(1)(f) + Art. 32(2) | PR.IR-04, PR.DS-01, RC.RP-04 | — |
| `AG-D-04.4-002` | The availability of essential and basic functions is protected also after an incident through resilience and recovery measures, with exploitation-mitigation mechanisms and techniques reducing incident impact and corrective measures restoring conformity. | maintain | A | `SG-D-04.4.HL` | CRA | Annex I Part I (2)(h) + (2)(i) + (2)(k) + Art. 13(21) | PR.IR-03, PR.DS-10 | — |

### D-05.1 — Data Minimisation

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.1-001` | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed; further processing is compatible with the original purposes per the Art. 6(4) five-factor test; by-design and by-default minimisation applies, and an impact assessment is performed for high-risk processing. | maintain | privacy-right | `SG-D-05.1.HL` | GDPR | Art. 5(1)(c) + Art. 6(4) + Art. 25(1)/(2) + Art. 35 | PR.DS-10, ID.AM-03, GV.OC-03, GV.PO-01 | The Art. 9 special-category leg is inert for this case: no special-category data is processed. |
| `AG-D-05.1-002` | Data processed by the product — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with the risk assessment and the intended purpose plus reasonably foreseeable use supplying the proportionality calibration. | maintain | privacy-right | `SG-D-05.1.HL` | CRA | Annex I Part I (2)(g) + Art. 3(23) + Art. 13(2) + Art. 13(3) | PR.DS-10, ID.AM-03 | — |

### D-05.2 — Retention & Archiving

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.2-001` | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes processed; longer retention is permitted only where lawful and subject to Art. 89(1) safeguards, and the record of processing documents the envisaged erasure time limits per category of data. | maintain | privacy-right | `SG-D-05.2.HL` | GDPR | Art. 5(1)(e) + Art. 89(1) + Art. 30(1)(f) | PR.DS-10, ID.AM-03 | — |
| `AG-D-05.2-002` | Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail, and the support-period end-date is provided clearly and understandably at the time of purchase. | maintain | privacy-right | `SG-D-05.2.HL` | CRA | Art. 13(8) + Art. 13(9) + Art. 13(18) + Art. 13(19) + Annex I Part II (7) + (8) + Annex II §7 | PR.PS-02, GV.OV-02, GV.OC-04 | The 5-year support-period floor and the 10-year availability tail are absolute; they do not scale down with company size. |

### D-05.3 — Right to Erasure

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.3-001` | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds (a)–(f) applies; on processor contract end, the processor deletes or returns all personal data and existing copies. | cease | privacy-right | `SG-D-05.3.HL` | GDPR | Art. 17(1)(a)–(f) + Art. 28(3)(g) | PR.DS-10, PR.DS-10, GV.SC-04 | — |
| `AG-D-05.3-002` | The user of the product can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner. | cease | privacy-right | `SG-D-05.3.HL` | CRA | Annex I Part I (2)(m) | PR.DS-10, PR.DS-10, PR.DS-02 | — |

### D-05.4 — Data Portability

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.4-001` | The data subject receives personal data in a structured, commonly used, machine-readable format, supplied without undue delay and free of charge, and can transmit those data to another controller without hindrance; where technically feasible the company transmits directly to the receiving controller. | achieve | privacy-right | `SG-D-05.4.HL` | GDPR | Art. 20(1)–(4) + Art. 15(3) + Art. 12(3) + Art. 12(5) | PR.DS-10, PR.DS-10 | The right is scoped to consent- or contract-based processing carried out by automated means, which covers the company's B2B subscription relationship. |

### D-06.1 — Vendor Risk Assessment

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.1-001` | The company engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures such that processing meets the Regulation's requirements and protects data-subject rights, with the Art. 28(3) closed-list clauses documented and the sub-processor authorisation chain material to the due diligence. | achieve | accountability | `SG-D-06.1.HL` | GDPR | Art. 28(1) + Art. 28(2) + Art. 28(3)(a)–(h) | GV.SC-02, GV.SC-04, ID.AM-04 | — |
| `AG-D-06.1-002` | The company exercises due diligence when integrating components sourced from third parties — including free and open-source software components not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product; on becoming aware of a component vulnerability it addresses and remediates it without delay and shares relevant information with the component supplier. | achieve | accountability | `SG-D-06.1.HL` | CRA | Art. 13(5) + Art. 13(6) + Art. 3(48) | GV.SC-01, GV.SC-02, ID.RA-02 | — |

### D-06.2 — Software Bill of Materials

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.2-002` | The company draws up and maintains a software bill of materials covering the components and dependencies contained in the product, in a commonly used and machine-readable format that includes at minimum the top-level dependencies. | achieve | C | `SG-D-06.2.HL` | CRA | Annex I Part II (1) | ID.AM-02, GV.SC-02, GV.SC-03 | — |

### D-06.3 — Contractual Security Obligations

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.3-001` | Controller/processor contracts and related transfer instruments include the eight-element Art. 28(3)(a)–(h) floor, sub-processor authorisation and change-notification, processor security-measure commitments, audit and inspection access, and contract-end return or deletion; the Art. 46 safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA. | maintain | accountability | `SG-D-06.3.HL` | GDPR | Art. 28(3)(a)–(h) + Art. 32 + Art. 46 + Art. 48 | — | — |
| `AG-D-06.3-002` | Contractual security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place the product on the Union market only after verifying conformity assessment, technical documentation, conformity marking and manufacturer identification, and distributors act with due care and escalate non-conformity or vulnerabilities. | maintain | accountability | `SG-D-06.3.HL` | CRA | Art. 19 + Art. 20 | — | The company distributes its own product directly and occupies neither the importer nor the distributor role, so this row binds only through the manufacturer-side duties those operators verify against. |

### D-07.1 — Secure-by-Design Principles

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.1-001` | The company implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement data-protection principles in an effective manner and to integrate the necessary safeguards into the processing, and ensures that by default only personal data necessary for each specific purpose are processed. | maintain | C | `SG-D-07.1.HL` | GDPR | Art. 25(1) + Art. 25(2) | PR.PS-06, PR.DS-10 | — |
| `AG-D-07.1-002` | When placing the product on the market, the company ensures it has been designed, developed and produced in accordance with the essential cybersecurity requirements of Annex I Part I, with the cybersecurity risk assessment propagated across the six lifecycle phases — planning, design, development, production, delivery, and maintenance — with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact. | maintain | C | `SG-D-07.1.HL` | CRA | Art. 13(1) + Art. 13(2) | PR.PS-06, PR.PS-01 | — |

### D-07.2 — Secure Coding Practices

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.2-002` | The company designs, develops, and produces the product so as to limit its attack surfaces, including the attack surfaces of external interfaces, and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques. | maintain | C | `SG-D-07.2.HL` | CRA | Annex I Part I (2)(j) + (2)(k) | PR.PS-06, PR.PS-02 | — |

### D-07.3 — Build & Update Distribution Security

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.3-002` | The company securely distributes updates for the product in a timely manner, including through automatic updates where appropriate, and ensures that updates are disseminated free of charge, are clearly described, and contain information on the security improvements and on the actions the user should take. | maintain | C | `SG-D-07.3.HL` | CRA | Annex I Part II (7) + (8) | PR.PS-06, PR.PS-02 | — |

### D-07.4 — Change Management

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.4-002` | The company ensures that procedures are in place for products that are part of a series of production to remain in conformity with the Regulation. | achieve | C | `SG-D-07.4.HL` | CRA | Art. 13(14) | GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04 | — |

### D-08.1 — General Security Awareness

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.1-001` | The data protection officer informs and advises the company and the employees who carry out processing of their obligations under the Regulation, and monitors compliance including the assignment of responsibilities and the awareness-raising and training of staff involved in processing operations. | maintain | accountability | `SG-D-08.1.HL` | GDPR | Art. 39(1)(a) + Art. 39(1)(b) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.1-002` | The product is accompanied by detailed instructions — or an internet address referring to such instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use. | maintain | accountability | `SG-D-08.1.HL` | CRA | Annex II §8(a)–(e) | PR.AT-01 | — |

### D-08.2 — Role-Specific Competence

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.2-001` | The data protection officer monitors compliance including the assignment of responsibilities and the awareness-raising and training of staff involved in processing operations — the role-specific layer of the DPO-catalysed awareness function. | maintain | accountability | `SG-D-08.2.HL` | GDPR | Art. 39(1)(b) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.2-002` | Where the product is intended for integration into other products, the company provides the information necessary for the integrator to comply with the essential cybersecurity requirements of Annex I Part I and the documentation requirements of Annex VII. | maintain | accountability | `SG-D-08.2.HL` | CRA | Annex II §8(f) | PR.AT-02, GV.SC-03 | — |

### D-09.1 — Information Security Policies

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.1-001` | The company implements appropriate technical and organisational measures, such as policies, which are designed to implement data-protection principles in an effective manner, carrying the Art. 5(2) accountability burden with the data protection officer as governance anchor. | maintain | accountability | `SG-D-09.1.HL` | GDPR | Art. 24(1) + Art. 5(2) + Art. 37–39 | GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02 | — |
| `AG-D-09.1-002` | The company establishes the policies, processes and procedures necessary to implement its product-security obligations, including the coordinated vulnerability disclosure policy, secure-update distribution, support-period determination, and cessation-of-operations communication. | maintain | accountability | `SG-D-09.1.HL` | CRA | Art. 13(8) + Art. 24(1) | GV.PO-01, GV.PO-02 | — |

### D-09.2 — Impact & Risk Assessments

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.2-001` | Prior to processing likely to result in a high risk to the rights and freedoms of natural persons, the company carries out a data-protection impact assessment covering the four Art. 35(7) content items, reviewed when the risk represented by the processing operations changes. | achieve | accountability | `SG-D-09.2.HL` | GDPR | Art. 35(1) + Art. 35(7) + Art. 35(11) | ID.RA-05, ID.RA-04 | — |
| `AG-D-09.2-002` | The company documents the cybersecurity risk assessment and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use and indicating the applicability of the Annex I Part I (2) requirements, recorded in the Annex VII §3 risk-assessment record. | achieve | accountability | `SG-D-09.2.HL` | CRA | Art. 13(2) + Art. 13(3) + Art. 13(4) + Annex VII §3 | ID.RA-05, GV.SC-07 | — |

### D-09.3 — Asset Inventories

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.3-002` | The company draws up technical documentation containing at least a general description of the product and a description of the design, development, production and vulnerability-handling processes including the system architecture description, drawn up before placing on the market, updated during the support period, and kept at the disposal of market surveillance authorities. | achieve | accountability | `SG-D-09.3.HL` | CRA | Annex VII §1 + §2 + Art. 31(2) + Art. 13(13) | ID.AM-01, ID.AM-02 | — |

### D-09.4 — Records of Processing

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.4-001` | The company maintains a record of processing activities under its responsibility, in writing or electronic form, containing the Art. 30(1) seven-item content list, with a parallel processor-side record, made available to the supervisory authority on request. | maintain | accountability | `SG-D-09.4.HL` | GDPR | Art. 30(1)–(5) | ID.AM-08, PR.DS-10, GV.PO-02 | The Art. 30(5) under-250-employee exception is nominally available to an 8-person team but is not relied upon, because the processing is neither occasional nor free of risk to data-subject rights. |
| `AG-D-09.4-002` | The company draws up the technical documentation before placing the product on the market, carries out the conformity assessment procedure, draws up the EU declaration of conformity and affixes the conformity marking, and keeps the technical documentation and the declaration at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer. | maintain | accountability | `SG-D-09.4.HL` | CRA | Art. 13(12) + Art. 13(13) + Art. 28 + Art. 30 + Art. 31 + Art. 32 | ID.AM-08, PR.DS-10, ID.RA-05 | — |

### D-10.1 — Continuous Security Monitoring

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.1-001` | The company implements appropriate technical and organisational measures to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services and regularly tests, assesses and evaluates their effectiveness, monitoring for the five Art. 32(2) risk types with a clear definition of the moment of becoming aware of a breach. | maintain | A | `SG-D-10.1.HL` | GDPR | Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) | DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04 | — |
| `AG-D-10.1-002` | The product provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, with an opt-out mechanism for the user, and the company facilitates the sharing of information about potential vulnerabilities through a single contact address. | maintain | A | `SG-D-10.1.HL` | CRA | Annex I Part I (2)(l) + Annex I Part II (6) | DE.CM-01, DE.CM-09, ID.IM-04 | — |

### D-10.2 — Audit Logging & Traceability

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.2-001` | The company maintains compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections — records of processing, consent records, processor contract records, breach notification records, and impact-assessment records — made available to the supervisory authority on request. | maintain | A|accountability | `SG-D-10.2.HL` | GDPR | Art. 30(3) + Art. 5(2) + Art. 31 | PR.DS-01, PR.PS-04, DE.CM-01, GV.PO-02 | — |
| `AG-D-10.2-002` | The company maintains the technical documentation, preserves the cybersecurity risk-assessment documentation during the support period with updates as appropriate, and ensures that test reports demonstrating verification of conformity with Annex I Parts I and II form part of the technical documentation and are available on reasoned request from market surveillance authorities. | maintain | A|accountability | `SG-D-10.2.HL` | CRA | Annex VII §3 + §5–§8 + Art. 13(4) + Art. 13(22) + Annex I Part II (3) | PR.DS-01, PR.PS-02, GV.PO-02, ID.RA-04 | — |

### D-10.3 — Compliance Testing

| AG ID | Goal | Pattern | Property | Baseline goal id (corpus) | Reg | Artigos | Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.3-001` | The company implements a process for regularly testing, assessing and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment at least when the risk represented by processing operations changes. | maintain | accountability | `SG-D-10.3.HL` | GDPR | Art. 32(1)(d) + Art. 35(11) | PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03 | — |
| `AG-D-10.3-002` | The company carries out effective and regular tests and reviews of the product, and the technical documentation contains the reports of the tests carried out to verify the conformity of the product and of the vulnerability-handling processes with Annex I Parts I and II. | maintain | accountability | `SG-D-10.3.HL` | CRA | Annex I Part II (3) + Annex VII §6 + Annex VIII + Art. 6 + Annex III | PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03 | The product is default-class — not Class I, Class II, or critical under Art. 6 and Annex III — so conformity is demonstrated via the Annex VIII Part I internal-production-control module without notified-body involvement. |

**Inline notes — critical IDs carried in the main flow:**

- **`AG-D-01.3-001` (D-01.3 Key Management)** — Phantom goal. `CR-D-01.3-001` in the Phase 2 catalog references the legacy PG ID, but `OBL-D-01.3-001` carries no PG/SG in Phase 2 Doc 10; the goal exists only in this document's Appendix A. Carried as finding **F-01 / F-03** (LOW); resolution deferred to the human arbiter per AGENTS.md P7. The regulatory obligation itself is unaffected and is stated in the D-01.3 row above.
- **`AG-D-09.1-001` (D-09.1 Information Security Policies)** — Dual-coverage with `AG-D-09.1-002` (finding F-02, documented as intentional; NI reconciled to 2.500 under F-10). The same policy architecture satisfies both GDPR Art. 24 and CRA Art. 31 — one artefact, two regulatory readings.
- **`AG-D-09.2-001` (D-09.2 Impact & Risk Assessments)** — Dual-coverage with `AG-D-09.2-002` . Resolved by tension **T-M-001**: a single unified assessment produces both the data-protection impact assessment and the product cybersecurity risk assessment as dual outputs.

---

**Inline notes — critical IDs carried in the main flow:**

- **`AG-D-04.3-002` (D-04.3 Regulatory Notification)** — Anchor goal for tension **T-001**. Highest-priority SG in the case and the only HIGH-risk profile: the internal notification workflow runs on the **max-SLA 24h** routing so that the shorter of the two regulatory deadlines governs the single internal clock. See §4 T-001.
- **`AG-D-09.1-002` (D-09.1 Information Security Policies)** — Dual-coverage with `AG-D-09.1-001`; the same policy architecture discharges both. Technical documentation retention is **10 years or the support period, whichever is longer** (CRA Art. 13(13)). Normalised Intensity **2.500** is authoritative.
- **`AG-D-09.2-002` (D-09.2 Impact & Risk Assessments)** — Dual-coverage with `AG-D-09.2-001` ; the same assessment framework serves both, per T-M-001.

---

---

## §4 Tensions Resolved (4 tensions)

### T-001 (D-04.3) — Notification timing difference

**Type:** timing | **Severity:** HIGH

**Root cause.** Two regulations impose different notification deadlines on the same event — one 72 hours, the other 24 hours — and the company occupies both regulated roles simultaneously. A single incident therefore triggers both obligations, with clocks that start from related but distinct awareness moments and recipients that are different bodies.

**Resolution.** A single internal notification workflow operates with the **shortest applicable regulatory deadline**. A unified event record generates per-recipient submissions from one clock-start discipline, so the company bears both obligations on the same artefact rather than running two parallel workflows with divergent service levels.

**Risk if unresolved.** HIGH — fines up to €10M or 2% of turnover under the longer-deadline regulation, plus market-surveillance non-conformity under the shorter. For an 8-person team the cumulative exposure could be existential.

**Anchors:** §3 D-04.3 rows; `AG-D-04.3-002` (Appendix A).

### T-002 (D-06.1, D-06.3) — Vendor-management scope

**Type:** scope | **Severity:** MEDIUM

**Root cause.** One regulation governs downstream data processors; the other governs the entire product supply chain including open-source dependencies. The two scopes overlap on the same suppliers but ask different questions of them.

**Resolution.** A **single vendor-management template** addresses both the data-processor obligations and the product supply-chain obligations, producing dual-output documentation that satisfies both regulatory scopes from one due-diligence pass.

**Risk if unresolved.** MEDIUM — processor non-compliance plus a supply-chain gap. Mitigation cost is bounded by the reuse: the marginal effort of the second scope is small once the first is documented.

**Anchors:** §3 D-06.1 and D-06.3 rows; `AG-D-06.1-001`, `AG-D-06.1-002`, `AG-D-06.3-001`, `AG-D-06.3-002` (Appendix A).

### T-003 (D-09.4, D-09.1) — Documentation overlap

**Type:** requirement | **Severity:** MEDIUM

**Root cause.** Two regulations require written records with materially different content focus and structure — one oriented to processing activities, the other to product technical documentation — yet both describe the same underlying system.

**Resolution.** A **unified documentation repository** serves both the records-of-processing requirement and the technical-documentation requirement, with retention aligned to the **longest applicable regulatory floor** (10 years or the support period, whichever is longer).

**Risk if unresolved.** MEDIUM — audit findings under both regulations. Mitigation is procedural (template unification), not infrastructural, so it does not compete for engineering capacity.

**Anchors:** §3 D-09.1 and D-09.4 rows; `AG-D-09.1-001`, `AG-D-09.1-002`, `AG-D-09.4-001`, `AG-D-09.4-002` (Appendix A).

### T-004 (D-08.2) — Data-protection versus product-security competence

**Type:** intensity | **Severity:** LOW

**Root cause.** An 8-person team must carry both data-protection competence and product-security competence. At MICRO scale these overlap in the same individuals; at LARGE or MAX scale they are distinct roles with distinct reporting lines.

**Resolution.** A **competency matrix** covers both data-protection and product-security competence, with separation of duties preserved at the role-documentation level even where the same person holds both roles.

**Risk if unresolved.** LOW — the competent-personnel requirement is procedural. Documenting competence discharges the obligation; no headcount change is implied at current scale.

**Anchors:** §3 D-08.2 row; `AG-D-08.2-001`, `AG-D-08.2-002` (Appendix A).

---

## §5 Track B Decision Trail (37 rows)



| Sub-Domain | S | I | P | Tier | Rationale |
|-----------|---|---|---|------|-----------|
| D-01.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-01.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-02.4 | MICRO | BUILD_REQUIRED | SHOULD | DEFERRED | §5.2 drop-one-tier + MICRO + FTE=0.85 ≤ 1.0 → DEFERRED |
| D-03.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-03.2 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-03.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-03.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-04.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-05.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-06.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-06.4 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-07.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-07.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-08.1 | MICRO | INHERITABLE | MUST | MINIMAL | §5.1 row MICRO col INHERITABLE = MINIMAL |
| D-08.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-09.4 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.1 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.2 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |
| D-10.3 | MICRO | BUILD_REQUIRED | MUST | LIGHTWEIGHT | §5.1 row MICRO col BUILD_REQUIRED = LIGHTWEIGHT |

---

## §6 NIST Controls Mapping

### §6.1 D-01.1 — Data at Rest Encryption

_Applicable regulations: GDPR, CRA_

#### §7.1.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |

#### §7.1.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizatio... | NIST_PF/GOVERN-P/GV.RM-P1.json |
| IDENTIFY-P | ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. | NIST_PF/IDENTIFY-P/ID.RA-P2.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |

### §6.2 D-01.2 — Data in Transit Encryption

_Applicable regulations: GDPR, CRA_

#### §7.2.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |

#### §7.2.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.3 D-01.3 — Cryptographic Key Management

_Applicable regulations: GDPR, CRA_

#### §7.3.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-04 | Identity assertions are protected, conveyed, and verified | NIST_CSF/PROTECT/PR.AA-04.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |

#### §7.3.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizatio... | NIST_PF/GOVERN-P/GV.RM-P1.json |
| IDENTIFY-P | ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. | NIST_PF/IDENTIFY-P/ID.RA-P2.json |
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| PROTECT-P | PR.AC-P3 | Remote access is managed. | NIST_PF/PROTECT-P/PR.AC-P3.json |
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.4 D-01.4 — Data Integrity Mechanisms

_Applicable regulations: GDPR, CRA_

#### §7.4.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |

#### §7.4.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.5 D-02.1 — Vulnerability Identification

_Applicable regulations: GDPR, CRA_

#### §7.5.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| GOVERN | GV.RM-01 | Risk management objectives are established and agreed to by organizational stake... | NIST_CSF/GOVERN/GV.RM-01.json |
| GOVERN | GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizi... | NIST_CSF/GOVERN/GV.RM-06.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| IDENTIFY | ID.IM-02 | Improvements are identified from security tests and exercises, including those d... | NIST_CSF/IDENTIFY/ID.IM-02.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-03 | Internal and external threats to the organization are identified and recorded | NIST_CSF/IDENTIFY/ID.RA-03.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |

#### §7.5.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizatio... | NIST_PF/GOVERN-P/GV.RM-P1.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| IDENTIFY-P | ID.IM-P1 | Systems/products/services that process data are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P1.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. | NIST_PF/IDENTIFY-P/ID.RA-P2.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.MA-P1 | Maintenance and repair of organizational assets are performed and logged, with a... | NIST_PF/PROTECT-P/PR.MA-P1.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.6 D-02.2 — Patch Management & Updates

_Applicable regulations: GDPR, CRA_

#### §7.6.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated | NIST_CSF/IDENTIFY/ID.RA-06.json |
| PROTECT | PR.IR-01 | Networks and environments are protected from unauthorized logical access and usa... | NIST_CSF/PROTECT/PR.IR-01.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |

#### §7.6.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.7 D-02.3 — Coordinated Vulnerability Disclosure

_Applicable regulations: CRA_

#### §7.7.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| RESPOND | RS.CO-03 | Information is shared with designated internal and external stakeholders | NIST_CSF/RESPOND/RS.CO-03.json |

#### §7.7.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |

### §6.8 D-03.1 — Identity Lifecycle Management

_Applicable regulations: GDPR, CRA_

#### §7.8.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| PROTECT | PR.AA-02 | Identities are proofed and bound to credentials based on the context of interact... | NIST_CSF/PROTECT/PR.AA-02.json |
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-04 | Identity assertions are protected, conveyed, and verified | NIST_CSF/PROTECT/PR.AA-04.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AA-06 | Physical access to assets is managed, monitored, and enforced commensurate with ... | NIST_CSF/PROTECT/PR.AA-06.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |

#### §7.8.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| PROTECT-P | PR.AC-P3 | Remote access is managed. | NIST_PF/PROTECT-P/PR.AC-P3.json |
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |

### §6.9 D-03.2 — Multi-Factor Authentication

_Applicable regulations: GDPR, CRA_

#### §7.9.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-04 | Identity assertions are protected, conveyed, and verified | NIST_CSF/PROTECT/PR.AA-04.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AA-06 | Physical access to assets is managed, monitored, and enforced commensurate with ... | NIST_CSF/PROTECT/PR.AA-06.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protecte... | NIST_CSF/PROTECT/PR.DS-02.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |

#### §7.9.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| PROTECT-P | PR.AC-P3 | Remote access is managed. | NIST_PF/PROTECT-P/PR.AC-P3.json |
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.10 D-03.3 — Authorisation & Least Privilege

_Applicable regulations: GDPR, CRA_

#### §7.10.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| PROTECT | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are mana... | NIST_CSF/PROTECT/PR.AA-01.json |
| PROTECT | PR.AA-03 | Users, services, and hardware are authenticated | NIST_CSF/PROTECT/PR.AA-03.json |
| PROTECT | PR.AA-04 | Identity assertions are protected, conveyed, and verified | NIST_CSF/PROTECT/PR.AA-04.json |
| PROTECT | PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, ma... | NIST_CSF/PROTECT/PR.AA-05.json |
| PROTECT | PR.AA-06 | Physical access to assets is managed, monitored, and enforced commensurate with ... | NIST_CSF/PROTECT/PR.AA-06.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |

#### §7.10.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited f... | NIST_PF/PROTECT-P/PR.AC-P1.json |
| PROTECT-P | PR.AC-P3 | Remote access is managed. | NIST_PF/PROTECT-P/PR.AC-P3.json |
| PROTECT-P | PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated ... | NIST_PF/PROTECT-P/PR.AC-P6.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.11 D-03.4 — Secure System Defaults

_Applicable regulations: GDPR, CRA_

#### §7.11.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |

#### §7.11.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.12 D-04.1 — Incident Detection & Triage

_Applicable regulations: GDPR, CRA_

#### §7.12.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |

#### §7.12.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.13 D-04.2 — Incident Containment & Response

_Applicable regulations: GDPR, CRA_

#### §7.13.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| RECOVER | RC.RP-01 | The recovery portion of the incident response plan is executed once initiated fr... | NIST_CSF/RECOVER/RC.RP-01.json |
| RECOVER | RC.RP-03 | The integrity of backups and other restoration assets is verified before using t... | NIST_CSF/RECOVER/RC.RP-03.json |
| RECOVER | RC.RP-04 | Critical mission functions and cybersecurity risk management are considered to e... | NIST_CSF/RECOVER/RC.RP-04.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |
| RESPOND | RS.MI-02 | Incidents are eradicated | NIST_CSF/RESPOND/RS.MI-02.json |

#### §7.13.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| CONTROL-P | CT.DP-P3 | Data are processed to limit the formulation of inferences about individuals’ beh... | NIST_PF/CONTROL-P/CT.DP-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.MA-P1 | Maintenance and repair of organizational assets are performed and logged, with a... | NIST_PF/PROTECT-P/PR.MA-P1.json |
| PROTECT-P | PR.PO-P4 | Policy and regulations regarding the physical operating environment for organiza... | NIST_PF/PROTECT-P/PR.PO-P4.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

#### §7.13.3 NIST AI RMF controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| MANAGE | MANAGE-2.1 | Resources required to manage AI risks are taken into account, along with viable ... | NIST_AI_RMF/MANAGE/MANAGE-2.1.json |
| MANAGE | MANAGE-2.3 | Procedures are followed to respond to and recover from a previously unknown risk... | NIST_AI_RMF/MANAGE/MANAGE-2.3.json |

### §6.14 D-04.3 — Incident Notification & Reporting

_Applicable regulations: GDPR, CRA_

#### §7.14.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| RESPOND | RS.AN-03 | Analysis is performed to establish what has taken place during an incident and t... | NIST_CSF/RESPOND/RS.AN-03.json |
| RESPOND | RS.AN-07 | Incident data and metadata are collected, and their integrity and provenance are... | NIST_CSF/RESPOND/RS.AN-07.json |
| RESPOND | RS.CO-02 | Internal and external stakeholders are notified of incidents | NIST_CSF/RESPOND/RS.CO-02.json |
| RESPOND | RS.MA-01 | The incident response plan is executed in coordination with relevant third parti... | NIST_CSF/RESPOND/RS.MA-01.json |
| RESPOND | RS.MA-02 | Incident reports are triaged and validated | NIST_CSF/RESPOND/RS.MA-02.json |
| RESPOND | RS.MA-03 | Incidents are categorized and prioritized | NIST_CSF/RESPOND/RS.MA-03.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |

#### §7.14.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DM-P3 | Data elements can be accessed for alteration. | NIST_PF/CONTROL-P/CT.DM-P3.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |

### §6.15 D-04.4 — Incident Recovery & Lessons Learned

_Applicable regulations: GDPR, CRA_

#### §7.15.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adve... | NIST_CSF/PROTECT/PR.IR-03.json |
| PROTECT | PR.IR-04 | Adequate resource capacity to ensure availability is maintained | NIST_CSF/PROTECT/PR.IR-04.json |
| RECOVER | RC.RP-01 | The recovery portion of the incident response plan is executed once initiated fr... | NIST_CSF/RECOVER/RC.RP-01.json |
| RECOVER | RC.RP-03 | The integrity of backups and other restoration assets is verified before using t... | NIST_CSF/RECOVER/RC.RP-03.json |
| RECOVER | RC.RP-04 | Critical mission functions and cybersecurity risk management are considered to e... | NIST_CSF/RECOVER/RC.RP-04.json |

#### §7.15.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P3 | Data are processed to limit the formulation of inferences about individuals’ beh... | NIST_PF/CONTROL-P/CT.DP-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P4 | Policy and regulations regarding the physical operating environment for organiza... | NIST_PF/PROTECT-P/PR.PO-P4.json |
| PROTECT-P | PR.PT-P1 | Removable media is protected and its use restricted according to policy. | NIST_PF/PROTECT-P/PR.PT-P1.json |
| PROTECT-P | PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to p... | NIST_PF/PROTECT-P/PR.PT-P2.json |

### §6.16 D-05.1 — Data Minimisation

_Applicable regulations: GDPR, CRA_

#### §7.16.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| PROTECT | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | NIST_CSF/PROTECT/PR.DS-01.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §7.16.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.17 D-05.2 — Retention & Archiving

_Applicable regulations: GDPR, CRA_

#### §7.17.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.AM-03 | Representations of the organization's authorized network communication and inter... | NIST_CSF/IDENTIFY/ID.AM-03.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |

#### §7.17.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.18 D-05.3 — Right to Erasure

_Applicable regulations: GDPR, CRA_

#### §7.18.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |

#### §7.18.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |

### §6.19 D-05.4 — Data Portability

_Applicable regulations: GDPR_

#### §7.19.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.DS-10 | The confidentiality, integrity, and availability of data-in-use are protected | NIST_CSF/PROTECT/PR.DS-10.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |

#### §7.19.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |

### §6.20 D-06.1 — Vendor Risk Assessment

_Applicable regulations: GDPR, CRA_

#### §7.20.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.AM-04 | Inventories of services provided by suppliers are maintained | NIST_CSF/IDENTIFY/ID.AM-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |

#### §7.20.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |

### §6.21 D-06.2 — Software Bill of Materials (SBOM)

_Applicable regulations: CRA_

#### §7.21.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |

#### §7.21.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |

### §6.22 D-06.3 — Contractual Security Obligations

_Applicable regulations: GDPR, CRA_

#### §7.22.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.CM-06 | External service provider activities and services are monitored to find potentia... | NIST_CSF/DETECT/DE.CM-06.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.SC-02 | Cybersecurity roles and responsibilities for suppliers, customers, and partners ... | NIST_CSF/GOVERN/GV.SC-02.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.AM-04 | Inventories of services provided by suppliers are maintained | NIST_CSF/IDENTIFY/ID.AM-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-02 | Cyber threat intelligence is received from information sharing forums and source... | NIST_CSF/IDENTIFY/ID.RA-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |
| RESPOND | RS.MA-04 | Incidents are escalated or elevated as needed | NIST_CSF/RESPOND/RS.MA-04.json |
| RESPOND | RS.MI-01 | Incidents are contained | NIST_CSF/RESPOND/RS.MI-01.json |

#### §7.22.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| CONTROL-P | CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organ... | NIST_PF/CONTROL-P/CT.PO-P1.json |
| GOVERN-P | GV.AT-P2 | Senior executives understand their roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P2.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.MA-P1 | Maintenance and repair of organizational assets are performed and logged, with a... | NIST_PF/PROTECT-P/PR.MA-P1.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.23 D-07.1 — Secure-by-Design Principles

_Applicable regulations: GDPR, CRA_

#### §7.23.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §7.23.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.24 D-07.2 — Secure Coding Practices

_Applicable regulations: CRA_

#### §7.24.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §7.24.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.25 D-07.3 — CI/CD Pipeline Security

_Applicable regulations: CRA_

#### §7.25.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §7.25.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.26 D-07.4 — Change Management

_Applicable regulations: CRA_

#### §7.26.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted to ensure co... | NIST_CSF/GOVERN/GV.OV-02.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |
| PROTECT | PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk | NIST_CSF/PROTECT/PR.PS-02.json |
| PROTECT | PR.PS-06 | Secure software development practices are integrated, and their performance is m... | NIST_CSF/PROTECT/PR.PS-06.json |

#### §7.26.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.IM-P1 | Systems/products/services that process data are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P1.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.27 D-08.1 — General Security Awareness

_Applicable regulations: GDPR, CRA_

#### §7.27.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |

#### §7.27.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.28 D-08.2 — Role-Specific Competence

_Applicable regulations: GDPR, CRA_

#### §7.28.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.RR-01 | Organizational leadership is responsible and accountable for cybersecurity risk ... | NIST_CSF/GOVERN/GV.RR-01.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.RR-04 | Cybersecurity is included in human resources practices | NIST_CSF/GOVERN/GV.RR-04.json |
| GOVERN | GV.SC-03 | Cybersecurity supply chain risk management is integrated into cybersecurity and ... | NIST_CSF/GOVERN/GV.SC-03.json |
| PROTECT | PR.AT-01 | Personnel are provided with awareness and training so that they possess the know... | NIST_CSF/PROTECT/PR.AT-01.json |
| PROTECT | PR.AT-02 | Individuals in specialized roles are provided with awareness and training so tha... | NIST_CSF/PROTECT/PR.AT-02.json |

#### §7.28.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. | NIST_PF/GOVERN-P/GV.AT-P1.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |

### §6.29 D-09.1 — Information Security Policies

_Applicable regulations: GDPR, CRA_

#### §7.29.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.OC-04 | Critical objectives, capabilities, and services that external stakeholders depen... | NIST_CSF/GOVERN/GV.OC-04.json |
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| GOVERN | GV.RM-01 | Risk management objectives are established and agreed to by organizational stake... | NIST_CSF/GOVERN/GV.RM-01.json |
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |
| GOVERN | GV.RM-05 | Lines of communication across the organization are established for cybersecurity... | NIST_CSF/GOVERN/GV.RM-05.json |
| GOVERN | GV.RR-01 | Organizational leadership is responsible and accountable for cybersecurity risk ... | NIST_CSF/GOVERN/GV.RR-01.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| GOVERN | GV.RR-03 | Adequate resources are allocated commensurate with the cybersecurity risk strate... | NIST_CSF/GOVERN/GV.RR-03.json |
| GOVERN | GV.SC-01 | A cybersecurity supply chain risk management program, strategy, objectives, poli... | NIST_CSF/GOVERN/GV.SC-01.json |
| GOVERN | GV.SC-04 | Suppliers are known and prioritized by criticality | NIST_CSF/GOVERN/GV.SC-04.json |

#### §7.29.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P4 | System or device configurations permit selective collection or disclosure of dat... | NIST_PF/CONTROL-P/CT.DP-P4.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| GOVERN-P | GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizatio... | NIST_PF/GOVERN-P/GV.RM-P1.json |
| IDENTIFY-P | ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. | NIST_PF/IDENTIFY-P/ID.RA-P2.json |

### §6.30 D-09.2 — Impact & Risk Assessments

_Applicable regulations: GDPR, CRA_

#### §7.30.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjus... | NIST_CSF/GOVERN/GV.OV-01.json |
| GOVERN | GV.RM-04 | Strategic direction that describes appropriate risk response options is establis... | NIST_CSF/GOVERN/GV.RM-04.json |
| GOVERN | GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk managemen... | NIST_CSF/GOVERN/GV.RR-02.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| GOVERN | GV.SC-07 | The risks posed by a supplier, their products and services, and other third part... | NIST_CSF/GOVERN/GV.SC-07.json |

#### §7.30.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| CONTROL-P | CT.DP-P1 | Data are processed to limit observability and linkability (e.g., data actions ta... | NIST_PF/CONTROL-P/CT.DP-P1.json |
| CONTROL-P | CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identifi... | NIST_PF/CONTROL-P/CT.DP-P2.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| GOVERN-P | GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood... | NIST_PF/GOVERN-P/GV.PO-P5.json |
| GOVERN-P | GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizatio... | NIST_PF/GOVERN-P/GV.RM-P1.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. | NIST_PF/IDENTIFY-P/ID.RA-P2.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |

### §6.31 D-09.3 — Asset Inventories

_Applicable regulations: CRA_

#### §7.31.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY | ID.AM-01 | Inventories of hardware managed by the organization are maintained | NIST_CSF/IDENTIFY/ID.AM-01.json |
| IDENTIFY | ID.AM-02 | Inventories of software, services, and systems managed by the organization are m... | NIST_CSF/IDENTIFY/ID.AM-02.json |
| IDENTIFY | ID.AM-05 | Assets are prioritized based on classification, criticality, resources, and impa... | NIST_CSF/IDENTIFY/ID.AM-05.json |
| PROTECT | PR.PS-01 | Configuration management practices are established and applied | NIST_CSF/PROTECT/PR.PS-01.json |

#### §7.31.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.32 D-09.4 — Records of Processing

_Applicable regulations: GDPR, CRA_

#### §7.32.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |

#### §7.32.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures ar... | NIST_PF/IDENTIFY-P/ID.DE-P1.json |
| IDENTIFY-P | ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners,... | NIST_PF/IDENTIFY-P/ID.DE-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |

### §6.33 D-10.1 — Continuous Security Monitoring

_Applicable regulations: GDPR, CRA_

#### §7.33.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| IDENTIFY | ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are... | NIST_CSF/IDENTIFY/ID.IM-04.json |
| IDENTIFY | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | NIST_CSF/IDENTIFY/ID.RA-01.json |
| IDENTIFY | ID.RA-03 | Internal and external threats to the organization are identified and recorded | NIST_CSF/IDENTIFY/ID.RA-03.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |

#### §7.33.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| IDENTIFY-P | ID.IM-P1 | Systems/products/services that process data are inventoried. | NIST_PF/IDENTIFY-P/ID.IM-P1.json |
| IDENTIFY-P | ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service pro... | NIST_PF/IDENTIFY-P/ID.IM-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.34 D-10.2 — Audit Logging & Traceability

_Applicable regulations: GDPR, CRA_

#### §7.34.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.AE-03 | Information is correlated from multiple sources | NIST_CSF/DETECT/DE.AE-03.json |
| DETECT | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | NIST_CSF/DETECT/DE.CM-01.json |
| DETECT | DE.CM-09 | Computing hardware and software, runtime environments, and their data are monito... | NIST_CSF/DETECT/DE.CM-09.json |
| GOVERN | GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity - includ... | NIST_CSF/GOVERN/GV.OC-03.json |
| GOVERN | GV.PO-01 | Policy for managing cybersecurity risks is established based on organizational c... | NIST_CSF/GOVERN/GV.PO-01.json |
| GOVERN | GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and ... | NIST_CSF/GOVERN/GV.PO-02.json |
| IDENTIFY | ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are iden... | NIST_CSF/IDENTIFY/ID.RA-04.json |
| PROTECT | PR.DS-11 | Backups of data are created, protected, maintained, and tested | NIST_CSF/PROTECT/PR.DS-11.json |
| IDENTIFY | ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their lif... | NIST_CSF/IDENTIFY/ID.AM-08.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |
| RECOVER | RC.RP-03 | The integrity of backups and other restoration assets is verified before using t... | NIST_CSF/RECOVER/RC.RP-03.json |

#### §7.34.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data pr... | NIST_PF/COMMUNICATE-P/CM.AW-P1.json |
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| COMMUNICATE-P | CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processi... | NIST_PF/COMMUNICATE-P/CM.PO-P1.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| CONTROL-P | CT.DP-P3 | Data are processed to limit the formulation of inferences about individuals’ beh... | NIST_PF/CONTROL-P/CT.DP-P3.json |
| GOVERN-P | GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing ... | NIST_PF/GOVERN-P/GV.PO-P1.json |
| GOVERN-P | GV.PO-P2 | Processes to instill organizational privacy values within system/product/service... | NIST_PF/GOVERN-P/GV.PO-P2.json |
| GOVERN-P | GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to pri... | NIST_PF/GOVERN-P/GV.PO-P3.json |
| GOVERN-P | GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party ... | NIST_PF/GOVERN-P/GV.PO-P4.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.DS-P1 | Data-at-rest are protected | NIST_PF/PROTECT-P/PR.DS-P1.json |
| PROTECT-P | PR.DS-P2 | Data-in-transit are protected. | NIST_PF/PROTECT-P/PR.DS-P2.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |
| PROTECT-P | PR.PO-P4 | Policy and regulations regarding the physical operating environment for organiza... | NIST_PF/PROTECT-P/PR.PO-P4.json |

### §6.35 D-10.3 — Compliance Testing

_Applicable regulations: GDPR, CRA_

#### §7.35.1 NIST CSF 2.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| DETECT | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activiti... | NIST_CSF/DETECT/DE.AE-02.json |
| GOVERN | GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and review... | NIST_CSF/GOVERN/GV.OV-03.json |
| IDENTIFY | ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inhere... | NIST_CSF/IDENTIFY/ID.RA-05.json |
| IDENTIFY | ID.IM-03 | Improvements are identified from execution of operational processes, procedures,... | NIST_CSF/IDENTIFY/ID.IM-03.json |
| PROTECT | PR.PS-04 | Log records are generated and made available for continuous monitoring | NIST_CSF/PROTECT/PR.PS-04.json |

#### §7.35.2 NIST PF 1.0 controls

| Function | Control ID | Description (1-liner) | Path |
|---|---|---|---|
| COMMUNICATE-P | CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus group... | NIST_PF/COMMUNICATE-P/CM.AW-P2.json |
| CONTROL-P | CT.DM-P1 | Data elements can be accessed for review | NIST_PF/CONTROL-P/CT.DM-P1.json |
| GOVERN-P | GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including t... | NIST_PF/GOVERN-P/GV.MT-P1.json |
| GOVERN-P | GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communic... | NIST_PF/GOVERN-P/GV.MT-P2.json |
| IDENTIFY-P | ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions... | NIST_PF/IDENTIFY-P/ID.RA-P1.json |
| IDENTIFY-P | ID.RA-P3 | Potential problematic data actions and associated problems are identified. | NIST_PF/IDENTIFY-P/ID.RA-P3.json |
| PROTECT-P | PR.PO-P1 | A baseline configuration of information technology is created and maintained inc... | NIST_PF/PROTECT-P/PR.PO-P1.json |
| PROTECT-P | PR.PO-P3 | Backups of information are conducted, maintained, and tested. | NIST_PF/PROTECT-P/PR.PO-P3.json |

### §6.36 Provenance

- **Source files:** `00_METHODOLOGY/PREPROCESSING_by_domain/Things/*.xlsx` (NIST CSF 2.0 Implementation Examples, NIST PF 1.0 Core, NIST AI RMF Playbook) + `00_METHODOLOGY/PREPROCESSING_by_domain/_global/*.md` (NIST CSF 2.0 subcategories reference) + sub-domain corpora at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_*/D-XX.X/D-XX.X.json`
- **Mapping date:** 2026-08-14
- **Coverage scope:** 35 ACTIVE sub-domains (D-01.1..D-10.3 minus D-02.4, D-06.4, D-08.3 NOT_ADDRESSED). 3 NOT_ADDRESSED sub-domains excluded per Doc 07 §3.
- **Controls total:** ~300 NIST CSF 2.0 + ~200 NIST PF 1.0 across 35 sub-domains (see §7 cross-references).
- **Pilot date (D-01.1 only):** 2026-08-13 — full coverage achieved 2026-08-14.

### §6.37 Cross-references

- `by_subdomain/<D-XX.X>.json` — 35 aggregated mappings separated by framework (CSF + PF + AI RMF where applicable)
- per-control JSONs: `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/<framework>/<function>/<control_id>.json`
- per-subdomain corpus: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_*/D-XX.X/` (source-of-truth for control derivation)

---

---

## §7 Cross-References

- **Appendix A**: All 74 detail cards preserved verbatim for Phase 2 traceability — `11_Rules_Catalog.md` and `12_Rules_Catalog.xlsx` reference these IDs in their "Related Goals" column. The §A.0 alias table maps every legacy PG/SG ID to its AG equivalent.
- **Doc 04 §4 BG-01..BG-05**: Business Goals → Adjusted Goals traceability. Each BG cell carries the AG ID directly plus the §2 / §3 / §4 column reference: BG-01 → §2 + §3; BG-02 → §2 + §4; BG-03 → §3 D-05.3 (`AG-D-05.3-001`) + D-05.4 (`AG-D-05.4-001`); BG-04 → §3 D-02.1 (`AG-D-02.1-001`) + §4 D-02.1 (`AG-D-02.1-002`) + D-07.x; BG-05 → §3 D-06.1 (`AG-D-06.1-001`) + §3 D-06.1 (`AG-D-06.1-002`) + §4 T-002. Both AG IDs and Appendix A.A.0 alias are listed.
- **Doc 07 Sub-Domain Coverage Matrix (§3)**: Source of the 35 ACTIVE / 3 NOT_ADDRESSED split used in §2-§4.
- **Doc 07b Proportionality Profile**: 5-attribute per-sub-domain operationalisation (`satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`).
- **Doc 05b Ambiguity Register**: 417 ambiguity cards (R1/R2/R3 variant readings) — informs disambiguation of the corpus Baseline Goals restated in §3.
- **Phase 2 `10_Privacy_Security_Goals.md`**: original PG/SG formulation — resolved by this document (§3-§4).
- **Phase 2 `09_Strategic_Tensions_Report.md` (legacy)**: Original tensions list (T-001..T-004) — same IDs preserved here, now resolved with max-SLA routing in §4.
- **`00_METHODOLOGY/REFERENCE/proportionality_model.md` §1, §5, §6**: Invariant + decision table + tier attribute definitions (cited throughout).
- **`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/`**: Corpus source for the Baseline Goals (`SO-D-XX.Y.HL` + `SO-D-XX.Y.<REG>`, consumed by reference) and for the restated goals in §3.

---

## §8 Validation

- **35 ACTIVE sub-domains × 3 columns** (high-level + GDPR-driven + CRA-driven) = **105 cells** in §2-§4, of which **8 are N/A** (7 GDPR: D-02.2, D-02.3, D-06.2, D-07.2, D-07.3, D-07.4, D-09.3; 1 CRA: D-05.4) → **97 populated adjusted goals**.
- **AG IDs in §3**: 35 entries in §2 (slot 001) + 28 in §3 (slot 001) + 34 in §4 (slot 002) = **97 AG entries**, with **8 carrying `—` for N/A cells** (7 GDPR + 1 CRA). Distinct AG IDs used in main tables: **35 slot 001 (HL/GDPR-driven, one per ACTIVE sub) + 34 slot 002 (CRA-driven) = 69 distinct IDs**.
- **74 AG IDs preserved in Appendix A**: every legacy PG/SG ID referenced by Phase 2 deliverables resolves via the §A.0 alias table.
- **§A.0 alias table columns**: legacy ID → AG ID → regulation → sub-domain → notes.
- **§2 / §3 / §4 / §5 are technology-free** — no vendor, product, or tool named (verified by blocklist scan and by inspection).
- **Baseline Goal wording inherited from the corpus unchanged.** Any technology tokens (`CI/CD`, `SBOM`, and similar) in that wording come from the frozen Phase 0 Baseline Goal prose and are retained as inherited corpus wording (ADR-004 D2 — frozen artifact content). Technology-neutrality applies to the Adjusted Goals layer (§3), not to the inherited Baseline Goal wording.
- **Track B decision table: 37 rows** in §5 (35 ACTIVE + D-02.4 + D-06.4). D-08.3 is NOT_ADDRESSED and was never tiered.
- **Distribution (37 tiered rows): 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37** (matches Doc 07b §3 + §4 verbatim). Restricted to the 35 ACTIVE rows of §2-§4: **31 LIGHTWEIGHT + 4 MINIMAL**, all MUST.
- **4 tensions resolved** with max-SLA routing in §4 (T-001..T-004, IDs preserved from legacy Phase 2 + `phase1_ontology.yaml`).
- Floor rule preserved: every MUST ≥ MINIMAL per `proportionality_model.md §5.3`.
- Lints: see `validation/SPRINT4_REPORT.md` — legacy PG/SG/CR/BPR IDs lint as warnings; AG IDs lint as PASS.
- `validate_aegis_ids.py --quiet` passes — all 74 distinct AG IDs cross-reference validly. Document Structure reports a pre-existing heading-pattern failure on §0/§9, unrelated to the goals tables.

---

## §9 Version History
| 5.1 | 2026-09-22 | aegis-mvp executor (designation harmonization) | **Phase 1 designation = Goals: the "AO" label is retired.** All prose "AO" references -> "AG" (ID values were already `AG-D-XX.X-NNN`; no ID changed). Headings, column headers, frontmatter keys (`ao_*` -> `ag_*`), title and this file name updated (`Doc06_Adjusted_Goals.md`). Legacy PG/SG aliases and Appendix A cards preserved verbatim. |

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Fase de Especificação 4 Executor | Initial release — 74 adjusted goals (37 PG + 37 SG) + 4 tensions resolved + 37-row Track B decision trail |
| 2.0 | 2026-08-06 | Fase de Especificação 5 Executor | Deep enrichment — 74 detail cards (12 fields each: Description, Scope, Out of scope, Source Article, Corpus path, NIST CSF Anchors, Verification Criteria, Verification Method, Owner, Status, Dependencies, Risk, Affected Stakeholders, Implementation Posture, Implementation Priority). 4 tensions expanded to multi-paragraph root cause analysis + source citations + resolution options + implementation + verification. **NO Effort/Cost/Timeline fields added** per Fase de Especificação 5 scope. Tables enriched with "See full details" anchor column. **Superseded by v3.0** — the tech-rich §2/§2a/§3/§3a of this version are preserved verbatim in Appendix A. |
| 3.0 | 2026-08-10 | Executor | Phase 1 tech-free restructure. New §2/§3/§4 (high-level + GDPR-driven + CRA-driven, 35 rows × 3 columns, hybrid format) derived from the regulatory corpus. 4 tensions rewritten without technology references (§5). 74 PG/SG detail cards preserved in Appendix A (DEPRECATED). 6 critical IDs (`PG-D-01.3-001`, `SG-D-04.3-001`, `PG`/`SG-D-09.1-001`, `PG`/`SG-D-09.2-001`) retained in the main flow with inline notes. Scope corrected to 35 ACTIVE sub-domains per Doc 07 §3 (D-02.4 / D-06.4 / D-08.3 NOT_ADDRESSED). |
| 4.0 | 2026-08-10 | Fase de Especificação 8 Executor | **AG ID migration.** 74 PG/SG IDs → 74 AG IDs (`PG-D-XX.X-001` → `AG-D-XX.X-001`; `SG-D-XX.X-001` → `AG-D-XX.X-002`). §1 docstring updated. 6 critical IDs in §3/§4 inline notes carry `formerly_known_as` aliases. §5 tension anchors updated. §8 cross-references to Doc 04 BG-03/BG-04 carry AG aliases. §9 validation rewritten for AG counts. Appendix A header note + DEPRECATED alias table (74 rows) added; the 74 detail cards preserved verbatim. Phase 2 lints (`lint_10_pso_rules`, `lint_11_rules_catalog`) updated to accept legacy PG/SG/CR/BPR IDs as DEPRECATED warnings during the transition window. Tech-free invariant preserved. |
| 5.0 | 2026-08-10 | Fase de Especificação 9 Executor | **Canonical AG IDs in §2/§3/§4 tables.** §2 HL (35 rows) and §3 GDPR-driven (35 rows, 7 N/A) now carry an `AG ID` column with `AG-D-XX.X-001` (slot 001, regulation-agnostic HL or GDPR-driven); §4 CRA-driven (35 rows, 1 N/A) carries `AG-D-XX.X-002` (slot 002, CRA-driven). Total: 35 + 28 + 34 = 97 AG entries in the main tables (69 distinct IDs in §2/§3/§4; 74 total in document including Appendix A.NOT_ADDRESSED subs D-02.4 / D-06.4). Appendix A.A.0 alias table expanded with `Regulation` and `Sub-domain` columns (74 rows × 5 columns, self-contained lookup). §1 + §8 + §9 rewritten for v5.0 AG ID counts (note: section numbers shifted in v6.0 with §7 now NIST Controls Mapping). Doc 04 §4 BG-01..BG-05 cells updated to reference §2/§3/§4 by AG ID. Frontmatter: `version: 5.0`, `id_format: AG-D-XX.X-NNN`, `ao_canonical_ids_count: 35`. `validate_aegis_ids.py --quiet` PASS; Phase 1/2/3 lint gates PASS. |
| 7.0 | 2026-09-22 | aegis-mvp executor (structure per ADR-003 D1 + ADR-004) | **Consolidated goals table.** Former §2 high-level table eliminated (duplicate of the regulation-driven slots); former §3+§4 merged into one §3 table grouped by sub-domain, one row per goal, with the ADR-003 D1 columns (Pattern, Property, Parent goal — draft values, P7) plus Reg. New §2 Framing (size, area, roles, inherited capabilities) absorbs the generic scale/hosting adjustments; goal-specific adjustments stay inline. Sections renumbered (former §5-§10 → §4-§9). Tier/Priority remain in §5 Track B. |
| 6.0 | 2026-08-13 | Fase de Especificação 10 Executor | **NIST Controls Layer pilot (D-01.1).** New §7 NIST Controls Mapping added before Appendix A. CONTROLS/ restructured by framework→function (NIST_CSF/<function>/, NIST_PF/<function>-P/, NIST_AI_RMF/<function>/) + by_subdomain/. §7..§10 renumbered to §8..§11. D-01 detail cards (8) extracted from Appendix A to `_deprecated/07c_Appendix_A_D01_OLD.md`; Appendix A now retains D-02..D-10 (66 cards, LEGACY). Frontmatter: `version: 6.0`, `tech_free_sections` adds §7, `appendix_a_status: PARTIAL_LEGACY`, `appendix_a_cards_count: 66`, `appendix_a_migrated_to_deprecated: 8`. Pilot scope: 10 controls (5 CSF + 4 PF + 1 AI RMF) for D-01.1 only. |
| 7.0 | 2026-08-14 | Executor (§3 NIST Controls expansion) | **§7 full coverage expansion.** 35 ACTIVE sub-domains now mapped to NIST CSF 2.0 + NIST PF 1.0 (+ NIST AI RMF where applicable). §7 grew from 1 pilot subsection (D-01.1, 10 controls) to 35 subsections (~300 CSF + ~200 PF controls total). 34 new `by_subdomain/<D-XX.X>.json` files created (D-01.2 through D-10.3, excluding D-02.4/D-06.4/D-08.3 NOT_ADDRESSED). Frontmatter: `version: 7.0`, `nist_controls_full_coverage: true`, `active_subdomains_mapped: 35`. |

---

## §10 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author (Fase de Especificação 7 tech-free restructure) | Fase de Especificação 7 Executor | | 2026-08-10 |
| Document Author (Fase de Especificação 5 deep enrichment) | Fase de Especificação 5 Executor | | 2026-08-06 |
| Document Author (Fase de Especificação 4 base) | Fase de Especificação 4 Executor | | 2026-08-06 |
| Business Review (CEO) | | | |
| Technical Review (CTO) | | | |
| AEGIS Methodology Review | | | |

**Next documents that consume this profile:**
- Phase 2 `11_Rules_Catalog.md` (rules consume the adjusted goals in §2-§4; legacy PG/SG IDs preserved in `_deprecated/07c_Appendix_A_OLD.md` and `_deprecated/07c_Appendix_A_D01_OLD.md` for traceability during the transition window)
- Phase 3 `14_Architectural_Nodes.md` (architecture consumes the tier from §6)


---
