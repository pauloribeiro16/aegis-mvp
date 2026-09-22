# D-04.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-009 | Personal-data breaches contained and mitigated via Art. 33(3)(d) measures (incl. rendering data unintelligible) + Art. 34(3)(a)/(b) unintelligibility carve-out | Personal data; post-detection containment, mitigation and remediation runbooks; ID.AM-08 + PR.IR-04 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | personal-data post-breach runbook (controller-side) | TOMs incl. unintelligibility rendering + subsequent measures eliminating high risk | `where appropriate` (Art. 33(3)(d)) + unintelligibility carve-out (Art. 34(3)(a)/(b)) | supervisory authority (Art. 33(3)(d) measures description); data subjects (Art. 34 unless carve-out applies) | Art. 33(3)(d) + Art. 34(3)(a)/(b) |

## Sub-SO (GDPR)

#### D-04.2.1 — Sub-SO for GDPR

```yaml
id: SO-D-04.2.GDPR
subdomain: D-04.2
applies_to: [GDPR]
inherits_from: SO-GDPR-009
source_SR: SR-GDPR-015
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk no longer materialises (Art. 34(3)(b)); the controller describes the measures taken or proposed in the Art. 33(3)(d) supervisory-authority notification.

**Considerations.**
- The GDPR containment-and-mitigation obligation is the personal-data post-breach runbook; the operational substrate is a TOMs catalogue that the controller applies when a personal-data breach is detected, with the unintelligibility rendering as the GDPR-unique carve-out that operates as a substitute for Art. 34 data-subject notification when applied. The `where appropriate` qualifier from Art. 33(3)(d) propagates and operationalises the TOMs catalogue depth: high-risk data categories (special categories, financial data, health data) trigger deeper and more aggressive containment than low-risk categories.
- The downstream notification cascade (Art. 33 supervisory-authority notification including the measures description) is part of D-04.3, not D-04.2.

**CSF anchors (from `SR-GDPR-015` v0.3 security_rationale):**
RS.MI-01, RS.MI-02, PR.DS-01.
**PF 1.1 anchors (from `SR-GDPR-015` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
PR.PO-P7, CT.DM-P10.
*(ID.AM-08 anchors the data-disposal-managed leg (the unintelligibility
rendering is the GDPR-unique expression of this anchor); PR.IR-04
anchors the adequate-resource-capacity leg (the TOMs catalogue
operationalises the resource allocation for containment); RC.RP-04
anchors the recovery-plans-executed leg for the post-event
containment-then-recovery sequence.)*

---


## Security Requirements (GDPR)

#### 4.2.1 — Personal-data post-breach TOMs with Art. 34(3)(a)/(b) unintelligibility carve-out

```yaml
- req_id: 4.2.1
  volere_section: 15
  volere_subtype: immunity

  title: "Personal-data breaches contained and mitigated through TOMs incl. unintelligibility rendering; Art. 33(3)(d) measures description in supervisory-authority notification"

  derives_from:
    hso_sub_so: SO-4.2.GDPR
    per_reg_so: SO-GDPR-009
    source_sr: SR-GDPR-015
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.2.md
    objective_ref_section: "### 4.2.1"

  description: |
    The product shall contain and mitigate personal-data breaches through appropriate technical and organisational measures (TOMs), including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk to data subjects' rights and freedoms no longer materialises (Art. 34(3)(b)), with the measures taken or proposed documented in the Art. 33(3)(d) supervisory-authority notification content; the `where appropriate` qualifier from Art. 33(3)(d) operationalises the TOMs depth with high-risk data categories (Art. 9 special categories, financial data, health data) triggering deeper and more aggressive containment than low-risk categories (GDPR Art. 33(3)(d) + Art. 34(3)(a)/(b) + Art. 32(1)(d)).

  fit_criterion: |
    A personal-data post-breach TOMs catalogue is maintained covering containment, mitigation and remediation measures, with the measures selected per the `where appropriate` Art. 33(3)(d) qualifier and depth scaled to data-category risk (Art. 9 special categories, financial data, health data trigger deeper measures); PR.DS-01 data-at-rest protected leg anchors the cryptographic foundation (with the operational condition that the protection measures were applied to the data actually affected by the breach, not merely to data generally); PR.IR-04 adequate-resource-capacity leg anchors the resource allocation for containment; ID.AM-08 data-managed-consistent-with-risk-strategy leg anchors the unintelligibility-rendering discipline; the Art. 34(3)(a) unintelligibility rendering — operationalised as encryption with sufficient key separation that the adversary cannot recover plaintext, with the cryptographic key unavailable to any party outside the controller's authorised set — is the GDPR-unique carve-out that operates as a substitute for Art. 34 data-subject notification when applied; the Art. 34(3)(b) `subsequent measures which ensure that the high risk no longer likely to materialise` leg is the harder threshold — the controller must demonstrate that mitigation actually neutralises the high risk, not merely that mitigation was attempted; the Art. 33(3)(d) measures description in the supervisory-authority notification (4.3 cross-ref) covers both taken and proposed measures; for multi-reg parties, the GDPR TOMs are documented as a section within the NIS 2 entity-level response plan or within the DORA BC arrangements, not as a separate runbook; the personal-data post-breach containment discipline operates at the controller post-event runbook layer only, with the boundary hand-off to entity-level `contain` phase (NIS 2 leg), product-design availability (CRA leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by TOMs catalogue audit + Art. 33(3)(d) measures description in notification records review + Art. 34(3)(a) encryption-with-key-separation evidence on the affected dataset (PR.DS-01 + PR.IR-04) + Art. 34(3)(b) mitigation-effect demonstration records (when Art. 34(3)(b) is invoked) + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.1 (containment triggered by prior `becoming aware` data-flow detection event), 4.2.2 (when controller is also NSIE — GDPR TOMs documented as section within NIS 2 plan), 4.2.4 (when DORA-controller — GDPR TOMs documented as section within DORA BC arrangements)]

  nist_csf: [RS.MI-01, RS.MI-02, PR.DS-01, ID.AM-08, PR.IR-04, RC.RP-04]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim):**
