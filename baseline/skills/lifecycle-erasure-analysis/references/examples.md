# End-to-End Case Studies — Data Lifecycle & Irreversible Erasure

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-07`.

---

## Case Study 1: Workspace Dissolution and Data Purge (`UC-02d`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-02d — Dissolve Workspace
- **Primary Actor:** Workspace Owner
- **Pre-conditions:** Workspace exists.
- **Trigger:** Owner requests workspace dissolution.
- **Data Exchanged:** Workspace ID, Confirmation.

#### Main Success Scenario:
1. Owner submits dissolution request.
2. System sets workspace status to "archived".
3. System hides workspace from user dashboards.
4. System confirms dissolution.

#### Failure Scenarios:
- 1a. User is not Workspace Owner: System halts action.
```

---

### Step-by-Step Analytical Evaluation

1. **Step 2 Finding — Indefinite Data Retention under Archival Label (`PRIN-ENG-07`):**  
   *Analysis:* Marking a workspace as "archived" retains all customer tasks, uploaded documents, comments, and member records indefinitely without an established retention ceiling or deletion schedule.
2. **Missing Cascading Disposal:**  
   *Analysis:* Fails to define a retention timeline for permanent destruction of underlying data and attachments.

---

### Derived Atomic Privacy Requirements (EARS Syntax)

- `REQ-PRV-LIFE-020` (Workspace Dissolution Cascade):  
  *When* a workspace dissolution is confirmed, *the* Data Lifecycle Subsystem *SHALL* schedule all associated tasks, project boards, and file attachments for irreversible purge after an optional 30-day grace recovery window.
- `REQ-PRV-LIFE-021` (Disaster Recovery Ledger Recording):  
  *When* executing the permanent purge of a dissolved workspace, *the* System *SHALL* record an immutable tombstone identifier in the disaster recovery ledger to prevent data resurrection upon snapshot restore.

---

### Remediated Functional Use Case (`UC-02d`)

```markdown
### Use Case: UC-02d — Dissolve Workspace (Hardened)
- **Primary Actor:** Workspace Owner
- **Pre-conditions:** Owner holds verified ownership authority; re-authentication completed.
- **Trigger:** Owner initiates dissolution and exports workspace archive.
- **Data Exchanged:** Workspace ID, Re-authentication Credentials, Export Choice.

#### Main Success Scenario:
1. Owner requests workspace dissolution and re-authenticates.
2. System provides complete data export archive (JSON/CSV with all attachments) to Owner.
3. Owner confirms permanent dissolution.
4. System transitions workspace to restricted grace-period status for 30 days (read-only, accessible solely to Owner for recovery).
5. Upon expiration of grace period, System irreversibly purges all workspace records, tasks, and stored file attachments across all tiers.
6. System commits deletion tombstone to the disaster recovery ledger.
7. System notifies Owner of final irreversible purge.
```
