# D-06.2 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-06.2.0 — High-level SecurityObjective
```yaml
id: SG-D-06.2.HL
subdomain: D-06.2
applies_to: auto  # single-regulator sub-domain — activates when CRA in applicable_regs AND the sub-SO activates; the high-level SO is redundant in this single-regulator case but is still emitted for traceability per the activation model in ../../index.md lines 32-42
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.2.md §D-06.2
verified_relationship_basis: CRDA-deep verified (0 pairs — single-participant sub-domain; CRA is the SOLE AUTHORITY for D-06.2 per AEGIS taxonomy §4.1; GDPR, NIS 2, DORA, AI Act are all out-of-scope; the Annex I Part II (1) SBOM authoring duty + Annex VII §2(b) technical-documentation retention + Annex VII §8 MSA reasoned-request disclosure + Annex II §9 optional user access + Art. 13(24) Commission implementing acts compose the three-anchored SBOM architecture — authoring, retention, regulatory disclosure; the high-level SO describes the common SBOM duty — the manufacturer draws up and maintains an SBOM in a commonly used and machine-readable format covering at least the top-level dependencies, with format flexibility (POLY-S3 R3 reading per SR-CRA-008 pending Commission implementing acts under Art. 13(24)) and `where necessary` MSA-disclosure scope (POLY-S2 R1 reading per SR-CRA-053); no CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY classifications by construction (single regulator))
emergent_tensions: 0
```
**Objective.** The manufacturer draws up and maintains a software bill of materials (SBOM) covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies.
