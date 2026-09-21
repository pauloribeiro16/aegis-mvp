# D-04.3 — Pair analysis: CRA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim):**
> Art. 14(3) requires the manufacturer to notify any severe incident having an impact on the security of the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) and to ENISA, via the single reporting platform.

**AI_Act article (verbatim):**
> Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires providers of high-risk AI systems, and deployers where applicable, to report any serious incident to the market surveillance authorities of the Member States where the incident occurred. The reporting timeline depends on the severity: 15 days after the provider becomes aware (default), 10 days if the incident results in death, 2 days for widespread infringement.

**Scope comparison:**
- CRA scope: product with digital elements and manufacturer duties.
- AI Act scope: high-risk AI providers/deployers and GPAI providers.
- Scope overlap: Conditional, when the product with digital elements is also a high-risk AI system or GPAI model and the same party bears both roles.

**Trigger comparison:**
- CRA trigger: AEV or severe product incident.
- AI Act trigger: serious AI incident.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- CRA: 24h/72h/14d for AEV; 24h/72h/1m for severe incident.
- AI Act: 15d default, 10d death, 2d widespread infringement; GPAI without undue delay.
- Tension: GENUINE if same-party/same-product overlap; NONE if manufacturer/provider/deployer roles are split.

**Recipient comparison:**
- CRA: CSIRT coordinator and ENISA.
- AI Act: market surveillance authorities or AI Office.

**Content template comparison:**
- CRA: product incident/vulnerability details and mitigation information.
- AI Act: serious-incident details, causal attribution and corrective measures.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONTRADICTORY on confirmed same-party overlap

**Reasoning (1-2 paragraphs):** The CRDA X is plausible only when the same product and same actor sit under both regimes. CRA and AI Act are frequently layered but not always actor-identical: a product manufacturer, AI provider and AI deployer can be different legal persons.

When the same party is both CRA manufacturer and AI Act provider/deployer for the same system, the notification clocks diverge sharply. Then the contradiction/tension is real and must be resolved through strictest-deadline routing. Without that role overlap, the baseline is scope-disjoint coordination.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should include a role-unification test for AI products before assigning a single notification owner.


## Summary (Domain Analysis)

| CRA ↔ AI_Act | **contradictory** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-031–033, Art. 14(3)–(4)) | SI: 24h/72h/1m |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-031, SR-CRA-032, SR-CRA-033 |
| **AI_Act** (SR-AIACT-022, Art. 73(1)–(4)) | 15d default + 10d (death) + 2d (widespread) |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-022 |

**Why contradictory (timeline + scope)**: CRA's 24h is tighter than AI Act's 15d default; AI Act's 2d (widespread) is the only AI Act tier that competes with CRA's 24h. The scope differs: CRA severe incident is product-level (manufacturer-centric); AI Act serious incident is high-risk-AI-level (provider+deployer-centric). The two regulations must run in parallel when a high-risk AI is also a CRA-classified product.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

