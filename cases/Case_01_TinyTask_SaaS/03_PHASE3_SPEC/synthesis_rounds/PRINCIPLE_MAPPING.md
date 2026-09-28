# Principle Mapping — Functional Requirements Analyzed Against the 7 Secure Design Principles (TinyTask SaaS)


## §1 Principle ↔ Functional Model Matrix (principle-centric)

### `PRIN-ENG-01` — Explicit Trust Boundaries & Complete Mediation

Every interface separating zones of differing privilege is demarcated; every crossing flow is authenticated and validated; no unmediated bypass.

| Where | Realization | RN | State |
|---|---|---|---|
| `R7.1`, `R7.2` / `{U.C. 7.1}` `{U.C. 7.2}` | Gateway responses cross the boundary with complete mediation; billing state changes only on verified receipts | RN15 | Bound |
| `R6.2` / `{U.C. 6.2}` | Notification transport crosses the boundary with verified origin (webhook signature) | RN16 | Bound |
| `R1.2` / `{U.C. 1.2}` | Profile records protected within the boundary; egress scoped | RN23 | Bound |
| All UCs (preconditions) | Transport confidentiality on every external-boundary flow | RN24 | Cross-cutting |
| `R8.1`, `R8.2` / `{U.C. 8.1}` `{U.C. 8.2}` | Rights-exercise execution mediated by verified requester identity | RN27 | Bound |

**Verdict: followed.**

### `PRIN-ENG-02` — Attack Surface Minimization & Peripheral Resilience

Entry points, channels and active interfaces reduced to the minimum; auxiliary ingress matches core security intensity.

| Where | Realization | RN | State |
|---|---|---|---|
| `R5.1` / `{U.C. 5.1}` | Upload surface minimized; disallowed types rejected at the boundary; content validated | RN13 | Bound |
| `R4.2`, `R6.1` / `{U.C. 4.2}` `{U.C. 6.1}` | Transition/query request floods throttled (resilience of peripheral flows) | RN17 | Bound |
| `R4.1`, `R5.2` / `{U.C. 4.1}` `{U.C. 5.2}` | Rendered/ingested content neutralized (no executable payloads) | RN14 | Bound |

**Verdict: followed.**

### `PRIN-ENG-03` — Least Privilege & Mechanism Isolation

Every principal operates with minimum privileges; distinct tenants/sensitivity levels never share unisolated mechanisms.

| Where | Realization | RN | State |
|---|---|---|---|
| `R2.1`, `R3.1` / `{U.C. 2.1}` `{U.C. 3.1}` | Tenant context enforced on every provisioning/creation action; containers born isolated | RN9 | Bound |
| `R2.2`, `R3.2`, `R8.1` / `{U.C. 2.2}` `{U.C. 3.2}` `{U.C. 8.1}` | RBAC mediation before membership/archive/export mutations; Owner irremovable | RN12 | Bound |
| `R2.3`, `R6.1` / `{U.C. 2.3}` `{U.C. 6.1}` | Metrics/audit queries purpose-scoped; no cross-tenant or surveillance aggregation | RN22 | Bound |
| `R4.3` / `{U.C. 4.3}` | Recurrence daemon executes in an isolated service context | RN9 (pre) | Bound |

**Verdict: followed.**

### `PRIN-ENG-04` — Fail-Safe Defaults & Closed Failure States

Access decisions and state transitions default to refusal; failures terminate in a secure closed state.

| Where | Realization | RN | State |
|---|---|---|---|
| `R1.1`, `R1.3` / `{U.C. 1.1}` `{U.C. 1.3}` | Credentials stored unrecoverable; lockout fails closed; enumeration-resistant recovery responses | RN10, RN11 | Bound |
| `R5.2` / `{U.C. 5.2}` | Sanitization fails safe — payloads never executed by default | RN14 | Bound |
| `R7.2` / `{U.C. 7.2}` | Expired grace period → restricted read-only state, never silent open access | functional (description) | Bound |
| `R2.1`, `R3.1` / `{U.C. 2.1}` `{U.C. 3.1}` | New artifacts start with restrictive secure-by-default configuration | RN28 | Bound |

**Verdict: followed.**

### `PRIN-ENG-05` — Requirement Verifiability & Atomicity

Every security/privacy requirement is atomic with a deterministic pass/fail verification method.

| Where | Realization | RN | State |
|---|---|---|---|
| All RN cards + every round proposal | Volere fit criterion + empirical method (`TEST`/`INSPECT`/`DEMONSTRATE`/`ANALYZE`) on each requirement | global | Bound (recorded once) |

**Verdict: followed** (structural — enforced by the card anatomy and the round-proposal template).

