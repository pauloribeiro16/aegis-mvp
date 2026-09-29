# Phase 2 Objective Mapping — Exhaustive Coverage Matrix (TinyTask SaaS)

> **Verdict vocabulary (ADR-007 D4):** `Fully covered` — the union of carrier fit criteria reconstitutes the objective's Verification Criteria and every statement leg is carried, out-of-scale-recorded, or carved out · `Partially covered` — the functional legs are carried; named legs are carved out to the organizational lane, design guidance, or a pending proposal · `No functional carrier (organizational)` — PROCESS/CAPABILITY obligation, recorded decision (input repertoire of `Doc03_Organizational_Requirements.md`, ADR-008) · `Design guidance` / `N/A`. The `VC discharge (R2)` column is the authoritative discharge record; delivered card chains cite primary drivers only (ADR-007 D3).


## D-01 — Data Protection

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `PO-D-01.1-001` | Personal data at rest processed with appropriate security | `R1.2` (profile records) | TB | **Partially covered (RN23)** | RN23 → at-rest confidentiality (volumes, file assets, backups); carve-out: ongoing CIA/resilience of processing systems → organizational lane (SO-D-04.4-001/SO-D-10.1-001) | anchors match published set · R2 re-audit |
| `SO-D-01.1-002` | Data at rest encrypted with state-of-the-art mechanisms | `R1.1`, `R1.3`, `R7.1`, `R7.2` | TB | **Partially covered (RN10, RN15, RN23)** | RN23 → product components; release-artifacts leg discharged via RN23 infrastructure-manifest INSPECT (SaaS interpretation recorded R2); RN15 → billing-state integrity only (not at-rest encryption) | RN10 anchor set corrected R0-recal · R2 re-audit |
| `PO-D-01.2-001` | Personal data in transit confidential and unaltered | `R1.1`, all UC preconditions | TB | **Fully covered (RN24)** | RN24 fit criterion is broader than the objective (all data vs personal data flows — safe superset); Art. 32(2) five-event enumeration carried at its confidentiality/integrity core | anchors match |
| `SO-D-01.2-002` | CRA twin: data in transit encrypted (state of the art) | `R1.1`, all UC preconditions | TB | **Fully covered (RN24 + RN13/RN14/RN17 x-ref)** | leg 1 (transport encryption) → RN24; attack-surface-limitation leg → SO-D-07.2-002 carriers RN13/RN14/RN17 (cross-reference recorded) | ADJ-9 accepted R1 · R2 union record |
| `PO-D-01.3-001` | Re-identification info kept separate (key separation) | — (design constraint) | — | **Design guidance** | — | design/Phase 4 context |
| `SO-D-01.3-002` | Cryptographic keys and auth material managed/protected | — (design constraint) | — | **Design guidance** | — | design/Phase 4 context |
| `PO-D-01.4-001` | Accuracy + rectification without delay | `R1.2` (profile editing) | V | **Partially covered (R1.2 elevation)** | self-service rectification of profile fields carried; carrier has no fit criterion (ROUND2 §2 P1); Art. 19 recipient-notification cascade → organizational lane | D3 elevation, STEP5 CH-04 · R2 re-audit |
| `SO-D-01.4-002` | Integrity of stored/transmitted data, commands, configuration | `R7.1`, `R7.2` (billing state), `R6.2` (webhook messages) | V | **Partially covered (RN15, RN16)** | RN15 → stored billing state; RN16 → webhook channel; configuration integrity → RN23 manifests (x-ref); carve-outs: corruption-reported leg → ROUND2 §2 P4; release-artifacts leg → SaaS interpretation (as SO-D-01.1-002) | re-driven, ADJ-7/ADJ-8 accepted R1 · R2 re-audit |

## D-02 — Vulnerability Management

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-02.1-001` | Process: regularly test effectiveness of measures | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-02.1-002` | Product free of known exploitable vulnerabilities; SBOM-correlated identification | — (release/dependency practice) | AS | **No functional carrier** (organizational/dev-process) | — | ADJ-1…ADJ-4 |
| `SO-D-02.2-002` | Vulnerabilities remediated via security updates; secure distribution | — (deployment practice) | — | **No functional carrier** (organizational/dev-process) | — | ADJ-2 |
| `SO-D-02.3-002` | Coordinated vulnerability disclosure policy | — | — | **No functional carrier** (organizational policy) | — | — |

