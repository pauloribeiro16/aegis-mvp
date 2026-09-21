# D-04.3 — Pair analysis: NIS 2 ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: NIS2 ↔ AI_Act

**NIS2 article (verbatim):**
> Article 23(4)(a) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact (OJ L 333, 27.12.2022, p. 129).

**AI_Act article (verbatim):**
> Art. 73(1)–(4) of Regulation (EU) 2024/1689 requires providers of high-risk AI systems, and deployers where applicable, to report any serious incident to the market surveillance authorities of the Member States where the incident occurred. The reporting timeline depends on the severity: 15 days after the provider becomes aware (default), 10 days if the incident results in death, 2 days for widespread infringement.

**Scope comparison:**
- NIS2 scope: essential/important entity significant incidents.
- AI Act scope: high-risk AI serious incidents and GPAI serious incidents.
- Scope overlap: Conditional, when a NIS2 entity is also the provider/deployer and the same AI event is a NIS2 significant incident.

**Trigger comparison:**
- NIS2 trigger: significant incident.
- AI Act trigger: serious incident under Art. 73 or GPAI serious incident under Art. 55.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- NIS2: 24h early warning, 72h notification, 1m final.
- AI Act: 15d default, 10d death, 2d widespread infringement; GPAI without undue delay.
- Tension: GENUINE if same-party/same-event overlap; NONE if AI and NIS2 scopes are separate.

**Recipient comparison:**
- NIS2: CSIRT or competent authority.
- AI Act: market surveillance authorities, or AI Office for GPAI.

**Content template comparison:**
- NIS2: significant-incident severity, impact, suspected cause and IoCs.
- AI Act: serious-incident severity, causal/awareness trigger and corrective measures.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONTRADICTORY on confirmed same-party overlap

**Reasoning (1-2 paragraphs):** The CRDA X is correct only for the overlap branch. The AI Act does not govern all NIS2 incidents; NIS2 does not govern all AI serious incidents. The same organisation can be both a NIS2 entity and an AI provider/deployer, but that must be established by role and event facts.

When both apply, NIS2's 24-hour early warning is earlier than the AI Act's default 15-day and death 10-day clocks, while the AI Act 2-day widespread-infringement clock competes with the NIS2 24-hour tier. This is a real timeline-orchestration issue, not a universal contradiction.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should treat NIS2 and AI Act as parallel recipient routes only after confirming both entity role and AI-system incident classification.


## Summary (Domain Analysis)

<!-- pair: NIS2,AI_Act -->
| NIS2 ↔ AI_Act | **contradictory** | Tension/difference |
|---|---|---|
| **NIS2** (SR-NIS2-010–013, Art. 23(4)(a)–(e)) | 24h/72h/1m tiered notification |  |
|   → full rationale: `../../../Regulation/NIS2/02_SecurityRules_NIST.md` SR-NIS2-010, SR-NIS2-011, SR-NIS2-012, SR-NIS2-013 |
| **AI_Act** (SR-AIACT-022, Art. 73(1)–(4)) | 15d default + 10d (death) + 2d (widespread infringement) |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-022 |

**Why contradictory (timeline)**: NIS2's tightest tier is 24h; AI Act's tightest trigger is 2d (widespread infringement), with 15d default. NIS2's 24h binds for essential/important entities; AI Act's 15d applies to high-risk AI providers/deployers not falling under NIS2. Where both apply (NIS2-essential entity deploying high-risk AI), the NIS2 24h binds; AI Act 15d must be re-operationalised as 24h via binding-procedure principle.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
44 lines — see ../../_migration_report.md)_

