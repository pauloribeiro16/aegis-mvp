# D-05.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-035 + SO-CRA-061 (cross-ref) | Security updates and supporting advisory messages remain available across support period + Art. 13(18) 10-year Annex II information accessibility | Update artefacts (firmware, patches, advisories) + Annex II information; manufacturer obligation; Annex I Part II (7)/(8) + Art. 13(9) 10-year tail + Art. 13(18) 10-year information accessibility + Art. 13(8) 5-year support-period floor; PR.PS-02 + GV.OC-04 (10-year tail SR) + PR.PS-02 + GV.OV-02 |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | update artefacts (security updates, firmware, patches, advisories) + Annex II information | floor (lower bound, support period + 10-year tail) | ongoing availability of security updates across support period + Annex II information accessibility | support period ≥5 years (Art. 13(8)) OR expected use time if shorter; update-availability tail ≥10 years from issue date OR remainder of support period, whichever is longer (Art. 13(9)); Annex II information accessibility ≥10 years from placing on market (Art. 13(18)) | support period (post-market, 5-year minimum) + 10-year availability tail | market surveillance authority (MSA) + users | Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge + Art. 13(8) support period + Art. 13(9) 10-year update-availability tail + Art. 13(18) 10-year Annex II information accessibility + Art. 13(19) support-period end-date display + Annex II §7 |

## Sub-SO (CRA)

#### D-05.2.2 — Sub-SO for CRA

