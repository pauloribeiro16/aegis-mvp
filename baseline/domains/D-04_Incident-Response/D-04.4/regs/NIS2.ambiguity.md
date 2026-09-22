# D-04.4 — Relevant Ambiguity (NIS 2)

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
#### 3.5 NIS2-CL11 — Art. 21(2)(b) — Incident handling
**Source locus:**
> **(b)** incident handling;
**Instance 1 — POLY — S2 — `incident handling`**
The phrase is defined in Art. 6(8): `any actions and procedures aiming to prevent, detect, analyse, and contain or to respond to and recover from an incident`. The 6-action list is illustrative (`aiming to`).
- **R1:** The 6-action list is exhaustive.
- **R2:** The 6-action list is a floor; entity must add more actions.
- **R3:** `incident handling` is process-only (NIST SP 800-61 model).
- **R4:** `incident handling` is team-only (CSIRT/SOC personnel).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Exhaustive | None in OJ |
| R2 | Floor | In-Directive: `aiming to` (illustrative) |
| R3 | Process | None in OJ; NIST SP 800-61 |
| R4 | Team | None in OJ; ENISA CSIRT-services guidance |
R2 is the literal reading. R3 vs R4 is a Layer 1 polysemy. S2.
*Berry anchor:* §3.3.1 (`incident handling`); §5.1 (`aiming to`).
---
#### 3.6 NIS2-CL12 — Art. 21(2)(c) — Business continuity, backup, disaster recovery, crisis management
**Source locus:**
> **(c)** business continuity, such as backup management and disaster recovery, and crisis management;
**Instance 1 — VAG + POLY — S2 — `business continuity`**
- **R1:** Service continuity (operational).
- **R2:** Data continuity (backup-restoration).
- **R3:** Organisational continuity (going-concern).
- **R4:** All three (cumulative).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Service | None in OJ |
| R2 | Data | None in OJ |
| R3 | Organisational | None in OJ |
| R4 | Cumulative | In-Directive: `such as backup management and disaster recovery` (R2 implied) + `crisis management` (R3 implied) |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`business continuity`).
**Instance 2 — COORD — S3 — `business continuity, such as backup management and disaster recovery, and crisis management`**
The structure is `BC, such as [examples], and CM`. The `such as` opens an illustrative list (Berry §5.1 `include` pattern) inside an AND of `business continuity` and `crisis management`. The nesting admits ≥3 parse trees:
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | BC + (examples) + CM, all required | In-Directive: literal reading |
| R2 | BC + (examples) are illustrative, CM is independent | None in OJ |
| R3 | BC and CM are the two required; examples are floor | None in OJ |
R1 and R3 produce materially distinct compliance obligations (R1 mandates all three; R3 admits partial compliance). S3.
*Berry anchor:* §5.1 (`such as`); §5.5 (nested coordination).
**Instance 3 — POLY — S2 — `crisis management`**
- **R1:** Strategic crisis management (executive-level coordination, communication).
- **R2:** Tactical crisis management (operational, technical).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strategic | None in OJ; ISO 22361 |
| R2 | Tactical | None in OJ; ISO 22361 |
| R3 | Both | None in OJ; recital 56 |
*Berry anchor:* §3.3.1 (`crisis management`).
**Instance 4 — POLY — S2 — `backup management`**
- **R1:** `backup management` = backup policy.
- **R2:** `backup management` = backup operations (tape rotation, offsite storage).
- **R3:** `backup management` = backup recovery testing.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Policy | None in OJ |
| R2 | Operations | None in OJ; ISO 22301 |
| R3 | Recovery testing | None in OJ; ISO 22301 |
*Berry anchor:* §3.3.1 (`backup management`).
**Instance 5 — POLY — S2 — `disaster recovery`**
- **R1:** `disaster recovery` = IT-DR (technical recovery of systems).
- **R2:** `disaster recovery` = site recovery (physical site restoration).
- **R3:** `disaster recovery` = both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | IT | None in OJ; ISO 24762 |
| R2 | Site | None in OJ; ISO 24762 |
| R3 | Both | None in OJ |
*Berry anchor:* §3.3.1 (`disaster recovery`).
---
#### 3.11 NIS2-CL36 — Art. 23(4)(b) — Incident notification 72h
**Source locus:**
> **(b)** **<mark>without undue delay and in any event within 72 hours of becoming aware of the significant incident</mark>**, an incident notification, which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise;
**Instance 1 — VAG + COORD — S3 — twin-trigger at 72h**
Same pattern as CL35 at 72h. S3.
*Berry anchor:* §5.1 (`undue`); §5.7 (temporal operator); §5.4.7 (temporal AND).
**Instance 2 — SCOPE-Q + POLY — S3 — `becoming aware`**
Same awareness trigger as CL35. S3.
**Instance 3 — VAG — S2 — `indicators of compromise`**
IoC — defined in cybersecurity vocabulary; the Directive does not import a definition.
- **R1:** IoC = technical indicator (IP, hash, domain).
- **R2:** IoC = behavioural indicator (TTP).
- **R3:** Any indicator.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | None in OJ; MITRE ATT&CK |
| R2 | Behavioural | None in OJ; MITRE ATT&CK |
| R3 | Any | In-Directive: literal `indicators` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`indicators of compromise`).
**Instance 4 — VAG — S2 — `where available`**
Soft hedge on the IoC inclusion. The IoC is included only if the entity has it.
*Berry anchor:* §5.1 (`where available`).
---
#### 3.13 NIS2-CL38 — Art. 23(4)(d) — Final report 1m
**Source locus:**
> **(d)** a final report **not later than one month** after the submission of the incident notification under point (b), including the following:
> (i) a detailed description of the incident, including its severity and impact;
> (ii) the type of threat or root cause that is likely to have triggered the incident;
> (iii) applied and ongoing mitigation measures;
> (iv) where applicable, the cross-border impact of the incident;
**Instance 1 — VAG — S2 — `one month`**
- **R1:** Calendar month (1st to last day).
- **R2:** 30 days.
- **R3:** Working month (~22 working days).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Calendar | In-Directive: literal `one month` |
| R2 | 30 days | None in OJ |
| R3 | Working | None in OJ |
R1 is the literal reading. S2 (lower severity than CL35/CL36 because the hard anchor reduces temporal ambiguity).
*Berry anchor:* §5.7 (temporal operator).
**Instance 2 — VAG — S2 — `detailed description`**
- **R1:** `detailed` = comprehensive (full technical narrative).
- **R2:** `detailed` = sufficient for the CSIRT to act.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Comprehensive | None in OJ |
| R2 | Sufficient | None in OJ |
*Berry anchor:* §5.1 (`detailed`).
**Instance 3 — POLY — S2 — `root cause`**
`root cause` — same POLY as T3 NIS2-C27.
- **R1:** Technical root cause.
- **R2:** Organisational root cause.
- **R3:** Procedural root cause.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical | None in OJ; ISO/IEC 27001 |
| R2 | Organisational | None in OJ |
| R3 | Procedural | None in OJ |
*Berry anchor:* §3.3.1 (`root cause`).
**Instance 4 — COORD — S2 — `applied AND ongoing`**
The cumulative-vs-temporal reading.
- **R1:** Cumulative (both applied-so-far and ongoing-from-now must be reported).
- **R2:** Temporal (applied-so-far, ongoing-from-now).
- **R3:** Single composite.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cumulative | In-Directive: literal `applied and ongoing` |
| R2 | Temporal | None in OJ |
| R3 | Composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND); §5.5 (parallelism).
---
#### 3.14 NIS2-CL39 — Art. 23(4)(e) — Ongoing incident
**Source locus:**
> **(e)** in the event of an ongoing incident at the time of the submission of the final report referred to in point (d), Member States shall ensure that entities concerned provide a **progress report at that time** and a **final report within one month of their handling of the incident**.
**Instance 1 — VAG — S2 — `ongoing incident`**
`ongoing` — at the time of the 1-month final report submission, the incident is still in progress.
- **R1:** `ongoing` = still under containment.
- **R2:** `ongoing` = recovery phase.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Containment | None in OJ |
| R2 | Recovery | None in OJ |
| R3 | Either | In-Directive: literal `ongoing` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`ongoing`).
**Instance 2 — VAG — S2 — `within one month of their handling of the incident`**
The 1-month clock restarts on `handling of the incident`. `handling` — POLY per Art. 6(8) (process/team/capability).
*Berry anchor:* §3.3.1 (`handling`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

`one month` — calendar month or 30 days? Same Berry temporal question as GDPR Art. 33(4).

### from regs/NIS2.ambiguity.md

`detailed` — undefined. Same Berry VAG as GDPR Art. 33(4) `detailed`.

<!-- aegis:purity: own_reg=NIS2; demoted=2; core_cross_mentions=0 -->