<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-07.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-07.2 Secure Coding Practices](../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.2.md)
#### D-07.2 Secure Coding Practices
<!-- participants: CRA, DORA, AI_Act -->
**Participants (from CRDA):** CRA, DORA, AI_Act
**Sole-authority note (CRDA flag):** AEGIS taxonomy §4.1 marks DORA as sole authority for D-07.2 Secure Coding Practices. The OJ Art. 9(4)(f) text is on `patches and updates` (patch-management policy) — not coding standards. Per SR-DORA-007 v0.2 audit, this pilot finds no OJ-text support for the DORA sole-authority assignment and recommends Layer 2 review (see P0 disagreement report).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-07.2 Secure Coding Practices
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.2.md`](../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.2.md)
> (3 pairs verified against OJ text — **3 participating regulations
> are CRA, DORA (partial), AI Act (partial) with GDPR and NIS 2
> explicitly out-of-scope** as noted by `DomainAnalysis/D-07_Secure-Development/D-07.2.md`
> line 27: "Participants (from CRDA): CRA, DORA, AI_Act"; and the
> DomainAnalysis out-of-scope notes line 31-32: "GDPR is process- and
> outcome-oriented; it does not specify secure-coding practices ...
> NIS2 ... OJ Art. 21(2)(e) does not mention CI/CD pipeline, secure
> coding standards, or specific coding practices").
>
> **P0 disagreement ON PARTICIPATION (per CRDA-deep §D-07.2):** the AEGIS
> taxonomy §4.1 marks DORA as the SOLE AUTHORITY for D-07.2. The CRDA-deep
> OJ-text verification finds no OJ-text support for this assignment
> (Art. 9(4)(e) is on change-management policies; Art. 9(4)(f) is on
> patches and updates — no OJ clause prescribes coding standards).
> DORA-side participation is preserved here as **partial** per
> SR-DORA-023 (Art. 9(4)(e) D-07.4 primary, D-07.2 partial by inference
> only).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-07.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR is process- and outcome-oriented; it does not specify secure-coding practices. The AEGIS taxonomy notes DORA as the sole authority for D-07.2 (per the D-07.2 GDPR SO file `01_SecurityObjectives.md` line 213 — "GDPR is outcome-oriented; DORA is sole authority"). **CRDA-deep note:** the sole-authority claim is disputed per the OJ-text verification — see the P0 disagreement block above. | — |
| NIS2 | (out-of-scope) | T3-vs-text gap (synthesis §8, T3 NIS2-C11): OJ Art. 21(2)(e) does not mention CI/CD pipeline, secure coding standards, or specific coding practices. AEGIS taxonomy marks DORA as the sole authority. **CRDA-deep note:** the sole-authority claim is disputed per the OJ-text verification — see the P0 disagreement block above. | — |
| CRA | SO-CRA-046 (partial) | A product with digital elements is designed, developed, and produced to limit attack surfaces — including external interfaces — and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation). | **Product-level outcome mandates** (limit attack surface, mitigate exploitation) — not coding-standard mandates. The CRA-side participation at D-07.2 is **partial** in the SR sense (outcome-level obligations routed from Annex I; no specific coding-standard mandate in OJ). |
| DORA | (no OJ-mandated D-07.2 SO; partial via SO-DORA-013 Art. 9(4)(e) — D-07.4 primary) | No dedicated secure-coding mandate in OJ; AEGIS taxonomy §4.1 marks DORA as sole authority but OJ-literal text is silent. **T4-vs-text gap awareness:** T4 maps DORA-C19 (Art. 9(4)(f) patches and updates) to D-07.2 but the OJ text is about patch-management policies, not coding practices. The SR-DORA-023 Art. 9(4)(e) change-management **partially** maps to D-07.2 as inference only (D-07.4 primary). | **Entity-level process** (six-step change management per Art. 9(4)(e) — recorded/tested/assessed/approved/implemented/verified). The DORA-side participation at D-07.2 is **partial** by inference (Art. 9(4)(e) change-mgmt implies secure-coding dimension through testing-vulnerability-assessments + source-code-reviews as part of the testing modalities per Art. 25, but no OJ-mandated coding-standard prescription). |
| AI_Act | SO-AIACT-009 (partial via Art. 15(4)–(5)) | High-risk AI systems … be designed and developed with appropriate technical and organisational measures to … (b) enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws — Art. 15(4)–(5) per the SR-AIACT-016 reading. | **AI/ML-focused secure-coding dimension** — 6 AI-attack-defence categories enumerated (data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws). The AI-Act-side participation at D-07.2 is **partial** in the SR sense (AI-attack-defence categories do not map to conventional secure-coding mandates). |

## Validated relationships (from CRDA-deep §D-07.2)

#### Validated relationships (from CRDA-deep §D-07.2)
Of 3 pairs, **3 verified as SAME — COMPLEMENTARY (all CRDA initial classifications held after OJ-text analysis)**: no CORRECTED, no CONTRADICTORY **BUT with substantial scope-disjoint qualifiers on 2 of 3 pairs in baseline** — CRA↔DORA = N (typically) — substantively scope-disjoint because distinct actors handle distinct objects (manufacturer-side product coding outcomes vs financial-entity-side process change-management); CRA↔AI_Act = SAME — COMPLEMENTARY with Conditional Y scope overlap (for AI-enabled CRA products the same product is both CRA-regulated and AI-Act-high-risk); DORA↔AI_Act = N (typically) — substantively scope-disjoint because distinct actors handle distinct objects (financial-entity-side process change-management vs AI-system-coding). The three regulators look at secure-coding from three distinct regulatory perspectives that **DO NOT stack on the same party in baseline**:
- **CRA ↔ DORA** — COMPLEMENTARY (SAME) (CRDA classification preserved; **but with scope-disjoint qualifier per OJ-literal reading** — CRDA-deep notes the 'complementary' label is more a taxonomy artifact than a substantive relationship): CRA Annex I Part I (2)(j) + (2)(k) specifies **product-level outcomes** (attack-surface reduction, exploitation mitigation) — the manufacturing side of the supply chain; DORA Art. 9(4)(e) specifies **entity-level process** (change-management six-step: recorded/tested/assessed/approved/implemented/verified) — the financial-entity side of the supply chain. The two regimes do not overlap substantively on coding practices — CRA covers the product, DORA covers the process. **No DORA SR exists for D-07.2 from OJ-literal text** (the SR-DORA-023 audit confirms Art. 9(4)(f) is patch-management policy, not coding standards). When a financial entity deploys a CRA-regulated product, the manufacturer (CRA-bound) has done the product-side Annex I coding-outcomes; the financial entity (DORA-bound) does the change-mgmt six-step on the deployed product. The scope-disjoint test: **N (typically)** — different objects (product coding outcomes vs entity change process), different actors (manufacturer vs financial entity). Pair is scope-disjoint in the OJ-literal reading.
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME): CRA covers **conventional product coding practices** (attack-surface, exploitation); AI Act covers **AI/ML-specific attacks** (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws) per SR-AIACT-016. For an **AI-enabled CRA product** (CRA-regulated product that embeds a high-risk AI system), both regimes apply — CRA Annex I (2)(j) + (2)(k) plus AI Act Art. 15(4)–(5) — but the AI Act defence categories do not substitute for CRA's outcome-level obligations. The scope-disjoint test: **Conditional (Y when the CRA-regulated product is an AI-enabled product with high-risk AI components; N for CRA-regulated products without AI)**.
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME) (CRDA classification preserved; **but with scope-disjoint qualifier per OJ-literal reading** — CRDA-deep notes the 'sole authority' taxonomy assignment for DORA at D-07.2 is a taxonomy artifact that requires Layer 2 review; **no OJ mandate for coding standards in DORA**): No OJ-level overlap. AI Act addresses AI/ML coding (Art. 15(4)–(5)); DORA addresses process change-management (Art. 9(4)(e)). The "sole authority" taxonomy assignment for DORA at D-07.2 is a taxonomy artifact that requires Layer 2 review — no OJ mandate for coding standards in DORA. When a DORA financial entity deploys high-risk AI, both regimes apply at different layers: **DORA change-management gate (Art. 9(4)(e)) + AI Act AI-specific attack-defence (Art. 15(4)–(5))**. The scope-disjoint test: **N (typically)** — different objects (entity process vs AI-system coding), different actors, different lifecycle stages. Pair is substantively scope-disjoint; CRDA "complementary" is a taxonomy artifact.
The secure-coding architecture is **legitimately diverse with substantial scope-disjoint structure** — each regulator targets a **distinct target object** (product-level coding outcomes [attack-surface + exploitation] / entity-level process [change-mgmt six-step with implicit coding-dimension inference — no OJ mandate] / AI-system-level attack-defence [6 AI/ML-specific categories]) at a **distinct trigger** (manufacturer places product on market [Annex I Part I chapeau] / financial entity ICT change event [Art. 9(4)(e)] / high-risk AI system design/development [Art. 15(4)–(5)]) with a **distinct obligation anchor** (CRA `attack-surface limitation + exploitation-mitigation` outcome mandate / DORA `recorded/tested/assessed/approved/implemented/verified` change-mgmt process mandate with implicit coding-inference dimension / AI Act 6-category AI-attack-defence mandate). The high-level SO surfaces the **common secure-coding duty** (attack-surface limitation + exploitation mitigation + AI-attack-defence + appropriate coding-practice evidence base — typically built from industry frameworks NIST SSDF + OWASP SAMM + ISO/IEC 27034 since no OJ clause prescribes specific coding standards) while preserving the **per-reg target object** and acknowledging the **substantial scope-disjoint structure on 2 of 3 pairs in baseline**. The high-level SO does **NOT** engage on the baseline 2-of-3 N scope-disjoint pairs in the typical integrated stack; it engages only on the Conditional-Y integrated stack (when an AI-enabled CRA product is also deployed by a DORA financial entity — the vertically-integrated manufacturer-controller-deployer stack).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  CRA  |
| --- | --- |
|  **CRA**  |  —  |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional Y** = scope overlap only under specific circumstances (AI-enabled CRA product — vertically-integrated manufacturer-controller-deployer stack). **N (typically)** = scope-disjoint in baseline (distinct actors, distinct objects, distinct supply-chain levels). CRDA-deep scope-disjoint tests: **CRA↔DORA = N (typically)** (substantive scope-disjoint because distinct actors handle distinct objects — manufacturer-side product coding outcomes vs financial-entity-side process change-management); **CRA↔AI_Act = Conditional Y** (Y for AI-enabled high-risk CRA products; N for CRA-regulated products without AI); **DORA↔AI_Act = N (typically)** (substantive scope-disjoint because distinct actors handle distinct objects — financial-entity-side process change-management vs AI-system-coding). **The high-level SO engages only on the Conditional-Y integrated stacks**; on the 2-of-3 N scope-disjoint baseline pairs, the high-level SO does **NOT** engage in baseline.

## Cross-recipient map

#### Cross-recipient map
D-07.2 generates partial recipient fragmentation at the **coding-standards evidence layer** but does **not generate a notification cascade of D-07.2 itself** (the coding-practices baseline is the upstream operational instrument for the secure-by-design decision at D-07.1 and the secure-development-procedures supplier-assessment three-prong at D-06.1). The recipient set is at the **coding-evidence layer**: **CRA's market surveillance authority (MSA)** on the Annex VII §2 design/development documentation (cross to D-09.4 — SO-CRA-059) + Annex VII §3 risk-assessment record (cross to D-09.2 — SO-CRA-053) — the Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation outcomes are demonstrated through the design/development documentation; **DORA's competent authority (national financial supervisory authority)** on the Art. 9(4)(e) change-management six-step policy + Art. 25 testing modalities (source-code reviews, vulnerability assessments, penetration testing as part of the 12-way open testing-modality list per SO-DORA-005) — the DORA-side coding dimension is implicit in the change-mgmt six-step's `tested` and `assessed` legs + the Art. 25 testing modalities (no OJ-mandated coding-standards receipt; SR-DORA-023 partial at D-07.2 by inference only — see P0 disagreement above); **AI Act's provider / MSA / AI Office** on the QMS documented design-control procedures (Art. 17(1)(c) — design/design control/design verification) + Annex IV technical documentation + the Art. 15(4)–(5) AI-attack-defence measures (SR-AIACT-016) — the AI Act Art. 15(4)–(5) 6-category AI-attack-defence receives coding-practices evidence on training-data-set poisoning + pre-trained-component poisoning + adversarial-example resistance + model-evasion resistance + confidentiality-attack defence + model-flaw defence. **The DORA-side coding-evidence has no OJ-mandated coding-standards receipt per the P0 disagreement** — the AEGIS-taxonomy sole-authority assignment has no OJ-text anchor; the DORA-side coding dimension is demonstrated through the change-mgmt six-step `tested` + `assessed` legs + the Art. 25 testing modalities (source-code-reviews where feasible as one modality), not through an OJ-mandated coding-standards prescription. **D-06.1 (Vendor Risk Assessment) is where the supplier-secure-development-procedures three-prong (NIS 2 Art. 21(3) sentence 1 third limb) + CRA Art. 13(5) component due diligence operate** as upstream gates that D-07.2's coding-practices baseline must satisfy; **D-07.1 (Secure-by-Design Principles) is where the by-design decision is propagated into D-07.2 as the code-level instruction** — D-07.2 is where the by-design outputs become code; **D-04.3 (Regulatory Notification) is where a downstream coding-related vulnerability manifest as a notification to MSAs and CSIRTs**. D-07.2 is the **operational downstream artefact** where the upstream by-design decision (D-07.1) + the supplier-secure-development-procedures gate (D-06.1) become code.
---

## HSO considerations (from D-07.2.0 — High-level SecurityObjective)

**Considerations.**
- 3 of 5 regulations participate (CRA, DORA partial, AI Act partial); GDPR and NIS 2 are explicitly out-of-scope (OJ Art. 25(1) does not specify secure-coding practices; OJ Art. 21(2)(e) does not mention CI/CD pipeline or secure-coding standards).
- The coding-practice evidence base is typically built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034) since no OJ clause prescribes specific coding standards.
- The three participating regulators anchor the coding-practices duty at distinct target objects: CRA `limitation of attack surfaces, including attack surfaces of external interfaces` (Annex I Part I (2)(j)) + `reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques` (Annex I Part I (2)(k)) — product-coding-outcome mandate at the manufacturer side; DORA Art. 9(4)(e) change-management six-step — entity-process mandate at the financial-entity side, with implicit coding-dimension inference through `tested`/`assessed` legs + Art. 25 testing modalities (source-code reviews where feasible) — no OJ-mandated secure-coding-standards prescription (P0 disagreement on AEGIS-taxonomy sole-authority assignment); AI Act Art. 15(4)–(5) — AI-system attack-defence mandate at the AI-system-provider side (6 categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws).
- 3 pairwise cells verified by CRDA-deep as 3 SAME — COMPLEMENTARY (no CORRECTED, no CONTRADICTORY), but with substantial scope-disjoint qualifiers on 2 of 3 pairs in baseline: CRA↔DORA = N typically (manufacturer vs financial-entity, product vs process); CRA↔AI_Act = Conditional Y on AI-enabled CRA products; DORA↔AI_Act = N typically (financial-entity process vs AI-system coding).
- The high-level SO engages only on the Conditional-Y integrated stack (when an AI-enabled CRA product is also deployed by a DORA financial entity — the vertically-integrated manufacturer-controller-deployer stack). For a 5-FTE SaaS startup with CRA applicability only, the high-level SO is NOT activated.
- The two Layer 2 review items (P0 DORA-taxonomy-disagreement + CRA outcome-level vs AI Act attack-category layered-stack requirement) are documented separately — not as CONTRADICTORY/CORRECTED reclassifications that require Phase 1C tension-resolution.
- For AI-enabled CRA products, CRA Annex I Part I (2)(j) + (2)(k) outcome-level obligations + AI Act Art. 15(4)–(5) attack-defence categories stack with **no OJ-level consolidation rule** (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9, which does not extend to coding practices).
- The per-reg perspective (target object, trigger, anchor, threshold, evidence template, recipient, legal anchor) is preserved verbatim in the three sub-SOs; the per-tier scope-disjoint structure is surfaced as a 2-of-3 N qualifier in baseline.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 3 participating regulations each define D-07.2 over a distinct **target object** of the secure-coding architecture; the target object, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on coding practices.
| Axis (reg) | Target object | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **CRA** | product-coding outcomes (attack-surface + exploitation-mitigation) at the manufacturer side | manufacturer places product on market (Annex I Part I chapeau) + ongoing during support period per Art. 13(8) | `limit its attack surfaces, including attack surfaces of external interfaces` (Annex I Part I (2)(j)) + `reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques` (Annex I Part I (2)(k)) — qualitative outcome mandates, no coding-standard mandate in OJ | market surveillance authority (MSA) — Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record | Annex I Part I chapeau + (2)(j) attack-surface + (2)(k) exploitation-mitigation + Art. 13(1) design/development/production per Annex I Part I + Art. 13(2) risk-assessment propagation across 6 phases + Annex VII §2 + Annex VII §3 |
| **DORA** | entity-process change-management six-step (recorded/tested/assessed/approved/implemented/verified) — implicit coding-dimension inference at the financial-entity side (no OJ-mandated secure-coding-standards prescription) | ICT change event at financial entity (Art. 9(4)(e) — software / hardware / firmware / system / security-parameter change) — secure-coding dimension is implicit through the `tested` and `assessed` legs + the Art. 25 testing modalities (source-code-reviews where feasible as one modality) | no OJ coding-standards mandate; implicit coding-dimension via Art. 9(4)(e) change-mgmt six-step `tested` + `assessed` legs + Art. 25 testing modalities; the AEGIS-taxonomy sole-authority assignment has no OJ-text anchor per the P0 disagreement | competent authority (national financial supervisory authority) — Art. 9(4)(e) change-mgmt policy + Art. 25 testing modalities | Art. 9(4)(e) change-mgmt six-step + Art. 25 testing modalities (12-way open list including source-code reviews) — **no OJ Art. 9(4)(f) patches-and-updates prescribing secure-coding standards** |
| **AI_Act** | AI-system attack-defence (6 AI/ML-specific attack categories) at the AI-system-provider side | high-risk AI system design/development (Art. 15(4)–(5)) | Art. 15(4) `enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use` + Art. 15(4)(b) 6-category AI-attack-defence: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws — qualitative; the Art. 15(4) `as appropriate to the AI system's purpose and conditions of use` is a proportionality qualifier at the AI-system-purpose level | provider + market surveillance authority + AI Office — QMS design-control + Annex IV technical documentation + Art. 15(4)–(5) attack-defence measures (SR-AIACT-016) | Art. 15(4) + Art. 15(5) + Art. 17(1)(c) QMS design/design-control/design-verification + Recital 78 GDPR preservation |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-07.2.HL`) engages on a given party **only if ≥2 applicable
regulations have a Y or Conditional Y scope overlap on the same party**
on the same coding event. **In baseline, only 1 of 3 pairs (CRA↔AI_Act)
has Conditional Y scope overlap on the AI-enabled CRA product
integrated stack — for a CRA-regulated product that is also an AI-Act-
high-risk AI system, the two obligations stack vertically on the same
product**. For an AI-enabled CRA product, the manufacturer does the
CRA-side Annex I Part I (2)(j) + (2)(k) product-coding-outcomes
(attack-surface + exploitation-mitigation); the AI Act Art. 15(4)–(5)
AI-attack-defence categories apply on top for the AI/ML-specific
attack resistance (data/model poisoning + adversarial examples + model
evasion + confidentiality attacks + model flaws). The two regimes DO
NOT substitute — the AI Act defence categories do not substitute for
CRA's outcome-level obligations, and the CRA outcome-level obligations
do not substitute for the AI Act defence categories. The other 2 pairs
(CRA↔DORA + DORA↔AI_Act) are N in baseline; the high-level SO does
NOT engage on these pairs. For a CRA manufacturer that is also a DORA
financial entity, the manufacturer-side CRA coding-outcomes feed the
financial-entity-side DORA change-mgmt six-step — but the pair is
scope-disjoint in baseline (distinct actors, distinct objects) and
becomes Y only on atypical layered integrated stacks. For an AI system
provider that is also a DORA financial entity, the AI-system-side AI
Act coding applies on the AI-system lifecycle while the DORA-side
change-mgmt applies on the financial-entity ICT-system lifecycle — the
pair is scope-disjoint in baseline (distinct actors, distinct
objects, distinct lifecycle stages). **The three target objects are
NOT layered on the typical integrated stack** — the per-reg coding
dimension stands on its own with the per-tier scope-disjoint structure
preserved; the high-level SO does **NOT** collapse the three target
objects into a single coding-architecture. The per-reg perspective on
target object, trigger, anchor, threshold, recipient, and evidence
template is preserved verbatim. For a 5-FTE SaaS startup with CRA
applicability only (no DORA applicability, no AI Act applicability on
the high-risk-AI-system side), only the CRA sub-SO activates; the
high-level SO is **NOT activated** because there is no Conditional Y
or Y scope overlap on a single coding event. For a CRA manufacturer
that is also a DORA financial entity that also deploys high-risk AI
(typical integrated stack with all 3 applicable regs), the high-
level SO engages only on the Conditional-Y integrated stack for the
product's coding dimension on the integrated manufacturer-controller-
deployer artefact.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **3 of 5 regulations participate** (CRA, DORA **partial**, AI Act
  **partial**; **GDPR and NIS 2 are explicitly out-of-scope** — OJ Art.
  25(1) does not specify secure-coding practices; OJ Art. 21(2)(e) does
  not mention CI/CD pipeline or secure-coding standards).
