<!-- aegis:case-scope: GDPR, CRA, NIS2, AI_Act — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-01.4 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-01.4 Data Integrity Mechanisms](../../DomainAnalysis/D-01_Data-Protection/D-01.4.md)
#### D-01.4 Data Integrity Mechanisms
<!-- participants: GDPR, CRA, DORA, AI_Act (partial) -->
**Participants (from CRDA):** GDPR, CRA, DORA, AI_Act (partial via Art. 15(3) backup/fail-safe plans in SR-AIACT-015); NIS2 absent.

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md`](../../CrossRegulation/DeepAnalysis/D-01_Data-Protection/D-01.4.md)
> (6 pairs verified against OJ text; CRDA initial classifications included 4
> COMPLEMENTARY + 1 EQUAL + 2 DIFFERENT PERSPECTIVE — all corrected to SAME
> after OJ-text analysis; CRA↔DORA was EQUAL and remained SAME on
> correction).

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-01.4)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-003 | Personal data accurate and, where necessary, kept up to date; every reasonable step to ensure erasure/rectification without delay | Controller/processor; Art. 5(1)(d) accuracy + Art. 16 rectification + Art. 5(1)(f) integrity; personal-data scope; semantic accuracy (workflow leg) + storage integrity |
| CRA | SG-CRA-005 | Integrity of stored/transmitted/processed data + commands/programs/configuration protected against any manipulation not authorised by the user; corruption reported | Manufacturer; Annex I Part I (2)(f) integrity + (2)(l) logging; product-level; "personal or other"; technical integrity (universal-quantifier "any manipulation") |
| DORA | SG-DORA-001 (cross-ref) | Integrity is one dimension of the 4×3 CIA+A matrix (at rest, in use, in transit) | Financial entity; Art. 9(2) CIA+A 4-way AND + 3-way OR of data states; ICT-system-level; `high standards`; OJ-explicit integrity dimension |
| AI Act | SG-AIACT-009 (partial) | High-risk AI systems resilient as possible regarding errors, faults, inconsistencies — technical redundancy (backup or fail-safe plans) | Provider; Art. 15(3); AI-system-level; resilience-not-integrity framing; AI-system-level property bundled with accuracy and robustness |

## Validated relationships (from CRDA-deep §D-01.4)

#### Validated relationships (from CRDA-deep §D-01.4)
All 6 pairs verified by CRDA-deep as **SAME** (CRDA-deep corrected CRDA's
initial mixed classifications — 4 COMPLEMENTARY + 1 EQUAL (CRA↔DORA, which
was already aligned) + 2 DIFFERENT PERSPECTIVE (GDPR↔AI_Act,
DORA↔AI_Act) — all to SAME after OJ-text analysis). The underlying
obligation is the same (preserve the integrity property of data against
unauthorised modification, and detect/report corruptions); the pairs
differ on the **primary object** (GDPR = personal-data semantic accuracy +
storage integrity; CRA = data + commands + programs + configuration
technical integrity; DORA = ICT-system CIA+A integrity cell; AI Act =
AI-system resilience to errors/faults/inconsistencies) and on the **layer**
(personal-data workflow leg vs storage/perimeter leg vs ICT-system leg vs
AI-system leg). The objects are **nested, not disjoint**: CRA integrity sits
inside DORA CIA+A, which sits inside GDPR personal-data accuracy, which is
a sub-property of AI Act system resilience. A harmonised compliance system
must document each object separately rather than collapsing the four into a
single "integrity" claim. CRDA-deep explicitly notes (GDPR↔AI_Act pair):
the objects are nested — AI-system resilience sits inside the storage
stack that GDPR's PR.DS-01 protects; GDPR accuracy sits inside the AI-system
lifecycle that Art. 15(1) constrains.
The scope-overlap column in the matrix below indicates whether the same
data asset can trigger both regulations on a single party; this is the
gating condition for the high-level SO to engage.
|   |  GDPR  |  CRA  |  AI Act  |
| --- | --- | --- | --- |
|  **GDPR**  |  —  |  Y (CRA product stores personal data — typical); disjoint in baseline as manufacturer ≠ controller  |  Y (high-risk AI processes personal data — typical)  |
|  **CRA**  |  Y  |  —  |  Y (CRA-regulated product is also high-risk AI — edge-AI scenario); disjoint in baseline as CRA universal ↔ AI Act high-risk-only  |
|  **AI Act**  |  Y  |  Y  |  —  |
Legend: **Y** = scope overlap on the same data asset (high-level SO can
engage on a single data asset). CRDA-deep scope-disjoint tests: all 6
pairs verified as Y. The CRA↔AI_Act edge-AI scenario is the only
scope-overlap case that requires integrated manufacturer-controller
treatment; the other pairs overlap on the typical SaaS/financial/AI deployment.

## Cross-recipient map

#### Cross-recipient map
N/A — D-01.4 (data integrity mechanisms) does not involve distinct
recipient classes (same as D-01.1, D-01.2, D-01.3). The recipients are
supervisory authorities for compliance demonstration on inspection only
(GDPR SA, CRA MSA, DORA CA + ESAs, AI Act conformity-assessment body +
MSA). The Art. 73 serious-incident reporting (AI Act) and the DORA Art. 19
major-ICT-related-incident reporting and the GDPR Art. 33 breach
notification (when integrity failure is a personal-data breach) are
distinct obligations routed through D-04.3, not D-01.4. The CRA Art. 14(3)
severe-incident notification (when corruption escalates to severe incident)
is also routed through D-04.3, not D-01.4. The D-04.3 sub-domain is the
canonical recipient-fragmentation locus for the data-protection area.
---

## HSO considerations (from D-01.4.0 — High-level SecurityObjective)

**Considerations.**
- The four participating regulations converge on the same substantive
  obligation (integrity of data) but each operates at a distinct object
  layer on the same data asset: GDPR's semantic accuracy + storage integrity
  (Art. 5(1)(d) accuracy + Art. 16 rectification cascade + Art. 5(1)(f)
  integrity), CRA's technical integrity with universal-quantifier protection
  (Annex I (2)(f) integrity of data + commands + programs + configuration
  against `any manipulation or modification not authorised by the user` +
  (2)(l) corruption reporting), DORA's ICT-system CIA+A integrity cell
  (Art. 9(2) 4-way CIA+A × 3-way data states), and AI Act's AI-system
  resilience (Art. 15(3) `as resilient as possible regarding errors, faults
  or inconsistencies` with backup/fail-safe plans as one permissible means).
- The objects are nested: CRA integrity sits inside DORA CIA+A, which sits
  inside GDPR personal-data accuracy, which is a sub-property of AI Act
  system resilience.
- CRDA-deep verified all 6 pairs as SAME — a single integrity stack
  (PR.DS-01 + PR.DS-10 + PR.PS-04 — cryptographic hashes, MACs, write-audit
  logging, corruption reporting, integrity-checked storage) + documented
  rectification workflow (Art. 16 cascade + Art. 19 recipients notification)
  discharges all four obligations on the same data asset when the per-reg
  objects are documented separately.
- The high-level SO describes the common obligation (integrity of data
  against unauthorised modification, with corruption detected/logged/
  reported); the per-regulation perspective is preserved in the four
  sub-SOs (primary object, scope qualifier, recipient, content template).
- For assets touching only one regulatory scope, only the triggered sub-SO
  applies.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-01.4 over a distinct
**primary object**; the integrity obligation, the trigger, the recipient,
and the legal anchor all depend on which object the asset falls into.
| Axis (reg) | Trigger | Primary object | Recipient | Legal anchor |
|---|---|---|---|---|
| **GDPR** | continuous + on Art. 16 request | personal-data semantic accuracy + storage integrity | supervisory authority (DPA) + data subjects (Art. 16) | Art. 5(1)(d) + Art. 5(1)(f) + Art. 16 + Art. 19 cascade |
| **CRA** | continuous + corruption-event reporting | data + commands + programs + configuration (universal quantifier) | user / administering party (corruption report) | Annex I Part I (2)(f) + (2)(l) |
| **DORA** | continuous + annual scenario review (Art. 7(2)) | ICT-system CIA+A (4×3 matrix; integrity cell) | national CA + ESAs | Art. 9(2) |
| **AI Act** | continuous + lifecycle (Art. 15(1)) | AI-system resilience to errors/faults/inconsistencies | conformity-assessment body (ex ante) + MSA (ex post) + AI Office for GPAI | Art. 15(3) |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-01.4.HL`) engages on a given data asset **if and only if ≥2
applicable regulations' primary-object scopes overlap on the same data
asset** (e.g. personal data stored on a CRA-regulated product deployed by
a DORA financial entity running a high-risk AI workload that processes
the personal data — a vertically-integrated manufacturer-controller on a
financial-services stack with an AI-system layer above). The nested-object
framing means the engagement is **layered**: the high-level SO describes the
common obligation, and the four sub-SOs each anchor a distinct object layer
that the company must document separately. Pure co-applicability of
disjoint-scope regulations on different data assets does **not** trigger
cross-regulation aggregation — see the Activation logic in the file header.
For a 5-FTE SaaS startup with GDPR + CRA applicability but no DORA / AI Act
applicability, only the GDPR and CRA sub-SOs activate; the high-level SO
engages on the same data asset when both apply. For a DORA financial entity
deploying high-risk AI that processes personal data, the high-level SO
engages on all four layers (personal-data accuracy + product-side
technical integrity + ICT-system integrity cell + AI-system resilience) on
the same data asset.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- 4 of 5 regulations participate (GDPR, CRA, DORA, AI Act partial via Art.
  15(3); NIS 2 absent per AEGIS taxonomy §4.1 — NIS 2 does not impose
  data-integrity mechanisms as a standalone obligation; CRA + DORA are
  dedicated authorities).
