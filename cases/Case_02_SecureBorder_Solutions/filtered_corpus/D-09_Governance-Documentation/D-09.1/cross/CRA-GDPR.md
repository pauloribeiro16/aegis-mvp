# D-09.1 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 24(1) + Art. 5(2)):**
> [as quoted above]

**CRA article (verbatim, Art. 24(1) + Art. 13(8) + Art. 27(1)/(2)/(5)/(8)/(9)):**
> "Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product." — Art. 24(1) CRA (per SR-CRA-072)
> "Products with digital elements and the processes put in place by the manufacturer shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I where those products and processes conform to harmonised standards …" — Art. 27(1) CRA
> "The Commission may adopt implementing acts establishing common specifications …" — Art. 27(2) CRA
> "Common specifications … shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I …" — Art. 27(5) CRA
> "A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881 … shall be presumed to be in conformity with the essential cybersecurity requirements …" — Art. 27(8) CRA

**Scope comparison:**
- GDPR scope: controller-side data-protection policies.
- CRA scope: manufacturer-side cybersecurity policies + OSS steward policies + presumption-of-conformity machinery.
- Scope overlap: **N (typically)** — different actors (controller vs. manufacturer/steward).

**Trigger comparison:**
- GDPR trigger: controller's adoption of data-protection policies.
- CRA trigger: manufacturer/steward adoption of cybersecurity policies.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- CRA: support period + 10-year Annex II accessibility.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- CRA: MSA.

**Content template comparison:**
- GDPR: not codified for content.
- CRA: not codified for content (Art. 24(1) OSS steward policy contains 4 sub-elements (i)–(iv) per SR-CRA-072).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR addresses controller policies for personal data processing; CRA addresses manufacturer policies for product cybersecurity (and OSS steward policies under Art. 24). The two policies are different artefacts and can coexist without overlap.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the controller is also a manufacturer or OSS steward; N otherwise)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two parallel tracks: GDPR Art. 24 controller policies + CRA Art. 24/27 manufacturer/steward policies + presumption-of-conformity machinery.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,CRA -->
| GDPR ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-043, Art. 24(1)+(2)) | Appropriate technical and organisational measures; data-protection policies. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-043 |
| **CRA** (SR-CRA-072, Art. 24(1) OSS steward policy; SR-CRA-073, Art. 24(2) OSS steward cooperation; SR-CRA-075, Art. 13(8) manufacturer policies cluster; SR-CRA-077, Art. 27(1)/(2)/(5) presumption via harmonised standards / common specs; SR-CRA-078, Art. 27(8)/(9) CSA-certification presumption) | OSS steward cybersecurity policy; manufacturer policies/processes/procedures; presumption of conformity. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-072 / SR-CRA-073 / SR-CRA-075 / SR-CRA-077 / SR-CRA-078 |

**Why complementary**: GDPR addresses controller policies for personal data processing; CRA addresses manufacturer policies for product cybersecurity. The two policies are different artefacts and can coexist without overlap.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
45 lines — see ../../_migration_report.md)_