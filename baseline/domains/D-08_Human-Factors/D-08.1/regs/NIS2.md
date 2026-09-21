# D-08.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-018 | Basic cyber hygiene practices are established, covering all users of network and information systems with access to entity systems and services (Art. 21(2)(g) first clause). | Entity-wide hygiene baseline; workforce-and-systems substrate. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | entity-wide workforce and systems (workforce hygiene baseline covering phishing, password discipline, removable-media) | entity-wide basic-hygiene baseline per Art. 21(2)(g) first clause `basic cyber hygiene practices and cybersecurity training` | `appropriate and proportionate` (Art. 21(1) chapeau) + state-of-the-art (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative cadence; the OJ does not enumerate the hygiene practices — entity-discretionary interpretation under Recital 56 proportionality | management body (Art. 20(1) approve+oversee+liability) + competent authority — Art. 21(2)(g) basic-hygiene records + Art. 21(1) documented policies + Art. 20(1) management-body approval | Art. 21(2)(g) first clause + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Art. 20(1) management-body approval + Recital 56 proportionality |

## Sub-SO (NIS 2)

#### D-08.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-08.1.NIS2
subdomain: D-08.1
applies_to: [NIS2]
inherits_from: SO-NIS2-018
source_SR: SR-NIS2-029
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure basic cyber hygiene practices and cybersecurity training (Art. 21(2)(g) first clause NIS 2).

**Considerations.**
- The NIS 2 hygiene baseline is the entity-wide substrate covering all users of network and information systems with access to entity systems and services (per SO-NIS2-018 scope).
- The hygiene practices are not enumerated in the OJ — `basic cyber hygiene` admits three operative readings (minimal-password-patch-antivirus, broader ENISA baseline, sector-specific), with the chosen reading being entity-discretionary interpretation under Recital 56 proportionality (per SR-NIS2-029 ambiguity_notes).
- PR.AT-01 anchors the human-side hygiene substrate (phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, disciplined use of administrative privileges).
- PR.PS-01 anchors the system-side hygiene substrate (baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory).
- The two together define the workforce-and-assets hygiene baseline that ENISA, the SANS Top 20, and the Australian Cyber Security Centre Essential Eight converge on (per SR-NIS2-029 security_rationale).
**CSF anchors (from `SR-NIS2-029` v0.3 security_rationale):**
PR.AT-01, PR.PS-01.
*(PR.AT-01 anchors the human-side hygiene substrate: phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, and the disciplined use of administrative privileges. PR.PS-01 anchors the system-side hygiene substrate: baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory. Together PR.AT-01 and PR.PS-01 define the workforce-and-assets hygiene baseline that ENISA, the SANS Top 20 and the Australian Cyber Security Centre Essential Eight converge on. The two controls also propagate into the vulnerability-hygiene loop: hygiene lapses are themselves a recurring source of incidents that ID.RA-01 records and PR.PS-02 remediates. The control set enables ex-post demonstration that the entity operates against a documented hygiene baseline rather than an ad-hoc checklist, with the depth calibrated to Article 21(1) proportionality factors and the baseline re-reviewed when ENISA or national guidance material changes.)*

---


## Security Requirements (NIS 2)

#### 8.1.2 — Entity-wide basic-hygiene baseline with `appropriate and proportionate` calibration

