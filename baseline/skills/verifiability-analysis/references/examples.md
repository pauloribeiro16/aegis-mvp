# End-to-End Case Studies — Requirements Verifiability & Atomicity

Realistic case studies showing how vague compliance mandates and PRD text are transformed into atomic, verifiable engineering specifications.

---

## Case Study 1: Transforming GDPR Art. 32 / CRA Annex I into Verifiable Requirements

### Context
A product manager drafting the security specification for TinyTask writes an initial compliance section based directly on high-level legal text.

### Initial Draft Requirements

> **Section 4.2 Security Specification (Initial Draft):**  
> 1. "The service must ensure appropriate technical and organizational measures to protect personal data against accidental loss, alteration, or unauthorized disclosure."  
> 2. "The application should have robust logging and monitoring to detect security incidents quickly."  
> 3. "Software updates must be delivered securely to customers without introducing bugs."

### Critique & Failure Analysis

- **Item 1:** Direct copy-paste of GDPR Art. 32 prose. Completely unverifiable. What constitutes "appropriate"? What specific measures? What tests prove compliance?
- **Item 2:** Uses subjective terms "robust" and "quickly". Does not specify what events are logged, where logs are stored, log retention periods, or time-to-alert thresholds.
- **Item 3:** Uses non-normative "should", subjective "securely", and an unfalsifiable negative "without introducing bugs".

---

### Remediated Atomic Engineering Specifications

#### `REQ-SEC-DATA-001` (Data-at-Rest Encryption)
- **EARS Pattern:** Ubiquitous
- **Specification:** The Database Subsystem SHALL encrypt all persistent storage volumes, tablespaces, and automated snapshots using an AEAD cipher (e.g. AES-256-GCM) with customer-isolated encryption keys.
- **Verification Method:** `[Infrastructure Configuration Audit]` (Automated policy test asserting persistent storage encryption and key isolation).
- **Traceability:** `PO-D-03.1-001` (GDPR Art. 32(1)(a)).

#### `REQ-SEC-AUDT-001` (Security Event Audit Logging)
- **EARS Pattern:** Event-Driven
- **Specification:** When an authentication event (login success, login failure, password reset) or authorization failure occurs, the Audit Logger SHALL write a structured JSON event containing timestamp (ISO 8601 UTC), actor identity (`user_id` or `anonymous`), client IP, event type, and outcome within 100 milliseconds to an append-only log stream.
- **Verification Method:** `[Automated Integration Test]` (Triggers failed login; polls test log stream; asserts JSON schema and field contents).
- **Traceability:** `SO-D-07.1-001` (CRA Annex I Part I §2(a)).

#### `REQ-SEC-UPDT-001` (Cryptographically Signed Over-the-Air Updates)
- **EARS Pattern:** Event-Driven
- **Specification:** When a client application downloads a software update package, the update installer SHALL verify the Ed25519 digital signature of the update binary against the embedded vendor public key prior to executing the installation script.
- **Verification Method:** `[Automated Integration Test]` (Attempts update with untrusted/tampered binary; asserts installation aborts with exit code 128 and error message `signature_verification_failed`).
- **Traceability:** `SO-D-06.1-001` (CRA Annex I Part I §2(e)).

### Traceability & Verifiability Ledger

| Original Statement | Flaw | New Atomic ID | EARS Syntax | Test Method |
|---|---|---|---|---|
| "appropriate measures to protect data" | Legal generality; no technical bounds | `REQ-SEC-DATA-001` | Ubiquitous (*The system SHALL*) | IaC Terraform Compliance Spec |
| "robust logging... detect incidents quickly" | Subjective adjectives ("robust", "quickly") | `REQ-SEC-AUDT-001` | Event-Driven (*When... SHALL*) | Automated Test verifying JSON log stream |
| "updates delivered securely without bugs" | Non-normative "should", unfalsifiable negative | `REQ-SEC-UPDT-001` | Event-Driven (*When... SHALL*) | Tampered Binary Integration Test (Ed25519) |
