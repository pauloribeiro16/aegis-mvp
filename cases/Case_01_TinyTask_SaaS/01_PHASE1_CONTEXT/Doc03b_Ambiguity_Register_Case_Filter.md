---
document_id: AEGIS-P1-RICH-05b
title: Ambiguity Register (Rich Mode)
phase: 1
version: 2.1
created: 2026-08-06
updated: 2026-09-14
author: Fase de Especificação 2 Executor (ambiguity-register-builder)
status: CITES_BASELINE_AMBIGUITY_REGISTRY
status_history:
  - { date: '2026-09-14', from: DEEP_ENRICHED, to: CITES_BASELINE_AMBIGUITY_REGISTRY,
      reason: 'F1-pilot C1 fold — case-side Doc09 reclassified from JUSTIFIED-EXTENSION to CITES-BASELINE per phase1_rich_extension.md v1.1. This doc now cites the methodology canon at 00_METHODOLOGY/AMBIGUITY_REGISTRY/ (49 clauses dedup, 5 regulations). Per-case content preserved for graph/parser liveness. Cases adopting a different reading from the canon should document the justified variant here.' }
deep_enrichment_date: 2026-08-06
resolution_sections_added: 20
fields_per_resolution: 3
case: Case_01_TinyTask_SaaS
applicable_regs: [GDPR, CRA]
active_subdomains: 37
inactive_subdomains: [D-08.3]
ambiguity_cards_total: 417
ambiguity_cards_gdpr: 276
ambiguity_cards_cra: 141
ambiguity_cards_top20: 20
source_corpus: 00_METHODOLOGY/PREPROCESSING_by_domain/domains/
related_documents:
  - ../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/README.md (methodology canon — authoritative for ambiguity resolution)
  - ../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/registry.md (49 clauses dedup, GDPR + CRA + NIS 2 + DORA + AI Act)
  - ../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/registry.csv (machine-readable)
  - ../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/changelog.md
classification_in_methodology_diagram: CITES-BASELINE (per phase1_rich_extension.md v1.1, 2026-09-14)
f1_pilot_fold_date: 2026-09-14
---

# Ambiguity Register (Rich Mode)

> **⚠️ F1-pilot C1 fold — 2026-09-14.** A interpretação regulatória de ambiguidade vive agora no canon metodológico
> [`00_METHODOLOGY/AMBIGUITY_REGISTRY/`](../../../../00_METHODOLOGY/AMBIGUITY_REGISTRY/README.md)
> — 49 cláusulas deduplicadas, 5 regulamentos, com variantes, resoluções canónicas e proveniência por caso.
> Este documento é uma **instância per-caso** (CITE-BASELINE) e mantém-se na íntegra para liveness
> do `phase1_graph.json`, dos parsers e do dashboard. **Se esta empresa adopta uma leitura diferente
> da canónica para uma cláusula específica, documente-a aqui como variante justificada** — não substitua
> a canónica silenciosamente. Ver `phase1_rich_extension.md v1.1` para a reclassificação metodológica
> (JUSTIFIED-EXTENSION → CITES-BASELINE) e `CHANGE_LOG_CENTRAL.md` 2026-09-14.

