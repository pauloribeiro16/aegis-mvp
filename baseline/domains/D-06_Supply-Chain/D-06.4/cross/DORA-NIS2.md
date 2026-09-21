# D-06.4 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)

**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> (See GDPR↔DORA pair above for the verbatim text.)

**Scope comparison:**
- NIS 2 scope: direct supplier (entity-side).
- DORA scope: critical ICT third-party provider (financial-entity-side, CIF-only).
- Scope overlap: **Y when a financial entity is also a NIS 2 essential / important entity** — DORA audit rights extend to critical / important providers, which may include non-direct providers via the supply chain.

**Trigger comparison:**
- NIS 2 trigger: continuous supply-chain security.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **PARTIAL** — NIS 2 is continuous; DORA is per-CIF contract.

**Threshold/timeline comparison:**
- NIS 2: `direct` scope-limiter.
- DORA: CIF-only audit rights.
- Tension: **NONE** — DORA audit rights extend beyond NIS 2's `direct` scope.

**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- DORA: competent authority.

**Content template comparison:**
- NIS 2: documented supplier list under `direct` scope.
- DORA: Art. 30(3)(e)(i) audit-rights clause.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY** (DORA exceeds NIS 2)
**Reasoning:** NIS 2 `direct` scope-limiter limits the supplier universe; DORA Art. 30(3)(e) audit rights apply to critical or important providers (which may include non-direct providers via the supply chain). A financial entity's DORA audit rights extend beyond NIS 2's `direct` scope into the broader supply chain of critical providers.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when a financial entity is also a NIS 2 essential / important entity — both apply on the same supplier relationship.** DORA exceeds NIS 2 in the audit-rights dimension.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a consolidated supplier-management architecture: (1) NIS 2 `direct` supplier list; (2) DORA Art. 30(3)(e) audit-rights clause for CIF contracts. The COMPLEMENTARY label is preserved.

---


## Summary (Domain Analysis)

| NIS2 ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-014, Art. 21(2)(d)) | Direct supplier security |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-014 |
| **DORA** (SR-DORA-022, Art. 30(3)(e)) | Unrestricted audit rights over critical ICT third-party providers |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-022 |

**Why complementary (DORA exceeds)**: NIS2 `direct` scope-limiter limits the supplier universe; DORA Art. 30(3)(e) audit rights apply to critical or important providers (which may include non-direct providers via the supply chain). A financial entity's DORA audit rights extend beyond NIS2's `direct` scope into the broader supply chain of critical providers.



