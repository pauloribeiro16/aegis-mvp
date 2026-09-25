# UC ↔ Phase 2 Objective Correspondence Matrix (TinyTask SaaS)


## §1 Correspondence Grid (objective × UC package)

Columns are the functional packages (`R1`–`R8`); cells list the UCs `{n.m}` where the objective binds and the `RN` carrying it. UC-level detail (what each objective demands there) is in §2.

| Objective | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| `PO-D-01.1-001` (GDPR) (data at rest security) | `{1.2}` RN23 | — | — | — | — | — | — | — |
| `SO-D-01.1-002` (CRA) (encryption at rest, SotA) | `{1.1}` `{1.3}` RN10 | — | — | — | — | — | `{7.1}` `{7.2}` RN15† | — |
| `PO-D-01.2-001` (GDPR) (data in transit) | `{1.1}` RN24 (pre) — cross-cutting: all transport flows | ← | ← | ← | ← | ← | ← | ← |
| `SO-D-01.2-002` (CRA) (CRA twin, in transit) | `{1.1}` RN24† (pre; ADJ-9 twin driver) — cross-cutting | ← | ← | ← | ← | ← | ← | ← |
| `PO-D-01.4-001` (GDPR) (accuracy & rectification) | `{1.2}` (R1.2 Must — D3, no RN) | — | — | — | — | — | — | — |
| `SO-D-01.4-002` (CRA) (integrity of data & commands) | — | — | — | — | — | `{6.2}` RN16† | `{7.1}` `{7.2}` RN15† | — |
| `SO-D-03.1-002` (CRA) (identity/credential management) | `{1.1}` `{1.3}` RN11† | — | — | — | — | — | — | — |
| `SO-D-03.2-002` (CRA) (protection from unauthorised access) | `{1.2}` RN9† (pre) | `{2.1}` `{2.3}` `{4.3}` RN9† | `{3.1}` RN9† | `{4.1}` RN9† (pre) | — | `{6.1}` RN9† (pre) | — | — |
| `SO-D-03.3-002` (CRA) (authenticated & authorized access) | — | `{2.2}` RN12† | `{3.1}` `{3.2}` RN12† (ext) | — | — | — | — | `{8.1}` RN12† (ext) |
| `SO-D-03.4-001` (CRA) (by-default only necessary data) | `{1.1}` RN19 | — | — | — | — | — | — | — |
| `PO-D-05.2-001` (GDPR) (retention limitation) | — | — | — | — | `{5.1}` RN25 | — | — | — |
| `PO-D-05.3-001` (GDPR) (erasure on request) | — | — | — | — | — | — | — | `{8.2}` RN21 |
| `PO-D-05.4-001` (GDPR) (portability) | — | — | — | — | — | — | — | `{8.1}` RN20 |
| `SO-D-05.1-002` (CRA) (CRA twin, data limitation) | — *(realized functionally by RN19/RN25; no direct chain)* | — | — | — | — | — | — | — |
| `SO-D-07.2-002` (CRA) (attack-surface limitation) | — | — | — | `{4.1}` RN14† (ext) `{4.2}` `{6.1}` RN17† | `{5.1}` RN13† `{5.2}` RN14† | — | — | — |
| `SO-D-07.1-002` (CRA) (Annex I umbrella) | — *(umbrella; direct chains re-driven by ADJ-4/ADJ-6)* | — | — | — | — | — | — | — |
| `SO-D-08.1-002` (CRA) (secure-use instructions) | — | — | — | — | — | — | — | — *(P-04 pending: documentation coverage)* |
| `PO-D-09.4-001` (GDPR) (Art. 30 records) | `{1.2}` RN26 | — | — | — | — | — | — | — |
| `SO-D-10.1-002` (CRA) (records & monitors activity) | `{1.1}` `{1.3}` RN18† | `{2.1}` `{2.2}` `{2.3}` RN18† | `{3.1}` `{3.2}` RN18† | `{4.3}` RN18† | — | `{6.1}` RN18† | `{7.1}` `{7.2}` RN18† | `{8.2}` RN18† |

### Principles (transversal)

