# D-03.1 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.1 NIS2-CL07 — Art. 21(1) sentence 1 — Risk-management core obligation
**Source locus:**
> Member States shall ensure that essential and important entities take **<mark>appropriate and proportionate technical, operational and organisational measures</mark>** to manage the risks posed to the security of network and information systems which those entities use for their operations or for the provision of their services, and to prevent or minimise the **impact** of incidents on recipients of their services and on other services.
**Instance 1 — VAG — S3 — `appropriate and proportionate`**
The opening qualifier. Three materially distinct readings:
- **R1:** `appropriate` and `proportionate` are independent (entity must satisfy both tests, separately).
- **R2:** `appropriate` modifies `proportionate` (entity must satisfy proportionality, with `appropriate` as a placeholder synonym).
- **R3:** `appropriate and proportionate` is a single compound qualifier (a fixed phrase).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent | None in OJ |
| R2 | Hierarchical | None in OJ |
| R3 | Compound | In-Directive: Art. 21(1) sentence 2 operationalises proportionality by specific factors (exposure, size, likelihood, severity) |
R1 and R3 produce materially distinct compliance obligations (R1 admits two separate failure modes; R3 admits one composite test). S3.
This is the dominant VAG trigger of NIS 2. **It propagates to all 10 sub-points of Art. 21(2)(a)–(j) and to Art. 21(3) and Art. 21(4).** Every measure listed in Art. 21(2) inherits the `appropriate and proportionate` qualifier by reference to "The measures referred to in paragraph 1".
*Berry anchor:* §5.1 (`appropriate`, `proportionate`).
**Instance 2 — POLY — S2 — `technical, operational and organisational measures`**
Three-term coordination. Three readings:
- **R1:** Three distinct categories of measures (entity must implement at least one of each).
- **R2:** Cumulative description (a measure is "technical, operational and organisational" if it has all three characteristics).
- **R3:** Open list (entity may add more categories).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct categories | In-Directive: literal `technical, operational and organisational` |
| R2 | Cumulative single measure | None in OJ |
| R3 | Open list | In-Directive: recital 56 (proportionality) |
R1 is the literal reading. R3 is the dominant reading (recital 56 implies entity-discretion on additional categories). S2.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 3 — VAG + POLY — S2 — `manage the risks`**
`manage the risks` — what counts as `management`? Reading:
- **R1:** Identify + assess + mitigate.
- **R2:** Treat (avoid, accept, transfer, mitigate).
- **R3:** Continuous monitoring + adjustment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Identify-assess-mitigate | None in OJ; ISO/IEC 27005 |
| R2 | ISO 27005 risk-treatment | None in OJ; ISO/IEC 27005 |
| R3 | Continuous monitoring | None in OJ; NIST RMF |
*Berry anchor:* §3.3.1 (`manage`).
**Instance 4 — POLY — S2 — `impact`**
`impact` — on recipients of services (downstream effect) or on other services (cascading effect)?
- **R1:** Impact on direct recipients.
- **R2:** Impact on other services (cascade).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Recipients | In-Directive: literal `recipients of their services` |
| R2 | Other services | In-Directive: literal `on other services` |
| R3 | Both | In-Directive: literal `recipients … and … other services` |
R3 is the literal reading (coordinated by `and`). The fact that the two objects are coordinated by AND rather than OR means the entity must consider impact on both. S2 because the surface ambiguity is between "focus on direct recipients" and "consider cascading effects".
*Berry anchor:* §3.3.1 (`impact`); §5.4.7 (AND).
---
#### 3.12 NIS2-CL18 — Art. 21(2)(i) — HR security + access control + asset management
**Source locus:**
> **(i)** human resources security, access control policies and asset management;
**Instance 1 — POLY — S2 — `human resources security`**
- **R1:** Staff-security (vetting, training).
- **R2:** HR-driven-security (policies owned by HR department).
- **R3:** Workforce-security (insider-threat).
- **R4:** Lifecycle-security (joiners, movers, leavers).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Staff | None in OJ |
| R2 | HR-driven | None in OJ |
| R3 | Workforce | None in OJ |
| R4 | Lifecycle | None in OJ; ISO 27001 A.6 |
R1, R3, R4 are operative. S2.
*Berry anchor:* §3.3.1 (`human resources security`).
**Instance 2 — POLY — S2 — `access control policies`**
- **R1:** RBAC (role-based).
- **R2:** ABAC (attribute-based).
- **R3:** MAC (mandatory).
- **R4:** DAC (discretionary).
- **R5:** Any (model-agnostic).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | RBAC | None in OJ; ISO 27001 A.5.15 |
| R2 | ABAC | None in OJ; NIST 800-162 |
| R3 | MAC | None in OJ |
| R4 | DAC | None in OJ |
| R5 | Any | In-Directive: literal `policies` is model-agnostic |
R5 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`access control`).
**Instance 3 — POLY — S2 — `asset management`**
- **R1:** Hardware asset management (devices).
- **R2:** Software asset management (licences, versions).
- **R3:** Information asset management (data).
- **R4:** All three.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hardware | None in OJ |
| R2 | Software | None in OJ |
| R3 | Information | None in OJ; ISO 27001 A.5.9 |
| R4 | All | None in OJ; recital 56 |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`asset management`).
**Instance 4 — COORD — S3 — `human resources security, access control policies and asset management`**
Three distinct security domains coordinated by AND in a single sub-point. Each domain is independently a discipline (ISO 27001 A.6, A.5.15, A.5.9 respectively). The clause does not signal whether partial compliance (2 of 3) satisfies the obligation.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All three required (cumulative) | In-Directive: literal |
| R2 | At least one required (pick one) | None in OJ |
| R3 | A subset (e.g. two) required | None in OJ |
R1 is the literal reading. R2 and R3 produce materially distinct compliance obligations (R2 admits single-domain satisfaction). S3.
*Berry anchor:* §5.5 (three-way coordination).
**Layer 1 observation — T3-vs-text gap (T3 NIS2-C20).** T3 reads this clause as `role-based access, need-to-know principle, least privilege enforcement`. **The OJ text contains none of these phrases** — it mentions only `access control policies`. The role-based / need-to-know / least-privilege unpacking is imported from ISO 27001 A.5.15 interpretation.
---

<!-- aegis:purity: own_reg=NIS2; demoted=0; core_cross_mentions=0 -->

