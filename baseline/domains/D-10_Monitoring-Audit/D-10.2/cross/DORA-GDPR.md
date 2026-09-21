# D-10.2 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 5(2) + Art. 30(3)):**
> [as quoted above]

**DORA article (verbatim, Art. 9(4)(a) per SR-DORA-031):**
> "Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable." — Art. 9(4)(a) DORA

**Scope comparison:**
- GDPR scope: compliance records with integrity + traceability.
- DORA scope: information security policy defining CIA+A rules (logging implicit, not standalone).
- Scope overlap: **N (typically)** — different record types (compliance vs. CIA+A policy).

**Trigger comparison:**
- GDPR trigger: processing of personal data.
- DORA trigger: information security policy adoption.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: until processing ceases + on SA request.
- DORA: no OJ-text retention period for logging.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- DORA: NCA.

**Content template comparison:**
- GDPR: Art. 30(1)/(2) content items.
- DORA: CIA+A information security policy.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR compliance records + DORA CIA+A logging stack for DORA financial entities. The two regimes address different record types (compliance vs. operational).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when the DORA financial entity is a controller with compliance records)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered stack: GDPR Art. 30 RoPA + DORA Art. 9(4)(a) CIA+A policy (with logging under the policy).

---


