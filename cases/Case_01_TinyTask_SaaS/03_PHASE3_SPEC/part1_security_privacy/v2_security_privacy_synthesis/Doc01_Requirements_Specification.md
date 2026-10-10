# E1.1b – TinyTask SaaS: Requirements Specification (Functional Cards & Security/Privacy Constraints)

## Executive Summary

This deliverable establishes the formal, verifiable requirements specification for the **TinyTask SaaS** platform, providing the authoritative contractual baseline for software engineering, quality assurance, and automated verification.

In accordance with software engineering literature (Robertson & Robertson, Cockburn, Wiegers & Beatty, and IEEE 29148), this specification models the static, verifiable properties of the system. Operational processes, As-Is/To-Be workflows, and Product Use Cases (*PUC*) are decoupled into upstream deliverable [`Doc00_Process_and_Operational_Workflows.md`](Doc00_Process_and_Operational_Workflows.md). Every functional requirement card in this catalog explicitly traces back to the operational PUC it realizes.

Security, privacy, and regulatory constraints derived from the AEGIS methodology (GDPR and CRA) are systematically integrated into each requirement card using the Easy Approach to Requirements Syntax (EARS) pattern, complete with full traceability to Phase 2 operational objectives and published control anchors (NIST CSF 2.0 and NIST Privacy Framework 1.1).

---

## Table of Contents

