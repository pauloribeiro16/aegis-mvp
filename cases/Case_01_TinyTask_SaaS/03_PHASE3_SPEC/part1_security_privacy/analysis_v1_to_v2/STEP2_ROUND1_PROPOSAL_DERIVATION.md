# Step 2 — Round 1 Proposal Derivation (ADJ-1…ADJ-9 + P-01…P-04)

> **Rule:** every proposal carries the EARS constraint, the risk it addresses, the altitude level (L2), a Volere fit criterion, an ISO 29148 verification method, and the full chain `regulation article → Phase 2 objective → PRIN-ENG → candidate anchor` (manual Step 3).

## 1. Re-anchor proposals (ADJ-1…ADJ-9) — chain corrections, no behavior change

Derived from the wrong-lane driver findings (STEP1 §2.1): the constraint text is already accepted and correct; only the cited Phase 2 objective (and therefore the anchor set) moves to the objective that actually owns the property.

| Item | Constraint(s) | From (organizational lane) | To (product owner of the property) | Rationale |
|---|---|---|---|---|
| ADJ-1 | RN9 | `SO-D-02.1-002` | `SO-D-03.2-002` | tenant isolation is enforced by control mechanisms (CRA 2(d)) |
| ADJ-2 | RN11 (+RN10/RN12 co-driver) | `SO-D-02.2-002` | `SO-D-03.1-002` | session/credential handling is verified identity management |
| ADJ-3 | RN12 | `SO-D-02.1-002` | `SO-D-03.3-002` | RBAC = authenticated & authorized access |
| ADJ-4 | RN13, RN17 | `SO-D-07.1-002` / `SO-D-02.1-002, SO-D-05.1-002` | `SO-D-07.2-002` | upload validation and throttling are attack-surface limitation |
| ADJ-5 | RN18 (+`SO-D-04.1-002` co-driver) | `SO-D-03.1-002` | `SO-D-10.1-002` | audit logging = the product records & monitors activity |
| ADJ-6 | RN14 | `SO-D-07.1-002` (umbrella) | `SO-D-07.2-002` | content neutralization = surface limitation, not the umbrella |
| ADJ-7 | RN15 | `SO-D-01.1-002, SO-D-08.1-002` | `SO-D-01.4-002` | billing invariants are integrity, not confidentiality |
| ADJ-8 | RN16 | `SO-D-05.1-002, SO-D-08.1-002` | `SO-D-01.4-002` | webhook origin verification = message integrity |
| ADJ-9 | RN24 | `PO-D-01.2-001` (GDPR only) | + twin `SO-D-01.2-002` (CRA) | the case has CRA active; twin symmetry |

## 2. New-constraint proposals (P-01…P-04) — from the four uncovered product-lane objectives

| Item | Objective | Proposed constraint (L2, EARS) | Chain | Risk addressed |
|---|---|---|---|---|
| P-01 | `SO-D-03.1-001` (GDPR Art. 12(6)+11(2)) | If a data-subject request to export or erase personal data is submitted, the system shall verify the requester's identity before executing the request → `RN27`, MUST | → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6 | rights executed by an unauthorized third party |
| P-02 | `SO-D-03.4-002` (CRA 2(b)+(c)) | When a new shared artifact is created, the system shall initialize it with the most restrictive supported configuration, resettable by an authorized user → `RN28`, MUST | → `PRIN-ENG-04` → CSF PR.PS-01 | artifacts born open |
| P-03 | `SO-D-05.3-002` (CRA 2(m)) | Owner deletes a workspace with permanent erasure of all content and settings, account preserved → **D1** `R8.3` + `PUC 8.3` + `{U.C. 8.3}`, `RN30`; RN21 co-driver | → `PRIN-ENG-07` → CSF PR.DS-10, PR.DS-02 | abandoned workspaces retain data indefinitely |
| P-04 | `SO-D-08.1-002` (CRA Annex II §8) | Secure-use instructions covering commissioning and lifetime measures, for users and administrators → `RN29`, SHOULD | → CSF PR.AT-01 | insecure product use |

Formulation discipline: all new constraints stay at L2 (technology-neutral control objectives — no mechanisms, no parameters); fit criteria are binary and verifiable (`TEST`/`INSPECT`); the regulatory driver is carried as data in the chain, never as an ID prefix.
