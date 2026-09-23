# Step 4: Functional Augmentation & Traceability Weaving

> **Step ID:** STEP-04  
> **Inputs:**  
> - Step 1 Functional Baseline (`v0_functional_baseline/Doc01`, `Doc02`)  
> - Step 3 EARS Requirements Specification (`Doc03_Security_Privacy_Requirements.md`)  
> - Alistair Cockburn (*Writing Effective Use Cases*, Chapter on Extension Handling)  
> **Outputs:**  
> - Augmented `Doc01_Requirements_Elicitation_and_PUC.md` (in `v1_security_privacy_synthesis/`)  
> - Augmented `Doc02_System_Use_Cases.md` (in `v1_security_privacy_synthesis/`)  
> **Status:** Specification Synthesis Completed & Verified  

---

## 1. Purpose & Methodological Rationale

The central challenge in requirements engineering is **how to inject security and regulatory constraints into functional models without corrupting functional clarity**.

If an engineer directly rewrites the Main Success Scenario (MSS) to include security checks, the use case turns into a procedural implementation script:
- *Bad Practice:* "Step 2: System calculates argon2id hash of password, checks Redis rate limit, checks session table, and evaluates tenant UUID."
- *Cockburn's Golden Rule:* **Keep the Main Success Scenario clean and user-goal focused.** 

**The AEGIS Methodological Solution:**
Security and privacy constraints are woven into the functional model strictly via three non-intrusive extension points:
1. **Security Preconditions:** Declare the authentication and tenant invariants that must hold before the use case begins.
2. **Threat Extensions (Alternative Flows):** Explicit branch points that specify system behavior when an attack or failure occurs (e.g., brute-force lockout, forged webhook, XSS payload).
3. **Enhanced Minimal Guarantees:** Strict postconditions ensuring fail-safe state rollback, zero data leakage, and immutable security audit logging (`REQ-SEC-10`).

---

## 2. Augmenting `Doc01`: Non-Functional Synthesis Table 7b

In `Doc01_Requirements_Elicitation_and_PUC.md`, the 18 atomic functional requirement cards (`R1.1` to `R8.2`) remain pure and technology-neutral. 

To bind the security constraints, Section 2.3 is augmented with **Table 7b (Security & Privacy Non-Functional Synthesis)**, establishing direct lineage to `Doc03`:

```markdown
*Table 7b. Security & Privacy Non-Functional Synthesis (Traceable to Phase 2 & Doc03)*

| ID | Security & Privacy Requirement | Upstream Origin | Bound Functional Requirements | Verification |
|---|---|---|---|---|
| **REQ-SEC-01** | Multi-Tenant Data Isolation & Mediation | CRA Annex I / SO-D-02.1-002 | R1.2, R2.1, R3.1 | TEST |
| **REQ-SEC-02** | Credential Hardening & Salted Hashing | CRA Annex I / SO-D-02.1-002 | R1.1 | TEST |
| **REQ-SEC-03** | Cryptographic Session Management & Invalidation | CRA Annex I / SO-D-02.2-002 | R1.1 | TEST |
| **REQ-SEC-04** | Role-Based Access Control & Action Mediation | CRA Annex I / SO-D-02.1-002 | R2.1, R2.2, R3.1 | TEST |
| **REQ-SEC-05** | File Upload Strict Validation & Content Isolation | CRA Annex I / SO-D-07.1-002 | R5.1 | TEST |
| **REQ-SEC-06** | Context-Aware Output Encoding & Sanitization | CRA Annex I / SO-D-07.1-002 | R5.2 | TEST |
| **REQ-SEC-07** | Cryptographic Billing Invariant Protection | CRA Annex I / SO-D-01.1-002 | R7.1, R7.2 | INSPECT |
| **REQ-SEC-08** | Asymmetric HMAC Webhook Signature Verification | CRA Annex I / SO-D-05.1-002 | R7.1, R7.2 | TEST |
| **REQ-SEC-09** | Inbound API Token Mediation & Rate Limiting | CRA Annex I / SO-D-02.1-002 | R1.1, R4.2 | TEST |
| **REQ-SEC-10** | Non-Repudiable Security Audit Logging | CRA Annex I / SO-D-03.1-002 | R1.1 to R8.2 | TEST |
| **REQ-PRIV-01** | Registration Data Minimization by Default | GDPR Art. 5(1)(c) / PO-D-06.1-001 | R1.1 | INSPECT |
| **REQ-PRIV-02** | Structured Personal Data Portability & Export | GDPR Art. 20 / PO-D-06.2-001 | R8.1 | DEMONSTRATE |
| **REQ-PRIV-03** | Irreversible Data Subject Erasure & Pseudonymization | GDPR Art. 17 / PO-D-06.2-001 | R8.2 | TEST |
| **REQ-PRIV-04** | Purpose Limitation & Activity History Segregation | GDPR Art. 5(1)(b) / PO-D-06.1-001 | R6.1, R6.2 | ANALYZE |
| **REQ-PRIV-05** | Personal Data Encryption at Rest | GDPR Art. 32 / PO-D-01.1-001 | R1.1, R1.2, R8.1 | INSPECT |
| **REQ-PRIV-06** | Mandatory End-to-End Transport Layer Encryption | GDPR Art. 32 / PO-D-01.2-001 | R1.1 to R8.2 | TEST |
| **REQ-PRIV-07** | Automated Orphan File Asset Cleanup & Expiration | GDPR Art. 5(1)(e) / PO-D-06.1-001 | R5.1 | TEST |
| **REQ-PRIV-08** | Privacy Audit Trail for Personal Data Modifications | GDPR Art. 30 / PO-D-03.1-001 | R1.1, R1.2, R8.2 | INSPECT |
```

