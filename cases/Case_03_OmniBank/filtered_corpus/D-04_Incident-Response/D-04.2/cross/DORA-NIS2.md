# D-04.2 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2)(b) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding incident handling. Article 6(8) defines `incident handling` as all actions and procedures aiming at, where appropriate, preventing, detecting, analysing, containing and responding to and recovering from an incident.

**DORA article (verbatim):**
> Art. 11(1) requires financial entities to put in place a comprehensive ICT business continuity policy. Art. 11(2) requires financial entities to implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms aiming to (a)–(e).

**Scope comparison:**
- NIS2 scope: entity-level incident-handling `contain` phase.
- DORA scope: financial-entity BC policy and BC implementation arrangements including containment plans under Art. 11(2)(c).
- Scope overlap: Conditional where a DORA financial entity is also within retained NIS2 scope.

**Trigger comparison:**
- NIS2 trigger: significant incident under Art. 23(3).
- DORA trigger: ICT-related incident under Art. 17(1).
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: lifecycle-phase content.
- DORA: dedicated plans activated without delay per Art. 11(2)(c).
- Tension: NONE.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- DORA: competent authority and clients per Art. 19.

**Content template comparison:**
- NIS2: containment action records.
- DORA: dedicated plans, procedures, mechanisms per Art. 11(2) chapeau + (a)–(e).

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** The OJ text supports complementarity. NIS2 mandates the lifecycle phase; DORA specifies that for financial entities, the phase must be operationalised through dedicated, appropriate and documented arrangements subject to independent internal audit for non-microenterprises. A financial entity already subject to DORA exceeds the NIS2 containment requirement for the financial-services subset of incidents.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should treat DORA BC arrangements as satisfying NIS2 containment for the financial-sector subset, with the NIS2 chapeau coverage recorded as the additional layer.


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **complementary** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-008, Art. 21(2)(b)) | Six-action incident-handling — `contain` phase |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-008 |
| **DORA** (SR-DORA-013 + SR-DORA-014, Art. 11(1)–(3)) | BC policy + dedicated arrangements (response/recovery plans) |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-013, SR-DORA-014 |

**Why complementary**: NIS2 mandates the lifecycle phase exists; DORA specifies that for financial entities, the phase must be operationalised through dedicated, appropriate, and documented arrangements subject to independent internal audit. A financial entity already subject to DORA exceeds the NIS2 containment requirement for the financial-services subset of incidents.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_