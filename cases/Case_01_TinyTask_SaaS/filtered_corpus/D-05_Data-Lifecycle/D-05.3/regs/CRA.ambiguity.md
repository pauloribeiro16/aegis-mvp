# D-05.3 — Relevant Ambiguity (CRA)

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
#### 3.6 CRA-CL142 — Part I (2)(m) — Secure deletion
**Source locus:**
> provide the possibility for users to **securely and easily remove on a permanent basis all data and settings** and, where such data can be transferred to other products or systems, ensure that this is done in a secure manner.
**Instance 1 — VAG — S2 — `securely and easily`**
Two qualifiers (AND).
- **R1:** Both must be satisfied (secure AND easy).
- **R2:** Secure takes priority over easy.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal `and` |
| R2 | Secure priority | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.4.7 (AND).
**Instance 2 — VAG — S2 — `permanent basis`**
`permanent` — what level of irrecoverability?
- **R1:** Cryptographic erasure (key deletion).
- **R2:** Physical destruction (storage wipe).
- **R3:** Any method that makes recovery infeasible.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Crypto erasure | None in OJ |
| R2 | Physical wipe | None in OJ |
| R3 | Infeasible recovery | None in OJ |
R3 is the literal reading. S2.
---
#### 3.3 CRA-CL158 — Ann. II §8 — Instructions
**Source locus:**
> detailed instructions or an internet address referring to such detailed instructions and information on: (a) … (f) …
**Instance 1 — VAG — S2 — `detailed instructions`**
`detailed` — how detailed?
- **R1:** Complete security guide.
- **R2:** Summary of key points.
- **R3:** Context-dependent (based on product complexity).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Complete guide | In-Directive: literal `detailed` |
| R2 | Summary | None in OJ |
| R3 | Context-dependent | In-Directive: Art. 13(8) support period context |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`detailed`).
**Instance 2 — SCOPE-Q — S2 — `or an internet address referring to such detailed instructions`**
Alternative: physical document or URL.
- **R1:** Physical document sufficient.
- **R2:** URL sufficient.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Physical | In-Directive: literal `or` |
| R2 | URL | In-Directive: literal `internet address` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
**End of Annex II file. Next: `11_CRA_AnnexVII_TechDocumentation.md`.**

<!-- aegis:purity: own_reg=CRA; demoted=0; core_cross_mentions=0 -->

