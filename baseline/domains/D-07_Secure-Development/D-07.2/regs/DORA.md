# D-07.2 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | (no OJ-mandated D-07.2 SO; partial via SO-DORA-013 Art. 9(4)(e) — D-07.4 primary) | No dedicated secure-coding mandate in OJ; AEGIS taxonomy §4.1 marks DORA as sole authority but OJ-literal text is silent. **T4-vs-text gap awareness:** T4 maps DORA-C19 (Art. 9(4)(f) patches and updates) to D-07.2 but the OJ text is about patch-management policies, not coding practices. The SR-DORA-023 Art. 9(4)(e) change-management **partially** maps to D-07.2 as inference only (D-07.4 primary). | **Entity-level process** (six-step change management per Art. 9(4)(e) — recorded/tested/assessed/approved/implemented/verified). The DORA-side participation at D-07.2 is **partial** by inference (Art. 9(4)(e) change-mgmt implies secure-coding dimension through testing-vulnerability-assessments + source-code-reviews as part of the testing modalities per Art. 25, but no OJ-mandated coding-standard prescription). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | entity-process change-management six-step (recorded/tested/assessed/approved/implemented/verified) — implicit coding-dimension inference at the financial-entity side (no OJ-mandated secure-coding-standards prescription) | ICT change event at financial entity (Art. 9(4)(e) — software / hardware / firmware / system / security-parameter change) — secure-coding dimension is implicit through the `tested` and `assessed` legs + the Art. 25 testing modalities (source-code-reviews where feasible as one modality) | no OJ coding-standards mandate; implicit coding-dimension via Art. 9(4)(e) change-mgmt six-step `tested` + `assessed` legs + Art. 25 testing modalities; the AEGIS-taxonomy sole-authority assignment has no OJ-text anchor per the P0 disagreement | competent authority (national financial supervisory authority) — Art. 9(4)(e) change-mgmt policy + Art. 25 testing modalities | Art. 9(4)(e) change-mgmt six-step + Art. 25 testing modalities (12-way open list including source-code reviews) — **no OJ Art. 9(4)(f) patches-and-updates prescribing secure-coding standards** |

## Sub-SO (DORA)

#### D-07.2.2 — Sub-SO for DORA