| Principle | Bound RNs |
|---|---|
| `PRIN-ENG-01` (trust boundaries & complete mediation) | RN15†, RN16†, RN23, RN24 |
| `PRIN-ENG-02` (attack-surface minimization) | RN13†, RN17† |
| `PRIN-ENG-03` (least privilege & mechanism isolation) | RN9†, RN12†, RN22 |
| `PRIN-ENG-04` (fail-safe defaults) | RN10, RN11†, RN14† |
| `PRIN-ENG-05` (atomic verifiability) | global — realized by the Volere fit criterion + verification method on every RN/proposal (recorded once here) |
| `PRIN-ENG-06` (default-on privacy & minimization) | RN19, RN20 |
| `PRIN-ENG-07` (non-repudiable observability) | RN18†, RN21, RN25, RN26 |

### Pending new proposals (Round 1, no RN yet)

| Item | UCs affected | Content |
|---|---|---|
| P-01 | `{8.1}` `{8.2}` | Identity verification before rights-exercise execution (`SO-D-03.1-001`) |
| P-02 | `{2.1}` `{3.1}` | Restrictive secure-by-default configuration on new artifacts (`SO-D-03.4-002`) |
| P-03 | new `{8.3}` (D1 candidate `R8.3`) | Owner workspace deletion with permanent erasure (`SO-D-05.3-002`) |
| P-04 | package-level (documentation surface) | Secure-use instructions coverage (`SO-D-08.1-002`, SHOULD) |

---

## §2 Per-UC Correspondence Cards

### `{U.C. 1.1}` Register and authenticate user accounts

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-01.1-002` | CRA | Stored credentials protected with state-of-the-art mechanisms (not recoverable) | TB | RN10 | Covered |
| `SO-D-03.1-002` | CRA | Credentials and session entitlements managed and invalidated in a verified way | LP | RN11 | ADJ-2 pending (current driver `SO-D-02.2-002`) |
| `SO-D-03.4-001` | CRA | Registration collects only the necessary personal data | DM | RN19 | Covered |
| `SO-D-10.1-002` | CRA | Authentication attempts (incl. lockouts) recorded for monitoring | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `PO-D-01.2-001` | GDPR | Session/credential traffic confidential in transit | TB | RN24 | Cross-cutting (precondition) |
| `PRIN-ENG-04` | — | Authentication decisions default to refusal; lockout fails closed | FS | RN10, RN11† | Bound |


### `{U.C. 1.2}` Manage user profile and account preferences

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `PO-D-01.1-001` | GDPR | Profile personal data at rest appropriately protected | TB | RN23 | Covered |
| `PO-D-09.4-001` | GDPR | Profile modifications emit a privacy audit record (Art. 30 accountability) | V | RN26 | Covered |
| `PO-D-01.4-001` | GDPR | Inaccurate personal data rectifiable without delay (profile editing is the mechanism) | V | — | Covered (R1.2 Must, D3) |
| `PRIN-ENG-01` | — | Profile records protected within the trust boundary | TB | RN23 | Bound |


### `{U.C. 1.3}` Recover access to a locked user account

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-01.1-002` | CRA | Recovery proves identity without weakening stored-credential protection | TB | RN10 | Covered |
| `SO-D-03.1-002` | CRA | Recovery invalidates all sessions (entitlement reset) | LP | RN11 | ADJ-2 pending (current driver `SO-D-02.2-002`) |
| `SO-D-10.1-002` | CRA | Recovery attempts recorded in the audit log | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `PRIN-ENG-04` | — | Recovery fails closed on expired/reused links; enumeration-resistant neutral responses | FS | RN10 | Bound |


### `{U.C. 2.1}` Create and configure workspace

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-03.2-002` | CRA | New workspace container isolated from birth (tenant boundary) | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |
| `SO-D-10.1-002` | CRA | Provisioning attempt recorded; isolation violations logged | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `SO-D-03.4-002` | CRA | Workspace starts with restrictive secure-by-default configuration | FS | — | P-02 pending |
| `PRIN-ENG-03` | — | Tenant context enforced on every provisioning action | LP | RN9† | Bound |


### `{U.C. 2.2}` Invite workspace members and manage access roles

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-03.3-002` | CRA | Role mutations only by authenticated, authorized admins; Owner irremovable | LP | RN12 | ADJ-3 pending (current driver `SO-D-02.1-002`) |
| `SO-D-10.1-002` | CRA | Role modifications and denials permanently logged | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `PRIN-ENG-03` | — | RBAC mediation before every membership action | LP | RN12† | Bound |


