# Traceability Repair Ledger — Case_03_OmniBank

> **Date:** 2026-09-29 · **Scope:** the referential-integrity defects found when the ADR-007 discharge semantics were checked against this case. Reproduce with `python scripts/check_traceability.py --case Case_03_OmniBank` and `python scripts/reanchor_chains.py --case Case_03_OmniBank` (dry run).
> **Root cause:** the Phase 3 chains were authored against a fixed five-slot convention (001=GDPR, 002=CRA, 003=NIS 2, 004=DORA, 005=AI_Act) while Phase 2 numbers objectives **compactly** — canonical order GDPR → CRA → NIS 2 → DORA → AI Act, numbered `001…n` over those actually present in each sub-domain. Where a sub-domain lacks an earlier regulation, every later suffix shifts down. 28 of the 134 objectives carry a suffix that convention never anticipated.

## 1. Repaired (mechanical, verifiable)

| Repair | Extent | Verification |
|---|---|---|
| Chain re-anchoring to the compact numbering | 35 citations rewritten in `part1_security_privacy/Doc01_Requirements_Elicitation_and_PUC.md` | `reanchor_chains.py --apply`; T2 fell 25 → 0 |
| Same-sub-domain multi-law chains corrected by hand | 6 constraint rows (RN11/RN12/RN15/RN19/RN20, awareness training, compliance-records) | T1/T2 clean on those rows |
| Cross-sub-domain chains with no objective for the cited law | 2 rows (RN13 transport; secure-by-default) — the non-existent regulation leg removed | T1 clean on those rows |
| Corrupted Phase 2 rows | 4 rows (`SO-D-01.3-003`, `SO-D-01.4-002`, `SO-D-01.4-004`, `SO-D-05.2-002`) carried baseline markdown/YAML inside the Operational Statement cell, splitting the 9-column table into 11 fields. Excess cells removed against the `Parent Goal` column as anchor | all 134 rows now 9 fields; Method/Owner/VC parse canonically |
| Dangling tension reference | T-002 cited `SO-D-05.2-004`, which has no objective row → corrected to `SO-D-05.2-003` (the AI-Act leg of D-05.2) | T1 |
| Stale prose after the 103 → 134 renumbering | `01_PHASE1_CONTEXT/README.md` (output line + per-regulation table), `02_PHASE2_RULES/README.md` (input + exchange unit), `03_PHASE3_SPEC/README.md` | counts now 134 / 29+105 and 29 / 36 / 24 / 30 / 15 |
| Exit Gate G6 evidence | the G6 row claimed "STEP1–STEP5" while only STEP3/4/5 exist; the row now names the three files that do | T4 |
| Sufficiency figure | "95/100 rows carried" exceeded the matrix's own arithmetic (92/100 = 100 − 2 organizational − 6 N/A); corrected in the Case_02 assessment | T3b |

## 2. Resolved on 2026-09-29 (no longer open)

| Location | Resolution |
|---|---|
| `Doc01` L447 — Retention Family | `DORA/NIS 2 record floors` → `SO-D-05.2-005` removed. D-05.2 holds only GDPR/CRA/AI Act, so no such objective exists; the DORA records leg is already carried at D-10.2 by the Compliance Records chain. The retention row now cites the GDPR objective alone. |
| `Doc01` L501 — ICT Third-Party Register | Re-segmented by law: `DORA Art. 28-30` → `SO-D-06.4-004` · `GDPR Art. 28` → `PO-D-06.1-001`/`PO-D-06.3-001` · `NIS 2 Art. 21(3)` → `SO-D-06.1-003`/`SO-D-06.3-003`. The phantom `SO-D-06.4-005` and a duplicated `SO-D-06.1-003` are gone. |
| `Doc01` L740 / `Doc02` L925 — AI Adversarial Robustness | The AI-Act leg re-pointed per sub-domain (`SO-D-02.1-005`/`-02.4-003`/`-07.1-005`/`-07.2-003`/`-10.3-005`) and separated from the CRA leg (`SO-D-02.1-002`/`-07.2-001`); Doc02's step chain aligned to the same set. |
| `Doc01` L193 — AI Event Logging | `SO-D-05.2-004` → `SO-D-05.2-003` (the AI-Act leg of D-05.2). |
| `Doc02` L511 / L568 / L607 | Bare `chain:` citations with no law token, invisible to the re-anchoring script: `SO-D-05.2-005` dropped, `SO-D-05.1-004` → `-003`, `SO-D-06.2-002` → `-001`. |
| Driver symmetry (T5) | 37 drivers whose declared carrier did not cite them back were attached to that carrier with the law and article taken from the Phase 2 spine (`scripts/attach_missing_chains.py`): 4 in Case_01, 3 in Case_02, 30 in Case_03. Transversal rows are exempt per ADR-007 D3 — the matrix is their record of record. |

## 3. Recorded debt (ADR-007 D2/D3)

- **Coverage granularity.** All 128 `Accepted R1` verdicts in `OBJECTIVE_MAPPING.md` assert coverage by **carrier linkage** (the objective id appears in a chain), not by discharge. A leg-level audit has been run in Case_01 only, where 20 of 26 "covered" rows became "partially covered" with named carve-outs. The same note is recorded in the Case_02 matrix. Attaching a chain makes the derivation auditable; it does not certify that the carrier's fit criteria discharge the objective.
- **Organizational lane.** The 2 DPO objectives are verdicted `No functional carrier (organizational)`; this case has no `part1_security_privacy/Doc03_Organizational_Requirements.md`, so the ADR-008 lane is codified but unexercised here. It was first executed in Case_02 (`ORG-D-08.1-001`, `ORG-D-08.2-001`, 2026-09-29).

## 4. Guards now in force

- `python scripts/check_traceability.py --strict` — T1 id resolution, T2 law/driver regulation coherence, T3 totals arithmetic, T3b ratio ceiling, T4 gate evidence, T5 driver symmetry. Scoped to the **active** deliverable: version folders are historical snapshots and are never asserted against, since they legitimately carry ids an earlier numbering produced.
- `python scripts/reanchor_chains.py --case <name> [--apply]` — re-anchors chains after a Phase 2 renumbering; dry-run by default.
- Codified as **R12b** in `AGENTS.md`.
