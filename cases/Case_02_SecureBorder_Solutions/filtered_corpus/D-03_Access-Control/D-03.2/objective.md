# D-03.2 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-03.2.0 — High-level SecurityObjective
```yaml
id: SG-D-03.2.HL
subdomain: D-03.2
applies_to: auto  # activates when ≥2 applicable regs overlap on the same authentication event
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md §D-03.2
verified_relationship_basis: CRDA-deep verified (6 pairs, all SAME — CRDA initial 6 COMPLEMENTARY corrected to SAME after OJ-text analysis; 4×4 matrix complete — note: AI Act out-of-scope per AEGIS taxonomy §4; the four participating regulators target different authentication explicitness, which is preserved verbatim in the per-reg sub-SOs rather than as an unresolved tension; the DORA T4-vs-text gap on `strong authentication` vs MFA is a P0-flagged reading-choice divergence captured in `SR-DORA-002` ambiguity_notes)
emergent_tensions: 0
```
**Objective.** Authentication of users, services, and hardware that
interact with the entity's systems, products, services, components and
data operates through an authentication mechanism of sufficient strength
for the risk in scope, with the strictest applicable floor discharging
the most permissive on the same authentication event when both apply.
