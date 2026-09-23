---
name: verifiability-analysis
description: Evaluates security and privacy requirements derived from functional use cases to eliminate subjective qualifiers and enforce atomic, verifiable EARS syntax.
---

# Requirements Verifiability & Atomicity Analysis

Evaluates security and privacy requirements derived from functional Use Cases (`UC-*`) to eliminate ambiguous or subjective phrasing, decompose compound requirements into atomic statements, and guarantee that every requirement has a deterministic verification method.

> **Target Principle:**  
> - `PRIN-ENG-05` (Requirement Verifiability & Atomicity — ISO/IEC/IEEE 29148 / EARS)

---

## 1. Operational Mandate & Scope

The agent acts as a Systems Requirements Engineer and Compliance Lead reviewing **Requirements Derived from Functional Use Cases (`UC-*`)**:
- **Requirement Statements:** Candidate security (`REQ-SEC-*`) and privacy (`REQ-PRV-*`) requirements binding a functional use case.
- **Statement Syntax & Quality:** Inspecting against the ISO/IEC/IEEE 29148:2018 quality characteristics (singularity, unambiguous phrasing, necessity, verifiability).
- **Verification Methods:** Confirming each requirement specifies an empirical verification category (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`).

The analysis is **technology-agnostic**: it enforces linguistic rigor, formal EARS grammar, and testability without prescribing specific test frameworks, programming languages, or execution environments.

---

## 2. Evaluation Procedure

1. **Subjective Vocabulary Scan:** Scan candidate requirement text for non-verifiable words ("appropriate", "adequate", "sufficient", "fast", "properly", "robust", "securely", "gracefully").
2. **Atomicity Decomposition (`PRIN-ENG-05`):** Detect compound sentences joined by coordinating conjunctions ("and", "or", "as well as"). Split compound requirements into atomic statements with individual identifiers.
3. **EARS Grammar Structuring:** Ensure the requirement conforms strictly to one of the canonical EARS patterns (*When... SHALL*, *While... SHALL*, *If... then SHALL*, or *The system SHALL*).
4. **Verification Method Binding:** Attach an explicit verification method category (`TEST`, `INSPECT`, `DEMONSTRATE`, `ANALYZE`) with an objective pass/fail threshold.
5. **Output Delivery:** Produce:
   - Statement Defect Annotations (ambiguity, compound statements).
   - Decomposed Atomic EARS Requirements.
   - Requirements Verifiability Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Candidate Requirement for Task Creation (`UC-03`)

> "The task attachment subsystem should securely store uploaded files, verify file safety fast, and handle storage quota exceeded errors gracefully."

---

### 3.2 Step-by-Step Analytical Evaluation

1. **Defect 1 — Non-Normative Modal Verb:** Uses "should" instead of RFC 2119 normative "SHALL".
2. **Defect 2 — Subjective & Non-Verifiable Adjectives:** Uses "securely store", "verify file safety fast", and "handle errors gracefully". An engineer or auditor cannot write a binary pass/fail test for "fast" or "gracefully".
3. **Defect 3 — Compound Concern (`PRIN-ENG-05`):** Combines three disjoint concerns (at-rest encryption, malicious file screening, and quota error handling) into a single sentence.

---

### 3.3 Remediated Atomic Requirements (EARS Syntax)

#### `REQ-SEC-DATA-010` (Attachment At-Rest Encryption)
- **EARS Pattern:** Ubiquitous
- **Specification:** The Storage Subsystem SHALL encrypt all persistent task attachment objects at rest using an AEAD cryptographic cipher with keys isolated per tenant.
- **Verification Method:** `INSPECT` (Verification of at-rest encryption configuration and key isolation).
- **Parent Use Case:** `UC-03` (Task Attachment Ingestion).

#### `REQ-SEC-MALW-001` (Pre-Persistence Attachment Screening)
- **EARS Pattern:** Event-Driven
- **Specification:** When an attachment file is received, the Ingestion Gateway SHALL execute malware signature and file structure verification within 1500 milliseconds for files under 25 megabytes, rejecting infected files before committing them to persistent storage.
- **Verification Method:** `TEST` (Automated integration test uploading standardized EICAR test file; asserts immediate rejection).
- **Parent Use Case:** `UC-03` (Task Attachment Ingestion).

#### `REQ-SEC-QUOT-001` (Deterministic Quota Error Handling)
- **EARS Pattern:** Unwanted Behavior
- **Specification:** If an uploaded file causes the workspace storage volume to exceed its allocated quota, then the Storage Subsystem SHALL terminate the upload, discard all temporary file fragments, and return an explicit quota exceeded error.
- **Verification Method:** `TEST` (Automated test filling quota to 100%; asserts subsequent upload fails and leaves zero orphaned fragments).
- **Parent Use Case:** `UC-03` (Task Attachment Ingestion).

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for EARS grammar patterns and subjective term replacement tables.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for compound and untestable requirement smells.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for full Use Case requirement decomposition walkthroughs.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured requirements verification checklist.
