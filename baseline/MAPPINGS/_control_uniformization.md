# Control anchor uniformization ledger (dashboard correspondence)

- Date: 2026-09-22
- Reference: `baseline/MAPPINGS/sr_control_mappings/<REG>.json` — extracted from the
  per-regulation dashboards in `methodology_compact/00_METHODOLOGY/00_VISUALISATIONS/`
  (read-only; `Case_*`, `data`, `UNIFIED`, `tests` ignored).
- Policy: for the same sr_id / clause, the dashboard control set wins (user decision).
  Baseline-only SRs are left untouched and listed below. Ids unresolvable against
  `baseline/CONTROLS` are never propagated. Primary anchor lists that are not in
  strict machine-readable format are kept verbatim and flagged below.
  Italic gloss lines after a list are contextual prose (kept verbatim); when a gloss
  names a token outside the uniformized set it is listed as informational.
- Axes: PF 1.1 only where the GDPR dashboard publishes it; AI RMF only where the
  AI_Act dashboard publishes it (no overlay supplementation).
- Machine-readable change list: `_uniformization_changes.json` (consumed by
  `scripts/verify_no_loss.py` as documented transformations).

| Kind | Count |
|---|---|
| axis_yaml_added | 44 |
| csf_replaced | 92 |
| gloss_stray_tokens | 29 |
| manifest | 10 |
| registry_csv | 1 |

## CSF set replacements (baseline -> dashboard)

