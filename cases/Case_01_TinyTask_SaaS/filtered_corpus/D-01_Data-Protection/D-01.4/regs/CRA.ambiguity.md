# D-01.4 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.5 CRA-CL141 — Part I (2)(l) — Logging and monitoring
**Source locus:**
> provide security related information by **recording and monitoring relevant internal activity**, including the access to or modification of data, services or functions, **with an opt-out mechanism for the user**;
**Instance 1 — VAG — S2 — `relevant internal activity`**
`relevant` — to what?
- **R1:** Security-relevant only.
- **R2:** All activity (audit log).
- **R3:** Risk-based.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Security-relevant | In-Directive: literal `security related` |
| R2 | All | None in OJ |
| R3 | Risk-based | In-Directive: Art. 13(2) risk assessment |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant`).
**Instance 2 — VAG — S2 — `opt-out mechanism for the user`**
User can opt out of logging? The reading:
- **R1:** User can disable logging entirely.
- **R2:** User can limit logging scope.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Disable entirely | In-Directive: literal `opt-out` |
| R2 | Limit scope | None in OJ |
| R3 | Both | None in OJ |
---

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

R1 is the literal reading. S2. **Cross-reference to Art. 21(2)(j) NIS 2** where the opt-out is also present.

<!-- aegis:purity: own_reg=CRA; demoted=1; core_cross_mentions=0 -->

