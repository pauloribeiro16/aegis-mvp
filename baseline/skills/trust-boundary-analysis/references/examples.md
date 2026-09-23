# End-to-End Case Studies — Trust Boundary & Complete Mediation

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-01`.

---

## Case Study 1: Multi-Tenant Workspace Invitation (`UC-02`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-02 — Workspace Member Invitation
- **Primary Actor:** Authenticated User
- **Pre-conditions:** User possesses an active account.
- **Trigger:** User enters an email address and role to invite a collaborator to a workspace.
- **Data Exchanged:** Target Workspace ID, Invitee Email, Assigned Role.

#### Main Success Scenario:
1. User submits invitation details with Workspace ID, Invitee Email, and Role.
2. Ingress Gateway receives request and checks that User's session token is valid.
3. System inserts invitation record into database for the specified Workspace ID.
4. System sends invitation link to Invitee Email.
5. System confirms invitation sent to User.

#### Failure Scenarios:
- 2a. User session invalid: System displays login screen.
```

---

### Step-by-Step Analytical Evaluation

1. **Step 3 Finding — Missing Complete Mediation on Workspace Boundary (`PRIN-ENG-01`):**  
   *Risk:* The gateway verifies that the user is logged in, but Step 3 executes the invitation insertion without verifying that the user is an **Administrator or Owner** of the specified Workspace ID. An authenticated member of Workspace A can invite malicious actors to Workspace B simply by modifying the `Workspace ID` parameter.
2. **Step 3 Finding — Absence of Privilege Boundary Check:**  
   *Risk:* Any user can assign the `Administrator` or `Owner` role to invitees without checking whether the user possesses the authority to grant that role.

---

### Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-BND-020` (Workspace Authorization Complete Mediation):  
  *When* a workspace invitation is requested, *the* Workspace Management Service *SHALL* verify that the authenticated actor holds an active administrative role within the target workspace, rejecting unauthorized requests before creating invitation records.
- `REQ-SEC-BND-021` (Role Delegation Ceilings):  
  *When* assigning a role to an invitee, *the* Workspace Management Service *SHALL* assert that the assigned role does not exceed the actor's own role privilege level.

---

### Remediated Functional Use Case (`UC-02`)

```markdown
### Use Case: UC-02 — Workspace Member Invitation (Hardened)
- **Primary Actor:** Workspace Administrator
- **Pre-conditions:** Administrator holds an active session with verified administrative rights in the target workspace.
- **Trigger:** Administrator submits invitation form with Invitee Email and Role.
- **Data Exchanged:** Workspace ID, Invitee Email, Assigned Role.

#### Main Success Scenario:
1. Administrator submits invitation request.
2. Ingress Gateway authenticates session and dispatches request to Core Workspace Service.
3. Core Workspace Service evaluates complete mediation: verifies that the actor holds administrative authority within the designated Workspace ID and that the assigned role does not exceed the actor's privilege tier.
4. Core Workspace Service generates a cryptographically random, single-use invitation token with a 72-hour expiration window.
5. Core Workspace Service commits invitation record scoped to the target workspace.
6. System dispatches invitation notification with secure acceptance link.
7. System records audit log entry and confirms invitation to Administrator.

#### Failure Scenarios:
- 2a. Unauthenticated session: Ingress Gateway rejects request.
- 3a. Actor lacks administrative role in target workspace: Core Workspace Service rejects request with access denied.
- 3b. Role exceeds actor's privilege tier: Core Workspace Service rejects request with invalid role delegation.
```
