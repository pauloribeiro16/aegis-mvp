# D-06.4 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 27(1)/(2)):**
> "Where Article 3(2) applies, the controller or the processor shall designate in writing a representative in the Union." — Art. 27(1) GDPR
>
> "The obligation set out in paragraph 1 shall not apply to: (a) processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or of personal data relating to criminal convictions as referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing; or (b) a public authority or body." — Art. 27(2)(a)/(b) GDPR

**NIS 2 article (verbatim, Art. 23(6) + Art. 23(8)):**
> "The competent authorities or the CSIRTs shall inform the other affected Member States and ENISA about the incident. The competent authorities or the CSIRTs shall, in accordance with Union or national law, provide the relevant information to the recipients of the services of the entity concerned." — NIS 2 Art. 23(6)
>
> "Single points of contact shall forward the notifications referred to in this Article to the single points of contact of other affected Member States and to ENISA." — NIS 2 Art. 23(8)

**Scope comparison:**
- GDPR scope: non-EU controller / processor → EU representative (legal-address anchor).
- NIS 2 scope: cross-MS notification routing → SPOC + ENISA (notification-routing mechanism).
- Scope overlap: **N (typically) — different mechanisms (legal address vs notification routing).** They overlap when a non-EU controller operates across multiple MS.

**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- NIS 2 trigger: significant incident notification.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold (per-processing-event assessment).
- NIS 2: significant-incident threshold + 24h early warning + 72h notification + final report.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- NIS 2: SPOC + ENISA + affected MS.

**Content template comparison:**
- GDPR: written representative designation.
- NIS 2: incident-notification routing through SPOC.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 27 designates an EU *representative* (a legal-address anchor for non-EU controllers); NIS 2 Art. 23(6) routes notifications across *Member States* via SPOCs (Single Points of Contact). Different actors (representative vs SPOC), different purposes (legal address vs notification routing). Both apply when a non-EU controller operates across multiple MS.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms, distinct actors.**

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer record: (1) GDPR Art. 27 representative designation; (2) NIS 2 SPOC identification for incident-notification routing. The COMPLEMENTARY label is preserved.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-038, Art. 27(1)/(2)) | Written EU representative for non-EU controllers/processors |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-038 |
| **NIS2** (SR-NIS2-018, Art. 23(6) + Art. 23(8)) | Cross-border notification across Member States and ENISA via SPOC |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-018 |

**Why complementary**: GDPR Art. 27 designates an EU *representative* (a legal-address anchor for non-EU controllers); NIS2 Art. 23(6) routes notifications across *Member States* via SPOCs (Single Points of Contact). Different actors (representative vs SPOC), different purposes (legal address vs notification routing). Both apply when a non-EU controller operates across multiple MS.



