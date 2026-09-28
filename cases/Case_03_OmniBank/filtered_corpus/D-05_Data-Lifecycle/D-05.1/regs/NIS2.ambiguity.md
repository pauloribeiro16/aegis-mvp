# D-05.1 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.1 NIS2-CL52 — Art. 25(1) — Member State encouragement of standards
**Source locus:**
> In order to promote the convergent implementation of Article 21(1) and (2), Member States shall, **<mark>without imposing or discriminating in favour of the use of a particular type of technology</mark>**, encourage the use of European and international standards and technical specifications relevant to the security of network and information systems.
**Instance 1 — VAG — S2 — `shall … encourage`**
Same `shall encourage` pattern as Art. 20(2) (NIS2-CL05) and Art. 24(1) (NIS2-CL49). Discretionary encouragement; not binding.
*Berry anchor:* §3.3.1 (`shall encourage`).
**Instance 2 — VAG — S2 — `without imposing or discriminating in favour of the use of a particular type of technology`**
The technology-neutrality clause. Three readings:
- **R1:** MS must not require a specific technology.
- **R2:** MS must not favour one technology over another.
- **R3:** Both (comprehensive technology-neutrality).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Non-imposition | In-Directive: literal `without imposing` |
| R2 | Non-discrimination | In-Directive: literal `discriminating in favour of` |
| R3 | Both | In-Directive: literal `or` (inclusive) |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`without imposing`); §5.4.7 (OR).
**Instance 3 — VAG — S2 — `European and international standards and technical specifications`**
The OR between European and international, with `and technical specifications` as an addition.
- **R1:** European standards.
- **R2:** International standards.
- **R3:** Either.
- **R4:** Plus technical specifications (always).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | European | In-Directive: literal |
| R2 | International | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
| R4 | Plus specs | In-Directive: literal `and technical specifications` |
R3 + R4 combined. S2.
*Berry anchor:* §5.4.7 (OR + AND).
**Instance 4 — VAG — S2 — `relevant to the security of network and information systems`**
`relevant` — relevant to which version? Relevant to which domain?
- **R1:** All standards relevant to NIS.
- **R2:** Standards explicitly adopted by ENISA.
- **R3:** Standards in the European/international catalogue (Reg. 1025/2012).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All NIS-relevant | In-Directive: literal `relevant` |
| R2 | ENISA-adopted | None in OJ |
| R3 | Catalogue | In-Directive: Art. 6(16)/(17) cross-ref |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`relevant`).
---
#### 3.2 NIS2-CL53 — Art. 25(2) — ENISA advice and guidelines
**Source locus:**
> ENISA, in cooperation with Member States, and, where appropriate, after consulting relevant stakeholders, shall draw up **<mark>advice and guidelines</mark>** regarding the technical areas to be considered in relation to paragraph 1 as well as regarding already existing standards, including national standards, which would allow for those areas to be covered.
**Instance 1 — VAG — S2 — `shall draw up`**
`shall draw up` is mandatory (vs. `may`). ENISA is obliged to produce advice/guidelines.
*Berry anchor:* §3.3.1 (`shall draw up`).
**Instance 2 — POLY — S2 — `advice and guidelines`**
Two outputs (AND). Three readings:
- **R1:** Both required.
- **R2:** Either (substitution).
- **R3:** Composite (a single output: "advice-and-guidelines").
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both | In-Directive: literal |
| R2 | Either | None in OJ |
| R3 | Composite | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`advice`/`guidelines`); §5.4.7 (AND).
**Instance 3 — VAG — S2 — `where appropriate, after consulting relevant stakeholders`**
Same soft-hedge + consultation pattern as Art. 22(2) (CL25).
*Berry anchor:* §5.1 (`where appropriate`); §3.3.1 (`relevant stakeholders`).
**Instance 4 — VAG — S2 — `the technical areas to be considered`**
`technical areas` — defined how? By ENISA? By standards catalogue?
- **R1:** ENISA-defined.
- **R2:** Standards-catalogue-derived.
- **R3:** Both.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ENISA | In-Directive: literal `ENISA … shall draw up` |
| R2 | Catalogue | None in OJ |
| R3 | Both | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`technical areas`).
**Instance 5 — VAG — S2 — `including national standards`**
`including` — illustrative (Berry `include` pattern). National standards are an example; not exhaustive.
*Berry anchor:* §5.1 (`including`).
---
### 4. Cross-clause structural observations (Art. 25)
1. **Art. 25 is encouragement-only.** No binding entity obligation. The article's operational impact is on the entity's evidence base: standards cited in Art. 25(1) and ENISA guidelines produced under Art. 25(2) are non-mandatory but provide a soft path to Art. 21 compliance.
2. **The technology-neutrality clause is the most distinctive single phrase.** `without imposing or discriminating in favour of the use of a particular type of technology` is the only explicit technology-neutrality mandate in Chapter IV. It is a structural commitment to standards-based (not technology-specific) regulation.
3. **ENISA's `shall draw up advice and guidelines` is one of the few mandatory provisions on ENISA in Chapter IV.** Most ENISA references in Chapter IV are `may` (Art. 21(5), Art. 22(1), Art. 23(11), Art. 24(3)). Art. 25(2) is `shall draw up` — a positive obligation.
---
### 5. T3-to-v0.2 mapping
T3 had no clause for Art. 25 — it was outside the T3 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 25 with 2 atomic clauses (CL52–CL53).
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | NIS2-CL52 | Art. 25(1) | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL53 | Art. 25(2) | T3 omitted; v0.2 adds. |
---
**End of Art. 25 file. Next: `99_NIS2_Synthesis.md`.**

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.ambiguity.md

4. **Cross-regulation parallel.** Art. 25 mirrors the standardisation provisions in CRA Art. 27 (presumption of conformity via harmonised standards) and AI Act Art. 40 (conformity assessment via harmonised standards). The `European and international standards and technical specifications` triplet is the standard cross-regulation formulation.

<!-- aegis:purity: own_reg=NIS2; demoted=1; core_cross_mentions=0 -->