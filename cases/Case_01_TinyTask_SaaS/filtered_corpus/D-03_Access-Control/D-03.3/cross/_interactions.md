<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-03.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-03.3 Authorisation & Least Privilege](../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.3.md)
#### D-03.3 Authorisation & Least Privilege
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-03.3 Authorisation
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md`](../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.3.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope** per AEGIS taxonomy
> §4; CRA's Annex I Part I (2)(d) + (2)(j) carry both the access-control
> and the attack-surface-limitation dimensions within one sub-point; the
> (2)(j) attack-surface pillar is the **CRA-specific reporting lever** not
> mirrored in GDPR / NIS 2 / DORA).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-03.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality | Controller/processor; Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b); personal-data-scope chain of authority controller → processor → authorised persons; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| NIS 2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i) literal AND; entity-side model-agnostic access-control policy; PR.AA-01 + PR.AA-05 |
| CRA | SO-CRA-017 + SO-CRA-024 | Access to product with digital elements limited to authenticated and authorised users, services, hardware; possible unauthorised access reported; attack-surface limitation | Manufacturer; Annex I Part I (2)(d) + (2)(j); product-side access boundary + reporting + attack-surface-reduction; PR.AA-05 + PR.AA-06 + DE.CM-09 |
| DORA | SO-DORA-006 | ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only | Financial entity; Art. 9(4)(c) `legitimate and approved` AND + `only` qualifier (T4-vs-text gap: T4 reads RBAC + need-to-know + least privilege; OJ literal preserves "legitimate and approved functions and activities only"); PR.AA-05 + PR.AA-06 |

## Validated relationships (from CRDA-deep §D-03.3)

#### Validated relationships (from CRDA-deep §D-03.3)
All 6 pairs verified by CRDA-deep as **COMPLEMENTARY** (CRDA-deep corrected
CRDA's initial classifications — 1 pair initially marked **EQUAL** on
NIS2↔DORA was corrected to COMPLEMENTARY after OJ-text analysis showed
DORA's `only` qualifier is operationally more demanding than NIS 2's
model-agnostic `access control policies`; the other 5 pairs were
COMPLEMENTARY in CRDA and verified). The underlying obligation is the
**same substantive authorisation/least-privilege duty** (managing what
each principal may do on the system, anchored to the principle of least
privilege per PR.AA-05); the pairs differ on the **access surface** at
which authorisation operates, on the **textual anchor** of the obligation,
and on the **threshold language**.
The four regulators operate at four **different access surfaces** but
converge on the same **CSF operational pivot** (PR.AA-05 — access
permissions managed per least privilege):
- **GDPR** — personal-data-scope chain of authority: the
  controller → processor → authorised-persons chain under Art. 29 +
  Art. 32(4) + Art. 28(3)(a)/(b), with documented instructions and
  confidentiality undertakings as the binding instruments; the
  `instructions` anchor (POLY-S2) and the `appropriate statutory
  obligation of confidentiality` anchor (VAG-S2) are the principal
  polysemies preserved in `SR-GDPR-011` + `SR-GDPR-012` ambiguity_notes.
- **NIS 2** — entity-side access-control policy: the entity establishes
  and applies access-control policies for its network and information
  systems under Art. 21(2)(i), coordinated by the literal AND with
  HR-security (SR-NIS2-004 + D-03.1) and asset-management
  (SR-NIS2-005 + D-09.3 / D-03.3 cross); the access-control-policy
  reference is **model-agnostic** — the OJ text does not impose RBAC,
  ABAC, MAC or DAC — so any model that satisfies least-privilege is
  operative at the implementation layer. The T3-vs-text gap
  (T3 imports `RBAC + need-to-know + least privilege` vocabulary not
  present in the OJ; the SR preserves model-agnostic OJ language).
- **CRA** — product-side access boundary + reporting + attack-surface
  limitation: the manufacturer limits access to the product, its data,
  services and functions to authenticated and authorised users,
  services and hardware (Annex I Part I (2)(d)) **and** reports possible
  unauthorised access (Annex I Part I (2)(d) `possible` reading =
  inclusive — any successful + any detected-but-failed attempt)
  **and** limits attack surfaces including external interfaces
  (Annex I Part I (2)(j)). The reporting-and-attack-surface pillars
  are **CRA-specific** and not mirrored in the other three
  regulations' authorisation obligations; the cross-validation report
  flags VAG-S2 on `possible unauthorised access` (R1 inclusive chosen).
- **DORA** — financial-entity ICT-asset access policy: the financial
  entity limits physical or logical access to information assets and
  ICT assets to what is required for legitimate and approved functions
  and activities only (Art. 9(4)(c)), with the literal `only`
  qualifier (Berry §5.3.1 — correctly placed before the limiting
  phrase) closing off any access that is not strictly tied to a
  legitimate and approved function. The T4-vs-text gap (T4 imports
  `need-to-know + least privilege` vocabulary not in OJ; the SR
  preserves OJ-literal language and maps to PR.AA-05 by
  meaning-alignment without importing non-OJ vocabulary).
The substantive obligations are **compatible** — no clause forbids
what another mandates; a single organisation across all four
regulators must operate a **multi-boundary authorisation architecture**
with the boundaries explicitly documented:
|   |  GDPR  |  CRA  |
| --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (controller + CRA manufacturer; chain-of-authority ↔ product primitive)  |
|  **CRA**  |  Conditional (manufacturer-controller; product primitive ↔ chain-of-authority)  |  —  |
Legend: **Y** = scope overlap on a single artefact (high-level SO can
engage on a single party); **N** = scope-disjoint in baseline case; **Conditional** = disjoint in baseline case, Y on
integrated-stack or vertical-integration scenario. CRDA-deep
scope-disjoint tests: all 6 pairs = **Conditional** (no baseline
scope overlap, Y on integrated-stack or cross-sector entities). The
high-level SO engages on a single party **if and only if ≥2
applicable regulations' authorisation surfaces overlap on the same
party** (e.g. a controller that is also a NIS 2 essential entity
operating CRA-regulated products and running a DORA-class financial
ICT system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-boundary authorisation
architecture).
The **textual anchor** differs across the four regulations: GDPR
`chain of authority controller → processor → authorised persons`
(Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)); NIS 2 `access control
policies` model-agnostic (Art. 21(2)(i) — T3-vs-text gap, T3 imposes
RBAC + need-to-know + least privilege not in OJ); CRA `limited to
authenticated and authorised users, services and hardware` (Annex I
Part I (2)(d) + `(2)(j) limit attack surfaces including external
interfaces`); DORA `legitimate and approved functions and activities
only` (Art. 9(4)(c) — T4-vs-text gap, T4 imposes `need-to-know and
least privilege` not in OJ literal). The two **T-vs-text gaps** on
NIS 2 and DORA are methodologically significant: T3/T4 import
best-practice vocabulary not in the OJ text, and the Executor
preserves OJ-literal language in the SRs. Layer 2/3 should adjudicate
whether the T-imposed best practice survives as interpretive
continuation or whether the OJ-literal reading prevails. The
**DORA `only` qualifier** is operationally **more demanding than the
NIS 2 model-agnostic framing** and **strictly more demanding than CRA's
`limited to authenticated and authorised`** on the overlap surface —
DORA is the binding floor where the financial-entity-side and the
CRA-product-side stack up on the same artefact.
CRA's **report on possible unauthorised access** (Annex I Part I (2)(d)
`possible unauthorised access` — VAG S2 with R1 inclusive chosen) is
the **broadest visibility framing**: any unauthorised-access attempt
that succeeds, plus any attempt detected even when it failed, falls
within scope; backed by Annex I Part I (2)(l) recording-and-monitoring
(SR-CRA-027) and DE.CM-09 monitoring. GDPR's Art. 32(4) + Art. 29
chain-of-authority + Art. 28(3)(a)/(b) is the staff-side anchoring;
NIS 2's Art. 21(2)(i) is the policy-level; DORA's Art. 9(4)(c) is the
`legitimate and approved` framing. The reporting dimension is
**CRA-specific** and is not mirrored in the other three regulations'
authorisation obligations; the cross-validation is on PR.AA-05 +
PR.AA-06 (shared) + DE.CM-09 (CRA-specific).

## Cross-recipient map

#### Cross-recipient map
D-03.3 generates recipient fragmentation across the four regulators
at the **compliance-demonstration point**: GDPR's supervisory authority
(Art. 29 instruction register audit + Art. 28(3)(a) processor contract
inspection), NIS 2's competent authority / CSIRT (Art. 21(2)(i) entity
governance audit), CRA's market surveillance authority (Annex VII
technical documentation on the access-control framework, including
attack-surface-limitation evidence) plus product users (Annex II §8
user-facing instructions on monitoring + opt-out), and DORA's national
competent authority + ESAs (Art. 9(4)(c) policy evidence + access
register audit). These are distinct regulatory channels but they do
not generate the notification cascade of D-04.3 — they are
**compliance-evidence channels** on the same authorisation
architecture. For a controller that deploys CRA products and is also
a DORA financial entity, the boundary hand-offs at the
controller-↔-processor-↔-CRA-product-user-↔-DORA-financial-staff
interfaces are documented as the controlled interfaces; the
recipient channels layer rather than collapse, with the most
demanding floor (DORA `only` + CRA `verifiable manner` per D-03.1
discharge) operative on the same artefact.
---

## HSO considerations (from D-03.3.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations impose the same substantive authorisation duty anchored to PR.AA-05 (access permissions managed per least privilege); each targets a distinct authorisation surface at a distinct textual anchor and discharges through a distinct evidence template: GDPR instruction-bound processing (Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b); the `instructions` polysemy is R1 documented-in-the-contract with operational instructions recorded contemporaneously); NIS 2 model-agnostic access-control policy (Art. 21(2)(i); the literal AND binds access-control + HR-security + asset-management together; the T3-vs-text gap on `RBAC + need-to-know + least privilege` is preserved as model-agnostic); CRA authenticated-and-authorised product access with possible-unauthorised-access reporting and attack-surface limitation (Annex I Part I (2)(d) + (2)(j); R1 inclusive reading on `possible`); DORA legitimate-and-approved functions and activities only (Art. 9(4)(c); the literal `only` qualifier is the binding floor on the financial-entity-side; the T4-vs-text gap on `need-to-know + least privilege` is preserved as OJ-literal).
- The high-level SO surfaces the common authorisation/least-privilege duty (PR.AA-05 + PR.AA-06 anchors); the per-regulation perspective is preserved in the four sub-SOs (authorisation surface, textual anchor, evidence template, recipient).
- A single organisation across all four regulators must operate a multi-boundary authorisation architecture with explicit boundary hand-offs: personal-data-scope instructions feed into entity-side access-control policy; entity-side access-control policy feeds into CRA product access; product-side access controls inform DORA financial-entity-side legitimate-and-approved mappings.
- The DORA `only` qualifier is the strictest authorisation floor and discharges the CRA `limited to authenticated and authorised` and the NIS 2 `access control policies` on the same artefact when both apply.
- The CRA `possible unauthorised access` reporting dimension is the strictest visibility floor and is not mirrored in the other three regulators; the CRA DE.CM-09 monitoring is the pair to PR.AA-05 + PR.AA-06 in the SR-CRA-024 anchor.
- For parties that touch only one regulatory scope, only the triggered sub-SO applies.
- CRA is the strictest reporting floor (`possible unauthorised access` R1 inclusive) and supports the NIS 2 `appropriate and proportionate` test on visibility for entities that are both NIS 2 essential entities AND CRA manufacturers.
- DORA's `only` qualifier supports the NIS 2 `where appropriate` test on authorisation tightness for financial-sector entities also within retained NIS 2 scope.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-03.3 over a distinct
**authorisation surface** (the boundary at which authorisation is
managed); the trigger, the textual anchor, the threshold language,
the evidence template, and the recipient all depend on which surface
the authorisation operates on.
| Axis (reg) | Authorisation surface | Trigger | Textual anchor | Threshold language | Recipient | Evidence template |
|---|---|---|---|---|---|---|
| **GDPR** | personal-data-scope chain of authority (controller → processor → authorised persons) | continuous (instruction-bound processing) | `chain of authority controller → processor → authorised persons` (Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)) | `documented instructions` + confidentiality undertakings + Art. 5(1)(c) necessity on identified-purpose scope | supervisory authority (instruction register + processor contract inspection) | instruction register + processor Art. 28(3)(a)/(b) contract + confidentiality undertaking register + technical enforcement per PR.AA-05 + PR.AA-06 |
| **NIS 2** | entity-side access-control policy (model-agnostic) | continuous (entity access-control duty) | `access control policies` model-agnostic (Art. 21(2)(i) literal AND with HR-security + asset-management) | `appropriate and proportionate` (Art. 21(1)) — T3-vs-text gap preserved | competent authority / CSIRT (entity governance audit) | access-control policy + role definitions + HR-lifecycle records + asset-management register, on PR.AA-01 + PR.AA-05 + ID.AM-01/02 anchors |
| **CRA** | product-side authenticated-and-authorised product access + reporting + attack-surface limitation | continuous (product access-control duty + triggered on detection of unauthorised access) | `limited to authenticated and authorised users, services and hardware` + `possible unauthorised access reported` + `limit attack surfaces including external interfaces` (Annex I Part I (2)(d) + (2)(j)) | R1 inclusive on `possible` + state-of-the-art (Annex I (2)(e) `commensurate with the identified cybersecurity risk`) | market surveillance authority (Annex VII technical documentation) + product users (Annex II §8 user-facing instructions on monitoring + opt-out) | access-control records + attack-surface-reduction evidence + runtime-monitoring logs (DE.CM-09) + reporting evidence, on PR.AA-05 + PR.AA-06 + DE.CM-09 anchors |
| **DORA** | financial-entity-side ICT-asset access (physical or logical, both required per R1) | continuous (financial-entity ICT-access-policy duty) | `physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only` (Art. 9(4)(c); the literal `only` qualifies the limiting phrase) | `legitimate AND approved` + `only` qualifier (T4-vs-text gap preserved as OJ-literal — `need-to-know + least privilege` not in OJ) | national competent authority + ESAs (Art. 9(4)(c) policy evidence + access register audit) | entitlement inventory + access-review records + separation-of-duties attestation logs + physical-access audit trails, on PR.AA-05 + PR.AA-06 anchors with multi-party authorisation for privileged grants |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix; all
6 pairs = **Conditional** — no baseline scope overlap, Y on
integrated-stack or cross-sector entities. The high-level SO engages
on a single party **if and only if ≥2 applicable regulations'
authorisation surfaces overlap on the same party** with documented
boundary hand-offs.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-03.3.HL`) engages on a given party **if and only if ≥2 applicable
regulations' authorisation-surface scope-determiners overlap on the
same party** (e.g. a controller that is also a NIS 2 essential entity
operating CRA-regulated products and running a DORA-class financial
ICT system — a vertically-integrated manufacturer-controller on a
financial-services stack with a multi-boundary authorisation
architecture). Pure co-applicability of disjoint-surface regulations
on different artefacts does **not** trigger cross-regulation
aggregation — see the Activation logic in the file header. For a
5-FTE SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA
applicability, only the GDPR and CRA sub-SOs activate; the
high-level SO engages on the same party if both apply, with the
boundary between personal-data-scope instruction-bound processing and
product-side access boundary documented as the controlled hand-off.
**The four authorisation surfaces are layered, not collapsed**:
personal-data-scope chain of authority (GDPR, staff-side); entity-side
access-control policy (NIS 2, internal joiner-mover-leaver);
product-side authenticated-and-authorised boundary (CRA,
product-side); financial-entity-side ICT-asset access (DORA, ICT-
asset-side). The high-level SO surfaces the common
authorisation/least-privilege duty but does **NOT** aggregate the
per-reg authorisation surfaces, textual anchors, or evidence
templates.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4 — no AI Act clause imposes an
  authorisation/least-privilege mandate; AI Act AIA-C11 cites
  Art. 12(4) which does not exist in OJ).
