# D-10.3 — Relevant Ambiguity (CRA)

> Part 4 ambiguity analysis for CRA, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## CRA
#### 2.1 CRA-CL124 — Art. 32(2) — Class I conformity assessment
**Source locus:**
> Where, in assessing the compliance of an important product with digital elements that falls under class I as set out in Annex III and the processes put in place by its manufacturer with the essential cybersecurity requirements set out in Annex I, the manufacturer has not applied or has applied only in part harmonised standards, common specifications or European cybersecurity certification schemes at assurance level at least 'substantial' as referred to in Article 27, or where such harmonised standards, common specifications or European cybersecurity certification schemes do not exist, the product with digital elements concerned and the processes put in place by the manufacturer shall be submitted with regard to those essential cybersecurity requirements to either of the following procedures: (a) the EU-type examination procedure (based on module B) … followed by conformity to EU-type based on internal production control (based on module C) …; or (b) a conformity assessment based on full quality assurance (based on module H) ….
**Instance 1 — VAG — S3 — `has not applied or has applied only in part`**
The trigger for third-party assessment.
- **R1:** Not applied at all.
- **R2:** Applied only in part.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Not at all | In-Directive: literal |
| R2 | Only in part | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`applied only in part`).
**Instance 2 — POLY — S2 — `harmonised standards, common specifications or European cybersecurity certification schemes`**
Three alternative conformity routes (OR).
- **R1:** Harmonised standards only.
- **R2:** Common specifications only.
- **R3:** Certification schemes only.
- **R4:** Any combination.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Standards | In-Directive: Art. 27(1) |
| R2 | Common specs | In-Directive: Art. 27(2) |
| R3 | Certification | In-Directive: Art. 27(8) |
| R4 | Any | In-Directive: literal `or` |
R4 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 2.2 CRA-CL125 — Art. 32(3) — Class II conformity assessment
**Source locus:**
> Where the product is an important product with digital elements that falls under class II as set out in Annex III, the manufacturer shall demonstrate conformity with the essential cybersecurity requirements set out in Annex I by using any of the following procedures: (a) EU-type examination procedure (based on module B) … followed by conformity to EU-type based on internal production control (based on module C) …; (b) a conformity assessment based on full quality assurance (based on module H) …; or (c) where available and applicable, a European cybersecurity certification scheme pursuant to Article 27(9) of this Regulation at assurance level at least 'substantial' ….
**Instance 1 — VAG — S3 — `at assurance level at least 'substantial'`**
The assurance-level threshold.
- **R1:** Level "substantial" is the minimum.
- **R2:** Higher levels may be required.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Substantial minimum | In-Directive: literal `at least` |
| R2 | Higher per Commission | In-Directive: Art. 27(9) delegated acts |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`at least`).
---
#### 2.3 CRA-CL127 — Art. 32(5) — FOSS simplified conformity assessment
**Source locus:**
> Manufacturers of products with digital elements qualifying as free and open-source software, which fall under the categories set out in Annex III, shall be able to demonstrate conformity with the essential cybersecurity requirements set out in Annex I by using one of the procedures referred to in paragraph 1 of this Article, provided that the technical documentation referred to in Article 31 is made available to the public at the time of the placing on the market of those products.
**Instance 1 — VAG — S2 — `made available to the public`**
`to the public` — any public? or a specific public?
- **R1:** Any public access (website, repository).
- **R2:** MSA-accessible (on request).
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any public | In-Directive: literal |
| R2 | MSA | None in OJ |
| R3 | Both | In-Directive: literal |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`to the public`).
---
### 3. T3-to-v0.2 mapping
T3 had no clauses for Art. 27–32. The v0.2 expansion adds 21 atomic clauses (CL108–CL128).
---
**End of Art. 27–32 file. Next: `09_CRA_AnnexI_EssentialRequirements.md`.**
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
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
#### CRA-CL173 — Ann. VIII Part II (6) — EU-type certificate
**Source locus:**
> Where the type and the vulnerability handling processes meet the essential cybersecurity requirements set out in Annex I, the notified body shall issue an EU-type examination certificate to the manufacturer. The certificate shall contain the name and address of the manufacturer, the conclusions of the examination, the conditions (if any) for its validity and the necessary data for identification of the approved type and vulnerability handling processes. The certificate may have one or more annexes attached. … Where the type and the vulnerability handling processes do not satisfy the applicable essential cybersecurity requirements set out in Annex I, the notified body shall refuse to issue an EU-type examination certificate and shall inform the applicant accordingly, giving detailed reasons for its refusal.
**Instance 1 — VAG — S2 — `conditions (if any) for its validity`**
`conditions` — what conditions?
- **R1:** Periodic review conditions.
- **R2:** Change-management conditions.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Periodic review | None in OJ |
| R2 | Change-management | In-Directive: Ann. VIII Part II (7) modifications |
| R3 | Both | None in OJ |
R2 is the dominant reading (Part II (7) covers modifications). S2.
---
### 4. T3-to-v0.2 mapping
T3 had no clauses for Annex VIII. The v0.2 expansion adds 9 atomic clauses (CL168–CL176).
---
**End of Annex VIII file. Next: `99_CRA_Synthesis.md`.**

<!-- aegis:purity: own_reg=CRA; demoted=0; core_cross_mentions=0 -->

