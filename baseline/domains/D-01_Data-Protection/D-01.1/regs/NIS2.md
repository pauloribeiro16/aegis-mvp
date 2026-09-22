# D-01.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-001 | Cryptography policies and procedures covering CIA of stored, transmitted, processed data | Essential/important entity; Art. 21(2)(h); NIS scope (broader than personal data); `where appropriate` hedge |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | continuous (Art. 21(1) appropriate-and-proportionate) | network and information systems | CSIRT or CA | Art. 21(2)(h) |

## Sub-SO (NIS 2)

#### D-01.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-01.1.NIS2
subdomain: D-01.1
applies_to: [NIS2]
inherits_from: SO-NIS2-001
source_SR: SR-NIS2-001
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities establish policies and
procedures regarding the use of cryptography and, where appropriate,
encryption, covering the confidentiality, integrity, and authenticity of
data stored, transmitted, and processed by network and information
systems (Art. 21(2)(h)).

**CSF anchors (from `SR-NIS2-001` v0.3 security_rationale):**
PR.DS-01, PR.DS-02, GV.RM-04.

---


## Security Requirements (NIS 2)

#### 1.1.2 — NIS scope data at rest

```yaml
- req_id: 1.1.2
  volere_section: 15
  volere_subtype: integrity

  title: "Cryptography policies cover CIA of stored NIS data"

  derives_from:
    hso_sub_so: SO-D-01.1.NIS2
    per_reg_so: SO-NIS2-001
    source_sr: SR-NIS2-001
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.1.md
    objective_ref_section: "### D-01.1.2"

  description: |
    The product shall establish policies and procedures regarding the use of cryptography and, where appropriate, encryption, covering the confidentiality, integrity and authenticity of data stored by network and information systems of essential and important entities (NIS 2 Art. 21(2)(h)).

  fit_criterion: |
    A documented cryptography policy exists and is maintained per Art. 21(2)(h); where the entity's risk assessment determines encryption is appropriate, AES-256 (or stronger) symmetric encryption is applied to NIS-scope data at rest; key custody is separated from data access; policy review cadence is documented; verified by policy inspection + automated configuration audit + CSIRT/CA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: ["1.3 (Key Management — pending generation)"]

  nist_csf: [PR.DS-01, PR.DS-02, GV.RM-04]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS 2 article (verbatim from SR-NIS2-001, Art. 21(2)(h)):**
> Article 21(2)(h) of Directive (EU) 2022/2555 (NIS2) requires essential and important entities to establish policies and procedures regarding the use of cryptography and, where appropriate, encryption.

**NIS 2 article (verbatim — SR-NIS2-001, Art. 21(2)(h)):**
> Article 21(2)(h) … establish policies and procedures regarding the use of cryptography and, where appropriate, encryption.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.1: GDPR↔NIS2 CORRECTED from COMPLEMENTARY; NIS2↔CRA CORRECTED from COMPLEMENTARY; NIS2↔DORA CORRECTED from EQUAL)
```

### from regs/NIS2.md body

**Considerations.**

- The `where appropriate` hedge on encryption admits a narrower scope than
  GDPR's `appropriate`, but where NIS 2 is narrower, GDPR is stricter
  (always applicable to personal data on the same datastore).

### from regs/NIS2.md body

- The NIS 2 cryptography-policy obligation is OJ-silent on the in-use
  dimension (DORA Art. 9(2) is OJ-explicit on the 3-state OR — see
  D-01.1.4); for the at-rest cell the two are the same obligation.


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # NIS2↔CRA = Y (NIS 2 essential entity uses CRA product — typical); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The `where appropriate` hedge on encryption admits a narrower scope than
    GDPR's `appropriate`, but where NIS 2 is narrower, GDPR is stricter
    (always applicable to personal data on the same datastore). The NIS 2
    cryptography-policy obligation is OJ-silent on the in-use dimension (DORA
    Art. 9(2) is OJ-explicit on the 3-state OR — see D-01.1.4); for the at-rest
    cell the two are the same obligation. (Copied from the HSO Considerations
    block of `### D-01.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=5; core_cross_mentions=0 -->