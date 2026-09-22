# D-01.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-01.3 Cryptographic Key Management](../../DomainAnalysis/D-01_Data-Protection/D-01.3.md)
#### D-01.3 Cryptographic Key Management
<!-- participants: GDPR, CRA, DORA; NIS2 partial; AI_Act absent -->
**Participants (from CRDA):** GDPR, CRA, DORA (NIS2 partial via SR-NIS2-001 cryptography policy; AI_Act absent per AEGIS taxonomy §4.1; CRA has a T2-vs-text gap on explicit key-management — the SR-CRA-004 reading imports Annex I (2)(d) access-control + (2)(e) "other technical means" to anchor the separation).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md`](../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.3.md)
> (3 pairs verified against OJ text; CRDA initial 3 COMPLEMENTARY
> classifications corrected to SAME after OJ-text analysis).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-01.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-002 | Pseudonymisation/encryption with separate-storage test for the additional information (keys) + Art. 34(3)(a) unintelligibility carve-out | Controller/processor; Art. 4(5) de-attribution test + Art. 34(3)(a) breach-context carve-out; personal-data scope; risk-anchored `appropriate` |
| CRA | SO-CRA-004 | Cryptographic key separation from operational environment (custodian ≠ consumer) | Manufacturer; Annex I Part I (2)(d)+(e) functional-RBAC reading (T2-vs-text gap reading per `99_CRA_Synthesis.md` §4); product-level; "personal or other"; state-of-the-art baseline |
| DORA | SO-DORA-002 | Strong authentication + cryptographic-key protection + encryption (3-control AND) with classification-driven cipher strength | Financial entity; Art. 9(4)(d) 3-control AND; ICT-system-level; entity-level HSM/split-knowledge/classification-tiered rotation; `high standards` anchor |

## Validated relationships (from CRDA-deep §D-01.3)

#### Validated relationships (from CRDA-deep §D-01.3)
All 3 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial 3 COMPLEMENTARY classifications to SAME after OJ-text analysis).
The underlying obligation is the same (cryptographic key separation between
custodian and consumer, so that possession of the key material — not the
storage medium — is the necessary condition for intelligibility); the pairs
differ only on scope qualifier (`personal data` vs `product with digital
elements` vs `ICT of financial entity`) and on the **operational depth**
(GDPR = de-attribution test via Art. 4(5); CRA = functional RBAC
separation; DORA = HSM-anchored custodianship + split-knowledge ceremonies
+ classification-tiered rotation + quorum-based recovery). CRDA-deep
explicitly notes (CRA↔DORA pair) that CRA is the necessary-but-not-sufficient
product-side floor and DORA is the entity-side depth layer — the two are
genuinely layered in depth, not scope-disjoint. The GDPR↔CRA pair converges
on key separation as the technical property and "unauthorised party cannot
access" as the operational test, with the Art. 32 documentation vs Annex VII
conformity dossier as the only documentation difference. The GDPR↔DORA pair
converges on the de-attribution test (PR.DS-01 + PR.IR-03) sitting beneath
DORA's classification-driven tiering (PR.DS-01 + GV.RM-04); meeting the
DORA Art. 9(4)(d) classification-driven tiering discharges the GDPR
key-separation obligation on the same data asset, with the controller's
Art. 32 documentation trail preserved separately.
The scope-overlap column in the matrix below indicates whether the same
key material can trigger both regulations on a single party; this is the
gating condition for the high-level SO to engage.
| | GDPR | CRA | DORA |
|---|---|---|---|
| **GDPR** | — | Y (CRA product stores personal data — typical); disjoint in baseline as manufacturer ≠ controller | Y (DORA financial entity processes personal data — typical) |
| **CRA** | Y | — | Y (DORA financial entity uses CRA product); disjoint in baseline as manufacturer ≠ financial entity |
| **DORA** | Y | Y | — |
Legend: **Y** = scope overlap on the same key material (high-level SO can
engage on a single key-custody architecture); **disjoint in baseline** =
manufacturer and controller/financial entity are typically different
parties (hand-off scenario). CRDA-deep scope-disjoint tests: GDPR↔CRA = Y;
GDPR↔DORA = Y; CRA↔DORA = Y.

## Cross-recipient map

#### Cross-recipient map
N/A — D-01.3 (key management) does not involve distinct recipient classes
(same as D-01.1 and D-01.2). The recipients are supervisory authorities for
compliance demonstration on inspection only (GDPR SA, CRA MSA, DORA CA + ESAs).
There is no notification or reporting trigger for the key-management
obligation itself (the Art. 34(3)(a) unintelligibility carve-out operates as
a defence to the data-subject notification under Art. 34, not as a separate
notification to a recipient). The D-04.3 sub-domain is the canonical
recipient-fragmentation locus for the data-protection area.
---

## HSO considerations (from D-01.3.0 — High-level SecurityObjective)

**Considerations.**
- The three participating regulations converge on the same substantive
  obligation (key separation as the technical property) but each
  operationalises it at a distinct depth on the same data asset: GDPR's
  de-attribution test (Art. 4(5) "additional information kept separately and
  subject to appropriate technical and organisational measures"; Art.
  34(3)(a) "render unintelligible to any person who is not authorised to
  access it"), CRA's functional-RBAC separation (Annex I (2)(d)
  access-control + (2)(e) "other technical means" reading per `SR-CRA-004`
  ambiguity_notes), and DORA's classification-driven entity-level
  architecture (Art. 9(4)(d) 3-control AND of strong authentication + key
  protection + encryption, classification-driven cipher strength with
  HSM-anchored custodianship + split-knowledge ceremonies + rotation
  cadence scaled to data criticality).
- CRDA-deep verified all 3 pairs as SAME — a single key-custody
  architecture (HSM-anchored custodianship + functional RBAC + documented
  rotation) discharges all three obligations on the same key material: the
  GDPR Art. 4(5) de-attribution test is met by the separation, the CRA
  Annex I (2)(d)+(e) functional-RBAC separation is met by the role-distinct
  credential assignment, and the DORA Art. 9(4)(d) classification-driven
  tiering is met by the tiered rotation cadence.
- The high-level SO describes the common obligation (key separation); the
  per-regulation perspective is preserved in the three sub-SOs (depth
  anchor, scope qualifier, recipient for compliance demonstration).
- For artefacts touching only one regulatory scope, only the triggered
  sub-SO applies.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 3 participating regulations each define D-01.3 over a distinct material
scope; the depth anchor and the legal anchor depend on which scope the key
material protects.
| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + breach-context (Art. 34(3)(a) carve-out) | personal-data additional information (keys) | supervisory authority (DPA) | Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility |
| **CRA** | continuous product-side baseline | cryptographic keys of product with digital elements | MSA + ENISA | Annex I Part I (2)(d) access control + (2)(e) `other technical means` |
| **DORA** | continuous + classification-driven re-tuning | cryptographic keys of ICT-supported financial-entity data | national CA + ESAs | Art. 9(4)(d) strong auth + key protection + encryption (3-control AND) |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-01.3.HL`) engages on a given key-custody architecture **if and only if
≥2 applicable regulations' scopes overlap on the same key material** (e.g.
the key material protecting personal data on a CRA-regulated product
deployed by a DORA financial entity — a vertically-integrated
manufacturer-controller on a financial-services stack). Pure co-applicability
of disjoint-scope regulations on different key material does **not** trigger
cross-regulation aggregation — see the Activation logic in the file header.
For a 5-FTE SaaS startup with GDPR + CRA applicability but no DORA
applicability, only the GDPR and CRA sub-SOs activate; the high-level SO
engages on the same key material when both apply. For a DORA financial
entity that is also a GDPR controller, the high-level SO engages on the
classification-driven tiering + de-attribution test pair on the same key
material; the DORA depth layer (HSM + split-knowledge + quorum-recovery)
sits above the GDPR/CRA floor.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 3 of 5 regulations participate (GDPR, CRA, DORA; NIS 2 partial via
  `SR-NIS2-001` cryptography policy but standalone out-of-scope for D-01.3
  per `99_NIS2_Synthesis.md` §8 T3-vs-text gap; AI Act absent per AEGIS
  taxonomy §4.1).
