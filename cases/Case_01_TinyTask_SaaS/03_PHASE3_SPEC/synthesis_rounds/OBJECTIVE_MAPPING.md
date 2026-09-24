# Phase 2 Objective Mapping — Exhaustive Coverage Matrix (TinyTask SaaS)

> **Purpose:** Conformant Step 2 output (manual Step 2 item 4; ADR-005): **every** Phase 2 objective and principle with an explicit verdict against the functional model, so a reviewer can judge whether each placement makes sense. This matrix is what the Step 3 rounds negotiate.
> **Source of objectives/principles/anchors:** `../../02_PHASE2_RULES/Doc01_Operational_Objectives.md` (published control set = final column) + `Doc02_Secure_Design_Principles.md`.
> **State legend:** `Covered (RNx)` = applied in V1 by the named requirement(s) · `Partial` = applied but chain driver/anchors need the listed adjustment · `Proposed R1 (P-xx / ADJ-x)` = new constraint or re-drive awaiting a client verdict in the register · `No functional carrier` = recorded decision (organizational/process control per ADR-002; not a product requirement) · `Design guidance` = constrains the design, deferred to architecture/Phase 4 context · `N/A` = requirement type not applicable to a SaaS product.
> **Skills (analysis lens):** AS = attack-surface-analysis · TB = trust-boundary-analysis · LP = least-privilege-analysis · FS = fail-safe-defaults-analysis · V = verifiability-analysis · DM = data-minimization-analysis · LE = lifecycle-erasure-analysis.
> **Recalibration note:** chains previously citing phantom `PO-D-06.1/2-001` and `PO-D-03.1-001` were remapped to the real objectives below (STEP7 §3); anchors corrected to each cited objective's published set.

---

## D-01 — Data Protection

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-01.1-001` | Personal data at rest processed with appropriate security | `R1.2` (profile records) | TB | **Covered (RN23)** — anchors match published set | — |
| `SO-D-01.1-002` | Data at rest encrypted with state-of-the-art mechanisms | `R1.1`, `R1.3`, `R7.1`, `R7.2` | TB | **Covered (RN10, RN15, RN23)** — RN10 anchor set corrected R0-recal | — |
| `PO-D-01.2-001` | Personal data in transit confidential and unaltered | `R1.1`, all UC preconditions | TB | **Covered (RN24)** — anchors match | — |
| `SO-D-01.2-002` | CRA twin: data in transit encrypted (state of the art) | `R1.1`, all UC preconditions | TB | **Proposed R1 (ADJ-9)** — add CRA twin driver to RN24's chain | ADJ-9 |
| `PO-D-01.3-001` | Re-identification info kept separate (key separation) | — (design constraint) | — | **Design guidance** | design/Phase 4 context |
| `SO-D-01.3-002` | Cryptographic keys and auth material managed/protected | — (design constraint) | — | **Design guidance** | design/Phase 4 context |
| `PO-D-01.4-001` | Accuracy + rectification without delay | `R1.2` (profile editing) | V | **Covered** (D3 elevation, STEP5 CH-04) | — |
| `SO-D-01.4-002` | Integrity of stored/transmitted data, commands, configuration | `R7.1`, `R7.2` (billing state), `R6.2` (webhook messages) | V | **Proposed R1 (ADJ-7, ADJ-8)** — re-drive RN15/RN16 to this integrity objective | ADJ-7, ADJ-8 |

## D-02 — Vulnerability Management

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-02.1-001` | Process: regularly test effectiveness of measures | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-02.1-002` | Product free of known exploitable vulnerabilities; SBOM-correlated identification | — (release/dependency practice) | AS | **No functional carrier** (organizational/dev-process) — *was wrongly driving RN9/RN10/RN12/RN17; chains re-anchored, re-drives proposed* | ADJ-1…ADJ-4 |
| `SO-D-02.2-002` | Vulnerabilities remediated via security updates; secure distribution | — (deployment practice) | — | **No functional carrier** (organizational/dev-process) — *was wrongly driving RN11; re-drive proposed* | ADJ-2 |
| `SO-D-02.3-002` | Coordinated vulnerability disclosure policy | — | — | **No functional carrier** (organizational policy) | — |

## D-03 — Access Control

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-03.1-001` | Verify identity of data-subject rights requests (Art. 15–22) | `R8.1`, `R8.2` | TB | **Proposed R1 (P-01)** — identity verification before export/erasure execution | P-01 |
| `SO-D-03.1-002` | Identities, credentials, entitlements managed in a verified way | `R1.1`, `R2.2` (credentials, roles) | LP | **Partial → Proposed R1 (ADJ-2)** — RN11 re-drive here; RN10/RN12 to gain it as co-driver | ADJ-2 |
| `SO-D-03.2-001` | Authorized persons act on documented instructions (GDPR side) | — | — | **No functional carrier** (organizational) | — |
| `SO-D-03.2-002` | Protection from unauthorised access via control mechanisms (CRA 2)(d) home | `R2.1`, `R3.1` (tenant isolation) | TB | **Partial → Proposed R1 (ADJ-1)** — RN9 re-drive here from SO-D-02.1-002 | ADJ-1 |
| `SO-D-03.3-001` | Processor-side documented instructions + confidentiality | — | — | **No functional carrier** (organizational) | — |
| `SO-D-03.3-002` | Access limited to authenticated and authorized users/services | `R2.2` (RBAC) | LP | **Partial → Proposed R1 (ADJ-3)** — RN12 re-drive here from SO-D-02.1-002 | ADJ-3 |
| `SO-D-03.4-001` | By default only necessary personal data processed | `R1.1` (registration form) | DM | **Covered (RN19)** — after PO recalibration | — |
| `SO-D-03.4-002` | Secure-by-default configuration, resettable by user | `R2.1`, `R3.1` (defaults) | FS | **Proposed R1 (P-02)** — restrictive secure defaults on new artifacts | P-02 |

