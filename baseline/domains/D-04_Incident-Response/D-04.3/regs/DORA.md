# D-04.3 — DORA module

> Regulation-specific layer: applies when `DORA` is in scope
> (activation: `if DORA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| DORA | SO-DORA-008 | Major ICT incident notification to CA + clients | Major ICT incident; financial entity → CA + clients |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **DORA** | major ICT-related incident (Art. 18 classification) | ICT of financial entities | competent authority + clients | Art. 19(1)+(3) | `without undue delay as soon as aware` (4h pending RTS per IR (EU) 2024/2956) |

## Sub-SO (DORA)

#### D-04.3.4 — Sub-SO for DORA

```yaml
id: SO-D-04.3.DORA
subdomain: D-04.3
applies_to: [DORA]
inherits_from: SO-DORA-008
source_SR: SR-DORA-017
activation: if DORA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** A major ICT-related incident is reported to the relevant competent authority without undue delay (Art. 19(1)); affected clients are separately informed without undue delay as soon as the financial entity becomes aware of the major ICT-related incident (Art. 19(3)).

**Considerations.**
- Under the literal OJ text of Art. 19(1), no hard hour-anchor is supplied; the temporal anchor is delegated to the EBA / ESMA / EIOPA RTS under Art. 18(3) and partially addressed in Implementing Regulation (EU) 2024/2956.
- Affected-client notification under Art. 19(3) — and, where the OJ-corrective note in `SR-DORA-017` applies, only when the incident has financial-interest impact on clients.

**CSF anchors (from `SR-DORA-017` v0.3 security_rationale):**
RS.CO-02, RS.MA-04.

---


## Security Requirements (DORA)

#### 4.3.4 — `Without undue delay` major ICT incident notification to CA + affected clients

```yaml
- req_id: 4.3.4
  volere_section: 15
  volere_subtype: audit

  title: "Major ICT-related incident reported to competent authority `without undue delay`; affected clients informed `without undue delay` as soon as financial entity becomes aware — pending EBA/ESMA/EIOPA RTS (4h pending)"

  derives_from:
    hso_sub_so: SO-4.3.DORA
    per_reg_so: SO-DORA-008
    source_sr: SR-DORA-017
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.4"

  description: |
    The product shall report a major ICT-related incident — classified per Art. 18 criteria — to the relevant competent authority without undue delay (Art. 19(1)) and shall separately inform affected clients without undue delay as soon as the financial entity becomes aware of the major ICT-related incident (Art. 19(3)); the temporal anchor is delegated to the EBA / ESMA / EIOPA Regulatory Technical Standards under Art. 18(3) and partially addressed in Implementing Regulation (EU) 2024/2956 (pending 4h preliminary RTS) — for DORA + GDPR overlap the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle (DORA Art. 19(1) + Art. 19(3) + Art. 18(3) RTS delegation + IR (EU) 2024/2956 + Art. 17(1) incident management process).

  fit_criterion: |
    A DORA CA-notification pipeline is operated with parallel CA + client tracks: the CA notification (Art. 19(1)) fires per the EBA/ESMA/EIOPA RTS under Art. 18(3) (Implementing Regulation (EU) 2024/2956 pending 4h preliminary-classification tier; substantive thresholds + content template per RTS when published) — the L1-level preliminary classification within 4h of awareness, the L2 intermediate notification with root cause + recovery actions, and the L3 final notification with full detail once the incident is closed; the affected-client notification (Art. 19(3)) fires without undue delay AS SOON AS the financial entity becomes aware (the literal DORA temporal anchor on the client side), with the OJ-corrective note per `SR-DORA-017` v0.2 audit applying only when the incident has financial-interest impact on clients (where the OJ-corrective note does not reduce the `without undue delay AS SOON AS` trigger to a `where-and-when` construction); the financial entity must document the major-incident classification (Art. 18 + RTS criteria) and the parallel track distinction; the DORA `without undue delay` clock is shorter than GDPR 72h in practice on the CA-notification side once RTS-level granularity is published; for DORA + GDPR overlap on the same event, the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle (the `where feasible` GDPR softening does not survive the DORA multi-reg overlap per CRDA-deep GDPR↔DORA CONDITIONAL-CONTRADICTORY); the DORA Art. 17(1) ICT-related incident management process is the upstream prerequisite (defined, established, implemented — SR-DORA-017 inherits from SR-DORA-016); verified by Art. 18 major-incident classification records inspection + DORA CA-notification logs review + RTS-tier clock-anchor records inspection (4h pending RTS) + DORA client-notification logs review + parallel-track discipline documentation + national-CA + ESA inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.4 (notification clock depends on 4.1 DORA multi-layer + SPOF detection feeding the awareness event), 4.2.4 (notification content requires prior BC-arrangements containment classification + impact assessment feeding Art. 19(1) content template + Art. 19(3) client notification)]

  nist_csf: [RS.CO-02, RS.MA-04]

  applicable_if:
    regs: [DORA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (DORA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).


## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/DORA.md body — field `verified_relationship`

```yaml
verified_relationship: CONDITIONAL (CRDA-deep, D-04.3 GDPR↔DORA: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY; NIS2↔DORA: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY; CRA↔DORA: SCOPE-DISJOINT baseline; DORA↔AI_Act: SCOPE-DISJOINT baseline / CONDITIONAL-CONTRADICTORY)
```

### from regs/DORA.md body

- Where the incident also involves personal data, the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle (CRDA-deep §D-04.3 GDPR↔DORA pair): the `where feasible` softening of GDPR does not survive the multi-reg overlap with DORA.

### from regs/DORA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # DORA↔GDPR = Conditional (Y DORA-FE processes personal data; parallel tracks — DORA `without undue delay` CA + GDPR Art. 33 72h DPA, both fire from same awareness moment; DORA CA-track beats GDPR on clock; the `where feasible` GDPR softening does not survive multi-reg overlap per CRDA-deep); DORA↔NIS2 = Conditional (Y cross-sector; pure-financial entities: DORA absorbs NIS 2 ICT-hazard notification via lex specialis; cross-sector: parallel tracks fire from same awareness moment, NIS 2 chapeau extends to physical+operational); DORA↔CRA = pure SCOPE-DISJOINT (manufacturer ≠ financial entity by default; when DORA FE is also manufacturer, vertical-integration scenario, parallel CRA + DORA reports); DORA↔AI_Act = Conditional (Y FE deploys high-risk AI; parallel tracks — DORA `without undue delay` CA + AI Act 15d/10d/2d MSA, both fire from same awareness moment)

```

### from regs/DORA.md body — field `considerations`

```yaml
  considerations: |
    The DORA notification obligation is the major ICT incident CA notification + affected-client notification; the operational substrate is a DORA CA-notification pipeline with parallel CA + client tracks. Under the literal OJ text of Art. 19(1), no hard hour-anchor is supplied; the temporal anchor is delegated to EBA / ESMA / EIOPA RTS under Art. 18(3) and partially addressed in Implementing Regulation (EU) 2024/2956 (the pending 4h preliminary-classification tier). Where the incident also involves personal data, the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle: the `where feasible` softening of GDPR does not survive the multi-reg overlap with DORA (per CRDA-deep GDPR↔DORA CONDITIONAL-CONTRADICTORY — the DORA `without undue delay` is the operative ceiling). Affected-client notification under Art. 19(3) applies with the OJ-corrective note per `SR-DORA-017` v0.2 audit: only when the incident has financial-interest impact on clients (otherwise the literal `without undue delay AS SOON AS they become aware` triggers, with the corrective note refining only the client-side temporal scope, not the temporal anchor). For pure-financial entities (NIS 2 §9 fall-back does not apply — DORA is lex specialis), DORA absorbs the NIS 2 ICT-hazard notification obligation; the high-level SO does not aggregate across the lex-specialis boundary in that direction. (Copied from the HSO Considerations block of `### 4.3.4`; preserved here for self-contained traceability.)
```

### from regs/DORA.md body

**DORA article (verbatim):**

> Art. 19(1) imposes on financial entities a hard duty to notify the relevant competent authority of any major ICT-related incident, operating in parallel with — and not substituting for — the GDPR Art. 72-hour personal data breach notification under Regulation (EU) 2016/679 Art. 33 and the NIS 2 incident-notification workflow under Directive (EU) 2022/2555 Art. 23, both of which must be triggered under their own criteria where applicable.
> [OJ-corrective note (v0.2 audit, material): Art. 19(3) — trigger condition dropped. OJ Art. 19(3) conditions client notification: `Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients about the major ICT-related incident and about the measures that have been taken to mitigate the adverse effects of such incident.` The SR drops the trigger condition `and has an impact on the financial interests of clients` — converting a conditional obligation into an unconditional one. Every major incident would trigger client notification under the SR; OJ scopes to those with client-financial-impact.]

<!-- aegis:purity: own_reg=DORA; demoted=5; core_cross_mentions=2 -->
