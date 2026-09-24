# Step 2: Regulatory Cross-Cutting & Threat Derivation

> **Step ID:** STEP-02  
> **Inputs:**  
> - Step 1 Functional Asset & Boundary Audit  
> - Phase 2 `Doc01_Operational_Objectives.md` (35 Active Sub-Domains, `PO-*` & `SO-*`)  
> - Phase 2 `Doc02_Secure_Design_Principles.md` (7 Engineering Principles `PRIN-ENG-01` to `PRIN-ENG-07`)  
> **Output:** Cross-Cutting Regulatory & Threat Mapping Matrix  
> **Methodological Grounding:** STRIDE Threat Modeling (Shostack, 2014), Privacy by Design (Cavoukian, 2009), Saltzer & Schroeder (1975)  

---

## 1. Purpose & Methodological Rationale

Step 2 executes the systematic juxtaposition of upstream compliance and engineering rules (**Phase 2**) against the pure functional baseline (**Version 0**).

In the AEGIS methodology:
- **Phase 2 establishes *what the organization must achieve*** to satisfy regulatory mandates (GDPR, CRA) and secure design principles.
- **Phase 3 specifies *how software functionalities behave under constraint*** to enforce those objectives.

To prevent arbitrary or disconnected security requirements, Step 2 applies a rigorous **threat and privacy gap analysis** across each of the 8 functional areas, deriving the exact operational safeguards required.

---

## 2. Review of Upstream Phase 2 Driving Invariants

```text
+-----------------------------------------------------------------------------------+
|                        AEGIS PHASE 2 REGULATORY & DESIGN SPINE                    |
+-----------------------------------------------------------------------------------+
|  GDPR Regulatory Spine (PO-*)                        |  CRA Regulatory Spine (SO-*)            |
|  - PO-D-01.1-001: Data at Rest Cryptographic Protection| - SO-D-01.1-002: Secret Store Invariants|
|  - PO-D-01.2-001: Data in Transit Protection         |  - SO-D-02.1-002: Hardened Auth & RBAC  |
|  - PO-D-03.1-001: Privacy Audit Logging              |  - SO-D-02.2-002: Session Invalidation  |
|  - PO-D-06.1-001: Data Minimization                  |  - SO-D-03.1-002: Security Audit Logs   |
|  - PO-D-06.2-001: Data Subject Rights                |  - SO-D-05.1-002: Rate Limiting & DoS   |
|                                                      |  - SO-D-07.1-002: Input Sanitization    |
|                                                      |  - SO-D-08.1-002: Webhook Authentication|
+-----------------------------------------+-----------------------------------------+
|                  7 UNIVERSAL SECURE DESIGN PRINCIPLES (Doc02)                     |
|  PRIN-ENG-01: Explicit Trust Boundaries & Complete Mediation (Saltzer & Schroeder)|
|  PRIN-ENG-02: Attack Surface Minimization & Peripheral Resilience (Howard/Schneier)|
|  PRIN-ENG-03: Least Privilege & Mechanism Isolation (Saltzer & Schroeder)          |
|  PRIN-ENG-04: Fail-Safe Defaults & Closed Failure States (Saltzer & Schroeder)     |
|  PRIN-ENG-05: Atomic Verifiability & Unambiguous Acceptance Criteria (EARS/ISO)   |
|  PRIN-ENG-06: Default-On Privacy & Data Minimization by Construction (Cavoukian)  |
|  PRIN-ENG-07: Non-Repudiable Observability & Forensic Integrity (Schneier)        |
+-----------------------------------------------------------------------------------+
```

---

## 3. Cognitive Trajectory: Functional-Area-by-Functional-Area Threat & Regulatory Synthesis

### Functional Area 1: User Accounts & Authentication (`R1.1`, `R1.2` | `{U.C. 1.1}`, `{U.C. 1.2}`)
- **V0 Baseline Scope:** User registers, validates email link, logs in with credentials, edits profile.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Credential Stuffing / Brute Force):* Attackers script automated login attempts against the public ingress.
  - *Threat 2 (Plaintext Password Exposure):* Internal database dump reveals user credentials.
  - *Threat 3 (Session Hijacking):* Session tokens intercepted over unencrypted channels or persisting after logout.
  - *Privacy Threat 4 (Data Maximization):* Registration form unnecessarily demanding personal phone numbers or demographic data.
