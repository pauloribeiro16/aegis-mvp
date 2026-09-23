# V0 → V1 → V2 Analysis Tables — TinyTask SaaS

> **Document Purpose:** Tabular view of the V0 functional baseline, V2 consolidated top-level, and V1 security & privacy synthesis — each functional requirement appears once with its V0 essence, V2 state, and V1 RN bindings side by side.

> **Source of Truth:** `v0_functional_baseline/` (V0, LOCKED) · top-level `Doc01`/`Doc02` (V2, consolidated) · `v1_security_privacy_synthesis/` (V1, APPROVED).

---

## §1 Version Ladder (what each V contains)

| Version | Path | Role | Requirements | Non-Functional | Security & Privacy | Status |
|---|---|---|---|---|---|---|
| **V0** | `v0_functional_baseline/` | Pure functional snapshot — 8 capability packages, 18 atomic requirement cards, 18 PUCs, 18 Sea-Level UCs. | 18 (`R1.1`–`R8.2`) | 0 | 0 | LOCKED |
| **V1** | `v1_security_privacy_synthesis/` | V0 augmented with security & privacy synthesis — Doc03 RN9–RN26 in 7-row anatomy; V0 Doc01/Doc02 augmented with RN traces. | 18 (unchanged) | 8 (`RN1`–`RN8`) | 18 (`RN9`–`RN26`) | APPROVED |
| **V2** | top-level `Doc01`/`Doc02` | Consolidated top-level — pure functional baseline at v2.1 with anti-pattern cleanup; security & privacy traceability carried through v1 traceability matrix. | 18 (consolidated R-codes) | 8 (`RN1`–`RN8`) | 0 (RN9–RN26 absorbed via v1 traceability matrix) | ACTIVE |

## §2 Master Matrix per Functional Requirement (R)