> Filtered corpus ambiguity cards (Berry lens) — only GDPR + CRA applicable sub-domains for Case_01.
> Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/D-XX.Y.json:ambiguity_cards[]`
> Methodology: per-card filter on `regulation ∈ {GDPR, CRA}`; per-SD inclusion if sub-domain appears in `04a_Architecture_DataInventory.md` Compliance Mapping table (37 active sub-domains, D-08.3 inactive).

## §1 Summary Statistics

| Metric | Value |
|--------|-------|
| Total sub-domains inspected | 37 (D-08.3 INACTIVE) |
| Sub-domains with ≥1 in-scope card | 37 |
| Total in-scope cards | 417 |
| GDPR cards | 276 |
| CRA cards | 141 |
| Severity S1 (low) | 0 |
| Severity S2 (medium) | 251 |
| Severity S3 (high) | 252 |

## §2 Per-Sub-Domain Breakdown

| Sub-domain | Sub-domain Name | In-scope / Total cards |
|------------|-----------------|------------------------|
| D-01.1 | Data at Rest Encryption | 12 / 46 |
| D-01.2 | Data in Transit Encryption | 7 / 33 |
| D-01.3 | Key Management | 7 / 11 |
| D-01.4 | Data Integrity Mechanisms | 11 / 18 |
| D-02.1 | Vulnerability Identification | 13 / 70 |
| D-02.2 | Patch Management | 6 / 9 |
| D-02.3 | Coordinated Vulnerability Disclosure | 5 / 32 |
| D-02.4 | Threat-Led Penetration Testing | 2 / 7 |
| D-03.1 | Identity Lifecycle Management | 21 / 75 |
| D-03.2 | Multi-Factor Authentication | 2 / 27 |
| D-03.3 | Authorisation & Least Privilege | 6 / 35 |
| D-03.4 | Secure System Defaults | 6 / 12 |
| D-04.1 | Incident Detection & Triage | 6 / 34 |
| D-04.2 | Containment & Mitigation | 10 / 43 |
| D-04.3 | Regulatory Notification | 34 / 94 |
| D-04.4 | Data Restoration & Recovery | 6 / 41 |
| D-05.1 | Data Minimisation | 27 / 38 |
| D-05.2 | Retention & Archiving | 7 / 14 |
| D-05.3 | Right to Erasure | 12 / 20 |
| D-05.4 | Data Portability | 3 / 6 |
| D-06.1 | Vendor Risk Assessment | 4 / 31 |
| D-06.2 | Software Bill of Materials | 2 / 5 |
| D-06.3 | Contractual Security Obligations | 23 / 76 |
| D-06.4 | Third-Party Boundary Management | 9 / 36 |
| D-07.1 | Secure-by-Design Principles | 17 / 53 |
| D-07.2 | Secure Coding Practices | 2 / 5 |
| D-07.3 | CI/CD Pipeline Security | 2 / 5 |
| D-07.4 | Change Management | 5 / 12 |
| D-08.1 | General Security Awareness | 6 / 39 |
| D-08.2 | Role-Specific Competence | 3 / 33 |
| D-09.1 | Information Security Policies | 53 / 131 |
| D-09.2 | Impact & Risk Assessments | 23 / 87 |
| D-09.3 | Asset Inventories | 3 / 61 |
| D-09.4 | Records of Processing | 33 / 116 |
| D-10.1 | Continuous Security Monitoring | 11 / 66 |
| D-10.2 | Audit Logging & Traceability | 9 / 23 |
| D-10.3 | Compliance Testing | 9 / 39 |

## §3 Top 20 Ambiguity Cards (severity-sorted)

> Selection rule: cards ranked by maximum instance severity (S3 > S2 > S1), then by sub-domain ID. Sub-domain grouping preserved for reviewability.

### D-01.1 — Data at Rest Encryption

- **Sub-domain Path:** `domains/D-01_Data-Protection/D-01.1/`
- **In-scope cards:** 5 of 12 (selected for top 20)

#### Card #1: GDPR-RT16 — Art. 21(1) (Objection grounds and overriding)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`compelling legitimate grounds`).
- **Type:** data subject right (object)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-OBJECTION
- **Corpus path:** `domains/D-01_Data-Protection/D-01.1/D-01.1.json:ambiguity_cards`
- **Case impact:** TinyTask stores EU customer email/name/project data at rest (SYS-01/02/03 + STORE-01/02/03). Encryption choice (column-level vs volume-level) affects breach-likelihood under Art. 32.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `compelling legitimate grounds` (verbatim from corpus)

- **R1 (EDPB Guidelines on legitimate interests.):** `Compelling` = strictly necessary (lex specialis to legitimate interests).
- **R2 (Loose reading.):** `Compelling` = materially more weighty than legitimate interests.



#### Resolution (per card 1):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because EDPB Guidelines are the authoritative interpretation; 'compelling legitimate grounds' under Art. 21(1) anchors on EDPB standard for the controller balancing test.

**Stakeholder Impact:** DPO (must sign off on objection-handling procedure), CTO (technical implementation of opt-out flows), Customers (data subjects exercising Art. 21 right)

**Risk if not resolved:** MEDIUM — audit finding possible under Art. 5(2) accountability if objection grounds differ from EDPB standard

#### Card #2: GDPR-CP02 — Art. 25(1) (Privacy by design)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `effective`, `necessary`).
- **Type:** design obligation
- **Obligated party:** CONTROLLER
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.1/D-01.1.json:ambiguity_cards`
- **Case impact:** TinyTask stores EU customer email/name/project data at rest (SYS-01/02/03 + STORE-01/02/03). Encryption choice (column-level vs volume-level) affects breach-likelihood under Art. 32.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **R1 (Industry reading.):** `State of the art` = ISO 27001 + sector-specific best practices at design time.
- **R2 (Strict reading.):** `State of the art` = ENISA / EDPB-published state-of-the-art guidance.
- **R3 (Loose reading.):** `State of the art` = any reasonable technical measure documented at design time.

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `effective manner` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`effective` is inquiry-resistant but inherits Art. 32(1)(d) testing obligation. S2 because the compliance practice (test + document) is the same.

---
```



#### Resolution (per card 2):

**Recommended Variant:** R2 (Strict reading.) — chosen because Art. 25(1) privacy by design must align with ENISA/EDPB-published state-of-the-art guidance, not just industry practice.

**Stakeholder Impact:** CTO (architectural decisions), DPO (PbD sign-off), Lead Dev (implementation)

**Risk if not resolved:** MEDIUM — Art. 25(1) PbD is a hard obligation; misaligned 'state of the art' reading creates GDPR Art. 5(2) accountability gap

#### Card #3: GDPR-CP15 — Art. 32(1) (Security measures (open list))

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
- **Type:** security
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.1/D-01.1.json:ambiguity_cards`
- **Case impact:** TinyTask stores EU customer email/name/project data at rest (SYS-01/02/03 + STORE-01/02/03). Encryption choice (column-level vs volume-level) affects breach-likelihood under Art. 32.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
```

- **Type:** COORD
- **Severity:** S3
- **Ambiguous phrase:** `(a) AND (b) AND (c) AND (d)` (verbatim from corpus)

- **R1 (Industry standard (BCP/DRP best practice).):** `Timely` = RTO defined per processing activity (objective measure).
- **R2 (EDPB Guidelines 7/2019 (generic).):** `Timely` = as-soon-as-practicable for the specific incident.



#### Resolution (per card 3):

**Recommended Variant:** R2 (EDPB Guidelines 7/2019 (generic).) — chosen because Art. 32(1) open-list security measures align with EDPB Guidelines 7/2019 'timely' = as-soon-as-practicable per specific incident.

**Stakeholder Impact:** CTO + DPO (security measures catalog), Customers (data subjects protected by CIA+R measures)

**Risk if not resolved:** HIGH — Art. 32 is the canonical security obligation; misreading creates direct compliance gap

#### Card #4: GDPR-CL23 — Art. 9(2)(g) (Substantial public interest)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
- **Type:** lawfulness base (special category)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-MEMBER-STATE-LAW
- **Corpus path:** `domains/D-01_Data-Protection/D-01.1/D-01.1.json:ambiguity_cards`
- **Case impact:** TinyTask stores EU customer email/name/project data at rest (SYS-01/02/03 + STORE-01/02/03). Encryption choice (column-level vs volume-level) affects breach-likelihood under Art. 32.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `substantial public interest` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.

S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.

---
```



