---
ficha_id: PROM-P3A-04
title: 'Propose the security constraint an objective awaits'
phase_step: 'Phase 3 Part 1 · Proposal (wave 4)'
pattern: 'one structured call per active sub-domain'
version: 1.0.1
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md wave 4'
  - 'ADR-005 (iterative risk-acceptance rounds: propose → Accept/Reject/Adjust per item)'
  - 'ADR-007 D2/D4 (published anchor sets; the five-verdict vocabulary)'
---

# PROM-P3A-04 — Propose the security constraint an objective awaits

## Metadata

| Field | Content |
|---|---|
| Role | Security & privacy requirements engineer |
| Mission | For each objective whose verdict asked for a proposal, draft ONE constraint in EARS form with a binary fit criterion, the risk it addresses, and a chain inside the objective's published anchor set |
| Inputs | The sub-domain's objectives with their verdicts and published anchors, the frozen V0 card pool, the recorded verdict table |
| Output | One markdown section per target objective, in the order given |
| Human gate | **G-P3-A** — every proposal is a proposal until the round judges it per item |
| Failure mode | A constraint that pre-bakes implementation detail (parameters, vendors, protocols — R13 anti-pattern 11), a fit criterion that cannot be judged true/false, an anchor the objective does not publish |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `PROPOSAL_PACK.md` | The objectives with published anchors, the V0 pool, and the verdicts recorded for this sub-domain |
| 2 | `VERDICTS.md` context | The carve-outs say where each leg went — the proposal answers the legs marked *pending proposal* |

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
### PO-D-XX.Y-NNN

**Constraint (EARS):** Where the system stores personal data at rest, the system shall encrypt the stored data with mechanisms consistent with current industry standards.
**Fit criterion:** A stored dump of the data store is unreadable without the key; a record with no key reference fails review.
**Risk addressed:** Personal data at rest readable by an attacker with disk access.
**Chain anchors:** `PR.AC-1`, `PR.DS-1`
**Proposed carrier:** `R1.1` — or `new` if no existing card can carry it
```

Exactly one section per target objective, in the order given.

## Rules the output must obey

- **High-level control abstraction (R13).** Regulation → article → control
  framework → high-level control objective. No operational parameters
  ("30-minute timeout", "128-bit entropy"), no vendor, no protocol.
- **Anchors come only from the objective's published set.** The objective block
  lists them; naming another is a fabrication.
- **EARS with a system (or organizational) subject and `shall`.** One behaviour
  per constraint.
- **The fit criterion is binary.** A reviewer can judge it true or false from
  evidence; no vague adjectives without a verifiable reading.
- **Propose for the legs the verdict carved out** — not a rewrite of the whole
  objective.

## Self-checks (L2)

- One section per target objective, in order, id as the heading.
- Every constraint contains `shall` and names its subject.
- Every fit criterion is judgeable true/false.
- No anchor outside the objective's published set.
- No technology, vendor, or parameter values.

## Human gate

Every proposal is judged per item in the round: Accept, Reject (explicit risk
acceptance, recorded), or Adjust. Nothing here closes anything.

## Failure handling

One repair round on structure (missing section, missing field, non-EARS text,
foreign anchor).

## Normative source

Doc 08 wave 4 · ADR-005 · ADR-007 D2/D4 · the measured first `p3a_map` run
(52 organizational verdicts whose discharges name functional legs — the pool
gap this stage fills).

## Changelog

- 1.0.1 — added the R5 neutrality block with the ADR-009 D5 prohibited→mandatory mapping. EARS constraints were specifying the mechanism rather than the property

## Prompt body

> You are given one sub-domain's objectives, their recorded verdicts, the
> published anchor sets, and the frozen V0 card pool. For each objective whose
> recorded action asks for a proposal, draft ONE security constraint: EARS form
> with a system subject and `shall`, a binary fit criterion, the risk it
> addresses, and chain anchors taken ONLY from that objective's published set.
> Name the card that could carry it (`R<n>.<m>` from the pool) or `new`.
> High-level control objective only — no parameters, vendors, or protocols.
