# D-06.2 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-06.2 Software Bill of Materials (SBOM)](../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.2.md)
#### D-06.2 Software Bill of Materials (SBOM)
<!-- participants: CRA (sole authority) -->
**Participants (from CRDA):** CRA (sole authority)
**Sole-authority note:** GDPR, NIS2, DORA, and AI Act are all out-of-scope for D-06.2 per AEGIS taxonomy §4.1. CRA Annex I Part II (1) is the SOLE AUTHORITY for SBOM. This is the only sub-domain in Part C where CRA is the sole authority across all 5 regulations.
**Pairwise matrix:** No applicable pairs — only one participant (CRA).
**NIST CSF 2.0 anchoring via ID.AM-02** (Inventories of software platforms and applications). CRA maps ID.AM-02 via SR-CRA-008 (machine-readable format) and SR-CRA-052 (top-level dependencies) and SR-CRA-053 (technical documentation). Single-regulation; CSF mapping is consistent. The CRA Annex II §9 SBOM access location (optional user access) is not separately mapped by CSF 2.0; it is a product-instruction construct.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a single-track SBOM obligation per CRA. Phase 3 case generation must validate that CRA-classified case companies produce and maintain an SBOM covering top-level dependencies in a commonly used machine-readable format (e.g., SPDX or CycloneDX). The Annex VII §8 MSA-disclosure obligation is an institutional hook, not an operational requirement; case companies do not need to provide the SBOM to users by default (Annex II §9 is optional).
---

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-06.2 Software Bill of Materials (SBOM)
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.2.md`](../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.2.md)
> (**0 pairs verified against OJ text — 1 of 5 participating
> regulation is CRA — SOLE AUTHORITY** as noted by
> `DomainAnalysis/D-06_Supply-Chain/D-06.2.md` line 36: "GDPR,
> NIS2, DORA, and AI Act are all out-of-scope for D-06.2 per AEGIS
> taxonomy §4.1. CRA Annex I Part II (1) is the SOLE AUTHORITY for
> SBOM. This is the only sub-domain in the D-06 Supply-Chain folder
> where CRA is the sole authority across all 5 regulations").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-06.2)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-038 | Manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies; on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements | Product with digital elements; manufacturer SBOM; Art. 3(39) SBOM definition + Annex I Part II (1) SBOM + Art. 13(24) Commission implementing acts on SBOM format + Annex II §9 SBOM optional user access + Annex VII §2(b) SBOM in technical documentation + Annex VII §8 SBOM on MSA reasoned request; ID.AM-02 + GV.SC-02 + GV.SC-03 |
| GDPR | — (out-of-scope) | No SBOM mandate in GDPR; CRA sole authority per AEGIS taxonomy §4.1 | n/a |
| NIS2 | — (out-of-scope) | No SBOM mandate in NIS 2; CRA sole authority per AEGIS taxonomy §4.1 | n/a |
| DORA | — (out-of-scope) | No SBOM mandate in DORA Art. 28; DORA's Art. 24(4) SBOM cross-ref applies to digital operational resilience testing, not to the Annex I Part II (1) SBOM; CRA is the sole authority | n/a |
| AI_Act | — (out-of-scope) | No SBOM mandate in AI Act; CRA sole authority per AEGIS taxonomy §4.1 | n/a |
**Sole-authority framing.** The CRDA-deep source-of-truth explicitly
notes that **GDPR, NIS 2, DORA, and AI Act are all out-of-scope for
D-06.2** per AEGIS taxonomy §4.1. CRA Annex I Part II (1) is the
**SOLE AUTHORITY** for the manufacturer-side SBOM obligation. The
NSD (formal record containing details and supply-chain
relationships of the components included in the software elements
of the product, per Art. 3(39) on the SBOM definition) is a
manufacturer-side architectural artefact under Art. 13(1) design-
time + Annex I Part II (1) identification-and-documentation duty,
documented in Annex VII §2(b) technical documentation, optional
for user-facing access under Annex II §9, and disclosed to MSAs on
reasoned request under Annex VII §8. GDPR may have an architectural
soft-touch with the SBOM via `SR-GDPR-032` `commonly used` ambiguity
in Art. 15(3) (the portable-format duty under Art. 15(3) requires
`commonly used electronic form`, and the cross-pollination from the
SBOM machine-readable-format selection may inform the portability
format selection) — but `commonly used` is **undefined** in the
GDPR OJ text and is not an SBOM mandate. The CRA mechanism is the
**sole authority** on D-06.2, and the 1 sub-SO (CRA) is the entire
regulatory surface of D-06.2.

## Validated relationships (from CRDA-deep §D-06.2)

#### Validated relationships (from CRDA-deep §D-06.2)
**No pairwise cells** — single-participant sub-domain. The NSD per
Art. 3(39) is a formal record where the manufacturer documents **at
minimum the top-level dependencies of the product** (per Annex I
Part II (1) `covering at least the top-level dependencies` floor) in
a **commonly used and machine-readable format** (per Annex I Part II
(1) format requirement; per `SR-CRA-008` ambiguity_notes, the
POLY-S3 + VAG-S3 reading is **R3** — "any commonly-used machine-
readable format that supports automated component identification,"
pending the Commission implementing acts under Art. 13(24)). The
SBOM obligation operates across three operational anchors: **(1)
authoring** (Annex I Part II (1) — the manufacturer draws up the
SBOM at product release); **(2) retention** (Annex VII §2(b) —
the SBOM is included in the technical documentation, surviving the
Annex VII §4 retention period of 10 years or support period,
whichever is longer, per Art. 13(13) + Art. 13(9) 10-year tail);
**(3) regulatory disclosure** (Annex VII §8 — on a reasoned request
from an MSA, the SBOM is provided where necessary for the authority
to check compliance with the Annex I cybersecurity requirements;
the `where necessary` scope is the subset of the SBOM directly
relevant to the compliance question under investigation, per
`SR-CRA-053` VAG-S2 R1 reading — not a comprehensive dump of every
component). The Annex II §9 user-access provision is **optional**
under R1 reading per `SR-CRA-053` (manufacturer's discretion whether
to publish the SBOM externally; the obligation is only to include
it in the technical documentation under Annex VII §2(b)). The
Commission implementing acts under Art. 13(24) authorise further
specification of the format and elements of the SBOM — a forward-
looking clause that anticipates standardisation work (CEN/CENELEC
under Art. 27 + Recital 60 on harmonised standards) and may raise
the floor from the current `top-level dependencies` minimum.
The NSD architecture is **single-regulator** — the CRA sub-SO
captures the **full regulatory surface** (Art. 3(39) definition +
Annex I Part II (1) authoring + Annex VII §2(b) retention + Annex
II §9 optional user access + Art. 13(24) Commission implementing
acts + Annex VII §8 MSA reasoned request). The high-level SO and
the CRA sub-SO both describe the same obligation at different
abstraction levels, and the high-level SO is **redundant in this
single-regulator case** (per the activation model in
`../../index.md` lines 32–42 — `1 reg applicable → use that reg's
sub-SO directly; the high-level SO is redundant in this case but
is still emitted for traceability`).

## Cross-recipient map

#### Cross-recipient map
D-06.2 generates recipient asymmetry between the **operational
artefact** (the SBOM as the manufacturer-side component-
identification record) and the **downstream compliance-demonstration
point**: **CRA's market surveillance authority (MSA)** on the
Annex VII §2(b) technical-documentation evidence (the SBOM in the
conformity-assessment record, surviving the Annex VII §4 retention
period) and on the Annex VII §8 reasoned-request pathway (the
SBOM-on-request capability that closes the loop between private
inventory and third-party-verifiable compliance); the **CRA-side
** user / integrator / researcher as the optional recipient of the
Annex II §9 user-facing SBOM disclosure (manufacturer's discretion
whether to publish); the **CRA-side** importer / distributor as the
downstream-of-manufacturer recipient of the SBOM-related Annex VII
§1–§2 records under Art. 19/20 (importer / distributor see Annex VII
on reasoned request but do not necessarily see the SBOM directly
under Annex II §9). The Annex VII §8 MSA-disclosure obligation is an
**institutional hook**, not an operational requirement; case
companies do not need to provide the SBOM to users by default
(Annex II §9 is optional). **The SBOM is the upstream**
component-identification artefact that feeds **D-06.1** (component
due diligence under SR-CRA-050), **D-02.1** (vulnerability
identification under SR-CRA-007), **D-02.2** (vulnerability
remediation + addressing the component vulnerabilities identified by
the SBOM under SR-CRA-008 + SR-CRA-010), and **D-09.4** (technical
documentation under SR-CRA-059). **D-06.3** (contractual security
obligations) consumes the SBOM-related Annex VII §1–§2 records as
part of the conformity-assessment record but does not address the
SBOM duty itself.
---

## HSO considerations (from D-06.2.0 — High-level SecurityObjective)

**Considerations.**
- Only 1 regulator participates (CRA is the SOLE AUTHORITY per AEGIS taxonomy §4.1); GDPR, NIS 2, DORA, AI Act are all out-of-scope. The high-level SO and the CRA sub-SO describe the same obligation at different abstraction levels, and the activation model treats the high-level SO as redundant in this single-regulator case but still emits it for traceability.
- The format-floor POLY-S3 is resolved to R3 (any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24)); the depth-floor POLY-S2 is resolved to R1 (first-level direct dependencies with depth-1 look-through, per SR-CRA-052); the `where necessary` MSA-disclosure scope POLY-S2 is resolved to R1 per SR-CRA-053 (necessary subset directly relevant to the compliance question).
- The soft-touch cross-pollination with SR-GDPR-032 `commonly used` ambiguity in Art. 15(3) is a format-selection-layer architectural support — the CRA-side SBOM format choice and the controller-side GDPR Art. 15(3) portability format choice may share infrastructure (e.g. a single data-catalog machinery) but the two obligations are not the same and the GDPR obligation is data-subject-right-bound while the CRA obligation is manufacturer-side-bound.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 1 participating regulation defines D-06.2 over a single
**artefact layer** of the SBOM architecture; the trigger, the
format anchor, the depth anchor, the retention anchor, and the
disclosure anchor all depend on which step of the three-anchored
SBOM lifecycle (authoring, retention, regulatory disclosure) is
engaged.
| Axis (reg) | Step | Trigger | Format anchor | Depth anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|---|
| **CRA** | authoring (Annex I Part II (1)) | product release + ongoing through support period under Art. 13(8) (per Annex VII §2(b) survival) — CONTINUOUS | `commonly used and machine-readable format` (POLY-S3 R3 per `SR-CRA-008`; pending Art. 13(24) Commission implementing acts) | `top-level dependencies` minimum (POLY-S2 R1 per `SR-CRA-052` — first-level direct dependencies with depth-1 look-through; depth-discretionary beyond the floor) | manufacturer (author) → technical-documentation bundle (Annex VII §2(b) destination) | Art. 3(39) SBOM definition + Annex I Part II (1) SBOM authoring + Art. 13(1) design-time + Art. 13(7) all-cybersecurity-aspects documentation + Art. 13(8) sentence 1 support-period handling + Art. 13(13) 10-year retention + Annex VII §2(b) |
| **CRA** | retention (Annex VII §2(b)) | continuing technical-documentation maintenance under Annex VII §4 retention | (same format as authoring) | (same depth as authoring; versioning tracks dependency changes) | market surveillance authority (MSA) on reasoned request | Annex VII §2(b) + Annex VII §4 retention (10 years or support period, whichever is longer) + Art. 13(13) + Art. 13(9) |
| **CRA** | regulatory disclosure (Annex VII §8) | MSA reasoned request | (same format as authoring — the SBOM is provided in the same machine-readable format) | `where necessary` scope (POLY-S2 R1 per `SR-CRA-053` — necessary subset of SBOM directly relevant to the compliance question under investigation) | market surveillance authority (MSA) | Annex VII §8 + Art. 13(22) MSA cooperation + Art. 13(4) sentence 1 risk assessment included in technical documentation |
| **CRA (optional, no separate sub-SO)** | user-facing access (Annex II §9) | manufacturer's discretion under Annex II §9 `if the manufacturer decides to make available` | (same format as authoring) | (manufacturer's discretion on depth — typically mirrors the authoring depth) | user / integrator (optional disclosure) | Annex II §9 + Art. 13(18) 10-year information accessibility + Art. 13(1) design-time |

## Scope-overlap matrix (1×1)

#### Scope-overlap matrix (1×1)
| | CRA |
|---|---|
| **CRA** | — |
Legend: **N/A** = no scope question for the self-pair (single-participant sub-domain). CRDA-deep scope-disjoint test: not applicable (no pairs to test).

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-06.2.HL`) engages on a given party **only when CRA is in
`applicable_regs`** (i.e., the party is a CRA-bound manufacturer of
products with digital elements placed on the Union market). Because
only 1 regulator participates on D-06.2, the high-level SO does
**not** aggregate cross-regulation surface; it serves as the
**traceability artefact** for the common SBOM duty in the single-
regulator case (per the activation model in `../../index.md` lines
32–42 — `1 reg applicable → use that reg's sub-SO directly; the
high-level SO is redundant in this case but is still emitted for
traceability`). For a 5-FTE SaaS startup that is a CRA-bound
manufacturer placing a product with digital elements on the Union
market, **the CRA sub-SO activates and the high-level SO is
emitted for traceability**; the manufacturer draws up the SBOM at
product release, includes it in the technical documentation under
Annex VII §2(b), retains it through the support period under Annex
VII §4, and discloses it to MSAs on reasoned request under Annex
VII §8. For an importer or distributor placing the product on the
market (Art. 19 + Art. 20), the SBOM is **not directly
transferred** under Annex II §9 (manufacturer's discretion); the
importer / distributor see the SBOM-related Annex VII records on
reasoned request under their own surveillance obligations but the
SBOM duty itself does not duplicate on the importer / distributor
(they inherit the manufacturer's CRA-side SBOM record by reference
in the conformity-assessment bundle).

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 1 of 5 regulations participates (CRA is the SOLE AUTHORITY for
  D-06.2 per AEGIS taxonomy §4.1; GDPR, NIS 2, DORA, AI Act are
  out-of-scope).
- 0 pairwise cells — single-participant sub-domain.
- No CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY classifications
  by construction (single regulator).
- The CRA sub-SO captures the **full regulatory surface** (Art.
  3(39) SBOM definition + Annex I Part II (1) SBOM authoring +
  Annex VII §2(b) technical-documentation retention + Annex II §9
  optional user access + Art. 13(24) Commission implementing acts +
  Annex VII §8 MSA reasoned request).
- The high-level SO does **NOT** resolve any conditional tension —
  there are **0 conditional emergent tensions** in this sub-domain
  (single regulator; no 3-way interaction surface; the format POLY
  ambiguity and the depth POLY ambiguity are inside-CRA and are
  resolved per `SR-CRA-008` and `SR-CRA-052` respectively; the
  `where necessary` scope POLY ambiguity is resolved per
  `SR-CRA-053`). Phase 1C Doc 07 does not need to resolve
  contradictions on D-06.2 because none exist by construction.
- **Scope caveat (CRITICAL — sole-authority scope framing)** —
  derived from CRDA-deep verified classifications: the D-06.2
  sub-domain is **single-regulator** — CRA Annex I Part II (1) is
  the sole authority for the manufacturer-side SBOM obligation. For
  a CRA-bound manufacturer in `applicable_regs`, the CRA sub-SO
  activates and the high-level SO is emitted for traceability
  (redundant in the single-regulator case per the activation
  model). For a party with CRA out of `applicable_regs` (no CRA
  scope — e.g. a non-EU manufacturer not placing products with
  digital elements on the Union market; a service-only entity that
  is not a manufacturer of products with digital elements; an
  importer / distributor that does not independently draw up an
  SBOM but inherits the manufacturer's Annex VII records), the CRA
  sub-SO does NOT activate and no sub-SO substitutes. Phase 1A
  must therefore emit **one check before applying the high-level
  SO** — confirming that CRA is in `applicable_regs` AND the party
  is a manufacturer of products with digital elements — and must
  NOT synthesise a GDPR-or-other-reg sub-SO on D-06.2 from the
  soft-touch cross-pollination (`SR-GDPR-032` `commonly used`
  ambiguity in Art. 15(3) is not an SBOM mandate).
- **Scope caveat (CRITICAL — three-anchored SBOM architecture)** —
  derived from CRDA-deep verified classifications: the SBOM duty
  operates across three operational anchors — **authoring** (Annex
  I Part II (1)), **retention** (Annex VII §2(b) + Annex VII §4),
  and **regulatory disclosure** (Annex VII §8). For a CRA-bound
  manufacturer, all three anchors must be satisfied; the SBOM must
  be **(1)** drawn up at product release in a commonly used and
  machine-readable format covering at least the top-level
  dependencies; **(2)** retained in the technical documentation
  through the support period and the 10-year tail; **(3)**
  disclosed to MSAs on reasoned request where necessary for
  compliance checking. The Annex II §9 user-facing access is a
  fourth **optional** anchor under manufacturer's discretion; it is
  not a separate obligation and does not duplicate the SBOM duty.
  For a 5-FTE SaaS startup, the three anchors are discharged with
  a documented Annex VII §2(b) artefact bundle + an MSA-request
  log + an updated SBOM across the support period; the optional
  Annex II §9 user-facing access is at manufacturer's discretion.
- **Scope caveat (CRITICAL — format POLY ambiguity pending
  Commission implementing acts)** — derived from CRDA-deep
  verified classifications: the `commonly used and machine-readable
  format` phrase (Annex I Part II (1) + Art. 13(24) Commission
  implementing acts) is POLY-S3 + VAG-S3 with three materially
  distinct readings per `SR-CRA-008` `ambiguity_notes` —
  **R1** (a specific sector format such as SPDX or CycloneDX
  anchored as the OJ-mandated format); **R2** (a different
  specific sector format as the OJ-mandated format); **R3** (any
  commonly-used machine-readable format that supports automated
  component identification, pending the implementing acts).
  The chosen reading is **R3** — the implementing-acts-dependent
  choice lets manufacturers pick what interoperates best with their
  tooling while preparing for the eventual binding specification.
  An additional **R5** reading (domain-agnostic cryptographic
  manifest that any SBOM-aware toolchain can ingest) is admitted
  as the long-run consensus direction but rejected for current OJ
  reading because Annex I Part II (1) does not specify such a
  manifest, leaving the implementing-acts route to harmonise. The
  format choice is documented in the conformity dossier under
  Annex VII §2(b); the manufacturer migrates when the implementing
  acts specify a binding format.
- **Scope caveat (CRITICAL — depth POLY ambiguity top-level floor)**
  — derived from CRDA-deep verified classifications: the
  `top-level dependencies` phrase (Annex I Part II (1)) is
  POLY-S2 with three materially distinct readings per
  `SR-CRA-052` `ambiguity_notes` — **R1** (first-level direct
  dependencies with depth-1 look-through — the OJ-literal floor);
  **R2** (full transitive closure — operationally heavier than the
  OJ text requires); **R3** (critical-path-only — would let
  vendors omit categories that may matter under coordinated
  vulnerability disclosure timelines). The chosen reading is
  **R1** — first-level direct dependencies with depth-1 look-
  through — honouring the OJ literal `at the very least the
  top-level dependencies` without forbidding deeper SBOMs at the
  manufacturer's discretion. The Annex I Part II (1) is the
  **floor**, not the ceiling; the manufacturer's discretion to
  include deeper dependencies is preserved (and may be encouraged
  in specific sectors where R2 or R3 is industry-standard). The
  Annex I Part II (1) floor is not strictly full-transitive; the
  implementing-acts route under Art. 13(24) may raise the floor
  for specific product categories.
- **Scope caveat (CRITICAL — `where necessary` MSA-disclosure
  scope POLY)** — derived from CRDA-deep verified classifications:
  the Annex VII §8 phrase `where necessary in order for that
  authority to be able to check compliance` is VAG-S2 — necessary
  to what scope? The chosen reading per `SR-CRA-053` is **R1** —
  `necessary` is the subset of the SBOM directly relevant to the
  compliance question under investigation, not a comprehensive dump
  of every component. The alternative reading R2 (full SBOM
  disclosure without scope filter) would over-disclose proprietary
  supply-chain relationships unrelated to the question and create
  an IP tension that Annex VII §8 does not require. The
  manufacturer documents the scope decision in the MSA-request log
  and discloses the relevant subset in a prompt-and-differentiated
  manner.
- **Scope caveat (CRITICAL — format choice must remain operational
  across SBOM-toolchain updates)** — derived from CRDA-deep verified
  classifications: the SBOM must be operational across the support
  period + 10-year tail, and the format choice must remain
  **machine-readable in tooling that survives** the support period.
  Format choices that depend on proprietary tooling without an open
  parser are not `commonly used and machine-readable` (the R3
  reading per `SR-CRA-008` excludes single-vendor or single-tool
  formats that lack a published specification). The manufacturer's
  SBOM is documented in the technical documentation with the format
  choice rationale and the open parser reference.
---

## Emergent tensions (from CRDA-deep §D-06.2)

#### Emergent tensions (from CRDA-deep §D-06.2)
**0 conditional emergent tensions** — single-regulator sub-domain.
The 0 pairwise cells mean there is no cross-regulation aggregation
surface on D-06.2; there is no CONTRADICTORY pair (single
regulator by construction); there is no SCOPE-DISJOINT pair (single
regulator by construction); there is no CORRECTED pair (single
regulator by construction). The SBOM architecture is **single-
regulator** — the CRA sub-SO captures the full regulatory surface
(Art. 3(39) definition + Annex I Part II (1) authoring + Annex VII
§2(b) retention + Annex II §9 optional user access + Art. 13(24)
Commission implementing acts + Annex VII §8 MSA reasoned request).
The format POLY-S3 ambiguity + the depth POLY-S2 ambiguity + the
`where necessary` scope POLY-S2 ambiguity are **inside-CRA** and
are resolved per `SR-CRA-008` + `SR-CRA-052` + `SR-CRA-053`
respectively; they do not generate a cross-regulation emergent
tension.
The soft-touch cross-pollination with `SR-GDPR-032` `commonly used`
ambiguity in Art. 15(3) — where the portable-format duty under
Art. 15(3) requires `commonly used electronic form`, and the cross-
pollination from the SBOM machine-readable-format selection may
inform the portability format selection — is **not a regulatory
pair** for D-06.2 purposes. It is an architectural support at the
format-selection layer where the manufacturer's CRA-side SBOM
format choice and the controller-side GDPR Art. 15(3) portability
format choice may share infrastructure (e.g., a single data-
catalog machinery that serves both the SBOM and the portability
export), but the GDPR obligation is data-subject-right-bound and
the CRA obligation is manufacturer-side-bound. The two are not the
same obligation; the architectural support does not generate a
D-06.2 sub-SO on the GDPR side and does not generate an emergent
tension.
The high-level SO is honesty-preserving about scope-disjointness —
because only 1 regulator participates, the high-level SO and the
CRA sub-SO describe the same obligation at different abstraction
levels, and the activation model treats the high-level SO as
redundant in this single-regulator case but still emits it for
traceability. The per-reg perspective (format anchor, depth
anchor, retention anchor, disclosure anchor, legal anchor) is
preserved verbatim in the 1 sub-SO.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with CRA in `applicable_regs` (i.e., a CRA-bound
manufacturer of products with digital elements placed on the Union
market) operates the **three-anchored + optional fourth SBOM
architecture** with explicit operational anchors (authoring,
retention, regulatory disclosure, optional user access). The high-
level SO (`SO-D-06.2.HL`) describes the common SBOM duty (the
manufacturer draws up and maintains an SBOM in a commonly used and
machine-readable format covering at least the top-level
dependencies, with format flexibility pending the Commission
implementing acts under Art. 13(24) and `where necessary` MSA-
disclosure scope per Annex VII §8 + SR-CRA-053). The per-reg
perspective is preserved in the 1 sub-SO (format anchor, depth
anchor, retention anchor, disclosure anchor, legal anchor). **The
0 conditional emergent tensions are documented as a single-
regulator architecture** with inside-CRA POLY ambiguities resolved
per `SR-CRA-008` + `SR-CRA-052` + `SR-CRA-053`, and the soft-touch
cross-pollination with `SR-GDPR-032` `commonly used` is **not a
regulatory pair** but a format-selection-layer architectural
support. Phase 1C Doc 07 documents the **SBOM strategy**: (1) the
three-anchored SBOM architecture (authoring + retention +
regulatory disclosure); (2) the Annex I Part II (1) `top-level
dependencies` floor with depth-discretionary SBOMs above the floor;
(3) the R3 format-choice reading pending Art. 13(24) implementing
acts, with format-choice rationale documented in the conformity
dossier; (4) the Annex VII §2(b) technical-documentation inclusion
surviving the Annex VII §4 retention period (10 years or support
period, whichever is longer); (5) the Annex VII §8 MSA reasoned-
request pathway with `where necessary` scope (POLY-S2 R1 reading —
necessary subset directly relevant to the compliance question);
(6) the optional Annex II §9 user-access pathway at manufacturer's
discretion (R1 — no obligation to publish the SBOM externally);
(7) the upstream→downstream SBOM propagation to D-06.1 (CRA Art.
13(5) component due diligence consumes the SBOM), D-02.1
(SR-CRA-007 vulnerability identification consumes the SBOM for
CVE matching), D-02.2 (SR-CRA-008 + SR-CRA-010 vulnerability
remediation addresses the component vulnerabilities), and D-09.4
(SR-CRA-059 Annex VII technical-documentation bundle includes the
SBOM as the §2(b) artefact); (8) the institutional hook of the
Annex VII §8 MSA-disclosure pathway (closing the loop between the
private SBOM and the public MSA-verifiable compliance path);
(9) the optional trust-signal lever of the Annex II §9 user-access
pathway at manufacturer's discretion (commonly used for the
nutritional-label analogy); (10) the format-migration posture when
the Commission implementing acts under Art. 13(24) specify a
binding format — the manufacturer documents the migration plan and
updates the SBOM to the new format with versioning evidence across
the support period. For proportionality (P2), a 5-FTE SaaS startup
with CRA applicability may default to the Annex I Part II (1)
`top-level dependencies` floor with a documented R3 format
choice (any commonly-used machine-readable format) — the
format-selection toolchain depends on the manufacturer's build
system; the Annex VII §2(b) technical-documentation bundle is the
conformity-assessment record; the Annex VII §8 MSA-disclosure
pathway is exercised on reasoned request under the `where
necessary` scope; the optional Annex II §9 user-access is at
the manufacturer's discretion (typically NOT enabled for B2B
products but enabled for consumer products as a trust-signal lever).
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-06.2 Software Bill of Materials (SBOM) — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.2.md`. See that file for cross-reg verified relationships (**0 pairs verified against OJ text — 1 of 5 participating regulation is CRA — SOLE AUTHORITY** per AEGIS taxonomy §4.1; GDPR, NIS 2, DORA, AI Act are all out-of-scope), the three-anchored SBOM architecture (authoring / retention / regulatory disclosure + optional user access), Objective/Considerations content, the format POLY-S3 (R3 reading per SR-CRA-008 pending Art. 13(24) Commission implementing acts), the depth POLY-S2 (R1 reading per SR-CRA-052 — first-level direct dependencies with depth-1 look-through), the `where necessary` MSA-disclosure scope POLY-S2 (R1 reading per SR-CRA-053 — necessary subset directly relevant to the compliance question), and the format-choice-must-remain-operational scope caveat (formats depending on proprietary tooling without an open parser are not `commonly used and machine-readable`). **Scope-title note (P0):** the index.md `SBOM` label is reconciled with the CRDA-deep `Software Bill of Materials (SBOM)` source-of-truth title — this file uses the CRDA-deep title per Batch 11 critical-rule #6 + #8 (the Batch 11 HSO file already documented the divergence). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
CRA only (1 of 5 regs — **CRA is SOLE AUTHORITY per AEGIS taxonomy §4.1**). 0 pairwise cells (single-participant sub-domain; no cross-regulation aggregation surface). GDPR has no SBOM mandate (a manufacturer may integrate a `commonly used` format reference per `SR-GDPR-032`, but `commonly used` is undefined and is not an SBOM mandate). NIS 2 has no SBOM mandate. DORA Art. 24(4) SBOM cross-ref applies to digital operational resilience testing, not to the Annex I Part II (1) SBOM. AI Act has no SBOM mandate. CRDA-deep verified **0 conditional emergent tensions** by construction (single regulator). The high-level SO and the CRA sub-SO describe the same obligation at different abstraction levels, and the activation model treats the high-level SO as redundant in this single-regulator case but still emits it for traceability per the activation model in `../../HierarchicalSecurityObjectives/index.md` lines 32–42. The CRA sub-SO captures the full regulatory surface (Art. 3(39) SBOM definition + Annex I Part II (1) authoring + Annex VII §2(b) technical-documentation retention + Annex II §9 optional user access + Art. 13(24) Commission implementing acts + Annex VII §8 MSA reasoned request) — the three-anchored (+ optional fourth) SBOM architecture.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 6.2
  volere_section: 15
  volere_subtype: audit
  title: "Manufacturer draws up and maintains a software bill of materials (SBOM) covering components and dependencies in a commonly used and machine-readable format with at minimum the top-level dependencies (three-anchored SBOM architecture: authoring + retention + regulatory disclosure + optional user access)"
  derives_from:
    hso_sub_so: SO-D-06.2.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.2.md
    objective_ref_section: "### D-06.2.0"
  description: |
    The product shall operate the three-anchored SBOM architecture with the manufacturer drawing up and maintaining an SBOM covering the components and dependencies contained in the product with digital elements, in a commonly used and machine-readable format that supports automated downstream consumption, with at minimum the top-level dependencies; the SBOM is (1) authored at product release and continuously updated through the support period, (2) retained in the technical documentation under Annex VII §2(b) surviving the Annex VII §4 retention period (10 years or support period, whichever is longer), and (3) disclosed to market surveillance authorities on reasoned request where necessary for the authority to check compliance with the Annex I cybersecurity requirements; the Annex II §9 user-facing access is at the manufacturer's discretion as the optional fourth anchor (CRA Art. 3(39) SBOM definition + Annex I Part II (1) authoring + Annex VII §2(b) technical-documentation retention + Annex VII §8 MSA reasoned request + Annex II §9 optional user access + Art. 13(24) Commission implementing acts + Art. 13(8) support-period handling + Art. 13(13) 10-year retention + Annex VII §4).
  fit_criterion: |
    A three-anchored SBOM architecture is operated covering authoring + retention + regulatory disclosure + optional user access; the authoring anchor produces an SBOM at product release in a commonly used and machine-readable format covering at minimum the top-level dependencies (POLY-S2 R1 reading per SR-CRA-052 — first-level direct dependencies with depth-1 look-through; depth-discretionary beyond the floor) with the format choice (POLY-S3 R3 reading per SR-CRA-008 — any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24); R5 domain-agnostic cryptographic-manifest reading admitted as long-run consensus direction but rejected for current OJ reading) documented in the conformity dossier under Annex VII §2(b) with format-choice rationale + open-parser reference (formats depending on proprietary tooling without an open parser are not `commonly used and machine-readable`); the SBOM is continuously updated across the support period under Art. 13(8); the retention anchor includes the SBOM in the technical documentation under Annex VII §2(b) surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9) 10-year tail; the regulatory-disclosure anchor provides the SBOM on reasoned request from a market surveillance authority under Annex VII §8 with the `where necessary` scope (POLY-S2 R1 reading per SR-CRA-053 — the subset of the SBOM directly relevant to the compliance question under investigation, not a comprehensive dump of every component) documented in the MSA-request log; the optional Annex II §9 user-facing access is at the manufacturer's discretion (POLY-S2 R1 reading per SR-CRA-053 — no obligation to publish the SBOM externally; the obligation is only to include it in the technical documentation); the format-migration posture when the Commission implementing acts under Art. 13(24) specify a binding format is documented with versioning evidence; the three-anchored SBOM architecture operates as the upstream component-identification artefact that feeds 6.1 (component due diligence under SR-CRA-050), 2.1 (vulnerability identification under SR-CRA-007 — SBOM feeds CVE matching), 2.2 (vulnerability remediation under SR-CRA-008 + SR-CRA-010 — addresses the component vulnerabilities identified by the SBOM), and 9.4 (technical documentation under SR-CRA-059 — SBOM is the Annex VII §2(b) artefact in the conformity-assessment bundle); verified by Annex VII §2(b) technical-documentation SBOM inclusion review + SBOM versioning records audit + Annex VII §4 retention compliance review + Annex VII §8 MSA-request response log inspection + Annex II §9 user-access posture documentation review + MSA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: [6.1.3 (SBOM feeds component-tier inventory substrate under SR-CRA-050 due diligence)]
  nist_csf: [ID.AM-02, GV.SC-02, GV.SC-03]
  applicable_if:
    regs: [CRA]
    scope_overlap: N/A   # single-participant sub-domain; the high-level SO is redundant in this single-regulator case but is still emitted for traceability per the activation model in ../../HierarchicalSecurityObjectives/index.md lines 32-42
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Only 1 regulator participates (CRA is the SOLE AUTHORITY per AEGIS taxonomy §4.1); GDPR, NIS 2, DORA, AI Act are all out-of-scope. The high-level SO and the CRA sub-SO describe the same obligation at different abstraction levels, and the activation model treats the high-level SO as redundant in this single-regulator case but still emits it for traceability. The format-floor POLY-S3 is resolved to R3 (any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24)); the depth-floor POLY-S2 is resolved to R1 (first-level direct dependencies with depth-1 look-through, per SR-CRA-052); the `where necessary` MSA-disclosure scope POLY-S2 is resolved to R1 per SR-CRA-053 (necessary subset directly relevant to the compliance question). The soft-touch cross-pollination with SR-GDPR-032 `commonly used` ambiguity in Art. 15(3) is a format-selection-layer architectural support — the CRA-side SBOM format choice and the controller-side GDPR Art. 15(3) portability format choice may share infrastructure (e.g. a single data-catalog machinery) but the two obligations are not the same and the GDPR obligation is data-subject-right-bound while the CRA obligation is manufacturer-side-bound. The SBOM is the upstream component-identification artefact that feeds 6.1 (component due diligence under SR-CRA-050), 2.1 (vulnerability identification under SR-CRA-007), 2.2 (vulnerability remediation under SR-CRA-008 + SR-CRA-010), and 9.4 (technical documentation under SR-CRA-059). The format-migration posture when the Commission implementing acts under Art. 13(24) specify a binding format is documented with versioning evidence across the support period. CRDA-deep verified 0 conditional emergent tensions by construction (single regulator); the three-anchored SBOM architecture is the manufacturer-side architectural artefact under Art. 13(1) design-time + Annex I Part II (1) identification-and-documentation duty, documented in Annex VII §2(b) technical documentation, optional for user-facing access under Annex II §9, and disclosed to MSAs on reasoned request under Annex VII §8. (Copied from the HSO Considerations block of `### D-06.2.0`; preserved here for self-contained traceability.)
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-06.2
title: D-06.2 Software Bill of Materials (SBOM) — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.2 Software Bill of Materials (SBOM)
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-06_Supply-Chain/D-06.2.md
status: DRAFT
---
> **Deep analysis:** [D-06.2 Software Bill of Materials (SBOM)](../../DeepAnalysis/D-06_Supply-Chain/D-06.2.md)
#### D-06.2 Software Bill of Materials (SBOM)
<!-- participants: CRA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | — | Out-of-scope (sole authority: CRA) | n/a |
| NIS2 | — | Out-of-scope (sole authority: CRA) | n/a |
| CRA | SO-CRA-038 | Manufacturer draws up and maintains SBOM in commonly used, machine-readable format covering at least top-level dependencies; provided to MSA on reasoned request (Annex I Part II (1) + Art. 13(24) + Annex VII §2(b) + Annex VII §8) | Product with digital elements; manufacturer SBOM |
| DORA | — | Out-of-scope (sole authority: CRA) | n/a |
| AI_Act | — | Out-of-scope (sole authority: CRA) | n/a |
**Sole-authority note:** GDPR, NIS2, DORA, and AI Act are all out-of-scope for D-06.2 per AEGIS taxonomy §4.1. CRA Annex I Part II (1) is the SOLE AUTHORITY for SBOM. This is the only sub-domain in Part B where CRA is the sole authority across all 5 regulations.
##### Pairwise matrix
No applicable pairs — only one participant (CRA).
##### Emergent tensions (3+ regulations)
None.
##### SR cross-validation
NIST CSF 2.0 anchoring via **ID.AM-02** (Software platforms and applications inventoried). CRA maps ID.AM-02 via SR-CRA-008 (machine-readable format) and SR-CRA-052 (top-level dependencies) and SR-CRA-053 (technical documentation). Single-regulation; CSF mapping is consistent. The CRA Annex II §9 SBOM access location (optional user access) is not separately mapped by CSF 2.0; it is a product-instruction construct.
##### Downstream implication
Phase 2 obligation derivation produces a single-track SBOM obligation per CRA. Phase 3 case generation must validate that CRA-classified case companies produce and maintain an SBOM covering top-level dependencies in a commonly used machine-readable format (e.g., SPDX or CycloneDX). The Annex VII §8 MSA-disclosure obligation is an institutional hook, not an operational requirement; case companies do not need to provide the SBOM to users by default (Annex II §9 is optional).
---
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-06.2
title: D-06.2 Software Bill of Materials (SBOM) — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.2 Software Bill of Materials (SBOM)
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-06_Supply-Chain/D-06.2.md
status: DRAFT
---
> **Domain analysis:** [D-06.2 Software Bill of Materials (SBOM)](../../DomainAnalysis/D-06_Supply-Chain/D-06.2.md)
#### D-06.2 Software Bill of Materials (SBOM)
<!-- participants: CRA (sole authority) -->
**Participants (from CRDA):** CRA (sole authority)
**Sole-authority note:** GDPR, NIS2, DORA, and AI Act are all out-of-scope for D-06.2 per AEGIS taxonomy §4.1. CRA Annex I Part II (1) is the SOLE AUTHORITY for SBOM. This is the only sub-domain in Part C where CRA is the sole authority across all 5 regulations.
**Pairwise matrix:** No applicable pairs — only one participant (CRA).
**NIST CSF 2.0 anchoring via ID.AM-02** (Inventories of software platforms and applications). CRA maps ID.AM-02 via SR-CRA-008 (machine-readable format) and SR-CRA-052 (top-level dependencies) and SR-CRA-053 (technical documentation). Single-regulation; CSF mapping is consistent. The CRA Annex II §9 SBOM access location (optional user access) is not separately mapped by CSF 2.0; it is a product-instruction construct.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a single-track SBOM obligation per CRA. Phase 3 case generation must validate that CRA-classified case companies produce and maintain an SBOM covering top-level dependencies in a commonly used machine-readable format (e.g., SPDX or CycloneDX). The Annex VII §8 MSA-disclosure obligation is an institutional hook, not an operational requirement; case companies do not need to provide the SBOM to users by default (Annex II §9 is optional).
---
---