#### Resolution (per card 4):

**Recommended Variant:** R1 (Per manufacturer instructions — Annex II §8). — chosen because Annex II §8 'necessary measures during initial commissioning' is the literal reading; R1 is the in-Directive disambiguation.

**Stakeholder Impact:** CTO (product installation guidance), Lead Dev (documentation), Customers (per-instructions installation)

**Risk if not resolved:** HIGH — CRA market-surveillance audit risk; non-conformity prevents EU market access

#### Card #5: CRA-CL02 — Art. 6(a) proviso (Installation/use conditions)

- **Card variant:** source-locus
- **Berry anchor:** §5.1 (`properly`).
- **Type:** —
- **Obligated party:** —
- **Obligation type:** —
- **Corpus path:** `domains/D-01_Data-Protection/D-01.1/D-01.1.json:ambiguity_cards`
- **Case impact:** TinyTask stores EU customer email/name/project data at rest (SYS-01/02/03 + STORE-01/02/03). Encryption choice (column-level vs volume-level) affects breach-likelihood under Art. 32.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `properly installed, maintained` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`properly` — what constitutes proper?

- R1: Per manufacturer instructions (Annex II §8).
- R2: Per industry standards.
- R3: Per a reasonable user's understanding.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per instructions | In-Directive: Annex II §8 `necessary measures during initial commissioning` |
| R2 | Per industry | None in OJ |
| R3 | Per reasonable user | None in OJ |

R1 is the literal reading. R2/R3 admit materially different compliance populations. S3.
```

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `intended purpose or under conditions which can reasonably be foreseen` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`intended purpose` (Art. 3(23)) OR `reasonably foreseeable` (Art. 3(24)) — alternative conditions.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Intended purpose OR foreseeable | In-Directive: literal `or` |
| R2 | Intended purpose ONLY | None in OJ |
| R3 | Foreseeable ONLY | None in OJ |

R1 is the literal reading. S3.
```

- **Type:** VAG
- **Severity:** S2
- **Ambiguous phrase:** `where applicable, the necessary security updates have been installed` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`necessary security updates` — which updates are necessary?

- R1: Critical security updates only.
- R2: All security updates.
- R3: Updates required by Annex I Part II §3 (effective and regular tests).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Critical | None in OJ |
| R2 | All | In-Directive: Annex I Part II §3 |
| R3 | Per Annex I | In-Directive: Annex I Part II §3 |

R2 is the literal reading. S2.
```

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `installed` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`installed` — software-only? Hardware? Firmware?

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Software | None in OJ |
| R2 | Hardware | None in OJ |
| R3 | Any | In-Directive: literal `installed` |

R3 is the literal reading. S2.
```




#### Resolution (per card 5):

**Recommended Variant:** R2 (All security updates.) — chosen because Annex I Part II §3 supports R2 'All security updates' reading; aligns with secure-by-default principles.

**Stakeholder Impact:** CTO (update distribution pipeline), Lead Dev (auto-update default), Customers (security update recipients)

**Risk if not resolved:** MEDIUM — installation conditions are user-facing; misalignment creates Art. 6(a) gap

### D-01.2 — Data in Transit Encryption

- **Sub-domain Path:** `domains/D-01_Data-Protection/D-01.2/`
- **In-scope cards:** 3 of 7 (selected for top 20)

#### Card #6: GDPR-RT16 — Art. 21(1) (Objection grounds and overriding)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`compelling legitimate grounds`).
- **Type:** data subject right (object)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-OBJECTION
- **Corpus path:** `domains/D-01_Data-Protection/D-01.2/D-01.2.json:ambiguity_cards`
- **Case impact:** All EU traffic flows cross public networks (FLOW-01/02/03/04/05). Transit encryption (TLS 1.2+/HSTS) is non-negotiable.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `compelling legitimate grounds` (verbatim from corpus)

- **R1 (EDPB Guidelines on legitimate interests.):** `Compelling` = strictly necessary (lex specialis to legitimate interests).
- **R2 (Loose reading.):** `Compelling` = materially more weighty than legitimate interests.



