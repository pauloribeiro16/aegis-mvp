<!-- aegis:case-scope: GDPR, CRA, NIS2, DORA, AI_Act — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-09.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-09.3 Asset Inventories](../../DomainAnalysis/D-09_Governance-Documentation/D-09.3.md)
#### D-09.3 Asset Inventories
<!-- participants: NIS2, CRA, DORA -->
**Participants (from CRDA):** NIS2, CRA, DORA
**Sole-authority note (CRDA flag):** DORA Art. 7(1) is the dedicated authority — explicit `identify, classify, adequately document` mandate on the `3-way AND` of ICT supported business functions + information assets + ICT assets. NIS 2 and CRA provide partial coverage only.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-09.3 Asset Inventories
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md)
> (3 pairs verified against OJ text — **3 participating regulations
> are NIS 2, CRA, DORA; GDPR + AI Act are explicitly out-of-scope** as
> noted by `DomainAnalysis/D-09_Governance-Documentation/D-09.3.md`
> line 27: "Participants: NIS2, CRA, DORA" and line 80: "DORA sole-
> authority taxonomy assignment is OJ-supported … DORA is the sole
> authority for D-09.3. Unlike D-07.2 (where the sole-authority
> assignment is OJ-text-unsupported), D-09.3's sole-authority is
> OJ-literal (Art. 7(1) explicit `identify, classify, adequately
> document` mandate on the `3-way AND` of ICT supported business
> functions + information assets + ICT assets)").
>
> **Critical note (CRDA flag — DORA sole authority).** D-09.3 has the
> **DORA Art. 7(1) dedicated authority** for entity-level ICT asset
> inventories. The three pairs verify as: **1 SAME — COMPLEMENTARY
> (NIS 2 ↔ CRA — scope-disjoint `N (typically)` per CRDA) + 1 SAME —
> EQUAL (NIS 2 ↔ DORA on entity-level asset inventory, DORA-dominant)
> + 1 SAME — COMPLEMENTARY (CRA ↔ DORA — Conditional-Y, CRA
> documentation feeds DORA asset register)**. **No CORRECTED, no
> CONTRADICTORY** pairs. The high-level SO surfaces the **common
> entity-level asset-inventory duty** (identification + classification
> + documentation of ICT supported business functions + information
> assets + ICT assets + dependencies), with DORA Art. 7(1) as the
> dedicated authority for DORA financial entities and NIS 2 Art.
> 21(2)(i) + CRA Annex VII §1-§2 as partial-coverage inputs.
>
> **Critical note (CRDA flag — NIS 2 ↔ CRA substantive scope-disjoint).**
> Per CRDA-deep `§D-09.3 line 66`: "Substantively scope-disjoint;
> CRDA 'complementary' is a taxonomy artifact" — the pair operates on
> **different objects** (entity asset register vs. product
> architecture documentation) serving **different audit purposes**
> (entity-level NCA/MSA review vs. product-level MSA review). The two
> regimes meet at the **supplier-customer interface** (CRA-conformant
> product is an input to the NIS 2 entity's asset register).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-09.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SG-NIS2-003 (primary, partial) + SG-NIS2-021 (cross) | Entity-level asset-management sub-domain coordinated with access control (Art. 21(2)(i) `human resources security, access control policies and asset management`) + management-body oversight of Art. 21 measures (Art. 20(1)). | Partial coverage via access-control coordination; no dedicated asset-inventory mandate; NIS 2 does not impose a dedicated asset-inventory mandate (NIS 2 participant note: "NIS 2 does not impose a dedicated asset-inventory mandate"). |
| CRA | SG-CRA-061 (partial) | Annex VII §1 `general description` (intended purpose + software versions affecting compliance) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other). | Documentation-centric, not a formal asset register in the DORA sense; **partial coverage only**; **substantively scope-disjoint from NIS 2** per CRDA `N (typically)` (per CRDA-deep `§D-09.3 line 66`). |
| DORA | SG-DORA-017 (sole authority) | Identify, classify, and adequately document ICT supported business functions + roles and responsibilities + information assets + ICT assets + their roles and dependencies in relation to ICT risk (Art. 7(1)). | Entity-level formal asset inventory; **the dedicated authority per AEGIS taxonomy §4.1** (OJ-literal Art. 7(1) 3-way AND); DORA-dominant for DORA financial entities. |
| GDPR | (out-of-scope as strict mandate) | RoPA focus on processing purposes, data categories, recipients, safeguards — not information assets. No standalone SO for D-09.3 from GDPR. | RoPA is a related-but-distinct artefact (see D-09.4). |
| AI_Act | (out-of-scope) | AI Act does not impose an asset-inventory mandate. | — |

## Validated relationships (from CRDA-deep §D-09.3)

#### Validated relationships (from CRDA-deep §D-09.3)
Of 3 pairs, **3 verified as SAME — no CORRECTED, no CONTRADICTORY**. The 3 verified relationships are distributed as **1 SAME — COMPLEMENTARY (NIS 2 ↔ CRA — substantively scope-disjoint per CRDA `N (typically)`) + 1 SAME — EQUAL (NIS 2 ↔ DORA — DORA-dominant for financial entities) + 1 SAME — COMPLEMENTARY (CRA ↔ DORA — Conditional-Y)**. **The three participating regulators look at the asset-inventory duty from three distinct regulatory perspectives**, with DORA Art. 7(1) as the dedicated OJ-literal authority for entity-level asset-inventory; NIS 2 Art. 21(2)(i) + CRA Annex VII §1-§2 provide partial coverage that **does not collapse into the DORA-dominant stack**:
- **NIS2 ↔ CRA** — COMPLEMENTARY (SAME) **with critical CRDA scope-disjoint flag**: NIS 2 covers **entity-level asset management** via Art. 21(2)(i) `human resources security, access control policies and asset management` (partial coverage, one of three coordinated sub-domains of access control); CRA covers **product-level architecture documentation** via Annex VII §1 `general description` + Annex VII §2 `design, development, production and vulnerability-handling processes` (partial coverage, documentation-centric). **Scope-disjoint test: `N (typically)`** — different objects (entity asset register vs. product architecture documentation); substantively scope-disjoint. Per CRDA-deep `§D-09.3 line 66`: "CRDA `complementary` is a taxonomy artifact". The two regimes meet at the **supplier-customer interface** — CRA Annex VII §1-§2 architecture documentation (per SR-CRA-087) feeds the NIS 2 entity's asset register (per SR-NIS2-005). No reclassification required. The high-level SO does **NOT** collapse the two artefacts because they serve different audit purposes.
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose **asset-inventory obligations** at the entity level. NIS 2: Art. 21(2)(i) `human resources security, access control policies and asset management` (partial via access-control coordination; entity-discretionary under Recital 56 proportionality per SR-NIS2-005). DORA: Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` (sole authority, the dedicated OJ-literal anchor). **DORA Art. 7(1) is the dominant authority** for DORA financial entities; the explicit OJ-literal `identify, classify and adequately document` mandate on the `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies is more prescriptive than the NIS 2 partial-coordination approach. For DORA financial entities, the DORA entity-level asset inventory discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension (cross-coupled via access-control). DORA Art. 7(1) is the operationalised identifier; **CRDA flag** per CRDA-deep `§D-09.3 line 105`: "DORA Art. 7(1) is the dominant authority with explicit OJ-literal anchor. NIS 2 Art. 21(2)(i) is partial via access-control coordination." Scope-disjoint test: **Y (when a DORA financial entity is also an NSIE)**. No reclassification required.
- **CRA ↔ DORA** — COMPLEMENTARY (SAME): CRA architecture documentation feeds the DORA entity's asset register. CRA scope: Annex VII §1-§2 general description + architecture documentation (documentation-centric). DORA scope: Art. 7(1) `identify, classify, adequately document` (the dedicated authority; entity-level master record). **DORA's ICT asset inventory is the entity-level master record; CRA Annex VII §1-§2 is the product-level sub-register** — the two artefacts operate on different layers (CRA on the product layer; DORA on the entity layer). Per CRDA-deep `§D-09.3 line 146`: "CRA architecture documentation feeds the DORA entity's asset register. DORA's ICT asset inventory is the entity-level master record; CRA Annex VII §1-§2 is the product-level sub-register." Scope-disjoint test: **Conditional (Y when the DORA entity procures CRA-conformant products; N otherwise)**. No reclassification required. The DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register.
The asset-inventory architecture is **legitimately diverse with DORA Art. 7(1) sole-authority + NIS 2 + CRA partial coverage**. The three regulators impose asset-inventory artefacts from three distinct regulatory perspectives under three distinct anchors: **NIS 2 Art. 21(2)(i) entity-level partial asset-management coordination** (with access control as the converging sub-domain; asset-management is one of three coordinated sub-domains of access control); **CRA Annex VII §1-§2 product-level partial architecture documentation** (documentation-centric; the general description and architecture description of how software components build on or feed into each other); **DORA Art. 7(1) financial-entity dedicated asset inventory** (the dedicated authority; explicit OJ-literal `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies). **The CRDA substantively scope-disjoint flag on NIS 2 ↔ CRA is structurally significant** — the pair operates on different objects (entity asset register vs. product architecture documentation) serving different audit purposes; no OJ-level consolidation rule exists between NIS 2 and CRA for the asset-inventory object. The high-level SO does **NOT** collapse the entity-level asset register with the product-level architecture documentation; the two artefacts stack on the supplier-customer interface.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |  NIS2  |  CRA  |  DORA  |
| --- | --- | --- | --- |
|  **NIS2**  |  —  |  **N (typically)** — different objects (entity asset register vs. product architecture documentation); substantively scope-disjoint per CRDA; CRDA `complementary` is a taxonomy artifact; the two regimes meet at the supplier-customer interface (CRA-conformant product is an input to the NIS 2 entity's asset register)  |  Y (DORA financial entity is also an NSIE; DORA Art. 7(1) `identify, classify, adequately document` is the dominant authority with explicit OJ-literal anchor — DORA-dominant stack discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension — EQUAL on entity-level asset inventory)  |
|  **CRA**  |  **N (typically)** (same; reciprocal — substantively scope-disjoint per CRDA — entity asset register vs. product architecture documentation; different audit purposes)  |  —  |  Conditional (Y when DORA entity procures CRA-conformant products; N otherwise — CRA Annex VII §1-§2 architecture documentation feeds the DORA asset register; DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register)  |
|  **DORA**  |  Y (same; reciprocal — DORA financial entity is NSIE; DORA-dominant stack discharges both — EQUAL on entity-level asset inventory)  |  Conditional (Y when DORA entity procures CRA-conformant; same; reciprocal — DORA-led stack with CRA Annex VII §1-§2 architecture documentation as upstream product-level sub-register)  |  —  |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **N (typically)** = substantively scope-disjoint per CRDA — no same-event overlap (high-level SO does **NOT** engage on this pair; CRDA `complementary` is a taxonomy artifact). **Conditional (Y/N)** = conditional overlap depending on entity-product combination — Y when the listed entity-product combination applies on a single party, N otherwise. CRDA-deep scope-disjoint tests: NIS2↔CRA = **N (typically)** — substantively scope-disjoint; NIS2↔DORA = Y; CRA↔DORA = Conditional (Y when DORA entity procures CRA-conformant products).

## Cross-recipient map

#### Cross-recipient map
D-09.3 generates a layered recipient set on the **asset-inventory evidence trail** but does **not generate a notification cascade of D-09.3 itself**. The recipient set is at the **asset-inventory-evidence layer**: **NIS 2's management body + competent authority** on the Art. 21(2)(i) `human resources security, access control policies and asset management` asset-management sub-domain + Art. 20(1) management-body approval records (cross-coupled with the policy-architecture requirement at D-09.1); **CRA's market surveillance authority (MSA)** on the Annex VII §1 `general description` + Annex VII §2 `design, development, production and vulnerability-handling processes` (per SR-CRA-087) + 10-year technical-documentation retention per Art. 13(13) (cross to D-09.4) + conformity-assessment records per Art. 27 + Article 31(2) `drawn up before placing on the market and updated during the support period`; **DORA's competent authority (NCA — national financial supervisory authority)** on the Art. 7(1) `identify, classify, adequately document` ICT asset register + Art. 6(4) three-lines-of-defence + EBA Guidelines on ICT and security risk management supervisory baseline. These are distinct regulatory channels on the same asset-inventory artefacts but they do not generate a notification cascade of D-09.3 itself — they are **compliance-evidence channels on the layered asset-inventory architecture**. GDPR's DPA is **NOT** a recipient because GDPR is explicitly out-of-scope for D-09.3 (RoPA is a related-but-distinct artefact at D-09.4). The AI Act MSA + AI Office is **NOT** a recipient because the AI Act is explicitly out-of-scope for D-09.3 (no asset-inventory mandate). The **D-09.1 (Information Security Policies)** is the upstream policy artefact where the asset-inventory architecture is governed by the documented policies; **D-09.4 (Records of Processing)** is the documentation-evidence downstream artefact where the asset register itself is one of the records to be retained (CRA Annex VII §1-§2 technical documentation; DORA ICT asset register documentation; NIS 2 entity-discretionary record). **D-09.2 (Impact & Risk Assessments)** is the operational downstream artefact where asset-classification feeds the entity-risk register. **D-06.1 (Vendor Risk Assessment)** is the supplier-side downstream where the CRA Annex VII §1-§2 architecture documentation (via the NIS 2 supplier-customer interface) is an input to the NIS 2 entity's supplier-risk register (cross-coupled via access control).
---

## HSO considerations (from D-09.3.0 — High-level SecurityObjective)

**Considerations.**
- **3 of 5 regulations participate** (NIS 2, CRA, DORA — **GDPR + AI Act explicitly out-of-scope** per CRDA). NIS 2 Art. 21(2)(i) provides **partial coverage** via access-control coordination (asset-management is one of three coordinated sub-domains of access control); CRA Annex VII §1-§2 provides **partial coverage** (documentation-centric — general description + architecture description, not a formal asset register in the DORA sense); **DORA Art. 7(1) is the dedicated authority** with explicit OJ-literal `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies.
- **CRDA-deep verified (3 pairs: 1 SAME — COMPLEMENTARY NIS 2 ↔ CRA — substantively scope-disjoint per CRDA `N (typically)`, different objects (entity asset register vs. product architecture documentation), CRDA `complementary` is a taxonomy artifact; + 1 SAME — EQUAL NIS 2 ↔ DORA on entity-level asset inventory, DORA-dominant; + 1 SAME — COMPLEMENTARY CRA ↔ DORA, Conditional-Y when DORA entity procures CRA-conformant products)** — no CORRECTED, no CONTRADICTORY. The high-level SO does NOT collapse the entity-level asset register with the product-level architecture documentation.
- **DORA sole-authority flag (per AEGIS taxonomy §4.1, OJ-literal)** distinguishes D-09.3 from D-07.2 where the sole-authority assignment is OJ-text-unsupported; NIS 2 and CRA provide partial coverage only.
- **Scope caveats**: (a) NIS 2 ↔ CRA substantively scope-disjoint (entity asset register vs. product architecture documentation) — different audit purposes (entity-level NCA review vs. product-level MSA review), the two regimes meet only at the supplier-customer interface; (b) NIS 2 ↔ DORA EQUAL discharges both on the DORA-dominant stack for financial entities; (c) CRA ↔ DORA is DORA-led with CRA Annex VII §1-§2 as upstream product-level sub-register feeding the DORA entity-level master record.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 3 participating regulations each define D-09.3 over a distinct **asset-inventory artefact** of the entity's asset management; the anchor, governance body, trigger, threshold, recipient, and legal anchor all depend on which perspective the regulation takes on the asset object.
| Axis (reg) | Asset-inventory artefact | Anchor (OJ-literal) | Governance body | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **NIS 2** | entity-level asset-management sub-domain coordinated with access control — partial coverage via access-control coordination; asset-management is one of three coordinated sub-domains of access control (HR security + access control + asset management) | Art. 21(2)(i) `human resources security, access control policies and asset management` | management body (Art. 20(1) sentence 1 `management bodies … approve the cybersecurity risk-management measures … oversee their implementation and can be held liable`) — NIS 2 sub-SO inherits the management-body approve/oversee/liable architecture from D-09.1 | management body + competent authority — Art. 21(2)(i) asset-management sub-domain + Art. 20(1) management-body approval records | Art. 21(2)(i) partial-coverage asset-management sub-domain + Art. 20(1) sentence 1 management-body approve/oversee/liable + Art. 21(1) chapeau `appropriate and proportionate` proportionality hook + Recital 56 proportionality |
| **CRA** | product-level technical documentation: Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production, and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other) — **partial coverage, documentation-centric, not a formal asset register in the DORA sense** | Annex VII §1 `general description` + Annex VII §2 `design, development, production, and vulnerability-handling processes` (per SR-CRA-087) | manufacturer (Art. 13(8) manufacturer policies/processes/procedures owner — cross to D-09.1) — distinct from data-protection governance body | market surveillance authority (MSA) — Annex VII §1 `general description` + Annex VII §2 `design, development, production, and vulnerability-handling processes` + 10-year technical-documentation retention per Art. 13(13) (cross to D-09.4) + conformity-assessment records per Art. 27 + Article 31(2) `drawn up before placing on the market and updated during the support period` | Annex VII §1 + Annex VII §2 (per SR-CRA-087) + Art. 31(1) `technical documentation … contain Annex I compliance evidence` + Art. 31(2) `drawn up before placing and updated during the support period` + Art. 13(13) `10-year documentation retention` + Art. 27(1)/(2)/(5)/(8)/(9) presumption-of-conformity machinery (cross to D-09.1) |
| **DORA** | financial-entity dedicated asset inventory: ICT supported business functions + roles and responsibilities + information assets + ICT assets + their roles and dependencies in relation to ICT risk — **entity-level formal asset inventory with explicit OJ-literal `3-way AND`** — **the dedicated authority per AEGIS taxonomy §4.1** | Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` (per SR-DORA-029) + Art. 6(4) three-lines-of-defence model | management body (Art. 5(2) four-verb coordination: define/approve/oversee/be responsible — cross to D-09.1) + control function with appropriate level of independence per three-lines-of-defence (Art. 6(4)) | competent authority (NCA — national financial supervisory authority) + management body — Art. 7(1) ICT asset register + Art. 6(4) three-lines-of-defence + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 7(1) `identify, classify, adequately document` 3-verb + `3-way AND` of ICT supported business functions + information assets + ICT assets + roles and dependencies (per SR-DORA-029) + Art. 6(4) three-lines-of-defence (per SR-DORA-017 cross) + Art. 5(2) management-body oversight (cross to D-09.1) + Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities` |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-09.3.HL`) engages on a given party **if and only if ≥2
applicable regulations have ≥1 Y or Conditional-Y-scope-overlap pair
on the same party** where both regimens operate on the **same
asset-inventory object**. For an integrated DORA financial entity
that is also an NSIE, the **NIS 2 ↔ DORA EQUAL pair** engages the
high-level SO on the entity-level asset inventory (DORA Art. 7(1)
dominant authority; NIS 2 Art. 21(2)(i) partial-coverage via
access-control coordination is discharged on the DORA stack). For a
DORA financial entity that procures CRA-conformant products, the
**CRA ↔ DORA COMPLEMENTARY pair** engages the high-level SO with the
DORA-led stack (DORA Art. 7(1) entity-level master record + CRA
Annex VII §1-§2 architecture documentation as upstream product-level
sub-register). For an NSIE that is not a DORA financial entity and
that is not a manufacturer (i.e. no CRA Annex VII §1-§2 documentation
duty), the high-level SO does **NOT** engage because only one
participating reg (NIS 2) has an asset-inventory partial-coverage
obligation; the NIS 2 Art. 21(2)(i) partial-coverage asset-management
sub-domain stands alone. **The NIS 2 ↔ CRA pair never engages the
high-level SO** because it is **substantively scope-disjoint per CRDA
`N (typically)`** — different objects (entity asset register vs.
product architecture documentation) on a single party; CRDA
`complementary` is a taxonomy artifact and the two regimes meet at
the supplier-customer interface without OJ-level consolidation. The
two artefacts are stacked on the supplier-customer interface (NIS 2
entity-side asset register + CRA manufacturer-side Annex VII §1-§2
technical documentation as upstream product sub-register), not
collapsed.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **3 of 5 regulations participate** (NIS 2, CRA, DORA — GDPR + AI Act
  explicitly out-of-scope per CRDA): NIS 2 (Art. 21(2)(i) +
  Art. 20(1) management-body approve/oversee/liable as
  entity-level partial asset-management coordination via
  access-control sub-domain); CRA (Annex VII §1-§2 as product-level
  partial architecture documentation); DORA (Art. 7(1) +
  Art. 6(4) + Art. 5(2) as financial-entity dedicated asset
  inventory with explicit OJ-literal `3-way AND`).
- **3 pairwise cells, verified by CRDA-deep**:
  NIS2↔CRA (SAME — COMPLEMENTARY — substantively scope-disjoint per
  CRDA `N (typically)` — different objects, entity asset register vs.
  product architecture documentation; substantively scope-disjoint;
  CRDA `complementary` is a taxonomy artifact);
  NIS2↔DORA (SAME — EQUAL — both regulations impose entity-level
  asset-inventory obligations; DORA Art. 7(1) is the dominant
  authority with explicit OJ-literal anchor; NIS 2 Art. 21(2)(i) is
  partial via access-control coordination; DORA-dominant for
  financial entities);
  CRA↔DORA (SAME — COMPLEMENTARY — Conditional-Y scope overlap when
  DORA entity procures CRA-conformant products; CRA Annex VII §1-§2
  architecture documentation feeds the DORA entity's asset register;
  DORA-led stack with CRA Annex VII §1-§2 as upstream product-level
  sub-register).
- The **sole-authority flag** on DORA Art. 7(1) is structurally
  significant: DORA is the dedicated authority per AEGIS taxonomy
  §4.1, with explicit OJ-literal `identify, classify, adequately
  document` mandate on the `3-way AND` of ICT supported business
  functions + information assets + ICT assets + roles + dependencies.
  Per CRDA DomainAnalysis §D-09.3 line 80, this distinguishes D-09.3
  from D-07.2 where the sole-authority assignment is OJ-text-
  unsupported. NIS 2 and CRA provide partial coverage only.
- The **substantive scope-disjoint flag** on NIS 2 ↔ CRA is
  structurally significant: per CRDA-deep §D-09.3 line 66, the two
  regimes operate on different objects (entity asset register vs.
  product architecture documentation) serving different audit
  purposes; CRDA `complementary` is a taxonomy artifact. No OJ-level
  cross-referencing exists; the two regimes meet at the
  supplier-customer interface only (CRA-conformant product is an
  input to the NIS 2 entity's asset register). Phase 1 entities with
  NIS 2 + CRA applicability must discharge both obligations
  separately.
- The three participating regulators impose **distinct
  asset-inventory artefacts** at **distinct anchors** with **distinct
  governance bodies**: NIS 2 (Art. 21(2)(i) entity-level partial
  asset-management coordination via access-control sub-domain;
  management-body approve/oversee/liable per Art. 20(1);
  entity-discretionary under Recital 56 proportionality); CRA
  (Annex VII §1-§2 product-level partial architecture documentation;
  manufacturer as governance body; 10-year technical-documentation
  retention per Art. 13(13); partial content codification via Annex
  VII §1-§2); DORA (Art. 7(1) financial-entity dedicated asset
  inventory with explicit OJ-literal `3-way AND`; management-body
  define/approve/oversee/be responsible per Art. 5(2); three-lines-
  of-defence per Art. 6(4); Art. 4 proportionality entity-
  discretionary). The thresholds align qualitatively (no regulation
  imposes a quantitative inventory cadence — all entity-discretionary
  under proportionality or equivalent). The three anchors align in
  their direction-of-travel (entity-level asset register + product-
  level architecture documentation + entity-level master record with
  product sub-register) but the artefacts, governance bodies,
  content templates, recipients, evidentiary templates diverge.
- The high-level SO describes the **COMMON OBJECTIVE**
  (entity-level asset inventory with identification +
  classification + documentation of ICT supported business
  functions + information assets + ICT assets + roles + dependencies,
  with DORA Art. 7(1) as the dedicated authority for DORA financial
  entities and NIS 2 Art. 21(2)(i) + CRA Annex VII §1-§2 as
  partial-coverage inputs); the **per-regulation perspective**
  (artefact, governance body, anchor, content template, threshold,
  recipient, evidence template) is preserved verbatim in the 3
  sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the asset-inventory duty
  itself**, because no pair was verified as CONTRADICTORY or
  CORRECTED (all 3 pairs are SAME — 1 SAME — COMPLEMENTARY + 1 SAME
  — EQUAL + 1 SAME — COMPLEMENTARY). Phase 1C Doc 07 does not need
  to resolve an asset-inventory-object contradiction because none
  exist by construction; however, **Phase 1C Doc 07 must perform the
  Layer 1 cross-cutting asset-inventory-architecture mapping**
  because the 3 regulators impose 3 distinct asset-inventory
  artefacts with no OJ-level consolidation rule (DORA sole authority
  with NIS 2 partial coverage + CRA partial coverage; CRA Annex VII
  §1-§2 architecture documentation as upstream product sub-register
  via the supplier-customer interface to the DORA entity-level
  master record; the substantive NIS 2 ↔ CRA scope-disjoint gap
  requires no cross-substitution between the two artefacts).
- **Scope caveat (CRITICAL — DORA Art. 7(1) sole authority
  OJ-supported)** — derived from CRDA-deep verified classifications:
  DORA Art. 7(1) is the dedicated authority per AEGIS taxonomy §4.1
  with explicit OJ-literal `identify, classify, adequately document`
  mandate on the `3-way AND` of ICT supported business functions +
  information assets + ICT assets + roles + dependencies. NIS 2 and
  CRA provide partial coverage only. Phase 1 entities with DORA
  applicability must maintain the DORA-compliant asset register (Art.
  7(1)) as the entity-level master record. For DORA financial
  entities that are also NSIEs, the NIS 2 Art. 21(2)(i) partial-
  coverage asset-management dimension is discharged on the DORA
  stack. For DORA financial entities that procure CRA-conformant
  products, the CRA Annex VII §1-§2 architecture documentation is an
  upstream product-level sub-register feeding the DORA entity-level
  master record.
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA EQUAL classification on
  entity-level asset inventory)** — derived from CRDA-deep verified
  classifications: both regulations impose entity-level
  asset-inventory obligations (NIS 2 Art. 21(2)(i) `human resources
  security, access control policies and asset management` partial
  via access-control coordination; DORA Art. 7(1) explicit
  `identify, classify, adequately document` mandate on the `3-way
  AND`). DORA Art. 7(1) is the dedicated authority and is more
  prescriptive than NIS 2's Art. 21(2)(i) partial-coverage approach.
  For DORA financial entities, the DORA entity-level asset inventory
  discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's
  Art. 21(2)(i) partial-coverage asset-management dimension —
  DORA-dominant under DORA's direct scope. For non-financial NSIEs,
  NIS 2 Art. 21(2)(i) partial coverage stands alone (no DORA Art.
  7(1) obligation).
- **Scope caveat (CRITICAL — NIS 2 ↔ CRA substantive scope-disjoint
  flag)** — derived from CRDA-deep verified classifications:
  per CRDA-deep §D-09.3 line 66, the pair is **substantively
  scope-disjoint on a single event at a single party** — different
  objects (entity asset register vs. product architecture
  documentation) serving different audit purposes (entity-level NCA
  review vs. product-level MSA review). The two regimes meet at the
  **supplier-customer interface** only (CRA-conformant product is an
  input to the NIS 2 entity's asset register). CRDA `complementary`
  is a taxonomy artifact. Phase 1 entities with NIS 2 + CRA
  applicability (non-DORA manufacturer + NSIE) must discharge both
  obligations separately on distinct artefacts that are not
  substitutable.
---

## Emergent tensions (from CRDA-deep §D-09.3)

#### Emergent tensions (from CRDA-deep §D-09.3)
**0 conditional emergent tensions** on the asset-inventory duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 3 pairs are all SAME — 1 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 1 SAME — COMPLEMENTARY. **No CORTRADICTORY or CORRECTED reclassifications** — CRDA preserves every pair as SAME.
The **DORA sole-authority flag (CRDA DomainAnalysis §D-09.3 line 80)** is the structurally significant operational divergence — DORA Art. 7(1) is the dedicated authority per AEGIS taxonomy §4.1 with explicit OJ-literal `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies; NIS 2 and CRA provide partial coverage only. **This distinguishes D-09.3 from D-07.2** where the sole-authority assignment is OJ-text-unsupported. Phase 1 entities with DORA applicability must maintain the DORA-compliant entity-level master record (Art. 7(1)) as the entity-level asset register. For DORA financial entities that are also NSIEs, the DORA Art. 7(1) `3-way AND` discharges both regulations on the EQUAL pair. For DORA financial entities that procure CRA-conformant products, the CRA Annex VII §1-§2 architecture documentation is the upstream product-level sub-register feeding the DORA entity-level master record on the COMPLEMENTARY pair.
The **substantive scope-disjoint flag on NIS 2 ↔ CRA (CRDA-deep §D-09.3 line 66)** is the structurally significant operational divergence — the pair operates on **different objects** (entity asset register vs. product architecture documentation) serving **different audit purposes** (entity-level NCA review vs. product-level MSA review). CRDA `complementary` is a taxonomy artifact. The two regimes meet at the **supplier-customer interface** only (CRA-conformant product is an input to the NIS 2 entity's asset register). No OJ-level cross-referencing exists between NIS 2 and CRA for the asset-inventory object. Phase 1 entities with NIS 2 + CRA applicability (non-DORA manufacturer + NSIE) must discharge both obligations separately on distinct artefacts that are not substitutable.
The **NIS 2 ↔ DORA EQUAL classification on entity-level asset inventory** is the structurally significant EQUAL pair: both regulations impose entity-level asset-inventory obligations (NIS 2 Art. 21(2)(i) partial via access-control coordination; DORA Art. 7(1) explicit `3-way AND`). **DORA Art. 7(1) is more prescriptive than NIS 2 Art. 21(2)(i)** — the dedicated authority with the `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies. For DORA financial entities, the DORA Art. 7(1) entity-level `3-way AND` inventory discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension — DORA-dominant under DORA's direct scope (EQUAL classification). For non-financial NSIEs, the NIS 2 Art. 21(2)(i) partial-coverage asset-management sub-domain stands alone (no DORA Art. 7(1) obligation).
The **CRA ↔ DORA COMPLEMENTARY pair on DORA-led stack** is the structurally significant COMPLEMENTARY pair: CRA Annex VII §1-§2 architecture documentation feeds the DORA entity-level asset register; DORA's ICT asset inventory is the entity-level master record; CRA Annex VII §1-§2 is the product-level sub-register. The two artefacts operate on different layers (CRA on the product layer; DORA on the entity layer). The DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register is operationalised at the supplier-customer interface; no OJ-level cross-referencing exists between CRA and DORA for the asset-inventory object.
The high-level SO surfaces the **common entity-level asset-inventory duty** (identification + classification + documentation of the `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies) with **DORA Art. 7(1) as the dedicated authority** for DORA financial entities and NIS 2 Art. 21(2)(i) + CRA Annex VII §1-§2 as partial-coverage inputs serving distinct audit purposes (entity-level NCA review, product-level MSA review, supplier-customer interface for cross-layer integration). The per-reg perspective on the asset-inventory artefact, anchor, governance body, content template, threshold, recipient, and evidence template is documented separately in the 3 sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 3-distinct-artefacts structure (NIS 2 partial via access control / CRA partial via Annex VII §1-§2 / DORA Art. 7(1) dedicated authority) with the substantive scope-disjoint flag on NIS 2 ↔ CRA is itself the structural reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-09.3 — with overlapping asset-inventory scope-determiners on the same party — operates a **layered 3-artefact asset-inventory architecture** with **DORA Art. 7(1) as the dedicated authority** (when DORA applies) and partial-coverage inputs from NIS 2 Art. 21(2)(i) (entity-level partial asset-management coordination via access control) + CRA Annex VII §1-§2 (product-level partial architecture documentation). The high-level SO (`SG-D-09.3.HL`) describes the **common entity-level asset-inventory duty** (identification + classification + documentation of the `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies) with DORA Art. 7(1) as the dedicated authority; the per-reg perspective is preserved in the 3 sub-SOs (artefact, governance body, anchor, content template, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 3-artefact structure operationalising the per-reg governance body on the integrated asset-inventory architecture. The high-level SO does NOT collapse the 3 asset-inventory artefacts (NIS 2 partial via access control / CRA partial via Annex VII §1-§2 / DORA Art. 7(1) dedicated authority); the per-reg perspective on the artefact, governance body, anchor, content template, threshold, recipient, and evidence template is preserved verbatim. **The NIS 2 ↔ CRA substantive scope-disjoint flag** means the two artefacts cannot be cross-substituted; they coexist on the supplier-customer interface. Phase 1C Doc 07 documents the **asset-inventory strategy**: (1) a DORA-dominant stack for financial entities with the DORA Art. 7(1) `3-way AND` inventory as the entity-level master record (per SR-DORA-029) and the CRA Annex VII §1-§2 architecture documentation as upstream product-level sub-register (per SR-CRA-087) when CRA-conformant products are procured (Conditional-Y scope overlap); (2) the **DORA sole-authority OJ-supported flag** distinguishing D-09.3 from D-07.2 (OJ-literal `3-way AND`); (3) the **NIS 2 ↔ CRA substantive scope-disjoint flag** preserved as a Layer 1 cross-cutting architecture-mapping item (no OJ-level consolidation; entity asset register + product architecture documentation on the supplier-customer interface); (4) the **NIS 2 ↔ DORA EQUAL pair** discharges both regulations on the DORA-dominant stack for financial entities under DORA's direct scope; (5) the **CRA ↔ DORA COMPLEMENTARY pair** stacks the CRA Annex VII §1-§2 as upstream product sub-register feeding the DORA entity-level master record (DORA-led stack); (6) **GDPR RoPA is explicitly out-of-scope** for D-09.3 per CRDA explicit note (RoPA is a related-but-distinct artefact at D-09.4, not a strict asset-inventory mandate); (7) **AI Act is explicitly out-of-scope** for D-09.3 per CRDA explicit note (no asset-inventory mandate). The Layer 1 mapping reconciles the 3 asset-inventory artefacts (NIS 2 + CRA + DORA) on the supplier-customer interface (CRA → NIS 2/DORA upstream; DORA Art. 7(1) entity-level master record for financial entities) without OJ-level consolidation.
---
**Document version:** 0.1 — initial derivation from CRDA-deep §D-09.3 (3 pairs verified).
**See also:** [`D-09.1.md`](D-09.1.md) (Information Security Policies — 5-reg participation with no OJ-level consolidation rule); [`D-09.2.md`](D-09.2.md) (Impact & Risk Assessments — 5-reg participation with the **only OJ-level cross-regulation consolidation rule** at CRA Art. 13(4) sentence 2 / AI Act Art. 9 risk-management system); [`D-09.4.md`](D-09.4.md) (Records of Processing — 5-reg participation with 4 documentation regimes + DORA fully absent + no OJ-level consolidation rule for documentation); [`index.md`](../index.md); [`../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md`](../../CrossRegulation/DeepAnalysis/D-09_Governance-Documentation/D-09.3.md) (CRDA-deep source).

## Part 1 §3 — context

### 3. Security Requirements
## 9.3 Asset Inventories — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.3.md`. See that file for the CRDA-deep verified classification (3 pairs: 1 SAME — COMPLEMENTARY (NIS 2 ↔ CRA — substantively scope-disjoint per CRDA `N (typically)` — different objects, entity asset register vs. product architecture documentation; substantively scope-disjoint; CRDA `complementary` is a taxonomy artifact) + 1 SAME — EQUAL (NIS 2 ↔ DORA — DORA Art. 7(1) sole authority with explicit OJ-literal anchor; DORA-dominant for financial entities) + 1 SAME — COMPLEMENTARY (CRA ↔ DORA — Conditional-Y when DORA entity procures CRA-conformant products; CRA Annex VII §1-§2 architecture documentation feeds DORA entity-level master record) — no CORRECTED, no CONTRADICTORY, no scope-disjoint-on-same-party pairs; **3 of 5 regulations participate** (NIS 2, CRA, DORA — **GDPR + AI Act explicitly out-of-scope**), the **DORA Art. 7(1) sole-authority flag** with explicit OJ-literal `identify, classify and adequately document` mandate on the `3-way AND` of ICT supported business functions + information assets + ICT assets + roles + dependencies (distinct from D-07.2 where sole-authority is OJ-text-unsupported), the **NIS 2 ↔ CRA substantive scope-disjoint flag** (entity asset register vs. product architecture documentation serving different audit purposes; CRDA `complementary` is a taxonomy artifact; the two regimes meet at the supplier-customer interface without OJ-level consolidation), the NIS 2 ↔ DORA EQUAL on entity-level asset inventory (DORA-dominant for financial entities), the CRA ↔ DORA COMPLEMENTARY (DORA-led stack with CRA Annex VII §1-§2 as upstream product-level sub-register), the per-reg asset-inventory artefact / governance body / anchor / content template / threshold / recipient / evidence template, and the aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
NIS 2, CRA, DORA (**3 of 5 regulations**; **GDPR + AI Act explicitly out-of-scope** per CRDA: GDPR RoPA focus is on processing purposes / data categories / recipients / safeguards — not information assets (RoPA is a related-but-distinct artefact at 9.4); AI Act does not impose an asset-inventory mandate). Each regulator imposes a **distinct asset-inventory artefact** at a **distinct layer** under a **distinct anchor** with a **distinct governance body**: NIS 2 (Art. 21(2)(i) `human resources security, access control policies and asset management` — entity-level **partial** asset-management coordination via the access-control sub-domain; entity-discretionary under Recital 56 proportionality; management-body approve/oversee/liable per Art. 20(1)) — **partial coverage only**; CRA (Annex VII §1 `general description` (intended purpose + software versions affecting compliance) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other)) — **partial coverage only**, documentation-centric, not a formal asset register in the DORA sense; **DORA** (Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` — financial-entity **dedicated asset inventory** with explicit OJ-literal `3-way AND`; Art. 6(4) three-lines-of-defence; Art. 5(2) management-body define/approve/oversee/be responsible) — **the dedicated authority per AEGIS taxonomy §4.1**, OJ-literal.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 9.3
  volere_section: 15
  volere_subtype: audit
  title: "Asset inventories are established through a documented entity-level asset register with identification + classification + documentation of ICT supported business functions + information assets + ICT assets + roles + dependencies"
  derives_from:
    hso_sub_so: SO-9.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-09_Governance-Documentation/9.3.md
    objective_ref_section: "### 9.3.0"
  description: |
    The product shall establish asset inventories through a documented entity-level asset register with identification + classification + documentation of ICT supported business functions + information assets + ICT assets + their roles and dependencies in relation to ICT risk, where ≥2 of the participating regulations (NIS 2, CRA, DORA) have applicability with overlapping asset-inventory architecture scope-determiners on the same party, with DORA Art. 7(1) as the dedicated authority for DORA financial entities and NIS 2 Art. 21(2)(i) + CRA Annex VII §1-§2 as partial-coverage inputs, with the per-reg asset-inventory artefact, governance body, anchor, content template, threshold, recipient, and evidence template preserved verbatim in the 3 sub-SOs.
  fit_criterion: |
    A documented entity-level asset-inventory architecture is established covering all 3 participating asset-inventory artefacts (or the subset applicable to the entity) at the asset-inventory-evidence layer: (1) NIS 2 entity-level asset-management sub-domain per Art. 21(2)(i) `human resources security, access control policies and asset management` (partial coverage via access-control coordination, with the management-body approve/oversee/liable architecture per Art. 20(1) as governance hook, calibrated by Recital 56 proportionality + state-of-the-art floor + cost factor) — **partial coverage only**; (2) CRA product-level architecture documentation per Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other), drawn up before placing on the market and updated during the support period per Art. 31(2), retained at MSA disposal for at least 10 years per Art. 13(13), with the manufacturer as governance body per Art. 13(8) — **partial coverage only**, documentation-centric, NOT a formal asset register in the DORA sense; (3) **DORA Art. 7(1) financial-entity dedicated asset inventory** `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` with the **3-way AND** chain of ICT supported business functions + information assets + ICT assets + roles + dependencies, under the three-lines-of-defence model per Art. 6(4) with management-body define/approve/oversee/be responsible per Art. 5(2), calibrated by Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities` — **the dedicated authority per AEGIS taxonomy §4.1 with explicit OJ-literal anchor** (distinct from D-07.2 where sole-authority is OJ-text-unsupported); the **NIS 2 ↔ CRA pair is substantively scope-disjoint per CRDA `N (typically)`** on a single event at a single party (per CRDA-deep §9.3 line 66) — different objects (entity asset register vs. product architecture documentation), different audit purposes (entity-level NCA review vs. product-level MSA review), CRDA `complementary` is a taxonomy artifact, the two regimes meet at the **supplier-customer interface** without OJ-level consolidation; the **NIS 2 ↔ DORA EQUAL pair** discharges NIS 2 Art. 21(2)(i) partial-coverage on the DORA-dominant stack for financial entities under DORA's direct scope (DORA Art. 7(1) is the dominant authority with explicit OJ-literal anchor); the **CRA ↔ DORA COMPLEMENTARY pair** engages with a **DORA-led stack** (DORA Art. 7(1) entity-level master record + CRA Annex VII §1-§2 architecture documentation as upstream product-level sub-register feeding the DORA master record, when the DORA entity procures CRA-conformant products).
  priority: MUST
  verification_method: TEST
  dependencies: [9.3.1, 9.3.2, 9.3.3]
  nist_csf: [ID.AM-01, ID.AM-02, ID.AM-05]
  applicable_if:
    regs: [NIS2, CRA, DORA]
    scope_overlap: Conditional   # HL engages when ≥2 applicable regs have ≥1 Y or Conditional-Y-scope-overlap pair on the same party; for 9.3 the 3×3 matrix shows 2 pairs with Y or Conditional-Y activation on the joint-condition operator (NIS2↔DORA = Y; CRA↔DORA = Conditional-Y when DORA entity procures CRA-conformant products). The NIS2↔CRA pair is **substantively scope-disjoint per CRDA `N (typically)`** — substantively scope-disjoint (different objects — entity asset register vs. product architecture documentation; different audit purposes; CRDA `complementary` is a taxonomy artifact); the HL does NOT engage on the NIS2↔CRA pair alone (no same-event overlap). The HL engages on the NIS2↔DORA EQUAL pair (DORA-dominant stack) and/or the CRA↔DORA COMPLEMENTARY pair (DORA-led stack with CRA as upstream product-level sub-register). For an NSIE that is not a DORA financial entity and that is not a manufacturer (no CRA Annex VII §1-§2 documentation duty), only the NIS 2 partial-coverage sub-SO activates and the HL does not engage (single-reg mode).
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The high-level SO surfaces the **common entity-level asset-inventory duty** (identification + classification + documentation of ICT supported business functions + information assets + ICT assets + roles + dependencies) with **DORA Art. 7(1) as the dedicated authority** for DORA financial entities (per AEGIS taxonomy §4.1, OJ-literal `3-way AND`) and NIS 2 Art. 21(2)(i) + CRA Annex VII §1-§2 as partial-coverage inputs. The 3 verified pairs are all SAME — 1 SAME — COMPLEMENTARY (NIS 2 ↔ CRA substantively scope-disjoint) + 1 SAME — EQUAL (NIS 2 ↔ DORA, DORA-dominant) + 1 SAME — COMPLEMENTARY (CRA ↔ DORA, DORA-led) — no CORRECTED, no CONTRADICTORY. **DORA sole-authority flag (per AEGIS taxonomy §4.1, OJ-literal)** distinguishes 9.3 from D-07.2 where the sole-authority assignment is OJ-text-unsupported; DORA Art. 7(1) explicit OJ-literal `identify, classify and adequately document` mandate on the `3-way AND` is the dominant anchor. The **NIS 2 ↔ CRA substantive scope-disjoint flag** is structurally significant — per CRDA-deep §9.3 line 66, the pair operates on different objects (entity asset register vs. product architecture documentation) serving different audit purposes (entity-level NCA review vs. product-level MSA review); CRDA `complementary` is a taxonomy artifact and the two regimes meet at the supplier-customer interface only (CRA-conformant product is an input to the NIS 2 entity's asset register). The **NIS 2 ↔ DORA EQUAL classification** discharges both obligations on the DORA-dominant stack for financial entities; the **CRA ↔ DORA COMPLEMENTARY** is DORA-led with CRA Annex VII §1-§2 as upstream product-level sub-register. The HL does NOT collapse the entity-level asset register with the product-level architecture documentation; the two artefacts stack on the supplier-customer interface. GDPR's DPA is **NOT** a recipient because GDPR is explicitly out-of-scope for 9.3 (RoPA is a related-but-distinct artefact at 9.4). The AI Act MSA + AI Office is **NOT** a recipient because the AI Act is explicitly out-of-scope for 9.3 (no asset-inventory mandate). **No OJ-level consolidation rule** at 9.3 (no OJ-permitted substitution exists across the 3 participating regs on the asset-inventory object — distinct from 9.2 which has the CRA Art. 13(4) sentence 2 consolidation rule on the assessment-object dimension). **Step Reference:** HL is decomposed into 3 per-reg sub-requirements below (one per participating regulation); each sub-requirement carries its own derivation, fit_criterion, and applicable_if. The 3 asset-inventory artefacts operate on distinct layers (entity-level asset register / product-level architecture documentation / entity-level master record with product sub-register) and serve distinct audit purposes; the per-reg artefact, anchor, governance body, content template, threshold, recipient, and evidence template are preserved verbatim in the 3 sub-SOs.
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-09.3
title: D-09.3 Asset Inventories — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.3 Asset Inventories
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-09_Governance-Documentation/D-09.3.md
status: DRAFT
---
> **Deep analysis:** [D-09.3 Asset Inventories](../../DeepAnalysis/D-09_Governance-Documentation/D-09.3.md)
#### D-09.3 Asset Inventories
<!-- participants: NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope as strict mandate) | RoPA focus on processing purposes, data categories, recipients, safeguards — not information assets. No standalone SO for D-09.3 from GDPR. | RoPA is a related-but-distinct artefact (see D-09.4). |
| NIS2 | SG-NIS2-003 + SG-NIS2-021 (partial) | Asset management as one of three coordinated sub-domains of access control (Art. 21(2)(i)) + management-body oversight. | Partial coverage via access-control coordination; no dedicated asset-inventory mandate. |
| CRA | SG-CRA-061 (partial) | Annex VII §1-§2 requires general description including SW versions + system-architecture description. | Documentation-centric, not a formal asset register. AEGIS taxonomy §4.1 marks DORA as sole authority for D-09.3. |
| DORA | SG-DORA-017 (sole authority) | Identify, classify, and adequately document ICT supported business functions, roles and responsibilities, information assets, ICT assets, and dependencies (Art. 7(1)). | Entity-level formal asset inventory; the dedicated authority per AEGIS taxonomy §4.1. |
| AI_Act | (out-of-scope) | AI Act does not impose asset-inventory mandate. | — |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3 regulations)
<!-- emergent: NIS2,CRA,DORA -->
- **DORA sole-authority taxonomy assignment is OJ-supported**: AEGIS taxonomy §4.1 marks DORA as sole authority for D-09.3. Unlike D-07.2 (where the sole-authority assignment is OJ-text-unsupported), D-09.3's sole-authority is OJ-literal (Art. 7(1) explicit `identify, classify, adequately document` mandate on the `3-way AND` of ICT supported business functions + information assets + ICT assets). NIS 2 and CRA provide partial coverage only.
- **CRA Annex VII §1-§2 is documentation-centric, not asset-register-centric**: The CRA general-description + architecture-description mandate is a technical-documentation artefact, not a formal asset register in the DORA sense. The two artefacts serve different audit purposes: CRA Annex VII is reviewed by market surveillance authorities; DORA asset register is reviewed by competent authorities and feeds the ICT risk register. No OJ-level cross-referencing.
<!-- /emergent -->
##### SR cross-validation
The 3 applicable regulations map D-09.3 to the NIST CSF 2.0 Subcategory **ID.AM-01** (Inventories of hardware managed within the system) and **ID.AM-02** (Inventories of software, services, and systems managed) as the convergent pair. DORA additionally maps **ID.AM-05** (Assets are prioritized based on classification, criticality, and business value) for the classify-and-document dimension; NIS 2 additionally maps **PR.PS-01** (Configuration management practices established) via the access-control coordination.
##### Downstream implication
Phase 1 entities must maintain a DORA-compliant asset register (Art. 7(1)) with NIS 2 partial-coverage access-control-asset linkages and CRA Annex VII §1-§2 product-architecture documentation as inputs. The DORA register is the entity-level master record.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-09.3
title: D-09.3 Asset Inventories — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-09 Governance & Documentation
sub_domain: D-09.3 Asset Inventories
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-09_Governance-Documentation/D-09.3.md
status: DRAFT
---
> **Domain analysis:** [D-09.3 Asset Inventories](../../DomainAnalysis/D-09_Governance-Documentation/D-09.3.md)
#### D-09.3 Asset Inventories
<!-- participants: NIS2, CRA, DORA -->
**Participants (from CRDA):** NIS2, CRA, DORA
**Sole-authority note (CRDA flag):** DORA Art. 7(1) is the dedicated authority — explicit `identify, classify, adequately document` mandate on the `3-way AND` of ICT supported business functions + information assets + ICT assets. NIS 2 and CRA provide partial coverage only.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

## Residual pair content (AI_Act, deep)

##### Pair: AI_Act ↔ [not in CRDA D-09.3 participants]
> **Note:** AI Act is out-of-scope for D-09.3 per CRDA (no asset-inventory mandate). No pair analysis included.
---

## Residual pair content (AI_Act, deep3)

##### Pair: AI_Act ↔ [not in CRDA D-09.3 participants]
> **Note:** AI Act is out-of-scope for D-09.3 per CRDA (no asset-inventory mandate). No pair analysis included.
---
---

## Residual pair content (GDPR, deep)

##### Pair: GDPR ↔ [not in CRDA D-09.3 participants]
> **Note:** GDPR is out-of-scope as strict mandate for D-09.3 per CRDA (RoPA focuses on processing purposes/data categories/recipients/safeguards — not information assets). GDPR ↔ CRA / GDPR ↔ DORA / GDPR ↔ NIS2 pairs not in CRDA matrix. No pair analysis included.
---

## Residual pair content (GDPR, deep3)

##### Pair: GDPR ↔ [not in CRDA D-09.3 participants]
> **Note:** GDPR is out-of-scope as strict mandate for D-09.3 per CRDA (RoPA focuses on processing purposes/data categories/recipients/safeguards — not information assets). GDPR ↔ CRA / GDPR ↔ DORA / GDPR ↔ NIS2 pairs not in CRDA matrix. No pair analysis included.
---
