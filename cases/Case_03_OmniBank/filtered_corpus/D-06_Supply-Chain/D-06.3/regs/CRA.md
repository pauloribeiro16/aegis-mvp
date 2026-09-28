# D-06.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SG-CRA-039; SG-CRA-040 | Importers perform pre-market checks and escalation; distributors act with due care, verify CE/documentation/manufacturer/importer compliance, and escalate non-conformity or vulnerabilities | Product market-access layer; importer/distributor obligations to manufacturer and market surveillance authority (MSA), imposed by regulation rather than negotiated as a DPA |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | importer/distributor market-access chain and component-vulnerability hand-off | before market placement; reason to believe non-conformity; vulnerability identified | pre-market check record; CE/documentation verification; non-conformity/corrective-measures record | MSA; manufacturer; component supplier | Art. 19; Art. 20; Art. 13(6) |

## Sub-SO (CRA)

#### D-06.3.3 — Sub-SO for CRA

```yaml
id: SG-D-06.3.CRA
subdomain: D-06.3
applies_to: [CRA]
inherits_from: [SG-CRA-039, SG-CRA-040]
source_SR: [SR-CRA-051, SR-CRA-054, SR-CRA-055, SR-CRA-057, SR-CRA-058]
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** CRA contractual-security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place products with digital elements on the Union market only after verifying conformity assessment, technical documentation, CE marking, and manufacturer identification, and escalate significant risk or vulnerabilities to the manufacturer and MSA while taking corrective measures; distributors act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, and escalate non-conformity or vulnerabilities.

**CSF anchors (from CRA SRs):** GV.SC-02, GV.SC-04, RS.MI-01, RS.MA-04.

---


## Security Requirements (CRA)

#### 6.3.3 — Importer/distributor Art. 19/20 market-access duties + Art. 13(6) component-vulnerability escalation

```yaml
- req_id: 6.3.3
  volere_section: 15
  volere_subtype: immunity

  title: "Importer pre-market verification (Art. 19) + distributor due-care + non-conformity escalation (Art. 20) + component-vulnerability reporting (Art. 13(6)) — regulatory economic-operator duties, NOT DPA-style contracts"

  derives_from:
    hso_sub_so: SG-D-06.3.CRA
    per_reg_so: SG-CRA-039, SG-CRA-040
    source_sr: SR-CRA-051, SR-CRA-054, SR-CRA-055, SR-CRA-057, SR-CRA-058
    hso_file: ../../HierarchicalSecurityObjectives/D-06_Supply-Chain/D-06.3.md
    objective_ref_section: "### D-06.3.3"

  description: |
    The product shall enforce importer duties under Art. 19 (verify conformity assessment, technical documentation, CE marking, manufacturer identification before market placement; escalation when product presents significant risk or vulnerabilities, taking corrective measures) and distributor duties under Art. 20 (act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, escalate non-conformity or vulnerabilities), plus Art. 13(6) component-vulnerability reporting on becoming aware of a vulnerability (address and remediate in product per Annex I Part II; share code and documentation with OSS maintainer per Art. 13(6) sentence 2); CRA economic-operator duties are imposed by regulation rather than negotiated as a DPA.

  fit_criterion: |
    An economic-operator compliance matrix is maintained per importer/distributor/modifier with documented pre-market verification records (Art. 19(2) conformity-assessment verification + technical-documentation check + CE marking + manufacturer-identification verification) and due-care records (Art. 20(2) CE-marking verification + documentation review + manufacturer/importer-compliance verification); Art. 19(3) importer-measures records document escalation and corrective-measures when product presents significant risk or vulnerabilities; Art. 20(3) distributor non-conformity records document escalation to manufacturer/importer and corrective-measures without undue delay; Art. 13(6) sentence 1 component-vulnerability reporting address-and-remediate duty operates on becoming-aware (feeds manufacturer-side remediation per Annex I Part II), with Art. 13(6) sentence 2 OSS-sharing limb applying when an OSS component is integrated (code and documentation shared with OSS maintainer); the CRA economic-operator duties are MSA-facing regulatory obligations, NOT DPA-style negotiated contracts — the GDPR DPA matrix and DORA ICT-contract matrix do not subsume CRA duties (different actor, different regulatory direction, different recipient); in NIS 2 overlap (NIS 2 entity deploys CRA product), the CRA escalation feeds the NIS 2 supplier-risk-register input (NIS2↔CRA lifecycle hinge); verified by economic-operator compliance matrix review + Art. 19(2) pre-market verification records inspection + Art. 19(3) corrective-measures records audit + Art. 20(2) distributor due-care records inspection + Art. 20(3) non-conformity escalation log review + Art. 13(6) component-vulnerability reporting log review + MSA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [6.1.3 (third-party-component due diligence shapes component-vulnerability reporting inputs), 6.4.3 (substantial-modification accountability + 10-year economic-operator identification retention are the boundary-side handles that feed this matrix's records)]

  nist_csf: [GV.SC-04, RS.MI-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Art. 19 + Art. 20):**
> "An importer shall place on the market only products with digital elements that comply with Chapter II, Section 2 and where the relevant conformity assessment procedure has been carried out by the manufacturer or on behalf of the manufacturer … An importer shall, before placing a product with digital elements on the market, ensure that … the conformity assessment has been carried out, the technical documentation has been drawn up, the product bears the CE marking and is accompanied by the required documents … and the manufacturer has complied with the requirements set out in Article 13(5) and (7)." — CRA Art. 19(1)/(2)
>
> "A distributor shall act with due care in relation to the requirements of this Regulation when making a product with digital elements available on the market. Before making a product with digital elements available on the market, a distributor shall verify that … the CE marking has been affixed … the product is accompanied by the required documents … and the manufacturer and the importer have complied with the requirements set out in Article 13(5), (7) and (9) …" — CRA Art. 20(1)/(2)
>
> "Where a distributor has reason to believe that a product with digital elements is not in conformity with Chapter II, Section 2, the distributor shall not make the product available on the market until conformity has been restored, and shall inform the manufacturer and the market surveillance authority of the significant risk." — CRA Art. 20(3)
>
> "Where a vulnerability is identified in a product with digital elements that the distributor has made available on the market, the distributor shall inform the manufacturer and take immediate corrective measures necessary to bring the product into conformity, including, where appropriate, withdrawal or recall." — CRA Art. 20(4)

**CRA article (verbatim, Art. 13(6) sentence 1):**
> "Upon identifying a vulnerability in a component integrated in the product with digital elements, the manufacturer shall report the vulnerability to the person or entity manufacturing or maintaining that component, and address and remediate the vulnerability in accordance with the vulnerability handling requirements set out in Annex I, Part II." — CRA Art. 13(6) sentence 1


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE (CRDA-deep, D-06.3: GDPR↔CRA = DIFFERENT-PERSPECTIVE; NIS2↔CRA = COMPLEMENTARY; CRA↔DORA = DIFFERENT-PERSPECTIVE)
```

### from regs/CRA.md body

**Considerations.**

- Component-vulnerability reporting under Art. 13(6) is the post-contract upstream feedback path that connects CRA-side escalation with the NIS 2 supplier-security assessment (the NIS2↔CRA lifecycle hinge).

### from regs/CRA.md body

- The CRA layer is regulatory and market-surveillance-facing; it does not become a GDPR-style DPA or a DORA ICT-service contract.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller deployer; CRA market-access duties coexist with DPA — different actor and instrument); CRA↔NIS2 = Conditional (Y NIS 2 entity deploys CRA product; CRA escalation feeds NIS 2 supplier-risk-register); CRA↔DORA = Conditional (Y when CRA product procured by financial entity; CRA market-access duties coexist with DORA ICT-contract)

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA contractual-security obligation is the economic-operator duty structure imposed by regulation rather than negotiated as a DPA — importer Art. 19 pre-market verification + Art. 19(3) corrective-measures on significant risk/vulnerability + distributor Art. 20(2) due-care + Art. 20(3) non-conformity escalation + Art. 13(6) component-vulnerability reporting on becoming-aware; the operational substrate is an economic-operator compliance matrix keyed by actor (importer / distributor / manufacturer-equivalent / upstream component supplier) and trigger (pre-market placement / reason to believe non-conformity / vulnerability identified). The CRA layer is regulatory and market-surveillance-facing; it does NOT convert into DPA-style contracts or DORA ICT-service contracts because it maps to D-06.3 — its obligations are imposed on economic operators by regulation with MSA recipient. Art. 13(6) component-vulnerability reporting is the post-contract upstream feedback path that connects CRA-side escalation with the NIS 2 supplier-security assessment (the NIS2↔CRA lifecycle hinge). The CRA economic-operator records feed D-06.4-CRA boundary architecture (10-year retention, substantial-modification accountability, manufacturer-equivalent triggers). (Copied from the HSO Considerations block of `### D-06.3.3`; preserved here for self-containment per Volere shell `considerations` field definition.)
```

### from regs/CRA.md body

**CRA article (verbatim, Art. 19 + Art. 20):**

> (See GDPR↔CRA pair above for the verbatim Art. 19 + Art. 20 text.)

<!-- aegis:purity: own_reg=CRA; demoted=6; core_cross_mentions=1 -->