| File | SR | Old | New |
|---|---|---|---|
| `baseline/domains/D-01_Data-Protection/D-01.1/regs/DORA.md` | SR-DORA-001 | `nist_csf: [PR.DS-01]` | `nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08]` |
| `baseline/domains/D-01_Data-Protection/D-01.2/regs/DORA.md` | SR-DORA-001 | `nist_csf: [PR.DS-02]` | `nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08]` |
| `baseline/domains/D-01_Data-Protection/D-01.3/regs/DORA.md` | SR-DORA-002 | `nist_csf: [PR.AA-03, PR.AA-04, PR.DS-01, GV.RM-04]` | `nist_csf: [PR.AA-03, PR.AA-04]` |
| `baseline/domains/D-01_Data-Protection/D-01.3/regs/GDPR.md` | SR-GDPR-003 | `nist_csf: [PR.DS-01, PR.IR-03]` | `nist_csf: [PR.DS-01]` |
| `baseline/domains/D-01_Data-Protection/D-01.4/regs/DORA.md` | SR-DORA-001 | `nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05]` | `nist_csf: [PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08]` |
| `baseline/domains/D-01_Data-Protection/D-01.4/regs/GDPR.md` | SR-GDPR-005 | `nist_csf: [PR.DS-01, PR.DS-10, ID.AM-08]` | `nist_csf: [PR.DS-01, ID.AM-08]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/AI_Act.md` | SR-AIACT-001 | `nist_csf: [ID.RA-03, ID.RA-04, ID.RA-06, PR.PS-06, RS.MI-01, RS.MA-03, GV.RM-01, GV.RM-06]` | `nist_csf: [GV.RM-01, GV.RM-06]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/CRA.md` | SR-CRA-006 | `nist_csf: [ID.RA-01, ID.AM-02, PR.PS-02]` | `nist_csf: [ID.RA-01, PR.PS-02]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/DORA.md` | SR-DORA-004 | `nist_csf: [ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, PR.PS-02, GV.OV-02]` | `nist_csf: [ID.RA-01, ID.RA-03]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/GDPR.md` | SR-GDPR-007 | `nist_csf: [ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02]` | `nist_csf: [ID.RA-01, PR.PS-02]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.2/regs/CRA.md` | SR-CRA-010 | `nist_csf: [PR.PS-02, PR.IR-03, ID.RA-01, ID.RA-06, PR.PS-01, GV.OV-02]` | `nist_csf: [PR.PS-02, ID.RA-06]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.2/regs/DORA.md` | SR-DORA-006 | `nist_csf: [PR.PS-01, PR.PS-02, PR.IR-01, PR.IR-03, ID.RA-01]` | `nist_csf: [PR.PS-01, PR.IR-01, PR.IR-03]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.3/regs/CRA.md` | SR-CRA-019 | `nist_csf: [GV.PO-01, GV.SC-04, RS.CO-03]` | `nist_csf: [GV.PO-01, GV.SC-04]` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.4/regs/DORA.md` | SR-DORA-008 | `nist_csf: [GV.OV-02, ID.RA-01, ID.RA-04, PR.PS-06]` | `nist_csf: [GV.OV-02, ID.RA-01, PR.PS-06]` |
| `baseline/domains/D-03_Access-Control/D-03.1/regs/CRA.md` | SR-CRA-023 | `nist_csf: [PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09]` | `nist_csf: [PR.AA-01, ID.AM-01]` |
| `baseline/domains/D-03_Access-Control/D-03.1/regs/GDPR.md` | SR-GDPR-009 | `nist_csf: [PR.AA-02, PR.AA-03, ID.AM-08]` | `nist_csf: [PR.AA-03, PR.AA-02]` |
| `baseline/domains/D-03_Access-Control/D-03.1/regs/NIS2.md` | SR-NIS2-003 | `nist_csf: [PR.AA-01, PR.AA-05, PR.AT-02]` | `nist_csf: [PR.AA-01, PR.AA-05]` |
| `baseline/domains/D-03_Access-Control/D-03.2/regs/CRA.md` | SR-CRA-023 | `nist_csf: [PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09]` | `nist_csf: [PR.AA-01, ID.AM-01]` |
| `baseline/domains/D-03_Access-Control/D-03.2/regs/GDPR.md` | SR-GDPR-011 | `nist_csf: [PR.AA-05, PR.AA-06, PR.AT-02]` | `nist_csf: [PR.AA-05, PR.AA-06]` |
| `baseline/domains/D-03_Access-Control/D-03.2/regs/NIS2.md` | SR-NIS2-006 | `nist_csf: [PR.AA-03, PR.AA-05, PR.DS-02, PR.IR-03]` | `nist_csf: [PR.AA-03, PR.AA-05]` |
| `baseline/domains/D-03_Access-Control/D-03.3/regs/CRA.md` | SR-CRA-024 | `nist_csf: [PR.AA-01, PR.AA-05, PR.AA-06, PR.PS-04, ID.AM-01, DE.CM-09]` | `nist_csf: [PR.AA-05, PR.AA-06, DE.CM-09]` |
| `baseline/domains/D-03_Access-Control/D-03.3/regs/DORA.md` | SR-DORA-010 | `nist_csf: [PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06]` | `nist_csf: [PR.AA-05, PR.AA-06]` |
| `baseline/domains/D-03_Access-Control/D-03.3/regs/GDPR.md` | SR-GDPR-011 | `nist_csf: [PR.AA-05, PR.AA-06, PR.AT-02]` | `nist_csf: [PR.AA-05, PR.AA-06]` |
| `baseline/domains/D-03_Access-Control/D-03.3/regs/NIS2.md` | SR-NIS2-003 | `nist_csf: [PR.AA-01, PR.AA-05, ID.AM-01, ID.AM-02]` | `nist_csf: [PR.AA-01, PR.AA-05]` |
| `baseline/domains/D-03_Access-Control/D-03.4/regs/CRA.md` | SR-CRA-025 | `nist_csf: [PR.PS-01, ID.AM-08, GV.SC-03]` | `nist_csf: [PR.PS-01, ID.AM-08]` |
| `baseline/domains/D-03_Access-Control/D-03.4/regs/GDPR.md` | SR-GDPR-013 | `nist_csf: [PR.PS-01, ID.AM-08, GV.PO-01]` | `nist_csf: [PR.PS-01, ID.AM-08]` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/CRA.md` | SR-CRA-027 | `nist_csf: [DE.CM-09, PR.PS-04, RS.MA-02]` | `nist_csf: [PR.PS-04, DE.AE-08]` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/DORA.md` | SR-DORA-011 | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, RS.MA-01, RS.MA-02, RS.MA-03]` | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02]` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/GDPR.md` | SR-GDPR-014 | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, PR.PS-04, RS.MA-02]` | `nist_csf: [DE.CM-01, DE.CM-09, RS.MA-02]` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/NIS2.md` | SR-NIS2-008 | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, PR.PS-04, RS.MA-01]` | `nist_csf: [RS.MA-01, RS.AN-03]` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/CRA.md` | SR-CRA-043 | `nist_csf: [PR.IR-03, PR.IR-04, DE.CM-09]` | `nist_csf: [PR.IR-03, ID.AM-08]` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/DORA.md` | SR-DORA-013 | `nist_csf: [RC.RP-01, RC.RP-04, PR.IR-04, PR.IR-03, PR.DS-11, RC.RP-03]` | `nist_csf: [RC.RP-01, PR.IR-03]` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/GDPR.md` | SR-GDPR-015 | `nist_csf: [RS.MI-01, RS.MI-02, PR.DS-01, ID.AM-08, PR.IR-04, RC.RP-04]` | `nist_csf: [RS.MI-01, RS.MI-02, PR.DS-01]` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/NIS2.md` | SR-NIS2-008 | `nist_csf: [RS.MI-01, RS.MI-02, PR.IR-03, PR.IR-04, RC.RP-01]` | `nist_csf: [RS.MA-01, RS.AN-03]` |
| `baseline/domains/D-04_Incident-Response/D-04.3/regs/CRA.md` | SR-CRA-029 | `nist_csf: [RS.MA-02, RS.CO-02, RS.AN-03, RS.AN-07]` | `nist_csf: [RS.MA-02, RS.CO-02]` |
| `baseline/domains/D-04_Incident-Response/D-04.3/regs/DORA.md` | SR-DORA-017 | `nist_csf: [RS.CO-02, RS.MA-04, RS.MA-03]` | `nist_csf: [RS.CO-02, RS.MA-04]` |
| `baseline/domains/D-04_Incident-Response/D-04.3/regs/NIS2.md` | SR-NIS2-010 | `nist_csf: [RS.MA-04, RS.MA-02, RS.MA-03]` | `nist_csf: [RS.MA-04, RS.MA-02]` |
| `baseline/domains/D-04_Incident-Response/D-04.4/regs/DORA.md` | SR-DORA-013 | `nist_csf: [RC.RP-01, RC.RP-03, RC.RP-04, PR.IR-03, PR.IR-04, PR.DS-11]` | `nist_csf: [RC.RP-01, PR.IR-03]` |
| `baseline/domains/D-05_Data-Lifecycle/D-05.1/regs/AI_Act.md` | SR-AIACT-003 | `nist_csf: [ID.AM-03, ID.AM-08, PR.PS-06, PR.DS-01, GV.OC-03]` | `nist_csf: [ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04]` |
| `baseline/domains/D-05_Data-Lifecycle/D-05.1/regs/GDPR.md` | SR-GDPR-025 | `nist_csf: [ID.AM-08, ID.AM-03, GV.OC-03, GV.PO-01]` | `nist_csf: [ID.AM-08, ID.AM-03]` |
| `baseline/domains/D-05_Data-Lifecycle/D-05.2/regs/CRA.md` | SR-CRA-016 | `nist_csf: [PR.PS-02, GV.OV-02, GV.OC-04]` | `nist_csf: [PR.PS-02, GV.OV-02]` |
| `baseline/domains/D-05_Data-Lifecycle/D-05.3/regs/GDPR.md` | SR-GDPR-030 | `nist_csf: [PR.DS-10, ID.AM-08, GV.SC-04]` | `nist_csf: [PR.DS-10, ID.AM-08]` |
| `baseline/domains/D-06_Supply-Chain/D-06.1/regs/DORA.md` | SR-DORA-019 | `nist_csf: [GV.SC-01, GV.SC-02, GV.SC-03, ID.AM-04]` | `nist_csf: [GV.SC-02, ID.AM-04]` |
| `baseline/domains/D-06_Supply-Chain/D-06.1/regs/GDPR.md` | SR-GDPR-033 | `nist_csf: [GV.SC-02, GV.SC-03, ID.AM-04]` | `nist_csf: [GV.SC-02, GV.SC-03]` |
| `baseline/domains/D-06_Supply-Chain/D-06.1/regs/NIS2.md` | SR-NIS2-020 | `nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02]` | `nist_csf: [GV.SC-02, GV.SC-03]` |
| `baseline/domains/D-06_Supply-Chain/D-06.2/regs/CRA.md` | SR-CRA-008 | `nist_csf: [ID.AM-02, GV.SC-02, GV.SC-03]` | `nist_csf: [ID.AM-02, GV.SC-02]` |
| `baseline/domains/D-06_Supply-Chain/D-06.3/regs/CRA.md` | SR-CRA-051 | `nist_csf: [GV.SC-02, GV.SC-04, RS.MI-01, RS.MA-04]` | `nist_csf: [GV.SC-04, RS.MI-02]` |
| `baseline/domains/D-06_Supply-Chain/D-06.3/regs/DORA.md` | SR-DORA-019 | `nist_csf: [GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, DE.CM-06]` | `nist_csf: [GV.SC-02, ID.AM-04]` |
| `baseline/domains/D-06_Supply-Chain/D-06.3/regs/GDPR.md` | SR-GDPR-034 | `nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, GV.OC-03, ID.AM-08]` | `nist_csf: [GV.SC-03]` |
| `baseline/domains/D-06_Supply-Chain/D-06.3/regs/NIS2.md` | SR-NIS2-020 | `nist_csf: [GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02, PR.PS-06]` | `nist_csf: [GV.SC-02, GV.SC-03]` |
| `baseline/domains/D-06_Supply-Chain/D-06.4/regs/CRA.md` | SR-CRA-059 | `nist_csf: [GV.RR-02, GV.SC-03, GV.SC-04, GV.OC-03, GV.SC-02]` | `nist_csf: [GV.RR-02, GV.SC-03]` |
| `baseline/domains/D-06_Supply-Chain/D-06.4/regs/NIS2.md` | SR-NIS2-018 | `nist_csf: [RS.MA-04, GV.SC-05, GV.SC-02, GV.SC-03, ID.AM-04, ID.RA-02]` | `nist_csf: [RS.MA-04, GV.SC-05]` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/AI_Act.md` | SR-AIACT-014 | `nist_csf: [PR.PS-06, ID.RA-01]` | `nist_csf: [PR.PS-06, PR.IR-03, ID.RA-04]` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/CRA.md` | SR-CRA-064 | `nist_csf: [PR.PS-06, PR.PS-01]` | `nist_csf: [PR.PS-06, GV.PO-02]` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/DORA.md` | SR-DORA-004 | `nist_csf: [PR.PS-06]` | `nist_csf: [ID.RA-01, ID.RA-03]` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/NIS2.md` | SR-NIS2-026 | `nist_csf: [PR.PS-06, PR.PS-02]` | `nist_csf: [PR.PS-06, GV.SC-02]` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/AI_Act.md` | SR-AIACT-016 | `nist_csf: [PR.PS-06, ID.RA-01]` | `nist_csf: [ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03]` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/CRA.md` | SR-CRA-067 | `nist_csf: [PR.PS-06, PR.PS-02]` | `nist_csf: [PR.PS-01, PR.PS-02]` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/DORA.md` | SR-DORA-023 | `nist_csf: [PR.PS-06]` | `nist_csf: [PR.PS-01, PR.PS-02, PR.PS-06]` |
| `baseline/domains/D-07_Secure-Development/D-07.3/regs/CRA.md` | SR-CRA-009 | `nist_csf: [PR.PS-06, PR.PS-02]` | `nist_csf: [ID.AM-02, GV.SC-03]` |
| `baseline/domains/D-07_Secure-Development/D-07.4/regs/CRA.md` | SR-CRA-069 | `nist_csf: [GV.OV-01, GV.PO-02, PR.PS-02, GV.SC-04, GV.OV-02, ID.IM-04]` | `nist_csf: [GV.OV-01, GV.PO-02]` |
| `baseline/domains/D-08_Human-Factors/D-08.2/regs/AI_Act.md` | SR-AIACT-013 | `nist_csf: [PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04, GV.RR-01]` | `nist_csf: [PR.AT-02, PR.AT-01, GV.RR-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/AI_Act.md` | SR-AIACT-010 | `nist_csf: [GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04, GV.OC-03, GV.OC-04]` | `nist_csf: [GV.PO-01, GV.OC-03, GV.OC-04]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/CRA.md` | SR-CRA-072 | `nist_csf: [GV.PO-01, GV.PO-02, GV.SC-01, GV.SC-04, GV.OC-03]` | `nist_csf: [GV.PO-01, GV.SC-01]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/DORA.md` | SR-DORA-026 | `nist_csf: [GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.OC-03, GV.OC-04, GV.RM-05]` | `nist_csf: [GV.RR-01, GV.RR-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/GDPR.md` | SR-GDPR-043 | `nist_csf: [GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.RR-03, GV.OV-03]` | `nist_csf: [GV.PO-01, GV.PO-02, GV.RM-04]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/NIS2.md` | SR-NIS2-032 | `nist_csf: [GV.PO-01, GV.RR-02, GV.OV-01, GV.RM-05]` | `nist_csf: [GV.RR-02, GV.PO-01]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/AI_Act.md` | SR-AIACT-001 | `nist_csf: [ID.RA-05, GV.RM-04]` | `nist_csf: [GV.RM-01, GV.RM-06]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/CRA.md` | SR-CRA-064 | `nist_csf: [ID.RA-05, GV.SC-07]` | `nist_csf: [PR.PS-06, GV.PO-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/DORA.md` | SR-DORA-028 | `nist_csf: [ID.RA-05, GV.RR-02]` | `nist_csf: [GV.RR-02, GV.RM-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/GDPR.md` | SR-GDPR-045 | `nist_csf: [ID.RA-04, ID.RA-05]` | `nist_csf: [ID.RA-01, ID.RA-05, ID.RA-06]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/NIS2.md` | SR-NIS2-035 | `nist_csf: [ID.RA-05, GV.OV-01]` | `nist_csf: [ID.RA-05, GV.PO-01]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/CRA.md` | SR-CRA-087 | `nist_csf: [ID.AM-01, ID.AM-02]` | `nist_csf: [GV.PO-02, ID.AM-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/DORA.md` | SR-DORA-029 | `nist_csf: [ID.AM-01, ID.AM-02, ID.AM-05]` | `nist_csf: [ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-05]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/NIS2.md` | SR-NIS2-005 | `nist_csf: [PR.PS-01, ID.AM-01, ID.AM-02]` | `nist_csf: [ID.AM-01, ID.AM-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/AI_Act.md` | SR-AIACT-008 | `nist_csf: [ID.AM-08, GV.PO-01]` | `nist_csf: [PR.PS-04, GV.PO-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/CRA.md` | SR-CRA-085 | `nist_csf: [ID.AM-08, ID.RA-05]` | `nist_csf: [GV.PO-02, GV.OC-03]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/DORA.md` | SR-DORA-031 | `nist_csf: [ID.AM-08, GV.PO-01]` | `nist_csf: [GV.PO-01, ID.AM-08, GV.OC-03]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/GDPR.md` | SR-GDPR-048 | `nist_csf: [ID.AM-08, GV.PO-02]` | `nist_csf: [ID.AM-03, GV.PO-02]` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/NIS2.md` | SR-NIS2-043 | `nist_csf: [ID.AM-08]` | `nist_csf: [GV.SC-04, GV.OC-03]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/CRA.md` | SR-CRA-100 | `nist_csf: [DE.CM-01, DE.CM-09, ID.IM-04]` | `nist_csf: [DE.CM-09, DE.CM-01]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/DORA.md` | SR-DORA-030 | `nist_csf: [DE.CM-01, DE.CM-09, PR.PS-04, DE.AE-02, ID.RA-01, ID.RA-03]` | `nist_csf: [DE.CM-01, DE.CM-09, PR.PS-04]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/GDPR.md` | SR-GDPR-019 | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04]` | `nist_csf: [RS.CO-03, RS.MA-04]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/NIS2.md` | SR-NIS2-009 | `nist_csf: [DE.CM-01, DE.CM-09, DE.AE-02, ID.IM-04]` | `nist_csf: [DE.CM-01, DE.CM-09]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/AI_Act.md` | SR-AIACT-007 | `nist_csf: [PR.PS-04, DE.CM-09, DE.AE-03, RC.RP-03]` | `nist_csf: [PR.PS-04, DE.CM-09, DE.AE-03]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/CRA.md` | SR-CRA-088 | `nist_csf: [PR.DS-11, ID.AM-08, GV.PO-02, ID.RA-04]` | `nist_csf: [GV.OC-03, ID.RA-04, GV.SC-04]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/GDPR.md` | SR-GDPR-044 | `nist_csf: [PR.DS-11, PR.PS-04, DE.CM-01, GV.PO-02]` | `nist_csf: [GV.PO-02, GV.OV-03]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/AI_Act.md` | SR-AIACT-003 | `nist_csf: [ID.IM-03, ID.RA-05, PR.PS-04, GV.OV-03]` | `nist_csf: [ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/CRA.md` | SR-CRA-101 | `nist_csf: [ID.IM-03, ID.RA-05, DE.AE-02, GV.OV-03]` | `nist_csf: [ID.RA-04, GV.OV-01]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/DORA.md` | SR-DORA-008 | `nist_csf: [ID.IM-03, ID.RA-05, DE.AE-02, GV.OV-03, PR.PS-04]` | `nist_csf: [GV.OV-02, ID.RA-01, PR.PS-06]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/GDPR.md` | SR-GDPR-019 | `nist_csf: [ID.IM-03, ID.RA-05, DE.AE-02, GV.OV-03]` | `nist_csf: [RS.CO-03, RS.MA-04]` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/NIS2.md` | SR-NIS2-037 | `nist_csf: [ID.IM-03, ID.RA-05, GV.OV-03, DE.AE-02]` | `nist_csf: [GV.PO-01, ID.IM-01, GV.OV-03]` |

## Review flags

- none

## Informational: gloss lines mentioning tokens outside the uniformized set

- `D-01.1/regs/CRA.md @L37` — gloss mentions outside uniformized set: ['PR.DS-02']
- `D-01.1/regs/DORA.md @L38` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-01.2/regs/DORA.md @L37` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-01.4/regs/DORA.md @L38` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-04.1/regs/GDPR.md @L40` — gloss mentions outside uniformized set: ['DE.AE-02', 'PR.PS-04']
- `D-04.1/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['DE.AE-02', 'PR.PS-04']
- `D-04.2/regs/CRA.md @L38` — gloss mentions outside uniformized set: ['DE.CM-09', 'PR.IR-04']
- `D-04.2/regs/GDPR.md @L40` — gloss mentions outside uniformized set: ['ID.AM-08', 'PR.IR-04']
- `D-04.2/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['PR.IR-03']
- `D-04.3/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['RS.AN-03', 'RS.AN-07']
- `D-04.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['RS.MA-03']
- `D-07.1/regs/AI_Act.md @L40` — gloss mentions outside uniformized set: ['ID.RA-01']
- `D-07.1/regs/CRA.md @L39` — gloss mentions outside uniformized set: ['PR.PS-01']
- `D-07.1/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['PR.PS-02']
- `D-07.2/regs/AI_Act.md @L42` — gloss mentions outside uniformized set: ['ID.RA-01']
- `D-07.2/regs/CRA.md @L42` — gloss mentions outside uniformized set: ['PR.PS-06']
- `D-07.3/regs/CRA.md @L39` — gloss mentions outside uniformized set: ['PR.PS-02', 'PR.PS-06']
- `D-08.1/regs/NIS2.md @L40` — gloss mentions outside uniformized set: ['ID.RA-01', 'PR.PS-02']
- `D-09.1/regs/GDPR.md @L36` — gloss mentions outside uniformized set: ['GV.RR-02']
- `D-09.1/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['GV.OV-01']
- `D-09.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['PR.PS-01']
- `D-10.1/regs/GDPR.md @L36` — gloss mentions outside uniformized set: ['DE.AE-02', 'DE.CM-01', 'DE.CM-09', 'ID.IM-04']
- `D-10.2/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['ID.AM-08', 'PR.DS-11']
- `D-10.2/regs/GDPR.md @L36` — gloss mentions outside uniformized set: ['DE.CM-01', 'PR.DS-11']
- `D-10.3/regs/AI_Act.md @L36` — gloss mentions outside uniformized set: ['GV.OV-03', 'ID.IM-03', 'ID.RA-05', 'PR.PS-04']
- `D-10.3/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05']
- `D-10.3/regs/DORA.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05', 'PR.PS-04']
- `D-10.3/regs/GDPR.md @L36` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05']
- `D-10.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'ID.IM-03', 'ID.RA-05']

