# Step 3: EARS Requirement Formulation & Fit Criteria Derivation

> **Step ID:** STEP-03  
> **Inputs:**  
> - Step 2 Regulatory Cross-Cutting & Threat Matrix  
> - Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed., Chapter 11)  
> - Suzanne & James Robertson (*Mastering the Requirements Process: Getting Requirements Right*, 3rd ed.)  
> - ISO/IEC/IEEE 29148:2018 (Requirements Engineering Standard)  
> **Output:** Syntactic Specification of 10 `REQ-SEC-*` and 8 `REQ-PRIV-*` Requirements  
> **Status:** Normative Specification Trajectory  

---

## 1. Purpose & Methodological Rationale

In classical requirements engineering, the failure to state non-functional constraints unambiguously leads to the **Vague Adjective Trap** (Anti-Pattern 8 in `phase3_functional_spec_guidelines.md`): engineers write that a system must be "secure", "fast", or "robust", which cannot be verified or tested.

Step 3 transforms the regulatory drivers and threat mitigations derived in Step 2 into **atomic, mathematically verifiable system requirements** using two foundational methodologies:
1. **EARS (Easy Approach to Requirements Syntax):** Developed by Alistair Mavin et al. and formalized by Karl Wiegers & Joy Beatty (2013). Enforces rigid sentence templates that eliminate ambiguity.
2. **Volere Fit Criteria:** Developed by Suzanne & James Robertson (2012). Establishes an objective, quantifiable metric that separates satisfaction from failure.
3. **ISO/IEC/IEEE 29148 Verification Methods:** Categorizes how the requirement is verified: `TEST`, `INSPECT`, `DEMONSTRATE`, or `ANALYZE`.

---

## 2. The 5 Canonical EARS Sentence Patterns

```text
+-----------------------------------------------------------------------------------+
|                           THE 5 EARS SYNTACTIC PATTERNS                           |
+-----------------------------------------------------------------------------------+
| 1. UBIQUITOUS (Always active):                                                    |
|    "The [system name] shall [system response]."                                   |
+-----------------------------------------------------------------------------------+
| 2. EVENT-DRIVEN (Triggered by an external stimulus):                              |
|    "When [optional precondition] [triggering event],                              |
|     the [system name] shall [system response]."                                   |
+-----------------------------------------------------------------------------------+
| 3. STATE-DRIVEN (Active while in a defined operational mode):                     |
|    "While [in a specific state], the [system name] shall [system response]."      |
+-----------------------------------------------------------------------------------+
| 4. UNWANTED BEHAVIOR (Handling errors, threats, or boundary violations):          |
|    "If [unwanted condition or failure mode],                                      |
|     then the [system name] shall [system response]."                              |
+-----------------------------------------------------------------------------------+
| 5. OPTIONAL FEATURE (Active only when a feature is enabled):                      |
|    "Where [feature is present], the [system name] shall [system response]."      |
+-----------------------------------------------------------------------------------+
```

---

## 3. Cognitive Trajectory: Formulation of Product Security Requirements (`REQ-SEC-*`)

### `REQ-SEC-01`: Multi-Tenant Data Isolation & Mediation
- **Syntactic Selection:** *Combined Ubiquitous & State-Driven*. Multi-tenancy is an architectural invariant that must be enforced continuously during all query executions.
- **Formulation:** 
  > *"The system shall enforce tenant context verification on every internal database query and asset retrieval, such that while operating in multi-tenant mode, the application services shall deny access to any record, project, task, or file whose organization identifier does not match the active authenticated session's organization identifier."*
- **Why this EARS Pattern:** Prevents query developers from assuming client-side tenant filtering; requires the server-side data access layer to enforce isolation on every query.
- **Volere Fit Criterion Rationale:** Must be a measurable 100% threshold: `100% of synthetic cross-tenant query probes executed during automated integration testing return HTTP 403 Forbidden with zero records leaked.`
- **Verification Method:** `TEST` (Automated integration test suite injecting foreign tenant IDs).

### `REQ-SEC-02`: Credential Hardening & Salted Hashing
- **Syntactic Selection:** *Event-Driven*. Triggered by the event of a user registering or resetting credentials.
- **Formulation:**
  > *"When a user sets or updates their account password, the system shall hash the password using a memory-hard, salted cryptographic hashing algorithm prior to persisting it in the internal application database, and the system shall never store, log, or transmit passwords in plaintext."*
