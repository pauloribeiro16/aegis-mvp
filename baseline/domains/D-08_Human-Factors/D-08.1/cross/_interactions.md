# D-08.1 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-08.1 General Security Awareness](../../DomainAnalysis/D-08_Human-Factors/D-08.1.md)
#### D-08.1 General Security Awareness
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority / partial-coverage notes:** AI Act is fully absent from D-08.1 per CRDA (no general-security-awareness mandate); AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) cover role-specific AI competence in D-08.2. CRA is "partial coverage" (Annex II §8 user-instructions only — not workforce awareness).

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-08.1 General Security Awareness
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md`](../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.1.md)
> (6 pairs verified against OJ text — **4 participating regulations
> are GDPR, NIS 2, CRA, DORA; AI Act is fully absent** as noted by
> `DomainAnalysis/D-08_Human-Factors/D-08.1.md`
> line 27: "Participants: GDPR, NIS2, CRA, DORA" and lines 30–35:
> "CRA is 'partial coverage' (Annex II §8 user-instructions only — not
> workforce awareness) ... AI Act does not impose a general-security-
> awareness mandate").
>
> **AI Act absence note (per CRDA-deep §D-08.1 line 277):** CRDA marks
> AI Act as out-of-scope for D-08.1 (no general-security-awareness
> mandate). The AI Act Art. 4 (AI literacy) and SR-AIACT-012
> (human-oversight training for high-risk AI) are mapped to D-08.2
> (role-specific competence), not D-08.1. No AI Act pair is included
> in the D-08.1 verification.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-08.1)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations and on the controller's or processor's data-protection policies applicable to their role (Art. 39(1)(a)+(b)). | DPO-driven; workforce awareness on data-protection obligations specific to processing role. |
| NIS2 | SO-NIS2-018 | Basic cyber hygiene practices are established, covering all users of network and information systems with access to entity systems and services (Art. 21(2)(g) first clause). | Entity-wide hygiene baseline; workforce-and-systems substrate. |
| CRA | SO-CRA-048 (partial) | Detailed user-facing instructions (Annex II §8(a)–(f)) for product secure use over lifetime. | User instructions with the product, not workforce awareness; partial-coverage. AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness. |
| DORA | SO-DORA-015 | ICT security awareness programmes and digital operational resilience training as compulsory modules in staff training schemes, with complexity commensurate to the remit of staff functions (Art. 13(6)). | Entity-level compulsory training; awareness + digital operational resilience training combined. |
| AI_Act | (out-of-scope) | AI Act does not impose a general-security-awareness mandate. AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) are mapped to D-08.2. | — |

## Validated relationships (from CRDA-deep §D-08.1)

#### Validated relationships (from CRDA-deep §D-08.1)
Of 6 pairs, **6 verified as SAME — no CORRECTED, no CONTRADICTORY** — the four regulators look at general security awareness from four distinct regulatory perspectives that are layered rather than contradictory. The **3 SAME — COMPLEMENTARY** pairs (GDPR↔NIS2, GDPR↔DORA, NIS2↔DORA) stack on the integrated staff training programme. The **1 SAME — EQUAL** pair (NIS2↔DORA, where DORA's `compulsory modules` is more prescriptive than NIS 2's `basic cyber hygiene`) discharges both obligations on the DORA financial-entity stack. The **3 SAME — DIFFERENT-PERSPECTIVE (substantively scope-disjoint)** pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) operate in parallel on different audiences (internal workforce vs external product-user) with no consolidation rule — different audiences and different content mean no reclassification is required, but the two parallel tracks coexist:
- **GDPR ↔ NIS2** — COMPLEMENTARY (SAME): GDPR awareness is DPO-driven and data-protection-focused (Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations` + Art. 39(1)(a) `inform and advise … the employees who carry out processing of their obligations`); NIS 2 awareness is hygiene-focused (`basic cyber hygiene practices` per Art. 21(2)(g) first clause, covering phishing, password discipline, removable-media). The two training programmes can be combined into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation. Scope-disjoint test: **Y (when the controller-NSIE's workforce needs both data-protection awareness and cyber-hygiene training)**. No reclassification required.
- **GDPR ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME) (substantively scope-disjoint): GDPR addresses workforce awareness on data-protection obligations (DPO-catalysed, internal staff); CRA addresses end-user instructions shipped with the product (external user, Annex II §8(a)–(f) detailed instructions for the lifetime of the product). The audiences differ (internal staff vs external user) and the content differs (regulation compliance awareness vs product secure use). Scope-disjoint test: **N (typically)** — different audiences (workforce vs end-user), different objects (regulation compliance awareness vs product secure-use instructions), different triggers (DPO-catalysed vs manufacturer ships product). No reclassification required, but no consolidation rule applies.
- **GDPR ↔ DORA** — COMPLEMENTARY (SAME): DORA training is compulsory-modules-led (Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules`); GDPR awareness is DPO-catalysed (Art. 39(1)(a)+(b)). DORA's `commensurate to the remit of their functions` phrasing subsumes GDPR's role-specific dimension; the two regimes stack with the DORA programme as the carrier and GDPR content as a module. Scope-disjoint test: **Y (when a DORA financial entity is a controller processing personal data over its own staff)**. No reclassification required.
- **NIS2 ↔ CRA** — DIFFERENT-PERSPECTIVE (SAME) (substantively scope-disjoint): NIS 2 covers workforce awareness on hygiene (Art. 21(2)(g) first clause `basic cyber hygiene practices` covering internal staff); CRA covers user instructions with the product (Annex II §8(a)–(f) external user). Different audiences (workforce vs end-user) and different content (hygiene baseline vs product secure use). Scope-disjoint test: **N (typically)** — different audiences, different objects. No reclassification required.
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose workforce awareness programmes at the entity level (Art. 21(2)(g) first clause NIS 2 + Art. 13(6) DORA). DORA's `compulsory modules` is more prescriptive than NIS 2's `basic cyber hygiene` (which is entity-discretionary under Recital 56). For financial entities, DORA is the dominant authority; for non-financial NSIEs, NIS 2 is the authority. Scope-disjoint test: **Y (when a DORA financial entity is also an NSIE applying workforce awareness)**. No reclassification required.
- **CRA ↔ DORA** — DIFFERENT-PERSPECTIVE (SAME) (substantively scope-disjoint): CRA covers external user instructions (Annex II §8(a)–(f) manufacturer-shipped with the product, B2C/user-facing); DORA covers internal staff training modules (Art. 13(6) `compulsory modules` in staff training schemes, workforce). Different audiences (external users vs internal staff) and different content. Scope-disjoint test: **N (typically)** — different audiences, different objects. No reclassification required.
The general-security-awareness architecture is **legitimately diverse with substantively scope-disjoint structure** — each regulator targets a **distinct target audience** (DPO-catalysed processing staff / entity-wide hygiene baseline workforce / manufacturer-shipped end-user with product / financial-entity compulsory-modules-led staff) at a **distinct trigger** (DPO activity per Art. 39(1)(b) / entity-wide basic-hygiene baseline per Art. 21(2)(g) / manufacturer places product on market with Annex II §8 instructions / financial entity establishes training schemes with Art. 13(6) compulsory modules) with a **distinct obligation anchor** (GDPR Art. 39(1)(a)+(b) DPO `inform and advise` + `awareness-raising and training of staff involved in processing operations`; NIS 2 Art. 21(2)(g) first clause `basic cyber hygiene practices and cybersecurity training` with `appropriate and proportionate` chapeau + state-of-the-art floor; CRA Annex II §8(a)–(f) `detailed instructions … covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use` — user-facing — partial coverage; DORA Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions`). The high-level SO surfaces the **common general-awareness duty** (documented training programme + population-wide coverage + audience-routing + governance hooks); the per-reg target audience, trigger, anchor, threshold, evidence template, recipient are preserved verbatim in the four sub-SOs.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
| | GDPR | NIS2 | CRA | DORA |
|---|---|---|---|---|
| **GDPR** | — | Y (controller = NSIE; data-protection awareness module + hygiene module combined into single curriculum) | N (typically) — substantively scope-disjoint (internal staff vs external user; DPO-driven vs manufacturer-shipped) | Y (financial-entity-controller with workforce awareness obligations; DORA programme as carrier + GDPR content as module) |
| **NIS2** | Y (same; reciprocal — controller-NSIE) | — | N (typically) — substantively scope-disjoint (workforce vs end-user; entity-wide hygiene vs manufacturer-shipped instructions) | Y (DORA financial entity = NSIE; DORA-dominant stack discharges both obligations for financial entities) |
| **CRA** | N (typically) (same; reciprocal — substantively scope-disjoint) | N (typically) (same; reciprocal — substantively scope-disjoint) | — | N (typically) — substantively scope-disjoint (external end-user vs internal staff; manufacturer-shipped vs compulsory-modules) |
| **DORA** | Y (same; reciprocal — financial-entity-controller with CIF clauses documented on controller side) | Y (same; reciprocal — DORA compulsory-modules exceeds NIS 2 `appropriate and proportionate` baseline for financial-services subset) | N (typically) (same; reciprocal — substantively scope-disjoint) | — |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). **N (typically)** = substantive scope-disjoint — different audiences (internal workforce vs external product-user) and different objects (regulation compliance awareness vs product secure-use instructions). The CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) are **substantively scope-disjoint** — the 3 pairs are SAME — DIFFERENT-PERSPECTIVE per CRDA-deep verified classifications. No SCOPE-DISJOINT reclassifications are required, but the parallel tracks coexist on different audiences with no consolidation rule. CRDA-deep scope-disjoint tests: GDPR↔NIS2 = Y; GDPR↔CRA = N (typically) substantively scope-disjoint (different audiences, different objects); GDPR↔DORA = Y; NIS2↔CRA = N (typically) substantively scope-disjoint; NIS2↔DORA = Y; CRA↔DORA = N (typically) substantively scope-disjoint.

