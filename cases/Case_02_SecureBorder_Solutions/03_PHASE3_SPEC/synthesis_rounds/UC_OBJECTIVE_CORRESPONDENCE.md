# UC ↔ Phase 2 Objective Correspondence Matrix (SecureBorder eGate)

> **Scope:** all 28 Level-1 use cases; per-UC cards list the objectives binding there, the regulation (`Reg`), the carrying constraint or chain row, and the Round-1 state. Regulation-tagged per the Phase 2 ambit (GDPR personal data · CRA product · NIS 2 entity · AI Act high-risk AI).
> **Verdicts:** Round 1 CONVERGED (20/20 + 51/51 accepts, 2026-09-28) — see [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md).

## §1 Correspondence Grid (objective-family × UC area)

| Area | GDPR | CRA | NIS 2 | AI Act |
|---|---|---|---|---|
| R1 biometric verification | RN11, RN12, RN13, RN16*, RN28* | RN11, RN13, RN14, RN15, RN20, RN22, RN24, chains | — | RN15, RN24 |
| R2 oversight | — | RN19 | RN18 | RN29 |
| R3 identity & access | RN19 | RN17, RN18, RN19, RN20 | RN17, RN18, RN19 | — |
| R4 traveller rights | RN16, RN28, chains | chains | — | — |
| R5 monitoring & incidents | RN26, chains | RN22, chains | RN23, chains | RN25 |
| R6 notifications | RN21, RN26 | RN14, RN21, chains | RN21, chains | RN21 |
| R7 vulnerabilities & updates | chains | RN27, chains | chains | — |
| R8 secure development | — | RN20, chains | — | RN15 |
| R9 AI governance | — | chains | — | RN24, RN25, RN29, RN30, chains |
| R10 governance & vendors | chains | chains | chains | chains |
| R11 training | — | chains | chains | RN29 |

*RN16/RN28 are traveller-facing (data subjects), listed in R1/R4 flows.

## §2 Per-UC Correspondence Cards

### `{U.C. 1.1}` Enrol traveller biometric reference

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | GDPR | Only template extracted; raw capture discarded immediately (V0 functional) | DM | chain | Covered (functional + chain row proposed) |
| `SO-D-05.1-002` | CRA | Product data limited to what is necessary for the intended purpose | DM | chain | Chain row accepted R1 |
| `PO-D-01.1-001` | GDPR | Stored template encrypted at rest | TB | RN11 | Accepted R1 |
| `SO-D-01.1-002` | CRA | Product data at rest encrypted (state of the art) | TB | RN11 | Accepted R1 (co-driver) |
| `PO-D-01.3-001` | GDPR | De-linking key material under separated custody | LP | RN12 | Accepted R1 |
| `SO-D-01.3-002` | CRA | Product key material with role separation | LP | RN12 | Accepted R1 (co-driver) |
| `PO-D-05.2-001` | GDPR | Templates retained no longer than necessary | LE | chain | Chain row accepted R1 |
| `SO-D-03.4-002` | CRA | Enrolment configuration starts restrictive | FS | RN20 | Accepted R1 |

### `{U.C. 1.2}` Perform biometric verification and gate decision

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-01.2-001` | GDPR | Verification flows confidential and unaltered in transit | TB | RN13 | Accepted R1 (cross-cutting) |
| `SO-D-01.2-002` | CRA | Transit encryption on gate↔back-office channel | TB | RN13 | Accepted R1 (co-driver) |
| `SO-D-01.4-002` | CRA | Gate decisions and commands integrity-protected | V | RN14 | Accepted R1 |
| `SO-D-01.4-004` | AI Act | Resilience to errors/faults; fail-safe gate state | FS | RN15 | Accepted R1 |
| `SO-D-10.2-004` | AI Act | Automatic event logging over lifetime (T-002 leg) | V | RN24 | Accepted R1 |
| `SO-D-04.1-002` | CRA | Relevant internal activity recorded and monitored | V | RN22 | Accepted R1 (co-driver) |
| `SO-D-03.4-002` | CRA | Verification configuration starts restrictive, resettable | FS | RN20 | Accepted R1 |

### `{U.C. 1.3}` Consult traveller passage decision records

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-01.1-001` | GDPR | Decision records encrypted at rest | TB | RN11 | Accepted R1 |
| `SO-D-01.4-002` | CRA | Records integrity-protected; corruption reported | V | RN14 | Accepted R1 |

