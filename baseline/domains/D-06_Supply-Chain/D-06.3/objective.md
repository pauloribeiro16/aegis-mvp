# D-06.3 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-06.3.0 — High-level SecurityObjective
```yaml
id: SO-D-06.3.HL
subdomain: D-06.3
applies_to: auto
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.3.md §D-06.3
verified_relationship_basis: CRDA-deep verified (6 pairs: 5 SAME + 1 CORRECTED; GDPR↔NIS2 = COMPLEMENTARY, GDPR processor DPA clauses layer with NIS 2 direct-supplier contract/security assessment; GDPR↔CRA = DIFFERENT-PERSPECTIVE, controller-processor contract vs importer/distributor market-surveillance obligations; GDPR↔DORA = CORRECTED — COMPLEMENTARY, Art. 28(3) 8-element DPA + DORA Art. 30(2) 9-element ICT-contract list form a clause-list union, not a contradiction; NIS2↔CRA = COMPLEMENTARY, ex-ante supplier assessment vs product/component lifecycle escalation; NIS2↔DORA = EQUAL with DORA exceeding NIS 2, DORA Art. 30 operationalises NIS 2 security-related contractual aspects in the financial-services subset; CRA↔DORA = DIFFERENT-PERSPECTIVE, market-surveillance-facing economic-operator obligations vs financial-entity ICT contract obligations; no verified CONTRADICTORY pairs; AI Act out-of-scope per AEGIS taxonomy §4.1)
emergent_tensions: 1
```
**Objective.** Third-party security obligations are made enforceable through contracts, transfer safeguards, written mandates, or market-access duties, as appropriate to the regulatory perspective and the actor involved.