## Cross-recipient map

#### Cross-recipient map
D-08.1 generates a layered recipient set on the **general-security-awareness evidence trail** but does **not generate a notification cascade of D-08.1 itself** (the awareness programme is the upstream governance input to the workforce cybersecurity posture). The recipient set is at the **training-evidence layer**: **GDPR's supervisory authority (DPA)** on the Art. 5(2) accountability evidence (Art. 39(1)(b) DPO-catalysed awareness/training records + Art. 30(4) staff awareness record + Art. 47(2)(n) BCR training — cross to D-09.2 via the Art. 35 DPIA necessary-assessment chain); **NIS 2's management body + competent authority** on the Art. 21(1) + 21(2)(g) documented policies on basic cyber hygiene + Art. 20(1) management-body approval+oversight+liability for the awareness measures; **CRA's market surveillance authority (MSA)** on the Annex II §8(a)–(f) user-facing detailed instructions + Art. 13(18) support-period accessibility (10-year information accessibility for Annex II information — **user-facing audience only**, not workforce); **DORA's competent authority (national financial supervisory authority)** on the Art. 13(6) compulsory-modules training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline. These are distinct regulatory channels on the same training-records artefact but they do not generate a notification cascade of D-08.1 itself — they are **compliance-evidence channels on the layered training programme**. The **AI Act's full absence from D-08.1** means there is no AI Act recipient on D-08.1 — AI Act Art. 4 AI literacy + Art. 14 human-oversight training are routed to D-08.2 (role-specific competence), where the AI Act recipient set is documented. **D-08.2 (Role-Specific Competence) is the operational downstream artefact where D-08.1's general awareness becomes role-specific depth**; **D-09.1 (Information Security Policies) is where the training programme is integrated into the broader organisational policy governance**; **D-04.3 (Regulatory Notification) is the notification cascade where training-programme evidence flows to supervisory authorities on incident reporting**; **D-09.4 (Records of Processing) is the documentation-channel cross-link for GDPR Art. 30 staff-awareness records and CRA Annex II §8 user-facing instructions**.
---

## HSO considerations (from D-08.1.0 — High-level SecurityObjective)

