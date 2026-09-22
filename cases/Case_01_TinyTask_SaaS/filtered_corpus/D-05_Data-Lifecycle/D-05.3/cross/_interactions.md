<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-05.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-05.3 Right to Erasure](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md)
#### D-05.3 Right to Erasure
<!-- participants: GDPR, CRA -->
**Participants (from CRDA):** GDPR, CRA
**Sole-authority note:** NIS2, DORA, and AI Act are out-of-scope for D-05.3 per AEGIS taxonomy §4.1. GDPR Art. 17 is the dedicated authority for personal-data erasure. CRA Annex I Part I (2)(m) addresses product-data removal which may include personal data but is not framed as a data-subject right.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-05.3 Right to Erasure
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md`](../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md)
> (1 pair verified against OJ text — **2 of 5 participating regulations
> are GDPR, CRA; NIS 2, DORA, AI Act are out-of-scope per AEGIS
> taxonomy §4.1** as noted by `DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md`
> line 36: "NIS2, DORA, and AI Act are out-of-scope for D-05.3 per AEGIS
> taxonomy §4.1. GDPR Art. 17 is the dedicated authority for personal-data
> erasure. CRA Annex I Part I (2)(m) addresses product-data removal which
> may include personal data but is not framed as a data-subject right").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-05.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-018 + SG-GDPR-019 | Personal data erased without undue delay on the data subject's Art. 17(1) request + processor deletion or return of all personal data (Art. 28(3)(g)) after end of processing services, with existing copies deleted unless Union/Member State law requires storage | Personal data; controller + processor; Art. 17(1)(a)–(f) + Art. 17(2) + Art. 28(3)(g) + Art. 5(1)(c)/(e) cross-refs + Art. 19 cascade (cross to D-04.3 SG-GDPR-012); PR.DS-10 + ID.AM-08 + GV.SC-04 |
| CRA | SG-CRA-036 | User of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner | Product data (personal or other) + settings; manufacturer-bound; Annex I Part I (2)(m) first limb (terminal deletion) + second limb (cross-product secure transfer) + Annex II §8(d) decommissioning instructions; PR.DS-10 + ID.AM-08 (+ PR.DS-02 for the second limb) |

## Validated relationships (from CRDA-deep §D-05.3)

#### Validated relationships (from CRDA-deep §D-05.3)
Of 1 pair, **1 verified as SAME — COMPLEMENTARY** (CRDA initial classification held after OJ-text analysis); **no SCOPE-DISJOINT, no CORRECTED, no CONTRADICTORY classifications** on the erasure duty:
- **GDPR ↔ CRA** — COMPLEMENTARY (SAME): GDPR Art. 17 is a **data-subject right** (controller-bound, triggered by the data subject's Art. 17(1) request, grounded in the Art. 5(1)(c) data-minimisation + Art. 5(1)(e) storage-limitation principles + Art. 28(3)(g) processor-side mirror); CRA Annex I Part I (2)(m) is a **user-facing mechanism** (manufacturer-bound, embedded in product design at Art. 13(1) design-time, information-supplied under Art. 13(18) + Annex II §8(d)). When the user exercising the CRA removal is also the data subject exercising Art. 17 on the same product, the two obligations stack and do not contradict: the **manufacturer-side (CRA) layer** provides the secure and easily-removable affordance + the documented data-class inventory enabling comprehensive deletion; the **controller-side (GDPR) layer** executes the Art. 17(1) trigger through that affordance, applies the controller-side necessity test for the 6 Art. 17(1) grounds (a)–(f), honours the Art. 12 transparency + Art. 17(2) confirmation-of-action obligations, and cascades per Art. 19 to downstream recipients (the Art. 19 cascade is in D-04.3 — SG-GDPR-012 — because notification is the structural element there). The **polysemy of `deletes` in Art. 28(3)(g)** (Berry-flagged POLY-S3 — physical destruction vs logical deletion vs cryptographic erasure) is resolved by `SR-GDPR-030` to the **cryptographic-erasure reading**: destruction of the cryptographic key (held outside the data substrate) scales across backups and replicas without per-copy destruction and aligns with EDPB Guidelines 5/2020 on storage limitation. The CRA product design must **support that cryptographic-erasure path** — Annex I Part I (2)(m) `securely and easily remove on a permanent basis` is satisfied when the manufacturer exposes a key-destruction affordance or, where not feasible, a secure-overwrite affordance that achieves equivalent recovery-infeasibility. The CRA `securely and easily` qualifier is **VAG+COORD-S2** (R1 — bot... (line truncated to 2000 chars)
The erasure architecture is **legitimately layered** — the data-subject right (GDPR) and the product-side affordance (CRA) target the **same operational aim** (render the user's data inaccessible on the user's election) but operate on **complementary layers** (controller-side policy execution vs manufacturer-side product design). The high-level SO surfaces the **common erasure duty**; the per-regulation perspective is preserved verbatim in the 2 sub-SOs (controller-side right execution vs manufacturer-side affordance provision).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  **Y** (when the data subject invoking Art. 17(1) is also the user invoking the CRA (2)(m) removal mechanism on a CRA-classified product processing personal data; the two obligations stack — manufacturer enables the mechanism, controller operationalises the right)  |
|  **CRA**  |  **Y** (same condition, reciprocal)  |  —  |
Legend: **Y** = scope overlap on the same event at the same party (the only gating condition for the high-level SO to engage on D-05.3). **N/A** = no scope question for the self-pair. CRDA-deep scope-disjoint test: GDPR↔CRA = **Y when (i) CRA-classified product processing personal data AND (ii) the user is the data subject AND (iii) the request is exercised through the product-side affordance AND (iv) the request reaches the controller-side policy execution** — outside the joint condition, the obligation is single-regulator (a pure CRA-only product with no personal-data subset invokes the manufacturer-only CRA layer; a GDPR-only controller with no CRA-classified product invokes the controller-only GDPR layer without a product-side affordance dependency).

## Cross-recipient map

#### Cross-recipient map
D-05.3 itself does **not** generate recipient asymmetry on the erasure event — the erasure process is **inward-looking** (the controller / manufacturer executes the deletion through their own infrastructure, then propagates the deletion result to the operational evidence base). The recipient fragmentation is at the **downstream compliance-demonstration point**: **GDPR's supervisory authority (DPA)** on the Art. 5(2) accountability evidence (Art. 17(2) confirmation + Art. 30 RoPA record update + Art. 5(1)(c)/(e) policy evidence + Art. 28(3)(g) processor-side mirror where applicable) and on the Art. 19 cascade to downstream recipients where erasure is invoked (the cascade is structured in D-04.3 SG-GDPR-012); **CRA's market surveillance authority (MSA)** on the Annex VII §2 technical-documentation evidence (data-class inventory + deletion-mechanism documentation + Annex II §8(d) decommissioning instructions) and on the Annex VII §6 test reports demonstrating verification of conformity with Annex I Part I (2)(m). These are distinct regulatory channels on the same erasure event but they do **not** generate a notification cascade of D-05.3 itself — they are **compliance-evidence channels on the same erasure architecture**. **The Art. 19 cascade (GDPR → downstream recipients) is structurally in D-04.3 (SG-GDPR-012) because notification to recipients is the distinct obligation; the erasure itself is D-05.3 (SG-GDPR-018 + SG-GDPR-019).**
---

## HSO considerations (from D-05.3.0 — High-level SecurityObjective)

**Considerations.**
- Two participating regulations (GDPR, CRA) stack on the same party in the personal-data subset: GDPR Art. 17(1) data-subject right (controller-bound, 6 grounds (a)–(f)) with Art. 17(2) confirmation + Art. 12 transparency + Art. 19 cascade (to D-04.3) + Art. 28(3)(g) processor-side mirror; CRA Annex I Part I (2)(m) first-limb terminal deletion + second-limb secure cross-product transfer (manufacturer-bound). CRDA-deep verified GDPR↔CRA = COMPLEMENTARY (SAME, layer-stacking pattern).
- Deletion path converges on cryptographic-erasure or secure-overwrite (both compatible with SR-GDPR-030 + SR-CRA-048); evidence templates diverge (Art. 5(2) accountability + Art. 30 RoPA + Art. 17(2) confirmation + Art. 19 cascade vs Annex VII §2 technical documentation + Annex II §8(d) decommissioning instructions + Annex VII §6 test reports).
- Art. 17(1) `without undue delay` and CRA `securely and easily` are both VAG (no quantitative clock); the controller-side service-level governs policy execution (typically monthly under EDPB practice, ≤2 months under Art. 12(3) for complex requests); the manufacturer-side affordance-depth governs architectural support (calibrated per Art. 13(2) risk assessment). The two clocks are not aligned by the high-level SO.
- Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving/research/statistical, establishment-exercise-defence of legal claims) are the layer-segregated exception structure: GDPR-side Art. 17(3) governs the controller; CRA-side (2)(m) governs the manufacturer; the two do NOT override each other.
- For a 5-FTE SaaS with GDPR-only applicability, only the GDPR sub-SO activates; for a CRA-only manufacturer (no personal data), only the CRA sub-SO activates; for an integrated manufacturer-controller on a CRA-classified product, both sub-SOs stack on the same product event.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 2 participating regulations each define D-05.3 over a distinct **layer** of the erasure architecture; the layer, the trigger, the deletion path, the recipient, and the legal anchor all depend on whether the obligation is layer-side (manufacturer) or controller-side (GDPR).
| Axis (reg) | Layer | Trigger | Deletion path | Evidence template | Recipient | Legal anchor |
|---|---|---|---|---|---|---|
| **GDPR** | controller-side policy execution on personal data (data-subject right + processor mirror) | data subject's Art. 17(1) request (6 grounds (a)–(f)) — TRIGGERED; processor's contract-end moment under Art. 28(3)(g) — PER-CONTRACT-END | cryptographic key-destruction (SR-GDPR-030 POLY-S3 → cryptographic-erasure reading) where the controller retains the key outside the data substrate and the data is encrypted at rest; secure overwrite where cryptographic-erasure is not feasible; physical-media destruction as ultimate fallback (rare, narrow) | Art. 5(2) accountability evidence (Art. 17(2) confirmation + Art. 12 transparency + Art. 30 RoPA record update + Art. 35(7) DPIA record where applicable) + processor-side Art. 28(3)(g) deletion-or-return record | supervisory authority (DPA) — Art. 58 inspection; downstream recipients per Art. 19 cascade (D-04.3 SG-GDPR-012) | Art. 17(1)(a)–(f) + Art. 17(2) + Art. 17(3)(a)–(e) exceptions + Art. 28(3)(g) + Art. 5(1)(c)/(e) cross + Art. 12 transparency + Art. 19 cascade |
| **CRA** | manufacturer-side user-facing removal affordance on product data + settings + secure cross-product transfer | user's product-initiated removal request — TRIGGERED; user's election to transfer to another product — TRIGGERED | secure permanent removal (SR-CRA-048 VAG+POLY-S2 → cryptographic-erase / secure-overwrite / physical-media-destruction R3 reading) + secure cross-product transfer (SR-CRA-049 VAG-S2 → confidentiality + integrity + destination-authentication R1) | Annex VII §2 technical documentation (data-class inventory + deletion-mechanism architecture) + Annex II §8(d) decommissioning instructions + Annex VII §6 test reports demonstrating verification of conformity with Annex I Part I (2)(m) | market surveillance authority (MSA) — Annex VII compliance demonstration on reasoned request; user as the direct recipient of the removal affordance | Annex I Part I (2)(m) first limb + second limb + Art. 13(1) design-time + Art. 13(18) + Annex II §8(d) + Art. 13(2) risk assessment underpinning the deletion-mechanism depth |

## Scope-overlap matrix (2×2)

#### Scope-overlap matrix (2×2)
(See the validated-relationships table above for the 2×2 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-05.3.HL`) engages on a given party **if and only if ≥2 applicable
regulations' layer scope-determiners overlap on the same party** (e.g.
a GDPR controller that also manufactures CRA-classified products that
process personal data, with both the controller's Art. 17 policy
execution and the manufacturer's (2)(m) affordance operating on the
same product event — a vertically-integrated manufacturer-controller on
a stacked erasure architecture). Pure co-applicability of disjoint-layer
regulations on different events does **not** trigger cross-regulation
aggregation — see the Activation logic in the file header. For a 5-FTE
SaaS startup with GDPR-only applicability (no CRA-classified products
processing personal data in scope), only the GDPR sub-SO activates; the
high-level SO is redundant in this single-regulator case but is still
emitted for traceability. **The two layers are stacked, not collapsed**:
the controller-side layer executes the policy through the
manufacturer-side layer; the high-level SO surfaces the common erasure
duty but does **NOT** aggregate the per-reg layer, trigger, deletion
path, evidence template, or recipient.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 2 of 5 regulations participate (GDPR, CRA; NIS 2, DORA, AI Act are
  out-of-scope per AEGIS taxonomy §4.1 — GDPR Art. 17 is the dedicated
  authority for personal-data erasure; CRA Annex I Part I (2)(m) addresses
  product-data removal which may include personal data but is not framed
  as a data-subject right; the three other regulations do not impose
  erasure-as-data-subject-right obligations).
