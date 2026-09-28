# D-06.3 — Relevant Ambiguity (DORA)

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
#### 6.1 Art. 4 propagation pattern — three distinct proportionality regimes
Art. 4 establishes **three distinct proportionality regimes** that operate simultaneously:
- **Art. 4(1) — Ch. II proportionality** (CL4-1): default for the ICT risk management framework.
- **Art. 4(2) — Ch. III, IV, V Sec. I proportionality** (CL4-2): default for incident reporting, testing, and third-party risk.
- **Art. 4(3) — CA-review proportionality** (CL4-3): meta-provision requiring CAs to consider proportionality when reviewing the framework.
The three regimes are **not symmetric**: Art. 4(1) is self-implementing (the entity applies it directly); Art. 4(2) defers to chapter-specific clauses (Art. 16 simplification, Art. 25(3) microenterprise exception); Art. 4(3) is addressed to CAs.
- **Berry anchor:** §3.3.1 (`principle of proportionality`); §5.1 (`proportionate`).
- **Structural implication:** the proportionality overlay is **inherited by every Ch. II–V Sec. I clause** in v0.2. Every clause card in `02b`–`05a` carries `proportionality-status: Art. 4 applies`. The v0.2 convention was established in the pilot file (`01_DORA_Art3_Definitions.md` §2 note on Art. 4).
#### 4.18 CL19-1 — Art. 19(1) — Major incident reporting (single-CA designation; significant CIs → ECB)
**Source locus:** Art. 19(1).
> Financial entities shall report major ICT-related incidents to the **relevant competent authority** as referred to in Article 46 in accordance with paragraph 4 of this Article.
>
> Where a financial entity is subject to supervision by more than one national competent authority referred to in Article 46, Member States shall designate a **single competent authority** as the relevant competent authority responsible for carrying out the functions and duties provided for in this Article.
>
> **Credit institutions classified as significant**, in accordance with Article 6(4) of Regulation (EU) No 1024/2013, shall report major ICT-related incidents to the **relevant national competent authority designated in accordance with Article 4 of Directive 2013/36/EU**, which shall **immediately transmit that report to the ECB**.
>
> For the purpose of the first subparagraph, financial entities shall produce, after collecting and analysing all relevant information, the initial notification and reports referred to in paragraph 4 of this Article using the templates referred to in Article 20 and submit them to the competent authority. In the event that a technical impossibility prevents the submission of the initial notification using the template, financial entities shall notify the competent authority about it via alternative means.
>
> The initial notification and reports referred to in paragraph 4 shall include all information necessary for the competent authority to determine the significance of the major ICT-related incident and assess possible cross-border impacts.
>
> Without prejudice to the reporting pursuant to the first subparagraph by the financial entity to the relevant competent authority, Member States may additionally determine that some or all financial entities shall also provide the initial notification and each report referred to in paragraph 4 of this Article using the templates referred to in Article 20 to the competent authorities or the computer security incident response teams (CSIRTs) designated or established in accordance with Directive (EU) 2022/2555.
**Instance 1 — POLY — S3 — `relevant competent authority`**
`relevant` is undefined. Three readings:
- **R1:** The CA designated by the Member State per Art. 46.
- **R2:** The CA specific to the entity's sector (e.g. NCA for credit institutions; NCA for insurers).
- **R3:** The single CA designated in accordance with paragraph 1 sub-2 (for entities subject to multi-CA supervision).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per Art. 46 | In-Directive: Art. 46 cross-reference |
| R2 | Sector-specific | None in OJ |
| R3 | Single-CA designation | In-Directive: paragraph 1 sub-2 |
R1 is the literal reading. R3 is the operational reading for multi-CA entities. S3.
*Berry anchor:* §5.1 (`relevant`); §3.3.1 (`competent authority`).
**Instance 2 — POLY — S2 — `Credit institutions classified as significant`**
Inherits Art. 6(4) Reg. (EU) No 1024/2013 (SSM Regulation). S2 (the classification is shared with the SSM prudential supervision framework).
*Berry anchor:* §3.3.1 (`classified as significant`).
**Instance 3 — VAG — S2 — `immediately transmit`**
`immediately` stronger than `without undue delay` but still Berry S2 (operational practice converges on continuous transmission). S2.
*Berry anchor:* §5.1 (`immediately`); §5.7 (temporal operator).
**Instance 4 — POLY — S3 — `technical impossibility`**
The fallback trigger is undefined.
- **R1:** Persistent (e.g. template-system outage).
- **R2:** Transient (e.g. network failure).
- **R3:** Documented (e.g. CA-side outage).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Persistent | None in OJ |
| R2 | Transient | None in OJ |
| R3 | Documented | None in OJ |
S3.
*Berry anchor:* §3.3.1 (`technical impossibility`).
**Instance 5 — POLY — S2 — `alternative means`**
`alternative` undefined. S2 (means could be email, phone, encrypted channel).
*Berry anchor:* §3.3.1 (`alternative means`).
**Instance 6 — VAG — S2 — `all information necessary for the competent authority to determine the significance of the major ICT-related incident and assess possible cross-border impacts`**
*Berry anchor:* §5.1 (`all information necessary`); §3.3.1 (`significance`, `cross-border impacts`).
**Definitional anchor:** DORA-D10 `major ICT-related incident` (S3 regress).
**RTS-pending:** Art. 18(3)(a) (the `major` threshold); Art. 20 (templates per para. 1 sub-3).
**Scope:** regulator→financial-entity.
**Proportionality-status:** Art. 4 applies.
---
#### 4.19 CL19-2 — Art. 19(2) — Voluntary significant cyber threat notification
**Source locus:** Art. 19(2).
> Financial entities may, on a voluntary basis, notify **significant cyber threats** to the relevant competent authority when **they deem the threat to be of relevance to the financial system, service users or clients**. The relevant competent authority may provide such information to other relevant authorities referred to in paragraph 6.
>
> Credit institutions classified as significant, in accordance with Article 6(4) of Regulation (EU) No 1024/2013, may, on a voluntary basis, notify significant cyber threats to relevant national competent authority, designated in accordance with Article 4 of Directive 2013/36/EU, which shall immediately transmit the notification to the ECB.
>
> Member States may determine that those financial entities that on a voluntary basis notify in accordance with the first subparagraph may also transmit that notification to the CSIRTs designated or established in accordance with Directive (EU) 2022/2555.
**Instance 1 — POLY — S3 — `they deem the threat to be of relevance to the financial system, service users or clients`**
Three relevance anchors (OR). Combination rule undefined: any one suffices, or all three required?
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any one (OR) | In-Directive: literal `or` |
| R2 | All three (AND) | None in OJ |
| R3 | Entity judgment | In-Directive: literal `they deem` |
R3 (entity judgment) is the operative reading; R1 is the literal reading. R1 vs R2 admit materially distinct notification populations. S3.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`relevance`, `deem`).
**Instance 2 — POLY — S2 — `may, on a voluntary basis`**
Discretionary obligation. S2 (the `may` is the operative trigger; entity judgment applies).
*Berry anchor:* §3.3.1 (`may`, `voluntary basis`); §5.1 (`may`).
**Definitional anchor:** DORA Art. 3(13) `significant cyber threat` (DORA-D13, S3).
**RTS-pending:** Art. 18(3)(c) (significance thresholds); Art. 20(a)(iii) (notification content).
**Proportionality-status:** Art. 4 applies.
---
#### 4.20 CL19-3 — Art. 19(3) — Client notification
**Source locus:** Art. 19(3).
> Where a major ICT-related incident occurs and **has an impact on the financial interests of clients**, financial entities shall, **without undue delay as soon as they become aware of it**, inform their clients about the major ICT-related incident and about the **measures that have been taken to mitigate the adverse effects** of such incident.
>
> In the case of a significant cyber threat, financial entities shall, where applicable, inform their clients that are **potentially affected** of any **appropriate protection measures** which the latter may consider taking.
**Instance 1 — VAG — S3 — `without undue delay as soon as they become aware of it`**
- **R1:** `without undue delay` is the primary trigger; `as soon as they become aware` is the clock-start.
- **R2:** `as soon as they become aware` is the primary trigger; `without undue delay` is the response standard.
- **R3:** Both independent.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Primary + clock | In-Directive: literal |
| R2 | Clock + standard | None in OJ |
| R3 | Independent | None in OJ |
R1 is the dominant reading. S3.
**Instance 2 — SCOPE-Q + POLY — S3 — `becoming aware of`**
*Berry anchor:* §3.3.1 (`becoming aware`).
**Instance 3 — VAG — S3 — `impact on the financial interests of clients`**
`financial interests` undefined. Three readings:
- **R1:** Direct monetary loss (e.g. funds misdirected, fees overcharged).
- **R2:** Indirect monetary impact (e.g. service unavailability causing business disruption).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Direct | None in OJ |
| R2 | Indirect | None in OJ |
| R3 | Either | In-Directive: literal `financial interests` (broad) |
S3.
*Berry anchor:* §3.3.1 (`financial interests`).
**Instance 4 — VAG — S2 — `measures that have been taken to mitigate the adverse effects`**
Two layered Berry terms (`measures` + `mitigate` + `adverse effects`). S2.
*Berry anchor:* §5.1 (`measures`, `mitigate`); §3.3.1 (`adverse effects`).
**Instance 5 — POLY — S2 — `where applicable` (cyber-threat sub-paragraph)**
Soft hedge on informing clients about a potential (not yet actualised) threat. S2.
*Berry anchor:* §5.1 (`where applicable`).
**Instance 6 — POLY — S2 — `potentially affected` (cyber-threat sub-paragraph)**
*Berry anchor:* §3.3.1 (`potentially affected`).
**Definitional anchor:** DORA-D10 `major ICT-related incident` (S3 regress); DORA-D13 `significant cyber threat`.
**RTS-pending:** Art. 18(3)(a); Art. 18(3)(c).
**Scope:** regulator→financial-entity→client (notification chain to clients).
**Proportionality-status:** Art. 4 applies.
---
#### 4.22 CL19-5 — Art. 19(5) — Outsourcing of reporting
**Source locus:** Art. 19(5).
> Financial entities may outsource, in accordance with Union and national sectoral law, the reporting obligations under this Article to a **third-party service provider**. In case of such outsourcing, the financial entity remains **fully responsible for the fulfilment of the incident reporting requirements**.
**Instance 1 — VAG — S2 — `in accordance with Union and national sectoral law`**
*Berry anchor:* §3.3.1 (`in accordance with`).
**Instance 2 — VAG — S2 — `third-party service provider`**
Inherits DORA Art. 3(19) `ICT third-party service provider` (DORA-D19). S2.
*Berry anchor:* §3.3.1 (`third-party service provider`); cf. pilot §3.
**Instance 3 — VAG — S2 — `fully responsible`**
The same responsibility-clause pattern as DORA Art. 26(3) `retain at all times full responsibility for ensuring compliance with this Regulation`. S2.
*Berry anchor:* §5.1 (`fully`); §3.3.1 (`responsible`).
**Definitional anchor:** DORA Art. 3(19) `ICT third-party service provider`.
**Proportionality-status:** Art. 4 applies.
---
#### 4.23 CL19-6 — Art. 19(6) — CA→other authorities forwarding (5 recipient categories)
**Source locus:** Art. 19(6).
> Upon receipt of the initial notification and of each report referred to in paragraph 4, the competent authority shall, in a timely manner, provide details of the major ICT-related incident to the following recipients based, as applicable, on their respective competences:
>
> (a) EBA, ESMA or EIOPA;
>
> (b) the ECB, in the case of financial entities referred to in Article 2(1), points (a), (b) and (d);
>
> (c) the competent authorities, single points of contact or CSIRTs designated or established in accordance with Directive (EU) 2022/2555;
>
> (d) the resolution authorities, as referred to in Article 3 of Directive 2014/59/EU, and the Single Resolution Board (SRB) with respect to entities referred to in Article 7(2) of Regulation (EU) No 806/2014, and with respect to entities and groups referred to in Article 7(4)(b) and (5) of Regulation (EU) No 806/2014 if such details concern incidents that pose a risk to ensuring critical functions within the meaning of Article 2(1), point (35), of Directive 2014/59/EU; and
>
> (e) other relevant public authorities under national law.
**Instance 1 — VAG — S3 — `in a timely manner` (CA forwarding)**
`timely manner` for CA→other-authorities transmission. Same Berry `timely` family as CL17-8. S3.
*Berry anchor:* §5.1 (`timely`); §5.7 (temporal operator).
**Instance 2 — POLY — S2 — `based, as applicable, on their respective competences`**
*Berry anchor:* §5.1 (`as applicable`); §3.3.1 (`respective competences`).
**Instance 3 — COORD — S2 — `ECB, in the case of financial entities referred to in Article 2(1), points (a), (b) and (d)`**
Three ECB-coverage categories (Art. 2(1)(a) credit institutions; (b) insurance undertakings; (d) investment firms). S2 (the cross-reference is mechanically defined).
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Instance 4 — VAG — S3 — `Single Resolution Board (SRB) … critical functions within the meaning of Article 2(1), point (35), of Directive 2014/59/EU`**
The SRB-recipient trigger depends on the **risk to critical functions** under BRRD Art. 2(1)(35). Same Berry `critical functions` definition (inherits from BRRD). S3.
*Berry anchor:* §5.1 (`critical functions`); §3.3.1 (`risk to ensuring`).
**Definitional anchor:** DORA-D10; DORA Art. 2(1)(a)/(b)/(d); DORA Art. 46 (single-CA designation cross-ref).
**Scope:** regulator→regulator (intra-supervisory).
**Proportionality-status:** Art. 4 applies.
---
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
#### 4.28 CL21-2 — Art. 21(3) — Report submission deadline
**Source locus:** Art. 21(3).
> The ESAs shall submit the report referred to in paragraph 1 to the European Parliament, to the Council and to the Commission by **17 January 2025**.
**Instance 1 — POLY — S2 — submission recipients (EP + Council + Commission)**
Three recipients. S2.
**Definitional anchor:** DORA-D29.
**Proportionality-status:** Art. 4 applies.
**Status note:** as of mid-2025, the deadline (17 January 2025) has passed; the ESAs Joint Committee report was published in Q1 2025 (per Council Document 5572/25 of 7 February 2025).
---
#### 4.29 CL22-1 — Art. 22(1) — Competent authority supervisory feedback
**Source locus:** Art. 22(1).
> Without prejudice to the technical input, advice or remedies and subsequent follow-up which may be provided, where applicable, in accordance with national law, by the CSIRTs under Directive (EU) 2022/2555, the competent authority shall, upon receipt of the initial notification and of each report as referred to in Article 19(4), **acknowledge receipt and may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance** to the financial entity, in particular by making available any relevant **anonymised information and intelligence** on similar threats, and may discuss **remedies applied at the level of the financial entity and ways to minimise and mitigate adverse impact across the financial sector**. Without prejudice to the supervisory feedback received, financial entities shall remain **fully responsible for the handling and for consequences of the ICT-related incidents reported pursuant to Article 19(1)**.
**Instance 1 — POLY — S3 — `may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance`**
Discretionary CA feedback. Multiple hedge modalities (`may` + `where feasible` + `relevant and proportionate` + `feedback or guidance`). The regulatory framing is: the CA acknowledges and may-but-not-must provide feedback. Three readings:
- **R1:** Mandatory feedback obligation (deep reading).
- **R2:** Discretionary feedback (literal reading).
- **R3:** Default-with-exceptions.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Mandatory | None in OJ |
| R2 | Discretionary | In-Directive: literal `may` |
| R3 | Default-with-exceptions | None in OJ |
R2 is the literal reading. R1 vs R2 admit materially distinct CA-supervision compliance populations. S3.
*Berry anchor:* §3.3.1 (`may`); §5.1 (`feasible`, `relevant`, `proportionate`).
**Instance 2 — VAG — S2 — `relevant and proportionate`**
Same two-adjective Berry pair as Art. 4(2) chapeau. S2.
*Berry anchor:* §5.1 (`relevant`, `proportionate`).
**Instance 3 — POLY — S2 — `anonymised information and intelligence`**
Two information types (AND). S2.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`anonymised`, `intelligence`).
**Instance 4 — VAG — S2 — `fully responsible for the handling and for consequences`**
Same responsibility-clause as CL19-5. S2.
*Berry anchor:* §5.1 (`fully`); §3.3.1 (`handling`, `consequences`).
**Definitional anchor:** DORA Art. 46 (CA designation).
**Scope:** regulator→financial-entity.
**Proportionality-status:** Art. 4 applies.
---
#### 6.4 Art. 19(6) — 5-recipient multi-supervisory routing
Art. 19(6) requires the competent authority to forward the incident details to **5 categories of recipients**:
| # | Recipient | Trigger |
|---|---|---|
| (a) | EBA, ESMA or EIOPA | All |
| (b) | ECB | If Art. 2(1)(a)/(b)/(d) entities (credit institutions, insurance undertakings, investment firms) |
| (c) | NIS 2 CAs / SPOCs / CSIRTs | Cross-Directive (DORA ↔ NIS 2) |
| (d) | Resolution authorities (BRRD) + SRB | If incident poses risk to BRRD critical functions |
| (e) | Other public authorities under national law | Member State-determined |
This is the **most extensive multi-supervisory routing in the 5-regulation corpus**. An incident may simultaneously engage 5 different supervisory streams. The CA→recipients timing is `in a timely manner` (CL19-6 Instance 1, S3).
- **Berry anchor:** §3.3.1 (`based, as applicable, on their respective competences`); §5.1 (`in a timely manner`).
- **Structural implication:** the CA-side reporting system must support **5-way multiplexing**. The financial-entity-side report (Art. 19(4)) produces a single document; the CA-side multiplexer splits it.
#### 6.6 Art. 22 — supervisory feedback: discretionary vs. mandatory
Art. 22(1) specifies that the competent authority **may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance**. The `may` is the operative trigger. Three readings (CL22-1 Instance 1): R1 mandatory, R2 discretionary (literal), R3 default-with-exceptions. R2 is the literal reading.
- **Berry anchor:** §3.3.1 (`may`); §5.1 (`feasible`, `relevant`, `proportionate`).
- **Structural implication:** Art. 22(1) creates a **discretion gap** between reporting (mandatory, Art. 19) and supervisory response (discretionary, Art. 22). This is a **closed-loop asymmetry**: entities must report; CAs may respond.
#### 6.9 Art. 19(5) — outsourcing + responsibility clause
Art. 19(5) permits the financial entity to **outsource** the reporting obligations under Art. 19 to a third-party service provider (under Union and national sectoral law), **with the financial entity remaining fully responsible**. This mirrors DORA Art. 26(3) `retain at all times full responsibility for ensuring compliance with this Regulation` (for TLPT) and DORA Art. 22(1) `Without prejudice to the supervisory feedback received, financial entities shall remain fully responsible`.
- **Berry anchor:** §3.3.1 (`in accordance with`); §5.1 (`fully responsible`).
- **Structural implication:** the **responsibility non-delegation principle** is consistent across Ch. III (Art. 19(5)), Ch. IV (Art. 26(3)), and Art. 22(1). A financial entity cannot outsource its reporting compliance by outsourcing the reporting process.
## DORA v0.2 — Chapter IV: Digital Operational Resilience Testing (Art. 24–27)
> **Source.** OJ L 333, 27.12.2022, p. 45–48. `03_REFERENCE_MATERIAL/Regulatory_References/DORA.txt`, lines **2595–2850**.
>
> **Pattern.** Each article quoted in full, then per-clause analysis. Universal `[recital NN]` convention. DORA-specific fields: `definitional-anchor`, `proportionality-status: Art. 4 applies`, `RTS-pending: Art. 20` (where applicable), `definitional-anchor: DORA Art. 26(11) → TIBER-EU` (non-binding guidance).
>
> **Chapter IV establishes the testing programme.** Art. 24 sets the general programme as an integral part of the Art. 6 ICT risk-management framework. Art. 25 enumerates (in an open list) the test modalities. Art. 26 mandates Threat-Led Penetration Testing (TLPT) on a hard 3-year cadence, anchored to the **TIBER-EU** framework (non-binding). Art. 27 specifies requirements for testers (NEW in v0.2; T3 omitted Art. 27 entirely).
>
> **Articles in this file:** 4 articles, 24 paragraphs, 17 atomic clauses (CL24-1 … CL27-3).
---
### 1. Articles covered
| Article | Title | Paragraphs | New in v0.2? | T3 clause |
|---|---|---|---|---|
| Art. 24 | General requirements for the performance of digital operational resilience testing | 6 | No (extended) | **C32** |
| Art. 25 | Testing of ICT tools and systems | 3 | No (extended) | **C33** |
| Art. 26 | Advanced testing of ICT tools, systems and processes based on TLPT | 11 | No (extended) | **C34** |
| Art. 27 | Requirements for testers for the carrying out of TLPT | 3 | **YES** | — (not in T3) |
**Note on Art. 4 (Proportionality):** every clause card in this file carries `proportionality-status: Art. 4 applies` (per pilot convention).
**Note on Art. 20 (RTS-pending):** no RTS mandate in Ch. IV specifically (the RTS mandate is in Art. 26(11) for TLPT details, addressed inline).
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CL24-1 | Art. 24(1)+(2) chapeau | Programme establishment | **S3** | Testing programme as integral part of Art. 6 ICT risk-management framework. |
| CL24-2 | Art. 24(3) | Risk-based approach | **S3** | Risk-based approach per Art. 4(2); `evolving landscape of ICT risk`; `criticality of information assets`. |
| CL24-3 | Art. 24(4) | Independence + conflicts of interest | **S3** | Tests by independent parties (internal or external); conflicts of interest avoided. |
| CL24-4 | Art. 24(5) | Remediation procedures | **S2** | Procedures to prioritise, classify and remedy issues; internal validation. |
| CL24-5 | Art. 24(6) | Yearly testing cadence | **S2** | At least yearly tests on ICT systems supporting critical or important functions. |
| CL25-1 | Art. 25(1) | Open-list test modalities | **S3** | 12 enumerated modalities (`such as vulnerability assessments … penetration testing`). |
| CL25-2 | Art. 25(2) | CSD/CCP pre-deployment | **S2** | Vulnerability assessments before any deployment/redeployment. |
| CL25-3 | Art. 25(3) | Microenterprise exception | **S3** | Microenterprises combine risk-based with strategic planning of ICT testing. |
| CL26-1 | Art. 26(1) | TLPT cadence | **S2** | **Every 3 years**; competent authority may reduce/increase. |
| CL26-2 | Art. 26(2) | TLPT scope | **S3** | Live production systems; critical or important functions. |
| CL26-3 | Art. 26(3)+(4) | CTPP participation + pooled TLPT | **S3** | Pooled testing across multiple entities when CTPPs are in scope. |
| CL26-4 | Art. 26(5)+(6)+(7) | Risk-mgmt controls + attestation | **S3** | Risk controls during TLPT; attestation + mutual recognition between CAs. |
| CL26-5 | Art. 26(8) | Identification of TLPT entities | **S3** | Three criteria: impact, financial stability, ICT risk profile. |
| CL26-6 | Art. 26(11) | ESAs RTS per TIBER-EU | **S2** | Draft RTS developed in agreement with ECB; **non-binding TIBER-EU anchor**. |
| CL27-1 | Art. 27(1)(a)–(e) | Tester requirements (external) | **S3** | Five sub-requirements: suitability, expertise, certification, assurance, insurance. |
| CL27-2 | Art. 27(2)(a)–(c) | Internal-tester additional conditions | **S3** | Approval by CA; sufficient resources; threat intelligence provider external. |
| CL27-3 | Art. 27(3) | Data processing in contracts | **S2** | Contracts require sound management of TLPT results and data. |
**Total: 17 atomic clauses (Art. 24: 5; Art. 25: 3; Art. 26: 6; Art. 27: 3).**
---
### 3. Verbatim OJ text — Art. 24–27
#### 4.9 CL26-1 — Art. 26(1) — TLPT cadence
**Source locus:** Art. 26(1).
> Financial entities, other than entities referred to in Article 16(1), first subparagraph, and other than microenterprises, which are identified in accordance with paragraph 8, third subparagraph, of this Article, shall carry out **at least every 3 years** advanced testing by means of TLPT. Based on the risk profile of the financial entity and taking into account operational circumstances, the competent authority may, where necessary, request the financial entity to **reduce or increase this frequency**.
**Instance 1 — POLY — S2 — `at least every 3 years`**
`at least every 3 years` admits three readings:
- **R1:** The gap between two consecutive TLPTs must be ≥3 years.
- **R2:** TLPTs must occur in years divisible by 3 (calendar 3-year cycle).
- **R3:** Three complete TLPTs per decade (rolling average).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Gap ≥3 years | In-Directive: literal `at least every 3 years` |
| R2 | Calendar 3-year cycle | None in OJ |
| R3 | Rolling average | None in OJ |
R1 is the literal reading. S2 (the operational practice converges on R1).
*Berry anchor:* §5.7 (temporal operator); §5.1 (`at least`).
**Instance 2 — VAG — S3 — `where necessary, request the financial entity to reduce or increase this frequency`**
The trigger and bounds are undefined.
- **R1:** CA may reduce frequency based on low risk profile.
- **R2:** CA may increase frequency based on high risk profile.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Reduce only | In-Directive: literal `reduce or increase` |
| R2 | Increase only | In-Directive: literal `reduce or increase` |
| R3 | Either | In-Directive: literal |
R3 is the literal reading. The `where necessary` hedge does not specify what `necessary` means (high-risk evolution? significant findings from prior TLPT? sectoral threat?). S3.
*Berry anchor:* §5.1 (`where necessary`); §5.4.7 (OR in discretion).
**Definitional anchor:** DORA Art. 3(17) `TLPT` (DORA-D17) → Art. 26(11) → TIBER-EU.
**RTS-pending:** Art. 26(11) (see CL26-6).
**Proportionality-status:** Art. 4 applies.
---
#### 6.2 Art. 26(1) — Hard numeric anchor (3 years) reduces temporal ambiguity
- **Berry anchor:** §5.7 (temporal operators); §5.1 (`at least every 3 years`).
- **Structural implication:** the 3-year cadence materially reduces temporal ambiguity for TLPT (compared to the year-by-year discretionary `at least yearly` of Art. 24(6), which is S2). However, the CA discretion clause (`reduce or increase this frequency`) partially reopens the ambiguity (CL26-1 Instance 2, S3).
- **Layer 1 observation:** hard numeric anchors are **the single most effective disambiguation technique** in EU cybersecurity regulations. DORA uses two of them in Ch. IV: 3 years (Art. 26(1)) and yearly (Art. 24(6)). Both anchor the temporal operator; the 3-year anchor is more rigid and less vulnerable to entity discretion.
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
#### 4.4 CL28-4 — Art. 28(5) + (6) — Information security + audit/auditor
**Source locus:** Art. 28(5) and 28(6).
> Financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with **appropriate information security standards** …. the **most up-to-date and highest quality information security standards** …. In exercising access, inspection and audit rights …. **risk-based approach** …. **commonly accepted audit standards** …. **high technical complexity** …. **appropriate skills and knowledge** ….
**Instance 1 — VAG — S3 — `appropriate information security standards` + `most up-to-date and highest quality`**
The standards baseline is undefined; the super-latives (`most up-to-date`, `highest quality`) are undefined for critical/important. Three materially distinct readings of the standards baseline:
- **R1:** ISO 27001 (or equivalent) baseline; industry-leading (ISO 27001:2022 + sector-specific add-ons) for critical/important.
- **R2:** Sector-specific standards baseline; CA-determined for critical/important.
- **R3:** CTPP-defined baseline (subject to entity approval).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ISO 27001 / state-of-the-art | In-Directive: literal `most up-to-date and highest quality` |
| R2 | Sectoral / CA-determined | None in OJ |
| R3 | CTPP-defined | None in OJ |
R1 vs R3 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`appropriate`, `most up-to-date`, `highest quality`).
**Instance 2 — VAG — S3 — `commonly accepted audit standards` + `appropriate skills and knowledge`**
`commonly accepted` is undefined; `appropriate skills` is Berry-flagged. Three materially distinct readings of the audit-regime:
- **R1:** International standards (ISAE 3402, SOC 2 Type II) + certified qualifications (CISSP, CISM, CISA).
- **R2:** Sectoral standards + experience-based competence.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | International + certified | None in OJ |
| R2 | Sectoral + experience | None in OJ |
R1 is the most likely interpretation but R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`commonly accepted`, `appropriate`); §3.3.1 (`audit standards`).
---
#### 4.9 CL30-1 — Art. 30(1) — Written contract + format
**Source locus:** Art. 30(1).
> The rights and obligations of the financial entity and of the ICT third-party service provider shall be **clearly allocated and set out in writing** …. include the service level agreements and be documented in **one written document** …. available to the parties **on paper, or in a document with another downloadable, durable and accessible format**.
**Instance 1 — VAG — S2 — `clearly allocated` + `one written document` + `downloadable, durable and accessible format` (consolidated)**
Three Berry-classic qualifiers in the chapeau. `clearly` undefined; `one written document` admits multiple readings; `downloadable, durable and accessible` is a three-property AND list. Three readings of the format-specification gate:
- **R1:** Explicit bilateral commitments in a single PDF; all three format properties required.
- **R2:** Sufficient detail to enable enforcement in a master agreement + incorporated documents; CA-determined format.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Single PDF + all three properties | In-Directive: literal `one written document` + `and` |
| R2 | Master + incorporated + CA-determined | None in OJ |
R1 is the literal reading; R1 vs R2 admit materially distinct compliance populations. S2.
*Berry anchor:* §5.1 (`clearly`); §3.3.1 (`one written document`); §5.4.7 (AND).
**Definitional anchor:** DORA Art. 3(21) DORA-D21 `ICT services`.
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No (baseline obligation).
**Scope:** `regulator→financial-entity` + propagated to CTPP contracts.
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

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in this file inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; Art. 3(5) `ICT risk`; Art. 3(30) `management body` (composite cross-reference, see pilot file §2.10). The Art. 3(22) `critical or important function` (S3 tautology, see pilot file §2.7) propagates to Art. 6(8)(f).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`effective`, `prudent`); §5.4.7 (AND); cf. CRA-CL27 `handled effectively` (same pattern).

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** Art. 4's proportionality pattern mirrors **NIS 2 Art. 1(2)** (proportionality in scope) and **CRA Art. 1(2)** (proportionality for microenterprises and SMEs). DORA Art. 4 is more elaborate than either, providing explicit CA-review (CL4-3) that NIS 2 and CRA do not have.


