<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-03.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-03.4 Secure System Defaults](../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md)
#### D-03.4 Secure System Defaults
**Participants (from CRDA):** GDPR, CRA

## Part 1 §1 — Cross-Regulation Analysis context

### D-04 Incident Response

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-03.4 Secure System Defaults
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md`](../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md)
> (1 pair verified against OJ text — **the two participating regulations
> are GDPR, CRA; NIS 2 contributes only partial coverage via SO-NIS2-003
> Art. 21(2)(i) asset-management dimension; DORA and AI Act are
> out-of-scope** per AEGIS taxonomy §4; the single pairwise analysis is
> GDPR ↔ CRA, verified as SAME DIFFERENT-PERSPECTIVE).
>
> **P0 disagreement (labelling).** The CRDA-deep and CRDA-Domain files
> label this sub-domain "Secure System Defaults" (titled in
> [`../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md`](../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.4.md)
> and
> [`../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md`](../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.4.md)).
> The AEGIS taxonomy index
> [`../index.md`](../index.md) row 110 uses the canonical title
> "Privileged Access Management". This HSO file follows the
> index/taxonomy title (per the user's directive and per the canonical
> taxonomy); the **substantive obligation content** is sourced from
> CRDA-deep, which addresses the Art. 25(2) data-by-default + Annex I
> (2)(b)/(c) product-secure-by-default + auto-update-default obligations.
> The labelling discrepancy is flagged for Layer 2 review.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-03.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-007 | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose are processed — across amount, extent, period, and accessibility | Controller; Art. 25(2); data-protection by default; scope = personal data; "by default" across 4 dimensions (amount, extent, period, accessibility); PR.PS-01 + ID.AM-08 + GV.PO-01 |
| CRA | SO-CRA-018 + SO-CRA-019 | Product made available with secure-by-default configuration + reset to original state + automatic security updates default + opt-out + postponement | Manufacturer; Annex I Part I (2)(b) + (2)(c); product-level; "tailor-made" carve-out for business users; reset capability; auto-update default; PR.PS-01 + ID.AM-08 + GV.SC-03 |
| NIS 2 | SO-NIS2-003 (partial) | Partial coverage via SO-NIS2-003 (access control policies + HR security + asset management); NIS 2 does not impose a dedicated default-disposition SO | n/a — partial coverage; Art. 21(2)(i) asset-management dimension touches configuration-management but does not impose a secure-defaults mandate |
| DORA | — | Out-of-scope (DORA does not impose a default-disposition mandate; CRA Annex I §2(b) sole authority per taxonomy §4) | n/a |
| AI_Act | — | Out-of-scope (no default-disposition mandate; CRA sole authority per taxonomy §4) | n/a |

## Validated relationships (from CRDA-deep §D-03.4)

#### Validated relationships (from CRDA-deep §D-03.4)
The single pairwise cell — **GDPR ↔ CRA** — verified by CRDA-deep as
**SAME DIFFERENT-PERSPECTIVE** (CRDA's initial classification
confirmed by OJ-text analysis; no corrective notes). The two
regulators target **different default objects** at **different
layers**:
- **GDPR** — data-centric by default: the controller implements
  appropriate technical and organisational measures ensuring that, by
  default, only personal data which are necessary for each specific
  purpose of the processing are processed. The obligation applies to
  the amount of personal data collected, the extent of their
  processing, the period of their storage, and their accessibility
  (Art. 25(2)). In particular, the measures shall ensure that by
  default personal data are not made accessible without the
  individual's intervention to an indefinite number of natural
  persons. The four-dimensional AND (amount, extent, period,
  accessibility) is preserved from `SR-GDPR-013` `ambiguity_notes`;
  EDPB Guidelines 04/2019 on Article 25 treat the four dimensions
  as independent minima.
- **CRA** — product-centric by default: the manufacturer makes the
  product with digital elements available on the market with a
  secure-by-default configuration — including the possibility for
  the user to reset the product to its original state — unless
  otherwise agreed between manufacturer and business user in
  relation to a tailor-made product with digital elements (Annex I
  Part I (2)(b)), with the secure-by-default configuration ensuring
  that vulnerabilities can be addressed through security updates —
  automatic security updates installed within an appropriate
  timeframe, enabled by default, with a clear and easy-to-use
  opt-out mechanism, through notification of available updates to
  users, and with the option to temporarily postpone them (Annex I
  Part I (2)(c) — `SR-CRA-018` + `SR-CRA-019`).
The two regulators operate at **two different default-objects** but
converge on the same **CSF operational pivot** (PR.PS-01 configuration
management established, documented, and applied + ID.AM-08 data
managed consistent with the organisation's risk strategy):
- **GDPR** — personal data protection by default, calibrated to the
  identified processing purpose (Art. 5(1)(c) data minimisation +
  Art. 25(1) privacy by design underlying principles). The four
  dimensions — amount, extent, period, accessibility — must each be
  minimised and AND-coordinated.
- **CRA** — product secure-by-default configuration, anchored to
  state-of-the-art measures and a reset-to-original-state capability,
  with the tailor-made carve-out applying to negotiated enterprise
  configurations (R1 literal on `tailor-made` = business-user-only;
  R2 any-customised rejected as overreach; consumer products cannot
  opt out). The auto-update dimension (Annex I Part I (2)(c) —
  R1 features-enabled-on-default; R2 deny-all-initial; R3 zero-config;
  R1 chosen as adopted + R4 rejected on tailor-made-conflict).
There is **no contradiction** between the two obligations even in
overlap cases (e.g. a CRA-regulated product processing personal
data): the GDPR Art. 25(2) four-dimension test operates on the data
and the CRA Annex I (2)(b) test operates on the product configuration.
The **scope-overlap** between GDPR (data-centric) and CRA
(product-centric) is **Conditional** when a CRA product processes
personal data; the **CRA tailor-made carve-out** (Annex I Part I
(2)(b) "unless otherwise agreed between manufacturer and business
user in relation to a tailor-made product") is a product-level
configuration exception that does **NOT** apply to GDPR's
data-protection by default — a CRA tailor-made product
configuration does not exempt the controller from GDPR's
data-protection by default. The two obligations layer rather than
collide.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (CRA product processes personal data; data-by-default ↔ product-secure-by-default; CRA tailor-made carve-out does NOT exempt GDPR)  |
|  **CRA**  |  Conditional (CRA product processes personal data; product-secure-by-default ↔ data-by-default)  |  —  |
Legend: **Y** = scope overlap on a single artefact (high-level SO can
engage on a single party); **N** = scope-disjoint in baseline case; **Conditional** = disjoint in baseline case, Y on CRA-product-that-processes-personal-data scenario. CRDA-deep scope-disjoint
test: GDPR ↔ CRA = **Conditional** (no baseline scope overlap, Y on
CRA product that processes personal data; tailor-made carve-out does
not propagate into GDPR scope).

## Cross-recipient map

#### Cross-recipient map
D-03.4 generates recipient fragmentation across the two regulators at
the **compliance-demonstration point**: GDPR's supervisory authority
(Art. 25(2) by-default audit on the four dimensions — amount, extent,
period, accessibility) and CRA's market surveillance authority (Annex
VII technical documentation on secure-by-default configuration +
Annex II §6 user-facing instructions on the default state) + product
users (Annex II §6 user-facing information on the secure default +
reset capability). These are distinct regulatory channels but they do
not generate the notification cascade of D-04.3 — they are
**compliance-evidence channels** on the same default-disposition
posture. For a controller that deploys a CRA-regulated product, the
boundary hand-off at the controller-data-side ↔ product-configuration-
side interface is documented as the controlled interface; the
recipient channels layer rather than collapse, with the CRA secure-
by-default floor (Annex I (2)(b) + (2)(c)) operative on the
configuration side and the GDPR four-dimension by-default floor
operative on the data side.
---

## HSO considerations (from D-03.4.0 — High-level SecurityObjective)

**Considerations.**
- The two participating regulations impose different-perspective default-disposition obligations anchored to the same CSF operational pivot (PR.PS-01 + ID.AM-08); each targets a distinct default object: GDPR data-by-default (Art. 25(2) — four AND-coordinated dimensions: amount of data collected, extent of processing, period of storage, accessibility; the four dimensions are independent minima per EDPB Guidelines 04/2019); CRA product secure-by-default (Annex I Part I (2)(b) — secure-by-default configuration + reset-to-original-state capability + tailor-made carve-out for business users + auto-update default per Annex I Part I (2)(c) — automatic security updates enabled by default with a clear and easy-to-use opt-out mechanism + notification of available updates + option to postpone temporarily).
- The high-level SO surfaces the common default-disposition duty (baseline minimum-necessary / secure posture requiring affirmative intervention to relax); the per-regulation perspective is preserved in the two sub-SOs (default object, threshold language, evidence template, recipient).
- A single organisation across both regulators must operate a two-layer default posture with the data-centric by-default (GDPR) and the product-centric secure-by-default (CRA) documented as two layers of the same default disposition, with the CRA tailor-made carve-out NOT propagating into GDPR scope (a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2)).
- The CRA reset-to-original-state capability is the CRA-specific recovery path that returns the user to the secure baseline, supporting the GDPR Art. 25(2) four-dimension accessibility test on the data side via product recovery.
- The CRA auto-update default (Annex I Part I (2)(c)) is the CRA-specific update-default posture that ensures vulnerabilities are addressed by default without requiring affirmative user intervention, supporting the GDPR availability-and-resilience dimension on the data side via maintained-updated product configuration.
- For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- For proportionality (P2), a 5-FTE SaaS with both GDPR and CRA applicability can meet the GDPR + CRA floor with a documented data-minimisation by-default policy covering the four Art. 25(2) dimensions + a product secure-by-default configuration + reset capability + auto-update default; the same configuration typically satisfies both regulators with appropriate documentation.
- CRA is the strictest configuration floor (R1 features-enabled-on-default adopted; reset capability + tailor-made carve-out architecture) and discharges the GDPR `appropriate by-default measures` when the same party operates both manufacturer-side and controller-side roles on the same product.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 2 participating regulations each define D-03.4 over a distinct
**default-object layer** (the boundary at which the default
disposition is applied); the trigger, the textual anchor, the
threshold language, the evidence template, and the recipient all
depend on which layer the default object falls into.
| Axis (reg) | Default-object layer | Trigger | Textual anchor | Threshold language | Recipient | Evidence template |
|---|---|---|---|---|---|---|
| **GDPR** | data-centric by-default (processing systems) | continuous (Art. 25(2) four-dimension AND) | `by default, only personal data which are necessary for each specific purpose of the processing are processed` (Art. 25(2)) + four AND-coordinated dimensions (amount, extent, period, accessibility) | `appropriate technical and organisational measures` + Art. 5(1)(c) data minimisation + `without the individual's intervention` opt-in gate | supervisory authority (four-dimension by-default audit) | by-default settings across four Art. 25(2) dimensions + Art. 5(1)(c) minimisation register + opt-in-gate evidence + per-system minimisation evidence, on PR.PS-01 + ID.AM-08 + GV.PO-01 anchors |
| **CRA** | product-centric secure-by-default (product configuration) | continuous (Annex I Part I (2)(b) configuration + (2)(c) auto-update at market placement + reset capability) | `secure-by-default configuration` + `reset to original state` + tailor-made carve-out (Annex I Part I (2)(b)); `automatic security updates enabled by default` + `opt-out mechanism` + `notification of available updates` + `option to postpone` (Annex I Part I (2)(c)) | `secure by default` R1 features-enabled-on-default + reset capability R1 factory-reset-no-user-data + tailor-made R1 business-user-only + auto-update R1 enabled-by-default-with-opt-out | market surveillance authority (Annex VII technical documentation) + product users (Annex II §6 user-facing information on the secure default + reset capability) | secure-by-default configuration + reset procedure + tailor-made contractual records + auto-update default + opt-out mechanism discoverability + update-notification mechanism, on PR.PS-01 + ID.AM-08 + GV.SC-03 anchors |

