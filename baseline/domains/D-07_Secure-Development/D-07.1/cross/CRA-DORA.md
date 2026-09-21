# D-07.1 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim, Art. 13(1)):**
> [as quoted in GDPR ↔ CRA above]

**DORA article (verbatim, Art. 9(4)(b)):**
> [as quoted in GDPR ↔ DORA above]

**Scope comparison:**
- CRA scope: manufacturer-side product cybersecurity across 6 lifecycle phases.
- DORA scope: financial-entity network/infrastructure management + change management.
- Scope overlap: **Y (when a DORA entity procures CRA-regulated products).**

**Trigger comparison:**
- CRA trigger: manufacturer places product on market.
- DORA trigger: ICT system establishment / change event.
- Trigger alignment: **DIFFERENT** (maker side vs. user side).

**Threshold/timeline comparison:**
- CRA: support period ≥ 5 years (Art. 13(8)).
- DORA: no quantitative threshold.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA, users.
- DORA: management body, NCA.

**Content template comparison:**
- CRA: Annex VII technical documentation.
- DORA: Art. 6(1) ICT risk-management framework + Art. 9(4)(b) network-management record.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA governs the products DORA entities procure and deploy; DORA's secure-by-design absence (no dedicated by-design mandate in OJ) is filled by the upstream CRA obligation. A DORA entity satisfies its design-procurement baseline by selecting CRA-conformant products and recording the conformance in its supplier-risk register per SR-DORA-006 (network/infrastructure) and SR-DORA-023 (change-management).

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the DORA entity is also a CRA product deployer/procurer)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a CRA-as-upstream-gate model: CRA-conformant products are inputs to DORA's Art. 6(1) ICT risk-management framework.

---


## Summary (Domain Analysis)

| CRA ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-064, Art. 13(1); SR-CRA-065, Art. 13(2)) | Product-level three-phase design/development/production with risk assessment. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-065 |
| **DORA** (SR-DORA-004, Art. 9(4)(b)+(f) — partial) | Network/infrastructure mgmt + change-management; secure-by-design is implicit. | |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-004 |

**Why complementary**: CRA governs the products DORA entities procure and deploy. DORA's secure-by-design absence is filled by the upstream CRA obligation: a DORA entity satisfies its design-procurement baseline by selecting CRA-conformant products and recording the conformance in its supplier-risk register.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

