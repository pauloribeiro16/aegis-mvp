# Evaluation Checklist — Attack Surface & Peripheral Resilience

Verification checklist for auditing functional Use Cases (`UC-*`) against `PRIN-ENG-02`.

---

## 1. Use Case Trigger & Entry Point Pruning (`PRIN-ENG-02`)

- [ ] **Justified Public Triggers:** Every public or external entry point corresponds to a strictly necessary functional requirement.
- [ ] **No Unauthenticated State Mutations:** Use case steps that mutate application state (e.g. creating tasks, altering settings) require an authenticated actor.
- [ ] **Administrative Flows Segregated:** Diagnostic and administrative actions are segregated into separate, privileged Use Cases rather than embedded as side-channels in user workflows.

---

## 2. Peripheral Resilience & Auxiliary Ingress (`PRIN-ENG-02`)

- [ ] **Cryptographic Verification of External Triggers:** Asynchronous external events (webhooks, notifications) explicitly require cryptographic origin verification.
- [ ] **Replay & Freshness Controls:** External callback flows include timestamp validation and idempotency checks to prevent event replay attacks.
- [ ] **Rate Limiting & Payload Ceilings:** External entry points specify payload size bounds and rate limits as functional preconditions.
- [ ] **Mediation Enforcement:** No use case step depicts an actor directly addressing background queues or persistent stores without passing through an authenticating mediation component.
