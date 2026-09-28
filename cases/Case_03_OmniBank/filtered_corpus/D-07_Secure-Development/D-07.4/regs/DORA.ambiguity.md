# D-07.4 — Relevant Ambiguity (DORA)

> Part 4 ambiguity analysis for DORA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## DORA
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
#### 4.30 CL22-2 — Art. 22(2) — ESAs yearly aggregated report
**Source locus:** Art. 22(2).
> The ESAs shall, through the Joint Committee, on an **anonymised and aggregated basis, report yearly on major ICT-related incidents**, the details of which shall be provided by competent authorities in accordance with Article 19(6), setting out at least the **number of major ICT-related incidents, their nature and their impact on the operations of financial entities or clients, remedial actions taken and costs incurred**.
>
> The ESAs shall issue **warnings and produce high-level statistics** to support ICT threat and vulnerability assessments.
**Instance 1 — POLY — S3 — `anonymised AND aggregated basis`**
**Instance 2 — POLY — S2 — `yearly` (cadence)**
Same Berry `yearly` family (cf. DORA Art. 24(6) CL24-5 `at least yearly`). S2.
*Berry anchor:* §5.7 (temporal); §5.1 (`yearly`).
**Instance 3 — POLY — S2 — 5 enumerated reporting elements**
| Element | Key ambiguity | Berry anchor |
|---|---|---|
| `number of major ICT-related incidents` | Absolute vs. normalised | §3.3.1 |
| `their nature` | Vector (attack type) vs. impact type | §3.3.1 |
| `their impact on the operations of financial entities or clients` | Internal ops vs. client-side impact | §3.3.1 |
| `remedial actions taken` | Process vs. outcome | §3.3.1 |
| `costs incurred` | Direct only vs. direct+indirect | §3.3.1 |
S2 (per element). Aggregate S3 due to `at least` (`at least` suggests the list is open).
*Berry anchor:* §5.4.5 (`at least` open-list); §3.3.1.
**Instance 4 — VAG — S2 — `warnings and high-level statistics`**
`warnings` + `high-level statistics` — two ESA output types. S2.
*Berry anchor:* §3.3.1 (`warnings`, `high-level statistics`).
**Definitional anchor:** DORA-D10.
**Scope:** regulator-internal (between ESAs and the public).
**Proportionality-status:** Art. 4 applies.
---
#### 6.5 Art. 21 — single EU Hub feasibility report (RTS-style structural delegation)
Art. 21 mandates a **feasibility report** by the ESAs Joint Committee (in consultation with ECB and ENISA) on the potential centralisation of incident reporting through a **single EU Hub**. The report must comprise **7 elements** (a)–(g).
This is **not an obligation on financial entities** — it is a meta-procedural mandate on the ESAs. But its outcome (whether or not a single EU Hub is established) could materially alter the entity-side reporting architecture. As of Q1 2025 (post the 17 January 2025 deadline), the ESAs Joint Committee report was published; the legislative follow-up is uncertain.
- **Berry anchor:** §3.3.1 (`single EU Hub`); §5.1 (`feasibility`); §3.3.1 (`interoperability`).
- **Layer 1 catalogue only.** Layer 2 must surface the architectural implications (sensitive-information concentration, jurisdictional sovereignty, operational resilience of the hub).
#### 6.6 Art. 22 — supervisory feedback: discretionary vs. mandatory
Art. 22(1) specifies that the competent authority **may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance**. The `may` is the operative trigger. Three readings (CL22-1 Instance 1): R1 mandatory, R2 discretionary (literal), R3 default-with-exceptions. R2 is the literal reading.
- **Berry anchor:** §3.3.1 (`may`); §5.1 (`feasible`, `relevant`, `proportionate`).
- **Structural implication:** Art. 22(1) creates a **discretion gap** between reporting (mandatory, Art. 19) and supervisory response (discretionary, Art. 22). This is a **closed-loop asymmetry**: entities must report; CAs may respond.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.ambiguity.md

Same `anonymised and aggregated` pattern as NIS 2 CL45. S2 on anonymity/aggregation; S3 on the combination rule.

### from regs/DORA.ambiguity.md

*Berry anchor:* §5.4.7 (AND); §3.3.1 (`anonymised`, `aggregated`); cf. NIS 2 CL45.

### from regs/DORA.ambiguity.md

- **Structural implication:** the **single EU Hub** is structurally analogous to the **NIS 2 single point of contact (SPOC)** (NIS 2 Art. 12) and the **CER Directive critical-entity framework** but at a higher integration level.

### from regs/DORA.ambiguity.md

The structural pattern is **mandatory acknowledge + discretionary substance** — the CA must acknowledge receipt (per the `shall … acknowledge receipt and may … provide` coordination) but the substantive feedback is at CA discretion. This is **the opposite** of the NIS 2 Art. 23(5) pattern (mandatory CSIRT response within 24h), and is a deliberate DORA choice reflecting the CA-specific regulatory authority.

<!-- aegis:purity: own_reg=DORA; demoted=4; core_cross_mentions=0 -->