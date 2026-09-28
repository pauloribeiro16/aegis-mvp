# Step 3: EARS Requirement Formulation & Fit Criteria Derivation

> **Step ID:** STEP-03  
> **Inputs:**  
> - Step 2 Regulatory Cross-Cutting Matrix (threat analysis out of Phase 3 — Phase 4, ADR-005)  
> - Karl Wiegers & Joy Beatty (*Software Requirements*, 3rd ed., Chapter 11)  
> - Suzanne & James Robertson (*Mastering the Requirements Process: Getting Requirements Right*, 3rd ed.)  
> - ISO/IEC/IEEE 29148:2018 (Requirements Engineering Standard)  
> **Output:** Syntactic Specification of the 18 Security & Privacy NFRs (`RN9`–`RN26`)  
> **Status:** Normative Specification Trajectory  

---

## 1. Purpose & Methodological Rationale

In classical requirements engineering, the failure to state non-functional constraints unambiguously leads to the **Vague Adjective Trap** (Anti-Pattern 8 in `phase3_functional_spec_guidelines.md`): engineers write that a system must be "secure", "fast", or "robust", which cannot be verified or tested.

Step 3 transforms the regulatory drivers and mapped obligations derived in Step 2 into **atomic, mathematically verifiable system requirements** using two foundational methodologies:
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

## 3. Cognitive Trajectory: Formulation of Product Security Requirements (`RN9`–`RN18`)

### `RN9`: Multi-Tenant Data Isolation & Mediation
- **Syntactic Selection:** *Combined Ubiquitous & State-Driven*. Multi-tenancy is an architectural invariant that must be enforced continuously during all query executions.
- **Formulation:** 
  > *"The system shall enforce tenant context verification on every internal database query and asset retrieval, such that while operating in multi-tenant mode, the application services shall deny access to any record, project, task, or file whose organization identifier does not match the active authenticated session's organization identifier."*
- **Why this EARS Pattern:** Prevents query developers from assuming client-side tenant filtering; requires the server-side data access layer to enforce isolation on every query.
- **Volere Fit Criterion Rationale:** Must be a measurable 100% threshold: `100% of synthetic cross-tenant query probes executed during automated integration testing return HTTP 403 Forbidden with zero records leaked.`
- **Verification Method:** `TEST` (Automated integration test suite injecting foreign tenant IDs).

### `RN10`: Credential Confidentiality Protection (State of the Art)
- **Syntactic Selection:** *Event-Driven*. Triggered by the event of a user registering or resetting credentials.
- **Formulation:**
  > *"When a user sets or updates their account password, the system shall protect the credential using state-of-the-art mechanisms such that the original value cannot be recovered from any stored representation, and the system shall never store, log, or transmit passwords in recoverable form."*
- **Why this EARS Pattern:** Pinpoints the exact lifecycle moment (password update) and dictates the immediate defensive transformation.
- **Volere Fit Criterion Rationale:** Verifiable via database inspection and unit tests: `Stored credential representations are one-way verifiable (original value not recoverable), unique per credential, and zero recoverable credential values appear in application logs or data stores.`
- **Verification Method:** `TEST` (Automated credential-storage inspection).

### `RN11`: Session Management & Invalidation
- **Syntactic Selection:** *Combined State-Driven & Event-Driven*. Governs the active session state and the expiration/logout events.
- **Formulation:**
  > *"While a user is authenticated, the system shall manage session state using unpredictable session identifiers. When a user initiates logout or exceeds an established period of user inactivity, the system shall terminate and invalidate the session state on both client and server sides, preventing resumption without re-authentication."*
- **Why this EARS Pattern:** Couples the background invariant (non-predictable session identifiers) with explicit trigger events (logout or established inactivity).
- **Volere Fit Criterion Rationale:** Objective control threshold: `Post-logout or invalidated session tokens submitted to protected API endpoints are rejected with authentication failure status; invalidated sessions cannot be resumed without re-authentication.`
- **Verification Method:** `TEST` (Automated session expiration and revocation test suite).

### `RN12`: Role-Based Access Control & Action Mediation
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered by an administrative mutation attempt; handles the unauthorized role condition.
- **Formulation:**
  > *"When an authenticated user attempts to create, update, or delete project metadata or workspace configurations, the system shall evaluate the user's assigned workspace role. If the user does not possess the requisite administrative role, the system shall refuse the operation, preserve existing state, and log the unauthorized attempt."*
- **Why this EARS Pattern:** Explicitly dictates what happens on authorization failure (fail-safe defaults).
- **Volere Fit Criterion Rationale:** `Standard workspace members attempting administrative mutations receive an HTTP 403 response; database audit logs record timestamp, actor ID, and target resource.`
- **Verification Method:** `TEST` (Automated RBAC test matrix evaluating all 4 roles).

### `RN13`: File Upload Strict Validation & Content Isolation
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered by file attachment upload; branches on invalid file signature or size.
- **Formulation:**
  > *"When a file attachment is uploaded, the system shall validate that the actual file content matches its declared file type and actual content signature against an allowlist of non-executable document formats, and if an invalid signature, unauthorized executable format, or payload exceeding configured capacity limits is detected, the system shall reject the upload and discard the temporary buffer."*
