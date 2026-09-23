# D-06.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-021 | Controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)) | Processor due diligence; controller-driven; qualitative `sufficient guarantees` + Art. 28(2) sub-processor authorisation + Art. 4(7)/(8) controller/processor definitions; GV.SC-02 + GV.SC-04 + ID.AM-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | processor as legal entity (data-processing counterparty) | per-processor engagement (Art. 28(1) prior-to-engagement gate + Art. 28(2) sub-processor authorisation chain) | `sufficient guarantees` (qualitative) + Art. 28(3) DPA clauses (closed list: instructions + purpose limitation + confidentiality + security + sub-processor authorisation + data-subject-rights assistance + Art. 33/34 assistance + return/deletion + audit/inspection) + EDPB Guidelines 07/2020 4-factor test (knowledge, reliability, resources, compliance-track-record) | supervisory authority (DPA) — Art. 5(2) accountability + Art. 30 RoPA on processors + Art. 28(3) DPA inspection | Art. 28(1) + Art. 28(2) + Art. 28(3)(a)–(h) + Art. 4(7)/(8) + Art. 30(2) + Art. 5(2) + Art. 24 controller accountability + Art. 25 by-design + Art. 32 security of processing |

## Sub-SO (GDPR)

#### D-06.1.1 — Sub-SO for GDPR

```yaml
id: SG-D-06.1.GDPR
subdomain: D-06.1
applies_to: [GDPR]
inherits_from: SG-GDPR-021
source_SR: SR-GDPR-033
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)); the Art. 28(3) DPA closed-list clauses (a)–(h) are documented and the sub-processor authorisation chain (Art. 28(2)) is material to the due diligence.

**Considerations.**
- The EDPB Guidelines 07/2020 4-factor reading (knowledge + reliability of resources + compliance track-record + financial stability) operationalises the `sufficient guarantees` qualitative threshold.
**CSF anchors (from `SR-GDPR-033` v0.3 security_rationale):**
GV.SC-02, GV.SC-03.
**PF 1.1 anchors (from `SR-GDPR-033` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
ID.DE-P5, ID.IM-P2.
*(GV.SC-02 anchors the supplier-prioritisation dimension — suppliers
(here: processors) are prioritised by criticality, with the
criticality anchored on the processor's data-class and volume
exposure; the EDPB Guidelines 07/2020 4-factor reading operationalises
GV.SC-02 in the data-processing-counterparty context. GV.SC-04
anchors the supplier-routine-assessment dimension — suppliers are
routinely assessed using audits, test results, certifications, or
other forms of evaluation to confirm they are meeting their
contractual obligations; the Art. 28(3)(h) audit / inspection clause
maps to GV.SC-04 directly. ID.AM-04 anchors the resource-prioritised
dimension — resources (here: data-processing dependencies on
processors) are prioritised based on classification, with the
criticality anchored on the personal-data class and volume. The
three subcategories together enable the controller to demonstrate
ex post, through documented processor due-diligence records,
contract audit / inspection evidence, and Art. 30 RoPA processor-
categorisation records, that the Art. 28(1) `sufficient guarantees`
threshold has been calibrated by the EDPB Guidelines 07/2020 4-factor
test and that the Art. 28(3) DPA closed-list clauses have been
documented and attested to by the processor.)*

---


## Security Requirements (GDPR)

#### 6.1.1 — Processor-as-legal-entity due diligence with documented `sufficient guarantees`

```yaml
- req_id: 6.1.1
  volere_section: 15
  volere_subtype: immunity

  title: "Processor-as-legal-entity due diligence with documented `sufficient guarantees` and Art. 28(3) DPA closed-list clauses"

  derives_from:
    hso_sub_so: SO-6.1.GDPR
    per_reg_so: SG-GDPR-021
    source_sr: SR-GDPR-033
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/6.1.md
    objective_ref_section: "### 6.1.1"

  description: |
    The product shall operate processor-as-legal-entity due diligence on each data-processing counterparty before engagement — verifying that the processor provides sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights — and shall document the EDPB Guidelines 07/2020 4-factor assessment (knowledge + reliability of resources + compliance track-record + financial stability), the Art. 28(3) closed-list DPA clauses (a)–(h), and the sub-processor authorisation chain under Art. 28(2) (GDPR Art. 28(1) `sufficient guarantees` + Art. 28(2) sub-processor authorisation + Art. 28(3) DPA closed list + Art. 4(7)/(8) controller/processor definitions).

  fit_criterion: |
    A processor-selection discipline is operated before engagement covering each prospective processor via GV.SC-02 documented-due-diligence practice (written due-diligence questionnaire, certifications review, security-measures audit, sub-processor inventory) anchored on the EDPB Guidelines 07/2020 4-factor test; the Art. 28(3) closed-list DPA clauses (a) documented instructions + (b) confidentiality + (c) Art. 32 measures + (d) sub-processor conditions + (e) data-subject-rights assistance + (f) Art. 33/34 incident-assistance + (g) deletion-or-return + (h) audit/inspection are documented in each processor contract with attestation of compliance; the Art. 28(2) sub-processor authorisation chain is materialised as a written prior-authorisation regime (specific or general with information right) and a sub-processor list maintained in the Art. 30(2) RoPA processor record; the processor-as-legal-entity due diligence discipline operates at the data-processing-counterparty boundary only, with the tier hand-off to supplier-tier (NIS 2 leg), component-tier (CRA leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces (when the same supplier is a processor + direct supplier + component source + ICT provider, the four assessments compose into a single supplier-of-record without collapsing the per-tier evidence); verified by EDPB 07/2020 4-factor processor-guarantees evidence review + Art. 28(3) closed-list DPA-clause attestation review + Art. 28(2) sub-processor authorisation chain inspection + Art. 30(2) RoPA processor-record inspection + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.2 (when controller is also essential/important entity — processor-tier assessment feeds supplier-tier assessment), 6.1.3 (when controller deploys/manufactures CRA product — component-tier feeds processor-tier for personal-data subset), 6.1.4 (when controller is also financial entity — DORA four-factor satisfies GDPR `sufficient guarantees` with GDPR-specific Art. 28(3) clauses appended on controller side)]

  nist_csf: [GV.SC-02, GV.SC-03]
  nist_pf: [ID.DE-P5, ID.IM-P2]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 28(1) + Art. 28(2) + Art. 4(7)/(8)):**
