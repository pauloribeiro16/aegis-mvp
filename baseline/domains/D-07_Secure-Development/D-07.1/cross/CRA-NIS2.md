# D-07.1 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim, Art. 21(2)(e)):**
> [as quoted in GDPR ↔ NIS2 above]

**CRA article (verbatim, Art. 13(1)):**
> [as quoted in GDPR ↔ CRA above]

**Scope comparison:**
- NIS 2 scope: entity-level security of NIS across acquisition, development, maintenance (entity side / user side).
- CRA scope: manufacturer-side product cybersecurity across 6 lifecycle phases (planning, design, development, production, delivery, maintenance).
- Scope overlap: **Y (when the entity procures a CRA-regulated product — they meet at the supplier-customer boundary).**

**Trigger comparison:**
- NIS 2 trigger: entity activity in NIS acquisition/development/maintenance.
- CRA trigger: manufacturer places product on market.
- Trigger alignment: **DIFFERENT** (entity side vs. maker side).

**Threshold/timeline comparison:**
- NIS 2: no quantitative threshold; Art. 21(1) appropriate-and-proportionate.
- CRA: support period ≥ 5 years (Art. 13(8)).
- Tension: **NONE** (different actors / different lifecycle stages).

**Recipient comparison:**
- NIS 2: management body, competent authority.
- CRA: market surveillance authority (MSA), users.

**Content template comparison:**
- NIS 2: not codified for content; entity-discretionary methodology under Recital 56.
- CRA: Annex VII §1-§4 design/development/risk-assessment/support-period record.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** NIS 2 Art. 21(2)(e) governs the entity's procurement and internal development of NIS (the user side); CRA Art. 13(1)/(2) governs the manufacturer's design of products (the maker side). The two regimes meet at the supply-chain boundary — NIS 2 Art. 21(2)(d) supplier obligations reference CRA-conformant products via SR-NIS2-020/024. No contradiction; full coverage requires both.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the entity procures a CRA-regulated product and integrates it into NIS)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a supplier-customer interface map: CRA-conformant product serves as upstream gate for NIS 2 Art. 21(2)(e) deployment decisions; NIS 2 entity's supplier-risk register references CRA Annex VII technical documentation.

---


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-026, Art. 21(2)(e) acquisition; SR-NIS2-027, Art. 21(2)(e) development; SR-NIS2-028, Art. 21(2)(e) maintenance) | Entity-level lifecycle security across acquisition, development, maintenance. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-026 / SR-NIS2-027 / SR-NIS2-028 |
| **CRA** (SR-CRA-064, Art. 13(1); SR-CRA-065, Art. 13(2); SR-CRA-066, Art. 13(3) — partial at D-09.2) | Product-level design/development/production per Annex I Part I with documented risk assessment across 6 phases. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-064 / SR-CRA-065 |

**Why complementary**: NIS 2 governs the entity's procurement and internal development of NIS (the user side); CRA governs the manufacturer's design of products (the maker side). The two regimes meet at the supply-chain boundary — NIS 2 Art. 21(2)(d) supplier obligations reference CRA-conformant products via SR-NIS2-020/024. No contradiction; full coverage requires both.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

