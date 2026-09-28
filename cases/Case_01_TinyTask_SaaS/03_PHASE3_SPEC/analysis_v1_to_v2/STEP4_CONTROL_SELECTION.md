# Step 4 — Control Identification & Selection (post-convergence)

> **Ledger:** [`../synthesis_rounds/ROUND1_REGISTER.md`](../synthesis_rounds/ROUND1_REGISTER.md) §3 (authoritative per-constraint table with selection rationale).
> **Rules applied:** anchors copied only from pre-verified surfaces — the driver objective's published control set (Phase 2 `Doc01` final column) and the mapping store (`baseline/MAPPINGS/sr_control_mappings/<REG>.json`); PF 1.1 anchors accompany GDPR-derived obligations only (R2/R8); an out-of-set anchor would require explicit rationale + W4 admission (ADR-001) — none was needed.

## 1. Process

1. For each of the 13 accepted items, read the target objective's published control set.
2. Select the subset of published anchors matching the constraint's protective property (integrity → `PR.DS-01`/`PR.DS-10`; access enforcement → `PR.AA-05`/`PR.AA-06`; surface protection → `PR.PS-06`/`PR.PS-02`; defaults → `PR.PS-01`; monitoring → `DE.CM-01`/`DE.CM-09`; awareness → `PR.AT-01`; authentication → `PR.AA-01`/`PR.AA-02`/`PR.AA-03`).
3. For the GDPR-derived new constraint, pull the PF axis from the mapping store: `SR-GDPR-009` ("Proportionate identity verification for rights requests") publishes `nist_csf: PR.AA-03, PR.AA-02` and `nist_pf: PR.AC-P6, PR.AC-P3` → selected `PF PR.AC-P6`.
4. Record per-item rationale in the register (which control, from which surface, why best fit).

## 2. Resulting control surface (V2)

- **NIST CSF 2.0 — 18 distinct subcategories:** GV.OC-03 · ID.AM-03, ID.AM-08 · PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-10, PR.PS-01, PR.PS-02, PR.PS-06, PR.IR-01 · DE.CM-01, DE.CM-09.
- **NIST Privacy Framework — 8 anchors (GDPR-derived only):** CT.DP-P2, CT.DM-P1, CT.DM-P3, CM.AW-P2, CM.PO-P2, PR.DS-P1, PR.DS-P2, PR.AC-P6.
- **Integrity notes:** `SO-D-05.3-002`'s published set lists `PR.DS-10` twice (literal duplicate in Phase 2 `Doc01`); selections cite the unique value. RS/RC-function anchors sit on organizational-lane objectives and are intentionally not selected at product level (recoverability slice carried by RN2/RN5).
