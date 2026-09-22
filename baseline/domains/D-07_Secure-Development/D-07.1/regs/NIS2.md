# D-07.1 — NIS 2 module

> Regulation-specific layer: applies when `NIS2` is in scope
> (activation: `if NIS2 in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| NIS2 | SO-NIS2-017 | Security integrated into acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure, across the system lifecycle (Art. 21(2)(e)). | Entity-level lifecycle discipline; three coordinated phases (acquisition, development, maintenance); `appropriate and proportionate` chapeau + state-of-the-art floor + cost factor (Art. 21(1)); vulnerability handling+disclosure leg is one of three coordinated legs. |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **NIS2** | NIS lifecycle security across acquisition, development, maintenance (entity side / user side) | NIS-acquisition activity (Art. 21(2)(e) first clause) + development activity (Art. 21(2)(e) second clause) + maintenance activity (Art. 21(2)(e) third clause) + vulnerability handling and disclosure (Art. 21(2)(e) fourth clause) | `appropriate and proportionate` (Art. 21(1) chapeau) + `state of the art` (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative threshold | management body (Art. 20(1) approve+oversee+liability) + competent authority | Art. 21(2)(e) + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Art. 20(1) management-body approval |

## Sub-SO (NIS 2)

#### D-07.1.2 — Sub-SO for NIS 2

```yaml
id: SO-D-07.1.NIS2
subdomain: D-07.1
applies_to: [NIS2]
inherits_from: SO-NIS2-017
source_SR: SR-NIS2-026
activation: if NIS2 in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) NIS 2).

**Considerations.**
- The 3-phase coordinated lifecycle (acquisition, development, maintenance) is operationalised through: (1) acquisition-phase supplier SDLC assessment (per SR-NIS2-026 on the basis of Art. 21(3) sentence 1 supplier-secure-development-procedures three-prong); (2) development-phase in-house secure-by-design decisions (per SR-NIS2-027); (3) maintenance-phase vulnerability handling+disclosure + patch-management + change-management (per SR-NIS2-028).
- Art. 21(1) chapeau `appropriate and proportionate` is read with Art. 21(1) sentence 2 state-of-the-art floor + Recital 56 cost-of-implementation qualifier + Member-State-transposition-supplied proportionality calibration.
- Art. 20(1) management-body approval+oversight+liability leg (cross to D-09.1) is the upstream governance instrument.
**CSF anchors (from `SR-NIS2-026` v0.3 security_rationale):**
PR.PS-06, GV.SC-02.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the NIS 2 Art. 21(2)(e) 3-phase coordinated lifecycle (acquisition + development + maintenance) maps to PR.PS-06 directly. PR.PS-02 anchors the software-maintenance dimension — software is maintained, replaced, and removed commensurate with risk; the NIS 2 Art. 21(2)(e) maintenance phase + vulnerability-handling-and-disclosure leg maps to PR.PS-02 directly. The two subcategories together enable the essential / important entity to demonstrate ex post, through documented supplier-SDLC-assessment records on the acquisition phase + in-house secure-by-design-decision records on the development phase + vulnerability-handling records + maintenance records + Art. 20(1) management-body approval record on the maintenance phase, that the Art. 21(2)(e) security-in-acquisition+development+maintenance duty has been exercised with the `appropriate and proportionate` chapeau + state-of-the-art floor.)*

---


## Security Requirements (NIS 2)

#### 7.1.2 — Entity-level security in acquisition, development and maintenance

