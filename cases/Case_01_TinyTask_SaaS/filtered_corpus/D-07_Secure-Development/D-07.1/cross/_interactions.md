<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-07.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-07.1 Secure-by-Design Principles](../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.1.md)
#### D-07.1 Secure-by-Design Principles
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority / partial-coverage notes:** DORA is "partial" coverage — the OJ Art. 9(4)(b) text addresses network/infrastructure management structure, not a dedicated by-design mandate. Secure-by-design is operationalised through DORA's change-management and testing-programme architecture (Art. 9(4)(e), Art. 24). This is reflected in the SR-DORA-004 SR mapping (Art. 7(2) + Art. 8(2)) and SR-DORA-006 (Art. 9(4)(b)).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-07.1 Secure-by-Design Principles
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md`](../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.1.md)
> (10 pairs verified against OJ text — **all 5 participating regulations
> are GDPR, NIS 2, CRA, DORA, AI Act** as noted by `DomainAnalysis/D-07_Secure-Development/D-07.1.md`
> line 27: "Participants (from CRDA): GDPR, NIS2, CRA, DORA, AI_Act").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-07.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-024 | Personal-data processing implements data-protection principles (data minimisation) in an effective manner at means-determination and processing time, integrating necessary safeguards (pseudonymisation, encryption, by-default limits) at state-of-the-art level (Art. 25(1)+(2)). | Privacy-by-design as controller obligation; minimisation/pseudonymisation/encryption as canonical by-design techniques; qualitative proportionality anchored in state-of-the-art + cost + nature/scope/context/purposes/risks. |
| NIS2 | SO-NIS2-017 | Security integrated into acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure, across the system lifecycle (Art. 21(2)(e)). | Entity-level lifecycle discipline; three coordinated phases (acquisition, development, maintenance); `appropriate and proportionate` chapeau + state-of-the-art floor + cost factor (Art. 21(1)); vulnerability handling+disclosure leg is one of three coordinated legs. |
| CRA | SO-CRA-045 | A product with digital elements is designed, developed, and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment propagated across the planning, design, development, production, delivery, and maintenance phases (Art. 13(1)+(2)). | Product-level by-design; essential-requirement conformance with health-and-safety of users as a cross-cutting objective; risk-assessment propagation across 6 lifecycle phases per Art. 13(2); Annex VII §3 risk-assessment record. |
| DORA | SO-DORA-004 (partial) | Sound network and infrastructure management structure using appropriate techniques, methods and protocols + patch and update policies (Art. 9(4)(b)+(f)) — **secure-by-design is implicit, not an OJ-mandate standalone**; operationalised through Art. 9(4)(e) change-management six-step (SR-DORA-023). | Financial-entity operational resilience; no dedicated by-design clause in OJ; the security-in-design dimension is operationalised through change-management (Art. 9(4)(e)) and the testing programme (Art. 24); SR-DORA-004 routes Art. 9(4)(b) and Art. 9(4)(f) into D-07.1 partial coverage. |
| AI_Act | SO-AIACT-009 + SO-AIACT-010 | High-risk AI systems achieve appropriate level of accuracy, robustness, and cybersecurity with lifecycle consistency (Art. 15(1) + Art. 15(4)–(5)) + a QMS with 13 enumerated aspects including design/design control/design verification (Art. 17(1)+(1)(c)). | AI-system-specific design discipline; QMS as formal carrier of design controls; lifecycle-consistency clause as qualitative cross-cutting requirement; SR-AIACT-014 (Art. 15(1)) + SR-AIACT-018 (Art. 17(1)(c)). |

## Validated relationships (from CRDA-deep §D-07.1)

#### Validated relationships (from CRDA-deep §D-07.1)
Of 10 pairs, **10 verified as SAME — COMPLEMENTARY (all CRDA initial classifications held after OJ-text analysis): no CORRECTED, no SCOPE-DISJOINT in baseline, no CONTRADICTORY**. The five regulations look at secure-by-design from five distinct regulatory perspectives and are layered rather than contradictory:
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR Art. 25(1) addresses *what* must be designed in (data-protection properties via pseudonymisation and minimisation); NIS 2 Art. 21(2)(e) addresses *that* secure lifecycle discipline applies across acquisition/development/maintenance. The two regimes stack at the same controller-NSIE entity, with the GDPR by-design outputs (pseudonymised-by-default pipelines) realised through the NIS 2 acquisition gate (supplier SDLC assessment) and development gate (in-house secure-by-design decisions per SR-NIS2-027). The OJ literal text does not contradict; the joint addressee discharges both obligations with distinct evidence trails.
- **GDPR ↔ CRA** — COMPLEMENTARY (SAME): GDPR Art. 25(1) addresses *what* data-protection properties must be designed in; CRA Art. 13(1)/(2) addresses *that* the design discipline applies to a product with digital elements across three coordinated verbs (designed, developed, produced) with risk-assessment propagation across 6 phases. For a CRA-regulated product that processes personal data, both regimes apply: the manufacturer's CRA design discipline discharges the engineering substrate, and the controller's GDPR Art. 25(1) discharges the personal-data overlay. The two converge on "design as a regulatory event" but address different design-output objects (data-protection properties vs. product cybersecurity).
- **GDPR ↔ DORA** — COMPLEMENTARY (SAME): DORA's Art. 9(4)(b) is not a dedicated by-design mandate — secure-by-design is operationalised through change management (Art. 9(4)(e)) and testing programme (Art. 24). The OJ literal text does not contain a dedicated by-design anchor; the SR-DORA-004 mapping to D-07.1 is partial. For a DORA financial entity that is a controller processing personal data, GDPR Art. 25(1) provides the data-protection by-design overlay while DORA's change-management six-step provides the engineering discipline. The two stack with distinct evidence trails (documented Art. 25(1) assessment on the controller side; documented Art. 6(1) ICT risk-management framework + Art. 9(4)(e) change-management + Art. 24 testing programme on the financial entity side).
- **GDPR ↔ AI_Act** — COMPLEMENTARY (SAME): GDPR Art. 25(1) addresses data-protection by-design; AI Act Art. 15(1) + Art. 17(1)(c) addresses high-risk AI system design (accuracy/robustness/cybersecurity) and the QMS design-control sub-process. AI-Act-Recital 78 explicitly preserves the GDPR. The two obligations stack — a high-risk AI system processing personal data discharges both with distinct design outputs (privacy property vs. AI-system property).
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 Art. 21(2)(e) governs the entity's procurement and internal development of NIS (the user side); CRA Art. 13(1)/(2) governs the manufacturer's design of products (the maker side). The two regimes meet at the supply-chain boundary — NIS 2 Art. 21(2)(d) supplier obligations reference CRA-conformant products via SR-NIS2-020/024. No contradiction; full coverage requires both (entity-level supplier due diligence stacks with product-level by-design at the supplier-customer boundary).
- **NIS2 ↔ DORA** — COMPLEMENTARY (SAME): NIS 2 mandates lifecycle security as a continuous obligation; DORA mandates the change-management six-step (recorded/tested/assessed/approved/implemented/verified) per Art. 9(4)(e) that operationalises the maintenance phase. NIS 2 financial-entity coverage is light in this domain (financial entities under DORA are NSIEs partially, but DORA's dedicated obligations dominate). The two regimes meet at the maintenance phase: NIS 2 Art. 21(2)(e) maintenance-phase security requirements are operationalised through DORA Art. 9(4)(e) six-step process.
- **NIS2 ↔ AI_Act** — COMPLEMENTARY (SAME): NIS 2 Art. 21(2)(e) development-time obligations apply to NIS that embed AI; AI Act Art. 15(1) + Art. 17(1)(c) design obligations apply to high-risk AI systems regardless of NIS status. The regimes stack — NIS 2 procurement gate (SR-NIS2-026) and AI Act QMS (SR-AIACT-017) both apply to the same entity, with the AI Act design verification record supplementing the NIS 2 supplier-assessment evidence.
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA governs the products DORA entities procure and deploy; DORA's secure-by-design absence (no dedicated by-design mandate in OJ) is filled by the upstream CRA obligation. A DORA entity satisfies its design-procurement baseline by selecting CRA-conformant products and recording the conformance in its supplier-risk register per SR-DORA-006 (network/infrastructure) and SR-DORA-023 (change-management).
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME): For an AI-enabled product (CRA-regulated product that embeds a high-risk AI system), both regimes apply. CRA Art. 13(4) sentence 2 explicitly permits a "unified risk assessment" under AI Act Art. 9 to substitute for the CRA risk assessment when both apply — see SR-CRA-066 ambiguity_notes. The AI Act QMS and CRA Annex I conformity stack with the explicit cross-regulation consolidation rule for risk assessment.
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME): DORA financial entities deploying high-risk AI must satisfy both. DORA's change-management six-step (Art. 9(4)(e)) is the operational gate; AI Act QMS design controls (Art. 17(1)(c)) is the governance gate. The two do not overlap substantively; they stack (operational gate + governance gate).
The secure-by-design architecture is **legitimately diverse** — each regulator targets a **distinct target object** (data-protection-properties / NIS-lifecycle security / product-cybersecurity via Annex I Part I / ICT-infrastructure-management + change-mgmt / AI-system-accuracy-robustness-cybersecurity + QMS) at a **distinct trigger** (controller means-determination / NSIE NIS acquisition+development+maintenance / manufacturer places product on market / financial entity establishes ICT infrastructure / provider places high-risk AI system on market) with a **distinct obligation anchor** (GDPR Art. 25(1)+(2) `designed to implement data-protection principles` + state-of-the-art + 4-factor qualitative proportionality; NIS 2 Art. 21(2)(e) `security in acquisition, development and maintenance` + Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor; CRA Art. 13(1)+(2) `designed, developed and produced` per Annex I Part I + 6-phase risk-assessment propagation per Art. 13(2) + Art. 13(4) sentence 2 AI-Act-substitution; DORA Art. 9(4)(b) network/infrastructure-management + Art. 9(4)(e) change-management six-step + Art. 24 testing programme + Art. 9(4)(f) patch policies — **no dedicated by-design mandate**, by-design is implicit; AI Act Art. 15(1) accuracy/robustness/cybersecurity with lifecycle consistency + Art. 15(4)–(5) AI-attack-defence + Art. 17(1) QMS with 13 enumerated aspects including Art. 17(1)(c) design/design control/design verification + Recital 78 GDPR preservation). The high-level SO surfaces the **common secure-by-design duty** (security integrated into the lifecycle via documented by-design decisions + risk-assessment propagation + proportionate safeguards + lifecycle consistency); the per-regulation perspective is preserved verbatim in the five sub-SOs (target object, trigger, anchor, threshold, evidence template, recipient).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Y (integrated manufacturer-controller-deployer — CRA product processing personal data; manufacturer-side CRA by-design + controller-side GDPR by-design stack vertically)  |
|  **CRA**  |  Y (same; reciprocal — integrated manufacturer-controller stack)  |  —  |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Y; GDPR↔CRA = Y; GDPR↔DORA = Y on financial-entity-controller stack; GDPR↔AI_Act = Y on provider/deployer-controller-processing-personal-data-via-AI; NIS2↔CRA = Y on entity-deployer-+-CRA-manufacturer integrated stack; NIS2↔DORA = Y on DORA-financial-entity-+-NSIE combined stack; NIS2↔AI_Act = Y on NIS-embedding-high-risk-AI; CRA↔DORA = Y on DORA-entity-+-CRA-product-procurer; CRA↔AI_Act = Y on AI-enabled-CRA-product; DORA↔AI_Act = Y on DORA-financial-entity-deploying-high-risk-AI. All 10 pairs are Y in baseline — no SCOPE-DISJOINT in baseline, no CONTRADICTORY reclassifications.

## Cross-recipient map

#### Cross-recipient map
D-07.1 generates a layered recipient set on the **secure-by-design evidence trail** but does **not generate a notification cascade of D-07.1 itself** (the by-design decision is the upstream architectural input to the design-develop-deploy lifecycle). The recipient set is at the **design-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 5(2) accountability evidence (Art. 25(1) documented necessity assessment, often via DPIA per Art. 35 — cross to D-09.2); **NIS 2's management body + competent authority** on the Art. 21(1) + 21(2)(e) documented risk-analysis policies and the Art. 20(1) management-body approval+oversight+liability for the lifecycle-security measures; **CRA's market surveillance authority (MSA)** on the Annex VII §3 risk-assessment record + Annex VII §2 design/development documentation + Annex I Part I (2) sub-point evidence; **DORA's competent authority (national financial supervisory authority)** on the Art. 6(1) ICT risk-management framework + Art. 9(4)(e) change-management six-step + Art. 24 testing programme (the DORA side does not generate a dedicated by-design receipt — the by-design compliance is documented through the change-mgmt + testing outputs); **AI Act's provider / MSA / AI Office** on the QMS documented design-control procedures (Art. 17(1)(c) — design/design control/design verification) + Annex IV technical documentation + post-market monitoring reports under Art. 72. These are distinct regulatory channels on the same secure-by-design evidence but they do not generate a notification cascade of D-07.1 itself — they are **compliance-evidence channels on the layered by-design architecture**. **D-07.2 (Secure Coding Practices) and D-07.3 (CI/CD Pipeline Security) are the operational downstream artefacts where D-07.1's by-design decision becomes a code-level instruction; D-07.4 (Change Management) is where the DORA-side by-design operationalisation manifests via the change-management six-step; D-04.3 (Regulatory Notification) is where a downstream design-flaw incident manifests as a notification to MSAs and CSIRTs.** D-07.1 is the **upstream architectural decision** that the downstream artefacts must implement.
---

## HSO considerations (from D-07.1.0 — High-level SecurityObjective)

**Considerations.**
- All five participating regulations (GDPR, NIS 2, CRA, DORA, AI Act) impose a secure-by-design duty at distinct target objects with distinct anchors: GDPR Art. 25(1) privacy-by-design with state-of-the-art + 4-factor qualitative proportionality + Art. 25(2) by-default limits on the controller's means-determination; NIS 2 Art. 21(2)(e) entity-level lifecycle discipline across acquisition, development, and maintenance with `appropriate and proportionate` chapeau + state-of-the-art floor; CRA Art. 13(1) + Art. 13(2) product-level by-design with risk-assessment propagation across 6 lifecycle phases per Annex I Part I; DORA Art. 9(4)(b) + Art. 9(4)(f) network-and-infrastructure management + patch policies — secure-by-design is implicit, not an OJ-mandate standalone, operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme; AI Act Art. 15(1) + Art. 17(1)(c) high-risk AI system accuracy, robustness, and cybersecurity with lifecycle consistency + QMS design/design-control/design-verification.
- Each regulator anchors by-design with a distinct qualitative threshold and proportionality qualifier (GDPR `state of the art` + cost + nature/scope/context/purposes/risks; NIS 2 `appropriate and proportionate` + state-of-the-art; CRA `essential cybersecurity requirements` + 6-phase risk-assessment propagation; DORA `appropriate techniques, methods and protocols` + `controlled manner` + risk-assessment-approach; AI Act `appropriate level` + `perform consistently throughout their lifecycle` + QMS-documented).
- 10 pairwise cells are verified by CRDA-deep as 10 SAME — COMPLEMENTARY (no CORRECTED, no CONTRADICTORY, no SCOPE-DISJOINT in baseline): each regulator targets a distinct target object at a distinct trigger, and they stack on a typical entity that is both controller + NSIE + CRA manufacturer + DORA financial entity + AI Act provider/deployer.
- The high-level SO engages if and only if ≥2 applicable regulations have Y scope overlap on the same party. For a 5-FTE SaaS startup with GDPR + CRA only, the high-level SO engages on the integrated manufacturer-controller-deployer stack. For a NIS 2 essential entity that is not a financial entity and does not manufacture CRA-classified products, only the applicable sub-SOs activate on the GDPR↔NIS2 COMPLEMENTARY pair.
- The DORA dedicated-by-design absence is the operative structural feature: for a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, D-07.1 by-design compliance is demonstrated through the change-management six-step + testing programme outputs, with no standalone OJ-mandated by-design obligation. The OJ-literal absence of a DORA by-design clause is preserved as a structural Layer 2 review item (not a CONTRADICTORY/CORRECTED reclassification).
- NIS 2 Art. 21(2)(e) operates across 3 coordinated phases (acquisition, development, maintenance); CRA Art. 13(2) operates across 6 phases (planning, design, development, production, delivery, maintenance) — the two are not 1:1 aligned but stack at the supplier-customer boundary.
- AI Act Art. 15(4)–(5) AI-specific attack categories (data/model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) do not substitute for CRA Annex I Part I (2)(j) attack-surface limitation or (2)(k) exploitation-mitigation outcomes; the two stack on AI-enabled CRA products with no OJ-level consolidation rule for attack defence.
- The `state of the art` anchor is duplicated across the five regulations but interpreted independently; entities implementing all 5 must reconcile through documented decision records.
- AI Act Recital 78 preserves GDPR, so the two obligations stack with the GDPR personal-data overlay on top of the AI Act AI-system property baseline.
- The per-regulation perspective (target object, trigger, anchor, threshold, evidence template, recipient, legal anchor) is preserved verbatim in the five sub-SOs; the high-level SO does NOT collapse the five target objects, triggers, anchors, thresholds, evidence templates, or recipients into a single by-design architecture.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-07.1 over a distinct **target object** of the secure-by-design architecture; the target object, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the design-lifecycle.
| Axis (reg) | Target object | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | data-protection properties via pseudonymisation + minimisation + by-default limits | controller's means-determination (Art. 25(1)) + processing time (Art. 25(1)) | `state of the art` + `cost of implementation` + `nature, scope, context and purposes of processing` + `risks of varying likelihood and severity` — 4-factor qualitative proportionality (no quantitative threshold) + Art. 25(2) by-default on amount/extent/period/access | supervisory authority (DPA) — Art. 5(2) accountability (documented necessity assessment, often via DPIA per Art. 35 — cross to D-09.2) | Art. 25(1) + Art. 25(2) + Art. 5(1)(f) + Art. 5(2) + Art. 24(1) + Art. 32(1)(a) + Art. 35(7) + Art. 4(5) pseudonymisation definition |
| **NIS2** | NIS lifecycle security across acquisition, development, maintenance (entity side / user side) | NIS-acquisition activity (Art. 21(2)(e) first clause) + development activity (Art. 21(2)(e) second clause) + maintenance activity (Art. 21(2)(e) third clause) + vulnerability handling and disclosure (Art. 21(2)(e) fourth clause) | `appropriate and proportionate` (Art. 21(1) chapeau) + `state of the art` (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative threshold | management body (Art. 20(1) approve+oversee+liability) + competent authority | Art. 21(2)(e) + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Art. 20(1) management-body approval |
| **CRA** | product cybersecurity via Annex I Part I essential requirements | manufacturer places product on market (Art. 13(1)) + planning/design/development/production/delivery/maintenance phases (6 lifecycle phases per Art. 13(2) chapeau) + ongoing during support period per Art. 13(8) | `essential cybersecurity requirements set out in Part I of Annex I` (Art. 13(1)) + risk-assessment propagation across 6 phases (Art. 13(2)) + support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)); no quantitative threshold | market surveillance authority (MSA) — Annex VII §3 risk-assessment record + Annex VII §2 design/development documentation + Annex I Part I (2) sub-point evidence | Art. 13(1) + Art. 13(2) chapeau + sentence 1 + sentence 2 + Art. 13(3) sentence 1 + Art. 13(7) + Art. 13(8) + Art. 13(18) + Annex I Part I chapeau + Annex VII §2 + Annex VII §3 |
| **DORA** | ICT-infrastructure management structure + change-management six-step + patch policies (financial-entity side) | establishment of ICT infrastructure (continuous per Art. 9(4)(b)) + ICT change event (Art. 9(4)(e) six-step) + patch update event (Art. 9(4)(f)) | no OJ dedicated by-design mandate; `appropriate techniques, methods and protocols` (Art. 9(4)(b) qualitative) + Art. 9(4)(e) six-step mandatory (recorded/tested/assessed/approved/implemented/verified) + Art. 4 proportionality under Recital 56; no quantitative threshold for design cadence | competent authority (national financial supervisory authority) + management body — Art. 6(1) ICT risk-management framework + Art. 9(4)(b) infrastructure record + Art. 9(4)(e) change-mgmt policy + Art. 24 testing programme | Art. 9(4)(b) + Art. 9(4)(e) + Art. 9(4)(f) + Art. 6(1) ICT risk-management framework + Art. 24 testing programme (no dedicated by-design OJ clause — partial at D-07.1) |
| **AI_Act** | AI-system accuracy / robustness / cybersecurity (lifecycle-consistent) + QMS design/design-control/design-verification | provider places high-risk AI system on market (Art. 6 + Art. 15(1)) + design/development activity (Art. 17(1)(c)) + design-control sub-process in QMS | `appropriate level of accuracy, robustness, and cybersecurity` (Art. 15(1) qualitative) + `perform consistently … throughout their lifecycle` (Art. 15(1) lifecycle-consistency qualitative) + Art. 15(4)–(5) AI-attack defence (6 attack categories) + Art. 17(1) QMS documented in `systematic and orderly manner` + 13-element closed list (a)–(m); no quantitative threshold | provider (QMS design-control documented) + market surveillance authority (QMS + Annex IV technical documentation) + AI Office (for GPAI on systemic-risk tracking) | Art. 15(1) + Art. 15(4)–(5) + Art. 17(1) + Art. 17(1)(c) + Recital 78 GDPR preservation + Annex IV technical documentation |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
(See the validated-relationships table above for the 5×5 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-07.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations target overlapping target objects on the same party** (e.g.
a financial entity that is also a NIS 2 essential entity AND processes
personal data AND manufactures CRA-classified products AND deploys
high-risk AI — a vertically-integrated financial-manufacturer-controller-
AI-deployer with full GDPR + NIS 2 + CRA + DORA + AI Act applicability on
the same secure-by-design architecture). For an integrated
financial-manufacturer-controller-AI-deployer, all five apply in
sequence: **GDPR gates the controller-side privacy-by-design** (Art. 25(1)
data-protection properties); **NIS 2 specifies the NIS-lifecycle
architecture** (Art. 21(2)(e) acquisition+development+maintenance with
state-of-the-art floor); **CRA certifies the product by-design discipline**
(Art. 13(1) + Annex I Part I + Annex VII §3 risk-assessment record); **DORA
operationalises the change-management six-step + testing programme**
(Art. 9(4)(e) + Art. 24 — the DORA-side by-design operationalisation since
DORA has no OJ-mandated dedicated by-design clause); **AI Act governs the
high-risk AI system design** (Art. 15(1) accuracy+robustness+cybersecurity
+ Art. 17(1)(c) QMS design/design control/design verification). For a
5-FTE SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA /
AI Act applicability, only the GDPR and CRA sub-SOs activate; the high-
level SO engages on the same party on the integrated
manufacturer-controller-deployer stack (CRA Art. 13(1) product by-design
discipline + GDPR Art. 25(1) controller-side data-protection by-design
stack vertically on the same product-lifecycle). For a NIS 2 essential
entity that is not a financial entity and does not manufacture CRA-
classified products (NIS 2 + GDPR only or NIS 2 only with non-CRA-
classified products), only the applicable sub-SOs activate and the high-
level SO engages on the GDPR↔NIS2 COMPLEMENTARY pair. **The five target
objects are layered, not collapsed**: data-protection properties via
pseudonymisation+minimisation (GDPR, controller-driven means-
determination); NIS-lifecycle security across three coordinated phases
(NIS 2, entity-driven continuous supply-chain security); product
cybersecurity via Annex I Part I (CRA, manufacturer-driven per-
component design); ICT-infrastructure management + change-mgmt + testing
(DORA, financial-entity-driven continuous infrastructure management);
AI-system accuracy + robustness + cybersecurity with QMS (AI Act, AI-
system-provider-driven design-lifecycle). The high-level SO surfaces
the common secure-by-design duty but does **NOT** collapse the per-reg
target object, trigger, anchor, threshold, recipient, or evidence
template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **5 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA, AI Act —
  **all 5 participate**, no out-of-scope): GDPR (Art. 25(1)+(2) privacy-
  by-design as controller obligation); NIS 2 (Art. 21(2)(e)
  lifecycle-security as entity obligation); CRA (Art. 13(1)+(2) +
  Annex I Part I as manufacturer obligation); DORA (Art. 9(4)(b)
  + 9(4)(e) + 24 as financial-entity obligation — **partial**: secure-by-
  design is implicit, not an OJ-mandate standalone); AI Act (Art. 15(1)
  + 17(1)(c) as high-risk-AI-system-provider obligation).
- **10 pairwise cells, verified by CRDA-deep as 10 SAME — COMPLEMENTARY
  (no CORRECTED)**: GDPR↔NIS2 (SAME — COMPLEMENTARY — `what` data-
  protection by-design + `that` NIS-lifecycle security stack at
  controller-NSIE); GDPR↔CRA (SAME — COMPLEMENTARY — data-protection
  properties vs. product-cybersecurity via Annex I Part I, integrated-
  manufacturer-controller-deployer); GDPR↔DORA (SAME — COMPLEMENTARY —
  controller-side data-protection by-design overlay on financial-
  entity change-mgmt six-step + testing); GDPR↔AI_Act (SAME —
  COMPLEMENTARY — data-protection by-design overlay on AI-system
  accuracy+robustness+cybersecurity + QMS, Recital 78 preservation);
  NIS2↔CRA (SAME — COMPLEMENTARY — entity-side NIS-lifecycle + maker-
  side product-lifecycle, supplier-customer boundary); NIS2↔DORA (SAME
  — COMPLEMENTARY — NSIE maintenance-phase operationalised through
  DORA change-mgmt six-step); NIS2↔AI_Act (SAME — COMPLEMENTARY — NIS-
  embedding-high-risk-AI integrated stack, NIS 2 procurement gate +
  AI Act QMS); CRA↔DORA (SAME — COMPLEMENTARY — product-side CRA
  by-design feeds DORA design-procurement baseline); CRA↔AI_Act (SAME
  — COMPLEMENTARY — CRA Art. 13(4) sentence 2 explicit
  AI-Act-substitution for risk assessment on AI-enabled-CRA-product);
  DORA↔AI_Act (SAME — COMPLEMENTARY — DORA change-mgmt operational
  gate + AI Act QMS governance gate, no substantive overlap).
- The five regulations impose **distinct secure-by-design duties** at
  **distinct target objects** with **distinct triggers** and **distinct
  anchors**: GDPR controller-side privacy-by-design (Art. 25(1)
  `designed to implement data-protection principles` + 4-factor
  qualitative proportionality state-of-the-art+cost+nature/scope/context/
  purposes/risks + Art. 25(2) by-default on amount/extent/period/access);
  NIS 2 entity-side NIS-lifecycle security (Art. 21(2)(e) acquisition+
  development+maintenance + vulnerability-handling-and-disclosure +
  `appropriate and proportionate` chapeau + state-of-the-art floor +
  Art. 20(1) management-body approval); CRA manufacturer-side product
  by-design (Art. 13(1) `designed, developed and produced per Annex I
  Part I` + Art. 13(2) risk-assessment propagation across 6 lifecycle
  phases + support period ≥ 5 years + Annex VII §3 record); DORA
  financial-entity-side infrastructure management + change-mgmt + testing
  (Art. 9(4)(b) `sound network and infrastructure management structure`
  + Art. 9(4)(e) `recorded, tested, assessed, approved, implemented and
  verified in a controlled manner` six-step + Art. 9(4)(f) patch policies
  + Art. 24 testing programme — **no dedicated by-design OJ clause**,
  secure-by-design operationalised through change-mgmt + testing); AI
  Act AI-system-provider-side design/development with QMS (Art. 15(1)
  `accuracy, robustness, and cybersecurity … perform consistently …
  throughout their lifecycle` + Art. 15(4)–(5) AI-attack defence +
  Art. 17(1) QMS documented in `systematic and orderly manner` + Art.
  17(1)(c) design/design-control/design-verification 3-way AND +
  Recital 78 GDPR preservation). The thresholds align qualitatively
  (GDPR `state of the art` + 4-factor; NIS 2 `appropriate and
  proportionate` + state-of-the-art; CRA `essential cybersecurity
  requirements` of Annex I Part I + support-period ≥ 5 years; DORA
  `appropriate techniques, methods and protocols` + change-mgmt six-step
  + Art. 4 proportionality; AI Act `appropriate level of accuracy,
  robustness, and cybersecurity` + QMS-documented). The five anchors
  align in their direction-of-travel (proportionality calibrated to
  risk) but the target objects, triggers, evidentiary templates,
  recipients diverge.
- The high-level SO describes the **COMMON OBJECTIVE** (security
  integrated into the acquisition, design, development, production,
  deployment and maintenance of systems and products via documented by-
  design decisions + risk-assessment propagation + proportionate
  safeguards + lifecycle consistency); the **per-regulation
  perspective** (target object, trigger, anchor, threshold, recipient,
  evidence template) is preserved verbatim in the five sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the secure-by-design duty itself**,
  because no pair was verified as CONTRADICTORY or CORRECTED (all 10
  pairs are SAME — COMPLEMENTARY). Phase 1C Doc 07 does not need to
  resolve a secure-by-design contradiction because none exist by
  construction. The **DORA dedicated-by-design absence** is a
  **structural Layer 2 review item** — preserved as a partial-participation
  fact and surfaced as a SR-DORA-004 partial mapping. The 5-layer by-
  design architecture (GDPR controller means-determination → NIS 2
  entity NIS-lifecycle → CRA manufacturer product-lifecycle → DORA
  financial-entity change-mgmt six-step + testing → AI Act high-risk AI
  system design + QMS) is itself the layered reconciliation that
  supersedes any single-regulator reading.
- **Scope caveat (CRITICAL — DORA dedicated-by-design absence)** —
  derived from CRDA-deep verified classifications: DORA has no OJ-
  mandated dedicated by-design clause. Art. 9(4)(b) text is "sound
  network and infrastructure management structure using appropriate
  techniques, methods and protocols" — not a by-design mandate. The
  secure-by-design dimension for DORA is operationalised through **Art.
  9(4)(e) change-management six-step** (recorded/tested/assessed/
  approved/implemented/verified in a controlled manner) and **Art. 24
  testing programme** (12-way open list of testing modalities
  including vulnerability assessments, scans, source-code reviews,
  scenario-based tests, compatibility testing, performance testing,
  end-to-end testing, penetration testing). For a DORA-only entity that
  is not a CRA manufacturer and does not process personal data via
  high-risk AI, D-07.1 by-design compliance is demonstrated through
  the change-management six-step + testing programme outputs, with no
  standalone by-design obligation. For a DORA entity that is also a
  CRA manufacturer and processes personal data, the upstream CRA-side
  by-design discipline feeds the downstream DORA-side change-mgmt
  six-step + testing — the upstream→downstream by-design propagation
  is the controlled hand-off with explicit CRA-side disclosure to the
  downstream DORA tier.
- **Scope caveat (CRITICAL — NIS 2 lifecycle security vs GDPR
  privacy-by-design)** — derived from CRDA-deep verified
  classifications: NIS 2 Art. 21(2)(e) addresses `that` secure lifecycle
  discipline applies across acquisition+development+maintenance + vuln
  handling and disclosure; GDPR Art. 25(1) addresses `what` data-
  protection properties must be designed in. For an integrated
  controller-NSIE, the GDPR by-design outputs (pseudonymised-by-default
  pipelines, minimisation by-default, encryption by-default) are
  realised through the NIS 2 acquisition gate (supplier SDLC
  assessment per SR-NIS2-026) and the NIS 2 development gate (in-
  house secure-by-design decisions per SR-NIS2-027). The two regimes
  stack with distinct evidence trails (GDPR: documented Art. 25(1)
  assessment on the controller side via Art. 5(2) accountability; NIS
  2: Art. 21(2)(e) NIS-lifecycle security records + Art. 21(1)
  documented policies on risk analysis + IS security per SR-NIS2-022
  + Art. 20(1) management-body approval).
- **Scope caveat (CRITICAL — CRA product by-design + Annex VII §3 risk
  assessment)** — derived from CRDA-deep verified classifications: CRA
  Art. 13(2) requires that the cybersecurity risk assessment is taken
  into account during planning, design, development, production,
  delivery and maintenance phases — **6 lifecycle phases**. The risk
  assessment is documented (Art. 13(3) sentence 1 + Art. 13(7)) and
  updated when there is a change of risk represented by the product
  (Art. 13(3) sentence 1 `updated as appropriate`). The Annex VII §3
  technical documentation includes the risk-assessment record
  (CRA-CL162). For an integrated manufacturer that is also a
  controller, the CRA-side by-design discipline documents the product
  cybersecurity via Annex I Part I; the controller-side GDPR Art. 25(1)
  by-design discipline documents the personal-data overlay on top of
  the CRA-side product. The CRA Art. 13(4) sentence 2 explicitly
  permits a unified risk assessment under AI Act Art. 9 to substitute
  for the CRA risk assessment when both apply (SR-CRA-066
  `ambiguity_notes`).
- **Scope caveat (CRITICAL — AI Act design/development + QMS)** —
  derived from CRDA-deep verified classifications: AI Act Art. 15(1)
  + Art. 17(1)(c) constitute the AI-Act-side by-design
  architecture — Art. 15(1) sets the lifecycle-consistency accuracy+
  robustness+cybersecurity baseline; Art. 17(1)(c) requires `design,
  design control and design verification` as part of the QMS. The
  Art. 15(4)–(5) AI-attack defence categories (data poisoning, model
  poisoning, adversarial examples, model evasion, confidentiality
  attacks, model flaws) are **AI-specific attack categories** that do
  not substitute for CRA Annex I Part I (j) attack-surface or (k)
  exploitation-mitigation outcomes. For an AI-enabled CRA product, the
  two obligations stack — CRA Annex I Part I (j) + (k) for product-
  level outcomes + AI Act Art. 15(4)–(5) for AI-specific attack
  defence — with no OJ-level consolidation rule for the attack-defence
  dimension (unlike the CRA Art. 13(4) sentence 2 unified-risk-
  assessment carve-out for AI Act Art. 9, which does not extend to
  attack defence).
- **Scope caveat (CRITICAL — `state of the art` anchor is duplicated
  but uncoordinated)** — derived from CRDA-deep verified
  classifications: GDPR Art. 25(1) `taking into account the state of
  the art`; NIS 2 Art. 21(1) sentence 2 `state of the art`; CRA Annex
  I Part I chapeau + Annex I opening (harmonised standards)
  `commensurate with the state of the art`; DORA Art. 4 + Recital 56
  `state of the art` (in the proportionality-anchor sense); AI Act
  Art. 9(1) `state of the art` (risk-management-system anchor) + Art.
  15(1) `appropriate level` + Art. 9(7) `state of the art` for
  testing. Each regulation interprets the anchor independently — GDPR
  weights cost + nature/scope/context/purposes/risks in addition to
  state-of-the-art; NIS 2 weights `appropriate and proportionate`
  chapeau + cost factor; CRA weights Annex I essential-requirements;
  DORA weights financial-entity proportionality under Recital 56 + EBA
  Guidelines; AI Act weights harmonised standards + Art. 9 risk-
  management. An entity implementing all 5 must reconcile the five
  `state of the art` baselines through documented decision records
  (per-regulation baseline + integrated-stack reconciliation).
- **Scope caveat (CRITICAL — 6-phase CRA risk-assessment propagation
  vs 3-phase NIS 2 lifecycle)** — derived from CRDA-deep verified
  classifications: CRA Art. 13(2) propagates the risk assessment
  across 6 lifecycle phases (planning, design, development, production,
  delivery, maintenance); NIS 2 Art. 21(2)(e) operates across 3
  coordinated phases (acquisition, development, maintenance). The two
  regimes are not 1:1 aligned — CRA's `production` and `delivery`
  phases have no direct NIS 2 analogue (NIS 2 stops at the entity-
  side boundary); CRA's `planning` phase has no direct NIS 2 analogue
  either (NIS 2 acquisition assumes the supplier-side work is done).
  For an integrated entity that is both CRA manufacturer + NIS 2 NSIE,
  the 6-phase CRA risk-assessment record + the 3-phase NIS 2 lifecycle
  evidence stack with the CRA-side covering planning/design/development/
  production/delivery/maintenance and the NIS 2-side covering
  acquisition (with vendor SDLC assessment per SR-NIS2-026) /
  development (with in-house secure-by-design decisions per SR-NIS2-027)
  / maintenance (with change-mgmt operationalisation).
---

## Emergent tensions (from CRDA-deep §D-07.1)

#### Emergent tensions (from CRDA-deep §D-07.1)
**0 conditional emergent tensions** on the secure-by-design duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 10 pairs are all SAME — COMPLEMENTARY with different angles, and the five regulators look at secure-by-design from five distinct regulatory perspectives that are **layered rather than contradictory**. **No SCOPE-DISJOINT in baseline** — the 5×5 matrix shows **Y scope overlap** across all 10 pairs in baseline (the GDPR↔DORA pair is Conditional Y on the financial-entity-controller combined stack per the CRDA-deep `scope_overlap` notation; the GDPR↔AI_Act pair is Y on the provider/deployer-controller-processing-personal-data-via-AI stack; all other 8 pairs are Y in baseline). **No CONTRADICTORY pairs** on the secure-by-design duty itself. The **target-object divergence** (data-protection-properties / NIS-lifecycle security / product-cybersecurity via Annex I Part I / ICT-infrastructure-management + change-mgmt six-step + testing / AI-system-accuracy+robustness+cybersecurity + QMS) is the **legitimately diverse dimension**: each regulator targets a distinct target object at a distinct trigger (controller means-determination / NSIE NIS-lifecycle activity / manufacturer places product on market / financial entity establishes ICT infrastructure / provider places high-risk AI system on market), and the operational convergence is on a **5-layer by-design architecture** with explicit layered hand-offs.
The **verbatim-linguistic match between GDPR and AI Act** (privacy-by-design + data-protection properties via pseudonymisation+minimisation on the GDPR side, accuracy+robustness+cybersecurity with lifecycle consistency + QMS design/design-control/design-verification on the AI Act side) discharges both obligations in the high-risk-AI-system-processing-personal-data integrated stack with distinct design outputs (privacy property vs. AI-system property) — **AI-Act-Recital 78 preserves the GDPR** so the two obligations stack with the GDPR personal-data overlay on top of the AI Act AI-system property baseline.
The **DORA dedicated-by-design absence** is the structurally significant divergence: DORA has no OJ-mandated dedicated by-design clause — Art. 9(4)(b) is network/infrastructure-management, Art. 9(4)(f) is patches and updates. The DORA-side by-design operationalisation is via Art. 9(4)(e) change-management six-step + Art. 24 testing programme — operational mechanisms that demonstrate PR.PS-06 mapping without an OJ-mandated dedicated by-design clause. This is a **structural Layer 2 review item** (not a CONTRADICTORY or CORRECTED reclassification) — the DORA participation at D-07.1 is preserved per SR-DORA-004 partial mapping, with the OJ-literal absence of by-design text documented as a Taxonomy-vs-OJ gap.
The **`state of the art` anchor is duplicated but uncoordinated** across the five regulations: GDPR Art. 25(1) `taking into account the state of the art` + cost + nature/scope/context/purposes/risks (4-factor qualitative); NIS 2 Art. 21(1) sentence 2 `state of the art`; CRA Annex I opening `commensurate with the state of the art`; DORA Art. 4 + Recital 56 `state of the art` (proportionality-anchor sense); AI Act Art. 9(1) `state of the art` (risk-management-system anchor) + Art. 9(7) `state of the art` for testing. Each regulation interprets the anchor independently. An entity implementing all 5 must reconcile the five `state of the art` baselines through documented decision records (per-regulation baseline + integrated-stack reconciliation) — the SRS2 `state of the art` POLY is read at the per-reg level per `SR-GDPR-039` etc. The reconciliation is **layered not collapsed** — each reg's `state of the art` baseline stands on its own with the integrated-stack reconciliation providing the cross-reg hand-off.
The high-level SO surfaces the common secure-by-design duty; the per-reg target object, trigger, anchor, threshold, recipient, and evidence template are documented separately in the five sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 5-layer by-design architecture (GDPR controller means-determination → NIS 2 entity NIS-lifecycle → CRA manufacturer product-lifecycle → DORA financial-entity change-mgmt six-step + testing → AI Act high-risk AI system design + QMS) is itself the layered reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-07.1 — with overlapping target-object scope-determiners on the same party — operates a **5-layer by-design architecture** with explicit layered hand-offs. The high-level SO (`SO-D-07.1.HL`) describes the common secure-by-design duty (documented by-design decisions + risk-assessment propagation + proportionate safeguards + lifecycle consistency); the per-reg perspective is preserved in the five sub-SOs (target object, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 5-layer by-design architecture (GDPR gates controller-side privacy-by-design → NIS 2 specifies NIS-lifecycle architecture → CRA certifies product by-design discipline → DORA operationalises change-management six-step + testing → AI Act governs high-risk AI system design + QMS) operationalising the inter-reg hand-offs. The high-level SO does NOT collapse the five target objects into a single by-design architecture; the per-reg perspective on target object, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **secure-by-design strategy**: (1) a 5-layer by-design architecture with explicit target-object hand-offs (GDPR Art. 25(1) data-protection by-design → NIS 2 Art. 21(2)(e) 3-phase NIS-lifecycle → CRA Art. 13(1) + 13(2) + Annex I Part I product-cybersecurity + 6-phase risk-assessment-propagation → DORA Art. 9(4)(b) + 9(4)(e) + 24 infrastructure-management + change-mgmt six-step + testing → AI Act Art. 15(1) + 17(1)(c) accuracy+robustness+cybersecurity + QMS design/design-control/design-verification); (2) the DORA dedicated-by-design absence as a structural Layer 2 review item (no OJ mandate; SR-DORA-004 partial mapping; by-design compliance demonstrated via change-management six-step + testing programme outputs); (3) the NIS 2 maintenance-phase operationalisation through DORA change-management six-step when the entity is a DORA financial entity that is also a NIS 2 NSIE; (4) the CRA `direct` third-party components including non-commercial OSS (Art. 3(48) FOSS) feeding the DORA design-procurement baseline when the deployer is a DORA financial entity (cross to D-06.1 — note: this by-design scope-overlap is with the supply-chain sub-domain, not D-07.1 itself); (5) the CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment on AI-enabled-CRA-products — the by-design risk-assessment obligation is satisfied by the AI Act Art. 9 + Art. 17 risk-management-system documentation that covers both regimes' risk-assessment content; (6) the `state of the art` anchor duplicated-but-uncoordinated across 5 regulations — documented decision records per-regulation baseline + integrated-stack reconciliation; (7) the 6-phase CRA risk-assessment-propagation vs 3-phase NIS 2 lifecycle architecture — the CRA-side planning+design+development+production+delivery+maintenance maps to the NIS 2-side acquisition+development+maintenance with the NIS 2 acquisition covering the supplier-side SDLC equivalent of CRA-side planning+design+development+production; (8) the AI-Act-Recital 78 GDPR preservation operating at the controller-side-by-design-overlay layer for high-risk-AI-system-processing-personal-data integrated stacks; (9) the Annex VII §2 + §3 CRA-side technical documentation as the evidence pack for the manufacturer-side by-design architecture; (10) the Art. 17 QMS as the formal carrier of the AI-Act-side design/design-control/design-verification controls, with the QMS documentation per Art. 11 + 12(2) Annex IV technical documentation as the evidence pack; (11) the D-07.1 by-design outputs propagating downstream to D-07.2 (Secure Coding Practices) as the code-level instruction + D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction + D-07.4 (Change Management) as the DORA-side by-design operationalisation. For proportionality (P2), a 5-FTE SaaS startup with GDPR + CRA applicability may default to the GDPR Art. 25(1) + 25(2) by-design + by-default documentation plus the CRA Art. 13(1) + 13(2) Annex I Part I + 6-phase risk-assessment-propagation (NIS 2 / DORA / AI Act are out of scope unless the SaaS operates in a NIS 2-essential sector, is a financial entity, or is a high-risk AI provider/deployer); a NIS 2 essential entity in a non-financial sector must additionally document the Art. 21(2)(e) NIS-lifecycle architecture + Art. 21(1) `appropriate and proportionate` chapeau + Art. 20(1) management-body approval; a financial entity in scope of all 5 regulations must additionally document the Art. 9(4)(b) + 9(4)(e) + 24 DORA-side by-design operationalisation through change-management six-step + testing programme + Art. 5(2)+(4) management-body define-approve-oversee-responsibility leg, with the GDPR Art. 25(1)+(2) controller-side by-design + by-default documentation appended on the data-protection overlay and the NIS 2 Art. 21(2)(e) NIS-lifecycle security supplied by reference; a CRA manufacturer that is also a high-risk AI provider must additionally document the AI Act Art. 15(1) + 17(1)(c) accuracy+robustness+cybersecurity + QMS design/design-control/design-verification, with the CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 documented.

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-07.1 Secure-by-Design Principles — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md`. See that file for cross-reg verified relationships (10 pairs verified by CRDA-deep as **10 SAME — COMPLEMENTARY — no CORRECTED, no CONTRADICTORY, no SCOPE-DISJOINT in baseline**), scope overlap matrix (all 10 pairs Y or Conditional Y — the five regulators look at secure-by-design from five distinct regulatory perspectives and stack on the typical integrated stack), Objective / Considerations content, DORA dedicated-by-design absence (Layer 2 review item), 6-phase CRA risk-assessment propagation vs 3-phase NIS 2 lifecycle non-alignment, AI-Act-Recital-78 GDPR preservation, `state of the art` anchor duplicated-but-uncoordinated, and aggregation logic. **Scope-title note (P0):** the corpus index title `Secure Design` is reconciled with the CRDA-deep authoritative `Secure-by-Design Principles` — this file covers the by-design architectural-integrity leg only; the by-code leg is in D-07.2 (Volere subtype immunity) and the by-process leg is in D-07.3 / D-07.4. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA, AI Act (5 of 5 regs — all participate per AEGIS taxonomy §4.1; this is the only D-07.x sub-domain with full 5-reg participation). CRDA-deep verified 10 pairs as SAME — COMPLEMENTARY (none required CRDA correction). The five regulators target **distinct target objects** at **distinct boundaries** (data-protection-properties at controller means-determination / NIS-lifecycle security across acquisition+development+maintenance / product-cybersecurity via Annex I Part I across 6 lifecycle phases / ICT-infrastructure-management + change-mgmt six-step at financial-entity side / AI-system-accuracy+robustness+cybersecurity + QMS at high-risk-AI-system-provider side), and the high-level SO surfaces the common secure-by-design duty (security integrated into the lifecycle via documented by-design decisions + risk-assessment propagation + proportionate safeguards + lifecycle consistency) while preserving the per-reg target object. The **DORA dedicated-by-design absence** (no OJ-mandated standalone by-design clause — Art. 9(4)(b) is network/infrastructure-management + Art. 9(4)(f) is patches-and-updates; secure-by-design operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme) is the structural Layer 2 review item — SR-DORA-004 partial mapping preserved.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 7.1
  volere_section: 15
  volere_subtype: integrity
  title: "Security integrated into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation, proportionate safeguards, and lifecycle consistency (5-layer by-design architecture)"
  derives_from:
    hso_sub_so: SO-D-07.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.0"
  description: |
    The product shall integrate security into the acquisition, design, development, production, deployment and maintenance of systems and products via documented by-design decisions, risk-assessment propagation across the regulated lifecycle phases, proportionate safeguards calibrated to the per-regulation anchor, and lifecycle consistency of the by-design properties, as the common secure-by-design duty converging across GDPR Art. 25(1)+(2) data-protection by-design and by-default, NIS 2 Art. 21(2)(e) security in acquisition + development + maintenance, CRA Art. 13(1)+(2) + Annex I Part I essential cybersecurity requirements with 6-phase risk-assessment propagation, DORA Art. 9(4)(b)+(e)+(f) + Art. 24 infrastructure-management + change-management six-step + testing (partial — no OJ dedicated by-design mandate; secure-by-design operationalised through change-mgmt + testing), and AI Act Art. 15(1) + Art. 17(1)(c) accuracy+robustness+cybersecurity with lifecycle consistency + QMS design/design-control/design-verification, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A documented by-design architecture is maintained across the 5-layer by-design stack (GDPR controller-side data-protection by-design / NIS 2 entity-side NIS-lifecycle / CRA manufacturer-side product-lifecycle / DORA financial-entity-side infrastructure-management + change-mgmt + testing / AI Act high-risk-AI-system-provider-side accuracy+robustness+cybersecurity + QMS) with one design-decision record per layer; per-layer evidence trails document (a) target object, (b) trigger event, (c) anchor (the 4-factor GDPR proportionality / NIS 2 `appropriate and proportionate` + state-of-the-art / CRA Annex I essential requirements / DORA `appropriate techniques, methods and protocols` + change-mgmt six-step / AI Act `appropriate level` + QMS), (d) threshold qualifier, (e) recipient, and (f) evidence template; the `state of the art` anchor is reconciled across the 5 regulators through documented decision records (per-regulation baseline + integrated-stack reconciliation) — `state of the art` is interpreted independently per regulation but anchored to a documented common baseline; CRA Art. 13(2) 6-phase risk-assessment propagation (planning / design / development / production / delivery / maintenance) is realised through documented risk-assessment update records per Annex VII §3; NIS 2 Art. 21(2)(e) 3-phase coordinated lifecycle (acquisition / development / maintenance) is realised through supplier-SDLC assessment at acquisition gate + in-house secure-by-design decisions at development gate + vulnerability-handling-and-disclosure + maintenance at maintenance gate (per SR-NIS2-026/027/028); DORA Art. 9(4)(e) change-management six-step (recorded / tested / assessed / approved / implemented / verified in a controlled manner) + Art. 24 testing programme (12-way open list including source-code reviews where feasible) is the DORA-side by-design operationalisation; AI Act Art. 17(1) QMS is documented in `systematic and orderly manner` covering all 13 enumerated aspects (a)–(m) with Art. 17(1)(c) design/design-control/design-verification 3-way AND; the per-layer by-design decision record includes the `state of the art` calibration date and the per-regulation proportionality factors; verified by 5-layer by-design architecture documentation review + per-layer design-decision-record audit + `state of the art` reconciliation-record inspection + CRA Annex VII §3 risk-assessment-record audit + NIS 2 supplier-SDLC assessment + in-house by-design-decision records review + DORA Art. 9(4)(e) change-mgmt policy + Art. 24 testing programme records inspection + AI Act Art. 17(1)(c) QMS design-control record + Annex IV technical-documentation review + DPA / management body + MSA / national CA + ESA / AI Office inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.PS-06, PR.PS-02, PR.PS-01, ID.RA-01, GV.PO-02]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs have Y scope overlap on the same party AND ≥1 sub-SO activates; all 10 pairs are Y or Conditional Y in baseline — see HSO scope-overlap matrix
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    All five participating regulations impose a secure-by-design duty at distinct target objects with distinct anchors: GDPR Art. 25(1) privacy-by-design with state-of-the-art + cost + nature/scope/context/purposes/risks 4-factor qualitative proportionality + Art. 25(2) by-default on amount/extent/period/access; NIS 2 Art. 21(2)(e) entity-level lifecycle discipline across acquisition + development + maintenance with `appropriate and proportionate` chapeau + state-of-the-art floor + cost factor + Art. 20(1) management-body approval + oversight + liability; CRA Art. 13(1) + Art. 13(2) product-level by-design with risk-assessment propagation across 6 lifecycle phases (planning / design / development / production / delivery / maintenance) per Annex I Part I + support period ≥ 5 years + Annex VII §3 risk-assessment record; DORA Art. 9(4)(b) + Art. 9(4)(f) network-and-infrastructure management + patch policies — secure-by-design is implicit (no OJ-mandated standalone by-design clause), operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme + Art. 6(1) ICT risk-management framework + Art. 5(2)+(4) management-body responsibility; AI Act Art. 15(1) + Art. 17(1)(c) high-risk AI system accuracy, robustness, and cybersecurity with lifecycle consistency + QMS design/design-control/design-verification + Art. 17(1) 13-element closed list. The five target objects (data-protection-properties / NIS-lifecycle security / product-cybersecurity via Annex I Part I / ICT-infrastructure-management + change-mgmt / AI-system-accuracy-robustness-cybersecurity + QMS) are layered, not collapsed. The high-level SO surfaces the common secure-by-design duty (documented by-design decisions + risk-assessment propagation + proportionate safeguards + lifecycle consistency); the per-regulation perspective is preserved verbatim in the five sub-SOs. 10 pairwise cells are verified by CRDA-deep as 10 SAME — COMPLEMENTARY (no CORRECTED, no CONTRADICTORY, no SCOPE-DISJOINT in baseline): each regulator targets a distinct target object at a distinct trigger, and they stack on a typical entity that is both controller + NSIE + CRA manufacturer + DORA financial entity + AI Act provider/deployer. The 0 conditional emergent tensions are documented as the layered 5-layer reconciliation. The DORA dedicated-by-design absence is the structurally significant divergence: DORA OJ Art. 9(4)(b) is `sound network and infrastructure management structure using appropriate techniques, methods and protocols` — not a by-design mandate; the secure-by-design dimension for DORA is operationalised through Art. 9(4)(e) change-management six-step + Art. 24 testing programme (Layer 2 review item — SR-DORA-004 partial mapping at D-07.1). The `state of the art` anchor is duplicated across the five regulations but interpreted independently — entities implementing all 5 must reconcile through documented decision records (per-regulation baseline + integrated-stack reconciliation). AI Act Recital 78 preserves GDPR — the two obligations stack with the GDPR personal-data overlay on top of the AI Act AI-system property baseline. (Copied from the HSO Considerations block of `### D-07.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-07.1
title: D-07.1 Secure-by-Design Principles — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.1 Secure-by-Design Principles
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---
> **Deep analysis:** [D-07.1 Secure-by-Design Principles](../../DeepAnalysis/D-07_Secure-Development/D-07.1.md)
#### D-07.1 Secure-by-Design Principles
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-024 | Data-protection principles integrated at means-determination and processing time with by-design safeguards (Art. 25(1)). | Privacy-by-design as a controller obligation; minimisation/pseudonymisation/encryption as the canonical by-design techniques. |
| NIS2 | SO-NIS2-017 | Security in acquisition, development, and maintenance of NIS across the system lifecycle (Art. 21(2)(e)). | Entity-level lifecycle discipline; three coordinated phases (acquisition, development, maintenance). |
| CRA | SO-CRA-045 | Design, development, production per Annex I Part I across 6 lifecycle phases with risk-assessment propagation (Art. 13(1)/(2)). | Product-level by-design; essential-requirement conformance with health-and-safety of users as a cross-cutting objective. |
| DORA | SO-DORA-004 (partial) | Network/infrastructure management structure + patch policies (Art. 9(4)(b)+(f)) — design dimension is operationalised through change mgmt. | Financial-entity operational resilience; secure-by-design is implicit, not an OJ-mandate standalone. |
| AI_Act | SO-AIACT-009 + SO-AIACT-010 | Accuracy/robustness/cybersecurity baseline across lifecycle (Art. 15) + QMS with 13 enumerated aspects including design/design control/design verification (Art. 17). | AI-system-specific design discipline; QMS as the formal carrier of design controls. |
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
- **No by-design mandate in DORA creates a supplier-conformance gap**: All other 4 regulations impose a by-design obligation (GDPR via Art. 25; NIS 2 via Art. 21(2)(e); CRA via Art. 13(1)/(2); AI Act via Art. 17(1)). DORA's coverage is implicit (operationalised through change-management). A DORA-only entity has no OJ-mandated by-design baseline, and DORA entities procuring CRA-regulated products must demonstrate that the upstream CRA design discipline substitutes for the absent DORA by-design obligation.
- **The `state of the art` anchor is duplicated but uncoordinated**: GDPR Art. 25(1), NIS 2 Art. 21(1) sentence 2, CRA Annex I opening, DORA Art. 4, and AI Act Art. 9(1) all anchor to `state of the art` — but each regulation interprets the anchor independently. An entity implementing all 5 must reconcile the five `state of the art` baselines (industry-framework reading in GDPR; cost/state-of-the-art in NIS 2; Annex I essential-requirements in CRA; EBA Guidelines in DORA; harmonised standards + AI Act Art. 9 risk-management in AI Act).
<!-- /emergent -->
##### SR cross-validation
The 5 regulations map D-07.1 by-design to the NIST CSF 2.0 Subcategories **PR.PS-06** (Secure software development practices integrated, and their performance is monitored throughout the SDLC) and **PR.PS-02** (Software is maintained, replaced, and removed commensurate with risk) as the dominant pair. GDPR additionally maps **PR.DS-12** (Data managed consistent with risk strategy) for the by-design data-protection dimension; CRA additionally maps **PR.PS-01** (Configuration management practices established, documented, and applied) for the by-default layer. The CSF mapping converges on the SDLC-discipline anchor with regulation-specific additions on the data/configuration/asset dimensions.
##### Downstream implication
A Phase 1 entity must implement at minimum one by-design obligation from each applicable regulation — the regimes stack, not substitute. The CRA-conformant product design serves as the upstream gate for NIS 2 / DORA / AI Act deployment decisions. GDPR by-design outputs (pseudonymisation, minimisation) become a CRA Annex I input only when the product processes personal data — the cross-regulation propagation is conditional on data-classification overlap.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-07.1
title: D-07.1 Secure-by-Design Principles — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.1 Secure-by-Design Principles
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-07_Secure-Development/D-07.1.md
status: DRAFT
---
> **Domain analysis:** [D-07.1 Secure-by-Design Principles](../../DomainAnalysis/D-07_Secure-Development/D-07.1.md)
#### D-07.1 Secure-by-Design Principles
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Sole-authority / partial-coverage notes:** DORA is "partial" coverage — the OJ Art. 9(4)(b) text addresses network/infrastructure management structure, not a dedicated by-design mandate. Secure-by-design is operationalised through DORA's change-management and testing-programme architecture (Art. 9(4)(e), Art. 24). This is reflected in the SR-DORA-004 SR mapping (Art. 7(2) + Art. 8(2)) and SR-DORA-006 (Art. 9(4)(b)).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