- **Why this EARS Pattern:** Addresses the file upload attack surface by specifying content-level validation, not just declared file extensions.
- **Volere Fit Criterion Rationale:** `Submissions of spoofed executable binaries or payloads exceeding configured capacity limits are rejected with an explicit validation error, and zero temporary files remain on disk.`
- **Verification Method:** `TEST` (File-type spoofing test suite).

### `RN14`: Untrusted Content Neutralization
- **Syntactic Selection:** *Event-Driven*. Triggered when comment data is retrieved and rendered to users.
- **Formulation:**
  > *"When task comments or rich-text descriptions are rendered to users, the system shall neutralize embedded active content so that submitted scripts, markup, or executable payloads are rendered as inert text."*
- **Why this EARS Pattern:** Establishes that defense occurs at the output boundary, ensuring complete protection against stored script injection.
- **Volere Fit Criterion Rationale:** `100% of stored script-injection test vectors injected into comment fields are rendered as inert text with zero script execution.`
- **Verification Method:** `TEST` (Automated browser-based dynamic security probe).

### `RN15`: Cryptographic Billing Invariant Protection
- **Syntactic Selection:** *Ubiquitous*. An absolute invariant governing financial and quota mutations.
- **Formulation:**
  > *"The system shall cryptographically verify all subscription transaction receipts received from the external payment gateway, ensuring that subscription tier upgrades are committed to the internal application database only upon successful cryptographic receipt validation."*
- **Why this EARS Pattern:** Guarantees that commercial privileges cannot be escalated through out-of-order or fabricated billing calls.
- **Volere Fit Criterion Rationale:** `Simulated unauthenticated or forged payment webhooks fail signature validation and produce zero changes in tenant billing status.`
- **Verification Method:** `INSPECT` (Code review and automated webhook verification test).

### `RN16`: Cryptographic Webhook Origin Verification
- **Syntactic Selection:** *Event-Driven*. Triggered when outbound event webhooks are dispatched to external listeners.
- **Formulation:**
  > *"When dispatching outbound event notifications to external webhook listeners, the system shall compute a cryptographic message authentication code across the event payload using a tenant-specific shared secret and transmit the authentication proof in the request headers."*
- **Why this EARS Pattern:** Ensures origin authenticity and payload integrity for downstream consumers.
- **Volere Fit Criterion Rationale:** `Receiver test harness validates payload integrity and origin authenticity using the shared secret; any payload byte tampering invalidates the computed authentication proof.`
- **Verification Method:** `TEST` (Payload tampering and cryptographic message authentication verification test harness).

### `RN17`: Inbound API Token Mediation & Rate Limiting
- **Syntactic Selection:** *Combined Event-Driven & Unwanted Behavior*. Triggered on inbound API requests; handles the threshold exceedance.
- **Formulation:**
  > *"When an external productivity API client sends a request to TinyTask endpoints, the system shall authenticate the client token and evaluate invocation frequency against established tenant rate limits to protect service availability against resource exhaustion. If the rate limit is exceeded, the system shall throttle requests and return standard rate-limiting notifications."*
- **Why this EARS Pattern:** Defines both the normal authentication path and the explicit rate-limiting throttle response.
- **Volere Fit Criterion Rationale:** `Automated load generation exceeding established tenant rate thresholds receives rate-limiting status responses, recovering normal processing once the request rate conforms to operational capacity.`
- **Verification Method:** `TEST` (Automated API load and rate-limiting test).

### `RN18`: Non-Repudiable Security Audit Logging
- **Syntactic Selection:** *Combined Ubiquitous & Event-Driven*. System-wide obligation capturing all security events.
- **Formulation:**
  > *"The system shall generate an immutable security audit record for all authentication attempts, privilege elevations, user deletions, subscription modifications, and permission rejections, containing timestamp, tenant ID, actor identity, action descriptor, and source IP address."*
- **Why this EARS Pattern:** Ensures non-repudiation and forensic auditability across the entire platform lifecycle.
- **Volere Fit Criterion Rationale:** `Audit log files are append-only; administrative users cannot alter or truncate audit entries; 100% of sensitive operations generate an audit log entry.`
- **Verification Method:** `TEST` (Tamper verification and audit event generation test).

---

## 4. Cognitive Trajectory: Formulation of Personal Data Protection Requirements (`RN19`–`RN26`)

### `RN19`: Registration Data Minimization by Default
- **Syntactic Selection:** *Ubiquitous*. Governs the design of all onboarding workflows.
- **Formulation:**
  > *"The system shall collect only the minimum personal data fields necessary to establish user identity and billing contact (specifically: full name, business email address, and hashed credentials), and shall not enforce or require personal phone numbers, physical home addresses, or demographic markers."*
- **Volere Fit Criterion Rationale:** `Database schema inspection confirms zero mandatory extraneous personal fields; registration form contains only the 3 strictly necessary identity fields.`
- **Verification Method:** `INSPECT` (Schema audit and registration form inspection).

