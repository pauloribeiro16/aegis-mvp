---
ficha_id: PROM-P3A-01
title: 'Verdict the coverage matrix for one sub-domain'
phase_step: 'Phase 3 Part 1 · Coverage mapping'
pattern: 'one structured call per active sub-domain'
version: 1.1.1
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'ADR-007 D2/D4 (fulfillment semantics and the five-verdict vocabulary)'
  - 'ADR-008 D4 (routing by realization class)'
  - 'ADR-003 (realization class: PRODUCT vs PROCESS/CAPABILITY)'
  - 'cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/synthesis_rounds/OBJECTIVE_MAPPING.md'
---

# PROM-P3A-01 — Verdict the coverage matrix for one sub-domain

## Metadata

| Field | Content |
|---|---|
| Role | Regulatory compliance analyst |
| Mission | For each Phase 2 objective of this sub-domain, decide whether the product lane discharges it, partly discharges it, or does not discharge it at all — and say which legs go where |
| Inputs | The sub-domain's Phase 2 objectives with their published control-anchor sets, and the candidate functional requirement cards from the frozen V0 baseline |
| Output | A markdown table, one row per objective, in the order given |
| Human gate | **G-P3-A** — the round register; verdicts are entered per item afterwards |
| Failure mode | A verdict that is decoration rather than analysis: a carrier named with no leg identified, a discharge that restates the objective, or an anchor the objective does not publish |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `OBJECTIVE_MAPPING.skeleton.md` | The rows to fill — one block per objective, with the judgement columns empty |
| 2 | `V0_CARDS.md` | The candidate functional cards: id, name, description. **This is the whole carrier pool** |
| 3 | `VERDICTS.md` | The five verdicts and what each one means |

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
| Objective | Summary | Functional carrier | Skill | State | VC discharge | Action / Round |
|---|---|---|---|---|---|---|
| `PO-D-XX.Y-NNN` | one line, the objective in plain words | `R1.1`, `R2.2` — from the candidate pool, or `—` | `TB`/`AS`/`LP`/`DM`/`FS`/`LE`/`V`, or `—` | **one of the five verdicts, verbatim** | which legs are carried, which are carved out and where — or `—` only for a row that genuinely has nothing to say, which the gates reject | free text |
```

Exactly seven columns, one row per objective, in the order the objectives were
given. The `Objective` cell repeats the id and nothing else.

## What is not an organizational obligation

`No functional carrier (organizational)` means the duty is a PROCESS or
CAPABILITY obligation — a contract, a policy, a decision, a reporting duty. It
does **not** mean "no card mentions this".

A transversal concern — transport protection, data at rest, audit logging,
tenant isolation — is carried by a functional card **plus** a transversal
constraint that the constraint stage derives afterwards. At this stage that
constraint does not exist yet, so there is nothing to name. Verdict such a row
`Partially covered`, write the missing leg in the discharge as *"no card
carries it alone; requires a new transversal constraint"*, and put
`RN (a derivar)` in the carrier cell.

Routing it to `organizational` says the obligation is a process duty. When it
is not, that route is a carve-out of the wrong kind: the objective leaves the
product lane and nothing ever picks it up.

## The five verdicts

| Verdict | When |
|---|---|
| `Fully covered (anchored)` | Every leg of the objective is carried by named card(s), nothing is carved out, and each named card's constraints sit inside this objective's published anchor set |
| `Partially covered (functional leg + explicit carve-out)` | Some legs are carried. Every leg that is **not** carried is named in the discharge, with where it goes: the organizational lane, design guidance, or a pending proposal |
| `No functional carrier (organizational)` | The obligation is a PROCESS or CAPABILITY duty — a contract, a policy, a decision, a reporting duty. No software feature discharges it. Name the specific organizational obligation |
| `Design guidance` | The obligation constrains how a future design should behave, and is not yet a testable requirement |
| `N/A` | The obligation's addressee or context does not exist for this company. Give the reason |

Pick exactly one. A row that is neither fully carried nor wholly organizational is
`Partially covered` — that verdict exists precisely to stop a half-truth being
recorded as a full one.

## The discharge column

For any row that is not `N/A`, say in one paragraph:

1. which legs the named carrier(s) carry, and
2. which legs they do not, and where each of those goes.

Do not restate the objective. Do not claim a reconstruction against the Phase 2
Verification Criteria: those are template sentences that repeat the objective's own
name, so there is nothing object-specific to check against. The column records what
is carried and what is carved out — nothing more, and the verdict word says
`anchored` rather than `discharge-verified` for the same reason.

## Rules the output must obey

- **Carriers come only from the candidate pool.** A card id that is not in
  `V0_CARDS.md` is a fabrication and fails the stage.
- **Anchors come only from the objective's own published set.** Never name a
  control the objective did not publish. The objective block already lists them.
- **A `Fully covered` row needs a discharge.** "Fully covered" with an empty
  discharge is the failure this stage exists to prevent.
- **A `No functional carrier` row needs the obligation named.** "Organizational" on
  its own is a routing decision with no content and fails the stage.
- **A `N/A` row needs the reason.** Which addressee, or which context, is absent.
- **One row per objective, in the order given.** Reordering, merging, dropping or
  inventing a row is a parse failure, not a judgement.

## Self-checks (L2)

- Every objective in the input has exactly one row.
- Every carrier named appears in the candidate pool.
- Every verdict is one of the five words above, exactly.
- No row is `Fully covered` with an empty discharge.
- No row is `No functional carrier` with an empty discharge.
- No anchor is named that the objective's block did not list.

## Human gate

Verdicts are proposals until the round register carries a verdict per item. This
call produces the proposals; it does not close the round.

## Failure handling

One repair round on a structural defect — a missing row, an unknown carrier, a
verdict word outside the vocabulary — with a message naming only that defect. A
substantive disagreement with the objective is not a defect and is not repaired; it
is the round's business.

## Normative source

ADR-007 D2/D4 · ADR-008 D4 · ADR-003 · the hand-authored Case 01 coverage matrix,
which is the only one of the three cases carrying a discharge column.

## Changelog

- 1.1.1 — added the R5 neutrality block with the ADR-009 D5 prohibited→mandatory mapping. the discharge column is where technology vocabulary leaks (TLS, AES-256)

- 1.1.0 (2026-10-10) — added `RN (a derivar)` as a carrier value. The first cluster run routed 52 of 65 objectives to `organizational` and named none fully covered, because a transversal concern has no carrier until the constraint stage derives one, and the vocabulary had no value for "not derived yet". The enum is unchanged; only the carrier cell gained a value.

## Prompt body

> You are given the Phase 2 objectives of one sub-domain and the candidate
> functional requirement cards that may carry them. For each objective, choose
> exactly one of the five verdicts, name the carrying card or cards from the
> candidate pool, and write the discharge paragraph that says which legs are
> carried and which are carved out to where. Use only the control anchors the
> objective itself publishes. Emit one markdown table row per objective, in the
> order given, with exactly these columns:
>
> `Objective | Summary | Functional carrier | Skill | State | VC discharge | Action / Round`