# D-01.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-01.3.0 — High-level SecurityObjective
```yaml
id: SG-D-01.3.HL
subdomain: D-01.3
applies_to: auto  # activates when ≥2 applicable regs overlap on same key material
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md §D-01.3
verified_relationship_basis: CRDA-deep verified (3 pairs, all SAME — CRDA initial 3 COMPLEMENTARY corrected to SAME after OJ-text analysis)
emergent_tensions: 0
```
**Objective.** Cryptographic keys and related authentication material are
managed with separation of roles such that possession of the key material
is not bundled with possession of the operational environment that uses it;
the key custodian and the data consumer are distinct roles under distinct
technical and organisational control, with the cryptographic key (not the
storage medium) as the necessary condition for intelligibility of the
protected data.
