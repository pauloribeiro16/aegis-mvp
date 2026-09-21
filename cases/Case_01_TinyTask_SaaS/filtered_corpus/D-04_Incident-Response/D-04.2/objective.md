# D-04.2 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-04.2.0 — High-level SecurityObjective
```yaml
id: SO-D-04.2.HL
subdomain: D-04.2
applies_to: auto  # activates when ≥2 applicable regs target overlapping containment layers on the same party AND ≥1 sub-SO activates
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md §D-04.2
verified_relationship_basis: CRDA-deep verified (6 pairs, 5 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE — no CRDA corrections needed; 4×4 matrix complete — note: AI Act out-of-scope per AEGIS taxonomy §4.1; the four participating regulators target different containment layers, which is preserved verbatim in the per-reg sub-SOs rather than as an unresolved tension)
emergent_tensions: 0
```
**Objective.** Security incidents affecting the entity's systems, products, services, components and data are contained and mitigated through appropriate measures that address the incident's impact and reduce the probability of further damage.

