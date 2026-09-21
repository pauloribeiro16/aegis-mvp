# D-07.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-07.3.0 — High-level SecurityObjective
```yaml
id: SO-D-07.3.HL
subdomain: D-07.3
applies_to: auto  # activates when ≥2 applicable regs have a Y or Conditional Y scope overlap on the same party AND ≥1 sub-SO activates; for D-07.3 the only 1 pair is NIS2↔CRA = Conditional Y (only when an NIS 2 entity procures a CRA-conformant product) AND N (typically) — so the high-level SO engages ONLY on the Conditional-Y integrated stack (NIS 2 entity procuring CRA-conformant product). For a 5-FTE SaaS startup with NIS 2 applicability only (no CRA applicability), the high-level SO is NOT activated. For a CRA-regulated manufacturer that is not an NIS 2 entity, the high-level SO is NOT activated either.
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md §D-07.3
verified_relationship_basis: CRDA-deep verified (1 pair: 1 SAME — COMPLEMENTARY with substantial scope-disjoint qualifier — NIS2↔CRA = SAME — COMPLEMENTARY with N (typically) qualifier + Conditional Y (when NIS 2 entity procures CRA-conformant product); no CORRECTED, no CONTRADICTORY — 1 COMPLEMENTARY pair; 2×2 matrix complete (NIS2 participates + CRA participates = 1 pair); the two participating regulators target distinct target objects (entity-side deployment-and-maintenance pipeline via Art. 21(2)(e) third clause partial coverage of the maintenance dimension / product-side update delivery path via Annex I Part II (7) + (8)) at distinct triggers (essential/important entity NIS deployment activity / manufacturer places product on market + distributes updates during the support period) and the high-level SO surfaces the common CI/CD-pipeline-security duty — build-time control baseline + update-distribution delivery-path security — typically built from industry frameworks NIST SP 800-204 + OWASP CI/CD Top 10 + SLSA since no OJ clause prescribes CI/CD build-time controls — while preserving the per-reg target object, trigger, anchor, threshold, evidence template, recipient and acknowledging the substantial scope-disjoint structure on the typical case; **NOTE — NIS 2 T3-vs-text gap**: NIS 2 Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`; the partial coverage is via the maintenance dimension with the T3 taxonomy importing CI/CD-pipeline vocabulary not in the OJ text; AEGIS taxonomy §4.1 marks NIS 2 as sole authority; **NOTE — CRA Annex I Part II (7)+(8) coverage scope**: CRA covers product-side update delivery path only; CRA does not specify CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments); CRA participation at D-07.3 is partial-coverage cross-ref only; **NOTE — no OJ-level consolidation rule on CI/CD pipeline security across the two regimes** — NIS 2 entity-side maintenance dimension + CRA product-side update delivery path meet at the supplier-customer boundary via the CRA-conformant product procurement record but neither prescribes an integrated CI/CD build-time baseline)
emergent_tensions: 0  # strictly: 0 CONTRADICTORY or CORRECTED reclassifications on the CI/CD-pipeline-security duty itself — the 1 verified pair is SAME — COMPLEMENTARY with scope-disjoint qualifier; no Phase 1C tension resolution is required for D-07.3
```
**Objective.** CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-agent integrity, ephemeral build environments) and update-distribution delivery-path security.

