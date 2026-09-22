# D-01.4 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-01.4.0 — High-level SecurityObjective
```yaml
id: SO-D-01.4.HL
subdomain: D-01.4
applies_to: auto  # activates when ≥2 applicable regs overlap on same data asset
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md §D-01.4
verified_relationship_basis: CRDA-deep verified (6 pairs, all SAME — CRDA initial 4 COMPLEMENTARY + 1 EQUAL + 2 DIFFERENT PERSPECTIVE corrected to SAME after OJ-text analysis)
emergent_tensions: 0
```
**Objective.** Data integrity is preserved against unauthorised modification
across the data lifecycle — at rest, in transit, and in use — with
corruption detected, logged, and reported, and with semantic accuracy
maintained as the workflow leg of the personal-data principle.
