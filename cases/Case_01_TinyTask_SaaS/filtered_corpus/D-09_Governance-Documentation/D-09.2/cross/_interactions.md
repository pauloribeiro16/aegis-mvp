<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-09.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-09.2 Impact & Risk Assessments](../../DomainAnalysis/D-09_Governance-Documentation/D-09.2.md)
#### D-09.2 Impact & Risk Assessments
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Critical note (CRDA flag):** D-09.2 is the most heavily-overlapped sub-domain. All 5 regulations overlap with distinct risk/impact assessment regimes from different angles: GDPR DPIA (Art. 35), NIS 2 risk analysis (Art. 21(2)(a) + Art. 22), CRA cybersecurity risk assessment (Art. 13(3) + Annex VII §3), DORA ICT risk framework (Art. 6/7), AI Act FRIA (Art. 9). The assessments are NOT cross-referenced at the OJ level — each is a separate artefact with distinct triggers, content, and review cadences. The ONLY OJ-level consolidation rule is CRA Art. 13(4) sentence 2 (AI Act Art. 9 risk management substitutes for CRA risk assessment).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-09.2 Impact & Risk Assessments
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md)
> (10 pairs verified against OJ text — **5 participating regulations
> are GDPR, NIS 2, CRA, DORA, AI Act; all 5 participate** as noted by
> `DomainAnalysis/D-09_Governance-Documentation/D-09.2.md`
> line 27: "Participants: GDPR, NIS2, CRA, DORA, AI_Act" and line 27
> critical note: "CRITICAL FOR D-09.2. All 5 regulations overlap.
> Each imposes a distinct risk/impact assessment regime from a
> different angle … The assessments are NOT cross-referenced at the
> OJ level — each is a separate artefact with distinct triggers,
> content, and review cadences").
>
> **Critical note (CRDA flag).** D-09.2 has the **only OJ-level cross-
> regulation consolidation rule** — **CRA Art. 13(4) sentence 2**: `The
> cybersecurity risk assessment referred to in paragraph 2 shall be
> part of, or combined with, the risk assessment required by other
> Union legal acts applicable to the product with digital elements.`
> This permits the AI Act Art. 9 risk-management system to substitute
> for the CRA cybersecurity risk assessment when both apply to the same
> product (per SR-CRA-066 ambiguity_notes). The other 9 pairs have no
> OJ-level consolidation. **No CORRECTED, no CONTRADICTORY** pairs.
> The high-level SO surfaces the **common risk-assessment duty**
> (documented assessment + identified risks + mitigation measures +
> review cadence), recognising the 5 distinct assessment *objects*
> (data-subject rights / entity operational / product cybersecurity /
> ICT operational / AI-system) and the 5 distinct review cadences.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-09.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-028 + SO-GDPR-036 + SO-GDPR-037 (cross-ref) | DPIA covering the four Art. 35(7) content items (systematic description, necessity & proportionality, risks, mitigation); reviewed on change of risk per Art. 35(11); joint-controller arrangement per Art. 26 (cross to D-06.3); DPO designation per Art. 37-39 cross-referenced from D-09.1. | Personal-data-rights impact; pre-launch for high-risk processing; reviewed on risk change. |
| NIS2 | SO-NIS2-022 + SO-NIS2-016 + SR-NIS2-028 (Art. 21(1)) | Policies on risk analysis + EU-level coordinated supply-chain risk assessments via Art. 22(1) Cooperation Group (cross to D-09.4); all-hazards methodology with appropriate-and-proportionate chapeau and state-of-the-art floor + cost factor per Recital 56 + entity-discretionary interpretation. | Entity-level operational continuous risk analysis + EU-level coordinated assessments; no pre-launch DPIA. |
| CRA | SO-CRA-053 + SO-CRA-054 | Cybersecurity risk assessment documented + updated during support period (Art. 13(3) sentence 1); covers intended purpose + reasonably foreseeable use including operational environment and assets to be protected (Art. 13(3) sentence 2); maps Annex I Part I (2) applicability and indicates how those requirements are implemented as informed by the risk assessment (Art. 13(3) sentence 3); documented in Annex VII §3 risk-assessment record; reviewed on material change of risk (Art. 13(3) sentence 1 `updated as appropriate`). | Product-level pre-market + support-period cybersecurity risk assessment; supports Annex I Part I (2) applicability mapping; **subject to CRA Art. 13(4) sentence 2 consolidation rule** with AI Act Art. 9 risk management. |
| DORA | SO-DORA-017 + SO-DORA-003 | Three-lines-of-defence model + ICT supported business functions / information assets / ICT assets identification, classification, documentation (Art. 6(4) + Art. 7(1) — cross to D-09.3); ICT risk identification register on a continuous basis with at-least-yearly risk-scenario review (Art. 7(2) sentence 1 + sentence 2). | Financial-entity operational ICT risk framework; continuous + yearly review; no pre-launch DPIA-equivalent. |
| AI_Act | SO-AIACT-001 | Continuous, iterative risk-management system across AI lifecycle (Art. 9(1) `established, implemented, documented and maintained`) with 4-step process (Art. 9(2)(a) identify/analyse known + reasonably foreseeable risks; (b) estimate/evaluate reasonably-foreseeable-misuse risks; (c) evaluate post-market-monitoring-data risks; (d) adopt appropriate and targeted risk-management measures); cross-coupled with Art. 27 FRIA for certain Annex III categories. | AI-system pre-market + post-market risk-management system; Art. 9 risk management as the FRIA-equivalent; **subject to CRA Art. 13(4) sentence 2 consolidation rule** with CRA Art. 13(3) risk assessment. |

## Validated relationships (from CRDA-deep §D-09.2)

#### Validated relationships (from CRDA-deep §D-09.2)
Of 10 pairs, **10 verified as SAME — no CORRECTED, no CONTRADICTORY**. The 10 verified relationships are distributed as **4 SAME — DIFFERENT-PERSPECTIVE + 5 SAME — COMPLEMENTARY + 1 SAME — EQUAL (NIS 2 ↔ DORA)**. The architecture is **legitimately diverse with 1 OJ-level consolidation rule** — the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR-involving pairs) reflect the structural pre-launch DPIA vs operational-continuous asymmetry; the 5 SAME — COMPLEMENTARY pairs reflect non-GDPR pairs where the assessment regimes operate on distinct objects or layers with no consolidation rule (except the CRA↔AI_Act pair); the 1 SAME — EQUAL pair (NIS 2 ↔ DORA) discharges both obligations on the DORA-dominant stack for financial entities. **CRDA flag: ONLY the CRA Art. 13(4) sentence 2 pair (CRA ↔ AI Act) has an OJ-level consolidation rule permitting substitution** — for AI-enabled CRA-regulated products, the AI Act Art. 9 risk-management system can substitute for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes):
- **GDPR ↔ NIS2** — DIFFERENT-PERSPECTIVE (SAME): GDPR DPIA is **pre-launch for high-risk personal-data processing** (Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` + Art. 35(11) `review on change of risk`); NIS 2 risk analysis is **operational continuous** (Art. 21(2)(a) `policies on risk analysis and information system security`). The two regimes do not substitute — a controller-NSIE must operate both. Different triggers (pre-launch DPIA vs continuous operational); different cadences (on-change review vs continuous methodology); different content (4-item Art. 35(7) GDPR DPIA content vs no codified content under NIS 2 entity-discretionary under Recital 56). No reclassification required. Scope-disjoint test: **Conditional (Y when the DPIA is conducted for an NSIE's processing; N otherwise)**.
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): GDPR DPIA assesses impact on **data subjects' rights and freedoms** (Art. 35(7)(c) `an assessment of the risks to the rights and freedoms of data subjects`); CRA cybersecurity risk assessment assesses **cybersecurity risks to the product and its users** (Art. 13(2) `cybersecurity risk assessment … based on the intended purpose and reasonably foreseeable use`). The two risk **objects** differ (rights-and-freedoms vs cybersecurity). For a CRA-regulated product that processes personal data, both assessments are required, but the OJ does not require cross-referencing. **The CRA Art. 13(4) sentence 2 carve-out for AI Act Art. 9 unified-risk-assessment does NOT extend to GDPR DPIA** — even when the CRA risk assessment has been performed, the GDPR DPIA must be a separate artefact covering the data-subject-rights perspective. No reclassification required. Scope-disjoint test: **Y (when the CRA-regulated product processes personal data)**.
- **GDPR ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME): GDPR DPIA is **pre-launch** for high-risk processing; DORA risk framework is **operational continuous + at-least-yearly review** (Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios`). **No pre-launch DPIA-equivalent in DORA**. The two regimes do not substitute — a DORA financial entity that is a controller must operate both. Different triggers (high-risk-processing event vs continuous operational); different cadences (on-change review vs continuous + yearly); different content (4-item Art. 35(7) GDPR DPIA content vs ICT risk identification register + risk-scenario register per DORA Art. 7(2)). No reclassification required. Scope-disjoint test: **Y (when the DORA financial entity conducts a DPIA for high-risk personal-data processing)**.
- **GDPR ↔ AI_Act** — DIFFERENT-PERSPECTIVE (SAME): GDPR DPIA is **pre-launch for high-risk processing**; AI Act Art. 9 risk management is **continuous across the AI lifecycle** (Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step process). The two assessments **overlap in scope for AI systems processing personal data** but the triggers differ (high-risk-processing trigger vs high-risk-AI trigger). AI Act Recital 78 preserves GDPR (`protection of natural persons in relation to the processing of personal data … governed by Regulation (EU) 2016/679` and the broader preservation of Regulation (EU) 2018/1725); the two stack without substitution. **AI Act Art. 27 FRIA may be required for certain Annex III categories** (cross-coupled with the DPIA). No reclassification required. Scope-disjoint test: **Y (when a high-risk AI system processes personal data)**.
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 risk analysis is **entity-level operational** (Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(3) sentence 2 take-into-account Art. 22 coordinated supply-chain assessments + SR-NIS2-028 Art. 21(1) state-of-the-art + cost factor); CRA risk assessment is **product-level pre-market** (Art. 13(3) sentence 1 `documented and updated` + Annex VII §3 risk-assessment record). The two regimes meet at the supplier-customer interface — a CRA-conformant product's risk assessment is an input to the NIS 2 entity's supplier-risk register (cross to D-06.1 Vendor Risk Assessment). No reclassification required. Scope-disjoint test: **Y (when the entity procures CRA-conformant products)**.
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose risk-analysis obligations. NIS 2: Art. 21(2)(a) `policies on risk analysis and information system security` (entity-discretionary under Recital 56 proportionality + state-of-the-art floor per Art. 21(1)). DORA: Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios`. The two regulations impose **continuous operational risk identification** with overlapping compliance obligation. DORA's three-lines-of-defence is the dominant authority for financial entities under DORA's direct scope; NIS 2 applies to the financial entity only insofar as it is an NSIE outside DORA. Scope-disjoint test: **Y (when the DORA financial entity is also an NSIE applying risk-analysis)**. No reclassification required.
- **NIS2 ↔ AI_Act** — COMPLEMENTARY (SAME): NIS 2 risk analysis is **entity-level operational** (Art. 21(2)(a)); AI Act risk management is **AI-system-level continuous iterative** (Art. 9(1) + Art. 9(2) 4-step process). For NSIEs deploying high-risk AI, both apply — the AI Act layer adds the AI-specific 4-step process to the NIS 2 risk-analysis policy. Scope-disjoint test: **Y (when an NSIE deploys high-risk AI)**. No reclassification required.
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA risk assessment is **product-level pre-market** (Art. 13(3)); DORA three-lines-of-defence is **entity-level operational governance** (Art. 6(4)). The two regimes do not substitute — a DORA entity procuring CRA products must discharge both. No reclassification required. Scope-disjoint test: **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)**.
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME) **with critical consolidation rule**: CRA Art. 13(4) sentence 2 explicitly permits the AI Act Art. 9 risk-management system to substitute for the CRA cybersecurity risk assessment when both apply to the same product: `The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements.` Per SR-CRA-066 ambiguity_notes: `For AI-enabled products that are both CRA-regulated and AI-Act high-risk, the AI Act Art. 9 risk-management system can be the CRA cybersecurity risk assessment artefact (part of, or combined with). The two regimes co-discharge on a single artefact when both apply to the same product.` **This is the only OJ-level cross-regulation consolidation rule in D-09.2.** No other cross-regulation consolidation exists. No reclassification required. Scope-disjoint test: **Y (when the same product is both CRA-regulated and AI-Act high-risk)**.
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME): DORA ICT risk framework is **entity-level operational** (Art. 6(4) + Art. 7(2) sentence 1 + sentence 2); AI Act risk management is **AI-system-level continuous iterative** (Art. 9(1) + Art. 9(2) 4-step process). The two stack without OJ-level consolidation (DORA has no equivalent to CRA Art. 13(4) sentence 2). Scope-disjoint test: **Y (when a DORA financial entity deploys high-risk AI)**. No reclassification required.
The impact-and-risk-assessment architecture is **legitimately diverse with 5 distinct assessment *objects* + 5 distinct review cadences + 1 OJ-level consolidation rule**. The five regulators impose assessment regimes from five distinct regulatory perspectives on five distinct assessment objects with five distinct lifecycle phases and review cadences: **GDPR DPIA on data-subject rights (pre-launch + on-change review)**; **NIS 2 risk analysis on entity operational risk (continuous + Recital 56 proportionality)**; **CRA cybersecurity risk assessment on product cybersecurity risk (pre-market + support-period + on-material-change review)**; **DORA ICT risk framework on financial-entity ICT operational risk (continuous + at-least-yearly review)**; **AI Act risk management on AI-system risk (continuous iterative across AI lifecycle)**. The **only OJ-level consolidation rule** is CRA Art. 13(4) sentence 2 — the AI Act Art. 9 risk-management system can substitute for the CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product. No other cross-regulation substitution is OJ-permitted. The 9 other pairs must operate on distinct artefacts (DPIA + NIS 2 risk-analysis policy + CRA risk-assessment record + DORA risk identification register + AI Act risk-management system as 5 separate artefacts for a vertically-integrated stack — DORA financial entity that is a controller deploying CRA-regulated high-risk AI).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Y (CRA-regulated product processes personal data; **no OJ-level consolidation rule** — GDPR DPIA must be a separate artefact even when CRA risk assessment performed; object differs — rights-and-freedoms vs cybersecurity)  |
|  **CRA**  |  Y (same; reciprocal — CRA-regulated product processes personal data; **no OJ-level consolidation rule**; CRA product-level pre-market + support-period; object differs — rights-and-freedoms vs cybersecurity)  |  —  |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional (Y/N)** = conditional overlap depending on entity-product combination — Y when the listed entity-product combination applies on a single party, N otherwise. **CRITICAL** = the only OJ-level cross-regulation consolidation rule in D-09.2 (CRA Art. 13(4) sentence 2 — substitution with AI Act Art. 9). CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Conditional (Y when DPIA conducted for NSIE's processing); GDPR↔CRA = Y (no OJ-level consolidation); GDPR↔DORA = Y (no OJ-level consolidation); GDPR↔AI_Act = Y (no OJ-level consolidation); NIS2↔CRA = Y; NIS2↔DORA = Y; NIS2↔AI_Act = Y; CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant); CRA↔AI_Act = Y (CRA Art. 13(4) sentence 2 consolidation rule); DORA↔AI_Act = Y (no OJ-level consolidation).

## Cross-recipient map

#### Cross-recipient map
D-09.2 generates a layered recipient set on the **impact-and-risk-assessment evidence trail** but does **not generate a notification cascade of D-09.2 itself**. The recipient set is at the **assessment-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 35(7) DPIA content + Art. 35(11) review records + Art. 36(1) prior consultation where residual risk is high (cross to D-04.3 Regulatory Notification) + joint-controller arrangement per Art. 26 (cross to D-06.3) + Art. 5(2) accountability burden; **NIS 2's management body + competent authority** on the Art. 21(2)(a) `policies on risk analysis and information system security` + SR-NIS2-028 Art. 21(1) state-of-the-art + cost factor + Art. 22(1) EU-level Cooperation Group coordinated supply-chain risk assessments (cross to D-09.4); **CRA's market surveillance authority (MSA)** on the Art. 13(3) sentence 1 documented-and-updated cybersecurity risk assessment + Annex VII §3 risk-assessment record + Art. 13(3) sentence 2 intended-purpose + reasonably-foreseeable-use analysis + Art. 13(3) sentence 3 Annex I Part I (2) applicability mapping + Art. 13(4) sentence 2 consolidation with AI Act Art. 9; **DORA's competent authority (NCA — national financial supervisory authority)** on the Art. 7(2) sentence 1 continuous ICT risk identification register + sentence 2 at-least-yearly risk-scenario review records + Art. 6(4) three-lines-of-defence documentation + EBA Guidelines on ICT and security risk management supervisory baseline; **AI Act's market surveillance authority + AI Office** on the Art. 9(1) `established, implemented, documented and maintained` risk-management system + Art. 9(2) 4-step (a)-(d) documentation + Art. 27 FRIA for certain Annex III categories. These are distinct regulatory channels on the same assessment-records artefacts but they do not generate a notification cascade of D-09.2 itself — they are **compliance-evidence channels on the layered assessment architecture**. The **D-09.1 (Information Security Policies)** is the policy upstream artefact where the 5 assessment regimes are calibrated against the per-reg policy architectures; **D-09.3 (Asset Inventories)** is the documentation downstream artefact where DORA Art. 7(1) `identify, classify and adequately document` ICT supported business functions + information assets + ICT assets operates; **D-09.4 (Records of Processing)** is the documentation downstream artefact where GDPR RoPA + CRA technical documentation + AI Act Annex IV technical documentation + DORA ICT asset registers stack.
---

## HSO considerations (from D-09.2.0 — High-level SecurityObjective)

**Considerations.**
- 5 of 5 regulations participate with **distinct assessment objects and cadences** — GDPR (Art. 35(1) + Art. 35(7) 4-item content + Art. 35(11) — pre-launch DPIA on data-subject rights, on-change review), NIS 2 (Art. 21(2)(a) + Art. 22(1) — continuous operational risk-analysis policy, all-hazards methodology under Recital 56), CRA (Art. 13(3) + Annex VII §3 — pre-market + support-period cybersecurity risk assessment, on-material-change review), DORA (Art. 6(4) + Art. 7(2) — continuous + at-least-yearly ICT risk framework), AI Act (Art. 9(1) + Art. 9(2)(a)-(d) 4-step — continuous iterative risk-management system across AI lifecycle; Art. 27 FRIA for certain Annex III categories).
- **CRDA-deep verified (10 pairs: 4 SAME — DIFFERENT-PERSPECTIVE all 4 GDPR pairs reflecting pre-launch DPIA vs continuous/iterative asymmetry + 5 SAME — COMPLEMENTARY + 1 SAME — EQUAL NIS 2 ↔ DORA on continuous operational risk identification, DORA-dominant for financial entities)** — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs; the high-level SO does NOT collapse the 5 distinct assessment regimes.
- **Single OJ-level cross-regulation consolidation rule — CRA Art. 13(4) sentence 2**: `The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements.` For AI-enabled CRA-regulated products, a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes) — the only OJ-level consolidation rule in D-09.2. No other cross-regulation substitution is OJ-permitted.
- **Scope caveats**: (a) 5 cadences are not synchronised (pre-launch / continuous / pre-market + support-period / continuous + yearly / continuous iterative) — an entity must satisfy 5 independent review triggers without a unified cadence; (b) GDPR DPIA does NOT address cybersecurity risk per CRDA flag (DomainAnalysis §D-09.2 line 175) — for CRA-regulated products processing personal data, GDPR DPIA must be a separate artefact even when the CRA risk assessment has been performed; (c) NIS 2 ↔ DORA EQUAL discharges both obligations on the DORA-dominant stack for financial entities.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-09.2 over a distinct **assessment object** of the impact-and-risk-assessment architecture; the assessment object, the trigger, the content template, the threshold anchor, the recipient, the review cadence, and the legal anchor all depend on which perspective the regulation takes on the assessment object.
| Axis (reg) | Assessment object | Trigger | Content template | Review cadence | Recipient | Legal anchor |
|---|---|---|---|---|---|---|
| **GDPR** | data-subject rights and freedoms (risks to rights-and-freedoms dimension) — pre-launch DPIA on high-risk personal-data processing | high-risk-processing event (Art. 35(1) `likely to result in a high risk to the rights and freedoms of natural persons`) | 4-item Art. 35(7) closed list: (a) systematic description of the envisaged processing operations and the purposes of the processing, including where applicable the legitimate interest pursued by the controller; (b) assessment of the necessity and proportionality of the processing operations in relation to the purposes; (c) assessment of the risks to the rights and freedoms of data subjects; (d) measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation | pre-launch + on-change review per Art. 35(11) `review … where there has been a change of the risk represented by processing operations` | supervisory authority (DPA) — Art. 35(7) DPIA content + Art. 35(11) review records + Art. 36(1) prior consultation where residual risk is high (cross to D-04.3) + Art. 5(2) accountability burden + Art. 26(1) joint-controller arrangement (cross to D-06.3) | Art. 35(1) + Art. 35(4) (DPA consultation triggers) + Art. 35(7) 4-item content + Art. 35(11) review cadence + Art. 36(1) prior consultation + Art. 4(7) (controller/joint controllers) + Art. 26(1) joint-controller arrangement + Art. 5(2) accountability + Art. 24(1) appropriate measures |
| **NIS2** | entity operational cybersecurity risk (network-and-information-systems dimension) — continuous risk-analysis policy | entity-establishment / on-going operational | not codified for content — entity-discretionary under Recital 56 proportionality + Art. 21(1) chapeau `appropriate and proportionate … taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity` + state-of-the-art floor (Art. 21(1) sentence 2) + cost factor (Recital 56); all-hazards methodology per SR-NIS2-040 | continuous (no codified cadence); entity-discretionary under Recital 56 | management body + competent authority — Art. 21(2)(a) risk-analysis policy + Art. 22(1) Cooperation Group coordinated assessments + Art. 20(1) management-body approval; cross to D-09.4 for EU-level coordinated assessments | Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art (Art. 21(1) sentence 2) + Recital 56 cost factor + Art. 22(1) Cooperation Group coordinated supply-chain assessments + Art. 20(1) management-body approve/oversee/liable + SR-NIS2-028 Art. 21(1) state-of-the-art + cost factor + SR-NIS2-040 all-hazards methodology |
| **CRA** | product cybersecurity risk (product-side dimension) — pre-market + support-period cybersecurity risk assessment; Annex I Part I (2) applicability mapping | product placement on market (Art. 13(1) trigger) + support-period maintenance (Art. 13(8) — cross to D-09.4) + on-change review of risk | not codified for content template; substantively per Art. 13(2) `take into account the intended purpose and reasonably foreseeable use, including operational environment and assets to be protected` + Art. 13(3) sentence 3 `indicate whether and in what manner the Annex I Part I (2) requirements apply to the relevant product and how those requirements are implemented as informed by the risk assessment` + Annex VII §3 risk-assessment record | pre-market + on-change review of risk per Art. 13(3) sentence 1 `updated as appropriate` (material change of product, material change of threat landscape, or upon becoming aware of a previously unidentified vulnerability per SR-CRA-066) | market surveillance authority (MSA) — Art. 13(3) documented + updated + Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping + Art. 13(4) sentence 1 technical-documentation inclusion + Art. 13(4) sentence 2 unification with AI Act Art. 9 risk management | Art. 13(2) risk assessment (intended purpose + reasonably foreseeable use + operational environment + assets to be protected) + Art. 13(3) sentence 1 `documented and updated` + sentence 2 `intended purpose and reasonably foreseeable use` + sentence 3 `Annex I Part I (2) applicability mapping` + Art. 13(4) sentence 1 (technical-documentation inclusion) + Art. 13(4) sentence 2 (consolidation with AI Act Art. 9 risk management) + Art. 13(7) update on becoming aware of vulnerability + Art. 13(8) support period + Annex I Part I (2) applicability + Annex VII §3 risk-assessment record |
| **DORA** | financial-entity ICT operational risk (ICT-supported business functions dimension) — continuous + at-least-yearly review | financial-entity establishment / on-going operational | ICT risk identification register (sources of ICT risk, exposure to/from other financial entities, cyber threats, ICT vulnerabilities relevant to ICT supported business functions / information assets / ICT assets per Art. 7(2) sentence 1) + risk-scenario register (reviewed at-least-yearly per Art. 7(2) sentence 2) | continuous + at-least-yearly per Art. 7(2) sentence 1 + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them` | competent authority (NCA — national financial supervisory authority) — Art. 7(2) sentence 1 continuous ICT risk identification register + sentence 2 at-least-yearly risk-scenario review + Art. 6(4) three-lines-of-defence documentation + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 6(4) `three lines of defence model` (or internal risk management and control model) + Art. 7(1) `identify, classify and adequately document` ICT supported business functions + information assets + ICT assets + Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them` + EBA Guidelines on ICT and security risk management supervisory baseline |
| **AI_Act** | AI-system risk (high-risk AI system lifecycle dimension) — continuous iterative risk-management system | high-risk AI system lifecycle (continuous + iterative per Art. 9(1) `established, implemented, documented and maintained in relation to high-risk AI systems`) | 4-step Art. 9(2) closed list: (a) the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights; (b) the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks arising from analysis of post-market monitoring data; (d) the adoption of appropriate and targeted risk-management measures; cross-coupled with Art. 27 FRIA for certain Annex III categories | continuous + iterative across AI lifecycle per Art. 9(1) `established, implemented, documented and maintained` | provider + MSA + AI Office — Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step documentation + Art. 27 FRIA documentation for certain Annex III categories + cross-coupling with deployer measures per Art. 26(1) | Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2) 4-step closed list (a)-(d) `known and the reasonably foreseeable risks to health, safety and fundamental rights` + `reasonably foreseeable misuse` + `post-market monitoring data` + `appropriate and targeted risk-management measures` + Art. 27 FRIA for certain Annex III categories + Art. 26(1) deployer measures aligned with provider instructions |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
(See the validated-relationships table above for the 5×5 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-09.2.HL`) engages on a given party **if and only if ≥2 applicable
regulations have ≥1 Y or Conditional-Y-scope-overlap pair on the same
party** (e.g. a DORA financial entity that is also a controller
processing personal data via a CRA-regulated high-risk AI system — a
vertically-integrated financial-controller-manufacturer-AI-deployer
with all 5 regs applicable). For an integrated DORA financial entity
that is also a controller, the GDPR + DORA sub-SOs activate; the high-
level SO engages on the GDPR↔DORA DIFFERENT-PERSPECTIVE pair (pre-
launch DPIA on data-subject rights vs continuous + at-least-yearly DORA
risk framework; no OJ-level consolidation). For an entity with GDPR +
CRA + AI Act applicability on a CRA-regulated high-risk AI that
processes personal data, the GDPR + CRA + AI Act sub-SOs activate; the
high-level SO engages on the GDPR↔CRA + GDPR↔AI_Act DIFFERENT-
PERSPECTIVE pairs (no OJ-level consolidation on the GDPR side) and on
the CRA↔AI_Act COMPLEMENTARY pair **with the CRA Art. 13(4) sentence 2
OJ-level consolidation rule** (a unified AI Act Art. 9 risk-management
system substitutes for the CRA Art. 13(3) cybersecurity risk
assessment when both apply to the same product — per SR-CRA-066
ambiguity_notes). For a 5-FTE SaaS startup with CRA applicability only
(no GDPR / NIS 2 / DORA / AI Act applicability), only the CRA sub-SO
activates on the product-side pre-market + support-period cybersecurity
risk assessment. For a NIS 2 essential entity that is not a
controller, not a financial entity, and does not manufacture CRA-
classified products (NIS 2 only), only the NIS 2 sub-SO activates and
the high-level SO does not engage (single-reg mode). For a CRA
manufacturer of a high-risk AI system (no controller, no NIS 2, no
DORA), the CRA + AI Act sub-SOs activate and **the CRA Art. 13(4)
sentence 2 unification rule applies** — a unified AI Act Art. 9
risk-management system discharges both CRA Art. 13(3) cybersecurity
risk assessment and AI Act Art. 9 risk management on a single
artefact. The five assessment regimes are stacked, not collapsed:
pre-launch DPIA on data-subject rights (GDPR); continuous operational
risk-analysis policy on entity operational risk (NIS 2); pre-market +
support-period cybersecurity risk assessment on product cybersecurity
risk (CRA); continuous + at-least-yearly ICT risk framework on
financial-entity ICT operational risk (DORA); continuous iterative
risk-management system on AI-system risk (AI Act). The high-level SO
surfaces the common documented-assessment duty (documented assessment +
identified risks + mitigation measures + review cadence + per-reg-
object preservation) but does **NOT** collapse the per-reg assessment
object, trigger, content template, threshold, recipient, or review
cadence. **The single OJ-level cross-regulation consolidation rule**
(CRA Art. 13(4) sentence 2 — CRA ↔ AI Act) is a Phase 1C Doc 07
harmonisation item — for AI-enabled CRA-regulated products, the
unified AI Act Art. 9 risk-management system discharges both
obligations on a single artefact.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **5 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA, AI Act —
  all five participate on the assessment object): GDPR (Art. 35(1)
  pre-launch DPIA on data-subject rights + Art. 35(7) 4-item content +
  Art. 35(11) on-change review); NIS 2 (Art. 21(2)(a) continuous
  operational risk-analysis policy + SR-NIS2-028 Art. 21(1) state-of-
  the-art + cost factor + Art. 22(1) Cooperation Group coordinated
  supply-chain assessments); CRA (Art. 13(3) sentence 1 `documented and
  updated` + sentence 2 `intended purpose and reasonably foreseeable
  use` + sentence 3 `Annex I Part I (2) applicability mapping` + Annex
  VII §3 risk-assessment record); DORA (Art. 6(4) three-lines-of-
  defence + Art. 7(2) sentence 1 `continuously … identify all sources
  of ICT risk` + sentence 2 `review on a regular basis, and at least
  yearly, the risk scenarios`); AI Act (Art. 9(1) `established,
  implemented, documented and maintained` + Art. 9(2) 4-step process
  + Art. 27 FRIA for certain Annex III categories).
