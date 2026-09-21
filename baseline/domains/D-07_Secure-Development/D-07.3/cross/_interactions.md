# D-07.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-07.3 CI/CD Pipeline Security](../../CrossRegulation/DomainAnalysis/D-07_Secure-Development/D-07.3.md)
#### D-07.3 CI/CD Pipeline Security
<!-- participants: NIS2, CRA -->
**Participants (from CRDA):** NIS2, CRA
**Sole-authority note:** AEGIS taxonomy §4.1 marks NIS 2 as sole authority for D-07.3 CI/CD Pipeline Security (T3-vs-text gap: OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`). NIS 2 provides only partial coverage via the maintenance dimension. CRA Annex I Part II (7)+(8) covers update distribution (delivery path), not CI/CD build-time controls.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-07.3 CI/CD Pipeline Security
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md`](../../CrossRegulation/DeepAnalysis/D-07_Secure-Development/D-07.3.md)
> (1 pair verified against OJ text — **2 participating regulations
> are NIS 2 and CRA; GDPR, DORA, and AI Act are explicitly
> out-of-scope** as noted by `DomainAnalysis/D-07_Secure-Development/D-07.3.md`
> line 27: "Participants (from CRDA): NIS2, CRA"; and the
> DomainAnalysis out-of-scope notes lines 31-35: "GDPR is not
> domain-specific ... DORA does not impose CI/CD mandate ... AI Act
> does not impose CI/CD mandate. SR-AIACT-023 (Art. 55(1)(a) GPAI
> evaluation with adversarial testing) has testing-and-validation
> dimensions but not CI/CD build-time controls").
>
> **Sole-authority note (per CRDA-deep §D-07.3):** AEGIS taxonomy §4.1
> marks NIS 2 as sole authority for D-07.3 CI/CD Pipeline Security
> (T3-vs-text gap: OJ Art. 21(2)(e) does not mention `pipeline`,
> `CI`, or `CD`). NIS 2 provides only partial coverage via the
> **maintenance** dimension. CRA Annex I Part II (7)+(8) covers
> update distribution (delivery path), **not** CI/CD build-time
> controls.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-07.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR is not domain-specific on CI/CD pipelines; it does not specify build-time controls, signed artefacts, or build-agent integrity. | — |
| NIS2 | SO-NIS2-017 (partial via maintenance dimension — SO-NIS2-017 routes via Art. 21(2)(e) third clause) | Security in maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) third clause) — partial coverage of CI/CD via the maintenance dimension. T3-vs-text gap per `04_NIS2.md` line 29: OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`. | **Entity-level partial coverage** via the maintenance dimension; AEGIS taxonomy §4.1 marks NIS 2 as sole authority. The partial coverage is realised through the maintenance phase of the 3-phase coordinated lifecycle (acquisition/development/maintenance — `SR-NIS2-028` on the basis of Art. 21(2)(e) third clause); the CI/CD build-time control surface (signed artefacts, build-agent integrity, ephemeral build environments) is **industry best-practice, not regulatory mandate**. |
| CRA | (no OJ-mandated D-07.3 SO; partial via SO-CRA-009 cross-ref to Annex I Part II (7)+(8)) | Annex I Part II (7) `securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates` + Annex I Part II (8) `ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take` — **delivery path only**, **not** CI/CD build-time controls (signed artefacts, build-agent integrity). | **Product-level delivery path** at the manufacturer side — the maker-side update distribution obligation that meets the user-side (NIS 2) maintenance dimension at the supplier-customer boundary. AEGIS taxonomy §4.1 marks NIS 2 as sole authority; CRA participation is preserved as partial-coverage cross-ref only. |
| DORA | (out-of-scope) | DORA does not impose CI/CD mandate. | — |
| AI_Act | (out-of-scope) | AI Act does not impose CI/CD mandate. SR-AIACT-023 (Art. 55(1)(a) GPAI evaluation with adversarial testing) has testing-and-validation dimensions but **not** CI/CD build-time controls. | — |

## Validated relationships (from CRDA-deep §D-07.3)

#### Validated relationships (from CRDA-deep §D-07.3)
Of 1 pair, **1 verified as SAME — COMPLEMENTARY with substantial scope-disjoint qualifier on the typical case**: no CORRECTED, no CONTRADICTORY **BUT with substantial scope-disjoint structure in baseline**. The two regulators look at CI/CD pipeline security from two distinct partial-coverage regulatory perspectives that **DO NOT stack on the same event in baseline**:
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME) (CRDA classification preserved; **but with substantively scope-disjoint qualifier per OJ-literal reading**): NIS 2 Art. 21(2)(e) third clause covers **security in the maintenance of network and information systems, including vulnerability handling and disclosure** — the entity-side deployment-and-maintenance dimension that encompasses delivery-path controls via the maintenance phase. CRA Annex I Part II (7)+(8) covers **product-side secure-update distribution** — the manufacturer-side obligation to securely distribute + disseminate security updates. The two regimes meet at the supplier-customer interface: NIS 2 procurement gate (`SR-NIS2-026` on the basis of Art. 21(3) sentence 1 supplier-secure-development-procedures three-prong) references CRA-conformant products, and CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway. The **scope-disjoint test** (does this pair actually overlap on a single event at a single party?): **N (typically)** — different objects (entity-side CI/CD pipeline / NIS-deployment-pipeline vs product-side update delivery path), different actors (essential/important entity deploying NIS vs manufacturer distributing security updates). Pair is substantively scope-disjoint; CRDA "complementary" is more a taxonomy artifact than a substantive relationship, with engagement only on the Atypical Conditional-Y integrated stack when an NIS 2 essential/important entity procures a CRA-regulated product (the supplier-customer boundary). **No OJ mandate exists in any of the 5 regulations for CI/CD build-time controls** (signed artefacts, build-agent integrity, ephemeral build environments) — Phase 1 entities must construct the CI/CD pipeline-security baseline from industry frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA) and demonstrate compliance against NIS 2's partial-coverage maintenance dimension and CRA's partial-coverage update-distribution pathway.
The CI/CD-pipeline-security architecture is **legitimately diverse with substantial scope-disjoint structure on the typical case** — each regulator targets a **distinct target object** (entity-side deployment-and-maintenance pipeline [NIS 2 Art. 21(2)(e) third clause — partial coverage via maintenance dimension, AEGIS-taxonomy sole-authority assignment with T3-vs-text gap] / product-side update delivery path [CRA Annex I Part II (7) + (8)]) at a **distinct trigger** (essential/important entity NIS deployment activity [Art. 21(2)(e) third clause trigger] / manufacturer places product on market [Annex I Part I chapeau] + distributes updates during the support period [Annex I Part II (7)+(8) trigger]) with a **distinct obligation anchor** (NIS 2 `security in … maintenance of network and information systems, including vulnerability handling and disclosure` — entity-side partial-coverage of the CI/CD delivery-path dimension via the maintenance phase + `appropriate and proportionate` chapeau [Art. 21(1)] + `state of the art` [Art. 21(1) sentence 2]; CRA `securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates` + `without delay` / `free of charge` / `clearly described` / `information on the security improvements` [Annex I Part II (7)+(8)] + 5-year support-period floor [Art. 13(8) sentence 3]). The high-level SO surfaces the **common CI/CD-pipeline-security duty** (build-time control baseline + update-distribution delivery-path security) typically built from industry frameworks NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA, while preserving the per-reg target object and acknowledging the **substantial scope-disjoint structure on the typical case** — the high-level SO **engages only on the Conditional-Y integrated stack** (when an NIS 2 essential/important entity procures a CRA-regulated product — the supplier-customer boundary).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | NIS2 | CRA |
|---|---|---|
| **NIS2** | — | Conditional Y (when an NIS 2 essential/important entity procures a CRA-regulated product — the supplier-customer boundary where the NIS 2 procurement gate (`SR-NIS2-026`) references CRA-conformant products). N (typically) — different objects (entity-side CI/CD pipeline / deployment-and-maintenance dimension vs product-side update delivery path), different actors, different supply-chain levels. |
| **CRA** | Conditional Y (same; reciprocal — when an NIS 2 essential/important entity deploys a CRA-conformant product on which CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway). N (typically) — same as above (reciprocal). | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional Y** = scope overlap only under specific circumstances (NIS 2 entity procures a CRA-conformant product — supplier-customer boundary). **N (typically)** = scope-disjoint in baseline (distinct actors, distinct objects, distinct supply-chain levels). CRDA-deep scope-disjoint tests: **NIS2↔CRA = N (typically)** (substantive scope-disjoint because distinct actors handle distinct objects — entity-side deployment-and-maintenance pipeline vs product-side update delivery path). **The high-level SO engages only on the Conditional-Y integrated stack** for NIS 2 entity procuring a CRA-conformant product — atypical integrated stacks where an essential/important entity is also procuring CRA-classified products; for typical integrated stacks the high-level SO does NOT engage.

## Cross-recipient map

#### Cross-recipient map
D-07.3 generates partial recipient fragmentation at the **CI/CD-pipeline evidence layer** but does **not generate a notification cascade of D-07.3 itself** (the CI/CD pipeline security is the upstream operational instrument that bridges the by-design decision at D-07.1 and the secure-coding practices at D-07.2 on the entity-side, or the by-design + secure-coding at the product-side on the manufacturer-side). The recipient set is at the **CI/CD-pipeline-evidence layer**: **NIS 2's management body + competent authority** on the Art. 21(2)(e) third-clause maintenance-dimension evidence (the NIS 2 entity-side partial-coverage of CI/CD via maintenance — patch-management policies + vulnerability-handling-and-disclosure records + Art. 20(1) management-body approval of the Art. 21 measures); **CRA's market surveillance authority (MSA)** on the Annex I Part II (7)+(8) update-distribution evidence + Annex VII §2 design/development documentation (covering the secure-update-distribution mechanism as a portion of the Annex VII §2 design/development documentation set) — the manufacturer-side partial-coverage of CI/CD via the update-delivery path; the **NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA industry frameworks** are the source of the **CI/CD build-time control baseline** (signed artefacts, build-agent integrity, ephemeral build environments) on the typical-case integrated stack where neither NIS 2 nor CRA provides an OJ mandate — Phase 1 entities demonstrate CI/CD pipeline security through industry-framework adoption + per-reg partial-coverage evidence. **D-07.1 (Secure-by-Design Principles) and D-07.2 (Secure Coding Practices) are the operational downstream artefacts** where D-07.3's CI/CD pipeline security becomes a code-level instruction; D-07.4 (Change Management) is the operational hand-off where D-07.3's CI/CD build output transitions to deployment via the change-mgmt six-step (DORA) or the series-of-production conformity procedure (CRA).
---

## HSO considerations (from D-07.3.0 — High-level SecurityObjective)

**Considerations.**
- 2 of 5 regulations participate (NIS 2, CRA); GDPR, DORA, and AI Act are explicitly out-of-scope (none of GDPR / DORA / AI Act OJ text specifies CI/CD build-time controls or CI/CD pipeline-security controls as such).
- Build-time controls are typically built from industry frameworks (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA) since no OJ clause prescribes CI/CD build-time controls.
- NIS 2 `security in … maintenance of network and information systems, including vulnerability handling and disclosure` (Art. 21(2)(e) third clause) — entity-side partial-coverage of CI/CD via the maintenance dimension (T3-vs-text gap: OJ does not mention `pipeline`, `CI`, or `CD` — the partial coverage is realised through the 3-phase coordinated lifecycle via the maintenance phase; AEGIS taxonomy §4.1 marks NIS 2 as sole authority with the T3-vs-text caveat).
- CRA `securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates` (Annex I Part II (7)) + dissemination free of charge + clearly described + security improvement information + user-actionable guidance (Annex I Part II (8) verbatim) — product-side update-delivery-path partial-coverage (`without delay` qualitative; 5-year support-period floor from Art. 13(8) sentence 3; 10-year update-availability tail from Art. 13(9)).
- 1 pairwise cell verified by CRDA-deep as SAME — COMPLEMENTARY with substantial scope-disjoint qualifier on the typical case — the two regimes target distinct objects at distinct actors (entity-side CI/CD pipeline vs product-side update delivery path; NSIE deploying NIS vs manufacturer distributing security updates).
- The high-level SO engages only on the Conditional-Y integrated stack (when an NIS 2 essential/important entity procures a CRA-regulated product — the supplier-customer boundary where the NIS 2 procurement gate references CRA-conformant products and CRA Part II (7)/(8) update-distribution obligations discharge the NIS 2 supplier-side patch pathway); on the typical-case N scope-disjoint baseline, the high-level SO does NOT engage.
- CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments) are industry best-practice, not regulatory mandate — Phase 1 entities must construct the CI/CD baseline from industry frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA) and demonstrate compliance against NIS 2's partial-coverage maintenance dimension and CRA's partial-coverage update-distribution pathway.
- For a 5-FTE SaaS startup with NIS 2 applicability only (no CRA applicability), the high-level SO is NOT activated. For a CRA-regulated manufacturer that is not an NIS 2 entity, the high-level SO is NOT activated either.
- The per-reg perspective (target object, trigger, anchor, threshold, evidence template, recipient, legal anchor) is preserved verbatim in the two sub-SOs with the substantial scope-disjoint structure on the typical case.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 2 participating regulations each define D-07.3 over a distinct **target object** of the CI/CD-pipeline architecture; the target object, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the CI/CD pipeline.
| Axis (reg) | Target object | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **NIS2** | entity-side deployment-and-maintenance pipeline (partial coverage of CI/CD via maintenance dimension; AEGIS taxonomy §4.1 sole-authority assignment with T3-vs-text gap — OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`) | essential/important entity NIS deployment activity (Art. 21(2)(e) third clause trigger) | `appropriate and proportionate` (Art. 21(1) chapeau) + `state of the art` (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative cadence; no quantitative CI/CD-pipeline controls (T3-vs-text gap) | management body (Art. 20(1) approve + oversee + liability) + competent authority on the Art. 21 measures + the Art. 23 significant-incident reporting flow when a CI/CD pipeline compromise leads to a significant incident | Art. 21(2)(e) third clause + Art. 21(1) chapeau + sentence 2 + Art. 20(1) management-body approval |
| **CRA** | product-side update delivery path (manufacturer securely distributes + disseminates updates free of charge + with advisory messages describing user-actionable security improvements) | manufacturer places product on market (Annex I Part I chapeau) + ongoing during support period per Art. 13(8) (5-year floor + 10-year update-availability tail per Art. 13(9)) | `without delay` (Annex I Part II (8)) — qualitative, no quantitative cadence; 5-year support-period floor (Art. 13(8) sentence 3); 10-year update-availability tail (Art. 13(9)); free-of-charge + clearly-described + information on security-improvements + actions-the-user-should-take (Annex I Part II (8)) | market surveillance authority (MSA) — Annex VII §2 design/development documentation (covering the secure-update-distribution mechanism) + Annex I Part II (7)+(8) update-distribution evidence + the user/customer as direct recipient of the update + the Article 14 actively-exploited-vulnerability / severe-incident flow when an update-distribution compromise is material | Annex I Part II (7) + Annex I Part II (8) + Art. 13(8) sentence 3 (support-period floor) + Art. 13(9) (10-year update-availability tail) + Annex VII §2 |

## Scope-overlap matrix (2×2)

#### Scope-overlap matrix (2×2)
(See the validated-relationships table above for the 2×2 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-07.3.HL`) engages on a given party **only if ≥2 applicable
regulations have a Y or Conditional Y scope overlap on the same party**
on the same CI/CD-pipeline event. **In the typical case, the only 1 pair
(NIS2↔CRA) returns N (typically)** — substantively scope-disjoint
because distinct actors (essential/important entity vs manufacturer)
handle distinct objects (entity-side deployment-and-maintenance pipeline
vs product-side update delivery path) at distinct supply-chain levels
(downstream vs upstream). The pair becomes Y only on the **Conditional-Y
integrated stack** (when an NIS 2 essential/important entity procures a
CRA-conformant product — the supplier-customer boundary): the
NIS 2 entity-side procurement gate (`SR-NIS2-026` on the basis of
Art. 21(3) sentence 1 supplier-secure-development-procedures
three-prong) references CRA-conformant products, and the CRA Part II
(7)/(8) update-distribution obligations discharge the NIS 2
supplier-side patch pathway. For an essential/important entity that
deploys a CRA-conformant product, the **CRA-side Annex I Part II
(7)+(8) update-delivery-path partial-coverage** feeds the **NIS 2-side
maintenance-dimension partial-coverage** at the entity side — but the
pair is **substantively scope-disjoint in baseline** (distinct actors,
distinct objects, distinct supply-chain levels) and becomes Y only on
atypical integrated stacks. **The two target objects are NOT layered
on the typical-case integrated stack** — the per-reg CI/CD-pipeline
dimension stands on its own with the scope-disjoint structure preserved;
the high-level SO does **NOT** collapse the two target objects into a
single CI/CD-pipeline architecture. The per-reg perspective on target
object, trigger, anchor, threshold, recipient, and evidence template is
preserved verbatim. For a CRA-regulated manufacturer that is **not** an
NIS 2 essential/important entity, only the CRA sub-SO activates and the
high-level SO is **NOT activated** because there is no Conditional Y or
Y scope overlap on a single CI/CD-pipeline event. For an essential/
important entity that does **not** deploy CRA-conformant products (NIS 2
only with non-CRA-classified products), only the NIS 2 sub-SO activates
and the high-level SO is **NOT activated** either. For an essential/
important entity that deploys CRA-conformant products (the
Conditional-Y integrated stack), the high-level SO engages for the
supplier-customer boundary event (the procurement record + the
update-distribution evidence + the entity-side maintenance-dimension
patch cadence). **No OJ clause prescribes an integrated CI/CD
build-time baseline** across the two regimes — the high-level SO does
NOT collapse the two partial-coverage dimensions into a single
architecture; the per-reg perspective is preserved verbatim with the
**industry-framework (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA)
CI/CD build-time baseline** serving as the operational instrument on
the typical-case integrated stack where neither regulator provides an
OJ mandate.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **2 of 5 regulations participate** (NIS 2, CRA; **GDPR, DORA, AI Act
  are explicitly out-of-scope** — OJ Art. 25(1) does not specify
  CI/CD-pipeline controls; OJ DORA Art. 9(4)(e) is change-management
  policy; OJ DORA Art. 9(4)(f) is patches-and-updates policy; no OJ
  clause prescribes CI/CD build-time controls).
- **1 pairwise cell, verified by CRDA-deep as 1 SAME — COMPLEMENTARY
  with substantial scope-disjoint qualifier on the typical case:**
  NIS2↔CRA (SAME — COMPLEMENTARY with N (typically) qualifier + Y on
  the Conditional-Y integrated stack — entity-side maintenance
  dimension meets product-side update-delivery path at the
  supplier-customer boundary).
- The two regulations impose **distinct partial-coverage CI/CD-pipeline
  duties** at **distinct target objects** with **distinct triggers**
  and **distinct anchors**: NIS 2 entity-side deployment-and-
  maintenance pipeline (Art. 21(2)(e) third clause — `appropriate and
  proportionate` chapeau + `state of the art` floor + 3-phase
  coordinated lifecycle with partial-coverage of CI/CD via the
  maintenance phase — T3-vs-text gap; no OJ CI/CD-pipeline controls);
  CRA product-side update delivery path (Annex I Part II (7) `without
  delay` + (8) `free of charge` + `clearly described` + `information on
  the security improvements` + `actions the user should take` — 5-year
  support-period floor from Art. 13(8) sentence 3 + 10-year
  update-availability tail from Art. 13(9) — **no OJ CI/CD-pipeline
  build-time controls**). The two partial-coverage dimensions do **NOT**
  form an integrated CI/CD-pipeline baseline — Phase 1 entities must
  build the **CI/CD build-time control baseline** from industry
  frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA) and
  demonstrate compliance against each regulation's partial-coverage
  dimension independently.
- The high-level SO describes the **COMMON OBJECTIVE** (CI/CD-pipeline
  security — build-time control baseline + update-distribution
  delivery-path security); the **per-regulation perspective** (target
  object, trigger, anchor, threshold, recipient, evidence template) is
  preserved verbatim in the two sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension on the CI/CD-pipeline-security duty itself — **0
  CONTRADICTORY or CORRECTED reclassifications** because the 1 verified
  pair is SAME — COMPLEMENTARY (no CONTRADICTORY, no CORRECTED; the
  scope-disjoint qualifier is a structure-of-engagement observation,
  not a reclassification). **No Phase 1C tension resolution is
  required** for D-07.3 — Phase 1C Doc 07 documents the
  CI/CD-pipeline-security strategy without resolving a CI/CD-pipeline
  contradiction because none exists by construction. **The T3-vs-text
  gap on NIS 2 Art. 21(2)(e)** is a structural Layer 2 review item —
  preserved as a T3-vs-OJ gap and surfaced as a NIS 2-side T3-import
  caveat (the OJ does not contain the `pipeline` / `CI` / `CD`
  vocabulary; the AEGIS-taxonomy sole-authority assignment imports the
  T3 vocabulary). **The CRA Annex I Part II (7)+(8) partial-coverage
  cross-ref** is a structural Layer 2 review item — preserved as a
  partial-coverage cross-ref with the OJ-literal delivery-path scope
  documented and surfaced as a CRA-side coverage-scope caveat (the OJ
  covers product-side update delivery path only, not CI/CD build-time
  controls).
- **Scope caveat (CRITICAL — NIS 2 T3-vs-text gap)** — derived from
  CRDA-deep verified classifications: NIS 2 Art. 21(2)(e) third clause
  text is `security in the maintenance of network and information
  systems, including vulnerability handling and disclosure` — **no OJ
  reference to `pipeline`, `CI`, or `CD`**. The T3 taxonomy imports
  CI/CD-pipeline vocabulary not in the OJ text (per
  `04_NIS2.md` line 29 / synthesis §8: T3 NIS2-C11 attributes
  `D-07.3 CI/CD pipelines` to the locus but the OJ text does not
  contain the vocabulary). AEGIS taxonomy §4.1 marks NIS 2 as the SOLE
  AUTHORITY for D-07.3 — this assignment imports the T3 vocabulary and
  has a T3-vs-text gap. **The NIS 2-side participation at D-07.3 is
  preserved as partial-coverage** via the maintenance dimension (the
  3-phase coordinated lifecycle of Art. 21(2)(e) — acquisition + 
  development + maintenance — with partial CI/CD coverage via the
  maintenance phase + vulnerability handling and disclosure); the
  CRDA-deep coverage is `NIS 2 is not the dedicated authority; the
  partial coverage is via the maintenance dimension`. Layer 2 review
  item: either (a) the AEGIS taxonomy §4.1 should be clarified to
  note that NIS 2 is the entity-side partial-coverage authority with
  T3-vs-text gap, or (b) the T3 taxonomy should be revised to remove
  the CI/CD-pipeline attribution from NIS 2 Art. 21(2)(e). For a 5-FTE
  NIS 2 entity, the CI/CD-pipeline dimension is demonstrated through
  the entity-side maintenance-dimension partial-coverage + the
  industry-framework CI/CD build-time baseline — not through an
  OJ-mandated CI/CD-pipeline control set.
- **Scope caveat (CRITICAL — CRA Annex I Part II (7)+(8) coverage
  scope)** — derived from CRDA-deep verified classifications: CRA
  Annex I Part II (7) text is `securely distribute updates for the
  product with digital elements in a timely manner, including, where
  appropriate, through automatic updates` + (8) text is `ensure that
  updates are disseminated free of charge, are clearly described,
  contain information on the security improvements and on the actions
  the user should take` — **product-side update delivery path only,
  not CI/CD build-time controls**. The CRA-side participation at
  D-07.3 is preserved as partial-coverage cross-ref via SO-CRA-009
  (Annex I Part II (7) — secure update distribution). The OJ does not
  prescribe signed artefacts, build-agent integrity, or ephemeral
  build environments. **For a CRA-regulated manufacturer, the
  CI/CD-pipeline dimension is demonstrated through the Annex I Part II
  (7)+(8) update-delivery-path evidence + the industry-framework
  CI/CD build-time baseline** — not through an OJ-mandated CI/CD
  build-time control prescription.
- **Scope caveat (CRITICAL — no OJ-level CI/CD-pipeline control
  prescription across the two regimes)** — derived from CRDA-deep
  verified classifications: the two regimes cover distinct partial-
  coverage dimensions (NIS 2 entity-side maintenance + CRA product-side
  update delivery path) — **no OJ clause prescribes an integrated
  CI/CD-pipeline control baseline** (no CI/CD build-time control
  prescription; no signed-artefact mandate; no build-agent-integrity
  mandate; no ephemeral-build-environment mandate). Unlike the CRA
  Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk
  assessment (when both apply on AI-enabled CRA products), no OJ
  clause permits a unified CI/CD-pipeline baseline across the two
  regimes. **Phase 1 entities must construct the CI/CD-pipeline
  baseline from industry frameworks** (NIST SP 800-204, OWASP CI/CD
  Top 10, SLSA) and demonstrate compliance against each regulation's
  partial-coverage dimension independently. The entity-side
  procurement record (NIS 2 `SR-NIS2-026` supplier-secure-development-
  procedures three-prong) + the product-side Annex VII §2 design/
  development documentation (CRA) + the industry-framework CI/CD
  build-time baseline together constitute the integrated
  CI/CD-pipeline-security evidence base on the Conditional-Y
  integrated stack; on the typical-case N scope-disjoint baseline,
  each regulator's partial-coverage dimension is implemented
  independently.
---

## Emergent tensions (from CRDA-deep §D-07.3)

#### Emergent tensions (from CRDA-deep §D-07.3)
**0 conditional emergent tensions** on the CI/CD-pipeline-security duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 1 verified pair (NIS2↔CRA) is SAME — COMPLEMENTARY with substantial scope-disjoint qualifier on the typical case, and the two regulators look at CI/CD pipeline security from two distinct partial-coverage regulatory perspectives that are **substantively scope-disjoint in baseline**. **No SCOPE-DISJOINT in CRDA-classification sense** (the 2×2 matrix returns N (typically) on the typical case + Conditional Y on the integrated stack) — the scope-disjointness is in the OJ-literal sense (distinct objects, distinct actors, distinct supply-chain levels) rather than a CONTRADICTORY / CORRECTED reclassification. **No CONTRADICTORY pairs** on the CI/CD-pipeline-security duty itself. The **target-object divergence** (entity-side deployment-and-maintenance pipeline partial-coverage [NIS 2 Art. 21(2)(e) third clause with T3-vs-text gap] / product-side update delivery path [CRA Annex I Part II (7)+(8) verbatim]) is the **legitimately diverse dimension**: each regulator targets a distinct target object at a distinct trigger (essential/important entity NIS deployment activity / manufacturer places product on market + distributes updates during the support period), and the operational convergence is on a **2-layer CI/CD-pipeline-security architecture** — (a) the entity-side partial-coverage via the maintenance dimension + (b) the product-side update-delivery-path partial-coverage — with industry-framework build-time baseline (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA) as the operational instrument on the typical-case integrated stack where neither regulator provides an OJ CI/CD build-time mandate.
The **NIS 2 T3-vs-text gap** is the structurally significant divergence: NIS 2 Art. 21(2)(e) third clause is `security in the maintenance of network and information systems, including vulnerability handling and disclosure` — no OJ reference to `pipeline`, `CI`, or `CD`. The T3 taxonomy imports the CI/CD-pipeline vocabulary (per `04_NIS2.md` line 29 / synthesis §8: T3 NIS2-C11 attributes `D-07.3 CI/CD pipelines` to the locus but the OJ text does not contain the vocabulary). AEGIS taxonomy §4.1 marks NIS 2 as the SOLE AUTHORITY for D-07.3 — this assignment imports the T3 vocabulary and has a T3-vs-text gap. The NIS 2-side participation at D-07.3 is preserved as partial-coverage via the maintenance dimension (SR-NIS2-028 on the basis of Art. 21(2)(e) third clause). This is a **structural Layer 2 review item** (not a CONTRADICTORY or CORRECTED reclassification) — the T3-vs-text gap is documented as a Taxonomy-vs-OJ gap.
The **CRA Annex I Part II (7)+(8) coverage scope** is the structurally significant divergence on the CRA side: CRA Annex I Part II (7)+(8) covers **product-side update delivery path only**, not CI/CD build-time controls. The CRA-side participation at D-07.3 is preserved as partial-coverage cross-ref via SO-CRA-009 (D-02.2 patch management primary with cross-ref to D-07.3 partial). The OJ literal text is silent on CI/CD build-time controls (signed artefacts, build-agent integrity, ephemeral build environments) — the industry-framework build-time baseline (NIST SP 800-204 / OWASP CI/CD Top 10 / SLSA) is the operational instrument on the typical-case integrated stack. This is a **structural Layer 2 review item** (not a CONTRADICTORY or CORRECTED reclassification) — the partial-coverage scope is documented as an OJ-coverage-scope caveat.
The high-level SO surfaces the common CI/CD-pipeline-security duty (build-time control baseline + update-distribution delivery-path security); the per-reg target object, trigger, anchor, threshold, recipient, and evidence template are documented separately in the two sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 2-layer CI/CD-pipeline-security architecture (NIS 2 entity-side partial-coverage via maintenance dimension [T3-vs-text gap] → CRA product-side update-delivery-path partial-coverage via Annex I Part II (7)+(8) [OJ-literal coverage scope]) is itself the layered reconciliation that supersedes any single-regulator reading on the Conditional-Y integrated stack; on the typical-case N scope-disjoint baseline, the two partial-coverage dimensions are implemented independently.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-07.3 — with overlapping target-object scope-determiners on the same Conditional-Y integrated stack — operates a **2-layer CI/CD-pipeline-security architecture** with explicit layered hand-offs and **industry-framework build-time baseline** as the operational instrument. The high-level SO (`SO-D-07.3.HL`) describes the common CI/CD-pipeline-security duty (build-time control baseline + update-distribution delivery-path security — typically built from industry frameworks NIST SP 800-204 + OWASP CI/CD Top 10 + SLSA since no OJ clause prescribes CI/CD build-time controls); the per-reg perspective is preserved in the two sub-SOs (target object, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 2-layer CI/CD-pipeline-security architecture (NIS 2 entity-side partial-coverage via maintenance dimension [Art. 21(2)(e) third clause + T3-vs-text gap + AEGIS-taxonomy sole-authority assignment] → CRA product-side update-delivery-path partial-coverage via Annex I Part II (7)+(8)) operationalising the inter-reg hand-off at the supplier-customer boundary of the Conditional-Y integrated stack. The high-level SO does NOT collapse the two target objects into a single CI/CD-pipeline architecture; the per-reg perspective on target object, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **CI/CD-pipeline-security strategy**: (1) a 2-layer CI/CD-pipeline-security architecture with explicit target-object hand-offs (NIS 2 Art. 21(2)(e) third clause entity-side maintenance-dimension partial-coverage with T3-vs-text gap → CRA Annex I Part II (7)+(8) product-side update-delivery-path partial-coverage) — **the entity-side NIS 2 procurement gate (`SR-NIS2-026`) + the product-side CRA Part II (7)/(8) update-distribution evidence meet at the supplier-customer boundary on the Conditional-Y integrated stack**; (2) the **NIS 2 T3-vs-text gap as a structural Layer 2 review item** (no OJ mandate for CI/CD build-time controls; `SR-NIS2-028` partial-coverage via the maintenance dimension; AEGIS taxonomy §4.1 sole-authority assignment with T3-vs-text caveat — either (a) the AEGIS taxonomy §4.1 should be clarified, or (b) the T3 taxonomy should be revised to remove the CI/CD-pipeline attribution from NIS 2 Art. 21(2)(e)); (3) the **CRA Annex I Part II (7)+(8) coverage-scope caveat as a structural Layer 2 review item** (no OJ CI/CD build-time mandate; partial-coverage cross-ref via SO-CRA-009 / `SR-CRA-009`; CRA covers product-side update delivery path only); (4) the **industry-framework CI/CD build-time baseline** (NIST SP 800-204, OWASP CI/CD Top 10, SLSA) as the operational instrument on the typical-case integrated stack where neither regulator provides an OJ CI/CD build-time mandate — the entity builds the CI/CD build-time baseline from industry frameworks and demonstrates compliance against each regulator's partial-coverage dimension independently on the typical-case N scope-disjoint baseline, or against the integrated supplier-customer-boundary evidence on the Conditional-Y integrated stack.
**End of file.**

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-07.3 CI/CD Pipeline Security — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md`. This is a thin Volere overlay: it adds requirement IDs, Volere classification, fit criteria, priority, verification method, dependencies, applicability, and satisfaction placeholders only; HSO Objective text, OJ text, NIST CSF rationale, scope-overlap analysis, and per-regulation considerations remain in the referenced source files.

## Participating regulations (§3)

### Participating regulations
NIS2 and CRA (2 of 5 regs). See the HSO provenance file for out-of-scope findings, scope-overlap gating, and the NIS2/CRA partial-coverage caveats.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 7.3
  volere_section: 15
  volere_subtype: immunity
  title: "Integrated CI/CD and secure-update delivery evidence baseline for Conditional-Y NIS2/CRA stacks"
  derives_from:
    hso_sub_so: SO-D-07.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md
    objective_ref_section: "### D-07.3.0"
  description: |
    The product shall maintain a verifiable CI/CD and secure-update-delivery evidence baseline for the Conditional-Y integrated stack where NIS2 entity-side maintenance controls and CRA product-side update-delivery controls apply to the same supplier-customer release event.
  fit_criterion: |
    For 100% of covered production releases, a release evidence pack exists before deployment or dissemination and contains immutable build provenance, artefact integrity verification, isolated build-execution evidence, vulnerability-triage linkage, release approval, update-distribution record, rollback status, and a signed exception record for any unavailable control.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.PS-02, ID.RA-01, PR.PS-06]
  applicable_if:
    regs: [NIS2, CRA]
    scope_overlap: conditional
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    See `../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.3.md` for scope-disjoint structure, Conditional-Y activation, and per-regulation target-object preservation.
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-07.3
title: D-07.3 CI/CD Pipeline Security — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.3 CI/CD Pipeline Security
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-07_Secure-Development/D-07.3.md
status: DRAFT
---
> **Deep analysis:** [D-07.3 CI/CD Pipeline Security](../../DeepAnalysis/D-07_Secure-Development/D-07.3.md)
#### D-07.3 CI/CD Pipeline Security
<!-- participants: NIS2, CRA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR is not domain-specific. | — |
| NIS2 | SO-NIS2-017 (partial via maintenance dimension) | Security in maintenance (Art. 21(2)(e) third clause) encompasses delivery-path controls. T3-vs-text gap: OJ does not mention `pipeline`, `CI`, or `CD`. | Entity-level partial coverage; NIS 2 is the dedicated authority per AEGIS taxonomy §4.1. |
| CRA | (out-of-scope as standalone) | Annex I Part II (7)+(8) covers update distribution, not CI/CD build-time controls. AEGIS taxonomy §4.1 marks NIS 2 as sole authority. | Product-level delivery path only; no build-time controls (signed artefacts, build-agent integrity). |
| DORA | (out-of-scope) | DORA does not impose CI/CD mandate. | — |
| AI_Act | (out-of-scope) | AI Act does not impose CI/CD mandate. SR-AIACT-023 (Art. 55(1)(a) GPAI evaluation with adversarial testing) has testing-and-validation dimensions but not CI/CD build-time controls. | — |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (2 regulations)
- Only 2 regulations have non-zero coverage. No 3-regulation emergent tension exists.
##### SR cross-validation
Both applicable regulations map D-07.3 to **PR.PS-06** (Secure software development practices integrated) for the SDLC-discipline anchor, with CRA additionally anchoring on **PR.PS-02** (Software maintained/replaced commensurate with risk) for the update-distribution lifecycle. The Subcategory mapping reflects the limited OJ-text support — the coverage is at the process-discipline layer, not the pipeline-architecture layer.
##### Downstream implication
The CI/CD pipeline security sub-domain has no dedicated OJ mandate in any of the 5 regulations. Phase 1 entities must construct the CI/CD baseline from industry frameworks (NIST SP 800-204, OWASP CI/CD Top 10, SLSA) and demonstrate compliance against NIS 2's partial-coverage maintenance dimension and CRA's partial-coverage update-distribution pathway. The pipeline-architecture controls (signed artefacts, build-agent integrity, ephemeral build environments) are industry-best-practice, not regulatory mandate.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-07.3
title: D-07.3 CI/CD Pipeline Security — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-07 Secure Development
sub_domain: D-07.3 CI/CD Pipeline Security
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-07_Secure-Development/D-07.3.md
status: DRAFT
---
> **Domain analysis:** [D-07.3 CI/CD Pipeline Security](../../DomainAnalysis/D-07_Secure-Development/D-07.3.md)
#### D-07.3 CI/CD Pipeline Security
<!-- participants: NIS2, CRA -->
**Participants (from CRDA):** NIS2, CRA
**Sole-authority note:** AEGIS taxonomy §4.1 marks NIS 2 as sole authority for D-07.3 CI/CD Pipeline Security (T3-vs-text gap: OJ Art. 21(2)(e) does not mention `pipeline`, `CI`, or `CD`). NIS 2 provides only partial coverage via the maintenance dimension. CRA Annex I Part II (7)+(8) covers update distribution (delivery path), not CI/CD build-time controls.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

