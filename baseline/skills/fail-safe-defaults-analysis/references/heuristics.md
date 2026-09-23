# Analytical Heuristics — Fail-Safe Defaults & Closed Failure States

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-04`.

---

## 1. Default-Deny Decision Paths (PRIN-ENG-04)

### Rule 1.1: Explicit Whitelist Evaluation
- Every decision point in a functional use case must evaluate against explicit affirmative criteria (e.g. valid credentials, authorized role, confirmed payment).
- Any unmodeled, unrecognized, or ambiguous input condition must automatically branch into the failure scenario (rejection).

### Rule 1.2: Terminal Rejection Fallbacks
- Alternative flows must never "fall through" into subsequent success steps without completing all prerequisite assertions.

---

## 2. Fail-Closed Dependency Resilience (PRIN-ENG-04)

### Rule 2.1: External Outage Fail-Closed
- When a use case relies on an external entity (e.g. identity verification, payment settlement, fraud evaluation):
  1. If the external dependency is unreachable, times out, or returns an error, the use case MUST NOT grant access or perform state mutations.
  2. The flow must terminate in a safe, closed state (action aborted, user notified with clear guidance).

### Rule 2.2: Atomic State Rollback
- Multi-step operations modifying multiple resources must maintain transactional integrity:
  $$\text{Failure at Step } N \implies \text{Rollback Steps } 1 \dots N-1$$
- Use cases must never leave partial state active when an intermediate step aborts.
