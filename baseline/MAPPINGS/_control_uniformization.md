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
| ambiguity_anchors | 245 |
| axis_block_added | 39 |
| csf_replaced | 57 |
| gloss_stray_tokens | 29 |
| manifest | 10 |
| registry_csv | 1 |

## CSF set replacements (baseline -> dashboard)

| File | SR | Old | New |
|---|---|---|---|
| `baseline/domains/D-01_Data-Protection/D-01.1/regs/DORA.md` | SR-DORA-001 | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05.` | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.` |
| `baseline/domains/D-01_Data-Protection/D-01.2/regs/DORA.md` | SR-DORA-001 | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05.` | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.` |
| `baseline/domains/D-01_Data-Protection/D-01.4/regs/DORA.md` | SR-DORA-001 | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-05.` | `PR.DS-01, PR.DS-02, PR.DS-10, ID.AM-08.` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/DORA.md` | SR-DORA-004+SR-DORA-005 | `ID.RA-01, ID.RA-03, PR.PS-02, GV.OV-02.` | `ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-04, GV.OV-02.` |
| `baseline/domains/D-02_Vulnerability-Management/D-02.1/regs/GDPR.md` | SR-GDPR-007+SR-GDPR-008 | `ID.RA-01, PR.PS-02; ID.RA-05, ID.IM-02.` | `ID.RA-01, PR.PS-02, ID.RA-05, ID.IM-02.` |
| `baseline/domains/D-03_Access-Control/D-03.4/regs/GDPR.md` | SR-GDPR-013 | `PR.PS-01, ID.AM-08, GV.PO-01.` | `PR.PS-01, ID.AM-08.` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/CRA.md` | SR-CRA-027+SR-CRA-100 | `DE.CM-09, PR.PS-04, RS.MA-02.` | `PR.PS-04, DE.AE-08, DE.CM-09, DE.CM-01.` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/GDPR.md` | SR-GDPR-014 | `DE.AE-02, PR.PS-04, DE.CM-01.` | `DE.CM-01, DE.CM-09, RS.MA-02.` |
| `baseline/domains/D-04_Incident-Response/D-04.1/regs/NIS2.md` | SR-NIS2-008+SR-NIS2-009 | `DE.CM-01, DE.AE-02, PR.PS-04.` | `RS.MA-01, RS.AN-03, DE.CM-01, DE.CM-09.` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/CRA.md` | SR-CRA-043+SR-CRA-044 | `PR.IR-04, PR.IR-03, DE.CM-09.` | `PR.IR-03, ID.AM-08, GV.SC-04.` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/DORA.md` | SR-DORA-013+SR-DORA-014+SR-DORA-016 | `RC.RP-01, RC.RP-04, PR.IR-04, PR.IR-03.` | `RC.RP-01, PR.IR-03, RC.RP-04, PR.IR-04, RS.MA-01, RS.AN-03.` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/GDPR.md` | SR-GDPR-015 | `ID.AM-08, PR.IR-04, RC.RP-04.` | `RS.MI-01, RS.MI-02, PR.DS-01.` |
| `baseline/domains/D-04_Incident-Response/D-04.2/regs/NIS2.md` | SR-NIS2-008 | `PR.IR-03, PR.IR-04, RC.RP-01.` | `RS.MA-01, RS.AN-03.` |
| `baseline/domains/D-05_Data-Lifecycle/D-05.3/regs/CRA.md` | SR-CRA-048+SR-CRA-049 | `PR.DS-10, ID.AM-08 (+ PR.DS-02 for the second limb).` | `PR.DS-10, ID.AM-08, PR.DS-02.` |
| `baseline/domains/D-06_Supply-Chain/D-06.1/regs/GDPR.md` | SR-GDPR-033 | `GV.SC-02, GV.SC-04, ID.AM-04.` | `GV.SC-02, GV.SC-03.` |
| `baseline/domains/D-06_Supply-Chain/D-06.1/regs/NIS2.md` | SR-NIS2-020 | `GV.SC-02, ID.AM-04, GV.OC-03.` | `GV.SC-02, GV.SC-03.` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/AI_Act.md` | SR-AIACT-014 | `PR.PS-06, ID.RA-01.` | `PR.PS-06, PR.IR-03, ID.RA-04.` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/CRA.md` | SR-CRA-064 | `PR.PS-06, PR.PS-01.` | `PR.PS-06, GV.PO-02.` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/DORA.md` | SR-DORA-004 | `PR.PS-06.` | `ID.RA-01, ID.RA-03.` |
| `baseline/domains/D-07_Secure-Development/D-07.1/regs/NIS2.md` | SR-NIS2-026 | `PR.PS-06, PR.PS-02.` | `PR.PS-06, GV.SC-02.` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/AI_Act.md` | SR-AIACT-016 | `PR.PS-06, ID.RA-01.` | `ID.RA-04, PR.PS-06, RS.MI-01, RS.MA-03.` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/CRA.md` | SR-CRA-067 | `PR.PS-06, PR.PS-02.` | `PR.PS-01, PR.PS-02.` |
| `baseline/domains/D-07_Secure-Development/D-07.2/regs/DORA.md` | SR-DORA-023 | `PR.PS-06.` | `PR.PS-01, PR.PS-02, PR.PS-06.` |
| `baseline/domains/D-07_Secure-Development/D-07.3/regs/CRA.md` | SR-CRA-009 | `PR.PS-06, PR.PS-02.` | `ID.AM-02, GV.SC-03.` |
| `baseline/domains/D-08_Human-Factors/D-08.1/regs/CRA.md` | SR-CRA-071 | `PR.AT-01 (with UNMAPPED_CSF on the user-side).` | `PR.AT-01.` |
| `baseline/domains/D-08_Human-Factors/D-08.2/regs/AI_Act.md` | SR-AIACT-013+SR-AIACT-020 | `PR.AT-02, PR.AT-01, GV.RR-02.` | `PR.AT-02, PR.AT-01, GV.RR-02, GV.RR-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/AI_Act.md` | SR-AIACT-010+SR-AIACT-017 | `GV.PO-01 (primary), GV.PO-02.` | `GV.PO-01 (primary), GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/CRA.md` | SR-CRA-072+SR-CRA-075+SR-CRA-077 | `GV.PO-01 (primary), GV.PO-02.` | `GV.PO-01 (primary), GV.SC-01, GV.PO-02, GV.OC-03.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/DORA.md` | SR-DORA-026+SR-DORA-027+SR-DORA-028 | `GV.PO-01 (primary), GV.RR-02, GV.RM-04.` | `GV.RR-01, GV.RR-02, GV.PO-01 (primary), GV.OC-01, GV.RM-04, GV.RM-02.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/GDPR.md` | SR-GDPR-043+SR-GDPR-044 | `GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.RR-02.` | `GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.OV-03.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.1/regs/NIS2.md` | SR-NIS2-035+SR-NIS2-036+SR-NIS2-037 | `GV.PO-01 (primary), GV.OV-01, GV.PO-02.` | `ID.RA-05, GV.PO-01 (primary), PR.PS-01, ID.IM-01, GV.OV-03.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/AI_Act.md` | SR-AIACT-001+SR-AIACT-002 | `ID.RA-05 (primary), GV.RM-04.` | `GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, ID.RA-06.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/CRA.md` | SR-CRA-064+SR-CRA-065+SR-CRA-066+SR-CRA-079 | `ID.RA-05 (primary), GV.SC-07.` | `PR.PS-06, GV.PO-02, ID.RA-05 (primary), GV.OV-02.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/DORA.md` | SR-DORA-028+SR-DORA-004+SR-DORA-005 | `ID.RA-05 (primary), GV.RR-02.` | `GV.RR-02, GV.RM-02, ID.RA-01, ID.RA-03, ID.RA-05 (primary), ID.IM-04, GV.OV-02.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/GDPR.md` | SR-GDPR-045+SR-GDPR-046+SR-GDPR-047 | `ID.RA-05 (primary), ID.RA-04.` | `ID.RA-01, ID.RA-05 (primary), ID.RA-06, RS.AN-03, ID.IM-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.2/regs/NIS2.md` | SR-NIS2-035+SR-NIS2-039+SR-NIS2-040 | `ID.RA-05 (primary), GV.OV-01.` | `ID.RA-05 (primary), GV.PO-01, GV.RM-06, ID.RA-06, PR.IR-01.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/CRA.md` | SR-CRA-087+SR-CRA-088 | `ID.AM-01, ID.AM-02.` | `GV.PO-02, ID.AM-02, GV.OC-03, ID.RA-04, GV.SC-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/DORA.md` | SR-DORA-029 | `ID.AM-01, ID.AM-02, ID.AM-05.` | `ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-05.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.3/regs/NIS2.md` | SR-NIS2-005 | `PR.PS-01 (primary), ID.AM-01, ID.AM-02.` | `ID.AM-01, ID.AM-02.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/AI_Act.md` | SR-AIACT-008+SR-AIACT-009+SR-AIACT-010+SR-AIACT-017 | `ID.AM-08 (primary), ID.AM-08, GV.PO-01.` | `PR.PS-04, GV.PO-02, RC.RP-03, GV.PO-01, GV.OC-03, GV.OC-04, GV.RM-01, GV.RM-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/CRA.md` | SR-CRA-085+SR-CRA-087+SR-CRA-088+SR-CRA-078 | `ID.AM-08 (primary), ID.AM-08, ID.RA-05.` | `GV.PO-02, GV.OC-03, ID.AM-02, ID.RA-04, GV.SC-04.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/DORA.md` | SR-DORA-031 | `ID.AM-08 (primary), ID.AM-08, GV.PO-01.` | `GV.PO-01, ID.AM-08 (primary), GV.OC-03.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/GDPR.md` | SR-GDPR-048+SR-GDPR-050+SR-GDPR-065 | `ID.AM-08 (primary), ID.AM-08, GV.PO-02.` | `ID.AM-03, GV.PO-02, PR.PS-04, DE.AE-03, RS.AN-07, PR.AA-02.` |
| `baseline/domains/D-09_Governance-Documentation/D-09.4/regs/NIS2.md` | SR-NIS2-043 | `ID.AM-08 (primary), ID.AM-08.` | `GV.SC-04, GV.OC-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/AI_Act.md` | SR-AIACT-021+SR-AIACT-022 | `DE.CM-09 (primary), ID.IM-04, GV.OV-03.` | `DE.CM-09 (primary), ID.IM-04, GV.OV-03, RS.CO-02, RS.MA-04, RS.MA-03, RS.MA-01.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/CRA.md` | SR-CRA-100+SR-CRA-101 | `DE.CM-01 (primary), DE.CM-09, ID.IM-04.` | `DE.CM-09, DE.CM-01 (primary), ID.RA-04, GV.OV-01.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/DORA.md` | SR-DORA-030+SR-DORA-011+SR-DORA-012+SR-DORA-004 | `DE.CM-01 (primary), DE.CM-09, PR.PS-04, DE.AE-02, ID.RA-01, ID.RA-03.` | `DE.CM-01 (primary), DE.CM-09, PR.PS-04, DE.AE-02, RS.MA-01, ID.RA-01, ID.RA-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/GDPR.md` | SR-GDPR-019+SR-GDPR-020 | `DE.CM-01 (primary), DE.CM-09, DE.AE-02, ID.IM-04.` | `RS.CO-03, RS.MA-04, PR.DS-01, PR.IR-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.1/regs/NIS2.md` | SR-NIS2-009+SR-NIS2-014 | `DE.CM-01 (primary), DE.CM-09, DE.AE-02, ID.IM-04.` | `DE.CM-01 (primary), DE.CM-09, RS.MA-04, RS.MA-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/AI_Act.md` | SR-AIACT-007+SR-AIACT-008+SR-AIACT-009 | `PR.PS-04 (primary), DE.CM-09, DE.AE-03, RC.RP-03, PR.PS-04.` | `PR.PS-04 (primary), DE.CM-09, DE.AE-03, GV.PO-02, RC.RP-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/CRA.md` | SR-CRA-088+SR-CRA-080+SR-CRA-069+SR-CRA-070+SR-CRA-102 | `PR.DS-11 (primary), ID.AM-08, GV.PO-02, ID.RA-04.` | `GV.OC-03, ID.RA-04, GV.SC-04, ID.RA-05, GV.OV-01, GV.PO-02, PR.PS-02.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.2/regs/GDPR.md` | SR-GDPR-044+SR-GDPR-048+SR-GDPR-050 | `PR.DS-11 (primary), PR.PS-04, DE.CM-01, GV.PO-02.` | `GV.PO-02, GV.OV-03, ID.AM-03, PR.PS-04, DE.AE-03, RS.AN-07.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/AI_Act.md` | SR-AIACT-003+SR-AIACT-014 | `ID.IM-03 (primary), ID.RA-05, PR.PS-04, GV.OV-03.` | `ID.RA-01, ID.RA-04, PR.PS-06, GV.SC-04, PR.IR-03.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/CRA.md` | SR-CRA-101+SR-CRA-103+SR-CRA-104 | `ID.IM-03 (primary), ID.RA-05, DE.AE-02, GV.OV-03.` | `ID.RA-04, GV.OV-01, GV.PO-02, ID.RA-01, GV.OC-03, GV.SC-04.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/DORA.md` | SR-DORA-008+SR-DORA-009+SR-DORA-010 | `ID.IM-03 (primary), ID.RA-05, DE.AE-02, GV.OV-03, PR.PS-04.` | `GV.OV-02, ID.RA-01, PR.PS-06, ID.RA-04, PR.AA-05, PR.AA-06.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/GDPR.md` | SR-GDPR-019+SR-GDPR-021+SR-GDPR-022 | `ID.IM-03 (primary), ID.RA-05, DE.AE-02, GV.OV-03.` | `RS.CO-03, RS.MA-04, RS.CO-02, ID.AM-08.` |
| `baseline/domains/D-10_Monitoring-Audit/D-10.3/regs/NIS2.md` | SR-NIS2-037+SR-NIS2-038 | `ID.IM-03 (primary), ID.RA-05, GV.OV-03, DE.AE-02.` | `GV.PO-01, ID.IM-01, GV.OV-03, GV.PO-02.` |

