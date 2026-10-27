---
ficha_id: PROM-P3B-06
title: 'The risk governance summary the human reads before signing'
phase_step: 'Phase 3 Part 2 · Etapa 2.5 — governance summary (onda D)'
pattern: 'deterministic document (no model call)'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'the plan''s Etapa 2.4/2.5 (the golden rule; G7–G12)'
  - 'RAND MR-114 signpost pattern (S-279) — every acceptance carries its review signpost'
---

# PROM-P3B-06 — The risk governance summary

## Metadata

| Field | Content |
|---|---|
| Role | (no model — composed by `p3b_risk_round` + `p3b_gate`) |
| Mission | Put in front of the person who signs: the register (inherent → mitigation → residual), the open attack paths, the statutory threats that cannot be accepted away, and the six gates |
| Inputs | The threat stores, the trees, the register, the signatures |
| Output | `05_RISK_REGISTER_AND_GOVERNANCE.md` + `steps/phase3b/gate_report.md` |
| Failure mode | A register that reads CONCLUDED while signatures are missing (G7); a residual that dropped without a requirement (the arithmetic is code-side for exactly this) |

## What the human is asked to do

One decision per threat, in `steps/phase3b/risk_verdicts.json`:

| Decision | Meaning |
|---|---|
| `Accept_Mitigated` | the named Part 1 requirements reduce this risk to the stated residual; accepted |
| `Accept_Residual_Risk` | a non-statutory Medium/High accepted for THIS version, with justification and review signpost |
| `Transfer` | contractually moved (insurance / provider SLA), evidence named |
| `Avoid` | the exposing capability was removed from the scope |
| `Reject_Risk_Require_Mitigation` | NOT accepted — reopens Part 1 with your instruction (the ADR-005 reverse loop) |

Every entry carries `accepted_by_person`, `person_role`, `justification`,
`review_signpost`. A non-mitigated STATUTORY threat cannot be accepted or
transferred (G9) — the only way out is to mitigate.

## Human gate

Part 2's golden rule: the model computes and proposes; ONLY A PERSON signs
`steps/phase3b/risk_verdicts.json` (G-P3-B). Nothing here accepts a risk.

## Technology neutrality (R5) — write the second column

| Do not write | Write |
|---|---|
| *TLS 1.3, HTTPS, SSH* | authenticated and encrypted end-to-end communication channel |
| *AWS S3, Azure Blob* | External Object Storage Service |
| *Stripe, PayPal* | External Payment Gateway |
| *JWT, session cookies* | cryptographically signed, time-bound session authentication token |
| *PostgreSQL, MongoDB* | Internal Application Database |
| *MFA, 2FA* | a second, independent verification factor at authentication |

Name the property and the component's ROLE, never the product or protocol.

## Changelog

- 1.0.0 (2026-10-27): created for Onda D (Part 2 construction, ADR-012 + the
  2026-10-27 catalog ratification: CWE+CAPEC core; ATT&CK/D3FEND/ATLAS/EMB3D
  consultive; 3315 ids ingested from the local KG catalogs).
