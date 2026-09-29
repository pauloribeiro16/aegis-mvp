---
id: 'AEGIS-MVP-ADR-008'
date: 2026-09-28
status: ACCEPTED
decided_by: researcher (working session)
amends: 'ADR-2026-09-22_mvp-technology-only-scope.md (ADR-002, PROCESS increment reserved) · ADR-2026-09-22_pipeline-io-contract.md (ADR-004, Fase 3 output unit)'
---

# ADR-008 — Phase 3 gains an organizational deliverable: Doc03 Organizational Requirements (PROCESS lane)

## 1. Status

**ACCEPTED** — decided by the researcher on 2026-09-28. Materializes, at specification level, the "future PROCESS increment" reserved by ADR-002; the MVP's TECHNOLOGY-only implementation scope is unchanged.

## 2. The question, stated precisely

31 of Case_01's 62 Phase 2 objectives — plus the uncarried legs surfaced by the ADR-007 re-audit — bind on organizational/process controls: breach notification 72 h, coordinated vulnerability disclosure, Art. 28 contract floors, DPO awareness and training, DPIA, SBOM, technical documentation. Today they exist only as verdict strings (`No functional carrier (organizational)`) in the coverage matrix. The capability-lane rule promises they are "never silently dropped… deferred to the future PROCESS increment", but that increment was never designed: no deliverable, no derivation rules, no anchor surface, no slot in the pipeline I/O contract. Can organizational obligations be derived into requirements with the same rigor as product requirements, in a separate document, without breaking ADR-002?

## 3. Decision

### D1 — Doc03 Organizational Requirements is the second Part 1 output

`Doc03_Organizational_Requirements.md` per case, inside `03_PHASE3_SPEC/`, derived by the same synthesis machinery as Doc01. Phase 3 Part 1 therefore outputs two units of exchange: product requirements (Doc01/Doc02 — TECHNOLOGY lane) and organizational requirements (Doc03 — PROCESS lane). ADR-004's I/O table is amended accordingly; Phase 4 consumes both.

### D2 — Derivation machine (identical semantics, organizational subject)

Each organizational requirement carries: an EARS constraint with an organizational subject (`The organization shall <response>.`; `When <trigger>, the organization shall <response>.`; `While <state>, …`; `If <condition>, then …`; `Where <activity exists>, …`), a Volere fit criterion, a verification method — `INSPECT`/`DEMONSTRATE`/`ANALYZE` dominate, `TEST` where automated evidence exists — an owner (from the Phase 2 Governance & Stakeholder Matrix), a MoSCoW priority driven by regulatory priority, and the full chain `regulation article → Phase 2 objective → (principle) → organizational control anchor`. One requirement per congruent demand set (ADR-007 D1 applies unchanged); specificity stays at L2 (no invented parameters — values come from the regulation, a cited source, or a risk assessment).

### D3 — Routing rule

A demand leg routes by its realization class (ADR-003): TECHNOLOGY leg → Doc01 product requirement; PROCESS/CAPABILITY leg → Doc03 organizational requirement. Doc03 input rows come from (a) objectives verdicted `No functional carrier (organizational)`, and (b) carve-outs recorded in the ADR-007 discharge records.

### D4 — Anchor surface (pre-verified, organizational)

Primary: NIST CSF 2.0 GOVERN function (`baseline/CONTROLS/NIST_CSF_2.0/GOVERN/`, 31 subcategory files) plus other CSF functions where the anchor is organizational in nature. Advisory, under R2b agent discretion (not enforced by `verify_no_loss.py`): ISO/IEC 27001:2022 Annex A organizational controls (`ISO_27001_2022/A5_ORGANIZATIONAL/`), ENISA NIS2 baseline (`ENISA/NIS2_BASELINE/`), BSI IT-Grundschutz OPS layer. PF 1.1 anchors accompany GDPR-derived obligations only (dashboard-published axis, R8). No invented anchors (R2).

### D5 — Identifiers and designation

Organizational requirements use IDs `ORG-D-XX.Y-NNN` — Fase 3 layer, designation "Requirements". The `Doc03` slot is reused; the deliverable's charter is organizational requirements, distinct from the product NFR catalog whose former content lives absorbed in Doc01 cards.

### D6 — Relationship to ADR-002

ADR-002 scoped the MVP to the TECHNOLOGY lane of the practices/implementation catalog. ADR-008 stays at specification level: Doc03 specifies organizational requirements and their verification methods; it does not implement process controls and does not admit PROCESS-class entries into the MVP practices catalog. Total compliance remains conditional on operating the lane (company operation / Phase 4), now with a derived, verifiable specification instead of recorded verdicts.

### D7 — Rounds, gates and validation apply unchanged

Doc03 content enters through ADR-005 rounds (per-item Accept/Reject/Adjust), is covered by the Part 1 Exit Gate (G1's exhaustive-mapping evidence surface extends to the organizational mapping), R12 lint (`doc_lint.py --strict`), R11 discipline, and specificity matching (L2 ceiling).

## 4. Consequences

- Case_01: no backfill by default — Part 1 closed GREEN on 2026-09-28; its carve-outs remain recorded decisions pointing at the lane; a backfill round is possible on the researcher's order.
- Case_02: Doc03 skeleton created now; derivation runs with its next synthesis round on the researcher's order.
- The sufficiency statement "total compliance is conditional on operating the process lane" gains its designated artifact.
- Phase 4 verification planning must include organizational verification evidence (INSPECT/DEMONSTRATE/ANALYZE).

## 5. Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Keep organizational obligations as matrix verdict strings | Zero derivation, zero verification path; the PROCESS-increment promise stays unfulfilled. |
| Absorb organizational obligations into Doc01 cards | Contradicts the discharge verdicts (no functional surface exists) and Doc01's product charter; mixes lanes inside one deliverable. |
| Wait for a full PROCESS increment (Phase 2 pipeline for PROCESS class) | Larger change than needed; the specification is derivable now with existing machinery. |

## 6. References

- `templates/phase3_functional_spec_guidelines.md` §3.5 (derivation procedure + card anatomy)
- ADR-007 (discharge records → Doc03 input rows), ADR-002 (lane split), ADR-003 (`realization_class`), ADR-004 (I/O contract, amended)
- `baseline/CONTROLS/NIST_CSF_2.0/GOVERN/` · `baseline/CONTROLS/ISO_27001_2022/A5_ORGANIZATIONAL/` · `baseline/CONTROLS/ENISA/NIS2_BASELINE/`
