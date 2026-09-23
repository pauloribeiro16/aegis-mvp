# V0 → V1 → V2 Analysis Tables — TinyTask SaaS

> **Document Purpose:** Tabular view of the V0 functional baseline, the V2 consolidated top-level, and the V1 security & privacy synthesis. **V1 absorbs all security & privacy NFRs directly into the functional requirement cards** (R<n.m>); a separate Doc03 catalog no longer exists. Each functional R shows the regulation → Phase 2 rule → secure-design principle → control anchor chain that grounds its constraints.

> **Source of Truth:** `v0_functional_baseline/` (V0, LOCKED) · top-level `Doc01`/`Doc02` (V2, consolidated) · `v1_security_privacy_synthesis/Doc01` (V1, APPROVED, contains absorbed NFRs).

---

## §1 Version Ladder (what each V contains)

| Version | Path | Role | Requirements (R) | Non-Functional (RN) | Security & Privacy | Status |
|---|---|---|---|---|---|---|
| **V0** | `v0_functional_baseline/` | Pure functional snapshot — 8 capability packages, 18 atomic requirement cards, 18 PUCs, 18 Sea-Level UCs. | 18 (`R1.1`–`R8.2`) | 0 | 0 | LOCKED |
| **V1** | `v1_security_privacy_synthesis/Doc01_*` | V0 + security & privacy synthesis **absorbed into each R card** (Security & Privacy Constraints block: regulation → Phase 2 rule → PRIN-ENG → CSF/PF/AIRMF anchor). 8 standalone operational NFRs retained as `RN1`–`RN8`. 18 security/privacy NFRs renumbered `RN9`–`RN26` (single interval, no prefix families) and embedded into the relevant R cards. | 18 (unchanged) | 26 (`RN1`–`RN26`, all 26 live) | 18 absorbed + 8 standalone operational | APPROVED |
| **V2** | top-level `Doc01`/`Doc02` | Consolidated top-level — pure functional baseline at v2.1 with anti-pattern cleanup; security & privacy traceability carried through Doc02 traceability matrix (compact NFR list per R). | 18 (consolidated R-codes) | 26 | 18 absorbed | ACTIVE |

## §2 Master Matrix per Functional Requirement (R)

