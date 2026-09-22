# D-05.2 — GDPR module

> Regulation-specific layer: applies when `GDPR` is in scope
> (activation: `if GDPR in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-017 | Personal data kept no longer than necessary; longer only where lawful and Art. 89(1) safeguards in place (Art. 5(1)(e) storage limitation + Art. 30(1)(f) RoPA retention time-limits) | Personal data; storage limitation; controller/processor; Art. 5(1)(e) + Art. 30(1)(f) + Art. 89(1); ID.AM-08 + ID.AM-03 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | personal data (data-subject-identifiable) | ceiling (upper limit, qualitative) | continued storage of personal data beyond processing-purpose end | `no longer than is necessary for the purposes for which the personal data are processed` (Art. 5(1)(e) VAG) + Art. 30(1)(f) `envisaged time limits for erasure` + Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for the public-interest/scientific-research/statistical carve-out | collection → purpose end → erasure; Art. 89(1) carve-out for archiving/research/statistical | supervisory authority (DPA) — Art. 5(2) accountability + Art. 30(1) RoPA + Art. 17 erasure | Art. 5(1)(e) + Art. 30(1)(f) + Art. 89(1) + Art. 17 + Art. 19 cascade |

## Sub-SO (GDPR)

#### D-05.2.1 — Sub-SO for GDPR

```yaml
id: SG-D-05.2.GDPR
subdomain: D-05.2
applies_to: [GDPR]
inherits_from: SG-GDPR-017
source_SR: SR-GDPR-029
activation: if GDPR in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)).

**CSF anchors (from `SR-GDPR-029` v0.3 security_rationale):**
ID.AM-08, ID.AM-03.
**PF 1.1 anchors (from `SR-GDPR-029` — dashboard `00_VISUALISATIONS/GDPR/GDPR_Dashboard.html`, mechanical uniformization):**
CT.PO-P4, CT.DM-P5.
*(ID.AM-08 captures the per-dataset risk-and-purpose binding — the
controller defines and documents a retention period for each category,
resets the clock when the underlying purpose changes, and pairs
long-term archiving or research-only retention with the Art. 89(1)
pseudonymisation, aggregation and access-limitation safeguards so
that the residual data set at any moment is the smallest the purpose
permits. ID.AM-03 captures the data-inventory substrate without which
retention cannot be enforced — every personal-data category must
appear in an inventory tagged with declared purpose, lawful basis and
envisaged erasure time, so that periodic review can decide to retain,
anonymise or delete against a documented clock rather than against an
undocumented assumption. The two subcategories together enable the
controller to demonstrate ex post, against the Art. 5(2) accountability
duty, that no personal data was retained beyond the period necessary
for its declared purpose on the day of any supervisory inspection.)*

---


## Security Requirements (GDPR)

#### 5.2.1 — Personal-data retention ceiling per Art. 5(1)(e) with Art. 89(1) safeguards for public-interest/research/statistical carve-out

