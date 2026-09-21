# D-10.2 — Pair analysis: GDPR ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ CRA

**GDPR article (verbatim, Art. 5(2) + Art. 30(3)):**
> "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 ('accountability')." — Art. 5(2) GDPR
> "The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request." — Art. 30(3) GDPR

**CRA article (verbatim, Annex VII §5-§8 + Annex VII §3):**
> "The technical documentation shall contain: (5) the list of the harmonised standards … applied in full or in part … (6) the reports of the tests carried out to verify the conformity of the product … (7) a copy of the EU declaration of conformity … (8) on a reasoned request from a market surveillance authority, where necessary to check compliance, the software bill of materials …" — CRA Annex VII §5-§8 (per SR-CRA-088)
> "The technical documentation shall contain an assessment of the cybersecurity risks against which the product with digital elements is designed, developed, produced, delivered and maintained pursuant to Article 13 …" — CRA Annex VII §3 (per SR-CRA-080)

**Scope comparison:**
- GDPR scope: compliance records (RoPA, consent, processor contracts, breach notifications, DPIA) maintained with integrity and traceability.
- CRA scope: documentation traceability + risk-assessment record + test reports.
- Scope overlap: **N (typically)** — different record types (compliance vs. product cybersecurity).

**Trigger comparison:**
- GDPR trigger: processing of personal data.
- CRA trigger: product placement on market.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: until processing ceases + on SA request.
- CRA: 10 years or support period, whichever longer.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- CRA: MSA.

**Content template comparison:**
- GDPR: Art. 30(1)/(2) content items.
- CRA: Annex VII §5-§8 standards + tests + declaration + SBOM-on-request.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR records focus on processing activities and demonstrability of compliance; CRA records focus on product cybersecurity documentation and conformity. Different record types serving different audit purposes.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically)** — different record types, different triggers. Substantively scope-disjoint.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 30 RoPA + CRA Annex VII §5-§8 technical documentation.

---


