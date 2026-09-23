---
name: fail-safe-defaults-analysis
description: Evaluates functional use cases (UC-*) to ensure exception paths, missing preconditions, and dependency outages default to refusal (fail closed) without leaking diagnostic state.
---

# Fail-Safe Defaults & Closed Failure Analysis

Evaluates functional Use Cases (`UC-*`) to verify that all failure branches, missing preconditions, and external dependency outages terminate in a secure closed state without exposing internal system details or causing partial state corruption.

> **Target Principle:**  
> - `PRIN-ENG-04` (Fail-Safe Defaults & Closed Failure States — Saltzer & Schroeder / OWASP)

---

## 1. Operational Mandate & Scope

The agent acts as a Systems Reliability & Resilience Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Precondition Failures:** How the use case responds when mandatory preconditions (authentication, active subscription, required permissions) are unsatisfied.
- **Alternative & Exception Branches:** Ensuring alternative branches terminate in explicit refusal rather than implicit pass-through.
- **External Dependency Outages:** Verifying that failures or timeouts of external services (identity providers, payment gateways, notification delivery) fail closed.
- **State Rollback Semantics:** Confirming that multi-step transactions roll back fully if an intermediate step aborts.

The analysis is **technology-agnostic**: it audits functional decision branches and state rollback requirements without prescribing specific middleware or programming constructs.

---

## 2. Evaluation Procedure

1. **Failure Branch Inventory:** Extract all failure scenarios, validation aborts, and exception paths documented in the use case.
2. **Default-Deny Verification (`PRIN-ENG-04`):** Confirm that any condition not explicitly matching a success rule defaults to refusal of access.
3. **Fail-Closed Dependency Audit:** For any step relying on an external service or internal subsystem, determine the system's behavior if that component times out or raises an error. Verify that the flow fails closed (rejects the transaction) rather than failing open.
4. **State Consistency & Atomic Rollback:** Confirm that if a multi-step mutation (e.g. creating a workspace and allocating seats) fails midway, previous partial mutations are completely undone.
5. **Output Delivery:** Produce:
   - Step-by-Step Failure Handling Annotations.
   - Derived Atomic Security Requirements in EARS syntax.
   - Remediated Use Case Specification with explicit fail-closed branches.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-05`)

```markdown
### Use Case: UC-05 — Subscription Seat Allocation
- **Primary Actor:** Workspace Administrator
- **Pre-conditions:** Workspace exists.
- **Trigger:** Administrator purchases 5 additional seats.
- **Data Exchanged:** Workspace ID, Seat Count, Payment Details.

#### Main Success Scenario:
1. Administrator submits purchase request for additional seats.
2. System updates workspace record to reflect new seat quota.
3. System requests payment charge from external Payment Gateway.
4. System confirms successful seat expansion to Administrator.

#### Failure Scenarios:
- 3a. External Payment Gateway times out or is unreachable: System assumes payment will complete later and leaves new seats active to avoid disrupting the customer.
- 3b. Payment declined: System leaves seats active but sends warning email.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Step 2 Finding — Inverted State Mutation Order (`PRIN-ENG-04`):**  
   *Analysis:* Step 2 increments the seat quota *before* payment is verified in Step 3. If Step 3 aborts or times out, the user receives free seats without payment.
2. **Failure Branch 3a & 3b Finding — Fail-Open Vulnerability:**  
   *Analysis:* Leaving seats active when payment fails or times out violates fail-safe defaults. The system fails open under error conditions, causing commercial and security exposure.
   *Remediation:* Reorder steps so payment verification gates seat allocation. If payment fails or times out, the system must fail closed: no seats are allocated, and the transaction is aborted.

---

### 3.3 Derived Atomic Security Requirements (EARS Syntax)

- `REQ-SEC-FAIL-001` (Fail-Closed Payment Gating):  
  *When* a seat allocation purchase is requested, *the* Subscription Management Subsystem *SHALL* verify successful payment settlement before incrementing the workspace seat quota, terminating in a closed rejection state if payment is not confirmed.
- `REQ-SEC-FAIL-002` (Atomic Transaction Rollback):  
  *If* any step of a multi-tier allocation workflow fails, *then the* System *SHALL* roll back all intermediate modifications, leaving workspace quotas in their pre-transaction state.

---

### 3.4 Remediated Functional Use Case (`UC-05`)

```markdown
### Use Case: UC-05 — Subscription Seat Allocation (Hardened)
- **Primary Actor:** Workspace Administrator
- **Pre-conditions:** Administrator holds verified billing authority for the target workspace.
- **Trigger:** Administrator submits purchase request for additional seats.
- **Data Exchanged:** Workspace ID, Requested Seat Count, Payment Token.

#### Main Success Scenario:
1. Administrator submits seat expansion request.
2. System validates billing permissions and verifies payment authorization with external Payment Gateway.
3. Upon confirmed payment authorization, System atomically increments the workspace seat quota.
4. System issues receipt confirmation to Administrator.

#### Failure Scenarios:
- 2a. Payment authorization declined, timed out, or unconfirmed: System fails closed, aborts transaction without updating seat quota, and notifies Administrator of payment failure.
- 3a. Internal persistence failure occurs: System rolls back seat allocation, voids payment authorization, and emits opaque transaction error.
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic fail-closed heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for fail-open and partial-state functional smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete Use Case failure flow walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured fail-safe defaults checklist.
