# D-07.1 — High-level Security Objective (regulation-neutral)

> Common objective of the sub-domain; activates when ≥2 applicable regulations'
> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation
> perspectives live in [regs/](regs/); aggregation reasoning in
> [cross/_interactions.md](cross/_interactions.md).

#### D-07.1.0 — High-level SecurityObjective
```yaml
id: SO-D-07.1.HL
subdomain: D-07.1
applies_to: auto  # activates when ≥2 applicable regs have ≥1 pair with Y scope overlap on the same party AND ≥1 sub-SO activates; for D-07.1 all 10 pairs have Y scope overlap on a single party at the same event, so once ≥2 regs are applicable the high-level SO engages
status: static
derivation_source: ../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md §D-07.1
verified_relationship_basis: CRDA-deep verified (10 pairs: 10 SAME — COMPLEMENTARY, no CORRECTED, no SCOPE-DISJOINT in baseline, no CONTRADICTORY — 10 COMPLEMENTARY pairs covering all combinations of 5 participating regs (GDPR+5 = 4 pairs; NIS2+4 = 3 pairs (NIS2→GDPR, NIS2→CRA, NIS2→DORA, NIS2→AI_Act); CRA+3 = 2 pairs (CRA→GDPR, CRA→NIS2, CRA→DORA, CRA→AI_Act); DORA+2 = 1 pair (DORA→GDPR, DORA→NIS2, DORA→CRA, DORA→AI_Act); AI_Act+1 = 0 pairs (all four above); total = 4+3+2+1+0 = 10 pairs); 5×5 matrix complete — the five participating regulators target distinct target objects (data-protection-properties via pseudonymisation+minimisation / NIS-lifecycle security across acquisition+development+maintenance / product-cybersecurity via Annex I Part I with 6-phase risk-assessment propagation / ICT-infrastructure-management with change-mgmt six-step + testing programme as by-design operationalisation / AI-system-accuracy-robustness-cybersecurity with QMS design-control) with distinct triggers (controller means-determination / NSIE NIS lifecycle activity / manufacturer places product on market / financial entity establishes ICT infrastructure / provider places high-risk AI system on market) and the high-level SO surfaces the common secure-by-design duty — security integrated into the lifecycle via documented by-design decisions + risk-assessment propagation + proportionate safeguards + lifecycle consistency — while preserving the per-reg target object, trigger, anchor, threshold, evidence template, recipient; **NOTE — DORA dedicated by-design absence**: DORA OJ Art. 9(4)(b) is network/infrastructure-management + patches, not a dedicated by-design mandate; DORA is partial at D-07.1 with secure-by-design operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme; SR-DORA-004 partial mapping preserved)
emergent_tensions: 0
```
**Objective.** Security is integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency.
