# D-01.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-001 (cross-ref) / SO-CRA-003 | Confidentiality of data in transit via state-of-the-art encryption + attack-surface limitation | Manufacturer; Annex I Part I (2)(e) + (2)(j); product-level; state-of-the-art baseline + attack-surface-limitation |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | continuous product-side baseline | data transmitted by product with digital elements | MSA + ENISA | Annex I Part I (2)(e) + (2)(j) |

## Sub-SO (CRA)

#### D-01.2.2 — Sub-SO for CRA

```yaml
id: SO-D-01.2.CRA
subdomain: D-01.2
applies_to: [CRA]
inherits_from: SO-CRA-003
source_SR: SR-CRA-003
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Where data is transmitted by a product with digital
elements — personal or other — the confidentiality of the data in transit
is protected by encrypting relevant data using state-of-the-art mechanisms,
with the Annex I (2)(j) attack-surface-limitation leg constraining the
exposed interfaces through which the data could otherwise leak (Annex I
Part I (2)(e) + (2)(j)).

- The (2)(e)+(2)(j) combination operationalises the in-transit cell of the
  Annex I umbrella; PR.DS-02 + PR.IR-01 are the joint anchors, with
  PR.IR-01 capturing the attack-surface-limitation leg.

**CSF anchors (from `SR-CRA-003` v0.3 security_rationale):**
PR.DS-02, PR.IR-01.

---


## Security Requirements (CRA)

#### 1.2.2 — Product data in transit (state-of-the-art + attack-surface-limitation)

```yaml
- req_id: 1.2.2
  volere_section: 15
  volere_subtype: integrity

  title: "Product-transmitted data is encrypted with state-of-the-art mechanisms and exposed interfaces are minimised"

  derives_from:
    hso_sub_so: SO-D-01.2.CRA
    per_reg_so: SO-CRA-003
    source_sr: SR-CRA-003
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.2.md
    objective_ref_section: "### D-01.2.2"

  description: |
    The product shall protect the confidentiality of data in transit by encrypting the relevant data using state-of-the-art mechanisms, in a manner that renders the data unintelligible to any person not authorised to access it, and shall limit the attack surface of the product with digital elements by constraining the exposed interfaces through which the data could otherwise leak (CRA Annex I Part I (2)(e) + (2)(j)).

  fit_criterion: |
    State-of-the-art symmetric encryption (e.g. TLS 1.3 with AES-256-GCM or equivalent, harmonised-standards-conformant under CRA Art. 27) is applied to data in transit of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met; the Annex I (2)(j) attack-surface-limitation leg is documented (exposed interfaces enumerated, default ports minimised, unused services disabled); both internal east-west traffic and externally-exposed transport edges are covered per the R3 reading; verified by Annex I conformity-assessment evidence + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key/Certificate Management — pending generation)", "3.x (Mutual Authentication — pending generation)"]

  nist_csf: [PR.DS-02, PR.IR-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim — SR-CRA-003, Annex I Part I (2)(e) + (2)(j)):**
> Annex I Part I (2)(e) … by encrypting relevant data at rest or in transit using state-of-the-art mechanisms. Annex I Part I (2)(j) limit attack surfaces … including external interfaces.

**CRA article (verbatim — SR-CRA-003, Annex I Part I (2)(e)+(j)):**
> Annex I Part I (2)(e) … encrypting relevant data at rest or in transit using state-of-the-art mechanisms. Annex I Part I (2)(j) limit attack surfaces.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.2: GDPR↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

**Considerations.**

- The CRA state-of-the-art + attack-surface-limitation substrate is stricter
  than GDPR's risk-anchored layer; meeting CRA discharges GDPR on the
  in-transit channel for the same artefact.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # CRA↔GDPR = Y (CRA product transmits personal data — typical); CRA↔DORA = Y (DORA FE uses CRA product); HL engages on overlap (disjoint in baseline as manufacturer ≠ controller/FE)

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA state-of-the-art + attack-surface-limitation substrate is stricter
    than GDPR's risk-anchored layer; meeting CRA discharges GDPR on the in-transit
    channel for the same artefact. The (2)(e)+(2)(j) combination operationalises
    the in-transit cell of the Annex I umbrella; PR.DS-02 + PR.IR-01 are the joint
    anchors, with PR.IR-01 capturing the attack-surface-limitation leg. (Copied
    from the HSO Considerations block of `### D-01.2.2`; preserved here for
    self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=0 -->