### from regs/DORA.ambiguity.md

The information set is undefined. The standard is "necessary" — same Berry pattern as NIS 2 CL36 "where available" and GDPR Art. 33(3) `all relevant information`. S2.

### from regs/DORA.ambiguity.md

Twin temporal trigger: `without undue delay` AND `as soon as they become aware of`. Three readings (same as NIS 2 CL35):

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`without undue delay`); §5.7 (temporal operator); §5.4.7 (temporal AND); cf. NIS 2 CL35.

### from regs/DORA.ambiguity.md

Same awareness trigger as NIS 2 CL35 Instance 2 (R1 actual vs R2 constructive knowledge). S3.

### from regs/DORA.ambiguity.md

Same Berry `potentially` as NIS 2 CL27 `likely to adversely affect`. S2.

### from regs/DORA.ambiguity.md

Same Berry `in accordance with` pattern as CRA Annex I chapeau. S2.

### from regs/DORA.ambiguity.md

The recipients are selected based on competence. Same Berry pattern as NIS 2 CL42 `where appropriate`. S2.

### from regs/DORA.ambiguity.md

`consistent approach` between DORA reporting and NIS 2 reporting (NIS 2 Art. 23; cf. NIS 2 file §3.10). S3.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the CER Directive (EU) 2022/2557 parallel is **NIS 2 Art. 23(10)** (CSIRTs/CAs provide info to CER authorities). DORA's Art. 19(6)(d) (resolution authorities + SRB) is unique to DORA — no other regulation has a single-actor forwarding to the **Single Resolution Board**.


