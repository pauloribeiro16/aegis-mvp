# D-04.1 — Pair analysis: NIS 2 ↔ DORA

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ DORA

**NIS2 article (verbatim):**
> Article 21(2) chapeau introduces the all-hazards approach, which requires the detection capability to cover cybersecurity, operational, and physical-environment hazards affecting network and information systems (Recital 56). Article 21(2)(b) requires the detection dimension of incident handling.

**DORA article (verbatim):**
> Art. 10(1) requires financial entities to have in place mechanisms to promptly detect anomalous activities, in accordance with Art. 17, including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure.

**Scope comparison:**
- NIS2 scope: all-hazards entity detection.
- DORA scope: ICT-specific threat-class-categorised detection.
- Scope overlap: Conditional where a DORA financial entity is also within retained NIS2 scope.

**Trigger comparison:**
- NIS2 trigger: detection of an adverse event affecting service continuity.
- DORA trigger: detection of anomalous ICT activities, performance issues, SPOFs.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: 24h/72h/1m tiered reporting clocks.
- DORA: without undue delay, with Art. 18 classification thresholds.
- Tension: NONE.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- DORA: competent authority and clients.

**Content template comparison:**
- NIS2: severity, impact, IoCs.
- DORA: classification-driven notification content.

**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE

**Verified relationship (after OJ-text analysis):** SAME — DIFFERENT-PERSPECTIVE

**Reasoning (1-2 paragraphs):** The OJ text supports the CRDA classification. NIS2 is all-hazards (Recital 56); DORA is ICT-specific. A financial entity subject to DORA Art. 10 satisfies the NIS2 detection obligation for the ICT-hazard subset, but must extend detection to physical and operational hazards per the NIS2 chapeau.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect**; it should be "scope-disjoint" in baseline. This pair was not classified contradictory.

**Downstream implication (1-2 sentences):** Doc 07 should extend DORA detection to the NIS2 all-hazards envelope, with the chapeau coverage recorded as the additional layer.


## Summary (Domain Analysis)

<!-- pair: NIS2,DORA -->
| NIS2 ↔ DORA | **different-perspective** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-009, Art. 21(2) chapeau + (b)) | All-hazards monitoring to surface adverse events |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-009 |
| **DORA** (SR-DORA-011 + SR-DORA-012, Art. 10(1)–(2)) | Multi-class anomalous-activity detection + threshold-driven response triggering |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-011, SR-DORA-012 |

**Why different-perspective**: NIS2 is all-hazards and entity-wide (any incident affecting service continuity); DORA is ICT-specific and threat-class-categorised (anomalous activity, ICT incidents, performance issues, SPOFs). A financial entity already subject to DORA Art. 10 satisfies the NIS2 detection obligation for the ICT-hazard subset, but must extend the detection envelope to cover physical and operational hazards per NIS2 chapeau.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

