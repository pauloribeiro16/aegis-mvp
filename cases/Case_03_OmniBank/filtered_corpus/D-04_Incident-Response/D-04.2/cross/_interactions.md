<!-- aegis:case-scope: GDPR, CRA, NIS2, DORA, AI_Act — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-04.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-04.2 Containment & Mitigation](../../DomainAnalysis/D-04_Incident-Response/D-04.2.md)
#### D-04.2 Containment & Mitigation
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-04.2; containment is operationalised via CRA's Annex I (2)(h)/(i)/(k) at the product level and via NIS2/DORA's response-plan architecture at the entity level.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-04.2 Containment & Mitigation
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md`](../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.2.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope** per AEGIS taxonomy §4.1;
> AI Act does not impose a containment-and-mitigation mandate; containment
> is operationalised via CRA's Annex I (2)(h)/(i)/(k) at the product level
> and via NIS 2 / DORA's response-plan architecture at the entity level).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-04.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-009 | Personal-data breaches contained and mitigated via Art. 33(3)(d) measures (incl. rendering data unintelligible) + Art. 34(3)(a)/(b) unintelligibility carve-out | Personal data; post-detection containment, mitigation and remediation runbooks; ID.AM-08 + PR.IR-04 |
| NIS 2 | SG-NIS2-005 | Six-action incident-handling capability (prevent, detect, analyse, contain, respond, recover) per Art. 21(2)(b) + Art. 6(8) `contain` action | Entity-level ICT systems; lifecycle-phase content; RC.RP-01 + RC.RP-04 + PR.IR-03 |
| CRA | SG-CRA-021 + SG-CRA-022 | Product availability preserved post-incident via resilience and DoS-resistance + cascading-impact minimisation + exploitation mitigation | Product with digital elements; manufacturer design; Annex I Part I (2)(h)/(i)/(k); PR.IR-04 + PR.IR-03 + DE.CM-09 |
| DORA | SG-DORA-010 | Comprehensive ICT business continuity policy operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms (incl. response and recovery plans subject to independent internal audit for non-microenterprises; backup policies; restoration and recovery procedures) | Financial entity; BC arrangements under Art. 11 + Art. 12; RC.RP-01 + RC.RP-04 + PR.IR-04 |

## Validated relationships (from CRDA-deep §D-04.2)

#### Validated relationships (from CRDA-deep §D-04.2)
All 6 pairs verified by CRDA-deep as **non-SAME (no correction needed)** —
the underlying **containment-and-mitigation duty** is consistent across
the four regulators, but each operates on a **distinct containment
layer**:
- **GDPR** — personal-data post-breach runbook (controller-side): the
  controller takes measures to address the personal-data breach
  (Art. 33(3)(d) — measures taken or proposed, including mitigation
  measures), and the unintelligibility carve-out (Art. 34(3)(a)/(b))
  allows rendering data unintelligible as a substitute for Art. 34
  data-subject notification.
- **NIS 2** — entity-level incident-handling `contain` phase: the
  entity operates the Art. 6(8) six-action incident-handling lifecycle
  with `contain` as one of the six actions (Art. 21(2)(b)); the
  entity-wide response plan provides the procedural framework.
- **CRA** — product-level post-incident availability and
  cascading-impact minimisation: the product is designed to protect
  the availability of essential and basic functions also after an
  incident (Annex I Part I (2)(h) — DoS resilience), to minimise the
  negative impact on other devices/networks (Annex I Part I (2)(i)),
  and to reduce the impact of an incident using exploitation-mitigation
  mechanisms (Annex I Part I (2)(k)).
- **DORA** — financial-entity BC arrangements: the financial entity
  operates a comprehensive ICT business continuity policy
  (Art. 11(1)) operationalised through dedicated, appropriate and
  documented arrangements including response and recovery plans
  (Art. 11(2)/(3) — subject to independent internal audit for
  non-microenterprises), backup policies (Art. 12(1)), and restoration
  / recovery procedures.
The containment layers and **containment objects** are **different**
but the **containment-and-mitigation duty** is the **same substantive
obligation** — verified by CRDA-deep as non-SAME (5 COMPLEMENTARY + 1
DIFFERENT-PERSPECTIVE), no pair required CRDA correction. There is no
contradiction because no clause forbids what another mandates; a single
organisation across all four regulators must operate a **multi-layer
containment architecture**, with the layers explicitly documented. The
containment layer is preserved verbatim in the per-reg sub-SOs rather
than collapsed into a single containment duty.
The scope-overlap column in the matrix below indicates whether the same
event can trigger both regulations on a single party; this is the gating
condition for the high-level SO to engage.
|   |  GDPR  |  NIS 2  |  CRA  |  DORA  |
| --- | --- | --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (controller is also NIS 2 NSIE; GDPR runbook inside NIS 2 plan)  |  Conditional (Y integrated manufacturer-controller; disjoint in baseline: post-breach runbook ↔ product-design)  |  Conditional (DORA FE is also controller; disjoint baseline: runbook ↔ BC arrangements)  |
|  **NIS 2**  |  Conditional  |  —  |  Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint in baseline: entity-level phase ↔ product-level design)  |  Conditional (Y cross-sector; N pure-financial via lex specialis — DORA BC exceeds NIS 2 `contain`)  |
|  **CRA**  |  Conditional (Y integrated; disjoint baseline)  |  Conditional (Y deployer; disjoint baseline)  |  —  |  Conditional (Y DORA FE deploys CRA product; disjoint baseline: product ↔ entity)  |
|  **DORA**  |  Conditional (Y DORA-controller; disjoint baseline)  |  Conditional (Y cross-sector; N pure-financial lex specialis)  |  Conditional (Y deployer-side; disjoint baseline)  |  —  |
Legend: **Conditional** = scope overlap only under specific circumstances
(integrated-stack manufacturer-controller, NIS 2 entity deploying CRA
products, etc.); **N** = typically disjoint (high-level SO does NOT
engage by the mere co-applicability of both regulations); CRDA-deep
scope-disjoint tests: all 6 pairs marked Conditional (Y on
vertical-integration / integrated-stack; N in baseline).

## Cross-recipient map

#### Cross-recipient map
D-04.2 itself does **not** generate recipient asymmetry — the
containment-and-mitigation process is **inward-looking** (the entity
takes measures to contain and mitigate the incident's impact on its
own systems, products, services and data). The recipient fragmentation
across the four regulators is at the **downstream notification point**
(D-04.3) and the **compliance-demonstration point**: GDPR's supervisory
authority (Art. 33(3)(d) measures description), NIS 2's CSIRT or
competent authority (Art. 23(4)(b)/(c) incident notification + 1m
final report with mitigation measures), CRA's CSIRT + ENISA (Art. 14(1)
AEV/SI notification + Art. 14(2)(c) final report with corrective
measures), and DORA's competent authority + clients (Art. 19(1)+(3)
notification + Art. 11 BC arrangements audit). These are distinct
regulatory channels but they do not generate the containment cascade
of D-04.2 — they are compliance-evidence channels on the same
containment architecture. **D-04.3 is where the recipient asymmetry
manifests; D-04.2 is the containment-and-mitigation layer that feeds
it (via the measures description in the notification content).**
---

## HSO considerations (from D-04.2.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations (GDPR, NIS 2, CRA, DORA) impose a containment-and-mitigation duty but each targets a distinct containment layer and anchors to a distinct threshold: GDPR's post-breach TOMs (technical and organisational measures) including unintelligibility rendering (Art. 33(3)(d) + Art. 34(3)(a)/(b) unintelligibility carve-out; the unintelligibility rendering is GDPR-unique and acts as a substitute for Art. 34 data-subject notification when applied); NIS 2's entity-side incident-handling `contain` phase within the 6-action lifecycle (Art. 21(2)(b) + Art. 6(8) six-action definition with `contain` as one of the six actions); CRA's product-side availability preservation + cascading-impact minimisation + exploitation mitigation (Annex I Part I (2)(h) DoS resilience + (2)(i) cross-product impact minimisation + (2)(k) exploitation mitigation; the three-clause constellation is CRA-unique and operates at the product-design level); DORA's financial-entity-side BC arrangements with response and recovery plans + backup policies + restoration procedures (Art. 11(1)/(2)/(3) + Art. 12(1); the BC-arrangements architecture is DORA-unique and the strictest containment-architecture floor in the AEGIS corpus).
- The high-level SO surfaces the common containment-and-mitigation duty (contain the incident's impact, mitigate further damage, take measures to address the breach / incident, route to the downstream recovery / notification pipeline); the per-regulation perspective (containment layer, measure type, threshold qualifier, evidence template) is preserved in the four sub-SOs.
- A single organisation across all four regulators must operate a multi-layer containment architecture with explicit layer hand-offs: personal-data runbook feeds entity-level response plan at the controller/NSIE boundary; entity-level response plan feeds product resilience architecture via deployment (CRA products instrument their resilience & exploitation mitigation to support the deployer's containment); product resilience feeds back into DORA BC arrangements via integration. For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- The high-level SO does NOT collapse the four containment layers into a single measure type — the layers contain different objects (personal-data breach impact vs all-hazards entity event impact vs product availability vs ICT infrastructure) and produce different measure types (TOMs incl. unintelligibility render vs lifecycle-phase actions vs product-design choices vs BC arrangements).
- The high-level SO is honesty-preserving about scope-disjoint cases: for a 5-FTE SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA applicability, only the GDPR and CRA sub-SOs activate; the high-level SO engages on the same party if both apply, with the boundary between personal-data runbook (GDPR) and product-resilience architecture (CRA) documented as the controlled hand-off.
- DORA's BC arrangements with response-and-recovery plans (Art. 11(2)/(3)) are the strictest containment-architecture floor — they require dedicated, appropriate and documented arrangements, plans, procedures and mechanisms (the 4-way AND), plus independent internal audit for non-microenterprises (Art. 11(3) — the audit requirement is DORA-unique) — and exceed the NIS 2 `contain` requirement for financial-sector entities also within retained NIS 2 scope.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-04.2 over a distinct
**containment layer**; the measure type, the threshold qualifier, the
evidence template, the recipient (downstream), and the legal anchor all
depend on which layer the containment action falls into.
| Axis (reg) | Containment layer | Measure type | Threshold anchor | Recipient (downstream) | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | personal-data post-breach runbook (controller-side) | TOMs incl. unintelligibility rendering + subsequent measures eliminating high risk | `where appropriate` (Art. 33(3)(d)) + unintelligibility carve-out (Art. 34(3)(a)/(b)) | supervisory authority (Art. 33(3)(d) measures description); data subjects (Art. 34 unless carve-out applies) | Art. 33(3)(d) + Art. 34(3)(a)/(b) |
| **NIS 2** | entity-level incident-handling `contain` phase | lifecycle-phase actions (the `contain` action within the 6-action Art. 6(8) incident-handling lifecycle) | `appropriate and proportionate` (Art. 21(1)) | CSIRT or competent authority (Art. 23(4)(b) notification; 1m final report) | Art. 21(2)(b) + Art. 6(8) (six-action `contain` phase) |
| **CRA** | product-level post-incident availability + cross-product impact + exploitation mitigation | product-design choices (Annex I Part I (2)(h) DoS resilience; (2)(i) cross-product impact; (2)(k) exploitation mitigation) | continuous product design + post-incident availability preservation | CSIRT + ENISA (Art. 14 AEV/SI notification); product users (Art. 14(8) mitigation measures) | Annex I Part I (2)(h) + (2)(i) + (2)(k); Art. 13(21) corrective measures |
| **DORA** | financial-entity BC arrangements | BC policy + dedicated arrangements (response + recovery plans + backup policies + restoration procedures) — 4-way AND of artefacts | `dedicated, appropriate and documented` (Art. 11(2)); independent internal audit for non-microenterprises (Art. 11(3)) | competent authority + clients (Art. 19(1)+(3) notification); internal audit function (Art. 11(3)) | Art. 11(1)/(2)/(3) + Art. 12(1) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-04.2.HL`) engages on a given party **if and only if ≥2 applicable
regulations' containment-layer scope-determiners overlap on the same
party** (e.g. a controller that is also a NIS 2 essential entity
operating CRA-regulated products and running a DORA-class financial ICT
system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-layer containment architecture).
Pure co-applicability of disjoint-layer regulations on different
containment objects does **not** trigger cross-regulation aggregation —
see the Activation logic in the file header. For a 5-FTE SaaS startup
with GDPR + CRA applicability but no NIS 2 / DORA applicability, only
the GDPR and CRA sub-SOs activate; the high-level SO engages on the
same party if both apply, with the boundary between personal-data
runbook (GDPR) and product-resilience architecture (CRA) documented as
the controlled hand-off. **The four containment layers are layered, not
collapsed**: personal-data post-breach measures are documented in the
controller's runbook (GDPR); entity-level containment actions are
documented in the entity response plan (NIS 2); product-availability
measures are documented in the product design (CRA); BC arrangements
are documented in the financial-entity BC policy (DORA). The high-level
SO surfaces the common containment-and-mitigation duty but does **NOT**
aggregate the per-reg containment layers, measure types, or evidence
templates.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4.1 — AI Act does not impose a
  containment-and-mitigation mandate; containment is operationalised via
  CRA's Annex I (2)(h)/(i)/(k) at the product level and via NIS 2 /
  DORA's response-plan architecture at the entity level).