- 3 pairwise cells, verified by CRDA-deep as **all SAME** after OJ-text
  analysis: GDPR↔CRA (CORRECTED from COMPLEMENTARY), GDPR↔DORA (CORRECTED
  from COMPLEMENTARY), CRA↔DORA (CORRECTED from COMPLEMENTARY).
- The three regulations impose the **same substantive obligation** (key
  separation between custodian and consumer) with different **depth anchors**
  (GDPR = de-attribution test; CRA = functional RBAC separation; DORA =
  HSM-anchored custodianship + split-knowledge + classification-driven
  tiering). CRA is the necessary-but-not-sufficient product-side floor;
  DORA is the entity-side depth layer; GDPR is the personal-data-side
  method that earns the Art. 34(3)(a) carve-out.
- The high-level SO describes the **COMMON OBJECTIVE** (key separation as
  the technical property so that possession of the key material — not the
  storage medium — is the necessary condition for intelligibility); the
  **per-regulation perspective** (depth anchor, scope qualifier, recipient,
  content template) is preserved verbatim in the three sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension — there
  are 0 conditional emergent tensions in this sub-domain; CRDA-deep
  verified all 3 pairs as SAME. Phase 1C Doc 07 does not need to resolve
  contradictions on D-01.3 because none exist; the task is to **stack the
  documentation** so that a single key-custody architecture discharges all
  three obligations.
