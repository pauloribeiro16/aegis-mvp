# Evaluation Checklist — Fail-Safe Defaults & Closed Failure States

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-04`.

---

## 1. Default-Deny Decision Logic (`PRIN-ENG-04`)

- [ ] **Affirmative Assertion Gate:** Use case success scenarios require explicit, affirmative validation of all prerequisites; absence of evidence is treated as denial.
- [ ] **No Fallthrough on Failure:** Alternative flows terminate in explicit refusal rather than falling through to subsequent operational steps.

---

## 2. Fail-Closed Resilience & Rollbacks (`PRIN-ENG-04`)

- [ ] **External Outage Fail-Closed:** Timeouts, unreachable services, or unconfirmed payments terminate in a closed, safe state with zero unauthorized permissions granted.
- [ ] **Atomic Transaction Rollback:** Multi-step operations specify that intermediate modifications roll back completely if a subsequent step fails.
- [ ] **Opaque User Errors:** Failure branches specify sanitized, non-revealing error messages to users rather than leaking internal system or database details.
