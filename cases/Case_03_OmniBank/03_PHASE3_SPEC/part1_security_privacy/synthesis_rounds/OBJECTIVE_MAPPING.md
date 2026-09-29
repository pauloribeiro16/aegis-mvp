# Phase 2 Objective Mapping — Exhaustive Coverage Matrix (OmniBank Financial Systems)

> **Scope:** all 134 Phase 2 objectives (29 `PO-` GDPR · 105 `SO-` across CRA 36, NIS 2 24, DORA 30, AI Act 15) + the 7 principles (see [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md)).
> **State legend:** `Accepted R1 (RNxx)` = new constraint accepted in Round 1 · `Accepted R1 (chain row)` = realized by an existing V0 functional card, chain attached in Round 1 · no-carrier/N-A = recorded decisions.
> **Verdicts:** Round 1 CONVERGED (16/16 + 92/92 accepts by client directive, 2026-09-29) — recorded in [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md).

> **Coverage-granularity note (recorded debt, ADR-007 D2/D3).** The `Accepted R1` verdicts above assert coverage at **carrier-linkage** granularity: the objective id appears in a requirement's chain. They are **not** discharge-verified — no per-objective check has confirmed that the carriers' Volere fit criteria reconstitute the objective's Phase 2 Verification Criteria, nor that every leg of its Operational Statement is carried. A leg-level audit has been performed in Case_01 only, where it moved 20 of 26 rows from "covered" to "partially covered" with named carve-outs. Treat the N/A and organizational rows as the *only* verdicts here resting on more than linkage, and route any uncarried PROCESS/CAPABILITY leg to the organizational deliverable (`part1_security_privacy/Doc03_Organizational_Requirements.md`, ADR-008). Enforced mechanically by `python scripts/check_traceability.py --case Case_03_OmniBank` (T5 reports drivers whose declared carrier does not cite them back).

> **Numbering note.** Phase 2 numbers objectives *compactly* within each sub-domain: regulations in the canonical order GDPR → CRA → NIS 2 → DORA → AI Act, numbered `001…n` over those actually present. Where a sub-domain lacks an earlier regulation, every later suffix shifts down. Phase 3 chains are re-anchored against this numbering (`scripts/reanchor_chains.py`); a citation must never be assumed to follow a fixed five-slot convention.