### `{U.C. 2.1}` Review and override automated decisions

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-03.3-002` | CRA | Override restricted to authorized overseers | LP | RN19 | Accepted R1 |
| `SO-D-08.2-004` | AI Act | Oversight effective: authority to intervene/suspend/reverse (Art. 14) | TB | RN29 | Accepted R1 |

### `{U.C. 2.2}` Manage manual-lane referrals

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-03.2-003` | NIS 2 | Referral handling under authenticated operator sessions | TB | RN18 | Accepted R1 |

### `{U.C. 3.1}` Manage operator identity lifecycle

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-03.1-003` | NIS 2 | Provisioning on induction, review on change, revocation on separation | LP | RN17 | Accepted R1 |
| `SO-D-03.1-002` | CRA | Product-side identities/entitlements verifiably managed | LP | RN17 | Accepted R1 (co-driver) |

### `{U.C. 3.2}` Authenticate operators with multi-factor verification

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-03.2-003` | NIS 2 | MFA/continuous authentication per policy | TB | RN18 | Accepted R1 |
| `SO-D-03.2-002` | CRA | Control mechanisms against unauthorised access | TB | RN18 | Accepted R1 (co-driver) |

### `{U.C. 3.3}` Assign and review operational access roles

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-03.2-001` | GDPR | Authorized persons act on documented instructions only | LP | RN19 | Accepted R1 |
| `SO-D-03.3-002` | CRA | Access limited to authenticated, authorised principals | LP | RN19 | Accepted R1 (co-driver) |
| `SO-D-03.3-003` | NIS 2 | Entity-level access-control policies applied | LP | RN19 | Accepted R1 (co-driver) |

### `{U.C. 4.1}` Process traveller data-subject requests

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-03.1-001` | GDPR | Requester identity verified before execution (Art. 12(6)) | TB | RN16 | Accepted R1 |
| `PO-D-05.3-001` | GDPR | Erasure without undue delay; key material destroyed (T-002) | LE | RN28 | Accepted R1 |
| `PO-D-05.4-001` | GDPR | Structured, machine-readable portability export | LE | RN28 | Accepted R1 (co-driver) |
| `PO-D-01.4-001` | GDPR | Rectification cascade (Art. 16 + Art. 19) | V | chain | Chain row accepted R1 |
| `SO-D-05.3-002` | CRA | Permanent removal of product data/settings on request | LE | chain | Chain row accepted R1 |

### `{U.C. 4.2}` Maintain records of processing activities

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-09.4-001` | GDPR | Art. 30 records maintained under responsibility | V | chain | Chain row accepted R1 |

### `{U.C. 5.1}` Collect and correlate fleet security events

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-10.1-002` | CRA | Product records and monitors relevant internal activity | V | RN22 | Accepted R1 |
| `SO-D-10.1-004` | AI Act | Post-market monitoring data ingested (Art. 72) | AS | RN25 | Accepted R1 |

### `{U.C. 5.2}` Triage and manage incidents

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-04.1-001` | GDPR | Awareness moment documented; 72 h clock anchored | V | RN26 | Accepted R1 |
| `PO-D-04.2-001` | GDPR | Containment/mitigation measures recorded | V | RN26 | Accepted R1 (co-driver) |
| `SO-D-04.1-003` | NIS 2 | Incident handling across the six lifecycle actions | AS | RN23 | Accepted R1 |
| `SO-D-04.2-003` | NIS 2 | Full lifecycle closure with CSIRT-ready evidence | AS | RN23 | Accepted R1 (co-driver) |

### `{U.C. 5.3}` Recover services and exercise continuity

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-04.2-002` | CRA | Availability of essential functions protected after incident | FS | chain | Chain row accepted R1 |
| `SO-D-04.4-002` | CRA | Resilience/mitigation measures on the fleet | FS | chain | Chain row accepted R1 |
| `SO-D-04.4-003` | NIS 2 | Continuity, backup, disaster recovery, crisis management | FS | chain | Chain row accepted R1 |
| `PO-D-04.4-001` | GDPR | Ongoing CIA + resilience of processing systems | FS | chain | Chain row accepted R1 |
| `PO-D-10.1-001` | GDPR | CIA + resilience measures (entity leg) | FS | chain | Chain row accepted R1 |

