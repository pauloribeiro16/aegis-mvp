# Evaluation Checklist — Fail-Safe Defaults & Closed Failure States

Comprehensive verification checklist for evaluating routing, authorization, and error handling against `PRIN-ENG-04`.

---

## 1. Routing & Ingress Default-Deny (`PRIN-ENG-04`)

- [ ] **Default Catch-All Route:** The ingress reverse proxy or API gateway terminates unmatched routes with an explicit HTTP 404 or 405 error, rather than serving file directories or falling through.
- [ ] **Method Whitelisting:** HTTP methods not explicitly declared on a route are terminated with HTTP 405 Method Not Allowed.
- [ ] **Firewall Ingress Default Drop:** Cloud security groups and firewall policies enforce a terminal `DROP` rule on all inbound traffic.

---

## 2. Authorization Fallbacks (`PRIN-ENG-04`)

- [ ] **Terminal Deny Fallback:** Authorization policy evaluators default to `DENY` when no explicit `ALLOW` rule matches.
- [ ] **Fail-Closed on Auth Outages:** When an external identity provider (IDP) or token introspection endpoint times out or returns an error, access is denied (HTTP 503), never granted.
- [ ] **Missing Token Handling:** Unauthenticated requests are rejected immediately at the gateway layer prior to invoking domain logic.

---

## 3. Exception Handling & Transaction Integrity (`PRIN-ENG-04`)

- [ ] **Opaque Client Errors:** Global error handlers intercept uncaught exceptions and return sanitized, opaque JSON error responses (`{"error": "internal_error"}`).
- [ ] **No Stack Trace Exposure:** Stack traces, internal file paths, environment variables, and SQL query strings are never emitted in client responses.
- [ ] **Automated Transaction Rollback:** Multi-table or distributed mutations are wrapped in atomic transactions that automatically roll back upon any exception.
- [ ] **Idempotent Retry Handling:** Webhook and event consumers verify idempotency keys to ensure retried failures do not duplicate side-effects.
