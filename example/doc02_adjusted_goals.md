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
inputs: [Doc01_INTAKE_FORM.md, baseline/domains/, baseline/CONTROLS/, baseline/MAPPINGS/]
outputs: [11_Rules_Catalog.md]
related_documents: [Doc01_INTAKE_FORM.md, baseline/00_Taxonomy_Reference.md, baseline/01_Ambiguity_Registry.md]
cross_checked_against: [Doc01_INTAKE_FORM.md, baseline/00_Taxonomy_Reference.md]
frozen: false
---

# Adjusted Goals per Sub-Domain (Rich Mode)

---

## §0 Document Purpose

This document is the **Phase 1 Adjusted Goals layer** of the TinyTask SaaS case — the Fase 0 → Fase 1 exchange of the pipeline I/O contract (ADR-004): the frozen corpus **Baseline Goals** (high-level goal `SG-D-XX.Y.HL` + per-regulation baseline goals) restated against one company. It binds every ACTIVE sub-domain to:

1. A **regulatory floor** — the corpus Baseline Goals, consumed by reference.
2. A **framing** — the company context that conditions every goal: size/tier, area of operation, regulatory roles, inherited capabilities (§2).
3. **Adjusted Goals** — one D1 card per goal (ADR-003): company-proportional, regulation-anchored, slot 001 GDPR / slot 002 CRA (§3).
4. **Resolutions** for the 4 strategic tensions (T-001..T-004), in §4.
5. A **Track B tier** per sub-domain, in §5.
6. The **NIST controls mapping** per sub-domain, in §6.

## §1 Regulatory Floor (corpus, by reference)

The baseline floor for goals is consumed by reference from `baseline/domains/` and `baseline/MAPPINGS/traceability/` per rule R9.

## §2 Framing (TinyTask SaaS)

| Dimension | Framing |
|---|---|
| Size | 8-person team, MICRO scale — tiers LIGHTWEIGHT/MINIMAL. Consequences: security-awareness training runs as a single documented cycle (D-08.1); custodian/consumer key-role separation is achieved at the platform-role level, not by disjoint individuals (D-01.3); recovery evidence collapses to a single dual-purpose artefact for both regulators (D-04.4). |
| Area of operation | B2B SaaS appointment platform for psychology clinics (EU-domiciled, Portugal); processes personal data of patients and clinic staff on a continuous, non-occasional basis. |
| Regulatory roles | Data controller (GDPR) and manufacturer of a product with digital elements (CRA); the company distributes its own product and occupies neither the importer nor the distributor role. |
| Inherited capabilities | Supplier-managed hosting: at-rest encryption capability and key custody are inherited from a supplier-managed layer rather than operated in-house (D-01.1, D-01.3). |

## §3 Adjusted Goals

### §3.0 Structure and Interpretation Guide

Each active sub-domain presents:
1. **High-Level Security Goal (`SG-D-XX.Y.HL`):** The common, regulation-neutral baseline objective inherited from the methodology corpus (`baseline/domains/`).
2. **Regulation baseline (`SG-D-XX.Y.<REG>`):** Each confirmed regulation's Sub-SO objective, verbatim from the corpus module — the regulatory floor the adjusted goal restates.
3. **Regulation-specific Adjusted Goals:** Company-proportional restatements for each confirmed applicable regulation (slot 001 for GDPR, slot 002 for CRA).
4. **Adjustment Column (`Adjustment`):**
   - **`—` (Standard Proportionality):** Indicates that the goal follows the overarching company proportionality defined in **§2 Framing** (MICRO scale, 8-person team, supplier-managed hosting layer, B2B SaaS) without requiring sub-domain-specific legal exceptions or procedural deviations.
   - **Explicit Notes (12 goals):** Document specific regulatory boundary conditions, statutory exceptions, or interpretation baselines that apply uniquely to that sub-domain (e.g. inactive special-category data provisions, support period duration floors, conformity self-assessment modules, or direct distribution roles).

---

### D-01.1 — Data at Rest Encryption

**High-Level Security Goal (SG-D-01.1.HL):** Data held at rest in storage is protected against unauthorised access through appropriate technical measures — primarily encryption with appropriate key custody — calibrated to the risks identified in the entity's risk assessment and commensurate with the state of the art.

**Regulation baseline — `SG-D-01.1.GDPR` (GDPR):** Personal data at rest is processed in a manner that ensures appropriate security — including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage — using appropriate technical or organisational measures, with the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (Art. 5(1)(f) + Art. 32(1)(b); the `appropriate` threshold is anchored by the five Art. 32(1) preamble factors — state of the art, costs of implementation, nature, scope, context, purposes, risks).

**Regulation baseline — `SG-D-01.1.CRA` (CRA):** Where a product with digital elements stores data — personal or other — the confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms (Annex I Part I (2)(e)).


| AG ID | Adjusted Goal | Company implication | Pattern | Property | Parent Goal | Baseline source | Regulatory source | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.1-001` | Personal data at rest is processed with appropriate technical or organisational measures, so that it stays protected against unauthorised or unlawful processing and against accidental loss, destruction or damage, and so that the ongoing confidentiality, integrity, availability and resilience of the processing systems and services that carry it can be ensured. At this scale those measures are the ones the hosting supplier puts in place, so the duty TinyTask carries is to hold the supplier to them in the processing agreement rather than to operate them itself. | TinyTask operates no infrastructure of its own, so it holds no at-rest protection capability it can point at; what it must be able to show is a written commitment in the hosting agreement covering the clinic task data, re-checked when that agreement is renewed. | maintain | Confidentiality | `SO-D-01.1.HL` | `SG-D-01.1.GDPR` | GDPR Art. 5(1)(f) + Art. 32(1)(b) | narrowed: the protection is inherited from the hosting supplier rather than operated in-house — because TinyTask runs no infrastructure of its own. |
| `AG-D-01.1-002` | Data stored by the product with digital elements — clinic task data and the account data behind it — has its confidentiality protected by encrypting the relevant stores at rest with mechanisms meeting the state of the art. The company places that product on the market itself, so the guarantee it owes travels with every copy it distributes and not only with the tenants it happens to host. | TinyTask is the party placing the product with digital elements on the market, so it is the one that has to show the encryption floor holds in the product as distributed; the hosting supplier's controls cover the hosted estate, which is a narrower thing than the product obligation. | maintain | Confidentiality | `SO-D-01.1.HL` | `SG-D-01.1.CRA` | CRA Annex I Part I (2)(e) | narrowed: the state-of-the-art floor binds the distributed product, not only the hosted estate — because TinyTask places its own product on the market and occupies neither the importer nor the distributor role. |

### D-01.2 — Data in Transit Encryption

**High-Level Security Goal (SG-D-01.2.HL):** Data in transit — across network paths, inter-service calls, and third-party APIs — is protected against unauthorised disclosure and alteration through cryptographic confidentiality and integrity controls (mutual authentication, encryption, integrity verification).

**Regulation baseline — `SG-D-01.2.GDPR` (GDPR):** Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted) (Art. 32(1)(b) + Art. 32(2)).

**Regulation baseline — `SG-D-01.2.CRA` (CRA):** Where data is transmitted by a product with digital elements — personal or other — the confidentiality of the data in transit is protected by encrypting relevant data using state-of-the-art mechanisms, with the Annex I (2)(j) attack-surface-limitation leg constraining the exposed interfaces through which the data could otherwise leak (Annex I Part I (2)(e) + (2)(j)).


| AG ID | Adjusted Goal | Company implication | Pattern | Property | Parent Goal | Baseline source | Regulatory source | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.2-001` | Personal data transmitted across networks, inter-service channels and third-party infrastructure remains confidential and unaltered while in transit, and the protection put on that path is chosen against the five-event Art. 32(2) enumeration — accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data so transmitted. Between a clinic user and the platform the path TinyTask controls ends at the hosting supplier's boundary, so the enumeration has to be answered on both sides of that boundary. | Clinic staff reach the platform over links TinyTask does not own, so the in-transit duty is met partly by the hosting supplier's transport protection and partly by what the platform does on its own edge; the risk enumeration has to be answered for the clinic link, not asserted once for the whole service. | maintain | Confidentiality | `SO-D-01.2.HL` | `SG-D-01.2.GDPR` | GDPR Art. 32(1)(b) + Art. 32(2) | narrowed: the duty is answered on both sides of the hosting boundary — because clinic users connect to a platform TinyTask operates on infrastructure it does not. |
| `AG-D-01.2-002` | Data transmitted by the product with digital elements — personal or other — has its confidentiality in transit protected by encrypting what travels using state-of-the-art mechanisms, and the interfaces through which that data could otherwise leave are kept to the ones the product actually needs. TinyTask builds and distributes the product itself, so that guarantee is owed by the product wherever it is deployed, independently of any transport protection the deployment happens to add. | As the manufacturer of the product with digital elements, TinyTask is what owes the transmission guarantee to every clinic that installs it; a hosting supplier's transport protection covers the deployment it provides and says nothing about copies running elsewhere. | maintain | Confidentiality | `SO-D-01.2.HL` | `SG-D-01.2.CRA` | CRA Annex I Part I (2)(e) + (2)(j) | narrowed: the transmission guarantee is owed by the product wherever it is deployed — because TinyTask distributes its own product rather than only operating a hosted service. |