#### Resolution (per card 6):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because EDPB Guidelines are authoritative for Art. 21(1); transit encryption is non-negotiable under Art. 32(1)(a).

**Stakeholder Impact:** CTO (TLS configuration), DPO (Art. 21 objection handling), Customers (transit-protected subjects)

**Risk if not resolved:** MEDIUM — Art. 21 + Art. 32 obligations both apply; EDPB-aligned reading discharges both

#### Card #7: GDPR-CP15 — Art. 32(1) (Security measures (open list))

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
- **Type:** security
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.2/D-01.2.json:ambiguity_cards`
- **Case impact:** All EU traffic flows cross public networks (FLOW-01/02/03/04/05). Transit encryption (TLS 1.2+/HSTS) is non-negotiable.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
```

- **Type:** COORD
- **Severity:** S3
- **Ambiguous phrase:** `(a) AND (b) AND (c) AND (d)` (verbatim from corpus)

- **R1 (Industry standard (BCP/DRP best practice).):** `Timely` = RTO defined per processing activity (objective measure).
- **R2 (EDPB Guidelines 7/2019 (generic).):** `Timely` = as-soon-as-practicable for the specific incident.



#### Resolution (per card 7):

**Recommended Variant:** R2 (EDPB Guidelines 7/2019 (generic).) — chosen because Art. 32(1) security measures on transit encryption follow EDPB 'timely' guidance per specific incident.

**Stakeholder Impact:** CTO + DPO (security measures catalog for transit), Customers (transit-protected subjects)

**Risk if not resolved:** HIGH — Art. 32 is canonical; transit encryption is a primary control

#### Card #8: GDPR-CL23 — Art. 9(2)(g) (Substantial public interest)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
- **Type:** lawfulness base (special category)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-MEMBER-STATE-LAW
- **Corpus path:** `domains/D-01_Data-Protection/D-01.2/D-01.2.json:ambiguity_cards`
- **Case impact:** All EU traffic flows cross public networks (FLOW-01/02/03/04/05). Transit encryption (TLS 1.2+/HSTS) is non-negotiable.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `substantial public interest` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.

S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.

---
```




#### Resolution (per card 8):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because Art. 21 + Art. 32 obligations converge on EDPB-aligned reading for transit encryption under substantial public interest clauses.

**Stakeholder Impact:** CTO + DPO (transit controls + objection handling), Customers

**Risk if not resolved:** MEDIUM — Art. 9(2)(g) special category rarely applies to TinyTask (no special category data)

### D-01.3 — Key Management

- **Sub-domain Path:** `domains/D-01_Data-Protection/D-01.3/`
- **In-scope cards:** 5 of 7 (selected for top 20)

#### Card #9: GDPR-CP02 — Art. 25(1) (Privacy by design)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `effective`, `necessary`).
- **Type:** design obligation
- **Obligated party:** CONTROLLER
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.3/D-01.3.json:ambiguity_cards`
- **Case impact:** KMS choice (AWS KMS vs HSM) affects Art. 32(1)(a) pseudonymisation/encryption and CRA Annex I §1.2 attack-surface.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **R1 (Industry reading.):** `State of the art` = ISO 27001 + sector-specific best practices at design time.
- **R2 (Strict reading.):** `State of the art` = ENISA / EDPB-published state-of-the-art guidance.
- **R3 (Loose reading.):** `State of the art` = any reasonable technical measure documented at design time.

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `effective manner` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`effective` is inquiry-resistant but inherits Art. 32(1)(d) testing obligation. S2 because the compliance practice (test + document) is the same.

