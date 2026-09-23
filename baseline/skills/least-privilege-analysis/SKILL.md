---
name: least-privilege-analysis
description: Evaluates functional use cases (UC-*) to ensure actors and internal processing operations operate with strictly minimal authority, preventing ambient access or shared mechanism exposure.
---

# Least Privilege & Mechanism Isolation Analysis

Evaluates functional Use Cases (`UC-*`) to ensure that actor roles and internal processing steps operate strictly with the minimum authority necessary for their functional purpose, and that execution contexts are isolated across tenants.

> **Target Principle:**  
> - `PRIN-ENG-03` (Least Privilege & Mechanism Isolation — Saltzer & Schroeder)

---

## 1. Operational Mandate & Scope

The agent acts as an Authorization & Systems Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Actor Role Capabilities:** Evaluating the operational verbs (create, read, update, delete, configure, export) granted to each actor role in the use case.
- **Internal Processing Authority:** Ensuring internal asynchronous workers, notification dispatchers, and batch processors possess only the authority needed for their specific sub-task.
- **Tenant & Mechanism Separation:** Verifying that distinct tenant operations or sensitivity levels do not execute under shared, ambient operational credentials.

The analysis is **technology-agnostic**: it focuses on logical privileges, role capabilities, and resource boundaries rather than cloud provider IAM syntax.

---

## 2. Evaluation Procedure

1. **Role Authority Extraction:** For each actor and system component participating in the use case, extract the complete list of actions permitted.
2. **Minimal Authority Triage (`PRIN-ENG-03`):** Assess whether any granted action is broader than required to achieve the step's specific functional outcome (e.g. granting full workspace deletion capability to a user who only needs to archive a single task).
3. **Internal Component Scoping:** Confirm that background workers executing sub-tasks (e.g. PDF generation, email dispatch) do not have authority to alter unrelated domain entities (e.g. billing records or user accounts).
4. **Mechanism Isolation Audit:** Ensure that multi-tenant workflows isolate execution state and data access, prohibiting shared unpartitioned channels.
5. **Output Delivery:** Produce:
   - Step-by-Step Privilege Annotations.
   - Derived Atomic Security Requirements in EARS syntax.
   - Remediated Use Case Specification with scoped role capabilities.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-01`)

```markdown
### Use Case: UC-01 — User Profile Update and Workspace Settings
- **Primary Actor:** Workspace Collaborator
- **Pre-conditions:** Collaborator is logged into the workspace.
- **Trigger:** Collaborator navigates to settings page.
- **Data Exchanged:** Display Name, Notification Preferences, Workspace Default Retention Policy, Billing Contact.

#### Main Success Scenario:
1. Collaborator submits updated profile display name and workspace retention policy.
2. System receives submission and updates both the user's profile and the workspace configuration.
3. System triggers background indexing worker to update global search indexes.
4. System confirms update to Collaborator.

#### Failure Scenarios:
- 1a. Invalid input format: System prompts user to correct fields.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Step 1 & 2 Finding — Excessive Role Authority (`PRIN-ENG-03`):**  
   *Analysis:* A regular Workspace Collaborator is permitted to modify the `Workspace Default Retention Policy` and `Billing Contact`. These administrative capabilities exceed the collaborator's legitimate operational scope, violating least privilege.
   *Remediation:* Split the use case: profile updates belong to regular collaborators; workspace-level retention and billing modifications require an explicit Workspace Administrator role.
2. **Step 3 Finding — Unconstrained Background Worker Authority:**  
   *Analysis:* The background indexing worker should only have read access to published task text; it must not possess write authority to alter user profiles or workspace configurations.

---

### 3.3 Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-PRIV-001` (Role-Bounded Workspace Configuration):  
  *When* a workspace configuration change is submitted, *the* Workspace Governance Subsystem *SHALL* verify that the actor holds the Workspace Administrator role, rejecting submissions from standard collaborators.
- `REQ-SEC-PRIV-002` (Worker Authority Scoping):  
  *While* processing search index tasks, *the* Search Indexing Subsystem *SHALL* operate with read-only authority restricted to public workspace content, with zero write permissions on user account or billing data.

---

### 3.4 Remediated Functional Use Case (`UC-01`)

```markdown
### Use Case: UC-01 — User Profile Update (Hardened)
- **Primary Actor:** Authenticated User
- **Pre-conditions:** User holds an active session.
- **Trigger:** User submits profile update form.
- **Data Exchanged:** Display Name, Avatar reference, Notification Preferences.

#### Main Success Scenario:
1. User submits profile changes (scoped strictly to personal attributes).
2. System validates input constraints and updates personal profile record.
3. System confirms update to User.

*(Note: Workspace configuration and retention policies are relocated to dedicated administrative Use Case `UC-ADM-01` restricted to Workspace Administrators).*
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic role scoping heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for functional flow over-privilege smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete Use Case privilege reduction walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured least privilege checklist.
