# Analytical Heuristics — Fail-Safe Defaults & Closed Failure States

Detailed technical heuristics for inspecting routing, authorization, and error handling against `PRIN-ENG-04`.

---

## 1. Default-Deny Routing & Ingress Heuristic (PRIN-ENG-04)

### Rule 1.1: Explicit Route Whitelisting
- Ingress routers and reverse proxies must enforce an explicit terminal catch-all rule:
  $$\mathtt{catch\_all} \longrightarrow \mathtt{REJECT}\ (404\ \text{or}\ 405)$$
- Requests with unmapped HTTP methods or unknown paths must never be proxied to internal application containers.

### Rule 1.2: Terminal Authorization Fallback
- Authorization decision logic must be structured so that failure to affirmatively match an `ALLOW` rule terminates in `DENY`.
- Missing attributes, corrupted tokens, or empty permission sets must evaluate to denial without exception.

---

## 2. Fail-Closed Resilience Heuristic (PRIN-ENG-04)

### Rule 2.1: Security Dependency Failures Must Fail Closed
- When upstream security systems (e.g. Identity Providers, Policy Decision Points, Token Introspection APIs, WAF services) fail, time out, or throw errors:
  1. The enforcement point MUST NOT grant access to the protected resource under the guise of "maintaining service availability".
  2. The enforcement point must fail closed by returning HTTP `503 Service Unavailable` with a standard `Retry-After` header.

### Rule 2.2: Opaque Client Errors & Sanitization
- Uncaught exceptions at application boundaries must never bubble raw database errors, system file paths, or stack traces to external callers:
  1. Emit an opaque JSON payload: `{"error": "internal_server_error", "request_id": "<uuid>"}`.
  2. Persist the full exception, call stack, and context internally to a secure, access-controlled log store.

---

## 3. Database Transaction & State Integrity (PRIN-ENG-04)

### Rule 3.1: Automated Rollback on Partial Failures
- Multi-step state modifications must execute within an explicit database transaction block.
- Any error occurring before transaction commit must trigger an immediate rollback, leaving zero orphaned records or inconsistent state.