## Scope-overlap matrix (2×2)

#### Scope-overlap matrix (2×2)
(See the validated-relationships table above for the 2×2 matrix; the
single pair = **Conditional** — no baseline scope overlap, Y on
CRA-product-that-processes-personal-data. The high-level SO engages
on a single party **if and only if both regulations' default-object
layers overlap on the same party** with documented boundary hand-offs.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-03.4.HL`) engages on a given party **if and only if both GDPR
and CRA are applicable AND the same product processes personal data**
(e.g. a controller that deploys a CRA-regulated product that
processes personal data; the four-dimension by-default on the data
side + the secure-by-default configuration on the product side
overlap on the same artefact). The CRA tailor-made carve-out does
NOT propagate into GDPR scope: even a bespoke CRA tailor-made product
configuration does not exempt the controller from GDPR Art. 25(2)
on the data side. Pure co-applicability of disjoint-default-object
regulations on different products does **not** trigger
cross-regulation aggregation — see the Activation logic in the file
header. For a 5-FTE SaaS startup with GDPR + CRA applicability but
the SaaS does not process personal data through the CRA product, only
the CRA sub-SO activates on the product-side and only the GDPR
sub-SO activates on the controller-side; the high-level SO engages on
the same party if both apply and the CRA product processes personal
data, with the boundary between data-centric by-default and
product-centric secure-by-default documented as the controlled
hand-off. **The two default-object layers are layered, not
collapsed**: data-centric by-default (GDPR, processing-system-side);
product-centric secure-by-default (CRA, product-side). The
high-level SO surfaces the common default-disposition duty but does
**NOT** aggregate the per-reg default objects, threshold languages,
or evidence templates.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 2 of 5 regulations participate (GDPR, CRA; NIS 2 contributes only
  partial coverage via SO-NIS2-003 Art. 21(2)(i) asset-management
  dimension but does not impose a dedicated default-disposition
  mandate; DORA and AI Act are out-of-scope per AEGIS taxonomy §4 —
  no DORA / AI Act clause imposes a default-disposition mandate; CRA
  Annex I §2(b) is sole authority per taxonomy §4 for the
  product-side).
- 1 pairwise cell, verified by CRDA-deep as **SAME
  DIFFERENT-PERSPECTIVE** after OJ-text analysis: GDPR↔CRA (CRDA
  initial DIFFERENT-PERSPECTIVE confirmed; no corrective notes).
- The two regulations impose the **same substantive
  default-disposition duty** but each targets a **distinct default
  object** at a **distinct layer**: GDPR's data-centric by-default
  on processing systems, CRA's product-centric secure-by-default on
  product configuration. The textual anchors differ (GDPR `by
  default, only personal data which are necessary for each specific
  purpose of the processing are processed` + four-dimension AND /
  CRA `secure-by-default configuration` + `reset to original state`
  + tailor-made carve-out + Annex I Part I (2)(c) auto-update
  default + opt-out + postponement). The threshold languages differ
  (GDPR `appropriate technical and organisational measures` + Art.
  5(1)(c) data minimisation + `without the individual's intervention`
  opt-in gate / CRA R1 features-enabled-on-default + R1
  factory-reset-no-user-data + R1 business-user-only tailor-made + R1
  enabled-by-default-with-opt-out auto-update). **CRA is the
  strictest configuration floor** (R1 features-enabled-on-default is
  stricter than optional-zero-state; reset capability + tailor-made
  carve-out architecture + auto-update default collectively form the
  strictest product-side disposition); **discharges the GDPR
  `appropriate by-default measures`** when the same party operates
  both manufacturer-side and controller-side roles on the same
  product.
