# Phase 2 Objective Mapping — Exhaustive Coverage Matrix (SecureBorder eGate)

> **Scope:** all 100 Phase 2 objectives (29 `PO-` GDPR · 34 `SO-` CRA · 22 `SO-` NIS 2 · 15 `SO-` AI Act) + the 7 principles (see [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md)).
> **State legend:** `Accepted R1 (RNxx)` = new constraint accepted in Round 1 with this objective as driver · `Accepted R1 (chain row)` = the objective is realized by an existing V0 functional card; the regulatory chain was attached to that card in Round 1 · transversal = umbrella realized by slices · no-carrier/N-A = recorded decisions.
> **Verdicts:** Round 1 CONVERGED (20/20 + 51/51 accepts, 2026-09-28) — per-item verdicts recorded in [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md); nothing enters the baseline silently.

## D-01 — Data Protection & Encryption

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-01.1-001` | Personal data at rest protected with appropriate security | `R1.1`, `R1.3` (RN11) | TB | **Accepted R1 (RN11)** | RN11 |
| `SO-D-01.1-002` | Product data at rest encrypted (state of the art) | `R1.1`, `R1.3` (RN11 co-driver) | TB | **Accepted R1 (RN11 co-driver)** | RN11 |
| `SO-D-01.1-003` | NIS 2 cryptography policies and procedures | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `PO-D-01.2-001` | Personal data in transit confidential and unaltered | all UC preconditions (RN13) | TB | **Accepted R1 (RN13, cross-cutting)** | RN13 |
| `SO-D-01.2-002` | CRA twin: product data in transit encrypted | all UC preconditions (RN13 co-driver) | TB | **Accepted R1 (RN13 co-driver)** | RN13 |
| `PO-D-01.3-001` | Re-identification info kept separate (key separation) | `R1.1`, `R1.2` (RN12) | LP | **Accepted R1 (RN12)** | RN12 |
| `SO-D-01.3-002` | Product key material managed with role separation | `R1.1`, `R1.2` (RN12 co-driver) | LP | **Accepted R1 (RN12 co-driver)** | RN12 |
| `PO-D-01.4-001` | Accuracy + rectification without delay (Art. 16 cascade) | `R4.1` (functional) | V | **Accepted R1 (chain row)** | R4.1 |
| `SO-D-01.4-002` | Integrity of stored/transmitted data, commands, configuration | `R1.2`, `R1.3`, `R6.1` (RN14) | V | **Accepted R1 (RN14)** | RN14 |
| `SO-D-01.4-004` | AI robustness: resilient to errors/faults, redundancy/fail-safe | `R1.2`, `R8.3`, `R9.2` (RN15) | FS | **Accepted R1 (RN15)** | RN15 |

## D-02 — Vulnerability Management

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-02.1-001` | GDPR: regular testing of measures effectiveness + DPIA review | `R7.1` (chain row) | AS | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-02.1-002` | CRA: no known exploitable vulnerabilities; continuing identification | `R7.1` (chain row) | AS | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-02.1-003` | NIS 2: coordinated vulnerability handling in lifecycle | `R7.1` (chain row) | AS | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-02.1-004` | AI Act: risk-management system incl. AI attack-surface risks | `R9.1` (chain row) | AS | **Accepted R1 (chain row)** | R9.1 |
| `SO-D-02.2-002` | CRA: remediation via security updates without delay | `R7.2` (chain row) | AS | **Accepted R1 (chain row)** | R7.2 |
| `SO-D-02.3-002` | CRA: coordinated vulnerability disclosure policy + contact address | `R7.3` (chain row) | AS | **Accepted R1 (chain row)** | R7.3 |
| `SO-D-02.3-003` | NIS 2: disclosure process integrated in lifecycle | `R7.3` (chain row) | AS | **Accepted R1 (chain row)** | R7.3 |
| `SO-D-02.4-002` | CRA: effective and regular security testing with evidence | `R7.1` (chain row) | AS | **Accepted R1 (chain row)** | R7.1 |
| `SO-D-02.4-004` | AI Act: testing for consistent performance + real-world conditions | `R9.3` (chain row) | AS | **Accepted R1 (chain row)** | R9.3 |

## D-03 — Access Control & Identity Management

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-03.1-001` | Rights-requester identity verified proportionately (Art. 12(6)) | `R4.1` (RN16) | TB | **Accepted R1 (RN16)** | RN16 |
| `SO-D-03.1-002` | CRA: product identities/credentials/entitlements verifiably managed | `R3.1`, `R3.3` (RN17 co-driver) | LP | **Accepted R1 (RN17 co-driver)** | RN17 |
| `SO-D-03.1-003` | NIS 2: workforce identity lifecycle (induction/change/separation) | `R3.1` (RN17 driver) | LP | **Accepted R1 (RN17)** | RN17 |
| `PO-D-03.2-001` | Authorized persons act on documented instructions (GDPR) | `R3.3` (RN19 co-driver) | LP | **Accepted R1 (RN19 co-driver)** | RN19 |
| `SO-D-03.2-002` | CRA: protection from unauthorised access via control mechanisms | `R3.2` (RN18 co-driver) | TB | **Accepted R1 (RN18 co-driver)** | RN18 |
| `SO-D-03.2-003` | NIS 2: multi-factor/continuous authentication; secured communications | `R3.2` (RN18 driver) | TB | **Accepted R1 (RN18)** | RN18 |
| `PO-D-03.3-001` | Authorized persons act on documented instructions (confidentiality) | `R3.3` (RN19 co-driver) | LP | **Accepted R1 (RN19 co-driver)** | RN19 |
| `SO-D-03.3-002` | CRA: access limited to authenticated and authorised principals | `R3.3`, `R2.1` (RN19 co-driver) | LP | **Accepted R1 (RN19 co-driver)** | RN19 |
| `SO-D-03.3-003` | NIS 2: entity-level access-control policies | `R3.3` (RN19 co-driver) | LP | **Accepted R1 (RN19 co-driver)** | RN19 |
| `PO-D-03.4-001` | GDPR: by default only necessary personal data processed | `R1.2`, `R8.1` (RN20 co-driver) | FS | **Accepted R1 (RN20 co-driver)** | RN20 |
| `SO-D-03.4-002` | CRA: secure-by-default configuration, resettable | `R1.2`, `R8.1` (RN20 driver) | FS | **Accepted R1 (RN20)** | RN20 |