## D-04 — Incident Response

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-04.1-001` | Breach detection/triage, awareness moment documented (72 h) | — (process; supported by RN18 logs) | — | **No functional carrier** (organizational process) | — |
| `SO-D-04.1-002` | Relevant internal activity recorded (access/modification) | `R6.1` (audit feed) | V | **Partial → Proposed R1 (ADJ-5 alt)** — RN18 co-driver candidate alongside SO-D-10.1-002 | ADJ-5 |
| `SO-D-04.2-001` | Breach containment/mitigation measures | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-04.2-002` | Availability of essential functions protected after incident | — (ops; RN5 backups adjacent) | — | **No functional carrier** (organizational/ops; RN5 covers the V0 functional slice) | — |
| `SO-D-04.3-001` | Breach notified to supervisory authority (72 h) | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-04.3-002` | Actively-exploited vulnerability notified (3-tier timeline) | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-04.4-001` | Ongoing CIA + resilience of processing systems ensured | — (ops) | — | **No functional carrier** (organizational/ops; RN2/RN5 cover the V0 slice) | — |
| `SO-D-04.4-002` | Recovery measures with defined RPO | `RN5` (V0, W1) | — | **Covered (RN5, V0 slice)** | — |

## D-05 — Data Lifecycle

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | Minimization + purpose limitation (adequate, relevant, necessary) | `R1.1` (registration), `R2.3`/`R6.1` (activity data) | DM | **Covered (RN19, RN22)** — recalibrated from phantom PO-D-06.1-001 | — |
| `SO-D-05.1-002` | CRA twin: product data limited to what is necessary | `R1.1`, `R5.1` (lifecycle) | DM | **Covered (RN19, RN25)** — was wrongly driving RN16/RN17; those re-driven (ADJ-4, ADJ-7) | ADJ-4, ADJ-7 |
| `PO-D-05.2-001` | Retention no longer than necessary | `R5.1` (attachments) | LE | **Covered (RN25)** — recalibrated from phantom PO-D-06.1-001 | — |
| `SO-D-05.2-002` | Updates/advisories available across support period | — | — | **No functional carrier** (organizational/support process) | — |
| `PO-D-05.3-001` | Erasure without undue delay on request (Art. 17) | `R8.2` | LE | **Covered (RN21)** — recalibrated from phantom PO-D-06.2-001 | — |
| `SO-D-05.3-002` | User can permanently remove all data and settings of the product | `R8.2` (account) — **gap: workspace-level deletion missing** | LE | **Proposed R1 (P-03)** — Owner workspace deletion with permanent erasure | P-03 |
| `PO-D-05.4-001` | Portability: structured, machine-readable, free of charge | `R8.1` | LE | **Covered (RN20)** — recalibrated from phantom PO-D-06.2-001 | — |

## D-06 — Supply Chain & Third-Party Security

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-06.1-001` | Processors provide sufficient guarantees (GDPR Art. 28) | — | — | **No functional carrier** (organizational/procurement) | — |
| `SO-D-06.1-002` | Due diligence on third-party/open-source components | — | — | **No functional carrier** (organizational/dev-process) | — |
| `SO-D-06.2-002` | SBOM maintained, machine-readable | — | — | **No functional carrier** (organizational/dev-process) | — |
| `SO-D-06.3-001` | Art. 28(3)(a)–(h) contract floor + sub-processor chain | — | — | **No functional carrier** (organizational/contracts) | — |
| `SO-D-06.3-002` | Economic-operator contractual duties (importers/distributors) | — | — | **N/A** (no distribution chain for a SaaS service) | — |

## D-07 — Secure Development

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-07.1-001` | DPbD technical/organisational measures (pseudonymisation…) | transversal (RN19/RN23 realize slices) | DM | **Covered (transversal)** | — |
| `SO-D-07.1-002` | Product designed per Annex I essential requirements (umbrella) | transversal | AS | **Covered (umbrella for RN13/RN14)** — specific drivers re-assigned to SO-D-07.2-002 where narrower | ADJ-4, ADJ-6 |
| `SO-D-07.2-002` | Attack surfaces limited (incl. external components) | `R5.1` (uploads), `R4.2` (throttling), `R5.2`/`R6.2` (rendering/webhooks) | AS | **Partial → Proposed R1 (ADJ-4, ADJ-6)** — RN13/RN17 re-drive here; RN16's integrity anchor re-based | ADJ-4, ADJ-6 |
| `SO-D-07.3-002` | Secure, timely update distribution (automatic where appropriate) | — | — | **No functional carrier** (organizational/deployment) | — |
| `SO-D-07.4-002` | Series-production conformity procedures | — | — | **N/A** (SaaS has no production series) | — |

