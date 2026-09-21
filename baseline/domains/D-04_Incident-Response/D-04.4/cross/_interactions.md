# D-04.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-04.4 Data Restoration & Recovery](../../DomainAnalysis/D-04_Incident-Response/D-04.4.md)
#### D-04.4 Data Restoration & Recovery
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Part 1 §1 — Cross-Regulation Analysis context

### Summary table (corrections vs CRDA)
| Sub-domain | Pair | CRDA classification | Verified classification | Reason for change |
|---|---|---|---|---|
| D-03.3 | NIS2 ↔ DORA | Equal (E) | Complementary | DORA Art. 9(4)(c) adds the `legitimate and approved functions and activities only` qualifier; NIS2 remains model-agnostic. |
| D-04.3 | GDPR ↔ NIS2 | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | Same-party overlap exists only where a controller is also a NIS2 entity and one event is both a personal-data breach and significant incident. |
| D-04.3 | GDPR ↔ DORA | Contradictory (X) | Conditional contradiction | Both apply only on a personal-data breach that is also a major ICT-related incident at a financial entity; DORA client notification has an additional client-financial-impact condition. |
| D-04.3 | GDPR ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | AI serious incidents and personal-data breaches overlap only when role and event facts align. |
| D-04.3 | NIS2 ↔ CRA | Equal (E) | Complementary | CRA AEV track has a 14-day final tier and product/manufacturer scope; NIS2 has an entity-level 1-month final report. |
| D-04.3 | NIS2 ↔ DORA | Contradictory (X) | Conditional contradiction | DORA/NIS2 overlap depends on dual applicability; DORA financial-sector scope prevents treating all DORA incidents as NIS2-reportable by default. |
| D-04.3 | NIS2 ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | NIS2 significant incidents and AI Act serious incidents are different triggers; same-party overlap must be proven. |
| D-04.3 | CRA ↔ DORA | Contradictory (X) | Scope-disjoint baseline | Typical case is manufacturer versus financial-entity deployer; no single-party deadline collision. |
| D-04.3 | CRA ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | CRA manufacturer and AI provider/deployer roles may be split; tension exists only when the same party/system carries both roles. |
| D-04.3 | DORA ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | Financial ICT incidents and AI serious incidents overlap only for financial entities with the relevant AI role and event classification. |
| D-04.4 | NIS2 ↔ DORA | Equal (E) | Complementary | DORA has a more detailed financial-sector BC/backup/recovery overlay; it is not the same obligation as NIS2 BC/DR/CM. |
### P0 disagreement report
I disagree with any unconditional reading of the D-04.3 X cells. The OJ-derived text supports real timeline tension only when the same event triggers both regulations at the same legal party; otherwise the correct baseline is scope-disjoint coordination across different actors, recipients and event objects.
I also disagree with the CRDA EQUAL labels for NIS2↔CRA in D-04.3 and NIS2↔DORA in D-03.3/D-04.4. The source text shows similar control families, but materially different actors, object layers, final-report clocks or sector-specific qualifiers.
### Quality flags
- The pre-existing staging file contained D-03, D-04.1 and D-04.2; this pass completed D-04.3 and D-04.4 and added the correction summary.
- Source quotations are verbatim excerpts from the provided SO/SR files, not full official-journal article reproductions.
- The DORA and AI Act source files contain corrective notes on Art. 19(3), Art. 11(2) and Art. 73 timing; those caveats are preserved in the relevant pair analyses.
- Repository workflow-gate validation could not run under `.venv` because the virtual environment is absent in this workspace; structural verification was run separately after writing.
---
---
document_id: AEGIS-PREPROC-STAGE-CRDA-DEEP-PART-C
title: "Cross-Regulation Deep Analysis — Part C (D-05 + D-06)"
phase: "Pre-processing (Regulatory Baseline) — per-pair OJ-text verification"
version: 0.1
created: 2026-07-09
updated: 2026-07-09
author: "Executor C (sub-agent)"
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
scope: D-05 (Data Lifecycle, 4 sub-domains) + D-06 (Supply Chain, 4 sub-domains)
purpose: Per-pair OJ-text deep analysis verifying the CRDA pairwise classifications using the scope-disjoint test and the 5-option relationship taxonomy. CRDA is NOT modified by this analysis; findings are recommendations for the Validator and Orchestrator.
---
## Cross-Regulation Deep Analysis — Part C (D-05 + D-06)
### Methodology
#### Scope-disjoint test (the operational pivot)
For each pair (A, B) classified in CRDA, the test asks: **does A's triggering event overlap with B's triggering event at a single regulated party (controller / manufacturer / financial entity / deployer / provider) on a single occasion?**
- **Yes** → pair overlaps on the same real-world event; CRDA's substantive classification (equal / complementary / contradictory / different-perspective) is informative.
- **No** → pair's triggering events address **distinct objects at distinct actors**; the regulations do not actually impose obligations on the same party on the same occasion. The CRDA classification is then a *taxonomy* artifact (two rules happen to map to the same AEGIS sub-domain) rather than a *substantive* relationship. In this case the correct substantive classification is **SCOPE-DISJOINT**.
- **Conditional** → the pair overlaps only under specific factual circumstances; the label is correct in baseline only if the case company matches those circumstances.
#### 5 relationship classes
| Class | Test | When it applies |
|---|---|---|
| **EQUAL** | Same scope/angle, same triggering event, same addressee | NIS2 ↔ DORA on third-party risk (D-06.1); NIS2 ↔ DORA on contract clauses (D-06.3); GDPR ↔ CRA on EU-side representative designation (D-06.4) |
| **COMPLEMENTARY** | Different scope/angle but both apply on the same event | CRA + GDPR on a controller deploying a CRA-compliant product (D-05.1); NIS2 + DORA + GDPR on a financial entity's contract stack (D-06.3) |
| **DIFFERENT-PERSPECTIVE** | Same object but distinct regulatory framing | CRA ↔ DORA on supplier due diligence (D-06.1) — product-level vs entity-level perspective on the same chain |
| **CONTRADICTORY** | Mutually exclusive requirements on a single event | (Almost none found — see P0 disagreement report) |
| **SCOPE-DISJOINT** | Different objects, different actors, different triggers | CRA Annex I Part II (7)/(8) update-availability tail vs GDPR Art. 5(1)(e) retention ceiling (D-05.2) — different data, different actors, different triggers |
#### Verbatim OJ text sourcing
Verbatim text is taken from the per-regulation `02_SecurityRules_NIST.md` files (`regulatory_rationale` field of each SR, with the SR's own `source_clauses.article_ref` confirming the OJ locus). Where the OJ passage is long, the operative phrase is reproduced; the article-ref footnote points to the full article. Article text not directly quoted in a SR is drawn from the corresponding `01_SecurityObjectives.md` `source_clauses` list.
#### Relationship to CRDA
CRDA classifies pairs on a 4-way taxonomy (equal / complementary / contradictory / different-perspective). This deep analysis keeps CRDA's labels but **adds** the scope-disjoint test. Where CRDA labeled a pair "contradictory" but the scope-disjoint test shows the pair cannot both bind the same party on the same occasion, the verified relationship is **SCOPE-DISJOINT** (or **COMPLEMENTARY** if the floor-within-ceiling pattern applies). The CRDA file itself is not modified by this pilot — corrections are listed in the summary table at the end for the Validator's downstream action.
#### Frontmatter chain
This file is part of the CRDA-deep pilot chain:
- Part A (`_STAGING_crda_deep_part_A.md`) — D-01 + D-02
- Part B (`_STAGING_crda_deep_part_B.md`) — D-03 + D-04
- Part C (this file) — D-05 + D-06
- Subsequent parts — D-07 onwards
---
### D-05 Data Lifecycle

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-04.4 Data Restoration & Recovery
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md`](../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.4.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope** per AEGIS taxonomy §4.1
> as noted by `DomainAnalysis/D-04_Incident-Response/D-04.4.md` line 36:
> "AI Act Art. 15(3) backup/fail-safe plans are technical-redundancy solutions
> covered under D-01.4/D-02.1, not entity-level recovery. NIS2/DORA/CRA are
> the dedicated authorities").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-04.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-014 | Timely restoration of availability and access to personal data after physical or technical incident (with continuing confidentiality, integrity and resilience of processing systems) | Personal-data availability; controller/processor; Art. 32(1)(b)+(c) + Art. 5(1)(f) (cross) + Art. 32(2) risk-enumeration (cross); PR.IR-04 + PR.DS-11 + RC.RP-04 |
| NIS 2 | SO-NIS2-013 | Business-continuity triad (BC + backup + DR + crisis management) ensuring the ability to restore availability and integrity of network and information systems and manage crises arising from significant incidents | Entity ICT systems; all-hazards approach (Art. 21(2) chapeau + Recital 56); Art. 21(2)(c); RC.RP-04 + PR.DS-11 |
| CRA | SO-CRA-021 (cross-ref) | Preservation of availability of essential and basic functions of a product with digital elements *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and reduced incident impact via exploitation-mitigation mechanisms | Product with digital elements; manufacturer perspective; Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21); PR.IR-03 + PR.DS-12 |
| DORA | SO-DORA-010 | Comprehensive ICT BC policy with dedicated arrangements/plans/procedures/mechanisms including ICT response and recovery plans (independent internal audit for non-microenterprises), backup policies with criticality/confidentiality-graded scope and minimum frequency, and restoration and recovery procedures and methods | Financial entity; BC framework + backup architecture + audit-verified arrangements; Art. 11(1)–(3) + Art. 12(1); RC.RP-01 + PR.IR-03 + RC.RP-04 + PR.IR-04 + PR.DS-11 + RC.RP-03 |

## Validated relationships (from CRDA-deep §D-04.4)

#### Validated relationships (from CRDA-deep §D-04.4)
Of 6 pairs, **5 verified as SAME (4 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; CRDA initial classifications held after OJ-text analysis) and 1 CORRECTED** (NIS 2 ↔ DORA: CRDA `EQUAL` → verified `COMPLEMENTARY (DORA-specific overlay)` because DORA has a financial-sector BC architecture with explicit arrangements, response/recovery plans, backup-frequency criteria and audit expectations that go beyond the generic NIS 2 BC/DR/CM floor); **no SCOPE-DISJOINT classifications, no CONTRADICTORY classifications** on the recovery duty:
- **GDPR ↔ NIS 2** — COMPLEMENTARY (SAME): GDPR mandates the *outcome* (timely restoration of personal-data availability, Art. 32(1)(c)); NIS 2 mandates the *infrastructure* (BC + backup + DR + CM triad, Art. 21(2)(c)). A NIS 2-compliant BC framework operationalises the GDPR `timely manner` VAG anchor with tested recovery evidence for the personal-data subset.
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): GDPR restoration is *post-event and data-centric* (controller restores personal-data availability); CRA availability is *pre-event design-time and product-centric* (product is built to maintain essential functions during/after attack, Annex I Part I (2)(h)). CRA product resilience reduces the probability that GDPR's restoration trigger fires; it does not replace the controller's duty to restore access to personal data.
- **GDPR ↔ DORA** — COMPLEMENTARY (SAME): for a financial entity processing personal data, DORA supplies the concrete backup-and-restoration architecture that operationalises GDPR's open-textured `timely manner` requirement — DORA Art. 12(1)(a) backup scope and frequency on criticality/confidentiality + Art. 12(1)(b) restoration-and-recovery procedures and methods are the measurable implementation of GDPR Art. 32(1)(c).
- **NIS 2 ↔ CRA** — COMPLEMENTARY (SAME): NIS 2 is *entity-level* BC covering the deployer's recovery; CRA is *product-level* resilience covering the product's continued operation. Their controls stack: CRA product resilience reduces the load on the NIS 2 BC framework; NIS 2 ensures the entity can recover when products fail.
- **NIS 2 ↔ DORA** — **CORRECTED: CRDA `EQUAL` → verified `COMPLEMENTARY (DORA-specific overlay)`**: DORA is not merely the same BC obligation as NIS 2; it has a financial-sector-specific BC architecture with explicit `dedicated, appropriate and documented` arrangements (Art. 11(2) 3-way AND of adjectives + 4-way AND of artefact types = `arrangements, plans, procedures, mechanisms`), response and recovery plans (Art. 11(3); independent internal audit review for non-microenterprises), backup-frequency criteria calibrated to `criticality of information or the confidentiality level of the data` (Art. 12(1)(a)), restoration and recovery procedures and methods (Art. 12(1)(b)), and audit expectations. A DORA-compliant programme satisfies NIS 2 for the overlapping ICT subset but is not equal-to NIS 2. **DORA also carries an OJ-corrective note (v0.2 audit, material): Art. 11(2)(c)/(d)/(e) — BCP objectives mislabelled in the source SR's `regulatory_rationale`. The OJ Art. 11(2) chapeau + (a)–(e) actually reads: (a) ensure the continuity of the financial entity's critical or important functions; (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions; (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident; (d) estimate preliminary impacts, damages and losses; (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19. The SR's labels for (c)/(d)/(e) (manage crises, protect stakeholders, comply with regulatory obligations) do NOT match the OJ items.** This OJ corrective note is preserved verbatim and propagated to the DORA sub-SO below; it does not change the substantive classification (COMPLEMENTARY) but materially affects how DORA's BC-policy objectives are mapped at sub-SO level.
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA product resilience supports continued product functionality; DORA requires the financial entity to restore services and data through documented backup and recovery procedures. Neither substitutes for the other.
The recovery architecture is consistently layered: **product resilience (CRA) → entity BC + backup + DR + CM (NIS 2) → financial-entity BC framework + backup-architecture on criticality/confidentiality + restoration methods (DORA) → personal-data-specific restoration outcome (GDPR Art. 32(1)(c))**. The four regulators stack on the same party rather than contradict; the personal-data outcome is the cross-layer verification target that aggregates the three underlying layers. The high-level SO surfaces the common restoration duty; the per-reg perspective is preserved verbatim in the four sub-SOs (recovery layer, anchor, cadence/calibration, evidence template).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS 2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Conditional (controller is also NIS 2 NSIE; entity BC framework operationalises the GDPR `timely` outcome for the personal-data subset) | Conditional (Y integrated manufacturer-controller; disjoint in baseline: data-outcome ↔ product-resilience) | Conditional (DORA FE is also controller; disjoint in baseline: data-outcome ↔ backup/restore-architecture) |
| **NIS 2** | Conditional | — | Conditional (Y NIS 2 entity deploys/manufactures CRA products; disjoint baseline: entity ↔ product) | Conditional (Y cross-sector; N pure-financial via lex specialis) |
| **CRA** | Conditional (Y integrated; disjoint baseline) | Conditional (Y deployer; disjoint baseline) | — | Conditional (Y DORA FE deploys CRA product; disjoint baseline: product ↔ ICT-infrastructure) |
| **DORA** | Conditional (Y DORA-controller; disjoint baseline) | Conditional (Y cross-sector; N pure-financial lex specialis) | Conditional (Y deployer-side; disjoint baseline) | — |
Legend: **Conditional** = scope overlap only under specific circumstances
(integrated-stack manufacturer-controller, NIS 2 entity deploying CRA
products, etc.); **N** = typically disjoint (high-level SO does NOT
engage by the mere co-applicability of both regulations); CRDA-deep
scope-disjoint tests: all 6 pairs marked Conditional (Y on
vertical-integration / integrated-stack; N in baseline).

## Cross-recipient map

#### Cross-recipient map
D-04.4 itself does **not** generate recipient asymmetry — the
restoration-and-recovery process is **inward-looking** (the entity
restores its own systems/data/products and prepares the evidence trail
for compliance demonstration). The recipient fragmentation across the
four regulators is at the **downstream compliance-demonstration
point**: GDPR's supervisory authority (Art. 5(2) accountability +
Art. 32 documentation expectations); NIS 2's competent authority or
CSIRT evidence path where incident reporting (D-04.3) cascades from
the recovery event; CRA's market-surveillance authority evidence path
(Annex VII technical-documentation compliance evidence, esp. Annex VII
§6 test reports demonstrating recovery-architecture verification); and
DORA's competent authority evidence path (Art. 5(2) management-body
oversight + Art. 11(3) independent internal audit for non-microenterprises
+ Art. 12(1) backup-and-restoration documentation). These are distinct
regulatory channels but they do not generate the recovery cascade of
D-04.4 — they are compliance-evidence channels on the same recovery
event. **D-04.3 and D-09.4 are where the recipient asymmetry manifests;
D-04.4 is the restoration-and-recovery layer that produces the
accountability evidence base.**
---

## HSO considerations (from D-04.4.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations (GDPR, NIS 2, CRA, DORA) impose a restoration-and-recovery duty but each operates on a distinct recovery layer with a distinct calibration: GDPR's personal-data timely-manner restoration of availability and access (Art. 32(1)(c) + Art. 5(1)(f) cross + Art. 32(2) risk-enumeration cross; the `timely manner` VAG anchor is the personal-data-specific outcome but does NOT specify a clock — the VAG is resolved by operational layering with NIS 2 / DORA cadence); NIS 2's entity-side BC + backup + DR + CM triad (Art. 21(2)(c) + Art. 21(1) `appropriate and proportionate` + all-hazards chapeau + Recital 56); CRA's product-side intra-product availability preservation also after an incident through resilience and DoS-mitigation (Annex I Part I (2)(h) + exploitation-mitigation (2)(k) + cross-product impact containment (2)(i)); DORA's financial-entity-side comprehensive ICT BC policy with dedicated arrangements, response and recovery plans (independent internal audit for non-microenterprises), backup policies on criticality/confidentiality, and restoration/recovery procedures and methods (Art. 11(1)–(3) + Art. 12(1); subject to the OJ-corrective note on Art. 11(2)(c)/(d)/(e) objective labelling — see DORA sub-SO below).
- The high-level SO surfaces the common restoration duty (restore availability, integrity and resilience of systems, products, services, components and data; document the recovery architecture; test the recovery capability; deliver the recovery evidence); the per-regulation perspective (recovery layer, anchor, calibration/cadence, evidence template, independent-verification scope) is preserved in the four sub-SOs.
- A single organisation across all four regulators must operate a multi-layer recovery architecture with explicit layer hand-offs: CRA product resilience reduces the probability that NIS 2 entity BC framework needs to engage; NIS 2 entity BC framework + backup + DR + CM is the operational vehicle that discharges the GDPR `timely manner` outcome for non-financial entities and financial-entity-non-DORA parties; DORA Art. 11–12 is the stricter financial-sector overlay that resolves the GDPR `timely` VAG anchor via the Art. 12(1)(a) backup-scoping on criticality or confidentiality and the Art. 12(1)(b) restoration/recovery procedures and methods, with Art. 11(3) independent internal audit review for non-microenterprises as the verification floor. For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- The high-level SO does NOT collapse the four recovery layers into a single recovery event — the layers recover different objects (product-resilience vs entity-BC vs backup-architecture vs personal-data-outcome) and produce different evidence templates (resilience-architecture under Annex VII §2 vs BC plan + backup records + DR tests + CM records vs DORA backup-and-restoration documentation + audit-review records vs GDPR controller-side recovery-exercise records under Art. 5(2) + Art. 32 documentation expectations).
- The high-level SO is honesty-preserving about scope-disjoint cases: for a 5-FTE SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA applicability, only the GDPR and CRA sub-SOs activate; the high-level SO engages on the same party if both apply, with the boundary between CRA product resilience (CRA) and GDPR controller restoration outcome (GDPR) documented as the layer-segregated hand-off (CRA-product resilience reduces probability of restoration trigger; controller still owns the restoration outcome).
- DORA's Art. 12(1)(a) backup-scoping on criticality or confidentiality (VAG) + Art. 11(3) independent internal audit (non-microenterprises) is the strictest recovery-architecture floor and supports the NIS 2 `appropriate and proportionate` test on recovery depth for financial-sector entities also within retained NIS 2 scope, but does NOT make DORA co-extensive with NIS 2 (the DORA-specific overlay is material: response and recovery plans as distinct artefacts; backup-scoping on the risk-based criterion; audit-verified BC arrangements — see DORA sub-SO below).

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-04.4 over a distinct
**recovery layer**; the recovery object, the recovery anchor, the
cadence/calibration, the documented recovery evidence, and the
independent-verification scope (where applicable) all depend on which
layer the recovery event falls into.
| Axis (reg) | Recovery layer | Anchor | Cadence/calibration | Evidence template | Independent verification | Legal anchor |
|---|---|---|---|---|---|---|
| **GDPR** | data-availability outcome (controller-side, personal-data availability + integrity + resilience of processing systems) | `timely manner` (Art. 32(1)(c)) — VAG (resolved by layered BC framework cadence) | RTO/RPO defined per processing activity; tested recovery objectives | recovery-exercise records under Art. 5(2) + Art. 32 documentation; backup-test results | supervisory authority inspection (Art. 58) — not systematic | Art. 32(1)(c) + Art. 5(1)(f) (cross) + Art. 32(2) (cross) |
| **NIS 2** | entity-level BC framework (entity ICT systems, all-hazards; backup + DR + CM triad) | `business continuity, such as backup management and disaster recovery, and crisis management` (Art. 21(2)(c)) | `appropriate and proportionate` (Art. 21(1)) + all-hazards chapeau + Recital 56; BC plan + backup records + DR tests + CM records | BC plan + backup records + DR test results + CM records | Member State competent authority / CSIRT audit (no systematic internal-audit floor) | Art. 21(2)(c) + Art. 21(1) + Recital 56 |
| **CRA** | product-internal resilience + exploitation mitigation (intra-product availability after incident) | `also after an incident` (Annex I Part I (2)(h)) — design-time and runtime resilience | risk-based per Article 13(2) risk assessment + product support period | resilience architecture + exploitation-mitigation evidence in Annex VII §2 technical documentation | market-surveillance authority (Annex VII) — not systematic; manufacturer self-attestation by default | Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) |
| **DORA** | financial-entity ICT BC framework + backup-architecture on criticality/confidentiality + restoration methods | `comprehensive ICT business continuity policy` (Art. 11(1)) + `dedicated, appropriate and documented arrangements, plans, procedures and mechanisms` (Art. 11(2)) + `backup policies and procedures … based on the criticality of information or the confidentiality level of the data` (Art. 12(1)(a)) | risk-based via criticality or confidentiality tiering; tiered backup cadences (Tier 1 critical, Tier 2 standard, Tier 3 reporting) | BC policy + recovery plans + backup-and-restoration documentation + audit-review records | **independent internal audit (Art. 11(3) — non-microenterprises)** — systematic second-line / third-line assurance floor | Art. 11(1)–(3) + Art. 12(1) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-04.4.HL`) engages on a given party **if and only if ≥2 applicable
regulations' recovery-layer scope-determiners overlap on the same
party** (e.g. a controller that is also a NIS 2 essential entity
manufacturing CRA-regulated products and running a DORA-class financial
ICT system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-layer recovery architecture).
Pure co-applicability of disjoint-layer regulations on different
recovery objects does **not** trigger cross-regulation aggregation —
see the Activation logic in the file header. For a 5-FTE SaaS startup
with GDPR + CRA applicability but no NIS 2 / DORA applicability, only
the GDPR and CRA sub-SOs activate; the high-level SO engages on the
same party if both apply, with the boundary between CRA product
resilience (CRA) and GDPR controller restoration outcome (GDPR)
documented as the controlled hand-off (CRA-product resilience reduces
probability of restoration trigger; controller still owns the
restoration outcome). **The four recovery layers are layered, not
collapsed**: product resilience is operationalised inside the product
boundary (CRA); entity-level BC framework is operationalised at the
entity boundary across backup + DR + CM pillars (NIS 2);
financial-entity BC framework + backup-architecture is operationalised
at the financial-entity infrastructure layer (DORA); personal-data
restoration outcome is verified at the controller-side processing
layer (GDPR). The high-level SO surfaces the common restoration duty
but does **NOT** aggregate the per-reg recovery layer, anchor,
calibration/cadence, evidence template, or independent-verification
scope.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4.1 — AI Act Art. 15(3)
  backup/fail-safe plans are technical-redundancy solutions covered
  under D-01.4/D-02.1, not entity-level recovery).
