---
ficha_id: PROM-P3A-07
title: 'Derive security constraints from one engineering principle'
phase_step: 'Phase 3 Part 1 · Principle-seeded synthesis'
pattern: 'one structured call per engineering principle'
version: 1.0.0
created: 2026-10-12
status: ACTIVE
normative_source:
  - 'ADR-007 D2/D4 (discharge semantics; the five-verdict vocabulary)'
  - 'ADR-001 (admitted good practice layer — principles are the entry)'
  - 'cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md §Engineering Principles (RN24 is a PRIN-ENG-01 binding)'
---

# PROM-P3A-07 — Derive security constraints from one engineering principle

## Metadata

| Field | Content |
|---|---|
| Role | Security architect |
| Mission | Decide whether this engineering principle demands a product-side control the company must build, and if so propose the constraint that implements it at the company's scale |
| Inputs | The principle, the objectives the matrix routed organizational (with published anchors), the existing functional cards, the fact sheet |
| Output | A markdown block per proposed constraint, keyed by the routed objective it primarily discharges |
| Human gate | **G-P3-A** — the proposals enter the same acceptance round as the objective-driven ones |
| Failure mode | Decorative binding: a constraint that restates the principle instead of implementing it, or technology vocabulary because the mechanism was named instead of the property |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `PRINCIPLE_PACK.md` | The principle, the routed objectives with their published anchor sets, the card catalogue, the fact sheet |

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
### `PO-D-XX.Y-NNN`

**Constraint (EARS):** Where <trigger>, the system shall <property at this company's scale>.
**Fit criterion:** <binary, deterministic pass/fail>
**Risk addressed:** <the concrete failure this prevents for THIS company>
**Chain anchors:** `PR.DS-02`, `GV.SC-04`
**Proposed carrier:** `new`
**Also carries:** `SO-D-XX.Y-NNN`, `PO-D-XX.Y-NNN`
```

`Also carries` may be empty. The block id must be one of the routed objectives
in the pack. If the principle adds nothing for these objectives, return an
empty fenced block.

## Rules the output must obey

- **The block id is a routed objective.** A principle constraint discharges
  obligations the matrix said had no carrier — it may not invent new scope.
- **Anchors come only from the published sets in the pack.** A control outside
  them does not exist for this case (R2).
- **Carrier is always `new`.** A principle constraint creates its card; it does
  not borrow one.
- **Proportionality is the job.** The fact sheet's scale decides the form: an
  8-person hosted SaaS gets managed-platform controls, not an enterprise PKI.
  A constraint the company cannot operate is decoration.
- **Implement, don't restate.** "The system shall enforce trust boundaries" is
  the principle again. "The system shall mediate every session through an
  authenticated channel that terminates inside the application boundary" is a
  constraint.

## Self-checks (L2)

- Every block id is one of the routed objectives in the pack.
- Every anchor appears in a published set in the pack.
- Every constraint contains SHALL and names a property, not a product.
- Every fit criterion is decidable by inspection or test.
- `Also carries` names only routed objectives.

## Human gate

The proposals join the same round as the objective-driven ones, keyed by their
primary objective. Accept/Reject/Adjust per item is the researcher's; a reject
is a recorded risk acceptance, never silent.

## Failure handling

One repair round on a structural defect — a missing field, a non-routed block
id, an anchor outside the published sets. An empty answer is not a defect: the
principle may have nothing to add, and the round never sees it.

## Normative source

ADR-007 D2/D4 · ADR-001 · the hand-written Case 01's principle table, where
RN24 (transport protection) is a PRIN-ENG-01 binding and RN18/RN26 are
PRIN-ENG-07 — the shape this ficha restores.

## Changelog

- 1.0.0 — first issue. The pipeline's PRINCIPLE_MAPPING stayed a skeleton
  because no pass derived constraints from principles; every objective a
  principle should have carried routed organizational for want of a carrier.

## Prompt body

> You are given one engineering principle, the objectives the coverage matrix
> routed to the organizational lane (each with its published control anchors),
> the functional cards that exist, and the company fact sheet. Decide whether
> this principle demands a product-side control the company must build at its
> own scale. If it does, emit one block per constraint in the Output schema,
> keyed by the routed objective the constraint primarily discharges, naming in
> `Also carries` the other routed objectives it discharges too. Anchors come
> only from the published sets on the page. If the principle adds nothing for
> these objectives, return an empty fenced block — that is a valid answer.
