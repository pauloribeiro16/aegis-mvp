---
ficha_id: PROM-P3B-03
title: 'Linddun the model: privacy threats against the person, not the system'
phase_step: 'Phase 3 Part 2 · Etapa 2.2 — LINDDUN (onda D)'
pattern: 'one structured call over the whole model'
version: 1.2.0
created: 2026-10-27
status: ACTIVE
body_is_instruction: true
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

One `### <target> T-<n>` section per privacy threat, with these exact bold
fields (the same anatomy as the STRIDE call, LINDDUN categories):

```markdown
### OWNER T-1

**Threat:** The billing platform can link the owner's identity documents to the behavioural profile of a named customer without a lawful basis.
**Category:** Linkability
**Inherent likelihood:** 3
**Inherent impact:** 4
**Mitigating requirements:** `SO-D-01.1-001`
**Mitigation assessment:** PARTIAL_MITIGATION
**Defense mechanism or gap:** the accepted constraints gate data access by role, but no requirement bounds profile linkage or retention of linked identifiers
**Statutory obligation:** no
```

The category is exactly one of `Linkability`, `Identifiability`,
`Non-repudiation`, `Detectability`, `Information disclosure`,
`Non-compliance`. The assessment is exactly one of `FULL_MITIGATION`,
`PARTIAL_MITIGATION`, `UNMITIGATED_GAP` — any assessment other than
`UNMITIGATED_GAP` must name the Part 1 requirements that mitigate. Scores
are integers 1–5.

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

- 1.2.0 (2026-10-30) — the output schema is now INLINE (concrete exemplar,
  the six LINDDUN categories and the three assessment enums). The measured
  failure this closes: the muse arm's first Part 2 run (job 2168250) failed
  the L0 twice with every field missing — the schema section said only
  "Same fields as the STRIDE call (PROM-P3B-02)", a pointer the model cannot
  open, so it guessed the field format.
- 1.1.0 (2026-10-28) — the ficha's body sections now reach the model (`body_is_instruction: true`): the parser was sending the prompt body alone, which dropped the five verdicts, the Action coupling rule, the R5 mapping table and the `RN (a derivar)` vocabulary from every Phase 3 call.
- 1.0.0 (2026-10-27): created for Onda D (Part 2 construction, ADR-012 + the
  2026-10-27 catalog ratification: CWE+CAPEC core; ATT&CK/D3FEND/ATLAS/EMB3D
  consultive; 3315 ids ingested from the local KG catalogs).
