<!-- aegis:case-scope: GDPR, CRA, NIS2, DORA, AI_Act — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-04.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-04.3 Regulatory Notification](../../DomainAnalysis/D-04_Incident-Response/D-04.3.md)
#### D-04.3 Regulatory Notification
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
> **v0.2 update.** Re-written based on the **CRDA-deep** OJ-text-verified analysis
> ([`../../CrossRegulation/_archive/00_CrossRegulation_DeepAnalysis.md`](../../CrossRegulation/_archive/00_CrossRegulation_DeepAnalysis.md),
> [`../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md`](../../CrossRegulation/DeepAnalysis/D-04_Incident-Response/D-04.3.md)). Key changes:
> 1. **Mixed relationship classifications** — 1 SAME (GDPR↔CRA), 1 COMPLEMENTARY
>    (NIS2↔CRA), 1 pure SCOPE-DISJOINT (CRA↔DORA — actor-disjoint baseline, no
>    overlap tension), and 7 with overlap tension (GDPR↔NIS2,
>    GDPR↔DORA, GDPR↔AI_Act, NIS2↔DORA, NIS2↔AI_Act, CRA↔AI_Act, DORA↔AI_Act)
>    classified as SCOPE-DISJOINT baseline / [CONDITIONAL-]CONTRADICTORY on
>    confirmed same-party overlap. The timelines differ
>    (4h / 24h / 72h / 14d / 15d / 1m) because they are different
>    legislative instruments each governing a different recipient; they apply
>    in parallel when the same event triggers multiple regulations, NOT as
>    contradictions on a single recipient.
> 2. **High-level SO reformulated** to reflect the verified-relationship
>    findings: it surfaces the cross-recipient map (5 distinct recipient
>    classes) rather than implying tension.
> 3. **Scope-disjoint test** added: the high-level SO activates only when the
>    event's material scope overlaps with ≥2 applicable regulations' scopes.
> 4. **Validated relationship table** added with 10 pairs, scope-overlap
>    Conditional/SAME/N-typically.
> 5. **Sub-SO annotations updated** to reflect CRDA-deep's actual verified
>    labels per pair (each sub-SO now lists 4 pairs with their verified
>    classifications, not a blanket "SAME").
## D-04.3 Regulatory Notification
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/_archive/00_CrossRegulation_DeepAnalysis.md`](../../CrossRegulation/_archive/00_CrossRegulation_DeepAnalysis.md)
> Part B §D-04.3 (the section that maps to sub-domain D-04.3 in the source file).
> The CRDA-deep verified each of the 10 pairwise cells against the OJ text of
> each regulation. **Key finding:** the 10 pairs are **NOT uniformly SAME** —
> the verified classification is mixed: 1 SAME (GDPR↔CRA — same obligation,
> actor-disjoint baseline), 1 COMPLEMENTARY (NIS2↔CRA — different timelines
> and actors), 1 pure SCOPE-DISJOINT (CRA↔DORA — actor-disjoint baseline, no
> overlap tension), and 7 with overlap tension (GDPR↔NIS2, GDPR↔DORA,
> GDPR↔AI_Act, NIS2↔DORA, NIS2↔AI_Act, CRA↔AI_Act, DORA↔AI_Act) classified
> as SCOPE-DISJOINT baseline / [CONDITIONAL-]CONTRADICTORY on confirmed
> same-party overlap. The apparent timeline divergence
> (4h / 24h / 72h / 14d / 15d / 1m) reflects different legislative instruments
> each governing a different recipient, not contradicting obligations on a
> single recipient. Where the same event triggers ≥2 regulations (genuine
> multi-reg overlap), the timelines apply in parallel.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep D-04.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-010 | 72h SA notification | Personal-data breach; controller → DPA |
| NIS 2 | SG-NIS2-006 | 24h early warning + 72h incident | Significant incident; entity → CSIRT / CA |
| CRA | SG-CRA-024 | 24h/72h/14d AEV progressive disclosure | AEV in product with digital elements; manufacturer → CSIRT + ENISA |
| DORA | SG-DORA-008 | Major ICT incident notification to CA + clients | Major ICT incident; financial entity → CA + clients |
| AI Act | SG-AIACT-013 | 15d / 10d / 2d tiered serious incident reporting | High-risk AI serious incident; provider / deployer → MSA |

## Validated relationships (from CRDA-deep §D-04.3)

#### Validated relationships (from CRDA-deep §D-04.3)
All 10 pairs verified by CRDA-deep as **mixed (not all SAME)** — the
underlying obligation is the same (notify the relevant authority), but the
verified classifications are:
- **1 SAME** (GDPR↔CRA — same obligation, actor-disjoint baseline);
- **1 COMPLEMENTARY** (NIS2↔CRA — different timelines and actors);
- **1 pure SCOPE-DISJOINT** (CRA↔DORA — actor-disjoint baseline, no overlap
  tension);
- **7 with overlap tension** (GDPR↔NIS2, GDPR↔DORA, GDPR↔AI_Act, NIS2↔DORA,
  NIS2↔AI_Act, CRA↔AI_Act, DORA↔AI_Act) classified as SCOPE-DISJOINT
  baseline / [CONDITIONAL-]CONTRADICTORY on confirmed same-party overlap.
The scope-overlap column in the matrix below indicates whether the same
event can trigger both on a single party; this is the gating condition for
the high-level SO to engage.
|   |  GDPR  |  NIS 2  |  CRA  |  DORA  |  AI Act  |
| --- | --- | --- | --- | --- | --- |
|  **GDPR**  |  —  |  Conditional (controller is also NIS 2 NSIE)  |  SAME (controlador ≠ fabricante)  |  Conditional (DORA FE processes personal data)  |  Conditional (high-risk AI processes personal data)  |
|  **NIS 2**  |  Conditional  |  —  |  COMPLEMENTARY (manufacturer is separate party)  |  Conditional (DORA FE is also NSIE)  |  Conditional (NSIE deploys high-risk AI)  |
|  **CRA**  |  SAME  |  COMPLEMENTARY  |  —  |  N typically (manufacturer is separate from FE)  |  Conditional (CRA product embeds high-risk AI)  |
|  **DORA**  |  Conditional  |  Conditional  |  N typically  |  —  |  Conditional (FE deploys high-risk AI)  |
|  **AI Act**  |  Conditional  |  Conditional  |  Conditional  |  Conditional  |  —  |
Legend: **Conditional** = scope overlap only under specific circumstances
(integrated-stack vendor, FE deploying CRA product, etc.); **SAME** = genuine
multi-reg overlap on same event; **N typically** = disjoint in baseline
(manufacturer/controller split, supply-chain hand-off); **COMPARTMENTARY** =
similar obligation, different actor/level.

## Cross-recipient map (5 distinct recipient classes)

#### Cross-recipient map (5 distinct recipient classes)
| Recipient | Triggered by |
|---|---|
| DPA (Data Protection Authority) | GDPR Art. 33(1) |
| CSIRT or Competent Authority | NIS 2 Art. 23(4); CRA Art. 14(1)/(3) |
| Competent Authority (financial) | DORA Art. 19(1)+(3) |
| Market Surveillance Authority (MSA) | AI Act Art. 73(1)–(4) |
| AI Office | AI Act Art. 55 (GPAI) |
When a single event triggers multiple regulations (e.g., a personal data breach
at a financial entity using a CRA-classified high-risk AI product), the entity
must notify **all applicable recipients** with their per-reg clock starting from
the event's trigger moment.
---

## HSO considerations (from D-04.3.0 — High-level SecurityObjective)

**Considerations.**
- Where the same event overlaps with ≥2 regulations' scopes (e.g., a personal data breach at a financial entity using a CRA-classified high-risk AI product), all applicable timelines bind in parallel from the event's trigger moment — the entity must discharge each applicable notification in parallel, using each regulation's own clock and template. The timelines differ (4h / 24h / 72h / 14d / 15d / 1m) because they are different legislative instruments each governing a different recipient; they apply in parallel when the same event triggers multiple regulations, NOT as contradictions on a single recipient.
- The high-level SO surfaces the cross-recipient map across 5 distinct recipient classes (DPA / CSIRT or CA / financial CA / MSA / AI Office) and the parallel-clock binding requirement. The high-level SO does NOT collapse the per-regulation perspective — each regulation's substantive content template and recipient remains distinct; the per-regulation perspective is preserved in the five sub-SOs.
- For events that touch only one regulatory scope, only the triggered sub-SO applies.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 5 participating regulations each define D-04.3 over a **distinct material
scope**; the notification trigger, the recipient, and the legal anchor all
depend on which scope the event falls into.
| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor | Clock |
|---|---|---|---|---|---|
| **GDPR** | personal data breach (Art. 4(12)) | personal data processing | supervisory authority (DPA) | Art. 33(1) | 72h `where feasible` |
| **NIS 2** | significant incident (Art. 23(3) test A+B) | network and information systems | CSIRT or competent authority | Art. 23(4) | 24h early warning → 72h → 1m final |
| **CRA** | actively-exploited vulnerability (Art. 14(1)) OR severe incident (Art. 14(3)) | product with digital elements | CSIRT + ENISA | Art. 14(2)/(4) | 24h → 72h → 14d (AEV) or 24h → 72h → 1m (SI) |
| **DORA** | major ICT-related incident (Art. 18 classification) | ICT of financial entities | competent authority + clients | Art. 19(1)+(3) | `without undue delay as soon as aware` (4h pending RTS per IR (EU) 2024/2956) |
| **AI Act** | serious incident (Art. 3(49), 3 sub-categories) | high-risk AI system (or GPAI for Art. 55) | market surveillance authorities (or AI Office for GPAI) | Art. 73(1)–(4) | 15d default; 10d (death); 2d (widespread infringement) |

## Scope-overlap matrix (5×5)

#### Scope-overlap matrix (5×5)
Whether the material scopes of two regulations can coincide on a single underlying
event is the gating condition for the high-level SO to engage. Y = overlapping
scopes (high-level SO can engage on a single event); Conditional = overlap only
under specific circumstances; N = typically disjoint (high-level SO does NOT
engage by the mere co-applicability of both regulations).
(See the validated-relationships table above for the 5×5 matrix.)

## Worked examples (anchor cases for the matrix above)

#### Worked examples (anchor cases for the matrix above)
- **GDPR ↔ NIS 2 = Y**: a personal data breach at an NIS 2-essential entity is
  simultaneously a personal data breach (GDPR) and a significant incident
  (NIS 2). Same event, two parallel notification tracks.
- **GDPR ↔ CRA = Conditional**: typically disjoint (a CRA-classified product
  sold to a non-GDPR customer only triggers CRA); overlap occurs when the
  product processes personal data — then the personal data breach triggers
  GDPR DPA notification and the AEV triggers CRA CSIRT+ENISA notification.
- **GDPR ↔ DORA = Y**: a personal data breach at a financial entity triggers
  GDPR SA notification and DORA `without undue delay` CA notification; the
  GDPR 72h binds the timeline.
- **GDPR ↔ AI Act = Y**: a serious incident in a high-risk AI system that
  also constitutes a personal data breach triggers GDPR Art. 33 and AI Act
  Art. 73 in parallel.
- **NIS 2 ↔ CRA = Conditional**: typically disjoint (a CRA-classified product
  sold to a non-NIS 2 customer only triggers CRA); overlap occurs when the
  product is deployed by an NIS 2-essential/important entity, so the same
  AEV is both CRA-reportable and NIS 2-reportable.
- **CRA ↔ DORA = N typically** (disjoint in baseline): a CRA-classified product
  is sold by a manufacturer to a separate party (a financial entity), so
  the manufacturer's CRA report and the financial entity's DORA report are
  on different supply-chain legs. Overlap occurs only when the financial
  entity is the integrated manufacturer-controller (vertical-integration
  scenario). In the common case, these are supply-chain hand-offs.
- **CRA ↔ AI Act = Conditional**: the scopes are disjoint by default (CRA
  covers all products with digital elements; AI Act covers only high-risk AI
  systems). Overlap requires the CRA-classified product to embed a high-risk
  AI component — then the AEV triggers CRA and the AI Act serious-incident
  trigger fires in parallel.
- **NIS 2 ↔ DORA = Y**: financial entities are NIS 2-essential entities;
  a major ICT incident at a financial entity is both NIS 2-significant and
  DORA-major.
- **NIS 2 ↔ AI Act = Y**: an NIS 2-essential entity deploying high-risk AI
  triggers both on a serious AI incident.
- **DORA ↔ AI Act = Y**: a financial entity deploying high-risk AI triggers
  both on a serious AI incident affecting its ICT.

## Scope-overlap principle (operational). The high-level SO (`SG-D-04.3.HL`)

#### Scope-overlap principle (operational). The high-level SO (`SG-D-04.3.HL`)
engages on a given event **if and only if the event's material scope overlaps
with the material scope of ≥2 applicable regulations**. Pure co-applicability
of disjoint-scope regulations on the same entity does **not** trigger
cross-regulation aggregation on a single event — see the Activation logic
above. Two single-party events that happen to coincide (e.g., a
breach and a separate vulnerability disclosure on the same day) are distinct
events and do NOT engage the high-level SO.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 5 of 5 regulations participate (GDPR, NIS 2, CRA, DORA, AI Act — the only
  fully-covered 5-track sub-domain in the AEGIS corpus).
- 10 pairwise cells, verified by CRDA-deep as **mixed (not all SAME)**:
  1 SAME (GDPR↔CRA), 1 COMPLEMENTARY (NIS2↔CRA), 1 pure SCOPE-DISJOINT
  (CRA↔DORA), and 7 with overlap tension (GDPR↔NIS2, GDPR↔DORA, GDPR↔AI_Act,
  NIS2↔DORA, NIS2↔AI_Act, CRA↔AI_Act, DORA↔AI_Act) classified as
  SCOPE-DISJOINT baseline / [CONDITIONAL-]CONTRADICTORY on confirmed
  same-party overlap. The dominant pattern is **scope-disjoint baseline with
  conditional contradiction on confirmed same-party overlap** — not blanket
  pairwise contradictions.
- The timelines (4h / 24h / 72h / 14d / 15d / 1m) are different legislative
  instruments each governing a different recipient class; they apply in
  parallel when the same event triggers multiple regulations, NOT as
  contradictions on a single recipient.
- The high-level SO describes the **COMMON OBJECTIVE** (notify the
  applicable recipient(s) of a major security incident); the
  **per-regulation perspective** (timeline, recipient, content template,
  content-rule) is preserved verbatim in the five sub-SOs.
- The high-level SO does **NOT** resolve the timeline/recipient tension — it
  surfaces it as the canonical reconciliation point for **Phase 1C Doc 07**
  (`02_Obligation_Conflict_Resolution.md`). No single binding-procedure
  principle is supplied by the high-level SO; that is a Phase 1C responsibility.
- **Scope caveat (CRITICAL)** — derived from CRDA-deep verified
  classifications: the high-level SO does NOT aggregate across disjoint
  scopes. A SaaS startup with GDPR + CRA applicability does NOT have a
  cross-regulation notification obligation on a single event (the personal
  data breach is a GDPR-only notification; the product vulnerability is a
  CRA-only notification — these are owned by different parties and ride
  on different recipient tracks). The high-level SO activates when the
  **same event** triggers multiple applicable regulations' sub-SOs
  (multi-reg overlap on the same incident), as enumerated in the
  Scope-overlap matrix above. Phase 1A must therefore emit two checks
  before applying the high-level SO: (1) the company has ≥2 applicable
  regulations covering D-04.3, AND (2) the specific incident under
  evaluation has a material scope that overlaps with ≥2 of those
  regulations' scopes. If either check fails, the high-level SO is
  redundant and only the triggered sub-SO(s) apply.
---

## Emergent tensions (from CRDA-deep D-04.3)

#### Emergent tensions (from CRDA-deep D-04.3)
1. **CONDITIONAL on multi-reg overlap** (same event, multiple applicable
   regs): **Five-track timeline divergence with no operationalisation
   principle specified in any one regulation.** Each regulation's clock is
   anchored to a distinct recipient and trigger moment; an entity subject to
   all 5 must maintain a 5-recipient notification pipeline with up to 6
   distinct deadlines (4h DORA / 24h NIS 2 / 24h CRA / 72h GDPR / 14d CRA-AEV
   / 15d AI Act / 1m NIS 2-final). No regulation specifies the
   binding-procedure principle for resolving simultaneous triggers on a
   single event. *Resolution belongs in Phase 1C Doc 07.* When the
   underlying event's scope overlaps with only one applicable regulation's
   scope, this tension does not activate — the single triggered sub-SO
   applies on its own clock.
2. **CONDITIONAL on multi-reg overlap** (same event, multiple applicable
   regs): **Recipient fragmentation exceeds pairwise additivity.** The 5
   regulations notify to 5 distinct recipient classes — **DPA** (GDPR),
   **CSIRT** (NIS 2 / CRA), **CA** (DORA), **MSA** (AI Act high-risk), **AI
   Office** (AI Act GPAI). Pairwise readings treat each pair
   independently; the operational pipeline must allocate events to
   recipients in a single decision. The non-pairwise additivity is the
   *routing complexity* — no single regulation specifies how to route an
   event that satisfies multiple triggers simultaneously (e.g. a NIS
   2-significant incident affecting personal data in a CRA-classified
   product deployed by a financial entity using high-risk AI). Phase 1C
   must codify a recipient-routing matrix. When the event's scope overlaps
   with only one applicable regulation's scope, only the single
   recipient applies — no routing problem arises.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-04.3 — with overlapping
scopes on a single event — must operate to the **shortest clock** across all
applicable timelines + produce **multiple content templates** for **multiple
recipients**. The high-level SO (`SG-D-04.3.HL`) surfaces these tensions but
does NOT resolve them. **Resolution is at design level:** a unified
notification pipeline that generates per-regulation submissions from a single
underlying event record, with the binding-procedure principle (`shortest
clock binds per recipient, but parallel recipients each get their own deadline`)
codified in the company's notification playbook.

## Part 1 §3 — context

### 3. Security Requirements
## 4.3 Regulatory Notification — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md`. See that file for cross-reg verified relationships (CRDA-deep verified 10 pairs — 1 SAME + 1 COMPLEMENTARY + 1 pure SCOPE-DISJOINT + 7 SCOPE-DISJOINT baseline / [CONDITIONAL-]CONTRADICTORY on confirmed same-party overlap; the high-level SO surfaces the 5-recipient cross-recipient map), 5×5 scope-overlap matrix, Objective/Considerations content, timeline divergence (4h / 24h / 72h / 14d / 15d / 1m) across distinct recipient classes (DPA / CSIRT or CA / financial CA / MSA / AI Office), 2 emergent tensions (parallel-clock binding + recipient-routing complexity), and the Phase 1C Doc 07 reconciliation responsibility. **Scope note (P0):** 4.3 is the **only fully-covered 5-track sub-domain** in the AEGIS corpus — all 5 regs participate; the HL aggregates parallel-clock binding across recipients only when the event's material scope overlaps with ≥2 applicable regs' scopes (the lex-specialis carve-out on pure-financial entities applies separately to 4.4). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA, DORA, AI Act (5 of 5 regs — the only fully-covered 5-track sub-domain). CRDA-deep verified 10 pairs as mixed (not uniformly SAME): 1 SAME (GDPR↔CRA), 1 COMPLEMENTARY (NIS2↔CRA), 1 pure SCOPE-DISJOINT (CRA↔DORA), and 7 with overlap tension (GDPR↔NIS2, GDPR↔DORA, GDPR↔AI_Act, NIS2↔DORA, NIS2↔AI_Act, CRA↔AI_Act, DORA↔AI_Act). The five regulators notify to **5 distinct recipient classes** (DPA / CSIRT or CA / financial CA / MSA / AI Office) on **5 distinct timeline patterns** (72h / 24h→72h→1m / 24h→72h→14d / 4h pending RTS / 15d-or-10d-or-2d) — the timelines apply in parallel when the same event triggers multiple recipients, NOT as contradictions on a single recipient. The high-level SO surfaces the common notification duty; the per-regulation perspective (timeline, recipient, content template, content-rule) is preserved verbatim in the five sub-SOs. The DORA `without undue delay` clock delegates the temporal anchor to EBA/ESMA/EIOPA RTS under Art. 18(3) (partially addressed in Implementing Regulation (EU) 2024/2956 pending 4h RTS); the AI Act Art. 73 four-trigger × four-timeline matrix is the most temporally complex notification clause in the AEGIS corpus.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 4.3
  volere_section: 15
  volere_subtype: audit
  title: "Major security incidents notified to all applicable recipients within the per-regulation timelines, with a multi-recipient notification pipeline that discharges parallel clocks on a single underlying event (multi-recipient notification pipeline)"
  derives_from:
    hso_sub_so: SO-4.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-04_Incident-Response/4.3.md
    objective_ref_section: "### 4.3.0"
  description: |
    The product shall notify major security incidents to all applicable recipients — DPA (GDPR Art. 33(1)), CSIRT or competent authority (NIS 2 Art. 23(4); CRA Art. 14(2)/(4)), competent authority (DORA Art. 19(1)) plus clients (Art. 19(3)), MSA (AI Act Art. 73(1)–(4) high-risk), and AI Office (AI Act Art. 55 GPAI) — within each applicable per-regulation timeline (72h `where feasible`; 24h early warning + 72h notification + 1m final; 24h + 72h + 14d AEV or 24h + 72h + 1m SI; `without undue delay` pending RTS 4h; 15d default / 10d death / 2d widespread infringement / 15d causal-link-anchor), via a unified multi-recipient notification pipeline that generates per-regulation submissions from a single underlying event record, where ≥2 of the 5 sub-domain scope-determiners overlap on the same event (per CRDA-deep 10-pair mixed-classification).
  fit_criterion: |
    A unified multi-recipient notification pipeline is operated generating per-regulation submissions from a single underlying event record, with per-recipient clock-start discipline (parallel clocks run from the event's trigger moment, not sequential), per-recipient content-template segregation (the GDPR Art. 33(3) Nature/Categories/Approximate-numbers/Consequences/Measures template is preserved as a GDPR-unique template; the NIS 2 severity/impact/IoC pattern is preserved; the CRA 24h/72h/14d progressive-disclosure content is preserved; the DORA Art. 19(1)+(3) CA + client templates are preserved; the AI Act Art. 73 trigger × timeline matrix is preserved), per-recipient channel gating (DPA / CSIRT or CA / financial CA / MSA / AI Office), per-recipient routing decision recorded against the 5×5 scope-overlap matrix (privacy/confidentiality marker per channel), per-recipient content-rule enforcement (the GDPR Art. 33(1) `unless unlikely to result in a risk` carve-out is preserved as GDPR-unique; the NIS 2 `in any event` ceiling ensures the `where feasible` GDPR softening does not survive multi-reg overlap; the AI Act Art. 73(2) causal-link-anchor `whichever is later` rule is preserved; the DORA `without undue delay` delegates to EBA/ESMA/EIOPA RTS under Art. 18(3) per Implementing Regulation (EU) 2024/2956 pending 4h RTS); the parallel-clock binding principle (shortest clock binds per recipient, but parallel recipients each get their own deadline) is documented in the notification playbook; the recipient-routing complexity (which recipient + which clock) is codified in the recipient-decision matrix; the binding procedure for joint obligations (e.g. personal data breach at a financial entity using a CRA-classified high-risk AI product triggering DPA + CSIRT + financial CA + MSA on one underlying event) is codified; verified by notification-pipeline architecture review + per-recipient clock-anchor records inspection (5 timeline patterns documented separately) + per-recipient content-template coverage audit + recipient-routing-decision matrix inspection + parallel-clock binding-principle documentation review + DPA / CSIRT / CA / MSA / AI Office inspection-ready evidence packs on request.
  priority: MUST
  verification_method: TEST
  dependencies: [4.1 (notification depends on a prior detection-and-triage event feeding the notification trigger — `becoming aware` anchor from 4.1 GDPR leg binds the 72h clock; DORA detection architecture feeds GDPR awareness), 4.2 (notification depends on containment classification for severity/impact content — the 72h tier requires severity+impact assessment per NIS 2 SR-NIS2-011; CRA 72h tier requires nature-of-exploit information per Art. 14(2)(b))]
  nist_csf: [RS.CO-02, RS.MA-04, RS.MA-01, RS.MA-02, RS.MA-03]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA, AI_Act]
    scope_overlap: conditional   # HL engages on the same event only if event's material scope overlaps with ≥2 applicable regs' scopes (CRDA-deep scope-overlap principle); for events touching only one reg, only the triggered sub-SO applies on its own clock
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    4.3 is the **only fully-covered 5-track sub-domain** in the AEGIS corpus; the 5 sub-SOs operate on 5 distinct recipient classes (DPA / CSIRT or CA / financial CA / MSA / AI Office) with 5 distinct timeline patterns. The two emergent tensions (5-track timeline divergence with no operationalisation principle specified in any one regulation; recipient fragmentation exceeds pairwise additivity) are NOT resolved by the high-level SO — they are surfaced as the canonical reconciliation point for Phase 1C Doc 07 (`02_Obligation_Conflict_Resolution.md`). A unified notification pipeline may serve the technical substrate, but the policy and evidence layers must remain recipient-segregated for compliance demonstration. For events that touch only one regulatory scope, only the triggered sub-SO applies on its own clock (no multi-recipient pipeline needed). (Copied from the HSO Considerations block of `### 4.3.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-04.3
title: D-04.3 Regulatory Notification — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.3 Regulatory Notification
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---
> **Deep analysis:** [D-04.3 Regulatory Notification](../../DeepAnalysis/D-04_Incident-Response/D-04.3.md)
#### D-04.3 Regulatory Notification
<!-- participants: GDPR, NIS2, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-010, 011, 012, 013 | 72h SA notification + high-risk subject communication + recipient cascade + prior-consultation trigger | Personal-data breach; controller→DPA→subject |
| NIS2 | SG-NIS2-006, 007, 008, 009, 010, 011, 012 | 24h early warning + 72h notification + 1m final report + TSP derogation + intermediate + recipient + cross-MS | Significant incident; entity→CSIRT→CA→recipients |
| CRA | SG-CRA-023–033 | Two-tier reporting: 24h/72h/14d AEV + 24h/72h/1m severe incident + intermediate + user + voluntary + cross-border | AEV / severe incident; manufacturer→CSIRT+ENISA→users |
| DORA | SG-DORA-008, 009 | Major ICT incident notification to CA + client notification + crisis communication plans | Major ICT incident; financial entity→CA→clients→public |
| AI_Act | SG-AIACT-013, 014 | Tiered serious incident reporting (15d/10d/2d triggers: awareness/causal-link/death/widespread) + GPAI serious incident to AI Office | High-risk AI / GPAI systemic risk; provider/deployer→MSA/AI Office |
**Critical — 5 regulations overlap with DIFFERENT timelines:**
- GDPR: 72h SA + `without undue delay` subject communication
- NIS2: 24h early warning + 72h incident + 1m final + intermediate on CSIRT request
- CRA AEV: 24h early warning + 72h vulnerability notification + 14d final
- CRA severe incident: 24h early warning + 72h incident + 1m final
- DORA: `without undue delay` supervisor + `without undue delay as soon as aware` client
- AI Act high-risk: 15d default + 10d (death) + 2d (widespread infringement)
- AI Act GPAI: `without undue delay` to AI Office
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,NIS2,CRA,DORA,AI_Act -->
- **5-track timeline divergence with no operationalisation principle specified.** GDPR (72h `where feasible`), NIS2 (24h/72h/1m), CRA (24h/72h/14d AEV + 24h/72h/1m SI), DORA (`without undue delay`), AI Act (15d/10d/2d). The pairwise contradictions surface 4 separate timeline conflicts (GDPR↔NIS2, GDPR↔DORA, NIS2↔DORA, NIS2↔AI_Act, CRA↔DORA, CRA↔AI_Act, DORA↔AI_Act), but the *operational consequence* is non-additive: an entity subject to all 5 must maintain a 5-recipient notification pipeline with up to 6 distinct deadlines (24h/2d/72h/14d/15d/1m), and no regulation specifies the binding-procedure principle for resolving simultaneous triggers. Phase 2 must define a binding-procedure rule: the strictest timeline binds per recipient, but parallel recipients (CSIRT vs DPA vs MSA vs AI Office vs CA) each get their own deadline.
- **Recipient fragmentation exceeds pairwise additivity.** The 5 regulations notify to 5 distinct recipient classes (DPA, CSIRT, MSA, competent authority, AI Office) with overlapping but non-identical event triggers. The pairwise readings treat each pair independently, but the operational pipeline must allocate events to recipients in a single decision. The non-pairwise additivity is the *routing complexity* — no single regulation specifies how to route an event that satisfies multiple triggers simultaneously (e.g., a NIS2-significant incident affecting personal data in a CRA-classified product deployed by a financial entity using high-risk AI). Phase 2 must codify a recipient-routing matrix.
<!-- /emergent -->
##### SR cross-validation
NIST CSF 2.0 mapping is dominated by **RS.MA-04** (Incident information shared with stakeholders) and **RS.MA-01/02/03** (Incident management executed at planning/assessment/analysis tiers). GDPR maps to RS.CO-02 (Stakeholders notified of incidents) via the data-subject communication SR-GDPR-019. CRA's user notification SR-CRA-036 maps to RS.CO-03 (Incident details shared with stakeholders). AI Act's tiered triggers (SR-AIACT-022) maps to RS.MA-04 with the temporal differentiation. The CSF 2.0 surface is consistent — no CSF cross-mapping conflict. The conflict is purely at the timeline and recipient level, which is not a CSF construct; it is a regulatory-orchestration concern.
##### Downstream implication
Phase 2 obligation derivation for D-04.3 is the single most complex orchestration problem in the methodology. The output must include: (1) a notification-deadline matrix per regulation, (2) a recipient-routing rule for simultaneous triggers, (3) a binding-procedure principle for conflicting timelines, (4) a per-tier content-requirement schedule (24h early warning content ≠ 72h incident content ≠ 1m final report content). Phase 3 case generation must validate that case companies in the financial-entity / NIS2-essential / high-risk-AI-deployer intersection produce a single unified notification playbook that satisfies all 5 regulations. The 14d CRA AEV final tier (CRA-specific) is a tightening that does not appear in any other regulation; case companies must surface this independently.
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-04.3
title: D-04.3 Regulatory Notification — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-04 Incident Response
sub_domain: D-04.3 Regulatory Notification
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-04_Incident-Response/D-04.3.md
status: DRAFT
---
> **Domain analysis:** [D-04.3 Regulatory Notification](../../DomainAnalysis/D-04_Incident-Response/D-04.3.md)
#### D-04.3 Regulatory Notification
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA, AI_Act

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