---

## 3. Augmenting `Doc02`: Concrete Use Case Transformations

The following comparative examples illustrate how Cockburn sea-level use cases were augmented from V0 to V1:

### Example 1: `{U.C. 1.1}` Register and authenticate user accounts

#### Version 0 (Pure Functional Baseline):
```markdown
- **Preconditions:** The user has access to a valid email inbox.
- **Extensions:**
  - **5b. Invalid login credentials:**
    - 5b1. System informs actor of authentication failure and increments failed attempt counter without revealing whether the email or password was incorrect.
- **Minimal Guarantees:** Failed attempts leave database credentials unmodified; no partial account records remain in an ambiguous state.
```

#### Version 1 (Synthesized Baseline):
```markdown
- **Security & Privacy Traces:** `REQ-SEC-02` (Credential Hashing), `REQ-SEC-03` (Session Invalidation), `REQ-SEC-10` (Audit Logging), `REQ-PRIV-01` (Data Minimization), `REQ-PRIV-06` (TLS 1.3)
- **Preconditions:** network connection terminates over TLS 1.3 (REQ-PRIV-06); The user has access to a valid email inbox.
- **Extensions:**
  - **5b. Invalid login credentials:**
    - 5b1. System informs actor of authentication failure and increments failed attempt counter without revealing whether the email or password was incorrect (REQ-SEC-02).
  - **5c. Repeated authentication failures exceed threshold (5 attempts):**
    - 5c1. System temporarily blocks authentication attempts for target account for 15 minutes, returns generic throttling notice, and records security alert in audit log (REQ-SEC-03, REQ-SEC-10).
- **Minimal Guarantees:** Failed attempts leave database credentials unmodified; security audit log records timestamp and client IP for every rejected attempt; zero credentials or session tokens are leaked (REQ-SEC-10).
```
- **Cognitive Justification:** Precondition enforces transport security (`REQ-PRIV-06`); Extension 5c mitigates credential stuffing (`REQ-SEC-03`); Minimal guarantee mandates non-repudiable audit logging (`REQ-SEC-10`). The Main Success Scenario is 100% preserved.

---

### Example 2: `{U.C. 5.1}` Manage task deliverable attachments

#### Version 0 (Pure Functional Baseline):
```markdown
- **Preconditions:** Actor has Member or Admin permissions in the workspace; task exists.
- **Extensions:**
  - **4b. Upload transmission interrupted:**
    - 4b1. System deletes incomplete binary fragments and informs actor to retry the transfer.
- **Minimal Guarantees:** Incomplete or corrupted file fragments are automatically purged from storage buffers.
```

#### Version 1 (Synthesized Baseline):
```markdown
- **Security & Privacy Traces:** `REQ-SEC-05` (Strict File Validation & Malware Isolation), `REQ-PRIV-07` (Orphan File Expiration)
- **Preconditions:** actor possesses Member role; storage quota not exceeded; task exists.
- **Extensions:**
  - **4b. Upload transmission interrupted:**
    - 4b1. System deletes incomplete binary fragments and informs actor to retry the transfer.
  - **4c. Disallowed file type or executable binary signature detected:**
    - 4c1. System rejects upload, purges temporary buffer immediately, and records file security event (REQ-SEC-05).
- **Minimal Guarantees:** Incomplete or corrupted file fragments are automatically purged from storage buffers; deleted attachments are marked for irreversible cleanup within 14 days (REQ-PRIV-07).
```
- **Cognitive Justification:** Extension 4c blocks malicious disguised binaries at the magic-byte level (`REQ-SEC-05`); Minimal guarantee prevents indefinite personal document retention (`REQ-PRIV-07`).

