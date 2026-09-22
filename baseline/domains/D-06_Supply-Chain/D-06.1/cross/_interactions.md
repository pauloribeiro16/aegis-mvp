# D-06.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-06.1 Vendor Risk Assessment](../../CrossRegulation/DomainAnalysis/D-06_Supply-Chain/D-06.1.md)
#### D-06.1 Vendor Risk Assessment
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.1 per AEGIS taxonomy §4.1 — AI Act value-chain obligations (Art. 25) are cross-relationship, not in the 29-clause cybersecurity set. DORA/NIS2 are sole authorities for entity-level third-party risk; CRA Art. 13(5) is sole authority for product-level supplier obligations.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-06.1 Vendor Risk Assessment
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md`](../../CrossRegulation/DeepAnalysis/D-06_Supply-Chain/D-06.1.md)
> (6 pairs verified against OJ text — **4 of 5 participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is out-of-scope per AEGIS
> taxonomy §4.1** as noted by `DomainAnalysis/D-06_Supply-Chain/D-06.1.md`
> line 36: "AI Act is out-of-scope for D-06.1 per AEGIS taxonomy §4.1 —
> AI Act value-chain obligations (Art. 25) are cross-relationship, not
> in the 29-clause cybersecurity set. DORA/NIS2 are sole authorities for
> entity-level third-party risk; CRA Art. 13(5) is sole authority for
> product-level supplier obligations").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-06.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-021 | Controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)) | Processor due diligence; controller-driven; qualitative `sufficient guarantees` + Art. 28(2) sub-processor authorisation + Art. 4(7)/(8) controller/processor definitions; GV.SC-02 + GV.SC-04 + ID.AM-04 |
| NIS2 | SO-NIS2-014 | Supply chain security is managed across direct supplier and service-provider relationships, including security-related aspects of those relationships (Art. 21(2)(d) + Art. 21(1) chapeau) | Entity supplier relationships; `direct` scope-limiter (Tier-1 + operationally-dependent sub-tier scope is calibrated by Member State transposition); continuous risk-management; GV.SC-02 + ID.AM-04 + GV.OC-03 |
| CRA | SO-CRA-037 | Manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) + Art. 13(6) + Art. 3(48) FOSS definition) | Product component integration; manufacturer-driven; `due diligence` procedural + substantive (VAG+POLY-S3, R3 reading); entities up to Art. 3(40) dealer / Art. 3(11) importer responsibilities; GV.SC-01 + GV.SC-02 + ID.RA-02 |
| DORA | SO-DORA-011 | ICT third-party risk is managed taking into account the nature, scale, complexity and importance of ICT-related dependencies and the risks arising from contractual arrangements on the use of ICT services (Art. 28(1) four-factor AND); contractual arrangements comply with appropriate information security standards; for critical or important functions (CIF), the most up-to-date and highest quality information security standards are used (Art. 28(5) escalator) | Financial entity ICT third-party; multi-factor proportionality; `critical or important functions` undefined distinction (POLY-S2 across 18 clauses); continuous risk-management; GV.SC-02 + ID.AM-04 |

## Validated relationships (from CRDA-deep §D-06.1)

#### Validated relationships (from CRDA-deep §D-06.1)
Of 6 pairs, **6 verified as SAME (all CRDA initial classifications held after OJ-text analysis): 2 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE + 1 EQUAL** — **no CORRECTED, no SCOPE-DISJOINT, no CONTRADICTORY** classifications on the vendor-risk-assessment duty itself. The four regulations look at supply chain from four distinct perspectives and are layered rather than contradictory:
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR processor due diligence is on the *processor as legal entity* (data-processing counterparty); NIS 2 supply chain security is on *direct suppliers and service providers* (broader scope, includes non-data-processing suppliers per Art. 21(2)(d)). When the supplier is both a processor and a service provider, both apply and the GDPR `sufficient guarantees` test is a **sharper threshold** on the same risk substrate that NIS 2's `appropriate and proportionate` Art. 21(1) chapeau operates on. The NIS 2 `direct` scope-limiter (POLY-S3 with three readings — R1 Tier-1 only, R2 Tier-1 + technically integrated, R3 Tier-1 + operationally dependent — per `SR-NIS2-020` `ambiguity_notes`) is the key operational handle on which parts of the supplier base are in NIS 2 scope. There is **no contradiction** between GDPR's per-processor due diligence and NIS 2's continuous supply-chain security — they are layered, with the GDPR leg providing the data-processing-counterparty dimension and the NIS 2 leg providing the broader entity-level supply-chain dimension.
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): GDPR processor due diligence is on the *processor as legal entity*; CRA third-party component due diligence is on *components as technical artefacts* (including non-commercial OSS, which GDPR does not separately contemplate per Art. 3(48) FOSS definition). When a CRA-compliant product is integrated into a GDPR controller's processing, the manufacturer has already done CRA-level component due diligence; the controller still owes GDPR-level processor due diligence on the **manufacturer** (the manufacturer is the processor when the controller deploys the product for processing). The two layers are different perspectives on the same supply chain — entity-level (GDPR) versus product-level (CRA). There is **no contradiction** because the two objects (processor as legal entity / component as technical artefact) and the two triggers (per-processor engagement / per-component integration) are distinct; the obligations stack vertically on the integrated manufacturer-controller-deployer stack.
- **GDPR ↔ DORA** — COMPLEMENTARY (SAME) (DORA exceeds GDPR): DORA's four-factor proportionality test (Art. 28(1) — nature, scale, complexity, importance) is a **sharper operationalisation** of the GDPR `sufficient guarantees` Art. 28(1) test. A financial entity already subject to DORA Art. 28 satisfies GDPR Art. 28(1) `sufficient guarantees` via the proportionality documentation, but **must explicitly document the GDPR-specific processor guarantees** that are not in the DORA Art. 30(2) closed list verbatim — instruction-bound processing per Art. 28(3)(a), audit rights per Art. 28(3)(h), sub-processor authorisation per Art. 28(2) — because DORA's ICT third-party risk regime is broader than GDPR's processor regime and does not separate the data-processing-counterparty dimension. The DORA four-factor test operationalises GDPR's qualitative `sufficient guarantees` threshold with sharper factors; there is **no contradiction** because the two thresholds are calibrated at different specificity — qualitative vs four-factor — and the DORA exceeds GDPR rather than contradicts it.
- **NIS2 ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME): NIS 2 supplier relationships are at the *entity* level (the deployer's supplier list under Art. 21(2)(d) + Art. 21(3) supplier assessment three-prong: vulnerabilities + quality + secure-development procedures); CRA third-party component due diligence is at the *product* level (the manufacturer's component list under Art. 13(5)). The two lists **overlap when the deployer is the entity and the manufacturer supplies a CRA-compliant product** — the deployer does NIS 2-level supplier due diligence on the manufacturer (entity-to-entity), while the manufacturer does CRA-level component due diligence on its third-party components (product-internal). The objects and triggers are different (entity-level supplier / product-level component), so the obligations **layer vertically** rather than contradict. The `due diligence` POLY-S3 ambiguity in CRA Art. 13(5) (R1 procedural-only / R2 substantive-only / R3 procedural+substantive) is resolved by `SR-CRA-050` to R3 (procedural + substantive), which aligns with the NIS 2 supplier-assessment three-prong.
- **NIS2 ↔ DORA** — EQUAL (SAME) (DORA exceeds NIS 2): DORA's Art. 28(1) four-factor proportionality test (nature, scale, complexity, importance) operationalises the NIS 2 Art. 21(1) `appropriate and proportionate` chapeau with **explicit factors** — same object (supplier risk), same addressee (entity), but DORA's sharper test exceeds NIS 2's general test. A financial entity implementing DORA **exceeds** NIS 2's supply-chain security requirement in the financial-services subset; NIS 2 remains the floor for the broader essential / important-entity population. The label is correct: same object, same addressee, DORA's sharper test exceeds NIS 2's general test. There is **no contradiction** — the two thresholds are calibrated at different specificity (qualitative chapeau with Member-State-transposition-supplied detail vs four-factor with explicit listed factors) and the DORA exceeds NIS 2 rather than contradicts it.
- **CRA ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME): CRA third-party component due diligence is **product-level** (the manufacturer's third-party components under Art. 13(5)); DORA ICT third-party risk is **entity-level** (the financial entity's ICT service providers under Art. 28(1)). The two are at different levels of the supply chain: **CRA = upstream** (manufacturer's inputs); **DORA = midstream** (deployer's ICT providers). The pair is typically **scope-disjoint because distinct actors handle distinct objects** — the CRA-bound manufacturer is upstream of the DORA-bound financial entity's ICT providers. When a financial entity deploys a CRA-compliant product, the manufacturer (CRA-bound) and the deployer (DORA-bound) are typically **different parties**. There is **no contradiction** because the two regimes target different supply-chain layers with different objects, different actors, and different triggers. The obligations compose into a 2-layer record when both apply, with the CRA covering the product side and the DORA covering the entity side of the same supply chain.
The vendor-risk-assessment architecture is **legitimately diverse** — each regulator targets a **distinct target object** (processor as legal entity / direct supplier as relationship / third-party component as technical artefact / ICT third-party service provider as financial-entity counterparty) at a **distinct trigger** (per-processor engagement / continuous supply-chain security / per-component integration / continuous ICT third-party risk management under proportionality) with a **distinct obligation anchor** (GDPR `sufficient guarantees` qualitative + Art. 28(3) DPA + Art. 28(2) sub-processor authorisation; NIS 2 `appropriate and proportionate` chapeau + Art. 21(2)(d) `direct` scope-limiter + Art. 21(3) supplier-assessment three-prong; CRA `due diligence` procedural + substantive + Art. 13(6) component vulnerability reporting + Art. 3(48) FOSS inclusion; DORA Art. 28(1) four-factor AND + Art. 28(5) CIF escalator + Art. 30(2) 9-element closed list). The high-level SO surfaces the **common vendor-risk-assessment duty** (vendor / supplier / component / ICT-provider due diligence with risk-anchored proportionality documentation + ongoing monitoring + recipient evidence); the per-regulation perspective is preserved verbatim in the four sub-SOs (target object, trigger, anchor, threshold, evidence template, recipient).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Y (controller = essential / important entity; the data-processing supplier is also a direct supplier under Art. 21(2)(d); both apply on the same supplier relationship with the GDPR `sufficient guarantees` test sharpening the NIS 2 `appropriate and proportionate` chapeau) | Y (integrated manufacturer-controller stack — manufacturer does CRA component due diligence; controller does GDPR processor due diligence on the manufacturer; the two layers stack vertically on the same supplier chain) | Y (financial entity = controller; the ICT third-party is also a processor; DORA four-factor test operationalises GDPR `sufficient guarantees`; GDPR-specific processor clauses are appended on the controller side) |
| **NIS2** | Y (same; reciprocal) | — | Conditional (Y when deployer is the essential / important entity and the manufacturer supplies a CRA-compliant product — entity-level supplier due diligence on the manufacturer stacks with product-level component due diligence; N when the manufacturer is in a non-EU jurisdiction with no supplier relationship to the NIS 2 entity) | Y (financial entity = essential / important entity; DORA satisfies NIS 2 in the financial-services subset via the Art. 28(1) four-factor proportionality test) |
| **CRA** | Y (same; reciprocal — manufacturer-controller deployer) | Conditional (same as NIS 2↔CRA) | — | N (typically) — CRA is upstream (manufacturer's inputs), DORA is midstream (deployer's ICT providers); the manufacturer and the financial entity are typically different parties; disjoint in baseline |
| **DORA** | Y (same; reciprocal — financial-entity-controller with CIF clauses documented on controller side) | Y (same; reciprocal — DORA four-factor test exceeds NIS 2 `appropriate and proportionate`) | N (typically) — distinct actors, distinct objects, distinct supply-chain levels | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **Conditional** = scope overlap only under specific circumstances (financial-entity-integrated-stack; vertically-integrated manufacturer-controller-deployer). **N** = scope-disjoint in baseline (manufacturer-side CRA component due diligence vs financial-entity-side DORA ICT third-party risk — distinct actors, distinct objects, distinct supply-chain levels). CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Y on the essential-entity-controller combined stack; GDPR↔CRA = Y on the integrated-stack manufacturer-controller; GDPR↔DORA = Y on the financial-entity-controller; NIS2↔CRA = Conditional Y when the deployer is the entity AND the manufacturer supplies a CRA-compliant product; NIS2↔DORA = Y on the financial-entity-essential-entity combined stack; CRA↔DORA = N in baseline — distinct actors, distinct supply-chain levels.

## Cross-recipient map

#### Cross-recipient map
D-06.1 generates partial recipient fragmentation at the **vendor-risk-assessment evidence layer** but does **not generate a notification cascade of D-06.1 itself** (the vendor-risk-assessment is the upstream gate before the contractual and operational obligations of D-06.3 / D-06.4 engage). The recipient set is at the **downstream compliance-evidence point**: **GDPR's supervisory authority (DPA)** on the Art. 5(2) accountability evidence (Art. 28(1) `sufficient guarantees` documentation + Art. 28(3) DPA clauses + Art. 30(2) RoPA record on the categories of processors + Art. 28(2) sub-processor authorisation chain); **NIS 2's CSIRT or competent authority** on the Art. 21(2)(d) supplier-risk register and the Art. 21(3) supplier-assessment three-prong evidence (vulnerabilities + quality + secure-development procedures); **CRA's market surveillance authority (MSA)** on the Annex VII §2 technical documentation record on integrated components (component inventory + due-diligence rationale) + the SBOM per Annex I Part II (1) (see `D-06.2` for the SBOM sub-domain); **DORA's competent authority (national financial supervisory authority)** on the four-factor proportionality assessment + Art. 30(2) 9-element contract + Art. 28(5) standards compliance for CIFs. These are distinct regulatory channels on the same vendor-risk-assessment evidence but they do not generate a notification cascade of D-06.1 itself — they are **compliance-evidence channels on the same vendor-risk-assessment architecture**. **D-06.3 (Contractual Security Obligations) is where the recipient asymmetry manifests operationally on the contractual architecture that the vendor-risk-assessment gates; D-06.4 (Third-Party Boundary Management) is where the recipient asymmetry manifests on the cross-border / representative / substantial-modification architecture; D-04.3 (Regulatory Notification) is where a vendor-side incident manifests as a downstream notification to MSAs and CSIRTs. D-06.1 is the upstream gate that decides which vendors enter the supply chain, with documented due diligence feeding the contractual layer in D-06.3 and the operational monitoring in D-10.**
---

## HSO considerations (from D-06.1.0 — High-level SecurityObjective)

**Considerations.**
- Four participating regulations (GDPR, NIS 2, CRA, DORA) each impose this duty on a distinct target object at a distinct trigger: GDPR `sufficient guarantees` qualitative test on the processor as legal entity (Art. 28(1)/(2) + Art. 4(7)/(8)); NIS 2 `appropriate and proportionate` chapeau on direct suppliers and service providers (Art. 21(1) + Art. 21(2)(d) + Art. 21(3) supplier-assessment three-prong: vulnerabilities + quality + secure-development procedures); CRA `due diligence` procedural + substantive on third-party components as technical artefacts including non-commercial OSS (Art. 13(5)/(6) + Art. 3(48) FOSS); DORA Art. 28(1) four-factor proportionality on ICT third-party service providers with Art. 28(5) CIF escalator.
- CRDA-deep verified relationships (6 pairs, all SAME — 2 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE + 1 EQUAL; no CORRECTED, no CONTRADICTORY): GDPR↔NIS2 = COMPLEMENTARY (GDPR `sufficient guarantees` is sharper than NIS 2 `appropriate and proportionate` on shared risk substrate); GDPR↔CRA = DIFFERENT-PERSPECTIVE (entity-level processor vs product-level component); GDPR↔DORA = COMPLEMENTARY (DORA exceeds GDPR — four-factor operationalises `sufficient guarantees` with sharper factors, GDPR-specific Art. 28(3) DPA clauses appended on controller side); NIS2↔CRA = DIFFERENT-PERSPECTIVE (entity-level supplier vs product-level component); NIS2↔DORA = EQUAL (DORA exceeds NIS 2 in financial-services subset — four-factor operationalises `appropriate and proportionate`); CRA↔DORA = DIFFERENT-PERSPECTIVE (upstream product-level vs midstream entity-level ICT provider; typically scope-disjoint in baseline).
- Implementation guidance: the four target objects are layered not collapsed — processor as legal entity (GDPR), direct supplier as relationship (NIS 2), third-party component as technical artefact (CRA), ICT third-party service provider as financial-entity counterparty (DORA). A unified vendor-risk-assessment platform may serve the technical substrate but policy and evidence layers must remain target-object-segregated.
- Scope caveats: entity-level vs product-level distinction (CRA is upstream — manufacturer's inputs; DORA is midstream — deployer's ICT providers; GDPR/NIS 2 are downstream — deployer's own supplier due diligence); DORA four-factor exceeds both GDPR `sufficient guarantees` and NIS 2 `appropriate and proportionate`; CRA Art. 3(48) FOSS inclusion is the CRA-specific operational handle that GDPR/NIS 2/DORA do not separately replicate; NIS 2 supplier-assessment three-prong is more granular than the GDPR `sufficient guarantees` test and the CRA `due diligence` test.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-06.1 over a distinct **target object** of the vendor-risk-assessment architecture; the target object, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the supply chain.
| Axis (reg) | Target object | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | processor as legal entity (data-processing counterparty) | per-processor engagement (Art. 28(1) prior-to-engagement gate + Art. 28(2) sub-processor authorisation chain) | `sufficient guarantees` (qualitative) + Art. 28(3) DPA clauses (closed list: instructions + purpose limitation + confidentiality + security + sub-processor authorisation + data-subject-rights assistance + Art. 33/34 assistance + return/deletion + audit/inspection) + EDPB Guidelines 07/2020 4-factor test (knowledge, reliability, resources, compliance-track-record) | supervisory authority (DPA) — Art. 5(2) accountability + Art. 30 RoPA on processors + Art. 28(3) DPA inspection | Art. 28(1) + Art. 28(2) + Art. 28(3)(a)–(h) + Art. 4(7)/(8) + Art. 30(2) + Art. 5(2) + Art. 24 controller accountability + Art. 25 by-design + Art. 32 security of processing |
| **NIS2** | direct supplier / service provider as relationship (entity-level supplier list) | continuous supply-chain security (Art. 21(2)(d)) + per-supplier assessment three-prong (Art. 21(3) sentence 1: vulnerabilities + quality + secure-development procedures) + EU-level coordinated risk propagation (Art. 21(3) sentence 2 → Art. 22) | `appropriate and proportionate` (Art. 21(1) chapeau) + `direct` scope-limiter (Art. 21(2)(d)) + state-of-the-art (Art. 21(1) sentence 2) | CSIRT or competent authority | Art. 21(1) chapeau + Art. 21(2)(d) + Art. 21(3) sentence 1 + Art. 22 + Art. 21(1) sentence 2 state-of-the-art |
| **CRA** | third-party component as technical artefact (manufacturer's component list, including non-commercial OSS per Art. 3(48)) | per-component integration (continuous during support period under Art. 13(8)) + on-becoming-aware of component vulnerability (Art. 13(6) sentence 1) + sharing with component supplier (Art. 13(6) sentence 2) | `due diligence` (VAG+POLY-S3, R3 procedural + substantive per `SR-CRA-050`) + Art. 13(2) risk-assessment propagation across 6 lifecycle phases + Art. 3(48) FOSS inclusion (non-commercial OSS not made available in commercial activity is in scope) + Annex I Part II (1) component identification (SBOM is D-06.2) | market surveillance authority (MSA) — Annex VII §2 technical documentation + Annex VII §3 risk-assessment record + Annex I Part II (1) component identification + Annex II information deliverable | Art. 13(5) + Art. 13(6) + Art. 3(48) FOSS definition + Art. 13(2) risk assessment + Art. 13(8) support-period handling + Annex VII §2 + Annex VII §3 |
| **DORA** | ICT third-party service provider as financial-entity counterparty (broader than GDPR's processor) | continuous ICT third-party risk management (Art. 28(1)) + contractual arrangement entry (Art. 28(5) standards compliance) + concentration-risk identification (Art. 28(4) on the critical-ICT third-party register under Art. 28(4) → Art. 29 designation) | Art. 28(1) four-factor proportionality — nature, scale, complexity, importance — explicit AND + service / process / function criticality + Art. 28(5) CIF escalator (`most up-to-date and highest quality information security standards`) + Art. 30(2) 9-element closed contract list (a)–(i) | competent authority (national financial supervisory authority) — Art. 28 proportionality record + Art. 30(2) contract + Art. 28(5) standards compliance for CIFs | Art. 28(1) + Art. 28(4) concentration + Art. 28(5) CIF + Art. 30(1) clearly-allocated obligations + Art. 30(2) closed list (a)–(i) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-06.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations target overlapping target objects on the same party** (e.g.
a financial entity that is also a NIS 2 essential entity AND
manufactures CRA-classified products AND processes personal data — a
vertically-integrated financial-manufacturer-controller with full
GDPR + NIS 2 + CRA + DORA applicability on the same supplier
relationship). For a financial entity deploying CRA-classified products
processing personal data, all four apply in sequence: **DORA gates the
selection** (Art. 28(1) four-factor proportionality); **NIS 2 specifies
the direct-supplier scope** (Art. 21(2)(d) `direct` scope-limiter + Art.
21(3) supplier-assessment three-prong on vulnerabilities + quality +
secure-development procedures); **CRA certifies the product** (the
manufacturer has already done component due diligence at Art. 13(5));
**GDPR requires processor-guarantees documentation** (Art. 28(1)
`sufficient guarantees` + EDPB Guidelines 07/2020 4-factor + Art. 28(3)
DPA clauses). For a 5-FTE SaaS startup with GDPR + CRA applicability
but no NIS 2 or DORA applicability, only the GDPR and CRA sub-SOs
activate; the high-level SO engages on the same party on the integrated
manufacturer-controller stack (CRA component due diligence + GDPR
processor due diligence stack vertically on the same supply chain).
For a NIS 2 essential entity that is not a financial entity and does not
manufacture CRA-classified products (NIS 2 + GDPR only or NIS 2 only
with non-CRA-classified products), only the applicable sub-SOs
activate and the high-level SO engages on the conditional Y pairs.
**The four target objects are layered, not collapsed**: processor as
legal entity (GDPR, controller-driven per-processor engagement);
direct supplier as relationship (NIS 2, entity-driven continuous
supply-chain security); third-party component as technical artefact
(CRA, manufacturer-driven per-component integration); ICT third-party
service provider as financial-entity counterparty (DORA, financial-
entity-driven continuous ICT third-party risk). The high-level SO
surfaces the common vendor-risk-assessment duty but does **NOT**
collapse the per-reg target object, trigger, anchor, threshold,
recipient, or evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA; **AI Act is
  out-of-scope** per AEGIS taxonomy §4.1 — AI Act value-chain
  obligations (Art. 25) are cross-relationship, not in the 29-clause
  cybersecurity set; DORA / NIS 2 are sole authorities for entity-level
  third-party risk; CRA Art. 13(5) is sole authority for
  product-level supplier obligations).
- 6 pairwise cells, verified by CRDA-deep as **6 SAME (no CORRECTED)**:
  GDPR↔NIS2 (SAME — COMPLEMENTARY, sharper-qualitative-on-shared-risk-
  substrate); GDPR↔CRA (SAME — DIFFERENT-PERSPECTIVE, entity-level
  processor vs product-level component); GDPR↔DORA (SAME —
  COMPLEMENTARY, **DORA exceeds GDPR**, four-factor operationalises
  `sufficient guarantees` with sharper factors); NIS2↔CRA (SAME —
  DIFFERENT-PERSPECTIVE, entity-level supplier vs product-level
  component); NIS2↔DORA (SAME — EQUAL, **DORA exceeds NIS 2**,
  four-factor operationalises `appropriate and proportionate` chapeau);
  CRA↔DORA (SAME — DIFFERENT-PERSPECTIVE, upstream product-level vs
  midstream entity-level).
- The four regulations impose **distinct vendor-risk-assessment duties**
  at **distinct target objects** with **distinct triggers**: GDPR
  processor due diligence (Art. 28(1) `sufficient guarantees`
  qualitative + Art. 28(3) DPA closed list + Art. 28(2) sub-processor
  authorisation); NIS 2 direct-supplier security (Art. 21(2)(d) `direct`
  scope-limiter + Art. 21(3) supplier-assessment three-prong + Art. 22
  EU-level risk propagation); CRA third-party component due diligence
  (Art. 13(5) `due diligence` procedural + substantive R3 reading +
  Art. 13(6) component vulnerability reporting + Art. 3(48) FOSS
  inclusion); DORA ICT third-party risk (Art. 28(1) four-factor
  proportionality + Art. 28(5) CIF escalator + Art. 30(2) 9-element
  contract list). The thresholds align qualitatively (GDPR
  `sufficient guarantees`; NIS 2 `appropriate and proportionate`;
  CRA `due diligence`; DORA four-factor) but the target objects,
  triggers, anchors, evidence templates, recipients diverge. DORA
  exceeds both NIS 2 (in the financial-services subset) and GDPR (via
  the four-factor operationalisation), so where DORA applies it
  discharges the GDPR `sufficient guarantees` and the NIS 2 `appropriate
  and proportionate` tests in the financial-entity subset, with the
  GDPR-specific Art. 28(3) DPA clauses appended on the controller side.
- The high-level SO describes the **COMMON OBJECTIVE** (vendor /
  supplier / component / ICT-provider due diligence with risk-anchored
  proportionality documentation + ongoing monitoring + recipient
  evidence; the 4-tier assessment chain articulated: DORA gates
  selection → NIS 2 specifies direct-supplier scope → CRA certifies
  product → GDPR requires processor-guarantees documentation); the
  **per-regulation perspective** (target object, trigger, anchor,
  threshold, recipient, evidence template) is preserved verbatim in
  the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the vendor-risk-assessment duty
  itself**, because no pair was verified as CONTRADICTORY or CORRECTED
  (all 6 pairs are SAME with different angles). Phase 1C Doc 07 does
  not need to resolve a vendor-risk-assessment contradiction because
  none exist by construction. The 4-tier assessment chain is itself
  the layered reconciliation that supersedes any single-regulator
  reading; the per-tier risk calibration (DORA four-factor at the
  ICT-provider tier; NIS 2 `direct` scope-limiter at the supplier-tier;
  CRA `due diligence` at the component-tier; GDPR `sufficient
  guarantees` at the processor-tier) preserves the per-reg
  proportionality discipline while enabling the integrated-stack
  assessment.
- **Scope caveat (CRITICAL — entity-level vs product-level
  distinction)** — derived from CRDA-deep verified classifications:
  the D-06.1 sub-domain distinguishes **entity-level vendor risk**
  (GDPR processor due diligence, NIS 2 direct-supplier security, DORA
  ICT third-party risk) from **product-level component due diligence**
  (CRA third-party components) — these are different **levels of the
  supply chain** in addition to being different **target objects**.
  CRA is **upstream** (the manufacturer's inputs); DORA is
  **midstream** (the deployer's ICT providers); GDPR / NIS 2 are
  **downstream** (the deployer's due diligence on its own suppliers).
  The three levels compose into a **3-tier supplier chain**: (1) CRA
  — manufacturer-side component due diligence on the manufacturer's
  third-party components; (2) DORA — financial-entity-side ICT
  third-party risk on the deployer's ICT providers (financial-entity
  subset); (3) GDPR + NIS 2 — deployer-side due diligence on the
  deployer's direct suppliers. For an integrated manufacturer that is
  also the deployer, the manufacturer's CRA-side component due
  diligence feeds the deployer's GDPR / NIS 2 / DORA-side due
  diligence — the upstream→downstream due-diligence propagation is
  the controlled hand-off, with explicit CRA-side disclosure to the
  downstream tier.
- **Scope caveat (CRITICAL — DORA four-factor exceeds GDPR
  `sufficient guarantees`)** — derived from CRDA-deep verified
  classifications: DORA's Art. 28(1) four-factor proportionality test
  (nature, scale, complexity, importance) **operationalises** the GDPR
  Art. 28(1) `sufficient guarantees` qualitative test with **sharper
  factors**. A financial entity subject to DORA Art. 28 satisfies GDPR
  Art. 28(1) via the proportionality documentation, but **must
  explicitly document the GDPR-specific processor guarantees** that
  are not in the DORA Art. 30(2) closed list verbatim — instruction-
  bound processing per Art. 28(3)(a), audit rights per Art. 28(3)(h),
  sub-processor authorisation per Art. 28(2), confidentiality per
  Art. 28(3)(b), data-subject-rights assistance per Art. 28(3)(e),
  Art. 33/34 incident-assistance per Art. 28(3)(f), and
  deletion-or-return per Art. 28(3)(g) (cross to D-05.3 sub-SO
  SR-GDPR-031). For an integrated financial-entity-controller, the
  DORA proportionality record discharges the GDPR `sufficient
  guarantees` test, with the GDPR-specific Art. 28(3) clauses
  appended on the controller side.
- **Scope caveat (CRITICAL — DORA four-factor exceeds NIS 2 `appropriate
  and proportionate`)** — derived from CRDA-deep verified
  classifications: DORA's Art. 28(1) four-factor proportionality test
  operationalises the NIS 2 Art. 21(1) `appropriate and proportionate`
  chapeau with **explicit factors** (nature, scale, complexity,
  importance), and a financial entity implementing DORA **exceeds**
  NIS 2's supply-chain security requirement in the financial-services
  subset. For a NIS 2 essential entity that is not a financial entity,
  the NIS 2 chapeau applies with the Member-State-transposition-
  supplied detail on the proportionality calibration; for a financial
  entity that is also a NIS 2 essential entity, the DORA four-factor
  test discharges the NIS 2 chapeau in the supply-chain-security
  dimension. The `direct` scope-limiter (POLY-S3 R1/R2/R3 per
  `SR-NIS2-020`) is the NIS 2-specific operational handle that DORA
  does not separately replicate (DORA Art. 28(1) `ICT-related
  dependencies` is broader than `direct suppliers` and reaches the
  full ICT service-provision graph in the financial-entity subset).
- **Scope caveat (CRITICAL — CRA `direct` third-party components
  include non-commercial OSS)** — derived from CRDA-deep verified
  classifications: CRA Art. 13(5) sentence 1 **explicitly includes**
  components of free and open-source software not made available on
  the market in the course of a commercial activity (per Art. 3(48)
  FOSS definition). This is the CRA-specific operational handle that
  GDPR / NIS 2 / DORA do not separately replicate. GDPR processor due
  diligence on a non-commercial OSS supplier is not directly
  applicable (the OSS developer is typically not a processor in the
  GDPR sense); NIS 2 supplier-security may apply if the OSS developer
  is a `direct supplier` under the Member-State-transposition
  `direct` reading; DORA ICT third-party risk may apply if the OSS
  supplier is an ICT third-party service provider. The CRA Art. 3(48)
  reach to non-commercial OSS is the **extension beyond the typical
  commercial supplier framework** that makes D-06.1 in the CRA
  perspective broader than the same sub-domain in the GDPR / NIS 2 /
  DORA perspectives. For a manufacturer integrating a non-commercial
  OSS component, the CRA Art. 13(5) due diligence applies with the
  OSS-specific calibration (e.g. stewardship assessment, CVD policy
  review, vulnerability disclosure channel, governance-
  transparency review — see `SR-CRA-050` `ambiguity_notes` on the
  `due diligence` POLY-S3 R3 reading for OSS-specific calibration).
- **Scope caveat (CRITICAL — NIS 2 supplier-assessment three-prong)** —
  derived from CRDA-deep verified classifications: NIS 2 Art. 21(3)
  sentence 1 imposes a **three-prong supplier assessment** —
  vulnerabilities specific to each direct supplier + overall quality
  of products and cybersecurity practices + supplier secure-
  development procedures — **all three required** (COORD-S2 across
  three AND-coordinated limbs per `SR-NIS2-023` and `SR-DORA-019`
  Propagated). The three-prong is more granular than the GDPR Art. 28(1)
  `sufficient guarantees` test (which is single qualitative + EDPB 4-
  factor) and the CRA Art. 13(5) `due diligence` test (which is
  procedural + substantive R3). For an essential entity across NIS 2 +
  GDPR + CRA, the three-prong discharges the
  vulnerabilities-secure-development-procedures dimensions of the
  supplier assessment, with the GDPR Art. 28(1) processor-guarantees
  layer appended on the controller side and the CRA Art. 13(5)
  due-diligence layer documented on the manufacturer side.
---

## Emergent tensions (from CRDA-deep §D-06.1)

#### Emergent tensions (from CRDA-deep §D-06.1)
**0 conditional emergent tensions** on the vendor-risk-assessment
duty itself — no pair was verified as CONTRADICTORY or CORRECTED.
The 6 pairs are all SAME with different angles (2 COMPLEMENTARY + 3
DIFFERENT-PERSPECTIVE + 1 EQUAL), and the four regulators look at
the supply chain from four distinct perspectives that are **layered
rather than contradictory**. **No SCOPE-DISJOINT baseline pairs** —
the 4×4 matrix shows **Y or Conditional Y** scope overlap in baseline
across all 6 pairs (the CRA↔DORA pair is N-in-baseline because
distinct actors handle distinct supply-chain levels, but the pair is
also DIFFERENT-PERSPECTIVE — the same conceptual framing as the
other 5 pairs). **No CONTRADICTORY pairs** on the vendor-risk-
assessment duty itself. The **target-object divergence** (processor
as legal entity / supplier as relationship / component as technical
artefact / ICT third-party as financial-entity counterparty) is the
**legitimately diverse dimension**: each regulator targets a distinct
target object at a distinct trigger (per-processor engagement /
continuous supply-chain security / per-component integration /
continuous ICT third-party risk), and the operational convergence is
on a **4-tier vendor-risk-assessment architecture** with explicit
layered hand-offs.
The **verbatim-linguistic match between GDPR and DORA** (both
anchor on a `sufficient guarantees` / `four-factor` operationalisation
of risk-anchored proportionality, with DORA sharper than GDPR)
discharges the GDPR `sufficient guarantees` test in the financial-
services subset via the DORA proportionality documentation, with the
GDPR-specific Art. 28(3) DPA clauses appended on the controller side
— the layer-by-layer mapping is documented in the 4-tier assessment
chain.
The **DORA-exceeds-NIS 2 calibration** (DORA's Art. 28(1) four-
factor exceeds NIS 2's Art. 21(1) `appropriate and proportionate`
chapeau) means that a financial entity implementing DORA discharges
NIS 2's supply-chain-security requirement in the financial-services
subset via the DORA proportionality documentation; NIS 2 remains the
floor for the broader essential / important-entity population. The
`direct` scope-limiter (POLY-S3 R1/R2/R3) is the NIS 2-specific
operational handle that DORA does not replicate (DORA Art. 28(1)
`ICT-related dependencies` is broader than `direct suppliers`).
The **CRA `direct` third-party components including non-commercial
OSS** (Art. 3(48) FOSS definition) is the CRA-specific operational
extension beyond the typical commercial-supplier framework — the
manufacturer-side Art. 13(5) due diligence applies to non-commercial
OSS components that become part of the product with digital elements
placed on the Union market. The OSS-specific due-diligence
calibration (stewardship assessment, CVD policy review, vulnerability
disclosure channel, governance-transparency review) is the operational
substrate that distinguishes the CRA side from the GDPR / NIS 2 /
DORA sides on the OSS-inclusion dimension.
The high-level SO surfaces the common vendor-risk-assessment duty;
the per-reg target object, trigger, anchor, threshold, recipient,
and evidence template are documented separately in the four sub-SOs
and the per-recipient evidence packs. **0 conditional emergent
tensions** because no pair was verified as CONTRADICTORY or
CORRECTED — the 4-tier assessment chain is itself the layered
reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-06.1 — with
overlapping target-object scope-determiners on the same party —
operates a **4-tier supplier / vendor risk assessment chain** with
explicit layered hand-offs. The high-level SO (`SO-D-06.1.HL`)
describes the common vendor-risk-assessment duty (risk-anchored due
diligence with proportionality documentation + ongoing monitoring +
recipient evidence); the per-reg perspective is preserved in the four
sub-SOs (target object, trigger, anchor, threshold, recipient,
evidence template). **The 0 conditional emergent tensions are
documented as a layered reconciliation**, with the 4-tier
assessment chain (DORA gates selection → NIS 2 specifies direct-
supplier scope → CRA certifies product → GDPR requires processor-
guarantees documentation) operationalising the inter-reg
hand-offs. The high-level SO does NOT collapse the four target
objects into a single risk-assessment architecture; the per-reg
perspective on target object, trigger, anchor, threshold, recipient,
and evidence template is preserved verbatim. Phase 1C Doc 07
documents the **vendor-risk-assessment strategy**: (1) a 4-tier
supplier / vendor risk assessment chain with explicit target-
object hand-offs (DORA four-factor → NIS 2 `direct` scope-limiter
R2 reading → CRA `due diligence` R3 reading → GDPR EDPB
Guidelines 07/2020 4-factor); (2) the DORA-exceeds-NIS 2
operationalisation where DORA applies, with NIS 2 supplied-by-
reference for the supplier-security layer in the financial-
services subset; (3) the DORA-exceeds-GDPR `sufficient guarantees`
operationalisation, with the GDPR-specific Art. 28(3) DPA clauses
appended on the controller side; (4) the CRA `direct` third-party
components including non-commercial OSS (Art. 3(48) FOSS), with
the OSS-specific due-diligence calibration (stewardship + CVD
policy + disclosure channel + governance transparency); (5) the NIS
2 Art. 21(3) three-prong supplier assessment (vulnerabilities +
quality + secure-development procedures), with all three required
(COORD-S2 across AND-coordinated limbs); (6) the CRA Art. 13(6)
component vulnerability handling (address + remediate + share
upstream) as the upstream→downstream supply-chain vulnerability-
hand-off; (7) the GDPR Art. 28(2) sub-processor authorisation
chain, with the same sufficient-guarantees threshold at each tier;
(8) the DORA Art. 28(4) critical-ICT third-party register as the
financial-entity-specific governance substrate for CIF-classified ICT
providers; (9) the Annex VII §2 + §3 CRA-side technical documentation
as the evidence pack for the manufacturer-side component due-
diligence architecture; (10) the Annex I Part II (1) SBOM (cross to
D-06.2 — SO-CRA-038 + SR-CRA-008 / SR-CRA-052 / SR-CRA-053) as the
upstream component-identification artefact that the CRA Art. 13(5)
due diligence consumes. For proportionality (P2), a 5-FTE SaaS
startup with GDPR + CRA applicability may default to the GDPR Art.
28(1) `sufficient guarantees` documentation plus the CRA Art. 13(5)
component due-diligence documentation (NIS 2 and DORA are out of
scope unless the SaaS operates in a NIS 2-essential sector or is a
financial entity); a NIS 2 essential entity in a non-financial
sector must additionally document the Art. 21(2)(d) `direct`-
supplier security under the Member-State-transposition `direct`
reading (R1 / R2 / R3 calibration per `SR-NIS2-020`) and the Art.
21(3) three-prong supplier assessment on vulnerabilities + quality
+ secure-development procedures; a financial entity in scope of
all four regulations must additionally document the Art. 28(1)
four-factor proportionality assessment + Art. 28(4) critical-ICT
third-party register + Art. 28(5) CIF escalator on `most up-to-date
and highest quality` standards compliance, with the GDPR Art. 28(3)
clauses appended on the controller side and the NIS 2 `appropriate
and proportionate` chapeau supplied by reference via the DORA
proportionality documentation.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## 6.1 Vendor Risk Assessment — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md`. See that file for cross-reg verified relationships (6 pairs verified as **6 SAME — no CORRECTED, no CONTRADICTORY, no SCOPE-DISJOINT**: 2 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE + 1 EQUAL — the four regulators target **distinct target objects** at **distinct triggers** with **distinct obligation anchors**: processor as legal entity / direct supplier as relationship / third-party component as technical artefact / ICT third-party service provider as financial-entity counterparty), scope overlap matrix, Objective/Considerations content, the 4-tier assessment-chain reconciliation (DORA gates selection → NIS 2 specifies direct-supplier scope → CRA certifies product → GDPR requires processor-guarantees documentation), the DORA four-factor exceeds GDPR `sufficient guarantees` + NIS 2 `appropriate and proportionate` scope caveats, the CRA Art. 3(48) FOSS inclusion scope caveat, and the NIS 2 Art. 21(3) three-prong supplier assessment scope caveat. **Scope-title note (P0):** the index.md `Supplier Security` label is reconciled with the CRDA-deep `Vendor Risk Assessment` source-of-truth title — this file uses the CRDA-deep title per Batch 11 critical-rule #6 + #8 (the Batch 11 HSO file already documented the divergence). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; AI Act value-chain obligations Art. 25 are cross-relationship, not in the 29-clause cybersecurity set; DORA / NIS 2 are sole authorities for entity-level third-party risk; CRA Art. 13(5) is sole authority for product-level supplier obligations). CRDA-deep verified 6 pairs as **6 SAME** (2 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE + 1 EQUAL — none required CRDA correction). The four regulators target **distinct target objects** at **distinct triggers** (processor-as-legal-entity / direct-supplier-as-relationship / third-party-component-as-technical-artefact / ICT-third-party-as-financial-entity-provider) and the high-level SO surfaces the **common vendor-risk-assessment duty** (vendor / supplier / component / ICT-provider due diligence with risk-anchored proportionality documentation + ongoing monitoring + recipient evidence) while preserving the **per-reg target object, trigger, anchor, threshold, evidence template, recipient** — the four target objects are layered, not collapsed. The 4-tier assessment chain (DORA gates selection → NIS 2 specifies direct-supplier scope → CRA certifies product → GDPR requires processor-guarantees documentation) is itself the layered reconciliation that supersedes any single-regulator reading.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 6.1
  volere_section: 15
  volere_subtype: immunity
  title: "Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence with proportionality documentation and ongoing monitoring before entry to the supply chain (4-tier assessment chain across the 4 distinct target objects)"
  derives_from:
    hso_sub_so: SO-6.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md
    objective_ref_section: "### 6.1.0"
  description: |
    The product shall operate vendor / supplier / component / ICT third-party service-provider due diligence with risk-anchored proportionality documentation and ongoing monitoring before entry to the supply chain — across the 4-tier assessment chain targeting the four distinct target objects (processor as legal entity, direct supplier as relationship, third-party component as technical artefact, ICT third-party service provider as financial-entity counterparty) — as the common vendor-risk-assessment duty converging across GDPR Art. 28(1) `sufficient guarantees` qualitative + Art. 28(2) sub-processor authorisation, NIS 2 Art. 21(2)(d) `direct` scope-limiter + Art. 21(1) `appropriate and proportionate` chapeau + Art. 21(3) three-prong supplier assessment (vulnerabilities + quality + secure-development procedures), CRA Art. 13(5) `due diligence` procedural + substantive on third-party components including non-commercial OSS per Art. 3(48), and DORA Art. 28(1) four-factor proportionality (nature, scale, complexity, importance) with Art. 28(5) `most up-to-date and highest quality` escalator for critical or important functions, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A 4-tier vendor-risk-assessment architecture is operated with explicit tier separation (processor-tier GDPR / supplier-tier NIS 2 / component-tier CRA / ICT-provider-tier DORA) and documented tier hand-offs at the assessment-type surfaces; each tier records assessment object (processor-as-legal-entity / supplier-as-relationship / component-as-technical-artefact / ICT-provider-as-counterparty), proportionality anchor (qualitative `sufficient guarantees` / `appropriate and proportionate` chapeau / `due diligence` procedural+substantive R3 / four-factor AND), trigger gate (per-processor engagement / continuous supply-chain security / per-component integration / continuous ICT third-party risk management), evidence template (EDPB Guidelines 07/2020 4-factor + Art. 28(3) DPA / Art. 21(3) three-prong / Annex VII §2 + Art. 13(2) risk assessment / Art. 28(1) four-factor + Art. 30(2) contract), and recipient (DPA / CSIRT-or-competent-authority / MSA / national-financial-supervisory-authority) per asset; the 4-tier assessment chain operates as DORA gates selection → NIS 2 specifies direct-supplier scope → CRA certifies product → GDPR requires processor-guarantees documentation, with DORA Art. 28(1) four-factor operationalising both GDPR Art. 28(1) `sufficient guarantees` and NIS 2 Art. 21(1) chapeau in the financial-services subset; CRA Art. 3(48) FOSS-included third-party component due diligence applies with non-commercial OSS calibration (stewardship assessment, CVD policy review, governance-transparency review); the NIS 2 Art. 21(3) three-prong supplier assessment discharges the vulnerabilities-secure-development-procedures dimensions with the GDPR processor-guarantees layer appended on the controller side; verified by 4-tier assessment-architecture documentation review + per-tier risk-anchored proportionality records inspection + EDPB 07/2020 4-factor processor-guarantees evidence review (when GDPR in scope) + Art. 21(3) three-prong supplier-assessment records inspection (when NIS 2 in scope) + Annex VII §2 component-due-diligence rationale review (when CRA in scope) + Art. 28(1) four-factor proportionality record + Art. 28(5) CIF-standards compliance evidence review (when DORA in scope) + DPA / CSIRT-or-CA / MSA / national-FE-CA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-02]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping target objects on the same party (see HSO scope-overlap principle); AI Act out-of-scope
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    Four participating regulations (GDPR, NIS 2, CRA, DORA) each impose this duty on a distinct target object at a distinct trigger with a distinct obligation anchor: GDPR `sufficient guarantees` qualitative test on the processor as legal entity (Art. 28(1)/(2) + Art. 4(7)/(8)); NIS 2 `appropriate and proportionate` chapeau on direct suppliers and service providers (Art. 21(1) + Art. 21(2)(d) `direct` scope-limiter + Art. 21(3) supplier-assessment three-prong); CRA `due diligence` procedural + substantive on third-party components as technical artefacts including non-commercial OSS (Art. 13(5)/(6) + Art. 3(48) FOSS); DORA Art. 28(1) four-factor proportionality on ICT third-party service providers with Art. 28(5) CIF escalator. CRDA-deep verified relationships (6 pairs, all SAME — 2 COMPLEMENTARY + 3 DIFFERENT-PERSPECTIVE + 1 EQUAL; no CORRECTED, no CONTRADICTORY): GDPR↔NIS2 = COMPLEMENTARY (GDPR `sufficient guarantees` is sharper than NIS 2 `appropriate and proportionate` on shared risk substrate); GDPR↔CRA = DIFFERENT-PERSPECTIVE (entity-level processor vs product-level component); GDPR↔DORA = COMPLEMENTARY (DORA exceeds GDPR — four-factor operationalises `sufficient guarantees` with sharper factors, GDPR-specific Art. 28(3) DPA clauses appended on controller side); NIS2↔CRA = DIFFERENT-PERSPECTIVE (entity-level supplier vs product-level component); NIS2↔DORA = EQUAL (DORA exceeds NIS 2 in financial-services subset — four-factor operationalises `appropriate and proportionate` chapeau with sharper factors); CRA↔DORA = DIFFERENT-PERSPECTIVE (upstream product-level vs midstream entity-level ICT provider; typically scope-disjoint in baseline because distinct actors handle distinct objects). The 4-tier assessment chain (DORA gates selection → NIS 2 specifies direct-supplier scope → CRA certifies product → GDPR requires processor-guarantees documentation) is itself the layered reconciliation that supersedes any single-regulator reading. A unified vendor-risk-assessment platform may serve the technical substrate, but policy and evidence layers must remain target-object-segregated. CRDA-deep verified 0 conditional emergent tensions in this sub-domain; the task is to stack the documentation so that the 4-tier vendor-risk-assessment architecture (with per-tier target object, proportionality anchor, trigger gate, evidence template, and recipient documented separately) discharges all four obligations on the same party, with explicit tier hand-offs at the assessment-type surfaces. (Copied from the HSO Considerations block of `### 6.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-06.1
title: D-06.1 Vendor Risk Assessment — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.1 Vendor Risk Assessment
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-06_Supply-Chain/D-06.1.md
status: DRAFT
---
> **Deep analysis:** [D-06.1 Vendor Risk Assessment](../../DeepAnalysis/D-06_Supply-Chain/D-06.1.md)
#### D-06.1 Vendor Risk Assessment
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-021 | Controller engages only processors providing sufficient guarantees to implement TOMs (Art. 28(1)/(2)) | Processor due diligence; controller-driven |
| NIS2 | SO-NIS2-014 | Supply chain security managed across direct supplier/service-provider relationships (Art. 21(2)(d)) | Entity supplier relationships; `direct` scope-limiter |
| CRA | SO-CRA-037 | Manufacturer due diligence on third-party components including non-commercial OSS (Art. 13(5)) | Product component integration; manufacturer-driven |
| DORA | SO-DORA-011 | ICT third-party risk managed under four-factor proportionality (nature, scale, complexity, importance) (Art. 28(1)) | Financial entity ICT third-party; multi-factor proportionality |
| AI_Act | — | Out-of-scope (sole authorities: DORA/NIS2 + CRA Art. 13–14) | n/a |
**Sole-authority note:** AI Act is out-of-scope for D-06.1 per AEGIS taxonomy §4.1 — AI Act value-chain obligations (Art. 25) are cross-relationship, not in the 29-clause cybersecurity set. DORA/NIS2 are sole authorities for entity-level third-party risk; CRA Art. 13(5) is sole authority for product-level supplier obligations.
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
None. The four regulations look at supply chain from four distinct perspectives (processor / supplier / component / ICT third-party) and are layered, not contradictory.
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **GV.SC-02** (Suppliers prioritised by criticality) and **ID.AM-04** (Resources prioritised based on classification). GDPR maps both via SR-GDPR-033 (processor selection). NIS2 maps ID.AM-04 + ID.RA-01 + ID.RA-02 via SR-NIS2-022 (per-supplier vulnerability intelligence). CRA maps GV.SC-01 + GV.SC-02 + ID.RA-02 via SR-CRA-050. DORA maps GV.SC-02 + ID.AM-04 via SR-DORA-019. The CSF 2.0 surface is consistent — GV.SC and ID.AM/ID.RA are the shared categories. The proportional scoping (NIS2 `direct`, DORA `four-factor`) is a regulatory-specific construct that does not appear in CSF 2.0.
##### Downstream implication
Phase 2 obligation derivation must produce a 4-tier supplier/vendor risk assessment: (1) GDPR processor due diligence, (2) NIS2 direct supplier security, (3) CRA third-party component due diligence, (4) DORA ICT third-party risk under proportionality. For a financial entity deploying CRA-compliant products processing personal data, all four apply in sequence: DORA gates the selection (four-factor proportionality), NIS2 specifies the direct-supplier scope, CRA certifies the product (manufacturer already did component due diligence), GDPR requires processor-guarantees documentation. Phase 3 case generation must validate the 4-tier assessment chain.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-06.1
title: D-06.1 Vendor Risk Assessment — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-06 Supply Chain
sub_domain: D-06.1 Vendor Risk Assessment
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-06_Supply-Chain/D-06.1.md
status: DRAFT
---
> **Domain analysis:** [D-06.1 Vendor Risk Assessment](../../DomainAnalysis/D-06_Supply-Chain/D-06.1.md)
#### D-06.1 Vendor Risk Assessment
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority note:** AI Act is out-of-scope for D-06.1 per AEGIS taxonomy §4.1 — AI Act value-chain obligations (Art. 25) are cross-relationship, not in the 29-clause cybersecurity set. DORA/NIS2 are sole authorities for entity-level third-party risk; CRA Art. 13(5) is sole authority for product-level supplier obligations.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)