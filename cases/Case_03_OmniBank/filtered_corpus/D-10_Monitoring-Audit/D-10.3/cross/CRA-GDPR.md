# D-10.3 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 32(1)(d) + Art. 35(11)):**
> [as quoted above]

**CRA article (verbatim, Annex VII §6 + Annex I Part II (3)):**
> "The technical documentation shall contain the reports of the tests carried out to verify the conformity of the product … and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I." — CRA Annex VII §6 (per SR-CRA-101)
> "Manufacturers of products with digital elements shall … carry out effective and regular tests and reviews of the product …" — CRA Annex I Part II (3) (per SR-CRA-101)
> "The manufacturer shall ensure that products with digital elements which are not subject to the conformity assessment procedures applicable to important products of class I or class II or to critical products may demonstrate conformity by using one of the following procedures: (a) Module A (internal production control) …" — CRA Annex VIII Part I (Module A) (per SR-CRA-103)
> "The notified body shall examine the design of the product and the vulnerability-handling processes … and issue an EU-type examination certificate …" — CRA Annex VIII Part II (Module B+C and H) (per SR-CRA-104)

**Scope comparison:**
- GDPR scope: regular testing of security-measure effectiveness + DPIA review on risk change.
- CRA scope: effective-and-regular tests + conformity-assessment modules (Module A self-assessment, Module B+C and H notified-body).
- Scope overlap: **Conditional (Y when the controller deploys CRA-regulated products)**.

**Trigger comparison:**
- GDPR trigger: effectiveness-evaluation.
- CRA trigger: effective-and-regular tests + conformity-assessment.
- Trigger alignment: **PARTIAL**.

**Threshold/timeline comparison:**
- GDPR: `regularly testing`.
- CRA: `effective and regular` — Annex I Part II (3) per SR-CRA-101, cadence entity-discretionary per the OJ-literal text.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- CRA: MSA.

**Content template comparison:**
- GDPR: not codified for content.
- CRA: Annex VII §6 test reports + Annex VIII Part I-IV conformity-assessment modules.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR testing is effectiveness-evaluation; CRA testing is conformity-assessment via Modules A/B+C/H/certification. Different testing regimes serving different audit purposes.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the controller deploys CRA-regulated products)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 32(1)(d) effectiveness-evaluation + CRA Annex VII §6 test reports + Annex VIII conformity-assessment.

---
