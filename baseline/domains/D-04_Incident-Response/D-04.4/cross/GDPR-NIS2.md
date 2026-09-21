# D-04.4 — Pair analysis: GDPR ↔ NIS 2

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ NIS2

**GDPR article (verbatim):**
> Art. 32(1)(c) requires, among the security measures the controller and processor must implement, the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.

**NIS2 article (verbatim):**
> Article 21(2)(c) of Directive (EU) 2022/2555 requires essential and important entities to take measures regarding business continuity, such as backup management and disaster recovery, and crisis management (OJ L 333, 27.12.2022, p. 127).

**Scope comparison:**
- GDPR scope: availability and access to personal data.
- NIS2 scope: business continuity, backup management, disaster recovery and crisis management for essential/important entities.
- Scope overlap: Conditional when a controller is also a NIS2 entity and the affected systems support personal-data processing.

**Trigger comparison:**
- GDPR trigger: physical or technical incident affecting personal-data availability/access.
- NIS2 trigger: continuous BC/DR/CM obligation, activated by operational disruption.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- GDPR: timely manner, operationalised by tested recovery objectives.
- NIS2: appropriate and proportionate BC/DR/CM triad.
- Tension: NONE.

**Recipient comparison:**
- GDPR: supervisory evidence path; data subjects indirectly through service restoration.
- NIS2: competent authority or CSIRT evidence path where incident reporting applies.

**Content template comparison:**
- GDPR: restoration ability and tested recovery evidence for personal data.
- NIS2: BC plan, backup records, DR tests and crisis-management records.

**Classified relationship (from CRDA):** COMPLEMENTARY

**Verified relationship (after OJ-text analysis):** SAME — COMPLEMENTARY

**Reasoning (1-2 paragraphs):** GDPR states the restoration outcome for personal data. NIS2 supplies the broader operational-resilience framework that makes the outcome achievable. The two are not equal because NIS2 reaches wider business continuity and crisis management, while GDPR remains personal-data-specific.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: any contradiction claim would be scope-incorrect; CRDA classified this pair as complementary.

**Downstream implication (1-2 sentences):** Doc 07 should use the NIS2 BC/DR framework to evidence GDPR's timely-restoration requirement for the personal-data subset.


## Summary (Domain Analysis)

<!-- pair: GDPR,NIS2 -->
| GDPR ↔ NIS2 | **complementary** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-024, Art. 32(1)(b)/(c) + Art. 5(1)(f)) | Timely availability restoration after physical/technical incident |  |
|   → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-024 |
| **NIS2** (SR-NIS2-019, Art. 21(2)(c)) | BC + backup + disaster recovery + crisis management triad |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-019 |

**Why complementary**: GDPR mandates the *outcome* (timely restore of personal-data availability); NIS2 mandates the *infrastructure* (BC+DR+CM triad). A NIS2-compliant BC framework operationalises the GDPR Art. 32(1)(c) `timely manner` requirement. The `timely` anchor in GDPR is VAG (no specific deadline), which is resolved by NIS2's all-hazards BC framework cadence.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
42 lines — see ../../_migration_report.md)_