- 6 pairwise cells, verified by CRDA-deep as **non-SAME (no correction
  needed)**: GDPR↔NIS2 = COMPLEMENTARY (post-breach runbook ↔ entity
  phase; NIS 2 plan is the procedural wrapper, GDPR measures inside),
  GDPR↔CRA = DIFFERENT-PERSPECTIVE (post-breach runbook ↔ product
  design; layered pre-event vs post-event), GDPR↔DORA = COMPLEMENTARY
  (post-breach runbook ↔ BC arrangements; DORA plan is the wrapper,
  GDPR measures inside), NIS2↔CRA = COMPLEMENTARY (entity phase ↔
  product design; layered, not overlapping), NIS2↔DORA = COMPLEMENTARY
  (entity phase ↔ BC arrangements; DORA BC exceeds NIS 2 `contain` for
  the financial-services subset), CRA↔DORA = COMPLEMENTARY (product
  design ↔ BC arrangements; layered, not overlapping).
- The four regulations impose the **same substantive
  containment-and-mitigation duty** but each targets a **distinct
  containment layer** at a **distinct boundary**: personal-data
  post-breach (GDPR), entity-level incident-handling phase (NIS 2),
  product-level post-incident availability (CRA), financial-entity BC
  arrangements (DORA). The measure types differ (TOMs incl.
  unintelligibility render vs lifecycle-phase actions vs product-design
  choices vs BC arrangements). The threshold qualifiers differ (GDPR
  `where appropriate` + unintelligibility carve-out vs NIS 2
  `appropriate and proportionate` vs CRA continuous product design vs
  DORA `dedicated, appropriate and documented` + independent internal
  audit for non-microenterprises).
