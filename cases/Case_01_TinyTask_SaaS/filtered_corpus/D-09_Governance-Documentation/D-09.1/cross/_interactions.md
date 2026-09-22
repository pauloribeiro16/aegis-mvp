<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-09.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-09.1 Information Security Policies](../../DomainAnalysis/D-09_Governance-Documentation/D-09.1.md)
#### D-09.1 Information Security Policies
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Critical note (CRDA flag):** D-09.1 is the most heavily-overlapped sub-domain. All 5 regulations overlap with distinct policy artefacts and no OJ-level consolidation rule.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-09.1 Information Security Policies
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md)
> (10 pairs verified against OJ text — **5 participating regulations
> are GDPR, NIS 2, CRA, DORA, AI Act; all 5 participate** as noted by
> `DomainAnalysis/D-09_Governance-Documentation/D-09.1.md`
> line 27: "Participants: GDPR, NIS2, CRA, DORA, AI_Act" and lines 168–173:
> "Five-policy-stack with no OJ-level consolidation rule:
> D-09.1 is the most heavily-overlapped sub-domain. GDPR (data-protection
> policy + DPO), NIS 2 (governance + 3 policies), CRA (manufacturer
> policies + presumption of conformity), DORA (ICT risk management
> framework + three-lines-of-defence), AI Act (QMS + transparency).
> All five apply simultaneously to a DORA financial entity that
> processes personal data and ships AI-enabled CRA-regulated products.
> There is no OJ-level consolidation rule.").
>
> **Critical note (CRDA flag).** D-09.1 is the **most heavily-overlapped
> sub-domain** with 5 regulators and 10 verified pairwise relationships —
> no OJ-level consolidation rule applies. **No CORRECTED, no
> CONTRADICTORY** pairs — all 10 pairs are SAME (9 SAME — COMPLEMENTARY
> + 1 SAME — EQUAL). The high-level SO surfaces the **common
> information-security-policy duty** (documented policy architecture +
> governance hooks + accountability chain); the per-reg perspective is
> preserved verbatim in the 5 sub-SOs.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-09.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-026 + SG-GDPR-027 + SG-GDPR-037 | Appropriate data-protection policies reviewed and updated where necessary, with the controller responsibility-accountability chain (Art. 24(1)/(2) + Art. 5(2)) and DPO designation + independence (Art. 37/38/39), securing the controller-side policy architecture. | Process-oriented data-protection policies; DPO as governance anchor; accountability under Art. 5(2). |
| NIS2 | SG-NIS2-021 + SG-NIS2-022 + SG-NIS2-023 | Management body of essential/important entities approves the cybersecurity risk-management measures, oversees their implementation, and can be held liable (Art. 20(1)); policies on risk analysis + IS security (Art. 21(2)(a)) and policies/procedures to assess effectiveness of cybersecurity risk-management measures (Art. 21(2)(f)). | Governance-first with policy artefact; management-body approve/oversee/liable architecture on top of three policy artefacts. |
| CRA | SG-CRA-049 + SG-CRA-050 + SG-CRA-051 + SG-CRA-052 | OSS-steward cybersecurity policy fostering the development of a secure product with digital elements and effective vulnerability handling (Art. 24(1)); OSS-steward cooperation with market surveillance authorities (Art. 24(2)); manufacturer policies/processes/procedures for CRA cybersecurity obligations including CVD policy + secure-update distribution + support-period factors + cessation-of-operations procedure (Art. 13(8) + Annex I Part II §5 + Art. 13(23)); presumption of conformity via harmonised standards / common specifications / CSA certification (Art. 27(1)/(2)/(5)/(8)/(9)). | Product-level policy framework + standards-presumption machinery + OSS-steward cybersecurity policy. |
| DORA | SG-DORA-016 + SG-DORA-017 | Management body defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework (Art. 5(2)), supported by a sound, comprehensive and well-documented framework (Art. 6(1)); ICT risk assigned to a control function with appropriate level of independence according to three lines of defence model + identification/classification/documentation of ICT supported business functions and information/ICT assets (Art. 6(4) + Art. 7(1)). | Financial-entity ICT risk-management framework; three-lines-of-defence + asset identification/classification as governance anchor. |
| AI_Act | SG-AIACT-007 + SG-AIACT-010 | High-risk AI systems are designed and developed so their operation is sufficiently transparent to enable deployers to interpret output and use it appropriately, accompanied by concise, complete, correct and clear instructions for use (Art. 13(1)+(3)); a quality management system documented in a systematic and orderly manner in the form of written policies, procedures and instructions covering at least 13 enumerated aspects including design/design control/design verification and risk-management-system documentation (Art. 17(1)). | AI-system-specific policy carrier via QMS; transparency-to-deployers as policy content. |

## Validated relationships (from CRDA-deep §D-09.1)

#### Validated relationships (from CRDA-deep §D-09.1)
Of 10 pairs, **10 verified as SAME — no CORRECTED, no CONTRADICTORY**. The 10 verified relationships are distributed as **9 SAME — COMPLEMENTARY + 1 SAME — EQUAL (NIS 2 ↔ DORA)**. **The five regulations look at the information-security-policy duty from five distinct regulatory perspectives that stack without consolidation** — the 9 SAME — COMPLEMENTARY pairs (GDPR↔NIS2, GDPR↔CRA, GDPR↔DORA, GDPR↔AI_Act, NIS2↔CRA, NIS2↔AI_Act, CRA↔DORA, CRA↔AI_Act, DORA↔AI_Act) operate on distinct policy artefacts under distinct anchors and stack on the integrated governance architecture; the 1 SAME — EQUAL pair (NIS 2 ↔ DORA) discharges both obligations on the DORA-dominant stack for financial entities. The architecture is **legitimately diverse with no scope-disjoint structure** — the 10 same-direction pairs leave no CONTRADICTORY overlap and the same-different-perspective categorisation does not apply (every pair operates within the policy object, with the perspective diverging only in sub-aspect such as actor / anchor / governance body):
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR mandates the controller-side data-protection policy artefact (Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` + Art. 5(2) `the controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1`); NIS 2 mandates the governance act (management body approves/oversees/liable per Art. 20(1) sentence 1) AND the entity-level risk-analysis + IS-security + effectiveness-assessment policy artefacts (Art. 21(2)(a)+(f)). For entities that are both controllers and NSIEs, NIS 2's governance architecture (approve/oversee/liable) extends to the GDPR policies — the two regimes stack with the NIS 2 management-body approval as the governance hook on top of the GDPR policy artefact. Scope-disjoint test: **Y (when the controller-NSIE adopts data-protection policies subject to management-body approval)**. No reclassification required.
- **GDPR ↔ CRA** — COMPLEMENTARY (SAME): GDPR addresses controller policies for personal-data processing (Art. 24); CRA addresses manufacturer policies for product cybersecurity (Art. 13(8) + Art. 24 OSS-steward policy) + the presumption-of-conformity machinery (Art. 27(1)/(2)/(5)/(8)/(9)). The two policies are different artefacts and can coexist without overlap. For a controller-manufacturer (a vertically-integrated entity that processes personal data AND ships CRA-regulated products), the two regimes apply simultaneously on different policy artefacts — controller policies on the GDPR side and manufacturer policies on the CRA side, with no OJ-level consolidation rule. Scope-disjoint test: **Conditional (Y when the controller is also a manufacturer or OSS steward; N otherwise)**. No reclassification required.
- **GDPR ↔ DORA** — COMPLEMENTARY (SAME): GDPR mandates controller-side data-protection policies (Art. 24) with DPO + accountability (Art. 37-39 + Art. 5(2)); DORA mandates financial-entity management-body define/approve/oversee/implement + a sound/comprehensive/well-documented ICT risk-management framework (Art. 5(2) + Art. 6(1)) + three-lines-of-defence + asset identification (Art. 6(4) + Art. 7(1)) + 5-artefact types (strategies, policies, procedures, ICT protocols and tools per Art. 6(2)). DORA is the dominant authority for financial entities; GDPR policies become a module within the framework. Scope-disjoint test: **Y (when the DORA financial entity is a controller adopting data-protection policies within the framework)**. No reclassification required.
- **GDPR ↔ AI_Act** — COMPLEMENTARY (SAME): GDPR data-protection policies stack with AI Act QMS policies (Art. 17(1) 13-element closed list (a)-(m) `systematic and orderly manner in the form of written policies, procedures and instructions`); AI Act does not displace GDPR for personal-data processing (Recital 78 `protection of natural persons in relation to the processing of personal data by Union institutions, bodies, offices and agencies … is governed by Regulation (EU) 2018/1725` and the broader preservation of Regulation (EU) 2016/679). For a controller that is also an AI-Act provider/deployer of high-risk AI, the two regimes stack with the AI Act QMS as a sub-policy of the GDPR data-protection policy architecture. Scope-disjoint test: **Y (when the provider/deployer is a controller processing personal data via high-risk AI)**. No reclassification required.
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 mandates the entity-level policy artefact (Art. 21(2)(a) risk-analysis policy + IS-security policy + Art. 21(2)(f) effectiveness-assessment policy) and the governance act (Art. 20(1) management-body approve/oversee/liable); CRA provides the presumption-of-conformity machinery that the NIS 2 entity can rely on when procuring CRA-conformant products (Art. 27(1) `Products with digital elements and the processes put in place by the manufacturer shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I where those products and processes conform to harmonised standards …` + Art. 27(2) `The Commission may adopt implementing acts establishing common specifications …` + Art. 27(5) `Common specifications … shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I …` + Art. 27(8) `A product with digital elements and the processes put in place by the manufacturer for which the manufacturer has obtained an EU statement of conformity or an EU certificate under a European cybersecurity certification scheme adopted pursuant to Regulation (EU) 2019/881 … shall be presumed to be in conformity with the essential cybersecurity requirements …`). The CRA presumption substitutes for parts of the NIS 2 supplier-assessment obligation (cross to D-06.1) but does not substitute for the NIS 2 entity-level policy architecture. Scope-disjoint test: **Conditional (Y when the entity procures CRA-conformant products; N otherwise)**. No reclassification required.
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose policy + governance architecture. NIS 2: Art. 20(1) management-body approve/oversee/liable + Art. 21(2)(a) risk-analysis policy + IS-security policy + Art. 21(2)(f) effectiveness-assessment policy. DORA: Art. 5(2) management-body define/approve/oversee/be-responsible + Art. 6(1) ICT risk-management framework + Art. 6(4) three-lines-of-defence + asset identification. DORA's ICT risk-management framework is the dominant authority for financial entities under DORA's direct scope; NIS 2 applies to the financial entity only insofar as it is an NSIE (essential/important entity) outside DORA. The EQUAL classification preserves the OJ literal parallel between the two regimes on the policy object; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry. Scope-disjoint test: **Y (when the DORA financial entity is also an NSIE adopting risk-management policies subject to management-body approval)**. No reclassification required.
- **NIS2 ↔ AI_Act** — COMPLEMENTARY (SAME): NIS 2 governance applies at the entity level (Art. 20(1) + Art. 21(2)(a) + Art. 21(2)(f)); AI Act QMS applies at the AI-system level (Art. 17(1) 13-element closed list + Art. 13(1)+(3) transparency instructions). For NSIEs deploying high-risk AI, the QMS becomes a sub-policy of the entity-level NIS 2 governance framework — the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy. Scope-disjoint test: **Y (when an NSIE deploys high-risk AI and the AI Act QMS becomes a sub-policy)**. No reclassification required.
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA's presumption of conformity via harmonised standards + common specifications + CSA certification (Art. 27(1)/(2)/(5)/(8)/(9)) allows DORA entities to rely on CRA-conformant products as inputs to their ICT risk-management framework (Art. 6(1)). The two policies operate on different layers — CRA on the product layer (the artefact manufactured and placed on the market), DORA on the entity layer (the financial-entity governance architecture). For a DORA entity procuring CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to D-06.1) but does not discharge the DORA framework obligation. Scope-disjoint test: **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)**. No reclassification required.
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME): For AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack (Annex I Part I essential cybersecurity requirements including Annex I Part I (2) cybersecurity risk assessment mapping) coexists with the AI Act QMS stack (Art. 17(1) 13-element closed list (a)-(m)). The two operate on different layers — CRA on the product cybersecurity requirements, AI Act on the AI-system quality-management system — and the policies stack on the same integrated product-organisation. **CRDA flag: unlike D-09.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, D-09.1 has no comparable OJ-level consolidation rule** — at D-09.1 the two policies are co-dischargeable but not substitutable. Scope-disjoint test: **Y (when the same product is both CRA-regulated and AI-Act high-risk)**. No reclassification required.
- **DORA ↔ AI_Act** — COMPLEMENTARY (SAME): DORA's ICT risk-management framework (Art. 6(1) + Art. 5(2) + Art. 6(4)) + AI Act's QMS (Art. 17(1) 13-element closed list) + AI Act's deployer measures (Art. 26(1) `appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use accompanying the systems`) stack for DORA financial entities deploying high-risk AI. The three-lines-of-defence model and the QMS are compatible governance architectures (QMS provides the AI-system-quality layer; three-lines-of-defence provides the entity-level-risk layer). Scope-disjoint test: **Y (when a DORA financial entity deploys high-risk AI and integrates QMS into the framework)**. No reclassification required.
The information-security-policy architecture is **legitimately diverse without scope-disjoint structure** — each regulator imposes a **distinct policy artefact** under a **distinct anchor** at a **distinct governance hook**: GDPR (Art. 24(1) `policies … designed to implement data-protection principles … in an effective manner` + Art. 5(2) accountability + DPO designation per Art. 37-39) — controller-side data-protection policies with DPO as governance anchor; NIS 2 (Art. 20(1) sentence 1 `approve the cybersecurity risk-management measures … oversee their implementation and can be held liable` + Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures`) — entity-level policy artefacts with management-body approve/oversee/liable architecture; CRA (Art. 24(1) `cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product` + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) presumption of conformity via harmonised standards / common specifications / CSA certification) — manufacturer-side / OSS-steward-side policies with presumption-of-conformity machinery; DORA (Art. 5(2) `shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` + Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively` + Art. 6(4) `three lines of defence model` + Art. 7(1) `identify, classify and adequately document`) — financial-entity ICT risk-management framework with three-lines-of-defence as governance anchor; AI Act (Art. 17(1) `quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)` + Art. 13(1)+(3) transparency-to-deployers instructions-for-use) — provider-side QMS with 13 enumerated aspects as policy carrier. The high-level SO surfaces the **common policy duty** (documented policy architecture + governance hooks + accountability chain + per-reg perspective preservation); the per-regulation anchor, governance body, content template, threshold, evidence template, and recipient are preserved verbatim in the five sub-SOs.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (Y when controller is also manufacturer or OSS steward; N otherwise — different artefacts, different actors)  |
|  **CRA**  |  Conditional (Y when controller is also manufacturer/OSS steward; same; reciprocal)  |  —  |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional (Y/N)** = conditional overlap depending on entity-product combination — Y when the listed entity-product combination applies on a single party, N otherwise. **No N (typically) pairs** — D-09.1 has no scope-disjoint structure. CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Y; GDPR↔CRA = Conditional (Y when controller is also manufacturer or OSS steward); GDPR↔DORA = Y; GDPR↔AI_Act = Y; NIS2↔CRA = Conditional (Y when entity procures CRA-conformant); NIS2↔DORA = Y; NIS2↔AI_Act = Y; CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant); CRA↔AI_Act = Y; DORA↔AI_Act = Y.

## Cross-recipient map

#### Cross-recipient map
D-09.1 generates a layered recipient set on the **information-security-policy evidence trail** but does **not generate a notification cascade of D-09.1 itself**. The recipient set is at the **policy-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 24(1) appropriate-measures demonstration + Art. 30 (cross to D-09.4) + Art. 35 (cross to D-09.2) + Art. 5(2) accountability burden + DPO designation records per Art. 37-39; **NIS 2's management body + competent authority** on the Art. 21(1) documented policies on risk analysis + IS security + Art. 21(2)(f) effectiveness-assessment + Art. 20(1) management-body approval; **CRA's market surveillance authority (MSA)** on the Art. 24(1) OSS-steward cybersecurity policy + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records; **DORA's competent authority (national financial supervisory authority / NCA)** on the Art. 6(1) ICT risk-management framework + Art. 5(2) management-body oversight + Art. 6(4) three-lines-of-defence + EBA Guidelines on ICT and security risk management supervisory baseline; **AI Act's market surveillance authority + AI Office + provider + deployer** on the Art. 17(1) QMS documented policies/procedures/instructions + Art. 13(1)+(3) transparency-to-deployers instructions-for-use. These are distinct regulatory channels on the same policy-records artefacts but they do not generate a notification cascade of D-09.1 itself — they are **compliance-evidence channels on the layered policy architecture**. The **D-09.2 (Impact & Risk Assessments)** is the operational downstream artefact where the D-09.1 policy architecture is implemented through documented assessments; **D-09.4 (Records of Processing)** is the documentation downstream artefact where GDPR RoPA + CRA technical documentation + AI Act Annex IV technical documentation + DORA ICT asset registers stack. **D-08.3 (Management Board Training)** is the human-side downstream where the D-09.1 policy architecture is implemented through DORA Art. 5(4) + NIS 2 Art. 20(2) management-body training; **D-06.1 (Vendor Risk Assessment)** is the supply-chain downstream where the CRA Art. 27 presumption-of-conformity machinery operationalises the NIS 2 / DORA supplier-assessment evidence obligation.
---

## HSO considerations (from D-09.1.0 — High-level SecurityObjective)

**Considerations.**
- 5 of 5 regulations participate with **distinct anchors and governance bodies** — GDPR (Art. 24(1) + Art. 5(2) + DPO Art. 37-39 — controller-side data-protection policies with DPO as governance anchor), NIS 2 (Art. 20(1) + Art. 21(2)(a)+(f) — entity-level policy artefacts with management-body approve/oversee/liable architecture), CRA (Art. 24(1) OSS-steward + Art. 13(8) manufacturer + Art. 27(1)/(2)/(5)/(8)/(9) presumption-of-conformity machinery), DORA (Art. 5(2) + Art. 6(1) + Art. 6(4) + Art. 7(1) — financial-entity ICT risk-management framework with three-lines-of-defence), AI Act (Art. 17(1) 13-element QMS closed list + Art. 13(1)+(3) transparency-to-deployers).
- **CRDA-deep verified (10 pairs: 9 SAME — COMPLEMENTARY + 1 SAME — EQUAL NIS 2 ↔ DORA on policy + governance dimension, DORA-dominant for financial entities)** — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs; the high-level SO does NOT collapse any per-reg policy artefact.
- **Most heavily-overlapped sub-domain** with no OJ-level consolidation rule (unlike D-09.2 where CRA Art. 13(4) sentence 2 covers risk-assessment, not policy); Phase 1 entities must build a 5-policy architecture with 5 distinct governance bodies (DPO / management body / manufacturer-OSS-steward / management body / provider) and reconcile the DPO role with the management body in the corporate-governance charter.
- **Scope caveats**: (a) NIS 2 ↔ DORA EQUAL discharges both obligations on the DORA-dominant stack for financial entities; (b) DPO (GDPR) vs. management body (NIS 2 / DORA) interplay is a Layer 1 architecture-mapping item (DPO reports to management body but is not a member per Art. 38(6)); (c) CRA presumption of conformity does not extend cross-regulation — it discharges the CRA conformity-assessment obligation only, not GDPR/NIS 2/DORA policy obligations.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-09.1 over a distinct **policy artefact** of the information-security-policy architecture; the anchor, governance body, trigger, threshold anchor, recipient, and legal anchor all depend on which perspective the regulation takes on the policy object.
| Axis (reg) | Policy artefact | Anchor (OJ-literal) | Governance body | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | controller-side data-protection policies, reviewed and updated where necessary in light of the nature, scope, context, and purposes of processing, the risks of varying likelihood and severity, and the cost of implementation | Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` + Art. 5(2) accountability + DPO (Art. 37-39) | DPO (designated individual with Art. 39(1) tasks reporting to the management body but not a member per Art. 38(6)) | supervisory authority (DPA) — Art. 5(2) accountability on Art. 24(1) policies + Art. 30(4) (cross to D-09.4) + Art. 35(7) (cross to D-09.2) | Art. 24(1) + Art. 24(2) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) chapeau + Art. 37(1) + Art. 38(1) + Art. 38(6) conflict of interests + Art. 39(1) DPO tasks |
| **NIS2** | entity-level policies on risk analysis + IS security + policies and procedures to assess effectiveness of cybersecurity risk-management measures | Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` | management body (Art. 20(1) sentence 1 `management bodies … approve the cybersecurity risk-management measures … oversee their implementation and can be held liable for infringements`) | management body + competent authority — Art. 21(2)(a)+(f) policy records + Art. 21(1) documented policies on risk analysis + IS security + Art. 20(1) management-body approval records | Art. 20(1) sentence 1 + Art. 21(2)(a) + Art. 21(2)(f) + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Recital 56 proportionality |
| **CRA** | OSS-steward cybersecurity policy (Art. 24(1) 4-element: documenting, addressing, remediating vulnerabilities; sharing information within the open-source community) + manufacturer policies/processes/procedures including CVD policy, secure-update distribution, support-period determination methodology, cessation-of-operations communication + presumption of conformity via harmonised standards / common specifications / CSA certification | Art. 24(1) `Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster the development of a secure product with digital elements as well as an effective handling of vulnerabilities by the developers of that product` + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1) `Products with digital elements and the processes put in place by the manufacturer shall be presumed to be in conformity with the essential cybersecurity requirements set out in Part I of Annex I where those products and processes conform to harmonised standards` + Art. 27(8) CSA certification | OSS steward (Art. 24(1) OSS-steward policy owner) + manufacturer (Art. 13(8) manufacturer policies/processes/procedures owner) — distinct from data-protection governance body | market surveillance authority (MSA) — Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) conformity-assessment records + Annex VII technical documentation (cross to D-09.4) | Art. 24(1) + Art. 24(2) + Art. 13(8) + Art. 13(8) sentence 6 CVD policy + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation of operations + Art. 27(1) + Art. 27(2) + Art. 27(5) + Art. 27(8) + Art. 27(9) + Recital 25 (Annex II scope) |
| **DORA** | sound, comprehensive, well-documented ICT risk-management framework comprising 5-artefact types (strategies, policies, procedures, ICT protocols, tools) + three-lines-of-defence model + ICT supported business functions / information assets / ICT assets identified, classified, documented | Art. 5(2) `The management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` + Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively` + Art. 6(4) `three lines of defence model` | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible + `all arrangements`) — corporate-governance body | competent authority (NCA — national financial supervisory authority) + management body — Art. 6(1) ICT risk-management framework + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 5(2) + Art. 6(1) + Art. 6(2) 5-artefact closed list (`strategies, policies, procedures, ICT protocols and tools`) + Art. 6(4) three-lines-of-defence + Art. 7(1) asset identification/classification + Art. 4 proportionality |
| **AI_Act** | provider-side QMS documented in a systematic and orderly manner in the form of written policies, procedures, instructions, covering at least 13 enumerated aspects ((a) compliance strategy; (b) design/development/verification; (c) post-market monitoring; (d) data quality; (e) risk management; (f) … (m)) + transparency-to-deployers via instructions-for-use | Art. 17(1) `The quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) … (m)` + Art. 13(1) `sufficiently transparent to enable deployers to interpret a system's output and use it appropriately` + Art. 13(3) `concise, complete, correct and clear` instructions for use | provider (high-risk AI system provider with Art. 17(1) QMS + Art. 13(1) transparency-to-deployers + Art. 26(1) deployer measures aligned with instructions) — distinct from MSA / AI Office oversight | provider, deployer, MSA, AI Office — Art. 17(1) QMS documented policies/procedures/instructions + Art. 13(1)+(3) transparency instructions-for-use + Art. 26(1) deployer measures aligned with instructions | Art. 17(1) + Art. 17(1)(c) design/design control/verification + Art. 17(1)(g) risk-management-system documentation cross-reference to Art. 9 + Art. 13(1) + Art. 13(3) + Art. 26(1) |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
(See the validated-relationships table above for the 5×5 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-09.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations have ≥1 Y or Conditional-Y-scope-overlap pair on the same
party** (e.g. a DORA financial entity that is also a controller and
processes personal data — a vertically-integrated financial-controller
with GDPR + DORA applicability on the layered 5-policy architecture).
For an integrated DORA financial entity that is also a NIS 2 NSIE
processor, the GDPR + NIS 2 + DORA sub-SOs activate; the high-level SO
engages on the GDPR↔NIS2 COMPLEMENTARY pair (NIS 2 management-body
approve/oversee/liable governance extends to the GDPR data-protection
policies) and the NIS 2↔DORA EQUAL pair (DORA-dominant stack discharges
both obligations for financial entities). For a CRA-regulated manufacturer
that is also a controller (controller-manufacturer), the GDPR + CRA
sub-SOs activate on **two different artefacts** (controller-side data-
protection policies vs. manufacturer-side policies for product
cybersecurity) — the two tracks coexist without OJ-level consolidation
rule; the high-level SO does **NOT** collapse the artefact boundaries.
For an entity with GDPR + CRA + AI Act applicability but no NIS 2 /
DORA applicability, the three sub-SOs activate on distinct artefacts
(controller policies + manufacturer policies + QMS) that must be
reconciled in the consolidated policy architecture. The five policy
artefacts are stacked, not collapsed: DPO-catalysed controller policies
(GDPR); management-body approve/oversee/liable on entity-level policy
artefacts (NIS 2); manufacturer / OSS-steward policies with
presumption-of-conformity machinery (CRA); management-body
define/approve/oversee/be-responsible + three-lines-of-defence on
financial-entity ICT risk-management framework (DORA); provider-side
13-element QMS as policy carrier (AI Act). The high-level SO surfaces
the common documented-policy-architecture duty but does **NOT** collapse
the per-reg anchor, governance body, content template, threshold,
recipient, or evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **5 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA, AI Act —
  all five participate on the policy object): GDPR (Art. 24(1) + Art.
  5(2) + DPO Art. 37-39 as controller-side data-protection policies with
  DPO governance anchor); NIS 2 (Art. 20(1) + Art. 21(2)(a) + Art.
  21(2)(f) as entity-level policy artefacts with management-body
  approve/oversee/liable architecture); CRA (Art. 24(1) OSS-steward
  policy + Art. 13(8) manufacturer policies + Art. 27(1)/(2)/(5)/(8)/(9)
  presumption-of-conformity machinery as manufacturer-side /
  OSS-steward-side policies); DORA (Art. 5(2) + Art. 6(1) + Art. 6(4) +
  Art. 7(1) as financial-entity ICT risk-management framework with
  three-lines-of-defence as governance anchor); AI Act (Art. 17(1) 13-
  element QMS + Art. 13(1)+(3) transparency-to-deployers as provider-
  side QMS as policy carrier).
