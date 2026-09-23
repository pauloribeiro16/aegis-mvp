# Analytical Heuristics — Data Minimization & Privacy Balance

Detailed technical heuristics for inspecting request/response schemas, database columns, and telemetry payloads against `PRIN-PRV-01` and `PRIN-PRV-03`.

---

## 1. Ingress Minimization Heuristic (PRIN-PRV-01)

### Rule 1.1: Strict Ingress Schema & Mass Assignment Rejection
- Inbound API payloads must reject unexpected or unrecognized fields:
  1. Schemas must configure strict input validation (e.g. `extra = "forbid"` in Pydantic, or `additionalProperties: false` in JSON Schema).
  2. Prevent mass assignment: Never pass raw request dictionaries directly to ORM model instantiators (e.g. `User(**request.json)`).

### Rule 1.2: Purpose Justification Triage
- For every input field collected during user onboarding or feature workflows:
  1. If a field cannot be linked to a current functional feature, it must be removed.
  2. Optional profile attributes (e.g. phone numbers, social media links) must never be made mandatory.

---

## 2. Egress Minimization Heuristic (PRIN-PRV-01)

### Rule 2.1: Explicit Projection via Dedicated DTOs
- Microservices and web controllers must never return raw database entities:
  1. Define explicit output DTO classes for each consumer persona (e.g. `PublicViewDTO`, `OwnerViewDTO`, `AdminViewDTO`).
  2. Sensitive fields (`password_hash`, `mfa_secret`, `stripe_customer_id`, `ssn`, `internal_risk_score`) must be structurally absent from the public DTO definitions.

---

## 3. Privacy-Preserving Balance Heuristic (PRIN-PRV-03)

### Rule 3.1: Data Coarsening & Pseudonymization
- Where user attributes are needed for operational features, coarsen or pseudonymize the data at the ingestion boundary:
  1. **Geolocation:** If location is used for currency or language selection, store only the ISO 3166-1 alpha-2 country code (`"PT"`) or coarse city, discarding latitude and longitude coordinates.
  2. **Timestamps:** If full precision is unnecessary, truncate timestamps to date or hour.
  3. **IP Addresses in Logs:** Truncate IPv4 addresses by zeroing the last octet (`192.168.1.0/24`) or hash with a daily rotating salt prior to ingestion into analytics systems.
