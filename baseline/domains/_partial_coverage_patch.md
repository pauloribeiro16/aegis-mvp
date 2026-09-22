# Partial-coverage patch ledger (M9 — M7 follow-up)

- Date: 2026-09-22
- Scope: strictly additive YAML `nist_csf:` array of the named Volere requirement cards, AND propagation of the same anchor to every Sub-SO card in the corpus that cites the same `source_SR` (so check H stays green).
- Idempotent: re-run = 0 changes.

## Primary patches (M7 audit findings)

| Sub | Reg | Req | Anchor added | Justification | File | Before | After |
|---|---|---|---|---|---|---|---|
| D-04.2 | DORA | 4.2.4 | `RS.MA-01` | Article basis cites 'incident' as a key action; RS.MA-01 is the CSF subcategory for incident-management-plan execution with third-party coordination, covering the BC arrangements dispatch dimension (Art. 11(2) + Art. 19(1) + Art. 19(3)). | `baseline/domains/D-04_Incident-Response/D-04.2/regs/DORA.md` | `nist_csf: [PR.IR-03, RC.RP-01, RS.MA-01]` | `nist_csf: [PR.IR-03, RC.RP-01, RS.MA-01]` |
| D-04.2 | NIS2 | 4.2.2 | `RS.MA-01` | Article basis cites 'incident' as a key action; RS.MA-01 covers incident management with third-party coordination per the Art. 6(8) six-action lifecycle. | `baseline/domains/D-04_Incident-Response/D-04.2/regs/NIS2.md` | `nist_csf: [RS.MA-01, RS.AN-03]` | `nist_csf: [RS.MA-01, RS.AN-03]` |
| D-07.1 | DORA | 7.1.4 | `PR.PS-02` | Article basis cites 'patch' as a key action; PR.PS-02 covers software maintenance commensurate with risk, operationalising Art. 9(4)(f) patch-and-update policies documented in the fit_criterion. | `baseline/domains/D-07_Secure-Development/D-07.1/regs/DORA.md` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` |

Total primary patches applied: **3**


## Residual line mappings (M10 completion — DORA re-anchor vs original corpus)

The DORA re-anchor replaced anchor-list/YAML lines that `verify_no_loss.py` compares against the original corpus. Machine-readable pair list: `baseline/MAPPINGS/_uniformization_changes.json` (`surface: dora_reanchor_m10`). Pairing:

| Sub | Old line (original corpus) | New line (current) |
|---|---|---|
| D-02.1 | `ID.RA-01, ID.RA-03, PR.PS-02, GV.OV-02.` | `ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, GV.OV-02, PR.PS-02.` |
| D-02.1 | `nist_csf: [ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, PR.PS-02, GV.OV-02]` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` |
| D-04.2 | `nist_csf: [RC.RP-01, RC.RP-04, PR.IR-04, PR.IR-03, PR.DS-11, RC.RP-03]` | `nist_csf: [PR.IR-03, RC.RP-01, RS.MA-01]` |
| D-04.4 | `nist_csf: [RC.RP-01, RC.RP-03, RC.RP-04, PR.IR-03, PR.IR-04, PR.DS-11]` | `nist_csf: [RC.RP-01, PR.IR-03, RS.MA-01]` |
| D-07.1 | `PR.PS-06.` | `ID.RA-01, ID.RA-03, PR.PS-02.` |
| D-07.1 | `nist_csf: [PR.PS-06]` | `nist_csf: [ID.RA-01, ID.RA-03, PR.PS-02]` |
| D-09.2 | `ID.RA-05 (primary), GV.RR-02.` | `GV.RR-02, GV.RM-02, ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, GV.OV-02, ` |
| D-10.1 | `DE.CM-01 (primary), DE.CM-09, PR.PS-04, DE.AE-02, ID.RA-01, ID.RA-03.` | `DE.CM-01, DE.CM-09, PR.PS-04, DE.AE-02, RS.MA-01, ID.RA-01, ID.RA-03, ` |

Also fixed: glued `RS.MA-01` token on the D-04.2 anchors header line.
