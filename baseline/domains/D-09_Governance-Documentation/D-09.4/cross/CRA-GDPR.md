# D-09.4 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 30(1)–(4)):**
> [as quoted above]

**CRA article (verbatim, Art. 13(12) + Art. 13(13) + Annex VII §1-§8):**
> "Where, prior to placing a product with digital elements on the market, the manufacturer has carried out a conformity assessment procedure … the manufacturer shall draw up the technical documentation … and draw up the EU declaration of conformity." — Art. 13(12) CRA (per SR-CRA-085)
> "The manufacturer shall keep the technical documentation and the EU declaration of conformity at the disposal of the market surveillance authorities for at least 10 years after the product has been placed on the market, or for the support period, whichever is longer." — Art. 13(13) CRA (per SR-CRA-084)

**Scope comparison:**
- GDPR scope: controller/processor RoPA.
- CRA scope: product-level technical documentation + EU declaration + CE marking + Annex VII 8-item content.
- Scope overlap: **N (typically)** — different record types.

**Trigger comparison:**
- GDPR trigger: processing of personal data.
- CRA trigger: product placement on market.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: 250-employee carve-out; retention until processing ceases + on SA request.
- CRA: 10 years or support period, whichever longer.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- CRA: MSA.

**Content template comparison:**
- GDPR: Art. 30(1)/(2) content items.
- CRA: Annex VII 8-item content list.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR RoPA covers processing activities (purposes, data categories, recipients, safeguards); CRA technical documentation covers product cybersecurity (design, development, risk assessment, SBOM, conformity). Different artefacts serving different audit purposes. The two regimes do not cross-substitute.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different record types, different triggers. Substantively scope-disjoint.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 30 RoPA + CRA Annex VII technical documentation. No OJ-level consolidation.

---


## Summary (Domain Analysis)

| GDPR ↔ CRA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-048, Art. 30(1)-(4)) | RoPA with 250-employee carve-out. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-048 |
| **CRA** (SR-CRA-085, Art. 13(12) pre-market docs + EU declaration + CE; SR-CRA-087, Annex VII §1-§2 general description + design/development; SR-CRA-088, Annex VII §5-§8 standards + tests + declaration + SBOM) | Technical documentation + EU declaration + CE marking + Annex VII 8-item content. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-085 / SR-CRA-087 / SR-CRA-088 |

**Why different-perspective**: GDPR RoPA covers processing activities (purposes, data categories, recipients, safeguards); CRA technical documentation covers product cybersecurity (design, development, risk assessment, SBOM, conformity). Different artefacts serving different audit purposes. The two regimes do not cross-substitute.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

