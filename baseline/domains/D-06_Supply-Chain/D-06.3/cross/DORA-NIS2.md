# D-06.3 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

**DORA article (verbatim, Art. 30(1)+(2)):**
> (See GDPR↔DORA pair above for the verbatim 9-element list.)

**Scope comparison:**
- NIS 2 scope: direct supplier contract (entity-side).
- DORA scope: ICT third-party contract (financial-entity-side).
- Scope overlap: **Y when a financial entity is also a NIS 2 essential / important entity**.

**Trigger comparison:**
- NIS 2 trigger: continuous supply-chain security.
- DORA trigger: per-ICT-third-party contract.
- Trigger alignment: **PARTIAL** — NIS 2 is continuous; DORA is per-contract.

**Threshold/timeline comparison:**
- NIS 2: "security-related contractual aspects" (open-texture).
- DORA: closed 9-element list.
- Tension: **NONE** — DORA's 9-element list operationalises NIS 2's `security-related contractual aspects` with specific provisions.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- DORA: competent authority.

**Content template comparison:**
- NIS 2: security-related supplier-contract terms.
- DORA: 9-element Art. 30(2) contract.

**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL** (DORA exceeds NIS 2)
**Reasoning:** DORA's 9-element contract list operationalises the NIS 2 `security-related contractual aspects` with specific provisions. A financial entity implementing DORA Art. 30 exceeds NIS 2's contractual-security requirement for the financial-services subset of suppliers. The label is correct: same object (contractual-security on direct supplier), DORA's closed list exceeds NIS 2's open-texture floor.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when a financial entity is also a NIS 2 essential / important entity — both apply on the same supplier relationship.** DORA satisfies NIS 2 in the financial-services subset.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a consolidated contract template satisfying both regimes. The DORA 9-element list is documented and the NIS 2 `security-related contractual aspects` chapeau is satisfied by reference.

---


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **equal** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-020, Art. 21(2)(d)) | Direct supplier security by contract |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-020 |
| **DORA** (SR-DORA-021 + SR-DORA-022, Art. 30(1)–(3)) | Minimum 9 contractual elements + unrestricted audit rights |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-021, SR-DORA-022 |

**Why equal (DORA exceeds)**: DORA's 9-element contract list operationalises the NIS2 `security-related contractual aspects` with specific provisions. A financial entity implementing DORA Art. 30 exceeds NIS2's contractual-security requirement for the financial-services subset of suppliers.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

