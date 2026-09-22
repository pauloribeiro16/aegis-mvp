# D-07.2 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-046 (partial) | A product with digital elements is designed, developed, and produced to limit attack surfaces — including external interfaces — and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation). | **Product-level outcome mandates** (limit attack surface, mitigate exploitation) — not coding-standard mandates. The CRA-side participation at D-07.2 is **partial** in the SR sense (outcome-level obligations routed from Annex I; no specific coding-standard mandate in OJ). |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | product-coding outcomes (attack-surface + exploitation-mitigation) at the manufacturer side | manufacturer places product on market (Annex I Part I chapeau) + ongoing during support period per Art. 13(8) | `limit its attack surfaces, including attack surfaces of external interfaces` (Annex I Part I (2)(j)) + `reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques` (Annex I Part I (2)(k)) — qualitative outcome mandates, no coding-standard mandate in OJ | market surveillance authority (MSA) — Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record | Annex I Part I chapeau + (2)(j) attack-surface + (2)(k) exploitation-mitigation + Art. 13(1) design/development/production per Annex I Part I + Art. 13(2) risk-assessment propagation across 6 phases + Annex VII §2 + Annex VII §3 |

## Sub-SO (CRA)

#### D-07.2.1 — Sub-SO for CRA

```yaml
id: SO-D-07.2.CRA
subdomain: D-07.2
applies_to: [CRA]
inherits_from: SO-CRA-046
source_SR: SR-CRA-067
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** The manufacturer designs, develops, and produces the product with digital elements to limit its attack surfaces, including attack surfaces of external interfaces (Annex I Part I (2)(j) CRA), and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k) CRA).

**Considerations.**
- `attack-surface limitation` is the outcome-level mandate on product-side coding — minimum-necessary external interfaces, minimum-necessary attack surfaces, and minimum-necessary exploitable paths.
- `exploitation-mitigation` is the outcome-level mandate on product-side incident-impact-reduction — appropriate mechanisms and techniques to reduce the impact of an incident (ASLR, stack-canaries, control-flow integrity, sandboxing, memory-safe language subsystems, bounds checking, least-privilege subsystems, reduced-privilege components as typical mechanisms).
- The CRA-side participation at D-07.2 is partial in the SR sense: OJ Annex I Part I (2)(j) + (2)(k) prescribes outcome-level mandates but does NOT specify secure-coding standards (no coding-language-specific linting, no secure-coding-framework adoption, no NIST SSDF/OWASP SAMM/ISO/IEC 27034 enforcement). The manufacturer builds the coding-standards baseline from industry frameworks (NIST SSDF, OWASP SAMM, ISO/IEC 27034) and demonstrates compliance against the Annex I Part I (2)(j) + (2)(k) outcome-level obligations.
- CRA-side coding-outcomes are demonstrated in Annex VII §2 design/development documentation + Annex VII §3 risk-assessment record (cross to D-09.4 — SO-CRA-059 + SO-CRA-053).
- The Annex I Part I (2) attack-surface + exploitation-mitigation outcomes are propagated downstream from the 6-phase CRA risk-assessment-propagation at D-07.1 (planning + design + development + production + delivery + maintenance) — at the development phase, the coding-outcome decisions are realised through in-house secure-coding decisions.
- For a 5-FTE manufacturer of a CRA-regulated product, the coding-outcomes baseline is built from industry frameworks and demonstrated against Annex I Part I (2)(j) + (2)(k) outcome-level obligations via the Annex VII §2 design/development documentation record.

**CSF anchors (from `SR-CRA-067` v0.3 security_rationale):**
PR.PS-01, PR.PS-02.
*(PR.PS-06 anchors the secure-software-development lifecycle dimension — secure software development practices are integrated, and their performance is monitored throughout the SDLC; the CRA Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation outcomes are realised through the SDLC, with the manufacturer building the coding-standards baseline from industry frameworks. PR.PS-02 anchors the software-maintenance dimension — software is maintained, replaced, and removed commensurate with risk; the Annex I Part I (2)(j) + (2)(k) attack-surface + exploitation-mitigation outcomes are maintained across the support period ≥ 5 years (Art. 13(8) sentence 3) — with ongoing exploitation-mitigation updates + attack-surface monitoring + vulnerability remediation per Art. 13(6) (cross to D-02.2 — SO-CRA-008 + SO-CRA-010). The two subcategories together enable the manufacturer to demonstrate ex post, through the documented Annex VII §2 design/development documentation record + Annex VII §3 risk-assessment record + Annex I Part I (2)(j)/(k) outcome evidence + Art. 13(8) support-period record, that the attack-surface limitation + exploitation-mitigation coding-outcome duties have been exercised with the Annex I Part I essential-requirements anchor + 6-phase risk-assessment propagation.)*

---


## Security Requirements (CRA)

#### 7.2.1 — Product coding outcomes: attack-surface limitation + exploitation-mitigation

```yaml
- req_id: 7.2.1
  volere_section: 15
  volere_subtype: immunity

  title: "Product with digital elements designed, developed and produced to limit attack surfaces (including external interfaces) and to reduce incident impact via exploitation-mitigation mechanisms and techniques"

  derives_from:
    hso_sub_so: SO-D-07.2.CRA
    per_reg_so: SO-CRA-046
    source_sr: SR-CRA-067, SR-CRA-068
    hso_file: ../../HierarchicalSecurityObjectives/D-07_Secure-Development/D-07.2.md
    objective_ref_section: "### D-07.2.1"

  description: |
    The product shall be designed, developed and produced to limit its attack surfaces — including attack surfaces of external interfaces — and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (CRA Annex I Part I (2)(j) + Annex I Part I (2)(k) + Art. 13(1) + Art. 13(2) risk-assessment propagation across 6 lifecycle phases).

  fit_criterion: |
    A documented attack-surface-limitation discipline is maintained per Annex I Part I (2)(j) — minimum-necessary external interfaces (default-closed port suppression, surface-area-baselining), minimum-necessary attack surfaces, minimum-necessary exploitable paths; configuration-management practices are established, documented, and applied to assets per PR.PS-01 with default-closed external interfaces and surface-area-baselining; software is maintained commensurate with risk per PR.PS-02 with risk-assessment-driven attack-surface reduction per Art. 13(2) 6-phase risk-assessment propagation; a documented exploitation-mitigation discipline is maintained per Annex I Part I (2)(k) — appropriate mechanisms and techniques to reduce the impact of an incident (ASLR, DEP/NX, stack canaries, control-flow integrity / CFI, sandboxing, secure enclaves, configuration hardening, principle of least privilege at process level) commensurate with risk per Art. 13(2) risk assessment; the SDLC-process evidence in the technical documentation under Annex VII §2 shows which mitigation mechanisms are in scope for the product and how they are configured; Annex VII §3 risk-assessment record documents the attack-surface + exploitation-mitigation risk-assessment outputs; the coding-practices evidence base is built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034) since OJ Annex I Part I (2)(j) + (2)(k) does NOT specify secure-coding standards (no coding-language-specific linting, no secure-coding-framework adoption prescription); the support period ≥ 5 years per Art. 13(8) sentence 3 is maintained with ongoing exploitation-mitigation updates + attack-surface monitoring + vulnerability remediation per Art. 13(6); for AI-enabled CRA products, CRA Annex I Part I (2)(j) + (2)(k) outcome-level obligations stack with AI Act Art. 15(4)–(5) attack-defence categories — **no OJ-level consolidation rule** exists for coding practices (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices); verified by Annex I Part I (2)(j) attack-surface-limitation evidence audit (default-closed interfaces, surface-area baseline) + Annex I Part I (2)(k) exploitation-mitigation mechanism inventory + Annex VII §2 design/development documentation review + Annex VII §3 risk-assessment record audit + 6-phase risk-assessment-propagation records inspection + Art. 13(6) vulnerability remediation records + Art. 13(8) support-period record + MSA / ENISA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [7.2.3 (when AI-enabled CRA product — CRA Annex I Part I (2)(j)+(k) outcome-level obligations + AI Act Art. 15(4)–(5) AI-attack-defence categories stack vertically with no OJ-level consolidation rule)]

  nist_csf: [PR.PS-06, PR.PS-02]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim, Annex I Part I (2)(j) + (2)(k)):**
