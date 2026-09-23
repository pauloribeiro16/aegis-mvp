# Evaluation Checklist — Trust Boundary & Complete Mediation

Comprehensive verification checklist for evaluating architectural boundaries and mediation against `PRIN-MOD-01`, `PRIN-SEC-02`, and `PRIN-SEC-04`.

---

## 1. Boundary Demarcation & Authentication (`PRIN-MOD-01`)

- [ ] **Cryptographic Boundary Ingress:** Every transition from an untrusted or DMZ zone to an internal application zone enforces cryptographic authentication (mTLS or signed internal tokens).
- [ ] **No Unauthenticated Identity Headers:** Downstream microservices do not trust plaintext caller headers (e.g. `X-User-Id`, `X-Tenant-Id`) without cryptographic verification.
- [ ] **Explicit Boundary Schemas:** All data crossing a trust boundary is validated against strict schemas (Pydantic, JSON Schema, Protobuf) before execution.
- [ ] **Data Stores Isolated from Ingress:** Databases, caches, and object storage are unreachable from public client networks and reside in private subnets.

---

## 2. Complete Mediation (`PRIN-SEC-02`)

- [ ] **Localized Authorization:** Domain microservices verify that the authenticated caller has permission to access the requested resource (preventing IDOR).
- [ ] **Multi-Tenant Scoping:** Every database query, cache lookup, or document fetch includes the tenant identifier derived from the verified token claims.
- [ ] **Bounded Cache Validity:** Authorization decisions cached in memory or distributed caches have bounded TTLs ($\le 60$ seconds) or invalidate upon role change events.
- [ ] **No Perimeter-Only Trust:** Services behind the API gateway do not bypass authorization checks under the assumption that the gateway performed all checks.

---

## 3. Separation of Privilege (`PRIN-SEC-04`)

- [ ] **Distinct Service Identities:** Web API runtimes, background task workers, and administrative CLI tools use separate service accounts.
- [ ] **Scoped Database Users:** Application services connect to databases using roles restricted to necessary tables and operations (no database superusers in application configs).
- [ ] **Isolation of High-Risk Processing:** Workers processing untrusted files (e.g. image/PDF parsers, code execution) run in sandboxed containers with read-only root filesystems and minimal network egress.
