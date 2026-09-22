# D-05.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-034 | Product data (personal or other) limited to adequate/relevant/necessary for intended purpose | Product data; manufacturer design; Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) `intended purpose`; ID.AM-08 + ID.AM-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product data (personal or other) | design / development of a product with digital elements with attack-surface implications | `adequate, relevant and limited to what is necessary in relation to the intended purpose of the product` (Annex I Part I (2)(g) verbatim); the `intended purpose` per Art. 3(23) | design-time + runtime (per Annex I risk assessment under Art. 13(2)) | market surveillance authority (MSA) — Annex VII §2 technical documentation + Annex VII §3 risk-assessment record | Annex I Part I (2)(g) + Art. 13(3) sentence 2 + Art. 3(23) intended purpose + Art. 13(2) risk assessment |

## Sub-SO (CRA)

#### D-05.1.2 — Sub-SO for CRA

```yaml
id: SO-D-05.1.CRA
subdomain: D-05.1
applies_to: [CRA]
inherits_from: SO-CRA-034
source_SR: SR-CRA-046
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)).

**CSF anchors (from `SR-CRA-046` v0.3 security_rationale):**
ID.AM-08, ID.AM-03.
*(ID.AM-08 anchors the strategic-posture dimension — data is managed
consistent with the manufacturer's risk strategy, with the Art. 13(2)
risk assessment supplying the proportionality bar that determines which
data classes are adequate, relevant, and necessary for the product's
intended purpose. ID.AM-03 anchors the operational-traceability
dimension — inventories of data and corresponding metadata for
designated data types are maintained, providing the demonstrable
record that the manufacturer knows which data classes are present in
the product and on what basis each class was admitted under the
minimisation principle. The two subcategories together enable the
manufacturer to demonstrate ex post, through risk-strategy alignment
and data-inventory records in the technical documentation under Annex
VII §2, that the Annex I Part I (2)(g) minimisation principle has
been discharged and that the product's data footprint is no broader
than its intended purpose requires.)*

---


## Security Requirements (CRA)

#### 5.1.2 — Product-data minimisation per Annex I Part I (2)(g) tied to Art. 3(23) intended purpose

```yaml
- req_id: 5.1.2
  volere_section: 15
  volere_subtype: privacy

  title: "Product data limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with risk-assessment proportionality calibration"

  derives_from:
    hso_sub_so: SO-D-05.1.CRA
    per_reg_so: SO-CRA-034
    source_sr: SR-CRA-046
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.1.md
    objective_ref_section: "### D-05.1.2"

  description: |
    The product shall limit data processed by a product with digital elements — personal or other — to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)).

  fit_criterion: |
    A manufacturer-side product-data minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory per product variant with intended-purpose tag) + ID.AM-08 data managed consistent with the manufacturer's risk strategy (Art. 13(2) risk assessment supplies the proportionality bar); the Annex I Part I (2)(g) `adequate, relevant and limited to what is necessary in relation to the intended purpose of the product` test is applied to every data-collection surface at design-time and re-calibrated on any product change; the Art. 3(23) intended purpose is documented in the technical documentation under Annex VII §2 and the risk assessment under Annex VII §3 calibrates which data classes are adequate/relevant/necessary for that purpose; for an integrated-stack manufacturer-controller (the same party is both manufacturer and controller), the manufacturer-controller documents the Art. 6(4) compatibility assessment separately from the CRA-side design-time minimisation; the CRA-side minimisation does NOT require the Art. 6(4) compatibility test on change of purpose (that is the GDPR-side controller's residual obligation); CRA-side coverage of training data is sequential not concurrent with AI Act Art. 10 — CRA Annex I Part I (2)(g) operates at runtime on product data, AI Act Art. 10 operates upstream on the training pipeline; verified by Annex VII §2 technical-documentation inspection + Annex VII §3 risk-assessment record review + per-data-class intended-purpose mapping audit + Annex I Part I (2)(g) minimisation test per data-class review + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: INSPECT
  dependencies: [5.1.1 (when CRA-classified product processes personal data at runtime — verbatim-language match binds; GDPR-side Art. 6(4) compatibility test is the residual GDPR-only requirement not absorbed by CRA-side), 5.1.3 (when CRA-classified high-risk AI product — upstream AI Act training-data quality feeds downstream CRA runtime minimisation; 3-track matrix applies)]

  nist_csf: [ID.AM-08, ID.AM-03]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part I (2)(g) + Art. 13(3) sentence 2):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (g) limit its attack surfaces, including attack surfaces of third-party components integrated into the product, by means of an internal architecture that minimises the exposure of the product's attack surfaces and the data processed by it, including by means of the processing of only the data that are adequate, relevant and limited to what is necessary in relation to the intended purpose of the product ('data minimisation')." — CRA Annex I Part I (2)(g)
>
> "The risk assessment shall be performed by the manufacturer and shall … take into account … the intended purpose of the product with digital elements, as well as the circumstances of use … including the reasonably foreseeable use thereof." — CRA Art. 13(3) sentence 2

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-05.1: GDPR↔CRA = COMPLEMENTARY (SAME — verbatim "adequate, relevant and limited to what is necessary" language; controller-driven purpose vs manufacturer-design intended purpose); CRA↔AI_Act = COMPLEMENTARY (SAME — runtime product data vs training pipeline data; different lifecycle stages, sequential not concurrent))
```

### from regs/CRA.md body

**Considerations.**

- Verbatim operative-language match with GDPR Art. 5(1)(c) — the literal "adequate, relevant and limited to what is necessary" wording binds both regimes on the same dataset when a CRA-compliant product processes personal data at runtime.

### from regs/CRA.md body

- CRA does NOT require the GDPR Art. 6(4) compatibility test on change of purpose; the residual GDPR-only requirement (change-of-purpose compatibility) is documented by the controller on the controller side, not absorbed into CRA Annex I Part I (2)(g).

### from regs/CRA.md body

- Data-class layering: CRA operates at runtime on the product's intended-purpose data; GDPR operates upstream on the data-subject collection decision; AI Act operates upstream on the training pipeline. The three data classes are layered, not collapsed.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated-stack manufacturer-controller; the runtime product minimisation applies to the personal-data subset flowing through the product at runtime; disjoint in baseline: product-data vs personal-data controller-driven collection); CRA↔AI_Act = Conditional (Y when training data for a CRA-classified high-risk AI product is the same dataset; AI Act training-stage quality criteria sharpen CRA runtime minimisation; disjoint in baseline — different lifecycle stages, sequential not concurrent); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA data-minimisation obligation is the manufacturer-side product-data minimisation tied to the Art. 3(23) intended purpose, with the Art. 13(2) risk assessment supplying the proportionality calibration and the Art. 13(3) sentence 2 reasonably-foreseeable-use supplying the misuse-envelope. The verbatim operative-language match with GDPR Art. 5(1)(c) — the literal "adequate, relevant and limited to what is necessary" wording — binds both regimes on the same dataset when a CRA-compliant product processes personal data at runtime; the stricter operational interpretation binds on the shared risk substrate. CRA does NOT require the GDPR Art. 6(4) compatibility test on change of purpose; the residual GDPR-only requirement is the change-of-purpose compatibility assessment documented by the controller on the controller side. Data-class layering: CRA operates at runtime on the product's intended-purpose data; GDPR operates upstream on the data-subject collection decision; AI Act operates upstream on the training pipeline. The three data classes are layered, not collapsed. (Copied from the HSO Considerations block of `### D-05.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=2 -->