- 6 pairwise cells, verified by CRDA-deep as **all COMPLEMENTARY**
  after OJ-text analysis: GDPR↔NIS2 (SAME — COMPLEMENTARY),
  GDPR↔CRA (SAME — COMPLEMENTARY), GDPR↔DORA (SAME — COMPLEMENTARY),
  NIS2↔CRA (SAME — COMPLEMENTARY), NIS2↔DORA (**CORRECTED** from CRDA
  EQUAL — DORA `only` qualifier is operationally more demanding than
  NIS 2's model-agnostic `access control policies`; COMPLEMENTARY is
  the verified classification), CRA↔DORA (SAME — COMPLEMENTARY).
- The four regulations impose the **same substantive
  authorisation/least-privilege duty** but each targets a **distinct
  authorisation surface** at a **distinct textual anchor**: GDPR's
  personal-data-scope chain of authority, NIS 2's entity-side
  access-control policy (model-agnostic), CRA's product-side
  authenticated-and-authorised boundary + reporting + attack-surface
  limitation, DORA's financial-entity-side legitimate-and-approved-only
  ICT-asset access policy. The textual anchors differ (GDPR `chain
  of authority` / NIS 2 `access control policies` model-agnostic /
  CRA `limited to authenticated and authorised users, services and
  hardware` + `possible unauthorised access reported` + `limit
  attack surfaces` / DORA `legitimate and approved functions and
  activities only` with the literal `only` qualifier). **DORA's
  `only` qualifier is the strictest authorisation floor** and is the
  binding floor where DORA and CRA / NIS 2 overlap on the same
  artefact. **CRA's `possible unauthorised access reported` is the
  strictest visibility floor** and is not mirrored in the other
  three regulators.
