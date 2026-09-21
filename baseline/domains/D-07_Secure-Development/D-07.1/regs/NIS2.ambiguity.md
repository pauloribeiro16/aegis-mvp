# D-07.1 — Relevant Ambiguity (NIS 2)

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
#### 3.8 NIS2-CL14 — Art. 21(2)(e) — Acquisition, development, maintenance + vulnerability handling
**Source locus:**
> **(e)** security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure;
**Instance 1 — VAG — S2 — `security in`**
`security in` — security in the process of acquisition/development/maintenance (process-security) or security of the systems being acquired/developed/maintained (product-security)?
- **R1:** Process-security (secure SDLC).
- **R2:** Product-security (the systems themselves are secure).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Process | None in OJ; NIST SSDF |
| R2 | Product | None in OJ |
| R3 | Both | None in OJ; recital 56 |
R3 is the dominant reading. S2.
*Berry anchor:* §5.1 (`security in`).
**Instance 2 — COORD — S2 — `acquisition AND development AND maintenance`**
Three coordinated lifecycle phases.
- **R1:** Three distinct lifecycle phases, each requiring security measures.
- **R2:** Composite description of the system lifecycle.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three distinct | In-Directive: literal `acquisition, development and maintenance` |
| R2 | Composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 3 — POLY — S2 — `vulnerability handling`**
- **R1:** Process (intake → triage → fix).
- **R2:** Capability (team).
- **R3:** Programme (organisational function).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Process | None in OJ; ISO/IEC 30111 |
| R2 | Capability | None in OJ |
| R3 | Programme | None in OJ |
*Berry anchor:* §3.3.1 (`vulnerability handling`).
**Instance 4 — COORD — S2 — `vulnerability handling AND disclosure`**
- **R1:** Two distinct activities (internal handling + external disclosure).
- **R2:** Composite (one process: handle + disclose).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Two distinct | In-Directive: literal `handling and disclosure` |
| R2 | Composite | None in OJ |
R1 is the literal reading. S2. **Cross-reference:** Art. 12(1) NIS 2 designates a CSIRT as coordinator for coordinated vulnerability disclosure — institutional context.
*Berry anchor:* §5.4.7 (AND).
---
#### 3.14 NIS2-CL20 — Art. 21(3) sentence 1 — Supply-chain risk assessment
**Source locus:**
> Member States shall ensure that, when considering which measures referred to in paragraph 2, point (d), of this Article are appropriate, entities take into account the vulnerabilities specific to each direct supplier and service provider and the overall quality of products and cybersecurity practices of their suppliers and service providers, including their secure development procedures.
**Instance 1 — VAG — S2 — `overall quality`**
`overall quality` — quality of what? Product? Service? Supplier-relationship? Process?
- **R1:** Product-quality.
- **R2:** Service-quality.
- **R3:** Process-quality.
- **R4:** Composite (product + service + process).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Product | None in OJ |
| R2 | Service | None in OJ |
| R3 | Process | None in OJ |
| R4 | Composite | In-Directive: literal `overall` suggests composite |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`quality`).
**Instance 2 — VAG — S2 — `secure development procedures`**
`secure development procedures` — same VAG as Art. 21(2)(e) `security in … development`. Reading:
- **R1:** Internal secure-SDLC.
- **R2:** External supplier assessment (SDLC of supplier).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Internal | None in OJ |
| R2 | External (supplier) | In-Directive: literal `their suppliers` |
| R3 | Both | In-Directive: Art. 21(2)(d) is about supplier relationships |
R2 is the literal reading (the obligation is on the entity to assess the supplier's SDLC). S2.
*Berry anchor:* §3.3.1 (`secure development procedures`).
**Instance 3 — POLY — S2 — `vulnerabilities`**
- **R1:** Security vulnerabilities (CVE-type).
- **R2:** Business vulnerabilities (SPOF, dependency).
- **R3:** Compliance vulnerabilities (certification gaps).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Security | In-Directive: Art. 6(15) `vulnerability` definition |
| R2 | Business | None in OJ |
| R3 | Compliance | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`vulnerabilities`).
**Instance 4 — COORD — S2 — `vulnerabilities AND overall quality AND secure development procedures`**
Three coordinated assessment objects, each requiring a distinct methodology. R1 reading.
*Berry anchor:* §5.5 (three-way coordination).
**Instance 5 — SCOPE-Q — S2 — `each`**
`vulnerabilities specific to each direct supplier and service provider` (Berry §5.2.1): the unit (supplier-entity vs. supplier-product vs. supplier-service) is unspecified.
- **R1:** Each supplier-entity.
- **R2:** Each supplier-product.
- **R3:** Each supplier-service.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity | In-Directive: literal `each direct supplier and service provider` |
| R2 | Product | None in OJ |
| R3 | Service | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.2.1 (`each`).
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

**Layer 1 observation — T3-vs-text gap (T3 NIS2-C11).** T3 reads this clause as `CI/CD Pipeline Security`. **The OJ Art. 21(2)(e) text does not contain `pipeline`, `CI`, `CD`, `continuous integration`, or `continuous deployment`.** Pipeline security as a distinct obligation is a T3-imposed layer, not a Directive obligation. Same T3-vs-text gap pattern as GDPR C15/C17/C28 and CRA C03/C06.

### from regs/NIS2.ambiguity.md

4. **Cross-regulation parallel.** Art. 25 mirrors the standardisation provisions in CRA Art. 27 (presumption of conformity via harmonised standards) and AI Act Art. 40 (conformity assessment via harmonised standards). The `European and international standards and technical specifications` triplet is the standard cross-regulation formulation.

<!-- aegis:purity: own_reg=NIS2; demoted=2; core_cross_mentions=0 -->

