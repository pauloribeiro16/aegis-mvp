# D-01.1 — Relevant Ambiguity (DORA)

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
#### 4.1 CL4-1 — Art. 4(1) — Proportionality chapeau (Ch. II)
**Source locus:** Art. 4(1).
> Financial entities shall implement the rules laid down in Chapter II in accordance with the principle of proportionality, taking into account their size and overall risk profile, and the nature, scale and complexity of their services, activities and operations.
**Instance 1 — VAG — S3 — `principle of proportionality`**
The proportionality principle is a **general principle of EU law** (case-law-laden: Cassis de Dijon, Lange, Schwarz, etc.) but Art. 4(1) makes it the **specific override for Ch. II implementation**. Three materially distinct readings:
- **R1:** Quantitative (proportional to size: headcount, balance-sheet total, turnover).
- **R2:** Risk-based (proportional to the ICT risk profile of the entity).
- **R3:** Combined: size, risk profile, AND nature/scale/complexity (literal reading).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative (size) | None in OJ |
| R2 | Risk-based | In-Directive: literal `overall risk profile` |
| R3 | Combined (size + risk + nature/scale/complexity) | In-Directive: literal `taking into account their size and overall risk profile, and the nature, scale and complexity` |
R1 vs R3 admit materially distinct compliance populations (R1: small entity is automatically exempted; R3: a small entity with high risk profile may still need to comply fully). S3.
*Berry anchor:* §5.1 (`proportionality`); §3.3.1 (`principle of proportionality`).
**Instance 2 — VAG — S3 — `nature, scale and complexity`**
The three-factor qualifier. Each term admits its own ambiguity.
| Sub-factor | Key ambiguity | Berry anchor |
|---|---|---|
| `nature` | Sectoral (banking vs. insurance vs. asset management) vs. operational (online vs. branch) | §3.3.1 (`nature`) |
| `scale` | Volume of operations, number of clients, geographic spread | §3.3.1 (`scale`) |
| `complexity` | Organisational (group structure) vs. technical (legacy systems, multi-vendor) | §3.3.1 (`complexity`) |
S3 (the three sub-factors are not formally weighted; an entity may emphasise one over another).
*Berry anchor:* §3.3.1 (`nature, scale and complexity`).
---
#### 4.4 CL5-1 — Art. 5(1) — Internal governance and control framework chapeau
**Source locus:** Art. 5(1).
> Financial entities shall have in place an **internal governance and control framework** that ensures an **effective and prudent** management of ICT risk, in accordance with Article 6(4), in order to achieve a high level of digital operational resilience.
**Instance 1 — VAG — S3 — `internal governance and control framework`**
The framework chapeau. Three materially distinct readings:
- **R1:** Three lines of defence model (per Art. 6(4) cross-reference).
- **R2:** Two lines of defence (business + control, common in some Member States).
- **R3:** Composite: any recognised internal-control model.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three lines of defence | In-Directive: Art. 6(4) `according to the three lines of defence model` |
| R2 | Two lines of defence | None in OJ |
| R3 | Any model | In-Directive: Art. 6(4) `or an internal risk management and control model` |
R3 is the literal reading (Art. 6(4) gives the option). S3 (the choice between R1 and R3 yields materially distinct control populations).
*Berry anchor:* §3.3.1 (`governance and control framework`); §5.4.7 (AND/OR structure).
**Instance 2 — VAG — S3 — `effective and prudent`**
Two vague qualifiers (AND). Both are Berry classics.
- **R1:** Effective (outcome-based) AND prudent (process-based, conservative).
- **R2:** Hendiadys (single concept: risk-management discipline).
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct qualifiers | In-Directive: literal `and` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations (R1 requires both outcome and process; R3 allows either). S3.
**Instance 3 — POLY — S2 — `a high level of digital operational resilience`**
The target standard. Inherits DORA-D01 `digital operational resilience` (S3 `build, assure and review`).
- **R1:** All three lifecycle phases per R1 of DORA-D01.
- **R2:** Continuous process per R2 of DORA-D01.
- **R3:** All three control families per R3 of DORA-D01.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Lifecycle phases | In-Directive: DORA-D01 |
| R2 | Continuous process | In-Directive: DORA-D01 |
| R3 | Control families | In-Directive: DORA-D01 |
S2 (the target is propagated from the definition).
*Berry anchor:* §3.3.1 (`high level`); §3.3.1 (`digital operational resilience`).
**Definitional anchor:** DORA Art. 3(1) `digital operational resilience` (DORA-D01); DORA Art. 3(5) `ICT risk` (DORA-D05).
**Proportionality-status:** Art. 4 applies.
**Scope:** financial entity.
---
#### 4.9 CL6-1 — Art. 6(1) chapeau — Framework chapeau
**Source locus:** Art. 6(1).
> Financial entities shall have a **sound, comprehensive and well-documented ICT risk management framework** as part of their overall risk management system, which enables them to **address ICT risk quickly, efficiently and comprehensively** and to ensure a high level of digital operational resilience.
**Instance 1 — VAG — S3 — `sound, comprehensive and well-documented` (three-verb coordination)**
The three qualifiers (AND) of the framework. Three materially distinct readings:
- **R1:** Three discrete attributes (sound = effective, comprehensive = complete, well-documented = traceable).
- **R2:** Hendiadys-like (one quality with three reinforcing labels).
- **R3:** All three required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Three discrete | In-Directive: literal `sound, comprehensive and well-documented` |
| R2 | Hendiadys | None in OJ |
| R3 | All three | In-Directive: literal `and` |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations (R1: each quality can be tested independently; R3: one composite quality suffices). S3.
*Berry anchor:* §5.1 (`sound`, `comprehensive`); §5.4.7 (AND); §5.5 (parallelism); cf. CL24-1 `sound and comprehensive` (testing programme, same pattern).
**Instance 2 — VAG — S3 — `address ICT risk quickly, efficiently and comprehensively` (three-verb coordination of the framework's purpose)**
The 3-verb coordination on the framework's purpose. Three materially distinct readings:
- **R1:** Three distinct operational qualities (speed, resource-efficiency, completeness).
- **R2:** Hendiadys.
- **R3:** All three required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal `quickly, efficiently and comprehensively` |
| R2 | Hendiadys | None in OJ |
| R3 | All three | In-Directive: literal `and` |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`quickly`, `efficiently`, `comprehensively`); §5.4.7 (AND); §5.5 (parallelism).
**Instance 3 — POLY — S2 — `part of their overall risk management system`**
The framework's position within the broader risk-management architecture. The integration is **mandatory** (the framework is part of the system, not parallel to it). Two readings:
- **R1:** Embedded (the ICT framework is a sub-component of the overall risk-management system).
- **R2:** Coordinated (the ICT framework is parallel but coordinated).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Embedded | In-Directive: literal `part of` |
| R2 | Coordinated | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`part of`).
**Definitional anchor:** DORA Art. 3(5) `ICT risk` (DORA-D05); DORA Art. 3(1) `digital operational resilience` (DORA-D01).
**Proportionality-status:** Art. 4 applies (the chapeau is the primary propagation point).
**Scope:** financial entity.
---
#### 4.10 CL6-2 — Art. 6(2)+(3) — Framework content + minimise impact
**Source locus:** Art. 6(2) and 6(3).
> 2. The ICT risk management framework shall include at least **strategies, policies, procedures, ICT protocols and tools** that are necessary to **duly and adequately** protect all information assets and ICT assets, including computer software, hardware, servers, as well as to protect all relevant physical components and infrastructures, such as premises, data centres and sensitive designated areas, to ensure that all information assets and ICT assets are adequately protected from risks including damage and unauthorised access or usage.
>
> 3. In accordance with their ICT risk management framework, financial entities shall **minimise the impact of ICT risk** by deploying appropriate strategies, policies, procedures, ICT protocols and tools. They shall provide **complete and updated information on ICT risk and on their ICT risk management framework** to the competent authorities upon their request.
**Instance 1 — POLY — S3 — `strategies, policies, procedures, ICT protocols and tools` (5-category enumeration)**
The framework's content categories. The list is **open** (`at least`). Three readings:
- **R1:** Closed (the 5 are exhaustive; the framework must contain all of them).
- **R2:** Open (the 5 are a floor; additional categories may be added).
- **R3:** Compound (the 5 are illustrative; the framework must contain all 5 but may add more).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed | None in OJ |
| R2 | Open | In-Directive: literal `at least` |
| R3 | Floor | None in OJ |
R2 is the literal reading. S3 (R1 vs R2 admit materially distinct compliance populations: R1 excludes, e.g., a dedicated `standards` category as mandatory; R2 requires it but allows additions).
*Berry anchor:* §5.1 (`at least`); §3.3.1 (`strategies`, `policies`, `procedures`, `protocols`, `tools`).
**Instance 2 — VAG — S3 — `duly and adequately` (compound hedge)**
The compound adverb. Three readings:
- **R1:** `duly` = in accordance with applicable rules; `adequately` = sufficient for the purpose.
- **R2:** Hendiadys.
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal `duly and adequately` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S3.
**Instance 3 — POLY — S2 — `information assets and ICT assets` (AND)**
Two asset categories. S2 (both categories must be protected). The `and` is conjunctive.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`information assets` (DORA-D06), `ICT assets` (DORA-D07)).
**Instance 4 — POLY — S2 — `physical components and infrastructures, such as premises, data centres and sensitive designated areas` (sub-clause)**
The physical-asset scope. The `such as` is open-list. Three materially distinct readings:
- **R1:** Premises only.
- **R2:** Premises + data centres.
- **R3:** Any physical location (open list).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Premises | None in OJ |
| R2 | Premises + DC | None in OJ |
| R3 | Any | In-Directive: literal `such as` (open list) |
R3 is the literal reading. S2.
*Berry anchor:* §5.1 (`such as`); §3.3.1 (`physical components`, `premises`, `data centres`).
**Instance 5 — VAG — S3 — `minimise the impact of ICT risk` (Art. 6(3))**
`minimise` is Berry-flagged (the `as low as reasonably practicable` cousin). Three readings:
- **R1:** Absolute minimum (zero impact is the target).
- **R2:** Reasonable minimum (per ALARP / cost-benefit).
- **R3:** Reduction to acceptable level (per risk tolerance).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Absolute | None in OJ |
| R2 | Reasonable | None in OJ |
| R3 | Acceptable | In-Directive: Art. 6(8)(b) `risk tolerance level` |
R3 is the literal reading (Art. 6(8)(b) cross-reference). S3.
*Berry anchor:* §3.3.1 (`minimise`); §3.3.1 (`impact`).
**Instance 6 — VAG — S2 — `complete and updated information on ICT risk` (Art. 6(3))**
The CA-reporting obligation. Two vague qualifiers (AND):
- **R1:** `complete` = exhaustive coverage of all risks; `updated` = current as of report date.
- **R2:** Hendiadys.
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct | In-Directive: literal `complete and updated` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`complete`, `updated`); §5.4.7 (AND).
**Definitional anchor:** DORA Art. 3(5) `ICT risk` (DORA-D05); DORA Art. 3(6) `information asset` (DORA-D06); DORA Art. 3(7) `ICT asset` (DORA-D07).
**Proportionality-status:** Art. 4 applies.
**Scope:** financial entity (Art. 6(2)); financial entity → competent authority (Art. 6(3) reporting).
---
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
#### 4.6 CL25-1 — Art. 25(1) — Open-list test modalities
**Source locus:** Art. 25(1).
> The digital operational resilience testing programme referred to in Article 24 shall provide, in accordance with the criteria set out in Article 4(2), for the execution of **appropriate tests, such as vulnerability assessments and scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires and scanning software solutions, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing**.
**Instance 1 — POLY — S3 — `appropriate tests, such as …` (open list of 12 modalities)**
The list is **explicitly open** (`such as …`) but enumerates 12 specific modalities. Three readings of how to treat the list:
- **R1:** Closed list (the 12 are exhaustive; financial entities must conduct all of them).
- **R2:** Open list (the 12 are illustrative; entities must choose from these or add others).
- **R3:** Open list with 12-floor (entities must conduct at least these 12).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed list | None in OJ |
| R2 | Open list | In-Directive: literal `such as` (Berry §5.1 open-list signal) |
| R3 | Open with floor | None in OJ |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R1: entity conducts only the 12; R2: entity adds modalities e.g. red team, social engineering, fuzz testing). S3.
**Instance 2 — POLY — S2 — 12 individual modalities**
Each modality admits internal ambiguity (e.g. `vulnerability assessments and scans` could mean automated-only, manual-only, or hybrid; `penetration testing` could be black-box, grey-box, or white-box).
| Modality | Key ambiguity | Berry anchor |
|---|---|---|
| `vulnerability assessments and scans` | Automated vs. manual scope | §3.3.1 (`assessments`) |
| `open source analyses` | OSS code review vs. OSS dependency analysis | §3.3.1 (`open source`) |
| `network security assessments` | External vs. internal network | §3.3.1 (`network`) |
| `gap analyses` | Compliance-gap vs. capability-gap | §3.3.1 (`gap`) |
| `physical security reviews` | Premises-only vs. hardware-inclusive | §3.3.1 (`physical security`) |
| `questionnaires and scanning software solutions` | Self-assessment vs. auditor-driven | §3.3.1 (`questionnaires`) |
| `source code reviews where feasible` | `feasible` undefined; static vs. dynamic | §5.1 (`feasible`) |
| `scenario-based tests` | Adversary-emulation vs. failure-mode | §3.3.1 (`scenario`) |
| `compatibility testing` | Interoperability vs. backward-compat | §3.3.1 (`compatibility`) |
| `performance testing` | Load vs. stress vs. soak | §3.3.1 (`performance`) |
| `end-to-end testing` | Business-process vs. data-flow | §3.3.1 (`end-to-end`) |
| `penetration testing` | Black-box vs. grey-box vs. white-box | §3.3.1 (`penetration`) |
Each row is S2 on its own (the modality is recognised; the specific implementation is open). The aggregate is the open-list pattern at S3.
---
#### 4.7 CL25-2 — Art. 25(2) — CSD/CCP pre-deployment vulnerability assessments
**Source locus:** Art. 25(2).
> Central securities depositories and central counterparties shall perform vulnerability assessments **before any deployment or redeployment of new or existing applications and infrastructure components, and ICT services supporting critical or important functions** of the financial entity.
**Instance 1 — POLY — S2 — `deployment or redeployment`**
`deployment` vs. `redeployment`:
- **R1:** Strict: redeployment = re-installation of existing component.
- **R2:** Broad: redeployment = any configuration change to a previously deployed component.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Strict (reinstall) | None in OJ |
| R2 | Broad (config change) | In-Directive: literal `redeployment` (broad) |
| R3 | Either | In-Directive: literal `or` |
R2 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`deployment`, `redeployment`).
**Instance 2 — COORD — S2 — `new or existing applications and infrastructure components, and ICT services`**
Three categories (OR) coordinated. Compound scope:
- **R1:** Each category tested separately.
- **R2:** Compound scope: any combination tested.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Separate | None in OJ |
| R2 | Compound | In-Directive: literal `or` |
R2 is the literal reading. S2.
*Berry anchor:* §5.4.7 (multi-way OR).
---
#### 6.1 Art. 25(1) — 12-modality open list (POLY/S3)
- **Structural implication:** the 12 modalities are illustrative, not exhaustive. Financial entities may add (e.g. red team, social engineering, fuzz testing) but should not omit any of the 12 without justification.
#### 6.5 Art. 25(2) — Sectoral carve-out for CSD/CCP
Art. 25(2) imposes a **pre-deployment vulnerability assessment obligation on two specific entity types** (CSDs and CCPs). This is a sectoral carve-out unique in Ch. IV — no other clause names specific entity types.
- **Berry anchor:** §3.3.1 (`central securities depositories`, `central counterparties`).
- **Structural implication:** CSDs and CCPs are **financial market infrastructures (FMIs)** with systemic importance. The pre-deployment assessment obligation reflects the FMI-specific risk profile (a deployment-induced vulnerability could cascade to the entire clearing or settlement system).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in this file inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; Art. 3(5) `ICT risk`; Art. 3(30) `management body` (composite cross-reference, see pilot file §2.10). The Art. 3(22) `critical or important function` (S3 tautology, see pilot file §2.7) propagates to Art. 6(8)(f).