---
```



#### Resolution (per card 9):

**Recommended Variant:** R2 (Strict reading — ENISA/EDPB state-of-the-art.) — chosen because Art. 25(1) PbD anchors on ENISA/EDPB-published state-of-the-art guidance for KMS design.

**Stakeholder Impact:** CTO (KMS choice), DPO (PbD sign-off), Lead Dev (KMS configuration)

**Risk if not resolved:** MEDIUM — Art. 25(1) PbD hard obligation; KMS choice affects Art. 32(1)(a)

#### Card #10: GDPR-CP15 — Art. 32(1) (Security measures (open list))

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
- **Type:** security
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.3/D-01.3.json:ambiguity_cards`
- **Case impact:** KMS choice (AWS KMS vs HSM) affects Art. 32(1)(a) pseudonymisation/encryption and CRA Annex I §1.2 attack-surface.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
```

- **Type:** COORD
- **Severity:** S3
- **Ambiguous phrase:** `(a) AND (b) AND (c) AND (d)` (verbatim from corpus)

- **R1 (Industry standard (BCP/DRP best practice).):** `Timely` = RTO defined per processing activity (objective measure).
- **R2 (EDPB Guidelines 7/2019 (generic).):** `Timely` = as-soon-as-practicable for the specific incident.



#### Resolution (per card 10):

**Recommended Variant:** R2 (EDPB Guidelines 7/2019 (generic).) — chosen because Art. 32(1) KMS-related security measures follow EDPB 'timely' guidance per specific incident.

**Stakeholder Impact:** CTO + DPO (KMS-related measures), Customers (key-custody-protected subjects)

**Risk if not resolved:** HIGH — Art. 32 KMS is canonical security obligation

#### Card #11: GDPR-CP19 — Art. 34(1) (High-risk threshold)

- **Card variant:** GDPR-light
- **Berry anchor:** §3.3.1 (`high risk` polysemy — vs Art. 33 `risk` vs Art. 35 `high risk`).
- **Type:** breach communication
- **Obligated party:** CONTROLLER
- **Obligation type:** TRIGGERED (per high-risk breach)
- **Corpus path:** `domains/D-01_Data-Protection/D-01.3/D-01.3.json:ambiguity_cards`
- **Case impact:** KMS choice (AWS KMS vs HSM) affects Art. 32(1)(a) pseudonymisation/encryption and CRA Annex I §1.2 attack-surface.

**Instances:**

- **Type:** POLY+VAG
- **Severity:** S3
- **Ambiguous phrase:** `likely to result in a high risk` (verbatim from corpus)

- **R1 (EDPB Guidelines 9/2022.):** `High risk` = objectively elevated above ordinary processing risk.
- **R2 (CNIL guidance.):** `High risk` = severe impact on data subject's rights.



#### Resolution (per card 11):

**Recommended Variant:** R1 (EDPB Guidelines 9/2022 — 'high risk' = objectively elevated). — chosen because EDPB Guidelines 9/2022 establish the 'objectively elevated above ordinary processing risk' standard; 'likely to result in high risk' trigger for Art. 34 communication.

**Stakeholder Impact:** DPO (Art. 34 communication trigger evaluation), CTO (incident response), Customers (high-risk notification recipients)

**Risk if not resolved:** HIGH — Art. 34 high-risk trigger is a breach communication obligation; misreading creates Art. 34 non-compliance

#### Card #12: GDPR-CP20 — Art. 34(3) (Exceptions to data-subject communication)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`appropriate`, `unintelligible`, `disproportionate effort`), §5.4.7 (`OR (a) OR (b) OR (c)`).
- **Type:** breach communication exception
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-BREACH
- **Corpus path:** `domains/D-01_Data-Protection/D-01.3/D-01.3.json:ambiguity_cards`
- **Case impact:** KMS choice (AWS KMS vs HSM) affects Art. 32(1)(a) pseudonymisation/encryption and CRA Annex I §1.2 attack-surface.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `render the personal data unintelligible` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`Unintelligible` (typically achieved via encryption) inherits the encryption-key-management question. If keys are lost, data is unintelligible in one sense but inaccessible to legitimate users too.
```

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `disproportionate effort` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Same Berry-flagged phrase as Art. 14(5)(b). S3 because the exception triggers instead-of notification duty, materially distinct compliance outcome.

---


#### Resolution (per card 12):

**Recommended Variant:** R3 (Per Annex I — comprehensive unintelligibility + disproportionate effort test). — chosen because Art. 34(3) exception requires both unintelligibility (encryption sufficient) AND disproportionate effort test; R3 captures the conjunction.

**Stakeholder Impact:** DPO (exception evaluation), CTO (encryption efficacy proof), Customers (notification recipients)

**Risk if not resolved:** MEDIUM — Art. 34(3) exception is conditional; misapplication removes the notification obligation incorrectly

### Article 35 — Data protection impact assessment

#### Verbatim (with highlighting)

> Article 35
> Data protection impact assessment
>
> 1. Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data. A single assessment may address a set of similar processing operations that present similar high risks.

> 2. The controller shall seek the advice of the data protection officer, where designated, when carrying out a data protection impact assessment.

> 3. A data protection impact assessment referred to in paragraph 1 shall in particular be required in the case of:

> (a) a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person;

> (b) processing on a large scale of special categories of data referred to in Article 9(1), or of personal data relating to criminal convictions and offences referred to in Article 10; or

> (c) a systematic monitoring of a publicly accessible area on a large scale.

> 4. The supervisory authority shall establish and make public a list of the kind of processing operations which are subject to the requirement for a data protection impact assessment pursuant to paragraph 1. The supervisory authority shall communicate those lists to the Board referred to in Article 68.

> 5. The supervisory authority may also establish and make public a list of the kind of processing operations for which no data protection impact assessment is required.

> 6. Prior to the adoption of the lists referred to in paragraphs 4 and 5, the competent supervisory authority shall apply the consistency mechanism referred to in Article 63 where such lists involve processing activities which are related to the offering of goods or services to data subjects or to the monitoring of their behaviour in several Member States, or may substantially affect the free movement of personal data within the Union.

> 7. The assessment shall contain at least:

> (a) a systematic description of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller;

> (b) an assessment of the necessity and proportionality of the processing operations in relation to the purposes;

> (c) an assessment of the risks to the rights and freedoms of data subjects referred to in paragraph 1;

> (d) the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation taking into account the rights and legitimate interests of data subjects and other persons concerned.

> 8. Compliance with approved codes of conduct referred to in Article 40 by the relevant controllers or processors shall be taken into due account in assessing the impact of the processing operations performed by such controllers or processors, in particular for the purposes of a data protection impact assessment.

> 9. Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing, without prejudice to the protection of commercial or public interests or the security of processing operations.

