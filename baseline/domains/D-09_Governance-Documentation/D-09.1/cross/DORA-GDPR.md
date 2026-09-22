# D-09.1 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 24(1) + Art. 5(2)):**
> [as quoted above]

**DORA article (verbatim, Art. 5(2) + Art. 6(1) + Art. 6(4)):**
> "The management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework." — Art. 5(2) DORA (per SR-DORA-026)
> "Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively." — Art. 6(1) DORA (per SR-DORA-027)
> "Financial entities shall assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … in accordance with the three lines of defence model, or an internal risk management and control model." — Art. 6(4) DORA (per SR-DORA-028)

**Scope comparison:**
- GDPR scope: controller-side data-protection policies.
- DORA scope: financial-entity ICT risk-management framework + three-lines-of-defence.
- Scope overlap: **Y (when a DORA financial entity is a controller processing personal data).**

**Trigger comparison:**
- GDPR trigger: controller's adoption of data-protection policies.
- DORA trigger: management-body define/approve/oversee/implement + ICT risk-management framework.
- Trigger alignment: **PARTIAL** (both policy-driven).

**Threshold/timeline comparison:**
- GDPR: no quantitative cadence.
- DORA: no quantitative cadence (entity-discretionary under Art. 4 proportionality).
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: data subject, DPA.
- DORA: management body, NCA.

**Content template comparison:**
- GDPR: not codified for content.
- DORA: Art. 6(2) lists 5 artefact types — `strategies, policies, procedures, ICT protocols and tools`.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** DORA's ICT risk-management framework is the dominant authority for financial entities; GDPR policies become a module within the framework. DORA Art. 5(2) governance + GDPR Art. 5(2) accountability stack.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity is a controller adopting data-protection policies within the framework)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a DORA-led stack: DORA Art. 6(1) ICT risk-management framework as carrier + GDPR Art. 24 data-protection policies as module.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-043, Art. 24(1)+(2)) | Appropriate data-protection policies. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-043 |
| **DORA** (SR-DORA-026, Art. 5(2) management body defines/approves/oversees/implements; SR-DORA-027, Art. 6(1) sound/comprehensive/well-documented ICT risk management framework; SR-DORA-028, Art. 6(4) three-lines-of-defence + asset identification) | ICT risk management framework with three-lines-of-defence model and asset identification/classification. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-026 / SR-DORA-027 / SR-DORA-028 |

**Why complementary**: DORA's ICT risk management framework is the dominant authority for financial entities; GDPR policies become a module within the framework. DORA Art. 5(2) governance + GDPR Art. 5(2) accountability stack.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_