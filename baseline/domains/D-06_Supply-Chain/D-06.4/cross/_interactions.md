# D-06.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-06.4 Third-Party Boundary Management](../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.4.md)
#### D-06.4 Third-Party Boundary Management
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.4 per AEGIS taxonomy §4.1. DORA and NIS 2 are sole authorities for third-party-boundary architecture.

## Part 1 §1 — Cross-Regulation Analysis context

### Summary statistics
| Metric | Value |
|---|---|
| Sub-domains covered | 8 (D-05.1–D-05.4, D-06.1–D-06.4) |
| Pair analyses produced | **25** |
| Pairs classified as CONTRADICTORY in CRDA | 4 |
| Pairs corrected from CRDA | **4** |
| Sole-authority sub-domains | 2 (D-05.4 GDPR, D-06.2 CRA) |
| 2-reg sub-domain | D-05.3 (1 pair) |
| 3-reg sub-domains | D-05.1, D-05.2 (3 pairs each) |
| 4-reg sub-domains | D-06.1, D-06.3, D-06.4 (6 pairs each) |
#### Distribution of verified relationship taxonomy
| Relationship type | Count | Sub-domains |
|---|---|---|
| EQUAL | 4 | D-06.1 NIS2↔DORA; D-06.3 NIS2↔DORA; D-06.4 GDPR↔CRA; (NIS2↔DORA also COMPLEMENTARY at D-06.4) |
| COMPLEMENTARY | 11 | D-05.1 (3); D-05.2 (1 corrected + 1); D-05.3 (1); D-06.1 (3); D-06.3 (2 corrected + 1); D-06.4 (2) |
| DIFFERENT-PERSPECTIVE | 7 | D-05.2 (1); D-06.1 (3); D-06.3 (2); D-06.4 (3) |
| CONTRADICTORY | 0 | (none confirmed — see P0 disagreement report) |
| SCOPE-DISJOINT | 2 | D-05.1 GDPR↔AI_Act (corrected from CONTRADICTORY); D-05.2 GDPR↔CRA (corrected from CONTRADICTORY) |
---
### Summary table (corrections vs CRDA)
| Sub-domain | Pair | CRDA classification | Verified classification | Reason for change |
|---|---|---|---|---|
| D-05.1 | GDPR ↔ AI_Act | CONTRADICTORY (special-category) | **SCOPE-DISJOINT** | AI Act Art. 10(5) is a conditional carve-out to GDPR Art. 9(1), not a contradiction of GDPR Art. 5(1)(c). The pair only overlaps for the narrow 6-condition bias-correction scenario; in baseline the pair is scope-disjoint. CRDA reasoning itself concedes the carve-out framing — the "contradictory" label is internally inconsistent. |
| D-05.2 | GDPR ↔ CRA | CONTRADICTORY (direction) | **SCOPE-DISJOINT** | GDPR Art. 5(1)(e) caps personal-data retention; CRA Annex I Part II (7)/(8) requires update-artefact availability. Different data classes (personal data vs update artefacts), different actors (controller vs manufacturer), different triggers (retention vs availability). CRDA reasoning itself concedes the axes are disjoint — the "contradictory" label is internally inconsistent. |
| D-05.2 | GDPR ↔ AI_Act | CONTRADICTORY (direction) | **COMPLEMENTARY** (floor-within-ceiling) | GDPR Art. 5(1)(e) is qualitative ceiling; AI Act Art. 19(1) is 6-month minimum floor. The two reconcile within the intersection [6 months, "necessary"] — the textbook floor-within-ceiling pattern, which is COMPLEMENTARY not CONTRADICTORY. CRDA reasoning itself states: "The two are reconcilable". |
| D-06.3 | GDPR ↔ DORA | CONTRADICTORY (overlap) | **COMPLEMENTARY** (clause-list union) | GDPR Art. 28(3) has 8 mandatory elements; DORA Art. 30(2) has 9 minimum elements. The two lists overlap but are not identical — the union is the operative rule when the financial entity is also a controller. CRDA reasoning itself acknowledges this: "the contract must satisfy both sets" — which is the textbook union pattern. The "contradictory" label is scope-incorrect. |
(4 corrections in total: 3 from CONTRADICTORY → SCOPE-DISJOINT or COMPLEMENTARY; the CRDA file remains untouched.)
---
### P0 disagreement report
#### Disagreement 1: The CRDA "contradictory" label is over-applied in D-05 + D-06
**Concern:** The CRDA file marks 4 pairs as "contradictory" in D-05 + D-06 (GDPR↔AI_Act D-05.1; GDPR↔CRA D-05.2; GDPR↔AI_Act D-05.2; GDPR↔DORA D-06.3). On OJ-text verification, none of these is a true contradiction — each is either scope-disjoint (the regulations address different data classes / actors / triggers) or complementary (one sets a ceiling, the other a floor; one sets a clause list, the other a clause list). The CRDA reasoning itself frequently concedes this internally ("regulatory carve-out", "not on the same axis", "the two are reconcilable", "the contract must satisfy both sets") while keeping the contradictory label.
**Why this matters:** A "contradictory" label drives Phase 2 obligation derivation toward a reconciliation clause that says "if both apply, the stricter wins" — which is wrong when the pair is scope-disjoint (no overlap means no conflict) or genuinely complementary (both apply simultaneously and additively). The P2 obligation table will inherit the over-classification and produce either false conflicts (scope-disjoint) or under-built union rules (complementary).
**Recommendation to Orchestrator / Validator:** Correct the 4 labels in the CRDA file per the Summary table above. Specifically: change D-05.1 GDPR↔AI_Act to **scope-disjoint** (with Art. 10(5) carve-out annotation); change D-05.2 GDPR↔CRA to **scope-disjoint**; change D-05.2 GDPR↔AI_Act to **complementary**; change D-06.3 GDPR↔DORA to **complementary** (with clause-list union rule).
#### Disagreement 2: The CRDA does not distinguish "EQUAL (different objects)" from "EQUAL (same object)"
**Concern:** The CRDA marks 3 pairs as EQUAL in D-05 + D-06, but the three pairs are not equivalent in form. NIS 2↔DORA on D-06.1 and D-06.3 is *same-object* equality (DORA's four-factor test or 9-element list operationalises NIS 2's open-texture chapeau); GDPR↔CRA on D-06.4 is *different-object* equality (the same form — written EU-side representative — applied to different objects: data-protection representative vs product-compliance AR). Phase 2 obligation derivation should treat these differently: same-object equality means single control satisfies both; different-object equality means the two representatives co-exist.
**Recommendation to Orchestrator / Validator:** Annotate the CRDA EQUAL pairs with a sub-flag for same-object vs different-object. Phase 2 obligation derivation should then use single-control vs dual-control derivation rules accordingly.
#### Disagreement 3: The CRDA does not annotate "Conditional" overlap
**Concern:** Several pairs are Conditional — they overlap only on specific factual circumstances. The CRDA's 4-way taxonomy does not capture this. Phase 2 obligation derivation will apply unconditional derivation rules and produce obligation statements that either over-claim (saying both regulations always apply when they only sometimes do) or under-claim (saying they only sometimes apply when they almost always do in practice).
**Recommendation to Orchestrator / Validator:** Annotate each CRDA pair with a Conditional flag where applicable. For D-05 + D-06 the following pairs are Conditional in scope-disjoint sense: D-05.1 GDPR↔CRA (Y when CRA product processes personal data); D-05.1 GDPR↔AI_Act (Y only for the narrow Art. 10(5) carve-out scenario); D-05.2 GDPR↔CRA (Y when CRA update-distribution log contains personal data); D-06.1 GDPR↔CRA (Y when controller deploys CRA product); D-06.1 NIS2↔CRA (Y when deployer is entity and manufacturer supplies CRA product); D-06.3 NIS2↔CRA (Y when NIS 2 entity deploys CRA product); D-06.4 GDPR↔CRA (Y when non-EU entity is both GDPR controller and CRA manufacturer); D-06.4 GDPR↔DORA (Y when non-EU ICT provider is critical/important for financial entity); D-06.4 NIS2↔CRA (Y when NIS 2 entity deploys CRA product substantially modified by third party).
---
### Quality flags
| Flag | Severity | Notes |
|---|---|---|
| **SR-AIACT-008 T5 mapping error** | Cosmetic | AI_Act validation report v0.1 §3.4 / §6 flags T5 citation of Art. 12(4) (which does not exist in the OJ); substance is in Art. 19(1). Used OJ-literal locus at Art. 19(1) in this analysis. |
| **SR-DORA-021 Art. 30(2) gloss** | Material | DORA validation report v0.2 F-10 flags audit rights and exit strategies misattributed from Art. 30(3). Used OJ-literal 9-element list at Art. 30(2) in this analysis. |
| **SR-CRA-050 `due diligence` VAG+POLY-S3** | Cosmetic | R3 (procedural + substantive) reading chosen; alternative R1 (procedural only) and R2 (substantive only) preserved. |
| **SR-NIS2-020 `direct` SCOPE-Q S3** | Material | Three materially distinct readings (R1 Tier-1 / R2 technically integrated / R3 operationally dependent). R1 chosen as minimum; R2 and R3 to be considered per Recital 56. Member State transposition divergence noted (BSI favours R1+R3; ANSSI favours R2+R3). |
| **CRA 10-year tail interpretive** | Cosmetic | CRDA reads "10-year update-availability tail" from Annex II Art. 13(18) + Art. 13(8); OJ-literal anchor is the 5-year support-period minimum + 10-year Annex II information accessibility. |
| **DORA Art. 28(5) standards POLY** | Material | DORA validation report v0.2 §3.5 flags the open-naming question. Reading chosen: entity-selected standards with supervisory-recognised standards (ISO/IEC 27001, SOC 2, NIST CSF, EBA Guidelines) as the EU-acceptable floor. |
| **GDPR Art. 30(1)(f) `where possible` hedge** | Cosmetic | GDPR deduction audit v0.1 F-6 flags the hedge dropped in SR-GDPR-029. Used OJ-literal text with hedge in this analysis. |
---
### Chain metadata
| Field | Value |
|---|---|
| Total pair analyses | **25** |
| Classification corrections from CRDA | **4** |
| P0 disagreements raised | **3** |
| Quality flags surfaced | **7** (1 material, 2 cosmetic, plus 4 cross-cutting) |
| Methodology | 5-class taxonomy (EQUAL / COMPLEMENTARY / CONTRADICTORY / DIFFERENT-PERSPECTIVE / SCOPE-DISJOINT) + scope-disjoint test |
| CRDA file status | **Unchanged** (this analysis is staging; corrections are recommendations for the Validator) |
| Phase 1C Doc 07 implications | Documented per pair in `Downstream implication (1-2 sentences)` blocks |
---
---
document_id: AEGIS-PREPROC-STAGE-CRDA-DEEP-PART-D
title: "Cross-Regulation Deep Analysis — Part D (D-07 + D-08 + D-09 + D-10)"
phase: "Pre-processing (Regulatory Baseline) — per-pair OJ-text verification"
version: 0.1
created: 2026-07-09
updated: 2026-07-09
author: "Executor D (sub-agent)"
status: DRAFT
chain_version: v2.1
related_documents:
  - ../../_archive/00_CrossRegulation_Domain_Analysis.md
  - ../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../Regulation/AI_Act/02_SecurityRules_NIST.md
inputs:
  - 5 × 01_SecurityObjectives.md
  - 5 × 02_SecurityRules_NIST.md
  - ../../_archive/00_CrossRegulation_Domain_Analysis.md
