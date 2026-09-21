# D-03.3 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
## DORA v0.2 — Chapter II Section I + Art. 4: Governance and Proportionality (Art. 4–6)
> **Source.** OJ L 333, 27.12.2022, p. 29–32. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **1635–1789**.
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending`, `scope`.
>
> **Why these three articles together (umbrella file `02a`).** Art. 4 is in Ch. I (General Provisions) but the proportionality principle it establishes **propagates to every clause in Ch. II–V Sec. I**. Art. 5 (governance) and Art. 6 (framework chapeau) are the structural anchors to which Art. 4 attaches. Grouping them in `02a` lets the reader see the **proportionality overlay + management-body liability + framework chapeau** as a single conceptual block. The remaining 10 articles of Ch. II Sec. II (Art. 7–16, the operational risk-management provisions) are analysed in `02b_DORA_Ch2Sec2_Framework.md`.
>
> **Articles in this file:** 3 articles, 17 paragraphs (Art. 4: 3; Art. 5: 4 + 9 sub-points; Art. 6: 10 + 8 sub-points), 13 atomic clauses (CL4-1 … CL6-5).
---
### 1. Articles covered
| Article | Title | Paragraphs | T3 clause | New in v0.2? |
|---|---|---|---|---|
| Art. 4 | Proportionality principle | 3 | **C01** (proportionality) | No (extended — T3 had a single clause; v0.2 has 3) |
| Art. 5 | Governance and organisation | 4 + 9 sub-points (a)–(i) | **C02** (governance), **C03** (management body), **C04** (board training) | No (extended — T3 had 3 clauses; v0.2 has 5) |
| Art. 6 | ICT risk management framework (chapeau) | 10 + 8 sub-points (a)–(h) | **C05** (framework chapeau), **C06** (control function), **C07** (audit), **C08** (resilience strategy) | No (extended — T3 had 4 clauses; v0.2 has 5) |
**Note on Art. 4 (Proportionality):** the three paragraphs of Art. 4 attach proportionality to (i) Ch. II as the default; (ii) Ch. III, IV, V Sec. I by specific reference; (iii) competent-authority review under Art. 6(5) and Art. 16(2). Each clause card in the rest of v0.2 carries a `proportionality-status: Art. 4 applies` flag (per pilot convention).
**Note on RTS-pending:** no RTS mandate in this article range. Art. 15 (RTS mandate to ESAs on Art. 9–11 elements) is meta-procedural; the substantive impact lives in Art. 9–11, not in this file. The Art. 4 proportionality principle is **self-implementing** — no RTS/ITS specifies the criteria.
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL4-1 | Art. 4(1) | Proportionality chapeau (Ch. II) | **S3** | Implement Ch. II per proportionality (size, risk profile, nature/scale/complexity). |
| CL4-2 | Art. 4(2) | Proportionality propagation (Ch. III, IV, V Sec. I) | **S3** | Application proportionate to size/risk/nature/scale/complexity. |
| CL4-3 | Art. 4(3) | CA review of proportionality | **S2** | Competent authorities consider proportionality in framework review. |
| CL5-1 | Art. 5(1) | Internal governance and control framework chapeau | **S3** | Internal governance framework ensuring effective and prudent ICT risk management. |
| CL5-2 | Art. 5(2) chapeau | Management body 4-verb coordination | **S3** | Management body: `define, approve, oversee and be responsible for` ICT risk management framework. |
| CL5-3 | Art. 5(2)(a)–(d) | Management body sub-points (responsibility + standards + roles + strategy) | **S3** | Ultimate responsibility; high standards (availability, authenticity, integrity, confidentiality); clear roles; digital operational resilience strategy + risk tolerance. |
| CL5-4 | Art. 5(2)(e)–(i) | Management body sub-points (continuity + audit + budget + ICT-TPP + reporting) | **S3** | ICT business continuity; ICT internal audit plans; budget; ICT-TPP policy; reporting channels. |
| CL5-5 | Art. 5(3)+(4) | Designation + training | **S3** | Designate monitoring role (other than microenterprises); management body training. |
| CL6-1 | Art. 6(1) chapeau | Framework chapeau | **S3** | `Sound, comprehensive and well-documented` ICT risk management framework. |
| CL6-2 | Art. 6(2)+(3) | Framework content + minimise impact | **S3** | Strategies, policies, procedures, ICT protocols, tools; minimise impact; CA info. |
| CL6-3 | Art. 6(4)+(6) | Independence + 3 lines of defence + internal audit | **S3** | Control function independence; three lines of defence; internal audit by auditors with ICT expertise. |
| CL6-4 | Art. 6(5)+(7) | Documentation + review + follow-up | **S3** | Documented and reviewed at least yearly (or periodically for microenterprises); major-incident triggers; formal follow-up. |
| CL6-5 | Art. 6(8)+(9)+(10) | Digital operational resilience strategy + multi-vendor + outsourcing | **S3** | 8-point strategy; optional multi-vendor strategy; outsourcing of compliance verification. |
**Total: 13 atomic clauses (Art. 4: 3; Art. 5: 5; Art. 6: 5).**
---
### 3. Verbatim OJ text — Art. 4–6
#### 6.1 Art. 4 propagation pattern — three distinct proportionality regimes
Art. 4 establishes **three distinct proportionality regimes** that operate simultaneously:
- **Art. 4(1) — Ch. II proportionality** (CL4-1): default for the ICT risk management framework.
- **Art. 4(2) — Ch. III, IV, V Sec. I proportionality** (CL4-2): default for incident reporting, testing, and third-party risk.
- **Art. 4(3) — CA-review proportionality** (CL4-3): meta-provision requiring CAs to consider proportionality when reviewing the framework.
The three regimes are **not symmetric**: Art. 4(1) is self-implementing (the entity applies it directly); Art. 4(2) defers to chapter-specific clauses (Art. 16 simplification, Art. 25(3) microenterprise exception); Art. 4(3) is addressed to CAs.
- **Berry anchor:** §3.3.1 (`principle of proportionality`); §5.1 (`proportionate`).
- **Structural implication:** the proportionality overlay is **inherited by every Ch. II–V Sec. I clause** in v0.2. Every clause card in `02b`–`05a` carries `proportionality-status: Art. 4 applies`. The v0.2 convention was established in the pilot file (`01_DORA_Art3_Definitions.md` §2 note on Art. 4).
#### 6.3 Art. 6 chapeau — the framework's three-attribute triad
Art. 6(1) opens with `sound, comprehensive and well-documented` (three attributes, AND). This is the **framework-level analog** of:
- **Art. 24(1) `sound and comprehensive`** (testing programme, two attributes; CL24-1)
- **Berry anchor:** §5.1 (`sound`, `comprehensive`, `well-documented`); §5.4.7 (AND); §5.5 (parallelism).
- **Structural implication:** the framework's three attributes set the bar for every Ch. II–V Sec. I clause. Any clause that fails one of the three (e.g. a framework that is `comprehensive and well-documented` but not `sound`) would be non-compliant.
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

**Note on definitional anchors:** every ICT-related clause in this file inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; Art. 3(5) `ICT risk`; Art. 3(30) `management body` (composite cross-reference, see pilot file §2.10). The Art. 3(22) `critical or important function` (S3 tautology, see pilot file §2.7) propagates to Art. 6(8)(f).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** Art. 4's proportionality pattern mirrors **NIS 2 Art. 1(2)** (proportionality in scope) and **CRA Art. 1(2)** (proportionality for microenterprises and SMEs). DORA Art. 4 is more elaborate than either, providing explicit CA-review (CL4-3) that NIS 2 and CRA do not have.


### from regs/DORA.ambiguity.md

- **CRA Annex I Part I §1 chapeau** `products with digital elements shall be designed, developed and produced …` (manufacturing lifecycle, three verbs; CRA-CL14)

### from regs/DORA.ambiguity.md

- **NIS 2 Art. 21(1) `appropriate and proportionate technical, operational and organisational measures`** (measures chapeau)


### from regs/DORA.ambiguity.md

The 3-attribute triad (`sound, comprehensive and well-documented`) is **the most demanding framework chapeau in the 5-regulation corpus** — it requires three distinct qualities (effectiveness, completeness, traceability). CRA Annex I Part I §1 has three verbs (design, develop, produce) but they describe **processes** not qualities. DORA's triad describes **qualities of an artifact** (the framework itself), which is a different kind of obligation.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the triad is the most explicit framework-quality specification in the corpus. NIS 2 Art. 21(1) uses `appropriate and proportionate` (2 qualifiers); CRA Annex I Part I uses process verbs; GDPR Art. 24 uses `appropriate` (1 qualifier). DORA's 3-attribute triad is the most demanding.


### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`appropriate`); §3.3.1 (`register`). Same as CRA-CL129.

<!-- aegis:purity: own_reg=DORA; demoted=7; core_cross_mentions=0 -->