> 10. Where processing pursuant to point (c) or (e) of Article 6(1) has a legal basis in Union law or in the law of the Member State to which the controller is subject, that law regulates the specific processing operation or set of operations in question, and a data protection impact assessment has already been carried out as part of a general impact assessment in the context of the adoption of that legal basis, paragraphs 1 to 7 shall not apply unless Member States deem it to be necessary to carry out such an assessment prior to processing activities.

> 11. Where necessary, the controller shall carry out a review to assess if processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations.

#### Clause breakdown
```


#### Card #13: CRA-CL02 — Art. 6(a) proviso (Installation/use conditions)

- **Card variant:** source-locus
- **Berry anchor:** §5.1 (`properly`).
- **Type:** —
- **Obligated party:** —
- **Obligation type:** —
- **Corpus path:** `domains/D-01_Data-Protection/D-01.3/D-01.3.json:ambiguity_cards`
- **Case impact:** KMS choice (AWS KMS vs HSM) affects Art. 32(1)(a) pseudonymisation/encryption and CRA Annex I §1.2 attack-surface.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `properly installed, maintained` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`properly` — what constitutes proper?

- R1: Per manufacturer instructions (Annex II §8).
- R2: Per industry standards.
- R3: Per a reasonable user's understanding.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per instructions | In-Directive: Annex II §8 `necessary measures during initial commissioning` |
| R2 | Per industry | None in OJ |
| R3 | Per reasonable user | None in OJ |

R1 is the literal reading. R2/R3 admit materially different compliance populations. S3.
```

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `intended purpose or under conditions which can reasonably be foreseen` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`intended purpose` (Art. 3(23)) OR `reasonably foreseeable` (Art. 3(24)) — alternative conditions.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Intended purpose OR foreseeable | In-Directive: literal `or` |
| R2 | Intended purpose ONLY | None in OJ |
| R3 | Foreseeable ONLY | None in OJ |

R1 is the literal reading. S3.
```

- **Type:** VAG
- **Severity:** S2
- **Ambiguous phrase:** `where applicable, the necessary security updates have been installed` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`necessary security updates` — which updates are necessary?

- R1: Critical security updates only.
- R2: All security updates.
- R3: Updates required by Annex I Part II §3 (effective and regular tests).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Critical | None in OJ |
| R2 | All | In-Directive: Annex I Part II §3 |
| R3 | Per Annex I | In-Directive: Annex I Part II §3 |

R2 is the literal reading. S2.
```

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `installed` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`installed` — software-only? Hardware? Firmware?

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Software | None in OJ |
| R2 | Hardware | None in OJ |
| R3 | Any | In-Directive: literal `installed` |

R3 is the literal reading. S2.
```




#### Resolution (per card 13):

**Recommended Variant:** R1 (Per manufacturer instructions — Annex II §8). — chosen because Annex II §8 supports R1 'per manufacturer instructions' as the in-Directive disambiguation.

**Stakeholder Impact:** CTO (KMS installation guidance), Lead Dev (documentation), Customers

**Risk if not resolved:** HIGH — CRA market-surveillance audit risk for KMS installation conditions

### D-01.4 — Data Integrity Mechanisms

- **Sub-domain Path:** `domains/D-01_Data-Protection/D-01.4/`
- **In-scope cards:** 3 of 11 (selected for top 20)

#### Card #14: GDPR-RT12 — Art. 16 (Rectification right)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`without undue delay`, `inaccurate`, `incomplete`).
- **Type:** data subject right (rectification)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-REQUEST
- **Corpus path:** `domains/D-01_Data-Protection/D-01.4/D-01.4.json:ambiguity_cards`
- **Case impact:** Backup integrity (STORE-02) must withstand ransomware — affects Art. 32(1)(b) CIA+R and CRA Annex I §2(2).

**Instances:**

- **Type:** POLY
- **Severity:** S3
- **Ambiguous phrase:** `supplementary statement` (verbatim from corpus)

- **R1 (EDPB Guidelines on Art. 16.):** Supplementary statement required only when factual dispute exists.
- **R2 (Strict reading.):** Supplementary statement required upon data-subject request, regardless of factual dispute.



#### Resolution (per card 14):

**Recommended Variant:** R2 (Strict reading — supplementary statement required upon request). — chosen because Art. 16 rectification right is broad; supplementary statement is part of the rectification, not contingent on factual dispute.

**Stakeholder Impact:** DPO (rectification handling), CTO (data integrity controls), Customers (rectification requesters)

**Risk if not resolved:** MEDIUM — Art. 16 is a hard right; supplementary statement incomplete creates Art. 16 gap

#### Card #15: GDPR-CP15 — Art. 32(1) (Security measures (open list))

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
- **Type:** security
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-01_Data-Protection/D-01.4/D-01.4.json:ambiguity_cards`
- **Case impact:** Backup integrity (STORE-02) must withstand ransomware — affects Art. 32(1)(b) CIA+R and CRA Annex I §2(2).

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
```

- **Type:** COORD
- **Severity:** S3
- **Ambiguous phrase:** `(a) AND (b) AND (c) AND (d)` (verbatim from corpus)

- **R1 (Industry standard (BCP/DRP best practice).):** `Timely` = RTO defined per processing activity (objective measure).
- **R2 (EDPB Guidelines 7/2019 (generic).):** `Timely` = as-soon-as-practicable for the specific incident.



#### Resolution (per card 15):

**Recommended Variant:** R2 (EDPB Guidelines 7/2019 — timely = as-soon-as-practicable). — chosen because Art. 32(1) backup-integrity controls align with EDPB 'timely' = as-soon-as-practicable per incident.

**Stakeholder Impact:** CTO + DPO (backup integrity controls), Customers (data integrity-protected subjects)

**Risk if not resolved:** HIGH — Art. 32 CIA+R is canonical; backup integrity is a primary control

#### Card #16: GDPR-CL23 — Art. 9(2)(g) (Substantial public interest)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
- **Type:** lawfulness base (special category)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-MEMBER-STATE-LAW
- **Corpus path:** `domains/D-01_Data-Protection/D-01.4/D-01.4.json:ambiguity_cards`
- **Case impact:** Backup integrity (STORE-02) must withstand ransomware — affects Art. 32(1)(b) CIA+R and CRA Annex I §2(2).

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `substantial public interest` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.

S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.

---
```