- The high-level SO describes the **COMMON OBJECTIVE** (contain the
  incident's impact, mitigate further damage, take measures to address
  the breach / incident, route to the downstream recovery / notification
  pipeline); the **per-regulation perspective** (containment layer,
  measure type, threshold qualifier, evidence template, downstream
  recipient) is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 6 pairs as non-SAME but also non-contradictory
  (5 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE). Phase 1C Doc 07 does not
  need to resolve contradictions on D-04.2 because none exist on the
  containment-and-mitigation duty itself; the task is to **stack the
  documentation** so that a single multi-layer containment architecture
  discharges all four obligations on the same party, with explicit
  layer hand-offs at the containment-type surfaces.
- **Scope caveat (CRITICAL — containment-layer divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the four containment layers into a single measure type.
  Personal-data post-breach TOMs, entity-level lifecycle-phase actions,
  product-design availability choices, and BC arrangements are
  **distinct measure types** at **distinct layers**, with distinct
  evidence templates (Art. 33(3)(d) measures description vs lifecycle-
  phase action records vs Annex VII design documentation vs Art. 11(2)
  arrangements registry). A unified containment runbook may serve the
  technical substrate (e.g. an incident-management playbook that
  references all four), but the policy and evidence layers must remain
  **layer-segregated** for compliance demonstration. Phase 1A must
  therefore emit **four checks before applying the high-level SO** (one
  per participating regulation) to confirm that the per-reg containment
  layer, measure type, threshold qualifier, and evidence template are
  documented separately; the high-level SO surfaces the common
  containment-and-mitigation duty but does NOT aggregate the per-reg
  containment layers.
- **Scope caveat (CRITICAL — DORA BC-arrangements strictness)** —
  derived from CRDA-deep verified classifications: DORA's Art. 11(2)
  `dedicated, appropriate and documented` arrangements +
  Art. 11(3) independent internal audit for non-microenterprises +
  Art. 12(1) backup policies + restoration procedures is the
  **strictest containment-architecture floor** in the AEGIS corpus.
  The independent internal audit requirement is DORA-unique — no other
  participating regulator imposes an audit obligation on the
  containment architecture. For a DORA + NIS 2 party, the DORA BC
  arrangements exceed the NIS 2 `contain` requirement for the
  financial-services subset of incidents; the high-level SO does not
  aggregate across the DORA-exceeds-NIS 2 boundary in that direction.
  For a DORA + GDPR party, the GDPR Art. 33(3)(d) personal-data
  measures must be documented as a section within the DORA BC
  arrangements (Doc 07 downstream implication), not as a separate
  runbook.
- **Scope caveat (CRITICAL — GDPR unintelligibility carve-out)** —
  derived from CRDA-deep verified classifications: the GDPR Art. 34(3)
  (a)/(b) unintelligibility rendering is **uniquely GDPR** and operates
  as a substitute for Art. 34 data-subject notification when applied.
  No other participating regulator has an equivalent unintelligibility
  carve-out. For a GDPR-only party or a GDPR + CRA party, the
  unintelligibility rendering is the GDPR-specific containment measure
  type; for a multi-reg party, the unintelligibility measure is
  documented in the GDPR runbook and the CRA Annex I (2)(h) resilience
  design operates as the product-side complement.
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA lex specialis on
  pure-financial entities)** — derived from CRDA-deep verified
  classifications: for pure-financial entities (NIS 2 §9 fall-back
  does not apply — DORA is lex specialis), DORA BC arrangements absorb
  the NIS 2 `contain` requirement for the financial-services subset;
  the high-level SO does not aggregate across the lex-specialis
  boundary in that direction. For cross-sector entities, the NIS 2
  entity-level phase layers on the DORA financial-entity BC
  arrangements, and the high-level SO engages on the same party with
  explicit boundary hand-offs (the NIS 2 chapeau coverage is the
  additional layer for non-financial incidents).
