# D-07.1 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim, Art. 25(1)):**
> "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller shall … implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing in order to meet the requirements of this Regulation and protect the rights of data subjects." — Art. 25(1) GDPR

**NIS2 article (verbatim, Art. 21(2)(e)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (e) security in acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure." — Art. 21(2)(e) NIS 2

**Scope comparison:**
- GDPR scope: controller's means-determination and ongoing processing of personal data; data-protection properties (minimisation, pseudonymisation) integrated by design.
- NIS 2 scope: entity-level lifecycle security of network and information systems (NIS) across three coordinated phases: acquisition, development, maintenance.
- Scope overlap: **Y (when the same entity is both a controller and an NSIE processing personal data through NIS).**

**Trigger comparison:**
- GDPR trigger: controller's means-determination for personal-data processing.
- NIS 2 trigger: design / development / maintenance activity on NIS.
- Trigger alignment: **DIFFERENT** (data-protection focus vs. NIS-lifecycle focus) but co-applicable on the same product/system.

**Threshold/timeline comparison:**
- GDPR: no quantitative threshold; proportionality is qualitative, anchored in `state of the art`, cost, nature, scope, context, purposes, risks.
- NIS 2: no quantitative threshold; Art. 21(1) appropriate-and-proportionate is qualitative, with Recital 56 anchoring proportionality factors.
- Tension: **NONE** (both qualitative proportionality).

**Recipient comparison:**
- GDPR: supervisory authority (DPA), data subjects.
- NIS 2: management body, competent authority.

**Content template comparison:**
- GDPR: not codified; demonstrated via Art. 5(2) accountability (documented necessity assessment, often via DPIA).
- NIS 2: not codified for by-design content; entity-discretionary methodology under Recital 56.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 25(1) requires *what* must be designed in (data-protection properties via pseudonymisation and minimisation); NIS 2 Art. 21(2)(e) requires *that* secure lifecycle discipline applies across acquisition/development/maintenance. The two regimes stack at the same controller-NSIE entity, with the GDPR by-design outputs (pseudonymised-by-default pipelines) realised through the NIS 2 acquisition gate (supplier SDLC assessment) and development gate (in-house secure-by-design decisions per SR-NIS2-027). The OJ literal text does not contradict; the joint addressee discharges both obligations with distinct evidence trails.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y (when the controller-NSIE designs NIS that processes personal data).** No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a joint by-design stack: GDPR Art. 25(1) outputs (data-protection properties) become inputs to the NIS 2 Art. 21(2)(e) lifecycle evidence trail.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-039, Art. 25(1); SR-GDPR-040, Art. 25(1)+32(1)(a); SR-GDPR-041, Art. 25(2)) | Privacy-by-design embedded at means-determination; pseudonymisation + minimisation as the canonical techniques. | |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-039 / SR-GDPR-040 / SR-GDPR-041 |
| **NIS2** (SR-NIS2-026, Art. 21(2)(e) acquisition; SR-NIS2-027, Art. 21(2)(e) development; SR-NIS2-028, Art. 21(2)(e) maintenance) | Security in acquisition, development, and maintenance of NIS across the lifecycle. | |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-026 / SR-NIS2-027 / SR-NIS2-028 |

**Why complementary**: GDPR is process-oriented and prescribes by-design techniques (minimisation, pseudonymisation); NIS 2 is outcome-oriented and prescribes the lifecycle phases (acquisition/development/maintenance) without enumerating techniques. An entity can implement both by aligning the GDPR by-design outputs (pseudonymised-by-default pipelines) with the NIS 2 acquisition gate (supplier SDLC assessment).



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_