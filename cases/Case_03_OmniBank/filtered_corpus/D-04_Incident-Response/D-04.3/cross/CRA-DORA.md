# D-04.3 — Pair analysis: CRA ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ DORA

**CRA article (verbatim):**
> Art. 14(1) requires a manufacturer to notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) — the CSIRT of the Member State where the manufacturer has its main establishment in the Union — and to ENISA, via the single reporting platform established under Art. 16.

**DORA article (verbatim):**
> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.

**Scope comparison:**
- CRA scope: manufacturer reporting for product vulnerabilities or severe product incidents.
- DORA scope: financial-entity reporting for major ICT-related incidents.
- Scope overlap: N typically; Conditional only where the financial entity is also the manufacturer or otherwise bears manufacturer obligations for the product.

**Trigger comparison:**
- CRA trigger: manufacturer awareness of AEV or severe incident.
- DORA trigger: financial entity classification of a major ICT-related incident.
- Trigger alignment: DIFFERENT.

**Threshold/timeline comparison:**
- CRA: 24h/72h/14d or 24h/72h/1m depending on track.
- DORA: without undue delay after major-incident classification.
- Tension: NONE in the typical deployer/manufacturer split; GENUINE only in same-party overlap.

**Recipient comparison:**
- CRA: CSIRT coordinator and ENISA.
- DORA: financial competent authority and clients where Art. 19(3) conditions are met.

**Content template comparison:**
- CRA: product/vulnerability or severe-incident track content.
- DORA: financial-entity major-incident report and client mitigation information.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline

**Reasoning (1-2 paragraphs):** This is the clearest P0 case. The OJ text places CRA duties on the manufacturer and DORA duties on the financial entity. In the common case, a bank using a CRA-regulated product is not the manufacturer, so the clocks do not collide on a single party.

The same underlying incident chain may produce separate obligations at different parties: the manufacturer reports under CRA; the financial entity reports under DORA. That is coordination, not contradiction. CRDA's unconditional X is scope-incorrect for the baseline.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? N typically / Conditional only in same-party manufacturer-financial-entity cases
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline.

**Downstream implication (1-2 sentences):** Doc 07 should model CRA↔DORA as a supply-chain notification hand-off by default, not as a single-party conflicting-deadline problem.


## Summary (Domain Analysis)

<!-- pair: CRA,DORA -->
| CRA ↔ DORA | **contradictory** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-029–033, Art. 14(2)–(4)) | AEV: 24h/72h/14d; SI: 24h/72h/1m |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-029, SR-CRA-030, SR-CRA-031, SR-CRA-032, SR-CRA-033 |
| **DORA** (SR-DORA-017, Art. 19(1) + Art. 19(3)) | `without undue delay` supervisor + `without undue delay as soon as aware` client |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-017 |

**Why contradictory (timeline)**: CRA hard-anchors at 24h/72h/14d/1m; DORA uses only `without undue delay`. CRA's 14d AEV final is tighter than any DORA-specific anchor. Phase 2 must align DORA `without undue delay` with CRA's tier structure when the same event is both a CRA severe incident/AEV and a DORA major ICT incident.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_