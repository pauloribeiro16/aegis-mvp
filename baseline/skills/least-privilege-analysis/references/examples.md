# End-to-End Case Studies — Least Privilege & Mechanism Isolation

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-03`.

---

## Case Study 1: Task Commenting & Attachment Management (`UC-03b`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-03b — Add Comment and Attachment to Task
- **Primary Actor:** Workspace Viewer (Read-Only Role)
- **Pre-conditions:** Viewer has access to view tasks.
- **Trigger:** Viewer types comment and attaches file.
- **Data Exchanged:** Task ID, Comment Text, File Attachment.

#### Main Success Scenario:
1. Viewer submits comment and file.
2. System attaches comment and file to the task.
3. System updates task modification timestamp and re-indexes the entire workspace.
4. System confirms comment posted.

#### Failure Scenarios:
- 1a. File too large: System displays error.
```

---

### Step-by-Step Analytical Evaluation

1. **Step 1 & 2 Finding — Role Privilege Violation (`PRIN-ENG-03`):**  
   *Risk:* A user holding the `Viewer` (read-only) role is permitted to modify state by posting comments and uploading files. This breaks the role definition.
2. **Step 3 Finding — Excessive Processing Privilege:**  
   *Risk:* Updating a comment triggers a full re-indexing of the entire workspace, introducing denial-of-service risks through resource exhaustion.

---

### Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-PRIV-010` (Role-Constrained State Modification):  
  *When* a task comment or attachment is submitted, *the* Authorization Subsystem *SHALL* verify that the actor holds at least the Collaborator role, rejecting submissions from actors assigned to Viewer roles with access denied.
- `REQ-SEC-PRIV-011` (Incremental Worker Authority):  
  *When* a comment is created, *the* Indexing Subsystem *SHALL* operate with incremental authority restricted to the specific new comment entity, prohibiting full-workspace re-indexing.

---

### Remediated Functional Use Case (`UC-03b`)

```markdown
### Use Case: UC-03b — Add Comment and Attachment to Task (Hardened)
- **Primary Actor:** Verified Workspace Collaborator
- **Pre-conditions:** Collaborator holds an active session with write permissions on the target task.
- **Trigger:** Collaborator submits comment form with optional file attachment.
- **Data Exchanged:** Workspace ID, Task ID, Comment Text, File Attachment.

#### Main Success Scenario:
1. Collaborator submits comment and attachment.
2. Ingress Gateway validates active session and routes to Core Task Service.
3. Core Task Service verifies that actor holds Collaborator or higher role within the target workspace.
4. Core Task Service persists comment and commits attachment within the tenant's isolated storage quota.
5. Core Task Service dispatches scoped incremental update event to notification and indexing processors.
6. System confirms comment posted to Collaborator.

#### Failure Scenarios:
- 3a. Actor holds Viewer role: System rejects action with insufficient privilege.
```