- 6 pairwise cells, verified by CRDA-deep as **all SAME** after OJ-text
  analysis: GDPR↔CRA (CORRECTED from COMPLEMENTARY), GDPR↔DORA (CORRECTED
  from COMPLEMENTARY), GDPR↔AI_Act (CORRECTED from DIFFERENT PERSPECTIVE),
  CRA↔DORA (CORRECTED from EQUAL — no change in classification, only
  verified), CRA↔AI_Act (CORRECTED from COMPLEMENTARY), DORA↔AI_Act
  (CORRECTED from DIFFERENT PERSPECTIVE).
- The four regulations impose the **same substantive obligation** (data
  integrity) at different **object layers**: GDPR (personal-data semantic
  accuracy + storage integrity), CRA (data + commands + programs +
  configuration technical integrity with universal-quantifier), DORA (ICT
  system CIA+A integrity cell), AI Act (AI-system resilience to
  errors/faults/inconsistencies). The objects are **nested**: CRA integrity
  sits inside DORA CIA+A, which sits inside GDPR personal-data accuracy,
  which is a sub-property of AI Act system resilience.
- The high-level SO describes the **COMMON OBJECTIVE** (integrity of data
  against unauthorised modification, with corruption detected/logged/reported);
  the **per-regulation perspective** (primary object, scope qualifier,
  recipient, content template) is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional tension — there
  are 0 conditional emergent tensions in this sub-domain; CRDA-deep
  verified all 6 pairs as SAME. Phase 1C Doc 07 does not need to resolve
  contradictions on D-01.4 because none exist; the task is to **document
  the layered objects** so that each per-reg layer is discharged
  separately on the same data asset.
