---
name: attack-surface-analysis
description: Inspects system interfaces, network listener configurations, OpenAPI contracts, and auxiliary endpoints to minimize exposed entry points and enforce uniform security intensity.
---

# Attack Surface & Peripheral Resilience Analysis

Analyzes system interfaces, network listeners, API route catalogs, and auxiliary ingress points to minimize public exposure and ensure peripheral components match core security standards.

> **Target Principle:**  
> - `PRIN-ENG-02` (Attack Surface Minimization & Peripheral Resilience — Howard & LeBlanc / Schneier)

---

## 1. Operational Mandate & Scope

The agent acts as an Application Security Architect reviewing design and deployment artifacts:
- **API Contracts:** OpenAPI / Swagger specifications, gRPC protobuf definitions, GraphQL schemas.
- **Network & Deployment Specs:** `docker-compose.yml`, Kubernetes Ingress/Service manifests, Terraform/CloudFormation security groups.
- **Auxiliary Ingress:** Third-party webhooks, event callback handlers, administrative portals, health/metrics endpoints.

The goal is to eliminate unnecessary exposure, isolate auxiliary interfaces to internal planes, and verify that all remaining entry points enforce uniform authentication, rate limiting, and integrity protection.

---

## 2. Evaluation Procedure

1. **Inventory Collection:** Extract all exposed ports, network protocols, URL paths, and HTTP methods from the target artifact.
2. **Business Necessity Triage:** For each exposed path or port, determine if direct public access is strictly required by an end-user or authorized external client.
3. **Auxiliary & Administrative Segregation:** Identify diagnostic endpoints (`/metrics`, `/health`, `/actuator`, `/debug/pprof`), documentation UIs (`/docs`, `/swagger-ui`), and administrative tooling. Confirm they are either disabled in production or bound exclusively to internal management interfaces.
4. **Weakest-Link Ingress Verification:** Inspect external callback listeners (webhooks, asynchronous notifications). Verify that authentication and rate limiting are not relaxed compared to primary APIs.
5. **Report Generation:** Output findings using the standardized Attack Surface Reduction Ledger.

---

## 3. Concrete Walkthrough Example

### 3.1 Input Artifact: Vulnerable OpenAPI 3.1 Specification

```yaml
openapi: 3.1.0
info:
  title: TaskFlow Notification & Ingestion Service
  version: 1.0.0
paths:
  /api/v1/tasks:
    get:
      summary: List user tasks
      security:
        - BearerAuth: []
      responses:
        '200':
          description: OK
  /api/v1/webhooks/stripe:
    post:
      summary: Stripe billing event callback
      description: Receives asynchronous billing notifications
      # SMELL: No security requirement or signature header specified
      responses:
        '200':
          description: Event received
  /metrics:
    get:
      summary: Prometheus performance metrics
      # SMELL: Diagnostic endpoint exposed alongside public routes without auth
      responses:
        '200':
          description: Metrics text
  /debug/pprof/goroutine:
    get:
      summary: Go runtime diagnostic profiling
      # SMELL: Debug profiler active in production API
      responses:
        '200':
          description: Goroutine dump
```

### 3.2 Analytical Evaluation

1. **Violation of `PRIN-MOD-03` (Attack Surface Minimization):**
   - `/metrics` and `/debug/pprof/goroutine` are published on the public API gateway listener. Internal operational telemetry and runtime debuggers expose memory layouts, internal IP addresses, and routine counts, aiding attacker reconnaissance.
   - **Remediation:** Remove `/debug/pprof/*` entirely from the production route table. Move `/metrics` to an internal monitoring listener bound exclusively to the private container network (e.g. port `9090` accessible only by the scraper).
2. **Violation of `PRIN-SEC-08` (Weakest Link Resilience):**
   - `/api/v1/webhooks/stripe` lacks an explicit security scheme. While core `/api/v1/tasks` requires `BearerAuth`, the webhook route allows unauthenticated POSTs, exposing the service to forged billing state changes and unbounded resource exhaustion.
   - **Remediation:** Enforce HMAC SHA-256 signature verification via the `Stripe-Signature` header, require timestamp freshness verification (tolerance $\le$ 300s), and apply dedicated ingress rate limiting.

### 3.3 Remediated OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: TaskFlow Notification & Ingestion Service (Hardened)
  version: 1.0.0
servers:
  - url: https://api.taskflow.com
    description: Public Application Ingress
paths:
  /api/v1/tasks:
    get:
      summary: List user tasks
      security:
        - BearerAuth: []
      responses:
        '200':
          description: OK
  /api/v1/webhooks/stripe:
    post:
      summary: Stripe billing event callback
      security:
        - StripeWebhookSignature: []
      parameters:
        - in: header
          name: Stripe-Signature
          required: true
          schema:
            type: string
          description: HMAC-SHA256 signature generated by Stripe using shared secret
      responses:
        '200':
          description: Event verified and queued
        '400':
          description: Missing or invalid signature / stale timestamp
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
    StripeWebhookSignature:
      type: apiKey
      in: header
      name: Stripe-Signature
```

### 3.4 Attack Surface Reduction Ledger

| Interface / Route | Original State | Evaluated Risk | Remediated State | Principle |
|---|---|---|---|---|
| `/debug/pprof/*` | Public route | Runtime profiling & memory reconnaissance | **Removed** from production router | `PRIN-MOD-03` |
| `/metrics` | Public port 443 | Infrastructure enumeration & metrics harvesting | **Relocated** to internal listener `:9090` | `PRIN-MOD-03` |
| `/api/v1/webhooks/stripe` | Unauthenticated POST | Forged billing state changes, denial-of-service | **Hardened**: Mandatory HMAC signature check + replay cache | `PRIN-SEC-08` |

---

## 4. Reference Catalogs

- **Detailed Heuristics:** Consult [`references/heuristics.md`](references/heuristics.md) for in-depth rules on route pruning, listener segregation, and webhook validation algorithms.
- **Concrete Anti-Patterns:** Consult [`references/antipatterns.md`](references/antipatterns.md) for real-world configuration smells across Docker, cloud firewalls, and application frameworks.
- **Realistic Case Studies:** Consult [`references/examples.md`](references/examples.md) for multi-tier microservice and infrastructure hardening examples.
- **Audit Checklist:** Consult [`references/checklist.md`](references/checklist.md) for the structured evaluation checklist.
