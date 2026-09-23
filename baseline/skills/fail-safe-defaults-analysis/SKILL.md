---
name: fail-safe-defaults-analysis
description: Evaluates routing fallbacks, authorization middleware, exception handling, and circuit breakers to ensure systems fail securely into a closed, default-deny state.
---

# Fail-Safe Defaults & Closed Failure Analysis

Inspects ingress routing configurations, authorization middleware, exception handlers, and external dependency circuit breakers to verify that access decisions default to refusal and that unexpected failures terminate in a secure closed state.

> **Target Principle:**  
> - `PRIN-ENG-04` (Fail-Safe Defaults & Closed Failure States — Saltzer & Schroeder / OWASP)

---

## 1. Operational Mandate & Scope

The agent acts as a Systems Resilience & Security Architect reviewing:
- **Routing & Ingress Gateways:** Reverse proxy catch-alls, firewall default policies, API gateway route tables.
- **Authorization Decision Engines:** Middleware pipelines, Policy Decision Points (PDPs), role evaluators.
- **Exception & Error Handlers:** Global error middleware, uncaught exception handlers, database transaction rollbacks.
- **Circuit Breakers & Degraded States:** Upstream service failure handling (e.g. auth service timeouts, external IDP outages).

The goal is to guarantee that whenever a condition is not explicitly satisfied or an error occurs, the system defaults to denial of access and safe rollback.

---

## 2. Evaluation Procedure

1. **Default-Deny Policy Verification:** Inspect routing and authorization rule sets. Confirm that access is denied unless an explicit affirmative rule permits it.
2. **Fail-Open vs Fail-Closed Triage:** Evaluate system behavior when external security dependencies (LDAP, OAuth2/OIDC IDP, token introspection, policy engines) time out or return errors. Verify that the gateway fails closed (rejects requests with HTTP 503/500).
3. **Exception Boundary Leakage:** Inspect global error handling. Confirm that internal errors emit opaque error codes (e.g. `{"error": "internal_error", "reference_id": "err_9812"}`) and never disclose stack traces, memory dumps, or SQL query strings.
4. **State Machine & Transaction Rollback:** Ensure that aborted operations trigger automated database transaction rollbacks, preventing partial state corruption.
5. **Ledger Output:** Produce a Fail-Safe Defaults Audit Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Vulnerable Authorization & Error Handling Middleware

```python
# FastAPI / Flask routing middleware
@app.middleware("http")
async def authorization_middleware(request: Request, call_next):
    user_token = request.headers.get("Authorization")
    
    try:
        auth_decision = await verify_with_auth_service(user_token)
        if auth_decision == "ALLOW":
            return await call_next(request)
        elif auth_decision == "DENY":
            return JSONResponse(status_code=403, content={"error": "Access Denied"})
    except TimeoutError:
        # SMELL 1: Fails open on auth service timeout to 'preserve availability'
        logger.warning("Auth service timed out. Allowing request through in degraded mode.")
        return await call_next(request)
    except Exception as e:
        # SMELL 2: Returns raw exception details and stack trace to client
        return JSONResponse(status_code=500, content={"error": str(e), "trace": traceback.format_exc()})

    # SMELL 3: Missing fallback return; unhandled decision falls through to allow
    return await call_next(request)
```

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-ENG-04` (Fail-Open on Dependency Outage):**
   - When `verify_with_auth_service` times out, the middleware executes `call_next(request)`, granting unauthenticated callers full access to private endpoints.
   - **Remediation:** Must fail closed. An authentication outage must return HTTP 503 Service Unavailable, never allow unauthenticated execution.
2. **Violation of `PRIN-ENG-04` (Uncaught Exception Leakage):**
   - The catch block returns `traceback.format_exc()` directly to the client, exposing file paths, library versions, and database query strings to attackers.
   - **Remediation:** Log the full trace internally with a correlation ID; return a sanitized, opaque error response.
3. **Violation of `PRIN-ENG-04` (Missing Default-Deny Fallback):**
   - If `auth_decision` is neither "ALLOW" nor "DENY" (e.g. empty or unexpected status), execution falls through to `call_next`.
   - **Remediation:** Explicit terminal default return HTTP 403 Forbidden.

### 3.3 Remediated Middleware Specification

```python
@app.middleware("http")
async def authorization_middleware(request: Request, call_next):
    user_token = request.headers.get("Authorization")
    correlation_id = str(uuid.uuid4())
    
    try:
        auth_decision = await verify_with_auth_service(user_token)
        if auth_decision == "ALLOW":
            return await call_next(request)
            
        # Explicit denial
        return JSONResponse(
            status_code=403,
            content={"error": "access_denied", "correlation_id": correlation_id}
        )
    except TimeoutError:
        # Hardened: Fail closed upon authentication service failure
        logger.error(f"[{correlation_id}] Auth service timeout. Failing closed.")
        return JSONResponse(
            status_code=503,
            headers={"Retry-After": "30"},
            content={"error": "auth_service_unavailable", "correlation_id": correlation_id}
        )
    except Exception as e:
        # Hardened: Opaque client response; internal debug logging
        logger.exception(f"[{correlation_id}] Unhandled middleware error: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": "internal_server_error", "correlation_id": correlation_id}
        )
```

### 3.4 Fail-Safe Defaults Audit Ledger

| Component / Path | Initial Handling | Hazard | Remediated Handling | Principle |
|---|---|---|---|---|
| Auth Timeout | Fails open (`call_next`) | Total auth bypass during network degradation | **Fails closed**: Returns HTTP 503 + Retry-After | `PRIN-ENG-04` |
| Exception Handler | Emits `traceback.format_exc()` | System path and environment disclosure | **Sanitized**: Opaque error JSON with UUID correlation | `PRIN-ENG-04` |
| Decision Fallthrough | Implicit pass-through | Unmodeled states execute unauthenticated | **Default-Deny**: Explicit terminal HTTP 403 fallback | `PRIN-ENG-04` |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for fail-closed timeout algorithms, circuit breaker states, and error sanitization rules.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for fail-open authorization bypasses, stack trace exposures, and unhandled promise rejections.
- **End-to-End Case Studies:** Consult [`references/examples.md`](references/examples.md) for gateway circuit breaker and database transaction rollback scenarios.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured fail-safe defaults checklist.
