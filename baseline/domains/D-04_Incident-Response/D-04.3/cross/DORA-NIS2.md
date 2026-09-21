# D-04.3 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 23(4)(a) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact (OJ L 333, 27.12.2022, p. 129).

**DORA article (verbatim):**
> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.

**Scope comparison:**
- NIS2 scope: significant incidents at essential or important entities.
- DORA scope: major ICT-related incidents at financial entities.
- Scope overlap: Conditional, where NIS2 obligations remain applicable to a financial entity or to non-financial functions not fully displaced by the financial-sector lex-specialis layer.

**Trigger comparison:**
- NIS2 trigger: significant incident, with severe disruption/loss or considerable damage tests.
- DORA trigger: major ICT-related incident under Art. 18 classification.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: 24h/72h/1m tiered structure.
- DORA: without undue delay after major-incident classification, with reporting templates and classification criteria.
- Tension: GENUINE only if both reporting regimes apply to the same event at the same party.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- DORA: relevant financial competent authority and affected clients where Art. 19(3) applies.

**Content template comparison:**
- NIS2: early warning, incident notification, final report and requested intermediate reports.
- DORA: major-incident report and client-facing mitigation communication under the financial-sector template.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — CONDITIONAL-CONTRADICTORY only where both regimes remain applicable

**Reasoning (1-2 paragraphs):** The OJ text does not support an unconditional contradiction. NIS2 and DORA use different sectoral scopes and trigger taxonomies. Where DORA is lex specialis for financial entities, the baseline should not assume a full duplicate NIS2 notification track without a scope/legal-applicability decision.

If both tracks apply to the same financial entity and incident, the NIS2 hard 24h/72h/1m cascade must be reconciled with DORA's without-undue-delay major-incident reporting. That is a genuine operational tension, but it is conditional on dual applicability.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should include a DORA/NIS2 applicability gate before assigning deadlines; do not automatically impose the NIS2 24h tier on every DORA incident.


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **contradictory** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-010–013, Art. 23(4)(a)–(e)) | 24h/72h/1m tiered notification structure |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-010, SR-NIS2-011, SR-NIS2-012, SR-NIS2-013 |
| **DORA** (SR-DORA-017, Art. 19(1) + Art. 19(3)) | `without undue delay` supervisor + `without undue delay as soon as aware` client |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-017 |

**Why contradictory (structure)**: NIS2 has hard-anchor tiered timelines (24h/72h/1m); DORA has only `without undue delay`. For financial entities that are NIS2-essential or NIS2-important, NIS2's hard anchors bind via the per-entity classification; DORA's `without undue delay` must be operationalised to satisfy NIS2's 24h/72h/1m tiers. Phase 2 must set the DORA timeline at the NIS2 tier structure.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