- **Why this EARS Pattern:** Pinpoints the exact lifecycle moment (password update) and dictates the immediate defensive transformation.
- **Volere Fit Criterion Rationale:** Verifiable via database inspection and unit tests: `Stored password fields match standard cryptographic hash digest formats with unique salt lengths >= 16 bytes; zero plaintext password instances in application logs.`
- **Verification Method:** `TEST` (Unit test verifying cryptographic derivation and salt uniqueness).

### `REQ-SEC-03`: Cryptographic Session Management & Invalidation
- **Syntactic Selection:** *Combined State-Driven & Event-Driven*. Governs the active session state and the expiration/logout events.
- **Formulation:**
  > *"While a user is authenticated, the system shall maintain session state using cryptographically random tokens with a minimum of 128 bits of entropy. When a user initiates logout or exceeds 30 minutes of inactivity, the system shall immediately invalidate the session token on both client and server sides."*
- **Why this EARS Pattern:** Couples the background invariant (high entropy tokens) with explicit trigger events (logout or idle timeout).
- **Volere Fit Criterion Rationale:** Objective timing threshold: `Post-logout or expired session tokens submitted to protected API endpoints are rejected with HTTP 401 Unauthorized within 100 milliseconds.`
- **Verification Method:** `TEST` (Automated session expiration and revocation test suite).

### `REQ-SEC-04`: Role-Based Access Control & Action Mediation
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered by an administrative mutation attempt; handles the unauthorized role condition.
- **Formulation:**
  > *"When an authenticated user attempts to create, update, or delete project metadata or workspace configurations, the system shall evaluate the user's assigned workspace role. If the user does not possess the requisite administrative role, the system shall refuse the operation, preserve existing state, and log the unauthorized attempt."*
- **Why this EARS Pattern:** Explicitly dictates what happens on authorization failure (fail-safe defaults).
- **Volere Fit Criterion Rationale:** `Standard workspace members attempting administrative mutations receive an HTTP 403 response; database audit logs record timestamp, actor ID, and target resource.`
- **Verification Method:** `TEST` (Automated RBAC test matrix evaluating all 4 roles).

### `REQ-SEC-05`: File Upload Strict Validation & Content Isolation
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered by file attachment upload; branches on invalid file signature or size.
- **Formulation:**
  > *"When a file attachment is uploaded, the system shall validate that the actual file content matches the declared file signature (magic bytes) against an allowlist of non-executable document formats, and if an invalid signature, executable file, or size exceeding 25 MB is detected, the system shall reject the upload and discard the temporary buffer."*
- **Why this EARS Pattern:** Addresses the file upload attack surface by specifying validation at the magic-byte level, not just superficial file extensions.
- **Volere Fit Criterion Rationale:** `Submissions of spoofed executable binaries (e.g. .exe renamed to .pdf) are rejected with an explicit validation error, and zero temporary files remain on disk.`
- **Verification Method:** `TEST` (MIME/magic-byte spoofing test suite).

### `REQ-SEC-06`: Context-Aware Output Encoding & Sanitization
- **Syntactic Selection:** *Event-Driven*. Triggered when comment data is retrieved and rendered to users.
- **Formulation:**
  > *"When task comments or rich-text descriptions are rendered to users, the system shall perform context-aware output encoding to neutralize embedded scripts, HTML tags, or executable markup."*
- **Why this EARS Pattern:** Establishes that defense occurs at the output boundary, ensuring complete protection against stored XSS.
- **Volere Fit Criterion Rationale:** `100% of stored XSS test vectors injected into comment fields are rendered as inert text entities with zero script execution.`
- **Verification Method:** `TEST` (Automated browser-based dynamic security probe).

### `REQ-SEC-07`: Cryptographic Billing Invariant Protection
- **Syntactic Selection:** *Ubiquitous*. An absolute invariant governing financial and quota mutations.
- **Formulation:**
  > *"The system shall cryptographically verify all subscription transaction receipts received from the external payment gateway, ensuring that subscription tier upgrades are committed to the internal application database only upon successful cryptographic receipt validation."*
