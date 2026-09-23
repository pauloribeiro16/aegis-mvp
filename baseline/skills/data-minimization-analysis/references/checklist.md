# Evaluation Checklist — Data Minimization & Privacy Balance

Comprehensive verification checklist for evaluating schemas and data flows against `PRIN-PRV-01` and `PRIN-PRV-03`.

---

## 1. Ingress Minimization (`PRIN-PRV-01`)

- [ ] **Strict Schema Validation:** API request schemas reject extra, unmodeled properties (`additionalProperties: false` or `extra = 'forbid'`).
- [ ] **No Mass Assignment:** Controllers never pass raw request bodies directly to database ORM models or database update queries.
- [ ] **Functional Justification:** Every input field collected across onboarding, settings, and forms maps directly to an active feature.
- [ ] **No Premature Collection:** Financial or physical address details are only requested during actual billing checkout, never during free tier sign-up.

---

## 2. Egress Exposure & DTO Scoping (`PRIN-PRV-01`)

- [ ] **Dedicated Output DTOs:** Every API endpoint returns an explicit DTO projection, never raw database entities.
- [ ] **Sensitive Field Absence:** Passwords, password hashes, biometric tokens, MFA secrets, and payment tokens are completely absent from all response models.
- [ ] **Internal Telemetry Exclusion:** System metadata (e.g. `failed_login_count`, internal database foreign keys, tenant encryption keys) is excluded from client responses.
- [ ] **Role-Based DTOs:** Public collaborator views display only display names and avatars; private account details are accessible only by the account owner.

---

## 3. Privacy-Preserving Balance & Coarsening (`PRIN-PRV-03`)

- [ ] **Location Coarsening:** Where location is required for language or localized pricing, only coarse country/region codes are retained; GPS coordinates are discarded.
- [ ] **Log Scrubbing:** Application logs, error trackers, and telemetry streams automatically scrub or hash IP addresses, email addresses, and bearer tokens.
- [ ] **Synthetic / Anonymous Identifiers:** Cross-service references use opaque UUIDs rather than email addresses or national identity numbers.
