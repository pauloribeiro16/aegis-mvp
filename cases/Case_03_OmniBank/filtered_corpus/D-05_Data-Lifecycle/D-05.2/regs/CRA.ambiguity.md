# D-05.2 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
#### 3.14 CRA-CL33 — Art. 13(9) — 10-year update availability
**Source locus:**
> Manufacturers shall ensure that each security update … remains available after it has been issued for a **minimum of 10 years or for the remainder of the support period, whichever is longer**.
**Instance 1 — VAG — S2 — `whichever is longer`**
The 10-year vs remainder-of-support comparison.
- **R1:** Always 10 years minimum.
- **R2:** May be longer if support period > 10.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 10-year floor | In-Directive: literal `minimum of 10 years` |
| R2 | Support-period floor | In-Directive: literal `whichever is longer` |
R2 is the literal reading. S2.
*Berry anchor:* §5.7 (temporal).
**Instance 2 — POLY — S2 — `security update`**
`security update` — patch? firmware update? configuration change?
- **R1:** Patch.
- **R2:** Firmware.
- **R3:** Configuration.
- **R4:** Any.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Patch | None in OJ |
| R2 | Firmware | None in OJ |
| R3 | Configuration | None in OJ |
| R4 | Any | In-Directive: literal `security update` |
R4 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`security update`).
---
#### 3.7 CRA-CL61 — Art. 14(5)(a) — Severe-incident test A
**Source locus:**
> **(a)** it **negatively affects or is capable of negatively affecting** the ability of a product with digital elements to protect the availability, authenticity, integrity or confidentiality of **sensitive or important data or functions**; or
**Instance 1 — VAG — S3 — `negatively affects or is capable of negatively affecting`**
- **R1:** Past only (already affected).
- **R2:** Potential only (capable of affecting).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Past | In-Directive: literal |
| R2 | Potential | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR).
**Instance 2 — POLY — S2 — `sensitive or important data or functions`**
`data or functions` (same as Art. 3(44)) + `sensitive or important` (undefined qualifier).
- **R1:** `sensitive` = personal data.
- **R2:** `sensitive` = critical business data.
- **R3:** `sensitive` = any data whose loss has consequences.
- **R4:** `important` = essential to product function.
- **R5:** `important` = significant to user operations.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Personal data | None in OJ |
| R2 | Critical business | None in OJ |
| R3 | Consequential | None in OJ |
| R4 | Essential to product | None in OJ |
| R5 | Significant to user | None in OJ |
R5 is the broadest reading. S2.
*Berry anchor:* §3.3.1 (`sensitive`/`important`).
**Instance 3 — COORD — S3 — `sensitive OR important` (OR of two qualifiers)**
- **R1:** `sensitive` only.
- **R2:** `important` only.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sensitive | In-Directive: literal |
| R2 | Important | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR).
**Instance 4 — POLY — S2 — `availability, authenticity, integrity or confidentiality`**
---
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

Same pattern as NIS 2 Art. 23(3) `caused or is capable of causing`. Actual vs potential.

### from regs/CRA.ambiguity.md

Same four dimensions as NIS 2 Art. 6(2) D02. Inherits same POLY (authenticity undefined).

<!-- aegis:purity: own_reg=CRA; demoted=2; core_cross_mentions=0 -->