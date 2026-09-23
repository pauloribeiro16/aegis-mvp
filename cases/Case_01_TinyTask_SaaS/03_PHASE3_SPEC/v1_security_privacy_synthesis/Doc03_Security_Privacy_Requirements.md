# AEGIS Phase 3 — Security & Privacy Requirements Specification (TinyTask SaaS)

> **Document ID:** AEGIS-P3-DOC03  
> **Case Study:** Case 01 — TinyTask SaaS (B2B Task Management Multi-Tenant Platform)  
> **Lifecycle Phase:** AEGIS Phase 3 — Specification  
> **Version:** Version 1 (V1) — Security & Privacy Synthesis  
> **Status:** APPROVED  
> **Authoring Standard:** EARS (Easy Approach to Requirements Syntax / Wiegers & Beatty) & Volere Non-Functional Fit Criteria (Robertson & Robertson)  
> **Verification Standard:** ISO/IEC/IEEE 29148:2018 (TEST, INSPECT, DEMONSTRATE, ANALYZE)  

---

## 1. Executive Overview & Synthesis Scope

This document specifies the formal **Non-Functional Security and Privacy Requirements** for TinyTask SaaS. It represents the normative bridge between **Phase 2 (Operationalization)** and the **Phase 3 Functional Specification**:
- It consumes the 35 active sub-domain Operational Objectives from Phase 2 (`Doc01_Operational_Objectives.md`), segregating GDPR personal data obligations (`PO-D-XX.Y-NNN`) from Cyber Resilience Act (CRA) product resilience obligations (`SO-D-XX.Y-NNN`).
- It enforces the 7 universal Secure Design Principles from Phase 2 (`Doc02_Secure_Design_Principles.md`), embedding trust boundaries, fail-safe defaults, least privilege, and data minimization.
- It translates these obligations into atomic, verifiable system requirements using **EARS syntax templates** (Wiegers & Beatty, 2013), completely bound to the 18 Functional Requirements (`R1.1` to `R8.2`) and 18 System Use Cases (`{U.C. 1.1}` to `{U.C. 8.2}`).

---

## 2. Master Traceability Matrix: Phase 2 to Phase 3

The following matrix establishes bidirectional traceability across regulatory drivers, operational objectives, engineering principles, functional scope, and the resulting Phase 3 security/privacy requirements:

