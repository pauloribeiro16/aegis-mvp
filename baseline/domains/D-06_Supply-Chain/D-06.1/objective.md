# D-06.1 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-06.1.0 — High-level SecurityObjective
```yaml
id: SO-D-06.1.HL
subdomain: D-06.1
applies_to: auto  # activates when ≥2 applicable regs have ≥1 pair with Y/Conditional scope overlap on the same party AND ≥1 sub-SO activates; for D-06.1 all 6 pairs have Y or Conditional Y scope overlap, so once ≥2 regs are applicable the high-level SO engages
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md §D-06.1
verified_relationship_basis: CRDA-deep verified (6 pairs: 6 SAME, no CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY — 2 COMPLEMENTARY (GDPR↔NIS2 = COMPLEMENTARY, sharper-qualitative-on-shared-risk-substrate; GDPR↔DORA = COMPLEMENTARY (DORA exceeds GDPR), four-factor-proportionality operationalises GDPR sufficient-guarantees with sharper factors) + 3 DIFFERENT-PERSPECTIVE (GDPR↔CRA = entity-level processor vs product-level component; NIS2↔CRA = entity-level supplier vs product-level component; CRA↔DORA = upstream product-level vs midstream entity-level ICT provider) + 1 EQUAL (NIS2↔DORA = same-object-same-addressee-sharper-test, DORA exceeds NIS2); 4×4 matrix complete — note: AI Act is out-of-scope per AEGIS taxonomy §4.1 — AI Act value-chain obligations (Art. 25) are cross-relationship, not in the 29-clause cybersecurity set; the four participating regulators target distinct target objects (processor-as-legal-entity / direct-supplier-as-relationship / third-party-component-as-technical-artefact / ICT-third-party-as-financial-entity-provider) with distinct triggers (per-processor engagement / continuous supply-chain security / per-component integration / continuous ICT third-party risk management under Art. 28(1) four-factor proportionality) and the high-level SO surfaces the common vendor-risk-assessment duty — risk-anchored due diligence with proportionality documentation + ongoing monitoring + recipient evidence — while preserving the per-reg target object, trigger, anchor, threshold, evidence template, recipient)
emergent_tensions: 0
```
**Objective.** Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain.
