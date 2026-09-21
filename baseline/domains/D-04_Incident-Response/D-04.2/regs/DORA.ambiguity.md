# D-04.2 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
#### 4.13 CL6-5 — Art. 6(8)+(9)+(10) — Digital operational resilience strategy + multi-vendor + outsourcing
**Source locus:** Art. 6(8), 6(9), 6(10).
> 8. The ICT risk management framework shall include a **digital operational resilience strategy** setting out how the framework shall be implemented. To that end, the digital operational resilience strategy shall include methods to address ICT risk and attain specific ICT objectives, by:
>
> (a) explaining how the ICT risk management framework supports the financial entity's business strategy and objectives;
>
> (b) establishing the **risk tolerance level for ICT risk, in accordance with the risk appetite of the financial entity, and analysing the impact tolerance for ICT disruptions**;
>
> (c) setting out clear information security objectives, including key performance indicators and key risk metrics;
>
> (d) explaining the ICT reference architecture and any changes needed to reach specific business objectives;
>
> (e) outlining the different mechanisms put in place to detect ICT-related incidents, prevent their impact and provide protection from it;
>
> (f) evidencing the current digital operational resilience situation on the basis of the number of major ICT-related incidents reported and the effectiveness of preventive measures;
>
> (g) implementing digital operational resilience testing, in accordance with Chapter IV of this Regulation;
>
> (h) outlining a communication strategy in the event of ICT-related incidents the disclosure of which is required in accordance with Article 14.
>
> 9. Financial entities may, in the context of the digital operational resilience strategy referred to in paragraph 8, define a **holistic ICT multi-vendor strategy**, at group or entity level, showing key dependencies on ICT third-party service providers and explaining the rationale behind the procurement mix of ICT third-party service providers.
>
> 10. Financial entities may, in accordance with Union and national sectoral law, **outsource the tasks of verifying compliance with ICT risk management requirements** to intra-group or external undertakings. In case of such outsourcing, the financial entity remains **fully responsible for the verification of compliance with the ICT risk management requirements**.
**Instance 1 — POLY — S3 — Art. 6(8)(a)–(h) — 8-point strategy enumeration**
The strategy content list. **Open or closed**?
- **R1:** Closed (the 8 are exhaustive; the strategy must contain all of them).
- **R2:** Open (the 8 are illustrative; additional elements may be added).
- **R3:** Floor (the 8 are minimum; additional elements required).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed | None in OJ |
| R2 | Open | In-Directive: literal `include … by` (open-list) |
| R3 | Floor | None in OJ |
R2 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`include … by`); §5.4.7 (8-way enumeration).
**Instance 2 — VAG — S3 — `risk tolerance level for ICT risk, in accordance with the risk appetite of the financial entity` (Art. 6(8)(b))**
`risk tolerance` and `risk appetite` are **case-law-laden banking-supervision terms** (Basel Committee, EBA guidelines). Three materially distinct readings:
- **R1:** Risk tolerance = quantitative limit; risk appetite = qualitative board statement.
- **R2:** Risk tolerance = qualitative; risk appetite = quantitative.
- **R3:** Synonymous (both refer to the same concept).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Tolerance-quant, Appetite-qual | In-Directive: EBA Guidelines on ICT and Security Risk Management |
| R2 | Tolerance-qual, Appetite-quant | None in OJ |
| R3 | Synonymous | None in OJ |
R1 is the dominant EBA-aligned reading. S3.
*Berry anchor:* §3.3.1 (`risk tolerance`, `risk appetite`); §5.1 (`in accordance with`).
**Instance 3 — VAG — S3 — `key performance indicators and key risk metrics` (Art. 6(8)(c))**
The KPI/KRM pair. Three readings:
- **R1:** KPIs (forward-looking performance) AND KRMs (backward-looking risk).
- **R2:** Two labels for the same metrics.
- **R3:** Either, per entity choice.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct (forward vs. backward) | None in OJ |
| R2 | Synonymous | None in OJ |
| R3 | Either | In-Directive: literal `and` |
R1 is the conventional reading. S3.
*Berry anchor:* §3.3.1 (`key performance indicators`, `key risk metrics`); §5.4.7 (AND).
**Instance 4 — POLY — S2 — `major ICT-related incidents reported and the effectiveness of preventive measures` (Art. 6(8)(f))**
Two evidence sources (AND). The clause does not specify **how many** major incidents or **what** effectiveness threshold. S2.
*Berry anchor:* §3.3.1 (`major ICT-related incidents`, `effectiveness`).
**Instance 5 — VAG — S3 — `holistic ICT multi-vendor strategy` (Art. 6(9))**
The multi-vendor strategy. `holistic` is Berry-flagged. Three readings:
- **R1:** Multi-vendor for all ICT services (no single-vendor dependencies).
- **R2:** Multi-vendor for critical services (CTPPs may still be single-vendor for non-critical).
- **R3:** Documented strategy (any structure; the entity is its own judge of "holistic").
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All-services | None in OJ |
| R2 | Critical-only | None in OJ |
| R3 | Documented | In-Directive: literal `holistic` (entity judgment) |
R3 is the literal reading. S3 (R1 vs R3 admit materially distinct compliance populations: R1 requires vendor diversification; R3 requires only documentation).
*Berry anchor:* §3.3.1 (`holistic`); §3.3.1 (`multi-vendor`).
**Instance 6 — POLY — S3 — `outsource the tasks of verifying compliance with ICT risk management requirements to intra-group or external undertakings` (Art. 6(10))**
The outsourcing permission. Two paths (OR): intra-group OR external. Three readings:
- **R1:** Outsourcing permitted under any of (a) Union sectoral law, (b) national sectoral law, (c) both.
- **R2:** Outsourcing permitted only if both Union and national law allow.
- **R3:** Outsourcing permitted under either Union or national law.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Either (Union OR national) | In-Directive: literal `in accordance with Union and national sectoral law` |
| R2 | Both required | None in OJ |
| R3 | Either | In-Directive: literal |
R1 is the literal reading (the `and` in `Union and national sectoral law` is conjunctive but each is independently sufficient — see also Art. 28 outsourcing provisions). S3.
*Berry anchor:* §5.4.7 (AND/OR in `Union and national`); §3.3.1 (`intra-group`, `external undertakings`).
**Instance 7 — VAG — S3 — `fully responsible for the verification of compliance with the ICT risk management requirements` (Art. 6(10))**
The non-delegable responsibility. `fully` admits three readings:
- **R1:** Absolute (no derogation even from gross negligence of outsourcee).
- **R2:** Standard (ordinary liability for own acts and those of the outsourcee).
- **R3:** Strict (joint-and-several liability with the outsourcee).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Absolute | None in OJ |
| R2 | Standard | None in OJ |
| R3 | Strict | In-Directive: literal `fully responsible` + non-delegable principle |
R3 is the literal reading (consistent with the management-body non-delegable responsibility in CL5-5 Instance 1). S3.
*Berry anchor:* §3.3.1 (`fully responsible`); cf. CL5-5 Instance 1 `ultimate responsibility`.
**Definitional anchor:** DORA Art. 3(1) `digital operational resilience` (DORA-D01, S3 `build, assure and review`); DORA Art. 3(10) `major ICT-related incident` (DORA-D10, S3 `high adverse impact`); DORA Art. 3(8) `ICT-related incident` (DORA-D08); DORA Art. 3(22) `critical or important function` (S3 tautology); DORA Art. 3(19) `ICT third-party service provider` (DORA-D19); DORA Art. 3(20) `ICT intra-group service provider` (DORA-D20).
**Proportionality-status:** Art. 4 applies (Art. 6(8)(b) `risk appetite` and Art. 6(9) `multi-vendor strategy` are both proportionality-sensitive).
**Scope:** financial entity.
---
### 5. T3-vs-text gaps
This section catalogues **inconsistencies between the v0.1 T3 mapping** and the OJ text. Per pilot convention, T3-vs-text gaps are flagged separately from linguistic ambiguities of the regulation (they are inconsistencies of the mapping layer, not of the text).
#### 6.3 Art. 6 chapeau — the framework's three-attribute triad
Art. 6(1) opens with `sound, comprehensive and well-documented` (three attributes, AND). This is the **framework-level analog** of:
- **Art. 24(1) `sound and comprehensive`** (testing programme, two attributes; CL24-1)
- **Berry anchor:** §5.1 (`sound`, `comprehensive`, `well-documented`); §5.4.7 (AND); §5.5 (parallelism).
- **Structural implication:** the framework's three attributes set the bar for every Ch. II–V Sec. I clause. Any clause that fails one of the three (e.g. a framework that is `comprehensive and well-documented` but not `sound`) would be non-compliant.
#### 6.6 Art. 6(8) — the 8-point resilience strategy
Art. 6(8) enumerates **8 strategy elements** (open list: `include … by`). The 8 elements cover the strategy's full lifecycle: (a) business alignment, (b) risk tolerance, (c) KPIs/KRMs, (d) reference architecture, (e) detection/prevention, (f) current state evidence, (g) testing, (h) communication.
- **Berry anchor:** §3.3.1 (`include … by`); §5.4.7 (8-way enumeration).
- **Structural implication:** the 8-point strategy is the **operational mirror** of the framework's three-attribute triad (CL6-1 Instance 1). Where the triad describes the framework's qualities, the 8 elements describe its **contents**. A framework that is `sound, comprehensive and well-documented` and contains all 8 elements satisfies the chapeau.
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
#### 6.5 Art. 21 — single EU Hub feasibility report (RTS-style structural delegation)
Art. 21 mandates a **feasibility report** by the ESAs Joint Committee (in consultation with ECB and ENISA) on the potential centralisation of incident reporting through a **single EU Hub**. The report must comprise **7 elements** (a)–(g).
This is **not an obligation on financial entities** — it is a meta-procedural mandate on the ESAs. But its outcome (whether or not a single EU Hub is established) could materially alter the entity-side reporting architecture. As of Q1 2025 (post the 17 January 2025 deadline), the ESAs Joint Committee report was published; the legislative follow-up is uncertain.
- **Berry anchor:** §3.3.1 (`single EU Hub`); §5.1 (`feasibility`); §3.3.1 (`interoperability`).
- **Layer 1 catalogue only.** Layer 2 must surface the architectural implications (sensitive-information concentration, jurisdictional sovereignty, operational resilience of the hub).
#### 6.9 Art. 19(5) — outsourcing + responsibility clause
Art. 19(5) permits the financial entity to **outsource** the reporting obligations under Art. 19 to a third-party service provider (under Union and national sectoral law), **with the financial entity remaining fully responsible**. This mirrors DORA Art. 26(3) `retain at all times full responsibility for ensuring compliance with this Regulation` (for TLPT) and DORA Art. 22(1) `Without prejudice to the supervisory feedback received, financial entities shall remain fully responsible`.
- **Berry anchor:** §3.3.1 (`in accordance with`); §5.1 (`fully responsible`).
- **Structural implication:** the **responsibility non-delegation principle** is consistent across Ch. III (Art. 19(5)), Ch. IV (Art. 26(3)), and Art. 22(1). A financial entity cannot outsource its reporting compliance by outsourcing the reporting process.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