| Phase 3 Reqs | Requirement Name | Upstream Phase 2 Rule | Secure Design Principle | Functional Reqs Bound | System Use Cases Bound | Empirical Verification |
|---|---|---|---|---|---|---|
| `RN9` | Multi-Tenant Data Isolation & Mediation | `SO-D-02.1-002` | `PRIN-ENG-01`, `PRIN-ENG-03` | `R1.2`, `R2.1`, `R3.1` | `{U.C. 1.2}`, `{U.C. 2.1}`, `{U.C. 3.1}` | `TEST` |
| `RN10` | Credential Hardening & Salted Hashing | `SO-D-02.1-002` | `PRIN-ENG-04`, `PRIN-ENG-05` | `R1.1` | `{U.C. 1.1}` | `TEST` |
| `RN11` | Cryptographic Session Management & Invalidation | `SO-D-02.2-002` | `PRIN-ENG-04` | `R1.1` | `{U.C. 1.1}` | `TEST` |
| `RN12` | Role-Based Access Control & Action Mediation | `SO-D-02.1-002` | `PRIN-ENG-01`, `PRIN-ENG-03` | `R2.1`, `R2.2`, `R3.1` | `{U.C. 2.1}`, `{U.C. 2.2}`, `{U.C. 3.1}` | `TEST` |
| `RN13` | File Upload Strict Validation & Content Isolation | `SO-D-07.1-002` | `PRIN-ENG-02`, `PRIN-ENG-04` | `R4.1`, `R4.2` | `{U.C. 4.1}`, `{U.C. 4.2}` | `TEST` |
| `RN14` | Context-Aware Output Encoding & Sanitization | `SO-D-07.1-002` | `PRIN-ENG-04` | `R5.1` | `{U.C. 5.1}` | `TEST` |
| `RN15` | Cryptographic Billing Invariant Protection | `SO-D-01.1-002`, `SO-D-08.1-002` | `PRIN-ENG-03`, `PRIN-ENG-07` | `R7.1`, `R7.2` | `{U.C. 7.1}`, `{U.C. 7.2}` | `INSPECT` |
| `RN16` | Cryptographic Webhook Origin Verification | `SO-D-05.1-002`, `SO-D-08.1-002` | `PRIN-ENG-01`, `PRIN-ENG-02` | `R8.1` | `{U.C. 8.1}` | `TEST` |
| `RN17` | Inbound API Token Mediation & Rate Limiting | `SO-D-02.1-002`, `SO-D-05.1-002` | `PRIN-ENG-01`, `PRIN-ENG-02` | `R8.2` | `{U.C. 8.2}` | `TEST` |
| `RN18` | Non-Repudiable Security Audit Logging | `SO-D-03.1-002` | `PRIN-ENG-07` | `R1.1` to `R8.2` | All Use Cases | `TEST` |
| `RN19`| Registration Data Minimization by Default | `PO-D-06.1-001` | `PRIN-ENG-06` | `R1.1` | `{U.C. 1.1}` | `INSPECT` |
| `RN20`| Structured Personal Data Portability & Export | `PO-D-06.2-001` | `PRIN-ENG-06` | `R1.2` | `{U.C. 1.2}` | `DEMONSTRATE` |
| `RN21`| Irreversible Data Subject Erasure & Pseudonymization | `PO-D-06.2-001` | `PRIN-ENG-06` | `R1.1`, `R1.2` | `{U.C. 1.1}`, `{U.C. 1.2}` | `TEST` |
| `RN22`| Purpose Limitation & Time Log Segregation | `PO-D-06.1-001` | `PRIN-ENG-03`, `PRIN-ENG-06` | `R6.1`, `R6.2` | `{U.C. 6.1}`, `{U.C. 6.2}` | `ANALYZE` |
| `RN23`| Personal Data Cryptographic Protection at Rest | `PO-D-01.1-001` | `PRIN-ENG-01` | `R1.1`, `R1.2`, `R6.1` | `{U.C. 1.1}`, `{U.C. 1.2}`, `{U.C. 6.1}` | `INSPECT` |
| `RN24`| Mandatory End-to-End Transport Layer Cryptographic Protection | `PO-D-01.2-001` | `PRIN-ENG-01` | `R1.1` to `R8.2` | All Use Cases | `TEST` |
| `RN25`| Automated Orphan File Asset Cleanup & Expiration | `PO-D-06.1-001` | `PRIN-ENG-06` | `R4.2` | `{U.C. 4.2}` | `TEST` |
| `RN26`| Privacy Audit Trail for Data Subject Modifications | `PO-D-03.1-001` | `PRIN-ENG-07` | `R1.1`, `R1.2`, `R6.1` | `{U.C. 1.1}`, `{U.C. 1.2}`, `{U.C. 6.1}` | `INSPECT` |

---

## 3. Product Cyber Resilience Requirements (CRA Specification — `RN9` to `RN18`)

### `RN9`: Multi-Tenant Data Isolation & Mediation
- **EARS Pattern:** Ubiquitous & State-Driven
- **Statement:** The system shall enforce tenant context verification on every internal database query and asset retrieval, such that while operating in multi-tenant mode, the application services shall deny access to any record, project, task, or file whose organization identifier does not match the active authenticated session's organization identifier.
- **Upstream Traces:** `SO-D-02.1-002`, `PRIN-ENG-01`, `PRIN-ENG-03`
- **Functional Traces:** `R1.2`, `R2.1`, `R3.1` | `{U.C. 1.2}`, `{U.C. 2.1}`, `{U.C. 3.1}`
- **Volere Fit Criterion:** 100% of synthetic cross-tenant query probes executed during automated integration testing return HTTP 403 Forbidden with zero records leaked.
- **Verification Method:** `TEST` (Automated integration suite executing cross-tenant injection vectors).

### `RN10`: Credential Hardening & Salted Hashing
- **EARS Pattern:** Event-Driven
- **Statement:** When a user sets or updates their account password, the system shall hash the password using a memory-hard, salted cryptographic hashing algorithm prior to persisting it in the internal application database, and the system shall never store, log, or transmit passwords in plaintext.
- **Upstream Traces:** `SO-D-02.1-002`, `SO-D-01.1-002`, `PRIN-ENG-04`
- **Functional Traces:** `R1.1` | `{U.C. 1.1}`
- **Volere Fit Criterion:** Inspection of persistent user tables and application logs confirms zero plaintext password instances, and stored password fields match standard cryptographic hash digest formats with unique salt lengths >= 16 bytes.
- **Verification Method:** `TEST` (Automated unit tests validating hash derivation and entropy).