- 6 pairwise cells, verified by CRDA-deep as **5 SAME (no further
  correction needed) + 1 CORRECTED**: GDPR↔NIS2 = COMPLEMENTARY (SAME
  — outcome ↔ infrastructure); GDPR↔CRA = DIFFERENT-PERSPECTIVE
  (SAME — post-event data-centric ↔ pre-event design-time product-centric);
  GDPR↔DORA = COMPLEMENTARY (SAME — DORA Art. 12 backup tiers
  operationalise GDPR `timely manner`); NIS2↔CRA = COMPLEMENTARY (SAME
  — entity ↔ product; layered, not overlapping); **NIS2↔DORA =
  CORRECTED — was EQUAL → COMPLEMENTARY (DORA-specific BC/backup/recovery
  overlay) — DORA is not merely the same obligation as NIS 2;
  DORA carries financial-sector arrangements, response/recovery plans,
  backup-frequency criteria on criticality or confidentiality, and
  audit expectations that go beyond the NIS 2 generic BC/DR/CM floor;
  OJ-corrective note on Art. 11(2)(c)/(d)/(e) objective labelling
  preserved in the DORA sub-SO); CRA↔DORA = COMPLEMENTARY (SAME —
  product-resilience ↔ financial-entity-BC + backup; both required,
  neither substitutes).
