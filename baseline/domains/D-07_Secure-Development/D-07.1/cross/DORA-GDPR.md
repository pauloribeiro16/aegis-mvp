# D-07.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 25(1)):**
> [as quoted above]

**DORA article (verbatim, Art. 9(4)(b)):**
> "Financial entities shall … (b) establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks." — Art. 9(4)(b) DORA

**Scope comparison:**
- GDPR scope: controller-side means-determination for personal-data processing.
- DORA scope: financial-entity network and infrastructure management structure.
- Scope overlap: **Conditional (Y when a financial entity is a controller processing personal data over its own ICT systems).**

**Trigger comparison:**
- GDPR trigger: controller's means-determination.
- DORA trigger: establishment of network/infrastructure management structure (continuous).
- Trigger alignment: **DIFFERENT** (data-protection properties vs. ICT infrastructure).

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold; Art. 24 appropriate-and-proportionate.
- DORA: no quantitative threshold; Art. 4 proportionality under Recital 56.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- DORA: competent authority (NCA), management body.

**Content template comparison:**
- GDPR: documented Art. 25(1) assessment.
- DORA: documented Art. 6(1) ICT risk-management framework + Art. 9(4)(b) network-management record.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** DORA Art. 9(4)(b) is not a dedicated by-design mandate — secure-by-design is operationalised through change management (Art. 9(4)(e)) and testing programme (Art. 24). The OJ literal text does not contain a dedicated by-design anchor; the SR-DORA-004 mapping to D-07.1 is partial at best. For a DORA financial entity that is a controller processing personal data, GDPR Art. 25(1) provides the data-protection by-design overlay while DORA's change-management six-step provides the engineering discipline. The two stack with distinct evidence trails.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y when a DORA financial entity processes personal data over its ICT systems)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-layer by-design baseline (operationalised via change management Art. 9(4)(e) + testing Art. 24) augmented by the GDPR Art. 25(1) data-protection by-design overlay for personal-data processing.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-039, Art. 25(1); SR-GDPR-040, Art. 25(1)+32(1)(a)) | Privacy-by-design + pseudonymisation-by-design. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-039 / SR-GDPR-040 |
| **DORA** (SR-DORA-004, Art. 9(4)(b)+(f) — partial) | Network/infrastructure management structure with patch-management policies (secure-by-design is implicit, not standalone). | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-004 |

**Why complementary**: DORA does not impose a dedicated by-design mandate — secure-by-design is operationalised through the testing programme (Art. 24) and change-management controls (Art. 9(4)(e)). GDPR's by-design obligations therefore have no direct DORA counterpart at the entity level for the financial sector; the two coexist without overlap for non-product design decisions.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

