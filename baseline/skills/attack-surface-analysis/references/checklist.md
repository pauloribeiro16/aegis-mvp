# Evaluation Checklist — Attack Surface & Peripheral Resilience

Comprehensive verification checklist for assessing systems against `PRIN-MOD-03` and `PRIN-SEC-08`.

---

## 1. Network & Port Exposure (`PRIN-MOD-03`)

- [ ] **Public Port Minimization:** Only standard HTTPS ingress (port 443) is exposed to the public internet (`0.0.0.0/0`).
- [ ] **Data Store Isolation:** Database listeners (PostgreSQL `5432`, MySQL `3306`, MongoDB `27017`), caches (Redis `6379`, Memcached `11211`), and message queues (RabbitMQ `5672`, Kafka `9092`) have no public host port mappings.
- [ ] **SSH / RDP Disablement:** Administrative remote access ports (22, 3389) are prohibited on public interfaces and restricted to private VPN/bastion access.

---

## 2. API Routes & Endpoint Pruning (`PRIN-MOD-03`)

- [ ] **Diagnostic & Profiling Routes:** Endpoints such as `/debug/pprof/*`, `/actuator/*`, `/trace`, and `/env` are disabled or excluded from production builds.
- [ ] **Metrics Segregation:** Prometheus `/metrics` is bound exclusively to an internal management interface or protected via mutual TLS (mTLS).
- [ ] **Interactive Documentation:** Swagger UI (`/swagger-ui.html`, `/docs`) and GraphQL playgrounds are disabled in production environments.
- [ ] **Wildcard Route Rejection:** Ingress reverse proxy returns HTTP 404/405 for any unmatched paths or unwhitelisted HTTP verbs (`TRACE`, `TRACK`).
- [ ] **Strict CORS Whitelist:** `Access-Control-Allow-Origin` specifies exact trusted domains; wildcards (`*`) combined with credentials (`Access-Control-Allow-Credentials: true`) are strictly forbidden.

---

## 3. Peripheral Ingress & Webhook Resilience (`PRIN-SEC-08`)

- [ ] **Cryptographic Signature Verification:** Inbound third-party webhooks enforce HMAC SHA-256 signature verification using pre-shared secrets.
- [ ] **Timing-Safe Verification:** Signature comparison uses constant-time string comparison (`crypto.timingSafeEqual`) to prevent timing side-channel attacks.
- [ ] **Timestamp Freshness Window:** Inbound webhook payloads include a timestamp header verified within a $\le 300$-second tolerance window.
- [ ] **Replay Protection:** Unique event IDs from validated webhook payloads are checked against an ephemeral replay cache.
- [ ] **Request Body Limits:** Public callback endpoints enforce an explicit payload size ceiling (e.g. $\le 256$ KB) prior to buffer parsing.
- [ ] **Uniform Rate Limiting:** Webhook and public auxiliary endpoints enforce rate limiting that matches or exceeds the stringency applied to primary user endpoints.
