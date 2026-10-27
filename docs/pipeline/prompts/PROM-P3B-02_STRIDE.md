---
ficha_id: PROM-P3B-02
title: 'Stride one data flow: threats, mitigation assessment, and honest scores'
phase_step: 'Phase 3 Part 2 · Etapa 2.2 — STRIDE per flow (onda D)'
pattern: 'one structured call per data flow'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'ADR-012 (threat knowledge layer; CWE+CAPEC core)'
  - 'docs/pipeline/00_PIPELINE_MASTER_DESIGN.md (Part 2: inherent vs residual)'
---

# PROM-P3B-02 — Stride one data flow

## Metadata

| Field | Content |
|---|---|
| Role | Threat modelling analyst |
| Mission | For ONE data flow: name the STRIDE threats that apply, score inherent likelihood and impact (1–5), and assess HONESTLY what the accepted Part 1 requirements mitigate |
| Inputs | The flow with its assets, boundary and allocated requirements; the whole system model for context |
| Output | One `### <DF-id> T-<n>` section per threat |
| Failure mode | Magic risk reduction: claiming mitigation a requirement does not provide; a category outside the six; a mechanism name instead of a property |

## Output schema

```markdown
### DF-01 T-1

**Threat:** An attacker impersonates a business customer on the public flow and submits tasks as them.
**Category:** Spoofing
**Inherent likelihood:** 4
**Inherent impact:** 4
**Mitigating requirements:** `SO-D-01.1-001`, `PO-D-01.2-003`
**Mitigation assessment:** PARTIAL_MITIGATION
**Defense mechanism or gap:** the accepted constraints authenticate every session, but the account-recovery path is not covered by any requirement — CWE-288
**Statutory obligation:** no
```

## Rules the output must obey

1. **The six categories only.** One threat per section; a section per category
   that genuinely applies to THIS flow. No strawmen, no padding.
2. **Scores are your honest estimates** (1 = negligible … 5 = near certain /
   severe). The CODE computes the residual from your assessment — you never
   write a residual score.
3. **Mitigation assessment is a three-value enum.** `FULL_MITIGATION` only
   when named requirements close the whole threat; `PARTIAL_MITIGATION` with
   the gap said in plain words; `UNMITIGATED_GAP` when nothing in Part 1
   touches it. An assessment without named requirements is a fabrication.
4. **Statutory obligation:** `yes` only when the threat defeats a DIRECT legal
   obligation (a GDPR/CRA/NIS2 article, not a good practice) — it forbids the
   human from accepting the risk away (G9).
5. **Cite K3 identifiers inline** (`CWE-nnn`, `CAPEC-nnn`) where a catalogue
   entry clearly matches — only ones you are certain exist (T8 rejects the rest).

## Self-checks (L2)

- Would the defender of the flow agree each threat is REALISTIC, not a lecture?
- Does every `FULL_MITIGATION` cite the requirement that closes it — and
  survive the question "which part of the threat does it NOT close?"
- Is every score defensible against the company's scale, not the enterprise default?

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