```yaml
id: SO-D-07.2.DORA
subdomain: D-07.2
applies_to: [DORA]
inherits_from: SO-DORA-013 (partial via Art. 9(4)(e) — D-07.4 primary, D-07.2 partial by inference only)
source_SR: SR-DORA-023
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** Financial entities implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters, that are based on a risk assessment approach, in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner (Art. 9(4)(e) DORA — 6-step change-management process).

**Considerations.**
- The secure-coding dimension for DORA is implicit through the `tested` and `assessed` legs of the change-mgmt six-step + the Art. 25 testing modalities (12-way open list including vulnerability assessments, scans, source code reviews where feasible, scenario-based tests, penetration testing, etc.).
- The DORA-side participation at D-07.2 is partial in the SR sense: no OJ mandate prescribes secure-coding standards specifically. The DORA-side coding dimension is derived from the change-mgmt six-step's `tested` + `assessed` legs + the Art. 25 testing modalities (source-code reviews where feasible as one of 12 modalities).
- **P0 disagreement ON PARTICIPATION (preserved as Layer 2 review item):** AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 but this assignment has no OJ-text anchor per CRDA-deep verification (Art. 9(4)(e) is change-management policy; Art. 9(4)(f) is patches-and-updates policy; no OJ clause prescribes secure-coding standards). Either (a) revise the taxonomy to remove the DORA sole-authority assignment, or (b) identify the OJ clause that supports it.
- For a 5-FTE financial entity, the DORA-side coding dimension is demonstrated through: (1) documented Art. 9(4)(e) change-management policies/procedures/controls with the 6-step process; (2) Art. 25 testing programme with the 12-way open testing-modality list; (3) Art. 11(3) response-and-recovery plans + Art. 11(2) backup-policies — NOT through an OJ-mandated secure-coding-standards prescription.
- The DORA-side coding-output is the change-management-evidenced deployed code; the coding-standards baseline itself (NIST SSDF/OWASP SAMM/ISO/IEC 27034) is supplied by the entity's ICT risk-management-policy tier rather than by an OJ mandate.
**CSF anchors (from `SR-DORA-023` v0.3 security_rationale):**
PR.PS-01, PR.PS-02, PR.PS-06.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the DORA Art. 9(4)(e) change-mgmt six-step `tested` + `assessed` legs + Art. 25 testing modalities (source-code reviews where feasible as one of 12 modalities) + Art. 11(3) response-and-recovery plans + the absence of an OJ-mandated secure-coding-standards prescription (per the P0 disagreement ON PARTICIPATION) are the DORA-side coding-practices operational mechanisms that map to PR.PS-06. The DORA-side PR.PS-06 anchor is operationalised through the change-management + testing instruments rather than through an OJ-mandated secure-coding-standards prescription — this is the structurally significant Layer 2 review item (no OJ secure-coding-standards mandate; SR-DORA-023 partial at D-07.2 by inference only). For a 5-FTE financial entity, the PR.PS-06 anchor is demonstrated through the change-management six-step + Art. 25 testing programme outputs without an OJ-mandated secure-coding-standards prescription.)*

---


## Security Requirements (DORA)

#### 7.2.2 — Entity-side change-management six-step with implicit coding-dimension inference (DORA partial — no OJ-mandated secure-coding-standards prescription)

```yaml
- req_id: 7.2.2
  volere_section: 15
  volere_subtype: immunity

  title: "ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified) with implicit coding-dimension inference through tested/assessed legs and Art. 25 testing modalities (DORA partial — no OJ-mandated secure-coding-standards prescription; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary)"

  derives_from:
    hso_sub_so: SO-D-07.2.DORA
    per_reg_so: SO-DORA-013 (partial via Art. 9(4)(e) — D-07.4 primary, D-07.2 partial by inference only)
    source_sr: SR-DORA-023
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.2.md
    objective_ref_section: "### D-07.2.2"

  description: |
    The product shall implement documented policies, procedures and controls for ICT change management — covering changes to software, hardware, firmware components, systems or security parameters — that are based on a risk assessment approach, in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner, with the secure-coding dimension implicit through the `tested` and `assessed` legs of the change-management six-step and the Art. 25 testing modalities (DORA Art. 9(4)(e) — 6-step change-management process + Art. 25 testing programme; **partial at D-07.2, no OJ-mandated secure-coding-standards prescription**).

  fit_criterion: |
    A documented Art. 9(4)(e) change-management policy is maintained covering all change targets (software / hardware / firmware components / systems / security parameters) with the 6-step process (recorded / tested / assessed / approved / implemented / verified in a controlled manner) based on a risk assessment approach; the secure-coding dimension for DORA is implicit through the `tested` and `assessed` legs of the change-management six-step + the Art. 25 testing modalities (12-way open testing-modality list: vulnerability assessments, scans, source code reviews where feasible, scenario-based tests, penetration testing, end-to-end testing, performance testing, compatibility testing, etc.) — source-code reviews where feasible serve as one modality for the secure-coding-dimension inference; the DORA-side participation at D-07.2 is **partial in the SR sense** — no OJ mandate prescribes secure-coding standards specifically; the DORA-side coding dimension is derived from the change-mgmt six-step's `tested` + `assessed` legs + the Art. 25 testing modalities; for a 5-FTE financial entity, the DORA-side coding dimension is demonstrated through (1) documented Art. 9(4)(e) change-management policies/procedures/controls with the 6-step process, (2) Art. 25 testing programme with the 12-way open testing-modality list, (3) Art. 11(3) response-and-recovery plans + Art. 11(2) backup-policies — NOT through an OJ-mandated secure-coding-standards prescription; the coding-standards baseline itself (NIST SSDF/OWASP SAMM/ISO/IEC 27034) is supplied by the entity's ICT risk-management-policy tier rather than by an OJ mandate; **P0 disagreement ON PARTICIPATION** (AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 but CRDA-deep finds no OJ-text support — Art. 9(4)(e) is change-management policy; Art. 9(4)(f) is patches-and-updates policy; no OJ clause prescribes secure-coding standards; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary) — Layer 2 review item; verified by Art. 9(4)(e) change-management policy + procedure + control records review (each ICT change shows recorded / tested / assessed / approved / implemented / verified) + Art. 25 testing-programme records audit (each of the 12 modalities documented including source-code reviews where feasible) + Art. 11(3) response-and-recovery plan + Art. 11(2) backup-policy records inspection + national CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: []   # CRA↔DORA = N typically (scope-disjoint in baseline; manufacturer vs financial-entity, product vs process); DORA↔AI_Act = N typically (scope-disjoint in baseline; financial-entity vs AI-system-provider, process vs AI-system coding); HL engagement NOT activated on baseline

  nist_csf: [PR.PS-06]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).


