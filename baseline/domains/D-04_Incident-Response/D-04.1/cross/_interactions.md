# D-04.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-04.1 Incident Detection & Triage](../../DomainAnalysis/D-04_Incident-Response/D-04.1.md)
#### D-04.1 Incident Detection & Triage
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-04.1 per AEGIS taxonomy §4.1; AI Act detection obligations are coupled to the Art. 73/55 reporting triggers (D-04.3) and not standalone.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-04.1 Incident Detection & Triage
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md`](../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.1.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope** per AEGIS taxonomy §4.1;
> AI Act detection obligations are coupled to the Art. 73/55 reporting
> triggers (D-04.3) and not standalone).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-04.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-008 | Personal-data breach detection and triaging with documented "becoming aware" moment anchoring the 72h clock | Personal data; controller/processor; Art. 32(1)(b) + Art. 33(1) `becoming aware` + Art. 4(12) breach definition; PR.PS-04 + DE.AE-02 |
| NIS 2 | SO-NIS2-005 | Six-action incident-handling capability (prevent, detect, analyse, contain, respond, recover) per Art. 21(2)(b) + Art. 6(8) definition | Entity-level ICT systems; all-hazards approach (Art. 21(2) chapeau); PR.PS-04 + DE.CM-01 + DE.AE-02 |
| CRA | SO-CRA-020 + SO-CRA-068 | Recording and monitoring of product internal activity with user opt-out, corruption reporting | Product with digital elements; manufacturer perspective; Annex I Part I (2)(l); DE.CM-09 + PR.PS-04 |
| DORA | SO-DORA-007 + SO-DORA-008 | Multi-class anomalous-activity detection with SPOF identification (Art. 10) + ICT-related incident management process (Art. 17(1)) | Financial-entity ICT; performance + incidents + SPOFs; DE.CM-01 + DE.CM-09 + RS.MA-01 |

## Validated relationships (from CRDA-deep §D-04.1)

#### Validated relationships (from CRDA-deep §D-04.1)
All 6 pairs verified by CRDA-deep as **non-SAME (no correction needed)** —
the underlying **detection-and-triage duty** is consistent across the four
regulators, but each operates on a **distinct detection layer**:
- **GDPR** — data-flow boundary (controller-side, ingress/egress of personal
  data): the controller detects a personal-data breach (Art. 4(12)) and
  documents the moment of "becoming aware" (Art. 33(1)) to anchor the 72h
  notification clock.
- **NIS 2** — entity-level all-hazards: the entity detects adverse events
  affecting network and information systems across cybersecurity,
  operational and physical-environment hazards (Art. 21(2) chapeau + Recital
  56), with the incident-handling 6-action lifecycle (Art. 6(8)) covering
  detect as one of the six actions (Art. 21(2)(b)).
- **CRA** — product-internal state: the manufacturer detects intra-product
  state changes (access to or modification of data, services, or functions)
  per Annex I Part I (2)(l), with a user-visible opt-out mechanism where
  appropriate.
- **DORA** — financial-entity ICT infrastructure: the financial entity
  detects anomalous ICT activities, performance issues, and SPOFs per
  Art. 10(1), with multi-layer threshold-driven escalation per Art. 10(2).
The detection objects and **detection layers** are **different** but the
**detection-and-triage duty** is the **same substantive obligation** —
verified by CRDA-deep as non-SAME (3 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE),
no pair required CRDA correction. There is no contradiction because no
clause forbids what another mandates; a single organisation across all
four regulators must operate a **multi-layer detection architecture**,
with the layers explicitly documented. The detection layer is preserved
verbatim in the per-reg sub-SOs rather than collapsed into a single
detection duty.
The scope-overlap column in the matrix below indicates whether the same
event can trigger both regulations on a single party; this is the gating
condition for the high-level SO to engage.
| | GDPR | NIS 2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Conditional (controller is also NIS 2 NSIE; data-flow detection feeds entity detection) | Conditional (Y integrated manufacturer-controller; disjoint in baseline: data-flow ↔ product-internal state) | Conditional (DORA financial entity is also controller; disjoint in baseline: data-flow ↔ ICT-infrastructure) |
| **NIS 2** | Conditional | — | Conditional (Y NIS 2 entity deploys/manufactures CRA product; disjoint in baseline: entity ↔ product) | Conditional (Y cross-sector; N pure-financial via lex specialis) |
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
D-04.1 itself does **not** generate recipient asymmetry — the
detection-and-triage process is **inward-looking** (the entity detects an
event and feeds it into the response/notification pipeline). The
recipient fragmentation across the four regulators is at the
**downstream notification point** (D-04.3) and the
**compliance-demonstration point**: GDPR's supervisory authority
(Art. 33 notification), NIS 2's CSIRT or competent authority (Art. 23(4)
notification), CRA's CSIRT + ENISA (Art. 14(1)/(3) notification), and
DORA's competent authority + clients (Art. 19(1)+(3) notification).
These are distinct regulatory channels but they do not generate the
detection cascade of D-04.1 — they are compliance-evidence channels on
the same detection event. **D-04.3 is where the recipient asymmetry
manifests; D-04.1 is the detection-and-triage layer that feeds it.**
---

## HSO considerations (from D-04.1.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations (GDPR, NIS 2, CRA, DORA) impose a detection-and-triage duty but each targets a distinct detection layer and anchors to a distinct threshold: GDPR's data-flow-boundary awareness of personal-data breach (Art. 4(12) + Art. 33(1) `becoming aware` — the awareness anchor is GDPR-unique and drives the 72h clock); NIS 2's entity-side all-hazards monitoring with the 6-action incident-handling lifecycle covering `detect` (Art. 21(2) chapeau + Recital 56 + Art. 6(8) + Art. 21(2)(b)); CRA's product-side intra-product state-change visibility (Annex I Part I (2)(l); the recording-and-monitoring obligation is CRA-unique and provides the manufacturer's view inside the product boundary); DORA's financial-entity-side multi-class anomalous-activity detection with SPOF identification and threshold-driven escalation (Art. 10(1) + Art. 10(2); the multi-layer + auto-alert + SPOF pattern is DORA-unique).
- The high-level SO surfaces the common detection-and-triage duty (detect, document the trigger moment, triage, route to the downstream response/notification pipeline); the per-regulation perspective (detection layer, trigger anchor, threshold qualifier, evidence template) is preserved in the four sub-SOs.
- A single organisation across all four regulators must operate a multi-layer detection architecture with explicit layer hand-offs: data-flow detection feeds entity detection at the controller/NSIE boundary; entity detection feeds product detection via deployment (CRA products instrument their intra-product visibility to feed the deployer-side detection); product detection feeds back into DORA infrastructure detection via integration. For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- The high-level SO does NOT collapse the four detection layers into a single detection event — the layers detect different objects (personal-data breach vs all-hazards event vs intra-product state change vs anomalous ICT activity) and produce different trigger moments (GDPR `becoming aware`, NIS 2 detection-of-adverse-event, CRA product-internal-event-recording, DORA anomalous-activity-threshold).
- The high-level SO is honesty-preserving about scope-disjoint cases: for a 5-FTE SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA applicability, only the GDPR and CRA sub-SOs activate; the high-level SO engages on the same party if both apply, with the boundary between data-flow detection (GDPR) and product-internal detection (CRA) documented as the controlled hand-off.
- DORA's multi-layer + SPOF-identification detection (Art. 10(1)/(2)) is the strictest detection-architecture floor and supports the NIS 2 `where appropriate` test on detection depth for financial-sector entities also within retained NIS 2 scope.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-04.1 over a distinct
**detection layer**; the trigger, the threshold anchor, the documented
trigger moment, the recipient (downstream), and the legal anchor all
depend on which layer the detection event falls into.
| Axis (reg) | Detection layer | Trigger | Threshold anchor | Recipient (downstream) | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | data-flow boundary (controller-side, personal-data ingress/egress) | awareness of personal-data breach | `becoming aware` (Art. 33(1)) — document the trigger moment | supervisory authority (Art. 33 notification) | Art. 32(1)(b) + Art. 33(1) + Art. 4(12) |
| **NIS 2** | entity boundary (entity ICT systems, all-hazards) | detection of adverse event affecting service continuity | `appropriate and proportionate` (Art. 21(1)); all-hazards coverage (Art. 21(2) chapeau + Recital 56) | CSIRT or competent authority (Art. 23(4) notification) | Art. 21(2)(b) + Art. 6(8) (six-action `detect` phase) |
| **CRA** | product-internal state (intra-product state changes) | continuous recording and monitoring of relevant internal activity | continuous product monitoring with user opt-out where appropriate | CSIRT + ENISA (Art. 14(1)/(3) AEV/SI notification) | Annex I Part I (2)(l) |
| **DORA** | financial-entity ICT infrastructure | detection of anomalous ICT activity, performance issues, SPOFs meeting Art. 10 thresholds | multi-layer + alert thresholds + auto-alert to relevant staff + SPOF identification | competent authority + clients (Art. 19(1)+(3) notification) | Art. 10(1) + Art. 10(2); Art. 17(1) incident-management-process `detect/manage/notify` 3-way |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-04.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations' detection-layer scope-determiners overlap on the same
party** (e.g. a controller that is also a NIS 2 essential entity
operating CRA-regulated products and running a DORA-class financial ICT
system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-layer detection architecture).
Pure co-applicability of disjoint-layer regulations on different
detection objects does **not** trigger cross-regulation aggregation —
see the Activation logic in the file header. For a 5-FTE SaaS startup
with GDPR + CRA applicability but no NIS 2 / DORA applicability, only
the GDPR and CRA sub-SOs activate; the high-level SO engages on the
same party if both apply, with the boundary between data-flow detection
(GDPR) and product-internal detection (CRA) documented as the
controlled hand-off. **The four detection layers are layered, not
collapsed**: data-flow events are detected at the controller boundary
(GDPR); entity-level events are detected at the entity boundary
(NIS 2); product-internal events are detected inside the product (CRA);
anomalous-ICT events are detected at the financial-entity
infrastructure (DORA). The high-level SO surfaces the common
detection-and-triage duty but does **NOT** aggregate the per-reg
detection layers, trigger anchors, or evidence templates.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4.1 — AI Act detection obligations
  are coupled to the Art. 73/55 reporting triggers (D-04.3) and not
  standalone).
- 6 pairwise cells, verified by CRDA-deep as **non-SAME (no correction
  needed)**: GDPR↔NIS2 = COMPLEMENTARY (data-flow ↔ entity; data-flow
  detection feeds entity detection), GDPR↔CRA = DIFFERENT-PERSPECTIVE
  (data-flow ↔ product-internal state; layered, not overlapping),
  GDPR↔DORA = COMPLEMENTARY (data-flow ↔ financial-entity ICT; DORA
  detection events feed GDPR `becoming aware`), NIS2↔CRA =
  COMPLEMENTARY (entity ↔ product; CRA product feeds NIS 2 entity
  detection via Annex I (2)(l)), NIS2↔DORA = DIFFERENT-PERSPECTIVE
  (all-hazards ↔ ICT-specific; DORA Art. 10 satisfies NIS 2 detection
  for the ICT-hazard subset, NIS 2 chapeau extends to physical +
  operational hazards), CRA↔DORA = DIFFERENT-PERSPECTIVE
  (product-internal ↔ financial-entity ICT infrastructure; both
  required, neither substitutes for the other).
- The four regulations impose the **same substantive detection-and-triage
  duty** but each targets a **distinct detection layer** at a
  **distinct boundary**: data-flow boundary (GDPR), entity boundary
  (NIS 2), product-internal state (CRA), financial-entity ICT
  infrastructure (DORA). The trigger anchors differ (GDPR `becoming
  aware`, NIS 2 detection-of-adverse-event, CRA
  product-internal-event-recording, DORA anomalous-activity-threshold).
  The threshold qualifiers differ (GDPR implicit, NIS 2 `appropriate and
  proportionate` + all-hazards chapeau, CRA continuous with opt-out,
  DORA multi-layer + auto-alert + SPOF identification).
- The high-level SO describes the **COMMON OBJECTIVE** (detect
  security-relevant events at the appropriate layer, document the
  trigger moment, triage, route to the downstream response / notification
  pipeline); the **per-regulation perspective** (detection layer,
  trigger anchor, threshold qualifier, evidence template, downstream
  recipient) is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 6 pairs as non-SAME but also non-contradictory
  (3 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE). Phase 1C Doc 07 does not
  need to resolve contradictions on D-04.1 because none exist on the
  detection-and-triage duty itself; the task is to **stack the
  documentation** so that a single multi-layer detection architecture
  discharges all four obligations on the same party, with explicit
  layer hand-offs at the detection-type surfaces.
- **Scope caveat (CRITICAL — detection-layer divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the four detection layers into a single detection event.
  Data-flow breaches, all-hazards entity events, product-internal state
  changes, and anomalous ICT activities are **distinct detection
  objects** at **distinct layers**, with distinct trigger moments
  (awareness vs detection vs continuous-recording vs threshold-cross)
  and distinct evidence templates (breach-record vs adverse-event-log
  vs Annex I (2)(l) recording vs Art. 10(1) SPOF register). A unified
  SIEM may serve the technical substrate (e.g. a SIEM with multiple
  detection pipelines), but the policy and evidence layers must remain
  **layer-segregated** for compliance demonstration. Phase 1A must
  therefore emit **four checks before applying the high-level SO** (one
  per participating regulation) to confirm that the per-reg detection
  layer, trigger anchor, threshold qualifier, and evidence template are
  documented separately; the high-level SO surfaces the common
  detection-and-triage duty but does NOT aggregate the per-reg
  detection layers.
- **Scope caveat (CRITICAL — DORA multi-layer strictness)** — derived
  from CRDA-deep verified classifications: DORA's Art. 10(2) multi-layer
  + alert-threshold + auto-alert + SPOF-identification detection
  architecture is **stricter than the GDPR `becoming aware` trigger
  alone** — the financial entity must demonstrate layered detection
  with explicit alert thresholds and automatic escalation, not merely
  that a breach was eventually detected. For a DORA + GDPR party, the
  DORA detection architecture discharges the GDPR `becoming aware` leg
  when the same detection event crosses both layers; the evidence
  layer must document which detection events triggered which role's
  awareness moment.
- **Scope caveat (CRITICAL — NIS 2 all-hazards extension)** — derived
  from CRDA-deep verified classifications: DORA Art. 10 is
  ICT-specific; NIS 2 detection is all-hazards (cybersecurity +
  operational + physical-environment, per Art. 21(2) chapeau + Recital
  56). A DORA + NIS 2 party must extend the DORA detection envelope to
  the NIS 2 all-hazards scope (physical environment + operational
  hazards beyond ICT). For pure-financial entities (NIS 2 §9 fall-back
  does not apply — DORA is lex specialis), DORA absorbs the NIS 2
  detection obligation for the ICT-hazard subset; the high-level SO
  does not aggregate across the lex-specialis boundary in that
  direction for the ICT-hazard scope, but does aggregate for the
  physical/operational hazards where NIS 2 still binds.
- **Scope caveat (CRITICAL — CRA product-internal non-substitution)** —
  derived from CRDA-deep verified classifications: CRA Annex I Part I
  (2)(l) product-internal recording does NOT substitute for entity-level
  detection (NIS 2 / DORA). A CRA-compliant product feeds detection
  signals into the deployer's entity-level pipeline, but neither
  replaces nor overlaps with the deployer's detection architecture.
  This is structurally different from D-03.1 (where CRA `verifiable
  manner` is the strictest knowledge-test floor); here, CRA product
  detection is layered under, not above, entity-level detection.
---

## Emergent tensions (from CRDA-deep §D-04.1)

#### Emergent tensions (from CRDA-deep §D-04.1)
None — sub-domain is **non-SAME in baseline (6 pairs verified as
non-SAME: 3 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE; no CRDA
corrections needed — CRDA initial classifications held after OJ-text
analysis)**. No conditional emergent tensions on the
detection-and-triage duty itself. The **detection-layer divergence**
(data-flow / entity / product-internal / financial-entity ICT) is the
**legitimately diverse dimension**: each regulator targets a distinct
layer, and the operational convergence is on a **multi-layer detection
architecture** with explicit layer hand-offs. The **trigger-anchor
divergence** (GDPR `becoming aware` / NIS 2 `detection of adverse
event` / CRA continuous-recording / DORA anomalous-activity-threshold)
is **wording-only on a common substantive duty**; each regulator
documents its trigger moment for its own notification clock, but the
detection-and-triage duty itself is the same. The **threshold-anchor
divergence** (implicit vs `appropriate and proportionate` + all-hazards
chapeau vs continuous with opt-out vs multi-layer + auto-alert + SPOF)
reflects the layered detection architecture: DORA Art. 10(2) is the
**strictest detection-architecture floor** and supports the NIS 2
`where appropriate` test on detection depth for financial-sector
entities also within retained NIS 2 scope. The **scope-disjoint
divergence** (NIS 2 §9 fall-back / DORA lex specialis on
pure-financial entities) is **handled by the lex-specialis carve-out**
— DORA absorbs the NIS 2 ICT-hazard detection obligation and the
high-level SO does not aggregate across the lex-specialis boundary in
that direction (physical + operational hazards still bind via NIS 2).
The high-level SO surfaces the common detection-and-triage duty; the
per-reg detection layer, trigger anchor, threshold qualifier, and
evidence template are documented separately in the four sub-SOs and
the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-04.1 — with
overlapping detection-layer scope-determiners on the same party —
operates a **multi-layer detection architecture** with explicit layer
hand-offs. The high-level SO (`SO-D-04.1.HL`) describes the common
detection-and-triage duty (detect, document the trigger moment,
triage, route to the downstream response / notification pipeline); the
per-reg perspective is preserved in the four sub-SOs (detection layer,
trigger anchor, threshold qualifier, evidence template, downstream
recipient). **No conflict-resolution is required on D-04.1 because
CRDA-deep verified all 6 pairs as non-SAME and non-contradictory.**
Phase 1C Doc 07 documents the **layered detection strategy**: (1) a
multi-layer detection architecture with explicit layer hand-offs at
the detection-type surfaces (data-flow vs entity vs product-internal
vs financial-entity ICT); (2) the DORA `multi-layer + auto-alert + SPOF`
floor as the operative ceiling when both DORA and NIS 2 apply on the
same detection event (DORA discharges the ICT-hazard NIS 2 detection
obligation); (3) the NIS 2 all-hazards chapeau as the extension
requirement on DORA-only parties (physical + operational hazards
beyond ICT); (4) the lex-specialis carve-out for pure-financial
entities (DORA absorbs NIS 2 ICT-hazard detection; no aggregation
across the boundary for ICT hazards; aggregation only for the
physical/operational hazards NIS 2 still binds); (5) the CRA
product-internal recording as a **feed** (not a substitute) for
entity-level detection. For proportionality (P2), a 5-FTE SaaS with
GDPR + CRA applicability may default to the GDPR `becoming aware`
trigger as the trigger moment anchor + the CRA Annex I (2)(l)
product-internal recording as the detection backbone (NIS 2 entity
detection + DORA multi-layer SPOF are out of scope); a 500-FTE DORA
financial entity must additionally implement the Art. 10(2) multi-layer
+ alert-threshold + auto-alert + SPOF-identification architecture per
`SR-DORA-011` + `SR-DORA-012`; a DORA + NIS 2 cross-sector entity
must document both the DORA multi-layer detection AND the NIS 2
all-hazards extension (physical + operational hazards) with explicit
hand-offs between them.

## Part 1 §3 — context

### 3. Security Requirements
## 4.1 Incident Detection & Triage — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md`. See that file for cross-reg verified relationships (6 pairs verified as non-SAME — no correction needed: 3 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE; the four regulators target **different detection layers** at distinct boundaries: data-flow / entity / product-internal / financial-entity ICT), scope overlap matrix, Objective/Considerations content, detection-layer divergence, DORA multi-layer + SPOF strictness, NIS 2 all-hazards extension, CRA product-internal non-substitution, and aggregation logic. **Scope-title note (P0):** the corpus index title `Incident Detection & Response` is reconciled with the CRDA-deep `Incident Detection & Triage` — this file covers detection/triage/awareness-anchoring only; `response` in the index title should be read as `detection-and-triage` for compliance purposes. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; AI Act detection obligations are coupled to the Art. 73/55 reporting triggers handled in 4.3 and not standalone). CRDA-deep verified 6 pairs as non-SAME (3 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE — none required CRDA correction). The four regulators target **different detection layers** at **distinct boundaries** (data-flow / entity / product-internal / financial-entity ICT), and the high-level SO surfaces the common detection-and-triage duty while preserving the per-reg detection layer — the four detection layers are layered, not collapsed. DORA's `multi-layer + alert-threshold + auto-alert + SPOF-identification` architecture (Art. 10(1)/(2)) is the strictest detection-architecture floor in the AEGIS corpus.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 4.1
  volere_section: 15
  volere_subtype: audit
  title: "Security-relevant events detected and triaged at the appropriate detection layer, with documented trigger moments that anchor the downstream response and notification pipelines (multi-layer detection architecture)"
  derives_from:
    hso_sub_so: SO-4.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.1.md
    objective_ref_section: "### 4.1.0"
  description: |
    The product shall detect and triage security-relevant events affecting the entity's systems, products, services, components and data at the appropriate detection layer — data-flow boundary (controller-side, personal-data ingress/egress), entity boundary (entity ICT systems, all-hazards), product-internal state (intra-product state changes), or financial-entity ICT infrastructure (anomalous ICT activities with SPOF identification) — and shall document the trigger moment of each detection event in a manner that anchors the downstream response (4.2) and notification (4.3) pipelines, as the common detection-and-triage duty converging across GDPR Art. 32(1)(b) + Art. 33(1) `becoming aware` + Art. 4(12) breach definition, NIS 2 Art. 21(2)(b) + Art. 6(8) six-action `detect` + Art. 21(2) chapeau all-hazards, CRA Annex I Part I (2)(l) recording-and-monitoring + Part II (6) vulnerability-sharing, and DORA Art. 10(1) + Art. 10(2) multi-layer + SPOF + Art. 17(1) `detect` leg, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A multi-layer detection architecture is operated with one detection pipeline per layer (data-flow / entity / product-internal / financial-entity ICT) and explicit layer hand-offs at the detection-type surfaces; each pipeline records detection object, trigger anchor, threshold qualifier, awareness/triage moment, recipient (downstream), and evidence template per asset; the DORA `multi-layer + alert-threshold + auto-alert + SPOF-identification` floor (Art. 10(2)) is the operative ceiling when both DORA and NIS 2 apply on the same detection event (DORA discharges the ICT-hazard NIS 2 detection obligation); the NIS 2 all-hazards chapeau is the extension requirement on DORA-only parties (physical + operational hazards beyond ICT); the GDPR `becoming aware` trigger moment is documented per the controller's designated breach-handling role; the CRA Annex I (2)(l) product-internal recording feeds the deployer's entity-level pipeline as a feed (not a substitute); verified by detection-architecture documentation review + per-layer detection-coverage audit + trigger-moment timestamp records inspection + layer hand-off protocol documentation + data-flow breach-detection log review (when GDPR in scope) + entity all-hazards monitoring records inspection (when NIS 2 in scope) + product-internal recording + Annex I (2)(l) opt-out mechanism review (when CRA in scope) + Art. 10(2) multi-layer + SPOF register inspection (when DORA in scope) + DPA / CSIRT / MSA / CA + ESA + AI Office inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, PR.PS-04, RS.MA-01, RS.MA-02, RS.MA-03, ID.RA-04]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping detection layers on the same party (see HSO scope-overlap principle); AI Act out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive detection-and-triage duty but each targets a distinct detection layer at a distinct boundary and anchors to a distinct trigger moment: GDPR data-flow-boundary awareness of personal-data breach (Art. 33(1) `becoming aware` — the awareness anchor is GDPR-unique and binds the 72h clock in 4.3); NIS 2 entity-side all-hazards monitoring with the 6-action `detect` leg (Art. 21(2)(b) + Art. 6(8) + Art. 21(2) chapeau + Recital 56); CRA product-side intra-product state-change recording with user opt-out (Annex I Part I (2)(l) — the recording-and-monitoring obligation is CRA-unique and provides the manufacturer's view inside the product boundary); DORA financial-entity-side multi-layer detection with alert thresholds, auto-alert and SPOF identification (Art. 10(1) + Art. 10(2) — the multi-layer + auto-alert + SPOF pattern is DORA-unique and the strictest detection-architecture floor in the AEGIS corpus). The high-level SO surfaces the common detection-and-triage duty (detect, document the trigger moment, triage, route to the downstream response/notification pipeline); the per-regulation perspective (detection layer, trigger anchor, threshold qualifier, evidence template) is preserved in the four sub-SOs. A unified SIEM may serve the technical substrate (e.g. a SIEM with multiple detection pipelines), but the policy and evidence layers must remain layer-segregated for compliance demonstration. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so that a single multi-layer detection architecture (with the per-reg detection layer, trigger anchor, threshold qualifier, and evidence template documented separately) discharges all four obligations on the same party, with explicit layer hand-offs at the detection-type surfaces. (Copied from the HSO Considerations block of `### 4.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-04.1
title: D-04.1 Incident Detection & Triage — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.1 Incident Detection & Triage
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-04_Incident-Response/D-04.1.md
status: DRAFT
---
> **Deep analysis:** [D-04.1 Incident Detection & Triage](../../DeepAnalysis/D-04_Incident-Response/D-04.1.md)
#### D-04.1 Incident Detection & Triage
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-008 | Personal-data breach detection and triaging with documented "becoming aware" moment anchoring the 72h clock | Personal data; controller/processor perspective |
| NIS2 | SO-NIS2-005 | Six-action incident-handling capability (prevent, detect, analyse, contain, respond, recover) per Art. 21(2)(b) | Entity-level ICT systems; all-hazards approach |
| CRA | SO-CRA-020 | Recording and monitoring of product internal activity with user opt-out, corruption reporting | Product with digital elements; manufacturer perspective |
| DORA | SO-DORA-007 | Multi-class anomalous-activity detection with SPOF identification per Art. 10(1)–(2) | Financial-entity ICT; performance + incidents + SPOFs |
| AI_Act | — | Out-of-scope (sole authorities: NIS2/DORA) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-04.1 per AEGIS taxonomy §4.1 — AI Act detection obligations are coupled to the Art. 73/55 reporting triggers (D-04.3) and not standalone. NIS2/DORA are the dedicated authorities for detection-and-triage architecture.
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
None. The pairwise readings above are additive — no 3-way contradiction or non-pairwise-surfacing observation. The 4-way detection layer (entity / product / personal-data / financial-entity) is layered, not contradictory.
##### SR cross-validation
NIST CSF 2.0 coverage is anchored on **DE.CM-01** (Networks monitored) and **DE.CM-09** (Computing hardware monitored) by GDPR, NIS2, and DORA; CRA anchors on **PR.PS-04** (Software logs recorded) and **DE.AE-08** (Vulnerabilities identified). The two anchor families are complementary: DE.CM-* covers the network/hardware perimeter (entity level) and PR.PS-04/DE.AE-08 covers the product-internal surface. No DE.CM or DE.AE conflict; mapping is consistent across regulations. RS.MA-* (Incident management executed) appears only in CRA (SR-CRA-027's secondary mapping) and DORA, reflecting the difference between detection-only and detection+response-triggering obligations.
##### Downstream implication
Phase 2 obligation derivation must distinguish detection-architecture obligations (DORA Art. 10, NIS2 Art. 21(2)(b)) from detection-trigger obligations (GDPR Art. 33(1) `becoming aware`). The methodology must ensure a financial entity implementing both DORA and GDPR produces a single integrated detection pipeline that satisfies both; the SO-GDPR-008 "becoming aware" anchor must be re-interpreted as the moment a DORA-detected event crosses the personal-data threshold.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-04.1
title: D-04.1 Incident Detection & Triage — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.1 Incident Detection & Triage
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-04_Incident-Response/D-04.1.md
status: DRAFT
---
> **Domain analysis:** [D-04.1 Incident Detection & Triage](../../DomainAnalysis/D-04_Incident-Response/D-04.1.md)
#### D-04.1 Incident Detection & Triage
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-04.1 per AEGIS taxonomy §4.1; AI Act detection obligations are coupled to the Art. 73/55 reporting triggers (D-04.3) and not standalone.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

