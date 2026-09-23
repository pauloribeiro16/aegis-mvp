# Anti-Patterns & Smells — Requirements Verifiability & Atomicity

Common requirement drafting anti-patterns that create compliance risk, untestable code, and communication breakdowns between security and engineering.

---

## 1. Compound Run-On Requirements

### Bad Pattern: Multi-Concern Monolithic Statement

> "The system must encrypt customer data in transit and at rest, support customer-managed encryption keys, rotate keys regularly, and alert the security team whenever an unauthorized access attempt occurs."

**Why It Fails:**  
- Bundles four distinct subsystems: TLS configuration, database at-rest encryption, KMS key management/rotation, and SIEM security alerting.
- Cannot be assigned to a single sprint, team, or automated test case. If TLS passes but key rotation is missing, the requirement status is ambiguous.

**Remediated Decomposition:**
1. `REQ-SEC-CRYP-001`: In-transit TLS 1.3 requirement.
2. `REQ-SEC-CRYP-002`: AES-256-GCM at-rest database storage requirement.
3. `REQ-SEC-CRYP-003`: Automated 90-day KMS key rotation requirement.
4. `REQ-SEC-ALRT-001`: Real-time SIEM alert generation on 401/403 thresholds.

---

## 2. Untestable Modal Verbs and Wishful Thinking

### Bad Pattern: Non-Binding & Unfalsifiable Language

> "The API should strive to prevent SQL injection vulnerabilities and should ideally sanitize all incoming inputs as best as possible."

**Why It Fails:**  
- "Should strive" and "ideally" provide zero engineering constraint.
- "As best as possible" gives no objective benchmark for automated security testing.

**Remediated Pattern:**
> "The API database access layer SHALL execute all SQL queries using parameterized prepared statements or an ORM that enforces type-checked bind variables, strictly prohibiting string concatenation or interpolation of untrusted input."  
> *Verification Method: [Static Analysis / SAST semgrep rule checking for SQL query string interpolation]*

---

## 3. Negative Unbounded Requirements

### Bad Pattern: Proving a Universal Negative

> "The system must never allow any unauthorized data leaks or security breaches."

**Why It Fails:**  
- Impossible to verify or falsify. No automated test or audit can prove the absolute absence of all future vulnerabilities.

**Remediated Pattern:**
> "When an HTTP request targets a tenant-scoped endpoint, the API Gateway SHALL verify that the tenant identifier in the JWT claims matches the resource tenant ID, rejecting mismatches with HTTP 403 Forbidden before reaching domain business logic."  
> *Verification Method: [Automated BDD Security Integration Test]*