- **Scope caveat (CRITICAL — CRA product-design pre-event vs GDPR
  post-event)** — derived from CRDA-deep verified classifications: the
  CRA containment architecture (Annex I Part I (2)(h)/(i)/(k)) is
  **pre-event design + post-incident availability preservation**, while
  the GDPR containment is **post-event reaction**. A CRA-compliant
  product is designed to contain an incident internally and minimise
  cascading impact, reducing the probability that a GDPR-relevant breach
  occurs; if one does, the GDPR Art. 33(3)(d) runbook takes over. The
  two are **temporally distinct** (pre-event vs post-event) and
  **temporally complementary** (CRA design reduces the probability of
  GDPR containment needing to fire); the high-level SO does not
  collapse the temporal distinction.
---

## Emergent tensions (from CRDA-deep §D-04.2)

#### Emergent tensions (from CRDA-deep §D-04.2)
None — sub-domain is **non-SAME in baseline (6 pairs verified as
non-SAME: 5 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; no CRDA
corrections needed — CRDA initial classifications held after OJ-text
analysis)**. No conditional emergent tensions on the
containment-and-mitigation duty itself. The **containment-layer
divergence** (personal-data post-breach / entity-level lifecycle phase /
product-design availability / financial-entity BC arrangements) is the
**legitimately diverse dimension**: each regulator targets a distinct
layer, and the operational convergence is on a **multi-layer
containment architecture** with explicit layer hand-offs. The
**measure-type divergence** (TOMs incl. unintelligibility render vs
lifecycle-phase actions vs product-design choices vs BC arrangements)
reflects the layered containment architecture: DORA BC arrangements
are the **strictest containment-architecture floor** (4-way AND of
artefacts + independent internal audit for non-microenterprises) and
exceed the NIS 2 `contain` requirement for financial-sector entities
also within retained NIS 2 scope. The **temporal-divergence**
(GDPR post-event reaction / NIS 2 lifecycle-phase / CRA pre-event design
+ post-incident preservation / DORA BC arrangements) reflects the
three-layer containment construct (product design → entity plans →
breach-specific content) identified by CRDA's downstream implication:
"Phase 3 case generation must verify that case companies operating
across all three layers produce a single integrated containment
playbook." The **GDPR unintelligibility carve-out** (Art. 34(3)(a)/(b))
is **uniquely GDPR** and operates as a substitute for Art. 34
data-subject notification when applied — no other participating
regulator has an equivalent carve-out. The **scope-disjoint divergence**
(NIS 2 §9 fall-back / DORA lex specialis on pure-financial entities) is
**handled by the lex-specialis carve-out** — DORA absorbs the NIS 2
`contain` obligation for the financial-services subset and the
high-level SO does not aggregate across the lex-specialis boundary in
that direction. The high-level SO surfaces the common
containment-and-mitigation duty; the per-reg containment layer, measure
type, threshold qualifier, and evidence template are documented
separately in the four sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-04.2 — with
overlapping containment-layer scope-determiners on the same party —
operates a **multi-layer containment architecture** with explicit
layer hand-offs. The high-level SO (`SG-D-04.2.HL`) describes the common
containment-and-mitigation duty (contain the incident's impact,
mitigate further damage, take measures to address the breach /
incident, route to the downstream recovery / notification pipeline);
the per-reg perspective is preserved in the four sub-SOs
(containment layer, measure type, threshold qualifier, evidence
template, downstream recipient). **No conflict-resolution is required
on D-04.2 because CRDA-deep verified all 6 pairs as non-SAME and
non-contradictory.** Phase 1C Doc 07 documents the **layered
containment strategy**: (1) a multi-layer containment architecture with
explicit layer hand-offs at the containment-type surfaces (personal-
data runbook vs entity-level phase vs product-design vs BC arrangements);
(2) the DORA `dedicated, appropriate and documented` arrangements +
independent internal audit for non-microenterprises as the operative
ceiling when both DORA and NIS 2 apply on the same financial-services
incident (DORA BC arrangements exceed the NIS 2 `contain` requirement
for the financial-services subset); (3) the GDPR Art. 34(3)(a)/(b)
unintelligibility rendering as the GDPR-unique carve-out that operates
as a substitute for Art. 34 data-subject notification when applied;
(4) the CRA Annex I Part I (2)(h)/(i)/(k) product-design architecture
as the **pre-event design + post-incident preservation** layer that
reduces the probability of GDPR / NIS 2 / DORA containment needing to
fire; (5) the lex-specialis carve-out for pure-financial entities
(DORA absorbs NIS 2 `contain` for the financial-services subset; no
aggregation across the boundary). For proportionality (P2), a 5-FTE
SaaS with GDPR + CRA applicability may default to a personal-data
post-breach runbook (GDPR) + product-resilience evidence pack (CRA
Annex VII documentation) without the NIS 2 lifecycle-phase or DORA
BC-arrangements obligations (both out of scope); a 500-FTE DORA
financial entity must additionally implement the Art. 11(2) 4-way AND
of BC arrangements + Art. 11(3) independent internal audit for
non-microenterprises + Art. 12(1) backup policies + restoration
procedures per `SR-DORA-013` + `SR-DORA-014` + `SR-DORA-016`; a DORA +
NIS 2 cross-sector entity must document both the DORA BC arrangements
AND the NIS 2 entity-level response plan with explicit hand-offs
between them (the NIS 2 chapeau coverage is the additional layer for
non-financial incidents; physical + operational hazards beyond ICT
still bind via NIS 2).

