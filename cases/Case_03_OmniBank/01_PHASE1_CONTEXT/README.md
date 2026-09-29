# Phase 1 — Contextual Definition (Case 03 — OmniBank Financial Systems)

> **Status:** COMPLETE (1.0.0, 2026-09-28)  
> **Input:** `Doc01_INTAKE_FORM.md` (company-provided facts, 5 sections)  
> **Output:** `Doc02_Adjusted_Goals.md` — 134 Adjusted Goals (29 PO / 105 SO) across 38/38 active sub-domains for the five applicable regulations (GDPR, CRA, NIS 2, DORA, AI Act).

## Pipeline contract (ADR-004)

- **Consumed:** Baseline Goals (frozen modular baseline) + company context (intake).
- **Produced:** Adjusted Goals (`AG-D-XX.Y-NNN`) — the only exchange unit Phase 2 consumes.
- **Corpus:** `filtered_corpus/` — composed verbatim slice of the modular baseline for the five active regulations (38 sub-domains; regulation purity by construction; zero summaries).

## Key classification decisions

| Regulation | Role | Notes |
|---|---|---|
| GDPR | Controller (+ processor, employee data) | 29 objective pairs |
| CRA | Manufacturer, Class I important product | 36 |
| NIS 2 | Essential Entity (Annex I banking) | 24 |
| DORA | Financial Entity (credit institution + PSP) | 30 |
| AI Act | **Provider & Deployer** (OmniScore, Annex III §5(b)) | 15 |

Proportionality: LARGE scale — in-house key custody (HSM), 24/7 SOC, dedicated security organization; DORA ICT risk-management and resilience-testing families; AI Act provider duties (conformity, registration) stack on deployer duties for OmniScore.