- The high-level SO describes the **COMMON OBJECTIVE**
  (authorisation per least privilege + boundary hand-offs +
  explicit attack-surface-limitation + reporting); the
  **per-regulation perspective** (authorisation surface, textual
  anchor, threshold language, evidence template, recipient) is
  preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions on the
  authorisation/least-privilege duty itself; CRDA-deep verified all
  6 pairs as COMPLEMENTARY. Phase 1C Doc 07 does not need to resolve
  contradictions on D-03.3 because none exist on the
  authorisation/least-privilege duty itself; the task is to
  **stack the documentation** so that a single multi-boundary
  authorisation architecture discharges all four obligations on the
  same party, with explicit boundary hand-offs at the
  authorisation-surface interfaces.
- **Scope caveat (CRITICAL — authorisation-surface divergence)** —
  derived from CRDA-deep verified classifications: the high-level
  SO does NOT collapse the four authorisation surfaces into a
  single authorisation surface. Personal-data-scope chain of
  authority, entity-side access-control policy, product-side
  authenticated-and-authorised boundary, and financial-entity-side
  ICT-asset access are **distinct authorisation surfaces** at
  **distinct boundaries**, with distinct triggers (instruction-bound
  processing vs entity AC duty vs product AC duty + triggered
  reporting vs financial-entity AC duty), distinct textual anchors,
  distinct threshold languages, and distinct evidence templates
  (instruction register + Art. 28(3)(a) contract vs access-control
  policy + role definitions vs Annex VII access-control records +
  Annex II §8 user-facing instructions vs entitlement inventory +
  access-review records + separation-of-duties attestation). A
  unified authorisation architecture may serve the technical
  substrate (e.g. an access-control platform with policy packages
  per surface), but the policy and evidence layers must remain
  **surface-segregated** for compliance demonstration. Phase 1A
  must therefore emit **four checks before applying the high-level
  SO** (one per participating regulation) to confirm that the
  per-reg authorisation surface, textual anchor, threshold
  language, and evidence template are documented separately; the
  high-level SO surfaces the common authorisation/least-privilege
  duty but does NOT aggregate the per-reg authorisation surfaces.
