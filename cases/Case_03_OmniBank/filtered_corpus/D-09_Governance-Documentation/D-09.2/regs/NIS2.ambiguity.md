# D-09.2 — Relevant Ambiguity (NIS 2)

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
#### 3.4 NIS2-CL10 — Art. 21(2)(a) — Risk analysis / IS security policies
**Source locus:**
> **(a)** policies on risk analysis and information system security;
**Instance 1 — VAG — S2 — opening of 21(1) propagation**
The chapeau of Art. 21(2) says "The measures referred to in paragraph 1 shall … include at least the following". The `appropriate and proportionate` qualifier (CL07 Instance 1) propagates to every sub-point. Every (a)–(j) sub-point therefore inherits S3 VAG on `appropriate and proportionate`. **The 10 sub-points (CL10–CL19) carry this propagated instance in addition to their own.**
**Instance 2 — POLY — S2 — `policies`**
- **R1:** Formal documented policies (PDF, internal portal).
- **R2:** Informal practices (de facto policies, unwritten norms).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Formal | None in OJ; recital 56 |
| R2 | Informal | None in OJ |
*Berry anchor:* §3.3.1 (`policies`).
**Instance 3 — COORD — S2 — `risk analysis AND information system security`**
- **R1:** Two distinct policy domains (entity must have a risk-analysis policy AND an IS-security policy).
- **R2:** Single composite domain (one policy covering both).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Two policies | In-Directive: literal `risk analysis and information system security` |
| R2 | One composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
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

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

### from regs/NIS2.ambiguity.md

**Layer 1 observation** — The physical-environment scope of NIS 2 is broader than DORA, CRA, AI Act (all of which are software/cyber-focused). The all-hazards approach with physical-environment coverage is the **single most distinctive feature of NIS 2 vs the other four regulations** in the corpus. **For software-compliance analysis, the physical-environment dimension is out-of-scope**: it does not generate software requirements, only physical-security requirements. The clause is included for completeness but flagged as **out-of-scope for the software-compliance track of the methodology**. Layer 3 (inference-trust) will need to adjudicate whether software-software integration controls are needed for the physical-environment dimension (e.g. environmental sensors feeding into SIEM).

<!-- aegis:purity: own_reg=NIS2; demoted=2; core_cross_mentions=0 -->