- **Scope caveat (CRITICAL — depth framing)** — derived from CRDA-deep
  verified classifications: the high-level SO does NOT aggregate across
  manufacturer/controller hands-offs as equivalent depth layers. A
  SaaS-using-CRA-product scenario has disjoint baseline obligations (CRA
  manufacturer supplies product-side key-separation baseline; GDPR
  controller implements the de-attribution test on its own key custody; the
  two are separate compliance tracks unless the same party is both
  manufacturer and controller). The CRA product-side floor met at the
  manufacturer does not by itself discharge the GDPR controller's
  deployment-side responsibility — the controller's risk assessment and
  key-separation architecture remain its own. Similarly, the CRA↔DORA
  pair is genuinely layered in depth (CRA product-side RBAC ≠ DORA
  entity-side HSM/split-knowledge/quorum-recovery); the high-level SO
  surfaces the common objective but the **depth proportionality** is the
  Phase 1C design lever: a DORA financial entity requires the full
  split-knowledge + quorum-recovery stack; a small SaaS (no DORA scope)
  meets the floor with HSM-anchored custodianship + documented rotation.
---

## Emergent tensions (from CRDA-deep §D-01.3)

#### Emergent tensions (from CRDA-deep §D-01.3)
None — sub-domain is **all-SAME in baseline (3 pairs verified as SAME
after OJ-text analysis; CRDA initial 3 COMPLEMENTARY classifications
corrected to SAME)**. No conditional emergent tensions. The **depth
divergence** (GDPR de-attribution test vs CRA functional-RBAC separation vs
DORA HSM/split-knowledge/classification-tiered) is **layered in depth, not
contradictory in scope**: CRA is the necessary-but-not-sufficient product-side
floor, DORA is the entity-side depth layer, GDPR is the personal-data-side
method that earns the Art. 34(3)(a) carve-out. The three depths converge on
the same technical property (key separation between custodian and consumer)
at different operational rigours. The operational convergence is on
**HSM-anchored key custodianship + functional RBAC + classification-driven
rotation**, and the strictest depth layer (DORA's HSM + split-knowledge +
quorum-recovery) discharges the shallower layers on the same key material
when the DORA financial entity is also a GDPR controller using CRA-regulated
products. CRDA-deep explicitly notes (in the CRA↔DORA pair reasoning) that
CRA is the necessary-but-not-sufficient product-side floor and DORA is the
entity-side depth layer — the depth framing is correct, not a contradiction.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-01.3 — with
overlapping scopes on the same key material — operates a **single
key-custody architecture (HSM-anchored custodianship + functional RBAC +
classification-driven rotation)** that discharges all obligations. The
high-level SO (`SO-D-01.3.HL`) describes the common obligation (key
separation); the per-reg perspective is preserved in the sub-SOs (depth
anchor, scope qualifier, recipient for compliance demonstration). **No
conflict-resolution is required on D-01.3 because CRDA-deep verified all 3
pairs as SAME.** Phase 1C Doc 07 documents the **stacked documentation
strategy**: (1) a single key-custody architecture (HSM-anchored, RBAC-separated,
classification-tiered rotation); (2) a joint risk assessment citing all
three legal anchors (Art. 4(5) + Art. 34(3)(a) + Annex I (2)(d)+(e) +
Art. 9(4)(d)); (3) per-recipient evidence packs for SA / MSA / DORA CA on
request. **Proportionality is the decisive design lever (P2)** — D-01.3 is
the **deepest-stack sub-domain within D-01** per the CRDA Domain Analysis
downstream implication: a DORA financial entity requires the full
split-knowledge + quorum-recovery stack; a 5-FTE SaaS (no DORA scope) meets
the floor with HSM-anchored custodianship + documented rotation; a
DORA-financial-entity-using-CRA-product scenario stacks the CRA product-side
RBAC + the DORA entity-side HSM/split-knowledge + the GDPR de-attribution
test + the Art. 34(3)(a) unintelligibility carve-out — all on the same key
material with a single documentation trail.

