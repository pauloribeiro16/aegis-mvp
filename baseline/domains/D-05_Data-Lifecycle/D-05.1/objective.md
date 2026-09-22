# D-05.1 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-05.1.0 — High-level SecurityObjective
```yaml
id: SO-D-05.1.HL
subdomain: D-05.1
applies_to: auto  # activates when ≥2 applicable regs target overlapping data classes on the same party AND the Art. 10(5) carve-out does not dissolve the engagement
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md §D-05.1
verified_relationship_basis: CRDA-deep verified (3 pairs: 2 SAME — GDPR↔CRA = COMPLEMENTARY (verbatim "adequate, relevant and limited to what is necessary" language; controller-driven purpose vs manufacturer-design intended purpose); CRA↔AI_Act = COMPLEMENTARY (runtime product data vs training pipeline data — different lifecycle stages, sequential not concurrent); 1 CORRECTED — GDPR↔AI_Act, was CONTRADICTORY → SCOPE-DISJOINT (with explicit Art. 10(5) carve-out — the AI Act creates a conditional exception to GDPR Art. 9(1) special-category prohibition, conditioned on 6 cumulative safeguards (a)–(f), which is the textbook exception-permission pattern not the prohibition-vs-prohibition pattern that "contradictory" connotes); 3×3 matrix complete — note: NIS 2 and DORA are out-of-scope per AEGIS taxonomy §4.1; the three participating regulators target different data classes (personal data / product data / training data) with different triggers (controller-driven / manufacturer-design / provider-driven) and the high-level SO surfaces the common data-minimisation duty while preserving the per-reg data class and the Art. 10(5) special-category gateway)
emergent_tensions: 1
```
**Objective.** Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the purpose for which it is processed, with a documented necessity assessment and, where the underlying purpose changes, a compatibility assessment confirming that the new use is consistent with the original. Special-category data is processed only where a narrow exception applies and is documented to that effect.