## Part 1 §3 — context

### 3. Security Requirements
## 4.2 Containment & Mitigation — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md`. See that file for cross-reg verified relationships (6 pairs verified as non-SAME — no correction needed: 5 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE; the four regulators target **different containment layers** at distinct boundaries: personal-data post-breach runbook / entity-level lifecycle phase / product-level availability & resilience / financial-entity BC arrangements), scope overlap matrix, Objective/Considerations content, containment-layer divergence, DORA BC-arrangements strictness, GDPR unintelligibility carve-out, NIS 2 ↔ DORA lex specialis on pure-financial entities, CRA pre-event vs GDPR post-event temporal distinction, and aggregation logic. **Scope-title note (P0):** the corpus index title `Forensics & Analysis` is reconciled with the CRDA-deep `Containment & Mitigation` — this file covers containment/mitigation/recovery clauses only (Art. 33(3)(d) GDPR, Art. 21(2)(b) NIS 2 + Art. 6(8) `contain` action, Annex I Part I (2)(h)/(i)/(k) CRA, Art. 11 DORA), not forensics/evidence-analysis clauses. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; AI Act does not impose a containment-and-mitigation mandate; containment is operationalised via CRA's Annex I (2)(h)/(i)/(k) at the product level and via NIS 2 / DORA's response-plan architecture at the entity level). CRDA-deep verified 6 pairs as non-SAME (5 COMPLEMENTARY + 1 DIFFERENT-PERSPECTIVE — none required CRDA correction). The four regulators target **different containment layers** at **distinct boundaries** (personal-data post-breach runbook / entity-level lifecycle phase / product-level availability & resilience / financial-entity BC arrangements), and the high-level SO surfaces the common containment-and-mitigation duty while preserving the per-reg containment layer — the four containment layers are layered, not collapsed. DORA's `dedicated, appropriate and documented` arrangements + independent internal audit for non-microenterprises + backup policies + restoration procedures (Art. 11(2)/(3) + Art. 12(1)) is the strictest containment-architecture floor in the AEGIS corpus.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 4.2
  volere_section: 15
  volere_subtype: immunity
  title: "Incidents contained and mitigated through appropriate measures at the appropriate containment layer, with multi-layer containment architecture covering pre-event design, post-event reaction, and BC arrangements (multi-layer containment architecture)"
  derives_from:
    hso_sub_so: SO-4.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md
    objective_ref_section: "### 4.2.0"
  description: |
    The product shall contain and mitigate security incidents through appropriate measures that address the incident's impact and reduce the probability of further damage, at the appropriate containment layer — personal-data post-breach runbook (controller-side, TOMs incl. unintelligibility rendering), entity-level incident-handling `contain` phase (entity-wide response plan), product-level post-incident availability + cross-product impact minimisation + exploitation mitigation (product design), or financial-entity BC arrangements (BC policy + response/recovery plans + backup policies + restoration procedures) — and shall route the contained incident to the downstream recovery (4.4) and notification (4.3) pipelines, as the common containment-and-mitigation duty converging across GDPR Art. 33(3)(d) + Art. 34(3)(a)/(b) unintelligibility carve-out, NIS 2 Art. 21(2)(b) + Art. 6(8) six-action `contain`, CRA Annex I Part I (2)(h) DoS resilience + (2)(i) cross-product impact + (2)(k) exploitation mitigation + Art. 13(21) corrective measures, and DORA Art. 11(1) + Art. 11(2) `dedicated, appropriate and documented` + Art. 11(3) response/recovery plans + independent internal audit for non-microenterprises + Art. 12(1) backup policies + restoration procedures, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A multi-layer containment architecture is operated with one containment measure catalogue per layer (personal-data post-breach TOMs / entity-level lifecycle-phase actions / product-design availability choices / BC arrangements) and explicit layer hand-offs at the containment-type surfaces; each catalogue records measure type, threshold qualifier, evidence template, and downstream recipient per asset; the DORA `dedicated, appropriate and documented` + independent internal audit for non-microenterprises + backup policies + restoration procedures (Art. 11(2)/(3) + Art. 12(1)) is the operative ceiling when both DORA and NIS 2 apply on the same financial-services incident (DORA BC arrangements exceed the NIS 2 `contain` requirement for the financial-services subset); the GDPR Art. 34(3)(a)/(b) unintelligibility rendering is documented as the GDPR-unique carve-out that operates as a substitute for Art. 34 data-subject notification when applied; the CRA Annex I Part I (2)(h)/(i)/(k) product-design architecture is the pre-event design + post-incident preservation layer that reduces the probability of GDPR / NIS 2 / DORA containment needing to fire; for multi-reg parties, the GDPR Art. 33(3)(d) personal-data measures are documented as a section within the NIS 2 entity-level response plan or within the DORA BC arrangements (Doc 07 downstream implication), not as a separate runbook; the lex-specialis carve-out discharges the NIS 2 `contain` obligation for pure-financial entities (DORA absorbs NIS 2 `contain` for the financial-services subset); verified by containment-architecture documentation review + per-layer measure-catalogue audit + layer hand-off protocol documentation + Art. 33(3)(d) measures description review (when GDPR in scope) + Art. 21(2)(b) `contain` phase action records inspection (when NIS 2 in scope) + Annex I (2)(h)/(i)/(k) design-documentation review (when CRA in scope) + Art. 11(2)/(3) BC-arrangements registry + Art. 11(3) independent internal audit records (when DORA in scope and non-microenterprise) + DPA / CSIRT / MSA / CA + ESA + AI Office inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: [4.1 (containment depends on a prior detection-and-triage event feeding the containment trigger)]
  nist_csf: [RS.MI-01, RS.MI-02, PR.DS-01, ID.AM-08, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-04, DE.CM-09]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping containment layers on the same party (see HSO scope-overlap principle); AI Act out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive containment-and-mitigation duty but each targets a distinct containment layer at a distinct boundary and produces distinct measure types: GDPR personal-data post-breach TOMs incl. unintelligibility rendering (Art. 33(3)(d) + Art. 34(3)(a)/(b); the unintelligibility rendering is GDPR-unique and acts as a substitute for Art. 34 data-subject notification when applied); NIS 2 entity-level incident-handling `contain` phase within the 6-action lifecycle (Art. 21(2)(b) + Art. 6(8)); CRA product-side availability preservation + cascading-impact minimisation + exploitation mitigation (Annex I Part I (2)(h) DoS resilience + (2)(i) cross-product impact + (2)(k) exploitation mitigation; the three-clause constellation is CRA-unique and operates at the product-design level — pre-event design + post-incident preservation, temporally distinct from GDPR's post-event reaction); DORA financial-entity BC arrangements with response and recovery plans + backup policies + restoration procedures (Art. 11(1)/(2)/(3) + Art. 12(1); the BC-arrangements architecture is DORA-unique and the strictest containment-architecture floor — 4-way AND of artefacts + independent internal audit for non-microenterprises). A unified containment runbook may serve the technical substrate (e.g. an incident-management playbook that references all four), but the policy and evidence layers must remain layer-segregated for compliance demonstration. The temporal distinction is preserved (GDPR post-event reaction / NIS 2 lifecycle-phase / CRA pre-event design + post-incident preservation / DORA BC arrangements); the high-level SO does not collapse the temporal distinction. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so that a single multi-layer containment architecture (with the per-reg containment layer, measure type, threshold qualifier, and evidence template documented separately) discharges all four obligations on the same party, with explicit layer hand-offs at the containment-type surfaces. (Copied from the HSO Considerations block of `### 4.2.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-04.2
title: D-04.2 Containment & Mitigation — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.2 Containment & Mitigation
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-04_Incident-Response/D-04.2.md
status: DRAFT
---
> **Deep analysis:** [D-04.2 Containment & Mitigation](../../DeepAnalysis/D-04_Incident-Response/D-04.2.md)
#### D-04.2 Containment & Mitigation
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-009 | Personal-data breaches contained and mitigated via Art. 33(3)(d) measures (incl. rendering data unintelligible) | Personal data; post-detection containment |
| NIS2 | SG-NIS2-005 | Six-action incident-handling lifecycle covering `contain` and `respond` (Art. 6(8) definition) | Entity ICT; lifecycle phase |
| CRA | SG-CRA-021, SG-CRA-022 | Product availability preserved post-incident via resilience and DoS-resistance + cascading-impact minimisation | Product with digital elements; manufacturer design |
| DORA | SG-DORA-008, SG-DORA-010 | ICT incident management process (Art. 17(1) `detect/manage/notify`) + BC policy with response/recovery plans (Art. 11(3)) | Financial entity; response-plan architecture |
| AI_Act | — | Out-of-scope (sole authorities: NIS2/DORA/CRA) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-04.2 per AEGIS taxonomy §4.1 — AI Act does not impose a containment mandate. Containment is operationalised via CRA's Annex I (2)(h)/(i)/(k) resilience/availability architecture at the product level and via NIS2/DORA's response-plan architecture at the entity level.
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
None. The containment architecture is consistently layered: product → entity → personal-data-specific runbook. No 3-way contradiction; no non-pairwise-surfacing effect.
##### SR cross-validation
NIST CSF 2.0 anchoring is consistent: PR.IR-03 (Network resources prioritised based on importance), PR.IR-04 (Adequate resource capacity), and RC.RP-04 (Recovery plans executed). GDPR adds ID.AM-08 (Data disposal managed) only via the unintelligibility-rendering path. CRA's exploitation-mitigation obligation (SR-CRA-068 `Deploy-time exploitation-mitigation mechanisms and techniques`, Annex I Part I (2)(k)) maps to a CSF category not separately enumerated under DE.CM; this is a known CSF 2.0 gap and is appropriately flagged as a product-design construct rather than a CSF GOVERN/IDENTIFY category.
##### Downstream implication
Phase 2 obligation derivation must treat containment as a 3-layer construct: (1) product design (CRA), (2) entity-level plans (NIS2/DORA), (3) breach-specific content (GDPR Art. 33(3)(d) unintelligibility render). Phase 3 case generation must verify that case companies operating across all three layers produce a single integrated containment playbook.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-04.2
title: D-04.2 Containment & Mitigation — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.2 Containment & Mitigation
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-04_Incident-Response/D-04.2.md
status: DRAFT
---
> **Domain analysis:** [D-04.2 Containment & Mitigation](../../DomainAnalysis/D-04_Incident-Response/D-04.2.md)
#### D-04.2 Containment & Mitigation
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-04.2; containment is operationalised via CRA's Annex I (2)(h)/(i)/(k) at the product level and via NIS2/DORA's response-plan architecture at the entity level.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
