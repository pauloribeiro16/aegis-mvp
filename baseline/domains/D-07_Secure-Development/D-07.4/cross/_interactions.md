# D-07.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-07.4 Change Management](../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.4.md)
#### D-07.4 Change Management
<!-- participants: CRA, DORA -->
**Participants (from CRDA):** CRA, DORA
**Sole-authority note:** NIS 2 has no OJ mandate for change-management controls (CRDA confirmed); GDPR imposes process outcomes (Art. 24 review-and-update) but does not specify change-management controls. CRA Art. 13(14) and DORA Art. 9(4)(e) are dedicated authorities.

## Part 1 §1 — Cross-Regulation Analysis context

### D-08 Human Factors

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-07.4 Change Management
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md`](../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.4.md)
> (1 pair verified against OJ text — **2 participating regulations
> are CRA and DORA; GDPR, NIS 2, and AI Act are explicitly
> out-of-scope** as noted by `DomainAnalysis/D-07_Secure-Development/D-07.4.md`
> line 27: "Participants (from CRDA): CRA, DORA"; and the
> DomainAnalysis out-of-scope notes lines 30-34: "GDPR imposes process
> outcomes (Art. 24 review-and-update) but does not specify
> change-management controls ... NIS 2 has no OJ mandate for
> change-management controls (CRDA confirmed) ... AI Act does not
> impose a change-management mandate").
>
> **Sole-authority note (per CRDA-deep §D-07.4 + CRA validation report
> line 177):** NIS 2 has no OJ mandate for change-management controls
> (CRDA confirmed); GDPR imposes process outcomes (Art. 24 review-and-
> update) but does not specify change-management controls. **CRA
> Art. 13(14) + Art. 21-22 + DORA Art. 9(4)(e) are dedicated
> authorities.** AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for
> D-07.4 — CRDA-deep finds that CRA covers substantial modification
> with manufacturer-equivalent consequences and preserves CRA as
> co-equal participant (per `CRDA/03_validation_report.md` line 177).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-07.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR imposes process outcomes (Art. 24 review-and-update of technical and organisational measures) but does not specify change-management controls. | — |
| NIS2 | (out-of-scope) | NIS 2 does not impose change-management controls. CRA Art. 13(14) + Art. 21-22 + DORA Art. 9(4)(e) are dedicated authorities (per `DomainAnalysis/D-07_Secure-Development/D-07.4.md` line 32: "NIS 2 has no OJ mandate for change-management controls — CRDA confirmed"). AEGIS taxonomy marks DORA as SOLE AUTHORITY but CRA covers substantial modification. | — |
| CRA | SO-CRA-047 | Procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation; changes to the product are assessed against the conformity assessment, and where a change is a substantial modification under Art. 3(30), the entity making the modification is treated as the manufacturer with the attendant obligations (Art. 13(14) + Art. 21-22 + Art. 3(30) + Art. 13(10)). | **Product-level change management across series production** + **substantial-modification trigger with manufacturer-equivalent consequences** (Art. 22 third-party substantial-modification = manufacturer). The substantial-modification trigger (Art. 3(30) D30 — VAG+POLY+COORD-S3) fires the manufacturer-equivalent status transfer when a third party carries out a substantial modification and makes that product available on the market (Art. 22(1)) or when an importer/distributor places a product on the market under its own name/trademark or carries out a substantial modification (Art. 21). |
| DORA | SO-DORA-013 | Documented policies, procedures and controls for ICT change management — covering changes to software, hardware, firmware components, systems or security parameters — ensure that all changes are recorded, tested, assessed, approved, implemented and verified in a controlled manner, based on a risk assessment approach (Art. 9(4)(e) 5-way OR of change-targets + 6-way AND of change-management steps: recorded/tested/assessed/approved/implemented/verified + `controlled manner`). | **Entity-level change management**; **explicit OJ-mandate** under Art. 9(4)(e) (DORA is the only OJ-mandated dedicated authority for entity-level change-management-controls). The 6-step process is mandatory; the 5 change-target categories (software + hardware + firmware + systems + security parameters) are cumulative (S3 COORD). |
| AI_Act | (out-of-scope) | AI Act does not impose a change-management mandate. | — |

## Validated relationships (from CRDA-deep §D-07.4)

#### Validated relationships (from CRDA-deep §D-07.4)
Of 1 pair, **1 verified as SAME — COMPLEMENTARY (no CORRECTED, no CONTRADICTORY)** with **Conditional Y scope overlap** on the substantial-modification trigger event. The two regulators look at change management from two distinct regulatory perspectives that **stack on the Conditional-Y integrated event** (when a DORA financial entity customises a CRA-conformant product, triggering Art. 22 third-party substantial modification = manufacturer + layering DORA's six-step on top of CRA's substantial-modification trigger):
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA covers **product-level changes** (substantial modification = manufacturer via Art. 21-22 [importer/distributor + third-party modifier manufacturer-equivalent status] + series-production conformity via Art. 13(14) + substantial-modification compliance scope via Art. 13(10)) — the maker-side change management at the product-lifecycle level. DORA covers **entity-level changes** (every software/hardware/firmware/systems/security-parameter change goes through the six-step process: recorded, tested, assessed, approved, implemented, verified in a controlled manner based on a risk-assessment approach — Art. 9(4)(e)) — the user-side change management at the entity-ICT-infrastructure level. The two regimes meet at the manufacturer-customer boundary in two distinct ways: (a) the **supplier-customer boundary** where a CRA-conformant product is procured by a DORA financial entity — the CRA-side series-production conformity + DORA-side change-management six-step operate independently on the product and entity sides respectively, with the DORA six-step documentation serving as **evidence trail for CRA Art. 13(14) series-production conformity** when substantively the same change event is recorded on both sides; (b) the **Conditional-Y substantial-modification event** where a DORA financial entity customises a CRA-conformant product in a manner that triggers Art. 22 third-party substantial modification = manufacturer — the DORA entity becomes a CRA-manufacturer-equivalent with the attendant CRA obligations (Art. 13 conformity-assessment + Art. 14 AEV/SI notification + Annex I compliance + technical documentation per Annex VII) AND must continue to operate the DORA-side six-step process (Art. 9(4)(e)). The OJ literal text does not contradict; the joint addressee discharges both obligations with **layered documentation** (DORA six-step record + CRA Art. 13(14) series-production record + substantial-modification assessment per Art. 13(10) + Annex VII technical-documentation update). The **scope-disjoint test**: **Y on the substantial-modification trigger event** (Conditional Y per OJ-literal reading) — when the DORA entity customises a CRA-conformant product, the same change event triggers both regimes on a single party at a single event. **N (typically)** on the simple supplier-customer boundary (the CRA-side product change-management operates at the manufacturer side; the DORA-side entity change-management operates at the customer side; distinct parties, distinct objects).
The change-management architecture is **legitimately diverse with Conditional Y scope-overlap structure** — each regulator targets a **distinct target object** (product-level series-production conformity + substantial-modification consequences / entity-level change-management six-step) at a **distinct trigger** (manufacturer series-production event + substantial-modification event / financial-entity ICT change event) with a **distinct obligation anchor** (CRA Art. 13(14) `procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation` + Art. 21 `an importer or distributor who places a product with digital elements on the market under its own name or trademark, or who carries out a substantial modification … is considered to be the manufacturer for the purposes of the Regulation and assumes the manufacturer's obligations under Arts. 13 and 14` + Art. 22(1) `a natural or legal person, other than the manufacturer, importer, or distributor, that carries out a substantial modification … is considered to be the manufacturer for the purposes of the Regulation` + Art. 3(30) substantial-modification definition; DORA Art. 9(4)(e) `documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner`). The high-level SO surfaces the **common change-management duty** (documented change-management procedures + risk-assessment-approach + controlled-manner + 5-way OR change-targets / 6-way AND change-management steps + substantial-modification assessment + manufacturer-equivalent status consequences where applicable) while preserving the per-reg target object, trigger, anchor, threshold, evidence template, recipient.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | CRA | DORA |
|---|---|---|
| **CRA** | — | Y on the substantial-modification trigger event (when a DORA financial entity customises a CRA-conformant product in a manner that triggers Art. 22 third-party substantial modification = manufacturer — same change event triggers both regimes on a single party at a single event). N (typically) on the simple supplier-customer boundary (CRA-side product change-management at manufacturer side; DORA-side entity change-management at customer side; distinct parties, distinct objects). |
| **DORA** | Y (same; reciprocal — substantial-modification trigger event). N (typically) (same; reciprocal — supplier-customer boundary). | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional Y** (== Y on substantial-modification trigger event) = scope overlap only when the DORA financial entity customises a CRA-conformant product in a manner that triggers Art. 22 third-party substantial modification. **N (typically)** = substantive scope-disjoint on the simple supplier-customer boundary (distinct parties, distinct objects). CRDA-deep scope-disjoint tests: **CRA↔DORA = Y on substantial-modification trigger event** (per CRDA-deep §D-07.4 line 66: "Scope-disjoint test: Does this pair actually overlap on a single event at a single party? **Y (when the DORA entity customises a CRA-conformant product — Art. 22 third-party substantial modification)**"); **N (typically)** on the simple supplier-customer boundary. **No reclassification required.**

