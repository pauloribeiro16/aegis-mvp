# D-04.1 — Relevant Ambiguity (NIS 2)

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
#### 3.3 NIS2-CL09 — Art. 21(2) chapeau — All-hazards approach + physical environment
**Source locus:**
> The measures referred to in paragraph 1 shall be **based on an all-hazards approach** that aims to protect network and information systems and **<mark>the physical environment of those systems</mark>** from incidents…
**Instance 1 — VAG — S2 — `all-hazards approach`**
`all-hazards` — natural, technological, malicious, accidental? Cybersecurity only or broader?
- **R1:** All cybersecurity hazards (intentional, accidental, environmental).
- **R2:** All hazards including natural disasters (earthquake, flood), pandemics.
- **R3:** All hazards including physical security (intrusion, theft, sabotage).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cybersecurity-only | None in OJ |
| R2 | Including natural | None in OJ |
| R3 | Including physical | In-Directive: literal `physical environment of those systems` |
R3 is the dominant reading (the chapeau explicitly includes physical-environment protection). S2.
*Berry anchor:* §5.1 (`all-hazards`).
**Instance 2 — VAG + SCOPE-Q — S2 — `the physical environment of those systems`**
The physical environment is in scope. The reading:
- **R1:** Server rooms, data centres, network equipment closets.
- **R2:** Buildings (offices, call centres).
- **R3:** Surrounding critical infrastructure (power, cooling, telecoms).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Data-centre scope | In-Directive: literal `physical environment` |
| R2 | Building scope | None in OJ |
| R3 | Critical-infrastructure scope | None in OJ |
R1 is the literal reading. R2 and R3 are operational extensions. S2.
*Berry anchor:* §5.1 (`physical environment`); §5.2.1 (scope).
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

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

**Layer 1 observation** — The physical-environment scope of NIS 2 is broader than DORA, CRA, AI Act (all of which are software/cyber-focused). The all-hazards approach with physical-environment coverage is the **single most distinctive feature of NIS 2 vs the other four regulations** in the corpus. **For software-compliance analysis, the physical-environment dimension is out-of-scope**: it does not generate software requirements, only physical-security requirements. The clause is included for completeness but flagged as **out-of-scope for the software-compliance track of the methodology**. Layer 3 (inference-trust) will need to adjudicate whether software-software integration controls are needed for the physical-environment dimension (e.g. environmental sensors feeding into SIEM).

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->

