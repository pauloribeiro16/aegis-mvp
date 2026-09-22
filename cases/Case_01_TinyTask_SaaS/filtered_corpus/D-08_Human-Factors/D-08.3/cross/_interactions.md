<!-- aegis:case-scope: GDPR, CRA — matrix tables filtered to active regulations; other tables retained verbatim -->
# D-08.3 — Cross-regulation interactions

> Inherently multi-regulation material: scope-overlap matrix, validated
> relationships, emergent tensions, aggregation logic, the multi-reg
> high-level requirement, HSO considerations, and non-participant notes.
> Consult only when ≥2 regulations are applicable. No per-regulation
> obligation lives here.

## Structural banners (merged Parts)

# Part 1 — Sub-domain definition

## Part 1 §1 — Cross-Regulation Analysis context

### 1. Cross-Regulation Analysis
> **Domain analysis:** [D-08.3 Management Board Training](../../DomainAnalysis/D-08_Human-Factors/D-08.3.md)
#### D-08.3 Management Board Training
<!-- participants: NIS2, DORA -->
**Participants (from CRDA):** NIS2, DORA
**Sole-authority / partial-coverage notes:** GDPR has no management-board training mandate (CRDA confirmed); CRA has no management-board training mandate; AI Act has no management-board training mandate (but AI Act Art. 4 AI-literacy may extend management-body competence to AI risk literacy — interplay with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 unresolved per CRDA).

## Part 1 §1 — Cross-Regulation Analysis context

### D-09 Governance & Documentation

## Part 1 §2 — HSO context

