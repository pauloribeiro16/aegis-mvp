# D-05.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-05.4 Data Portability](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md)
#### D-05.4 Data Portability
<!-- participants: GDPR (sole authority) -->
**Participants (from CRDA):** GDPR (sole authority)
**Sole-authority note:** NIS2, CRA, DORA, and AI Act are all out-of-scope for D-05.4 per AEGIS taxonomy §4.1. GDPR Art. 20 is the SOLE AUTHORITY. The CRA Annex I Part I (2)(m) secure cross-product data transfer (SR-CRA-049) overlaps at the *technical* level (secure transfer mechanism) but does not constitute a portability *right* — it is a manufacturer-side architectural obligation, not a data-subject right.
**Pairwise matrix:** No applicable pairs — only one participant (GDPR).
**NIST CSF 2.0 anchoring:** **PR.DS-10** (Data-in-use protected) and **PR.DS-12** (Data managed consistent with risk strategy). Single-regulation; CSF mapping is consistent.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a single-track portability rule. Phase 3 case generation validates that case companies expose an Art. 20 export function for personal data. The CRA cross-product transfer mechanism (SR-CRA-049) should be cited as a *complementary* technical anchor when the data resides in a CRA-classified product, but it does not substitute for the GDPR Art. 20 right.
---

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-05.4 Data Portability
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md`](../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md)
> (**1 of 5 participating regulation is GDPR — SOLE AUTHORITY** as noted
> by `DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md` line 36: "NIS2,
> CRA, DORA, and AI Act are all out-of-scope for D-05.4 per AEGIS
> taxonomy §4.1. GDPR Art. 20 is the SOLE AUTHORITY. The CRA Annex I
> Part I (2)(m) secure cross-product data transfer (SR-CRA-049) overlaps
> at the *technical* level — the secure transfer mechanism that supports
> a cross-controller portability event when the data resides in a
> CRA-classified product — but it does **not** constitute a portability
> *right** (it is a manufacturer-side architectural obligation addressed
> to the product, not a data-subject right per Art. 20). The CRA
> mechanism is cited as a *complementary technical anchor* in this HSO
> file (sub-SO Objective + Phase 1C Doc 07 implications) but does
> **not** ground a CRA sub-SO. The 1 sub-SO (GDPR) is the entire
> regulatory surface of D-05.4.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-05.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-020 | Data subject receives personal data in a structured, commonly used, machine-readable format and can transmit those data to another controller without hindrance; the Art. 15(3) `commonly used electronic form` copy is the operational companion obligation supplying the read-only copy at the data subject's request, and Art. 20 supplies the portability right to transmit to another controller | Personal data; data-subject right; Art. 20(1)/(2)/(3)/(4) + Art. 15(3) companion copy; PR.DS-10 + PR.DS-12 |
**Sole-authority framing.** The CRDA-deep source-of-truth explicitly
notes that **CRA, NIS 2, DORA, and AI Act are all out-of-scope for
D-05.4** per AEGIS taxonomy §4.1. GDPR Art. 20 is the **SOLE
AUTHORITY** for the data-subject portability right. The CRA Annex I
Part I (2)(m) second-limb secure cross-product transfer
(`SR-CRA-049`) overlaps at the *technical* level — the secure transfer
mechanism that supports a cross-controller portability event when the
data resides in a CRA-classified product — but it does **not**
constitute a portability *right* (it is a manufacturer-side
architectural obligation addressed to the product, not a data-subject
right per Art. 20). The CRA mechanism is cited as a *complementary
technical anchor* in this HSO file (sub-SO Objective + Phase 1C Doc 07
implications) but does **not** ground a CRA sub-SO. The 1 sub-SO
(GDPR) is the entire regulatory surface of D-05.4.

## Validated relationships (from CRDA-deep §D-05.4)

#### Validated relationships (from CRDA-deep §D-05.4)
**No pairwise cells** — single-participant sub-domain. There is no
cross-regulation aggregation surface on D-05.4; the high-level SO and
the GDPR sub-SO both describe the same GDPR Art. 20 obligation at
different abstraction levels, and the high-level SO is **redundant
in this single-regulator case** (per the activation model in
`../../index.md` lines 32–42 — `1 reg applicable → use that reg's
sub-SO directly; the high-level SO is redundant in this case but is
still emitted for traceability`).
The architectural interplay with CRA Annex I Part I (2)(m) **is not
a regulatory pair** for D-05.4 purposes — it is a **technical anchor**
that supports the GDPR Art. 20 right when the data resides in a
CRA-classified product, but the CRA clause does not constitute a
portability obligation in the GDPR Art. 20 sense:
- **GDPR Art. 20 → CRA Annex I Part I (2)(m) (technical anchor only)**:
  GDPR Art. 20 grants the data subject the right to receive personal
  data concerning them in a structured, commonly used, machine-readable
  format and to transmit those data to another controller without
  hindrance (Art. 20(1)). Art. 20(2) requires the controller to provide
  the data in the same format where technically feasible, with
  cross-controller direct transmission requiring the technical means.
  Art. 20(3) qualifies the right: (a) processing is based on consent
  (Art. 6(1)(a)) or contract (Art. 6(1)(b)); (b) processing is carried
  out by automated means. Art. 20(4) excludes processing for the
  performance of a task carried out in the public interest or in the
  exercise of official authority, or for the legitimate-interest
  grounds (Art. 6(1)(e)/(f)).
  When the portability-eligible personal data resides in a
  CRA-classified product, the controller-side Art. 20 export pipeline
  is supported architecturally by the **CRA Annex I Part I (2)(m)
  second-limb** secure cross-product transfer mechanism (`SR-CRA-049`)
  — confidentiality + integrity + destination-authentication as the
  three constituent controls. The CRA mechanism is the technical
  platform that makes the Art. 20 cross-controller transmission
  operationally feasible; the CRA mechanism does NOT independently
  ground a portability obligation on the CRA side because it is a
  manufacturer-side architectural obligation, not a data-subject right
  (the user invoking the CRA (2)(m) second limb is exercising a
  manufacturer's product affordance, not an Art. 20 portability claim
  against a controller).
- This is a **layered technical support** rather than a regulatory
  pair: the **regulatory obligation is GDPR-only** (Art. 20 data-subject
  right against the controller); the **technical anchor is CRA-side**
  (manufacturer-designed cross-product transfer mechanism per Annex I
  Part I (2)(m) second limb) when the data resides in a CRA-classified
  product. The two are not the same obligation; the CRA mechanism
  supports the GDPR obligation architecturally without imposing a
  second regulatory track on D-05.4.
The portability architecture is **single-regulator** — the GDPR
sub-SO captures the full regulatory surface; the CRA technical anchor
is a dependency on the data substrate (CRA-classified product at the
storage layer) rather than a second regulatory channel. The
high-level SO describes the common portability duty with the CRA
technical anchor noted in the Objective text; the per-regulation
perspective is preserved verbatim in the 1 sub-SO (trigger, format,
recipient, legal anchor).

## Cross-recipient map

#### Cross-recipient map
D-05.4 itself does **not** generate recipient asymmetry on the
portability event — the portability export is **outward-looking** in
the data-subject-as-recipient sense (the data subject is the recipient
of the export) but the regulatory channel is **inward-looking** at
the controller level (the controller executes the export and
documents the export pipeline). The recipient fragmentation is at
the **downstream compliance-demonstration point** (and is
single-regulator by construction): **GDPR's supervisory authority
(DPA)** on the Art. 5(2) accountability evidence (Art. 20(2)
structured-and-machine-readable format compliance + Art. 12(1)
transparency about the right + Art. 12(3) ≤1-month service-level
with possible extension to ≤2 months for complex requests +
Art. 30(1)(b) RoPA record on the categories of data subjects and
personal data + Art. 35(7) DPIA where applicable). The data subject
is the **direct recipient** of the portability export (the export
itself is the artefact); the receiving controller (in a
cross-controller portability event) is the **operational downstream
recipient** (it receives the data through the data subject's
transmission or — under Art. 20(2) sentence 2 — directly from the
originating controller where technically feasible, with the explicit
limitation that the originating controller is not required to
implement cross-controller direct transmission where it is
technically infeasible and the data subject retains the right to
transmit themselves). **No secondary regulatory channel exists on
D-05.4** — the export pipeline, the format compliance evidence, and
the cross-controller transmission infrastructure all flow through the
GDPR channel.
---

## HSO considerations (from D-05.4.0 — High-level SecurityObjective)

**Considerations.**
- Only 1 regulator participates (GDPR is the SOLE AUTHORITY per AEGIS taxonomy §4.1); NIS 2, CRA, DORA, AI Act are all out-of-scope. The high-level SO and the GDPR sub-SO describe the same obligation at different abstraction levels, and the activation model treats the high-level SO as redundant in this single-regulator case but still emits it for traceability.
- The CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is a complementary **technical anchor** when the portability-eligible personal data resides in a CRA-classified product — the manufacturer's secure-transfer mechanism (confidentiality + integrity + destination-authentication) is the architectural substrate that makes the Art. 20 cross-controller transmission operationally feasible. The CRA mechanism is NOT a portability right (it is a manufacturer-side architectural obligation) and does NOT ground a CRA sub-SO on D-05.4.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 1 participating regulation defines D-05.4 over a single **layer**
of the portability architecture; the trigger, the format anchor, the
recipient distribution, and the legal anchor all depend on whether the
portability event is exercised on the regulatory layer (controller)
or whether it operates against the technical substrate (CRA-classified
product at the storage layer).
| Axis (reg) | Layer | Trigger | Format anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | controller-side data-subject right (Art. 20 portability) | data subject's Art. 20 request (Art. 20(3) conditions met — consent/contract basis + automated means; Art. 20(4) exclusions honoured) — TRIGGERED | `structured, commonly used and machine-readable format` (Art. 20(1)) — operationalised via SR-GDPR-032 structured-interoperable reading (JSON, CSV, XML per EDPB Guidelines 06/2020) | data subject (Art. 20(1) direct recipient); receiving controller (Art. 20(1) cross-controller transmission target); DPA (Art. 58 supervision on the export-pipeline documentation) | Art. 20(1)/(2)/(3)/(4) + Art. 15(3) companion copy + Art. 12(1) transparency + Art. 12(3) ≤1-month (≤2-month complex) service-level + Art. 12(5) free of charge + Art. 13(2)(b) / Art. 14(2)(c) information-supply + Art. 30(1)(b) RoPA record + Art. 35(7) DPIA where applicable + Art. 5(2) accountability |
| **CRA (technical anchor only, NOT a sub-SO)** | manufacturer-side product-side cross-product transfer mechanism (Annex I Part I (2)(m) second limb) | user's product-initiated cross-product transfer request — TRIGGERED | `securely` (R1 reading per SR-CRA-049: confidentiality + integrity + destination-authentication — the three-component secure-transfer reading aligned with the controller-side PR.DS-02 ↔ SR-GDPR-032 PR.DS-10/12 anchors) | user as the direct recipient of the secure-transfer affordance (NOT a GDPR Art. 20 portability claim against the controller) | Annex I Part I (2)(m) second limb + Art. 13(1) + Art. 13(2) risk assessment on the binding-mechanism depth |

## Scope-overlap matrix (1×1)

#### Scope-overlap matrix (1×1)
| | GDPR |
|---|---|
| **GDPR** | — |
Legend: **N/A** = no scope question for the self-pair (single-participant sub-domain). CRDA-deep scope-disjoint test: not applicable (no pairs to test).

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-05.4.HL`) engages on a given party **only when GDPR is in
`applicable_regs`** (and the data subject exercises the Art. 20
right). Because only 1 regulator participates on D-05.4, the
high-level SO does **not** aggregate cross-regulation surface; it
serves as the **traceability artefact** for the common portability
duty in the single-regulator case (per the activation model in
`../../index.md` lines 32–42 — `1 reg applicable → use that reg's
sub-SO directly; the high-level SO is redundant in this case but is
still emitted for traceability`). The regulatory-right layer (GDPR
Art. 20 against the controller) and the technical-anchor layer
(CRA Annex I Part I (2)(m) second limb against the manufacturer
when the data resides in a CRA-classified product) are **distinct
layers — not collapsed and not aggregated**: the regulatory layer
binds the controller; the technical-anchor layer supports the
architectural substrate. For a 5-FTE SaaS startup with GDPR
applicability (no CRA-classified product on the data-substrate
side), only the GDPR sub-SO activates and the technical anchor is
not invoked. For a controller whose portability-eligible data
resides in a CRA-classified product (e.g. an integrated
manufacturer-controller operating a CRA-classified cloud platform),
**both layers operate**: the regulatory layer binds the controller
to supply the Art. 20 export pipeline; the technical anchor
supports the cross-controller transmission through the
manufacturer's (2)(m) second-limb secure-transfer mechanism. The
high-level SO describes the common portability duty but does NOT
collapse the regulatory layer and the technical-anchor layer — the
two remain distinct.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 1 of 5 regulations participates (GDPR is the SOLE AUTHORITY for
  D-05.4 per AEGIS taxonomy §4.1; NIS 2, CRA, DORA, AI Act are
  out-of-scope at the regulatory layer; CRA is cited as a technical
  anchor only).