## D-04 — Incident Response & Notification

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-04.1-001` | GDPR: breach detection/triage; awareness moment documented (72 h) | `R5.2`, `R6.1` (RN26 driver) | V | **Accepted R1 (RN26)** | RN26 |
| `SO-D-04.1-002` | CRA: relevant internal activity recorded and monitored | `R5.1`, `R1.2` (RN22 co-driver) | V | **Accepted R1 (RN22 co-driver)** | RN22 |
| `SO-D-04.1-003` | NIS 2: incident-handling capability (six lifecycle actions) | `R5.2`, `R5.3` (RN23 driver) | AS | **Accepted R1 (RN23)** | RN23 |
| `PO-D-04.2-001` | GDPR: breach containment and mitigation measures | `R5.2` (RN26 co-driver) | V | **Accepted R1 (RN26 co-driver)** | RN26 |
| `SO-D-04.2-002` | CRA: availability of essential functions protected after incident | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.2-003` | NIS 2: incident handling across the full lifecycle | `R5.2` (RN23 co-driver) | AS | **Accepted R1 (RN23 co-driver)** | RN23 |
| `PO-D-04.3-001` | GDPR: breach notification to SA within 72 h | `R6.1` (RN21 co-driver) | V | **Accepted R1 (RN21 co-driver, T-001)** | RN21 |
| `SO-D-04.3-002` | CRA: actively-exploited vulnerability notification (three-tier) | `R6.1` (RN21 co-driver) | V | **Accepted R1 (RN21 co-driver, T-001)** | RN21 |
| `SO-D-04.3-003` | NIS 2: significant incident twin-trigger (24 h / 72 h / 1 month) | `R6.1` (RN21 co-driver) | V | **Accepted R1 (RN21 co-driver, T-001)** | RN21 |
| `SO-D-04.3-004` | AI Act: serious incident report to market surveillance | `R6.1` (RN21 co-driver) | V | **Accepted R1 (RN21 co-driver, T-001)** | RN21 |
| `PO-D-04.4-001` | GDPR: ongoing CIA + resilience of processing systems | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.4-002` | CRA: availability protected also after an incident | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-04.4-003` | NIS 2: continuity, backup, disaster recovery, crisis management | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |

