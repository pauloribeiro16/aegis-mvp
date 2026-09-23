# End-to-End Case Studies — Fail-Safe Defaults & Closed Failure States

Comprehensive before-and-after evaluations of functional Use Cases (`UC-*`) against `PRIN-ENG-04`.

---

## Case Study 1: User Account Registration & Organization Binding (`UC-01b`)

### Initial (Flawed) Functional Use Case

```markdown
### Use Case: UC-01b — User Registration with Organization Joining
- **Primary Actor:** New User
- **Pre-conditions:** User possesses an invitation token to join an organization.
- **Trigger:** User submits registration form with email, password, and invitation token.
- **Data Exchanged:** Email, Password, Invitation Token.

#### Main Success Scenario:
1. User submits registration details.
2. System creates user account record.
3. System attempts to bind user account to organization and allocate licensed seat.
4. System issues confirmation receipt and logs user in.

#### Failure Scenarios:
- 3a. Organization has zero available seats left: System displays error message stating "Organization full, but account created successfully".
```

---

### Step-by-Step Analytical Evaluation

1. **Step 2 & 3 Finding — Partial State Orphan Hazard (`PRIN-ENG-04`):**  
   *Analysis:* If Step 3 aborts because the organization has no seats left, Step 2 already persisted the user account. The user is left in an orphaned "half-registered" state without organization membership, cluttering the identity database and confusing the user.
2. **Missing Atomic Transaction:**  
   *Analysis:* Registration and organization binding must succeed or fail as an indivisible unit.

---

### Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-FAIL-020` (Atomic Registration Rollback):  
  *If* organization binding or seat validation fails during invited user registration, *then the* Identity Management Subsystem *SHALL* roll back account creation completely, leaving zero persistent state.

---

### Remediated Functional Use Case (`UC-01b`)

```markdown
### Use Case: UC-01b — User Registration with Organization Joining (Hardened)
- **Primary Actor:** New User
- **Pre-conditions:** User holds a valid, non-expired invitation token.
- **Trigger:** User submits registration form.
- **Data Exchanged:** Email, Password, Invitation Token.

#### Main Success Scenario:
1. User submits registration form with invitation token.
2. System verifies token validity, expiration window, and organization seat availability within an atomic transaction.
3. System creates user credentials and binds user to the target organization simultaneously.
4. System invalidates the invitation token to prevent reuse.
5. System confirms registration and initiates user onboarding.

#### Failure Scenarios:
- 2a. Token invalid, expired, or organization has zero available seats: System fails closed, aborts registration transaction with zero state persisted, and displays clear error message to User.
```
