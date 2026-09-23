# Doc01 — AS-IS / TO-BE Model & Requirements Elicitation (TinyTask SaaS)

> **Document ID:** `TT-P3-DOC01`  
> **Deliverable Reference:** `E1.1 – TinyTask SaaS AS-IS / TO-BE Model & Requirements Elicitation`  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification (Functional Baseline)  
> **Reference Standard:** GPTools Deliverable E1.1 Standard (`GPTools_ModeloASIS_TOBE V2.0`)  
> **Prioritization Model:** MoSCoW (MUST, SHOULD, COULD, WON'T)  
> **Language:** English  
> **Status:** Approved Functional Baseline  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Glossary](#2-glossary)
3. [Part I — Scope](#3-part-i--scope)
   - 3.1 [Objective](#31-objective)
     - 3.1.1 [Problem Description](#311-problem-description)
     - 3.1.2 [Product Position Description](#312-product-position-description)
     - 3.1.3 [Expected Impact](#313-expected-impact)
     - 3.1.4 [Key Characteristics](#314-key-characteristics)
   - 3.2 [Stakeholders](#32-stakeholders)
   - 3.3 [System Users](#33-system-users)
   - 3.4 [Constraints](#34-constraints)
4. [Part II — As-Is](#4-part-ii--as-is)
   - 4.1 [Business Roles in Context](#41-business-roles-in-context)
   - 4.2 [As-Is Workflow Processes & Information Fragmentation](#42-as-is-workflow-processes--information-fragmentation)
     - 4.2.1 [Gathering General Project Information](#421-gathering-general-project-information)
     - 4.2.2 [Task Definition, Attribution, and Scheduling](#422-task-definition-attribution-and-scheduling)
     - 4.2.3 [Tracking Task Progress and Executed Time](#423-tracking-task-progress-and-executed-time)
     - 4.2.4 [Managing Attachments, Specifications, and Media](#424-managing-attachments-specifications-and-media)
     - 4.2.5 [Handling Commercial Subscriptions and Invoicing](#425-handling-commercial-subscriptions-and-invoicing)
     - 4.2.6 [Handling Customer Data Export & Account Deletion Requests](#426-handling-customer-data-export--account-deletion-requests)
   - 4.3 [Current IT Support & Operational Deficiencies](#43-current-it-support--operational-deficiencies)
     - 4.3.1 [Spreadsheet-Driven Tracking Limitations](#431-spreadsheet-driven-tracking-limitations)
     - 4.3.2 [Dispersed Email and Instant Messaging Chains](#432-dispersed-email-and-instant-messaging-chains)
     - 4.3.3 [Unmanaged Cloud Storage Drives](#433-unmanaged-cloud-storage-drives)
     - 4.3.4 [Lack of Centralized Account and Data Lifecycle Controls](#434-lack-of-centralized-account-and-data-lifecycle-controls)
5. [Part III — To-Be](#5-part-iii--to-be)
   - 5.1 [Initial Customer Expectations](#51-initial-customer-expectations)
   - 5.2 [System Actors](#52-system-actors)
   - 5.3 [Functional Requirements (MoSCoW)](#53-functional-requirements-moscow)
     - 5.3.1 [MoSCoW Prioritization Technique](#531-moscow-prioritization-technique)
     - 5.3.2 [Summary Table of Functional Requirements](#532-summary-table-of-functional-requirements)
     - 5.3.3 [Detailed Specifications of Functional Requirements](#533-detailed-specifications-of-functional-requirements)
   - 5.4 [Non-Functional Requirements](#54-non-functional-requirements)
     - 5.4.1 [Domain Non-Functional Requirements](#541-domain-non-functional-requirements)
     - 5.4.2 [Operational & Infrastructure Non-Functional Requirements](#542-operational--infrastructure-non-functional-requirements)
   - 5.5 [Business Use Cases & Product Use Cases (PUC)](#55-business-use-cases--product-use-cases-puc)
   - 5.6 [System Use Case Model ({U.C.1} to {U.C.6})](#56-system-use-case-model-uc1-to-uc6)
     - 5.6.1 [{U.C.1} — Authenticate and Manage User Accounts](#561-uc1--authenticate-and-manage-user-accounts)
     - 5.6.2 [{U.C.2} — Configure and Administrate Workspaces](#562-uc2--configure-and-administrate-workspaces)
     - 5.6.3 [{U.C.3} — Manage Projects and Tasks Lifecycle](#563-uc3--manage-projects-and-tasks-lifecycle)
     - 5.6.4 [{U.C.4} — Ingest and Manage Attachments and Media](#564-uc4--ingest-and-manage-attachments-and-media)
     - 5.6.5 [{U.C.5} — Manage Team Collaboration and Notification Alerts](#565-uc5--manage-team-collaboration-and-notification-alerts)
     - 5.6.6 [{U.C.6} — Manage Commercial Subscriptions and Account Lifecycle](#566-uc6--manage-commercial-subscriptions-and-account-lifecycle)
6. [Conclusions](#6-conclusions)
7. [Bibliography](#7-bibliography)

---

## 1. Executive Summary

This deliverable specifies the formal **AS-IS / TO-BE Architecture** and **Functional Requirements Elicitation Baseline** for **TinyTask SaaS** (Case 01). TinyTask is a multi-tenant B2B task management, project coordination, and team collaboration web application designed for small and medium-sized enterprises.

Applying the methodological framework of CCG GPTools Deliverable E1.1 (`GPTools_ModeloASIS_TOBE V2.0`), this document captures the **pure functional baseline** of the product as conceived by business stakeholders and prospective users—representing the incoming functional input that will subsequently be hardened with security and privacy requirements in Phase 3.

The analysis provides:
1. **Scope & Context:** Operational problem positioning, target product characteristics, stakeholders, user roles, and business constraints;
2. **As-Is Operational Model:** Detailed analysis of existing manual workflows across spreadsheets, informal messaging channels, and unmanaged file shares, supported by 6 data tables of manually manipulated fields;
3. **To-Be System Model:** Formal customer expectations, system actors, an exhaustive summary table of functional requirements (`R1` through `R12`, comprising 38 functional statements) prioritized via MoSCoW, **individual formal specification cards for every requirement**, domain quality attributes, a Product Use Case (PUC) summary table, and the Level-0/Level-1 System Use Case architecture (`{U.C.1}` to `{U.C.6}`).

---

## 2. Glossary

The following table provides the glossary of terms and acronyms utilized throughout this specification:

*Table 1 — Glossary & Acronyms*

| Term / Acronym | Definition |
|---|---|
| **As-Is** | The baseline operational state of workflow execution, tools, and data flows before the adoption of TinyTask SaaS. |
| **To-Be** | The target operational state enabled by the implementation and deployment of the TinyTask SaaS platform. |
| **B2B** | Business-to-Business commercial software model where services are rendered to organizations. |
| **Kanban** | Visual workflow management method displaying work items across sequential status columns. |
| **MoSCoW** | Prioritization methodology classifying requirements into Must have, Should have, Could have, and Won't have. |
| **Multi-Tenancy** | Software architecture where a single instance of software serves multiple customer organizations with logical data isolation. |
| **PUC** | Product Use Case — business-level interaction boundary defined in the Volere requirements specification process. |
| **RBAC** | Role-Based Access Control enforcing permission policies based on user organizational roles. |
| **SaaS** | Software-as-a-Service cloud delivery model. |
| **Stripe** | External financial payment gateway managing customer credit card tokenization, subscriptions, and webhooks. |
| **U.C.** | Use Case designation within the system functional decomposition. |
| **Workspace** | Tenant boundary isolating projects, tasks, members, uploaded media, and commercial subscriptions for an organization. |

---

## 3. Part I — Scope

### 3.1 Objective

#### 3.1.1 Problem Description
Small businesses, creative agencies, digital consultancies, and agile software development teams frequently suffer from severe operational friction in their daily project execution. Teams of 5 to 50 collaborators typically manage work through a disjointed patchwork of disconnected tools: shared spreadsheets that lack real-time synchronization, endless email chains with buried attachments, informal chat messages on WhatsApp or Slack where tasks are assigned without due dates or accountable ownership, and unmanaged cloud storage folders where document versions overwrite each other.

This operational fragmentation produces critical business failures:
1. **Lack of Centralized Visibility:** Project leaders and team managers cannot easily observe the real-time status of work items, resulting in missed customer deadlines and resource bottlenecks.
2. **Accountability Deficit:** Without formal assignment, status progression, and change auditing, tasks fall through organizational cracks.
3. **Collaboration Inefficiencies:** Conversations about tasks are scattered across emails and chat rooms rather than being attached directly to the task context.
4. **Administrative Overhead:** Significant billable hours are wasted manually updating tracking spreadsheets, chasing colleagues for status reports, and locating misplaced document revisions.

#### 3.1.2 Product Position Description
**TinyTask SaaS** is positioned as an intuitive, unified, cloud-native B2B productivity platform specifically engineered for small and medium-sized organizations. Unlike heavyweight enterprise project management suites that suffer from extreme configuration complexity and high licensing costs, TinyTask delivers a lean, focused workspace experience combining:
- Frictionless task lifecycle management across interactive Kanban and tabular views;
- Contextual team discussions directly embedded within task cards;
- File attachment ingestion directly associated with tasks;
- Multi-tenant organizational isolation with self-service subscription management and user data export/deletion.

#### 3.1.3 Expected Impact
Implementing TinyTask yields direct, measurable organizational improvements:
- **Efficiency Gains:** Reduces internal status reporting and task lookup time by over 40% through centralized boards and automated notifications.
- **Delivery Reliability:** Decreases overdue task rates through clear attribution, explicit priority tagging, and automated deadline reminders.
- **Team Alignment:** Keeps team discussions, files, and updates unified in a single task card view.
- **Commercial Scalability:** Enables the TinyTask enterprise to operate a sustainable, recurring subscription revenue model (Free, Pro, and Enterprise tiers) powered by automated payment gateway integration.

#### 3.1.4 Key Characteristics
The TinyTask platform delivers the following primary functional characteristics:
1. **Multi-Tenant Workspace Structure:** Logical segregation ensuring an organization's projects, tasks, files, and users belong to distinct workspaces.
2. **Dynamic Work Views:** Instant switching between visual Kanban board workflows (drag-and-drop state progression) and filterable tabular task registers.
3. **Contextual In-Task Collaboration:** Rich-text Markdown comments with `@username` tagging that immediately alerts mentioned colleagues.
4. **Task Attachment Handling:** Direct file uploads associated with tasks with user-friendly download and deletion controls.
5. **Role-Based Access Governance:** Permission differentiation across four canonical workspace roles (`Owner`, `Admin`, `Member`, `Viewer`).
6. **Turnkey Subscription Lifecycle:** Self-service checkout, automated tier provisioning, and webhook reconciliation via integration with external payment gateways (Stripe).
7. **Self-Service Account Lifecycle:** User data export and account closure workflows.
8. **Automated Notification Feeds:** In-app notification center and scheduled daily summary digest emails.
9. **Responsive Multi-Device Access:** Standards-compliant web application operating seamlessly on desktop and mobile browsers.
10. **Activity History Feeds:** Automatic recording of task status updates, assignee changes, and comments.

### 3.2 Stakeholders

The key stakeholders holding a direct or indirect interest in the development and operation of TinyTask SaaS include:

*Table 2 — Stakeholders*

| Stakeholder Group | Representative Profile | Core Interest & Expectations |
|---|---|---|
| **Platform Founders & Executives** | TinyTask Micro-Enterprise Leadership (Lisbon) | Sustainable product-market fit, low operational overhead, high customer retention, and automated subscription revenue collection. |
| **Engineering & Operations Team** | TinyTask 8-Person Core Technical Team | Modular, maintainable codebase, low infrastructure maintenance burden, robust automated testing, and clean software architecture. |
| **Subscribing Organization Owners** | SME Business Owners, Agency Executives | High team productivity, affordable predictable software costs, secure workspace isolation, and full ownership of business data. |
| **Team Leaders & Project Managers** | Department Leads, Project Coordinators | Real-time operational visibility into task bottlenecks, seamless delegation, and automated progress notifications. |
| **Individual Contributors** | Engineers, Designers, Marketing Specialists | Clean, intuitive task tracking without administrative friction, clear priorities, and focused communication. |
| **External Clients & Guests** | Third-Party Stakeholders, Project Observers | Read-only inspection of deliverables and progress without operational friction. |

### 3.3 System Users

System users correspond directly to the operational roles recognized by the TinyTask application:

*Table 3 — System Users*

| System User | Definition |
|---|---|
| **Workspace Owner** | The commercial authority and primary administrator of a workspace. Controls billing, subscription tiers, member quotas, workspace data export, and workspace deletion. |
| **Workspace Admin** | Operational manager within a workspace. Authorized to invite new members, modify roles (`Admin`, `Member`, `Viewer`), create/archive projects, and configure team settings. |
| **Workspace Member** | Core collaborative team user. Creates, edits, assigns, and transitions tasks; uploads attachments; posts comments; and manages personal profile settings. |
| **Workspace Viewer** | External client or auditor granted read-only visibility into projects, task lists, and comment feeds without modification or creation privileges. |

### 3.4 Constraints

At the time of baseline specification, the following operational and commercial constraints govern TinyTask:
- **Team & Scale Constraint:** The development and maintenance organization consists of 8 persons; product scope must remain lean, robust, and maintainable.
- **Commercial Constraint:** Core billing workflows must integrate with Stripe Checkout to delegate credit card handling to external providers.
- **Functional Neutrality:** This document establishes the pure functional capabilities required by the business; security, privacy, and regulatory controls will be formally overlaid in subsequent Phase 3 deliverables.

---

## 4. Part II — As-Is

### 4.1 Business Roles in Context

In the baseline As-Is operational context—typical of small organizations prior to adopting TinyTask—collaborators execute multiple overlapping roles without formal system boundaries:

- **Business Owner:** Manages commercial commitments informally, tracking project expenditures and customer subscriptions on local accounting spreadsheets.
- **Project Lead:** Spends 2 to 3 hours daily consolidating status updates from team members across email and chat, manually editing a shared spreadsheet.
- **Team Contributor:** Manages personal work queues in disparate desktop note applications; has no central visibility into team dependencies or changing priorities.
- **External Client:** Receives sporadic project updates via email attachments; has no direct window to review work in progress.

### 4.2 As-Is Workflow Processes & Information Fragmentation

#### 4.2.1 Gathering General Project Information
When a new project is initiated in the As-Is state, general parameters are established in an unstructured spreadsheet stored in a shared folder:

*Table 4 — Data Manually Inserted for New Project Creation (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| Project Name | Text | Yes | Duplication and inconsistent naming across departments. |
| Client / Entity Name | Text | Yes | Inconsistent spelling; no integration with customer registries. |
| Start Date | Date (`dd/mm/yyyy`) | Yes | Often left blank or estimated vaguely. |
| Target End Date | Date (`dd/mm/yyyy`) | Yes | No automated alert mechanisms as deadline approaches. |
| Responsible Project Lead | Text | Yes | Often reassigned informally without updating the document. |
| Allocated Budget (€) | Decimal Number | No | Rarely reconciled against real hours executed. |
| Initial Notes / Scope | Text Block | No | Overwritten constantly; version history lost. |

#### 4.2.2 Task Definition, Attribution, and Scheduling
Task definitions in the As-Is environment are recorded across separate spreadsheet tabs or personal notes:

*Table 5 — Data Manually Inserted for Task Definition & Scheduling (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| Task Title | Text | Yes | Vague statements lacking formal acceptance criteria. |
| Assignee Name | Text | No | Frequently unassigned, leading to dropped tasks. |
| Priority Level | Drop-down (`High`, `Med`, `Low`) | No | Rarely updated; lacks standardized rating criteria. |
| Target Deadline | Date (`dd/mm/yyyy`) | No | Deadlines passed without alerts or notifications. |
| Estimated Hours | Integer | No | Disconnected from actual execution logs. |
| Dependencies | Freeform Text | No | Broken dependency tracking; causes severe project bottlenecks. |

#### 4.2.3 Tracking Task Progress and Executed Time
Tracking task execution relies on manual self-reporting by collaborators:

*Table 6 — Data Manually Inserted for Task Status & Progress Tracking (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| Execution Status | Drop-down (`To-Do`, `In-Progress`, `Done`) | Yes | Frequently stale; relies entirely on manual user discipline. |
| Date of Last Update | Date (`dd/mm/yyyy`) | No | Rarely updated accurately; no timestamped audit. |
| Updated By | Text | No | No identity verification; anyone can mark a task complete. |
| Actual Hours Spent | Decimal Number | No | High reporting friction leads to missing time data. |
| Blocker / Impediment | Freeform Text | No | Blockers buried in cells; not highlighted to leadership. |

#### 4.2.4 Managing Attachments, Specifications, and Media
Files are managed across email attachments and unmanaged shared drives:

*Table 7 — Data Manually Inserted for Attachment & Document Sharing (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| File Name | Text | Yes | Versioning chaos (e.g., `spec_v2_final_FINAL.docx`). |
| Shared Drive URL | Text URL | Yes | Publicly accessible links without expiration or password. |
| File Category | Freeform Text | No | Disorganized directory structures; files lost. |
| Associated Task / Milestone | Freeform Text | No | Loose association; impossible to trace deliverable history. |
| Upload Date | Date (`dd/mm/yyyy`) | Yes | Manually recorded; no cryptographic hash or audit log. |

#### 4.2.5 Handling Commercial Subscriptions and Invoicing
Commercial client billing in the As-Is state is manually tracked in accounting spreadsheets:

*Table 8 — Data Manually Inserted for Client Subscriptions & Invoicing (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| Customer Organization Name | Text | Yes | Manual data entry across invoicing and project tools. |
| Plan Tier | Drop-down (`Free`, `Pro`, `Custom`) | Yes | Feature limits manually enforced by checking user counts. |
| Monthly Fee (€) | Decimal Number | Yes | Invoices generated manually; delayed revenue recognition. |
| Payment Status | Drop-down (`Paid`, `Pending`, `Overdue`) | Yes | Requires manual reconciliation against bank statements. |
| Subscription Renewal Date | Date (`dd/mm/yyyy`) | Yes | Missed renewals lead to unbilled service usage. |

#### 4.2.6 Handling Customer Data Export & Account Deletion Requests
Under the As-Is model, customer requests to export data or delete accounts are handled ad hoc:

*Table 9 — Data Manually Recorded for Account Data Requests (As-Is)*

| Data Field | Data Type | Mandatory | Observed Operational Deficiencies |
|---|---|---|---|
| Requester Full Name | Text | Yes | Requires manual identity verification via email. |
| Requester Email Address | Text | Yes | Dispersed across hundreds of spreadsheets and chat channels. |
| Request Type | Drop-down (`Data Export`, `Account Deletion`) | Yes | Manual data harvesting takes days of administrative time. |
| Request Received Date | Date (`dd/mm/yyyy`) | Yes | Risk of forgotten requests or delays. |
| Execution Status | Drop-down (`Pending`, `Completed`) | Yes | No automated confirmation receipt issued to user. |

### 4.3 Current IT Support & Operational Deficiencies

#### 4.3.1 Spreadsheet-Driven Tracking Limitations
Shared spreadsheets are fundamentally unsuitable for multi-user project coordination:
- Concurrent editing collisions result in lost updates.
- No granular permission controls: any user with write access can delete entire worksheets.
- Complete absence of an automated change history to verify who altered a task.

#### 4.3.2 Dispersed Email and Instant Messaging Chains
Using email and general instant messaging for task management causes severe information fragmentation:
- Decisions made in 1-on-1 chats are invisible to the wider team.
- Critical task assignments are buried under unrelated conversational chatter.
- Notifications cannot be scoped or prioritized, leading to notification fatigue.

#### 4.3.3 Unmanaged Cloud Storage Drives
File sharing via generic cloud storage links creates significant governance gaps:
- No linkage between an uploaded asset and the specific task context it fulfills.
- Direct public sharing links cannot be tracked or automatically revoked when projects conclude.

#### 4.3.4 Lack of Centralized Account and Data Lifecycle Controls
The As-Is state poses operational and administrative overhead:
- **No Data Isolation:** Customer organization data is commingled in shared folders without clear workspace boundaries.
- **Manual Export Burden:** Exporting all project records for a client requires tedious manual copying across multiple files.
- **Incomplete Account Closure:** When a collaborator leaves or requests account deletion, their name and references remain scattered across numerous spreadsheets and email chains.

---

## 5. Part III — To-Be

### 5.1 Initial Customer Expectations

The target "To-Be" state formalizes the requirements of stakeholders into a cohesive, centralized SaaS platform. The following table details the core initial customer expectations derived from business discovery:

*Table 10 — Customer Initial Expectations*

| Expectation ID | Initial Expectation | Description |
|---|---|---|
| **`EXP-01`** | **Centralize Work in Tenant Workspaces** | Consolidate all projects, tasks, discussions, and files into distinct organizational workspaces with role-based access. |
| **`EXP-02`** | **Visual & Intuitive Task Lifecycle** | Provide Kanban boards and list views with real-time drag-and-drop status transitions (`To-Do`, `In-Progress`, `Under-Review`, `Done`). |
| **`EXP-03`** | **Contextual In-Task Collaboration** | Embed Markdown discussions directly inside task cards with `@username` tagging and automated in-app notifications. |
| **`EXP-04`** | **Integrated Task Attachment Management** | Enable users to upload, preview, download, and delete task attachments directly within the task card. |
| **`EXP-05`** | **Automated Subscription & Billing Management** | Enable self-service plan upgrades/downgrades via secure payment gateway integration without handling cardholder data. |
| **`EXP-06`** | **Self-Service Account & Data Management** | Provide self-service personal data export and account closure workflows with automated confirmation receipts. |

### 5.2 System Actors

The following table formally specifies the actors interacting with the TinyTask platform:

*Table 11 — System Actors*

| Actor ID | Actor Name | Description |
|---|---|---|
| **`ACT-01`** | **Workspace Owner** | The commercial authority and primary administrator of a workspace. Controls billing, subscription tiers, member quotas, workspace data export, and workspace deletion. |
| **`ACT-02`** | **Workspace Admin** | Operational manager within a workspace. Authorized to invite new members, modify roles (`Admin`, `Member`, `Viewer`), create/archive projects, and configure team settings. |
| **`ACT-03`** | **Workspace Member** | Core collaborative team user. Creates, edits, assigns, and transitions tasks; uploads attachments; posts comments; and manages personal profile settings. |
| **`ACT-04`** | **Workspace Viewer** | External client or auditor granted read-only visibility into projects, task lists, and comment feeds without modification or creation privileges. |
| **`ACT-05`** | **External Payment Gateway** | External payment processing engine (Stripe) that interacts via secure HTTPS APIs and delivers signed asynchronous webhook notifications concerning subscription state changes. |
| **`ACT-06`** | **System Scheduler** | Internal background daemon executing periodic jobs, including daily email notification digests, token expiration sweeps, and retention cleanups. |

### 5.3 Functional Requirements (MoSCoW)

#### 5.3.1 MoSCoW Prioritization Technique
Below are described the functional requirements. For each requirement, a priority is assigned according to the MoSCoW technique:
- **Must:** Requirement that must be satisfied in the baseline release; mandatory for operational viability and core user workflows.
- **Should:** Requirement of high business value that should be considered; essential for a complete user experience where workarounds cause friction.
- **Could:** Desirable feature or enhancement that is useful, but not strictly required if schedule or resource constraints dictate omission.
- **Won't:** Requirement that may be considered in future releases, but is explicitly excluded from the current baseline release.

For each requirement, a formal specification card is established with the following properties:
- **ID & Name:** Unique identifier and standardized name of the requirement.
- **Description:** Clear operational description of the functional behavior.
- **Requirement Origin:** Business, stakeholder, or user need originating the requirement.
- **Interfaces:** Participating End Users and External Services.
- **Dependencies:** Stakeholders, Data Sources, Extraction Periodicity, and Preceding Requirements.
- **Identified Constraints / Restrictions:** Business rules, validation boundaries, and operational limitations.
- **Priority:** MoSCoW priority classification.

#### 5.3.2 Summary Table of Functional Requirements

*Table 12 — Summary Table of Functional Requirements (MoSCoW)*

| ID | ID | Requirement | Priority | Restrictions / Constraints |
|---|---|---|---|---|
| **`R1`** | | **User Account & Identity Governance** | **MUST** | Registration, login, password recovery, session review. |
| | `R1.1` | User registration with email address verification | MUST | Email address must be unique across the platform. |
| | `R1.2` | User credential authentication and session issuance | MUST | Standard login; returns active workspace list. |
| | `R1.3` | Password recovery workflow via email link | MUST | Single-use reset link sent to registered email. |
| | `R1.4` | Role-Based Access Control (Owner, Admin, Member, Viewer) | MUST | Roles scoped per workspace tenant. |
| | `R1.5` | User active session inspection and remote termination | SHOULD | User can review and log out remote sessions. |
| | `R1.6` | Multi-Factor Authentication (MFA / TOTP) support | COULD | Optional secondary verification code. |
| | `R1.7` | Enterprise Single Sign-On (SAML 2.0 / OIDC) federation | WON'T | Out of scope for micro-SaaS initial release. |
| **`R2`** | | **Workspace & Team Administration** | **MUST** | Multi-tenant workspace management and team roster. |
| | `R2.1` | Workspace creation assigning creator as Workspace Owner | MUST | Unique workspace name and URL slug. |
| | `R2.2` | Member invitation workflow via email | MUST | Capped by active plan tier member limit. |
| | `R2.3` | Member role modification and membership revocation | MUST | Admins cannot demote or remove Workspace Owner. |
| | `R2.4` | Workspace organization profile customization (name, logo) | SHOULD | Image logo up to 2 MB. |
| | `R2.5` | Workspace member activity and onboarding overview | COULD | Summarizes active contributor counts. |
| | `R2.6` | Custom fine-grained permission matrix editor | WON'T | Out of scope; restricted to canonical roles. |
| **`R3`** | | **Project Lifecycle & Containerization** | **MUST** | Project organization and privacy scoping. |
| | `R3.1` | Project creation with title, description, and privacy settings | MUST | Projects belong strictly to one workspace. |
| | `R3.2` | Project archiving into read-only state | SHOULD | Read-only mode preserving historical tasks. |
| **`R4`** | | **Task Authoring & Attribution** | **MUST** | Work item creation, assignment, and priority rating. |
| | `R4.1` | Task authoring with title, description, priority, assignee, due date | MUST | Title mandatory; defaults to `To-Do`. |
| | `R4.2` | Restrict task assignment to active workspace members | MUST | Cannot assign tasks to external emails. |
| | `R4.3` | Visual priority rating badges (Low, Medium, High, Urgent) | SHOULD | Default priority is `Medium`. |
| **`R5`** | | **Workflow Progression & Kanban Board Views** | **MUST** | Visual status progression and board view. |
| | `R5.1` | Status transitions between To-Do, In-Progress, Under-Review, Done | MUST | Records author and timestamp on every update. |
| | `R5.2` | Interactive Kanban board with drag-and-drop state update | MUST | Drag-and-drop card movement across columns. |
| | `R5.3` | Recurring task auto-cloning upon status completion | COULD | Clones task on daily, weekly, or monthly cycle. |
| **`R6`** | | **Multi-Dimensional Task Querying & Filtering** | **MUST** | Search and filter criteria across project boards. |
| | `R6.1` | Filter tasks by status, assignee, priority, and date range | MUST | Dynamic filtering without full-page reload. |
| | `R6.2` | Gantt chart timeline dependencies and critical path | WON'T | Out of scope for micro-SaaS initial release. |
| **`R7`** | | **Task Attachment Management** | **MUST** | Uploading and validating task attachments. |
| | `R7.1` | File attachment to active tasks with 25 MB size cap | MUST | Maximum file size of 25 MB per attachment. |
| | `R7.2` | Standard document and image format support | MUST | Supports common PDF, Office, and image types. |
| **`R8`** | | **Attachment Access & Removal** | **MUST** | Downloading and deleting task attachments. |
| | `R8.1` | Direct authorized attachment download | MUST | Accessible only to authorized workspace users. |
| | `R8.2` | Attachment deletion from task card | MUST | Uploader or Admin can delete attachment. |
| | `R8.3` | Inline image thumbnail preview on task card | COULD | Displays thumbnail preview inside task card. |
| **`R9`** | | **Collaborative In-Task Discussions** | **MUST** | Threaded commentary and team mentions. |
| | `R9.1` | Threaded Markdown comments on task detail cards | MUST | Blocked on archived projects. |
| | `R9.2` | User `@username` mentions dispatching notifications | MUST | Tagged users receive in-app notification. |
| | `R9.3` | Real-time WebSocket push for instant comment sync | COULD | Instant comment updates without reload. |
| **`R10`** | | **Activity History & Notification Alerts** | **MUST** | Audit history and alert center. |
| | `R10.1` | Chronological activity history logging on task card | MUST | Logs who made changes and timestamp. |
| | `R10.2` | In-app notification center for assignments and mentions | MUST | Badges and alerts for unread items. |
| | `R10.3` | Scheduled daily email summary digest | SHOULD | Consolidates pending tasks and mentions daily. |
| **`R11`** | | **Commercial Subscription Lifecycle** | **MUST** | Plan tier management via Stripe. |
| | `R11.1` | Plan tier upgrade checkout initiation via Stripe Checkout | MUST | Self-service tier upgrade (Free to Pro/Enterprise). |
| | `R11.2` | Webhook event processing for automated plan updates | MUST | Ingests Stripe payment events to update quota. |
| | `R11.3` | Automated tier quota reconciliation on payment success | MUST | Updates active workspace member seat limits. |
| | `R11.4` | Past-due grace period handling on payment failure | MUST | 7-day grace period before feature restriction. |
| **`R12`** | | **User Account & Data Lifecycle** | **MUST** | Data export and account closure workflows. |
| | `R12.1` | Self-service user data export (JSON format) | MUST | User can download copy of personal data. |
| | `R12.2` | Workspace-wide data archive export (ZIP archive) | MUST | Workspace Owner can export workspace data. |
| | `R12.3` | User account deletion and name anonymization | MUST | Closes account; replaces author name with `[Deleted User]`. |
| | `R12.4` | Account closure confirmation receipt | SHOULD | Generates digital receipt of account closure. |

#### 5.3.3 Detailed Specifications of Functional Requirements

The following tables present the formal specification cards for each functional requirement, mirroring the 7-row specification standard of GPTools Deliverable E1.1:

*Table 13 — Formal Specification Card: R1.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R1.1` **Name:** User Registration with Email Verification |
| **Description** | The system must allow new users to register an account by submitting an email address, full name, and password, dispatching an email verification link to confirm address ownership and activate the account. |
| **Requirement Origin** | User Onboarding & Identity Lifecycle Need |
| **Interfaces** | **End Users:** New User (Unauthenticated); **External Services:** Transactional Email Service |
| **Dependencies** | **Stakeholders:** Subscribing Organizations, Platform Founders; **Data Sources:** User Database; **Extraction Periodicity:** On demand; **Preceding Requirements:** None |
| **Identified Constraints** | Email address must be unique across the platform; registration link expires after 24 hours. |
| **Priority** | **MUST** |

*Table 14 — Formal Specification Card: R1.2*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R1.2` **Name:** User Credential Authentication & Session Issuance |
| **Description** | The system must authenticate registered users against their email and password credentials, generating an active session and returning the list of accessible workspace memberships. |
| **Requirement Origin** | Core User Access Need |
| **Interfaces** | **End Users:** Registered User; **External Services:** None |
| **Dependencies** | **Stakeholders:** All Users; **Data Sources:** User Database; **Extraction Periodicity:** On demand (login attempt); **Preceding Requirements:** `R1.1` |
| **Identified Constraints** | Clear error messages provided on failed login attempts; password must meet minimum length of 8 characters. |
| **Priority** | **MUST** |

*Table 15 — Formal Specification Card: R1.3*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R1.3` **Name:** Password Recovery Workflow |
| **Description** | The system must provide a self-service password recovery flow that dispatches a reset link to the user's registered email address, allowing the user to establish a new password and resume access. |
| **Requirement Origin** | User Account Support & Self-Service Need |
| **Interfaces** | **End Users:** Registered User; **External Services:** Transactional Email Service |
| **Dependencies** | **Stakeholders:** Subscribing Organizations, Individual Users; **Data Sources:** User Database; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R1.1` |
| **Identified Constraints** | Password reset links expire within 1 hour; existing login sessions terminated upon password update. |
| **Priority** | **MUST** |

*Table 16 — Formal Specification Card: R1.4*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R1.4` **Name:** Role-Based Access Control (RBAC) Enforcement |
| **Description** | The system must enforce Role-Based Access Control differentiating permissions among four predefined roles (`Owner`, `Admin`, `Member`, `Viewer`) scoped per workspace tenant. |
| **Requirement Origin** | Team Management & Organizational Governance |
| **Interfaces** | **End Users:** All Workspace Users; **External Services:** None |
| **Dependencies** | **Stakeholders:** Subscribing Organizations, Team Leads; **Data Sources:** Workspace Membership Table; **Extraction Periodicity:** Per request; **Preceding Requirements:** `R1.2` |
| **Identified Constraints** | User permissions are strictly evaluated within the context of the active workspace. |
| **Priority** | **MUST** |

*Table 17 — Formal Specification Card: R1.5*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R1.5` **Name:** Active Session Inspection & Remote Termination |
| **Description** | The system should enable users to inspect a list of their active login sessions (device type, approximate location, and last active timestamp) and log out any session remotely. |
| **Requirement Origin** | User Account Management Need |
| **Interfaces** | **End Users:** Registered User; **External Services:** None |
| **Dependencies** | **Stakeholders:** Individual Contributors; **Data Sources:** Session Store; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R1.2` |
| **Identified Constraints** | Terminated sessions must be immediately revoked across devices. |
| **Priority** | **SHOULD** |

*Table 18 — Formal Specification Card: R2.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R2.1` **Name:** Workspace Creation & Ownership Binding |
| **Description** | The system must permit an authenticated user to create a new workspace tenant with a custom name and unique URL slug, automatically designating the creator as the `Workspace Owner`. |
| **Requirement Origin** | Multi-Tenant Organization Setup Need |
| **Interfaces** | **End Users:** Authenticated User; **External Services:** None |
| **Dependencies** | **Stakeholders:** Subscribing Organization Owners; **Data Sources:** Workspace Database; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R1.2` |
| **Identified Constraints** | Workspace URL slugs must be alphanumeric and globally unique. |
| **Priority** | **MUST** |

*Table 19 — Formal Specification Card: R2.2*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R2.2` **Name:** Member Invitation Workflow |
| **Description** | The system must allow Workspace Owners and Admins to invite team members by email address with a designated role, verifying that the member count does not exceed active plan seat limits. |
| **Requirement Origin** | Team Onboarding & Workspace Administration |
| **Interfaces** | **End Users:** Workspace Owner, Workspace Admin; **External Services:** Transactional Email Service |
| **Dependencies** | **Stakeholders:** Team Leads, Subscribing Owners; **Data Sources:** Workspace Membership Table, Subscription Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R2.1` |
| **Identified Constraints** | Invitations must be blocked when the active member limit of the workspace's plan tier is reached. |
| **Priority** | **MUST** |

*Table 20 — Formal Specification Card: R2.3*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R2.3` **Name:** Member Role Modification & Access Revocation |
| **Description** | The system must allow Workspace Owners and Admins to modify member roles or remove members from the workspace, immediately revoking access to workspace projects while preserving historical task attribution. |
| **Requirement Origin** | Team Governance & Offboarding Need |
| **Interfaces** | **End Users:** Workspace Owner, Workspace Admin; **External Services:** None |
| **Dependencies** | **Stakeholders:** Subscribing Owners, Team Leads; **Data Sources:** Workspace Membership Table; **Extraction Periodicity:** Real-time; **Preceding Requirements:** `R2.2` |
| **Identified Constraints** | Admins cannot demote or remove the Workspace Owner. |
| **Priority** | **MUST** |

*Table 21 — Formal Specification Card: R3.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R3.1` **Name:** Project Container Creation & Configuration |
| **Description** | The system must allow Workspace Admins and Members to create projects within the workspace, specifying a project title, description, and privacy setting (visible to all members or restricted to selected users). |
| **Requirement Origin** | Project Organization Need |
| **Interfaces** | **End Users:** Workspace Admin, Workspace Member; **External Services:** None |
| **Dependencies** | **Stakeholders:** Team Leads, Project Coordinators; **Data Sources:** Project Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R2.1` |
| **Identified Constraints** | Projects belong strictly to one workspace and cannot be shared across workspace boundaries. |
| **Priority** | **MUST** |

*Table 22 — Formal Specification Card: R4.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R4.1` **Name:** Task Authoring & Attribution |
| **Description** | The system must permit workspace members to create tasks within a project, specifying task title, descriptive text, priority level, due date, and assigning responsibility to a workspace colleague. |
| **Requirement Origin** | Core Task Management Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin; **External Services:** None |
| **Dependencies** | **Stakeholders:** Individual Contributors, Team Leads; **Data Sources:** Task Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R3.1` |
| **Identified Constraints** | Task title is mandatory; initial status defaults to `To-Do`; assignees must be active workspace members. |
| **Priority** | **MUST** |

*Table 23 — Formal Specification Card: R5.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R5.1` **Name:** Task Workflow State Progression |
| **Description** | The system must allow authorized users to transition task status across standardized workflow states (`To-Do`, `In-Progress`, `Under-Review`, `Done`), recording the acting user and timestamp on every update. |
| **Requirement Origin** | Agile Task Execution Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin; **External Services:** None |
| **Dependencies** | **Stakeholders:** Team Leads, Individual Contributors; **Data Sources:** Task Table, Activity Log; **Extraction Periodicity:** Real-time; **Preceding Requirements:** `R4.1` |
| **Identified Constraints** | Status updates must execute reliably and reflect immediately in all active board views. |
| **Priority** | **MUST** |

*Table 24 — Formal Specification Card: R5.2*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R5.2` **Name:** Interactive Kanban Board Drag-and-Drop |
| **Description** | The system must provide an interactive Kanban board representation grouping tasks by status columns and updating status state values via client-side drag-and-drop interactions. |
| **Requirement Origin** | User Experience & Workflow Productivity Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin, Workspace Viewer; **External Services:** None |
| **Dependencies** | **Stakeholders:** Individual Contributors, Team Leads; **Data Sources:** Task Table; **Extraction Periodicity:** Real-time; **Preceding Requirements:** `R5.1` |
| **Identified Constraints** | Board updates must implement responsive user interface updates with reliable server synchronization. |
| **Priority** | **MUST** |

*Table 25 — Formal Specification Card: R6.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R6.1` **Name:** Multi-Dimensional Task Filtering & Search |
| **Description** | The system must provide real-time querying and filtering of tasks by status, assignee, priority rating, and due date range without requiring full application page reloads. |
| **Requirement Origin** | Daily Operational Efficiency Need |
| **Interfaces** | **End Users:** All Workspace Users; **External Services:** None |
| **Dependencies** | **Stakeholders:** All Users; **Data Sources:** Task Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R4.1` |
| **Identified Constraints** | Filtering must operate responsively across projects containing large numbers of tasks. |
| **Priority** | **MUST** |

*Table 26 — Formal Specification Card: R7.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R7.1` **Name:** Task File Attachment Ingestion |
| **Description** | The system must permit members to attach documents, spreadsheets, and image files to tasks, validating that individual file sizes do not exceed 25 MB per attachment. |
| **Requirement Origin** | Team Collaboration & Deliverable Sharing Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin; **External Services:** Cloud Object Storage |
| **Dependencies** | **Stakeholders:** Individual Contributors; **Data Sources:** Attachment Metadata Table, Storage Service; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R4.1` |
| **Identified Constraints** | Files exceeding the 25 MB limit must be rejected with an informative user error message. |
| **Priority** | **MUST** |

*Table 27 — Formal Specification Card: R8.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R8.1` **Name:** Authorized Task Attachment Retrieval |
| **Description** | The system must allow authorized workspace members to download or view file attachments associated with tasks to which they have project access. |
| **Requirement Origin** | Deliverable Review & Collaboration Need |
| **Interfaces** | **End Users:** All Workspace Users; **External Services:** Cloud Object Storage |
| **Dependencies** | **Stakeholders:** Subscribing Organizations, Team Leads; **Data Sources:** Attachment Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R7.1` |
| **Identified Constraints** | Users outside the containing workspace cannot access or download task attachments. |
| **Priority** | **MUST** |

*Table 28 — Formal Specification Card: R9.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R9.1` **Name:** Threaded Markdown Task Comments |
| **Description** | The system must provide threaded Markdown comment discussions on task detail panels, enabling team members to exchange feedback, specifications, and progress updates. |
| **Requirement Origin** | In-Context Team Communication Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin; **External Services:** None |
| **Dependencies** | **Stakeholders:** Individual Contributors, Team Leads; **Data Sources:** Comment Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R4.1` |
| **Identified Constraints** | Comments cannot be posted to archived projects; comments preserve author and creation timestamp. |
| **Priority** | **MUST** |

*Table 29 — Formal Specification Card: R9.2*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R9.2` **Name:** Collaborative `@username` Mentions |
| **Description** | The system must parse `@username` mentions within task comments, validating that tagged users belong to the workspace and generating targeted in-app notifications. |
| **Requirement Origin** | Team Notification & Asynchronous Coordination Need |
| **Interfaces** | **End Users:** Workspace Member, Workspace Admin; **External Services:** Notification Service |
| **Dependencies** | **Stakeholders:** Individual Contributors; **Data Sources:** Workspace Membership Table, Notification Table; **Extraction Periodicity:** Real-time on comment submit; **Preceding Requirements:** `R9.1` |
| **Identified Constraints** | Tagging non-members of the workspace must be safely ignored. |
| **Priority** | **MUST** |

*Table 30 — Formal Specification Card: R10.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R10.1` **Name:** Chronological Activity History Logging |
| **Description** | The system must record a chronological history log on each task card whenever a task is created, status-transitioned, reassigned, or commented upon, logging the user and timestamp. |
| **Requirement Origin** | Team Accountability & Progress Transparency Need |
| **Interfaces** | **End Users:** All Workspace Users; **External Services:** None |
| **Dependencies** | **Stakeholders:** Team Leads, Subscribing Owners; **Data Sources:** Task Activity Table; **Extraction Periodicity:** Real-time on state change; **Preceding Requirements:** `R4.1`, `R5.1` |
| **Identified Constraints** | Historical activity records must be displayed chronologically on the task card. |
| **Priority** | **MUST** |

*Table 31 — Formal Specification Card: R11.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R11.1` **Name:** Commercial Subscription Checkout via Stripe |
| **Description** | The system must enable the Workspace Owner to initiate plan upgrades (from Free to Pro/Enterprise) by creating a hosted Stripe Checkout session, redirecting the user securely without touching credit card details. |
| **Requirement Origin** | Commercial Operations & Revenue Model |
| **Interfaces** | **End Users:** Workspace Owner; **External Services:** Stripe Checkout API |
| **Dependencies** | **Stakeholders:** Platform Founders, Workspace Owners; **Data Sources:** Workspace Table, Stripe API; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R2.1` |
| **Identified Constraints** | Cardholder PAN and CVV numbers must never be received, transmitted, or stored on TinyTask servers. |
| **Priority** | **MUST** |

*Table 32 — Formal Specification Card: R11.2*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R11.2` **Name:** Webhook Subscription Event Processing |
| **Description** | The system must receive and process incoming payment gateway webhooks to update workspace subscription statuses, renewal dates, and payment failure states. |
| **Requirement Origin** | Automated Billing Reconciliation Need |
| **Interfaces** | **End Users:** External Payment Gateway (Stripe); **External Services:** Stripe Webhook Engine |
| **Dependencies** | **Stakeholders:** Platform Founders, Operations Team; **Data Sources:** Webhook Ingestion Service; **Extraction Periodicity:** Real-time on HTTP POST; **Preceding Requirements:** `R11.1` |
| **Identified Constraints** | System must verify webhook validity and update workspace active plan status atomically. |
| **Priority** | **MUST** |

*Table 33 — Formal Specification Card: R12.1*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R12.1` **Name:** Self-Service User Data Export |
| **Description** | The system must provide a self-service data export mechanism allowing authenticated users to request a structured JSON file containing their user profile, created tasks, and posted comments. |
| **Requirement Origin** | User Data Ownership & Portability Need |
| **Interfaces** | **End Users:** Registered User; **External Services:** Transactional Email Service |
| **Dependencies** | **Stakeholders:** Subscribing Organizations, Individual Users; **Data Sources:** Application Database; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R1.2` |
| **Identified Constraints** | Export file is generated asynchronously in the background and a download link delivered to user email. |
| **Priority** | **MUST** |

*Table 34 — Formal Specification Card: R12.3*

| Property | Value |
|---|---|
| **ID & Name** | **ID:** `R12.3` **Name:** User Account Deletion & Name Anonymization |
| **Description** | The system must permit users to delete their account, removing their personal login profile and anonymizing their display name across historical task comments and logs to `[Deleted User]`. |
| **Requirement Origin** | User Account Closure & Privacy Need |
| **Interfaces** | **End Users:** Registered User; **External Services:** None |
| **Dependencies** | **Stakeholders:** Individual Users, Workspace Owners; **Data Sources:** User Database, Task Table, Comment Table; **Extraction Periodicity:** On demand; **Preceding Requirements:** `R1.2` |
| **Identified Constraints** | User must confirm intent by re-entering password; shared team tasks remain intact with author anonymized. |
| **Priority** | **MUST** |

### 5.4 Non-Functional Requirements

#### 5.4.1 Domain Non-Functional Requirements
Domain non-functional requirements define the quality attributes governing user experience, performance, and reliability:

*Table 35 — Domain Non-Functional Requirements*

| ID | Requirement | Priority | Type |
|---|---|---|---|
| **`RN1`** | The web application user interface must achieve a First Contentful Paint (FCP) under 1.5 seconds and sub-200 ms interactive response times for drag-and-drop board state updates under standard broadband connections. | **MUST** | Desempenho / Performance |
| **`RN2`** | The platform must be fully responsive, accessible, and functional across modern desktop and mobile browsers (Chromium, Firefox, Safari) without requiring proprietary browser plugins. | **MUST** | Usabilidade / Portabilidade |
| **`RN3`** | The Kanban board engine must support rendering and manipulating up to 1,000 active tasks per project without degrading client-side scrolling or dragging frame rates (minimum 50 fps). | **SHOULD** | Escalabilidade / Scalability |
| **`RN4`** | The production SaaS infrastructure must target a minimum operational service availability of 99.5% uptime during standard business hours (08:00 - 20:00 CET), excluding announced maintenance. | **MUST** | Fiabilidade / Reliability |

#### 5.4.2 Operational & Infrastructure Non-Functional Requirements
Operational and infrastructure non-functional requirements define multi-tenancy, data backup, and hosting capabilities:

*Table 36 — Operational & Infrastructure Non-Functional Requirements*

| ID | Requirement | Priority | Type |
|---|---|---|---|
| **`RN5`** | Multi-tenant data segregation must ensure that every database query in a workspace context returns only records belonging to that workspace tenant. | **MUST** | Arquitetura / Multi-Tenancy |
| **`RN6`** | Database backups must be executed automatically on a daily schedule, enabling point-in-time recovery in case of operational hardware failure or service outage. | **MUST** | Gestão & Infraestrutura / Backups |
| **`RN7`** | The web application must provide a consistent visual design system and predictable navigation menus across all workspace modules. | **MUST** | Usabilidade / Design System |

### 5.5 Business Use Cases & Product Use Cases (PUC)

The following table synthesizes the complete **Product Use Cases (PUC)** bridging the As-Is operational deficiencies into the To-Be system capabilities:

*Table 37 — Product Use Case (PUC) Summary Table*

| PUC | Nome do PUC | Atores/Utilizadores | Input e Output |
|---|---|---|---|
| **1.1** | Registar Conta de Utilizador | Novo Utilizador | (in) Nome completo, email, palavra-passe. (out) Email de verificação enviado; conta pendente registada. |
| **1.2** | Autenticar no Sistema | Utilizador Registado | (in) Email e palavra-passe. (out) Sessão iniciada; lista de workspaces autorizados. |
| **1.3** | Recuperar Palavra-passe | Utilizador Registado | (in) Email da conta; nova palavra-passe. (out) Confirmação de reset; acesso restabelecido. |
| **1.4** | Inspecionar e Terminar Sessões | Utilizador Autenticado | (in) Comando de consulta/terminação de sessão. (out) Lista de sessões ativas; confirmação de revogação. |
| **2.1** | Criar Workspace | Utilizador Autenticado | (in) Nome da organização, slug URL único. (out) Workspace provisionado; utilizador como Workspace Owner. |
| **2.2** | Convidar Membros para Workspace | Workspace Owner / Admin | (in) Email do convidado, perfil atribuído (Admin/Member/Viewer). (out) Convite enviado por email; membro pendente registado. |
| **2.3** | Gerir Perfis e Membros | Workspace Owner / Admin | (in) ID do membro, novo perfil ou ordem de remoção. (out) Perfil atualizado; membro removido do workspace. |
| **2.4** | Consultar Quotas do Workspace | Workspace Owner / Admin | (in) Consulta às definições do workspace. (out) Utilização de membros (vagas vs limite do plano), espaço em disco gasto. |
| **3.1** | Criar e Gerir Projetos | Workspace Admin / Member | (in) Nome do projeto, descrição, privacidade (público/privado). (out) Contentor de projeto criado/atualizado; lista de projetos. |
| **3.2** | Criar e Atribuir Tarefas | Workspace Member / Admin | (in) Título da tarefa, descrição, prioridade, responsável, data de fim. (out) Tarefa criada; notificação enviada ao responsável. |
| **3.3** | Atualizar Estado da Tarefa | Workspace Member / Admin | (in) ID da tarefa, novo estado (To-Do, In-Progress, Review, Done). (out) Estado atualizado no Kanban; registo de histórico. |
| **3.4** | Filtrar e Pesquisar Tarefas | Utilizador do Workspace | (in) Parâmetros de filtro (estado, responsável, prioridade, data). (out) Vista filtrada de tarefas no ecrã sem recarregamento. |
| **4.1** | Carregar Anexo para Tarefa | Workspace Member / Admin | (in) ID da tarefa, ficheiro binário, nome. (out) Ficheiro carregado e associado à tarefa. |
| **4.2** | Descarregar Anexo | Utilizador do Workspace | (in) ID do anexo, ID da tarefa. (out) Ficheiro descarregado para o dispositivo do utilizador. |
| **4.3** | Eliminar Anexo | Workspace Member / Admin | (in) ID do anexo, confirmação de eliminação. (out) Anexo removido da tarefa e do armazenamento. |
| **5.1** | Comentar Tarefa com Menções | Workspace Member / Admin | (in) ID da tarefa, texto em Markdown, menção `@username`. (out) Comentário anexado à tarefa; notificação enviada ao utilizador mencionado. |
| **5.2** | Consultar Feed de Atividades | Utilizador do Workspace | (in) ID do workspace ou projeto. (out) Feed cronológico com as alterações efetuadas na equipa. |
| **5.3** | Enviar Digest Diário por Email | System Scheduler | (in) Execução agendada (08:00 UTC), notificações por ler. (out) Email resumo consolidado enviado aos utilizadores subscritos. |
| **6.1** | Iniciar Atualização de Plano | Workspace Owner | (in) Seleção de plano (Pro, Enterprise), ciclo de faturação. (out) Redirecionamento seguro para sessão no Stripe Checkout. |
| **6.2** | Processar Webhooks de Pagamento | Gateway de Pagamento | (in) Notificação de pagamento confirmado do Stripe. (out) Quota de vagas e estado do workspace atualizados. |
| **6.3** | Exportar Dados Pessoais | Utilizador Registado | (in) Pedido de exportação de dados da conta. (out) Ficheiro JSON gerado com todos os dados pessoais do utilizador. |
| **6.4** | Eliminar Conta e Dados | Utilizador Registado | (in) Pedido de eliminação de conta, password confirmada. (out) Conta eliminada; nome anonimizado no histórico de tarefas. |

### 5.6 System Use Case Model ({U.C.1} to {U.C.6})

The macro-architecture of the system is organized into 6 High-Level System Use Cases:

```mermaid
flowchart LR
    subgraph Atores ["Atores do Sistema"]
        Owner["Workspace Owner<br>(ACT-01)"]
        Admin["Workspace Admin<br>(ACT-02)"]
        Member["Workspace Member<br>(ACT-03)"]
        Viewer["Workspace Viewer<br>(ACT-04)"]
        Stripe["External Payment Gateway<br>(ACT-05)"]
        Scheduler["System Scheduler<br>(ACT-06)"]
    end

    subgraph TinyTask_System ["TinyTask SaaS — Nível 0"]
        UC1["{U.C.1}<br>Autenticar e Gerir Contas de Utilizador"]
        UC2["{U.C.2}<br>Configurar e Administrar Workspaces"]
        UC3["{U.C.3}<br>Gerir Projetos e Tarefas"]
        UC4["{U.C.4}<br>Gerir Anexos e Media"]
        UC5["{U.C.5}<br>Gerir Colaboração e Notificações"]
        UC6["{U.C.6}<br>Gerir Subscrições e Ciclo de Vida da Conta"]
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

#### 5.6.1 {U.C.1} — Authenticate and Manage User Accounts
Provides user registration, credential authentication, password recovery, and tenant membership access. Detailed into sub-cases `{U.C.1.1}` (User Registration), `{U.C.1.2}` (Authentication & Sessions), `{U.C.1.3}` (Password Recovery), and `{U.C.1.4}` (Session Review & RBAC).

#### 5.6.2 {U.C.2} — Configure and Administrate Workspaces
Governs multi-tenant workspace creation, member invitation workflows, role administration, and quota monitoring. Detailed into sub-cases `{U.C.2.1}` (Workspace Creation), `{U.C.2.2}` (Member Invitations), `{U.C.2.3}` (Role Administration & Removal), and `{U.C.2.4}` (Quota & Settings Inspection).

#### 5.6.3 {U.C.3} — Manage Projects and Tasks Lifecycle
Provides project containerization, task authoring, assignment, priority tagging, due date tracking, and workflow state progression across Kanban and list representations. Detailed into sub-cases `{U.C.3.1}` (Project Containers), `{U.C.3.2}` (Task Authoring), `{U.C.3.3}` (Workflow & Kanban State Updates), and `{U.C.3.4}` (Task Filtering & Search).

#### 5.6.4 {U.C.4} — Ingest and Manage Attachments and Media
Provides ingestion, storage, retrieval, and deletion of files and media assets associated with tasks. Detailed into sub-cases `{U.C.4.1}` (File Upload), `{U.C.4.2}` (File Download & Preview), and `{U.C.4.3}` (Attachment Deletion).

#### 5.6.5 {U.C.5} — Manage Team Collaboration and Notification Alerts
Enables communication among team members through Markdown task comments, user `@mentions`, activity history tracking, and scheduled email summary notifications. Detailed into sub-cases `{U.C.5.1}` (Task Comments & Mentions), `{U.C.5.2}` (Activity Stream & In-App Alerts), and `{U.C.5.3}` (Scheduled Email Digest).

#### 5.6.6 {U.C.6} — Manage Commercial Subscriptions and Account Lifecycle
Encompasses the commercial subscription lifecycle (plan checkout, tier upgrades, Stripe webhook processing) alongside self-service data export and account deletion workflows. Detailed into sub-cases `{U.C.6.1}` (Stripe Plan Checkout), `{U.C.6.2}` (Webhook Subscription Reconciliation), `{U.C.6.3}` (User Data Export), and `{U.C.6.4}` (Account Deletion & Name Anonymization).

---

## 6. Conclusions

This deliverable establishes the **pure functional baseline** for TinyTask SaaS, strictly reflecting business workflows and user capabilities without pre-baking security engineering solutions. By contrasting the manual, fragmented As-Is baseline against the structured To-Be capabilities, the specification provides unambiguous functional requirements, explicit actor boundaries, prioritized MoSCoW rankings, and a clear mapping to downstream Level-0 and Level-1 System Use Cases (`Doc02_System_Use_Cases.md`).

This functional foundation constitutes the exact incoming operational baseline to be consumed by AEGIS Phase 3, where security and privacy requirements will be formally derived and overlaid using the AEGIS autonomous skills suite and Phase 2 Operational Objectives.

---

## 7. Bibliography

1. Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
2. Centro de Computação Gráfica (CCG) & PIEP. (2023). *E1.1 – GPTools_ModeloASIS_TOBE V2.0: Relatório de Análise de Requisitos e Modelo As-Is / To-Be*. Guimarães, Portugal.
3. Centro de Computação Gráfica (CCG) & PIEP. (2023). *E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0: Especificação de Casos de Uso e Decomposição Funcional*. Guimarães, Portugal.
