# D-06.4 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

**CRA article (verbatim, Art. 22(1)/(2) + Art. 23(1)/(2)):**
> "A natural or legal person, other than the manufacturer, the importer or the distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market shall be considered to be the manufacturer for the purposes of this Regulation." — CRA Art. 22(1)
>
> "The manufacturer obligations referred to in paragraph 1 shall apply to the affected part of the product with digital elements or, where the substantial modification has an impact on the cybersecurity of the product with digital elements as a whole, to the entire product with digital elements." — CRA Art. 22(2)
>
> "Economic operators shall, on a reasoned request from a market surveillance authority, identify: (a) any economic operator that has supplied them with a product with digital elements; (b) any economic operator to which they have supplied a product with digital elements." — CRA Art. 23(1)
>
> "Economic operators shall keep the information referred to in paragraph 1 for a period of 10 years after they have been supplied with the product with digital elements and after they have supplied the product with digital elements." — CRA Art. 23(2)

**Scope comparison:**
- NIS 2 scope: direct-supplier scope-limiter (entity-side, who the entity is liable for).
- CRA scope: substantial-modification triggers (who becomes the manufacturer) + economic-operator identification.
- Scope overlap: **N (typically) — different actors, different triggers.** Both apply when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party.

**Trigger comparison:**
- NIS 2 trigger: per-direct-supplier.
- CRA trigger: per-substantial-modification + per-MSA-identification-request.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- NIS 2: `direct` scope-limiter.
- CRA: Art. 3(30) substantial-modification + Art. 23(2) 10-year retention.
- Tension: **NONE**.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- CRA: MSA.

**Content template comparison:**
- NIS 2: documented supplier list under `direct` scope.
- CRA: substantial-modification record + Art. 23 supply-chain identification log (10-year retention).

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** NIS 2 `direct` scope-limiter is about *who* the entity is liable for (direct suppliers); CRA Art. 22 / 23 is about *who* becomes the manufacturer (third-party on substantial modification) and *who* provides identification to MSAs. Different actors, different triggers. Both apply when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party: the deployer is NIS 2-liable for the direct supplier, and the third-party modifier becomes a CRA-manufacturer.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct actors, distinct triggers.** Conditional overlap when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) NIS 2 deployer-side direct-supplier list; (2) CRA substantial-modification record + 10-year supply-chain identification log. The DIFFERENT-PERSPECTIVE label is preserved.

---


## Summary (Domain Analysis)

| NIS2 ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-014, Art. 21(2)(d)) | Direct supplier and service-provider security (`direct` scope-limiter) |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-014 |
| **CRA** (SR-CRA-062 + SR-CRA-063, Art. 22(1)/(2) + Art. 23) | Third-party substantial modification triggers manufacturer status + economic-operator identification + 10-year retention |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-062, SR-CRA-063 |

**Why different-perspective**: NIS2 `direct` scope-limiter is about *who* the entity is liable for (direct suppliers); CRA Art. 22/23 is about *who* becomes the manufacturer (third-party on substantial modification) and *who* provides identification to MSAs. Different actors, different triggers. Both apply when a NIS2-entity deploys a CRA-classified product substantially modified by a third party: the deployer is NIS2-liable for the direct supplier, and the third-party modifier becomes a CRA-manufacturer.



