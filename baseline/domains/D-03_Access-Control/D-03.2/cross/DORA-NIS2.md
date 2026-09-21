# D-03.2 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2)(j) of Directive (EU) 2022/2555, in its first clause, requires essential and important entities to use multi-factor authentication or continuous authentication solutions, where appropriate.

**DORA article (verbatim):**
> Art. 9(4)(d) requires financial entities to implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

**Scope comparison:**
- NIS2 scope: MFA/continuous authentication for essential/important entities.
- DORA scope: strong authentication for financial entities.
- Scope overlap: Conditional where a financial entity is also within retained NIS2 scope.

**Trigger comparison:**
- NIS2 trigger: continuous risk-based authentication duty.
- DORA trigger: continuous financial-sector authentication duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: where appropriate.
- DORA: strong authentication based on standards and dedicated controls.
- Tension: NONE.

**Recipient comparison:**
- NIS2: entity governance and NIS competent authority evidence.
- DORA: financial-entity governance and competent-authority evidence.

**Content template comparison:**
- NIS2: MFA/continuous-authentication policy, factor/justification.
- DORA: strong-authentication standard, control-system, key-protection evidence.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. Both regulate authentication; NIS2 is risk-anchored, DORA is strong-authentication-anchored. A financial entity also within retained NIS2 scope can satisfy both with one architectural design. There is no tension because neither clause forbids what the other mandates.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat the DORA strong-authentication standard as the NIS2 "where appropriate" floor in the financial-sector context.


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **Complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-006, Art. 21(2)(j)) | MFA or continuous authentication "where appropriate" | Entity-level; OR; PR.AA-03 + PR.AA-05 |
| **DORA** (SR-DORA-002, Art. 9(4)(d)) | Strong authentication mechanisms (dominant EBA reading: MFA) | Financial entity; strong-authentication; PR.AA-03 + PR.AA-04 |

**Why Complementary**: Both regulations impose an authentication obligation, with NIS 2's "where appropriate" hedge and DORA's "strong authentication" anchor. The DORA OJ text does not say "multi-factor" (T4-vs-text gap); the dominant EBA Guidelines reading is MFA. A DORA financial entity that is a NIS 2 essential entity is jointly bound: NIS 2's "where appropriate" hedge + DORA's "strong authentication" — the two converge on PR.AA-03 (users/services/hardware authenticated) as the shared anchor. The "where appropriate" vs "strong authentication" difference is a threshold difference: NIS 2 requires proportionality to risk; DORA requires high-standard strength. → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-006; `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-002



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