## D-01 — Data Protection & Encryption

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-01.1-001` | Personal data at rest is processed in a manner that ensures appropriate security — including protection agains... | `R2.1` (RN14) | TB | **Accepted R1 (RN14)** | RN14 |
| `SO-D-01.1-002` | Where a product with digital elements stores data — personal or other — the confidentiality of that data is pr... | `R2.1` (RN14) | TB | **Accepted R1 (RN14)** | RN14 |
| `SO-D-01.1-003` | Essential and important entities establish policies and procedures regarding the use of cryptography and, wher... | `R2.1` (RN14) | TB | **Accepted R1 (RN14)** | RN14 |
| `SO-D-01.1-004` | Data confidentiality, integrity, authenticity and availability are maintained at high standards across all dat... | `R2.1` (RN14) | TB | **Accepted R1 (RN14)** | RN14 |
| `PO-D-01.2-001` | Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains conf... | all UC preconditions (RN13) | TB | **Accepted R1 (RN13)** | RN13 |
| `SO-D-01.2-002` | Where data is transmitted by a product with digital elements — personal or other — the confidentiality of the ... | all UC preconditions (RN13) | TB | **Accepted R1 (RN13)** | RN13 |
| `SO-D-01.2-003` | Data confidentiality, integrity, authenticity and availability are maintained at high standards across all dat... | all UC preconditions (RN13) | TB | **Accepted R1 (RN13)** | RN13 |
| `PO-D-01.3-001` | Where pseudonymisation or encryption is applied to personal data, the additional information required to re-id... | `R2.3` (RN15) | LP | **Accepted R1 (RN15)** | RN15 |
| `SO-D-01.3-002` | Cryptographic keys and related authentication material used to protect the confidentiality and integrity of st... | `R2.3` (RN15) | LP | **Accepted R1 (RN15)** | RN15 |
| `SO-D-01.3-003` | Strong authentication mechanisms, cryptographic-key protection measures, and data encryption are implemented t... | `R2.3` (RN15) | LP | **Accepted R1 (RN15)** | RN15 |
| `PO-D-01.4-001` | Personal data are accurate and, where necessary, kept up to date; every reasonable step is taken to ensure tha... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-01.4-002` | The integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integri... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-01.4-003` | Data confidentiality, integrity, authenticity and availability are maintained at high standards across all dat... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-01.4-004` | High-risk AI systems are as resilient as possible regarding errors, faults, or inconsistencies that may occur ... | `R11.4` (RN25) | AS | **Accepted R1 (RN25)** | RN25 |
## D-02 — Vulnerability Management

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-02.1-001` | A controller or processor operates a process for regularly testing, assessing, and evaluating the effectivenes... | `R3.1` (chain row) | AS | **Accepted R1 (chain row)** | R3.1 |
| `SO-D-02.1-002` | A product with digital elements is made available on the market without known exploitable vulnerabilities (Ann... | `R3.1` (chain row) | AS | **Accepted R1 (chain row)** | R3.1 |
| `SO-D-02.1-003` | Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinate... | `R3.1` (chain row) | AS | **Accepted R1 (chain row)** | R3.1 |
| `SO-D-02.1-004` | Sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT-supported business funct... | `R3.1` (chain row) | AS | **Accepted R1 (chain row)** | R3.1 |
| `SO-D-02.1-005` | A risk-management system is established, implemented, documented, and maintained for high-risk AI systems thro... | `R10.2` (chain row) | AS | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-02.2-001` | Vulnerabilities of a product with digital elements are addressed and remediated through security updates witho... | `R3.2` (chain row) | AS | **Accepted R1 (chain row)** | R3.2 |
| `SO-D-02.2-002` | A sound network and infrastructure management structure is established, using appropriate techniques, methods ... | `R3.2` (chain row) | AS | **Accepted R1 (chain row)** | R3.2 |
| `SO-D-02.3-001` | The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for it... | `R3.3` (chain row) | AS | **Accepted R1 (chain row)** | R3.3 |
| `SO-D-02.3-002` | Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinate... | `R3.3` (chain row) | AS | **Accepted R1 (chain row)** | R3.3 |
| `SO-D-02.4-001` | Effective and regular tests and reviews of the security of a product with digital elements are applied on a co... | `R3.4` (chain row) | AS | **Accepted R1 (chain row)** | R3.4 |
| `SO-D-02.4-002` | A sound and comprehensive digital operational resilience testing programme is established, maintained and revi... | `R3.4` (chain row) | AS | **Accepted R1 (chain row)** | R3.4 |
| `SO-D-02.4-003` | High-risk AI systems are tested to ensure that they perform consistently for their intended purpose (Art. 9(6)... | `R11.4` (chain row) | AS | **Accepted R1 (chain row)** | R11.4 |
## D-03 — Access Control & Identity Management

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-03.1-001` | The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonabl... | `R4.1` (chain row) | LP | **Accepted R1 (chain row)** | R4.1 |
| `SO-D-03.1-002` | Identities, credentials, and access entitlements for users, services, and integrated components of the product... | `R4.1` (RN21) | LP | **Accepted R1 (RN21)** | RN21 |
| `SO-D-03.1-003` | Identities of the workforce — employees, contractors and other authorised personnel with access to network and... | `R4.1` (chain row) | LP | **Accepted R1 (chain row)** | R4.1 |
| `SO-D-03.1-004` | Identity assertions for financial-entity staff and service-to-service identities are managed, protected, and c... | `R4.1` (chain row) | LP | **Accepted R1 (chain row)** | R4.1 |
| `PO-D-03.2-001` | Persons authorised to process personal data act only on documented instructions from the controller (or proces... | `R4.2` (chain row) | TB | **Accepted R1 (chain row)** | R4.2 |
| `SO-D-03.2-002` | Protection from unauthorised access uses appropriate control mechanisms, which may include authentication, ide... | `R4.2` (RN19) | TB | **Accepted R1 (RN19)** | RN19 |
| `SO-D-03.2-003` | Multi-factor authentication or continuous authentication solutions are used where appropriate, and secured voi... | `R4.2` (RN19) | TB | **Accepted R1 (RN19)** | RN19 |
| `SO-D-03.2-004` | Strong authentication mechanisms (based on relevant standards and dedicated control systems) are implemented a... | `R4.2` (RN19) | TB | **Accepted R1 (RN19)** | RN19 |
| `PO-D-03.3-001` | Persons authorised to process personal data act only on documented instructions from the controller (or proces... | `R4.3` (chain row) | LP | **Accepted R1 (chain row)** | R4.3 |
| `SO-D-03.3-002` | Access to the product with digital elements, its data, services, and functions is limited to authenticated and... | `R4.3` (chain row) | LP | **Accepted R1 (chain row)** | R4.3 |
| `SO-D-03.3-003` | Access-control policies are established and applied at the entity level for the entity's network and informati... | `R4.3` (chain row) | LP | **Accepted R1 (chain row)** | R4.3 |
| `SO-D-03.3-004` | ICT security policies limit physical or logical access to information assets and ICT assets to what is require... | `R4.3` (chain row) | LP | **Accepted R1 (chain row)** | R4.3 |
| `PO-D-03.4-001` | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by... | `R4.4`, `R8.2` (RN20) | FS | **Accepted R1 (RN20)** | RN20 |
| `SO-D-03.4-002` | Products with digital elements are made available on the market with a secure-by-default configuration — inclu... | `R4.4`, `R8.2` (RN20) | FS | **Accepted R1 (RN20)** | RN20 |
## D-04 — Incident Response & Notification

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-04.1-001` | Personal-data breaches are detected and triaged, and the moment of "becoming aware" is documented to anchor th... | `R5.1` (chain row) | V | **Accepted R1 (chain row)** | R5.1 |
| `SO-D-04.1-002` | Relevant internal activity of the product with digital elements — including access to or modification of data,... | `R5.1` (chain row) | V | **Accepted R1 (chain row)** | R5.1 |
| `SO-D-04.1-003` | An incident-handling capability is established, covering the prevention, detection, analysis, containment, res... | `R5.1` (chain row) | V | **Accepted R1 (chain row)** | R5.1 |
| `SO-D-04.1-004` | Anomalous activities — including ICT network performance issues and ICT-related incidents — are promptly detec... | `R5.1` (chain row) | V | **Accepted R1 (chain row)** | R5.1 |
| `PO-D-04.2-001` | Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, ... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.2-002` | The availability of essential and basic functions of a product with digital elements is protected also after a... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.2-003` | The entity operates the incident-handling capability across all six actions of the Art. 6(8) `incident handlin... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.2-004` | A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documente... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `PO-D-04.3-001` | A personal data breach is notified to the competent supervisory authority without undue delay and, where feasi... | `R5.2` (RN18) | V | **Accepted R1 (RN18)** | RN18 |
| `SO-D-04.3-002` | An actively-exploited vulnerability contained in a product with digital elements that the manufacturer becomes... | `R5.2` (RN18) | V | **Accepted R1 (RN18)** | RN18 |
| `SO-D-04.3-003` | A significant incident is notified to the CSIRT or, where applicable, the competent authority via a twin-trigg... | `R5.2` (RN18) | V | **Accepted R1 (RN18)** | RN18 |
| `SO-D-04.3-004` | A major ICT-related incident is reported to the relevant competent authority without undue delay (Art. 19(1));... | `R5.2` (RN18) | V | **Accepted R1 (RN18)** | RN18 |
| `SO-D-04.3-005` | A serious incident involving a high-risk AI system is reported to the market surveillance authorities of the M... | `R5.2` (RN18) | V | **Accepted R1 (RN18)** | RN18 |
| `PO-D-04.4-001` | The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing system... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.4-002` | The availability of essential and basic functions of a product with digital elements is protected *also after ... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.4-003` | Business continuity, backup management, disaster recovery, and crisis management capabilities are maintained, ... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.4-004` | A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documente... | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
## D-05 — Data Lifecycle

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to ... | `R6.1` (chain row) | DM | **Accepted R1 (chain row)** | R6.1 |
| `SO-D-05.1-002` | Data processed by a product with digital elements — personal or other — is limited to what is adequate, releva... | `R6.1` (chain row) | DM | **Accepted R1 (chain row)** | R6.1 |
| `SO-D-05.1-003` | High-risk AI systems which make use of techniques involving the training of AI models with data are developed ... | `R1.2`, `R6.1` (RN12) | DM | **Accepted R1 (RN12)** | RN12 |
| `PO-D-05.2-001` | Personal data are kept in a form which permits identification of data subjects for no longer than is necessary... | `R6.2` (chain row) | LE | **Accepted R1 (chain row)** | R6.2 |
| `SO-D-05.2-002` | Security updates and supporting advisory messages remain available to users across the support period and the ... | `R6.2` (chain row) | LE | **Accepted R1 (chain row)** | R6.2 |
| `SO-D-05.2-003` | Providers of high-risk AI systems keep the logs referred to in Art. 12(1) — automatically generated by their h... | `R1.2`, `R11.2` (RN23) | V | **Accepted R1 (RN23)** | RN23 |
| `PO-D-05.3-001` | Personal data are erased without undue delay on the data subject's Art. 17(1) request where one of the six Art... | `R6.3`, `R11.2` (RN17) | LE | **Accepted R1 (RN17)** | RN17 |
| `SO-D-05.3-002` | The user of a product with digital elements can securely and easily remove, on a permanent basis, all data and... | `R6.3` (chain row) | LE | **Accepted R1 (chain row)** | R6.3 |
| `PO-D-05.4-001` | The data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + ... | `R6.4` (chain row) | LE | **Accepted R1 (chain row)** | R6.4 |
## D-06 — Supply Chain & Third-Party Security

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-06.1-001` | The controller engages only processors providing sufficient guarantees to implement appropriate technical and ... | `R7.1` (chain row) | V | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-06.1-002` | The manufacturer exercises due diligence when integrating components sourced from third parties — including co... | `R7.1` (chain row) | V | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-06.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational ... | `R7.1` (chain row) | V | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-06.1-004` | Financial entities manage ICT third-party risk taking into account four-factor proportionality — nature, scale... | `R7.1` (RN26) | V | **Accepted R1 (RN26)** | RN26 |
| `SO-D-06.2-001` | The manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the prod... | `R7.2` (chain row) | V | **Accepted R1 (chain row)** | R7.2 |
| `PO-D-06.3-001` | Controller/processor contracts and related transfer instruments include the GDPR-specific contractual security... | `R7.3` (chain row) | V | **Accepted R1 (chain row)** | R7.3 |
| `SO-D-06.3-002` | CRA contractual-security coverage is expressed through economic-operator duties rather than a single negotiate... | `R7.3` (chain row) | V | **Accepted R1 (chain row)** | R7.3 |
| `SO-D-06.3-003` | Essential and important entities manage contractual security for direct supplier and service-provider relation... | `R7.3` (chain row) | V | **Accepted R1 (chain row)** | R7.3 |
| `SO-D-06.3-004` | Financial entities structure ICT third-party contractual arrangements so that rights and obligations are clear... | `R7.3` (chain row) | V | **Accepted R1 (chain row)** | R7.3 |
| `PO-D-06.4-001` | Non-EU controllers and processors falling under GDPR Art. 3(2) designate a representative in writing in the Un... | — | — | **N/A** (recorded — inapplicable to this entity/product form) | — |
| `SO-D-06.4-002` | CRA third-party boundary management preserves product-compliance accountability across EU/non-EU and supply-ch... | — | — | **N/A** (recorded — inapplicable to this entity/product form) | — |
| `SO-D-06.4-003` | NIS 2 boundary management is split across cross-border notification routing and entity-side supplier-scope con... | `R7.1` (chain row) | V | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-06.4-004` | Contractual arrangements concerning critical or important functions grant the financial entity, an appointed t... | `R7.1` (RN26) | V | **Accepted R1 (RN26)** | RN26 |
## D-07 — Secure Development & AI Design

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-07.1-001` | The controller implements appropriate technical and organisational measures — such as pseudonymisation — which... | `R8.1` (chain row) | AS | **Accepted R1 (chain row)** | R8.1 |
| `SO-D-07.1-002` | When placing a product with digital elements on the market, the manufacturer ensures that it has been designed... | `R8.1` (chain row) | AS | **Accepted R1 (chain row)** | R8.1 |
| `SO-D-07.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational ... | `R8.1` (chain row) | AS | **Accepted R1 (chain row)** | R8.1 |
| `SO-D-07.1-004` | Financial entities establish a sound network and infrastructure management structure using appropriate techniq... | `R8.1` (chain row) | AS | **Accepted R1 (chain row)** | R8.1 |
| `SO-D-07.1-005` | High-risk AI systems are designed and developed in such a way that they achieve an appropriate level of accura... | `R11.4` (RN25) | AS | **Accepted R1 (RN25)** | RN25 |
| `SO-D-07.2-001` | The manufacturer designs, develops, and produces the product with digital elements to limit its attack surface... | `R8.2` (chain row) | AS | **Accepted R1 (chain row)** | R8.2 |
| `SO-D-07.2-002` | Financial entities implement documented policies, procedures and controls for ICT change management, including... | `R8.2` (chain row) | AS | **Accepted R1 (chain row)** | R8.2 |
| `SO-D-07.2-003` | High-risk AI systems are designed and developed with appropriate technical and organisational measures to enab... | `R11.4` (RN25) | AS | **Accepted R1 (RN25)** | RN25 |
| `SO-D-07.3-001` | The manufacturer of a product with digital elements shall securely distribute updates for the product with dig... | `R3.2` (chain row) | AS | **Accepted R1 (chain row)** | R3.2 |
| `SO-D-07.3-002` | Essential and important entities take appropriate and proportionate technical, operational and organisational ... | `R3.2` (chain row) | AS | **Accepted R1 (chain row)** | R3.2 |
| `SO-D-07.4-001` | The manufacturer of a product with digital elements that is part of a series of production ensures that proced... | — | — | **N/A** (recorded — inapplicable to this entity/product form) | — |
| `SO-D-07.4-002` | Financial entities implement documented policies, procedures and controls for ICT change management, including... | `R8.3` (chain row) | V | **Accepted R1 (chain row)** | R8.3 |
## D-08 — Human Factors & Oversight

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-08.1-001` | The data protection officer informs and advises the controller or the processor and the employees who carry ou... | — | — | **No functional carrier** (organizational — DPO advisory activity, recorded decision) | — |
| `SO-D-08.1-002` | A product with digital elements is accompanied by detailed instructions — or an internet address referring to ... | `R9.1` (chain row) | V | **Accepted R1 (chain row)** | R9.1 |
| `SO-D-08.1-003` | Essential and important entities take appropriate and proportionate technical, operational and organisational ... | `R9.1` (chain row) | V | **Accepted R1 (chain row)** | R9.1 |
| `SO-D-08.1-004` | Financial entities develop ICT security awareness programmes and digital operational resilience training as co... | `R9.1` (chain row) | V | **Accepted R1 (chain row)** | R9.1 |
| `PO-D-08.2-001` | The data protection officer monitors compliance with this Regulation, including the assignment of responsibili... | — | — | **No functional carrier** (organizational — DPO compliance monitoring, recorded decision) | — |
| `SO-D-08.2-002` | Where the product with digital elements is intended for integration into other products with digital elements,... | — | — | **N/A** (recorded — inapplicable to this entity/product form) | — |
| `SO-D-08.2-003` | Member States shall encourage essential and important entities to offer similar training to their employees on... | `R9.2` (chain row) | V | **Accepted R1 (chain row)** | R9.2 |
| `SO-D-08.2-004` | Financial entities develop ICT security awareness programmes and digital operational resilience training as co... | `R9.2` (chain row) | V | **Accepted R1 (chain row)** | R9.2 |
| `SO-D-08.2-005` | High-risk AI systems are designed and developed in such a way, including with appropriate human-machine interf... | `R1.3`, `R9.2` (RN22) | TB | **Accepted R1 (RN22)** | RN22 |
| `SO-D-08.3-001` | Member States shall ensure that members of the management bodies of essential and important entities are requi... | `R9.2` (chain row) | V | **Accepted R1 (chain row)** | R9.2 |
| `SO-D-08.3-002` | Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable t... | `R9.2` (chain row) | V | **Accepted R1 (chain row)** | R9.2 |
## D-09 — Governance & Documentation

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-09.1-001` | The controller implements **appropriate technical and organisational measures, such as policies … which are de... | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-002` | An open-source software steward **puts in place and documents in a verifiable manner a cybersecurity policy** ... | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-003` | The management body of essential and important entities **approves the cybersecurity risk-management measures,... | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-004` | The management body of the financial entity **defines, approves, oversees and is responsible for the implement... | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-005` | High-risk AI systems are **designed and developed to ensure that their operation is sufficiently transparent t... | `R1.3`, `R9.2` (RN22) | TB | **Accepted R1 (RN22)** | RN22 |
| `PO-D-09.2-001` | Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the... | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-09.2-002` | The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2)** and updates it as a... | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-09.2-003` | Essential and important entities establish **policies on risk analysis and information system security** (Art.... | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-09.2-004` | Financial entities shall, on a continuous basis, **identify all sources of ICT risk** including risk exposure ... | `R10.2` (RN24) | AS | **Accepted R1 (RN24)** | RN24 |
| `SO-D-09.2-005` | A risk management system is **established, implemented, documented and maintained** in relation to high-risk A... | `R10.2` (RN24) | AS | **Accepted R1 (RN24)** | RN24 |
| `SO-D-09.3-001` | Manufacturers of products with digital elements draw up **technical documentation** containing at least a **ge... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.3-002` | Essential and important entities adopt **access control policies coordinated with human resources security and... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.3-003` | Financial entities **identify, classify and adequately document all ICT supported business functions, the role... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `PO-D-09.4-001` | Each controller and processor **maintains a record of processing activities under its responsibility** (Art. 3... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.4-002` | The manufacturer **draws up before placing a product with digital elements on the market the technical documen... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.4-003` | Member States shall **encourage the use of European or internationally accepted standards and specifications r... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.4-004` | Financial entities **develop and document an information security policy defining rules to protect the availab... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.4-005` | Providers of high-risk AI systems **draw up and keep up-to-date the technical documentation of the high-risk A... | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
## D-10 — Monitoring, Audit & Testing

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-10.1-001` | The controller and processor implement appropriate technical and organisational measures to ensure the **ongoi... | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `SO-D-10.1-002` | A product with digital elements **provides security-related information by recording and monitoring relevant i... | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `SO-D-10.1-003` | Essential and important entities establish an **incident-handling capability** covering prevention, detection,... | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `SO-D-10.1-004` | Financial entities **continuously monitor and control the security and functioning of ICT systems and tools** ... | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `SO-D-10.1-005` | Providers of high-risk AI systems **establish and document a post-market monitoring system in a manner that is... | `R10.2` (RN24) | AS | **Accepted R1 (RN24)** | RN24 |
| `PO-D-10.2-001` | The controller and processor **maintain compliance records in writing or in electronic form with integrity and... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-10.2-002` | The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmonised standards applied... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-10.2-003` | Financial entities **develop and document an information security policy defining rules to protect the availab... | `R11.2` (chain row) | V | **Accepted R1 (chain row)** | R11.2 |
| `SO-D-10.2-004` | Providers of high-risk AI systems ensure the systems **technically allow for the automatic recording of events... | `R1.2`, `R11.2` (RN23) | V | **Accepted R1 (RN23)** | RN23 |
| `PO-D-10.3-001` | The controller and processor implement appropriate technical and organisational measures including **a process... | `R11.3` (chain row) | V | **Accepted R1 (chain row)** | R11.3 |
| `SO-D-10.3-002` | Manufacturers of products with digital elements **carry out effective and regular tests and reviews of the pro... | `R11.3` (chain row) | V | **Accepted R1 (chain row)** | R11.3 |
| `SO-D-10.3-003` | Essential and important entities establish **policies and procedures to assess the effectiveness of cybersecur... | `R11.3` (chain row) | V | **Accepted R1 (chain row)** | R11.3 |
| `SO-D-10.3-004` | Financial entities **establish, maintain and review a sound and comprehensive digital operational resilience t... | `R11.3` (chain row) | V | **Accepted R1 (chain row)** | R11.3 |
| `SO-D-10.3-005` | Providers of high-risk AI systems ensure the systems are **tested for the purpose of identifying the most appr... | `R11.4` (RN25) | AS | **Accepted R1 (RN25)** | RN25 |

## Coverage totals (this matrix)

| Verdict | Count |
|---|---|
| Accepted R1 — RN-carried rows | 36 rows → 16 constraints (RN11–RN26), all accepted |
| Accepted R1 — chain rows on functional cards | 92 |
| No functional carrier (recorded decision) | 2 |
| N/A (recorded) | 4 |
| **Total objectives** | **134** |

Every objective is explicitly placed; none is silent. The high functional coverage reflects a functional baseline that already spans the customer/AI product core and the banking-grade operating functions.