- The four regulations impose the **same substantive restoration-and-
  recovery duty** but each operates on a **distinct recovery layer**
  with a **distinct anchor**: personal-data-outcome (GDPR `timely
  manner` VAG), entity-BC-triad (NIS 2 `business continuity, such as
  backup management and disaster recovery, and crisis management`),
  product-internal resilience (CRA `also after an incident`),
  financial-entity-BC + backup-scoping (DORA `comprehensive ICT
  business continuity policy` + `dedicated, appropriate and
  documented` + `based on criticality or confidentiality`).
- The high-level SO describes the **COMMON OBJECTIVE** (restore the
  availability, integrity and resilience of systems, products,
  services, components and data; document the recovery architecture;
  test the recovery capability; deliver the recovery evidence); the
  **per-regulation perspective** (recovery layer, anchor,
  calibration/cadence, evidence template, independent-verification
  scope) is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified 5 of 6 pairs as non-SAME-but-SAME (CRDA initial
  classifications held) and corrected the 6th pair (NIS2↔DORA) from
  EQUAL to COMPLEMENTARY (DORA-specific overlay). The correction does
  NOT introduce a tension; it tightens the verified classification to
  what the OJ text actually says. Phase 1C Doc 07 does not need to
  resolve contradictions on D-04.4 because none exist on the
  restoration-and-recovery duty itself; the task is to **stack the
  recovery architecture** so that a single multi-layer recovery
  architecture discharges all four obligations on the same party,
  with explicit layer hand-offs at the recovery-type surfaces.
