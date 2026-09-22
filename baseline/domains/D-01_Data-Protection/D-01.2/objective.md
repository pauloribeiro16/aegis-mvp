# D-01.2 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-01.2.0 — High-level SecurityObjective
```yaml
id: SO-D-01.2.HL
subdomain: D-01.2
applies_to: auto  # activates when ≥2 applicable regs overlap on same channel
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.2.md §D-01.2
verified_relationship_basis: CRDA-deep verified (3 pairs, all SAME — CRDA initial 3 COMPLEMENTARY corrected to SAME after OJ-text analysis)
emergent_tensions: 0
```
**Objective.** Data in transit — across network paths, inter-service
calls, and third-party APIs — is protected against unauthorised disclosure
and alteration through cryptographic confidentiality and integrity controls
(mutual authentication, encryption, integrity verification).
