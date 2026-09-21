# D-01.2 — Relevant Ambiguity (DORA)

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
#### 6.1 Art. 4 propagation pattern — three distinct proportionality regimes
Art. 4 establishes **three distinct proportionality regimes** that operate simultaneously:
- **Art. 4(1) — Ch. II proportionality** (CL4-1): default for the ICT risk management framework.
- **Art. 4(2) — Ch. III, IV, V Sec. I proportionality** (CL4-2): default for incident reporting, testing, and third-party risk.
- **Art. 4(3) — CA-review proportionality** (CL4-3): meta-provision requiring CAs to consider proportionality when reviewing the framework.
The three regimes are **not symmetric**: Art. 4(1) is self-implementing (the entity applies it directly); Art. 4(2) defers to chapter-specific clauses (Art. 16 simplification, Art. 25(3) microenterprise exception); Art. 4(3) is addressed to CAs.
- **Berry anchor:** §3.3.1 (`principle of proportionality`); §5.1 (`proportionate`).
- **Structural implication:** the proportionality overlay is **inherited by every Ch. II–V Sec. I clause** in v0.2. Every clause card in `02b`–`05a` carries `proportionality-status: Art. 4 applies`. The v0.2 convention was established in the pilot file (`01_DORA_Art3_Definitions.md` §2 note on Art. 4).
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

- **Cross-regulation consistency:** Art. 4's proportionality pattern mirrors **NIS 2 Art. 1(2)** (proportionality in scope) and **CRA Art. 1(2)** (proportionality for microenterprises and SMEs). DORA Art. 4 is more elaborate than either, providing explicit CA-review (CL4-3) that NIS 2 and CRA do not have.


<!-- aegis:purity: own_reg=DORA; demoted=3; core_cross_mentions=0 -->

