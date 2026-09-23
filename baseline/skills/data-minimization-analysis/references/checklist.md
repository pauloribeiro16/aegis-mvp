# Evaluation Checklist — Data Minimization & Privacy Balance

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-06`.

---

## 1. Ingress Minimization in Use Cases (`PRIN-ENG-06`)

- [ ] **Functional Justification:** Every field listed under `Data Exchanged` is indispensable for the primary goal of the use case.
- [ ] **No Speculative Collection:** Fields collected for potential future marketing or unstated analytics are excluded from the use case.
- [ ] **Deferred Sensitivity:** Financial, billing, or physical identity details are deferred until the specific use case requiring them (e.g. checkout) is invoked.

---

## 2. Egress Scoping & Collaborator Views (`PRIN-ENG-06`)

- [ ] **Persona-Based Scoping:** Steps that display user data to collaborators project only public handles and avatars.
- [ ] **No Internal Metadata Exposure:** System risk scores, internal database identifiers, and security counters are excluded from user-facing screens.
- [ ] **Attribute Coarsening:** Contextual parameters (location, time) are coarsened to the minimum precision needed for functionality.
