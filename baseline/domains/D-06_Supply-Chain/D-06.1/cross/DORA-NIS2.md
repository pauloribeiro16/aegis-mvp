# D-06.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

**DORA article (verbatim, Art. 28(1) + Art. 28(5)):**
> "Financial entities shall manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services …" — DORA Art. 28(1)

**Scope comparison:**
- NIS 2 scope: direct supplier relationships (entity-level).
- DORA scope: ICT third-party service providers (financial-entity-level).
- Scope overlap: **Y when a financial entity is also a NIS 2 essential / important entity**.

**Trigger comparison:**
- NIS 2 trigger: continuous supply-chain security.
- DORA trigger: continuous ICT third-party risk with four-factor proportionality.
- Trigger alignment: **SAME** — both continuous.

**Threshold/timeline comparison:**
- NIS 2: "appropriate and proportionate" + `direct` scope-limiter.
- DORA: four-factor proportionality (nature, scale, complexity, importance).
- Tension: **NONE** — DORA's four-factor test operationalises NIS 2's `appropriate and proportionate` chapeau with explicit factors.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- DORA: competent authority (national financial supervisory authority).

**Content template comparison:**
- NIS 2: documented supply-chain security programme; Member State transposition may specify minimum-clause catalogues.
- DORA: four-factor proportionality assessment + Art. 30(2) 9-element contract.

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL** (DORA exceeds NIS 2)
**Reasoning:** DORA's four-factor proportionality test operationalises the NIS 2 `appropriate and proportionate` Art. 21(1) chapeau with explicit factors. A financial entity implementing DORA exceeds NIS 2's supply chain security requirement (financial-entity subset). The label is correct: same object, same addressee, DORA's sharper test exceeds NIS 2's general test.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the financial entity is also a NIS 2 essential / important entity — both apply on the same supplier relationship.** DORA satisfies NIS 2 in the financial-services subset; NIS 2 remains the floor for the broader essential / important-entity population.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a consolidated risk-assessment record satisfying both regimes; the DORA four-factor test is documented and the NIS 2 `appropriate and proportionate` chapeau is satisfied by reference.

---


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-020, Art. 21(2)(d)) | Direct supplier and service-provider security |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-020 |
| **DORA** (SR-DORA-019, Art. 28(1)) | ICT third-party risk under four-factor proportionality |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-019 |

**Why equal (DORA exceeds NIS2)**: DORA's four-factor proportionality test operationalises the NIS2 `appropriate and proportionate` Art. 21(1) chapeau with explicit factors. A financial entity implementing DORA exceeds NIS2's supply chain security requirement.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