- **Scope caveat (CRITICAL — layered-object framing)** — derived from
  CRDA-deep verified classifications: the high-level SO does NOT collapse
  the four primary objects into a single "integrity" claim. The objects
  are nested but distinct: GDPR's semantic accuracy (workflow leg) is a
  controller obligation beyond CRA's technical-integration scope; CRA's
  universal-quantifier integrity (commands + programs + configuration) is
  a product-side obligation beyond GDPR's data-only scope; DORA's CIA+A
  integrity cell is an ICT-system-level obligation beyond CRA's product-side
  scope; AI Act's resilience (backup/fail-safe plans) is an AI-system-level
  obligation beyond DORA's ICT-system scope. A harmonised compliance system
  must document each object separately rather than collapsing the four into
  a single "integrity" claim. Phase 1A must therefore emit **four checks
  before applying the high-level SO** (one per participating regulation)
  to confirm that the per-reg object layer is documented; the high-level
  SO surfaces the common obligation but does NOT aggregate the layered
  objects.
---

## Emergent tensions (from CRDA-deep §D-01.4)

#### Emergent tensions (from CRDA-deep §D-01.4)
None — sub-domain is **all-SAME in baseline (6 pairs verified as SAME
after OJ-text analysis; CRDA initial 4 COMPLEMENTARY + 1 EQUAL + 2
DIFFERENT PERSPECTIVE classifications corrected to SAME)**. No conditional
emergent tensions. The **object-layer divergence** (GDPR personal-data
semantic accuracy + storage integrity; CRA data + commands + programs +
configuration technical integrity; DORA ICT-system CIA+A integrity cell; AI
Act AI-system resilience to errors/faults/inconsistencies) is **layered
in object, not contradictory in scope** — the four objects are nested (CRA
integrity sits inside DORA CIA+A, which sits inside GDPR personal-data
accuracy, which is a sub-property of AI Act system resilience). The
operational convergence is on **PR.DS-01 (storage integrity) + PR.DS-10
(in-use integrity) + PR.PS-04 (log records)**, with each regulation adding
its layer-specific anchor (GDPR's ID.AM-08 data-quality workflow + Art. 16
rectification; CRA's PR.PS-04 corruption reporting + (2)(l) logging;
DORA's PR.DS-02 in-transit integrity + ID.AM-08 risk-strategy; AI Act's
PR.IR-03 / PR.IR-04 / PR.DS-11 resilience + backup). The strictest
operational surface (DORA's ICT-system integrity + CRA's universal-quantifier
protection on the product substrate) covers the storage-integrity leg;
GDPR's accuracy workflow + AI Act's resilience plan are layered above. The
high-level SO surfaces the common obligation; the per-reg objects are
documented separately rather than collapsed into a single "integrity" claim.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-01.4 — with
overlapping scopes on the same data asset — operates a **single integrity
stack (PR.DS-01 + PR.DS-10 + PR.PS-04) + documented rectification workflow
(Art. 16 + Art. 19)** that discharges all obligations on the layered objects.
The high-level SO (`SG-D-01.4.HL`) describes the common obligation (data
integrity against unauthorised modification, with corruption detected/logged/reported);
the per-reg perspective is preserved in the four sub-SOs (primary object,
scope qualifier, recipient, content template). **No conflict-resolution is
required on D-01.4 because CRDA-deep verified all 6 pairs as SAME** — the
resolution work is at the **layered-object documentation** level: the
company profile must document integrity at four distinct object levels
(personal-data, ICT-system, AI-system, configuration) and the cascade
between them. Phase 1C Doc 07 documents the **layered-object strategy**:
(1) integrity stack (PR.DS-01 + PR.DS-10 + PR.PS-04 — cryptographic hashes,
MACs, write-audit logging, corruption reporting); (2) per-recipient
documentation of each object layer (GDPR accuracy workflow + Art. 16
cascade, CRA universal-quantifier + corruption report, DORA CIA+A
integrity cell, AI Act resilience + backup/fail-safe); (3) cross-references
between the layered objects (CRA integrity substrate under DORA CIA+A,
under GDPR accuracy workflow, under AI Act resilience). **Proportionality
(P2):** a non-AI, non-DORA SaaS handles the GDPR + CRA floor (PR.DS-01 +
PR.DS-10 + PR.PS-04 + Art. 16 rectification workflow); a DORA financial
entity adds the system-level integrity layer (ID.AM-08 risk-strategy + DORA
Art. 9(2) 4×3 matrix); a DORA financial entity using high-risk AI adds the
AI-system resilience layer (PR.IR-03 + PR.IR-04 + PR.DS-11 + Art. 15(3)
backup/fail-safe). For proportionality, D-01.4 is a **layered-object**
sub-domain: a small SaaS with GDPR + CRA applicability meets the floor
without dedicated investment beyond the standard at-rest encryption stack;
the DORA + AI Act depth layers are the costly additions for financial
entities using high-risk AI.

