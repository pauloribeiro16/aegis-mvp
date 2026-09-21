# D-10.2 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
#### 3.8 CRA-CL21–CL22 — Art. 13(4) — Technical documentation inclusion + AI carve-out
(Summarised — full analysis in dedicated file.)
**Instance 1 — VAG — S2 — `technical documentation required pursuant to Article 31 and Annex VII`**
Cross-reference. Inherits Art. 31 + Annex VII specifications.
*Berry anchor:* §3.3.1 (`technical documentation`).
**Instance 2 — POLY — S2 — `cybersecurity risk assessment may be part of the risk assessment required by those Union legal acts`**
- **R1:** Optional (entity choice).
- **R2:** Encouraged but not required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Optional | In-Directive: literal `may` |
| R2 | Encouraged | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`may`).
---
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
#### 3.9 CRA-CL145 — Part II (3) — Security testing
**Source locus:**
> apply **effective and regular tests and reviews** of the security of the product with digital elements;
**Instance 1 — VAG — S3 — `effective and regular`**
Two qualifiers.
- **R1:** `effective` = test detects real vulnerabilities. `regular` = periodic.
- **R2:** `effective` = test is comprehensive. `regular` = ad-hoc.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Detect + periodic | None in OJ |
| R2 | Comprehensive + ad-hoc | None in OJ |
S3.
*Berry anchor:* §5.1 (`effective`, `regular`).
**Instance 2 — VAG — S2 — `tests and reviews`**
Two activities (AND).
- **R1:** Both (automated tests + manual reviews).
- **R2:** Either (automated tests OR manual reviews).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
---
## CRA v0.2 — Annex VIII Conformity Assessment Procedures
> **Source.** OJ L, 20.11.2024, p. 75–80. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4426–4769.
>
> **Pattern.** Key clauses quoted, then per-clause analysis.
>
> **Annex VIII defines three conformity-assessment modules:** Module A (internal control), Module B+C (EU-type examination + internal production control), Module H (full quality assurance). Art. 32 routes products to modules based on classification.
---
### 1. Module architecture
| Module | Part | Name | Role |
|---|---|---|---|
| **A** | I | Internal control | Manufacturer self-assessment. |
| **B** | II | EU-type examination | Notified body examines design + vuln handling. |
| **C** | III | Internal production control | Manufacturer controls production per EU-type. |
| **B+C** | II + III | EU-type + production control | Notified body examines design; manufacturer controls production. |
| **H** | IV | Full quality assurance | Notified body audits QMS. |
---
### 2. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL168 | Ann. VIII Part I (1) | Module A duty | **S2** | Manufacturer self-declares compliance; sole responsibility. |
| CRA-CL169 | Ann. VIII Part I (2) | Tech docs (Module A) | **S2** | Draw up Annex VII documentation. |
| CRA-CL170 | Ann. VIII Part I (3) | Design/production/vuln (Module A) | **S2** | Manufacturer takes all measures for design/dev/production/vuln compliance. |
| CRA-CL171 | Ann. VIII Part II (1) | Module B definition | **S2** | Notified body examines design + vuln handling; attests compliance. |
| CRA-CL172 | Ann. VIII Part II (3) | Module B application | **S2** | Application to single notified body. |
| CRA-CL173 | Ann. VIII Part II (6) | EU-type certificate | **S2** | Notified body issues certificate; may refuse and inform. |
| CRA-CL174 | Ann. VIII Part II (8) | Module B periodic audits | **S2** | Periodic audits of vuln handling processes. |
| CRA-CL175 | Ann. VIII Part III (1) | Module C definition | **S2** | Manufacturer controls production per EU-type. |
| CRA-CL176 | Ann. VIII Part IV (1) | Module H definition | **S2** | Full quality assurance; notified body audits QMS. |
**Total: 9 atomic clauses for Annex VIII.**
---
### 3. Selected instance

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.ambiguity.md

The AI Act carve-out: risk assessment can be unified across CRA + AI Act.

### from regs/CRA.ambiguity.md

R1 is the literal reading. S2. **Cross-reference to Art. 21(2)(j) NIS 2** where the opt-out is also present.

<!-- aegis:purity: own_reg=CRA; demoted=2; core_cross_mentions=0 -->

