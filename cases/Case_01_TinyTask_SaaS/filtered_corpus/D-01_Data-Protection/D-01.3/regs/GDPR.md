# D-01.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-002 | Pseudonymisation/encryption with separate-storage test for the additional information (keys) + Art. 34(3)(a) unintelligibility carve-out | Controller/processor; Art. 4(5) de-attribution test + Art. 34(3)(a) breach-context carve-out; personal-data scope; risk-anchored `appropriate` |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + breach-context (Art. 34(3)(a) carve-out) | personal-data additional information (keys) | supervisory authority (DPA) | Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility |

## Sub-SO (GDPR)

#### D-01.3.1 — Sub-SO for GDPR

```yaml
id: SO-D-01.3.GDPR
subdomain: D-01.3
applies_to: [GDPR]
inherits_from: SO-GDPR-002
source_SR: SR-GDPR-003, SR-GDPR-004
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Where pseudonymisation or encryption is applied to personal
data, the additional information required to re-identify the data subject
(the cryptographic key, the mapping table, or the tokenisation seed) is
kept separately and is subject to appropriate technical and organisational
measures that prevent attribution (Art. 4(5) de-attribution test + Art.
34(3)(a) unintelligibility carve-out + Art. 32(1)(a) pseudonymisation/
encryption anchor).

**CSF anchors (from `SR-GDPR-003` + `SR-GDPR-004` v0.3 security_rationale):**
PR.DS-01, PR.IR-03.
*(`SR-GDPR-003` covers the Art. 32(1)(a) + Art. 4(5) pseudonymisation-separation
test anchored to PR.DS-01; `SR-GDPR-004` covers the Art. 34(3)(a)
unintelligibility carve-out anchored to PR.DS-01 + PR.IR-03 — the
resilience dimension of the carve-out presupposes that the key separation
remains effective on the day of the breach.)*

---


## Security Requirements (GDPR)

#### 1.3.1 — Personal-data key separation (Art. 4(5) de-attribution + Art. 34(3)(a) carve-out)

```yaml
- req_id: 1.3.1
  volere_section: 15
  volere_subtype: access

  title: "Personal-data key material kept separately to prevent re-attribution (de-attribution test)"

  derives_from:
    hso_sub_so: SO-D-01.3.GDPR
    per_reg_so: SO-GDPR-002
    source_sr: SR-GDPR-003, SR-GDPR-004
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.3.md
    objective_ref_section: "### D-01.3.1"

  description: |
    The product shall keep the additional information required to re-identify personal data (the cryptographic key, mapping table, or tokenisation seed) separately from the personal data and subject to appropriate technical and organisational measures that prevent attribution, so that unintelligibility is preserved on the day of a breach (GDPR Art. 4(5) de-attribution test + Art. 32(1)(a) pseudonymisation/encryption anchor + Art. 34(3)(a) unintelligibility carve-out).

  fit_criterion: |
    The cryptographic key, mapping table, or tokenisation seed protecting personal data is stored physically or logically separated from the personal data it protects; separation is governed by RBAC-distinct roles with distinct credentials under documented control (key-material custodian role ≠ data-platform operator role); the operational condition `those measures were applied to the personal data affected by the personal data breach` (Art. 34(3)(a) carve-out) is verifiable — the controller demonstrates that the unintelligibility measures covered the affected dataset, not merely that they were deployed somewhere in the system; verified by automated configuration audit of key-storage location + manual separation-of-roles review + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-01, PR.IR-03]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim — SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a)):**
> Art. 4(5) pseudonymisation … the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to appropriate technical and organisational measures. Art. 34(3)(a) … render the personal data unintelligible to any person who is not authorised to access it, such as encryption.

**GDPR article (verbatim — SR-GDPR-003 + SR-GDPR-004, Art. 4(5) + Art. 32(1)(a) + Art. 34(3)(a)):**
> Art. 4(5) … additional information is kept separately and is subject to appropriate technical and organisational measures. Art. 32(1)(a) pseudonymisation and encryption of personal data.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.3: GDPR↔CRA CORRECTED from COMPLEMENTARY; GDPR↔DORA CORRECTED from COMPLEMENTARY)
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR↔CRA = Y (CRA product stores personal data — typical); GDPR↔DORA = Y (DORA financial entity processes personal data — typical); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    GDPR's Art. 4(5) de-attribution test is the personal-data-side method that
    earns the Art. 34(3)(a) unintelligibility carve-out. The OJ-literal
    operational condition `those measures were applied to the personal data
    affected by the personal data breach` is binding — a controller whose
    encryption is applied only to part of the dataset does NOT satisfy the
    exception for a breach on the non-encrypted part (per SR-GDPR-004
    OJ-corrective note). The de-attribution test is the shallowest of the three
    depths (vs CRA functional-RBAC and DORA HSM/split-knowledge/quorum);
    meeting the DORA depth layer discharges the GDPR de-attribution test on
    the same key material when the DORA financial entity is also a GDPR
    controller. (Copied from the HSO Considerations block of `### D-01.3.1`;
    preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->