| Req ID | Requirement Name | Priority | V0 Essence (verbatim from snapshot) | V2 State (top-level) | V1 Synthesis: Security & Privacy Constraints (absorbed) | Verification Method(s) |
|---|---|---|---|---|---|---|
| `R1.1` | Register and authenticate user accounts | Must | The system must allow prospective users to create an account with email verification, authenticate using valid credentials to establish an active session, and autonomously request password reset assistance via email. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R1.2` | Manage user profile and account preferences | Should | The system must allow an authenticated user to view and update their personal profile details (full name, avatar image, and contact details) and configure notification preferences. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R2.1` | Create and configure workspace | Must | The system must allow an authenticated user to instantiate an isolated organizational workspace by specifying a workspace name and unique URL slug, automatically assigning the creator as Workspace Owner and permitting subsequent configuration of workspace branding and organization name. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R2.2` | Invite workspace members and manage access roles | Must | The system must allow Workspace Admins and Owners to invite team members via email, assign access roles (Owner, Admin, Member, Viewer) that govern operational permissions within the workspace, modify member roles, or revoke membership, respecting active seat limits. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R2.3` | Monitor workspace activity and operational metrics | Could | The system must compile and present aggregated operational metrics to workspace leadership, displaying active member counts, tasks completed during the billing cycle, and total deliverable file storage consumed. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R3.1` | Create and configure projects | Must | The system must allow Workspace Admins and Members to initialize distinct project containers within a workspace, specifying project name, description of deliverables, and visibility settings (workspace-wide or restricted to selected members). | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R3.2` | Archive completed projects | Should | The system must allow Workspace Admins and Owners to transition completed projects into archived status, rendering all tasks and discussions read-only and hiding the project from daily operational views while preserving historical data. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R4.1` | Create and assign tasks | Must | The system must allow authorized team members to create tasks within a project by specifying a mandatory title, optional description, priority level (Low, Medium, High, Urgent), and target due date, and assign execution responsibility to one or more active workspace members. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R4.2` | Track and transition task workflow states on visual boards | Must | The system must render tasks in interactive Kanban boards with standard status columns (To-Do, In-Progress, Under-Review, Done) and tabular views, allowing members to transition cards between states and filter tasks dynamically by assignee, status, priority, or overdue status. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R4.3` | Configure recurring automated tasks | Could | The system must allow users to configure recurrence schedules (weekly or monthly) on a task, automatically creating a duplicate task instance in the "To-Do" column once the current instance is marked "Done". | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R5.1` | Manage task deliverable attachments | Must | The system must allow authorized team members to upload deliverable files (supporting documents, spreadsheets, presentations, and images) up to 25 MB in size per file directly into a task card, view inline previews, download attached files, and remove outdated attachments. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R5.2` | Post in-task discussion comments and mention collaborators | Must | The system must provide a contextual comment thread inside each task card supporting rich text Markdown formatting and parsing collaborator mentions (@user) to automatically dispatch in-app notifications to tagged users. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R6.1` | Consult chronological audit history on task cards | Must | The system must record and display a chronological audit feed on each task card documenting state changes, assignee reallocations, due date adjustments, and attachment events, identifying author and timestamp. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R6.2` | Receive workspace alerts and daily task digests | Should | The system must provide an in-app notification center for direct assignments and @mentions, and automatically dispatch a daily summary email digest listing upcoming and overdue tasks assigned to the user. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R7.1` | Subscribe and manage workspace commercial plans | Must | The system must allow the Workspace Owner to select a commercial plan tier (Free, Pro, Enterprise) and complete checkout via the external payment gateway, automatically updating workspace plan status, renewal date, and authorized member seat quotas upon payment confirmation. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R7.2` | Enforce operational grace period upon payment failure | Must | The system must grant a 7-day operational grace period if an automated subscription renewal payment fails, maintaining normal workspace access while presenting payment update notices to the Workspace Owner before applying plan restrictions. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R8.1` | Export personal and workspace data archives | Must | The system must allow authenticated users to download a structured export of their personal profile and authored tasks, and allow Workspace Owners to export a comprehensive archive of workspace projects, tasks, comments, and attachments. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |
| `R8.2` | Close user accounts and terminate workspace access | Must | The system must allow users to autonomously terminate their accounts, invalidating active credentials and sessions, ending active workspace memberships, and dispatching a formal confirmation receipt via email. | Verbatim copy of V0 (no consolidation delta). | — | TEST/INSPECT/DEMONSTRATE/ANALYZE per absorbed NFR. |

## §3 NFR Catalogue (RN1–RN26, single interval)