### D-01.3 — Key Management

**High-Level Security Goal (SG-D-01.3.HL):** Cryptographic keys and related authentication material are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it; the key custodian and the data consumer are distinct roles under distinct technical and organisational control, with the cryptographic key (not the storage medium) as the necessary condition for intelligibility of the protected data.

**Regulation baseline — `SG-D-01.3.GDPR` (GDPR):** Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject (the cryptographic key, the mapping table, or the tokenisation seed) is kept separately and is subject to appropriate technical and organisational measures that prevent attribution (Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility carve-out + Art. 32(1)(a) pseudonymisation/ encryption anchor).

**Regulation baseline — `SG-D-01.3.CRA` (CRA):** Cryptographic keys and related authentication material used to protect the confidentiality and integrity of stored, transmitted or otherwise processed data by a product with digital elements — personal or other — are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it (Annex I Part I (2)(d) access-control + (2)(e) "other technical means" reading per `SR-CRA-004` ambiguity_notes; the Annex I text does not mention key management explicitly — the synthesis catalogue `99_CRA_Synthesis.md` §4 flags this as a T2-vs-text gap — so the key-separation reading rests on the combination of Annex I (2)(d) access-control duty with the Annex I (2)(e) "other technical means" residual).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.3-001` | Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject — the key, the mapping table, or the tokenisation seed — is kept separately and is subject to appropriate technical and organisational measures that prevent attribution. | maintain | Confidentiality | SG-D-01.3.HL | GDPR | Art. 4(5) + Art. 34(3)(a) + Art. 32(1)(a) | PR.DS-01, PR.IR-03 | — |
| `AG-D-01.3-002` | Cryptographic keys and related authentication material used to protect the confidentiality and integrity of data stored, transmitted or otherwise processed by the product are managed with separation of roles, so that possession of the key material is not bundled with possession of the operational environment that uses it. | maintain | Confidentiality | SG-D-01.3.HL | CRA | Annex I Part I (2)(d) + (2)(e) | PR.DS-01, PR.AA-05, GV.OV-01 | The Annex I text does not mention key management explicitly; the key-separation reading rests on combining the access-control duty with the `other technical means` residual, flagged as a text-versus-interpretation gap in the corpus synthesis catalogue. |

### D-01.4 — Data Integrity

**High-Level Security Goal (SG-D-01.4.HL):** Data integrity is preserved against unauthorised modification across the data lifecycle — at rest, in transit, and in use — with corruption detected, logged, and reported, and with semantic accuracy maintained as the workflow leg of the personal-data principle.

**Regulation baseline — `SG-D-01.4.GDPR` (GDPR):** Personal data are accurate and, where necessary, kept up to date; every reasonable step is taken to ensure that personal data that are inaccurate are erased or rectified without delay (Art. 5(1)(d) accuracy principle), with the integrity property anchored to two further legs — storage integrity (Art. 5(1)(f)) and the Art. 16 rectification cascade with Art. 19 recipient-cascade duty.

**Regulation baseline — `SG-D-01.4.CRA` (CRA):** The integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, is protected against any manipulation or modification not authorised by the user (Annex I Part I (2)(f) — the universal-quantifier `any` makes the integrity protection unconditional); corruption is reported to the user / administering party (Annex I Part I (2)(f) `report on corruptions` + (2)(l) logging + monitoring).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-01.4-001` | Personal data are accurate and, where necessary, kept up to date, and inaccurate data are erased or rectified without delay, with the integrity property anchored to two further legs — storage integrity and the rectification cascade carrying the Art. 19 recipient-notification duty. | maintain | Integrity | SG-D-01.4.HL | GDPR | Art. 5(1)(d) + Art. 5(1)(f) + Art. 16 + Art. 19 | PR.DS-01, PR.DS-10, PR.DS-10 | — |
| `AG-D-01.4-002` | The integrity of stored, transmitted, or otherwise processed data — as well as the integrity of commands, programs, and configuration — is protected against any manipulation or modification not authorised by the user, and corruption is reported to the user or administering party. | maintain | Integrity | SG-D-01.4.HL | CRA | Annex I Part I (2)(f) + (2)(l) | PR.DS-01, PR.DS-10, PR.PS-04 | The universal quantifier `any` makes this integrity protection unconditional — it admits no risk-based relaxation at MICRO scale. |

### D-02.1 — Vulnerability Identification

**High-Level Security Goal (SG-D-02.1.HL):** Vulnerabilities — including, where in scope, AI-system-specific attack surfaces (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) — are identified on a continuing basis across the system, product, ICT asset, or AI system that an entity operates, manufactures, deploys, or processes, with the resulting identification artefact (vulnerability register, risk-scenario catalogue, SBOM, or risk-management file) feeding the entity's testing, remediation, and notification cascades.

**Regulation baseline — `SG-D-02.1.GDPR` (GDPR):** A controller or processor operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures for ensuring the security of the processing (Art. 32(1)(d)); the data-protection impact assessment under Art. 35 is reviewed when there is a change of the risk represented by processing operations (Art. 35(11)).

