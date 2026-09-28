# Step 5 — Absorption and V2 Evolution (Doc01/Doc02 4.0.0)

> **Applied change classes:** chain realignment (data update on absorbed constraints — no functional change), new absorbed constraints, one **D1** derived requirement. `v0_functional_baseline/` and `v1_security_privacy_synthesis/` untouched.

## 1. What entered the deliverables

| Change | Class | Where |
|---|---|---|
| 11 constraint chains re-anchored (ADJ-1…ADJ-9: `RN9`, `RN10`, `RN11`, `RN12`, `RN13`, `RN14`, `RN15`, `RN16`, `RN17`, `RN18`, `RN24`) with anchor sets realigned to each new driver's published set | constraint-data realignment | `Doc01` §2.2 constraint rows + Table 7 type cells |
| `RN27` Requester Identity Verification for Rights Exercise (MUST) | new absorbed constraint | `R8.1`, `R8.2` cards; `{U.C. 8.1}` step 2 + ext 2b; `{U.C. 8.2}` step 5 + ext 5a |
| `RN28` Secure-by-Default Configuration with User Reset (MUST) | new absorbed constraint | `R2.1`, `R3.1` cards; `{U.C. 2.1}` step 3; `{U.C. 3.1}` step 3 + ext 1c |
| `RN29` Secure-Use Instructions (SHOULD) | new Table 7 row | `Doc01` Table 7 (documentation surface, `INSPECT`) |
| `RN30` Workspace Permanent Removal (MUST) + RN21 co-driver + RN18 audit | **D1** derived requirement | new card `R8.3`, `PUC 8.3`, `{U.C. 8.3}` (fully dressed, Sea-Level) |

## 2. Version ladder

- `Doc01`/`Doc02` Version History **4.0.0** (2026-09-28): Round 1 synthesis row (register reference, counts 20/20/20).
- Folder architecture: `v2_security_privacy_synthesis/` holds the approved 4.0.0 pair + README (same structure as v0/v1); the top-level `Doc01`/`Doc02` are synced active copies. Ladder in `../analysis_v0_to_v1/V0_V1_V2_ANALYSIS_TABLES.md` updated (V2 row).

## 3. Matrix synchronization (post-convergence)

- `OBJECTIVE_MAPPING.md`: 14 → **26 covered** (re-drives and new carriers folded in), states updated per row, totals recomputed (26 / 31 / 2 / 3 = 62).
- `PRINCIPLE_MAPPING.md`: pending rows → `Bound (RN27/RN28/RN30)`; §2 gains the `R8.3` rows; totals 0 pending, 20/20 requirements realizing ≥1 principle.
- `UC_OBJECTIVE_CORRESPONDENCE.md`: pending markers resolved, 3 grid rows added (`SO-D-03.1-001`, `SO-D-03.4-002`, `SO-D-05.3-002`), `{U.C. 8.3}` card added, totals 20/20 cards.

## 4. Verification

- Phase 3 Quality Checklist (§6) re-run: all items green; `python scripts/doc_lint.py --strict` → 0 findings.
- Sufficiency assessed: [`../synthesis_rounds/SUFFICIENCY_ASSESSMENT.md`](../synthesis_rounds/SUFFICIENCY_ASSESSMENT.md) — Part 1 Exit Gate GREEN.
