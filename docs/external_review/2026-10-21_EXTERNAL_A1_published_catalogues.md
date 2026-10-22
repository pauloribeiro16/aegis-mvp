---
document_id: AEGIS-EXT-A1-2026-10-21
title: 'External A1 — the published identifier catalogues, transcribed'
version: 1.0.0
created: 2026-10-21
status: 'PROVENANCE RECORD — published identifier lists returned by the external normative audit; NOT yet verified against the published standards'
source: 'External model, response to A1 in docs/external_review/2026-10-21_AEGIS_context_briefing_for_external_review.md'
---

# External A1 — the published identifier catalogues

> **What this file is.** On 2026-10-21 an external model, given the repository and
> the A1 brief, returned the *published* identifier space of the standards our
> advisory referentials claim to instantiate. Those lists are the input ADR-014's
> signpost was waiting for ("the published control list returned by the external
> normative audit").
>
> **What this file is not.** It is **not** a verified catalogue. It is one
> external source, at the model's own confidence grade ALTA, transcribed verbatim
> so that the mapping work has a durable source and a single place to be checked
> against. Every list below is **pending verification against the published
> standard**. Nothing here has been applied to the baseline; ADR-014's signpost
> fired, but the *decision* of how to re-file the local cards is still open
> (see §5).

## 1. How the external source was obtained, and what it could see

The external model read the repository through a `.zip` whose directory listing
was truncated and whose file contents were DEFLATE-compressed streams it could
not decompress. Consequences, verified locally on 2026-10-21:

- It could read **directory and file names** and the **aggregator** JSONs
  (`<FRAMEWORK>.json`, `_MANIFEST.json`), but **not** the per-control leaf
  contents. Its own answer says so: *"Conteúdo textual interno de cada folha
  JSON … NOT VERIFIABLE na árvore .zip anexada (os 600+ ficheiros estão
  comprimidos em fluxos DEFLATE binários)"*.
- It read **`master` (`3e293abd`)**, not the working branch. The QNRCS referential
  and the whole Phase 3 Part 1 work exist only on
  `feat/phase3-part1-coverage-mapping`; its "QNRCS ausente" row is therefore
  correct **for the snapshot it read**, not a defect of the referential.
- Its **counts** are therefore estimates and several are wrong (see §4). Its
  **published** columns are its own knowledge of the standards, and those are
  the deliverable.

**The next audit must read the branch and the leaves.** A bundle with the four
referentials under question in readable form, plus the specs, is at
`/tmp/aegis_review_bundle.tar.gz` (rebuild command in §6).

## 2. ISO/IEC 42001:2023 — Annex A, 38 published controls

**The structural rule the external source states (confidence ALTA):** in Annex A
the `.1` position of each section is the **control objective** title, never a
selectable control; all controls therefore begin at `.2`. Section A.6 is
structured at **four levels** (A.6.1.x, A.6.2.x).

| Section | Published controls (count) | Titles as returned |
|---|---|---|
| A.2 Policies related to AI | 3 | A.2.2 AI policy · A.2.3 Alignment with other organizational policies · A.2.4 Review of the AI policy |
| A.3 Internal organization | 2 | A.3.2 AI roles and responsibilities · A.3.3 Reporting of concerns |
| A.4 Resources for AI systems | 5 | A.4.2 Resource documentation · A.4.3 Data resources · A.4.4 Tooling resources · A.4.5 System and computing resources · A.4.6 Human resources |
| A.5 Assessing impacts of AI systems | 4 | A.5.2 AI system impact assessment process · A.5.3 Documentation of AI system impact assessments · A.5.4 Assessing AI system impact on individuals or groups of individuals · A.5.5 Assessing societal impacts of AI systems |
| A.6 AI system life cycle | 9 | A.6.1.2 Objectives for responsible development of AI system · A.6.1.3 Processes for responsible AI system design and development · A.6.2.2 AI system requirements and specification · A.6.2.3 Documentation of AI system design and development · A.6.2.4 AI system verification and validation · A.6.2.5 AI system deployment · A.6.2.6 AI system operation and monitoring · A.6.2.7 AI system technical documentation · A.6.2.8 AI system recording of event logs |
| A.7 Data for AI systems | 5 | A.7.2 Data for development and enhancement of AI system · A.7.3 Acquisition of data · A.7.4 Quality of data for AI systems · A.7.5 Data provenance · A.7.6 Data preparation |
| A.8 Information for interested parties of AI systems | 4 | A.8.2 System documentation and information for users · A.8.3 External reporting · A.8.4 Communication of incidents · A.8.5 Information for interested parties |
| A.9 Use of AI systems | 3 | A.9.2 Processes for responsible use of AI systems · A.9.3 Objectives for responsible use of AI system · A.9.4 Intended use of the AI system |
| A.10 Third-party and customer relationships | 3 | A.10.2 Allocating responsibilities · A.10.3 Suppliers · A.10.4 Customers |

**Consequence for us.** Our local referential has **33** cards against **38**
published controls, spread differently (we hold 2/6/4/3/13/4/1 across A.2–A.8;
the published counts are 3/2/5/4/9/5/4/3/3). There is **no 1:1 mapping**: our
A.6 family carries 13 local cards against 9 published controls at four levels,
and two published sections (A.9, A.10) are absent. Any realignment is therefore
a **content-mapping exercise, not a renumbering** — see §5.

## 3. ISO/IEC 27701:2019 — Annexes A and B, 49 published controls

**The structural rule the external source states (confidence ALTA):** the 2019
edition numbers **Annex A as `A.7.x.y`** (mirroring Clause 7, PII controllers)
and **Annex B as `B.8.x.y`** (mirroring Clause 8, PII processors). The
standalone 2025 edition renumbered these to A.1.2.2–A.1.5.5 and A.2.2.2–A.2.5.9.

**Annex A — PII controllers (31):**

| Section | Published controls |
|---|---|
| A.7.2 Conditions for collection and processing (8) | A.7.2.1 Identify and document purpose · A.7.2.2 Identify lawful basis · A.7.2.3 Determine when and how consent is to be obtained · A.7.2.4 Obtain and record consent · A.7.2.5 Privacy impact assessment · A.7.2.6 Contracts with PII processors · A.7.2.7 Joint PII controller · A.7.2.8 Records related to processing PII |
| A.7.3 Obligations to PII principals (10) | A.7.3.1 … A.7.3.10 — Determining and fulfilling obligations · Determining information · Providing information · Providing mechanism to modify or withdraw consent · Providing mechanism to object · Access, correction and/or erasure · Informing third parties · Providing copy of PII processed · Handling requests · Automated decision making |
| A.7.4 Privacy by design and privacy by default (9) | A.7.4.1 … A.7.4.9 — Limit collection · Limit processing · Accuracy and quality · PII minimization objectives · De-identification and deletion at the end of processing · Temporary files · Retention · Disposal · PII transmission controls |
| A.7.5 PII sharing, transfer, and disclosure (4) | A.7.5.1 Identify basis for transfer between jurisdictions · A.7.5.2 Countries and international organizations to which PII can be transferred · A.7.5.3 Records of transfer of PII · A.7.5.4 Records of PII disclosure to third parties |

**Annex B — PII processors (18):**

| Section | Published controls |
|---|---|
| B.8.2 Conditions for collection and processing (6) | B.8.2.1 Customer agreement · B.8.2.2 Organization's purposes · B.8.2.3 Marketing and advertising use · B.8.2.4 Infringing instruction · B.8.2.5 Customer obligations · B.8.2.6 Records related to processing PII |
| B.8.3 Obligations to PII principals (1) | B.8.3.1 Obligations to PII principals |
| B.8.4 Privacy by design and privacy by default (3) | B.8.4.1 Temporary files · B.8.4.2 Return, transfer or disposal of PII · B.8.4.3 PII transmission controls |
| B.8.5 PII sharing, transfer, and disclosure (8) | B.8.5.1 Basis for transfer between jurisdictions · B.8.5.2 Countries and international organizations to which PII can be transferred · B.8.5.3 Records of PII disclosures to third parties · B.8.5.4 Notification of PII disclosure requests · B.8.5.5 Legally binding PII disclosures · B.8.5.6 Disclosure of subcontractors used to process PII · B.8.5.7 Engagement of a subcontractor to process PII · B.8.5.8 Change of subcontractor to process PII |

**This contradicts an earlier internal reading** that placed the processor-side set
at A.6.11/A.6.12 and treated A.5.34 as the root of both. The external structure
is the coherent one: the annexes mirror the clauses (7 and 8), and the four
levels are `A.7.<section>.<control>`. Our local `A.5.34.n.m` / `A.6.34.n.m`
scheme is synthetic in all 35 cards, and `A.5.34` collides with ISO/IEC
27001:2022's own A.5.34.

## 4. The other referentials — what the external source returned

| Referential | Published space (as returned) | Our local state (verified locally, 2026-10-21) | Verdict on the finding |
|---|---|---|---|
| **NIST AI SSDF** (SP 800-218A) | keeps the SSDF v1.1 ids exactly (PO.1.1..RV.3.3) and adds 3 tasks (PW.1.4, PW.4.5, RV.1.4); **no id carries an `.AI.` infix** | 17 cards, **all 17** with the invented `.AI.` infix (PO.AI.1, PS.AI.1, PW.AI.1, RV.AI.1…) | **CONFIRMED** — 17/17 ids resolve to no published task |
| **NIST SSDF** (SP 800-218 v1.1) | 42 active tasks in 19 practices; PW.3.1, PW.3.2, PW.4.2, PW.4.3, PW.5.2 **Withdrawn**; PS.2 and PS.3 have only `.1` | 44 cards; PW.8.1/8.2, PW.9.1/9.2, RV.1.3, RV.3.3 **absent**; PS.2.2 and PS.3.2 **present** (and should not be); PW.3.1, PW.3.2, PW.4.2, PW.4.3, PW.5.2 **present** | **CONFIRMED except one**: PO.1.3 is **present** locally (the source listed it as omitted) |
| **OWASP SAMM v2.0** | 15 practices: G-SM, G-PC, G-EG, D-TA, D-SR, D-SA, I-SB, I-SD, I-DM, V-AA, V-RT, V-ST, O-IM, O-EM, O-OM | 15 cards; **exactly 7** are v1.0-era or synthetic: G.SR.1, D.TM.1, V.AR.1, V.TE.1, O.IS.1, O.MM.1, O.OE.1 (the other 8 match by name in dot form) | **CONFIRMED, precisely 7 of 15** |
| **NIST SP 800-53 Rev 5** | ~325 base controls; CA-4 (→CA-2) and RA-4 (→RA-3) Withdrawn | 274 cards; CA-04 and RA-04 **present**; **all 23** claimed-active omissions confirmed absent (AC-09, AC-16, AU-14, AU-16, RA-06..RA-10, SC-47..SC-51, SI-14..SI-23) | **CONFIRMED** — and note the source's count of 241 is wrong (we hold 274) |
| **CIS Controls v8** | 18 controls ("1".."18") + **153 safeguards** ("1.1".."18.5") mapped to IG1/IG2/IG3 | 18 cards, ids "01".."18", **0/153** safeguards | **CONFIRMED** (unchanged from §7 of the briefing) |
| **ENISA** | no unified published id scheme; the technical guidance is *Technical Implementation Guidance on Cybersecurity Risk Management Measures* (Jun 2024) | 28 cards, all local taxonomy, of which 11 (`NIS2-21-1..11`) mirror NIS2 Art. 21(2)(a)–(j) plus an umbrella card, with **0** consumers outside the folder | **CONFIRMED in kind** — the source's own count of the Art. 21(2) alíneas is 10, and our 11th file is the umbrella |
| **BSI IT-Grundschutz, Edition 2023** | 111 Bausteine in 10 layers: ISMS, ORP, CON, OPS, DER, APP, SYS, IND, NET, INF. **CON = Konzepte und Vorgehensweisen** (CON.1 Kryptokonzept, CON.2 Datenschutz, CON.3 Datensicherungskonzept) — *not* containerisation. IAM → ORP.4; PKI → CON.1; directory services → APP.2.1/2.2/2.3; containers → SYS.1.6; Kubernetes → APP.4.4; detection & reaction → DER.1..DER.4 | 35 cards; our `CON` family holds containerisation (should be SYS.1.6 / APP.4.4), our `IDM` family holds identity/PKI/federation (should be ORP.4 / CON.1 / APP.2.x), and OPS.1/APP.1..5/NET.1..4/SYS.1..4 are 2-level collapses of 3–4 level Bausteine | **CONFIRMED — and assumption A10 fires** (our reading of `CON` as containerisation was wrong) |

**Counts the external source got wrong** (verified locally): NIST SP 800-53 241
(actual 274), NIST SSDF 42 active / 44 cards (actual 44 cards), BSI 31 (actual
35 — and its own table sums to 35), ISO 27701 35 cards (correct), NIST AI SSDF
17 (correct), OWASP ASVS 83 (correct), ENISA 28 (correct).

## 5. What this opens, and what it does not decide

**Open, and now actionable:** ADR-014's signpost condition 1 (*the published
Annex A becomes available*) has fired, so D2 — *"the intra-section ordinal is a
local subset ordinal"* — is retirable. The 27701 identifiers can be re-filed
onto the published A.7.x.y / B.8.x.y space. The BSI families can be re-filed
onto the published Bausteine.

