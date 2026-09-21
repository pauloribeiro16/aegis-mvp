# D-10.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 32(2) + Art. 33(1)):**
> [as quoted above]

**DORA article (verbatim, Art. 8(1) per SR-DORA-030; OJ-literal locus Art. 9(1) per the v0.2 audit):**
> "Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures." — DORA Art. 8(1) per SR-DORA-030 (OJ-literal locus Art. 9(1))

**Scope comparison:**
- GDPR scope: entity-level monitoring (5 Art. 32(2) risk types).
- DORA scope: financial-entity continuous monitoring and control of ICT-system security and functioning (CIA+A).
- Scope overlap: **Y (when the DORA financial entity is a controller processing personal data)**.

**Trigger comparison:**
- GDPR trigger: 5 Art. 32(2) risk types.
- DORA trigger: ICT-system security and functioning monitoring (CIA+A).
- Trigger alignment: **PARTIAL** (DORA is broader — security AND functioning; GDPR is 5 risk types).

**Threshold/timeline comparison:**
- GDPR: breach-`becoming-aware` 72h clock.
- DORA: continuous (Art. 9(1)).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- DORA: NCA.

**Content template comparison:**
- GDPR: not codified for content.
- DORA: monitoring tools + policies + procedures.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** DORA monitoring is broader (security and functioning) than GDPR monitoring (5 risk types). DORA subsumes the GDPR detection capability within its entity-level continuous-monitoring mandate for financial entities.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is a controller processing personal data)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 9(1) continuous monitoring + GDPR Art. 32(2) 5-risk-type detection as a sub-component.

---