```yaml
- req_id: 8.1.2
  volere_section: 15
  volere_subtype: immunity

  title: "Entity-wide basic cyber-hygiene practices with workforce hygiene substrate and proportionate calibration"

  derives_from:
    hso_sub_so: SO-8.1.NIS2
    per_reg_so: SO-NIS2-018
    source_sr: SR-NIS2-029
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md
    objective_ref_section: "### 8.1.2"

  description: |
    The product shall establish basic cyber-hygiene practices and cybersecurity training for all users of network and information systems with access to entity systems and services (Art. 21(2)(g) first clause NIS 2), with the depth calibrated by the Art. 21(1) `appropriate and proportionate` chapeau and the state-of-the-art floor, on the entity-wide workforce-and-systems substrate, and with Art. 20(1) management-body approval+oversight+liability.

  fit_criterion: |
    An entity-wide basic-hygiene programme is operated covering all users of network and information systems with access to entity systems and services via the human-side hygiene substrate PR.AT-01 (phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, disciplined use of administrative privileges) plus the system-side hygiene substrate PR.PS-01 (baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory); the two together operationalise the ENISA / SANS Top 20 / Australian Cyber Security Centre Essential Eight convergence on workforce-and-assets hygiene; the chosen reading of `basic cyber hygiene` is the broader ENISA baseline reading, with the chosen reading being entity-discretionary interpretation under Recital 56 proportionality (no quantitative cadence in Art. 21(2)(g) and no OJ enumeration — three operative readings admitted per SR-NIS2-029 ambiguity_notes); the depth is calibrated by the Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor + Recital 56 proportionality factors (nature/size/risk profile/cost of implementation); for an integrated controller-NSIE workforce the NIS 2 hygiene module combines with the GDPR DPO-catalysed data-protection awareness module into a single curriculum (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship — combined curriculum with separate evidence trails); for DORA financial entities, the DORA Art. 13(6) `compulsory modules` exceeds NIS 2 `basic cyber hygiene` and the DORA programme discharges the NIS 2 workforce-awareness obligation (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs); for a CRA-regulated manufacturer, the NIS 2 hygiene baseline on the workforce is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule); the Art. 20(1) management-body approval is documented as the governance hook; verified by entity-wide hygiene-coverage audit + PR.AT-01 + PR.PS-01 records review + Art. 21(1) proportionality calibration documentation + Art. 20(1) management-body approval records + management-body + competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [8.1.1 (when controller = NSIE — NIS 2 hygiene module combines with GDPR data-protection module into single curriculum), 8.1.4 (when DORA-NSIE — DORA Art. 13(6) discharges NIS 2 workforce-awareness obligation for financial entities)]

  nist_csf: [PR.AT-01, PR.PS-01]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(g) first clause):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (g) basic cyber hygiene practices and cybersecurity training." — Art. 21(2)(g) first clause NIS 2 (per SR-NIS2-029)

**NIS2 article (verbatim, Art. 21(2)(g) first clause):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-08.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — DPO data-protection vs hygiene baseline stack at controller-NSIE); NIS2↔DORA = EQUAL (SAME — both regulations impose workforce awareness programmes at entity level; DORA-dominant for financial entities); NIS2↔CRA = DIFFERENT-PERSPECTIVE (SAME — substantively scope-disjoint; workforce vs end-user audiences; no consolidation rule))
```

### from regs/NIS2.md body

- For an integrated controller-NSIE workforce, the NIS 2 hygiene module combines with the GDPR DPO-catalysed data-protection awareness module into a single curriculum.

### from regs/NIS2.md body

- For DORA financial entities, the DORA Art. 13(6) `compulsory modules` is more prescriptive than NIS 2's `basic cyber hygiene` (entity-discretionary under Recital 56) — DORA-dominant for financial entities; NIS 2-dominant for non-financial NSIEs (per CRDA-deep §D-08.1 NIS2↔DORA EQUAL classification).

### from regs/NIS2.md body

- For a CRA-regulated manufacturer, the NIS 2 hygiene baseline on the workforce is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule applies).


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Y (controller-NSIE; combined curriculum); NIS2↔CRA = N (typically) substantively scope-disjoint (workforce vs end-user); NIS2↔DORA = Y (DORA financial entity = NSIE; DORA programme discharges NIS 2; for pure-financial NIS 2 §9 fall-back does not apply — DORA lex specialis); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 general-awareness obligation is the **entity-wide hygiene baseline** covering all users of network and information systems with access to entity systems and services (per SO-NIS2-018 scope). The hygiene practices are not enumerated in the OJ — `basic cyber hygiene` admits three operative readings (minimal-password-patch-antivirus, broader ENISA baseline, sector-specific), with the chosen reading being entity-discretionary interpretation under Recital 56 proportionality (per SR-NIS2-029 ambiguity_notes). PR.AT-01 anchors the human-side hygiene substrate (phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, disciplined use of administrative privileges). PR.PS-01 anchors the system-side hygiene substrate (baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory). The two together define the workforce-and-assets hygiene baseline that ENISA, the SANS Top 20, and the Australian Cyber Security Centre Essential Eight converge on (per SR-NIS2-029 security_rationale). The two controls also propagate into the vulnerability-hygiene loop: hygiene lapses are themselves a recurring source of incidents that ID.RA-01 records and PR.PS-02 remediates. **8.2 layer (8.2.2)** adds the Member-State-encouraged employee training on risk-identification and assessment per Art. 20(2) sentence 2. For an integrated controller-NSIE workforce, the NIS 2 hygiene module combines with the GDPR DPO-catalysed data-protection awareness module into a single curriculum. For DORA financial entities, the DORA Art. 13(6) `compulsory modules` is more prescriptive than NIS 2's `basic cyber hygiene` (entity-discretionary under Recital 56) — DORA-dominant for financial entities; NIS 2-dominant for non-financial NSIEs (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification). For a CRA-regulated manufacturer, the NIS 2 hygiene baseline on the workforce is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule applies). The recipient is the management body (Art. 20(1) approve+oversee+liability) + competent authority (Art. 21(1) + Art. 21(2)(g) basic-hygiene records). (Copied from the HSO Considerations block of `### 8.1.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=6; core_cross_mentions=2 -->