```yaml
- req_id: 7.1.2
  volere_section: 15
  volere_subtype: integrity

  title: "Security integrated into the acquisition, development and maintenance of network and information systems across the 3-phase coordinated lifecycle with vulnerability handling and disclosure"

  derives_from:
    hso_sub_so: SO-D-07.1.NIS2
    per_reg_so: SO-NIS2-017
    source_sr: SR-NIS2-026, SR-NIS2-027, SR-NIS2-028
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.1.md
    objective_ref_section: "### D-07.1.2"

  description: |
    The product shall take appropriate and proportionate technical, operational and organisational measures to ensure security in the acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure, with the three coordinated lifecycle phases operationalised through supplier SDLC assessment at acquisition, in-house secure-by-design decisions at development, and vulnerability handling+disclosure + patch-management + change-management at maintenance (NIS 2 Art. 21(2)(e) + Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor).

  fit_criterion: |
    A documented 3-phase NIS 2 lifecycle (acquisition / development / maintenance) is maintained with: (1) **acquisition phase** — supplier-SDLC assessment per Art. 21(3) sentence 1 supplier-secure-development-procedures three-prong (SR-NIS2-026), with supplier-by-design evidence records retained; (2) **development phase** — in-house secure-by-design decisions documented per SR-NIS2-027 covering threat modelling, secure-by-design choices, secure-coding standards, code review, security testing (mapped to PR.PS-06) and component selection / dependency hygiene / update channels (mapped to PR.PS-02); (3) **maintenance phase** — vulnerability handling+disclosure with CSIRT-coordinated disclosure channel per Art. 12(1) (mapped to ID.RA-01) and patch + configuration + replacement cadence commensurate with risk (mapped to PR.PS-02); the 3-phase architecture has explicit hand-offs at the acquisition gate (supplier → entity), the development gate (in-house design decisions), and the maintenance gate (vulnerability discovery → validation → record → response); Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor + Recital 56 cost-of-implementation qualifier governs the depth and scope; Art. 20(1) management-body approval + oversight + liability is the upstream governance instrument; for an integrated controller-NSIE, the NIS 2 acquisition-phase supplier SDLC assessment realises the GDPR Art. 25(1) controller-side by-design outputs (pseudonymised-by-default pipelines, minimisation-by-default) at the procurement gate; verified by supplier-SDLC assessment records review + in-house secure-by-design-decision records inspection + vulnerability handling-and-disclosure records review + maintenance + patch-cadence records audit + Art. 20(1) management-body approval record + management body + competent authority inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.1.1 (when controller is also NSIE — GDPR by-design outputs realised through NIS 2 acquisition + development gates), 7.1.3 (when NIS 2 entity procures / manufactures CRA product — NIS 2 supplier-customer boundary references CRA Annex VII technical documentation), 7.1.4 (when DORA financial entity is also NSIE — DORA Art. 9(4)(e) change-mgmt operationalises NIS 2 maintenance phase for ICT-hazard subset; NIS 2 chapeau extends to physical + operational hazards), 7.1.5 (when NIS embeds high-risk AI — NIS 2 procurement gate + AI Act QMS governance gate stack)]

  nist_csf: [PR.PS-06, GV.SC-02]

  applicable_if:
    regs: [NIS2]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (NIS 2)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**NIS2 article (verbatim, Art. 21(2)(e)):**
> "[Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to … ] (e) security in acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure." — Art. 21(2)(e) NIS 2


**NIS2 article (verbatim, Art. 21(2)(e)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/NIS2.md body — field `verified_relationship`

```yaml
verified_relationship: COMPLEMENTARY (CRDA-deep, D-07.1: GDPR↔NIS2 = COMPLEMENTARY (SAME — `what` data-protection by-design outputs realised through `that` NIS 2 acquisition gate + development gate); NIS2↔CRA = COMPLEMENTARY (SAME — entity-side NIS-lifecycle security stacks with maker-side product by-design at supplier-customer boundary); NIS2↔DORA = COMPLEMENTARY (SAME — NSIE maintenance-phase operationalised through DORA change-mgmt six-step); NIS2↔AI_Act = COMPLEMENTARY (SAME — NIS 2 procurement gate on NIS-embedding-AI stacks with AI Act QMS governance gate))
```

### from regs/NIS2.md body

- For an integrated controller-NSIE, NIS 2 acquisition-phase security (supplier SDLC assessment per SR-NIS2-026) realises GDPR Art. 25(1) controller-side by-design outputs (pseudonymised-by-default pipelines, minimisation-by-default); NIS 2 development-phase security (in-house secure-by-design decisions per SR-NIS2-027) implements the by-design outputs in code (D-07.2), CI/CD (D-07.3), and change-management (D-07.4).

### from regs/NIS2.md body

- The 3-phase NIS 2 lifecycle has a 6-phase CRA lifecycle mapping: CRA covers planning/design/development/production/delivery/maintenance; NIS 2 covers acquisition/development/maintenance (NIS 2 acquisition covers the supplier-side SDLC equivalent of CRA planning + design + development + production).


### from regs/NIS2.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # NIS2↔GDPR = Y (controller-NSIE); NIS2↔CRA = Y (NIS 2 entity deploys / manufactures CRA product; supplier-customer boundary); NIS2↔DORA = Y (DORA FE = NSIE — DORA Art. 9(4)(e) operationalises NIS 2 maintenance phase); NIS2↔AI_Act = Y (NIS-embedding-high-risk-AI); HL engages on overlap

```

### from regs/NIS2.md body — field `considerations`

```yaml
  considerations: |
    The NIS 2 secure-by-design obligation is the entity-level lifecycle discipline across 3 coordinated phases (acquisition / development / maintenance) with vulnerability handling and disclosure as the fourth coordinated leg; the operational substrate is supplier-SDLC assessment at acquisition + in-house secure-by-design decisions at development + vulnerability-handling-and-disclosure at maintenance. The `appropriate and proportionate` chapeau from Art. 21(1) propagates with the state-of-the-art floor + Recital 56 cost factor. Art. 20(1) management-body approval + oversight + liability is the upstream governance instrument. The 3-phase NIS 2 lifecycle has a 6-phase CRA lifecycle mapping (CRA covers planning / design / development / production / delivery / maintenance; NIS 2 covers acquisition / development / maintenance) — the two regimes are not 1:1 aligned but stack at the supplier-customer boundary. The NIS 2 maintenance phase is operationalised through DORA Art. 9(4)(e) change-management six-step + Art. 24 testing programme for ICT-hazard subset on DORA FEs (NIS 2 chapeau extends to physical + operational hazards). (Copied from the HSO Considerations block of `### D-07.1.2`; preserved here for self-contained traceability.)
```

### from regs/NIS2.md body

**NIS2 article (verbatim, Art. 21(2)(e)):**

> [as quoted in GDPR ↔ NIS2 above]

<!-- aegis:purity: own_reg=NIS2; demoted=6; core_cross_mentions=2 -->
