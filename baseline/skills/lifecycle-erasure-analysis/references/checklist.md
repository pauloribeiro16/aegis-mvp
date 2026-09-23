# Evaluation Checklist — Data Lifecycle & Irreversible Erasure

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-07`.

---

## 1. Cascading Destruction in Use Cases (`PRIN-ENG-07`)

- [ ] **No Raw Soft-Deletes:** Entity deletion steps specify irreversible anonymization or purge of personal identifiers rather than mere status flag changes.
- [ ] **Comprehensive Cascade:** Deleting a parent account or workspace cascades to child tasks, comments, notes, and file attachments across all storage tiers.
- [ ] **Immediate Session Invalidation:** Initiating account deletion revokes active sessions and credentials immediately.

---

## 2. Disaster Recovery Resilience & User Rights (`PRIN-ENG-07`)

- [ ] **Disaster Recovery Tombstones:** Deletion flows generate persistent tombstone entries to prevent account resurrection during snapshot restoration.
- [ ] **Pre-Deletion Data Portability:** Users are provided an opportunity to export their personal data in an open, structured format prior to permanent deletion.
- [ ] **Audit Receipt:** The system provides an immutable audit confirmation of completed erasure to the requesting actor.
