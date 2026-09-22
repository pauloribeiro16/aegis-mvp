# D-06.3 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.6 NIS2-CL06 — Art. 20 chapeau — Implicit proportionality / scope hook
**Source locus (chapeau of Art. 20, paraphrased from sentence 1):**
> Member States shall ensure that [the obligations] apply to essential and important entities.
**Instance 1 — VAG + POLY — S2 — `essential and important entities`**
The term is defined in Art. 3 but Art. 3's own classification criteria (size thresholds, sectoral lists, Member State discretion) are open. Three layers of indeterminacy:
- Layer A: `essential` vs. `important` — different supervisory regimes (Art. 32 fines, Art. 33 enforcement measures).
- Layer B: size thresholds (medium vs. large per Recommendation 2003/361/EC).
- Layer C: sectoral coverage (Annex I/II).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Two-tier binary (essential OR important) | In-Directive: Art. 3(1)–(2) |
| R2 | Member-State-discretionary boundary | In-Directive: Art. 3(1)(e), (g) — Member States may identify additional essential entities |
| R3 | Annex I/II sector lists are exhaustive | In-Directive: Art. 2(1) + Annex I/II |
R1 is the structural reading. R2 is the Member-State-discretion reading. R3 is the sectoral-exhaustive reading. S2 because the surface ambiguity drives whether an entity falls in the scope of Art. 20 (R1/R2/R3 may give different answers for borderline cases like cloud-computing providers with mixed sectoral exposure).
*Berry anchor:* §3.3.1 (`essential and important entities`); §5.2.1 (Annex lists).
**Layer 1 observation** — The Art. 3 classification of an entity is a **prerequisite** for all of Art. 20, 21, 22, 23, 24, 25 obligations. If an entity is not classified as essential or important, none of these apply. The classification itself is ambiguous (R2: Member-State discretion; R3: Annex I/II exhaustive). This is the **single most important scope-defining layer of NIS 2** — flagged in synthesis.
---
### 4. Cross-clause structural observations (Art. 20)
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| NIS2-C01 | Art. 20(1) | NIS2-CL01 + NIS2-CL02 | Art. 20(1) | v0.2 splits sentence 1 (CL01) from sentence 2 carve-out (CL02); T3 only analysed sentence 1. |
| NIS2-C02 | Art. 20(2) | NIS2-CL03 + NIS2-CL04 + NIS2-CL05 | Art. 20(2) | v0.2 splits the three coordinated sub-phrases; T3 treated sentence 2 as a single clause. |
| (none) | — | NIS2-CL06 | Art. 20 chapeau | v0.2 adds the Art. 3 classification-propagation analysis that T3 omitted. |
---
**End of Art. 20 file. Next: `03_NIS2_Art21_RiskManagement.md` (the heart of NIS 2).**
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
#### 3.15 NIS2-CL21 — Art. 21(3) sentence 2 — EU-level risk propagation
**Source locus:**
> Member States shall also ensure that, when considering which measures referred to in that point are appropriate, entities are required to take into account the results of the coordinated security risk assessments of critical supply chains carried out in accordance with Article 22(1).
**Instance 1 — VAG — S2 — `take into account`**
`take into account` — passive consideration or active integration?
- **R1:** Passive consideration (entity reads the assessment).
- **R2:** Active integration (entity incorporates the assessment into its own risk management).
- **R3:** Compliance (entity adopts the assessment's recommendations).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Passive | In-Directive: literal `take into account` |
| R2 | Active | None in OJ |
| R3 | Compliance | None in OJ |
R1 is the literal reading. R3 implies a stronger obligation that the Directive does not state. S2.
*Berry anchor:* §3.3.1 (`take into account`).
**Instance 2 — POLY — S2 — `results`**
`results` — recommendations, findings, or full report?
- **R1:** Recommendations.
- **R2:** Findings.
- **R3:** Full report.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Recommendations | None in OJ |
| R2 | Findings | None in OJ |
| R3 | Full report | None in OJ |
*Berry anchor:* §3.3.1 (`results`).
---
## NIS 2 v0.2 — Article 22 Coordinated Security Risk Assessments of Critical Supply Chains
> **Source.** OJ L 333, 27.12.2022, p. 128. `03_REFERENCE_MATERIAL/Regulatory_References/NIS2.txt`, lines ~2870–2890.
>
> **Pattern.** Article quoted in full (paragraph by paragraph), then per-clause analysis.
>
> **Article 22 is short (2 paragraphs) but materially consequential:** it operationalises the supply-chain analysis at the EU level, and Art. 21(3) sentence 2 (already analysed in `03_NIS2_Art21_RiskManagement.md` NIS2-CL21) requires entities to "take into account" the results of these EU-level assessments. This is the **single most important entity-facing propagation hook in NIS 2** for the supply-chain theme.
---
### 1. Article 22 — full text
> **Article 22 — Union level coordinated security risk assessments of critical supply chains**
>
> **1.** The Cooperation Group, in cooperation with the Commission and ENISA, **<mark>may carry out coordinated security risk assessments of specific critical ICT services, ICT systems or ICT products supply chains</mark>**, taking into account **technical and, where relevant, non-technical risk factors**.
> **2.** The Commission, after consulting the Cooperation Group and ENISA, and, where necessary, relevant stakeholders, shall **identify the specific critical ICT services, ICT systems or ICT products** that may be subject to the coordinated security risk assessment referred to in paragraph 1.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| NIS2-CL23 | Art. 22(1) sentence 1 (the assessment) | EU-level assessment | **S2** | Cooperation Group may carry out coordinated risk assessments of critical ICT supply chains. |
| NIS2-CL24 | Art. 22(1) sentence 2 (the factors) | Risk-factor scope | **S2** | Technical and, where relevant, non-technical risk factors. |
| NIS2-CL25 | Art. 22(2) | Commission selection | **S2** | Commission identifies the specific critical ICT services/systems/products subject to assessment. |
**Total: 3 atomic clauses.**
---
### 3. Detailed cards
#### 3.1 NIS2-CL23 — Art. 22(1) sentence 1 — Coordinated supply-chain risk assessment
**Source locus:**
> The Cooperation Group, in cooperation with the Commission and ENISA, **<mark>may carry out coordinated security risk assessments of specific critical ICT services, ICT systems or ICT products supply chains</mark>**.
**Instance 1 — VAG — S2 — `critical` (in "critical ICT services, ICT systems or ICT products")**
`critical` is undefined in Art. 6. The reading:
- **R1:** `critical` = essential to the functioning of the internal market.
- **R2:** `critical` = identified in Annex I/II as a sector.
- **R3:** `critical` = significant impact if disrupted (cf. Art. 2(2)(c)–(d) "significant impact").
- **R4:** `critical` = not elsewhere defined; Commission determines via implementing acts.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Internal-market essentiality | None in OJ |
| R2 | Annex I/II sector | In-Directive: Annex I/II is the closest sectoral list |
| R3 | Significant-impact-based | In-Directive: Art. 2(2)(c)–(d) cross-ref |
| R4 | Commission-determined | In-Directive: Art. 22(2) gives Commission selection power |
R4 is the dominant reading (Art. 22(2) places the selection with the Commission). S2.
*Berry anchor:* §5.1 (`critical`).
**Instance 2 — VAG — S2 — `specific` (in "specific critical ICT services, ICT systems or ICT products")**
`specific` — specifies on what basis?
- **R1:** `specific` by sector.
- **R2:** `specific` by product/service category.
- **R3:** `specific` by single ICT product/service (e.g. a named product or vendor).
- **R4:** `specific` = ad hoc / discretionary by Cooperation Group.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sector-based | None in OJ |
| R2 | Category-based | None in OJ |
| R3 | Named product | None in OJ; recital 60 (case-by-case) |
| R4 | Ad hoc | In-Directive: literal `may carry out` is discretionary |
R4 is the dominant reading (the chapeau `may carry out` is discretionary). S2.
*Berry anchor:* §5.1 (`specific`).
**Instance 3 — POLY — S2 — `ICT services, ICT systems or ICT products`**
The OR across three ICT categories. The reading:
- **R1:** Three distinct categories — assessment can target any one of the three.
- **R2:** Composite category — assessment can target an integrated offering spanning all three.
- **R3:** `ICT services` and `ICT systems` are functional; `ICT products` is artefact-based.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal OR |
| R2 | Composite | None in OJ |
| R3 | Functional vs. artefact | None in OJ; recital 60 |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`ICT services`/`ICT systems`/`ICT products`); §5.4.7 (OR).
**Instance 4 — POLY — S2 — `supply chains`**
`supply chains` — the chain of suppliers, the chain of products, or the chain of services?
- **R1:** Chain of suppliers (organisational).
- **R2:** Chain of products (artefact-based).
- **R3:** Chain of services (service-based).
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Suppliers | None in OJ |
| R2 | Products | None in OJ |
| R3 | Services | None in OJ |
| R4 | All | In-Directive: literal `supply chains` is broad |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`supply chains`).
**Instance 5 — VAG — S2 — `coordinated`**
`coordinated` — coordinated by whom? Coordinated across what dimension?
- **R1:** Coordinated across Member States.
- **R2:** Coordinated across sectors.
- **R3:** Coordinated across the Cooperation Group + Commission + ENISA (institutional).
- **R4:** All three (cross-Member-State, cross-sector, multi-institutional).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cross-MS | None in OJ; recital 60 |
| R2 | Cross-sector | None in OJ |
| R3 | Multi-institutional | In-Directive: literal `Cooperation Group, in cooperation with the Commission and ENISA` |
| R4 | All | None in OJ |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`coordinated`).
**Instance 6 — VAG — S2 — `security risk assessment`**
`security risk assessment` — assessment of what? Risks to ICT supply chains, risks through ICT supply chains, or risks by ICT supply chains?
- **R1:** Risks **to** ICT supply chains (e.g. disruption of supply).
- **R2:** Risks **through** ICT supply chains (e.g. compromised product spreads risk downstream).
- **R3:** Risks **by** ICT supply chains (e.g. supplier misfeasance).
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | To | None in OJ |
| R2 | Through | None in OJ |
| R3 | By | None in OJ |
| R4 | All | None in OJ; recital 60 |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`security risk assessment`).
**Instance 7 — VAG — S2 — `may carry out`**
`may carry out` is permissive (vs. mandatory `shall carry out`). The reading:
- **R1:** Discretionary — Cooperation Group decides whether to act.
- **R2:** Mandatory when triggered — once the Commission identifies a supply chain under Art. 22(2), the assessment is mandatory.
- **R3:** Hybrid.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Pure discretion | In-Directive: literal `may` |
| R2 | Triggered mandatory | None in OJ; recital 60 |
| R3 | Hybrid | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`may carry out`).
---
#### 3.2 NIS2-CL24 — Art. 22(1) sentence 2 — Risk-factor scope
**Source locus:**
> …taking into account **technical and, where relevant, non-technical risk factors**.
**Instance 1 — VAG — S2 — `technical … non-technical risk factors`**
The OR between `technical` and `non-technical`, with `where relevant` on the non-technical side. Three readings:
- **R1:** Technical factors always; non-technical when relevant.
- **R2:** Either category when relevant.
- **R3:** Both when relevant.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Technical always, non-tech when relevant | In-Directive: literal `technical and, where relevant, non-technical` |
| R2 | Either | None in OJ |
| R3 | Both | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`where relevant`); §5.4.7 (AND with hedge).
**Instance 2 — VAG — S2 — `risk factors`**
`risk factors` — same POLY as Art. 6(9) `risk`. Same readings:
- **R1:** Threat-based (CVE, attack surface).
- **R2:** Impact-based (downstream consequences).
- **R3:** Likelihood-based (probability).
- **R4:** Composite.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Threat | None in OJ |
| R2 | Impact | None in OJ |
| R3 | Likelihood | None in OJ |
| R4 | Composite | In-Directive: Art. 6(9) `risk` definition |
R4 is the dominant reading (inherits Art. 6(9)). S2.
*Berry anchor:* §3.3.1 (`risk factors`).
**Instance 3 — POLY — S2 — `non-technical`**
`non-technical` — what does it cover?
- **R1:** Organisational/governance.
- **R2:** Geopolitical (e.g. supplier's country).
- **R3:** Market structure (concentration, single-points-of-failure).
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Organisational | None in OJ |
| R2 | Geopolitical | None in OJ; recital 60 |
| R3 | Market | None in OJ |
| R4 | All | None in OJ |
R4 is the dominant reading. S2.
*Berry anchor:* §3.3.1 (`non-technical`).
---
## NIS 2 v0.2 — Article 24 Use of European Cybersecurity Certification Schemes
> **Source.** OJ L 333, 27.12.2022, p. 130–131. `03_REFERENCE_MATERIAL/Regulatory_References/NIS2.txt`, lines ~3020–3050.
>
> **Pattern.** Article quoted in full, then per-clause analysis.
>
> **Article 24 has 3 paragraphs and is short.** It is the only provision in Chapter IV that allows Member States to *require* the use of European cybersecurity certification schemes — a binding-certification hook that integrates the Cybersecurity Act (Reg. 2019/881) into NIS 2 enforcement.
---
### 1. Article 24 — full text
> **Article 24 — Use of European cybersecurity certification schemes**
>
> **1.** In order to demonstrate compliance with particular requirements of Article 21, Member States **<mark>may require</mark>** essential and important entities to use particular ICT products, ICT services and ICT processes, developed by the essential or important entity or procured from third parties, that are **certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881**. Furthermore, Member States shall encourage essential and important entities to use **<mark>qualified trust services</mark>**.
> **2.** The Commission is empowered to adopt delegated acts, in accordance with Article 38, to supplement this Directive by specifying which categories of essential and important entities are to be required to use certain certified ICT products, ICT services and ICT processes or obtain a certificate under a European cybersecurity certification scheme adopted pursuant to Article 49 of Regulation (EU) 2019/881. Those delegated acts shall be adopted where insufficient levels of cybersecurity have been identified and shall include an implementation period.
>
> Before adopting such delegated acts, the Commission shall carry out an impact assessment and shall carry out consultations in accordance with Article 56 of Regulation (EU) 2019/881.
>
> **3.** Where no appropriate European cybersecurity certification scheme for the purposes of paragraph 2 of this Article is available, the Commission may, after consulting the Cooperation Group and the European Cybersecurity Certification Group, request ENISA to prepare a candidate scheme pursuant to Article 48(2) of Regulation (EU) 2019/881.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| NIS2-CL48 | Art. 24(1) sentence 1 (certification requirement) | Certification hook | **S2** | Member States may require entities to use certified ICT products/services/processes. |
| NIS2-CL49 | Art. 24(1) sentence 2 (qualified trust services) | Encouragement | **S2** | Member States shall encourage use of qualified trust services. |
| NIS2-CL50 | Art. 24(2) (Commission delegated acts) | Delegated acts | **S2** | Commission may specify which entities must use certified products. |
| NIS2-CL51 | Art. 24(3) (ENISA candidate scheme) | ENISA power | **S2** | Commission may request ENISA to prepare a candidate scheme. |
**Total: 4 atomic clauses.**
---
### 3. Detailed cards
#### 3.1 NIS2-CL48 — Art. 24(1) sentence 1 — Certification requirement
**Source locus:**
> In order to demonstrate compliance with particular requirements of Article 21, Member States **<mark>may require</mark>** essential and important entities to use particular ICT products, ICT services and ICT processes, developed by the essential or important entity or procured from third parties, that are **certified under European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881**.
**Instance 1 — VAG — S2 — `may require`**
Member State discretion. Three readings:
- **R1:** Pure discretion — each MS decides.
- **R2:** Discretion conditioned on Art. 21 compliance — `In order to demonstrate compliance`.
- **R3:** Discretion conditioned on Commission delegated acts (Art. 24(2)).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Discretion | In-Directive: literal `may require` |
| R2 | Compliance-conditioned | In-Directive: literal `In order to demonstrate compliance` |
| R3 | Commission-conditioned | In-Directive: Art. 24(2) |
R1 is the literal reading; R2 and R3 are contextual modifiers. S2.
*Berry anchor:* §3.3.1 (`may require`).
**Instance 2 — VAG — S2 — `particular requirements of Article 21`**
`particular requirements` — which sub-points of Art. 21(2)(a)–(j)?
- **R1:** Any sub-point.
- **R2:** Only sub-points that are certification-relevant (e.g. cryptography (h), access control (i), MFA (j)).
- **R3:** Sub-points explicitly named in delegated acts.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any | In-Directive: literal |
| R2 | Certification-relevant | None in OJ |
| R3 | Delegated-act-named | In-Directive: Art. 24(2) |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`particular`).
**Instance 3 — POLY — S2 — `ICT products, ICT services and ICT processes`**
Three categories (AND). Same coordination pattern as Art. 22(1) (CL23) and Art. 21(2) (NIS2-CL07).
- **R1:** Three distinct categories (any of which may be required).
- **R2:** Composite (entity may use any of the three).
- **R3:** All three required cumulatively.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal |
| R2 | Composite | None in OJ |
| R3 | All | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`ICT products`/`ICT services`/`ICT processes`); §5.5 (three-way coordination).
**Instance 4 — POLY — S2 — `developed by the essential or important entity or procured from third parties`**
The OR between in-house and procured.
- **R1:** In-house or procured (entity's choice).
- **R2:** The certification requirement applies only to procured (third-party) products.
- **R3:** Applies to both equally.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity choice | In-Directive: literal |
| R2 | Procured only | None in OJ |
| R3 | Both equally | In-Directive: literal `or` |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 5 — VAG — S2 — `European cybersecurity certification schemes adopted pursuant to Article 49 of Regulation (EU) 2019/881`**
Cross-reference to the Cybersecurity Act. The schemes are defined and adopted by the CSA. The Directive imports the CSA's certification architecture.
*Berry anchor:* §3.3.1 (`European cybersecurity certification schemes`).
---
#### 3.2 NIS2-CL49 — Art. 24(1) sentence 2 — Qualified trust services
**Source locus:**
> Furthermore, Member States shall encourage essential and important entities to use **<mark>qualified trust services</mark>**.
**Instance 1 — VAG — S2 — `shall encourage`**
`shall encourage` — same as Art. 20(2) (NIS2-CL05). Discretionary encouragement; not binding.
*Berry anchor:* §3.3.1 (`shall encourage`).
**Instance 2 — POLY — S2 — `qualified trust services`**
Cross-reference to Art. 6(26) `qualified trust service` (Reg. 910/2014 / eIDAS). Inherits the eIDAS definition.
*Berry anchor:* §3.3.1 (`qualified trust services`).
---
#### 3.3 NIS2-CL50 — Art. 24(2) — Commission delegated acts
**Source locus:**
> The Commission is empowered to adopt delegated acts, in accordance with Article 38, to supplement this Directive by specifying which categories of essential and important entities are to be required to use certain certified ICT products, ICT services and ICT processes or obtain a certificate under a European cybersecurity certification scheme adopted pursuant to Article 49 of Regulation (EU) 2019/881. Those delegated acts shall be adopted where insufficient levels of cybersecurity have been identified and shall include an implementation period.
**Instance 1 — VAG — S2 — `insufficient levels of cybersecurity`**
`insufficient levels` — measured how? By what methodology?
- **R1:** Measured by CSA (ENISA threat landscape).
- **R2:** Measured by national CSAs.
- **R3:** Measured by incident statistics (Art. 23).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ENISA | In-Directive: ENISA is the closest authority |
| R2 | National CSA | None in OJ |
| R3 | Incidents | In-Directive: Art. 23 incident data |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`insufficient levels`).
**Instance 2 — VAG — S2 — `categories of essential and important entities`**
`categories` — by sector? By size? By risk profile?
- **R1:** Sector-based (Annex I/II).
- **R2:** Size-based (Rec. 2003/361/EC).
- **R3:** Risk-profile-based.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sector | In-Directive: Annex I/II |
| R2 | Size | In-Directive: Art. 3 cross-ref |
| R3 | Risk | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`categories`).
**Instance 3 — VAG — S2 — `shall include an implementation period`**
`implementation period` — undefined. How long?
- **R1:** 6 months.
- **R2:** 12 months.
- **R3:** 24 months.
- **R4:** Discretionary.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 6m | None in OJ |
| R2 | 12m | None in OJ |
| R3 | 24m | None in OJ |
| R4 | Discretionary | In-Directive: literal `shall include` but content undefined |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`implementation period`).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