| RN ID | Name | Type | Regulatory Anchor | Phase 2 Upstream Rule(s) | Secure-Design Principle | Control Anchors | Bound R IDs |
|---|---|---|---|---|---|---|---|
| `RN1` | Page load <500 ms on Kanban boards / task lists with up to 200 items | Operational | — (industry best practice) | — | — | — | — |
| `RN2` | Monthly availability ≥ 99.5% excluding announced maintenance | Operational | — (industry best practice) | — | — | — | — |
| `RN3` | Responsive UI down to 375 px viewport | Operational | — (industry best practice) | — | — | — | — |
| `RN4` | Storage scales to 50,000 active tasks per workspace without degradation | Operational | — (industry best practice) | — | — | — | — |
| `RN5` | Daily automated backups; RPO < 24 h | Operational | — (industry best practice) | — | — | — | — |
| `RN6` | UI localized in English and Portuguese | Operational | — (industry best practice) | — | — | — | — |
| `RN7` | Payment gateway integration: authenticated channels + cryptographic webhook signature verification | Operational | — (industry best practice) | — | — | — | — |
| `RN8` | Strict logical data segregation across workspaces (multi-tenancy) | Operational | — (industry best practice) | — | — | — | — |
| `RN10` | Credential Hardening & Salted Hashing | Security/Privacy | `CRA Annex I Part I (2)(d) + (2)(j)` | `SO-D-02.1-002, SO-D-01.1-002` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | CSF: PR.AA-03, PR.DS-01 | R1.1 |
| `RN11` | Cryptographic Session Management & Invalidation | Security/Privacy | `CRA Annex I Part I (2)(d) + (2)(j)` | `SO-D-02.2-002` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | CSF: PR.AA-03, PR.DS-02 | R1.1 |
| `RN12` | Role-Based Access Control & Action Mediation | Security/Privacy | `CRA Annex I Part I (2)(d)` | `SO-D-02.1-002` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | CSF: PR.AA-05, PR.AA-06 | R2.1, R2.2, R3.1 |
| `RN13` | File Upload Strict Validation & Content Isolation | Security/Privacy | `CRA Annex I Part I (2)(j)` | `SO-D-07.1-002` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | CSF: PR.PS-06, PR.PS-02 | R4.1, R4.2 |
| `RN14` | Context-Aware Output Encoding & Sanitization | Security/Privacy | `CRA Annex I Part I (2)(l)` | `SO-D-07.1-002` | `PRIN-ENG-04` Fail-Safe Defaults & Closed Failure States | CSF: PR.PS-06 | R5.1 |
| `RN15` | Cryptographic Billing Invariant Protection | Security/Privacy | `CRA Annex I Part I (2)(l)` | `SO-D-01.1-002, SO-D-08.1-002` | `PRIN-ENG-01` Trust Boundaries & Complete Mediation | CSF: PR.DS-01, PR.DS-02 | R7.1, R7.2 |
| `RN16` | Cryptographic Webhook Origin Verification | Security/Privacy | `CRA Annex I Part I (2)(l)` | `SO-D-05.1-002, SO-D-08.1-002` | `PRIN-ENG-01` Trust Boundaries & Complete Mediation | CSF: PR.DS-02, PR.AA-05 | R8.1 |
| `RN17` | Inbound API Token Mediation & Rate Limiting | Security/Privacy | `CRA Annex I Part I (2)(d) + (2)(j)` | `SO-D-02.1-002, SO-D-05.1-002` | `PRIN-ENG-02` Attack Surface Minimization & Peripheral Resilience | CSF: PR.AA-01, PR.IR-01 | R8.2 |
| `RN18` | Non-Repudiable Security Audit Logging | Security/Privacy | `CRA Annex I Part I (2)(l)` | `SO-D-03.1-002` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | CSF: PR.PS-04, DE.AE-02 | R1.1, R8.2 |
| `RN19` | Registration Data Minimization by Default | Security/Privacy | `GDPR Art. 5(1)(c)` | `PO-D-06.1-001` | `PRIN-ENG-06` Proactive Data Minimization & Scoped Projection | CSF: PR.DS-10, GV.OC-03 · PF: CT.DP-P2 | R1.1 |
| `RN20` | Structured Personal Data Portability & Export | Security/Privacy | `GDPR Art. 20 + Art. 15(3) + Art. 12(3)` | `PO-D-06.2-001` | `PRIN-ENG-06` Proactive Data Minimization & Scoped Projection | CSF: PR.DS-10 · PF: CT.DM-P1 | R1.2 |
| `RN21` | Irreversible Data Subject Erasure & Pseudonymization | Security/Privacy | `GDPR Art. 17 + Art. 28(3)(g)` | `PO-D-06.2-001` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | CSF: PR.DS-10 · PF: CT.DM-P1 | R1.1, R1.2 |
| `RN22` | Purpose Limitation & Time Log Segregation | Security/Privacy | `GDPR Art. 5(1)(b) + Art. 6(4)` | `PO-D-06.1-001` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | CSF: GV.OC-03, PR.DS-10 · PF: CM.PO-P2 | R6.1, R6.2 |
| `RN23` | Personal Data Cryptographic Protection at Rest | Security/Privacy | `GDPR Art. 32(1)(a) + Art. 5(1)(f)` | `PO-D-01.1-001` | `PRIN-ENG-01` Trust Boundaries & Complete Mediation | CSF: PR.DS-01, PR.DS-10 · PF: PR.DS-P1 | R1.1, R1.2, R6.1 |
| `RN24` | Mandatory End-to-End Transport Layer Cryptographic Protection | Security/Privacy | `GDPR Art. 32(1)(a) + Art. 32(2)` | `PO-D-01.2-001` | `PRIN-ENG-01` Trust Boundaries & Complete Mediation | CSF: PR.DS-02, PR.IR-01 · PF: PR.DS-P2 | R1.1, R8.2 |
| `RN25` | Automated Orphan File Asset Cleanup & Expiration | Security/Privacy | `GDPR Art. 5(1)(e)` | `PO-D-06.1-001` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | CSF: PR.IP-06, PR.DS-10 · PF: CT.DM-P3 | R4.2 |
| `RN26` | Privacy Audit Trail for Personal Data Modifications | Security/Privacy | `GDPR Art. 30` | `PO-D-03.1-001` | `PRIN-ENG-07` End-to-End Lifecycle Security & Irreversible Erasure | CSF: PR.PT-01, DE.CM-01 · PF: CM.AW-P2 | R1.1, R1.2, R6.1 |
| `RN9` | Multi-Tenant Data Isolation & Mediation | Security/Privacy | `CRA Annex I Part I (2)(d)` | `SO-D-02.1-002` | `PRIN-ENG-03` Least Privilege & Mechanism Isolation | CSF: PR.AA-05, PR.DS-01 | R1.2, R2.1, R3.1 |