### `{U.C. 2.3}` Monitor workspace activity and operational metrics

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | GDPR | Aggregated metrics used only for the stated purpose; no surveillance creep | DM | RN22 | Covered |
| `SO-D-03.2-002` | CRA | Metrics queries tenant-scoped; cross-tenant probes blocked | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |
| `SO-D-10.1-002` | CRA | Isolation-breach attempts on metrics logged | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |


### `{U.C. 3.1}` Create and configure projects

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-03.2-002` | CRA | Project container created inside the tenant boundary | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |
| `SO-D-03.3-002` | CRA | Creation restricted to authorized members; violations logged | LP | RN12 | ADJ-3 pending (current driver `SO-D-02.1-002`) |
| `SO-D-03.4-002` | CRA | New projects default to restricted visibility | FS | — | P-02 pending |
| `SO-D-10.1-002` | CRA | Creation and unauthorized-attempt events recorded | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |


### `{U.C. 3.2}` Archive completed projects

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-03.3-002` | CRA | Archive transition only by Admin/Owner; unauthorized attempts denied and logged | LP | RN12 | ADJ-3 pending (current driver `SO-D-02.1-002`; via extension 3b) |
| `SO-D-10.1-002` | CRA | Access violations on archive recorded | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`; via extension 3b) |


### `{U.C. 4.1}` Create and assign tasks

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-07.2-002` | CRA | Task title/description neutralized against embedded active payloads | AS | RN14 | ADJ-6 pending (current driver `SO-D-07.1-002`; via extension 3b) |
| `SO-D-03.2-002` | CRA | Task created within the authorized project/tenant context (precondition) | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |


### `{U.C. 4.2}` Track and transition task workflow states on visual boards

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-07.2-002` | CRA | Transition request flood throttled (attack-surface resilience) | AS | RN17 | ADJ-4 pending (current drivers `SO-D-02.1-002`/`SO-D-05.1-002`; via extension 2b) |


### `{U.C. 4.3}` Configure recurring automated tasks

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-03.2-002` | CRA | Daemon executes in an isolated service context (precondition) | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |
| `SO-D-10.1-002` | CRA | Automation skips/failures logged (extension 2a) | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |


### `{U.C. 5.1}` Manage task deliverable attachments

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-07.2-002` | CRA | Uploads validated against declared type + content signature; executables rejected | AS | RN13 | ADJ-4 pending (current driver `SO-D-07.1-002`) |
| `PO-D-05.2-001` | GDPR | Deleted attachments purged on a retention schedule, not kept indefinitely | LE | RN25 | Covered |
| `PRIN-ENG-02` | — | Upload surface minimized; disallowed types rejected at the boundary | AS | RN13† | Bound |


### `{U.C. 5.2}` Post in-task discussion comments and mention collaborators

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-07.2-002` | CRA | Rendered comments cannot carry executable payloads (inert text) | AS | RN14 | ADJ-6 pending (current driver `SO-D-07.1-002`) |
| `PRIN-ENG-04` | — | Sanitization fails safe — payloads never executed by default | FS | RN14† | Bound |


### `{U.C. 6.1}` Consult chronological audit history on task cards

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `PO-D-05.1-001` | GDPR | Audit feed used only for its stated purpose (no productivity surveillance) | DM | RN22 | Covered |
| `SO-D-07.2-002` | CRA | Audit queries paginated/throttled against exhaustion | AS | RN17 | ADJ-4 pending (current drivers `SO-D-02.1-002`/`SO-D-05.1-002`; via extension 2b) |
| `SO-D-10.1-002` | CRA | History entries read-only, tamper-proof via the recording objective | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `SO-D-03.2-002` | CRA | Query scoped to the authorized tenant (precondition) | TB | RN9 | ADJ-1 pending (current driver `SO-D-02.1-002`) |


