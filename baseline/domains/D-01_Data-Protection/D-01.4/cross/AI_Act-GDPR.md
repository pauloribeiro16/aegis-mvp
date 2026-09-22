# D-01.4 — Pair analysis: GDPR ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: GDPR ↔ AI_Act

**GDPR article (verbatim — SR-GDPR-005, Art. 5(1)(d)):**
> Art. 5(1)(d) personal data must be accurate and, where necessary, kept up to date … erased or rectified without delay.

**AI Act article (verbatim — SR-AIACT-015, Art. 15(3)):**
> Art. 15(3) High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment … The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans.

**Scope comparison:**
- GDPR: personal-data accuracy + integrity.
- AI Act: AI-system resilience via backup/fail-safe plans (resilience, not integrity in the technical sense).
- Scope overlap: Y when a high-risk AI system processes personal data (e.g. credit scoring, hiring, biometric identification).

**Trigger comparison:**
- GDPR: continuous + Art. 16 request.
- AI Act: continuous + lifecycle-consistency (Art. 15(1) "perform consistently throughout their lifecycle").
- Trigger alignment: PARTIAL — both continuous; AI Act adds the lifecycle-consistency sub-trigger.

**Threshold/timeline comparison:**
- GDPR: "reasonable step" + "without delay".
- AI Act: "as resilient as possible" (R3 state-of-the-art per SR-AIACT-015 ambiguity_notes).
- Tension: NONE — different objects (personal-data accuracy vs AI-system resilience to errors/faults/inconsistencies).

**Recipient comparison:**
- GDPR: SA + data subjects.
- AI Act: conformity-assessment body (ex ante) + market-surveillance authority (ex post) + AI Office for GPAI.

**Content template comparison:**
- GDPR: Art. 16 + Art. 19 rectification cascade.
- AI Act: technical-redundancy solutions (backup or fail-safe plans) per Art. 15(3).

**Classified relationship (from CRDA):** DIFFERENT PERSPECTIVE.

**Verified relationship (after OJ-text analysis):** SAME (CORRECTED — wording only).

**Reasoning:** The two target different objects (personal-data semantic accuracy + storage integrity vs AI-system resilience to errors/faults/inconsistencies via backup/fail-safe) and use different CSF anchors (GDPR PR.DS-01 + ID.AM-08 + PR.DS-10 vs AI Act PR.IR-03 + PR.IR-04 + PR.DS-11). CRDA's DIFFERENT PERSPECTIVE correctly identifies the framing difference; under the 5-option taxonomy the relationship is better described as COMPLEMENTARY (the data accuracy property coexists with the system resilience property on the same AI-system-using-personal-data asset). The objects are nested: AI-system resilience sits inside the storage stack that GDPR's PR.DS-01 protects; GDPR accuracy sits inside the AI-system lifecycle that Art. 15(1) constrains.

**Scope-disjoint test:** Y when a GDPR controller deploys a high-risk AI system processing personal data.

**Downstream implication:** Layered-objects sub-domain: a controller-provider relationship must document both objects separately. Same-flag: CRDA classification stands under the 4-option framing; under the 5-option framing the pair is COMPLEMENTARY on the same asset.

---


## Summary (Domain Analysis)

<!-- pair: GDPR,AI_Act -->
| GDPR ↔ AI_Act | **Different perspective** | Tension/difference |
|---|---|---|
| **GDPR** (SR-GDPR-005 + SR-GDPR-006, Art. 5(1)(d) + Art. 16) | Accuracy of stored personal data; rectification with cascade | Personal-data scope; semantic accuracy + storage integrity |
| **AI_Act** (SR-AIACT-014 + SR-AIACT-015, Art. 15(1)+(3)) | Accuracy + robustness + cybersecurity (3-way AND); resilience to errors/faults/inconsistencies (Art. 15(3) backup/fail-safe) | High-risk AI provider; AI-system-level; resilience rather than integrity; `accuracy, robustness, cybersecurity` is a 3-way AND POLY (each term inquiry-resistant; partial compliance undefined) |

**Why Different perspective**: GDPR's integrity obligation is data-centric and tied to the accuracy principle. AI Act's resilience obligation is system-centric and tied to the AI-specific risk-management system; "as resilient as possible" is the literal standard. The two converge on a controller-provider relationship when an AI system processes personal data: GDPR's data-accuracy + AI Act's system-resilience, each enforced separately. They are not contradictory because they target different objects (data vs system). → full rationale: `../../../Regulation/GDPR/02_SecurityRules_NIST.md` SR-GDPR-005; `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-014 + SR-AIACT-015



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
43 lines — see ../../_migration_report.md)_