**Considerations.**
- 4 of 5 regulations participate (GDPR, NIS 2, CRA, DORA); AI Act is fully absent per CRDA-deep §D-08.1 (AI Act Art. 4 AI literacy + SR-AIACT-012 human-oversight training for high-risk AI are mapped to D-08.2, not D-08.1).
- GDPR Art. 39(1)(a) `inform and advise the controller or the processor and the employees who carry out processing of their obligations` + Art. 39(1)(b) `monitor compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations` — DPO-catalysed workforce data-protection awareness on the controller's processing-staff audience.
- NIS 2 Art. 21(2)(g) first clause `basic cyber hygiene practices and cybersecurity training` — entity-wide hygiene baseline with `appropriate and proportionate` chapeau + state-of-the-art floor, on the entity's workforce and systems substrate.
- CRA Annex II §8(a)–(f) `detailed instructions … covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use` — manufacturer-shipped user-facing instructions on the end-user audience — **partial coverage** (user-facing not workforce).
- DORA Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` — financial-entity compulsory-modules-led staff training on the financial-entity workforce.
- 6 pairwise cells: 3 SAME — COMPLEMENTARY (GDPR↔NIS2, GDPR↔DORA, NIS2↔DORA), 1 SAME — EQUAL (NIS2↔DORA on workforce awareness at entity level — DORA `compulsory modules` exceeds NIS 2 `basic cyber hygiene`), 3 SAME — DIFFERENT-PERSPECTIVE substantively scope-disjoint (GDPR↔CRA, NIS2↔CRA, CRA↔DORA — internal workforce vs external end-user with product).
- The high-level SO engages on the Y-pairs integrated stack when ≥2 regs are applicable: GDPR↔NIS2 (DPO module + hygiene module combined into single curriculum); GDPR↔DORA (DORA programme as carrier + GDPR content as module); NIS2↔DORA (DORA-dominant for financial entities; NIS 2-dominant for non-financial NSIEs).
- The CRA-involving pairs operate on substantively scope-disjoint audiences (internal workforce vs external end-user with product) — the parallel tracks coexist with no consolidation rule; the high-level SO does NOT collapse the audience boundaries.
- For a 5-FTE SaaS startup with GDPR + CRA applicability, the two parallel training-programme tracks must be maintained separately (substantively scope-disjoint audiences).
- The per-reg target audience, trigger, anchor, threshold, evidence template, recipient are preserved verbatim in the four sub-SOs.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 4 participating regulations each define D-08.1 over a distinct **target audience** of the general-security-awareness architecture; the target audience, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the awareness programme.
| Axis (reg) | Target audience | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | DPO-catalysed processing staff with data-subject-facing or access-management responsibilities (internal workforce) | DPO-catalysed awareness/training activity per Art. 39(1)(b) `awareness-raising and training of staff involved in processing operations` + Art. 39(1)(a) `inform and advise the controller or the processor and the employees who carry out processing of their obligations` | no quantitative cadence (DPO-discretionary under Recital 56); `awareness-raising` implies ongoing reinforcement not one-off induction; Art. 5(2) accountability burden shifts demonstration duty to the controller | supervisory authority (DPA) — Art. 5(2) accountability on the Art. 39(1)(b) DPO-catalysed awareness/training records + Art. 30(4) staff awareness record + Art. 47(2)(n) BCR training (cross to D-09.2 via Art. 35 DPIA necessary-assessment chain) | Art. 39(1)(a) + Art. 39(1)(b) + Art. 5(1)(f) (cross) + Art. 5(2) accountability + Art. 24(1) + Art. 30(4) + Art. 47(2)(n) BCR |
| **NIS2** | entity-wide workforce and systems (workforce hygiene baseline covering phishing, password discipline, removable-media) | entity-wide basic-hygiene baseline per Art. 21(2)(g) first clause `basic cyber hygiene practices and cybersecurity training` | `appropriate and proportionate` (Art. 21(1) chapeau) + state-of-the-art (Art. 21(1) sentence 2) + Recital 56 cost factor; no quantitative cadence; the OJ does not enumerate the hygiene practices — entity-discretionary interpretation under Recital 56 proportionality | management body (Art. 20(1) approve+oversee+liability) + competent authority — Art. 21(2)(g) basic-hygiene records + Art. 21(1) documented policies + Art. 20(1) management-body approval | Art. 21(2)(g) first clause + Art. 21(1) chapeau + Art. 21(1) sentence 2 state-of-the-art + Art. 20(1) management-body approval + Recital 56 proportionality |
| **CRA** | end-user (external user with the product) — partial coverage per AEGIS taxonomy §4.1; workforce-side limited to Annex II §8(f) integrator information | manufacturer places product on market (Art. 13(1) trigger); Annex II §8(a)–(f) instructions accompany the product throughout the lifetime; Art. 13(18) 10-year Annex II information accessibility | support period ≥ 5 years (Art. 13(8) sentence 3) + 10-year Annex II information accessibility (Art. 13(18)) — qualitative support-period framing; the `detailed` content threshold is harmonised-standards-pending | end-user (B2C/user-facing) + market surveillance authority (MSA) — Annex II §8(a)–(f) instructions on the product; Annex II §8(f) integrator information discharge the workforce-side partial dimension for B2B integrators | Art. 13(1) + Annex II §8(a) + Annex II §8(b) + Annex II §8(c) + Annex II §8(d) + Annex II §8(e) + Annex II §8(f) + Art. 13(18) support-period accessibility + Recital 25 (Annex II scope) |
| **DORA** | financial-entity staff with `commensurate to the remit of their functions` complexity (workforce training across all staff functions) | financial entity establishes training schemes (Art. 13(6) `compulsory modules in their staff training schemes`) — continuous obligation | `compulsory` (Art. 13(6) — completion-mandatory per SR-DORA-025 ambiguity reading) + `commensurate to the remit of their functions` (function-specific calibration per the OJ literal) — qualitative + `level of complexity` qualitative; no quantitative cadence | competent authority (national financial supervisory authority) + management body — Art. 13(6) `compulsory modules` training records + Art. 5(2) management-body oversight + EBA Guidelines on ICT and security risk management supervisory baseline | Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` + Art. 5(2) management-body responsibility + EBA Guidelines on ICT and security risk management |
| **AI_Act** | (out-of-scope) — AI Act Art. 4 (AI literacy) + Art. 14 (human-oversight training) are mapped to D-08.2 (role-specific competence), not D-08.1 | — | — | — | — |

