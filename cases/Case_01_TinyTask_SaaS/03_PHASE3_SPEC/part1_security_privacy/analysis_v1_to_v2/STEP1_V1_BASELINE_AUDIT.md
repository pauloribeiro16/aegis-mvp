# Step 1 — V1 Baseline Audit Against the Exhaustive Coverage Matrix

> **Input:** `../v1_security_privacy_synthesis/Doc01`/`Doc02` (3.0.x) · Phase 2 spine (62 objectives: 12 PO + 50 SO; 28 GDPR / 34 CRA rows) · `../synthesis_rounds/OBJECTIVE_MAPPING.md` · `../synthesis_rounds/PRINCIPLE_MAPPING.md`

## 1. What the exhaustive mapping found in V1

Juxtaposing every Phase 2 objective and all 7 principles against the V1 functional model produced the pre-round state (Round 0, consolidated 2026-09-23/24):

| Verdict | Count | Notes |
|---|---|---|
| Covered | 14 | incl. 1 transversal umbrella (`SO-D-07.1-002`) |
| Partial → re-drive needed | 8 rows / 9 items | constraint real but driven by the wrong objective |
| New constraint needed | 4 | gaps with no carrier (`SO-D-03.1-001`, `SO-D-03.4-002`, `SO-D-05.3-002`, `SO-D-08.1-002`) |
| No functional carrier | 31 | organizational/process lane — recorded decisions (ADR-002) |
| Design guidance | 2 | D-01.3 key/custody separation (design-time) |
| N/A | 3 | distribution chain, series production, integration information |
| **Total** | **62** | none silent |

## 2. Defects the audit surfaced

1. **Wrong-lane drivers:** 9 constraints (`RN9`–`RN18`, `RN24`) cited organizational/dev-process objectives (e.g. `SO-D-02.1-002` vulnerability-testing process, `SO-D-02.2-002` update distribution) as derivation drivers for product properties — the property belonged to a different (product-security) objective.
2. **Phantom drivers (executed directly, Round 0):** `PO-D-06.1-001`, `PO-D-06.2-001`, `PO-D-03.1-001` do not exist in Case_01 Phase 2; citations were recalibrated to the real objectives (`PO-D-05.1-001`, `PO-D-05.2-001`, `PO-D-05.3-001`, `PO-D-05.4-001`, `PO-D-09.4-001`) without a client decision needed (citation correction, not behavior change). Recorded in V1 Version History 3.0.2.
3. **Anchor mismatches:** chain anchors not belonging to the cited objective's published control set (e.g. `RN9` citing `PR.PS-02, PR.PS-01, ID.RA-01` on `SO-D-02.1-002`, whose published set carries different IDs).
4. **Uncovered product-lane objectives:** identity verification for rights requests, secure-by-default configuration, workspace permanent removal, secure-use instructions — no V1 carrier at all.
5. **Skills:** analysis-lens attribution present in the mappings after Round 0 (TB/AS/LP/FS/V/DM/LE), completing the 7/7 lens coverage.

## 3. Output

The audited state feeds Step 2: the 9 wrong-lane drivers became re-anchor proposals (ADJ-1…ADJ-9); the 4 uncovered objectives became new-constraint proposals (P-01…P-04).
