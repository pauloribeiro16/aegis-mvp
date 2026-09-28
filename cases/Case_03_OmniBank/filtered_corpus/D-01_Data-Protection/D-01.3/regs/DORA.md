# D-01.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SG-DORA-002 | Strong authentication + cryptographic-key protection + encryption (3-control AND) with classification-driven cipher strength | Financial entity; Art. 9(4)(d) 3-control AND; ICT-system-level; entity-level HSM/split-knowledge/classification-tiered rotation; `high standards` anchor |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | continuous + classification-driven re-tuning | cryptographic keys of ICT-supported financial-entity data | national CA + ESAs | Art. 9(4)(d) strong auth + key protection + encryption (3-control AND) |

## Sub-SO (DORA)

#### D-01.3.3 — Sub-SO for DORA

```yaml
id: SG-D-01.3.DORA
subdomain: D-01.3
applies_to: [DORA]
inherits_from: SG-DORA-002
source_SR: SR-DORA-002, SR-DORA-003
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Strong authentication mechanisms, cryptographic-key protection
measures, and data encryption are implemented through coordinated policies
and protocols, with the cryptographic-key protection leg tied to approved
data classification and ICT risk assessment processes (Art. 9(4)(d)
3-control AND of strong authentication + key protection + encryption).

- The `approved data classification` qualifier is binding: data-classification
  processes must be approved by the financial entity's governance layer
  (Art. 5(2) management body oversight), and ICT risk assessment processes
  must satisfy Art. 6 chapeau.
- The classification and assessment drive the encryption level — tiered
  classification is reflected in tiered cryptographic strength (EBA
  Guidelines on ICT and security risk management §149).
**CSF anchors (from `SR-DORA-002` + `SR-DORA-003` v0.3 security_rationale):**
PR.AA-03, PR.AA-04, PR.DS-01, GV.RM-04.
*(`SR-DORA-002` covers the strong-authentication leg anchored to PR.AA-03
+ PR.AA-04 (identity assertions protected); `SR-DORA-003` covers the
classification-driven cryptographic-key protection leg anchored to PR.DS-01
+ GV.RM-04 (HSM-anchored custodianship + rotation cadence + strategic
risk-management direction). The two SRs together operationalise the 3-control
AND of Art. 9(4)(d).)*

---


## Security Requirements (DORA)

#### 1.3.3 — Financial-entity cryptographic-key protection with classification-driven tiering

```yaml
- req_id: 1.3.3
  volere_section: 15
  volere_subtype: access

  title: "Financial-entity cryptographic keys protected with classification-driven cipher strength and depth"

  derives_from:
    hso_sub_so: SG-D-01.3.DORA
    per_reg_so: SG-DORA-002
    source_sr: SR-DORA-002, SR-DORA-003
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.3.md
    objective_ref_section: "### D-01.3.3"

  description: |
    The product shall implement strong authentication mechanisms, cryptographic-key protection measures, and data encryption as a coordinated 3-control AND tied to approved data classification and ICT risk assessment processes (DORA Art. 9(4)(d)), with the key-protection leg operationalised through HSM-anchored custodianship, split-knowledge ceremonies, classification-driven rotation cadence scaled to data criticality, and quorum-based recovery procedures (DORA Art. 9(2) + Art. 9(4)(d) + EBA Guidelines on ICT and security risk management §149).

  fit_criterion: |
    Cryptographic keys protecting financial-entity ICT-supported data are stored in FIPS 140-3 / Common Criteria EAL4+ certified HSMs (or RTS-conformant equivalent under DORA Art. 15 where applicable); split-knowledge ceremonies with quorum-based recovery are documented and tested (per EBA Guidelines §149 depth guidance); rotation cadence is classified-tiered (high-criticality data: ≤12 months; medium-criticality: ≤24 months; low-criticality: ≤36 months — scaled per EBA Guidelines §149 criticality matrix); the `approved data classification` qualifier is met (data-classification processes approved by management body per Art. 5(2); ICT risk assessment satisfies Art. 6 chapeau); verified by HSM-configuration audit + rotation-cadence review + classification-driven cipher-strength overlay + national-CA + ESAs inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.AA-03, PR.AA-04]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**DORA article (verbatim — SR-DORA-002 + SR-DORA-003, Art. 9(4)(d)):**
> Art. 9(4)(d) … strong authentication mechanisms, based on relevant standards and dedicated control systems, and protection measures of cryptographic keys whereby data is encrypted based on results of approved data classification and ICT risk assessment processes.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.3: GDPR↔DORA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/DORA.md body

**Considerations.**

- The DORA classification-driven entity-level architecture operationalises
  HSM-anchored custodianship + split-knowledge ceremonies + rotation cadence
  scaled to data criticality + quorum-based key-recovery procedures that sit
  above the CRA product-side functional-RBAC floor.

### from regs/DORA.md body

- The `high standards` anchor is qualitatively softer than CRA's `state of
  the art`; the OJ text defers the measurement criterion to EBA / ESMA /
  EIOPA RTS under Art. 15.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Y (DORA financial entity is GDPR controller — typical); DORA↔CRA = Y (DORA financial entity uses CRA product); HL engages on overlap

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA classification-driven entity-level architecture is the deepest
    layer of the three (HSM + split-knowledge + quorum-recovery +
    classification-driven rotation). It operationalises the Art. 9(4)(d)
    3-control AND (strong auth + key protection + encryption) and sits
    above the CRA product-side functional-RBAC floor and the GDPR personal-
    data de-attribution test. The `high standards` anchor is qualitatively
    softer than CRA's `state of the art`; the OJ text defers the measurement
    criterion to EBA / ESMA / EIOPA RTS under Art. 15. For a DORA financial
    entity that is also a GDPR controller using CRA-regulated products,
    meeting the DORA depth layer discharges both the GDPR and CRA
    obligations on the same key material, with the controller's Art. 32
    documentation trail preserved separately. (Copied from the HSO
    Considerations block of `### D-01.3.3`; preserved here for self-
    contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=0 -->
