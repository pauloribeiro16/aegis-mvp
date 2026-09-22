# D-04.4 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-04.4.0 — High-level SecurityObjective
```yaml
id: SO-D-04.4.HL
subdomain: D-04.4
applies_to: auto  # activates when ≥2 applicable regs target overlapping recovery layers on the same party AND ≥1 sub-SO activates
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md §D-04.4
verified_relationship_basis: CRDA-deep verified (6 pairs: 5 SAME — 4 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; 1 CORRECTED — NIS 2 ↔ DORA, was EQUAL → COMPLEMENTARY (DORA-specific BC/backup/recovery overlay) — no SCOPE-DISJOINT, no CONTRADICTORY; 4×4 matrix complete — note: AI Act out-of-scope per AEGIS taxonomy §4.1; the four participating regulators stack the recovery architecture in three layers — CRA product resilience, NIS 2 entity BC triad, DORA financial-entity BC + backup-scoping on criticality/confidentiality — with the GDPR `timely manner` outcome as the personal-data-specific verification target; the high-level SO surfaces the common restoration duty while preserving the per-reg layer and the DORA-correction note that DORA is not co-extensive with NIS 2; the OJ-corrective note on DORA Art. 11(2)(c)/(d)/(e) is preserved verbatim in the DORA sub-SO)
emergent_tensions: 0
```
**Objective.** Systems, products, services, components and data are restored and recovered with documented recovery evidence applicable to the recovery dimensions of all four participating regulators on the same party.
