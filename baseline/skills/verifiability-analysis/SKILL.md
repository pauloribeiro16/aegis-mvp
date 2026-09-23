---
name: verifiability-analysis
description: Decomposes ambiguous or compound security and privacy requirements into atomic, unambiguous, and automated-testable specifications using EARS syntax.
---

# Requirements Verifiability & Atomicity Analysis

Evaluates security and privacy requirement specifications to eliminate ambiguous phrasing, decompose compound requirements into atomic statements, and guarantee that every requirement has a deterministic, testable verification method.

> **Target Principle:**  
> - `PRIN-ENG-05` (Requirement Verifiability & Atomicity — ISO/IEC/IEEE 29148 / EARS)

---

## 1. Operational Mandate & Scope

The agent acts as a Principal Requirements Engineer and Compliance QA Lead reviewing:
- **Requirement Specifications:** System Requirements Specifications (SRS), Product Requirement Documents (PRDs), RFC security sections.
- **Security & Privacy Objectives:** Operational Objectives (`PO-` / `SO-`), regulatory transpositions, architecture acceptance criteria.
- **Test Plans & Acceptance Criteria:** QA test suites, automated security regression assertions, compliance audit statements.

The goal is to eliminate untestable adjectives ("secure", "robust", "fast", "gracefully"), split compound statements joined by "and/or", and convert statements into deterministic EARS syntax with associated automated tests.

---

## 2. Evaluation Procedure

1. **Ambiguity & Jargon Scan:** Scan candidate text for subjective adjectives and adverbs:
   - *Prohibited Terms:* "appropriate", "adequate", "sufficient", "seamless", "user-friendly", "robust", "securely", "properly", "fast", "gracefully".
2. **Atomicity Decomposition (`PRIN-REQ-02`):** Search for conjunctions ("and", "as well as", "while also"). Split compound requirements so that each statement specifies exactly **one** system response to **one** condition.
3. **EARS Formatting (`PRIN-REQ-04`):** Restructure each requirement using the Easy Approach to Requirements Syntax:
   - **Event-Driven:** *When* `<trigger>`, *the* `<system>` *SHALL* `<action>`.
   - **State-Driven:** *While* `<state>`, *the* `<system>` *SHALL* `<action>`.
   - **Unwanted Behavior:** *If* `<trigger/fault>`, *then the* `<system>` *SHALL* `<action>`.
4. **Deterministic Verification Method Assignment (`PRIN-REQ-01`):** Assign each atomic requirement an explicit verification method:
   - `[Automated Unit/Integration Test]`
   - `[Static Analysis / SAST Rule]`
   - `[DAST / Penetration Assertion]`
   - `[Infrastructure / Config Audit]`
5. **Traceability Binding (`PRIN-REQ-03`):** Map each requirement back to its parent Operational Objective (`PO-` or `SO-`).
6. **Ledger Output:** Produce a Requirements Verifiability Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Flawed & Compound PRD Requirement

> "The authentication system should securely store user passwords, provide fast login, and handle failed login attempts properly to prevent brute-force attacks."

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-REQ-01` & `PRIN-REQ-04` (Unambiguous & Verifiable):**
   - Phrased with non-normative modal verbs ("should" instead of RFC 2119 "SHALL").
   - Contains untestable subjective qualifiers: "securely store", "fast login", "properly handle". A QA engineer cannot write a deterministic pass/fail assertion for "fast" or "properly".
2. **Violation of `PRIN-REQ-02` (Atomicity):**
   - Merges three distinct architectural concerns into a single sentence: password hashing, authentication latency, and brute-force mitigation.
3. **Violation of `PRIN-REQ-03` (Traceability):**
   - Missing explicit identifier and upstream objective citation.

### 3.3 Remediated Atomic Requirements (EARS Syntax)

#### `REQ-SEC-AUTH-001` (Password Hashing Function)
- **Specification:** When persisting new or updated user credentials, the Authentication Service SHALL hash the password using Argon2id with parameters: memory cost = 64 MiB (`m=65536`), time cost = 3 iterations (`t=3`), parallelism = 4 threads (`p=4`), and a cryptographically secure random salt of at least 16 bytes.
- **Verification Method:** `[Automated Unit Test]` (Asserts hashing output format, algorithm string, and parameter tags upon user registration).
- **Parent Objective:** `SO-D-03.1-001` (Cryptographic Protections).

#### `REQ-SEC-AUTH-002` (Authentication Latency SLA)
- **Specification:** When processing a valid authentication request, the Ingress API SHALL respond with HTTP 200 within 250 milliseconds for the 95th percentile under a sustained load of 200 concurrent requests/second.
- **Verification Method:** `[Performance / Load Test]` (Automated k6 / Gatling pipeline stage in staging).
- **Parent Objective:** `SO-D-03.1-002` (Service Availability).

#### `REQ-SEC-AUTH-003` (Brute-Force Rate Limiting & Error Timing)
- **Specification:** If more than 5 failed authentication attempts occur for a single username or source IP within a 60-second sliding window, then the Authentication Gateway SHALL return HTTP 429 (Too Many Requests) with a `Retry-After: 60` header for all subsequent attempts for the remainder of that window.
- **Verification Method:** `[Automated Integration Test]` (Submits 6 sequential bad credentials; asserts 6th request receives HTTP 429 with `Retry-After`).
- **Parent Objective:** `SO-D-03.1-003` (Abuse Prevention).

### 3.4 Requirements Verifiability Ledger

| Original Text Segment | Flaw Detected | Remediated ID | EARS Pattern | Verification Method |
|---|---|---|---|---|
| "securely store user passwords" | Subjective adjective; no algorithm specified | `REQ-SEC-AUTH-001` | Event-Driven (*When... SHALL*) | Automated Unit Test (Argon2id parameters) |
| "provide fast login" | Untestable performance term; no metric | `REQ-SEC-AUTH-002` | Event-Driven (*When... SHALL*) | Load Test (P95 $\le$ 250ms @ 200 rps) |
| "handle failed logins properly" | Ambiguous adverb; unstated rate limit | `REQ-SEC-AUTH-003` | Unwanted Behavior (*If... then SHALL*) | Integration Test (HTTP 429 after 5 fails) |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for EARS syntax templates and the subjective vocabulary replacement table.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for compound run-on requirements and untestable compliance prose.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for full PRD and compliance requirement transformations.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured requirements verification checklist.
