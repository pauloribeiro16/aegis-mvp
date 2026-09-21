# D-03.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-03.2 Multi-Factor Authentication](../../CrossRegulation/DomainAnalysis/D-03_Access-Control/D-03.2.md)
#### D-03.2 Multi-Factor Authentication
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-03.2 Multi-Factor Authentication
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md`](../../CrossRegulation/DeepAnalysis/D-03_Access-Control/D-03.2.md)
> (6 pairs verified against OJ text — **all four participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope**).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-03.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-006 (cross-ref) / SO-GDPR-005 (cross-ref) | No explicit MFA mandate; staff-side via instructions + confidentiality (Art. 28(3)(b) + Art. 29); data-subject-side via Art. 12(6) verification | Controller/processor; no explicit MFA; PR.AA-05 + PR.AA-06 + PR.AT-02 |
| NIS 2 | SO-NIS2-004 | MFA or continuous authentication solutions "where appropriate" + secured voice/video/text + secured emergency | Essential/important entity; Art. 21(2)(j) first clause; "where appropriate" hedge; OR of MFA and continuous authentication (not redundant); PR.AA-03 + PR.AA-05 |
| CRA | SO-CRA-016 (partial) | Protection from unauthorised access via appropriate control mechanisms, which may include authentication, identity, or access-management systems (no explicit MFA mandate) | Manufacturer; Annex I Part I (2)(d); "including but not limited to" + 3-way OR (authentication / identity / access-management); PR.AA-01 + PR.AA-05 + PR.AA-06 + DE.CM-09 |
| DORA | SO-DORA-002 | Strong authentication mechanisms (T4 reads MFA; OJ says "strong authentication") | Financial entity; Art. 9(4)(d); dominant EBA Guidelines reading is MFA but OJ has no "multi-factor" phrase (T4-vs-text gap); PR.AA-03 + PR.AA-04 |

## Validated relationships (from CRDA-deep §D-03.2)

#### Validated relationships (from CRDA-deep §D-03.2)
All 6 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial classifications — **all 6 pairs initially marked COMPLEMENTARY**
were verified as SAME after OJ-text analysis). The underlying obligation
is the **same substantive authentication-mechanism duty** (ensuring that
the authentication event is sufficiently strong for the risk in scope);
the pairs differ on the **authentication explicitness in OJ text**, on
the **threshold anchor**, and on the **authentication target**. The four
regulators operate at four **different explicitness levels**:
- **GDPR** — no explicit MFA mandate. The OJ Art. 28(3)(b) + Art. 29
  obligations bind staff to instructions and confidentiality, and Art.
  12(6) governs data-subject verification at the rights-exercise
  endpoint, but neither clause imposes an authentication-strength
  threshold. GDPR supplies the **authorisation and confidentiality
  wrapper** for authentication mechanisms chosen at the controller's
  discretion; it does not name MFA.
- **NIS 2** — explicit MFA or continuous authentication "where
  appropriate" (Art. 21(2)(j) first clause). The OR admits both MFA
  and continuous-authentication as alternative authentication paradigms
  — they are not redundant — and the `where appropriate` hedge closes
  the sub-point. ENISA's 2022 baseline security recommendations list
  MFA as a default for all administrative and privileged access.
- **CRA** — "appropriate control mechanisms, which may include
  authentication, identity, or access-management systems" (Annex I Part
  I (2)(d)). The "including but not limited to" + 3-way OR
  (authentication / identity / access-management) admits MFA as one
  possible choice but does not impose it; the OJ text is **silent on
  MFA** and the CRA scope is **partial**. The T2-imposed `multi-factor
  or continuous authentication` reading is rejected because the OJ Annex
  I text does not contain these phrases.
- **DORA** — "strong authentication mechanisms" (Art. 9(4)(d)). The OJ
  text does not say "multi-factor"; the dominant EBA Guidelines
  reading on ICT and security risk management §145–§148 is MFA, but
  the literal OJ text admits other `strong` mechanisms. The T4-vs-text
  gap is **P0-flagged material reading-choice divergence** and is
  preserved in `SR-DORA-002` `ambiguity_notes`.
The authentication mechanisms are **not the same across the four
regulators in textual explicitness** but the authentication-mechanism
duty is the **same substantive obligation** — verified by CRDA-deep as
SAME after OJ-text analysis. There is no contradiction because no
clause forbids what another mandates; a single organisation across
all four regulators must operate a **layered authentication
architecture**, with the **most demanding floor (DORA's
strong-authentication)** discharging the **most permissive (CRA's
"may include")** on the same authentication event when both apply on
the same asset.
The scope-overlap column in the matrix below indicates whether the same
artefact can trigger both regulations on a single party; this is the
gating condition for the high-level SO to engage.
| | GDPR | NIS 2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Conditional (Y when controller is also NIS 2 entity; staff authentication event is the same trigger) | Conditional (Y when CRA product hosts staff- or data-subject-authentication endpoints) | Conditional (Y when DORA financial entity is also controller) |
| **NIS 2** | Conditional | — | Conditional (Y when NIS 2 entity deploys or manufactures CRA product) | Conditional (Y cross-sector entities; N pure-financial via lex specialis) |
| **CRA** | Conditional (Y integrated manufacturer-controller; product hosting the authentication endpoint) | Conditional (Y NIS 2 entity deploying CRA product) | — | Conditional (Y DORA financial entity deploying CRA product) |
| **DORA** | Conditional (Y DORA-controller) | Conditional (Y cross-sector; N pure-financial lex specialis) | Conditional (Y DORA deployer-side + CRA product-side) | — |
Legend: **Y** = scope overlap on a single artefact (high-level SO can
engage on a single party); **Conditional** = disjoint in baseline case, Y
on integrated-stack or vertical-integration scenario. CRDA-deep
scope-disjoint tests: GDPR↔NIS2 = Conditional (Y when controller is
also NIS 2 entity); GDPR↔CRA = Conditional (Y when CRA product hosts
authentication endpoints); GDPR↔DORA = Conditional (Y when DORA
financial entity is also controller); NIS2↔CRA = Conditional; NIS2↔DORA
= Conditional (Y cross-sector, N pure-financial lex specialis);
CRA↔DORA = Conditional. **All 6 pairs are Conditional**, reflecting
the layered authentication architecture pattern rather than the
identity-boundary-disjoint pattern of D-03.1.

## Cross-recipient map

#### Cross-recipient map
D-03.2 itself does **not** generate recipient asymmetry — the
authentication-mechanism architecture is inward-looking, with the
authentication event feeding downstream authorisation (D-03.3) and
audit-trail (D-10.2) sub-domains. The recipient fragmentation across
the four regulators is at the **compliance-demonstration point**:
GDPR's supervisory authority (Art. 32 confidentiality evidence on
authentication-strength audit), NIS 2's competent authority / CSIRT
(Art. 21(2)(j) authentication-policy evidence), CRA's market
surveillance authority (Annex VII technical documentation on
authentication-mechanism choice), and DORA's national competent
authority + ESAs (Art. 9(4)(d) strong-authentication-policy evidence
under the EBA Guidelines dominant MFA reading). These are distinct
regulatory channels but they do not generate the notification cascade
of D-04.3 — they are compliance-evidence channels on the same
authentication-mechanism architecture. The D-04.3 sub-domain is the
canonical recipient-fragmentation locus for the authentication-failure
notification dimension (when an authentication failure reaches the
incident-reporting threshold).
---

## HSO considerations (from D-03.2.0 — High-level SecurityObjective)

**Considerations.**
- All four participating regulations impose the same substantive authentication-mechanism duty but each anchors it to a distinct OJ-text explicitness level, a distinct threshold anchor, and a distinct authentication target: GDPR silent on authentication strength — staff-side via instructions + confidentiality (Art. 28(3)(b) + Art. 29), data-subject-side via verification (Art. 12(6)); NIS 2 explicit MFA or continuous authentication "where appropriate" (Art. 21(2)(j) first clause); CRA permissive "appropriate control mechanisms, may include authentication" (Annex I Part I (2)(d), no explicit MFA mandate — the "may include" reading is the literal OJ anchor); DORA demanding `strong authentication mechanisms based on relevant standards and dedicated control systems` (Art. 9(4)(d) — T4 reads MFA, OJ does not say MFA; dominant EBA Guidelines reading is MFA but the literal OJ reading admits other `strong` mechanisms; the T4-vs-text gap is P0-flagged in `SR-DORA-002` `ambiguity_notes`).
- The high-level SO describes the common authentication-mechanism duty (sufficient strength for the risk in scope, calibrated by the strictest applicable floor); the per-regulation perspective is preserved in the four sub-SOs (OJ explicitness, threshold anchor, authentication target, evidence template, recipient).
- DORA is the strictest anchor and discharges the other three on a single authentication event when DORA applies on the same party; for parties not within DORA scope, NIS 2's `where appropriate` (read with the risk-based Art. 21(1) factors) is the operative authentication-strength floor.
- CRA's "may include" is the product-side baseline; a CRA product implementing the NIS 2 MFA-floor or the DORA strong-authentication-floor exceeds the CRA requirement on the authentication dimension.
- GDPR is the silent surrounding wrapper — neither MFA-mandating nor MFA-prohibiting, supplying instructions + confidentiality + minimisation rather than authentication-strength threshold.
- The DORA T4-vs-text gap on `strong authentication` vs MFA is the operative reading-choice risk for financial entities: the dominant EBA Guidelines reading is MFA (R3), but a literal OJ reading admits other `strong` mechanisms (R5); the chosen reading in `SR-DORA-002` is mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory reading, pending the ESAs Joint Committee RTS under Art. 15.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-03.2 over a distinct
**authentication target** (the principal whose authentication is being
governed) and a distinct **OJ-text explicitness level**; the trigger,
the threshold anchor, the authentication target, the recipient, and
the legal anchor all depend on which scope the authentication event falls
into.
| Axis (reg) | OJ explicitness | Authentication target | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|---|
| **GDPR** | silent | staff (authorised persons) + data subjects (rights-request endpoint) | continuous (Art. 32(1)(b) confidentiality) + triggered (Art. 12(6) verification on reasonable doubt) | (no MFA threshold; instructions + confidentiality on staff-side; reasonable-means-proportionate on requester-side) | supervisory authority (compliance-evidence audit) | Art. 28(3)(b) + Art. 29 + Art. 12(6) |
| **NIS 2** | explicit (MFA or continuous) | staff + privileged access (entity workforce) | continuous (Art. 21(2) all-hazards) | `where appropriate` + Art. 21(1) factors (state of the art, costs, exposure, size, risk) | competent authority / CSIRT (entity governance audit) | Art. 21(2)(j) first clause |
| **CRA** | permissive (`may include authentication`) | product users + services + integrated components | continuous (operational lifetime) + risk-anchored | `appropriate control mechanisms … commensurate with identified cybersecurity risk` (Annex I Part I (2)(d)) | market surveillance authority (Annex VII technical documentation) | Annex I Part I (2)(d) |
| **DORA** | demanding (`strong authentication`) | financial-entity staff + service identities + machine identities | continuous (financial-entity operation) | `strong authentication mechanisms based on relevant standards and dedicated control systems` + Art. 6(8) appropriate level of independence | national competent authority + ESAs (EBA Guidelines dominant MFA reading) | Art. 9(4)(d) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-03.2.HL`) engages on a given authentication event **if and only
if ≥2 applicable regulations' authentication-target scope-determiners
overlap on the same authentication event** (e.g. staff-authentication
at a controller that is also a NIS 2 essential entity operating
CRA-regulated products and running DORA-class financial ICT — a
multi-floor authentication architecture on the same staff-credential
event). Pure co-applicability of disjoint-target regulations on
different authentication events does **not** trigger cross-regulation
aggregation — see the Activation logic in the file header. For a 5-FTE
SaaS startup with GDPR + CRA applicability but no NIS 2 / DORA
applicability, only the GDPR and CRA sub-SOs activate; the high-level
SO engages on the same authentication event if both apply, with the
GDPR silent-wrapper around the CRA product-user authentication choice.
**The four authentication-target scope-determiners are layered, not
collapsed**: staff-authentication (NIS 2, DORA) on top of data-subject
verification (GDPR) on top of product-user authentication (CRA). The
high-level SO surfaces the common authentication-mechanism duty but
does **NOT** aggregate the per-reg OJ explicitness, threshold anchors,
or evidence templates. **The DORA T4-vs-text gap on `strong
authentication` vs MFA is the operative reading-choice risk** for
financial entities; the chosen reading in `SR-DORA-002` is
mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory
reading, pending the ESAs Joint Committee RTS under Art. 15.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; AI Act is
  out-of-scope per AEGIS taxonomy §4 — no AI Act clause imposes an
  authentication-strength mandate; the AI Act threat model covers
  AI-specific attack categories handled in D-02.1, not D-03.2).