- The high-level SO describes the **COMMON OBJECTIVE**
  (default-disposition with baseline minimum-necessary / secure
  posture requiring affirmative intervention to relax); the
  **per-regulation perspective** (default object, textual anchor,
  threshold language, evidence template, recipient) is preserved
  verbatim in the two sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions on the
  default-disposition duty itself; CRDA-deep verified the single
  pair as SAME DIFFERENT-PERSPECTIVE. Phase 1C Doc 07 does not need
  to resolve contradictions on D-03.4 because none exist on the
  default-disposition duty itself; the task is to **stack the
  documentation** so that a single two-layer default posture
  discharges both obligations on the same party (when a CRA
  product processes personal data on the same artefact), with
  explicit layer hand-offs at the controller-data-side ↔
  product-configuration-side interface. For parties that deploy a
  CRA product that does not process personal data, only the CRA
  sub-SO activates; the GDPR sub-SO does not activate on the
  product side and the high-level SO does not engage.
- **Scope caveat (CRITICAL — default-object divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does
  NOT collapse the two default-object layers into a single
  default-object layer. Data-centric by-default (processing-system)
  and product-centric secure-by-default (product-configuration) are
  **distinct default-object layers** at **distinct boundaries**,
  with distinct triggers (Art. 25(2) four-dimension AND vs Annex I
  (2)(b) configuration + (2)(c) auto-update + reset), distinct
  textual anchors, distinct threshold languages, and distinct
  evidence templates (four-dimension by-default settings + Art.
  5(1)(c) minimisation register vs Annex VII secure-by-default
  configuration + reset procedure + tailor-made contractual records
  + auto-update default + opt-out discoverability + update-
  notification mechanism). A unified configuration-management
  framework may serve the technical substrate, but the policy and
  evidence layers must remain **layer-segregated** for compliance
  demonstration. Phase 1A must therefore emit **two checks before
  applying the high-level SO** (one per participating regulation) to
  confirm that the per-reg default-object layer, textual anchor,
  threshold language, and evidence template are documented
  separately; the high-level SO surfaces the common
  default-disposition duty but does NOT aggregate the per-reg
  default-object layers.
- **Scope caveat (CRITICAL — CRA tailor-made carve-out does not
  propagate into GDPR)** — derived from CRDA-deep verified
  classifications: the CRA tailor-made carve-out (Annex I Part I
  (2)(b) `unless otherwise agreed between manufacturer and business
  user in relation to a tailor-made product with digital elements`)
  is a **product-level configuration exception** that does NOT
  apply to GDPR's data-by-default obligation on the controller side.
  A CRA tailor-made product configuration does not exempt the
  controller from GDPR Art. 25(2). The two layers remain distinct:
  the product-side configuration may be bespoke (tailor-made carve-
  out applies); the data-side processing is still under the Art.
  25(2) four-dimension AND. R1 literal reading preserves this
  non-propagation; R2 (any-customised) overreaches the carve-out.
- **Scope caveat (CRITICAL — auto-update default posture)** —
  derived from CRDA-deep verified classifications: the CRA Annex I
  Part I (2)(c) auto-update default posture (`automatic security
  updates installed within an appropriate timeframe, enabled by
  default, with a clear and easy-to-use opt-out mechanism, through
  notification of available updates to users, and with the option to
  temporarily postpone them`) is the **CRA-specific
  update-default posture** that ensures vulnerabilities are
  addressed by default without requiring affirmative user
  intervention. R1 features-enabled-on-default adopted; R2 deny-all
  initial state; R3 zero-config security; R2 and R3 are
  operationally convergent with R1 in many cases but R1 is the
  literal anchor. R4 (post-deployment configuration surface)
  rejected where it would conflict with the tailor-made carve-out.
  The auto-update default supports the GDPR availability-and-
  resilience dimension (Art. 32(1)(b)/(c) implicitly via processed
  data) on the data side via maintained-updated product
  configuration.
---

## Emergent tensions (from CRDA-deep §D-03.4)

#### Emergent tensions (from CRDA-deep §D-03.4)
None — sub-domain is **single-pair SAME DIFFERENT-PERSPECTIVE** (1
pair verified as SAME DIFFERENT-PERSPECTIVE after OJ-text analysis;
CRDA's initial DIFFERENT-PERSPECTIVE confirmed; no corrective notes).
No conditional emergent tensions on the default-disposition duty
itself. The **default-object divergence** (data-centric by-default vs
product-centric secure-by-default) is the **legitimately diverse
dimension**: each regulator targets a distinct default object at a
distinct layer, and the operational convergence is on a **two-layer
default posture** with explicit layer hand-offs. The
**textual-anchor divergence** (GDPR Art. 25(2) four-dimension AND +
`without the individual's intervention` opt-in gate / CRA Annex I
Part I (2)(b) `secure-by-default configuration` + `reset to original
state` + tailor-made carve-out + Annex I Part I (2)(c) auto-update
default + opt-out + postponement) is **wording-only on a common
substantive default-disposition duty**; the strictest configuration
floor (CRA R1 features-enabled-on-default) discharges the looser ones
on the same party when the same configuration substrate operates both
roles. The **threshold-language divergence** (GDPR `appropriate
technical and organisational measures` + Art. 5(1)(c) data minimisation
+ `without the individual's intervention` opt-in gate / CRA R1
features-enabled-on-default + R1 factory-reset + R1
business-user-only tailor-made + R1 enabled-by-default-with-opt-out
auto-update) is **wording-only on different operational anchors**
that converge on the same substantive default-disposition duty. The
**scope-divergence** (GDPR Art. 25(2) applies to processing systems;
CRA Annex I (2)(b) applies to products with digital elements; CRA
tailor-made carve-out product-level only and does NOT propagate into
GDPR scope on the data side) is **handled by the layer-segregation
discipline** — the two layers remain distinct: the product-side
configuration may be bespoke (tailor-made carve-out applies); the
data-side processing is still under the Art. 25(2) four-dimension
AND. The high-level SO surfaces the common default-disposition duty;
the per-reg default object, textual anchor, threshold language,
evidence template, and recipient are documented separately in the two
sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with both GDPR and CRA applicable in scope of D-03.4 — and
operating a CRA-regulated product that processes personal data —
operates a **two-layer default posture** with explicit layer hand-
offs. The high-level SO (`SO-D-03.4.HL`) describes the common
default-disposition duty (baseline minimum-necessary / secure posture
requiring affirmative intervention to relax); the per-reg perspective
is preserved in the two sub-SOs (default object, textual anchor,
threshold language, evidence template, recipient). **No conflict-
resolution is required on D-03.4 because CRDA-deep verified the
single pair as SAME DIFFERENT-PERSPECTIVE on the default-disposition
duty.** Phase 1C Doc 07 documents the **two-layer default strategy**:
(1) a data-centric by-default configuration on the processing-system
side covering all four Art. 25(2) dimensions simultaneously, with the
EDPB Guidelines 04/2019 four-independent-minima reading preserved;
(2) a product-centric secure-by-default configuration on the product-
configuration side with reset capability + tailor-made carve-out
architecture + auto-update default posture; (3) the CRA
tailor-made carve-out as **NOT** propagating into GDPR scope on the
data side; (4) the CRA reset-to-original-state capability as the
**CRA-specific recovery path** that supports the GDPR
four-dimension accessibility test on the data side via product
recovery; (5) the CRA auto-update default as the **CRA-specific
update-default posture** that supports the GDPR availability-and-
resilience dimension via maintained-updated product configuration.
For proportionality (P2), a 5-FTE SaaS with both GDPR and CRA
applicability and a CRA product that processes personal data can meet
the GDPR + CRA floor with a documented data-minimisation by-default
policy covering the four Art. 25(2) dimensions + a product secure-
by-default configuration + reset capability + auto-update default;
the same configuration typically satisfies both regulators with
appropriate documentation; for a CRA product that does NOT process
personal data, only the CRA sub-SO activates on the product side,
the GDPR sub-SO does not activate on the product side, and the
high-level SO does not engage.

## Part 1 §3 — context

### 3. Security Requirements
## D-03.4 Secure System Defaults — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.4.md`. See that file for cross-reg verified relationships (1 pair verified — GDPR ↔ CRA as **SAME DIFFERENT-PERSPECTIVE**; CRDA initial DIFFERENT-PERSPECTIVE confirmed after OJ-text analysis; no corrective notes), scope overlap matrix (2×2 — only 2 participants), Objective/Considerations content, default-object-layer divergence (data-centric by-default on processing systems / product-centric secure-by-default on product configuration), the EDPB Guidelines 04/2019 four-independent-minima reading on Art. 25(2), CRA R1 features-enabled-on-default + R1 factory-reset + R1 business-user-only tailor-made + R1 enabled-by-default-with-opt-out readings, the CRA tailor-made carve-out NOT propagating into GDPR scope, the labelling discrepancy with the AEGIS taxonomy index row 110 ("Privileged Access Management" vs "Secure System Defaults" — substantive obligation content sourced from CRDA-deep), and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA (2 of 5 regs — NIS 2 contributes only partial coverage via SO-NIS2-003 Art. 21(2)(i) asset-management dimension and does not impose a dedicated default-disposition mandate; DORA and AI Act out-of-scope per AEGIS taxonomy §4 — no DORA / AI Act clause imposes a default-disposition mandate; CRA Annex I §2(b) is sole authority per taxonomy §4 for the product-side). CRDA-deep verified the single pair (GDPR ↔ CRA) as **SAME DIFFERENT-PERSPECTIVE** with no corrective notes. The two regulators target **different default-object layers** at distinct boundaries: GDPR data-by-default (Art. 25(2) four AND-coordinated dimensions — amount, extent, period, accessibility) and CRA product secure-by-default (Annex I Part I (2)(b) configuration + reset + tailor-made carve-out + Annex I Part I (2)(c) auto-update default + opt-out + postponement); the high-level SO surfaces the common default-disposition duty (baseline minimum-necessary / secure posture requiring affirmative intervention to relax) while preserving the per-reg default-object layer — the two layers are layered, not collapsed.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 3.4
  volere_section: 15
  volere_subtype: access
  title: "Default disposition of data-centric processing systems and product-centric configurations managed so that the baseline state is the minimum-necessary / secure configuration (two-layer default posture with explicit layer hand-offs)"
  derives_from:
    hso_sub_so: SO-D-03.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.4.md
    objective_ref_section: "### D-03.4.0"
  description: |
    The product shall manage the default disposition of the entity's data-centric processing systems and the product's product-centric configuration so that the baseline state of every processing system and every product configuration is the minimum-necessary / secure configuration, with relaxation requiring affirmative data-subject or user intervention, as the common default-disposition duty converging across GDPR Art. 25(2) four AND-coordinated dimensions (amount of data collected, extent of processing, period of storage, accessibility) + Art. 25(1) privacy-by-design + Art. 5(1)(c) data minimisation and CRA Annex I Part I (2)(b) secure-by-default configuration + reset-to-original-state capability + tailor-made carve-out + Annex I Part I (2)(c) automatic security updates enabled by default + opt-out + postponement, where both regulations apply on the same party AND the CRA product processes personal data (the controlled interface at which the two layers stack up on the same artefact).
  fit_criterion: |
    A two-layer default posture operates with one default register per layer (data-centric by-default settings across the four Art. 25(2) AND-coordinated dimensions + Art. 5(1)(c) minimisation register + opt-in-gate evidence; product-centric secure-by-default configuration + reset procedure + tailor-made contractual records + auto-update default + opt-out discoverability + update-notification mechanism); explicit layer hand-off protocols are documented at the controller-data-side ↔ product-configuration-side interface; the four GDPR Art. 25(2) dimensions are minimised independently and AND-coordinated per EDPB Guidelines 04/2019 (any reading allowing some dimensions to be relaxed if others are tightened is rejected); the CRA tailor-made carve-out does NOT propagate into GDPR scope — even a bespoke CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side; the CRA reset-to-original-state capability is the CRA-specific recovery path that supports the GDPR four-dimension accessibility test on the data side via product recovery; the CRA auto-update default is the CRA-specific update-default posture that supports the GDPR availability-and-resilience dimension via maintained-updated product configuration; the CRA R1 features-enabled-on-default is the strictest product-side configuration floor and discharges the GDPR `appropriate by-default measures` when the same party operates both manufacturer-side and controller-side roles on the same product; verified by four-dimension by-default settings audit + Art. 5(1)(c) minimisation register review + opt-in-gate evidence + secure-by-default configuration + reset procedure evidence + tailor-made contractual records + auto-update default documentation + opt-out discoverability check + update-notification mechanism review + DPA / MSA / ENISA inspection-ready evidence packs on request.
  priority: MUST
  verification_method: TEST
  dependencies: [3.1.1 (data-subject identity verification feeds the opt-in-gate evidence), 3.1.3 (product-side identity substrate feeds the secure-by-default baseline)]
  nist_csf: [PR.PS-01, ID.AM-08, GV.PO-01, GV.SC-03]
  applicable_if:
    regs: [GDPR, CRA]
    scope_overlap: conditional   # HL engages only when both GDPR and CRA are applicable AND the same CRA product processes personal data (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The two participating regulations impose different-perspective default-disposition obligations anchored to the same CSF operational pivot (PR.PS-01 + ID.AM-08); each targets a distinct default object at a distinct layer — GDPR data-by-default (processing-system side, four AND-coordinated Art. 25(2) dimensions per EDPB Guidelines 04/2019 four-independent-minima reading; the `without the individual's intervention` opt-in gate closes the accessibility dimension; Art. 5(1)(c) data minimisation is the underlying principle; Art. 25(1) privacy-by-design supplies the design-time counterpart) and CRA product secure-by-default (product-configuration side, Annex I Part I (2)(b) configuration + reset-to-original-state + tailor-made carve-out + Annex I Part I (2)(c) auto-update default + opt-out + postponement; R1 features-enabled-on-default adopted on secure-by-default with R2 deny-all-initial and R3 zero-config-security as operationally-convergent alternative readings rejected where they would conflict with the tailor-made carve-out; R1 factory-reset-no-user-data on reset semantic; R1 business-user-only on tailor-made scope; R1 enabled-by-default-with-opt-out on auto-update). The two layers are layered, not collapsed: a unified configuration-management framework may serve the technical substrate, but the policy and evidence layers must remain layer-segregated for compliance demonstration. The CRA tailor-made carve-out does NOT propagate into GDPR scope — a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so a single two-layer default posture discharges both obligations on the same party (when a CRA product processes personal data on the same artefact), with explicit layer hand-offs at the controller-data-side ↔ product-configuration-side interface. For parties that deploy a CRA product that does NOT process personal data, only the CRA sub-SO activates on the product side, the GDPR sub-SO does not activate on the product side, and the high-level SO does not engage. (Copied from the HSO Considerations block of `### D-03.4.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-03.4
title: D-03.4 Secure System Defaults — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.4 Secure System Defaults
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-03_Access-Control/D-03.4.md
status: DRAFT
---
> **Deep analysis:** [D-03.4 Secure System Defaults](../../DeepAnalysis/D-03_Access-Control/D-03.4.md)
#### D-03.4 Secure System Defaults
<!-- participants: GDPR, CRA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-007 | Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose are processed — across amount, extent, period, accessibility | Controller; Art. 25(2); data-protection by default; scope = personal data; "by default" across 4 dimensions (amount, extent, period, accessibility) |
| CRA | SO-CRA-018 / SO-CRA-019 / SO-CRA-025 / SO-CRA-026 | Product made available with secure-by-default configuration + reset to original state + automatic security updates default + opt-out + postponement | Manufacturer; Annex I Part I (2)(b) + (2)(c); product-level; "tailor-made" carve-out; reset capability |
| NIS2 | — | Partial coverage via SO-NIS2-003 (Art. 21(2)(i) — asset-management dimension covers configuration); no dedicated secure-defaults SO | n/a |
| DORA | — | Out-of-scope (no secure-defaults mandate; CRA Annex I §2(b) sole authority per taxonomy §4) | n/a |
| AI_Act | — | Out-of-scope (no secure-defaults mandate; CRA sole authority per taxonomy §4) | n/a |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
- None. Only two regulators (GDPR + CRA) have substantive secure-defaults mandates; NIS 2 contributes only a partial coverage via SO-NIS2-003 (Art. 21(2)(i) — asset-management dimension); DORA and AI Act are out-of-scope.
##### SR cross-validation
GDPR maps to ID.AM-08 (data managed consistent with risk strategy) + GV.PO-01 (organisational cybersecurity policy); CRA maps to PR.PS-01 (configuration management) + ID.AM-08 + GV.SC-03 (contractual supply-chain). The shared ID.AM-08 anchor is the operational pivot; the divergent anchors (GV.PO-01 vs PR.PS-01) reflect the data-centric vs product-centric perspective split. No contradictory mappings.
##### Downstream implication
For Phase 1C Doc 07, D-03.4 is a **two-layer default** sub-domain: a controller deploying a CRA-regulated product is bound by both the data-centric by-default (GDPR) and the product-centric secure-by-default (CRA). Proportionality: a small SaaS meets the GDPR + CRA floor with a documented data-minimisation by-default policy + a product secure-by-default configuration + reset capability; the same configuration typically satisfies both regulators with appropriate documentation.
---
### Summary of cross-regulation observations
#### Cross-cutting observations (informative for Phase 1C Doc 07)
1. **Sole-authority sub-domains** (per AEGIS taxonomy §4): D-02.3 CVD (CRA sole); D-03.4 — partial (CRA sole for product-side, GDPR for data-side; NIS 2 partial via SO-NIS2-003 asset-management); D-07.x (out of Part A range); D-08.3 Management Board Training (DORA + NIS 2 sole; out of Part A range). Within Part A: D-02.2 has CRA + DORA as substantive authorities; D-02.3 has CRA as sole substantive authority; D-03.4 has GDPR (data-side) + CRA (product-side) as the two substantive authorities.
2. **Common CSF pivots**: PR.DS-01 (D-01.1), PR.DS-02 (D-01.2), PR.AA-05 (D-03.3), PR.AA-03 (D-03.2), ID.RA-01 (D-02.1), PR.PS-02 (D-02.2). These six CSF subcategories are the operational substrate for the 12 sub-domains and form the natural Layer 2/3 reconciliation anchors.
3. **T-vs-text gaps (Layer 2 review candidates)**: NIS 2 Art. 21(2)(i) (T3 imposed RBAC + need-to-know + least privilege not in OJ) and DORA Art. 9(4)(c) (T4 imposed `need-to-know and least privilege` not in OJ literal) and DORA Art. 9(4)(d) (T4 imposed MFA not in OJ literal `strong authentication`) and AI Act AIA-C11 (T5 cited Art. 12(4) which does not exist in OJ). These are material reading-choice divergences that propagate to the pairwise matrix and emergent-tension cells.
4. **State-of-the-art and "appropriate" polysemy** (cross-cutting Berry-classic): GDPR `appropriate` (Art. 5(1)(f), Art. 25, Art. 32), NIS 2 `appropriate and proportionate` (Art. 21(1)), CRA `state of the art` (Annex I (2)(e)), DORA `high standards` (Art. 9(2)). The four anchors differ in operational depth and P1 risk: CRA's state-of-the-art is the strictest (harmonised-standards floor), DORA's "high standards" is the least specified (pending ESAs RTS), GDPR's "appropriate" is risk-anchored, and NIS 2's "appropriate and proportionate" is multi-factor (state of the art + cost + exposure + size + likelihood/severity).
5. **P1 (Compliant ≠ Secure) reminders** (per AEGIS P1 principle):
   - **D-01.1/D-01.2/D-01.3**: a state-of-the-art encryption baseline (CRA / DORA) does not guarantee that the key-management architecture is operationally separable (P6) or that the deployment architecture is resilient (P1). The compliance + security gap is operational, not technical.
   - **D-02.1/D-02.4**: a vulnerability-identification programme (ID.RA-01) + a testing programme (PR.PS-06) does not guarantee that identified vulnerabilities are remediated within an operationally defensible cadence (P1). The compliance + security gap is the remediation-velocity dimension.
   - **D-03.1/D-03.2/D-03.3**: a documented access-control policy (PR.AA-05) does not guarantee that the access grants are actually operated per least privilege in production (P1). The compliance + security gap is the operational discipline dimension.
6. **P2 (Company Reality First — Proportionality Is Not Optional) reminders**:
   - 5-FTE SaaS: D-01.1, D-01.2 typically met by default-on cloud-platform encryption (PR.DS-01 + PR.DS-02); D-01.3 met by cloud-provider HSM (no separate architecture needed); D-02.1 met by SCA + SAST + vendor advisories (ID.RA-01 + ID.AM-02 SBOM if CRA scope); D-03.1/D-03.2/D-03.3 met by IdP-as-a-Service (PR.AA-01 + PR.AA-03 + PR.AA-05).
   - 500-FTE financial entity (DORA scope): the DORA "high standards" anchor + the at-least-yearly hard anchor on risk-scenario review + the TLPT 3-year cycle + the documented patch policy + the strong-authentication layer materially expand the architecture.
   - DORA + NIS 2 + GDPR + CRA + AI Act all-in-scope entity: the layered testing + the AI-specific attack taxonomy + the multi-boundary identity architecture + the layered access-control with the DORA "only" qualifier + the deep key-management stack are the operative floor.
7. **P3 (Multiple Perspectives)**: each pairwise matrix cell carries at least two perspectives (Compliance + Security, or Product + Entity, or Personal-Data + ICT-System, or Staff + Data-Subject, or Workforce + Product-User). The 4-axis framework (Compliance / Security / Business / Risk / Technical) is implicitly embedded in the relationship classification.
8. **P4 (Deliberation Over Isolation)**: the pairwise matrix and emergent-tension cells are the deliberation substrate; each pair + each emergent is a position that should be challenged and re-litigated in Phase 1C Doc 07 review.
9. **P5 (Change Propagation)**: a change to any of the five SO/SR files (e.g. an OJ-corrective note in CRA-CL134 or DORA-C08) propagates to this staging file. The relationship-classification and emergent-tension cells are sensitive to the source SR IDs' content; P5 vigilance is required.
10. **P6 (Start From Reality, Not From Regulations)**: the four requirements with no security rationale distinct from the regulatory rationale (P1 collapse risk) are flagged in the source SR files' `ambiguity_notes` and propagated to the cross-validation cells. The Layer 2/3 review should test each pairwise cell against a real-company deployment to confirm the compliance + security gap is documented.
11. **P7 (Human Is the Final Arbiter)**: all relationship classifications and emergent-tension cells are the Executor's first cut and are subject to human review in Phase 1C Doc 07. The P0 disagreement report below records the Executor's substantive disagreements with the source materials.
---
**End of Part A staging file.**
---
## Cross-Regulation Domain Analysis — Part B
> **Scope.** This Part B covers 12 sub-domains across 3 macro-domains: D-04 (Incident Response),
> D-05 (Data Lifecycle), D-06 (Supply Chain). Part A covered D-01, D-02, D-03. Parts A+B together
> cover half of the 10×38 taxonomy. Remaining 18 sub-domains are staged for Part C/D.
>
> **Reading guide.** Each sub-domain section contains: (1) participants table with SO IDs,
> (2) pairwise matrix using the 4-type relationship taxonomy, (3) emergent tensions (only when
> 3+ regulations and tensions exceed the sum of pairwise readings), (4) SR cross-validation
> via NIST CSF 2.0, (5) downstream implication for downstream phases (Phase 2 obligation
> derivation + Phase 3 case generation).
---
### D-04 Incident Response
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-03.4
title: D-03.4 Secure System Defaults — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.4 Secure System Defaults
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-03_Access-Control/D-03.4.md
status: DRAFT
---
> **Domain analysis:** [D-03.4 Secure System Defaults](../../DomainAnalysis/D-03_Access-Control/D-03.4.md)
#### D-03.4 Secure System Defaults
**Participants (from CRDA):** GDPR, CRA

## Part 3 — context

### D-04 Incident Response
---

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