scope: D-07 (Secure Development, 4 sub-domains) + D-08 (Human Factors, 3 sub-domains) + D-09 (Governance & Documentation, 4 sub-domains) + D-10 (Monitoring & Audit, 3 sub-domains) = 14 sub-domains, 91 pair analyses
purpose: Per-pair OJ-text deep analysis verifying the CRDA pairwise classifications using the scope-disjoint test and the 5-option relationship taxonomy. CRDA is NOT modified by this analysis; findings are recommendations for the Validator and Orchestrator.
---
## Cross-Regulation Deep Analysis — Part D (D-07 + D-08 + D-09 + D-10)
### Methodology
#### Scope-disjoint test (the operational pivot)
For each pair (A, B) classified in CRDA, the test asks: **does A's triggering event overlap with B's triggering event at a single regulated party (controller / manufacturer / financial entity / deployer / provider / NSIE / essential entity) on a single occasion?**
- **Yes** → pair overlaps on the same real-world event; CRDA's substantive classification (equal / complementary / contradictory / different-perspective) is informative.
- **No** → pair's triggering events address **distinct objects at distinct actors**; the regulations do not actually impose obligations on the same party on the same occasion. The CRDA classification is then a *taxonomy* artifact (two rules happen to map to the same AEGIS sub-domain) rather than a *substantive* relationship. In this case the correct substantive classification is **SCOPE-DISJOINT**.
- **Conditional** → the pair overlaps only under specific factual circumstances; the label is correct in baseline only if the case company matches those circumstances.
#### 5 relationship classes
| Class | Test | When it applies (Part D examples) |
|---|---|---|
| **EQUAL** | Same scope/angle, same triggering event, same addressee | NIS 2 ↔ DORA on change management (D-07.4); NIS 2 ↔ DORA on risk analysis (D-09.2); NIS 2 ↔ DORA on monitoring (D-10.1); NIS 2 ↔ DORA on management-body training (D-08.3); NIS 2 ↔ DORA on awareness (D-08.1); NIS 2 ↔ DORA on testing (D-10.3) |
| **COMPLEMENTARY** | Different scope/angle but both apply on the same event | GDPR ↔ NIS 2 on by-design (D-07.1); GDPR ↔ DORA on monitoring (D-10.1); CRA ↔ DORA on risk assessment (D-09.2) |
| **DIFFERENT-PERSPECTIVE** | Same object but distinct regulatory framing | GDPR ↔ CRA on training (D-08.1, workforce vs. user); NIS 2 ↔ CRA on training (D-08.1, workforce vs. integrator); CRA ↔ DORA on awareness (D-08.1, user-instructions vs. staff modules) |
| **CONTRADICTORY** | Mutually exclusive requirements on a single event | None found in D-07 to D-10 in baseline classification |
| **SCOPE-DISJOINT** | Different objects, different actors, different triggers | GDPR ↔ CRA on asset inventories (D-09.3, personal data vs. ICT assets); CRA ↔ AI Act on testing (D-10.3, conformity assessment vs. AI risk-management testing); CRA user-instructions vs. internal staff awareness (D-08.1) |
#### Verbatim OJ text sourcing
Verbatim text is taken from the per-regulation `02_SecurityRules_NIST.md` files (`regulatory_rationale` field of each SR, with the SR's own `source_clauses.article_ref` confirming the OJ locus). Where the OJ passage is long, the operative phrase is reproduced; the article-ref footnote points to the full article. Article text not directly quoted in a SR is drawn from the corresponding `01_SecurityObjectives.md` `source_clauses` list.
#### Relationship to CRDA
CRDA classifies pairs on a 4-way taxonomy (equal / complementary / contradictory / different-perspective). This deep analysis keeps CRDA's labels but **adds** the scope-disjoint test. Where CRDA labeled a pair "complementary" or "different-perspective" but the scope-disjoint test shows the pair cannot both bind the same party on the same occasion, the verified relationship is **SCOPE-DISJOINT** (or **COMPLEMENTARY** if the floor-within-ceiling pattern applies). The CRDA file itself is not modified by this pilot — corrections are listed in the summary table at the end for the Validator's downstream action.
#### Frontmatter chain
This file is part of the CRDA-deep pilot chain:
- Part A (`_STAGING_crda_deep_part_A.md`) — D-01 + D-02
- Part B (`_STAGING_crda_deep_part_B.md`) — D-03 + D-04
- Part C (`_STAGING_crda_deep_part_C.md`) — D-05 + D-06
- Part D (this file) — D-07 + D-08 + D-09 + D-10
- Subsequent parts — D-11 onwards
#### Part D coverage
- 14 sub-domains: D-07.1, D-07.2, D-07.3, D-07.4, D-08.1, D-08.2, D-08.3, D-09.1, D-09.2, D-09.3, D-09.4, D-10.1, D-10.2, D-10.3.
- 91 pair analyses (CRDA-omitted pairs included with explicit "not classified by CRDA" annotation).
- Zero "contradictory" classifications in CRDA for D-07 to D-10; the P0 concern (Part C: contradictory classifications that are scope-incorrect) does not surface here, but the scope-disjoint test still surfaces several pairs where CRDA labelled them "complementary" or "different-perspective" when they are substantively scope-disjoint.
---
### D-07 Secure Development
---

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-06.4 Third-Party Boundary Management
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md`](../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.4.md)
> (6 pairs verified against OJ text — **4 of 5 participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope per AEGIS taxonomy §4.1**).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-06.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-023 | Non-EU controllers/processors falling under Art. 3(2) designate a representative in writing in the Union, subject to narrow occasional/low-risk/public-authority exceptions | Legal-address anchor for non-EU personal-data actors; DPA/data-subject-facing representative |
| NIS2 | SO-NIS2-012; SO-NIS2-014 (partial); SO-NIS2-016 (partial) | Cross-MS notification routing through CSIRTs/competent authorities/SPOCs/ENISA; direct-supplier scope-limiter and EU-level supply-chain-risk propagation provide entity-boundary hooks | Entity-level boundary and cross-border information flow; Member-State-transposition-sensitive |
| CRA | SO-CRA-041; SO-CRA-042; SO-CRA-043; SO-CRA-044 | Non-EU manufacturer authorised representative; importer/distributor manufacturer-equivalent trigger; third-party substantial-modification trigger; economic-operator identification and 10-year retention | Product-compliance boundary; MSA-facing authorised representative and supply-chain traceability |
| DORA | SO-DORA-012 (partial) | Financial entities and competent authorities have unrestricted access, inspection, and audit rights over critical ICT third-party providers, with narrowly bounded alternative assurance where other clients' rights are affected | Financial-entity audit-rights boundary over CIF-supporting ICT providers |

## Validated relationships (from CRDA-deep §D-06.4)

#### Validated relationships (from CRDA-deep §D-06.4)
Of 6 pairs, **6 verified as SAME**: 2 COMPLEMENTARY, 1 EQUAL (different objects), and 3 DIFFERENT-PERSPECTIVE. There are **no CORRECTED, no CONTRADICTORY, and no verified conflict pairs** in D-06.4. Several pairs are **N in baseline** under the scope-disjoint test because the mechanisms are different; CRDA-deep preserves the SAME taxonomy label because they layer into a common third-party-boundary architecture when the factual overlap exists.
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR Art. 27 creates an EU legal-address representative for non-EU controllers/processors. NIS 2 Art. 23(6)/(8) routes notifications across Member States and ENISA through CSIRTs, competent authorities, and SPOCs. Different mechanisms, but both matter when a non-EU controller operates across multiple Member States and incidents cross borders.
- **GDPR ↔ CRA** — EQUAL (SAME, different objects): GDPR Art. 27 and CRA Art. 18 both require a written EU-side representative for non-EU actors, but the objects differ. GDPR uses a data-protection representative; CRA uses a product-compliance authorised representative with a non-delegable-obligations carve-out. Both representatives coexist where the same non-EU entity is both a non-EU controller/processor and a CRA manufacturer.
- **GDPR ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME): GDPR Art. 27 is a legal-address obligation; DORA Art. 30(3)(e) is an access/inspection/audit-rights obligation for CIF-supporting ICT third-party contracts. They overlap conditionally when a non-EU ICT provider is critical or important for a financial entity and is also within GDPR Art. 3(2).
- **NIS2 ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): NIS 2 `direct` supplier scope determines who the entity is liable for; CRA Art. 22/23 determines who becomes the manufacturer after substantial modification and who must identify upstream/downstream economic operators. Conditional overlap exists when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party.
- **NIS2 ↔ DORA** — COMPLEMENTARY (SAME) (DORA exceeds NIS 2): NIS 2 limits entity-side supply-chain scope through `direct` supplier/service-provider relationships; DORA Art. 30(3)(e) audit rights extend into critical ICT third-party providers and may reach beyond direct providers through the critical provider chain. Where a financial entity is also a NIS 2 entity, DORA provides the sharper audit-rights layer.
- **CRA ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME): CRA Art. 23 creates an economic-operator identification duty and 10-year traceability record; DORA Art. 30(3)(e) creates financial-entity/competent-authority audit rights. They point in different directions but compose where a CRA-classified product is supplied to a financial entity through an economic-operator chain.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Conditional (N in baseline: legal representative vs SPOC routing; Y when non-EU controller operates across multiple MS and an incident route crosses borders) | Y (same non-EU entity can be both GDPR controller/processor and CRA manufacturer; two written EU-side representatives or mandates coexist) | Conditional (N in baseline: legal-address vs audit rights; Y when non-EU ICT provider is critical/important for financial entity and also falls under GDPR Art. 3(2)) |
| **NIS2** | Conditional (same as GDPR↔NIS2) | — | Conditional (N in baseline: direct supplier scope vs third-party substantial modification; Y when NIS 2 deployer uses CRA product substantially modified by third party) | Y (financial entity is also NIS 2 entity; DORA audit rights extend beyond NIS 2 direct-supplier floor) |
| **CRA** | Y (same non-EU entity; different objects/mandates) | Conditional (same as NIS2↔CRA) | — | Conditional (N in baseline: economic-operator identification vs financial-entity audit rights; Y when CRA product is supplied to financial entity through importer/distributor chain) |
| **DORA** | Conditional (same as GDPR↔DORA) | Y (same financial-entity supplier relationship; DORA exceeds NIS 2 audit-rights layer) | Conditional (same as CRA↔DORA) | — |
Legend: **Y** = scope overlap on a single event at a single party. **Conditional** = overlap only under specific factual circumstances. **N in baseline** = distinct mechanisms, actors, or directions; the high-level SO still records the pair so Phase 1C can build a representative/rights matrix without falsely merging duties.

## Cross-recipient map

#### Cross-recipient map
D-06.4 creates recipient fragmentation at the **third-party-boundary** layer. **GDPR** uses the Union representative as the DPA/data-subject legal-address anchor for non-EU controllers/processors. **NIS 2** routes significant incident information through CSIRTs, competent authorities, SPOCs, ENISA, and other affected Member States. **CRA** uses the authorised representative, economic operators, and market surveillance authorities to maintain EU-side product-compliance accountability and 10-year supply-chain traceability. **DORA** creates direct contractual rights for the financial entity and competent authority to access, inspect, audit, and copy relevant documentation for critical ICT third-party providers.
---

## HSO considerations (from D-06.4.0 — High-level SecurityObjective)

**Considerations.**
- Four participating regulations (GDPR, NIS 2, CRA, DORA) anchor different mechanisms: GDPR anchors non-EU personal-data actors through a written Union representative; NIS 2 anchors entity-level supplier boundaries and cross-MS notification routing; CRA anchors product-compliance accountability through authorised representatives, manufacturer-equivalent triggers, third-party substantial-modification rules, and 10-year economic-operator traceability; DORA anchors financial-entity and competent-authority access, inspection, and audit rights over critical ICT third-party providers.
- CRDA-deep verified relationships (6 pairs, all SAME: 2 COMPLEMENTARY + 1 EQUAL with different objects + 3 DIFFERENT-PERSPECTIVE; no CORRECTED, no CONTRADICTORY).
- The high-level SO does not collapse these mechanisms — it builds a boundary matrix showing which representative, route, traceability record, or audit right applies in each factual scenario.
- The 1 conditional emergent tension (four-party boundary architecture — GDPR representative + CRA authorised representative + NIS 2 cross-MS routing + DORA CIF audit rights at the same time on a non-EU provider) is regulated by role-and-recipient allocation rather than by collapsing boundary mechanisms.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
| Axis (reg) | Target object | Trigger | Boundary instrument | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | non-EU controller/processor under Art. 3(2) | offering goods/services to EU data subjects or monitoring behaviour, unless Art. 27(2) exception applies | written Union representative designation | DPA; data subjects; representative | Art. 27(1)/(2) |
| **NIS2** | cross-border incident flow and direct supplier/service-provider boundary | significant incident with two or more affected Member States; direct supplier/service-provider relationship | SPOC forwarding; CSIRT/competent-authority routing; supplier-scope register | SPOC; ENISA; affected Member States; CSIRT/competent authority | Art. 23(6); Art. 23(8); Art. 21(2)(d) |
| **CRA** | non-EU manufacturer, importer/distributor/modifier, and economic-operator chain | written AR mandate; own-name placement; substantial modification; MSA reasoned request | authorised representative mandate; manufacturer-equivalent status; substantial-modification record; 10-year identification log | MSA; manufacturer; economic operators | Art. 18; Art. 21; Art. 22; Art. 23 |
| **DORA** | CIF-supporting ICT third-party provider | contractual arrangement concerning critical or important function | unrestricted access/inspection/audit rights; on-site documentation copy right; alternative-assurance exception | financial entity; competent authority; appointed third party | Art. 30(3)(e)(i)/(ii) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
| | GDPR | NIS 2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Conditional (N in baseline: legal representative vs SPOC routing; Y when non-EU controller operates across multiple MS and an incident route crosses borders) | Y (same non-EU entity can be both GDPR controller/processor and CRA manufacturer; two written EU-side representatives or mandates coexist) | Conditional (N in baseline: legal-address vs audit rights; Y when non-EU ICT provider is critical/important for financial entity and also falls under GDPR Art. 3(2)) |
| **NIS 2** | Conditional (same as GDPR↔NIS2) | — | Conditional (N in baseline: direct supplier scope vs third-party substantial modification; Y when NIS 2 deployer uses CRA product substantially modified by third party) | Y (financial entity is also NIS 2 entity; DORA audit rights extend beyond NIS 2 direct-supplier floor) |
| **CRA** | Y (same non-EU entity; different objects/mandates) | Conditional (same as NIS2↔CRA) | — | Conditional (N in baseline: economic-operator identification vs financial-entity audit rights; Y when CRA product is supplied to financial entity through importer/distributor chain) |
| **DORA** | Conditional (same as GDPR↔DORA) | Y (same financial-entity supplier relationship; DORA exceeds NIS 2 audit-rights layer) | Conditional (same as CRA↔DORA) | — |
Legend: **Y** = scope overlap on a single event at a single party. **Conditional** = overlap only under specific factual circumstances. **N** = scope-disjoint in baseline.
(See the validated-relationships table above for the per-cell notes.)

## Scope-overlap principle (operational)

#### Scope-overlap principle (operational)
The high-level SO (`SO-D-06.4.HL`) engages when ≥2 participating regulations apply to the same boundary scenario. The clearest dual-representative scenario is a non-EU manufacturer of a CRA-classified product that also controls or processes personal data of EU data subjects: GDPR Art. 27 and CRA Art. 18 both apply, but the mandates differ and must not be merged. The clearest audit-boundary scenario is a financial entity that is also a NIS 2 entity and depends on a critical ICT third-party provider: NIS 2 defines the direct-supplier boundary and DORA adds unrestricted audit/access rights over the CIF provider. CRA joins where a product is supplied through an economic-operator chain or substantially modified by a third party.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate: GDPR, NIS 2, CRA, DORA. AI Act is out-of-scope for D-06.4 per AEGIS taxonomy §4.1.
- All 6 pairs are verified as **SAME** in CRDA-deep; no pair is corrected or contradictory.
- The verified relationship mix is: 2 COMPLEMENTARY (GDPR↔NIS2; NIS2↔DORA), 1 EQUAL (GDPR↔CRA, different objects), and 3 DIFFERENT-PERSPECTIVE (GDPR↔DORA; NIS2↔CRA; CRA↔DORA).
- The high-level SO describes the **COMMON OBJECTIVE**: explicit third-party-boundary allocation across representatives, routing, supplier scope, substantial-modification accountability, traceability, and audit rights.
- The **single emergent tension** is the **four-party boundary architecture**: a multi-regulated non-EU or cross-border supply chain may need multiple representatives, an entity-side direct-supplier register, a CRA manufacturer-equivalence decision, and DORA CIF audit rights at the same time.
- Baseline scope-disjoint facts are preserved: many pairs are N in baseline because they use distinct mechanisms, but they become operationally relevant at the multi-regulation intersection.
---

## Emergent tensions (from CRDA-deep §D-06.4)

#### Emergent tensions (from CRDA-deep §D-06.4)
**1 conditional emergent tension**: the **four-party boundary architecture**. A non-EU provider or manufacturer may simultaneously require a GDPR Union representative, a CRA authorised representative, NIS 2 cross-MS routing and direct-supplier boundary treatment, and DORA audit/access rights if it supplies critical ICT services to a financial entity. The tension is not a contradiction; it is an allocation problem. Phase 1C must preserve the four mechanisms in a boundary matrix rather than merging them into one generic `third-party contact` or `supplier owner` field.
The GDPR↔CRA EQUAL pair requires special treatment: it is **EQUAL in form** (written EU-side representative) but **different in object** (data-protection representative vs product-compliance authorised representative). A single legal entity may perform both roles only if both mandates and recipient channels are separately documented; otherwise two representatives or two mandates coexist.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in D-06.4 must maintain a representative/rights matrix keyed by third-party role, jurisdiction, service/product criticality, modification status, and incident-routing scope. For a non-EU SaaS manufacturer that processes EU personal data and supplies a critical ICT service to a financial entity, the matrix includes GDPR Art. 27 representative designation, CRA Art. 18 authorised representative and Art. 23 traceability, DORA Art. 30(3)(e) audit rights, and NIS 2 cross-MS routing if incident impact reaches multiple Member States. The one emergent tension is resolved by role-and-recipient allocation, not by collapsing boundary mechanisms.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-06.4 Third-Party Boundary Management — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md`. See that file for cross-reg verified relationships (6 pairs: 6 SAME — no CORRECTED, no CONTRADICTORY — 2 COMPLEMENTARY + 1 EQUAL (different objects) + 3 DIFFERENT-PERSPECTIVE), scope overlap matrix, Objective/Considerations content, the 1 emergent tension (the four-party boundary architecture — GDPR Union representative + CRA authorised representative + NIS 2 cross-MS routing and direct-supplier scope + DORA CIF audit/access rights at the same time on a non-EU provider or critical ICT service), the GDPR↔CRA EQUAL (different objects) special treatment (EQUAL in form but data-protection representative vs product-compliance authorised representative; a single legal entity may perform both roles only if both mandates and recipient channels are separately documented), and the role-and-recipient allocation principle (NOT collapsing boundary mechanisms into one generic `third-party contact` or `supplier owner` field). **Scope-title note (P0):** the index.md row used the placeholder `D-06.4 Concentration Risk (PENDING Batch 11)` label; this file uses the CRDA-deep source-of-truth title `D-06.4 Third-Party Boundary Management` per Batch 11 critical-rule #6 + #8 (the Batch 12 HSO file already documented the divergence — this is notably NOT a concentration-risk sub-domain per CRDA-deep source-of-truth; concentration-risk appears as one DORA Art. 28(4) limb within D-06.3 DORA rather than as the title of D-06.4). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1). CRDA-deep verified 6 pairs as **6 SAME** (no CORRECTED, no CONTRADICTORY; 2 COMPLEMENTARY + 1 EQUAL (different objects) + 3 DIFFERENT-PERSPECTIVE). The four regulators anchor distinct boundary mechanisms: GDPR anchors non-EU personal-data actors through a written Union representative (Art. 27(1)/(2)) unless an Art. 27(2) exception applies; NIS 2 anchors entity-level supplier boundaries (Art. 21(2)(d) `direct` scope-limiter) and cross-MS notification routing (Art. 23(6)/(8) through CSIRTs / competent authorities / SPOCs / ENISA); CRA anchors product-compliance accountability through authorised representatives (Art. 18 written mandate), manufacturer-equivalent triggers (Art. 21 own-name/trademark), substantial-modification rules (Art. 22 third-party modification), and 10-year economic-operator traceability (Art. 23 upstream/downstream identification record); DORA anchors financial-entity and competent-authority access / inspection / audit rights over critical ICT third-party providers (Art. 30(3)(e)(i)/(ii) with narrowly bounded alternative-assurance exception). The 1 emergent tension is the **four-party boundary architecture** — a multi-regulated non-EU or cross-border supply chain may require multiple representatives, an entity-side direct-supplier register, a CRA manufacturer-equivalence decision, and DORA CIF audit rights at the same time. The high-level SO does NOT collapse these mechanisms; it builds a boundary matrix showing which representative, route, traceability record, or audit right applies in each factual scenario.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 6.4
  volere_section: 15
  volere_subtype: audit
  title: "Third-party boundary responsibilities are explicitly allocated across EU Union representatives, NIS 2 cross-MS routing + direct-supplier scope, CRA authorised representative + manufacturer-equivalent + substantial-modification + 10-year economic-operator records, and DORA CIF audit/access rights — role-and-recipient matrix without collapsing mechanisms"
  derives_from:
    hso_sub_so: SO-D-06.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.4.md
    objective_ref_section: "### D-06.4.0"
  description: |
    The product shall explicitly allocate third-party boundary responsibilities across the four boundary mechanisms — GDPR Art. 27(1)/(2) written Union representative for non-EU controllers/processors (unless Art. 27(2) exception applies); NIS 2 Art. 23(6)/(8) cross-MS notification routing via CSIRTs / SPOCs / ENISA plus Art. 21(2)(d) `direct` supplier/service-provider scope-limiter; CRA Art. 18 written authorised representative mandate + Art. 21 own-name/trademark manufacturer-equivalent + Art. 22 third-party substantial-modification manufacturer-status + Art. 23 10-year upstream/downstream economic-operator identification log; DORA Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights for the financial entity, appointed third party, and competent authority over critical ICT third-party providers (with narrowly bounded alternative-assurance exception) — preserving each mechanism's role / recipient / record instrument and avoiding collapse into a generic `third-party contact` or `supplier owner` field.
  fit_criterion: |
    A 4-axis representative / rights / traceability / routing boundary matrix is maintained keyed by third-party role / jurisdiction / service-or-product criticality / modification status / incident-routing scope, with explicit boundary-mechanism separation (GDPR-art-27-written-Union-representative / NIS2-art-236-art-238-cross-MS-SPOC-routing + art-212d-direct-supplier-scope-register / CRA-art-18-AR-mandate + art-21-importer-or-distributor-own-name-trigger + art-22-substantial-modification-record + art-23-10-year-economic-operator-identification-log / DORA-art-303ei-ii-unrestricted-access-inspection-audit-rights) and documented cross-mechanism hand-offs at boundary intersections; each axis records (a) target object (non-EU controller-or-processor / cross-border incident flow / non-EU manufacturer or substantial modifier / CIF-supporting ICT third-party), (b) trigger gate (offering-goods-or-services-or-monitoring-Art-32 / significant-incident-2-MS-or-more-or-direct-supplier-relationship / written-AR-mandate-or-own-name-placement-or-substantial-modification-or-MSA-reasoned-request / CIF-supporting-contractual-arrangement), (c) record instrument (written-Art-27-representative-designation / SPOC-forwarding + CSIRT-or-competent-authority-routing + supplier-scope-register / AR-mandate + manufacturer-equivalent-status + substantial-modification-record + 10-year-economic-operator-identification-log / unrestricted-access-inspection-audit-rights-framework + on-site-documentation-copy-right + alternative-assurance-exception-when-other-clients-rights-affected), and (d) recipient (DPA-or-data-subjects / SPOC-or-ENISA-or-affected-MS-or-CSIRT-or-competent-authority / MSA-or-manufacturer-or-economic-operators / financial-entity-or-competent-authority-or-appointed-third-party); the four-party boundary architecture emergent tension is resolved by role-and-recipient allocation rather than by collapsing boundary mechanisms; verified by boundary-matrix documentation review + per-axis written-mandate inspection + cross-MS-routing-record review + 10-year economic-operator-identification-log spot-check + CIF audit-rights-framework signed-attestation review + DPA/SPOC/MSA/national-financial-supervisory-authority-or-competent-authority inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: [6.3 (contractual-security matrix provides the contractual substrate that legitimises audit-rights invocation; CRA economic-operator records feed CRA-AR mandate and substantial-modification records; DORA Art. 30 CIF-clauses establish contractual basis for Art. 30(3)(e) audit-rights), 6.1 (vendor-risk-assessment four-factor proportionality shapes CIF designation that triggers audit-rights; processor-tier feeds cross-MS SPOC routing for GDPR-NIS 2 dual controllers)]
  nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-05, GV.OC-02, GV.OC-03, GV.RR-02, RS.CO-04, ID.AM-04, ID.RA-02, DE.CM-06]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs anchor boundary mechanisms on the same non-EU or cross-border supply-chain event (see HSO scope-overlap principle); AI Act out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Four participating regulations (GDPR, NIS 2, CRA, DORA) each anchor a distinct boundary mechanism: GDPR anchors non-EU personal-data actors through a written Union representative; NIS 2 anchors entity-level supplier boundaries and cross-MS notification routing; CRA anchors product-compliance accountability through authorised representatives, manufacturer-equivalent triggers, third-party substantial-modification rules, and 10-year economic-operator traceability; DORA anchors financial-entity and competent-authority access / inspection / audit rights over critical ICT third-party providers. CRDA-deep verified relationships (6 pairs: 6 SAME, no CORRECTED, no CONTRADICTORY; 2 COMPLEMENTARY + 1 EQUAL (different objects) + 3 DIFFERENT-PERSPECTIVE). The 1 conditional emergent tension is the **four-party boundary architecture** — a multi-regulated non-EU or cross-border supply chain may need GDPR Union representative + CRA authorised representative + NIS 2 cross-MS routing / direct-supplier register + DORA CIF audit rights at the same time. The GDPR↔CRA EQUAL (different objects) pair requires special treatment: it is EQUAL in form (written EU-side representative) but different in object (data-protection representative vs product-compliance authorised representative); a single legal entity may perform both roles only if both mandates and recipient channels are separately documented, otherwise two representatives or two mandates coexist. The high-level SO does NOT collapse these mechanisms — it builds a boundary matrix showing which representative, route, traceability record, or audit right applies in each factual scenario, preserving per-reg target object, trigger, boundary instrument, and recipient. The role-and-recipient allocation principle governs Phase 1C Doc 07: the matrix is keyed by third-party role, jurisdiction, service/product criticality, modification status, and incident-routing scope. (Copied from the HSO Considerations block of `### D-06.4.0`; preserved here for self-containment per Volere shell `considerations` field definition; the substantive content lives in HSO.)
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-06.4
title: D-06.4 Third-Party Boundary Management — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.4 Third-Party Boundary Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-06_Supply-Chain/D-06.4.md
status: DRAFT
---
> **Deep analysis:** [D-06.4 Third-Party Boundary Management](../../DeepAnalysis/D-06_Supply-Chain/D-06.4.md)
#### D-06.4 Third-Party Boundary Management
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-023 | Non-EU controllers/processors designate an EU representative in writing (Art. 27(1)/(2)) | Non-EU controller/processor; representative designation |
| NIS2 | SO-NIS2-014 (partial) + SO-NIS2-018 | Direct supplier scope-limiter (Art. 21(2)(d)) + cross-MS notification routing (Art. 23(6)) | Entity-level boundary; direct supplier + cross-MS information flow |
| CRA | SO-CRA-041, SO-CRA-042, SO-CRA-043, SO-CRA-044 | Authorised representative appointment + manufacturer-equivalent status on own-name placement + third-party substantial-modification triggers + economic-operator identification + 10-year retention (Art. 18 + Art. 21 + Art. 22 + Art. 23) | Non-EU manufacturer → EU AR; substantial-modification triggers; identification + 10y retention |
| DORA | SO-DORA-012 (partial) | Unrestricted audit rights over critical ICT third-party providers (Art. 30(3)(e)) | Financial-entity audit-rights architecture over critical providers |
| AI_Act | — | Out-of-scope (sole authorities: DORA/NIS2) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-06.4 per AEGIS taxonomy §4.1. DORA and NIS2 are sole authorities for third-party-boundary architecture.
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,NIS2,CRA,DORA -->
- **Four-party boundary architecture with cross-cutting substantial-modification trigger.** GDPR Art. 27 representative + CRA Art. 18 AR + NIS2 `direct` scope-limiter + DORA audit rights — each imposes a different mechanism for boundary management. The pairwise readings surface specific actor-level overlaps (GDPR↔CRA both require EU-side representatives, but for different objects), but the *non-pairwise observation* is that a single non-EU entity subject to multiple regulations (e.g., a non-EU manufacturer of CRA-classified products that processes EU personal data and supplies critical ICT to financial entities) must maintain multiple representative relationships (GDPR Art. 27 representative + CRA Art. 18 AR), satisfy NIS2's `direct` scope-limiter if the entity supplies NIS2-essential entities, and accept DORA audit rights if the entity is a critical provider. Phase 2 must produce a representative/rights matrix that allocates obligations across these four tracks.
<!-- /emergent -->
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **GV.SC-03** (Contracts with suppliers and third-party partners) and **GV.SC-04** (Suppliers and third-party partners are routinely assessed). All four regulations map to these two CSF subcategories. The substantial-modification trigger (CRA Art. 22) and the manufacturer-equivalent status (CRA Art. 21) are not separately mapped by CSF 2.0; they are product-classification constructs outside the CSF GOVERN/IDENTIFY scope.
##### Downstream implication
Phase 2 obligation derivation must produce a 4-track third-party-boundary matrix: (1) GDPR Art. 27 representative designation, (2) CRA Art. 18 AR appointment, (3) NIS2 `direct` scope-limiter compliance, (4) DORA audit-rights assertion. For non-EU entities with multi-regulation exposure, all four apply simultaneously. Phase 3 case generation must validate the representative architecture and audit-rights enforcement in case companies operating at the multi-regulation intersection.
---
### Summary statistics
| Metric | Value |
|---|---|
| Sub-domains covered | 12 (D-04.1–D-04.4, D-05.1–D-05.4, D-06.1–D-06.4) |
| Total pairwise cells | 53 |
| Total emergent tensions | 7 (across D-04.3: 2, D-05.1: 1, D-05.2: 1, D-06.3: 1, D-06.4: 1) |
| 5-reg sub-domain | D-04.3 only (10 pairs, 2 emergent tensions) |
| 4-reg sub-domains | D-04.1, D-04.2, D-04.4, D-06.1, D-06.3, D-06.4 (6 pairs each) |
| 3-reg sub-domains | D-05.1, D-05.2 (3 pairs each) |
| 2-reg sub-domains | D-05.3 (1 pair) |
| 1-reg sub-domains | D-05.4, D-06.2 (sole authority) |
#### Distribution of relationship taxonomy across pairwise cells
| Relationship type | Count | Sub-domains |
|---|---|---|
| Complementary | ~38 | majority of layered architectures (D-04.x, D-06.x) |
| Different-perspective | ~10 | product-vs-entity distinctions (D-04.1, D-04.2, D-04.4, D-06.1, D-06.3, D-06.4) |
| Contradictory | ~5 | D-04.3 timeline conflicts (GDPR↔NIS2, GDPR↔DORA, GDPR↔AI_Act, NIS2↔DORA, NIS2↔AI_Act, CRA↔DORA, CRA↔AI_Act, DORA↔AI_Act); D-05.1 special-category (GDPR↔AI_Act); D-05.2 retention-direction (GDPR↔CRA, GDPR↔AI_Act); D-06.3 clause-list overlap (GDPR↔DORA) |
| Equal | ~3 | NIS2↔DORA recovery + vendor-risk; DORA exceeds; CRA↔DORA containment recovery |
#### Sole-authority summary
| Sub-domain | Sole authority | Justification (per AEGIS taxonomy §4.1) |
|---|---|---|
| D-05.2 (Retention) | GDPR | Personal-data storage limitation is data-subject-rights anchored; NIS2/DORA operational-resilience-focused; CRA 10y tail is update-availability distinct; AI Act 6mo is log-retention distinct |
| D-05.3 (Erasure) | GDPR | Art. 17 data-subject right; CRA Annex I (2)(m) is manufacturer design, not a rights instrument |
| D-05.4 (Portability) | GDPR | Art. 20 data-subject right; CRA Annex I (2)(m) is technical transfer, not a right |
| D-06.2 (SBOM) | CRA | Annex I Part II (1) is sole SBOM mandate |
#### Critical complexity point — D-04.3
D-04.3 (Regulatory Notification) is the single most complex orchestration problem in Part B:
- 5 regulations overlap (only sub-domain in Part B where AI_Act participates beyond out-of-scope)
- 10 pairwise combinations
- 6 distinct timeline tiers (24h, 72h, 14d, 15d, 1m, plus `without undue delay`)
- 5 distinct recipient classes (DPA, CSIRT, MSA, CA, AI Office)
- 2 emergent tensions (binding-procedure principle + recipient-routing matrix)
---
**End of Part B staging document.**
---
## Cross-Regulation Domain Analysis — Part C (D-07 + D-08 + D-09 + D-10)
> **Scope.** Staging-only cross-regulation analysis across the 5 EU regulations (GDPR, NIS 2, CRA, DORA, AI Act) for sub-domains D-07.1 through D-10.3 (14 sub-domains). Each sub-domain is rendered with: participants table, pairwise matrix (up to 10 cells), emergent tensions (only when 3+ regulations overlap), SR cross-validation (NIST CSF 2.0), and downstream implication.
>
> **Relationship taxonomy.** `equal` (same scope/angle), `complementary` (different scope/angle, additive), `contradictory` (mutually exclusive requirements), `different-perspective` (same object, distinct framing).
>
---
### D-07 Secure Development
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-06.4
title: D-06.4 Third-Party Boundary Management — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.4 Third-Party Boundary Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-06_Supply-Chain/D-06.4.md
status: DRAFT
---
> **Domain analysis:** [D-06.4 Third-Party Boundary Management](../../DomainAnalysis/D-06_Supply-Chain/D-06.4.md)
#### D-06.4 Third-Party Boundary Management
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.4 per AEGIS taxonomy §4.1. DORA and NIS 2 are sole authorities for third-party-boundary architecture.
##### Pair: GDPR ↔ NIS2
**GDPR article (verbatim, Art. 27(1)/(2)):**
> "Where Article 3(2) applies, the controller or the processor shall designate in writing a representative in the Union." — Art. 27(1) GDPR
>
> "The obligation set out in paragraph 1 shall not apply to: (a) processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9(1) or of personal data relating to criminal convictions as referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing; or (b) a public authority or body." — Art. 27(2)(a)/(b) GDPR
**NIS 2 article (verbatim, Art. 23(6) + Art. 23(8)):**
> "The competent authorities or the CSIRTs shall inform the other affected Member States and ENISA about the incident. The competent authorities or the CSIRTs shall, in accordance with Union or national law, provide the relevant information to the recipients of the services of the entity concerned." — NIS 2 Art. 23(6)
>
> "Single points of contact shall forward the notifications referred to in this Article to the single points of contact of other affected Member States and to ENISA." — NIS 2 Art. 23(8)
**Scope comparison:**
- GDPR scope: non-EU controller / processor → EU representative (legal-address anchor).
- NIS 2 scope: cross-MS notification routing → SPOC + ENISA (notification-routing mechanism).
- Scope overlap: **N (typically) — different mechanisms (legal address vs notification routing).** They overlap when a non-EU controller operates across multiple MS.
**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- NIS 2 trigger: significant incident notification.
- Trigger alignment: **DIFFERENT**.
**Threshold/timeline comparison:**
- GDPR: no quantitative threshold (per-processing-event assessment).
- NIS 2: significant-incident threshold + 24h early warning + 72h notification + final report.
- Tension: **NONE**.
**Recipient comparison:**
- GDPR: supervisory authority (DPA).
- NIS 2: SPOC + ENISA + affected MS.
**Content template comparison:**
- GDPR: written representative designation.
- NIS 2: incident-notification routing through SPOC.
**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY**
**Reasoning:** GDPR Art. 27 designates an EU *representative* (a legal-address anchor for non-EU controllers); NIS 2 Art. 23(6) routes notifications across *Member States* via SPOCs (Single Points of Contact). Different actors (representative vs SPOC), different purposes (legal address vs notification routing). Both apply when a non-EU controller operates across multiple MS.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms, distinct actors.**
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer record: (1) GDPR Art. 27 representative designation; (2) NIS 2 SPOC identification for incident-notification routing. The COMPLEMENTARY label is preserved.
---
##### Pair: GDPR ↔ CRA
**GDPR article (verbatim, Art. 27(1)):**
> "Where Article 3(2) applies, the controller or the processor shall designate in writing a representative in the Union." — Art. 27(1) GDPR
**CRA article (verbatim, Art. 18(1)–(3)):**
> "A manufacturer established outside the Union may, by written mandate, appoint an authorised representative established in the Union to perform specified tasks on behalf of the manufacturer." — CRA Art. 18(1)
>
> "The mandate of the authorised representative shall not cover the obligations laid down in Article 13(1) to (11), Article 13(12) first subparagraph, point (a), and Article 13(14)." — CRA Art. 18(2)
>
> "The authorised representative shall perform the tasks specified in the mandate. The mandate shall allow the authorised representative to perform at least the following tasks: (a) keeping a copy of the EU declaration of conformity and the technical documentation at the disposal of the market surveillance authorities for the period referred to in Article 13(13); (b) providing the market surveillance authorities, on reasoned request, with all the information and documentation necessary to demonstrate the conformity of a product with digital elements with the essential cybersecurity requirements set out in Annex I; (c) cooperating with the market surveillance authorities, at their request, on any action taken to address non-compliance with the essential cybersecurity requirements set out in Annex I presented by a product with digital elements covered by the mandate of the authorised representative." — CRA Art. 18(3)
**Scope comparison:**
- GDPR scope: data-protection representative for non-EU controller / processor.
- CRA scope: product-compliance authorised representative for non-EU manufacturer.
- Scope overlap: **Y (when the same non-EU entity is both a non-EU controller and a non-EU CRA manufacturer)** — different objects, different mandates.
**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- CRA trigger: non-EU manufacturer placing CRA-classified product on the EU market.
- Trigger alignment: **PARTIAL** — both for non-EU entities, but addressing different objects.
**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- CRA: written mandate + non-delegable carve-out (Art. 18(2)).
- Tension: **NONE**.
**Recipient comparison:**
- GDPR: DPA + data subject.
- CRA: MSA + national competent authority.
**Content template comparison:**
- GDPR: written representative designation.
- CRA: written AR mandate (Art. 18(1)).
**Classified relationship (from CRDA):** EQUAL
**Verified relationship (after OJ-text analysis):** **SAME — EQUAL** (different objects)
**Reasoning:** Both GDPR Art. 27 and CRA Art. 18 require a written EU-side representative for non-EU entities. Different objects: GDPR = data-protection representative; CRA = product-compliance authorised representative. When a non-EU manufacturer of CRA-classified products is also a non-EU controller, both representatives are required, with different mandates (Art. 27 representative handles data-subject requests and DPA liaison; Art. 18 AR retains technical documentation and cooperates with MSA). The label "equal" captures the same form (written EU-side representative) but the substance is layered, not redundant.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when the same non-EU entity is both a non-EU controller and a non-EU CRA manufacturer — both apply on the same entity but address different obligations.**
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer representative architecture: (1) GDPR Art. 27 data-protection representative; (2) CRA Art. 18 product-compliance AR. The EQUAL label is preserved.
---
##### Pair: GDPR ↔ DORA
**GDPR article (verbatim, Art. 27(1)):**
> (See GDPR↔CRA pair above for the verbatim text.)
**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> "Where the contractual arrangements concern critical or important functions, the contractual arrangements shall, in addition to the elements set out in paragraph 2, include the following: … (e) the rights of the financial entity and the competent authority to obtain, from the ICT third-party service provider, unrestricted rights of access, inspection and audit by the financial entity, or an appointed third party, and by the competent authority … including the right to take copies of relevant documentation on-site if critical to the operations of the ICT third-party service provider, the effective exercise of which is not impeded or limited by other contractual arrangements or implementation policies. The right to agree on alternative assurance levels if other clients' rights are affected shall be allowed." — DORA Art. 30(3)(e)(i)+(ii)
**Scope comparison:**
- GDPR scope: EU representative designation for non-EU controller / processor.
- DORA scope: audit rights over critical ICT third-party providers (CIF-only).
- Scope overlap: **N — different mechanisms (legal-address vs audit rights).** They overlap when a non-EU ICT third-party provider is critical / important for a financial entity.
**Trigger comparison:**
- GDPR trigger: non-EU controller / processor with Art. 3(2) activity.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **DIFFERENT**.
**Threshold/timeline comparison:**
- GDPR: no quantitative threshold.
- DORA: CIF-only.
- Tension: **NONE**.
**Recipient comparison:**
- GDPR: DPA.
- DORA: financial entity + competent authority.
**Content template comparison:**
- GDPR: written representative designation.
- DORA: Art. 30(3)(e)(i) audit-rights clause in CIF-supporting contracts.
**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** GDPR Art. 27 is a *legal-address* obligation (representative must be EU-based, mandate in writing); DORA Art. 30(3)(e) is a *rights* obligation (audit + inspection + on-site copy rights). Different mechanisms: GDPR = designate, DORA = assert audit rights. Both apply when a non-EU ICT third-party provider is critical / important for a financial entity.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms.** Conditional overlap when a non-EU ICT third-party provider is critical / important for a financial entity.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) GDPR Art. 27 representative designation; (2) DORA Art. 30(3)(e) audit-rights clause for CIF contracts. The DIFFERENT-PERSPECTIVE label is preserved.
---
##### Pair: NIS2 ↔ CRA
**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)
**CRA article (verbatim, Art. 22(1)/(2) + Art. 23(1)/(2)):**
> "A natural or legal person, other than the manufacturer, the importer or the distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market shall be considered to be the manufacturer for the purposes of this Regulation." — CRA Art. 22(1)
>
> "The manufacturer obligations referred to in paragraph 1 shall apply to the affected part of the product with digital elements or, where the substantial modification has an impact on the cybersecurity of the product with digital elements as a whole, to the entire product with digital elements." — CRA Art. 22(2)
>
> "Economic operators shall, on a reasoned request from a market surveillance authority, identify: (a) any economic operator that has supplied them with a product with digital elements; (b) any economic operator to which they have supplied a product with digital elements." — CRA Art. 23(1)
>
> "Economic operators shall keep the information referred to in paragraph 1 for a period of 10 years after they have been supplied with the product with digital elements and after they have supplied the product with digital elements." — CRA Art. 23(2)
**Scope comparison:**
- NIS 2 scope: direct-supplier scope-limiter (entity-side, who the entity is liable for).
- CRA scope: substantial-modification triggers (who becomes the manufacturer) + economic-operator identification.
- Scope overlap: **N (typically) — different actors, different triggers.** Both apply when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party.
**Trigger comparison:**
- NIS 2 trigger: per-direct-supplier.
- CRA trigger: per-substantial-modification + per-MSA-identification-request.
- Trigger alignment: **DIFFERENT**.
**Threshold/timeline comparison:**
- NIS 2: `direct` scope-limiter.
- CRA: Art. 3(30) substantial-modification + Art. 23(2) 10-year retention.
- Tension: **NONE**.
**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- CRA: MSA.
**Content template comparison:**
- NIS 2: documented supplier list under `direct` scope.
- CRA: substantial-modification record + Art. 23 supply-chain identification log (10-year retention).
**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** NIS 2 `direct` scope-limiter is about *who* the entity is liable for (direct suppliers); CRA Art. 22 / 23 is about *who* becomes the manufacturer (third-party on substantial modification) and *who* provides identification to MSAs. Different actors, different triggers. Both apply when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party: the deployer is NIS 2-liable for the direct supplier, and the third-party modifier becomes a CRA-manufacturer.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct actors, distinct triggers.** Conditional overlap when a NIS 2 entity deploys a CRA-classified product substantially modified by a third party.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) NIS 2 deployer-side direct-supplier list; (2) CRA substantial-modification record + 10-year supply-chain identification log. The DIFFERENT-PERSPECTIVE label is preserved.
---
##### Pair: NIS2 ↔ DORA
**NIS 2 article (verbatim, Art. 21(2)(d)):**
> "… supply chain security including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." — NIS 2 Art. 21(2)(d)
**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> (See GDPR↔DORA pair above for the verbatim text.)
**Scope comparison:**
- NIS 2 scope: direct supplier (entity-side).
- DORA scope: critical ICT third-party provider (financial-entity-side, CIF-only).
- Scope overlap: **Y when a financial entity is also a NIS 2 essential / important entity** — DORA audit rights extend to critical / important providers, which may include non-direct providers via the supply chain.
**Trigger comparison:**
- NIS 2 trigger: continuous supply-chain security.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **PARTIAL** — NIS 2 is continuous; DORA is per-CIF contract.
**Threshold/timeline comparison:**
- NIS 2: `direct` scope-limiter.
- DORA: CIF-only audit rights.
- Tension: **NONE** — DORA audit rights extend beyond NIS 2's `direct` scope.
**Recipient comparison:**
- NIS 2: CSIRT / competent authority.
- DORA: competent authority.
**Content template comparison:**
- NIS 2: documented supplier list under `direct` scope.
- DORA: Art. 30(3)(e)(i) audit-rights clause.
**Classified relationship (from CRDA):** COMPLEMENTARY
**Verified relationship (after OJ-text analysis):** **SAME — COMPLEMENTARY** (DORA exceeds NIS 2)
**Reasoning:** NIS 2 `direct` scope-limiter limits the supplier universe; DORA Art. 30(3)(e) audit rights apply to critical or important providers (which may include non-direct providers via the supply chain). A financial entity's DORA audit rights extend beyond NIS 2's `direct` scope into the broader supply chain of critical providers.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **Y when a financial entity is also a NIS 2 essential / important entity — both apply on the same supplier relationship.** DORA exceeds NIS 2 in the audit-rights dimension.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a consolidated supplier-management architecture: (1) NIS 2 `direct` supplier list; (2) DORA Art. 30(3)(e) audit-rights clause for CIF contracts. The COMPLEMENTARY label is preserved.
---
##### Pair: CRA ↔ DORA
**CRA article (verbatim, Art. 23(1)/(2)):**
> (See NIS2↔CRA pair above for the verbatim text.)
**DORA article (verbatim, Art. 30(3)(e)(i)+(ii)):**
> (See GDPR↔DORA pair above for the verbatim text.)
**Scope comparison:**
- CRA scope: economic-operator identification duty (operator-side).
- DORA scope: audit rights on financial-entity-side over critical providers.
- Scope overlap: **N (typically) — different mechanisms, different directions.** Both apply when a CRA-classified product is supplied to a financial entity via an importer / distributor.
**Trigger comparison:**
- CRA trigger: per-MSA-identification-request + 10-year retention.
- DORA trigger: CIF-supporting ICT third-party contract.
- Trigger alignment: **DIFFERENT**.
**Threshold/timeline comparison:**
- CRA: Art. 23(2) 10-year retention.
- DORA: CIF-only audit rights.
- Tension: **NONE**.
**Recipient comparison:**
- CRA: MSA.
- DORA: financial entity + competent authority.
**Content template comparison:**
- CRA: Art. 23 supply-chain identification log (10-year retention).
- DORA: Art. 30(3)(e)(i) audit-rights clause.
**Classified relationship (from CRDA):** DIFFERENT-PERSPECTIVE
**Verified relationship (after OJ-text analysis):** **SAME — DIFFERENT-PERSPECTIVE**
**Reasoning:** CRA Art. 23(1) imposes an *identification duty on economic operators* (they must identify upstream supplier and downstream recipient); DORA Art. 30(3)(e) imposes *audit rights on financial entities* over critical providers. Different mechanisms: CRA = operator-side identification obligation; DORA = financial-entity-side rights. Both apply when a CRA-classified product is supplied to a financial entity via an importer / distributor.
**Scope-disjoint test:** Does this pair actually overlap on a single event at a single party? **N (typically) — distinct mechanisms, distinct directions.**
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a 2-layer architecture: (1) CRA economic-operator identification log (10-year retention); (2) DORA audit-rights clause for CIF contracts. The DIFFERENT-PERSPECTIVE label is preserved.
---
### Summary statistics
| Metric | Value |
|---|---|
| Sub-domains covered | 8 (D-05.1–D-05.4, D-06.1–D-06.4) |
| Pair analyses produced | **25** |
| Pairs classified as CONTRADICTORY in CRDA | 4 |
| Pairs corrected from CRDA | **4** |
| Sole-authority sub-domains | 2 (D-05.4 GDPR, D-06.2 CRA) |
| 2-reg sub-domain | D-05.3 (1 pair) |
| 3-reg sub-domains | D-05.1, D-05.2 (3 pairs each) |
| 4-reg sub-domains | D-06.1, D-06.3, D-06.4 (6 pairs each) |
#### Distribution of verified relationship taxonomy
| Relationship type | Count | Sub-domains |
|---|---|---|
| EQUAL | 4 | D-06.1 NIS2↔DORA; D-06.3 NIS2↔DORA; D-06.4 GDPR↔CRA; (NIS2↔DORA also COMPLEMENTARY at D-06.4) |
| COMPLEMENTARY | 11 | D-05.1 (3); D-05.2 (1 corrected + 1); D-05.3 (1); D-06.1 (3); D-06.3 (2 corrected + 1); D-06.4 (2) |
| DIFFERENT-PERSPECTIVE | 7 | D-05.2 (1); D-06.1 (3); D-06.3 (2); D-06.4 (3) |
| CONTRADICTORY | 0 | (none confirmed — see P0 disagreement report) |
| SCOPE-DISJOINT | 2 | D-05.1 GDPR↔AI_Act (corrected from CONTRADICTORY); D-05.2 GDPR↔CRA (corrected from CONTRADICTORY) |
---
### Summary table (corrections vs CRDA)
| Sub-domain | Pair | CRDA classification | Verified classification | Reason for change |
|---|---|---|---|---|
| D-05.1 | GDPR ↔ AI_Act | CONTRADICTORY (special-category) | **SCOPE-DISJOINT** | AI Act Art. 10(5) is a conditional carve-out to GDPR Art. 9(1), not a contradiction of GDPR Art. 5(1)(c). The pair only overlaps for the narrow 6-condition bias-correction scenario; in baseline the pair is scope-disjoint. CRDA reasoning itself concedes the carve-out framing — the "contradictory" label is internally inconsistent. |
| D-05.2 | GDPR ↔ CRA | CONTRADICTORY (direction) | **SCOPE-DISJOINT** | GDPR Art. 5(1)(e) caps personal-data retention; CRA Annex I Part II (7)/(8) requires update-artefact availability. Different data classes (personal data vs update artefacts), different actors (controller vs manufacturer), different triggers (retention vs availability). CRDA reasoning itself concedes the axes are disjoint — the "contradictory" label is internally inconsistent. |
| D-05.2 | GDPR ↔ AI_Act | CONTRADICTORY (direction) | **COMPLEMENTARY** (floor-within-ceiling) | GDPR Art. 5(1)(e) is qualitative ceiling; AI Act Art. 19(1) is 6-month minimum floor. The two reconcile within the intersection [6 months, "necessary"] — the textbook floor-within-ceiling pattern, which is COMPLEMENTARY not CONTRADICTORY. CRDA reasoning itself states: "The two are reconcilable". |
| D-06.3 | GDPR ↔ DORA | CONTRADICTORY (overlap) | **COMPLEMENTARY** (clause-list union) | GDPR Art. 28(3) has 8 mandatory elements; DORA Art. 30(2) has 9 minimum elements. The two lists overlap but are not identical — the union is the operative rule when the financial entity is also a controller. CRDA reasoning itself acknowledges this: "the contract must satisfy both sets" — which is the textbook union pattern. The "contradictory" label is scope-incorrect. |
(4 corrections in total: 3 from CONTRADICTORY → SCOPE-DISJOINT or COMPLEMENTARY; the CRDA file remains untouched.)
---
### P0 disagreement report
#### Disagreement 1: The CRDA "contradictory" label is over-applied in D-05 + D-06
**Concern:** The CRDA file marks 4 pairs as "contradictory" in D-05 + D-06 (GDPR↔AI_Act D-05.1; GDPR↔CRA D-05.2; GDPR↔AI_Act D-05.2; GDPR↔DORA D-06.3). On OJ-text verification, none of these is a true contradiction — each is either scope-disjoint (the regulations address different data classes / actors / triggers) or complementary (one sets a ceiling, the other a floor; one sets a clause list, the other a clause list). The CRDA reasoning itself frequently concedes this internally ("regulatory carve-out", "not on the same axis", "the two are reconcilable", "the contract must satisfy both sets") while keeping the contradictory label.
**Why this matters:** A "contradictory" label drives Phase 2 obligation derivation toward a reconciliation clause that says "if both apply, the stricter wins" — which is wrong when the pair is scope-disjoint (no overlap means no conflict) or genuinely complementary (both apply simultaneously and additively). The P2 obligation table will inherit the over-classification and produce either false conflicts (scope-disjoint) or under-built union rules (complementary).
**Recommendation to Orchestrator / Validator:** Correct the 4 labels in the CRDA file per the Summary table above. Specifically: change D-05.1 GDPR↔AI_Act to **scope-disjoint** (with Art. 10(5) carve-out annotation); change D-05.2 GDPR↔CRA to **scope-disjoint**; change D-05.2 GDPR↔AI_Act to **complementary**; change D-06.3 GDPR↔DORA to **complementary** (with clause-list union rule).
#### Disagreement 2: The CRDA does not distinguish "EQUAL (different objects)" from "EQUAL (same object)"
**Concern:** The CRDA marks 3 pairs as EQUAL in D-05 + D-06, but the three pairs are not equivalent in form. NIS 2↔DORA on D-06.1 and D-06.3 is *same-object* equality (DORA's four-factor test or 9-element list operationalises NIS 2's open-texture chapeau); GDPR↔CRA on D-06.4 is *different-object* equality (the same form — written EU-side representative — applied to different objects: data-protection representative vs product-compliance AR). Phase 2 obligation derivation should treat these differently: same-object equality means single control satisfies both; different-object equality means the two representatives co-exist.
**Recommendation to Orchestrator / Validator:** Annotate the CRDA EQUAL pairs with a sub-flag for same-object vs different-object. Phase 2 obligation derivation should then use single-control vs dual-control derivation rules accordingly.
#### Disagreement 3: The CRDA does not annotate "Conditional" overlap
**Concern:** Several pairs are Conditional — they overlap only on specific factual circumstances. The CRDA's 4-way taxonomy does not capture this. Phase 2 obligation derivation will apply unconditional derivation rules and produce obligation statements that either over-claim (saying both regulations always apply when they only sometimes do) or under-claim (saying they only sometimes apply when they almost always do in practice).
**Recommendation to Orchestrator / Validator:** Annotate each CRDA pair with a Conditional flag where applicable. For D-05 + D-06 the following pairs are Conditional in scope-disjoint sense: D-05.1 GDPR↔CRA (Y when CRA product processes personal data); D-05.1 GDPR↔AI_Act (Y only for the narrow Art. 10(5) carve-out scenario); D-05.2 GDPR↔CRA (Y when CRA update-distribution log contains personal data); D-06.1 GDPR↔CRA (Y when controller deploys CRA product); D-06.1 NIS2↔CRA (Y when deployer is entity and manufacturer supplies CRA product); D-06.3 NIS2↔CRA (Y when NIS 2 entity deploys CRA product); D-06.4 GDPR↔CRA (Y when non-EU entity is both GDPR controller and CRA manufacturer); D-06.4 GDPR↔DORA (Y when non-EU ICT provider is critical/important for financial entity); D-06.4 NIS2↔CRA (Y when NIS 2 entity deploys CRA product substantially modified by third party).
---
### Quality flags
| Flag | Severity | Notes |
|---|---|---|
| **SR-AIACT-008 T5 mapping error** | Cosmetic | AI_Act validation report v0.1 §3.4 / §6 flags T5 citation of Art. 12(4) (which does not exist in the OJ); substance is in Art. 19(1). Used OJ-literal locus at Art. 19(1) in this analysis. |
| **SR-DORA-021 Art. 30(2) gloss** | Material | DORA validation report v0.2 F-10 flags audit rights and exit strategies misattributed from Art. 30(3). Used OJ-literal 9-element list at Art. 30(2) in this analysis. |
| **SR-CRA-050 `due diligence` VAG+POLY-S3** | Cosmetic | R3 (procedural + substantive) reading chosen; alternative R1 (procedural only) and R2 (substantive only) preserved. |
| **SR-NIS2-020 `direct` SCOPE-Q S3** | Material | Three materially distinct readings (R1 Tier-1 / R2 technically integrated / R3 operationally dependent). R1 chosen as minimum; R2 and R3 to be considered per Recital 56. Member State transposition divergence noted (BSI favours R1+R3; ANSSI favours R2+R3). |
| **CRA 10-year tail interpretive** | Cosmetic | CRDA reads "10-year update-availability tail" from Annex II Art. 13(18) + Art. 13(8); OJ-literal anchor is the 5-year support-period minimum + 10-year Annex II information accessibility. |
| **DORA Art. 28(5) standards POLY** | Material | DORA validation report v0.2 §3.5 flags the open-naming question. Reading chosen: entity-selected standards with supervisory-recognised standards (ISO/IEC 27001, SOC 2, NIST CSF, EBA Guidelines) as the EU-acceptable floor. |
| **GDPR Art. 30(1)(f) `where possible` hedge** | Cosmetic | GDPR deduction audit v0.1 F-6 flags the hedge dropped in SR-GDPR-029. Used OJ-literal text with hedge in this analysis. |
---
### Chain metadata
| Field | Value |
|---|---|
| Total pair analyses | **25** |
| Classification corrections from CRDA | **4** |
| P0 disagreements raised | **3** |
| Quality flags surfaced | **7** (1 material, 2 cosmetic, plus 4 cross-cutting) |
| Methodology | 5-class taxonomy (EQUAL / COMPLEMENTARY / CONTRADICTORY / DIFFERENT-PERSPECTIVE / SCOPE-DISJOINT) + scope-disjoint test |
| CRDA file status | **Unchanged** (this analysis is staging; corrections are recommendations for the Validator) |
| Phase 1C Doc 07 implications | Documented per pair in `Downstream implication (1-2 sentences)` blocks |
---
---
document_id: AEGIS-PREPROC-STAGE-CRDA-DEEP-PART-D
title: "Cross-Regulation Deep Analysis — Part D (D-07 + D-08 + D-09 + D-10)"
phase: "Pre-processing (Regulatory Baseline) — per-pair OJ-text verification"
version: 0.1
created: 2026-07-09
updated: 2026-07-09
author: "Executor D (sub-agent)"
status: DRAFT
chain_version: v2.1
related_documents:
  - ../../_archive/00_CrossRegulation_Domain_Analysis.md
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
inputs:
  - 5 × 01_SecurityObjectives.md
  - 5 × 02_SecurityRules_NIST.md
  - ../../_archive/00_CrossRegulation_Domain_Analysis.md
