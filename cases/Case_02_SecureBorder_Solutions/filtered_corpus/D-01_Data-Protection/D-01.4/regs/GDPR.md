# D-01.4 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-003 | Personal data accurate and, where necessary, kept up to date; every reasonable step to ensure erasure/rectification without delay | Controller/processor; Art. 5(1)(d) accuracy + Art. 16 rectification + Art. 5(1)(f) integrity; personal-data scope; semantic accuracy (workflow leg) + storage integrity |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + on Art. 16 request | personal-data semantic accuracy + storage integrity | supervisory authority (DPA) + data subjects (Art. 16) | Art. 5(1)(d) + Art. 5(1)(f) + Art. 16 + Art. 19 cascade |

## Sub-SO (GDPR)

#### D-01.4.1 — Sub-SO for GDPR

```yaml
id: SG-D-01.4.GDPR
subdomain: D-01.4
applies_to: [GDPR]
inherits_from: SG-GDPR-003
source_SR: SR-GDPR-005, SR-GDPR-006
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data are accurate and, where necessary, kept up to
date; every reasonable step is taken to ensure that personal data that are
inaccurate are erased or rectified without delay (Art. 5(1)(d) accuracy
principle), with the integrity property anchored to two further legs —
storage integrity (Art. 5(1)(f)) and the Art. 16 rectification cascade with
Art. 19 recipient-cascade duty.

**CSF anchors (from `SR-GDPR-005` + `SR-GDPR-006` v0.3 security_rationale):**
PR.DS-01, ID.AM-08, PR.DS-10.
**PF 1.1 anchors (from `SR-GDPR-005`, `SR-GDPR-006` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
CT.DM-P1, CT.DM-P3, CM.AW-P5.
*(`SR-GDPR-005` covers the Art. 5(1)(d) accuracy + Art. 5(1)(f) integrity leg
anchored to PR.DS-01 (storage-layer immutability, write-audit logging,
tamper-evidence) + ID.AM-08 (policy-level data-management discipline
governing data-quality monitoring, periodic refresh cadence, and the
feedback loop to the rectification workflow); `SR-GDPR-006` covers the Art.
16 + Art. 19 rectification workflow anchored to PR.DS-10 (controlled-write
integrity check on data in process) + ID.AM-08 (recipient register +
propagation procedure).)*

---


## Security Requirements (GDPR)

#### 1.4.1 — Personal-data accuracy and storage integrity

```yaml
- req_id: 1.4.1
  volere_section: 15
  volere_subtype: integrity

  title: "Personal data accurate, up to date, and protected against unauthorised modification"

  derives_from:
    hso_sub_so: SG-D-01.4.GDPR
    per_reg_so: SG-GDPR-003
    source_sr: SR-GDPR-005, SR-GDPR-006
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md
    objective_ref_section: "### D-01.4.1"

  description: |
    The product shall ensure personal data are accurate and, where necessary, kept up to date; every reasonable step shall be taken to ensure that inaccurate personal data are erased or rectified without delay, with the storage-integrity property anchored separately and the Art. 16 rectification cascade with Art. 19 recipient-cascade duty preserved (GDPR Art. 5(1)(d) accuracy + Art. 5(1)(f) integrity + Art. 16 + Art. 19 cascade).

  fit_criterion: |
    Personal-data storage uses integrity-checked storage with cryptographic hashes / MACs that detect tampering on reads (PR.DS-01); data-quality monitoring is in place with documented periodic-refresh cadence governing accuracy review (ID.AM-08); the Art. 16 rectification workflow is documented with recipient register and propagation procedure to each recipient to whom the personal data have been disclosed (ID.AM-08 + Art. 19 cascade); verified by automated integrity-check audit (hash/MAC validation) + manual rectification-cascade review + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-01, ID.AM-08]
  nist_pf: [CT.DM-P1, CT.DM-P3]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim — SR-GDPR-005, Art. 5(1)(d) + Art. 5(1)(f)):**
> Art. 5(1)(d) personal data must be accurate and, where necessary, kept up to date; every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay.

**GDPR article (verbatim — SR-GDPR-005, Art. 5(1)(d)):**
> Art. 5(1)(d) personal data must be accurate and, where necessary, kept up to date … erased or rectified without delay.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.4: GDPR↔CRA CORRECTED from COMPLEMENTARY; GDPR↔DORA CORRECTED from COMPLEMENTARY; GDPR↔AI_Act CORRECTED from DIFFERENT PERSPECTIVE)
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # GDPR↔CRA = Y; GDPR↔DORA = Y; GDPR↔AI_Act = Y (high-risk AI processes personal data — typical); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    GDPR's anchor combines three legs — semantic accuracy (Art. 5(1)(d) —
    workflow leg, controller obligation beyond CRA's technical-integration
    scope), storage integrity (Art. 5(1)(f) — substrate leg, discharges via
    CRA's universal-quantifier protection when the storage is a CRA-regulated
    product), and the Art. 16 rectification cascade with Art. 19
    recipient-cascade duty. The accuracy workflow remains a controller
    obligation beyond CRA's technical-integration scope (when the CRA
    product stores personal data, the controller's accuracy workflow is
    layered above the CRA product-side integrity). The Art. 19 cascade is
    binding: the controller must communicate the rectification to each
    recipient to whom the personal data have been disclosed, unless this
    proves impossible or involves disproportionate effort. (Copied from the
    HSO Considerations block of `### D-01.4.1`; preserved here for self-
    contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=0 -->