### `RN11`: Cryptographic Session Management & Invalidation
- **EARS Pattern:** State-Driven & Event-Driven
- **Statement:** While a user is authenticated, the system shall maintain session state using cryptographically random tokens with a minimum of 128 bits of entropy. When a user initiates logout or exceeds 30 minutes of inactivity, the system shall immediately invalidate the session token on both client and server sides.
- **Upstream Traces:** `SO-D-02.2-002`, `PRIN-ENG-04`
- **Functional Traces:** `R1.1` | `{U.C. 1.1}`
- **Volere Fit Criterion:** Post-logout or expired session tokens submitted to protected API endpoints are rejected with HTTP 401 Unauthorized within 100 milliseconds.
- **Verification Method:** `TEST` (Automated session invalidation test suite).

### `RN12`: Role-Based Access Control & Action Mediation
- **EARS Pattern:** Event-Driven & Unwanted Behavior
- **Statement:** When an authenticated user attempts to create, update, or delete project metadata or workspace configurations, the system shall evaluate the user's assigned workspace role. If the user does not possess the requisite administrative role, the system shall refuse the operation, preserve existing state, and log the unauthorized attempt.
- **Upstream Traces:** `SO-D-02.1-002`, `PRIN-ENG-03`, `PRIN-ENG-04`
- **Functional Traces:** `R2.1`, `R2.2`, `R3.1` | `{U.C. 2.1}`, `{U.C. 2.2}`, `{U.C. 3.1}`
- **Volere Fit Criterion:** Standard workspace members attempting administrative mutations receive an HTTP 403 response; database audit logs record timestamp, actor ID, and target resource.
- **Verification Method:** `TEST` (RBAC matrix permission verification suite).

### `RN13`: File Upload Strict Validation & Content Isolation
- **EARS Pattern:** Event-Driven & Unwanted Behavior
- **Statement:** When a file attachment is uploaded, the system shall validate that the actual file content matches the declared file signature (magic bytes) against an allowlist of non-executable document formats, and if an invalid signature, executable file, or size exceeding 25 MB is detected, the system shall reject the upload and discard the temporary buffer.
- **Upstream Traces:** `SO-D-07.1-002`, `PRIN-ENG-02`, `PRIN-ENG-04`
- **Functional Traces:** `R4.1`, `R4.2` | `{U.C. 4.1}`, `{U.C. 4.2}`
- **Volere Fit Criterion:** Submissions of spoofed executable binaries (e.g. `.exe` renamed to `.pdf`) are rejected with an explicit validation error, and zero temporary files remain on disk.
- **Verification Method:** `TEST` (Malicious payload upload and MIME-mismatch test suite).

### `RN14`: Context-Aware Output Encoding & Sanitization
- **EARS Pattern:** Event-Driven
- **Statement:** When task comments or rich-text descriptions are rendered to users, the system shall perform context-aware output encoding to neutralize embedded scripts, HTML tags, or executable markup.
- **Upstream Traces:** `SO-D-07.1-002`, `PRIN-ENG-04`
- **Functional Traces:** `R5.1` | `{U.C. 5.1}`
- **Volere Fit Criterion:** 100% of stored XSS test vectors injected into comment fields are rendered as inert text entities with zero script execution.
- **Verification Method:** `TEST` (Automated browser-based dynamic security assertion).

### `RN15`: Cryptographic Billing Invariant Protection
- **EARS Pattern:** Ubiquitous
- **Statement:** The system shall cryptographically verify all subscription transaction receipts received from the external payment gateway, ensuring that subscription tier upgrades are committed to the internal application database only upon successful cryptographic receipt validation.
- **Upstream Traces:** `SO-D-01.1-002`, `SO-D-08.1-002`, `PRIN-ENG-03`
- **Functional Traces:** `R7.1`, `R7.2` | `{U.C. 7.1}`, `{U.C. 7.2}`
- **Volere Fit Criterion:** Simulated unauthenticated or forged payment webhooks fail signature validation and produce zero changes in tenant billing status.
- **Verification Method:** `TEST` (Mock payment gateway webhook signature suite).

### `RN16`: Cryptographic Webhook Origin Verification
- **EARS Pattern:** Event-Driven
- **Statement:** When dispatching outbound event notifications to external webhook listeners, the system shall compute a cryptographic message authentication code across the event payload using a tenant-specific shared secret and transmit the authentication proof in the request headers.
- **Upstream Traces:** `SO-D-05.1-002`, `SO-D-08.1-002`, `PRIN-ENG-02`
- **Functional Traces:** `R8.1` | `{U.C. 8.1}`
- **Volere Fit Criterion:** Receiver test harness validates payload integrity and origin authenticity using the shared secret; any payload byte tampering invalidates the computed authentication proof.
- **Verification Method:** `TEST` (Webhook payload integrity and tamper assertion suite).

