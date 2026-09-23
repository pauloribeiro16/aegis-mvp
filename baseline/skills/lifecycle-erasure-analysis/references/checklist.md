# Evaluation Checklist — Data Lifecycle & Irreversible Erasure

Comprehensive verification checklist for evaluating data retention, deletion cascades, and erasure workflows against `PRIN-PRV-02` and `PRIN-PRV-04`.

---

## 1. Deletion Completeness & Anonymization (`PRIN-PRV-02`)

- [ ] **No Raw Soft-Deletes:** Setting boolean flags (`is_deleted = true`) is accompanied by irreversible anonymization or hashing of all personal data fields (`email`, `full_name`, `phone`, `tax_id`).
- [ ] **Cryptographic Destruction of Passwords:** Password hashes and session tokens are overwritten with static sentinel values (e.g. `"ERASED"`).
- [ ] **Multi-Table Cascade:** Deletion triggers cascading deletes on user-owned private entities (personal tasks, private notes, direct messages).
- [ ] **Object Storage Purge:** All associated files, profile avatars, and attachments in cloud object storage (S3/GCS) are permanently deleted.

---

## 2. Backup & Disaster Recovery Tombstoning (`PRIN-PRV-02`)

- [ ] **Immutable Tombstone Ledger:** Erasure events are recorded in an append-only tombstone ledger stored independently of primary database snapshots.
- [ ] **Automated Restore Replay:** Disaster recovery procedures mandate the automated replay of tombstones against any restored snapshot prior to resuming production traffic.
- [ ] **Bounded Backup Retention:** Database snapshots and WAL logs have an automated retention ceiling (e.g. maximum 30 days) after which physical backup blocks are purged.
- [ ] **Crypto-Shredding Validation:** Where per-tenant or per-user keys are used, destroying the key in KMS renders historical backup data permanently undecryptable.

---

## 3. User Autonomy & Transparent Confirmation (`PRIN-PRV-04`)

- [ ] **Self-Service Deletion:** Account deletion is executable directly by the end-user via application settings without requiring customer support mediation.
- [ ] **Pre-Deletion Data Portability:** Users can export a complete machine-readable copy of their data (JSON/CSV) prior to confirming deletion.
- [ ] **Immediate Session Termination:** Triggering deletion immediately revokes all active JWTs, refresh tokens, and in-memory session caches.
- [ ] **Audit Confirmation:** The system provides an immutable timestamped confirmation confirming complete account erasure.
