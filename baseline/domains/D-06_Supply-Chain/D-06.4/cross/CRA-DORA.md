# D-06.4 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 23(1)/(2)):**
> (See NIS2↔CRA pair above for the verbatim text.)

**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> (See GDPR↔DORA pair above for the verbatim text.)

**Scope comparison:**
- CRA scope: economic-operator identification duty (operator-side).
- DORA scope: audit rights on financial-entity-side over critical providers.
- Scope overlap: **N (typically) — different mechanisms, different directions.** Both apply when a CRA-classified product is supplied to a financial entity via an importer / distributor.

**Trigger comparison:**
- CRA trigger: per-MSA-identification-request + 10-year retention.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- CRA: Art. 23(2) 10-year retention.
- DORA: CIF-only audit rights.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: financial entity + competent authority.

**Content template comparison:**
- CRA: Art. 23 supply-chain identification log (10-year retention).
- DORA: Art. 30(3)(e)(i) audit-rights clause.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** CRA Art. 23(1) imposes an *identification duty on economic operators* (they must identify upstream supplier and downstream recipient); DORA Art. 30(3)(e) imposes *audit rights on financial entities* over critical providers. Different mechanisms: CRA = operator-side identification obligation; DORA = financial-entity-side rights. Both apply when a CRA-classified product is supplied to a financial entity via an importer / distributor.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms, distinct directions.**

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) CRA economic-operator identification log (10-year retention); (2) DORA audit-rights clause for CIF contracts. The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-063, Art. 23(1)/(2)) | Economic-operator identification + 10-year retention |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-063 |
| **DORA** (SR-DORA-022, Art. 30(3)(e)) | Unrestricted audit rights over critical ICT third-party providers |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-022 |

**Why different-perspective**: CRA Art. 23(1) imposes an *identification duty on economic operators* (they must identify upstream supplier and downstream recipient); DORA Art. 30(3)(e) imposes *audit rights on financial entities* over critical providers. Different mechanisms: CRA = operator-side identification obligation; DORA = financial-entity-side rights. Both apply when a CRA-classified product is supplied to a financial entity via an importer/distributor.