#### Resolution (per card 16):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because EDPB standard for 'substantial public interest' under Art. 9(2)(g) applies; backup integrity does not typically invoke special category.

**Stakeholder Impact:** CTO + DPO, Customers (rarely invoke special category for backup integrity)

**Risk if not resolved:** MEDIUM — Art. 9(2)(g) special category rarely applies to TinyTask (no special category data)

### D-02.1 — Vulnerability Identification

- **Sub-domain Path:** `domains/D-02_Vulnerability-Management/D-02.1/`
- **In-scope cards:** 4 of 13 (selected for top 20)

#### Card #17: GDPR-RT16 — Art. 21(1) (Objection grounds and overriding)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`compelling legitimate grounds`).
- **Type:** data subject right (object)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-OBJECTION
- **Corpus path:** `domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json:ambiguity_cards`
- **Case impact:** Vuln identification cadence (monthly/quarterly) is the practical expression of Art. 32(1)(d) testing.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `compelling legitimate grounds` (verbatim from corpus)

- **R1 (EDPB Guidelines on legitimate interests.):** `Compelling` = strictly necessary (lex specialis to legitimate interests).
- **R2 (Loose reading.):** `Compelling` = materially more weighty than legitimate interests.



#### Resolution (per card 17):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because Art. 21 + Art. 32(1)(d) testing obligation; EDPB standard for objection grounds + testing cadence.

**Stakeholder Impact:** CTO (vuln scan cadence), DPO (objection handling), Customers

**Risk if not resolved:** MEDIUM — Art. 32(1)(d) testing obligation + Art. 21 objections both apply

#### Card #18: GDPR-CP15 — Art. 32(1) (Security measures (open list))

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy).
- **Type:** security
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Corpus path:** `domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json:ambiguity_cards`
- **Case impact:** Vuln identification cadence (monthly/quarterly) is the practical expression of Art. 32(1)(d) testing.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `state of the art` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
```

- **Type:** COORD
- **Severity:** S3
- **Ambiguous phrase:** `(a) AND (b) AND (c) AND (d)` (verbatim from corpus)

- **R1 (Industry standard (BCP/DRP best practice).):** `Timely` = RTO defined per processing activity (objective measure).
- **R2 (EDPB Guidelines 7/2019 (generic).):** `Timely` = as-soon-as-practicable for the specific incident.



#### Resolution (per card 18):

**Recommended Variant:** R2 (EDPB Guidelines 7/2019 (generic).) — chosen because Art. 32(1)(d) vuln identification follows EDPB 'timely' guidance per specific incident.

**Stakeholder Impact:** CTO (vuln scan tooling), DPO (Art. 32 testing obligation)

**Risk if not resolved:** HIGH — Art. 32(1)(d) testing is canonical; vuln cadence is the practical expression

#### Card #19: GDPR-CL23 — Art. 9(2)(g) (Substantial public interest)

- **Card variant:** GDPR-light
- **Berry anchor:** §5.1 (`substantial public interest`, `proportionate`, `essence of the right to data protection`, `suitable and specific measures`).
- **Type:** lawfulness base (special category)
- **Obligated party:** CONTROLLER
- **Obligation type:** PER-MEMBER-STATE-LAW
- **Corpus path:** `domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json:ambiguity_cards`
- **Case impact:** Vuln identification cadence (monthly/quarterly) is the practical expression of Art. 32(1)(d) testing.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `substantial public interest` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.

S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.

---
```



#### Resolution (per card 19):

**Recommended Variant:** R2 (EDPB Guidelines on legitimate interests.) — chosen because EDPB standard for 'substantial public interest' under Art. 9(2)(g); vuln identification does not typically invoke special category.

**Stakeholder Impact:** CTO + DPO, Customers

**Risk if not resolved:** MEDIUM — Art. 9(2)(g) special category rarely applies to TinyTask

#### Card #20: CRA-CL06 — Art. 7(2)(a) (Classification criterion A)

- **Card variant:** source-locus
- **Berry anchor:** §3.3.1 (`primarily`).
- **Type:** —
- **Obligated party:** —
- **Obligation type:** —
- **Corpus path:** `domains/D-02_Vulnerability-Management/D-02.1/D-02.1.json:ambiguity_cards`
- **Case impact:** Vuln identification cadence (monthly/quarterly) is the practical expression of Art. 32(1)(d) testing.