**Regulation baseline — `SG-D-02.1.CRA` (CRA):** A product with digital elements is made available on the market without known exploitable vulnerabilities (Annex I Part I (2)(a)), and vulnerabilities contained in the product — including the components listed in an SBOM — are identified and documented on a continuing basis throughout the support period (Annex I Part II (1) + Art. 13(3) + Art. 13(7)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.1-001` | The company operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment when the risk represented by processing operations changes. | achieve | Confidentiality | SG-D-02.1.HL | GDPR | Art. 32(1)(d) + Art. 35(11) | ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02 | — |
| `AG-D-02.1-002` | The product is made available on the market without known exploitable vulnerabilities, and vulnerabilities contained in it — including those in the components listed in the software bill of materials — are identified and documented on a continuing basis throughout the support period. | achieve | Confidentiality | SG-D-02.1.HL | CRA | Annex I Part I (2)(a) + Annex I Part II (1) + Art. 13(3) + Art. 13(7) | ID.RA-01, ID.AM-02, PR.PS-02 | — |

### D-02.2 — Patch Management

**High-Level Security Goal (SG-D-02.2.HL):** Vulnerabilities identified in the upstream identification pipeline are addressed and remediated through security updates that are distributed via a secure, separated channel, with the entity-side policy governing patch deployment (severity-classified deployment windows, automated isolation of affected information assets in the event of a cyber-attack) forming a layered patch-management workflow on the asset.

**Regulation baseline — `SG-D-02.2.CRA` (CRA):** Vulnerabilities of a product with digital elements are addressed and remediated through security updates without delay, including — where technically feasible — through security updates provided separately from functionality updates (Annex I Part II (2) + Annex I Part I (2)(c)); security updates are disseminated without delay to users via mechanisms that ensure the secure distribution of updates, accompanied by advisory messages describing the action users can take (Annex I Part II (7) + (8)); vulnerabilities — including those of integrated components — are handled effectively and in accordance with the Annex I Part II vulnerability-handling requirements throughout the support period determined by the manufacturer (minimum 5 years, or the expected use time if shorter — Art. 13(8)); each security update made available during the support period remains available after it has been issued for at least 10 years or for the remainder of the support period, whichever is longer (Art. 13(9)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.2-002` | Vulnerabilities are addressed and remediated through security updates without delay, provided separately from functionality updates where technically feasible, and disseminated to users via mechanisms ensuring secure distribution together with advisory messages describing the action users can take. | achieve | Confidentiality | SG-D-02.2.HL | CRA | Annex I Part II (2) + (7) + (8) + Annex I Part I (2)(c) + Art. 13(8) + Art. 13(9) | PR.PS-02, PR.IR-03, ID.RA-01, PR.PS-01 | Each security update remains available for at least 10 years or the remainder of the support period, whichever is longer — a retention floor that outlasts the company's current planning horizon. |

### D-02.3 — Coordinated Vulnerability Disclosure

**High-Level Security Goal (SG-D-02.3.HL):** A coordinated vulnerability disclosure (CVD) ecosystem is maintained, covering the manufacturer-side CVD policy (intake, triage, publication, post-disclosure verification), a publicly identifiable contact address for vulnerability reporting, and — when the manufacturer also operates as a NIS 2 essential entity in a Member State — the institutional CSIRT-coordinated pathway under Art. 12(1) that integrates the manufacturer-side CVD with the Member-State-level disclosure coordination.

**Regulation baseline — `SG-D-02.3.CRA` (CRA):** The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for its products with digital elements (Annex I Part II (5) + Art. 13(8) sentence 6); once a security update has been made available, the manufacturer shares and publicly discloses information about the fixed vulnerabilities, including a description of the vulnerability, the affected products, the impacts, the severity, and the remediation guidance — subject to a duly justified delay exception where security risks of publication outweigh security benefits (Annex I Part II (4)); the manufacturer facilitates the sharing of information about potential vulnerabilities in its products and in third-party components contained therein, including by providing a publicly identifiable contact address for the reporting of vulnerabilities (Annex I Part II (6)); the manufacturer designates a single point of contact to enable users — including security researchers — to communicate directly and rapidly with the manufacturer (Art. 13(17) + Annex II §2).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-02.3-002` | The company puts in place, documents and enforces a coordinated vulnerability disclosure policy, publicly discloses information about fixed vulnerabilities once an update is available, facilitates the sharing of information about potential vulnerabilities through a publicly identifiable contact address, and designates a single point of contact for users including security researchers. | achieve | Confidentiality | SG-D-02.3.HL | CRA | Annex I Part II (4) + (5) + (6) + Art. 13(8) + Art. 13(17) + Annex II §2 | GV.PO-01, GV.SC-04, RS.CO-03 | — |

### D-03.1 — Identity Lifecycle

**High-Level Security Goal (SG-D-03.1.HL):** Identities of principals that interact with the entity's systems, products, services, components and data are managed in a verifiable, lifecycle-aware manner with documented boundaries between identity types and explicit hand-off protocols at boundary surfaces.

**Regulation baseline — `SG-D-03.1.GDPR` (GDPR):** The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification, before action is taken; the controller may request additional information necessary to confirm the identity, and the data subject must supply enough information to enable identification if they wish to exercise the rights (Art. 12(6) + Art. 11(2); the verification scope is constrained by Art. 5(1)(c) data minimisation).

**Regulation baseline — `SG-D-03.1.CRA` (CRA):** Identities, credentials, and access entitlements for users, services, and integrated components of the product with digital elements are managed in a verifiable manner throughout the operational lifetime of the product (Annex I Part I (2)(d) + Art. 13(15) type/batch/serial unique identification + Art. 13(17) single point of contact; backed by Annex II §3 unique-identification user information).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.1-001` | The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification before action is taken; the company may request additional information necessary to confirm identity, and the verification scope is itself constrained by data minimisation. | maintain | Confidentiality | SG-D-03.1.HL | GDPR | Art. 12(6) + Art. 11(2) + Art. 5(1)(c) | PR.AA-03, PR.AA-02, PR.DS-10 | — |
| `AG-D-03.1-002` | Identities, credentials, and access entitlements for users, services, and integrated components of the product are managed in a verifiable manner throughout the operational lifetime of the product, backed by unique product identification and a designated single point of contact. | maintain | Confidentiality | SG-D-03.1.HL | CRA | Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3 | PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 | — |

### D-03.2 — Authentication Strength

**High-Level Security Goal (SG-D-03.2.HL):** Authentication of users, services, and hardware that interact with the entity's systems, products, services, components and data operates through an authentication mechanism of sufficient strength for the risk in scope, with the strictest applicable floor discharging the most permissive on the same authentication event when both apply.

**Regulation baseline — `SG-D-03.2.GDPR` (GDPR):** Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality (Art. 28(3)(b) + Art. 29 + Art. 32(4) instruction-only processing); the identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification (Art. 12(6) + Art. 11(2)).

**Regulation baseline — `SG-D-03.2.CRA` (CRA):** Protection from unauthorised access uses appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product (Annex I Part I (2)(d) — "including but not limited to" + 3-way OR).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.2-001` | Persons authorised to process personal data act only on documented instructions from the company and are bound by confidentiality or an appropriate statutory obligation of confidentiality; the identity of data subjects making rights-exercise requests is verified proportionately to the risk of mis-identification. | maintain | Confidentiality | SG-D-03.2.HL | GDPR | Art. 28(3)(b) + Art. 29 + Art. 32(4) + Art. 12(6) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.2-002` | Protection from unauthorised access uses appropriate control mechanisms — which may include authentication, identity, or access-management systems — appropriate to the identified cybersecurity risk of the product. | maintain | Confidentiality | SG-D-03.2.HL | CRA | Annex I Part I (2)(d) | PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09 | The Annex I formulation is a non-exhaustive three-way disjunction, so the obligation is discharged by any mechanism proportionate to the assessed risk. |

### D-03.3 — Authorisation & Least Privilege

**High-Level Security Goal (SG-D-03.3.HL):** The entitlement to perform actions on the entity's systems, products, services, components, and data is managed per least privilege with explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between access surfaces.

**Regulation baseline — `SG-D-03.3.GDPR` (GDPR):** Persons authorised to process personal data act only on documented instructions from the controller (or processor), and are bound by confidentiality or an appropriate statutory obligation of confidentiality, with documented instructions binding the controller → processor → authorised-persons chain of authority under Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) and Art. 4(7) + Art. 4(8) anchoring controller and processor definitions.