- **10 pairwise cells, verified by CRDA-deep**:
  GDPR↔NIS2 (SAME — COMPLEMENTARY — `what` controller policies + `that`
  management-body governance act stack at controller-NSIE);
  GDPR↔CRA (SAME — COMPLEMENTARY — Conditional-Y scope overlap when
  controller is also manufacturer or OSS steward);
  GDPR↔DORA (SAME — COMPLEMENTARY — DORA framework as carrier +
  controller data-protection policies as module for DORA financial
  entities that are controllers);
  GDPR↔AI_Act (SAME — COMPLEMENTARY — AI Act Recital 78 explicit GDPR
  preservation; AI Act QMS as sub-policy of GDPR controller policies for
  providers/deployers that are controllers processing personal data via
  high-risk AI);
  NIS2↔CRA (SAME — COMPLEMENTARY — Conditional-Y scope overlap when
  entity procures CRA-conformant products; NIS 2 policy artefact + CRA
  presumption-of-conformity machinery;
  NIS2↔DORA (SAME — EQUAL — both regulations impose policy + governance
  architecture; DORA-dominant for financial entities under DORA's
  direct scope);
  NIS2↔AI_Act (SAME — COMPLEMENTARY — NIS 2 entity-level governance +
  AI Act QMS as sub-policy for NSIEs deploying high-risk AI);
  CRA↔DORA (SAME — COMPLEMENTARY — Conditional-Y scope overlap when
  DORA entity procures CRA-conformant products; CRA presumption
  substitutes for parts of DORA supplier-assessment evidence but not
  DORA framework obligation);
  CRA↔AI_Act (SAME — COMPLEMENTARY — CRA Annex I conformity + AI Act
  QMS stack for products that are both CRA-regulated and AI-Act
  high-risk; **no OJ-level consolidation rule at D-09.1** — unlike D-
  09.2 CRA Art. 13(4) sentence 2 which permits AI Act Art. 9 to
  substitute for CRA risk assessment, that rule covers the *risk-
  assessment object* not the *policy object*);
  DORA↔AI_Act (SAME — COMPLEMENTARY — DORA ICT risk-management framework
  + AI Act QMS + Art. 26(1) deployer measures stack for DORA financial
  entities deploying high-risk AI; three-lines-of-defence + QMS
  compatible governance architectures).
- The five participating regulations impose **distinct policy
  artefacts** at **distinct anchors** with **distinct governance
  bodies** and **distinct content templates**: GDPR (controller-side
  Art. 24(1) data-protection policies with DPO governance anchor, content
  not codified — entity-discretionary); NIS 2 (Art. 21(2)(a)+(f) policy
  artefacts + Art. 20(1) management-body approve/oversee/liable, content
  not codified — entity-discretionary under Recital 56 proportionality);
  CRA (Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies,
  Art. 24(1) OSS-steward policy has 4-element partial content codification
  (i)-(iv) per SR-CRA-072; presumption of conformity via Art. 27
  harmonised standards / common specifications / CSA certification);
  DORA (Art. 5(2) + Art. 6(1) ICT risk-management framework + Art.
  6(4) three-lines-of-defence, Art. 6(2) 5-artefact closed list
  `strategies, policies, procedures, ICT protocols and tools`);
  AI Act (Art. 17(1) 13-element QMS closed list (a)-(m) +
  transparency-to-deployers instructions-for-use per Art. 13(1)+(3) —
  full content codification). The thresholds align qualitatively (no
  regulation imposes a quantitative policy-cadence — all are entity-
  discretionary under proportionality or equivalent). The five anchors
  align in their direction-of-travel (documented policy architecture
  with governance + accountability + content + governance-body hooks)
  but the artefacts, governance bodies, content templates, recipients,
  evidentiary templates diverge.
- The high-level SO describes the **COMMON OBJECTIVE** (documented
  policy architecture + governance hooks + accountability chain +
  per-reg perspective preservation); the **per-regulation perspective**
  (artefact, governance body, anchor, content template, threshold,
  recipient, evidence template) is preserved verbatim in the five sub-
  SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the policy-duty itself**, because no
  pair was verified as CONTRADICTORY or CORRECTED (all 10 pairs are
  SAME — 9 SAME — COMPLEMENTARY + 1 SAME — EQUAL with no scope-disjoint
  structure). Phase 1C Doc 07 does not need to resolve a policy-object
  contradiction because none exist by construction; **however**, Phase
  1C Doc 07 must perform the **Layer 1 cross-cutting governance-
  architecture mapping** because the 5 regulators impose 5 distinct
  policy artefacts with no OJ-level consolidation rule (CRDA Domain-
  Analysis flag — "Five-policy-stack with no OJ-level consolidation
  rule"; "DPO (GDPR) vs. management body (NIS 2 / DORA)" interplay
  unresolved at the OJ level; "Presumption of conformity (CRA Art. 27)
  does not extend cross-regulation"). The Layer 1 mapping reconciles the
  DPO role with the management body in the corporate-governance charter
  and operationalises the AI Act QMS as a sub-policy.
- **Scope caveat (CRITICAL — no OJ-level consolidation rule at D-09.1)**
  — derived from CRDA-deep verified classifications: D-09.1 is the most
  heavily-overlapped sub-domain with all 5 regulators imposing distinct
  policy artefacts and no OJ-level consolidation rule. Phase 1 entities
  must build a governance-architecture mapping that nests all five
  policies without overlap. The Layer 1 cross-cutting analysis is
  required to reconcile the DPO (GDPR) and management body (NIS 2 /
  DORA) roles in the corporate-governance charter. AI Act QMS becomes a
  sub-policy of the integrated policy architecture. CRA presumption of
  conformity is the upstream gate for CRA-conformant products but does
  not discharge cross-regulation obligations (NIS 2 entity-side policy
  artefact, DORA ICT risk-management framework, GDPR data-protection
  policies remain independently required).
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA EQUAL classification on
  policy + governance architecture)** — derived from CRDA-deep verified
  classifications: both regulations impose policy + governance
  architecture (NIS 2 Art. 20(1) management-body approve/oversee/liable +
  Art. 21(2)(a)+(f) policy artefacts vs. DORA Art. 5(2) +
  Art. 6(1) ICT risk-management framework + Art. 6(4) three-lines-of-
  defence). For DORA financial entities, the DORA ICT risk-management
  framework discharges both DORA's dedicated framework obligation and
  NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance
  act. For non-financial NSIEs, NIS 2 is the authority. The EQUAL
  classification preserves the OJ literal parallel between the two
  regimes on the policy + governance dimension; the dominant-authority
  reading is the operational consequence of the DORA-direct-
  applicability vs NIS 2-MS-transposition asymmetry.
- **Scope caveat (CRITICAL — DPO vs management body interplay)** —
  derived from CRDA-deep verified classifications (DomainAnalysis
  §D-09.1 line 172): GDPR's DPO is a designated individual with Art.
  39(1) tasks; NIS 2 / DORA's management body is the corporate-
  governance body with collective approve/oversee/liable obligations.
  The DPO reports to the management body but is not a member of it
  (Art. 38(6) conflict-of-interests). The interplay between the DPO's
  advisory role and the management body's liability exposure is
  unresolved at the OJ level. Phase 1 entities must reconcile the DPO
  role in the corporate-governance charter (e.g., DPO attends management-
  body meetings as observer with advisory role without voting rights).
- **Scope caveat (CRITICAL — CRA presumption-of-conformity does not
  extend cross-regulation)** — derived from CRDA-deep verified
  classifications (DomainAnalysis §D-09.1 line 173): CRA presumption of
  conformity via harmonised standards (Art. 27(1)) discharges the CRA
  conformity-assessment obligation only. It does not substitute for the
  GDPR Art. 24(1) appropriate-measures obligation, NIS 2 Art.
  21(2)(a)+(f) policy obligation, or DORA Art. 6(1) ICT risk-management
  framework. Phase 1 entities must discharge each regime's policy
  obligation separately even when the underlying product is CRA-
  conformant.
---

## Emergent tensions (from CRDA-deep §D-09.1)

#### Emergent tensions (from CRDA-deep §D-09.1)
**0 conditional emergent tensions** on the information-security-policy duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 10 pairs are all SAME — 9 SAME — COMPLEMENTARY + 1 SAME — EQUAL. **No scope-disjoint pairs** at D-09.1 — every pair activates at the Y or Conditional-Y-on-same-party level on at least the layered-stack dimension. **No SCOPE-DISJOINT reclassifications** — CRDA preserves every pair as SAME — COMPLEMENTARY or SAME — EQUAL. **No CONTRADICTORY pairs** on the policy-duty itself. The **policy-artefact divergence** (controller-side data-protection policies / entity-level risk-analysis + IS-security + effectiveness-assessment policy artefacts / manufacturer-side + OSS-steward-side policies with presumption-of-conformity machinery / financial-entity ICT risk-management framework / provider-side QMS) is the **legitimately diverse dimension**: each regulator imposes a distinct policy artefact under a distinct anchor at a distinct governance hook (DPO / management body / manufacturer-OSS-steward / management-body / provider), and the operational convergence is on a **layered 5-policy architecture** — the high-level SO surfaces the common policy duty without collapsing the per-reg perspective.
The **most-heavily-overlapped sub-domain flag (CRDA DomainAnalysis §D-09.1 line 27)** is the structurally significant operational divergence — D-09.1 is the most heavily-overlapped sub-domain with all 5 regulators imposing distinct policy artefacts and no OJ-level consolidation rule (unlike D-09.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment — that unification rule covers the *risk-assessment object* not the *policy object* at D-09.1). Phase 1 entities building a vertically-integrated stack (DORA financial entity that processes personal data and ships AI-enabled CRA-regulated products) face a 5-policy architecture with no OJ-level consolidation. The Phase 1C Doc 07 must perform the **Layer 1 cross-cutting governance-architecture mapping** to nest all five policies without overlap and reconcile the DPO role (GDPR) with the management body (NIS 2 / DORA) in the corporate-governance charter. AI Act QMS becomes a sub-policy; CRA presumption-of-conformity is the upstream gate for CRA-conformant products but does not discharge cross-regulation obligations. The **DPO (GDPR) vs. management body (NIS 2 / DORA)** interplay is a Layer 1 architecture-mapping item: the DPO reports to the management body but is not a member of it (Art. 38(6) conflict-of-interests); the management body's collective approve/oversee/liable obligations under NIS 2 / DORA are distinct from the DPO's advisory role; the OJ does not prescribe a specific reconciliation. Phase 1 entities reconcile the DPO role in the corporate-governance charter (e.g., DPO attends management-body meetings as observer with advisory role without voting rights).
The **NIS 2 ↔ DORA EQUAL classification on policy + governance architecture** is the structurally significant EQUAL pair: both regulations impose policy + governance architecture (NIS 2 Art. 20(1) management-body approve/oversee/liable + Art. 21(2)(a)+(f) policy artefacts; DORA Art. 5(2) + Art. 6(1) ICT risk-management framework + Art. 6(4) three-lines-of-defence). DORA's `sound, comprehensive and well-documented` Art. 6(1) framework is more prescriptive than NIS 2's `policies on risk analysis and information system security` Art. 21(2)(a) (which is entity-discretionary under Recital 56). For DORA financial entities, the DORA ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act — DORA-dominant under DORA's direct scope. For non-financial NSIEs, NIS 2 is the authority. The EQUAL classification preserves the OJ literal parallel between the two regimes on the policy + governance dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry.
The **5-artifact content template variation** is the structurally significant content-codification divergence: GDPR not codified for content (entity-discretionary controller-policy content); NIS 2 Art. 21(2)(a)+(f) policy artefacts (entity-discretionary under Recital 56 proportionality); CRA Art. 24(1) OSS-steward 4-element cybersecurity policy (i)-(iv) per SR-CRA-072 — partial content codification; DORA Art. 6(2) 5-artefact closed list (`strategies, policies, procedures, ICT protocols and tools`); AI Act Art. 17(1) 13-element closed list (a)-(m) — full content codification. The content-template variation means Phase 1 entities building a consolidated policy must reconcile 5 different content-template dimensions with no OJ-level consolidation rule.
The high-level SO surfaces the common information-security-policy duty (documented policy architecture + governance hooks + accountability chain + per-reg perspective preservation); the per-reg perspective on the policy artefact, anchor, governance body, content template, threshold, recipient, and evidence template is documented separately in the 5 sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the layered 5-policy architecture (controller-side data-protection policies / entity-level risk-analysis + IS-security + effectiveness-assessment / manufacturer-side + OSS-steward-side / financial-entity ICT risk-management framework / provider-side QMS) with the 5 distinct governance bodies (DPO / management body / manufacturer-OSS-steward / management body / provider) is itself the layered reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-09.1 — with overlapping policy-architecture scope-determiners on the same party — operates a **layered 5-policy architecture** with 5 distinct governance hooks. The high-level SO (`SG-D-09.1.HL`) describes the common documented-policy-architecture duty (documented policy architecture + governance hooks + accountability chain + per-reg perspective preservation); the per-reg perspective is preserved in the 5 sub-SOs (artefact, governance body, anchor, content template, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 5-policy architecture operationalising the per-reg governance body on the integrated policy architecture. The high-level SO does NOT collapse the 5 policy artefacts into a single policy; the per-reg perspective on the artefact, governance body, anchor, content template, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **information-security-policy strategy**: (1) a 5-layer policy architecture with explicit governance-body hand-offs (GDPR Art. 24(1) + Art. 5(2) + Art. 37-39 DPO controller policies → NIS 2 Art. 20(1) + Art. 21(2)(a)+(f) entity-level policy artefacts with management-body approve/oversee/liable → CRA Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies + Art. 27(1)/(2)/(5)/(8)/(9) presumption-of-conformity machinery → DORA Art. 5(2) + Art. 6(1) + Art. 6(4) + Art. 7(1) financial-entity ICT risk-management framework → AI Act Art. 17(1) QMS + Art. 13(1)+(3) transparency-to-deployers); (2) the most-heavily-overlapped-sub-domain flag with no OJ-level consolidation rule as a Layer 1 governance-architecture mapping item (5 distinct governance bodies: DPO / management body / manufacturer-OSS-steward / management body / provider); (3) the Layer 1 mapping reconciles the DPO (GDPR) with the management body (NIS 2 / DORA) in the corporate-governance charter (DPO reports to the management body but is not a member per Art. 38(6)); (4) AI Act QMS becomes a sub-policy of the integrated policy architecture; (5) CRA presumption-of-conformity (Art. 27(1)/(2)/(5)/(8)/(9)) is the upstream gate for CRA-conformant products but does not discharge cross-regulation obligations; (6) the 5-artifact content template variation (entity-discretionary / entity-discretionary / partial codification / 5-artefact closed list / 13-element closed list) must be reconciled in the consolidated policy architecture without OJ-level consolidation rule; (7) the EQUAL NIS 2 ↔ DORA classification on policy + governance architecture discharges both obligations on the DORA-dominant stack for financial entities under DORA's direct scope — for non-financial NSIEs, NIS 2 is the authority. The high-level SO does NOT resolve any policy-object contradiction because none exist by construction (10 SAME — 9 COMPLEMENTARY + 1 EQUAL); the Layer 1 cross-cutting governance-architecture mapping is the operational mechanism for nesting the 5 policies in a single integrated policy architecture.
---
**Document version:** 0.1 — initial derivation from CRDA-deep §D-09.1 (10 pairs verified).
**See also:** [`D-09.2.md`](D-09.2.md) (Impact & Risk Assessments — same 5-reg participation + 1 OJ-level consolidation rule — CRA Art. 13(4) sentence 2 on AI Act Art. 9 substituting for CRA risk assessment); [`index.md`](../index.md); [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.1.md) (CRDA-deep source).

## Part 1 §3 — context

### 3. Security Requirements
## 9.1 Information Security Policies — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md`. See that file for the CRDA-deep verified classification (10 pairs: 9 SAME — COMPLEMENTARY + 1 SAME — EQUAL — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs; **5 of 5 regulations participate**; the **most heavily-overlapped sub-domain** per CRDA-deep §9.1 line 27 with **no OJ-level consolidation rule** at 9.1 — unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment), the per-reg 5-distinct-policy-artefact architecture (GDPR controller-side data-protection policies with DPO governance anchor; NIS 2 entity-level risk-analysis + IS-security + effectiveness-assessment policy artefacts with management-body approve/oversee/liable; CRA manufacturer-side / OSS-steward-side policies with presumption-of-conformity machinery; DORA financial-entity ICT risk-management framework with three-lines-of-defence; AI Act provider-side QMS with 13-element closed list + transparency-to-deployers instructions-for-use), the NIS 2 ↔ DORA EQUAL classification with DORA-dominant stack for financial entities, the DPO (GDPR) vs. management body (NIS 2 / DORA) interplay as Layer 1 cross-cutting governance-architecture mapping item, the CRA-presumption-of-conformity scope-limitation (does not extend cross-regulation), the per-reg artefact / governance body / anchor / content template / threshold / recipient / evidence template, and the aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA, AI Act (ALL 5 — the most heavily-overlapped sub-domain per CRDA-deep §9.1 line 27). The five regulators each impose a **distinct policy artefact** under a **distinct anchor** at a **distinct governance hook**: GDPR (Art. 24(1) `policies … designed to implement data-protection principles … in an effective manner` + Art. 5(2) accountability + DPO per Art. 37-39) — controller-side data-protection policies with DPO as governance anchor; NIS 2 (Art. 20(1) + Art. 21(2)(a) `policies on risk analysis and information system security` + Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures`) — entity-level policy artefacts with management-body approve/oversee/liable architecture; CRA (Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies/processes/procedures + Art. 27(1)/(2)/(5)/(8)/(9) presumption of conformity via harmonised standards / common specifications / CSA certification) — manufacturer-side / OSS-steward-side policies with presumption-of-conformity machinery; DORA (Art. 5(2) `define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` + Art. 6(1) `sound, comprehensive and well-documented ICT risk management framework` + Art. 6(4) `three lines of defence model` + Art. 7(1) `identify, classify and adequately document`) — financial-entity ICT risk-management framework with three-lines-of-defence; AI Act (Art. 17(1) `quality management system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions` 13-element closed list (a)-(m) + Art. 13(1)+(3) transparency-to-deployers instructions-for-use) — provider-side QMS as policy carrier.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 9.1
  volere_section: 15
  volere_subtype: integrity
  title: "Information security policies established through a documented policy architecture with governance hooks and accountability chain anchoring the entity's cybersecurity posture"
  derives_from:
    hso_sub_so: SO-9.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.1.md
    objective_ref_section: "### 9.1.0"
  description: |
    The product shall establish information security policies through a documented policy architecture with governance hooks and an accountability chain that anchors the entity's cybersecurity posture, where ≥2 of the participating regulations (GDPR, NIS 2, CRA, DORA, AI Act) have applicability with overlapping policy scope-determiners on the same party, with the per-reg policy artefact, governance body, anchor, content template, threshold, recipient, and evidence template preserved verbatim in the five sub-SOs.
  fit_criterion: |
    A documented policy architecture is established covering all five participating policy artefacts (or the subset applicable to the entity) at the policy-evidence layer with the per-reg governance body as the policy-approval hook: GDPR controller-side data-protection policies with the DPO (designated individual with Art. 39(1) tasks reporting to the management body but not a member per Art. 38(6) conflict-of-interests) as governance anchor (Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` + Art. 24(2) `appropriate data-protection policies` + Art. 5(2) accountability burden + Art. 37(1) DPO designation triggers), with the policy reviewed and updated `where necessary` on a material-change-of-risk trigger supplemented by annual periodic review (EDPB Guidelines 07/2019 on accountability); NIS 2 entity-level policies on risk analysis + IS security (Art. 21(2)(a)) + policies and procedures to assess the effectiveness of cybersecurity risk-management measures (Art. 21(2)(f)) with the management body as governance body approving the Art. 21 measures (Art. 20(1) sentence 1 first-clause `approve`) and overseeing their implementation (Art. 20(1) sentence 1 second-clause `oversees`), with documented management-body approval minute + entity-discretionary content calibrated by Recital 56 proportionality + state-of-the-art floor (Art. 21(1) sentence 2); CRA manufacturer policies/processes/procedures (Art. 13(8) + Annex I Part II §5 CVD policy + Annex I Part II §7 secure-update distribution + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation-of-operations communication) + OSS-steward cybersecurity policy (Art. 24(1) 4-element (i)-(iv) `documenting, addressing, remediating vulnerabilities; sharing of information concerning discovered vulnerabilities within the open-source community`) + presumption-of-conformity machinery (Art. 27(1) harmonised standards + Art. 27(2)/(5) common specifications + Art. 27(8) CSA certification) tracked at the conformity-assessment evidence layer; DORA ICT risk-management framework (Art. 5(2) four-verb coordination define/approve/oversee/be responsible + Art. 6(1) `sound, comprehensive and well-documented` framework + Art. 6(2) 5-artefact closed list `strategies, policies, procedures, ICT protocols and tools` + Art. 6(4) `three lines of defence model` + Art. 7(1) `identify, classify and adequately document` ICT supported business functions / information assets / ICT assets + Art. 4 proportionality for smaller entities); AI Act QMS documented in a systematic and orderly manner in the form of written policies, procedures, and instructions covering at least the 13 enumerated aspects (a)-(m) per Art. 17(1) closed list (compliance strategy + design/design control/design verification + post-market monitoring + data quality + risk management + ... + transparency-to-deployers instructions-for-use per Art. 13(1)+(3) `concise, complete, correct and clear` 4-way AND + `relevant, accessible and comprehensible` 3-way AND); the five policy artefacts are stacked on the integrated governance architecture and the per-reg artefact boundaries are NOT collapsed — the 9 SAME — COMPLEMENTARY pairs (GDPR↔NIS2, GDPR↔CRA, GDPR↔DORA, GDPR↔AI_Act, NIS2↔CRA, NIS2↔AI_Act, CRA↔DORA, CRA↔AI_Act, DORA↔AI_Act) operate on distinct policy artefacts under distinct anchors and stack on the layered architecture with the 1 SAME — EQUAL pair (NIS 2 ↔ DORA) discharging both obligations on the DORA-dominant stack for DORA financial entities (DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act for DORA financial entities that are also NSIEs, per CRDA-deep §9.1 NIS2↔DORA verified relationship); the Layer 1 cross-cutting governance-architecture mapping reconciles the DPO role (GDPR) with the management body (NIS 2 / DORA) in the corporate-governance charter (DPO reports to management body but is not a member per Art. 38(6)); the CRA presumption-of-conformity machinery does not extend cross-regulation — it discharges the CRA conformity-assessment obligation only, not GDPR/NIS 2/DORA/AI Act policy obligations; AI Act QMS becomes a sub-policy of the integrated policy architecture; the documentation trail is built under each reg's accountability burden (Art. 5(2) GDPR accountability + Art. 21(1) NIS 2 documented policies chapeau + Art. 24(2) CRA OSS-steward verifiable documentation + Art. 5(2) DORA management-body oversight + EBA Guidelines on Internal Governance + Art. 17(1) AI Act systematic-and-orderly QMS); verified by documented policy architecture review + per-reg artefact evidence pack on request + DPO designation records (GDPR, when applicable) + management-body approval minute + Art. 21 documented-policy chapeau (NIS 2) + Annex VII technical documentation (CRA, when applicable) + Art. 5(2) management-body oversight records + EBA Guidelines on Internal Governance fit-and-proper framework (DORA, when applicable) + Art. 17(1) QMS documentation + Art. 13(1)+(3) instructions-for-use (AI Act, when applicable) + per-reg supervisory review.
  priority: MUST
  verification_method: TEST
  dependencies: [9.1.1, 9.1.2, 9.1.3, 9.1.4, 9.1.5]
  nist_csf: [GV.PO-01, GV.PO-02, GV.RR-02]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: Y   # HL engages whenever ≥2 applicable regs have ≥1 Y or Conditional-Y-scope-overlap pair on the same party; for 9.1 the matrix shows every pair has Y or Conditional-Y activation on the joint-condition operator (no N (typically) scope-disjoint pairs), so the HL engages whenever ≥2 regs are applicable; the 9 SAME — COMPLEMENTARY pairs stack on the layered 5-policy architecture; the 1 SAME — EQUAL pair (NIS 2 ↔ DORA) discharges both obligations on the DORA-dominant stack for financial entities
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The high-level SO surfaces the **common documented-policy-architecture duty** (documented policy architecture + governance hooks + accountability chain) converging across GDPR Art. 24(1)/(2) + Art. 5(2) + DPO Art. 37-39 + NIS 2 Art. 20(1) + Art. 21(2)(a)+(f) + CRA Art. 24(1) OSS-steward policy + Art. 13(8) manufacturer policies + Art. 27(1)/(2)/(5)/(8)/(9) presumption of conformity + DORA Art. 5(2) + Art. 6(1)/(2)/(4) + Art. 7(1) + AI Act Art. 17(1) QMS + Art. 13(1)+(3) transparency-to-deployers; the **per-reg policy artefact, governance body, anchor, content template, threshold, recipient, and evidence template** are preserved verbatim in the five sub-SOs. The 10 verified pairs are all SAME — 9 SAME — COMPLEMENTARY + 1 SAME — EQUAL (NIS 2 ↔ DORA on policy + governance dimension, DORA-dominant for financial entities) — no CORRECTED, no CONTRADICTORY, no scope-disjoint pairs. **Most heavily-overlapped sub-domain** with no OJ-level consolidation rule at 9.1 (unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*); Phase 1 entities must build a 5-policy architecture with 5 distinct governance bodies (DPO / management body / manufacturer-OSS-steward / management body / provider) and reconcile the DPO role with the management body in the corporate-governance charter. The high-level SO does NOT collapse any per-reg policy artefact; it surfaces the common documented-policy-architecture duty with the per-reg anchor, governance body, content template, threshold, evidence template, and recipient preserved verbatim in the five sub-SOs. The **scope caveat (DPO vs management body interplay)** is a Layer 1 cross-cutting governance-architecture mapping item — DPO is a designated individual with Art. 39(1) tasks reporting to the management body but not a member per Art. 38(6) conflict-of-interests; the DPO role and the management body are reconciled in the corporate-governance charter. (Copied from the HSO Considerations block of `### 9.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-09.1
title: D-09.1 Information Security Policies — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.1 Information Security Policies
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---
> **Deep analysis:** [D-09.1 Information Security Policies](../../DeepAnalysis/D-09_Governance-Documentation/D-09.1.md)
#### D-09.1 Information Security Policies
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-026 + SG-GDPR-027 + SG-GDPR-037 | Appropriate data-protection policies reviewed and updated; controller responsibility; DPO designation + independence (Art. 24, Art. 5(2), Art. 37/38/39). | Process-oriented data-protection policies; DPO as governance anchor. |
| NIS2 | SG-NIS2-021 + SG-NIS2-022 + SG-NIS2-023 | Management body approves/oversees/liable; policies on risk analysis + IS security; policies to assess effectiveness (Art. 20(1), Art. 21(2)(a)+(f)). | Governance-first with policy artefact; management-body accountability architecture. |
| CRA | SG-CRA-049 + SG-CRA-050 + SG-CRA-051 + SG-CRA-052 | OSS steward cybersecurity policy; manufacturer policies/processes/procedures; presumption of conformity via harmonised standards / common specs / CSA certification (Art. 13(8), Art. 24, Art. 27). | Product-level policy framework + standards-presumption machinery. |
| DORA | SG-DORA-016 + SG-DORA-017 | Management body defines/approves/oversees/implements ICT risk management framework; three-lines-of-defence + asset identification (Art. 5(2), Art. 6(1)/(4), Art. 7(1)). | Financial-entity ICT risk management framework; three-lines-of-defence as governance anchor. |
| AI_Act | SG-AIACT-007 + SG-AIACT-010 + SG-AIACT-011 | Transparency to deployers; QMS with 13 enumerated aspects; deployer measures aligned with instructions (Art. 13, Art. 17, Art. 26). | AI-system-specific policies via QMS; transparency-as-policy. |
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
- **Five-policy-stack with no OJ-level consolidation rule**: D-09.1 is the most heavily-overlapped sub-domain. GDPR (data-protection policy + DPO), NIS 2 (governance + 3 policies), CRA (manufacturer policies + presumption of conformity), DORA (ICT risk management framework + three-lines-of-defence), AI Act (QMS + transparency). All five apply simultaneously to a DORA financial entity that processes personal data and ships AI-enabled CRA-regulated products. There is no OJ-level consolidation rule. Phase 1 entities must build a governance-architecture mapping that nests all five policies without overlap. Recommend Layer 1 cross-cutting analysis.
- **DPO (GDPR) vs. management body (NIS 2 / DORA)**: GDPR's DPO is a designated individual with Art. 39(1) tasks; NIS 2 / DORA's management body is the corporate governance body with collective approve/oversee/liable obligations. The DPO reports to the management body but is not a member of it (Art. 38(6) conflict-of-interests). The interplay between the DPO's advisory role and the management body's liability exposure is unresolved at the OJ level.
- **Presumption of conformity (CRA Art. 27) does not extend cross-regulation**: CRA presumption of conformity via harmonised standards discharges the CRA conformity-assessment obligation only. It does not substitute for the GDPR Art. 24 appropriate-measures obligation, NIS 2 Art. 21(2)(a) policy obligation, or DORA Art. 6(1) ICT risk management framework. Phase 1 entities must discharge each regime's policy obligation separately even when the underlying product is CRA-conformant.
<!-- /emergent -->
##### SR cross-validation
All 5 regulations map D-09.1 to the NIST CSF 2.0 Subcategory **GV.PO-01** (Organizational cybersecurity policy established, communicated, enforced) as the convergent anchor. DORA additionally maps **GV.RR-02** (Roles/responsibilities/accountabilities established) for the three-lines-of-defence architecture; GDPR additionally maps **GV.RM-04** (Strategic direction for risk response) for the data-protection-policy anchor; NIS 2 additionally maps **GV.OV-01** (Risk management strategy outcomes reviewed) for the management-body-oversight dimension.
##### Downstream implication
Phase 1 entities must implement five policy artefacts (or a consolidated policy that nests all five). The Layer 1 governance-architecture mapping is required. The DPO role (GDPR) and the management body (NIS 2 / DORA) must be reconciled in the corporate-governance charter. AI Act QMS becomes a sub-policy. CRA presumption of conformity is the upstream gate for CRA-conformant products but does not discharge cross-regulation obligations.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-09.1
title: D-09.1 Information Security Policies — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.1 Information Security Policies
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-09_Governance-Documentation/D-09.1.md
status: DRAFT
---
> **Domain analysis:** [D-09.1 Information Security Policies](../../DomainAnalysis/D-09_Governance-Documentation/D-09.1.md)
#### D-09.1 Information Security Policies
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act
**Critical note (CRDA flag):** D-09.1 is the most heavily-overlapped sub-domain. All 5 regulations overlap with distinct policy artefacts and no OJ-level consolidation rule.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
