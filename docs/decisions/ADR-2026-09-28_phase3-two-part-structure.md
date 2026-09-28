---
id: 'AEGIS-MVP-ADR-006'
date: 2026-09-28
status: ACCEPTED
decided_by: researcher (working session)
amends: 'ADR-2026-09-24_phase4-threat-analysis-and-iterative-risk-acceptance.md (ADR-005, D3 phase placement) · ADR-2026-09-22_pipeline-io-contract.md (ADR-004, phase chain)'
---

# ADR-006 — Phase 3 runs in two parts: Part 1 Security & Compliance, Part 2 Threat & Risk Analysis

## 1. Status

**ACCEPTED** — decided by the researcher on 2026-09-28. This ADR amends the phase chain of ADR-004 and the phase placement of ADR-005 (D3); the ADR-005 round cycle and explicit control selection are unchanged.

## 2. The question, stated precisely

ADR-005 placed threat analysis in a separate **Fase 4**, launched on researcher judgment. The researcher's operating model is different: the threat & risk analysis **belongs to Phase 3 as its second part**, launched through **formal stop criteria** (a gate) rather than through an unstructured judgment call. How should Phase 3 and the phase chain be restructured?

## 3. Decision

### D1 — Phase 3 has two parts

- **Part 1 — Security & Compliance** (Steps 1–5b of the existing process): elicitation, exhaustive objective/principle mapping, risk-acceptance rounds, control selection, absorption — producing the versioned baseline (`v0`/`v1`/`v2`…). Lives where it lives today (`03_PHASE3_SPEC/`).
- **Part 2 — Threat & Risk Analysis**: STRIDE/LINDDUN over the accepted baseline + case risk register; outputs carry `TM-D-XX.Y-NNN` IDs. Lives in `03_PHASE3_SPEC/part2_threat_risk/`.

### D2 — The launch of Part 2 is gated by formal stop criteria

The **Part 1 Exit Gate (G1–G6)** — exhaustive mapping 100% verdicted (G1), rounds converged (G2), control selection complete (G3), deliverables at current version with checklist + `doc_lint --strict` green (G4), sufficiency assessment produced with explicit residuals (G5), transition dossier complete (G6) — is codified in the process manual and evidenced per case in the transition dossier. All six GREEN is a necessary condition to launch Part 2; the researcher then orders the launch.

### D3 — Phase chain amended (ADR-004)

`F0 Baseline → F1 Goals → F2 Objectives → F3 Specification [Part 1 + Part 2] → F4 Verification & Implementation`.

- The ADR-005 "Fase 4 — Threat Analysis" becomes **Phase 3 Part 2** (no separate phase).
- The former "Fase 5 — Verification & Assurance" is renamed **Fase 4 — Verification & Implementation**; the "Fase 5" designation is retired.

### D4 — Part 1 remains threat-free

No threat catalog, attack modeling, or abuse-case derivation appears in Part 1 deliverables. This supersedes the 2026-09-28 amendment on ADR-005's Case_01 grandfathering (no deferred-threat dossier is retained or created): Part 2 performs the analysis from scratch over the accepted baseline, seeded by the asset and trust-boundary statements of Part 1.

### D5 — Designations

Part 1 outputs requirements (`REQ-D-XX.Y-NNN`, practice `R<n>`/`RN<n>`); Part 2 outputs threat-model entries (`TM-D-XX.Y-NNN`) and the case risk register.

## 4. Consequences

- **Case_01:** Part 1 is complete — the Exit Gate is GREEN and evidenced in `cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/analysis_v1_to_v2/README.md`; Part 2 is cleared to launch on the researcher's order.
- **Case_02 and later cases:** replicate the same structure — Part 1 rounds → gate → Part 2.
- The ADR-005 round cycle, per-item verdicts, and explicit control selection are **unchanged**; only the phase placement of threat analysis and the phase chain change.
- Process manual, Phase 3 READMEs, and AGENTS.md are updated to the two-part structure and the amended chain.

## 5. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Keep ADR-005's separate Fase 4 | Splits the specification workstream in two; the gate between specification and threat analysis is a stop-criteria decision, not a phase boundary. |
| Merge threat analysis into Part 1 rounds | Reintroduces the ADR-005 conflation — threat work would precede client risk decisions instead of validating the accepted baseline. |
| Gate = researcher judgment only (no codified criteria) | Not auditable; the gate must be evidence-checkable (G1–G6). |

## 6. References

- ADR-005 (round cycle — unchanged; D3 phase placement superseded by D3 here)
- ADR-004 (pipeline I/O contract — phase chain amended)
- `cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/PHASE3_PROCESS_AND_METHODOLOGY.md` (Part 1 Exit Gate codification)
