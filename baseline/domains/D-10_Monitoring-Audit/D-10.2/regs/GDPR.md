# D-10.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-031 | Compliance records (records of processing, consent records, processor contract records, breach notification records, DPIA records) are maintained in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections. | Entity-level compliance-record integrity + traceability; Art. 30(3) `in writing, including in electronic form` + Art. 5(2) `demonstrate compliance` (accountability) + Art. 31 SA cooperation; supervisor authority access on request. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | entity-level compliance records (RoPA, consent, processor contracts, breach notifications, DPIA) maintained in writing or electronic form with integrity + traceability + accountability demonstrability + SA cooperation on request | Art. 30(3) `The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request` + Art. 5(2) `The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1` + Art. 31 SA cooperation | entity (controller / processor) on personal-data processing activities | data subject + DPA — Art. 30(3) records `made available to the supervisory authority on request` + Art. 5(2) accountability demonstrability | Art. 30(1)/(2)/(3) record content + Art. 5(2) accountability + Art. 31 SA cooperation + Art. 24(1) chapeau responsibility |

## Sub-SO (GDPR)

#### D-10.2.1 — Sub-SO for GDPR

```yaml
id: SO-D-10.2.GDPR
subdomain: D-10.2
applies_to: [GDPR]
inherits_from: SO-GDPR-031
source_SR: SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_4
```

**Objective.** The controller and processor **maintain compliance records in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections** (Art. 30(3) + Art. 5(2) + Art. 31 GDPR), including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — made available to the supervisory authority on request (Art. 30(3)).

