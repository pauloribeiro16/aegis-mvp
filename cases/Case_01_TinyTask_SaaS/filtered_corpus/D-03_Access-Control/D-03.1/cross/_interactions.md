<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-03.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-03.1 Identity Lifecycle Management](../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.1.md)
#### D-03.1 Identity Lifecycle Management
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-03.1 Identity Lifecycle Management
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md`](../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.1.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope**).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-03.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-005 | Identity of data subjects making rights-exercise requests verified using reasonable means proportionate to risk | Controller; Art. 12(6) + Art. 11(2); data-subject-side (external) identity verification; PR.AA-03 + PR.AA-02 |
| NIS 2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i); workforce-side (internal) joiner-mover-leaver; PR.AA-01 + PR.AA-05 + PR.AT-02 |
| CRA | SO-CRA-015 | Identities, credentials, and access entitlements for users, services, and integrated components managed in a verifiable manner | Manufacturer; Annex I Part I (2)(d) + Art. 13(15); product-side (user / service / integrated-component identities); PR.AA-01 + ID.AM-01 |
| DORA | SO-DORA-002 (partial) | Strong authentication + key protection (Art. 9(4)(d) 3-control AND); identity-lifecycle is one dimension | Financial entity; Art. 9(4)(d); staff + service-to-service identities (financial-entity-side); PR.AA-03 + PR.AA-04 |

## Validated relationships (from CRDA-deep §D-03.1)

#### Validated relationships (from CRDA-deep §D-03.1)
All 6 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial classifications — 2 pairs initially marked **DIFFERENT PERSPECTIVE**
and 4 pairs marked **COMPLEMENTARY** were all verified as SAME after
OJ-text analysis). The underlying obligation is the **same substantive
identity-management duty** (managing identities of principals that
interact with a system — for authentication, authorisation, verification
or accountability purposes); the pairs differ on the **identity subject**
that each regulation targets. The four regulators operate at four
**different identity boundaries**:
- **GDPR** — data subjects (external, rights-exercise context): the
  controller verifies the identity of a natural person making a request
  under Art. 15–22 (Art. 12(6)) and the data subject supplies enabling
  information (Art. 11(2)). Proportionate to risk; minimal collection
  per Art. 5(1)(c).
- **NIS 2** — workforce (internal, joiner-mover-leaver): the entity
  manages its own personnel identities throughout the employment
  lifecycle — provisioning on induction, entitlement review on role
  change, revocation on separation. Continuously; appropriate and
  proportionate per Art. 21(1).
- **CRA** — product users, services, and integrated components
  (product-side): the manufacturer manages identities and credentials
  for human users of the product, service identities, and identities of
  integrated components, in a "verifiable manner" throughout the
  operational lifetime. Unique product identification (type/batch/serial
  per Art. 13(15) + Annex II §3) backs the SBOM-correlated identity
  register.
- **DORA** — staff + service-to-service identities (financial-entity-side):
  the strong-authentication obligation of Art. 9(4)(d) covers
  financial-entity staff and machine/service identities with identity
  assertions managed, protected and conveyed under standards.
The identity objects are **different** but the identity-management duty
is the **same substantive obligation** — verified by CRDA-deep as
SAME after OJ-text analysis. There is no contradiction because no
clause forbids what another mandates; a single organisation across
all four regulators must operate a **multi-boundary identity
architecture**, with the boundaries explicitly documented. CRA's
"verifiable manner" (Annex I Part I (2)(d)) is **stricter** than GDPR's
"reasonable means proportionate to risk" (Art. 12(6)) — the manufacturer
must demonstrate that identities are managed verifiably, not merely that
verification is proportional.
The scope-overlap column in the matrix below indicates whether the same
artefact can trigger both regulations on a single party; this is the
gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (disjoint in baseline; Y when CRA product hosts data-subject rights endpoints)  |
|  **CRA**  |  Conditional (Y integrated manufacturer-controller)  |  —  |
Legend: **Y** = scope overlap on a single artefact (high-level SO can
engage on a single party); **N** = scope-disjoint in baseline case; **Conditional** = disjoint in baseline case, Y on
integrated-stack or vertical-integration scenario. CRDA-deep
scope-disjoint tests: GDPR↔NIS2 = N (data subjects vs workforce are
distinct identity objects even on a controller-and-NSIE); GDPR↔CRA =
Conditional; GDPR↔DORA = Conditional; NIS2↔CRA = Conditional; NIS2↔DORA
= Conditional (cross-sector Y, pure-financial N lex specialis); CRA↔DORA
= Conditional.

## Cross-recipient map

#### Cross-recipient map
D-03.1 itself does **not** generate recipient asymmetry — the
identity-management process is inward-looking, with the resulting
identity register feeding downstream authentication (D-03.2),
authorisation (D-03.3) and audit-trail (D-10.2) sub-domains. The
recipient fragmentation across the four regulators is at the
**compliance-demonstration point**: GDPR's supervisory authority
(Art. 12 verification evidence on rights-request audit), NIS 2's
competent authority / CSIRT (Art. 21(2)(i) entity governance),
CRA's market surveillance authority (Annex VII technical documentation
on identity-management framework), and DORA's national competent
authority + ESAs (Art. 9(4)(d) authentication-policy evidence). These
are distinct regulatory channels but they do not generate the
notification cascade of D-04.3 — they are compliance-evidence
channels on the same identity-management architecture.
---

## HSO considerations (from D-03.1.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations impose the same substantive identity-management duty but each targets a distinct identity subject at a distinct boundary and anchors to a distinct threshold: GDPR data-subject-side proportionate verification on reasonable doubt (Art. 12(6) + Art. 11(2); minimal collection per Art. 5(1)(c)); NIS 2 workforce-side continuous joiner-mover-leaver lifecycle under HR-security discipline (Art. 21(2)(i); the access-control policy and asset-management sub-domains are coordinated by the literal AND in the same sub-point); CRA product-side verifiable identity-management for users, services and integrated components (Annex I Part I (2)(d) + Art. 13(15) + Annex II §3; the "verifiable manner" reading is stricter than the GDPR proportionality test); DORA financial-entity-side strong-authentication identity assertion management (Art. 9(4)(d); the identity-lifecycle is one of the three coordinated controls in the same sub-point — strong authentication + key protection + encryption).
- The high-level SO describes the common identity-management duty (verifiable, lifecycle-aware, boundary-disciplined); the per-regulation perspective is preserved in the four sub-SOs (identity subject, threshold anchor, evidence template, recipient).
- A single organisation across all four regulators must operate a multi-boundary identity architecture with explicit boundary hand-offs: data-subject verification flows into staff authentication at the rights-exercise endpoint; staff identity feeds into product-user identity via deployment; product-user identity feeds back into DORA service-identity via integration.
- For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- CRA is the strictest knowledge-test floor ("verifiable manner") and discharges the GDPR `reasonable means proportionate to risk` on the identity-management dimension when the same party operates both manufacturer-side and controller-side roles.
- DORA's identity-assertion discipline (PR.AA-04) — managing, protecting and conveying identity assertions in a manner that verifies authenticity — is the strictest assertion-conveyance floor and supports the NIS 2 `where appropriate` test on authentication strength for financial-sector entities also within retained NIS 2 scope.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-03.1 over a distinct
**identity subject** (the boundary at which identity is managed); the
trigger, the threshold anchor, the lifecycle cadence, the recipient, and
the legal anchor all depend on which boundary the identity falls into.
| Axis (reg) | Identity subject | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | data subjects (external, rights-exercise) | reasonable doubts concerning identity of requester (Art. 12(6)) | `reasonable means proportionate to risk` + Art. 5(1)(c) minimisation | supervisory authority (verification-evidence audit) | Art. 12(6) + Art. 11(2) |
| **NIS 2** | workforce (internal, joiner-mover-leaver) | continuous (provisioning on induction, review on role change, revocation on separation) | `appropriate and proportionate` (Art. 21(1)) | competent authority / CSIRT (entity governance audit) | Art. 21(2)(i) (HR-security dimension) |
| **CRA** | product users + services + integrated components | continuous (throughout operational lifetime) + triggered (becoming aware of identity-vulnerability) | `verifiable manner` (Annex I Part I (2)(d)) | market surveillance authority (Annex VII technical documentation) + users (Annex II §3 unique identification) | Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3 |
| **DORA** | financial-entity staff + service identities | continuous (strong-authentication under standards) | `strong authentication mechanisms based on relevant standards and dedicated control systems` + Art. 6(8) `appropriate level of independence` | national competent authority + ESAs | Art. 9(4)(d) (3-control AND: strong auth + key protection + encryption) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-03.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations' identity-boundary scope-determiners overlap on the same
party** (e.g. a controller that is also a NIS 2 essential entity
operating CRA-regulated products and running a DORA-class financial ICT
system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-boundary identity architecture).
Pure co-applicability of disjoint-boundary regulations on different
identity objects does **not** trigger cross-regulation aggregation — see
the Activation logic in the file header. For a 5-FTE SaaS startup with
GDPR + CRA applicability but no NIS 2 / DORA applicability, only the
GDPR and CRA sub-SOs activate; the high-level SO engages on the same
party if both apply, with the boundary between data-subject verification
and product-user identity management documented as the controlled
hand-off. **The four identity boundaries are layered, not collapsed**:
data subjects are external (GDPR); workforce is internal (NIS 2);
product users + services + components are product-side (CRA); staff +
service identities are financial-entity-side (DORA). The high-level SO
surfaces the common identity-management duty but does **NOT** aggregate
the per-reg identity subjects, threshold anchors, or evidence templates.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4 — CRA Art. 13(11) is the dedicated
  authority for product-level identity management; no AI Act clause
  imposes an identity-lifecycle mandate).
- 6 pairwise cells, verified by CRDA-deep as **all SAME** after
  OJ-text analysis: GDPR↔NIS2 (CORRECTED from DIFFERENT-PERSPECTIVE),
  GDPR↔CRA (CORRECTED from DIFFERENT-PERSPECTIVE), GDPR↔DORA (CORRECTED
  from COMPLEMENTARY), NIS2↔CRA (CORRECTED from COMPLEMENTARY),
  NIS2↔DORA (CORRECTED from COMPLEMENTARY), CRA↔DORA (CORRECTED from
  COMPLEMENTARY).
- The four regulations impose the **same substantive identity-management
  duty** but each targets a **distinct identity subject** at a
  **distinct boundary**: data subjects (GDPR, external rights-exercise),
  workforce (NIS 2, internal joiner-mover-leaver), product users +
  services + integrated components (CRA, product-side), staff +
  service identities (DORA, financial-entity-side). The threshold
  anchors differ (GDPR's `reasonable means proportionate to risk` /
  NIS 2's `appropriate and proportionate` / CRA's `verifiable manner` /
  DORA's `strong authentication based on relevant standards`). CRA's
  `verifiable manner` is the **strictest knowledge-test floor** and
  discharges GDPR's `reasonable means` when the same party is both
  manufacturer-side and controller-side.
- The high-level SO describes the **COMMON OBJECTIVE** (verifiable,
  lifecycle-aware, boundary-disciplined identity management); the
  **per-regulation perspective** (identity subject, threshold anchor,
  evidence template, recipient) is preserved verbatim in the four
  sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 6 pairs as SAME. Phase 1C Doc 07 does not need
  to resolve contradictions on D-03.1 because none exist on the
  identity-management duty itself; the task is to **stack the
  documentation** so that a single multi-boundary identity architecture
  discharges all four obligations on the same party, with explicit
  boundary hand-offs at the identity-type surfaces.
- **Scope caveat (CRITICAL — identity-subject divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the four identity subjects into a single principal type.
  Data subjects, workforce, product users, services, integrated
  components, financial-entity staff and service identities are
  **distinct identity objects** at **distinct boundaries**, with
  distinct lifecycle triggers (rights-request vs employment lifecycle
  vs product operational lifetime vs financial-entity continuous
  operation) and distinct evidence templates (verification record vs
  joiner-mover-leaver ticket vs Annex VII identity-management
  framework vs PR.AA-04 identity-assertion audit trail). A unified
  IAM system may serve the technical substrate (e.g. an identity
  provider with multiple identity classes), but the policy and
  evidence layers must remain **boundary-segregated** for compliance
  demonstration. Phase 1A must therefore emit **four checks before
  applying the high-level SO** (one per participating regulation) to
  confirm that the per-reg identity subject, boundary, threshold
  anchor, and evidence template are documented separately; the
  high-level SO surfaces the common identity-management duty but does
  NOT aggregate the per-reg identity subjects.
- **Scope caveat (CRITICAL — CRA "verifiable manner" strictness)** —
  derived from CRDA-deep verified classifications: the CRA "verifiable
  manner" threshold is **stricter than GDPR's "reasonable means
  proportionate to risk"** — the manufacturer must demonstrate that
  identities (users, services, integrated components) are managed
  verifiably throughout the operational lifetime, not merely that
  verification is proportional to a request risk. For a party in both
  CRA and GDPR scope, the CRA floor discharges the GDPR verification
  leg when the same identity substrate operates both roles; the
  evidence layer must document which artefacts support which role.
- **Scope caveat (CRITICAL — DORA lex specialis)** — derived from
  CRDA-deep verified classifications: the NIS 2 ↔ DORA pair is **NOT
  the same** relationship on cross-sector entities as on pure-financial
  entities. For pure-financial entities (NIS 2 §9 fall-back does not
  apply to entities already covered by DORA in scope), DORA absorbs
  the NIS 2 workforce-identity-lifecycle obligation via lex specialis;
  the high-level SO does not aggregate across the lex-specialis
  boundary in that direction. For cross-sector entities, the NIS 2
  entity-side HR-security dimension layers on the DORA
  financial-entity-side identity-assertion discipline, and the
  high-level SO engages on the same party.
---

## Emergent tensions (from CRDA-deep §D-03.1)

#### Emergent tensions (from CRDA-deep §D-03.1)
None — sub-domain is **all-SAME in baseline (6 pairs verified as SAME
after OJ-text analysis; CRDA initial 2 DIFFERENT-PERSPECTIVE + 4
COMPLEMENTARY classifications corrected to SAME)**. No conditional
emergent tensions on the identity-management duty itself. The
**identity-subject divergence** (data subjects / workforce / product
users + services + components / staff + service identities) is the
**legitimately diverse dimension**: each regulator targets a distinct
boundary, and the operational convergence is on a **multi-boundary
identity architecture** with explicit boundary hand-offs. The
**threshold-anchor divergence** (GDPR `reasonable means proportionate to
risk` / NIS 2 `appropriate and proportionate` / CRA `verifiable manner` /
DORA `strong authentication based on relevant standards`) is
**wording-only on a common substantive duty**; the strictest
knowledge-test floor (CRA `verifiable manner`) discharges the looser
ones on the same party when the same identity substrate operates both
roles. The CRA `verifiable manner` is **stricter than GDPR's
proportionality test** — the manufacturer's verifiable-management
discipline is the operative ceiling when both apply. The DORA
identity-assertion discipline (PR.AA-04) is the strictest
**assertion-conveyance floor** and supports the NIS 2 `where
appropriate` test on authentication strength for financial-sector
entities also within retained NIS 2 scope. The **scope-disjoint
divergence** (NIS 2 §9 fall-back / DORA lex specialis on pure-financial
entities) is **handled by the lex-specialis carve-out** — DORA absorbs
the NIS 2 obligation and the high-level SO does not aggregate across
the lex-specialis boundary in that direction. The high-level SO
surfaces the common identity-management duty; the per-reg identity
subject, boundary, threshold anchor, lifecycle cadence, recipient and
evidence template are documented separately in the four sub-SOs and
the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-03.1 — with
overlapping identity-boundary scope-determiners on the same party —
operates a **multi-boundary identity architecture** with explicit
boundary hand-offs. The high-level SO (`SO-D-03.1.HL`) describes the
common identity-management duty (verifiable, lifecycle-aware,
boundary-disciplined); the per-reg perspective is preserved in the four
sub-SOs (identity subject, threshold anchor, evidence template,
recipient). **No conflict-resolution is required on D-03.1 because
CRDA-deep verified all 6 pairs as SAME on the identity-management
duty.** Phase 1C Doc 07 documents the **layered identity-management
strategy**: (1) a multi-boundary identity architecture with explicit
boundary hand-offs at the identity-type surfaces (data subjects vs
workforce vs product users + services + components vs staff + service
identities); (2) the CRA `verifiable manner` floor as the operative
ceiling when both CRA and GDPR apply on the same identity substrate;
(3) the DORA `strong authentication based on relevant standards` as the
assertion-conveyance floor for financial-sector entities also
within retained NIS 2 scope; (4) the lex-specialis carve-out for
pure-financial entities (DORA absorbs NIS 2; no aggregation across
the boundary). For proportionality (P2), a 5-FTE SaaS with GDPR + CRA
applicability may default to the CRA `verifiable manner` floor as the
highest common denominator (DORA's assertion-conveyance discipline is
out of scope; NIS 2 workforce lifecycle is out of scope unless the SaaS
scales to essential-entity size); a 500-FTE DORA financial entity must
additionally document the PR.AA-04 identity-assertion-conveyance
discipline (signed tokens, mutual transport authentication, PKI
chain-of-trust) per `SR-DORA-002`; a DORA + NIS 2 cross-sector entity
must document both the DORA financial-entity-side assertion
discipline AND the NIS 2 workforce-side HR-lifecycle discipline with
explicit boundary hand-offs between them.

## Part 1 §3 — context

### 3. Security Requirements
## D-03.1 Identity Lifecycle Management — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md`. See that file for cross-reg verified relationships (6 pairs verified as SAME — CRDA initial 2 DIFFERENT-PERSPECTIVE + 4 COMPLEMENTARY corrected to SAME after OJ-text analysis), scope overlap matrix, Objective/Considerations content, identity-subject divergence (data subjects / workforce / product users + services + components / staff + service identities), CRA "verifiable manner" strictness, DORA lex specialis carve-out, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; no AI Act clause imposes an identity-lifecycle mandate; CRA Art. 13(11) is the dedicated authority for product-level identity management). CRDA-deep verified 6 pairs as all-SAME (2 corrected from DIFFERENT-PERSPECTIVE + 4 corrected from COMPLEMENTARY after OJ-text analysis). The four regulators target **different identity subjects** at **distinct boundaries** (data subjects external / workforce internal joiner-mover-leaver / product users + services + components product-side / staff + service identities financial-entity-side), and the high-level SO surfaces the common identity-management duty while preserving the per-reg boundary — the four identity boundaries are layered, not collapsed.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 3.1
  volere_section: 15
  volere_subtype: access
  title: "Identities of principals managed verifiably across the lifecycle with documented boundaries between identity types (multi-boundary identity architecture)"
  derives_from:
    hso_sub_so: SO-D-03.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.1.md
    objective_ref_section: "### D-03.1.0"
  description: |
    The product shall manage identities of principals that interact with the entity's systems, products, services, components and data — data subjects (external, rights-exercise), workforce (internal, joiner-mover-leaver), product users + services + integrated components (product-side), and staff + service identities (financial-entity-side) — in a verifiable, lifecycle-aware manner with documented boundaries between identity types and explicit hand-off protocols at boundary surfaces, as the common identity-management duty converging across GDPR Art. 12(6) + Art. 11(2) + Art. 5(1)(c), NIS 2 Art. 21(2)(i) HR-security dimension, CRA Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3, and DORA Art. 9(4)(d) identity-assertion discipline, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A multi-boundary identity architecture is operated with one identity register per boundary (data-subject verification register, workforce JML register, product-side user/service/component register, financial-entity staff/service-identity assertion register) and explicit hand-off protocols at the four identity-type surfaces; each register records identity subject, trigger, threshold anchor, lifecycle cadence, recipient, and evidence template per asset; the CRA `verifiable manner` floor is the operative ceiling when both CRA and GDPR apply on the same identity substrate; the DORA `strong authentication based on relevant standards` is the assertion-conveyance floor for financial-sector entities also within retained NIS 2 scope; the lex-specialis carve-out discharges the NIS 2 obligation for pure-financial entities (DORA absorbs NIS 2); verified by register audit-trail inspection at all four boundaries + boundary hand-off-protocol documentation review + CRA Annex VII identity-management framework inspection (when CRA in scope) + DPA / national-CA / CSIRT / MSA + ESA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, ID.AM-01, PR.AT-02, ID.AM-08, DE.CM-09]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping identity boundaries on the same party (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive identity-management duty but each targets a distinct identity subject at a distinct boundary and anchors to a distinct threshold: GDPR data-subject-side proportionate verification on reasonable doubt (Art. 12(6) + Art. 11(2); minimal collection per Art. 5(1)(c)); NIS 2 workforce-side continuous joiner-mover-leaver lifecycle under HR-security discipline (Art. 21(2)(i); the access-control policy and asset-management sub-domains are coordinated by the literal AND in the same sub-point); CRA product-side verifiable identity-management for users, services and integrated components (Annex I Part I (2)(d) + Art. 13(15) + Annex II §3; the "verifiable manner" reading is stricter than the GDPR proportionality test); DORA financial-entity-side strong-authentication identity assertion management (Art. 9(4)(d); identity-lifecycle is one of the three coordinated controls in the same sub-point — strong authentication + key protection + encryption). The four identity boundaries are layered, not collapsed — a unified IAM system may serve the technical substrate but the policy and evidence layers must remain boundary-segregated for compliance demonstration. The CRA "verifiable manner" is the strictest knowledge-test floor and discharges GDPR's "reasonable means" when both apply on the same identity substrate; the DORA identity-assertion discipline (PR.AA-04) is the strictest assertion-conveyance floor and supports the NIS 2 `where appropriate` test on authentication strength for financial-sector entities also within retained NIS 2 scope. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so a single multi-boundary identity architecture discharges all four obligations on the same party, with explicit boundary hand-offs at the identity-type surfaces. (Copied from the HSO Considerations block of `### D-03.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-03.1
title: D-03.1 Identity Lifecycle Management — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.1 Identity Lifecycle Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-03_Access-Control/D-03.1.md
status: DRAFT
---
> **Deep analysis:** [D-03.1 Identity Lifecycle Management](../../DeepAnalysis/D-03_Access-Control/D-03.1.md)
#### D-03.1 Identity Lifecycle Management
<!-- participants: GDPR, NIS2, CRA, DORA (partial) -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-005 | Identity of data subjects making rights-exercise requests verified using reasonable means proportionate to risk | Controller; Art. 12(6) + Art. 11(2); data-subject-side identity verification; PR.AA-03 + PR.AA-02 |
| NIS2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i); HR-security dimension covers joiner-mover-leaver; PR.AA-01 + PR.AA-05 + PR.AT-02 |
| CRA | SO-CRA-015 | Identities, credentials, and access entitlements for users, services, and integrated components managed in a verifiable manner | Manufacturer; Annex I Part I (2)(d) + Art. 13(15); product-level; "verifiable manner" (VAG) + Annex II §3 user-facing unique identification |
| DORA | SO-DORA-002 (partial) | Strong authentication + key protection (Art. 9(4)(d) 3-control AND) | Financial entity; Art. 9(4)(d); identity-lifecycle is one dimension of the strong-authentication obligation; PR.AA-03 + PR.AA-04 |
| AI_Act | — | Out-of-scope (no identity-lifecycle mandate; CRA Art. 13(11) sole authority per taxonomy §4) | n/a |
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
<!-- emergent: GDPR,NIS2,CRA,DORA -->
- All four regulations impose an identity-management obligation, but the **identity subject** differs: GDPR (data subjects, external), NIS 2 (workforce, internal), CRA (product users + services + integrated components, product-side), DORA (staff + service-to-service identities, financial-entity-side). The four operate at different identity boundaries and are **not contradictory** because they target different identity objects. A company across all four must operate a multi-boundary identity architecture, with the boundaries clearly documented. Layer 2/3 should specify the hand-off protocols at the boundary surfaces (e.g. data subject → staff via rights-exercise; staff → service identity via authentication; service identity → product user via integration).
- **CRA's "verifiable manner"** (Annex I Part I (2)(d)) is a S3 VAG term that the SR-CRA-023 reading resolves to PR.AA-01 (identities managed by the organisation) + ID.AM-01 (hardware inventories). The verifiable-manner threshold is operationally consequential for product manufacturers: a CRA product that does not have a verifiable identity-management framework for users/services/components fails Annex I Part I (2)(d). This is **stricter** than GDPR's data-subject-side verification (Art. 12(6) "reasonable means proportionate to risk").
<!-- /emergent -->
##### SR cross-validation
CSF mappings are diverse: GDPR maps to PR.AA-03 + PR.AA-02 + ID.AM-08; NIS 2 to PR.AA-01 + PR.AA-05 + PR.AT-02; CRA to PR.AA-01 + ID.AM-01; DORA to PR.AA-03 + PR.AA-04. The shared anchors are PR.AA-01 (NIS 2 + CRA) and PR.AA-03 (GDPR + DORA); the supplementary anchors (PR.AA-02, PR.AA-04, PR.AA-05, PR.AT-02, ID.AM-08, ID.AM-01) capture the boundary-specific depth. The cross-cutting observation: identity management is a sub-domain where the four regulators target different identity objects and the CSF mapping accordingly diverges at the supplementary layer.
##### Downstream implication
For Phase 1C Doc 07, D-03.1 is a **multi-boundary identity architecture** sub-domain: a company across multiple regulators must document each identity boundary separately. Proportionality: a small SaaS (no DORA, no NIS 2) may operate a unified identity service for product users and staff; a DORA financial entity must operate separate identity architectures for staff, services, and data subjects, with documented boundary hand-offs.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-03.1
title: D-03.1 Identity Lifecycle Management — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.1 Identity Lifecycle Management
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-03_Access-Control/D-03.1.md
status: DRAFT
---
> **Domain analysis:** [D-03.1 Identity Lifecycle Management](../../DomainAnalysis/D-03_Access-Control/D-03.1.md)
#### D-03.1 Identity Lifecycle Management
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