## Review flags

- none

## Informational: gloss lines mentioning tokens outside the uniformized set

- `D-01.1/regs/CRA.md @L37` — gloss mentions outside uniformized set: ['PR.DS-02']
- `D-01.1/regs/DORA.md @L38` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-01.2/regs/DORA.md @L37` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-01.4/regs/DORA.md @L38` — gloss mentions outside uniformized set: ['ID.AM-05']
- `D-04.1/regs/GDPR.md @L38` — gloss mentions outside uniformized set: ['DE.AE-02', 'PR.PS-04']
- `D-04.1/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['DE.AE-02', 'PR.PS-04']
- `D-04.2/regs/CRA.md @L38` — gloss mentions outside uniformized set: ['DE.CM-09', 'PR.IR-04']
- `D-04.2/regs/GDPR.md @L38` — gloss mentions outside uniformized set: ['ID.AM-08', 'PR.IR-04']
- `D-04.2/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['PR.IR-03']
- `D-04.3/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['RS.AN-03', 'RS.AN-07']
- `D-04.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['RS.MA-03']
- `D-07.1/regs/AI_Act.md @L38` — gloss mentions outside uniformized set: ['ID.RA-01']
- `D-07.1/regs/CRA.md @L39` — gloss mentions outside uniformized set: ['PR.PS-01']
- `D-07.1/regs/NIS2.md @L38` — gloss mentions outside uniformized set: ['PR.PS-02']
- `D-07.2/regs/AI_Act.md @L40` — gloss mentions outside uniformized set: ['ID.RA-01']
- `D-07.2/regs/CRA.md @L42` — gloss mentions outside uniformized set: ['PR.PS-06']
- `D-07.3/regs/CRA.md @L39` — gloss mentions outside uniformized set: ['PR.PS-02', 'PR.PS-06']
- `D-08.1/regs/NIS2.md @L40` — gloss mentions outside uniformized set: ['ID.RA-01', 'PR.PS-02']
- `D-09.1/regs/GDPR.md @L34` — gloss mentions outside uniformized set: ['GV.RR-02']
- `D-09.1/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['GV.OV-01']
- `D-09.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['PR.PS-01']
- `D-10.1/regs/GDPR.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'DE.CM-01', 'DE.CM-09', 'ID.IM-04']
- `D-10.2/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['ID.AM-08', 'PR.DS-11']
- `D-10.2/regs/GDPR.md @L34` — gloss mentions outside uniformized set: ['DE.CM-01', 'PR.DS-11']
- `D-10.3/regs/AI_Act.md @L34` — gloss mentions outside uniformized set: ['GV.OV-03', 'ID.IM-03', 'ID.RA-05', 'PR.PS-04']
- `D-10.3/regs/CRA.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05']
- `D-10.3/regs/DORA.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05', 'PR.PS-04']
- `D-10.3/regs/GDPR.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'GV.OV-03', 'ID.IM-03', 'ID.RA-05']
- `D-10.3/regs/NIS2.md @L34` — gloss mentions outside uniformized set: ['DE.AE-02', 'ID.IM-03', 'ID.RA-05']

