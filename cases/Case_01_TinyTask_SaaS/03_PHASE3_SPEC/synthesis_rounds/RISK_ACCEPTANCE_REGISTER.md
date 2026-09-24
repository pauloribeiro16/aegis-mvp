# Phase 3 — Risk Acceptance Register (TinyTask SaaS)

> **Purpose:** Authoritative record of the iterative synthesis rounds (ADR-005): every proposed security/privacy constraint, the risk it addresses, and the client's per-item verdict. No `Doc01`/`Doc02` version evolves before the register reaches convergence.
> **Normative basis:** `../PHASE3_PROCESS_AND_METHODOLOGY.md` Step 3 (Iterative Synthesis & Risk-Acceptance Rounds); ADR-005.
> **Template:** `templates/phase3_risk_acceptance_register.md`.

---

## Round rules

1. **One proposal per item**: an EARS constraint carrying (a) the risk it addresses, (b) its altitude level (L2 verifiable constraint / L3 mechanism category — guidelines §2.5), (c) its full regulatory chain (`regulation article → Phase 2 rule → PRIN-ENG → candidate anchor`), (d) a Volere Fit Criterion and Verification Method.
2. **Client verdict per item**, recorded verbatim per round: **Accept** · **Reject** · **Adjust** (wording, level, or scope → re-proposed next round).
3. **A rejection is an explicit risk acceptance**: the item stays registered as `Risk-accepted (client decision)` — it is never silently dropped.
4. **Convergence**: a round with no new rejections, or an explicit client decision to close the baseline. Only then do the deliverable versions evolve; control selection (Step 4) follows.
5. Functional refinement-pass items (Step 5b, taxonomy D1–D4) enter the cycle as round proposals like any other.

---

## Rounds — Proposals

_(no round proposals yet — future revisions enter here)_

| Item | Proposal (EARS constraint) | Risk addressed | Level | Regulatory chain | Fit criterion / Verification | Client verdict | Notes / adjustment |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

---

## Cumulative status

| Item | Final status | Rounds involved | Decision trace |
|---|---|---|---|
|  |  |  |  |

**Status legend:**
- **Accepted** — client accepted the proposal as formulated.
- **Risk-accepted (client decision)** — client rejected the proposal and formally accepts the associated risk; the risk and its owner stay on record.
- **Adjusted** — client required changes; the adjusted formulation re-enters the next round; final status recorded on acceptance.

---

## Convergence record

| Round | Date | New items | Rejections | Outcome |
|---|---|---|---|---|
| 0 (pre-cycle consolidation) | 2026-09-23/24 | 15 absorbed constraints (`RN9`–`RN26`) + 3 cross-cutting (`RN17`, `RN18`, `RN24`) | — | Grandfathered: V1 (19 cards) approved under the one-shot process before ADR-005; treated as the accepted starting position. |
