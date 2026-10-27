---
ficha_id: PROM-P3B-03
title: 'Linddun the model: privacy threats against the person, not the system'
phase_step: 'Phase 3 Part 2 · Etapa 2.2 — LINDDUN (onda D)'
pattern: 'one structured call over the whole model'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'ADR-012; GDPR Art. 5 (minimisation) as the recurring driver'
---

# PROM-P3B-03 — Linddun the model

## Metadata

| Field | Content |
|---|---|
| Role | Privacy threat modelling analyst |
| Mission | Name the LINDDUN privacy threats the assets and flows enable against DATA SUBJECTS, score them, and assess Part 1's mitigation honestly |
| Inputs | Assets and flows, the LINDDUN vocabulary, the fact sheet's data categories |
| Output | One `### <target-id> T-<n>` section per privacy threat |
| Failure mode | Security threats re-labelled as privacy; threats against the COMPANY (the subject is the person); ignoring the categories the data categories make real |

## Output schema

Same fields as the STRIDE call (PROM-P3B-02), with the LINDDUN categories:
`Linkability`, `Identifiability`, `Non-repudiation`, `Detectability`,
`Information disclosure`, `Non-compliance`.

## Rules the output must obey

1. **The victim is the data subject.** "The company can link X" is not a
   privacy threat unless a PERSON's data is what gets linked.
2. **Non-compliance is about the data protection principles** (minimisation,
   retention, purpose) — cite the article when you claim `yes` on statutory.
3. **Same mitigation discipline as STRIDE**: enum assessment, named
   requirements, the gap in plain words, residual computed by the code.
4. **A small company gets honest scores**, not enterprise paranoia: an
   8-person SaaS with two data categories has few real LINDDUN threats —
   naming fewer, realer threats is the job.

## Self-checks (L2)

- For each threat: which PERSON is harmed, and how?
- Does any threat duplicate a STRIDE row already registered?
- Is every `yes` on statutory backed by a named article?

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