## D-03 — Access Control

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-03.1-001` | Verify identity of data-subject rights requests (Art. 15–22) | `R8.1`, `R8.2` (RN27) | TB | **Partially covered (RN27)** | export/erase request verification carried; Art. 15/16/18/21 request types + minimisation-constrained verification leg → ROUND2 §2 P2 | P-01 accepted R1 · R2 re-audit |
| `SO-D-03.1-002` | Identities, credentials, entitlements managed in a verified way | `R1.1`, `R1.3`, `R2.2` (credentials, sessions, roles) | LP | **Partially covered (RN11; RN10/RN12 co-drivers)** | credentials (RN10), session lifecycle (RN11), entitlement mediation (RN12) carried; carve-outs: joiner/mover/leaver offboarding beyond self-service, unique product identification, single point of contact → organizational lane | ADJ-2 accepted R1 · R2 re-audit |
| `SO-D-03.2-001` | Authorized persons act on documented instructions (GDPR side) | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-03.2-002` | Protection from unauthorised access via control mechanisms (CRA 2)(d) home | `R2.1`, `R3.1` (tenant isolation) | TB | **Fully covered (RN9)** | RN9 access-management fit criterion (100%-probe) reconstitutes the VC | re-driven, ADJ-1 accepted R1 |
| `SO-D-03.3-001` | Processor-side documented instructions + confidentiality | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-03.3-002` | Access limited to authenticated and authorized users/services | `R2.2` (RBAC) | LP | **Partially covered (RN12)** | RN12 → authorized-mutation mediation + refused-mutation logging; x-refs: RN11 (authentication gating), RN17 (inbound service authentication), RN13/RN14 (surface limitation); carve-outs: active alerting beyond logging → organizational monitoring lane; hardware principals out-of-scale (no integrated hardware) | re-driven, ADJ-3 accepted R1 · R2 re-audit |
| `SO-D-03.4-001` | By default only necessary personal data processed | `R1.1` (registration form) | DM | **Partially covered (RN19)** | amount collected → RN19; extent of processing → RN22 (x-ref); accessibility → RN12/RN28 (x-refs: RBAC + restrictive defaults satisfy the "not accessible without intervention to indefinite persons" leg); period-of-storage beyond attachments (RN25) → organizational retention schedules | after PO recalibration · R2 re-audit |
| `SO-D-03.4-002` | Secure-by-default configuration, resettable by user | `R2.1`, `R3.1` (RN28) | FS | **Partially covered (RN28)** | legs 1–2 (restrictive default + user reset) carried; update-mechanism legs (automatic installation, enabled-by-default, opt-out, postponement) inapplicable to a SaaS deployment model (interpretation recorded R2) → operational update process → organizational lane (SO-D-07.3-002) | P-02 accepted R1 · R2 re-audit |

## D-04 — Incident Response

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-04.1-001` | Breach detection/triage, awareness moment documented (72 h) | — (process; supported by RN18 logs) | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-04.1-002` | Relevant internal activity recorded (access/modification) | `R6.1` (audit feed) | V | **Partially covered (RN18)** | *recorded* leg carried by RN18; carve-outs: monitoring / detection & triage → organizational process lane; opt-out leg: not appropriate for immutable security audit records (interpretation recorded R2, PRIN-ENG-07 non-repudiable observability) | ADJ-5 accepted R1 · R2 re-audit |
| `SO-D-04.2-001` | Breach containment/mitigation measures | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-04.2-002` | Availability of essential functions protected after incident | — (ops; RN5 backups adjacent) | — | **No functional carrier** (organizational/ops; RN5 covers the V0 functional slice) | — | — |
| `SO-D-04.3-001` | Breach notified to supervisory authority (72 h) | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-04.3-002` | Actively-exploited vulnerability notified (3-tier timeline) | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-04.4-001` | Ongoing CIA + resilience of processing systems ensured | — (ops) | — | **No functional carrier** (organizational/ops; RN2/RN5 cover the V0 slice) | — | — |
| `SO-D-04.4-002` | Recovery measures with defined RPO | `RN5` (V0, W1) | — | **Partially covered (RN5)** | data-recovery slice carried (daily backups, RPO < 24 h — no fit criterion, ROUND2 §2 P1); exploitation-mitigation leg → RN13/RN14/RN17 (x-refs); corrective measures restoring conformity → organizational lane | V0 slice · R2 re-audit |