- 0 pairwise cells — single-participant sub-domain.
- No CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY classifications
  by construction (single regulator).
- The GDPR sub-SO captures the **full regulatory surface** (Art.
  20(1) portability right + Art. 20(2) format + Art. 20(3)
  conditions + Art. 20(4) exclusions + Art. 15(3) companion copy
  + Art. 12 transparency + Art. 12(3) service-level + Art. 13/14
  information-supply + Art. 5(2) accountability + Art. 30(1)(b)
  RoPA record + Art. 35(7) DPIA where applicable).
- The high-level SO does **NOT** resolve any conditional tension —
  there are **0 conditional emergent tensions** in this sub-domain
  (single regulator; no 3-way interaction surface; the CRA technical
  anchor is not a regulatory pair and does not generate a tension).
  Phase 1C Doc 07 does not need to resolve contradictions on
  D-05.4 because none exist by construction.
- **Scope caveat (CRITICAL — sole-authority scope framing)** —
  derived from CRDA-deep verified classifications: the D-05.4
  sub-domain is **single-regulator** — GDPR Art. 20 is the sole
  authority for the data-subject portability right. For a party
  with GDPR in `applicable_regs`, the GDPR sub-SO activates and
  the high-level SO is emitted for traceability (redundant in
  the single-regulator case per the activation model). For a
  party with GDPR out of `applicable_regs` (no GDPR scope —
  e.g. a non-EU-controlled processor that nevertheless
  manufactures CRA-classified products), the GDPR sub-SO does
  NOT activate (and the CRA technical anchor does NOT generate
  a sub-SO on D-05.4 because the CRA mechanism is an
  architectural support and not a portability right). Phase 1A
  must therefore emit **one check before applying the
  high-level SO** — confirming that GDPR is in `applicable_regs`
  — and must NOT synthesise a CRA-or-other-reg sub-SO on D-05.4
  from the architectural-anchor mapping.
