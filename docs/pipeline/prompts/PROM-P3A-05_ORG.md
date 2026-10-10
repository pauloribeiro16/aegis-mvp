---
ficha_id: PROM-P3A-05
title: 'Write the organizational requirement for one duty'
phase_step: 'Phase 3 Part 1 · Organizational lane (wave 5)'
pattern: 'one structured call per duty'
version: 1.0.0
created: 2026-10-10
status: ACTIVE
normative_source:
  - 'docs/pipeline/08_PHASE3_PART1_CONSTRUCTION.md wave 5'
  - 'ADR-008 D4 (routing by realization class; duties, not verdict rows)'
  - 'cases/Case_01_TinyTask_SaaS/03_PHASE3_SPEC/part1_security_privacy/Doc03_Organizational_Requirements.md (the golden anatomy)'
---

# PROM-P3A-05 — Write the organizational requirement for one duty

## Metadata

| Field | Content |
|---|---|
| Role | Governance & compliance requirements engineer |
| Mission | For ONE organizational duty (which may span several objectives and sub-domains), write the single EARS requirement with an organizational subject, a binary fit criterion, and a NIST CSF chain |
| Inputs | The duty block (its objectives, dispositions and warrants from the proportionality audit) and the company fact sheet |
| Output | One markdown block of bold fields — the ORG card without its id |
| Human gate | The acceptance round (G-P3-A) |
| Failure mode | One requirement per objective instead of per duty (the 1:1 trap the audit records); an enterprise-shaped duty written without the proportional form the audit's warrant describes; a fit criterion that is a process description rather than a pass/fail test |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `DUTY.md` | The duty: objectives, the audit's disposition and warrant — the warrant's proportional form is what the statement shall describe |
| 2 | `FACT_SHEET.yaml` | The company (R6) |

## Output schema

```markdown
**Statement (EARS):** Where the organization detects corruption or unauthorised modification of stored billing state, the organization shall record the detection and route it to a named owner for assessment.
**Requirement Origin:** GDPR Art. 33(1) breach-handling duty; proportionality audit warrant
**Fit criterion:** A detection with no owner record does not close.
**Verification Method:** INSPECT
**Chain:** GDPR Art. 33(1) → `SO-D-04.1-001` → `DE.CM-9`, `GV.RR-2`
**Control Anchors:** `DE.CM-9`, `GV.RR-2`
**Dependencies:** Stakeholders: founders; Owner: named per requirement; Cadence: per detection; Information Systems / Databases: ; Databases: —
**Priority:** Must
```

## Rules the output must obey

- **One requirement per DUTY.** The duty block already merged the rows that
  share the obligation — do not split it back by objective or sub-domain.
- **The proportional form is in the warrant.** The audit decided the shape the
  duty takes at this company's scale; write THAT, not the enterprise form.
- **EARS with `the organization shall`.** The subject is the organization, not
  the system.
- **Anchors are NIST CSF (GOVERN function where applicable)** and must be real
  CSF ids — the pipeline verifies each resolves under `baseline/CONTROLS/`.
- **No id.** The pipeline allocates `ORG-D-XX.Y-NNN` per duty.

## Self-checks (L2)

- The statement has `the organization shall` and one behaviour.
- The fit criterion is judgeable true/false.
- Verification Method is TEST/INSPECT/DEMONSTRATE/ANALYZE.
- Every control anchor is a plausible NIST CSF 2.0 id.
- Priority is Must or Should.

## Human gate

The card is a proposal until the round judges it.

## Failure handling

One repair round on structure (missing field, non-EARS statement, unknown
anchor, wrong method enum).

## Normative source

Doc 08 wave 5 · ADR-008 D4 · the Case 01 audit (32 rows → 16 duties) and its
hand-written `Doc03` (the golden).

## Prompt body

> You are given ONE organizational duty: the objectives it merges, the audit's
> disposition (ORG) and the warrant describing the proportional form this
> company's scale demands. Write the single EARS requirement with an
> organizational subject, a binary fit criterion, a verification method, the
> chain, and NIST CSF control anchors. Do not allocate an id. Write the
> proportional form the warrant describes — not the enterprise form.