- 6 pairwise cells, verified by CRDA-deep as **all SAME** after
  OJ-text analysis: GDPR↔NIS2 (CORRECTED from COMPLEMENTARY),
  GDPR↔CRA (CORRECTED from COMPLEMENTARY), GDPR↔DORA (CORRECTED from
  COMPLEMENTARY), NIS2↔CRA (CORRECTED from COMPLEMENTARY),
  NIS2↔DORA (CORRECTED from COMPLEMENTARY), CRA↔DORA (CORRECTED from
  COMPLEMENTARY).
- The four regulations impose the **same substantive
  authentication-mechanism duty** but each anchors it to a distinct
  **OJ-text explicitness level** (GDPR silent / NIS 2 explicit /
  CRA permissive / DORA demanding), a distinct **threshold anchor**
  (none / `where appropriate` / `appropriate commensurate with risk` /
  `strong authentication based on relevant standards`), and a distinct
  **authentication target** (staff + data subjects / staff /
  product users + services + components / staff + service identities +
  machine identities). The strictest floor (DORA `strong authentication
  based on relevant standards` ≈ MFA via EBA reading) discharges the
  other three on the same authentication event when DORA applies on
  the same party; for parties not within DORA scope, the NIS 2
  `where appropriate` (read with Art. 21(1) factors) is the operative
  authentication-strength floor.
