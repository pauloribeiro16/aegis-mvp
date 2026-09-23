# Evaluation Checklist — Trust Boundary & Complete Mediation

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-01`.

---

## 1. Boundary Demarcation in Use Cases (`PRIN-ENG-01`)

- [ ] **Explicit Execution Tiers:** Every use case step explicitly identifies the initiating actor and the mediating internal subsystem.
- [ ] **No Unmediated Access to Storage:** External actors never interact directly with persistent data stores, caches, or background queues.
- [ ] **Inter-Service Boundary Demarcation:** Asynchronous events and notifications explicitly carry verified caller and tenant context.

---

## 2. Complete Mediation & Multi-Tenancy (`PRIN-ENG-01`)

- [ ] **Localized Tenancy Assertion:** Every read, write, or delete step verifies that the target resource belongs to the actor's authorized workspace/tenant.
- [ ] **Role Authorization Verification:** Actions that alter configurations, invite users, or delete data require explicit verification of role permissions at the domain logic tier.
- [ ] **No Ambient / Perimeter-Only Trust:** Steps do not assume that an initial gateway authentication check grants blanket authorization to all downstream resources.
