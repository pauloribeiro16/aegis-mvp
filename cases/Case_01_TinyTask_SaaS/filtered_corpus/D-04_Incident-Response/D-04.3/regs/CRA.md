# D-04.3 — CRA module

> Regulation-specific layer: applies when `CRA` is in scope
> (activation: `if CRA in applicable_regs`). Independent of any other
> regulation; cross-regulation material is demoted to the trailing
> 'Cross-references (informational)' section and to [../cross/](../).

| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| CRA | SO-CRA-024 | 24h/72h/14d AEV progressive disclosure | AEV in product with digital elements; manufacturer → CSIRT + ENISA |

| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |
|---|---|---|---|---|
| **CRA** | actively-exploited vulnerability (Art. 14(1)) OR severe incident (Art. 14(3)) | product with digital elements | CSIRT + ENISA | Art. 14(2)/(4) | 24h → 72h → 14d (AEV) or 24h → 72h → 1m (SI) |

## Sub-SO (CRA)

#### D-04.3.3 — Sub-SO for CRA

```yaml
id: SO-D-04.3.CRA
subdomain: D-04.3
applies_to: [CRA]
inherits_from: SO-CRA-024
source_SR: SR-CRA-029
activation: if CRA in applicable_regs
phase_1A_role: 1_of_N
```

**Objective.** An actively-exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours (Art. 14(2)(a), `SR-CRA-029`); vulnerability notification within 72 hours with general information, nature of exploit, mitigations, and user actions (Art. 14(2)(b), `SR-CRA-030`); final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`).

**CSF anchors (from `SR-CRA-029` v0.3 security_rationale):**
RS.MA-02, RS.CO-02.
*(The downstream `SR-CRA-030` 72h/14d tiers add RS.AN-03, RS.AN-07.)*

---


## Security Requirements (CRA)

#### 4.3.3 — AEV three-tier 24h/72h/14d + SI three-tier 24h/72h/1m to CSIRT + ENISA

```yaml
- req_id: 4.3.3
  volere_section: 15
  volere_subtype: audit

  title: "Actively-exploited vulnerability notified on three-tier pattern — 24h early warning + 72h vulnerability notification + 14d final report — to CSIRT + ENISA, with severe-incident (SI) parallel pathway at 24h/72h/1m"

  derives_from:
    hso_sub_so: SO-4.3.CRA
    per_reg_so: SO-CRA-024
    source_sr: SR-CRA-029, SR-CRA-030
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.3"

  description: |
    The product shall notify an actively-exploited vulnerability contained in a product with digital elements — that the manufacturer becomes aware of — on a three-tier temporal pattern: an early warning within 24 hours of the manufacturer becoming aware (Art. 14(2)(a), `SR-CRA-029`); a vulnerability notification within 72 hours with general information, the nature of the exploit, affected products, and available mitigations (Art. 14(2)(b), `SR-CRA-030`); and a final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`); additionally, for severe incidents per Art. 14(3)/(4) a parallel three-tier pathway applies at 24h / 72h / 1m — to the CSIRT designated under Art. 14(2) and to ENISA (CRA Annex I Part I (2)(l) + Part II (4)/(5) + Art. 13(8) + Art. 14(1)/(2)/(3)/(4) + Art. 15 coordinated vulnerability disclosure).

  fit_criterion: |
    An AEV-notification pipeline is operated with dual-pathway discipline (AEV 24h/72h/14d per Art. 14(1); SI 24h/72h/1m per Art. 14(3)/(4)) — the manufacturer designates which Art. 14 leg applies per the AEV-vs-SI classification test; the 24h early-warning tier for AEV fires upon manufacturer awareness of an actively-exploited vulnerability; the 72h vulnerability-notification tier provides the structured content (general information, nature of exploit, affected products, available mitigations, user-actions advice); the 14d final-report tier closes with the corrective/mitigating measure being available (which may be earlier than 14d); for SI the parallel 24h/72h/1m pathway applies; the manufacturer notifies the CSIRT designated under Art. 14(2) and ENISA, with the Art. 15 CVD process enabling coordinated disclosure; the manufacturer documents the personal-data-subset awareness moment feeding GDPR `becoming aware` when the CRA-manufacturer is also a controller (integrated-stack); the product-internal recording from 4.1 CRA leg feeds the AEV-detection trigger; the Art. 14(3)/(4) SI pathway `unlawful OR malicious acts` (R2 distinct terms) preserves both reporting categories independently; the CVD process (Art. 15) coordinates with MSA/CSIRT/ENISA but does not replace the Art. 14 24h/72h/14d tier; verified by AEV-notification logs review + 24h + 72h + 14d clock-anchor records inspection + progressive-disclosure content-template coverage audit (3 tiers) + AEV-vs-SI classification-test documentation + Art. 15 CVD process discipline review + ENISA + CSIRT inspection-ready evidence pack on request.

  priority: MUST
  verification_method: TEST
  dependencies: [4.1.3 (notification clock depends on 4.1 CRA product-internal recording feeding the AEV detection trigger), 4.2.3 (notification content requires prior exploitation-mitigation discipline feeding 72h tier nature-of-exploit section)]

  nist_csf: [RS.MA-02, RS.CO-02, RS.AN-03, RS.AN-07]

  applicable_if:
    regs: [CRA]
  satisfaction:
    controls: []
    nodes: []

```


