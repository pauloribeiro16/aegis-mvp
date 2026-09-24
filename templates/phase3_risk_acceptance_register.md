# Phase 3 — Risk Acceptance Register (<Case Name>)

> **Purpose:** Authoritative record of the iterative synthesis rounds (ADR-005): every proposed security/privacy constraint, the risk it addresses, and the client's per-item verdict. No `Doc01`/`Doc02` version evolves before the register reaches convergence.
> **Normative basis:** `PHASE3_PROCESS_AND_METHODOLOGY.md` Step 3 (Iterative Synthesis & Risk-Acceptance Rounds); ADR-005.
> **Location:** one instance per case at `cases/<CASE>/03_PHASE3_SPEC/synthesis_rounds/RISK_ACCEPTANCE_REGISTER.md`.

---

## Round rules

1. **One proposal per item**: an EARS constraint carrying (a) the risk it addresses, (b) its altitude level (L2 verifiable constraint / L3 mechanism category — guidelines §2.5), (c) its full regulatory chain (`regulation article → Phase 2 rule → PRIN-ENG → candidate anchor`), (d) a Volere Fit Criterion and Verification Method.
2. **Client verdict per item**, recorded verbatim per round: **Accept** · **Reject** · **Adjust** (wording, level, or scope → re-proposed next round).
3. **A rejection is an explicit risk acceptance**: the item stays registered as `Risk-accepted (client decision)` — it is never silently dropped.
4. **Convergence**: a round with no new rejections, or an explicit client decision to close the baseline. Only then do the deliverable versions evolve; control selection (Step 4) follows.
5. Functional refinement-pass items (Step 5b, taxonomy D1–D4) enter the cycle as round proposals like any other.

---

## Round <N> — <date> — Proposal

| Item | Proposal (EARS constraint) | Risk addressed | Level | Regulatory chain | Fit criterion / Verification | Client verdict | Notes / adjustment |
|---|---|---|---|---|---|---|---|
| <RN-candidate or D-item> | <"The system shall …"> | <risk the constraint mitigates> | L2 | <Art. … → PO/SO-… → PRIN-ENG-…> | <fit criterion · TEST/INSPECT/…> | Accept / Reject / Adjust | <client wording> |

---

## Cumulative status

| Item | Final status | Rounds involved | Decision trace |
|---|---|---|---|
| <RN-candidate> | Accepted / Risk-accepted (client decision) / Adjusted → <final wording> | R1 … Rn | <e.g., "R1 Adjust (level L3→L2); R2 Accepted"> |

**Status legend:**
- **Accepted** — client accepted the proposal as formulated.
- **Risk-accepted (client decision)** — client rejected the proposal and formally accepts the associated risk; the risk and its owner stay on record.
- **Adjusted** — client required changes; the adjusted formulation re-enters the next round; final status recorded on acceptance.

---

## Convergence record

| Round | Date | New items | Rejections | Outcome |
|---|---|---|---|---|
| 1 | <date> | <n> | <n> | <e.g., "2 adjustments → re-proposed in R2"> |
| … | | | | **Baseline closed on round <N>** |