- 1 pairwise cell, verified by CRDA-deep as **1 SAME — COMPLEMENTARY**
  (GDPR ↔ CRA: CRDA initial classification held; the pair STACKS — the
  manufacturer enables the deletion affordance (CRA), and the controller
  operationalises the data-subject right through that affordance (GDPR);
  no SCOPE-DISJOINT, no CONTRADICTORY, no CORRECTED classifications).
- The two regulations impose **the same substantive erasure duty**
  (render the user's data inaccessible on the user's election) but each
  operates on a **distinct layer** with a **distinct trigger**:
  controller-side policy execution on Art. 17(1) grounds (GDPR,
  data-subject-initiated) vs manufacturer-side user-facing removal
  affordance (CRA, user-initiated); the deletion path converges on
  cryptographic-erasure or secure-overwrite (both readings are compatible
  with SR-GDPR-030 + SR-CRA-048); the evidence templates diverge
  (Art. 5(2) accountability + Art. 30 RoPA + Art. 17(2) confirmation +
  Art. 19 cascade vs Annex VII §2 technical documentation + Annex II
  §8(d) decommissioning instructions + Annex VII §6 test reports).
- The high-level SO describes the **COMMON OBJECTIVE** (render the user's
  data inaccessible on the user's election; support the data-subject
  right through the product-side affordance; cascade to recipients per
  Art. 19 where applicable; execute the cryptographic-erasure deletion
  path per SR-GDPR-030 on the personal-data subset; deliver the
  documentary evidence base); the **per-regulation perspective** (layer,
  trigger, deletion path, evidence template, recipient) is preserved
  verbatim in the 2 sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are **0 conditional emergent tensions** in this sub-domain (only
  2 regulations participate; no 3-way interaction surface). Phase 1C
  Doc 07 does not need to resolve contradictions on D-05.3 because the
  single verified pair is COMPLEMENTARY and the layer-stacking pattern
  is the textbook operational convergence on the same aim from two
  complementary regulatory channels.
