# D-01.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-004 | Cryptographic key separation from operational environment (custodian ≠ consumer) | Manufacturer; Annex I Part I (2)(d)+(e) functional-RBAC reading (T2-vs-text gap reading per `99_CRA_Synthesis.md` §4); product-level; "personal or other"; state-of-the-art baseline |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | continuous product-side baseline | cryptographic keys of product with digital elements | MSA + ENISA | Annex I Part I (2)(d) access control + (2)(e) `other technical means` |

## Sub-SO (CRA)

#### D-01.3.2 — Sub-SO for CRA

```yaml
id: SO-D-01.3.CRA
subdomain: D-01.3
applies_to: [CRA]
inherits_from: SO-CRA-004
source_SR: SR-CRA-004
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Cryptographic keys and related authentication material used
to protect the confidentiality and integrity of stored, transmitted or
otherwise processed data by a product with digital elements — personal or
other — are managed with separation of roles such that possession of the
key material is not bundled with possession of the operational environment
that uses it (Annex I Part I (2)(d) access-control + (2)(e) "other technical
means" reading per `SR-CRA-004` ambiguity_notes; the Annex I text does not
mention key management explicitly — the synthesis catalogue
`99_CRA_Synthesis.md` §4 flags this as a T2-vs-text gap — so the
key-separation reading rests on the combination of Annex I (2)(d)
access-control duty with the Annex I (2)(e) "other technical means"
residual).

**Considerations.**
- The reading chosen anchors separation in functional role-based access
  control rather than physical separation: the key-material custodian and
  the operational-environment custodian are distinct roles with distinct
  credentials.
**CSF anchors (from `SR-CRA-004` v0.3 security_rationale):**
PR.DS-01, PR.AA-05, GV.OV-01.
*(PR.DS-01 anchors the cryptographic protection so that possession of the
key — not the storage medium — is the necessary condition for
intelligibility; PR.AA-05 captures the access-control dimension with
distinct custodians for key-material and operational environments under
least-privilege entitlements; GV.OV-01 ensures the key-separation policy is
reviewed across the support period under the manufacturer's broader
risk-management strategy.)*

---


## Security Requirements (CRA)

#### 1.3.2 — Product-side cryptographic key separation from operational environment

```yaml
- req_id: 1.3.2
  volere_section: 15
  volere_subtype: access

  title: "Cryptographic keys of product with digital elements separated from operational environment"

  derives_from:
    hso_sub_so: SO-D-01.3.CRA
    per_reg_so: SO-CRA-004
    source_sr: SR-CRA-004
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.3.md
    objective_ref_section: "### D-01.3.2"

  description: |
    The product shall manage cryptographic keys and related authentication material used to protect the confidentiality and integrity of stored, transmitted or otherwise processed data with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it (CRA Annex I Part I (2)(d) access-control + (2)(e) `other technical means` reading; T2-vs-text gap per `99_CRA_Synthesis.md` §4 — Annex I text does not mention key management explicitly, so the key-separation reading rests on the combination of (2)(d) access-control with the (2)(e) `other technical means` residual).

  fit_criterion: |
    The product with digital elements implements functional RBAC separation such that the key-material custodian and the operational-environment custodian are distinct roles with distinct credentials under least-privilege entitlements; the Annex I (2)(e) `render unintelligible` test is met by separation of role credentials (not by physical separation alone); the state-of-the-art baseline governs primitive choice (CRA Art. 27 harmonised-standards-conformant equivalent acceptable); verified by Annex I conformity-assessment evidence + technical documentation inspection (Annex VII) + MSA/ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-01, PR.AA-05, GV.OV-01]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim — SR-CRA-004, Annex I Part I (2)(d) + (2)(e)):**
> Annex I Part I (2)(e) … by encrypting … and by using other technical means. Annex I Part I (2)(d) protect from unauthorised access by appropriate control mechanisms.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.3: GDPR↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

- The CRA state-of-the-art baseline + harmonised-standards anchor (Art. 27)
  governs the primitive choice; the CRA product-side key-separation
  baseline is the necessary-but-not-sufficient floor for DORA financial
  entities and the floor for CRA-only manufacturers.


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # CRA↔GDPR = Y (CRA product stores personal data — typical); CRA↔DORA = Y (DORA financial entity uses CRA product); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA product-side functional-RBAC separation is the necessary-but-not-
    sufficient floor for DORA financial entities and the floor for CRA-only
    manufacturers. The state-of-the-art baseline + harmonised-standards anchor
    (Art. 27) governs the primitive choice. CRDA-deep notes (CRA↔DORA pair)
    that CRA is the necessary-but-not-sufficient product-side floor and DORA
    is the entity-side depth layer — the two are genuinely layered in depth,
    not scope-disjoint. A SaaS-using-CRA-product scenario has disjoint
    baseline obligations (CRA manufacturer supplies product-side key-
    separation baseline; GDPR controller implements the de-attribution test
    on its own key custody); the CRA product-side floor met at the
    manufacturer does not by itself discharge the GDPR controller's
    deployment-side responsibility. (Copied from the HSO Considerations
    block of `### D-01.3.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=0 -->

