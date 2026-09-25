# Principle Mapping — Functional Requirements Analyzed Against the 7 Secure Design Principles (TinyTask SaaS)

> **Purpose:** The principle-centric mirror of [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md): for **each secure-design principle** (`PRIN-ENG-01`..`07`, Phase 2 `Doc02`), where it binds across the functional model (requirement cards `R<n.m>` and use cases `{U.C.n.m}`), how it is realized there, and its coverage state — so a reviewer can judge whether **every principle is being followed**, the same way the objective mapping judges whether every objective is applied.
> **Sources:** `../../02_PHASE2_RULES/Doc02_Secure_Design_Principles.md` (principle definitions) · `../v1_security_privacy_synthesis/Doc01` (in-card NFR absorption) · [`UC_OBJECTIVE_CORRESPONDENCE.md`](UC_OBJECTIVE_CORRESPONDENCE.md) (per-UC bindings) · [`RISK_ACCEPTANCE_REGISTER.md`](RISK_ACCEPTANCE_REGISTER.md) (pending gaps).
> **State legend:** `Bound (RNx)` = realized by the named absorbed NFR / in-card constraint · `Bound (functional)` = realized directly in the requirement's functional description (no RN needed) · `Pending (P-xx / ADJ-x)` = gap proposed in the open round, awaiting client verdict · `Cross-cutting` = binds via shared table row / preconditions, not a single card.
> **Skills (analysis lens):** AS = attack-surface-analysis · TB = trust-boundary-analysis · LP = least-privilege-analysis · FS = fail-safe-defaults-analysis · V = verifiability-analysis · DM = data-minimization-analysis · LE = lifecycle-erasure-analysis.

---

## §1 Principle ↔ Functional Model Matrix (principle-centric)

### `PRIN-ENG-01` — Explicit Trust Boundaries & Complete Mediation

Every interface separating zones of differing privilege is demarcated; every crossing flow is authenticated and validated; no unmediated bypass.

| Where | Realization | RN | State |
|---|---|---|---|
| `R7.1`, `R7.2` / `{U.C. 7.1}` `{U.C. 7.2}` | Gateway responses cross the boundary with complete mediation; billing state changes only on verified receipts | RN15 | Bound |
| `R6.2` / `{U.C. 6.2}` | Notification transport crosses the boundary with verified origin (webhook signature) | RN16 | Bound |
| `R1.2` / `{U.C. 1.2}` | Profile records protected within the boundary; egress scoped | RN23 | Bound |
| All UCs (preconditions) | Transport confidentiality on every external-boundary flow | RN24 | Cross-cutting |
| `R8.1`, `R8.2` / `{U.C. 8.1}` `{U.C. 8.2}` | Rights-exercise execution mediated by verified requester identity | — | Pending (P-01) |

**Verdict: followed.** One pending mediation gap (P-01) awaiting verdict.

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
| `R2.1`, `R3.1` / `{U.C. 2.1}` `{U.C. 3.1}` | New artifacts start with restrictive secure-by-default configuration | — | Pending (P-02) |

**Verdict: followed.** One pending default-configuration gap (P-02) awaiting verdict.

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

**Verdict: followed.**

---

## §2 Per-Requirement Principle Check (R1.1–R8.2)

One row per functional requirement: which principles it realizes and via what. A row without any principle binding is only legitimate when the requirement has no security surface (recorded explicitly, never silent).

| Req | Principles realized | Via | State |
|---|---|---|---|
| `R1.1` | 04, 06 | credential hashing + fail-closed lockout (04); registration minimization (06) | Bound (RN10, RN11, RN19) |
| `R1.2` | 01, 07 | profile records inside the boundary (01); privacy audit trail (07) | Bound (RN23, RN26) |
| `R1.3` | 04, 07 | recovery fails closed (04); recovery attempts audit-logged (07) | Bound (RN10, RN11, RN18) |
| `R2.1` | 03 | tenant isolation from birth | Bound (RN9; P-02 pending for defaults) |
| `R2.2` | 03 | RBAC mediation on membership mutations | Bound (RN12) |
| `R2.3` | 03 | purpose-scoped aggregation | Bound (RN22) |
| `R3.1` | 03 | project containers inside the tenant boundary | Bound (RN9; P-02 pending for defaults) |
| `R3.2` | — | no security surface beyond archive mediation (covered via `{U.C. 3.2}` extension, RN12) | Covered via UC |
| `R4.1` | 02 | content neutralization on task fields | Bound (RN14 via `{U.C. 4.1}` extension) |
| `R4.2` | 02 | transition flood throttling | Bound (RN17 via `{U.C. 4.2}`) |
| `R4.3` | 03 | daemon isolation | Bound (RN9 precondition) |
| `R5.1` | 02, 07 | upload surface minimization (02); retention purge (07) | Bound (RN13, RN25) |
| `R5.2` | 02, 04 | content neutralization (02); fail-safe sanitization (04) | Bound (RN14) |
| `R6.1` | 02, 03 | query throttling (02); purpose scoping (03) | Bound (RN17, RN22) |
| `R6.2` | 01 | verified notification origin across the boundary | Bound (RN16) |
| `R7.1` | 01, 04 | gateway mediation (01); forged-receipt fail-closed (04) | Bound (RN15) |
| `R7.2` | 01, 04 | verified payment events (01); restricted-state fail-securely (04) | Bound (RN15 + functional) |
| `R8.1` | 01, 03, 06 | mediated export (01); Owner-only workspace archive (03); own-data-only archive (06) | Bound (RN20, RN12 via extension; P-01 pending identity) |
| `R8.2` | 01, 07 | mediated erasure execution (01); irreversible + non-repudiable erasure (07) | Bound (RN21, RN18; P-01 pending identity) |

**Cross-cutting principles (not per-card):** PRIN-ENG-05 (verifiability — structural, all cards); RN17 (rate limiting), RN18 (audit logging), RN24 (transport encryption) live as standalone Quality Attributes rows binding every UC.

---

## §3 Coverage Totals & Gaps

| Surface | Count | Notes |
|---|---|---|
| Principles followed | 7/7 | every principle has ≥1 realization; none without a carrier |
| Pending principle gaps | 2 | P-01 (PRIN-ENG-01 mediation of rights execution), P-02 (PRIN-ENG-04 secure-by-default configuration) — both already proposed in the open round |
| Requirements realizing ≥1 principle | 18/19 | `R3.2` realized at UC level (extension) |
| Pending re-drives touching principle chains | 10 RNs | ADJ-1…ADJ-9 (drivers, not principles) — see register |

**Read rule:** gaps in this matrix are **principle gaps**, not requirement defects — they feed the open round in [`RISK_ACCEPTANCE_REGISTER.md`](RISK_ACCEPTANCE_REGISTER.md) as proposals; nothing is silently accepted.
