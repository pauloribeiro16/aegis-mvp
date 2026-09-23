# End-to-End Case Studies — Data Lifecycle & Irreversible Erasure

Realistic before-and-after scenarios evaluating GDPR right to erasure cascades, cryptographic shredding, and backup tombstoning.

---

## Case Study 1: Multi-Tenant SaaS Right to Erasure Cascade & Backup Tombstone

### Context
A multi-tenant SaaS user exercises their GDPR Art. 17 right to erasure. The platform stores records in PostgreSQL, uploaded images in AWS S3, and takes daily RDS snapshots with a 30-day retention window.

### Initial (Non-Compliant) Process
1. Web endpoint executes:
   ```sql
   UPDATE users SET status = 'deleted' WHERE id = 'usr_542';
   ```
2. The user is logged out.
3. All tasks, project comments, and uploaded files in S3 are preserved untouched.
4. Backups continue to capture the user's plain-text records.

### Analysis & Non-Compliance Findings
- **Failure of Erasure (`PRIN-PRV-02`):** The personal data is merely hidden from immediate UI queries (`WHERE status != 'deleted'`). It remains fully accessible to DB administrators and raw SQL reports.
- **Orphan Accumulation (`PRIN-PRV-02`):** Files uploaded to S3 (profile avatars, attachments containing sensitive documents) are never scheduled for deletion.
- **Resurrection Hazard (`PRIN-PRV-02`):** If the database is restored from a backup next month, the account can be queried in full.

---

### Remediated Architecture & Process

#### 1. Multi-Store Cascading Deletion Transaction
```python
def execute_gdpr_erasure(user_id: str, db: Session, s3_client):
    # Step 1: Query all S3 keys owned by user
    attachments = db.query(Attachment).filter(Attachment.user_id == user_id).all()
    for att in attachments:
        s3_client.delete_object(Bucket=att.bucket_name, Key=att.s3_key)
    
    # Step 2: Delete private task records
    db.query(Attachment).filter(Attachment.user_id == user_id).delete()
    db.query(PersonalNote).filter(PersonalNote.user_id == user_id).delete()
    
    # Step 3: Irreversibly anonymize collaborative records
    anon_email = f"erased_{hashlib.sha256(user_id.encode()).hexdigest()[:16]}@deleted.local"
    db.query(User).filter(User.id == user_id).update({
        "email": anon_email,
        "full_name": "Erased Account",
        "password_hash": "ERASED",
        "is_deleted": True,
        "deleted_at": datetime.now(timezone.utc)
    })
    
    # Step 4: Record immutable tombstone
    tombstone = DeletionTombstone(
        user_id=user_id,
        anonymized_hash=anon_email,
        erased_at=datetime.now(timezone.utc)
    )
    db.add(tombstone)
    db.commit()
    
    # Step 5: Export tombstone to append-only DR recovery S3 bucket
    s3_client.put_object(
        Bucket="tinytask-disaster-recovery-tombstones",
        Key=f"tombstones/{user_id}.json",
        Body=tombstone.to_json()
    )
```

#### 2. Backup Restoration Playbook Integration
Whenever an RDS snapshot is restored into staging or production, the automated orchestrator runs:
```bash
python scripts/dr_replay_tombstones.py --tombstone-bucket tinytask-disaster-recovery-tombstones
```
This re-applies all deletion actions, ensuring restored snapshots never resurrect erased users.

### Remediation Ledger

| Target Store | Initial State | Risk | Remediated State | Principle |
|---|---|---|---|---|
| User Record | `status = 'deleted'` | PII retained in plain text | **Cryptographically anonymized** (`deleted_<hash>@...`) | `PRIN-PRV-02` |
| S3 Attachments | Orphaned indefinitely | Data retention violation | **Purged synchronously** via S3 API before commit | `PRIN-PRV-02` |
| DB Backups | Plaintext retained for 30d | Compliance resurrection on restore | **Immutable Tombstone Ledger** replayed upon DR restore | `PRIN-PRV-02` |
| User Experience | Support ticket required | Lack of user autonomy | **Self-service** deletion API with immediate confirmation receipt | `PRIN-PRV-04` |
