# D-03.4 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim):**
> Art. 25(2) obliges the controller to implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons.

**CRA article (verbatim):**
> Annex I Part I (2)(b) requires products to be made available on the market with a secure-by-default configuration — including the possibility to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements. Art. 6(a) proviso anchors the configuration to intended purpose and reasonably foreseeable use.

**Scope comparison:**
- GDPR scope: data-protection by default across amount, extent, period and accessibility of personal data.
- CRA scope: secure-by-default configuration of the product, including reset capability, with the tailor-made carve-out.
- Scope overlap: Conditional when a CRA product processes personal data.

**Trigger comparison:**
- GDPR trigger: continuous data-protection-by-default obligation.
- CRA trigger: continuous product secure-by-default obligation at market placement.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: appropriate by-default measures across four dimensions.
- CRA: secure by default with reset capability; tailor-made carve-out for business users.
- Tension: NONE.

**Recipient comparison:**
- GDPR: data subjects and supervisory authority.
- CRA: product users and market surveillance.

**Content template comparison:**
- GDPR: by-default settings across four Art. 25(2) dimensions.
- CRA: secure-by-default configuration and reset procedure.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** GDPR is data-centric by default; CRA is product-centric by default. The OJ text confirms that they target different objects at different layers. There is no contradiction, even in overlap cases, because the GDPR Art. 25(2) four-dimension test operates on the data and the CRA Annex I (2)(b) test operates on the product configuration.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat data-by-default and product-secure-by-default as two layers of the same default posture, with documentation showing how each dimension is satisfied.


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **Different perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-013, Art. 25(2)) | Data-protection by default: only personal data necessary for each specific purpose processed — across amount, extent, period, accessibility | Controller; personal-data scope; "by default" across 4 dimensions; PR.DS-12 + GV.PO-01 (data-management + policy) |
| **CRA** (SR-CRA-018 + SR-CRA-025 + SR-CRA-026, Annex I Part I (2)(b)+(c)) | Secure-by-default configuration + reset to original + automatic security updates default + opt-out + postponement | Manufacturer; product-level; "tailor-made" carve-out for business users; PR.PS-01 + PR.DS-12 + GV.SC-03 |

**Why Different perspective**: GDPR's "by default" obligation is **data-centric** (only the personal data necessary for the purpose is processed, across 4 dimensions); CRA's "secure by default" obligation is **product-centric** (the product is made available with secure-by-default configuration + reset capability). The two are different perspectives on "default" at different objects (data vs product). A controller deploying a CRA-regulated product is jointly bound: the data-centric by-default (GDPR) + the product-centric by-default (CRA). The two are not contradictory: they target different objects at different layers. **Caveat:** the CRA `tailor-made` carve-out (Annex I Part I (2)(b) "unless otherwise agreed between manufacturer and business user in relation to a tailor-made product") is a product-level configuration exception that does not apply to GDPR's data-centric by-default obligation — a CRA tailor-made product configuration does not exempt the controller from GDPR's data-protection by default. → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-013; `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-018 + SR-CRA-025 + SR-CRA-026



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

