---
ficha_id: PROM-P3A-02
title: 'Propose the functional card inventory for the product surface'
phase_step: 'Phase 3 Part 1 · V0 baseline (wave 2) — inventory'
pattern: 'one structured call for the whole surface'
version: 1.0.1
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md wave 2'
  - 'templates/phase3_functional_spec_guidelines.md §3.3 (card filling rules), §7 (anti-patterns)'
---

# PROM-P3A-02 — Propose the functional card inventory

## Metadata

| Field | Content |
|---|---|
| Role | Product requirements analyst |
| Mission | Propose the smallest set of functional requirement cards that covers the product surface this company's Phase 2 objectives imply — business functions only, zero security content |
| Inputs | The company fact sheet and the Phase 2 operational objectives deliverable |
| Output | A markdown table, one row per proposed card |
| Human gate | None for the inventory itself; the cards it spawns pass the acceptance round (G-P3-A) |
| Failure mode | The pre-baked security trap (2FA, hashing, GDPR anonymization inside functional cards — R13 anti-pattern 1) and the clam-level decomposition trap (micro-UI cards) |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `FACT_SHEET.yaml` | The company: size, products, data, infrastructure — the surface has to fit THIS company (R6) |
| 2 | `PHASE2_OBJECTIVES.md` | The operational objectives the product will be measured against |

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
| Card | Name | Business basis |
|---|---|---|
| `R1.1` | Register and authenticate user accounts | Customer accounts are the intake's core entity |
```

Card ids `R<n>.<m>`, grouped by package `R<n>`. One row per card.

## Rules the output must obey

- **Business functions only.** No security or privacy mechanism belongs in a V0
  card — the security constraints arrive later, through the acceptance round.
- **Company scale (R13).** An 8-person micro-SaaS does not get enterprise SSO
  federation or oversized features.
- **Active verb names (R13).** `Manage user accounts`, never `User account
  management`.
- **Every card has a business basis in the intake.** A card the fact sheet
  cannot ground is invented (R6).

## Self-checks (L2)

- Every card name starts with an active verb.
- No card mentions security mechanisms, vendors, or technologies (R5).
- Every card's business basis cites something the fact sheet or the intake states.
- The set covers the product surface the objectives imply — no orphan business line.

## Human gate

The inventory is a proposal; the acceptance round judges the cards.

## Failure handling

One repair round on structure (id format, empty cell, non-verb name). Coverage
disagreements are the round's business.

## Normative source

Doc 08 wave 2 · R13 §3.3/§7 · R6.

## Changelog

- 1.0.1 — added the R5 neutrality block with the ADR-009 D5 prohibited→mandatory mapping. inventory names were restating the platform's own component list

## Prompt body

> You are given a company's fact sheet and its Phase 2 operational objectives.
> Propose the functional requirement cards that make up this product: one table
> row per card, ids `R<n>.<m>`, active-verb names, and a business basis grounded
> in the intake. Business functions only — no security mechanisms, no vendors,
> no technologies. Scale the repertoire to this company.