- **10 pairwise cells, verified by CRDA-deep**:
  GDPR↔NIS2 (SAME — DIFFERENT-PERSPECTIVE — pre-launch DPIA on data-
  subject rights vs continuous operational risk-analysis on entity
  operational risk — Conditional-Y scope overlap when DPIA conducted
  for NSIE's processing);
  GDPR↔CRA (SAME — DIFFERENT-PERSPECTIVE — pre-launch DPIA on data-
  subject rights vs pre-market + support-period cybersecurity risk
  assessment on product cybersecurity risk — **no OJ-level
  consolidation** even when CRA risk assessment performed, GDPR DPIA
  must be a separate artefact);
  GDPR↔DORA (SAME — DIFFERENT-PERSPECTIVE — pre-launch DPIA on data-
  subject rights vs continuous + at-least-yearly ICT risk framework on
  financial-entity ICT operational risk — **no OJ-level
  consolidation**);
  GDPR↔AI_Act (SAME — DIFFERENT-PERSPECTIVE — pre-launch DPIA on data-
  subject rights vs continuous iterative risk-management system on AI-
  system risk — AI Act Recital 78 explicit GDPR preservation;
  **no OJ-level consolidation**);
  NIS2↔CRA (SAME — COMPLEMENTARY — entity-level operational + product-
  level pre-market; meet at supplier-customer interface; CRA risk
  assessment is an input to NIS 2 entity's supplier-risk register);
  NIS2↔DORA (SAME — EQUAL — both regulations impose continuous
  operational risk-identification obligations; DORA-dominant for
  financial entities under DORA's direct scope; EQUAL on continuous
  operational risk identification);
  NIS2↔AI_Act (SAME — COMPLEMENTARY — NIS 2 entity-level operational
  + AI Act AI-system-level continuous iterative; AI Act layer adds
  the AI-specific 4-step process to the NIS 2 risk-analysis policy);
  CRA↔DORA (SAME — COMPLEMENTARY — CRA product-level pre-market +
  support-period + DORA entity-level operational; Conditional-Y scope
  overlap when DORA entity procures CRA-conformant);
  CRA↔AI_Act (SAME — COMPLEMENTARY — **CRITICAL CONSOLIDATION RULE**:
  CRA Art. 13(4) sentence 2 explicitly permits the AI Act Art. 9 risk-
  management system to substitute for the CRA cybersecurity risk
  assessment when both apply to the same product — per SR-CRA-066
  ambiguity_notes: `For AI-enabled products that are both CRA-
  regulated and AI-Act high-risk, the AI Act Art. 9 risk-management
  system can be the CRA cybersecurity risk assessment artefact (part
  of, or combined with). The two regimes co-discharge on a single
  artefact when both apply to the same product.` **The only OJ-level
  cross-regulation consolidation rule in D-09.2**);
  DORA↔AI_Act (SAME — COMPLEMENTARY — DORA entity-level operational +
  AI Act AI-system-level continuous iterative; **no OJ-level
  consolidation** — DORA has no equivalent to CRA Art. 13(4) sentence
  2).
- The five participating regulations impose **distinct assessment
  regimes** at **distinct assessment *objects*** with **distinct
  triggers + content templates + cadences + recipients**:
  GDPR pre-launch DPIA on data-subject rights + 4-item Art. 35(7) content
  + Art. 35(11) on-change review;
  NIS 2 continuous operational risk-analysis policy (entity-
  discretionary under Recital 56 + Art. 21(1) chapeau + state-of-the-
  art floor) — no codified content; all-hazards methodology per SR-
  NIS2-040;
  CRA pre-market + support-period cybersecurity risk assessment on
  product cybersecurity risk with Annex VII §3 risk-assessment record
  — **subject to CRA Art. 13(4) sentence 2 consolidation rule with AI
  Act Art. 9**;
  DORA continuous + at-least-yearly ICT risk framework on financial-
  entity ICT operational risk — three-lines-of-defence +
  ICT-supported-business-functions / information-assets / ICT-assets
  identified, classified, adequately documented per Art. 7(1);
  AI Act continuous iterative risk-management system on AI-system risk
  with 4-step Art. 9(2) closed list (a)-(d) — cross-coupled with Art.
  27 FRIA for certain Annex III categories.
  The 5 cadences are not synchronised (pre-launch / continuous /
  pre-market + support-period + on-material-change / continuous +
  yearly / continuous iterative); no OJ-level cadence harmonisation
  exists — an entity must satisfy 5 independent review triggers without
  a unified cadence.
- The high-level SO describes the **COMMON OBJECTIVE** (documented
  assessment + identified risks + mitigation measures + review cadence
  + per-reg-object preservation); the **per-regulation perspective**
  (assessment object, trigger, content template, threshold, recipient,
  review cadence, evidence template) is preserved verbatim in the
  five sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the assessment-object dimension
  itself**, because no pair was verified as CONTRADICTORY or CORRECTED
  (all 10 pairs are SAME — 4 SAME — DIFFERENT-PERSPECTIVE + 5 SAME —
  COMPLEMENTARY + 1 SAME — EQUAL with no scope-disjoint structure).
  Phase 1C Doc 07 does not need to resolve an assessment-object
  contradiction because none exist by construction; **however**,
  Phase 1C Doc 07 must (1) **operationalise the single OJ-level cross-
  regulation consolidation rule** (CRA Art. 13(4) sentence 2 — for AI-
  enabled CRA-regulated products, a unified AI Act Art. 9 risk-
  management system substitutes for the CRA Art. 13(3) cybersecurity
  risk assessment when both apply to the same product); and (2)
  perform the **Layer 1 cross-cutting assessment-objects mapping** to
  identify the 5 distinct assessment *objects* and to align the 5
  distinct review cadences without a unified OJ-level cadence. CRDA-
  flagged "Five overlapping risk/impact assessments with only one
  consolidation rule" (DomainAnalysis §D-09.2 line 173) is itself a
  Layer 1 cross-cutting assessment-objects mapping item, not an
  emergent tension requiring Phase 1C resolution on the assessment-
  object dimension itself.
- **Scope caveat (CRITICAL — single OJ-level cross-regulation
  consolidation rule)** — derived from CRDA-deep verified
  classifications (DomainAnalysis §D-09.2 lines 173, 175; DeepAnalysis
  §CRA ↔ AI Act pair line 29): the ONLY OJ-level cross-regulation
  consolidation rule in D-09.2 is **CRA Art. 13(4) sentence 2**: `The
  cybersecurity risk assessment referred to in paragraph 2 shall be
  part of, or combined with, the risk assessment required by other
  Union legal acts applicable to the product with digital elements.`
  For AI-enabled CRA-regulated products (the SAME product is both CRA-
  regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-
  management system substitutes for the CRA Art. 13(3) cybersecurity
  risk assessment (per SR-CRA-066 ambiguity_notes). Phase 1 entities
  can satisfy both obligations with a single artefact. **No other
  cross-regulation substitution is OJ-permitted** at D-09.2 — the GDPR
  DPIA, NIS 2 risk-analysis policy, DORA ICT risk framework, and CRA
  risk assessment (when not subject to Art. 13(4) sentence 2
  consolidation) are all distinct artefacts with no OJ-level
  substitution rule.
- **Scope caveat (CRITICAL — pre-launch vs operational asymmetry)** —
  derived from CRDA-deep verified classifications: GDPR DPIA is pre-
  launch (high-risk-processing trigger + on-change review); NIS 2 risk
  analysis is continuous; CRA risk assessment is pre-market + support-
  period; DORA risk framework is continuous + yearly review; AI Act
  risk management is continuous iterative across lifecycle. The review
  cadences are not synchronised (per DomainAnalysis §D-09.2 line 174).
  An entity must satisfy 5 independent review triggers without a
  unified cadence. Phase 1 entities must implement 5 distinct review
  triggers without a unified cadence — the Layer 1 cross-cutting
  mapping identifies when a single calendar event triggers ≥2 review
  cycles (e.g., material change of a CRA-regulated product may trigger
  CRA on-material-change review + AI Act Art. 9 iterative review + GDPR
  Art. 35(11) on-change review + DORA Art. 7(2) sentence 2 yearly
  review).
- **Scope caveat (CRITICAL — GDPR DPIA does NOT address cybersecurity
  risk)** — derived from CRDA-deep verified classifications
  (DomainAnalysis §D-09.2 line 175): GDPR Art. 35(7) covers risks to
  data-subject rights and freedoms; it does not require cybersecurity-
  risk analysis. The CRA risk assessment covers cybersecurity risks; the
  NIS 2 / DORA risk frameworks cover operational ICT risks; the AI Act
  covers AI-system risks. None of the four non-GDPR assessments
  substitute for GDPR DPIA. For a CRA-regulated product processing
  personal data, the GDPR DPIA must be a separate artefact even when
  the CRA risk assessment has been performed. Per CRDA flag: `GDPR DPIA
  does not address cybersecurity risk` — `for a CRA-regulated product
  processing personal data, the GDPR DPIA must be a separate artefact
  even when the CRA risk assessment has been performed`.
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA EQUAL classification on
  continuous operational risk identification)** — derived from CRDA-
  deep verified classifications (DeepAnalysis §NIS2 ↔ DORA pair lines
  274-279; DomainAnalysis §NIS 2 ↔ DORA lines 110-114): both
  regulations impose continuous operational risk-identification
  obligations. NIS 2: Art. 21(2)(a) `policies on risk analysis and
  information system security` (entity-discretionary under Recital 56
  proportionality + state-of-the-art floor per Art. 21(1)). DORA:
  Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1
  `continuously … identify all sources of ICT risk` + sentence 2
  `review on a regular basis, and at least yearly, the risk scenarios`.
  DORA's three-lines-of-defence + continuous + at-least-yearly
  discharge both DORA's dedicated risk-analysis obligations and NIS
  2's Art. 21(2)(a) policy artefacts for DORA financial entities under
  DORA's direct scope. For non-financial NSIEs, NIS 2 is the authority.
  The EQUAL classification preserves the OJ literal parallel between
  the two regimes on the continuous operational risk-identification
  dimension; the dominant-authority reading is the operational
  consequence of the DORA-direct-applicability vs NIS 2-MS-
  transposition asymmetry.
---

## Emergent tensions (from CRDA-deep §D-09.2)

#### Emergent tensions (from CRDA-deep §D-09.2)
**0 conditional emergent tensions** on the impact-and-risk-assessment duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 10 pairs are all SAME — 4 SAME — DIFFERENT-PERSPECTIVE (all 4 GDPR pairs) + 5 SAME — COMPLEMENTARY + 1 SAME — EQUAL (NIS 2 ↔ DORA on continuous operational risk identification). **No scope-disjoint pairs** at D-09.2 — every pair activates at the Y or Conditional-Y-on-same-party level. **No SCOPE-DISJOINT reclassifications** — CRDA preserves every pair as SAME — DIFFERENT-PERSPECTIVE / COMPLEMENTARY / EQUAL. **No CONTRADICTORY pairs** on the assessment-object dimension itself. The **assessment-object divergence** (data-subject rights / entity operational risk / product cybersecurity risk / ICT operational risk / AI-system risk) is the **legitimately diverse dimension**: each regulator operates on a distinct assessment object with a distinct trigger and lifecycle phase, and the operational convergence is on a **layered 5-assessment architecture** with 5 distinct cadences — pre-launch DPIA / continuous operational / pre-market + support-period / continuous + at-least-yearly / continuous iterative across AI lifecycle. The high-level SO surfaces the common documented-assessment duty (documented assessment + identified risks + mitigation measures + review cadence + per-reg-object preservation); the per-reg assessment object, trigger, content template, threshold, recipient, and review cadence are documented separately in the 5 sub-SOs and the per-recipient evidence packs.
The **single OJ-level cross-regulation consolidation rule** (CRA Art. 13(4) sentence 2 unification) is the structurally significant operational harmonisation — the ONLY cross-regulation substitution rule at D-09.2: for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes). **No other cross-regulation substitution is OJ-permitted** — the GDPR DPIA, NIS 2 risk-analysis policy, DORA ICT risk framework, and CRA risk assessment (when not subject to Art. 13(4) sentence 2 consolidation) are all distinct artefacts with no OJ-level substitution rule. The 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) reflect the structural pre-launch DPIA vs continuous / iterative assessment asymmetry; **CRDA flag — GDPR DPIA does NOT address cybersecurity risk** (DomainAnalysis §D-09.2 line 175) — `GDPR Art. 35(7) covers risks to data-subject rights and freedoms; it does not require cybersecurity-risk analysis; for a CRA-regulated product processing personal data, the GDPR DPIA must be a separate artefact even when the CRA risk assessment has been performed`. The 5 cadences are not synchronised and no OJ-level cadence harmonisation exists (DomainAnalysis §D-09.2 line 174 — pre-launch vs operational review asymmetry).
The **NIS 2 ↔ DORA EQUAL classification on continuous operational risk identification** is the structurally significant EQUAL pair: both regulations impose continuous operational risk-identification obligations. NIS 2 Art. 21(2)(a) `policies on risk analysis and information system security` is entity-discretionary under Recital 56 proportionality + state-of-the-art floor per Art. 21(1). DORA Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios` is the dedicated financial-entity operational framework. For DORA financial entities under DORA's direct scope, the DORA Art. 6(4) + Art. 7(2) sentence 1 + sentence 2 discharges both DORA's dedicated risk-analysis obligations and NIS 2's Art. 21(2)(a) policy artefacts for DORA financial entities. For non-financial NSIEs, NIS 2 is the authority. The EQUAL classification preserves the OJ literal parallel between the two regimes on the continuous operational risk-identification dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry. **NOTE — DORA OJ-literal locus**: the OJ-literal locus for Art. 7(2) sentence 1 + sentence 2 is Art. 8(2) per the SR-DORA-004 / SR-DORA-005 v0.2 audit note; the SR preserves the substantive content.
The high-level SO surfaces the common risk-assessment duty (documented assessment + identified risks + mitigation measures + review cadence + per-reg-object preservation); the per-reg perspective on the assessment object, trigger, content template, threshold, recipient, review cadence, and evidence template is documented separately in the 5 sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the layered 5-assessment architecture (data-subject rights / entity operational risk / product cybersecurity risk / ICT operational risk / AI-system risk) with 5 distinct assessment triggers and review cadences is itself the layered reconciliation that supersedes any single-regulator reading. **1 OJ-level cross-regulation consolidation rule** (CRA Art. 13(4) sentence 2) operationalises the AI-enabled-CRA-regulated-product harmonisation on a single artefact.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-09.2 — with overlapping assessment-architecture scope-determiners on the same party — operates a **layered 5-assessment architecture** with 5 distinct assessment objects, 5 distinct triggers, 5 distinct content templates, 5 distinct review cadences, 5 distinct recipients. The high-level SO (`SO-D-09.2.HL`) describes the common documented-assessment duty (documented assessment + identified risks + mitigation measures + review cadence + per-reg-object preservation); the per-reg perspective is preserved in the 5 sub-SOs (assessment object, trigger, content template, threshold, recipient, review cadence, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 5-assessment architecture operationalising the 5 distinct assessment triggers and review cadences without a unified OJ-level cadence. The high-level SO does NOT collapse the 5 assessment regimes into a single artefact; the per-reg perspective on the assessment object, trigger, content template, threshold, recipient, review cadence, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **impact-and-risk-assessment strategy**: (1) a 5-layer assessment architecture with explicit assessment-object hand-offs (GDPR Art. 35(1) + Art. 35(7) + Art. 35(11) pre-launch DPIA on data-subject rights → NIS 2 Art. 21(2)(a) + SR-NIS2-028 + Art. 22(1) continuous operational risk-analysis policy on entity operational risk → CRA Art. 13(3) sentence 1 + sentence 2 + sentence 3 + Annex VII §3 pre-market + support-period cybersecurity risk assessment on product cybersecurity risk → DORA Art. 6(4) + Art. 7(2) sentence 1 + sentence 2 continuous + at-least-yearly ICT risk framework on financial-entity ICT operational risk → AI Act Art. 9(1) + Art. 9(2)(a)-(d) + Art. 27 FRIA continuous iterative risk-management system on AI-system risk); (2) the single OJ-level cross-regulation consolidation rule (CRA Art. 13(4) sentence 2 — for AI-enabled CRA-regulated products, a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment) is a Phase 1C Doc 07 harmonisation item — for AI-enabled CRA-regulated products, the unified AI Act Art. 9 risk-management system discharges both obligations on a single artefact; (3) the Layer 1 cross-cutting assessment-objects mapping identifies the 5 distinct assessment *objects* (data-subject rights / entity operational risk / product cybersecurity risk / ICT operational risk / AI-system risk) and aligns the 5 distinct review cadences (pre-launch + on-change review / continuous / pre-market + support-period + on-material-change / continuous + at-least-yearly / continuous iterative across AI lifecycle) without a unified OJ-level cadence; (4) the GDPR DPIA on data-subject rights must be a separate artefact even when the CRA risk assessment / NIS 2 risk-analysis policy / DORA ICT risk framework / AI Act Art. 9 risk-management system is in place — the CRDA DomainAnalysis flag (`GDPR DPIA does not address cybersecurity risk`) is the operational interpretation; (5) the NIS 2 ↔ DORA EQUAL classification on continuous operational risk identification discharges both obligations on the DORA-dominant stack for financial entities under DORA's direct scope — for non-financial NSIEs, NIS 2 is the authority; (6) the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) reflect the structural pre-launch DPIA vs continuous / iterative assessment asymmetry — the **CRITICAL CRDA DomainAnalysis flag** (line 173) `Five overlapping risk/impact assessments with only one consolidation rule: GDPR DPIA (Art. 35), NIS 2 risk analysis (Art. 21(2)(a) + Art. 22), CRA cybersecurity risk assessment (Art. 13(3) + Annex VII §3), DORA ICT risk framework (Art. 6/7), AI Act FRIA-equivalent (Art. 9) — five separate assessment regimes that may all apply to the same entity-product combination. The ONLY OJ-level consolidation rule is CRA Art. 13(4) sentence 2 (AI Act Art. 9 risk management substitutes for CRA risk assessment). No other cross-regulation consolidation exists. Phase 1 entities must maintain five separate risk registers with no OJ-level cross-referencing. **Recommend Layer 1 cross-cutting analysis** to map the five assessment objects` is the Layer 1 mapping basis. The high-level SO does NOT resolve any assessment-object contradiction because none exist by construction (10 SAME — 4 DIFFERENT-PERSPECTIVE + 5 COMPLEMENTARY + 1 EQUAL); the Layer 1 cross-cutting assessment-objects mapping is the operational mechanism for nesting the 5 assessment regimes in a single integrated assessment architecture, and the single OJ-level cross-regulation consolidation rule (CRA Art. 13(4) sentence 2) is the operational mechanism for unifying the CRA ↔ AI Act assessments on a single artefact when both apply to the same product.
---
**Document version:** 0.1 — initial derivation from CRDA-deep §D-09.2 (10 pairs verified + 1 OJ-level consolidation rule).
**See also:** [`D-09.1.md`](D-09.1.md) (Information Security Policies — same 5-reg participation + no OJ-level consolidation rule); [`index.md`](../index.md); [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.2.md) (CRDA-deep source).

## Part 1 §3 — context

### 3. Security Requirements
## 9.2 Impact & Risk Assessments — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md`. See that file for the CRDA-deep verified classification (10 pairs: 4 SAME — DIFFERENT-PERSPECTIVE + 5 SAME — COMPLEMENTARY + 1 SAME — EQUAL — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs; **5 of 5 regulations participate**; **1 OJ-level cross-regulation consolidation rule** — CRA Art. 13(4) sentence 2 permitting AI Act Art. 9 risk management to substitute for CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product), the 5 distinct assessment objects (data-subject rights / entity operational / product cybersecurity / ICT operational / AI-system), the 5 distinct review cadences (pre-launch on-change / continuous / pre-market + support-period / continuous + yearly / continuous iterative), the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs reflecting pre-launch DPIA vs operational-continuous asymmetry with **no OJ-level consolidation** — GDPR DPIA must be a separate artefact even when CRA risk assessment has been performed per DomainAnalysis §9.2 line 175 CRDA flag: "GDPR DPIA does NOT address cybersecurity risk"), the NIS 2 ↔ DORA EQUAL on continuous operational risk identification (DORA-dominant for financial entities), the CRA ↔ AI_Act consolidation rule (CRA Art. 13(4) sentence 2 — the only OJ-permitted substitution in 9.2), the per-reg assessment object / trigger / content template / threshold / recipient / review cadence / legal anchor, and the aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA, AI Act (ALL 5 — no scope-disjoint pair at 9.2, hence the only sub-domain where the HL engages whenever ≥2 regs are applicable; CRDA flag: "Five overlapping risk/impact assessments with only one consolidation rule"). Each regulator imposes a **distinct assessment regime** at a **distinct assessment object** under a **distinct trigger** at a **distinct lifecycle phase** with a **distinct review cadence**: GDPR (Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` + Art. 35(7) 4-item content + Art. 35(11) `review on change of risk`) — pre-launch DPIA on data-subject rights; NIS 2 (Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor per Art. 21(1) sentence 2 + Recital 56 cost factor + Art. 22(1) Cooperation Group coordinated assessments) — continuous operational risk-analysis policy on entity operational risk; CRA (Art. 13(3) sentence 1 `documented and updated` + sentence 2 `intended purpose and reasonably foreseeable use` + sentence 3 Annex I Part I (2) applicability mapping + Annex VII §3 risk-assessment record) — pre-market + support-period cybersecurity risk assessment on product cybersecurity risk; DORA (Art. 6(4) `three lines of defence model` + Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk` + sentence 2 `review on a regular basis, and at least yearly, the risk scenarios`) — continuous + at-least-yearly ICT risk framework on financial-entity ICT operational risk; AI Act (Art. 9(1) `established, implemented, documented and maintained` + Art. 9(2)(a)-(d) 4-step process + Art. 27 FRIA for certain Annex III categories) — continuous iterative risk-management system on AI-system risk.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 9.2
  volere_section: 15
  volere_subtype: integrity
  title: "Impact and risk assessments are established through a documented assessment of identified risks and mitigation measures with a review cadence calibrated to the lifecycle phase of the assessment object"
  derives_from:
    hso_sub_so: SO-9.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.2.md
    objective_ref_section: "### 9.2.0"
  description: |
    The product shall establish impact and risk assessments through documented assessments of identified risks and mitigation measures with a review cadence calibrated to the lifecycle phase of the assessment object, where ≥2 of the participating regulations (GDPR, NIS 2, CRA, DORA, AI Act) have applicability with overlapping assessment-architecture scope-determiners on the same party, with the 5 distinct per-reg assessment objects, triggers, content templates, thresholds, recipients, and review cadences preserved verbatim in the 5 sub-SOs, and with the CRA Art. 13(4) sentence 2 OJ-level consolidation rule permitting AI Act Art. 9 risk management to substitute for CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product.
  fit_criterion: |
    A documented impact-and-risk-assessment architecture is established covering all 5 participating assessment regimes (or the subset applicable to the entity) at the assessment-evidence layer: (1) GDPR pre-launch DPIA per Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` with the 4-item Art. 35(7) content (systematic description of processing + necessity/proportionality + risks to data-subject rights + measures envisaged to address risks) reviewed on change of risk per Art. 35(11) and submitted for prior consultation where residual risk is high per Art. 36(1), submitted to DPA on demand under Art. 5(2) accountability; (2) NIS 2 continuous operational risk-analysis policy per Art. 21(2)(a) `policies on risk analysis and information system security` with all-hazards methodology per SR-NIS2-040, calibrated by Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art floor + Recital 56 cost factor, incorporating Art. 22(1) Cooperation Group coordinated supply-chain assessments per Art. 21(3) sentence 2, management-body-approved per Art. 20(1); (3) CRA pre-market + support-period cybersecurity risk assessment per Art. 13(3) sentence 1 `documented and updated` covering intended purpose + reasonably foreseeable use per sentence 2 + Annex I Part I (2) applicability mapping per sentence 3, documented in Annex VII §3 risk-assessment record, updated on material change of risk or upon becoming aware of a previously unidentified vulnerability per Art. 13(7), with Art. 27 presumption-of-conformity machinery for harmonised-standards-aligned assessments; (4) DORA continuous ICT risk identification register per Art. 7(2) sentence 1 + at-least-yearly risk-scenario review per sentence 2, under three-lines-of-defence per Art. 6(4), with proportionality calibrated to Art. 4 `size, nature, scale and complexity`; (5) AI Act continuous iterative risk-management system per Art. 9(1) `established, implemented, documented and maintained` with the 4-step Art. 9(2)(a)-(d) process documented and integrated with Art. 27 FRIA for certain Annex III categories; the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) discharge the GDPR DPIA as a **separate artefact** even when CRA / DORA / NIS 2 / AI Act assessments are in place (per DomainAnalysis §9.2 line 175 CRDA flag — GDPR DPIA does NOT address cybersecurity risk), the NIS 2 ↔ DORA EQUAL pair discharges both obligations on the DORA-dominant stack for financial entities, and the CRA Art. 13(4) sentence 2 unification rule discharges CRA Art. 13(3) cybersecurity risk assessment on a unified AI Act Art. 9 risk-management system artefact for AI-enabled CRA-regulated products (per SR-CRA-066 ambiguity_notes — the ONLY OJ-level cross-regulation consolidation rule in 9.2).
  priority: MUST
  verification_method: TEST
  dependencies: [9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5]
  nist_csf: [ID.RA-01, ID.RA-04, ID.RA-05]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: Y   # HL engages whenever ≥2 applicable regs have ≥1 Y or Conditional-Y-scope-overlap pair on the same party; for 9.2 the matrix shows every pair has Y or Conditional-Y activation on the joint-condition operator (no N (typically) scope-disjoint pairs); the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) reflect the structural pre-launch DPIA vs continuous / iterative assessment asymmetry and stack on the layered 5-assessment architecture; the 5 SAME — COMPLEMENTARY pairs stack on distinct assessment *objects* with no consolidation rule (except the CRA↔AI_Act pair which has the CRA Art. 13(4) sentence 2 OJ-level consolidation rule permitting substitution); the 1 SAME — EQUAL pair (NIS 2 ↔ DORA) discharges both obligations on the DORA-dominant stack for financial entities
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The high-level SO surfaces the **common documented-assessment duty** (documented assessment + identified risks + mitigation measures + review cadence) converging across GDPR Art. 35(1) + Art. 35(7) + Art. 35(11) + NIS 2 Art. 21(2)(a) + Art. 22(1) + CRA Art. 13(3) sentence 1-3 + Art. 13(7) + Annex VII §3 + DORA Art. 6(4) + Art. 7(2) sentence 1 + sentence 2 + AI Act Art. 9(1) + Art. 9(2)(a)-(d) + Art. 27 FRIA; the **per-reg assessment object, trigger, content template, threshold, recipient, and review cadence** are preserved verbatim in the 5 sub-SOs. The 10 verified pairs are all SAME — 4 SAME — DIFFERENT-PERSPECTIVE + 5 SAME — COMPLEMENTARY + 1 SAME — EQUAL — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs. **CRDA flag — GDPR DPIA does NOT address cybersecurity risk** (DomainAnalysis §9.2 line 175): for CRA-regulated products processing personal data, the GDPR DPIA must be a separate artefact even when the CRA cybersecurity risk assessment has been performed; the 4 SAME — DIFFERENT-PERSPECTIVE pairs (all 4 GDPR pairs) reflect this structural pre-launch DPIA vs operational-continuous asymmetry. The **single OJ-level cross-regulation consolidation rule** — CRA Art. 13(4) sentence 2: `The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements` — permits the AI Act Art. 9 risk-management system to substitute for the CRA Art. 13(3) cybersecurity risk assessment when both apply to the same product (per SR-CRA-066 ambiguity_notes); no other cross-regulation substitution is OJ-permitted at 9.2. The 5 cadences are not synchronised (pre-launch / continuous / pre-market + support-period / continuous + yearly / continuous iterative); an entity must satisfy 5 independent review triggers without a unified OJ-level cadence. The **NIS 2 ↔ DORA EQUAL pair** discharges both continuous operational risk-identification obligations on the DORA-dominant stack for financial entities under DORA's direct scope. **Most heavily-overlapped sub-domain** with **1 OJ-level consolidation rule + 0 emergent tensions**. Phase 1 entities must build a **layered 5-assessment architecture** with 5 distinct assessment objects + 5 distinct triggers + 5 distinct cadences; the HL does NOT collapse the per-reg assessment regime into a single artefact. **Step Reference:** HL requirement is decomposed into 5 per-reg sub-requirements (one per participating regulation) below; each sub-requirement carries its own derivation, fit_criterion, and applicable_if. The 5 assessment regimes operate on distinct assessment *objects* at distinct lifecycle phases; the per-reg assessment object, trigger, content template, threshold, recipient, review cadence, and evidence template are preserved verbatim in the 5 sub-SOs.
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-09.2
title: D-09.2 Impact & Risk Assessments — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.2 Impact & Risk Assessments
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---
> **Deep analysis:** [D-09.2 Impact & Risk Assessments](../../DeepAnalysis/D-09_Governance-Documentation/D-09.2.md)
#### D-09.2 Impact & Risk Assessments
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
> **CRITICAL FOR D-09.2.** All 5 regulations overlap. Each imposes a distinct risk/impact assessment regime from a different angle: GDPR DPIA (Art. 35), NIS 2 risk analysis (Art. 21(2)(a) + Art. 22 coordinated assessments), CRA cybersecurity risk assessment (Art. 13(3) + Annex VII §3), DORA ICT risk framework (Art. 6/7), AI Act FRIA (Art. 9). The assessments are NOT cross-referenced at the OJ level — each is a separate artefact with distinct triggers, content, and review cadences.
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-028 + SO-GDPR-036 | DPIA covering Art. 35(7) four content items (systematic description, necessity/proportionality, risks, mitigation); joint-controller arrangement (Art. 35, Art. 26). | Personal-data-rights impact; pre-launch for high-risk processing; reviewed on risk change. |
| NIS2 | SO-NIS2-022 + SO-NIS2-016 + SR-NIS2-028 (Art. 21(1)) | Policies on risk analysis + EU-level coordinated supply-chain risk assessments via Art. 22(1). | Entity-level operational risk analysis (Art. 21); EU-level coordinated assessments (Art. 22); no pre-launch DPIA. |
| CRA | SO-CRA-053 + SO-CRA-054 | Cybersecurity risk assessment documented + updated during support period; covers intended purpose + reasonably foreseeable use; maps Annex I Part I (2) applicability. | Product-level pre-market risk assessment; documented in Annex VII §3; reviewed on material change. |
| DORA | SO-DORA-017 (Art. 6(4) three-lines-of-defence) + SO-DORA-003 (Art. 7(2) continuous + yearly review) | ICT risk management framework with three-lines-of-defence + continuous ICT risk identification + yearly review of risk scenarios. | Financial-entity operational ICT risk framework; no pre-launch DPIA-equivalent. |
| AI_Act | SO-AIACT-001 | Continuous, iterative risk management system across AI lifecycle with 4-step process (identify/analyse known+foreseeable risks; estimate/evaluate misuse risks; evaluate post-market risks; adopt targeted measures). | AI-system pre-market + post-market risk management system; Art. 9 risk management as the FRIA-equivalent. |
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
- **CRITICAL: Five overlapping risk/impact assessments with only one consolidation rule**: GDPR DPIA (Art. 35), NIS 2 risk analysis (Art. 21(2)(a) + Art. 22), CRA cybersecurity risk assessment (Art. 13(3) + Annex VII §3), DORA ICT risk framework (Art. 6/7), AI Act FRIA-equivalent (Art. 9) — five separate assessment regimes that may all apply to the same entity-product combination. The ONLY OJ-level consolidation rule is CRA Art. 13(4) sentence 2 (AI Act Art. 9 risk management substitutes for CRA risk assessment). No other cross-regulation consolidation exists. Phase 1 entities must maintain five separate risk registers with no OJ-level cross-referencing. **Recommend Layer 1 cross-cutting analysis** to map the five assessment objects (data-subject rights, entity operational risk, product cybersecurity risk, ICT operational risk, AI-system risk) to a unified register.
- **Pre-launch vs. operational review asymmetry**: GDPR DPIA is pre-launch (reviewed on change of risk); NIS 2 risk analysis is continuous; CRA risk assessment is pre-market + support-period; DORA risk framework is continuous + yearly review; AI Act risk management is continuous iterative across lifecycle. The review cadences are not synchronised. An entity must satisfy five independent review triggers without a unified cadence.
- **GDPR DPIA does not address cybersecurity risk**: GDPR Art. 35(7) covers risks to data-subject rights and freedoms; it does not require cybersecurity-risk analysis. The CRA risk assessment covers cybersecurity risks; the NIS 2 / DORA risk frameworks cover operational ICT risks; the AI Act covers AI-system risks. None of the four non-GDPR assessments substitute for GDPR DPIA. For a CRA-regulated product processing personal data, the GDPR DPIA must be a separate artefact even when the CRA risk assessment has been performed.
<!-- /emergent -->
##### SR cross-validation
All 5 regulations map D-09.2 to the NIST CSF 2.0 Subcategory **ID.RA-05** (Threats, vulnerabilities, likelihoods, impacts used to understand inherent risk and inform risk response) as the convergent anchor. GDPR additionally maps **ID.RA-04** (Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded) for the DPIA-specific impact-and-likelihood dimension; AI Act additionally maps **GV.RM-04** (Strategic direction for risk response) for the continuous-iterative dimension; CRA additionally maps **GV.SC-07** (Suppliers prioritised by criticality) for the supply-chain risk dimension.
##### Downstream implication
D-09.2 is the most heavily-overlapped sub-domain. Phase 1 entities must implement five distinct assessment artefacts with no OJ-level consolidation. The Layer 1 cross-cutting analysis is required to map the five assessment objects. For DORA financial entities deploying high-risk AI products processing personal data, all five assessments apply simultaneously. The CRA Art. 13(4) sentence 2 AI-Act-substitution rule is the only OJ-level consolidation available.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-09.2
title: D-09.2 Impact & Risk Assessments — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.2 Impact & Risk Assessments
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-09_Governance-Documentation/D-09.2.md
status: DRAFT
---
> **Domain analysis:** [D-09.2 Impact & Risk Assessments](../../DomainAnalysis/D-09_Governance-Documentation/D-09.2.md)
#### D-09.2 Impact & Risk Assessments
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Critical note (CRDA flag):** D-09.2 is the most heavily-overlapped sub-domain. All 5 regulations overlap with distinct risk/impact assessment regimes from different angles: GDPR DPIA (Art. 35), NIS 2 risk analysis (Art. 21(2)(a) + Art. 22), CRA cybersecurity risk assessment (Art. 13(3) + Annex VII §3), DORA ICT risk framework (Art. 6/7), AI Act FRIA (Art. 9). The assessments are NOT cross-referenced at the OJ level — each is a separate artefact with distinct triggers, content, and review cadences. The ONLY OJ-level consolidation rule is CRA Art. 13(4) sentence 2 (AI Act Art. 9 risk management substitutes for CRA risk assessment).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