- **Scope caveat (CRITICAL — regulatory-right vs technical-anchor
  layer distinction)** — derived from CRDA-deep verified
  classifications: the **CRA Annex I Part I (2)(m) second-limb**
  secure cross-product transfer (`SR-CRA-049`) is NOT a
  portability right (it is a manufacturer-side architectural
  obligation addressed to the product), and does NOT ground a
  sub-SO on D-05.4. The CRA architectural support is cited in
  the Objective text and the sub-SO Objective text as the
  **technical anchor** when the portability-eligible personal
  data resides in a CRA-classified product — the manufacturer's
  secure-transfer mechanism (confidentiality + integrity +
  destination-authentication) is the architectural substrate
  that makes the Art. 20 cross-controller transmission
  operationally feasible. The regulatory layer (GDPR Art. 20
  against the controller) and the technical-anchor layer (CRA
  Annex I Part I (2)(m) second limb against the manufacturer)
  are distinct and are not collapsed by the high-level SO. For an
  integrated manufacturer-controller (e.g. a SaaS company
  manufacturing its own CRA-classified cloud platform), the
  two layers STACK architecturally on the same data-substrate
  product but remain **legally distinct**: the controller-side
  Art. 20 obligation binds under GDPR; the manufacturer-side
  (2)(m) second-limb obligation binds under CRA. The
  high-level SO does NOT aggregate the two into a single
  portability obligation.
