# D-01.2 — Relevant Ambiguity (NIS 2)

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
#### 3.13 NIS2-CL19 — Art. 21(2)(j) — MFA + secured comms + secured emergency comms
**Source locus:**
> **(j)** the use of multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems within the entity, **where appropriate**.
**Instance 1 — VAG — S3 — `where appropriate`**
`where appropriate` closes the entire sub-point, softening all four coordinated obligations (per T3 NIS2-C21). Three readings:
- **R1:** `appropriate` = appropriate to the system.
- **R2:** `appropriate` = appropriate to the user.
- **R3:** `appropriate` = appropriate to the risk.
- **R4:** `appropriate` = appropriate to cost.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | System | None in OJ |
| R2 | User | None in OJ |
| R3 | Risk | In-Directive: Art. 21(1) factors |
| R4 | Cost | In-Directive: Art. 21(1) cost-of-implementation |
R3 is the dominant reading. S3.
*Berry anchor:* §5.1 (`where appropriate`).
**Instance 2 — POLY — S2 — `multi-factor authentication`**
- **R1:** SMS-OTP.
- **R2:** TOTP (authenticator apps).
- **R3:** Hardware token (FIDO2 / YubiKey).
- **R4:** Platform-authenticated (passkeys, device biometrics).
- **R5:** Any.
| # | Reading | Disambiguation source |
|---|---|---|
| R1-R4 | Various MFA mechanisms | None in OJ |
| R5 | Any | In-Directive: literal `multi-factor authentication` is mechanism-agnostic |
R5 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`multi-factor authentication`).
**Instance 3 — COORD — S3 — Four distinct obligations coordinated via OR and AND**
The sub-point contains: `MFA OR continuous authentication` (OR) + `secured voice, video AND text communications` (AND of three comms modalities) + `AND secured emergency communication systems` (AND of a fourth). Berry §5.4.7: the parse tree admits ≥6 distinct obligation shapes.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | MFA + (voice + video + text) + emergency comms | In-Directive: literal |
| R2 | (MFA or continuous) + (voice + video + text) + emergency comms | None in OJ |
| R3 | (MFA or continuous) + (any of voice/video/text) + emergency comms | None in OJ |
| R4 | (MFA or continuous) + (voice + video + text) — emergency comms optional | None in OJ |
| R5 | MFA only (encryption of comms and emergency is optional) | None in OJ |
| R6 | At least one of the four | None in OJ |
R1 is the literal reading. The other readings admit partial compliance. R1 and R5 produce materially distinct compliance populations. S3.
*Berry anchor:* §5.4.7 (multiple coordinations).
**Instance 4 — POLY — S2 — `secured`**
`secured` voice/video/text/emergency — encrypted? Authenticated? Access-controlled? Signed?
- **R1:** `secured` = encrypted.
- **R2:** `secured` = authenticated.
- **R3:** `secured` = access-controlled.
- **R4:** `secured` = all of the above.
- **R5:** `secured` = at least one.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Encrypted | None in OJ; Art. 21(2)(h) cryptography context |
| R2 | Authenticated | None in OJ |
| R3 | Access-controlled | None in OJ |
| R4 | All | None in OJ |
| R5 | Any | In-Directive: literal `secured` is mechanism-agnostic |
R5 is the literal reading. R1 is the dominant industry reading. S2.
*Berry anchor:* §3.3.1 (`secured`).
**Layer 1 observation — T3-vs-text gap (T3 NIS2-C22).** T3 reads this clause as `Audit Logging & Traceability`. **The OJ Art. 21(2)(j) text does not mention logging, audit trails, or traceability.** The logging attribution appears to come from a parallel reading of Art. 21(2)(b) (`incident handling` requires logs). T3-vs-text gap.
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same POLY as GDPR and CRA:

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->