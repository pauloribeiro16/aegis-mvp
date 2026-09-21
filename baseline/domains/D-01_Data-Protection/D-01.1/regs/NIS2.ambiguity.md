# D-01.1 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 2.1 Definition (1) `network and information system` (NIS2-D01)
**Source text:**
> **(1)** **`'network and information system'`** means:
> **(a)** an electronic communications network as defined in Article 2, point (1), of Directive (EU) 2018/1972;
> **(b)** any device or group of interconnected or related devices, one or more of which, pursuant to a programme, carry out automatic processing of digital data; or
> **(c)** digital data stored, processed, retrieved or transmitted by elements covered under points (a) and (b) for the purposes of their operation, use, protection and maintenance;
**Analysis.**
- **VAG — S2** — `related` (in (b)) is undefined. Does `related` mean physically-connected, logically-connected (shared protocol), or merely co-located? A device in the same rack that is not networked is "related" to the rack? The clause does not say. **Two readings:**
  - **R1 (broad):** any device in physical or logical proximity to a network device counts — captures operational technology (OT), IoT, building-management systems, badge readers.
  - **R2 (narrow):** `related` requires a logical connection (e.g. shared bus, MQTT broker, network gateway) — excludes isolated co-located devices.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | `related` = physical/logical proximity (broad) | None in OJ; ENISA guidance tilts broad |
  | R2 | `related` = logical connection only (narrow) | None in OJ; cybersecurity-industry practice (NIS 2 implementation studies) tilts narrow |
  *Berry anchor:* §5.1 (`related` undefined).
- **POLY — S2** — `device` in (b) has at least three readings:
  - **R1:** hardware device (physical appliance).
  - **R2:** virtual device (VM, container).
  - **R3:** software-as-device (e.g. a software-defined gateway with no dedicated hardware).
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | `device` = hardware only | None in OJ |
  | R2 | `device` = hardware or virtual | None in OJ; Reg. 2019/881 uses "ICT product" with broader scope |
  | R3 | `device` = hardware, virtual, or software-only | None in OJ; CSA cloud computing definitions allow software-only services |
  *Berry anchor:* §3.3.1 (`device`).
- **COORD — S2** — (a) OR (b) OR (c) — three coordinated definitions by disjunction. The OR is inclusive (the chapeau says `means:` then lists (a), (b), (c) — consistent with EU drafting convention for inclusive definitions). However, **(c) is a data definition** while (a) and (b) are system/equipment definitions. A system can be (a) without containing (c); a data store can be (c) without being (a) or (b). The three readings:
  - **R1:** (a), (b), (c) are all independent paths — qualifying as any one suffices.
  - **R2:** (a) and (b) are system-level; (c) is a downstream qualifier — qualifying under (a) or (b) and also holding (c) is required.
  - **R3:** The Directive uses (a) for ECS-anchored networks, (b) for ICT-anchored systems, (c) for the data dimension; an entity qualifies if any one applies, but the obligations attach to all three jointly.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Independent OR — any one path qualifies | None in OJ; drafting convention |
  | R2 | (a)/(b) qualify the system; (c) qualifies the data inside the system | None in OJ; recital context |
  | R3 | Qualifying as any one path suffices; obligations attach jointly | None in OJ |
  *Berry anchor:* §5.4.7 (OR across three sub-clauses).
---
#### 2.2 Definition (2) `security of network and information systems` (NIS2-D02)
**Source text:**
> **(2)** **`'security of network and information systems'`** means the ability of network and information systems to resist, at a given level of confidence, any event that may compromise the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, those network and information systems;
**Analysis.**
- **VAG — S3** — `at a given level of confidence`: the modifier is open. The reading determines the threshold at which an entity's security measures are deemed sufficient. Three materially distinct readings:
  - **R1:** `level of confidence` is subjective/qualitative — management attestation.
  - **R2:** `level of confidence` is relative — comparable to peer entities or sector baseline.
  - **R3:** `level of confidence` is absolute — measurable (e.g. probability metric, sigma-level).
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Subjective/qualitative (management attestation) | None in OJ |
  | R2 | Relative (peer/sector baseline) | None in OJ; ENISA security-baseline guidance |
  | R3 | Absolute (probabilistic metric) | None in OJ; ISO/IEC 27004 measurement-of-security concept |
  R1 and R3 produce materially distinct compliance obligations (R1 admits paper exercises; R3 requires measurement). R2 is intermediate. S3.
  *Berry anchor:* §5.1 (`level of confidence`).