## §4 Use Case Augmentation ({U.C. 1.1} to {U.C. 8.2})

Security & Privacy Traces in Doc02 are now NFR-RN<n> references pointing to the absorbed cards in Doc01 §3.

| UC ID | UC Name | NFR-RN absorbed (from bound R card) |
|---|---|---|
| `{{U.C. 1.1}}` | Register and authenticate user accounts | NFR-RN10, NFR-RN11, NFR-RN18, NFR-RN19, NFR-RN24 |
| `{{U.C. 1.2}}` | Manage user profile and account preferences | NFR-RN9, NFR-RN20, NFR-RN23, NFR-RN26 |
| `{{U.C. 2.1}}` | Create and configure workspace | NFR-RN9, NFR-RN12, NFR-RN18 |
| `{{U.C. 2.2}}` | Invite workspace members and manage access roles | NFR-RN12, NFR-RN18, NFR-RN19 |
| `{{U.C. 2.3}}` | Monitor workspace activity and operational metrics | NFR-RN9, NFR-RN12 |
| `{{U.C. 3.1}}` | Create and configure projects | NFR-RN9, NFR-RN12, NFR-RN18 |
| `{{U.C. 3.2}}` | Archive completed projects | NFR-RN12, NFR-RN18 |
| `{{U.C. 4.1}}` | Create and assign tasks | NFR-RN9, NFR-RN12 |
| `{{U.C. 4.2}}` | Track and transition task workflow states on visual boards | NFR-RN9, NFR-RN17 |
| `{{U.C. 4.3}}` | Configure recurring automated tasks | NFR-RN9, NFR-RN18 |
| `{{U.C. 5.1}}` | Manage task deliverable attachments | NFR-RN13, NFR-RN25 |
| `{{U.C. 5.2}}` | Post in-task discussion comments and mention collaborators | NFR-RN14, NFR-RN26 |
| `{{U.C. 6.1}}` | Consult chronological audit history on task cards | NFR-RN18, NFR-RN22 |
| `{{U.C. 6.2}}` | Receive workspace alerts and daily task digests | NFR-RN9, NFR-RN24 |
| `{{U.C. 7.1}}` | Subscribe and manage workspace commercial plans | NFR-RN15, NFR-RN16, NFR-RN18 |
| `{{U.C. 7.2}}` | Enforce operational grace period upon payment failure | NFR-RN15, NFR-RN16, NFR-RN18 |
| `{{U.C. 8.1}}` | Export personal and workspace data archives | NFR-RN20, NFR-RN23, NFR-RN9 |
| `{{U.C. 8.2}}` | Close user accounts and terminate workspace access | NFR-RN21, NFR-RN26, NFR-RN11, NFR-RN18 |

## §5 Coverage Totals

| Surface | Count | Notes |
|---|---|---|
| V0 functional capabilities | 8 (R1–R8) | Pure functional, tech-neutral. |
| V0 atomic functional requirements | 18 (R1.1–R8.2) | MoSCoW priorities: 13 MUST / 3 SHOULD / 2 COULD / 0 WON'T. |
| V0 Product Use Cases | 18 (PUC 1.1–8.2) | Triggered by business events. |
| V0 Sea-Level Use Cases | 18 ({U.C. 1.1}–8.2) | Zero leaf nodes. |
| V1 NFRs (single interval RN1–RN26) | 26 | 8 operational (RN1–RN8, standalone) + 18 security/privacy (RN9–RN26, absorbed into R cards). |
| V1 NFR-Security absorbed per R card | variable (1–8 NFR per card) | Each R shows the regulation → Phase 2 rule → PRIN-ENG → CSF/PF/AIRMF chain inside its Security & Privacy Constraints block. |
| V2 functional requirements | 18 | Identical to V0; consolidation is structural, not textual. |
| Phase 2 rules upstream of NFRs | 100 (per Phase 2 Doc01) | 35 GDPR (PO-) + 35 CRA (SO-) + 30 duplicates across ambits. |