```yaml
- req_id: 5.2.1
  volere_section: 15
  volere_subtype: privacy

  title: "Personal data retained no longer than necessary for the processing purpose; longer retention only where lawful and subject to Art. 89(1) safeguards; Art. 30(1)(f) RoPA time-limits documented per category"

  derives_from:
    hso_sub_so: SG-D-05.2.GDPR
    per_reg_so: SG-GDPR-017
    source_sr: SR-GDPR-029
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.2.md
    objective_ref_section: "### D-05.2.1"

  description: |
    The product shall keep personal data in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)).

  fit_criterion: |
    A controller-side personal-data-retention-ceiling architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (every personal-data category appears in an inventory tagged with declared purpose, lawful basis, and envisaged erasure time so that periodic review can decide to retain, anonymise or delete against a documented clock) + ID.AM-08 data managed consistent with the controller's risk strategy (the controller defines and documents a retention period for each category, resets the clock when the underlying purpose changes, and pairs long-term archiving or research-only retention with the Art. 89(1) pseudonymisation, aggregation and access-limitation safeguards); the Art. 5(1)(e) `no longer than is necessary` ceiling is enforced per data category with periodic erasure-or-anonymisation review; the Art. 30(1)(f) RoPA envisages-time-limits-for-erasure (or the criteria for determining them, where possible per OJ hedge) are documented per category; for the public-interest/research/statistical carve-out, Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) are applied so that the residual data set at any moment is the smallest the purpose permits; the controller demonstrates ex post against the Art. 5(2) accountability duty that no personal data was retained beyond the period necessary for its declared purpose on the day of any supervisory inspection; when the same data flow is also a CRA update artefact (CRA update-distribution log containing personal data) or an AI Act log (AI log containing personal data), the GDPR Art. 5(1)(e) `necessary` boundary is the operative cap on the personal-data subset, with separation architecture (pseudonymisation of the personal-data subset, separate retention rules) as the controlled hand-off to the CRA-side availability tail or AI Act-side log floor; verified by data-inventory audit + per-category retention-period documentation review + Art. 30(1)(f) RoPA time-... (line truncated to 2000 chars)

  priority: MUST
  verification_method: TEST
  dependencies: [5.2.2 (when CRA update-distribution log contains personal data — separation architecture is the layering rule; GDPR Art. 5(1)(e) `necessary` boundary remains the operative cap on the personal-data subset, CRA-side availability tail applies to the artefact portion), 5.2.3 (when AI log contains personal data — floor-within-ceiling relationship; operative range is [6 months, "necessary"] with AI Act setting the floor and GDPR setting the cap)]

  nist_csf: [ID.AM-08, ID.AM-03]
  nist_pf: [CT.PO-P4, CT.DM-P5]

  applicable_if:
    regs: [GDPR]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (GDPR)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**GDPR article (verbatim, Art. 5(1)(e) + Art. 30(1)(f)):**
> "Personal data shall be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed ('storage limitation'). Personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89(1) subject to implementation of the appropriate technical and organisational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject." — Art. 5(1)(e) GDPR
>
> "Each controller … shall maintain a record of processing activities under its responsibility … that contains … where possible, the envisaged time limits for erasure of the different categories of data." — Art. 30(1)(f) GDPR

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/GDPR.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-05.2: GDPR↔CRA = CORRECTED from CONTRADICTORY to SCOPE-DISJOINT (separation-architecture layering rule); GDPR↔AI_Act = CORRECTED from CONTRADICTORY to COMPLEMENTARY (floor-within-ceiling))
```

### from regs/GDPR.md body

**Considerations.**

- The CRA 10-year tail is on update artefacts (non-personal data) and Annex II information, NOT on personal data; when a CRA update log contains personal data, separation architecture (pseudonymisation of the personal-data subset) is the layering rule — GDPR Art. 5(1)(e) `necessary` boundary remains the operative cap on the personal-data portion.

### from regs/GDPR.md body

- The AI Act ≥6-month floor is a subset of GDPR's "necessary" envelope — the floor-within-ceiling relationship binds when AI logs contain personal data, with operative range [6 months, "necessary"] and the controller/provider choosing actual retention within the range based on intended purpose.


### from regs/GDPR.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # GDPR↔CRA = Conditional (Y when CRA update log contains personal data — separation-architecture layering rule; N pure update artefacts with no personal data — pair is scope-disjoint in baseline); GDPR↔AI_Act = Conditional (Y when AI logs contain personal data — floor-within-ceiling; N pure technical logs with no personal data — pair is substantive-complementary on the same data flow with operative range [6 months, "necessary"]); HL engages on overlap

```

### from regs/GDPR.md body — field `considerations`

```yaml
  considerations: |
    The GDPR retention/archiving obligation is the controller-side personal-data-retention ceiling anchored on Art. 5(1)(e) `no longer than is necessary` plus the Art. 30(1)(f) RoPA envisaged-time-limits-for-erasure documentation plus the Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for the public-interest/research/statistical carve-out. The CRA 10-year tail is on update artefacts (non-personal data) and Annex II information, NOT on personal data; when a CRA update log contains personal data, separation architecture is the layering rule and GDPR Art. 5(1)(e) `necessary` boundary remains the operative cap on the personal-data portion. The AI Act ≥6-month floor is a subset of GDPR's `necessary` envelope — the floor-within-ceiling relationship binds when AI logs contain personal data, with operative range [6 months, "necessary"] and the controller/provider choosing actual retention within the range based on intended purpose. (Copied from the HSO Considerations block of `### D-05.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=GDPR; demoted=5; core_cross_mentions=2 -->
