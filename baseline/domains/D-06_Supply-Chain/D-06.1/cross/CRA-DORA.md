# D-06.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 13(5)):**
> "Manufacturers shall exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements." — CRA Art. 13(5)

**DORA article (verbatim, Art. 28(1)):**
> "Financial entities shall manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services …" — DORA Art. 28(1)

**Scope comparison:**
- CRA scope: third-party components at the product level (manufacturer's inputs).
- DORA scope: ICT third-party service providers at the entity level (financial entity's ICT providers).
- Scope overlap: **N (typically) — different levels of the supply chain.** CRA is upstream (manufacturer's inputs); DORA is midstream (deployer's ICT providers).

**Trigger comparison:**
- CRA trigger: per-component integration.
- DORA trigger: per-ICT-provider risk management.
- Trigger alignment: **DIFFERENT** — product-level vs entity-level.

**Threshold/timeline comparison:**
- CRA: "due diligence" (VAG+POLY-S3 R3 procedural + substantive).
- DORA: four-factor proportionality.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: competent authority.

**Content template comparison:**
- CRA: Annex VII §2 component-due-diligence record + SBOM.
- DORA: four-factor proportionality + Art. 30(2) 9-element contract.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** CRA component due diligence is product-level (manufacturer's third-party components); DORA ICT third-party risk is entity-level (financial entity's ICT service providers). The two are at different levels of the supply chain: CRA = upstream (manufacturer's inputs); DORA = midstream (deployer's ICT providers).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct actors, distinct objects, distinct triggers.** When a financial entity deploys a CRA-compliant product, the manufacturer (CRA-bound) and the deployer (DORA-bound) are typically different parties.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer record: (1) CRA manufacturer-side component due diligence; (2) DORA financial-entity-side ICT third-party risk. The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-050, Art. 13(5)) | Third-party component due diligence |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-050 |
| **DORA** (SR-DORA-019, Art. 28(1)) | ICT third-party risk under four-factor proportionality |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-019 |

**Why different-perspective**: CRA component due diligence is product-level (manufacturer's third-party components); DORA ICT third-party risk is entity-level (financial entity's ICT service providers). The two are at different levels of the supply chain: CRA = upstream (manufacturer's inputs); DORA = midstream (deployer's ICT providers).



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 13(5)):**
> "Manufacturers shall exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements." — CRA Art. 13(5)

**DORA article (verbatim, Art. 28(1)):**
> "Financial entities shall manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services …" — DORA Art. 28(1)

**Scope comparison:**
- CRA scope: third-party components at the product level (manufacturer's inputs).
- DORA scope: ICT third-party service providers at the entity level (financial entity's ICT providers).
- Scope overlap: **N (typically) — different levels of the supply chain.** CRA is upstream (manufacturer's inputs); DORA is midstream (deployer's ICT providers).

**Trigger comparison:**
- CRA trigger: per-component integration.
- DORA trigger: per-ICT-provider risk management.
- Trigger alignment: **DIFFERENT** — product-level vs entity-level.

**Threshold/timeline comparison:**
- CRA: "due diligence" (VAG+POLY-S3 R3 procedural + substantive).
- DORA: four-factor proportionality.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- DORA: competent authority.

**Content template comparison:**
- CRA: Annex VII §2 component-due-diligence record + SBOM.
- DORA: four-factor proportionality + Art. 30(2) 9-element contract.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** CRA component due diligence is product-level (manufacturer's third-party components); DORA ICT third-party risk is entity-level (financial entity's ICT service providers). The two are at different levels of the supply chain: CRA = upstream (manufacturer's inputs); DORA = midstream (deployer's ICT providers).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct actors, distinct objects, distinct triggers.** When a financial entity deploys a CRA-compliant product, the manufacturer (CRA-bound) and the deployer (DORA-bound) are typically different parties.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer record: (1) CRA manufacturer-side component due diligence; (2) DORA financial-entity-side ICT third-party risk. The DIFFERENT-PERSPECTIVE label is preserved.

---


---


