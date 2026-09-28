# D-09.2 — Pair analysis: GDPR ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ DORA

**GDPR article (verbatim, Art. 35(1) + Art. 35(7)):**
> [as quoted above]

**DORA article (verbatim, Art. 6(4) + Art. 7(2)):**
> "Financial entities shall assign the responsibility for managing and overseeing ICT risk to a control function and ensure an appropriate level of independence … in accordance with the three lines of defence model, or an internal risk management and control model." — Art. 6(4) DORA (per SR-DORA-028)
> "Financial entities shall, on a continuous basis, identify all sources of ICT risk, in particular the risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities relevant to their ICT supported business functions, information assets and ICT assets." — Art. 7(2) sentence 1 DORA (per SR-DORA-004; the OJ-literal locus is Art. 8(2) per the v0.2 audit note)
> "Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them." — Art. 7(2) sentence 2 DORA (per SR-DORA-005; the OJ-literal locus is Art. 8(2) per the v0.2 audit note)

**Scope comparison:**
- GDPR scope: pre-launch DPIA for high-risk personal-data processing.
- DORA scope: continuous ICT risk identification + at-least-yearly risk-scenario review + three-lines-of-defence.
- Scope overlap: **Y (when the DORA financial entity is a controller processing personal data).**

**Trigger comparison:**
- GDPR trigger: high-risk processing event.
- DORA trigger: continuous ICT risk identification + yearly risk-scenario review.
- Trigger alignment: **DIFFERENT**.

**Threshold/timeline comparison:**
- GDPR: DPIA before processing + review on change of risk.
- DORA: continuous + at-least-yearly.
- Tension: **NONE**.

**Recipient comparison:**
- GDPR: DPA.
- DORA: NCA.

**Content template comparison:**
- GDPR: 4-item Art. 35(7) content.
- DORA: ICT risk identification register + risk-scenario register.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR DPIA is pre-launch; DORA risk framework is operational continuous + yearly review. No pre-launch DPIA-equivalent in DORA.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA financial entity conducts a DPIA for high-risk personal-data processing)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce two separate artefacts: GDPR Art. 35 DPIA (pre-launch) + DORA Art. 7(2) continuous identification + Art. 7(2) sentence 2 yearly review.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,DORA -->
| GDPR ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-045, Art. 35(1)-(4)) | DPIA pre-launch. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-045 |
| **DORA** (SR-DORA-028, Art. 6(4) three-lines-of-defence) | Three-lines-of-defence + asset identification/classification. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-028 |

**Why different-perspective**: GDPR DPIA is pre-launch; DORA risk framework is operational continuous + yearly review. No pre-launch DPIA-equivalent in DORA.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_