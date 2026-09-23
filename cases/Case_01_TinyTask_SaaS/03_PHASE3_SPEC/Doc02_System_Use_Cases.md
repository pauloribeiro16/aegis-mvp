# E1.2 – TinyTask SaaS: Requirements Analysis and System Use Cases

## Executive Summary

This report establishes the formal system use case specification for the **TinyTask SaaS** platform, complementing the AS-IS / TO-BE model (*Doc01*) and formalizing the functional interactions between human actors, external services, and core system capabilities.

The methodological framework follows the Volere approach and triangular functional decomposition. In strict accordance with the project guidelines, system use cases are refined to **Level 1** (`{U.C.n.m}`), omitting step-by-step procedural execution sequences and leaf-node decomposition (`{U.C.n.m.k}`).

The specifications here represent pure functional business capabilities. Security and privacy overlays will be formally derived in subsequent Phase 3 deliverables using AEGIS Phase 2 Operational Objectives and automated auditing skills.

---

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. System Requirements Approach](#2-system-requirements-approach)
  - [2.1 Volere Approach and Triangular Functional Decomposition](#21-volere-approach-and-triangular-functional-decomposition)
  - [2.2 Refinement Boundary (No Leaf Nodes)](#22-refinement-boundary-no-leaf-nodes)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. Requirements Analysis](#3-requirements-analysis)
  - [3.1 Work Context Model](#31-work-context-model)
  - [3.2 Summary Table of Product Use Cases (PUC)](#32-summary-table-of-product-use-cases-puc)
- [4. Domain Application Use Cases](#4-domain-application-use-cases)
  - [4.1 System Actors](#41-system-actors)
  - [4.2 System Use Cases](#42-system-use-cases)
    - [4.2.1 Use Case 1 – Authenticate into the System](#421-use-case-1--authenticate-into-the-system)
    - [4.2.2 Use Case 2 – Manage Workspaces and Teams](#422-use-case-2--manage-workspaces-and-teams)
    - [4.2.3 Use Case 3 – Manage Projects](#423-use-case-3--manage-projects)
    - [4.2.4 Use Case 4 – Manage and Execute Tasks](#424-use-case-4--manage-and-execute-tasks)
    - [4.2.5 Use Case 5 – Manage Task Attachments](#425-use-case-5--manage-task-attachments)
    - [4.2.6 Use Case 6 – Collaborate and Notify](#426-use-case-6--collaborate-and-notify)
    - [4.2.7 Use Case 7 – Manage Commercial Subscriptions](#427-use-case-7--manage-commercial-subscriptions)
    - [4.2.8 Use Case 8 – Manage User Data and Close Accounts](#428-use-case-8--manage-user-data-and-close-accounts)
- [5. Non-Functional Requirements](#5-non-functional-requirements)
- [6. Conclusions](#6-conclusions)
- [7. Bibliography](#7-bibliography)
- [Version History](#version-history)

---

## 1. Introduction

The **TinyTask SaaS** platform delivers a lean, agile, and intuitive workspace for distributed teams to coordinate projects, manage tasks, and track deadlines.

This document formalizes the functional architecture of TinyTask, specifying the work context model, system actors, and Level-1 system use cases corresponding to the functional requirements defined in *Doc01*.

---

## 2. System Requirements Approach

### 2.1 Volere Approach and Triangular Functional Decomposition

The specification adheres to established software engineering principles:
1. **Product Boundary Definition:** Rigorous identification of incoming inputs (`in`) and outgoing deliverables (`out`) via Product Use Cases (*PUC*).
2. **Triangular Functional Decomposition:** Hierarchical refinement from Level-0 macro capabilities down to Level-1 system use cases, maintaining direct traceability to MoSCoW-prioritized requirements.

### 2.2 Refinement Boundary (No Leaf Nodes)

In strict accordance with Rule R13 and the project guidelines:
- **Refinement Boundary:** Use cases are specified up to **Level 1** (`{U.C.n.m}`).
- **Omission of Leaf Nodes:** The specification **does not decompose** into sub-sub-cases (`{U.C.n.m.k}`) and **does not define** step-by-step procedural execution sequences (Step 1, Step 2, etc.).
- **Pure Functionality:** Descriptions focus exclusively on user-facing business capabilities, free from premature technology lock-in or pre-baked security controls.

### 2.3 Non-Functional Requirements

Non-functional requirements frame system efficiency, reliability, availability, and usability targets to ensure robust operational execution.

---

## 3. Requirements Analysis

### 3.1 Work Context Model

The work context diagram delineates interactions between the TinyTask core system, human actors, and external services:

```mermaid
flowchart TD
    subgraph Human_Actors["Human Actors"]
        UA["Unauthenticated User"]
        WM["Workspace Member"]
        WA["Workspace Admin"]
        WO["Workspace Owner"]
        WV["Workspace Viewer"]
    end

    subgraph TinyTask_Platform["TinyTask SaaS Core"]
        Core["Core Platform Services & Database"]
    end

    subgraph External_Services["External Services"]
        PayGateway["External Payment Gateway"]
        MailService["Transactional Email Service"]
    end

    UA -- "Registration & Login Requests" --> Core
    WM -- "Create Tasks, Comments & Attachments" --> Core
    WA -- "Manage Members & Projects" --> Core
    WO -- "Manage Subscriptions & Billing" --> Core
    WV -- "Read-Only Inspection" --> Core

    Core -- "Dispatch Notifications & Verification" --> MailService
    Core <--> "Checkout Sessions & Webhooks" --> PayGateway
```

### 3.2 Summary Table of Product Use Cases (PUC)

The following table maps Product Use Cases to participating actors, inputs, and outputs:

*Table 1. Summary table of Product Use Cases (PUC)*

| PUC | PUC Name | Actors / Users | Input and Output |
|---|---|---|---|
| **1.1** | Register and Activate User Account | Unauthenticated User, Notification / Email Service | **(in)** Full name, email, password<br>**(out)** Verification email with activation link |
| **1.2** | Authenticate User and Issue Session | Registered User | **(in)** Email and password credentials<br>**(out)** Active session and authorized workspace list |
| **1.3** | Recover User Password via Reset Link | Registered User, Notification / Email Service | **(in)** User registered email address<br>**(out)** Password reset email with secure token |
| **2.1** | Create Organization Workspace | Workspace Owner | **(in)** Workspace name and URL slug<br>**(out)** Instantiated workspace with creator as Owner |
| **2.2** | Invite and Manage Workspace Members | Workspace Admin, Workspace Owner, Notification / Email Service | **(in)** Invitee email and assigned role (Admin, Member, Viewer)<br>**(out)** Invitation email and member added to roster |
| **2.3** | Configure Workspace Profile Settings | Workspace Admin, Workspace Owner | **(in)** Updated workspace name and logo image (up to 2 MB)<br>**(out)** Updated workspace branding across client views |
| **3.1** | Create and Configure New Project | Workspace Admin, Workspace Member | **(in)** Project title, scope description, visibility setting<br>**(out)** Initialized project accessible in navigation menu |
| **3.2** | Archive Completed Project | Workspace Admin, Workspace Owner | **(in)** Selection of target project to archive<br>**(out)** Read-only project hidden from operational views |
| **4.1** | Create and Assign Project Task | Workspace Member, Workspace Admin | **(in)** Title, description, priority, due date, assignee<br>**(out)** New task card in "To-Do" and assignee notification |
| **4.2** | Update Task State on Kanban Board | Workspace Member, Workspace Admin | **(in)** Drag card to target column (In-Progress, Under-Review, Done)<br>**(out)** Updated task status and audit history event |
| **4.3** | Search and Filter Tasks | All Users | **(in)** Search terms and filter criteria (assignee, priority, status)<br>**(out)** Filtered board and table views updated in real-time |
| **5.1** | Attach Deliverable File to Task Card | Workspace Member, Workspace Admin | **(in)** File selection (up to 25 MB size cap)<br>**(out)** Uploaded file linked to task attachment gallery |
| **5.2** | Download and Delete Task Attachment | Workspace Member, Workspace Admin | **(in)** Download or delete command for specified file<br>**(out)** File transferred to client or purged from attachment gallery |
| **6.1** | Post Comment and Mention Collaborator | Workspace Member, Workspace Admin | **(in)** Markdown comment text with user mentions (@user)<br>**(out)** Comment posted and notifications delivered to tagged users |
| **6.2** | Consult In-App Notification Center | Authenticated User | **(in)** Access user notification drawer<br>**(out)** Chronological list of unread mentions and task assignments |
| **7.1** | Subscribe and Upgrade Commercial Plan | Workspace Owner, External Payment Gateway | **(in)** Selected plan tier (Pro/Enterprise) and billing info<br>**(out)** Payment confirmation and updated workspace quotas |
| **7.2** | Process Billing Webhook and Reconcile Quotas | External Payment Gateway, Platform Core | **(in)** Asynchronous webhook notification with payment event<br>**(out)** Reconciled plan tier and member quotas in database |
| **8.1** | Export Personal and Workspace Data | Authenticated User, Workspace Owner | **(in)** Data export request (personal format or workspace archive)<br>**(out)** Downloadable archive package generated for client |
| **8.2** | Deactivate and Close User Account | Authenticated User, Notification / Email Service | **(in)** Autonomous account deletion confirmation<br>**(out)** Credentials purged, name anonymized, receipt dispatched |

---

## 4. Domain Application Use Cases

### 4.1 System Actors

The platform defines the following actors:
- **Workspace Owner:** Commercial and organizational authority. Manages billing, plans, and workspace deletion.
- **Workspace Admin:** Operational team manager. Configures settings, manages members, and creates projects.
- **Workspace Member:** Active contributor. Creates and edits tasks, posts comments, and uploads attachments.
- **Workspace Viewer:** Guest user granted read-only visibility into projects and task boards.
- **External Payment Gateway:** External service processing payments and dispatching webhook notices.
- **Notification / Email Service:** External service dispatching verification emails and task alerts.

### 4.2 System Use Cases

#### 4.2.1 Use Case 1 – Authenticate into the System

Encompasses user entry into the platform, credential verification, and account recovery:

- **{U.C. 1.1} Register New Account:** An unauthenticated visitor submits registration details (name, email, and password). The system verifies email uniqueness and dispatches an activation link.
- **{U.C. 1.2} Authenticate User Credentials:** The user submits email and password credentials. The system verifies credentials, generates an active session, and returns accessible workspaces.
- **{U.C. 1.3} Recover Account Credentials:** A user requests password recovery, prompting the system to validate the account and dispatch a time-limited reset link.

#### 4.2.2 Use Case 2 – Manage Workspaces and Teams

Governs workspace organizational setup and member roster administration:

- **{U.C. 2.1} Create Workspace:** Any registered user instantiates a new workspace, automatically becoming the Workspace Owner.
- **{U.C. 2.2} Invite and Manage Members:** Administrators send email invitations and assign member roles (Admin, Member, Viewer), respecting plan seat limits.
- **{U.C. 2.3} Configure Workspace Profile:** Administrators update the workspace display name and upload organization logos (image up to 2 MB).

#### 4.2.3 Use Case 3 – Manage Projects

Organizes projects and work streams within the workspace:

- **{U.C. 3.1} Create and Configure Project:** Administrators or members create new projects, configuring name, scope description, and visibility permissions.
- **{U.C. 3.2} Archive Project:** Moves a completed project into historical archive status, rendering tasks read-only.

#### 4.2.4 Use Case 4 – Manage and Execute Tasks

Represents the core operational engine of the platform:

- **{U.C. 4.1} Create and Assign Task:** Users record tasks with mandatory titles, descriptions, due dates, priority ratings, and member attributions.
- **{U.C. 4.2} Transition Task States on Kanban Board:** Users drag and drop task cards across columns ("To-Do", "In-Progress", "Under-Review", "Done") to update status.
- **{U.C. 4.3} Search and Filter Tasks:** Users search tasks and filter views dynamically by assignee, status, and priority.

#### 4.2.5 Use Case 5 – Manage Task Attachments

Governs deliverable documentation linked to task cards:

- **{U.C. 5.1} Upload Task Attachment:** Users attach documents, spreadsheets, or images (up to 25 MB) directly to task cards.
- **{U.C. 5.2} Download and Remove Attachment:** Users download deliverable files and allow uploaders or admins to delete attachments.

#### 4.2.6 Use Case 6 – Collaborate and Notify

Manages team discussions, alerts, and mentions:

- **{U.C. 6.1} Post Comments and Mention Collaborators:** Users exchange contextual messages in Markdown within task cards, tagging colleagues via "@user".
- **{U.C. 6.2} Consult Notification Center:** Displays in-app unread alerts and sends automated daily summary digests via email.

#### 4.2.7 Use Case 7 – Manage Commercial Subscriptions

Governs commercial billing and plan tier lifecycle:

- **{U.C. 7.1} Subscribe and Upgrade Plan:** Workspace Owners select paid plans and initiate checkout via external payment gateway.
- **{U.C. 7.2} Process Billing Webhooks and Reconcile Quotas:** Ingests asynchronous payment events from payment gateway to update workspace quotas automatically.

#### 4.2.8 Use Case 8 – Manage User Data and Close Accounts

Ensures user autonomy, data portability, and account closure:

- **{U.C. 8.1} Export Personal and Workspace Data:** Users generate personal structured data archives, and Workspace Owners download complete workspace packages.
- **{U.C. 8.2} Deactivate and Close Account:** Users autonomously close accounts, invalidating credentials, anonymizing names, and receiving confirmation receipts.

---

## 5. Non-Functional Requirements

As defined in *Doc01*, the platform satisfies the following non-functional criteria:
- **Performance (RN1):** Board load time under 500 ms for up to 200 tasks.
- **Availability (RN2):** Minimum 99.5% service availability.
- **Usability (RN3):** Fully responsive layout for viewports from 375 px upwards.
- **Scalability (RN4):** Capacity for 50,000 active tasks per workspace without performance loss.
- **Recoverability (RN5):** Daily automated backups with RPO under 24 hours.
- **Internationalization (RN6):** Full interface localization in English and Portuguese.
- **Interoperability (RN7):** Secure payment gateway integration with cryptographic signature validation.
- **Multi-Tenancy (RN8):** Complete logical data isolation across workspaces.

---

## 6. Conclusions

This specification formalizes the functional requirements and system use cases for the **TinyTask SaaS** platform, providing a robust, unambiguous, and purely functional baseline.

With this specification locked, the system's functional boundary is completely defined, enabling the downstream synthesis of AEGIS Phase 3 Security and Privacy Requirements.

---

## Bibliography

1. Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley Professional.
2. Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
3. Fowler, M. (2003). *UML Distilled: A Brief Guide to the Standard Object Modeling Language* (3rd ed.). Addison-Wesley Professional.

---

## Version History

| Version | Date | Author | Modification Notes |
|---|---|---|---|
| **1.0.0** | 2026-09-23 | AEGIS Technical Team | Initial baseline release of System Use Cases specification (Doc02) matching GPTools E1.2 deliverable standard, Level-1 refinement without leaf nodes, and active action verb phrasing. |