## Cross-recipient map

#### Cross-recipient map
D-07.4 generates a layered recipient set on the **change-management evidence trail**. The recipient set is at the **change-management-evidence layer**: **CRA's market surveillance authority (MSA)** on the Art. 13(14) series-production conformity procedure + Art. 21-22 substantial-modification assessment evidence + Art. 13(10) substantial-modification compliance scope + Art. 13(21) immediate corrective measures (on non-conformity — cross to D-04.2 — `SO-CRA-063`) + Annex VII §2 design/development documentation (updating the conformity-assessment record when a substantial modification occurs); **DORA's competent authority (national financial supervisory authority)** on the Art. 9(4)(e) change-management policy + the six-step change-management record (recorded/tested/assessed/approved/implemented/verified across the 5 change-target categories — software/hardware/firmware/systems/security parameters) + management body on the Art. 5(2) management-body responsibility for all arrangements related to the ICT risk-management framework. **On the Conditional-Y substantial-modification event (a DORA financial entity customises a CRA-conformant product triggering Art. 22 third-party substantial modification = manufacturer)**: the recipient set is **both** the DORA competent authority (on the DORA-side six-step record) **and** the CRA MSA (on the CRA-side Annex VII technical-documentation update + the Art. 13 conformity-assessment update + the Art. 14 AEV/SI notification if the substantial modification creates an actively-exploited-vulnerability or severe-incident event). The DORA six-step documentation can serve as **the evidence trail for CRA Art. 13(14) series-production conformity** on the same change event (per `CRDA/00_README.md` line 206: "DORA six-step documentation can serve as the evidence trail for CRA Art. 13(14) series-production conformity"); **D-07.1 (Secure-by-Design Principles) + D-07.2 (Secure Coding Practices) + D-07.3 (CI/CD Pipeline Security)** are the operational upstream artefacts whose change events flow through D-07.4's change-management procedure — D-07.4 is the **change-management gate** that records + tests + assesses + approves + implements + verifies the SDLC deliverables from the upstream artefacts.
---

