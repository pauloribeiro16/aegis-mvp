<!-- excessive-reclassification-v1 -->

# Reclassification note on `excessive` entries (M7 follow-up)

The auditor's M7 pass flagged 78 entries as `excessive`. A targeted re-read (independent of the auditor's heuristic) distinguishes two cases:

| Kind | Count | Meaning | Fix? |
|---|---|---|---|
| **literal duplicates** (same ID listed more than once within one objective's anchor list) | 78 | mechanical noise; fixable with `dedupe_objective_anchors.py` | yes (idempotent, 0 occurrences in this corpus) |
| **cross-block overlap** (a Sub-SO card and one of its Volere requirements share the same anchor set) | 0 | intentional — the requirement's `nist_csf:` references the consolidated Sub-SO anchors; this is how the corpus is structured | no — these are not redundant |

`dedupe_objective_anchors.py` was written and run; it reports 0 changes (the audit's 78 'excessive' verdicts are all of the cross-block kind). No corpus file has been modified.

## Literal duplicates (none in this corpus)

- ### D-01.1 · DORA · subso SO-D-01.1.DORA: {'PR.DS-01': 2, 'PR.DS-02': 2, 'PR.DS-10': 2}
- ### D-01.2 · DORA · subso SO-D-01.2.DORA: {'PR.DS-01': 2, 'PR.DS-02': 2, 'PR.DS-10': 2}
- ### D-01.3 · CRA · subso SO-D-01.3.CRA: {'PR.DS-01': 2, 'PR.AA-05': 2, 'GV.OV-01': 2}
- ### D-01.3 · DORA · subso SO-D-01.3.DORA: {'PR.AA-03': 4, 'PR.AA-04': 2, 'PR.DS-01': 4, 'GV.RM-04': 2}
- ### D-01.3 · GDPR · subso SO-D-01.3.GDPR: {'PR.DS-01': 6, 'PR.IR-03': 2}
- ### D-01.4 · AI_Act · subso SO-D-01.4.AI_Act: {'PR.IR-03': 2, 'PR.IR-04': 4, 'PR.DS-11': 2}
- ### D-01.4 · CRA · subso SO-D-01.4.CRA: {'PR.DS-01': 2, 'PR.DS-10': 2, 'PR.PS-04': 2}
- ### D-01.4 · DORA · subso SO-D-01.4.DORA: {'PR.DS-01': 3, 'PR.DS-02': 3, 'PR.DS-10': 3, 'ID.AM-05': 2}
- ### D-01.4 · GDPR · subso SO-D-01.4.GDPR: {'PR.DS-01': 2, 'ID.AM-08': 3, 'PR.DS-10': 2}
- ### D-02.1 · CRA · subso SO-D-02.1.CRA: {'ID.RA-01': 2, 'ID.AM-02': 3, 'PR.PS-02': 2}
- ### D-02.1 · DORA · subso SO-D-02.1.DORA: {'ID.RA-01': 2, 'ID.RA-03': 2, 'GV.OV-02': 2}
- ### D-02.1 · GDPR · subso SO-D-02.1.GDPR: {'ID.RA-01': 2, 'PR.PS-02': 2, 'ID.RA-05': 2, 'ID.IM-02': 2}
- ### D-02.1 · NIS2 · subso SO-D-02.1.NIS2: {'ID.RA-01': 2, 'GV.SC-04': 2}
- ### D-02.3 · NIS2 · subso SO-D-02.3.NIS2: {'ID.RA-01': 2, 'GV.SC-04': 2}
- ### D-02.4 · AI_Act · subso SO-D-02.4.AI_Act: {'ID.RA-01': 3, 'ID.RA-04': 6, 'PR.PS-06': 3, 'GV.SC-04': 3}
- ### D-02.4 · CRA · subso SO-D-02.4.CRA: {'ID.RA-01': 6, 'PR.PS-06': 3, 'DE.CM-09': 3}
- ### D-03.1 · CRA · subso SO-D-03.1.CRA: {'PR.AA-01': 2, 'ID.AM-01': 2, 'PR.AA-05': 2, 'PR.AA-06': 2, 'DE.CM-09': 2}
- ### D-03.1 · DORA · subso SO-D-03.1.DORA: {'PR.AA-03': 4, 'PR.AA-04': 2}
- ### D-03.1 · GDPR · subso SO-D-03.1.GDPR: {'PR.AA-03': 2, 'PR.AA-02': 3, 'ID.AM-08': 2}
- ### D-03.1 · NIS2 · subso SO-D-03.1.NIS2: {'PR.AA-01': 3, 'PR.AA-05': 4, 'PR.AT-02': 2}
- ### D-03.2 · CRA · subso SO-D-03.2.CRA: {'PR.AA-01': 4, 'PR.AA-05': 4, 'PR.AA-06': 4, 'ID.AM-01': 2, 'DE.CM-09': 2}
- ### D-03.2 · DORA · subso SO-D-03.2.DORA: {'PR.AA-03': 4, 'PR.AA-04': 2}
- ### D-03.2 · NIS2 · subso SO-D-03.2.NIS2: {'PR.AA-03': 4, 'PR.AA-05': 2, 'PR.DS-02': 2, 'PR.IR-03': 2}
- ### D-03.3 · CRA · subso SO-D-03.3.CRA: {'PR.AA-05': 4, 'PR.AA-06': 4, 'DE.CM-09': 2}
- ### D-03.3 · DORA · subso SO-D-03.3.DORA: {'PR.AA-05': 3, 'PR.AA-06': 3}
- ### D-03.3 · GDPR · subso SO-D-03.3.GDPR: {'PR.AA-05': 6, 'PR.AA-06': 4, 'PR.AT-02': 2}
- ### D-03.3 · NIS2 · subso SO-D-03.3.NIS2: {'PR.AA-01': 2, 'PR.AA-05': 4, 'ID.AM-01': 4, 'ID.AM-02': 2}
- ### D-03.4 · CRA · subso SO-D-03.4.CRA: {'PR.PS-01': 3, 'ID.AM-08': 2, 'GV.SC-03': 2}
- ### D-03.4 · GDPR · subso SO-D-03.4.GDPR: {'PR.PS-01': 3, 'ID.AM-08': 3}
- ### D-04.1 · CRA · subso SO-D-04.1.CRA: {'PR.PS-04': 2, 'DE.CM-09': 2}
- ### D-04.1 · DORA · subso SO-D-04.1.DORA: {'DE.CM-01': 2, 'DE.CM-09': 2, 'DE.AE-02': 4, 'RS.MA-01': 2}
- ### D-04.1 · GDPR · subso SO-D-04.1.GDPR: {'DE.CM-01': 2}
- ### D-04.1 · NIS2 · subso SO-D-04.1.NIS2: {'DE.CM-01': 2}
- ### D-04.2 · CRA · subso SO-D-04.2.CRA: {'PR.IR-03': 2, 'PR.IR-04': 2}
- ### D-04.2 · DORA · subso SO-D-04.2.DORA: {'RC.RP-01': 2, 'PR.IR-03': 2, 'RC.RP-04': 2, 'PR.IR-04': 4}
- ### D-04.4 · CRA · subso SO-D-04.4.CRA: {'PR.IR-03': 2, 'ID.AM-08': 2}
- ### D-04.4 · GDPR · subso SO-D-04.4.GDPR: {'PR.IR-04': 4, 'PR.DS-11': 2, 'RC.RP-04': 2}
- ### D-04.4 · NIS2 · subso SO-D-04.4.NIS2: {'RC.RP-04': 2, 'PR.DS-11': 2}
- ### D-05.1 · CRA · subso SO-D-05.1.CRA: {'ID.AM-08': 2, 'ID.AM-03': 2}
- ### D-05.2 · GDPR · subso SO-D-05.2.GDPR: {'ID.AM-08': 2, 'ID.AM-03': 2}
- ### D-05.3 · CRA · subso SO-D-05.3.CRA: {'PR.DS-10': 3, 'ID.AM-08': 4, 'PR.DS-02': 3}
- ### D-06.1 · CRA · subso SO-D-06.1.CRA: {'GV.SC-01': 6, 'GV.SC-02': 2, 'ID.RA-02': 3}
- ### D-06.1 · DORA · subso SO-D-06.1.DORA: {'GV.SC-02': 4, 'ID.AM-04': 3}
- ### D-06.1 · GDPR · subso SO-D-06.1.GDPR: {'GV.SC-02': 3, 'GV.SC-04': 2}
- ### D-06.1 · NIS2 · subso SO-D-06.1.NIS2: {'GV.SC-02': 2}
- ### D-07.1 · AI_Act · subso SO-D-07.1.AIACT: {'PR.PS-06': 3, 'ID.RA-04': 2, 'ID.RA-01': 2}
- ### D-07.1 · CRA · subso SO-D-07.1.CRA: {'PR.PS-06': 3}
- ### D-07.1 · GDPR · subso SO-D-07.1.GDPR: {'PR.PS-06': 2, 'ID.AM-08': 3}
- ### D-07.1 · NIS2 · subso SO-D-07.1.NIS2: {'PR.PS-06': 3, 'PR.PS-02': 2}
- ### D-07.2 · AI_Act · subso SO-D-07.2.AIACT: {'ID.RA-04': 2, 'PR.PS-06': 2, 'ID.RA-01': 2}
- ### D-07.2 · CRA · subso SO-D-07.2.CRA: {'PR.PS-02': 2}
- ### D-07.2 · DORA · subso SO-D-07.2.DORA: {'PR.PS-06': 5}
- ### D-07.3 · NIS2 · subso SO-D-07.3.NIS2: {'PR.PS-02': 3, 'ID.RA-01': 6}
- ### D-07.4 · DORA · subso SO-D-07.4.DORA: {'PR.PS-01': 4, 'PR.PS-02': 5, 'PR.PS-06': 4}
- ### D-08.1 · CRA · subso SO-D-08.1.CRA: {'PR.AT-01': 4}
- ### D-08.1 · DORA · subso SO-D-08.1.DORA: {'PR.AT-01': 3, 'PR.AT-02': 3}
- ### D-08.1 · GDPR · subso SO-D-08.1.GDPR: {'PR.AT-01': 3, 'PR.AT-02': 2}
- ### D-08.1 · NIS2 · subso SO-D-08.1.NIS2: {'PR.AT-01': 3, 'PR.PS-01': 3}
- ### D-08.2 · AI_Act · subso SO-D-08.2.AIACT: {'PR.AT-02': 4, 'PR.AT-01': 3, 'GV.RR-02': 4, 'GV.RR-04': 2}
- ### D-08.2 · CRA · subso SO-D-08.2.CRA: {'PR.AT-02': 3, 'GV.SC-03': 3}
- ### D-08.2 · DORA · subso SO-D-08.2.DORA: {'PR.AT-01': 3, 'PR.AT-02': 3}
- ### D-08.2 · GDPR · subso SO-D-08.2.GDPR: {'PR.AT-01': 3, 'PR.AT-02': 2}
- ### D-08.2 · NIS2 · subso SO-D-08.2.NIS2: {'PR.AT-01': 3, 'PR.AT-02': 3}
- ### D-08.3 · DORA · subso SO-D-08.3.DORA: {'PR.AT-02': 3, 'GV.RR-01': 3}
- ### D-09.1 · GDPR · subso SO-D-09.1.GDPR: {'GV.PO-01': 6, 'GV.RM-04': 2}
- ### D-09.1 · NIS2 · subso SO-D-09.1.NIS2: {'GV.PO-01': 6}
- ### D-09.2 · NIS2 · subso SO-D-09.2.NIS2: {'ID.RA-05': 3, 'GV.PO-01': 2}
- ### D-09.3 · NIS2 · subso SO-D-09.3.NIS2: {'ID.AM-01': 4, 'ID.AM-02': 2, 'PR.PS-01': 2}
- ### D-10.1 · AI_Act · subso SO-D-10.1.AI_Act: {'DE.CM-09': 3, 'ID.IM-04': 2, 'GV.OV-03': 2}
- ### D-10.1 · GDPR · subso SO-D-10.1.GDPR: {'DE.CM-01': 2}
- ### D-10.2 · CRA · subso SO-D-10.2.CRA: {'ID.RA-04': 4, 'GV.PO-02': 2, 'PR.PS-02': 2, 'PR.DS-11': 2}
- ### D-10.2 · DORA · subso SO-D-10.2.DORA: {'GV.PO-01': 3, 'ID.AM-08': 2, 'GV.OC-03': 2}
- ### D-10.2 · GDPR · subso SO-D-10.2.GDPR: {'GV.PO-02': 2, 'PR.PS-04': 2, 'PR.DS-11': 2}
- ### D-10.3 · AI_Act · subso SO-D-10.3.AI_Act: {'ID.RA-04': 2, 'ID.IM-03': 2}
- ### D-10.3 · CRA · subso SO-D-10.3.CRA: {'ID.RA-04': 2, 'ID.RA-01': 2, 'ID.IM-03': 2}
- ### D-10.3 · DORA · subso SO-D-10.3.DORA: {'ID.RA-04': 2, 'ID.IM-03': 2, 'DE.AE-02': 2}
- ### D-10.3 · GDPR · subso SO-D-10.3.GDPR: {'ID.IM-03': 2}
- ### D-10.3 · NIS2 · subso SO-D-10.3.NIS2: {'GV.PO-01': 2, 'GV.OV-03': 2, 'ID.IM-03': 2}

## Cross-block overlaps (representative sample, 10 of 0)



---

<!-- executive-summary-v1 -->

# Executive summary — objective-anchor audit

- Total objectives audited: **268**
- Sub-domains covered: **38**
- Verdicts: sufficient=187, partial=3, excessive=78
- Confidence: high=163, medium=0, low=105

## Partial-coverage findings (requires review)

| Sub-domain | Entry |
|---|---|
| D-04.2 | D-04.2 · DORA · req 4.2.4 |
| D-04.2 | D-04.2 · NIS2 · req 4.2.2 |
| D-07.1 | D-07.1 · DORA · req 7.1.4 |

These objectives have a missing CSF 2.0 anchor relative to the regulatory obligation in their article basis. The agent judges them as worth human review.

## Sub-domains containing partial-coverage entries

D-04.2, D-07.1

## How to read this report

- Each `### D-XX.Y · REG · subso SO-...` and `### D-XX.Y · REG · req N.N.N` entry follows the 7-field template.
- Anchors classified CORE / UTILITY / NOISE based on objective + fit_criterion keywords vs. CSF 2.0 official title.
- `excessive` verdicts flag literal duplicate IDs in the same objective's `anchors_listed` (mechanical duplication, safe to deduplicate).
- `partial` verdicts flag an objective whose regulatory article cites a CSF control not in the listed anchors.
- `low` confidence: the article block for the source_SR does not list a per-SR nist_csf_mapping; CORE/UTILITY judgments use only the official CSF title and the objective prose. Verify by opening the article.


---

# AEGIS Modular Corpus — Objective NIST CSF 2.0 Anchor Audit

Single-pass audit of all 268 objective records (Sub-SO cards and Volere requirement cards) in `baseline/domains/_audit_input.jsonl`. Each anchor in `anchors_listed` is judged **CORE** (literal action match), **UTILITY** (reinforces but is not the direct action), or **NOISE** (tangential / subsumed). Missing anchors are detected by cross-checking the article's per-`sr_id` `nist_csf_mapping` against `anchors_listed` (article-mapped controls that map to the action keyword but are absent from the listed anchors are flagged). Excessive anchors are flagged when the same anchor id appears more than once in `anchors_listed` (literal duplicate).

## D-01.1 Data at Rest Encryption

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Where a product with digital elements stores data — personal or other — the confidentia... | CRA | sufficient | - | high |

### D-01.1 · CRA · subso SO-D-01.1.CRA
- **Objective**: Where a product with digital elements stores data — personal or other — the confidentiality of that data is protected by encrypting relevant data at rest using state-of-the-art mechanisms (Annex I Part I (2)(e)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product-stored data is encrypted using state-of-the-art mechanisms" The product shall ... | CRA | sufficient | - | high |

### D-01.1 · CRA · req 1.1.3
- **Title**: "Product-stored data is encrypted using state-of-the-art mechanisms"
- **Description**: The product shall protect the confidentiality of stored data — personal or other — by encrypting relevant data at rest using state-of-the-art mechanisms, in a manner that renders the data unintelligible to any person who is not authorised to access it (CRA Annex I Part I (2)(e), read with Annex II `personal data` Art. 3(47) cross-reference to GDPR Art. 4(1)).
- **Fit criterion (prose)**: State-of-the-art symmetric encryption (AES-256 minimum, or harmonised-standards-conformant equivalent under CRA Art. 27) is applied to all data at rest of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met for the relevant data; key custody is functionally separated by role-based access control (key-material custodian vs operational-environment custodian are distinct roles with distinct credentials); verified by Annex I conformity-assessment evidence + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Data confidentiality, integrity, authenticity and availability are maintained at high s... | DORA | excessive | - | high |

### D-01.1 · DORA · subso SO-D-01.1.DORA
- **Objective**: Data confidentiality, integrity, authenticity and availability are maintained at high standards across all data states, including at rest, through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability (Art. 9(2)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.DS-02, PR.DS-10 — literal duplicate(s) of PR.DS-01, PR.DS-02, PR.DS-10
- **Confidence**: high (article mapping and CSF title both consulted)

| "ICT-supported data of financial entity maintained at high standards of CIA at rest" Th... | DORA | sufficient | - | high |

### D-01.1 · DORA · req 1.1.4
- **Title**: "ICT-supported data of financial entity maintained at high standards of CIA at rest"
- **Description**: The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across data states including at rest, through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability (DORA Art. 9(2)).
- **Fit criterion (prose)**: High-standards symmetric encryption (AES-256 or stronger, EBA/ESMA/EIOPA RTS-conformant under DORA Art. 15 where applicable) is applied to financial-entity ICT-supported data at rest; the DORA Art. 9(4)(d) classification-driven cipher-strength overlay (per SR-DORA-003 / GV.RM-04) is documented for ICT risk-classification mapping; key-custody architecture is documented; verified by configuration audit + classification-driven cipher-strength overlay review + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal data at rest is processed in a manner that ensures appropriate security — incl... | GDPR | sufficient | - | high |

### D-01.1 · GDPR · subso SO-D-01.1.GDPR
- **Objective**: Personal data at rest is processed in a manner that ensures appropriate security — including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage — using appropriate technical or organisational measures, with the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (Art. 5(1)(f) + Art. 32(1)(b); the `appropriate` threshold is anchored by the five Art. 32(1) preamble factors — state of the art, costs of implementation, nature, scope, context, purposes, risks).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('data at rest') in objective maps to PR.DS-01
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal data at rest is protected by appropriate technical measures" The product shal... | GDPR | sufficient | - | high |

### D-01.1 · GDPR · req 1.1.1
- **Title**: "Personal data at rest is protected by appropriate technical measures"
- **Description**: The product shall protect personal data held at rest in storage against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical measures — primarily encryption with appropriate key custody — anchored to the five Art. 32(1) preamble factors (state of the art, costs of implementation, nature, scope, context, purposes, risks) (GDPR Art. 5(1)(f) + Art. 32(1)(a)/(b)).
- **Fit criterion (prose)**: AES-256 (or stronger) symmetric encryption is applied to all personal-data storage volumes; key custody is logically or physically separated from data access; the controller/processor risk-assessment artefact cites the five Art. 32(1) preamble factors and selects cipher strength accordingly; verified by automated configuration audit + manual key-custody review + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Essential and important entities establish policies and procedures regarding the use of... | NIS2 | sufficient | - | high |

### D-01.1 · NIS2 · subso SO-D-01.1.NIS2
- **Objective**: Essential and important entities establish policies and procedures regarding the use of cryptography and, where appropriate, encryption, covering the confidentiality, integrity, and authenticity of data stored, transmitted, and processed by network and information systems (Art. 21(2)(h)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/NIS2_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Cryptography policies cover CIA of stored NIS data" The product shall establish polici... | NIS2 | sufficient | - | high |

### D-01.1 · NIS2 · req 1.1.2
- **Title**: "Cryptography policies cover CIA of stored NIS data"
- **Description**: The product shall establish policies and procedures regarding the use of cryptography and, where appropriate, encryption, covering the confidentiality, integrity and authenticity of data stored by network and information systems of essential and important entities (NIS 2 Art. 21(2)(h)).
- **Fit criterion (prose)**: A documented cryptography policy exists and is maintained per Art. 21(2)(h); where the entity's risk assessment determines encryption is appropriate, AES-256 (or stronger) symmetric encryption is applied to NIS-scope data at rest; key custody is separated from data access; policy review cadence is documented; verified by policy inspection + automated configuration audit + CSIRT/CA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.1/articles/NIS2_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-01.2 Data in Transit Encryption

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Where data is transmitted by a product with digital elements — personal or other — the ... | CRA | sufficient | - | high |

### D-01.2 · CRA · subso SO-D-01.2.CRA
- **Objective**: Where data is transmitted by a product with digital elements — personal or other — the confidentiality of the data in transit is protected by encrypting relevant data using state-of-the-art mechanisms, with the Annex I (2)(j) attack-surface-limitation leg constraining the exposed interfaces through which the data could otherwise leak (Annex I Part I (2)(e) + (2)(j)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — Action keyword ('data in transit') in objective maps to PR.DS-02
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **UTILITY** — CSF title shares 1 token ('protected') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product-transmitted data is encrypted with state-of-the-art mechanisms and exposed int... | CRA | sufficient | - | high |

### D-01.2 · CRA · req 1.2.2
- **Title**: "Product-transmitted data is encrypted with state-of-the-art mechanisms and exposed interfaces are minimised"
- **Description**: The product shall protect the confidentiality of data in transit by encrypting the relevant data using state-of-the-art mechanisms, in a manner that renders the data unintelligible to any person not authorised to access it, and shall limit the attack surface of the product with digital elements by constraining the exposed interfaces through which the data could otherwise leak (CRA Annex I Part I (2)(e) + (2)(j)).
- **Fit criterion (prose)**: State-of-the-art symmetric encryption (e.g. TLS 1.3 with AES-256-GCM or equivalent, harmonised-standards-conformant under CRA Art. 27) is applied to data in transit of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met; the Annex I (2)(j) attack-surface-limitation leg is documented (exposed interfaces enumerated, default ports minimised, unused services disabled); both internal east-west traffic and externally-exposed transport edges are covered per the R3 reading; verified by Annex I conformity-assessment evidence + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — Action keyword ('data in transit') in objective maps to PR.DS-02
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Data confidentiality, integrity, authenticity and availability are maintained at high s... | DORA | excessive | - | high |

### D-01.2 · DORA · subso SO-D-01.2.DORA
- **Objective**: Data confidentiality, integrity, authenticity and availability are maintained at high standards across all data states, including in transit, through ICT security policies, procedures, protocols and tools (Art. 9(2)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.DS-02, PR.DS-10 — literal duplicate(s) of PR.DS-01, PR.DS-02, PR.DS-10
- **Confidence**: high (article mapping and CSF title both consulted)

| "ICT-supported data of financial entity maintained at high standards of CIA in transit"... | DORA | sufficient | - | high |

### D-01.2 · DORA · req 1.2.3
- **Title**: "ICT-supported data of financial entity maintained at high standards of CIA in transit"
- **Description**: The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across all data states, including in transit, through ICT security policies, procedures, protocols and tools (DORA Art. 9(2)).
- **Fit criterion (prose)**: High-standards in-transit cryptography (TLS 1.3 or stronger, with cipher suites conforming to EBA/ESMA/EIOPA RTS under DORA Art. 15 where applicable) is applied across all in-transit channels of the financial entity's ICT landscape; mutual-authentication (mTLS) architecture + zone-trust + peer-peer authentication between internal services is documented; network-segmentation policy is documented; verified by configuration audit + zone-trust architecture review + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal data transmitted across networks, inter-service channels, and third-party infr... | GDPR | sufficient | - | high |

### D-01.2 · GDPR · subso SO-D-01.2.GDPR
- **Objective**: Personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted) (Art. 32(1)(b) + Art. 32(2)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **CORE** — CSF title literally matches action keyword ('network')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal data in transit remains confidential and unaltered" The product shall ensure ... | GDPR | sufficient | - | high |

### D-01.2 · GDPR · req 1.2.1
- **Title**: "Personal data in transit remains confidential and unaltered"
- **Description**: The product shall ensure that personal data transmitted across networks, inter-service channels, and third-party infrastructure remains confidential and unaltered in transit, with the in-transit protection anchored to the five-event Art. 32(2) risk enumeration (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted) (GDPR Art. 32(1)(b) + Art. 32(2)).
- **Fit criterion (prose)**: TLS 1.3 (or stronger) is applied to all in-transit channels carrying personal data; the five-event Art. 32(2) risk enumeration is addressed by technical measures on each event class (encryption for confidentiality, integrity verification for alteration, network segmentation for destruction/loss/access); cipher-suite selection is documented; verified by automated network scan + configuration audit + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.2/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — Action keyword ('data in transit') in objective maps to PR.DS-02
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **CORE** — CSF title literally matches action keyword ('network')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-01.3 Cryptographic Key Management

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Cryptographic keys and related authentication material used to protect the confidential... | CRA | excessive | - | high |

### D-01.3 · CRA · subso SO-D-01.3.CRA
- **Objective**: Cryptographic keys and related authentication material used to protect the confidentiality and integrity of stored, transmitted or otherwise processed data by a product with digital elements — personal or other — are managed with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it (Annex I Part I (2)(d) access-control + (2)(e) "other technical means" reading per `SR-CRA-004` ambiguity_notes; the Annex I text does not mention key management explicitly — the synthesis catalogue `99_CRA_Synthesis.md` §4 flags this as a T2-vs-text gap — so the key-separation reading rests on the combination of Annex I (2)(d) access-control duty with the Annex I (2)(e) "other technical means" residual).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/CRA_Art_6.md` (Art. 6) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 5 action tokens with objective
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 5 action tokens with objective
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.AA-05, GV.OV-01 — literal duplicate(s) of PR.DS-01, PR.AA-05, GV.OV-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Cryptographic keys of product with digital elements separated from operational environ... | CRA | sufficient | - | high |

### D-01.3 · CRA · req 1.3.2
- **Title**: "Cryptographic keys of product with digital elements separated from operational environment"
- **Description**: The product shall manage cryptographic keys and related authentication material used to protect the confidentiality and integrity of stored, transmitted or otherwise processed data with separation of roles such that possession of the key material is not bundled with possession of the operational environment that uses it (CRA Annex I Part I (2)(d) access-control + (2)(e) `other technical means` reading; T2-vs-text gap per `99_CRA_Synthesis.md` §4 — Annex I text does not mention key management explicitly, so the key-separation reading rests on the combination of (2)(d) access-control with the (2)(e) `other technical means` residual).
- **Fit criterion (prose)**: The product with digital elements implements functional RBAC separation such that the key-material custodian and the operational-environment custodian are distinct roles with distinct credentials under least-privilege entitlements; the Annex I (2)(e) `render unintelligible` test is met by separation of role credentials (not by physical separation alone); the state-of-the-art baseline governs primitive choice (CRA Art. 27 harmonised-standards-conformant equivalent acceptable); verified by Annex I conformity-assessment evidence + technical documentation inspection (Annex VII) + MSA/ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/CRA_Art_6.md` (Art. 6) — paraphrased action
- **Anchors listed**:
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('least-privilege') in objective maps to PR.AA-05
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Strong authentication mechanisms, cryptographic-key protection measures, and data encry... | DORA | excessive | - | high |

### D-01.3 · DORA · subso SO-D-01.3.DORA
- **Objective**: Strong authentication mechanisms, cryptographic-key protection measures, and data encryption are implemented through coordinated policies and protocols, with the cryptographic-key protection leg tied to approved data classification and ICT risk assessment processes (Art. 9(4)(d) 3-control AND of strong authentication + key protection + encryption).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-03, PR.AA-04, PR.DS-01, GV.RM-04 — literal duplicate(s) of PR.AA-03, PR.AA-04, PR.DS-01, GV.RM-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial-entity cryptographic keys protected with classification-driven cipher streng... | DORA | sufficient | - | high |

### D-01.3 · DORA · req 1.3.3
- **Title**: "Financial-entity cryptographic keys protected with classification-driven cipher strength and depth"
- **Description**: The product shall implement strong authentication mechanisms, cryptographic-key protection measures, and data encryption as a coordinated 3-control AND tied to approved data classification and ICT risk assessment processes (DORA Art. 9(4)(d)), with the key-protection leg operationalised through HSM-anchored custodianship, split-knowledge ceremonies, classification-driven rotation cadence scaled to data criticality, and quorum-based recovery procedures (DORA Art. 9(2) + Art. 9(4)(d) + EBA Guidelines on ICT and security risk management §149).
- **Fit criterion (prose)**: Cryptographic keys protecting financial-entity ICT-supported data are stored in FIPS 140-3 / Common Criteria EAL4+ certified HSMs (or RTS-conformant equivalent under DORA Art. 15 where applicable); split-knowledge ceremonies with quorum-based recovery are documented and tested (per EBA Guidelines §149 depth guidance); rotation cadence is classified-tiered (high-criticality data: ≤12 months; medium-criticality: ≤24 months; low-criticality: ≤36 months — scaled per EBA Guidelines §149 criticality matrix); the `approved data classification` qualifier is met (data-classification processes approved by management body per Art. 5(2); ICT risk assessment satisfies Art. 6 chapeau); verified by HSM-configuration audit + rotation-cadence review + classification-driven cipher-strength overlay + national-CA + ESAs inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/CRA_Art_6.md` (Art. 6) — paraphrased action
- **Anchors listed**:
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 4 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Where pseudonymisation or encryption is applied to personal data, the additional inform... | GDPR | excessive | - | high |

### D-01.3 · GDPR · subso SO-D-01.3.GDPR
- **Objective**: Where pseudonymisation or encryption is applied to personal data, the additional information required to re-identify the data subject (the cryptographic key, the mapping table, or the tokenisation seed) is kept separately and is subject to appropriate technical and organisational measures that prevent attribution (Art. 4(5) de-attribution test + Art. 34(3)(a) unintelligibility carve-out + Art. 32(1)(a) pseudonymisation/ encryption anchor).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.IR-03 — literal duplicate(s) of PR.DS-01, PR.IR-03
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data key material kept separately to prevent re-attribution (de-attribution t... | GDPR | sufficient | - | high |

### D-01.3 · GDPR · req 1.3.1
- **Title**: "Personal-data key material kept separately to prevent re-attribution (de-attribution test)"
- **Description**: The product shall keep the additional information required to re-identify personal data (the cryptographic key, mapping table, or tokenisation seed) separately from the personal data and subject to appropriate technical and organisational measures that prevent attribution, so that unintelligibility is preserved on the day of a breach (GDPR Art. 4(5) de-attribution test + Art. 32(1)(a) pseudonymisation/encryption anchor + Art. 34(3)(a) unintelligibility carve-out).
- **Fit criterion (prose)**: The cryptographic key, mapping table, or tokenisation seed protecting personal data is stored physically or logically separated from the personal data it protects; separation is governed by RBAC-distinct roles with distinct credentials under documented control (key-material custodian role ≠ data-platform operator role); the operational condition `those measures were applied to the personal data affected by the personal data breach` (Art. 34(3)(a) carve-out) is verifiable — the controller demonstrates that the unintelligibility measures covered the affected dataset, not merely that they were deployed somewhere in the system; verified by automated configuration audit of key-storage location + manual separation-of-roles review + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.3/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — Action keyword ('encrypt') in objective maps to PR.DS-01
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-01.4 Data Integrity Mechanisms

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are as resilient as possible regarding errors, faults, or inconsis... | AI_Act | excessive | - | high |

### D-01.4 · AI_Act · subso SO-D-01.4.AI_Act
- **Objective**: High-risk AI systems are as resilient as possible regarding errors, faults, or inconsistencies that may occur within the system or the environment (Art. 15(3)); the robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.IR-03, PR.IR-04, PR.DS-11 — literal duplicate(s) of PR.IR-03, PR.IR-04, PR.DS-11
- **Confidence**: high (article mapping and CSF title both consulted)

| "High-risk AI system resilient to errors, faults, or inconsistencies via technical redu... | AI_Act | sufficient | - | high |

### D-01.4 · AI_Act · req 1.4.4
- **Title**: "High-risk AI system resilient to errors, faults, or inconsistencies via technical redundancy"
- **Description**: The product shall ensure high-risk AI systems are as resilient as possible regarding errors, faults, or inconsistencies that may occur within the system or the environment, with robustness achieved through technical redundancy solutions which may include backup or fail-safe plans (AI Act Art. 15(3)); the resilience target is read as R3 state-of-the-art per `SR-AIACT-015` ambiguity_notes and is proportionate to the intended purpose per Recital 66.
- **Fit criterion (prose)**: The high-risk AI system implements resilience mechanisms for errors, faults, and inconsistencies that occur within the system or its environment (PR.IR-03 — failover, redundant inference paths, graceful degradation); capacity is sized for the resilience target, not just steady-state workload (PR.IR-04); where the OJ-permitted `backup` means is selected, backups are created, protected, maintained, and tested (PR.DS-11); where the `fail-safe plan` means is selected, the fail-safe behaviour is documented and tested; the resilience target is proportionate to the intended purpose per Recital 66; verified by resilience-mechanism audit (failover test, redundant-inference-path exercise) + backup-testing evidence + fail-safe plan documentation + conformity-assessment body + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 7 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The integrity of stored, transmitted, or otherwise processed data — personal or other —... | CRA | excessive | - | high |

### D-01.4 · CRA · subso SO-D-01.4.CRA
- **Objective**: The integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, is protected against any manipulation or modification not authorised by the user (Annex I Part I (2)(f) — the universal-quantifier `any` makes the integrity protection unconditional); corruption is reported to the user / administering party (Annex I Part I (2)(f) `report on corruptions` + (2)(l) logging + monitoring).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 4 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 4 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.DS-10, PR.PS-04 — literal duplicate(s) of PR.DS-01, PR.DS-10, PR.PS-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Integrity of stored/transmitted/processed data + commands + programs + configuration p... | CRA | sufficient | - | high |

### D-01.4 · CRA · req 1.4.2
- **Title**: "Integrity of stored/transmitted/processed data + commands + programs + configuration protected against unauthorised manipulation"
- **Description**: The product shall protect the integrity of stored, transmitted, or otherwise processed data — personal or other — as well as the integrity of commands, programs, and configuration, against any manipulation or modification not authorised by the user, and shall report corruption to the user / administering party (CRA Annex I Part I (2)(f) universal-quantifier `any` makes the integrity protection unconditional + (2)(l) logging + monitoring + corruption reporting).
- **Fit criterion (prose)**: All stored, transmitted, or processed data — together with commands, programs, and configuration — are protected by cryptographic hashes / MACs / signed firmware (PR.DS-01 + PR.DS-10) such that any unauthorised manipulation invalidates the integrity check on the next read; corruption events are surfaced as log records suitable for continuous monitoring (PR.PS-04) and reported to the user / administering party; verified by Annex I (2)(f) conformity-assessment evidence + Annex I (2)(l) corruption-report verification + technical documentation inspection + MSA/ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Data confidentiality, integrity, authenticity and availability are maintained at high s... | DORA | excessive | - | high |

### D-01.4 · DORA · subso SO-D-01.4.DORA
- **Objective**: Data confidentiality, integrity, authenticity and availability are maintained at high standards across all data states — at rest, in use, or in transit — through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability (Art. 9(2)).
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05 — literal duplicate(s) of PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05
- **Confidence**: high (article mapping and CSF title both consulted)

| "ICT-system data integrity maintained at high standards across all data states" The pro... | DORA | sufficient | - | high |

### D-01.4 · DORA · req 1.4.3
- **Title**: "ICT-system data integrity maintained at high standards across all data states"
- **Description**: The product shall maintain data confidentiality, integrity, authenticity and availability at high standards across all data states — at rest, in use, or in transit — through ICT security policies, procedures, protocols and tools designed to ensure ICT-system resilience, continuity and availability, with the integrity cell of the 4×3 CIA+A × data-states matrix as the binding property on the DORA side (DORA Art. 9(2)).
- **Fit criterion (prose)**: ICT-system-level integrity controls cover at-rest integrity (PR.DS-01 — cryptographic hashes / MACs on stored data), in-transit integrity (PR.DS-02 — signed-protocol integrity on data in motion), in-use integrity (PR.DS-10 — runtime integrity controls such as signed firmware, control-flow integrity, tamper-detection instrumentation), and risk-strategy-managed data integrity (ID.AM-05 — data managed consistent with risk strategy per DORA Art. 6 chapeau); the integrity cell of the DORA Art. 9(2) 4×3 matrix is documented and discharged; verified by configuration audit of all four integrity anchors + classification-driven cipher-strength overlay (per DORA Art. 9(4)(d) + SR-DORA-003 GV.RM-04) + national-CA + ESAs inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal data are accurate and, where necessary, kept up to date; every reasonable step... | GDPR | excessive | - | low |

### D-01.4 · GDPR · subso SO-D-01.4.GDPR
- **Objective**: Personal data are accurate and, where necessary, kept up to date; every reasonable step is taken to ensure that personal data that are inaccurate are erased or rectified without delay (Art. 5(1)(d) accuracy principle), with the integrity property anchored to two further legs — storage integrity (Art. 5(1)(f)) and the Art. 16 rectification cascade with Art. 19 recipient-cascade duty.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/AI_Act_Art_72.md` (Art. 72) — paraphrased action
- **Anchors listed**:
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-01, ID.AM-08, PR.DS-10 — literal duplicate(s) of PR.DS-01, ID.AM-08, PR.DS-10
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Personal data accurate, up to date, and protected against unauthorised modification" T... | GDPR | sufficient | - | low |

### D-01.4 · GDPR · req 1.4.1
- **Title**: "Personal data accurate, up to date, and protected against unauthorised modification"
- **Description**: The product shall ensure personal data are accurate and, where necessary, kept up to date; every reasonable step shall be taken to ensure that inaccurate personal data are erased or rectified without delay, with the storage-integrity property anchored separately and the Art. 16 rectification cascade with Art. 19 recipient-cascade duty preserved (GDPR Art. 5(1)(d) accuracy + Art. 5(1)(f) integrity + Art. 16 + Art. 19 cascade).
- **Fit criterion (prose)**: Personal-data storage uses integrity-checked storage with cryptographic hashes / MACs that detect tampering on reads (PR.DS-01); data-quality monitoring is in place with documented periodic-refresh cadence governing accuracy review (ID.AM-08); the Art. 16 rectification workflow is documented with recipient register and propagation procedure to each recipient to whom the personal data have been disclosed (ID.AM-08 + Art. 19 cascade); verified by automated integrity-check audit (hash/MAC validation) + manual rectification-cascade review + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-01_Data-Protection/D-01.4/articles/AI_Act_Art_72.md` (Art. 72) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 5 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-02.1 Vulnerability Identification

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| A risk-management system is established, implemented, documented, and maintained for hi... | AI_Act | sufficient | - | high |

### D-02.1 · AI_Act · subso SO-D-02.1.AI_Act
- **Objective**: A risk-management system is established, implemented, documented, and maintained for high-risk AI systems throughout their lifecycle, comprising a continuous iterative process of (a) identification and analysis of known and reasonably foreseeable risks, (b) estimation and evaluation of risks emerging from use under conditions of reasonably foreseeable misuse, (c) evaluation of other risks arising from analysis of post-market monitoring data, and (d) adoption of appropriate and targeted risk-management measures (Art. 9(2)); the high-risk AI system is designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and is resilient against errors, faults, or inconsistencies that may occur within the system or the environment, with appropriate technical and organisational measures to prevent, detect, respond to, resolve, and control for attacks trying to manipulate the training data set (data poisoning), pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks, or model flaws (Art. 15(1)/(4)–(5)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Continuous iterative AI risk-identification (Art. 9(2) 4-step cycle) + AI-specific att... | AI_Act | sufficient | - | high |

### D-02.1 · AI_Act · req 2.1.5
- **Title**: "Continuous iterative AI risk-identification (Art. 9(2) 4-step cycle) + AI-specific attack-taxonomy register (Art. 15(4)–(5))"
- **Description**: The product shall establish, implement, document and maintain a risk-management system for high-risk AI systems throughout their lifecycle, comprising a continuous iterative process of (a) identification and analysis of known and reasonably foreseeable risks, (b) estimation and evaluation of risks emerging from use under conditions of reasonably foreseeable misuse, (c) evaluation of other risks arising from analysis of post-market monitoring data, and (d) adoption of appropriate and targeted risk-management measures; and shall design and develop the high-risk AI system to achieve appropriate accuracy, robustness and cybersecurity with appropriate technical and organisational measures to prevent, detect, respond to, resolve, and control for AI-specific attacks (data poisoning, model poisoning, adversarial examples or model evasion, confidentiality attacks, model flaws) (AI Act Art. 9(1) + Art. 9(2)(a)–(d) + Art. 15(1) + Art. 15(4)–(5)).
- **Fit criterion (prose)**: A risk-management system document is established, implemented, documented, and maintained for each high-risk AI system across its lifecycle with stakeholder-agreed objectives (GV.RM-01) and a standardised risk-calculation method (GV.RM-06); the Art. 9(2) 4-step closed-list cycle operates continuously with ID.RA-03 threat identification + ID.RA-04 impact-and-likelihood scoring + ID.RA-06 response-tracking trails from identified risk to selected treatment; an AI-specific attack-taxonomy register covers the six Art. 15(4)–(5) categories (data poisoning, model poisoning, adversarial examples or model evasion, confidentiality attacks, model flaws) with PR.PS-06 secure-SDLC artefacts (threat models, code-review records, test reports) and prioritisation by impact and likelihood; verified by risk-management-system documentation audit + Art. 9(2) 4-step cycle evidence review + AI-specific attack-taxonomy register inspection + Art. 72 post-market monitoring feedback loop trace + conformity-assessment body + MSA + AI Office inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.RM-06 — A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated — **CORE** — CSF title shares 6 action tokens with objective
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - ID.RA-06 — Risk responses are chosen, prioritized, planned, tracked, and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MI-01 — Incidents are contained — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A product with digital elements is made available on the market without known exploitab... | CRA | excessive | - | high |

### D-02.1 · CRA · subso SO-D-02.1.CRA
- **Objective**: A product with digital elements is made available on the market without known exploitable vulnerabilities (Annex I Part I (2)(a)), and vulnerabilities contained in the product — including the components listed in an SBOM — are identified and documented on a continuing basis throughout the support period (Annex I Part II (1) + Art. 13(3) + Art. 13(7)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, ID.AM-02, PR.PS-02 — literal duplicate(s) of ID.RA-01, ID.AM-02, PR.PS-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product made available without known exploitable vulnerabilities; SBOM-backed identifi... | CRA | sufficient | - | high |

### D-02.1 · CRA · req 2.1.3
- **Title**: "Product made available without known exploitable vulnerabilities; SBOM-backed identification throughout support period"
- **Description**: The product shall be made available on the market without known exploitable vulnerabilities, and vulnerabilities contained in the product — including components listed in a software bill of materials — shall be identified and documented on a continuing basis throughout the support period, with the manufacturer exercising the Annex VII §3 due-diligence `constructive knowledge` baseline (inquiry-resistant: knowledge that a reasonably diligent risk-assessment process should have surfaced, not only CVE-published weaknesses) (CRA Annex I Part I (2)(a) + Annex I Part II (1) + Art. 13(3) + Art. 13(7) + Art. 13(8)).
- **Fit criterion (prose)**: The release-engineering pipeline closes out identified vulnerabilities before market placement under the R2 `constructive knowledge` baseline (vendor advisories + ISACs + CERT-EU alerts + peer-manufacturer channels joined by the manufacturer); a vulnerability register and a machine-readable SBOM covering at least the top-level dependencies are maintained across the support period; vulnerability records are queryable against newly-disclosed CVEs across historical releases; the technical documentation under Annex VII §2(b) + §3 + §6 + §8 retains the SBOM, risk-based justification, test reports and MSA-request response logs; verified by release-gate evidence + SBOM format-validity check + Annex VII conformity-dossier inspection + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT-s... | DORA | excessive | - | high |

### D-02.1 · DORA · subso SO-D-02.1.DORA
- **Objective**: Sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT-supported business functions, information assets, and ICT assets — are identified on a continuous basis, and the risk scenarios impacting the entity are reviewed on a regular basis, at least yearly (Art. 7(2) + Art. 8(2)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, ID.RA-03, GV.OV-02 — literal duplicate(s) of ID.RA-01, ID.RA-03, GV.OV-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Continuous ICT-risk identification + at-least-yearly scenario review (hard anchor)" Th... | DORA | sufficient | - | high |

### D-02.1 · DORA · req 2.1.4
- **Title**: "Continuous ICT-risk identification + at-least-yearly scenario review (hard anchor)"
- **Description**: The product shall, on a continuous basis, identify all sources of ICT risk — including cyber threats and ICT vulnerabilities relevant to ICT-supported business functions, information assets, and ICT assets — and the risk scenarios impacting the entity shall be reviewed on a regular basis, at least yearly, with the at-least-yearly floor binding even where the entity-internal regular-basis cadence is set tighter (DORA Art. 7(2) + Art. 8(2)).
- **Fit criterion (prose)**: A continuous ICT-risk-identification programme operates with documented cadence (vulnerability scanning, CVE-feed ingestion, authenticated vulnerability validation, threat-intelligence feeds weighted by the OJ `in particular the risk exposure to and from other financial entities` qualifier under Art. 7(2)); an annual risk-scenario register refresh executes by EBA Guidelines on ICT and security risk management §100 with management-body approval; inter-entity risk-exposure annotations (Art. 45 ESAs cooperation framework) are recorded; verified by ID.RA-01 vulnerability-register audit + ID.RA-03 threat-catalogue review + ID.RA-05 likelihood-by-impact matrix inspection + ID.IM-04 / GV.OV-02 strategic-review records + management-body approval evidence + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 5 action tokens with objective
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A controller or processor operates a process for regularly testing, assessing, and eval... | GDPR | excessive | - | high |

### D-02.1 · GDPR · subso SO-D-02.1.GDPR
- **Objective**: A controller or processor operates a process for regularly testing, assessing, and evaluating the effectiveness of the technical and organisational measures for ensuring the security of the processing (Art. 32(1)(d)); the data-protection impact assessment under Art. 35 is reviewed when there is a change of the risk represented by processing operations (Art. 35(11)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.IM-02 — Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.IM-02 — Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02 — literal duplicate(s) of ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Periodic testing of security measures + DPIA review on material change" The product sh... | GDPR | sufficient | - | low |

### D-02.1 · GDPR · req 2.1.1
- **Title**: "Periodic testing of security measures + DPIA review on material change"
- **Description**: The product shall operate a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing, and the data-protection impact assessment under Art. 35 shall be reviewed at least when there is a change of the risk represented by processing operations, with cadence and depth anchored to the five Art. 32(1) preamble factors (state of the art, costs of implementation, nature, scope, context, purposes, risks) (GDPR Art. 32(1)(d) + Art. 35(11)).
- **Fit criterion (prose)**: A periodic testing programme (vulnerability scans, control-effectiveness tests, penetration tests against critical systems) operates with documented cadence scaled to the five Art. 32(1) preamble factors; a DPIA register documents review on every material change (processing-purpose change under Art. 6(4), data-category change, data-subject-population change, technical-context change, regulatory-expectation change); the testing programme and DPIA register survive an Art. 5(2) accountability check; verified by testing-records audit + DPIA register inspection + change-trigger review log + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.IM-02 — Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Vulnerabilities in network and information systems are identified, handled, and disclos... | NIS2 | excessive | - | high |

### D-02.1 · NIS2 · subso SO-D-02.1.NIS2
- **Objective**: Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle (Art. 21(2)(e)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, GV.SC-04 — literal duplicate(s) of ID.RA-01, GV.SC-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Vulnerability handling and external disclosure integrated into system lifecycle" The p... | NIS2 | sufficient | - | high |

### D-02.1 · NIS2 · req 2.1.2
- **Title**: "Vulnerability handling and external disclosure integrated into system lifecycle"
- **Description**: The product shall identify, handle, and disclose vulnerabilities in network and information systems through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle, with the Art. 21(2)(e) appropriate-and-proportionate qualifier propagated from Art. 21(1) (NIS 2 Art. 21(2)(e)).
- **Fit criterion (prose)**: A documented CVD policy exists and is maintained under Art. 21(2)(e); vulnerability signals from internal scanning, vendor advisories, threat-intelligence feeds and coordinated-disclosure submissions are ingested, validated against the entity's asset population, and recorded with severity, scope and remediation status; supplier-vulnerability-assessment (Art. 21(3) sentence 1) and CSIRT-coordinated disclosure pathway are operational; verified by CVD policy inspection + intake-triage-remediation-verification records + CSIRT disclosure records (4.3 cross-ref) + national-CA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.1/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-02.2 Patch Management & Updates

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Vulnerabilities of a product with digital elements are addressed and remediated through... | CRA | sufficient | PR.PS-02 | high |

### D-02.2 · CRA · subso SO-D-02.2.CRA
- **Objective**: Vulnerabilities of a product with digital elements are addressed and remediated through security updates without delay, including — where technically feasible — through security updates provided separately from functionality updates (Annex I Part II (2) + Annex I Part I (2)(c)); security updates are disseminated without delay to users via mechanisms that ensure the secure distribution of updates, accompanied by advisory messages describing the action users can take (Annex I Part II (7) + (8)); vulnerabilities — including those of integrated components — are handled effectively and in accordance with the Annex I Part II vulnerability-handling requirements throughout the support period determined by the manufacturer (minimum 5 years, or the expected use time if shorter — Art. 13(8)); each security update made available during the support period remains available after it has been issued for at least 10 years or for the remainder of the support period, whichever is longer (Art. 13(9)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (1)**: PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — Article maps PR.PS-02 for action keyword 'update' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Vulnerabilities remediated without delay; separated secure update distribution; 5-year... | CRA | sufficient | - | high |

### D-02.2 · CRA · req 2.2.1
- **Title**: "Vulnerabilities remediated without delay; separated secure update distribution; 5-year support + 10-year availability tail"
- **Description**: The product shall address and remediate vulnerabilities — including those of integrated third-party components listed in the SBOM — without delay through security updates, provided — where technically feasible — separately from functionality updates, disseminated without delay to users via mechanisms that ensure the secure distribution of updates, free of charge (unless otherwise agreed for a tailor-made product), accompanied by advisory messages describing the action users can take, with automatic security updates installed within an appropriate timeframe as a default setting with a clear and easy-to-use opt-out mechanism and postponement option, handled effectively throughout the support period determined by the manufacturer (minimum 5 years, or the expected use time if shorter), and with each security update made available during the support period remaining available for at least 10 years or for the remainder of the support period, whichever is longer (CRA Annex I Part I (2)(c) + Annex I Part II (2) + (7) + (8) + Art. 13(6) + Art. 13(8) + Art. 13(9)).
- **Fit criterion (prose)**: Remediation action commences immediately on the R2 `constructive knowledge` awareness baseline (vendor advisories + ISACs + CERT-EU alerts + peer-manufacturer channels joined) with a documented timeline from awareness to user-dissemination; technical-feasibility carve-out for non-separation of security from functionality updates is recorded in the conformity dossier under Annex VII; security-update binaries are integrity-protected (signed artefacts, transport security, atomic apply/rollback) and disseminated via a separated secure channel; auto-update is the default setting with discoverable single-click opt-out and postponement, and Annex II §8(e) user-facing disclosure is present; support period is at least 5 years (or expected use time if shorter) and documented end-date is displayed; each issued security update remains downloadable for the maximum of 10 years or support-period remainder, whichever is longer; verified by remediation-timeline audit + technical-feasibility carve-out log + update-archive integrity check + auto-update default + opt-out discoverability test + support-period documentation + 10-year tail archive inspection + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-06 — Risk responses are chosen, prioritized, planned, tracked, and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('update') in objective maps to PR.PS-02
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A sound network and infrastructure management structure is established, using appropria... | DORA | sufficient | PR.PS-02 | high |

### D-02.2 · DORA · subso SO-D-02.2.DORA
- **Objective**: A sound network and infrastructure management structure is established, using appropriate techniques, methods and protocols — which may include automated mechanisms to isolate affected information assets in the event of cyber-attacks (Art. 9(4)(b)) — and appropriate and comprehensive documented policies for patches and updates are maintained (Art. 9(4)(f)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (1)**: PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — Article maps PR.PS-02 for action keyword 'patch' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Appropriate and comprehensive documented patch policy + automated blast-radius isolati... | DORA | sufficient | - | high |

### D-02.2 · DORA · req 2.2.2
- **Title**: "Appropriate and comprehensive documented patch policy + automated blast-radius isolation of affected information assets"
- **Description**: The product shall maintain a sound network and infrastructure management structure using appropriate techniques, methods and protocols that may include implementing automated mechanisms to isolate affected information assets in the event of cyber-attacks, and shall have appropriate and comprehensive documented policies for patches and updates covering the entity's full ICT asset estate with severity-classified deployment windows (DORA Art. 9(4)(b) + Art. 9(4)(f)).
- **Fit criterion (prose)**: A documented patch-and-update policy exists, is approved by management, and specifies scope (full asset estate), severity-classification taxonomy, SLA-bound deployment windows per severity tier, exception-handling procedures for compensating controls during deferred-patch windows, rollback runbooks for production-impacting patches, and approval authorities; PR.PS-01 configuration-management baseline (golden images, drift detection, configuration-as-code) is enforced; PR.PS-02 severity-classified patch discipline operates across the ICT asset estate with documented exception register; PR.IR-01 network-segmentation and PR.IR-03 automated blast-radius isolation mechanisms (segmentation, micro-segmentation around payment-processing and settlement-infrastructure zones, automated isolation on detected compromise) are tested; the ID.RA-01 entity-side vulnerability register feeds patch-priority ordering; verified by patch-policy document inspection + severity-tier SLA-window records + configuration-baseline audit + segmentation + isolation-test outcomes + exception-register review + management-body approval evidence + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **CORE** — CSF title literally matches action keyword ('network')
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('patch') in objective maps to PR.PS-02
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-02.3 Coordinated Vulnerability Disclosure

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The manufacturer puts in place, documents and enforces a policy on coordinated vulnerab... | CRA | sufficient | - | high |

### D-02.3 · CRA · subso SO-D-02.3.CRA
- **Objective**: The manufacturer puts in place, documents and enforces a policy on coordinated vulnerability disclosure for its products with digital elements (Annex I Part II (5) + Art. 13(8) sentence 6); once a security update has been made available, the manufacturer shares and publicly discloses information about the fixed vulnerabilities, including a description of the vulnerability, the affected products, the impacts, the severity, and the remediation guidance — subject to a duly justified delay exception where security risks of publication outweigh security benefits (Annex I Part II (4)); the manufacturer facilitates the sharing of information about potential vulnerabilities in its products and in third-party components contained therein, including by providing a publicly identifiable contact address for the reporting of vulnerabilities (Annex I Part II (6)); the manufacturer designates a single point of contact to enable users — including security researchers — to communicate directly and rapidly with the manufacturer (Art. 13(17) + Annex II §2).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Manufacturer puts in place, documents and enforces CVD policy for products with digita... | CRA | sufficient | - | high |

### D-02.3 · CRA · req 2.3.1
- **Title**: "Manufacturer puts in place, documents and enforces CVD policy for products with digital elements; publicly identifiable contact address; SPOC; public disclosure of fixed vulnerabilities with `duly justified` delay exception"
- **Description**: The product shall have a coordinated vulnerability disclosure (CVD) policy that is put in place, documented and enforced across the support period, with the manufacturer — once a security update has been made available — sharing and publicly disclosing information about the fixed vulnerabilities (description, affected products, impacts, severity, remediation guidance) subject to a `duly justified` delay exception where security risks of publication outweigh security benefits, and the manufacturer shall facilitate the sharing of information about potential vulnerabilities in its products and in third-party components contained therein by providing a publicly identifiable contact address for vulnerability reporting and designating a single point of contact (per CRA Annex I Part II (4) + (5) + (6) + Art. 13(8) sentence 6 + Art. 13(17) + Art. 14(1)–(4) + Art. 14(8) + Art. 14(9) + Art. 16(2) + Art. 17(5) + Annex II §2).
- **Fit criterion (prose)**: A documented CVD policy is published on the manufacturer's external-facing surface and enforced operationally (intake-channel evidence + triage-log records + post-disclosure verification artefacts under SR-CRA-019 R3 reading); a publicly identifiable contact address is machine-discoverable via security.txt or well-known URI (Annex I Part II (6) + Art. 13(17) + Annex II §2); an Art. 13(17) single point of contact is designated and contactable; fixed-vulnerability information (description, affected products, impacts, severity, remediation guidance) is publicly disclosed without delay after a security update is made available, with any `duly justified` delay recorded under the Art. 14(9) categories-based delay-justification framework; Art. 14(8) user-notification on confirmed AEVs/SIs is issued to known users; the EU vulnerability database under Art. 17(5) is populated; the Annex VII §2(b) technical documentation retains the CVD policy + intake/triage records + delay-justification register; verified by CVD policy inspection + contact-address machine-discoverability check + SPOC contactability test + public-disclosure record audit + Art. 14(9) delay-justification register inspection + EU vulnerability database population check + MSA + ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - RS.CO-03 — Information is shared with designated internal and external stakeholders — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Vulnerabilities in network and information systems are identified, handled, and disclos... | NIS2 | excessive | - | high |

### D-02.3 · NIS2 · subso SO-D-02.3.NIS2
- **Objective**: Vulnerabilities in network and information systems are identified, handled, and disclosed through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle (Art. 21(2)(e)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.3/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, GV.SC-04 — literal duplicate(s) of ID.RA-01, GV.SC-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Vulnerability handling and disclosure integrated into system acquisition, development,... | NIS2 | sufficient | - | high |

### D-02.3 · NIS2 · req 2.3.2
- **Title**: "Vulnerability handling and disclosure integrated into system acquisition, development, and maintenance lifecycle (entity-side institutional Art. 12(1) CSIRT-coordinated pathway acknowledgement)"
- **Description**: The product shall identify, handle, and disclose vulnerabilities in network and information systems through a coordinated vulnerability handling and disclosure process integrated into the system acquisition, development, and maintenance lifecycle, with the Art. 21(2)(e) appropriate-and-proportionate qualifier propagated from Art. 21(1) and the entity-side institutional CSIRT-coordinated pathway under Art. 12(1) acknowledged as the Member-State-level coordination channel that integrates with the 4.3 reporting cascade (per NIS 2 Art. 21(2)(e) + Art. 12(1) + Art. 21(3) sentence 1).
- **Fit criterion (prose)**: A coordinated vulnerability handling and disclosure process is integrated into the system acquisition, development, and maintenance lifecycle under Art. 21(2)(e); vulnerability signals from internal scanning, vendor advisories, threat-intelligence feeds and coordinated-disclosure submissions are ingested, validated against the entity's asset population, and recorded with severity, scope and remediation status in an ID.RA-01 register that survives the audit window; the supplier-vulnerability-assessment under Art. 21(3) sentence 1 captures upstream supplier vulnerability channels (including CRA-published advisories via the GV.SC-04 supplier-correspondence channel); the Art. 12(1) institutional CSIRT-coordinated pathway for significant incidents is operationally acknowledged (the institutional pathway is the Member-State CSIRT's coordinating role, out of SO scope per `99_NIS2_Synthesis.md` §8); the 4.3 Art. 23(4) cascade hook is operational on the same intake register; verified by CVD/handling-process documentation inspection + ID.RA-01 register audit + supplier-correspondence records + Art. 12(1) institutional pathway acknowledgement records + 4.3 cascade integration test + CSIRT or CA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.3/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-02.4 Threat-Led Penetration Testing

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are tested to ensure that they perform consistently for their inte... | AI_Act | excessive | - | high |

### D-02.4 · AI_Act · subso SO-D-02.4.AI_Act
- **Objective**: High-risk AI systems are tested to ensure that they perform consistently for their intended purpose (Art. 9(6)) and tested in real-world conditions in accordance with the detailed rules of Art. 60 (Art. 9(7)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04 — literal duplicate(s) of ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "High-risk AI systems tested to perform consistently for intended purpose (Art. 9(6)) a... | AI_Act | sufficient | - | high |

### D-02.4 · AI_Act · req 2.4.3
- **Title**: "High-risk AI systems tested to perform consistently for intended purpose (Art. 9(6)) and tested in real-world conditions per Art. 60 (Art. 9(7))"
- **Description**: The product shall have high-risk AI systems tested to ensure that they perform consistently for their intended purpose and tested in real-world conditions in accordance with the detailed rules of Art. 60, with the Art. 9(6) consistency-for-intended-purpose testing validating the AI-specific risk-management-measure effectiveness throughout the SDLC and the Art. 9(7) + Art. 60 real-world-conditions testing operating under the informed-consent regime (per AI Act Art. 9(6) + Art. 9(7) + Art. 60).
- **Fit criterion (prose)**: Art. 9(6) consistency-for-intended-purpose testing of the AI-system's risk-management-measure effectiveness operates throughout the lifecycle against the Art. 9(2) 4-step risk-identification cycle outputs (ID.RA-01 + ID.RA-04 substrate), with documented test records covering accuracy + robustness + cybersecurity dimensions (SR-AIACT-003); Art. 9(7) + Art. 60 real-world-conditions testing operates under the informed-consent regime (testing in real-world conditions requires informed consent of natural persons subjected to testing, with the detailed rules specified in Art. 60 implementing acts); the AI-system testing integrates with the SDLC (model training + validation + testing datasets per Art. 10 + model evaluation + adversarial testing) under PR.PS-06; the testing programme's reliance on third-party datasets, pre-trained components, and external evaluation services is captured under GV.SC-04 supplier-conformance; the Art. 72 post-market monitoring feedback loop consumes the testing evidence; verified by Art. 9(6) consistency-for-intended-purpose evidence + Art. 60 informed-consent records + SDLC testing integration review + Art. 72 post-market monitoring feedback loop trace + AI Act conformity-assessment body + MSA + AI Office inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Effective and regular tests and reviews of the security of a product with digital eleme... | CRA | excessive | - | high |

### D-02.4 · CRA · subso SO-D-02.4.CRA
- **Objective**: Effective and regular tests and reviews of the security of a product with digital elements are applied on a continuing basis throughout the support period, with the tests and reviews producing evidence of conformity with the Annex I Part I cybersecurity requirements (Annex I Part II (3) + Annex VII §6); reports of the tests carried out to verify conformity are part of the technical documentation (Annex VII §6); the testing programme itself is audited under Module B periodic audits of the vulnerability-handling processes (Annex VIII Part II (8)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/CRA_Art_27.md` (Art. 27) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-01, PR.PS-06, DE.CM-09 — literal duplicate(s) of ID.RA-01, PR.PS-06, DE.CM-09
- **Confidence**: high (article mapping and CSF title both consulted)

| "Effective and regular tests and reviews of product security across the support period ... | CRA | sufficient | - | high |

### D-02.4 · CRA · req 2.4.1
- **Title**: "Effective and regular tests and reviews of product security across the support period with Annex VII §6 test-report evidence + Annex VIII Part II (8) Module B periodic audits"
- **Description**: The product shall have effective and regular tests and reviews of its security applied on a continuing basis throughout the support period, with the tests and reviews producing evidence of conformity with the Annex I Part I cybersecurity requirements and reports of the tests carried out to verify conformity forming part of the technical documentation, and the testing programme itself being audited under Module B periodic audits of the vulnerability-handling processes (per CRA Annex I Part II (3) + Annex VII §6 + Annex VIII Part II (8) + Art. 13(7) + Art. 13(8) sentence 1).
- **Fit criterion (prose)**: An SDLC-integrated testing programme (static analysis + dynamic analysis + fuzzing + integration testing + penetration testing + threat-modelling reviews per SR-CRA-022 PR.PS-06) operates on a continuing basis across the support period under Art. 13(8); the testing programme produces documented test reports retained in the technical documentation under Annex VII §6; the testing programme is audited under Annex VIII Part II (8) Module B periodic audits of the vulnerability-handling processes; the `effective and regular` cadence is documented with: `effective` = test coverage and false-positive rates recorded per cycle; `regular` = scheduled cadence with the Annex VII §6 record per cycle; R3 test-once-before-release rejected as failing both `regular` and the Annex VIII Part II (8) periodic-audit anchor; verified by SDLC-pipeline evidence + Annex VII §6 test-report review + Annex VIII Part II (8) Module B periodic audit records + Annex I Part I cybersecurity-requirements conformity evidence + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/CRA_Art_27.md` (Art. 27) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A sound and comprehensive digital operational resilience testing programme is establish... | DORA | sufficient | - | high |

### D-02.4 · DORA · subso SO-D-02.4.DORA
- **Objective**: A sound and comprehensive digital operational resilience testing programme is established, maintained and reviewed as an integral part of the ICT risk-management framework (Art. 24(1)), drawing on a portfolio of testing modalities — vulnerability assessments, scans, open source analyses, network security assessments, gap analyses, physical security reviews, questionnaires and scanning software solutions, source code reviews where feasible, scenario-based tests, compatibility testing, performance testing, end-to-end testing and penetration testing (Art. 25(1)); the testing programme includes advanced testing by means of TLPT at least every three years, with frequency adjustments at the competent authority's request (Art. 26(1)).
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Sound and comprehensive testing programme (12-modality portfolio under Art. 25(1)) + a... | DORA | sufficient | - | high |

### D-02.4 · DORA · req 2.4.2
- **Title**: "Sound and comprehensive testing programme (12-modality portfolio under Art. 25(1)) + advanced TLPT every 3 years under Art. 26(1) where Art. 26(8) significant-entity criteria are met"
- **Description**: The product shall have a sound and comprehensive digital operational resilience testing programme established, maintained and reviewed as an integral part of the ICT risk-management framework, drawing on the Art. 25(1) 12-chunk portfolio of testing modalities (vulnerability assessments and scans; open source analyses; network security assessments; gap analyses; physical security reviews; questionnaires and scanning software solutions; source code reviews where feasible; scenario-based tests; compatibility testing; performance testing; end-to-end testing; penetration testing), with the programme reviewed at least yearly under Art. 24(1) and including advanced testing by means of TLPT at least every three years under Art. 26(1) where the Art. 26(8) significant-entity criteria (size, interconnectedness, complexity, risk profile) are met, with frequency adjustments at the competent authority's request (per DORA Art. 24(1) + Art. 25(1) + Art. 26(1) + Art. 26(8)).
- **Fit criterion (prose)**: A comprehensive testing programme covers all 12 OJ-named testing modalities per SR-DORA-008 OJ-literal enumeration (vulnerability assessments + scans + open source analyses + network security assessments + gap analyses + physical security reviews + questionnaires + scanning software solutions + source code reviews where feasible + scenario-based tests + compatibility testing + performance testing + end-to-end testing + penetration testing — `scanning software solutions` paired with `questionnaires` per OJ-chunk #6); the programme is reviewed at least yearly under Art. 24(1) with management-body approval (GV.OV-02 strategic-review records); advanced TLPT on the TIBER-EU methodology is performed at least every 3 years under Art. 26(1) where the Art. 26(8) significant-entity criteria are met, with CA-communicated frequency adjustments recorded (SR-DORA-009); the ID.RA-01 vulnerabilities-identified-validated-recorded register feeds the testing programme at the ICT-system level and the ID.RA-04 threats-identified-and-prioritised register sub-stratifies the testing programme by threat category; PR.PS-06 secure-software-development practices integrate the testing programme with the SDLC for entities that develop software; verified by testing-programme documentation audit + 12-modality coverage inspection + Art. 24(1) at-least-yearly programme review records + TLPT report inspection + CA-communicated frequency-adjustment log + ID.RA-01 + ID.RA-04 register review + management-body approval evidence + DORA CA + ESAs inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-03.1 Identity Lifecycle Management

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Identities, credentials, and access entitlements for users, services, and integrated co... | CRA | excessive | - | high |

### D-03.1 · CRA · subso SO-D-03.1.CRA
- **Objective**: Identities, credentials, and access entitlements for users, services, and integrated components of the product with digital elements are managed in a verifiable manner throughout the operational lifetime of the product (Annex I Part I (2)(d) + Art. 13(15) type/batch/serial unique identification + Art. 13(17) single point of contact; backed by Annex II §3 unique-identification user information).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09 — literal duplicate(s) of PR.AA-01, ID.AM-01, PR.AA-05, PR.AA-06, DE.CM-09
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product users, services, and integrated components identities managed in verifiable ma... | CRA | sufficient | - | high |

### D-03.1 · CRA · req 3.1.3
- **Title**: "Product users, services, and integrated components identities managed in verifiable manner throughout operational lifetime"
- **Description**: The product shall manage identities, credentials, and access entitlements for users, services, and integrated components of the product with digital elements in a verifiable manner throughout the operational lifetime of the product, with type/batch/serial unique identification per Art. 13(15) + Annex II §3 backing the SBOM-correlated identity register and a single point of contact per Art. 13(17) (CRA Annex I Part I (2)(d) + Art. 13(15) + Art. 13(17) + Annex II §3).
- **Fit criterion (prose)**: A product-side identity-management framework is maintained in verifiable manner throughout the operational lifetime, covering human users, service identities, and integrated-component identities; type/batch/serial unique-identification markings back the SBOM-correlated identity register (ID.AM-01 hardware-inventory substrate); reporting-on-access and attack-surface-limitation artefacts (PR.AA-05 + PR.AA-06) document least-privilege enforcement and authorised-only access to users/services/hardware; monitoring for attempted and successful unauthorised access (DE.CM-09) provides the visibility leg; the CRA `verifiable manner` reading is the strictest knowledge-test floor of the four participating regulators and discharges the GDPR `reasonable means proportionate to risk` when the same party operates both manufacturer-side and controller-side roles; verified by product-side identity-register audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + unique-identification marking review + SBOM format-validity check + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-01
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Identity assertions for financial-entity staff and service-to-service identities are ma... | DORA | excessive | - | high |

### D-03.1 · DORA · subso SO-D-03.1.DORA
- **Objective**: Identity assertions for financial-entity staff and service-to-service identities are managed, protected, and conveyed in a manner that verifies authenticity, as one dimension of the strong-authentication + cryptographic-key-protection + risk-based encryption 3-control AND in Art. 9(4)(d).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-03, PR.AA-04 — literal duplicate(s) of PR.AA-03, PR.AA-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Staff + service identities managed with assertion-conveyance integrity under strong-au... | DORA | sufficient | - | high |

### D-03.1 · DORA · req 3.1.4
- **Title**: "Staff + service identities managed with assertion-conveyance integrity under strong-authentication discipline"
- **Description**: The product shall manage, protect, and convey identity assertions for financial-entity staff and service-to-service identities in a manner that verifies authenticity, as one of the three coordinated controls in Art. 9(4)(d) (strong authentication + cryptographic-key protection + risk-based data encryption), backed by an authenticator-inventory register with AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 per the EBA Guidelines on ICT and security risk management §145–§148 dominant supervisory expectation (DORA Art. 9(4)(d)).
- **Fit criterion (prose)**: An identity provider operates with assertion-conveyance integrity (signed federated-identity tokens, mutual transport authentication, PKI chain-of-trust) for staff and service-to-service identities at the financial-entity boundary; an authenticator-inventory register with AAL mappings (NIST SP 800-63B AAL2/AAL3, FIDO2/WebAuthn for phishing-resistance, PKI for service-to-service) is maintained and reviewed; the DORA identity-assertion discipline (PR.AA-04) is the strictest assertion-conveyance floor and supports the NIS 2 `where appropriate` test on authentication strength for financial-sector entities also within retained NIS 2 scope; for pure-financial entities, DORA absorbs the NIS 2 workforce-identity-lifecycle obligation via lex specialis and the HL does not aggregate across the lex-specialis boundary; verified by authenticator-inventory register audit + AAL-mapping documentation review + PKI chain-of-trust audit logs + identity-provider assurance records + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The identity of a natural person making a rights-exercise request under Art. 15–22 is v... | GDPR | excessive | - | high |

### D-03.1 · GDPR · subso SO-D-03.1.GDPR
- **Objective**: The identity of a natural person making a rights-exercise request under Art. 15–22 is verified using reasonable means proportionate to the risk of mis-identification, before action is taken; the controller may request additional information necessary to confirm the identity, and the data subject must supply enough information to enable identification if they wish to exercise the rights (Art. 12(6) + Art. 11(2); the verification scope is constrained by Art. 5(1)(c) data minimisation).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.AA-02 — Identities are proofed and bound to credentials based on the context of interactions — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.AA-02 — Identities are proofed and bound to credentials based on the context of interactions — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-02 — Identities are proofed and bound to credentials based on the context of interactions — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-03, PR.AA-02, ID.AM-08 — literal duplicate(s) of PR.AA-03, PR.AA-02, ID.AM-08
- **Confidence**: high (article mapping and CSF title both consulted)

| "Data-subject identity verified using reasonable means proportionate to risk (rights-ex... | GDPR | sufficient | - | high |

### D-03.1 · GDPR · req 3.1.1
- **Title**: "Data-subject identity verified using reasonable means proportionate to risk (rights-exercise endpoint)"
- **Description**: The product shall verify the identity of a natural person making a rights-exercise request under Art. 15–22 using reasonable means proportionate to the risk of mis-identification, with the controller permitted to request additional information necessary to confirm the identity and the data subject supplying enabling information sufficient to confirm identification if they wish to exercise the rights; the verification scope is constrained by Art. 5(1)(c) data minimisation (GDPR Art. 12(6) + Art. 11(2) + Art. 5(1)(c)).
- **Fit criterion (prose)**: A graduated verification standard operates at the rights-exercise endpoint (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk) with verification requests anchored to documented risk-classification criteria; an Art. 5(1)(c) minimisation register documents the identity-verification artefacts collected and the proportionality justification per request class; the verification policy applies at the controller-facing rights-exercise boundary only, with the boundary hand-off to staff authentication (D-03.2) and to product-user identity management (CRA leg) documented as the controlled interface at which the GDPR verification discipline ends; verified by verification-policy inspection + graduated-verification records audit + Art. 5(1)(c) minimisation register review + boundary hand-off-protocol documentation + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-02 — Identities are proofed and bound to credentials based on the context of interactions — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Identities of the workforce — employees, contractors and other authorised personnel wit... | NIS2 | excessive | - | low |

### D-03.1 · NIS2 · subso SO-D-03.1.NIS2
- **Objective**: Identities of the workforce — employees, contractors and other authorised personnel with access to network and information systems — are managed throughout the employment lifecycle, with provisioning on induction, entitlement review on role change, and revocation on separation, integrated into the entity's access-control policy and asset-management discipline (Art. 21(2)(i) HR-security dimension, coordinated by the literal AND with access-control policies and asset management).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-01, PR.AA-05, PR.AT-02 — literal duplicate(s) of PR.AA-01, PR.AA-05, PR.AT-02
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Workforce identities managed throughout the employment lifecycle (joiner-mover-leaver)... | NIS2 | sufficient | - | low |

### D-03.1 · NIS2 · req 3.1.2
- **Title**: "Workforce identities managed throughout the employment lifecycle (joiner-mover-leaver)"
- **Description**: The product shall manage identities of the workforce — employees, contractors and other authorised personnel with access to network and information systems — throughout the employment lifecycle, with provisioning on induction, entitlement review on role change, and revocation on separation, integrated into the entity's access-control policy and asset-management discipline; the `appropriate and proportionate` qualifier from Art. 21(1) operationalises the lifecycle rigour with high-risk roles triggering tighter verification and review cadences than low-risk roles (NIS 2 Art. 21(2)(i) HR-security dimension, coordinated by the literal AND with access-control policies and asset management).
- **Fit criterion (prose)**: A joiner-mover-leaver (JML) register operates for the workforce with documented induction-provisioning tickets, role-transition review tickets, and separation-revocation tickets, each linked to the underlying personnel-record event; access-control policy and asset-management artefacts reference the JML register; risk-tiered verification and review cadences apply (privileged access and sensitive-data-exposure roles trigger tighter cadences than low-risk roles); the workforce identity-lifecycle discipline operates at the internal workforce boundary only, with the boundary hand-off to data-subject verification (GDPR leg) and product-user identity management (CRA leg) documented as the controlled interface at which the NIS 2 workforce discipline ends; verified by JML register audit + risk-tier mapping review + access-control policy inspection + asset-management cross-reference + competent authority / CSIRT inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.1/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title literally matches action keyword ('identities')
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-03.2 Multi-Factor Authentication

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Protection from unauthorised access uses appropriate control mechanisms, which may incl... | CRA | excessive | - | low |

### D-03.2 · CRA · subso SO-D-03.2.CRA
- **Objective**: Protection from unauthorised access uses appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product (Annex I Part I (2)(d) — "including but not limited to" + 3-way OR).
- **Anchors listed**:
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — Action keyword ('identity') in objective maps to PR.AA-01
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **UTILITY** — CSF title shares 1 token ('the') with objective; reinforces but is not the direct action
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — Action keyword ('identity') in objective maps to PR.AA-01
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **UTILITY** — CSF title shares 1 token ('the') with objective; reinforces but is not the direct action
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09 — literal duplicate(s) of PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Appropriate control mechanisms for protection from unauthorised access, which may incl... | CRA | sufficient | - | low |

### D-03.2 · CRA · req 3.2.3
- **Title**: "Appropriate control mechanisms for protection from unauthorised access, which may include authentication"
- **Description**: The product shall protect against unauthorised access through appropriate control mechanisms, which may include authentication, identity, or access-management systems, appropriate to the identified cybersecurity risk of the product; the OJ Annex I Part I (2)(d) text does NOT contain the phrase `multi-factor` or `continuous authentication` — the T2 mapping that imposed these phrases is rejected on the literal OJ — and the OJ names authentication as one of three admitted control families (the others being identity and access-management) (CRA Annex I Part I (2)(d) — `including but not limited to` + 3-way OR).
- **Fit criterion (prose)**: A product-side authentication-mechanism choice operates, anchored to a documented risk assessment for the product with digital elements; the OJ Annex I Part I (2)(d) text does not specify the authentication mechanism, so the SR preserves the OJ-literal language without naming MFA; the mechanism selection is at the manufacturer's discretion under the 3-way OR (authentication / identity / access-management); an MFA deployment at the CRA product-side exceeds the CRA requirement on the authentication dimension; a single-factor deployment at a CRA-regulated product is OJ-compliant under CRA but may not satisfy NIS 2 or DORA when those regs apply on the same party; reporting-on-access and attack-surface-limitation artefacts document least-privilege enforcement and authorised-only access to users/services/hardware; monitoring for attempted and successful unauthorised access (DE.CM-09) provides the visibility leg; verified by risk-assessment audit + mechanism-selection rationale records + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + MSA / ENISA inspection-ready evidence pack on request.
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — Action keyword ('identity') in objective maps to PR.AA-01
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| Strong authentication mechanisms (based on relevant standards and dedicated control sys... | DORA | excessive | - | high |

### D-03.2 · DORA · subso SO-D-03.2.DORA
- **Objective**: Strong authentication mechanisms (based on relevant standards and dedicated control systems) are implemented as one of three coordinated controls in Art. 9(4)(d), together with cryptographic-key protection measures and risk-based data encryption.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-03, PR.AA-04 — literal duplicate(s) of PR.AA-03, PR.AA-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Strong authentication mechanisms based on relevant standards (Art. 9(4)(d); dominant E... | DORA | sufficient | - | high |

### D-03.2 · DORA · req 3.2.4
- **Title**: "Strong authentication mechanisms based on relevant standards (Art. 9(4)(d); dominant EBA MFA reading)"
- **Description**: The product shall implement strong authentication mechanisms based on relevant standards and dedicated control systems, as one of three coordinated controls in Art. 9(4)(d), together with cryptographic-key protection measures and risk-based data encryption; the OJ Art. 9(4)(d) text does NOT contain the phrase `multi-factor` — the T4-vs-text gap is P0-flagged in `SR-DORA-002` `ambiguity_notes` — but the dominant EBA Guidelines on ICT and security risk management §145–§148 reading is MFA (DORA Art. 9(4)(d)).
- **Fit criterion (prose)**: An authenticator-inventory register with AAL mappings aligned with NIST SP 800-63B AAL2/AAL3 (per the EBA Guidelines §145–§148 dominant supervisory expectation) is maintained for financial-entity staff, service identities, and machine identities; the strong-authentication architecture includes FIDO2/WebAuthn for phishing-resistance, PKI for service-to-service, certificate-based authentication in service-to-service flows, signed federated-identity tokens, mutual transport authentication, and PKI chain-of-trust for identity-assertion integrity (PR.AA-04); the DORA strong-authentication floor discharges the NIS 2 `where appropriate` test (when NIS 2 also applies — typically only on cross-sector entities), exceeds the CRA `may include` permissive baseline, and provides the strong-authentication substrate that the GDPR silent-wrapper surrounds with instructions + confidentiality; for pure-financial entities, DORA absorbs the NIS 2 authentication-strength obligation via lex specialis; the T4-vs-text gap on `strong authentication` vs MFA is documented as the chosen reading (mechanism-agnostic R5 with R3 MFA as the dominant EU supervisory reading, pending the ESAs Joint Committee RTS under Art. 15); verified by authenticator-inventory register audit + AAL-mapping documentation review + PKI chain-of-trust audit logs + identity-provider assurance records + chosen-reading rationale records + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Persons authorised to process personal data act only on documented instructions from th... | GDPR | sufficient | - | low |

### D-03.2 · GDPR · subso SO-D-03.2.GDPR
- **Objective**: Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality (Art. 28(3)(b) + Art. 29 + Art. 32(4) instruction-only processing); the identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification (Art. 12(6) + Art. 11(2)).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_5.md` (Art. 5) — paraphrased action
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Authentication governed by instructions + confidentiality + minimisation (no OJ authen... | GDPR | sufficient | - | low |

### D-03.2 · GDPR · req 3.2.1
- **Title**: "Authentication governed by instructions + confidentiality + minimisation (no OJ authentication-strength threshold)"
- **Description**: The product shall ensure that persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality, and that the identity of data subjects making rights-exercise requests is verified using reasonable means proportionate to the risk of mis-identification; GDPR does not impose an authentication-strength threshold — the OJ Art. 28(3)(b) + Art. 29 obligations govern the authorisation and confidentiality of authenticated staff, and Art. 12(6) governs the verification of the data-subject requester at the rights-exercise endpoint (GDPR Art. 28(3)(b) + Art. 29 + Art. 32(4) + Art. 12(6) + Art. 11(2)).
- **Fit criterion (prose)**: A chain-of-authority pattern operates (controller → processor → authorised persons, with documented instructions binding each link) and a verification pattern operates (data-subject → verification-on-reasonable-doubt → proportionate additional information); Art. 28(3)(b) processor-contract confidentiality is documented for all processors and sub-processors; Art. 5(1)(c) minimisation applies to authentication-verification artefacts; the authentication-strength selection is the controller's discretion — a controller selecting MFA at the staff-authentication endpoint satisfies Art. 32(1)(b) confidentiality, a controller selecting single-factor password authentication is not forbidden by GDPR but must satisfy the surrounding instruction + confidentiality + minimisation obligations; the GDPR silent-wrapper around authentication is the surrounding obligation that does not impose an authentication-strength threshold but does require the authorisation + verification architecture; verified by documented-instructions register audit + processor-contract confidentiality review + verification-policy inspection + minimisation register review + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_5.md` (Art. 5) — paraphrased action
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Multi-factor authentication or continuous authentication solutions are used where appro... | NIS2 | excessive | - | high |

### D-03.2 · NIS2 · subso SO-D-03.2.NIS2
- **Objective**: Multi-factor authentication or continuous authentication solutions are used where appropriate, and secured voice, video and text communications as well as secured emergency communication systems are deployed within the entity (Art. 21(2)(j)).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 3 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 3 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03 — literal duplicate(s) of PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03
- **Confidence**: high (article mapping and CSF title both consulted)

| "Multi-factor or continuous authentication `where appropriate` (Art. 21(2)(j) first cla... | NIS2 | sufficient | - | high |

### D-03.2 · NIS2 · req 3.2.2
- **Title**: "Multi-factor or continuous authentication `where appropriate` (Art. 21(2)(j) first clause)"
- **Description**: The product shall use multi-factor authentication or continuous authentication solutions where appropriate, and deploy secured voice, video and text communications and secured emergency communication systems within the entity; the OR admits both MFA and continuous-authentication as alternative authentication paradigms — they are not redundant — and the `where appropriate` hedge closes the sub-point (NIS 2 Art. 21(2)(j)).
- **Fit criterion (prose)**: An authentication-mechanism choice (MFA or continuous-authentication) is documented with risk-tier mapping anchored to Art. 21(1) factors (state of the art, costs of implementation, exposure, size, risk) and a documented `where appropriate` justification per authentication surface; ENISA 2022 baseline security recommendations (MFA as default for all administrative and privileged access) are reflected in the risk-tier mapping; the mechanism selection (FIDO2 / WebAuthn vs TOTP vs hardware-token) is at the entity's discretion under the mechanism-agnostic R5 reading; the SMS-OTP reading is rejected for new deployments given the SS7 / SIM-swap attack surface; the DORA strong-authentication floor (≈ MFA via EBA reading) discharges the `where appropriate` test when DORA applies on the same party; the second and third clauses of Art. 21(2)(j) (secured voice/video/text + secured emergency) are routed to D-01.2 (data-in-transit) and D-04.4 (resilience) and are out of scope of this D-03.2 leg; verified by risk-tier mapping review + mechanism-selection rationale records + ENISA-baseline gap assessment + competent authority / CSIRT inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.2/articles/DORA_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — Action keyword ('authentication') in objective maps to PR.AA-03
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 4 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title literally matches action keyword ('data-in-transit')
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-03.3 Authorisation & Least Privilege

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Access to the product with digital elements, its data, services, and functions is limit... | CRA | excessive | - | low |

### D-03.3 · CRA · subso SO-D-03.3.CRA
- **Objective**: Access to the product with digital elements, its data, services, and functions is limited to authenticated and authorised users, services, and hardware, with possible unauthorised access reported (Annex I Part I (2)(d) `protection from unauthorised access through appropriate control mechanisms` + `possible unauthorised access reported` — R1 inclusive reading on `possible`) and attack surfaces including external interfaces limited (Annex I Part I (2)(j)).
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-05, PR.AA-06, DE.CM-09 — literal duplicate(s) of PR.AA-05, PR.AA-06, DE.CM-09
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Access to product with digital elements limited to authenticated and authorised users,... | CRA | sufficient | - | low |

### D-03.3 · CRA · req 3.3.3
- **Title**: "Access to product with digital elements limited to authenticated and authorised users, services, and hardware; possible unauthorised access reported; attack surfaces including external interfaces limited (multi-leg product-side authorisation framework)"
- **Description**: The product shall limit access to the product with digital elements, its data, services and functions to authenticated and authorised users, services, and hardware, with possible unauthorised access reported (R1 inclusive reading on `possible` — any successful + any detected-but-failed attempt) and attack surfaces including external interfaces limited (CRA Annex I Part I (2)(d) `protection from unauthorised access through appropriate control mechanisms` + `possible unauthorised access reported` + Annex I Part I (2)(j) `limit attack surfaces including external interfaces`).
- **Fit criterion (prose)**: A product-side authenticated-and-authorised boundary operates with PR.AA-05 + PR.AA-06 least-privilege entitlement baseline + boundary-enforcement on physical and logical assets; a reporting-and-monitoring substrate under PR.PS-04 + DE.CM-09 captures attempted and successful unauthorised access and surfaces it as observable events; type/batch/serial unique-identification markings per Art. 13(15) + Annex II §3 back the SBOM-correlated identity register (ID.AM-01) on which the (2)(d) control mechanisms rely; Annex I Part I (2)(j) attack-surface-reduction evidence documents least-privilege enforcement at external interfaces (network ingress, exposed APIs, hardware ports); the `possible unauthorised access` R1 inclusive reading is the strictest visibility floor across the four regulators — R2 (any access attempt at all) overreaches the literal, R3 (failed-but-detected subset only) under-reaches because successful breaches must also be reported; the product-side authorisation framework operates at the product boundary only, with the boundary hand-off to GDPR personal-data-scope chain (when the CRA product hosts data-subject rights endpoints) and to NIS 2 entity-side access-control policy (when a CRA manufacturer is also a NIS 2 essential entity) and to DORA financial-entity-side ICT-asset access (when a DORA financial entity deploys the CRA product) documented as the controlled interfaces at which the CRA product-side discipline ends; verified by product-side identity-register audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + attack-surface-reduction evidence + runtime-monitoring logs + Annex II §8 user-facing instructions on monitoring + opt-out + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — Action keyword ('identity') in objective maps to PR.AA-01
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| ICT security policies limit physical or logical access to information assets and ICT as... | DORA | excessive | - | high |

### D-03.3 · DORA · subso SO-D-03.3.DORA
- **Objective**: ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only, with the literal `only` qualifier (Berry §5.3.1 — correctly placed before the limiting phrase) closing off any access that is not strictly tied to a legitimate and approved function (Art. 9(4)(c) physical or logical access + `legitimate AND approved` AND-coordinated + `only` qualifier).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-05, PR.AA-06 — literal duplicate(s) of PR.AA-05, PR.AA-06
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial-entity ICT security policies limit physical or logical access to information... | DORA | sufficient | - | high |

### D-03.3 · DORA · req 3.3.4
- **Title**: "Financial-entity ICT security policies limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only (literal `only` qualifier)"
- **Description**: The product shall ensure that ICT security policies of the financial entity limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only, with the literal `only` qualifier (Berry §5.3.1 — `only` correctly placed before the limiting phrase) closing off any access that is not strictly tied to a legitimate and approved function, anchored to PR.AA-05 + PR.AA-06 with the OJ `legitimate AND approved` two-axis gating operationalised through documented entitlement rationales and access-request approval workflows with multi-party authorisation for privileged grants (DORA Art. 9(4)(c) physical or logical access + `legitimate AND approved` AND-coordinated + `only` qualifier).
- **Fit criterion (prose)**: A financial-entity-side ICT-asset access policy operates with the literal `only` qualifier enforced on every access grant — no access may be granted that is not tied to a documented legitimate and approved function; an entitlement inventory + access-review records + separation-of-duties attestation logs + physical-access audit trails (badge access, mantrap entry, secure-room zoning, CCTV) satisfy the PR.AA-05 + PR.AA-06 physical-and-logical twin layer; multi-party authorisation is enforced for privileged grants on the OJ `legitimate AND approved` two-axis gating (function-aligned entitlement rationale AND governance-approved access-request approval workflow); the T4-vs-text gap on `need-to-know + least privilege` vocabulary not present in the OJ literal is preserved as OJ-literal `legitimate and approved functions and activities only` — Layer 2/3 to adjudicate whether the T-imposed best practice survives as interpretive continuation; the DORA `only` qualifier is the binding authorisation floor where the financial-entity-side stacks up on the same artefact with CRA product-side `limited to authenticated and authorised` and NIS 2 model-agnostic `access control policies`, and discharges those obligations on the same access-control substrate when both apply; the financial-entity-side ICT-asset access discipline operates at the financial-entity boundary only, with the boundary hand-off to NIS 2 entity-side model-agnostic access-control policy (when the financial entity is also a NIS 2 essential entity, i.e. cross-sector) and to CRA product-side authenticated-and-authorised boundary (when a DORA financial entity deploys CRA products) documented as the controlled interfaces at which the DORA `legitimate and approved only` discipline ends; verified by entitlement inventory audit + access-review records + separation-of-duties attestation logs + physical-access audit trails + multi-party-authorisation log review + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.AA-03 — Users, services, and hardware are authenticated — **CORE** — CSF title literally matches action keyword ('authenticated')
  - PR.AA-04 — Identity assertions are protected, conveyed, and verified — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title literally matches action keyword ('least privilege')
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Persons authorised to process personal data act only on documented instructions from th... | GDPR | excessive | - | high |

### D-03.3 · GDPR · subso SO-D-03.3.GDPR
- **Objective**: Persons authorised to process personal data act only on documented instructions from the controller (or processor), and are bound by confidentiality or an appropriate statutory obligation of confidentiality, with documented instructions binding the controller → processor → authorised-persons chain of authority under Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) and Art. 4(7) + Art. 4(8) anchoring controller and processor definitions.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/GDPR_Art_28.md` (Art. 28) — paraphrased action
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-05, PR.AA-06, PR.AT-02 — literal duplicate(s) of PR.AA-05, PR.AA-06, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Authorisation in personal-data scope operates through documented instructions and conf... | GDPR | sufficient | - | high |

### D-03.3 · GDPR · req 3.3.1
- **Title**: "Authorisation in personal-data scope operates through documented instructions and confidentiality undertakings (chain of authority controller → processor → authorised persons)"
- **Description**: The product shall ensure that persons authorised to process personal data act only on documented instructions from the controller (or processor), with the controller → processor → authorised-persons chain of authority binding each link and authorised persons bound by confidentiality or an appropriate statutory obligation of confidentiality, anchored to PR.AA-05 + PR.AA-06 + PR.AT-02 on the personal-data-scope chain-of-authority pattern that Arts. 29 + 28(3)(a)/(b) + 32(4) establish (GDPR Art. 29 + Art. 32(4) + Art. 28(3)(a)/(b) + Art. 4(7)/(8)).
- **Fit criterion (prose)**: A documented-instructions register records, for each processing operation, the controller-issued instruction, the processor-contract Art. 28(3)(a)/(b) clause that anchors it, and the operational instructions issued under it; an Art. 28(3)(b) confidentiality-undertaking register binds each authorised natural person (controller staff, processor staff, sub-processor staff) to either an equivalent-scope NDA, a pre-existing statutory professional-secrecy, or a Member-State-law public-sector employee-secrecy; technical enforcement under PR.AA-05 + PR.AA-06 prevents processing outside documented authority and surfaces it as observable events; the personal-data-scope chain-of-authority discipline operates at the staff-side / processor-boundary only, with the boundary hand-off to NIS 2 workforce-side lifecycle (D-03.1) and to CRA product-side authenticated-and-authorised boundary documented as the controlled interfaces at which the GDPR instruction-bound discipline ends; verified by documented-instructions register audit + Art. 28(3)(a)/(b) processor-contract inspection + confidentiality-undertaking register review + PR.AA-05/PR.AA-06 access-enforcement evidence + boundary hand-off-protocol documentation + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/GDPR_Art_28.md` (Art. 28) — paraphrased action
- **Anchors listed**:
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-06
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Access-control policies are established and applied at the entity level for the entity'... | NIS2 | excessive | - | low |

### D-03.3 · NIS2 · subso SO-D-03.3.NIS2
- **Objective**: Access-control policies are established and applied at the entity level for the entity's network and information systems, covering access limited to authorised users, services, and hardware on a least-privilege basis, with the literal AND binding access-control + HR-security + asset-management together (Art. 21(2)(i)).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title shares 7 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — CSF title shares 7 action tokens with objective
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — Action keyword ('authoris') in objective maps to PR.AA-05
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02 — literal duplicate(s) of PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Entity-side access-control policy established and applied to network and information s... | NIS2 | sufficient | - | low |

### D-03.3 · NIS2 · req 3.3.2
- **Title**: "Entity-side access-control policy established and applied to network and information systems on a model-agnostic least-privilege basis (Art. 21(2)(i) literal AND of AC + HR-security + asset-management)"
- **Description**: The product shall establish and apply access-control policies at the entity level for the entity's network and information systems, covering access limited to authorised users, services, and hardware on a least-privilege basis, with the literal AND of the Art. 21(2)(i) sub-point binding access-control + HR-security + asset-management together and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the rigour (NIS 2 Art. 21(2)(i) literal AND with HR-security + asset-management; Art. 21(1) appropriate-and-proportionate propagates).
- **Fit criterion (prose)**: A model-agnostic access-control policy (the OJ does not impose RBAC, ABAC, MAC or DAC — the policy can be implemented under any model that satisfies least-privilege; the T3-vs-text gap on `RBAC + need-to-know + least privilege` vocabulary not present in the OJ is preserved as model-agnostic) is established and applied with documented role definitions, PR.AA-01 identity-governance evidence base (joiner/mover/leaver records, privilege reviews, entitlement inventories) and PR.AA-05 least-privilege policy + entitlement assignments + access-review records + revocation tickets; the literal AND of the three Art. 21(2)(i) sub-domains is preserved — AC + HR-security (D-03.1) + asset-management (D-09.3 / D-03.3 cross) all three required in cumulative form, partial-compliance readings (two-of-three) rejected by the literal conjunction; the entity-side access-control policy discipline operates at the internal entity boundary only, with the boundary hand-off to GDPR personal-data-scope chain (D-03.3 GDPR sub-requirement) and to CRA product-side authenticated-and-authorised boundary documented as the controlled interfaces at which the NIS 2 model-agnostic discipline ends; Member State transposition divergence may apply on national AC-model compatibility (e.g. French ANSSI classified-inventory expectations for essential sectors, German BSI authoritative-register expectations); verified by access-control policy inspection + role-definition documentation review + HR-lifecycle records audit (D-03.1) + asset-management cross-reference (D-09.3 / D-03.3) + privilege-review records + competent authority / CSIRT inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — CSF title literally matches action keyword ('inventories')
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title literally matches action keyword ('inventories')
  - PR.AA-01 — Identities and credentials for authorized users, services, and hardware are managed by the organization — **CORE** — Action keyword ('identity') in objective maps to PR.AA-01
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title literally matches action keyword ('least privilege')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-03.4 Secure System Defaults

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Products with digital elements are made available on the market with a secure-by-defaul... | CRA | excessive | - | low |

### D-03.4 · CRA · subso SO-D-03.4.CRA
- **Objective**: Products with digital elements are made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements (Annex I Part I (2)(b)), and the secure-by-default configuration ensures that vulnerabilities can be addressed through security updates — automatic security updates installed within an appropriate timeframe, enabled by default, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them (Annex I Part I (2)(c)).
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-01, ID.AM-08, GV.SC-03 — literal duplicate(s) of PR.PS-01, ID.AM-08, GV.SC-03
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Products with digital elements made available with secure-by-default configuration + r... | CRA | sufficient | - | high |

### D-03.4 · CRA · req 3.4.2
- **Title**: "Products with digital elements made available with secure-by-default configuration + reset-to-original-state capability + auto-update default + opt-out + postponement (Annex I Part I (2)(b) + (2)(c) multi-leg product default)"
- **Description**: The product shall be made available on the market with a secure-by-default configuration — including the possibility for the user to reset the product to its original state — unless otherwise agreed between manufacturer and business user in relation to a tailor-made product with digital elements, and the secure-by-default configuration shall ensure that vulnerabilities can be addressed through security updates — automatic security updates installed within an appropriate timeframe, enabled by default, with a clear and easy-to-use opt-out mechanism, through notification of available updates to users, and with the option to temporarily postpone them (CRA Annex I Part I (2)(b) + Art. 6(a) proviso + Art. 3(23) intended-purpose anchor + Annex I Part I (2)(c) + Annex II §8(e) opt-out discoverability).
- **Fit criterion (prose)**: A product-centric secure-by-default configuration operates with PR.PS-01 configuration-management baseline applied at first power-up to every unit leaving the manufacturing pipeline (R1 features-enabled-on-default — security features including authentication, access control, audit logging, network segmentation, secure-update mechanism enabled by default at first power-up; R2 deny-all-initial state and R3 zero-config-security operationally-convergent alternative readings rejected where they would conflict with the tailor-made carve-out; R4 post-deployment-surface rejected where it would conflict with the tailor-made carve-out); the reset-to-original-state capability (R1 factory-reset-no-user-data as the literal reading; R2 initial-config-preserving-user-data underweights the reset semantic) provides the recovery path back to the secure baseline; the tailor-made carve-out (R1 business-user-only on the carve-out scope; R2 any-customised rejected as overreach; consumer products cannot opt out of the default-secure floor) is documented in tailor-made contractual records; the auto-update default (R1 enabled-by-default-with-opt-out adopted; R2 deny-all-initial state; R3 zero-config security; R2 and R3 operationally-convergent with R1 in many cases; R4 post-deployment-surface rejected where it would conflict with the tailor-made carve-out) is on by default at first power-up with a clear and easy-to-use opt-out mechanism (UI discoverable + single-click) per Annex II §8(e); notification of available updates is delivered to users; postponement is temporarily available; Annex I Part I (2)(c) `within an appropriate timeframe` is anchored to the severity of the addressed vulnerability and the user's operational environment per the Art. 13(2) risk assessment (R2 chosen; R1 single quantitative ceiling rejected because severity modulation is the operative sanity check; R3 manufacturer discretion rejected as failing the inquiry-resistant test); ID.AM-08 data-management risk strategy governs the configuration-management baseline policy; the CRA tailor-made carve-out does NOT propagate into GDPR scope — even a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2) on the data side; verified by secure-by-default configuration audit + reset-capability evidence + tailor-made contractual records + auto-update default documentation + opt-out discoverability check + update-notification mechanism review + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + Annex II §8(e) user-facing-instructions inspection + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal-data processing systems implement appropriate technical and organisational mea... | GDPR | excessive | - | high |

### D-03.4 · GDPR · subso SO-D-03.4.GDPR
- **Objective**: Personal-data processing systems implement appropriate technical and organisational measures ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed — across the four AND-coordinated dimensions of amount of data collected, extent of their processing, period of their storage, and their accessibility — with the additional constraint that personal data are not made accessible without the individual's intervention to an indefinite number of natural persons (Art. 25(2) + Art. 25(1) privacy-by-design cross-anchor + Art. 5(1)(c) data minimisation underlying principle).
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.4/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 5 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-01, ID.AM-08 — literal duplicate(s) of PR.PS-01, ID.AM-08
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data processing systems implement by-default measures across amount, extent, ... | GDPR | sufficient | - | high |

### D-03.4 · GDPR · req 3.4.1
- **Title**: "Personal-data processing systems implement by-default measures across amount, extent, period, and accessibility (Art. 25(2) four-dimension AND)"
- **Description**: The product shall ensure that personal-data processing systems implement appropriate technical and organisational measures such that, by default, only personal data which are necessary for each specific purpose of the processing are processed — across the four AND-coordinated dimensions of amount of personal data collected, extent of their processing, period of their storage, and their accessibility — with the additional constraint that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons (GDPR Art. 25(2) + Art. 25(1) privacy-by-design + Art. 5(1)(c) data minimisation underlying principle).
- **Fit criterion (prose)**: A by-default configuration operates at the processing-system level with the four Art. 25(2) dimensions minimised independently and AND-coordinated — amount of personal data collected limited to what is necessary for the specific purpose (no over-collection); extent of processing limited to operations necessary for the specific purpose (no out-of-purpose processing); period of storage limited to retention necessary for the specific purpose (no indefinite retention); accessibility limited to recipients intended by the specific purpose (no exposure to an indefinite number of natural persons without the individual's intervention); PR.PS-01 configuration-management baseline establishes the four default values as system properties rather than operator judgement; ID.AM-08 data-management risk strategy governs opt-in collection, opt-out for out-of-purpose operations, minimum-necessary retention, and no public access unless explicitly granted; GV.PO-01 organisational cybersecurity policy is the governance-side anchor; the EDPB Guidelines 04/2019 four-independent-minima reading is preserved — any reading allowing some dimensions to be relaxed if others are tightened is rejected as it would weaken the default and is not supported by EDPB; the `without the individual's intervention` opt-in gate closes the accessibility dimension — the controller must not bypass the data subject's affirmative action to expose data; the data-centric by-default discipline operates at the processing-system layer only, with the layer hand-off to CRA product-centric secure-by-default (when the processing system is a CRA-regulated product) documented as the controlled layer interface at which the GDPR data-centric four-dimension AND ends; the CRA tailor-made carve-out does NOT propagate into GDPR scope — even a CRA tailor-made product configuration does not exempt the controller from GDPR Art. 25(2); verified by four-dimension by-default settings audit + Art. 5(1)(c) minimisation register review + opt-in-gate evidence + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-03_Access-Control/D-03.4/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-04.1 Incident Detection & Triage

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Relevant internal activity of the product with digital elements — including access to o... | CRA | excessive | - | low |

### D-04.1 · CRA · subso SO-D-04.1.CRA
- **Objective**: Relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — is recorded and monitored, with a user-visible opt-out mechanism where appropriate, and any corruption or unauthorised modification is reported (Annex I Part I (2)(l)).
- **Anchors listed**:
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - DE.AE-08 — Incidents are declared when adverse events meet the defined incident criteria — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-02 — Incident reports are triaged and validated — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-04, DE.CM-09 — literal duplicate(s) of PR.PS-04, DE.CM-09
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Product-internal activity recorded and monitored with user opt-out where appropriate; ... | CRA | sufficient | - | high |

### D-04.1 · CRA · req 4.1.3
- **Title**: "Product-internal activity recorded and monitored with user opt-out where appropriate; corruption / unauthorised modification reported"
- **Description**: The product shall record and monitor relevant internal activity of the product with digital elements — including access to or modification of data, services, or functions — on a continuing basis throughout the support period under Art. 13(8), with a user-visible opt-out mechanism where appropriate for events that are not security-critical, and any corruption or unauthorised modification shall be reported to the user (CRA Annex I Part I (2)(l) + Part II (6) + Art. 13(8)).
- **Fit criterion (prose)**: An intra-product recording capability is maintained on a continuing basis throughout the support period under Art. 13(8), capturing state changes relevant to security (access to or modification of data, services, or functions) via DE.CM-09 computing-hardware-monitored leg + PR.PS-04 software-logs-recorded leg + RS.MA-02 incident-reports-triaged leg; a user-visible opt-out mechanism operates where appropriate for events that are not security-critical (the opt-out is not a blanket opt-out of security-relevant events); corruption and unauthorised-modification events are reported to the user via the reporting mechanism under Annex I Part II (6); the recording-and-monitoring obligation is CRA-unique and provides the manufacturer's view inside the product boundary; the product-internal recording feeds the deployer's entity-level (NIS 2) and financial-entity (DORA) detection pipelines as a feed, not a substitute; the product-internal detection discipline operates at the product boundary only, with the boundary hand-off to data-flow detection (GDPR leg) and entity-level all-hazards monitoring (NIS 2 leg) documented as the controlled interfaces; verified by Annex I (2)(l) recording-coverage audit + Annex I Part II (6) reporting-mechanism inspection + user-opt-out mechanism review (events that are not security-critical) + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — CSF title literally matches action keyword ('triage')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Anomalous activities — including ICT network performance issues and ICT-related inciden... | DORA | excessive | - | high |

### D-04.1 · DORA · subso SO-D-04.1.DORA
- **Objective**: Anomalous activities — including ICT network performance issues and ICT-related incidents — are promptly detected through detection mechanisms that enable multiple layers of control, define alert thresholds and criteria, trigger and initiate ICT-related incident response processes, and identify potential material single points of failure (Art. 10(1) + Art. 10(2)). An ICT-related incident management process is defined, established and implemented to detect, manage and notify ICT-related incidents (Art. 17(1)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title shares 3 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('anomal') in objective maps to DE.AE-02
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title shares 3 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('anomal') in objective maps to DE.AE-02
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: DE.CM-01, DE.CM-09, DE.AE-02, RS.MA-01 — literal duplicate(s) of DE.CM-01, DE.CM-09, DE.AE-02, RS.MA-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Multi-class anomalous-activity detection with SPOF identification, alert thresholds, a... | DORA | sufficient | - | high |

### D-04.1 · DORA · req 4.1.4
- **Title**: "Multi-class anomalous-activity detection with SPOF identification, alert thresholds, automatic escalation, and Art. 17(1) `detect` leg of incident management process"
- **Description**: The product shall operate a financial-entity ICT infrastructure detection capability that promptly detects anomalous activities — including ICT network performance issues and ICT-related incidents — through detection mechanisms that enable multiple layers of control, define alert thresholds and criteria to trigger and initiate ICT-related incident response processes (including automatic alert mechanisms for relevant staff in charge of ICT-related incident response), and identify potential material single points of failure; an ICT-related incident management process shall be defined, established and implemented to detect, manage and notify ICT-related incidents (DORA Art. 10(1) + Art. 10(2) + Art. 17(1) `detect` leg).
- **Fit criterion (prose)**: A multi-layer detection architecture is operated on the financial-entity ICT infrastructure with DE.CM-01 networks-monitored leg + DE.CM-09 computing-hardware-monitored leg (SPOF identification substrate) + DE.AE-02 adverse-event analysis leg for threshold-driven escalation; the architecture defines explicit alert thresholds and criteria (Art. 10(2)) and includes automatic alert mechanisms for relevant staff in charge of ICT-related incident response; an SPOF register (Art. 10(1) `identify potential material single points of failure`) is maintained and reviewed with material-SPOF remediation tracking; the Art. 17(1) ICT-related incident management process is defined, established and implemented, with the `detect` leg wired into the multi-layer detection architecture under RS.MA-01 incident-management-plan-executed; the DORA detection architecture is the operational source of GDPR awareness events (Art. 33(1) `becoming aware` — 4.3 cross-ref) when personal data are involved on the same party; for pure-financial entities, DORA absorbs the NIS 2 detection obligation for the ICT-hazard subset via lex specialis; the financial-entity detection discipline operates at the financial-entity boundary only, with the boundary hand-off to data-flow detection (GDPR leg) and entity-level all-hazards monitoring (NIS 2 leg) documented as the controlled interfaces; verified by multi-layer detection-architecture documentation audit + alert-threshold definitions review + auto-alert mechanism operational-test evidence + SPOF register audit + Art. 17(1) incident-management-process inspection + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('audit') in objective maps to DE.AE-02
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — Action keyword ('incidents') in objective maps to RS.MA-02
  - RS.MA-03 — Incidents are categorized and prioritized — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal-data breaches are detected and triaged, and the moment of "becoming aware" is ... | GDPR | excessive | - | high |

### D-04.1 · GDPR · subso SO-D-04.1.GDPR
- **Objective**: Personal-data breaches are detected and triaged, and the moment of "becoming aware" is documented to anchor the 72-hour notification clock (Art. 33(1) + Art. 4(12) breach definition).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — CSF title literally matches action keyword ('triage')
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 2 action tokens with objective
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: DE.CM-01 — literal duplicate(s) of DE.CM-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data breaches detected at the controller data-flow boundary with documented `... | GDPR | sufficient | - | high |

### D-04.1 · GDPR · req 4.1.1
- **Title**: "Personal-data breaches detected at the controller data-flow boundary with documented `becoming aware` moment anchoring the 72h clock"
- **Description**: The product shall detect personal-data breaches at the controller's data-flow boundary — covering the five Art. 4(12) breach types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data transmitted, stored or otherwise processed) — and shall document the moment of "becoming aware" by a controller employee with delegated breach-handling responsibility, with the awareness moment anchoring the Art. 33(1) 72-hour notification clock in 4.3 (GDPR Art. 32(1)(b) + Art. 33(1) `becoming aware` + Art. 4(12) breach definition).
- **Fit criterion (prose)**: Continuous monitoring of the controller's data-flow boundary is operated covering the five Art. 4(12) breach types via DE.CM-01 networks-monitored leg (unauthorised disclosure / exfiltration vector) + DE.CM-09 host / runtime / data leg (alteration / access / loss vector) + PR.PS-04 log-records-generated leg; a designated breach-handling role receives validated incident reports under RS.MA-02 incident-reports-triaged; a documented `becoming aware` moment is timestamped at the moment the breach is captured by the controller's detection capability and recorded per EDPB Guidelines 9/2022 §3.4; the awareness moment anchors the Art. 33(1) 72h clock (4.3 cross-ref); the data-flow detection discipline operates at the controller boundary only, with the boundary hand-off to entity-level all-hazards monitoring (NIS 2 leg) and product-internal recording (CRA leg) documented as the controlled interfaces; verified by data-flow monitoring coverage audit + breach-detection log review + `becoming aware` timestamp records inspection + breach-handling role-designation documentation + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('log') in objective maps to DE.AE-02
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — CSF title literally matches action keyword ('triage')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| An incident-handling capability is established, covering the prevention, detection, ana... | NIS2 | excessive | - | low |

### D-04.1 · NIS2 · subso SO-D-04.1.NIS2
- **Objective**: An incident-handling capability is established, covering the prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) + Art. 6(8) six-action `incident handling` definition), with the detection dimension operationalised as all-hazards entity-level monitoring that surfaces adverse events affecting service continuity (Art. 21(2) chapeau + Recital 56).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 4 action tokens with objective
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: DE.CM-01 — literal duplicate(s) of DE.CM-01
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Entity-level all-hazards detection operating the Art. 6(8) six-action `detect` leg of ... | NIS2 | sufficient | - | low |

### D-04.1 · NIS2 · req 4.1.2
- **Title**: "Entity-level all-hazards detection operating the Art. 6(8) six-action `detect` leg of incident handling"
- **Description**: The product shall operate entity-level all-hazards monitoring covering cybersecurity, operational, and physical-environment hazards affecting network and information systems (per Art. 21(2) chapeau + Recital 56), with the `detect` action as one of the six Art. 6(8) `incident handling` actions (prevent, detect, analyse, contain, respond, recover) under Art. 21(2)(b), and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the detection depth with high-risk roles and systems triggering deeper detection coverage than low-risk ones (NIS 2 Art. 21(2)(b) + Art. 6(8) six-action definition + Art. 21(2) chapeau all-hazards + Recital 56).
- **Fit criterion (prose)**: An entity-wide monitoring capability is operated covering cybersecurity + operational + physical-environment hazards via DE.CM-01 networks-monitored leg (entity-level network telemetry, flow analytics, north-south and east-west monitoring) + DE.CM-09 host / runtime / data leg (endpoint telemetry, process-level behavioural signals, runtime-environment integrity monitoring) + DE.AE-02 adverse-event analysis leg (detection-triage threshold); the `detect` action of the six Art. 6(8) incident-handling actions is documented in the entity-level incident-response procedure (RS.MA-01 incident-management-plan-executed) with explicit coordination discipline with CSIRT, competent authority, single point of contact and sectoral peers; the detection capability produces the awareness event on which the Art. 23(4)(a) 24-hour clock trigger (4.3 cross-ref) is built; risk-tiered detection depth (high-risk roles / systems trigger deeper coverage) is documented per the Art. 21(1) `appropriate and proportionate` qualifier; the entity-level detection discipline operates at the entity boundary only, with the boundary hand-off to data-flow detection (GDPR leg), product-internal recording (CRA leg) and financial-entity multi-layer detection (DORA leg) documented as the controlled interfaces; verified by entity-level monitoring coverage audit + risk-tier mapping review + six-action incident-handling procedure inspection + adverse-event analysis records review + CSIRT / competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('audit') in objective maps to DE.AE-02
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 3 action tokens with objective
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-04.2 Incident Containment & Response

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The availability of essential and basic functions of a product with digital elements is... | CRA | excessive | - | low |

### D-04.2 · CRA · subso SO-D-04.2.CRA
- **Objective**: The availability of essential and basic functions of a product with digital elements is protected also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer minimises the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)). Where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer takes the corrective measures necessary to bring the product into conformity, or to withdraw or recall the product (Art. 13(21)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.IR-03 — literal duplicate(s) of PR.IR-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Product availability preserved after incident via resilience + DoS resistance + cross-... | CRA | sufficient | - | low |

### D-04.2 · CRA · req 4.2.3
- **Title**: "Product availability preserved after incident via resilience + DoS resistance + cross-product impact minimisation + exploitation mitigation; Art. 13(21) corrective measures on non-conformity"
- **Description**: The product shall protect the availability of essential and basic functions also after an incident, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks (Annex I Part I (2)(h)); the manufacturer shall minimise the negative impact by the product itself or connected devices on the availability of services provided by other devices or networks (Annex I Part I (2)(i)); the manufacturer shall reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k)); where the manufacturer knows or has reason to believe that the product or processes are not in conformity with the Annex I cybersecurity requirements, the manufacturer shall immediately take the corrective measures necessary to bring the product or processes into conformity, or to withdraw or recall the product (Art. 13(21) + Annex I Part I (2)(h) + (2)(i) + (2)(k)).
- **Fit criterion (prose)**: A product-design framework is maintained combining DoS resilience (Annex I Part I (2)(h)) + cross-product impact minimisation (Annex I Part I (2)(i)) + exploitation-mitigation mechanisms (Annex I Part I (2)(k)) via PR.IR-04 adequate-resource-capacity leg (DoS resilience) + PR.IR-03 network-resources-prioritised leg (cross-product impact minimisation) + DE.CM-09 computing-hardware-monitored leg (exploitation-mitigation mechanism effectiveness); the post-incident availability preservation is the design-time commitment that the essential and basic functions remain available after an incident; the exploitation-mitigation mechanisms and techniques reduce the impact of an incident when one occurs; the cascading-impact-minimisation design limits the negative impact by the product on the availability of services provided by other devices or networks; where non-conformity is identified, Art. 13(21) corrective measures are taken immediately — including conformity-restoration, withdrawal or recall; the three-clause Annex I Part I (2)(h)/(i)/(k) constellation is CRA-unique and operates at the product-design level — the containment happens inside the product boundary, pre-event design + post-incident preservation (temporally distinct from GDPR's post-event reaction); for a DORA financial entity deploying CRA products, the CRA resilience design feeds the DORA BC arrangements (4.2-DORA cross-ref); the product-design containment discipline operates at the product boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), entity-level `contain` phase (NIS 2 leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by Annex VII §2(b) + §3 + §6 + §8 design-documentation inspection (DoS resilience, cross-product impact minimisation, exploitation mitigation) + Art. 13(21) corrective-measures records review (when non-conformity occurs) + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| A comprehensive ICT business continuity policy is operationalised through dedicated, ap... | DORA | excessive | - | high |

### D-04.2 · DORA · subso SO-D-04.2.DORA
- **Objective**: A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms — including ICT response and recovery plans (subject to independent internal audit for non-microenterprises), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup based on criticality or confidentiality, and restoration and recovery procedures and methods (Art. 11(1) + Art. 11(2) + Art. 11(3) + Art. 12(1)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/DORA_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 2 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('backup') in objective maps to PR.IR-04
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title shares 2 action tokens with objective
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 2 action tokens with objective
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('backup') in objective maps to PR.IR-04
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: RC.RP-01, PR.IR-03, RC.RP-04, PR.IR-04 — literal duplicate(s) of RC.RP-01, PR.IR-03, RC.RP-04, PR.IR-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial-entity BC arrangements: dedicated, appropriate and documented response/recov... | DORA | partial | RS.MA-01 | high |

### D-04.2 · DORA · req 4.2.4
- **Title**: "Financial-entity BC arrangements: dedicated, appropriate and documented response/recovery plans + backup policies + restoration procedures; independent internal audit for non-microenterprises"
- **Description**: The product shall operate a comprehensive ICT business continuity policy operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms — including ICT response and recovery plans (subject to independent internal audit for non-microenterprises per Art. 11(3)), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup based on criticality or confidentiality (per Art. 12(1)), and restoration and recovery procedures and methods (DORA Art. 11(1) + Art. 11(2) + Art. 11(3) + Art. 12(1)).
- **Fit criterion (prose)**: A comprehensive ICT business continuity policy is established and implemented as an integral part of the overall business continuity policy of the financial entity; the BC arrangements are operationalised through a 4-way AND of artefacts per Art. 11(2) — response and recovery plans (RC.RP-01 recovery-plan-execution leg + RC.RP-04 recovery-plans-executed leg), backup policies and procedures (PR.IR-04 adequate-resource-capacity leg + PR.IR-03 network-resources-prioritised leg for criticality-based backup scope), restoration and recovery procedures and methods (RC.RP-04), and crisis-management actions; the `dedicated, appropriate and documented` qualifier from Art. 11(2) is operationalised as artefacts registered in the BC arrangements registry; for non-microenterprises, an independent internal audit of the BC arrangements (Art. 11(3)) is conducted and the audit records are inspection-ready; backup policies specify scope of data subject to backup and minimum frequency of backup based on criticality or confidentiality (Art. 12(1)); restoration and recovery procedures and methods are documented and tested; the DORA BC arrangements are the strictest containment-architecture floor in the AEGIS corpus (4-way AND of artefacts + independent internal audit for non-microenterprises); the DORA BC arrangements exceed the NIS 2 `contain` requirement for the financial-services subset of incidents; the GDPR Art. 33(3)(d) personal-data TOMs are documented as a section within the DORA BC arrangements (4.2-GDPR cross-ref), not as a separate runbook; for pure-financial entities, DORA absorbs the NIS 2 `contain` obligation for the financial-services subset via lex specialis; the BC arrangements discipline operates at the financial-entity boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), entity-level `contain` phase (NIS 2 leg) and product-design availability (CRA leg) documented as the controlled interfaces; verified by BC arrangements registry audit + Art. 11(2) 4-way AND artefact review + Art. 11(3) independent internal audit records (when non-microenterprise) + Art. 12(1) backup-policy + restoration-procedure documentation review + BC arrangements testing records inspection + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/DORA_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 4 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 4 action tokens with objective
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('backup') in objective maps to PR.IR-04
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
  - RC.RP-03 — The integrity of backups and other restoration assets is verified before using them for restoration — **CORE** — Action keyword ('recover') in objective maps to RC.RP-03
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: partial (1 potential missing anchor(s))
- **Missing (1)**: RS.MA-01 — The incident management plan is executed in coordination with relevant third parties once an incident is declared — Article maps RS.MA-01 for action keyword 'incident' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal-data breaches are contained and mitigated through appropriate technical and or... | GDPR | sufficient | - | high |

### D-04.2 · GDPR · subso SO-D-04.2.GDPR
- **Objective**: Personal-data breaches are contained and mitigated through appropriate technical and organisational measures, including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk no longer materialises (Art. 34(3)(b)); the controller describes the measures taken or proposed in the Art. 33(3)(d) supervisory-authority notification.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - RS.MI-01 — Incidents are contained — **CORE** — CSF title literally matches action keyword ('contain')
  - RS.MI-02 — Incidents are eradicated — **CORE** — Action keyword ('mitigat') in objective maps to RS.MI-02
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **UTILITY** — CSF title shares 1 token ('ensure') with objective; reinforces but is not the direct action
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data breaches contained and mitigated through TOMs incl. unintelligibility re... | GDPR | sufficient | - | high |

### D-04.2 · GDPR · req 4.2.1
- **Title**: "Personal-data breaches contained and mitigated through TOMs incl. unintelligibility rendering; Art. 33(3)(d) measures description in supervisory-authority notification"
- **Description**: The product shall contain and mitigate personal-data breaches through appropriate technical and organisational measures (TOMs), including — where applicable — measures rendering the personal data unintelligible to any person who is not authorised to access the data (Art. 34(3)(a)) and subsequent measures that ensure the high risk to data subjects' rights and freedoms no longer materialises (Art. 34(3)(b)), with the measures taken or proposed documented in the Art. 33(3)(d) supervisory-authority notification content; the `where appropriate` qualifier from Art. 33(3)(d) operationalises the TOMs depth with high-risk data categories (Art. 9 special categories, financial data, health data) triggering deeper and more aggressive containment than low-risk categories (GDPR Art. 33(3)(d) + Art. 34(3)(a)/(b) + Art. 32(1)(d)).
- **Fit criterion (prose)**: A personal-data post-breach TOMs catalogue is maintained covering containment, mitigation and remediation measures, with the measures selected per the `where appropriate` Art. 33(3)(d) qualifier and depth scaled to data-category risk (Art. 9 special categories, financial data, health data trigger deeper measures); PR.DS-01 data-at-rest protected leg anchors the cryptographic foundation (with the operational condition that the protection measures were applied to the data actually affected by the breach, not merely to data generally); PR.IR-04 adequate-resource-capacity leg anchors the resource allocation for containment; ID.AM-08 data-managed-consistent-with-risk-strategy leg anchors the unintelligibility-rendering discipline; the Art. 34(3)(a) unintelligibility rendering — operationalised as encryption with sufficient key separation that the adversary cannot recover plaintext, with the cryptographic key unavailable to any party outside the controller's authorised set — is the GDPR-unique carve-out that operates as a substitute for Art. 34 data-subject notification when applied; the Art. 34(3)(b) `subsequent measures which ensure that the high risk no longer likely to materialise` leg is the harder threshold — the controller must demonstrate that mitigation actually neutralises the high risk, not merely that mitigation was attempted; the Art. 33(3)(d) measures description in the supervisory-authority notification (4.3 cross-ref) covers both taken and proposed measures; for multi-reg parties, the GDPR TOMs are documented as a section within the NIS 2 entity-level response plan or within the DORA BC arrangements, not as a separate runbook; the personal-data post-breach containment discipline operates at the controller post-event runbook layer only, with the boundary hand-off to entity-level `contain` phase (NIS 2 leg), product-design availability (CRA leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by TOMs catalogue audit + Art. 33(3)(d) measures description in notification records review + Art. 34(3)(a) encryption-with-key-separation evidence on the affected dataset (PR.DS-01 + PR.IR-04) + Art. 34(3)(b) mitigation-effect demonstration records (when Art. 34(3)(b) is invoked) + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title literally matches action keyword ('data-at-rest')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — CSF title shares 4 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 4 action tokens with objective
  - RS.MI-01 — Incidents are contained — **CORE** — CSF title literally matches action keyword ('contain')
  - RS.MI-02 — Incidents are eradicated — **CORE** — Action keyword ('mitigat') in objective maps to RS.MI-02
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The entity operates the incident-handling capability across all six actions of the Art.... | NIS2 | sufficient | - | high |

### D-04.2 · NIS2 · subso SO-D-04.2.NIS2
- **Objective**: The entity operates the incident-handling capability across all six actions of the Art. 6(8) `incident handling` lifecycle (prevent, detect, analyse, contain, respond, recover), with the `contain` action documented in the entity-level response plan as the lifecycle phase that isolates affected systems and prevents further damage (Art. 21(2)(b)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 3 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **UTILITY** — Reinforces obligation in same CSF function (PROTECT) but does not directly match the action
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Entity-level `contain` action within the Art. 6(8) six-action incident-handling lifecy... | NIS2 | partial | RS.MA-01 | high |

### D-04.2 · NIS2 · req 4.2.2
- **Title**: "Entity-level `contain` action within the Art. 6(8) six-action incident-handling lifecycle; entity response plan as procedural wrapper"
- **Description**: The product shall operate the entity-level incident-handling capability across all six actions of the Art. 6(8) `incident handling` lifecycle (prevent, detect, analyse, contain, respond, recover), with the `contain` action documented in the entity-level response plan as the lifecycle phase that isolates affected systems and prevents further damage, and the `appropriate and proportionate` qualifier from Art. 21(1) operationalising the containment depth with high-impact incidents triggering deeper and more aggressive containment than low-impact ones (NIS 2 Art. 21(2)(b) + Art. 6(8) six-action `contain` action).
- **Fit criterion (prose)**: The entity-level response plan documents the `contain` action as one of the six Art. 6(8) incident-handling actions (prevent, detect, analyse, contain, respond, recover) with explicit isolation procedures, system-segregation runbooks, blast-radius limitation protocols, and stakeholder-coordination steps for the `contain` phase; PR.IR-03 network-resources-prioritised-based-on-importance leg anchors the isolation of high-importance resources first; PR.IR-04 adequate-resource-capacity leg anchors the resource allocation for containment; RC.RP-01 recovery-plan-execution leg anchors the contain-then-recover sequence; risk-tiered containment depth (high-impact incidents trigger deeper and more aggressive containment) is documented per the Art. 21(1) `appropriate and proportionate` qualifier; the entity-level response plan is the procedural wrapper that hosts the GDPR Art. 33(3)(d) TOMs (controller/NSIE scenario — 4.2-GDPR cross-ref) and the CRA Annex I (2)(h)/(i)/(k) product-resilience evidence (NIS 2 deployer scenario — 4.2-CRA cross-ref); for multi-reg parties, the NIS 2 response plan hosts the GDPR personal-data measures and the CRA product-resilience evidence under explicit cross-references; the entity-level containment discipline operates at the entity boundary only, with the boundary hand-off to personal-data post-breach runbook (GDPR leg), product-design availability (CRA leg) and BC arrangements (DORA leg) documented as the controlled interfaces; verified by entity-level response plan inspection + six-action `contain` phase operational records review + risk-tier containment mapping review + CSIRT / competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.2/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
  - RS.MI-01 — Incidents are contained — **CORE** — CSF title literally matches action keyword ('contain')
  - RS.MI-02 — Incidents are eradicated — **UTILITY** — CSF title shares 1 token ('incidents') with objective; reinforces but is not the direct action
- **Coverage verdict**: partial (1 potential missing anchor(s))
- **Missing (1)**: RS.MA-01 — Incident management plan executed in coordination with relevant third parties once an incident is declared — Article maps RS.MA-01 for action keyword 'incident' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-04.3 Incident Notification & Reporting

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| A serious incident involving a high-risk AI system is reported to the market surveillan... | AI_Act | sufficient | - | high |

### D-04.3 · AI_Act · subso SO-D-04.3.AI_Act
- **Objective**: A serious incident involving a high-risk AI system is reported to the market surveillance authorities of the Member States where the incident occurred under a differentiated 4-timeline × 4-trigger matrix (Art. 73(1)–(4)): 15 days after the provider becomes aware (default); 10 days if the incident results in death; 2 days for widespread infringement; 15 days from reasonable likelihood of causal link (whichever is later with the awareness trigger, per Art. 73(2)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/AI_Act_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Serious incident involving high-risk AI reported to market surveillance authorities un... | AI_Act | sufficient | - | high |

### D-04.3 · AI_Act · req 4.3.5
- **Title**: "Serious incident involving high-risk AI reported to market surveillance authorities under 4-trigger × 4-timeline matrix (15d default / 10d death / 2d widespread / 15d causal-link-anchor); GPAI systemic-risk report separately to AI Office under Art. 55"
- **Description**: The product shall report any serious incident — per the Art. 3(49) three-sub-category definition ((a) death; (b) serious harm to health; (c) serious infringement of fundamental rights) — involving a high-risk AI system to the market surveillance authorities of the Member States where the incident occurred under the differentiated 4-timeline × 4-trigger matrix of Art. 73(1)–(4): 15 days after the provider becomes aware (default, Art. 73(1)/(4)); 10 days if the incident results in death (Art. 73(2)); 2 days for widespread infringement (Art. 73(3)); 15 days from reasonable likelihood of causal link, whichever is later with the awareness trigger (Art. 73(2) causal-link-anchor); additionally, GPAI providers of systemic-risk models separately report under Art. 55 (GPAI Article 55) / `SR-AIACT-024` / `SO-AIACT-014` to the AI Office without undue delay — distinct recipient, separate clock, two recipient classes in total (MSA for high-risk AI serious incidents; AI Office for GPAI systemic-risk incidents) (AI Act Art. 3(49) sub-categories (a)/(b)/(c) + Art. 73(1)–(4) 4-trigger × 4-timeline matrix + Art. 55 GPAI).
- **Fit criterion (prose)**: An MSA-notification pipeline is operated with 4-trigger × 4-timeline matrix discipline: the default 15d timeline fires upon provider awareness (per Art. 73(1)/(4) — `15 days after the date on which the provider becomes aware`); the 10d timeline fires when the serious incident results in death (per Art. 73(2)); the 2d timeline fires when the serious incident constitutes widespread infringement (per Art. 73(3)); the causal-link-anchor 15d fires from the reasonable likelihood of causal link, whichever is later with the awareness trigger (per Art. 73(2) literal); the provider classifies the incident against the Art. 3(49) three-sub-category definition ((a) death; (b) serious harm to health; (c) serious infringement of fundamental rights) before the timeline is selected; the MSAs of the Member States where the incident occurred receive the report via the MS-determined routing channel; the report contains at minimum: a description of the incident; the category of serious incident (death / serious harm / fundamental rights infringement); the impact and consequences; the AI system's identification; the corrective measures taken; the planned follow-up; for GPAI systemic-risk models, a separate Art. 55 report to the AI Office fires without undue delay; for events overlapping with GDPR (personal data breach) / NIS 2 (significant incident) / CRA (AEV) / DORA (major ICT incident) on a single underlying event, parallel clocks run — e.g. 2d AI Act widespread + 10d AI Act death + 15d AI Act default + 24h NIS 2 early warning + 72h GDPR/NIS 2/CRA + 14d CRA AEV + 1m NIS 2 final — up to 6 distinct deadlines; the binding-procedure principle (shortest clock binds per recipient, but parallel recipients each get their own deadline) is documented in the notification playbook (Doc 07 downstream); the Art. 73 obligation is the most temporally complex notification clause in the AEGIS corpus; verified by MSA-notification logs review + Art. 3(49) sub-category classification records inspection + 4-trigger × 4-timeline matrix coverage audit + MSA-of-where-occurred routing documentation + parallel-clock binding-principle records inspection (on multi-reg overlap) + AI Office (GPAI Art. 55) notification logs review (when GPAI in scope) + AI Office + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/AI_Act_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - RS.MA-03 — Incidents are categorized and prioritized — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('incidents') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| An actively-exploited vulnerability contained in a product with digital elements that t... | CRA | sufficient | - | high |

### D-04.3 · CRA · subso SO-D-04.3.CRA
- **Objective**: An actively-exploited vulnerability contained in a product with digital elements that the manufacturer becomes aware of is notified on a three-tier temporal pattern: early warning within 24 hours (Art. 14(2)(a), `SR-CRA-029`); vulnerability notification within 72 hours with general information, nature of exploit, mitigations, and user actions (Art. 14(2)(b), `SR-CRA-030`); final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/CRA_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - RS.MA-02 — Incident reports are triaged and validated — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **CORE** — CSF title shares 2 action tokens with objective
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 2 action tokens with objective
  - RS.AN-07 — Incident data and metadata are collected, and their integrity and provenance are preserved — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Actively-exploited vulnerability notified on three-tier pattern — 24h early warning + ... | CRA | sufficient | - | low |

### D-04.3 · CRA · req 4.3.3
- **Title**: "Actively-exploited vulnerability notified on three-tier pattern — 24h early warning + 72h vulnerability notification + 14d final report — to CSIRT + ENISA, with severe-incident (SI) parallel pathway at 24h/72h/1m"
- **Description**: The product shall notify an actively-exploited vulnerability contained in a product with digital elements — that the manufacturer becomes aware of — on a three-tier temporal pattern: an early warning within 24 hours of the manufacturer becoming aware (Art. 14(2)(a), `SR-CRA-029`); a vulnerability notification within 72 hours with general information, the nature of the exploit, affected products, and available mitigations (Art. 14(2)(b), `SR-CRA-030`); and a final report within 14 days of a corrective or mitigating measure being available (Art. 14(2)(c), `SR-CRA-030`); additionally, for severe incidents per Art. 14(3)/(4) a parallel three-tier pathway applies at 24h / 72h / 1m — to the CSIRT designated under Art. 14(2) and to ENISA (CRA Annex I Part I (2)(l) + Part II (4)/(5) + Art. 13(8) + Art. 14(1)/(2)/(3)/(4) + Art. 15 coordinated vulnerability disclosure).
- **Fit criterion (prose)**: An AEV-notification pipeline is operated with dual-pathway discipline (AEV 24h/72h/14d per Art. 14(1); SI 24h/72h/1m per Art. 14(3)/(4)) — the manufacturer designates which Art. 14 leg applies per the AEV-vs-SI classification test; the 24h early-warning tier for AEV fires upon manufacturer awareness of an actively-exploited vulnerability; the 72h vulnerability-notification tier provides the structured content (general information, nature of exploit, affected products, available mitigations, user-actions advice); the 14d final-report tier closes with the corrective/mitigating measure being available (which may be earlier than 14d); for SI the parallel 24h/72h/1m pathway applies; the manufacturer notifies the CSIRT designated under Art. 14(2) and ENISA, with the Art. 15 CVD process enabling coordinated disclosure; the manufacturer documents the personal-data-subset awareness moment feeding GDPR `becoming aware` when the CRA-manufacturer is also a controller (integrated-stack); the product-internal recording from 4.1 CRA leg feeds the AEV-detection trigger; the Art. 14(3)/(4) SI pathway `unlawful OR malicious acts` (R2 distinct terms) preserves both reporting categories independently; the CVD process (Art. 15) coordinates with MSA/CSIRT/ENISA but does not replace the Art. 14 24h/72h/14d tier; verified by AEV-notification logs review + 24h + 72h + 14d clock-anchor records inspection + progressive-disclosure content-template coverage audit (3 tiers) + AEV-vs-SI classification-test documentation + Art. 15 CVD process discipline review + ENISA + CSIRT inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/AI_Act_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 2 action tokens with objective
  - RS.AN-07 — Incident data and metadata are collected, and their integrity and provenance are preserved — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **CORE** — CSF title shares 3 action tokens with objective
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — Action keyword ('incidents') in objective maps to RS.MA-02
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| A major ICT-related incident is reported to the relevant competent authority without un... | DORA | sufficient | - | high |

### D-04.3 · DORA · subso SO-D-04.3.DORA
- **Objective**: A major ICT-related incident is reported to the relevant competent authority without undue delay (Art. 19(1)); affected clients are separately informed without undue delay as soon as the financial entity becomes aware of the major ICT-related incident (Art. 19(3)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Major ICT-related incident reported to competent authority `without undue delay`; affe... | DORA | sufficient | - | high |

### D-04.3 · DORA · req 4.3.4
- **Title**: "Major ICT-related incident reported to competent authority `without undue delay`; affected clients informed `without undue delay` as soon as financial entity becomes aware — pending EBA/ESMA/EIOPA RTS (4h pending)"
- **Description**: The product shall report a major ICT-related incident — classified per Art. 18 criteria — to the relevant competent authority without undue delay (Art. 19(1)) and shall separately inform affected clients without undue delay as soon as the financial entity becomes aware of the major ICT-related incident (Art. 19(3)); the temporal anchor is delegated to the EBA / ESMA / EIOPA Regulatory Technical Standards under Art. 18(3) and partially addressed in Implementing Regulation (EU) 2024/2956 (pending 4h preliminary RTS) — for DORA + GDPR overlap the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle (DORA Art. 19(1) + Art. 19(3) + Art. 18(3) RTS delegation + IR (EU) 2024/2956 + Art. 17(1) incident management process).
- **Fit criterion (prose)**: A DORA CA-notification pipeline is operated with parallel CA + client tracks: the CA notification (Art. 19(1)) fires per the EBA/ESMA/EIOPA RTS under Art. 18(3) (Implementing Regulation (EU) 2024/2956 pending 4h preliminary-classification tier; substantive thresholds + content template per RTS when published) — the L1-level preliminary classification within 4h of awareness, the L2 intermediate notification with root cause + recovery actions, and the L3 final notification with full detail once the incident is closed; the affected-client notification (Art. 19(3)) fires without undue delay AS SOON AS the financial entity becomes aware (the literal DORA temporal anchor on the client side), with the OJ-corrective note per `SR-DORA-017` v0.2 audit applying only when the incident has financial-interest impact on clients (where the OJ-corrective note does not reduce the `without undue delay AS SOON AS` trigger to a `where-and-when` construction); the financial entity must document the major-incident classification (Art. 18 + RTS criteria) and the parallel track distinction; the DORA `without undue delay` clock is shorter than GDPR 72h in practice on the CA-notification side once RTS-level granularity is published; for DORA + GDPR overlap on the same event, the parallel GDPR 72h notification under Art. 33 binds via the binding-procedure principle (the `where feasible` GDPR softening does not survive the DORA multi-reg overlap per CRDA-deep GDPR↔DORA CONDITIONAL-CONTRADICTORY); the DORA Art. 17(1) ICT-related incident management process is the upstream prerequisite (defined, established, implemented — SR-DORA-017 inherits from SR-DORA-016); verified by Art. 18 major-incident classification records inspection + DORA CA-notification logs review + RTS-tier clock-anchor records inspection (4h pending RTS) + DORA client-notification logs review + parallel-track discipline documentation + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A personal data breach is notified to the competent supervisory authority without undue... | GDPR | sufficient | - | high |

### D-04.3 · GDPR · subso SO-D-04.3.GDPR
- **Objective**: A personal data breach is notified to the competent supervisory authority without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms (Art. 33(1)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data breach notified to supervisory authority within 72 hours `where feasible... | GDPR | sufficient | - | high |

### D-04.3 · GDPR · req 4.3.1
- **Title**: "Personal-data breach notified to supervisory authority within 72 hours `where feasible` of becoming aware, with `unlikely risk` carve-out documented"
- **Description**: The product shall notify the competent supervisory authority of a personal data breach without undue delay and, where feasible, no later than 72 hours after the controller becomes aware of the breach — unless the breach is unlikely to result in a risk to data subjects' rights and freedoms — at which point the Art. 33(3) Nature/Categories/Approximate-numbers/Consequences/Measures content template is filed (GDPR Art. 33(1) + Art. 33(3) + Art. 4(12) breach definition; the `where feasible` softening is GDPR-unique among the 4.3 regulators).
- **Fit criterion (prose)**: A DPA-notification pipeline is operated with documented breach-classification discipline (controller designates whether breach is `unlikely to result in a risk`, `may result in a risk`, or `likely to result in a high risk` per EDPB Guidelines 9/2022 §3.5), 72h clock-start anchored at the 4.1 GDPR leg's `becoming aware` moment (parallel-clock binding principle); the Art. 33(3) content template (Nature / Categories of data subjects and records / Approximate numbers / Likely consequences / Measures taken or proposed / DPO contact) is filed via the MS-determined DPA entry-point channel within 72h `where feasible`, with phased notification allowed only when full information is not simultaneously available; the `unless unlikely to result in a risk` carve-out is documented as a GDPR-unique condition (does not survive multi-reg overlap with NIS 2 — NIS 2 `in any event` ceiling binds); for events that may result in a high risk to rights and freedoms, the Art. 34 data-subject communication obligation is cascaded separately (4.3 GDPR + 4.2 GDPR Unintelligibility carve-out is 4.2 territory, not 4.3); verified by DPA-notification logs review + 72h clock-anchor records inspection + Art. 33(3) content-template coverage audit + `where feasible` softening documentation + `unlikely risk` carve-out-justification records (where invoked) + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/GDPR_Art_32.md` (Art. 32) — paraphrased action
- **Anchors listed**:
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| A significant incident is notified to the CSIRT or, where applicable, the competent aut... | NIS2 | sufficient | - | high |

### D-04.3 · NIS2 · subso SO-D-04.3.NIS2
- **Objective**: A significant incident is notified to the CSIRT or, where applicable, the competent authority via a twin-trigger pattern — an early warning within 24 hours of awareness (Art. 23(4)(a), `SR-NIS2-010`) followed by an incident notification within 72 hours with severity, impact, and (where available) indicators of compromise (Art. 23(4)(b), `SR-NIS2-011`).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/NIS2_Art_23.md` (Art. 23) — paraphrased action
- **Anchors listed**:
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Significant incident notified via twin-trigger pattern — 24h early warning + 72h incid... | NIS2 | sufficient | - | high |

### D-04.3 · NIS2 · req 4.3.2
- **Title**: "Significant incident notified via twin-trigger pattern — 24h early warning + 72h incident notification + 1m final report — to CSIRT or competent authority"
- **Description**: The product shall notify significant incidents — per Art. 23(3) tests A or B — to the CSIRT or, where applicable, the competent authority via the twin-trigger pattern: an early warning within 24 hours of becoming aware of the significant incident (Art. 23(4)(a), `SR-NIS2-010`), an incident notification within 72 hours of becoming aware with severity, impact, and (where available) indicators of compromise (Art. 23(4)(b), `SR-NIS2-011`), and a final report no later than one month after the incident notification (Art. 23(4)(c), `SR-NIS2-012`), with the `in any event` ceiling ensuring no softening (NIS 2 Art. 21(2)(b) chapeau + Art. 23(4) + Art. 23(3) + Art. 6(8) six-action definition).
- **Fit criterion (prose)**: A CSIRT-notification pipeline is operated with 3-tier temporal discipline: 24h early warning clock-started from 4.1 NIS 2 leg's awareness event (Art. 23(4)(a) — `without undue delay and in any event within 24 hours`), 72h incident notification with severity/impact/IoC content (Art. 23(4)(b) — `in any event within 72 hours`), and 1m final report (Art. 23(4)(c) — 30 days after incident notification, the standard reading per Recital 56); the `in any event` ceiling is documented as the NIS 2-unique binding rule that overrides the GDPR `where feasible` softening on multi-reg overlap; the Art. 23(3) significant-incident tests (test A — service-disruption severity 5+ qualified impacts; test B — significant impact on continuity of essential services) gate the obligation; the 24h early-warning tier fires upon substantive awareness even before full triage; the 72h notification tier provides the assessment (severity, impact, IoCs) and updates the 24h tier; the final report tier closes the lifecycle with detailed forensic/post-incident content; for eIDAS QTSPs the derogation to 24h applies (Art. 23(4) ¶2 — `SR-NIS2-013`); for critical-infrastructure digital-infrastructure categories the Art. 23(11) implementing-acts may add granularity (4.3 Generic); verified by CSIRT-notification logs review + 24h clock-anchor records inspection + 72h clock-anchor records inspection + 1m clock-anchor records inspection + severity/impact/IoC content-template coverage audit + Art. 23(3) significant-incident tests documentation + on-demand intermediate-report records (when CA requests Art. 23(4)(b) `SR-NIS2-014`) + CSIRT / competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.3/articles/NIS2_Art_23.md` (Art. 23) — paraphrased action
- **Anchors listed**:
  - RS.MA-02 — Incident reports are triaged and validated — **CORE** — CSF title literally matches action keyword ('triage')
  - RS.MA-03 — Incidents are categorized and prioritized — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('incidents') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-04.4 Incident Recovery & Lessons Learned

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The availability of essential and basic functions of a product with digital elements is... | CRA | excessive | - | low |

### D-04.4 · CRA · subso SO-D-04.4.CRA
- **Objective**: The availability of essential and basic functions of a product with digital elements is protected *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, and the manufacturer reduces the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques and minimises the negative impact on services of other devices and networks (Annex I Part I (2)(h) + (2)(k) + (2)(i) + Art. 13(21) corrective measures).
- **Anchors listed**:
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.IR-03, ID.AM-08 — literal duplicate(s) of PR.IR-03, ID.AM-08
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Product with digital elements preserves essential and basic functions `also after an i... | CRA | sufficient | - | low |

### D-04.4 · CRA · req 4.4.3
- **Title**: "Product with digital elements preserves essential and basic functions `also after an incident` through resilience and exploitation-mitigation architecture (intra-product recovery, layered not substituted)"
- **Description**: The product with digital elements shall preserve the availability of essential and basic functions *also after an incident*, through resilience and mitigation measures including resistance to and recovery from denial-of-service attacks, with the manufacturer reducing the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (binary + runtime layers — rate-limiting, ASLR/DEP, control-flow integrity, configuration hardening) and minimising the negative impact on services of other devices and networks (cross-product impact containment) (CRA Annex I Part I (2)(h) `also after an incident` + (2)(k) exploitation-mitigation + (2)(i) cross-product impact minimisation + Art. 13(21) corrective measures; the Annex I (2)(h) anchor is design-time and runtime — resilience must be in place before the incident, not bolted on after).
- **Fit criterion (prose)**: An intra-product resilience architecture is engineered pre-incident so that essential and basic functions survive an attack (Annex I Part I (2)(h) `also after an incident`) — the resilience mechanism is in place before the incident, not bolted on after; an exploitation-mitigation mechanism operates at the binary layer + runtime layer — rate-limiting, ASLR/DEP, control-flow integrity (CFI), configuration hardening, sandboxing, secure enclaves, principle of least privilege at process level — via ID.AM-08 data-management-discipline substrate (Annex I Part I (2)(k)); cross-product impact containment minimises the negative impact on services of other devices or networks via Annex I Part I (2)(i) cross-boundary responsibility (the (2)(i) CRA-unique reading); the (2)(h)+(2)(k)+(2)(i) triad is risk-calibrated via the Art. 13(2) risk assessment; the Annex VII §2 technical-documentation evidence demonstrates the resilience architecture (general description §1 + design / vuln-handling processes §2 + SBOM §2 + risk-assessment §3); the Annex VII §6 test-reports demonstrate verification of conformity with Annex I Part I and Part II cybersecurity requirements (including the post-incident-availability obligation of (2)(h)); the product-internal resilience feeds the deployer's entity-level (NIS 2) and financial-entity (DORA) BC frameworks via deployment (CRA products reduce the load on the entity's BC framework by continuing to function during/after attack); for an integrated manufacturer-controller (manufacturer is also controller), the CRA product-internal resilience feeds the controller-side recovery-evidence base via Annex VII technical documentation; the CRA product-internal resilience does NOT replace the deployer's entity-level BC framework for cases where the product itself fails or the attack propagates beyond the product boundary (CRA is a layered-not-substituted caveat — structurally different from 4.1 where CRA `verifiable manner` is the strictest knowledge-test floor; here, CRA is a layered prevention/mitigation); verified by Annex I (2)(h) resilience architecture review + (2)(k) exploitation-mitigation evidence inspection + (2)(i) cross-product impact-containment evidence review + Annex VII §2 technical-documentation review + Annex VII §6 test-reports review (including post-incident-availability verification) + Art. 13(2) risk-calibration documentation + MSA reasoned-request inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| A comprehensive ICT business continuity policy is operationalised through dedicated, ap... | DORA | sufficient | PR.IR-04 | high |

### D-04.4 · DORA · subso SO-D-04.4.DORA
- **Objective**: A comprehensive ICT business continuity policy is operationalised through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms, including ICT response and recovery plans (subject to independent internal audit review for non-microenterprises, Art. 11(3)), backup policies and procedures specifying the scope of the data subject to backup and the minimum frequency of the backup, based on the criticality of information or the confidentiality level of the data (Art. 12(1)(a)), and restoration and recovery procedures and methods (Art. 12(1)(b)).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (1)**: PR.IR-04 — Adequate resource capacity to ensure availability is maintained — Article maps PR.IR-04 for action keyword 'backup' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Comprehensive ICT BC policy with dedicated appropriate documented arrangements + respo... | DORA | sufficient | - | high |

### D-04.4 · DORA · req 4.4.4
- **Title**: "Comprehensive ICT BC policy with dedicated appropriate documented arrangements + response/recovery plans + backup-scoping on criticality/confidentiality + restoration procedures; OJ-corrected Art. 11(2)(a)–(e) BC-policy objectives preserved verbatim"
- **Description**: The product shall operationalise a comprehensive ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms (Art. 11(2) 3-way AND of adjectives + 4-way AND of artefact types = `arrangements, plans, procedures, mechanisms`), including ICT response and recovery plans (Art. 11(3); subject to independent internal audit review for non-microenterprises), backup policies and procedures specifying the scope of data subject to backup and the minimum frequency of backup, based on the criticality of information or the confidentiality level of the data (Art. 12(1)(a) — `criticality or confidentiality` basis), and restoration and recovery procedures and methods (Art. 12(1)(b)) (DORA Art. 11(1)–(3) + Art. 12(1); the OJ-corrected Art. 11(2)(a)–(e) objective list per `SR-DORA-014` v0.2 audit applies — (a) continuity of critical or important functions; (b) quick+appropriate+effective response/resolution; (c) without-delay activation of dedicated plans with containment measures; (d) preliminary impact/damage/loss estimation; (e) communication + crisis-management per Art. 14 + CA reporting per Art. 19).
- **Fit criterion (prose)**: A comprehensive ICT BC framework is operated at the financial-entity ICT-infrastructure layer with the DORA `dedicated, appropriate and documented` 3-way AND + `arrangements + plans + procedures + mechanisms` 4-way AND + Art. 11(3) independent internal audit on non-microenterprises as the audit-verification floor; the Art. 11(2)(a)–(e) objective list is implemented with the OJ-corrected labels — (a) ensure the continuity of the financial entity's critical or important functions (continuity-of-critical-functions / operational continuity); (b) quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions (response-and-resolution / rapid incident handling); (c) activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident (plan-activation / without-delay containment per type of incident); (d) estimate preliminary impacts, damages and losses (impact-and-loss-estimation / preliminary, near-real-time); (e) set out communication and crisis management actions that ensure that updated information is transmitted to all relevant internal staff and external stakeholders in accordance with Article 14, and report to the competent authorities in accordance with Article 19 (communication-and-CA-reporting / per Art. 14 + Art. 19); a BC policy specifies the criteria under which recovery transitions from incident-response to recovery-mode (RC.RP-01); the documented arrangements/plans/procedures/mechanisms (4-way AND) operationalise the five-objective Art. 11(2)(a)–(e) list into concrete recovery capability (RC.RP-04); resource-capacity substrate (PR.IR-04 redundant compute + storage + network + alternative-site capacity); backup policies and procedures (Art. 12(1)(a)) specify the scope of data subject to backup and the minimum frequency, calibrated to the `criticality of information or the confidentiality level of the data` VAG with tiered backup cadences per `SR-DORA-015` — Tier 1 critical trading books synchronously replicated; Tier 2 settlement data at high cadence; Tier 3 reporting data at standard cadence; restoration and recovery procedures and methods (Art. 12(1)(b)) specify how restored data is operationalised into running services (RC.RP-04 service-restoration) with integrity verification before restoration (RC.RP-03 restore-confidence per Recital 57's testing-not-merely-writing principle); on GDPR + DORA parties, the DORA Art. 12(1)(a) backup-tiering on criticality/confidentiality + Art. 12(1)(b) restoration procedures + Art. 11(3) independent internal audit for non-microenterprises supply the measurable implementation of the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) for the personal-data subset; on NIS 2 + DORA parties (cross-sector or pure-financial via lex specialis), the DORA BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset, with the NIS 2 all-hazards chapeau extending beyond ICT (operational + physical-environment hazards); the DORA BC framework does NOT make DORA co-extensive with NIS 2 — the financial-sector overlay is material (response and recovery plans as distinct artefacts; risk-calibrated backup scoping; audit-verified BC arrangements); verified by Art. 11(1) BC policy review + Art. 11(2) arrangements + plans + procedures + mechanisms (4-way AND) arrangements registry audit + Art. 11(3) response-and-recovery-plans documentation + independent internal audit review records on non-microenterprises + Art. 12(1)(a) backup-scoping records on criticality/confidentiality + tiered-backup-cadence evidence + Art. 12(1)(b) restoration procedures inspection + Art. 11(2)(a)–(e) OJ-corrected objective-mapping documentation review + national-CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/DORA_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 3 action tokens with objective
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('backup') in objective maps to PR.IR-04
  - RC.RP-01 — The recovery portion of the incident response plan is executed once initiated from the incident response process — **CORE** — CSF title literally matches action keyword ('recover')
  - RC.RP-03 — The integrity of backups and other restoration assets is verified before using them for restoration — **CORE** — Action keyword ('recover') in objective maps to RC.RP-03
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The ability to ensure the ongoing confidentiality, integrity, availability and resilien... | GDPR | excessive | - | high |

### D-04.4 · GDPR · subso SO-D-04.4.GDPR
- **Objective**: The ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services is maintained, and to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(b) + Art. 32(1)(c); Art. 5(1)(f) integrity/confidentiality cross-reference; Art. 32(2) five-event risk-enumeration cross).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 3 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 3 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.IR-04, PR.DS-11, RC.RP-04 — literal duplicate(s) of PR.IR-04, PR.DS-11, RC.RP-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal data availability and access restored in `timely manner` after physical or te... | GDPR | sufficient | - | high |

### D-04.4 · GDPR · req 4.4.1
- **Title**: "Personal data availability and access restored in `timely manner` after physical or technical incident, with tested recovery-exercise evidence discharging Art. 5(2) accountability"
- **Description**: The product shall ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (Art. 32(1)(b)) and shall restore the availability of and access to personal data in a timely manner in the event of a physical or technical incident (Art. 32(1)(c)), with the recovery evidence produced by tested recovery exercises (PR.IR-04 adequate resource capacity + PR.DS-11 backup creation + protection + maintenance + testing + RC.RP-04 critical mission functions restored) supplying the Art. 5(2) accountability evidence the supervisory authority may inspect under Art. 58 (GDPR Art. 32(1)(b) + Art. 32(1)(c) + Art. 5(1)(f) integrity/confidentiality cross-reference + Art. 32(2) five-event risk-enumeration cross; `timely manner` VAG anchor resolved by per-reg operationalising framework — NIS 2 BC framework cadence for NIS 2 + GDPR parties; DORA Art. 12 backup-tiering for DORA + GDPR parties; per-activity RTO/RPO for GDPR-only parties).
- **Fit criterion (prose)**: A tested-recovery-exercise capability is operated with documented per-processing-activity RTO/RPO targets under PR.IR-04 adequate-resource-capacity substrate (resource headroom to absorb incident and recover availability within the documented RTO) + PR.DS-11 backup-discipline substrate (backups created on defined cadence, integrity-protected, maintained across technology lifecycle, tested for restorability on a defensible schedule with ransomware-resistant retention and offsite replication with RPO alignment) + RC.RP-04 recovery-execution substrate (tested recovery plan with documented RTO/RPO per activity, critical-mission-function restoration discipline, restore-confidence integrity verification before restoration); the five-event risk-enumeration cross (Art. 32(2)) anchors the trigger assessment — accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data — and the recovery exercise demonstrates that each risk class can be remediated within the documented RTO/RPO; the Art. 32 documentation expectations provide the supervisory-authority evidence base (Art. 58 inspection); the BC framework documentation + recovery-exercise records + backup-test results are the audit-grade artefacts; for GDPR-only parties (no NIS 2 / DORA applicability), the controller documents `timely manner` via tested per-activity RTO/RPO targets; for NIS 2 + GDPR parties, the NIS 2 BC framework cadence (BC plan + backup records + DR tests + CM records) operationalises the GDPR `timely` VAG anchor with tested recovery evidence for the personal-data subset; for DORA + GDPR parties, the DORA Art. 12(1)(a) backup-scoping on criticality/confidentiality + Art. 12(1)(b) restoration/recovery procedures + Art. 11(3) independent internal audit on non-microenterprises supply the measurable implementation; verified by per-processing-activity RTO/RPO documentation review + PR.DS-11 backup-test results inspection + RC.RP-04 recovery-exercise records audit + Art. 32 documentation-records review + Art. 5(2) accountability evidence pack + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 7 action tokens with objective
  - PR.IR-04 — Adequate resource capacity to ensure availability is maintained — **CORE** — Action keyword ('resilien') in objective maps to PR.IR-04
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Business continuity, backup management, disaster recovery, and crisis management capabi... | NIS2 | excessive | - | high |

### D-04.4 · NIS2 · subso SO-D-04.4.NIS2
- **Objective**: Business continuity, backup management, disaster recovery, and crisis management capabilities are maintained, ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents (Art. 21(2)(c); the `business continuity, such as backup management and disaster recovery, and crisis management` structure imposes an AND chain across the BC + backup + DR + CM triad).
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 3 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: RC.RP-04, PR.DS-11 — literal duplicate(s) of RC.RP-04, PR.DS-11
- **Confidence**: high (article mapping and CSF title both consulted)

| "Entity-level business continuity, backup management, disaster recovery, and crisis man... | NIS2 | sufficient | - | high |

### D-04.4 · NIS2 · req 4.4.2
- **Title**: "Entity-level business continuity, backup management, disaster recovery, and crisis management triad maintained with all-hazards scope and risk-tiered depth"
- **Description**: The product shall maintain business continuity, backup management, disaster recovery, and crisis management capabilities — ensuring the ability to restore the availability and integrity of network and information systems and to manage crises arising from significant incidents — under the `appropriate and proportionate` qualifier (Art. 21(1)) with the all-hazards chapeau (Art. 21(2) + Recital 56) extending the recovery envelope to operational + physical-environment + cyber hazards, and the BC + backup + DR + CM triad documented in BC plan + backup records + DR test results + CM records (NIS 2 Art. 21(2)(c) + Art. 21(1) `appropriate and proportionate` + all-hazards chapeau + Recital 56; the `such as backup management and disaster recovery, and crisis management` structure imposes an AND chain across the four pillars).
- **Fit criterion (prose)**: An entity-level BC framework is maintained with the four-pillar BC + backup + DR + CM triad as the operational vehicle; a tested BC plan is produced documenting scenarios (operational + physical-environment + cyber hazards per Recital 56 all-hazards); backup records demonstrate PR.DS-11 backup creation (defined cadence), protection (encryption-at-rest + immutable storage + ransomware-resistant retention + offsite replication with RPO alignment), maintenance across the technology lifecycle, and tested restorability on a defensible schedule; DR test results demonstrate RC.RP-04 critical-mission-function restoration with documented RTO/RPO per activity calibrated to the Art. 21(1) `appropriate and proportionate` analysis; CM records demonstrate crisis-management discipline for incidents beyond ICT (operational + physical-environment hazards); high-risk roles / systems trigger deeper recovery depth per risk-tier mapping; the BC framework cadence operationalises the GDPR `timely manner` VAG anchor (Art. 32(1)(c)) on non-financial parties — the tested recovery-exercise records are the measurable implementation; on DORA + NIS 2 parties, the DORA Art. 11–12 BC framework absorbs the NIS 2 BC/DR/CM obligation for the ICT subset (DORA is lex specialis on pure-financial entities) but the NIS 2 all-hazards chapeau extends beyond ICT (operational + physical-environment hazards), with the high-level SO not aggregating across the lex-specialis boundary in the ICT-hazard direction; on CRA + NIS 2 parties, CRA Annex I Part I (2)(h) product-internal resilience reduces the load on the NIS 2 entity-level BC framework via deployment (the product continues to function during/after attack); ISO 22301 (BCMS) and ISO 22361 (crisis management) are recognised methodological anchors cross-referenced in the `SR-NIS2-019` `regulatory_rationale`; verified by BC plan + backup records + DR test results + CM records review + Art. 21(1) `appropriate and proportionate` calibration documentation + all-hazards scenario coverage audit + risk-tier mapping review + MS competent-authority / CSIRT inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-04_Incident-Response/D-04.4/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 4 action tokens with objective
  - RC.RP-04 — Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-05.1 Data Minimisation

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems which make use of techniques involving the training of AI models w... | AI_Act | sufficient | - | high |

### D-05.1 · AI_Act · subso SO-D-05.1.AIACT
- **Objective**: High-risk AI systems which make use of techniques involving the training of AI models with data are developed on the basis of training, validation and testing data sets that meet the quality criteria — relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose (Art. 10(3)) — supported by data governance practices that detect, prevent and mitigate possible biases (Art. 10(1) + Art. 10(2) 8-element closed list (a)–(h)).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "High-risk AI training/validation/testing datasets meet Art. 10(3) quality criteria and... | AI_Act | sufficient | - | high |

### D-05.1 · AI_Act · req 5.1.3
- **Title**: "High-risk AI training/validation/testing datasets meet Art. 10(3) quality criteria and Art. 10(2) 8-element data-governance practice; Art. 10(5) special-category 6-cumulative-condition gateway documented when applicable"
- **Description**: The product shall develop high-risk AI systems on the basis of training, validation and testing data sets that meet the quality criteria of being relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose (Art. 10(3)), supported by data governance practices that detect, prevent and mitigate possible biases per the Art. 10(2) 8-element closed list (a)–(h); exceptional special-category processing for bias detection and correction is permitted only when all 6 cumulative Art. 10(5) conditions (a)–(f) are satisfied (Art. 10(1) + Art. 10(2) + Art. 10(3) + Art. 10(5)).
- **Fit criterion (prose)**: A provider-side training-pipeline data-governance architecture is operated under ID.AM-03 datasets and corresponding metadata inventory (data sources through preparation operations to deployed model, with bias-detection (f) and bias-detection/prevention/mitigation (g) records) + ID.AM-08 data managed consistent with the provider's risk strategy (the upstream control that (f) and (g) operationalise) + PR.PS-06 secure software development practices integrated (the secure engineering pipeline into which data-collection, preparation and bias-mitigation practices are embedded) + PR.DS-01 data-at-rest CIA protected (the pseudonymisation, differential-privacy and federated-learning techniques that constitute the state-of-the-art privacy-preserving measures referenced by the Art. 10(5) safeguards clause) + GV.OC-03 legal/regulatory/contractual requirements regarding cybersecurity understood and managed (the legal-and-regulatory understanding substrate that the cross-regulation GDPR Art. 9 interaction requires); the Art. 10(2) 8-element closed list (a)–(h) is AND-coordinated so partial compliance with six of eight does not satisfy Art. 10; the Art. 10(3) 4-criterion quality benchmark (relevant, sufficiently representative, free of errors, complete) is verified per dataset; when special-category personal data is processed for bias detection and correction, the Art. 10(5) 6-cumulative-condition gateway is documented: (a) bias detection and correction cannot be effectively achieved by processing other data, (b) special categories are strictly necessary and limited to the bias detection and correction, (c) effective technical and organisational safeguards in place, (d) datasets subject to enhanced data governance, (e) safeguards documented, (f) special-category data deleted after the bias detection and correction; `biases` is read cumulatively across statistical / algorithmic / societal senses; outside the narrow Art. 10(5) window, the AI Act does not trigger special-categor... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 10 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 6 action tokens with objective
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title literally matches action keyword ('data-at-rest')
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 8 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Data processed by a product with digital elements — personal or other — is limited to w... | CRA | excessive | - | high |

### D-05.1 · CRA · subso SO-D-05.1.CRA
- **Objective**: Data processed by a product with digital elements — personal or other — is limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.AM-08, ID.AM-03 — literal duplicate(s) of ID.AM-08, ID.AM-03
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product data limited to what is adequate, relevant, and necessary in relation to the i... | CRA | sufficient | - | high |

### D-05.1 · CRA · req 5.1.2
- **Title**: "Product data limited to what is adequate, relevant, and necessary in relation to the intended purpose of the product, with risk-assessment proportionality calibration"
- **Description**: The product shall limit data processed by a product with digital elements — personal or other — to what is adequate, relevant, and necessary in relation to the intended purpose of the product (Art. 3(23) `intended purpose` definition), with the risk assessment per Art. 13(2) and the intended purpose + reasonably foreseeable use per Art. 13(3) sentence 2 supplying the proportionality calibration (Annex I Part I (2)(g)).
- **Fit criterion (prose)**: A manufacturer-side product-data minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory per product variant with intended-purpose tag) + ID.AM-08 data managed consistent with the manufacturer's risk strategy (Art. 13(2) risk assessment supplies the proportionality bar); the Annex I Part I (2)(g) `adequate, relevant and limited to what is necessary in relation to the intended purpose of the product` test is applied to every data-collection surface at design-time and re-calibrated on any product change; the Art. 3(23) intended purpose is documented in the technical documentation under Annex VII §2 and the risk assessment under Annex VII §3 calibrates which data classes are adequate/relevant/necessary for that purpose; for an integrated-stack manufacturer-controller (the same party is both manufacturer and controller), the manufacturer-controller documents the Art. 6(4) compatibility assessment separately from the CRA-side design-time minimisation; the CRA-side minimisation does NOT require the Art. 6(4) compatibility test on change of purpose (that is the GDPR-side controller's residual obligation); CRA-side coverage of training data is sequential not concurrent with AI Act Art. 10 — CRA Annex I Part I (2)(g) operates at runtime on product data, AI Act Art. 10 operates upstream on the training pipeline; verified by Annex VII §2 technical-documentation inspection + Annex VII §3 risk-assessment record review + per-data-class intended-purpose mapping audit + Annex I Part I (2)(g) minimisation test per data-class review + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal data collected and processed are limited to what is adequate, relevant, and ne... | GDPR | sufficient | - | high |

### D-05.1 · GDPR · subso SO-D-05.1.GDPR
- **Objective**: Personal data collected and processed are limited to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing is compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing.
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Personal data limited to what is adequate, relevant, and necessary for the processing ... | GDPR | sufficient | - | low |

### D-05.1 · GDPR · req 5.1.1
- **Title**: "Personal data limited to what is adequate, relevant, and necessary for the processing purpose, with Art. 6(4) compatibility assessment on change of purpose and Art. 9(1) special-category prohibition honoured"
- **Description**: The product shall limit personal data collected and processed to what is adequate, relevant, and necessary in relation to the purposes for which they are processed (Art. 5(1)(c)); further processing shall be compatible with the original purposes per the Art. 6(4) compatibility test (5 factors); special-category processing requires an Art. 9(2) basis subject to the Art. 9(1) prohibition; by-design and by-default minimisation is applied per Art. 25(1)/(2); a DPIA under Art. 35 is performed for high-risk processing.
- **Fit criterion (prose)**: A controller-side personal-data-minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory with declared purpose, lawful basis, and envisaged erasure time per data category) + ID.AM-08 data managed consistent with the controller's risk strategy (per-purpose collection limits + retention schedules); the Art. 5(1)(c) `adequate, relevant, limited to what is necessary` test is applied to every data-collection surface and documented in a necessity assessment per data class; an Art. 6(4) 5-factor compatibility assessment (a) purpose link, (b) context of collection, (c) nature of personal data, (d) possible consequences for the data subject, (e) existence of appropriate safeguards is performed and documented on every change of purpose and is NOT absorbed by the CRA-side design-time minimisation when both apply on the same integrated-stack manufacturer-controller; Art. 9(1) special-category prohibition is enforced absent an Art. 9(2) basis (including the substantial public interest Art. 9(2)(g) where applicable) OR the AI Act Art. 10(5) 6-cumulative-condition gateway (when high-risk AI bias correction applies); Art. 25(1) by-design minimisation integrates the necessity test at the time of means-determination; Art. 25(2) by-default minimisation ensures only data necessary for each specific purpose are processed by default; Art. 35(7) DPIA content items are present for any high-risk processing; Art. 30(1)(f) RoPA envisages-time-limits-for-erasure are documented per category; Art. 5(2) accountability evidence is inspection-ready; verified by data-inventory audit + per-class necessity-assessment review + Art. 6(4) compatibility-assessment records inspection + Art. 9(1) prohibition-enforcement audit + Art. 25 by-design and by-default documentation review + DPIA records inspection (for high-risk processing) + Art. 30(1)(f) RoPA time-limits review + DPA inspection-ready evidence pack on re... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 4 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-05.2 Retention & Archiving

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Providers of high-risk AI systems keep the logs referred to in Art. 12(1) — automatical... | AI_Act | sufficient | - | high |

### D-05.2 · AI_Act · subso SO-D-05.2.AIACT
- **Objective**: Providers of high-risk AI systems keep the logs referred to in Art. 12(1) — automatically generated by their high-risk AI systems and to the extent such logs are under their control — for a period appropriate to the intended purpose, of at least six months, unless provided otherwise in the applicable Union or national law, in particular Union law on the protection of personal data (Art. 19(1)).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "High-risk AI system logs retained ≥6 months per Art. 19(1); upward adjustment justifie... | AI_Act | sufficient | - | high |

### D-05.2 · AI_Act · req 5.2.3
- **Title**: "High-risk AI system logs retained ≥6 months per Art. 19(1); upward adjustment justified by intended purpose; floor-within-ceiling layering with GDPR when logs contain personal data"
- **Description**: The product shall keep the logs referred to in Art. 12(1) — automatically generated by the high-risk AI systems and to the extent such logs are under the provider's control — for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular Union law on the protection of personal data (Art. 19(1)).
- **Fit criterion (prose)**: A provider-side high-risk AI log-retention architecture is operated under PR.PS-04 log-records-generated and retained (the log-generation substrate that the 6-month retention floor requires — without continuous log generation per Art. 12(1) `over the lifetime` VAG aligned with the product-lifecycle definition in Art. 3(1)(c), the retention duty is vacuous and the post-market monitoring and incident-investigation flows have no reconstructable trail) + GV.PO-02 cybersecurity policies and procedures established (the policy substrate that the upward adjustment clause `appropriate to the intended purpose` requires — retention duration beyond the 6-month floor is justified by the system's risk class and documented in the provider's cybersecurity policies and procedures); the Art. 19(1) ≥6-month floor is enforced for every high-risk AI log (the `events (logs)` POLY is read broadly to include inference decisions, model decisions, override events beyond conventional security logs per Art. 12(2) `functioning of a high-risk AI system` opening); any upward adjustment beyond 6 months is documented with the intended-purpose justification; the `under their control` qualifier is the responsibility-allocation hinge (physical control + legal control via contractual retention obligation + technical access via read-access — cumulative reading); the GDPR escape clause `unless provided otherwise in the applicable Union or national law, in particular Union law on the protection of personal data` defers to GDPR Art. 5(1)(e) when the log contains personal data — the operative retention range is [6 months, "necessary"] with AI Act setting the floor and GDPR setting the cap (floor-within-ceiling); when AI logs contain personal data, separation architecture (pseudonymisation of the personal-data subset, separate retention rules, separate storage paths) may be used as a controlled hand-off; verified by Art. 19(1) ≥6-month floor-enforcement audit + `appropriate to the intended purpose` upwar... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Security updates and supporting advisory messages remain available to users across the ... | CRA | sufficient | PR.PS-02 | high |

### D-05.2 · CRA · subso SO-D-05.2.CRA
- **Objective**: Security updates and supporting advisory messages remain available to users across the support period and the 10-year (or remainder-of-support-period) update-availability tail (Art. 13(9) 10-year update-availability tail + Art. 13(8) 5-year support-period floor + Art. 13(18) 10-year Annex II information accessibility + Annex I Part II (7) secure update distribution + Annex I Part II (8) dissemination without delay, free of charge, with advisory messages); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (1)**: PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — Article maps PR.PS-02 for action keyword 'update' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Security updates available across support period and the 10-year-or-remainder tail; An... | CRA | sufficient | - | high |

### D-05.2 · CRA · req 5.2.2
- **Title**: "Security updates available across support period and the 10-year-or-remainder tail; Annex II information accessible for ≥10 years from placing on market; support-period end-date communicated at purchase"
- **Description**: The product shall keep security updates and supporting advisory messages available to users across the support period and the 10-year-or-remainder-of-support-period update-availability tail (Art. 13(9) 10-year tail + Art. 13(8) 5-year support-period floor), with secure update distribution and dissemination without delay, free of charge (Annex I Part II (7)/(8)), and the Annex II information shall remain accessible for at least 10 years from placing on market (Art. 13(18)); the manufacturer provides the support-period end-date clearly and understandably at the time of purchase (Art. 13(19) + Annex II §7).
- **Fit criterion (prose)**: A manufacturer-side update-availability-tail architecture is operated under PR.PS-02 software maintained, replaced, and removed commensurate with risk (the artefact-availability leg — signed packages, version archives, integrity-protected catalogues, rather than the active-patching leg) + GV.OV-02 organisational cybersecurity risk-management strategy reviewed and adjusted (the strategic-review dimension — as the technology baseline and threat landscape evolve, the manufacturer reviews its retention strategy against the Art. 13(9) floor) + GV.OC-04 critical objectives, capabilities, and services that stakeholders depend on or expect from the organisation are understood and communicated (the user-as-stakeholder dimension — advisory messages required by Annex I Part II (8) supply the per-update communication channel and the Annex II information deliverable supplies the durable instruction layer); the Art. 13(8) 5-year support-period floor is enforced per product (or expected use time if shorter); the Art. 13(9) 10-year-or-remainder-of-support-period update-availability tail is enforced per update with the twin-anchor pattern (R2 reading — the longer of 10 years from issue date or the remainder of the support period applies per update; R1 always-10-years and R3 always-remainder are both rejected because they ignore the "whichever is longer" qualifier or the 10-year floor respectively); the Art. 13(18) ≥10-year Annex II information accessibility is enforced from placing on market with the conjunction support-period + at-least-10-years preserved (the longer of the two governing); the Art. 13(19) support-period end-date display at purchase is implemented clearly and understandably with the month and year (Annex II §7); the CRA 10-year tail is on update artefacts (firmware, patches, advisories — non-personal data) and Annex II information, NOT on personal data; when a CRA update-distribution log contains personal data, separation architecture (pseudonymisation of the pe... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.OC-04 — Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated — **CORE** — CSF title shares 14 action tokens with objective
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 7 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('patch') in objective maps to PR.PS-02
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Personal data are kept in a form which permits identification of data subjects for no l... | GDPR | excessive | - | high |

### D-05.2 · GDPR · subso SO-D-05.2.GDPR
- **Objective**: Personal data are kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/GDPR_Art_30.md` (Art. 30) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.AM-08, ID.AM-03 — literal duplicate(s) of ID.AM-08, ID.AM-03
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal data retained no longer than necessary for the processing purpose; longer ret... | GDPR | sufficient | - | high |

### D-05.2 · GDPR · req 5.2.1
- **Title**: "Personal data retained no longer than necessary for the processing purpose; longer retention only where lawful and subject to Art. 89(1) safeguards; Art. 30(1)(f) RoPA time-limits documented per category"
- **Description**: The product shall keep personal data in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (Art. 5(1)(e)); longer retention is permitted only where lawful and subject to Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) for archiving purposes in the public interest, scientific or historical research, or statistical purposes; the RoPA documents the envisaged time limits for erasure of the different categories of data (Art. 30(1)(f)).
- **Fit criterion (prose)**: A controller-side personal-data-retention-ceiling architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (every personal-data category appears in an inventory tagged with declared purpose, lawful basis, and envisaged erasure time so that periodic review can decide to retain, anonymise or delete against a documented clock) + ID.AM-08 data managed consistent with the controller's risk strategy (the controller defines and documents a retention period for each category, resets the clock when the underlying purpose changes, and pairs long-term archiving or research-only retention with the Art. 89(1) pseudonymisation, aggregation and access-limitation safeguards); the Art. 5(1)(e) `no longer than is necessary` ceiling is enforced per data category with periodic erasure-or-anonymisation review; the Art. 30(1)(f) RoPA envisages-time-limits-for-erasure (or the criteria for determining them, where possible per OJ hedge) are documented per category; for the public-interest/research/statistical carve-out, Art. 89(1) safeguards (pseudonymisation, aggregation, access limitation) are applied so that the residual data set at any moment is the smallest the purpose permits; the controller demonstrates ex post against the Art. 5(2) accountability duty that no personal data was retained beyond the period necessary for its declared purpose on the day of any supervisory inspection; when the same data flow is also a CRA update artefact (CRA update-distribution log containing personal data) or an AI Act log (AI log containing personal data), the GDPR Art. 5(1)(e) `necessary` boundary is the operative cap on the personal-data subset, with separation architecture (pseudonymisation of the personal-data subset, separate retention rules) as the controlled hand-off to the CRA-side availability tail or AI Act-side log floor; verified by data-inventory audit + per-category retention-period documentation review + Art. 30(1)(f) RoPA time-... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.2/articles/GDPR_Art_30.md` (Art. 30) — paraphrased action
- **Anchors listed**:
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-05.3 Right to Erasure

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The user of a product with digital elements can securely and easily remove, on a perman... | CRA | excessive | - | low |

### D-05.3 · CRA · subso SO-D-05.3.CRA
- **Objective**: The user of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product; where such data can be transferred to other products or systems, the transfer is done in a secure manner (Annex I Part I (2)(m) first limb — terminal deletion on user election — and second limb — secure cross-product transfer).
- **Anchors listed**:
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-02 — The confidentiality, integrity, and availability of data-in-transit are protected — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.DS-10, ID.AM-08, PR.DS-02 — literal duplicate(s) of PR.DS-10, ID.AM-08, PR.DS-02
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "User of a product with digital elements can securely and easily remove, on a permanent... | CRA | sufficient | - | low |

### D-05.3 · CRA · req 5.3.2
- **Title**: "User of a product with digital elements can securely and easily remove, on a permanent basis, all data and settings of the product via a discoverable user-interface affordance, with Annex II §8(d) decommissioning instructions"
- **Description**: The product shall expose a discoverable user-interface affordance allowing the user to securely and easily remove, on a permanent basis, all data and settings of the product (Annex I Part I (2)(m) first limb — both secure AND easy; permanent = recovery-infeasible), supported by Annex II §8(d) decommissioning instructions and the Annex VII §2 data-class inventory demonstrating that the deletion surface is comprehensive.
- **Fit criterion (prose)**: A manufacturer-side user-facing removal affordance is exposed through the product UI (per SR-CRA-048 VAG+COORD-S2 R1 — both secure AND easy via a discoverable user-interface affordance; a deletion mechanism that is easy but not secure (plain-delete of pointers without overwriting storage) fails, one that is secure but not easy (deep-wipe requiring specialist tooling the user does not have) fails); the deletion surface is comprehensive (ID.AM-08 data-class inventory per Annex VII §2 covers telematics, locally-cached cloud-synced state, paired-device records — SR-CRA-048 POLY-S2 R1 universal-quantifier reading); the deletion mechanism applies cryptographic-erase, secure-overwrite, or physical-media destruction as needed for recovery-infeasibility per SR-CRA-048 POLY-VAG-S2 R3 (any method that makes recovery infeasible is acceptable); PR.DS-10 in-use data-path coverage is documented (the runtime-protection layer that the secure-removal affordance extends through); ID.AM-08 data-class inventory is maintained (the architectural-decision layer — the manufacturer designs the product to retain no extraneous data that would survive disposal); Annex II §8(d) decommissioning instructions are supplied with the product (the information deliverable under Art. 13(18)); Annex VII §2 technical documentation + Annex VII §6 test reports demonstrate verification of conformity with Annex I Part I (2)(m); the (2)(m) affordance is independent of any GDPR-side Art. 17(3) carve-outs — the user retains the product-side removal affordance even when the controller-side obligation is lawfully suspended under Art. 17(3); for an integrated manufacturer-controller on a CRA-classified product processing personal data, the manufacturer's (2)(m) affordance is the architectural substrate through which the controller's Art. 17 path executes and the manufacturer's Annex VII documentation discharges the controller's Art. 5(2) accountability evidence; verified by UI affordance discoverability test + d... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Personal data are erased without undue delay on the data subject's Art. 17(1) request w... | GDPR | sufficient | - | high |

### D-05.3 · GDPR · subso SO-D-05.3.GDPR
- **Objective**: Personal data are erased without undue delay on the data subject's Art. 17(1) request where one of the six Art. 17(1) grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn (no other Art. 6(1) basis applies); (c) Art. 21(1) objection (no overriding compelling legitimate ground) or Art. 21(2) direct-marketing objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child (Art. 8(1)). On processor contract end, the processor deletes or returns all personal data and existing copies per Art. 28(3)(g).
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Personal data erased without undue delay on the data subject's Art. 17(1) request wher... | GDPR | sufficient | - | high |

### D-05.3 · GDPR · req 5.3.1
- **Title**: "Personal data erased without undue delay on the data subject's Art. 17(1) request where one of the 6 grounds applies; processor deletes or returns all personal data on contract end per Art. 28(3)(g); cryptographic key destruction as deletion path"
- **Description**: The product shall erase personal data without undue delay on the data subject's Art. 17(1) request where one of the six grounds (a)–(f) applies: (a) no longer necessary for original purposes; (b) consent withdrawn; (c) Art. 21 objection; (d) unlawful processing; (e) legal-obligation erasure; (f) information-society-service offers to a child; on processor contract end, the processor deletes or returns all personal data and deletes existing copies per Art. 28(3)(g), operationalised through cryptographic key destruction where the controller holds the key outside the data substrate (per SR-GDPR-030 POLY-S3 → cryptographic-erasure reading).
- **Fit criterion (prose)**: A controller-side erasure architecture is operated under PR.DS-10 in-use key-custody discipline (the runtime-protection prerequisite that erasure must extend through — active replicas, query caches, processing pipelines) + ID.AM-08 documented deletion procedure keyed to the Art. 17 trigger conditions and Art. 5(1)(e) purpose-end moment (the lifecycle-management substrate); cryptographic key destruction is the operational realisation of `deletes` per SR-GDPR-030 POLY-S3 → cryptographic-erasure reading — key held outside the data substrate, key destruction scales across backups and replicas without per-copy destruction, aligned with EDPB Guidelines 5/2020; backup copies are in scope per SR-GDPR-031 SCOPE-Q R1 unless protected by a separate Union/Member State law storage obligation; audit logs are out of scope to the extent needed for legal-accountability purposes (SR-GDPR-031 R1); the 6 Art. 17(1) grounds (a)–(f) are evaluated on every request; the Art. 17(3) carve-outs (freedom of expression, legal obligation, public-interest public-health, archiving per Art. 89(1), establishment-exercise-defence of legal claims) are honoured as exception structure without relaxing the erasure duty beyond what they permit; Art. 17(2) confirmation of action is delivered to the data subject; Art. 12(1) transparency on the right is provided; the Art. 19 cascade to downstream recipients (rectification/erasure/restriction notification) is executed (handled structurally in D-04.3 SO-GDPR-012 — not duplicated here); Art. 30(1)(f) RoPA envisages-time-limits-for-erasure are documented per category; Art. 5(2) accountability evidence is inspection-ready; for a processor, the Art. 28(3)(g) contract-end deletion-or-return obligation is documented with GV.SC-04 evidentiary confirmation (audit, test result, or independent inspection so the controller can demonstrate, against Art. 5(2), that on the day any supervisory inspection occurs the personal data under the processor's custody no longer ex... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_11.md` (Art. 11) — paraphrased action
- **Anchors listed**:
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-05.4 Data Portability

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The data subject receives personal data in a structured, commonly used, machine-readabl... | GDPR | sufficient | - | high |

### D-05.4 · GDPR · subso SO-D-05.4.GDPR
- **Objective**: The data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)). The data subject can transmit those data to another controller without hindrance (Art. 20(1)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2). The right applies where processing is based on consent (Art. 6(1)(a)) or contract (Art. 6(1)(b)) AND processing is carried out by automated means (Art. 20(3)); the right does NOT apply to public-interest-task or legitimate-interest processing (Art. 20(4)), and the controller may refuse an export where it would adversely affect third-party rights.
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Data subject receives personal data in a structured, commonly used, machine-readable f... | GDPR | sufficient | - | high |

### D-05.4 · GDPR · req 5.4.1
- **Title**: "Data subject receives personal data in a structured, commonly used, machine-readable format (Art. 20(1) + Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, ≤2 months complex) and free of charge (Art. 12(5)); cross-controller direct transmission provided where technically feasible"
- **Description**: The product shall, on the data subject's Art. 20(1) request, deliver a copy of the portability-eligible personal data (Art. 6(1)(a) consent or Art. 6(1)(b) contract basis + Art. 20(3) automated-means requirement) in a structured, commonly used, machine-readable format (Art. 15(3) companion copy), supplied by the controller without undue delay (Art. 12(3) ≤1 month, extendable to ≤2 months for complex requests) and free of charge (Art. 12(5)); where technically feasible, the originating controller transmits directly to the receiving controller (Art. 20(2) sentence 2).
- **Fit criterion (prose)**: A controller-side Art. 20 portability export endpoint is operated under PR.DS-10 runtime integrity posture (the export must reflect current processing truth under controlled exposure rather than stale snapshot drift — partial views derived from the same in-use data set are properly handled) + ID.AM-08 format-quality substrate (the structured, machine-readable, downstream-tool-friendly formats are layered into the data-handling substrate rather than treated as ad-hoc report outputs, ensuring security-classification discipline is preserved); the structured-interoperable format (JSON, CSV, XML per EDPB Guidelines 06/2020 — the print-ready reading (PDF/scanned image) rejected as defeating the purpose, the controller-proprietary reading rejected as functionally obstructing) is supplied as the default per SR-GDPR-032 VAG-S3 structured-interoperable reading; the Art. 20(3) consent/contract-basis + automated-means conditions are checked before exporting (portability applies only when the processing is based on Art. 6(1)(a) consent OR Art. 6(1)(b) contract AND the processing is carried out by automated means); the Art. 20(4) exclusions (no public-interest-task processing, no legitimate-interest processing) are honoured without prejudice to the Art. 21 right to object; the Art. 20(3) third-party-rights carve-out is honoured (refusal on the rare-but-honest ground that the export would adversely affect third-party rights and freedoms); the Art. 12(3) service-level of ≤1 month (extendable to ≤2 months for complex requests with reasoned extension notice delivered to the data subject within the original ≤1-month period) is met; the export is free of charge per Art. 12(5); cross-controller direct transmission is provided where technically feasible per Art. 20(2) sentence 2 (mutually-authenticated transport encryption with destination authentication + signed export manifests); Art. 13(2)(b) / Art. 14(2)(c) information-supply notifies the data subject of the right at collection (... (line truncated to 2000 chars)
- **Regulatory basis**: `domains/D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.DS-10 — The confidentiality, integrity, and availability of data-in-use are protected — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-06.1 Vendor Risk Assessment

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The manufacturer exercises due diligence when integrating components sourced from third... | CRA | excessive | - | high |

### D-06.1 · CRA · subso SO-D-06.1.CRA
- **Objective**: The manufacturer exercises due diligence when integrating components sourced from third parties — including components of free and open-source software not made available on the market in the course of a commercial activity (Art. 3(48) FOSS definition) — so that those components do not compromise the cybersecurity of the product with digital elements (Art. 13(5) sentence 1); on becoming aware of a component vulnerability (Art. 13(6) sentence 1), the manufacturer addresses and remediates it without delay and shares relevant information with the component supplier (Art. 13(6) sentence 2).
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — Action keyword ('supplier') in objective maps to GV.SC-01
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — Action keyword ('supplier') in objective maps to GV.SC-01
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — Action keyword ('supplier') in objective maps to GV.SC-01
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.SC-01, GV.SC-02, ID.RA-02 — literal duplicate(s) of GV.SC-01, GV.SC-02, ID.RA-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Third-party-component due diligence procedural + substantive including non-commercial ... | CRA | sufficient | - | high |

### D-06.1 · CRA · req 6.1.3
- **Title**: "Third-party-component due diligence procedural + substantive including non-commercial OSS per Art. 3(48), with Art. 13(6) vulnerability reporting and Annex VII §2 technical-documentation record"
- **Description**: The product shall exercise due diligence — procedural + substantive R3 reading — when integrating components sourced from third parties, including components of free and open-source software not made available on the market in the course of a commercial activity per Art. 3(48) FOSS definition, so that those components do not compromise the cybersecurity of the product with digital elements; on becoming aware of a vulnerability in a component (including OSS), the vulnerability is reported to the component maintainer and addressed + remediated in the product per Annex I Part II, with code and documentation shared with the OSS maintainer per Art. 13(6) sentence 2; the due-diligence discipline operates across the support period under Art. 13(8) and is documented in the Annex VII §2 technical documentation (CRA Art. 13(5) `due diligence` R3 + Art. 13(6) component vulnerability reporting + Art. 3(48) FOSS definition + Art. 13(2) risk assessment + Art. 13(8) support-period handling + Annex VII §2).
- **Fit criterion (prose)**: A manufacturer-side third-party-component due-diligence discipline is operated via GV.SC-01 documented programme-governance layer (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed by organisational stakeholders, covering commercial and non-commercial OSS components) + GV.SC-02 component inventory + prioritisation by criticality + assessment against documented cybersecurity criteria + ID.RA-02 threat-intelligence loop (CVE feeds, advisories, OSS-security mailing lists); each integrated third-party component — commercial or non-commercial OSS per Art. 3(48) — undergoes the R3 procedural + substantive due diligence reading (documented vetting process evidenced in Annex VII §2, plus positive verification of supplier / component security posture), with OSS-specific calibration (stewardship assessment, CVD policy review, vulnerability disclosure channel, governance-transparency review) per SR-CRA-050 ambiguity_notes; the Art. 13(6) sentence 1 vulnerability-reporting address-and-remediate duty operates on becoming-aware of a component vulnerability, with the Art. 13(6) sentence 2 OSS-sharing limb applying when an OSS component is integrated (code and documentation shared with the OSS maintainer for fix development); the SBOM under Annex I Part II (1) (D-06.2 cross-ref) feeds the component-inventory substrate; the component-tier due-diligence discipline operates at the product-internal boundary only, with the tier hand-off to processor-tier (GDPR leg), supplier-tier (NIS 2 leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces; verified by GV.SC-01 programme-governance documentation review + GV.SC-02 component-prioritisation records audit + ID.RA-02 threat-intelligence-feed evidence review + Annex VII §2 component-due-diligence rationale review + Annex VII §3 risk-assessment record review + Art. 13(6) component-vulnerability reporting log inspection + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('supply chain')
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Financial entities manage ICT third-party risk taking into account four-factor proporti... | DORA | excessive | - | high |

### D-06.1 · DORA · subso SO-D-06.1.DORA
- **Objective**: Financial entities manage ICT third-party risk taking into account four-factor proportionality — nature, scale, complexity and importance of ICT-related dependencies (Art. 28(1) four-way AND) — and the risks arising from contractual arrangements on the use of ICT services; the Art. 28(5) CIF escalator ("most up-to-date and highest quality information security standards") applies to contractual arrangements concerning critical or important functions.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third-party') in objective maps to GV.SC-02
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — CSF title shares 1 token ('services') with objective; reinforces but is not the direct action
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third-party') in objective maps to GV.SC-02
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — CSF title shares 1 token ('services') with objective; reinforces but is not the direct action
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — CSF title shares 1 token ('services') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.SC-02, ID.AM-04 — literal duplicate(s) of GV.SC-02, ID.AM-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "ICT-third-party-as-financial-entity-counterparty risk under Art. 28(1) four-factor pro... | DORA | sufficient | - | high |

### D-06.1 · DORA · req 6.1.4
- **Title**: "ICT-third-party-as-financial-entity-counterparty risk under Art. 28(1) four-factor proportionality (nature, scale, complexity, importance) with Art. 28(5) CIF escalator"
- **Description**: The product shall manage ICT third-party risk taking into account the nature, scale, complexity and importance of ICT-related dependencies and the risks arising from contractual arrangements on the use of ICT services, including the criticality or importance of the respective service, process or function — with the four factors informing risk assessment cumulatively and the criticality-or-importance judgement applying to all three artefact categories; contractual arrangements with ICT third-party service providers comply with appropriate information security standards, and for contractual arrangements concerning critical or important functions, the most up-to-date and highest quality information security standards are used (DORA Art. 28(1) four-factor AND + service/process/function OR + Art. 28(5) CIF escalator + Art. 28(4) concentration-risk identification + Art. 30(1)+(2) closed-list 9-element contract + Art. 30(3)(e)(i)+(ii) audit-rights architecture).
- **Fit criterion (prose)**: A financial-entity ICT-third-party-risk-management discipline is operated via GV.SC-02 prioritisation and assessment engine stratified by the Art. 28(1)(i) four-factor AND proportionality (nature, scale, complexity, importance — all four factors informing risk assessment cumulatively per COORD-S2 R1) + Art. 28(1)(ii) criticality-or-importance of the respective service/process/function (cumulative per COORD-S2 across all three artefacts) + ID.AM-04 supplier inventory substrate (the proportionality judgement is grounded in the actual supplier inventory, not ad-hoc case-by-case reasoning); each ICT third-party service-provider relationship is assessed against a documented supply-chain risk-management process aligned with EBA Guidelines on outsourcing arrangements; for contractual arrangements concerning critical or important functions (CIF), the Art. 28(5) CIF escalator is applied — the most up-to-date and highest quality information security standards are used (with the `critical or important` distinction POLY-S2 propagated to 18 of 38 DORA clauses per SR-DORA-019 ambiguity_notes — both categories in scope with distinct obligations attached, pending EBA RTS clarity); the Art. 30(1)+(2) 9-element closed-list contract (a)–(i) materialises the assessment into the contractual instrument + the Art. 30(3)(e)(i)+(ii) universal unrestricted rights of access, inspection and audit (with the alternative-assurance-levels qualification when other clients' rights are affected) closes the audit loop; the DORA four-factor test operationalises GDPR Art. 28(1) `sufficient guarantees` and NIS 2 Art. 21(1) chapeau with sharper factors in the financial-services subset (DORA-dominant stack where applicable); the ICT-third-party-as-financial-entity-counterparty risk discipline operates at the financial-entity ICT-dependency boundary only, with the tier hand-off to processor-tier (GDPR leg), supplier-tier (NIS 2 leg), and component-tier (CRA leg) documented as the controlled interfaces; verified by GV.SC-02 supplier-prioritisation records audit + ID.AM-04 supplier-inventory review + Art. 28(1) four-factor proportionality record inspection + Art. 28(5) CIF-standards compliance evidence review + Art. 30(2) 9-element contract attestation review + Art. 30(3)(e) audit-rights architecture documentation review + national-financial-supervisory-authority + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — Action keyword ('supplier') in objective maps to GV.SC-01
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The controller engages only processors providing sufficient guarantees to implement app... | GDPR | excessive | - | high |

### D-06.1 · GDPR · subso SO-D-06.1.GDPR
- **Objective**: The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights (Art. 28(1)); the Art. 28(3) DPA closed-list clauses (a)–(h) are documented and the sub-processor authorisation chain (Art. 28(2)) is material to the due diligence.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/GDPR_Art_28.md` (Art. 28) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.SC-02, GV.SC-04 — literal duplicate(s) of GV.SC-02, GV.SC-04
- **Confidence**: high (article mapping and CSF title both consulted)

| "Processor-as-legal-entity due diligence with documented `sufficient guarantees` and Ar... | GDPR | sufficient | - | high |

### D-06.1 · GDPR · req 6.1.1
- **Title**: "Processor-as-legal-entity due diligence with documented `sufficient guarantees` and Art. 28(3) DPA closed-list clauses"
- **Description**: The product shall operate processor-as-legal-entity due diligence on each data-processing counterparty before engagement — verifying that the processor provides sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights — and shall document the EDPB Guidelines 07/2020 4-factor assessment (knowledge + reliability of resources + compliance track-record + financial stability), the Art. 28(3) closed-list DPA clauses (a)–(h), and the sub-processor authorisation chain under Art. 28(2) (GDPR Art. 28(1) `sufficient guarantees` + Art. 28(2) sub-processor authorisation + Art. 28(3) DPA closed list + Art. 4(7)/(8) controller/processor definitions).
- **Fit criterion (prose)**: A processor-selection discipline is operated before engagement covering each prospective processor via GV.SC-02 documented-due-diligence practice (written due-diligence questionnaire, certifications review, security-measures audit, sub-processor inventory) anchored on the EDPB Guidelines 07/2020 4-factor test; the Art. 28(3) closed-list DPA clauses (a) documented instructions + (b) confidentiality + (c) Art. 32 measures + (d) sub-processor conditions + (e) data-subject-rights assistance + (f) Art. 33/34 incident-assistance + (g) deletion-or-return + (h) audit/inspection are documented in each processor contract with attestation of compliance; the Art. 28(2) sub-processor authorisation chain is materialised as a written prior-authorisation regime (specific or general with information right) and a sub-processor list maintained in the Art. 30(2) RoPA processor record; the processor-as-legal-entity due diligence discipline operates at the data-processing-counterparty boundary only, with the tier hand-off to supplier-tier (NIS 2 leg), component-tier (CRA leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces (when the same supplier is a processor + direct supplier + component source + ICT provider, the four assessments compose into a single supplier-of-record without collapsing the per-tier evidence); verified by EDPB 07/2020 4-factor processor-guarantees evidence review + Art. 28(3) closed-list DPA-clause attestation review + Art. 28(2) sub-processor authorisation chain inspection + Art. 30(2) RoPA processor-record inspection + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/GDPR_Art_28.md` (Art. 28) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Essential and important entities take appropriate and proportionate technical, operatio... | NIS2 | excessive | - | high |

### D-06.1 · NIS2 · subso SO-D-06.1.NIS2
- **Objective**: Essential and important entities take appropriate and proportionate technical, operational and organisational measures across direct supplier and service-provider relationships, including security-related aspects of those relationships (Art. 21(2)(d)), taking into account state of the art (Art. 21(1) sentence 2) and the risks posed to the security of network and information systems; the Art. 21(3) sentence 1 three-prong supplier assessment (supplier-specific vulnerabilities + overall quality of products and cybersecurity practices + supplier secure-development procedures) is performed per direct supplier, with EU-level coordinated risk-propagation inputs (Art. 21(3) sentence 2 → Art. 22) taken into account where available.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — Reinforces obligation in same CSF function (IDENTIFY) but does not directly match the action
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.SC-02 — literal duplicate(s) of GV.SC-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Direct-supplier-as-relationship security with Art. 21(2)(d) `direct` scope-limiter, Ar... | NIS2 | sufficient | - | low |

### D-06.1 · NIS2 · req 6.1.2
- **Title**: "Direct-supplier-as-relationship security with Art. 21(2)(d) `direct` scope-limiter, Art. 21(1) `appropriate and proportionate` chapeau, and Art. 21(3) three-prong supplier assessment"
- **Description**: The product shall operate direct-supplier-as-relationship security covering security-related aspects concerning the relationships between each entity and its direct suppliers or service providers (Art. 21(2)(d) `direct` scope-limiter, with the chosen reading R1 Tier-1 contractual as the minimum + R2 technically integrated + R3 operationally dependent per Recital 56), calibrated to state of the art (Art. 21(1) sentence 2) and the risks posed, with the Art. 21(3) sentence 1 three-prong supplier assessment performed per direct supplier — supplier-specific vulnerabilities (vulnerabilities specific to each direct supplier per SR-NIS2-022) + overall quality of products and cybersecurity practices + supplier secure-development procedures — and EU-level coordinated risk-assessment inputs (Art. 21(3) sentence 2 → Art. 22 Cooperation Group) taken into account where available (NIS 2 Art. 21(2)(d) + Art. 21(1) chapeau + Art. 21(3) sentence 1 three-prong + Art. 21(1) sentence 2 state-of-the-art + Recital 56).
- **Fit criterion (prose)**: A direct-supplier-risk-management discipline is operated covering each in-scope direct supplier via GV.SC-02 supplier register and prioritisation methodology (with R1 Tier-1 contractual as the minimum `direct` scope + R2 technical-integration + R3 operationally-dependent per Recital 56 risk-management-precaution principle); the Art. 21(3) three-prong supplier assessment is performed per direct supplier covering (a) supplier-specific vulnerabilities via ID.RA-01 vulnerabilities-identified leg + ID.RA-02 threat-intelligence-collected leg (CVE feeds, vendor advisories, sectoral CSIRT notifications, threat-intelligence subscriptions) + ID.AM-04 supplier-inventory substrate, (b) overall quality of products and cybersecurity practices via GV.SC-04 audits/test-results/certifications leg (chosen R4 composite reading of `overall quality` per SR-NIS2-022 ambiguity_notes), (c) supplier secure-development procedures via the externally-assessable interpretation (questionnaire / contract clause / third-party attestation) per SR-NIS2-023; the Art. 21(1) `appropriate and proportionate` chapeau and Art. 21(1) sentence 2 state-of-the-art qualifier calibrate the assessment depth to risk profile and cost; the Art. 21(3) sentence 2 EU-level coordinated risk-assessment inputs (Cooperation Group + Commission + ENISA under Art. 22(1)) are taken into account in supplier-risk decisions; the direct-supplier-as-relationship security discipline operates at the entity-level supplier boundary only, with the tier hand-off to processor-tier (GDPR leg), component-tier (CRA leg), and ICT-provider-tier (DORA leg) documented as the controlled interfaces; verified by supplier-register audit + Art. 21(3) three-prong per-supplier assessment records inspection + GV.SC-04 audit/test-result records review + ID.RA-02 threat-intelligence-feed evidence review + Art. 22 EU-level coordinated-assessment inputs integration review + CSIRT-or-competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 6 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-06.2 Software Bill of Materials (SBOM)

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The manufacturer draws up and maintains an SBOM covering the components and dependencie... | CRA | sufficient | - | high |

### D-06.2 · CRA · subso SO-D-06.2.CRA
- **Objective**: The manufacturer draws up and maintains an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)).
- **Anchors listed**:
  - (none listed)
- **Coverage verdict**: sufficient (no anchors required (reg has no obligation in this sub-domain))
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (no anchors listed (expected state for inapplicable regs))

| "Three-anchored SBOM architecture: machine-readable format covering at least top-level ... | CRA | sufficient | - | high |

### D-06.2 · CRA · req 6.2.1
- **Title**: "Three-anchored SBOM architecture: machine-readable format covering at least top-level dependencies authored at release + retained in technical documentation under Annex VII §2(b) + disclosed to MSAs on reasoned request under Annex VII §8 + optional user access under Annex II §9"
- **Description**: The product shall draw up and maintain an SBOM covering the components and dependencies contained in the product with digital elements in a commonly used and machine-readable format that includes, at minimum, the top-level dependencies (Annex I Part II (1)); the SBOM is included in the technical documentation under Annex VII §2(b) surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9); on a reasoned request from a market surveillance authority, the SBOM is provided where necessary for the authority to check compliance with the Annex I cybersecurity requirements (Annex VII §8); the manufacturer may, where it decides to make available an SBOM externally, identify where it is located under Annex II §9 (manufacturer's discretion, no obligation to publish); the format and elements of the SBOM may be further specified by Commission implementing acts under Art. 13(24); the SBOM is the upstream component-identification artefact that feeds the SR-CRA-050 component due diligence in 6.1 and the SR-CRA-007 + SR-CRA-008 + SR-CRA-010 vulnerability identification + remediation in D-02.x (CRA Art. 3(39) SBOM definition + Annex I Part II (1) authoring + Annex VII §2(b) technical-documentation retention + Annex II §9 optional user access + Art. 13(24) Commission implementing acts + Annex VII §8 MSA reasoned request + Art. 13(1) design-time + Art. 13(7) all-cybersecurity-aspects documentation + Art. 13(8) sentence 1 support-period handling + Art. 13(13) 10-year retention + Annex VII §4 retention).
- **Fit criterion (prose)**: A manufacturer-side three-anchored SBOM architecture is operated via ID.AM-02 software-inventory substrate (the SBOM is the most specific operational expression of the software-inventory principle in the product-side cybersecurity domain, with the machine-readable format qualifier supplying the queryable interface that defenders use to correlate upstream CVEs against the product's dependency surface — a `commonly used and machine-readable format` is the structural requirement that turns the SBOM from a static artefact into an input to vulnerability-management automation, CVE matching, and downstream supply-chain risk assessment) + GV.SC-02 supply-chain encoding (the format encodes supplier and supply-chain relationships per the Art. 3(39) definition, so the SBOM supports both vulnerability lookup and supplier-prioritisation under the broader cybersecurity supply-chain risk-management process) + GV.SC-03 retention-and-disclosure architecture (the Annex VII §2(b) technical-documentation layer survives the Annex VII §4 retention period and ties to the type-examination record for Class II products under Annex IV, and the Annex II §9 user-facing SBOM access is the contractual-equivalent transparency lever for voluntary disclosure, with the SBOM-internal record as the contractual coordination point with downstream integrators who depend on the SBOM for their own SR-CRA-050 due-diligence work); the authoring anchor (Annex I Part II (1)) produces an SBOM in a commonly used and machine-readable format covering at minimum the top-level dependencies (POLY-S2 R1 reading per SR-CRA-052 — first-level direct dependencies with depth-1 look-through; depth-discretionary beyond the floor) with the format choice (POLY-S3 R3 reading per SR-CRA-008 — any commonly-used machine-readable format that supports automated component identification, pending the Commission implementing acts under Art. 13(24)) documented in the conformity dossier; the retention anchor (Annex VII §2(b) + Annex VII §4) includes the SBOM in the technical documentation surviving the Annex VII §4 retention period (10 years or support period, whichever is longer) per Art. 13(13) + Art. 13(9) 10-year tail; the regulatory-disclosure anchor (Annex VII §8) provides the SBOM on reasoned request from an MSA with the `where necessary` scope (POLY-S2 R1 reading per SR-CRA-053 — necessary subset directly relevant to the compliance question under investigation, not a comprehensive dump of every component) documented in the MSA-request log; the optional Annex II §9 user-facing access is at the manufacturer's discretion (POLY-S2 R1 reading per SR-CRA-053 — no obligation to publish the SBOM externally; the obligation is only to include it in the technical documentation); the format-migration posture when the Commission implementing acts under Art. 13(24) specify a binding format is documented with versioning evidence across the support period; the SBOM is continuously updated through the support period under Art. 13(8); the three-anchored SBOM architecture operates as the upstream component-identification artefact feeding 6.1 (component due diligence under SR-CRA-050), 2.1 (vulnerability identification under SR-CRA-007), 2.2 (vulnerability remediation under SR-CRA-008 + SR-CRA-010), and 9.4 (technical documentation under SR-CRA-059); verified by Annex VII §2(b) technical-documentation SBOM inclusion review + ID.AM-02 software-inventory substrate audit (format supports automated CVE matching) + GV.SC-02 supplier-relationship encoding review + SBOM versioning records audit + Annex VII §4 retention compliance review + Annex VII §8 MSA-request response log inspection + Annex II §9 user-access posture documentation review + Art. 13(8) continuous-update evidence review + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 5 action tokens with objective
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-02
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-06.3 Contractual Security Obligations

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| CRA contractual-security coverage is expressed through economic-operator duties rather ... | CRA | sufficient | - | low |

### D-06.3 · CRA · subso SO-D-06.3.CRA
- **Objective**: CRA contractual-security coverage is expressed through economic-operator duties rather than a single negotiated contract: importers place products with digital elements on the Union market only after verifying conformity assessment, technical documentation, CE marking, and manufacturer identification, and escalate significant risk or vulnerabilities to the manufacturer and MSA while taking corrective measures; distributors act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, and escalate non-conformity or vulnerabilities.
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MI-01 — Incidents are contained — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Importer pre-market verification (Art. 19) + distributor due-care + non-conformity esc... | CRA | sufficient | - | high |

### D-06.3 · CRA · req 6.3.3
- **Title**: "Importer pre-market verification (Art. 19) + distributor due-care + non-conformity escalation (Art. 20) + component-vulnerability reporting (Art. 13(6)) — regulatory economic-operator duties, NOT DPA-style contracts"
- **Description**: The product shall enforce importer duties under Art. 19 (verify conformity assessment, technical documentation, CE marking, manufacturer identification before market placement; escalation when product presents significant risk or vulnerabilities, taking corrective measures) and distributor duties under Art. 20 (act with due care, verify CE marking and required documentation, confirm manufacturer/importer compliance, escalate non-conformity or vulnerabilities), plus Art. 13(6) component-vulnerability reporting on becoming aware of a vulnerability (address and remediate in product per Annex I Part II; share code and documentation with OSS maintainer per Art. 13(6) sentence 2); CRA economic-operator duties are imposed by regulation rather than negotiated as a DPA.
- **Fit criterion (prose)**: An economic-operator compliance matrix is maintained per importer/distributor/modifier with documented pre-market verification records (Art. 19(2) conformity-assessment verification + technical-documentation check + CE marking + manufacturer-identification verification) and due-care records (Art. 20(2) CE-marking verification + documentation review + manufacturer/importer-compliance verification); Art. 19(3) importer-measures records document escalation and corrective-measures when product presents significant risk or vulnerabilities; Art. 20(3) distributor non-conformity records document escalation to manufacturer/importer and corrective-measures without undue delay; Art. 13(6) sentence 1 component-vulnerability reporting address-and-remediate duty operates on becoming-aware (feeds manufacturer-side remediation per Annex I Part II), with Art. 13(6) sentence 2 OSS-sharing limb applying when an OSS component is integrated (code and documentation shared with OSS maintainer); the CRA economic-operator duties are MSA-facing regulatory obligations, NOT DPA-style negotiated contracts — the GDPR DPA matrix and DORA ICT-contract matrix do not subsume CRA duties (different actor, different regulatory direction, different recipient); in NIS 2 overlap (NIS 2 entity deploys CRA product), the CRA escalation feeds the NIS 2 supplier-risk-register input (NIS2↔CRA lifecycle hinge); verified by economic-operator compliance matrix review + Art. 19(2) pre-market verification records inspection + Art. 19(3) corrective-measures records audit + Art. 20(2) distributor due-care records inspection + Art. 20(3) non-conformity escalation log review + Art. 13(6) component-vulnerability reporting log review + MSA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - RS.MI-01 — Incidents are contained — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Financial entities structure ICT third-party contractual arrangements so that rights an... | DORA | sufficient | - | high |

### D-06.3 · DORA · subso SO-D-06.3.DORA
- **Objective**: Financial entities structure ICT third-party contractual arrangements so that rights and obligations are clearly allocated and set out in writing, the Art. 30(2)(a)–(i) minimum elements are present, Art. 28(5) information-security standards are contractually evidenced, and contractual arrangements supporting critical or important functions include the additional CIF clauses required under Art. 30(3) (including unrestricted access/inspection/audit rights where applicable).
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third-party') in objective maps to GV.SC-02
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - DE.CM-06 — External service provider activities and services are monitored to find potentially adverse events — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Art. 30(1)+(2) 9-element ICT-contract closed-list + Art. 28(5) standards record + Art.... | DORA | sufficient | - | high |

### D-06.3 · DORA · req 6.3.4
- **Title**: "Art. 30(1)+(2) 9-element ICT-contract closed-list + Art. 28(5) standards record + Art. 30(3) CIF-only clauses (audit/access/exit) — clause-list union with GDPR Art. 28(3) when same ICT provider is processor"
- **Description**: The product shall structure ICT third-party contractual arrangements so that rights and obligations are clearly allocated and set out in writing per Art. 30(1), incorporate the Art. 30(2)(a)–(i) 9-element minimum ICT-contract list, evidence Art. 28(5) information-security standards contractually (most up-to-date and highest quality for CIF per Art. 28(5) sentence 2; appropriate standards for non-CIF per Art. 28(5) sentence 1), and add Art. 30(3)(a)–(f) CIF-only clauses for critical or important functions (including audit rights, exit-strategy provisions, and concentration-risk identification per Art. 28(4)) — the CORRECTED CRDA pair resolves to clause-list union with GDPR Art. 28(3) when same ICT provider is processor; DORA-exceeds-NIS 2 in financial-services subset.
- **Fit criterion (prose)**: A financial-entity ICT-contract matrix is maintained for each ICT third-party service-provider relationship, with Art. 30(1) clear written allocation of rights and obligations and the Art. 30(2)(a)–(i) 9-element closed-list minimum clauses present in each contract: (a) clear description of functions / ICT services / objectives + (b) effective date + duration + notice periods + (c) locations (data processing, storage, support, service performance) + (d) termination / exit-strategy provisions + (e) financial-entity and competent-authority access/inspection/audit rights per Art. 30(3)(e)(i)/(ii) + alternative-assurance exception only where other clients' rights are affected + (f) SLA + monitoring + reporting + (g) partial/full-substitution provisions + (h) cost allocation + (i) contingency arrangements; Art. 28(5) sentence 1 `appropriate information security standards` applies to non-CIF contracts; Art. 28(5) sentence 2 `most up-to-date and highest quality information security standards` is the CIF escalator for arrangements supporting critical or important functions; Art. 30(3)(a)–(f) CIF-only clauses are added for CIF support (audit-rights framework, on-site documentation-copy right, exit-strategy + transition support, sub-outsourcing restrictions, termination triggers for non-performance); Art. 28(4) concentration-risk identification accompanies CIF support (alternative ICT providers, re-internalisation feasibility); in GDPR overlap (same ICT provider is processor), the contract applies the **clause-list union** of GDPR Art. 28(3) 8-element DPA + DORA Art. 30 9-element ICT-contract list, with GDPR-specific processor terms retained whenever the ICT provider processes personal data (CORRECTED CRDA pair from CONTRADICTORY to COMPLEMENTARY — UNION, NOT substitution); in NIS 2 overlap (financial entity is also NIS 2 essential entity), DORA Art. 30 satisfies NIS 2 `security-related contractual aspects` floor (DORA-exceeds-NIS 2 discharge) — NIS 2 chapeau extends to physical + operational hazards via lex specialis analysis; verified by ICT-contract matrix inspection + Art. 30(2)(a)–(i) 9-element closed-list clause-inventory attestation review + Art. 28(5) standards record review + Art. 30(3) CIF-clause review when CIF support + clause-list union attestation when GDPR overlap + concentration-risk identification record review + national-financial-supervisory-authority-or-competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-06 — External service provider activities and services are monitored to find potentially adverse events — **CORE** — CSF title shares 5 action tokens with objective
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third-party') in objective maps to GV.SC-02
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Controller/processor contracts and related transfer instruments include the GDPR-specif... | GDPR | sufficient | - | low |

### D-06.3 · GDPR · subso SO-D-06.3.GDPR
- **Objective**: Controller/processor contracts and related transfer instruments include the GDPR-specific contractual security obligations required for personal-data processing: the Art. 28(3)(a)–(h) eight-element DPA floor, sub-processor authorisation and change-notification, processor Art. 32 security-measure commitments, audit/inspection access, and contract-end return/deletion; the Art. 46 appropriate-safeguards mechanism and the Art. 48 international-agreement filter apply where personal data leaves the EEA or is exposed to third-country legal-process pressure.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Art. 28(3)(a)–(h) 8-element DPA closed-list contracts + Art. 46 transfer safeguards + ... | GDPR | sufficient | - | low |

### D-06.3 · GDPR · req 6.3.1
- **Title**: "Art. 28(3)(a)–(h) 8-element DPA closed-list contracts + Art. 46 transfer safeguards + Art. 48 international-agreement filter for third-country legal-process exposure"
- **Description**: The product shall materialise controller/processor contractual security obligations as Art. 28(3)(a)–(h) 8-element DPA contracts, Art. 46 appropriate-safeguards instruments for third-country transfers without adequacy decisions, and an Art. 48 international-agreement filter for third-country court/administrative requests, with sub-processor authorisation under Art. 28(2), Art. 32 processor security-measure commitments, audit/inspection access, and contract-end return/deletion — GDPR layer is additive on DORA Art. 30, never substituted (the CORRECTED CRDA pair is clause-list union).
- **Fit criterion (prose)**: A controller-processor DPA matrix is maintained covering each in-scope processor via Art. 28(3)(a)–(h) 8 closed-list clauses — (a) documented instructions + (b) confidentiality + (c) Art. 32 measures + (d) sub-processor conditions + (e) data-subject-rights assistance + (f) Art. 33/34 incident-assistance + (g) deletion-or-return + (h) audit/inspection — attested in each DPA contract; Art. 28(2) sub-processor authorisation chain is materialised as a written prior-authorisation regime with a maintained processor list per Art. 30(2) RoPA; Art. 46 safeguards operate for each transfer (SCCs, BCRs, codes of conduct, certification, ad-hoc contractual clauses) where no adequacy decision exists, with transfer-mapping per Schrems II / EDPB Recommendations 01/2020 supplementary-measures assessment; Art. 48 international-agreement filter rejects or routes through an international-agreement basis any third-country court/administrative request for personal-data disclosure; in DORA overlap, Art. 28(3) 8-element DPA clauses + Art. 46/48 safeguards ADD to DORA Art. 30(2) ICT-contract elements (clause-list union, NOT substitution) with GDPR-specific processor terms retained whenever the ICT provider processes personal data; verified by DPA matrix inspection + Art. 28(3)(a)–(h) closed-list clause-inventory attestation review + Art. 28(2) sub-processor chain inspection + Art. 46 transfer-mapping review + Art. 48 international-agreement filter log review + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Essential and important entities manage contractual security for direct supplier and se... | NIS2 | sufficient | - | high |

### D-06.3 · NIS2 · subso SO-D-06.3.NIS2
- **Objective**: Essential and important entities manage contractual security for direct supplier and service-provider relationships by documenting the supplier universe under the `direct` scope-limiter, embedding security-related contractual aspects into supplier relationships, and assessing each direct supplier against the Art. 21(3) three-prong supplier-assessment structure (supplier-specific vulnerabilities + overall quality of products/services and cybersecurity practices + supplier secure-development procedures); Art. 22 coordinated supply-chain risk assessments are taken into account where available.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Art. 21(2)(d) direct-supplier contractual-security embedding + Art. 21(3) three-prong ... | NIS2 | sufficient | - | low |

### D-06.3 · NIS2 · req 6.3.2
- **Title**: "Art. 21(2)(d) direct-supplier contractual-security embedding + Art. 21(3) three-prong assessment evidence + Art. 22 coordinated-assessment ingestion"
- **Description**: The product shall embed security-related contractual aspects into each direct supplier/service-provider relationship under Art. 21(2)(d) (with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56), maintain documented Art. 21(3) sentence 1 three-prong supplier-assessment evidence per direct supplier (supplier-specific vulnerabilities + overall quality of products/services and cybersecurity practices + supplier secure-development procedures), and ingest Art. 22 EU-level coordinated supply-chain risk-assessment outputs where available — NIS 2 remains separate operational handle from GDPR DPA and from DORA Art. 30, with CRA Art. 13(6) component-vulnerability reporting as the upstream feedback path.
- **Fit criterion (prose)**: A direct-supplier contractual-security matrix is maintained covering each in-scope direct supplier via Art. 21(2)(d) `direct` scope-limiter with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56 risk-management-precaution principle; security-related contractual aspects are embedded via documented contract clauses or schedules covering incident notification, audit cooperation, security-measure commitments, vulnerability disclosure, and termination-for-cause; Art. 21(3) sentence 1 three-prong supplier-assessment evidence is maintained per supplier covering (i) supplier-specific vulnerabilities via ID.RA-01 + ID.RA-02 + CVE feeds + vendor advisories + sectoral CSIRT notifications, (ii) overall quality of products/services and cybersecurity practices via GV.SC-04 audit/test-result/certification records, (iii) supplier secure-development procedures via externally-assessable interpretation (questionnaire / contract clause / third-party attestation); Art. 21(3) sentence 2 EU-level coordinated assessment outputs (Cooperation Group + Commission + ENISA under Art. 22(1)) are ingested in supplier-risk decisions; in DORA overlap (financial entity = NIS 2 essential entity), DORA Art. 30 9-element ICT-contract list satisfies NIS 2 contractual-security floor (DORA-exceeds-NIS 2); the GDPR DPA layer adds data-protection-specific clauses when controller-NSIE combined; CRA Art. 13(6) component-vulnerability reporting provides the upstream post-contract feedback path (NIS2↔CRA lifecycle hinge) without converting CRA into DPA-style contract; verified by supplier-contractual-security matrix review + Art. 21(3) three-prong per-supplier assessment evidence inspection + GV.SC-04 audit/test-result records review + Art. 22 EU-level coordinated-assessment inputs integration evidence + CSIRT-or-competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 5 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-06.4 Third-Party Boundary Management

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| CRA third-party boundary management preserves product-compliance accountability across ... | CRA | sufficient | - | low |

### D-06.4 · CRA · subso SO-D-06.4.CRA
- **Objective**: CRA third-party boundary management preserves product-compliance accountability across EU/non-EU and supply-chain actor boundaries: a non-EU manufacturer may appoint an authorised representative by written mandate, but core manufacturer obligations remain non-delegable; an importer or distributor that places a product under its own name/trademark or substantially modifies it becomes manufacturer-equivalent; a third party that substantially modifies a product becomes the manufacturer for the affected part (or the entire product if the modification affects the whole product's cybersecurity); economic operators maintain upstream/downstream identification records and provide them to MSAs on reasoned request, retaining the supply-chain information for 10 years.
- **Anchors listed**:
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third party') in objective maps to GV.SC-02
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Art. 18 written authorised representative mandate + Art. 21 own-name/trademark manufac... | CRA | sufficient | - | high |

### D-06.4 · CRA · req 6.4.3
- **Title**: "Art. 18 written authorised representative mandate + Art. 21 own-name/trademark manufacturer-equivalent + Art. 22 third-party substantial-modification manufacturer-status + Art. 23 10-year upstream/downstream economic-operator identification log"
- **Description**: The product shall preserve CRA product-compliance accountability across EU/non-EU and supply-chain actor boundaries — Art. 18 written authorised representative mandate (non-EU manufacturer may appoint AR in writing, with non-delegable manufacturer obligations remaining on the manufacturer; single-entity may also be GDPR Art. 27 representative only with separately documented mandates and recipient channels); Art. 21 own-name/trademark manufacturer-equivalent trigger (importer or distributor placing a product under own name/trademark, or modifying it in a way that may affect compliance with the CRA, becomes manufacturer-equivalent); Art. 22 substantial-modification rule (third party that substantially modifies a product becomes the manufacturer for the affected part, or for the entire product if the modification affects the whole product's cybersecurity); Art. 23 10-year upstream/downstream economic-operator identification log (economic operators maintain identification records and provide them to MSAs on reasoned request, retaining supply-chain information for 10 years) — CRA AR mandate is NOT a GDPR Art. 27 representative or a DORA Art. 30(3)(e) audit-right.
- **Fit criterion (prose)**: A CRA economic-operator boundary matrix is maintained per non-EU manufacturer / importer / distributor / substantial-modifier with explicit boundary-mechanism separation: Art. 18 authorised representative mandate is documented per non-EU manufacturer with written mandate text, AR establishment-on-Union-territory record, AR delegation-by-manufacturer scope (NOT core manufacturer obligations), AR obligation-set (Art. 30 RoPA leg + Annex VII technical-documentation access + MSA cooperation on reasoned request); Art. 21 own-name/trademark manufacturer-equivalent trigger is operated as an own-name-placement event log + intended-purpose-modification assessment + manufacturer-equivalent-status register per importer or distributor; Art. 22 substantial-modification rule is operated as a substantial-modification event log with criterion criteria (consequence-not-considered-in-initial-assessment + obliges-the-manufacturer-to-ensure-the-product-remains-compliant-with-CRA + may-affect-the-whole-product-cybersecurity) per substantial modifier, with affected-part OR entire-product manufacturer-status designation per substantial-modification scope; Art. 23 10-year upstream/downstream economic-operator identification log is maintained with economic-operator records (name, contact, role, identification details, supply-chain position) and is provided to MSAs on reasoned request with 10-year retention; non-delegable manufacturer obligations (per Art. 18 carve-out in the AR-mandate standard text — typically conformance-assessment responsibilities, technical-documentation-keeping, incident-handling under Art. 14, vulnerability-handling under Art. 13) remain on the manufacturer regardless of AR mandate; the CRA AR does NOT replace the GDPR Art. 27 representative — one handles data-protection correspondence (DPA, data subjects) and one handles product-compliance technical-documentation/MSA cooperation; the CRA AR does NOT replace the DORA CIF audit-rights — CRA is upstream traceability; DORA is downstream audit; verified by AR-mandate register review + own-name-placement event log audit + substantial-modification event log audit + 10-year economic-operator identification log spot-check + non-delegable-obligations retention attestation + MSA inspection-ready evidence pack on request + GDPR-DPA-recipient separation attestation when AR-and-GDPR-representative dual-role.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — Action keyword ('third party') in objective maps to GV.SC-02
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Contractual arrangements concerning critical or important functions grant the financial... | DORA | sufficient | - | high |

### D-06.4 · DORA · subso SO-D-06.4.DORA
- **Objective**: Contractual arrangements concerning critical or important functions grant the financial entity, an appointed third party, and the competent authority unrestricted rights of access, inspection, and audit over the ICT third-party service provider, including on-site copying of relevant documentation where critical to provider operations; those rights must not be impeded or limited by other contractual arrangements or implementation policies, and alternative assurance levels may be agreed only where other clients' rights are affected.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - DE.CM-06 — External service provider activities and services are monitored to find potentially adverse events — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights (including on-si... | DORA | sufficient | - | high |

### D-06.4 · DORA · req 6.4.4
- **Title**: "Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights (including on-site documentation copy right) for financial entity / appointed third party / competent authority over CIF-supporting ICT third-party providers, with narrowly bounded alternative-assurance exception only where other clients' rights are affected"
- **Description**: The product shall operate Art. 30(3)(e)(i)/(ii) unrestricted access / inspection / audit rights over ICT third-party service providers for contractual arrangements concerning critical or important functions, extending to financial entity / appointed third party / competent authority and including the on-site documentation-copy right where critical to provider operations; those rights must NOT be impeded or limited by other contractual arrangements or implementation policies; alternative-assurance levels may be agreed only where other clients' rights are affected; DORA CIF audit-rights extend beyond NIS 2 direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth); CIF audit-rights do NOT replace CRA Art. 23 economic-operator identification (different direction).
- **Fit criterion (prose)**: A CIF audit-rights framework is operated per CIF-supporting ICT third-party service-provider relationship covering (i) financial-entity access / inspection / audit right exercised directly or through an appointed third party, (ii) competent-authority access / inspection / audit right, (iii) on-site documentation-copy right where critical to provider operations, with (iv) alternative-assurance-levels qualification applied only where other clients' rights are affected — the alternative-assurance exception is narrowly bounded and does not replace the primary audit-right (alternative is documented justification for the affected scope only); the CIF audit-rights contractually anchored via the Art. 30(3)(e)(i) + (ii) clauses (D-06.3 DORA cross-ref), and must not be impeded or limited by other contractual arrangements (e.g., NDAs with shared providers, sub-outsourcing restrictions by upstream ICT providers) or by implementation policies (e.g., provider-internal audit-on-demand-only schedules); the CIF audit-rights are exercised through documented audit procedures covering audit-scope alignment, audit-finding artefact transport, audit-finding acceptance criteria, audit-finding remediation tracking per the financial entity's risk-management framework; in NIS 2 overlap (financial entity is also NIS 2 entity), the CIF audit-rights extend beyond the NIS 2 Art. 21(2)(d) direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth) and reach into critical provider chains beyond direct providers; in CRA overlap, economic-operator identification (Art. 23, D-06.4 CRA leg) and CIF audit-rights (Art. 30(3)(e), DORA leg) point in different directions but compose where a CRA-classified product is supplied to a financial entity through importer/distributor channels; in GDPR overlap (non-EU CIF-supporting ICT provider falls under Art. 3(2)), the GDPR Art. 27 representative address coexists with the CIF audit-right, NOT substitute (the two mechanisms operate at distinct boundaries); verified by CIF audit-rights framework documentation review + Art. 30(3)(e)(i)/(ii) audit-exercise record audit + alternative-assurance-exception narrowly-bounded application review + on-site documentation-copy right exercise evidence + Art. 30(3) audit-clause contractual backing attestation + national-financial-supervisory-authority-or-competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - DE.CM-06 — External service provider activities and services are monitored to find potentially adverse events — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Non-EU controllers and processors falling under GDPR Art. 3(2) designate a representati... | GDPR | sufficient | - | high |

### D-06.4 · GDPR · subso SO-D-06.4.GDPR
- **Objective**: Non-EU controllers and processors falling under GDPR Art. 3(2) designate a representative in writing in the Union unless the Art. 27(2) exception applies; the representative is the legal-address and accountability anchor for supervisory-authority and data-subject contact.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/GDPR_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - GV.OC-02 — Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risk management are understood and considered — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Art. 27(1) written Union representative designation for non-EU controllers/processors ... | GDPR | sufficient | - | high |

### D-06.4 · GDPR · req 6.4.1
- **Title**: "Art. 27(1) written Union representative designation for non-EU controllers/processors under Art. 3(2), subject to Art. 27(2) occasional / low-risk / public-authority exceptions"
- **Description**: The product shall ensure that non-EU controllers and processors falling under GDPR Art. 3(2) (offering goods/services to EU data subjects or monitoring behaviour in the Union) designate in writing a representative in the Union, subject only to the narrow Art. 27(2) occasional / low-risk / public-authority exceptions — the representative is the legal-address and accountability anchor for supervisory-authority and data-subject contact; in CRA overlap (same non-EU entity is also CRA manufacturer), the GDPR representative does NOT replace the CRA authorised representative — single legal entity may perform both roles only if both mandates and recipient channels are separately documented.
- **Fit criterion (prose)**: An Art. 27 written-Union-representative discipline is operated per non-EU controller/processor falling under Art. 3(2) with no Art. 27(2) exception; each designated representative maintains a written mandate, a Union address, an establishment-on-Union-territory-of-business record, a designated data-subject and supervisory-authority contact function, and a documented articulation of representative obligations (Art. 30(2) RoPA reference, Art. 58(1) DPA cooperation, Art. 13/14 information-clause identification); the Art. 27(2) occasional / low-risk / public-authority exception is applied per non-EU controller/processor only with documented exception-eligibility assessment (processing occasional + low-risk + no special-category data + no large-scale systematic monitoring — typically meets all four limbs cumulatively to engage the exception; an Art. 27(2)(a)–(c) reading is rejected as insufficient, the exception requires the exceptional-low-risk threshold); the GDPR representative designation does NOT replace the CRA authorised representative — in CRA overlap, the single legal entity may perform both roles only if both mandates and recipient channels are separately documented (data-protection correspondence vs product-compliance technical-documentation/MSA cooperation); in DORA overlap (non-EU ICT provider is CIF-supporting for a financial entity and falls under Art. 3(2)), the GDPR representative address coexists with DORA contractual audit/access rights, not substitute; verified by representative designation register review + Art. 27(2) exception-eligibility assessment audit + representative written-mandate inspection + DPA inspection-ready evidence pack on request + CRA-AR-mandate separate-documentation attestation when CRA overlap (or single-entity dual-role mandate split with separately documented recipient channels).
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/GDPR_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - GV.OC-02 — Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risk management are understood and considered — **CORE** — CSF title shares 2 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| NIS 2 boundary management is split across cross-border notification routing and entity-... | NIS2 | sufficient | - | low |

### D-06.4 · NIS2 · subso SO-D-06.4.NIS2
- **Objective**: NIS 2 boundary management is split across cross-border notification routing and entity-side supplier-scope control: for incidents affecting two or more Member States, CSIRTs, competent authorities, and SPOCs route information to other affected Member States and ENISA; for supply-chain boundaries, the Art. 21(2)(d) `direct` supplier/service-provider scope-limiter defines which third parties sit inside the entity's NIS 2 supplier-security perimeter, and Art. 22 coordinated supply-chain risk-assessment outputs feed into supplier decisions where available.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('incidents') with objective; reinforces but is not the direct action
  - GV.SC-05 — Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties — **CORE** — CSF title shares 5 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Art. 23(6)/(8) cross-MS SPOC / CSIRT / ENISA notification routing + Art. 21(2)(d) `dir... | NIS2 | sufficient | - | low |

### D-06.4 · NIS2 · req 6.4.2
- **Title**: "Art. 23(6)/(8) cross-MS SPOC / CSIRT / ENISA notification routing + Art. 21(2)(d) `direct` supplier/service-provider scope register + Art. 22 coordinated supply-chain risk-assessment ingestion"
- **Description**: The product shall split NIS 2 third-party boundary management across two boundary mechanisms — (a) cross-border incident-flow routing for significant incidents affecting two or more Member States per Art. 23(6) (SPOC designation, CSIRT/competent-authority routing, notification to other affected Member States and ENISA where appropriate) and Art. 23(8) (single-window notification and cooperation); and (b) entity-level direct-supplier/service-provider boundary under Art. 21(2)(d) `direct` scope-limiter (with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56), with Art. 22 EU-level coordinated supply-chain risk-assessment outputs ingested where available — NIS 2 `direct` scope determines entity liability; DORA CIF audit rights (Art. 30(3)(e)) extend the boundary layer for financial entities.
- **Fit criterion (prose)**: A two-track NIS 2 boundary matrix is maintained with explicit separation of (Track-1) cross-MS routing and (Track-2) direct-supplier-scope register: Track-1 cross-MS routing covers each significant incident affecting 2+ Member States via SPOC designation per Art. 23(6)/(8), CSIRT-and-competent-authority notification forwarding, ENISA notification where Art. 23(8)(b) cooperation framework applies, and recorded affected-MS notification routing with timestamps; Track-2 direct-supplier scope covers each in-scope direct supplier / service-provider under Art. 21(2)(d) `direct` scope-limiter with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56 risk-management-precaution principle (the THREE materially distinct readings R1/R2/R3 are PRESERVED with R1 as minimum + R2/R3 added per Recital 56; Member-State-transposition divergence: German BSI favours R1+R3, French ANSSI favours R2+R3, both may signal forthcoming n-hop obligations in critical sectors), with Art. 22 coordinated supply-chain risk-assessment outputs (Cooperation Group + Commission + ENISA under Art. 22(1)) ingested in supplier-scope decisions; the two tracks feed the cross-domain D-06.3 supplier-contract matrix (Art. 21(2)(d) supplier contracts) and the cross-domain risk-assessment record; in DORA overlap, DORA Art. 30(3)(e) CIF audit-rights extend the boundary layer for financial entities beyond the direct-supplier floor (DORA-exceeds-NIS 2 in audit-rights depth); in CRA overlap, CRA Art. 22 substantial-modification and Art. 23 economic-operator identification operate at distinct boundaries (CRA determines manufacturer-status; NIS 2 determines entity supplier liability); verified by SPOC routing log review + CSIRT-and-competent-authority notification forwarding record audit + cross-MS routing timestamps inspection + direct-supplier-scope register audit + Art. 22 EU-level coordinated-assessment inputs integration evidence + CSIRT-or-competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-06_Supply-Chain/D-06.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **CORE** — CSF title literally matches action keyword ('supplier')
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-05 — Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties — **CORE** — CSF title shares 6 action tokens with objective
  - ID.AM-04 — Inventories of services provided by suppliers are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-02 — Cyber threat intelligence is received from information sharing forums and sources — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-07.1 Secure-by-Design Principles

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are designed and developed in such a way that they achieve an appr... | AI_Act | excessive | - | high |

### D-07.1 · AI_Act · subso SO-D-07.1.AIACT
- **Objective**: High-risk AI systems are designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle (Art. 15(1) AI Act).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06, ID.RA-01 — literal duplicate(s) of PR.PS-06, ID.RA-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "High-risk AI systems designed and developed to achieve appropriate level of accuracy, ... | AI_Act | sufficient | - | high |

### D-07.1 · AI_Act · req 7.1.5
- **Title**: "High-risk AI systems designed and developed to achieve appropriate level of accuracy, robustness, and cybersecurity, performing consistently throughout their lifecycle, with QMS covering design/design-control/design-verification"
- **Description**: The product shall ensure that high-risk AI systems are designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and perform consistently in those respects throughout their lifecycle, with a Quality Management System implemented in a systematic and orderly manner covering at least 13 enumerated aspects including techniques, procedures and systematic actions for the design, design control and design verification of the high-risk AI system (AI Act Art. 15(1) + Art. 17(1) + Art. 17(1)(c) + Art. 17(1)(g) cross-reference to Art. 9 risk-management-system documentation).
- **Fit criterion (prose)**: A documented Art. 15(1) accuracy+robustness+cybersecurity baseline is maintained with lifecycle consistency (`perform consistently in those respects throughout their lifecycle`); the baseline is calibrated to `appropriate level` per the intended purpose + conditions of use; an Art. 17(1) Quality Management System is documented in `systematic and orderly manner` (POLY — ISO 9001 / ISO/IEC 23053 / internal bespoke) in the form of written policies, procedures and instructions; the QMS covers all 13 enumerated aspects (a)–(m) per Art. 17(1) including Art. 17(1)(c) `design, design control and design verification` 3-way AND; Art. 17(1)(g) cross-references Art. 9 risk-management-system documentation; the by-design outputs feed Annex IV technical documentation (per Art. 11 + Art. 12(2)) which is the technical-documentation evidence base; the Art. 15(4)–(5) AI-attack-defence categories (6 categories: data poisoning + model poisoning + adversarial examples + model evasion + confidentiality attacks + model flaws) are addressed as AI-specific attack-resistance obligations that do not substitute for CRA Annex I Part I (2)(j) attack-surface limitation or (2)(k) exploitation-mitigation outcomes on AI-enabled CRA products; AI Act Recital 78 explicitly preserves GDPR — for a high-risk AI system processing personal data, AI Act Art. 15(1) + QMS design/design-control/design-verification stacks with GDPR Art. 25(1) data-protection by-design as distinct design outputs (AI-system property vs privacy property); the by-design risk-assessment obligation on AI-enabled CRA products is satisfied by AI Act Art. 9 + Art. 17 risk-management-system documentation (per CRA Art. 13(4) sentence 2 explicit AI-Act-substitution carve-out for risk assessment); verified by Art. 15(1) accuracy+robustness+cybersecurity baseline documentation review + lifecycle-consistency evidence audit + Art. 17(1) QMS systematic-and-orderly-manner documentation inspection + Art. 17(1)(c) design/design-control/design-verification sub-record review + Art. 9 risk-management-system documentation cross-reference + Art. 15(4)–(5) AI-attack-defence measures record (for AI/ML-specific attacks) + Annex IV technical-documentation audit + provider + MSA + AI Office inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| When placing a product with digital elements on the market, the manufacturer ensures th... | CRA | excessive | - | high |

### D-07.1 · CRA · subso SO-D-07.1.CRA
- **Objective**: When placing a product with digital elements on the market, the manufacturer ensures that it has been designed, developed and produced in accordance with the essential cybersecurity requirements set out in Part I of Annex I (Art. 13(1) CRA), with the cybersecurity risk assessment propagated across the 6 lifecycle phases (planning, design, development, production, delivery, maintenance) per Art. 13(2) chapeau + sentence 1, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact (Art. 13(2) sentence 2).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06 — literal duplicate(s) of PR.PS-06
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product with digital elements designed, developed and produced in accordance with Anne... | CRA | sufficient | - | low |

### D-07.1 · CRA · req 7.1.3
- **Title**: "Product with digital elements designed, developed and produced in accordance with Annex I Part I essential cybersecurity requirements with risk assessment propagated across planning, design, development, production, delivery and maintenance"
- **Description**: The product shall be designed, developed and produced in accordance with the essential cybersecurity requirements set out in Annex I Part I, with the cybersecurity risk assessment taken into account across the planning, design, development, production, delivery and maintenance phases of the product, with a view to minimising cybersecurity risks, preventing incidents, and minimising their impact including in relation to the health and safety of users (CRA Art. 13(1) + Art. 13(2) chapeau + sentence 1 + sentence 2 + Annex I Part I chapeau + Annex VII §2 + Annex VII §3).
- **Fit criterion (prose)**: The product by-design discipline conforms to Annex I Part I essential cybersecurity requirements across the 11 sub-points (a)–(k) including attack-surface limitation (2)(j) + exploitation mitigation (2)(k) + automatic security updates (2)(c) + integrity protection (2)(f) + data-minimisation (2)(g) + resilience+availability (2)(h) + cascading-impact minimisation (2)(i) + recording-and-monitoring (2)(l); a documented cybersecurity risk assessment per Art. 13(2) is propagated across the 6 lifecycle phases (planning / design / development / production / delivery / maintenance) with the assessment comprising at least the analysis of risks based on intended purpose and reasonably foreseeable use (including operational environment, assets to be protected, expected lifetime) per Art. 13(3) sentence 2, indicating whether and in what manner the Annex I Part I (2) requirements apply and how they are implemented per Art. 13(3) sentence 3; the risk assessment is documented in the Annex VII §3 technical documentation and updated when there is a change of risk represented by the product per Art. 13(3) sentence 1; Annex VII §2 design/development documentation forms the technical-documentation evidence base; the support period is determined in accordance with Art. 13(8) with ≥ 5 years expected per sentence 3; Annex II information accessibility is maintained for 10 years per Art. 13(18); for an integrated manufacturer-controller-deployer, the CRA-side Annex I Part I product by-design discharges the engineering substrate while GDPR Art. 25(1) controller-side by-design discharges the personal-data overlay; for an AI-enabled CRA product, CRA Art. 13(4) sentence 2 explicit AI-Act-substitution for risk assessment permits a unified risk assessment under AI Act Art. 9 to substitute for the CRA risk assessment when both apply (per SR-CRA-066); verified by Annex I Part I (2) sub-point evidence per product class + Annex VII §2 design/development documentation review + Annex VII §3 risk-assessment record audit + 6-phase risk-assessment-propagation records inspection + Art. 13(3) sentence 1 update-on-change-of-risk record + Art. 13(8) support-period record + Art. 13(18) 10-year information-accessibility record + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md` (Art. 10) — paraphrased action
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities establish a sound network and infrastructure management structure us... | DORA | sufficient | - | high |

### D-07.1 · DORA · subso SO-D-07.1.DORA
- **Objective**: Financial entities establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols (Art. 9(4)(b) DORA) with appropriate and comprehensive documented policies for patches and updates maintained (Art. 9(4)(f)).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Sound network and infrastructure management structure with appropriate techniques/meth... | DORA | partial | PR.PS-02 | high |

### D-07.1 · DORA · req 7.1.4
- **Title**: "Sound network and infrastructure management structure with appropriate techniques/methods/protocols, patch and update policies, and secure-by-design operationalised via change-management six-step + testing programme (DORA partial — no OJ dedicated by-design mandate)"
- **Description**: The product shall establish a sound network and infrastructure management structure using appropriate techniques, methods and protocols with appropriate and comprehensive documented policies for patches and updates, with the secure-by-design dimension operationalised through documented ICT change-management policies, procedures and controls for software, hardware, firmware components, systems or security parameters that are recorded, tested, assessed, approved, implemented and verified in a controlled manner, based on a risk assessment approach, supported by the Art. 24 ICT risk-management testing programme (DORA Art. 9(4)(b) + Art. 9(4)(f) + Art. 9(4)(e) + Art. 24 — partial at D-07.1; no OJ-mandated dedicated by-design clause).
- **Fit criterion (prose)**: A documented Art. 9(4)(b) network-and-infrastructure-management structure is maintained using appropriate techniques, methods and protocols; documented Art. 9(4)(f) patch-and-update policies are maintained appropriate and comprehensive per the risk profile; the secure-by-design dimension is operationalised through the Art. 9(4)(e) ICT change-management six-step (recorded / tested / assessed / approved / implemented / verified in a controlled manner, based on a risk assessment approach) covering all change targets (software / hardware / firmware components / systems / security parameters) per SR-DORA-023; the Art. 24 ICT risk-management testing programme is operated with the 12-way open testing-modality list including vulnerability assessments, scans, source-code reviews where feasible, scenario-based tests, penetration testing, end-to-end testing, performance testing, compatibility testing, etc.; the by-design architecture integrates with Art. 6(1) ICT risk-management framework + Art. 5(2)+(4) management-body responsibility for the ICT risk-management framework; for a DORA-only entity that is not a CRA manufacturer and does not process personal data via high-risk AI, by-design compliance is demonstrated through the change-management six-step + testing programme outputs, with no standalone OJ-mandated by-design obligation; for a DORA FE that is also a CRA manufacturer, the upstream CRA-side Annex I Part I product by-design feeds the downstream DORA-side change-management six-step + testing; for a DORA FE that is also a controller processing personal data, the controller-side GDPR Art. 25(1) data-protection by-design sits on top of the DORA-side change-management six-step + testing; verified by Art. 9(4)(b) infrastructure-management structure records review + Art. 9(4)(f) patch-policy records audit + Art. 9(4)(e) change-management six-step records inspection (each ICT change shows recorded / tested / assessed / approved / implemented / verified) + Art. 24 testing-programme records review (each of the 12 modalities documented) + Art. 6(1) ICT risk-management-framework record + Art. 5(2)+(4) management-body responsibility record + national CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: partial (1 potential missing anchor(s))
- **Missing (1)**: PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — Article maps PR.PS-02 for action keyword 'patch' present in objective
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The controller implements appropriate technical and organisational measures — such as p... | GDPR | excessive | - | high |

### D-07.1 · GDPR · subso SO-D-07.1.GDPR
- **Objective**: The controller implements appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles, such as data minimisation, in an effective manner and to integrate the necessary safeguards into the processing (Art. 25(1) GDPR), and ensures that by default only personal data which are necessary for each specific purpose are processed (Art. 25(2) GDPR).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06, ID.AM-08 — literal duplicate(s) of PR.PS-06, ID.AM-08
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personal-data processing implements data-protection principles via appropriate technic... | GDPR | sufficient | - | high |

### D-07.1 · GDPR · req 7.1.1
- **Title**: "Personal-data processing implements data-protection principles via appropriate technical and organisational measures designed into the means of processing, with by-default limits on amount, extent, storage period and accessibility"
- **Description**: The product shall implement appropriate technical and organisational measures — such as pseudonymisation — which are designed to implement data-protection principles (such as data minimisation) in an effective manner and to integrate the necessary safeguards into the processing at the time of means-determination and at the time of the processing itself, and shall ensure that by default only personal data which are necessary for each specific purpose are processed (GDPR Art. 25(1) + Art. 25(2)).
- **Fit criterion (prose)**: A documented Art. 25(1) by-design necessity assessment is maintained for each processing activity, applying the 4-factor qualitative proportionality (state of the art + cost of implementation + nature/scope/context/purposes of processing + risks of varying likelihood and severity); the by-design decisions include pseudonymisation, minimisation, encryption, and by-default safeguards integrated at the time of means-determination; an Art. 25(2) by-default operational implementation is maintained covering the amount of personal data collected, the extent of processing, the period of storage, and the accessibility of the data — operationalised through minimal-data-collection pipelines, minimal-access, minimal-storage-periods, and minimal-scope-of-processing controls; the by-design and by-default pair forms a 2-tier architecture: by-design is the architectural decision record; by-default is the operational implementation; decisions are documented in a necessity assessment often via DPIA per Art. 35(7) and demonstrated to the DPA under Art. 5(2) accountability + Art. 30 RoPA on processing purposes and safeguards + Art. 24(1) responsibility of the controller; for an integrated manufacturer-controller-deployer, the controller-side GDPR Art. 25(1) by-design sits on top of the upstream CRA-side Annex I Part I product-cybersecurity by-design (the manufacturer has done CRA Art. 13(1) product by-design); the GDPR Art. 25(1) by-design outputs (pseudonymised-by-default pipelines, minimisation-by-default) are propagated downstream to D-07.2 (Secure Coding Practices) as the code-level instruction and D-07.3 (CI/CD Pipeline Security) as the delivery-path instruction; verified by Art. 25(1) necessity-assessment records review + Art. 25(2) by-default operational-implementation evidence inspection + 4-factor proportionality calibration records review + Art. 30 RoPA entries + Art. 35(7) DPIA content items (when DPIA required) + Art. 5(2) accountability record + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md` (Art. 25) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Essential and important entities take appropriate and proportionate technical, operatio... | NIS2 | excessive | - | high |

### D-07.1 · NIS2 · subso SO-D-07.1.NIS2
- **Objective**: Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) NIS 2).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/NIS2_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
  - GV.SC-02 — Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06, PR.PS-02 — literal duplicate(s) of PR.PS-06, PR.PS-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Security integrated into the acquisition, development and maintenance of network and i... | NIS2 | sufficient | - | low |

### D-07.1 · NIS2 · req 7.1.2
- **Title**: "Security integrated into the acquisition, development and maintenance of network and information systems across the 3-phase coordinated lifecycle with vulnerability handling and disclosure"
- **Description**: The product shall take appropriate and proportionate technical, operational and organisational measures to ensure security in the acquisition, development and maintenance of network and information systems, including vulnerability handling and disclosure, with the three coordinated lifecycle phases operationalised through supplier SDLC assessment at acquisition, in-house secure-by-design decisions at development, and vulnerability handling+disclosure + patch-management + change-management at maintenance (NIS 2 Art. 21(2)(e) + Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor).
- **Fit criterion (prose)**: A documented 3-phase NIS 2 lifecycle (acquisition / development / maintenance) is maintained with: (1) **acquisition phase** — supplier-SDLC assessment per Art. 21(3) sentence 1 supplier-secure-development-procedures three-prong (SR-NIS2-026), with supplier-by-design evidence records retained; (2) **development phase** — in-house secure-by-design decisions documented per SR-NIS2-027 covering threat modelling, secure-by-design choices, secure-coding standards, code review, security testing (mapped to PR.PS-06) and component selection / dependency hygiene / update channels (mapped to PR.PS-02); (3) **maintenance phase** — vulnerability handling+disclosure with CSIRT-coordinated disclosure channel per Art. 12(1) (mapped to ID.RA-01) and patch + configuration + replacement cadence commensurate with risk (mapped to PR.PS-02); the 3-phase architecture has explicit hand-offs at the acquisition gate (supplier → entity), the development gate (in-house design decisions), and the maintenance gate (vulnerability discovery → validation → record → response); Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor + Recital 56 cost-of-implementation qualifier governs the depth and scope; Art. 20(1) management-body approval + oversight + liability is the upstream governance instrument; for an integrated controller-NSIE, the NIS 2 acquisition-phase supplier SDLC assessment realises the GDPR Art. 25(1) controller-side by-design outputs (pseudonymised-by-default pipelines, minimisation-by-default) at the procurement gate; verified by supplier-SDLC assessment records review + in-house secure-by-design-decision records inspection + vulnerability handling-and-disclosure records review + maintenance + patch-cadence records audit + Art. 20(1) management-body approval record + management body + competent authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.1/articles/AI_Act_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('patch') in objective maps to PR.PS-02
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (default)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-07.2 Secure Coding Practices

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are designed and developed with appropriate technical and organisa... | AI_Act | excessive | - | high |

### D-07.2 · AI_Act · subso SO-D-07.2.AIACT
- **Objective**: High-risk AI systems are designed and developed with appropriate technical and organisational measures to enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws (Art. 15(4)–(5) AI Act).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - RS.MI-01 — Incidents are contained — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - RS.MA-03 — Incidents are categorized and prioritized — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06, ID.RA-01 — literal duplicate(s) of PR.PS-06, ID.RA-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "High-risk AI systems designed and developed to effectively resist, as appropriate to p... | AI_Act | sufficient | - | high |

### D-07.2 · AI_Act · req 7.2.3
- **Title**: "High-risk AI systems designed and developed to effectively resist, as appropriate to purpose and conditions of use, attempts at training-data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks or model flaws"
- **Description**: The product shall ensure that high-risk AI systems are designed and developed with appropriate technical and organisational measures to enable the AI systems to effectively resist, as appropriate to the AI system's purpose and conditions of use, attempts to manipulate the training data set (data poisoning) or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws (AI Act Art. 15(4)–(5)).
- **Fit criterion (prose)**: A documented Art. 15(4) attack-defence baseline is maintained for the 6 AI/ML-specific attack categories: (1) **data poisoning** — defence against manipulation of the training data set, including input-validation + data-provenance checks + training-data sanitisation + anomaly-detection on training-set distribution; (2) **model poisoning** — defence against manipulation of pre-trained components, including supply-chain integrity for pre-trained components + signed-model checksums + pre-training-component provenance verification; (3) **adversarial examples** — defence against inputs designed to cause the AI model to make a mistake, including adversarial-input detection + input-preprocessing hardening + adversarial-robustness training; (4) **model evasion** — defence against adversarial-example-induced evasion, including evasion-aware model-update cadence + detection-of-evasion-attempt signals; (5) **confidentiality attacks** — defence against attacks on confidentiality of training data, parameters, or outputs, including differential-privacy training + model-parameter access controls + output-redaction discipline + membership-inference resistance; (6) **model flaws** — defence against vulnerabilities or weaknesses inherent in model architecture or training process, including architecture-review discipline + known-flaw catalogue + flaw-driven model-update cadence; the baseline is calibrated to `appropriate to the AI system's purpose and conditions of use` (Art. 15(4) proportionality qualifier) — informed by intended purpose (cross to D-09.2 — SO-AIACT-001 Art. 9 risk-management-system) and conditions of use (operational environment + reasonably foreseeable use); the Art. 15(4)–(5) AI-attack-defence categories are AI/ML-specific and do NOT map to conventional secure-coding mandates (no general coding-standards prescription in AI Act — the AI Act addresses AI-attack-defence, not conventional coding practices); the AI-attack-defence coding-practices baseline is built from AI/ML-specific frameworks (NIST AI RMF, ISO/IEC 23894, MITRE ATLAS) and demonstrated against the 6 Art. 15(4)–(5) attack-defence categories via the QMS + Annex IV documentation; AI-Act-Recital 78 GDPR preservation operates at the AI-system side for high-risk AI systems processing personal data — the AI-Act-side AI-attack-defence does NOT substitute for the GDPR Art. 25(1) data-protection by-design; the GDPR-side by-design is layered on top via the controller-means-determination + processing-time by-default; for AI-enabled CRA products (CRA-regulated product that embeds a high-risk AI system), AI Act Art. 15(4)–(5) AI-attack-defence stacks with CRA Annex I Part I (2)(j) attack-surface + (2)(k) exploitation-mitigation — the two regimes DO NOT substitute (AI Act defence categories do not substitute for CRA's outcome-level obligations, and vice versa); **no OJ-level consolidation rule exists** for the coding-practices dimension (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices); verified by Art. 15(4) 6-category AI-attack-defence measures record review + Art. 15(4) proportionality calibration records (purpose + conditions of use) + QMS design-control record (Art. 17(1)(c) — design/design-control/design-verification) + Annex IV technical-documentation audit + Art. 9 risk-management-system documentation cross-reference + provider + MSA + AI Office inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The manufacturer designs, develops, and produces the product with digital elements to l... | CRA | excessive | - | low |

### D-07.2 · CRA · subso SO-D-07.2.CRA
- **Objective**: The manufacturer designs, develops, and produces the product with digital elements to limit its attack surfaces, including attack surfaces of external interfaces (Annex I Part I (2)(j) CRA), and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (Annex I Part I (2)(k) CRA).
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-02 — literal duplicate(s) of PR.PS-02
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Product with digital elements designed, developed and produced to limit attack surface... | CRA | sufficient | - | low |

### D-07.2 · CRA · req 7.2.1
- **Title**: "Product with digital elements designed, developed and produced to limit attack surfaces (including external interfaces) and to reduce incident impact via exploitation-mitigation mechanisms and techniques"
- **Description**: The product shall be designed, developed and produced to limit its attack surfaces — including attack surfaces of external interfaces — and to reduce the impact of an incident using appropriate exploitation-mitigation mechanisms and techniques (CRA Annex I Part I (2)(j) + Annex I Part I (2)(k) + Art. 13(1) + Art. 13(2) risk-assessment propagation across 6 lifecycle phases).
- **Fit criterion (prose)**: A documented attack-surface-limitation discipline is maintained per Annex I Part I (2)(j) — minimum-necessary external interfaces (default-closed port suppression, surface-area-baselining), minimum-necessary attack surfaces, minimum-necessary exploitable paths; configuration-management practices are established, documented, and applied to assets per PR.PS-01 with default-closed external interfaces and surface-area-baselining; software is maintained commensurate with risk per PR.PS-02 with risk-assessment-driven attack-surface reduction per Art. 13(2) 6-phase risk-assessment propagation; a documented exploitation-mitigation discipline is maintained per Annex I Part I (2)(k) — appropriate mechanisms and techniques to reduce the impact of an incident (ASLR, DEP/NX, stack canaries, control-flow integrity / CFI, sandboxing, secure enclaves, configuration hardening, principle of least privilege at process level) commensurate with risk per Art. 13(2) risk assessment; the SDLC-process evidence in the technical documentation under Annex VII §2 shows which mitigation mechanisms are in scope for the product and how they are configured; Annex VII §3 risk-assessment record documents the attack-surface + exploitation-mitigation risk-assessment outputs; the coding-practices evidence base is built from industry frameworks (NIST SSDF + OWASP SAMM + ISO/IEC 27034) since OJ Annex I Part I (2)(j) + (2)(k) does NOT specify secure-coding standards (no coding-language-specific linting, no secure-coding-framework adoption prescription); the support period ≥ 5 years per Art. 13(8) sentence 3 is maintained with ongoing exploitation-mitigation updates + attack-surface monitoring + vulnerability remediation per Art. 13(6); for AI-enabled CRA products, CRA Annex I Part I (2)(j) + (2)(k) outcome-level obligations stack with AI Act Art. 15(4)–(5) attack-defence categories — **no OJ-level consolidation rule** exists for coding practices (unlike CRA Art. 13(4) sentence 2 unified-risk-assessment carve-out for AI Act Art. 9 risk assessment, which does NOT extend to coding practices); verified by Annex I Part I (2)(j) attack-surface-limitation evidence audit (default-closed interfaces, surface-area baseline) + Annex I Part I (2)(k) exploitation-mitigation mechanism inventory + Annex VII §2 design/development documentation review + Annex VII §3 risk-assessment record audit + 6-phase risk-assessment-propagation records inspection + Art. 13(6) vulnerability remediation records + Art. 13(8) support-period record + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.2/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('update') in objective maps to PR.PS-02
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 7 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities implement documented policies, procedures and controls for ICT chang... | DORA | excessive | - | low |

### D-07.2 · DORA · subso SO-D-07.2.DORA
- **Objective**: Financial entities implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters, that are based on a risk assessment approach, in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner (Art. 9(4)(e) DORA — 6-step change-management process).
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-06 — literal duplicate(s) of PR.PS-06
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified... | DORA | sufficient | - | low |

### D-07.2 · DORA · req 7.2.2
- **Title**: "ICT change-management six-step (recorded/tested/assessed/approved/implemented/verified) with implicit coding-dimension inference through tested/assessed legs and Art. 25 testing modalities (DORA partial — no OJ-mandated secure-coding-standards prescription; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary)"
- **Description**: The product shall implement documented policies, procedures and controls for ICT change management — covering changes to software, hardware, firmware components, systems or security parameters — that are based on a risk assessment approach, in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner, with the secure-coding dimension implicit through the `tested` and `assessed` legs of the change-management six-step and the Art. 25 testing modalities (DORA Art. 9(4)(e) — 6-step change-management process + Art. 25 testing programme; **partial at D-07.2, no OJ-mandated secure-coding-standards prescription**).
- **Fit criterion (prose)**: A documented Art. 9(4)(e) change-management policy is maintained covering all change targets (software / hardware / firmware components / systems / security parameters) with the 6-step process (recorded / tested / assessed / approved / implemented / verified in a controlled manner) based on a risk assessment approach; the secure-coding dimension for DORA is implicit through the `tested` and `assessed` legs of the change-management six-step + the Art. 25 testing modalities (12-way open testing-modality list: vulnerability assessments, scans, source code reviews where feasible, scenario-based tests, penetration testing, end-to-end testing, performance testing, compatibility testing, etc.) — source-code reviews where feasible serve as one modality for the secure-coding-dimension inference; the DORA-side participation at D-07.2 is **partial in the SR sense** — no OJ mandate prescribes secure-coding standards specifically; the DORA-side coding dimension is derived from the change-mgmt six-step's `tested` + `assessed` legs + the Art. 25 testing modalities; for a 5-FTE financial entity, the DORA-side coding dimension is demonstrated through (1) documented Art. 9(4)(e) change-management policies/procedures/controls with the 6-step process, (2) Art. 25 testing programme with the 12-way open testing-modality list, (3) Art. 11(3) response-and-recovery plans + Art. 11(2) backup-policies — NOT through an OJ-mandated secure-coding-standards prescription; the coding-standards baseline itself (NIST SSDF/OWASP SAMM/ISO/IEC 27034) is supplied by the entity's ICT risk-management-policy tier rather than by an OJ mandate; **P0 disagreement ON PARTICIPATION** (AEGIS taxonomy §4.1 marks DORA as SOLE AUTHORITY for D-07.2 but CRDA-deep finds no OJ-text support — Art. 9(4)(e) is change-management policy; Art. 9(4)(f) is patches-and-updates policy; no OJ clause prescribes secure-coding standards; SR-DORA-023 partial at D-07.2 by inference only, D-07.4 primary) — Layer 2 review item; verified by Art. 9(4)(e) change-management policy + procedure + control records review (each ICT change shows recorded / tested / assessed / approved / implemented / verified) + Art. 25 testing-programme records audit (each of the 12 modalities documented including source-code reviews where feasible) + Art. 11(3) response-and-recovery plan + Art. 11(2) backup-policy records inspection + national CA + ESA inspection-ready evidence pack on request.
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

## D-07.3 CI/CD Pipeline Security

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The manufacturer of a product with digital elements shall securely distribute updates f... | CRA | sufficient | - | low |

### D-07.3 · CRA · subso SO-D-07.3.CRA
- **Objective**: The manufacturer of a product with digital elements shall securely distribute updates for the product with digital elements in a timely manner, including, where appropriate, through automatic updates (Annex I Part II (7) CRA), and ensure that updates are disseminated free of charge, are clearly described, contain information on the security improvements and on the actions the user should take (Annex I Part II (8) CRA).
- **Anchors listed**:
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('update') in objective maps to PR.PS-02
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Product-side secure-update delivery evidence for CRA-regulated products" The product s... | CRA | sufficient | - | low |

### D-07.3 · CRA · req 7.3.2
- **Title**: "Product-side secure-update delivery evidence for CRA-regulated products"
- **Description**: The product shall maintain secure-update delivery evidence showing that CRA-regulated product updates are integrity-protected, disseminated through an approved channel, accompanied by release metadata, and retained as technical-documentation evidence for the support period.
- **Fit criterion (prose)**: For 100% of security updates, the update-delivery record contains artefact identifier, signature or equivalent integrity proof, distribution-channel identifier, advisory-message reference, user-action metadata, publication timestamp, support-period applicability, and technical-documentation retention reference.
- **Anchors listed**:
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('update') in objective maps to PR.PS-02
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| Essential and important entities take appropriate and proportionate technical, operatio... | NIS2 | excessive | - | low |

### D-07.3 · NIS2 · subso SO-D-07.3.NIS2
- **Objective**: Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure security in the maintenance of network and information systems, including vulnerability handling and disclosure (Art. 21(2)(e) third clause NIS 2).
- **Anchors listed**:
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-02, ID.RA-01 — literal duplicate(s) of PR.PS-02, ID.RA-01
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Entity-side deployment and maintenance pipeline evidence for network and information s... | NIS2 | sufficient | - | low |

### D-07.3 · NIS2 · req 7.3.1
- **Title**: "Entity-side deployment and maintenance pipeline evidence for network and information systems"
- **Description**: The product shall maintain release-path evidence showing that entity-side network-and-information-system maintenance releases are linked to vulnerability handling, disclosure intake, risk approval, deployment verification, and remediation tracking under the NIS2 maintenance perspective.
- **Fit criterion (prose)**: For 100% of in-scope maintenance releases, the pipeline record links the release identifier to a vulnerability register entry or scheduled maintenance item, risk assessment, approval actor, build or package identifier, deployment timestamp, post-deployment verification result, rollback decision, and management-body or delegated-control evidence reference.
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

## D-07.4 Change Management

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| The manufacturer of a product with digital elements that is part of a series of product... | CRA | sufficient | - | low |

### D-07.4 · CRA · subso SO-D-07.4.CRA
- **Objective**: The manufacturer of a product with digital elements that is part of a series of production ensures that procedures are in place for products with digital elements that are part of a series of production to remain in conformity with this Regulation (Art. 13(14) CRA).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('for') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('with') with objective; reinforces but is not the direct action
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **UTILITY** — CSF title shares 1 token ('the') with objective; reinforces but is not the direct action
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Product-side change records preserve series-production conformity and substantial-modi... | CRA | sufficient | - | low |

### D-07.4 · CRA · req 7.4.1
- **Title**: "Product-side change records preserve series-production conformity and substantial-modification decisions"
- **Description**: The product shall maintain auditable product-side change records that preserve series-production conformity decisions, substantial-modification assessments, and manufacturer-equivalent status determinations for CRA-regulated products.
- **Fit criterion (prose)**: For 100% of product changes, the change record contains product/version identifier, change classification, substantial-modification decision, conformity-impact assessment, affected technical-documentation reference, responsible role, approval decision, corrective-action link where applicable, and retention location for market-surveillance inspection.
- **Anchors listed**:
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| Financial entities implement documented policies, procedures and controls for ICT chang... | DORA | excessive | - | high |

### D-07.4 · DORA · subso SO-D-07.4.DORA
- **Objective**: Financial entities implement documented policies, procedures and controls for ICT change management, including changes to software, hardware, firmware components, systems or security parameters … based on a risk assessment approach … in order to ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner (Art. 9(4)(e) DORA — 5-way OR change-targets + 6-way AND change-management steps + `controlled manner` mandate).
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.4/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.PS-01, PR.PS-02, PR.PS-06 — literal duplicate(s) of PR.PS-01, PR.PS-02, PR.PS-06
- **Confidence**: high (article mapping and CSF title both consulted)

| "Entity-side ICT change records demonstrate controlled, risk-based change execution" Th... | DORA | sufficient | - | high |

### D-07.4 · DORA · req 7.4.2
- **Title**: "Entity-side ICT change records demonstrate controlled, risk-based change execution"
- **Description**: The product shall maintain auditable ICT change records showing that DORA-relevant changes to the entity's ICT environment follow the required risk-based change lifecycle from request through post-implementation verification.
- **Fit criterion (prose)**: For 100% of in-scope ICT changes, the change ticket contains requester, affected asset or parameter, risk assessment, test evidence, approver, implementation evidence, verification result, emergency-change flag if applicable, segregation-of-duty check, rollback decision, and immutable audit timestamp.
- **Regulatory basis**: `domains/D-07_Secure-Development/D-07.4/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.PS-01 — Configuration management practices are established and applied — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-08.1 General Security Awareness

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| A product with digital elements is accompanied by detailed instructions — or an interne... | CRA | excessive | - | high |

### D-08.1 · CRA · subso SO-D-08.1.CRA
- **Objective**: A product with digital elements is accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01 — literal duplicate(s) of PR.AT-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Product with digital elements accompanied by detailed user-facing secure-use instructi... | CRA | sufficient | - | high |

### D-08.1 · CRA · req 8.1.3
- **Title**: "Product with digital elements accompanied by detailed user-facing secure-use instructions covering the lifetime of the product"
- **Description**: The product with digital elements shall be accompanied by detailed instructions — or an internet address referring to such detailed instructions — covering the necessary measures during initial commissioning and throughout the lifetime of the product to ensure its secure use (Annex II §8(a)–(e) CRA), and — where the product is intended for integration into other products — the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA), with a duty to provide the instructions in paper or electronic form accessible for the support period under Art. 13(18).
- **Fit criterion (prose)**: The product with digital elements is accompanied by detailed secure-use instructions under Annex II §8(a) initial-commissioning + lifetime measures, §8(b) how changes to the product affect data security, §8(c) how security-relevant updates are installed, §8(d) secure decommissioning including user-data removal, §8(e) how the default automatic-update setting can be turned off, and §8(f) — where intended for integration — the information necessary for the integrator to comply with Annex I + Annex VII; the instructions are provided in paper or electronic form and remain accessible for the support period ≥ 5 years under Art. 13(8) sentence 3 + 10-year Annex II information accessibility under Art. 13(18); the CRA participation at 8.1 is partial — Annex II §8(a)–(f) addresses the end-user audience with the product (not workforce) per AEGIS taxonomy §4.1; the workforce-side partial dimension is the Annex II §8(f) integrator information for B2B integrators who incorporate the product into a downstream system (information counterpart to a contractually-anchored SCRM commitment per SR-CRA-108 security_rationale — Annex II §8(f) integrates at the 8.2 layer); the `detailed` content threshold is harmonised-standards-pending (no OJ definition of `detailed`); the chosen reading of `Throughout the lifetime of the product` is the entire supported lifetime + 10-year update tail (per SR-CRA-071 ambiguity reading); verified by Annex II §8(a)–(f) instruction-set review + Art. 13(18) support-period accessibility audit + Annex II §8(f) integrator-information review (B2B integrators) + support-period ≥ 5 years + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + market surveillance authority (MSA) / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Financial entities develop ICT security awareness programmes and digital operational re... | DORA | excessive | - | high |

### D-08.1 · DORA · subso SO-D-08.1.DORA
- **Objective**: Financial entities develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions (Art. 13(6) DORA).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.AT-02 — literal duplicate(s) of PR.AT-01, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "ICT security awareness programmes and digital operational resilience training as compu... | DORA | sufficient | - | high |

### D-08.1 · DORA · req 8.1.4
- **Title**: "ICT security awareness programmes and digital operational resilience training as compulsory modules in financial-entity staff training schemes"
- **Description**: The product shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in the financial-entity's staff training schemes (Art. 13(6) DORA), with a level of complexity commensurate to the remit of staff functions, on the financial-entity's workforce audience, with a digital-operational-resilience-testing-aligned syllabus and Art. 5(2) management-body oversight.
- **Fit criterion (prose)**: A financial-entity compulsory-modules-led staff training scheme is operated covering PR.AT-01 baseline awareness (phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes, removable-media hygiene, disciplined use of administrative privileges) + PR.AT-02 role-specific depth calibrated to the remit of staff functions (incident response, ICT operations, fraud investigation, third-party governance — 8.2 layer 8.2.4); the training modules are `compulsory` (completion-mandatory per SR-DORA-025 ambiguity reading — not mere attendance); the level of complexity is calibrated to the remit of staff functions per the OJ-literal `commensurate to the remit of their functions` formulation (T4-vs-text gap: T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit` — the Executor keeps the OJ-literal locus per SR-DORA-025 ambiguity_notes); completion thresholds (completion percentages, assessment-pass thresholds) are documented as a condition of employment rather than as optional professional development; the DORA Art. 13(6) programme is co-existent with GDPR Art. 39 staff-awareness duties for personal-data processing and NIS 2 Art. 21(2)(g) basic security training baselines (EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration); the DORA Art. 13(6) programme is the carrier programme and the GDPR content is a sub-component for a DORA financial entity that is a controller processing personal data over its own staff (per CRDA-deep §8.1 GDPR↔DORA verified relationship); the DORA Art. 13(6) `compulsory modules` exceeds NIS 2 `basic cyber hygiene` and discharges the NIS 2 workforce-awareness obligation for DORA financial entities (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs); for DORA financial entities deploying high-risk AI, the DORA programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) 5-element + 4-element AND human-overseer competence is a sub-component (8.2 layer 8.2.4 + 8.2.5 — cross-ref); for DORA financial entities deploying/manufacturing CRA products, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator); Art. 5(2) management-body oversight is documented; verified by Art. 13(6) `compulsory modules` training-records inspection + completion-thresholds documentation + EBA Guidelines supervisory baseline review + Art. 5(2) management-body oversight records + national CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The data protection officer informs and advises the controller or the processor and the... | GDPR | excessive | - | high |

### D-08.1 · GDPR · subso SO-D-08.1.GDPR
- **Objective**: The data protection officer informs and advises the controller or the processor and the employees who carry out processing of their obligations pursuant to this Regulation and to other Union or Member State data protection provisions (Art. 39(1)(a) GDPR), and monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/GDPR_Art_39.md` (Art. 39) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.AT-02 — literal duplicate(s) of PR.AT-01, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Personnel authorised to process personal data receive DPO-catalysed awareness-raising ... | GDPR | sufficient | - | high |

### D-08.1 · GDPR · req 8.1.1
- **Title**: "Personnel authorised to process personal data receive DPO-catalysed awareness-raising and training on GDPR obligations applicable to their role"
- **Description**: The product shall operate a DPO-catalysed data-protection awareness programme covering personnel authorised to process personal data, with the DPO informing and advising the controller or processor and the employees who carry out processing of their obligations (Art. 39(1)(a) GDPR) and monitoring compliance including assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR), where the controller is the data-protection awareness anchor on the controller-side processing-staff audience.
- **Fit criterion (prose)**: A DPO-catalysed data-protection awareness programme is operated covering all personnel authorised to process personal data via PR.AT-01 broad-coverage leg (phishing, social-engineering, password-discipline, removable-media, incident-reporting reflexes as they apply to data-protection obligations) on a recurring cadence with content that updates to reflect emerging threats and the changing data flows of the organisation; the DPO inform-and-advise obligation under Art. 39(1)(a) is documented with documented advisory records (DPO briefs + induction material + privacy-notice change advisory); the DPO awareness-raising and training obligation under Art. 39(1)(b) is documented with annual induction-completion records + periodic reinforcement records (DPO-discretionary cadence under Recital 56 — no quantitative OJ cadence; `awareness-raising` implies ongoing reinforcement rather than one-off induction per SR-GDPR-042 ambiguity reading); personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities receive role-specific reinforcement of their GDPR and cybersecurity obligations under PR.AT-02 (8.2 layer — cross-ref 8.2.1); the programme is documented under Art. 5(2) accountability so the controller can demonstrate on the day of any supervisory inspection that the Art. 39(1)(a)+(b) DPO-catalysed awareness function was operationally exercised and recorded; for an integrated controller-NSIE workforce the GDPR data-protection module combines with the NIS 2 entity-wide basic-hygiene module into a single curriculum where the data-protection module feeds the GDPR obligation and the hygiene module feeds the NIS 2 obligation (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship — separate evidence trails on the controller side vs the entity side); for a DORA financial entity that is a controller processing personal data over its own staff, the DORA Art. 13(6) programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed data-protection awareness is a sub-component of the carrier (per CRDA-deep §8.1 GDPR↔DORA verified relationship — DORA programme as carrier + GDPR content as module); for a CRA-regulated manufacturer that is also a controller, the GDPR workforce awareness obligation is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs external end-user — per CRDA-deep §8.1 GDPR↔CRA verified relationship — no consolidation rule applies); verified by DPO-catalysed awareness-records inspection + DPO inform-and-advise records review + Art. 5(2) accountability evidence pack + training-cadence documentation + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/GDPR_Art_39.md` (Art. 39) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Essential and important entities take appropriate and proportionate technical, operatio... | NIS2 | excessive | - | high |

### D-08.1 · NIS2 · subso SO-D-08.1.NIS2
- **Objective**: Essential and important entities take appropriate and proportionate technical, operational and organisational measures to ensure basic cyber hygiene practices and cybersecurity training (Art. 21(2)(g) first clause NIS 2).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.PS-01 — literal duplicate(s) of PR.AT-01, PR.PS-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Entity-wide basic cyber-hygiene practices with workforce hygiene substrate and proport... | NIS2 | sufficient | - | high |

### D-08.1 · NIS2 · req 8.1.2
- **Title**: "Entity-wide basic cyber-hygiene practices with workforce hygiene substrate and proportionate calibration"
- **Description**: The product shall establish basic cyber-hygiene practices and cybersecurity training for all users of network and information systems with access to entity systems and services (Art. 21(2)(g) first clause NIS 2), with the depth calibrated by the Art. 21(1) `appropriate and proportionate` chapeau and the state-of-the-art floor, on the entity-wide workforce-and-systems substrate, and with Art. 20(1) management-body approval+oversight+liability.
- **Fit criterion (prose)**: An entity-wide basic-hygiene programme is operated covering all users of network and information systems with access to entity systems and services via the human-side hygiene substrate PR.AT-01 (phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, disciplined use of administrative privileges) plus the system-side hygiene substrate PR.PS-01 (baseline configurations, secure configuration standards, change management and patch cadence for the NIS inventory); the two together operationalise the ENISA / SANS Top 20 / Australian Cyber Security Centre Essential Eight convergence on workforce-and-assets hygiene; the chosen reading of `basic cyber hygiene` is the broader ENISA baseline reading, with the chosen reading being entity-discretionary interpretation under Recital 56 proportionality (no quantitative cadence in Art. 21(2)(g) and no OJ enumeration — three operative readings admitted per SR-NIS2-029 ambiguity_notes); the depth is calibrated by the Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor + Recital 56 proportionality factors (nature/size/risk profile/cost of implementation); for an integrated controller-NSIE workforce the NIS 2 hygiene module combines with the GDPR DPO-catalysed data-protection awareness module into a single curriculum (per CRDA-deep §8.1 GDPR↔NIS2 verified relationship — combined curriculum with separate evidence trails); for DORA financial entities, the DORA Art. 13(6) `compulsory modules` exceeds NIS 2 `basic cyber hygiene` and the DORA programme discharges the NIS 2 workforce-awareness obligation (per CRDA-deep §8.1 NIS2↔DORA EQUAL classification — DORA-dominant for financial entities, NIS 2-dominant for non-financial NSIEs); for a CRA-regulated manufacturer, the NIS 2 hygiene baseline on the workforce is independent of the CRA Annex II §8(a)–(f) user-facing instructions (substantively scope-disjoint audiences — workforce vs end-user — no consolidation rule); the Art. 20(1) management-body approval is documented as the governance hook; verified by entity-wide hygiene-coverage audit + PR.AT-01 + PR.PS-01 records review + Art. 21(1) proportionality calibration documentation + Art. 20(1) management-body approval records + management-body + competent-authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.1/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-08.2 Role-Specific Competence

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are designed and developed in such a way, including with appropria... | AI_Act | excessive | - | low |

### D-08.2 · AI_Act · subso SO-D-08.2.AIACT
- **Objective**: High-risk AI systems are designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use (Art. 14(1) AI Act) — the provider-side design obligation for the human-oversight capability.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/AI_Act_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 2 action tokens with objective
  - GV.RR-04 — Cybersecurity is included in human resources practices — **UTILITY** — Reinforces obligation in same CSF function (GOVERN) but does not directly match the action
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 6 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 2 action tokens with objective
  - GV.RR-04 — Cybersecurity is included in human resources practices — **UTILITY** — Reinforces obligation in same CSF function (GOVERN) but does not directly match the action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04 — literal duplicate(s) of PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "High-risk AI system human overseers enabled with the 5 cumulative oversight abilities ... | AI_Act | sufficient | - | low |

### D-08.2 · AI_Act · req 8.2.5
- **Title**: "High-risk AI system human overseers enabled with the 5 cumulative oversight abilities (provider) and assigned with competence, training, authority, and support (deployer)"
- **Description**: The product shall, on the provider-side, be designed and developed in such a way, including with appropriate human-machine interface tools, that the high-risk AI system can be effectively overseen by natural persons during the period in which it is in use (Art. 14(1) AI Act), with the natural persons assigned to human oversight enabled, as appropriate and proportionate, to discharge five cumulative oversight abilities (Art. 14(4)(a)–(e): properly understand; remain aware of automation bias; correctly interpret; decide not to use / disregard / override / reverse; intervene on the operation or interrupt the system); and on the deployer-side, deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support (Art. 26(2) AI Act — 4-element AND `competence, training AND authority AND support`).
- **Fit criterion (prose)**: For an AI-Act-scope high-risk AI system, the provider-side Art. 14(4) 5-element closed-list AND-coordinated design obligation is operationalised in NIST CSF 2.0 through PR.AT-02 (Workforce understands role-specific responsibilities — covers sub-points (a) `properly understand` and (c) `correctly interpret`) + PR.AT-01 (User awareness and training — covers sub-points (b) `remain aware of automation bias`, (d) `decide`, (e) `intervene`) + GV.RR-02 (RACI substrate — overseers must hold formal authority to override and interrupt the system per sub-points (d) and (e)) — the 5-element list is AND-coordinated and all five abilities must be enabled cumulatively (partial compliance is non-compliance per SR-AIACT-013 ambiguity_notes); the design-by-design substrate includes the human-machine interface tools that enable the oversight-abilities under Art. 14(1); on the deployer-side Art. 26(2) 4-element AND, the deployer maintains a personnel file per overseer documenting each of the four elements (competence, training, authority, support) per SR-AIACT-020 ambiguity_notes, with GV.RR-02 (Roles, responsibilities, authorities, accountabilities established, communicated, understood, enforced — the four-way AND that the deployer must evidence for each overseer) + GV.RR-04 (Cybersecurity in HR practices — screening, onboarding, training, awareness, offboarding operationalises the `necessary support` element) + PR.AT-02 (the deployer's personnel-qualification anchor — competence, training) + supplementary PR.AT-01 + PR.AT-02 + GV.RR-01; the provider-design + deployer-assignment twin-trigger is the AI-Act-specific competence architecture (provider-side Art. 14 design-by-design substrate + deployer-side Art. 26(2) assignment-on-deployment substrate); for an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR Art. 39(1)(b) DPO-catalysed role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified DIFFERENT-PERSPECTIVE pair on the same-natural-person operator); for NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship — NIS 2 risk-identification baseline + AI Act 5-element + 4-element AND stack); for DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship); for a CRA-regulated manufacturer that is also an AI Act provider, the CRA Annex II §8(f) integrator-facing information is independent of the AI Act Art. 14(4) + Art. 26(2) human-overseer competence (substantively scope-disjoint audiences — B2B integrator vs AI-overseer role within deployer organization — per CRDA-deep §8.2 CRA↔AI_Act Executor-recommended SCOPE-DISJOINT pair); verified by 5-element + 4-element AND personnel-file inspection per overseer + provider QMS design-control documentation (Art. 17(1) QMS documented in `systematic and orderly manner`) + Annex IV technical-documentation review + post-market monitoring Art. 72 + provider / deployer / MSA / AI Office inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/AI_Act_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 9 action tokens with objective
  - GV.RR-04 — Cybersecurity is included in human resources practices — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Where the product with digital elements is intended for integration into other products... | CRA | excessive | - | low |

### D-08.2 · CRA · subso SO-D-08.2.CRA
- **Objective**: Where the product with digital elements is intended for integration into other products with digital elements, the manufacturer provides the information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (Annex II §8(f) CRA).
- **Anchors listed**:
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title shares 4 action tokens with objective
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-02, GV.SC-03 — literal duplicate(s) of PR.AT-02, GV.SC-03
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Where the product is intended for integration, information necessary for the integrato... | CRA | sufficient | - | low |

### D-08.2 · CRA · req 8.2.3
- **Title**: "Where the product is intended for integration, information necessary for the integrator to comply with Annex I cybersecurity requirements and Annex VII documentation requirements is delivered"
- **Description**: The product with digital elements shall, where intended for integration into other products with digital elements, be accompanied by information necessary for the integrator to comply with the essential cybersecurity requirements set out in Part I of Annex I and the documentation requirements set out in Annex VII (CRA Annex II §8(f)), on the B2B integrator audience — partial coverage per AEGIS taxonomy §4.1.
- **Fit criterion (prose)**: Where the product with digital elements is `intended for integration` per the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4 — not third-party speculation about possible integration patterns), the product is accompanied by information via PR.AT-02 integrator's understanding of the upstream product's threat model, configuration constraints, and vulnerability-handling interface + GV.SC-03 contractual/information-disclosure layer (the §8(f) information is the information counterpart to a contractually-anchored SCRM commitment); the information covers the cybersecurity measures required for the integrator to maintain Annex I compliance + the documentation requirements set out in Annex VII; the information is provided in paper or electronic form and remains accessible for the support period ≥ 5 years under Art. 13(8) sentence 3 + 10-year Annex II information accessibility under Art. 13(18); the CRA participation at 8.2 is partial — Annex II §8(f) addresses the B2B integrator audience (not workforce) per AEGIS taxonomy §4.1; the asymmetry — workforce training (NIS 2 / DORA / GDPR) vs product-integrator training (CRA) — is unique to 8.2 per DomainAnalysis §8.2 line 107; the Annex II §8(f) integrator-B2B audience operates on a substantively scope-disjoint audience from the GDPR / NIS 2 / DORA workforce programmes and the AI Act human-overseer role within the deployer organization — no consolidation rule applies on the 4 CRA-involving pairs (GDPR↔CRA, NIS2↔CRA, CRA↔DORA, CRA↔AI_Act — Executor-recommended SCOPE-DISJOINT per CRDA-deep §8.2); **8.1 layer (8.1.3)** adds the user-facing secure-use instructions (Annex II §8(a)–(e)) + the integrator-facing dimension (Annex II §8(f)) at the general-awareness level — this 8.2 layer adds the role-specific depth on the integrator-B2B audience (Annex II §8(f) only — the integrator's role-specific understanding of threat model + configuration + vulnerability-handling); verified by Annex II §8(f) integrator-information review (B2B integrators only — product intended for integration) + Art. 13(18) support-period accessibility audit + Annex VII §2(b) + §3 + §6 + §8 technical-documentation inspection + market surveillance authority (MSA) / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.SC-03 — Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes — **CORE** — CSF title shares 3 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities develop ICT security awareness programmes and digital operational re... | DORA | excessive | - | high |

### D-08.2 · DORA · subso SO-D-08.2.DORA
- **Objective**: Financial entities develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes, with a level of complexity commensurate to the remit of their functions (Art. 13(6) DORA).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.AT-02 — literal duplicate(s) of PR.AT-01, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial-entity staff training modules with level of complexity commensurate to the r... | DORA | sufficient | - | high |

### D-08.2 · DORA · req 8.2.4
- **Title**: "Financial-entity staff training modules with level of complexity commensurate to the remit of staff functions"
- **Description**: The product shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in the financial-entity's staff training schemes, with a level of complexity commensurate to the remit of staff functions (Art. 13(6) DORA), on the financial-entity's workforce audience, with function-specific depth calibrated to the staff function taxonomy (incident response, ICT operations, fraud investigation, third-party governance, and other security-critical roles).
- **Fit criterion (prose)**: A financial-entity `commensurate to the remit` function-specific depth training programme is operated for staff in security-critical roles via PR.AT-02 role-specific depth (Workforce understands role-specific responsibilities) covering incident response (cross to D-04 layer — RS.MA-01 incident-management-plan-executed), ICT operations (cross to D-10 layer — DE.CM-01 networks-monitored + DE.CM-09 host-monitored), fraud investigation (cross to 4.4 detection + recovery), third-party governance (cross to D-06 supply-chain — GV.SC-04 supplier-assessment), and other security-critical roles receiving function-specific depth rather than a uniform baseline; the chosen reading of `level of complexity commensurate to the remit of their functions` is function-specific calibration per the OJ literal formulation per SR-DORA-025 ambiguity_notes; the chosen reading of `compulsory` is completion-mandatory (not mere attendance) per SR-DORA-025; **T4-vs-text gap awareness:** T4 reads `role-specific training` but the OJ Art. 13(6) uses only `commensurate to the remit of their functions` — the Executor keeps the OJ-literal locus per SR-DORA-025; the training modules are `compulsory` as a condition of employment rather than as optional professional development; completion thresholds (completion percentages, assessment-pass thresholds) are documented per the staff function taxonomy; the DORA Art. 13(6) `commensurate to the remit` programme is co-existent with GDPR Art. 39 staff-awareness duties for personal-data processing (EBA Guidelines on ICT and security risk management set out the supervisory expectation on calibration, AI Act Art. 4(2) provider-deployer literacy duties intersect where AI systems are in scope of the same staff training schemes); for an integrated financial-entity-controller with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair on the DORA financial entity = controller); for DORA financial entities that are also NSIEs, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification); for DORA financial entities deploying high-risk AI, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence is a sub-component (per CRDA-deep §8.2 DORA↔AI_Act verified relationship); for a CRA-regulated manufacturer that is also a DORA financial entity, the DORA Art. 13(6) internal staff training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — internal staff vs B2B integrator — per CRDA-deep §8.2 CRA↔DORA Executor-recommended SCOPE-DISJOINT pair); verified by per-role `commensurate to the remit` training-records inspection + completion-thresholds documentation per staff function taxonomy + EBA Guidelines supervisory baseline review + Art. 5(2) management-body oversight records + national CA + ESA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The data protection officer monitors compliance with this Regulation, including the ass... | GDPR | excessive | - | high |

### D-08.2 · GDPR · subso SO-D-08.2.GDPR
- **Objective**: The data protection officer monitors compliance with this Regulation, including the assignment of responsibilities, awareness-raising and training of staff involved in processing operations (Art. 39(1)(b) GDPR) — the role-specific layer of the DPO-catalysed awareness function.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/GDPR_Art_39.md` (Art. 39) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.AT-02 — literal duplicate(s) of PR.AT-01, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Role-specific training for processing staff with data-subject-facing, access-managemen... | GDPR | sufficient | - | high |

### D-08.2 · GDPR · req 8.2.1
- **Title**: "Role-specific training for processing staff with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities"
- **Description**: The product shall provide role-specific training for personnel with data-subject-facing, access-management, breach-response, or DPO-deputy responsibilities (the role-specific layer of the Art. 39(1)(b) DPO-catalysed awareness function), with quarterly or event-triggered cadence and content covering GDPR-specific and cybersecurity-specific obligations for the assigned role (GDPR Art. 39(1)(a) + Art. 39(1)(b)).
- **Fit criterion (prose)**: A DPO-catalysed role-specific training programme is operated for personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities via PR.AT-02 role-understanding dimension (Workforce understands role-specific responsibilities) on a quarterly cadence or event-triggered cadence (whichever is sooner — material change of role, material change of processing profile, material change of risk, post-incident); the chosen reading per SR-GDPR-042 ambiguity_notes splits the obligation into (1) general awareness training on GDPR for all personnel involved in processing, on an annual basis (8.1 layer — 8.1.1 cross-ref) + (2) role-specific training for personnel with the four responsibility-types above, on a quarterly or event-triggered basis (this layer); the role-specific training covers: data-subject-rights handling (Arts. 12–22), access-management including privileged-access review (Art. 25 + Art. 32), breach-response including notification timelines (Art. 33 + Art. 34 — D-04 cross-references), DPO-deputy capacity when the primary DPO is unavailable (Art. 38–39), and updated content reflecting emerging threats + the changing data flows of the organisation; the role-specific training is documented under Art. 5(2) accountability so the controller can demonstrate on the day of any supervisory inspection that the Art. 39(1)(b) DPO-catalysed role-specific training was operationally exercised and recorded; for an integrated controller-NSIE adopting Member-State encouragement, the GDPR role-specific layer stacks with the NIS 2 Member-State-encouraged employee risk-identification training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship — joint curriculum on the Y-pair); for a DORA financial entity that is a controller processing personal data with role-specific staff, the DORA Art. 13(6) `commensurate to the remit` programme is the carrier and the GDPR Art. 39(1)(b) DPO-catalysed role-specific training is a sub-component (per CRDA-deep §8.2 GDPR↔DORA Executor-recommended COMPLEMENTARY pair on the DORA financial entity = controller); for an AI Act deployer-controller with the same natural person as both data-processing staff and AI human overseer, the AI Act Art. 14(4) + Art. 26(2) layer is the additional competence dimension on top of the GDPR role-specific training (Conditional Y per CRDA-deep §8.2 GDPR↔AI_Act verified DIFFERENT-PERSPECTIVE pair); verified by role-specific training records inspection (per responsibility-type — four-way review) + DPO-catalysed training-completion records inspection + Art. 5(2) accountability evidence pack + DPA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/GDPR_Art_39.md` (Art. 39) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Member States shall encourage essential and important entities to offer similar trainin... | NIS2 | excessive | - | high |

### D-08.2 · NIS2 · subso SO-D-08.2.NIS2
- **Objective**: Member States shall encourage essential and important entities to offer similar training to their employees on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2 NIS 2).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/NIS2_Art_20.md` (Art. 20) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-01, PR.AT-02 — literal duplicate(s) of PR.AT-01, PR.AT-02
- **Confidence**: high (article mapping and CSF title both consulted)

| "Employees gain sufficient knowledge and skills to identify risks and assess cybersecur... | NIS2 | sufficient | - | high |

### D-08.2 · NIS2 · req 8.2.2
- **Title**: "Employees gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Member-State-encouraged, entity-side on adoption)"
- **Description**: The product shall offer employees training on a regular basis, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices (Art. 20(2) sentence 2 NIS 2), with the entity-side SR applying to entities that adopt the Member-State encouragement (binding force on the Member State rather than directly on the entity per SR-NIS2-030).
- **Fit criterion (prose)**: A Member-State-encouraged employee risk-identification training programme is operated when the entity adopts the encouragement, covering PR.AT-01 recurring training content (phishing, social engineering, password discipline, threat-recognition capability) + PR.AT-02 role-specific dimension supporting the OJ's purpose clause that employees must `gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices`; the temporal anchor `on a regular basis` is entity-discretionary under Recital 56 (annual, biannual, ad-hoc, or event-triggered cadence — entity choice); the compound `similar training` reads as parallel-to-management-training per SR-NIS2-030 (the OJ coordinates sentence 2 with sentence 1 within the same paragraph); the chosen reading of `shall encourage` is the cumulative reading (national policy + financial incentives + sectoral guidance + all) since the OJ is silent on the encouragement mechanism; the entity-side SR applies to entities that adopt the encouragement (Orchestrator-recommended treatment per SR-NIS2-030 — the Article 20(2) sentence 2 binding force is on the Member State rather than directly on the entity); the training is anchored in the NIST NICE Workforce Framework and proportionate to the entity's exposure; for an integrated controller-NSIE adopting Member-State encouragement, the NIS 2 Member-State-encouraged employee risk-identification training stacks with the GDPR Art. 39(1)(b) DPO-catalysed role-specific training on the same workforce (Conditional Y per CRDA-deep §8.2 GDPR↔NIS2 verified relationship — joint curriculum on the Y-pair); for DORA financial entities, DORA-dominant for the role-specific training dimension (Art. 13(6) `commensurate to the remit` function-specific calibration is more prescriptive than NIS 2 Art. 20(2) sentence 2 encouraged-not-mandatory — per CRDA-deep §8.2 NIS2↔DORA EQUAL classification); for NSIEs deploying high-risk AI and assigning human oversight, the NIS 2 Art. 20(2) sentence 2 employee risk-identification training stacks with the AI Act Art. 14(4) + Art. 26(2) human-overseer 5-element + 4-element AND competence (per CRDA-deep §8.2 NIS2↔AI_Act verified relationship — NIS 2 risk-identification baseline + AI Act 5-element competence stack); for a CRA-regulated manufacturer that is also an NSIE, the NIS 2 employee risk-identification training is independent of the CRA Annex II §8(f) integrator-facing information (substantively scope-disjoint audiences — workforce vs B2B integrator — per CRDA-deep §8.2 NIS2↔CRA Executor-recommended SCOPE-DISJOINT pair); the training programme coordinates with the Art. 20(2) sentence 1 management-body training via SR-NIS2-031 (cross to 8.3); verified by employee training-records inspection + risk-identification competency assessment records + NIST NICE Workforce Framework curriculum anchor documentation + management body + competent authority inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.2/articles/NIS2_Art_20.md` (Art. 20) — paraphrased action
- **Anchors listed**:
  - PR.AT-01 — Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-08.3 Management Board Training

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Members of the management body shall actively keep up to date with sufficient knowledge... | DORA | excessive | - | high |

### D-08.3 · DORA · subso SO-D-08.3.DORA
- **Objective**: Members of the management body shall actively keep up to date with sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed (Art. 5(4) DORA).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.3/articles/DORA_Art_4.md` (Art. 4) — paraphrased action
- **Anchors listed**:
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: PR.AT-02, GV.RR-01 — literal duplicate(s) of PR.AT-02, GV.RR-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Members of the management body of financial entities actively keep up to date with suf... | DORA | sufficient | - | high |

### D-08.3 · DORA · req 8.3.2
- **Title**: "Members of the management body of financial entities actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk, commensurate to the ICT risk being managed"
- **Description**: The product shall ensure that members of the management body of the financial entity actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed (per DORA Art. 5(4)), on the financial-entity workforce audience, with the literacy underpinning the Art. 5(2) management-body responsibility.
- **Fit criterion (prose)**: Each member of the management body has documented evidence of `actively keep up to date` against the Art. 5(4) threshold — `sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific training on a regular basis, commensurate to the ICT risk being managed` — with PR.AT-02 training-and-knowledge component (the `sufficient knowledge and skills` OJ phrase operationalised as documented role-and-responsibility literacy, evidence of `actively keep up to date`, and training records calibrated to the ICT risk being managed) + GV.RR-01 accountability-and-culture component (the management body's literacy tied to the personal-capacity prerequisite for the Art. 5(2) oversight-and-liability regime and to the broader fit-and-proper expectations under EBA Guidelines on Internal Governance + CRD Art. 91 + MiFID II Art. 4(1)(36)/(37)); the `sufficient` threshold is read at the role-relevant-competency end of the spectrum per the `commensurate to the ICT risk` qualifier (S2 VAG, per SR-DORA-024 ambiguity_notes); the `regular basis` is read as risk-driven cadence per the literal `actively keep up to date` formulation (S2 VAG — risk-driven cadence rather than scheduled or ongoing); the `commensurate to the ICT risk` is read as risk-proportional rather than risk-quantified (S2 VAG — the OJ does not impose a numeric floor); the `actively keep up to date` is read as the literal AND of self-study, formal training, or both (S2 POLY — chosen reading: literal AND, per SR-DORA-024 ambiguity_notes); evidence forms (training-attendance logs, assessment scores, peer-benchmark exercises) are documented under entity policy and remain for entity policy (per SR-DORA-024 ambiguity_notes remain-open); the programme co-exists with EBA Guidelines on Internal Governance and the fit-and-proper frameworks (CRD Art. 91, MiFID II Art. 4(1)(36)/(37) cross-reference); for smaller entities under Art. 4 proportionality, training evidence is proportionate to risk exposure; the programme is the literacy underpinning of the Art. 5(2) management-body responsibility (`define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework`) and the personal-capacity threshold for Art. 5(2) to operate meaningfully, per SR-DORA-024 regulatory_rationale; the programme couples with 8.3.1 on a DORA-dominant stack for a DORA financial entity that is also an NSIE (DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` direct entity-side obligation discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities, per CRDA-deep §8.3 NIS2↔DORA verified relationship — DORA-dominant); the programme couples with 8.1.4 (workforce-scale compulsory-modules substrate) and 8.2.4 (workforce-scale role-specific depth) without collapsing the governance-track / workforce-scale track distinction (per CRDA-deep §8.3 scope caveat on management-body training as governance-track counterpart — DORA Art. 5(4) = governance track; DORA Art. 13(6) = workforce-scale track); the programme is documented under Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance fit-and-proper framework; verified by management-body training programme documentation review + per-individual-member training-completion records + Art. 5(4) supervisory-evidence pack + NCA (national financial supervisory authority) review on request + EBA Guidelines on Internal Governance fit-and-proper assessment where applicable.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.3/articles/DORA_Art_4.md` (Art. 4) — paraphrased action
- **Anchors listed**:
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 5 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Member States shall ensure that members of the management bodies of essential and impor... | NIS2 | sufficient | - | high |

### D-08.3 · NIS2 · subso SO-D-08.3.NIS2
- **Objective**: Member States shall ensure that members of the management bodies of essential and important entities are required to follow training, in order that they gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity (Art. 20(2) sentence 1 NIS 2).
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.3/articles/NIS2_Art_20.md` (Art. 20) — paraphrased action
- **Anchors listed**:
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Members of management bodies of essential and important entities follow cybersecurity ... | NIS2 | sufficient | - | high |

### D-08.3 · NIS2 · req 8.3.1
- **Title**: "Members of management bodies of essential and important entities follow cybersecurity training to gain sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices"
- **Description**: The product shall ensure that members of the management bodies of essential and important entities follow cybersecurity training gaining sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity (per NIS 2 Art. 20(2) sentence 1), where the entity-side SR applies where the Member State has transposed the literacy prerequisite for the Art. 20(1) approve+oversee+liable governance duties.
- **Fit criterion (prose)**: Each member of the management body individually (the OJ does not provide a designation carve-out — the literal `members of the management bodies` reads as every member individually, per SR-NIS2-031 ambiguity_notes) has documented evidence of cybersecurity training completion covering the OJ purpose-clause objects — `sufficient knowledge and skills to identify risks and assess cybersecurity risk-management practices and their impact on the services provided by the entity` — with PR.AT-02 executive-literacy substrate (each member individually possesses sufficient knowledge to identify risks and assess cybersecurity risk-management practices, with documented evidence of training completion) + GV.RR-01 leadership-culture substrate (trained members exercise the Art. 20(1) approve+oversee+liable obligations with informed judgement and accept personal liability exposure under Art. 20(1) sentence 1 third clause on a substantively-informed basis); the binding-force locus is the both reading (statute mandates, entity operationalises) under the standard MS-implementation pattern, with Member State transposition divergence preserved (the chosen reading is the both reading since the OJ literal `are required to follow` is compatible with either locus, per SR-NIS2-031 ambiguity_notes); the `training` content is entity-discretionary (formal certified programme preferred where the entity seeks documented compliance evidence, with awareness-briefing and tabletop-exercise readings admitted, per SR-NIS2-031 ambiguity_notes); the `sufficient knowledge and skills` threshold is read in the cybersecurity-specific dominant sense because the OJ coordinates it with `cybersecurity risk-management practices`; the programme couples with 8.3.2 on a DORA-dominant stack for a DORA financial entity that is also an NSIE (DORA Art. 5(4) `actively keep up to date` + `commensurate to the ICT risk` discharges both DORA's dedicated management-body obligation and NIS 2's Member-State-imposed Art. 20(2) sentence 1 literacy prerequisite for DORA financial entities, per CRDA-deep §8.3 NIS2↔DORA verified relationship); the Art. 20(2) sentence 1 training obligation is the literacy prerequisite for the Art. 20(1) approve+oversee+liable obligations (cross-ref 9.1.2 for the management-body approval minute + Art. 21(2)(a) policy artefact) — without trained members, the management body cannot meaningfully discharge the approve-and-oversee obligations or be held accountable for infringements, per SR-NIS2-031 regulatory_rationale; the programme is documented under Art. 21(1) NIS 2 chapeau with the management-body approval minute as governance hook (cross-ref 9.1.2); the workforce-scale upstream substrate (8.1 general awareness — 8.1.2) and the workforce-scale depth dimension (8.2 role-specific competence — 8.2.2) feed the management-body literacy substrate without collapsing the governance-track / workforce-scale track distinction; verified by management-body training programme documentation review + per-individual-member training-completion records + Art. 20(2) sentence 1 supervisory-evidence pack + competent-authority (national NIS 2 supervisory authority) review on request.
- **Regulatory basis**: `domains/D-08_Human-Factors/D-08.3/articles/NIS2_Art_20.md` (Art. 20) — paraphrased action
- **Anchors listed**:
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 6 action tokens with objective
  - PR.AT-02 — Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind — **CORE** — CSF title literally matches action keyword ('train')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-09.1 Information Security Policies

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| High-risk AI systems are **designed and developed to ensure that their operation is suf... | AI_Act | sufficient | - | low |

### D-09.1 · AI_Act · subso SO-D-09.1.AI_Act
- **Objective**: High-risk AI systems are **designed and developed to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately** (Art. 13(1) AI Act), accompanied by **concise, complete, correct and clear instructions for use** (Art. 13(3) AI Act); a provider **puts a quality management system in place** documented in written policies, procedures and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OC-04 — Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Provider of high-risk AI system operates a documented quality management system with a... | AI_Act | sufficient | - | low |

### D-09.1 · AI_Act · req 9.1.5
- **Title**: "Provider of high-risk AI system operates a documented quality management system with at least 13 enumerated aspects and instructions for use enabling deployer-interpretable transparency"
- **Description**: The product shall operate a documented quality management system (QMS) ensuring compliance with the AI Act, documented in a systematic and orderly manner in the form of written policies, procedures, and instructions covering at least the 13 enumerated aspects of Art. 17(1) closed list (a)-(m), with high-risk AI systems designed and developed to ensure sufficiently transparent operation enabling deployers to interpret a system's output and use it appropriately, accompanied by concise, complete, correct and clear instructions for use (per AI Act Art. 17(1) + Art. 13(1) + Art. 13(3)).
- **Fit criterion (prose)**: A QMS is documented under Art. 17(1) (SR-AIACT-017) in a systematic and orderly manner in the form of written policies, procedures, and instructions (POLY on `quality management system` — R1 ISO 9001 / R2 ISO/IEC 23053 / R3 internal bespoke; chosen reading: R3 literal since the OJ does not name any specific standard — Recital 67 characterises the QMS as inspired by established quality standards but does not mandate a specific standard); the QMS covers at least the 13 enumerated aspects (a)-(m) of the Art. 17(1) closed list with GV.PO-01 policy arm (the top-level written cybersecurity policy that operationalises the 13-element list including the policies, procedures, and instructions anchor) + GV.PO-02 process-and-procedure arm (the policies accompanied by documented processes and procedures, also documented, communicated, and enforced — the systematic-and-orderly requirement of Art. 17(1)) + GV.RM-01 risk-management-objectives binding (the QMS bound to risk-management objectives agreed by organisational stakeholders, satisfying sub-point (g)'s cross-reference to Art. 9 risk-management system) + GV.RM-04 strategic-direction layer (risk appetite, response posture, escalation criteria that connect policy formulation and risk-objective setting to operational risk-treatment decisions) + GV.OC-03 legal-and-regulatory obligations register (the QMS understands and manages the full set of legal, regulatory, and contractual obligations that the AI Act adds on top of CRA, NIS 2, GDPR, and DORA); high-risk AI systems are designed and developed to ensure sufficiently transparent operation enabling deployers to interpret a system's output and use it appropriately under Art. 13(1) (SR-AIACT-010) with GV.PO-01 cybersecurity-policy substrate (transparency must be policy-bound and enforced to be supervisory-auditable) + GV.OC-03 legal-and-regulatory understanding substrate (distinguishing the high-risk-specific Art. 13(1) transparency duty from the Art. 50 user-facing and Art. 70 deployer-information duties, ensuring the cumulative AND of explainability, disclosure, and interpretability senses is operationalised against an understood regulatory baseline) + GV.OC-04 stakeholder-communication dimension (deployers are the principal stakeholders for AI-system transparency, operationalising the `interpret a system's output AND use it appropriately` opening through understood capabilities and limitations); the chosen reading for `sufficiently transparent` + `appropriate type and degree of transparency` is cumulative (explainability + disclosure + interpretability) because the `interpret a system's output AND use it appropriately` opening implicates each sense (per SR-AIACT-010 ambiguity_notes — central S3 ambiguity on `sufficiently transparent` admits three AI-governance senses: explainability / disclosure / interpretability, each implying different technical implementations — explainable-AI tooling / system documentation / model-architecture disclosure respectively); Art. 13(3) instructions-for-use are `concise, complete, correct and clear` (4-way AND) + `relevant, accessible and comprehensible` (3-way AND) + `characteristics, capabilities and limitations of performance` (POLY triple) — the high-risk-system transparency instructions-for-use accompanying the system; the QMS is documented under Art. 17(1) systematic-and-orderly QMS + Art. 9 risk-management cross-reference + Art. 43/47 conformity-assessment accountability chain; the QMS becomes a sub-policy of the integrated policy architecture on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation — AI Act QMS as sub-policy of GDPR data-protection policies for providers/deployers that are controllers processing personal data via high-risk AI, per CRDA-deep §9.1 GDPR↔AI_Act verified relationship); for an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair (the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy, per CRDA-deep §9.1 NIS2↔AI_Act verified relationship); for AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (CRA on the product cybersecurity requirements + AI Act on the AI-system quality-management system — no OJ-level consolidation rule at 9.1, unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*, per CRDA-deep §9.1 CRA↔AI_Act verified relationship); for a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component, per CRDA-deep §9.1 DORA↔AI_Act verified relationship); verified by Art. 17(1) QMS documentation review + Art. 13(1) sufficiently-transparent design-and-development evidence + Art. 13(3) `concise, complete, correct and clear` instructions-for-use documentation review + Art. 17(1)(g) Art. 9 risk-management-system cross-reference documentation + Art. 43/47 conformity-assessment records + Art. 50 user-facing transparency records (when applicable) + MSA / AI Office / provider / deployer inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 10 action tokens with objective
  - GV.OC-04 — Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated — **CORE** — CSF title shares 10 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 7 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| An open-source software steward **puts in place and documents in a verifiable manner a ... | CRA | sufficient | - | low |

### D-09.1 · CRA · subso SO-D-09.1.CRA
- **Objective**: An open-source software steward **puts in place and documents in a verifiable manner a cybersecurity policy** (Art. 24(1) CRA) covering vulnerability documentation, remediation, and information-sharing within the open-source community; a manufacturer **establishes policies, processes and procedures necessary to implement its CRA cybersecurity obligations** (Art. 13(8) CRA) including CVD policy, secure-update distribution, support-period determination, and cessation-of-operations communication.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — CSF title shares 4 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Manufacturer and OSS-steward cybersecurity policies with verifiable documentation, CVD... | CRA | sufficient | - | low |

### D-09.1 · CRA · req 9.1.3
- **Title**: "Manufacturer and OSS-steward cybersecurity policies with verifiable documentation, CVD, support-period, and presumption of conformity via harmonised standards, common specifications, or CSA certification"
- **Description**: The product shall establish manufacturer policies/processes/procedures necessary to implement CRA cybersecurity obligations — including the CVD policy under Annex I Part II §5 + Art. 13(8) sentence 6, the secure-update distribution mechanism under Annex I Part II §7, the support-period determination methodology under Art. 13(8) sentence 2, and the cessation-of-operations communication procedure under Art. 13(23) (per CRA Art. 13(8)) — and where applicable, OSS-steward cybersecurity policy fostering secure development and effective vulnerability handling (per Art. 24(1) 4-element (i)-(iv)) with verifiable documentation + cooperation with market surveillance authorities (per Art. 24(2)), with the presumption-of-conformity machinery via harmonised standards / common specifications / CSA certification (per Art. 27(1)/(2)/(5)/(8)/(9)).
- **Fit criterion (prose)**: Manufacturer policies/processes/procedures are documented under Art. 13(8) sentence 6 `appropriate policies including a CVD policy` + Annex I Part II §5 CVD policy + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation-of-operations communication procedure (SR-CRA-075) with GV.PO-01 policy-instrument layer (CVD policy + support-period-determination methodology established, communicated to security researchers, users, and other stakeholders via publication and promotion, and enforced through the documented policy framework) + GV.PO-02 implementation-process layer (policies operationalised through documented processes — CVD coordination workflow + support-period calculation procedure + policy-update mechanism — with implementation evidence recorded in technical documentation under Annex VII §2(b)); for OSS-steward entities, an Art. 24(1) cybersecurity policy is put in place and documented in a verifiable manner fostering the secure development of products with digital elements and effective vulnerability handling (SR-CRA-072) with GV.PO-01 policy-instrument layer (cybersecurity policy established, communicated across the steward's maintainer base + contributors + downstream dependents, and enforced through the documented 4-element (i)-(iv) `documenting, addressing, remediating vulnerabilities; sharing of information concerning discovered vulnerabilities within the open-source community`) + GV.SC-01 supply-chain-risk-management dimension (policy positioned as the entry point of the steward's SCRM programme, with upstream-coverage of OSS contributors and downstream-coverage of dependents integrated into the programme); the OSS-steward verifiable-documentation character of the policy supplies the auditability anchor under Art. 24(2) MSA cooperation (SR-CRA-073) — upon reasoned request the steward provides documentation of the cybersecurity policy and the relevant security aspects of the products they steward, with GV.SC-04 third-party-assessment dimension (MSA treated as a regulated assessor; cooperation duty operationalises the third-party-assessment-on-request function with documentation of policy + security aspects supplying the assessment record) + GV.OC-03 legal-and-regulatory-requirements-managed dimension (steward's regulatory requirements managed, with the request-triggered nature of the duty preserved — no standing reporting or audit); the presumption-of-conformity machinery is tracked at the conformity-assessment evidence layer via Art. 27(1) harmonised standards (SR-CRA-077) + Art. 27(2)/(5) common specifications via implementing acts + Art. 27(8) CSA certification at the assurance level specified by Art. 8(1) `substantial` or Art. 32(2)/(3) `high`, with GV.OC-03 standing duty to track the Official Journal list of harmonised standards and know which Annex I requirements each cited standard covers + GV.PO-02 common-specification fallback as documented process (the SDLC executes when no harmonised standard exists, and records the alternative solution adopted); the presumption is rebuttable — the OJ literal `presumed` signals a rebuttable presumption rather than a binding acquittal per general EU product-safety case law — and the coverage qualifier `to the extent that the standards cover those requirements` means that an Annex I requirement not addressed by the cited standard is not swept into the presumption and must be demonstrated by the manufacturer (partial-standard coverage shifts the burden back onto the manufacturer for un-addressed elements); for a controller-manufacturer (vertically-integrated entity that processes personal data AND ships CRA-regulated products), the CRA manufacturer-side policies and the GDPR controller-side data-protection policies coexist on different artefacts (manufacturer-side policies for product cybersecurity + controller-side data-protection policies for personal-data processing) on the GDPR↔CRA SAME — COMPLEMENTARY pair (different artefacts, different actors — no OJ-level consolidation rule, per CRDA-deep §9.1 GDPR↔CRA verified relationship); for a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair (Conditional Y when DORA entity procures CRA-conformant products, per CRDA-deep §9.1 CRA↔DORA verified relationship); for AI-enabled products that are both CRA-regulated and AI-Act high-risk, the CRA Annex I conformity stack coexists with the AI Act QMS stack on the CRA↔AI_Act SAME — COMPLEMENTARY pair (CRA on the product cybersecurity requirements + AI Act on the AI-system quality-management system; no OJ-level consolidation rule at 9.1 — unlike 9.2 where CRA Art. 13(4) sentence 2 permits AI Act Art. 9 risk management to substitute for CRA risk assessment, that rule covers the *risk-assessment object* not the *policy object*, per CRDA-deep §9.1 CRA↔AI_Act verified relationship); verified by manufacturer policies/processes/procedures documentation review + Annex VII technical documentation (cross to 9.4) + Art. 24(2) OSS-steward cooperation-on-request records + Annex II §8(a)-(f) instruction-set review (when product-side applies, cross to 8.1 partial) + Annex I Part I + Part II conformity-assessment records + Official Journal harmonised-standards list tracking + common-specification fallback procedure documentation + CSA certification records at the assurance level specified + MSA / ENISA inspection-ready evidence pack on request.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_14.md` (Art. 14) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 8 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.SC-01 — A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders — **CORE** — Action keyword ('supplier') in objective maps to GV.SC-01
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The management body of the financial entity **defines, approves, oversees and is respon... | DORA | sufficient | - | low |

### D-09.1 · DORA · subso SO-D-09.1.DORA
- **Objective**: The management body of the financial entity **defines, approves, oversees and is responsible for the implementation of all arrangements related to the ICT risk management framework** (Art. 5(2) DORA), supported by a **sound, comprehensive and well-documented ICT risk management framework** (Art. 6(1)) with a three-lines-of-defence model (Art. 6(4)).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 4 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OC-01 — The organizational mission is understood and informs cybersecurity risk management — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - GV.RM-02 — Risk appetite and risk tolerance statements are established, communicated, and maintained — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Financial entity operates a sound, comprehensive, well-documented ICT risk-management ... | DORA | sufficient | - | low |

### D-09.1 · DORA · req 9.1.4
- **Title**: "Financial entity operates a sound, comprehensive, well-documented ICT risk-management framework with three-lines-of-defence and identified, classified, documented ICT supported business functions and assets"
- **Description**: The product shall establish and maintain a sound, comprehensive, and well-documented ICT risk-management framework comprising strategies, policies, procedures, ICT protocols, and tools, with the management body defining, approving, overseeing, and being responsible for its implementation (per DORA Art. 5(2) four-verb coordination + Art. 6(1) framework + Art. 6(2) 5-artefact closed list), with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence according to the three lines of defence model (per Art. 6(4)), and with ICT supported business functions, information assets, and ICT assets identified, classified, and adequately documented (per Art. 7(1)).
- **Fit criterion (prose)**: A sound, comprehensive, and well-documented ICT risk-management framework is established under Art. 6(1) `which enables them to address ICT risk quickly, efficiently and comprehensively` (SR-DORA-027) with GV.PO-01 + GV.PO-02 + GV.RM-04 (the framework documents the entity's approach to ICT risk, supports the operational-procedure layer with documented processes and procedures, and couples policy formulation to strategic-direction and update-coupling); the framework comprises the Art. 6(2) 5-artefact closed list `strategies, policies, procedures, ICT protocols and tools`; the management body discharges the Art. 5(2) four-verb coordination (SR-DORA-026) `define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework` with GV.RR-01 leadership accountability + GV.RR-02 approval as documented governance act (the approval minute records the management body's reading of the framework, acceptance of residual risk, and resource commitment, creating executive sponsorship) + GV.OC-03 standing duty to track the full set of legal, regulatory, and contractual obligations that DORA adds on top of CRA, NIS 2, GDPR, and AI Act; the `define, approve, oversee and be responsible for` (S2 VAG + POLY + COORD per SR-DORA-026 ambiguity_notes) four-verb coordination carries the ambiguity on whether the four verbs are four distinct obligations or a composite — chosen reading: four distinct obligations (the OJ coordinates four verbs with commas and the conjunction `and`); the responsibility for managing and overseeing ICT risk is assigned to a control function with appropriate level of independence according to the three lines of defence model (or an internal risk management and control model) per Art. 6(4) (SR-DORA-027) with GV.RR-02 + GV.OC-03 (the three-lines-of-defence model is operationalised as a documented control-function independence architecture, with the operational-management function as first line, the risk-management and compliance function as second line, and the internal-audit function as third line, each with documented independence and reporting lines); ICT supported business functions, roles and responsibilities, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk are identified, classified and adequately documented per Art. 7(1) (SR-DORA-027 cross) with GV.OC-04 critical-objectives-and-capabilities understanding (the entity understands and communicates the ICT-supported business functions, the assets supporting those functions, and their roles and dependencies in relation to ICT risk) + GV.RM-05 upward-channel substrate (the CISO and relevant functions have documented escalation paths to the management body, including exception and incident reporting); the framework is documented under Art. 5(2) management-body oversight + EBA Guidelines on Internal Governance supervisory baseline + EBA Guidelines on ICT and security risk management; for smaller entities under Art. 4 proportionality, the framework is proportionate to the entity's risk exposure, size, and complexity; for a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities, per CRDA-deep §9.1 NIS2↔DORA verified relationship); for a DORA financial entity that is also a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR Art. 24(1) data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair (DORA-dominant for financial entities, per CRDA-deep §9.1 GDPR↔DORA verified relationship); for a DORA entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery discharges parts of the DORA supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the DORA framework obligation on the CRA↔DORA SAME — COMPLEMENTARY pair (Conditional Y when DORA entity procures CRA-conformant products, per CRDA-deep §9.1 CRA↔DORA verified relationship); for a DORA financial entity that deploys high-risk AI, the DORA ICT risk-management framework + AI Act QMS + Art. 26(1) deployer measures stack on the DORA↔AI_Act SAME — COMPLEMENTARY pair (three-lines-of-defence + QMS compatible governance architectures; DORA-led stack with AI Act QMS as sub-component, per CRDA-deep §9.1 DORA↔AI_Act verified relationship); verified by Art. 6(1) framework documentation review + Art. 5(2) management-body oversight records + Art. 6(2) 5-artefact closed-list records + Art. 6(4) three-lines-of-defence model documentation + Art. 7(1) ICT asset register + asset classification records + EBA Guidelines on ICT and security risk management supervisory-baseline documentation + NCA (national financial supervisory authority) review on request.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 7 action tokens with objective
  - GV.OC-04 — Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated — **CORE** — CSF title shares 4 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 5 action tokens with objective
  - GV.RM-05 — Lines of communication across the organization are established for cybersecurity risks, including risks from suppliers and other third parties — **CORE** — CSF title shares 8 action tokens with objective
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 6 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 8 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The controller implements **appropriate technical and organisational measures, such as ... | GDPR | excessive | - | low |

### D-09.1 · GDPR · subso SO-D-09.1.GDPR
- **Objective**: The controller implements **appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner** (Art. 24(1) GDPR), with the Art. 5(2) accountability burden and the DPO as the governance anchor (Art. 37-39).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.PO-01, GV.RM-04 — literal duplicate(s) of GV.PO-01, GV.RM-04
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller implements appropriate data-protection policies reviewed and updated where ... | GDPR | sufficient | - | low |

### D-09.1 · GDPR · req 9.1.1
- **Title**: "Controller implements appropriate data-protection policies reviewed and updated where necessary, with DPO designation, independence, and Art. 5(2) accountability"
- **Description**: The product shall establish, document, review, and update appropriate data-protection policies designed to implement data-protection principles in an effective manner (per GDPR Art. 24(1) + Art. 24(2)), with the DPO designated per Art. 37(1) triggers and operating with the independence, resources, and expert-knowledge maintenance required by Art. 38 (per Art. 38(1) timely involvement + Art. 38(2) resources + Art. 38(3) direct reporting + Art. 38(6) conflict-of-interests prohibition), and with Art. 5(2) accountability burden demonstrating continuous compliance with the Art. 5(1) principles.
- **Fit criterion (prose)**: Appropriate data-protection policies are documented and enforced under Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` (SR-GDPR-043) with GV.PO-01 policy-instrument discipline (every controller has a communicated, current, enforced cybersecurity-and-data-protection policy anchored on the Art. 24(2) proportionality test) + GV.PO-02 operational-procedure layer (each policy backed by documented processes — incident response, breach notification, data-subject rights, retention, processor onboarding — so the policy is real rather than paper) + GV.RM-04 strategic-direction and review-coupling (the controller communicates how it identifies and responds to risks, including the cadence and triggers for policy and procedure refresh, operationalising the Art. 24(1) `where necessary` review obligation on a material-change-of-risk trigger supplemented by annual periodic review per EDPB Guidelines 07/2019 on accountability); the policies are reviewed and updated `where necessary` against the material-change-of-risk trigger; the controller can demonstrate continuous compliance under Art. 5(2) accountability (SR-GDPR-044) with GV.PO-02 procedural-evidence backbone (RoPA entries, DPIA artefacts, audit logs, training records, breach-response records preserved on a continuous basis per EDPB Guidelines on accountability 07/2019) + GV.OV-03 evaluated-and-reviewed-correction dimension (controller's performance against cybersecurity and data-protection objectives measured and adjusted, with adjustments materialising as refreshed policies, processes, and procedures); a DPO is designated where any of the Art. 37(1) triggers applies (public authority + core-activity regular/systematic monitoring of data subjects on large scale + core-activity large-scale special-category or criminal-conviction processing), with Art. 37(7) publication of the designation (SR-GDPR-062), and operates with Art. 38 independence and resourcing (SR-GDPR-063): timely involvement in all Art. 38(1) issues relating to personal-data protection + Art. 38(2) resources necessary to carry out Art. 39 tasks + access to personal data and processing operations + expert-knowledge maintenance + Art. 38(3) direct reporting to highest management level with no instructions regarding exercise of Art. 39 tasks + Art. 38(4) protection against dismissal or penalty for performing tasks + Art. 38(6) conflict-of-interests prohibition (DPO may not hold roles with direct data-processing decision authority — head of marketing, head of IT operations, CISO where that role includes decisions about processing purposes or means — per EDPB Guidelines 3/2018 §6); the DPO performs the Art. 39(1) tasks with adequate independence, resources, and expert knowledge (advisory, monitoring, assurance); for an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance architecture extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair (NIS 2 management-body approval minute as governance hook on top of the GDPR policy artefact — policies are stacked not collapsed, per CRDA-deep §9.1 GDPR↔NIS2 verified relationship); for a DORA financial entity that is a controller, the DORA Art. 6(1) ICT risk-management framework is the carrier and the GDPR Art. 24(1) data-protection policies are a module within the framework on the GDPR↔DORA SAME — COMPLEMENTARY pair (DORA-dominant for financial entities, per CRDA-deep §9.1 GDPR↔DORA verified relationship); for a provider/deployer of high-risk AI that is also a controller, the AI Act QMS becomes a sub-policy of the GDPR data-protection policies on the GDPR↔AI_Act SAME — COMPLEMENTARY pair (AI Act Recital 78 explicit GDPR preservation, per CRDA-deep §9.1 GDPR↔AI_Act verified relationship); verified by Art. 24(1) data-protection policy documentation review + Art. 24(1) `where necessary` review-cadence records + Art. 5(2) accountability evidence pack (RoPA + DPIA + audit logs + training records + breach-response records) + Art. 37(7) DPO designation publication + Art. 38(3) direct-reporting documentation + Art. 38(6) conflict-of-interests assessment + DPA supervisory review on request.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 7 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 5 action tokens with objective
  - GV.RR-01 — Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving — **CORE** — CSF title shares 4 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 7 action tokens with objective
  - GV.RR-03 — Adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies — **CORE** — CSF title shares 9 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The management body of essential and important entities **approves the cybersecurity ri... | NIS2 | excessive | - | low |

### D-09.1 · NIS2 · subso SO-D-09.1.NIS2
- **Objective**: The management body of essential and important entities **approves the cybersecurity risk-management measures, oversees their implementation, and can be held liable for infringements** (Art. 20(1) sentence 1 NIS 2); the entity adopts **policies on risk analysis and information system security** (Art. 21(2)(a)) and **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f)).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-01 — Improvements are identified from evaluations — **UTILITY** — Reinforces obligation in same CSF function (IDENTIFY) but does not directly match the action
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 5 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.PO-01 — literal duplicate(s) of GV.PO-01
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Essential and important entities establish policies on risk analysis, information syst... | NIS2 | sufficient | - | low |

### D-09.1 · NIS2 · req 9.1.2
- **Title**: "Essential and important entities establish policies on risk analysis, information system security, and effectiveness assessment, approved and overseen by the management body"
- **Description**: The product shall establish and maintain documented policies on risk analysis and information system security (per NIS 2 Art. 21(2)(a)) and policies and procedures to assess the effectiveness of cybersecurity risk-management measures (per NIS 2 Art. 21(2)(f)), with the management body approving the Art. 21 measures and overseeing their implementation (per Art. 20(1) sentence 1 first-clause `approve` + second-clause `oversees`) and bearing personal liability for infringements (per Art. 20(1) sentence 1 third-clause `can be held liable`).
- **Fit criterion (prose)**: Documented policies are established and maintained under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) documenting the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems, and under Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` (SR-NIS2-036) with results feeding back into the risk-management cycle, with the depth calibrated by Art. 21(1) `appropriate and proportionate` chapeau + state-of-the-art floor (Art. 21(1) sentence 2) + Recital 56 proportionality (nature/size/risk profile/cost of implementation); the management body formally approves the Art. 21 measures through a documented approval minute (SR-NIS2-032) with GV.RR-02 approval as documented governance act (the approval minute records the management body's reading of the measures, acceptance of residual risk, and resource commitment, creating executive sponsorship) + GV.PO-01 downstream enforceability (the approved measures become the binding organisational cybersecurity policy); the management body continuously oversees the implementation (SR-NIS2-033) with GV.OV-01 active-monitoring dimension (management body reviews implementation status, receives exception reports, interrogates the CISO on residual-risk drift, authorises adjustments to the Art. 21 measures as the threat landscape and entity exposure evolve) + GV.RM-05 upward-channel substrate (the CISO and relevant functions have documented escalation paths to the management body, including exception and incident reporting); the management body bears personal liability for Art. 21 infringements (SR-NIS2-034) under Art. 20(1) sentence 1 third-clause `can be held liable` — the literacy prerequisite is the Art. 20(2) sentence 1 training obligation (cross-ref 8.3.1) which makes the management body structurally positioned to discharge Art. 20(1) oversight responsibilities with informed judgement; the policy artefact is layered under Art. 21(1) chapeau with the three policy records (Art. 21(2)(a) risk-analysis + IS-security policies + Art. 21(2)(f) effectiveness-assessment policies + procedures) and the management-body approval minute as governance hook; the policy content is entity-discretionary under Recital 56 proportionality — the OJ does not enumerate specific content; for an integrated controller-NSIE, the NIS 2 management-body approve/oversee/liable governance architecture extends to the GDPR data-protection policies on the GDPR↔NIS2 SAME — COMPLEMENTARY pair (NIS 2 management-body approval minute as governance hook on top of the GDPR policy artefact — policies are stacked not collapsed, per CRDA-deep §9.1 GDPR↔NIS2 verified relationship); for a DORA financial entity that is also an NSIE, the DORA Art. 6(1) ICT risk-management framework discharges both DORA's dedicated framework obligation and NIS 2's Art. 21(2)(a)+(f) policy artefacts + Art. 20(1) governance act on the NIS 2 ↔ DORA SAME — EQUAL pair (DORA-dominant stack for financial entities, per CRDA-deep §9.1 NIS2↔DORA verified relationship); for an NSIE that deploys high-risk AI, the AI Act QMS becomes a sub-policy of the entity-level NIS 2 governance framework on the NIS2↔AI_Act SAME — COMPLEMENTARY pair (the AI Act layer adds the AI-specific 13-element QMS to the NIS 2 risk-analysis policy, per CRDA-deep §9.1 NIS2↔AI_Act verified relationship); for an entity that procures CRA-conformant products, the CRA presumption-of-conformity machinery substitutes for parts of the NIS 2 supplier-assessment evidence obligation (cross to 6.1) but does not substitute for the NIS 2 entity-level policy architecture on the NIS2↔CRA SAME — COMPLEMENTARY pair (Conditional Y when entity procures CRA-conformant products, per CRDA-deep §9.1 NIS2↔CRA verified relationship); verified by Art. 21(2)(a) + Art. 21(2)(f) policy-records review + Art. 20(1) management-body approval minute + Art. 20(1) oversight records (board minutes + dashboard reviews + exception registers) + Art. 21(1) chapeau documented-policies evidence + Member State supervisory review (national NIS 2 supervisory authority) on request.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_17.md` (Art. 17) — paraphrased action
- **Anchors listed**:
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 5 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.RM-05 — Lines of communication across the organization are established for cybersecurity risks, including risks from suppliers and other third parties — **CORE** — CSF title shares 8 action tokens with objective
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 7 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-09.2 Impact & Risk Assessments

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| A risk management system is **established, implemented, documented and maintained** in ... | AI_Act | sufficient | - | low |

### D-09.2 · AI_Act · subso SO-D-09.2.AI_Act
- **Objective**: A risk management system is **established, implemented, documented and maintained** in relation to high-risk AI systems (Art. 9(1) AI Act), comprising the four Art. 9(2)(a)-(d) steps: identify and analyse known and reasonably foreseeable risks; estimate and evaluate reasonably-foreseeable-misuse risks; evaluate post-market-monitoring-data risks; and adopt appropriate and targeted risk-management measures.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.RM-06 — A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - ID.RA-06 — Risk responses are chosen, prioritized, planned, tracked, and communicated — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Provider establishes, implements, documents, and maintains a continuous iterative risk... | AI_Act | sufficient | - | low |

### D-09.2 · AI_Act · req 9.2.5
- **Title**: "Provider establishes, implements, documents, and maintains a continuous iterative risk-management system across the AI lifecycle with the four Art. 9(2)(a)-(d) steps, cross-coupled with Art. 27 FRIA for certain Annex III categories"
- **Description**: The product shall ensure that the provider of a high-risk AI system establishes, implements, documents, and maintains a continuous iterative risk-management system across the AI lifecycle (per AI Act Art. 9(1)) running the four Art. 9(2)(a)-(d) steps (identify/analyse known + reasonably foreseeable risks; estimate/evaluate reasonably-foreseeable-misuse risks; evaluate post-market-monitoring-data risks; adopt appropriate and targeted risk-management measures), cross-coupled with Art. 27 FRIA documentation for certain Annex III categories.
- **Fit criterion (prose)**: A continuous iterative risk-management system is established, implemented, documented, and maintained across the AI lifecycle under Art. 9(1) `established, implemented, documented and maintained` (SR-AIACT-001) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 9(2)(a) `the identification and analysis of the known and the reasonably foreseeable risks to health, safety and fundamental rights` + Art. 9(2)(b) `the estimation and evaluation of the risks emerging from use under conditions of reasonably foreseeable misuse` + Art. 9(2)(c) `the evaluation of other risks arising from analysis of post-market monitoring data`) + GV.RM-04 strategic-direction-and-review-coupling dimension (Art. 9(2)(d) `the adoption of appropriate and targeted risk-management measures` with documented feedback into the AI lifecycle); the risk-management system runs the **4-step Art. 9(2)(a)-(d) process**: (a) identify and analyse known and reasonably foreseeable risks to health, safety and fundamental rights; (b) estimate and evaluate risks emerging from use under conditions of reasonably foreseeable misuse (adversarial use + out-of-scope use + accidental misuse); (c) evaluate other risks arising from analysis of post-market monitoring data per Art. 72 + Art. 73 incident reporting; (d) adopt appropriate and targeted risk-management measures (elimination first where reasonably practicable, then engineering controls + protective + information measures); the system is **continuous iterative** across the AI lifecycle (design → development → placement on market → operation → post-market monitoring → significant modification → decommissioning) with documented iteration triggers and review cadences; the system is **cross-coupled** with Art. 27 FRIA for certain Annex III categories (deployer-side Fundamental Rights Impact Assessment) where the high-risk AI system is in Annex III and deployed by public authorities + private actors providing public services + banking + insurance + employment + law enforcement + migration + justice + democratic-process use cases — the FRIA documents the fundamental-rights risk dimension that complements the Art. 9 risk-management system on the deployer side; **CRITICAL consolidation rule** — CRA Art. 13(4) sentence 2 unification: for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment (per SR-CRA-066 ambiguity_notes); this is the ONLY OJ-level cross-regulation consolidation rule in 9.2; the unified artefact must satisfy BOTH Art. 9(2)(a)-(d) + Art. 13(3) sentence 1-3 content (intended purpose + reasonably foreseeable use + Annex I Part I (2) applicability mapping); the provider can demonstrate ex post, against the market surveillance authority + AI Office, that the Art. 9(1) risk-management system was carried out across the AI lifecycle with the 4-step Art. 9(2)(a)-(d) process documented and integrated with Art. 27 FRIA documentation for certain Annex III categories; the provider coordinates with deployer measures per Art. 26(1) `use of the high-risk AI system in accordance with the instructions for use accompanying the system` with the deployer-side Art. 4(5) + Art. 26(1) human-oversight measures layered on the provider-side risk-management measures; **AI Act risk management does NOT address data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the AI Act Art. 9 risk-management system is in place; AI Act Recital 78 explicit GDPR preservation.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2... | CRA | sufficient | - | low |

### D-09.2 · CRA · subso SO-D-09.2.CRA
- **Objective**: The manufacturer documents the **cybersecurity risk assessment referred to in Art. 13(2)** and updates it as appropriate during the support period, with the assessment covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2) and indicating Annex I Part I (2) applicability (Art. 13(3) sentence 3) — documented in the **Annex VII §3 risk-assessment record** (Art. 13(4) sentence 1 + Annex VII §3 CRA).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Manufacturer documents the cybersecurity risk assessment referred to in Art. 13(2) cov... | CRA | sufficient | - | low |

### D-09.2 · CRA · req 9.2.3
- **Title**: "Manufacturer documents the cybersecurity risk assessment referred to in Art. 13(2) covering intended purpose + reasonably foreseeable use + Annex I Part I (2) applicability, updated during support period and recorded in Annex VII §3"
- **Description**: The product shall ensure that the manufacturer documents and updates, during the support period, the cybersecurity risk assessment referred to in Art. 13(2) covering intended purpose and reasonably foreseeable use (Art. 13(3) sentence 2), indicating how Annex I Part I (2) requirements apply and are implemented (Art. 13(3) sentence 3), with the assessment drawn up before placing the product on the market and updated during the support period (Art. 13(4) sentence 1 + Art. 31(2)) — documented in the Annex VII §3 risk-assessment record, and subject to the CRA Art. 13(4) sentence 2 consolidation rule where applicable.
- **Fit criterion (prose)**: The cybersecurity risk assessment is documented under Art. 13(3) sentence 1 `documented and updated` (SR-CRA-064) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 13(2) `cybersecurity risk assessment … taking into account the intended purpose and reasonably foreseeable use, including operational environment and assets to be protected`) + GV.SC-07 suppliers-prioritised-by-criticality dimension (the supplier-side risk-assessment perspective informing the manufacturer risk assessment, cross to 6.1); the assessment covers per Art. 13(3) sentence 2 the intended purpose + reasonably foreseeable use including operational environment and assets to be protected, with reasonable foreseeability scoped to `intentional misuses … as well as in those uses which are reasonably foreseeable by the manufacturer`; the assessment indicates per Art. 13(3) sentence 3 `whether and in what manner the Annex I Part I (2) requirements apply to the relevant product and how those requirements are implemented as informed by the risk assessment` — the applicability mapping from Annex I Part I (2) to the product's circumstances; the assessment is documented in the Annex VII §3 risk-assessment record per Art. 13(4) sentence 1 `The product with digital elements shall be accompanied by the technical documentation referred to in Annex VII` + Annex VII §3 (per SR-CRA-066 ambiguity_notes); the assessment is drawn up before placing on the market and updated during the support period per Art. 13(3) sentence 1 `updated as appropriate` + Art. 13(7) `upon becoming aware of a previously unidentified vulnerability` + Art. 13(8) support period + Art. 31(2) `drawn up before placing on the market and updated during the support period`; the assessment is retained at the disposal of market surveillance authorities for at least 10 years after placement on the market or the support period, whichever is longer, per Art. 13(13); the assessment is subject to the presumption-of-conformity machinery per Art. 27(1)/(2)/(5)/(8)/(9) where harmonised standards / common specifications / European cybersecurity certification scheme under Regulation (EU) 2019/881 apply — the presumption discharges the CRA conformity-assessment obligation where alignment exists (per SR-CRA-066 ambiguity_notes); **CRITICAL consolidation rule — CRA Art. 13(4) sentence 2**: `The cybersecurity risk assessment referred to in paragraph 2 shall be part of, or combined with, the risk assessment required by other Union legal acts applicable to the product with digital elements` — for AI-enabled CRA-regulated products (the SAME product is both CRA-regulated and AI-Act high-risk), a unified AI Act Art. 9 risk-management system substitutes for the CRA Art. 13(3) cybersecurity risk assessment on a single artefact (per SR-CRA-066 ambiguity_notes); this is the ONLY OJ-level cross-regulation consolidation rule in 9.2 and no other cross-regulation substitution is OJ-permitted (the GDPR DPIA on data-subject rights must be a separate artefact even when CRA cybersecurity risk assessment performed, per CRDA flag DomainAnalysis §9.2 line 175); the manufacturer can demonstrate ex post, against the market surveillance authority, that the Art. 13(3) sentence 1 documented-and-updated risk assessment was carried out with the Annex VII §3 risk-assessment record + Annex I Part I (2) applicability mapping + on-material-change update per Art. 13(7) + 10-year retention per Art. 13(13).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.SC-07 — The risks posed by a supplier, their products and services, and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship — **CORE** — CSF title shares 6 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities shall, on a continuous basis, **identify all sources of ICT risk** i... | DORA | sufficient | - | low |

### D-09.2 · DORA · subso SO-D-09.2.DORA
- **Objective**: Financial entities shall, on a continuous basis, **identify all sources of ICT risk** including risk exposure to and from other financial entities, and **assess cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets** (Art. 7(2) sentence 1 DORA); risk scenarios are reviewed on a regular basis, and at least yearly (Art. 7(2) sentence 2), under a three-lines-of-defence model (Art. 6(4) DORA).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 3 action tokens with objective
  - GV.RM-02 — Risk appetite and risk tolerance statements are established, communicated, and maintained — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Financial entity continuously identifies ICT risks and reviews risk scenarios at least... | DORA | sufficient | - | low |

### D-09.2 · DORA · req 9.2.4
- **Title**: "Financial entity continuously identifies ICT risks and reviews risk scenarios at least yearly under the three-lines-of-defence model with classification and documentation per Art. 7(1)-(2)"
- **Description**: The product shall ensure that the financial entity, on a continuous basis, identifies all sources of ICT risk and assesses cyber threats and ICT vulnerabilities relevant to its ICT supported business functions, information assets, and ICT assets (per DORA Art. 7(2) sentence 1), with risk scenarios reviewed on a regular basis and at least yearly (per Art. 7(2) sentence 2), under a three-lines-of-defence model (per Art. 6(4)) and with identification / classification / documentation per Art. 7(1).
- **Fit criterion (prose)**: The financial entity's ICT risk identification register is maintained on a continuous basis under Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk … including the risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities relevant to ICT supported business functions, information assets and ICT assets` (SR-DORA-028) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (the register identifies ICT risk sources + exposure to/from other financial entities + cyber threats + ICT vulnerabilities, mapped to the ICT supported business functions / information assets / ICT assets identified and classified per Art. 7(1) `identify, classify and adequately document all ICT supported business functions … the information assets and ICT assets` cross-ref 9.3) + GV.RR-02 management-body approve/oversee dimension (the register is management-body-overseen per Art. 5(2) four-verb coordination `define, approve, oversee and be responsible for`); the register is operated under the **three-lines-of-defence model** per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line) with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence; the risk-scenario review is conducted on a regular basis and at least yearly per Art. 7(2) sentence 2 `review on a regular basis, and at least yearly, the risk scenarios impacting them`, with the depth calibrated to Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities`; the register and review records are retained per EBA Guidelines on ICT and security risk management supervisory baseline; the register coordinates with Art. 7(1) ICT asset inventory (cross to 9.3 DORA sub-SO) and the Art. 6(1) ICT risk-management framework (cross to 9.1 DORA sub-SO); for financial entities under DORA's direct scope, the **continuous + at-least-yearly ICT risk framework** discharges both DORA's dedicated risk-identification obligation and NIS 2's Art. 21(2)(a) continuous operational risk-analysis policy on the DORA-dominant stack — EQUAL classification (per CRDA flag DomainAnalysis §9.2 line 110-114); the management body's Art. 5(4) `actively keep up to date` training obligation (cross-ref 8.3.2) is the literacy prerequisite for the Art. 5(2) define/approve/oversee/be-responsible architecture; **DORA ICT risk framework does NOT extend to data-subject rights** (per CRDA flag DomainAnalysis §9.2 line 175): the GDPR DPIA on data-subject rights must be a separate artefact even when the DORA ICT risk framework is in place; **DORA has no equivalent to CRA Art. 13(4) sentence 2** — the DORA ↔ AI_Act pair has no OJ-level consolidation rule.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.RR-02 — Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Prior to processing that is likely to result in a high risk to the rights and freedoms ... | GDPR | sufficient | - | low |

### D-09.2 · GDPR · subso SO-D-09.2.GDPR
- **Objective**: Prior to processing that is likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a **data-protection impact assessment** covering the four Art. 35(7) content items and reviewed on change of risk per Art. 35(11) (Art. 35(1) + Art. 35(7) GDPR).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_27.md` (Art. 27) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.RA-06 — Risk responses are chosen, prioritized, planned, tracked, and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - RS.AN-03 — Analysis is performed to establish what has taken place during an incident and the root cause of the incident — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller carries out a pre-launch DPIA covering the four Art. 35(7) content items be... | GDPR | sufficient | - | low |

### D-09.2 · GDPR · req 9.2.1
- **Title**: "Controller carries out a pre-launch DPIA covering the four Art. 35(7) content items before high-risk personal-data processing, reviewed on change of risk per Art. 35(11) and submitted for prior consultation where residual risk is high"
- **Description**: The product shall ensure that, prior to processing likely to result in a high risk to the rights and freedoms of natural persons, the controller carries out a data-protection impact assessment (DPIA) covering the four Art. 35(7) content items (systematic description of envisaged processing + necessity-and-proportionality assessment + risks to rights and freedoms + measures envisaged to address the risks), reviewed on change of risk per Art. 35(11), and submitted for prior consultation under Art. 36(1) where residual risk remains high.
- **Fit criterion (prose)**: A pre-launch DPIA is documented and maintained under Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` (SR-GDPR-045) covering the 4-item Art. 35(7) content list (SR-GDPR-046) with ID.RA-04 impact-and-likelihood dimension (Art. 35(7)(c) `assessment of the risks to the rights and freedoms of data subjects` + Art. 35(7)(d) `measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation`) + ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 35(7)(c) impact on data-subject rights and freedoms under Art. 5(1) principles); the DPIA identifies whether the processing falls within Art. 35(3)(a)-(d) mandatory-DPIA cases (systematic + extensive evaluation + large-scale special-category / systematic monitoring on large scale / innovative use of new technologies / automated decision-making with legal/similar effect) or the DPA-published Art. 35(4) blacklist; the DPIA is reviewed on change of risk per Art. 35(11) `review … where there has been a change of the risk represented by processing operations`, with material-change-of-risk trigger supplemented by a documented periodic-review cadence; the DPIA is submitted for prior consultation under Art. 36(1) where the residual risk remains high, with the controller documenting the consultation outcome in the accountability records under Art. 5(2); the DPIA is one of the records to be retained per Art. 5(2) accountability burden and is made available on request to the supervisory authority (DPA) with the DPIA content demonstrable against the 4-item Art. 35(7) list; the Art. 26 joint-controller arrangement is reflected in the DPIA with the joint-controller roles allocated per Art. 26(1) (cross to D-06.3); the Art. 35(11) review records identify the trigger event, the date, the assessment of the change, the residual-risk recalculation, and any updated measures; the controller can demonstrate Art. 5(2) accountability for the DPIA process with continuity of evidence (DPIA + reviews + prior-consultation records preserved on a continuing basis, EDPB Guidelines on accountability 07/2019); the DPIA coordinates with the DPO per Art. 39(1)(c) advice obligation (cross to 9.1 GDPR sub-SO DPO anchor); **CRDA flag — GDPR DPIA does NOT address cybersecurity risk** (DomainAnalysis §9.2 line 175): the DPIA's risk object is data-subject rights and freedoms; the CRA Art. 13(3) cybersecurity risk assessment or the NIS 2 Art. 21(2)(a) risk-analysis policy or the DORA Art. 7(2) ICT risk framework discharges the cybersecurity-risk-assessment obligation on a **separate artefact** — the DPIA is stacked, not collapsed with the cybersecurity assessments.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Essential and important entities establish **policies on risk analysis and information ... | NIS2 | excessive | - | low |

### D-09.2 · NIS2 · subso SO-D-09.2.NIS2
- **Objective**: Essential and important entities establish **policies on risk analysis and information system security** (Art. 21(2)(a) NIS 2) on a continuous basis, taking into account the proportionality factors (degree of exposure, likelihood of incidents, severity, state of the art, costs of implementation per Recital 56); the Cooperation Group may carry out coordinated supply-chain risk assessments under Art. 22(1) NIS 2 that NSIEs take into account per Art. 21(3) sentence 2.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.RM-06 — A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-06 — Risk responses are chosen, prioritized, planned, tracked, and communicated — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-01 — Networks and environments are protected from unauthorized logical access and usage — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-05 — literal duplicate(s) of ID.RA-05
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Essential and important entities establish and maintain documented policies on risk an... | NIS2 | sufficient | - | low |

### D-09.2 · NIS2 · req 9.2.2
- **Title**: "Essential and important entities establish and maintain documented policies on risk analysis and information system security on a continuous basis with all-hazards methodology and Cooperation Group coordinated-assessments ingestion"
- **Description**: The product shall ensure that the essential or important entity establishes and maintains, on a continuous basis, documented policies on risk analysis and information system security (per NIS 2 Art. 21(2)(a)) with an all-hazards methodology calibrated by the Art. 21(1) `appropriate and proportionate` chapeau and the Recital 56 proportionality factors, ingesting the EU-level Cooperation Group coordinated supply-chain risk assessments per Art. 22(1) via Art. 21(3) sentence 2.
- **Fit criterion (prose)**: Documented policies on risk analysis and information system security are established and maintained on a continuous basis under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems) + GV.OV-01 management-body oversight dimension (the policies are management-body-approved per Art. 20(1) sentence 1 first-clause `approve` + continuously-overseen per second-clause `oversees`); the policies apply an **all-hazards methodology** per SR-NIS2-040 covering cyber + non-cyber hazards (natural disasters + power failures + human errors + malicious acts + supply-chain disruptions + technical failures) with the depth calibrated by Art. 21(1) chapeau `appropriate and proportionate … taking into account the degree of exposure of the entity to risks … the likelihood of incidents … their severity` + state-of-the-art floor per Art. 21(1) sentence 2 + Recital 56 cost factor; the entity incorporates the EU-level Cooperation Group coordinated supply-chain risk assessments per Art. 22(1) into its risk-analysis policy per Art. 21(3) sentence 2 (cross to 9.4); the management body formally approves the Art. 21(2)(a) policy through a documented approval minute; the policy is reviewed and updated on a material-change-of-risk trigger (e.g., new threat landscape, organisational change, new critical-asset class, Art. 22(1) coordinated-assessment publication) with cadence entity-discretionary under Recital 56; the policy identifies the risk-analysis scope (information systems supporting essential services + business processes + supporting assets), the risk methodology (asset-threat-vulnerability-impact combination scoring, or equivalent), the risk-treatment options (accept / mitigate / transfer / avoid), the residual-risk acceptance chain, and the responsible functions; for DORA financial entities under DORA's direct scope, the DORA Art. 6(4) three-lines-of-defence + Art. 7(2) sentence 1 continuous + sentence 2 at-least-yearly discharge both DORA's dedicated continuous + at-least-yearly ICT risk-identification obligation and NIS 2's Art. 21(2)(a) continuous operational risk-analysis policy — DORA-dominant stack with EQUAL classification; the management body's Art. 20(2) sentence 1 training obligation (cross-ref 8.3.1) is the literacy prerequisite for the Art. 20(1) approve/oversee/liable architecture.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 6 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-09.3 Asset Inventories

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Manufacturers of products with digital elements draw up **technical documentation** con... | CRA | sufficient | - | low |

### D-09.3 · CRA · subso SO-D-09.3.CRA
- **Objective**: Manufacturers of products with digital elements draw up **technical documentation** containing at least a **general description** of the product (Annex VII §1) and a **description of the design, development, production and vulnerability-handling processes** including the system architecture description (Annex VII §2); the technical documentation is drawn up before placing on the market and updated during the support period (Art. 31(2) CRA), and kept at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 3 action tokens with objective
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-04
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Manufacturer draws up product-level technical documentation containing at least the ge... | CRA | sufficient | - | low |

### D-09.3 · CRA · req 9.3.2
- **Title**: "Manufacturer draws up product-level technical documentation containing at least the general description and the design/development/production/vulnerability-handling-processes architecture description per Annex VII §1-§2"
- **Description**: The product shall ensure that the manufacturer of a product with digital elements draws up technical documentation containing at least a general description of the product (Annex VII §1) and a description of the design, development, production, and vulnerability-handling processes including the system architecture description (Annex VII §2), with the technical documentation drawn up before placing on the market and updated during the support period.
- **Fit criterion (prose)**: The technical documentation is drawn up under Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production and vulnerability-handling processes` (system architecture description documenting how software components build on or feed into each other) (per SR-CRA-087 + SR-CRA-088) with ID.AM-01 hardware-inventory dimension (the documentation identifies the software versions affecting compliance + hardware external features supporting compliance with Annex I) + ID.AM-02 software-services-systems-inventory dimension (the documentation identifies how the system architecture components build on or feed into each other, providing the upstream sub-register for the entity-level master record); the technical documentation is **drawn up before placing on the market and updated during the support period** per Art. 31(2) `drawn up before placing on the market and updated during the support period` (SR-CRA-087 + Art. 13(8) support period); the technical documentation is **retained at the disposal of market surveillance authorities for at least 10 years after placement on the market or the support period, whichever is longer** per Art. 13(13) `made available to the market surveillance authorities for at least 10 years after the placement on the market of the product with digital elements or for the support period, whichever is longer`; the manufacturer acts as governance body per Art. 13(8) (cross to 9.1 CRA sub-SO 9.1.3 for the manufacturer policies/processes/procedures owner), distinct from the data-protection governance body under GDPR; for AI Act high-risk components of the product, the Annex VII §1-§2 documentation cross-references the AI Act Art. 9 risk-management-system records (which serve as the cybersecurity evidence layer for both CRA + AI Act under CRA Art. 13(4) sentence 2 consolidation); the documentation is subject to the presumption-of-conformity machinery per Art. 27(1)/(2)/(5)/(8)/(9) where harmonised standards / common specifications / European cybersecurity certification scheme under Regulation (EU) 2019/881 cover the Annex VII content; **CRA partial coverage**: CRA Annex VII §1-§2 is documentation-centric (general description + architecture), NOT a formal asset register in the DORA sense; **partial coverage only**; the partial coverage does NOT substitute for the NIS 2 entity-level asset-management sub-domain (substantively scope-disjoint per CRDA `N (typically)`) or the DORA entity-level `3-way AND` inventory (different audit purposes — product-level MSA review vs. entity-level NCA review); the recipient is the **market surveillance authority (MSA)** on Annex VII §1 `general description` + Annex VII §2 `design, development, production and vulnerability-handling processes` + 10-year technical-documentation retention per Art. 13(13) (cross to 9.4 for the records-of-processing layer) + conformity-assessment records per Art. 27 + Article 31(2) `drawn up before placing on the market and updated during the support period`.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-02
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities **identify, classify and adequately document all ICT supported busin... | DORA | sufficient | - | high |

### D-09.3 · DORA · subso SO-D-09.3.DORA
- **Objective**: Financial entities **identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk** (Art. 7(1) DORA — the dedicated authority with explicit OJ-literal `3-way AND`); responsibility for managing and overseeing ICT risk is assigned to a control function with appropriate independence per the three lines of defence model (Art. 6(4) DORA).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial entity identifies, classifies, and adequately documents ICT supported busine... | DORA | sufficient | - | high |

### D-09.3 · DORA · req 9.3.3
- **Title**: "Financial entity identifies, classifies, and adequately documents ICT supported business functions + roles and responsibilities + information assets + ICT assets + dependencies in relation to ICT risk under three-lines-of-defence and management-body governance"
- **Description**: The product shall ensure that the financial entity identifies, classifies, and adequately documents all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk (per DORA Art. 7(1)) — with the inventory operated under the three-lines-of-defence model (per Art. 6(4)) and approved by the management body under the Art. 5(2) four-verb coordination.
- **Fit criterion (prose)**: The financial entity maintains a dedicated entity-level asset inventory under Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporting those functions, and their roles and dependencies in relation to ICT risk` (per SR-DORA-029) (per CRDA DomainAnalysis §9.3 line 80 — **DORA Art. 7(1) is the dedicated authority with explicit OJ-literal anchor**) with ID.AM-01 hardware-inventory dimension (Art. 7(1) `information assets` + `ICT assets` dimension mapped to NIST CSF 2.0 ID.AM-01) + ID.AM-02 software-services-systems-inventory dimension (Art. 7(1) `ICT supported business functions` + software-inventory dimension mapped to NIST CSF 2.0 ID.AM-02) + **ID.AM-05 assets-prioritised-by-criticality dimension** (Art. 7(1) `classify` dimension mapped to NIST CSF 2.0 ID.AM-05 — **classification dimension unique to DORA** among the 3 participating regs; NIS 2 does not impose the classify dimension; CRA does not impose the classify dimension); the inventory demonstrates the **3-way AND** chain of (1) ICT supported business functions + (2) information assets + (3) ICT assets, with the **+ roles and responsibilities + dependencies** extensions per Art. 7(1) (the OJ-literal chain includes ICT supported business functions, roles and responsibilities, information assets, ICT assets, and their roles and dependencies — 3 primary + 2 extensions); the inventory is operated under the **three-lines-of-defence model** per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line) with responsibility for managing and overseeing ICT risk assigned to a control function with appropriate level of independence; the inventory is approved and overseen by the management body under the **Art. 5(2) four-verb coordination** `define, approve, oversee and be responsible for` (cross to 9.1 DORA sub-SO 9.1.4 for the four-verb coordination); the depth and granularity are calibrated by Art. 4 proportionality `in relation to the size, nature, scale and complexity of the financial entity's activities`; for DORA financial entities that are also NSIEs, the **DORA Art. 7(1) `3-way AND` discharges both the NIS 2 Art. 21(2)(i) partial-coverage asset-management dimension and DORA's dedicated Art. 7(1) obligation** — DORA-dominant stack with EQUAL classification on entity-level asset inventory; for DORA financial entities that procure CRA-conformant products, the CRA Annex VII §1-§2 architecture documentation is an upstream **product-level sub-register** feeding the DORA entity-level master record — DORA-led stack with CRA as upstream product-level sub-register (per CRDA-deep §9.3 line 146); the **classification dimension** (Art. 7(1) `classify`) is **unique to DORA** among the 3 participating regs — NIS 2 and CRA provide partial coverage only with no classify dimension; the recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on Art. 7(1) ICT asset register + Art. 6(4) three-lines-of-defence + Art. 5(2) management-body define/approve/oversee/be responsible + EBA Guidelines on ICT and security risk management supervisory baseline.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — Action keyword ('inventory') in objective maps to ID.AM-02
  - ID.AM-05 — Assets are prioritized based on classification, criticality, resources, and impact on the mission — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| Essential and important entities adopt **access control policies coordinated with human... | NIS2 | excessive | - | high |

### D-09.3 · NIS2 · subso SO-D-09.3.NIS2
- **Objective**: Essential and important entities adopt **access control policies coordinated with human resources security and asset management** (Art. 21(2)(i) NIS 2), with the management body approving, overseeing, and being liable for the cybersecurity risk-management measures (Art. 20(1) sentence 1 NIS 2).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — Action keyword ('asset') in objective maps to ID.AM-01
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.AM-01, ID.AM-02, PR.PS-01 — literal duplicate(s) of ID.AM-01, ID.AM-02, PR.PS-01
- **Confidence**: high (article mapping and CSF title both consulted)

| "Essential and important entities adopt asset-management sub-domain coordinated with ac... | NIS2 | sufficient | - | high |

### D-09.3 · NIS2 · req 9.3.1
- **Title**: "Essential and important entities adopt asset-management sub-domain coordinated with access control under NIS 2 Art. 21(2)(i), approved and overseen by the management body"
- **Description**: The product shall ensure that the essential or important entity adopts access control policies coordinated with human resources security and asset management (per NIS 2 Art. 21(2)(i)), with the management body approving the Art. 21 cybersecurity risk-management measures and overseeing their implementation (per Art. 20(1) sentence 1).
- **Fit criterion (prose)**: The Art. 21(2)(i) sub-domain `human resources security, access control policies and asset management` (SR-NIS2-005) is established as one of three coordinated sub-domains of access control (HR security + access control + asset management) with PR.PS-01 configuration-management dimension (the entity demonstrates ex post that asset-management is established, reviewed, and updated in light of the proportionality factors — degree of exposure + likelihood of incidents + severity per Recital 56) + ID.AM-01 hardware-inventory dimension (entity demonstrates that inventories of hardware managed within the system are maintained, classified, and reviewed) + ID.AM-02 software-services-systems-inventory dimension (entity demonstrates that inventories of software, services, and systems managed are maintained, classified, and reviewed); the depth is entity-discretionary under Recital 56 proportionality + Art. 21(1) chapeau `appropriate and proportionate` + state-of-the-art floor (Art. 21(1) sentence 2) + cost factor; the management body formally approves the Art. 21(2)(i) sub-domain through a documented approval minute (cross to 9.1 NIS 2 sub-SO 9.1.2 for the management-body approve/oversee/liable architecture); for DORA financial entities under DORA's direct scope, the **DORA Art. 7(1) `3-way AND` inventory obligation is the dominant authority** and discharges both DORA's dedicated Art. 7(1) obligation and NIS 2's Art. 21(2)(i) partial-coverage asset-management dimension (cross-coupled via access-control) — DORA-dominant stack with EQUAL classification on entity-level asset inventory; for non-financial NSIEs, NIS 2 Art. 21(2)(i) partial coverage stands alone (no DORA Art. 7(1) obligation); the Art. 21(2)(i) sub-domain does NOT impose a dedicated asset-inventory mandate (per CRDA `NIS 2 does not impose a dedicated asset-inventory mandate`); the recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on Art. 21(2)(i) asset-management sub-domain + Art. 20(1) management-body approval records.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - ID.AM-01 — Inventories of hardware managed by the organization are maintained — **CORE** — CSF title literally matches action keyword ('inventories')
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title literally matches action keyword ('inventories')
  - PR.PS-01 — Configuration management practices are established and applied — **CORE** — CSF title literally matches action keyword ('configuration')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-09.4 Records of Processing

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Providers of high-risk AI systems **draw up and keep up-to-date the technical documenta... | AI_Act | sufficient | - | low |

### D-09.4 · AI_Act · subso SO-D-09.4.AI_Act
- **Objective**: Providers of high-risk AI systems **draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service** (Art. 11(1) AI Act), **keep the logs automatically recorded by the high-risk AI system to the extent under their control** (Art. 19(1) AI Act), and document the **quality management system** in written policies, procedures, and instructions covering at least the 13 enumerated aspects (a)-(m) (Art. 17(1) AI Act).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RC.RP-03 — The integrity of backups and other restoration assets is verified before using them for restoration — **CORE** — CSF title shares 3 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.OC-04 — Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated — **CORE** — CSF title shares 3 action tokens with objective
  - GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.RM-04 — Strategic direction that describes appropriate risk response options is established and communicated — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Provider of high-risk AI system draws up and keeps up-to-date the Annex IV technical d... | AI_Act | sufficient | - | low |

### D-09.4 · AI_Act · req 9.4.5
- **Title**: "Provider of high-risk AI system draws up and keeps up-to-date the Annex IV technical documentation before placing on market or putting into service, the 13-element QMS documentation, and the Art. 19(1) provider logs under their control"
- **Description**: The product shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service (per AI Act Art. 11(1)), keep the logs automatically recorded by the high-risk AI system to the extent under the provider's control (per Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control`), and document the quality management system in written policies, procedures, and instructions in a systematic and orderly manner covering at least the 13 enumerated aspects (a)-(m) of Art. 17(1) closed list, with AI Act Recital 78 explicit GDPR preservation.
- **Fit criterion (prose)**: Technical documentation is drawn up and kept up-to-date per Art. 11(1) `Providers of high-risk AI systems shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service` (SR-AIACT-009) verified by ID.AM-08 lifecycle-management dimension (the provider demonstrates ex post that the Annex IV technical documentation + Art. 19(1) logs + Art. 17(1) QMS documentation are managed throughout the AI-system life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Art. 17(1)(d) `data quality` + Art. 17(1)(g) `risk-management-system documentation cross-reference to Art. 9` are consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + GV.PO-01 cybersecurity-policy substrate (the Art. 17(1) QMS `systematic and orderly manner in the form of written policies, procedures and instructions` is an organisational policy under the QMS — cross to 9.1 AI Act sub-SO); the Annex IV technical documentation is drawn up before placing on the market or putting into service per Art. 11(1); the Art. 19(1) `Providers of high-risk AI systems shall keep the logs referred to in Article 12(1) … to the extent that such logs are under their control` (SR-AIACT-008) covers the automatic recording of events over the high-risk AI system's life cycle per Art. 12(1) + traceability per Art. 12(2); the Art. 17(1) QMS documentation covers the 13 enumerated aspects (a) compliance strategy; (b) design, development, and verification techniques; (c) design, design control, design verification of the high-risk AI system; (d) post-market monitoring (cross to 10.1 AI Act sub-SO); (e) data quality; (f) ... (m) — full content codification (vs GDPR's entity-discretionary content under Art. 24(2) or NIS 2's entity-discretionary content under Recital 56 proportionality); the recipient is the **MSA (market surveillance authority) + AI Office + provider** on the Art. 11 Annex IV technical documentation + Art. 12(1)/(2) automatic recording + Art. 17(1) 13-element QMS + Art. 19(1) logs; verified by MSA + AI Office audit pack (Annex IV technical documentation extract, QMS documentation extract, Art. 19(1) log retention evidence) + automated Annex IV field-completeness test + automated 13-element QMS field-completeness test. **IMPORTANT — AI Act Recital 78 GDPR preservation**: AI Act Recital 78 explicitly preserves GDPR for personal-data processing — `protection of natural persons in relation to the processing of personal data … is governed by Regulation (EU) 2016/679`; providers that are also controllers maintain **parallel artefacts** (GDPR RoPA + AI Act Annex IV + AI Act Art. 17(1) QMS) on distinct artefacts that are not substitutable. **IMPORTANT — CRA Art. 13(4) sentence 2 risk-assessment consolidation does NOT extend to documentation**: the CRA Art. 13(4) sentence 2 unification rule at 9.2 covers the *risk-assessment object*; there is no equivalent documentation-level consolidation rule at 9.4; the two regimes maintain **parallel artefacts** (CRA Annex VII + AI Act Annex IV + AI Act Art. 17(1) QMS).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 8 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The manufacturer **draws up before placing a product with digital elements on the marke... | CRA | sufficient | - | low |

### D-09.4 · CRA · subso SO-D-09.4.CRA
- **Objective**: The manufacturer **draws up before placing a product with digital elements on the market the technical documentation referred to in Art. 31** (Art. 13(12) sentence 1 CRA), carries out the conformity assessment procedure referred to in Art. 32, draws up the EU declaration of conformity under Art. 28, and affixes the CE marking under Art. 30 (Art. 13(12) sentence 2); the manufacturer keeps the technical documentation and the EU declaration of conformity at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (Art. 13(13) CRA).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.AM-02 — Inventories of software, services, and systems managed by the organization are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Manufacturer draws up before placing on market the technical documentation per Annex V... | CRA | sufficient | - | low |

### D-09.4 · CRA · req 9.4.3
- **Title**: "Manufacturer draws up before placing on market the technical documentation per Annex VII §1-§8 8-item content list, keeps it at MSA disposal for at least 10 years or the support period (whichever longer), and provides the EU declaration + CE marking"
- **Description**: The product shall draw up before placing a product with digital elements on the market the technical documentation referred to in Art. 31 (per CRA Art. 13(12) sentence 1), carry out the conformity assessment procedure referred to in Art. 32, draw up the EU declaration of conformity under Art. 28, and affix the CE marking under Art. 30 (per Art. 13(12) sentence 2), with the technical documentation and the EU declaration of conformity kept at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer (per Art. 13(13)), and the Annex VII §1-§8 8-item content list (general description; design, development, production, and vulnerability-handling processes; cybersecurity risk assessment; support-period determination; harmonised standards applied; reports of tests carried out; copy of the EU declaration of conformity; SBOM on MSA reasoned request) maintained throughout the support period.
- **Fit criterion (prose)**: Technical documentation is drawn up before placing on market per Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` (SR-CRA-085) verified by ID.AM-08 lifecycle-management dimension (manufacturer demonstrates ex post that the Annex VII §1-§8 8-item content list is managed throughout the product life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Annex VII §1 `general description` + §3 `cybersecurity risk assessment` dimensions are consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + ID.RA-05 risk-priority-response dimension (the Annex VII §3 `cybersecurity risk assessment` documentation is mapped to the priority risk responses per CRDA DomainAnalysis §9.4 line 113); the Annex VII §1-§8 8-item content list is fully content-codified (§1 general description; §2 design, development, production, and vulnerability-handling processes; §3 cybersecurity risk assessment; §4 support-period determination; §5 harmonised standards applied; §6 reports of tests carried out; §7 copy of the EU declaration of conformity; §8 SBOM on MSA reasoned request — per SR-CRA-087 + SR-CRA-088); the technical documentation is drawn up before placing on the market per Art. 31(2); the manufacturer carries out the conformity assessment procedure referred to in Art. 32 (selection of internal production control per Annex VI or third-party assessment per Annex VII depending on criticality class); the manufacturer draws up the EU declaration of conformity per Art. 28 + CE marking per Art. 30 (per Art. 13(12) sentence 2); the technical documentation + EU declaration of conformity are kept at MSA disposal for at least 10 years or the support period, whichever longer, per Art. 13(13) `10 years … or for the support period, whichever is longer` (SR-CRA-085); the manufacturer is identified per Art. 13(15) (single point of contact per Art. 13(17) + Art. 13(16) for product-identification where applicable); the support-period end-date is displayed per Art. 13(19) (cross to D-06.3 Contractual Security Obligations); the EU declaration is provided per Art. 13(20) + Annex II §6; immediate corrective measures are taken per Art. 13(21); MSA cooperation per Art. 13(22); cessation-of-operations notification per Art. 13(23); Commission implementing/delegated acts per Art. 13(24)/(25) + Art. 14(9)/(10) + Art. 7(3)/(4) + Art. 30(6). The recipient is the **MSA (market surveillance authority)** on the Annex VII §1-§8 8-item content list + Art. 13(12)/(13)/(15)-(25) + Art. 28 EU declaration + Art. 30 CE marking. Verified by MSA technical-file audit pack (Annex VII §1-§8 content list extract, EU declaration copy, CE marking documentation, 10-year or support-period retention evidence, SBOM on MSA reasoned request) + automated Annex VII §1-§8 field-completeness test. **IMPORTANT — CRA full content codification**: CRA Annex VII §1-§8 is fully content-codified — the 8-item content list is explicit (vs GDPR's Art. 30(1)(a)-(g) RoPA content list with entity-discretionary fields such as `where possible`). **IMPORTANT — CRA Annex VII does NOT cross-substitute for GDPR RoPA**: substantively scope-disjoint per CRDA `N (typically)` (different record types, different triggers, different audit purposes). **IMPORTANT — CRA + AI Act for AI-enabled products do NOT have OJ-level consolidation for documentation**: unlike the CRA Art. 13(4) sentence 2 risk-assessment consolidation rule at 9.2 (which substitutes AI Act Art. 9 risk-management for CRA risk-assessment), no equivalent documentation-level consolidation rule exists at 9.4.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 6 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities **develop and document an information security policy defining rules... | DORA | sufficient | - | low |

### D-09.4 · DORA · subso SO-D-09.4.DORA
- **Objective**: Financial entities **develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable** (Art. 9(4)(a) DORA); this is entity-level IS-policy documentation serving NCA audit purposes and is a **different record type from the GDPR RoPA**.
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Financial entity develops and documents an information security policy defining rules ... | DORA | sufficient | - | low |

### D-09.4 · DORA · req 9.4.4
- **Title**: "Financial entity develops and documents an information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of customers where applicable (Art. 9(4)(a) DORA)"
- **Description**: The product shall develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets, and ICT assets, including those of their customers, where applicable (per DORA Art. 9(4)(a)), under the management-body define/approve/oversee/be-responsible architecture per Art. 5(2) four-verb coordination, the three-lines-of-defence model per Art. 6(4), and the proportionality factors per Art. 4 (size, nature, scale, and complexity of the financial entity's activities); this is entity-level IS-policy documentation serving NCA audit purposes and is a **different record type from the GDPR RoPA**.
- **Fit criterion (prose)**: An information security policy is developed and documented per Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable` (SR-DORA-031) verified by ID.AM-08 lifecycle-management dimension (the financial entity demonstrates ex post that the IS-policy is managed throughout the life cycle of data, information assets, and ICT assets per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the IS-policy CIA+A 4-way + customer-where-applicable dimension is consistent with the entity's risk strategy per CRDA DomainAnalysis §9.4 line 113) + GV.PO-01 cybersecurity-policy substrate (the IS-policy is an organisational policy under the management-body define/approve/oversee/be-responsible architecture per Art. 5(2) — cross to 9.1 DORA sub-SO); the management body discharges the Art. 5(2) four-verb coordination `define, approve, oversee and be responsible for` (per SR-DORA-026); the three-lines-of-defence model is operationalised per Art. 6(4) (operational-management as first line, risk-management and compliance as second line, internal-audit as third line); the proportionality factors per Art. 4 `in relation to the size, nature, scale and complexity of the financial entity's activities` calibrate the IS-policy depth; no OJ-quantified retention period — entity-discretionary under Member State transposition; the recipient is the **competent authority (NCA — national financial supervisory authority) + management body** on the Art. 9(4)(a) IS-policy documentation serving NCA audit purposes. Verified by NCA audit pack (IS-policy extract, Art. 5(2) management-body approval minute, three-lines-of-defence documentation, Art. 4 proportionality calibration evidence) + automated CIA+A field-completeness test (availability, authenticity, integrity, confidentiality of data + information assets + ICT assets, customer-where-applicable). **IMPORTANT — DORA-absence flag**: per CRDA-deep §9.4 line 29, DORA is fully absent for RoPA-equivalent — DORA does not impose a RoPA obligation (no analogue to GDPR Art. 30). The DORA Art. 9(4)(a) IS-policy documentation is a **different record type** (entity-level IS-policy documentation) serving a **different audit purpose** (NCA audit on IS policy) than the GDPR RoPA (DPA audit on processing activities). For DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation; the DORA Art. 9(4)(a) IS-policy documentation is a separate artefact. **DORA BC/DR logging obligations (Art. 12) are operational continuity artefacts, not RoPA-equivalents** — covered separately under D-10 Monitoring & Audit. Phase 1 entities with GDPR + DORA applicability must maintain both GDPR RoPA + DORA Art. 9(4)(a) IS-policy documentation on distinct artefacts that are not substitutable (no cross-substitution OJ-permitted).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 7 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Each controller and processor **maintains a record of processing activities under its r... | GDPR | sufficient | - | low |

### D-09.4 · GDPR · subso SO-D-09.4.GDPR
- **Objective**: Each controller and processor **maintains a record of processing activities under its responsibility** (Art. 30(1) GDPR), in writing or electronic form (Art. 30(3) GDPR), containing the Art. 30(1) 7-item content list; the processor maintains a parallel record under Art. 30(2) GDPR; records are made available to the supervisory authority on request (Art. 30(4) GDPR), subject to the Art. 30(5) 250-employee exception.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 3 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 5 action tokens with objective
  - DE.AE-03 — Information is correlated from multiple sources — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - RS.AN-07 — Incident data and metadata are collected, and their integrity and provenance are preserved — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-02 — Identities are proofed and bound to credentials based on the context of interactions — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller and processor maintain a record of processing activities (RoPA) under Art. ... | GDPR | sufficient | - | low |

### D-09.4 · GDPR · req 9.4.1
- **Title**: "Controller and processor maintain a record of processing activities (RoPA) under Art. 30(1)/(2)/(3)/(4)/(5) GDPR with the 7-item content list, on-DPA-request, subject to the 250-employee exception"
- **Description**: The product shall maintain a record of processing activities under the controller's or processor's responsibility (per GDPR Art. 30(1) + Art. 30(2) processor RoPA), in writing or electronic form (per Art. 30(3) `in writing, including in electronic form`), with the Art. 30(1) (a)-(g) 7-item content list (name/contact details of controller; purposes of processing; categories of data subjects and personal data; categories of recipients; transfers to third country; envisaged time limits for erasure; general description of technical and organisational security measures), made available to the supervisory authority on request (per Art. 30(4)), subject to the Art. 30(5) 250-employee exception, and operationalising the Art. 5(2) accountability burden (per Art. 12-14 transparency to data subjects).
- **Fit criterion (prose)**: A RoPA is maintained per Art. 30(1) `record of processing activities under its responsibility` with the 7-item content list (SR-GDPR-048) verified by ID.AM-08 lifecycle-management dimension (controller demonstrates ex post that systems, hardware, software, services, and data are managed throughout their life cycle — the RoPA records the processing activities supporting that life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the Art. 30(1)(g) `general description of the technical and organisational security measures` is consistent with the entity's risk strategy) + GV.PO-02 process-and-procedure demonstrable-compliance (the Art. 30(3) `in writing, including in electronic form` form-factor is documented and demonstrable to the DPA on request); the processor maintains a parallel record per Art. 30(2) `record of processing activities carried out on behalf of the controller` with the (a)-(e) content (name/contact details of processor + controller; categories of processing; transfers to third country; TOMs; audit enablement to the extent necessary); records are made available to the supervisory authority on request per Art. 30(4) (SR-GDPR-050); the Art. 30(5) 250-employee exception is read at the R1 literal — `an undertaking or organisation employing fewer than 250 persons` is exempt from the RoPA obligation UNLESS processing is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, OR the processing includes special categories of data or criminal-conviction data; the RoPA operationalises Art. 5(2) accountability burden with Art. 12-14 transparency to data subjects cross-referenced (SR-GDPR-065-068); the recipient is the **DPA (supervisory authority)** on the Art. 30(1) RoPA content items + Art. 30(4) on-DPA-request + Art. 30(5) 250-employee exception + Art. 12-14 transparency; verified by DPA audit pack (RoPA extract, on-DPA-request retrieval procedure, accountability burden evidence, Art. 5(2) continuous compliance evidence) + automated RoPA field-completeness test (all 7 Art. 30(1)(a)-(g) fields populated for each processing activity) + Art. 30(3) form-factor inspection (writing or electronic form). **IMPORTANT — DORA-absence flag**: per CRDA-deep §9.4 line 29, DORA is fully absent for RoPA-equivalent — for DORA financial entities, the GDPR RoPA remains the dedicated authority for processing-activities documentation. The GDPR RoPA does NOT substitute for the CRA Annex VII 8-item technical documentation (substantively scope-disjoint per CRDA `N (typically)`), the NIS 2 Art. 24 certification-driven records (substantively scope-disjoint per CRDA `N (typically)`), the DORA Art. 9(4)(a) IS-policy documentation (different record type, different audit purpose), or the AI Act Annex IV + Art. 17(1) QMS documentation (parallel artefacts; no OJ-level consolidation rule for documentation at 9.4).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 11 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Member States shall **encourage the use of European or internationally accepted standar... | NIS2 | sufficient | - | high |

### D-09.4 · NIS2 · subso SO-D-09.4.NIS2
- **Objective**: Member States shall **encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems** (Art. 24(1) sentence 1 NIS 2) and of qualified trust services (Art. 24(1) sentence 2); the Commission may adopt delegated acts specifying entities that must use certified ICT products, services and processes (Art. 24(2) NIS 2), and ENISA may be requested to prepare a candidate European cybersecurity certification scheme (Art. 24(3) NIS 2).
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/NIS2_Art_24.md` (Art. 24) — paraphrased action
- **Anchors listed**:
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| "Member States encourage use of European or internationally accepted standards and spec... | NIS2 | sufficient | - | high |

### D-09.4 · NIS2 · req 9.4.2
- **Title**: "Member States encourage use of European or internationally accepted standards and specifications for the security of network and information systems, with Commission delegated acts under Art. 24(2) and ENISA candidate scheme request under Art. 24(3)"
- **Description**: The product shall record the use of certified ICT products, ICT services, and ICT processes under Member-State-driven standards and specifications relevant to the security of network and information systems (per NIS 2 Art. 24(1) sentence 1) and of qualified trust services (per Art. 24(1) sentence 2), with the Commission empowered to adopt delegated acts specifying entities required to use certified ICT products/services/processes (per Art. 24(2)) and ENISA empowered to be requested to prepare a candidate European cybersecurity certification scheme (per Art. 24(3)).
- **Fit criterion (prose)**: Certification-driven records are maintained per Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` (SR-NIS2-043) verified by ID.AM-08 lifecycle-management dimension (the NSIE demonstrates ex post that certified ICT products/services/processes are inventoried and managed throughout their life cycle per CRDA DomainAnalysis §9.4 line 113 cross-validation) + ID.AM-08 risk-strategy-consistent data management (the certification-driven records are consistent with the entity's risk strategy); Art. 24(1) sentence 2 `Member States shall also encourage, without prejudice to paragraph 1, the use of any qualified trust service` extends the certification-driven records to qualified trust services; Art. 24(2) `The Commission may adopt delegated acts … to specify which categories of essential and important entities shall be required to use certain certified ICT products, ICT services and ICT processes` — the certification-driven records are conditional on the Commission adopting such delegated acts; Art. 24(3) `ENISA may be requested to prepare a candidate European cybersecurity certification scheme` — the certification-driven records may feed ENISA candidate scheme preparation. The content is **not codified at OJ level** — entity-discretionary under Member State transposition. The recipient is the **management body + competent authority (national NIS 2 supervisory authority)** on the Art. 24(1)/(2)/(3) certification-driven records per Member State. **IMPORTANT — NIS 2 partial coverage at 9.4**: the NIS 2 Art. 24(1)/(2)/(3) certification-driven recordkeeping is **partial coverage** — Member-State-driven use of certified ICT products/services/processes, not a RoPA-equivalent; substantively scope-disjoint from GDPR per CRDA `N (typically)` (different record types, different triggers, different audit purposes). Phase 1 entities with NIS 2 + GDPR applicability must maintain both GDPR Art. 30 RoPA + NIS 2 Art. 24 certification-driven records on distinct artefacts that are not substitutable. For NSIEs that are CRA-conformant product procurers, the CRA Art. 27(8)/(9) CSA-certification presumption-of-conformity machinery is the upstream gate for NIS 2 procurements — Phase 1 must verify that procured CRA products hold CSA certification at the assurance level required by the Commission's delegated act under Art. 24(2). The **NIS 2 → CRA certification link** is the only cross-regulation link at 9.4 involving NIS 2.
- **Regulatory basis**: `domains/D-09_Governance-Documentation/D-09.4/articles/NIS2_Art_24.md` (Art. 24) — paraphrased action
- **Anchors listed**:
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 9 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

## D-10.1 Continuous Security Monitoring

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Providers of high-risk AI systems **establish and document a post-market monitoring sys... | AI_Act | excessive | - | low |

### D-10.1 · AI_Act · subso SO-D-10.1.AI_Act
- **Objective**: Providers of high-risk AI systems **establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system** (Art. 72(1) AI Act), with the system **actively and systematically collecting, documenting and analysing relevant data** (Art. 72(2) AI Act); market-surveillance cooperation under Regulation (EU) 2019/1020 applies (Art. 74(1) AI Act).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.MA-03 — Incidents are categorized and prioritized — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title shares 3 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: DE.CM-09, ID.IM-04, GV.OV-03 — literal duplicate(s) of DE.CM-09, ID.IM-04, GV.OV-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Provider of high-risk AI system establishes and documents a post-market monitoring sys... | AI_Act | sufficient | - | low |

### D-10.1 · AI_Act · req 10.1.5
- **Title**: "Provider of high-risk AI system establishes and documents a post-market monitoring system proportionate to the nature of the AI technologies and the risks, actively and systematically collecting, documenting and analysing relevant data across the AI lifecycle"
- **Description**: The product shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system (per AI Act Art. 72(1) `Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system`), with the system actively and systematically collecting, documenting and analysing relevant data (per Art. 72(2) `The post-market monitoring system shall actively and systematically collect, document and analyse relevant data`), and market-surveillance cooperation under Regulation (EU) 2019/1020 applying (per Art. 74(1)).
- **Fit criterion (prose)**: A post-market monitoring system is established and documented per Art. 72(1) + Art. 72(2) + Art. 74(1) (SR-AIACT-021 + SR-AIACT-022) verified by DE.CM-09 primary (Computing hardware and software, runtime environments, and their data are monitored — anchors the AI Act Art. 72(2) `actively and systematically collect, document and analyse relevant data` mapped to NIST CSF 2.0 DE.CM-09) + ID.IM-04 (Adequate resource capacity to ensure availability is maintained — anchors the post-market monitoring system per DomainAnalysis cross-validation) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 72 analysis-to-risk-management feedback loop); the post-market monitoring system is documented in a manner that is `proportionate to the nature of the AI technologies and the risks` (qualitative proportionality — per SR-AIACT-021 ambiguity_notes, the OJ does not quantify the proportionality; the chosen reading is: a documented proportionality assessment that calibrates the depth of monitoring to the AI technology class and risk category); the Art. 72(2) `actively and systematically collect, document and analyse` 3-way verb AND is operational across the AI-system lifecycle (collection channels + documentation layer + analysis layer + feedback loop); the analysis-to-risk-management feedback loop feeds back into the provider's risk-management-system documentation (Art. 9 — cross to 9.1 AI Act sub-SO) and the AI-system quality management system (Art. 17 — cross to 9.1 AI Act sub-SO); the Art. 72(3) post-market monitoring plan is documented and operational; the Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020 provides the MSA + AI Office recipient channel; the recipient is the **MSA (market surveillance authority) + AI Office + provider** on the Art. 72(1)-(3) post-market monitoring + Art. 74(1) market-surveillance cooperation; verified by MSA + AI Office audit pack (post-market monitoring system documentation, Art. 72 proportionality assessment, Art. 72(2) 3-way verb AND evidence, Art. 72(3) post-market monitoring plan, analysis-to-risk-management feedback loop evidence, Art. 74(1) market-surveillance cooperation evidence) + automated Art. 72(2) 3-way verb AND test (collection channels operational + documentation layer operational + analysis layer operational) + automated analysis-to-risk-management feedback loop test (post-market monitoring analysis feeds back into Art. 9 risk-management-system documentation + Art. 17 QMS). **IMPORTANT — AI Act post-market monitoring feedback loop** (Art. 72(2) `actively and systematically collect, document and analyse` → analysis-to-risk-management loop feeding Art. 9 + Art. 17) is AI-Act-specific and is preserved in this sub-SO. The AI Act Art. 72 monitoring is provider-side and is NOT subject to user opt-out (unlike CRA Annex I Part I (2)(l) opt-out); the CRA opt-out tension does NOT extend to the AI Act pair.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 5 action tokens with objective
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| A product with digital elements **provides security-related information by recording an... | CRA | sufficient | - | low |

### D-10.1 · CRA · subso SO-D-10.1.CRA
- **Objective**: A product with digital elements **provides security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provides an opt-out mechanism for the user** (Annex I Part I (2)(l) CRA); the manufacturer **facilitates the sharing of information about potential vulnerabilities** through a single contact address (Annex I Part II (6) CRA).
- **Anchors listed**:
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no candidate_articles listed; cannot cross-check article mappings)

| "Product with digital elements records and monitors relevant internal activity (access ... | CRA | sufficient | - | low |

### D-10.1 · CRA · req 10.1.3
- **Title**: "Product with digital elements records and monitors relevant internal activity (access to or modification of data, services or functions) with a user opt-out mechanism, and enables vulnerability sharing through a single contact address"
- **Description**: The product shall provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user (per CRA Annex I Part I (2)(l) `provide security-related information by recording and monitoring relevant internal activity, including access to or modification of data, services or functions, and provide an opt-out mechanism for the user`); the manufacturer shall facilitate the sharing of information about potential vulnerabilities of the product with digital elements through a single contact address (per Annex I Part II (6) `facilitate the sharing of information about potential vulnerabilities of the product with digital elements`).
- **Fit criterion (prose)**: Product-level on-device internal-activity monitoring is operational per Annex I Part I (2)(l) + Annex I Part II (6) (SR-CRA-100 + SR-CRA-101) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the CRA Annex I Part I (2)(l) on-device internal-activity monitoring mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the product-level on-device monitoring per DomainAnalysis cross-validation) + ID.IM-04 (Adequate resource capacity — anchors the manufacturer-side observability dimension); the on-device monitoring records and monitors access to or modification of data, services, or functions; the user opt-out mechanism is operational with a clear opt-out interface (UI surface) + opt-out state preservation across product restarts; the vulnerability-reporting contact address is operational per Annex I Part II (6) — single contact address (email or web form) for the sharing of information about potential vulnerabilities of the product with digital elements, integrated with the manufacturer's CVD policy per Annex I Part II §5 (cross to 2.3 Vulnerability Management + 9.1 CRA sub-SO); the recipient is the **MSA (market surveillance authority) + users** on the Annex I Part I (2)(l) on-device monitoring with user opt-out + Annex I Part II (6) vulnerability-reporting contact address; verified by MSA audit pack (on-device monitoring evidence, user opt-out mechanism evidence, vulnerability-reporting contact address operational evidence) + automated on-device monitoring coverage test (access to data + access to services + access to functions + modification of data + modification of services + modification of functions are all monitored) + automated user opt-out mechanism test (opt-out interface accessible + opt-out state preserved across product restarts) + automated vulnerability-reporting contact address test (single contact address operational and responsive). **IMPORTANT — CRDA-flagged GENUINE TENSION (primary flag, GDPR↔CRA)**: CRA Annex I Part I (2)(l) user opt-out vs. mandatory-monitoring regimes (GDPR Art. 32(2), NIS 2 Art. 21(2)(b), DORA Art. 8(1)) — the OJ does not resolve this conflict. The tension propagates to 3 of 10 pairs (GDPR↔CRA primary, NIS2↔CRA propagated, CRA↔DORA propagated). Phase 1 entities with this conflict must (a) maintain the mandatory monitoring under GDPR / NIS 2 / DORA on the entity layer regardless of the CRA opt-out at the product layer, and (b) escalate to Layer 2 OJ-level resolution for the cross-layer conflict. The two regimes can stack on the layered monitoring architecture (entity-layer mandatory + product-layer with opt-out), but the user's opt-out from CRA monitoring does not legally exempt the controller / NSIE / DORA entity from the respective mandatory-monitoring regime. **IMPORTANT — CRA opt-out mechanism is the origin of the 1 CRDA-flagged GENUINE TENSION**: CRA is the only regulator that explicitly permits user opt-out from monitoring (Annex I Part I (2)(l)); the opt-out mechanism is structurally significant and propagates against any mandatory-monitoring regime.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities **continuously monitor and control the security and functioning of I... | DORA | sufficient | - | low |

### D-10.1 · DORA · subso SO-D-10.1.DORA
- **Objective**: Financial entities **continuously monitor and control the security and functioning of ICT systems and tools** and **minimise the impact of ICT risk on ICT systems** (Art. 8(1) DORA per SR-DORA-030; OJ-literal locus Art. 9(1)); **anomalous activities are promptly detected** through multi-layered controls, alert thresholds, incident response triggers, and identification of single points of failure (Art. 10(1)+(2) DORA), with sources of ICT risk **identified on a continuous basis** and risk scenarios reviewed on a regular basis, at least yearly (Art. 7(2) DORA).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 3 action tokens with objective
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('anomal') in objective maps to DE.AE-02
  - RS.MA-01 — The incident response plan is executed in coordination with relevant third parties once an incident is declared — **CORE** — CSF title literally matches action keyword ('incident')
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Financial entity continuously monitors and controls the security and functioning of IC... | DORA | sufficient | - | low |

### D-10.1 · DORA · req 10.1.4
- **Title**: "Financial entity continuously monitors and controls the security and functioning of ICT systems and tools, with prompt anomalous-activity detection through multi-layered controls and continuous ICT risk identification"
- **Description**: The product shall continuously monitor and control the security and functioning of ICT systems and tools and minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures (per DORA Art. 8(1) per SR-DORA-030; OJ-literal locus Art. 9(1) `continuously monitor and control the security and functioning of ICT systems and tools`), with anomalous activities promptly detected through multi-layered controls, alert thresholds, incident response triggers, and identification of single points of failure (per Art. 10(1) `promptly detect anomalous activities` + Art. 10(2) multiple layers + alert thresholds + auto-alert to relevant staff), and sources of ICT risk identified on a continuous basis and risk scenarios reviewed on a regular basis, at least yearly (per Art. 7(2)).
- **Fit criterion (prose)**: Continuous monitoring of ICT systems and tools is operational per Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) `Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the deployment of appropriate ICT security tools, policies and procedures` (SR-DORA-030) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the DORA Art. 8(1) `continuously monitor and control` mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the financial-entity ICT-systems monitoring per DomainAnalysis cross-validation) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 8(1) `tools, policies and procedures` 3-way AND) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 10(1) prompt anomalous-activity detection) + ID.RA-01 (Asset vulnerabilities are identified, validated, and recorded — anchors the Art. 7(2) continuous ICT risk identification + yearly review) + ID.RA-03 (Threats to assets are identified and recorded — anchors the Art. 7(2) `cyber threats and ICT vulnerabilities`); the Art. 10(1) + Art. 10(2) prompt anomalous-activity detection is operational through multi-layered controls (network layer + system layer + application layer + data layer), alert thresholds, identification of single points of failure, and auto-alert to relevant staff; the Art. 7(2) continuous ICT risk identification is operational on a continuous basis with risk scenarios reviewed on a regular basis, at least yearly; the recipient is the **NCA (national competent authority) + management body** on the Art. 8(1) continuous monitoring + Art. 10(1)+(2) multi-layered detection + Art. 7(2) continuous ICT risk identification; verified by NCA + EBA Guidelines supervisory baseline audit pack (continuous monitoring evidence, prompt anomalous-activity detection evidence with multi-layered controls, alert thresholds, identification of single points of failure, auto-alert evidence, Art. 7(2) continuous ICT risk identification evidence with yearly review documentation). **DORA-led stack for financial entities**: DORA Art. 8(1) continuous monitoring is broader (security AND functioning) than GDPR Art. 32(2) 5-risk-type detection. For DORA financial entities that are also controllers, the DORA Art. 8(1) / Art. 9(1) continuous monitoring discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack. **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension**: both regulations impose continuous-monitoring obligations (NIS 2 Art. 21(2)(b) detection capability vs. DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) `continuously monitor and control`); for DORA financial entities that are also NSIEs, the DORA Art. 9(1) continuous monitoring discharges both obligations — DORA-dominant; for non-financial NSIEs, NIS 2 is the authority. The proportionality factors per Art. 4 `in relation to the size, nature, scale and complexity of the financial entity's activities` calibrate the depth of the continuous monitoring + multi-layered detection + continuous ICT risk identification. **CRDA-flagged GENUINE TENSION with CRA (propagated)**: CRA Annex I Part I (2)(l) user opt-out vs. DORA Art. 8(1) mandatory continuous monitoring — Layer 2 OJ-level resolution required.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md` (Art. 15) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title literally matches action keyword ('vulnerabilities')
  - ID.RA-03 — Internal and external threats to the organization are identified and recorded — **CORE** — CSF title shares 6 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The controller and processor implement appropriate technical and organisational measure... | GDPR | excessive | - | low |

### D-10.1 · GDPR · subso SO-D-10.1.GDPR
- **Objective**: The controller and processor implement appropriate technical and organisational measures to ensure the **ongoing confidentiality, integrity, availability and resilience of processing systems and services** (Art. 32(1)(b) GDPR) and **regularly test, assess and evaluate their effectiveness** (Art. 32(1)(d) GDPR); personal-data processing systems and services are monitored for the five Art. 32(2) risk types, with a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - RS.CO-03 — Information is shared with designated internal and external stakeholders — **CORE** — CSF title shares 2 action tokens with objective
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - PR.DS-01 — The confidentiality, integrity, and availability of data-at-rest are protected — **CORE** — CSF title shares 6 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title literally matches action keyword ('resilien')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **UTILITY** — CSF title shares 1 token ('are') with objective; reinforces but is not the direct action
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: DE.CM-01 — literal duplicate(s) of DE.CM-01
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller and processor monitor personal-data processing systems for the 5 Art. 32(2)... | GDPR | sufficient | - | low |

### D-10.1 · GDPR · req 10.1.1
- **Title**: "Controller and processor monitor personal-data processing systems for the 5 Art. 32(2) risk types, with breach-`becoming-aware` clock anchoring the Art. 33(1) 72-hour notification"
- **Description**: The product shall implement appropriate technical and organisational measures to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services (per GDPR Art. 32(1)(b)) and regularly test, assess and evaluate their effectiveness (per Art. 32(1)(d) `a process for regularly testing, assessing and evaluating`), with personal-data processing systems and services monitored for the 5 Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data), and a clear definition of the moment of `becoming aware of` a breach to anchor the Art. 33(1) 72-hour notification clock `without undue delay and, where feasible, not later than 72 hours after having become aware of it`.
- **Fit criterion (prose)**: Entity-level monitoring of personal-data processing systems is operational per Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) (SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — the controller demonstrates ex post that the 5-risk-type monitoring is operational on personal-data processing systems per DomainAnalysis cross-validation) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the personal-data processing systems monitoring dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the breach-`becoming-aware` clock per Art. 33(1) `the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of it, notify the personal data breach to the supervisory authority`) + ID.IM-04 (Adequate resource capacity to ensure availability is maintained — anchors the Art. 32(1)(b) ongoing availability dimension); the 5 Art. 32(2) risk types are: (i) accidental or unlawful destruction, (ii) loss, (iii) alteration, (iv) unauthorised disclosure of, (v) access to personal data; the breach-`becoming-aware` clock is operationalised with a clear definition of the moment of `becoming aware of` (per EDPB Guidelines 9/2022 on personal data breach notification under Regulation 2016/679 §3.2 — the controller has a high degree of certainty that a security incident has occurred that has led to personal data being compromised) and an audit trail that documents the moment-of-becoming-aware timestamp + the Art. 33(1) 72-hour notification timestamp; the recipient is the **data subject + DPA (supervisory authority)** on the Art. 32(2) detection evidence + Art. 33(1) notification; verified by DPA audit pack (5-risk-type monitoring evidence, breach-`becoming-aware` clock evidence, Art. 33(1) notification log, Art. 5(2) accountability burden evidence) + automated 5-risk-type coverage test (each of the 5 risk types is covered by the monitoring evidence) + automated breach-`becoming-aware` clock test (Art. 33(1) 72-hour notification triggered within 72h of moment-of-becoming-aware). **For DORA financial entities**, the **DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) continuous monitoring is broader (security AND functioning) than GDPR Art. 32(2) 5-risk-type detection; the DORA-led stack discharges the financial entity's continuous-monitoring obligation and the GDPR detection capability becomes a sub-component within the DORA-led stack (DORA-led stack for financial entities — cross to 10.1.4).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Essential and important entities establish an **incident-handling capability** covering... | NIS2 | sufficient | - | low |

### D-10.1 · NIS2 · subso SO-D-10.1.NIS2
- **Objective**: Essential and important entities establish an **incident-handling capability** covering prevention, detection, analysis, containment, response, and recovery of incidents (Art. 21(2)(b) NIS 2); the detection dimension is the partial-coverage dimension of D-10.1, operating on an all-hazards basis and feeding the Art. 23(1) significant-incident notification chain.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — CSF title shares 1 token ('incidents') with objective; reinforces but is not the direct action
  - RS.MA-03 — Incidents are categorized and prioritized — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Essential and important entities establish an incident-handling capability with 6-acti... | NIS2 | sufficient | - | low |

### D-10.1 · NIS2 · req 10.1.2
- **Title**: "Essential and important entities establish an incident-handling capability with 6-action lifecycle (prevent, detect, analyse, contain, respond, recover) covering detection of all-hazards incidents"
- **Description**: The product shall establish an incident-handling capability covering prevention, detection, analysis, containment, response, and recovery of incidents (per NIS 2 Art. 21(2)(b) `incident handling`), including those with significant impact on the provision of services, with the detection dimension operating on an all-hazards basis and feeding the Art. 23(1) significant-incident notification chain; the Art. 21(2)(b) detection capability is the **partial-coverage dimension** of 10.1 — NIS 2 does not impose a dedicated continuous-monitoring mandate beyond the detection dimension of incident handling.
- **Fit criterion (prose)**: An incident-handling capability is established per Art. 21(2)(b) `incident handling` (SR-NIS2-009 + SR-NIS2-014) with the 6-action lifecycle (prevent, detect, analyse, contain, respond, recover — per SR-NIS2-008) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the NIS 2 Art. 21(2)(b) incident-handling detection capability mapped to NIST CSF 2.0 DE.CM-01) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the all-hazards network and information systems monitoring per DomainAnalysis cross-validation) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 23(1) significant-incident detection trigger) + ID.IM-04 (Adequate resource capacity — anchors the prevention+detection+response feedback loop); the detection dimension operates on an all-hazards basis (all sources of ICT risk + cyber threats + ICT vulnerabilities — Art. 21(1) chapeau `Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems … which those entities use for their activities or the provision of their services, and to prevent or minimise the impact of incidents on the recipients of their services`); the all-hazards detection capability feeds the Art. 23(1) significant-incident notification chain (cross to 4.3 Regulatory Notification) when an incident has a significant impact on the continuity of essential services; the recipient is the **management body + competent authority (CSIRT — Computer Security Incident Response Team or national competent authority)** on the Art. 21(2)(b) detection capability + incident-handling 6-action lifecycle; verified by CSIRT audit pack (incident-handling 6-action lifecycle evidence, Art. 21(2)(b) all-hazards detection capability, Art. 23(1) significant-incident notification chain). **IMPORTANT — NIS 2 partial coverage at 10.1**: NIS 2 does NOT impose a dedicated continuous-monitoring mandate beyond the detection dimension of incident handling (Art. 21(2)(b)); the 10.1 coverage on the NIS 2 side is partial via the SO-NIS2-005 incident-handling detection capability. For DORA financial entities under DORA's direct scope, the **DORA Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) continuous monitoring is the dominant authority** and discharges both DORA's dedicated monitoring obligation and NIS 2's Art. 21(2)(b) partial-coverage detection dimension for DORA financial entities that are also NSIEs — **NIS 2 ↔ DORA EQUAL on continuous-monitoring dimension, DORA-dominant for financial entities**; for non-financial NSIEs, NIS 2 Art. 21(2)(b) detection capability operates on the all-hazards basis without a dedicated continuous-monitoring mandate.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - ID.IM-04 — Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-10.2 Audit Logging & Traceability

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Providers of high-risk AI systems ensure the systems **technically allow for the automa... | AI_Act | sufficient | - | low |

### D-10.2 · AI_Act · subso SO-D-10.2.AI_Act
- **Objective**: Providers of high-risk AI systems ensure the systems **technically allow for the automatic recording of events (logs) over the lifetime of the system** (Art. 12(1) AI Act) with logging capabilities ensuring a level of traceability of the functioning **appropriate to the intended purpose** (Art. 12(2) AI Act); providers **keep the logs** automatically generated by the high-risk AI system, to the extent under their control, for a period **appropriate to the intended purpose and of at least six months** unless provided otherwise in the applicable Union or national law (Art. 19(1) AI Act).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title shares 3 action tokens with objective
  - DE.AE-03 — Information is correlated from multiple sources — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - RC.RP-03 — The integrity of backups and other restoration assets is verified before using them for restoration — **CORE** — CSF title shares 3 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "High-risk AI system technically allows automatic recording of events (logs) over the l... | AI_Act | sufficient | - | low |

### D-10.2 · AI_Act · req 10.2.4
- **Title**: "High-risk AI system technically allows automatic recording of events (logs) over the lifetime of the system with traceability appropriate to the intended purpose; provider keeps logs under their control for at least six months"
- **Description**: The product shall technically allow for the automatic recording of events (logs) over the lifetime of the system (per AI Act Art. 12(1) `High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system`), with logging capabilities ensuring a level of traceability of the functioning of the high-risk AI system that is appropriate to the intended purpose (per Art. 12(2) `Logging capabilities shall ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose` + 3-element list Art. 12(2)(a)–(c) covering traceability of the functioning of the system / monitoring its operation / facilitating post-market monitoring pursuant to Article 72); the provider shall keep the logs automatically generated by the high-risk AI system, to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, and of at least six months, unless provided otherwise in the applicable Union or national law (per Art. 19(1) — OJ-literal locus preserved; **T5-vs-text gap note: AIA-C11 cites Art. 12(4) which does not exist in the OJ; substance is in Art. 19(1); OJ-literal locus at Art. 19(1)**).
- **Fit criterion (prose)**: AI-system automatic event logging is operational per Art. 12(1) + Art. 12(2) + Art. 19(1) (SR-AIACT-007 + SR-AIACT-008 + SR-AIACT-009) verified by PR.PS-04 primary (Software installation, operation, and updates are performed consistent with the security policy — anchors the AI Act Art. 12(1) `technically allow for the automatic recording of events (logs) over the lifetime of the system` mapped to NIST CSF 2.0 PR.PS-04) + DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored — anchors the AI-system automatic event logging with traceability per DomainAnalysis cross-validation) + DE.AE-03 (Information is correlated from multiple sources — anchors the Art. 12(2)(a)–(c) 3-element list) + RC.RP-03 (Recovery actions are performed and verified — anchors the Art. 19(1) provider log retention `appropriate to the intended purpose` proportionality + ≥6-month floor); the Art. 12(1) automatic event logging is operational over the system lifetime with the `over the lifetime` VAG covering the AI-system lifecycle (development + placement on market + operation + post-market monitoring); the Art. 12(2) traceability is `appropriate to the intended purpose` (POLY — qualitative proportionality) with the 3-element list (a) traceability of the functioning of the system, (b) monitoring its operation, (c) facilitating post-market monitoring pursuant to Article 72; the Art. 19(1) provider log retention is operational with **≥6-month hard floor** + `appropriate to the intended purpose` variable proportionality + `under their control` POLY scope discipline + GDPR escape clause `unless provided otherwise in the applicable Union or national law`; **T5-vs-text gap note preserved**: AIA-C11 cites Art. 12(4) which does not exist in the OJ (Art. 12 has only paragraphs 1–3); the substance is in Art. 19(1); OJ-literal locus preserved at Art. 19(1); the recipient is the **provider + MSA (market surveillance authority)** on the Art. 12(1)+(2) automatic event logging + Art. 19(1) provider log retention + Art. 74(1) market-surveillance cooperation under Regulation (EU) 2019/1020; verified by MSA + AI Office audit pack (automatic event logging evidence + traceability appropriate to intended purpose evidence + 3-element list evidence + provider log retention ≥6-month evidence + `under their control` POLY scope evidence + Art. 74(1) market-surveillance cooperation evidence) + automated logging capability test (system automatically records events over the lifetime + logs cover functioning traceability + operation monitoring + post-market monitoring facilitation) + automated retention floor test (≥6-month retention operational for all in-scope logs) + automated `under their control` POLY test (logs are kept by the provider or under provider-controlled processors within the Art. 19(1) POLY scope).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - DE.AE-03 — Information is correlated from multiple sources — **CORE** — CSF title shares 5 action tokens with objective
  - DE.CM-09 — Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
  - RC.RP-03 — The integrity of backups and other restoration assets is verified before using them for restoration — **CORE** — Action keyword ('recover') in objective maps to RC.RP-03
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmo... | CRA | excessive | - | low |

### D-10.2 · CRA · subso SO-D-10.2.CRA
- **Objective**: The manufacturer **maintains the technical documentation** (Annex VII §5-§8 CRA — harmonised standards applied, test reports, copy of the EU declaration of conformity, SBOM on MSA reasoned request), **preserves the cybersecurity risk-assessment documentation** (Annex VII §3 + Art. 13(4) sentence 1) during the support period (10 years or support period, whichever longer) with updates as appropriate, and ensures **test reports demonstrating verification of conformity with Annex I Part I and Part II** are part of the technical documentation and available on reasoned request from market surveillance authorities (Annex VII §6 + Annex I Part II (3) + Art. 13(22) CRA).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 3 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-02 — Software is maintained, replaced, and removed commensurate with risk — **CORE** — Action keyword ('update') in objective maps to PR.PS-02
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 2 action tokens with objective
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.RA-04, GV.PO-02, PR.DS-11 — literal duplicate(s) of ID.RA-04, GV.PO-02, PR.DS-11
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Manufacturer maintains technical documentation + risk-assessment documentation + test ... | CRA | sufficient | - | low |

### D-10.2 · CRA · req 10.2.2
- **Title**: "Manufacturer maintains technical documentation + risk-assessment documentation + test reports + SBOM on MSA reasoned request during the support period with effective/regular tests of the product"
- **Description**: The product shall maintain technical documentation — including a general description of the product, design and development information, harmonised standards applied, test reports, a copy of the EU declaration of conformity, and the software bill of materials (SBOM) on reasoned request from a market surveillance authority (per CRA Annex VII §5–§8) — together with the cybersecurity risk-assessment documentation preserved during the support period (10 years or support period, whichever longer) with updates as appropriate (per Annex VII §3 + Art. 13(4) sentence 1) and the manufacturer's policies, processes, and procedures (per Art. 13(8) — cross to 9.1), and shall carry out effective and regular tests and reviews of the product (per Annex I Part II (3)) with the test reports part of the technical documentation and available on reasoned request from market surveillance authorities (per Annex VII §6 + Art. 13(22)).
- **Fit criterion (prose)**: Product-level documentation traceability is operational per Annex VII §5–§8 + Annex VII §3 + Annex I Part II (3) + Art. 13(4) sentence 1 + Art. 13(22) (SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the CRA Annex VII §5–§8 technical documentation integrity mapped to NIST CSF 2.0 PR.DS-11) + ID.AM-08 (Data are securely deleted or destroyed — anchors the support-period retention + updates-as-appropriate per DomainAnalysis cross-validation) + GV.PO-02 (Information security policy is established, communicated, and maintained — anchors the Art. 13(8) manufacturer policies/processes/procedures + Annex VII §2(b) CVD policy) + ID.RA-04 (Potential impacts and likelihoods of threats are identified — anchors the Annex VII §3 risk-assessment documentation + Art. 13(2) cybersecurity risk assessment per Art. 13(4) sentence 1); the technical documentation content covers Annex VII §5 (general description of the product) + §6 (design and development information: harmonised standards applied + test reports) + §7 (copy of the EU declaration of conformity) + §8 (information on the software bill of materials — SBOM on MSA reasoned request); the risk-assessment documentation (Annex VII §3) is preserved during the support period (10 years or support period, whichever longer) with updates as appropriate per Art. 13(4) sentence 1; the effective and regular tests (Annex I Part II (3)) are operational with test reports available on reasoned request from MSA (Annex VII §6); the manufacturer policies, processes, and procedures (Art. 13(8) — cross to 9.1) are documented and operational; the MSA cooperation obligation (Art. 13(22)) is operationalised as: technical documentation + risk-assessment documentation + SBOM available to MSA on reasoned request `where necessary to check compliance`; the recipient is the **MSA (market surveillance authority) + users** on the Annex VII §5–§8 technical documentation + Annex VII §3 risk-assessment documentation + Annex I Part II (3) effective/regular tests + Art. 13(22) MSA cooperation; verified by MSA audit pack (technical documentation content items §5–§8 + risk-assessment documentation + Annex I Part II (3) test reports + Annex VII §6 test reports + Art. 13(8) manufacturer policies/processes/procedures + SBOM-on-request evidence) + automated documentation-integrity test (immutability / version control / cryptographic hash over technical documentation set) + automated support-period retention test (10 years or support period, whichever longer) + automated SBOM-on-request test (SBOM available to MSA on reasoned request within the Art. 13(22) window).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities **develop and document an information security policy defining rules... | DORA | excessive | - | high |

### D-10.2 · DORA · subso SO-D-10.2.DORA
- **Objective**: Financial entities **develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable** (Art. 9(4)(a) DORA); logging is **implicit in the CIA+A monitoring** under the Art. 8(1) continuous-monitoring mandate, not a standalone audit-logging obligation at D-10.2.
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.PO-01, ID.AM-08, GV.OC-03 — literal duplicate(s) of GV.PO-01, ID.AM-08, GV.OC-03
- **Confidence**: high (article mapping and CSF title both consulted)

| "Financial entity develops and documents an information security policy defining rules ... | DORA | sufficient | - | high |

### D-10.2 · DORA · req 10.2.3
- **Title**: "Financial entity develops and documents an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, with logging implicit in CIA+A monitoring"
- **Description**: The product shall develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable (per DORA Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including those of their customers, where applicable`), with logging **implicit in the CIA+A monitoring under the Art. 8(1) continuous-monitoring mandate (cross to 10.1)**, not a standalone audit-logging obligation at 10.2.
- **Fit criterion (prose)**: An information security policy is developed and documented per Art. 9(4)(a) (SR-DORA-031) verified by GV.PO-01 primary (Organizational information security policy is established and communicated — anchors the DORA Art. 9(4)(a) information security policy mapped to NIST CSF 2.0 GV.PO-01) + ID.AM-08 (Data assets are managed consistent with the organization's risk strategy — anchors the CIA+A 4-way of data/information assets/ICT assets 3-way per DomainAnalysis cross-validation) + GV.OC-03 (Legal and regulatory requirements regarding cybersecurity are understood and managed — anchors the Art. 9(4)(a) CIA+A rules + EBA Guidelines supervisory baseline); the information security policy defines rules to protect the CIA+A of data, information assets and ICT assets (the 3-way asset scope), including those of customers where applicable; the policy is documented, communicated, and maintained per GV.PO-01; the logging dimension is **implicit in the CIA+A monitoring under the Art. 8(1) OJ-literal locus Art. 9(1) continuous-monitoring mandate (cross to 10.1)** — **partial coverage only**, no standalone audit-logging obligation at 10.2; the policy is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity); the recipient is the **NCA (national competent authority)** on the Art. 9(4)(a) information security policy + EBA Guidelines supervisory baseline; verified by NCA audit pack (information security policy content + CIA+A rules + EBA Guidelines compliance + Art. 4 proportionality calibration + DORA-led audit-records stack governance) + automated policy-documentation test (policy exists in writing + policy content covers CIA+A 4-way + policy references the Art. 8(1) continuous-monitoring mandate + policy identifies the audit-records stack governance).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 10 action tokens with objective
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — CSF title literally matches action keyword ('policy')
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: high (article mapping and CSF title both consulted)

| The controller and processor **maintain compliance records in writing or in electronic ... | GDPR | excessive | - | low |

### D-10.2 · GDPR · subso SO-D-10.2.GDPR
- **Objective**: The controller and processor **maintain compliance records in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections** (Art. 30(3) + Art. 5(2) + Art. 31 GDPR), including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — made available to the supervisory authority on request (Art. 30(3)).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_13.md` (Art. 13) — paraphrased action
- **Anchors listed**:
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.AM-03 — Representations of the organization's authorized network communication and internal and external network data flows are maintained — **CORE** — CSF title shares 2 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 4 action tokens with objective
  - DE.AE-03 — Information is correlated from multiple sources — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - RS.AN-07 — Incident data and metadata are collected, and their integrity and provenance are preserved — **CORE** — CSF title shares 2 action tokens with objective
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 4 action tokens with objective
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.PO-02, PR.PS-04, PR.DS-11 — literal duplicate(s) of GV.PO-02, PR.PS-04, PR.DS-11
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller and processor maintain compliance records in writing or electronic form wit... | GDPR | sufficient | - | low |

### D-10.2 · GDPR · req 10.2.1
- **Title**: "Controller and processor maintain compliance records in writing or electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections"
- **Description**: The product shall maintain compliance records — including records of processing activities, consent records, processor contract records, breach notification records, and DPIA records — in writing or in electronic form with integrity and traceability sufficient to demonstrate compliance and to support supervisory-authority inspections (per GDPR Art. 30(3) `The records referred to in paragraphs 1 and 2 shall be maintained in writing, including in electronic form, and shall be made available to the supervisory authority on request`), with the controller or processor responsible for and able to demonstrate compliance (per Art. 5(2) `The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1`) and cooperating with the supervisory authority (per Art. 31).
- **Fit criterion (prose)**: Entity-level compliance records are maintained in writing or electronic form with integrity + traceability per Art. 30(3) + Art. 5(2) + Art. 31 (SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the GDPR Art. 30(3) `in writing, including in electronic form` records integrity mapped to NIST CSF 2.0 PR.DS-11) + PR.PS-04 (Networks and environments are protected — anchors the electronic-form records with integrity controls per DomainAnalysis cross-validation) + DE.CM-01 (Networks and network services are monitored to find potentially adverse events — anchors the Art. 30(3) traceability dimension + SA-access channel) + GV.PO-02 (Information security policy is established, communicated, and maintained — anchors the Art. 5(2) accountability demonstrability burden); the records content covers RoPA (records of processing activities per Art. 30(1)/(2)), consent records (Art. 7(1) + Recital 32 + EDPB Guidelines 05/2020 on consent), processor contract records (Art. 28(3)), breach notification records (Art. 33(1) + Art. 34(1)), and DPIA records (Art. 35(1)–(7)); the records are maintained in writing or in electronic form with integrity controls (immutability / write-once / cryptographic hash / version control) + traceability controls (audit trail of record access + modification + retention + destruction); the Art. 5(2) accountability demonstrability burden is operationalised as: the controller or processor can demonstrate ex post, against the supervisory authority inspection, that the compliance records were maintained in writing/electronic form with integrity + traceability sufficient for the SA to inspect; the Art. 31 SA cooperation obligation is operationalised as: records are made available to the supervisory authority on request (per Art. 30(3) `made available to the supervisory authority on request`); the recipient is the **data subject + DPA (supervisory authority)** on the Art. 30(3) compliance records + Art. 5(2) accountability evidence + Art. 31 SA cooperation; verified by DPA audit pack (RoPA evidence + consent records evidence + processor contract records + breach notification records + DPIA records + Art. 5(2) accountability demonstrability evidence + Art. 31 SA cooperation evidence) + automated records-integrity test (immutability / write-once / cryptographic hash chain over record set) + automated records-traceability test (audit trail of record access + modification + retention + destruction) + manual DPA-access simulation (records made available to SA on request within the Art. 30(3) window).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md` (Art. 12) — paraphrased action
- **Anchors listed**:
  - DE.CM-01 — Networks and network services are monitored to find potentially adverse events — **CORE** — CSF title literally matches action keyword ('monitor')
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title literally matches action keyword ('policy')
  - PR.DS-11 — Backups of data are created, protected, maintained, and tested — **CORE** — CSF title shares 5 action tokens with objective
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 6 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## D-10.3 Compliance Testing

| Objective | Regulation | Verdict | Missing | Confidence |
|---|---|---|---|---|
| Providers of high-risk AI systems ensure the systems are **tested for the purpose of id... | AI_Act | excessive | - | low |

### D-10.3 · AI_Act · subso SO-D-10.3.AI_Act
- **Objective**: Providers of high-risk AI systems ensure the systems are **tested for the purpose of identifying the most appropriate and targeted risk management measures**, and **testing shall ensure that high-risk AI systems perform consistently for their intended purpose** (Art. 9(6) AI Act); testing procedures may include **testing in real-world conditions in accordance with Article 60** (Art. 9(7) AI Act); high-risk AI systems are **designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout their lifecycle** (Art. 15(1) AI Act).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 5 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **CORE** — CSF title shares 2 action tokens with objective
  - PR.IR-03 — Mechanisms are implemented to achieve resilience requirements in normal and adverse situations — **CORE** — CSF title shares 3 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 3 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 3 action tokens with objective
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 5 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.IM-03 — literal duplicate(s) of ID.IM-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Provider ensures high-risk AI system is tested for the purpose of identifying risk man... | AI_Act | sufficient | - | low |

### D-10.3 · AI_Act · req 10.3.5
- **Title**: "Provider ensures high-risk AI system is tested for the purpose of identifying risk management measures, performs consistently for intended purpose, may be tested in real-world conditions per Article 60, and achieves appropriate accuracy/robustness/cybersecurity throughout the AI-system lifecycle"
- **Description**: The product shall be tested for the purpose of identifying the most appropriate and targeted risk management measures, with testing ensuring that the high-risk AI system performs consistently for its intended purpose (per AI Act Art. 9(6) `High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose`); testing procedures may include testing in real-world conditions in accordance with Article 60 (per Art. 9(7) `Testing procedures may include testing in real-world conditions in accordance with Article 60`); the high-risk AI system shall be designed and developed to achieve an appropriate level of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout its lifecycle (per Art. 15(1) `High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle`).
- **Fit criterion (prose)**: AI-system-level testing is operational per Art. 9(6) + Art. 9(7) + Art. 15(1) (SR-AIACT-003 + SR-AIACT-014) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the AI Act Art. 9(6) `tested for the purpose of identifying the most appropriate and targeted risk management measures` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 9(6) testing-for-risk-management risk-input dimension + Art. 9(7) real-world-conditions testing risk-input dimension) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 15(1) `throughout their lifecycle` lifecycle-testing dimension + the AI-system operational dimension) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 9(6) testing-for-risk-management feedback loop into the AI-Act provider's risk-management-system documentation (Art. 9 — cross to 9.1)); the Art. 9(6) testing-for-risk-management is operational with tests identifying the most appropriate and targeted risk management measures + tests ensuring consistent performance for the intended purpose; the Art. 9(7) real-world-conditions testing is operational per the Art. 60 detailed rules (testing in real-world conditions subject to the Art. 60 conditions); the Art. 15(1) `throughout their lifecycle` lifecycle-testing is operational with accuracy + robustness + cybersecurity baseline testing + consistent performance in those respects throughout the AI-system lifecycle; the testing regime is calibrated to (a) identify the most appropriate and targeted risk management measures (Art. 9(6) testing-for-risk-management), (b) potentially include real-world-conditions testing per Art. 60 (Art. 9(7)), AND (c) achieve an appropriate level of accuracy, robustness, and cybersecurity throughout the AI-system lifecycle (Art. 15(1) baseline); the recipient is the **provider + MSA (market surveillance authority) + AI Office** on the Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing per Art. 60 + Art. 15(1) accuracy/robustness/cybersecurity baseline testing throughout AI-system lifecycle; verified by MSA + AI Office audit pack (Art. 9(6) testing-for-risk-management outputs + Art. 9(7) real-world-conditions testing outputs + Art. 15(1) baseline testing outputs + lifecycle-testing evidence + Art. 9 risk-management-system documentation feedback loop (cross to 9.1) + Art. 72 post-market monitoring plan alignment (cross to 10.1)) + automated testing-for-risk-management test (tests identify risk management measures + tests ensure consistent performance for intended purpose) + automated real-world-conditions test (Art. 60 conditions met when real-world-conditions testing is included) + automated lifecycle-baseline test (accuracy + robustness + cybersecurity baseline throughout AI-system lifecycle).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 7 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Manufacturers of products with digital elements **carry out effective and regular tests... | CRA | excessive | - | low |

### D-10.3 · CRA · subso SO-D-10.3.CRA
- **Objective**: Manufacturers of products with digital elements **carry out effective and regular tests and reviews of the product** (Annex I Part II (3) CRA), and the technical documentation shall contain **the reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I** (Annex VII §6 CRA); conformity is demonstrated via the Annex VIII Part I (Module A internal production control) or Part II (Module B+C and H notified-body EU-type examination) conformity-assessment modules depending on product classification (Class I / Class II / critical per Art. 6 + Annex III).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-04
  - GV.OV-01 — Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **CORE** — Action keyword ('vulnerability') in objective maps to ID.RA-01
  - GV.OC-03 — Legal, regulatory, and contractual requirements regarding cybersecurity - including privacy and civil liberties obligations - are understood and managed — **CORE** — CSF title shares 3 action tokens with objective
  - GV.SC-04 — Suppliers are known and prioritized by criticality — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 2 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.IM-03 — literal duplicate(s) of ID.IM-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Manufacturer carries out effective and regular tests of the product, demonstrates conf... | CRA | sufficient | - | low |

### D-10.3 · CRA · req 10.3.3
- **Title**: "Manufacturer carries out effective and regular tests of the product, demonstrates conformity via OJ-codified modules (Module A or Module B+C and H), and includes test reports in technical documentation"
- **Description**: The product shall be subject to effective and regular tests and reviews (per CRA Annex I Part II (3) `carry out effective and regular tests and reviews of the product`), with conformity demonstrated via the OJ-codified modules — Annex VIII Part I (Module A internal production control — manufacturer self-assessment) or Annex VIII Part II (Module B+C and H notified-body EU-type examination certificate) depending on product classification (Class I / Class II / critical per Art. 6 + Annex III); the technical documentation shall contain reports of the tests carried out to verify the conformity of the product with digital elements and of the vulnerability-handling processes with the essential cybersecurity requirements set out in Part I and Part II of Annex I (per Annex VII §6).
- **Fit criterion (prose)**: Product-level conformity-assessment is operational per Annex I Part II (3) + Annex VII §6 + Annex VIII Part I (Module A) + Annex VIII Part II (Module B+C and H) (SR-CRA-101 + SR-CRA-103 + SR-CRA-104) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the CRA Annex I Part II (3) `effective and regular tests and reviews` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Annex VII §6 test reports as input to the conformity-assessment risk dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Annex I Part II (3) effective and regular tests as input to the vulnerability-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Annex VIII Part I–IV modules feedback loop into the manufacturer's quality-management system (Art. 13(8) cross to 9.1)); the Annex I Part II (3) `effective and regular tests` cadence is entity-discretionary under proportionality; the Annex VIII Part I (Module A internal production control) is operational for Class I products (manufacturer self-assessment); the Annex VIII Part II (Module B+C and H notified-body EU-type examination certificate) is operational for Class II and critical products (per Art. 6 + Annex III); the Annex VII §6 test reports are part of the technical documentation and available to MSA on reasoned request per Art. 13(22); the manufacturer policies, processes, and procedures (Art. 13(8) — cross to 9.1) feed the conformity-assessment feedback loop; the recipient is the **MSA (market surveillance authority)** on the Annex VII §6 test reports + Annex VIII Part I–IV conformity-assessment certificates + Annex I Part II (3) effective/regular tests; verified by MSA audit pack (Annex VII §6 test reports + Annex VIII conformity-assessment certificates + Annex I Part II (3) effective/regular tests evidence + module selection per product classification + Art. 13(22) MSA cooperation evidence + Art. 13(8) manufacturer policies/processes/procedures feedback loop) + automated conformity-assessment test (Module A self-assessment operational for Class I / Module B+C and H notified-body EU-type examination operational for Class II and critical) + automated Annex VII §6 test-report test (test reports part of technical documentation) + manual Annex I Part II (3) effective/regular tests review (tests executed + evidenced + cadence operational).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 6 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 5 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Financial entities **establish, maintain and review a sound and comprehensive digital o... | DORA | excessive | - | low |

### D-10.3 · DORA · subso SO-D-10.3.DORA
- **Objective**: Financial entities **establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework** (Art. 24(1) DORA), using a 12-way portfolio of testing methodologies (Art. 25(1) DORA); **significant financial entities carry out advanced testing of their ICT systems using threat-led penetration testing (TLPT) on a regular basis** (Art. 26(1) DORA per the Regulatory Technical Standards under Art. 26(8)).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.OV-02 — The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-01 — Vulnerabilities in assets are identified, validated, and recorded — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-06 — Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle — **CORE** — CSF title shares 3 action tokens with objective
  - ID.RA-04 — Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded — **CORE** — Action keyword ('risk') in objective maps to ID.RA-04
  - PR.AA-05 — Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties — **CORE** — CSF title shares 2 action tokens with objective
  - PR.AA-06 — Physical access to assets is managed, monitored, and enforced commensurate with risk — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — Action keyword ('log') in objective maps to DE.AE-02
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.IM-03 — literal duplicate(s) of ID.IM-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Financial entity establishes, maintains and reviews a sound and comprehensive digital ... | DORA | sufficient | - | low |

### D-10.3 · DORA · req 10.3.4
- **Title**: "Financial entity establishes, maintains and reviews a sound and comprehensive digital operational resilience testing programme with a 12-way testing modalities portfolio and TLPT for significant entities on a regular basis"
- **Description**: The product shall establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework (per DORA Art. 24(1) `Financial entities shall, in accordance with Chapter II, establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework`), using a 12-way portfolio of testing methodologies (per Art. 25(1)); significant financial entities shall carry out advanced testing of their ICT systems using threat-led penetration testing (TLPT) on a regular basis (per Art. 26(1) `Significant financial entities shall, on a regular basis, carry out advanced testing of their ICT systems using threat-led penetration testing`) per the Regulatory Technical Standards under Art. 26(8).
- **Fit criterion (prose)**: A digital operational resilience testing programme is established, maintained, and reviewed per Art. 24(1) + Art. 25(1) + Art. 26(1) (SR-DORA-008 + SR-DORA-009 + SR-DORA-010) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the DORA Art. 24(1) `sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 25(1) 12-way modalities risk-input dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the Art. 25(1) testing modalities input to the incident-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 24(1) `establish, maintain and review` testing programme lifecycle feedback loop) + PR.PS-04 (Software installation, operation, and updates are performed consistent with the security policy — anchors the Art. 25(1) testing modalities operational dimension + Art. 26(1) TLPT operational dimension); the Art. 24(1) `sound and comprehensive` testing programme is established, maintained, and reviewed as an integral part of the ICT risk-management framework; the Art. 25(1) 12-way testing modalities portfolio is operational (the 12-way enumerative list per Art. 25(1)); the Art. 26(1) TLPT for significant entities is operational `on a regular basis` per the Regulatory Technical Standards under Art. 26(8); the programme is calibrated to the Art. 4 proportionality factors (size, nature, scale, complexity); the recipient is the **NCA (national competent authority)** on the Art. 24(1) testing programme + Art. 25(1) 12-way modalities + Art. 26(1) TLPT reports; verified by NCA audit pack (Art. 24(1) testing programme content + Art. 25(1) 12-way modalities coverage + Art. 26(1) TLPT reports for significant entities + Art. 4 proportionality calibration + programme review cadence + EBA Guidelines supervisory baseline) + automated testing-programme test (programme exists in writing + programme is integral part of ICT risk-management framework + 12-way modalities coverage + TLPT cadence for significant entities) + manual programme-review review (programme established, maintained, reviewed + TLPT executed + evidenced + cadence operational + proportionality calibrated).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 6 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - PR.PS-04 — Log records are generated and made available for continuous monitoring — **CORE** — CSF title literally matches action keyword ('log')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| The controller and processor implement appropriate technical and organisational measure... | GDPR | excessive | - | low |

### D-10.3 · GDPR · subso SO-D-10.3.GDPR
- **Objective**: The controller and processor implement appropriate technical and organisational measures including **a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing** (Art. 32(1)(d) GDPR); the DPIA is **reviewed at least when there is a change of the risk represented by processing operations** (Art. 35(11) GDPR).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_27.md` (Art. 27) — paraphrased action
- **Anchors listed**:
  - RS.CO-03 — Information is shared with designated internal and external stakeholders — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - RS.MA-04 — Incidents are escalated or elevated as needed — **UTILITY** — Reinforces obligation in same CSF function (RESPOND) but does not directly match the action
  - RS.CO-02 — Internal and external stakeholders are notified of incidents — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.AM-08 — Systems, hardware, software, services, and data are managed throughout their life cycles — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **UTILITY** — CSF title shares 1 token ('and') with objective; reinforces but is not the direct action
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 4 action tokens with objective
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: ID.IM-03 — literal duplicate(s) of ID.IM-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Controller and processor establish a process for regularly testing, assessing and eval... | GDPR | sufficient | - | low |

### D-10.3 · GDPR · req 10.3.1
- **Title**: "Controller and processor establish a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures, with DPIA review at least when there is a change of the risk"
- **Description**: The product shall implement appropriate technical and organisational measures including a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing (per GDPR Art. 32(1)(d) `a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing`); the DPIA shall be reviewed at least when there is a change of the risk represented by processing operations (per Art. 35(11) `at least when there is a change of the risk represented by processing operations`).
- **Fit criterion (prose)**: An effectiveness-evaluation process is established per Art. 32(1)(d) + Art. 35(11) (SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the GDPR Art. 32(1)(d) `regularly testing, assessing and evaluating the effectiveness of technical and organisational measures` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the Art. 35(11) DPIA review on risk change dimension) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-evaluation input to the incident-handling chain) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 35(11) DPIA review feedback loop into the risk-management strategy); the Art. 32(1)(d) `regularly testing, assessing and evaluating` cadence is entity-discretionary under Art. 32(1)(d) `regularly` (DPO-discretionary); the Art. 35(11) DPIA review trigger is `at least when there is a change of the risk represented by processing operations` (event-triggered + minimum cadence on risk change); the Art. 32(1)(d) effectiveness-evaluation inputs feed the incident-handling chain (4.1) via DE.AE-02; the Art. 35(11) DPIA review feeds the risk-management strategy feedback loop (cross to 9.2) via GV.OV-03; the content of the effectiveness-evaluation is not codified (entity-discretionary under Art. 24(1) chapeau); the recipient is the **data subject + DPA (supervisory authority)** on the Art. 32(1)(d) effectiveness-evaluation evidence + Art. 35(11) DPIA review evidence; verified by DPA audit pack (effectiveness-evaluation cadence evidence + Art. 35(11) DPIA review on risk change evidence + Art. 5(2) accountability demonstrability burden + effectiveness-evaluation inputs to incident-handling chain + DPIA review feedback loop into risk-management strategy) + automated cadence test (regularly testing cadence operational + DPIA review trigger operational on risk change) + manual effectiveness-evaluation review (process for testing/assessing/evaluating is documented + executed + evidenced).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 6 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 4 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| Essential and important entities establish **policies and procedures to assess the effe... | NIS2 | excessive | - | low |

### D-10.3 · NIS2 · subso SO-D-10.3.NIS2
- **Objective**: Essential and important entities establish **policies and procedures to assess the effectiveness of cybersecurity risk-management measures** (Art. 21(2)(f) NIS 2) as part of the all-hazards risk-management framework; the cadence is entity-discretionary under Recital 56 (no quantitative threshold in the OJ).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_21.md` (Art. 21) — paraphrased action
- **Anchors listed**:
  - GV.PO-01 — Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced — **CORE** — Action keyword ('policies') in objective maps to GV.PO-01
  - ID.IM-01 — Improvements are identified from evaluations — **UTILITY** — Reinforces obligation in same CSF function (IDENTIFY) but does not directly match the action
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 2 action tokens with objective
  - GV.PO-02 — Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 2 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 2 action tokens with objective
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **UTILITY** — Reinforces obligation in same CSF function (DETECT) but does not directly match the action
- **Coverage verdict**: excessive (1 redundant anchor set(s))
- **Missing (if any)**: none detected
- **Excessive (1)**: GV.OV-03, ID.IM-03 — literal duplicate(s) of GV.OV-03, ID.IM-03
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

| "Essential and important entities establish policies and procedures to assess the effec... | NIS2 | sufficient | - | low |

### D-10.3 · NIS2 · req 10.3.2
- **Title**: "Essential and important entities establish policies and procedures to assess the effectiveness of cybersecurity risk-management measures as part of the all-hazards risk-management framework"
- **Description**: The product shall establish policies and procedures to assess the effectiveness of cybersecurity risk-management measures (per NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures`) as part of the all-hazards risk-management framework; the cadence is entity-discretionary under Recital 56 (no quantitative threshold in the OJ).
- **Fit criterion (prose)**: Effectiveness-assessment policies and procedures are established per Art. 21(2)(f) (SR-NIS2-037 + SR-NIS2-038) verified by ID.IM-03 primary (Configuration change control processes are in place — anchors the NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity risk-management measures` mapped to NIST CSF 2.0 ID.IM-03) + ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to establish risk tolerances — anchors the effectiveness-assessment feedback loop into the risk-management framework) + GV.OV-03 (Cybersecurity risk management strategy outcomes are reviewed and inform changes — anchors the Art. 21(2)(f) effectiveness-assessment feedback into the all-hazards risk-management strategy outcomes) + DE.AE-02 (Adverse events are analyzed to identify or determine the scope of an incident — anchors the effectiveness-assessment input to the incident-handling chain); the Art. 21(2)(f) cadence is entity-discretionary under Recital 56 (no quantitative threshold); the content is not codified (policies-and-procedures POLY); the policies and procedures feed the Art. 21(2)(a)–(j) risk-management cycle; the effectiveness-assessment inputs feed the incident-handling chain (4.1) via DE.AE-02; the recipient is the **management body + competent authority (CSIRT — Computer Security Incident Response Team or national competent authority)** on the Art. 21(2)(f) effectiveness-assessment outputs as part of the all-hazards risk-management framework; verified by CSIRT audit pack (policies and procedures content + cadence + effectiveness-assessment outputs + Art. 21(2)(a)–(j) risk-management cycle integration + incident-handling chain inputs) + automated policy-and-procedure test (policies exist in writing + procedures exist for execution + cadence operational + evidence templates defined) + manual effectiveness-assessment review (policies and procedures executed + evidenced + fed into risk-management cycle).
- **Regulatory basis**: `domains/D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md` (Art. 9) — paraphrased action
- **Anchors listed**:
  - DE.AE-02 — Potentially adverse events are analyzed to better understand associated activities — **CORE** — CSF title literally matches action keyword ('adverse event')
  - GV.OV-03 — Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed — **CORE** — CSF title shares 6 action tokens with objective
  - ID.IM-03 — Improvements are identified from execution of operational processes, procedures, and activities — **CORE** — CSF title shares 6 action tokens with objective
  - ID.RA-05 — Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization — **CORE** — CSF title literally matches action keyword ('risk')
- **Coverage verdict**: sufficient (at least one CORE anchor and no missing/excessive)
- **Missing (if any)**: none detected
- **Excessive (if any)**: none detected
- **Confidence**: low (no nist_csf_mapping found in candidate articles)

## Per-subdomain summary table

| Subdomain | n_objectives | n_CORE | n_UTILITY | n_NOISE | n_missing | verdict |
|---|---|---|---|---|---|---|
| D-01.1 | 8 | 22 | 0 | 0 | 0 | sufficient |
| D-01.2 | 6 | 16 | 1 | 0 | 0 | sufficient |
| D-01.3 | 6 | 25 | 3 | 0 | 0 | sufficient |
| D-01.4 | 8 | 42 | 2 | 0 | 0 | sufficient |
| D-02.1 | 10 | 45 | 6 | 0 | 0 | sufficient |
| D-02.2 | 4 | 11 | 0 | 0 | 2 | partial |
| D-02.3 | 4 | 9 | 0 | 0 | 0 | sufficient |
| D-02.4 | 6 | 29 | 3 | 0 | 0 | sufficient |
| D-03.1 | 8 | 39 | 2 | 0 | 0 | sufficient |
| D-03.2 | 8 | 35 | 4 | 0 | 0 | sufficient |
| D-03.3 | 8 | 44 | 0 | 0 | 0 | sufficient |
| D-03.4 | 4 | 18 | 2 | 0 | 0 | sufficient |
| D-04.1 | 8 | 42 | 5 | 0 | 0 | sufficient |
| D-04.2 | 8 | 41 | 6 | 0 | 2 | partial |
| D-04.3 | 10 | 14 | 19 | 0 | 0 | sufficient |
| D-04.4 | 8 | 25 | 2 | 0 | 1 | partial |
| D-05.1 | 6 | 15 | 0 | 0 | 0 | sufficient |
| D-05.2 | 6 | 13 | 0 | 0 | 1 | partial |
| D-05.3 | 4 | 15 | 0 | 0 | 0 | sufficient |
| D-05.4 | 2 | 4 | 0 | 0 | 0 | sufficient |
| D-06.1 | 8 | 35 | 6 | 0 | 0 | sufficient |
| D-06.2 | 2 | 3 | 0 | 0 | 0 | sufficient |
| D-06.3 | 8 | 32 | 12 | 0 | 0 | sufficient |
| D-06.4 | 8 | 22 | 7 | 0 | 0 | sufficient |
| D-07.1 | 10 | 28 | 6 | 0 | 1 | partial |
| D-07.2 | 6 | 19 | 4 | 0 | 0 | sufficient |
| D-07.3 | 4 | 10 | 4 | 0 | 0 | sufficient |
| D-07.4 | 4 | 19 | 9 | 0 | 0 | sufficient |
| D-08.1 | 8 | 28 | 2 | 0 | 0 | sufficient |
| D-08.2 | 10 | 47 | 2 | 0 | 0 | sufficient |
| D-08.3 | 4 | 12 | 0 | 0 | 0 | sufficient |
| D-09.1 | 10 | 58 | 3 | 0 | 0 | sufficient |
| D-09.2 | 10 | 35 | 3 | 0 | 0 | sufficient |
| D-09.3 | 6 | 22 | 1 | 0 | 0 | sufficient |
| D-09.4 | 10 | 25 | 8 | 0 | 0 | sufficient |
| D-10.1 | 10 | 44 | 11 | 0 | 0 | sufficient |
| D-10.2 | 8 | 42 | 8 | 0 | 0 | sufficient |
| D-10.3 | 10 | 57 | 15 | 0 | 0 | sufficient |

## Final stats

- Total records processed: **268**
- Verdicts: sufficient=187, partial=3, excessive=78
- Confidence: high=163, medium=0, low=105

### Low-confidence entries

- `D-01.4` `SO-D-01.4.GDPR` — no nist_csf_mapping found in candidate articles
- `D-01.4` `1.4.1` — no nist_csf_mapping found in candidate articles
- `D-02.1` `2.1.1` — no nist_csf_mapping found in candidate articles
- `D-03.1` `SO-D-03.1.NIS2` — no nist_csf_mapping found in candidate articles
- `D-03.1` `3.1.2` — no nist_csf_mapping found in candidate articles
- `D-03.2` `SO-D-03.2.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-03.2` `3.2.3` — no candidate_articles listed; cannot cross-check article mappings
- `D-03.2` `SO-D-03.2.GDPR` — no nist_csf_mapping found in candidate articles
- `D-03.2` `3.2.1` — no nist_csf_mapping found in candidate articles
- `D-03.3` `SO-D-03.3.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-03.3` `3.3.3` — no nist_csf_mapping found in candidate articles
- `D-03.3` `SO-D-03.3.NIS2` — no nist_csf_mapping found in candidate articles
- `D-03.3` `3.3.2` — no nist_csf_mapping found in candidate articles
- `D-03.4` `SO-D-03.4.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-04.1` `SO-D-04.1.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-04.1` `SO-D-04.1.NIS2` — no nist_csf_mapping found in candidate articles
- `D-04.1` `4.1.2` — no nist_csf_mapping found in candidate articles
- `D-04.2` `SO-D-04.2.CRA` — no nist_csf_mapping found in candidate articles
- `D-04.2` `4.2.3` — no nist_csf_mapping found in candidate articles
- `D-04.3` `4.3.3` — no nist_csf_mapping found in candidate articles
- `D-04.4` `SO-D-04.4.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-04.4` `4.4.3` — no nist_csf_mapping found in candidate articles
- `D-05.1` `5.1.1` — no nist_csf_mapping found in candidate articles
- `D-05.3` `SO-D-05.3.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-05.3` `5.3.2` — no nist_csf_mapping found in candidate articles
- `D-06.1` `6.1.2` — no nist_csf_mapping found in candidate articles
- `D-06.3` `SO-D-06.3.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-06.3` `SO-D-06.3.GDPR` — no nist_csf_mapping found in candidate articles
- `D-06.3` `6.3.1` — no nist_csf_mapping found in candidate articles
- `D-06.3` `6.3.2` — no nist_csf_mapping found in candidate articles
- `D-06.4` `SO-D-06.4.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-06.4` `SO-D-06.4.NIS2` — no nist_csf_mapping found in candidate articles
- `D-06.4` `6.4.2` — no nist_csf_mapping found in candidate articles
- `D-07.1` `7.1.3` — no nist_csf_mapping found in candidate articles
- `D-07.1` `7.1.2` — no nist_csf_mapping found in candidate articles
- `D-07.2` `SO-D-07.2.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.2` `7.2.1` — no nist_csf_mapping found in candidate articles
- `D-07.2` `SO-D-07.2.DORA` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.2` `7.2.2` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.3` `SO-D-07.3.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.3` `7.3.2` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.3` `SO-D-07.3.NIS2` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.3` `7.3.1` — no candidate_articles listed; cannot cross-check article mappings
- `D-07.4` `SO-D-07.4.CRA` — no nist_csf_mapping found in candidate articles
- `D-07.4` `7.4.1` — no candidate_articles listed; cannot cross-check article mappings
- `D-08.2` `SO-D-08.2.AIACT` — no nist_csf_mapping found in candidate articles
- `D-08.2` `8.2.5` — no nist_csf_mapping found in candidate articles
- `D-08.2` `SO-D-08.2.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-08.2` `8.2.3` — no nist_csf_mapping found in candidate articles
- `D-09.1` `SO-D-09.1.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-09.1` `9.1.5` — no nist_csf_mapping found in candidate articles
- `D-09.1` `SO-D-09.1.CRA` — no nist_csf_mapping found in candidate articles
- `D-09.1` `9.1.3` — no nist_csf_mapping found in candidate articles
- `D-09.1` `SO-D-09.1.DORA` — no nist_csf_mapping found in candidate articles
- `D-09.1` `9.1.4` — no nist_csf_mapping found in candidate articles
- `D-09.1` `SO-D-09.1.GDPR` — no nist_csf_mapping found in candidate articles
- `D-09.1` `9.1.1` — no nist_csf_mapping found in candidate articles
- `D-09.1` `SO-D-09.1.NIS2` — no nist_csf_mapping found in candidate articles
- `D-09.1` `9.1.2` — no nist_csf_mapping found in candidate articles
- `D-09.2` `SO-D-09.2.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-09.2` `9.2.5` — no nist_csf_mapping found in candidate articles
- `D-09.2` `SO-D-09.2.CRA` — no nist_csf_mapping found in candidate articles
- `D-09.2` `9.2.3` — no nist_csf_mapping found in candidate articles
- `D-09.2` `SO-D-09.2.DORA` — no nist_csf_mapping found in candidate articles
- `D-09.2` `9.2.4` — no nist_csf_mapping found in candidate articles
- `D-09.2` `SO-D-09.2.GDPR` — no nist_csf_mapping found in candidate articles
- `D-09.2` `9.2.1` — no nist_csf_mapping found in candidate articles
- `D-09.2` `SO-D-09.2.NIS2` — no nist_csf_mapping found in candidate articles
- `D-09.2` `9.2.2` — no nist_csf_mapping found in candidate articles
- `D-09.3` `SO-D-09.3.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-09.3` `9.3.2` — no nist_csf_mapping found in candidate articles
- `D-09.4` `SO-D-09.4.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-09.4` `9.4.5` — no nist_csf_mapping found in candidate articles
- `D-09.4` `SO-D-09.4.CRA` — no nist_csf_mapping found in candidate articles
- `D-09.4` `9.4.3` — no nist_csf_mapping found in candidate articles
- `D-09.4` `SO-D-09.4.DORA` — no candidate_articles listed; cannot cross-check article mappings
- `D-09.4` `9.4.4` — no nist_csf_mapping found in candidate articles
- `D-09.4` `SO-D-09.4.GDPR` — no nist_csf_mapping found in candidate articles
- `D-09.4` `9.4.1` — no nist_csf_mapping found in candidate articles
- `D-10.1` `SO-D-10.1.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-10.1` `10.1.5` — no nist_csf_mapping found in candidate articles
- `D-10.1` `SO-D-10.1.CRA` — no candidate_articles listed; cannot cross-check article mappings
- `D-10.1` `10.1.3` — no nist_csf_mapping found in candidate articles
- `D-10.1` `SO-D-10.1.DORA` — no nist_csf_mapping found in candidate articles
- `D-10.1` `10.1.4` — no nist_csf_mapping found in candidate articles
- `D-10.1` `SO-D-10.1.GDPR` — no nist_csf_mapping found in candidate articles
- `D-10.1` `10.1.1` — no nist_csf_mapping found in candidate articles
- `D-10.1` `SO-D-10.1.NIS2` — no nist_csf_mapping found in candidate articles
- `D-10.1` `10.1.2` — no nist_csf_mapping found in candidate articles
- `D-10.2` `SO-D-10.2.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-10.2` `10.2.4` — no nist_csf_mapping found in candidate articles
- `D-10.2` `SO-D-10.2.CRA` — no nist_csf_mapping found in candidate articles
- `D-10.2` `10.2.2` — no nist_csf_mapping found in candidate articles
- `D-10.2` `SO-D-10.2.GDPR` — no nist_csf_mapping found in candidate articles
- `D-10.2` `10.2.1` — no nist_csf_mapping found in candidate articles
- `D-10.3` `SO-D-10.3.AI_Act` — no nist_csf_mapping found in candidate articles
- `D-10.3` `10.3.5` — no nist_csf_mapping found in candidate articles
- `D-10.3` `SO-D-10.3.CRA` — no nist_csf_mapping found in candidate articles
- `D-10.3` `10.3.3` — no nist_csf_mapping found in candidate articles
- `D-10.3` `SO-D-10.3.DORA` — no nist_csf_mapping found in candidate articles
- `D-10.3` `10.3.4` — no nist_csf_mapping found in candidate articles
- `D-10.3` `SO-D-10.3.GDPR` — no nist_csf_mapping found in candidate articles
- `D-10.3` `10.3.1` — no nist_csf_mapping found in candidate articles
- `D-10.3` `SO-D-10.3.NIS2` — no nist_csf_mapping found in candidate articles
- `D-10.3` `10.3.2` — no nist_csf_mapping found in candidate articles
