# D-04.3 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS 2 | SO-NIS2-006 | 24h early warning + 72h incident | Significant incident; entity → CSIRT / CA |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS 2** | significant incident (Art. 23(3) test A+B) | network and information systems | CSIRT or competent authority | Art. 23(4) | 24h early warning → 72h → 1m final |

## Sub-SO (NIS 2)

#### D-04.3.2 — Sub-SO for NIS 2

```yaml
id: SO-D-04.3.NIS2
subdomain: D-04.3
applies_to: [NIS2]
inherits_from: SO-NIS2-006
source_SR: SR-NIS2-010
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A significant incident is notified to the CSIRT or, where applicable, the competent authority via a twin-trigger pattern — an early warning within 24 hours of awareness (Art. 23(4)(a), `SR-NIS2-010`) followed by an incident notification within 72 hours with severity, impact, and (where available) indicators of compromise (Art. 23(4)(b), `SR-NIS2-011`).

**CSF anchors (from `SR-NIS2-010` v0.3 security_rationale):**
RS.MA-04, RS.MA-02.
*(The downstream `SR-NIS2-011` 72h tier adds RS.MA-03.)*

---


## Security Requirements (NIS 2)

#### 4.3.2 — Twin-trigger 24h early warning + 72h notification + 1m final report to CSIRT

```yaml
- req_id: 4.3.2
  volere_section: 15
  volere_subtype: audit

  title: "Significant incident notified via twin-trigger pattern — 24h early warning + 72h incident notification + 1m final report — to CSIRT or competent authority"

  derives_from:
    hso_sub_so: SO-4.3.NIS2
    per_reg_so: SO-NIS2-006
    source_sr: SR-NIS2-010, SR-NIS2-011, SR-NIS2-012
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.2"

  description: |
    The product shall notify significant incidents — per Art. 23(3) tests A or B — to the CSIRT or, where applicable, the competent authority via the twin-trigger pattern: an early warning within 24 hours of becoming aware of the significant incident (Art. 23(4)(a), `SR-NIS2-010`), an incident notification within 72 hours of becoming aware with severity, impact, and (where available) indicators of compromise (Art. 23(4)(b), `SR-NIS2-011`), and a final report no later than one month after the incident notification (Art. 23(4)(c), `SR-NIS2-012`), with the `in any event` ceiling ensuring no softening (NIS 2 Art. 21(2)(b) chapeau + Art. 23(4) + Art. 23(3) + Art. 6(8) six-action definition).

  fit_criterion: |
    A CSIRT-notification pipeline is operated with 3-tier temporal discipline: 24h early warning clock-started from 4.1 NIS 2 leg's awareness event (Art. 23(4)(a) — `without undue delay and in any event within 24 hours`), 72h incident notification with severity/impact/IoC content (Art. 23(4)(b) — `in any event within 72 hours`), and 1m final report (Art. 23(4)(c) — 30 days after incident notification, the standard reading per Recital 56); the `in any event` ceiling is documented as the NIS 2-unique binding rule that overrides the GDPR `where feasible` softening on multi-reg overlap; the Art. 23(3) significant-incident tests (test A — service-disruption severity 5+ qualified impacts; test B — significant impact on continuity of essential services) gate the obligation; the 24h early-warning tier fires upon substantive awareness even before full triage; the 72h notification tier provides the assessment (severity, impact, IoCs) and updates the 24h tier; the final report tier closes the lifecycle with detailed forensic/post-incident content; for eIDAS QTSPs the derogation to 24h applies (Art. 23(4) ¶2 — `SR-NIS2-013`); for critical-infrastructure digital-infrastructure categories the Art. 23(11) implementing-acts may add granularity (4.3 Generic); verified by CSIRT-notification logs review + 24h clock-anchor records inspection + 72h clock-anchor records inspection + 1m clock-anchor records inspection + severity/impact/IoC content-template coverage audit + Art. 23(3) significant-incident tests documentation + on-demand intermediate-report records (when CA requests Art. 23(4)(b) `SR-NIS2-014`) + CSIRT / competent-authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.2 (notification clock depends on 4.1 NIS 2 awareness event; 24h bound), 4.2.2 (notification content requires prior containment classification feeding 72h tier severity/impact assessment)]

  nist_csf: [RS.MA-04, RS.MA-02, RS.MA-03]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim):**
> Article 23(4)(a) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning which, where applicable, shall indicate whether the significant incident is suspected of being caused by unlawful or malicious acts or could have a cross-border impact (OJ L 333, 27.12.2022, p. 129).

**NIS2 article (verbatim):**
> Article 23(4)(b) of Directive (EU) 2022/2555 requires the entity, upon becoming aware of a significant incident, to submit to the CSIRT or, where applicable, the competent authority, without undue delay and in any event within 72 hours of becoming aware of the significant incident, an incident notification which, where applicable, shall update the information referred to in point (a) and indicate an initial assessment of the significant incident, including its severity and impact, as well as, where available, the indicators of compromise (OJ L 333, 27.12.2022, p. 129).

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: CONDITIONAL (CRDA-deep, D-04.3 GDPR↔NIS2: SCOPE-DISJOINT baseline / CONTRADICTORY; NIS2↔CRA: COMPLEMENTARY; NIS2↔DORA: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY; NIS2↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY)
```

### from regs/NIS2.md body

**Considerations.**

- The `in any event` ceiling of the NIS 2 72-hour clock leaves no `where feasible` softening — when NIS 2 and GDPR both apply on the same event, the NIS 2 ceiling binds (24h early warning + 72h notification + 1m final report); the GDPR `where feasible` softening does not survive the multi-reg overlap.


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Conditional (Y controller-NSIE); NIS2↔CRA = COMPLEMENTARY (manufacturer-disjoint baseline; when manufacturer is also deployer, CRA and NIS 2 notify on different legs — AEV vs significant incident); NIS2↔DORA = Conditional (Y cross-sector; N pure-financial via DORA lex specialis — DORA absorbs NIS 2 ICT-hazard; NIS 2 chapeau extends to physical+operational hazards); NIS2↔AI_Act = Conditional (Y NSIE deploys high-risk AI; parallel clocks)

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 notification obligation is the significant-incident CSIRT-notification with twin-trigger pattern (24h + 72h + 1m); the operational substrate is a CSIRT-notification pipeline with 3-tier temporal discipline. The `in any event` ceiling is NIS 2-unique among the five 4.3 regulators — when NIS 2 and GDPR both apply on the same event, the NIS 2 ceiling binds (no `where feasible` softening on the multi-reg overlap). The Art. 23(3) significant-incident tests (test A + test B) gate the obligation; the entity must run both tests and document the determination. The CSIRT or competent authority routing is Member-State-determined (some MSes designate CSIRT as single-entry-point; others designate the CA with CSIRT forwarding under Art. 23(1) ¶2). The Art. 23(1) ¶1 recipient-of-services notification (when appropriate, softer than CSIRT-side) is captured separately under 4.3 downstream. For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 ICT-hazard notification obligation; the high-level SO does not aggregate across the lex-specialis boundary in that direction. The NIS 2 chapeau `all-hazards` (Art. 21(2) + Recital 56) extends the notification trigger to operational + physical-environment hazards beyond ICT. (Copied from the HSO Considerations block of `### 4.3.2`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=NIS2; demoted=4; core_cross_mentions=1 -->