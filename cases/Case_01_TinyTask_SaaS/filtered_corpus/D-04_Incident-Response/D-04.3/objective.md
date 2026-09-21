# D-04.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-04.3.0 — High-level SecurityObjective
```yaml
id: SO-D-04.3.HL
subdomain: D-04.3
applies_to: auto  # activates when ≥2 applicable regs overlap on same event
status: static    # pre-computed; not generated at Phase 1A
derivation_source: ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md §D-04.3
emergent_tensions: 2  # documented below
verified_relationship_basis: CRDA-deep verified (10 pairs, 1 SAME + 1 COMPLEMENTARY + 3 SCOPE-DISJOINT + 5 CONTRADICTORY / CONDITIONAL-CONTRADICTORY)
```
**Objective.** A major security incident is notified to the applicable recipients within the regulatory timelines applicable to the event's material scope.

