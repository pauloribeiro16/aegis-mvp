# Evaluation Checklist — Requirements Verifiability & Atomicity

Comprehensive verification checklist for evaluating security and privacy requirements against `PRIN-REQ-01` through `PRIN-REQ-04`.

---

## 1. Verifiability & Falsifiability (`PRIN-REQ-01`)

- [ ] **Deterministic Pass/Fail Criteria:** Every requirement can be verified by a deterministic automated test, tool, or objective inspection with a binary Pass or Fail outcome.
- [ ] **No Subjective Adjectives:** Words such as "adequate", "appropriate", "fast", "robust", "properly", "seamless", "user-friendly", and "securely" have been replaced with quantified numerical values or formal standards.
- [ ] **Automated Test Method Defined:** Each requirement specifies a verification mechanism (`[Unit Test]`, `[Integration Test]`, `[SAST Rule]`, `[DAST Assertion]`, `[IaC Compliance Test]`).

---

## 2. Atomicity & Scope (`PRIN-REQ-02`)

- [ ] **Single Functional Concern:** Each requirement addresses exactly one behavior, state, or constraint.
- [ ] **No Compound Statements:** Conjunctions ("and", "or", "while also") do not combine multiple independent system responses into a single statement.
- [ ] **Isolated Acceptance:** If any one sub-behavior fails, exactly one requirement fails without ambiguity regarding the remaining system functions.

---

## 3. Traceability (`PRIN-REQ-03`)

- [ ] **Canonical ID Assignment:** Every requirement has a standardized, stable identifier (e.g. `REQ-SEC-DATA-001`, `REQ-PRV-MIN-002`).
- [ ] **Upstream Objective Mapping:** Every requirement explicitly cites its parent Operational Objective (`PO-D-XX.Y-NNN` or `SO-D-XX.Y-NNN`).
- [ ] **No Orphan Requirements:** Requirements that cannot be traced to an engineering principle, architectural baseline, or operational objective are flagged for removal.

---

## 4. Unambiguous Specification & Syntax (`PRIN-REQ-04`)

- [ ] **EARS Syntax Conformance:** The requirement adheres strictly to one of the five EARS patterns (*Ubiquitous*, *Event-Driven*, *State-Driven*, *Unwanted Behavior*, or *Optional Feature*).
- [ ] **RFC 2119 Normative Verbs:** The statement uses capitalized normative verbs (**SHALL** / **SHALL NOT** for mandatory constraints; **SHOULD** only for optional guidance).
- [ ] **Active Voice & Explicit Actor:** The statement identifies the exact system component responsible for executing the action (e.g. "The Authentication Service SHALL...", never "It will be...").