## Part 1 §3 — context

### 3. Security Requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md`. See that file for cross-reg verified relationships, scope overlap matrix, Objective/Considerations content, and aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, CRA, DORA, AI_Act (4 of 5 regs; NIS 2 absent per AEGIS taxonomy §4.1 — NIS 2 does not impose data-integrity mechanisms as a standalone obligation; CRA + DORA are dedicated authorities; AI Act adds partial resilience dimension via Art. 15(3)). CRDA-deep verified 6 pairs as all-SAME (CRDA initial 4 COMPLEMENTARY + 1 EQUAL + 2 DIFFERENT PERSPECTIVE classifications corrected to SAME after OJ-text analysis).
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 1.4
  volere_section: 15
  volere_subtype: integrity
  title: "Data integrity preserved against unauthorised modification across the data lifecycle (multi-reg aggregation)"
  derives_from:
    hso_sub_so: SG-D-01.4.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-01_Data-Protection/D-01.4.md
    objective_ref_section: "### D-01.4.0"
  description: |
    The product shall preserve data integrity against unauthorised modification across the data lifecycle — at rest, in transit, and in use — with corruption detected, logged, and reported, and with semantic accuracy maintained as the workflow leg of the personal-data principle, as the common substantive obligation converging across GDPR Art. 5(1)(d)+(f) + Art. 16 + Art. 19, CRA Annex I Part I (2)(f)+(l), DORA Art. 9(2), and AI Act Art. 15(3) where ≥2 of these scopes overlap on the same data asset.
  fit_criterion: |
    An integrity stack (PR.DS-01 cryptographic hashes + PR.DS-10 in-use integrity controls + PR.PS-04 write-audit log records + corruption reporting) is in place on the data asset; corruption events are detected (via hash/MAC validation on reads + signed-firmware / control-flow integrity in use) and surfaced as log records suitable for continuous monitoring; per-reg object layers are documented separately (GDPR semantic-accuracy workflow + Art. 16 rectification cascade + Art. 19 recipient-cascade; CRA universal-quantifier protection covering data + commands + programs + configuration with corruption reporting to user/administering party; DORA ICT-system CIA+A integrity cell of the 4×3 matrix; AI Act resilience to errors/faults/inconsistencies with backup/fail-safe plans where high-risk AI applies); verified by automated integrity-check audit (hash/MAC verification) + manual log-records review + per-reg documentation pack + joint risk-assessment artefact citing all four legal anchors when scopes overlap; proportionality (P2): non-AI / non-DORA SaaS meets GDPR + CRA floor; DORA financial entity adds ICT-system integrity layer; DORA + AI Act adds AI-system resilience layer.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08, PR.PS-04, PR.IR-03, PR.IR-04]
  applicable_if:
    regs: [GDPR, CRA, DORA, AI_Act]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs' primary-object scopes overlap on same data asset (see HSO scope-overlap principle)
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations converge on the same substantive
    obligation (data integrity against unauthorised modification, with
    corruption detected/logged/reported) but each operates at a distinct
    object layer on the same data asset: GDPR's semantic accuracy + storage
    integrity (Art. 5(1)(d)+(f) + Art. 16 + Art. 19 cascade), CRA's
    technical integrity with universal-quantifier protection (Annex I
    (2)(f) + (2)(l) corruption reporting), DORA's ICT-system CIA+A
    integrity cell (Art. 9(2) 4-way AND × 3-way OR of data states), and
    AI Act's AI-system resilience (Art. 15(3) backup/fail-safe plans). The
    objects are nested (CRA integrity sits inside DORA CIA+A, which sits
    inside GDPR personal-data accuracy, which is a sub-property of AI Act
    system resilience) — the high-level SO surfaces the common obligation
    but the per-reg object layers must be documented separately rather than
    collapsed into a single `integrity` claim. CRDA-deep verified all 6
    pairs as SAME. (Copied from the HSO Considerations block of
    `### D-01.4.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-01.4
title: D-01.4 Data Integrity Mechanisms — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.4 Data Integrity Mechanisms
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-01_Data-Protection/D-01.4.md
status: DRAFT
---
> **Deep analysis:** [D-01.4 Data Integrity Mechanisms](../../DeepAnalysis/D-01_Data-Protection/D-01.4.md)
#### D-01.4 Data Integrity Mechanisms
<!-- participants: GDPR, CRA, DORA, AI_Act -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SG-GDPR-003 / SG-GDPR-014 | Personal data accurate and up to date; availability and access restored in a timely manner | Controller/processor; Art. 5(1)(d) accuracy + Art. 16 rectification + Art. 32(1)(b)/(c) resilience |
| CRA | SG-CRA-005 | Integrity of stored/transmitted/processed data + commands/programs/configuration protected against unauthorised manipulation, with corruption reported | Manufacturer; Annex I Part I (2)(f)+(l); product-level; "personal or other" |
| DORA | SG-DORA-001 (cross-ref) | Integrity is one dimension of the 4×3 CIA+A matrix | Financial entity; Art. 9(2); ICT-system scope; OJ-explicit integrity dimension |
| AI_Act | SG-AIACT-009 (partial) | High-risk AI systems as resilient as possible regarding errors, faults or inconsistencies — technical redundancy (backup, fail-safe) | Provider; Art. 15(3); AI-system-level; resilience-not-integrity framing |
| NIS2 | — | Out-of-scope for D-01.4 (NIS 2 does not impose integrity controls as a standalone obligation; CRA + DORA are dedicated authorities) | n/a |
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
##### Emergent tensions (3+ regulations)
<!-- emergent: GDPR,CRA,DORA,AI_Act -->
- The four regulations have **different primary objects for integrity**: GDPR (personal data semantic accuracy), CRA (data + commands + programs + configuration technical integrity), DORA (ICT system CIA+A integrity), AI Act (AI system resilience to errors/faults/inconsistencies). The objects are nested: CRA integrity sits inside DORA CIA+A, which sits inside GDPR personal-data accuracy, which is a sub-property of AI Act's system resilience. A harmonised compliance system must document each object separately rather than collapsing the four into a single "integrity" claim.
- **NIS 2 absence.** All four other regulations impose an integrity obligation; NIS 2 is silent on the standalone integrity dimension (T3-vs-text gap; CRA + DORA are dedicated authorities). For a NIS 2 NSIE that is not also DORA-scoped, the integrity obligation is anchored to NIS 2's broader risk-management framework rather than to a dedicated integrity clause. This is a **regulatory gap** that the AEGIS taxonomy should surface for Layer 2 review.
<!-- /emergent -->
##### SR cross-validation
CSF mappings converge on PR.DS-01 (data-at-rest) and PR.DS-10 (data-in-use) for the data integrity property. CRA additionally anchors on PR.PS-04 (logging); DORA on ID.AM-08 (risk-strategy); AI Act on PR.IR-03 + PR.IR-04 (resilience) + PR.DS-11 (data backup consistency). GDPR adds ID.AM-08 (data managed consistent with risk strategy) for the accuracy-side workflow. The shared PR.DS-01 + PR.DS-10 anchor is the operational pivot; divergence is at the supplementary layer (semantic accuracy / technical integrity / system resilience).
##### Downstream implication
For Phase 1C Doc 07, D-01.4 is a **layered object** sub-domain: the company profile must document integrity at four distinct object levels (personal-data, ICT-system, AI-system, configuration) and the cascade between them. Proportionality: a non-AI, non-DORA SaaS handles the GDPR + CRA floor; a DORA financial entity adds the system-level layer; a DORA financial entity using high-risk AI adds the AI-system layer.
---
### D-02 Vulnerability Management
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-01.4
title: D-01.4 Data Integrity Mechanisms — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-01 Data Protection & Encryption
sub_domain: D-01.4 Data Integrity Mechanisms
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-01_Data-Protection/D-01.4.md
status: DRAFT
---
> **Domain analysis:** [D-01.4 Data Integrity Mechanisms](../../DomainAnalysis/D-01_Data-Protection/D-01.4.md)
#### D-01.4 Data Integrity Mechanisms
<!-- participants: GDPR, CRA, DORA, AI_Act (partial) -->
**Participants (from CRDA):** GDPR, CRA, DORA, AI_Act (partial via Art. 15(3) backup/fail-safe plans in SR-AIACT-015); NIS2 absent.

## Part 3 — context

### D-02 Vulnerability Management
---

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)
