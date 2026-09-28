# D-10.3 — Relevant Ambiguity (NIS 2)

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
#### 3.9 NIS2-CL15 — Art. 21(2)(f) — Effectiveness assessment
**Source locus:**
> **(f)** policies and procedures to assess the effectiveness of cybersecurity risk-management measures;
**Instance 1 — VAG — S2 — `effectiveness`**
- **R1:** `effectiveness` = control-effectiveness (does the control work as designed).
- **R2:** `effectiveness` = risk-effectiveness (does the control reduce risk to acceptable level).
- **R3:** `effectiveness` = outcome-effectiveness (does the measure achieve its intended outcome).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Control | None in OJ; ISO/IEC 27004 |
| R2 | Risk | None in OJ |
| R3 | Outcome | None in OJ |
R1 and R2 are the dominant industry readings. Same POLY as T3 NIS2-C13. S2.
*Berry anchor:* §3.3.1 (`effectiveness`).
**Instance 2 — COORD — S2 — `policies AND procedures`**
- **R1:** Two distinct (entity must have both policies and procedures).
- **R2:** Hendiadys (one combined concept: documented policies-and-procedures).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Two distinct | In-Directive: literal |
| R2 | Hendiadys | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
---
#### 3.1 NIS2-CL52 — Art. 25(1) — Member State encouragement of standards
**Source locus:**
> In order to promote the convergent implementation of Article 21(1) and (2), Member States shall, **<mark>without imposing or discriminating in favour of the use of a particular type of technology</mark>**, encourage the use of European and international standards and technical specifications relevant to the security of network and information systems.
**Instance 1 — VAG — S2 — `shall … encourage`**
Same `shall encourage` pattern as Art. 20(2) (NIS2-CL05) and Art. 24(1) (NIS2-CL49). Discretionary encouragement; not binding.
*Berry anchor:* §3.3.1 (`shall encourage`).
**Instance 2 — VAG — S2 — `without imposing or discriminating in favour of the use of a particular type of technology`**
The technology-neutrality clause. Three readings:
- **R1:** MS must not require a specific technology.
- **R2:** MS must not favour one technology over another.
- **R3:** Both (comprehensive technology-neutrality).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Non-imposition | In-Directive: literal `without imposing` |
| R2 | Non-discrimination | In-Directive: literal `discriminating in favour of` |
| R3 | Both | In-Directive: literal `or` (inclusive) |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`without imposing`); §5.4.7 (OR).
**Instance 3 — VAG — S2 — `European and international standards and technical specifications`**
The OR between European and international, with `and technical specifications` as an addition.
- **R1:** European standards.
- **R2:** International standards.
- **R3:** Either.
- **R4:** Plus technical specifications (always).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | European | In-Directive: literal |
| R2 | International | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
| R4 | Plus specs | In-Directive: literal `and technical specifications` |
R3 + R4 combined. S2.
*Berry anchor:* §5.4.7 (OR + AND).
**Instance 4 — VAG — S2 — `relevant to the security of network and information systems`**
`relevant` — relevant to which version? Relevant to which domain?
- **R1:** All standards relevant to NIS.
- **R2:** Standards explicitly adopted by ENISA.
- **R3:** Standards in the European/international catalogue (Reg. 1025/2012).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All NIS-relevant | In-Directive: literal `relevant` |
| R2 | ENISA-adopted | None in OJ |
| R3 | Catalogue | In-Directive: Art. 6(16)/(17) cross-ref |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->