## D-05 — Data Lifecycle

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `PO-D-05.1-001` | Minimization + purpose limitation (adequate, relevant, necessary) | `R1.1` (registration), `R2.3`/`R6.1` (activity data) | DM | **Partially covered (RN19, RN22)** | registration minimality (RN19) + timesheet use limitation (RN22) carried; carve-outs: Art. 6(4) five-factor compatibility test, high-risk impact assessment → organizational lane | PO recalibration (R0) · R2 re-audit |
| `SO-D-05.1-002` | CRA twin: product data limited to what is necessary | `R1.1`, `R5.1` (lifecycle) | DM | **Partially covered (RN19, RN25)** | collection-minimality (RN19) + attachment retention (RN25) slices carried; carve-outs: minimality verification for remaining product data classes → design-time field limitation recorded (V0 fixed schemas), proportionality-calibration clause (risk assessment + foreseeable use) → organizational | RN16/RN17 re-driven away (ADJ-4/ADJ-7 accepted R1) · R2 re-audit |
| `PO-D-05.2-001` | Retention no longer than necessary | `R5.1` (attachments) | LE | **Partially covered (RN25)** | orphaned-attachment retention carried; carve-outs: retention ceilings for remaining data classes + documented erasure time limits per category → organizational retention schedules | PO recalibration (R0) · R2 re-audit |
| `SO-D-05.2-002` | Updates/advisories available across support period | — | — | **No functional carrier** (organizational/support process) | — | — |
| `PO-D-05.3-001` | Erasure without undue delay on request (Art. 17) | `R8.2` | LE | **Partially covered (RN21)** | irreversible erasure on request (self-service termination flow) carried; carve-out: processor delete-or-return at contract end → organizational/contracts lane | PO recalibration (R0) · R2 re-audit |
| `SO-D-05.3-002` | User can permanently remove all data and settings of the product | `R8.3` (workspace deletion; `R8.2` account) | LE | **Fully covered (RN30; RN21 co-driver)** | permanent removal of all content + settings, certified (RN30/RN21); secure-transfer leg → RN24 transit protection on the R8.1 export flow (cross-reference recorded) | P-03 accepted R1 (D1) · R2 union record |
| `PO-D-05.4-001` | Portability: structured, machine-readable, free of charge | `R8.1` | LE | **Partially covered (RN20)** | structured/machine-readable export incl. third-party-data exclusion carried; carve-outs: free-of-charge (company policy statement) → organizational; response-time bound → pending formulation; direct controller-to-controller transmission out-of-scale (recorded) | PO recalibration (R0) · R2 re-audit |

## D-06 — Supply Chain & Third-Party Security

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-06.1-001` | Processors provide sufficient guarantees (GDPR Art. 28) | — | — | **No functional carrier** (organizational/procurement) | — | — |
| `SO-D-06.1-002` | Due diligence on third-party/open-source components | — | — | **No functional carrier** (organizational/dev-process) | — | — |
| `SO-D-06.2-002` | SBOM maintained, machine-readable | — | — | **No functional carrier** (organizational/dev-process) | — | — |
| `SO-D-06.3-001` | Art. 28(3)(a)–(h) contract floor + sub-processor chain | — | — | **No functional carrier** (organizational/contracts) | — | — |
| `SO-D-06.3-002` | Economic-operator contractual duties (importers/distributors) | — | — | **N/A** (no distribution chain for a SaaS service) | — | — |

## D-07 — Secure Development

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `PO-D-07.1-001` | DPbD technical/organisational measures (pseudonymisation…) | transversal (RN19/RN23 realize slices) | DM | **Partially covered (transversal: RN19, RN23)** | by-default minimization (RN19) + at-rest safeguard (RN23) slices; pseudonymisation exemplar → RN21 (x-ref); carve-out: holistic by-design integration → design lane (Phase 4 context) | R2 re-audit |
| `SO-D-07.1-002` | Product designed per Annex I essential requirements (umbrella) | transversal | AS | **Partially covered (RN13/RN14/RN17 slices)** | essential-requirement slices carried via SO-D-07.2-002 drivers; carve-out: six-phase lifecycle risk-assessment propagation → organizational lane (SO-D-09.2-002) | specific drivers on SO-D-07.2-002, ADJ-4/ADJ-6 accepted R1 · R2 re-audit |
| `SO-D-07.2-002` | Attack surfaces limited (incl. external components) | `R5.1` (uploads), `R4.2` (throttling), `R5.2`/`R6.2` (rendering/webhooks) | AS | **Fully covered (RN13, RN14, RN17)** | both legs (surface limitation incl. external components; exploitation mitigation) carried with verified fit criteria | re-driven, ADJ-4/ADJ-6 accepted R1 |
| `SO-D-07.3-002` | Secure, timely update distribution (automatic where appropriate) | — | — | **No functional carrier** (organizational/deployment) | — | — |
| `SO-D-07.4-002` | Series-production conformity procedures | — | — | **N/A** (SaaS has no production series) | — | — |

## D-08 — Human Factors

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-08.1-001` | DPO informs/advises on obligations | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-08.1-002` | Product accompanied by secure-use instructions (or info address) | `R8` package documentation surface (RN29) | — | **Fully covered (RN29, SHOULD)** | all instruction legs carried; topic-minimum interpretation + SHOULD priority residual recorded (SUFFICIENCY_ASSESSMENT §1) | P-04 accepted R1 · R2 re-audit |
| `SO-D-08.2-001` | DPO monitors compliance, awareness, training | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-08.2-002` | Integration information for products integrating this product | — | — | **N/A** (product not offered for integration) | — | — |