## D-05 — Data Lifecycle

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | GDPR: minimization — adequate, relevant, necessary only | `R1.1` (functional: raw capture discarded; chain row) | DM | **Accepted R1 (chain row)** | R1.1 |
| `SO-D-05.1-002` | CRA: product data limited to what is necessary | `R1.1` (chain row) | DM | **Accepted R1 (chain row)** | R1.1 |
| `SO-D-05.1-004` | AI Act: training/validation/test data governance (Art. 10) | `R9.1` (chain row) | DM | **Accepted R1 (chain row)** | R9.1 |
| `PO-D-05.2-001` | GDPR: retention no longer than necessary | `R1.1`, `R4.1` (chain row) | LE | **Accepted R1 (chain row)** | R1.1, R4.1 |
| `SO-D-05.2-002` | CRA: updates and advisories available across support period | `R7.2` (RN27 co-driver) | AS | **Accepted R1 (RN27 co-driver)** | RN27 |
| `SO-D-05.2-004` | AI Act: Art. 12(1) logs kept ≥ 6 months, supplied on demand | `R1.2`, `R9.2` (RN24 co-driver) | V | **Accepted R1 (RN24 co-driver, T-002)** | RN24 |
| `PO-D-05.3-001` | GDPR: erasure without undue delay (Art. 17 grounds a–f) | `R4.1` (RN28 co-driver) | LE | **Accepted R1 (RN28 co-driver, T-002)** | RN28 |
| `SO-D-05.3-002` | CRA: user can permanently remove all product data/settings | `R4.1` (chain row) | LE | **Accepted R1 (chain row)** | R4.1 |
| `PO-D-05.4-001` | GDPR: portability — structured, machine-readable, free of charge | `R4.1` (RN28 co-driver) | LE | **Accepted R1 (RN28 co-driver)** | RN28 |

## D-06 — Supply Chain & Third-Party Security

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-06.1-001` | GDPR: processors provide sufficient guarantees (Art. 28) | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-06.1-002` | CRA: due diligence on third-party/open-source components | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-06.1-003` | NIS 2: direct supplier security measures (Art. 21(2)-(3)) | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-06.2-002` | CRA: SBOM maintained, machine-readable | `R8.2` (chain row) | V | **Accepted R1 (chain row)** | R8.2 |
| `PO-D-06.3-001` | GDPR: processor contract floor (Art. 28(3)(a)-(h)) | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-06.3-002` | CRA: importer/distributor economic-operator duties | — | — | **N/A** (manufacturer places its own product; no importer/distributor chain) | — |
| `SO-D-06.3-003` | NIS 2: supplier contractual security + three-prong assessment | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `PO-D-06.4-001` | GDPR: EU representative for non-EU controllers (Art. 27) | — | — | **N/A** (EU-established controller/processor) | — |
| `SO-D-06.4-002` | CRA: non-EU manufacturer boundary management | — | — | **N/A** (EU manufacturer) | — |
| `SO-D-06.4-003` | NIS 2: cross-border incident routing (multi-Member-State) | `R6.1` (chain row) | V | **Accepted R1 (chain row)** | R6.1 |

## D-07 — Secure Development & AI Design

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-07.1-001` | GDPR: DPbD technical/organisational measures (umbrella) | transversal (RN11, RN20 realize slices) | DM | **Covered (transversal)** — chains via RN11/RN20 | — |
| `SO-D-07.1-002` | CRA: Annex I essential requirements design umbrella | transversal (RN14, RN27, R8.1 chains) | AS | **Covered (transversal umbrella)** | — |
| `SO-D-07.1-003` | NIS 2: security in acquisition, development, maintenance | `R10.2` (chain row) | V | **Accepted R1 (chain row)** | R10.2 |
| `SO-D-07.1-004` | AI Act: accuracy/robustness/cybersecurity by design (Art. 15) | `R9.1` (chain row) | AS | **Accepted R1 (chain row)** | R9.1 |
| `SO-D-07.2-002` | CRA: attack surfaces limited (incl. external components) | `R8.1` (chain row) | AS | **Accepted R1 (chain row)** | R8.1 |
| `SO-D-07.2-004` | AI Act: resistance to adversarial attacks (Art. 15(4)-(5)) | `R9.3` (chain row) | AS | **Accepted R1 (chain row)** | R9.3 |
| `SO-D-07.3-002` | CRA: secure, timely update distribution incl. automatic where appropriate | `R7.2` (RN27 driver) | AS | **Accepted R1 (RN27)** | RN27 |
| `SO-D-07.3-003` | NIS 2: security in maintenance and repair | `R7.1` (chain row) | AS | **Accepted R1 (chain row)** | R7.1 |