### from regs/DORA.ambiguity.md

**Proportionality-status:** **THIS IS ART. 4** — the clause is the proportionality chapeau.
**Scope:** financial entity.
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system` (Ch. II is ICT-risk-management chapter).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`effective`, `prudent`); §5.4.7 (AND); cf. CRA-CL27 `handled effectively` (same pattern).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`duly`, `adequately`); §5.4.7 (AND); cf. CRA-CL46 `immediately take` (hendiadys classic).

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

*Berry anchor:* §5.1 (`such as`); cf. CRA-C05 (Annex I Part I §2(d) `including but not limited to`).

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D17 `TLPT` (for the penetration-testing sub-modality when elevated to TLPT, see CL26-*).
**Proportionality-status:** Art. 4 applies.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA-D22 `critical or important function` (S3 tautology).
**Proportionality-status:** Art. 4 applies (with sectoral specificity: only CSDs and CCPs, two specific entity types).

### from regs/DORA.ambiguity.md

Art. 25(1) enumerates 12 specific test modalities under the `such as …` open-list signal. The structural pattern is **identical to CRA Annex I Part I §2(d)** (`authentication, identity or access management systems` under `including but not limited to`) and to the CRA Annex I enumeration generally.

### from regs/DORA.ambiguity.md

- **Berry anchor:** §5.1 `such as` open-list marker; same pattern as CRA-C05 (Annex I Part I §2(d)).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** CRA, NIS 2 (Art. 21(2)(e) `secure system development and maintenance` includes similar open enumerations), and DORA all converge on the open-list pattern. This is a **regulatory-drafting convention**, not an artefact of any single regulation.


### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** CRA does not impose pre-deployment obligations. NIS 2 Art. 21(2)(f) requires `policies and procedures for cryptography` but not pre-deployment assessments. **DORA Art. 25(2) is a sectoral specificity.**


<!-- aegis:purity: own_reg=DORA; demoted=16; core_cross_mentions=0 -->