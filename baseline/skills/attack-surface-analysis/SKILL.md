---
name: attack-surface-analysis
description: Evaluates functional use cases (UC-*) to minimize exposed entry points, eliminate unnecessary interaction triggers, and ensure peripheral callbacks match core security rigor.
---

# Attack Surface & Peripheral Resilience Analysis

Evaluates functional Use Cases (`UC-*`) to minimize exposed interaction entry points, eliminate unneeded operational triggers, and ensure auxiliary integration flows enforce equal protection as core user journeys.

> **Target Principle:**  
> - `PRIN-ENG-02` (Attack Surface Minimization & Peripheral Resilience — Howard & LeBlanc / Schneier)

---

## 1. Operational Mandate & Scope

The agent acts as a Security & Systems Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Use Case Metadata:** Primary and secondary actors, operational triggers, pre-conditions, and post-conditions.
- **Interaction Flows:** Main success scenarios, alternative branches, and exception flows.
- **Auxiliary Integration Paths:** Asynchronous notifications, third-party webhooks, batch ingest triggers, and operational telemetry flows.

The goal is to analyze the functional flow—**independent of specific programming languages, web frameworks, or cloud vendor products**—ensuring that every interaction point is strictly justified, that auxiliary integration triggers are hardened, and that unmediated entry points are eliminated from the functional design.

---

## 2. Evaluation Procedure

1. **Entry Point & Trigger Inventory:** Extract every external trigger, user-initiated action, and automated callback specified across the use case steps.
2. **Functional Necessity Triage:** For each trigger and data exchange step, assess whether direct public or external access is indispensable to fulfill the actor's primary functional goal.
3. **Peripheral & Auxiliary Flow Audit:** Identify secondary interaction paths (e.g. external event notifications, webhook callbacks, asynchronous status polling). Verify that they do not permit unauthenticated entry into core state transitions.
4. **Step-by-Step Flow Inspection:** Trace each step of the main scenario and alternative flows against `PRIN-ENG-02`. Flag steps that introduce ambient, unauthenticated, or unpruned entry vectors.
5. **Output Delivery:** Produce:
   - Step-by-Step Vulnerability & Risk Annotations.
   - Derived Atomic Security Requirements in EARS syntax.
   - Remediated Use Case Specification with hardened interaction steps.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-03`)

```markdown
### Use Case: UC-03 — Task Creation and File Attachment Ingestion
- **Primary Actor:** Workspace Collaborator
- **Pre-conditions:** Collaborator is logged into the platform.
- **Trigger:** Collaborator clicks "New Task" or invokes the task creation action.
- **Data Exchanged:** Task title, description, priority, deadline, optional file attachment, temporary workspace ID.

#### Main Success Scenario:
1. Collaborator initiates task creation.
2. The System allocates a temporary draft task ID accessible without authentication to allow quick sharing before final save.
3. Collaborator inputs task metadata and uploads an attachment file.
4. An external notification hook allows third-party services to inject task status updates directly into the active draft.
5. Collaborator confirms creation, and the System commits the task to the workspace.

#### Failure Scenarios:
- 3a. Attachment upload exceeds allowable size: System displays error to user.
- 4a. Third-party notification fails: System logs warning and continues.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Step 2 Finding — Unauthenticated Public Entry Point (`PRIN-ENG-02`):**
   - *Analysis:* Allocating a publicly accessible draft task ID before authentication introduces an unmediated public interaction vector. Attackers can harvest or enumerate draft IDs, inject garbage data, or exhaust storage resources.
   - *Remediation:* Eliminate the unauthenticated draft path. All task creation actions must execute strictly within an authenticated, workspace-scoped session.
2. **Step 4 Finding — Weak Peripheral Integration Hook (`PRIN-ENG-02`):**
   - *Analysis:* Allowing third-party services to inject task status updates via an unauthenticated external hook violates peripheral resilience. The peripheral hook is a weak link compared to the authenticated collaborator session.
   - *Remediation:* Impose explicit cryptographic authentication (mutual authentication or signed message proofs) on external integration triggers, and prohibit direct state manipulation on draft tasks.

---

### 3.3 Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-SURF-001` (Authenticated Task Ingress Gate):
  *When* a task creation request is received, *the* Ingress Mediation Subsystem *SHALL* verify that the request originates from an authenticated session belonging to a verified workspace member, rejecting unauthenticated requests before allocating task identifiers or storage.
- `REQ-SEC-SURF-002` (Peripheral Integration Origin Verification):
  *When* an external third-party notification triggers a task state update, *the* Integration Gateway *SHALL* cryptographically verify the sender's digital signature and timestamp freshness before passing the payload to task processing logic.

---

### 3.4 Remediated Functional Use Case (`UC-03`)

```markdown
### Use Case: UC-03 — Task Creation and File Attachment Ingestion (Hardened)
- **Primary Actor:** Verified Workspace Member
- **Pre-conditions:** Member possesses an authenticated, active session within the target workspace.
- **Trigger:** Member submits task creation data through the authenticated workspace interface.
- **Data Exchanged:** Task title, description, priority, deadline, optional attachment file.

#### Main Success Scenario:
1. Member submits task metadata and attachment file within their authenticated workspace session.
2. The System verifies the member's active session and validates that attachment parameters meet platform constraints.
3. The System commits the task record and stores the attachment within the member's workspace boundary.
4. The System notifies active workspace collaborators of task creation via internal event dispatch.

#### Failure & Auxiliary Scenarios:
- 1a. Session is unauthenticated or expired: System rejects request and redirects to authentication challenge.
- 2a. Attachment exceeds size bounds or fails validation: System aborts upload without persisting partial state.
- 3a. External integration callback received: System cryptographically validates sender signature and timestamp; if invalid, request is rejected with access denied.
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic heuristics on entry point pruning and peripheral trigger mediation.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for functional flow anti-patterns (unauthenticated temporary states, unmediated public hooks).
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete Use Case audit walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured Use Case attack surface checklist.