### `PRIN-ENG-06` — Proactive Data Minimization & Scoped Projection

Only strictly indispensable data is collected, transmitted or retained; egress projects strictly scoped views.

| Where | Realization | RN | State |
|---|---|---|---|
| `R1.1` / `{U.C. 1.1}` | Registration collects only the necessary personal data | RN19 | Bound |
| `R8.1` / `{U.C. 8.1}` | Archive limited to the requester's own data (no third-party leakage) | RN20 | Bound |

**Verdict: followed.**

### `PRIN-ENG-07` — End-to-End Lifecycle Security & Irreversible Erasure

Protection covers the entire lifecycle; erasure permanently destroys across stores; observability is non-repudiable.

| Where | Realization | RN | State |
|---|---|---|---|
| All R / all UCs | Immutable security audit record for authentication, privilege, denial and billing events | RN18 | Bound (cross-cutting, Quality Attributes) |
| `R8.2` / `{U.C. 8.2}` | Erasure irreversible + pseudonymized; receipt issued; audit trail preserved | RN21 | Bound |
| `R5.1` / `{U.C. 5.1}` | Deleted attachments purged on a retention schedule (no indefinite retention) | RN25 | Bound |
| `R1.2` / `{U.C. 1.2}` | Personal-data modifications emit a privacy audit record (Art. 30 accountability) | RN26 | Bound |
| `R8.3` / `{U.C. 8.3}` | Workspace-level deletion permanently erases all workspace content and settings; deletion recorded | RN30, RN21 (co-driver), RN18 | Bound |

**Verdict: followed.**

---

## §2 Per-Requirement Principle Check (R1.1–R8.2)

One row per (requirement × principle) binding: the principle is named in full, the concrete mechanism states **how** it is upheld in that requirement, and the carrier names where the enforcement lives (absorbed NFR, functional description, or use-case extension/precondition). A requirement without a binding row has no direct security surface of its own and says so explicitly.

| Req | Principle | How it is upheld here | Carrier | State |
|---|---|---|---|---|
| `R1.1` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | Credentials stored unrecoverable; lockout fails closed after repeated failures | RN10, RN11 | Bound |
| `R1.1` | `PRIN-ENG-06` Proactive Data Minimization & Scoped Projection | Registration collects only the strictly necessary personal data | RN19 | Bound |
| `R1.2` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Profile records protected within the boundary; egress scoped | RN23 | Bound |
| `R1.2` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Profile modifications emit a privacy audit record (Art. 30 accountability) | RN26 | Bound |
| `R1.3` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | Recovery fails closed on expired/reused links; enumeration-resistant responses | RN10, RN11 | Bound |
| `R1.3` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Recovery attempts recorded in the audit log | RN18 | Bound |
| `R2.1` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Tenant context enforced on provisioning; workspace born isolated | RN9 | Bound |
| `R2.1` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | New workspace starts with restrictive secure-by-default configuration | RN28 | Bound |
| `R2.2` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | RBAC mediation before every membership/role mutation; Owner irremovable | RN12 | Bound |
| `R2.3` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Metrics purpose-scoped; no cross-tenant or surveillance aggregation | RN22 | Bound |
| `R3.1` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Project containers created inside the tenant boundary | RN9 | Bound |
| `R3.1` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | New projects default to restricted visibility | RN28 | Bound |
| `R3.2` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Archive transition only by Admin/Owner (no direct carrier; realized at `{U.C. 3.2}` via extension) | RN12 via `{U.C. 3.2}` | Bound (UC level) |
| `R4.1` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | Task title/description neutralized against embedded active payloads | RN14 via `{U.C. 4.1}` extension | Bound (UC level) |
| `R4.1` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Task created within the authorized project/tenant context (precondition) | RN9 via `{U.C. 4.1}` precondition | Bound (UC level) |
| `R4.2` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | Transition request floods throttled (peripheral-flow resilience) | RN17 via `{U.C. 4.2}` | Bound (UC level) |
| `R4.3` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Recurrence daemon executes in an isolated service context (precondition) | RN9 via `{U.C. 4.3}` precondition | Bound (UC level) |
| `R4.3` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Automation skips/failures logged | RN18 via `{U.C. 4.3}` extension | Bound (UC level) |
| `R5.1` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | Upload surface minimized; disallowed types rejected at the boundary; content validated | RN13 | Bound |
| `R5.1` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Deleted attachments purged on a retention schedule (no indefinite retention) | RN25 | Bound |
| `R5.2` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | Rendered comments cannot carry executable payloads | RN14 | Bound |
| `R5.2` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | Sanitization fails safe — payloads never executed by default | RN14 | Bound |
| `R6.1` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Audit feed purpose-scoped (no productivity surveillance) | RN22 | Bound |
| `R6.1` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | Audit queries paginated/throttled against exhaustion | RN17 via `{U.C. 6.1}` | Bound (UC level) |
| `R6.1` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | History query scoped to the authorized tenant (precondition) | RN9 via `{U.C. 6.1}` precondition | Bound (UC level) |
| `R6.2` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Notification transport crosses the trust boundary with verified origin (webhook signature) | RN16 | Bound |
| `R6.2` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Digest pipeline integrity — no forged or altered alerts | RN16 via `{U.C. 6.2}` | Bound (UC level) |
| `R7.1` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Gateway responses cross the boundary with complete mediation; billing changes only on verified receipts | RN15 | Bound |
| `R7.1` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Forged-webhook rejections recorded | RN18 via `{U.C. 7.1}` extension | Bound (UC level) |
| `R7.2` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Grace-state transitions driven by integrity-verified payment events | RN15 | Bound |
| `R7.2` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | Expired grace → restricted read-only state, never silent open access | functional (description) | Bound |
| `R8.1` | `PRIN-ENG-06` Proactive Data Minimization & Scoped Projection | Archive limited to the requester's own data (no third-party leakage) | RN20 | Bound |
| `R8.1` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Workspace-level export restricted to the Owner | RN12 via `{U.C. 8.1}` extension | Bound (UC level) |
| `R8.1` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Requester identity verified before executing the export | RN27 | Bound |
| `R8.2` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Erasure irreversible + pseudonymized; receipt issued; audit trail preserved | RN21, RN18 | Bound |
| `R8.2` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Closure invalidates all sessions/tokens (entitlement revocation) | RN11 via `{U.C. 8.2}` extension | Bound (UC level) |
| `R8.2` | `PRIN-ENG-01` Explicit Trust Boundaries & Complete Mediation | Requester identity verified before executing the erasure | RN27 | Bound |
| `R8.3` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | Workspace deletion permanently erases all workspace content; deletion recorded in audit log | RN30, RN21 (co-driver), RN18 | Bound |
| `R8.3` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | Deletion restricted to the Workspace Owner | RN12 via `{U.C. 8.3}` | Bound (UC level) |

