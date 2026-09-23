# Analytical Heuristics — Trust Boundary & Complete Mediation

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-01`.

---

## 1. Boundary Demarcation in Use Cases (PRIN-ENG-01)

### Rule 1.1: Explicit Interaction Tiers
- Every step of a functional use case must explicitly identify which conceptual tier executes the action:
  - *Actor Tier:* Browser, Mobile App, External Third Party.
  - *Ingress / Gateway Tier:* Session validation, rate limiting, initial routing.
  - *Core Domain Tier:* Business invariants, tenancy verification, authorization.
  - *Data / Storage Tier:* Persistence of state, cryptographic operations.

### Rule 1.2: No Direct Actor-to-Storage Paths
- A use case step must never depict an external actor or gateway reading from or writing to storage directly. All storage interactions must be mediated by the Core Domain Tier.

---

## 2. Complete Mediation Heuristic (PRIN-ENG-01)

### Rule 2.1: Localized Tenancy & Resource Authorization
- In multi-tenant systems, the fact that an actor is authenticated is insufficient to authorize data access.
- Every read or write step must evaluate:
  $$\text{Authorize}(\mathtt{ActorID}, \mathtt{Action}, \mathtt{ResourceID}) \ \wedge \ \mathtt{BelongsTo}(\mathtt{ResourceID}, \mathtt{ActorTenantID})$$
- If a use case step fetches an object by identifier alone without verifying tenancy, it violates Complete Mediation.

### Rule 2.2: Mediated Inter-Component Communication
- Background tasks, queues, and event consumers must receive explicit, verified contextual payloads. Use cases must not depict components querying or modifying state under unmediated shared authority.
