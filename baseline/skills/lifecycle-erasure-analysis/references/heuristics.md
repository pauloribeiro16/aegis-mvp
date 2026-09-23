# Analytical Heuristics — Data Lifecycle & Irreversible Erasure

Detailed technical heuristics for inspecting data retention, deletion cascades, and backup tombstoning against `PRIN-PRV-02` and `PRIN-PRV-04`.

---

## 1. Cryptographic Erasure (Crypto-Shredding) Heuristic (PRIN-PRV-02)

### Rule 1.1: Per-Entity Key Wrapping
- For large-scale data sets, multi-tenant databases, or immutable backup media (e.g. S3 Glacier, WORM storage):
  1. Personal data must be encrypted with a dedicated Data Encryption Key (DEK).
  2. The DEK must be wrapped by a Key Encryption Key (KEK) associated specifically with the user or tenant.
  3. Irreversible erasure is achieved by destroying the KEK/DEK in the KMS. Once the key is deleted, ciphertext across all database snapshots, replication streams, and cold backups becomes unrecoverable mathematical noise.

---

## 2. Cascade Deletion & Referential Integrity Heuristic (PRIN-PRV-02)

### Rule 2.1: Multi-Store Synchronous vs Asynchronous Cascades
- When a parent account or project is deleted:
  1. Direct relational dependencies (e.g. private drafts, individual settings) must be deleted via SQL `ON DELETE CASCADE`.
  2. Collaborative or financial audit trails that must be retained for legal/tax obligations (e.g. invoices, transaction logs) must have personal identifiers pseudonymized or replaced with synthetic hashes.
  3. Distributed assets (S3 buckets, search indices, cached sessions) must be purged via reliable, idempotent background queues (with dead-letter queues and retry metrics).

---

## 3. Disaster Recovery & Tombstone Replay Heuristic (PRIN-PRV-02)

### Rule 3.1: The Backup Resurrection Defense
- Restoring a database snapshot from cold storage must never re-activate deleted accounts:
  1. Maintain an immutable, append-only **Tombstone Ledger** stored separately from primary database snapshots (e.g. in an append-only S3 bucket with Object Lock or a dedicated DynamoDB table).
  2. The disaster recovery playbook must mandate a step:
     $$\text{Restore Snapshot} \longrightarrow \mathbf{Replay\ Tombstones} \longrightarrow \text{Open Ingress}$$
  3. Replaying the ledger ensures all deletions that occurred between snapshot capture and restore time are automatically re-applied before traffic resumes.

---

## 4. User Autonomy & Transparent Confirmation (PRIN-PRV-04)

### Rule 4.1: Self-Service Deletion & Portability
- The deletion mechanism must be directly accessible to the user without requiring human support intervention:
  1. Users must be able to download an archive of their data (data portability) prior to deletion in an open format (JSON, CSV).
  2. Deletion requests must require re-authentication (password or MFA challenge) to prevent malicious cross-site request forgery or accidental deletion.
  3. Upon completion, emit an immutable audit receipt confirming the timestamp of erasure.