### `RN17`: Inbound API Token Mediation & Rate Limiting
- **EARS Pattern:** Event-Driven & Unwanted Behavior
- **Statement:** When an external productivity API client sends a request to TinyTask endpoints, the system shall authenticate the client token and evaluate invocation frequency against a maximum threshold of 100 requests per minute per tenant. If the threshold is exceeded, the system shall throttle requests and return HTTP 429 Too Many Requests with a `Retry-After` header.
- **Upstream Traces:** `SO-D-02.1-002`, `SO-D-05.1-002`, `PRIN-ENG-02`
- **Functional Traces:** `R8.2` | `{U.C. 8.2}`
- **Volere Fit Criterion:** Automated load generator exceeding 100 req/min receives HTTP 429 starting at request 101, recovering exactly when the time window resets.
- **Verification Method:** `TEST` (Automated API rate limiting and token validation harness).

### `RN18`: Non-Repudiable Security Audit Logging
- **EARS Pattern:** Ubiquitous & Event-Driven
- **Statement:** The system shall generate an immutable security audit record for all authentication attempts, privilege elevations, user deletions, subscription modifications, and permission rejections, containing timestamp, tenant ID, actor identity, action descriptor, and source IP address.
- **Upstream Traces:** `SO-D-03.1-002`, `PRIN-ENG-07`
- **Functional Traces:** `R1.1` to `R8.2` | All Use Cases
- **Volere Fit Criterion:** Audit log files are append-only; administrative users cannot alter or truncate audit entries; 100% of sensitive operations generate an audit log entry.
- **Verification Method:** `TEST` (Audit log generation and append-only tamper test).

---

## 4. Personal Data Protection Requirements (GDPR Specification — `RN19` to `RN26`)

### `RN19`: Registration Data Minimization by Default
- **EARS Pattern:** Ubiquitous
- **Statement:** The system shall collect only the minimum personal data fields necessary to establish user identity and billing contact (specifically: full name, business email address, and hashed credentials), and shall not enforce or require personal phone numbers, physical home addresses, or demographic markers.
- **Upstream Traces:** `PO-D-06.1-001`, `PRIN-ENG-06`
- **Functional Traces:** `R1.1` | `{U.C. 1.1}`
- **Volere Fit Criterion:** Database schema inspection confirms zero mandatory extraneous personal fields; registration form contains only the 3 strictly necessary identity fields.
- **Verification Method:** `INSPECT` (Data schema and user onboarding field audit).

### `RN20`: Structured Personal Data Portability & Export
- **EARS Pattern:** Event-Driven
- **Statement:** When an authenticated workspace user requests an export of their personal account data (under GDPR Art. 20), the system shall compile all profile attributes, authored comments, assigned tasks, and logged hours into a machine-readable JSON archive within 24 hours of the request.
- **Upstream Traces:** `PO-D-06.2-001`, `PRIN-ENG-06`
- **Functional Traces:** `R1.2` | `{U.C. 1.2}`
- **Volere Fit Criterion:** Export package contains 100% of user-generated data formatted in valid, schema-conforming JSON without inclusion of third-party personal data.
- **Verification Method:** `DEMONSTRATE` (End-to-end data portability generation and schema validation).

### `RN21`: Irreversible Data Subject Erasure & Pseudonymization
- **EARS Pattern:** Event-Driven
- **Statement:** When a workspace administrator or user executes an account termination request (under GDPR Art. 17), the system shall permanently purge the user's credentials and personal contact details within 30 days, while pseudonymizing historical task comments and timesheets to maintain organizational audit integrity without retaining identifiable personal markers.
- **Upstream Traces:** `PO-D-06.2-001`, `PRIN-ENG-06`
- **Functional Traces:** `R1.1`, `R1.2` | `{U.C. 1.1}`, `{U.C. 1.2}`
- **Volere Fit Criterion:** Post-erasure database search for the user's email or full name yields zero matches; historical records display a non-reversible pseudonym (e.g. `Deactivated User [ID: 9481]`).
- **Verification Method:** `TEST` (Automated account erasure pipeline and pseudonymization check).