**Regulation baseline — `SG-D-03.3.CRA` (CRA):** Access to the product with digital elements, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported (Annex I Part I (2)(d) `protection from unauthorised access through appropriate control mechanisms` + `possible unauthorised access reported` — R1 inclusive reading on `possible`) and attack surfaces including external interfaces limited (Annex I Part I (2)(j)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.3-001` | Persons authorised to process personal data act only on documented instructions and are bound by confidentiality, with the documented instructions binding the controller → processor → authorised-persons chain of authority. | maintain | Confidentiality | SG-D-03.3.HL | GDPR | Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) + Art. 4(7) + Art. 4(8) | PR.AA-05, PR.AA-06, PR.AT-02 | — |
| `AG-D-03.3-002` | Access to the product, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported, and attack surfaces including external interfaces limited. | maintain | Confidentiality | SG-D-03.3.HL | CRA | Annex I Part I (2)(d) + (2)(j) | PR.AA-05, PR.AA-06, DE.CM-09 | — |

### D-03.4 — Secure System Defaults

**High-Level Security Goal (SG-D-03.4.HL):** The default disposition of the entity's data-centric processing systems and the product's product-centric configuration is managed so that the baseline state of every processing system and every product configuration is the minimum-necessary / secure configuration, with relaxation requiring affirmative data-subject or user intervention.

**Regulation baseline — `SG-D-03.4.GDPR` (GDPR):** Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed — across the four AND-coordinated dimensions of amount of data collected, extent of their processing, period of their storage, and their accessibility — with the additional constraint that personal data are not made accessible without the individual's intervention to an indefinite number of natural persons (Art. 25(2) + Art. 25(1) privacy-by-design cross-anchor + Art. 5(1)(c) data minimisation underlying principle).

**Regulation baseline — `SG-D-03.4.CRA` (CRA):** Products with digital elements are made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements (Annex I Part I (2)(b)), and the secure-by-default configuration ensures that vulnerabilities can be addressed through security updates — automatic security updates installed within an appropriate timeframe, enabled by default, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them (Annex I Part I (2)(c)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-03.4-001` | Processing systems ensure that, by default, only personal data necessary for each specific purpose are processed — across the four AND-coordinated dimensions of amount collected, extent of processing, period of storage, and accessibility — and personal data are not made accessible without the individual's intervention to an indefinite number of natural persons. | maintain | Confidentiality & Privacy Right | SG-D-03.4.HL | GDPR | Art. 25(2) + Art. 25(1) + Art. 5(1)(c) | PR.PS-01, PR.DS-10, GV.PO-01 | — |
| `AG-D-03.4-002` | The product is made available on the market with a secure-by-default configuration, including the possibility for the user to reset it to its original state, and that configuration ensures vulnerabilities can be addressed through security updates installed automatically within an appropriate timeframe, enabled by default, with a clear opt-out and a postponement option. | maintain | Confidentiality & Privacy Right | SG-D-03.4.HL | CRA | Annex I Part I (2)(b) + (2)(c) | PR.PS-01, PR.DS-10, GV.SC-03 | — |

### D-04.1 — Incident Detection & Triage

**High-Level Security Goal (SG-D-04.1.HL):** Security-relevant events affecting the entity's systems, products, services, components and data are detected and triaged with documented trigger moments that anchor the downstream notification and response pipelines.

**Regulation baseline — `SG-D-04.1.GDPR` (GDPR):** Personal-data breaches are detected and triaged, and the moment of "becoming aware" is documented to anchor the 72-hour notification clock (Art. 33(1) + Art. 4(12) breach definition).

**Regulation baseline — `SG-D-04.1.CRA` (CRA):** Relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported (Annex I Part I (2)(l)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.1-001` | Personal-data breaches are detected and triaged, and the moment of becoming aware is documented so as to anchor the 72-hour notification clock. | achieve | Availability | SG-D-04.1.HL | GDPR | Art. 33(1) + Art. 4(12) | DE.AE-02, PR.PS-04, DE.CM-01 | — |
| `AG-D-04.1-002` | Relevant internal activity of the product — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported. | achieve | Availability | SG-D-04.1.HL | CRA | Annex I Part I (2)(l) | DE.CM-09, PR.PS-04, RS.MA-02 | — |

### D-04.2 — Containment & Mitigation

**High-Level Security Goal (SG-D-04.2.HL):** Security incidents affecting the entity's systems, products, services, components and data are contained and mitigated through appropriate measures that address the incident's impact and reduce the probability of further damage.

**Regulation baseline — `SG-D-04.2.GDPR` (GDPR):** Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk no longer materialises (Art. 34(3)(b)); the controller describes the measures taken or proposed in the Art. 33(3)(d) supervisory-authority notification.

**Regulation baseline — `SG-D-04.2.CRA` (CRA):** The availability of essential and basic functions of a product with digital elements is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer minimises the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)). Where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer takes the corrective measures necessary to bring the product into conformity, or to withdraw or recall the product (Art. 13(21)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.2-001` | Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including measures rendering the personal data unintelligible to any unauthorised person and subsequent measures ensuring the high risk no longer materialises; the measures taken or proposed are described in the supervisory-authority notification. | achieve | Availability | SG-D-04.2.HL | GDPR | Art. 34(3)(a) + Art. 34(3)(b) + Art. 33(3)(d) | PR.DS-10, PR.IR-04, RC.RP-04 | — |
| `AG-D-04.2-002` | The availability of essential and basic functions is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks; the negative impact on the availability of services provided by other devices or networks is minimised; and where the product or processes are not in conformity, corrective measures are taken or the product is withdrawn or recalled. | achieve | Availability | SG-D-04.2.HL | CRA | Annex I Part I (2)(h) + (2)(i) + (2)(k) + Art. 13(21) | PR.IR-04, PR.IR-03, DE.CM-09 | — |

### D-04.3 — Regulatory Notification

**High-Level Security Goal (SG-D-04.3.HL):** A major security incident is notified to the applicable recipients within the regulatory timelines applicable to the event's material scope.

**Regulation baseline — `SG-D-04.3.GDPR` (GDPR):** A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms (Art. 33(1)).

**Regulation baseline — `SG-D-04.3.CRA` (CRA):** An actively-exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours (Art. 14(2)(a), `SR-CRA-029`); vulnerability notification within 72 hours with general information, nature of exploit, mitigations, and user actions (Art. 14(2)(b), `SR-CRA-030`); final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.3-001` | A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the company becomes aware of it — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms. | achieve | Availability & Accountability | SG-D-04.3.HL | GDPR | Art. 33(1) | RS.CO-02, RS.MA-01, RS.MA-03 | — |
| `AG-D-04.3-002` | An actively-exploited vulnerability contained in the product that the company becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours; vulnerability notification within 72 hours with general information, nature of the exploit, mitigations and user actions; and a final report within 14 days of a corrective or mitigating measure being available. | achieve | Availability & Accountability | SG-D-04.3.HL | CRA | Art. 14(2)(a) + Art. 14(2)(b) + Art. 14(2)(c) | RS.MA-02, RS.CO-02 | — |

### D-04.4 — Restoration & Recovery

**High-Level Security Goal (SG-D-04.4.HL):** Systems, products, services, components and data are restored and recovered with documented recovery evidence applicable to the recovery dimensions of all four participating regulators on the same party.

**Regulation baseline — `SG-D-04.4.GDPR` (GDPR):** The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(b) + Art. 32(1)(c); Art. 5(1)(f) integrity/confidentiality cross-reference; Art. 32(2) five-event risk-enumeration cross).

**Regulation baseline — `SG-D-04.4.CRA` (CRA):** The availability of essential and basic functions of a product with digital elements is protected *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques and minimises the negative impact on services of other devices and networks (Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) corrective measures).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-04.4-001` | The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and the availability of and access to personal data is restored in a timely manner in the event of a physical or technical incident. | maintain | Availability | SG-D-04.4.HL | GDPR | Art. 32(1)(b) + Art. 32(1)(c) + Art. 5(1)(f) + Art. 32(2) | PR.IR-04, PR.DS-01, RC.RP-04 | — |
| `AG-D-04.4-002` | The availability of essential and basic functions is protected also after an incident through resilience and recovery measures, with exploitation-mitigation mechanisms and techniques reducing incident impact and corrective measures restoring conformity. | maintain | Availability | SG-D-04.4.HL | CRA | Annex I Part I (2)(h) + (2)(i) + (2)(k) + Art. 13(21) | PR.IR-03, PR.DS-10 | — |

### D-05.1 — Data Minimisation

**High-Level Security Goal (SG-D-05.1.HL):** Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the purpose for which it is processed, with a documented necessity assessment and, where the underlying purpose changes, a compatibility assessment confirming that the new use is consistent with the original. Special-category data is processed only where a narrow exception applies and is documented to that effect.

**Regulation baseline — `SG-D-05.1.GDPR` (GDPR):** Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing is compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing.

**Regulation baseline — `SG-D-05.1.CRA` (CRA):** Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.1-001` | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed; further processing is compatible with the original purposes per the Art. 6(4) five-factor test; by-design and by-default minimisation applies, and an impact assessment is performed for high-risk processing. | maintain | Privacy Right | SG-D-05.1.HL | GDPR | Art. 5(1)(c) + Art. 6(4) + Art. 25(1)/(2) + Art. 35 | PR.DS-10, ID.AM-03, GV.OC-03, GV.PO-01 | The Art. 9 special-category leg is inert for this case: no special-category data is processed. |
| `AG-D-05.1-002` | Data processed by the product — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with the risk assessment and the intended purpose plus reasonably foreseeable use supplying the proportionality calibration. | maintain | Privacy Right | SG-D-05.1.HL | CRA | Annex I Part I (2)(g) + Art. 3(23) + Art. 13(2) + Art. 13(3) | PR.DS-10, ID.AM-03 | — |

### D-05.2 — Retention & Archiving

**High-Level Security Goal (SG-D-05.2.HL):** Data — across the data classes in scope — is retained for the period required to satisfy its declared purpose, with documented retention rationale and, where the underlying purpose changes, a reset of the retention clock. Long-term archiving or research-only retention is paired with safeguards proportional to the residual identifiability.

**Regulation baseline — `SG-D-05.2.GDPR` (GDPR):** Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)).

**Regulation baseline — `SG-D-05.2.CRA` (CRA):** Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail (Art. 13(9) 10-year update-availability tail + Art. 13(8) 5-year support-period floor + Art. 13(18) 10-year Annex II information accessibility + Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge, with advisory messages); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.2-001` | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes processed; longer retention is permitted only where lawful and subject to Art. 89(1) safeguards, and the record of processing documents the envisaged erasure time limits per category of data. | maintain | Privacy Right | SG-D-05.2.HL | GDPR | Art. 5(1)(e) + Art. 89(1) + Art. 30(1)(f) | PR.DS-10, ID.AM-03 | — |
| `AG-D-05.2-002` | Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail, and the support-period end-date is provided clearly and understandably at the time of purchase. | maintain | Privacy Right | SG-D-05.2.HL | CRA | Art. 13(8) + Art. 13(9) + Art. 13(18) + Art. 13(19) + Annex I Part II (7) + (8) + Annex II §7 | PR.PS-02, GV.OV-02, GV.OC-04 | The 5-year support-period floor and the 10-year availability tail are absolute; they do not scale down with company size. |

### D-05.3 — Right to Erasure

**High-Level Security Goal (SG-D-05.3.HL):** Data held about a person is rendered inaccessible to the controller on the data subject's election, and data held by a product with digital elements is rendered inaccessible to the manufacturer on the user's election, by whichever mechanism — the controller-side policy execution or the manufacturer-side product affordance — applies to the data object. Erasure is performed without undue delay and is documented to demonstrate compliance; where a processor is involved, the processor-side mirror ensures deletion-or-return at contract end.

**Regulation baseline — `SG-D-05.3.GDPR` (GDPR):** Personal data are erased without undue delay on the data subject's Art. 17(1) request where one of the six Art. 17(1) grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn (no other Art. 6(1) basis applies); (c) Art. 21(1) objection (no overriding compelling legitimate ground) or Art. 21(2) direct-marketing objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child (Art. 8(1)). On processor contract end, the processor deletes or returns all personal data and existing copies per Art. 28(3)(g).

**Regulation baseline — `SG-D-05.3.CRA` (CRA):** The user of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner (Annex I Part I (2)(m) first limb — terminal deletion on user election — and second limb — secure cross-product transfer).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.3-001` | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds (a)–(f) applies; on processor contract end, the processor deletes or returns all personal data and existing copies. | cease | Privacy Right | SG-D-05.3.HL | GDPR | Art. 17(1)(a)–(f) + Art. 28(3)(g) | PR.DS-10, PR.DS-10, GV.SC-04 | — |
| `AG-D-05.3-002` | The user of the product can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner. | cease | Privacy Right | SG-D-05.3.HL | CRA | Annex I Part I (2)(m) | PR.DS-10, PR.DS-10, PR.DS-02 | — |

### D-05.4 — Data Portability

**High-Level Security Goal (SG-D-05.4.HL):** Personal data are exported to the data subject in a structured, commonly used, machine-readable format, and the data subject can transmit those data to another controller without hindrance, subject to the qualifying conditions and exclusions that scope the right.

**Regulation baseline — `SG-D-05.4.GDPR` (GDPR):** The data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)). The data subject can transmit those data to another controller without hindrance (Art. 20(1)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2). The right applies where processing is based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) AND processing is carried out by automated means (Art. 20(3)); the right does NOT apply to public-interest-task or legitimate-interest processing (Art. 20(4)), and the controller may refuse an export where it would adversely affect third-party rights.


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-05.4-001` | The data subject receives personal data in a structured, commonly used, machine-readable format, supplied without undue delay and free of charge, and can transmit those data to another controller without hindrance; where technically feasible the company transmits directly to the receiving controller. | achieve | Privacy Right | SG-D-05.4.HL | GDPR | Art. 20(1)–(4) + Art. 15(3) + Art. 12(3) + Art. 12(5) | PR.DS-10, PR.DS-10 | The right is scoped to consent- or contract-based processing carried out by automated means, which covers the company's B2B subscription relationship. |

### D-06.1 — Vendor Risk Assessment

**High-Level Security Goal (SG-D-06.1.HL):** Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain.

**Regulation baseline — `SG-D-06.1.GDPR` (GDPR):** The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)); the Art. 28(3) DPA closed-list clauses (a)–(h) are documented and the sub-processor authorisation chain (Art. 28(2)) is material to the due diligence.