1. **Art. 20(1) is the only direct personal-liability provision in NIS 2.** No other article in Chapter IV imposes liability on natural persons. The provision is short but materially consequential. National implementations have begun diverging (e.g. Belgium's transposition law, France's transposition law) on which liability types attach.
2. **Art. 20(2) creates a two-tier training obligation:** mandatory (for members) + encouraged (for employees). The asymmetry is intentional in the Directive; the operational impact is that entities may be judged on management-body training compliance but not on employee training.
3. **The management-body training obligation is the second cross-regulation `training` polysemy hotspot** (the first was GDPR Art. 39 DPO training; the third is CRA Annex I Part II §2(c) `security update procedures` which includes training). All three share the same POLY pattern.
4. **The `essential and important entities` classification propagates through every Chapter IV clause.** Resolving it is the prerequisite for any other finding.

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

### from regs/NIS2.ambiguity.md

**Layer 1 observation — T3-vs-text gap (T3 NIS2-C11).** T3 reads this clause as `CI/CD Pipeline Security`. **The OJ Art. 21(2)(e) text does not contain `pipeline`, `CI`, `CD`, `continuous integration`, or `continuous deployment`.** Pipeline security as a distinct obligation is a T3-imposed layer, not a Directive obligation. Same T3-vs-text gap pattern as GDPR C15/C17/C28 and CRA C03/C06.

<!-- aegis:purity: own_reg=NIS2; demoted=3; core_cross_mentions=0 -->