## D-09 — Governance & Documentation

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `PO-D-09.1-001` | Accountability policies implementing data-protection principles | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-09.1-002` | Product-security policies, processes, procedures | — | — | **No functional carrier** (organizational) | — | — |
| `PO-D-09.2-001` | DPIA before high-risk processing | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-09.2-002` | Cybersecurity risk assessment documented + updated | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-09.3-002` | Technical documentation (general + design description) | — | — | **No functional carrier** (organizational) | — | — |
| `PO-D-09.4-001` | Art. 30 records of processing activities | `R1.2`, `R6.1` (privacy audit trail) | V | **No functional carrier (organizational)** | Art. 30 register is a documentary/organizational obligation (7-item content, processor-side record, authority availability); RN26 = supporting privacy event trail, chain unchanged | chain recalibration (R0) · R2 re-verdict |
| `SO-D-09.4-002` | Technical documentation + conformity assessment before market | — | — | **No functional carrier** (organizational) | — | — |

## D-10 — Monitoring & Audit

| Objective | Summary | Functional carrier | Skill | State (R2) | VC discharge (R2) | Action / Round |
|---|---|---|---|---|---|---|
| `SO-D-10.1-001` | Ongoing CIA + resilience of systems (technical/organisational) | — (ops; RN2/RN5 adjacent) | — | **No functional carrier** (organizational/ops) | — | — |
| `SO-D-10.1-002` | Product records and monitors relevant internal activity | `R6.1`, `R2.2` (security-relevant events) | V | **Partially covered (RN18)** | recording leg carried by RN18; carve-outs: continuous monitoring → organizational lane; opt-out leg → interpretation recorded (audit immutability, PRIN-ENG-07); single vulnerability-contact address → organizational lane (SO-D-02.3-002, CVD) | re-driven, ADJ-5 accepted R1 · R2 re-audit |
| `SO-D-10.2-001` | Compliance records with integrity/traceability | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-10.2-002` | Technical + risk-assessment documentation preserved | — | — | **No functional carrier** (organizational) | — | — |
| `SO-D-10.3-001` | Regular testing of measures' effectiveness | — | — | **No functional carrier** (organizational process) | — | — |
| `SO-D-10.3-002` | Effective, regular product testing; reports in documentation | — | — | **No functional carrier** (organizational process) | — | — |

## Engineering Principles (PRIN-ENG-01…07)

| Principle | Binding in V1 | Verdict |
|---|---|---|
| `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | RN15, RN16, RN24 chains | Bound |
| `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | RN13, RN17 chains | Bound |
| `PRIN-ENG-03` Least Privilege & Mechanism Isolation | RN9, RN12, RN22 chains | Bound |
| `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | RN7.2-adjacent, RN10/RN11 chains | Bound |
| `PRIN-ENG-05` Atomic Verifiability & Unambiguous Acceptance Criteria | **realized by the fit-criterion practice on every proposal — never explicitly bound** | **Recorded once here**: every RN carries a Volere fit criterion + verification method; binding is global, not per-chain. R2 exception recorded: RN1–RN8 and the R1.2 elevation lack fit criteria — repair proposed (ROUND2 §2 P1) |
| `PRIN-ENG-06` Default-On Privacy & Data Minimization by Construction | RN19 chain | Bound |
| `PRIN-ENG-07` Non-Repudiable Observability & Forensic Integrity | RN18, RN26 chains | Bound |

---

## Coverage totals (this matrix)

| Verdict | Count |
|---|---|
| Fully covered (discharge-verified) | 6 |
| Partially covered (functional leg + explicit carve-out) | 19 |
| No functional carrier (organizational) | 32 |
| Design guidance (Phase 4 context) | 2 |
| N/A (requirement type inapplicable to SaaS) | 3 |
| **Total objectives** | **62** |

Every objective above is explicitly placed with a discharge record — none is silent (ADR-007 D2). Round 1 closed on 2026-09-28 with 13/13 accepts — verdicts, formulations and control selections in [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md); accepted items applied in `Doc01`/`Doc02` 4.0.0. Round 2 (2026-09-28, [ADR-007](../../../../docs/decisions/ADR-2026-09-28_requirement-objective-fulfillment-semantics.md)) replaced name-linkage "Covered" verdicts with discharge records — record corrections applied by researcher mandate (approved working plan); baseline-change proposals P1–P4 pending client verdicts in [`ROUND2_REGISTER.md`](ROUND2_REGISTER.md).
