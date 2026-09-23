# Anti-Patterns & Smells — Data Lifecycle & Irreversible Erasure

Concrete configuration smells and architectural anti-patterns that prevent effective data erasure or lead to compliance breaches.

---

## 1. "Soft-Delete as Erasure" Fallacy

### Bad Pattern: Boolean Flag without Anonymization

```sql
-- User deletion handler
UPDATE users SET is_deleted = TRUE, deleted_at = NOW() WHERE id = 'usr_123';
-- SMELL: Email, hashed password, billing name, and IP remain in plain text in the table
```

**Consequence:** A data breach 6 months later exposes records of users who believed their accounts were deleted. Regulators (GDPR Art. 17) treat this as unlawful data retention.

**Hardened Pattern:**

```sql
-- Irreversible anonymization on soft-delete
UPDATE users 
SET 
    email = CONCAT('deleted_', MD5(id::text), '@erased.local'),
    full_name = 'Deleted Account',
    password_hash = 'ERASED',
    phone = NULL,
    tax_identifier = NULL,
    is_deleted = TRUE,
    deleted_at = NOW()
WHERE id = 'usr_123';
```

---

## 2. Orphaned Cloud Storage Attachments

### Bad Pattern: Deleting Database Metadata while S3 Files Persist

```python
# API route handler
def delete_task_attachment(attachment_id):
    # SMELL: Deletes database row but leaves file in S3 forever
    db.execute("DELETE FROM attachments WHERE id = %s", [attachment_id])
    db.commit()
    return {"status": "deleted"}
```

**Consequence:** Leaked pre-signed URLs or compromised S3 buckets allow direct access to files that customers believed were destroyed.

**Hardened Pattern:**

```python
def delete_task_attachment(attachment_id, s3_client):
    attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if attachment:
        # Delete underlying S3 object first or within transactional saga
        s3_client.delete_object(
            Bucket=attachment.s3_bucket,
            Key=attachment.s3_key
        )
        db.delete(attachment)
        db.commit()
    return {"status": "deleted"}
```

---

## 3. Backup Restoration Resurrecting Deleted Users

### Bad Pattern: Restoring Database Snapshot Directly to Production

```bash
# Disaster recovery script
pg_restore -d tinytask_prod /backups/snapshot_2026_09_01.dump
# SMELL: Users who deleted their accounts between Sept 1 and Sept 23 are resurrected!
```

**Consequence:** Previously erased accounts become active again, re-subscribing users to marketing emails and exposing erased PII.

**Hardened Pattern:**

```bash
# Hardened disaster recovery sequence
pg_restore -d tinytask_prod /backups/snapshot_2026_09_01.dump
# Replay cryptographic tombstones to re-purge all deleted accounts
python /opt/scripts/replay_tombstones.py --db-uri postgresql://... --ledger s3://tinytask-audit-ledger/tombstones/
```
