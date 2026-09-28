# Round 1 Register — Iterative Risk-Acceptance Synthesis (TinyTask SaaS)

> **Round window:** opened 2026-09-24 (proposals ADJ-1…ADJ-9, P-01…P-04) · verdicts collected 2026-09-28 · **Status: CONVERGED** — 13 Accepts, 0 Rejects, 0 Adjusts; no re-proposals required.
> **Inputs:** [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md) (exhaustive coverage matrix), [`PRINCIPLE_MAPPING.md`](PRINCIPLE_MAPPING.md) (principle gaps), `../v1_security_privacy_synthesis/Doc01`/`Doc02` (approved V1 baseline).
> **Effect:** accepted items evolve `Doc01`/`Doc02` to version 4.0.0, stored in `../v2_security_privacy_synthesis/` (top-level `Doc01`/`Doc02` kept as synced active copies); `v0_functional_baseline/` and `v1_security_privacy_synthesis/` remain untouched as history.
> **Control selection source rule (ADR-005 Step 4):** anchors are copied only from pre-verified surfaces — the driver objective's published control set (`02_PHASE2_RULES/Doc01`) and the mapping store (`baseline/MAPPINGS/sr_control_mappings/<REG>.json`). PF 1.1 anchors accompany GDPR-derived obligations only (R2/R8).

---

## §1 Verdict Ledger

| Item | Type | Affected constraint(s) | Chain change (from → to) | Verdict |
|---|---|---|---|---|
| ADJ-1 | Chain re-anchor | RN9 | `SO-D-02.1-002` → `SO-D-03.2-002` | **Accept** |
| ADJ-2 | Chain re-anchor | RN11; RN10, RN12 co-driver | `SO-D-02.2-002` → `SO-D-03.1-002`; RN10/RN12 gain `SO-D-03.1-002` | **Accept** |
| ADJ-3 | Chain re-anchor | RN12 | `SO-D-02.1-002` → `SO-D-03.3-002` | **Accept** |
| ADJ-4 | Chain re-anchor | RN13, RN17 | `SO-D-07.1-002` / `SO-D-02.1-002, SO-D-05.1-002` → `SO-D-07.2-002` | **Accept** |
| ADJ-5 | Chain re-anchor | RN18 | `SO-D-03.1-002` → `SO-D-10.1-002` + co-driver `SO-D-04.1-002` | **Accept** |
| ADJ-6 | Chain re-base | RN14 | `SO-D-07.1-002` (umbrella) → `SO-D-07.2-002` | **Accept** |
| ADJ-7 | Chain re-anchor | RN15 | `SO-D-01.1-002, SO-D-08.1-002` → `SO-D-01.4-002` | **Accept** |
| ADJ-8 | Chain re-anchor | RN16 | `SO-D-05.1-002, SO-D-08.1-002` → `SO-D-01.4-002` | **Accept** |
| ADJ-9 | Co-driver added | RN24 | `PO-D-01.2-001` + twin `SO-D-01.2-002` | **Accept** |
| P-01 | New constraint (absorbed) | **RN27** (new) | `GDPR Art. 12(6) + Art. 11(2)` → `SO-D-03.1-001` → `PRIN-ENG-01` | **Accept** |
| P-02 | New constraint (absorbed) | **RN28** (new) | `CRA Annex I Part I (2)(b) + (2)(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` | **Accept** |
| P-03 | **D1** derived requirement | **R8.3** (new RN30) + PUC 8.3 + {U.C. 8.3} | `CRA Annex I Part I (2)(m)` → `SO-D-05.3-002` → `PRIN-ENG-07`; RN21 (GDPR Art. 17) co-driver | **Accept** |
| P-04 | New documentation requirement | **RN29** (Table 7, SHOULD) | `CRA Annex II §8(a)–(e)` → `SO-D-08.1-002` | **Accept** |

Constraint wording of RN9–RN18, RN24 is unchanged by ADJ items; only driver objectives and control anchors change.

---

## §2 New Constraint Formulations (EARS, altitude L2, technology-neutral)

### RN27 — Requester Identity Verification for Rights Exercise (MUST; absorbs P-01)
- **EARS:** If a data-subject request to export or erase personal data is submitted, the system shall verify the requester's identity, using means proportionate to the risk of mis-identification, before executing the request.
- **Fit criterion:** every export/erasure execution is preceded by a recorded successful identity verification of the requester; unverified requests never reach execution.
- **Verification:** `TEST` · **Volere fit criterion:** binary, deterministic.
- **Chain:** `GDPR Art. 12(6) + Art. 11(2) + Art. 5(1)(c)` → `SO-D-03.1-001` → `PRIN-ENG-01` → CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6.
- **Carriers:** `R8.1`, `R8.2` cards; `{U.C. 8.1}` step 2 + extension 2b; `{U.C. 8.2}` step 5 + extension 5a.

