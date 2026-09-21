# D-08.2 — Relevant Ambiguity (DORA)

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
#### 4.10 CL26-2 — Art. 26(2) — TLPT scope
**Source locus:** Art. 26(2).
> Each threat-led penetration test shall cover **several or all critical or important functions** of a financial entity, and shall be performed on **live production systems** supporting such functions.
**Instance 1 — POLY — S2 — `several or all critical or important functions`**
`several` vs. `all`:
- **R1:** Several (≥2) suffices; all is not required.
- **R2:** All is the default; several only when CA approves.
- **R3:** Either, per CA determination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Several default | In-Directive: literal `several or all` |
| R2 | All default | None in OJ |
| R3 | CA-determined | In-Directive: Art. 26(2) CA validation |
R1 is the literal reading (per entity choice). S2.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`several`, `all`).
**Instance 2 — VAG — S3 — `live production systems`**
`live production` admits three readings:
- **R1:** Production-only (no test/staging environments).
- **R2:** Production-and-mirrored (production + equivalent staging).
- **R3:** Production-or-equivalent (either works).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Production-only | In-Directive: literal `live production systems` |
| R2 | Production-and-mirrored | In-Directive: TIBER-EU guidance |
| R3 | Either | None in OJ |
R1 is the literal reading. R1 vs R2 admit materially distinct compliance populations (R2 includes mirrored/staging environments that R1 excludes). S3.
*Berry anchor:* §3.3.1 (`live production`).
**Instance 3 — POLY — S2 — `underlying ICT systems, processes and technologies`**
Three categories (AND). Distinct scopes:
- **R1:** ICT systems (infrastructure) AND processes (business) AND technologies (tools).
- **R2:** Compound: any combination of the three.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All three (AND) | In-Directive: literal `systems, processes and technologies` |
| R2 | Compound | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
**Definitional anchor:** DORA Art. 3(17) `TLPT`; DORA-D22 `critical or important function` (S3 tautology).
**RTS-pending:** Art. 26(11) (CL26-6) covers scope details in (c)(i).
**Proportionality-status:** Art. 4 applies.
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

**T3:** C26 named `patch management`. **OJ:** patches are at Art. 9(4)(f) `have appropriate and comprehensive documented policies for patches and updates`; Art. 13(6) is training (`commensurate to the remit of their functions`), NOT patches. **Gap.** T3 likely mapped C26 to Art. 13(6) due to **incidental overlap** (both deal with security disciplines). **Implication.** v0.2 places patches in CL9-4 Instances 14-15 (Art. 9(4)(f) hinge); Art. 13(6) is analysed in CL13-2 Instance 3 (training). Same structural correction as Q6=a identifies for CRA-CL24.

### from regs/DORA.ambiguity.md

`consistent approach` between DORA reporting and NIS 2 reporting (NIS 2 Art. 23; cf. NIS 2 file §3.10). S3.

<!-- aegis:purity: own_reg=DORA; demoted=2; core_cross_mentions=0 -->

