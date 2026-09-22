---
document_id: AEGIS-MVP-ADR-002
title: 'MVP scope — TECHNOLOGY-only realization class'
status: 'ACCEPTED — decided by the researcher, 2026-09-22'
date: 2026-09-22
phase: 'MVP scope (aegis-mvp); cross-ref ADR-001'
author: 'Decision: PhD researcher; record: Executor session'
---

# ADR-002 — MVP scope: TECHNOLOGY-only realization class

> Registered decision (2026-09-22), stated by the researcher: *"O meu MVP vai focar-se apenas em tecnologia."* Scope clarified with the researcher the same day: the restriction applies to the **realization class of the future Phase 2 increment** — not to Phase 1 content.

---

## 1. Decision

- The **aegis-mvp demonstrator** scopes itself to the **`TECHNOLOGY`** lane of the AEGIS realization-class enum {`TECHNOLOGY`, `PROCESS`, `CAPABILITY`} (`Methodology_compact/00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` §2).
- When the MVP gains its **Phase 2 increment**, its rules/practices catalog admits **only TECHNOLOGY-class entries**: verifiable properties of the built state (test/configuration evidence, no recurring constitutive human judgement).
- **PROCESS-class** (coordinated activity sequences) and **CAPABILITY-class** (standing organizational abilities) rules/practices remain in the **full methodology** (Methodology_compact) and are **out of MVP scope**. They are not deprecated — the MVP is a demonstrator slice, not the methodology.
- **Phase 1 of the MVP is unchanged**: objectives stay technology-neutral in wording (SPEC R5); the P3 sub-domain selection logic is untouched. This decision governs downstream realization scope only.

## 2. Why (researcher to complete)

The decision was recorded as stated, without rationale. This section is deliberately reserved so the researcher can dictate the why later (same purpose as ADR-001 §5 — re-readable reasoning for the thesis).

## 3. Consequences

1. **ADR-001 interaction** — the D1 trichotomy (property/process/capability) remains the methodology's ontology; the MVP realizes only its TECHNOLOGY slice. The admission gate A1–A4 and D2 tier citation apply to that slice: for the MVP, T2/T3 citations are restricted to referential entries that can anchor technical properties.
2. **Future Phase 3 handoff** — only the TECHNOLOGY lane (`UC-*`, RUBRIC §5B) will be produced by the MVP; `PROC-*`/`CAP-*` cards are out of MVP scope.
3. **Selection filter** — the future MVP Phase 2 pipeline filters `realization_class == TECHNOLOGY`; candidates whose primary class is PROCESS/CAPABILITY are recorded as out-of-scope in the run's ledger, not silently dropped.
4. **Comparability** — methodology-level coverage claims (e.g., Case_01's 46 controls) remain full-scope; any MVP-derived count must state the TECHNOLOGY-only filter to stay comparable.
5. **No repo changes now** — SPEC.md already restricts the MVP to Phase 1; this ADR binds the design of the future Phase 2 increment (ADR-001 consequence campaign C5).

## 4. Related

- [ADR-001 — What "best practice" means in AEGIS Phase 2](ADR-2026-09-22_best-practice-layer.md) (same directory, same date).
- `Methodology_compact/00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` §2 (class definitions), §5 (lane mapping), §5B (`UC-*` nomenclature for the TECHNOLOGY lane).
