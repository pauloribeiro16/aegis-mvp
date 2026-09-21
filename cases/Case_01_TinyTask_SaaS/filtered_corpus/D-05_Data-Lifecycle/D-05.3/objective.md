# D-05.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-05.3.0 — High-level SecurityObjective
```yaml
id: SO-D-05.3.HL
subdomain: D-05.3
applies_to: auto  # activates when ≥2 applicable regs target overlapping erasure layers on the same party AND ≥1 sub-SO activates
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md §D-05.3
verified_relationship_basis: CRDA-deep verified (1 pair: 1 SAME — COMPLEMENTARY — GDPR↔CRA = COMPLEMENTARY (CRDA initial classification held); no SCOPE-DISJOINT, no CONTRADICTORY, no CORRECTED; 2×2 matrix complete — note: NIS 2, DORA, AI Act are out-of-scope per AEGIS taxonomy §4.1; the two participating regulators STACK on the same party in the personal-data subset — GDPR Art. 17 data-subject right (controller-bound) executed through the CRA Annex I Part I (2)(m) user-facing mechanism (manufacturer-bound) — the manufacturer enables the secure + easily + permanently removable affordance + the documented data-class inventory; the controller executes the Art. 17(1) trigger through that affordance with the cryptographic-erasure deletion path per SR-GDPR-030; the high-level SO surfaces the common erasure duty — render the user's data inaccessible on the user's election — while preserving the per-reg layer (controller's policy execution vs manufacturer's product design) and the per-reg trigger (Art. 17(1) request vs user-initiated product removal))
emergent_tensions: 0
```
**Objective.** Data held about a person is rendered inaccessible to the controller on the data subject's election, and data held by a product with digital elements is rendered inaccessible to the manufacturer on the user's election, by whichever mechanism — the controller-side policy execution or the manufacturer-side product affordance — applies to the data object. Erasure is performed without undue delay and is documented to demonstrate compliance; where a processor is involved, the processor-side mirror ensures deletion-or-return at contract end.

