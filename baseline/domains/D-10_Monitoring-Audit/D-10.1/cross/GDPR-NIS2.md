# D-10.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 32(2) + Art. 33(1)):**
> "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing, as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures … such as … (b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services; (c) the ability to restore the availability and access to personal data in a timely manner … (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures …" — Art. 32(1)+(2) GDPR

**NIS2 article (verbatim, Art. 21(2)(b) detection dimension):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (b) incident handling …" — Art. 21(2)(b) NIS 2 (per SR-NIS2-009)

**Scope comparison:**
- GDPR scope: personal-data processing systems monitored for adverse events covering 5 Art. 32(2) risk types; breach-`becoming-aware` anchoring for Art. 33(1) notification clock.
- NIS 2 scope: all-hazards monitoring to surface adverse events (incident-handling detection capability).
- Scope overlap: **Y (when the controller-NSIE processes personal data through NIS — detection capability overlaps).**

**Trigger comparison:**
- GDPR trigger: 5 Art. 32(2) risk types (accidental/unlawful destruction, loss, alteration, unauthorised disclosure/access).
- NIS 2 trigger: incident-handling detection capability (all-hazards).
- Trigger alignment: **PARTIAL** (different triggering frameworks — risk-type-triggered vs. incident-triggered).

**Threshold/timeline comparison:**
- GDPR: breach-`becoming-aware` anchoring for Art. 33(1) 72-hour notification clock.
- NIS 2: no quantitative threshold for monitoring.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: not codified for content.
- NIS 2: not codified for content (incident-handling 6-action lifecycle per SR-NIS2-008).

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR monitoring anchors on 5 risk types; NIS 2 monitoring anchors on incident-handling detection capability. The two regimes cover overlapping detection capability but with different triggering frameworks (risk-type-triggered vs. incident-triggered).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the controller-NSIE processes personal data through NIS)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered detection stack: GDPR Art. 32(2) 5-risk-type monitoring + NIS 2 Art. 21(2)(b) incident-handling detection capability.

---