- **Scope caveat (CRITICAL — DORA `only` qualifier strictness)** —
  derived from CRDA-deep verified classifications: the DORA `only`
  qualifier is **strictly more demanding than CRA's `limited to
  authenticated and authorised`** and **more demanding than NIS 2's
  model-agnostic `access control policies`** — the financial entity
  must demonstrate that access is limited to legitimate AND approved
  functions and activities ONLY (Berry §5.3.1 — `only` correctly
  placed before the limiting phrase). For a party in DORA + NIS 2
  + CRA scope, the DORA `only` qualifier discharges the CRA
  `limited to authenticated and authorised` and the NIS 2
  `access control policies` when the same access-control substrate
  operates all three roles; the evidence layer must document which
  artefacts support which role with the DORA `only` qualifier
  recorded as the binding floor on the financial-sector overlap.
  For pure-financial entities (NIS 2 §9 fall-back does not apply —
  DORA is lex specialis), DORA absorbs the NIS 2
  entity-side-access-control obligation on the same artefact via lex
  specialis; the high-level SO does not aggregate across the
  lex-specialis boundary in that direction.
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA CRDA EQUAL correction)** —
  derived from CRDA-deep verified classifications: the CRDA
  initial EQUAL classification on NIS2↔DORA is **over-tight**; the
  OJ anchors differ (NIS 2's `access control policies` model-agnostic
  vs DORA's `legitimate and approved functions and activities
  only` with the literal `only` qualifier). The DORA `only`
  qualifier is operationally more demanding than NIS 2's
  model-agnostic framing (it closes off any access that is not
  strictly tied to a legitimate and approved function, while NIS 2's
  model-agnostic framing leaves the access-control model to entity
  discretion). CRDA-deep verified the relationship as
  **COMPLEMENTARY**, not EQUAL; the SR preserves this correction.
- **Scope caveat (CRITICAL — T-vs-text gaps on NIS 2 and DORA)** —
  derived from CRDA-deep verified classifications: T3 (NIS 2
  Art. 21(2)(i)) and T4 (DORA Art. 9(4)(c)) import best-practice
  vocabulary (`RBAC + need-to-know + least privilege` on T3;
  `need-to-know and least privilege` on T4) **not present in the OJ
  text**. The Executor preserves OJ-literal language in the SRs
  and maps to PR.AA-05 by meaning-alignment. Layer 2/3 should
  adjudicate whether the T-imposed best practice survives as
  interpretive continuation or whether the OJ-literal reading
  prevails. A readopting-the-T-vocabulary decision would tighten
  the high-level SO's threshold language across both regulations
  on the same party; for now, the OJ-literal reading is preserved
  per P5 vigilance on the source SR IDs.
- **Scope caveat (CRITICAL — CRA `possible unauthorised access`
  reporting)** — derived from CRDA-deep verified classifications:
  the CRA `possible unauthorised access reported` (Annex I Part I
  (2)(d)) is the **broadest visibility framing** across the four
  regulators; R1 inclusive reading treats `possible` as covering
  both successful and detected-but-failed attempts. The DE.CM-09
  monitoring + reporting dimension is **CRA-specific** and is not
  mirrored in GDPR / NIS 2 / DORA's authorisation obligations. For
  a party in CRA + GDPR + NIS 2 + DORA scope, the CRA visibility
  floor discharges the `appropriate and proportionate` reporting
  dimension on the same identity substrate; the evidence layer must
  document which artefacts support which role. R2 (any access
  attempt at all) overreaches the literal; R3 (specifically the
  failed-but-detected subset) under-reaches because successful
  breaches must also be reported; R1 is chosen.
---

## Emergent tensions (from CRDA-deep §D-03.3)

#### Emergent tensions (from CRDA-deep §D-03.3)
None — sub-domain is **all-COMPLEMENTARY** (6 pairs verified as
COMPLEMENTARY after OJ-text analysis; CRDA's initial EQUAL on
NIS2↔DORA corrected to COMPLEMENTARY after OJ-text analysis showing
the DORA `only` qualifier is operationally more demanding than NIS 2's
model-agnostic framing). No conditional emergent tensions on the
authorisation/least-privilege duty itself. The **authorisation-
surface divergence** (personal-data-scope / entity-side access-control
/ product-side authenticated-and-authorised / financial-entity-side
ICT-asset access) is the **legitimately diverse dimension**: each
regulator targets a distinct authorisation surface, and the
operational convergence is on a **multi-boundary authorisation
architecture** with explicit boundary hand-offs. The **textual-anchor
divergence** (GDPR `chain of authority` / NIS 2 `access control
policies` model-agnostic / CRA `limited to authenticated and
authorised users, services and hardware` + `possible unauthorised
access reported` + `limit attack surfaces` / DORA `legitimate and
approved functions and activities only` with literal `only`) is
**wording-only on a common substantive duty**; the **strictest
authorisation floor** (DORA `only`) discharges the looser ones on the
same party when the same access-control substrate operates both
roles. The **threshold-language divergence** (NIS 2 `appropriate and
proportionate` / CRA `commensurate with the identified cybersecurity
risk` / DORA `legitimate AND approved` + `only` qualifier) is
**wording-only on different operational anchors** that converge on
the same substantive least-privilege duty. The two **T-vs-text gaps**
on NIS 2 (T3 imports `RBAC + need-to-know + least privilege` not in
OJ) and DORA (T4 imports `need-to-know and least privilege` not in
OJ literal) are methodologically significant — the Executor
preserves OJ-literal language and maps to PR.AA-05 by meaning-
alignment; Layer 2/3 should adjudicate whether the T-imposed best
practice survives as interpretive continuation or whether the OJ-
literal reading prevails. The **scope-disjoint divergence** (NIS 2 §9
fall-back / DORA lex specialis on pure-financial entities) is
**handled by the lex-specialis carve-out** — DORA absorbs the NIS 2
entity-side-access-control obligation on pure-financial entities and
the high-level SO does not aggregate across the lex-specialis
boundary in that direction. The high-level SO surfaces the common
authorisation/least-privilege duty; the per-reg authorisation
surface, textual anchor, threshold language, evidence template, and
recipient are documented separately in the four sub-SOs and the
per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-03.3 — with
overlapping authorisation-surface scope-determiners on the same party
— operates a **multi-boundary authorisation architecture** with
explicit boundary hand-offs. The high-level SO (`SO-D-03.3.HL`)
describes the common authorisation/least-privilege duty (PR.AA-05 +
PR.AA-06 anchors; surface-segregated evidence); the per-reg
perspective is preserved in the four sub-SOs (authorisation surface,
textual anchor, threshold language, evidence template, recipient).
**No conflict-resolution is required on D-03.3 because CRDA-deep
verified all 6 pairs as COMPLEMENTARY on the authorisation/least-
privilege duty.** Phase 1C Doc 07 documents the **layered
authorisation strategy**: (1) a multi-boundary authorisation
architecture with explicit boundary hand-offs at the authorisation-
surface interfaces (personal-data-scope ↔ entity-side ↔ product-side
↔ financial-entity-side); (2) the DORA `only` qualifier as the
operative ceiling on the financial-entity overlap where DORA scope
applies; (3) the CRA `possible unauthorised access` reporting as the
strictest visibility floor where CRA scope applies; (4) the
lex-specialis carve-out for pure-financial entities (DORA absorbs
NIS 2; no aggregation across the boundary); (5) the OJ-literal
language preserved over the T3/T4-imported best-practice vocabulary
as the operative baseline. For proportionality (P2), a 5-FTE SaaS
with GDPR + CRA applicability may default to the CRA `limited to
authenticated and authorised` + `possible unauthorised access
reported` + `limit attack surfaces` triple as the highest common
denominator (DORA's `only` qualifier is out of scope unless the SaaS
scales to financial-entity size; NIS 2's `access control policies`
is out of scope unless the SaaS scales to essential-entity size); a
500-FTE DORA financial entity must additionally document the DORA
`legitimate and approved functions and activities only` discipline
with entitlement inventory + access-review records + separation-
of-duties attestation logs + physical-access audit trails per
`SR-DORA-010`; a DORA + NIS 2 cross-sector entity must document both
the DORA financial-entity-side `legitimate and approved only`
discipline AND the NIS 2 entity-side model-agnostic access-control
policy discipline with explicit boundary hand-offs between them and
the lex-specialis carve-out noted.

## Part 1 §3 — context

### 3. Security Requirements
## D-03.3 Authorisation — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md`. See that file for cross-reg verified relationships (6 pairs verified as **COMPLEMENTARY** — CRDA initial 1 EQUAL on NIS2↔DORA corrected to COMPLEMENTARY after OJ-text analysis showing DORA `only` qualifier is operationally more demanding; 5 SAME-COMPLEMENTARY; AI Act out-of-scope per AEGIS taxonomy §4.1), scope overlap matrix, Objective/Considerations content, authorisation-surface divergence (personal-data-scope chain of authority / entity-side access-control policy / product-side authenticated-and-authorised boundary + reporting + attack-surface / financial-entity-side legitimate-and-approved-only ICT-asset access), DORA `only`-qualifier strictness, CRA `possible unauthorised access` reporting breadth, T3/T4-vs-text gaps, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; no AI Act clause imposes an authorisation/least-privilege mandate; AI Act AIA-C11 cites Art. 12(4) which does not exist in OJ). CRDA-deep verified 6 pairs as all-COMPLEMENTARY (1 pair corrected from CRDA EQUAL on NIS2↔DORA to COMPLEMENTARY; 5 pairs CRDA-SAME-COMPLEMENTARY confirmed after OJ-text analysis). The four regulators target **different authorisation surfaces** at distinct textual anchors and distinct threshold languages (GDPR instruction-bound processing / NIS 2 model-agnostic access-control policy / CRA authenticated-and-authorised + `possible unauthorised access reported` + attack-surface-limitation / DORA `legitimate and approved functions and activities only` with the literal `only` qualifier); the high-level SO surfaces the common authorisation/least-privilege duty while preserving the per-reg authorisation surface — the four boundaries are layered, not collapsed.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 3.3
  volere_section: 15
  volere_subtype: access
  title: "Entitlements to act on the entity's systems, products, services, components and data managed per least privilege with explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between authorisation surfaces (multi-boundary authorisation architecture)"
  derives_from:
    hso_sub_so: SO-D-03.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.3.md
    objective_ref_section: "### D-03.3.0"
  description: |
    The product shall manage the entitlement to perform actions on the entity's systems, products, services, components and data per least privilege with an explicit authorisation-model choice, documented entitlements, attack-surface-limitation evidence, and boundary hand-offs between the four authorisation surfaces — personal-data-scope chain of authority (controller → processor → authorised persons), entity-side access-control policy, product-side authenticated-and-authorised boundary with possible-unauthorised-access reporting and attack-surface-limitation, and financial-entity-side ICT-asset access policy — as the common authorisation/least-privilege duty converging across GDPR Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b), NIS 2 Art. 21(2)(i) literal AND of access-control + HR-security + asset-management, CRA Annex I Part I (2)(d) + (2)(j) + (2)(l) reporting + attack-surface-limitation, and DORA Art. 9(4)(c) `legitimate and approved functions and activities only` with the literal `only` qualifier, where ≥2 of these authorisation-surface scope-determiners overlap on the same party.
  fit_criterion: |
    A multi-boundary authorisation architecture is operated with one authorisation-surface register per boundary (personal-data-scope instruction register, entity-side access-control policy + role definitions, product-side authenticated-and-authorised boundary + reporting + attack-surface-limitation register, financial-entity-side ICT-asset access policy + entitlement inventory + access-review records + separation-of-duties attestation logs + physical-access audit trails); explicit boundary hand-off protocols are documented at each authorisation-surface interface; the DORA `only` qualifier is the binding authorisation floor where the financial-entity-side stacks up on the same artefact with CRA product-side `limited to authenticated and authorised` or NIS 2 model-agnostic `access control policies`; the CRA `possible unauthorised access` R1 inclusive reading is the binding visibility floor where CRA stacks up on the same artefact with GDPR / NIS 2 / DORA; the OJ-literal `access control policies` is preserved over the T3/T4-imported `RBAC + need-to-know + least privilege` vocabulary per the model-agnostic reading; the lex-specialis carve-out discharges the NIS 2 obligation for pure-financial entities (DORA absorbs NIS 2; no aggregation across the boundary); verified by authorisation-surface register audit-trail inspection at all four boundaries + boundary hand-off-protocol documentation review + CRA Annex VII access-control framework inspection (when CRA in scope) + DPA / national-CA / CSIRT / MSA + ESA inspection-ready evidence packs on request.
  priority: MUST
  verification_method: TEST
  dependencies: [3.1 (identity substrate feeds the entitlement inventory at each authorisation surface)]
  nist_csf: [PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04, ID.AM-01, ID.AM-02, DE.CM-09]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs' authorisation surfaces overlap on the same party (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    All four participating regulations impose the same substantive authorisation/least-privilege duty anchored to PR.AA-05 (access permissions managed per least privilege); each targets a distinct authorisation surface at a distinct textual anchor and discharges through a distinct evidence template. The DORA `only` qualifier (Berry §5.3.1 — `only` correctly placed before the limiting phrase) is strictly more demanding than CRA's `limited to authenticated and authorised` and than NIS 2's model-agnostic `access control policies` — the binding floor on the financial-sector overlap. The CRA `possible unauthorised access reported` R1 inclusive reading (any successful + any detected-but-failed attempt) is the broadest visibility framing across the four regulators and is not mirrored in the other three — the strictest visibility floor and the pair to PR.AA-05 + PR.AA-06 in the SR-CRA-024 anchor. The two T-vs-text gaps (T3 imports `RBAC + need-to-know + least privilege` on NIS 2 Art. 21(2)(i); T4 imports `need-to-know and least privilege` on DORA Art. 9(4)(c)) are methodologically significant — the Executor preserves OJ-literal language and maps to PR.AA-05 by meaning-alignment, pending Layer 2/3 adjudication. The four authorisation surfaces are layered, not collapsed: a unified access-control platform may serve the technical substrate but the policy and evidence layers must remain surface-segregated for compliance demonstration. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so a single multi-boundary authorisation architecture discharges all four obligations on the same party, with explicit boundary hand-offs at the authorisation-surface interfaces. (Copied from the HSO Considerations block of `### D-03.3.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-03.3