**Cross-cutting principles (not per-card):** `PRIN-ENG-05` Atomic Verifiability — structural, realized by the Volere fit criterion + verification method on every requirement and proposal (recorded once); RN17 (rate limiting), RN18 (audit logging), RN24 (transport encryption) bind every use case as standalone Quality Attributes rows.

**Per-principle rollup (requirements realizing each principle):**

| Principle | Requirements realizing it | Cover |
|---|---|---|
| `PRIN-ENG-01` Trust Boundaries & Complete Mediation | R1.2, R4.1, R6.1, R6.2, R7.1, R7.2, R8.1, R8.2 (+ RN24 cross-cutting) | 8 + cross-cutting |
| `PRIN-ENG-02` Attack Surface Minimization | R4.1, R4.2, R5.1, R5.2, R6.1 | 5 |
| `PRIN-ENG-03` Least Privilege & Mechanism Isolation | R2.1, R2.2, R2.3, R3.1, R3.2, R4.3, R6.1, R8.1, R8.2 | 9 |
| `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | R1.1, R1.3, R2.1, R3.1, R5.2, R7.2 | 6 |
| `PRIN-ENG-05` Atomic Verifiability | all (structural) | 19 + proposals |
| `PRIN-ENG-06` Proactive Data Minimization | R1.1, R8.1 | 2 |
| `PRIN-ENG-07` End-to-End Lifecycle Security & Erasure | R1.2, R1.3, R4.3, R5.1, R6.2, R7.1, R8.2 (+ RN18 cross-cutting) | 7 + cross-cutting |

## §3 Coverage Totals & Gaps

| Surface | Count | Notes |
|---|---|---|
| Principles followed | 7/7 | every principle has ≥1 realization; none without a carrier |
| Pending principle gaps | 0 | P-01/P-02 accepted in Round 1 and bound (RN27, RN28); P-03 accepted as D1 (`R8.3`); P-04 accepted (RN29) — see [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) |
| Requirements realizing ≥1 principle | 20/20 | `R3.2` realized at UC level (extension); `R8.3` added in Round 1 |
| Re-drives applied to principle chains | 11 RNs | ADJ-1…ADJ-9 accepted R1; drivers aligned to published control sets — see [`ROUND1_REGISTER.md`](ROUND1_REGISTER.md) |

**Read rule:** gaps in this matrix are **principle gaps**, not requirement defects — they enter the open round as proposals (verdicts recorded in the round documentation); nothing is silently accepted.