- **Scope caveat (CRITICAL — controller / manufacturer layer
  divergence)** — derived from CRDA-deep verified classifications: the
  high-level SO does NOT collapse the two layers into a single
  deletion-event. The controller-side layer executes the policy through
  the manufacturer's affordance on a single product event, but the
  controller-side obligations (Art. 17(1) trigger conditions + Art.
  17(2) confirmation + Art. 12 transparency + Art. 19 cascade +
  processor-side Art. 28(3)(g) mirror + Art. 5(2) accountability) are
  distinct from the manufacturer-side obligations (Annex I Part I
  (2)(m) affordance + Annex II §8(d) decommissioning instructions +
  Annex VII §2 technical documentation + Annex VII §6 test reports).
  A unified erasure pipeline may serve the technical substrate (e.g.
  a unified deletion API with multiple regulatory-compliant output
  paths), but the **policy and evidence layers must remain
  layer-segregated** for compliance demonstration. Phase 1A must
  therefore emit **two checks before applying the high-level SO** (one
  per participating regulation) to confirm that the per-reg layer,
  trigger, deletion path, evidence template, and recipient are
  documented separately; the high-level SO surfaces the common erasure
  duty but does NOT aggregate the per-reg layers.
- **Scope caveat (CRITICAL — GDPR Art. 17(3) carve-outs are NOT
  relaxed by CRA)** — derived from CRDA-deep verified classifications:
  the GDPR Art. 17(1) obligation is subject to Art. 17(3) exceptions
  (a) freedom of expression and information; (b) compliance with a
  legal obligation or task carried out in the public interest; (c)
  reasons of public interest in the area of public health; (d)
  archiving purposes in the public interest, scientific or historical
  research purposes or statistical purposes in accordance with
  Article 89(1); (e) establishment, exercise or defence of legal
  claims. The high-level SO does NOT extend the erasure duty beyond
  what Art. 17(1) requires, and the manufacturer-side CRA layer does
  NOT independently override a controller-side Art. 17(3) carve-out —
  if the controller is lawfully entitled to retain under Art. 17(3),
  the manufacturer's (2)(m) affordance does not impose an
  independent erasure mandate. Conversely, the CRA manufacturer's
  (2)(m) affordance is **not** limited by Art. 17(3) carve-outs
  because (2)(m) is a manufacturer-side architectural obligation
  addressed to the product, not a data-subject right — the user
  retains the product-side removal affordance even when the
  controller-side obligation is lawfully suspended. This is the
  layered carve-out structure: GDPR-side Art. 17(3) governs the
  controller; CRA-side (2)(m) governs the manufacturer; neither
  overrides the other.