- **Why this EARS Pattern:** Guarantees that commercial privileges cannot be escalated through out-of-order or fabricated billing calls.
- **Volere Fit Criterion Rationale:** `Simulated unauthenticated or forged payment webhooks fail signature validation and produce zero changes in tenant billing status.`
- **Verification Method:** `INSPECT` (Code review and automated webhook verification test).

### `REQ-SEC-08`: Asymmetric HMAC Webhook Signature Verification
- **Syntactic Selection:** *Event-Driven*. Triggered when outbound event webhooks are dispatched to external listeners.
- **Formulation:**
  > *"When dispatching outbound event notifications to external webhook listeners, the system shall compute an HMAC-SHA256 signature across the event payload using a tenant-specific shared secret and transmit the signature in the request headers."*
- **Why this EARS Pattern:** Ensures origin authenticity and payload integrity for downstream consumers.
- **Volere Fit Criterion Rationale:** `Receiver test harness validates payload integrity and origin authenticity using the shared secret; any payload byte tampering invalidates the computed signature.`
- **Verification Method:** `TEST` (Payload tampering and HMAC verification test harness).

### `REQ-SEC-09`: Inbound API Token Mediation & Rate Limiting
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered on inbound API requests; handles the threshold exceedance.
- **Formulation:**
  > *"When an external productivity API client sends a request to TinyTask endpoints, the system shall authenticate the client token and evaluate invocation frequency against a maximum threshold of 100 requests per minute per tenant. If the threshold is exceeded, the system shall throttle requests and return HTTP 429 Too Many Requests with a Retry-After header."*
- **Why this EARS Pattern:** Defines both the normal authentication path and the explicit rate-limiting throttle response.
- **Volere Fit Criterion Rationale:** `Automated load generator exceeding 100 req/min receives HTTP 429 starting at request 101, recovering exactly when the time window resets.`
- **Verification Method:** `TEST` (Automated API load and rate-limiting test).

### `REQ-SEC-10`: Non-Repudiable Security Audit Logging
- **Syntactic Selection:** *Combined Ubiquitous & Event-Driven*. System-wide obligation capturing all security events.
- **Formulation:**
  > *"The system shall generate an immutable security audit record for all authentication attempts, privilege elevations, user deletions, subscription modifications, and permission rejections, containing timestamp, tenant ID, actor identity, action descriptor, and source IP address."*
- **Why this EARS Pattern:** Ensures non-repudiation and forensic auditability across the entire platform lifecycle.
- **Volere Fit Criterion Rationale:** `Audit log files are append-only; administrative users cannot alter or truncate audit entries; 100% of sensitive operations generate an audit log entry.`
- **Verification Method:** `TEST` (Tamper verification and audit event generation test).

---

## 4. Cognitive Trajectory: Formulation of Personal Data Protection Requirements (`REQ-PRIV-*`)

### `REQ-PRIV-01`: Registration Data Minimization by Default
- **Syntactic Selection:** *Ubiquitous*. Governs the design of all onboarding workflows.
- **Formulation:**
  > *"The system shall collect only the minimum personal data fields necessary to establish user identity and billing contact (specifically: full name, business email address, and hashed credentials), and shall not enforce or require personal phone numbers, physical home addresses, or demographic markers."*
- **Volere Fit Criterion Rationale:** `Database schema inspection confirms zero mandatory extraneous personal fields; registration form contains only the 3 strictly necessary identity fields.`
- **Verification Method:** `INSPECT` (Schema audit and registration form inspection).

### `REQ-PRIV-02`: Structured Personal Data Portability & Export
- **Syntactic Selection:** *Event-Driven*. Triggered by user invocation of GDPR Art. 20 data portability.
- **Formulation:**
  > *"When an authenticated workspace user requests an export of their personal account data (under GDPR Art. 20), the system shall compile all profile attributes, authored comments, assigned tasks, and logged hours into a machine-readable JSON archive within 24 hours of the request."*
- **Volere Fit Criterion Rationale:** `Export package contains 100% of user-generated data formatted in valid, schema-conforming JSON without inclusion of third-party personal data.`
- **Verification Method:** `DEMONSTRATE` (End-to-end export generation and JSON schema validation).