> "On the basis of the cybersecurity risk assessment referred to in Article 13(2) … the product with digital elements shall: … (j) limit its attack surfaces, including attack surfaces of external interfaces … (k) reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques." — CRA Annex I Part I (2)(j)+(k)

**CRA article (verbatim, Annex I Part I (2)(j) + (2)(k)):**
> [as quoted above]

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: DIFFERENT-PERSPECTIVE-AT-PROCESS-VS-OUTCOME (CRDA-deep, D-07.2: CRA↔DORA = SAME — COMPLEMENTARY with scope-disjoint qualifier per OJ-literal reading — product-side Annex I Part I (2)(j) + (2)(k) outcome mandate vs entity-side Art. 9(4)(e) change-mgmt process mandate; substantively scope-disjoint in baseline; CRA↔AI_Act = SAME — COMPLEMENTARY with Conditional Y scope overlap on AI-enabled CRA products — CRA Annex I Part I (2)(j) + (2)(k) outcome mandate + AI Act Art. 15(4)–(5) attack-defence categories stack with no OJ-level consolidation rule)
```

### from regs/CRA.md body

- For an AI-enabled CRA product, CRA-side Annex I Part I (2)(j) + (2)(k) outcome mandate stacks with AI Act Art. 15(4)–(5) AI-attack-defence mandate — the two regimes DO NOT substitute; **no OJ-level consolidation rule exists for the coding-practices dimension** (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9, which does not extend to coding practices).

### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔DORA = N typically (manufacturer vs financial-entity; product vs process; scope-disjoint in baseline); CRA↔AI_Act = Conditional Y on AI-enabled CRA products; HL engages only on the Conditional Y integrated stack

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA secure-coding obligation is the product-level coding-outcome mandate at the manufacturer side; the operational substrate is the Annex I Part I (2)(j) attack-surface-limitation discipline (mapped to PR.PS-01 configuration-management + PR.PS-02 software maintenance) + the Annex I Part I (2)(k) exploitation-mitigation discipline (mapped to PR.PS-02 + PR.PS-06 SDLC). The two complementary outcome mandates operate together: (j) reduces what an attacker can reach; (k) reduces what the attacker can do once reached. The CRA-side participation at D-07.2 is **partial** in the SR sense: OJ Annex I Part I (2)(j) + (2)(k) prescribes outcome-level mandates but does NOT specify secure-coding standards (no coding-language-specific linting, no secure-coding-framework adoption, no NIST SSDF/OWASP SAMM/ISO/IEC 27034 enforcement). The manufacturer builds the coding-standards baseline from industry frameworks and demonstrates compliance against the Annex I Part I (2)(j) + (2)(k) outcome-level obligations. For AI-enabled CRA products, CRA-side outcome-level obligations stack with AI Act Art. 15(4)–(5) AI-attack-defence categories with **no OJ-level consolidation rule** (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices). The `complementary` CRDA classification label for CRA↔DORA is more a taxonomy artifact than a substantive relationship — the two regimes do not overlap substantively on coding practices (CRA covers the product, DORA covers the process); the pair is substantively scope-disjoint in baseline. (Copied from the HSO Considerations block of `### D-07.2.1`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=2 -->