### `{U.C. 6.1}` Execute unified regulatory notifications

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-04.3-001` | GDPR | Breach notification within 72 h | V | RN21 | Accepted R1 (co-driver, T-001) |
| `SO-D-04.3-002` | CRA | Actively-exploited vulnerability notification (three-tier) | V | RN21 | Accepted R1 (co-driver, T-001) |
| `SO-D-04.3-003` | NIS 2 | Significant incident twin-trigger (24 h/72 h/1 month) | V | RN21 | Accepted R1 (co-driver, T-001) |
| `SO-D-04.3-004` | AI Act | Serious-incident report per the AI Act matrix | V | RN21 | Accepted R1 (co-driver, T-001) |
| `SO-D-06.4-003` | NIS 2 | Cross-border incident routing (multi-Member-State) | V | chain | Chain row accepted R1 |
| `SO-D-01.4-002` | CRA | Notification dossiers integrity-protected | V | RN14 | Accepted R1 |

### `{U.C. 7.1}` Identify and remediate vulnerabilities

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-02.1-002` | CRA | Continuing vulnerability identification incl. SBOM components | AS | chain | Chain row accepted R1 |
| `SO-D-02.1-003` | NIS 2 | Coordinated vulnerability handling in the lifecycle | AS | chain | Chain row accepted R1 |
| `PO-D-02.1-001` | GDPR | Regular testing/assessment of measures effectiveness | AS | chain | Chain row accepted R1 |
| `SO-D-02.4-002` | CRA | Effective and regular security testing with evidence | AS | chain | Chain row accepted R1 |
| `SO-D-07.3-003` | NIS 2 | Security in maintenance and repair | AS | chain | Chain row accepted R1 |
| `SO-D-10.3-002` | CRA | Regular product testing; reports kept | V | chain | Chain row accepted R1 |

### `{U.C. 7.2}` Distribute signed software and model updates

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-07.3-002` | CRA | Secure, timely update distribution incl. automatic where appropriate | AS | RN27 | Accepted R1 |
| `SO-D-02.2-002` | CRA | Remediation via security updates without delay | AS | RN27 | Accepted R1 (co-driver) |
| `SO-D-05.2-002` | CRA | Updates and advisories available across the support period | AS | RN27 | Accepted R1 (co-driver) |
| `SO-D-08.1-002` | CRA | Advisory messages / secure-use instructions to users | V | chain | Chain row accepted R1 |

### `{U.C. 7.3}` Operate coordinated vulnerability disclosure

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-02.3-002` | CRA | CVD policy, disclosure duties, contact address | AS | chain | Chain row accepted R1 |
| `SO-D-02.3-003` | NIS 2 | Disclosure process integrated in the lifecycle | AS | chain | Chain row accepted R1 |

### `{U.C. 8.1}` Enforce release pipeline security gates

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-07.1-002` | CRA | Annex I essential requirements umbrella (design/production) | AS | chain | Chain row accepted R1 |
| `SO-D-07.2-002` | CRA | Attack surfaces limited (incl. external components) | AS | chain | Chain row accepted R1 |
| `SO-D-03.4-002` | CRA | Artifacts born with secure-by-default configuration | FS | RN20 | Accepted R1 |

### `{U.C. 8.2}` Maintain software bills of materials

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-06.2-002` | CRA | SBOM maintained, machine-readable, commonly accepted format | V | chain | Chain row accepted R1 |

### `{U.C. 8.3}` Version and roll back AI models

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-01.4-004` | AI Act | Rollback to last verified model version on fault | FS | RN15 | Accepted R1 |

### `{U.C. 9.1}` Maintain AI risk management and conformity documentation

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-02.1-004` | AI Act | Risk-management system incl. AI attack-surface risks (Art. 9+15) | AS | chain | Chain row accepted R1 |
| `SO-D-05.1-004` | AI Act | Training/validation/test data governance (Art. 10) | DM | chain | Chain row accepted R1 |
| `SO-D-07.1-004` | AI Act | Accuracy/robustness/cybersecurity by design (Art. 15) | AS | chain | Chain row accepted R1 |
| `SO-D-09.4-004` | AI Act | Annex IV technical documentation before conformity | V | chain | Chain row accepted R1 |
| `SO-D-09.2-004` | AI Act | Risk-management file established and maintained (T-003 leg) | V | chain | Chain row accepted R1 |

