# Analytical Heuristics — Requirements Verifiability & Atomicity

Detailed technical heuristics for evaluating and decomposing requirements into testable, verifiable specifications against `PRIN-REQ-01` through `PRIN-REQ-04`.

---

## 1. EARS Syntax Patterns (PRIN-REQ-04)

Requirements must conform to one of the five canonical Easy Approach to Requirements Syntax (EARS) patterns:

| Pattern Type | Syntax Template | Typical Use Case |
|---|---|---|
| **Ubiquitous** | The `<system>` SHALL `<action>`. | Invariant fundamental properties (e.g. data at rest encryption). |
| **Event-Driven** | *When* `<trigger>`, the `<system>` SHALL `<action>`. | User actions, API requests, state transitions. |
| **State-Driven** | *While* `<system state>`, the `<system>` SHALL `<action>`. | Operational modes (e.g. maintenance mode, degraded state). |
| **Unwanted Behavior** | *If* `<error condition / threat>`, *then* the `<system>` SHALL `<action>`. | Security anomalies, rate limiting, validation failures. |
| **Optional Feature** | *Where* `<feature is enabled>`, the `<system>` SHALL `<action>`. | Tenant-specific or subscription-tiered security modules. |

---

## 2. Subjective Term Replacement Table (PRIN-REQ-01, PRIN-REQ-04)

Whenever an ambiguous or subjective term is identified in a draft requirement, replace it with a quantified, testable threshold:

| Ambiguous Term | Why It Fails Verifiability | Quantified Replacement Pattern |
|---|---|---|
| **"securely"** | Subjective, cannot be tested directly. | Name the exact cryptographic primitive, key length, and mode (e.g. `AES-256-GCM with unique 96-bit nonce`). |
| **"fast" / "quickly"** | Dependent on environment and observer. | Bound by percentile and load: `within X ms for P95 at Y concurrent requests`. |
| **"adequate" / "appropriate"** | Legal hand-waving, unexecutable by dev. | Specify the exact technical standard or rule (e.g. `satisfies NIST SP 800-63B AAL2`). |
| **"gracefully"** | Undefined failure behavior. | Define exact HTTP response code, error JSON schema, and state rollback guarantees. |
| **"regularly"** | Ambiguous frequency. | Define exact cron schedule or trigger: `every 24 hours at 02:00 UTC`. |
| **"user-friendly"** | Aesthetic opinion. | Specify accessibility standard: `satisfies WCAG 2.1 Level AA`. |

---

## 3. Atomicity Decomposition Heuristic (PRIN-REQ-02)

### Rule 3.1: The Conjunction Rule
- If a requirement contains coordinating conjunctions (*and*, *as well as*, *or*, *plus*), test whether removing one half leaves a functional requirement.
- If yes, split into two separate requirements with sequential IDs.

### Rule 3.2: Single Verification Target
- A requirement is atomic if and only if a single test assertion (unit test method, integration test case, or lint rule) can return a binary PASS or FAIL result.
- If a requirement requires testing two unrelated subsystems (e.g. frontend display and backend database indexing), it must be split into two atomic requirements.
