---
name: data-minimization-analysis
description: Evaluates functional use cases (UC-*) to eliminate extraneous personal data collection, prevent excessive egress data exposure, and enforce purpose binding.
---

# Data Minimization & Privacy Balance Analysis

Evaluates functional Use Cases (`UC-*`) to ensure that data exchanged across interaction steps is strictly necessary for the primary functional purpose, preventing superfluous data collection at ingress and over-exposure at egress.

> **Target Principle:**  
> - `PRIN-ENG-06` (Proactive Data Minimization & Scoped Projection — Cavoukian / GDPR Art. 5)

---

## 1. Operational Mandate & Scope

The agent acts as a Privacy Engineer and Information Architect reviewing **Functional Use Cases (`UC-*`)**:
- **Data Exchanged Sections:** The inventory of data fields submitted by actors or returned by systems during use case execution.
- **Purpose Binding:** Verifying that every collected data attribute links directly to an active functional feature.
- **Egress Scoping:** Ensuring that interaction steps returning data to actors project only the minimal attributes required for that specific actor persona (e.g. public collaborator view vs private account owner view).

The analysis is **technology-agnostic**: it audits conceptual data dictionaries and functional flows without prescribing specific serialization formats (JSON/Protobuf) or ORM libraries.

---

## 2. Evaluation Procedure

1. **Use Case Data Field Extraction:** Extract all data fields listed under `Data Exchanged` and trace their role across the main scenario steps.
2. **Purpose Justification Triage (`PRIN-ENG-06`):** For each collected field, evaluate whether the use case can successfully achieve its functional outcome without that field. If a field is non-essential (e.g. phone number or birthdate collected for online project collaboration), flag it for removal.
3. **Egress Exposure Audit:** Inspect steps where the system displays or returns data to actors. Verify that internal metadata (security flags, internal IDs) and private collaborator attributes are not exposed to third parties.
4. **Coarsening & Privacy-Preserving Transformation:** Where an attribute is required for operational behavior (e.g. localized language or timezone), evaluate whether a coarse representation (e.g. country code or timezone offset) suffices instead of precise identifiers.
5. **Output Delivery:** Produce:
   - Data Field Justification & Minimization Annotations.
   - Derived Atomic Privacy Requirements in EARS syntax.
   - Remediated Use Case Specification with minimized data exchanges.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Functional Use Case (`UC-01`)

```markdown
### Use Case: UC-01 — User Registration and Onboarding
- **Primary Actor:** New User
- **Pre-conditions:** User has access to the public registration interface.
- **Trigger:** User submits account creation form.
- **Data Exchanged:** Email, Password, Full Legal Name, Phone Number, Date of Birth, Physical Mailing Address, Preferred Language.

#### Main Success Scenario:
1. User enters registration data and submits form.
2. System creates user record and stores all provided profile fields.
3. System sends email verification to user's email address.
4. System presents welcome dashboard displaying the user profile.

#### Failure Scenarios:
- 1a. Mandatory field left empty: System halts registration and prompts user.
```

---

### 3.2 Step-by-Step Analytical Evaluation

1. **`Data Exchanged` Finding — Superfluous Personal Data Collection (`PRIN-ENG-06`):**  
   *Analysis:* TinyTask is a digital collaboration tool. Collecting `Phone Number`, `Date of Birth`, and `Physical Mailing Address` during basic registration violates data minimization. None of these fields are needed to create an account, authenticate, or manage tasks.
   *Remediation:* Remove `Phone Number`, `Date of Birth`, and `Physical Mailing Address` from the registration data exchange. Retain only `Email`, `Password`, `Display Name`, and `Preferred Language`.
2. **Failure Branch 1a Finding — Coercive Mandatory Collection:**  
   *Analysis:* Requiring non-essential fields as mandatory preconditions for service access violates GDPR Art. 5(1)(c) and EDPB guidelines.

---

### 3.3 Derived Atomic Privacy Requirements (EARS Syntax)

- `REQ-PRV-MIN-001` (Registration Data Minimization):  
  *When* a new user account is registered, *the* Identity Subsystem *SHALL* accept only authentication credentials (email, password) and public display handle, prohibiting the mandatory collection of physical address, birthdate, or telephone numbers.
- `REQ-PRV-MIN-002` (Collaborator Profile Scoped Projection):  
  *When* rendering collaborator information within shared workspaces, *the* System *SHALL* project only display name and avatar reference, strictly omitting personal email addresses and contact information from non-administrative views.

---

### 3.4 Remediated Functional Use Case (`UC-01`)

```markdown
### Use Case: UC-01 — User Registration and Onboarding (Hardened)
- **Primary Actor:** New User
- **Pre-conditions:** User has access to the registration interface.
- **Trigger:** User submits account creation form.
- **Data Exchanged:** Email, Password, Display Name, Preferred Language.

#### Main Success Scenario:
1. User enters minimal credentials (Email, Password, Display Name).
2. System validates input constraints and creates user record with default restrictive privacy settings.
3. System issues verification dispatch to the provided email.
4. System presents onboarding dashboard.

#### Failure Scenarios:
- 1a. Missing credential or invalid email format: System prompts user to correct entry.
```

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for technology-agnostic data minimization heuristics.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for functional flow over-collection and exposure smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for complete Use Case data minimization walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured data minimization checklist.
