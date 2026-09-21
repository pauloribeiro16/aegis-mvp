# D-05.2 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-05.2.0 — High-level SecurityObjective
```yaml
id: SO-D-05.2.HL
subdomain: D-05.2
applies_to: auto  # activates when ≥2 applicable regs target overlapping data classes on the same party AND the floor-within-ceiling or separation-architecture layering rule engages
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.2.md §D-05.2
verified_relationship_basis: CRDA-deep verified (3 pairs: 1 SAME — CRA↔AI_Act = DIFFERENT-PERSPECTIVE (different objects — update artefact availability vs AI log retention; different actors — manufacturer vs provider; different purposes — user protection continuity vs post-market monitoring and incident reconstruction; 2 CORRECTED — GDPR↔CRA, was CONTRADICTORY (direction) → SCOPE-DISJOINT (the CRDA reasoning itself concedes "CRA's 10-year tail is about update availability, not personal-data retention", making the contradictory label scope-incorrect; the pair is scope-disjoint in baseline with separation-architecture requirement as the layering rule where the CRA update log contains personal data); GDPR↔AI_Act, was CONTRADICTORY (direction) → COMPLEMENTARY (floor-within-ceiling) (the AI Act ≥6-month floor is a subset of GDPR's "no longer than is necessary" envelope, which the CRDA reasoning itself states is reconcilable, making the contradictory label scope-incorrect; the pair is substantive-complementary on the same data flow when the AI log contains personal data, with the operative range [6 months, "necessary"]); 3×3 matrix complete — note: NIS 2 and DORA are out-of-scope per AEGIS taxonomy §4.1; the three participating regulators target different data classes (personal data / update artefact / AI log) with different obligation directions (GDPR ceiling / CRA floor / AI Act floor) and the high-level SO surfaces the common retention/archiving duty as a 3-axis layering rule — GDPR ceiling + AI Act floor + CRA availability tail — with explicit separation-architecture and floor-within-ceiling hand-offs)
emergent_tensions: 1
```
**Objective.** Data — across the data classes in scope — is retained for the period required to satisfy its declared purpose, with documented retention rationale and, where the underlying purpose changes, a reset of the retention clock. Long-term archiving or research-only retention is paired with safeguards proportional to the residual identifiability.