**Regulation baseline — `SG-D-06.1.CRA` (CRA):** The manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity (Art. 3(48) FOSS definition) — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) sentence 1); on becoming aware of a component vulnerability (Art. 13(6) sentence 1), the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier (Art. 13(6) sentence 2).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.1-001` | The company engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures such that processing meets the Regulation's requirements and protects data-subject rights, with the Art. 28(3) closed-list clauses documented and the sub-processor authorisation chain material to the due diligence. | achieve | Accountability | SG-D-06.1.HL | GDPR | Art. 28(1) + Art. 28(2) + Art. 28(3)(a)–(h) | GV.SC-02, GV.SC-04, ID.AM-04 | — |
| `AG-D-06.1-002` | The company exercises due diligence when integrating components sourced from third parties — including free and open-source software components not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product; on becoming aware of a component vulnerability it addresses and remediates it without delay and shares relevant information with the component supplier. | achieve | Accountability | SG-D-06.1.HL | CRA | Art. 13(5) + Art. 13(6) + Art. 3(48) | GV.SC-01, GV.SC-02, ID.RA-02 | — |

### D-06.2 — Software Bill of Materials

**High-Level Security Goal (SG-D-06.2.HL):** The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies.

**Regulation baseline — `SG-D-06.2.CRA` (CRA):** The manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.2-002` | The company draws up and maintains a software bill of materials covering the components and dependencies contained in the product, in a commonly used and machine-readable format that includes at minimum the top-level dependencies. | achieve | Confidentiality | SG-D-06.2.HL | CRA | Annex I Part II (1) | ID.AM-02, GV.SC-02, GV.SC-03 | — |

### D-06.3 — Contractual Security Obligations

**High-Level Security Goal (SG-D-06.3.HL):** Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, as appropriate to the regulatory perspective and the actor involved.

**Regulation baseline — `SG-D-06.3.GDPR` (GDPR):** Controller/processor contracts and related transfer instruments include the GDPR-specific contractual security obligations required for personal-data processing: the Art. 28(3)(a)–(h) eight-element DPA floor, sub-processor authorisation and change-notification, processor Art. 32 security-measure commitments, audit/inspection access, and contract-end return/deletion; the Art. 46 appropriate-safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA or is exposed to third-country legal-process pressure.

