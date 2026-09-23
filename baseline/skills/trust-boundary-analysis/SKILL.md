---
name: trust-boundary-analysis
description: Evaluates functional use cases (UC-*) to verify that trust boundaries between actors, mediation points, and data tiers are explicit, authenticated, and enforce complete mediation.
---

# Trust Boundary & Complete Mediation Analysis

Evaluates functional Use Cases (`UC-*`) to ensure trust boundary crossings between actors, systems, and storage tiers are explicitly demarcated, authenticated, and enforce complete mediation without ambient authority.

> **Target Principle:**  
> - `PRIN-ENG-01` (Explicit Trust Boundaries & Complete Mediation — Shostack / Saltzer & Schroeder)

---

## 1. Operational Mandate & Scope

The agent acts as a Systems Security Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Actor Transitions:** Demarcating transitions between External Actors (e.g. anonymous visitor, authenticated workspace member, third-party service) and Internal System Components.
- **Mediation Points:** Verifying that data flows passing between execution tiers terminate at an explicit policy enforcement point.
- **Context & Tenancy Binding:** Ensuring that every interaction step explicitly asserts the actor's authorized tenancy and role rather than relying on perimeter-only trust.

The analysis is **technology-agnostic**: it evaluates logical boundaries, data flows, and mediation requirements without prescribing specific network protocols, programming frameworks, or database products.

---

## 2. Evaluation Procedure

1. **Zone & Boundary Mapping:** Identify the operational zones implied by the use case:
   - *Untrusted External:* User agents, public networks, third-party integrations.
   - *Perimeter Mediation:* Ingress gateways, authentication checkpoints.
   - *Core Application Logic:* Business workflows, task processors.
   - *Persistent Storage:* Customer data stores, file archives.
2. **Boundary Crossing Audit:** Trace every step in the use case where data or control transitions between zones.
3. **Complete Mediation Verification (`PRIN-ENG-01`):** Ensure that downstream processing steps do not trust incoming claims blindly. Every step that reads or modifies data must explicitly assert and verify resource ownership (e.g. verifying that the actor belongs to the target workspace).
4. **Step-by-Step Flow Inspection:** Flag any step where an actor accesses internal components without passing through mediation, or where identity context is assumed without verification.
5. **Output Delivery:** Produce:
   - Step-by-Step Boundary Risk Annotations.
   - Derived Atomic Security Requirements in EARS syntax.
   - Remediated Use Case Specification with explicit mediation steps.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-04`)

```markdown
### Use Case: UC-04 — Task Assignment and Team Notification
- **Primary Actor:** Workspace Member
- **Pre-conditions:** Member is logged into the application.
- **Trigger:** Member selects a task and assigns it to another collaborator.
- **Data Exchanged:** Task ID, Assignee ID, Optional notification note.

#### Main Success Scenario:
1. Member submits task assignment request with Task ID and Assignee ID.
2. System receives request at the edge gateway and validates user session.
3. Edge gateway forwards request directly to the internal database to update task assignment record.
4. Internal database notifies background notification service to email the assignee.
5. System confirms assignment to the Member.

#### Failure Scenarios:
- 2a. Session invalid: System rejects request.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Step 3 Finding — Missing Complete Mediation & Boundary Bypass (`PRIN-ENG-01`):**
   - *Analysis:* The edge gateway routes directly to the internal database or assumes that validating the user session is sufficient. The system does not verify whether the authenticated member actually belongs to the workspace that owns the Task ID (Insecure Direct Object Reference hazard).
   - *Remediation:* The request must pass to the Core Domain Logic, which must explicitly verify that the caller's tenancy matches the task's workspace before any database update is permitted.
2. **Step 4 Finding — Unmediated Inter-Component Trust:**
   - *Analysis:* The notification trigger assumes ambient authority. The notification service must receive a validated domain event carrying verified tenant and actor context, rather than raw unmediated triggers.

---

### 3.3 Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-BND-001` (Workspace Tenancy Complete Mediation):  
  *When* a task assignment action is requested, *the* Task Management Service *SHALL* verify that both the executing actor and the referenced task belong to the same authenticated workspace, rejecting unauthorized cross-tenant assignments with access denied.
- `REQ-SEC-BND-002` (Mediated Event Dispatch):  
  *When* dispatching notifications, *the* System *SHALL* transmit cryptographically signed internal event messages containing verified workspace context, prohibiting unmediated database-to-worker side-channels.

---

### 3.4 Remediated Functional Use Case (`UC-04`)

```markdown
### Use Case: UC-04 — Task Assignment and Team Notification (Hardened)
- **Primary Actor:** Verified Workspace Member
- **Pre-conditions:** Member is authenticated and belongs to the workspace owning the task.
- **Trigger:** Member submits task assignment through the workspace interface.
- **Data Exchanged:** Workspace ID, Task ID, Assignee ID, Notification note.

#### Main Success Scenario:
1. Member submits task assignment request.
2. Ingress Gateway validates active session and routes request to Core Task Service.
3. Core Task Service verifies complete mediation: asserts that the member has permission to assign tasks within the specific workspace owning the Task ID.
4. Core Task Service updates the task assignment record in persistent storage within an isolated tenant scope.
5. Core Task Service publishes an authenticated assignment event to the internal notification queue.
6. Notification Service receives the verified event and dispatches notification to the Assignee.
7. System confirms task assignment to the Member.

#### Failure Scenarios:
- 2a. Unauthenticated session: Ingress Gateway terminates request.
- 3a. Member lacks permission or task belongs to another workspace: Core Task Service rejects request with access denied.
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic boundary discovery and mediation heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for functional flow boundary bypasses and ambient authority smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete multi-tier Use Case audit walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured boundary checklist.
