# Round 2 Register — Iterative Risk-Acceptance Synthesis (SecureBorder eGate)

> **Round window:** opened 2026-09-29 · **Status: CONVERGED — 1/1 accept + 1 consistency fix, by client directive** ("coloca o v2" with the evolution plan; 2026-09-29).
> **Inputs:** [`SUFFICIENCY_ASSESSMENT.md`](SUFFICIENCY_ASSESSMENT.md) — security verdict and the MoSCoW posture of the AI-testing carrier.
> **Effect:** `R9.3` elevated to MUST; deliverables evolve to 3.0.0, stored in `../v2_security_privacy_synthesis/` (top-level docs kept as synced active copies); `part1_security_privacy/v0_functional_baseline/` and `part1_security_privacy/v1_security_privacy_synthesis/` remain untouched as history.

## §1 Proposal

| Item | Type | Change | Driver | Verdict |
|---|---|---|---|---|
| E1 | **D3 — priority re-evaluation** | `R9.3` Test AI systems adversarially and explain decisions: SHOULD → **MUST** (Table 6, card, Doc02 matrix) | `AI Act Art. 9(6)-(7)` → `SO-D-02.4-004` — testing of high-risk AI systems for consistent performance and in real-world conditions is a mandatory provider duty ("shall be tested"); the adversarial leg (`AI Act Art. 15(4)-(5)` → `SO-D-07.2-004`) resists attacks trying to manipulate the system. A SHOULD posture for the border-control verification AI is indefensible against the chain | **Accept** |
| E2 | Consistency fix | Doc02 §3.2 matrix row `R7.3`: SHOULD → MUST (Table 6 and the card already carry MUST; the matrix row was stale) | — | **Accept** |

## §2 Control Selection

No change — `R9.3`'s chain rows (`SO-D-02.4-004`, `SO-D-07.2-004`, `SO-D-10.3-004` with CSF ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04) are unaffected by the priority elevation.

## §3 Convergence & Effect

- **Convergence:** closed with the client's directive accepting the elevation; no rejections, no adjustments.
- **Effect:** `Doc01` Table 6 + `R9.3` card + `Doc02` §3.2 → MUST (Version History 3.0.0, `../v2_security_privacy_synthesis/`).