- **Scope caveat (CRITICAL — `commonly used electronic form`
  format-quality floor)** — derived from CRDA-deep verified
  classifications: GDPR Art. 20 + Art. 15(3) carry VAG-S3
  ambiguity on the format open-texture (per `SR-GDPR-032`
  ambiguity_notes). The reading adopted is the
  **structured-interoperable reading**: JSON, CSV, or XML —
  aligned with EDPB Guidelines 06/2020 on data portability
  (which interpret the parallel Art. 20 phrase). Print-ready
  rendering (PDF or scanned image) is rejected as defeating the
  purpose; controller-preferred proprietary format is rejected as
  functionally obstructing. The high-level SO does NOT specify
  a single clock or format (the choice between JSON, CSV, or XML
  is delegated to the controller, calibrated per the data
  subject's context); the high-level SO does specify the
  **structural floor** (machine-readable; structured; commonly
  used; interoperable downstream) and the **service-level
  calibration anchor** (Art. 12(3) ≤1 month, ≤2 months for
  complex requests).
- **Scope caveat (CRITICAL — Art. 20(3) conditions + Art. 20(4)
  exclusions + third-party-rights carve-out)** — derived from
  CRDA-deep verified classifications: the Art. 20 portability
  right applies only when (a) processing is based on Art. 6(1)(a)
  consent or Art. 6(1)(b) contract AND (b) processing is
  carried out by automated means (Art. 20(3)). The right does
  NOT apply to (a) processing necessary for the performance
  of a task carried out in the public interest or in the
  exercise of official authority OR (b) processing for the
  legitimate-interest grounds (Art. 6(1)(e)/(f)), without
  prejudice to the data subject's Art. 21 right to object
  (Art. 20(4)). The Art. 20(3) third-party-rights carve-out
  is **rare-but-honest**: the controller may refuse an export
  where the export would infringe third-party rights; this
  is the structural qualifier on the right. The high-level SO
  does NOT relax the Art. 20(3) conditions, does NOT extend
  the right beyond Art. 20(4) exclusions, and does NOT
  override the third-party-rights carve-out.
---

## Emergent tensions (from CRDA-deep §D-05.4)

#### Emergent tensions (from CRDA-deep §D-05.4)
**0 conditional emergent tensions** — single-participant sub-domain.
Only 1 regulation participates (GDPR as SOLE AUTHORITY), and the
sub-domain has 0 pairwise cells and no scope-disjoint or
contradictory classifications by construction. The pairwise reading
captures the entire interaction surface (such as it is); there is no
non-pairwise 3-way observation to surface, and the CRA technical
anchor (SR-CRA-049, Annex I Part I (2)(m) second limb) is **not a
regulatory pair** — it is an architectural support for the GDPR Art.
20 cross-controller transmission when the portability-eligible data
resides in a CRA-classified product, and it does NOT generate a
tension. The **layered technical-support pattern** (regulatory-right
layer GDPR Art. 20 + technical-anchor layer CRA Annex I Part I
(2)(m) second limb on the data substrate) is the textbook
single-regulator sub-domain with one architectural dependency on a
separate but out-of-scope CRA mechanism: the regulatory layer binds
the controller under Art. 20; the technical anchor supports the
architectural substrate when the data resides in a CRA-classified
product; the two are distinct and the compliance demonstration
trails diverge (controller-side Art. 5(2) accountability + Art. 30
RoPA + Art. 12 transparency vs manufacturer-side Annex VII §2 + §6
technical documentation on the (2)(m) second-limb binding mechanism).
**No scope-disjoint pairs and no contradictory pairs** — the
high-level SO does NOT collapse the regulatory-right layer and the
technical-anchor layer; the **layer divergence** (regulatory right vs
technical support) is the **rare-but-honest single-regulator
distinction**: GDPR Art. 20 is the regulatory right, and CRA Annex I
Part I (2)(m) second limb is the architectural support. The high-
level SO surfaces the common portability duty with the technical
anchor noted in the Objective text; the per-reg trigger, format
anchor, recipient distribution, and legal anchor are documented in
the 1 sub-SO. The **structured-interoperable reading of `commonly
used electronic form`** (JSON, CSV, XML per EDPB Guidelines 06/2020)
is the **rare-but-honest format-quality convergence** — the EDPD-
aligned structured-interoperable reading aligns the export pipeline
with the cross-controller portability aim and the downstream-tool
interoperability requirement, while rejecting the print-ready and
controller-proprietary readings that would defeat the portability
purpose. The **Art. 20(3) conditions + Art. 20(4) exclusions + third-
party-rights carve-out** are the **rare-but-honest scope-qualifier
architecture**: portability applies only when (a) consent/contract
basis AND (b) automated means; portability does NOT apply to
public-interest-task or legitimate-interest processing; the
controller may refuse an export that would infringe third-party
rights. The high-level SO honours all three scope qualifiers
without extending or contracting them.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with GDPR in `applicable_regs` — and any portability-
eligible personal data (i.e. data processed on the basis of consent
or contract + by automated means) — operates a **portability export
pipeline** with the following structural elements documented
verbatim from the CRDA-deep verified classifications. The high-level
SO (`SO-D-05.4.HL`) describes the common portability duty (data
subject receives personal data in a structured, commonly used,
machine-readable format and can transmit to another controller
without hindrance, with the CRA architectural anchor noted in the
Objective text); the per-reg perspective is preserved in the 1
sub-SO (trigger, format anchor, recipient, legal anchor).
**No conflict-resolution is required on D-05.4** because the
sub-domain is single-regulator by construction and the CRA
architectural support is not a regulatory pair (it is a technical
anchor under SR-CRA-049 when the data resides in a CRA-classified
product, and does NOT generate a sub-SO on D-05.4). Phase 1C Doc 07
documents the **GDPR-only portability strategy**: (1) the Art. 20
export pipeline with the **structured-interoperable reading** of
`commonly used electronic form` per `SR-GDPR-032` ambiguity_notes
(JSON, CSV, XML per EDPB Guidelines 06/2020); (2) the **Art.
12(3) service-level** of ≤1 month (≤2 months for complex requests
with reasoned extension notice to the data subject within the
original ≤1 month period) free of charge under Art. 12(5); (3) the
**Art. 20(3) conditions** as the scope-qualifier (consent/contract
basis + automated means); (4) the **Art. 20(4) exclusions** as the
anti-scope (no public-interest-task; no legitimate-interest
processing; without prejudice to Art. 21 right to object); (5) the
**Art. 20(3) third-party-rights carve-out** as the rare-but-honest
structural qualifier (controller may refuse an export that would
adversely affect the rights and freedoms of others); (6) the
**Art. 13(2)(b) / Art. 14(2)(c) information-supply** as the
data-subject-awareness loop (the right exists + the categories of
personal data concerned); (7) the **Art. 12(1) transparency** as
the procedural-information loop (the right is documented at
collection + at data-subject-request time); (8) the **Art. 30(1)(b)
RoPA record** as the documentation loop (categories of data
subjects + categories of personal data + retention + security
measures); (9) the **Art. 35(7) DPIA where applicable** as the
risk-assessment loop; (10) the **PR.DS-10 + PR.DS-12 anchoring**
as the runtime-integrity + data-management substrate for the
export pipeline; (11) the **CRA Annex I Part I (2)(m) second-limb
secure cross-product transfer (`SR-CRA-049`)** cited as the
**complementary technical anchor** when the portability-eligible
data resides in a CRA-classified product — NOT a portability
right, NOT a sub-SO on D-05.4, but the architectural substrate
that makes the cross-controller transmission operationally
feasible; (12) the **layer-distinction architecture** — the
regulatory-right layer (GDPR Art. 20 against the controller) and
the technical-anchor layer (CRA Annex I Part I (2)(m) second limb
against the manufacturer) are distinct and not collapsed by the
high-level SO; the compliance demonstration trails diverge
(controller-side Art. 5(2) accountability + Art. 30 RoPA + Art. 12
transparency vs manufacturer-side Annex VII §2 + §6 technical
documentation on the binding-mechanism depth). For proportionality
(P2), a 5-FTE SaaS with GDPR applicability may default to a
structured-interoperable export endpoint (JSON/CSV/XML,
exportable per Art. 12(3) ≤1 month service-level, free of charge)
on the categories of personal data processed on the basis of
consent or contract by automated means (CRA technical anchor out
of scope unless the SaaS's data substrate is a CRA-classified
product); a mid-size manufacturer-controller operating a
CRA-classified cloud platform processing portability-eligible
personal data must additionally document the CRA Annex I Part I
(2)(m) second-limb secure-transfer mechanism in the Annex VII
technical documentation, with the controller-side Art. 20 export
pipeline executed through the manufacturer's secure-transfer
mechanism at the architectural layer and the Art. 5(2)
accountability evidence discharged via the Annex VII documentation.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-05.4 Data Portability — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.4.md`. See that file for CRDA-deep verified single-participant status (GDPR is the SOLE AUTHORITY for D-05.4 per AEGIS taxonomy §4.1 — NIS 2, CRA, DORA, AI Act are all out-of-scope at the regulatory layer; the CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is a *complementary technical anchor* when portability-eligible data resides in a CRA-classified product but does NOT constitute a portability *right* and does NOT ground a CRA sub-SO on D-05.4), structured-interoperable reading of `commonly used electronic form` per SR-GDPR-032 ambiguity_notes (JSON, CSV, XML per EDPB Guidelines 06/2020 — print-ready and controller-proprietary rejected as defeating the purpose), Art. 20(3) conditions (consent/contract basis + automated means) + Art. 20(4) exclusions (no public-interest-task or legitimate-interest processing) + Art. 20(3) third-party-rights carve-out, regulatory-right vs technical-anchor layer distinction (the GDPR Art. 20 obligation binds the controller; the CRA (2)(m) second-limb is an architectural support when the data resides in a CRA-classified product; the two layers are distinct and not collapsed by the high-level SO), and aggregation logic (1 of 5 regs participates, 0 pairwise cells, 0 emergent tensions, no CORRECTED/SCOPE-DISJOINT/CONTRADICTORY classifications by construction). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR SOLE AUTHORITY (1 of 5 regs — NIS 2, CRA, DORA, AI Act are out-of-scope per AEGIS taxonomy §4.1). CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is cited as a **complementary technical anchor** when portability-eligible data resides in a CRA-classified product — the manufacturer's secure-transfer mechanism (confidentiality + integrity + destination-authentication per PR.DS-02) is the architectural substrate that makes the Art. 20 cross-controller transmission operationally feasible; the CRA mechanism is NOT a portability right (it is a manufacturer-side architectural obligation addressed to the product, not a data-subject right per Art. 20) and does NOT ground a CRA sub-SO on D-05.4. The 1 sub-SO (GDPR) captures the **full regulatory surface**; the high-level SO is redundant in this single-regulator case but is emitted for traceability per the activation model.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 5.4
  volere_section: 15
  volere_subtype: privacy
  title: "Data subject receives personal data in a structured, commonly used, machine-readable format and can transmit to another controller without hindrance, with the CRA architectural anchor as a complementary technical support layer when applicable"
  derives_from:
    hso_sub_so: SO-D-05.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.4.md
    objective_ref_section: "### D-05.4.0"
  description: |
    The product shall provide a portability export pipeline delivering the data subject's personal data in a structured, commonly used, machine-readable format (per the structured-interoperable reading of Art. 20(1) + Art. 15(3)), with the right to transmit to another controller without hindrance where processing is based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) and carried out by automated means (Art. 20(3)), supported architecturally by the CRA (2)(m) second-limb secure-transfer mechanism as a complementary technical anchor (not a portability right) when the portability-eligible data resides in a CRA-classified product.
  fit_criterion: |
    A controller-side portability export pipeline is operated with a structured-interoperable format default (JSON, CSV, or XML per EDPB Guidelines 06/2020 — the print-ready rendering (PDF or scanned image) is rejected as defeating the purpose; controller-preferred proprietary format is rejected as functionally obstructing); Art. 12(3) ≤1-month service-level is met (extendable to ≤2 months for complex requests with reasoned extension notice within the original ≤1-month period); export is free of charge per Art. 12(5); Art. 20(3) conditions (consent/contract basis + automated means) are evaluated on every request; Art. 20(4) exclusions (no public-interest-task or legitimate-interest processing) are honoured without prejudice to the Art. 21 right to object; the Art. 20(3) third-party-rights carve-out (refusal where export would adversely affect third-party rights and freedoms) is honoured as the structural qualifier on the right; where the portability-eligible data resides in a CRA-classified product, the controller-side Art. 20 export pipeline is supported architecturally by the CRA Annex I Part I (2)(m) second-limb secure cross-product transfer mechanism (confidentiality + integrity + destination-authentication per PR.DS-02 — manufacturer-side architectural obligation, NOT a portability right) and the cross-controller direct transmission (Art. 20(2) sentence 2) is provided where technically feasible via mutually-authenticated transport encryption + signed export manifests; Art. 13(2)(b) / Art. 14(2)(c) information-supply notifies the data subject of the right at collection (the right exists + the categories of personal data concerned); Art. 30(1)(b) RoPA record documents categories of data subjects + categories of personal data; Art. 35(7) DPIA is performed where applicable; Art. 5(2) accountability evidence is inspection-ready; verified by portability export format audit + service-level review + consent/contract-basis eligibility check + cross-controller transmissi... (line truncated to 2000 chars)
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-10, PR.DS-12]
  applicable_if:
    regs: [GDPR]
    scope_overlap: Y   # HL engages only when GDPR in applicable_regs AND portability-eligible personal data exists (Art. 6(1)(a) consent or Art. 6(1)(b) contract basis + Art. 20(3) automated-means requirement); single-regulator sub-domain — the HL is redundant in this single-regulator case but is emitted for traceability per the activation model
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Single-participant sub-domain — GDPR is the SOLE AUTHORITY for D-05.4 per AEGIS taxonomy §4.1; NIS 2, CRA, DORA, AI Act are all out-of-scope at the regulatory layer; CRA is cited as a technical anchor only. The CRA Annex I Part I (2)(m) second-limb secure cross-product transfer (SR-CRA-049) is a complementary technical anchor when the portability-eligible personal data resides in a CRA-classified product — the manufacturer's secure-transfer mechanism (confidentiality + integrity + destination-authentication) is the architectural substrate that makes the Art. 20 cross-controller transmission operationally feasible; the CRA mechanism is NOT a portability right (it is a manufacturer-side architectural obligation addressed to the product, not a data-subject right per Art. 20) and does NOT ground a CRA sub-SO on D-05.4. The regulatory-right layer (GDPR Art. 20 against the controller) and the technical-anchor layer (CRA Annex I Part I (2)(m) second limb against the manufacturer when data resides in a CRA-classified product) are **distinct layers — not collapsed and not aggregated** by the high-level SO. The structured-interoperable reading of `commonly used electronic form` (JSON, CSV, XML per EDPB Guidelines 06/2020) is the format-quality floor — print-ready rendering (PDF or scanned image) is rejected as defeating the purpose; controller-preferred proprietary format is rejected as functionally obstructing; the high-level SO specifies the structural floor (machine-readable; structured; commonly used; interoperable downstream) and the service-level calibration anchor (Art. 12(3) ≤1 month, ≤2 months for complex requests) without specifying a single format or clock. The Art. 20(3) conditions + Art. 20(4) exclusions + third-party-rights carve-out are the scope-qualifier architecture: portability applies only when consent/contract basis AND automated means; portability does NOT apply to public-interest-task or legitimate-interest processing; the controller may refuse an e... (line truncated to 2000 chars)
```
---

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-05.4
title: D-05.4 Data Portability — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.4 Data Portability
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md
status: DRAFT
---
> **Deep analysis:** [D-05.4 Data Portability](../../DeepAnalysis/D-05_Data-Lifecycle/D-05.4.md)
#### D-05.4 Data Portability
<!-- participants: GDPR -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-020 | Data subject receives personal data in structured, commonly used, machine-readable format and can transmit to another controller (Art. 20 + Art. 15(3)) | Personal data; data-subject right |
| NIS2 | — | Out-of-scope (sole authority: GDPR) | n/a |
| CRA | — | Out-of-scope (sole authority: GDPR) | n/a |
| DORA | — | Out-of-scope (sole authority: GDPR) | n/a |
| AI_Act | — | Out-of-scope (sole authority: GDPR) | n/a |
**Sole-authority note:** NIS2, CRA, DORA, and AI Act are all out-of-scope for D-05.4 per AEGIS taxonomy §4.1. GDPR Art. 20 is the SOLE AUTHORITY. The CRA Annex I Part I (2)(m) secure cross-product data transfer (SR-CRA-049) overlaps at the *technical* level (secure transfer mechanism) but does not constitute a portability *right* — it is a manufacturer-side architectural obligation, not a data-subject right.
##### Pairwise matrix
No applicable pairs — only one participant (GDPR).
##### Emergent tensions (3+ regulations)
None.
##### SR cross-validation
NIST CSF 2.0 anchoring via **PR.DS-10** (Data-in-use protected) and **PR.DS-12** (Data disposal managed). Single-regulation; CSF mapping is consistent.
##### Downstream implication
Phase 2 obligation derivation produces a single-track portability rule. Phase 3 case generation validates that case companies expose an Art. 20 export function for personal data. The CRA cross-product transfer mechanism (SR-CRA-049) should be cited as a *complementary* technical anchor when the data resides in a CRA-classified product, but it does not substitute for the GDPR Art. 20 right.
---
### D-06 Supply Chain
---

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-05.4
title: D-05.4 Data Portability — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.4 Data Portability
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md
status: DRAFT
---
> **Domain analysis:** [D-05.4 Data Portability](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.4.md)
#### D-05.4 Data Portability
<!-- participants: GDPR (sole authority) -->
**Participants (from CRDA):** GDPR (sole authority)
**Sole-authority note:** NIS2, CRA, DORA, and AI Act are all out-of-scope for D-05.4 per AEGIS taxonomy §4.1. GDPR Art. 20 is the SOLE AUTHORITY. The CRA Annex I Part I (2)(m) secure cross-product data transfer (SR-CRA-049) overlaps at the *technical* level (secure transfer mechanism) but does not constitute a portability *right* — it is a manufacturer-side architectural obligation, not a data-subject right.
**Pairwise matrix:** No applicable pairs — only one participant (GDPR).
**NIST CSF 2.0 anchoring:** **PR.DS-10** (Data-in-use protected) and **PR.DS-12** (Data managed consistent with risk strategy). Single-regulation; CSF mapping is consistent.
**Downstream implication (Phase 1C Doc 07):** Phase 2 obligation derivation produces a single-track portability rule. Phase 3 case generation validates that case companies expose an Art. 20 export function for personal data. The CRA cross-product transfer mechanism (SR-CRA-049) should be cited as a *complementary* technical anchor when the data resides in a CRA-classified product, but it does not substitute for the GDPR Art. 20 right.
---
### D-06 Supply Chain
---