> Art. 33(3)(d) requires the controller's breach notification to the supervisory authority to describe the measures taken or proposed to be taken by the controller to address the personal data breach, including, where appropriate, measures to mitigate its possible adverse effects. Art. 34(3)(a) and (b) provide that subsequent measures rendering the personal data unintelligible or eliminating the high risk are valid exceptions to the data-subject notification under Art. 34(1).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-04.2: GDPR↔NIS2 = COMPLEMENTARY; GDPR↔CRA = DIFFERENT-PERSPECTIVE; GDPR↔DORA = COMPLEMENTARY)
```

### from regs/GDPR.md body

- The personal-data post-breach measure object is distinct from the NIS 2 entity-level lifecycle-phase actions, the CRA product-design availability choices, and the DORA BC arrangements — the controller-facing post-breach runbook is the containment layer, and the TOMs discipline operates at that layer only.

### from regs/GDPR.md body

- For a multi-reg party, the GDPR TOMs are documented as a section within the NIS 2 entity-level response plan (Doc 07 downstream implication) or within the DORA BC arrangements (Doc 07 downstream implication), not as a separate runbook.

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-NSIE; GDPR runbook inside NIS 2 plan); GDPR↔CRA = Conditional (Y integrated manufacturer-controller; disjoint in baseline: post-breach runbook ↔ product-design; CRA pre-event design + GDPR post-event reaction are temporally distinct); GDPR↔DORA = Conditional (Y DORA-controller; disjoint baseline: runbook ↔ BC arrangements; GDPR TOMs documented as section within DORA BC arrangements); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR containment-and-mitigation obligation is the personal-data post-breach runbook; the operational substrate is a TOMs catalogue that the controller applies when a personal-data breach is detected, with the unintelligibility rendering as the GDPR-unique carve-out that operates as a substitute for Art. 34 data-subject notification when applied. The `where appropriate` qualifier from Art. 33(3)(d) propagates and operationalises the TOMs catalogue depth. The Art. 34(3)(a) operational condition `those measures were applied to the personal data affected by the personal data breach` requires the controller to demonstrate that the encryption protected the actual affected dataset, not merely that encryption was deployed on the dataset generally (Berry §5.1 `affected by` qualifier is material). The Art. 34(3)(b) `no longer likely to materialise` threshold is hard — the controller must demonstrate that mitigation has materially reduced the risk below the Art. 34(1) threshold. The personal-data post-breach measure object is distinct from the NIS 2 entity-level lifecycle-phase actions, the CRA product-design availability choices, and the DORA BC arrangements — the controller-facing post-breach runbook is the containment layer, and the TOMs discipline operates at that layer only. The downstream notification cascade (Art. 33 supervisory-authority notification including the measures description) is part of 4.3, not 4.2. (Copied from the HSO Considerations block of `### 4.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=2 -->