- **Scope caveat (CRITICAL — recovery-layer divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the four recovery layers into a single recovery event.
  Product-resilience events, entity-level BC events, financial-entity
  BC + backup events, and personal-data-outcome events are **distinct
  recovery objects at distinct layers**, with distinct anchors (CRA
  `also after an incident` vs NIS 2 `BC + backup + DR + CM` vs DORA
  `comprehensive ICT BC` + `criticality/confidentiality-basis`) and
  distinct evidence templates (Annex VII §2 resilience architecture vs
  BC plan + backup records + DR tests + CM records vs DORA BC policy +
  backup-and-restoration documentation + audit-review records vs GDPR
  Art. 5(2) + Art. 32 documentation). A unified BC framework may serve
  the technical substrate (e.g. a unified BC platform with multiple
  recovery pipelines), but the policy and evidence layers must remain
  **layer-segregated** for compliance demonstration. Phase 1A must
  therefore emit **four checks before applying the high-level SO** (one
  per participating regulation) to confirm that the per-reg recovery
  layer, anchor, calibration/cadence, evidence template, and
  independent-verification scope are documented separately; the
  high-level SO surfaces the common restoration duty but does NOT
  aggregate the per-reg recovery layers.
- **Scope caveat (CRITICAL — DORA BC-overlay strictness, with the
  CRDA-correction flag)** — derived from CRDA-deep verified
  classifications: DORA's Art. 11–12 BC framework is **stricter than
  NIS 2 BC/DR/CM alone** because it adds the financial-sector overlay
  (Art. 11(2) `dedicated, appropriate and documented` 3-way AND +
  Art. 11(2) 4-way AND of artefact types `arrangements, plans,
  procedures, mechanisms`; Art. 11(3) independent internal audit for
  non-microenterprises; Art. 12(1)(a) backup-scoping on criticality or
  confidentiality; Art. 12(1)(b) restoration-and-recovery procedures
  and methods). **CRDA classified this pair as EQUAL in baseline;
  CRDA-deep verified it as COMPLEMENTARY (DORA-specific overlay)**
  because a DORA-compliant programme may satisfy NIS 2 for the
  overlapping ICT subset, but DORA is not co-extensive with NIS 2 —
  the financial-sector overlay is material (response and recovery
  plans as distinct artefacts; risk-calibrated backup scoping;
  audit-verified BC arrangements). For a DORA + NIS 2 party, the
  DORA BC framework discharges the NIS 2 BC/DR/CM obligation for the
  ICT subset; the evidence layer must document which BC framework is
  operating and on which regulatory calibration. **OJ-corrective
  note (v0.2 audit, material) on DORA Art. 11(2)(c)/(d)/(e)** —
  preserved verbatim in the DORA sub-SO — the SR's `regulatory_rationale`
  labels for (c)/(d)/(e) as `manage crises`, `protect stakeholders`,
  `comply with regulatory obligations` do NOT match the OJ items,
  which actually read: (c) activate, without delay, dedicated plans
  that enable containment measures, processes and technologies
  suited to each type of ICT-related incident; (d) estimate
  preliminary impacts, damages and losses; (e) set out communication
  and crisis management actions that ensure that updated information
  is transmitted to all relevant internal staff and external
  stakeholders in accordance with Article 14, and report to the
  competent authorities in accordance with Article 19. The
  substantive classification (COMPLEMENTARY) is unaffected; the
  mapping between BC-policy objectives and sub-SO language must use
  the OJ-corrected (a)–(e) labels.
- **Scope caveat (CRITICAL — NIS 2 all-hazards extension on DORA-only
  parties)** — derived from CRDA-deep verified classifications: DORA
  Art. 11–12 is ICT-specific; NIS 2 BC/DR/CM is all-hazards (BC +
  backup + DR + CM, where CM is `crisis management` for incidents
  beyond ICT — operational, physical-environment per Recital 56).
  A DORA + NIS 2 party must extend the DORA BC framework to the NIS 2
  all-hazards scope (crisis management beyond ICT; physical-environment
  and operational hazards). For pure-financial entities (NIS 2 §9
  fall-back does not apply — DORA is lex specialis), DORA absorbs the
  NIS 2 BC/DR/CM obligation for the ICT subset; the high-level SO
  does not aggregate across the lex-specialis boundary in that
  direction for the ICT-hazard scope, but does aggregate for the
  non-ICT-hazard scope (operational + physical-environment) where NIS
  2 still binds.
- **Scope caveat (CRITICAL — CRA product-internal resilience as a
  layer, not a substitute)** — derived from CRDA-deep verified
  classifications: CRA Annex I Part I (2)(h) product-internal
  resilience does NOT substitute for entity-level recovery (NIS 2 /
  DORA). A CRA-compliant product reduces the probability that an
  entity-level recovery event materialises (the product continues to
  function during/after attack), but does not replace the
  entity-level BC framework for cases where the product itself fails
  or the attack propagates beyond the product boundary. This is
  structurally different from D-04.1 (where CRA `verifiable manner`
  is the strictest knowledge-test floor); here, CRA product
  resilience is layered *above* the entity-level BC framework as a
  prevention/mitigation layer, with the entity-level BC framework
  remaining the operational floor when the CRA product fails.
- **Scope caveat (CRITICAL — GDPR `timely manner` VAG resolution)** —
  derived from CRDA-deep verified classifications: GDPR Art. 32(1)(c)
  `timely manner` is VAG (Recital 49 attempts to fix it as "as soon
  as possible" but does not bind the controller). For non-financial
  entities subject to NIS 2, the NIS 2 BC framework cadence resolves
  the GDPR `timely` VAG via tested recovery evidence (the entity can
  document RTO per processing activity and demonstrate alignment with
  the BC framework). For financial entities subject to DORA, DORA
  Art. 12(1)(a) backup-scoping on criticality/confidentiality + Art.
  12(1)(b) restoration/recovery procedures and methods + Art. 11(3)
  independent internal audit are the measurable implementation of
  GDPR `timely manner`. For a GDPR-only party (no NIS 2 / DORA
  applicability), the controller documents `timely` via tested
  per-activity RTO/RPO targets in the BC framework (PR.DS-11 +
  RC.RP-04 anchors). The high-level SO does NOT specify a single
  clock; the calibration is delegated to the operationalising
  per-reg framework.
---

## Emergent tensions (from CRDA-deep §D-04.4)

#### Emergent tensions (from CRDA-deep §D-04.4)
None — sub-domain is **non-contradictory in baseline (5 pairs verified
as SAME: 4 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; 1 CORRECTED
NIS 2 ↔ DORA from EQUAL to COMPLEMENTARY — DORA-specific overlay;
no CRDA corrections needed beyond the one CORRECTED pair; no
SCOPE-DISJOINT, no CONTRADICTORY classifications on the
restoration-and-recovery duty itself)**. No conditional emergent
tensions on the recovery duty. The **recovery-layer divergence**
(product resilience / entity BC triad / financial-entity BC framework
with backup-architecture on criticality/confidentiality /
personal-data-specific outcome) is the **legitimately diverse
dimension**: each regulator operates on a distinct recovery layer,
and the operational convergence is on a **multi-layer recovery
architecture** with explicit layer hand-offs. The **anchor divergence**
(GDPR `timely manner` VAG / NIS 2 `BC + backup + DR + CM` S2-AND /
CRA `also after an incident` / DORA `comprehensive ICT BC` + `dedicated,
appropriate and documented` + `based on criticality or confidentiality`)
is **wording-only on a common substantive duty**; each regulator
documents its anchor for its own calibration; the restoration-and-recovery
duty itself is the same across the four regulators. The
**calibration/cadence divergence** (VAG → layered BC-framework
resolution vs `appropriate and proportionate` + all-hazards chapeau
vs Article 13(2) risk-based vs `criticality or confidentiality`-based
tiering) reflects the multi-layer recovery architecture: DORA Art.
12(1)(a) backup-tiering on criticality/confidentiality + Art. 11(3)
independent internal audit is the **strictest recovery-architecture
floor** in the AEGIS corpus and supports the NIS 2 `appropriate and
proportionate` test on recovery depth for financial-sector entities
also within retained NIS 2 scope; the DORA-specific overlay is material
and means DORA is NOT co-extensive with NIS 2 (the correction from
EQUAL to COMPLEMENTARY captures this). The **scope-disjoint divergence**
(NIS 2 §9 fall-back / DORA lex specialis on pure-financial entities)
is **handled by the lex-specialis carve-out** — DORA absorbs the NIS
2 BC/DR/CM obligation for the ICT-hazard subset on pure-financial
entities and the high-level SO does not aggregate across the
lex-specialis boundary in that direction (the NIS 2 all-hazards chapeau
still binds for operational + physical-environment hazards beyond ICT).
The high-level SO surfaces the common restoration duty; the per-reg
recovery layer, anchor, calibration/cadence, evidence template, and
independent-verification scope are documented separately in the four
sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-04.4 — with
overlapping recovery-layer scope-determiners on the same party —
operates a **multi-layer recovery architecture** with explicit layer
hand-offs. The high-level SO (`SO-D-04.4.HL`) describes the common
restoration duty (restore availability, integrity and resilience of
systems, products, services, components and data; document the
recovery architecture; test the recovery capability; deliver the
recovery evidence); the per-reg perspective is preserved in the four
sub-SOs (recovery layer, anchor, calibration/cadence, evidence
template, independent-verification scope). **No conflict-resolution
is required on D-04.4 because CRDA-deep verified 5 of 6 pairs as
SAME and corrected the 6th pair (NIS 2 ↔ DORA) from EQUAL to
COMPLEMENTARY (DORA-specific overlay) without introducing a tension.**
The CORRECTED pair means DORA has a material financial-sector BC
overlay above and beyond NIS 2 generic BC/DR/CM; the high-level SO
does not collapse this overlay. Phase 1C Doc 07 documents the
**multi-layer recovery strategy**: (1) a multi-layer recovery
architecture with explicit layer hand-offs at the recovery-type
surfaces (product-resilience ↔ entity-BC ↔ financial-entity-BC +
backup-architecture ↔ personal-data-outcome); (2) the DORA Art. 12
backup-scoping on criticality or confidentiality + Art. 11(3)
independent internal audit as the operative ceiling when both DORA
and NIS 2 apply on the same recovery event (DORA discharges the
ICT-hazard NIS 2 BC/DR/CM obligation); (3) the NIS 2 all-hazards
chapeau as the extension requirement on DORA-only parties (operational
+ physical-environment hazards beyond ICT); (4) the lex-specialis
carve-out for pure-financial entities (DORA absorbs NIS 2 BC/DR/CM
for ICT hazards; no aggregation across the boundary for ICT hazards;
aggregation only for the operational + physical-environment hazards
NIS 2 still binds); (5) the CRA product-internal resilience as a
**layer** (not a substitute) for entity-level recovery — the CRA
product reduces the probability that an entity-level recovery event
materialises, but does not replace the deployer's entity-level BC
framework; (6) the GDPR `timely manner` VAG resolution via the
per-reg operationalising framework (NIS 2 BC framework cadence for
NIS 2 + GDPR parties; DORA Art. 12 backup-tiering for DORA + GDPR
parties; per-activity RTO/RPO for GDPR-only parties); (7) the OJ-
corrected DORA Art. 11(2)(a)–(e) objective list as the authoritative
language for the DORA BC-policy-objectives mapping. For proportionality
(P2), a 5-FTE SaaS with GDPR + CRA applicability may default to
Art. 32(1)(c) tested-recovery-evidence via documented per-activity
RTO/RPO targets plus the CRA Annex I Part I (2)(h) product-internal
resilience (NIS 2 entity BC framework + DORA multi-layer recovery
are out of scope); a 500-FTE DORA financial entity must additionally
implement the Art. 11(2) `dedicated, appropriate and documented`
arrangements/plans/procedures/mechanisms with the OJ-corrected
(a)–(e) objective list, the Art. 11(3) independent internal audit
review (non-microenterprises), and the Art. 12(1)(a) backup-scoping
on criticality or confidentiality with tiered backup cadences per
`SR-DORA-015`; a DORA + NIS 2 cross-sector entity must document
both the DORA BC framework AND the NIS 2 all-hazards extension
(operational + physical-environment hazards) with explicit hand-offs
between them, including the DORA-specific overlay being preserved
verbatim in the audit-verified BC arrangements.

## Part 1 §3 — context

### 3. Security Requirements
## 4.4 Data Restoration & Recovery — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md`. See that file for cross-reg verified relationships (6 pairs verified — 5 SAME — 4 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; 1 CORRECTED — NIS 2 ↔ DORA, CRDA `EQUAL` → CRDA-deep `COMPLEMENTARY (DORA-specific overlay)` — no SCOPE-DISJOINT, no CONTRADICTORY classifications on the recovery duty), scope overlap matrix, Objective/Considerations content, recovery-layer divergence (CRA product resilience / NIS 2 entity BC triad / DORA financial-entity BC + backup-scoping / GDPR personal-data outcome), 0 emergent tensions, the DORA BC-overlay strictness flag with OJ-corrective note on Art. 11(2)(c)/(d)/(e), the CRA product-resilience layered-not-substituted caveat, the NIS 2 all-hazards extension on DORA-only parties, the GDPR `timely manner` VAG resolution via operationalising frameworks, and the Phase 1C Doc 07 multi-layer-recovery-strategy responsibility. **Scope-title note (P0):** the HSO title is `Data Restoration & Recovery` (CRDA-deep source-of-truth title — `../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/4.4.md` line 3 + `../../CrossRegulation/DomainAnalysis/D-04_Incident-Response/4.4.md` line 9 + all four per-reg SO files). The `timely manner` GDPR VAG anchor (Art. 32(1)(c) + Recital 49) is preserved verbatim in the HSO; this file does NOT collapse the four recovery layers. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act is out-of-scope per AEGIS taxonomy §4.1 per `DomainAnalysis/D-04_Incident-Response/4.4.md` line 36: "AI Act Art. 15(3) backup/fail-safe plans are technical-redundancy solutions covered under D-01.4/2.1, not entity-level recovery. NIS2/DORA/CRA are the dedicated authorities"). CRDA-deep verified 6 pairs as **5 SAME (4 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; initial CRDA classifications held) + 1 CORRECTED** (NIS 2 ↔ DORA: was EQUAL → COMPLEMENTARY (DORA-specific BC/backup/recovery overlay) — no SCOPE-DISJOINT, no CONTRADICTORY). The four regulators operate on **4 distinct recovery layers** at distinct boundaries (data-availability outcome / entity BC triad / product-internal resilience / financial-entity BC + backup-architecture) — and the four recovery layers are **layered, not collapsed**. The recovery architecture stacks: CRA product resilience (pre-event design) → NIS 2 entity BC triad (mid-layer operational vehicle) → DORA financial-entity BC + backup-scoping (financial-sector strictest overlay) → GDPR personal-data-specific outcome (top verification target aggregating the three underlying layers). The OJ-corrective note on DORA Art. 11(2)(c)/(d)/(e) is preserved verbatim in the DORA sub-SO.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 4.4
  volere_section: 15
  volere_subtype: immunity
  title: "Systems, products, services, components and data restored and recovered with documented recovery evidence at the appropriate recovery layer — multi-layer recovery architecture stacking product resilience + entity BC + financial-entity BC + personal-data outcome"
  derives_from:
    hso_sub_so: SO-4.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.4.md
    objective_ref_section: "### 4.4.0"
  description: |
    The product shall restore and recover systems, products, services, components and data with documented recovery evidence at the appropriate recovery layer — personal-data-availability outcome (Art. 32(1)(c) `timely manner` controller-side), entity-level BC + backup + DR + CM triad (Art. 21(2)(c) all-hazards), product-internal resilience + exploitation-mitigation (Annex I Part I (2)(h)/(i)/(k) `also after an incident`), or financial-entity BC framework + backup-architecture on criticality/confidentiality + restoration procedures (Art. 11(1)–(3) `dedicated, appropriate and documented` + Art. 12(1)) — via a multi-layer recovery architecture with explicit layer hand-offs, where the personal-data outcome is the cross-layer verification target aggregating the three underlying layers on the same party.
  fit_criterion: |
    A multi-layer recovery architecture is operated with one recovery pipeline per layer (personal-data outcome / entity BC triad / product-internal resilience / financial-entity BC + backup-scoping) and explicit layer hand-offs at the recovery-type surfaces; each pipeline records recovery object (personal data / ICT systems / product essential functions / financial-entity ICT), recovery anchor (`timely manner` / `BC + backup + DR + CM` / `also after an incident` / `comprehensive ICT BC` + `criticality/confidentiality`), cadence/calibration (per-activity RTO/RPO / `appropriate and proportionate` + all-hazards / Art. 13(2) risk-based / `criticality or confidentiality` tiering), evidence template (recovery-exercise records / BC plan + backup records + DR tests + CM records / Annex VII §2 resilience architecture + (2)(h)/(k)/(i) verification / DORA BC policy + backup-and-restoration documentation + audit-review records), and independent-verification scope (SA inspection / MS CA or CSIRT audit / MSA reasoned-request review / Art. 11(3) independent internal audit for non-microenterprises); the DORA Art. 11(2)/(3) `dedicated, appropriate and documented` arrangements + 4-way AND of artefacts + independent internal audit for non-microenterprises + Art. 12(1) backup-scoping on criticality/confidentiality + Art. 12(1)(b) restoration procedures is the strictest recovery-architecture floor and operates as the operative ceiling when both DORA and NIS 2 apply on the same recovery event (DORA discharges the ICT-hazard NIS 2 BC/DR/CM obligation); the OJ-corrected DORA Art. 11(2)(a)–(e) objective list (continuity of critical functions; quick response/resolution; without-delay plan activation; impact/loss estimation; communication + CA reporting per Art. 14 + Art. 19) is used as the authoritative language for the DORA BC-policy-objectives mapping; the NIS 2 all-hazards chapeau (operational + physical-environment hazards beyond ICT) is the extension requirement on DORA-only parties (DORA is ICT-specific); for pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs NIS 2 BC/DR/CM for the ICT subset; the CRA Annex I Part I (2)(h) product-internal resilience is layered as a prevention/mitigation layer above the entity-level BC framework (reduces probability of recovery trigger; does NOT substitute); the GDPR `timely manner` VAG is operationalised via tested per-activity RTO/RPO targets (GDPR-only), NIS 2 BC framework cadence (NIS 2 + GDPR), or DORA Art. 12(1)(a) backup-tiering + Art. 11(3) audit floor (DORA + GDPR); a single multi-layer recovery architecture discharges all four obligations on the same party with explicit layer hand-offs at the recovery-type surfaces (product-resilience ↔ entity-BC ↔ financial-entity-BC + backup ↔ personal-data-outcome); verified by multi-layer recovery-architecture documentation review + per-layer recovery-pipeline audit + layer hand-off protocol documentation + GDPR Art. 32(1)(c) tested-recovery-exercise records inspection (when GDPR in scope) + NIS 2 Art. 21(2)(c) BC plan + backup records + DR test results + CM records inspection (when NIS 2 in scope) + CRA Annex VII §2 (2)(h)/(i)/(k) resilience architecture + exploitation-mitigation evidence review + Annex VII §6 test-reports review (when CRA in scope) + DORA Art. 11–12 BC + backup + restoration arrangements audit + Art. 11(3) independent internal audit rec... (line truncated to 2000 chars)
  priority: MUST
  verification_method: TEST
  dependencies: [4.1 (recovery depends on a prior detection-and-triage event feeding the recovery trigger), 4.2 (recovery depends on prior containment classification feeding the recovery scope — BC framework invoked when containment is not sufficient; restoration scope determined by what was contained)]
  nist_csf: [RC.RP-01, RC.RP-03, RC.RP-04, PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages when ≥2 applicable regs target overlapping recovery layers on the same party AND ≥1 sub-SO activates (per HSO scope-overlap principle); AI Act out-of-scope per AEGIS taxonomy §4.1 (AI Act Art. 15(3) backup/fail-safe plans are technical-redundancy solutions covered under D-01.4/2.1, not entity-level recovery)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive restoration-and-recovery duty but each operates on a distinct recovery layer with a distinct calibration: GDPR personal-data outcome with `timely manner` VAG anchor (Art. 32(1)(c) + Art. 5(1)(f) cross + Art. 32(2) risk-enumeration; the `timely` anchor is resolved by operational layering with NIS 2 / DORA cadence — Recital 49's `as soon as possible` is non-binding); NIS 2 entity-side BC + backup + DR + CM triad (Art. 21(2)(c) + Art. 21(1) `appropriate and proportionate` + all-hazards chapeau + Recital 56); CRA product-side intra-product availability preservation also after an incident through resilience and DoS-mitigation (Annex I Part I (2)(h) + exploitation-mitigation (2)(k) + cross-product impact containment (2)(i)); DORA financial-entity-side comprehensive ICT BC policy with dedicated arrangements, response/recovery plans (independent internal audit for non-microenterprises), backup policies on criticality/confidentiality, and restoration/recovery procedures (Art. 11(1)–(3) + Art. 12(1) — subject to the OJ-corrective note on Art. 11(2)(c)/(d)/(e) objective labelling preserved verbatim in the DORA sub-SO). The high-level SO surfaces the common restoration duty; the per-regulation perspective (recovery layer, anchor, calibration/cadence, evidence template, independent-verification scope) is preserved in the four sub-SOs. The **0 emergent tensions** mean CRDA-deep verified 5 of 6 pairs as non-SAME-but-SAME (initial CRDA classifications held) and corrected the 6th pair (NIS 2 ↔ DORA) from EQUAL to COMPLEMENTARY (DORA-specific overlay) without introducing a tension. The CORRECTED pair means DORA has a material financial-sector BC overlay above and beyond NIS 2 generic BC/DR/CM; the high-level SO does not collapse this overlay. A unified BC framework may serve the technical substrate, but the policy and evidence layers must remain layer-segregated for compliance demonstration. The CRA product-resilience layered-not-substituted caveat is structurally different from 4.1 (where CRA `verifiable manner` is the strictest knowledge-test floor); here, CRA product resilience is layered above the entity-level BC framework as a prevention/mitigation layer, with the entity-level BC framework remaining the operational floor when the CRA product fails. (Copied from the HSO Considerations block of `### 4.4.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-04.4
title: D-04.4 Data Restoration & Recovery — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.4 Data Restoration & Recovery
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-04_Incident-Response/D-04.4.md
status: DRAFT
---
> **Deep analysis:** [D-04.4 Data Restoration & Recovery](../../DeepAnalysis/D-04_Incident-Response/D-04.4.md)
#### D-04.4 Data Restoration & Recovery
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-014 | Timely availability restoration after physical/technical incident (Art. 32(1)(b)/(c)) | Personal-data availability; controller/processor |
| NIS2 | SO-NIS2-013 | Business continuity, backup management, disaster recovery, and crisis management (Art. 21(2)(c)) | Entity ICT; BC triad |
| CRA | SO-CRA-021 (cross-ref) | Product availability preserved after incident via resilience and DoS-resistance (Annex I Part I (2)(h)) | Product with digital elements; resilience design |
| DORA | SO-DORA-010 | Comprehensive ICT BC policy with response/recovery plans, backup policies, restoration procedures (Art. 11(1)–(3) + Art. 12(1)) | Financial entity; BC framework + backup architecture |
| AI_Act | — | Out-of-scope (sole authorities: NIS2/DORA/CRA) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-04.4 per AEGIS taxonomy §4.1 — AI Act Art. 15(3) backup/fail-safe plans are technical-redundancy solutions covered under D-01.4/D-02.1, not entity-level recovery. NIS2/DORA/CRA are the dedicated authorities.
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
##### Emergent tensions (3+ regulations)
None. The recovery architecture is consistently layered: product → entity → personal-data-specific outcome. No 3-way contradiction; no non-pairwise-surfacing effect. DORA's specificity on backup scoping (criticality/confidentiality) is the only structural sharpening, and it operates within the NIS2 BC framework rather than against it.
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **RC.RP-04** (Recovery plans executed), **PR.DS-11** (Backups created and protected), and **PR.IR-04** (Adequate resource capacity). GDPR maps RC.RP-04 via SR-GDPR-024 directly. NIS2 maps PR.DS-11 via SR-NIS2-019 (the backup pillar of the BC triad). DORA maps all three via SR-DORA-015 (explicit backup policy) and SR-DORA-014 (recovery plans). CRA's resilience design is partially outside the CSF RC/PR.IR scope (it is a product-design construct mapped to PR.IR-03 + PR.DS-12, not to RC.*). The CSF 2.0 surface is consistent; the CRA-side gap is known and flagged as a product-design vs CSF-operational category mismatch.
##### Downstream implication
Phase 2 obligation derivation for D-04.4 must distinguish the `timely` GDPR anchor (VAG, requires operationalisation) from the DORA-specific backup-scoping on criticality/confidentiality (which resolves the VAG). Phase 3 case generation must verify that financial-entity case companies produce a backup-scoping matrix grounded in DORA Art. 12(1)(a), and non-financial case companies must operationalise `timely` via NIS2-derived backup-cadence requirements. CRA's product-level resilience should be referenced in Phase 2 as a control already in place when the entity's ICT estate is built on CRA-compliant products.
---
### D-05 Data Lifecycle
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-04.4
title: D-04.4 Data Restoration & Recovery — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.4 Data Restoration & Recovery
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-04_Incident-Response/D-04.4.md
status: DRAFT
---
> **Domain analysis:** [D-04.4 Data Restoration & Recovery](../../DomainAnalysis/D-04_Incident-Response/D-04.4.md)
#### D-04.4 Data Restoration & Recovery
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Part 3 — context

### Summary table (corrections vs CRDA)
| Sub-domain | Pair | CRDA classification | Verified classification | Reason for change |
|---|---|---|---|---|
| D-03.3 | NIS2 ↔ DORA | Equal (E) | Complementary | DORA Art. 9(4)(c) adds the `legitimate and approved functions and activities only` qualifier; NIS2 remains model-agnostic. |
| D-04.3 | GDPR ↔ NIS2 | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | Same-party overlap exists only where a controller is also a NIS2 entity and one event is both a personal-data breach and significant incident. |
| D-04.3 | GDPR ↔ DORA | Contradictory (X) | Conditional contradiction | Both apply only on a personal-data breach that is also a major ICT-related incident at a financial entity; DORA client notification has an additional client-financial-impact condition. |
| D-04.3 | GDPR ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | AI serious incidents and personal-data breaches overlap only when role and event facts align. |
| D-04.3 | NIS2 ↔ CRA | Equal (E) | Complementary | CRA AEV track has a 14-day final tier and product/manufacturer scope; NIS2 has an entity-level 1-month final report. |
| D-04.3 | NIS2 ↔ DORA | Contradictory (X) | Conditional contradiction | DORA/NIS2 overlap depends on dual applicability; DORA financial-sector scope prevents treating all DORA incidents as NIS2-reportable by default. |
| D-04.3 | NIS2 ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | NIS2 significant incidents and AI Act serious incidents are different triggers; same-party overlap must be proven. |
| D-04.3 | CRA ↔ DORA | Contradictory (X) | Scope-disjoint baseline | Typical case is manufacturer versus financial-entity deployer; no single-party deadline collision. |
| D-04.3 | CRA ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | CRA manufacturer and AI provider/deployer roles may be split; tension exists only when the same party/system carries both roles. |
| D-04.3 | DORA ↔ AI_Act | Contradictory (X) | Scope-disjoint baseline / conditional contradiction | Financial ICT incidents and AI serious incidents overlap only for financial entities with the relevant AI role and event classification. |
| D-04.4 | NIS2 ↔ DORA | Equal (E) | Complementary | DORA has a more detailed financial-sector BC/backup/recovery overlay; it is not the same obligation as NIS2 BC/DR/CM. |
### P0 disagreement report
I disagree with any unconditional reading of the D-04.3 X cells. The OJ-derived text supports real timeline tension only when the same event triggers both regulations at the same legal party; otherwise the correct baseline is scope-disjoint coordination across different actors, recipients and event objects.
I also disagree with the CRDA EQUAL labels for NIS2↔CRA in D-04.3 and NIS2↔DORA in D-03.3/D-04.4. The source text shows similar control families, but materially different actors, object layers, final-report clocks or sector-specific qualifiers.
### Quality flags
- The pre-existing staging file contained D-03, D-04.1 and D-04.2; this pass completed D-04.3 and D-04.4 and added the correction summary.
- Source quotations are verbatim excerpts from the provided SO/SR files, not full official-journal article reproductions.
- The DORA and AI Act source files contain corrective notes on Art. 19(3), Art. 11(2) and Art. 73 timing; those caveats are preserved in the relevant pair analyses.
- Repository workflow-gate validation could not run under `.venv` because the virtual environment is absent in this workspace; structural verification was run separately after writing.
---
---
document_id: AEGIS-PREPROC-STAGE-CRDA-DEEP-PART-C
title: "Cross-Regulation Deep Analysis — Part C (D-05 + D-06)"
phase: "Pre-processing (Regulatory Baseline) — per-pair OJ-text verification"
version: 0.1
created: 2026-07-09
updated: 2026-07-09
author: "Executor C (sub-agent)"
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
scope: D-05 (Data Lifecycle, 4 sub-domains) + D-06 (Supply Chain, 4 sub-domains)
purpose: Per-pair OJ-text deep analysis verifying the CRDA pairwise classifications using the scope-disjoint test and the 5-option relationship taxonomy. CRDA is NOT modified by this analysis; findings are recommendations for the Validator and Orchestrator.
---
## Cross-Regulation Deep Analysis — Part C (D-05 + D-06)
### Methodology
#### Scope-disjoint test (the operational pivot)
For each pair (A, B) classified in CRDA, the test asks: **does A's triggering event overlap with B's triggering event at a single regulated party (controller / manufacturer / financial entity / deployer / provider) on a single occasion?**
- **Yes** → pair overlaps on the same real-world event; CRDA's substantive classification (equal / complementary / contradictory / different-perspective) is informative.
- **No** → pair's triggering events address **distinct objects at distinct actors**; the regulations do not actually impose obligations on the same party on the same occasion. The CRDA classification is then a *taxonomy* artifact (two rules happen to map to the same AEGIS sub-domain) rather than a *substantive* relationship. In this case the correct substantive classification is **SCOPE-DISJOINT**.
- **Conditional** → the pair overlaps only under specific factual circumstances; the label is correct in baseline only if the case company matches those circumstances.
#### 5 relationship classes
| Class | Test | When it applies |
|---|---|---|
| **EQUAL** | Same scope/angle, same triggering event, same addressee | NIS2 ↔ DORA on third-party risk (D-06.1); NIS2 ↔ DORA on contract clauses (D-06.3); GDPR ↔ CRA on EU-side representative designation (D-06.4) |
| **COMPLEMENTARY** | Different scope/angle but both apply on the same event | CRA + GDPR on a controller deploying a CRA-compliant product (D-05.1); NIS2 + DORA + GDPR on a financial entity's contract stack (D-06.3) |
| **DIFFERENT-PERSPECTIVE** | Same object but distinct regulatory framing | CRA ↔ DORA on supplier due diligence (D-06.1) — product-level vs entity-level perspective on the same chain |
| **CONTRADICTORY** | Mutually exclusive requirements on a single event | (Almost none found — see P0 disagreement report) |
| **SCOPE-DISJOINT** | Different objects, different actors, different triggers | CRA Annex I Part II (7)/(8) update-availability tail vs GDPR Art. 5(1)(e) retention ceiling (D-05.2) — different data, different actors, different triggers |
#### Verbatim OJ text sourcing
Verbatim text is taken from the per-regulation `02_SecurityRules_NIST.md` files (`regulatory_rationale` field of each SR, with the SR's own `source_clauses.article_ref` confirming the OJ locus). Where the OJ passage is long, the operative phrase is reproduced; the article-ref footnote points to the full article. Article text not directly quoted in a SR is drawn from the corresponding `01_SecurityObjectives.md` `source_clauses` list.
#### Relationship to CRDA
CRDA classifies pairs on a 4-way taxonomy (equal / complementary / contradictory / different-perspective). This deep analysis keeps CRDA's labels but **adds** the scope-disjoint test. Where CRDA labeled a pair "contradictory" but the scope-disjoint test shows the pair cannot both bind the same party on the same occasion, the verified relationship is **SCOPE-DISJOINT** (or **COMPLEMENTARY** if the floor-within-ceiling pattern applies). The CRDA file itself is not modified by this pilot — corrections are listed in the summary table at the end for the Validator's downstream action.
#### Frontmatter chain
This file is part of the CRDA-deep pilot chain:
- Part A (`_STAGING_crda_deep_part_A.md`) — D-01 + D-02
- Part B (`_STAGING_crda_deep_part_B.md`) — D-03 + D-04
- Part C (this file) — D-05 + D-06
- Subsequent parts — D-07 onwards
---
### D-05 Data Lifecycle
---

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