### `RN22`: Purpose Limitation & Time Log Segregation
- **EARS Pattern:** State-Driven
- **Statement:** While processing logged billable hours and timesheet summaries, the system shall utilize time records strictly for project cost tracking and client invoicing, and shall prevent the extraction or profiling of individual employee performance metrics for unconsented secondary purposes.
- **Upstream Traces:** `PO-D-06.1-001`, `PRIN-ENG-03`, `PRIN-ENG-06`
- **Functional Traces:** `R6.1`, `R6.2` | `{U.C. 6.1}`, `{U.C. 6.2}`
- **Volere Fit Criterion:** Query interface and analytics exports restrict aggregations to project and workspace summaries; individual granular logs are accessible only to the author and the authorized workspace administrator.
- **Verification Method:** `ANALYZE` (Data flow audit verifying access controls on time logging entities).

### `RN23`: Personal Data Cryptographic Protection at Rest
- **EARS Pattern:** Ubiquitous
- **Statement:** The system shall cryptographically protect all persistent storage volumes, file assets, and database backups containing personal data at rest against unauthorized extraction using state-of-the-art cryptographic mechanisms.
- **Upstream Traces:** `PO-D-01.1-001`, `PRIN-ENG-01`
- **Functional Traces:** `R1.1`, `R1.2`, `R6.1` | `{U.C. 1.1}`, `{U.C. 1.2}`, `{U.C. 6.1}`
- **Volere Fit Criterion:** Storage infrastructure manifests and volume configuration scripts confirm transparent cryptographic protection is enabled with managed key rotation.
- **Verification Method:** `INSPECT` (Infrastructure-as-Code and volume configuration audit).

### `RN24`: Mandatory End-to-End Transport Layer Cryptographic Protection
- **EARS Pattern:** Ubiquitous & Unwanted Behavior
- **Statement:** The system shall cryptographically protect all personal and sensitive data in transit across public and untrusted networks against unauthorized disclosure and tampering, using state-of-the-art cryptographic communication mechanisms, and if an unencrypted connection attempt is detected, the system shall refuse the connection or enforce cryptographic upgrade.
- **Upstream Traces:** `PO-D-01.2-001`, `PRIN-ENG-01`
- **Functional Traces:** `R1.1` to `R8.2` | All Use Cases
- **Volere Fit Criterion:** 100% of network traffic traversing external boundaries is cryptographically protected; unencrypted transmission attempts fail closed.
- **Verification Method:** `TEST` (Automated network inspection verifying cryptographic transport protection on all external endpoints).

### `RN25`: Automated Orphan File Asset Cleanup & Expiration
- **EARS Pattern:** Event-Driven
- **Statement:** When a workspace project or task containing file attachments is deleted, the system shall schedule the unlinked storage objects for permanent deletion within 14 days, preventing indefinite storage of orphaned personal documents.
- **Upstream Traces:** `PO-D-06.1-001`, `PRIN-ENG-06`
- **Functional Traces:** `R4.2` | `{U.C. 4.2}`
- **Volere Fit Criterion:** Background cleanup job successfully purges unreferenced storage files older than 14 days; object store audit verifies zero orphaned attachments remain.
- **Verification Method:** `TEST` (Lifecycle expiration assertion on object storage).

### `RN26`: Privacy Audit Trail for Personal Data Modifications
- **EARS Pattern:** Event-Driven
- **Statement:** When an administrator or user modifies profile information, email preferences, or data export requests, the system shall record a privacy event in the audit log indicating the data subject ID, operator ID, field modified, and timestamp.
- **Upstream Traces:** `PO-D-03.1-001`, `PRIN-ENG-07`
- **Functional Traces:** `R1.1`, `R1.2`, `R6.1` | `{U.C. 1.1}`, `{U.C. 1.2}`, `{U.C. 6.1}`
- **Volere Fit Criterion:** 100% of profile update and data deletion requests generate a structured audit record verifiable by the Data Protection Lead.
- **Verification Method:** `INSPECT` (Privacy audit log completeness review).

---

## 5. Verification & Compliance Sign-Off

In accordance with ISO/IEC/IEEE 29148:2018, every requirement specified above has been verified against the five criteria of well-formed requirements:
1. **Necessity:** Fully traceable to GDPR Chapter III / Art. 32 and CRA Annex I.
2. **Feasibility:** Implementable within standard micro-tier multi-tenant cloud architectures.
3. **Clarity:** Expressed using deterministic EARS syntax patterns.
4. **Verifiability:** Governed by an empirical test method (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) with concrete Volere fit criteria.
5. **Consistency:** Free of conflicting constraints across security resilience and personal privacy.