> "The controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing will meet the requirements of this Regulation and ensure the protection of data subjects' rights." — Art. 28(1) GDPR
>
> "The processor shall not engage another processor without prior specific or general written authorisation of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of other processors, thereby giving the controller the opportunity to object to such changes." — Art. 28(2) GDPR

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-06.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — sharper-qualitative-on-shared-risk-substrate; GDPR `sufficient guarantees` is sharper than the NIS 2 `appropriate and proportionate` chapeau on the same supplier-relationship risk substrate); GDPR↔CRA = DIFFERENT-PERSPECTIVE (SAME — entity-level processor as legal entity vs product-level component as technical artefact, integrated-stack layers); GDPR↔DORA = COMPLEMENTARY (SAME — DORA exceeds GDPR, Art. 28(1) four-factor proportionality operationalises GDPR `sufficient guarantees` with sharper factors, GDPR-specific Art. 28(3) DPA clauses appended on controller side))
```

### from regs/GDPR.md body

- On an integrated-stack manufacturer-controller-deployer, the controller-side GDPR due diligence on the manufacturer-as-processor layers vertically with the manufacturer's own CRA Art. 13(5) third-party component due diligence — the controller is still owed the Art. 28(1) due diligence on the manufacturer as the data-processing counterparty, even where the manufacturer has self-certified the product.

### from regs/GDPR.md body

- DORA's Art. 28(1) four-factor proportionality operationalises GDPR `sufficient guarantees` with sharper factors; a financial entity subject to DORA Art. 28 satisfies GDPR Art. 28(1) via the proportionality documentation but must explicitly document the GDPR-specific processor guarantees (Art. 28(3)(a) instruction-bound processing, Art. 28(3)(h) audit, Art. 28(2) sub-processor authorisation, Art. 28(3)(b) confidentiality, Art. 28(3)(e) data-subject-rights assistance, Art. 28(3)(f) Art. 33/34 incident-assistance, Art. 28(3)(g) deletion-or-return).


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-essential-entity; data-processing supplier is also direct supplier under Art. 21(2)(d); both apply on same supplier relationship with GDPR `sufficient guarantees` sharpening NIS 2 chapeau); GDPR↔CRA = Conditional (Y integrated manufacturer-controller stack; disjoint baseline: data-processing-counterparty ↔ product-component); GDPR↔DORA = Conditional (Y financial-entity-controller; disjoint baseline: data-processing-counterparty ↔ ICT-third-party); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR vendor-risk-assessment obligation is the processor-as-legal-entity due diligence on each data-processing counterparty; the operational substrate is a documented processor-selection discipline anchored on the EDPB Guidelines 07/2020 4-factor test (knowledge + reliability of resources + compliance track-record + financial stability), with the Art. 28(3) closed-list DPA clauses materialising the assessment into the contractual instrument and the Art. 28(2) sub-processor authorisation chain extending the discipline downstream. The `sufficient guarantees` threshold is qualitative (Berry-flagged VAG-S2 per SR-GDPR-033 ambiguity_notes); the chosen reading is documented-due-diligence practice, not controller self-attestation, and an alternative reading under which self-attestation is sufficient is rejected. The processor-as-legal-entity target object is distinct from the NIS 2 direct-supplier-as-relationship, the CRA third-party-component-as-technical-artefact, and the DORA ICT-third-party-as-financial-entity-counterparty — the four target objects are layered not collapsed. On an integrated manufacturer-controller-deployer stack, the controller-side GDPR due diligence on the manufacturer-as-processor layers vertically with the manufacturer's own CRA Art. 13(5) third-party component due diligence; the controller is still owed the Art. 28(1) due diligence on the manufacturer as the data-processing counterparty even where the manufacturer has self-certified the product. DORA Art. 28(1) four-factor proportionality operationalises GDPR `sufficient guarantees` with sharper factors; a financial entity subject to DORA Art. 28 satisfies GDPR Art. 28(1) via the proportionality documentation but must explicitly document the GDPR-specific processor guarantees (Art. 28(3)(a) instruction-bound processing, Art. 28(3)(h) audit, Art. 28(2) sub-processor authorisation, Art. 28(3)(b) confidentiality, Art. 28(3)(e) data-subject-rights assistance, Art. 28(3)(f) Art. 33/34 incident-assistance, Art. 28(3)(g) deletion-or-return) — the GDPR-specific clauses are appended on the controller side. (Copied from the HSO Considerations block of `### 6.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=2 -->