**Not decided, and it is a real decision:** our local cards are **not** the
published controls. 33 local cards against 38 published controls for 42001;
35 against 49 for 27701; 35 against 111 for BSI. A re-file has to choose, per
card, between:

1. **adopt** the published id (the card paraphrases that control);
2. **demote** the card to a local, non-published extension (no published id
   asserted — the pattern already used by ADR-014 D3 for the BSI `IDM` family);
3. **drop** the card (the published control is covered by another card, or the
   card was a filler).

Options 2 and 3 change the *size* of the referential and therefore what an agent
can cite from it — that is a methodology call (the researcher's), not an
executor's. **Nothing has been re-filed yet.**

## 6. Rebuilding the audit bundle

```bash
tar -czf /tmp/aegis_review_bundle.tar.gz \
  docs/external_review/2026-10-21_AEGIS_context_briefing_for_external_review.md \
  docs/external_review/2026-10-21_EXTERNAL_A1_published_catalogues.md \
  docs/decisions/ADR-2026-10-21_advisory-referential-nomenclature.md \
  scripts/specs/ config.yaml \
  baseline/CONTROLS/ISO_42001_2023/ baseline/CONTROLS/ISO_27701_2019/ \
  baseline/CONTROLS/CIS_CONTROLS_V8/ baseline/CONTROLS/BSI_GRUNDSCHUTZ/ \
  baseline/CONTROLS/NIST_SSDF/ baseline/CONTROLS/NIST_AI_SSDF/ \
  baseline/CONTROLS/NIST_SP_800_53R5/ baseline/CONTROLS/OWASP_SAMM/ \
  baseline/CONTROLS/*/*.json \
  pipeline/src/aegis_pipeline/phases/phase3/weave.py \
  pipeline/src/aegis_pipeline/phases/phase3/verdicts.py \
  pipeline/src/aegis_pipeline/phases/phase3/schemas.py \
  pipeline/src/aegis_pipeline/phases/phase3/skeleton.py \
  pipeline/src/aegis_pipeline/phases/phase1/goals.py \
  pipeline/src/aegis_pipeline/guards/quality_gates.py \
  pipeline/src/aegis_pipeline/guards/controls.py \
  pipeline/tests/phase3_gate_test.py \
  scripts/doc_lint.py scripts/check_traceability.py
```

The leaves of the six NIST/OWASP referentials were added to this bundle
relative to the one sent for A1: the A1 findings for those frameworks were made
from **file names only**, and a re-audit needs the texts.
