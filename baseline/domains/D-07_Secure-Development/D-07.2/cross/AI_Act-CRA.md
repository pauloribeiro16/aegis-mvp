# D-07.2 — Pair analysis: CRA ↔ AI Act

> Cross-regulation layer: consult only when BOTH regulations are applicable.
> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).

##### Pair: CRA ↔ AI_Act

**CRA article (verbatim, Annex I Part I (2)(j) + (2)(k)):**
> [as quoted above]

**AI_Act article (verbatim, Art. 15(4)–(5)):**
> "High-risk AI systems shall … be designed and developed with appropriate technical and organisational measures to … (a) … (b) enable the AI systems to effectively resist, as appropriate, to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws." — Art. 15(4) AI Act (per the SR-AIACT-016 reading)

**Scope comparison:**
- CRA scope: product-level coding outcomes (attack-surface reduction, exploit mitigation) — generic product coding.
- AI Act scope: AI/ML-specific attack defence (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws).
- Scope overlap: **Conditional (Y when the CRA-regulated product is an AI-enabled product with high-risk AI components).**

**Trigger comparison:**
- CRA trigger: product design/development.
- AI Act trigger: high-risk AI system design/development.
- Trigger alignment: **DIFFERENT** (generic product vs. AI-specific).

**Threshold/timeline comparison:**
- CRA: qualitative.
- AI Act: qualitative.
- Tension: **NONE**.

**Recipient comparison:**
- CRA: MSA.
- AI Act: MSA, AI Office.

**Content template comparison:**
- CRA: Annex VII §2 design/development documentation.
- AI Act: QMS design-control + Annex IV + Art. 15(4)/(5) attack-defence measures.

**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** CRA covers conventional product coding practices (attack-surface, exploitation); AI Act covers AI/ML-specific attacks (data/model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) per SR-AIACT-016. For AI-enabled products, both apply — CRA Annex I (2)(j)/(k) plus AI Act Art. 15(4)-(5) — but the AI Act defence categories do not substitute for CRA's outcome-level obligations.

**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Conditional (Y for AI-enabled high-risk products; N for CRA-regulated products without AI)**. No reclassification required.

**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation must produce a layered coding-defence stack for AI-enabled CRA products: CRA Annex I (2)(j)/(k) generic coding + AI Act Art. 15(4)/(5) AI-specific attack-defence.

---


## Summary (Domain Analysis)

<!-- pair: CRA,AI_Act -->
| CRA ↔ AI_Act | **complementary** | Tension/difference |
|---|---|---|
| **CRA** (SR-CRA-067, Annex I Part I (2)(j); SR-CRA-068, Annex I Part I (2)(k)) | Attack-surface reduction + exploitation mitigation at the outcome level. | |
|   → full rationale: `../../../Regulation/CRA/02_SecurityRules_NIST.md` SR-CRA-067 / SR-CRA-068 |
| **AI_Act** (SR-AIACT-009 via Art. 15(4)-(5) — partial at D-07.2) | 6-category AI-attack defence (data/model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws). | |
|   → full rationale: `../../../Regulation/AI_Act/02_SecurityRules_NIST.md` SR-AIACT-009 |

**Why complementary**: CRA covers conventional product coding practices (attack-surface, exploitation); AI Act covers AI/ML-specific attacks. For AI-enabled products, both apply — CRA Annex I (2)(j)/(k) plus AI Act Art. 15(4)-(5) — but the AI Act defence categories do not substitute for CRA's outcome-level obligations.



_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:
41 lines — see ../../_migration_report.md)_