- **3 pairwise cells, verified by CRDA-deep as 3 SAME — COMPLEMENTARY
  (no CORRECTED, no CONTRADICTORY):** CRA↔DORA (SAME — COMPLEMENTARY
  with scope-disjoint qualifier per OJ-literal reading — product-side
  vs entity-side, distinct actors, distinct objects, substantively
  scope-disjoint); CRA↔AI_Act (SAME — COMPLEMENTARY with Conditional
  Y scope overlap on AI-enabled CRA products); DORA↔AI_Act (SAME —
  COMPLEMENTARY with scope-disjoint qualifier per OJ-literal reading
  — entity-side vs AI-system-side, distinct actors, distinct objects,
  substantively scope-disjoint).
- The three regulations impose **distinct secure-coding duties** at
  **distinct target objects** with **distinct triggers** and **distinct
  anchors**: CRA manufacturer-side product-coding-outcome mandate
  (Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-
  mitigation — qualitative outcome mandates with no specific coding-
  standard prescription in OJ); DORA financial-entity-side entity-
  process change-mgmt mandate (Art. 9(4)(e) recorded/tested/assessed/
  approved/implemented/verified six-step with implicit coding-
  dimension inference through the `tested` and `assessed` legs + Art.
  25 testing modalities — **no OJ-mandated secure-coding-standards
  prescription**); AI Act AI-system-provider-side AI-attack-defence
  mandate (Art. 15(4)–(5) 6-category AI-attack-defence: data/model
  poisoning + adversarial examples + model evasion + confidentiality
  attacks + model flaws — qualitative). The three regulations DO NOT
  **stacking-prescribe a single coding-standards baseline** — the
  entity must build the coding-standards baseline from industry
  frameworks (NIST SSDF, OWASP SAMM, ISO/IEC 27034) and demonstrate
  compliance against each regulation's outcome (CRA) or process (DORA)
  or AI-attack-defence (AI Act) requirement.
