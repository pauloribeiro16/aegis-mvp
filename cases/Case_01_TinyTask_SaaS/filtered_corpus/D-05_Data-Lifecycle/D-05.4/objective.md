# D-05.4 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-05.4.0 — High-level SecurityObjective
```yaml
id: SG-D-05.4.HL
subdomain: D-05.4
applies_to: auto  # single-regulator sub-domain — activates when GDPR in applicable_regs AND the sub-SO activates; the high-level SO is redundant in this single-regulator case but is still emitted for traceability per the activation model in ../../index.md lines 32-42
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md §D-05.4
verified_relationship_basis: CRDA-deep verified (0 pairs — single-participant sub-domain; GDPR is the SOLE AUTHORITY for D-05.4 per AEGIS taxonomy §4.1; NIS 2, CRA, DORA, AI Act are out-of-scope; the CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is a *complementary technical anchor* when the data resides in a CRA-classified product but does NOT constitute a portability *right* and does not ground a CRA sub-SO on D-05.4; the high-level SO describes the common portability duty — the data subject receives personal data in a structured, commonly used, machine-readable format and can transmit to another controller — with the CRA architectural anchor noted in the Objective text and the per-reg perspective (trigger, format, recipient, legal anchor) preserved in the 1 sub-SO; no CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY classifications by construction (single regulator))
emergent_tensions: 0
```
**Objective.** Personal data are exported to the data subject in a structured, commonly used, machine-readable format, and the data subject can transmit those data to another controller without hindrance, subject to the qualifying conditions and exclusions that scope the right.
