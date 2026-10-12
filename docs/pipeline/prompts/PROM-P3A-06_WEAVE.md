---
ficha_id: PROM-P3A-06
title: 'Weave the accepted security constraints into one card use case'
phase_step: 'Phase 3 Part 1 · Weave (wave 6)'
pattern: 'one structured call per card carrying accepted constraints'
version: 1.0.1
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md wave 6'
  - 'templates/phase3_functional_spec_guidelines.md (Cockburn extensions; precondition discipline)'
---

# PROM-P3A-06 — Weave the accepted constraints into one card

## Metadata

| Field | Content |
|---|---|
| Role | Requirements engineer |
| Mission | For one card whose use case must absorb the round-accepted security constraints, write the security preconditions and the exception extensions those constraints impose |
| Inputs | The card as generated (with its use case) and the accepted constraints routed to it |
| Output | One markdown block: the card id plus three bold fields |
| Human gate | The exit gate (G1–G6) evaluates the woven deliverables; the round already judged the constraints |
| Failure mode | Re-deriving the constraint instead of absorbing it; turning a precondition into implementation detail; touching cards that have no accepted constraints |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `CARD.json` | The card, its PUC and its use case as generated in V0 |
| 2 | `ACCEPTED_CONSTRAINTS.md` | The constraints the round accepted and routed to this card |

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

**Preconditions:** The user session is authenticated; stored credentials are encrypted at rest per <accepted constraint>.
**Extensions:** 2a. Stored-data integrity check fails: the system refuses the operation and records the refusal.
**Constraints absorbed:** <objective-id> — <one line on how the use case now discharges it>
```

## Rules the output must obey

- **Absorb, do not re-derive.** The constraints are already accepted; the weave
  places them as preconditions/extensions, it does not restate or weaken them.
- **Cockburn discipline.** Preconditions are states true before the scenario
  starts; extensions are numbered `<step><letter>` and stay at Level 1.
- **Technology neutrality (R5).** No vendors, protocols, or parameters.
- **Empty when nothing routes to the card** — say so; do not invent content.

## Self-checks (L2)

- The block starts with the card id and carries the three fields.
- Every accepted constraint routed to this card appears in Constraints absorbed.
- Extensions reference existing scenario steps.
- No technology vocabulary.

## Human gate

Weaving happens after the round converged; the exit gate evaluates the result.

## Failure handling

One repair round on structure (missing field, wrong card id, missing constraint).

## Normative source

Doc 08 wave 6 · ADR-005 (accepted constraints are binding) · Cockburn.

## Changelog

- 1.0.1 — added the R5 neutrality block with the ADR-009 D5 prohibited→mandatory mapping. extension text was quoting mechanism from the constraint it absorbs

## Prompt body

> You are given one V0 card (with its use case) and the security constraints
> the acceptance round routed to it. Write the security preconditions and the
> numbered exception extensions those constraints impose on this use case, and
> list which constraint each absorbs. Absorb the constraints as they are — no
> re-derivation, no technology, no parameters. If nothing is routed to this
> card, return the block with empty additions.
