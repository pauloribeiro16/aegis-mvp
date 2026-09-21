# D-06.1 — Relevant Ambiguity (NIS 2)

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
#### 3.2 NIS2-CL08 — Art. 21(1) sentence 2 — Risk-management factors
**Source locus:**
> Taking into account **<mark>the state-of-the-art and, where applicable, relevant European and international standards, as well as the cost of implementation</mark>**, the measures referred to in the first subparagraph shall ensure a level of security of network and information systems **appropriate to the risks posed**. When assessing the proportionality of those measures, due account shall be taken of **the degree of the entity's exposure to risks, the entity's size and the likelihood of occurrence of incidents and their severity, including their societal and economic impact**.
**Instance 1 — VAG — S3 — `state-of-the-art`**
- **R1:** `state-of-the-art` = current best practice (qualitative).
- **R2:** `state-of-the-art` = published standards (e.g. ISO/IEC 27001:2022, NIST CSF 2.0).
- **R3:** `state-of-the-art` = cutting-edge research (academic / frontier).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Best practice | In-Directive: `state-of-the-art and … standards` (R1 contrasts with R2) |
| R2 | Standards | In-Directive: same as R1 |
| R3 | Frontier | None in OJ |
R1 and R2 produce materially distinct obligations (R1 admits "industry-typical" measures; R2 mandates standards-based measures). R3 is rejected by recital 56 (cost-of-implementation consideration implies off-the-shelf). S3.
*Berry anchor:* §5.1 (`state-of-the-art`).
**Instance 2 — VAG — S2 — `cost of implementation`**
`cost` — to whom? The entity's cost? The national-economy cost? The supply-chain cost?
- **R1:** Entity's cost.
- **R2:** National-economy cost (recital 56).
- **R3:** Supply-chain cost (R3 imports the Art. 21(2)(d) supply-chain frame).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity's cost | In-Directive: literal `cost of implementation` (the implementation is the entity's) |
| R2 | National-economy cost | In-Directive: recital 56 |
| R3 | Supply-chain cost | None in OJ |
R1 is the literal reading. R2 is a non-operational reading (national-economy cost is not assessable by the entity). R3 is T3-imposed (no support in the OJ text). S2.
*Berry anchor:* §3.3.1 (`cost`).
**Instance 3 — VAG — S2 — `appropriate to the risks posed`**
`appropriate to the risks posed` — what is the proportionality function?
- **R1:** Linear (proportional to exposure × likelihood × impact).
- **R2:** Tiered (mapped to entity's classification under Art. 3).
- **R3:** Risk-tiered (mapped to specific risk-assessment output).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Linear | None in OJ |
| R2 | Tiered | None in OJ; Art. 3 essential/important classification |
| R3 | Risk-tiered | In-Directive: Art. 21(1) sentence 2 lists risk factors |
R3 is the dominant reading. S2.
*Berry anchor:* §5.1 (`appropriate to the risks`).
**Instance 4 — VAG — S2 — `the degree of the entity's exposure to risks`**
`exposure` — exposure to threat? Exposure to impact? Exposure to incident likelihood?
- **R1:** Threat exposure.
- **R2:** Impact exposure (downstream).
- **R3:** Combined.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Threat | None in OJ |
| R2 | Impact | None in OJ |
| R3 | Combined | None in OJ; Art. 6(9) `risk` (loss or disruption) |
*Berry anchor:* §3.3.1 (`exposure`).
**Instance 5 — VAG — S2 — `the entity's size`**
`size` — by employee count, by turnover, by balance sheet total, by user count? The Recommendation 2003/361/EC definition is the standard EU benchmark, but the Directive does not reference it.
- **R1:** Employee count.
- **R2:** Turnover.
- **R3:** Balance sheet total.
- **R4:** User count (a non-traditional measure for digital service providers).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Employees | In-Directive: Art. 3 cross-refs to Rec. 2003/361/EC (employee + turnover) |
| R2 | Turnover | In-Directive: same as R1 |
| R3 | Balance sheet | In-Directive: same as R1 |
| R4 | User count | None in OJ |
R1–R3 are the standard EU micro/small/medium/large measures. R4 is T3-imposable. S2.
*Berry anchor:* §3.3.1 (`size`).
**Instance 6 — VAG — S2 — `likelihood of occurrence of incidents and their severity`**
`likelihood` + `severity` (AND). The two-factor risk-treatment.
- `likelihood` — same POLY as in Art. 6(9) (frequentist / Bayesian / qualitative).
- `severity` — same VAG as `severe` in Art. 23(3) (defines `significant incident`).
| # | Reading (likelihood) | Disambiguation source |
|---|---|---|
| R1 | Frequentist | None in OJ |
| R2 | Bayesian | None in OJ |
| R3 | Qualitative | None in OJ |
| # | Reading (severity) | Disambiguation source |
|---|---|---|
| R1 | Operational impact only | In-Directive: Art. 23(3)(a) `severe operational disruption` |
| R2 | Financial only | In-Directive: Art. 23(3)(a) `financial loss` |
| R3 | Societal + economic | In-Directive: literal `societal and economic impact` |
| R4 | Any | None in OJ; recital 56 |
R3 and R4 are operative. S2.
*Berry anchor:* §3.3.1 (`severity`).
**Instance 7 — VAG — S2 — `societal and economic impact`**
`societal` — collective harm to public welfare; `economic` — financial harm to markets or to the entity.
- **R1:** `societal` and `economic` are independent impact dimensions (entity must consider both).
- **R2:** `societal and economic` is a compound describing the type of impact.
- **R3:** `societal` = public-impact, `economic` = private-impact, and the AND binds them.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent dimensions | In-Directive: literal `societal and economic` |
| R2 | Compound description | None in OJ |
| R3 | Public + private | None in OJ; recital 56 |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
---
#### 3.7 NIS2-CL13 — Art. 21(2)(d) — Supply chain security (S3)
**Source locus:**
> **(d)** supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers;
**Instance 1 — VAG — S2 — `supply chain security`**
- **R1:** Securing the supply chain (each tier).
- **R2:** Securing the entity's relationship with suppliers (contractual, due-diligence).
- **R3:** Securing the products/services procured (product-security focus).
- **R4:** All three (cumulative).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Chain-focus | None in OJ |
| R2 | Relationship-focus | In-Directive: `relationships between each entity and its direct suppliers` |
| R3 | Product-focus | In-Directive: Art. 21(3) `quality of products` |
| R4 | All three | None in OJ |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`supply chain security`).
**Instance 2 — VAG — S2 — `security-related aspects`**
`security-related` is a soft qualifier. The reading:
- **R1:** Cybersecurity aspects only.
- **R2:** Information-security aspects (broader, includes non-cyber: physical, personnel).
- **R3:** Any aspect of the supplier relationship that has security implications.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cybersecurity only | None in OJ |
| R2 | Info-security | None in OJ |
| R3 | Any security implication | In-Directive: `security-related` (adjective) |
R3 is the literal reading. S2.
*Berry anchor:* §5.1 (`security-related`).
**Instance 3 — SCOPE-Q — S3 — `direct`**
**`direct suppliers or service providers`** — `direct` is the critical scope-limiter (T3 NIS2-C08, S3).
- **R1:** `direct` = contractually bound (Tier-1).
- **R2:** `direct` = technically integrated (API-connected, shared infrastructure).
- **R3:** `direct` = operationally dependent (single-point-of-failure).
- **R4:** `direct` = at least one of the above.
- **R5:** `direct` = all of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Contractual | None in OJ |
| R2 | Technical | None in OJ |
| R3 | Operational | None in OJ |
| R4 | Any | None in OJ; recital 56 |
| R5 | All | None in OJ |
R1 is the dominant reading in Member-State transposition practice. R2 and R3 are operationally distinct (R1 admits paper-based due diligence; R2 requires technical integration assessment; R3 requires SPOF analysis). S3.
This is the **single most consequential scope-limiting term in Chapter IV**. The reading determines whether the obligation reaches 1-hop, n-hop, or only contractual counter-parties. The Directive is silent; the Commission's 17 October 2024 implementing acts (Art. 21(5)) were originally expected to clarify this but as of mid-2025 are not yet published.
*Berry anchor:* §5.1 (`direct`); §5.2.1 (scope).
**Instance 4 — POLY — S2 — `suppliers or service providers`**
Hendiadys or distinct categories?
- **R1:** Hendiadys (one combined concept: "supplier-service-providers").
- **R2:** Distinct (suppliers provide goods; service providers provide services).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hendiadys | None in OJ |
| R2 | Distinct | In-Directive: literal `suppliers OR service providers` (OR) |
R2 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`suppliers`/`service providers`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->