**Instances:**

- **Type:** VAG
- **Severity:** S3
- **Ambiguous phrase:** `primarily performs functions critical to the cybersecurity` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Three modifiers (primarily + critical + cybersecurity). Three readings:

- R1: `primarily` = majority of functions.
- R2: `primarily` = main function (single dominant function).
- R3: `primarily` = principal (the function for which the product is sold).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Majority | None in OJ |
| R2 | Single dominant | None in OJ |
| R3 | Principal | None in OJ |

S3.
```

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `critical to the cybersecurity` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
`critical to the cybersecurity` — relative to what?

- R1: Critical to the cybersecurity of any product/network/service.
- R2: Critical to the cybersecurity of an entire class of products.
- R3: Critical to the cybersecurity of the user's operations.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Any product | In-Directive: literal `other products, networks or services` |
| R2 | Class of products | None in OJ |
| R3 | User's operations | None in OJ |

R1 is the literal reading. S2.
```

- **Type:** POLY
- **Severity:** S2
- **Ambiguous phrase:** `securing authentication and access, intrusion prevention and detection, end-point security or network protection` (verbatim from corpus)

- **Analysis (verbatim from corpus):**

```
Four examples (illustrative list). The reading:
- R1: These four are the only critical functions.
- R2: These four are illustrative; other functions can qualify.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Closed list | None in OJ |
| R2 | Open list | In-Directive: literal `including` |

R2 is the literal reading. S2.
```




#### Resolution (per card 20):

**Recommended Variant:** R3 (Open list — 'including' is illustrative). — chosen because Annex I literal 'including' supports R2/R3 open-list reading; CRA Art. 7(2)(a) classification criterion A is not closed-list.

**Stakeholder Impact:** CTO (CRA classification), Lead Dev (product security scope), Customers (product classification users)

**Risk if not resolved:** HIGH — CRA Art. 7(2)(a) classification drives conformity assessment procedure (default vs important/critical)

## §4 Recommended Disambiguation Order (top 5 by case impact)

> Ranking heuristic: severity (S3 first) × cross-subdomain propagation × TinyTask-specific risk exposure (Art. 33 notification, Art. 32 security, Art. 30 records).

| Rank | Card | Article | Why critical for TinyTask |
|------|------|---------|---------------------------|
| 1 | GDPR-RT16 (D-01.1) | Art. 21(1) | Art. 21 objection grounds trigger controller-side balancing test; EDPB Guidelines are the only authoritative reading available. |
| 2 | GDPR-CP02 (D-01.1) | Art. 25(1) | Art. 25 PbD is the design-phase obligation that propagates to all product features; "state of the art" must be anchored to a documented reading. |
| 3 | GDPR-CP15 (D-01.1) | Art. 32(1) | Art. 32 is the canonical security obligation — all Art. 32(1)(a–d) sub-clauses inherit "state of the art" and "appropriate" ambiguity. Drives baseline technical measures for SaaS. |
| 4 | CRA-CL02 (D-01.1) | Art. 6(a) proviso | CRA Art. 6(a) proviso governs market access — "properly installed/maintained" must be defensible against CRA market-surveillance audits. |
| 5 | GDPR-RT16 (D-01.2) | Art. 21(1) | Art. 21 objection grounds trigger controller-side balancing test; EDPB Guidelines are the only authoritative reading available. |

## §5 Provenance & Cross-references

- **Source corpus:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (38 sub-domain folders, 48 manifests, 38 sidecars, 623 articles)
- **Sidecar location:** `D-XX.Y/D-XX.Y.json` — `ambiguity_cards[]` array
- **Manifests:** `D-XX.Y/D-XX.Y.manifest.json` (per-sub-domain) + `D-XX.manifest.json` (per-domain aggregate)
- **Verbatim regulation text:** `D-XX.Y/articles/<REG>_Art_<N>.md` (623 files)
- **Data dictionary:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` (362 lines)
- **Card filter:** `card.regulation ∈ {GDPR, CRA}` — CRA and GDPR are the two regulations applicable to Case_01 (per `05_Regulatory_Applicability.md`)
- **Sub-domain filter:** 37 active per `04a_Architecture_DataInventory.md` Compliance Mapping table (D-08.3 explicitly INACTIVE)

## §6 Notes on Card Variants

Two card variants appear in the corpus:

- **`GDPR-light`** (most GDPR cards): variant readings are structured in `instances[].variant_readings[]` as `{id, reading, source}` triples.
- **`source-locus`** (most CRA cards): variant readings are embedded as Markdown tables inside `instances[].analysis_text`; `variant_readings[]` is empty.

Both variants are preserved verbatim in §3; readers should note that CRA cards require reading the `analysis_text` block to extract the R1/R2/R3 readings.

## §7 Gate Criteria (Fase de Especificação 3 readiness)

- [x] Ambiguity register methodology documented (§5, §6)
- [x] At least 1 example entry with full provenance (§3 — 20 entries with full provenance)
- [x] All open ambiguities catalogued by sub-domain (§2 — 37 sub-domains)
- [x] Top 5 disambiguation priorities ranked (§4)
- [ ] All ambiguities resolved (deferred to Fase de Especificação 3 with human review)