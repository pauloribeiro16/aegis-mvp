---
ficha_id: PROM-P3A-03
title: 'Draft one V0 card: 7-row requirement, PUC row, Level-1 use case'
phase_step: 'Phase 3 Part 1 · V0 baseline (wave 2) — per card'
pattern: 'one structured call per card'
version: 1.0.1
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md wave 2'
  - 'templates/phase3_functional_spec_guidelines.md §3.3 (card anatomy), §Cockburn (use cases)'
  - 'cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/v0_functional_baseline/ (the golden)'
---

# PROM-P3A-03 — Draft one V0 card

## Metadata

| Field | Content |
|---|---|
| Role | Product requirements analyst |
| Mission | Write the full V0 card for one inventory entry: the 7-row requirement card, its Product Use Case row, and its Level-1 fully-dressed use case |
| Inputs | The proposed inventory (for neighbour awareness) and the company fact sheet |
| Output | One markdown block with three sections: Card, PUC, Use case |
| Human gate | The acceptance round (G-P3-A) |
| Failure mode | Micro-UI procedural steps in the scenario, security content in a V0 card, technology leakage, passive nominalizations |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `INVENTORY.md` | The proposed surface — this card's neighbours |
| 2 | `FACT_SHEET.yaml` | The company context (R6) |

## Technology neutrality (R5) — write the second column

Specifications name **what must hold**, never **what implements it**. Naming a
protocol, algorithm, database engine or vendor in a requirement is a defect the
gate rejects, and the repair round will not tell you what to write instead. So
use the mapping: when the thought is the left-hand term, write the right-hand one.

| Do not write | Write |
|---|---|
| *Argon2id, PBKDF2, Bcrypt* | memory-hard adaptive cryptographic key derivation function |
| *HMAC-SHA256, HMAC* | keyed cryptographic message authentication code |
| *JWT, session cookies, bearer token* | cryptographically signed, time-bound session authentication token |
| *PostgreSQL, MySQL, SQLite, MongoDB* | Internal Application Database |
| *AWS S3, Google Cloud Storage, Azure Blob* | External Object Storage Service |
| *Stripe, PayPal, Adyen* | External Payment Gateway |
| *AES-256-GCM, RSA-4096* | authenticated high-assurance symmetric / asymmetric encryption |
| ***TLS 1.3, HTTPS, SSH*** | **authenticated and encrypted end-to-end communication channel** |
| *OAuth 2.0, OIDC, SAML* | federated identity and authorization assertion protocol |

The right-hand column is a control *objective*, not a mechanism. Do not soften it
into vagueness either — "secure communication" is non-conformance, because a fit
criterion cannot be written against it. Name the property, not the product.

## Output schema

```markdown
#### Card R1.1

| # | Row | Content |
|---|---|---|
| 1 | ID | R1.1 — Register and authenticate user accounts |
| 2 | Description | The system must allow … |
| 3 | Requirement Origin | Founders Business Case & User Onboarding Workflow |
| 4 | Interfaces | … |
| 5 | Dependencies | Stakeholders: …; Data Sources: …; Extraction Periodicity: on demand; Information Systems / Databases: ; Preceding Requirements: |
| 6 | Identified Problems | — |
| 7 | Priority | Must |

#### PUC

| PUC ID | Business Trigger | Primary Actor | System Operational Boundary | Deliverables & Outputs |
|---|---|---|---|---|
| PUC 1.1 | … | … | … | … |

#### Use case {U.C. 1.1}

**Traceability:** Requirement `R1.1` | PUC `1.1`
**Primary Actor:** …
**Preconditions:** …
**Trigger:** …
**Main Success Scenario:** 1. … 2. … 3. …
**Extensions:** 2a. …
**Success Guarantees:** …
**Minimal Guarantees:** …
```

## Rules the output must obey

- **The exact 7 rows, in order** (E1.1 Table 22 standard). `Identified Problems`
  is `—` in V0; `Preceding Requirements` stays empty unless a strict
  prerequisite exists.
- **Cockburn Sea-Level only.** The scenario stops at Level 1: actor–system
  exchanges, no button clicks, no field entries, no leaf use cases.
- **Zero security content.** No 2FA, no session termination, no hashing, no
  GDPR anonymization — the constraints arrive through the round.
- **Technology neutrality (R5).** Functional names only.
- **Origin is a business event or stakeholder**, never an internal module name.

## Self-checks (L2)

- The card has exactly the 7 rows; Priority is Must/Should/Could/Won't.
- The name uses the active verb form.
- The use case cites the card id in Traceability.
- The Main Success Scenario has ≥3 numbered actor/system steps.
- No vendor, database, framework, or protocol name anywhere.

## Human gate

The card is a proposal until the acceptance round judges it.

## Failure handling

One repair round on structure (missing row, missing field, non-verb name,
scenario too short, traceability mismatch).

## Normative source

Doc 08 wave 2 · R13 §3.3 · Cockburn *Writing Effective Use Cases* (Level 1).

## Changelog

- 1.0.1 — added the R5 neutrality block with the ADR-009 D5 prohibited→mandatory mapping. card descriptions were naming storage and transport products

## Prompt body

> You are given the proposed card inventory and the company fact sheet. Write
> the full V0 card for the assigned inventory entry: the 7-row requirement
> card, its PUC row, and its fully-dressed Level-1 use case. Business functions
> only; technology-neutral; active verbs; black-box actor–system scenario.