- The high-level SO describes the **COMMON OBJECTIVE** (attack-surface
  limitation + exploitation mitigation + AI-attack-defence +
  appropriate coding-practice evidence base typically built from
  industry frameworks since no OJ clause prescribes specific coding
  standards); the **per-regulation perspective** (target object,
  trigger, anchor, threshold, recipient, evidence template) is
  preserved verbatim in the three sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension on the coding-practices duty itself — **0 CONTRADICTORY or
  CORRECTED reclassifications** because all 3 verified pairs are SAME
  — COMPLEMENTARY. Two **Layer 2 review items** are documented
  separately (NOT as emergent_tensions): (a) **P0 DORA-taxonomy-
  disagreement** — AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY
  for D-07.2 but CRDA-deep finds no OJ-text support for that assignment
  (Art. 9(4)(e) is change-management policy; Art. 9(4)(f) is patches-
  and-updates policy; no OJ clause prescribes secure-coding standards);
  the DORA-side participation is preserved as partial per SR-DORA-023;
  (b) **CRA outcome-level vs AI Act attack-category layered-stack
  requirement** — for AI-enabled CRA products, the CRA Annex I Part I
  (2)(j) + (2)(k) outcome-level obligations + AI Act Art. 15(4)–(5)
  attack-defence categories stack with **no OJ-level consolidation
  rule** (unlike the CRA Art. 13(4) sentence 2 unified-risk-assessment
  carve-out for AI Act Art. 9, which does not extend to coding
  practices).