---

### Example 3: `{U.C. 7.1}` Subscribe and manage workspace commercial plans

#### Version 0 (Pure Functional Baseline):
```markdown
- **Preconditions:** Workspace exists; actor has an active session with Owner role.
- **Extensions:**
  - **5b. Gateway webhook payload lost or delayed:**
    - 5b1. System provides checkout status polling mechanism and syncs billing status upon receipt of asynchronous confirmation.
- **Minimal Guarantees:** No commercial plan upgrades or quota adjustments occur without confirmed payment gateway authorization.
```

#### Version 1 (Synthesized Baseline):
```markdown
- **Security & Privacy Traces:** `REQ-SEC-07` (Billing Invariant Protection), `REQ-SEC-08` (HMAC Webhook Verification), `REQ-SEC-10` (Audit Logging)
- **Preconditions:** actor has Owner role; session authenticated (REQ-SEC-04); Workspace exists.
- **Extensions:**
  - **5b. Gateway webhook payload lost or delayed:**
    - 5b1. System provides checkout status polling mechanism and syncs billing status upon receipt of asynchronous confirmation.
  - **5c. Payment webhook signature validation fails:**
    - 5c1. System rejects webhook as untrusted/forged, makes zero modifications to workspace subscription tier, and alerts security operations (REQ-SEC-07, REQ-SEC-08, REQ-SEC-10).
- **Minimal Guarantees:** No commercial plan upgrades or quota adjustments occur without verified cryptographic payment receipt (REQ-SEC-07, REQ-SEC-10).
```
- **Cognitive Justification:** Extension 5c prevents commercial fraud from spoofed webhooks (`REQ-SEC-08`); Minimal guarantee ensures no privilege elevation without verified cryptographic proof (`REQ-SEC-07`).

---

### Example 4: `{U.C. 8.2}` Close user accounts and terminate workspace access

#### Version 0 (Pure Functional Baseline):
```markdown
- **Preconditions:** Actor possesses an active authenticated session.
- **Extensions:**
  - **4b. Closure confirmed by single user:**
    - 4b1. System deactivates personal credentials, removes user from team rosters, and retains authored task comments under deactivated attribution.
- **Minimal Guarantees:** Account deactivation immediately revokes authentication tokens, preventing subsequent API or UI access.
```

#### Version 1 (Synthesized Baseline):
```markdown
- **Security & Privacy Traces:** `REQ-PRIV-03` (Right to Erasure), `REQ-PRIV-08` (Privacy Audit Trail), `REQ-SEC-03` (Session Invalidation), `REQ-SEC-10` (Audit Logging)
- **Preconditions:** actor possesses active session; identity confirmed (REQ-SEC-03).
- **Extensions:**
  - **4b. Closure confirmed by single user:**
    - 4b1. System deactivates personal credentials, removes user from team rosters, and pseudonymizes authored task comments in accordance with REQ-PRIV-03.
  - **4c. Session invalidation fails during closure:**
    - 4c1. System executes emergency forced server-side token revocation to prevent unauthorized post-closure access (REQ-SEC-03).
- **Minimal Guarantees:** Account deactivation immediately revokes authentication tokens, preventing subsequent API or UI access; personal data is pseudonymized within 30 days and audit logged (REQ-PRIV-03, REQ-SEC-10).
```
- **Cognitive Justification:** Extension 4b enforces GDPR Art. 17 right to erasure via pseudonymization (`REQ-PRIV-03`); Extension 4c and Minimal guarantee enforce immediate cryptographic session revocation (`REQ-SEC-03`).

---

## 4. Verification & Integrity Confirmation

Following the completion of Step 4, the repository was verified using the automated linter:
```bash
python scripts/doc_lint.py --strict
```
**Result:** `1639 files checked, 0 findings (0 files affected)` (Exit code 0).

All links resolve correctly, zero unresolved placeholders exist, and all requirements maintain strict technology neutrality and active verb conjugations.