### 2. Hierarchical Security Objective
## D-08.3 Management Board Training
> **CRDA-deep provenance.** This section was generated from
> [`../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.3.md`](../../CrossRegulation/DeepAnalysis/D-08_Human-Factors/D-08.3.md)
> (1 pair verified against OJ text — **2 participating regulations
> are NIS 2, DORA; GDPR, CRA, AI Act are fully absent** as noted by
> `DomainAnalysis/D-08_Human-Factors/D-08.3.md`
> line 27: "Participants: NIS2, DORA" and lines 30–35:
> "GDPR has no management-board training mandate (CRDA confirmed);
> CRA has no management-board training mandate; AI Act does not impose
> a management-board training mandate (but AI Act Art. 4 AI-literacy
> may extend management-body competence to AI risk literacy — interplay
> with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 unresolved per
> CRDA)").
>
> **AI Act / GDPR / CRA absence note (per CRDA-deep §D-08.3 lines
> 27–29):** CRDA marks GDPR, CRA, and AI Act as out-of-scope for
> D-08.3 (no management-board training mandate). For a controller-only
> entity, a CRA-manufacturer-only entity, or an AI-Act-deployer-only
> entity, no D-08.3 sub-SO activates; the entity routes to D-08.1
> (general security awareness) and D-08.2 (role-specific competence)
> for the GDPR DPO-catalysed workforce/role-specific obligation and the
> CRA Annex II §8(f) integrator-B2B obligation. No GDPR, CRA, or AI
> Act pair is included in the D-08.3 verification.
>
> **CRDA-unresolved interplay note (per CRDA-deep §D-08.3 line 29 and
> DomainAnalysis §D-08.3 line 52):** AI Act Art. 4 (AI literacy)
> creates a parallel-but-unmapped obligation that may extend
> management-body competence to AI risk literacy — the interplay
> between AI Act Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1
> for management bodies deploying high-risk AI is **unresolved per
> CRDA**. This is preserved as a structural Layer 2 review item in
> this HSO and surfaced in the aggregation logic below.

## Participants (CRDA-deep, full table)

#### Participants (from CRDA-deep §D-08.3)
| Regulation | Canonical SO | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR has no management-board training mandate (CRDA confirmed). | — |
| NIS2 | SG-NIS2-020 | Members of the management bodies of essential and important entities follow cybersecurity training, gaining sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by entity (Art. 20(2) sentence 1). | Management-body training mandatory (Member-State-imposed — the binding force is on the MS, with the entity-side SR applying only where the MS has transposed); literacy prerequisite for Art. 20(1) approve+oversee+liable governance duties. |
| CRA | (out-of-scope) | CRA has no management-board training mandate (CRDA confirmed). | — |
| DORA | SG-DORA-014 | Members of the management body actively keep up to date with sufficient knowledge and skills, including by following specific training on a regular basis, commensurate to the ICT risk being managed (Art. 5(4)). | Direct entity-side obligation; OJ-literal anchor on `sufficient knowledge and skills` + `regular basis` + `commensurate to the ICT risk`; the literacy underpinning of Art. 5(2) management-body responsibility. |
| AI_Act | (out-of-scope) | AI Act does not impose a management-board-training mandate (CRDA confirmed). AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy — **interplay with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 unresolved per CRDA**. | — |

## Validated relationships (from CRDA-deep §D-08.3)

#### Validated relationships (from CRDA-deep §D-08.3)
Of 1 pair in the 2×2 matrix, **1 verified as SAME — EQUAL** — the two regulators look at management-board training from a **single regulatory perspective** (executive-literacy substrate for cybersecurity governance) with **distinct binding-force loci** (NIS 2: Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable governance duties; DORA: direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`). The EQUAL classification reflects this — both regulations require management-body training with the same operative target (senior-executive literacy + governance competence) and the same CSF substrate (PR.AT-02 + GV.RR-01), and the dominant-authority reading (DORA-dominant for DORA financial entities; NIS 2 is dominant for non-financial NSIEs) is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry. **No CONTRADICTORY reclassifications** and **no CORRECTED reclassifications** on the management-board-training duty itself. The **1 SAME — EQUAL pair** (verified) is:
- **NIS2 ↔ DORA** — EQUAL (SAME): Both regulations impose management-body training. DORA's OJ-literal anchor is direct (Art. 5(4) is the entity-side obligation `Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed`); NIS 2's anchor is indirect (Art. 20(2) sentence 1 is the Member-State obligation `Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity`, with the entity-side SR applying only where the Member State has transposed). For DORA financial entities, the DORA Art. 5(4) obligation is the dominant authority. Scope-disjoint test: **Y (when the DORA financial entity is also an NSIE applying management-body training)**. No reclassification required.
The management-board-training architecture is **legitimately diverse with binding-force asymmetry** — both regulators target a **single target audience** (senior executives / management body) at **distinct binding-force loci** (NIS 2: Member-State obligation — the entity-side SR applies only where the MS has transposed, per SR-NIS2-031 ambiguity_notes; DORA: direct entity-side obligation) with **distinct obligation anchors** (NIS 2 Art. 20(2) sentence 1 `Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` — literacy prerequisite for Art. 20(1) approve+oversee+liable governance duties; DORA Art. 5(4) `Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` — direct entity-side literacy underpinning of Art. 5(2) management-body responsibility). The high-level SO surfaces the **common management-body literacy duty** (executive-literacy substrate + governance competence + documented training records + personal-capacity threshold for approve+oversee+liable governance duties); the per-reg binding-force locus, target audience, trigger, anchor, threshold, recipient, and evidence template are preserved verbatim in the two sub-SOs.
The scope-overlap column in the matrix below indicates whether the same event can trigger both regulations on a single party; this is the gating condition for the high-level SO to engage.
|   |
| --- |
Legend: **Y** = scope overlap on a single event at a single party (high-level SO engages on the joint-condition operator). The single NIS2↔DORA pair is **SAME — EQUAL** per CRDA-deep verified classification — both regulations impose management-body training with the same operative target (senior-executive literacy + governance competence) and the same CSF substrate (PR.AT-02 + GV.RR-01). CRDA-deep scope-disjoint test: NIS2↔DORA = Y (when the DORA financial entity is also an NSIE applying management-body training) — no reclassification required.

## Cross-recipient map

#### Cross-recipient map
D-08.3 generates a layered recipient set on the **management-body-training evidence trail** but does **not generate a notification cascade of D-08.3 itself** (the management-body training is the upstream governance literacy input to the broader approve+oversee+liable governance architecture). The recipient set is at the **management-body-literacy evidence layer**: **NIS 2's management body + competent authority** on the Art. 20(2) sentence 1 + Art. 20(1) management-body approval+oversight+liability for the management-body training measures (with Member State transposition divergence preserved — the binding force is on the MS, with the entity-side SR applying only where the MS has transposed, per SR-NIS2-031 ambiguity_notes); **DORA's competent authority (national financial supervisory authority)** on the Art. 5(4) management-body training records + Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance + fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference). These are distinct regulatory channels on the same management-body-literacy evidence but they do not generate a notification cascade of D-08.3 itself — they are **compliance-evidence channels on the layered management-body-literacy programme**. The **AI Act's full absence from D-08.3** means there is no AI Act recipient on D-08.3 — the CRDA-unresolved interplay between AI Act Art. 4 (AI literacy) and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 is preserved as a structural Layer 2 review item (per CRDA-deep §D-08.3 line 29 and DomainAnalysis line 52). **D-08.1 (General Security Awareness) is the upstream awareness substrate** that D-08.3's management-body literacy presupposes (without trained management-body members, the Art. 20(1) approve+oversee+liable obligations cannot be meaningfully discharged, per SR-NIS2-031 regulatory_rationale); **D-08.2 (Role-Specific Competence) is the workforce-scale depth dimension** that D-08.3's executive-literacy layer supervises (D-08.3 management-body training is the governance-track counterpart to the D-08.2 role-specific workforce training, per SR-DORA-024 / SR-DORA-025 stack — the Art. 5(4) management-body training is the governance track; the Art. 13(6) `compulsory modules` is the workforce scale track); **D-09.1 (Information Security Policies) is where the management-body approve+oversee+liable architecture is operationalised** (NIS 2 Art. 20(1) sentence 1 first/second/third clause approve+oversee+liable; DORA Art. 5(2) `define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` + Art. 6(1) `sound, comprehensive and well-documented` framework), with D-08.3's management-body literacy the personal-capacity prerequisite. **D-09.3 (Compliance Management) is where the management-body-training records are integrated into the broader compliance-management register** (Art. 5(2) DORA + EBA Guidelines on ICT and security risk management supervisory baseline). The **CRDA-unresolved interplay note** is preserved as a structural Layer 2 review item: AI Act Art. 4 (AI literacy) may extend the management-body syllabus to AI risk literacy for entities deploying high-risk AI in NIS-critical / ICT-risk contexts; the interplay is **unresolved per CRDA**.
---

## HSO considerations (from D-08.3.0 — High-level SecurityObjective)

**Considerations.**
- 2 of 5 regulations participate (NIS 2, DORA); GDPR, CRA, AI Act are fully absent per CRDA-deep §D-08.3 (GDPR has no management-board training mandate; CRA has no management-board training mandate; AI Act does not impose a management-board-training mandate per CRDA — but AI Act Art. 4 AI literacy may extend management-body competence to AI risk literacy for entities deploying high-risk AI in NIS-critical / ICT-risk contexts, and the interplay is **unresolved per CRDA** as a structural Layer 2 review item).
- NIS 2 Art. 20(2) sentence 1 `Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` — Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable governance duties (binding force on the MS, with entity-side SR applying only where the MS has transposed, per SR-NIS2-031 ambiguity_notes).
- DORA Art. 5(4) `Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` — direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`, the literacy underpinning of Art. 5(2) management-body responsibility.
- 1 pairwise cell verified by CRDA-deep as SAME — EQUAL — both regulations impose management-body training with the same operative target (senior-executive literacy + governance competence) and the same CSF substrate (PR.AT-02 + GV.RR-01); the dominant-authority reading (DORA-dominant for DORA financial entities; NIS 2-dominant for non-financial NSIEs) is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry.
- The high-level SO engages on the Y-pair integrated stack when the DORA financial entity is also an NSIE applying management-body training.
- **The CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy for entities deploying high-risk AI) is preserved as a structural Layer 2 review item; the high-level SO does NOT collapse the CRDA-unresolved interplay into a presumed EQUAL or CONTRADICTORY classification; the AI Act Art. 4 layer is documented as an unresolved parallel-but-unmapped obligation that may add a sub-component to the management-body syllabus without a standalone management-body training mandate.
- 0 conditional emergent tensions — no CONTRADICTORY or CORRECTED reclassifications on the management-body training duty itself.
- The per-reg binding-force locus, target audience, trigger, anchor, threshold, recipient, and evidence template are preserved verbatim in the two sub-SOs.

## Sub-domain scope structure (full table)

#### Sub-domain scope structure (verified by CRDA-deep)
The 2 participating regulations each define D-08.3 over a **single target audience** (management body / senior executives) with **distinct binding-force loci**; the binding-force locus, the target audience, the trigger, the obligation anchor, the threshold, the recipient, and the legal anchor all depend on which perspective the regulation takes on the management-body training programme.
| Axis (reg) | Target audience | Trigger | Threshold anchor | Recipient | Legal anchor |
|---|---|---|---|---|---|
| **GDPR** | (out-of-scope) — GDPR has no management-board training mandate (CRDA confirmed); the DPO-catalysed workforce awareness under GDPR Art. 39(1)(b) is mapped to D-08.1 (general security awareness) and D-08.2 (role-specific competence), not D-08.3 | — | — | — | — |
| **NIS2** | members of the management bodies of essential and important entities (every member individually — the OJ does not provide a designation carve-out; the definition of `management body` is Member-State-determined under Article 6 / Recital 75) | Member-State obligation — the binding force of Art. 20(2) sentence 1 is on the Member State (`Member States shall ensure`); the entity-side SR applies only where the Member State has transposed, per SR-NIS2-031 ambiguity_notes (chosen reading: both reading — statute mandates, entity operationalises) | `sufficient knowledge and skills` (cybersecurity-specific reading dominant per the OJ's coordination with `cybersecurity risk-management practices`) + `required to follow training` (S3 ambiguity on the binding-force locus — statutory reading, entity-internal reading, or both reading; chosen reading: both reading); no quantitative cadence; the OJ does not enumerate the content — entity-internal programme with the chosen reading being entity-discretionary (formal certified training preferred where the entity seeks documented compliance evidence) | management body (Art. 20(1) approve+oversee+liable) + competent authority (national NIS 2 supervisory authority) — Art. 20(2) sentence 1 management-body training records + Art. 20(1) management-body approval minute + Member State supervisory review | Art. 20(2) sentence 1 `Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` + Art. 20(1) sentence 1 first/second/third clause approve+oversee+liable (literacy prerequisite) + Recital 75 (management-body engagement as a strategic discipline) + Art. 6 (definition of `management body` is Member-State-determined) |
| **CRA** | (out-of-scope) — CRA has no management-board training mandate (CRDA confirmed); the CRA-side output is the user-facing instructions at Annex II §8(a)–(f) (D-08.1 partial coverage) and the integrator-B2B information at Annex II §8(f) (D-08.2 partial coverage), not D-08.3 | — | — | — | — |
| **DORA** | members of the management body of the financial entity (the OJ does not provide a designation carve-out; the definition of `management body` is determined by the company-law / sectoral governance architecture and the EBA Guidelines on Internal Governance fit-and-proper framework) | direct entity-side obligation — Art. 5(4) `shall actively keep up to date` is the direct entity-side trigger; the literacy underpinning of Art. 5(2) management-body responsibility (define+approve+oversee+be responsible); the clause co-exists with EBA Guidelines on Internal Governance and with the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference) | `sufficient knowledge and skills` (S2 VAG on `sufficient` — chosen reading at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier) + `regular basis` (S2 VAG — chosen reading is risk-driven cadence per the literal `actively keep up to date` formulation) + `commensurate to the ICT risk being managed` (S2 VAG — chosen reading is risk-proportional rather than risk-quantified); no quantitative cadence; the OJ does not enumerate the content — entity-internal programme with evidence forms for `actively keep up to date` (training-attendance logs, assessment scores, peer-benchmark exercises) remaining for entity policy | management body (Art. 5(2) define+approve+oversee+be responsible) + NCA (national financial supervisory authority) — Art. 5(4) `actively keep up to date` records + Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance fit-and-proper framework + Art. 91 CRD + Art. 4(1)(36)/(37) MiFID II cross-reference | Art. 5(4) `Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` + Art. 5(2) management-body responsibility (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) + EBA Guidelines on Internal Governance fit-and-proper + CRD Art. 91 + MiFID II Art. 4(1)(36)/(37) |
| **AI_Act** | (out-of-scope) — AI Act does not impose a management-board-training mandate (CRDA confirmed). **CRDA-unresolved interplay note**: AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy for entities deploying high-risk AI in NIS-critical / ICT-risk contexts — interplay with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 **unresolved per CRDA** | — | — | — | — |

## Scope-overlap matrix (2×2)

#### Scope-overlap matrix (2×2)
(See the validated-relationships table above for the 2×2 matrix.)

## Scope-overlap principle (operational). The high-level SO

#### Scope-overlap principle (operational). The high-level SO
(`SG-D-08.3.HL`) engages on a given party **if and only if the same
party has both NIS 2 and DORA applicability with overlapping management-
body-training scope-determiners** (e.g. a DORA financial entity that is
also a NIS 2 essential entity — a vertically-integrated financial
entity with full NIS 2 + DORA applicability on the same management-
body-training substrate). For a non-financial NSIE that is not a
financial entity (NIS 2 only), the high-level SO does **NOT** engage
the joint-condition operator — only the NIS 2 sub-SO activates, and
the management-body training is discharged against the Art. 20(2)
sentence 1 Member-State-imposed literacy prerequisite. For a DORA
financial entity that is not an NSIE (DORA only — e.g. a smaller
financial entity below the NIS 2 essentiality threshold), the high-
level SO does **NOT** engage the joint-condition operator — only the
DORA sub-SO activates, and the management-body training is discharged
against the Art. 5(4) `actively keep up to date` + `commensurate to
the ICT risk` direct entity-side obligation. For a DORA financial
entity that is also a NIS 2 essential entity (DORA + NIS 2), the
high-level SO engages on the Y-pair integrated stack — both sub-SOs
activate, and the DORA Art. 5(4) obligation is the dominant authority
(the DORA `actively keep up to date` + `regular basis` + `commensurate
to the ICT risk` direct entity-side obligation discharges both DORA's
dedicated management-body obligation and NIS 2's Member-State-imposed
Art. 20(2) sentence 1 literacy prerequisite, per the EQUAL
classification and the dominant-authority reading). **The two binding-
force loci are layered, not collapsed**: NIS 2 Member-State-imposed
literacy prerequisite (the entity-side SR applies only where the MS
has transposed, per SR-NIS2-031 ambiguity_notes — both reading:
statute mandates, entity operationalises) vs DORA direct entity-side
obligation with `actively keep up to date` + `regular basis` +
`commensurate to the ICT risk`. The high-level SO surfaces the common
management-body literacy duty but does **NOT** collapse the per-reg
binding-force locus, target audience, trigger, anchor, threshold,
recipient, or evidence template. The **CRDA-unresolved interplay with
AI Act Art. 4** is preserved as a structural Layer 2 review item: for
an entity that deploys high-risk AI in NIS-critical / ICT-risk
contexts, the AI Act Art. 4 (AI literacy) layer may add a sub-component
to the management-body syllabus without a standalone management-body
training mandate; the interplay is **unresolved per CRDA** and is NOT
collapsed into a presumed EQUAL or CONTRADICTORY classification.

## Aggregation logic (from CRDA-deep verified classifications)

#### Aggregation logic (from CRDA-deep verified classifications)
- **2 of 5 regulations participate** (NIS 2, DORA — **2 participate,
  GDPR, CRA, AI Act are fully absent**, no out-of-scope on NIS 2 /
  DORA): NIS 2 (Art. 20(2) sentence 1 management-body training
  mandatory — Member-State-imposed; the entity-side SR applies only
  where the MS has transposed, per SR-NIS2-031 ambiguity_notes);
  DORA (Art. 5(4) `actively keep up to date` + `commensurate to the
  ICT risk` direct entity-side obligation; the literacy underpinning
  of Art. 5(2) management-body responsibility); GDPR (no management-
  board training mandate; DPO-catalysed workforce awareness under Art.
  39(1)(b) is mapped to D-08.1 and D-08.2, not D-08.3); CRA (no
  management-board training mandate; Annex II §8 user-facing
  instructions and §8(f) integrator-B2B information are mapped to
  D-08.1 partial and D-08.2 partial, not D-08.3); AI Act (no
  management-board training mandate per CRDA — but AI Act Art. 4 AI
  literacy creates a parallel-but-unmapped obligation that may extend
  management-body competence to AI risk literacy, **interplay
  unresolved per CRDA** as a structural Layer 2 review item).
- **1 pairwise cell, verified by CRDA-deep as SAME — EQUAL**:
  NIS2↔DORA (SAME — EQUAL — both regulations impose management-body
  training with the same operative target — senior-executive literacy
  + governance competence — and the same CSF substrate — PR.AT-02 +
  GV.RR-01; the EQUAL classification reflects this parallel;
  the dominant-authority reading — DORA-dominant for financial
  entities; NIS 2 is dominant for non-financial NSIEs — is the
  operational consequence of the DORA-direct-applicability vs NIS
  2-MS-transposition asymmetry). The 2×2 matrix is **C(2,2) = 1 pair**
  — 1 cell in the matrix is the same verified pair on both sides of
  the reciprocal table.
- The two participating regulations impose **management-body literacy
  duties** at a **single target audience** (senior executives /
  management body) with **distinct binding-force loci** (NIS 2:
  Member-State-imposed literacy prerequisite for Art. 20(1) approve+
  oversee+liable governance duties — the entity-side SR applies only
  where the MS has transposed, per SR-NIS2-031 ambiguity_notes; DORA:
  direct entity-side obligation with `actively keep up to date` +
  `regular basis` + `commensurate to the ICT risk`). The thresholds
  align qualitatively (no regulation imposes quantitative cadence —
  both are entity-discretionary under Recital 56 proportionality or
  risk-driven cadence per the literal `actively keep up to date`
  formulation). The two anchors align in their direction-of-travel
  (executive-literacy substrate calibrated to risk + governance
  competence + personal-capacity threshold for approve+oversee+liable
  duties) but the binding-force loci, evidentiary templates, and
  recipients diverge (NIS 2: management body + national NIS 2
  supervisory authority; DORA: management body + NCA + EBA Guidelines
  on Internal Governance fit-and-proper framework + CRD Art. 91 +
  MiFID II Art. 4(1)(36)/(37) cross-reference).
- The high-level SO describes the **COMMON OBJECTIVE** (executive-
  literacy substrate + governance competence + documented training
  records + personal-capacity threshold for approve+oversee+liable
  governance duties); the **per-regulation perspective** (binding-
  force locus, target audience, trigger, anchor, threshold, recipient,
  evidence template) is preserved verbatim in the two sub-SOs.
- The high-level SO does **NOT** resolve any conditional emergent
  tension — **0 emergent tensions on the management-body training
  duty itself**, because the single verified pair is SAME — EQUAL
  (no CONTRADICTORY, no CORRECTED). Phase 1C Doc 07 does not need to
  resolve a management-body-training contradiction because none
  exists by construction. The **EQUAL classification** reflects the OJ
  literal parallel between NIS 2 Art. 20(2) sentence 1 and DORA Art.
  5(4) on the management-body-training dimension; the dominant-
  authority reading is the operational consequence of the DORA-direct-
  applicability vs NIS 2-MS-transposition asymmetry, not a
  contradiction.
- **Scope caveat (CRITICAL — GDPR / CRA / AI Act full absence)** —
  derived from CRDA-deep verified classifications: GDPR has no
  management-board training mandate (CRDA confirmed); CRA has no
  management-board training mandate (CRDA confirmed); AI Act does
  not impose a management-board-training mandate (CRDA confirmed).
  For a controller-only entity (GDPR applicability), a CRA-
  manufacturer-only entity (CRA applicability), or an AI-Act-deployer-
  only entity (AI Act applicability), no D-08.3 sub-SO activates. The
  entity routes to D-08.1 (general security awareness) and D-08.2
  (role-specific competence) for the GDPR DPO-catalysed workforce
  awareness and role-specific training (Art. 39(1)(b)), the CRA
  Annex II §8(a)–(f) user-facing instructions (D-08.1 partial) and
  §8(f) integrator-B2B information (D-08.2 partial), and the AI
  Act Art. 14(4) 5-element human-oversight capability + Art. 26(2)
  4-element AND deployer assignment (D-08.2 + D-08.4 partial).
- **Scope caveat (CRITICAL — CRDA-unresolved interplay with AI Act
  Art. 4)** — derived from CRDA-deep §D-08.3 line 29 and
  DomainAnalysis §D-08.3 line 52: AI Act Art. 4 (AI literacy) creates
  a parallel-but-unmapped obligation that may extend management-body
  competence to AI risk literacy for entities deploying high-risk AI
  in NIS-critical / ICT-risk contexts. The interplay between AI Act
  Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 is
  **unresolved per CRDA** and is preserved as a structural Layer 2
  review item. The high-level SO does NOT collapse the CRDA-unresolved
  interplay into a presumed EQUAL or CONTRADICTORY classification; the
  AI Act Art. 4 layer is documented as an **unresolved parallel-but-
  unmapped obligation** that may add a sub-component to the management-
  body syllabus (extending the `sufficient knowledge and skills` to
  AI risk literacy) without a standalone management-body training
  mandate. For an entity that deploys high-risk AI in NIS-critical /
  ICT-risk contexts, the AI Act Art. 4 AI-literacy layer may add an
  AI-risk sub-component to the management-body syllabus; the HSO
  preserves the CRDA-unresolved note and surfaces it as a structural
  Layer 2 review item, not as a verified reclassification.
- **Scope caveat (CRITICAL — NIS 2 binding-force locus)** — derived
  from CRDA-deep verified classifications: NIS 2 Art. 20(2) sentence 1
  is a Member-State obligation (`Member States shall ensure`); the
  entity-side SR applies only where the Member State has transposed
  (per SR-NIS2-031 ambiguity_notes — the chosen reading is the both
  reading: statute mandates, entity operationalises, as the standard
  MS-implementation pattern). The DORA programme is dominant authority
  for DORA financial entities (Art. 5(4) direct entity-side obligation
  with `actively keep up to date` + `commensurate to the ICT risk`
  discharges both DORA's dedicated management-body obligation and
  NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy
  prerequisite, per the EQUAL classification and the downstream
  implication in CRDA-deep §D-08.3 line 68: "Phase 2 obligation
  derivation must produce a DORA-dominant stack: DORA Art. 5(4)
  `actively keep up to date` + `commensurate to the ICT risk`
  discharges both DORA's dedicated management-body obligation and
  NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy
  prerequisite for DORA financial entities").
- **Scope caveat (CRITICAL — DORA `commensurate to the ICT risk` as
  risk-proportional anchor)** — derived from CRDA-deep verified
  classifications: DORA Art. 5(4) `commensurate to the ICT risk being
  managed` is a risk-proportional anchor (S2 VAG — chosen reading is
  risk-proportional rather than risk-quantified, per SR-DORA-024
  ambiguity_notes). The `regular basis` is a risk-driven cadence per
  the literal `actively keep up to date` formulation. For a smaller
  DORA financial entity under Art. 4 proportionality, training evidence
  can be proportionate to risk exposure. The EQUAL classification
  preserves the OJ literal parallel between NIS 2 Art. 20(2) sentence 1
  `sufficient knowledge and skills` + `required to follow training`
  and DORA Art. 5(4) `sufficient knowledge and skills` + `regular
  basis` + `commensurate to the ICT risk` on the management-body-
  training dimension; the dominant-authority reading (DORA-dominant
  for DORA financial entities; NIS 2 is dominant for non-financial
  NSIEs) is the operational consequence of the DORA-direct-
  applicability vs NIS 2-MS-transposition asymmetry.
- **Scope caveat (CRITICAL — D-08.3 management-body training as
  governance-track counterpart to D-08.1 / D-08.2 workforce-scale
  awareness)** — derived from CRDA-deep verified classifications:
  D-08.3 management-body training is the **governance-track
  counterpart** to the D-08.1 general security awareness + D-08.2
  role-specific workforce competence stack. The Art. 5(4) management-
  body training is the governance track (D-08.3); the Art. 13(6)
  `compulsory modules` is the workforce scale track (D-08.1 + D-08.2
  partial). For an integrated financial-entity-controller with
  management-body training obligations, the DORA Art. 5(4) programme
  is the carrier on the governance track; the DORA Art. 13(6) programme
  is the carrier on the workforce scale track. The two regimes stack
  with the DORA programme as the carrier on both tracks and the GDPR
  data-protection awareness (Art. 39(1)(b) DPO-catalysed) + the NIS 2
  Art. 20(2) sentence 1 management-body literacy + the NIS 2 Art.
  20(2) sentence 2 Member-State-encouraged employee risk-identification
  training documented in sub-components.
---

## Emergent tensions (from CRDA-deep §D-08.3)

#### Emergent tensions (from CRDA-deep §D-08.3)
**0 conditional emergent tensions** on the management-body-training duty itself — no pair was verified as CONTRADICTORY or CORRECTED. The single verified pair (NIS2↔DORA) is SAME — EQUAL per CRDA-deep verified classification. **The CRDA-unresolved interplay note** is preserved as a structural Layer 2 review item, NOT as an emergent tension: AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy for entities deploying high-risk AI in NIS-critical / ICT-risk contexts — the interplay between AI Act Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 is **unresolved per CRDA** (per CRDA-deep §D-08.3 line 29 and DomainAnalysis §D-08.3 line 52: "The interplay between AI Act Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 for management bodies deploying high-risk AI is unresolved"). **No SCOPE-DISJOINT reclassifications** — CRDA preserves the single NIS2↔DORA pair as SAME — EQUAL rather than as SCOPE-DISJOINT. **No CONTRADICTORY pairs** on the management-body-training duty itself. The **binding-force asymmetry** (NIS 2: Member-State-imposed — the entity-side SR applies only where the MS has transposed, per SR-NIS2-031 ambiguity_notes; DORA: direct entity-side obligation) is the **legitimately diverse dimension** of the EQUAL pair: both regulators target the same single target audience (senior executives / management body) at **distinct binding-force loci**, and the operational convergence is on a **2-layer management-body-literacy architecture** with explicit binding-force hand-offs (NIS 2 Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable + DORA direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`) — the two binding-force loci stack with the DORA programme as the dominant authority for DORA financial entities and NIS 2 as the dominant authority for non-financial NSIEs.
The **AI Act / GDPR / CRA full absence** is the structurally significant structural divergence: only 2 of 5 regulations participate on D-08.3 (NIS 2, DORA). GDPR has no management-board training mandate (DPO-catalysed workforce awareness under Art. 39(1)(b) is mapped to D-08.1 and D-08.2, not D-08.3). CRA has no management-board training mandate (the Annex II §8 user-facing instructions and §8(f) integrator-B2B information are mapped to D-08.1 partial and D-08.2 partial, not D-08.3). AI Act does not impose a management-board-training mandate per CRDA (AI Act Art. 14(4) 5-element + Art. 26(2) 4-element AND are mapped to D-08.2, not D-08.3; AI Act Art. 4 AI literacy creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy, **interplay unresolved per CRDA**). For an entity with only GDPR applicability, only CRA applicability, or only AI Act applicability, no D-08.3 sub-SO activates; the entity routes to D-08.1 (general security awareness) and D-08.2 (role-specific competence) for the GDPR DPO-catalysed workforce awareness and role-specific training, the CRA Annex II §8 user-facing instructions and §8(f) integrator-B2B information, and the AI Act Art. 14(4) 5-element + Art. 26(2) 4-element AND deployer assignment respectively.
The **NIS 2 Member-State-imposed vs DORA direct-entity-side EQUAL classification** is the structurally significant EQUAL pair: both regulations impose management-body training with the same operative target (senior-executive literacy + governance competence) and the same CSF substrate (PR.AT-02 + GV.RR-01). The EQUAL classification preserves the OJ literal parallel between NIS 2 Art. 20(2) sentence 1 `required to follow training` + `sufficient knowledge and skills` and DORA Art. 5(4) `actively keep up to date` + `sufficient knowledge and skills` + `regular basis` + `commensurate to the ICT risk` on the management-body-training dimension; the dominant-authority reading (DORA-dominant for DORA financial entities; NIS 2 is dominant for non-financial NSIEs) is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry, per CRDA-deep §D-08.3 line 68: "Phase 2 obligation derivation must produce a DORA-dominant stack: DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities".
The **CRDA-unresolved interplay with AI Act Art. 4** is preserved as a structural Layer 2 review item — NOT collapsed into a presumed EQUAL or CONTRADICTORY classification: for an entity that deploys high-risk AI in NIS-critical / ICT-risk contexts, the AI Act Art. 4 (AI literacy) layer may add a sub-component to the management-body syllabus (extending the `sufficient knowledge and skills` to AI risk literacy) without a standalone management-body training mandate. The interplay is **unresolved per CRDA** and is NOT mapped to a sub-SO in this HSO. The high-level SO surfaces the common management-body literacy duty (NIS 2 + DORA); the AI Act Art. 4 layer is documented as an unresolved parallel-but-unmapped obligation awaiting Layer 2 review.
The high-level SO surfaces the common management-body literacy duty; the per-reg binding-force locus, target audience, trigger, anchor, threshold, recipient, and evidence template are documented separately in the two sub-SOs and the per-recipient evidence packs. **0 conditional emergent tensions** because no pair was verified as CONTRADICTORY or CORRECTED — the 2-layer management-body-literacy architecture (NIS 2 Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable + DORA direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`) with the DORA-dominant stack for DORA financial entities and the NIS 2-dominant stack for non-financial NSIEs is itself the binding-force reconciliation that supersedes any single-regulator reading. The **CRDA-unresolved AI Act Art. 4 interplay** is preserved as a structural Layer 2 review item awaiting accumulated supervisory practice and the European Commission's interpretive guidance.

## Downstream implication for Phase 1C Doc 07

#### Downstream implication for Phase 1C Doc 07
A company with ≥2 applicable regulations in scope of D-08.3 — with overlapping management-body-training scope-determiners on the same party (e.g. a DORA financial entity that is also a NIS 2 essential entity) — operates a **2-layer management-body-literacy architecture** with the DORA-dominant stack (DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities, per CRDA-deep §D-08.3 downstream implication in line 68). The high-level SO (`SG-D-08.3.HL`) describes the common management-body literacy duty (executive-literacy substrate + governance competence + documented training records + personal-capacity threshold for approve+oversee+liable governance duties); the per-reg perspective is preserved in the two sub-SOs (binding-force locus, target audience, trigger, anchor, threshold, recipient, evidence template). **The 0 conditional emergent tensions are documented as a binding-force reconciliation**, with the 2-layer management-body-literacy architecture (NIS 2 Art. 20(2) sentence 1 Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable → DORA Art. 5(4) direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`) operationalising the DORA-dominant stack for DORA financial entities and the NIS 2-dominant stack for non-financial NSIEs. The high-level SO does NOT collapse the two binding-force loci into a single management-body-literacy architecture; the per-reg perspective on binding-force locus, target audience, trigger, anchor, threshold, recipient, and evidence template is preserved verbatim. Phase 1C Doc 07 documents the **management-body-training strategy**: (1) a 2-layer management-body-literacy architecture with explicit binding-force hand-offs (NIS 2 Art. 20(2) sentence 1 Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable → DORA Art. 5(4) direct entity-side obligation with `actively keep up to date` + `regular basis` + `commensurate to the ICT risk`); (2) the DORA-dominant stack for DORA financial entities (Art. 5(4) discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite); (3) the AI Act / GDPR / CRA full absence as a structural Layer 2 review item (no D-08.3 sub-SO activates for controller-only, CRA-manufacturer-only, or AI-Act-deployer-only entities; the CRDA-unresolved interplay between AI Act Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 for management bodies deploying high-risk AI is preserved as a structural Layer 2 review item awaiting accumulated supervisory practice and the European Commission's interpretive guidance); (4) the D-08.3 management-body training as the **governance-track counterpart** to the D-08.1 general security awareness + D-08.2 role-specific workforce competence stack (the Art. 5(4) management-body training is the governance track; the Art. 13(6) `compulsory modules` is the workforce scale track). The DORA-dominant stack for DORA financial entities is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry, and the HSO does NOT collapse the binding-force loci into a presumed EQUAL reclassification with the DORA programme as a universal carrier; the NIS 2 Member-State-imposed literacy prerequisite is preserved verbatim as the upstream governance substrate for non-financial NSIEs and as the MS-supervised sub-component for DORA financial entities with MS-transposed Member-State obligations.

## Part 1 §3 — context

### 3. Security Requirements
## 8.3 Management Board Training — Volere requirements
> **Provenance.** Derived from `../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.3.md`. See that file for the CRDA-deep verified classification (1 pair NIS2↔DORA = SAME — EQUAL on the management-body-training dimension — no CORRECTED, no CONTRADICTORY; 2×2 matrix complete; **GDPR / CRA / AI Act are fully absent** per CRDA-deep §8.3 lines 27–29), the binding-force-asymmetry reasoning (NIS 2 Art. 20(2) sentence 1 = Member-State obligation; DORA Art. 5(4) = direct entity-side obligation), the dominant-authority reading (DORA-dominant for DORA financial entities; NIS 2-dominant for non-financial NSIEs), the CRDA-unresolved interplay note (AI Act Art. 4 AI literacy may extend management-body competence to AI risk literacy — interplay with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 **unresolved per CRDA**, preserved as a structural Layer 2 review item), the per-reg binding-force locus / target audience / trigger / anchor / threshold / recipient / evidence template, and the aggregation logic. This file adds Volere shell fields per the `../Volere_shell.md` template.

## Participating regulations (§3)

### Participating regulations
NIS 2, DORA (2 of 5 — GDPR, CRA, AI Act fully absent per CRDA-deep §8.3 line 27). The two regulators look at management-body training from a **single regulatory perspective** (executive-literacy substrate for cybersecurity governance) with **distinct binding-force loci** (NIS 2 Art. 20(2) sentence 1 Member-State-imposed literacy prerequisite for Art. 20(1) approve+oversee+liable; DORA Art. 5(4) `actively keep up to date` + `regular basis` + `commensurate to the ICT risk` direct entity-side obligation). The high-level SO surfaces the **common executive-literacy duty** (executive-literacy substrate + governance competence + documented training records + personal-capacity threshold for approve+oversee+liable governance duties); the per-reg binding-force locus is preserved verbatim in the two sub-SOs.
---

## High-level requirement (multi-reg aggregation)

### High-level requirement
```yaml
- req_id: 8.3
  volere_section: 15
  volere_subtype: immunity
  title: "Management bodies of essential and important entities and financial entities maintain an executive-literacy substrate through a documented management-body training programme"
  derives_from:
    hso_sub_so: SO-8.3.HL
    hso_file: ../../HierarchicalSecurityObjectives/D-08_Human-Factors/8.3.md
    objective_ref_section: "### 8.3.0"
  description: |
    The product shall establish and maintain a documented management-body training programme delivering executive-literacy substrate, governance competence, and documented training records with the personal-capacity threshold needed to discharge the Art. 20(1) NIS 2 approve+oversee+liable and the Art. 5(2) DORA define+approve+oversee+be-responsible governance duties, on the management-body audience, where ≥2 of the participating regulations (NIS 2, DORA) have applicability with overlapping management-body-training scope-determiners on the same party.
  fit_criterion: |
    A documented management-body training programme is maintained covering each member of the management body individually (the OJ does not provide a designation carve-out — the literal `members of the management bodies` reads as every member individually, per SR-NIS2-031 ambiguity reading); the programme content anchors the OJ purpose-clause objects — `sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices` (NIS 2 Art. 20(2) sentence 1) and `sufficient knowledge and skills … to enable them to understand and assess ICT risk and its impact on the operations of the financial entity` (DORA Art. 5(4)) — with PR.AT-02 executive-literacy substrate (each management-body member individually possesses documented evidence of training completion) + GV.RR-01 leadership-culture substrate (trained members discharge the approve+oversee+liable / define+approve+oversee+be-responsible obligations with informed judgement on a substantively-informed basis rather than ceremonial sign-off); the programme evidences `actively keep up to date` + `regular basis` + `commensurate to the ICT risk` against the DORA Art. 5(4) threshold for DORA financial entities (training-attendance logs + assessment scores + peer-benchmark exercises, with evidence forms remaining for entity policy per SR-DORA-024 ambiguity_notes); for non-financial NSIEs the programme evidences the `required to follow training` + `sufficient knowledge and skills` threshold with the both-reading binding-force locus (statute mandates, entity operationalises, per SR-NIS2-031 ambiguity_notes) and is operationalised under Art. 20(1) management-body approval minute (cross-ref 9.1.2) + Art. 21(2)(a) policy artefact (cross-ref 9.1.2); for a DORA financial entity that is also a NIS 2 NSIE the DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` direct entity-side obligation discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite on the DORA-dominant stack (per CRDA-deep §8.3 NIS2↔DORA verified relationship — DORA-dominant for financial entities); for an entity that deploys high-risk AI the CRDA-unresolved interplay note is preserved — the AI Act Art. 4 AI-literacy layer may add a sub-component to the management-body syllabus (extending `sufficient knowledge and skills` to AI risk literacy) without a standalone management-body training mandate; the programme is documented under Art. 5(2) DORA accountability / Art. 21(1) NIS 2 documented-policy chapeau so the entity can demonstrate on the day of any supervisory inspection that the Art. 20(2) sentence 1 + Art. 5(4) management-body training function was operationally exercised and recorded; the programme couples with 8.1 general security awareness (workforce-scale upstream substrate) and 8.2 role-specific competence (workforce-scale depth dimension) without collapsing the governance-track / workforce-scale track distinction (per CRDA-deep §8.3 scope caveat on management-body training as governance-track counterpart); verified by management-body training programme documentation review + per-individual-member training-completion records + Art. 20(2) sentence 1 / Art. 5(4) supervisory-evidence pack + NCA / national NIS 2 supervisory authority review.
  priority: MUST
  verification_method: TEST
  dependencies: [8.3.1, 8.3.2]
  nist_csf: [PR.AT-02, GV.RR-01]
  applicable_if:
    regs: [NIS2, DORA]
    scope_overlap: conditional   # HL engages only when ≥1 pair with Y scope overlap exists (NIS2↔DORA = Y when DORA financial entity is also an NSIE applying management-body training); for non-financial NSIE only (NIS 2 only) or DORA-only financial entity (not an NSIE), the per-reg sub-SO discharges the obligation and the HL is redundant but emitted for traceability
  satisfaction:
    controls: []
    nodes: []
  considerations: |
    The high-level SO surfaces the **common executive-literacy duty** (executive-literacy substrate + governance competence + documented training records + personal-capacity threshold for approve+oversee+liable governance duties) converging across NIS 2 Art. 20(2) sentence 1 + DORA Art. 5(4); the **per-reg binding-force locus** (NIS 2 Member-State-imposed vs DORA direct entity-side) is preserved verbatim in the two sub-SOs. The 1 verified pair (NIS2↔DORA = SAME — EQUAL) reflects the OJ-literal parallel between `required to follow training` + `sufficient knowledge and skills` (NIS 2) and `actively keep up to date` + `sufficient knowledge and skills` + `regular basis` + `commensurate to the ICT risk` (DORA) on the management-body-training dimension; the dominant-authority reading is the operational consequence of the DORA-direct-applicability vs NIS 2-MS-transposition asymmetry. The **CRDA-unresolved interplay note** (AI Act Art. 4 may extend management-body competence to AI risk literacy) is preserved as a structural Layer 2 review item and does NOT collapse into a presumed EQUAL or CONTRADICTORY classification. **GDPR, CRA, AI Act fully absent** per CRDA-deep §8.3 line 27 — GDPR has no management-board training mandate (DPO-catalysed workforce awareness under Art. 39(1)(b) is mapped to 8.1 / 8.2, not 8.3); CRA has no management-board training mandate (Annex II §8 user-facing instructions + §8(f) integrator-B2B information are mapped to 8.1 partial / 8.2 partial, not 8.3); AI Act does not impose a management-board-training mandate per CRDA (the Art. 4 AI-literacy layer is a parallel-but-unmapped obligation that may add a sub-component to the syllabus without a standalone management-body training mandate). (Copied from the HSO Considerations block of `### 8.3.0`; preserved here for self-contained traceability.)
```
---

## Sub-requirements section heading

### Sub-requirements

## Structural banners (merged Parts)

# Part 2 — Domain Analysis (cross-regulation)

## Part 2 — Domain Analysis (summary layer)

---
document_id: AEGIS-PREPROC-CRDA-D-08.3
title: D-08.3 Management Board Training — Cross-Regulation Domain Analysis
phase: Pre-processing (Regulatory Baseline) — static cross-regulation analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.3 Management Board Training
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DeepAnalysis/D-08_Human-Factors/D-08.3.md
status: DRAFT
---
> **Deep analysis:** [D-08.3 Management Board Training](../../DeepAnalysis/D-08_Human-Factors/D-08.3.md)
#### D-08.3 Management Board Training
<!-- participants: NIS2, DORA -->
##### Participants
| Regulation | SO ID | 1-line summary | Scope/angle |
|---|---|---|---|
| GDPR | (out-of-scope) | GDPR has no management-board training mandate. | — |
| NIS2 | SG-NIS2-020 | Members of the management bodies follow cybersecurity training with sufficient knowledge and skills (Art. 20(2) sentence 1). | Management-body training mandatory (Member State obligation); literacy prerequisite for governance duties. |
| CRA | (out-of-scope) | No management-board training mandate in CRA. | — |
| DORA | SG-DORA-014 | Members of the management body actively keep up to date with sufficient knowledge and skills through specific training on a regular basis, commensurate to the ICT risk being managed (Art. 5(4)). | Direct entity-side obligation; OJ-literal anchor on `sufficient knowledge and skills` + `commensurate to the ICT risk`. |
| AI_Act | (out-of-scope) | AI Act does not impose a management-board-training mandate. | — |
##### Pairwise matrix

## Part 2 — Domain Analysis (summary layer)

<!-- /pair -->
##### Emergent tensions (2 regulations)
- Only 2 regulations have non-zero coverage. No 3-regulation emergent tension exists. Note: AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy, but the AI Act does not impose a training mandate on the management body per se. The interplay between AI Act Art. 4 and DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 for management bodies deploying high-risk AI is unresolved.
##### SR cross-validation
Both regulations map D-08.3 to the NIST CSF 2.0 Subcategories **PR.AT-02** (Senior executives understand their roles) and **GV.RR-01** (Organisational leadership responsible and accountable for cybersecurity risk) as the convergent pair. The Subcategory mapping reflects the executive-literacy substrate.
##### Downstream implication
Phase 1 entities must implement management-body training programmes that satisfy both DORA Art. 5(4) (direct, ICT-risk-commensurate) and NIS 2 Art. 20(2) sentence 1 (Member-State-imposed, literacy prerequisite). The DORA programme is the dominant authority for financial entities. AI Act Art. 4 AI-literacy obligations may extend the syllabus without a standalone management-body training mandate.
---
### D-09 Governance & Documentation
---

## Structural banners (merged Parts)

# Part 3 — Deep Analysis (per-pair)

## Part 3 — context

---
document_id: AEGIS-PREPROC-CRDA-DEEP-D-08.3
title: D-08.3 Management Board Training — Cross-Regulation Deep Analysis
phase: Pre-processing (Regulatory Baseline) — OJ-text-verified pairwise analysis
version: 0.1
created: 2026-07-09
updated: 2026-07-09
parent: ./index.md
macro_domain: D-08 Human Factors
sub_domain: D-08.3 Management Board Training
related_documents:
  - ../../../Regulation/GDPR/02_SecurityRules_NIST.md
  - ../../../Regulation/NIS2/02_SecurityRules_NIST.md
  - ../../../Regulation/CRA/02_SecurityRules_NIST.md
  - ../../../Regulation/DORA/02_SecurityRules_NIST.md
  - ../../../Regulation/AI_Act/02_SecurityRules_NIST.md
  - ../../DomainAnalysis/D-08_Human-Factors/D-08.3.md
status: DRAFT
---
> **Domain analysis:** [D-08.3 Management Board Training](../../DomainAnalysis/D-08_Human-Factors/D-08.3.md)
#### D-08.3 Management Board Training
<!-- participants: NIS2, DORA -->
**Participants (from CRDA):** NIS2, DORA
**Sole-authority / partial-coverage notes:** GDPR has no management-board training mandate (CRDA confirmed); CRA has no management-board training mandate; AI Act has no management-board training mandate (but AI Act Art. 4 AI-literacy may extend management-body competence to AI risk literacy — interplay with DORA Art. 5(4) / NIS 2 Art. 20(2) sentence 1 unresolved per CRDA).

## Part 3 — context

### D-09 Governance & Documentation
---

## Structural banners (merged Parts)

# Part 4 — Relevant Ambiguity (by regulation)

## Residual pair content (AI_Act, deep)

##### Pair: AI_Act ↔ [not in CRDA D-08.3 participants]
> **Note:** AI Act is not a D-08.3 participant per CRDA (no management-board training mandate). However, AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy — see CRDA emergent tension D-08.3. No pair analysis is included here.
---

## Residual pair content (AI_Act, deep3)

##### Pair: AI_Act ↔ [not in CRDA D-08.3 participants]
> **Note:** AI Act is not a D-08.3 participant per CRDA (no management-board training mandate). However, AI Act Art. 4 (AI literacy) creates a parallel-but-unmapped obligation that may extend management-body competence to AI risk literacy — see CRDA emergent tension D-08.3. No pair analysis is included here.
---
