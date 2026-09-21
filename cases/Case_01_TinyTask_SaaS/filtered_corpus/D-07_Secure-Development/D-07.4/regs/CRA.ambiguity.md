# D-07.4 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
#### 3.16 CRA-CL46 — Art. 13(21) — Corrective measures
**Source locus:**
> From the placing on the market and for the support period, manufacturers who know or have reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity with the essential cybersecurity requirements set out in Annex I shall **immediately take the corrective measures** necessary to bring that product with digital elements or the manufacturer's processes into conformity, or to withdraw or recall the product, as appropriate.
**Instance 1 — VAG — S2 — `immediately take`**
`immediately` — without delay? Same as `without undue delay`?
- **R1:** Without delay (any operational time).
- **R2:** Within 24h (same as Art. 14).
- **R3:** As soon as discovered.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Without delay | In-Directive: literal `immediately` |
| R2 | 24h | None in OJ |
| R3 | As soon as discovered | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`immediately`).
**Instance 2 — POLY — S2 — `corrective measures`**
What kind of measures?
- **R1:** Fix the product.
- **R2:** Update documentation.
- **R3:** Withdraw the product.
- **R4:** Recall the product.
- **R5:** Any combination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Fix | In-Directive: literal `bring … into conformity` |
| R2 | Update docs | None in OJ |
| R3 | Withdraw | In-Directive: literal |
| R4 | Recall | In-Directive: literal |
| R5 | Any | In-Directive: literal `as appropriate` |
R5 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`corrective measures`); §5.4.7 (OR).
---
### 4. Cross-clause structural observations (Art. 13)
1. **Art. 13(2) is the operational core of the manufacturer's risk-assessment duty.** The 6-phase lifecycle propagation (CL16) is the **longest single coordination pattern in CRA** — 6 phases coordinated by AND. Berry §5.5 parallelism admits partial-compliance readings.
2. **Art. 13(8) is the support-period architecture.** Three layered obligations: (a) handle vulnerabilities during support (CL27), (b) determine support period based on factors (CL28), (c) minimum 5 years (CL29). Combined with Art. 13(9) 10-year update availability (CL33), the **effective manufacturer obligation is a 10-year tail** that survives the support period.
3. **Art. 13(5) is the supply-chain due-diligence hook (Q6=b split).** T2 misattributed this clause to Art. 13(13)'s 10-year documentation retention. The v0.2 split places the actual Art. 13(5) due-diligence analysis here (CL23a) and the 10-year retention in CL38.
5. **`reasonable user expectations` (CL28) is the cross-regulation Berry-classic.** Same term-pattern as `reasonable foreseeability` in Art. 3(24)/(25). Layer 1 catalogues; Layer 2 must adjudicate against product-liability case law.
6. **6 S3 clauses (CL15, CL16, CL18, CL19, CL23a, CL27, CL28, CL33, CL42):** risk assessment, 6-phase propagation, documentation, intended purpose + foreseeability, due diligence, support-period factors, 10-year updates, single point of contact. **No S1 instances.**
7. **The Q6=b split resolves the T2-C24 mapping error.** T2-C24's "10-year documentation" substance is actually Art. 13(13) (CL38), not Art. 13(5). T2-C24's "due diligence" substance (which it didn't capture) is actually Art. 13(5) (CL23a). The v0.2 split surfaces both clauses.
---
### 5. T3-to-v0.2 mapping
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| CRA-C22 | Art. 13(1) | CRA-CL14 | Art. 13(1) | Same locus. |
| CRA-C22 (continued) | Art. 13(2) | CRA-CL15, CL16, CL17 | Art. 13(2) | v0.2 expands 6-phase + health/safety. |
| CRA-C23 | Art. 13(3)–(4) | CRA-CL18, CL19, CL20, CL21, CL22 | Art. 13(3)–(4) | v0.2 expands risk-assessment content. |
| **CRA-C24** | **Art. 13(5)** (T2 mis-attributed: it described Art. 13(13)) | **CRA-CL23a (Art. 13(5) due diligence) + CRA-CL38 (Art. 13(13) 10-year retention)** | Art. 13(5) and Art. 13(13) | **Per Q6=b: v0.2 splits T2-C24 mapping error into two clauses.** |
| (none) | — | CRA-CL24, CL25 | Art. 13(6) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL26 | Art. 13(7) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL27, CL28, CL29, CL30, CL31, CL32 | Art. 13(8) | T3 omitted; v0.2 expands into 6 atomic clauses. |
| (none) | — | CRA-CL33 | Art. 13(9) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL34, CL35 | Art. 13(10), (11) | T3 omitted; v0.2 adds. |
| (none) | — | CRA-CL36, CL37 | Art. 13(12) | T3 omitted; v0.2 adds. |
| (T2 mis-attributed to 13(5)) | (T2 mis-attributed) | CRA-CL38 | Art. 13(13) | **Per Q6=b: substance migrated here from T2-C24.** |
| (none) | — | CRA-CL39–CL50 | Art. 13(14)–(25) | T3 omitted; v0.2 adds 12 clauses. |
**Net: 3 T3 clauses → 36 v0.2 clauses (T3 missed 33 of the 36 Article 13 clauses; 1 T3 mapping error resolved via Q6=b).**
---
**End of Art. 13 file. Pilot complete.**
- `05_CRA_Art15-17_OtherReporting.md`
- `06_CRA_Art18-23_EconomicOperators.md`
- `07_CRA_Art24-26_OSS.md`
- `08_CRA_Art27-32_Conformity.md`
- `09_CRA_AnnexI_EssentialRequirements.md` (the binding core)
- `10_CRA_AnnexII_Instructions.md`
- `11_CRA_AnnexVII_TechDocumentation.md`
- `12_CRA_AnnexVIII_ConformityModules.md`
- `99_CRA_Synthesis.md`
- Global `00_Index.md` update + legacy `../Regulation/CRA/Ambiguity/03_CRA.md` annotation
#### 2.1 CRA-CL96 — Art. 21 — Manufacturer-equivalent trigger
**Source locus:**
> An importer or distributor shall be considered to be a manufacturer for the purposes of this Regulation and shall be subject to Articles 13 and 14, where that importer or distributor places a product with digital elements on the market **under its name or trademark** or carries out a **substantial modification** of a product with digital elements already placed on the market.
**Instance 1 — VAG — S3 — `under its name or trademark`**
`name or trademark` — what constitutes "under its name"?
- **R1:** Rebranding (white-label).
- **R2:** Co-branding.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | White-label | In-Directive: literal |
| R2 | Co-brand | None in OJ |
| R3 | Either | In-Directive: literal `under its name or trademark` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`name or trademark`).
**Instance 2 — VAG — S3 — `substantial modification`**
Inherits Art. 3(30) D30. Same POLY (affects compliance / modifies intended purpose). Propagates.
- **R1:** Any non-compliance change.
- **R2:** Material compliance change.
- **R3:** Intended-purpose modification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any | In-Directive: Art. 3(30) literal |
| R2 | Material | None in OJ |
| R3 | Intended-purpose | In-Directive: Art. 3(30) OR |
R1/R3 are the literal reading (OR). S3.
*Berry anchor:* §3.3.1; §5.4.7 (OR).
---
#### 2.2 CRA-CL97 — Art. 22(1) — Third-party substantial modification
**Source locus:**
> A natural or legal person, other than the manufacturer, the importer or the distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market, shall be considered to be a manufacturer for the purposes of this Regulation.
**Instance 1 — POLY — S2 — `other than the manufacturer, the importer or the distributor`**
Exclusion list. Who is left?
- **R1:** Third-party integrators.
- **R2:** System integrators.
- **R3:** Any person not already classified.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Third-party integrators | In-Directive: literal |
| R2 | System integrators | None in OJ |
| R3 | Any | In-Directive: literal `other than` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`other than`).
**Instance 2 — VAG — S2 — `carries out a substantial modification`**
`carries out` — performs the modification? authorises the modification?
- **R1:** Performs.
- **R2:** Authorises.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Performs | In-Directive: literal |
| R2 | Authorises | None in OJ |
| R3 | Either | In-Directive: literal |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`carries out`).
**Instance 3 — SCOPE-Q — S2 — `for the part of the product with digital elements that is affected by the substantial modification or, if the substantial modification has an impact on the cybersecurity of the product with digital elements as a whole, for the entire product`**
Scope of the obligation — part or whole.
- **R1:** Affected part only.
- **R2:** Entire product.
- **R3:** Either (depending on impact).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Part | In-Directive: literal |
| R2 | Entire | In-Directive: literal `if … has an impact on the cybersecurity … as a whole` |
| R3 | Either | In-Directive: literal |
R1/R3 are the literal reading (OR). S2.
*Berry anchor:* §3.3.1 (`affected`); §5.4.7 (OR).
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

4. **Art. 13(2) sentence 2 is CRA-unique.** The `health and safety of users` clause bridges cybersecurity to physical safety. No other regulation in the corpus (GDPR, NIS 2, DORA, AI Act) has this.

### from regs/CRA.ambiguity.md

Per the NIS 2 pattern, pausing here for your review before continuing with:

### from regs/CRA.ambiguity.md

- `04_CRA_Art14_Reporting.md` (the "Art. 23 NIS 2" analog)

<!-- aegis:purity: own_reg=CRA; demoted=3; core_cross_mentions=0 -->

