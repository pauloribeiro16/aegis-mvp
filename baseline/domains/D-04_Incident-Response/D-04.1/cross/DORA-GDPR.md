# D-04.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim):**
> Art. 32(1)(b) requires the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services. Art. 4(12) defines a personal data breach. Art. 33(1) anchors the 72-hour clock to the moment of becoming aware.

**DORA article (verbatim):**
> Art. 10(1) requires financial entities to have in place mechanisms to promptly detect anomalous activities, in accordance with Art. 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure. Art. 10(2) requires detection mechanisms to enable multiple layers of control, define alert thresholds and criteria to trigger and initiate ICT-related incident response processes, including automatic alert mechanisms for relevant staff in charge of ICT-related incident response.

**Scope comparison:**
- GDPR scope: detection of personal-data breaches.
- DORA scope: detection of anomalous ICT activities, including SPOF identification.
- Scope overlap: Conditional where a DORA financial entity processes personal data.

**Trigger comparison:**
- GDPR trigger: awareness of a personal-data breach.
- DORA trigger: detection of anomalous activities meeting Art. 10(1)/(2) thresholds.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: 72-hour clock.
- DORA: without undue delay, with RTS-defined classification thresholds under Art. 18.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory authority.
- DORA: competent authority and clients (per Art. 19(1)+(3)).

**Content template comparison:**
- GDPR: breach notification content per Art. 33(3).
- DORA: classification-driven notification content under Art. 19.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. DORA mandates layered detection with explicit alert thresholds and automatic escalation; GDPR mandates only the trigger outcome (becoming aware). A DORA Art. 10 detection event automatically feeds the GDPR Art. 33(1) "becoming aware" trigger when personal data are involved.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat the DORA detection pipeline as the operational source of GDPR "becoming aware" events for the personal-data subset, with the supervisory and competent-authority channels running in parallel.


## Summary (Domain Analysis)

| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-014, Art. 33(1)) | Continuous breach detection enabling the 72-hour clock |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-014 |
| **DORA** (SR-DORA-011 + SR-DORA-012, Art. 10(1)–(2)) | Multi-class anomalous-activity detection with SPOF identification + multi-layer threshold-driven response triggering |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-011, SR-DORA-012 |

**Why complementary**: DORA mandates layered detection mechanisms with explicit alert thresholds and automatic escalation; GDPR mandates only the trigger outcome (becoming aware). A financial entity implementing DORA Art. 10 produces detection events that automatically feed the GDPR Art. 33(1) "becoming aware" trigger when personal data are involved.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

