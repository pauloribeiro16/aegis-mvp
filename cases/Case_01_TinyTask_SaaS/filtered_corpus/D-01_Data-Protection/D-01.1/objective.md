# D-01.1 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-01.1.0 — High-level SecurityObjective
```yaml
id: SO-D-01.1.HL
subdomain: D-01.1
applies_to: auto  # activates when ≥2 applicable regs overlap on same datastore
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.1.md §D-01.1
verified_relationship_basis: CRDA-deep verified (6 pairs, all SAME — CRDA initial 5 COMPLEMENTARY + 1 EQUAL corrected to SAME after OJ-text analysis)
emergent_tensions: 0
```
**Objective.** Data held at rest in storage is protected against unauthorised
access through appropriate technical measures — primarily encryption with
appropriate key custody — calibrated to the risks identified in the entity's
risk assessment and commensurate with the state of the art.