**Regulation baseline — `SG-D-06.3.CRA` (CRA):** CRA contractual-security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place products with digital elements on the Union market only after verifying conformity assessment, technical documentation, CE marking, and manufacturer identification, and escalate significant risk or vulnerabilities to the manufacturer and MSA while taking corrective measures; distributors act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, and escalate non-conformity or vulnerabilities.


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-06.3-001` | Controller/processor contracts and related transfer instruments include the eight-element Art. 28(3)(a)–(h) floor, sub-processor authorisation and change-notification, processor security-measure commitments, audit and inspection access, and contract-end return or deletion; the Art. 46 safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA. | maintain | Accountability | SG-D-06.3.HL | GDPR | Art. 28(3)(a)–(h) + Art. 32 + Art. 46 + Art. 48 | — | — |
| `AG-D-06.3-002` | Contractual security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place the product on the Union market only after verifying conformity assessment, technical documentation, conformity marking and manufacturer identification, and distributors act with due care and escalate non-conformity or vulnerabilities. | maintain | Accountability | SG-D-06.3.HL | CRA | Art. 19 + Art. 20 | — | The company distributes its own product directly and occupies neither the importer nor the distributor role, so this row binds only through the manufacturer-side duties those operators verify against. |

### D-07.1 — Secure-by-Design Principles

**High-Level Security Goal (SG-D-07.1.HL):** Security is integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency.

**Regulation baseline — `SG-D-07.1.GDPR` (GDPR):** The controller implements appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing (Art. 25(1) GDPR), and ensures that by default only personal data which are necessary for each specific purpose are processed (Art. 25(2) GDPR).

**Regulation baseline — `SG-D-07.1.CRA` (CRA):** When placing a product with digital elements on the market, the manufacturer ensures that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I (Art. 13(1) CRA), with the cybersecurity risk assessment propagated across the 6 lifecycle phases (planning, design, development, production, delivery, maintenance) per Art. 13(2) chapeau + sentence 1, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact (Art. 13(2) sentence 2).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.1-001` | The company implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement data-protection principles in an effective manner and to integrate the necessary safeguards into the processing, and ensures that by default only personal data necessary for each specific purpose are processed. | maintain | Confidentiality | SG-D-07.1.HL | GDPR | Art. 25(1) + Art. 25(2) | PR.PS-06, PR.DS-10 | — |
| `AG-D-07.1-002` | When placing the product on the market, the company ensures it has been designed, developed and produced in accordance with the essential cybersecurity requirements of Annex I Part I, with the cybersecurity risk assessment propagated across the six lifecycle phases — planning, design, development, production, delivery, and maintenance — with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact. | maintain | Confidentiality | SG-D-07.1.HL | CRA | Art. 13(1) + Art. 13(2) | PR.PS-06, PR.PS-01 | — |

### D-07.2 — Secure Coding Practices

**High-Level Security Goal (SG-D-07.2.HL):** Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system attack-defence under an appropriate coding-practice evidence base.

**Regulation baseline — `SG-D-07.2.CRA` (CRA):** The manufacturer designs, develops, and produces the product with digital elements to limit its attack surfaces, including attack surfaces of external interfaces (Annex I Part I (2)(j) CRA), and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.2-002` | The company designs, develops, and produces the product so as to limit its attack surfaces, including the attack surfaces of external interfaces, and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques. | maintain | Confidentiality | SG-D-07.2.HL | CRA | Annex I Part I (2)(j) + (2)(k) | PR.PS-06, PR.PS-02 | — |

### D-07.3 — Build & Update Distribution Security

**High-Level Security Goal (SG-D-07.3.HL):** CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-agent integrity, ephemeral build environments) and update-distribution delivery-path security.

**Regulation baseline — `SG-D-07.3.CRA` (CRA):** The manufacturer of a product with digital elements shall securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates (Annex I Part II (7) CRA), and ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take (Annex I Part II (8) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.3-002` | The company securely distributes updates for the product in a timely manner, including through automatic updates where appropriate, and ensures that updates are disseminated free of charge, are clearly described, and contain information on the security improvements and on the actions the user should take. | maintain | Confidentiality | SG-D-07.3.HL | CRA | Annex I Part II (7) + (8) | PR.PS-06, PR.PS-02 | — |

### D-07.4 — Change Management

**High-Level Security Goal (SG-D-07.4.HL):** Change management delivers documented change-management procedures (manufacturer-side series-production conformity + entity-side change-management six-step), risk-assessment-approach, controlled-manner, and substantial-modification assessment with manufacturer-equivalent status consequences where applicable.