### `{U.C. 9.2}` Monitor AI accuracy, drift, and bias

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-10.2-004` | AI Act | Automatic event logging feeds monitoring (T-002 leg) | V | RN24 | Accepted R1 |
| `SO-D-10.1-004` | AI Act | Post-market monitoring loop into the risk system (Art. 72) | AS | RN25 | Accepted R1 |
| `SO-D-01.4-004` | AI Act | Degradation detection triggers fail-safe/rollback | FS | RN15 | Accepted R1 |

### `{U.C. 9.3}` Test AI systems adversarially and explain decisions

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-09.1-004` | AI Act | Transparency for deployers to interpret output (Art. 13) | V | RN30 | Accepted R1 |
| `SO-D-08.2-004` | AI Act | Interpretability sustaining human oversight (Art. 14) | TB | RN29 | Accepted R1 |
| `SO-D-02.4-004` | AI Act | Testing for consistent performance + real-world conditions (Art. 9(6)/(7)) | AS | chain | Chain row accepted R1 |
| `SO-D-07.2-004` | AI Act | Resistance to adversarial attacks (Art. 15(4)-(5)) | AS | chain | Chain row accepted R1 |
| `SO-D-10.3-004` | AI Act | Testing for targeted risk-management measures | V | chain | Chain row accepted R1 |

### `{U.C. 10.1}` Maintain unified impact and risk assessments

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-09.2-001` | GDPR | DPIA before high-risk processing (T-003 unified pass) | V | chain | Chain row accepted R1 |
| `SO-D-09.2-002` | CRA | Cybersecurity risk assessment documented + updated | V | chain | Chain row accepted R1 |
| `SO-D-09.2-003` | NIS 2 | Continuous risk-analysis policies | V | chain | Chain row accepted R1 |
| `SO-D-09.2-004` | AI Act | AI risk-management system (T-003 unified pass) | V | chain | Chain row accepted R1 |
| `PO-D-09.1-001` | GDPR | Policies implementing data-protection principles (Art. 24) | V | chain | Chain row accepted R1 |
| `SO-D-09.1-003` | NIS 2 | Management-body approval and oversight of measures | V | chain | Chain row accepted R1 |
| `SO-D-01.1-003` | NIS 2 | Cryptography-use policies and procedures | V | chain | Chain row accepted R1 |

### `{U.C. 10.2}` Assess vendors and record component provenance

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `PO-D-06.1-001` | GDPR | Processor due diligence (Art. 28 guarantees) | V | chain | Chain row accepted R1 |
| `PO-D-06.3-001` | GDPR | Processor contract floor (Art. 28(3)(a)-(h)) | V | chain | Chain row accepted R1 |
| `SO-D-06.1-002` | CRA | Third-party/open-source component due diligence | V | chain | Chain row accepted R1 |
| `SO-D-06.1-003` | NIS 2 | Direct supplier security measures (Art. 21(2)-(3)) | V | chain | Chain row accepted R1 |
| `SO-D-06.3-003` | NIS 2 | Supplier contractual security + three-prong assessment | V | chain | Chain row accepted R1 |
| `SO-D-07.1-003` | NIS 2 | Security in acquisition, development, maintenance | V | chain | Chain row accepted R1 |

### `{U.C. 10.3}` Maintain compliance reporting and audits

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-09.4-002` | CRA | Technical documentation before placing on market (Art. 13) | V | chain | Chain row accepted R1 |
| `SO-D-10.2-002` | CRA | Documentation maintained across the support period | V | chain | Chain row accepted R1 |
| `PO-D-10.2-001` | GDPR | Compliance records with integrity and traceability | V | chain | Chain row accepted R1 |
| `SO-D-10.3-003` | NIS 2 | Effectiveness-assessment policies for risk measures | V | chain | Chain row accepted R1 |
| `PO-D-10.3-001` | GDPR | Regular testing/assessment of measures (D-10 slice) | V | chain | Chain row accepted R1 |

### `{U.C. 11.1}` Deliver security and privacy awareness training

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-08.1-003` | NIS 2 | Basic cyber hygiene practices | V | chain | Chain row accepted R1 |
| `SO-D-08.2-003` | NIS 2 | Regular employee training | V | chain | Chain row accepted R1 |

### `{U.C. 11.2}` Deliver oversight and AI competence training

| Objective | Reg | What it demands here | Skill | Carrier | State |
|---|---|---|---|---|---|
| `SO-D-08.2-004` | AI Act | Oversight competence sustaining effective human mediation (Art. 14) | TB | RN29 | Accepted R1 |

## §3 Coverage Totals

| Surface | Count | Notes |
|---|---|---|
| UC cards | 28/28 | every use case has an explicit correspondence section; none silent |
| Objective bindings in per-UC cards | 101 | objectives bind on multiple UCs; unique-objective coverage totals in [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) |
| New constraints proposed | 20 (RN11–RN30) | plus 51 chain rows on functional carriers |

**Read rule:** every binding traces to a chain satisfying the anchor-integrity rule (anchors ∈ the cited objective's published control set or store-flagged); all bindings accepted in Round 1 and applied in Doc01/Doc02 2.0.0; verdicts recorded in [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md).
