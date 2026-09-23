# End-to-End Case Studies — Data Minimization & Privacy Balance

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-06`.

---

## Case Study 1: Task Management Collaborator Assignment (`UC-03c`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-03c — Assign Collaborator to Task
- **Primary Actor:** Project Manager
- **Pre-conditions:** Project exists with registered collaborators.
- **Trigger:** Manager selects a collaborator from the member dropdown.
- **Data Exchanged:** Task ID, Selected Member ID, Member Email, Member Phone, Member Internal Risk Score.

#### Main Success Scenario:
1. Manager selects collaborator to assign.
2. System updates task record with assignee ID.
3. System presents task view to all project collaborators, rendering the assignee's full profile (including email, phone, and risk score).

#### Failure Scenarios:
- 1a. Member ID invalid: System displays error.
```

---

### Step-by-Step Analytical Evaluation

1. **`Data Exchanged` Finding — Unnecessary Administrative & Contact Data (`PRIN-ENG-06`):**  
   *Analysis:* Passing `Member Phone` and `Member Internal Risk Score` during task assignment is completely irrelevant to assigning a task.
2. **Step 3 Finding — Excessive Egress Exposure:**  
   *Analysis:* Rendering private phone numbers and security risk scores to all project collaborators breaches confidentiality and violates data minimization.

---

### Derived Atomic Privacy Requirements (EARS Syntax)

- `REQ-PRV-MIN-020` (Task Assignee Data Scoping):  
  *When* assigning a collaborator to a task, *the* Task Management Service *SHALL* exchange only the opaque collaborator identifier and task identifier, strictly excluding private contact or risk metadata.
- `REQ-PRV-MIN-021` (Public Collaborator Card Projection):  
  *When* rendering collaborator assignments on task cards, *the* System *SHALL* display only the collaborator's public display name and avatar, withholding email addresses and system scores from team views.

---

### Remediated Functional Use Case (`UC-03c`)

```markdown
### Use Case: UC-03c — Assign Collaborator to Task (Hardened)
- **Primary Actor:** Project Collaborator with Management Rights
- **Pre-conditions:** Project and collaborator exist in authorized workspace.
- **Trigger:** Actor selects collaborator to assign to task.
- **Data Exchanged:** Task ID, Collaborator Identifier.

#### Main Success Scenario:
1. Actor submits task assignment with Task ID and Collaborator ID.
2. System verifies actor's permission to assign tasks within workspace.
3. System assigns collaborator to task.
4. System updates task display, projecting only the assignee's public display name and avatar.
5. System confirms assignment to Actor.
```