- **Scope caveat (CRITICAL — Art. 19 cascade is in D-04.3, not
  D-05.3)** — derived from CRDA-deep verified classifications: the
  Art. 19 cascade (rectification, erasure or restriction of
  processing is cascaded to each recipient to whom the personal
  data have been disclosed, unless impossible or involving
  disproportionate effort; the data subject is informed of those
  recipients on request) is a **notification obligation** with
  its own structural place in D-04.3 (SG-GDPR-012). Although
  erasure is the typical trigger, Art. 19 is structurally a
  notification duty on the controller, not an erasure duty on
  the data. The high-level SO for D-05.3 surfaces the erasure
  itself; the Art. 19 cascade is handled by D-04.3 SG-GDPR-012
  with its own recipient map and trigger logic. The boundary
  is documented explicitly to prevent double-counting.
- **Scope caveat (CRITICAL — Art. 28(3)(g) processor-side mirror
  vs in-product deletion API)** — derived from CRDA-deep verified
  classifications: the GDPR Art. 28(3)(g) processor-side mirror
  binds the processor to delete-or-return at the contract-end
  moment and to delete existing copies unless Union/Member State
  law requires storage; the CRA Annex I Part I (2)(m) binds the
  manufacturer to provide the deletion affordance. For an
  integrated manufacturer-controller where the manufacturer's
  cloud backend is also the controller's processor, the
  processor-side Art. 28(3)(g) mirror is exercised **through**
  the manufacturer's (2)(m) affordance at the architectural
  level (the deletion of all personal data + existing copies
  is implemented by the same backend operation) but the
  regulatory obligation remains distinct — the processor-side
  Art. 28(3)(g) is a contractual obligation between
  controller and processor; the manufacturer-side (2)(m) is a
  regulatory obligation between manufacturer and product user.
  When controller, processor, and manufacturer are the same
  party, the party discharges all three with a single deletion
  pipeline but must document the three obligations separately
  for compliance demonstration.
