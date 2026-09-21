# D-05.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis [VERBATIM]
> **Domain analysis:** [D-05.1 Data Minimisation](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md)
#### D-05.1 Data Minimisation
<!-- participants: GDPR, CRA, AI_Act -->
**Participants (from CRDA):** GDPR, CRA, AI_Act
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.1 per AEGIS taxonomy §4.1 — both are operational-resilience / incident-reporting focused, not data-lifecycle. GDPR is the dedicated authority; CRA addresses product-level (which can include non-personal data); AI Act addresses training-data-quality specifically.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective [VERBATIM]
## D-05.1 Data Minimisation
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md`](../../CrossRegulation/DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md)
> (3 pairs verified against OJ text — **3 of 5 participating regulations
> are GDPR, CRA, AI_Act; NIS 2 and DORA are out-of-scope per AEGIS
> taxonomy §4.1** as noted by `DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md`
> line 36: "NIS2 and DORA are out-of-scope for D-05.1 per AEGIS taxonomy
> §4.1 — both are operational-resilience / incident-reporting focused,
> not data-lifecycle. GDPR is the dedicated authority; CRA addresses
> product-level (which can include non-personal data); AI Act addresses
> training-data-quality specifically").

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-05.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-015 + SO-GDPR-016 (cross-ref) | Personal data limited to adequate/relevant/necessary + Art. 6(4) compatibility test + Art. 6(1)(a)–(f) lawfulness bases + Art. 9(1) prohibition with Art. 9(2) exceptions | Personal data; controller-driven; Art. 5(1)(c) + Art. 6(4) + Art. 5(1)(a)/(b) + Art. 6(1) + Art. 9(1) prohibition; PR.DS-12 + ID.AM-03 |
| CRA | SO-CRA-034 | Product data (personal or other) limited to adequate/relevant/necessary for intended purpose | Product data; manufacturer design; Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) `intended purpose`; PR.DS-12 + ID.AM-03 |
| AI_Act | SO-AIACT-003 + SO-AIACT-004 | High-risk AI training/validation/testing datasets meet quality criteria (relevant/representative/free of errors/complete) + bias-detection data governance (8-element list) + exceptional special-category processing for bias correction (6 cumulative conditions (a)–(f)) | Training data; provider-driven; Art. 10(1)/(2)/(3)/(5); ID.AM-03 + PR.DS-12 + PR.PS-06 + PR.DS-01 + GV.OC-03 |

## Validated relationships (from CRDA-deep §D-05.1)

#### Validated relationships (from CRDA-deep §D-05.1)
Of 3 pairs, **2 verified as SAME (1 COMPLEMENTARY + 1 COMPLEMENTARY; CRDA initial classifications held after OJ-text analysis) and 1 CORRECTED** (GDPR ↔ AI_Act: CRDA `CONTRADICTORY` → verified `SCOPE-DISJOINT` with explicit AI Act Art. 10(5) carve-out — the AI Act creates a *permission* that GDPR does not provide, conditioned on 6 cumulative safeguards, and the CRDA reasoning itself acknowledges "this is a regulatory carve-out *into* the data minimisation architecture, not a contradiction of minimisation as a principle, but it expands the set of permissible processing"; that admission is dispositive because the exception-permission pattern is not the prohibition-vs-prohibition pattern that `CONTRADICTORY` connotes). **No SCOPE-DISJOINT pairs on the baseline; no CONTRADICTORY pairs on the data-minimisation duty itself** — the AI Act carve-out is the single overlap point on the special-category-data window.
- **GDPR ↔ CRA** — COMPLEMENTARY (SAME): GDPR Art. 5(1)(c) and CRA Annex I Part I (2)(g) use the **verbatim operative language** "adequate, relevant and limited to what is necessary" — the wording overlap is literal and unambiguous. GDPR minimisation is purpose-driven (controller defines purpose, then minimises data); CRA minimisation is intended-purpose-driven (manufacturer defines product purpose per Art. 3(23), then minimises data processed). When the same data is processed by a CRA-compliant product deployed by a GDPR controller, both minimisations apply and the stricter operational interpretation binds. CRA does NOT require the Art. 6(4) compatibility test; the residual GDPR-only requirement is the change-of-purpose compatibility assessment.
- **GDPR ↔ AI_Act** — **CORRECTED: CRDA `CONTRADICTORY` → verified `SCOPE-DISJOINT (with explicit Art. 10(5) carve-out)`**: GDPR Art. 9(1) prohibits special-category personal data processing absent one of Art. 9(2) bases; AI Act Art. 10(5) creates an *exception* to GDPR Art. 9(1) — providers of high-risk AI may exceptionally process special-category data for bias detection/correction, subject to **6 cumulative conditions (a)–(f) all required**: (a) the bias detection and correction cannot be effectively achieved by processing other data; (b) the special categories of personal data are processed strictly necessary and limited to the bias detection and correction; (c) the providers have put in place effective technical and organisational safeguards to protect the data; (d) the datasets used for bias detection and correction are subject to enhanced data governance; (e) the safeguards are documented; (f) the special-category data are deleted after the bias detection and correction. The CRDA reasoning itself states this is a "regulatory carve-out *into* the data minimisation architecture, not a contradiction of minimisation as a principle" — that admission is dispositive. The Art. 10(5) provision is a **permission** that GDPR does not provide, conditioned on 6 safeguards; it is NOT a contradiction of GDPR Art. 5(1)(c) — it is an exception that allows *one specific additional purpose* (bias correction) for *one specific data class* (high-risk AI training data) when *one specific technical condition* (no alternative data) is met. Two regulators cannot impose mutually exclusive obligations on the same event when one creates a conditional exception to the other — that is the textbook exception-permission pattern, not the prohibition-vs-prohibition pattern. **Outside the narrow Art. 10(5) window** (i.e. for non-special-category data, or for non-bias-correction purposes, or when alternative non-special-category data IS available), the AI Act does not trigger special-category p... (line truncated to 2000 chars)
- **CRA ↔ AI_Act** — COMPLEMENTARY (SAME): CRA minimisation operates at **runtime on data the product processes when in use** (Annex I Part I (2)(g)); AI Act Art. 10 quality criteria operate **upstream on the training pipeline** (Art. 10(1)/(2)/(3)). They address different data sets at different lifecycle stages. When the same dataset flows through both (training data for a CRA-classified high-risk AI product), the AI Act quality criteria (relevant, representative, free of errors, complete) sharpen the CRA runtime minimisation principle. No contradiction; full coverage requires both. The pair is typically N on scope (different lifecycle stages; the only overlap is at the data-flow boundary where training data flows into runtime data, which is sequential not concurrent).
The data-minimisation architecture is **legitimately diverse** — each regulator targets a distinct data class (personal data vs product data vs training data) at a distinct trigger (controller-driven vs manufacturer-design vs provider-driven) with a distinct obligation anchor (GDPR Art. 5(1)(c) "adequate, relevant, necessary" + Art. 6(4) compatibility; CRA Annex I Part I (2)(g) "adequate, relevant, necessary" tied to Art. 3(23) intended purpose; AI Act Art. 10(1)/(2) dataset quality criteria + Art. 10(5) special-category 6-condition gateway). The high-level SO surfaces the **common substantive data-minimisation duty**; the per-regulation perspective is preserved verbatim in the three sub-SOs (data class, trigger, anchor, threshold, evidence template).
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | CRA | AI_Act |
|---|---|---|---|
| **GDPR** | — | Conditional (Y when the same data stream flows through a CRA-classified product at runtime, and the data is personal data; both minimisations apply and the stricter binds; GDPR retains the Art. 6(4) compatibility-test residual) | Conditional (Y in the narrow Art. 10(5) window: high-risk AI provider training a system with bias-detection needs that cannot be met by non-special-category data, all 6 conditions (a)–(f) satisfied; outside that window, the pair does not overlap and the AI Act does not trigger special-category processing) |
| **CRA** | Conditional (Y integrated-stack manufacturer-controller; the runtime product minimisation applies to the personal-data subset flowing through the product at runtime) | — | Conditional (Y when training data for a CRA-classified high-risk AI product is the same dataset; the AI Act training-stage quality criteria sharpen the CRA runtime minimisation; disjoint in baseline — different lifecycle stages, sequential not concurrent) |
| **AI_Act** | Conditional (Y in the Art. 10(5) window only; the AI Act provider is also a controller when the training data is personal; outside the Art. 10(5) window, the pair is scope-disjoint in baseline) | Conditional (Y sequential — training data → runtime product; disjoint in baseline) | — |
Legend: **Conditional** = scope overlap only under specific circumstances (personal data flowing through a CRA-classified product at runtime; high-risk AI provider in the narrow Art. 10(5) special-category window; integrated-stack manufacturer-controller-deployer). **N** = scope-disjoint in baseline (e.g. AI Act training-data quality vs CRA runtime product data are at different lifecycle stages; the overlap is sequential not concurrent). CRDA-deep scope-disjoint tests: GDPR↔CRA = Conditional (Y integrated-stack; N pure-CRA-only product with no personal-data subset); GDPR↔AI_Act = Conditional (Y Art. 10(5) only; N outside the window); CRA↔AI_Act = Conditional (Y sequential lifecycle data flow; N baseline different lifecycle stages).

## Cross-recipient map

#### Cross-recipient map
D-05.1 itself does **not** generate recipient asymmetry — the data-minimisation process is **inward-looking** (the controller / manufacturer / provider designs the data-collection surface to the purpose, then documents the necessity assessment, then propagates the necessity test to the data-inventory record). The recipient fragmentation across the three regulators is at the **downstream compliance-demonstration point**: GDPR's supervisory authority (DPA) on the Art. 5(2) accountability evidence (necessity assessment + Art. 6(4) compatibility for any change of purpose; DPIA under Art. 35 for high-risk processing); CRA's market surveillance authority (MSA) on the Annex VII §2 technical documentation (data-class inventory + minimisation rationale per intended purpose under Art. 3(23) + risk-assessment record under Annex VII §3); and AI Act's national competent authority + market surveillance authority (MSA) on the Annex IV technical documentation (dataset quality records + Art. 10(2) 8-element data governance practice records + Art. 10(5) 6-condition safeguard records for the special-category exception). These are distinct regulatory channels but they do not generate a notification cascade of D-05.1 itself — they are compliance-evidence channels on the same data-minimisation architecture. **D-05.3 (Right to Erasure) and D-09.4 (Records of Processing) are where the recipient asymmetry manifests operationally; D-05.1 is the upstream minimisation architecture that constrains the data-collection surface and produces the necessity-assessment evidence base.**
---

## HSO considerations (from D-05.1.0 — High-level SecurityObjective)

**Considerations.**
- Three participating regulations (GDPR, CRA, AI Act) each impose this duty on a distinct data class at a distinct trigger: GDPR Art. 5(1)(c) "adequate, relevant and limited to what is necessary" on personal data (controller-driven) plus the Art. 6(4) change-of-purpose compatibility test and Art. 9(1) special-category prohibition; CRA Annex I Part I (2)(g) verbatim "adequate, relevant and limited to what is necessary" on product data (manufacturer-design, tied to Art. 3(23) intended purpose); AI Act Art. 10(1)/(2) 8-element data-governance practice + Art. 10(3) 4-criterion dataset quality on training data (provider-driven).
- CRDA-deep verified relationships: GDPR↔CRA = SAME (verbatim operative-language match, controller-driven purpose vs manufacturer-design intended purpose); CRA↔AI_Act = SAME (runtime product data vs training pipeline data, different lifecycle stages); GDPR↔AI_Act = CORRECTED from CONTRADICTORY to SCOPE-DISJOINT with explicit AI Act Art. 10(5) carve-out into GDPR Art. 9(1) (the exception-permission pattern, not prohibition-vs-prohibition).
- The 1 conditional emergent tension (Art. 10(5) special-category gateway) is regulated by the 6-cumulative-condition matrix (a)–(f): bias detection cannot be achieved by other data + strict necessity + safeguards + enhanced governance + documentation + post-bias deletion. Outside that narrow window, GDPR Art. 9(1) prohibition binds and AI Act Art. 10(5) does not extend.
- Implementation guidance: the three data classes are layered not collapsed — personal data is collected from data subjects (GDPR), product data is collected at runtime by the product (CRA), training data is collected upstream for the training pipeline (AI Act). A unified data-management platform may serve the technical substrate, but policy and evidence layers must remain class-segregated.
- Scope caveats: GDPR-CRA verbatim language overlap is literal and the stricter operational interpretation binds on the shared risk substrate; CRA-AI_Act operates at sequential lifecycle stages (runtime vs training pipeline, disjoint in baseline); AI Act Art. 10(5) gateway does NOT extend to other special-category processing beyond the bias-correction window; the high-level SO does NOT relax GDPR Art. 9(1) prohibition beyond what Art. 10(5) explicitly permits.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 3 participating regulations each define D-05.1 over a distinct **data class**; the trigger, the threshold anchor, the lifecycle stage, the recipient, and the legal anchor all depend on which data class the minimisation duty applies to.
| Axis (reg) | Data class | Trigger | Threshold anchor | Lifecycle stage | Recipient | Legal anchor |
|---|---|---|---|---|---|---|
| **GDPR** | personal data (data-subject-identifiable) | collection or further processing of personal data (Art. 5(1)(c)); any change of purpose triggers Art. 6(4) compatibility | `adequate, relevant and limited to what is necessary` (Art. 5(1)(c)) + Art. 6(4) compatibility test (5 factors (a)–(e)) + Art. 5(1)(c) minimisation register | collection + further processing + change of purpose | supervisory authority (DPA) — Art. 5(2) accountability + Art. 35 DPIA + Art. 30 RoPA | Art. 5(1)(c) + Art. 6(4) + Art. 5(1)(a)/(b) + Art. 6(1) + Art. 9(1) prohibition + Art. 9(2) exceptions + Art. 25(1)/(2) by-design/by-default + Art. 35(7) DPIA content |
| **CRA** | product data (personal or other) | design / development of a product with digital elements with attack-surface implications | `adequate, relevant and limited to what is necessary in relation to the intended purpose of the product` (Annex I Part I (2)(g) verbatim); the `intended purpose` per Art. 3(23) | design-time + runtime (per Annex I risk assessment under Art. 13(2)) | market surveillance authority (MSA) — Annex VII §2 technical documentation + Annex VII §3 risk-assessment record | Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) intended purpose + Art. 13(2) risk assessment |
| **AI_Act** | training data (high-risk AI training/validation/testing datasets) | training of high-risk AI systems with data; bias detection and correction in those datasets | dataset quality criteria `relevant, sufficiently representative, and to the best extent possible, free of errors and complete` (Art. 10(3)) + 8-element data-governance practice (Art. 10(2) (a)–(h)) + special-category 6-cumulative-condition gateway (Art. 10(5) (a)–(f)) | training pipeline (upstream of runtime) | national competent authority + MSA — Annex IV technical documentation + Art. 10(2) data-governance records + Art. 10(5) safeguard records | Art. 10(1) + Art. 10(2) 8-element list (a)–(h) + Art. 10(3) 4-criterion quality + Art. 10(5) 6-cumulative-condition gateway |

## Scope-overlap matrix (3×3)

#### Scope-overlap matrix (3×3)
(See the validated-relationships table above for the 3×3 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-05.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations' data-class scope-determiners overlap on the same party**
(e.g. a GDPR controller that also manufactures CRA-regulated products
that process personal data and operates a high-risk AI system trained
on special-category data for bias correction — a vertically-integrated
manufacturer-controller-provider on a multi-class data minimisation
architecture). Pure co-applicability of disjoint-data-class regulations
on different data objects does **not** trigger cross-regulation
aggregation — see the Activation logic in the file header. For a 5-FTE
SaaS startup with GDPR + CRA applicability but no AI Act applicability,
only the GDPR and CRA sub-SOs activate; the high-level SO engages on the
same party if both apply, with the boundary between CRA
product-data minimisation and GDPR personal-data minimisation
documented as the controlled hand-off (CRA-product minimisation
reduces the personal-data footprint at runtime; controller still owns
the upstream personal-data collection decision). **The three data
classes are layered, not collapsed**: personal data is collected from
data subjects (GDPR); product data is collected by the product at
runtime (CRA); training data is collected upstream for the training
pipeline (AI Act). The high-level SO surfaces the common
data-minimisation duty but does **NOT** aggregate the per-reg data
class, trigger, threshold anchor, lifecycle stage, recipient, or
evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 3 of 5 regulations participate (GDPR, CRA, AI_Act; NIS 2 and DORA
  are out-of-scope per AEGIS taxonomy §4.1 — both are operational-
  resilience/incident-reporting focused, not data-lifecycle; GDPR is
  the dedicated authority for personal-data minimisation; CRA
  addresses product-level data; AI Act addresses training-data quality
  and the special-category bias-correction exception).
- 3 pairwise cells, verified by CRDA-deep as **2 SAME + 1 CORRECTED**:
  GDPR↔CRA (SAME — COMPLEMENTARY, CRDA initial classification held);
  CRA↔AI_Act (SAME — COMPLEMENTARY, CRDA initial classification held);
  GDPR↔AI_Act (**CORRECTED** from CONTRADICTORY to SCOPE-DISJOINT
  with explicit Art. 10(5) carve-out — the AI Act creates a
  conditional exception to GDPR Art. 9(1) conditioned on 6 cumulative
  safeguards (a)–(f), which is the exception-permission pattern not
  the prohibition-vs-prohibition pattern; the CRDA reasoning itself
  concedes the carve-out framing, making the `CONTRADICTORY` label
  scope-incorrect).
- The three regulations impose the **same substantive data-minimisation
  duty** but each operates on a **distinct data class** at a **distinct
  trigger**: personal data (GDPR, controller-driven collection and
  further processing); product data (CRA, manufacturer-design at
  design-time and runtime); training data (AI Act, provider-driven
  training pipeline upstream of runtime). The threshold anchors align
  qualitatively (GDPR `adequate, relevant, necessary`; CRA `adequate,
  relevant, necessary in relation to intended purpose`; AI Act
  `relevant, sufficiently representative, free of errors, complete`)
  but the data classes, the triggers, and the evidence templates
  diverge. The verbatim "adequate, relevant, necessary" wording of
  GDPR and CRA makes those two a literal-linguistic match (R1 in the
  ambiguity treatment); AI Act uses a parallel-but-distinct 4-criterion
  quality formulation.
- The high-level SO describes the **COMMON OBJECTIVE** (limit data to
  what is adequate/relevant/necessary for the declared purpose;
  document the necessity assessment; apply the Art. 6(4) compatibility
  test on any change of purpose; honour the Art. 9(1) special-category
  prohibition absent an Art. 9(2) basis or the Art. 10(5) AI-Act
  gateway; deliver the evidence base); the **per-regulation
  perspective** (data class, trigger, anchor, lifecycle stage,
  evidence template) is preserved verbatim in the three sub-SOs.
- The high-level SO does **NOT** resolve the 1 conditional emergent
  tension — the **3-way interaction on special-category data** (GDPR
  Art. 9(1) prohibition; AI Act Art. 10(5) gateway; CRA Annex I
  Part I (2)(g) silent on special-category — only adequacy/relevance/
  necessity). The pairwise readings (GDPR↔CRA, GDPR↔AI_Act,
  CRA↔AI_Act) each capture part of the interaction, but the
  *non-pairwise observation* is that AI Act's Art. 10(5) exception
  *enables* a processing class (special-category data for bias
  correction) that neither GDPR nor CRA explicitly contemplates. The
  high-level SO codifies the AI Act Art. 10(5) exception as a
  **gateway clause**: it is *permitted* by AI Act, *limited* by GDPR
  Art. 9(2) residual constraints (where applicable — the Art. 10(5)
  conditions are the operative safeguard; the GDPR Art. 9(2) bases
  continue to apply in parallel per the Art. 10(5) `subject to
  appropriate safeguards` anchor), and *unspecified* by CRA (CRA
  defers to whichever regulation governs the personal-data status of
  the data). The tension is **conditional** (it engages only in the
  narrow Art. 10(5) window — high-risk AI provider training a system
  with bias-detection needs that cannot be met by non-special-category
  data, all 6 conditions (a)–(f) satisfied) and is **regulated** by
  the Art. 10(5) 6-condition matrix. Phase 1C Doc 07 documents the
  gateway-clause architecture; Phase 3 case generation must surface
  the 6-condition matrix explicitly when the case company is a
  high-risk AI provider processing special-category data for bias
  correction.
- **Scope caveat (CRITICAL — data-class divergence)** — derived
  from CRDA-deep verified classifications: the high-level SO does NOT
  collapse the three data classes into a single data-collection
  architecture. Personal data, product data, and training data are
  **distinct data objects** at **distinct layers** (collection from
  data subjects vs runtime product capture vs upstream training
  pipeline), with distinct triggers, distinct threshold anchors, and
  distinct evidence templates (Art. 5(2) accountability + Art. 35
  DPIA + Art. 30 RoPA vs Annex VII §2 technical documentation +
  Annex VII §3 risk assessment vs Annex IV technical documentation +
  Art. 10(2) data-governance practice records + Art. 10(5) safeguard
  records). A unified data-management platform may serve the technical
  substrate (e.g. a unified data catalog with multiple data-class
  views), but the policy and evidence layers must remain
  **class-segregated** for compliance demonstration. Phase 1A must
  therefore emit **three checks before applying the high-level SO**
  (one per participating regulation) to confirm that the per-reg
  data class, trigger, threshold anchor, lifecycle stage, recipient,
  and evidence template are documented separately; the high-level SO
  surfaces the common data-minimisation duty but does NOT aggregate
  the per-reg data classes.
- **Scope caveat (CRITICAL — GDPR-CRA verbatim language overlap is
  literal)** — derived from CRDA-deep verified classifications: GDPR
  Art. 5(1)(c) and CRA Annex I Part I (2)(g) use the **verbatim
  operative language** "adequate, relevant and limited to what is
  necessary". The wording overlap is literal and unambiguous. For
  a party in both GDPR and CRA scope, the same data stream flowing
  through a CRA-classified product at runtime satisfies both
  minimisation tests on the same operative phrase. CRA does NOT
  require the Art. 6(4) compatibility test; the **residual
  GDPR-only requirement** is the change-of-purpose compatibility
  assessment. The controller-side responsibility for the Art. 6(4)
  compatibility test is not absorbed by the CRA-side design-time
  minimisation. For an integrated-stack manufacturer-controller (the
  same party is both manufacturer of the CRA product and controller
  of the personal data processing), the manufacturer-controller must
  document the Art. 6(4) compatibility assessment separately from
  the CRA-side Annex I Part I (2)(g) design-time minimisation.
- **Scope caveat (CRITICAL — CRA-AI_Act lifecycle-stage
  divergence)** — derived from CRDA-deep verified classifications:
  CRA Annex I Part I (2)(g) operates on data the product processes
  **at runtime**; AI Act Art. 10 operates on data the **training
  pipeline** uses upstream. They address different data sets at
  different lifecycle stages. When the same dataset flows through
  both (training data for a CRA-classified high-risk AI product),
  the AI Act training-stage quality criteria (relevant, representative,
  free of errors, complete) sharpen the CRA runtime minimisation
  principle (adequate, relevant, necessary for intended purpose).
  For an AI-enabled CRA product, the data-minimisation architecture
  must be a **3-track matrix** (CRA runtime product data minimisation
  + GDPR personal-data minimisation for the personal-data subset +
  AI Act training-data quality for the upstream training pipeline).
  Phase 3 case generation must validate that the runtime product does
  not retain more data than the training-data quality permits to flow
  into it (the upstream→downstream minimisation hand-off).
- **Scope caveat (CRITICAL — AI_Act Art. 10(5) gateway)** — derived
  from CRDA-deep verified classifications: the AI Act Art. 10(5)
  special-category exception is the **only point where data
  minimisation is *relaxed*** by one of the three regulations. The
  relaxation is **conditional** on 6 cumulative conditions (a)–(f)
  all required: (a) the bias detection and correction cannot be
  effectively achieved by processing other data; (b) the special
  categories of personal data are processed strictly necessary and
  limited to the bias detection and correction; (c) the providers
  have put in place effective technical and organisational safeguards
  to protect the data; (d) the datasets used for bias detection and
  correction are subject to enhanced data governance; (e) the
  safeguards are documented; (f) the special-category data are
  deleted after the bias detection and correction. Outside this
  narrow window, the GDPR Art. 9(1) prohibition binds; the
  exception-permission pattern does not extend to other
  special-category processing. The high-level SO does NOT relax the
  GDPR Art. 9(1) prohibition beyond what Art. 10(5) explicitly
  permits; the residual GDPR Art. 9(2) bases continue to apply in
  parallel.
---

## Emergent tensions (from CRDA-deep §D-05.1)

#### Emergent tensions (from CRDA-deep §D-05.1)
**1 conditional emergent tension** — the **3-way interaction on
special-category data** (GDPR Art. 9(1) prohibition + Art. 9(2)
exception bases; AI Act Art. 10(5) 6-cumulative-condition gateway;
CRA Annex I Part I (2)(g) silent on special-category — addresses
only adequacy/relevance/necessity for the intended purpose). The
pairwise readings (GDPR↔CRA, GDPR↔AI_Act, CRA↔AI_Act) each capture
part of the interaction, but the *non-pairwise observation* is that
AI Act's Art. 10(5) gateway *enables* a processing class (special-
category data for bias correction in high-risk AI systems) that
neither GDPR nor CRA explicitly contemplates: GDPR prohibits it
absent an Art. 9(2) basis (the Art. 9(2)(g) `substantial public
interest` basis is the most likely applicable basis, but the
processor must demonstrate the basis independently); CRA is silent
on special-category (the (2)(g) minimisation addresses the data
class abstractly, not the personal-data subset's special-category
status); AI Act Art. 10(5) creates a 6-cumulative-condition gateway
that operates as a permission. The high-level SO codifies the AI
Act Art. 10(5) exception as a **gateway clause**: it is *permitted*
by AI Act, *limited* by GDPR Art. 9(2) residual constraints (the
Art. 10(5) `subject to appropriate safeguards` anchor and the
parallel GDPR Art. 9(2) bases), and *unspecified* by CRA (CRA defers
to whichever regulation governs the personal-data status of the
data). The tension is **conditional** (it engages only in the narrow
Art. 10(5) window — high-risk AI provider training a system
with bias-detection needs that cannot be met by non-special-category
data, all 6 conditions (a)–(f) satisfied) and is **regulated** by
the Art. 10(5) 6-condition matrix. Phase 1C Doc 07 documents the
gateway-clause architecture; Phase 3 case generation must surface
the 6-condition matrix explicitly when the case company is a
high-risk AI provider processing special-category data for bias
correction.
**No SCOPE-DISJOINT baseline pairs** — the 3×3 matrix shows
**Conditional** scope overlap in baseline (N or Y depending on
vertical-integration / special-category window / sequential lifecycle
data flow); the baseline is not scope-disjoint across all three
pairs. **No CONTRADICTORY pairs on the data-minimisation duty
itself** — the 1 CORRECTED pair (GDPR ↔ AI_Act) was relabelled
from CONTRADICTORY to SCOPE-DISJOINT with explicit Art. 10(5)
carve-out, and the relabelling is preserved verbatim. The
**data-class divergence** (personal data / product data / training
data) is the **legitimately diverse dimension**: each regulator
targets a distinct data class at a distinct trigger (controller-
driven / manufacturer-design / provider-driven), and the operational
convergence is on a **multi-class data-minimisation architecture**
with explicit class-segregated hand-offs. The **verbatim-linguistic
match between GDPR and CRA** (`adequate, relevant and limited to
what is necessary` in both Art. 5(1)(c) and Annex I Part I (2)(g))
is the **rare-but-honest convergence on the same operative phrase**;
CRA does NOT require the Art. 6(4) compatibility test, so the
residual GDPR-only requirement is the change-of-purpose compatibility
assessment. The **lifecycle-stage divergence between CRA and AI_Act**
(runtime product data vs training pipeline data) is handled by the
3-track matrix (CRA runtime + GDPR personal-data subset + AI Act
training-stage); the upstream→downstream minimisation hand-off is
the controlled interface. The high-level SO surfaces the common
data-minimisation duty; the per-reg data class, trigger, anchor,
lifecycle stage, recipient, and evidence template are documented
separately in the three sub-SOs and the per-recipient evidence packs.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-05.1 — with
overlapping data-class scope-determiners on the same party — operates
a **multi-class data-minimisation architecture** with explicit
class-segregated hand-offs. The high-level SO (`SO-D-05.1.HL`)
describes the common data-minimisation duty (limit data to what is
adequate/relevant/necessary for the declared purpose; document the
necessity assessment; apply the Art. 6(4) compatibility test on any
change of purpose; honour the Art. 9(1) special-category prohibition
absent an Art. 9(2) basis or the Art. 10(5) AI-Act gateway; deliver
the evidence base); the per-reg perspective is preserved in the three
sub-SOs (data class, trigger, anchor, lifecycle stage, recipient,
evidence template). **The 1 conditional emergent tension on the
special-category data exception is documented as a gateway-clause
architecture**, not a contradiction. The high-level SO does NOT
collapse the three data classes into a single data-collection
architecture; the per-reg perspective on data class, trigger, anchor,
lifecycle stage, recipient, and evidence template is preserved
verbatim. Phase 1C Doc 07 documents the **multi-class data-
minimisation strategy**: (1) a multi-class data-minimisation
architecture with explicit data-class hand-offs at the
collection/runtime/training-pipeline surfaces (personal data vs
product data vs training data); (2) the GDPR Art. 5(1)(c) verbatim
language as the operative test for the GDPR ↔ CRA intersection on
the same data stream (CRA-product runtime minimisation satisfies
the GDPR-side test on the same data, with the Art. 6(4) compatibility
test as the residual GDPR-only requirement); (3) the AI Act Art. 10(5)
6-cumulative-condition special-category gateway as the **single
narrow permission** that expands the set of permissible processing
beyond what GDPR Art. 9(1) ordinarily permits (all 6 conditions
(a)–(f) required, with documented safeguards, enhanced data
governance, and post-correction deletion); (4) the CRA ↔ AI Act
sequential lifecycle data flow (training pipeline → runtime product)
as the controlled hand-off with explicit upstream-to-downstream
minimisation propagation; (5) the GDPR Art. 6(4) compatibility test
as the residual obligation on any change of purpose (not absorbed by
the CRA-side design-time minimisation); (6) the Art. 25(1)/(2)
by-design and by-default as the upstream policy loop on the GDPR
side; (7) the Art. 35(7) DPIA as the downstream risk-assessment loop
on the GDPR side for high-risk processing; (8) the Art. 10(2)
8-element data-governance practice as the upstream data-quality loop
on the AI Act side; (9) the Art. 10(3) 4-criterion dataset quality
benchmark (relevant, sufficiently representative, free of errors,
complete) as the substantive quality floor on the AI Act side; (10)
the Annex VII §2 + §3 CRA-side technical documentation as the
evidence pack for the product-internal data-minimisation architecture.
For proportionality (P2), a 5-FTE SaaS with GDPR + CRA applicability
may default to the CRA Annex I Part I (2)(g) design-time
minimisation plus the GDPR Art. 5(1)(c) controller-side necessity
assessment (AI Act training-data quality is out of scope unless the
SaaS trains a high-risk AI system with special-category data); a
mid-size AI-enabled product company in scope of all three regulations
must additionally document the AI Act Art. 10(2) 8-element
data-governance practice and the Art. 10(3) 4-criterion dataset
quality, with the Art. 10(5) 6-condition matrix surfaced explicitly
where special-category data is processed for bias correction.
---

## Part 1 §3 — context

### 3. Security Requirements [VERBATIM]
## D-05.1 Data Minimisation — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.1.md`. See that file for cross-reg verified relationships (3 pairs verified: 2 SAME — GDPR↔CRA = COMPLEMENTARY on verbatim "adequate, relevant and limited to what is necessary" language; CRA↔AI_Act = COMPLEMENTARY on runtime vs training lifecycle stages; 1 CORRECTED — GDPR↔AI_Act, was CONTRADICTORY → SCOPE-DISJOINT with explicit AI Act Art. 10(5) carve-out conditioned on 6 cumulative safeguards (a)–(f)), scope overlap matrix, Objective/Considerations content, data-class divergence (personal data / product data / training data), trigger divergence (controller-driven / manufacturer-design / provider-driven), GDPR↔CRA verbatim-linguistic match, CRA↔AI_Act lifecycle-stage divergence, AI Act Art. 10(5) 6-condition gateway architecture, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA, AI Act (3 of 5 regs — NIS 2 and DORA are out-of-scope per AEGIS taxonomy §4.1 — both are operational-resilience / incident-reporting focused, not data-lifecycle). CRDA-deep verified 3 pairs as 2 SAME (1 COMPLEMENTARY + 1 COMPLEMENTARY) + 1 CORRECTED (none required CRDA correction in the actionable sense — the corrected pair is a relabelling, not a new conflict). The three regulators target **distinct data classes** at **distinct triggers** (personal data / controller-driven; product data / manufacturer-design; training data / provider-driven), and the high-level SO surfaces the common data-minimisation duty while preserving the per-reg data class, trigger, threshold anchor, lifecycle stage, recipient, and evidence template — the three data classes are layered, not collapsed.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 5.1
  volere_section: 15
  volere_subtype: privacy
  title: "Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary for the declared purpose — multi-class data-minimisation architecture with class-segregated hand-offs"
  derives_from:
    hso_sub_so: SO-D-05.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.1.md
    objective_ref_section: "### D-05.1.0"
  description: |
    The product shall limit data — across the three in-scope data classes (personal data, product data, training data) — to what is adequate, relevant, and necessary in relation to the declared purpose, with a documented necessity assessment per data class, a documented Art. 6(4) compatibility assessment on any change of purpose (GDPR residual), and explicit class-segregated hand-offs between the controller-driven personal-data layer, the manufacturer-design product-data layer, and the provider-driven training-data layer, as the common data-minimisation duty converging across GDPR Art. 5(1)(c) + Art. 6(4) + Art. 9(1) prohibition, CRA Annex I Part I (2)(g) + Art. 3(23) intended purpose, and AI Act Art. 10(1)/(2)/(3) + Art. 10(5) 6-cumulative-condition special-category gateway, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A multi-class data-minimisation architecture is operated with explicit class-segregated hand-offs at the personal-data / product-data / training-data surfaces; each data class has a documented necessity assessment (purpose + lawful basis + data-class scope + necessity test + retention time-limit + safeguard posture) per ID.AM-03 data-inventory substrate + PR.DS-12 risk-strategy-bound retention; the GDPR Art. 6(4) 5-factor compatibility assessment is performed on any change of purpose and documented separately from the CRA-side Annex I Part I (2)(g) design-time minimisation; the AI Act Art. 10(2) 8-element data-governance practice is documented for training data with the Art. 10(3) 4-criterion dataset quality benchmark (relevant, sufficiently representative, free of errors, complete) verified per dataset; the AI Act Art. 10(5) 6-cumulative-condition special-category gateway (a)–(f) is surfaced explicitly when special-category data is processed for bias correction in high-risk AI systems, with documented safeguards (pseudonymisation, differential privacy, federated learning — PR.DS-01 state-of-the-art privacy-preserving measures) and post-correction deletion; the verbatim "adequate, relevant and limited to what is necessary" operative language binds both GDPR and CRA on the same data stream when a CRA-classified product processes personal data at runtime, with the stricter operational interpretation binding; verified by multi-class data-inventory audit + per-class necessity-assessment review + Art. 6(4) compatibility-assessment records inspection + CRA Annex I Part I (2)(g) design-time minimisation documentation review + Art. 10(2) 8-element governance-practice inspection + Art. 10(3) 4-criterion dataset-quality benchmark verification + Art. 10(5) 6-condition safeguard records review (when in scope) + class-segregated hand-off documentation review + DPA / MSA / national competent authority inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-12, ID.AM-03, GV.OC-03, GV.PO-01, PR.PS-06, PR.DS-01]
  applicable_if:
    regs: [GDPR, CRA, AI_ACT]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping data classes on the same party AND the Art. 10(5) carve-out does not dissolve the engagement; see HSO scope-overlap principle
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The three participating regulations impose the same substantive data-minimisation duty but each targets a distinct data class at a distinct trigger: GDPR Art. 5(1)(c) "adequate, relevant and limited to what is necessary" on personal data (controller-driven) plus the Art. 6(4) change-of-purpose compatibility test and Art. 9(1) special-category prohibition; CRA Annex I Part I (2)(g) verbatim "adequate, relevant and limited to what is necessary" on product data (manufacturer-design, tied to Art. 3(23) intended purpose); AI Act Art. 10(1)/(2) 8-element data-governance practice + Art. 10(3) 4-criterion dataset quality on training data (provider-driven). The 1 conditional emergent tension (Art. 10(5) special-category gateway) is regulated by the 6-cumulative-condition matrix (a)–(f): bias detection cannot be achieved by other data + strict necessity + safeguards + enhanced governance + documentation + post-bias deletion. The high-level SO surfaces the common data-minimisation duty (limit data to what is adequate/relevant/necessary for the declared purpose; document the necessity assessment; apply the Art. 6(4) compatibility test on any change of purpose; honour the Art. 9(1) special-category prohibition absent an Art. 9(2) basis or the Art. 10(5) AI-Act gateway; deliver the evidence base); the per-regulation perspective (data class, trigger, anchor, lifecycle stage, evidence template) is preserved verbatim in the three sub-SOs. (Copied from the HSO Considerations block of `### D-05.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-05.1
title: D-05.1 Data Minimisation — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.1 Data Minimisation
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md
status: DRAFT
---
> **Deep analysis:** [D-05.1 Data Minimisation](../../DeepAnalysis/D-05_Data-Lifecycle/D-05.1.md)
#### D-05.1 Data Minimisation
<!-- participants: GDPR, CRA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-015, SO-GDPR-016 | Personal data limited to adequate/relevant/necessary + Art. 6(4) compatibility test + Art. 6(1)(a)–(f) lawfulness bases | Personal data; controller-driven |
| NIS2 | — | Out-of-scope (sole authority: GDPR) | n/a |
| CRA | SO-CRA-034 | Product data (personal or other) limited to adequate/relevant/necessary for intended purpose | Product data; manufacturer design |
| DORA | — | Out-of-scope (sole authority: GDPR) | n/a |
| AI_Act | SO-AIACT-003, SO-AIACT-004, SO-AIACT-005, SO-AIACT-006 | High-risk AI training/validation/testing datasets meet quality criteria + bias-detection data governance + exceptional special-category processing for bias correction | Training data; provider-driven |
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.1 per AEGIS taxonomy §4.1 — both are operational-resilience/incident-reporting focused, not data-lifecycle. GDPR is the dedicated authority; CRA addresses product-level (which can include non-personal data); AI Act addresses training-data-quality specifically.
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,CRA,AI_Act -->
- **Special-category-data exception creates a 3-way interaction.** GDPR Art. 9(1) prohibits, AI Act Art. 10(5) creates the exception, CRA Annex I Part I (2)(g) addresses only adequacy/relevance/necessity (silent on special-category). The pairwise readings (GDPR↔CRA, GDPR↔AI_Act, CRA↔AI_Act) each capture part of the interaction, but the *non-pairwise observation* is that AI Act's exception enables a processing class that neither GDPR nor CRA explicitly contemplates. Phase 2 must codify the AI Act exception as a gateway clause: it is *permitted* by AI Act, *limited* by GDPR Art. 9(2) residual constraints, and *unspecified* by CRA (CRA defers to whichever regulation governs the personal-data status of the data).
<!-- /emergent -->
##### SR cross-validation
NIST CSF 2.0 anchoring is dominated by **PR.DS-12** (Data disposal managed) and **ID.AM-03** (Asset inventory prioritised). GDPR SR-GDPR-025 maps both directly. CRA SR-CRA-046 maps PR.DS-12 + ID.AM-03. AI Act SR-AIACT-004/005 adds PR.DS-01 (Data-at-rest protected) and PR.PS-06 (Secure software development practices integrated). The CSF 2.0 surface is consistent — no CSF cross-mapping conflict. The CSF layer does not separately enumerate training-data minimisation, which is a known gap; AI Act's data-governance obligation is partially outside the CSF 2.0 scope and is appropriately flagged as a regulatory-specific construct.
##### Downstream implication
Phase 2 obligation derivation must produce a 3-track minimisation matrix: (1) runtime minimisation (CRA Annex I Part I (2)(g)), (2) personal-data minimisation (GDPR Art. 5(1)(c) + Art. 6(4)), (3) training-data quality (AI Act Art. 10(1)–(5)). For high-risk AI products processing personal data, all three apply simultaneously. Phase 3 case generation must surface the AI Act Art. 10(5) special-category exception explicitly, because it is the only point where data minimisation is *relaxed* by one of the three regulations.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-05.1
title: D-05.1 Data Minimisation — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-05 Data Lifecycle
sub_domain: D-05.1 Data Minimisation
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md
status: DRAFT
---
> **Domain analysis:** [D-05.1 Data Minimisation](../../DomainAnalysis/D-05_Data-Lifecycle/D-05.1.md)
#### D-05.1 Data Minimisation
<!-- participants: GDPR, CRA, AI_Act -->
**Participants (from CRDA):** GDPR, CRA, AI_Act
**Sole-authority note:** NIS2 and DORA are out-of-scope for D-05.1 per AEGIS taxonomy §4.1 — both are operational-resilience / incident-reporting focused, not data-lifecycle. GDPR is the dedicated authority; CRA addresses product-level (which can include non-personal data); AI Act addresses training-data-quality specifically.

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