## Scope-overlap matrix (4×4)

#### Scope-overlap matrix (4×4)
(See the validated-relationships table above for the 4×4 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SO-D-08.1.HL`) engages on a given party **if and only if ≥2 applicable
regulations target overlapping target audiences on the same party** (e.g.
a financial entity that is also a NIS 2 essential entity AND processes
personal data AND manufactures CRA-classified products — a vertically-
integrated financial-manufacturer-controller with full GDPR + NIS 2 +
CRA + DORA applicability on the same training-programme substrate). For an
integrated controller-NSIE that does not manufacture CRA-classified
products, only the GDPR and NIS 2 sub-SOs activate; the high-level SO
engages on the GDPR↔NIS2 COMPLEMENTARY pair. For a financial entity
that is also a controller, only the GDPR and DORA sub-SOs activate; the
high-level SO engages on the GDPR↔DORA COMPLEMENTARY pair (DORA
programme as carrier + GDPR content as module). For a CRA manufacturer
that is also a controller, the GDPR + CRA sub-SOs activate on
**substantively scope-disjoint audiences** (DPO-catalysed workforce +
manufacturer-shipped end-user instructions) — the two tracks coexist in
parallel with no consolidation rule; the high-level SO does **NOT**
collapse the audience boundaries. For a 5-FTE SaaS startup with GDPR +
CRA applicability but no NIS 2 / DORA applicability, only the GDPR
and CRA sub-SOs activate; the **substantively scope-disjoint audiences**
mean the two parallel training-programme tracks must be maintained
separately. For a NIS 2 essential entity that is not a financial entity
and does not manufacture CRA-classified products (NIS 2 + GDPR only or
NIS 2 only with non-CRA-classified products), only the applicable
sub-SOs activate and the high-level SO engages on the GDPR↔NIS2
COMPLEMENTARY pair. **The four target audiences are layered, not
collapsed**: DPO-catalysed processing staff (GDPR, controller-driven
DPO-catalysed awareness); entity-wide hygiene baseline (NIS 2, entity-
driven continuous basic-hygiene coverage); manufacturer-shipped end-user
instructions (CRA, manufacturer-driven product-lifetime support);
financial-entity compulsory-modules-led staff training (DORA, financial-
entity-driven `commensurate to the remit` depth). The high-level SO
surfaces the common general-awareness duty but does **NOT** collapse the
per-reg target audience, trigger, anchor, threshold, recipient, or
evidence template.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **4 of 5 regulations participate** (GDPR, NIS 2, CRA, DORA —
  **4 participate, AI Act is fully absent**, no out-of-scope on
  GDPR/NIS2/CRA/DORA): GDPR (Art. 39(1)(a)+(b) DPO-catalysed workforce
  awareness as controller obligation); NIS 2 (Art. 21(2)(g) first
  clause entity-wide hygiene baseline as entity obligation); CRA
  (Annex II §8(a)–(f) user-facing instructions as manufacturer
  obligation — **partial coverage** per AEGIS taxonomy §4.1);
  DORA (Art. 13(6) compulsory-modules-led training as financial-entity
  obligation); AI Act (Art. 4 AI literacy + Art. 14 human-oversight
  training — **fully absent from D-08.1**, mapped to D-08.2 instead).
- **6 pairwise cells, verified by CRDA-deep as a mixed pattern**:
  GDPR↔NIS2 (SAME — COMPLEMENTARY — `what` data-protection awareness
  + `that` hygiene baseline stack at controller-NSIE); GDPR↔CRA (SAME
  — DIFFERENT-PERSPECTIVE — substantively scope-disjoint, workforce
  vs end-user audiences); GDPR↔DORA (SAME — COMPLEMENTARY —
  controller-side data-protection awareness overlay on financial-
  entity compulsory-modules-led programme); NIS2↔CRA (SAME —
  DIFFERENT-PERSPECTIVE — substantively scope-disjoint, workforce
  vs end-user audiences); NIS2↔DORA (SAME — EQUAL — both regulations
  impose workforce awareness programmes at entity level; DORA-dominant
  for financial entities); CRA↔DORA (SAME — DIFFERENT-PERSPECTIVE —
  substantively scope-disjoint, end-user instructions vs internal
  staff training).
- The four participating regulations impose **distinct general-
  awareness duties** at **distinct target audiences** with **distinct
  triggers** and **distinct anchors**: GDPR controller-side
  DPO-catalysed workforce (Art. 39(1)(a)+(b) `inform and advise` +
  `awareness-raising and training of staff involved in processing
  operations`); NIS 2 entity-side workforce (Art. 21(2)(g) first
  clause `basic cyber hygiene practices and cybersecurity training` +
  `appropriate and proportionate` chapeau + state-of-the-art floor +
  Art. 20(1) management-body approval); CRA manufacturer-side
  end-user (Annex II §8(a)–(f) `detailed instructions` — partial
  coverage); DORA financial-entity-side workforce (Art. 13(6)
  `compulsory modules in their staff training schemes` + `commensurate
  to the remit of their functions` — entity-internal governance hook).
  The thresholds align qualitatively (no regulation imposes
  quantitative cadence — all are entity-discretionary under Recital 56
  proportionality or equivalent). The four anchors align in their
  direction-of-travel (general-awareness coverage calibrated to risk)
  but the target audiences, triggers, evidentiary templates,
  recipients diverge.
- The high-level SO describes the **COMMON OBJECTIVE** (documented
  training programme + population-wide coverage + audience-routing +
  governance hooks); the **per-regulation perspective** (target
  audience, trigger, anchor, threshold, recipient, evidence template)
  is preserved verbatim in the four sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the general-awareness duty
  itself**, because no pair was verified as CONTRADICTORY or CORRECTED
  (all 6 pairs are SAME — 3 SAME — COMPLEMENTARY + 1 SAME — EQUAL +
  3 SAME — DIFFERENT-PERSPECTIVE substantively scope-disjoint). Phase
  1C Doc 07 does not need to resolve a general-awareness contradiction
  because none exist by construction. The **3 substantively scope-
  disjoint pairs** (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) are SAME —
  DIFFERENT-PERSPECTIVE per CRDA-deep verified classifications —
  no reclassification is required, but the parallel tracks coexist on
  different audiences (workforce vs end-user) with no consolidation
  rule. The **AI Act full absence** is a structural Layer 2 review
  item — AI Act Art. 4 (AI literacy) + Art. 14 (human-oversight
  training) are routed to D-08.2 (role-specific competence), not
  D-08.1 — the operational boundary between D-08.1 general awareness
  and D-08.2 role-specific competence is preserved by the per-
  regulation target-audience distinction.
- **Scope caveat (CRITICAL — AI Act full absence)** — derived from
  CRDA-deep verified classifications: AI Act does not impose a
  general-security-awareness mandate. AI Act Art. 4 (AI literacy) +
  Art. 14 (human-oversight training for high-risk AI) are mapped to
  D-08.2 (role-specific competence), not D-08.1. For an entity with
  AI Act applicability only, no D-08.1 sub-SO activates; the entity
  moves directly to D-08.2 for the AI Act role-specific obligation.
- **Scope caveat (CRITICAL — CRA partial coverage)** — derived from
  CRDA-deep verified classifications: CRA participation at D-08.1 is
  partial — Annex II §8(a)–(f) is user-facing instructions shipped
  with the product, not workforce awareness. AEGIS taxonomy §4.1
  marks NIS 2 / DORA / GDPR as the authorities for full staff
  awareness. The 3 CRA-involving pairs (GDPR↔CRA, NIS2↔CRA,
  CRA↔DORA) are SAME — DIFFERENT-PERSPECTIVE substantively scope-
  disjoint on the different-audiences dimension. For a CRA-regulated
  manufacturer, the workforce awareness obligation is discharged via
  NIS 2 / DORA / GDPR; the Annex II §8(a)–(f) user-facing
  instructions discharge the end-user-facing information duty. The
  Annex II §8(f) integrator information is a workforce-side partial
  dimension (B2B integrators), but the primary CRA-side output is
  user-facing.
- **Scope caveat (CRITICAL — NIS 2 hygiene baseline vs GDPR
  data-protection awareness)** — derived from CRDA-deep verified
  classifications: NIS 2 Art. 21(2)(g) first clause addresses
  `basic cyber hygiene practices and cybersecurity training` on the
  entity-wide workforce; GDPR Art. 39(1)(b) addresses DPO-catalysed
  `awareness-raising and training of staff involved in processing
  operations`. For an integrated controller-NSIE, the two awareness
  programmes can be combined into a single curriculum where the
  data-protection module feeds the GDPR obligation and the hygiene
  module feeds the NIS 2 obligation. The two regimes stack with
  distinct evidence trails (GDPR: documented Art. 39(1)(a)+(b) DPO-
  catalysed awareness/training records on the controller side via
  Art. 5(2) accountability; NIS 2: Art. 21(2)(g) basic-hygiene
  records + Art. 21(1) documented policies on risk analysis + IS
  security + Art. 20(1) management-body approval).
- **Scope caveat (CRITICAL — NIS 2 ↔ DORA EQUAL classification on
  workforce awareness)** — derived from CRDA-deep verified
  classifications: both regulations impose workforce awareness
  programmes at entity level (Art. 21(2)(g) first clause NIS 2 +
  Art. 13(6) DORA). DORA's `compulsory modules` is more prescriptive
  than NIS 2's `basic cyber hygiene` (which is entity-discretionary
  under Recital 56). For DORA financial entities, the DORA programme
  is dominant authority; for non-financial NSIEs, NIS 2 is the
  authority. The EQUAL classification preserves the OJ literal
  parallel between the two regimes on the workforce awareness
  dimension; the dominant-authority reading is the operational
  consequence of the DORA-direct-applicability vs NIS 2-MS-
  transposition asymmetry.
- **Scope caveat (CRITICAL — GDPR ↔ DORA COMPLEMENTARY on DORA
  programme as carrier)** — derived from CRDA-deep verified
  classifications: DORA's `compulsory modules in their staff
  training schemes, with a level of complexity commensurate to the
  remit of their functions` phrasing subsumes GDPR's role-specific
  dimension; the two regimes stack with the DORA programme as the
  carrier and GDPR content as a module. For a DORA financial entity
  that is a controller processing personal data over its own staff,
  the DORA Art. 13(6) programme is the carrier; the GDPR Art.
  39(1)(b) DPO-catalysed data-protection awareness is the module.
  The two evidence trails stack with the DORA programme as the
  carrier and GDPR content documented in a sub-component.
---

## Emergent tensions (from CRDA-deep §D-08.1)

#### Emergent tensions (from CRDA-deep §D-08.1)
**0 conditional emergent tensions** on the general-security-awareness duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The 6 pairs are all SAME — 3 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 3 SAME — DIFFERENT-PERSPECTIVE (substantively scope-disjoint). **The 3 SAME — DIFFERENT-PERSPECTIVE pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) are CRDA-verified as substantively scope-disjoint on the different-audiences dimension** — internal workforce (DPO-driven / entity-wide hygiene / compulsory-modules) vs external end-user with product — but the CRDA `same-different-perspective` classification preserves the substantive scope-disjointness without requiring reclassification, with the parallel tracks coexisting. **No SCOPE-DISJOINT reclassifications** — CRDA preserves the 3 different-audience pairs as SAME — DIFFERENT-PERSPECTIVE rather than as SCOPE-DISJOINT pairs. **No CONTRADICTORY pairs** on the general-awareness duty itself. The **target-audience divergence** (DPO-catalysed processing staff / entity-wide hygiene workforce / manufacturer-shipped end-user / financial-entity compulsory-modules staff) is the **legitimately diverse dimension**: each regulator targets a distinct target audience at a distinct trigger (DPO activity / entity-wide hygiene baseline / manufacturer places product on market / financial entity establishes training schemes), and the operational convergence is on a **4-layer awareness architecture** with explicit parallel tracks (workforce tracks on GDPR/NIS2/DORA + user-facing track on CRA) — the parallel tracks coexist on substantively scope-disjoint audiences with no consolidation rule.
The **AI Act full absence** is the structurally significant divergence: AI Act does not impose a general-security-awareness mandate per CRDA-deep §D-08.1 line 27 — AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) are mapped to D-08.2 (role-specific competence), not D-08.1. For an entity with AI Act applicability only, no D-08.1 sub-SO activates; the entity moves directly to D-08.2 for the AI Act role-specific obligation. The **CRA partial coverage** is the second structurally significant divergence: CRA Annex II §8(a)–(f) is user-facing instructions shipped with the product, not workforce awareness — AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness. For a CRA-regulated manufacturer, the workforce awareness obligation is discharged via NIS 2 / DORA / GDPR; the Annex II §8(a)–(f) user-facing instructions discharge the end-user-facing information duty.
The **NIS 2 hygiene baseline vs DORA compulsory-modules-led training EQUAL classification** is the structurally significant EQUAL pair: both regulations impose workforce awareness programmes at entity level — DORA's `compulsory modules` is more prescriptive than NIS 2's `basic cyber hygiene` (entity-discretionary under Recital 56). For DORA financial entities, the DORA programme is dominant authority; for non-financial NSIEs, NIS 2 is the authority. The EQUAL classification preserves the OJ literal parallel between the two regimes on the workforce awareness dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry (per SR-DORA-025 regulatory_rationale: "The clause co-exists with GDPR Art. 39 staff-awareness duties for personal-data processing (Regulation (EU) 2016/679) and with NIS 2 Art. 21(2)(g) basic security training baselines (Directive (EU) 2022/2555)").
The **GDPR ↔ DORA COMPLEMENTARY pair on DORA programme as carrier** is the structurally significant COMPLEMENTARY pair for the financial-services subset: DORA's `compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions` phrasing subsumes GDPR's role-specific dimension; the two regimes stack with the DORA programme as the carrier and GDPR content as a module. For a DORA financial entity that is a controller processing personal data over its own staff, the DORA Art. 13(6) programme is the carrier; the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is the module.
The high-level SO surfaces the common general-awareness duty; the per-reg target audience, trigger, anchor, threshold, recipient, and evidence template are documented separately in the four sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 4-layer awareness architecture (DPO-catalysed workforce / entity-wide hygiene baseline / manufacturer-shipped end-user / financial-entity compulsory-modules-led staff) with parallel tracks on substantively scope-disjoint audiences (workforce tracks on GDPR/NIS2/DORA + user-facing track on CRA) is itself the layered reconciliation that supersedes any single-regulator reading.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-08.1 — with overlapping target-audience scope-determiners on the same party — operates a **4-layer awareness architecture** with parallel tracks on substantively scope-disjoint audiences (workforce vs end-user). The high-level SO (`SO-D-08.1.HL`) describes the common general-awareness duty (documented training programme + population-wide coverage + audience-routing + governance hooks); the per-reg perspective is preserved in the four sub-SOs (target audience, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a layered reconciliation**, with the 4-layer awareness architecture (DPO-catalysed workforce / entity-wide hygiene baseline / manufacturer-shipped end-user / financial-entity compulsory-modules-led staff) operationalising the audience-routing between workforce tracks (GDPR / NIS 2 / DORA — Y scope overlap on internal-staff audience) and the parallel user-facing track (CRA — substantively scope-disjoint end-user audience). The high-level SO does NOT collapse the four target audiences into a single awareness architecture; the per-reg perspective on target audience, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **general-security-awareness strategy**: (1) a 4-layer awareness architecture with explicit target-audience hand-offs (GDPR Art. 39(1)(a)+(b) DPO-catalysed workforce → NIS 2 Art. 21(2)(g) first clause entity-wide hygiene baseline → CRA Annex II §8(a)–(f) user-facing instructions — partial coverage — → DORA Art. 13(6) financial-entity compulsory-modules-led staff training); (2) the AI Act full absence as a structural Layer 2 review item (AI Act Art. 4 AI literacy + Art. 14 human-oversight training routed to D-08.2, not D-08.1); (3) the CRA partial coverage as a structural Layer 2 review item (Annex II §8(a)–(f) user-facing not workforce awareness — AEGIS taxonomy §4.1 partial-coverage marker); (4) the NIS 2 ↔ DORA EQUAL classification on workforce awareness at entity level — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs; (5) the GDPR ↔ DORA COMPLEMENTARY pair on DORA programme as carrier + GDPR content as module for the financial-entity-controller stack; (6) the 3 substantively scope-disjoint pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) preserved as SAME — DIFFERENT-PERSPECTIVE per CRDA-deep verified classifications — parallel tracks coexist on different audiences with no consolidation rule; (7) the AI Act's full absence leaves D-08.1 with 4 participating regulations (GDPR, NIS 2, CRA, DORA) and 6 verified pairs.

## Part 1 §3 — context

### 3. Security Requirements
## 8.1 General Security Awareness — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md`. See that file for cross-reg verified relationships (6 pairs verified as 3 SAME — COMPLEMENTARY + 1 SAME — EQUAL + 3 SAME — DIFFERENT-PERSPECTIVE substantively scope-disjoint), scope overlap matrix, Objective/Considerations content, target-audience divergence (DPO-catalysed processing staff / entity-wide hygiene workforce / manufacturer-shipped end-user / financial-entity compulsory-modules-led staff), aggregation logic, **AI Act full absence** (per CRDA-deep §8.1 line 27: AI Act Art. 4 + SR-AIACT-012 are mapped to 8.2, not 8.1), and **CRA partial coverage** (Annex II §8 is user-facing — not workforce — AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness). This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
GDPR, NIS 2, CRA (partial), DORA (4 of 5 regs — AI Act out-of-scope per AEGIS taxonomy §4.1; CRDA-deep verified 6 pairs as SAME — no CORRECTED, no CONTRADICTORY). The four regulators target **distinct target audiences** at **distinct triggers** (DPO-catalysed workforce per Art. 39(1)(a)+(b) / entity-wide basic-hygiene baseline per Art. 21(2)(g) / manufacturer-shipped end-user with Annex II §8 instructions / financial-entity compulsory-modules-led training per Art. 13(6)), and the high-level SO surfaces the **common general-awareness duty** (documented training programme + population-wide coverage + audience-routing + governance hooks) while preserving the per-reg target audience, trigger, anchor, threshold, evidence template, recipient.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 8.1
  volere_section: 15
  volere_subtype: immunity
  title: "General security awareness established through a documented training programme with population-wide coverage, audience-routing, and governance hooks"
  derives_from:
    hso_sub_so: SO-8.1.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.1.md
    objective_ref_section: "### 8.1.0"
  description: |
    The product shall establish general security awareness for the controller's processing workforce, the entity-wide workforce and systems substrate, the manufacturer's end-user audience (where applicable), and the financial-entity compulsory-modules-led staff, through a documented training programme with population-wide coverage, audience-routing across the four target audiences, and governance hooks (DPO approval; management-body approval; market-surveillance accessibility; competent-authority evidence), as the common general-awareness duty converging across GDPR Art. 39(1)(a) + Art. 39(1)(b) DPO `inform and advise` + `awareness-raising and training of staff involved in processing operations`, NIS 2 Art. 21(2)(g) first clause `basic cyber hygiene practices and cybersecurity training` + Art. 21(1) `appropriate and proportionate` chapeau, CRA Annex II §8(a)–(f) `detailed instructions … covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use` — partial user-facing coverage, and DORA Art. 13(6) `ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions`, where ≥2 of these scope-determiners overlap on the same party.
  fit_criterion: |
    A documented training programme is maintained with four distinct audience routes operating in parallel (DPO-catalysed processing-staff module per Art. 39(1)(b) when GDPR in scope; entity-wide basic-hygiene baseline per Art. 21(2)(g) when NIS 2 in scope; manufacturer-shipped Annex II §8(a)–(f) + 10-year support-period accessibility per Art. 13(18) when CRA in scope; financial-entity compulsory-modules-led `commensurate to the remit` per Art. 13(6) when DORA in scope); each route documents target audience, trigger, anchor, threshold, evidence template, and recipient separately; the population-wide coverage discipline discharges PR.AT-01 broad-coverage leg + PR.AT-02 role-specific leg (8.2 layer) + PR.PS-01 system-side hygiene substrate (NIS 2); for an integrated controller-NSIE workforce the GDPR data-protection module and the NIS 2 hygiene module combine into a single curriculum with separate evidence trails (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship); for a DORA financial entity that is a controller, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is the module (per CRDA-deep §8.1 GDPR↔DORA verified relationship); for DORA financial entities, the DORA programme discharges the NIS 2 Art. 21(2)(g) workforce-awareness obligation (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification, DORA-dominant for financial entities); the CRA-side Annex II §8(f) integrator information operates on a substantively scope-disjoint audience (B2B external integrators) from the workforce programmes; Art. 20(1) management-body approval is documented when NIS 2 in scope; verified by training-programme documentation review + per-audience coverage audit + Art. 39(1)(b) DPO-catalysed awareness records inspection (when GDPR in scope) + Art. 21(2)(g) basic-hygiene records inspection (when NIS 2 in scope) + Annex II §8(a)–(f) instruction-set review + Annex II §8(f) integrator information review (when CRA in scope) + Art. 13(6) `compulsory modules` training records + EBA Guidelines supervisory baseline (when DORA in scope) + DPA / competent authority / MSA / national CA + ESA inspection-ready evidence pack on request.
  priority: MUST
  verification_method: TEST
  dependencies: []
  nist_csf: [PR.AT-01, PR.AT-02, PR.PS-01]
  applicable_if:
    regs: [GDPR, NIS2, CRA, DORA]
    scope_overlap: conditional   # HL engages only when ≥2 applicable regs target overlapping target audiences on the same party (see HSO scope-overlap principle); AI Act out-of-scope; CRA-involving pairs engage only on substantively scope-disjoint audiences (workforce vs end-user) — no consolidation rule across these
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The four participating regulations impose the same substantive general-security-awareness duty but each targets a **distinct target audience** at a **distinct trigger** with a **distinct obligation anchor**: GDPR Art. 39(1)(a) + Art. 39(1)(b) DPO-catalysed workforce (DPO-driven; data-protection focus; PR.AT-01 + PR.AT-02; Art. 5(2) accountability burden shifts demonstration duty to the controller); NIS 2 Art. 21(2)(g) first clause entity-wide hygiene baseline (`basic cyber hygiene practices and cybersecurity training`; `appropriate and proportionate` chapeau + state-of-the-art floor + Recital 56 proportionality; PR.AT-01 + PR.PS-01; Art. 20(1) management-body approval+oversight+liability); CRA Annex II §8(a)–(f) user-facing detailed instructions (manufacturer places product on market with Art. 13(18) 10-year Annex II information accessibility; `detailed` content threshold is harmonised-standards-pending; **partial coverage** — end-user audience, not workforce; AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness); DORA Art. 13(6) financial-entity compulsory-modules-led staff training (`commensurate to the remit of their functions` function-specific calibration; `compulsory` completion-mandatory per SR-DORA-025 ambiguity reading; PR.AT-01 + PR.AT-02; Art. 5(2) management-body oversight). The thresholds align qualitatively (no regulation imposes quantitative cadence — all are entity-discretionary under Recital 56 proportionality or equivalent). The four anchors align in their direction-of-travel (general-awareness coverage calibrated to risk) but the target audiences, triggers, evidentiary templates, recipients diverge. The high-level SO surfaces the **COMMON OBJECTIVE** (documented training programme + population-wide coverage + audience-routing + governance hooks); the **per-regulation perspective** (target audience, trigger, anchor, threshold, recipient, evidence template) is preserved verbatim in the four sub-SOs (8.1.1 / -NIS2 / -CRA / -DORA). **AI Act full absence** is preserved — AI Act Art. 4 + SR-AIACT-012 + Art. 14 human-oversight training are routed to 8.2 (role-specific competence), not 8.1, per CRDA-deep §8.1 line 27; no AI Act sub-requirement exists below. **CRA partial coverage** is preserved — the CRA-side general-awareness output at this layer is user-facing (Annex II §8(a)–(e)) + integrator-facing B2B (Annex II §8(f)); the manufacturer's or operator's workforce-side awareness obligation is discharged via NIS 2 / DORA / GDPR with the CRA-side output remaining substantively scope-disjoint from the workforce programmes. The **NIS2↔DORA EQUAL classification** (CRDA-deep) preserves the OJ literal parallel between the two regimes on the workforce awareness dimension; DORA's `compulsory modules` exceeds NIS 2's `basic cyber hygiene` (entity-discretionary under Recital 56) — for DORA financial entities DORA is the dominant authority; for non-financial NSIEs NIS 2 is the authority. CRDA-deep verified 0 conditional emergent tensions on the general-awareness duty itself; the 4×4 matrix is preserved without reclassification but the **3 substantively scope-disjoint pairs** (GDPR↔CRA, NIS2↔CRA, CRA↔DORA) operate on distinct audiences (workforce vs end-user) with no consolidation rule. (Copied from the HSO Considerations block of `### 8.1.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-08.1
title: D-08.1 General Security Awareness — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.1 General Security Awareness
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-08_Human-Factors/D-08.1.md
status: DRAFT
---
> **Deep analysis:** [D-08.1 General Security Awareness](../../DeepAnalysis/D-08_Human-Factors/D-08.1.md)
#### D-08.1 General Security Awareness
<!-- participants: GDPR, NIS2, CRA, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | SO-GDPR-025 | Personnel authorised to process personal data are informed and trained on GDPR obligations (Art. 39(1)(a)+(b)). | DPO-driven; workforce awareness on data-protection obligations specific to processing role. |
| NIS2 | SO-NIS2-018 | Basic cyber hygiene practices across all users of NIS (Art. 21(2)(g)). | Entity-wide hygiene baseline; workforce-and-systems substrate. |
| CRA | SO-CRA-048 (partial) | Detailed user-facing instructions (Annex II §8) for product secure use over lifetime. | User instructions with the product, not workforce awareness; partial-coverage. AEGIS taxonomy §4.1 marks NIS 2 / DORA / GDPR as the authorities for full staff awareness. |
| DORA | SO-DORA-015 | ICT security awareness programmes and digital operational resilience training as compulsory modules (Art. 13(6)). | Entity-level compulsory training; awareness + resilience training combined. |
| AI_Act | (out-of-scope) | AI Act does not impose a general-security-awareness mandate. | — |
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
##### Emergent tensions (4 regulations)
<!-- emergent: GDPR,NIS2,CRA,DORA -->
- **Audience fragmentation**: GDPR (DPO-driven staff), NIS 2 (entity-wide hygiene), CRA (external users with product), DORA (compulsory staff modules) each target a different population and content scope. A DORA financial entity that processes personal data and ships CRA-regulated products must operate four parallel training programmes that do not cross-substitute. The AEGIS Cross-Cutting Layer 1 reconciliation may consolidate the GDPR / DORA staff modules but cannot substitute for CRA's user-facing instructions or NIS 2's hygiene baseline.
- **AI_Act is fully absent**: AI Act does not impose a general-security-awareness mandate — but AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) cover role-specific AI competence. The taxonomy marks these as D-08.2 (training & competence) not D-08.1 (general awareness), but the operational boundary between D-08.1 general and D-08.2 role-specific is undefined when AI literacy is at stake.
<!-- /emergent -->
##### SR cross-validation
The 4 applicable regulations map D-08.1 to the NIST CSF 2.0 Subcategories **PR.AT-01** (All users informed and trained on cybersecurity topics) as the convergent anchor. DORA additionally maps **PR.AT-02** (All members of the workforce understand their roles) via the `commensurate to the remit` clause; GDPR additionally maps **PR.AT-02** for the role-specific dimension. The CSF mapping reflects the staff-awareness substrate.
##### Downstream implication
Phase 1 entities must implement audience-fragmented training programmes. A consolidated training-management system can carry the four programmes (GDPR + NIS 2 + CRA user-instructions + DORA) with audience-routing logic. The training-records retention is per regulation (GDPR indefinite until processing ceases; DORA per Art. 5(2) accountability; CRA per Annex II §8 lifetime; NIS 2 per Recital 56 proportionality).
---
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-08.1
title: D-08.1 General Security Awareness — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.1 General Security Awareness
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-08_Human-Factors/D-08.1.md
status: DRAFT
---
> **Domain analysis:** [D-08.1 General Security Awareness](../../DomainAnalysis/D-08_Human-Factors/D-08.1.md)
#### D-08.1 General Security Awareness
<!-- participants: GDPR, NIS2, CRA, DORA -->
**Participants (from CRDA):** GDPR, NIS2, CRA, DORA
**Sole-authority / partial-coverage notes:** AI Act is fully absent from D-08.1 per CRDA (no general-security-awareness mandate); AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) cover role-specific AI competence in D-08.2. CRA is "partial coverage" (Annex II §8 user-instructions only — not workforce awareness).

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

## Residual pair content (AI_Act, deep)

##### Pair: AI_Act ↔ [not in CRDA D-08.1] (omitted — AI Act is fully absent per CRDA)
> **Note:** CRDA marks AI Act as out-of-scope for D-08.1 (no general-security-awareness mandate). The AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) are mapped to D-08.2 (role-specific competence), not D-08.1. No pair analysis is included here.
---

## Residual pair content (AI_Act, deep3)

##### Pair: AI_Act ↔ [not in CRDA D-08.1] (omitted — AI Act is fully absent per CRDA)
> **Note:** CRDA marks AI Act as out-of-scope for D-08.1 (no general-security-awareness mandate). The AI Act Art. 4 (AI literacy) and SR-AIACT-012 (human-oversight training for high-risk AI) are mapped to D-08.2 (role-specific competence), not D-08.1. No pair analysis is included here.
---