- **Scope caveat (CRITICAL — `securely and easily` vs `without
  undue delay` — the qualitative-vs-qualitative VAG pairing)** —
  derived from CRDA-deep verified classifications: CRA Annex I
  Part I (2)(m) `securely and easily remove on a permanent
  basis` is VAG (no quantitative clock; R1 reading — both
  secure AND easy via a discoverable user-interface affordance).
  GDPR Art. 17(1) `without undue delay` is also VAG (no
  quantitative clock; Recital 59 reads "as soon as feasible",
  non-binding; EDPB practice typically monthly). The high-level
  SO does NOT specify a single clock for either obligation; the
  calibration is delegated to (a) the manufacturer-side
  affordance design (ease + speed + discoverability, calibrated
  per the product's intended purpose under Art. 13(2)) and (b)
  the controller-side service-level documented in the Art.
  17(2) acknowledgement (typically monthly, calibrated per the
  complexity and volume of the request, with possible extension
  to ≤2 months under Art. 12(3) for complex requests). The two
  clocks are **not aligned by the high-level SO** — the
  controller-side service-level governs the policy execution;
  the manufacturer-side affordance-depth governs the
  architectural support. They converge on the same operational
  aim (render the user's data inaccessible) but do not
  constrain each other's clocks.
---

## Emergent tensions (from CRDA-deep §D-05.3)

#### Emergent tensions (from CRDA-deep §D-05.3)
**0 conditional emergent tensions** — only 2 regulations participate on
D-05.3 (GDPR and CRA; NIS 2, DORA, AI Act out-of-scope per AEGIS
taxonomy §4.1), and the single verified pair is COMPLEMENTARY (CRDA
initial classification held after OJ-text analysis). The pairwise
reading captures the entire interaction surface; there is no
non-pairwise 3-way observation to surface, and no scope-disjoint or
contradictory label was applied to the verified pair. The
**layer-stacking pattern** (controller-side policy execution on Art. 17
grounded through the manufacturer-side (2)(m) affordance) is the
textbook operational convergence on the same aim from two complementary
regulatory channels: the manufacturer-side layer makes the deletion
possible at the architectural level; the controller-side layer makes
the deletion lawful at the policy-execution level. The two obligations
are distinct (different parties, different legal anchors, different
trigger conditions, different evidence templates) but converge on the
same product event when the product processes personal data and the
user is the data subject.
**No scope-disjoint pairs and no contradictory pairs on the erasure
duty itself** — the high-level SO does NOT collapse the two layers into
a single deletion event; the **layer divergence** (controller vs
manufacturer) is the **legitimately diverse dimension**: each regulator
targets a distinct layer at a distinct trigger (Art. 17(1) data-
subject-initiated vs user-initiated product removal) with a distinct
legal anchor (Art. 17(1) + Art. 17(2) + Art. 28(3)(g) + Art. 5(1)(c)/(e)
cross + Art. 19 cascade (cross) vs Annex I Part I (2)(m) + Annex II
§8(d) + Art. 13(1) + Art. 13(18)), and the operational convergence is on
a **stacked erasure architecture** (manufacturer-enabled affordance +
controller-executed policy) with explicit layer-segregated hand-offs
at the deletion-pipeline surface. The **CRDA `(2)(m) securely and
easily remove` and GDPR Art. 17(1) `without undue delay`** pairing is
the **rare-but-honest qualitative-vs-qualitative convergence** — both
are VAG (no quantitative clock); both are calibrated to the use case;
both operate on the same aim (render the user's data inaccessible).
The two clocks are not aligned by the high-level SO — the controller-
side service-level governs the policy execution (typically monthly
under EDPB practice); the manufacturer-side affordance-depth governs
the architectural support (calibrated per Art. 13(2) risk assessment).
The **Art. 17(3) carve-outs** (freedom of expression, legal obligation,
public interest, archiving, legal claims) are the rare-but-honest
**layer-segregated exception structure**: GDPR-side Art. 17(3)
governs the controller; CRA-side (2)(m) governs the manufacturer; the
two do NOT override each other. The high-level SO surfaces the common
erasure duty; the per-reg layer, trigger, deletion path, evidence
template, recipient, and legal anchor are documented separately in the
2 sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-05.3 — with
overlapping layer scope-determiners on the same party (e.g. a GDPR
controller that also manufactures CRA-classified products that
process personal data, with both the controller's Art. 17 policy
execution and the manufacturer's (2)(m) affordance operating on the
same product event) — operates a **stacked erasure architecture**
with explicit layer-segregated hand-offs. The high-level SO
(`SG-D-05.3.HL`) describes the common erasure duty (render the
user's data inaccessible on the user's election via either of the
two stacked mechanisms — the manufacturer-side affordance and/or
the controller-side policy execution; deliver the cryptographic-
erasure deletion path per `SR-GDPR-030` where applicable; cascade
to recipients per Art. 19 (cross to `SG-GDPR-012` / D-04.3) where
applicable; deliver the documentary evidence to the relevant
supervisory / market-surveillance authority); the per-reg
perspective is preserved in the 2 sub-SOs (layer, trigger,
deletion path, evidence template, recipient, legal anchor).
**No conflict-resolution is required on D-05.3 because CRDA-deep
verified the single pair as SAME — COMPLEMENTARY and the layer-
stacking pattern is the textbook operational convergence on the
same aim from two complementary regulatory channels.** Phase 1C
Doc 07 documents the **stacked erasure strategy**: (1) a stacked
erasure architecture with explicit layer hand-offs at the
deletion-pipeline surface (manufacturer-enabled affordance ↔
controller-executed policy); (2) the **GDPR Art. 17(1) `without
undue delay` as the controller-side service-level anchor** —
operationalised via the controller's documented service-level in
the Art. 17(2) acknowledgement (typically monthly per EDPB
practice; ≤2 months under Art. 12(3) for complex requests); (3) the
**CRA Annex I Part I (2)(m) `securely and easily remove on a
permanent basis` as the manufacturer-side affordance anchor** —
both secure AND easy via a discoverable user-interface affordance
(R1 reading; cryptographic-erase / secure-overwrite / physical-
media-destruction R3 reading on `permanent basis`); (4) the
**GDPR Art. 28(3)(g) processor-side mirror** as the contract-end
deletion-or-return obligation with deletion of existing copies
unless Union/Member State law requires storage (SR-GDPR-031 —
backup copies are in scope unless separately protected; audit logs
are out of scope to the extent needed for legal-accountability
purposes); (5) the **GDPR Art. 17(3) carve-outs** as the
controller-side exception architecture (freedom of expression,
legal obligation, public-interest public-health, archiving per
Art. 89(1), establishment-exercise-defence of legal claims);
(6) the **CRA Annex II §8(d) decommissioning instructions** as
the user-facing information deliverable; (7) the **CRA Annex VII
§2 + §6 technical documentation** as the manufacturer-side evidence
pack; (8) the **Art. 19 cascade** explicitly handled in D-04.3
SG-GDPR-012 (notification, not erasure); (9) the **polysemy of
`deletes` in Art. 28(3)(g)** resolved to the cryptographic-erasure
reading per SR-GDPR-030 (destruction of cryptographic key, with
the key held outside the data substrate, scales across backups
and replicas); (10) the **layer-segregated evidence** — controller-
side and manufacturer-side policy and evidence layers must remain
layer-segregated even when a unified deletion pipeline exists at
the architectural level, because the regulatory obligations
remain distinct and the compliance-demonstration trails diverge.
For proportionality (P2), a 5-FTE SaaS with GDPR-only
applicability may default to the GDPR Art. 17(1) policy execution
through whatever deletion API the controller's own infrastructure
exposes, with the cryptographic-erasure reading as the
operationalised baseline (CRA is out of scope unless the SaaS
manufactures CRA-classified products processing personal data); a
mid-size manufacturer of CRA-classified products processing
personal data must additionally document the Annex I Part I (2)(m)
affordance + Annex II §8(d) decommissioning instructions + Annex
VII §2 + §6 technical documentation, with the GDPR Art. 17 path
executed through the manufacturer's (2)(m) affordance and the
Art. 5(2) controller-side accountability evidence discharged via
the Annex VII technical documentation.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-05.3 Right to Erasure — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.3.md`. See that file for CRDA-deep verified relationships (1 pair: 1 SAME — COMPLEMENTARY — GDPR ↔ CRA = layer-stacking pattern; no SCOPE-DISJOINT, no CONTRADICTORY, no CORRECTED classifications on the erasure duty), scope overlap matrix (Y when CRA-classified product processes personal data AND the user is the data subject AND the request is exercised through the product-side affordance AND the request reaches the controller-side policy execution), sub-domain scope structure (controller-side vs manufacturer-side layer; Art. 17(1) trigger vs user-initiated product removal; cryptographic-erasure deletion path per SR-GDPR-030 POLY-S3 → cryptographic-erasure reading; per-reg evidence template divergence; Art. 19 cascade explicitly handled in D-04.3 SG-GDPR-012 because notification is structurally distinct from erasure), and aggregation logic (2 of 5 regs participate, 1 verified pair COMPLEMENTARY, 0 emergent tensions). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA (2 of 5 regs — NIS 2, DORA, AI Act are out-of-scope per AEGIS taxonomy §4.1). CRDA-deep verified 1 pair as 1 SAME — COMPLEMENTARY (GDPR ↔ CRA = layer-stacking pattern on the personal-data subset of a CRA-classified product). The two regulators target **distinct layers** at **distinct triggers** (controller-side policy execution on Art. 17(1) request vs manufacturer-side user-facing product removal on user-initiated request), and the high-level SO surfaces the **common erasure duty** (render the user's data inaccessible on the user's election via either stacked mechanism — the manufacturer-side affordance and/or the controller-side policy execution) while preserving the per-reg layer, trigger, deletion path, evidence template, recipient, and legal anchor — the two layers are stacked, not collapsed.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 5.3
  volere_section: 15
  volere_subtype: privacy
  title: "User's data is rendered inaccessible on the user's election via the stacked controller-side (GDPR Art. 17) + manufacturer-side (CRA (2)(m)) erasure architecture, with layer-segregated hand-offs"
  derives_from:
    hso_sub_so: SG-D-05.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.3.md
    objective_ref_section: "### D-05.3.0"
  description: |
    The product shall render the user's personal data inaccessible to the controller on the data subject's election via the GDPR Art. 17(1) data-subject right and/or to the manufacturer on the user's election via the CRA Annex I Part I (2)(m) user-facing removal affordance, with explicit layer-segregated hand-offs between the controller-side policy execution (GDPR) and the manufacturer-side product affordance (CRA) when both obligations stack on the same party in the personal-data subset of a CRA-classified product.
  fit_criterion: |
    A stacked erasure architecture is operated with explicit layer-segregated hand-offs at the deletion-pipeline surface; the controller-side Art. 17(1) trigger (6 grounds (a)–(f)) is honoured through the manufacturer's (2)(m) affordance when the data resides in a CRA-classified product; cryptographic key destruction (PR.DS-10 in-use key-custody substrate) renders the data inaccessible across backups and replicas (ID.AM-08 lifecycle management) per the SR-GDPR-030 cryptographic-erasure reading; the Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving per Art. 89(1), establishment-exercise-defence of legal claims) do NOT relax the manufacturer's (2)(m) architectural obligation — the user retains the product-side removal affordance even when the controller-side obligation is lawfully suspended; the Art. 19 cascade to downstream recipients (handled in D-04.3 SG-GDPR-012 because notification is structurally distinct from erasure) is not duplicated here; the controller-side "without undue delay" service-level (Art. 12(3) ≤1 month, ≤2 months for complex requests, calibration per Art. 17(2) acknowledgement) and the manufacturer-side "securely and easily" affordance-depth (calibrated per Art. 13(2) risk assessment) are NOT aligned — the two clocks govern different layers; verified by joint controller/manufacturer erasure pipeline audit + Art. 17(2) confirmation-of-action review + cryptographic-key-custody review + Annex II §8(d) decommissioning instructions review + Annex VII §2/§6 technical-documentation inspection + Art. 28(3)(g) processor-side mirror contract-end record (when processor involved) + DPA / MSA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-10, ID.AM-08, GV.SC-04]
  applicable_if:
    regs: [GDPR, CRA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping erasure layers on the same party AND ≥1 sub-SO activates (Y when CRA-classified product processes personal data AND user is the data subject AND request is exercised through product-side affordance AND reaches controller-side policy execution); see HSO scope-overlap principle
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Two participating regulations (GDPR, CRA) stack on the same party in the personal-data subset: GDPR Art. 17(1) data-subject right (controller-bound, 6 grounds (a)–(f)) with Art. 17(2) confirmation + Art. 12 transparency + Art. 19 cascade (cross to D-04.3 SG-GDPR-012) + Art. 28(3)(g) processor-side mirror; CRA Annex I Part I (2)(m) first-limb terminal deletion + second-limb secure cross-product transfer (manufacturer-bound). CRDA-deep verified GDPR ↔ CRA = COMPLEMENTARY (SAME — layer-stacking pattern on the personal-data subset; CRDA initial classification held after OJ-text analysis). The deletion path converges on cryptographic-erasure or secure-overwrite (both compatible with SR-GDPR-030 cryptographic-erasure reading + SR-CRA-048 POLY-VAG-S2 R3 reading); the evidence templates diverge (controller-side Art. 5(2) accountability + Art. 30 RoPA + Art. 17(2) confirmation + Art. 19 cascade vs manufacturer-side Annex VII §2 technical documentation + Annex II §8(d) decommissioning instructions + Annex VII §6 test reports). Art. 17(1) "without undue delay" and CRA "securely and easily" are both VAG (no quantitative clock) — the controller-side service-level governs policy execution (typically monthly under EDPB practice, ≤2 months under Art. 12(3) for complex requests); the manufacturer-side affordance-depth governs architectural support (calibrated per Art. 13(2) risk assessment); the two clocks are NOT aligned by the high-level SO. The layer-segregated evidence architecture is the structural guarantee: a unified deletion pipeline may serve the technical substrate (e.g. a unified deletion API with multiple regulatory-compliant output paths) but the policy and evidence layers must remain layer-segregated for compliance demonstration. The Art. 17(3) carve-outs are the layer-segregated exception structure: GDPR-side Art. 17(3) governs the controller; CRA-side (2)(m) governs the manufacturer; neither overrides the other. (Copied from the HSO Considerations block of `### D... (line truncated to 2000 chars)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-05.3
title: D-05.3 Right to Erasure — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.3 Right to Erasure
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---
> **Deep analysis:** [D-05.3 Right to Erasure](../../DeepAnalysis/D-05_Data-Lifecycle/D-05.3.md)
#### D-05.3 Right to Erasure
<!-- participants: GDPR, CRA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-018, SG-GDPR-019 | Personal data erased without undue delay on Art. 17(1) grounds + processor deletion/return on contract end (Art. 28(3)(g)) | Personal data; data-subject right + processor obligation |
| NIS2 | — | Out-of-scope (sole authority: GDPR) | n/a |
| CRA | SG-CRA-036 | User-initiated secure + permanent removal of all product data and settings; secure transfer to other products/systems (Annex I Part I (2)(m)) | Product data; user right |
| DORA | — | Out-of-scope (sole authority: GDPR) | n/a |
| AI_Act | — | Out-of-scope (sole authority: GDPR) | n/a |
**Sole-authority note:** NIS2, DORA, and AI Act are out-of-scope for D-05.3 per AEGIS taxonomy §4.1. GDPR Art. 17 is the dedicated authority for personal-data erasure. CRA Annex I Part I (2)(m) addresses product-data removal which may include personal data but is not framed as a data-subject right.
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
None. Only 2 regulations participate; no 3-way interaction surface.
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **PR.DS-10** (Data-in-use protected) and **ID.AM-08** (Data disposal managed). Both GDPR (SR-GDPR-030) and CRA (SR-CRA-048) map to ID.AM-08. The cryptographic-key-destruction path (GDPR SR-GDPR-030) maps to PR.DS-10. The CSF 2.0 surface is consistent and tight.
##### Downstream implication
Phase 2 obligation derivation is straightforward: two participants, complementary. The product must support the data-subject right by design (CRA Annex I Part I (2)(m) is the design-level hook; GDPR Art. 17 is the rights-level hook). Phase 3 case generation must verify that CRA-compliant products in case companies expose a deletion API aligned with GDPR Art. 17 obligations.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-05.3
title: D-05.3 Right to Erasure — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.3 Right to Erasure
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md
status: DRAFT
---
> **Domain analysis:** [D-05.3 Right to Erasure](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.3.md)
#### D-05.3 Right to Erasure
<!-- participants: GDPR, CRA -->
**Participants (from CRDA):** GDPR, CRA
**Sole-authority note:** NIS2, DORA, and AI Act are out-of-scope for D-05.3 per AEGIS taxonomy §4.1. GDPR Art. 17 is the dedicated authority for personal-data erasure. CRA Annex I Part I (2)(m) addresses product-data removal which may include personal data but is not framed as a data-subject right.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
