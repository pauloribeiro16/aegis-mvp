# D-03.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-016 (partial) | Protection from unauthorised access via appropriate control mechanisms, which may include authentication, identity, or access-management systems (no explicit MFA mandate) | Manufacturer; Annex I Part I (2)(d); "including but not limited to" + 3-way OR (authentication / identity / access-management); PR.AA-01 + PR.AA-05 + PR.AA-06 + DE.CM-09 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | permissive (`may include authentication`) | product users + services + integrated components | continuous (operational lifetime) + risk-anchored | `appropriate control mechanisms … commensurate with identified cybersecurity risk` (Annex I Part I (2)(d)) | market surveillance authority (Annex VII technical documentation) | Annex I Part I (2)(d) |

## Sub-SO (CRA)

#### D-03.2.3 — Sub-SO for CRA

```yaml
id: SO-D-03.2.CRA
subdomain: D-03.2
applies_to: [CRA]
inherits_from: SO-CRA-016 (partial)
source_SR: SR-CRA-023, SR-CRA-024
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Protection from unauthorised access uses appropriate
control mechanisms, which may include authentication, identity, or
access-management systems, appropriate to the identified cybersecurity
risk of the product (Annex I Part I (2)(d) — "including but not limited
to" + 3-way OR).

**Considerations.**
- The OJ Annex I Part I (2)(d) text does NOT contain the phrase `multi-factor` or `continuous authentication` (the T2 mapping that imposed these phrases is rejected on the literal OJ); the OJ names authentication as one of three admitted control families (the others being identity and access-management).
- CRA is the most permissive OJ-text anchor among the four participating regulators (the only one with an explicit "may include" language and no OJ-imposed authentication-strength threshold).
- The downstream AEV notification cascade (Art. 14) is part of D-04.3, not D-03.2.

**CSF anchors (from `SR-CRA-023` + `SR-CRA-024` v0.3 security_rationale):**
PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09.
*(`SR-CRA-023` covers the Annex I Part I (2)(d) authentication / identity
/ access-management 3-way OR + Art. 13(15) type/batch/serial unique
identification anchored to PR.AA-01 (identities and credentials managed
by the organisation — the authentication substrate) + ID.AM-01
(hardware inventories — the type/batch/serial marking backing the
SBOM-correlated identity register). `SR-CRA-024` covers the Annex I
Part I (2)(d)+(j) reporting-on-access and attack-surface-limitation
duty anchored to PR.AA-05 (access permissions per least privilege) +
PR.AA-06 (access limited to authorised users/services/hardware) +
DE.CM-09 (monitoring to detect attempted and successful unauthorised
access — the visibility leg that pairs with the preventive controls).
The two SRs together cover the (2)(d) `appropriate control
mechanisms, may include authentication` clause and the (2)(j)
attack-surface-limitation clause; the OJ does not specify the
authentication mechanism, so the SR preserves the OJ-literal
language without naming MFA.)*

---


## Security Requirements (CRA)

#### 3.2.3 — `Appropriate control mechanisms, may include authentication` (no explicit MFA mandate)

```yaml
- req_id: 3.2.3
  volere_section: 15
  volere_subtype: access

  title: "Appropriate control mechanisms for protection from unauthorised access, which may include authentication"

  derives_from:
    hso_sub_so: SO-D-03.2.CRA
    per_reg_so: SO-CRA-016 (partial)
    source_sr: SR-CRA-023, SR-CRA-024
    hso_file: ../../HierarchicalSecurityObjectives/D-03_Access-Control/D-03.2.md
    objective_ref_section: "### D-03.2.3"

  description: |
    The product shall protect against unauthorised access through appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product; the OJ Annex I Part I (2)(d) text does NOT contain the phrase `multi-factor` or `continuous authentication` — the T2 mapping that imposed these phrases is rejected on the literal OJ — and the OJ names authentication as one of three admitted control families (the others being identity and access-management) (CRA Annex I Part I (2)(d) — `including but not limited to` + 3-way OR).

  fit_criterion: |
    A product-side authentication-mechanism choice operates, anchored to a documented risk assessment for the product with digital elements; the OJ Annex I Part I (2)(d) text does not specify the authentication mechanism, so the SR preserves the OJ-literal language without naming MFA; the mechanism selection is at the manufacturer's discretion under the 3-way OR (authentication / identity / access-management); an MFA deployment at the CRA product-side exceeds the CRA requirement on the authentication dimension; a single-factor deployment at a CRA-regulated product is OJ-compliant under CRA but may not satisfy NIS 2 or DORA when those regs apply on the same party; reporting-on-access and attack-surface-limitation artefacts document least-privilege enforcement and authorised-only access to users/services/hardware; monitoring for attempted and successful unauthorised access (DE.CM-09) provides the visibility leg; verified by risk-assessment audit + mechanism-selection rationale records + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [3.1.3 (product-side identity substrate feeds the product-authentication mechanism choice)]

  nist_csf: [PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim):**
> Annex I Part I (2)(d) requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity, or access-management systems; the "including but not limited to" clause keeps the floor open to other technical means while naming the three substantive control families.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-03.2: GDPR↔CRA CORRECTED from COMPLEMENTARY; NIS2↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

- The CRA partial-coverage flag means that an MFA deployment at the CRA product-side exceeds the CRA requirement on the authentication dimension; a single-factor deployment at a CRA-regulated product is OJ-compliant under CRA but may not satisfy NIS 2 or DORA when those regs apply on the same party.

### from regs/CRA.md body

- For an organisation across multiple regulators, the CRA leg documents the product-side authentication baseline that the manufacturer operates at; an authentication-mechanism choice that exceeds the CRA permissive baseline (e.g. selecting MFA where the risk assessment warrants) is documented in Annex VII and feeds the downstream controller / NIS 2 essential-entity / financial-entity authentication architecture.

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y integrated manufacturer-controller; product hosting the authentication endpoint); CRA↔NIS2 = Conditional (Y NIS 2 entity deploying CRA product); CRA↔DORA = Conditional (Y DORA financial entity deploying CRA product); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    CRA is the most permissive OJ-text anchor among the four participating regulators (the only one with an explicit `may include` language and no OJ-imposed authentication-strength threshold). The CRA partial-coverage flag means that an MFA deployment at the CRA product-side exceeds the CRA requirement on the authentication dimension; a single-factor deployment at a CRA-regulated product is OJ-compliant under CRA but may not satisfy NIS 2 or DORA when those regs apply on the same party. For an organisation across multiple regulators, the CRA leg documents the product-side authentication baseline that the manufacturer operates at; an authentication-mechanism choice that exceeds the CRA permissive baseline (e.g. selecting MFA where the risk assessment warrants) is documented in Annex VII and feeds the downstream controller / NIS 2 essential-entity / financial-entity authentication architecture. The downstream AEV notification cascade (Art. 14) is part of D-04.3, not D-03.2. (Copied from the HSO Considerations block of `### D-03.2.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=1 -->