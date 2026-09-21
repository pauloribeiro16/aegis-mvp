# D-01.4 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-005 | Integrity of stored/transmitted/processed data + commands/programs/configuration protected against any manipulation not authorised by the user; corruption reported | Manufacturer; Annex I Part I (2)(f) integrity + (2)(l) logging; product-level; "personal or other"; technical integrity (universal-quantifier "any manipulation") |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | continuous + corruption-event reporting | data + commands + programs + configuration (universal quantifier) | user / administering party (corruption report) | Annex I Part I (2)(f) + (2)(l) |

## Sub-SO (CRA)

#### D-01.4.2 — Sub-SO for CRA

```yaml
id: SO-D-01.4.CRA
subdomain: D-01.4
applies_to: [CRA]
inherits_from: SO-CRA-005
source_SR: SR-CRA-005
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The integrity of stored, transmitted, or otherwise processed
data — personal or other — as well as the integrity of commands, programs,
and configuration, is protected against any manipulation or modification not
authorised by the user (Annex I Part I (2)(f) — the universal-quantifier
`any` makes the integrity protection unconditional); corruption is reported
to the user / administering party (Annex I Part I (2)(f) `report on
corruptions` + (2)(l) logging + monitoring).

- The reporting loop transforms silent-tampering failures into observable
  events.
**CSF anchors (from `SR-CRA-005` v0.3 security_rationale):**
PR.DS-01, PR.DS-10, PR.PS-04.
*(PR.DS-01 captures the data-at-rest integrity leg — cryptographic hashes,
MACs, and integrity-checked storage — ensuring that an adversary cannot
silently tamper with stored data without invalidating the integrity check
on the next read; PR.DS-10 anchors the data-in-use leg — runtime integrity
controls such as signed firmware, control-flow integrity, and
tamper-detection instrumentation; PR.PS-04 closes the detection loop by
ensuring that integrity events become observable log records suitable for
continuous monitoring, transforming silent tampering into observable events
rather than silent failures.)*

---


## Security Requirements (CRA)

#### 1.4.2 — Product-side technical integrity (universal-quantifier protection + corruption reporting)

```yaml
- req_id: 1.4.2
  volere_section: 15
  volere_subtype: integrity

  title: "Integrity of stored/transmitted/processed data + commands + programs + configuration protected against unauthorised manipulation"

  derives_from:
    hso_sub_so: SO-D-01.4.CRA
    per_reg_so: SO-CRA-005
    source_sr: SR-CRA-005
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md
    objective_ref_section: "### D-01.4.2"

  description: |
    The product shall protect the integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, against any manipulation or modification not authorised by the user, and shall report corruption to the user / administering party (CRA Annex I Part I (2)(f) universal-quantifier `any` makes the integrity protection unconditional + (2)(l) logging + monitoring + corruption reporting).

  fit_criterion: |
    All stored, transmitted, or processed data — together with commands, programs, and configuration — are protected by cryptographic hashes / MACs / signed firmware (PR.DS-01 + PR.DS-10) such that any unauthorised manipulation invalidates the integrity check on the next read; corruption events are surfaced as log records suitable for continuous monitoring (PR.PS-04) and reported to the user / administering party; verified by Annex I (2)(f) conformity-assessment evidence + Annex I (2)(l) corruption-report verification + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.DS-01, PR.DS-10, PR.PS-04]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim — SR-CRA-005, Annex I Part I (2)(f) + (l)):**
> Annex I Part I (2)(f) protect the integrity of stored, transmitted or otherwise processed data — personal or other — as well as the integrity of commands, programs and configuration against any manipulation or modification not authorised by the user. The manufacturer shall also report on corruptions.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.4: GDPR↔CRA CORRECTED from COMPLEMENTARY; CRA↔DORA CORRECTED from EQUAL; CRA↔AI_Act CORRECTED from COMPLEMENTARY)
```

### from regs/CRA.md body

**Considerations.**

- The CRA technical-integrity universal quantifier is the storage/protection
  leg — it covers data + commands + programs + configuration with the same
  protection level, which is a broader scope than GDPR's data-only accuracy
  + storage-integrity pair.

### from regs/CRA.md body

- The CRA product-side PR.DS-01 + PR.DS-10 + PR.PS-04 stack satisfies the
  storage/technical leg on a CRA-regulated product; the GDPR Art. 5(1)(d)
  accuracy + Art. 16 rectification workflow + Art. 19 cascade remains a
  controller obligation beyond CRA's technical-integration scope (when the
  CRA product stores personal data, the controller's accuracy workflow is
  layered above the CRA product-side integrity).


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # CRA↔GDPR = Y; CRA↔DORA = Y; CRA↔AI_Act = Y (edge-AI scenario — CRA-regulated product is also high-risk AI); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA universal-quantifier protection (`any manipulation or modification
    not authorised by the user`) is unconditional and broader than GDPR's
    data-only accuracy + storage-integrity pair — it covers commands +
    programs + configuration under the same protection level. The corruption
    reporting loop transforms silent-tampering failures into observable
    events. The CRA product-side PR.DS-01 + PR.DS-10 + PR.PS-04 stack
    satisfies the storage/technical leg on a CRA-regulated product; the
    GDPR Art. 5(1)(d) accuracy workflow + Art. 16 rectification + Art. 19
    cascade remains a controller obligation beyond CRA's technical-
    integration scope. (Copied from the HSO Considerations block of
    `### D-01.4.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=0 -->