| Req ID | Requirement Name | Priority | V0 Essence (verbatim from snapshot) | V2 State (top-level) | V1 Synthesis (RN bound) | Phase 2 Upstream Origin | Verification Method(s) |
|---|---|---|---|---|---|---|---|
| `R1.1` | Register and authenticate user accounts | Must | The system must allow prospective users to create an account with email verification, authenticate using valid credentials to establish an active session, and autonomously request password reset assistance via email. | Verbatim copy of V0 (no consolidation delta). | `RN10`, `RN11`, `RN18`, `RN19`, `RN21`, `RN23`, `RN24`, `RN26` | `SO-D-02.1-002`, `SO-D-01.1-002` | RN10: `TEST` (Automated unit t; RN11: `TEST` (Automated sessio; RN18: `TEST` (Audit log genera; RN19: `INSPECT` (Data schema a; RN21: `TEST` (Automated accoun; RN23: `INSPECT` (Infrastructur; RN24: `TEST` (Automated networ; RN26: `INSPECT` (Privacy audit |
| `R1.2` | Manage user profile and account preferences | Should | The system must allow an authenticated user to view and update their personal profile details (full name, avatar image, and contact details) and configure notification preferences. | Verbatim copy of V0 (no consolidation delta). | `RN9`, `RN20`, `RN21`, `RN23`, `RN26` | `SO-D-02.1-002` | RN9: `TEST` (Automated integr; RN20: `DEMONSTRATE` (End-to-en; RN21: `TEST` (Automated accoun; RN23: `INSPECT` (Infrastructur; RN26: `INSPECT` (Privacy audit |
| `R2.1` | Create and configure workspace | Must | The system must allow an authenticated user to instantiate an isolated organizational workspace by specifying a workspace name and unique URL slug, automatically assigning the creator as Workspace Owner and permitting subsequent configuration of workspace branding and organization name. | Verbatim copy of V0 (no consolidation delta). | `RN9`, `RN12` | `SO-D-02.1-002` | RN9: `TEST` (Automated integr; RN12: `TEST` (RBAC matrix perm |
| `R2.2` | Invite workspace members and manage access roles | Must | The system must allow Workspace Admins and Owners to invite team members via email, assign access roles (Owner, Admin, Member, Viewer) that govern operational permissions within the workspace, modify member roles, or revoke membership, respecting active seat limits. | Verbatim copy of V0 (no consolidation delta). | `RN12` | `SO-D-02.1-002` | RN12: `TEST` (RBAC matrix perm |
| `R2.3` | Monitor workspace activity and operational metrics | Could | The system must compile and present aggregated operational metrics to workspace leadership, displaying active member counts, tasks completed during the billing cycle, and total deliverable file storage consumed. | Verbatim copy of V0 (no consolidation delta). | — | — | — |
| `R3.1` | Create and configure projects | Must | The system must allow Workspace Admins and Members to initialize distinct project containers within a workspace, specifying project name, description of deliverables, and visibility settings (workspace-wide or restricted to selected members). | Verbatim copy of V0 (no consolidation delta). | `RN9`, `RN12` | `SO-D-02.1-002` | RN9: `TEST` (Automated integr; RN12: `TEST` (RBAC matrix perm |
| `R3.2` | Archive completed projects | Should | The system must allow Workspace Admins and Owners to transition completed projects into archived status, rendering all tasks and discussions read-only and hiding the project from daily operational views while preserving historical data. | Verbatim copy of V0 (no consolidation delta). | — | — | — |
| `R4.1` | Create and assign tasks | Must | The system must allow authorized team members to create tasks within a project by specifying a mandatory title, optional description, priority level (Low, Medium, High, Urgent), and target due date, and assign execution responsibility to one or more active workspace members. | Verbatim copy of V0 (no consolidation delta). | `RN13` | `SO-D-07.1-002` | RN13: `TEST` (Malicious payloa |
| `R4.2` | Track and transition task workflow states on visual boards | Must | The system must render tasks in interactive Kanban boards with standard status columns (To-Do, In-Progress, Under-Review, Done) and tabular views, allowing members to transition cards between states and filter tasks dynamically by assignee, status, priority, or overdue status. | Verbatim copy of V0 (no consolidation delta). | `RN13`, `RN25` | `SO-D-07.1-002` | RN13: `TEST` (Malicious payloa; RN25: `TEST` (Lifecycle expira |
| `R4.3` | Configure recurring automated tasks | Could | The system must allow users to configure recurrence schedules (weekly or monthly) on a task, automatically creating a duplicate task instance in the "To-Do" column once the current instance is marked "Done". | Verbatim copy of V0 (no consolidation delta). | — | — | — |
| `R5.1` | Manage task deliverable attachments | Must | The system must allow authorized team members to upload deliverable files (supporting documents, spreadsheets, presentations, and images) up to 25 MB in size per file directly into a task card, view inline previews, download attached files, and remove outdated attachments. | Verbatim copy of V0 (no consolidation delta). | `RN14` | `SO-D-07.1-002` | RN14: `TEST` (Automated browse |
| `R5.2` | Post in-task discussion comments and mention collaborators | Must | The system must provide a contextual comment thread inside each task card supporting rich text Markdown formatting and parsing collaborator mentions (@user) to automatically dispatch in-app notifications to tagged users. | Verbatim copy of V0 (no consolidation delta). | — | — | — |
| `R6.1` | Consult chronological audit history on task cards | Must | The system must record and display a chronological audit feed on each task card documenting state changes, assignee reallocations, due date adjustments, and attachment events, identifying author and timestamp. | Verbatim copy of V0 (no consolidation delta). | `RN22`, `RN23`, `RN26` | `PO-D-06.1-001` | RN22: `ANALYZE` (Data flow aud; RN23: `INSPECT` (Infrastructur; RN26: `INSPECT` (Privacy audit |
| `R6.2` | Receive workspace alerts and daily task digests | Should | The system must provide an in-app notification center for direct assignments and @mentions, and automatically dispatch a daily summary email digest listing upcoming and overdue tasks assigned to the user. | Verbatim copy of V0 (no consolidation delta). | `RN22` | `PO-D-06.1-001` | RN22: `ANALYZE` (Data flow aud |
| `R7.1` | Subscribe and manage workspace commercial plans | Must | The system must allow the Workspace Owner to select a commercial plan tier (Free, Pro, Enterprise) and complete checkout via the external payment gateway, automatically updating workspace plan status, renewal date, and authorized member seat quotas upon payment confirmation. | Verbatim copy of V0 (no consolidation delta). | `RN15` | `SO-D-01.1-002`, `SO-D-08.1-002` | RN15: `TEST` (Mock payment gat |
| `R7.2` | Enforce operational grace period upon payment failure | Must | The system must grant a 7-day operational grace period if an automated subscription renewal payment fails, maintaining normal workspace access while presenting payment update notices to the Workspace Owner before applying plan restrictions. | Verbatim copy of V0 (no consolidation delta). | `RN15` | `SO-D-01.1-002`, `SO-D-08.1-002` | RN15: `TEST` (Mock payment gat |
| `R8.1` | Export personal and workspace data archives | Must | The system must allow authenticated users to download a structured export of their personal profile and authored tasks, and allow Workspace Owners to export a comprehensive archive of workspace projects, tasks, comments, and attachments. | Verbatim copy of V0 (no consolidation delta). | `RN16` | `SO-D-05.1-002`, `SO-D-08.1-002` | RN16: `TEST` (Webhook payload  |
| `R8.2` | Close user accounts and terminate workspace access | Must | The system must allow users to autonomously terminate their accounts, invalidating active credentials and sessions, ending active workspace memberships, and dispatching a formal confirmation receipt via email. | Verbatim copy of V0 (no consolidation delta). | `RN17`, `RN18`, `RN24` | `SO-D-02.1-002`, `SO-D-05.1-002` | RN17: `TEST` (Automated API ra; RN18: `TEST` (Audit log genera; RN24: `TEST` (Automated networ |

## §3 Synthesis Trace: Security & Privacy Requirements (RN9–RN26)

| RN ID | Name | Regulatory Driver | Phase 2 Upstream | Phase 3 Functional Bound | Phase 3 Use Case Bound | Fit Criterion (verbatim) | Verification Method |
|---|---|---|---|---|---|---|---|
| `RN9` | Multi-Tenant Data Isolation & Mediation | CRA (Product Cyber Resilience) | `SO-D-02.1-002` | `R1.2`, `R2.1`, `R3.1` | {U.C. 1.2}, {U.C. 2.1}, {U.C. 3.1} | 100% of synthetic cross-tenant query probes executed during automated integration testing return HTTP 403 Forbidden with zero records leaked.
- **Verification Method:** `TEST` (Automated integration suite executing cross-tenant injection vectors). | `TEST` (Automated integration suite executing cross-tenant injection vectors). |
| `RN10` | Credential Hardening & Salted Hashing | CRA (Product Cyber Resilience) | `SO-D-02.1-002`, `SO-D-01.1-002` | `R1.1` | {U.C. 1.1} | Inspection of persistent user tables and application logs confirms zero plaintext password instances, and stored password fields match standard cryptographic hash digest formats with unique salt lengths >= 16 bytes.
- **Verification Method:** `TEST` (Automated unit tests validating hash derivation and entropy). | `TEST` (Automated unit tests validating hash derivation and entropy). |
| `RN11` | Cryptographic Session Management & Invalidation | CRA (Product Cyber Resilience) | `SO-D-02.2-002` | `R1.1` | {U.C. 1.1} | Post-logout or expired session tokens submitted to protected API endpoints are rejected with HTTP 401 Unauthorized within 100 milliseconds.
- **Verification Method:** `TEST` (Automated session invalidation test suite). | `TEST` (Automated session invalidation test suite). |
| `RN12` | Role-Based Access Control & Action Mediation | CRA (Product Cyber Resilience) | `SO-D-02.1-002` | `R2.1`, `R2.2`, `R3.1` | {U.C. 2.1}, {U.C. 2.2}, {U.C. 3.1} | Standard workspace members attempting administrative mutations receive an HTTP 403 response; database audit logs record timestamp, actor ID, and target resource.
- **Verification Method:** `TEST` (RBAC matrix permission verification suite). | `TEST` (RBAC matrix permission verification suite). |
| `RN13` | File Upload Strict Validation & Content Isolation | CRA (Product Cyber Resilience) | `SO-D-07.1-002` | `R4.1`, `R4.2` | {U.C. 4.1}, {U.C. 4.2} | Submissions of spoofed executable binaries (e.g. `.exe` renamed to `.pdf`) are rejected with an explicit validation error, and zero temporary files remain on disk.
- **Verification Method:** `TEST` (Malicious payload upload and MIME-mismatch test suite). | `TEST` (Malicious payload upload and MIME-mismatch test suite). |
| `RN14` | Context-Aware Output Encoding & Sanitization | CRA (Product Cyber Resilience) | `SO-D-07.1-002` | `R5.1` | {U.C. 5.1} | 100% of stored XSS test vectors injected into comment fields are rendered as inert text entities with zero script execution.
- **Verification Method:** `TEST` (Automated browser-based dynamic security assertion). | `TEST` (Automated browser-based dynamic security assertion). |
| `RN15` | Cryptographic Billing Invariant Protection | CRA (Product Cyber Resilience) | `SO-D-01.1-002`, `SO-D-08.1-002` | `R7.1`, `R7.2` | {U.C. 7.1}, {U.C. 7.2} | Simulated unauthenticated or forged payment webhooks fail signature validation and produce zero changes in tenant billing status.
- **Verification Method:** `TEST` (Mock payment gateway webhook signature suite). | `TEST` (Mock payment gateway webhook signature suite). |
| `RN16` | Cryptographic Webhook Origin Verification | CRA (Product Cyber Resilience) | `SO-D-05.1-002`, `SO-D-08.1-002` | `R8.1` | {U.C. 8.1} | Receiver test harness validates payload integrity and origin authenticity using the shared secret; any payload byte tampering invalidates the computed authentication proof.
- **Verification Method:** `TEST` (Webhook payload integrity and tamper assertion suite). | `TEST` (Webhook payload integrity and tamper assertion suite). |
| `RN17` | Inbound API Token Mediation & Rate Limiting | CRA (Product Cyber Resilience) | `SO-D-02.1-002`, `SO-D-05.1-002` | `R8.2` | {U.C. 8.2} | Automated load generator exceeding 100 req/min receives HTTP 429 starting at request 101, recovering exactly when the time window resets.
- **Verification Method:** `TEST` (Automated API rate limiting and token validation harness). | `TEST` (Automated API rate limiting and token validation harness). |
| `RN18` | Non-Repudiable Security Audit Logging | CRA (Product Cyber Resilience) | `SO-D-03.1-002` | `R1.1`, `R8.2` | — | Audit log files are append-only; administrative users cannot alter or truncate audit entries; 100% of sensitive operations generate an audit log entry.
- **Verification Method:** `TEST` (Audit log generation and append-only tamper test).

---

## 4. Personal Data Protection Requirements (GDPR Specification — `RN19` to `RN26`) | `TEST` (Audit log generation and append-only tamper test).

---

## 4. Personal Data Protection Requirements (GDPR Specification — `RN19` to `RN26`) |
| `RN19` | Registration Data Minimization by Default | GDPR (Personal Data Protection) | `PO-D-06.1-001` | `R1.1` | {U.C. 1.1} | Database schema inspection confirms zero mandatory extraneous personal fields; registration form contains only the 3 strictly necessary identity fields.
- **Verification Method:** `INSPECT` (Data schema and user onboarding field audit). | `INSPECT` (Data schema and user onboarding field audit). |
| `RN20` | Structured Personal Data Portability & Export | GDPR (Personal Data Protection) | `PO-D-06.2-001` | `R1.2` | {U.C. 1.2} | Export package contains 100% of user-generated data formatted in valid, schema-conforming JSON without inclusion of third-party personal data.
- **Verification Method:** `DEMONSTRATE` (End-to-end data portability generation and schema validation). | `DEMONSTRATE` (End-to-end data portability generation and schema validation). |
| `RN21` | Irreversible Data Subject Erasure & Pseudonymization | GDPR (Personal Data Protection) | `PO-D-06.2-001` | `R1.1`, `R1.2` | {U.C. 1.1}, {U.C. 1.2} | Post-erasure database search for the user's email or full name yields zero matches; historical records display a non-reversible pseudonym (e.g. `Deactivated User [ID: 9481]`).
- **Verification Method:** `TEST` (Automated account erasure pipeline and pseudonymization check). | `TEST` (Automated account erasure pipeline and pseudonymization check). |
| `RN22` | Purpose Limitation & Time Log Segregation | GDPR (Personal Data Protection) | `PO-D-06.1-001` | `R6.1`, `R6.2` | {U.C. 6.1}, {U.C. 6.2} | Query interface and analytics exports restrict aggregations to project and workspace summaries; individual granular logs are accessible only to the author and the authorized workspace administrator.
- **Verification Method:** `ANALYZE` (Data flow audit verifying access controls on time logging entities). | `ANALYZE` (Data flow audit verifying access controls on time logging entities). |
| `RN23` | Personal Data Cryptographic Protection at Rest | GDPR (Personal Data Protection) | `PO-D-01.1-001` | `R1.1`, `R1.2`, `R6.1` | {U.C. 1.1}, {U.C. 1.2}, {U.C. 6.1} | Storage infrastructure manifests and volume configuration scripts confirm transparent cryptographic protection is enabled with managed key rotation.
- **Verification Method:** `INSPECT` (Infrastructure-as-Code and volume configuration audit). | `INSPECT` (Infrastructure-as-Code and volume configuration audit). |
| `RN24` | Mandatory End-to-End Transport Layer Cryptographic Protection | GDPR (Personal Data Protection) | `PO-D-01.2-001` | `R1.1`, `R8.2` | — | 100% of network traffic traversing external boundaries is cryptographically protected; unencrypted transmission attempts fail closed.
- **Verification Method:** `TEST` (Automated network inspection verifying cryptographic transport protection on all external endpoints). | `TEST` (Automated network inspection verifying cryptographic transport protection on all external endpoints). |
| `RN25` | Automated Orphan File Asset Cleanup & Expiration | GDPR (Personal Data Protection) | `PO-D-06.1-001` | `R4.2` | {U.C. 4.2} | Background cleanup job successfully purges unreferenced storage files older than 14 days; object store audit verifies zero orphaned attachments remain.
- **Verification Method:** `TEST` (Lifecycle expiration assertion on object storage). | `TEST` (Lifecycle expiration assertion on object storage). |
| `RN26` | Privacy Audit Trail for Personal Data Modifications | GDPR (Personal Data Protection) | `PO-D-03.1-001` | `R1.1`, `R1.2`, `R6.1` | {U.C. 1.1}, {U.C. 1.2}, {U.C. 6.1} | 100% of profile update and data deletion requests generate a structured audit record verifiable by the Data Protection Lead.
- **Verification Method:** `INSPECT` (Privacy audit log completeness review).

--- | `INSPECT` (Privacy audit log completeness review).

--- |

## §4 Use Case Security Augmentation ({U.C. 1.1} to {U.C. 8.2})

| UC ID | UC Name | Security & Privacy Traces (RN) | Preconditions (V1 augmentation) | Minimal Guarantees (V1 augmentation) |
|---|---|---|---|---|
| `{U.C. 1.1}` | Register and authenticate user accounts | `RN10` (Credential Hashing), `RN11` (Session Invalidation), `RN18` (Audit Logging), `RN19` (Data Minimization), `RN24` (Transport Encryption) | network connection terminates over a secure encrypted channel (RN24); The user has access to a valid email inbox. | Failed attempts leave database credentials unmodified; security audit log records timestamp and client IP for every rejected attempt; zero credentials or session tokens are leaked (RN18).

--- |
| `{U.C. 1.2}` | Manage user profile and account preferences | `RN9` (Tenant Isolation), `RN20` (Portability), `RN23` (Encryption at Rest), `RN26` (Privacy Audit Trail) | token is authenticated and bound to target organization (RN9); User possesses an active authenticated session. | Existing profile data remains unchanged if validation fails; profile modifications emit a structured privacy audit record (RN26).

--- |
| `{U.C. 2.1}` | Create and configure workspace | `RN9` (Multi-Tenant Isolation), `RN12` (Role-Based Access Control), `RN18` (Audit Logging) | actor possesses valid authenticated session (RN9); Actor has an active authenticated user account. | No partially provisioned workspace records remain if container provisioning fails; audit log records provisioning attempt (RN18).

--- |
| `{U.C. 2.2}` | Invite workspace members and manage access roles | `RN12` (RBAC), `RN18` (Audit Logging), `RN19` (Data Minimization) | actor role verified via RBAC engine (RN12); Actor is authenticated with Admin or Owner privileges in the target workspace. | Member roster and seat quotas remain unaffected upon invitation or role assignment failures; all role modifications are permanently logged (RN18).

--- |
| `{U.C. 2.3}` | Monitor workspace activity and operational metrics | `RN9` (Multi-Tenant Isolation), `RN12` (RBAC) | tenant context verified (RN9); Actor holds Admin or Owner status in the workspace. | Zero cross-tenant metrics or data items are revealed; read failures produce no system state changes.

--- |
| `{U.C. 3.1}` | Create and configure projects | `RN9` (Multi-Tenant Isolation), `RN12` (RBAC), `RN18` (Audit Logging) | actor role authorized to create projects (RN12); Actor is an active member or admin of the workspace. | No unassigned or unisolated project containers are created; security audit trail records creation event (RN18).

--- |
| `{U.C. 3.2}` | Archive completed projects | `RN12` (RBAC), `RN18` (Audit Logging) | actor possesses Admin or Owner role (RN12); Actor possesses Admin or Owner role in the workspace; project is active. | Project state remains unmodified if archive authorization check fails.

--- |
| `{U.C. 4.1}` | Create and assign tasks | `RN9` (Multi-Tenant Isolation), `RN12` (RBAC) | actor belongs to authorized workspace project (RN9); Actor has member access to the parent active project. | No partial task records exist without an assigned project identifier and tenant context.

--- |
| `{U.C. 4.2}` | Track and transition task workflow states on visual boards | `RN9` (Multi-Tenant Isolation), `RN17` (Rate Limiting) | actor session is active; User has access rights to the project board. | Task status updates are atomic; concurrent transition collisions are resolved without data corruption.

--- |
| `{U.C. 4.3}` | Configure recurring automated tasks | `RN9` (Multi-Tenant Isolation), `RN18` (Audit Logging) | daemon executes within isolated service context (RN9); Task exists within an active project. | Automation failures log diagnostic traces and do not generate duplicate task instances.

--- |
| `{U.C. 5.1}` | Manage task deliverable attachments | `RN13` (Strict File Validation & Malware Isolation), `RN25` (Orphan File Expiration) | actor possesses Member role; storage quota not exceeded; User has access to the task card; member rights required for upload/delete; view rights sufficient for download. | Incomplete or corrupted file fragments are automatically purged from storage buffers; deleted attachments are marked for irreversible cleanup within 14 days (RN25).

--- |
| `{U.C. 5.2}` | Post in-task discussion comments and mention collaborators | `RN14` (Context-Aware Output Encoding & Anti-XSS), `RN26` (Privacy Audit Trail) | actor belongs to workspace team; Actor has member access to the project. | Unsubmitted draft comments are not stored; rendered comments are context-encoded to prevent stored XSS (RN14).

--- |
| `{U.C. 6.1}` | Consult chronological audit history on task cards | `RN18` (Audit Logging), `RN22` (Purpose Limitation) | actor possesses read permissions for target task (RN9); User has access rights to view the task card. | Audit records are read-only; history entries cannot be modified or deleted via user interfaces (RN18).

--- |
| `{U.C. 6.2}` | Receive workspace alerts and daily task digests | `RN9` (Multi-Tenant Isolation), `RN24` (Transport Encryption) | actor preferences permit notifications; User holds an active account in one or more workspaces. | Notification deliveries contain only authorized user task snippets and exclude sensitive credentials.

--- |
| `{U.C. 7.1}` | Subscribe and manage workspace commercial plans | `RN15` (Billing Invariant Protection), `RN16` (Cryptographic Webhook Verification), `RN18` (Audit Logging) | actor has Owner role; session authenticated (RN12); Actor is authenticated and holds the Workspace Owner role. | No commercial plan upgrades or quota adjustments occur without verified cryptographic payment receipt (RN15, RN18).

--- |
| `{U.C. 7.2}` | Enforce operational grace period upon payment failure | `RN15` (Billing Invariant Protection), `RN16` (Cryptographic Webhook Verification), `RN18` (Audit Logging) | external payment webhook verified via cryptographic signature (RN16); Workspace possesses an active paid commercial subscription reaching its renewal billing cycle. | Grace period state changes require verified payment gateway origin and emit immutable billing audit records (RN18).

--- |
| `{U.C. 8.1}` | Export personal and workspace data archives | `RN20` (Data Portability), `RN23` (Encryption at Rest), `RN9` (Tenant Isolation) | actor possesses valid session; organization export requires Owner role (RN12); Actor possesses valid authenticated session; workspace export restricted to Workspace Owner. | Personal data of third parties is strictly excluded from individual user data archives; exported archive package is encrypted at rest prior to download (RN20, RN23).

--- |
| `{U.C. 8.2}` | Close user accounts and terminate workspace access | `RN21` (Right to Erasure), `RN26` (Privacy Audit Trail), `RN11` (Session Invalidation), `RN18` (Audit Logging) | actor possesses active session; identity confirmed (RN11); Actor possesses an active authenticated user account. | Account deactivation immediately revokes authentication tokens, preventing subsequent API or UI access; personal data is pseudonymized within 30 days and audit logged (RN21, RN18).

--- |

## §5 Coverage Totals

| Surface | Count | Notes |
|---|---|---|
| V0 functional capabilities | 8 (R1–R8) | Pure functional, tech-neutral. |
| V0 atomic functional requirements | 18 (R1.1–R8.2) | MoSCoW priorities: 13 MUST / 3 SHOULD / 2 COULD / 0 WON'T. |
| V0 Product Use Cases | 18 (PUC 1.1–8.2) | Triggered by business events. |
| V0 Sea-Level Use Cases | 18 ({U.C. 1.1}–8.2) | Zero leaf nodes. |
| V1 base NFRs | 8 (RN1–RN8) | Performance, availability, usability, scalability, recoverability, i18n, interoperability, tenancy. |
| V1 security & privacy NFRs | 18 (RN9–RN26) | 10 CRA-derived (`RN9`–`RN18`) + 8 GDPR-derived (`RN19`–`RN26`). |
| V2 functional requirements | 18 | Identical to V0; consolidation is structural, not textual. |
| Phase 2 PO/SO rules upstream of all RN | 100 (per `Doc01_Operational_Objectives.md`) | 35 GDPR (PO-) + 35 CRA (SO-) + 30 duplicates across both ambits. |

