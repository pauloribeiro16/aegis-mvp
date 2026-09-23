---
name: lifecycle-erasure-analysis
description: Audits data retention, cascading deletion, object storage expiration, and cryptographic erasure to guarantee irreversible deletion across all operational tiers and backups.
---

# Data Lifecycle & Irreversible Erasure Analysis

Inspects relational database schemas, object storage lifecycle configurations, backup retention policies, and account deletion workflows to ensure personal data is irreversibly purged across all operational tiers in compliance with GDPR Art. 17 and privacy lifecycle standards.

> **Target Principle:**  
> - `PRIN-ENG-07` (End-to-End Lifecycle Security & Irreversible Erasure — Cavoukian / GDPR Art. 17)

---

## 1. Operational Mandate & Scope

The agent acts as a Data Protection & Database Reliability Architect reviewing:
- **Relational & NoSQL Data Models:** SQL foreign key constraints (`ON DELETE CASCADE` vs `RESTRICT`), table partitioning, soft-delete flags.
- **Object Storage & Cloud Buckets:** AWS S3 / GCP Cloud Storage bucket lifecycle rules, versioning policies, file deletion APIs.
- **Backup & Disaster Recovery Architectures:** Database snapshots, WAL archiving, backup restore pipelines, tombstone ledgers.
- **Self-Service Autonomy Interfaces:** Account deletion flows, data export (portability) APIs, user consent withdrawal mechanisms.

The objective is to verify that user deletion requests result in complete, irreversible data destruction across primary storage, secondary caches, object stores, and disaster recovery backups.

---

## 2. Evaluation Procedure

1. **Deletion Workflow Audit:** Trace the execution path triggered when a user or administrator requests account termination (`DELETE /api/v1/account`).
2. **Soft-Delete vs True Erasure Triage (`PRIN-PRV-02`):** Check if the system merely sets `is_deleted = true` without anonymizing or purging personal identifiers. If personal data remains in plain text, flag as a compliance violation.
3. **Multi-Store Cascade Verification:** Verify that deleting a user or project triggers cascading deletions across:
   - Primary relational database tables (tasks, comments, audit metadata).
   - Redis / in-memory cache keys (sessions, profile caches).
   - Object storage buckets (attachments, avatars, exported reports).
4. **Backup Resurrection Defense:** Inspect the disaster recovery restore procedure. Ensure that restoring a 14-day-old backup does not resurrect deleted user accounts (verify existence of a persistent, cryptographic Tombstone Ledger).
5. **Cryptographic Shredding Evaluation:** For high-scale or immutable storage, evaluate whether data is encrypted with a dedicated per-user/tenant key that can be destroyed in KMS to render data instantly irrecoverable across all historical backups.
6. **User Autonomy & Confirmation (`PRIN-PRV-04`):** Ensure user-initiated deletion is self-service, does not require customer support friction, and emits an immutable audit confirmation.
7. **Ledger Output:** Produce a Lifecycle & Erasure Audit Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Flawed Deletion Implementation

```python
# Application service handler
@app.delete("/api/v1/users/{user_id}")
def delete_user_account(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # SMELL 1: Soft-delete only. PII remains in plain text indefinitely
    user.is_deleted = True
    db.commit()
    
    # SMELL 2: Task comments, uploaded files in S3, and billing records are left untouched
    # SMELL 3: Redis user session remains active until TTL expiration
    return {"status": "user marked as deleted"}
```

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-PRV-02` (End-to-End Lifecycle Security):**
   - Setting `is_deleted = True` leaves name, email, and password hash permanently in the database. A breach or internal query still exposes this data.
   - Files uploaded by the user to S3 are never deleted, continuing to accrue storage costs and privacy exposure.
   - If the database is restored from a weekly snapshot, the user record is still completely intact.
2. **Violation of `PRIN-PRV-04` (Respect for User Autonomy):**
   - The user has no guarantee of erasure, active sessions are not immediately invalidated, and no cryptographic tombstone records the legal erasure event.

### 3.3 Remediated Erasure Architecture

```python
from datetime import datetime, timezone
import hashlib

@app.delete("/api/v1/users/{user_id}")
def delete_user_account(user_id: str, db: Session = Depends(get_db), s3=Depends(get_s3), redis=Depends(get_redis)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # 1. Immediate Session & Cache Invalidation
    redis.delete(f"session:{user_id}")
    redis.delete(f"profile_cache:{user_id}")
    
    # 2. Asynchronous S3 Object Purge
    purge_user_s3_assets(s3, bucket="tinytask-attachments", prefix=f"user_{user_id}/")
    
    # 3. Cascading Deletion of User-Owned Private Records
    db.query(TaskAttachment).filter(TaskAttachment.user_id == user_id).delete()
    
    # 4. Irreversible Anonymization of Collaborative Records
    user.email = f"erased_{hashlib.sha256(user_id.encode()).hexdigest()[:12]}@deleted.tinytask.local"
    user.display_name = "Deactivated User"
    user.password_hash = "ERASED"
    user.is_deleted = True
    
    # 5. Cryptographic Tombstone Recording (Replayed upon DB disaster recovery)
    tombstone = DeletionTombstone(
        entity_id=user_id,
        entity_type="user",
        erased_at=datetime.now(timezone.utc)
    )
    db.add(tombstone)
    db.commit()
    
    return {"status": "account permanently erased", "erased_at": tombstone.erased_at.isoformat()}
```

### 3.4 Lifecycle & Erasure Audit Ledger

| Component | Initial Handling | Finding / Non-Compliance | Remediated Handling | Principle |
|---|---|---|---|---|
| Database Record | `is_deleted = True` (Plain PII kept) | GDPR Art. 17 non-compliance; PII leakage | **Irreversible anonymization** + tombstone record | `PRIN-PRV-02` |
| S3 Storage Files | Orphaned indefinitely | Unbounded data retention | **Automated purge** of all S3 objects under user prefix | `PRIN-PRV-02` |
| Redis Sessions | Left to expire | Session hijack risk post-deletion | **Immediate invalidation** of session keys | `PRIN-PRV-04` |
| Backup Restore | User resurrected on snapshot recovery | Compliance resurrection hazard | **Tombstone Ledger replay** in DR pipeline | `PRIN-PRV-02` |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for crypto-shredding, backup tombstone architectures, and S3 lifecycle rules.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for soft-delete traps, orphan object accumulation, and backup resurrection flaws.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for multi-table cascade scripts and disaster recovery restore tombstone playbooks.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured lifecycle verification checklist.