## HSO considerations (from D-07.4.0 — High-level SecurityObjective)

**Considerations.**
- 2 of 5 regulations participate (CRA, DORA); GDPR, NIS 2, AI Act are explicitly out-of-scope (GDPR Art. 24 imposes review-and-update process outcomes but no change-management controls; NIS 2 has no OJ mandate for change-management controls per CRDA confirmation; AI Act does not impose a change-management mandate).
- CRA Art. 13(14) `procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation` + Art. 21-22 substantial-modification = manufacturer trigger (Art. 3(30) substantial-modification definition + Art. 13(10) substantial-modification compliance scope + Art. 13(21) immediate corrective measures on non-conformity) — product-side change-management obligation at the manufacturer side.
- DORA Art. 9(4)(e) `documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner` (5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate) — entity-side change-management obligation at the financial-entity side.
- 1 pairwise cell verified by CRDA-deep as SAME — COMPLEMENTARY with Conditional Y scope overlap on the substantial-modification trigger event: the high-level SO engages on the Conditional-Y integrated stack (when a DORA financial entity customises a CRA-conformant product in a manner that triggers Art. 22 third-party substantial modification = manufacturer — same change event triggers both regimes on a single party at a single event, layering DORA's six-step on top of CRA's substantial-modification trigger).
- On the simple supplier-customer boundary (N (typically)), the two regimes operate independently on the two sides (CRA-side series-production conformity at manufacturer + DORA-side change-management six-step at financial-entity) with the DORA six-step documentation serving as evidence trail for CRA Art. 13(14) series-production conformity when substantively the same change event is recorded on both sides.
- The two regulators stack on the substantial-modification trigger event with layered documentation (DORA six-step record + CRA Art. 13(14) series-production record + substantial-modification assessment per Art. 13(10) + Annex VII technical-documentation update).
- **AEGIS taxonomy §4.1 sole-authority disagreement (Layer 2 review item):** AEGIS taxonomy §4.1 marks DORA as the SOLE AUTHORITY for D-07.4 but CRDA-deep finds CRA Art. 13(14) + Art. 21-22 + Art. 13(10) constitute dedicated authorities for the substantial-modification trigger. CRA participation at D-07.4 is preserved as co-equal participant rather than partial-coverage cross-ref (per CRA validation report line 177). Either (a) revise the AEGIS taxonomy §4.1 to remove the DORA sole-authority assignment and add CRA as co-equal authority, or (b) identify the OJ clause that supports the DORA sole-authority reading.
- The per-reg perspective (target object, trigger, anchor, threshold, evidence template, recipient, legal anchor) is preserved verbatim in the two sub-SOs.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 2 participating regulations each define D-07.4 over a distinct **target object** of the change-management architecture; the target object, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on change management.
| Axis (reg) | Target object | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **CRA** | product-level change management across series production (Art. 13(14) continuous) + substantial-modification consequences (Art. 21-22 TRIGGERED) + substantial-modification compliance scope (Art. 13(10) TRIGGERED) + immediate corrective measures (Art. 13(21) TRIGGERED) | manufacturer series-production event (continuous) + substantial-modification event (TRIGGERED — Art. 3(30) substantial-modification definition) + manufacturer-equivalent trigger (Art. 21 importer/distributor trigger + Art. 22(1) third-party substantial-modification = manufacturer) + correction-event trigger (Art. 13(21) where manufacturer knows/has-reason-to-believe non-conformity) | `procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation` (Art. 13(14)) + `substantial modification` (Art. 3(30) D30 — VAG+POLY+COORD-S3: R1 (any non-compliance change) + R3 (intended-purpose modification) disjunctive literal reading) + `where the manufacturer knows or has reason to believe that the product with digital elements or the processes put in place by the manufacturer are not in conformity` (Art. 13(21)) — qualitative thresholds; no quantitative cadence | market surveillance authority (MSA) — Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record + Art. 13(22) MSA cooperation + Art. 14(1)/(3)/(8) AEV/SI/user-notification flows when a substantial modification creates an actively-exploited-vulnerability or severe-incident event; the user/customer as direct recipient of the change-management-related outputs (CRA-side documentation) | Art. 13(14) series-of-production conformity + Art. 3(30) substantial-modification definition + Art. 21 manufacturer-equivalent trigger + Art. 22(1) third-party substantial-modification = manufacturer + Art. 22(2) scope of obligations + Art. 13(10) substantial-modification compliance scope + Art. 13(21) immediate corrective measures + Annex VII §2 + Annex VII §3 + Art. 13(22) MSA cooperation |
| **DORA** | entity-level change management — explicit OJ-mandate six-step process (recorded/tested/assessed/approved/implemented/verified in a controlled manner based on a risk-assessment approach) | financial-entity ICT change event (continuous — every software/hardware/firmware/systems/security-parameter change goes through the six-step process) | 5-way OR change-targets (software + hardware + firmware + systems + security parameters — R1 all five in scope per S3 COORD) + 6-way AND change-management steps (recorded + tested + assessed + approved + implemented + verified — R1 cumulative all six required per S3 COORD; partial-process compliance is non-compliance) + `controlled manner` (R1 documented procedure + segregated approval R3 both per S2 VAG) + `risk assessment approach` (qualitative); no quantitative cadence; no quantitative six-step cadence | competent authority (national financial supervisory authority) — Art. 9(4)(e) change-management policy + the six-step change-management record; management body on the Art. 5(2) management-body responsibility for all arrangements related to the ICT risk-management framework | Art. 9(4)(e) 5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate + EBA Guidelines on ICT and security risk management supervisory baseline + Art. 6(1) ICT risk-management framework + Art. 5(2) management-body responsibility |