### `{U.C. 6.2}` Receive workspace alerts and daily task digests

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-01.4-002` | CRA | Digest/notification pipeline integrity — no forged or altered alerts | V | RN16 | ADJ-8 pending (current drivers `SO-D-05.1-002`/`SO-D-08.1-002`) |
| `PRIN-ENG-01` | — | Notification transport crosses the trust boundary with verified origin | TB | RN16† | Bound |


### `{U.C. 7.1}` Subscribe and manage workspace commercial plans

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-01.4-002` | CRA | Billing state changes only on integrity-verified receipts (no forged upgrades) | V | RN15 | ADJ-7 pending (current driver `SO-D-01.1-002`) |
| `SO-D-10.1-002` | CRA | Forged-webhook rejections recorded | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`; via extension 5c) |
| `PRIN-ENG-01` | — | Gateway responses cross the trust boundary with complete mediation | TB | RN15† | Bound |


### `{U.C. 7.2}` Enforce operational grace period upon payment failure

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `SO-D-01.4-002` | CRA | Grace-period transitions driven by integrity-verified payment events | V | RN15 | ADJ-7 pending (current driver `SO-D-01.1-002`) |
| `SO-D-10.1-002` | CRA | Replay detection and grace-state changes emit audit records | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`; via extension 3a) |
| `PRIN-ENG-04` | — | Fail-securely: expired grace → restricted read-only state, never silent open access | FS | — (R7.2 description, D2) | Bound |


### `{U.C. 8.1}` Export personal and workspace data archives

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `PO-D-05.4-001` | GDPR | Export delivered structured, machine-readable, without undue delay | LE | RN20 | Covered |
| `SO-D-03.3-002` | CRA | Workspace-level export restricted to the Owner (extension) | LP | RN12 | ADJ-3 pending (current driver `SO-D-02.1-002`) |
| `SO-D-03.1-002` | CRA | Export links single-use and expiring (session/entitlement hygiene) | LP | RN11 | ADJ-2 pending (current driver `SO-D-02.2-002`; via extension 4b) |
| `SO-D-03.1-001` | CRA | Requester identity verified before executing the export | TB | — | P-01 pending |
| `PRIN-ENG-06` | — | Archive limited to the requester's own data (no third-party leakage) | DM | RN20 | Bound |


### `{U.C. 8.2}` Close user accounts and terminate workspace access

| Objective / Principle | Reg | What it demands here | Skill | RN | State |
|---|---|---|---|---|---|
| `PO-D-05.3-001` | GDPR | Erasure without undue delay on request; irreversible + pseudonymized | LE | RN21 | Covered |
| `SO-D-03.1-002` | CRA | Closure invalidates all sessions/tokens (entitlement revocation) | LP | RN11 | ADJ-2 pending (current driver `SO-D-02.2-002`; via extension 5c) |
| `SO-D-10.1-002` | CRA | Closure and pseudonymization audit-logged | V | RN18 | ADJ-5 pending (current driver `SO-D-03.1-002`) |
| `SO-D-03.1-001` | CRA | Requester identity verified before executing the erasure | TB | — | P-01 pending |
| `PRIN-ENG-07` | — | Erasure non-repudiable: receipt issued, audit trail preserved | V | RN21, RN18† | Bound |


_(A `{U.C. 8.3}` Owner-workspace-deletion card becomes applicable if P-03 is accepted — see the pending block in §1.)_

---

## §3 Coverage Totals

| Surface | Count | Notes |
|---|---|---|
| UC cards | 19/19 | every use case has an explicit correspondence section; none silent |
| Objectives with UC bindings (target state) | 14 | rows in §1 with ≥1 cell; + 4 noted rows (twins/umbrella/instructions) |
| Objectives without UC binding | 44 | 31 no-functional-carrier + 2 design guidance + 3 N/A + SO-D-08.1-002 (P-04 documentation surface) — verdicts in `OBJECTIVE_MAPPING.md` |
| Pending re-drives marked † | 10 RNs | ADJ-1…ADJ-9 (see register) |
| Pending new proposals | 4 | P-01…P-04 |
| Most-covered UC | `{U.C. 1.1}` (5 rows) | authentication surface |
| Least-covered UC | `{U.C. 4.2}` (1 row) | throttling only — matches the V0 "no security surface" reading |

**Read rule:** every binding above traces to a chain that satisfies the anchor-integrity rule (chain anchors ∈ the cited objective's published control set); pending items take effect only after the client's verdicts, recorded in the round documentation.
