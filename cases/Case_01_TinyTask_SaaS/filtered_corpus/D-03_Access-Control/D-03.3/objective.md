# D-03.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-03.3.0 — High-level SecurityObjective
```yaml
id: SO-D-03.3.HL
subdomain: D-03.3
applies_to: auto  # activates when ≥2 applicable regs target overlapping authorisation surfaces on the same party
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md §D-03.3
verified_relationship_basis: CRDA-deep verified (6 pairs, all COMPLEMENTARY — 5 SAME-COMPLEMENTARY + 1 CORRECTED from CRDA EQUAL on NIS2↔DORA to COMPLEMENTARY after OJ-text analysis showing DORA 'only' qualifier is operationally more demanding; 4×4 matrix complete — note: AI Act out-of-scope per AEGIS taxonomy §4; the four participating regulators target different authorisation surfaces, which is preserved verbatim in the per-reg sub-SOs rather than as an unresolved tension)
emergent_tensions: 0
```
**Objective.** The entitlement to perform actions on the entity's systems,
products, services, components, and data is managed per least privilege
with explicit authorisation-model choice, documented entitlements,
attack-surface-limitation evidence, and boundary hand-offs between access
surfaces.

