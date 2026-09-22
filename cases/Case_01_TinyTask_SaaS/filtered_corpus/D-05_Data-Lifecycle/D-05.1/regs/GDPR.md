# D-05.1 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-015 + SO-GDPR-016 (cross-ref) | Personal data limited to adequate/relevant/necessary + Art. 6(4) compatibility test + Art. 6(1)(a)–(f) lawfulness bases + Art. 9(1) prohibition with Art. 9(2) exceptions | Personal data; controller-driven; Art. 5(1)(c) + Art. 6(4) + Art. 5(1)(a)/(b) + Art. 6(1) + Art. 9(1) prohibition; ID.AM-08 + ID.AM-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | personal data (data-subject-identifiable) | collection or further processing of personal data (Art. 5(1)(c)); any change of purpose triggers Art. 6(4) compatibility | `adequate, relevant and limited to what is necessary` (Art. 5(1)(c)) + Art. 6(4) compatibility test (5 factors (a)–(e)) + Art. 5(1)(c) minimisation register | collection + further processing + change of purpose | supervisory authority (DPA) — Art. 5(2) accountability + Art. 35 DPIA + Art. 30 RoPA | Art. 5(1)(c) + Art. 6(4) + Art. 5(1)(a)/(b) + Art. 6(1) + Art. 9(1) prohibition + Art. 9(2) exceptions + Art. 25(1)/(2) by-design/by-default + Art. 35(7) DPIA content |

## Sub-SO (GDPR)

#### D-05.1.1 — Sub-SO for GDPR

```yaml
id: SO-D-05.1.GDPR
subdomain: D-05.1
applies_to: [GDPR]
inherits_from: SO-GDPR-015 + SO-GDPR-016 (cross-ref)
source_SR: SR-GDPR-025, SR-GDPR-026
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing is compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing.

**CSF anchors (from `SR-GDPR-025` + `SR-GDPR-026` v0.3
security_rationale):**
ID.AM-08, ID.AM-03, GV.OC-03, GV.PO-01.
*(`SR-GDPR-025` covers the Art. 5(1)(c) `adequate, relevant, limited to
what is necessary` + Art. 6(4) 5-factor compatibility test anchored to
ID.AM-08 (data managed consistent with risk strategy — the
per-purpose collection limits and retention schedules) + ID.AM-03
(inventories of data and corresponding metadata for designated data
types — the data-inventory foundation without which the necessity
test cannot be applied and the Art. 6(4) compatibility assessment
cannot be run on a change of purpose). `SR-GDPR-026` covers the
Art. 5(1)(a) lawfulness/fairness/transparency + Art. 6(1) lawfulness
bases anchored to GV.OC-03 (legal/regulatory/contractual requirements
understood and managed — including privacy and civil-liberties
obligations) + GV.PO-01 (organisational cybersecurity policy
established, communicated, enforced — the lawfulness-basis policy
substrate). The four subcategories together operationalise the
controller-side personal-data-minimisation architecture: ID.AM-03
supplies the data-inventory knowledge property; ID.AM-08 supplies the
data-management discipline property; GV.OC-03 supplies the
legal/regulatory understanding substrate; GV.PO-01 supplies the
policy-establishment substrate. Art. 25(1)/(2) by-design and
by-default closes the upstream policy loop — minimisation is integrated
at the time of means-determination (Art. 25(1)) and at the time of
processing itself (Art. 25(2)); Art. 35(7) DPIA content items close
the downstream risk-assessment loop; Art. 30(1)(f) RoPA retention
time-limits close the documentation loop. Art. 5(2) accountability
provides the supervisory-authority evidence path.)*

---


## Security Requirements (GDPR)

#### 5.1.1 — Personal-data minimisation per Art. 5(1)(c) with Art. 6(4) compatibility on change of purpose and Art. 9(1) special-category prohibition

```yaml
- req_id: 5.1.1
  volere_section: 15
  volere_subtype: privacy

  title: "Personal data limited to what is adequate, relevant, and necessary for the processing purpose, with Art. 6(4) compatibility assessment on change of purpose and Art. 9(1) special-category prohibition honoured"

  derives_from:
    hso_sub_so: SO-D-05.1.GDPR
    per_reg_so: SO-GDPR-015 + SO-GDPR-016 (cross-ref)
    source_sr: SR-GDPR-025, SR-GDPR-026
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.1.md
    objective_ref_section: "### D-05.1.1"

  description: |
    The product shall limit personal data collected and processed to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing shall be compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing.

  fit_criterion: |
    A controller-side personal-data-minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory with declared purpose, lawful basis, and envisaged erasure time per data category) + ID.AM-08 data managed consistent with the controller's risk strategy (per-purpose collection limits + retention schedules); the Art. 5(1)(c) `adequate, relevant, limited to what is necessary` test is applied to every data-collection surface and documented in a necessity assessment per data class; an Art. 6(4) 5-factor compatibility assessment (a) purpose link, (b) context of collection, (c) nature of personal data, (d) possible consequences for the data subject, (e) existence of appropriate safeguards is performed and documented on every change of purpose and is NOT absorbed by the CRA-side design-time minimisation when both apply on the same integrated-stack manufacturer-controller; Art. 9(1) special-category prohibition is enforced absent an Art. 9(2) basis (including the substantial public interest Art. 9(2)(g) where applicable) OR the AI Act Art. 10(5) 6-cumulative-condition gateway (when high-risk AI bias correction applies); Art. 25(1) by-design minimisation integrates the necessity test at the time of means-determination; Art. 25(2) by-default minimisation ensures only data necessary for each specific purpose are processed by default; Art. 35(7) DPIA content items are present for any high-risk processing; Art. 30(1)(f) RoPA envisages-time-limits-for-erasure are documented per category; Art. 5(2) accountability evidence is inspection-ready; verified by data-inventory audit + per-class necessity-assessment review + Art. 6(4) compatibility-assessment records inspection + Art. 9(1) prohibition-enforcement audit + Art. 25 by-design and by-default documentation review + DPIA records inspection (for high-risk processing) + Art. 30(1)(f) RoPA time-limits review + DPA inspection-ready evidence pack on re... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: [5.1.2 (when CRA-classified product processes personal data at runtime — verbatim-language match binds both regimes on the same dataset with the stricter operational interpretation; the Art. 6(4) compatibility test remains the residual GDPR-only requirement), 5.1.3 (when high-risk AI provider processes special-category personal data for bias correction — Art. 10(5) 6-cumulative-condition gateway operates as a permission; outside that window, Art. 9(1) prohibition binds)]

  nist_csf: [ID.AM-08, ID.AM-03]
  nist_pf: [CT.PO-P4, CT.DP-P4, ID.RA-P3]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 5(1)(c) + Art. 6(4)):**
