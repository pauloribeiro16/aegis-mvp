# D-07.4 — Relevant Ambiguity (NIS 2)

> Part 4 ambiguity analysis for NIS 2, verbatim from the merged
> file. Cross-regulation analogies are demoted to the trailing section.

## NIS2
#### 3.3 NIS2-CL25 — Art. 22(2) — Commission selection
**Source locus:**
> The Commission, after consulting the Cooperation Group and ENISA, and, where necessary, relevant stakeholders, **<mark>shall identify the specific critical ICT services, ICT systems or ICT products</mark>** that may be subject to the coordinated security risk assessment referred to in paragraph 1.
**Instance 1 — VAG — S2 — `shall identify`**
`shall identify` — identify on what basis?
- **R1:** Identify based on sectoral risk (Annex I/II).
- **R2:** Identify based on impact (cf. Art. 2(2)(c)–(d)).
- **R3:** Identify based on stakeholder input (`where necessary, relevant stakeholders`).
- **R4:** Identify based on Commission discretion.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sectoral | In-Directive: Annex I/II |
| R2 | Impact-based | In-Directive: Art. 2(2)(c)–(d) |
| R3 | Stakeholder-input | In-Directive: literal `where necessary, relevant stakeholders` |
| R4 | Discretionary | In-Directive: literal `shall identify` is Commission-driven |
R4 is the literal reading; R3 is a procedural modifier on R4. S2.
*Berry anchor:* §3.3.1 (`shall identify`).
**Instance 2 — POLY — S2 — `specific critical ICT services, ICT systems or ICT products`**
The same `specific critical ICT` OR list as in CL23. Inherits the same readings.
*Berry anchor:* §3.3.1; §5.4.7 (OR).
**Instance 3 — VAG — S2 — `where necessary, relevant stakeholders`**
`where necessary` — soft hedge; `relevant stakeholders` — who counts as relevant?
- **R1:** Industry associations.
- **R2:** Specific entities (manufacturers, operators).
- **R3:** Standards bodies / ENISA partners.
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Industry | None in OJ |
| R2 | Specific entities | None in OJ |
| R3 | Standards bodies | None in OJ |
| R4 | All | None in OJ |
R4 is the literal reading. S2.
*Berry anchor:* §5.1 (`where necessary`); §3.3.1 (`relevant stakeholders`).
---
### 4. Cross-clause structural observations (Art. 22)
1. **Art. 22 is short and discretionary.** Only 2 paragraphs; the central verb is `may` (CL23) or `shall identify` (CL25). The Cooperation Group has wide latitude; the Commission has the selection power. The operational impact is on entities only via Art. 21(3) sentence 2 propagation (NIS2-CL21 in the Art. 21 file).
2. **`specific critical ICT services, ICT systems or ICT products` recurs in CL23 and CL25.** The phrase is the EU-level supply-chain scope. The Commission selects the targets; the Cooperation Group assesses. Entities have no direct obligation under Art. 22 but inherit the propagation through Art. 21(3).
3. **`technical and, where relevant, non-technical risk factors`** is the same Berry `AND with hedge` pattern as Art. 21(2)(h) `cryptography and, where appropriate, encryption` and Art. 21(2)(j) `where appropriate`. The directive consistently uses soft hedges on the non-cyber/optional side of binary terms. **Cross-clause pattern.**
4. **No directly entity-facing obligation in Art. 22 itself.** The propagation is via Art. 21(3) sentence 2 (NIS2-CL21 in the Art. 21 file), which requires entities to "take into account the results of the coordinated security risk assessments". This is the most consequential propagation chain in Chapter IV for the supply-chain theme.
---
### 5. T3-to-v0.2 mapping
T3 had no clause for Art. 22 — it was outside the T3 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 22 with 3 atomic clauses (CL23–CL25).
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | NIS2-CL23 | Art. 22(1) sentence 1 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL24 | Art. 22(1) sentence 2 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL25 | Art. 22(2) | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL21 (in Art. 21 file) | Art. 21(3) sentence 2 | The propagation hook — entities take into account the results of Art. 22 assessments. T3 omitted this propagation. |
---
**End of Art. 22 file. Next: `05_NIS2_Art23_Reporting.md` (the most consequential after Art. 21).**

<!-- aegis:purity: own_reg=NIS2; demoted=0; core_cross_mentions=0 -->