scope: D-07 (Secure Development, 4 sub-domains) + D-08 (Human Factors, 3 sub-domains) + D-09 (Governance & Documentation, 4 sub-domains) + D-10 (Monitoring & Audit, 3 sub-domains) = 14 sub-domains, 91 pair analyses
purpose: Per-pair OJ-text deep analysis verifying the CRDA pairwise classifications using the scope-disjoint test and the 5-option relationship taxonomy. CRDA is NOT modified by this analysis; findings are recommendations for the Validator and Orchestrator.
---
## Cross-Regulation Deep Analysis — Part D (D-07 + D-08 + D-09 + D-10)
### Methodology
#### Scope-disjoint test (the operational pivot)
For each pair (A, B) classified in CRDA, the test asks: **does A's triggering event overlap with B's triggering event at a single regulated party (controller / manufacturer / financial entity / deployer / provider / NSIE / essential entity) on a single occasion?**
- **Yes** → pair overlaps on the same real-world event; CRDA's substantive classification (equal / complementary / contradictory / different-perspective) is informative.
- **No** → pair's triggering events address **distinct objects at distinct actors**; the regulations do not actually impose obligations on the same party on the same occasion. The CRDA classification is then a *taxonomy* artifact (two rules happen to map to the same AEGIS sub-domain) rather than a *substantive* relationship. In this case the correct substantive classification is **SCOPE-DISJOINT**.
- **Conditional** → the pair overlaps only under specific factual circumstances; the label is correct in baseline only if the case company matches those circumstances.
#### 5 relationship classes
| Class | Test | When it applies (Part D examples) |
|---|---|---|
| **EQUAL** | Same scope/angle, same triggering event, same addressee | NIS 2 ↔ DORA on change management (D-07.4); NIS 2 ↔ DORA on risk analysis (D-09.2); NIS 2 ↔ DORA on monitoring (D-10.1); NIS 2 ↔ DORA on management-body training (D-08.3); NIS 2 ↔ DORA on awareness (D-08.1); NIS 2 ↔ DORA on testing (D-10.3) |
| **COMPLEMENTARY** | Different scope/angle but both apply on the same event | GDPR ↔ NIS 2 on by-design (D-07.1); GDPR ↔ DORA on monitoring (D-10.1); CRA ↔ DORA on risk assessment (D-09.2) |
| **DIFFERENT-PERSPECTIVE** | Same object but distinct regulatory framing | GDPR ↔ CRA on training (D-08.1, workforce vs. user); NIS 2 ↔ CRA on training (D-08.1, workforce vs. integrator); CRA ↔ DORA on awareness (D-08.1, user-instructions vs. staff modules) |
| **CONTRADICTORY** | Mutually exclusive requirements on a single event | None found in D-07 to D-10 in baseline classification |
| **SCOPE-DISJOINT** | Different objects, different actors, different triggers | GDPR ↔ CRA on asset inventories (D-09.3, personal data vs. ICT assets); CRA ↔ AI Act on testing (D-10.3, conformity assessment vs. AI risk-management testing); CRA user-instructions vs. internal staff awareness (D-08.1) |
#### Verbatim OJ text sourcing
Verbatim text is taken from the per-regulation `02_SecurityRules_NIST.md` files (`regulatory_rationale` field of each SR, with the SR's own `source_clauses.article_ref` confirming the OJ locus). Where the OJ passage is long, the operative phrase is reproduced; the article-ref footnote points to the full article. Article text not directly quoted in a SR is drawn from the corresponding `01_SecurityObjectives.md` `source_clauses` list.
#### Relationship to CRDA
CRDA classifies pairs on a 4-way taxonomy (equal / complementary / contradictory / different-perspective). This deep analysis keeps CRDA's labels but **adds** the scope-disjoint test. Where CRDA labeled a pair "complementary" or "different-perspective" but the scope-disjoint test shows the pair cannot both bind the same party on the same occasion, the verified relationship is **SCOPE-DISJOINT** (or **COMPLEMENTARY** if the floor-within-ceiling pattern applies). The CRDA file itself is not modified by this pilot — corrections are listed in the summary table at the end for the Validator's downstream action.
#### Frontmatter chain
This file is part of the CRDA-deep pilot chain:
- Part A (`_STAGING_crda_deep_part_A.md`) — D-01 + D-02
- Part B (`_STAGING_crda_deep_part_B.md`) — D-03 + D-04
- Part C (`_STAGING_crda_deep_part_C.md`) — D-05 + D-06
- Part D (this file) — D-07 + D-08 + D-09 + D-10
- Subsequent parts — D-11 onwards
#### Part D coverage
- 14 sub-domains: D-07.1, D-07.2, D-07.3, D-07.4, D-08.1, D-08.2, D-08.3, D-09.1, D-09.2, D-09.3, D-09.4, D-10.1, D-10.2, D-10.3.
- 91 pair analyses (CRDA-omitted pairs included with explicit "not classified by CRDA" annotation).
- Zero "contradictory" classifications in CRDA for D-07 to D-10; the P0 concern (Part C: contradictory classifications that are scope-incorrect) does not surface here, but the scope-disjoint test still surfaces several pairs where CRDA labelled them "complementary" or "different-perspective" when they are substantively scope-disjoint.
---
### D-07 Secure Development
---

## Part 4 — context

## GDPR
##### Art. 18(1) — Restriction grounds
**Clause: GDPR-RT13** | type: data subject right (restriction) | obligatedParty: CONTROLLER | obligationType: PER-REQUEST
**Berry anchor:** §5.4.7 (4-element OR-list (a) OR (b) OR (c) OR (d)).
**Instance 1 — COORD / S2 / `(a) OR (b) OR (c) OR (d)`**
4 disjunctive grounds; any one triggers restriction. Berry §5.4.7 menu-card pattern. S2 because all 4 grounds converge on the same restriction operation.
---
##### Art. 18(2) — Restricted processing limits
**Clause: GDPR-RT14** | type: data subject right (restriction scope) | obligatedParty: CONTROLLER | obligationType: PER-RESTRICTION-PERIOD
**Berry anchor:** §5.4.7 (`with the exception of storage, only ... with the data subject's consent OR for the establishment, exercise or defence of legal claims OR for the protection of the rights of another natural or legal person OR for reasons of important public interest`).
**Instance 1 — COORD / S3 / storage exception + 4 OR grounds**
5-way enumeration. Storage is permitted unconditionally; the 4 OR-grounds are alternatives. The `or` inclusivity question (Berry §5.1) repeats here.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Storage allowed; processing on any one of the 4 grounds sufficient. | Strict reading. |
| R2 | Storage allowed; processing requires cumulative satisfaction of multiple grounds. | Strict pro-data-subject reading. |
R1 vs R2 yield materially distinct retention-while-restricted workflows.
---
### Article 19 — Notification of rectification/erasure/restriction
#### Verbatim (with highlighting)
> **Article 19**
> **Notification obligation regarding rectification or erasure of personal data or restriction of processing**
>
> The controller shall communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Article 16, Article 17(1) and Article 18 to each recipient to whom the personal data have been disclosed, unless this proves **impossible** or involves **disproportionate effort**. The controller shall inform the data subject about those recipients if the data subject requests it.
#### Clause breakdown
##### Art. 21(3) — Absolute bar on direct-marketing after objection
**Clause: GDPR-RT17** | type: data subject right (absolute) | obligatedParty: CONTROLLER | obligationType: PER-OBJECTION
**Berry anchor:** none — Art. 21(3) is a clear absolute obligation.
**Instance 1 — none** — the clause is unambiguous: once the data subject objects to direct-marketing processing, the processing must cease. No variant readings.
---
### Article 22 — Automated individual decision-making
#### Verbatim (with highlighting)
> **Article 22**
> **Automated individual decision-making, including profiling**
>
> 1. The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her.
> 2. Paragraph 1 shall not apply if the decision:
> (a) is necessary for entering into, or performance of, a contract between the data subject and a data controller;
> (b) is authorised by Union or Member State law to which the controller is subject and which also lays down suitable measures to safeguard the data subject's rights and freedoms and legitimate interests; or
> (c) is based on the data subject's explicit consent.
> 3. In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement **suitable measures** to safeguard the data subject's rights and freedoms and legitimate interests, at least the right to obtain **human intervention** on the part of the controller, to express his or her point of view and to contest the decision.
> 4. Decisions referred to in paragraph 2 shall not be based on special categories of personal data referred to in Article 9(1), unless point (a) or (g) of Article 9(2) applies and suitable measures to safeguard the data subject's rights and freedoms and legitimate interests are in place.
#### Clause breakdown
##### Art. 22(1) — General prohibition on solely-automated decisions
**Clause: GDPR-RT18** | type: data subject right (ADM protection) | obligatedParty: CONTROLLER | obligationType: PER-DECISION
**Berry anchor:** §3.3.1 (`solely`, `significantly`).
**Instance 1 — POLY / S3 / `solely`, `similarly significantly affects`**
`Solely` excludes hybrid decisions (human review with AI recommendation) but the boundary (when does human review break the `solely` qualifier?) is undefined. `Similarly significantly affects` is undefined — what level of significance crosses the threshold?
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Solely` = no human involvement in the decision-making chain. | Strict text. |
| R2 | `Solely` = human involvement is rubber-stamping, not substantive review. | EDPB Guidelines on ADM. |
| R3 | `Solely` = human can override but AI makes the default decision. | Loose reading. |
R1 vs R3 yield materially distinct HITL (human-in-the-loop) engineering requirements.
**Variant readings for `significantly`:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Significant = financial impact, access to services, reputation. | EDPB Guidelines on ADM 2018. |
| R2 | Significant = any non-trivial impact on the data subject's life. | Strict pro-data-subject reading. |
R1 vs R2 yield materially distinct decision-classification systems.
---
##### Art. 23(1) — Permissible restriction grounds
**Clause: GDPR-RT20** | type: principle (restrictions scope) | obligatedParty: MEMBER STATE | obligationType: PER-RESTRICTION
**Berry anchor:** §5.1 (`essence of the fundamental rights and freedoms`, `necessary and proportionate`), §5.4.7 (10-element OR-list).
**Instance 1 — VAG / S3 / `essence of the fundamental rights and freedoms`**
`Essence` is Charter Art. 52(1) terminology. CJEU case law (Schrems I/II, Digital Rights Ireland) uses `essence` as a hard-test threshold but does not specify the operational test. S3 because Member State restrictions on Charter rights depend on the essence-test being met.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Essence` = the absolute core of the right (cannot be touched). | CJEU Charter interpretation. |
| R2 | `Essence` = the proportionality balance of the right. | Loose reading. |
R1 vs R2 yield materially distinct restriction-scrutiny standards.
**Instance 2 — COORD / S2 / `(a) OR (b) OR (c) OR ... (j)`**
10 disjunctive grounds (Berry §5.4.7 menu-card pattern). S2 because all 10 grounds converge on the same scrutiny mechanism.
---
### Chapter III synthesis
#### Counts
| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 27 | 20 / 20 |
| POLY | 11 | 11 / 20 |
| COORD | 12 | 12 / 20 |
| SCOPE-Q | 3 | 3 / 20 |
| **Total** | **53** | **20 / 20** |
| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 34 |
| S3 — High | 19 |
#### Recurring patterns
- `Reasonable` (Berry-flagged) appears in 8 of 20 clauses — dominant vague term of Chapter III.
- 1-month + 2-month temporal pair (Art. 12(3)) is the only hard numeric anchor in the chapter; all other timelines are vague.
- ADM (Art. 22) overlaps with AI Act Art. 13 — Chapter III Art. 22(3) `meaningful information about the logic` is the foundational obligation that the AI Act operationalises for high-risk AI.
#### Cross-clause structural observations
1. **Art. 12 is the procedural backbone.** All other rights (Art. 13–22) depend on Art. 12's response-time, identity-verification, and refusal grounds.
2. **Art. 13/14 split** — collection-source vs third-party-source information duties are structurally parallel but with different timing rules (immediate vs 1-month). The third-party-source timing is the more lenient and more often waived.
3. **Art. 15–22 cascade.** Each right (access, rectification, erasure, restriction, portability, object, ADM) inherits Art. 12's procedural rules and Art. 5(1)(d) accuracy / Art. 5(1)(c) minimisation anchors. Cross-clause implementations can reuse components.
4. **Art. 22 ADM** — the most software-impact-relevant right in GDPR, with direct overlap to AI Act's high-risk transparency requirements. Cross-regulatory coordination required.
5. **Art. 23 restrictions** — the Member State's escape valve from Chapter III. The `essence` test (Charter Art. 52(1)) is the constitutional backstop but its operationalisation is CJEU-driven.
#### Anti-pattern notes for downstream files
- Chapter IV inherits Chapter III rights via Art. 24(1) "implement appropriate technical and organisational measures" + Art. 25 by-design. `Appropriate measures` for rights-exercise includes consent-collection UIs, SAR portals, rectification workflows.
- Chapter V transfer mechanisms do not create new Chapter III rights but the Art. 15(2) right to be informed of transfer safeguards cross-references Chapter V.
##### Art. 27(2)(a) — Occasional-processing exception
**Clause: GDPR-CP06** | type: extraterritoriality exception | obligatedParty: NON-EU CONTROLLER/PROCESSOR | obligationType: PER-PROCESSING-ACTIVITY
**Berry anchor:** §5.1 (`occasional`, `large scale`, `unlikely`).
**Instance 1 — VAG / S3 / `occasional`, `large scale`, `unlikely to result in a risk`**
Three inquiry-resistant qualifiers combined with AND. The exception requires all three to fail (i.e., occasional AND small-scale AND low-risk). The boundary of each is undefined.
**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | `Occasional` = not regular/periodic; one-off processing. | EDPB Guidelines 3/2018. |
| R2 | `Occasional` = not in the controller's core business activity. | Recital 23 (non-binding). |
R1 vs R2 yield materially distinct representative-designation policies.
**Instance 2 — SCOPE-Q / S2 / `large scale`**
`large scale` is undefined; EDPB Guidelines 9/2022 (DPO designation context) attempt to fix factors (number of data subjects, volume of data, geographic range). S2 because the factors converge on the same compliance practice (large-scale determination documentation).
---
### Article 28 — Processor
#### Verbatim (with highlighting)
> **Article 28**
> **Processor**
>
> 1. Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing **sufficient guarantees** to implement **appropriate technical and organisational measures** in such a manner that processing will meet the requirements of this Regulation and ensure the protection of the rights of the data subject.
> 2. The processor shall not engage another processor without **prior specific or general written authorisation** of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of other processors, thereby giving the controller the opportunity to object to such changes.
> 3. Processing by a processor shall be governed by a **contract or other legal act** under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. That contract or other legal act shall stipulate, in particular, that the processor:
> (a) processes the personal data only on **documented instructions** from the controller (...)
> (b) ensures that persons authorised to process the personal data have committed themselves to **confidentiality** or are under an **appropriate statutory obligation of confidentiality**;
> (c) takes all measures required pursuant to Article 32;
> (d) respects the conditions referred to in paragraphs 2 and 4 for engaging another processor;
> (e) taking into account the nature of the processing, assists the controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III;
> (f) assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36 taking into account the nature of processing and the information available to the processor;
> (g) at the choice of the controller, **deletes or returns all the personal data** to the controller after the end of the provision of services relating to processing, and **deletes existing copies** unless Union or Member State law requires storage of the personal data;
> (h) makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to **audits, including inspections**, conducted by the controller or another auditor mandated by the controller.
#### Clause breakdown
## CRA
## CRA v0.2 — Articles 18–23 Economic Operators
> **Source.** OJ L, 20.11.2024, p. 42–45. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~2637–2814.
>
> **Pattern.** Articles quoted in full, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Articles 18–23 define obligations for economic operators other than the manufacturer:** authorised representatives (Art. 18), importers (Art. 19), distributors (Art. 20), substantial-modification triggers (Art. 21–22), and identification (Art. 23).
---
### 1. Atomic clause map
| Clause ID | Locus | Type | Highest Sev. | Gist |
|---|---|---|---|---|
| CRA-CL84 | Art. 18(1) (AR appointment) | AR appointment | **S2** | Manufacturer may appoint authorised representative. |
| CRA-CL85 | Art. 18(2) (AR mandate carve-out) | AR carve-out | **S2** | Art. 13(1)–(11), (12) first sub, (14) not part of AR mandate. |
| CRA-CL86 | Art. 18(3) (AR tasks) | AR tasks | **S2** | AR keeps tech docs, cooperates with MSAs. |
| CRA-CL87 | Art. 19(1) (importer compliance) | Importer duty | **S2** | Importers shall only place compliant products on market. |
| CRA-CL88 | Art. 19(2) (importer pre-market checks) | Importer checks | **S2** | Before placing: conformity assessment, tech docs, CE marking, contact info. |
| CRA-CL89 | Art. 19(3) (importer non-conformity) | Importer duty | **S2** | Importer shall not place non-conforming product; inform MSA of significant risk. |
| CRA-CL90 | Art. 19(5) (importer corrective measures) | Importer duty | **S2** | Importer immediately takes corrective measures; informs manufacturer of vulnerability. |
| CRA-CL91 | Art. 19(6) (importer documentation retention) | Retention | **S2** | Importer keeps EU declaration + tech docs for 10 years or support period. |
| CRA-CL92 | Art. 20(1) (distributor due care) | Distributor duty | **S2** | Distributors act with due care. |
| CRA-CL93 | Art. 20(2) (distributor pre-market checks) | Distributor checks | **S2** | Before making available: verify CE marking + manufacturer/importer compliance. |
| CRA-CL94 | Art. 20(3) (distributor non-conformity) | Distributor duty | **S2** | Distributor shall not make non-conforming product available; inform MSA. |
| CRA-CL95 | Art. 20(4) (distributor corrective measures) | Distributor duty | **S2** | Distributor takes corrective measures; informs manufacturer of vulnerability. |
| CRA-CL96 | Art. 21 (manufacturer-equivalent trigger) | Substantial-modification trigger | **S3** | Importer/distributor placing under own name or carrying out substantial modification = manufacturer. |
| CRA-CL97 | Art. 22(1) (third-party substantial modification) | Third-party trigger | **S2** | Third party carrying out substantial modification = manufacturer for that part (or whole). |
| CRA-CL98 | Art. 22(2) (scope of third-party obligations) | Scope | **S2** | Obligations apply to affected part or whole product. |
| CRA-CL99 | Art. 23(1) (identification duty) | Identification | **S2** | Economic operators provide supplier/recipient info to MSAs on request. |
| CRA-CL100 | Art. 23(2) (10-year retention) | Retention | **S2** | 10-year retention of supply-chain information. |
**Total: 17 atomic clauses for Art. 18–23.**
---
### 2. Detailed cards (selected)
#### 2.1 CRA-CL96 — Art. 21 — Manufacturer-equivalent trigger
**Source locus:**
> An importer or distributor shall be considered to be a manufacturer for the purposes of this Regulation and shall be subject to Articles 13 and 14, where that importer or distributor places a product with digital elements on the market **under its name or trademark** or carries out a **substantial modification** of a product with digital elements already placed on the market.
**Instance 1 — VAG — S3 — `under its name or trademark`**
`name or trademark` — what constitutes "under its name"?
- **R1:** Rebranding (white-label).
- **R2:** Co-branding.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | White-label | In-Directive: literal |
| R2 | Co-brand | None in OJ |
| R3 | Either | In-Directive: literal `under its name or trademark` |
R3 is the literal reading. S3.
*Berry anchor:* §3.3.1 (`name or trademark`).
**Instance 2 — VAG — S3 — `substantial modification`**
Inherits Art. 3(30) D30. Same POLY (affects compliance / modifies intended purpose). Propagates.
- **R1:** Any non-compliance change.
- **R2:** Material compliance change.
- **R3:** Intended-purpose modification.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any | In-Directive: Art. 3(30) literal |
| R2 | Material | None in OJ |
| R3 | Intended-purpose | In-Directive: Art. 3(30) OR |
R1/R3 are the literal reading (OR). S3.
*Berry anchor:* §3.3.1; §5.4.7 (OR).
---
#### 2.2 CRA-CL97 — Art. 22(1) — Third-party substantial modification
**Source locus:**
> A natural or legal person, other than the manufacturer, the importer or the distributor, that carries out a substantial modification of a product with digital elements and makes that product available on the market, shall be considered to be a manufacturer for the purposes of this Regulation.
**Instance 1 — POLY — S2 — `other than the manufacturer, the importer or the distributor`**
Exclusion list. Who is left?
- **R1:** Third-party integrators.
- **R2:** System integrators.
- **R3:** Any person not already classified.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Third-party integrators | In-Directive: literal |
| R2 | System integrators | None in OJ |
| R3 | Any | In-Directive: literal `other than` |
R3 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`other than`).
**Instance 2 — VAG — S2 — `carries out a substantial modification`**
`carries out` — performs the modification? authorises the modification?
- **R1:** Performs.
- **R2:** Authorises.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Performs | In-Directive: literal |
| R2 | Authorises | None in OJ |
| R3 | Either | In-Directive: literal |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`carries out`).
**Instance 3 — SCOPE-Q — S2 — `for the part of the product with digital elements that is affected by the substantial modification or, if the substantial modification has an impact on the cybersecurity of the product with digital elements as a whole, for the entire product`**
Scope of the obligation — part or whole.
- **R1:** Affected part only.
- **R2:** Entire product.
- **R3:** Either (depending on impact).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Part | In-Directive: literal |
| R2 | Entire | In-Directive: literal `if … has an impact on the cybersecurity … as a whole` |
| R3 | Either | In-Directive: literal |
R1/R3 are the literal reading (OR). S2.
*Berry anchor:* §3.3.1 (`affected`); §5.4.7 (OR).
---
## CRA v0.2 — Annex I Essential Cybersecurity Requirements
> **Source.** OJ L, 20.11.2024, p. 68–69. `03_REFERENCE_MATERIAL/Regulatory_References/CRA.txt`, lines ~4153–4234.
>
> **Pattern.** Each Part quoted verbatim with highlighting, then per-clause analysis. Universal `[recital NN]` convention.
>
> **Annex I is the binding normative core of CRA.** Part I defines security properties for products; Part II defines vulnerability-handling obligations for manufacturers. These are referenced by Art. 6, 7, 8, 13, 27, 28, 32, and are the ultimate compliance target. 21 of the 26 T2 clauses lived in Annex I.
---
### 1. Annex I — full text
#### 3.3 CRA-CL158 — Ann. II §8 — Instructions
**Source locus:**
> detailed instructions or an internet address referring to such detailed instructions and information on: (a) … (f) …
**Instance 1 — VAG — S2 — `detailed instructions`**
`detailed` — how detailed?
- **R1:** Complete security guide.
- **R2:** Summary of key points.
- **R3:** Context-dependent (based on product complexity).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Complete guide | In-Directive: literal `detailed` |
| R2 | Summary | None in OJ |
| R3 | Context-dependent | In-Directive: Art. 13(8) support period context |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`detailed`).
**Instance 2 — SCOPE-Q — S2 — `or an internet address referring to such detailed instructions`**
Alternative: physical document or URL.
- **R1:** Physical document sufficient.
- **R2:** URL sufficient.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Physical | In-Directive: literal `or` |
| R2 | URL | In-Directive: literal `internet address` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
**End of Annex II file. Next: `11_CRA_AnnexVII_TechDocumentation.md`.**
## NIS2
#### 3.3 NIS2-CL25 — Art. 22(2) — Commission selection
**Source locus:**
> The Commission, after consulting the Cooperation Group and ENISA, and, where necessary, relevant stakeholders, **<mark>shall identify the specific critical ICT services, ICT systems or ICT products</mark>** that may be subject to the coordinated security risk assessment referred to in paragraph 1.
**Instance 1 — VAG — S2 — `shall identify`**
`shall identify` — identify on what basis?
- **R1:** Identify based on sectoral risk (Annex I/II).
- **R2:** Identify based on impact (cf. Art. 2(2)(c)–(d)).
- **R3:** Identify based on stakeholder input (`where necessary, relevant stakeholders`).
- **R4:** Identify based on Commission discretion.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sectoral | In-Directive: Annex I/II |
| R2 | Impact-based | In-Directive: Art. 2(2)(c)–(d) |
| R3 | Stakeholder-input | In-Directive: literal `where necessary, relevant stakeholders` |
| R4 | Discretionary | In-Directive: literal `shall identify` is Commission-driven |
R4 is the literal reading; R3 is a procedural modifier on R4. S2.
*Berry anchor:* §3.3.1 (`shall identify`).
**Instance 2 — POLY — S2 — `specific critical ICT services, ICT systems or ICT products`**
The same `specific critical ICT` OR list as in CL23. Inherits the same readings.
*Berry anchor:* §3.3.1; §5.4.7 (OR).
**Instance 3 — VAG — S2 — `where necessary, relevant stakeholders`**
`where necessary` — soft hedge; `relevant stakeholders` — who counts as relevant?
- **R1:** Industry associations.
- **R2:** Specific entities (manufacturers, operators).
- **R3:** Standards bodies / ENISA partners.
- **R4:** All of the above.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Industry | None in OJ |
| R2 | Specific entities | None in OJ |
| R3 | Standards bodies | None in OJ |
| R4 | All | None in OJ |
R4 is the literal reading. S2.
*Berry anchor:* §5.1 (`where necessary`); §3.3.1 (`relevant stakeholders`).
---
### 4. Cross-clause structural observations (Art. 22)
1. **Art. 22 is short and discretionary.** Only 2 paragraphs; the central verb is `may` (CL23) or `shall identify` (CL25). The Cooperation Group has wide latitude; the Commission has the selection power. The operational impact is on entities only via Art. 21(3) sentence 2 propagation (NIS2-CL21 in the Art. 21 file).
2. **`specific critical ICT services, ICT systems or ICT products` recurs in CL23 and CL25.** The phrase is the EU-level supply-chain scope. The Commission selects the targets; the Cooperation Group assesses. Entities have no direct obligation under Art. 22 but inherit the propagation through Art. 21(3).
3. **`technical and, where relevant, non-technical risk factors`** is the same Berry `AND with hedge` pattern as Art. 21(2)(h) `cryptography and, where appropriate, encryption` and Art. 21(2)(j) `where appropriate`. The directive consistently uses soft hedges on the non-cyber/optional side of binary terms. **Cross-clause pattern.**
4. **No directly entity-facing obligation in Art. 22 itself.** The propagation is via Art. 21(3) sentence 2 (NIS2-CL21 in the Art. 21 file), which requires entities to "take into account the results of the coordinated security risk assessments". This is the most consequential propagation chain in Chapter IV for the supply-chain theme.
---
### 5. T3-to-v0.2 mapping
T3 had no clause for Art. 22 — it was outside the T3 cybersecurity-taxonomy subset. The v0.2 expansion adds Art. 22 with 3 atomic clauses (CL23–CL25).
| T3 clause | T3 article | v0.2 clause | v0.2 article | Notes |
|---|---|---|---|---|
| (none) | — | NIS2-CL23 | Art. 22(1) sentence 1 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL24 | Art. 22(1) sentence 2 | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL25 | Art. 22(2) | T3 omitted; v0.2 adds. |
| (none) | — | NIS2-CL21 (in Art. 21 file) | Art. 21(3) sentence 2 | The propagation hook — entities take into account the results of Art. 22 assessments. T3 omitted this propagation. |
---
**End of Art. 22 file. Next: `05_NIS2_Art23_Reporting.md` (the most consequential after Art. 21).**
#### 3.3 NIS2-CL28 — Art. 23(1) ¶1 — Cross-border information
**Source locus:**
> Each Member State shall ensure that those entities report, inter alia, any information enabling the CSIRT or, where applicable, the competent authority to determine any cross-border impact of the incident.
**Instance 1 — VAG — S2 — `inter alia`**
`inter alia` — among other things. The reporting is non-exhaustive; the entity may report more than the listed items. Standard EU drafting; the cross-border-impact info is mandatory, but other info is permitted.
*Berry anchor:* §3.3.1 (`inter alia`).
**Instance 2 — VAG — S2 — `cross-border impact`**
`cross-border impact` — impact in how many Member States? Impact of what kind?
- **R1:** Impact in two or more Member States.
- **R2:** Impact on cross-border services (single MS but cross-border flow).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ≥2 MS | In-Directive: Art. 6(7) `large-scale cybersecurity incident` |
| R2 | Cross-border services | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`cross-border`); §5.2.1 (`cross-border`).
---
#### 3.6 NIS2-CL31 — Art. 23(1) ¶3 — SPOC cross-border
**Source locus:**
> In the case of a cross-border or cross-sectoral significant incident, Member States shall ensure that their single points of contact are provided **<mark>in due time</mark>** with relevant information notified in accordance with paragraph 4.
**Instance 1 — VAG — S2 — `in due time`**
`in due time` — same Berry `undue`/`due` family but without the `undue` hedge. Slightly stronger than `without undue delay`?
- **R1:** Same as `without undue delay` (reasonable time).
- **R2:** Tighter than `without undue delay` (i.e. shorter).
- **R3:** Tied to the CSIRT/CA processing time.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Reasonable | None in OJ |
| R2 | Tighter | None in OJ |
| R3 | Tied to processing | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §5.1 (`in due time`).
**Instance 2 — VAG — S2 — `cross-border OR cross-sectoral`**
Two distinct trigger conditions. Three readings:
- **R1:** Cross-border (across MS).
- **R2:** Cross-sectoral (across sectors within or across MS).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cross-MS | In-Directive: literal `cross-border` |
| R2 | Cross-sector | In-Directive: literal `cross-sectoral` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR).
---
#### 3.17 NIS2-CL42 — Art. 23(6) — Cross-MS notification
**Source locus:**
> Where appropriate, and in particular where the significant incident concerns two or more Member States, the CSIRT, the competent authority or the single point of contact shall inform, **without undue delay**, the other affected Member States and ENISA of the significant incident.
**Instance 1 — VAG — S2 — `Where appropriate`**
Soft hedge.
**Instance 2 — VAG — S2 — `in particular where the significant incident concerns two or more Member States`**
Indicator (not definition) of when cross-MS notification is appropriate.
*Berry anchor:* §5.2.1 (`two or more`).
**Instance 3 — VAG — S2 — `without undue delay` (cross-MS)**
Same Berry `undue` term. S2.
---
#### 3.19 NIS2-CL44 — Art. 23(8) — SPOC forwarding
**Source locus:**
> At the request of the CSIRT or the competent authority, the single point of contact shall forward notifications received pursuant to paragraph 1 to the single points of contact of other affected Member States.
**Instance 1 — VAG — S2 — `At the request`**
Same on-demand trigger as CL37.
*Berry anchor:* §3.3.1 (`at the request`).
---
## DORA
#### 4.9 CL18-1 — Art. 18(1)(a) — Criterion 1 of 6 (clients/counterparts/transactions/reputation)
**Source locus:** Art. 18(1)(a). **[criterion 1 of 6 multiplicative criteria in Art. 18(1)]**
> (a) the **number and/or relevance of clients or financial counterparts affected** and, where applicable, the **amount or number of transactions affected** by the ICT-related incident, and whether the ICT-related incident has caused **reputational impact**;
**Instance 1 — POLY — S3 — `number and/or relevance of clients or financial counterparts affected`**
Three OR'd dimensions (number / relevance / financial-counterparts). Combination rule undefined.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative (number) | None in OJ |
| R2 | Qualitative (relevance) | None in OJ |
| R3 | Either | In-Directive: literal `and/or` |
| R4 | Counterparts-only | In-Directive: literal `financial counterparts` |
S3.
*Berry anchor:* §5.4.7 (AND/OR); §3.3.1 (`clients`, `financial counterparts`).
**Instance 2 — POLY — S2 — `amount or number of transactions affected`**
Two OR'd transaction measures. S2.
*Berry anchor:* §5.4.7 (OR).
**Instance 3 — VAG — S3 — `reputational impact`**
`reputational` undefined; `impact` undefined.
- **R1:** Media coverage.
- **R2:** Social-media exposure.
- **R3:** Customer-trust metrics.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Media | None in OJ |
| R2 | Social media | None in OJ |
| R3 | Customer trust | None in OJ; recital 45 |
S3.
*Berry anchor:* §5.1 (`reputational`); §3.3.1 (`impact`).
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**RTS-pending:** Art. 18(3)(a) (materiality thresholds for criterion 1).
**Proportionality-status:** Art. 4 applies.
---
#### 4.10 CL18-2 — Art. 18(1)(b) — Criterion 2 of 6 (duration)
**Source locus:** Art. 18(1)(b). **[criterion 2 of 6 multiplicative criteria in Art. 18(1)]**
> (b) the **duration of the ICT-related incident, including the service downtime**;
**Instance 1 — VAG — S2 — `duration`**
`duration` vs. `service downtime` — the relationship is undefined:
- **R1:** Duration = wall-clock time from incident start to full resolution.
- **R2:** Duration = service downtime only (excluding restoration time after which no user impact).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Wall-clock | None in OJ |
| R2 | Service downtime | In-Directive: literal `service downtime` |
R2 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`duration`, `service downtime`).
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**RTS-pending:** Art. 18(3)(a) (materiality thresholds for criterion 2).
**Proportionality-status:** Art. 4 applies.
---
#### 4.11 CL18-3 — Art. 18(1)(c) — Criterion 3 of 6 (geographical spread)
**Source locus:** Art. 18(1)(c). **[criterion 3 of 6 multiplicative criteria in Art. 18(1)]**
> (c) the **geographical spread** with regard to the areas affected by the ICT-related incident, **particularly if it affects more than two Member States**;
**Instance 1 — VAG — S3 — `geographical spread`**
The threshold is undefined (areas? countries? regions?).
- **R1:** Affected countries.
- **R2:** Affected regions within countries.
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Country-level | In-Directive: literal `Member States` reference |
| R2 | Region-level | None in OJ |
| R3 | Either | In-Directive: literal `geographical` (broad) |
S3.
*Berry anchor:* §3.3.1 (`geographical spread`); §5.2.1 (`particularly`).
**Instance 2 — POLY — S2 — `particularly if it affects more than two Member States`**
The `more than two` is illustrative (`particularly`), not exhaustive. An incident affecting 1 Member State but with major systemic impact could still qualify. S2.
*Berry anchor:* §5.2.1 (`particularly`); §5.4.5 (illustrative use).
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**RTS-pending:** Art. 18(3)(a) (materiality thresholds for criterion 3).
**Proportionality-status:** Art. 4 applies.
---
#### 4.12 CL18-4 — Art. 18(1)(d) — Criterion 4 of 6 (data losses)
**Source locus:** Art. 18(1)(d). **[criterion 4 of 6 multiplicative criteria in Art. 18(1)]**
> (d) the **data losses** that the ICT-related incident entails, in relation to **availability, authenticity, integrity or confidentiality** of data;
**Instance 1 — POLY — S3 — `data losses`**
What counts as `data loss`?
- **R1:** Loss of availability only (data inaccessible).
- **R2:** Loss of integrity (data corrupted, tampered).
- **R3:** Loss of confidentiality (data exposed).
- **R4:** Loss of authenticity (data provenance compromised).
- **R5:** All of the above (CIA+A).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Availability | In-Directive: `availability` listed |
| R2 | Integrity | In-Directive: literal `integrity` |
| R3 | Confidentiality | In-Directive: literal `confidentiality` |
| R4 | Authenticity | In-Directive: literal `authenticity` |
| R5 | All | In-Directive: literal `availability, authenticity, integrity or confidentiality` |
R5 is the literal reading. S3.
*Berry anchor:* §5.4.7 (4-way OR); §3.3.1 (`data losses`).
**Instance 2 — POLY — S2 — `availability, authenticity, integrity or confidentiality`**
Inherits DORA-D08 `ICT-related incident` POLY (NIS 2 Art. 6(1) parallel — `authenticity` undefined). S2.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`authenticity`); cf. DORA-D08.
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1); DORA-D08 POLY inheritance.
**RTS-pending:** Art. 18(3)(a).
**Proportionality-status:** Art. 4 applies.
---
#### 4.13 CL18-5 — Art. 18(1)(e) — Criterion 5 of 6 (criticality)
**Source locus:** Art. 18(1)(e). **[criterion 5 of 6 multiplicative criteria in Art. 18(1)]**
> (e) the **criticality of the services affected**, including the financial entity's transactions and operations;
**Instance 1 — VAG — S3 — `criticality`**
Inherits DORA-D22 tautology (`critical or important function` is defined tautologically via `materially impair`). S3 by structural propagation.
*Berry anchor:* §3.3.1 (`criticality`); cf. DORA-D22 (S3).
**Instance 2 — POLY — S2 — `including the financial entity's transactions and operations`**
Two service categories (AND). S2 (transactions ≠ operations but both inherit DORA-D22).
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`transactions`, `operations`).
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1); DORA-D22 tautology (S3 inheritance).
**RTS-pending:** Art. 18(3)(a).
**Proportionality-status:** Art. 4 applies.
---
#### 4.14 CL18-6 — Art. 18(1)(f) — Criterion 6 of 6 (economic impact)
**Source locus:** Art. 18(1)(f). **[criterion 6 of 6 multiplicative criteria in Art. 18(1)]**
> (f) the **economic impact**, in particular **direct and indirect costs and losses**, of the ICT-related incident in both **absolute and relative terms**.
**Instance 1 — POLY — S3 — `direct AND indirect costs AND losses`**
Three sub-attributes coordinated.
- **R1:** Direct + indirect costs only.
- **R2:** Direct + indirect losses only.
- **R3:** All four categories (costs+losses × direct+indirect).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Costs only | None in OJ |
| R2 | Losses only | None in OJ |
| R3 | All (matrix) | In-Directive: literal `direct and indirect costs and losses` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`direct`, `indirect`, `costs`, `losses`).
**Instance 2 — COORD — S2 — `absolute AND relative terms`**
Two measurement bases (AND). Both required.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`absolute`, `relative`).
**Definitional anchor:** DORA Art. 3(2) → NIS 2 Art. 6(1).
**RTS-pending:** Art. 18(3)(a).
**Proportionality-status:** Art. 4 applies.
---
#### 4.15 CL18-7 — Art. 18(2) — Significant cyber threats classification
**Source locus:** Art. 18(2).
> Financial entities shall classify cyber threats as significant based on the criticality of the services at risk, including the financial entity's transactions and operations, **number and/or relevance of clients or financial counterparts targeted** and the **geographical spread of the areas at risk**.
**Instance 1 — COORD — S3 — 3 sub-criteria combined**
Three classification criteria for `significant cyber threat`:
- Criticality of services at risk (inherits DORA-D22).
- Number/relevance of clients or financial counterparts targeted.
- Geographical spread of areas at risk.
The combination rule is undefined: all three required, any two, or any one?
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`significant`, `cyber threat`).
**Instance 2 — POLY — S2 — `number and/or relevance of clients or financial counterparts targeted`**
Same Berry `number and/or relevance` pattern as CL18-1. S2.
*Berry anchor:* §5.4.7 (AND/OR).
**Instance 3 — POLY — S2 — `geographical spread of the areas at risk`**
Same Berry `geographical spread` pattern as CL18-3. S2.
*Berry anchor:* §3.3.1 (`geographical spread`).
**Definitional anchor:** DORA Art. 3(13) `significant cyber threat` (DORA-D13); DORA-D22 tautology.
**RTS-pending:** Art. 18(3)(c) (high materiality thresholds for significant cyber threats).
**Proportionality-status:** Art. 4 applies.
---
#### 4.16 CL18-8 — Art. 18(3) — ESAs RTS mandate (criteria + thresholds)
**Source locus:** Art. 18(3).
> The ESAs shall, through the Joint Committee and in consultation with the ECB and ENISA, develop common draft regulatory technical standards further specifying the following:
>
> (a) the criteria set out in paragraph 1, including **materiality thresholds for determining major ICT-related incidents** or, as applicable, **major operational or security payment-related incidents**, that are subject to the reporting obligation laid down in Article 19(1);
>
> (b) the criteria to be applied by competent authorities for the purpose of assessing the **relevance of major ICT-related incidents** or, as applicable, major operational or security payment-related incidents, to relevant competent authorities in other Member States', and the details of reports of major ICT-related incidents or, as applicable, major operational or security payment-related incidents, to be shared with other competent authorities pursuant to Article 19(6) and (7);
>
> (c) the criteria set out in paragraph 2 of this Article, including **high materiality thresholds for determining significant cyber threats**.
**Instance 1 — VAG — S3 — `materiality thresholds for determining major ICT-related incidents`**
The hard numeric anchors (e.g. >X% downtime, >€Y economic impact, >Z clients affected) live in the RTS, not in OJ. S3 at the OJ locus because:
- **R1:** Threshold-per-criterion (6 separate thresholds, one per Art. 18(1) criterion).
- **R2:** Aggregate threshold (one master score).
- **R3:** Trigger-threshold (any one criterion exceeding its threshold = major).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per-criterion | None in OJ; recital 56 |
| R2 | Aggregate | None in OJ |
| R3 | Any-one | None in OJ |
S3.
*Berry anchor:* §5.1 (`materiality thresholds`); §3.3.1 (`major`); §3.3.1 (`major ICT-related incident`).
**Instance 2 — VAG — S3 — `major operational or security payment-related incidents`**
Cross-reference to Art. 3(11) `major operational or security payment-related incident` (DORA-D11; parallels DORA-D10 for payment sector). S3 inheritance.
*Berry anchor:* §3.3.1 (`major`, `operational`, `security`, `payment-related`).
**Instance 3 — POLY — S3 — `relevance of major ICT-related incidents` to other MS CAs**
The cross-MS relevance assessment is delegated to RTS. S3 (multi-CA assessment criteria).
*Berry anchor:* §3.3.1 (`relevance`).
**Instance 4 — VAG — S3 — `high materiality thresholds for determining significant cyber threats`**
The cyber-threat counterpart of Instance 1. Same S3.
*Berry anchor:* §5.1 (`high`); §3.3.1 (`materiality thresholds`).
**Definitional anchor:** DORA Art. 3(10) `major ICT-related incident` (DORA-D10, S3 regress); DORA-D22 tautology.
**RTS-pending:** **YES** — Art. 18(3) RTS to be submitted by **17 January 2024**. As of mid-2025, the RTS process is in the adoption pipeline (partially addressed by Reg. (EU) 2024/2956 Annex II — initial-notification content). **THE defining characteristic of Ch. III — the classification threshold has no OJ anchor.**
**Proportionality-status:** Art. 4 applies (per Art. 18(4) and recital 56).
---
#### 4.28 CL21-2 — Art. 21(3) — Report submission deadline
**Source locus:** Art. 21(3).
> The ESAs shall submit the report referred to in paragraph 1 to the European Parliament, to the Council and to the Commission by **17 January 2025**.
**Instance 1 — POLY — S2 — submission recipients (EP + Council + Commission)**
Three recipients. S2.
**Definitional anchor:** DORA-D29.
**Proportionality-status:** Art. 4 applies.
**Status note:** as of mid-2025, the deadline (17 January 2025) has passed; the ESAs Joint Committee report was published in Q1 2025 (per Council Document 5572/25 of 7 February 2025).
---
#### 4.29 CL22-1 — Art. 22(1) — Competent authority supervisory feedback
**Source locus:** Art. 22(1).
> Without prejudice to the technical input, advice or remedies and subsequent follow-up which may be provided, where applicable, in accordance with national law, by the CSIRTs under Directive (EU) 2022/2555, the competent authority shall, upon receipt of the initial notification and of each report as referred to in Article 19(4), **acknowledge receipt and may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance** to the financial entity, in particular by making available any relevant **anonymised information and intelligence** on similar threats, and may discuss **remedies applied at the level of the financial entity and ways to minimise and mitigate adverse impact across the financial sector**. Without prejudice to the supervisory feedback received, financial entities shall remain **fully responsible for the handling and for consequences of the ICT-related incidents reported pursuant to Article 19(1)**.
**Instance 1 — POLY — S3 — `may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance`**
Discretionary CA feedback. Multiple hedge modalities (`may` + `where feasible` + `relevant and proportionate` + `feedback or guidance`). The regulatory framing is: the CA acknowledges and may-but-not-must provide feedback. Three readings:
- **R1:** Mandatory feedback obligation (deep reading).
- **R2:** Discretionary feedback (literal reading).
- **R3:** Default-with-exceptions.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Mandatory | None in OJ |
| R2 | Discretionary | In-Directive: literal `may` |
| R3 | Default-with-exceptions | None in OJ |
R2 is the literal reading. R1 vs R2 admit materially distinct CA-supervision compliance populations. S3.
*Berry anchor:* §3.3.1 (`may`); §5.1 (`feasible`, `relevant`, `proportionate`).
**Instance 2 — VAG — S2 — `relevant and proportionate`**
Same two-adjective Berry pair as Art. 4(2) chapeau. S2.
*Berry anchor:* §5.1 (`relevant`, `proportionate`).
**Instance 3 — POLY — S2 — `anonymised information and intelligence`**
Two information types (AND). S2.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`anonymised`, `intelligence`).
**Instance 4 — VAG — S2 — `fully responsible for the handling and for consequences`**
Same responsibility-clause as CL19-5. S2.
*Berry anchor:* §5.1 (`fully`); §3.3.1 (`handling`, `consequences`).
**Definitional anchor:** DORA Art. 46 (CA designation).
**Scope:** regulator→financial-entity.
**Proportionality-status:** Art. 4 applies.
---
#### 4.30 CL22-2 — Art. 22(2) — ESAs yearly aggregated report
**Source locus:** Art. 22(2).
> The ESAs shall, through the Joint Committee, on an **anonymised and aggregated basis, report yearly on major ICT-related incidents**, the details of which shall be provided by competent authorities in accordance with Article 19(6), setting out at least the **number of major ICT-related incidents, their nature and their impact on the operations of financial entities or clients, remedial actions taken and costs incurred**.
>
> The ESAs shall issue **warnings and produce high-level statistics** to support ICT threat and vulnerability assessments.
**Instance 1 — POLY — S3 — `anonymised AND aggregated basis`**
Same `anonymised and aggregated` pattern as NIS 2 CL45. S2 on anonymity/aggregation; S3 on the combination rule.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`anonymised`, `aggregated`); cf. NIS 2 CL45.
**Instance 2 — POLY — S2 — `yearly` (cadence)**
Same Berry `yearly` family (cf. DORA Art. 24(6) CL24-5 `at least yearly`). S2.
*Berry anchor:* §5.7 (temporal); §5.1 (`yearly`).
**Instance 3 — POLY — S2 — 5 enumerated reporting elements**
| Element | Key ambiguity | Berry anchor |
|---|---|---|
| `number of major ICT-related incidents` | Absolute vs. normalised | §3.3.1 |
| `their nature` | Vector (attack type) vs. impact type | §3.3.1 |
| `their impact on the operations of financial entities or clients` | Internal ops vs. client-side impact | §3.3.1 |
| `remedial actions taken` | Process vs. outcome | §3.3.1 |
| `costs incurred` | Direct only vs. direct+indirect | §3.3.1 |
S2 (per element). Aggregate S3 due to `at least` (`at least` suggests the list is open).
*Berry anchor:* §5.4.5 (`at least` open-list); §3.3.1.
**Instance 4 — VAG — S2 — `warnings and high-level statistics`**
`warnings` + `high-level statistics` — two ESA output types. S2.
*Berry anchor:* §3.3.1 (`warnings`, `high-level statistics`).
**Definitional anchor:** DORA-D10.
**Scope:** regulator-internal (between ESAs and the public).
**Proportionality-status:** Art. 4 applies.
---
#### 4.31 CL23-1 — Art. 23 — Ch. III extension to operational/security payment-related incidents
**Source locus:** Art. 23 (single paragraph).
> The requirements laid down in this Chapter shall also apply to operational or security payment-related incidents and to major operational or security payment-related incidents, **where they concern credit institutions, payment institutions, account information service providers, and electronic money institutions**.
**Instance 1 — POLY — S3 — `operational OR security payment-related`**
Two payment-incident dimensions (OR).
- **R1:** Operational incidents (system availability, processing errors).
- **R2:** Security incidents (fraud, breach, unauthorised access).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational | In-Directive: literal |
| R2 | Security | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S3.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`operational`, `security`, `payment-related`).
**Instance 2 — POLY — S3 — 4 payment-entity categories**
`credit institutions` + `payment institutions` + `account information service providers` + `electronic money institutions` — four categories coordinated by commas (AND). Each entity type inherits a cross-referenced definition (see below). S3 (the combination rule is associative; in the OJ, all four categories are subject to Ch. III equally).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All four (AND) | In-Directive: literal |
| R2 | Each separately | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`credit institutions`, `payment institutions`, `AISPs`, `EMIs`).
**Definitional anchor (compound — each entity inherits from its sectoral regulation):**
| Entity | DORA Art. 3 cross-ref | Source regulation |
|---|---|---|
| `credit institution` | (31) | CRR Reg. 575/2013 Art. 4(1)(1) |
| `payment institution` | (35) | PSD2 Dir. 2015/2366 Art. 4(4) |
| `account information service provider` | (37) | PSD2 Dir. 2015/2366 Art. 33(1) |
| `electronic money institution` | (38) | EMD Dir. 2009/110/EC Art. 2(1) |
**Definitional anchor (incident cross-references):** DORA Art. 3(9) `operational or security payment-related incident` (DORA-D09); DORA Art. 3(11) `major operational or security payment-related incident` (DORA-D11 — parallels DORA-D10 S3 for the payment sector).
**Definitional anchor (definition cross-references in Art. 18):** Art. 18(3)(a) explicitly applies the materiality-threshold RTS to **major operational or security payment-related incidents** as well as major ICT-related incidents — i.e. the same Art. 18(3) RTS covers both.
**Scope:** sectoral expansion of Ch. III — same obligations, different entity classes.
**RTS-pending:** Art. 18(3)(a) (for the `major operational or security payment-related incident` threshold).
**Proportionality-status:** Art. 4 applies (the Art. 18(4) proportionality microenterprise consideration flows through).
---
### 5. T3-vs-text gaps
Per pilot convention, T3-vs-text gaps are flagged separately from linguistic ambiguities of the regulation (they are inconsistencies of the mapping layer, not of the text).
#### 6.1 Art. 18(1) — 6 multiplicative criteria with undefined combination rule (POLY/S3)
Art. 18(1) enumerates **6 specific criteria** (a)–(f) for classifying ICT-related incidents:
| # | Criterion | Cross-cuts |
|---|---|---|
| (a) | Clients/counterparts/transactions/reputational impact | Population + reputational |
| (b) | Duration including downtime | Temporal |
| (c) | Geographical spread (>2 MS trigger) | Geographic |
| (d) | Data losses (CIA+A) | Data dimension |
| (e) | Criticality of services | Operational |
| (f) | Economic impact (direct/indirect × absolute/relative) | Financial |
The OJ text says `based on the following criteria` (plural). The combination rule is itself undefined:
- **R1:** Per-criterion thresholds (6 separate thresholds; any one exceeded = major).
- **R2:** Aggregate score (one master score; aggregated metric = major).
- **R3:** Hybrid (per-criterion thresholds + aggregate ceiling).
The Art. 18(3)(a) RTS is mandated to specify `materiality thresholds for determining major ICT-related incidents`. As of mid-2025, the ESAs Joint Committee RTS is in the adoption pipeline. **Until the RTS is published, the 6-criteria combination rule is structurally ambiguous.**
- **Berry anchor:** §5.4.7 (6-way coordination); cf. CRA Annex I Part II (closed-list risk treatment catalogue).
- **Structural implication:** this is the **single deepest definitional regress** in Ch. III. The 6 criteria + undefined combination rule + RTS-pending materiality thresholds + DORA-D10 tautology + DORA-D22 tautology + Art. 3(22) tautology form a **6-layer regress** that is impossible to resolve at the OJ level alone.
- **Cross-regulation consistency:** the same pattern appears in NIS 2 Art. 23(3) (significant-incident test) and CRA Art. 14 (severe incident + implementing acts). All three regulations suffer the **threshold-in-RTS** issue. **DORA is the most verbose of the three** (6 criteria enumerated; NIS 2 has 2; CRA has 0 — fully in implementing acts).
#### 6.2 Art. 18(3) + Art. 20 — the two RTS-pending structural delegations
Ch. III contains **two pure structural delegations**:
| Delegation | Mandate | Deadline | Status (mid-2025) |
|---|---|---|---|
| **Art. 18(3) RTS** | Materiality thresholds + cross-MS relevance criteria + cyber-threat thresholds | 17 January 2024 | Deadline **passed**; RTS in adoption pipeline. |
| **Art. 20(a) RTS** | Report content + time limits + cyber-threat notification content | 17 July 2024 | Deadline **passed**; partly adopted as Reg. (EU) 2024/2956. |
| **Art. 20(b) ITS** | Standard forms, templates, procedures | 17 July 2024 | **Adopted** as Reg. (EU) 2024/2956 Annex IV. |
Together, **every operational obligation in Art. 19 (initial/intermediate/final reporting), Art. 18 (classification thresholds), and the client-notification tier in Art. 19(3) depends on these two RTS/ITS acts.** This is the defining structural characteristic of Ch. III.
- **Berry anchor:** §3.3.1 (`in accordance with`); §5.1 (`to be laid down`); §5.7 (temporal operator).
- **Structural implication:** the `RTS-pending` flag is **ubiquitous in Ch. III**. Entities cannot complete their incident-reporting system architecture without the RTS/ITS acts.
- **Cross-regulation consistency:** CRA Art. 24 has the equivalent (implementing acts for reporting under Art. 14). NIS 2 Art. 23(11) has the equivalent (implementing acts for the `significant incident` definition). All three regulations have **implementing-acts deadlines whose acts are partly or wholly published in 2024** (DORA: Reg. (EU) 2024/2956; NIS 2: not yet as of mid-2025).
#### 6.5 Art. 21 — single EU Hub feasibility report (RTS-style structural delegation)
Art. 21 mandates a **feasibility report** by the ESAs Joint Committee (in consultation with ECB and ENISA) on the potential centralisation of incident reporting through a **single EU Hub**. The report must comprise **7 elements** (a)–(g).
This is **not an obligation on financial entities** — it is a meta-procedural mandate on the ESAs. But its outcome (whether or not a single EU Hub is established) could materially alter the entity-side reporting architecture. As of Q1 2025 (post the 17 January 2025 deadline), the ESAs Joint Committee report was published; the legislative follow-up is uncertain.
- **Berry anchor:** §3.3.1 (`single EU Hub`); §5.1 (`feasibility`); §3.3.1 (`interoperability`).
- **Structural implication:** the **single EU Hub** is structurally analogous to the **NIS 2 single point of contact (SPOC)** (NIS 2 Art. 12) and the **CER Directive critical-entity framework** but at a higher integration level.
- **Layer 1 catalogue only.** Layer 2 must surface the architectural implications (sensitive-information concentration, jurisdictional sovereignty, operational resilience of the hub).
#### 6.6 Art. 22 — supervisory feedback: discretionary vs. mandatory
Art. 22(1) specifies that the competent authority **may, where feasible, provide in a timely manner relevant and proportionate feedback or high-level guidance**. The `may` is the operative trigger. Three readings (CL22-1 Instance 1): R1 mandatory, R2 discretionary (literal), R3 default-with-exceptions. R2 is the literal reading.
The structural pattern is **mandatory acknowledge + discretionary substance** — the CA must acknowledge receipt (per the `shall … acknowledge receipt and may … provide` coordination) but the substantive feedback is at CA discretion. This is **the opposite** of the NIS 2 Art. 23(5) pattern (mandatory CSIRT response within 24h), and is a deliberate DORA choice reflecting the CA-specific regulatory authority.
- **Berry anchor:** §3.3.1 (`may`); §5.1 (`feasible`, `relevant`, `proportionate`).
- **Structural implication:** Art. 22(1) creates a **discretion gap** between reporting (mandatory, Art. 19) and supervisory response (discretionary, Art. 22). This is a **closed-loop asymmetry**: entities must report; CAs may respond.
#### 6.7 Art. 23 — payment-sector extension (PSD2+EMD coverage)
Art. 23 **extends the entire Ch. III** to operational or security payment-related incidents for **4 payment-sector entity types**: credit institutions, payment institutions (PSDs Art. 4(4)), account information service providers (PSD2 Art. 33(1)), electronic money institutions (EMD Art. 2(1)).
- **Berry anchor:** §5.4.7 (AND/OR across 4 entity categories); §3.3.1 (`payment-related`).
- **Structural implication:** the **payment-sector reporting obligations are identical** to the ICT-related reporting obligations (same 3-tier structure, same CA routing). The only differentiation is the **incident type** (`operational or security payment-related` instead of `ICT-related`) and the **classification thresholds** (per Art. 18(3)(a) RTS — applies to `major operational or security payment-related incidents` alongside major ICT-related incidents).
- **Cross-regulation consistency:** Art. 23 is the **DORA↔PSD2 integration point**. Prior to DORA, payment-related incidents were reported under PSD2 Art. 96(1) with sectoral variations; DORA Art. 23 supersedes the PSD2 reporting architecture for the four entity types above.
- **Layer 1 catalogue only.** Layer 2 must surface the **PSD2 derogation analysis** (which PSD2 reporting obligations are preserved vs. replaced).
#### 4.15 CL27-1 — Art. 27(1)(a)–(e) — Tester requirements (external)
**Source locus:** Art. 27(1), five sub-points.
> Financial entities shall only use testers for the carrying out of TLPT, that:
>
> (a) **are of the highest suitability and reputability**;
>
> (b) possess **technical and organisational capabilities** and demonstrate specific expertise in **threat intelligence, penetration testing and red team testing**;
>
> (c) **are certified by an accreditation body in a Member State** or **adhere to formal codes of conduct or ethical frameworks**;
>
> (d) provide an **independent assurance, or an audit report**, in relation to the sound management of risks associated with the carrying out of TLPT, including the **due protection of the financial entity's confidential information and redress for the business risks of the financial entity**;
>
> (e) are **duly and fully covered by relevant professional indemnity insurances**, including against risks of misconduct and negligence.
**Instance 1 — VAG — S3 — `of the highest suitability and reputability` (sub-point a)**
`highest` is undefined (relative to what? `highest` among applicants? `highest` in the industry?).
- **R1:** Highest among applicants responding to the tender.
- **R2:** Highest in the industry (top decile).
- **R3:** Subjective entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Tender-relative | In-Directive: literal `highest suitability` |
| R2 | Industry-relative | None in OJ |
| R3 | Entity-relative | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`highest`); §3.3.1 (`suitability`, `reputability`).
**Instance 2 — VAG — S3 — `technical and organisational capabilities` (sub-point b)**
Same Berry pattern as GDPR Art. 32(1) (`technical and organisational measures`).
- **R1:** Both capabilities (AND).
- **R2:** Either capability (OR).
- **R3:** Coordinated (combined).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | AND | In-Directive: literal `and` |
| R2 | OR | None in OJ |
| R3 | Coordinated | None in OJ |
R1 is the literal reading. S3 (whether the tester can demonstrate one without the other is ambiguous).
*Berry anchor:* §5.4.7 (AND); §3.3.1 (`technical`, `organisational`).
**Instance 3 — POLY — S2 — `are certified by an accreditation body in a Member State or adhere to formal codes of conduct or ethical frameworks` (sub-point c)**
Two alternative paths (OR): certification OR codes of conduct.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Certification only | In-Directive: literal `certified by an accreditation body` |
| R2 | Codes of conduct only | In-Directive: literal `adhere to formal codes of conduct` |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. S2.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`accreditation body`, `formal codes`).
**Instance 4 — VAG — S3 — `independent assurance, or an audit report` (sub-point d)**
Two alternative deliverables (OR):
- **R1:** Independent assurance (e.g. SOC 2 Type II, ISAE 3402).
- **R2:** Audit report (e.g. ISO 27001 audit report).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Assurance only | None in OJ |
| R2 | Audit only | None in OJ |
| R3 | Either | In-Directive: literal `or` |
R3 is the literal reading. R1 vs R2 admit materially distinct compliance populations (assurance and audit are distinct deliverables in the assurance-services taxonomy). S3.
*Berry anchor:* §5.4.7 (OR); §3.3.1 (`assurance`, `audit report`).
**Instance 5 — VAG — S3 — `duly and fully covered by relevant professional indemnity insurances` (sub-point e)**
`duly and fully` is a compound hedge.
- **R1:** `duly` = in accordance with applicable insurance regulations; `fully` = comprehensive coverage.
- **R2:** `duly and fully` = hendiadys (single concept: complete and proper).
- **R3:** Either, per entity judgment.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Compound (two distinct qualifiers) | In-Directive: literal `duly and fully` |
| R2 | Hendiadys | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`duly`, `fully`); §5.4.7 (AND); §3.3.1 (`professional indemnity`).
**Definitional anchor:** DORA Art. 3(17) `TLPT`; DORA Art. 26(11) → TIBER-EU.
**RTS-pending:** Art. 26(11)(b) covers "the requirements and standards governing the use of internal testers" (note: this covers internal testers only; external tester requirements under Art. 27(1) are not subject to RTS).
**Proportionality-status:** Art. 4 applies.
---
#### 4.16 CL27-2 — Art. 27(2)(a)–(c) — Internal-tester additional conditions
**Source locus:** Art. 27(2).
> When using internal testers, financial entities shall ensure that, in addition to the requirements in paragraph 1, the following conditions are met:
>
> (a) such use has been **approved by the relevant competent authority or by the single public authority** designated in accordance with Article 26(9) and (10);
>
> (b) the relevant competent authority has verified that the financial entity has **sufficient dedicated resources** and ensured that **conflicts of interest are avoided** throughout the design and execution phases of the test; and
>
> (c) the threat intelligence provider is **external to the financial entity**.
**Instance 1 — VAG — S3 — `approved by the relevant competent authority or by the single public authority` (sub-point a)**
`approved` admits three readings:
- **R1:** Ex-ante approval required (before TLPT begins).
- **R2:** Ex-post approval (per CA discretion).
- **R3:** Standing approval (CA pre-approves framework; tester is approved by extension).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Ex-ante | In-Directive: literal `approved` (pre-test) |
| R2 | Ex-post | None in OJ |
| R3 | Standing | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.1 (`approved`); §3.3.1 (`competent authority`).
**Instance 2 — POLY — S2 — `sufficient dedicated resources` (sub-point b)**
`dedicated` admits two readings:
- **R1:** Fully segregated (resource cannot be shared with operational duties).
- **R2:** Allocable (resource may have a primary allocation to TLPT but can be temporarily reassigned).
- **R3:** Either.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Fully segregated | In-Directive: literal `dedicated` |
| R2 | Allocable | None in OJ |
| R3 | Either | None in OJ |
R1 is the literal reading. S2.
*Berry anchor:* §3.3.1 (`dedicated`); §5.1 (`sufficient`).
**Instance 3 — POLY — S2 — `the threat intelligence provider is external to the financial entity` (sub-point c)**
`external to the financial entity` admits two readings:
- **R1:** External to the legal entity (different corporate group).
- **R2:** External to the testing team (different team within the same entity).
- **R3:** External at the contract level (outsourced service).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Cross-entity | In-Directive: literal `external to the financial entity` |
| R2 | Cross-team | None in OJ |
| R3 | Outsourced | None in OJ |
R1 is the literal reading. R1 vs R3 admit materially distinct compliance populations (an intra-group provider under R3 is excluded under R1). S2.
*Berry anchor:* §3.3.1 (`external`); §3.3.1 (`threat intelligence provider`).
**Definitional anchor:** DORA Art. 3(17) `TLPT`; DORA Art. 26(11) → TIBER-EU.
**RTS-pending:** Art. 26(11)(b) explicitly covers "the requirements and standards governing the use of internal testers".
**Proportionality-status:** Art. 4 applies.
---
#### 6.3 Art. 27(1)–(2) — Tester independence (POLY/S3 + VAG/S3)
Art. 27 specifies five external-tester requirements (sub-points (a)–(e)) and three internal-tester additional conditions (sub-points (a)–(c)). The pattern is **stricter than Art. 24(4)** (which requires independence without specifying mechanism) and is the **only place in Ch. IV** where the regulation goes into operational detail on WHO performs the test.
- **Berry anchor:** §3.3.1 (independence); §5.1 (`highest suitability`); §3.3.1 (`professional indemnity`).
- **Structural implication:** Art. 27 creates a **two-track tester regime** — external (5 requirements) vs. internal (5 + 3 additional). The internal track is stricter on conflicts-of-interest avoidance (Art. 27(2)(b)) but allows reuse of the financial entity's own threat-intel resources, partially offset by the requirement that the **threat-intelligence provider** be external (Art. 27(2)(c)).
- **Cross-regulation consistency:** CRA Annex I Part II §3 requires `effective and regular tests and reviews` without specifying tester qualifications. NIS 2 Art. 21(2)(e) requires `policies and procedures … to assess the effectiveness of cybersecurity risk-management measures` without specifying tester qualifications. **DORA Art. 27 is the most specific tester-qualification regime in the 5-regulation corpus.** This is justified by the high-stakes nature of TLPT (live production systems, systemic risk).
#### 4.19 CL30-11 — Art. 30(3)(a) — Full SLAs + quantitative
**Source locus:** Art. 30(3)(a).
> **Full service level descriptions, including updates and revisions thereof with precise quantitative and qualitative performance targets** …. to allow **effective monitoring by the financial entity** …. and **enable appropriate corrective actions to be taken, without undue delay**, when agreed service levels are not met.
**Instance 1 — VAG — S3 — `precise quantitative and qualitative performance targets` + `without undue delay`**
Berry-flagged hendiadys on the targets; `without undue delay` is Berry-flagged temporal term (same as DORA Art. 24(1) `promptly`). Three materially distinct readings of the SLA-deepening gate:
- **R1:** Both (quantitative + qualitative); immediate upon SLA breach.
- **R2:** Either (one suffices); within agreed remediation window.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both + immediate | In-Directive: literal `and` + `without undue delay` |
| R2 | Either + window | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §5.1 (`precise`, `undue delay`); §5.7 (temporal).
**Definitional anchor:** DORA Art. 3(22) `critical or important function` (S3); Art. 30(3) chapeau (added layer for critical or important).
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No.
**Scope:** `regulator→CTPP contract` (critical/important functions only).
---
#### 4.20 CL30-12 — Art. 30(3)(b) — Notice + reporting (material impact)
**Source locus:** Art. 30(3)(b).
> **Notice periods and reporting obligations of the ICT third-party service provider** to the financial entity, including **notification of any development that might have a material impact** on the ICT third-party service provider's ability to effectively provide the ICT services ….
**Instance 1 — VAG — S3 — `material impact` + reporting cadence**
`material` is undefined (cf. CRA Annex I §1 `material risk`, NIS 2 Art. 21(2)(e) `significant harm`). Three readings of the reporting-threshold gate:
- **R1:** Quantitative threshold (% of service, financial loss).
- **R2:** Qualitative judgment (entity or CA).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Quantitative | None in OJ |
| R2 | Qualitative | In-Directive: literal `material impact` |
R2 is the literal reading. R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`material`); §3.3.1 (`material impact`).
**Definitional anchor:** DORA Art. 3(22) `critical or important function`.
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No.
**Scope:** `regulator→CTPP contract` (critical/important only).
---
#### 4.21 CL30-13 — Art. 30(3)(c) — Contingency + ICT security measures
**Source locus:** Art. 30(3)(c).
> **Requirements for the ICT third-party service provider to implement and test business contingency plans** and to have in place ICT security measures, tools and policies that provide an **appropriate level of security** for the provision of services by the financial entity in line with its regulatory framework.
**Instance 1 — VAG — S3 — `ICT security measures, tools and policies` + `appropriate level of security`**
Three-component scope (AND); `appropriate level of security` same Berry pattern as CL28-4 (Art. 28(5) `appropriate information security standards`). Three materially distinct readings:
- **R1:** All three (measures + tools + policies) + entity-defined security level.
- **R2:** Either component + industry benchmark (ISO 27001 + sectoral).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | All three + entity | In-Directive: literal `and` + `appropriate` |
| R2 | Either + industry | None in OJ |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.4.7 (AND); §5.1 (`appropriate`); §3.3.1.
**Definitional anchor:** DORA Art. 3(22) `critical or important function`.
**Proportionality-status:** Art. 4 applies.
**RTS-pending:** No.
**Scope:** `regulator→CTPP contract` (critical/important only).
---
#### 4.22 CL30-14 — Art. 30(3)(d) — TLPT cooperation
**Source locus:** Art. 30(3)(d).
> **The obligation of the ICT third-party service provider to participate and fully cooperate in the financial entity's TLPT** as referred to in Articles 26 and 27.
**Instance 1 — POLY — S3 — `participate AND fully cooperate`**
Two coordinated obligations. Three materially distinct readings of the TLPT-participation gate:
- **R1:** Both (participate + fully cooperate).
- **R2:** Either (participation by definition implies cooperation).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Both (AND) | In-Directive: literal `and` |
| R2 | Either | None in OJ |
R1 is the literal reading. S3.
*Berry anchor:* §5.4.7 (AND); §3.3.1.
**Definitional anchor:** DORA Art. 3(17) DORA-D17 `TLPT`; DORA Art. 26(11) → TIBER-EU (binding-to-non-binding regress).
**RTS-pending:** Art. 26(11) (deadline 17 July 2024, passed) — the TLPT details are subject to ESAs RTS jointly developed with ECB.
**Scope:** `regulator→CTPP contract` (critical/important only).
---
#### 4.23 CL30-15 — Art. 30(3)(e) + (f) — Monitoring rights + exit/transition
**Source locus:** Art. 30(3)(e), four sub-points (i)–(iv); and Art. 30(3)(f), two sub-points (i)–(ii); plus the penultimate microenterprise derogation paragraph.
> (e) **The right to monitor, on an ongoing basis**, …. (i) **unrestricted rights of access, inspection and audit** …. (ii) the right to agree on **alternative assurance levels** if other clients' rights are affected; (iii) **the obligation of the ICT third-party service provider to fully cooperate** during the onsite inspections …. (iv) **the obligation to provide details on the scope, procedures to be followed and frequency of such inspections and audits**.
>
> (f) **exit strategies, in particular the establishment of a mandatory adequate transition period**: (i) during which the ICT third-party service provider will **continue providing the respective functions, or ICT services** …. (ii) allowing the financial entity to **migrate to another ICT third-party service provider or change to in-house solutions** ….
>
> By way of derogation from point (e), the ICT third-party service provider and the financial entity that is a **microenterprise** may agree that the financial entity's rights of access, inspection and audit can be **delegated to an independent third party**, appointed by the ICT third-party service provider ….
**Instance 1 — VAG — S3 — `unrestricted rights of access, inspection and audit` + `alternative assurance levels` + microenterprise derogation**
Three Berry-classic terms in the audit-rights block. `unrestricted` is undefined; `alternative assurance` is undefined; the CTPP-appointed third party introduces a **conflict of interest** risk. Three materially distinct readings of the audit-rights gate:
- **R1:** Absolute right (no contractual limitations) + pooled audit + full derogation to CTPP-appointed third party.
- **R2:** Subject to reasonableness (proportionality) + third-party attestation (SOC 2 / ISAE 3402) + enhanced third-party requirements (audit by accredited third party).
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Absolute + pooled + full derogation | In-Directive: literal `unrestricted` + `delegated to an independent third party` |
| R2 | Reasonable + attestation + enhanced | In-Directive: sub-point (ii) `other clients' rights` |
R1 is the literal reading but R2 is recognised in the clause itself. S3.
*Berry anchor:* §5.1 (`unrestricted`, `alternative`, `independent`); §3.3.1.
**Instance 2 — VAG — S3 — `mandatory adequate transition period` + `migrate to another CTPP OR change to in-house solutions`**
`adequate` undefined; two migration paths (OR). Three materially distinct readings of the mandatory-transition gate:
- **R1:** Sectoral minimum transition (per CA expectations) + either migration path (FE choice).
- **R2:** Function-criticality-based transition + alternative CTPP only.
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Sectoral + either | In-Directive: literal `mandatory adequate` + `or` |
| R2 | Function-based + alternative only | In-Directive: literal `in particular` |
R1 vs R2 admit materially distinct compliance populations. S3.
*Berry anchor:* §5.1 (`mandatory adequate`); §5.4.7 (OR); §3.3.1 (`transition period`).
**Definitional anchor:** DORA Art. 3(61) DORA-D61 `Lead Overseer`; DORA Art. 3(60) DORA-D60 `microenterprise`; DORA Art. 3(22) `critical or important function` (S3).
**Proportionality-status:** Art. 4 applies (microenterprise exception is built-in).
**RTS-pending:** No (transition-period substance addressed inline; microenterprise derogation is OJ-defined).
**Scope:** `regulator→CTPP contract` (critical/important only; microenterprise derogation applies).
---
### 5. T3-vs-text gaps (catalogue only)
| Gap | Description | Affected clauses |
|---|---|---|
| **T3 omitted Art. 29 entirely** | T3 had no clause for Art. 29 (preliminary concentration risk). v0.2 adds CL29-1 + CL29-2. | CL29-1, CL29-2 |
| **T3 merged Art. 28(7)–(8)** | T3 had one umbrella clause (C36) for both termination (Art. 28(7)) and exit (Art. 28(8)). v0.2 collapses into single card CL28-5 (was separate CL28-7 + CL28-8). | CL28-5 |
| **T3 missed Art. 28(4)(c) → Art. 29 cross-reference** | T3 did not flag the explicit concentration-risk cross-reference. v0.2 surfaces in CL28-3 (Instance 1) and structural observation. | CL28-3, §6.2 |
| **T3 had one umbrella clause for Art. 30** | T3 C37/C38 covered Art. 30 at the chapeau level. v0.2 expands to 15 cards (1 chapeau + 9 sub-elements of 30(2) + 4 sub-elements of 30(3)(a)–(d) + the (3)(e)+(f) monitoring/exit block). | CL30-1 to CL30-15 |
| **T3 missed microenterprise derogation in Art. 30(3) penultimate paragraph** | T3 did not flag the `independent third party` audit-rights delegation. v0.2 surfaces in CL30-15. | CL30-15 (Instance 1) |
| **T3 missed Art. 28(9)+(10) ESAs ITS/RTS mandate** | T3 omitted the ESAs RTS on policy content and the ITS on register templates. | CL28-6 |
| **T3 missed `material` vs `significant` distinction** | Art. 28(7)(a) uses `significant breach`; Art. 30(3)(b) uses `material impact`. Same Berry pattern but distinct thresholds. | CL28-5, CL30-12 |
| **T3 missed Art. 30(3)(f) mandatory transition vs Art. 28(8) entity-defined exit** | T3 collapsed the two. v0.2 distinguishes: Art. 28(8) = entity-level exit; Art. 30(3)(f) = CTPP-side mandatory transition for critical/important. | CL28-5, CL30-15 |
| **T3 missed Art. 30(4) standard contractual clauses** | T3 omitted the "consider the use of standard contractual clauses" entity obligation. v0.2 catalogues as sub-element in CL30-1 cross-reference; full analysis in `05b`. | CL30-1 (RTS-pending note) |
---
### 6. Cross-clause structural observations
## AI_Act
_No applicable AI_Act ambiguity._