- The high-level SO describes the **COMMON OBJECTIVE** (sufficient
  authentication strength for the risk in scope, calibrated by the
  strictest applicable floor); the **per-regulation perspective**
  (OJ explicitness, threshold anchor, authentication target, evidence
  template, recipient) is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension —
  there are 0 conditional emergent tensions in this sub-domain;
  CRDA-deep verified all 6 pairs as SAME. Phase 1C Doc 07 does not
  need to resolve contradictions on D-03.2 because none exist on the
  authentication-mechanism duty itself; the task is to **stack the
  documentation** so that a single authentication-mechanism
  architecture (calibrated to the strictest applicable floor)
  discharges all four obligations on the same authentication event.
- **Scope caveat (CRITICAL — OJ-explicitness divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the four OJ-text explicitness levels into a single
  authentication-strength threshold. The four regulators do not impose
  the same OJ-text wording, and the per-reg evidence template must
  anchor to the per-reg threshold. The practical operational
  convergence is on a **single authentication-mechanism architecture**
  calibrated to the **DORA strong-authentication floor** when DORA
  applies, or to the **NIS 2 `where appropriate` floor** when only NIS
  2 + CRA + GDPR apply; the CRA "may include authentication" is the
  product-side permissive baseline that any NIS 2 or DORA
  authentication-mechanism choice exceeds; the GDPR silence is the
  surrounding wrapper that requires instructions + confidentiality on
  the staff-side and verification on the data-subject-side rather
  than authentication-strength threshold. The per-reg audit trail
  remains anchored to the per-reg threshold wording even when the
  operational deployment is unified.
- **Scope caveat (CRITICAL — DORA T4-vs-text gap)** — derived from
  CRDA-deep verified classifications: the high-level SO does NOT
  resolve the DORA `strong authentication mechanisms` vs `multi-factor
  authentication` reading-choice divergence. The OJ Art. 9(4)(d) text
  contains the phrase `strong authentication mechanisms` but not
  `multi-factor`; the dominant EBA Guidelines on ICT and security risk
  management §145–§148 reading is MFA, but the literal OJ reading
  admits other `strong` mechanisms (e.g. certificate-based
  authentication, hardware-token-only, PKI-bound device identity).
  The chosen reading in `SR-DORA-002` is **mechanism-agnostic (R5)
  with R3 (MFA) as the dominant EU supervisory reading**, and the
  T4-vs-text gap is **P0-flagged** in `SR-DORA-002` `ambiguity_notes`.
  The ESAs Joint Committee RTS under Art. 15 may eventually name
  specific authentication-strength standards (FIDO2/WebAuthn,
  NIST SP 800-63B AAL2/AAL3, ISO/IEC 27001 Annex A.10 or successor);
  until then, the financial entity should document the chosen reading
  and the rationale.
- **Scope caveat (CRITICAL — DORA lex specialis)** — derived from
  CRDA-deep verified classifications: the NIS 2 ↔ DORA pair is **NOT
  the same** relationship on cross-sector entities as on
  pure-financial entities. For pure-financial entities (NIS 2 §9
  fall-back does not apply to entities already covered by DORA in
  scope), DORA absorbs the NIS 2 authentication-strength obligation
  via lex specialis; the high-level SO does not aggregate across the
  lex-specialis boundary in that direction. For cross-sector entities,
  the NIS 2 entity-side `MFA or continuous authentication "where
  appropriate"` obligation layers on the DORA ICT-system strong
  authentication, and the high-level SO engages on the same
  authentication event with the DORA floor as the strictest anchor.
---

## Emergent tensions (from CRDA-deep §D-03.2)

#### Emergent tensions (from CRDA-deep §D-03.2)
None — sub-domain is **all-SAME in baseline (6 pairs verified as SAME
after OJ-text analysis; CRDA initial 6 COMPLEMENTARY classifications
corrected to SAME)**. No conditional emergent tensions on the
authentication-mechanism duty itself. The **OJ-explicitness divergence**
(GDPR silent / NIS 2 explicit `where appropriate` / CRA permissive
`may include` / DORA demanding `strong authentication based on
relevant standards`) is the **legitimately diverse dimension**: each
regulator names the authentication-strength threshold at a different
explicitness level, and the operational convergence is on a **layered
authentication-mechanism architecture** with the strictest applicable
floor (DORA `strong authentication`) discharging the loosest (CRA
"may include") on the same authentication event when both apply. The
**DORA T4-vs-text gap on `strong authentication` vs MFA is the
operative reading-choice risk** for financial entities — captured in
`SR-DORA-002` `ambiguity_notes` as the mechanism-agnostic R5 reading
with R3 (MFA) as the dominant EU supervisory reading. The
**target-scope divergence** (staff-authentication / data-subject
verification / product-user authentication / service-to-service
authentication) is **nested, not disjoint**: the four authentication
targets are layered (staff-auth subsumes data-subject verification at
the rights-request endpoint; product-user authentication feeds back
into staff-auth via deployment; service-to-service auth feeds into
product-user auth via integration). The **scope-disjoint divergence**
(NIS 2 §9 fall-back / DORA lex specialis on pure-financial entities)
is **handled by the lex-specialis carve-out** — DORA absorbs the NIS 2
authentication-strength obligation and the high-level SO does not
aggregate across the lex-specialis boundary in that direction. The
high-level SO surfaces the common authentication-mechanism duty; the
per-reg OJ explicitness, threshold anchor, authentication target, and
evidence template are documented separately in the four sub-SOs and
the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-03.2 — with
overlapping authentication-target scope-determiners on the same
authentication event — operates a **layered authentication-mechanism
architecture** calibrated to the **strictest applicable floor**. The
high-level SO (`SO-D-03.2.HL`) describes the common
authentication-mechanism duty (sufficient strength for the risk in
scope); the per-reg perspective is preserved in the four sub-SOs (OJ
explicitness, threshold anchor, authentication target, evidence
template, recipient). **No conflict-resolution is required on D-03.2
because CRDA-deep verified all 6 pairs as SAME on the
authentication-mechanism duty.** Phase 1C Doc 07 documents the
**layered authentication-mechanism strategy**: (1) a single
authentication-mechanism architecture calibrated to the **DORA
strong-authentication floor** when DORA applies (and where the
T4-vs-text gap is resolved by the chosen R5 mechanism-agnostic reading
with R3 MFA as the dominant supervisory expectation); (2) the **NIS 2
`where appropriate`** floor as the operative authentication-strength
threshold when only NIS 2 + CRA + GDPR apply (with the risk-based Art.
21(1) factors anchoring the proportionality test); (3) the **CRA
"may include"** as the product-side permissive baseline that any NIS 2
or DORA authentication-mechanism choice exceeds; (4) the **GDPR
silent-wrapper** of instructions + confidentiality + minimisation as
the surrounding obligation that does not impose an
authentication-strength threshold but does require the
authorisation + verification architecture; (5) the **lex-specialis
carve-out** for pure-financial entities (DORA absorbs NIS 2; no
aggregation across the boundary); (6) the **DORA T4-vs-text gap** as
the operative reading-choice risk pending the ESAs Joint Committee RTS
under Art. 15. For proportionality (P2), a 5-FTE SaaS with GDPR + CRA
applicability may default to the CRA `appropriate control mechanisms,
may include authentication` floor with the mechanism selection at the
manufacturer's discretion (no explicit MFA mandate; a single-factor
deployment is OJ-compliant under CRA but is not industry-state-of-
the-art per ENISA 2022 baseline); a 500-FTE DORA financial entity
must additionally document the **strong-authentication architecture
aligned with NIST SP 800-63B AAL2/AAL3** per the EBA Guidelines
dominant MFA reading, with the **PKI chain-of-trust** and
**identity-assertion integrity** anchored to PR.AA-04; a DORA + NIS 2
cross-sector entity must document both the DORA strong-authentication
floor AND the NIS 2 `where appropriate` MFA / continuous-authentication
choice, with the DORA floor as the strictest anchor discharging the
NIS 2 `where appropriate` test on the same authentication event.

