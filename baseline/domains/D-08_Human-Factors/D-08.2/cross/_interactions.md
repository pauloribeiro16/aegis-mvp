# D-08.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-08.2 Role-Specific Competence](../../DomainAnalysis/D-08_Human-Factors/D-08.2.md)
#### D-08.2 Role-Specific Competence
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority / partial-coverage notes:** CRA's role-specific dimension is integrator-facing (Annex II §8(f)) — B2B audience, not workforce. The asymmetry (workforce training for NIS 2 / DORA / GDPR vs. product-integrator training for CRA) is unique to D-08.2.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-08.2 Role-Specific Competence
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md`](../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.2.md)
> (10 pairs in the 5×5 matrix — **5 participating regulations
> are GDPR, NIS 2, CRA, DORA, AI Act — all 5 participate** as noted
> by `DomainAnalysis/D-08_Human-Factors/D-08.2.md` line 27:
> "Participants: GDPR, NIS2, CRA, DORA, AI_Act" and lines 30–35:
> "CRA's role-specific dimension is integrator-facing (Annex II §8(f))
> — B2B audience, not workforce. The asymmetry (workforce training
> for NIS 2 / DORA / GDPR vs. product-integrator training for CRA)
> is unique to D-08.2").
>
> **CRDA pair-coverage note (per CRDA-deep §D-08.2 line 73):** CRDA
> lists 5 verified pairs only (GDPR↔NIS2, GDPR↔AI_Act, NIS2↔DORA,
> NIS2↔AI_Act, DORA↔AI_Act); the 5 CRDA-omitted pairs
> (GDPR↔CRA, GDPR↔DORA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are
> documented with Executor-recommended classifications. The 10
> pairs in the 5×5 matrix are preserved in this HSO.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-08.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-025 (cross-ref at D-08.2) | DPO monitors assignment of responsibilities, awareness-raising, training of staff involved in processing (Art. 39(1)(b)). | Role-specific training for staff with data-subject-facing or access-management responsibilities. |
| NIS2 | SG-NIS2-019 | Employees offered similar training on a regular basis to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2). | Entity-side, encouraged-not-mandatory (Member State obligation); employee training for risk-identification and assessment capability. |
| CRA | SG-CRA-048 (partial via SR-CRA-108 Annex II §8(f)) | Integrator-facing information delivery for compliance with Annex I + Annex VII. | Limited role-specific dimension aimed at integrators (B2B), not workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence. |
| DORA | SG-DORA-015 (partial via Art. 13(6) `commensurate to the remit`) | Compulsory training with complexity commensurate to the remit of staff functions. T4-vs-text gap: T4 reads `role-specific training` but OJ text says `commensurate to the remit`. | Entity-level role-specific training; OJ-literal locus preserved. |
| AI_Act | SG-AIACT-008 + SG-AIACT-011 | Built-in human-oversight capability (Art. 14) + deployer assignment of competent human overseers (Art. 26(2)). | AI-system-specific competence: human overseers must have competence, training, authority. |

## Validated relationships (from CRDA-deep §D-08.2)

#### Validated relationships (from CRDA-deep §D-08.2)
Of 10 pairs in the 5×5 matrix, **5 verified by CRDA as SAME (no CORRECTED, no CONTRADICTORY)** — the five regulators look at role-specific competence from five distinct regulatory perspectives that are layered rather than contradictory. **5 pairs are documented as Executor-recommended classifications** (`NOT CLASSIFIED (CRDA omitted this pair for D-08.2)` per CRDA-deep §D-08.2) — the Executor recommends SCOPE-DISJOINT or COMPLEMENTARY on the omitted pairs, with the SCOPE-DISJOINT classifications reflecting substantively different audiences (workforce vs integrator-B2B vs AI-overseer role) and the COMPLEMENTARY classification (GDPR↔DORA) reflecting the DORA programme as carrier + GDPR role-specific module pattern. **No CONTRADICTORY reclassifications** and **no CORRECTED reclassifications** on the role-specific-competence duty itself. The **5 SAME pairs** (verified) are:
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR role-specific is DPO-catalysed (Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations`) and tied to processing role; NIS 2 Art. 20(2) sentence 2 employee training is encouraged (not mandatory at OJ level) and tied to risk-identification capability (`gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`). Different content (data-protection vs risk-identification) and different governance hooks (DPO-direct vs Member-State-encouraged). Scope-disjoint test: **Conditional (Y when the controller-NSIE adopts the encouragement; N otherwise)**. The Art. 20(2) sentence 2 binding force is on the Member State rather than directly on the entity (Orchestrator-recommended treatment per SR-NIS2-030 ambiguity_notes) — the entity-side SR applies to entities that adopt the encouragement.
- **GDPR ↔ AI_Act** — DIFFERENT-PERSPECTIVE (SAME): GDPR role-specific targets processing staff with data-subject-facing responsibilities (DPO-catalysed); AI Act targets human overseers of high-risk AI systems with the 5-element competence set (Art. 14(4)(a)–(e) + Art. 26(2) `competence, training AND authority` 3-way AND + `necessary support` 4th element). Different role, different content. Scope-disjoint test: **Conditional (Y when the same natural person is both a data-processing staff member and an AI human overseer)**. No reclassification required; where the same person holds both roles, the AI Act layer is the additional competence dimension.
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose role-specific training obligations (Art. 20(2) sentence 2 NIS 2 `similar training on a regular basis` + Art. 13(6) DORA `commensurate to the remit of their functions`). DORA's OJ-literal `commensurate to the remit` is the operative anchor; NIS 2's `similar training on a regular basis` is the parallel anchor. For DORA financial entities, the DORA programme is the dominant authority (DORA's `compulsory` qualifier is more prescriptive than NIS 2's `encouraged`). Scope-disjoint test: **Y (when the DORA financial entity is also an NSIE applying role-specific training)**. No reclassification required.
- **NIS2 ↔ AI_Act** — COMPLEMENTARY (SAME): NIS 2 employee training covers general risk-identification (Art. 20(2) sentence 2 `identify risks and assess cybersecurity risk-management practices`); AI Act adds the AI-specific 5-element competence for high-risk AI systems (Art. 14(4)(a)–(e)). For NSIEs deploying high-risk AI, both apply — the NIS 2 programme covers the baseline and the AI Act layer adds AI-specific competency. Scope-disjoint test: **Y (when the NSIE deploys high-risk AI and assigns human oversight)**. No reclassification required.
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME): DORA's `commensurate to the remit` covers all staff functions including AI-related ones (Art. 13(6)); AI Act adds the explicit 5-element + competence-training-authority-support set for high-risk AI (Art. 14(4) + Art. 26(2)). For DORA financial entities deploying high-risk AI, both apply and stack. Scope-disjoint test: **Y (when the DORA financial entity deploys high-risk AI)**. No reclassification required.
The **5 CRDA-omitted pairs (Executor-recommended classifications)** are:
- **GDPR ↔ CRA** — SCOPE-DISJOINT (recommended): The two regimes address entirely different audiences and objects — GDPR workforce training (DPO-catalysed, Art. 39(1)(b) — internal staff involved in processing) vs CRA Annex II §8(f) integrator-facing information (manufacturer-shipped, B2B integrators). The Annex II §8(f) integrator audience is a B2B external party, not an internal workforce member. Scope-disjoint test: **N** — different audiences (workforce vs integrator-B2B), different objects (data-protection role training vs Annex I compliance documentation), different triggers. CRDA's omission should be corrected by adding a "scope-disjoint" classification.
- **GDPR ↔ DORA** — COMPLEMENTARY (recommended): DORA's `commensurate to the remit` clause subsumes GDPR's role-specific layer when the DORA financial entity is a controller. The two regimes stack with the DORA programme as the carrier and the GDPR role-specific module as a sub-component. Scope-disjoint test: **Y (when the DORA financial entity is a controller with role-specific staff)**. CRDA's omission should be corrected by adding a "complementary" classification.
- **NIS2 ↔ CRA** — SCOPE-DISJOINT (recommended): The two regimes address entirely different audiences and objects — NIS 2 workforce training (Art. 20(2) sentence 2 — Member-State-encouraged) vs CRA Annex II §8(f) integrator-facing information (manufacturer-shipped, B2B integrators). Scope-disjoint test: **N** — different audiences, different objects. CRDA's omission should be corrected.
- **CRA ↔ DORA** — SCOPE-DISJOINT (recommended): The two regimes address entirely different audiences and objects — CRA Annex II §8(f) integrator-facing information (B2B) vs DORA Art. 13(6) internal staff training (`commensurate to the remit`). Scope-disjoint test: **N** — different audiences (integrator-B2B vs internal staff), different objects. CRDA's omission should be corrected.
- **CRA ↔ AI_Act** — SCOPE-DISJOINT (recommended): The two regimes address different audiences (CRA Annex II §8(f) integrator-B2B vs AI Act human-overseer role within the deployer organization) and different objects (Annex I compliance documentation vs AI-overseer competence Art. 14(4) + Art. 26(2)). Scope-disjoint test: **N** — different audiences, different objects. CRDA's omission should be corrected.
The role-specific-competence architecture is **legitimately diverse with audience-fragmented structure** — each regulator targets a **distinct target role** (DPO-catalysed processing staff / Member-State-encouraged employee risk-identification / manufacturer integrator-facing B2B / financial-entity function-specific depth / AI Act human-overseer 5-element) at a **distinct trigger** (DPO activity per Art. 39(1)(b) / Member State encouragement per Art. 20(2) sentence 2 / manufacturer ships integrator information per Annex II §8(f) / financial entity establishes training schemes with `commensurate to the remit` per Art. 13(6) / provider design per Art. 14 + deployer assignment per Art. 26(2)) with a **distinct obligation anchor** (GDPR Art. 39(1)(b) DPO `awareness-raising and training of staff involved in processing operations`; NIS 2 Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis` — Member-State encouraged, not OJ-direct; CRA Annex II §8(f) `information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` — B2B integrator — partial coverage; DORA Art. 13(6) `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` — function-specific calibration; AI Act Art. 14(4) 5-element closed-list (a)–(e) + Art. 26(2) `competence, training AND authority AND support` 4-element AND — provider design + deployer assignment). The high-level SO surfaces the **common role-specific-competence duty** (function-specific depth + audience-routing + competence-criteria-anchored training + governance hooks); the per-reg target role, trigger, anchor, threshold, evidence template, recipient are preserved verbatim in the five sub-SOs.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA | AI_Act |
|---|---|---|---|---|---|
| **GDPR** | — | Y (Cond) (controller-NSIE with both data-protection role-specific training + risk-identification training; entity adopts Member-State encouragement) | N (workforce vs integrator-B2B audiences; different objects; different triggers) | Y (DORA financial entity = controller with role-specific staff; DORA programme as carrier + GDPR role-specific module — recommended) | Y (Cond) (deployer-controller with same natural person as both data-processing staff and AI human overseer — Art. 14(4) + Art. 39(1)(b) stack) |
| **NIS2** | Y (Cond) (same; reciprocal — controller-NSIE adopts encouragement) | — | N (workforce vs integrator-B2B audiences; different objects) | Y (DORA financial entity = NSIE applying role-specific training; DORA-dominant) | Y (NSIE deploys high-risk AI and assigns human oversight; NIS 2 risk-identification baseline + AI Act 5-element competence stack) |
| **CRA** | N (same; reciprocal — substantively scope-disjoint) | N (same; reciprocal — substantively scope-disjoint) | — | N (integrator-B2B vs internal staff audiences; different objects) | N (integrator-B2B vs AI-overseer role within deployer organization; different objects) |
| **DORA** | Y (same; reciprocal — DORA programme as carrier + GDPR role-specific module — recommended) | Y (same; reciprocal — DORA-dominant for financial entities) | N (same; reciprocal — substantively scope-disjoint) | — | Y (DORA financial entity deploys high-risk AI; DORA `commensurate to the remit` carrier + AI Act 5-element sub-component) |
| **AI_Act** | Y (Cond) (same; reciprocal — same natural person as both data-processing staff and AI human overseer) | Y (same; reciprocal) | N (same; reciprocal — substantively scope-disjoint) | Y (same; reciprocal — DORA financial entity deploys high-risk AI) | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Y (Cond)** = scope overlap conditional on a specific event (e.g. controller-NSIE adopting Member-State encouragement; same natural person as both data-processing staff and AI human overseer). **N** = substantively scope-disjoint — different audiences and different objects; no consolidation rule exists. CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Y (Cond) on the controller-NSIE adopting encouragement; GDPR↔CRA = N substantively scope-disjoint (recommended); GDPR↔DORA = Y on DORA financial entity = controller (recommended); GDPR↔AI_Act = Y (Cond) on the same natural person as both data-processing staff and AI human overseer; NIS2↔CRA = N substantively scope-disjoint (recommended); NIS2↔DORA = Y on DORA financial entity = NSIE; NIS2↔AI_Act = Y on NSIE deploys high-risk AI; CRA↔DORA = N substantively scope-disjoint (recommended); CRA↔AI_Act = N substantively scope-disjoint (recommended); DORA↔AI_Act = Y on DORA financial entity deploys high-risk AI. The 5 CRDA-omitted pairs (GDPR↔CRA, GDPR↔DORA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) carry Executor-recommended classifications preserved in this HSO.

## Cross-recipient map

#### Cross-recipient map
D-08.2 generates a layered recipient set on the **role-specific-competence evidence trail**. The recipient set is at the **role-specific-training-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 5(2) accountability evidence (Art. 39(1)(b) DPO-catalysed role-specific training records — cross to D-09.2 via the Art. 35 DPIA necessary-assessment chain); **NIS 2's management body + competent authority** on the Art. 21(1) + 20(2) sentence 2 documented policies on risk-identification training + Art. 20(1) management-body approval+oversight+liability; **CRA's market surveillance authority (MSA)** on the Annex II §8(f) integrator-facing information + Art. 13(18) support-period accessibility (10-year information accessibility — **integrator-B2B audience only**, not workforce); **DORA's competent authority (national financial supervisory authority)** on the Art. 13(6) `commensurate to the remit` function-specific training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline; **AI Act's provider / deployer / MSA / AI Office** on the Art. 14(4) 5-element human-oversight capability (provider design — SR-AIACT-013) + Art. 26(2) `competence, training AND authority AND support` 4-element AND (deployer assignment — SR-AIACT-020) + Annex IV technical documentation + post-market monitoring reports under Art. 72. These are distinct regulatory channels on the same role-specific-competence evidence but they do not generate a notification cascade of D-08.2 itself — they are **compliance-evidence channels on the layered role-specific-competence architecture**. **D-08.1 (General Security Awareness) is the upstream awareness substrate where D-08.2's role-specific depth adds function-specific calibration**; **D-08.3 (Management Board Training) is the management-body literacy prerequisite for governance duties** (NIS 2 Art. 20(2) sentence 1 mandatory + DORA Art. 5(4) management-body training — partial AI Act interplay for senior-executive AI literacy); **D-07.1 (Secure-by-Design Principles) is where the AI Act Art. 14(1) oversight-design-by-design feeds the human-oversight capability** (SR-AIACT-012 anchors the workforce-role-understanding substrate that the `appropriate human-machine interface tools` qualifier requires); **D-04.3 (Regulatory Notification) is the notification cascade where role-specific training evidence flows to supervisory authorities on incident reporting**; **D-09.4 (Records of Processing) is the documentation-channel cross-link for GDPR Art. 30 staff-awareness records and CRA Annex II §8(f) integrator-facing information**.
---

## HSO considerations (from D-08.2.0 — High-level SecurityObjective)

**Considerations.**
- 5 of 5 regulations participate (GDPR, NIS 2, CRA, DORA, AI Act — all 5 participate).
- GDPR Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations` — DPO-catalysed role-specific training for processing staff with data-subject-facing or access-management responsibilities, on the controller's processing-staff audience.
- NIS 2 Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices` — Member-State-encouraged employee training on risk-identification capability (binding force on the Member State rather than directly on the entity per SR-NIS2-030).
- CRA Annex II §8(f) `where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` — integrator-facing B2B information for Annex I compliance by the integrator — **partial coverage** per AEGIS taxonomy §4.1.
- DORA Art. 13(6) `commensurate to the remit of their functions` — financial-entity function-specific-depth training, on the financial-entity workforce with function-specific depth audience.
- AI Act Art. 14(4)(a)–(e) 5-element closed-list (properly understand; remain aware of automation bias; correctly interpret; decide not to use / disregard / override / reverse; intervene on operation or interrupt) + Art. 26(2) `competence, training AND authority AND support` 4-element AND — AI Act human-overseer 5-element + 4-element competence set, on the high-risk-AI human-overseer audience within the deployer organization (provider-side Art. 14 design + deployer-side Art. 26(2) assignment).
- 10 pairwise cells in 5×5 matrix: 5 verified by CRDA as SAME (3 SAME — COMPLEMENTARY: GDPR↔NIS2, NIS2↔DORA, NIS2↔AI_Act; 1 SAME — EQUAL: NIS2↔DORA on workforce awareness at entity level; 1 SAME — DIFFERENT-PERSPECTIVE: GDPR↔AI_Act on same natural person as both data-processing staff and AI human overseer); 5 CRDA-omitted pairs with Executor-recommended classifications (4 SCOPE-DISJOINT on different-audiences: GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act — workforce / encouraged-employee / financial-entity-workforce / AI-human-overseer vs B2B integrator; 1 COMPLEMENTARY: GDPR↔DORA — DORA programme as carrier + GDPR role-specific module on DORA financial entity = controller).
- The high-level SO engages on the Y-pairs integrated stack when ≥2 regs are applicable: GDPR↔NIS2 (Conditional Y on controller-NSIE adopting Member-State encouragement); GDPR↔DORA (Y on DORA financial entity = controller with role-specific staff — DORA programme as carrier + GDPR role-specific module); GDPR↔AI_Act (Conditional Y on same natural person as both data-processing staff and AI human overseer); NIS2↔DORA (Y on DORA financial entity = NSIE applying role-specific training — DORA-dominant for financial entities); NIS2↔AI_Act (Y on NSIE deploys high-risk AI and assigns human oversight — NIS 2 risk-identification baseline + AI Act 5-element competence stack); DORA↔AI_Act (Y on DORA financial entity deploys high-risk AI — DORA `commensurate to the remit` carrier + AI Act 5-element sub-component).
- The 4 CRA-involving pairs operate on substantively scope-disjoint audiences (internal workforce / Member-State-encouraged employee / financial-entity workforce / AI human overseer vs B2B integrator) — the parallel tracks coexist with no consolidation rule; the high-level SO does NOT collapse the audience boundaries.
- For a 5-FTE SaaS startup with GDPR + CRA applicability, the two parallel training-programme tracks must be maintained separately (substantively scope-disjoint audiences — GDPR workforce role-specific training is independent of the CRA Annex II §8(f) integrator-facing information).
- The per-reg target role, trigger, anchor, threshold, evidence template, recipient are preserved verbatim in the five sub-SOs.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-08.2 over a distinct **target role** of the role-specific-competence architecture; the target role, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the role-specific-competence duty.
| Axis (reg) | Target role | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | DPO-catalysed processing staff with data-subject-facing or access-management responsibilities (role-specific layer of the Art. 39(1)(b) duty) | DPO-catalysed role-specific training (Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations`) | no quantitative cadence (DPO-discretionary under Recital 56); `awareness-raising` implies ongoing reinforcement not one-off induction; role-specific depth on data-subject-facing and access-management responsibilities | supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) role-specific training records (cross to D-09.2 via Art. 35 DPIA necessary-assessment chain) | Art. 39(1)(a) + Art. 39(1)(b) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) + Art. 30(4) + Art. 47(2)(n) BCR |
| **NIS2** | Member-State-encouraged employee training on risk-identification and assessment capability (entity-side, encouraged-not-mandatory at OJ level) | Member State encouragement per Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis` — binding force on Member State, not on entity directly (Orchestrator-recommended treatment per SR-NIS2-030) | `on a regular basis` entity-discretionary under Recital 56; the OJ is silent on training-frequency; the entity-side SR activates when the entity adopts the encouragement | management body (Art. 20(1) approve+oversee+liability) + competent authority — Art. 20(2) sentence 2 employee-training records + Art. 20(1) management-body approval | Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices` + Art. 20(2) sentence 1 purpose clause cross + Art. 20(1) management-body approval + Recital 56 proportionality |
| **CRA** | integrator (B2B external party) receiving information necessary for compliance with Annex I + Annex VII (partial coverage per AEGIS taxonomy §4.1) | manufacturer ships integrator-facing information per Annex II §8(f) `where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` | `intended for integration` per the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4) — not as third-party speculation; where intended purpose does not include integration, §8(f) is not engaged; support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)) | integrator (B2B external party) + market surveillance authority (MSA) — Annex II §8(f) integrator information + Art. 13(18) support-period accessibility | Art. 13(1) + Annex II §8(f) + Art. 13(18) support-period accessibility + Recital 25 (Annex II scope) |
| **DORA** | financial-entity staff with function-specific complexity `commensurate to the remit of their functions` (workforce with function-specific depth) | financial entity establishes training schemes (Art. 13(6) `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions`) — continuous obligation | `compulsory` (Art. 13(6) — completion-mandatory per SR-DORA-025 ambiguity reading) + `commensurate to the remit of their functions` (function-specific calibration per the OJ literal — T4-vs-text gap: T4 reads `role-specific training` while the OJ Art. 13(6) uses only `commensurate to the remit of their functions`) — qualitative + `level of complexity` qualitative; no quantitative cadence | competent authority (national financial supervisory authority) + management body — Art. 13(6) `commensurate to the remit` training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 13(6) `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` + Art. 5(2) management-body responsibility + EBA Guidelines on ICT and security risk management |
| **AI_Act** | high-risk AI system human overseers (provider-side Art. 14 design + deployer-side Art. 26(2) assignment) — AI-system-specific competence | provider design (Art. 14(1) `High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons`) + deployer assignment (Art. 26(2) `Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support`) — provider-design-by-design + deployer-assignment-on-deployment twin trigger | `as appropriate and proportionate` (Art. 14(4) qualitative) — 5 cumulative abilities must be enabled (Art. 14(4)(a)–(e)); Art. 26(2) 4-element AND: `competence, training AND authority AND support`; no quantitative threshold | provider (QMS design-control documented) + deployer (assignment documented) + market surveillance authority (MSA) (Annex IV technical documentation + Art. 17(1) QMS documented in `systematic and orderly manner`) + AI Office (for GPAI on systemic-risk tracking) | Art. 14(1) + Art. 14(2)–(5) — provider design + Art. 26(2) deployer assignment — competence, training, authority, support 4-element AND; Art. 17(1)(c) QMS design/design-control/design-verification cross to D-07.1; Recital 78 GDPR preservation |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
(See the validated-relationships table above for the 5×5 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-08.2.HL`) engages on a given party **if and only if ≥2 applicable
regulations target overlapping target roles on the same party** (e.g.
a financial entity that is also a NIS 2 essential entity AND processes
personal data AND manufactures CRA-classified products AND deploys
high-risk AI — a vertically-integrated financial-manufacturer-
controller-AI-deployer with full GDPR + NIS 2 + CRA + DORA + AI Act
applicability on the same role-specific-competence substrate). For an
integrated controller-NSIE adopting Member-State encouragement that
does not manufacture CRA-classified products and does not deploy high-
risk AI, only the GDPR and NIS 2 sub-SOs activate; the high-level SO
engages on the Conditional GDPR↔NIS2 COMPLEMENTARY pair. For a DORA
financial entity that is a controller processing personal data with
role-specific staff, only the GDPR and DORA sub-SOs activate; the
high-level SO engages on the COMPLEMENTARY GDPR↔DORA pair (DORA
programme as carrier + GDPR role-specific module). For a DORA
financial entity deploying high-risk AI processing personal data, only
the DORA and AI Act sub-SOs activate; the high-level SO engages on
the COMPLEMENTARY DORA↔AI_Act pair (DORA `commensurate to the remit`
carrier + AI Act 5-element sub-component). For a 5-FTE SaaS startup
with GDPR + CRA applicability but no NIS 2 / DORA / AI Act
applicability, only the GDPR and CRA sub-SOs activate; the **4
substantively scope-disjoint CRA-involving pairs** mean the two
parallel training-programme tracks must be maintained separately —
the GDPR workforce role-specific training is independent of the CRA
Annex II §8(f) integrator-facing information. For a NIS 2 essential
entity that is not a financial entity and does not manufacture CRA-
classified products (NIS 2 + GDPR only or NIS 2 only with non-CRA-
classified products), only the applicable sub-SOs activate and the
high-level SO engages on the Conditional GDPR↔NIS2 COMPLEMENTARY
pair. **The five target roles are layered, not collapsed**: DPO-
catalysed processing-staff role-specific (GDPR, controller-driven DPO-
catalysed); Member-State-encouraged employee risk-identification
(NIS 2, entity-driven Member-State encouragement); manufacturer
integrator-facing B2B (CRA, manufacturer-driven integrator information
— partial coverage); financial-entity function-specific-depth (DORA,
financial-entity-driven `commensurate to the remit` depth); AI Act
human-overseer 5-element + 4-element (AI Act, provider-design-by-design
+ deployer-assignment-on-deployment). The high-level SO surfaces the
common role-specific-competence duty but does **NOT** collapse the
per-reg target role, trigger, anchor, threshold, recipient, or
evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **5 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA, AI Act —
  **all 5 participate**, no out-of-scope): GDPR (Art. 39(1)(b) DPO-
  catalysed role-specific training as controller obligation — role-
  specific layer of the Art. 39(1)(b) duty); NIS 2 (Art. 20(2)
  sentence 2 employee training as Member-State-encouraged obligation
  — entity-side SR activates when the entity adopts the encouragement);
  CRA (Annex II §8(f) integrator-facing information as manufacturer
  obligation — **partial coverage** per AEGIS taxonomy §4.1, B2B
  audience); DORA (Art. 13(6) `commensurate to the remit` function-
  specific depth as financial-entity obligation — T4-vs-text gap on
  the `role-specific` vs `commensurate to the remit` reading); AI Act
  (Art. 14(4) 5-element + Art. 26(2) 4-element AND competence set as
  provider+deployer obligation — AI-system-specific competence).
- **10 pairwise cells in the 5×5 matrix, verified by CRDA-deep as a
  mixed pattern** (5 verified + 5 Executor-recommended for CRDA-omitted
  pairs): GDPR↔NIS2 (SAME — COMPLEMENTARY — DPO data-protection vs
  risk-identification capability stack at controller-NSIE adopting
  encouragement — Conditional Y); GDPR↔CRA (SCOPE-DISJOINT —
  recommended — workforce vs integrator-B2B audiences; different
  objects); GDPR↔DORA (COMPLEMENTARY — recommended — DORA programme
  as carrier + GDPR role-specific module on DORA financial entity =
  controller); GDPR↔AI_Act (SAME — DIFFERENT-PERSPECTIVE — DPO-
  catalysed processing-staff role-specific vs AI Act human-overseer
  5-element competence set — Conditional Y on same natural person as
  both data-processing staff and AI human overseer); NIS2↔CRA (SCOPE-
  DISJOINT — recommended — workforce vs integrator-B2B audiences);
  NIS2↔DORA (SAME — EQUAL — both regulations impose role-specific
  training; DORA-dominant for financial entities); NIS2↔AI_Act (SAME
  — COMPLEMENTARY — NIS 2 risk-identification baseline + AI Act
  AI-specific 5-element competence on NSIE deploying high-risk AI);
  CRA↔DORA (SCOPE-DISJOINT — recommended — integrator-B2B vs internal
  staff audiences); CRA↔AI_Act (SCOPE-DISJOINT — recommended —
  integrator-B2B vs AI-overseer role within deployer organization);
  DORA↔AI_Act (SAME — COMPLEMENTARY — DORA `commensurate to the remit`
  carrier + AI Act 5-element sub-component on DORA financial entity
  deploying high-risk AI).
- The five participating regulations impose **distinct role-specific-
  competence duties** at **distinct target roles** with **distinct
  triggers** and **distinct anchors**: GDPR controller-side DPO-
  catalysed processing-staff (Art. 39(1)(b) `awareness-raising and
  training of staff involved in processing operations` — role-specific
  layer); NIS 2 Member-State-encouraged employee risk-identification
  (Art. 20(2) sentence 2 `gain sufficient knowledge and skills to
  identify risks and assess cybersecurity risk-management practices` —
  encouraged-not-mandatory at OJ level); CRA manufacturer-side
  integrator-facing B2B (Annex II §8(f) `information necessary for
  the integrator to comply with the essential cybersecurity
  requirements` — partial coverage); DORA financial-entity-side
  function-specific depth (Art. 13(6) `commensurate to the remit of
  their functions` — function-specific calibration); AI Act provider-
  design + deployer-assignment twin-trigger human-overseer (Art.
  14(4)(a)–(e) 5-element + Art. 26(2) 4-element AND `competence,
  training AND authority AND support` — AI-system-specific
  competence). The thresholds align qualitatively (no regulation
  imposes quantitative cadence — all are entity-discretionary under
  Recital 56 proportionality or equivalent). The five anchors align
  in their direction-of-travel (function-specific depth calibrated to
  role) but the target roles, triggers, evidentiary templates,
  recipients diverge.
- The high-level SO describes the **COMMON OBJECTIVE** (function-
  specific depth + audience-routing + competence-criteria-anchored
  training + governance hooks); the **per-regulation perspective**
  (target role, trigger, anchor, threshold, recipient, evidence
  template) is preserved verbatim in the five sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the role-specific-competence
  duty itself**, because no pair was verified as CONTRADICTORY or
  CORRECTED (5 verified pairs are SAME — 3 SAME — COMPLEMENTARY +
  1 SAME — EQUAL + 1 SAME — DIFFERENT-PERSPECTIVE). Phase 1C Doc 07
  does not need to resolve a role-specific-competence contradiction
  because none exist by construction. The **4 substantively scope-
  disjoint pairs** (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are
  SCOPE-DISJOINT (recommended, NOT CLASSIFIED by CRDA) on the
  different-audiences dimension (workforce / Member-State-encouraged
  employee / financial-entity workforce / AI human overseer vs
  B2B integrator) — no reclassification is required, but the parallel
  tracks coexist on different audiences with no consolidation rule.
  The **CRA partial coverage** is a structural Layer 2 review item —
  preserved as a partial-participation fact and surfaced as a SCOPE-
  DISJOINT classification on the 4 CRA-involving pairs. The **AI Act
  5-element + 4-element AND** is the AI-Act-specific competence
  criterion — distinct from the DORA `commensurate to the remit`
  function-specific depth — and the two stack with the DORA programme
  as carrier. The 5-layer role-specific-competence architecture (GDPR
  DPO-catalysed processing-staff / NIS 2 Member-State-encouraged
  employee risk-identification / CRA manufacturer integrator-facing
  B2B / DORA financial-entity function-specific depth / AI Act
  human-overseer 5-element + 4-element) is itself the layered
  reconciliation that supersedes any single-regulator reading.
- **Scope caveat (CRITICAL — CRA partial coverage + asymmetry)** —
  derived from CRDA-deep verified classifications: CRA's role-
  specific dimension at D-08.2 is integrator-facing (Annex II §8(f)),
  B2B audience, not workforce. The asymmetry — workforce training
  (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is
  unique to D-08.2 (per DomainAnalysis §D-08.2 line 107). For an
  integrated manufacturer that is also a controller, the CRA-side
  Annex II §8(f) integrator information is independent of the GDPR-
  side Art. 39(1)(b) DPO-catalysed workforce training (substantively
  scope-disjoint audiences — workforce vs B2B integrator — per CRDA-
  deep §D-08.2 GDPR↔CRA verified relationship).
- **Scope caveat (CRITICAL — NIS 2 Member-State-encouraged)** —
  derived from CRDA-deep verified classifications: NIS 2 Art. 20(2)
  sentence 2 binding force is on the Member State rather than directly
  on the entity (Orchestrator-recommended treatment per SR-NIS2-030).
  The entity-side SR applies to entities that adopt the encouragement.
  For an integrated controller-NSIE that adopts the encouragement, the
  GDPR Art. 39(1)(b) DPO-catalysed role-specific training and the
  NIS 2 Art. 20(2) sentence 2 Member-State-encouraged employee
  training stack on the same workforce (Conditional Y on the controller-
  NSIE adopting encouragement).
- **Scope caveat (CRITICAL — DORA `commensurate to the remit`
  function-specific depth vs GDPR role-specific)** — derived from
  CRDA-deep verified classifications: DORA Art. 13(6) `commensurate
  to the remit of their functions` subsumes GDPR's role-specific
  dimension when the DORA financial entity is a controller. The two
  regimes stack with the DORA programme as the carrier and the GDPR
  role-specific module as a sub-component. For an integrated financial-
  entity-controller with role-specific staff, the DORA programme is
  the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific
  training is the module.
- **Scope caveat (CRITICAL — DORA `commensurate to the remit` vs AI
  Act 5-element + 4-element AND)** — derived from CRDA-deep verified
  classifications: DORA's `commensurate to the remit` covers all staff
  functions including AI-related ones (Art. 13(6)); AI Act adds the
  explicit 5-element (Art. 14(4)(a)–(e)) + 4-element AND (Art. 26(2)
  `competence, training AND authority AND support`) competence set for
  high-risk AI. For DORA financial entities deploying high-risk AI,
  both apply and stack with the DORA `commensurate to the remit`
  carrier + AI Act 5-element + 4-element AND sub-component.
- **Scope caveat (CRITICAL — AI Act Art. 14(4) 5-element closed-list
  AND Art. 26(2) 4-element AND)** — derived from CRDA-deep verified
  classifications: Art. 14(4)(a)–(e) is a 5-element closed-list AND
  (all five abilities must be enabled); Art. 26(2) is a 4-element AND
  (`competence, training AND authority AND support` — all four
  required). The two compound: provider-side Art. 14(4) design
  obligation + deployer-side Art. 26(2) assignment obligation. For an
  AI-enabled entity that is both provider and deployer (or that
  procures AI from a third-party provider and operates as deployer),
  both Art. 14(4) (provider) and Art. 26(2) (deployer) apply; the
  two obligations stack with the provider's design-by-design substrate
  + the deployer's assignment-on-deployment substrate.
- **Scope caveat (CRITICAL — GDPR ↔ AI_Act DIFFERENT-PERSPECTIVE on
  same natural person)** — derived from CRDA-deep verified
  classifications: GDPR role-specific targets processing staff with
  data-subject-facing responsibilities (DPO-catalysed); AI Act targets
  human overseers of high-risk AI systems with the 5-element
  competence set. Different role, different content. Where the same
  natural person holds both roles (data-processing staff + AI human
  overseer), the AI Act layer is the additional competence dimension
  (Conditional Y).
- **Scope caveat (CRITICAL — `state of the art` anchor is duplicated
  but uncoordinated)** — derived from CRDA-deep verified
  classifications: GDPR Art. 39(1)(b) `DPO discretion` (no OJ anchor);
  NIS 2 Art. 20(2) sentence 2 `on a regular basis` (entity-discretionary
  under Recital 56); CRA Annex II §8(f) `intended for integration`
  (intended-purpose scope); DORA Art. 13(6) `commensurate to the
  remit` (function-specific calibration); AI Act Art. 14(4) `as
  appropriate and proportionate` (qualitative) + 5-element closed
  list. Each regulation interprets the threshold anchor independently.
  An entity implementing all 5 must reconcile the five threshold
  anchors through documented decision records (per-regulation
  threshold + integrated-stack reconciliation).
---

## Emergent tensions (from CRDA-deep §D-08.2)

#### Emergent tensions (from CRDA-deep §D-08.2)
**0 conditional emergent tensions** on the role-specific-competence duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 5 verified pairs (GDPR↔NIS2, GDPR↔AI_Act, NIS2↔DORA, NIS2↔AI_Act, DORA↔AI_Act) are all SAME (3 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 1 SAME — DIFFERENT-PERSPECTIVE). The 5 CRDA-omitted pairs (GDPR↔CRA, GDPR↔DORA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) carry Executor-recommended classifications (4 SCOPE-DISJOINT on different-audiences + 1 COMPLEMENTARY on DORA programme as carrier) — no CONTRADICTORY or CORRECTED reclassifications. **The 4 SCOPE-DISJOINT pairs** (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are CRDA-recommended SCOPE-DISJOINT (NOT CLASSIFIED by CRDA) on the different-audiences dimension (workforce / Member-State-encouraged employee / financial-entity workforce / AI human overseer vs B2B integrator) — the substantive scope-disjointness on the different-audiences dimension is preserved without requiring reclassification, but the parallel tracks coexist. **No CONTRADICTORY pairs** on the role-specific-competence duty itself. The **target-role divergence** (DPO-catalysed processing staff / Member-State-encouraged employee risk-identification / manufacturer integrator-facing B2B / financial-entity function-specific depth / AI Act human-overseer 5-element + 4-element) is the **legitimately diverse dimension**: each regulator targets a distinct target role at a distinct trigger (DPO activity / Member State encouragement / manufacturer ships integrator information / financial entity establishes training schemes / provider design + deployer assignment), and the operational convergence is on a **5-layer role-specific-competence architecture** with explicit audience-routing — the parallel tracks coexist on substantively scope-disjoint audiences (workforce / encouraged-employee / financial-entity-workforce / AI-human-overseer vs B2B-integrator) with no consolidation rule on the CRA-involving pairs.
The **CRA partial coverage + asymmetry** is the structurally significant divergence: CRA's role-specific dimension at D-08.2 is integrator-facing (Annex II §8(f)), B2B audience, not workforce — the asymmetry — workforce training (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is unique to D-08.2 (per DomainAnalysis §D-08.2 line 107). The 4 CRA-involving pairs are SCOPE-DISJOINT (Executor-recommended) on the different-audiences dimension.
The **NIS 2 Member-State-encouraged vs DORA compulsory-modules EQUAL classification** is the structurally significant EQUAL pair: both regulations impose role-specific training obligations (Art. 20(2) sentence 2 NIS 2 `similar training on a regular basis` + Art. 13(6) DORA `commensurate to the remit of their functions`). DORA's OJ-literal `commensurate to the remit` is the operative anchor; NIS 2's `similar training on a regular basis` is the parallel anchor. For DORA financial entities, the DORA programme is the dominant authority (DORA's `compulsory` qualifier is more prescriptive than NIS 2's `encouraged`). The EQUAL classification preserves the OJ literal parallel between the two regimes on the role-specific-training dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry.
The **DORA `commensurate to the remit` carrier + AI Act 5-element + 4-element AND sub-component COMPLEMENTARY pair** is the structurally significant COMPLEMENTARY pair for the financial-services + high-risk-AI subset: DORA's `commensurate to the remit` covers all staff functions including AI-related ones; AI Act adds the explicit 5-element (Art. 14(4)(a)–(e)) + 4-element AND (Art. 26(2) `competence, training AND authority AND support`) competence set for high-risk AI. For DORA financial entities deploying high-risk AI, both apply and stack with the DORA programme as carrier and the AI Act layer as the additional sub-component.
The **GDPR ↔ DORA COMPLEMENTARY pair on DORA programme as carrier** is the structurally significant COMPLEMENTARY pair (Executor-recommended for the CRDA-omitted pair) for the financial-services + controller subset: DORA's `commensurate to the remit` subsumes GDPR's role-specific layer when the DORA financial entity is a controller. The two regimes stack with the DORA programme as the carrier and the GDPR role-specific module as a sub-component.
The high-level SO surfaces the common role-specific-competence duty; the per-reg target role, trigger, anchor, threshold, recipient, and evidence template are documented separately in the five sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 5-layer role-specific-competence architecture (GDPR DPO-catalysed processing-staff / NIS 2 Member-State-encouraged employee risk-identification / CRA manufacturer integrator-facing B2B / DORA financial-entity function-specific depth / AI Act human-overseer 5-element + 4-element) with parallel tracks on substantively scope-disjoint audiences (workforce / encouraged-employee / financial-entity-workforce / AI-human-overseer vs B2B-integrator) is itself the layered reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-08.2 — with overlapping target-role scope-determiners on the same party — operates a **5-layer role-specific-competence architecture** with explicit audience-routing on substantively scope-disjoint audiences (workforce / encouraged-employee / financial-entity-workforce / AI-human-overseer vs B2B-integrator). The high-level SO (`SG-D-08.2.HL`) describes the common role-specific-competence duty (function-specific depth + audience-routing + competence-criteria-anchored training + governance hooks); the per-reg perspective is preserved in the five sub-SOs (target role, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 5-layer role-specific-competence architecture (GDPR Art. 39(1)(b) DPO-catalysed processing-staff → NIS 2 Art. 20(2) sentence 2 Member-State-encouraged employee risk-identification → CRA Annex II §8(f) manufacturer integrator-facing B2B — partial coverage — → DORA Art. 13(6) `commensurate to the remit` financial-entity function-specific depth → AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND) operationalising the inter-reg hand-offs on the Y-pairs integrated stack. The high-level SO does NOT collapse the five target roles into a single role-specific-competence architecture; the per-reg perspective on target role, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **role-specific-competence strategy**: (1) a 5-layer role-specific-competence architecture with explicit target-role hand-offs (GDPR Art. 39(1)(b) DPO-catalysed processing-staff → NIS 2 Art. 20(2) sentence 2 Member-State-encouraged employee risk-identification → CRA Annex II §8(f) manufacturer integrator-facing B2B — partial coverage — → DORA Art. 13(6) `commensurate to the remit` financial-entity function-specific depth → AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND); (2) the CRA partial coverage + asymmetry as a structural Layer 2 review item (Annex II §8(f) integrator-facing B2B, not workforce — AEGIS taxonomy §4.1 partial-coverage marker); (3) the NIS 2 ↔ DORA EQUAL classification on role-specific training at entity level — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs adopting Member-State encouragement; (4) the DORA `commensurate to the remit` carrier + AI Act 5-element + 4-element AND sub-component COMPLEMENTARY pair for the financial-entity-deploying-high-risk-AI stack; (5) the GDPR ↔ DORA COMPLEMENTARY pair (Executor-recommended) on DORA programme as carrier + GDPR role-specific module for the financial-entity-controller stack; (6) the 4 substantively scope-disjoint CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) preserved as SCOPE-DISJOINT (Executor-recommended, NOT CLASSIFIED by CRDA) on different audiences (workforce / encouraged-employee / financial-entity-workforce / AI-human-overseer vs B2B-integrator) — parallel tracks coexist with no consolidation rule; (7) the AI Act 5-element closed-list + 4-element AND compound architecture (Art. 14(4) provider-design + Art. 26(2) deployer-assignment) operating as the AI-system-specific competence criterion distinct from the DORA `commensurate to the remit` function-specific depth; (8) the 5 participating regulations at D-08.2 (GDPR, NIS 2, CRA, DORA, AI Act — all 5 participate) with 10 verified pairs in the 5×5 matrix (5 CRDA-verified + 5 Executor-recommended for CRDA-omitted pairs); (9) the `state of the art` anchor is duplicated but uncoordinated across the 5 regulations (GDPR Art. 39(1)(b) DPO discretion / NIS 2 Art. 20(2) sentence 2 entity-discretionary / CRA Annex II §8(f) intended-purpose scope / DORA Art. 13(6) `commensurate to the remit` function-specific calibration / AI Act Art. 14(4) `as appropriate and proportionate` qualitative + 5-element closed list) — reconciliation through documented decision records (per-regulation threshold + integrated-stack reconciliation).

## Part 1 §3 — context

### 3. Security Requirements
## 8.2 Role-Specific Competence — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md`. See that file for cross-reg verified relationships (10 pairs in 5×5 matrix: 5 SAME verified — 3 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 1 SAME — DIFFERENT-PERSPECTIVE; 5 CRDA-omitted pairs with Executor-recommended classifications — 4 SCOPE-DISJOINT on different-audiences + 1 COMPLEMENTARY on DORA programme as carrier), scope overlap matrix, Objective/Considerations content, target-role divergence (DPO-catalysed processing-staff / Member-State-encouraged employee / manufacturer integrator-facing B2B / financial-entity function-specific depth / AI Act human-overseer 5-element + 4-element AND), aggregation logic, **AI Act full participation at 8.2** (Art. 4 + Art. 14 + Art. 26(2) — distinct from 8.1 absence), and **CRA partial coverage + asymmetry** (Annex II §8(f) is integrator-facing B2B — not workforce — AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA (partial), DORA, AI Act (5 of 5 regs — all 5 participate at 8.2 per AEGIS taxonomy §4.1 + HSO provenance block). CRDA-deep verified 5 SAME pairs (3 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 1 SAME — DIFFERENT-PERSPECTIVE — no CORRECTED, no CONTRADICTORY). The five regulators target **distinct target roles** at **distinct triggers** (DPO-catalysed workforce per Art. 39(1)(b) / Member-State-encouraged employee per Art. 20(2) sentence 2 / manufacturer integrator-B2B per Annex II §8(f) / financial-entity function-specific depth per Art. 13(6) `commensurate to the remit` / AI Act provider-design-by-design + deployer-assignment-on-deployment per Art. 14 + Art. 26(2)), and the high-level SO surfaces the **common role-specific-competence duty** (function-specific depth + audience-routing + competence-criteria-anchored training + governance hooks) while preserving the per-reg target role, trigger, anchor, threshold, evidence template, recipient.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 8.2
  volere_section: 15
  volere_subtype: immunity
  title: "Role-specific competence established through function-specific depth, audience-routing, competence-criteria-anchored training, and governance hooks"
  derives_from:
    hso_sub_so: SO-8.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.2.md
    objective_ref_section: "### 8.2.0"
  description: |
    The product shall establish role-specific competence on the five distinct target roles — DPO-catalysed processing staff (GDPR), Member-State-encouraged employees (NIS 2), manufacturer integrator-B2B (CRA — partial), financial-entity staff with `commensurate to the remit` depth (DORA), and high-risk AI human overseers (AI Act) — through function-specific depth, audience-routing across the five target roles, competence-criteria-anchored training (the AI Act 5-element + 4-element AND is the only OJ-quantitative competence criterion), and governance hooks (DPO approval; Member-State encouragement; manufacturer-shipped Annex II §8(f) information; management-body approval; provider QMS design-control + deployer assignment RACI), as the common role-specific-competence duty converging across GDPR Art. 39(1)(b) DPO `awareness-raising and training of staff involved in processing operations`, NIS 2 Art. 20(2) sentence 2 `offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices` — Member-State encouraged, CRA Annex II §8(f) `where the product is intended for integration into other products, the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` — partial B2B integrator, DORA Art. 13(6) `commensurate to the remit of their functions`, and AI Act Art. 14(4) 5-element closed-list (a)–(e) + Art. 26(2) 4-element AND `competence, training AND authority AND support` — provider-design + deployer-assignment twin-trigger, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A 5-layer role-specific-competence architecture is maintained with five distinct audience routes operating in parallel (DPO-catalysed processing-staff role-specific training per Art. 39(1)(b) when GDPR in scope; Member-State-encouraged employee risk-identification training per Art. 20(2) sentence 2 when NIS 2 in scope and the controller-NSIE adopts the encouragement; manufacturer Annex II §8(f) integrator-facing information when CRA in scope and the product is `intended for integration`; financial-entity `commensurate to the remit` function-specific depth when DORA in scope; AI Act Art. 14(4) 5-element + Art. 26(2) 4-element AND human-overseer competence when AI Act in scope); each route documents target role, trigger, anchor, competence criterion, evidence template, and recipient separately; PR.AT-02 role-understanding dimension is the cross-cutting anchor for all five routes; for an integrated financial-entity-controller with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair); for a DORA financial entity deploying high-risk AI, the DORA programme is the carrier and the AI Act 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship); for an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of GDPR role-specific training (per CRDA-deep §8.2 GDPR↔AI_Act verified DIFFERENT-PERSPECTIVE pair on the Conditional Y operator — same natural person); for NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship); for DORA financial entities also classified as NSIEs, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` exceeds NIS 2 `encouraged`); the CRA-side Annex II §8(f) integrator information operates on a substantively scope-disjoint audience (B2B external integrators) from the workforce programmes; verified by per-role competence-criterion audit + per-audience evidence-pack review + role-specific training records inspection + management-body approval + provider QMS design-control + deployer assignment RACI documentation + DPA / competent authority / MSA / AI Office / national CA + ESA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: [8.1]   # the 8.1 awareness substrate is the upstream governance input
  nist_csf: [PR.AT-02, PR.AT-01, GV.SC-03, GV.RR-02, GV.RR-04]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping target roles on the same party; the 5 Y-pairs (GDPR↔NIS2 Conditional, GDPR↔DORA recommended, GDPR↔AI_Act Conditional, NIS2↔DORA, NIS2↔AI_Act, DORA↔AI_Act) cover all 5 participating regulators; the 4 N-pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are substantively scope-disjoint on different audiences and do not engage the HL
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The five participating regulations impose the same substantive role-specific-competence duty but each targets a **distinct target role** at a **distinct trigger** with a **distinct obligation anchor and competence criterion**: GDPR Art. 39(1)(b) DPO-catalysed processing-staff role-specific (DPO-driven; role-specific layer of Art. 39(1)(b); PR.AT-01 + PR.AT-02; Art. 5(2) accountability burden shifts demonstration duty to the controller — `awareness-raising` and `training` split per SR-GDPR-042 ambiguity_notes into (1) general awareness training annually + (2) role-specific training for personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities, quarterly or event-triggered); NIS 2 Art. 20(2) sentence 2 Member-State-encouraged employee risk-identification (binding force on the Member State rather than directly on the entity per SR-NIS2-030 — entity-side SR applies to entities that adopt the encouragement; `similar training on a regular basis` entity-discretionary under Recital 56; PR.AT-01 + PR.AT-02); CRA Annex II §8(f) manufacturer integrator-B2B facing information (`information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII` — **partial coverage** per AEGIS taxonomy §4.1; PR.AT-02 + GV.SC-03; support period ≥ 5 years under Art. 13(8) + 10-year Annex II information accessibility under Art. 13(18); the chosen reading of `intended for integration` is the manufacturer's documented intended purpose — Article 3(23) D23 + Annex II §4 — not third-party speculation); DORA Art. 13(6) `commensurate to the remit of their functions` financial-entity function-specific depth (`compulsory` completion-mandatory; function-specific calibration per the OJ literal formulation; T4-vs-text gap: T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit` — Executor keeps the OJ-literal locus per SR-DORA-025; PR.AT-01 + PR.AT-02); AI Act Art. 14(4) 5-element closed-list (a)–(e) AND-coordinated `properly understand; remain aware of automation bias; correctly interpret; decide not to use / disregard / override / reverse; intervene on the operation or interrupt` + Art. 26(2) 4-element AND `competence, training AND authority AND support` (PR.AT-02 + PR.AT-01 + GV.RR-02 + GV.RR-04; provider-design-by-design + deployer-assignment-on-deployment twin-trigger). The thresholds align qualitatively (no regulation imposes quantitative cadence — all are entity-discretionary under Recital 56 proportionality or equivalent). The five anchors align in their direction-of-travel (function-specific depth calibrated to role) but the target roles, triggers, evidentiary templates, recipients diverge. The high-level SO surfaces the **COMMON OBJECTIVE** (function-specific depth + audience-routing + competence-criteria-anchored training + governance hooks); the **per-regulation perspective** (target role, trigger, anchor, threshold, recipient, evidence template) is preserved verbatim in the five sub-SOs. **CRA partial coverage** is preserved — the CRA-side role-specific output at this layer is integrator-B2B (Annex II §8(f)), not workforce; AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence; the 4 CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are substantively scope-disjoint (workforce / encouraged-employee / financial-entity workforce / AI human overseer vs B2B integrator) — the parallel tracks coexist on different audiences with no consolidation rule. **NIS 2 Member-State-encouraged layer** is preserved — Art. 20(2) sentence 2 binding force is on the Member State rather than directly on the entity; the entity-side SR applies to entities that adopt the encouragement. The **NIS2↔DORA EQUAL classification** preserves the OJ literal parallel on the role-specific-training dimension; DORA's `compulsory` qualifier exceeds NIS 2's `encouraged` — for DORA financial entities DORA is the dominant authority. CRDA-deep verified 0 conditional emergent tensions on the role-specific-competence duty itself. **The 4 SCOPE-DISJOINT pairs** (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act) are substantively scope-disjoint (different audiences) — the parallel tracks coexist with no consolidation rule; the high-level SO does NOT collapse the audience boundaries. The **5-layer role-specific-competence architecture** with explicit audience-routing is itself the layered reconciliation that supersedes any single-regulator reading. (Copied from the HSO Considerations block of `### 8.2.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-08.2
title: D-08.2 Role-Specific Competence — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.2 Role-Specific Competence
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-08_Human-Factors/D-08.2.md
status: DRAFT
---
> **Deep analysis:** [D-08.2 Role-Specific Competence](../../DeepAnalysis/D-08_Human-Factors/D-08.2.md)
#### D-08.2 Role-Specific Competence
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-025 (cross-ref at D-08.2) | DPO monitors assignment of responsibilities, awareness-raising, training of staff involved in processing (Art. 39(1)(b)). | Role-specific training for staff with data-subject-facing or access-management responsibilities. |
| NIS2 | SG-NIS2-019 | Employees offered similar training on a regular basis to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2). | Entity-side, encouraged-not-mandatory (Member State obligation); employee training for risk-identification and assessment capability. |
| CRA | SG-CRA-048 (partial via SR-CRA-108 Annex II §8(f)) | Integrator-facing information delivery for compliance with Annex I + Annex VII. | Limited role-specific dimension aimed at integrators (B2B), not workforce. AEGIS taxonomy §4.1 marks NIS 2 / DORA as the authorities for full role-specific workforce competence. |
| DORA | SG-DORA-015 (partial via Art. 13(6) `commensurate to the remit`) | Compulsory training with complexity commensurate to the remit of staff functions. T4-vs-text gap: T4 reads `role-specific training` but OJ text says `commensurate to the remit`. | Entity-level role-specific training; OJ-literal locus preserved. |
| AI_Act | SG-AIACT-008 + SG-AIACT-011 | Built-in human-oversight capability (Art. 14) + deployer assignment of competent human overseers (Art. 26(2)). | AI-system-specific competence: human overseers must have competence, training, authority. |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (5 regulations)
<!-- emergent: GDPR,NIS2,CRA,DORA,AI_Act -->
- **The five regulations impose role-specific competence on five different audiences**: GDPR DPO-driven processing staff; NIS 2 employees (encouraged); CRA integrators (B2B); DORA staff with `commensurate to the remit`; AI Act high-risk AI human overseers. The audiences overlap in practice (a single person may be both DORA-trained staff and AI-Act overseer), but the regulation-specific content (data-protection vs. hygiene vs. AI-oversight) does not substitute. The "commensurate to the remit" anchor in DORA is the broadest and absorbs the others in principle, but the OJ literal text in DORA is silent on AI competence.
- **CRA's role-specific dimension is integrator-facing, not workforce-facing**: This is the only sub-domain where CRA addresses a B2B audience (Annex II §8(f) integrator information). The asymmetry — workforce training (NIS 2 / DORA / GDPR) vs. product-integrator training (CRA) — is unique to D-08.2. Phase 1 entities must distinguish these two training streams.
<!-- /emergent -->
##### SR cross-validation
All 5 regulations map D-08.2 to the NIST CSF 2.0 Subcategories **PR.AT-02** (All members of the workforce understand their roles and responsibilities) and **PR.AT-01** (All users informed and trained on cybersecurity topics) as the convergent pair. AI Act additionally anchors on **GV.RR-02** (Roles, responsibilities, authorities, accountabilities established) for the 5-element oversight capability; DORA additionally anchors on **GV.RR-02** for the `commensurate to the remit` mapping.
##### Downstream implication
Phase 1 entities must implement audience-routing role-specific training. A DORA financial entity deploying high-risk AI processing personal data must satisfy five role-specific obligations in parallel. The training-records documentation should be audience-tagged for audit traceability.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-08.2
title: D-08.2 Role-Specific Competence — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.2 Role-Specific Competence
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-08_Human-Factors/D-08.2.md
status: DRAFT
---
> **Domain analysis:** [D-08.2 Role-Specific Competence](../../DomainAnalysis/D-08_Human-Factors/D-08.2.md)
#### D-08.2 Role-Specific Competence
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority / partial-coverage notes:** CRA's role-specific dimension is integrator-facing (Annex II §8(f)) — B2B audience, not workforce. The asymmetry (workforce training for NIS 2 / DORA / GDPR vs. product-integrator training for CRA) is unique to D-08.2.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)