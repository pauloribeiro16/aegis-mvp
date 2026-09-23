# E1.2 – TinyTask SaaS: System Use Cases

## Executive Summary

This deliverable establishes the formal **System Use Cases** for the **TinyTask SaaS** platform, translating the operational requirements and Product Use Cases (*PUC*) elicited in `Doc01` into rigorous, literature-grounded behavioral specifications and visual UML Use Case models. Grounded in foundational requirements engineering literature—specifically Alistair Cockburn's *Writing Effective Use Cases*, Craig Larman's *Applying UML and Patterns*, the OMG UML 2.5 standard, and the GPTools specification standard (`E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0`)—this document specifies each elementary user goal at **Level 1 ("Sea Level")**.

To provide complete operational clarity, each macro capability cluster is modeled with a robust, error-free **UML Use Case Diagram** rendered natively in Markdown via Mermaid, and every individual Level-1 use case is formalized with a **Fully Dressed Specification Card** detailing primary and supporting actors, stakeholders and interests, preconditions, triggers, black-box main success scenarios, branching extensions and alternative flows, success guarantees, and minimal guarantees. The resulting specification maintains strict technology neutrality, providing a verified functional baseline that directly supports downstream AEGIS Phase 3 security and privacy synthesis.

---

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. System Requirements Approach & Literature Foundations](#2-system-requirements-approach--literature-foundations)
  - [2.1 The Volere Triangular Decomposition: Business Events to System Use Cases](#21-the-volere-triangular-decomposition-business-events-to-system-use-cases)
  - [2.2 Use Case Architecture (Cockburn, Larman, Wiegers)](#22-use-case-architecture-cockburn-larman-wiegers)
  - [2.3 Visual UML Use Case Modeling in Markdown](#23-visual-uml-use-case-modeling-in-markdown)
  - [2.4 Anatomy of a Literature-Grounded Use Case](#24-anatomy-of-a-literature-grounded-use-case)
  - [2.5 Refinement Boundary: Cockburn's Sea Level (Level 1) vs. Micro-UI Anti-Patterns](#25-refinement-boundary-cockburns-sea-level-level-1-vs-micro-ui-anti-patterns)
- [3. Requirements Analysis](#3-requirements-analysis)
  - [3.1 Work Context Model](#31-work-context-model)
  - [3.2 Traceability Matrix: Requirements (Doc01) to System Use Cases (Doc02)](#32-traceability-matrix-requirements-doc01-to-system-use-cases-doc02)
- [4. Domain Application Use Cases](#4-domain-application-use-cases)
  - [4.1 System Actors](#41-system-actors)
  - [4.2 System Use Cases Specification](#42-system-use-cases-specification)
    - [{U.C. 1} Manage User Accounts and Authentication](#uc-1-manage-user-accounts-and-authentication)
      - [{U.C. 1.1} Register and authenticate user accounts](#uc-11-register-and-authenticate-user-accounts)
      - [{U.C. 1.2} Manage user profile and account preferences](#uc-12-manage-user-profile-and-account-preferences)
    - [{U.C. 2} Manage Workspaces and Teams](#uc-2-manage-workspaces-and-teams)
      - [{U.C. 2.1} Create and configure workspace](#uc-21-create-and-configure-workspace)
      - [{U.C. 2.2} Invite workspace members and manage access roles](#uc-22-invite-workspace-members-and-manage-access-roles)
      - [{U.C. 2.3} Monitor workspace activity and operational metrics](#uc-23-monitor-workspace-activity-and-operational-metrics)
    - [{U.C. 3} Manage Projects](#uc-3-manage-projects)
      - [{U.C. 3.1} Create and configure projects](#uc-31-create-and-configure-projects)
      - [{U.C. 3.2} Archive completed projects](#uc-32-archive-completed-projects)
    - [{U.C. 4} Manage and Execute Tasks](#uc-4-manage-and-execute-tasks)
      - [{U.C. 4.1} Create and assign tasks](#uc-41-create-and-assign-tasks)
      - [{U.C. 4.2} Track and transition task workflow states on visual boards](#uc-42-track-and-transition-task-workflow-states-on-visual-boards)
      - [{U.C. 4.3} Configure recurring automated tasks](#uc-43-configure-recurring-automated-tasks)
    - [{U.C. 5} Collaborate on Task Deliverables](#uc-5-collaborate-on-task-deliverables)
      - [{U.C. 5.1} Manage task deliverable attachments](#uc-51-manage-task-deliverable-attachments)
      - [{U.C. 5.2} Post in-task discussion comments and mention collaborators](#uc-52-post-in-task-discussion-comments-and-mention-collaborators)
    - [{U.C. 6} Track Activity History and Notifications](#uc-6-track-activity-history-and-notifications)
      - [{U.C. 6.1} Consult chronological audit history on task cards](#uc-61-consult-chronological-audit-history-on-task-cards)
      - [{U.C. 6.2} Receive workspace alerts and daily task digests](#uc-62-receive-workspace-alerts-and-daily-task-digests)
    - [{U.C. 7} Manage Commercial Subscriptions](#uc-7-manage-commercial-subscriptions)
      - [{U.C. 7.1} Subscribe and manage workspace commercial plans](#uc-71-subscribe-and-manage-workspace-commercial-plans)
      - [{U.C. 7.2} Enforce operational grace period upon payment failure](#uc-72-enforce-operational-grace-period-upon-payment-failure)
    - [{U.C. 8} Export Data and Close Accounts](#uc-8-export-data-and-close-accounts)
      - [{U.C. 8.1} Export personal and workspace data archives](#uc-81-export-personal-and-workspace-data-archives)
      - [{U.C. 8.2} Close user accounts and terminate workspace access](#uc-82-close-user-accounts-and-terminate-workspace-access)
- [5. Non-Functional Requirements](#5-non-functional-requirements)
- [6. Conclusions](#6-conclusions)
- [7. Bibliography](#7-bibliography)
- [Version History](#version-history)

---

## 1. Introduction

The **TinyTask SaaS** platform delivers a lean, collaborative project and task management environment tailored for small agile teams, agencies, and consultancies. Following the operational elicitation established in `Doc01` (AS-IS and TO-BE models), this deliverable establishes the formal **System Use Cases**.

In any mature software engineering lifecycle, requirements elicitation and use case modeling form a **sequential continuum**:
1. In `Doc01`, we identified business problems, established customer expectations, consolidated atomic functional requirements (prioritized via MoSCoW), and defined the Product Use Cases (*PUC*) boundary.
2. In `Doc02`, we take those requirements and PUCs and model the dynamic behavioral interactions between actors and the system, specifying how business goals are fulfilled in practice.

To prevent superficial or generic descriptions, this document adopts the best practices established in requirements engineering literature, formalizing each use case into an operational contract that details normal execution, edge cases, error conditions, and verifiable guarantees, accompanied by visual UML Use Case diagrams rendered directly in Markdown.

---

## 2. System Requirements Approach & Literature Foundations

### 2.1 The Volere Triangular Decomposition: Business Events to System Use Cases

The specification follows the Volere requirements engineering methodology (Robertson & Robertson, 2012). Every functional capability traces through a triangular derivation:
- **Business Event:** An occurrence in the operational environment that demands a response (e.g., *a new team member needs onboarding*, *a project phase is completed*, *a task deliverable is updated*).
- **Product Use Case (PUC):** The automated partition of the business process executed within the system boundary (defined in `Doc01` Table 8).
- **System Use Case:** The structured behavioral interaction between the primary actor and the system required to achieve the goal (detailed herein).

### 2.2 Use Case Architecture (Cockburn, Larman, Wiegers)

According to Alistair Cockburn (*Writing Effective Use Cases*, 2000), Craig Larman (*Applying UML and Patterns*, 2004), and Karl Wiegers & Joy Beatty (*Software Requirements*, 2013), use cases represent **behavioral contracts** between stakeholders and the system. They describe the system's behavior under various conditions as it responds to a request from one of its stakeholders (the primary actor).

Key literature principles enforced throughout this specification include:
1. **Black-Box Perspective (Larman, 2004):** The use case specifies *what* the system does (its responsibilities and external contracts), never *how* internal components, database tables, or algorithms execute it.
2. **Goal-Driven Scope (Cockburn, 2000):** Every use case is titled with an active verb phrase representing a clear, valuable user goal.
3. **Dual Scenario Coverage (Cockburn, 2000):** A use case is incomplete if it only documents the "happy path". Literature mandates documenting both the **Main Success Scenario** (the typical, ideal progression) and **Extensions** (alternative flows, branch conditions, validation failures, and exception handling).
4. **Verifiable Guarantees (Cockburn, 2000):** Every use case explicitly declares its **Success Guarantees** (what must be true if the goal is achieved) and **Minimal Guarantees** (what the system guarantees even if the goal fails, protecting system and data integrity).

### 2.3 Visual UML Use Case Modeling in Markdown

In standard software engineering, text specifications and visual diagrams complement each other. To make the specification natively readable, version-controllable, and visually rich without relying on static external images, this document leverages **Mermaid.js**, the open industry standard for rendering UML directly inside Markdown:
- Each macro capability cluster (`{U.C. 1}` to `{U.C. 8}`) is preceded by an error-free **UML Use Case Diagram** (`flowchart LR`), depicting the human actors and supporting external services linked to oval use case goals in standard UML notation.
- Node identifiers and text labels avoid special bracket characters that disrupt Markdown parsers, ensuring 100% error-free visual rendering.

### 2.4 Anatomy of a Literature-Grounded Use Case

Each Level-1 System Use Case in this document follows the formal, fully dressed specification card:

| Field | Description & Literature Definition |
|---|---|
| **ID & Name** | Canonical identifier (`{U.C. n.m}`) and active verb phrase denoting the user goal. |
| **Traceability** | Direct mapping to the underlying Functional Requirement (`R...`) and Product Use Case (`PUC...`) from `Doc01`. |
| **Primary Actor** | The principal human user or external system initiating the interaction to achieve a business goal. |
| **Supporting Actors** | Auxiliary subsystems or external services participating in the execution (e.g., Payment Gateway, Email Service). |
| **Scope & Level** | System boundary: *TinyTask SaaS*; Level: *Sea Level (User Goal / Level 1)*. |
| **Stakeholders & Interests** | The list of organizational stakeholders who care about the outcome and their specific interests. |
| **Preconditions** | The state the system and actors must be in before the use case can be triggered. |
| **Trigger** | The specific business event that initiates execution. |
| **Main Success Scenario** | Numbered sequence of operational interactions between the Actor and the System (normal/happy path). |
| **Extensions** | Branching conditions, business rule variations, and exception flows (e.g., `2a`, `3a`) indicating recovery paths. |
| **Success Guarantees** | The postconditions that must hold when the use case completes successfully. |
| **Minimal Guarantees** | The system state guaranteed even if the use case terminates prematurely (rollback, security preservation). |

### 2.5 Refinement Boundary: Cockburn's Sea Level (Level 1) vs. Micro-UI Anti-Patterns

A central lesson in Requirements Engineering is avoiding the **Clam-Level Decomposition Trap** (Anti-Pattern 3 in `phase3_functional_spec_guidelines.md`):
- **Sea Level (User Goal — Level 1):** The interaction satisfies a complete, discrete business task in a single sitting that delivers measurable value to the user (e.g., *Create and assign tasks*, *Invite workspace members*, *Manage deliverable attachments*).
- **Sub-function / Clam Level (Level 2+):** Micro-interactions such as clicking a specific button, focusing an input field, or validating a single string format.
- **Rule:** Refinement strictly anchors at **Level 1 (`{U.C.n.m}`)**. There are **zero leaf nodes (`{U.C.n.m.k}`)** and **zero procedural UI scripts** in the baseline. Step sequences in the Main Success Scenario represent *business-level actor intent and system response*, not UI layout instructions.

---

## 3. Requirements Analysis

### 3.1 Work Context Model

The following diagram illustrates the information boundaries between TinyTask SaaS and adjacent external entities:

```mermaid
flowchart TD
    User["Team Members and Admins"] -->|Credentials, Tasks, Comments, Deliverables| TT["TinyTask SaaS Platform"]
    Owner["Workspace Owner"] -->|Subscription Plans, Member Quotas, Data Archives| TT
    TT -->|Transactional Emails and Task Digests| Mail["Notification / Email Service"]
    TT -->|Checkout Sessions and Billing Inquiries| Gateway["External Payment Gateway"]
    Gateway -->|Payment Status Confirmations| TT
```

### 3.2 Traceability Matrix: Requirements (Doc01) to System Use Cases (Doc02)

The following matrix establishes strict bi-directional traceability between the 18 consolidated functional requirements from `Doc01` and the 18 Level-1 System Use Cases:

*Table 1. Traceability Matrix*

| Functional Req (Doc01) | Product Use Case (Doc01) | System Use Case (Doc02) | Use Case Title | Priority | Bound Security & Privacy Constraints (Doc03) |
|---|---|---|---|---|---|
| **R1.1** | **PUC 1.1** | **{U.C. 1.1}** | Register and authenticate user accounts | MUST | REQ-SEC-02, REQ-SEC-03, REQ-SEC-10, REQ-PRIV-01, REQ-PRIV-06 |
| **R1.2** | **PUC 1.2** | **{U.C. 1.2}** | Manage user profile and account preferences | SHOULD | REQ-SEC-01, REQ-PRIV-02, REQ-PRIV-05, REQ-PRIV-08 |
| **R2.1** | **PUC 2.1** | **{U.C. 2.1}** | Create and configure workspace | MUST | REQ-SEC-01, REQ-SEC-04, REQ-SEC-10 |
| **R2.2** | **PUC 2.2** | **{U.C. 2.2}** | Invite workspace members and manage access roles | MUST | REQ-SEC-04, REQ-SEC-10, REQ-PRIV-01 |
| **R2.3** | **PUC 2.3** | **{U.C. 2.3}** | Monitor workspace activity and operational metrics | COULD | REQ-SEC-01, REQ-SEC-04 |
| **R3.1** | **PUC 3.1** | **{U.C. 3.1}** | Create and configure projects | MUST | REQ-SEC-01, REQ-SEC-04, REQ-SEC-10 |
| **R3.2** | **PUC 3.2** | **{U.C. 3.2}** | Archive completed projects | SHOULD | REQ-SEC-04, REQ-SEC-10 |
| **R4.1** | **PUC 4.1** | **{U.C. 4.1}** | Create and assign tasks | MUST | REQ-SEC-01, REQ-SEC-04 |
| **R4.2** | **PUC 4.2** | **{U.C. 4.2}** | Track and transition task workflow states on visual boards | MUST | REQ-SEC-01, REQ-SEC-09 |
| **R4.3** | **PUC 4.3** | **{U.C. 4.3}** | Configure recurring automated tasks | COULD | REQ-SEC-01, REQ-SEC-10 |
| **R5.1** | **PUC 5.1** | **{U.C. 5.1}** | Manage task deliverable attachments | MUST | REQ-SEC-05, REQ-PRIV-07 |
| **R5.2** | **PUC 5.2** | **{U.C. 5.2}** | Post in-task discussion comments and mention collaborators | MUST | REQ-SEC-06, REQ-PRIV-08 |
| **R6.1** | **PUC 6.1** | **{U.C. 6.1}** | Consult chronological audit history on task cards | MUST | REQ-SEC-10, REQ-PRIV-04 |
| **R6.2** | **PUC 6.2** | **{U.C. 6.2}** | Receive workspace alerts and daily task digests | SHOULD | REQ-SEC-01, REQ-PRIV-06 |
| **R7.1** | **PUC 7.1** | **{U.C. 7.1}** | Subscribe and manage workspace commercial plans | MUST | REQ-SEC-07, REQ-SEC-08, REQ-SEC-10 |
| **R7.2** | **PUC 7.2** | **{U.C. 7.2}** | Enforce operational grace period upon payment failure | MUST | REQ-SEC-07, REQ-SEC-08, REQ-SEC-10 |
| **R8.1** | **PUC 8.1** | **{U.C. 8.1}** | Export personal and workspace data archives | MUST | REQ-PRIV-02, REQ-PRIV-05, REQ-SEC-01 |
| **R8.2** | **PUC 8.2** | **{U.C. 8.2}** | Close user accounts and terminate workspace access | MUST | REQ-PRIV-03, REQ-PRIV-08, REQ-SEC-03, REQ-SEC-10 |

---

## 4. Domain Application Use Cases

### 4.1 System Actors

The platform defines four human user roles and two external supporting system actors:
- **Workspace Owner:** Commercial and administrative authority. Controls billing, subscriptions, seat quotas, and organization-wide data archives.
- **Workspace Admin:** Operational team coordinator. Manages workspace configuration, invites members, allocates access roles, and initializes projects.
- **Workspace Member:** Standard contributor. Creates and updates tasks, uploads deliverables, participates in task discussions, and manages profile settings.
- **Workspace Viewer:** Read-only guest or client observer. Accesses authorized projects, boards, and task details without edit rights.
- **External Payment Gateway:** Third-party financial processor handling commercial plan checkout sessions and dispatching payment status confirmations.
- **Notification / Email Service:** Subsystem responsible for dispatching activation emails, password reset links, assignment alerts, and daily digests.

---

### 4.2 System Use Cases Specification

---

### {U.C. 1} Manage User Accounts and Authentication

#### UML Use Case Diagram: Capability Cluster {U.C. 1}

```mermaid
flowchart LR
    Visitor["Unauthenticated Visitor / Registered User"]
    Email["Notification / Email Service"]
    
    subgraph UC1_Cluster ["UC 1 - Manage User Accounts and Authentication"]
        UC1_1(["UC 1.1: Register and authenticate user accounts"])
        UC1_2(["UC 1.2: Manage user profile and account preferences"])
    end

    Visitor --> UC1_1
    Visitor --> UC1_2
    UC1_1 -.-> Email
```

#### {U.C. 1.1} Register and authenticate user accounts
- **Traceability:** Requirement `R1.1` | Product Use Case `PUC 1.1`
- **Security & Privacy Traces:** `REQ-SEC-02` (Credential Hashing), `REQ-SEC-03` (Session Invalidation), `REQ-SEC-10` (Audit Logging), `REQ-PRIV-01` (Data Minimization), `REQ-PRIV-06` (TLS 1.3)
- **Primary Actor:** Unauthenticated Visitor / Registered User
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Platform Founders:* Fast, self-service onboarding with low drop-off.
  - *End Users:* Secure, reliable access to authorized team workspaces.
- **Preconditions:** network connection terminates over TLS 1.3 (REQ-PRIV-06); The user has access to a valid email inbox.
- **Trigger:** A prospective user initiates account registration, an existing user attempts login, or a user requests credential recovery.
- **Main Success Scenario (Happy Path):**
  1. Actor submits registration details including full name, email address, and desired credentials.
  2. System validates input format, verifies email address uniqueness, creates an unactivated account, and dispatches a time-limited email activation link.
  3. Actor accesses the activation link sent via email.
  4. System activates the account record and presents the login interface.
  5. Actor submits valid credentials.
  6. System verifies credentials, creates an active authenticated session, and returns the user's authorized workspace dashboard.
- **Extensions (Alternative & Exception Flows):**
  - **1a. Email already registered:**
    - 1a1. System notifies actor that an account with that email already exists and offers login or password recovery options.
  - **1b. Invalid credential format:**
    - 1b1. System highlights formatting errors and prompts actor to supply conforming inputs.
  - **3a. Activation link expired or tampered:**
    - 3a1. System prompts actor that the link is invalid and offers to generate a fresh activation email.
  - **5a. Actor forgot credentials (Password Recovery Flow):**
    - 5a1. Actor submits registered email address on password recovery form.
    - 5a2. System verifies email existence and dispatches a single-use, time-limited reset link.
    - 5a3. Actor accesses reset link and provides a new password.
    - 5a4. System updates credentials and invalidates reset link. Use case resumes at step 5.
  - **5b. Invalid login credentials:**
    - 5b1. System informs actor of authentication failure and increments failed attempt counter without revealing whether the email or password was incorrect.
  - **5c. Repeated authentication failures exceed threshold (5 attempts):**
    - 5c1. System temporarily blocks authentication attempts for target account for 15 minutes, returns generic throttling notice, and records security alert in audit log (REQ-SEC-03, REQ-SEC-10).
- **Success Guarantees (Postconditions):** An authenticated session is issued to the user; the user has access to authorized workspace rosters.
- **Minimal Guarantees:** Failed attempts leave database credentials unmodified; security audit log records timestamp and client IP for every rejected attempt; zero credentials or session tokens are leaked (REQ-SEC-10).

---

#### {U.C. 1.2} Manage user profile and account preferences
- **Traceability:** Requirement `R1.2` | Product Use Case `PUC 1.2`
- **Security & Privacy Traces:** `REQ-SEC-01` (Tenant Isolation), `REQ-PRIV-02` (Portability), `REQ-PRIV-05` (Encryption at Rest), `REQ-PRIV-08` (Privacy Audit Trail)
- **Primary Actor:** Authenticated User
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors:* Maintain accurate identity details and control personal notification volume.
- **Preconditions:** token is authenticated and bound to target organization (REQ-SEC-01); User possesses an active authenticated session.
- **Trigger:** User accesses account settings to update personal information or adjust notification channels.
- **Main Success Scenario:**
  1. Actor navigates to profile settings and requests profile modification.
  2. System displays current profile data (full name, avatar graphic, contact details, notification preferences).
  3. Actor updates desired fields (e.g., changes display name, uploads new profile avatar, toggles email digest settings) and submits changes.
  4. System validates inputs and checks avatar file size (maximum 2 MB).
  5. System persists updated profile attributes and displays confirmation of successful update.
- **Extensions:**
  - **4a. Avatar graphic exceeds maximum size:**
    - 4a1. System rejects file, informs actor of the 2 MB limit, and retains current avatar.
  - **4b. Empty mandatory fields (e.g., blank name):**
    - 4b1. System prompts actor that display name is mandatory and halts update.
  - **4c. Session timeout or invalid tenant context:**
    - 4c1. System halts transaction, invalidates expired token, and redirects actor to re-authenticate without saving changes (REQ-SEC-03).
- **Success Guarantees:** Updated personal details and notification preferences take effect across all workspace views immediately.
- **Minimal Guarantees:** Existing profile data remains unchanged if validation fails; profile modifications emit a structured privacy audit record (REQ-PRIV-08).

---

### {U.C. 2} Manage Workspaces and Teams

#### UML Use Case Diagram: Capability Cluster {U.C. 2}

```mermaid
flowchart LR
    Owner["Workspace Owner"]
    Admin["Workspace Admin"]
    Email["Notification / Email Service"]

    subgraph UC2_Cluster ["UC 2 - Manage Workspaces and Teams"]
        UC2_1(["UC 2.1: Create and configure workspace"])
        UC2_2(["UC 2.2: Invite workspace members and manage access roles"])
        UC2_3(["UC 2.3: Monitor workspace activity and operational metrics"])
    end

    Owner --> UC2_1
    Owner --> UC2_2
    Owner --> UC2_3
    Admin --> UC2_1
    Admin --> UC2_2
    Admin --> UC2_3
    UC2_2 -.-> Email
```

#### {U.C. 2.1} Create and configure workspace
- **Traceability:** Requirement `R2.1` | Product Use Case `PUC 2.1`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-04` (Role-Based Access Control), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Authenticated User (becoming Workspace Owner) / Workspace Admin
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Business Customers:* Rapid creation of isolated, branded team collaboration environments.
  - *Platform Leadership:* Clear tenant separation and initial account ownership.
- **Preconditions:** actor possesses valid authenticated session (REQ-SEC-01); Actor has an active authenticated user account.
- **Trigger:** Actor requests the creation of a new organization workspace or edits an existing workspace profile.
- **Main Success Scenario:**
  1. Actor submits new workspace parameters: organization name, desired URL slug, and optional brand logo graphic.
  2. System validates name and verifies that the requested URL slug is globally unique.
  3. System provisions the isolated workspace container, sets default Free tier limits, and assigns the actor as the primary Workspace Owner.
  4. System routes actor into the newly initialized workspace environment ready for project setup.
- **Extensions:**
  - **2a. Requested URL slug is already taken:**
    - 2a1. System notifies actor and suggests available alternative slugs.
  - **2b. Workspace branding update on existing workspace:**
    - 2b1. Authorized Workspace Admin or Owner edits organization name or uploads new logo.
    - 2b2. System updates workspace metadata and renders updated branding to all active members.
  - **3c. Unauthorized tenant boundary manipulation attempt:**
    - 3c1. System refuses workspace container creation, terminates request, and emits high-priority security audit log (REQ-SEC-01, REQ-SEC-10).
- **Success Guarantees:** A logically isolated workspace is initialized; the creator possesses full administrative and billing privileges.
- **Minimal Guarantees:** No partially provisioned workspace records remain if container provisioning fails; audit log records provisioning attempt (REQ-SEC-10).

---

#### {U.C. 2.2} Invite workspace members and manage access roles
- **Traceability:** Requirement `R2.2` | Product Use Case `PUC 2.2`
- **Security & Privacy Traces:** `REQ-SEC-04` (RBAC), `REQ-SEC-10` (Audit Logging), `REQ-PRIV-01` (Data Minimization)
- **Primary Actor:** Workspace Admin / Workspace Owner
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Leads:* Flexible team onboarding and role governance without administrative overhead.
  - *Executive Leadership:* Strict enforcement of subscription seat quotas and role boundaries.
- **Preconditions:** actor role verified via RBAC engine (REQ-SEC-04); Actor is authenticated with Admin or Owner privileges in the target workspace.
- **Trigger:** Admin decides to add team collaborators, adjust an existing member's operational role, or revoke access.
- **Main Success Scenario:**
  1. Actor accesses member management interface and submits one or more collaborator email addresses with assigned initial roles (Admin, Member, Viewer).
  2. System verifies that adding the requested users will not exceed the workspace's active member seat limit.
  3. System generates unique invitation tokens and dispatches invitation emails with onboarding links to invitees.
  4. System logs pending invitations in the workspace member roster.
- **Extensions:**
  - **2a. Member limit reached under active subscription plan:**
    - 2a1. System halts invitation, notifies actor that seat capacity is exhausted, and prompts the Workspace Owner to upgrade plan tier.
  - **2b. Modifying an existing member's role:**
    - 2b1. Actor selects an existing member and updates their role (e.g., Member to Admin).
    - 2b2. System verifies actor has authority (only Owners can appoint Admins) and commits the updated role.
  - **2c. Revoking workspace membership:**
    - 2c1. Actor selects member to remove and confirms revocation.
    - 2c2. System verifies member is not the Workspace Owner (Owner cannot be removed).
    - 2c3. System revokes workspace access tokens, ends active project assignments, and frees one seat in the member quota.
  - **4d. Actor lacks required administrative privilege (RBAC violation):**
    - 4d1. System rejects invitation or role mutation with HTTP 403 Forbidden and records access denial in security audit log (REQ-SEC-04, REQ-SEC-10).
- **Success Guarantees:** Roster reflects updated members and roles; authorization rules are strictly updated for subsequent actions.
- **Minimal Guarantees:** Member roster and seat quotas remain unaffected upon invitation or role assignment failures; all role modifications are permanently logged (REQ-SEC-10).

---

#### {U.C. 2.3} Monitor workspace activity and operational metrics
- **Traceability:** Requirement `R2.3` | Product Use Case `PUC 2.3`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-04` (RBAC)
- **Primary Actor:** Workspace Admin / Workspace Owner
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Leads & Owners:* Clear visibility into team productivity, task throughput, and resource utilization.
- **Preconditions:** tenant context verified (REQ-SEC-01); Actor holds Admin or Owner status in the workspace.
- **Trigger:** Actor accesses the workspace management dashboard to review operational performance.
- **Main Success Scenario:**
  1. Actor requests workspace operational metrics view.
  2. System queries operational data stores across projects and aggregates key performance metrics: total active members, tasks completed in current billing cycle, open overdue items, and total deliverable storage consumed.
  3. System renders an aggregated metrics dashboard with visual progress indicators and utilization percentages against plan limits.
- **Extensions:**
  - **2a. Workspace has zero completed tasks:**
    - 2a1. System displays baseline setup guide and empty-state placeholders.
  - **2a. Cross-tenant metrics query attempt detected:**
    - 2a1. System blocks query execution, logs isolation breach attempt, and renders only authorized tenant data (REQ-SEC-01, REQ-SEC-10).
- **Success Guarantees:** Accurate, read-only operational telemetry is delivered to authorized management.
- **Minimal Guarantees:** Zero cross-tenant metrics or data items are revealed; read failures produce no system state changes.

---

### {U.C. 3} Manage Projects

#### UML Use Case Diagram: Capability Cluster {U.C. 3}

```mermaid
flowchart LR
    Admin["Workspace Admin / Owner"]
    Member["Workspace Member"]

    subgraph UC3_Cluster ["UC 3 - Manage Projects"]
        UC3_1(["UC 3.1: Create and configure projects"])
        UC3_2(["UC 3.2: Archive completed projects"])
    end

    Admin --> UC3_1
    Admin --> UC3_2
    Member --> UC3_1
```

#### {U.C. 3.1} Create and configure projects
- **Traceability:** Requirement `R3.1` | Product Use Case `PUC 3.1`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-04` (RBAC), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Workspace Admin / Workspace Member
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Project Managers:* Structuring client deliverables and team work streams into coherent containers.
  - *Team Contributors:* Clear organization and scope boundaries for tasks.
- **Preconditions:** actor role authorized to create projects (REQ-SEC-04); Actor is an active member or admin of the workspace.
- **Trigger:** Team initiates a new operational project or client engagement.
- **Main Success Scenario:**
  1. Actor requests project creation and submits project parameters: mandatory title, optional description of deliverables, and visibility setting (workspace-wide or private to designated members).
  2. System validates input data, assigns the actor as project creator, and initializes default task workflow columns (To-Do, In-Progress, Under-Review, Done).
  3. System records project entity and redirects actor to the initialized interactive project board.
- **Extensions:**
  - **1a. Blank project title:**
    - 1a1. System flags title as mandatory and prompts actor to provide a valid name.
  - **1b. Restricted project visibility configured:**
    - 1b1. Actor selects specific workspace members allowed to access the project.
    - 1b2. System restricts project board view strictly to the authorized subset of members.
  - **3b. Actor lacks project creation privileges:**
    - 3b1. System returns permission error and records unauthorized access attempt in audit log (REQ-SEC-04, REQ-SEC-10).
- **Success Guarantees:** Project container is provisioned with default workflow columns and accessible according to visibility rules.
- **Minimal Guarantees:** No unassigned or unisolated project containers are created; security audit trail records creation event (REQ-SEC-10).

---

#### {U.C. 3.2} Archive completed projects
- **Traceability:** Requirement `R3.2` | Product Use Case `PUC 3.2`
- **Security & Privacy Traces:** `REQ-SEC-04` (RBAC), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Workspace Admin / Workspace Owner
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Leads:* Decluttering active workspaces while retaining complete historical deliverable auditability.
- **Preconditions:** actor possesses Admin or Owner role (REQ-SEC-04); Actor possesses Admin or Owner role in the workspace; project is active.
- **Trigger:** All project deliverables are finalized and the project lifecycle reaches completion.
- **Main Success Scenario:**
  1. Actor accesses project settings and selects the archive project option.
  2. System prompts for confirmation, detailing that the project will transition to read-only status and disappear from daily operational board menus.
  3. Actor confirms archival.
  4. System transitions project state to archived, marks all enclosed tasks and discussions as read-only, and records timestamp and actor identity in audit logs.
  5. System updates workspace navigation, removing the project from active lists and moving it to the archived repository view.
- **Extensions:**
  - **1a. Unarchiving an archived project:**
    - 1a1. Actor locates project in archived repository and selects "Restore Project".
    - 1a2. System restores project to active status and enables editing capabilities.
  - **3b. Unauthorized member attempts project archive:**
    - 3b1. System denies archive transition, preserves active project state, and logs access violation (REQ-SEC-04, REQ-SEC-10).
- **Success Guarantees:** Project is read-only; historical tasks, discussions, and attachments remain accessible for compliance and reference.
- **Minimal Guarantees:** Project state remains unmodified if archive authorization check fails.

---

### {U.C. 4} Manage and Execute Tasks

#### UML Use Case Diagram: Capability Cluster {U.C. 4}

```mermaid
flowchart LR
    Member["Workspace Member / Admin"]
    Viewer["Workspace Viewer"]
    Daemon["Automated System Daemon"]
    Notify["Notification / Email Service"]

    subgraph UC4_Cluster ["UC 4 - Manage and Execute Tasks"]
        UC4_1(["UC 4.1: Create and assign tasks"])
        UC4_2(["UC 4.2: Track and transition task workflow states on visual boards"])
        UC4_3(["UC 4.3: Configure recurring automated tasks"])
    end

    Member --> UC4_1
    Member --> UC4_2
    Member --> UC4_3
    Viewer --> UC4_2
    Daemon --> UC4_3
    UC4_1 -.-> Notify
```

#### {U.C. 4.1} Create and assign tasks
- **Traceability:** Requirement `R4.1` | Product Use Case `PUC 4.1`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-04` (RBAC)
- **Primary Actor:** Workspace Member / Workspace Admin
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors & Leads:* Rapid, frictionless capture of actionable work items with clear ownership and deadlines.
- **Preconditions:** actor belongs to authorized workspace project (REQ-SEC-01); Actor has member access to the parent active project.
- **Trigger:** A new actionable work item or deliverable requirement arises.
- **Main Success Scenario:**
  1. Actor initiates task creation within a project and submits task attributes: mandatory title, optional description, priority level (Low, Medium, High, Urgent), target due date, and assigns one or more active workspace members.
  2. System validates input data, initializes task in the "To-Do" status column, and assigns a unique task identifier.
  3. System records task creation event in task audit history.
  4. System generates internal assignment notifications for each assigned collaborator and dispatches notification alerts.
  5. System displays the new task card on the project visual board.
- **Extensions:**
  - **1a. Missing mandatory title:**
    - 1a1. System prompts actor to enter a descriptive title.
  - **1b. Due date specified in the past:**
    - 1b1. System alerts actor that due date is prior to current date, permitting override if intentional for historical logging.
  - **1c. Assignee is not a member of the project:**
    - 1c1. System limits member picker strictly to users authorized on the project container.
  - **3b. Task creation payload contains unescaped malicious scripts:**
    - 3b1. System sanitizes title and description text, neutralising embedded script tags (REQ-SEC-06).
- **Success Guarantees:** Task card exists in the project backlog with assigned collaborators and initial status; assignees receive notifications.
- **Minimal Guarantees:** No partial task records exist without an assigned project identifier and tenant context.

---

#### {U.C. 4.2} Track and transition task workflow states on visual boards
- **Traceability:** Requirement `R4.2` | Product Use Case `PUC 4.2`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-09` (Rate Limiting)
- **Primary Actor:** Workspace Member / Workspace Admin / Workspace Viewer
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors:* Real-time operational visibility into workload, bottlenecks, and delivery progress.
  - *Clients & Viewers:* Transparent status updates without interrupting contributors.
- **Preconditions:** actor session is active; User has access rights to the project board.
- **Trigger:** Actor accesses the project board to inspect progress, filters the view, or moves a task card to reflect progress.
- **Main Success Scenario:**
  1. Actor opens the project board view.
  2. System queries active tasks and renders them categorized in visual status columns: To-Do, In-Progress, Under-Review, Done.
  3. Actor applies filter parameters (e.g., filter by specific assignee, urgent priority, or overdue due dates).
  4. System dynamically refreshes displayed task cards matching filter criteria.
  5. Actor transitions a task card from current column to a target status column (e.g., from "In-Progress" to "Under-Review").
  6. System verifies actor's edit authorization, updates the task state, records the transition event (author, prior state, new state, timestamp) in the task history, and updates board counters.
- **Extensions:**
  - **5a. Actor holds Viewer role (Read-Only):**
    - 5a1. System prevents state transitions and presents read-only board controls.
  - **5b. Task moved directly to "Done":**
    - 5b1. System records completion timestamp and checks whether task recurrence rules apply (triggering {U.C. 4.3} if configured).
  - **2b. High-frequency state transition requests exceed rate limit:**
    - 2b1. System throttles requests, returns HTTP 429 Too Many Requests, and preserves current board state (REQ-SEC-09).
- **Success Guarantees:** Task state transition is committed and reflected immediately across all team views; audit trail is updated.
- **Minimal Guarantees:** Task status updates are atomic; concurrent transition collisions are resolved without data corruption.

---

#### {U.C. 4.3} Configure recurring automated tasks
- **Traceability:** Requirement `R4.3` | Product Use Case `PUC 4.3`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Workspace Member / Workspace Admin (supported by Automated System Daemon)
- **Supporting Actors:** Automated System Daemon
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors:* Eliminate manual effort in recreating repetitive operational duties (e.g., weekly syncs, monthly reviews).
- **Preconditions:** daemon executes within isolated service context (REQ-SEC-01); Task exists within an active project.
- **Trigger:** User sets a recurrence schedule on a task, or a recurring task is transitioned to "Done".
- **Main Success Scenario:**
  1. Actor opens task details and configures a recurrence rule (e.g., every Monday, or 1st of every month).
  2. System validates schedule and attaches the recurrence rule to the task record.
  3. During operational execution, a team member transitions the current task instance to "Done".
  4. System marks the current instance "Done" and automatically instantiates a new duplicate task card in the "To-Do" column with due date set to the next scheduled interval.
  5. System copies task title, description, priority, and assignees to the new instance, leaving previous comments and attachments attached to the completed historical instance.
- **Extensions:**
  - **1a. Actor disables recurrence:**
    - 1a1. Actor removes recurrence schedule.
    - 1a2. System updates task record; task behaves as standard one-off item upon completion.
  - **2a. Recurring automation rule disabled or project archived:**
    - 2a1. Daemon skips execution, logs informational status, and schedules no new instances (REQ-SEC-10).
- **Success Guarantees:** Future recurring work items are scheduled and automatically instantiated without manual overhead.
- **Minimal Guarantees:** Automation failures log diagnostic traces and do not generate duplicate task instances.

---

### {U.C. 5} Collaborate on Task Deliverables

#### UML Use Case Diagram: Capability Cluster {U.C. 5}

```mermaid
flowchart LR
    Member["Workspace Member / Admin"]
    Viewer["Workspace Viewer"]
    Email["Notification / Email Service"]

    subgraph UC5_Cluster ["UC 5 - Collaborate on Task Deliverables"]
        UC5_1(["UC 5.1: Manage task deliverable attachments"])
        UC5_2(["UC 5.2: Post in-task discussion comments and mention collaborators"])
    end

    Member --> UC5_1
    Member --> UC5_2
    Viewer --> UC5_1
    UC5_2 -.-> Email
```

#### {U.C. 5.1} Manage task deliverable attachments
- **Traceability:** Requirement `R5.1` | Product Use Case `PUC 5.1`
- **Security & Privacy Traces:** `REQ-SEC-05` (Strict File Validation & Malware Isolation), `REQ-PRIV-07` (Orphan File Expiration)
- **Primary Actor:** Workspace Member / Workspace Admin / Workspace Viewer
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Contributors & Clients:* Centralize deliverable files in context, eliminating lost attachments and email silos.
- **Preconditions:** actor possesses Member role; storage quota not exceeded; User has access to the task card; member rights required for upload/delete; view rights sufficient for download.
- **Trigger:** Actor attaches a supporting document, downloads a deliverable, or deletes an obsolete file.
- **Main Success Scenario:**
  1. Actor accesses task card attachment section and selects a local file to upload.
  2. System validates file size against the 25 MB ceiling and verifies authorized file extensions (documents, spreadsheets, images).
  3. System streams file to the file storage service, indexes attachment metadata (filename, size, author, timestamp), and binds it to the task.
  4. System generates and displays an inline preview thumbnail and updates the task attachment badge counter.
  5. System records attachment upload in task audit history.
- **Extensions:**
  - **2a. File exceeds 25 MB size limit:**
    - 2a1. System rejects file upload, notifies actor of size violation, and prompts to select a smaller file.
  - **2b. Downloading an attachment:**
    - 2b1. Actor (Member, Admin, or Viewer) clicks download on an attachment.
    - 2b2. System delivers the file binary stream.
  - **2c. Removing an attachment:**
    - 2c1. Authorized actor (uploader or Admin) requests attachment deletion.
    - 2c2. System verifies deletion rights, removes file from storage service, detaches metadata, and logs deletion event in audit history.
  - **4c. Disallowed file type or executable binary signature detected:**
    - 4c1. System rejects upload, purges temporary buffer immediately, and records file security event (REQ-SEC-05).
- **Success Guarantees:** Deliverable file is stored, indexed, and available for authorized team retrieval; audit log records file lifecycle.
- **Minimal Guarantees:** Incomplete or corrupted file fragments are automatically purged from storage buffers; deleted attachments are marked for irreversible cleanup within 14 days (REQ-PRIV-07).

---

#### {U.C. 5.2} Post in-task discussion comments and mention collaborators
- **Traceability:** Requirement `R5.2` | Product Use Case `PUC 5.2`
- **Security & Privacy Traces:** `REQ-SEC-06` (Context-Aware Output Encoding & Anti-XSS), `REQ-PRIV-08` (Privacy Audit Trail)
- **Primary Actor:** Workspace Member / Workspace Admin
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors:* Maintain focused, contextual communication directly bound to deliverables.
- **Preconditions:** actor belongs to workspace team; Actor has member access to the project.
- **Trigger:** Collaborator posts a status note, asks a question, or tags a teammate on a task card.
- **Main Success Scenario:**
  1. Actor opens task card discussion section and enters comment text utilizing Markdown formatting.
  2. Actor types collaborator mention (`@collaborator`) selecting a target workspace member from the auto-complete suggestion list.
  3. Actor submits comment.
  4. System parses text, validates non-empty content, records comment in the task thread with author identity and timestamp.
  5. System identifies mentioned users and generates in-app notification alerts linking directly to the comment.
  6. System displays the new comment at the end of the chronological discussion thread.
- **Extensions:**
  - **1a. Empty comment submission:**
    - 1a1. System disables submission until non-whitespace text is entered.
  - **4a. Mentioned user has disabled email alerts:**
    - 4a1. System respects user preferences, generating in-app notification while suppressing external email dispatch.
  - **3c. Comment body contains malicious script or disallowed HTML tags:**
    - 3c1. System sanitizes and HTML-encodes input, rendering payload as inert text without executing active scripts (REQ-SEC-06).
- **Success Guarantees:** Comment is permanently appended to task context; tagged collaborators are alerted immediately.
- **Minimal Guarantees:** Unsubmitted draft comments are not stored; rendered comments are context-encoded to prevent stored XSS (REQ-SEC-06).

---

### {U.C. 6} Track Activity History and Notifications

#### UML Use Case Diagram: Capability Cluster {U.C. 6}

```mermaid
flowchart LR
    User["Registered Workspace User"]
    Email["Notification / Email Service"]

    subgraph UC6_Cluster ["UC 6 - Track Activity History and Notifications"]
        UC6_1(["UC 6.1: Consult chronological audit history on task cards"])
        UC6_2(["UC 6.2: Receive workspace alerts and daily task digests"])
    end

    User --> UC6_1
    User --> UC6_2
    UC6_2 -.-> Email
```

#### {U.C. 6.1} Consult chronological audit history on task cards
- **Traceability:** Requirement `R6.1` | Product Use Case `PUC 6.1`
- **Security & Privacy Traces:** `REQ-SEC-10` (Audit Logging), `REQ-PRIV-04` (Purpose Limitation)
- **Primary Actor:** Authorized Workspace Users (Member, Admin, Owner, Viewer)
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Project Managers & Team Leads:* Complete traceability and operational accountability for all task modifications.
- **Preconditions:** actor possesses read permissions for target task (REQ-SEC-01); User has access rights to view the task card.
- **Trigger:** Actor opens the task details card and navigates to the activity history tab.
- **Main Success Scenario:**
  1. Actor opens the activity history tab on a task card.
  2. System queries the immutable audit log table for all events tied to the task identifier.
  3. System renders a chronological timeline displaying: task creation, state transitions, assignee reallocations, due date changes, and attachment uploads/deletions, detailing the performing actor and exact timestamp for each event.
- **Extensions:**
  - **2a. Task has no historical modifications beyond creation:**
    - 2a1. System displays task creation event as the solitary timeline entry.
  - **2a. Audit log query exceeds pagination threshold:**
    - 2a1. System caps result batch at 100 entries and requires cursor-based pagination (REQ-SEC-09).
- **Success Guarantees:** Complete, tamper-evident audit history is presented to authorized users.
- **Minimal Guarantees:** Audit records are read-only; history entries cannot be modified or deleted via user interfaces (REQ-SEC-10).

---

#### {U.C. 6.2} Receive workspace alerts and daily task digests
- **Traceability:** Requirement `R6.2` | Product Use Case `PUC 6.2`
- **Security & Privacy Traces:** `REQ-SEC-01` (Multi-Tenant Isolation), `REQ-PRIV-06` (Transport Encryption)
- **Primary Actor:** Registered User
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Team Contributors:* Stay informed of immediate assignments and critical deadlines without notification overload.
- **Preconditions:** actor preferences permit notifications; User holds an active account in one or more workspaces.
- **Trigger:** User logs into the platform and checks the notification center, or scheduled morning digest daemon triggers.
- **Main Success Scenario:**
  1. Actor accesses platform interface and inspects notification bell icon displaying an unread alert counter.
  2. Actor clicks notification center; System displays an actionable list of recent notifications (task assignments, @mentions).
  3. Actor clicks a notification item; System marks the notification as read and navigates directly to the target task card.
  4. Concurrently, at scheduled morning time (08:00 local workspace time), system identifies all tasks due today or overdue for the user and dispatches a consolidated email digest.
- **Extensions:**
  - **1a. User has zero unread notifications:**
    - 1a1. System displays empty notification state ("All caught up").
  - **4a. User has opted out of daily email digests in profile preferences:**
    - 4a1. System skips email compilation for that user, preserving in-app notifications only.
  - **3a. External notification service unavailable:**
    - 3a1. System enqueues notifications in retry buffer and logs temporary transport failure without impacting core platform operations.
- **Success Guarantees:** User receives timely operational alerts and morning work prioritization guidance.
- **Minimal Guarantees:** Notification deliveries contain only authorized user task snippets and exclude sensitive credentials.

---

### {U.C. 7} Manage Commercial Subscriptions

#### UML Use Case Diagram: Capability Cluster {U.C. 7}

```mermaid
flowchart LR
    Owner["Workspace Owner"]
    Gateway["External Payment Gateway"]
    Email["Notification / Email Service"]

    subgraph UC7_Cluster ["UC 7 - Manage Commercial Subscriptions"]
        UC7_1(["UC 7.1: Subscribe and manage workspace commercial plans"])
        UC7_2(["UC 7.2: Enforce operational grace period upon payment failure"])
    end

    Owner --> UC7_1
    Owner --> UC7_2
    Gateway --> UC7_1
    Gateway --> UC7_2
    UC7_2 -.-> Email
```

#### {U.C. 7.1} Subscribe and manage workspace commercial plans
- **Traceability:** Requirement `R7.1` | Product Use Case `PUC 7.1`
- **Security & Privacy Traces:** `REQ-SEC-07` (Billing Invariant Protection), `REQ-SEC-08` (HMAC Webhook Verification), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Workspace Owner
- **Supporting Actors:** External Payment Gateway
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Workspace Owner:* Transparent self-service billing, predictable licensing, and instant seat capacity expansion.
  - *Platform Leadership:* Automated subscription revenue capture and accurate quota management.
- **Preconditions:** actor has Owner role; session authenticated (REQ-SEC-04); Actor is authenticated and holds the Workspace Owner role.
- **Trigger:** Owner decides to upgrade from Free tier to Pro or Enterprise, or updates payment details.
- **Main Success Scenario:**
  1. Actor navigates to workspace billing management and selects desired commercial plan tier and seat quantity.
  2. System initiates checkout session with the external payment gateway, transferring plan metadata and success/cancel callback parameters.
  3. System redirects actor's browser to the payment gateway's secure hosted payment page.
  4. Actor completes payment transaction with the external payment provider.
  5. External payment gateway records successful payment and dispatches asynchronous signed payment confirmation to the platform core.
  6. System verifies payment confirmation signature, updates workspace subscription record (plan tier, renewal date, payment status), and instantly expands the authorized member seat quota.
  7. Actor returns to TinyTask workspace, which displays confirmed active tier status and expanded member capacity.
- **Extensions:**
  - **4a. Actor cancels checkout on external gateway page:**
    - 4a1. Payment gateway redirects actor back to TinyTask workspace via cancel callback.
    - 4a2. System retains current plan status and presents checkout cancellation notice.
  - **5a. Payment authorization rejected by financial institution:**
    - 5a1. Payment gateway notifies actor of rejection and prompts for alternative payment method.
  - **5c. Payment webhook signature validation fails:**
    - 5c1. System rejects webhook as untrusted/forged, makes zero modifications to workspace subscription tier, and alerts security operations (REQ-SEC-07, REQ-SEC-08, REQ-SEC-10).
- **Success Guarantees:** Subscription plan and member seat limits are automatically upgraded upon payment confirmation.
- **Minimal Guarantees:** No commercial plan upgrades or quota adjustments occur without verified cryptographic payment receipt (REQ-SEC-07, REQ-SEC-10).

---

#### {U.C. 7.2} Enforce operational grace period upon payment failure
- **Traceability:** Requirement `R7.2` | Product Use Case `PUC 7.2`
- **Security & Privacy Traces:** `REQ-SEC-07` (Billing Invariant Protection), `REQ-SEC-08` (HMAC Webhook Verification), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** External Payment Gateway / Workspace Owner
- **Supporting Actors:** External Payment Gateway, Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *Business Customers:* Business continuity and prevention of abrupt work stoppage due to transient card failures.
  - *Finance Operations:* Systematic recovery of unpaid renewals before service termination.
- **Preconditions:** external payment webhook verified via cryptographic signature (REQ-SEC-08); Workspace possesses an active paid commercial subscription reaching its renewal billing cycle.
- **Trigger:** Automated recurring subscription renewal payment fails at the external payment gateway.
- **Main Success Scenario:**
  1. External payment gateway attempts recurring subscription charge; transaction fails (e.g., expired card, insufficient funds).
  2. External payment gateway dispatches payment failure event to TinyTask platform.
  3. System registers payment failure and initiates a 7-day operational grace period.
  4. System dispatches urgent notification email to the Workspace Owner and displays an administrative payment warning banner within the workspace.
  5. During the 7-day grace period, all workspace members retain full normal operational access to projects and tasks.
  6. Workspace Owner accesses billing settings and updates payment credentials via the external payment gateway.
  7. Payment gateway successfully charges renewal and dispatches payment confirmation.
  8. System lifts the grace period and clears warning banners.
- **Extensions:**
  - **6a. Grace period expires without payment resolution (Day 8):**
    - 6a1. System automatically transitions workspace to restricted read-only status and suspends member invitations until billing is rectified.
  - **3a. Webhook timestamp exceeds allowable replay window (5 minutes):**
    - 3a1. System rejects expired webhook payload, logs replay detection event, and halts state transition (REQ-SEC-08, REQ-SEC-10).
- **Success Guarantees:** Team operations are shielded from immediate disruption during temporary financial glitches; resolution restores normal status cleanly.
- **Minimal Guarantees:** Grace period state changes require verified payment gateway origin and emit immutable billing audit records (REQ-SEC-10).

---

### {U.C. 8} Export Data and Close Accounts

#### UML Use Case Diagram: Capability Cluster {U.C. 8}

```mermaid
flowchart LR
    User["Authenticated User"]
    Owner["Workspace Owner"]
    Email["Notification / Email Service"]

    subgraph UC8_Cluster ["UC 8 - Export Data and Close Accounts"]
        UC8_1(["UC 8.1: Export personal and workspace data archives"])
        UC8_2(["UC 8.2: Close user accounts and terminate workspace access"])
    end

    User --> UC8_1
    User --> UC8_2
    Owner --> UC8_1
    UC8_2 -.-> Email
```

#### {U.C. 8.1} Export personal and workspace data archives
- **Traceability:** Requirement `R8.1` | Product Use Case `PUC 8.1`
- **Security & Privacy Traces:** `REQ-PRIV-02` (Data Portability), `REQ-PRIV-05` (Encryption at Rest), `REQ-SEC-01` (Tenant Isolation)
- **Primary Actor:** Authenticated User / Workspace Owner
- **Supporting Actors:** None
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *End Users & Customers:* Autonomous data portability, offline backup capability, and complete vendor autonomy.
- **Preconditions:** actor possesses valid session; organization export requires Owner role (REQ-SEC-04); Actor possesses valid authenticated session; workspace export restricted to Workspace Owner.
- **Trigger:** User requests export of personal profile and task data, or Workspace Owner requests full organization archive.
- **Main Success Scenario:**
  1. Actor accesses data export options in settings menu and selects desired export scope (personal data export or full workspace archive).
  2. System verifies actor's authorization (Owner role required for workspace-level export).
  3. System initiates background archive compilation, aggregating user profile records, project details, task cards, comment histories, and deliverable attachments into structured JSON and standard archive formats.
  4. System compiles package and presents a secure, authenticated download link to the actor.
  5. Actor downloads the comprehensive archive package to their local workstation.
- **Extensions:**
  - **2a. Non-Owner attempts workspace-level export:**
    - 2a1. System rejects request with authorization notice, permitting personal data export only.
  - **3a. Large workspace archive compilation:**
    - 3a1. System notifies actor that compilation is queued and sends an email notification with download link once ready.
  - **2a. Workspace Member attempts organization-wide export:**
    - 2a1. System restricts export options strictly to the member's own profile and authored contributions (REQ-SEC-04).
  - **4b. Archive download link expires (link valid for 48 hours):**
    - 4b1. System invalidates expired download token and prompts actor to request a fresh export archive (REQ-SEC-03).
- **Success Guarantees:** Complete, structured operational and personal data is delivered to the user without data omission.
- **Minimal Guarantees:** Personal data of third parties is strictly excluded from individual user data archives; exported archive package is encrypted at rest prior to download (REQ-PRIV-02, REQ-PRIV-05).

---

#### {U.C. 8.2} Close user accounts and terminate workspace access
- **Traceability:** Requirement `R8.2` | Product Use Case `PUC 8.2`
- **Security & Privacy Traces:** `REQ-PRIV-03` (Right to Erasure), `REQ-PRIV-08` (Privacy Audit Trail), `REQ-SEC-03` (Session Invalidation), `REQ-SEC-10` (Audit Logging)
- **Primary Actor:** Authenticated User
- **Supporting Actors:** Notification / Email Service
- **Scope & Level:** TinyTask SaaS Platform | Sea Level (User Goal / Level 1)
- **Stakeholders & Interests:**
  - *End Users:* Full sovereignty over account lifecycle and certainty of credential deactivation.
  - *Workspace Admins:* Immediate revocation of departed member access privileges.
- **Preconditions:** actor possesses active session; identity confirmed (REQ-SEC-03); Actor possesses an active authenticated user account.
- **Trigger:** User chooses to terminate their platform account.
- **Main Success Scenario:**
  1. Actor accesses account security settings and selects "Close Account".
  2. System presents warning regarding permanent loss of credentials and severance of workspace memberships, requiring explicit confirmation.
  3. Actor confirms account termination.
  4. System invalidates all active sessions, revokes authentication tokens, marks the user account as closed, and removes active workspace memberships.
  5. System dispatches a formal digital confirmation receipt via email certifying account termination date and time.
  6. System terminates user session and redirects browser to public landing page.
- **Extensions:**
  - **3a. Actor is the sole Workspace Owner of an active multi-member workspace:**
    - 3a1. System halts account closure, notifying actor that workspace ownership must be transferred to another administrator or the workspace deleted before closing the personal account.
  - **4b. Closure confirmed by single user:**
    - 4b1. System deactivates personal credentials, removes user from team rosters, and pseudonymizes authored task comments in accordance with REQ-PRIV-03.
  - **4c. Session invalidation fails during closure:**
    - 4c1. System executes emergency forced server-side token revocation to prevent unauthorized post-closure access (REQ-SEC-03).
- **Success Guarantees:** User credentials and sessions are permanently deactivated; workspace access is revoked; confirmation receipt is sent.
- **Minimal Guarantees:** Account deactivation immediately revokes authentication tokens, preventing subsequent API or UI access; personal data is pseudonymized within 30 days and audit logged (REQ-PRIV-03, REQ-SEC-10).

---

## 5. Non-Functional Requirements

The non-functional requirements define the platform's performance, availability, and usability targets governing all use cases:

*Table 2. Non-Functional Requirements Summary*

| ID | Quality Attribute | Verification Target |
|---|---|---|
| **RN1** | Performance | Page load under 500 ms for boards with up to 200 items. |
| **RN2** | Availability | Monthly availability of >= 99.5%, excluding announced maintenance. |
| **RN3** | Usability | Responsive interface supporting viewport widths down to 375 px. |
| **RN4** | Scalability | Support up to 50,000 active tasks per workspace without degradation. |
| **RN5** | Recoverability | Daily database backups with RPO < 24 hours. |
| **RN6** | Internationalization | Localization in English and Portuguese. |
| **RN7** | Interoperability | Secure API communication with external payment gateway. |
| **RN8** | Tenant Isolation | Strict logical database segregation across workspaces. |

---

## 6. Conclusions

The system use case model establishes an exhaustive, literature-aligned functional baseline for TinyTask SaaS:
1. **Total Sea-Level Fidelity:** 18 Level-1 use cases cleanly cover all operational capabilities without leaf-node noise or micro-UI procedural scripts.
2. **Exhaustive Behavioral Contracts:** Each use case specifies pre/post conditions, black-box main success scenarios, and branching alternative/exception flows.
3. **Visual UML Coverage:** Every macro capability is illustrated with an error-free, native Markdown UML Use Case diagram.
4. **Seamless Sequential Traceability:** Direct 1:1 mapping from `Doc01` requirements (`R1.1`–`R8.2`) and PUCs (`PUC 1.1`–`PUC 8.2`) to System Use Cases (`{U.C. 1.1}`–`{U.C. 8.2}`).
5. **AEGIS Phase 3 Synthesis Ready:** Provides a rich, verified functional canvas for attack surface mapping, trust boundary analysis, and regulatory requirement derivation.

---

## 7. Bibliography

- Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley Professional.
- Larman, C. (2004). *Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development* (3rd ed.). Prentice Hall.
- Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process: Getting Requirements Right* (3rd ed.). Addison-Wesley Professional.
- Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
- Object Management Group (OMG). (2017). *OMG Unified Modeling Language (OMG UML) Version 2.5.1*.
- Centro de Computação Gráfica (CCG) & PIEP. (2023). *E1.2 – GPTools_AnáliseRequisitos_CasosDeUso_V4.0: Especificação de Casos de Uso e Decomposição Funcional*. Guimarães, Portugal.

---

## Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| **1.0.0** | 2026-09-23 | Requirements Engineering Agent | Initial baseline System Use Cases (GPTools E1.2 model). |
| **2.0.0** | 2026-09-23 | Requirements Engineering Agent | Pure functional alignment, active English verbs, zero leaf nodes. |
| **2.1.0** | 2026-09-23 | Requirements Engineering Agent | Consolidated to 18 Sea-Level use cases matching consolidated business requirements. |
| **3.0.0** | 2026-09-23 | Requirements Engineering Agent | Literature-grounded overhaul (Cockburn, Larman, Wiegers) with full pre/post conditions, main success scenarios, and extension flows for all 18 use cases. |
| **3.1.0** | 2026-09-23 | Requirements Engineering Agent | Added visual UML Use Case diagrams in native Markdown for each macro capability cluster, removing sequence diagrams. |
