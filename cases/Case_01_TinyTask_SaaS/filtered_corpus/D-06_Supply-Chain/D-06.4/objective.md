# D-06.4 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-06.4.0 — High-level SecurityObjective
```yaml
id: SO-D-06.4.HL
subdomain: D-06.4
applies_to: auto
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md §D-06.4
verified_relationship_basis: CRDA-deep verified (6 pairs: 6 SAME, no CORRECTED, no CONTRADICTORY; GDPR↔NIS2 = COMPLEMENTARY, EU legal-address representative vs cross-MS SPOC/ENISA notification routing; GDPR↔CRA = EQUAL (different objects), both written EU-side representatives but data-protection representative and product-compliance authorised representative coexist; GDPR↔DORA = DIFFERENT-PERSPECTIVE, legal-address designation vs CIF audit/access rights; NIS2↔CRA = DIFFERENT-PERSPECTIVE, direct-supplier scope-limiter vs substantial-modification manufacturer-status and economic-operator identification; NIS2↔DORA = COMPLEMENTARY with DORA exceeding NIS 2, critical-provider audit rights extend beyond direct-supplier floor; CRA↔DORA = DIFFERENT-PERSPECTIVE, economic-operator supply-chain identification vs financial-entity audit rights; AI Act out-of-scope per AEGIS taxonomy §4.1)
emergent_tensions: 1
```
**Objective.** Third-party boundary responsibilities are explicitly allocated so that non-EU representatives, direct-supplier scope, cross-border routing, substantial-modification accountability, economic-operator identification, and audit/access rights remain traceable to the correct actor and recipient.

