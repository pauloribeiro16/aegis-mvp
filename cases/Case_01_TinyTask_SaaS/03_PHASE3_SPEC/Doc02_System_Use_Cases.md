# Doc02 — System Use Cases (TinyTask SaaS)

> **Document ID:** `TT-P3-DOC02`  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification (Functional Baseline)  
> **Reference Standard:** Triangular Functional Decomposition & GPTools E1.2 Standard  
> **Decomposition Level:** Level-0 to Level-1 System Use Cases (High-Level Baseline)  
> **Status:** Approved Functional Baseline  

---

## Table of Contents

1. [Methodological Approach](#1-methodological-approach)
   - 1.1 [Volere Decomposition & System Use Cases](#11-volere-decomposition--system-use-cases)
   - 1.2 [Triangular Functional Decomposition Model](#12-triangular-functional-decomposition-model)
   - 1.3 [Scoping Constraint: High-Level Sub-Cases (No Leaf Nodes)](#13-scoping-constraint-high-level-sub-cases-no-leaf-nodes)
2. [System Actors & Operational Profiles](#2-system-actors--operational-profiles)
3. [Level-0 System Use Case Diagram](#3-level-0-system-use-case-diagram)
4. [High-Level System Use Cases ({U.C.1} to {U.C.6})](#4-high-level-system-use-cases-uc1-to-uc6)
   - 4.1 [{U.C.1} — User Account & Authentication Management](#41-uc1--user-account--authentication-management)
     - 4.1.1 [Context & Business Objective](#411-context--business-objective)
     - 4.1.2 [Level-1 Refinement Diagram](#412-level-1-refinement-diagram)
     - 4.1.3 [Level-1 System Sub-Cases](#413-level-1-system-sub-cases)
   - 4.2 [{U.C.2} — Workspace & Team Administration](#42-uc2--workspace--team-administration)
     - 4.2.1 [Context & Business Objective](#421-context--business-objective)
     - 4.2.2 [Level-1 Refinement Diagram](#422-level-1-refinement-diagram)
     - 4.2.3 [Level-1 System Sub-Cases](#423-level-1-system-sub-cases)
   - 4.3 [{U.C.3} — Project & Task Lifecycle Management](#43-uc3--project--task-lifecycle-management)
     - 4.3.1 [Context & Business Objective](#431-context--business-objective)
     - 4.3.2 [Level-1 Refinement Diagram](#432-level-1-refinement-diagram)
     - 4.3.3 [Level-1 System Sub-Cases](#433-level-1-system-sub-cases)
   - 4.4 [{U.C.4} — Task Attachment Management](#44-uc4--task-attachment-management)
     - 4.4.1 [Context & Business Objective](#441-context--business-objective)
     - 4.4.2 [Level-1 Refinement Diagram](#442-level-1-refinement-diagram)
     - 4.4.3 [Level-1 System Sub-Cases](#443-level-1-system-sub-cases)
   - 4.5 [{U.C.5} — Team Collaboration & Activity Feeds](#45-uc5--team-collaboration--activity-feeds)
     - 4.5.1 [Context & Business Objective](#451-context--business-objective)
     - 4.5.2 [Level-1 Refinement Diagram](#452-level-1-refinement-diagram)
     - 4.5.3 [Level-1 System Sub-Cases](#453-level-1-system-sub-cases)
   - 4.6 [{U.C.6} — Commercial Subscriptions & Account Lifecycle](#46-uc6--commercial-subscriptions--account-lifecycle)
     - 4.6.1 [Context & Business Objective](#461-context--business-objective)
     - 4.6.2 [Level-1 Refinement Diagram](#462-level-1-refinement-diagram)
     - 4.6.3 [Level-1 System Sub-Cases](#463-level-1-system-sub-cases)
5. [Summary of System Use Cases & Requirements Traceability](#5-summary-of-system-use-cases--requirements-traceability)

---

## 1. Methodological Approach

### 1.1 Volere Decomposition & System Use Cases

In accordance with the Volere requirements engineering methodology and the GPTools E1.2 specification standard, **System Use Cases** bridge the gap between high-level business goals (Product Use Cases, documented in `Doc01_Requirements_Elicitation_and_PUC.md`) and technical software architecture.

While Product Use Cases capture the business interactions between external stakeholders and the system boundary, System Use Cases structure the operational capabilities provided by the platform to support those business interactions.

### 1.2 Triangular Functional Decomposition Model

The triangular decomposition organizes functionality hierarchically:
- **Level-0 System Use Case Diagram:** Macro-level view depicting the system boundary and the assignment of human/system actors to the 6 primary capability domains.
- **High-Level System Use Cases (`{U.C.1}` to `{U.C.6}`):** Domain-level operational umbrellas describing the strategic objectives of each functional area.
- **Level-1 System Sub-Cases (`{U.C.n.m}`):** Coherent, semi-granular functional sub-cases establishing the primary capabilities, participating actors, operational pre-conditions, and mapped functional requirements (`R1` to `R12`).

```mermaid
flowchart TD
    L0["Level-0 System Architecture<br>(6 High-Level System Use Cases)"] --> L1["Level-1 System Sub-Cases<br>({U.C.1.1} .. {U.C.6.4})"]
    L1 -.->|Future Refinement Phase| LF["Leaf Use Cases & Execution Flows<br>(Interactive Co-Design)"]
    L1 --> MFR["Mapped Functional Requirements<br>(R1 .. R12 from Doc01)"]
```

### 1.3 Scoping Constraint: High-Level Sub-Cases (No Leaf Nodes)

> [!IMPORTANT]
> **Strict Baseline Scoping Constraint:**  
> In compliance with the project's phasing strategy, this document establishes the functional specification strictly down to **Level-1 System Sub-Cases (`{U.C.n.m}`)**.  
> **Leaf Use Cases** (e.g., sub-sub levels such as `{U.C.n.m.k}`, detailed step-by-step UI dialog sequences, alternative exception paths, and execution pseudocode) are **deliberately excluded** from this baseline. Leaf nodes will be developed subsequently in interactive collaboration with stakeholders and engineering leads.

---

## 2. System Actors & Operational Profiles

System actors designate formal operational roles interacting with the TinyTask platform. A single physical user may hold different roles across distinct workspace tenants.

| Actor ID | Actor Name | Classification | Primary Responsibilities & Permissions |
|---|---|---|---|
| **`ACT-01`** | **`Workspace Owner`** | Privileged Human User | Holds full administrative authority over a specific workspace tenant. Exclusively manages commercial subscription tiers, billing payment methods, tenant-wide data export, and workspace deletion. |
| **`ACT-02`** | **`Workspace Admin`** | Privileged Human User | Manages day-to-day organizational operations within a workspace. Authorized to invite new members, assign and modify member roles (`Admin`, `Member`, `Viewer`), create and archive projects, and manage team quotas. |
| **`ACT-03`** | **`Workspace Member`** | Operational Human User | Core collaborative user. Can create, edit, assign, and transition tasks; upload file attachments; post comments and `@mentions`; and inspect project Kanban boards. |
| **`ACT-04`** | **`Workspace Viewer`** | Read-Only Human User | External client, guest reviewer, or observer. Granted read-only visibility into projects, task lists, and comment feeds. Cannot create, modify, or delete any workspace artifacts. |
| **`ACT-05`** | **`External Payment Gateway`** | External System (Stripe) | External payment processing engine that interacts via secure HTTPS APIs and delivers signed asynchronous webhook notifications concerning subscription state changes. |
| **`ACT-06`** | **`System Scheduler`** | Automated Background Process | Internal background daemon executing periodic jobs, including daily email notification digests, token expiration sweeps, and retention cleanups. |

---

## 3. Level-0 System Use Case Diagram

The Level-0 diagram illustrates the global system boundary and the interactions between all system actors and the 6 primary System Use Cases.

```mermaid
flowchart LR
    subgraph Actors ["System Actors"]
        Owner["Workspace Owner<br>(ACT-01)"]
        Admin["Workspace Admin<br>(ACT-02)"]
        Member["Workspace Member<br>(ACT-03)"]
        Viewer["Workspace Viewer<br>(ACT-04)"]
        Stripe["External Payment Gateway<br>(ACT-05)"]
        Scheduler["System Scheduler<br>(ACT-06)"]
    end

    subgraph TinyTask_System ["TinyTask SaaS — Level-0 System Boundary"]
        UC1["{U.C.1}<br>User Account & Authentication"]
        UC2["{U.C.2}<br>Workspace & Team Administration"]
        UC3["{U.C.3}<br>Project & Task Lifecycle Management"]
        UC4["{U.C.4}<br>Task Attachment Management"]
        UC5["{U.C.5}<br>Team Collaboration & Activity Feeds"]
        UC6["{U.C.6}<br>Subscriptions & Account Lifecycle"]
    end

    Owner --> UC1
    Owner --> UC2
    Owner --> UC6

    Admin --> UC1
    Admin --> UC2
    Admin --> UC3
    Admin --> UC4
    Admin --> UC5

    Member --> UC1
    Member --> UC3
    Member --> UC4
    Member --> UC5

    Viewer --> UC1
    Viewer --> UC3
    Viewer --> UC5

    Stripe --> UC6
    Scheduler --> UC5
    Scheduler --> UC6
```

---

## 4. High-Level System Use Cases ({U.C.1} to {U.C.6})

### 4.1 {U.C.1} — User Account & Authentication Management

#### 4.1.1 Context & Business Objective
Provides user onboarding, identity verification, credential authentication, password recovery, and tenant membership access. It ensures that every user can securely sign in and access their authorized workspaces.

#### 4.1.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC1["{U.C.1} User Account & Authentication Management"] --> UC11["{U.C.1.1} User Registration & Email Verification"]
    UC1 --> UC12["{U.C.1.2} Credential Authentication & Session Issuance"]
    UC1 --> UC13["{U.C.1.3} Password Recovery Workflow"]
    UC1 --> UC14["{U.C.1.4} Tenant Role Resolution & Session Review"]
```

#### 4.1.3 Level-1 System Sub-Cases

##### `{U.C.1.1}` — User Registration & Email Verification
- **Primary Actor:** `New User` (Unauthenticated)
- **Scope & Purpose:** Enable self-service registration of a new user account, validating email format, verifying address ownership via email verification link, and creating the initial user profile.
- **Pre-conditions:** The user is unauthenticated and possesses an accessible email address.
- **Triggers:** User submits registration form on the public web application.
- **Data In / Out:**
  - `in`: Full name, email address, password, terms acceptance.
  - `out`: Verification email dispatched; pending user account record created.
- **Mapped Functional Requirements:** `R1.1`.

##### `{U.C.1.2}` — Credential Authentication & Session Issuance
- **Primary Actor:** `Registered User`
- **Scope & Purpose:** Validate user-supplied credentials (email and password), generate active login session, and retrieve accessible workspace memberships.
- **Pre-conditions:** User account exists and email verification is complete.
- **Triggers:** User submits login credentials.
- **Data In / Out:**
  - `in`: Email address, password credentials.
  - `out`: Active user session, user profile, list of authorized workspace memberships.
- **Mapped Functional Requirements:** `R1.2`, `R1.6`, `R1.7`.

##### `{U.C.1.3}` — Password Recovery Workflow
- **Primary Actor:** `Registered User`
- **Scope & Purpose:** Allow users who have forgotten their password to safely regain account access via a single-use reset link sent to their registered email address, terminating active sessions upon password reset.
- **Pre-conditions:** User has an active, registered account.
- **Triggers:** User selects "Forgot Password" on login interface.
- **Data In / Out:**
  - `in`: Account email address; reset token; new password credentials.
  - `out`: Reset link email dispatched; updated password; existing sessions terminated.
- **Mapped Functional Requirements:** `R1.3`.

##### `{U.C.1.4}` — Tenant Role Resolution & Session Review
- **Primary Actor:** `Workspace User` (`Owner`, `Admin`, `Member`, `Viewer`)
- **Scope & Purpose:** Evaluate the requesting user's active session against the target workspace boundary, apply Role-Based Access Control (RBAC), and allow users to inspect and log out active sessions.
- **Pre-conditions:** User possesses an active session.
- **Triggers:** User switches workspace context or inspects active sessions under account settings.
- **Data In / Out:**
  - `in`: Active session, target `workspace_id`, session termination command.
  - `out`: Workspace permission context; list of active sessions; logout confirmation.
- **Mapped Functional Requirements:** `R1.4`, `R1.5`.

---

### 4.2 {U.C.2} — Workspace & Team Administration

#### 4.2.1 Context & Business Objective
Governs multi-tenant workspace creation, member invitation workflows, role administration, and subscription quota monitoring. It enables organizations to coordinate teams while preserving strict separation between workspaces.

#### 4.2.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC2["{U.C.2} Workspace & Team Administration"] --> UC21["{U.C.2.1} Workspace Tenant Provisioning"]
    UC2 --> UC22["{U.C.2.2} Member Invitation Workflow"]
    UC2 --> UC23["{U.C.2.3} Member Role Administration & Offboarding"]
    UC2 --> UC24["{U.C.2.4} Workspace Settings & Quota Monitoring"]
```

#### 4.2.3 Level-1 System Sub-Cases

##### `{U.C.2.1}` — Workspace Tenant Provisioning
- **Primary Actor:** `Authenticated User`
- **Scope & Purpose:** Provision a distinct workspace tenant with a custom organizational name and unique URL slug, establishing the creator as the initial `Workspace Owner`.
- **Pre-conditions:** User is authenticated.
- **Triggers:** User initiates workspace creation from the workspace switcher interface.
- **Data In / Out:**
  - `in`: Workspace name, unique URL slug, initial plan tier selection.
  - `out`: Provisioned workspace tenant, initial default project, `Workspace Owner` role binding.
- **Mapped Functional Requirements:** `R2.1`.

##### `{U.C.2.2}` — Member Invitation Workflow
- **Primary Actor:** `Workspace Owner`, `Workspace Admin`
- **Scope & Purpose:** Invite team members to join the workspace by email, verifying that current member counts do not exceed the plan tier seat quota, and dispatching invitation emails.
- **Pre-conditions:** Requesting user holds `Owner` or `Admin` privileges in the workspace.
- **Triggers:** Admin enters invitee email and selects an initial role.
- **Data In / Out:**
  - `in`: Invitee email address, target role (`Admin`, `Member`, `Viewer`).
  - `out`: Invitation link emailed; pending membership record registered.
- **Mapped Functional Requirements:** `R2.2`.

##### `{U.C.2.3}` — Member Role Administration & Offboarding
- **Primary Actor:** `Workspace Owner`, `Workspace Admin`
- **Scope & Purpose:** Modify assigned roles of active members or remove members entirely, immediately revoking their access to workspace data while retaining historical attribution.
- **Pre-conditions:** Target user is an active member of the workspace; the `Workspace Owner` cannot be removed by an `Admin`.
- **Triggers:** Admin selects role change or member removal command in workspace settings.
- **Data In / Out:**
  - `in`: Target `user_id`, new role designation, or removal command.
  - `out`: Updated membership record; revocation of access; member list refreshed.
- **Mapped Functional Requirements:** `R2.3`, `R2.6`.

##### `{U.C.2.4}` — Workspace Settings & Quota Monitoring
- **Primary Actor:** `Workspace Owner`, `Workspace Admin`
- **Scope & Purpose:** Review workspace resource utilization (active seats, project counts) against active plan tier limits, and manage general workspace metadata (name, logo).
- **Pre-conditions:** User holds `Owner` or `Admin` role in the workspace.
- **Triggers:** Admin accesses the workspace settings dashboard.
- **Data In / Out:**
  - `in`: Workspace query parameters; optional updated organizational name/logo.
  - `out`: Utilization metrics display (allocated seats vs limit); updated workspace profile.
- **Mapped Functional Requirements:** `R2.4`, `R2.5`.

---

### 4.3 {U.C.3} — Project & Task Lifecycle Management

#### 4.3.1 Context & Business Objective
Forms the core operational engine of TinyTask. It provides project containerization, task authoring, assignment, priority tagging, due date tracking, and workflow state progression across Kanban and list representations.

#### 4.3.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC3["{U.C.3} Project & Task Lifecycle Management"] --> UC31["{U.C.3.1} Project Container Management"]
    UC3 --> UC32["{U.C.3.2} Task Authoring & Attribution"]
    UC3 --> UC33["{U.C.3.3} Workflow Progression & Board State Updates"]
    UC3 --> UC34["{U.C.3.4} Multi-Dimensional Task Filtering & Views"]
```

#### 4.3.3 Level-1 System Sub-Cases

##### `{U.C.3.1}` — Project Container Management
- **Primary Actor:** `Workspace Admin`, `Workspace Member`
- **Scope & Purpose:** Create, configure, update, and archive project containers that house discrete sets of tasks and collaborative threads.
- **Pre-conditions:** User is an active workspace member with creation privileges.
- **Triggers:** User creates or modifies a project.
- **Data In / Out:**
  - `in`: Project name, description, privacy setting, archive command.
  - `out`: Created/updated project record; project listing update.
- **Mapped Functional Requirements:** `R3.1`, `R3.2`.

##### `{U.C.3.2}` — Task Authoring & Attribution
- **Primary Actor:** `Workspace Member`, `Workspace Admin`
- **Scope & Purpose:** Define new work items within a project, specifying task title, description, priority level, target due date, and assigning responsibility to a workspace colleague.
- **Pre-conditions:** Containing project exists and is active (not archived).
- **Triggers:** User clicks "New Task" and submits form.
- **Data In / Out:**
  - `in`: Project ID, title, description, priority (`Low`, `Medium`, `High`, `Urgent`), assignee ID, due date.
  - `out`: Created task record; assignment notification routed to assignee.
- **Mapped Functional Requirements:** `R4.1`, `R4.2`, `R4.3`.

##### `{U.C.3.3}` — Workflow Progression & Board State Updates
- **Primary Actor:** `Workspace Member`, `Workspace Admin`
- **Scope & Purpose:** Transition tasks through standard operational stages (`To-Do`, `In-Progress`, `Under-Review`, `Done`), supporting drag-and-drop interactions on Kanban boards.
- **Pre-conditions:** Task exists; requesting user is an active workspace member.
- **Triggers:** User moves task card on Kanban board or changes status selector.
- **Data In / Out:**
  - `in`: Target `task_id`, new status value.
  - `out`: Updated task entity; board column reordering; activity log record; optional recurring task clone trigger.
- **Mapped Functional Requirements:** `R5.1`, `R5.2`, `R5.3`.

##### `{U.C.3.4}` — Multi-Dimensional Task Filtering & Views
- **Primary Actor:** `Workspace User` (`Owner`, `Admin`, `Member`, `Viewer`)
- **Scope & Purpose:** Query and display tasks according to selectable criteria, including assignee, status, priority, and date ranges, presented in customizable views.
- **Pre-conditions:** User has read access to the workspace.
- **Triggers:** User applies search keywords or filters on project view.
- **Data In / Out:**
  - `in`: Filter criteria (assignee ID, status list, priority list, due date range, sorting order).
  - `out`: Rendered task dataset matching filter criteria.
- **Mapped Functional Requirements:** `R6.1`, `R6.2`.

---

### 4.4 {U.C.4} — Task Attachment Management

#### 4.4.1 Context & Business Objective
Provides upload, storage, retrieval, and disposal of files and media assets associated with tasks, enforcing file size limits and easy access for team members.

#### 4.4.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC4["{U.C.4} Task Attachment Management"] --> UC41["{U.C.4.1} Task File Upload"]
    UC4 --> UC42["{U.C.4.2} Attachment Retrieval & Preview"]
    UC4 --> UC43["{U.C.4.3} Attachment Removal"]
```

#### 4.4.3 Level-1 System Sub-Cases

##### `{U.C.4.1}` — Task File Upload
- **Primary Actor:** `Workspace Member`, `Workspace Admin`
- **Scope & Purpose:** Upload file attachments (documents, spreadsheets, images) to a task, enforcing the 25 MB size cap.
- **Pre-conditions:** Task exists; user is authorized to edit the task.
- **Triggers:** User adds a file to the task attachment section.
- **Data In / Out:**
  - `in`: `task_id`, file binary, filename, file size.
  - `out`: Stored attachment record; task attachment list updated.
- **Mapped Functional Requirements:** `R7.1`, `R7.2`.

##### `{U.C.4.2}` — Attachment Retrieval & Preview
- **Primary Actor:** `Workspace User` (`Owner`, `Admin`, `Member`, `Viewer`)
- **Scope & Purpose:** Enable authorized users to download or preview task attachments associated with projects they can view.
- **Pre-conditions:** User belongs to the workspace containing the parent task.
- **Triggers:** User clicks on an attachment preview thumbnail or download button.
- **Data In / Out:**
  - `in`: `attachment_id`, `task_id`.
  - `out`: Downloadable file stream; optional thumbnail preview rendering.
- **Mapped Functional Requirements:** `R8.1`, `R8.3`.

##### `{U.C.4.3}` — Attachment Removal
- **Primary Actor:** `Workspace Member` (Uploader), `Workspace Admin`, `Workspace Owner`
- **Scope & Purpose:** Remove an attachment from a task, removing the record and associated file storage.
- **Pre-conditions:** User is either the original uploader or holds `Admin`/`Owner` role.
- **Triggers:** User clicks "Delete Attachment" and confirms.
- **Data In / Out:**
  - `in`: `attachment_id`, deletion confirmation.
  - `out`: Removed attachment record; task card updated.
- **Mapped Functional Requirements:** `R8.2`.

---

### 4.5 {U.C.5} — Team Collaboration & Activity Feeds

#### 4.5.1 Context & Business Objective
Enables communication among team members through Markdown task comments, user `@mentions`, activity history tracking, and automated email summary notifications.

#### 4.5.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC5["{U.C.5} Team Collaboration & Activity Feeds"] --> UC51["{U.C.5.1} Task Discussion & Collaborative Mentions"]
    UC5 --> UC52["{U.C.5.2} Workspace Event Stream & In-App Alerts"]
    UC5 --> UC53["{U.C.5.3} Scheduled Email Digest Generation"]
```

#### 4.5.3 Level-1 System Sub-Cases

##### `{U.C.5.1}` — Task Discussion & Collaborative Mentions
- **Primary Actor:** `Workspace Member`, `Workspace Admin`
- **Scope & Purpose:** Enable threaded discussion on tasks using Markdown formatting, parsing `@username` mentions to trigger targeted notifications for mentioned colleagues.
- **Pre-conditions:** Target task exists in an active project.
- **Triggers:** User submits a comment on the task detail panel.
- **Data In / Out:**
  - `in`: `task_id`, Markdown comment text, tagged user references.
  - `out`: Appended comment record; notifications dispatched to tagged users.
- **Mapped Functional Requirements:** `R9.1`, `R9.2`, `R9.3`.

##### `{U.C.5.2}` — Workspace Event Stream & In-App Alerts
- **Primary Actor:** `Workspace User` (`Owner`, `Admin`, `Member`, `Viewer`)
- **Scope & Purpose:** Record chronological history for task transitions and deliver notifications to the user's notification center.
- **Pre-conditions:** User is authenticated within a workspace.
- **Triggers:** Any state-changing event occurs on tasks assigned to or observed by the user.
- **Data In / Out:**
  - `in`: State-change event stream; user notification acknowledgment.
  - `out`: Notification badge counter update; chronological activity feed entries.
- **Mapped Functional Requirements:** `R10.1`, `R10.2`.

##### `{U.C.5.3}` — Scheduled Email Digest Generation
- **Primary Actor:** `System Scheduler`
- **Scope & Purpose:** Aggregate outstanding task due dates, overdue assignments, and unread mentions for each user into a daily email digest.
- **Pre-conditions:** Scheduler cron executes; user has daily digest enabled in preferences.
- **Triggers:** Daily schedule timer fires at 08:00 UTC.
- **Data In / Out:**
  - `in`: Pending unread notification records, user digest preferences.
  - `out`: Formatted summary email dispatched via transactional email provider.
- **Mapped Functional Requirements:** `R10.3`.

---

### 4.6 {U.C.6} — Commercial Subscriptions & Account Lifecycle

#### 4.6.1 Context & Business Objective
Encompasses the commercial subscription lifecycle (plan checkout, tier upgrades, Stripe webhook processing) alongside self-service data export and account closure workflows.

#### 4.6.2 Level-1 Refinement Diagram

```mermaid
flowchart TD
    UC6["{U.C.6} Commercial Subscriptions & Account Lifecycle"] --> UC61["{U.C.6.1} Plan Upgrade & Checkout Initiation"]
    UC6 --> UC62["{U.C.6.2} Webhook Subscription Reconciliation"]
    UC6 --> UC63["{U.C.6.3} Self-Service User Data Export"]
    UC6 --> UC64["{U.C.6.4} Account Closure & Name Anonymization"]
```

#### 4.6.3 Level-1 System Sub-Cases

##### `{U.C.6.1}` — Plan Upgrade & Checkout Initiation
- **Primary Actor:** `Workspace Owner`
- **Scope & Purpose:** Enable the Workspace Owner to select an upgraded plan tier (`Pro` or `Enterprise`), generating a hosted Stripe Checkout session.
- **Pre-conditions:** Requesting user is the verified `Workspace Owner`.
- **Triggers:** Owner selects "Upgrade Plan" in workspace billing settings.
- **Data In / Out:**
  - `in`: Desired plan tier ID, billing cycle (monthly/annual), return URL.
  - `out`: Hosted Stripe Checkout session URL redirect.
- **Mapped Functional Requirements:** `R11.1`.

##### `{U.C.6.2}` — Webhook Subscription Reconciliation
- **Primary Actor:** `External Payment Gateway` (Stripe)
- **Scope & Purpose:** Ingest and process incoming payment gateway webhooks to update workspace subscription statuses, seat quotas, and payment failure states.
- **Pre-conditions:** Webhook payload delivered from payment gateway.
- **Triggers:** Stripe delivers an HTTP POST request to the webhook endpoint.
- **Data In / Out:**
  - `in`: Webhook payload (`invoice.payment_succeeded`, etc.).
  - `out`: Updated workspace tier quota and billing status.
- **Mapped Functional Requirements:** `R11.2`, `R11.3`, `R11.4`.

##### `{U.C.6.3}` — Self-Service User Data Export
- **Primary Actor:** `Workspace Owner`, `Registered User`
- **Scope & Purpose:** Enable users to request an automated export of their personal account data or workspace data in structured formats (JSON and ZIP archive).
- **Pre-conditions:** User is authenticated and submits request.
- **Triggers:** User requests data export under account or workspace settings.
- **Data In / Out:**
  - `in`: Export scope request (personal data or full workspace).
  - `out`: Background export job queued; download link delivered to requester upon completion.
- **Mapped Functional Requirements:** `R12.1`, `R12.2`.

##### `{U.C.6.4}` — Account Closure & Name Anonymization
- **Primary Actor:** `Workspace Owner`, `Registered User`
- **Scope & Purpose:** Execute user account deletion requests, removing login credentials and anonymizing display names across historical task logs to `[Deleted User]`.
- **Pre-conditions:** User confirms deletion with password verification; if Workspace Owner, either transfers ownership or deletes the workspace tenant.
- **Triggers:** User submits account/workspace deletion request.
- **Data In / Out:**
  - `in`: User password re-verification, confirmation token.
  - `out`: User login removed; historical comments attributed to `[Deleted User]`; closure confirmation receipt.
- **Mapped Functional Requirements:** `R12.3`, `R12.4`.

---

## 5. Summary of System Use Cases & Requirements Traceability

The matrix below provides complete bidirectional traceability between all **Level-1 System Sub-Cases** and the **Functional Requirements** defined in `Doc01_Requirements_Elicitation_and_PUC.md`.

| High-Level UC | Level-1 Sub-Case | Sub-Case Title | Primary Actor | Mapped Functional Requirements |
|---|---|---|---|---|
| **`{U.C.1}`** | `{U.C.1.1}` | User Registration & Email Verification | New User | `R1.1` |
| | `{U.C.1.2}` | Credential Authentication & Session Issuance | Registered User | `R1.2`, `R1.6`, `R1.7` |
| | `{U.C.1.3}` | Password Recovery Workflow | Registered User | `R1.3` |
| | `{U.C.1.4}` | Tenant Role Resolution & Session Review | Workspace User | `R1.4`, `R1.5` |
| **`{U.C.2}`** | `{U.C.2.1}` | Workspace Tenant Provisioning | Authenticated User | `R2.1` |
| | `{U.C.2.2}` | Member Invitation Workflow | Workspace Owner / Admin | `R2.2` |
| | `{U.C.2.3}` | Member Role Administration & Offboarding | Workspace Owner / Admin | `R2.3`, `R2.6` |
| | `{U.C.2.4}` | Workspace Settings & Quota Monitoring | Workspace Owner / Admin | `R2.4`, `R2.5` |
| **`{U.C.3}`** | `{U.C.3.1}` | Project Container Management | Workspace Admin / Member | `R3.1`, `R3.2` |
| | `{U.C.3.2}` | Task Authoring & Attribution | Workspace Member / Admin | `R4.1`, `R4.2`, `R4.3` |
| | `{U.C.3.3}` | Workflow Progression & Board State Updates | Workspace Member / Admin | `R5.1`, `R5.2`, `R5.3` |
| | `{U.C.3.4}` | Multi-Dimensional Task Filtering & Views | Workspace User | `R6.1`, `R6.2` |
| **`{U.C.4}`** | `{U.C.4.1}` | Task File Upload | Workspace Member / Admin | `R7.1`, `R7.2` |
| | `{U.C.4.2}` | Attachment Retrieval & Preview | Workspace User | `R8.1`, `R8.3` |
| | `{U.C.4.3}` | Attachment Removal | Workspace Member / Admin | `R8.2` |
| **`{U.C.5}`** | `{U.C.5.1}` | Task Discussion & Collaborative Mentions | Workspace Member / Admin | `R9.1`, `R9.2`, `R9.3` |
| | `{U.C.5.2}` | Workspace Event Stream & In-App Alerts | Workspace User | `R10.1`, `R10.2` |
| | `{U.C.5.3}` | Scheduled Email Digest Generation | System Scheduler | `R10.3` |
| **`{U.C.6}`** | `{U.C.6.1}` | Plan Upgrade & Checkout Initiation | Workspace Owner | `R11.1` |
| | `{U.C.6.2}` | Webhook Subscription Reconciliation | External Payment Gateway | `R11.2`, `R11.3`, `R11.4` |
| | `{U.C.6.3}` | Self-Service User Data Export | Workspace Owner / User | `R12.1`, `R12.2` |
| | `{U.C.6.4}` | Account Closure & Name Anonymization | Workspace Owner / User | `R12.3`, `R12.4` |