### RN28 — Secure-by-Default Configuration with User Reset (MUST; absorbs P-02)
- **EARS:** When a new shared artifact (workspace or project) is created, the system shall initialize it with the most restrictive configuration the product supports, and the system shall allow an authorized user to reset the configuration to that default.
- **Fit criterion:** every newly created workspace/project starts with membership, visibility, and sharing settings at the restrictive default; a reset action restores exactly that state.
- **Verification:** `TEST`.
- **Chain:** `CRA Annex I Part I (2)(b) + (2)(c)` → `SO-D-03.4-002` → `PRIN-ENG-04` → CSF PR.PS-01.
- **Carriers:** `R2.1`, `R3.1` cards; `{U.C. 2.1}` step 3 + success guarantee; `{U.C. 3.1}` step 3 + extension 1c.

### RN30 — Workspace Permanent Removal (MUST; CRA leg of P-03, absorbed in `R8.3`)

- **EARS:** When the Workspace Owner confirms the deletion of a workspace, the system shall permanently erase all workspace content and settings across stores and shall issue a deletion receipt.
- **Fit criterion:** after an Owner-completed deletion no workspace content or settings are retrievable in any store, and the receipt certifies the deletion.
- **Verification:** `TEST`.
- **Chain:** `CRA Annex I Part I (2)(m)` → `SO-D-05.3-002` → `PRIN-ENG-07` → CSF PR.DS-10, PR.DS-02.
- **Carriers:** `R8.3` card; `{U.C. 8.3}` steps 4–5, extension 4b.

### RN29 — Secure-Use Instructions (SHOULD; absorbs P-04, Table 7 quality-attribute row)
- **Requirement:** the product shall be accompanied by secure-use instructions — or an address where they can be consulted — covering initial commissioning and lifetime measures: membership and role management, credential handling, and configuration of sharing defaults, addressed to end users and administrators.
- **Fit criterion:** the documentation contains a secure-use section addressing the listed minimum topics for both audiences.
- **Verification:** `INSPECT`.
- **Chain:** `CRA Annex II §8(a)–(e)` → `SO-D-08.1-002` → CSF PR.AT-01.

### R8.3 — Delete Workspace and Permanently Erase Workspace Data (D1 derived requirement, MUST; absorbs P-03)

