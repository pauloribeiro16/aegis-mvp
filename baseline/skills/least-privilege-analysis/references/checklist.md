# Evaluation Checklist — Least Privilege & Mechanism Isolation

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-03`.

---

## 1. Role Capability Scoping (`PRIN-ENG-03`)

- [ ] **Role Proportionality:** The operational verbs allowed in the use case correspond strictly to the legitimate mandate of the assigned actor role.
- [ ] **Separation of Operational and Administrative Flows:** Administrative capabilities (retention, billing, global deletions) are excluded from standard collaboration use cases.
- [ ] **Read-Only Actor Integrity:** Actors assigned read-only roles (e.g. Viewers, Auditors) cannot initiate state-mutating actions in any step.

---

## 2. Internal Processing Scoping (`PRIN-ENG-03`)

- [ ] **Sub-Task Authority Bounding:** Background processors, notification dispatchers, and indexing tasks operate with permissions bounded strictly to their immediate data inputs.
- [ ] **Tenant Mechanism Isolation:** Multi-tenant processing steps ensure that execution contexts and queues are strictly partitioned by tenant identity.