- **CRA Annex I Part I §1 chapeau** `products with digital elements shall be designed, developed and produced …` (manufacturing lifecycle, three verbs; CRA-CL14)

### from regs/DORA.ambiguity.md

- **NIS 2 Art. 21(1) `appropriate and proportionate technical, operational and organisational measures`** (measures chapeau)


### from regs/DORA.ambiguity.md

The 3-attribute triad (`sound, comprehensive and well-documented`) is **the most demanding framework chapeau in the 5-regulation corpus** — it requires three distinct qualities (effectiveness, completeness, traceability). CRA Annex I Part I §1 has three verbs (design, develop, produce) but they describe **processes** not qualities. DORA's triad describes **qualities of an artifact** (the framework itself), which is a different kind of obligation.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the triad is the most explicit framework-quality specification in the corpus. NIS 2 Art. 21(1) uses `appropriate and proportionate` (2 qualifiers); CRA Annex I Part I uses process verbs; GDPR Art. 24 uses `appropriate` (1 qualifier). DORA's 3-attribute triad is the most demanding.


### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** the open-list pattern is the **regulatory-drafting convention** shared with CRA Annex I Part I (multiple open enumerations) and NIS 2 Art. 21(2) (10 sub-points). DORA's 8 elements are **more strategic** (KPIs, risk tolerance, communication) than CRA's (technical requirements) and **more operational** than NIS 2's (governance policies).


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

`consistent approach` between DORA reporting and NIS 2 reporting (NIS 2 Art. 23; cf. NIS 2 file §3.10). S3.

### from regs/DORA.ambiguity.md

- **Structural implication:** the **single EU Hub** is structurally analogous to the **NIS 2 single point of contact (SPOC)** (NIS 2 Art. 12) and the **CER Directive critical-entity framework** but at a higher integration level.

### from regs/DORA.ambiguity.md

- **Cross-regulation consistency:** same pattern as GDPR Art. 28(4) (processor obligations do not discharge controller obligations) and NIS 2 Art. 21(1) (management-body responsibility).


<!-- aegis:purity: own_reg=DORA; demoted=13; core_cross_mentions=0 -->