```yaml
id: SO-D-05.2.CRA
subdomain: D-05.2
applies_to: [CRA]
inherits_from: SO-CRA-035, SO-CRA-061 (cross-ref)
source_SR: SR-CRA-016, SR-CRA-047
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail (Art. 13(9) 10-year update-availability tail + Art. 13(8) 5-year support-period floor + Art. 13(18) 10-year Annex II information accessibility + Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge, with advisory messages); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7).

- The CRA Art. 13(9) 10-year-or-remainder is a twin-anchor pattern — the longer of 10 years from issue date or the remainder of the support period applies per update (R2 reading).
**CSF anchors (from `SR-CRA-016` + `SR-CRA-047` v0.3
security_rationale):**
PR.PS-02, GV.OV-02, GV.OC-04.
*(`SR-CRA-016` covers the Art. 13(9) 10-year-or-remainder update-
availability tail anchored to PR.PS-02 (software maintained, replaced,
and removed commensurate with risk — the artefact-availability leg;
the maintained-software Subcategory interpreted at the artefact level
— signed packages, version archives, integrity-protected catalogues —
rather than at the active-patching level) + GV.OV-02 (organisational
cybersecurity risk-management strategy reviewed and adjusted to
address changes in the risk landscape — the strategic-review
dimension; as the technology baseline and threat landscape evolve,
the manufacturer must review its retention strategy against the
Art. 13(9) floor, ensuring long-lived products remain within the
operative availability envelope). `SR-CRA-047` covers the
Annex I Part II (7)+(8) + Art. 13(18) secure-update-distribution and
Annex II information accessibility duty anchored to PR.PS-02 +
GV.OC-04 (critical objectives, capabilities, and services that
stakeholders depend on or expect from the organisation are understood
and communicated — the user-as-stakeholder dimension; the manufacturer
understands and communicates to users the critical capabilities the
user depends on, with the advisory messages required by (8) supplying
the per-update communication channel and the Annex II information
deliverable supplying the durable instruction layer). The three
subcategories together enable the manufacturer to demonstrate ex post,
through documented update-distribution logs, user-communication
records, and Annex VII section 4 retention evidence, that each issued
security update has remained available for the maximum of its 10-year
floor or its support-period remainder, whichever is longer, and that
the Annex II information deliverable has remained accessible for at
least 10 years from placing on market.)*

---


## Security Requirements (CRA)

#### 5.2.2 — Update-artefact availability across support period + 10-year tail + 10-year Annex II information accessibility

```yaml
- req_id: 5.2.2
  volere_section: 15
  volere_subtype: privacy

  title: "Security updates available across support period and the 10-year-or-remainder tail; Annex II information accessible for ≥10 years from placing on market; support-period end-date communicated at purchase"

  derives_from:
    hso_sub_so: SO-D-05.2.CRA
    per_reg_so: SO-CRA-035, SO-CRA-061 (cross-ref)
    source_sr: SR-CRA-016, SR-CRA-047
    hso_file: ../../HierarchicalSecurityObjectives/D-05_Data-Lifecycle/D-05.2.md
    objective_ref_section: "### D-05.2.2"

  description: |
    The product shall keep security updates and supporting advisory messages available to users across the support period and the 10-year-or-remainder-of-support-period update-availability tail (Art. 13(9) 10-year tail + Art. 13(8) 5-year support-period floor), with secure update distribution and dissemination without delay, free of charge (Annex I Part II (7)/(8)), and the Annex II information shall remain accessible for at least 10 years from placing on market (Art. 13(18)); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7).

  fit_criterion: |
    A manufacturer-side update-availability-tail architecture is operated under PR.PS-02 software maintained, replaced, and removed commensurate with risk (the artefact-availability leg — signed packages, version archives, integrity-protected catalogues, rather than the active-patching leg) + GV.OV-02 organisational cybersecurity risk-management strategy reviewed and adjusted (the strategic-review dimension — as the technology baseline and threat landscape evolve, the manufacturer reviews its retention strategy against the Art. 13(9) floor) + GV.OC-04 critical objectives, capabilities, and services that stakeholders depend on or expect from the organisation are understood and communicated (the user-as-stakeholder dimension — advisory messages required by Annex I Part II (8) supply the per-update communication channel and the Annex II information deliverable supplies the durable instruction layer); the Art. 13(8) 5-year support-period floor is enforced per product (or expected use time if shorter); the Art. 13(9) 10-year-or-remainder-of-support-period update-availability tail is enforced per update with the twin-anchor pattern (R2 reading — the longer of 10 years from issue date or the remainder of the support period applies per update; R1 always-10-years and R3 always-remainder are both rejected because they ignore the "whichever is longer" qualifier or the 10-year floor respectively); the Art. 13(18) ≥10-year Annex II information accessibility is enforced from placing on market with the conjunction support-period + at-least-10-years preserved (the longer of the two governing); the Art. 13(19) support-period end-date display at purchase is implemented clearly and understandably with the month and year (Annex II §7); the CRA 10-year tail is on update artefacts (firmware, patches, advisories — non-personal data) and Annex II information, NOT on personal data; when a CRA update-distribution log contains personal data, separation architecture (pseudonymisation of the pe... (line truncated to 2000 chars)

  priority: MUST
  verification_method: INSPECT
  dependencies: [5.2.1 (when CRA update-distribution log contains personal data — separation-architecture layering rule applies; CRA tail applies to artefact portion; GDPR Art. 5(1)(e) `necessary` boundary applies to personal-data subset independently)]

  nist_csf: [PR.PS-02, GV.OV-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part II (7)/(8) + Art. 13(8)/(9)):**
> "Securely distribute updates … to the users of products with digital elements, in a timely manner, including, where appropriate, through automatic updates." — CRA Annex I Part II (7)
>
> "Ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take." — CRA Annex I Part II (8)
>
> "Where, after placing a product with digital elements on the market, the manufacturer becomes aware of a vulnerability affecting the security of the product, the manufacturer shall, without delay, disclose the vulnerability and any associated mitigations to the person or entity maintaining the product, where applicable, and to the market surveillance authorities, as well as, where the manufacturer becomes aware of an actively exploited vulnerability, to the users of the product." — CRA Art. 13(9) (vulnerability disclosure — adjacent but distinct from update availability)

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: NON-SAME (CRDA-deep, D-05.2: GDPR↔CRA = CORRECTED from CONTRADICTORY to SCOPE-DISJOINT (separation-architecture layering rule); CRA↔AI_Act = DIFFERENT-PERSPECTIVE (SAME — update artefact availability vs AI log retention))
```

### from regs/CRA.md body

**Considerations.**

- The CRA 10-year tail is on update artefacts (firmware, patches, advisories) and Annex II information — NOT on personal data; if a CRA product's update-distribution log contains personal data, separation architecture is the layering rule (pseudonymise the personal-data portion; CRA tail applies to the artefact portion, GDPR Art. 5(1)(e) `necessary` boundary applies to the personal-data subset independently).

### from regs/CRA.md body

- The AI Act ≥6-month AI-log floor is on a distinct data class (AI logs) at a different actor (provider); CRA↔AI_Act = DIFFERENT-PERSPECTIVE (disjoint in baseline, different objects/actors/purposes).


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = Conditional (Y when CRA update log contains personal data — separation-architecture layering rule; N pure update artefacts with no personal data — pair is scope-disjoint in baseline); CRA↔AI_Act = N (disjoint in baseline — different objects: update artefacts vs AI logs; different actors: manufacturer vs provider; different purposes: user protection continuity vs post-market monitoring); HL engages on overlap

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA retention/archiving obligation is the manufacturer-side update-artefact availability tail plus the Annex II information accessibility duty, anchored on the Art. 13(8) 5-year support-period floor + Art. 13(9) 10-year update-availability tail + Art. 13(18) ≥10-year Annex II information accessibility + Art. 13(19) support-period end-date display + Annex I Part II (7)/(8) secure-update-distribution and dissemination. The CRA 10-year tail is on update artefacts (firmware, patches, advisories) and Annex II information — NOT on personal data; if a CRA product's update-distribution log contains personal data, separation architecture is the layering rule (pseudonymise the personal-data portion; CRA tail applies to the artefact portion, GDPR Art. 5(1)(e) `necessary` boundary applies to the personal-data subset independently). The CRA Art. 13(9) `at least 10 years or for the remainder of the support period, whichever is longer` is a twin-anchor pattern where the 10-year floor and the support-period remainder are compared, and the longer of the two applies in each case — R2 reading. The AI Act ≥6-month AI-log floor is on a distinct data class (AI logs) at a different actor (provider); CRA↔AI_Act = DIFFERENT-PERSPECTIVE (disjoint in baseline, different objects/actors/purposes). (Copied from the HSO Considerations block of `### D-05.2.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=5; core_cross_mentions=1 -->