## Part 1 §3 — context

### 3. Security Requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.3.md`. See that file for cross-reg verified relationships, scope overlap matrix, Objective/Considerations content, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA, DORA (3 of 5 regs; NIS 2 partial via `SR-NIS2-001` cryptography policy but standalone out-of-scope for D-01.3 per `99_NIS2_Synthesis.md` §8 T3-vs-text gap; AI Act absent per AEGIS taxonomy §4.1). CRDA-deep verified 3 pairs as all-SAME (CRDA initial 3 COMPLEMENTARY classifications corrected to SAME after OJ-text analysis).
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 1.3
  volere_section: 15
  volere_subtype: access
  title: "Cryptographic keys are managed with separation between custodian and consumer (multi-reg aggregation)"
  derives_from:
    hso_sub_so: SO-D-01.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.3.md
    objective_ref_section: "### D-01.3.0"
  description: |
    The product shall manage cryptographic keys and related authentication material with separation of roles such that possession of the key material — not the storage medium — is the necessary condition for intelligibility of the protected data, as the common substantive obligation converging across GDPR Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a), CRA Annex I Part I (2)(d)+(e), and DORA Art. 9(4)(d) where ≥2 of these scopes overlap on the same key material.
  fit_criterion: |
    An HSM-anchored key-custody architecture is in place where the key-material custodian and the operational-environment consumer are distinct roles under distinct credentials with RBAC-enforced separation; documented key-rotation cadence is classified-tiered (scaled to data criticality per DORA Art. 9(4)(d) + EBA Guidelines §149 where DORA applies); functional RBAC separation meets CRA Annex I (2)(d)+(e) `other technical means` reading; the de-attribution test (GDPR Art. 4(5)) is met by physical or logical separation of the additional information from the personal data; verified by automated configuration audit of key-custody roles + manual separation-of-roles review + joint documentation trail citing all three legal anchors when scopes overlap; depth proportionality applied per P2 (DORA financial entity requires split-knowledge + quorum-recovery; 5-FTE SaaS meets the floor with HSM-anchored custodianship + documented rotation).
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.IR-03, GV.OV-01, GV.RM-04]
  applicable_if:
    regs: [GDPR, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs overlap on same key material (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The three participating regulations converge on the same substantive obligation
    (key separation as the technical property) but each operationalises it at a
    distinct depth on the same data asset: GDPR's de-attribution test (Art. 4(5)),
    CRA's functional-RBAC separation (Annex I (2)(d)+(e)), and DORA's
    classification-driven entity-level architecture (Art. 9(4)(d) 3-control AND).
    CRDA-deep verified all 3 pairs as SAME — a single key-custody architecture
    (HSM-anchored custodianship + functional RBAC + classification-driven
    rotation) discharges all three obligations on the same key material. For
    artefacts touching only one regulatory scope, only the triggered sub-
    requirement applies. Depth proportionality (P2) is the decisive design
    lever: a DORA financial entity requires the full split-knowledge +
    quorum-recovery stack; a small SaaS (no DORA scope) meets the floor with
    HSM-anchored custodianship + documented rotation. (Copied from the HSO
    Considerations block of `### D-01.3.0`; preserved here for self-contained
    traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-01.3
title: D-01.3 Cryptographic Key Management — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.3 Cryptographic Key Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-01_Data-Protection/D-01.3.md
status: DRAFT
---
> **Deep analysis:** [D-01.3 Cryptographic Key Management](../../DeepAnalysis/D-01_Data-Protection/D-01.3.md)
#### D-01.3 Cryptographic Key Management
<!-- participants: GDPR, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-002 (cross-ref) | When pseudonymisation or encryption applied, additional information (keys) kept separately with technical and organisational measures | Controller/processor; Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility exception |
| CRA | SO-CRA-004 | Cryptographic keys and related authentication material managed with separation of roles (key custodian ≠ operational environment) | Manufacturer; Annex I Part I (2)(d)+(e); product-level; separation as a T2-vs-text gap reading (CRA-CL134 + CRA-CL133 combined) |
| DORA | SO-DORA-002 | Strong authentication mechanisms + cryptographic-key protection measures + data encryption (3-control AND) | Financial entity; Art. 9(4)(d); classification-driven cipher strength |
| NIS2 | — | Out-of-scope for D-01.3 standalone (T3-vs-text gap per `99_NIS2_Synthesis.md` §8); keys covered implicitly by SO-NIS2-001 cryptography policy | n/a |
| AI_Act | — | Out-of-scope (no key-management mandate) | n/a |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,CRA,DORA -->
- All three regulations anchor key management to a **separation property** (custodian ≠ consumer), but the operational depth differs materially: GDPR (de-attribution test, PR.DS-01 + PR.IR-03); CRA (functional RBAC separation, PR.DS-01 + PR.AA-05 + GV.OV-01); DORA (HSM-anchored custodianship + split-knowledge + classification-driven cipher strength + quorum-based recovery, PR.DS-01 + PR.AA-03 + PR.AA-04 + GV.RM-04). A small SaaS company (CRA scope + GDPR scope) typically meets the floor; a DORA financial entity (all three) must operate a substantially deeper architecture. Proportionality (P2) is the relevant design lever.
<!-- /emergent -->
##### SR cross-validation
All three regulations share PR.DS-01 as a common CSF anchor; DORA additionally anchors on PR.AA-03 + PR.AA-04 (the strong-authentication + key-protection 3-control AND), and CRA additionally anchors on PR.AA-05 (least privilege) + GV.OV-01 (strategy review). GDPR additionally anchors on PR.IR-03 (resilience for the Art. 34(3)(a) carve-out). The cross-cutting observation: PR.DS-01 is the necessary but not sufficient anchor; the supplementary subcategories (PR.AA-*, PR.IR-*, GV.OV-*) encode the operational depth.
##### Downstream implication
For Phase 1C Doc 07, D-01.3 is the **deepest-stack** sub-domain within D-01: the DORA-classified key-management architecture is materially more expensive than the GDPR/CRA floor. Proportionality is decisive: a small SaaS (no DORA scope) meets the floor with HSM-anchored custodianship + documented rotation; a DORA financial entity requires the full split-knowledge + quorum-recovery stack.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-01.3
title: D-01.3 Cryptographic Key Management — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.3 Cryptographic Key Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-01_Data-Protection/D-01.3.md
status: DRAFT
---
> **Domain analysis:** [D-01.3 Cryptographic Key Management](../../DomainAnalysis/D-01_Data-Protection/D-01.3.md)
#### D-01.3 Cryptographic Key Management
<!-- participants: GDPR, CRA, DORA; NIS2 partial; AI_Act absent -->
**Participants (from CRDA):** GDPR, CRA, DORA (NIS2 partial via SR-NIS2-001 cryptography policy; AI_Act absent per AEGIS taxonomy §4.1; CRA has a T2-vs-text gap on explicit key-management — the SR-CRA-004 reading imports Annex I (2)(d) access-control + (2)(e) "other technical means" to anchor the separation).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)