title: D-03.3 Authorisation & Least Privilege — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.3 Authorisation & Least Privilege
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-03_Access-Control/D-03.3.md
status: DRAFT
---
> **Deep analysis:** [D-03.3 Authorisation & Least Privilege](../../DeepAnalysis/D-03_Access-Control/D-03.3.md)
#### D-03.3 Authorisation & Least Privilege
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-006 / SO-GDPR-011 | Persons authorised to process personal data act only on documented instructions + confidentiality | Controller/processor; Art. 28(3)(a)/(b) + Art. 29 + Art. 32(4); staff-side; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| NIS2 | SO-NIS2-003 (partial) | Access control policies + HR security + asset management (3 coordinated sub-domains) | Essential/important entity; Art. 21(2)(i); access-control + HR-security dimensions; PR.AA-01 + PR.AA-05 |
| CRA | SO-CRA-017 / SO-CRA-024 | Access to product with digital elements limited to authenticated and authorised users, services, hardware; possible unauthorised access reported; attack-surface limitation | Manufacturer; Annex I Part I (2)(d) + (2)(j); product-level; PR.AA-05 + PR.AA-06 + DE.CM-09 |
| DORA | SO-DORA-006 | Physical or logical access to information assets and ICT assets limited to what is required for legitimate and approved functions and activities only | Financial entity; Art. 9(4)(c); ICT-system scope; "legitimate and approved" AND + "only" qualifier (T4-vs-text gap — T4 reads RBAC + need-to-know + least privilege; OJ says only "legitimate and approved functions and activities only") |
| AI_Act | — | Out-of-scope (no authorisation mandate; CRA / NIS 2 / DORA sole authorities) | n/a |
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
- All four regulations impose an access-control obligation, but the **textual anchor** differs: GDPR `chain of authority controller → processor → authorised persons` (Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b)); NIS 2 `access control policies` model-agnostic (Art. 21(2)(i) — T3-vs-text gap, T3 imposes RBAC + need-to-know + least privilege not in OJ); CRA `limited to authenticated and authorised users, services, and hardware` (Annex I Part I (2)(d)); DORA `legitimate and approved functions and activities only` (Art. 9(4)(c) — T4-vs-text gap, T4 imposes `need-to-know and least privilege` not in OJ literal). The two **T-vs-text gaps** on NIS 2 and DORA are methodologically significant: T3/T4 import best-practice vocabulary not in the OJ text, and the Executor preserves OJ-literal language in the SRs. Layer 2/3 should adjudicate whether the T-imposed best practice survives as interpretive continuation or whether the OJ-literal reading prevails. P1 consequence: the differences in textual anchor produce different operational control architectures; a company across all four must reconcile the four anchors.
- **CRA's `report on possible unauthorised access`** (Annex I Part I (2)(d) "possible unauthorised access" — VAG S2) is the broadest framing: any unauthorised-access attempt that succeeds, plus any attempt detected even when it failed, falls within scope. GDPR's Art. 32(4) + Art. 29 chain-of-authority is the staff-side anchoring; NIS 2's Art. 21(2)(i) is the policy-level; DORA's Art. 9(4)(c) is the "legitimate and approved" framing. The reporting dimension is **CRA-specific** and is not mirrored in the other three regulations' authorisation obligations.
<!-- /emergent -->
##### SR cross-validation
CSF mappings converge on PR.AA-05 (access permissions managed per least privilege) for all four regulations, with PR.AA-06 (access limited to authorised users/services/hardware) as a shared anchor for GDPR and CRA. DORA additionally anchors on PR.AA-05 with the "only" qualifier; NIS 2 adds PR.AA-01 (identities managed) + PR.AT-02 (HR-security dimension). The shared PR.AA-05 + PR.AA-06 anchor is the operational pivot; divergence is at the supplementary layer (CRA DE.CM-09 monitoring; DORA's "only" qualifier on the access surface).
##### Downstream implication
For Phase 1C Doc 07, D-03.3 is a **layered access-control** sub-domain: a DORA financial entity with NIS 2 + CRA + GDPR scope operates a multi-layer access-control architecture with the DORA "only" qualifier as the most demanding floor. Proportionality: a small SaaS (no DORA, no NIS 2) meets the GDPR + CRA floor with documented instructions; a DORA financial entity must demonstrate the "only" qualifier with documented legitimate-and-approved function mappings for each access grant.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-03.3
title: D-03.3 Authorisation & Least Privilege — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.3 Authorisation & Least Privilege
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-03_Access-Control/D-03.3.md
status: DRAFT
---
> **Domain analysis:** [D-03.3 Authorisation & Least Privilege](../../DomainAnalysis/D-03_Access-Control/D-03.3.md)
#### D-03.3 Authorisation & Least Privilege
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