**Regulation baseline — `SG-D-07.4.CRA` (CRA):** The manufacturer of a product with digital elements that is part of a series of production ensures that procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation (Art. 13(14) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-07.4-002` | The company ensures that procedures are in place for products that are part of a series of production to remain in conformity with the Regulation. | achieve | Confidentiality | SG-D-07.4.HL | CRA | Art. 13(14) | GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04 | — |

### D-08.1 — General Security Awareness

**High-Level Security Goal (SG-D-08.1.HL):** General security awareness is established through a documented training programme with population-wide coverage, audience-routing, and governance hooks.

**Regulation baseline — `SG-D-08.1.GDPR` (GDPR):** The data protection officer informs and advises the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions (Art. 39(1)(a) GDPR), and monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR).

**Regulation baseline — `SG-D-08.1.CRA` (CRA):** A product with digital elements is accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.1-001` | The data protection officer informs and advises the company and the employees who carry out processing of their obligations under the Regulation, and monitors compliance including the assignment of responsibilities and the awareness-raising and training of staff involved in processing operations. | maintain | Accountability | SG-D-08.1.HL | GDPR | Art. 39(1)(a) + Art. 39(1)(b) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.1-002` | The product is accompanied by detailed instructions — or an internet address referring to such instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use. | maintain | Accountability | SG-D-08.1.HL | CRA | Annex II §8(a)–(e) | PR.AT-01 | — |

### D-08.2 — Role-Specific Competence

**High-Level Security Goal (SG-D-08.2.HL):** Role-specific competence is established through a function-specific depth, audience-routing, competence-criteria-anchored training, and governance hooks architecture.

**Regulation baseline — `SG-D-08.2.GDPR` (GDPR):** The data protection officer monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR) — the role-specific layer of the DPO-catalysed awareness function.

**Regulation baseline — `SG-D-08.2.CRA` (CRA):** Where the product with digital elements is intended for integration into other products with digital elements, the manufacturer provides the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-08.2-001` | The data protection officer monitors compliance including the assignment of responsibilities and the awareness-raising and training of staff involved in processing operations — the role-specific layer of the DPO-catalysed awareness function. | maintain | Accountability | SG-D-08.2.HL | GDPR | Art. 39(1)(b) | PR.AT-01, PR.AT-02 | — |
| `AG-D-08.2-002` | Where the product is intended for integration into other products, the company provides the information necessary for the integrator to comply with the essential cybersecurity requirements of Annex I Part I and the documentation requirements of Annex VII. | maintain | Accountability | SG-D-08.2.HL | CRA | Annex II §8(f) | PR.AT-02, GV.SC-03 | — |

### D-09.1 — Information Security Policies

**High-Level Security Goal (SG-D-09.1.HL):** Information security policies are established through a **documented policy architecture** with **governance hooks** and an **accountability chain** that anchor the entity's cybersecurity posture.

**Regulation baseline — `SG-D-09.1.GDPR` (GDPR):** The controller implements **appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner** (Art. 24(1) GDPR), with the Art. 5(2) accountability burden and the DPO as the governance anchor (Art. 37-39).

**Regulation baseline — `SG-D-09.1.CRA` (CRA):** An open-source software steward **puts in place and documents in a verifiable manner a cybersecurity policy** (Art. 24(1) CRA) covering vulnerability documentation, remediation, and information-sharing within the open-source community; a manufacturer **establishes policies, processes and procedures necessary to implement its CRA cybersecurity obligations** (Art. 13(8) CRA) including CVD policy, secure-update distribution, support-period determination, and cessation-of-operations communication.


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.1-001` | The company implements appropriate technical and organisational measures, such as policies, which are designed to implement data-protection principles in an effective manner, carrying the Art. 5(2) accountability burden with the data protection officer as governance anchor. | maintain | Accountability | SG-D-09.1.HL | GDPR | Art. 24(1) + Art. 5(2) + Art. 37–39 | GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02 | — |
| `AG-D-09.1-002` | The company establishes the policies, processes and procedures necessary to implement its product-security obligations, including the coordinated vulnerability disclosure policy, secure-update distribution, support-period determination, and cessation-of-operations communication. | maintain | Accountability | SG-D-09.1.HL | CRA | Art. 13(8) + Art. 24(1) | GV.PO-01, GV.PO-02 | — |

### D-09.2 — Impact & Risk Assessments

**High-Level Security Goal (SG-D-09.2.HL):** Impact and risk assessments are established through a **documented assessment** of identified risks and mitigation measures, with a **review cadence** calibrated to the lifecycle phase of the assessment object.

**Regulation baseline — `SG-D-09.2.GDPR` (GDPR):** Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a **data-protection impact assessment** covering the four Art. 35(7) content items and reviewed on change of risk per Art. 35(11) (Art. 35(1) + Art. 35(7) GDPR).

**Regulation baseline — `SG-D-09.2.CRA` (CRA):** The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2)** and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2) and indicating Annex I Part I (2) applicability (Art. 13(3) sentence 3) — documented in the **Annex VII §3 risk-assessment record** (Art. 13(4) sentence 1 + Annex VII §3 CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.2-001` | Prior to processing likely to result in a high risk to the rights and freedoms of natural persons, the company carries out a data-protection impact assessment covering the four Art. 35(7) content items, reviewed when the risk represented by the processing operations changes. | achieve | Accountability | SG-D-09.2.HL | GDPR | Art. 35(1) + Art. 35(7) + Art. 35(11) | ID.RA-05, ID.RA-04 | — |
| `AG-D-09.2-002` | The company documents the cybersecurity risk assessment and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use and indicating the applicability of the Annex I Part I (2) requirements, recorded in the Annex VII §3 risk-assessment record. | achieve | Accountability | SG-D-09.2.HL | CRA | Art. 13(2) + Art. 13(3) + Art. 13(4) + Annex VII §3 | ID.RA-05, GV.SC-07 | — |

### D-09.3 — Asset Inventories

**High-Level Security Goal (SG-D-09.3.HL):** Asset inventories are established through a **documented entity-level asset inventory** with **identification + classification + documentation** of ICT supported business functions, information assets, ICT assets, and their roles and dependencies.

**Regulation baseline — `SG-D-09.3.CRA` (CRA):** Manufacturers of products with digital elements draw up **technical documentation** containing at least a **general description** of the product (Annex VII §1) and a **description of the design, development, production and vulnerability-handling processes** including the system architecture description (Annex VII §2); the technical documentation is drawn up before placing on the market and updated during the support period (Art. 31(2) CRA), and kept at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.3-002` | The company draws up technical documentation containing at least a general description of the product and a description of the design, development, production and vulnerability-handling processes including the system architecture description, drawn up before placing on the market, updated during the support period, and kept at the disposal of market surveillance authorities. | achieve | Accountability | SG-D-09.3.HL | CRA | Annex VII §1 + §2 + Art. 31(2) + Art. 13(13) | ID.AM-01, ID.AM-02 | — |

### D-09.4 — Records of Processing

**High-Level Security Goal (SG-D-09.4.HL):** Records of processing activities are established through **parallel documentation regimes** that produce records of processing activities, technical documentation, certification records, information security policy documentation, and quality management system documentation serving distinct audit purposes.

**Regulation baseline — `SG-D-09.4.GDPR` (GDPR):** Each controller and processor **maintains a record of processing activities under its responsibility** (Art. 30(1) GDPR), in writing or electronic form (Art. 30(3) GDPR), containing the Art. 30(1) 7-item content list; the processor maintains a parallel record under Art. 30(2) GDPR; records are made available to the supervisory authority on request (Art. 30(4) GDPR), subject to the Art. 30(5) 250-employee exception.

**Regulation baseline — `SG-D-09.4.CRA` (CRA):** The manufacturer **draws up before placing a product with digital elements on the market the technical documentation referred to in Art. 31** (Art. 13(12) sentence 1 CRA), carries out the conformity assessment procedure referred to in Art. 32, draws up the EU declaration of conformity under Art. 28, and affixes the CE marking under Art. 30 (Art. 13(12) sentence 2); the manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-09.4-001` | The company maintains a record of processing activities under its responsibility, in writing or electronic form, containing the Art. 30(1) seven-item content list, with a parallel processor-side record, made available to the supervisory authority on request. | maintain | Accountability | SG-D-09.4.HL | GDPR | Art. 30(1)–(5) | ID.AM-08, PR.DS-10, GV.PO-02 | The Art. 30(5) under-250-employee exception is nominally available to an 8-person team but is not relied upon, because the processing is neither occasional nor free of risk to data-subject rights. |
| `AG-D-09.4-002` | The company draws up the technical documentation before placing the product on the market, carries out the conformity assessment procedure, draws up the EU declaration of conformity and affixes the conformity marking, and keeps the technical documentation and the declaration at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer. | maintain | Accountability | SG-D-09.4.HL | CRA | Art. 13(12) + Art. 13(13) + Art. 28 + Art. 30 + Art. 31 + Art. 32 | ID.AM-08, PR.DS-10, ID.RA-05 | — |

### D-10.1 — Continuous Security Monitoring

**High-Level Security Goal (SG-D-10.1.HL):** Continuous security monitoring is established through a **layered detection-and-monitoring architecture** spanning personal-data processing systems, network and information systems, on-device product activity, ICT systems and tools, and high-risk AI systems, with detection capability feeding the incident-response chain.

**Regulation baseline — `SG-D-10.1.GDPR` (GDPR):** The controller and processor implement appropriate technical and organisational measures to ensure the **ongoing confidentiality, integrity, availability and resilience of processing systems and services** (Art. 32(1)(b) GDPR) and **regularly test, assess and evaluate their effectiveness** (Art. 32(1)(d) GDPR); personal-data processing systems and services are monitored for the five Art. 32(2) risk types, with a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock.

**Regulation baseline — `SG-D-10.1.CRA` (CRA):** A product with digital elements **provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provides an opt-out mechanism for the user** (Annex I Part I (2)(l) CRA); the manufacturer **facilitates the sharing of information about potential vulnerabilities** through a single contact address (Annex I Part II (6) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.1-001` | The company implements appropriate technical and organisational measures to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services and regularly tests, assesses and evaluates their effectiveness, monitoring for the five Art. 32(2) risk types with a clear definition of the moment of becoming aware of a breach. | maintain | Availability | SG-D-10.1.HL | GDPR | Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) | DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04 | — |
| `AG-D-10.1-002` | The product provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, with an opt-out mechanism for the user, and the company facilitates the sharing of information about potential vulnerabilities through a single contact address. | maintain | Availability | SG-D-10.1.HL | CRA | Annex I Part I (2)(l) + Annex I Part II (6) | DE.CM-01, DE.CM-09, ID.IM-04 | — |

### D-10.2 — Audit Logging & Traceability

**High-Level Security Goal (SG-D-10.2.HL):** Audit logging and traceability are established through a **layered audit-records architecture** spanning compliance records with integrity and traceability, product-level technical documentation traceability, entity-level information security policy documentation, and AI-system event logging with retention floors.

**Regulation baseline — `SG-D-10.2.GDPR` (GDPR):** The controller and processor **maintain compliance records in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections** (Art. 30(3) + Art. 5(2) + Art. 31 GDPR), including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — made available to the supervisory authority on request (Art. 30(3)).

**Regulation baseline — `SG-D-10.2.CRA` (CRA):** The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmonised standards applied, test reports, copy of the EU declaration of conformity, SBOM on MSA reasoned request), **preserves the cybersecurity risk-assessment documentation** (Annex VII §3 + Art. 13(4) sentence 1) during the support period (10 years or support period, whichever longer) with updates as appropriate, and ensures **test reports demonstrating verification of conformity with Annex I Part I and Part II** are part of the technical documentation and available on reasoned request from market surveillance authorities (Annex VII §6 + Annex I Part II (3) + Art. 13(22) CRA).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.2-001` | The company maintains compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections — records of processing, consent records, processor contract records, breach notification records, and impact-assessment records — made available to the supervisory authority on request. | maintain | Availability & Accountability | SG-D-10.2.HL | GDPR | Art. 30(3) + Art. 5(2) + Art. 31 | PR.DS-01, PR.PS-04, DE.CM-01, GV.PO-02 | — |
| `AG-D-10.2-002` | The company maintains the technical documentation, preserves the cybersecurity risk-assessment documentation during the support period with updates as appropriate, and ensures that test reports demonstrating verification of conformity with Annex I Parts I and II form part of the technical documentation and are available on reasoned request from market surveillance authorities. | maintain | Availability & Accountability | SG-D-10.2.HL | CRA | Annex VII §3 + §5–§8 + Art. 13(4) + Art. 13(22) + Annex I Part II (3) | PR.DS-01, PR.PS-02, GV.PO-02, ID.RA-04 | — |

### D-10.3 — Compliance Testing

**High-Level Security Goal (SG-D-10.3.HL):** Compliance testing is established through a **5-parallel-testing-programme architecture** spanning effectiveness-evaluation of security measures, effectiveness-assessment of risk-management measures, product-level conformity-assessment, entity-level digital operational resilience testing with TLPT, and AI-system-level testing for risk management with real-world-conditions and accuracy/robustness/cybersecurity baseline testing.

**Regulation baseline — `SG-D-10.3.GDPR` (GDPR):** The controller and processor implement appropriate technical and organisational measures including **a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing** (Art. 32(1)(d) GDPR); the DPIA is **reviewed at least when there is a change of the risk represented by processing operations** (Art. 35(11) GDPR).

**Regulation baseline — `SG-D-10.3.CRA` (CRA):** Manufacturers of products with digital elements **carry out effective and regular tests and reviews of the product** (Annex I Part II (3) CRA), and the technical documentation shall contain **the reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I** (Annex VII §6 CRA); conformity is demonstrated via the Annex VIII Part I (Module A internal production control) or Part II (Module B+C and H notified-body EU-type examination) conformity-assessment modules depending on product classification (Class I / Class II / critical per Art. 6 + Annex III).


| AG ID | Adjusted Goal | Pattern | Property | Parent Goal | Regulation | Articles | Control Anchors | Adjustment |
|---|---|---|---|---|---|---|---|---|
| `AG-D-10.3-001` | The company implements a process for regularly testing, assessing and evaluating the effectiveness of the technical and organisational measures securing the processing, and reviews the impact assessment at least when the risk represented by processing operations changes. | maintain | Accountability | SG-D-10.3.HL | GDPR | Art. 32(1)(d) + Art. 35(11) | PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03 | — |
| `AG-D-10.3-002` | The company carries out effective and regular tests and reviews of the product, and the technical documentation contains the reports of the tests carried out to verify the conformity of the product and of the vulnerability-handling processes with Annex I Parts I and II. | maintain | Accountability | SG-D-10.3.HL | CRA | Annex I Part II (3) + Annex VII §6 + Annex VIII + Art. 6 + Annex III | PR.PS-02, ID.RA-05, DE.AE-02, GV.OV-03 | The product is default-class — not Class I, Class II, or critical under Art. 6 and Annex III — so conformity is demonstrated via the Annex VIII Part I internal-production-control module without notified-body involvement. |

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



| Sub-Domain | Scale | Inheritability | Priority | Tier | Rationale |
|---|---|---|---|---|---|
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

- **Source files:** Baseline controls at `baseline/CONTROLS/` (NIST CSF 2.0, NIST PF 1.0) and modular sub-domain corpora at `baseline/domains/D-XX_*/D-XX.X/`
- **Mapping date:** 2026-08-14
- **Coverage scope:** 35 ACTIVE sub-domains (D-01.1..D-10.3 minus D-02.4, D-06.4, D-08.3 NOT_ADDRESSED).
- **Controls total:** ~300 NIST CSF 2.0 + ~200 NIST PF 1.0 across 35 sub-domains.

### §6.37 Cross-references

- Per-control JSONs: `baseline/CONTROLS/<framework>/<function>/<control_id>.json`
- Per-subdomain corpus: `baseline/domains/D-XX_*/D-XX.X/` (source-of-truth for control derivation)
- Traceability mappings: `baseline/MAPPINGS/`

---

## §7 Cross-References

- **`Doc01_INTAKE_FORM.md`**: Company context intake form (profile, operational reality, micro-scale tiers, regulatory applicability).
- **`baseline/00_Taxonomy_Reference.md`**: Sub-domain canonical taxonomy (D-01.1 .. D-10.3).
- **`baseline/01_Ambiguity_Registry.md`**: Ambiguity registry cards informing disambiguation of regulatory clauses.
- **`baseline/domains/`**: Modular per-regulation corpus for Baseline Goals (`SO-D-XX.Y.HL` and per-regulation `regs/<REG>.md`).
- **`baseline/CONTROLS/`**: NIST CSF 2.0, NIST PF 1.1, and NIST AI RMF control referentials.
- **`baseline/MAPPINGS/`**: Traceability chain and SR control mapping store.
- **Strategic Tensions**: 4 tensions (T-001..T-004) resolved with max-SLA routing in §4.

---

## §8 Validation

- **35 ACTIVE sub-domains** mapped to Adjusted Goals in §3.
- Distinct AG IDs used in main tables: **35 slot 001 (GDPR-driven, one per ACTIVE sub) + 34 slot 002 (CRA-driven) = 69 distinct IDs**.
- **§2 / §3 / §4 / §5 are technology-free** — no vendor, product, or tool named (verified by blocklist scan and by inspection).
- **Baseline Goal wording inherited from the corpus unchanged.** Any technology tokens in that wording come from the frozen Phase 0 Baseline Goal prose and are retained as inherited corpus wording (ADR-004 D2). Technology-neutrality applies to the Adjusted Goals layer (§3), not to the inherited Baseline Goal wording.
- **Track B decision table: 37 rows** in §5 (35 ACTIVE + D-02.4 + D-06.4). D-08.3 is NOT_ADDRESSED and was never tiered.
- **Distribution (37 tiered rows): 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37**. Restricted to the 35 ACTIVE rows: **31 LIGHTWEIGHT + 4 MINIMAL**, all MUST.
- **4 tensions resolved** with max-SLA routing in §4 (T-001..T-004).
- Floor rule preserved: every MUST ≥ MINIMAL per methodology baseline.

---

## §9 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 7.2 | 2026-10-07 | aegis-mvp executor | D-01.1 and D-01.2 — the only blocks `compose.build_pack` ever slices into the P4 pack — restated in the 9-column EMIT shape the L0 gate validates (`Company implication` present, `Control Anchors` absent, `Parent Goal` in the `SO-` form), with their Adjusted Goals rewritten off the near-verbatim restatement the adaptation gate rejects: the D-01.2 row the D-01.1 call is shown measured 0.96 against the 0.88 ceiling of `check_obligation_retention`. The remaining 33 blocks keep the DELIVERED shape and never reach a prompt. |
| 7.1 | 2026-09-22 | aegis-mvp executor | Consolidated goals table per ADR-003 D1 + ADR-004; §2 Framing absorbs generic scale/hosting adjustments; AG designation enforced; cross-references aligned to MVP baseline. |
| 7.0 | 2026-08-14 | Executor | §6 NIST Controls full coverage expansion across 35 active sub-domains. |
| 6.0 | 2026-08-13 | Fase de Especificação 10 Executor | NIST Controls Layer pilot (D-01.1). CONTROLS/ restructured by framework→function. |
| 5.1 | 2026-09-22 | aegis-mvp executor | Phase 1 designation = Goals: the "AO" label is retired. All prose "AO" references -> "AG". |
| 5.0 | 2026-08-10 | Fase de Especificação 9 Executor | Canonical AG IDs in tables: slot 001 (GDPR-driven) and slot 002 (CRA-driven). |
| 4.0 | 2026-08-10 | Fase de Especificação 8 Executor | AG ID migration from legacy PG/SG IDs. |
| 3.0 | 2026-08-10 | Executor | Phase 1 tech-free restructure. Scope corrected to 35 ACTIVE sub-domains. |
| 2.0 | 2026-08-06 | Fase de Especificação 5 Executor | Deep enrichment — 74 detail cards. 4 tensions expanded. |
| 1.0 | 2026-08-06 | Fase de Especificação 4 Executor | Initial release — 74 adjusted goals + 4 tensions resolved + 37-row Track B decision trail. |

---

## §10 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author (tech-free restructure) | Executor | | 2026-08-10 |
| Business Review (CEO) | | | |
| Technical Review (CTO) | | | |
| AEGIS Methodology Review | | | |

**Next documents that consume this profile:**
- Phase 2 `11_Rules_Catalog.md` (rules consume the adjusted goals in §3)
- Phase 3 `14_Architectural_Nodes.md` (architecture consumes the tier from §5)


---