## D-08 — Human Factors

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-08.1-001` | DPO informs/advises on obligations | — | — | **No functional carrier** (organizational) | — |
| `SO-D-08.1-002` | Product accompanied by secure-use instructions (or info address) | help/documentation surface | — | **Proposed R1 (P-04)** — secure-use documentation coverage for users/admins (SHOULD) | P-04 |
| `SO-D-08.2-001` | DPO monitors compliance, awareness, training | — | — | **No functional carrier** (organizational) | — |
| `SO-D-08.2-002` | Integration information for products integrating this product | — | — | **N/A** (product not offered for integration) | — |

## D-09 — Governance & Documentation

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `PO-D-09.1-001` | Accountability policies implementing data-protection principles | — | — | **No functional carrier** (organizational) | — |
| `SO-D-09.1-002` | Product-security policies, processes, procedures | — | — | **No functional carrier** (organizational) | — |
| `PO-D-09.2-001` | DPIA before high-risk processing | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-09.2-002` | Cybersecurity risk assessment documented + updated | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-09.3-002` | Technical documentation (general + design description) | — | — | **No functional carrier** (organizational) | — |
| `PO-D-09.4-001` | Art. 30 records of processing activities | `R1.2`, `R6.1` (privacy audit trail) | V | **Covered (RN26)** — recalibrated from phantom PO-D-03.1-001 | — |
| `SO-D-09.4-002` | Technical documentation + conformity assessment before market | — | — | **No functional carrier** (organizational) | — |

## D-10 — Monitoring & Audit

| Objective | Summary | Functional carrier | Skill | State vs V1 | Action / Round |
|---|---|---|---|---|---|
| `SO-D-10.1-001` | Ongoing CIA + resilience of systems (technical/organisational) | — (ops; RN2/RN5 adjacent) | — | **No functional carrier** (organizational/ops) | — |
| `SO-D-10.1-002` | Product records and monitors relevant internal activity | `R6.1`, `R2.2` (security-relevant events) | V | **Partial → Proposed R1 (ADJ-5)** — RN18 re-drive here from SO-D-03.1-002 | ADJ-5 |
| `SO-D-10.2-001` | Compliance records with integrity/traceability | — | — | **No functional carrier** (organizational) | — |
| `SO-D-10.2-002` | Technical + risk-assessment documentation preserved | — | — | **No functional carrier** (organizational) | — |
| `SO-D-10.3-001` | Regular testing of measures' effectiveness | — | — | **No functional carrier** (organizational process) | — |
| `SO-D-10.3-002` | Effective, regular product testing; reports in documentation | — | — | **No functional carrier** (organizational process) | — |

## Engineering Principles (PRIN-ENG-01…07)

| Principle | Binding in V1 | Verdict |
|---|---|---|
| `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | RN15, RN16, RN24 chains | Bound |
| `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | RN13, RN17 chains | Bound |
| `PRIN-ENG-03` Least Privilege & Mechanism Isolation | RN9, RN12, RN22 chains | Bound |
| `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | RN7.2-adjacent, RN10/RN11 chains | Bound |
| `PRIN-ENG-05` Atomic Verifiability & Unambiguous Acceptance Criteria | **realized by the fit-criterion practice on every proposal — never explicitly bound** | **Recorded once here**: every RN carries a Volere fit criterion + verification method; binding is global, not per-chain |
| `PRIN-ENG-06` Default-On Privacy & Data Minimization by Construction | RN19 chain | Bound |
| `PRIN-ENG-07` Non-Repudiable Observability & Forensic Integrity | RN18, RN26 chains | Bound |

---

## Coverage totals (this matrix)

| Verdict | Count |
|---|---|
| Covered | 14 (incl. 1 umbrella) |
| Partial → re-drive proposed in R1 | 8 rows / 9 adjustment items (ADJ-1…ADJ-9) |
| New constraint proposed in R1 | 4 (P-01…P-04) |
| No functional carrier (recorded decision) | 31 |
| Design guidance (Phase 4 context) | 2 |
| N/A (requirement type inapplicable to SaaS) | 2 |
| **Total objectives** | **62** |

Every objective above is explicitly placed; none is silent. Re-drives and new constraints take effect only after the client's verdicts in `RISK_ACCEPTANCE_REGISTER.md` (Round 1).