- **Scope caveat (CRITICAL — DORA OJ-text absence on secure-coding
  standards)** — derived from CRDA-deep verified classifications: DORA
  OJ Art. 9(4)(e) text is `documented policies, procedures and
  controls for ICT change management, including changes to software,
  hardware, firmware components, systems or security parameters …
  recorded, tested, assessed, approved, implemented and verified in a
  controlled manner`; Art. 9(4)(f) text is `documented policies for
  patches and updates`; **no OJ clause prescribes secure-coding
  standards**. AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for
  D-07.2 — this assignment has no OJ-text anchor per CRDA-deep
  verification. The DORA-side participation at D-07.2 is preserved as
  partial per SR-DORA-023 (Art. 9(4)(e) D-07.4 primary, D-07.2 partial
  by inference only). Layer 2 review item: either (a) revise the
  taxonomy to remove the DORA sole-authority assignment, or (b)
  identify the OJ clause that supports it. **For a 5-FTE financial
  entity, the DORA-side coding dimension is demonstrated through the
  change-mgmt six-step + Art. 25 testing modalities** (source-code
  reviews where feasible as one of 12 modalities per SO-DORA-005) —
  not through an OJ-mandated coding-standards prescription.
- **Scope caveat (CRITICAL — no OJ-level consolidation rule for
  coding practices)** — derived from CRDA-deep verified
  classifications: unlike the CRA Art. 13(4) sentence 2 explicit
  AI-Act-substitution carve-out for risk assessment (when both apply
  on AI-enabled CRA products), no OJ clause permits a unified
  coding-standards baseline across the three regimes. The CRA
  outcome-level obligations (Annex I Part I (2)(j) + (2)(k)) + AI Act
  attack-defence categories (Art. 15(4)–(5)) + DORA process
  obligations (Art. 9(4)(e) change-mgmt six-step) stack with distinct
  evidence templates and cannot be substituted. The entity must
  demonstrate compliance against each regulation's outcome (CRA) or
  process (DORA) or AI-attack-defence (AI Act) requirement
  independently.
