# D-03.4 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-03.4.0 — High-level SecurityObjective
```yaml
id: SO-D-03.4.HL
subdomain: D-03.4
applies_to: auto  # activates when both GDPR and CRA applicable and the CRA product processes personal data
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md §D-03.4
verified_relationship_basis: CRDA-deep verified (1 pair, SAME DIFFERENT-PERSPECTIVE — CRDA initial classification confirmed after OJ-text analysis; the two participating regulators target different default objects at different layers, which is preserved verbatim in the per-reg sub-SOs rather than as an unresolved tension; note: 2×2 matrix smaller than 3×3 because only 2 participants)
emergent_tensions: 0
```
**Objective.** The default disposition of the entity's data-centric
processing systems and the product's product-centric configuration is
managed so that the baseline state of every processing system and every
product configuration is the minimum-necessary / secure configuration,
with relaxation requiring affirmative data-subject or user intervention.
