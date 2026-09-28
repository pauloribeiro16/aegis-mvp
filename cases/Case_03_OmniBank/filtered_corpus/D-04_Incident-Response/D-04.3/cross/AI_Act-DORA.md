# D-04.3 — Pair analysis: DORA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: DORA ↔ AI_Act

**DORA article (verbatim):**
> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.

**AI_Act article (verbatim):**
> Art. 55(1)(c) of Regulation (EU) 2024/1689 requires providers of general-purpose AI models with systemic risk to keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them.

**Scope comparison:**
- DORA scope: financial-entity major ICT-related incidents.
- AI Act scope: high-risk AI serious incidents or GPAI systemic-risk serious incidents.
- Scope overlap: Conditional, when a financial entity deploys/provides high-risk AI or GPAI and the same event is both an ICT major incident and an AI serious incident.

**Trigger comparison:**
- DORA trigger: major ICT-related incident classification.
- AI Act trigger: serious incident under Art. 73 or Art. 55.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- DORA: without undue delay after major-incident classification.
- AI Act: 15d/10d/2d for high-risk AI; without undue delay for GPAI serious incidents.
- Tension: GENUINE if the same event triggers both; NONE if financial ICT and AI serious-incident scopes are separate.

**Recipient comparison:**
- DORA: financial competent authority and clients where Art. 19(3) applies.
- AI Act: market surveillance authorities or AI Office.

**Content template comparison:**
- DORA: major-ICT incident classification/reporting and mitigation information.
- AI Act: AI serious-incident or GPAI serious-incident information and corrective measures.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY on confirmed overlap

**Reasoning (1-2 paragraphs):** DORA and the AI Act target different regulatory objects: financial-entity ICT resilience versus AI-system/GPAI serious incidents. A financial entity can deploy high-risk AI, but the overlap is factual, not automatic.

If overlap exists, the DORA without-undue-delay route and AI Act 15/10/2-day route must be coordinated by recipient. If not, there is no single-party contradiction. The CRDA X should therefore be converted into a conditional tension.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should make DORA↔AI Act notification conditional on a financial-entity AI role and should maintain separate recipient routes for financial supervisors and AI authorities.


## Summary (Domain Analysis)

<!-- pair: DORA,AI_Act -->
| DORA ↔ AI_Act | **contradictory** | Tension/difference |
|---|---|---|
| **DORA** (SR-DORA-017, Art. 19(1) + Art. 19(3)) | `without undue delay` + client notification |  |
|   → full rationale: `../../../Regulation/DORA/02_SecurityRules_NIST.md` SR-DORA-017 |
| **AI_Act** (SR-AIACT-022 + SR-AIACT-024, Art. 73(1)–(4) + Art. 55(1)(c)) | 15d/10d/2d (high-risk) + `without undue delay` (GPAI) to AI Office |  |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-022, SR-AIACT-024 |

**Why contradictory (timeline)**: DORA's `without undue delay` is functionally shorter than AI Act's 15d default but longer than AI Act's 2d (widespread). For a financial entity deploying high-risk AI, DORA's `without undue delay` must bind to its minimum operational interpretation (consistent with NIS2 24h/72h structure via DORA Art. 19(2) RTS/ITS). AI Act's 15d applies as a separate recipient track.



## Deep analysis — Part 3 rendering (differs from Part 1 §1)

##### Pair: DORA ↔ AI_Act

**DORA article (verbatim):**
> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.

**AI_Act article (verbatim):**
> Art. 55(1)(c) of Regulation (EU) 2024/1689 requires providers of general-purpose AI models with systemic risk to keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them.

**Scope comparison:**
- DORA scope: financial-entity major ICT-related incidents.
- AI Act scope: high-risk AI serious incidents or GPAI systemic-risk serious incidents.
- Scope overlap: Conditional, when a financial entity deploys/provides high-risk AI or GPAI and the same event is both an ICT major incident and an AI serious incident.

**Trigger comparison:**
- DORA trigger: major ICT-related incident classification.
- AI Act trigger: serious incident under Art. 73 or Art. 55.
- Trigger alignment: PARTIAL.

**Threshold/timeline comparison:**
- DORA: without undue delay after major-incident classification.
- AI Act: 15d/10d/2d for high-risk AI; without undue delay for GPAI serious incidents.
- Tension: GENUINE if the same event triggers both; NONE if financial ICT and AI serious-incident scopes are separate.

**Recipient comparison:**
- DORA: financial competent authority and clients where Art. 19(3) applies.
- AI Act: market surveillance authorities or AI Office.

**Content template comparison:**
- DORA: major-ICT incident classification/reporting and mitigation information.
- AI Act: AI serious-incident or GPAI serious-incident information and corrective measures.

**Classified relationship (from CRDA):** CONTRADICTORY

**Verified relationship (after OJ-text analysis):** CORRECTED — SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY on confirmed overlap

**Reasoning (1-2 paragraphs):** DORA and the AI Act target different regulatory objects: financial-entity ICT resilience versus AI-system/GPAI serious incidents. A financial entity can deploy high-risk AI, but the overlap is factual, not automatic.

If overlap exists, the DORA without-undue-delay route and AI Act 15/10/2-day route must be coordinated by recipient. If not, there is no single-party contradiction. The CRDA X should therefore be converted into a conditional tension.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? Conditional
- If N or Conditional: the CRDA "contradictory" classification is **scope-incorrect** as a baseline; it should be conditional.

**Downstream implication (1-2 sentences):** Doc 07 should make DORA↔AI Act notification conditional on a financial-entity AI role and should maintain separate recipient routes for financial supervisors and AI authorities.


---
