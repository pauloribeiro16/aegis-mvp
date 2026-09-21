# D-01.1 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-001 / SO-CRA-002 | State-of-the-art encryption of stored data (personal or other) | Manufacturer; Annex I Part I (1) + (2)(e); product-level; state-of-the-art baseline + harmonised-standards floor |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | continuous product-side baseline | product with digital elements | market surveillance authority + ENISA | Annex I Part I (1) + (2)(e) |

## Sub-SO (CRA)

#### D-01.1.3 — Sub-SO for CRA

```yaml
id: SO-D-01.1.CRA
subdomain: D-01.1
applies_to: [CRA]
inherits_from: SO-CRA-002
source_SR: SR-CRA-002
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Where a product with digital elements stores data —
personal or other — the confidentiality of that data is protected by
encrypting relevant data at rest using state-of-the-art mechanisms
(Annex I Part I (2)(e)).

**CSF anchors (from `SR-CRA-002` v0.3 security_rationale):**
PR.DS-01.
*(The umbrella `SR-CRA-001` additionally maps PR.DS-02 for the in-transit
channel of the same Annex I (2)(e) clause; that anchor is covered by
`SO-D-01.2.CRA` in §D-01.2 below.)*

---


## Security Requirements (CRA)

#### 1.1.3 — Product data at rest (state-of-the-art)

```yaml
- req_id: 1.1.3
  volere_section: 15
  volere_subtype: integrity

  title: "Product-stored data is encrypted using state-of-the-art mechanisms"

  derives_from:
    hso_sub_so: SO-D-01.1.CRA
    per_reg_so: SO-CRA-002
    source_sr: SR-CRA-002
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md
    objective_ref_section: "### D-01.1.3"

  description: |
    The product shall protect the confidentiality of stored data — personal or other — by encrypting relevant data at rest using state-of-the-art mechanisms, in a manner that renders the data unintelligible to any person who is not authorised to access it (CRA Annex I Part I (2)(e), read with Annex II `personal data` Art. 3(47) cross-reference to GDPR Art. 4(1)).

  fit_criterion: |
    State-of-the-art symmetric encryption (AES-256 minimum, or harmonised-standards-conformant equivalent under CRA Art. 27) is applied to all data at rest of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met for the relevant data; key custody is functionally separated by role-based access control (key-material custodian vs operational-environment custodian are distinct roles with distinct credentials); verified by Annex I conformity-assessment evidence + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key Management — pending generation)"]

  nist_csf: [PR.DS-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim from SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (1) ensure an appropriate level of cybersecurity based on the risks presented by the product. Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms, "or by using other technical means."

**CRA article (verbatim — SR-CRA-001 + SR-CRA-002, Annex I Part I (1) + (2)(e)):**
> Annex I Part I (2)(e) the confidentiality of stored, transmitted or otherwise processed data — personal or other — by encrypting relevant data at rest or in transit using state-of-the-art mechanisms.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.1: GDPR↔CRA CORRECTED from COMPLEMENTARY; NIS2↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

**Considerations.**

- The CRA state-of-the-art baseline + harmonised-standards anchor (Art. 27)
  is the strictest of the four participating regs; meeting the CRA floor
  discharges the GDPR `appropriate` obligation, the NIS 2 `where appropriate`
  obligation, and the DORA `high standards` obligation on the same data,
  when the CRA-regulated product is the artefact storing the data (CRDA-deep
  GDPR↔CRA pair reasoning — the convergence is not nominal: the strictest
  floor satisfies the others on the at-rest dimension).


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # CRA↔NIS2 = Y (NIS 2 essential entity uses CRA product — typical); CRA↔GDPR = Conditional (integrated manufacturer-controller); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA state-of-the-art baseline + harmonised-standards anchor (Art. 27)
    is the strictest of the four participating regs; meeting the CRA floor
    discharges the GDPR `appropriate` obligation, the NIS 2 `where appropriate`
    obligation, and the DORA `high standards` obligation on the same data,
    when the CRA-regulated product is the artefact storing the data (CRDA-deep
    GDPR↔CRA pair reasoning — the convergence is not nominal: the strictest
    floor satisfies the others on the at-rest dimension). (Copied from the HSO
    Considerations block of `### D-01.1.3`; preserved here for self-contained
    traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=1 -->