## Part 1 §3 — context

### 3. Security Requirements
## D-03.2 Multi-Factor Authentication — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md`. See that file for cross-reg verified relationships (6 pairs verified as SAME — CRDA initial 6 COMPLEMENTARY corrected to SAME after OJ-text analysis), scope overlap matrix, Objective/Considerations content, OJ-explicitness divergence (GDPR silent / NIS 2 explicit `where appropriate` / CRA permissive `may include` / DORA demanding `strong authentication`), DORA T4-vs-text gap, DORA lex specialis carve-out, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; no AI Act clause imposes an authentication-strength mandate; the AI Act threat model covers AI-specific attack categories handled in D-02.1, not D-03.2). CRDA-deep verified 6 pairs as all-SAME (all 6 corrected from COMPLEMENTARY after OJ-text analysis). The four regulators anchor to distinct OJ-text explicitness levels, distinct threshold anchors, and distinct authentication targets; the high-level SO surfaces the common authentication-mechanism duty while preserving the per-reg anchor and threshold — the strictest applicable floor discharges the loosest on the same authentication event when both apply.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 3.2
  volere_section: 15
  volere_subtype: access
  title: "Authentication mechanism of sufficient strength for the risk in scope, calibrated by the strictest applicable floor (layered authentication architecture)"
  derives_from:
    hso_sub_so: SO-D-03.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md
    objective_ref_section: "### D-03.2.0"
  description: |
    The product shall authenticate users, services, and hardware that interact with the entity's systems, products, services, components and data through an authentication mechanism of sufficient strength for the risk in scope, with the strictest applicable floor discharging the most permissive on the same authentication event when both apply, as the common authentication-mechanism duty converging across GDPR Art. 28(3)(b) + Art. 29 + Art. 12(6) (silent on authentication strength — instructions + confidentiality + verification wrapper), NIS 2 Art. 21(2)(j) first clause (explicit MFA or continuous authentication `where appropriate`), CRA Annex I Part I (2)(d) (permissive `appropriate control mechanisms, may include authentication`), and DORA Art. 9(4)(d) (demanding `strong authentication mechanisms based on relevant standards`), where ≥2 of these authentication-target scope-determiners overlap on the same authentication event.
  fit_criterion: |
    A single authentication-mechanism architecture is operated, calibrated to the DORA strong-authentication floor when DORA applies on the same party (with the T4-vs-text gap resolved by the chosen R5 mechanism-agnostic reading and R3 MFA as the dominant EBA Guidelines §145–§148 supervisory expectation, pending the ESAs Joint Committee RTS under Art. 15 that may eventually name specific standards — FIDO2/WebAuthn, NIST SP 800-63B AAL2/AAL3); for parties not within DORA scope, the NIS 2 `where appropriate` floor (read with Art. 21(1) factors) is the operative authentication-strength threshold; the CRA `may include` is the product-side permissive baseline that any NIS 2 or DORA authentication-mechanism choice exceeds; the GDPR silent-wrapper around authentication (instructions + confidentiality + minimisation + verification) is the surrounding obligation that does not impose an authentication-strength threshold but does require the authorisation + verification architecture; the lex-specialis carve-out discharges the NIS 2 obligation for pure-financial entities (DORA absorbs NIS 2); verified by authenticator-inventory register audit + AAL-mapping documentation review + mechanism-strength calibration records + per-reg evidence templates (DPA / national-CA / CSIRT / MSA + ESA inspection-ready evidence packs) on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, ID.AM-01, PR.AT-02, DE.CM-09]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs' authentication-target scope-determiners overlap on the same authentication event (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive authentication-mechanism duty but each anchors it to a distinct OJ-text explicitness level, a distinct threshold anchor, and a distinct authentication target. The strictest floor (DORA `strong authentication based on relevant standards` ≈ MFA via EBA Guidelines reading) discharges the other three on the same authentication event when DORA applies on the same party; for parties not within DORA scope, the NIS 2 `where appropriate` (read with Art. 21(1) factors) is the operative authentication-strength floor; CRA's "may include" is the product-side permissive baseline; GDPR is the silent surrounding wrapper supplying instructions + confidentiality + minimisation + verification rather than authentication-strength threshold. The DORA T4-vs-text gap on `strong authentication` vs MFA is the operative reading-choice risk for financial entities — the chosen SR-DORA-002 reading is mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory reading pending the ESAs Joint Committee RTS under Art. 15. The four authentication-target scope-determiners are layered, not collapsed: staff-authentication (NIS 2, DORA) on top of data-subject verification (GDPR) on top of product-user authentication (CRA). The HL surfaces the common authentication-mechanism duty but does NOT aggregate the per-reg OJ explicitness, threshold anchors, or evidence templates. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so a single authentication-mechanism architecture (calibrated to the strictest applicable floor) discharges all four obligations on the same authentication event. (Copied from the HSO Considerations block of `### D-03.2.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-03.2
title: D-03.2 Multi-Factor Authentication — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.2 Multi-Factor Authentication
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-03_Access-Control/D-03.2.md
status: DRAFT
---
> **Deep analysis:** [D-03.2 Multi-Factor Authentication](../../DeepAnalysis/D-03_Access-Control/D-03.2.md)
#### D-03.2 Multi-Factor Authentication
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-005 (cross-ref) / SO-GDPR-006 (cross-ref) | No explicit MFA mandate; authentication of staff is captured by Art. 28(3)(b) + Art. 29 (instructions + confidentiality); authentication of data-subject requesters is captured by Art. 12(6) | Controller/processor; no explicit MFA; staff-side via Art. 28(3)(b) confidentiality obligation; data-subject-side via Art. 12(6) verification |
| NIS2 | SO-NIS2-004 | MFA or continuous authentication solutions "where appropriate" + secured voice/video/text communications + secured emergency communication systems | Essential/important entity; Art. 21(2)(j); "where appropriate" hedge; OR of MFA and continuous authentication (not redundant) |
| CRA | SO-CRA-016 (partial) | Protection from unauthorised access via appropriate control mechanisms, which may include authentication, identity, or access-management systems (no explicit MFA) | Manufacturer; Annex I Part I (2)(d); "including but not limited to" + 3-way OR (authentication / identity / access-management) — the "may include" creates the partial-coverage flag |
| DORA | SO-DORA-002 | Strong authentication mechanisms (T4 reads MFA; OJ says "strong authentication") | Financial entity; Art. 9(4)(d); dominant EBA Guidelines reading is MFA but T4-vs-text gap flagged (OJ has no "multi-factor" phrase); PR.AA-03 + PR.AA-04 |
| AI_Act | — | Out-of-scope (no MFA mandate; CRA / NIS 2 / DORA sole authorities) | n/a |
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
- The four regulations have **different MFA explicitness** in the OJ text: GDPR (no explicit MFA — staff-side via instructions + confidentiality, data-subject-side via verification); NIS 2 (explicit MFA or continuous authentication "where appropriate"); CRA ("appropriate control mechanisms, may include authentication" — no explicit MFA); DORA ("strong authentication mechanisms" — T4-vs-text gap, dominant EBA reading is MFA). A company across all four must reconcile four different textual anchors. The **practical floor** is: NIS 2's "where appropriate" is the most explicit, DORA's "strong authentication" (interpreted as MFA via EBA Guidelines) is the most demanding, CRA's "may include" is the most permissive, and GDPR's silence is the least demanding. A DORA financial entity with NIS 2 + CRA scope typically meets the most demanding floor (DORA strong-authentication ≈ MFA via EBA reading) and satisfies the other three.
- **T4-vs-text gap on DORA-C16** (Art. 9(4)(d) "strong authentication" vs T4 "Multi-Factor Authentication") is a P0-flagged material reading-choice divergence in `02_DORA_Ch2Sec2_Framework.md` and propagated to `02_SecurityRules_NIST.md` SR-DORA-002 `ambiguity_notes`. The chosen reading is mechanism-agnostic (R5) with R3 (MFA) as the dominant EU supervisory reading. Layer 2/3 should resolve whether the ESAs Joint Committee RTS under Art. 15 will name specific authentication-strength standards.
<!-- /emergent -->
##### SR cross-validation
CSF mappings converge on PR.AA-03 (users, services, and hardware authenticated) for the authentication event and PR.AA-05 (least privilege) for the post-authentication surface. CRA additionally maps to PR.AA-06 (access limited to authorised users/services/hardware) + DE.CM-09 (monitoring); DORA additionally maps to PR.AA-04 (identity assertions managed/protected/conveyed). The shared PR.AA-03 + PR.AA-05 anchor is the operational pivot; the supplementary layer (PR.AA-04, PR.AA-06, DE.CM-09) captures the depth of each regulator's authentication architecture.
##### Downstream implication
For Phase 1C Doc 07, D-03.2 is a **layered authentication** sub-domain: a DORA financial entity with NIS 2 + CRA + GDPR scope operates a multi-layer authentication architecture where DORA's strong-authentication is the floor, NIS 2's MFA/continuous authentication is the explicit mechanism, CRA's "may include" is the product-side choice, and GDPR's staff-side instructions + confidentiality surround the authentication. Proportionality: a small SaaS (no DORA, no NIS 2) operates at the CRA + GDPR floor with discretion on the mechanism; a DORA financial entity must meet the strong-authentication floor with documented risk-tiered factor strength.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-03.2
title: D-03.2 Multi-Factor Authentication — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-03 Access Control
sub_domain: D-03.2 Multi-Factor Authentication
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-03_Access-Control/D-03.2.md
status: DRAFT
---
> **Domain analysis:** [D-03.2 Multi-Factor Authentication](../../DomainAnalysis/D-03_Access-Control/D-03.2.md)
#### D-03.2 Multi-Factor Authentication
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