> "Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')." — Art. 5(1)(c) GDPR
>
> "Where the processing for a purpose other than that for which the personal data have been collected is not based on the data subject's consent … the controller shall, in order to ascertain whether processing for another purpose is compatible with the purpose for which the personal data are initially collected, take into account, inter alia: (a) any link between the purposes … (b) the context of collection … (c) the nature of the personal data … (d) the possible consequences … (e) the existence of appropriate safeguards." — Art. 6(4) GDPR

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-05.1: GDPR↔CRA = COMPLEMENTARY (SAME — verbatim "adequate, relevant and limited to what is necessary" language; controller-driven purpose vs manufacturer-design intended purpose); GDPR↔AI_Act = CORRECTED from CONTRADICTORY to SCOPE-DISJOINT with Art. 10(5) carve-out)
```

### from regs/GDPR.md body

**Considerations.**

- Verbatim operative-language match with CRA Annex I Part I (2)(g) — when a CRA-compliant product processes personal data at runtime, the same minimisation test applies on the same dataset and the stricter operational interpretation binds.

### from regs/GDPR.md body

- The GDPR Art. 6(4) compatibility test on change of purpose is the residual GDPR-only requirement not absorbed by CRA-side design-time minimisation; for an integrated manufacturer-controller, the Art. 6(4) assessment is documented separately from the CRA Annex I Part I (2)(g) design-time record.

### from regs/GDPR.md body

- The AI Act Art. 10(5) special-category bias-correction gateway is an additional narrow permission for high-risk AI providers (all 6 cumulative conditions (a)–(f) required); outside that window, GDPR Art. 9(1) prohibition binds and the AI Act gateway does not extend the controller-side processing basis.


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔CRA = Conditional (Y when same data stream flows through CRA-classified product at runtime and is personal data; both minimisations apply with stricter binding; GDPR retains Art. 6(4) compatibility-test residual); GDPR↔AI_Act = Conditional (Y in the narrow Art. 10(5) window — high-risk AI provider training a system with bias-detection needs that cannot be met by non-special-category data, all 6 conditions (a)–(f) satisfied; outside that window, AI Act does not trigger special-category processing and the pair is scope-disjoint in baseline); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR data-minimisation obligation is the controller-side personal-data limitation anchored on Art. 5(1)(c) `adequate, relevant, limited to what is necessary` plus the Art. 6(4) 5-factor compatibility test on change of purpose plus the Art. 9(1) special-category prohibition plus the Art. 25(1)/(2) by-design and by-default integration. The verbatim operative-language match with CRA Annex I Part I (2)(g) binds both regimes on the same dataset when a CRA-compliant product processes personal data at runtime — the same minimisation test applies on the same operative phrase and the stricter operational interpretation binds. The GDPR Art. 6(4) compatibility test is the residual GDPR-only requirement not absorbed by CRA-side design-time minimisation; for an integrated manufacturer-controller, the Art. 6(4) assessment is documented separately from the CRA Annex I Part I (2)(g) design-time record. The AI Act Art. 10(5) special-category bias-correction gateway is an additional narrow permission for high-risk AI providers (all 6 cumulative conditions (a)–(f) required); outside that window, GDPR Art. 9(1) prohibition binds and the AI Act gateway does not extend the controller-side processing basis. (Copied from the HSO Considerations block of `### D-05.1.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=6; core_cross_mentions=2 -->
