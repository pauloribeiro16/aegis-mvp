# D-04.4 — Pair analysis: NIS 2 ↔ CRA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ CRA

**NIS2 article (verbatim):**
> Article 21(2)(c) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management (OJ L 333, 27.12.2022, p. 127).

**CRA article (verbatim):**
> Annex I Part I (2)(h) requires products to protect the availability of essential and basic functions — also after an incident — including through resilience and mitigation measures against denial-of-service attacks.

**Scope comparison:**
- NIS2 scope: entity-level BC/backup/DR/crisis management.
- CRA scope: product-level post-incident availability and resilience.
- Scope overlap: Conditional when a NIS2 entity deploys or manufactures CRA products.

**Trigger comparison:**
- NIS2 trigger: continuous BC duty and significant-incident/crisis activation.
- CRA trigger: continuous product availability/resilience duty.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: appropriate and proportionate BC/DR/CM.
- CRA: essential and basic product functions protected also after an incident.
- Tension: NONE.

**Recipient comparison:**
- NIS2: competent authority or CSIRT evidence path.
- CRA: product users and market surveillance.

**Content template comparison:**
- NIS2: BC plan, backup management, disaster recovery and crisis management.
- CRA: product resilience, DoS mitigation and incident impact reduction.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** NIS2 is entity-level; CRA is product-level. Their controls stack: CRA product resilience reduces the likelihood and severity of entity-level recovery events, while NIS2 ensures the entity can recover even when products fail.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradiction claim would be scope-incorrect; CRDA classified this pair as complementary.

**Downstream implication (1-2 sentences):** Doc 07 should link CRA resilience evidence into the NIS2 BC/DR inventory as supporting control evidence.


## Summary (Domain Analysis)

<!-- pair: NIS2,CRA -->
| NIS2 ↔ CRA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-019, Art. 21(2)(c)) | BC + backup + DR + CM triad |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-019 |
| **CRA** (SR-CRA-043, Annex I Part I (2)(h)) | Product availability post-incident + DoS-resistance |  |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-043 |

**Why complementary**: NIS2 BC covers the entity level (the deployer's recovery); CRA resilience covers the product level (the product's continued operation). Layered: the CRA product's resilience reduces the load on the NIS2 BC framework.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