**DORA article (verbatim, Art. 9(4)(e)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE-AT-PROCESS-VS-OUTCOME (CRDA-deep, D-07.2: CRA↔DORA = SAME — COMPLEMENTARY with scope-disjoint qualifier per OJ-literal reading — product-side Annex I Part I (2)(j) + (2)(k) outcome mandate vs entity-side Art. 9(4)(e) change-mgmt process mandate; substantively scope-disjoint in baseline; DORA↔AI_Act = SAME — COMPLEMENTARY with scope-disjoint qualifier per OJ-literal reading — entity-side change-mgmt process mandate vs AI-system-side attack-defence mandate; substantively scope-disjoint in baseline; **P0 disagreement on AEGIS-taxonomy sole-authority assignment** — AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 but CRDA-deep finds no OJ-text support; Layer 2 review item)
```

### from regs/DORA.md body

- CRDA-deep substantive note: the `complementary` label for CRA↔DORA is more a taxonomy artifact than a substantive relationship — the two regimes do not overlap substantively on coding practices (CRA covers the product, DORA covers the process); the high-level SO does NOT engage on the CRA↔DORA pair in baseline because the pair is substantively scope-disjoint.


### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: N typically   # CRA↔DORA = N typically (scope-disjoint in baseline); DORA↔AI_Act = N typically (scope-disjoint in baseline); HL does NOT engage on baseline 2-of-3 N scope-disjoint pairs; engages only on Conditional Y integrated stack (atypical — DORA FE also CRA manufacturer + AI-enabled CRA product)

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA secure-coding obligation is the financial-entity-side entity-process change-management with implicit coding-dimension inference — **no OJ-mandated secure-coding-standards prescription** is present in DORA; Art. 9(4)(e) text is `documented policies, procedures and controls for ICT change management … recorded, tested, assessed, approved, implemented and verified in a controlled manner`; Art. 9(4)(f) text is `documented policies for patches and updates`; **no OJ clause prescribes secure-coding standards** (no coding-language-specific linting, no secure-coding-framework adoption). AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 — this assignment has no OJ-text anchor per CRDA-deep verification (Layer 2 review item). The DORA-side participation at D-07.2 is preserved as partial per SR-DORA-023 (Art. 9(4)(e) D-07.4 primary, D-07.2 partial by inference only). For a 5-FTE financial entity, the DORA-side coding dimension is demonstrated through the change-management six-step + Art. 25 testing programme outputs (source-code reviews where feasible as one modality) — not through an OJ-mandated secure-coding-standards prescription. The `complementary` CRDA classification labels for CRA↔DORA and DORA↔AI_Act are more taxonomy artifacts than substantive relationships — the two pairs are substantively scope-disjoint in baseline; the high-level SO does NOT engage on these pairs. (Copied from the HSO Considerations block of `### D-07.2.2`; preserved here for self-contained traceability.)
```

### from regs/DORA.md body

**DORA article (verbatim, Art. 9(4)(e)):**

> [as quoted in NIS2 ↔ DORA above]

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=1 -->
