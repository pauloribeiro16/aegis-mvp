# End-to-End Case Studies — Attack Surface & Peripheral Resilience

Realistic, comprehensive before-and-after scenarios demonstrating how to inspect, triage, and remediate attack surface exposures.

---

## Case Study 1: SaaS Ingress Gateway & REST API Hardening

### Context
A multi-tenant SaaS application exposes a customer-facing API for project and task management, alongside integration endpoints for third-party tools.

### Initial (Vulnerable) Ingress & OpenAPI Configuration

```yaml
openapi: 3.1.0
info:
  title: Task Management Gateway
  version: 2.1.0
paths:
  /v1/auth/login:
    post:
      summary: User authentication
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
      responses:
        '200':
          description: JWT returned
  /v1/projects:
    get:
      summary: List user projects
      security:
        - BearerJWT: []
      responses:
        '200':
          description: Success
  /v1/admin/cache/clear:
    post:
      summary: Flush Redis Cache
      # SMELL 1: Admin utility route exposed on customer-facing API
      responses:
        '200':
          description: Flushed
  /v1/integrations/github/webhook:
    post:
      summary: Receive GitHub commit events
      # SMELL 2: No signature verification schema, no rate limits
      responses:
        '200':
          description: Event accepted
  /metrics:
    get:
      summary: Prometheus scrape endpoint
      # SMELL 3: Operational metrics exposed on public gateway
      responses:
        '200':
          description: OpenMetrics text
  /docs:
    get:
      summary: Interactive Swagger UI
      # SMELL 4: Interactive API exploration exposed in production
      responses:
        '200':
          description: HTML UI
```

### Analysis & Findings

1. **Administrative Route Exposure (`PRIN-MOD-03`):**  
   `/v1/admin/cache/clear` is accessible on the public internet. An attacker discovering this route can trigger denial-of-service by thrashing application caches.
2. **Operational Telemetry Exposure (`PRIN-MOD-03`):**  
   `/metrics` leaks JVM/Go garbage collection stats, request counts, and internal microservice names to anonymous users.
3. **Peripheral Ingress Weakness (`PRIN-SEC-08`):**  
   `/v1/integrations/github/webhook` allows unauthenticated POST requests, allowing malicious actors to inject fake webhook events and trigger unauthorized pipeline executions.
4. **Interactive Documentation Exposure (`PRIN-MOD-03`):**  
   `/docs` exposes the full API schema, facilitating automated vulnerability scanning.

---

### Remediated Architecture & Configuration

#### 1. Network & Router Segregation (Traefik / Nginx Ingress)
- Bind administrative and operational telemetry routes exclusively to a private internal listener on port `9090`, accessible only by Prometheus and admin bastion hosts.
- Disable Swagger UI `/docs` in the production environment.

#### 2. Hardened OpenAPI Specification (Public Listener Only)

```yaml
openapi: 3.1.0
info:
  title: Task Management Gateway (Hardened)
  version: 2.1.0
servers:
  - url: https://api.tinytask.eu
    description: Production Public API
paths:
  /v1/auth/login:
    post:
      summary: User authentication
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LoginRequest'
      responses:
        '200':
          description: Authentication tokens issued
        '429':
          description: Rate limit exceeded (Max 5 attempts/minute)
  /v1/projects:
    get:
      summary: List user projects
      security:
        - BearerJWT: []
      responses:
        '200':
          description: Success
  /v1/integrations/github/webhook:
    post:
      summary: Receive GitHub commit events
      security:
        - GitHubSignature256: []
      parameters:
        - in: header
          name: X-Hub-Signature-256
          required: true
          schema:
            type: string
          description: HMAC-SHA256 signature calculated over payload using shared webhook secret
      responses:
        '202':
          description: Event accepted for background processing
        '401':
          description: Invalid or missing cryptographic signature
components:
  securitySchemes:
    BearerJWT:
      type: http
      scheme: bearer
      bearerFormat: JWT
    GitHubSignature256:
      type: apiKey
      in: header
      name: X-Hub-Signature-256
```

### Remediation Ledger

| Route / Resource | Initial State | Finding / Hazard | Remediated State | Principle |
|---|---|---|---|---|
| `/v1/admin/cache/clear` | Public port 443 | DoS via cache thrashing | **Relocated** to internal port `:9090` (mTLS required) | `PRIN-MOD-03` |
| `/metrics` | Public port 443 | Infrastructure reconnaissance | **Relocated** to internal monitoring subnet | `PRIN-MOD-03` |
| `/docs` | Public port 443 | Schema harvesting | **Disabled** in production environment | `PRIN-MOD-03` |
| `/v1/integrations/github/webhook` | Unauthenticated | Spoofed events / DoS | **Enforced** HMAC SHA-256 validation + rate limiting | `PRIN-SEC-08` |