## D-08 — Human Factors & Oversight

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-08.1-001` | GDPR: DPO informs and advises on obligations | — | — | **No functional carrier** (organizational — DPO activity, recorded decision) | — |
| `SO-D-08.1-002` | CRA: secure-use instructions (commissioning + lifetime) | `R7.2` (chain row: advisory messages) | V | **Accepted R1 (chain row)** | R7.2 |
| `SO-D-08.1-003` | NIS 2: basic cyber hygiene practice | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `PO-D-08.2-001` | GDPR: DPO monitors compliance, awareness, training | — | — | **No functional carrier** (organizational — DPO activity, recorded decision) | — |
| `SO-D-08.2-002` | CRA: integration information for products integrating this product | — | — | **N/A** (product not offered for integration into other products) | — |
| `SO-D-08.2-003` | NIS 2: regular employee training encouragement | `R11.1` (chain row) | V | **Accepted R1 (chain row)** | R11.1 |
| `SO-D-08.2-004` | AI Act: effective human oversight (Art. 14), competence + interface | `R2.1`, `R11.2` (RN29) | TB | **Accepted R1 (RN29)** | RN29 |

## D-09 — Governance & Documentation

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-09.1-001` | GDPR: policies implementing data-protection principles (Art. 24) | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-002` | CRA: open-source software steward cybersecurity policy | — | — | **N/A** (SecureBorder is not an open-source steward) | — |
| `SO-D-09.1-003` | NIS 2: management body approves and oversees risk measures | `R10.1` (chain row) | V | **Accepted R1 (chain row)** | R10.1 |
| `SO-D-09.1-004` | AI Act: transparency for deployers to interpret output (Art. 13) | `R9.3` (RN30) | V | **Accepted R1 (RN30)** | RN30 |
| `PO-D-09.2-001` | GDPR: DPIA before high-risk processing (Art. 35) | `R10.1` (chain row, T-003) | V | **Proposal R1 (chain row, T-003)** | R10.1 |
| `SO-D-09.2-002` | CRA: cybersecurity risk assessment documented + updated (Art. 13(2)) | `R10.1` (chain row, T-003) | V | **Proposal R1 (chain row, T-003)** | R10.1 |
| `SO-D-09.2-003` | NIS 2: continuous risk-analysis policies | `R10.1` (chain row, T-003) | V | **Proposal R1 (chain row, T-003)** | R10.1 |
| `SO-D-09.2-004` | AI Act: risk-management system established and maintained (Art. 9) | `R10.1`, `R9.1` (chain row, T-003) | V | **Proposal R1 (chain row, T-003)** | R10.1, R9.1 |
| `PO-D-09.4-001` | GDPR: records of processing activities (Art. 30) | `R4.2` (functional — the card is the RoPA function) | V | **Accepted R1 (chain row)** | R4.2 |
| `SO-D-09.4-002` | CRA: technical documentation before placing on market (Art. 13) | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-09.4-003` | NIS 2: Member States encourage use of standards | — | — | **N/A** (addressee: Member States) | — |
| `SO-D-09.4-004` | AI Act: Annex IV technical documentation before conformity | `R9.1` (chain row) | V | **Accepted R1 (chain row)** | R9.1 |

## D-10 — Monitoring, Audit & Testing

| Objective | Summary | Functional carrier | Skill | State vs V0 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-10.1-001` | GDPR: ongoing CIA + resilience of processing systems | `R5.3` (chain row) | FS | **Accepted R1 (chain row)** | R5.3 |
| `SO-D-10.1-002` | CRA: product records and monitors relevant internal activity | `R5.1`, `R1.2` (RN22 driver) | V | **Accepted R1 (RN22)** | RN22 |
| `SO-D-10.1-003` | NIS 2: incident-handling capability (entity systems) | `R5.2`, `R5.3` (RN23 co-driver) | AS | **Accepted R1 (RN23 co-driver)** | RN23 |
| `SO-D-10.1-004` | AI Act: post-market monitoring system (Art. 72) | `R9.2`, `R5.1` (RN25) | AS | **Accepted R1 (RN25)** | RN25 |
| `PO-D-10.2-001` | GDPR: compliance records with integrity and traceability | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-10.2-002` | CRA: technical documentation maintained across support period | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-10.2-004` | AI Act: automatic event logging over lifetime (Art. 12) | `R1.2`, `R9.2` (RN24 driver) | V | **Accepted R1 (RN24, T-002)** | RN24 |
| `PO-D-10.3-001` | GDPR: regular testing/assessment of measures (D-10 slice) | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-10.3-002` | CRA: effective and regular product testing; reports in documentation | `R9.3`, `R7.1` (chain row) | V | **Accepted R1 (chain row)** | R9.3, R7.1 |
| `SO-D-10.3-003` | NIS 2: policies to assess effectiveness of risk measures | `R10.3` (chain row) | V | **Accepted R1 (chain row)** | R10.3 |
| `SO-D-10.3-004` | AI Act: testing to identify targeted risk-management measures | `R9.3` (chain row) | V | **Accepted R1 (chain row)** | R9.3 |

## Coverage totals (this matrix)

| Verdict | Count |
|---|---|
| Accepted via new constraint (RN-carried rows) | 39 rows → 20 constraints (RN11–RN30), all accepted R1 |
| Accepted chain row on existing functional card | 51 |
| Transversal umbrella | 2 |
| No functional carrier (recorded decision) | 2 |
| N/A (requirement type inapplicable) | 6 |
| **Total objectives** | **100** |

Every objective is explicitly placed; none is silent. The high coverage rate reflects the V0 elicitation for a RIGOROUS-tier essential entity whose functional set already includes the operational capabilities (monitoring, incident, vulnerability, SBOM, governance, training) that lighter products leave organizational.