- **Scope caveat (CRITICAL — substantial scope-disjoint structure on
  2 of 3 pairs in baseline)** — derived from CRDA-deep verified
  classifications: CRA↔DORA = N (typically) because distinct actors
  (manufacturer vs financial entity) handle distinct objects (product
  coding outcomes vs process change-mgmt) at distinct supply-chain
  levels (upstream vs midstream); DORA↔AI_Act = N (typically) because
  distinct actors (financial entity vs AI system provider) handle
  distinct objects (process change-mgmt vs AI-system coding) at
  distinct lifecycle stages (entity ICT-system vs AI-system). **The
  high-level SO engages only on the Conditional Y integrated stack**
  for AI-enabled CRA products — atypical integrated stacks where a
  CRA manufacturer or a CRA-regulated product is also deployed by a
  DORA financial entity or is also a high-risk AI system; for typical
  integrated stacks the high-level SO does NOT engage.
---

## Emergent tensions (from CRDA-deep §D-07.2)

#### Emergent tensions (from CRDA-deep §D-07.2)
**0 conditional emergent tensions** in the narrow CONTRADICTORY/CORRECTED sense on the coding-practices duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 3 pairs are all SAME — COMPLEMENTARY with different scope-disjoint qualifiers. **However, two structurally distinct Layer 2 review items are documented**:
**(1) P0 disagreement ON PARTICIPATION — AEGIS-taxonomy DORA sole-authority assignment has no OJ-text anchor (preserved as Layer 2 review item, per CRDA-deep §D-07.2):** the AEGIS taxonomy §4.1 marks DORA as the SOLE AUTHORITY for D-07.2 Secure Coding Practices. The CRDA-deep OJ-text verification finds **no OJ-text support** for this assignment: Art. 9(4)(e) text is on change-management policies; Art. 9(4)(f) text is on patches-and-updates; **no OJ clause prescribes secure-coding standards** (no coding-language-specific linting, no secure-coding-framework adoption). The T4-vs-text mapping for DORA-C19 (Art. 9(4)(f)) routes to D-07.2 in the AEGIS taxonomy but the OJ-literal text is patch-management, not coding practices. SR-DORA-023 audit confirms the DORA-side participation at D-07.2 is partial by inference only (D-07.4 primary). **Layer 2 review recommendation** per CRDA-deep: either (a) revise the AEGIS taxonomy to remove the DORA sole-authority assignment, or (b) identify the OJ clause that supports it. **This is not a CONTRADICTORY or CORRECTED reclassification** — the CRDA verified-classification of CRA↔DORA = SAME — COMPLEMENTARY holds; the Layer 2 review item is on the AEGIS-taxonomy-vs-OJ-text gap. **Documented separately** from the emergent_tensions count because it is a taxonomy-vs-OJ-text participation gap, not a regulatory-tension reclassification.
**(2) CRA outcome-level vs AI Act attack-category — required layered stack for AI-enabled CRA products, no OJ-level consolidation rule:** CRA requires attack-surface limitation (Annex I Part I (2)(j)) + exploitation mitigation (Annex I Part I (2)(k)) as outcomes; AI Act requires defence against 6 AI/ML-specific attack categories (Art. 15(4)–(5)). For AI-enabled CRA products (CRA-regulated product that embeds a high-risk AI system), both regimes apply with distinct evidence templates — the AI Act defence categories do not substitute for CRA's outcome-level obligations, and the CRA outcome-level obligations do not substitute for the AI Act defence categories. **No OJ-level consolidation rule exists** (unlike the CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does not extend to coding practices). The two regimes stack as parallel coding-architecture tracks. **Documented separately** from the emergent_tensions count because it is a layered-stack requirement on the Conditional Y integrated stack, not a CONTRADICTORY/CORRECTED reclassification that requires Phase 1C tension-resolution.
**Substantial scope-disjoint structure on 2 of 3 pairs in baseline:** CRA↔DORA = N (typically) and DORA↔AI_Act = N (typically) are **substantively scope-disjoint in baseline** because distinct actors handle distinct objects at distinct supply-chain levels / lifecycle stages (manufacturer-side product-coding-outcomes vs financial-entity-side process change-management; financial-entity-side process change-management vs AI-system-provider-side AI-system-coding). The `complementary` CRDA classification labels for these pairs are **more taxonomy artifacts than substantive relationships** per the CRDA-deep substantive note. The CRA↔AI_Act pair has **Conditional Y scope overlap** on AI-enabled CRA products — the high-level SO engages only on this Conditional Y integrated stack. **No SCOPE-DISJOINT baseline pairs in the 3×3 matrix are CORRECTED/CONTRADICTORY reclassifications** — they are scope-disjoint facts, not contradictions. The high-level SO does NOT engage on the baseline 2-of-3 N scope-disjoint pairs; it engages only on the Conditional Y integrated stack (AI-enabled CRA product deployed by a DORA financial entity or similar atypical integrated stack).
The high-level SO surfaces the common secure-coding duty (attack-surface limitation + exploitation mitigation + AI-attack-defence + appropriate coding-practice evidence base typically built from industry frameworks since no OJ clause prescribes specific coding standards); the per-reg target object, trigger, anchor, threshold, recipient, and evidence template are documented separately in the three sub-SOs with the substantial scope-disjoint structure preserved verbatim. **0 conditional emergent tensions** in the narrow CONTRADICTORY/CORRECTED sense — the three Layer 2 review items are documented separately as Layer 2 review items, NOT as emergent_tensions count that would require Phase 1C tension-resolution.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-07.2 — with overlapping scope-determiners on the Conditional Y integrated stack — operates a **3-track coding-architecture** with explicit layered hand-offs. The high-level SO (`SO-D-07.2.HL`) describes the common secure-coding duty (attack-surface limitation + exploitation mitigation + AI-attack-defence + appropriate coding-practice evidence base typically built from industry frameworks NIST SSDF + OWASP SAMM + ISO/IEC 27034 since no OJ clause prescribes specific coding standards); the per-reg perspective is preserved in the three sub-SOs (target object, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered 3-track architecture**, with the Conditional Y integrated stack (AI-enabled CRA product) operationalising the inter-reg hand-offs: CRA-side Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation + AI-Act-side Art. 15(4)–(5) AI-attack-defence categories stack vertically on the same integrated product. The high-level SO does NOT collapse the three target objects into a single coding-architecture; the per-reg perspective on target object, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim with the substantial scope-disjoint structure on 2 of 3 baseline pairs. Phase 1C Doc 07 documents the **secure-coding-practices strategy**: (1) a 3-track coding-architecture with explicit target-object hand-offs (CRA Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation → DORA Art. 9(4)(e) change-mgmt six-step + Art. 25 testing modalities → AI Act Art. 15(4)–(5) 6-category AI-attack-defence); (2) the **Layer 2 review item** on the AEGIS-taxonomy DORA sole-authority assignment with no OJ-text anchor — either revise the taxonomy to remove the assignment, or identify the OJ clause that supports it (preserved verbatim from CRDA-deep §D-07.2); (3) the **no OJ-level consolidation rule** for coding practices — unlike the CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9, no OJ clause permits a unified coding-standards baseline across the three regimes; the entity must build the coding-standards baseline from industry frameworks (NIST SSDF, OWASP SAMM, ISO/IEC 27034) and demonstrate compliance against each regulation's outcome (CRA) or process (DORA) or AI-attack-defence (AI Act) requirement independently; (4) the **substantial scope-disjoint structure** on 2 of 3 pairs in baseline (CRA↔DORA = N typically; DORA↔AI_Act = N typically) — the high-level SO engages only on the Conditional Y integrated stack (AI-enabled CRA product deployed by a DORA financial entity or similar atypical integrated stack); for typical integrated stacks the high-level SO does NOT engage; (5) the CRA ↔ AI Act Conditional Y scope overlap on AI-enabled CRA products — the CRA-side Annex I Part I (2)(j) + (2)(k) outcome mandate + AI-Act-side Art. 15(4)–(5) attack-defence categories stack vertically on the same integrated product with no OJ-level consolidation rule; (6) the DORA-side coding dimension is demonstrated through the change-mgmt six-step `tested` + `assessed` legs + Art. 25 testing modalities (source-code reviews where feasible as one of 12 modalities) — NOT through an OJ-mandated secure-coding-standards prescription; (7) the AI-Act-side AI-attack-defence is AI/ML-specific and does NOT map to conventional coding practices (no general coding-standards prescription in AI Act); (8) the Annex VII §2 + §3 CRA-side technical documentation as the evidence pack for the manufacturer-side coding-outcomes architecture; (9) the Art. 17 QMS as the formal carrier of the AI-Act-side attack-defence design/design-control/design-verification controls, with the QMS documentation per Art. 11 + 12(2) Annex IV technical documentation as the evidence pack; (10) the D-07.2 coding-outputs propagating downstream from D-07.1 (Secure-by-Design Principles) by-design decisions + from D-06.1 (Vendor Risk Assessment) supplier-secure-development-procedures three-prong. For proportionality (P2), a 5-FTE manufacturer of a CRA-regulated product with no AI-enabled component may default to CRA Annex I Part I (2)(j) + (2)(k) outcome-level documentation plus the Annex VII §2 design/development documentation record (DORA and AI Act are out of scope unless the manufacturer is also a DORA financial entity or is also a high-risk AI system provider); a CRA manufacturer that is also a high-risk AI system provider on an AI-enabled CRA product must additionally document the AI Act Art. 15(4)–(5) 6-category AI-attack-defence + Art. 17(1)(c) QMS design/design-control/design-verification, with the CRA Annex I Part I (2)(j) + (2)(k) outcome-level documentation supplied and the no OJ-level consolidation rule for coding practices preserved verbatim; a CRA manufacturer that is also a DORA financial entity (atypical integrated stack with all 3 applicable regs on the integrated manufacturer-financial-entity stack) must additionally document the Art. 9(4)(e) change-management six-step + Art. 25 testing modalities — **but the high-level SO does NOT engage on this typical N scope-disjoint integrated stack**; the high-level SO engages only on the Atypical-Conditional-Y integrated stack with the CRA-AI Act vertical stack + DORA on the Atypical-Conditional-Y integrated stack with all 3 applicable regs.

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-07.2 Secure Coding Practices — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.2.md`. See that file for cross-reg verified relationships (3 pairs verified by CRDA-deep as **3 SAME — COMPLEMENTARY — no CORRECTED, no CONTRADICTORY — but with substantial scope-disjoint qualifiers on 2 of 3 pairs in baseline**: CRA↔DORA = N typically, DORA↔AI_Act = N typically; CRA↔AI_Act = Conditional Y only on AI-enabled CRA products), scope overlap matrix, Objective / Considerations content, **P0 disagreement ON PARTICIPATION** (AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2; CRDA-deep finds no OJ-text support — Art. 9(4)(e) is change-management, Art. 9(4)(f) is patches-and-updates; DORA preserved as partial per SR-DORA-023), no OJ-mandated secure-coding-standards prescription (industry frameworks NIST SSDF + OWASP SAMM + ISO/IEC 27034 supply the coding-practices baseline), CRA outcome-level vs AI Act attack-category layered-stack requirement with no OJ-level consolidation rule (unlike CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment, which does NOT extend to coding practices), and aggregation logic. **Scope-title note (P0):** the corpus index title `Secure Coding` is reconciled with the CRDA-deep authoritative `Secure Coding Practices` — this file covers the by-code leg only; the by-design leg is in D-07.1 (Volere subtype integrity) and the by-process leg is in D-07.3 / D-07.4. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
CRA, DORA (partial), AI Act (partial) — 3 of 5 regs. **GDPR and NIS 2 are explicitly out-of-scope** for D-07.2 per OJ-text verification: GDPR Art. 25(1) is process- and outcome-oriented and does not specify secure-coding practices; NIS 2 Art. 21(2)(e) does not mention CI/CD pipeline, secure-coding standards, or specific coding practices. CRDA-deep verified 3 pairs as SAME — COMPLEMENTARY (none required CRDA correction) — but with substantial scope-disjoint qualifiers on 2 of 3 pairs in baseline: CRA↔DORA = N typically (different actors — manufacturer vs financial entity — handle different objects — product coding outcomes vs process change-management); DORA↔AI_Act = N typically (different actors — financial entity vs AI system provider — handle different objects — process change-management vs AI-system coding); CRA↔AI_Act = Conditional Y on AI-enabled CRA products. The three regulators target **distinct target objects** (product-level coding outcomes via Annex I Part I (2)(j)+(k) / entity-level process change-management six-step with implicit coding-dimension inference — no OJ-mandated secure-coding-standards prescription / AI-system-level attack-defence via Art. 15(4)–(5) 6 AI/ML-specific attack categories) at **distinct supply-chain levels / lifecycle stages**, and the **high-level SO does NOT engage on the baseline 2-of-3 N scope-disjoint pairs** — it engages only on the Conditional-Y integrated stack (AI-enabled CRA product deployed by a DORA financial entity or similar atypical integrated stack). **No OJ clause prescribes specific coding standards** — the coding-practices evidence base is typically built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034).
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 7.2
  volere_section: 15
  volere_subtype: immunity
  title: "Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system attack-defence under an appropriate coding-practice evidence base typically built from industry frameworks (Conditional-Y integrated stack only — no HL engagement on baseline 2-of-3 N scope-disjoint pairs)"
  derives_from:
    hso_sub_so: SO-D-07.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.2.md
    objective_ref_section: "### D-07.2.0"
  description: |
    The product shall deliver coding practices that limit attack surfaces, mitigate exploitation, and resist AI-system attacks, under an appropriate coding-practice evidence base typically built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034), as the common secure-coding duty converging across CRA Annex I Part I (2)(j) attack-surface limitation + (2)(k) exploitation-mitigation, DORA Art. 9(4)(e) change-management six-step with implicit coding-dimension inference (partial — no OJ mandate; DORA preserves as partial per SR-DORA-023), and AI Act Art. 15(4)–(5) AI-system attack-defence across 6 AI/ML-specific attack categories, where ≥2 of these scope-determiners have Y or Conditional Y scope overlap on the same party on the same coding event.
  fit_criterion: |
    A documented coding-practices architecture is maintained across the 3-track coding-architecture (CRA product-side Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation outcomes / DORA entity-side change-management six-step with implicit coding-dimension inference through the `tested` and `assessed` legs + Art. 25 testing modalities — partial at D-07.2, no OJ-mandated secure-coding-standards prescription / AI Act AI-system-side Art. 15(4)–(5) AI-attack-defence across 6 AI/ML-specific categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) with explicit target-object hand-offs; the coding-practices evidence base is built from industry frameworks — NIST SSDF (Secure Software Development Framework) for secure-development lifecycle practices, OWASP SAMM (Software Assurance Maturity Model) for software-assurance maturity, ISO/IEC 27034 for application-security controls — since no OJ clause prescribes specific coding standards; each track demonstrates compliance against its own regulation's outcome (CRA) / process (DORA) / AI-attack-defence (AI Act) requirement with distinct evidence templates that cannot be substituted; for AI-enabled CRA products (CRA-regulated product that embeds a high-risk AI system), CRA Annex I Part I (2)(j) + (2)(k) outcome-level obligations + AI Act Art. 15(4)–(5) attack-defence categories stack vertically with **no OJ-level consolidation rule** (unlike CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment, which does NOT extend to coding practices); the high-level SO does NOT engage on the baseline 2-of-3 N scope-disjoint pairs (CRA↔DORA, DORA↔AI_Act) — it engages only on the Conditional Y integrated stack (AI-enabled CRA product deployed by a DORA financial entity or similar atypical integrated stack); for a typical integrated stack (e.g. CRA manufacturer + DORA FE + AI system provider, with separate artefacts), each coding-track stands on its own with the per-tier scope-disjoint structure preserved; verified by coding-practices evidence-base documentation review (NIST SSDF + OWASP SAMM + ISO/IEC 27034 baseline) + per-track evidence-trail audit (CRA Annex I Part I (2)(j)+(k) outcomes / DORA change-mgmt six-step + Art. 25 testing modalities / AI Act Art. 15(4)–(5) AI-attack-defence measures) + AI-enabled CRA product layered-stack hand-off protocol inspection (when Conditional Y integrated stack applies) + scope-disjoint structure preserved on CRA↔DORA + DORA↔AI_Act baseline pairs + MSA / national CA + ESA / AI Office inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.PS-06, PR.PS-02, PR.PS-01, ID.RA-04]
  applicable_if:
    regs: [CRA, DORA, AI_Act]
    scope_overlap: conditional   # HL engages ONLY on Conditional Y integrated stack (AI-enabled CRA product deployed by DORA FE or similar atypical integrated stack); baseline 2-of-3 N scope-disjoint pairs do NOT trigger HL engagement; GDPR + NIS2 explicitly out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    3 of 5 regulations participate at D-07.2 (CRA, DORA **partial**, AI Act **partial**); **GDPR and NIS 2 are explicitly out-of-scope** per OJ-text verification (GDPR Art. 25(1) does not specify secure-coding practices; NIS 2 Art. 21(2)(e) does not mention CI/CD pipeline or coding standards). The three participating regulators anchor the coding-practices duty at distinct target objects with distinct supply-chain levels / lifecycle stages: CRA `limitation of attack surfaces, including attack surfaces of external interfaces` (Annex I Part I (2)(j)) + `reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques` (Annex I Part I (2)(k)) — product-coding-outcome mandate at the manufacturer side; DORA Art. 9(4)(e) change-management six-step — entity-process mandate at the financial-entity side, with implicit coding-dimension inference through `tested` / `assessed` legs + Art. 25 testing modalities (source-code reviews where feasible as one of 12 modalities per SO-DORA-005) — **no OJ-mandated secure-coding-standards prescription** (P0 disagreement ON PARTICIPATION per CRDA-deep; AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY but no OJ clause supports this assignment; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary); AI Act Art. 15(4)–(5) — AI-system attack-defence mandate at the AI-system-provider side with 6 AI/ML-specific attack categories. 3 pairwise cells verified by CRDA-deep as 3 SAME — COMPLEMENTARY (no CORRECTED, no CONTRADICTORY), but with substantial scope-disjoint qualifiers on 2 of 3 pairs in baseline (CRA↔DORA = N typically, DORA↔AI_Act = N typically). The high-level SO does NOT engage on the baseline 2-of-3 N scope-disjoint pairs; it engages only on the Conditional Y integrated stack. The **two Layer 2 review items** are documented separately as structural items — not as CONTRADICTORY/CORRECTED reclassifications: (a) **P0 DORA-taxonomy-disagreement** — AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 but CRDA-deep finds no OJ-text support (no OJ clause prescribes secure-coding standards); (b) **CRA outcome-level vs AI Act attack-category** layered-stack requirement for AI-enabled CRA products with no OJ-level consolidation rule. The coding-practices evidence base is typically built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034) since no OJ clause prescribes specific coding standards. 0 conditional emergent tensions in the narrow CONTRADICTORY/CORRECTED sense. (Copied from the HSO Considerations block of `### D-07.2.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-07.2
title: D-07.2 Secure Coding Practices — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.2 Secure Coding Practices
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-07_Secure-Development/D-07.2.md
status: DRAFT
---
> **Deep analysis:** [D-07.2 Secure Coding Practices](../../DeepAnalysis/D-07_Secure-Development/D-07.2.md)
#### D-07.2 Secure Coding Practices
<!-- participants: CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR is process- and outcome-oriented; it does not specify secure-coding practices. | — |
| NIS2 | (out-of-scope) | T3-vs-text gap (synthesis §8, T3 NIS2-C11): OJ Art. 21(2)(e) does not mention CI/CD pipeline, secure coding standards, or specific coding practices. | — |
| CRA | SO-CRA-046 | Attack-surface limitation (Annex I Part I (2)(j)) + exploitation mitigation (Annex I Part I (2)(k)) at the outcome level. | Product-level outcome mandates (limit attack surface, mitigate exploitation) — not coding-standard mandates. |
| DORA | SO-DORA-013 (partial via Art. 9(4)(e)) | ICT change-management policies cover software changes; secure-coding dimension is implicit. | T4-vs-text gap: T4 maps DORA-C19 (Art. 9(4)(f) patches) to D-07.2 but OJ text is patch-management policies, not coding practices. AEGIS taxonomy §4.1 marks DORA as sole authority for D-07.2 — this pilot finds no OJ-text support for that assignment and flags Layer 2 review. |
| AI_Act | SO-AIACT-009 (partial via Art. 15(4)-(5)) | AI-specific attack defence — 6 attack categories (data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks, model flaws). | AI/ML-focused secure-coding dimension; does not map to conventional secure-coding mandates. |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3 regulations)
<!-- emergent: CRA,DORA,AI_Act -->
- **The taxonomy's "sole authority" assignment for DORA is OJ-text-unsupported**: AEGIS taxonomy §4.1 marks DORA as the sole authority for D-07.2 Secure Coding Practices. The OJ Art. 9(4)(e) text is on change-management; Art. 9(4)(f) is on patches and updates. No OJ clause prescribes coding standards. The taxonomy assignment has no textual anchor in DORA. Recommend Layer 2 review: either (a) revise the taxonomy to remove the DORA sole-authority assignment, or (b) identify the OJ clause that supports it.
- **CRA outcome-level vs. AI Act attack-category**: CRA requires attack-surface reduction and exploitation mitigation as outcomes; AI Act requires defence against 6 specific AI-attack categories. The two regimes do not substitute — a CRA-regulated AI product must discharge both. No OJ-level consolidation rule exists for the AI-coding dimension (unlike the CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9, which does not extend to coding practices).
<!-- /emergent -->
##### SR cross-validation
The 3 applicable regulations map D-07.2 to the NIST CSF 2.0 Subcategory **PR.PS-06** (Secure software development practices integrated) as the convergent anchor. CRA additionally anchors on **PR.PS-02** (Software maintained/replaced/removed commensurate with risk) for the attack-surface/exploitation-mitigation lifecycle; AI Act additionally anchors on **ID.RA-01** (Vulnerabilities identified, validated, recorded) for the AI-attack-defence identification loop. The CSF mapping reflects that no regulation prescribes coding standards — the Subcategory mapping is at the SDLC-discipline layer, not the coding-standard layer.
##### Downstream implication
The taxonomy gap (DORA sole-authority with no OJ-text anchor) is a Layer 2 review item. Phase 1 entities should not treat DORA as a coding-standard authority absent OJ-text evidence. The three regimes do not produce a coordinated coding-standards baseline — the entity must build the coding-standards baseline from industry frameworks (NIST SSDF, OWASP SAMM, ISO 27034) and demonstrate compliance against each regulation's outcome or process requirement.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-07.2
title: D-07.2 Secure Coding Practices — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.2 Secure Coding Practices
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-07_Secure-Development/D-07.2.md
status: DRAFT
---
> **Domain analysis:** [D-07.2 Secure Coding Practices](../../DomainAnalysis/D-07_Secure-Development/D-07.2.md)
#### D-07.2 Secure Coding Practices
<!-- participants: CRA, DORA, AI_Act -->
**Participants (from CRDA):** CRA, DORA, AI_Act
**Sole-authority note (CRDA flag):** AEGIS taxonomy §4.1 marks DORA as sole authority for D-07.2 Secure Coding Practices. The OJ Art. 9(4)(f) text is on `patches and updates` (patch-management policy) — not coding standards. Per SR-DORA-007 v0.2 audit, this pilot finds no OJ-text support for the DORA sole-authority assignment and recommends Layer 2 review (see P0 disagreement report).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