### `RN20`: Structured Personal Data Portability & Export
- **Syntactic Selection:** *Event-Driven*. Triggered by user invocation of GDPR Art. 20 data portability.
- **Formulation:**
  > *"When an authenticated workspace user requests an export of their personal account data (under GDPR Art. 20), the system shall compile all profile attributes, authored comments, assigned tasks, and logged hours into a structured, commonly used, and machine-readable format for user retrieval."*
- **Volere Fit Criterion Rationale:** `Export package contains 100% of user-generated data formatted in structured, machine-readable format without inclusion of third-party personal data.`
- **Verification Method:** `DEMONSTRATE` (End-to-end export generation and schema validation).

### `RN21`: Irreversible Data Subject Erasure & Pseudonymization
- **Syntactic Selection:** *Event-Driven*. Triggered by user invocation of GDPR Art. 17 right to erasure.
- **Formulation:**
  > *"When a workspace administrator or user executes an account termination request (under GDPR Art. 17), the system shall irreversibly erase the user's credentials and direct personal contact details from active operational stores, while pseudonymizing historical task comments and timesheets to maintain organizational audit integrity without retaining identifiable personal markers."*
- **Volere Fit Criterion Rationale:** `Post-erasure database search for the user's email or full name yields zero matches; historical records display a non-reversible pseudonym (e.g. Deactivated User [ID: 9481]).`
- **Verification Method:** `TEST` (Account termination pipeline test and data pseudonymization assertion).

### `RN22`: Purpose Limitation & Activity Metrics Segregation
- **Syntactic Selection:** *State-Driven*. Governs the operational state of timesheet processing.
- **Formulation:**
  > *"While processing logged billable hours and timesheet summaries, the system shall utilize time records strictly for project cost tracking and client invoicing, and shall prevent the extraction or profiling of individual employee performance metrics for unconsented secondary purposes."*
- **Volere Fit Criterion Rationale:** `Query interface and analytics exports restrict aggregations to project and workspace summaries; individual granular logs are accessible only to the author and the authorized workspace administrator.`
- **Verification Method:** `ANALYZE` (Data governance and access query review).

### `RN23`: Personal Data Cryptographic Protection at Rest
- **Syntactic Selection:** *Ubiquitous*. Architectural storage invariant.
- **Formulation:**
  > *"The system shall cryptographically protect all persistent storage volumes, file assets, and database backups containing personal data at rest against unauthorized extraction using state-of-the-art cryptographic mechanisms."*
- **Volere Fit Criterion Rationale:** `Storage infrastructure manifests and volume configuration scripts confirm transparent cryptographic protection is enabled with managed key rotation.`
- **Verification Method:** `INSPECT` (Infrastructure-as-Code and volume configuration audit).

### `RN24`: Cryptographic Protection of Data in Transit
- **Syntactic Selection:** *Combined Ubiquitous & Unwanted Behavior*. Network ingress invariant.
- **Formulation:**
  > *"The system shall cryptographically protect all personal and sensitive data in transit across public and untrusted networks against unauthorized disclosure and tampering, using state-of-the-art cryptographic communication mechanisms, and if an unencrypted connection attempt is detected, the system shall refuse the connection or enforce cryptographic upgrade."*
- **Volere Fit Criterion Rationale:** `100% of network traffic traversing external boundaries is cryptographically protected; unencrypted transmission attempts fail closed.`
- **Verification Method:** `TEST` (Automated network inspection verifying cryptographic transport protection on all external endpoints).

### `RN25`: Automated Orphan File Asset Cleanup & Expiration
- **Syntactic Selection:** *Event-Driven*. Triggered by project or task deletion.
- **Formulation:**
  > *"When a workspace project or task containing file attachments is deleted, the system shall identify and schedule unlinked storage objects for permanent deletion in accordance with established retention policies, preventing indefinite storage of orphaned personal documents."*
- **Volere Fit Criterion Rationale:** `Automated cleanup routines purge unreferenced storage assets according to retention schedules; object store audit verifies zero orphaned attachments remain.`
- **Verification Method:** `TEST` (Object storage lifecycle expiration test).

### `RN26`: Privacy Audit Trail for Personal Data Modifications
- **Syntactic Selection:** *Event-Driven*. Triggered by user profile or preference changes.
- **Formulation:**
  > *"When an administrator or user modifies profile information, email preferences, or data export requests, the system shall record a privacy event in the audit log indicating the data subject ID, operator ID, field modified, and timestamp."*
- **Volere Fit Criterion Rationale:** `100% of profile update and data deletion requests generate a structured audit record verifiable by the Data Protection Lead.`
- **Verification Method:** `INSPECT` (Privacy audit log completeness audit).

---

## 5. Output Summary of Step 3

All 18 security and privacy requirements are now authored in precise, deterministic EARS syntax, equipped with objective Volere fit criteria, and bound to ISO 29148 verification methods. Per the 2026-09-23 absorption rule they are absorbed into the `Security & Privacy Constraints` rows of the V1 `Doc01` cards (cross-cutting NFRs stay standalone in the Quality Attributes table) — no standalone catalog document.
