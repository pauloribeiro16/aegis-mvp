---
name: lifecycle-erasure-analysis
description: Evaluates functional use cases (UC-*) to ensure personal data is irreversibly purged across all operational tiers and backups upon deletion triggers.
---

# Data Lifecycle & Irreversible Erasure Analysis

Evaluates functional Use Cases (`UC-*`) to verify that data lifecycle transitions, data retention limits, and account erasure requests result in complete, irreversible data destruction across primary storage, secondary caches, and disaster recovery backups.

> **Target Principle:**  
> - `PRIN-ENG-07` (End-to-End Lifecycle Security & Irreversible Erasure — Cavoukian / GDPR Art. 17)

---

## 1. Operational Mandate & Scope

The agent acts as a Data Protection & Systems Lifecycle Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Lifecycle Triggers:** Account deletion requests, workspace dissolution, data portability exports, and retention expiration events.
- **Cascading Deletion Workflows:** Ensuring that deleting a parent entity (e.g. account or workspace) triggers complete removal of associated child records, uploaded attachments, and activity logs.
- **Backup & Snapshot Resilience:** Verifying that the functional design prevents deleted personal data from being resurrected when restoring disaster recovery snapshots.

The analysis is **technology-agnostic**: it audits functional lifecycle flows and legal compliance guarantees without prescribing specific SQL statements, database engines, or cloud storage APIs.

---

## 2. Evaluation Procedure

1. **Lifecycle Trigger Inventory:** Identify all use case steps initiated by users or automated timers that request data deletion, account closure, or retention purges.
2. **Soft-Delete vs True Erasure Audit (`PRIN-ENG-07`):** Verify whether the use case merely marks an entity as "inactive" or "hidden" while retaining personal data in plain text. If personal data persists without irreversible anonymization, flag as a compliance violation.
3. **Multi-Store Cascade Tracing:** Ensure that the functional flow describes cascading deletion across:
   - Primary user profiles and private task records.
   - Associated file attachments and multimedia assets.
   - Shared collaborative activity feeds (which must be irreversibly pseudonymized/anonymized).
4. **Backup Resurrection Prevention:** Confirm the use case specifies an immutable deletion receipt (tombstone) that guarantees restored backups cannot resurrect erased accounts.
5. **Output Delivery:** Produce:
   - Lifecycle & Erasure Defect Annotations.
   - Derived Atomic Privacy Requirements in EARS syntax.
   - Remediated Use Case Specification with complete cascading erasure.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-06`)

```markdown
### Use Case: UC-06 — User Account Deletion
- **Primary Actor:** Authenticated User
- **Pre-conditions:** User possesses an active account.
- **Trigger:** User clicks "Delete Account" in profile settings.
- **Data Exchanged:** User ID, Confirmation confirmation checkbox.

#### Main Success Scenario:
1. User requests account deletion and confirms dialog.
2. System updates user status to "inactive".
3. System prevents user from logging in.
4. System confirms account closure.

#### Failure Scenarios:
- 1a. User cancels confirmation dialog: System returns to profile settings.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Step 2 Finding — Soft-Delete as Pseudo-Erasure (`PRIN-ENG-07`):**  
   *Analysis:* Marking an account as "inactive" does not delete personal data. The user's email, name, uploaded files, and comments remain stored in plain text. A future data breach or administrative report will expose their data, violating GDPR Art. 17 right to erasure.
   *Remediation:* The flow must mandate irreversible anonymization of the user profile and complete destruction of private assets.
2. **Missing Storage & Asset Purge:**  
   *Analysis:* Uploaded file attachments remain orphaned in storage, accumulating storage costs and privacy exposure.
3. **Missing Backup Resurrection Defense:**  
   *Analysis:* Restoring a database snapshot will bring the account back to life without record of the deletion request.

---

### 3.3 Derived Atomic Privacy Requirements (EARS Syntax)

- `REQ-PRV-LIFE-001` (Cascading Asset Destruction):  
  *When* an account deletion request is confirmed, *the* Data Lifecycle Subsystem *SHALL* permanently delete all private tasks, draft notes, and uploaded attachments owned by the user across all storage tiers within 24 hours.
- `REQ-PRV-LIFE-002` (Irreversible Profile Anonymization):  
  *When* executing account erasure, *the* Identity Subsystem *SHALL* replace all personal identifiers (email, full name, contact handles) with irreversible synthetic pseudonyms, rendering collaborative historical comments permanently unlinked to the individual.
- `REQ-PRV-LIFE-003` (Disaster Recovery Tombstone Assertion):  
  *While* maintaining disaster recovery snapshots, *the* System *SHALL* persist an immutable erasure tombstone ledger ensuring restored snapshots do not resurrect erased user identities.

---

### 3.4 Remediated Functional Use Case (`UC-06`)

```markdown
### Use Case: UC-06 — User Account Deletion and Right to Erasure (Hardened)
- **Primary Actor:** Authenticated User (Account Owner)
- **Pre-conditions:** User holds an active session; re-authentication completed.
- **Trigger:** User initiates account erasure request and provides security re-authentication.
- **Data Exchanged:** User ID, Authentication Challenge, Optional Export Format Request.

#### Main Success Scenario:
1. User requests account erasure; System verifies credentials via step-up re-authentication.
2. System offers immediate machine-readable data export (JSON/CSV) prior to permanent deletion.
3. User confirms irreversible erasure.
4. System terminates all active sessions and invalidates authentication credentials immediately.
5. System permanently purges private user records and associated file attachments across all storage tiers.
6. System irreversibly anonymizes user references in shared workspace comments with synthetic identifiers.
7. System records an immutable deletion tombstone in the disaster recovery ledger.
8. System issues final cryptographic confirmation receipt of erasure to User.

#### Failure Scenarios:
- 1a. Re-authentication fails: System halts erasure and logs security event.
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic lifecycle and tombstone heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for functional flow soft-delete and orphan asset smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete Use Case erasure walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured lifecycle checklist.