- [1. Operational Actors Reference](#1-operational-actors-reference)
- [2. Functional Requirements Baseline](#2-functional-requirements-baseline)
  - [2.1 MoSCoW Prioritization Method](#21-moscow-prioritization-method)
  - [2.2 Summary Table of Functional Requirements](#22-summary-table-of-functional-requirements)
  - [2.3 Detailed Specification Cards for Functional Requirements](#23-detailed-specification-cards-for-functional-requirements)
    - [R1 – Manage User Accounts and Authentication](#r1--manage-user-accounts-and-authentication)
    - [R2 – Manage Workspaces and Teams](#r2--manage-workspaces-and-teams)
    - [R3 – Manage Projects](#r3--manage-projects)
    - [R4 – Manage and Execute Tasks](#r4--manage-and-execute-tasks)
    - [R5 – Collaborate on Task Deliverables](#r5--collaborate-on-task-deliverables)
    - [R6 – Track Activity History and Notifications](#r6--track-activity-history-and-notifications)
    - [R7 – Manage Commercial Subscriptions](#r7--manage-commercial-subscriptions)
    - [R8 – Export Data and Close Accounts](#r8--export-data-and-close-accounts)
- [3. Non-Functional Requirements & Transversal Attributes](#3-non-functional-requirements--transversal-attributes)
  - [3.1 General Operational Quality Attributes](#31-general-operational-quality-attributes)
  - [3.2 Transversal Security and Privacy Requirements](#32-transversal-security-and-privacy-requirements)
- [Bibliography](#bibliography)
- [Version History](#version-history)

---

## 1. Operational Actors Reference

The functional requirements govern interactions initiated by the following operational actors (detailed in [`Doc00_Process_and_Operational_Workflows.md`](Doc00_Process_and_Operational_Workflows.md)):

*Table 1. Reference Actors*

| Actor | Category | Description |
|---|---|---|
| **Workspace Owner** | Internal User | Commercial and administrative authority. Manages billing, quotas, export, and workspace deletion. |
| **Workspace Admin** | Internal User | Operational workspace manager. Invites members, assigns roles, and configures organization settings. |
| **Workspace Member** | Internal User | Standard contributor. Creates and transitions tasks, uploads attachments, and collaborates in threads. |
| **Workspace Viewer** | External User | External client granted read-only visibility into authorized projects and boards. |
| **External Payment Gateway** | External System | Hosted payment processor executing billing transactions and dispatching webhook status events. |
| **Notification / Email Service** | External Subsystem | Messaging service dispatching verification emails, assignment notices, and daily digest emails. |

---

## 2. Functional Requirements Baseline

### 2.1 MoSCoW Prioritization Method

Functional requirements are prioritized using the MoSCoW methodology:
- **MUST:** Mandatory requirement that must be satisfied in the baseline release for the system to be viable.
- **SHOULD:** High-impact requirement that should be satisfied unless critical delivery constraints dictate deferral.
- **COULD:** Desirable functionality or enhancement that can be included if schedule and resources permit.
- **WON'T:** Out-of-scope feature that will not be implemented in the initial baseline release, reserved for future iterations.

### 2.2 Summary Table of Functional Requirements

*Table 2. List of functional requirements (Summary)*

| ID | ID | Requirement | Priority | Restrictions | Realizes PUC |
|---|---|---|---|---|---|
| **R1** | | **Manage User Accounts and Authentication** | **MUST** | | |
| | R1.1 | Register and authenticate user accounts | MUST | Unique email | PUC 1.1 |
| | R1.2 | Manage user profile and account preferences | MUST | | PUC 1.2 |
| | R1.3 | Recover access to a locked user account | MUST | | PUC 1.3 |
| **R2** | | **Manage Workspaces and Teams** | **MUST** | | |
| | R2.1 | Create and configure workspace | MUST | Unique URL slug | PUC 2.1 |
| | R2.2 | Invite workspace members and manage access roles | MUST | Seat quota | PUC 2.2 |
| | R2.3 | Monitor workspace activity and operational metrics | COULD | | PUC 2.3 |
| **R3** | | **Manage Projects** | **MUST** | | |
| | R3.1 | Create and configure projects | MUST | | PUC 3.1 |
| | R3.2 | Archive completed projects | SHOULD | | PUC 3.2 |
| **R4** | | **Manage and Execute Tasks** | **MUST** | | |
| | R4.1 | Create and assign tasks | MUST | | PUC 4.1 |
| | R4.2 | Track and transition task workflow states on visual boards | MUST | | PUC 4.2 |
| | R4.3 | Configure recurring automated tasks | COULD | | PUC 4.3 |
| **R5** | | **Collaborate on Task Deliverables** | **MUST** | | |
| | R5.1 | Manage task deliverable attachments | MUST | 25 MB cap | PUC 5.1 |
| | R5.2 | Post in-task discussion comments and mention collaborators | MUST | | PUC 5.2 |
| **R6** | | **Track Activity History and Notifications** | **MUST** | | |
| | R6.1 | Consult chronological audit history on task cards | MUST | | PUC 6.1 |
| | R6.2 | Receive workspace alerts and daily task digests | SHOULD | | PUC 6.2 |
| **R7** | | **Manage Commercial Subscriptions** | **MUST** | | |
| | R7.1 | Subscribe and manage workspace commercial plans | MUST | | PUC 7.1 |
| | R7.2 | Enforce operational grace period upon payment failure | MUST | 7-day limit | PUC 7.2 |
| **R8** | | **Export Data and Close Accounts** | **MUST** | | |
| | R8.1 | Export personal and workspace data archives | MUST | | PUC 8.1 |
| | R8.2 | Close user accounts and terminate workspace access | MUST | | PUC 8.2 |
| | R8.3 | Delete workspace and permanently erase workspace data | MUST | | PUC 8.3 |

---

### 2.3 Detailed Specification Cards for Functional Requirements

The detailed functional requirement cards follow the exact 7-row single-column format established in the reference project standard:

#### R1 – Manage User Accounts and Authentication

##### R1.1 – Register and authenticate user accounts

| Requirement |
|---|
| **ID:** R1.1 **Name:** Register and authenticate user accounts |
| **Description:** The system must allow prospective users to create an account with email verification, authenticate using valid credentials to establish an active session, and autonomously request password reset assistance via email. |
| **Requirement Origin:** Founders Business Case & User Onboarding Workflow (Realizes: PUC 1.1) |
| **Security & Privacy Constraints:**<br>**Chain** GDPR → `SO-D-03.4-001` · CRA → `SO-D-05.1-002`<br>**Chain** **NFR-RN10** Credential Confidentiality Protection (State of the Art) — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-01.1-002, SO-D-03.1-002` → `PRIN-ENG-04` → CSF PR.DS-01, PR.AA-01, PR.AA-05<br>**NFR-RN11** Session Management & Invalidation — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-03.1-002` → `PRIN-ENG-04` → CSF PR.AA-01, PR.AA-05, PR.AA-06<br>**NFR-RN19** Registration Data Minimization by Default — `GDPR Art. 5(1)(c)` → `PO-D-05.1-001` → `PRIN-ENG-06` → CSF PR.DS-10, GV.OC-03 / PF CT.DP-P2 |
| **Interfaces:** Registration screen; Login screen; Password recovery flow; Transactional email interface |
| **Dependencies:**<br>• **Stakeholders:** Platform Founders, All End Users<br>• **Data Sources:** Registration form submissions; Credential verification requests; Password reset requests<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Identity and Credential Store; Notification / Email Service<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R1.2 – Manage user profile and account preferences

| Requirement |
|---|
| **ID:** R1.2 **Name:** Manage user profile and account preferences |
| **Description:** The system must allow an authenticated user to view and update their personal profile details (full name, avatar image, and contact details) and configure notification preferences. |
| **Requirement Origin:** User Account Personalization Needs (Realizes: PUC 1.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN23** Personal Data Cryptographic Protection at Rest — `GDPR Art. 32(1)(a) + Art. 5(1)(f)` → `PO-D-01.1-001` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10 / PF PR.DS-P1<br>**NFR-RN26** Privacy Audit Trail for Personal Data Modifications — `GDPR Art. 30` → `PO-D-09.4-001` → `PRIN-ENG-07` → CSF ID.AM-08, PR.DS-10 / PF CM.AW-P2 <br>**D3 elevation driver** (no RN bound) — `GDPR Art. 5(1)(d) + Art. 16` → `PO-D-01.4-001`: the rectification duty is discharged by this card's own editing surface rather than by a transversal constraint, and the priority is raised to Must because a data-subject right admits no deferral |
| **Interfaces:** Profile settings screen; Notification preferences panel |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors<br>• **Data Sources:** Profile update submissions; Preference selections<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (user profile records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

##### R1.3 – Recover access to a locked user account

| Requirement |
|---|
| **ID:** R1.3 **Name:** Recover access to a locked user account |
| **Description:** The system must allow a user whose account is temporarily locked after repeated failed authentication attempts to autonomously regain access: the user requests recovery via the registered email address, receives a single-use time-limited recovery link, and upon following it the system lifts the lockout, invalidates all active sessions, and restores normal authentication. |
| **Requirement Origin:** User Account Availability & Self-Service Recovery Needs (Realizes: PUC 1.3 — derived from NFR-RN10/NFR-RN11 lockout behavior) |
| **Security & Privacy Constraints:**<br>**NFR-RN10** Credential Confidentiality Protection (State of the Art) — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-01.1-002, SO-D-03.1-002` → `PRIN-ENG-04` → CSF PR.DS-01, PR.AA-01, PR.AA-05<br>**NFR-RN11** Session Management & Invalidation — `CRA Annex I Part I (2)(d) + (2)(j)` → `SO-D-03.1-002` → `PRIN-ENG-04` → CSF PR.AA-01, PR.AA-05, PR.AA-06 |
| **Interfaces:** Account recovery request form; Recovery email link; Login screen |
| **Dependencies:**<br>• **Stakeholders:** All End Users, Platform Founders<br>• **Data Sources:** Account recovery requests; Lockout state records<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Identity and Credential Store; Notification / Email Service<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R2 – Manage Workspaces and Teams

##### R2.1 – Create and configure workspace

| Requirement |
|---|
| **ID:** R2.1 **Name:** Create and configure workspace |
| **Description:** The system must allow an authenticated user to instantiate an isolated organizational workspace by specifying a workspace name and unique URL slug, automatically assigning the creator as Workspace Owner and permitting subsequent configuration of workspace branding and organization name. |
| **Requirement Origin:** Multi-Tenant Organization Needs & Customer Expectation EXP-01 (Realizes: PUC 2.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN9** Multi-Tenant Data Isolation & Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-03.2-002` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06<br>**NFR-RN28** Secure-by-Default Configuration with User Reset — `CRA Annex I Part I (2)(b) + (2)(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01 |
| **Interfaces:** Workspace setup wizard; Organization branding settings |
| **Dependencies:**<br>• **Stakeholders:** Platform Founders, Business Customers<br>• **Data Sources:** Workspace creation form; Branding configuration<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (workspace registry); File Storage Service (branding assets)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R2.2 – Invite workspace members and manage access roles

| Requirement |
|---|
| **ID:** R2.2 **Name:** Invite workspace members and manage access roles |
| **Description:** The system must allow Workspace Admins and Owners to invite team members via email, assign access roles (Owner, Admin, Member, Viewer) that govern operational permissions within the workspace, modify member roles, or revoke membership, respecting active seat limits. |
| **Requirement Origin:** Team Collaboration Needs & Governance (Realizes: PUC 2.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN12** Role-Based Access Control & Action Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-03.3-002` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06 |
| **Interfaces:** Member invitation dialog; Role management console; Invitation email interface |
| **Dependencies:**<br>• **Stakeholders:** Team Leads, Project Managers<br>• **Data Sources:** Invitation submissions; Role assignments<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (membership roster)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R2.3 – Monitor workspace activity and operational metrics

| Requirement |
|---|
| **ID:** R2.3 **Name:** Monitor workspace activity and operational metrics |
| **Description:** The system must compile and present aggregated operational metrics to workspace leadership, displaying active member counts, tasks completed during the billing cycle, and total deliverable file storage consumed. |
| **Requirement Origin:** Team Coordination Needs & Management Reporting (Realizes: PUC 2.3) |
| **Security & Privacy Constraints:**<br>**NFR-RN22** Purpose Limitation & Activity Metrics Segregation — `GDPR Art. 5(1)(b) + Art. 6(4)` → `PO-D-05.1-001` → `PRIN-ENG-03` → CSF GV.OC-03, PR.DS-10 / PF CM.PO-P2 |
| **Interfaces:** Operational metrics dashboard |
| **Dependencies:**<br>• **Stakeholders:** Team Leads, Executive Leadership<br>• **Data Sources:** Workspace activity records<br>• **Extraction Periodicity:** on demand (continuous aggregation)<br>• **Information Systems / Databases:** Internal Application Database (activity aggregation)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Could |

---

#### R3 – Manage Projects

##### R3.1 – Create and configure projects

| Requirement |
|---|
| **ID:** R3.1 **Name:** Create and configure projects |
| **Description:** The system must allow Workspace Admins and Members to initialize distinct project containers within a workspace, specifying project name, description of deliverables, and visibility settings (workspace-wide or restricted to selected members). |
| **Requirement Origin:** Project Work Structuring Needs & Operational Workflow (Realizes: PUC 3.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN9** Multi-Tenant Data Isolation & Mediation — `CRA Annex I Part I (2)(d)` → `SO-D-03.2-002` → `PRIN-ENG-03` → CSF PR.AA-05, PR.AA-06<br>**NFR-RN28** Secure-by-Default Configuration with User Reset — `CRA Annex I Part I (2)(b) + (2)(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01 |
| **Interfaces:** Project creation form; Project settings screen |
| **Dependencies:**<br>• **Stakeholders:** Project Managers, Team Contributors<br>• **Data Sources:** Project creation submissions<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (project records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R3.2 – Archive completed projects

| Requirement |
|---|
| **ID:** R3.2 **Name:** Archive completed projects |
| **Description:** The system must allow Workspace Admins and Owners to transition completed projects into archived status, rendering all tasks and discussions read-only and hiding the project from daily operational views while preserving historical data. |
| **Requirement Origin:** Project Lifecycle Management Needs (Realizes: PUC 3.2) |
| **Interfaces:** Project lifecycle controls (archive action) |
| **Dependencies:**<br>• **Stakeholders:** Project Managers<br>• **Data Sources:** Project lifecycle actions<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (project records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Should |

---

#### R4 – Manage and Execute Tasks

##### R4.1 – Create and assign tasks

| Requirement |
|---|
| **ID:** R4.1 **Name:** Create and assign tasks |
| **Description:** The system must allow authorized team members to create tasks within a project by specifying a mandatory title, optional description, priority level (Low, Medium, High, Urgent), and target due date, and assign execution responsibility to one or more active workspace members. |
| **Requirement Origin:** Work Item Authoring Needs & Operational Allocation (Realizes: PUC 4.1) |
| **Interfaces:** Task editor; Assignee picker |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors, Project Managers<br>• **Data Sources:** Task creation form; Member picker selections<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (task records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R4.2 – Track and transition task workflow states on visual boards

| Requirement |
|---|
| **ID:** R4.2 **Name:** Track and transition task workflow states on visual boards |
| **Description:** The system must render tasks in interactive Kanban boards with standard status columns (To-Do, In-Progress, Under-Review, Done) and tabular views, allowing members to transition cards between states and filter tasks dynamically by assignee, status, priority, or overdue status. |
| **Requirement Origin:** Agile Workflow Tracking Needs & Customer Expectation EXP-02 (Realizes: PUC 4.2) |
| **Interfaces:** Kanban board view; Task list view; Filter controls |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors, Project Leads<br>• **Data Sources:** Task state transitions; Filter criteria<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (task state records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R4.3 – Configure recurring automated tasks

| Requirement |
|---|
| **ID:** R4.3 **Name:** Configure recurring automated tasks |
| **Description:** The system must allow users to configure recurrence schedules (weekly or monthly) on a task, automatically creating a duplicate task instance in the "To-Do" column once the current instance is marked "Done". |
| **Requirement Origin:** Repetitive Task Automation Needs (Realizes: PUC 4.3) |
| **Interfaces:** Recurrence configuration panel |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors<br>• **Data Sources:** Recurrence schedule settings<br>• **Extraction Periodicity:** per recurrence schedule<br>• **Information Systems / Databases:** Internal Application Database (recurrence rules, task instances)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Could |

---

#### R5 – Collaborate on Task Deliverables

##### R5.1 – Manage task deliverable attachments

| Requirement |
|---|
| **ID:** R5.1 **Name:** Manage task deliverable attachments |
| **Description:** The system must allow authorized team members to upload deliverable files (supporting documents, spreadsheets, presentations, and images) up to 25 MB in size per file directly into a task card, view inline previews, download attached files, and remove outdated attachments. |
| **Requirement Origin:** Document Centralization Needs & Customer Expectation EXP-04 (Realizes: PUC 5.1) |
| **Security & Privacy Constraints:**<br>**Chain** CRA → `SO-D-05.1-002`<br>**Chain** **NFR-RN13** File Upload Strict Validation & Content Isolation — `CRA Annex I Part I (2)(j)` → `SO-D-07.2-002` → `PRIN-ENG-02` → CSF PR.PS-06<br>**NFR-RN25** Automated Orphan File Asset Cleanup & Expiration — `GDPR Art. 5(1)(e)` → `PO-D-05.2-001` → `PRIN-ENG-07` → CSF PR.DS-10, ID.AM-03 / PF CT.DM-P3 |
| **Interfaces:** File upload control; Inline preview pane; Download interface |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors, Clients<br>• **Data Sources:** Uploaded deliverable files<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** File Storage Service; Internal Application Database (attachment metadata)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R5.2 – Post in-task discussion comments and mention collaborators

| Requirement |
|---|
| **ID:** R5.2 **Name:** Post in-task discussion comments and mention collaborators |
| **Description:** The system must provide a contextual comment thread inside each task card supporting rich text Markdown formatting and parsing collaborator mentions (@user) to automatically dispatch in-app notifications to tagged users. |
| **Requirement Origin:** In-Context Collaboration Needs & Customer Expectation EXP-03 (Realizes: PUC 5.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN14** Untrusted Content Neutralization — `CRA Annex I Part I (2)(l)` → `SO-D-07.2-002` → `PRIN-ENG-04` → CSF PR.PS-06 |
| **Interfaces:** Comment thread editor; Mention interface |
| **Dependencies:**<br>• **Stakeholders:** Team Contributors, Clients<br>• **Data Sources:** Comment submissions; Mention references<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (comment records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R6 – Track Activity History and Notifications

##### R6.1 – Consult chronological audit history on task cards

| Requirement |
|---|
| **ID:** R6.1 **Name:** Consult chronological audit history on task cards |
| **Description:** The system must record and display a chronological audit feed on each task card documenting state changes, assignee reallocations, due date adjustments, and attachment events, identifying author and timestamp. |
| **Requirement Origin:** Operational Transparency Needs & Team Accountability (Realizes: PUC 6.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN22** Purpose Limitation & Activity Metrics Segregation — `GDPR Art. 5(1)(b) + Art. 6(4)` → `PO-D-05.1-001` → `PRIN-ENG-03` → CSF GV.OC-03, PR.DS-10 / PF CM.PO-P2 |
| **Interfaces:** Task card audit timeline |
| **Dependencies:**<br>• **Stakeholders:** Project Managers, Contributors<br>• **Data Sources:** Task change events<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (audit event records)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R6.2 – Receive workspace alerts and daily task digests

| Requirement |
|---|
| **ID:** R6.2 **Name:** Receive workspace alerts and daily task digests |
| **Description:** The system must provide an in-app notification center for direct assignments and @mentions, and automatically dispatch a daily summary email digest listing upcoming and overdue tasks assigned to the user. |
| **Requirement Origin:** User Attention Management & Operational Digests (Realizes: PUC 6.2) |
| **Interfaces:** In-app notification center; Daily digest email interface |
| **Dependencies:**<br>• **Stakeholders:** Contributors, Team Leads<br>• **Data Sources:** Assignment events; Mention events; Due-date schedule<br>• **Extraction Periodicity:** on event / daily digest<br>• **Information Systems / Databases:** Internal Application Database (notification records); Notification / Email Service<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Should |

---

#### R7 – Manage Commercial Subscriptions

##### R7.1 – Subscribe and manage workspace commercial plans

| Requirement |
|---|
| **ID:** R7.1 **Name:** Subscribe and manage workspace commercial plans |
| **Description:** The system must allow the Workspace Owner to select a commercial plan tier (Free, Pro, Enterprise) and complete checkout via the external payment gateway, automatically updating workspace plan status, renewal date, and authorized member seat quotas upon payment confirmation. |
| **Requirement Origin:** Customer Subscription Needs & Commercial Policy (Realizes: PUC 7.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN15** Cryptographic Billing Invariant Protection — `CRA Annex I Part I (2)(l)` → `SO-D-01.4-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10 |
| **Interfaces:** Plan selection screen; Hosted checkout interface |
| **Dependencies:**<br>• **Stakeholders:** Executive Leadership, Business Customers<br>• **Data Sources:** Pricing catalog; Payment confirmation events<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (subscription records); External Payment Gateway<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R7.2 – Enforce operational grace period upon payment failure

| Requirement |
|---|
| **ID:** R7.2 **Name:** Enforce operational grace period upon payment failure |
| **Description:** The system must grant a 7-day operational grace period if an automated subscription renewal payment fails, maintaining normal workspace access while presenting payment update notices to the Workspace Owner. Upon grace period expiry without resolution, the system must transition the workspace to a restricted read-only state that preserves project consultation and data export while suspending content modifications and member invitations until billing is rectified. |
| **Requirement Origin:** Customer Retention & Business Continuity (Realizes: PUC 7.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN15** Cryptographic Billing Invariant Protection — `CRA Annex I Part I (2)(l)` → `SO-D-01.4-002` → `PRIN-ENG-01` → CSF PR.DS-01, PR.DS-10 |
| **Security & Privacy Constraints:**<br>**NFR-RN16** Cryptographic Webhook Origin Verification — `CRA Annex I Part I (2)(l)` → `SO-D-01.4-002` → `PRIN-ENG-01` → CSF PR.DS-10 |
| **Interfaces:** Billing status banner; Payment update prompt |
| **Dependencies:**<br>• **Stakeholders:** Customers, Finance Operations<br>• **Data Sources:** Payment failure events<br>• **Extraction Periodicity:** on event<br>• **Information Systems / Databases:** Internal Application Database (subscription records); External Payment Gateway (payment status)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

#### R8 – Export Data and Close Accounts

##### R8.1 – Export personal and workspace data archives

| Requirement |
|---|
| **ID:** R8.1 **Name:** Export personal and workspace data archives |
| **Description:** The system must allow authenticated users to download a structured export of their personal profile and authored tasks, and allow Workspace Owners to export a comprehensive archive of workspace projects, tasks, comments, and attachments. |
| **Requirement Origin:** Data Portability Needs & Customer Expectation EXP-06 (Realizes: PUC 8.1) |
| **Security & Privacy Constraints:**<br>**NFR-RN20** Structured Personal Data Portability & Export — `GDPR Art. 20 + Art. 15(3) + Art. 12(3)` → `PO-D-05.4-001` → `PRIN-ENG-06` → CSF PR.DS-10 / PF CT.DM-P1<br>**NFR-RN27** Requester Identity Verification for Rights Exercise — `GDPR Art. 12(6) + Art. 11(2)` → `SO-D-03.1-001` → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6 |
| **Interfaces:** Export request screen; Archive download interface |
| **Dependencies:**<br>• **Stakeholders:** End Users, Business Customers<br>• **Data Sources:** User profile records; Workspace content records<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (profile, task, comment records); File Storage Service (attachments)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R8.2 – Close user accounts and terminate workspace access

| Requirement |
|---|
| **ID:** R8.2 **Name:** Close user accounts and terminate workspace access |
| **Description:** The system must allow users to autonomously terminate their accounts, presenting a final personal data export option (R8.1) prior to irreversible erasure, invalidating active credentials and sessions, ending active workspace memberships, and dispatching a formal confirmation receipt via email. |
| **Requirement Origin:** Self-Service Account Termination & Customer Expectation EXP-06 (Realizes: PUC 8.2) |
| **Security & Privacy Constraints:**<br>**NFR-RN21** Irreversible Data Subject Erasure & Pseudonymization — `GDPR Art. 17 + Art. 28(3)(g)` → `PO-D-05.3-001` → `PRIN-ENG-07` → CSF PR.DS-10 / PF CT.DM-P1<br>**NFR-RN27** Requester Identity Verification for Rights Exercise — `GDPR Art. 12(6) + Art. 11(2)` → `SO-D-03.1-001` → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6 |
| **Interfaces:** Account closure flow; Confirmation email interface |
| **Dependencies:**<br>• **Stakeholders:** End Users, Workspace Admins<br>• **Data Sources:** Account closure requests<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (user account records, memberships); Notification / Email Service<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

##### R8.3 – Delete workspace and permanently erase workspace data

| Requirement |
|---|
| **ID:** R8.3 **Name:** Delete workspace and permanently erase workspace data |
| **Description:** The system must allow the Workspace Owner to delete an entire workspace together with all of its contents — projects, tasks, comments, attachments, and workspace settings — permanently and irreversibly, without deleting the owner's own account; the deletion is confirmed explicitly and certified with a receipt. |
| **Requirement Origin:** Workspace Lifecycle Management Needs & Data Sovereignty (Realizes: PUC 8.3 — derived from SO-D-05.3-002) |
| **Security & Privacy Constraints:**<br>**NFR-RN30** Workspace Permanent Removal — `CRA Annex I Part I (2)(m)` → `SO-D-05.3-002` → `PRIN-ENG-07` → CSF PR.DS-10, PR.DS-02<br>**NFR-RN21** Irreversible Data Subject Erasure & Pseudonymization (owner's personal data; co-driver) — `GDPR Art. 17 + Art. 28(3)(g)` → `PO-D-05.3-001` → `PRIN-ENG-07` → CSF PR.DS-10 / PF CT.DM-P1<br>**NFR-RN18** Security Audit Logging — `CRA Annex I Part I (2)(l)` → `SO-D-10.1-002, SO-D-04.1-002` → `PRIN-ENG-07` → CSF DE.CM-01, DE.CM-09 |
| **Interfaces:** Workspace deletion flow; Confirmation dialog; Deletion receipt email interface |
| **Dependencies:**<br>• **Stakeholders:** Business Customers, Workspace Owners<br>• **Data Sources:** Workspace deletion requests<br>• **Extraction Periodicity:** on demand<br>• **Information Systems / Databases:** Internal Application Database (workspace registry); File Storage Service (attachments)<br>• **Preceding Requirements:** |
| **Identified Problems:** |
| **Priority:** Must |

---

## 3. Non-Functional Requirements & Transversal Attributes

### 3.1 General Operational Quality Attributes

The platform non-functional requirements comprise the general operational quality attributes and the cross-cutting security & privacy requirements listed in Table 3; function-specific security & privacy NFRs are absorbed directly into the corresponding requirement cards as `Security & Privacy Constraints` rows (§2.3):

*Table 3. General Operational Quality Attributes*

| ID | Requirement | Fit criterion | Priority | Type |
|---|---|---|---|---|
| **RN1** | The platform must achieve a page load response time of under 500 ms for Kanban boards and task list views containing up to 200 items. | a measured page load for a 200-item board and task list stays under 500 ms | MUST | Performance & Efficiency |
| **RN2** | The system must maintain monthly service availability of at least 99.5%, excluding scheduled maintenance windows announced in advance. | monthly availability measured over any complete calendar month is at least 99.5%, excluding announced maintenance | MUST | Availability |
| **RN3** | The web application interface must be fully responsive, ensuring correct rendering on modern desktop and mobile viewports (minimum width of 375 px). | each viewport at or above 375 px width renders the board, task list, and forms without horizontal scroll or clipped controls | MUST | Usability |
| **RN4** | The storage architecture must support up to 50,000 active tasks per workspace without degradation in search, filter, or rendering speed. | a workspace holding 50,000 active tasks returns search, filter, and render results within the RN1 budget | SHOULD | Scalability |
| **RN5** | The system must execute automated daily database backups and maintain data recovery functionality with an RPO under 24 hours. | a restore from the most recent daily backup completes and returns the workspace to its pre-failure state within 24 hours of the failure | MUST | Recoverability · CRA → `SO-D-04.4-002` |
| **RN6** | The user interface must support internationalization (i18n), offering full system localization in English and Portuguese. | every user-facing string and date/number format resolves in both English and Portuguese | SHOULD | Internationalization |
| **RN7** | The payment gateway integration must communicate exclusively over authenticated secure channels and enforce cryptographic webhook signature verification. | an unsigned or wrongly-signed webhook is rejected without applying any subscription state change | MUST | Interoperability |
| **RN8** | The system architecture must enforce strict logical data segregation across workspaces (multi-tenancy), preventing cross-tenant access. | a read or write attempted across a workspace boundary is refused and logged | MUST | Architectural Integrity |
| **RN24** | The system shall cryptographically protect all data in transit across public and untrusted networks using state-of-the-art mechanisms, refusing or upgrading unencrypted connection attempts. | an unencrypted connection to a public interface is refused rather than downgraded | MUST | Security — Transport (GDPR Art. 32(1)(a)+Art. 32(2) + CRA Annex I Part I (2)(e) + (2)(j) → PO-D-01.2-001, SO-D-01.2-002 → PRIN-ENG-01 → CSF PR.DS-02, PR.IR-01 / PF PR.DS-P2) |
| **RN18** | The system shall record an immutable security audit entry for every authentication attempt, privilege elevation, permission rejection, subscription modification, access to or modification of personal data, and user-initiated deletion, retaining actor, action, timestamp, and origin. | every event class named in the requirement produces exactly one immutable entry carrying actor, action, timestamp, and origin, and no user-initiated deletion is missing an entry | MUST | Security — Auditability (CRA Annex I Part I (2)(l) → SO-D-10.1-002, SO-D-04.1-002 → PRIN-ENG-07 → CSF DE.CM-01, DE.CM-09) |
| **RN17** | The system shall authenticate inbound integration clients and throttle request volumes commensurate with operational capacity to protect availability against resource exhaustion, rejecting excess requests with a retry indication. | an inbound integration client without valid credentials is rejected, and a request burst beyond the stated capacity receives a retry indication instead of a queue | MUST | Security — Attack Surface (CRA Annex I Part I (2)(d)+(2)(j) → SO-D-07.2-002 → PRIN-ENG-02 → CSF PR.PS-02, PR.PS-06) |
| **RN29** | The product shall be accompanied by secure-use instructions — or an address where they can be consulted — covering commissioning and lifetime measures (membership and role management, credential handling, sharing-default configuration) for end users and administrators. | the published documentation contains a secure-use section covering all five listed topics, addressed to both end users and administrators | SHOULD | Security Documentation (CRA Annex II §8(a)–(e) → SO-D-08.1-002 → CSF PR.AT-01) |

---

## Bibliography

- Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
- Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley Professional.
- Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
- ISO/IEC/IEEE. (2018). *ISO/IEC/IEEE 29148: Systems and software engineering — Life cycle processes — Requirements engineering*.
- Mavin, A. et al. (2009). *EARS: Easy Approach to Requirements Syntax*. IEEE International Requirements Engineering Conference.

---

## Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| **1.0.0** | 2026-09-23 | Requirements Engineering Agent | Initial baseline elicitation (GPTools E1.1 structural model). |
| **2.0.0** | 2026-09-23 | Requirements Engineering Agent | Purified functional scope, removed pre-baked security controls, enforced English active verbs. |
| **2.1.0** | 2026-09-23 | Requirements Engineering Agent | Consolidated redundant requirements into 16 pure business requirements at Cockburn Sea Level. |
| **3.0.0** | 2026-09-23 | Requirements Engineering Agent | V1 Functional Refinement Pass: added derived requirement `R1.3` (locked-account recovery), refined `R7.2` and `R8.2`, elevated `R1.2` to MUST. |
| **4.0.0** | 2026-09-28 | Requirements Engineering Agent | Round 1 synthesis (ADR-005): 11 constraint chains re-anchored to Phase 2 objectives; new constraints RN27, RN28, RN29; derived requirement `R8.3` with `RN30`; 20 requirement cards. |
| **5.0.0** | 2026-10-01 | Requirements Engineering Agent | Modular separation pass: decoupled operational process flows and PUC catalog into [`Doc00_Process_and_Operational_Workflows.md`](Doc00_Process_and_Operational_Workflows.md). Refocused `Doc01` strictly on the atomic, contractual requirement specification cards and non-functional constraints with bidirectional traceability to PUCs. |
| **5.1.0** | 2026-10-10 | Requirements Engineering Agent | Consolidation pass: the superseded `Doc01_Requirements_Elicitation_and_PUC.md` (v4.0.0) was retired; this file is the single `Doc01`. Its Part I–III scope, As-Is model and PUC catalogue were already carried by [`Doc00_Process_and_Operational_Workflows.md`](Doc00_Process_and_Operational_Workflows.md), and the actor-to-functional-area context diagram was preserved in [`Doc02_System_Use_Cases.md`](Doc02_System_Use_Cases.md) §3.1. No requirement card changed. |