- **POLY — S2** — `ability … to resist`: the metaphor of "resistance" implies a binary (resists/does not resist), but security is a continuous variable. The reading:
  - **R1:** Binary — the system either resists or does not.
  - **R2:** Threshold — the system resists all events up to a defined threshold.
  - **R3:** Probabilistic — the system resists with a defined probability.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Binary resistance | None in OJ |
  | R2 | Threshold resistance | None in OJ; ISO/IEC 27005 risk-threshold concept |
  | R3 | Probabilistic resistance | None in OJ; FAIR / NIST 800-30 quantitative-risk concept |
  *Berry anchor:* §3.3.1 (`ability to resist`).
- **COORD — S2** — `availability OR authenticity OR integrity OR confidentiality` (OR of four CIA-triad dimensions plus authenticity). The reading:
  - **R1:** Compromise of any one dimension triggers the security obligation.
  - **R2:** The four dimensions are the full CIA-A set; an entity is "secure" only if all four are protected.
  | # | Reading | Disambiguation source |
  |---|---|---|
  | R1 | Any one compromise = security event | None in OJ; recital 32 (cybersecurity) |
  | R2 | All four must be protected | None in OJ; NIST CSF core functions |
  *Berry anchor:* §5.4.7 (OR across four sub-clauses).
- **Layer 1 observation** — The definition defines the **state of security**, not the **state of cybersecurity**. NIS 2(2) `security of network and information systems` is a broader concept than NIS 2(3) `cybersecurity`. (3) is a cross-reference to Reg. 2019/881. The boundary between "security of network and information systems" and "cybersecurity" in NIS 2 itself is not drawn in Art. 6 — the Directive uses both terms (e.g. Art. 1(2) "high common level of cybersecurity", Art. 21(1) "security of network and information systems"). A purely linguistic Layer 1 reading flags this terminological overlap for Layer 2 adjudication.
---
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
#### 3.11 NIS2-CL17 — Art. 21(2)(h) — Cryptography and, where appropriate, encryption
**Source locus:**
> **(h)** policies and procedures regarding the use of cryptography and, where appropriate, encryption;
**Instance 1 — POLY — S2 — `cryptography` vs. `encryption`**
- **R1:** Cryptography is the broader discipline; encryption is a sub-technique (encryption is to cryptography as data-processing is to computing).
- **R2:** Cryptography and encryption are synonyms.
- **R3:** Cryptography refers to algorithm selection; encryption refers to key management.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cryptography ⊃ encryption | In-Directive: literal `cryptography and, where appropriate, encryption` |
| R2 | Synonyms | None in OJ |
| R3 | Algorithm vs. key mgmt | None in OJ |
R1 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`cryptography`/`encryption`).
**Instance 2 — VAG — S2 — `where appropriate`**
Soft hedge on the encryption sub-obligation. Reading:
- **R1:** `appropriate` is determined by risk assessment.
- **R2:** `appropriate` is determined by state-of-the-art.
- **R3:** `appropriate` is determined by the entity's classification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Risk-based | In-Directive: Art. 21(1) factors |
| R2 | State-of-the-art-based | In-Directive: Art. 21(1) sentence 2 |
| R3 | Classification-based | None in OJ |
R1 and R2 are operative. S2.
*Berry anchor:* §5.1 (`where appropriate`).
**Instance 3 — COORD — S3 — `cryptography AND, where appropriate, encryption`**
AND of two terms where one is hedged. Three readings:
- **R1:** Cryptography always required; encryption required when appropriate.
- **R2:** Cryptography = encryption (the `where appropriate` applies to both).
- **R3:** Cryptography and encryption are alternatives (OR, not AND).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hierarchical AND (cryptography always, encryption sometimes) | In-Directive: literal `cryptography and, where appropriate, encryption` |
| R2 | Equal AND with hedge on both | None in OJ |
| R3 | OR | None in OJ |
R1 is the literal reading. S3 because the surface ambiguity drives whether the entity can satisfy Art. 21(2)(h) by adopting only cryptography (R1: yes, with the hedge; R2: no; R3: no).
*Berry anchor:* §5.4.7 (AND-with-hedge).
**Layer 1 observation — T3-vs-text gap (T3 NIS2-C16/C17/C18).** T3 splits this single sub-point into three distinct sub-domains (D-01.1 at rest, D-01.2 in transit, D-01.3 key management). **The OJ text contains no at-rest / in-transit / key-management distinction.** The split is interpretive. This is the largest single T3-vs-text gap in the NIS 2 corpus (3 T3 clauses on 1 OJ sub-point).
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
#### 3.2 NIS2-CL53 — Art. 25(2) — ENISA advice and guidelines
**Source locus:**
> ENISA, in cooperation with Member States, and, where appropriate, after consulting relevant stakeholders, shall draw up **<mark>advice and guidelines</mark>** regarding the technical areas to be considered in relation to paragraph 1 as well as regarding already existing standards, including national standards, which would allow for those areas to be covered.
**Instance 1 — VAG — S2 — `shall draw up`**
`shall draw up` is mandatory (vs. `may`). ENISA is obliged to produce advice/guidelines.
*Berry anchor:* §3.3.1 (`shall draw up`).
**Instance 2 — POLY — S2 — `advice and guidelines`**
Two outputs (AND). Three readings:
- **R1:** Both required.
- **R2:** Either (substitution).
- **R3:** Composite (a single output: "advice-and-guidelines").
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal |
| R2 | Either | None in OJ |
| R3 | Composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`advice`/`guidelines`); §5.4.7 (AND).
**Instance 3 — VAG — S2 — `where appropriate, after consulting relevant stakeholders`**
Same soft-hedge + consultation pattern as Art. 22(2) (CL25).
*Berry anchor:* §5.1 (`where appropriate`); §3.3.1 (`relevant stakeholders`).
**Instance 4 — VAG — S2 — `the technical areas to be considered`**
`technical areas` — defined how? By ENISA? By standards catalogue?
- **R1:** ENISA-defined.
- **R2:** Standards-catalogue-derived.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ENISA | In-Directive: literal `ENISA … shall draw up` |
| R2 | Catalogue | None in OJ |
| R3 | Both | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`technical areas`).
**Instance 5 — VAG — S2 — `including national standards`**
`including` — illustrative (Berry `include` pattern). National standards are an example; not exhaustive.
*Berry anchor:* §5.1 (`including`).
---
### 4. Cross-clause structural observations (Art. 25)
1. **Art. 25 is encouragement-only.** No binding entity obligation. The article's operational impact is on the entity's evidence base: standards cited in Art. 25(1) and ENISA guidelines produced under Art. 25(2) are non-mandatory but provide a soft path to Art. 21 compliance.
2. **The technology-neutrality clause is the most distinctive single phrase.** `without imposing or discriminating in favour of the use of a particular type of technology` is the only explicit technology-neutrality mandate in Chapter IV. It is a structural commitment to standards-based (not technology-specific) regulation.
3. **ENISA's `shall draw up advice and guidelines` is one of the few mandatory provisions on ENISA in Chapter IV.** Most ENISA references in Chapter IV are `may` (Art. 21(5), Art. 22(1), Art. 23(11), Art. 24(3)). Art. 25(2) is `shall draw up` — a positive obligation.
---
### 5. T3-to-v0.2 mapping
T3 had no clause for Art. 25 — it was outside the T3 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 25 with 2 atomic clauses (CL52–CL53).
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | NIS2-CL52 | Art. 25(1) | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL53 | Art. 25(2) | T3 omitted; v0.2 adds. |
---
**End of Art. 25 file. Next: `99_NIS2_Synthesis.md`.**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

- **Layer 1 observation** — The GDPR analog (Art. 4(1) `personal data`) and the CRA analog (Art. 3(1) `product with digital elements`) both produce definitional-anchor problems downstream. NIS 2's `network and information system` is the operational scope-defining term of Chapter IV; every obligation in Art. 21–25 attaches to "essential and important entities" only in respect of "their" network and information systems. Resolving (1) determines the scope of all Chapter IV obligations.


### from regs/NIS2.ambiguity.md

- **VAG — S2** — `authenticity`: GDPR Art. 5(1)(d) and ISO/IEC 27000 define `authenticity`; NIS 2 does not. A reading of `authenticity` requires recourse to the broader cybersecurity-vocabulary ecosystem (ISO/IEC 27000, NIST Glossary). The Directive does not import any of these.

  *Berry anchor:* §5.1 (`authenticity` undefined).

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

### from regs/NIS2.ambiguity.md

4. **Cross-regulation parallel.** Art. 25 mirrors the standardisation provisions in CRA Art. 27 (presumption of conformity via harmonised standards) and AI Act Art. 40 (conformity assessment via harmonised standards). The `European and international standards and technical specifications` triplet is the standard cross-regulation formulation.

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=0 -->

