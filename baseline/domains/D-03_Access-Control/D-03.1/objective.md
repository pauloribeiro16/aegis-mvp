# D-03.1 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-03.1.0 — High-level SecurityObjective
```yaml
id: SG-D-03.1.HL
subdomain: D-03.1
applies_to: auto  # activates when ≥2 applicable regs target overlapping identity boundaries on the same party
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md §D-03.1
verified_relationship_basis: CRDA-deep verified (6 pairs, all SAME — CRDA initial 2 DIFFERENT-PERSPECTIVE + 4 COMPLEMENTARY corrected to SAME after OJ-text analysis; 4×4 matrix complete — note: AI Act out-of-scope per AEGIS taxonomy §4; the four participating regulators target different identity subjects, which is preserved verbatim in the per-reg sub-SOs rather than as an unresolved tension)
emergent_tensions: 0
```
**Objective.** Identities of principals that interact with the entity's
systems, products, services, components and data are managed in a
verifiable, lifecycle-aware manner with documented boundaries between
identity types and explicit hand-off protocols at boundary surfaces.
