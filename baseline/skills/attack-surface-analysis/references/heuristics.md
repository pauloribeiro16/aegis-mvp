# Analytical Heuristics — Attack Surface & Peripheral Resilience

Detailed technical heuristics for inspecting interface definitions, deployment descriptors, and network policies against `PRIN-MOD-03` and `PRIN-SEC-08`.

---

## 1. Interface Pruning Heuristic (PRIN-MOD-03)

### Rule 1.1: Default-Deny Route Registration
- Every route exposed on an ingress gateway must be explicitly registered in the routing catalog.
- Wildcard route catch-alls (e.g. `/api/* -> upstream_handler`) that forward unmatched paths to backend frameworks without validation violate the principle. Unmatched paths must terminate at the reverse proxy with an immediate HTTP `404 Not Found` or `400 Bad Request`.

### Rule 1.2: Diagnostic & Management Interface Segregation
- Secondary operational interfaces must never share an ingress port or public IP address with core application routes:
  1. **Prometheus Metrics (`/metrics`):** Must bind to a dedicated internal port (e.g. `9090` or `9102`) bound to `127.0.0.1` or the private container subnet (`10.0.0.0/8`).
  2. **Runtime Profiling & Diagnostics (`/debug/pprof`, `/actuator`, `/trace`):** Must be excluded entirely from production container images or disabled via configuration flags (`PPROF_ENABLED=false`, `management.endpoints.web.exposure.exclude=*`).
  3. **Interactive Documentation UIs (`/docs`, `/swagger-ui.html`, `/redoc`):** In production environments, interactive documentation consoles must be either disabled or protected behind enterprise single sign-on (SSO) with role-based access control.

### Rule 1.3: HTTP Verb & Method Whitelisting
- Ingress routers must reject HTTP methods not explicitly implemented by the downstream route.
- Methods such as `TRACE`, `TRACK`, `CONNECT`, and `OPTIONS` (unless handled by a strict CORS preflight handler) must be terminated at the edge with HTTP `405 Method Not Allowed`.

---

## 2. Weakest Link Resilience Heuristic (PRIN-SEC-08)

### Rule 2.1: Asynchronous Callback & Webhook Verification
- Ingress points receiving external event notifications (e.g. Stripe, GitHub, SendGrid, Twilio) operate outside the primary user authentication session. They must not rely on obscurity or unprotected endpoints.
- Mandatory controls:
  1. **Cryptographic Signature Verification:** Every inbound payload must include a signed HMAC hash in an HTTP header (e.g. `X-Hub-Signature-256`, `Stripe-Signature`). The receiver must compute the HMAC using a pre-shared secret and verify it using constant-time comparison (`crypto.timingSafeEqual`) to prevent timing attacks.
  2. **Timestamp Freshness & Replay Prevention:** Signatures must bind a UNIX timestamp (`t=...`). Payloads with timestamps deviating by more than 300 seconds from server clock must be rejected. Validated event IDs must be recorded in an ephemeral replay cache (Redis TTL: 10 minutes).
  3. **Strict Payload Size Limits:** Webhook ingestion endpoints must enforce explicit request body limits (e.g. `client_max_body_size 256k;`) before JSON parsing to prevent unauthenticated memory exhaustion.

### Rule 2.2: Ingress Rate Limiting Equality
- Auxiliary listeners and public callback routes must have equal or stricter rate-limiting thresholds than primary user authentication endpoints.
- Unauthenticated public endpoints must enforce token-bucket or sliding-window rate limiting keyed by source IP and CIDR subnet (e.g. maximum 60 requests/minute per `/24` IPv4 block).