### `REQ-PRIV-03`: Irreversible Data Subject Erasure & Pseudonymization
- **Syntactic Selection:** *Event-Driven*. Triggered by user invocation of GDPR Art. 17 right to erasure.
- **Formulation:**
  > *"When a workspace administrator or user executes an account termination request (under GDPR Art. 17), the system shall permanently purge the user's credentials and personal contact details within 30 days, while pseudonymizing historical task comments and timesheets to maintain organizational audit integrity without retaining identifiable personal markers."*
- **Volere Fit Criterion Rationale:** `Post-erasure database search for the user's email or full name yields zero matches; historical records display a non-reversible pseudonym (e.g. Deactivated User [ID: 9481]).`
- **Verification Method:** `TEST` (Account termination pipeline test and data pseudonymization assertion).

### `REQ-PRIV-04`: Purpose Limitation & Time Log Segregation
- **Syntactic Selection:** *State-Driven*. Governs the operational state of timesheet processing.
- **Formulation:**
  > *"While processing logged billable hours and timesheet summaries, the system shall utilize time records strictly for project cost tracking and client invoicing, and shall prevent the extraction or profiling of individual employee performance metrics for unconsented secondary purposes."*
- **Volere Fit Criterion Rationale:** `Query interface and analytics exports restrict aggregations to project and workspace summaries; individual granular logs are accessible only to the author and the authorized workspace administrator.`
- **Verification Method:** `ANALYZE` (Data governance and access query review).

### `REQ-PRIV-05`: Personal Data Encryption at Rest
- **Syntactic Selection:** *Ubiquitous*. Architectural storage invariant.
- **Formulation:**
  > *"The system shall encrypt all persistent storage volumes, file assets, and database backups containing personal data at rest using AES-256 or an equivalent industry-standard cryptographic cipher."*
- **Volere Fit Criterion Rationale:** `Storage infrastructure manifests and volume configuration scripts confirm transparent disk and database encryption is enabled with cloud-managed key rotation.`
- **Verification Method:** `INSPECT` (Infrastructure-as-Code and volume configuration audit).

### `REQ-PRIV-06`: Mandatory End-to-End Transport Layer Encryption
- **Syntactic Selection:** *Combined Ubiquitous & Unwanted Behavior*. Network ingress invariant.
- **Formulation:**
  > *"The system shall encrypt all data in transit across public networks using TLS 1.3 (with fallback to TLS 1.2), and if an unencrypted HTTP connection attempt is detected, the system shall redirect the client to HTTPS or reject the connection."*
- **Volere Fit Criterion Rationale:** `SSL Labs scan of application ingress hosts yields an A+ grade; unencrypted port 80 connections immediately redirect to port 443 with HSTS enabled.`
- **Verification Method:** `TEST` (Automated TLS handshake and redirect probe).

### `REQ-PRIV-07`: Automated Orphan File Asset Cleanup & Expiration
- **Syntactic Selection:** *Event-Driven*. Triggered by project or task deletion.
- **Formulation:**
  > *"When a workspace project or task containing file attachments is deleted, the system shall schedule the unlinked storage objects for permanent deletion within 14 days, preventing indefinite storage of orphaned personal documents."*
- **Volere Fit Criterion Rationale:** `Background cleanup job successfully purges unreferenced storage files older than 14 days; object store audit verifies zero orphaned attachments remain.`
- **Verification Method:** `TEST` (Object storage lifecycle expiration test).

### `REQ-PRIV-08`: Privacy Audit Trail for Personal Data Modifications
- **Syntactic Selection:** *Event-Driven*. Triggered by user profile or preference changes.
- **Formulation:**
  > *"When an administrator or user modifies profile information, email preferences, or data export requests, the system shall record a privacy event in the audit log indicating the data subject ID, operator ID, field modified, and timestamp."*
- **Volere Fit Criterion Rationale:** `100% of profile update and data deletion requests generate a structured audit record verifiable by the Data Protection Lead.`
- **Verification Method:** `INSPECT` (Privacy audit log completeness audit).

---

## 5. Output Summary of Step 3

All 18 security and privacy requirements are now authored in precise, deterministic EARS syntax, equipped with objective Volere fit criteria, and bound to ISO 29148 verification methods. They form the core content of [`Doc03_Security_Privacy_Requirements.md`](../v1_security_privacy_synthesis/Doc03_Security_Privacy_Requirements.md).