### from regs/DORA.ambiguity.md

The structural pattern is **mandatory acknowledge + discretionary substance** — the CA must acknowledge receipt (per the `shall … acknowledge receipt and may … provide` coordination) but the substantive feedback is at CA discretion. This is **the opposite** of the NIS 2 Art. 23(5) pattern (mandatory CSIRT response within 24h), and is a deliberate DORA choice reflecting the CA-specific regulatory authority.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** same pattern as GDPR Art. 28(4) (processor obligations do not discharge controller obligations) and NIS 2 Art. 21(1) (management-body responsibility).


### from regs/DORA.ambiguity.md

**Note on definitional anchors:** every ICT-related clause in Ch. IV inherits from DORA Art. 3(2) → NIS 2 Art. 6(1) (`network and information system`). The TLPT definitional anchor is DORA Art. 26(11) → **TIBER-EU** (non-binding ECB framework) — same **binding-to-non-binding definitional regress** pattern as CRA Annex I → ISO standards.

### from regs/DORA.ambiguity.md

The `at least every 3 years` cadence is a **hard numeric anchor**. This is the same Berry-relief pattern as CRA Annex I §2(c) `automatic security updates installed within an appropriate timeframe` (no anchor) vs. CRA Annex II §4 `disseminated without delay` (no anchor).

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.1 (`appropriate`); §3.3.1 (`register`). Same as CRA-CL129.

### from regs/DORA.ambiguity.md

**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1) `network and information system`; DORA Art. 3(22) `critical or important function` (S3).
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No.
**Scope:** `regulator→financial-entity` + propagated to CTPP contractually.

<!-- aegis:purity: own_reg=DORA; demoted=18; core_cross_mentions=0 -->