**CSF anchors (from `SR-GDPR-044` + `SR-GDPR-048` + `SR-GDPR-050` v0.3 security_rationale):**
GV.PO-02, GV.OV-03, ID.AM-03, PR.PS-04, DE.AE-03, RS.AN-07.
**PF 1.1 anchors (from `SR-GDPR-044`, `SR-GDPR-048`, `SR-GDPR-050` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
GV.MT-P3, GV.PO-P5, ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8, CT.DM-P9.
*(PR.DS-11 — Data are destroyed according to policy — anchors the GDPR Art. 30(3) `in writing, including in electronic form` records integrity mapped to NIST CSF 2.0 PR.DS-11; PR.PS-04 — Networks and environments are protected — anchors the electronic-form records with integrity controls per DomainAnalysis cross-validation; DE.CM-01 — Networks and network services are monitored to find potentially adverse events — anchors the Art. 30(3) traceability dimension + SA-access channel; GV.PO-02 — Information security policy is established, communicated, and maintained — anchors the Art. 5(2) accountability demonstrability burden. The four subcategories together enable the controller or processor to demonstrate ex post, against the Art. 5(2) accountability burden and the Art. 31 SA cooperation obligation, that the compliance records were maintained in writing/electronic form with integrity + traceability sufficient for the SA to inspect.)*

---


## Security Requirements (GDPR)

#### 10.2.1 — Entity-level compliance records in writing/electronic form with integrity + traceability + Art. 5(2) accountability + Art. 31 SA cooperation

```yaml
- req_id: 10.2.1
  volere_section: 15
  volere_subtype: audit

  title: "Controller and processor maintain compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections"

  derives_from:
    hso_sub_so: SO-10.2.GDPR
    per_reg_so: SO-GDPR-031
    source_sr: SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050
    hso_file: ../../HierarchicalSecurityObjectives/D-10_Monitoring-Audit/10.2.md
    objective_ref_section: "### 10.2.1"

  description: |
    The product shall maintain compliance records — including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections (per GDPR Art. 30(3) `The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request`), with the controller or processor responsible for and able to demonstrate compliance (per Art. 5(2) `The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1`) and cooperating with the supervisory authority (per Art. 31).

  fit_criterion: |
    Entity-level compliance records are maintained in writing or electronic form with integrity + traceability per Art. 30(3) + Art. 5(2) + Art. 31 (SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the GDPR Art. 30(3) `in writing, including in electronic form` records integrity mapped to NIST CSF 2.0 PR.DS-11) + PR.PS-04 (Networks and environments are protected — anchors the electronic-form records with integrity controls per DomainAnalysis cross-validation) + DE.CM-01 (Networks and network services are monitored to find potentially adverse events — anchors the Art. 30(3) traceability dimension + SA-access channel) + GV.PO-02 (Information security policy is established, communicated, and maintained — anchors the Art. 5(2) accountability demonstrability burden); the records content covers RoPA (records of processing activities per Art. 30(1)/(2)), consent records (Art. 7(1) + Recital 32 + EDPB Guidelines 05/2020 on consent), processor contract records (Art. 28(3)), breach notification records (Art. 33(1) + Art. 34(1)), and DPIA records (Art. 35(1)–(7)); the records are maintained in writing or in electronic form with integrity controls (immutability / write-once / cryptographic hash / version control) + traceability controls (audit trail of record access + modification + retention + destruction); the Art. 5(2) accountability demonstrability burden is operationalised as: the controller or processor can demonstrate ex post, against the supervisory authority inspection, that the compliance records were maintained in writing/electronic form with integrity + traceability sufficient for the SA to inspect; the Art. 31 SA cooperation obligation is operationalised as: records are made available to the supervisory authority on request (per Art. 30(3) `made available to the supervisory authority on request`); the recipient is the **data subject + DPA (supervisory authority)** on the Art. 30(3) compliance records + Art. 5(2) accountability evidence + Art. 31 SA cooperation; verified by DPA audit pack (RoPA evidence + consent records evidence + processor contract records + breach notification records + DPIA records + Art. 5(2) accountability demonstrability evidence + Art. 31 SA cooperation evidence) + automated records-integrity test (immutability / write-once / cryptographic hash chain over record set) + automated records-traceability test (audit trail of record access + modification + retention + destruction) + manual DPA-access simulation (records made available to SA on request within the Art. 30(3) window).

  priority: MUST
  verification_method: TEST
  dependencies: [10.2.2 (N (typically) — substantively scope-disjoint by record-type distinctness; GDPR compliance records vs. CRA product documentation; no joint condition on this pair alone; engages only via DORA or AI Act third-regulator joint-condition), 10.2.3 (Conditional — Y when DORA financial entity is a controller; GDPR compliance records + DORA CIA+A information security policy stack on different record types: compliance vs. operational CIA+A policy; conditional discharge when the DORA-led stack integrates the Art. 30(3) records as a sub-component), 10.2.4 (Conditional — Y when high-risk AI system processes personal data and logs contain personal data; **floor-within-ceiling pattern** — AI Act Art. 19(1) ≥6-month hard floor WITHIN GDPR Art. 5(1)(e) `as long as necessary` envelope; the two regimes operate on different time scales; the floor-within-ceiling is OJ-consistent, NOT a tension; Phase 1 entities must implement AI Act Art. 19(1) ≥6-month retention as a hard minimum + extend to GDPR `necessary` envelope when the AI system `intended purpose` requires more than 6 months or when a DPA request requires longer retention)]

  nist_csf: [PR.DS-11, PR.PS-04, DE.CM-01, GV.PO-02]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 5(2) + Art. 30(3)):**
> "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 ('accountability')." — Art. 5(2) GDPR
> "The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request." — Art. 30(3) GDPR

**GDPR article (verbatim, Art. 5(2) + Art. 30(3)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-10.2: GDPR↔CRA = COMPLEMENTARY (SAME — substantively scope-disjoint by record-type distinctness; N (typically) — different record types, different triggers); GDPR↔DORA = COMPLEMENTARY (SAME — Conditional-Y when DORA financial entity is controller; GDPR compliance records + DORA CIA+A policy stack); GDPR↔AI_Act = COMPLEMENTARY (SAME — Conditional-Y when high-risk AI processes personal data; **floor-within-ceiling pattern** — AI Act Art. 19(1) 6-month floor WITHIN GDPR Art. 5(1)(e) ceiling envelope — OJ-consistent reconciliation, NOT a tension))
```

### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔CRA = N (typically) — substantively scope-disjoint by record-type distinctness; GDPR↔DORA = Conditional (Y when DORA financial entity is a controller); GDPR↔AI_Act = Conditional (Y when high-risk AI processes personal data and logs contain personal data; **floor-within-ceiling pattern** — OJ-consistent reconciliation, NOT a tension); HL engages when the GDPR sub-SO activates AND ≥1 other sub-SO activates on Y or Conditional-Y overlap.

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR audit-logging obligation at 10.2 is the **entity-level compliance records** with integrity + traceability + accountability + SA cooperation per Art. 30(3) + Art. 5(2) + Art. 31 (per SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050). Art. 30(3) `The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request` — the `in writing, including in electronic form` 2-way OR + the `made available to the supervisory authority on request` SA-access channel. Art. 5(2) `The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1` — the accountability demonstrability burden. Art. 31 SA cooperation — the controller, processor, and their representatives shall cooperate with the supervisory authority. The records content covers RoPA, consent records, processor contract records, breach notification records, and DPIA records. The recipient is the **data subject + DPA** on the Art. 30(3) compliance records + Art. 5(2) accountability evidence + Art. 31 SA cooperation. **Floor-within-ceiling pattern (NOT a tension) on GDPR ↔ AI_Act**: AI Act Art. 19(1) `at least six months` hard floor is a subset of GDPR Art. 5(1)(e) `as long as necessary` envelope; the two regimes operate on different time scales (one is a floor, one is a ceiling); the OJ does NOT resolve this as a conflict because the structural scope-asymmetry prevents OJ-level conflict; Phase 1 entities with high-risk AI systems processing personal data must implement AI Act Art. 19(1) ≥6-month retention as a hard minimum + extend to GDPR `necessary` envelope when the AI system `intended purpose` requires more than 6 months or when a DPA request requires longer retention. **Substantively scope-disjoint GDPR ↔ CRA pair** (N (typically) — compliance records vs. product documentation; different record types at different triggers; no overlap on a single event at a single party; HL does NOT engage on GDPR ↔ CRA pair alone). **For DORA financial entities that are also controllers**, the DORA Art. 9(4)(a) information security policy with CIA+A rules governs the entity-level audit-records stack under the Art. 4 proportionality factors, and the GDPR compliance records are maintained as a sub-component within the DORA-led CIA+A stack.
```

<!-- aegis:purity: own_reg=GDPR; demoted=3; core_cross_mentions=1 -->