- **Phase 2 Driving Rules:**
  - `SO-D-01.1-002` + CRA (2)(d): Require credential confidentiality protected by state-of-the-art mechanisms; the mechanism selection is a design decision (no hashing scheme is named by the corpus).
  - `SO-D-02.2-002`: Requires secure cryptographic session management, termination upon established inactivity, and immediate invalidation on logout.
  - `PO-D-06.1-001` & `PRIN-ENG-06`: Mandates data minimization during onboarding (name, email, credentials only).
  - `PO-D-01.2-001`: Mandates state-of-the-art cryptographic protection for all data in transit across external and inter-service channels.
  - `SO-D-03.1-002` & `PRIN-ENG-07`: Mandates security audit logging of failed authentication attempts.
- **Synthesis Decisions:**
  - Derive `RN10` (Credential Hardening), `RN11` (Session Invalidation), `RN19` (Registration Minimization), `RN24` (Data in Transit Encryption), and `RN18` (Audit Logging).

### Functional Area 2: Workspaces and Teams (`R2.1`, `R2.2`, `R2.3` | `{U.C. 2.1}`, `{U.C. 2.2}`, `{U.C. 2.3}`)
- **V0 Baseline Scope:** User creates workspace with URL slug, invites members, assigns roles, consults metrics.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Cross-Tenant Data Leakage):* An authenticated user belonging to Tenant A modifies their request parameters (IDOR) to access or modify Tenant B's workspace.
  - *Threat 2 (Privilege Escalation):* Standard workspace member invokes administrative member-invitation or role-promotion APIs.
- **Phase 2 Driving Rules:**
  - `SO-D-02.1-002`, `PRIN-ENG-01`, `PRIN-ENG-03`: Mandates complete mediation and multi-tenant isolation on every database query.
  - `PRIN-ENG-04`: Fail-safe defaults (default-deny catch-all on unauthorized operations).
  - `SO-D-03.1-002`: Non-repudiable audit logging of all role modifications.
- **Synthesis Decisions:**
  - Derive `RN9` (Multi-Tenant Data Isolation) and `RN12` (Role-Based Access Control).

### Functional Area 3: Manage Projects (`R3.1`, `R3.2` | `{U.C. 3.1}`, `{U.C. 3.2}`)
- **V0 Baseline Scope:** Team members create projects and archive completed projects.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Unauthorized Project Mutation):* Guests or standard members modifying project settings or archiving active work.
  - *Threat 2 (Unbounded Project Creation):* Malicious users generating millions of empty project containers to exhaust storage.
- **Phase 2 Driving Rules:**
  - `SO-D-02.1-002`: RBAC role enforcement (Admin role required for lifecycle state changes).
  - `PRIN-ENG-01`: Tenant boundary isolation.
- **Synthesis Decisions:**
  - Bind `RN9` and `RN12` to project creation and archiving workflows.

### Functional Area 4: Manage and Execute Tasks (`R4.1`, `R4.2`, `R4.3` | `{U.C. 4.1}`, `{U.C. 4.2}`, `{U.C. 4.3}`)
- **V0 Baseline Scope:** Create tasks, transition states on Kanban boards, configure recurrence.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (API Resource Starvation):* Automated client firing 1,000 board transition requests per second, exhausting server connections.
  - *Threat 2 (Cross-Tenant Task Tampering):* Injecting foreign task IDs into state transition endpoints.
- **Phase 2 Driving Rules:**
  - `SO-D-05.1-002` & `PRIN-ENG-02`: Rate limiting and peripheral resilience against request flooding.
  - `SO-D-02.1-002`: Continuous tenant context evaluation.
- **Synthesis Decisions:**
  - Derive `RN17` (Inbound API Rate Limiting) and bind `RN9`.

### Functional Area 5: Collaborate on Deliverables (`R5.1`, `R5.2` | `{U.C. 5.1}`, `{U.C. 5.2}`)
- **V0 Baseline Scope:** Upload deliverable files (25 MB cap) and post Markdown task comments.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Malicious Binary Upload / Web Shell):* Attacker uploads `.php`, `.exe`, or HTML file masquerading as a PDF to achieve remote execution.
  - *Threat 2 (Stored Cross-Site Scripting - XSS):* Attacker injects `<script>` or event handlers into task comment text to hijack session cookies of other team members.
  - *Privacy Threat 3 (Indefinite Data Retention):* Deleted deliverable attachments remain stored on disk indefinitely.
- **Phase 2 Driving Rules:**
  - `SO-D-07.1-002` & `PRIN-ENG-02`: Input validation, magic-byte file signature validation, and context-aware output encoding.
  - `PO-D-06.1-001` & `PRIN-ENG-06`: Automated lifecycle expiration of orphaned file assets in accordance with retention schedules.
- **Synthesis Decisions:**
  - Derive `RN13` (File Upload Strict Validation), `RN14` (Untrusted Content Neutralization), and `RN25` (Orphan File Asset Cleanup).

