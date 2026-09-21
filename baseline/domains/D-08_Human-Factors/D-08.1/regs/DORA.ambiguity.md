# D-08.1 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
##### 5.2.3 C26 — T3 patch-management mapping error (mapped to Art. 13(6) instead of Art. 9(4)(f))
#### 4.26 CL20-1 — Art. 20 — ESAs RTS/ITS mandate (whole article)
**Source locus:** Art. 20, in its entirety.
> The ESAs, through the Joint Committee, and in consultation with ENISA and the ECB, shall develop:
>
> (a) common draft regulatory technical standards in order to:
>
> (i) establish the content of the reports for major ICT-related incidents in order to reflect the criteria laid down in Article 18(1) and incorporate further elements, such as details for establishing the relevance of the reporting for other Member States and whether it constitutes a major operational or security payment-related incident or not;
>
> (ii) determine the time limits for the initial notification and for each report referred to in Article 19(4);
>
> (iii) establish the content of the notification for significant cyber threats.
>
> When developing those draft regulatory technical standards, the ESAs shall take into account the **size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations**, and in particular, with a view to ensuring that, for the purposes of this paragraph, point (a), point (ii), different time limits may reflect, as appropriate, specificities of financial sectors, without prejudice to maintaining a consistent approach to ICT-related incident reporting pursuant to this Regulation and to Directive (EU) 2022/2555. The ESAs shall, as applicable, provide justification when deviating from the approaches taken in the context of that Directive;
>
> (b) common draft implementing technical standards in order to establish the standard forms, templates and procedures for financial entities to report a major ICT-related incident and to notify a significant cyber threat.
>
> The ESAs shall submit the common draft regulatory technical standards referred to in the first paragraph, point (a), and the common draft implementing technical standards referred to in the first paragraph, point (b), to the Commission by **17 July 2024**.
**Instance 1 — VAG — S3 — `size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations`**
A four-factor proportionality formulation (size + risk profile + nature + scale + complexity, 5 adjectives actually). Same Berry pattern as Art. 4(2) chapeau. S3 (each factor admits S2 reading; the combination rule is itself undefined).
*Berry anchor:* §5.4.7 (5-way AND); §3.3.1 (`size`, `risk profile`, `nature, scale and complexity`); cf. DORA Art. 4(2).
**Instance 2 — VAG — S3 — `specificities of financial sectors`**
`specificities` undefined. Three readings:
- **R1:** Sectoral (banking vs. insurance vs. securities).
- **R2:** Sub-sectoral (retail banking vs. investment banking).
- **R3:** Business-model-specific.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sectoral | None in OJ |
| R2 | Sub-sectoral | In-Directive: recital 56 |
| R3 | Business-model | None in OJ |
S3.
*Berry anchor:* §5.1 (`specificities`); §3.3.1 (`financial sectors`).
**Instance 3 — VAG — S3 — `consistent approach … pursuant to this Regulation and to Directive (EU) 2022/2555`**
*Berry anchor:* §3.3.1 (`consistent approach`).
**Instance 4 — POLY — S2 — `standard forms, templates and procedures`**
Three operational artefacts (AND). S2.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`forms`, `templates`, `procedures`).
**Definitional anchor:** DORA-D10; DORA-D13.
**RTS-pending:** **YES — Art. 20 is the pure RTS+ITS delegation of Ch. III.** Both deadlines = 17 July 2024.
| Sub-act | Status (mid-2025) |
|---|---|
| RTS under (a)(i) (report content) | **Adopted** as Implementing Regulation (EU) 2024/2956 Annex II–IV. |
| RTS under (a)(ii) (time limits) | Per-sector time limits laid down in Reg. (EU) 2024/2956 Annex II. |
| RTS under (a)(iii) (cyber-threat notification content) | **Adopted** in Reg. (EU) 2024/2956 Annex III. |
| ITS under (b) (standard forms, templates, procedures) | **Adopted** in Reg. (EU) 2024/2956 Annex IV. |
Net: as of mid-2025, **the Art. 20 mandates are substantially implemented via Reg. (EU) 2024/2956** but Layer 1 catalogues the RTS-pending character because OJ Art. 20 is, by its own terms, an RTS delegation.
**Proportionality-status:** Art. 4 applies (explicit cross-reference).
---
#### 4.27 CL21-1 — Art. 21(1)+(2) — Single EU Hub feasibility mandate
**Source locus:** Art. 21(1) and 21(2).
> 1. The ESAs, through the Joint Committee, and in consultation with the ECB and ENISA, shall prepare a joint report assessing the **feasibility of further centralisation of incident reporting through the establishment of a single EU Hub for major ICT-related incident reporting** by financial entities. The joint report shall explore ways to facilitate the flow of ICT-related incident reporting, reduce associated costs and underpin thematic analyses with a view to enhancing supervisory convergence.
>
> 2. The joint report referred to in paragraph 1 shall comprise at least the following elements:
>
> (a) prerequisites for the establishment of a single EU Hub;
>
> (b) benefits, limitations and risks, including risks associated with the high concentration of sensitive information;
>
> (c) the necessary capability to ensure interoperability with regard to other relevant reporting schemes;
>
> (d) elements of operational management;
>
> (e) conditions of membership;
>
> (f) technical arrangements for financial entities and national competent authorities to access the single EU Hub;
>
> (g) a preliminary assessment of financial costs incurred by setting-up the operational platform supporting the single EU Hub, including the requisite expertise.
**Instance 1 — VAG — S3 — `single EU Hub`**
`single` + `Hub` — the architectural choice is undefined.
- **R1:** Single centralised data platform (one location, all CAs access).
- **R2:** Single API gateway (each CA holds data, common API).
- **R3:** Single standard (distributed but interoperable).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Centralised platform | In-Directive: literal `single EU Hub` |
| R2 | API gateway | None in OJ |
| R3 | Single standard | None in OJ |
S3.
*Berry anchor:* §3.3.1 (`single`, `Hub`); §5.1 (`single`).
**Instance 2 — VAG — S3 — `feasibility`**
`feasibility` of centralisation is broad — technical + legal + operational + financial + governance. S3.
*Berry anchor:* §5.1 (`feasibility`).
**Instance 3 — VAG — S3 — `thematic analyses with a view to enhancing supervisory convergence`**
`thematic analyses` + `supervisory convergence` — undefined. S3.
*Berry anchor:* §3.3.1 (`thematic analyses`, `supervisory convergence`).
**Instance 4 — VAG — S2 — `high concentration of sensitive information`**
`high concentration` is undefined. Same Berry pattern as DORA-D29 `ICT concentration risk`. S2.
*Berry anchor:* §5.1 (`high concentration`); cf. DORA-D29.
**Instance 5 — POLY — S2 — 7 enumerated elements**
Each element admits its own internal ambiguity:
| Element | Key ambiguity | Berry anchor |
|---|---|---|
| (a) `prerequisites` | Hard vs. soft preconditions | §3.3.1 (`prerequisites`) |
| (b) `benefits, limitations and risks` | Three-way comparison standard | §5.4.7 (three-way) |
| (c) `interoperability` | Technical vs. semantic | §3.3.1 (`interoperability`) |
| (d) `operational management` | Undefined scope | §3.3.1 (`operational management`) |
| (e) `conditions of membership` | Who becomes a member? | §3.3.1 (`membership`) |
| (f) `technical arrangements` | Read-only vs. write access | §3.3.1 (`technical arrangements`) |
| (g) `preliminary assessment of financial costs` | Method-based vs. estimate-based | §3.3.1 (`preliminary`) |
S2 (per-element); aggregate S3 due to the open-ended `at least` qualifier.
*Berry anchor:* §5.4.5 (illustrative use — `at least`); §3.3.1.
**Definitional anchor:** DORA-D29 `ICT concentration risk`; DORA Art. 50 (administrative penalties context).
**Scope:** regulator-internal (between ESAs and NCA institutional architecture, not directly entity-facing).
**Proportionality-status:** Art. 4 applies.
---
## DORA v0.2 — Chapter V Section I: Managing ICT Third-Party Risk (Art. 28–30)
> **Source.** OJ L 333, 27.12.2022, p. 49–53. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`:
> - Art. 28: lines **2819–2967** (10 paragraphs + chapeau).
> - Art. 29: lines **2970–3009** (2 paragraphs, 6 sub-paragraphs, no sub-letter points).
> - Art. 30: lines **3011–3118** (5 paragraphs; 30(2) lists 9 sub-elements (a)–(i); 30(3) lists 6 sub-elements (a)–(f), with (e) carrying 4 sub-points and (f) carrying 2 sub-points).
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 30(8)` (where applicable), `scope: regulator→financial-entity` (entity-facing contract obligations).
>
> **Chapter V Section I** establishes the entity-facing third-party risk regime. Art. 28 is the umbrella principles clause (governance, strategy, register, pre-contractual assessment, exit). Art. 29 is the **preliminary ICT concentration risk** assessment at entity level (NEW in v0.2; T3 omitted). Art. 30 enumerates the **15 key contractual provisions** (9 in Art. 30(2) for all ICT services; 6 in Art. 30(3) for critical or important functions).
>
> **Articles in this file:** 3 articles, 17 paragraphs, **23 atomic clauses** (CL28-1 … CL28-6; CL29-1 … CL29-2; CL30-1 … CL30-15).
>
> **Compactness notes (v0.2 D1, D3, D5):**
> - **D1** — strong compaction: variant readings consolidated from 3→2 where two readings yield identical compliance practice; 3 retained only where distinct obligations emerge.
> - **D3** — Layer 1 only: catalogue-only observations; no Layer 2 normative force introduced.
> - **D5** — entity-facing only: scope is `regulator→financial-entity`; CTPP-side obligations expressed as entity obligations to contractually enforce.
>
> **Note on Art. 4 (Proportionality):** every clause card in this file carries `proportionality-status: Art. 4 applies` (per pilot convention; Ch. V Sec. I is entity-facing).
>
> **Note on Art. 30(8) RTS-pending:** the substantive RTS mandate for **standard contractual clauses** (key for Art. 30) sits in Art. 30(8) (out of scope for this file; the substantive content is in Art. 30(1)–(7)). The RTS in Art. 28(10) (policy on ICT-CTPPs) and Art. 30(5) (subcontracting determination) are catalogued in this file with `RTS-pending: Yes`. The ITS in Art. 28(9) (register templates) is also pending.
---
### 1. Articles covered
| Article | Title | Paragraphs | New in v0.2? | T3 clause |
|---|---|---|---|---|
| Art. 28 | General principles | 10 | No (extended) | **C35, C36** |
| Art. 29 | Preliminary assessment of ICT concentration risk at entity level | 2 | **YES** | — (not in T3) |
| Art. 30 | Key contractual provisions | 5 + 1 RTS | No (extended) | **C37, C38** |
**Sequencing note.** T3 carried **C35/C36** for Art. 28 (general principles) and **C37/C38** for Art. 30 (general principles + contracts). v0.2 splits Art. 28 into **5 umbrella cards**, Art. 29 into **2 cards**, and **Art. 30 into 15 cards** (chapeau + 9 sub-elements of 30(2) + 6 sub-elements of 30(3) — the contract-architecture "coração"). Net expansion: ~5.5× for Art. 28-30 combined.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL28-1 | Art. 28 chapeau+(1)+(2) | Umbrella + strategy | **S3** | Integral component of Art. 6 framework; full responsibility; proportionality; multi-vendor strategy; management body review. |
| CL28-2 | Art. 28(3) | Register + reporting | **S3** | Register at entity / sub-consolidated / consolidated levels; yearly reporting; advance notification of planned critical/important arrangements. |
| CL28-3 | Art. 28(4)(a)–(e) | Pre-contractual assessment | **S3** | 5 sub-steps: critical/important identification, supervisory conditions, risk + concentration (Art. 29), due diligence, conflicts of interest. |
| CL28-4 | Art. 28(5)+(6) | Information security + audit | **S3** | `appropriate information security standards`; risk-based audit rights; auditor competence for high-complexity. |
| CL28-5 | Art. 28(7)+(8) | Termination + exit strategies | **S3** | 4 termination grounds; exit strategies for critical/important; tested, documented, transition plans. |
| CL28-6 | Art. 28(9)+(10) | ESAs ITS + RTS | **S2** | ITS on register templates (Art. 28(9)); RTS on policy content (Art. 28(10)). |
| CL29-1 | Art. 29(1) | Concentration-risk preliminary | **S3** | Non-substitutable CTPP OR multiple contracts with same / closely-connected CTPP. |
| CL29-2 | Art. 29(2) | Subcontracting + 3rd-country + insolvency | **S3** | Subcontracting risk weighing; insolvency law; 3rd-country law enforcement; long subcontracting chains. |
| CL30-1 | Art. 30(1) | Written contract + format | **S2** | Contract in one written document; SLAs included; paper or downloadable durable format. |
| CL30-2 | Art. 30(2)(a) | Function description + subcontracting | **S2** | Clear description of functions/ICT services; subcontracting conditions for critical/important. |
| CL30-3 | Art. 30(2)(b) | Locations + change notification | **S2** | Regions/countries of service provision and data processing; advance notification of location changes. |
| CL30-4 | Art. 30(2)(c) | Data CIA provisions | **S3** | Availability, authenticity, integrity, confidentiality; personal data. |
| CL30-5 | Art. 30(2)(d) | Data access / recovery / return | **S3** | Data access, recovery, return in easily accessible format; insolvency/resolution/discontinuation triggers. |
| CL30-6 | Art. 30(2)(e) | Service-level descriptions | **S2** | SLA descriptions including updates/revisions. |
| CL30-7 | Art. 30(2)(f) | Incident assistance cost | **S3** | CTPP assistance at no extra cost OR ex-ante-determined cost for related incidents. |
| CL30-8 | Art. 30(2)(g) | Cooperation with authorities | **S2** | CTPP cooperation with competent + resolution authorities + appointed persons. |
| CL30-9 | Art. 30(2)(h) | Termination + minimum notice | **S3** | Termination rights + minimum notice periods per CA/resolution authority expectations. |
| CL30-10 | Art. 30(2)(i) | Awareness + training | **S2** | CTPP participation in financial-entity awareness + training programmes (Art. 13(6)). |
| CL30-11 | Art. 30(3)(a) | Full SLAs + quantitative | **S3** | Quantitative + qualitative performance targets; effective monitoring; corrective action. |
| CL30-12 | Art. 30(3)(b) | Notice + reporting (material impact) | **S3** | Notice periods + reporting obligations; material-impact threshold. |
| CL30-13 | Art. 30(3)(c) | Contingency + ICT security measures | **S3** | CTPP business contingency plans, testing, ICT security measures, tools, policies. |
| CL30-14 | Art. 30(3)(d) | TLPT cooperation | **S3** | CTPP participation in financial-entity TLPT under Art. 26-27. |
| CL30-15 | Art. 30(3)(e)+(f) | Monitoring rights + exit/transition | **S3** | (3)(e) unrestricted access/inspection/audit (4 sub-points); (3)(f) mandatory adequate transition + migration. |
**Total: 23 atomic clauses** (Art. 28: 6; Art. 29: 2; Art. 30: 15 — including 1 chapeau, 9 sub-elements of 30(2), 4 sub-elements of 30(3)(a)–(d), and the combined (3)(e)+(f) block).
The clause count is **down from 28 in the prior version**. The reduction comes from: (i) consolidating Art. 28 chapeau into 6 umbrella cards (was 9); (ii) merging the 4 sub-points of Art. 30(3)(e) and the 2 sub-points of Art. 30(3)(f) into CL30-15 (the four (e)(i)–(iv) sub-points become a single card body; same for the two (f)(i)–(ii) sub-points). The **15 Art. 30(2)/(3) sub-elements remain separate** per the contract-architecture "coração" directive.
---
### 3. Verbatim OJ text — Art. 28–30
#### 4.1 CL28-1 — Art. 28 chapeau + (1) + (2) — Umbrella principles + strategy
**Source locus:** Art. 28 chapeau, (1)(a)+(b), and (2).
> Financial entities shall manage ICT third-party risk as an integral component of ICT risk within their ICT risk management framework as referred to in Article 6(1) …. shall **at all times, remain fully responsible** …. implemented in light of the **principle of proportionality**, taking into account [nature, scale, complexity, importance] and [risks … criticality or importance] …. shall **adopt, and regularly review**, a **strategy on ICT third-party risk**, taking into account the **multi-vendor strategy** …. include a **policy on the use of ICT services supporting critical or important functions** …. **regularly review the risks identified** ….
**Instance 1 — VAG — S3 — `at all times, remain fully responsible` + `principle of proportionality` (consolidated)**
Two Berry-classic qualifiers in the chapeau + (1)(a)+(b). Three materially distinct readings of the responsibility/proportionality nexus:
- **R1:** Strict (full liability for compliance + Art. 4(2)-proportionality).
- **R2:** Functional (oversight responsibility + entity-defined proportionality).
- **R3:** Hybrid (strict compliance, functional proportionality per Art. 4(2)).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict (full + Art. 4(2)) | In-Directive: literal `fully responsible` + Art. 4(2) reference |
| R2 | Functional (oversight + entity) | None in OJ |
| R3 | Hybrid | In-Directive: literal `at all times` + `principle of proportionality` |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`fully`, `at all times`, `proportionality`).
**Instance 2 — POLY — S2 — `individual and at group level` + `multi-vendor strategy` (consolidated)**
Two scoping qualifiers across (1)(b)(ii) and (2). The group-level assessment scope and the multi-vendor construct are both undefined.
- **R1:** Both individual AND group level; multi-vendor = ≥2 CTPPs per function.
- **R2:** Individual + sub-consolidated/consolidated where relevant; multi-vendor = goal-based (switchable).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict (both levels + ≥2 CTPPs) | In-Directive: literal `and` |
| R2 | Hybrid (where relevant + switchable) | In-Directive: literal `where relevant` + Art. 28(8) exit |
R2 is the literal reading (per `where relevant`). S2.
*Berry anchor:* §5.4.7 (AND); §5.1 (`multi-vendor`).
**Definitional anchor:** DORA Art. 3(18) `ICT third-party risk`; DORA Art. 3(19) `ICT third-party service provider`; DORA Art. 3(22) `critical or important function` (S3 tautology).
**Proportionality-status:** Art. 4 applies (explicit in Art. 28(1)(b) chapeau + limited exception for Art. 16(1) entities and microenterprises in Art. 28(2)).
**RTS-pending:** Art. 28(10) (RTS on policy content; deadline 17 January 2024, passed).
**Scope:** `regulator→financial-entity` (excluding Art. 16(1) first-subparagraph entities and microenterprises for the strategy obligation).
---
#### 4.2 CL28-2 — Art. 28(3) — Register of information + reporting
**Source locus:** Art. 28(3), five sub-paragraphs.
> Financial entities shall **maintain and update** at entity level, and at sub-consolidated and consolidated levels, a **register of information** …. **appropriately documented**, distinguishing between …. report **at least yearly** …. make available to the competent authority …. **inform the competent authority in a timely manner** ….
**Instance 1 — VAG — S3 — `appropriately documented` + `register of information` (consolidated)**
`appropriate` is Berry-classic (same as DORA Art. 25(1) `appropriate tests`, Art. 30(3)(c) `appropriate level of security`). The substantive content of the register is undefined; only its existence is mandated. Three materially distinct readings:
- **R1:** Entity-defined documentation + minimum register content.
- **R2:** Industry-standard documentation + comprehensive register.
- **R3:** Both, per ESAs ITS on standard templates (Art. 28(9), deadline 17 January 2024).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity + minimum | In-Directive: literal `appropriate` |
| R2 | Industry + comprehensive | None in OJ |
| R3 | Both (per ITS) | In-Directive: Art. 28(9) ITS mandate |
R1 vs R2 admit materially distinct compliance populations. R3 will be tightened by ESAs ITS. S3 (R2 tightening pending).
**Instance 2 — VAG — S3 — `inform the competent authority in a timely manner` (planned arrangement notification)**
The advance-notification trigger is undefined. The pre-commencement vs pre-signature distinction is Berry-flagged.
- **R1:** Before signature (advance approval).
- **R2:** After signature but before service commencement (notification only).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Before signature | None in OJ |
| R2 | Before commencement | In-Directive: literal `in a timely manner` + `planned` |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`timely`); §3.3.1 (`planned contractual arrangement`).
**Definitional anchor:** DORA Art. 3(22) `critical or important function` (S3 tautology).
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** Art. 28(9) (ITS on register templates, deadline 17 January 2024, passed; as of mid-2025, the ITS process is in the adoption pipeline).
**Scope:** `regulator→financial-entity` + `financial-entity→competent-authority` (register reporting).
---
#### 4.7 CL29-1 — Art. 29(1) — Concentration-risk preliminary assessment
**Source locus:** Art. 29(1), two sub-points + benefit/cost weighing.
> …. shall also take into account whether …. would lead to any of the following: (a) contracting an ICT third-party service provider that is **not easily substitutable**; or (b) having in place **multiple contractual arrangements** …. with the same ICT third-party service provider or with **closely connected ICT third-party service providers** …. weigh **the benefits and costs of alternative solutions** ….
**Instance 1 — VAG — S3 — `not easily substitutable` + `closely connected ICT third-party service providers`**
`easily` and `closely connected` are both undefined. Three materially distinct readings of the concentration-trigger test:
- **R1:** No equivalent alternative on market; same corporate group (parent-subsidiary).
- **R2:** Lock-in effect (only one CTPP fits technical requirements); joint ventures / partnerships.
- **R3:** Both — any concentration trigger qualifies.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | No alternative + same group | In-Directive: literal `not easily substitutable` |
| R2 | Lock-in + JV | None in OJ |
| R3 | Both | In-Directive: literal `closely connected` (broad) |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`easily`, `closely connected`); §3.3.1 (`substitutable`).
**Instance 2 — VAG — S2 — `weigh the benefits and costs of alternative solutions`**
`weigh` is Berry-flagged vague verb. The weighing methodology is undefined.
- **R1:** Cost-benefit analysis per Art. 4(2) criteria.
- **R2:** Entity judgment (qualitative or multi-criteria).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Art. 4(2)-aligned CBA | In-Directive: Art. 4(2) reference |
| R2 | Entity judgment | In-Directive: literal `weigh` |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`weigh`, `benefits and costs`).
**Definitional anchor:** DORA Art. 3(29) DORA-D29 `ICT concentration risk` (S3 tautology: `a degree of dependency` undefined).
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No (Art. 29 has no RTS mandate; concentration risk is entity-determined).
**Scope:** `regulator→financial-entity` (preliminary concentration assessment only).
---
#### 4.8 CL29-2 — Art. 29(2) — Subcontracting + third-country + insolvency
**Source locus:** Art. 29(2), four sub-paragraphs.
> …. **further subcontracts ICT services supporting a critical or important function** …. weigh **benefits and risks that may arise in connection with such subcontracting**, **in particular in the case of an ICT subcontractor established in a third-country** …. **insolvency law provisions** that would apply …. **the compliance with Union data protection rules and the effective enforcement of the law in that third country** …. **potentially long or complex chains of subcontracting** ….
**Instance 1 — VAG — S3 — `in particular in the case of an ICT subcontractor established in a third-country` + `effective enforcement of the law in that third country` (consolidated)**
The third-country emphasis is rhetorical — `in particular` does not exclude non-third-country subcontracting. `effective enforcement` is undefined. Three materially distinct readings:
- **R1:** All subcontracting subject to weighing; rule-of-law index for enforcement.
- **R2:** Third-country only triggers enhanced assessment; sectoral enforcement (ICT-sector).
- **R3:** Both — base assessment for all subcontracting, enhanced for third-country; both enforcement lenses.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All + rule-of-law | In-Directive: literal `weigh benefits and risks` (general) |
| R2 | Third-country + sectoral | None in OJ |
| R3 | Both | In-Directive: literal `in particular` + `effective enforcement` |
R3 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.4.7 (`in particular`); §5.1 (`effective`); §3.3.1 (`enforcement of the law`).
**Instance 2 — VAG — S3 — `insolvency law provisions` + `potentially long or complex chains of subcontracting` (consolidated)**
The cross-border insolvency assessment and the chain-length threshold are both undefined. Three materially distinct readings:
- **R1:** Identify applicable law + mechanisms (jurisdictional + recovery); strict chain (≥4 tiers).
- **R2:** Identify mechanisms only; any chain with a non-EU node.
- **R3:** Both (identify law + mechanisms); CTPP-disclosed chain-length threshold.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Identify law + ≥4 tiers | In-Directive: literal `insolvency law provisions` |
| R2 | Mechanisms + non-EU node | None in OJ |
| R3 | Both + CTPP-disclosed | In-Directive: literal `potentially long or complex` |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`duly consider`, `potentially long or complex`); §3.3.1 (`insolvency law provisions`, `chains of subcontracting`).
**Definitional anchor:** DORA Art. 3(24) DORA-D24 `ICT third-party service provider established in a third country`; DORA Art. 3(28) `ICT subcontractor established in a third country`.
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No.
**Scope:** `regulator→financial-entity` (assessment obligations before contracting).
---
#### 6.2 Art. 28 umbrella — five governance blocks
Art. 28 is the **management-body-facing umbrella clause**. Its 10 paragraphs split into five operational blocks (mapped to CL28-1 through CL28-5):
| Block | Paragraphs | Function |
|---|---|---|
| Principles + strategy | chapeau + (1) + (2) | Integral component, full responsibility, proportionality, multi-vendor, mgmt body review |
| Register | (3) | Documentation + reporting to CA |
| Pre-contract | (4)(a)–(e) | 5 sub-steps before entering arrangement |
| Security + audit | (5) + (6) | Information security standards + audit + auditor competence |
| Termination + exit | (7) + (8) | 4 termination grounds + exit strategies for critical/important |
| RTS/ITS | (9) + (10) | ESAs standards (templates + policy content) |
Each block is a governance checkpoint. **Art. 28 is the longest single article in DORA** (10 paragraphs) and the most operationally consequential. Block (4) explicitly cross-references **Art. 29** for concentration risk (CL28-3 → CL29-1 / CL29-2).
#### 6.3 Art. 29 — Concentration risk as a regulatory hook
Art. 29 was **newly highlighted in v0.2** (T3 omitted it entirely). It serves three structural purposes:
1. **Cross-reference target from Art. 28(4)(c):** the pre-contract risk assessment must include concentration risk per Art. 29.
2. **Subcontracting + third-country + insolvency vectors:** four sub-paragraphs in Art. 29(2) cover the substantive risks that Art. 28 does not address.
3. **Bridge to Art. 30(3)(f) exit strategies:** concentration risk drives exit-strategy depth (CL30-15 Instance 2).
- **Cross-regulation parallel:** DORA-D29 `ICT concentration risk` is a **standalone definition** (Art. 3(29)), but Art. 29 is the only article operationalising it at entity level. **Art. 33(1)–(2)** is the **ESA-level** concentration-risk analogue (analysed in `05b`).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**T3:** C26 named `patch management`. **OJ:** patches are at Art. 9(4)(f) `have appropriate and comprehensive documented policies for patches and updates`; Art. 13(6) is training (`commensurate to the remit of their functions`), NOT patches. **Gap.** T3 likely mapped C26 to Art. 13(6) due to **incidental overlap** (both deal with security disciplines). **Implication.** v0.2 places patches in CL9-4 Instances 14-15 (Art. 9(4)(f) hinge); Art. 13(6) is analysed in CL13-2 Instance 3 (training). Same structural correction as Q6=a identifies for CRA-CL24.

### from regs/DORA.ambiguity.md

`consistent approach` between DORA reporting and NIS 2 reporting (NIS 2 Art. 23; cf. NIS 2 file §3.10). S3.

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`appropriate`); §3.3.1 (`register`). Same as CRA-CL129.

<!-- aegis:purity: own_reg=DORA; demoted=3; core_cross_mentions=0 -->

