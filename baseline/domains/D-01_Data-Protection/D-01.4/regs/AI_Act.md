# D-01.4 — AI Act module

> Regulation-specific layer: applies when `AI_Act` is in scope
> (activation: `if AI_Act in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| AI Act | SG-AIACT-009 (partial) | High-risk AI systems resilient as possible regarding errors, faults, inconsistencies — technical redundancy (backup or fail-safe plans) | Provider; Art. 15(3); AI-system-level; resilience-not-integrity framing; AI-system-level property bundled with accuracy and robustness |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **AI Act** | continuous + lifecycle (Art. 15(1)) | AI-system resilience to errors/faults/inconsistencies | conformity-assessment body (ex ante) + MSA (ex post) + AI Office for GPAI | Art. 15(3) |

## Sub-SO (AI Act)

#### D-01.4.4 — Sub-SO for AI Act

```yaml
id: SG-D-01.4.AI_Act
subdomain: D-01.4
applies_to: [AI_Act]
inherits_from: SG-AIACT-009
source_SR: SR-AIACT-015
activation: if AI_Act in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** High-risk AI systems are as resilient as possible regarding
errors, faults, or inconsistencies that may occur within the system or the
environment (Art. 15(3)); the robustness of high-risk AI systems may be
achieved through technical redundancy solutions, which may include backup or
fail-safe plans.

- The 3-way OR of `errors, faults or inconsistencies` covers both
  AI-technical failures (e.g. inference-stage numerical instability) and
  environmental failures (e.g. sensor degradation); the 2-way OR for the
  means (`backup OR fail-safe plans`) signals that the OJ does not mandate
  a specific engineering pattern.
- Recital 66 confirms that resilience measures are to be proportionate to
  the intended purpose and the state of the art.
- The `as resilient as possible` standard is read as R3 state-of-the-art per
  `SR-AIACT-015` ambiguity_notes (the literal OJ sense).
**CSF anchors (from `SR-AIACT-015` v0.3 security_rationale):**
PR.IR-03, PR.IR-04, PR.DS-11.
**AI RMF anchors (from `SR-AIACT-015` — dashboard `00_VISUALISATIONS/AI_Act/AI_Act_Dashboard.html`, mechanical uniformization):**
MEASURE-2.6, MEASURE-2.7, MANAGE-2.3.
*(PR.IR-03 is the principal anchor — resilience mechanisms in normal and
adverse situations (failover, redundant inference paths, graceful
degradation); PR.IR-04 binds the capacity dimension (compute, storage,
network sized for the resilience target, not just steady-state workload);
PR.DS-11 operationalises the explicit `backup` means — backups created,
protected, maintained, and tested.)*

---


## Security Requirements (AI Act)

#### 1.4.4 — High-risk AI system resilience (errors, faults, inconsistencies)

```yaml
- req_id: 1.4.4
  volere_section: 15
  volere_subtype: integrity

  title: "High-risk AI system resilient to errors, faults, or inconsistencies via technical redundancy"

  derives_from:
    hso_sub_so: SG-D-01.4.AI_Act
    per_reg_so: SG-AIACT-009
    source_sr: SR-AIACT-015
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md
    objective_ref_section: "### D-01.4.4"

  description: |
    The product shall ensure high-risk AI systems are as resilient as possible regarding errors, faults, or inconsistencies that may occur within the system or the environment, with robustness achieved through technical redundancy solutions which may include backup or fail-safe plans (AI Act Art. 15(3)); the resilience target is read as R3 state-of-the-art per `SR-AIACT-015` ambiguity_notes and is proportionate to the intended purpose per Recital 66.

  fit_criterion: |
    The high-risk AI system implements resilience mechanisms for errors, faults, and inconsistencies that occur within the system or its environment (PR.IR-03 — failover, redundant inference paths, graceful degradation); capacity is sized for the resilience target, not just steady-state workload (PR.IR-04); where the OJ-permitted `backup` means is selected, backups are created, protected, maintained, and tested (PR.DS-11); where the `fail-safe plan` means is selected, the fail-safe behaviour is documented and tested; the resilience target is proportionate to the intended purpose per Recital 66; verified by resilience-mechanism audit (failover test, redundant-inference-path exercise) + backup-testing evidence + fail-safe plan documentation + conformity-assessment body + MSA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []

  nist_csf: [PR.IR-03, PR.IR-04, PR.DS-11]
  nist_airmf: [MEASURE-2.6, MEASURE-2.7, MANAGE-2.3]

  applicable_if:
    regs: [AI_Act]
  satisfaction:
    controls: []
    nodes: []

```


---


## Verbatim regulatory basis (AI Act)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**AI Act article (verbatim — SR-AIACT-015, Art. 15(3)):**
> Art. 15(3) High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment … The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans.

**AI Act article (verbatim — SR-AIACT-015, Art. 15(3)):**
> Art. 15(3) … as resilient as possible regarding errors, faults or inconsistencies … technical redundancy solutions, which may include backup or fail-safe plans.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/AI_Act.md body — field `verified_relationship`

```yaml
verified_relationship: SAME (CRDA-deep, D-01.4: GDPR↔AI_Act CORRECTED from DIFFERENT PERSPECTIVE; CRA↔AI_Act CORRECTED from COMPLEMENTARY; DORA↔AI_Act CORRECTED from DIFFERENT PERSPECTIVE)
```

### from regs/AI_Act.md body

**Considerations.**

- The AI Act's resilience framing is different from data-integrity in the
  conventional sense — it targets AI-system resilience to errors/faults/
  inconsistencies (a system-level property bundled with accuracy and
  robustness per Art. 15(1)) rather than the data-storage integrity
  property that GDPR / CRA / DORA govern.

### from regs/AI_Act.md body

- The CRA-AI Act deemed-compliance bridge (CRA Art. 12) provides a one-way
  shortcut for high-risk AI satisfying CRA Annex I; where the high-risk AI
  system is a CRA-regulated product (edge-AI device scenario), the CRA
  product-side technical integrity leg is the storage substrate, and the AI
  Act resilience leg is the AI-system leg above it.


### from regs/AI_Act.md body — field `scope_overlap`

```yaml
    scope_overlap: Y   # AI_Act↔GDPR = Y (high-risk AI processes personal data — typical); AI_Act↔CRA = Y (edge-AI scenario); AI_Act↔DORA = Y (DORA financial entity deploys high-risk AI); HL engages on overlap

```

### from regs/AI_Act.md body — field `considerations`

```yaml
  considerations: |
    The AI Act's resilience framing is different from data-integrity in the
    conventional sense — it targets AI-system resilience to errors/faults/
    inconsistencies (a system-level property bundled with accuracy and
    robustness per Art. 15(1)) rather than the data-storage integrity
    property that GDPR / CRA / DORA govern. The 3-way OR of `errors, faults
    or inconsistencies` covers both AI-technical failures (e.g. inference-
    stage numerical instability) and environmental failures (e.g. sensor
    degradation); the 2-way OR for the means (`backup OR fail-safe plans`)
    signals that the OJ does not mandate a specific engineering pattern.
    The `as resilient as possible` standard is read as R3 state-of-the-art
    per `SR-AIACT-015` ambiguity_notes (the literal OJ sense). The CRA-AI
    Act deemed-compliance bridge (CRA Art. 12) provides a one-way shortcut
    for high-risk AI satisfying CRA Annex I; where the high-risk AI system
    is a CRA-regulated product (edge-AI device scenario), the CRA product-
    side technical integrity leg is the storage substrate, and the AI Act
    resilience leg is the AI-system leg above it. (Copied from the HSO
    Considerations block of `### D-01.4.4`; preserved here for self-
    contained traceability.)
```

<!-- aegis:purity: own_reg=AI_Act; demoted=5; core_cross_mentions=0 -->