### Functional Area 6: Track Activity History & Notifications (`R6.1`, `R6.2` | `{U.C. 6.1}`, `{U.C. 6.2}`)
- **V0 Baseline Scope:** Consult chronological audit trail on task cards; receive email notifications.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Audit Log Tampering / Erasure):* Malicious insider deleting historical records to cover up unauthorized actions.
  - *Privacy Threat 2 (Employee Surveillance & Purpose Creep):* Management using task activity logs to monitor employee keystrokes or productivity metrics without consent.
- **Phase 2 Driving Rules:**
  - `SO-D-03.1-002` & `PRIN-ENG-07`: Append-only, tamper-resistant security audit logs.
  - `PO-D-06.1-001` & `PRIN-ENG-06`: Purpose limitation on operational logs.
- **Synthesis Decisions:**
  - Derive `RN18` (Non-Repudiable Security Audit Logging) and `RN22` (Purpose Limitation).

### Functional Area 7: Manage Commercial Subscriptions (`R7.1`, `R7.2` | `{U.C. 7.1}`, `{U.C. 7.2}`)
- **V0 Baseline Scope:** Upgrade commercial tiers, handle payment sessions, enforce 7-day grace period.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Forged Billing Webhooks):* Attacker sending mock HTTP POST requests to TinyTask's webhook endpoint claiming an enterprise plan was paid.
  - *Threat 2 (Replay Attacks):* Re-submitting previous valid payment notifications to extend subscriptions fraudulently.
- **Phase 2 Driving Rules:**
  - `SO-D-08.1-002` & `PRIN-ENG-02`: Cryptographic message authentication verification on all external webhook notifications.
  - `SO-D-01.1-002` & `PRIN-ENG-03`: Cryptographic verification of billing state invariants before granting quotas.
- **Synthesis Decisions:**
  - Derive `RN15` (Cryptographic Billing Invariant Protection) and `RN16` (Cryptographic Webhook Origin Verification).

### Functional Area 8: Export Data and Close Accounts (`R8.1`, `R8.2` | `{U.C. 8.1}`, `{U.C. 8.2}`)
- **V0 Baseline Scope:** Export profile/workspace data archive and deactivate account.
- **Threat & Vulnerability Hypotheses:**
  - *Threat 1 (Post-Closure Token Re-use):* Deactivated user account continues accessing APIs using previously issued session tokens.
  - *Privacy Threat 2 (Incomplete Erasure):* Personal data remaining active in database backups and operational tables after account termination.
  - *Privacy Threat 3 (Third-Party Data Contamination):* Exporting workspace archives exposing personal contact details of unrelated individuals.
- **Phase 2 Driving Rules:**
  - `PO-D-06.2-001`: GDPR Art. 17 (Right to Erasure) and Art. 20 (Data Portability).
  - `PO-D-01.1-001`: Encryption at rest for generated export archives.
  - `SO-D-02.2-002`: Emergency server-side token invalidation upon account termination.
- **Synthesis Decisions:**
  - Derive `RN20` (Structured Data Portability), `RN21` (Irreversible Erasure & Pseudonymization), `RN23` (Encryption at Rest), and `RN11` (Immediate Token Invalidation).

---

## 4. Harmonization of Regulatory Tensions

In accordance with Phase 2 §2, TinyTask SaaS resolves two key operational tensions:
1. **Tension T-M-002 (Integrated Security & Privacy by Design):**
   - *Conflict:* CRA demands deep logging and system observability, while GDPR demands strict data minimization.
   - *Harmonized Specification:* `RN18` records security-relevant metadata (timestamp, user ID, IP address, action), while `RN19` and `RN21` ensure that personal descriptions, sensitive notes, and plaintext passwords are never included in log streams.
2. **Tension T-001 (Audit Retention vs. Right to Erasure):**
   - *Conflict:* GDPR Art. 17 grants users the right to delete their personal data, but financial and security audit trails must maintain historical integrity.
   - *Harmonized Specification:* `RN21` purges user contact information and credentials, while replacing historical authorship with an irreversible cryptographic pseudonym (`Deactivated User [ID: 9481]`), preserving system consistency without violating data subject rights.

---

## 5. Output Summary of Step 2

Step 2 successfully derives:
- **10 CRA Security Requirements:** Covering multi-tenancy, authentication, sessions, RBAC, file uploads, XSS defense, billing invariants, webhook cryptographic origin verification, rate limiting, and audit trails.
- **8 GDPR Privacy Requirements:** Covering onboarding minimization, portability, erasure, purpose limitation, encryption at rest, encryption in transit, file lifecycle cleanup, and privacy audit logs.
- All 18 requirements are now ready for formal syntactic authoring in Step 3.
