# Analytical Heuristics — Least Privilege & Mechanism Isolation

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-03`.

---

## 1. Role Capability Scoping (PRIN-ENG-03)

### Rule 1.1: Functional Role Boundary
- In any functional use case, the actor initiating an action must hold a role whose legitimate mandate encompasses that action:
  - *Standard User / Collaborator:* Read, create, update, and delete objects they own or that are assigned to them within an authorized workspace.
  - *Workspace Administrator:* Configure workspace-level settings, manage member invitations, audit collaborator roles.
  - *Billing / Account Owner:* Modify subscription tiers, update payment contracts, initiate legal account closure.

### Rule 1.2: Prohibited Bundling of Administrative & Operational Capabilities
- A single functional use case must not bundle normal end-user collaboration with privileged administration (e.g. updating task status while simultaneously modifying platform retention rules).

---

## 2. Mechanism & Worker Isolation (PRIN-ENG-03)

### Rule 2.1: Sub-Task Authority Minimization
- When a use case delegates execution to internal sub-processes (e.g. background notification, document conversion, telemetry export):
  1. The sub-process must be scoped strictly to the data objects required to execute the sub-task.
  2. The sub-process must not inherit the full authority of the calling actor or system administrator.

### Rule 2.2: Multi-Tenant State Isolation
- Use cases must explicitly separate tenant execution contexts. A step in one tenant's use case flow must never address, read, or alter another tenant's shared queues or state.