Card constraints: **RN30** (below), RN21 (co-driver), RN18 (audit).
- **Card:** new leaf `R8.3` under package `R8`; matching `PUC 8.3` and `{U.C. 8.3}` (Sea-Level, fully dressed).
- **Description:** the Workspace Owner deletes a workspace and all its contents (projects, tasks, comments, attachments, settings) permanently, without deleting their own account.
- **Chain (constraints absorbed in-card):** `CRA Annex I Part I (2)(m)` → `SO-D-05.3-002` → `PRIN-ENG-07` → CSF PR.DS-10, PR.DS-02 (permanent removal); `GDPR Art. 17 + Art. 28(3)(g)` → `PO-D-05.3-001` → `PRIN-ENG-07` → CSF PR.DS-10 / PF CT.DM-P1 (RN21 co-driver, owner's personal data in the workspace); RN18 audit record of the deletion.
- **Verification (functional):** `TEST` — an Owner-completed workspace deletion leaves no retrievable workspace content or settings.

---

## §3 Control Selection (ADR-005 Step 4, post-convergence)

| Constraint | Selected anchors | Source surface | Selection rationale |
|---|---|---|---|
| RN9 | CSF PR.AA-05, PR.AA-06 | Published set on `SO-D-03.2-002` (PR.AA-01, PR.AA-05, PR.AA-06, ID.AM-01, DE.CM-09) | Isolation & mediation are enforced by access-permission control; ID.AM-01 (inventory) and DE.CM-09 (monitoring) are not the isolating mechanism. |
| RN10 | CSF PR.DS-01, PR.AA-01, PR.AA-05 | Published sets on `SO-D-01.1-002` + `SO-D-03.1-002` | Credential protection = at-rest protection + identity/credential management; PR.PS-02/PR.PS-01 belonged to the dropped dev-process driver. |
| RN11 | CSF PR.AA-01, PR.AA-05, PR.AA-06 | Published set on `SO-D-03.1-002` | Unchanged subset — all three ∈ published set of the new driver. |
| RN12 | CSF PR.AA-05, PR.AA-06 | Published set on `SO-D-03.3-002` (PR.AA-05, PR.AA-06, DE.CM-09) | RBAC mediation = permission enforcement + least privilege. |
| RN13 | CSF PR.PS-06 | Published set on `SO-D-07.2-002` (PR.PS-06, PR.PS-02) | Upload validation is a protective surface-reduction measure (PR.PS-06). |
| RN14 | CSF PR.PS-06 | Published set on `SO-D-07.2-002` | Content neutralization = protective measure (PR.PS-06), unchanged. |
| RN15 | CSF PR.DS-01, PR.DS-10 | Published set on `SO-D-01.4-002` (PR.DS-01, PR.DS-10, PR.PS-04) | Billing invariant = integrity of stored state; PR.AT-01 belonged to the dropped instructions driver. |
| RN16 | CSF PR.DS-10 | Published set on `SO-D-01.4-002` | Webhook origin verification = integrity of processed messages; ID.AM-03/PR.AT-01 belonged to the dropped drivers. |
| RN17 | CSF PR.PS-02, PR.PS-06 | Published set on `SO-D-07.2-002` | Throttling = protective measure against resource exhaustion on the exposed surface. |
| RN18 | CSF DE.CM-01, DE.CM-09 | Published sets on `SO-D-10.1-002` (DE.CM-01, DE.CM-09, ID.IM-04) + `SO-D-04.1-002` (DE.CM-09, PR.PS-04, RS.MA-02) | Audit logging = monitoring of relevant internal activity; PR.AA-05 belonged to the dropped driver. |
| RN24 | CSF PR.DS-02, PR.IR-01 / PF PR.DS-P2 (unchanged) | Published sets on `PO-D-01.2-001` + `SO-D-01.2-002` (PR.DS-02, PR.IR-01) | Twin CRA driver's published set matches the existing selection exactly; PF retained (GDPR-derived). |
| RN27 | CSF PR.AA-03, PR.AA-02 / PF PR.AC-P6 | Published set on `SO-D-03.1-001` (PR.AA-03, PR.AA-02, PR.DS-10) + mapping store `SR-GDPR-009` (nist_pf: PR.AC-P6, PR.AC-P3) | Identity verification = user authentication control; PF PR.AC-P6 selected from the store's SR-GDPR-009 axis (PR.AC-P3 available as alternate). |
| RN28 | CSF PR.PS-01 | Published set on `SO-D-03.4-002` (PR.PS-01, PR.DS-10, GV.SC-03) | Secure-by-default configuration = protective default (PR.PS-01). |
| RN30 | CSF PR.DS-10, PR.DS-02 | Published set on `SO-D-05.3-002` (PR.DS-10, PR.DS-02) | Permanent removal = destruction of data at rest and in use; PF CT.DM-P1 remains on RN21's GDPR chain (co-driver), not on the CRA leg. |
| RN29 | CSF PR.AT-01 | Published set on `SO-D-08.1-002` | Secure-use instructions = awareness & training material (PR.AT-01). |

Integrity note: the published set of `SO-D-05.3-002` lists `PR.DS-10` twice in `02_PHASE2_RULES/Doc01` (literal duplicate); the selection cites the unique value.

---

## §4 Skills Attribution (analysis lens, 1:1 with PRIN-ENG)

| Item | Skill |
|---|---|
| ADJ-1 (RN9 → SO-D-03.2-002) | TB (trust-boundary-analysis) |
| ADJ-2 (RN11 → SO-D-03.1-002) | LP (least-privilege-analysis) |
| ADJ-3 (RN12 → SO-D-03.3-002) | LP |
| ADJ-4/ADJ-6 (RN13/RN14/RN17 → SO-D-07.2-002) | AS (attack-surface-analysis) |
| ADJ-5 (RN18 → SO-D-10.1-002) | V (verifiability-analysis) |
| ADJ-7/ADJ-8 (RN15/RN16 → SO-D-01.4-002) | V |
| ADJ-9 (RN24 twin) | TB |
| P-01 (RN27) | TB |
| P-02 (RN28) | FS (fail-safe-defaults-analysis) |
| P-03 (R8.3) | LE (lifecycle-erasure-analysis) |
| P-04 (RN29) | — (documentation surface; INSPECT) |

All seven skills are in use across the coverage matrix (`OBJECTIVE_MAPPING.md` Skill column).

---

## §5 Convergence & Effect

- **Convergence criterion met:** the round produced no rejections and no adjustments; the client closed the item set on 2026-09-28.
- **Effect:** `Doc01`/`Doc02` evolve to **4.0.0** (stored in `v2_security_privacy_synthesis/`) applying: 11 chain re-anchors (D2-class: driver/anchor updates, constraint wording unchanged), 4 new constraints (RN27, RN28, RN30 absorbed in-card; RN29 in Table 7), 1 D1 derived requirement (R8.3 + PUC 8.3 + {U.C. 8.3}).
- Coverage after Round 1 (see updated totals in [`OBJECTIVE_MAPPING.md`](OBJECTIVE_MAPPING.md)): **26 objectives with a functional carrier · 31 organizational (no functional carrier, recorded decisions) · 2 design guidance · 3 N/A · total 62.**