## Verbatim regulatory basis (CRA)

> OJ-text quotes extracted from the cross-regulation pair analyses
> (single-regulation anchor source; full pairs in [../cross/](../)).

**CRA article (verbatim):**
> Art. 14(2)(a) requires the manufacturer to submit an early warning notification of an actively exploited vulnerability, without undue delay and in any event within 24 hours of the manufacturer becoming aware of it, indicating — where applicable — the Member States on the territory of which the manufacturer is aware that the product has been made available.

**CRA article (verbatim):**
> Art. 14(2)(b) requires the manufacturer to submit, unless the relevant information has already been provided, a vulnerability notification without undue delay and in any event within 72 hours of becoming aware of the actively exploited vulnerability, providing general information about the product, the nature of the exploit and vulnerability, the corrective or mitigating measures taken, and the actions users can take. Art. 14(2)(c) requires a final report no later than 14 days after a corrective or mitigating measure is available, including a description of the vulnerability (severity, impact), information on the malicious actor where available, and details of the security update or other corrective measures.

**CRA article (verbatim):**
> Art. 14(1) requires a manufacturer to notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) — the CSIRT of the Member State where the manufacturer has its main establishment in the Union — and to ENISA, via the single reporting platform established under Art. 16.

**CRA article (verbatim):**
> Art. 14(3) requires the manufacturer to notify any severe incident having an impact on the security of the product with digital elements that it becomes aware of, simultaneously to the CSIRT designated as coordinator under Art. 14(7) and to ENISA, via the single reporting platform.

## Cross-references (informational)

> Moved verbatim from the module body by `modularize_domains.py` (mechanical
> demotion). These units mention other regulations and are NOT part of this
> regulation's independent obligations. Cross-regulation reasoning lives in
> [`../cross/`](../). Nothing has been rewritten or deleted.

### from regs/CRA.md body — field `verified_relationship`

```yaml
verified_relationship: CONDITIONAL (CRDA-deep, D-04.3 GDPR↔CRA: SAME; NIS2↔CRA: COMPLEMENTARY; CRA↔DORA: SCOPE-DISJOINT baseline; CRA↔AI_Act: SCOPE-DISJOINT baseline / CONTRADICTORY)
```

### from regs/CRA.md body

**Considerations.**

- The 14-day AEV final tier is CRA-unique and tighter than any NIS 2 / DORA tier. CRA introduces a separate severe-incident (SI) pathway (24h / 72h / 1m) for non-AEV severe incidents per Art. 14(3)/(4).


### from regs/CRA.md body — field `scope_overlap`

```yaml
    scope_overlap: Conditional   # CRA↔GDPR = SAME (controlador ≠ fabricante by default; when integrated manufacturer-controller or CRA product processes personal data, GDPR `where feasible` softening does not survive multi-reg overlap with NIS 2 if NIS 2 also applies, but CRA absorbs the AEV leg); CRA↔NIS2 = COMPLEMENTARY (manufacturer-disjoint baseline; AEV ↔ significant-incident is different reporting scope; when manufacturer is also deployer, AEV and significant incident are reported on different legs, with AEV to CSIRT+ENISA and significant incident to CSIRT + CA); CRA↔DORA = pure SCOPE-DISJOINT (manufacturer ≠ financial entity by default; no overlap tension; when DORA FE is also manufacturer, vertical-integration scenario, parallel CRA + DORA reports); CRA↔AI_Act = Conditional (CRA product embeds high-risk AI component; AEV + Art. 73 serious incident run on different legs)

```

### from regs/CRA.md body — field `considerations`

```yaml
  considerations: |
    The CRA notification obligation is the AEV three-tier 24h/72h/14d + the SI parallel pathway 24h/72h/1m; the operational substrate is an AEV-notification pipeline with dual-pathway discipline (AEV vs SI). The 14-day AEV final tier is CRA-unique and tighter than any NIS 2 / DORA tier (NIS 2 final at 1m; DORA delegates to RTS); CRA introduces a separate severe-incident (SI) pathway for non-AEV severe incidents per Art. 14(3)/(4). The manufacturer is the typical obliged actor, but the deployer-side oversight under the NIS 2 leg requires the deployer to independently notify if the manufacturer's report does not propagate (downstream 4.3 NIS 2 leg). The Art. 15 CVD process coordinates with MSA / CSIRT / ENISA but does not replace the Art. 14 24h/72h/14d tier; the manufacturer's CVD policy (Art. 15(1)) enables structured vulnerability intake from external researchers. The Art. 14(2) recipient is the CSIRT designated under Art. 14(2) (single-entry-point per MS) plus ENISA (institutional recipient — receives copies per Art. 14(2)). For events that touch only one regulatory scope (e.g. CRA-only vulnerability disclosure without personal-data, NIS 2, DORA or AI Act overlap), only the CRA AEV + SI pathway applies on its own clock. (Copied from the HSO Considerations block of `### 4.3.3`; preserved here for self-contained traceability.)
```

<!-- aegis:purity: own_reg=CRA; demoted=4; core_cross_mentions=1 -->