## Scope-overlap matrix (2×2)

#### Scope-overlap matrix (2×2)
(See the validated-relationships table above for the 2×2 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-07.4.HL`) engages on a given party **if and only if ≥2 applicable
regulations have a Y scope overlap on the same party on the same change
event**. **Y is returned on the substantial-modification trigger event**
when a DORA financial entity customises a CRA-conformant product in a
manner that triggers Art. 22 third-party substantial modification =
manufacturer — the same change event triggers both regimes on a single
party at a single event, layering DORA's six-step on top of CRA's
substantial-modification trigger. **For the substantial-modification
trigger event**, the DORA financial entity: (a) becomes a CRA
manufacturer-equivalent with the attendant obligations (Art. 13
conformity-assessment + Art. 14 AEV/SI notification + Annex I
compliance + Annex VII technical documentation + Art. 13(8) support
period); (b) continues to operate the DORA-side six-step process
(Art. 9(4)(e)) for the entity's ICT-infrastructure changes; (c) must
operate both regimes' change-management controls on the same change
event with **layered documentation** (DORA six-step record + CRA Art.
13(14) series-production record + substantial-modification assessment
per Art. 13(10) + Annex VII technical-documentation update); (d) the
DORA six-step documentation **can serve as the evidence trail for CRA
Art. 13(14) series-production conformity** on the same change event
(per CRDA-deep §D-07.4 line 68). **On the simple supplier-customer
boundary (N (typically))**, the CRA-side series-production conformity
operates at the manufacturer side and the DORA-side change-management
six-step operates at the customer (financial-entity) side — distinct
parties, distinct objects — but the DORA six-step record can serve as
**the evidence trail for CRA Art. 13(14) series-production conformity**
when substantively the same change event is recorded on both sides.
The two target objects are layered, not collapsed:
product-level series-production conformity + substantial-modification
consequences at the manufacturer side (CRA) /
entity-level change-management six-step at the customer side (DORA).
For a CRA-regulated manufacturer that is **not** a DORA financial
entity (CRA only), only the CRA sub-SO activates; the high-level SO is
**NOT activated** because there is no Y scope overlap on a single
change event. For a DORA financial entity that does **not** procure
CRA-conformant products (DORA only with non-CRA-classified products),
only the DORA sub-SO activates; the high-level SO is **NOT activated**
either. For a CRA-regulated manufacturer that is **also** a DORA
financial entity (the integrated manufacturer-controller-deployer
stack), the high-level SO engages for any substantial-modification
event (the DORA entity customises a CRA-conformant product in a manner
that triggers Art. 22 third-party substantial modification = 
manufacturer).

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **2 of 5 regulations participate** (CRA, DORA; **GDPR, NIS 2, AI Act
  are explicitly out-of-scope** — GDPR Art. 24 imposes process
  outcomes (review-and-update) but no change-management controls; NIS 2
  has no OJ mandate for change-management controls (CRDA confirmed);
  AI Act does not impose a change-management mandate).
- **1 pairwise cell, verified by CRDA-deep as 1 SAME — COMPLEMENTARY
  with Conditional Y scope overlap on the substantial-modification
  trigger event:** CRA↔DORA (SAME — COMPLEMENTARY with Y on the
  substantial-modification event + N (typically) on the simple
  supplier-customer boundary).
- The two regulations impose **distinct change-management duties** at
  **distinct target objects** with **distinct triggers** and
  **distinct anchors**: CRA manufacturer-side product-level change
  management across series production (Art. 13(14) `procedures are in
  place for products with digital elements that are part of a series of
  production to remain in conformity with this Regulation` + series-
  of-production + Annex VII §2 documentation + Art. 3(30) substantial-
  modification definition + Art. 21-22 manufacturer-equivalent trigger)
  with substantial-modification consequences (Art. 13(10) compliance
  scope + Art. 13(21) immediate corrective measures + Annex VII
  technical-documentation update + Art. 14 AEV/SI notification if the
  substantial modification creates an actively-exploited-vulnerability
  or severe-incident event); DORA financial-entity-side entity-level
  change management (Art. 9(4)(e) 5-way OR change-targets + 6-way AND
  change-management steps + `controlled manner` mandate + risk-
  assessment-approach + EBA Guidelines supervisory baseline). The two
  regimes meet at the substantial-modification trigger event (Y scope
  overlap on the same change event when a DORA financial entity
  customises a CRA-conformant product).
- The high-level SO describes the **COMMON OBJECTIVE** (documented
  change-management procedures + risk-assessment-approach + controlled-
  manner + 5-way OR change-targets / 6-way AND change-management steps
  + substantial-modification assessment + manufacturer-equivalent
  status consequences where applicable); the **per-regulation
  perspective** (target object, trigger, anchor, threshold, recipient,
  evidence template) is preserved verbatim in the two sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension on the change-management duty itself — **0 CONTRADICTORY or
  CORRECTED reclassifications** because the 1 verified pair is SAME —
  COMPLEMENTARY. The **Y scope overlap on the substantial-modification
  trigger event** is the gating condition for the high-level SO to
  engage; on the simple supplier-customer boundary (N (typically)), the
  two regimes operate independently with the DORA six-step
  documentation serving as evidence trail for CRA Art. 13(14)
  series-production conformity when substantively the same change
  event is recorded on both sides. **No Phase 1C tension resolution is
  required** for D-07.4 — Phase 1C Doc 07 documents the
  change-management strategy without resolving a change-management
  contradiction because none exists by construction. The **AEGIS
  taxonomy §4.1 sole-authority disagreement** (AEGIS marks DORA as
  SOLE AUTHORITY; CRDA-deep finds CRA Art. 13(14) + Art. 21-22 + Art.
  13(10) constitute dedicated authorities for the substantial-
  modification trigger) is a **structural Layer 2 review item** — the
  CRA participation at D-07.4 is preserved here as co-equal participant
  rather than partial-coverage cross-ref (per CRA validation report
  line 177: "AEGIS taxonomy marks DORA as SOLE AUTHORITY but CRA
  covers substantial modification"). Layer 2 review item: either (a)
  revise the AEGIS taxonomy §4.1 to remove the DORA sole-authority
  assignment and add CRA as co-equal authority, or (b) identify the OJ
  clause that supports the DORA sole-authority reading — but the
  CRDA-deep verification finds the substantial-modification trigger
  is a CRA-side OJ-mandated event that the DORA-side six-step + 
  Art. 22 third-party-substantial-modification = manufacturer
  mechanism acknowledges when both regimes apply.
- **Scope caveat (CRITICAL — AEGIS taxonomy §4.1 sole-authority
  disagreement)** — derived from CRDA-deep verified classifications:
  AEGIS taxonomy §4.1 marks DORA as the SOLE AUTHORITY for D-07.4
  Change Management. The CRDA-deep OJ-text verification finds that
  CRA Art. 13(14) + Art. 21-22 + Art. 13(10) constitute dedicated
  authorities for the substantial-modification trigger with
  manufacturer-equivalent consequences (Art. 22 third-party
  substantial-modification = manufacturer). The CRA participation at
  D-07.4 is preserved here as **co-equal participant** rather than as
  partial-coverage cross-ref per CRA `03_validation_report.md` line
  177: "AEGIS taxonomy marks DORA as SOLE AUTHORITY but CRA covers
  substantial modification." Layer 2 review item: either (a) revise
  the AEGIS taxonomy §4.1 to remove the DORA sole-authority
  assignment and add CRA as co-equal authority, or (b) identify the OJ
  clause that supports the DORA sole-authority reading. **For a 5-FTE
  CRA-regulated manufacturer that is not a DORA financial entity**,
  the change-management obligation is the CRA Art. 13(14)
  series-production conformity + Art. 21-22 substantial-modification
  consequences — the DORA sole-authority reading does not apply
  because DORA is not in scope. **For a 5-FTE DORA financial entity
  that does not customise CRA-conformant products**, the
  change-management obligation is the DORA Art. 9(4)(e) six-step
  process — the CRA-side substantial-modification trigger is not in
  scope because the entity does not procure CRA-classified products.
- **Scope caveat (CRITICAL — Conditional-Y scope-overlap on the
  substantial-modification trigger event)** — derived from CRDA-deep
  verified classifications: the Y scope overlap on the
  substantial-modification trigger event (Art. 22 third-party
  substantial modification = manufacturer) is the gating condition for
  the high-level SO to engage. When the DORA financial entity
  customises a CRA-conformant product, the same change event triggers
  both regimes on a single party at a single event: (a) the DORA-side
  six-step process (Art. 9(4)(e) — recorded/tested/assessed/approved/
  implemented/verified in a controlled manner) for the entity's
  ICT-infrastructure change-management; (b) the CRA-side substantial-
  modification trigger (Art. 22 + Art. 13(14) series-of-production
  conformity + Art. 13(10) substantial-modification compliance scope
  + Art. 13(21) immediate corrective measures) for the product-side
  manufacturer-equivalent obligation. The two regimes stack with
  layered documentation (DORA six-step record + CRA Annex VII §2
  technical-documentation update + substantial-modification
  assessment per Art. 13(10) + Art. 14 AEV/SI notification if
  material). The DORA six-step documentation can serve as the
  evidence trail for CRA Art. 13(14) series-production conformity on
  the same change event (per CRDA-deep §D-07.4 line 68). For a
  typical integrated stack (CRA manufacturer + DORA financial entity
  on the simple supplier-customer boundary — no substantial
  modification), the two regimes operate **independently on the two
  sides** with the high-level SO **NOT** activating; the DORA six-step
  documentation can still serve as evidence trail for CRA series-
  production conformity when substantively the same change event is
  recorded on both sides.
- **Scope caveat (CRITICAL — DORA Art. 9(4)(e) six-step is the unique
  OJ-mandated dedicated authority for entity-level change-management
  controls)** — derived from CRDA-deep verified classifications: DORA
  Art. 9(4)(e) text is `documented policies, procedures and controls
  for ICT change management, including changes to software, hardware,
  firmware components, systems or security parameters … based on a
  risk assessment approach … in order to ensure that all changes to
  ICT systems are recorded, tested, assessed, approved, implemented
  and verified in a controlled manner` — the 5-way OR change-targets
  (software + hardware + firmware + systems + security parameters,
  R1 all five in scope per S3 COORD), the 6-way AND change-management
  steps (recorded + tested + assessed + approved + implemented +
  verified, R1 cumulative all six required per S3 COORD; partial-
  process compliance is non-compliance), and the `controlled manner`
  qualifier (R1 documented procedure + segregated approval R3 both per
  S2 VAG — preserved verbatim in `SR-DORA-023` `ambiguity_notes`). The
  DORA-side participation at D-07.4 is the **unique OJ-mandated
  dedicated authority for entity-level change-management controls**
  — the 5-way OR + 6-way AND mandate is OJ-verbatim with no
  equivalent OJ mandate in CRA (which addresses the product-side
  change management via Art. 13(14) + Art. 21-22 substantial-
  modification rather than via an OJ-verbatim six-step entity-level
  process). **For a 5-FTE DORA financial entity, the
  change-management obligation is the Art. 9(4)(e) six-step process**
  with EBA Guidelines supervisory baseline.
- **Scope caveat (CRITICAL — CRA Art. 13(14) OJ verbatim partial —
  the `keep the regulator informed of relevant changes in harmonised
  standards and common specifications` expansion)** — derived from
  CRDA-deep verified classifications + `CRDA/04_deduction_audit.md`
  line 98: Art. 13(14) OJ text reads `Manufacturers of products with
  digital elements that are part of a series of production shall
  ensure that … such products remain in conformity with this
  Regulation. The manufacturer shall also ensure that procedures are
  in place for series of production to remain in conformity,
  including, where applicable, procedures for …` with an ellipsis.
  `SR-CRA-069` + `SR-CRA-081` paraphrase the OJ-implicit claim "to
  keep the regulator informed of relevant changes in harmonised
  standards and common specifications" — this expansion **cannot be
  verified from the partial AMBIGUITY text**. No literal misquote
  identified, but the OJ verbatim for the `keep the regulator
  informed` portion is missing from the AMBIGUITY source. The
  SR-CRA-081 reading pairs Art. 13(7) `systematic documentation of
  cybersecurity aspects` with Art. 13(14) `series-of-production
  changes in harmonised standards` to construct an "always-current"
  record duty — this reading is **documented but OJ-verbatim-
  unverified** for the harmonised-standards-monitoring leg. Layer 2
  review item: confirm the OJ-verbatim text for the
  harmonised-standards-monitoring leg or revise the SR reading to
  preserve only the OJ-verbatim series-production conformity leg.
- **Scope caveat (CRITICAL — D-07.2 (Secure Coding Practices)
  cross-references via SR-DORA-023 D-07.2 partial)** — derived from
  CRDA-deep verified classifications + `CRDA/D-07_Secure-Development/
  D-07.2.md` line 54: `SR-DORA-023` (Art. 9(4)(e) D-07.4 primary)
  **partially** maps to D-07.2 (Secure Coding Practices) by inference
  only — the change-management six-step's `tested` + `assessed` legs +
  Art. 25 testing modalities (source-code reviews where feasible as
  one of 12 modalities) imply a secure-coding dimension, but no
  OJ-mandated coding-standards prescription. This is the **P0
  disagreement on AEGIS-taxonomy §4.1 sole-authority assignment for
  D-07.2** (AEGIS marks DORA as SOLE AUTHORITY; CRDA-deep finds no
  OJ-text support). For a 5-FTE DORA financial entity, the
  change-management obligation at D-07.4 is documented via the
  Art. 9(4)(e) six-step + the cross-reference to D-07.2 partial +
  Art. 25 testing modalities. Layer 2 review item (preserved at
  D-07.2): either (a) revise the AEGIS taxonomy to remove the DORA
  sole-authority assignment for D-07.2, or (b) identify the OJ clause
  that supports it.
---

## Emergent tensions (from CRDA-deep §D-07.4)

#### Emergent tensions (from CRDA-deep §D-07.4)
**0 conditional emergent tensions** on the change-management duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 1 verified pair (CRA↔DORA) is SAME — COMPLEMENTARY with Conditional Y scope overlap on the substantial-modification trigger event, and the two regulators look at change management from two distinct regulatory perspectives that **stack on the Conditional-Y integrated event**. **Y scope overlap** is returned on the substantial-modification trigger event (when a DORA financial entity customises a CRA-conformant product) — the same change event triggers both regimes on a single party at a single event. **N (typically)** is returned on the simple supplier-customer boundary — distinct parties, distinct objects. **No CONTRADICTORY pairs** on the change-management duty itself. The **target-object divergence** (product-level series-production conformity + substantial-modification consequences [CRA Art. 13(14) + 21-22 + 13(10) + 13(21)] / entity-level change-management six-step [DORA Art. 9(4)(e) 5-way OR + 6-way AND + `controlled manner`]) is the **legitimately diverse dimension**: each regulator targets a distinct target object at a distinct trigger (manufacturer series-production event + substantial-modification event / financial-entity ICT change event), and the operational convergence is on a **2-layer change-management architecture** — (a) the CRA-side product-level change management at the manufacturer side; (b) the DORA-side entity-level change-management six-step at the customer (financial-entity) side — with the Conditional-Y substantial-modification trigger event as the integration point (when a DORA financial entity customises a CRA-conformant product, the two regimes stack with layered documentation).
The **AEGIS taxonomy §4.1 sole-authority disagreement** is the structurally significant divergence: AEGIS taxonomy §4.1 marks DORA as the SOLE AUTHORITY for D-07.4 Change Management. The CRDA-deep OJ-text verification finds that CRA Art. 13(14) + Art. 21-22 + Art. 13(10) + Art. 13(21) constitute dedicated authorities for the substantial-modification trigger with manufacturer-equivalent consequences — the CRA participation at D-07.4 is preserved here as **co-equal participation** rather than as partial-coverage cross-ref (per CRA `03_validation_report.md` line 177: "AEGIS taxonomy marks DORA as SOLE AUTHORITY but CRA covers substantial modification"). This is a **structural Layer 2 review item** (not a CONTRADICTORY or CORRECTED reclassification) — the AEGIS-taxonomy sole-authority disagreement is documented as a Taxonomy-vs-OJ gap.
The **CRA Art. 13(14) OJ verbatim partial** is the structurally significant caveat on the CRA side: Art. 13(14) OJ text reads `Manufacturers of products with digital elements that are part of a series of production shall ensure that … such products remain in conformity with this Regulation. The manufacturer shall also ensure that procedures are in place for series of production to remain in conformity, including, where applicable, procedures for …` with an ellipsis. `SR-CRA-069` + `SR-CRA-081` paraphrase the OJ-implicit claim "to keep the regulator informed of relevant changes in harmonised standards and common specifications" — this expansion **cannot be verified from the partial AMBIGUITY text** per `CRDA/04_deduction_audit.md` line 98. No literal misquote identified, but the OJ verbatim for the `keep the regulator informed` portion is missing from the AMBIGUITY source. The SR-CRA-081 reading pairs Art. 13(7) `systematic documentation of cybersecurity aspects` with Art. 13(14) `series-of-production changes in harmonised standards` to construct an `always-current` record duty — this reading is documented but OJ-verbatim-unverified for the harmonised-standards-monitoring leg.
The high-level SO surfaces the common change-management duty (documented change-management procedures + risk-assessment-approach + controlled-manner + 5-way OR change-targets / 6-way AND change-management steps + substantial-modification assessment + manufacturer-equivalent status consequences where applicable); the per-reg target object, trigger, anchor, threshold, recipient, and evidence template are documented separately in the two sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 2-layer change-management architecture (CRA product-level series-production conformity + substantial-modification consequences [Art. 13(14) + 21-22 + 13(10) + 13(21)] → DORA entity-level change-management six-step [Art. 9(4)(e) 5-way OR + 6-way AND + `controlled manner`]) is itself the layered reconciliation that supersedes any single-regulator reading on the Conditional-Y substantial-modification trigger event; on the simple supplier-customer boundary, the two regimes operate independently with the DORA six-step documentation serving as evidence trail for CRA Art. 13(14) series-production conformity when substantively the same change event is recorded on both sides.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-07.4 — with overlapping target-object scope-determiners on the Conditional-Y substantial-modification trigger event — operates a **2-layer change-management architecture** with explicit layered hand-offs. The high-level SO (`SO-D-07.4.HL`) describes the common change-management duty (documented change-management procedures + risk-assessment-approach + controlled-manner + 5-way OR change-targets / 6-way AND change-management steps + substantial-modification assessment + manufacturer-equivalent status consequences where applicable); the per-reg perspective is preserved in the two sub-SOs (target object, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 2-layer change-management architecture (CRA product-level series-production conformity + substantial-modification consequences [Art. 13(14) + 21-22 + 13(10) + 13(21)] → DORA entity-level change-management six-step [Art. 9(4)(e) 5-way OR + 6-way AND + `controlled manner`]) operationalising the inter-reg hand-off on the Conditional-Y substantial-modification trigger event (when a DORA financial entity customises a CRA-conformant product, Art. 22 third-party substantial-modification = manufacturer). The high-level SO does NOT collapse the two target objects into a single change-management architecture; the per-reg perspective on target object, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **change-management strategy**: (1) a 2-layer change-management architecture with explicit target-object hand-offs (CRA Art. 13(14) series-production conformity + Art. 21-22 substantial-modification consequences → DORA Art. 9(4)(e) 6-step change-management process); (2) the **AEGIS taxonomy §4.1 sole-authority disagreement as a structural Layer 2 review item** (AEGIS marks DORA as SOLE AUTHORITY; CRDA-deep finds CRA Art. 13(14) + Art. 21-22 + Art. 13(10) + Art. 13(21) constitute dedicated authorities — preserved as co-equal participation; Layer 2 review item: either revise the AEGIS taxonomy to remove the DORA sole-authority assignment and add CRA as co-equal authority, or identify the OJ clause that supports the DORA sole-authority reading); (3) the **Conditional-Y substantial-modification trigger event** as the integration point — when a DORA financial entity customises a CRA-conformant product, Art. 22 third-party substantial-modification = manufacturer applies on top of the DORA-side six-step process with layered documentation (DORA six-step record + CRA Annex VII §2 technical-documentation update + substantial-modification assessment per Art. 13(10) + Art. 14 AEV/SI notification if material); (4) the **DORA six-step documentation as evidence trail** for CRA Art. 13(14) series-production conformity on the same change event when substantively the same change event is recorded on both sides (per CRDA-deep §D-07.4 line 68); (5) the **CRA Art. 13(14) OJ-verbatim-partial caveat** for the harmonised-standards-monitoring leg (per `CRDA/04_deduction_audit.md` line 98) — Layer 2 review item: confirm the OJ-verbatim text for the harmonised-standards-monitoring leg or revise the SR reading to preserve only the OJ-verbatim series-production conformity leg.
**End of file.**

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-07.4 Change Management — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md`. This is a thin Volere overlay: it adds requirement IDs, Volere classification, fit criteria, priority, verification method, dependencies, applicability, and satisfaction placeholders only; HSO Objective text, OJ text, NIST CSF rationale, scope-overlap analysis, and per-regulation considerations remain in the referenced source files.

## Participating regulations (§3)

### Participating regulations
CRA and DORA (2 of 5 regs). See the HSO provenance file for out-of-scope findings, Conditional-Y activation, and the taxonomy sole-authority caveat.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 7.4
  volere_section: 15
  volere_subtype: audit
  title: "Layered product-side and entity-side change records for Conditional-Y CRA/DORA substantial-modification events"
  derives_from:
    hso_sub_so: SO-D-07.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md
    objective_ref_section: "### D-07.4.0"
  description: |
    The product shall maintain layered product-side and entity-side change records when a CRA/DORA Conditional-Y substantial-modification event causes both change-management perspectives to apply to the same change.
  fit_criterion: |
    For 100% of Conditional-Y change events, one linked evidence pack contains the product change assessment, entity change ticket, risk assessment, approval, pre-implementation test evidence, implementation record, post-implementation verification, technical-documentation update reference, and authority-ready audit export.
  priority: MUST
  verification_method: INSPECT
  dependencies: []
  nist_csf: [GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04, PR.PS-01, PR.PS-06]
  applicable_if:
    regs: [CRA, DORA]
    scope_overlap: conditional
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.4.md` for Conditional-Y activation, target-object preservation, and Layer 2 taxonomy caveats.
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-07.4
title: D-07.4 Change Management — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.4 Change Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-07_Secure-Development/D-07.4.md
status: DRAFT
---
> **Deep analysis:** [D-07.4 Change Management](../../DeepAnalysis/D-07_Secure-Development/D-07.4.md)
#### D-07.4 Change Management
<!-- participants: CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR imposes process outcomes (Art. 24 review-and-update) but does not specify change-management controls. | — |
| NIS2 | (out-of-scope) | NIS 2 does not impose change-management controls. CRA Art. 13(14) and Art. 21-22 are dedicated authorities. | — |
| CRA | SO-CRA-047 | Procedures for series-of-production conformity + substantial-modification consequences (Art. 13(14), Art. 21-22, Art. 3(30)). | Product-level change management across series production; substantial modification triggers manufacturer-equivalent obligations. |
| DORA | SO-DORA-013 | Documented ICT change-management policies, procedures and controls covering software/hardware/firmware/components/systems/security parameters; six-step process (recorded, tested, assessed, approved, implemented, verified) under risk-based approach. | Entity-level change management; explicit OJ-mandate under Art. 9(4)(e). |
| AI_Act | (out-of-scope) | AI Act does not impose a change-management mandate. | — |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (2 regulations)
- Only 2 regulations have non-zero coverage. No 3-regulation emergent tension exists. Note: the substantial-modification regime under CRA Art. 21-22 + DORA Art. 9(4)(e) creates a layered obligation where the same change event must be assessed against both regimes — the substantive assessment objects differ (product-conformity vs. entity-process discipline) but the documentation overlap is high.
##### SR cross-validation
The two applicable regulations map D-07.4 to the NIST CSF 2.0 Subcategories **PR.PS-02** (Software maintained/replaced/removed commensurate with risk) and **PR.PS-01** (Configuration management practices established, documented, applied). CRA additionally anchors on **GV.SC-07** (Suppliers prioritised by criticality) via the substantial-modification trigger; DORA additionally anchors on **GV.RR-02** (Roles/responsibilities/accountabilities established) for the six-step approval-act dimension.
##### Downstream implication
Phase 1 entities must implement both regimes' change-management obligations: CRA's substantial-modification assessment for product changes; DORA's six-step process for entity-side changes. The regimes stack without overlap, but the same change event may trigger both. The DORA six-step documentation can serve as the evidence trail for CRA Art. 13(14) series-production conformity.
---
### D-08 Human Factors
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-07.4
title: D-07.4 Change Management — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.4 Change Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-07_Secure-Development/D-07.4.md
status: DRAFT
---
> **Domain analysis:** [D-07.4 Change Management](../../DomainAnalysis/D-07_Secure-Development/D-07.4.md)
#### D-07.4 Change Management
<!-- participants: CRA, DORA -->
**Participants (from CRDA):** CRA, DORA
**Sole-authority note:** NIS 2 has no OJ mandate for change-management controls (CRDA confirmed); GDPR imposes process outcomes (Art. 24 review-and-update) but does not specify change-management controls. CRA Art. 13(14) and DORA Art. 9(4)(e) are dedicated authorities.

## Part 3 — context

### D-08 Human Factors
---

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)