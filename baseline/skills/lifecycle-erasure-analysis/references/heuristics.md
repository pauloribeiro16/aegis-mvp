# Analytical Heuristics — Data Lifecycle & Irreversible Erasure

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-07`.

---

## 1. Cascading Destruction in Functional Flows (PRIN-ENG-07)

### Rule 1.1: Complete Sub-Resource Cascade
- A functional use case specifying entity deletion must define the disposition of all dependent sub-resources:
  - Private assets owned by the entity $\implies$ **Permanent Destruction**.
  - Shared assets co-authored by the entity $\implies$ **Irreversible Anonymization**.
  - Billing/tax transaction archives $\implies$ **Pseudonymization with Strict Retention Bound**.

### Rule 1.2: Immediate Session Invalidation
- Triggering an account deletion must terminate all active sessions, authorization tokens, and cached credentials immediately at Step 1, preventing subsequent access during asynchronous cleanup.

---

## 2. Disaster Recovery Resilience & Tombstoning (PRIN-ENG-07)

### Rule 2.1: The Resurrection Invariant
- The functional design must ensure that restoring a past system snapshot does not re-activate an erased user.
- Every erasure event must generate an immutable, persistent tombstone record that survives snapshot restoration and enforces re-erasure during disaster recovery.
