# Analytical Heuristics — Trust Boundary & Complete Mediation

Detailed technical heuristics for inspecting architectural data flows, service boundaries, and internal communication paths against `PRIN-MOD-01`, `PRIN-SEC-02`, and `PRIN-SEC-04`.

---

## 1. Boundary Demarcation Heuristic (PRIN-MOD-01)

### Rule 1.1: Cryptographic Authentication at Every Perimeter Crossing
- Whenever a request transitions from a lower-trust zone to a higher-trust zone (e.g. Zone 0 to Zone 1, or Zone 1 to Zone 2):
  1. The receiving service must authenticate the sender using a cryptographic mechanism (e.g. Mutual TLS with SPIFFE/x509 identities, or signed asymmetric JWTs).
  2. Plaintext or unsigned headers (e.g. `X-Authenticated-User`, `X-User-Role`) passed over an unauthenticated network are considered zero-trust violations.
  3. Boundary crossings must reject unauthenticated requests before allocating heavy compute or database connections.

### Rule 1.2: Boundary Input Validation & Canonicalization
- Boundary crossing handlers must enforce strict schema validation:
  1. Input payloads must be strictly typed and validated against an explicit schema (e.g. JSON Schema, Protobuf, Zod/Pydantic).
  2. String fields must be canonicalized (e.g. UTF-8 normalization, path canonicalization) at the boundary before passing to downstream logic to prevent path traversal or injection.

---

## 2. Complete Mediation Heuristic (PRIN-SEC-02)

### Rule 2.1: Localized Authorization Enforcement
- Authorization checks must not occur solely at the network edge or API gateway:
  1. **Defense-in-Depth:** While the API Gateway validates user session validity (authentication), the domain microservice must validate resource-level access (authorization).
  2. **Multi-Tenant Scoping:** Every database query, cache lookup, or document fetch must include the tenant identifier extracted from the cryptographically verified token claims, e.g.:
     $$\text{Query: } \mathtt{SELECT} \dots \mathtt{WHERE\ id} = :id \ \mathbf{AND} \ \mathtt{tenant\_id} = :claims.tenant\_id$$
  3. Cached authorization decisions must have bounded TTLs ($\le 60$ seconds) or event-driven invalidation to prevent stale authorization bypasses.

---

## 3. Separation of Privilege Heuristic (PRIN-SEC-04)

### Rule 3.1: Segmented Identities for Distinct Operational Roles
- Shared service accounts spanning multiple functional tiers are prohibited:
  1. Application runtime services, asynchronous background workers, and administrative migration scripts must use distinct database users with separate credentials.
  2. Workers consuming background queues must not possess permissions to modify billing configurations or alter security policies.
  3. Database roles for web services must not possess `DROP TABLE`, `ALTER TABLE`, or administrative database privileges.
