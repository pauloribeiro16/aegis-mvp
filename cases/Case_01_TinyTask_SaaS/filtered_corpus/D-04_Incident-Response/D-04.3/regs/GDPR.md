# D-04.3 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-010 | 72h SA notification | Personal-data breach; controller → DPA |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | personal data breach (Art. 4(12)) | personal data processing | supervisory authority (DPA) | Art. 33(1) | 72h `where feasible` |

## Sub-SO (GDPR)

#### D-04.3.1 — Sub-SO for GDPR

```yaml
id: SO-D-04.3.GDPR
subdomain: D-04.3
applies_to: [GDPR]
inherits_from: SO-GDPR-010
source_SR: SR-GDPR-016
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N  # if GDPR-only, high-level SO is redundant; sub-SO used directly
```

**Objective.** A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms (Art. 33(1)).

**CSF anchors (from `SR-GDPR-016` v0.3 security_rationale):**
RS.CO-02, RS.MA-04, RS.MA-03.

---


## Security Requirements (GDPR)

#### 4.3.1 — 72-hour DPA notification of personal-data breach with `where feasible` softening

```yaml
- req_id: 4.3.1
  volere_section: 15
  volere_subtype: audit

  title: "Personal-data breach notified to supervisory authority within 72 hours `where feasible` of becoming aware, with `unlikely risk` carve-out documented"

  derives_from:
    hso_sub_so: SO-4.3.GDPR
    per_reg_so: SO-GDPR-010
    source_sr: SR-GDPR-016
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.1"

  description: |
    The product shall notify the competent supervisory authority of a personal data breach without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms — at which point the Art. 33(3) Nature/Categories/Approximate-numbers/Consequences/Measures content template is filed (GDPR Art. 33(1) + Art. 33(3) + Art. 4(12) breach definition; the `where feasible` softening is GDPR-unique among the 4.3 regulators).

  fit_criterion: |
    A DPA-notification pipeline is operated with documented breach-classification discipline (controller designates whether breach is `unlikely to result in a risk`, `may result in a risk`, or `likely to result in a high risk` per EDPB Guidelines 9/2022 §3.5), 72h clock-start anchored at the 4.1 GDPR leg's `becoming aware` moment (parallel-clock binding principle); the Art. 33(3) content template (Nature / Categories of data subjects and records / Approximate numbers / Likely consequences / Measures taken or proposed / DPO contact) is filed via the MS-determined DPA entry-point channel within 72h `where feasible`, with phased notification allowed only when full information is not simultaneously available; the `unless unlikely to result in a risk` carve-out is documented as a GDPR-unique condition (does not survive multi-reg overlap with NIS 2 — NIS 2 `in any event` ceiling binds); for events that may result in a high risk to rights and freedoms, the Art. 34 data-subject communication obligation is cascaded separately (4.3 GDPR + 4.2 GDPR Unintelligibility carve-out is 4.2 territory, not 4.3); verified by DPA-notification logs review + 72h clock-anchor records inspection + Art. 33(3) content-template coverage audit + `where feasible` softening documentation + `unlikely risk` carve-out-justification records (where invoked) + DPA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.1 (notification requires prior `becoming aware` moment; 72h clock binds to 4.1 GDPR trigger anchor), 4.2.1 (notification content requires prior containment classification feeding Art. 33(3)(d) Measures-taken section)]

  nist_csf: [RS.CO-02, RS.MA-04, RS.MA-03]

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
> Art. 33(1) requires the controller, in the case of a personal data breach, to notify the personal data breach to the supervisory authority competent in accordance with Art. 55 without undue delay and, where feasible, not later than 72 hours after having become aware of it, unless the personal data breach is unlikely to result in a risk to the rights and freedoms of natural persons.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: CONDITIONAL (CRDA-deep, D-04.3 GDPR↔NIS2: SCOPE-DISJOINT baseline / CONTRADICTORY on overlap; GDPR↔CRA: SAME; GDPR↔DORA: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY; GDPR↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY)
```

### from regs/GDPR.md body

**Considerations.**

- The `where feasible` softening of the 72-hour clock is GDPR-unique among the D-04.3 regulators; the other D-04.3 regulations impose stricter `in any event` ceilings. When NIS 2 and GDPR both apply, the NIS 2 ceiling binds (no `where feasible` softening).


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔NIS2 = Conditional (Y controller-NSIE; when both apply, NIS 2 24h early warning binds and GDPR `where feasible` softening does not survive); GDPR↔CRA = SAME (controller ≠ fabricante by default; Conditional when integrated manufacturer-controller or product processes personal data); GDPR↔DORA = Conditional (Y DORA-FE processes personal data; when both apply, DORA `without undue delay` and parallel GDPR 72h run concurrently); GDPR↔AI_Act = Conditional (Y high-risk AI processes personal data; parallel clocks)

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR notification obligation is the personal-data-breach DPA notification; the operational substrate is a DPA-notification pipeline with 72h clock-start from `becoming aware`. The `where feasible` softening is GDPR-unique among the five 4.3 regulators; on multi-reg overlap with NIS 2, the NIS 2 `in any event` ceiling binds (no `where feasible` softening). The content template (Art. 33(3) Nature / Categories / Approximate numbers / Consequences / Measures) is GDPR-unique and must be filed with the DPA, even when the event is also NIS 2 / CRA / DORA / AI Act reportable. The `unlikely risk` carve-out (Art. 33(1) sentence 2) is a GDPR-unique condition for skip-licensing the notification; it survives on GDPR-only events but not on multi-reg overlap (NIS 2 doesn't have it; CRA doesn't have it; DORA doesn't have it; AI Act doesn't have it). The Art. 34 data-subject communication obligation for high-risk breaches is a separate downstream duty (Art. 34 + Art. 34(3)(a)/(b) unintelligibility carve-out is in 4.2 territory). (Copied from the HSO Considerations block of `### 4.3.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=4; core_cross_mentions=1 -->