# D-01.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-001 | CIA+A maintained across data states, including in transit (4×3 matrix) | Financial entity; Art. 9(2); ICT-system-level; `high standards`; OJ-explicit `in transit` dimension |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | continuous | data in transit of the financial entity | national CA + ESAs | Art. 9(2) |

## Sub-SO (DORA)

#### D-01.2.3 — Sub-SO for DORA

```yaml
id: SO-D-01.2.DORA
subdomain: D-01.2
applies_to: [DORA]
inherits_from: SO-DORA-001
source_SR: SR-DORA-001
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Data confidentiality, integrity, authenticity and
availability are maintained at high standards across all data states,
including in transit, through ICT security policies, procedures, protocols
and tools (Art. 9(2)).

**CSF anchors (from `SR-DORA-001` v0.3 security_rationale):**
PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.
*(The PR.DS-01 / PR.DS-10 / ID.AM-05 anchors are inherited from the 4×3
matrix context; D-01.2 is the in-transit cell, which is anchored
specifically by PR.DS-02.)*

---


## Security Requirements (DORA)

#### 1.2.3 — Financial-entity ICT data in transit

```yaml
- req_id: 1.2.3
  volere_section: 15
  volere_subtype: integrity

  title: "ICT-supported data of financial entity maintained at high standards of CIA in transit"

  derives_from:
    hso_sub_so: SO-D-01.2.DORA
    per_reg_so: SO-DORA-001
    source_sr: SR-DORA-001
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.2.md
    objective_ref_section: "### D-01.2.3"

  description: |
    The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across all data states, including in transit, through ICT security policies, procedures, protocols and tools (DORA Art. 9(2)).

  fit_criterion: |
    High-standards in-transit cryptography (TLS 1.3 or stronger, with cipher suites conforming to EBA/ESMA/EIOPA RTS under DORA Art. 15 where applicable) is applied across all in-transit channels of the financial entity's ICT landscape; mutual-authentication (mTLS) architecture + zone-trust + peer-peer authentication between internal services is documented; network-segmentation policy is documented; verified by configuration audit + zone-trust architecture review + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key/Certificate Management — pending generation)", "3.x (Mutual Authentication — pending generation)"]

  nist_csf: [PR.DS-02]

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

**DORA article (verbatim — SR-DORA-001, Art. 9(2)):**
> Art. 9(2) … high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.2: GDPR↔DORA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/DORA.md body

**Considerations.**

- DORA is OJ-explicit on the `in transit` dimension; the entity-level
  transport-security governance (zone trust, mTLS architecture,
  peer-peer authentication between internal services) is the DORA-specific
  overlay above the CRA product-side baseline.

### from regs/DORA.md body

- For a DORA financial entity that is also a GDPR controller, a single
  mutually-authenticated encrypted-channel architecture + documented
  network-segmentation policy satisfies both (CRDA-deep GDPR↔DORA pair
  reasoning).


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # DORA↔GDPR = Y (DORA FE transmits personal data — typical); DORA↔CRA = Y (FE uses CRA product); HL engages on overlap (disjoint in baseline as manufacturer ≠ financial entity)

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    DORA is OJ-explicit on the `in transit` dimension; the entity-level
    transport-security governance (zone trust, mTLS architecture, peer-peer
    authentication between internal services) is the DORA-specific overlay above
    the CRA product-side baseline. For a DORA financial entity that is also a
    GDPR controller, a single mutually-authenticated encrypted-channel
    architecture + documented network-segmentation policy satisfies both
    (CRDA-deep GDPR↔DORA pair reasoning). (Copied from the HSO Considerations
    block of `### D-01.2.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=0 -->
