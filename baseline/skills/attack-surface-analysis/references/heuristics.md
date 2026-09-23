# Analytical Heuristics — Attack Surface & Peripheral Resilience

Technology-agnostic heuristics for inspecting functional Use Cases (`UC-*`) against `PRIN-ENG-02`.

---

## 1. Functional Entry Point Pruning (PRIN-ENG-02)

### Rule 1.1: Justified Invocation Triggers
- Every interaction step initiated by an actor must link directly to the core business purpose of the Use Case.
- Auxiliary user interactions (e.g. "try without account", "temporary anonymous workspace", "unauthenticated preview") that introduce public entry points into core application state must be eliminated from the functional baseline unless explicitly mandated by business scope.

### Rule 1.2: Diagnostic & Management Path Exclusion
- Functional Use Cases describing end-user tasks must never embed administrative or diagnostic side-channels (e.g. "Step 3: User or Support Agent can inspect internal worker memory").
- Administrative operations, system maintenance, and operational metrics must be defined in separate, dedicated, and access-restricted Administrative Use Cases (`UC-ADM-*`).

---

## 2. Peripheral Resilience in Functional Flows (PRIN-ENG-02)

### Rule 2.1: Equal Rigor on Asynchronous Ingress Triggers
- When a Use Case is triggered or updated by an asynchronous external actor (e.g. third-party payment notification, external identity assertion, automated supplier callback):
  1. The functional flow must require the external actor to prove identity and payload authenticity before any internal state change is evaluated.
  2. The flow must specify payload size bounding and replay resistance (e.g. event freshness check) as explicit preconditions in the use case.

### Rule 2.2: Unmediated Ingress Prohibited
- No functional use case step may depict an actor directly manipulating persistent storage, queues, or background workers without passing through a declared mediation gateway.
