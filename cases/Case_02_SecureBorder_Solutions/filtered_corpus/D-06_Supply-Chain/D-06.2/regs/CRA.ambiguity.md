# D-06.2 — Relevant Ambiguity (CRA)

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
#### 3.7 CRA-CL143 — Part II (1) — SBOM
**Source locus:**
> identify and document vulnerabilities and components contained in products with digital elements, including by drawing up a **software bill of materials** in a commonly used and machine-readable format covering at the very least the **top-level dependencies** of the products;
**Instance 1 — VAG — S3 — `commonly used and machine-readable format`**
`commonly used` — which formats?
- **R1:** CycloneDX (OWASP).
- **R2:** SPDX (Linux Foundation).
- **R3:** Any machine-readable format.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CycloneDX | None in OJ |
| R2 | SPDX | None in OJ |
| R3 | Any | In-Directive: literal `commonly used` |
R3 is the literal reading. S3 because R1 vs R3 admit materially different compliance populations.
*Berry anchor:* §3.3.1 (`commonly used`).
**Instance 2 — VAG — S2 — `top-level dependencies`**
`top-level` — shallow vs deep.
- **R1:** First-level dependencies only (direct).
- **R2:** Transitive (all nested).
- **R3:** Critical dependencies only.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | First-level | In-Directive: literal `top-level` |
| R2 | Transitive | None in OJ |
| R3 | Critical | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`top-level`).
---
#### CRA-CL161 — Ann. VII §2(a) — System architecture
**Source locus:**
> a description of the system architecture explaining how software components build on or feed into each other and integrate into the overall processing;
**Instance 1 — VAG — S2 — `build on or feed into each other`**
Architectural description depth.
- **R1:** Component dependency graph.
- **R2:** Data flow diagram.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Dependency | In-Directive: literal `build on` |
| R2 | Data flow | In-Directive: literal `feed into` |
| R3 | Both | In-Directive: literal `or` |
R3 is the literal reading. S2.
---
**End of Annex VII file. Next: `12_CRA_AnnexVIII_ConformityModules.md`.**
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

<!-- aegis:purity: own_reg=CRA; demoted=0; core_cross_mentions=0 -->