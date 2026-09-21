# D-06.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

**CRA article (verbatim, Art. 13(5)):**
> "Manufacturers shall exercise due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements." — CRA Art. 13(5)

**Scope comparison:**
- NIS 2 scope: direct supplier relationships at the entity level (deployer's supplier list).
- CRA scope: third-party components at the product level (manufacturer's component list).
- Scope overlap: **N (typically) — different levels of the supply chain.** They overlap when the deployer is the entity and the manufacturer supplies a CRA-compliant product.

**Trigger comparison:**
- NIS 2 trigger: per-supplier direct-relationship.
- CRA trigger: per-component integration.
- Trigger alignment: **DIFFERENT** — entity-level vs product-level.

**Threshold/timeline comparison:**
- NIS 2: "appropriate and proportionate" + `direct` scope-limiter.
- CRA: "due diligence" (VAG+POLY-S3 R3 procedural + substantive).
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- CRA: MSA.

**Content template comparison:**
- NIS 2: documented supplier-risk assessment + Art. 21(3) sentence 2 EU-level risk propagation.
- CRA: Annex VII §2 component-due-diligence record + SBOM per Annex I Part II (1).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** NIS 2 supplier relationships are at the *entity* level (the deployer's supplier list); CRA component due diligence is at the *product* level (the manufacturer's component list). The two lists overlap when the deployer is the entity and the manufacturer supplies a CRA-compliant product: the deployer does NIS 2-level supplier due diligence on the manufacturer, while the manufacturer does CRA-level component due diligence on its third-party components.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the deployer is the entity and the manufacturer supplies a CRA-compliant product — both apply but at different supply-chain levels).** The pair is layered; the entity and the manufacturer are typically different parties.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer assessment record: (1) NIS 2 deployer-side supplier-risk register; (2) CRA manufacturer-side component-due-diligence record (SBOM-backed). The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-020, Art. 21(2)(d)) | Direct supplier and service-provider security |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-020 |
| **CRA** (SR-CRA-050, Art. 13(5)) | Third-party component due diligence including non-commercial OSS |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-050 |

**Why different-perspective**: NIS2 supplier relationships are at the *entity* level (the deployer's supplier list); CRA component due diligence is at the *product* level (the manufacturer's component list). The two lists overlap when the deployer is the entity and the manufacturer supplies a CRA-compliant product: the deployer does NIS2-level supplier due diligence on the manufacturer, while the manufacturer does CRA-level component due diligence on its third-party components.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

