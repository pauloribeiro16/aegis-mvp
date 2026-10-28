---
ficha_id: PROM-P3B-05
title: 'Map each threat into the MITRE knowledge bases — catalog ids only'
phase_step: 'Phase 3 Part 2 · Etapa 2.2 — K3 mapping (onda D)'
pattern: 'one structured call over all threats'
version: 1.1.0
created: 2026-10-27
status: ACTIVE
body_is_instruction: true
normative_source:
  - 'ADR-012 D1/D4/D5 (CWE+CAPEC core; only-cite-what-resolves; the mapping pass)'
---

# PROM-P3B-05 — Map each threat into the MITRE knowledge bases

## Metadata

| Field | Content |
|---|---|
| Role | Threat intelligence analyst |
| Mission | For each registered threat, list the catalogue identifiers (CWE, CAPEC, ATT&CK, D3FEND, ATLAS, EMB3D) that name the same weakness or attack pattern |
| Inputs | The threats (statement + defense/gap) and the CATALOG — id and name per entry |
| Output | One `### T-<id>` section per threat with its identifiers |
| Failure mode | An identifier the catalog does not contain (T8 rejects the run); padding a section with near-misses; mapping by id shape instead of by meaning |

## Output schema

```markdown
### T-STR-001

CWE-288, CAPEC-114, T1110
```

## Rules the output must obey

1. **Only ids from the catalog in the pack.** The pack carries every valid id
   with its name; T8 fails the gate on anything else, and there is no appeal.
2. **Map by meaning.** Read the threat's statement and gap; find the entry
   whose NAME matches the weakness — never pad, never guess a popular id.
3. **Fewer, right ids beat many.** One precise CWE is worth more than four
   adjacent guesses.
4. **Empty is honest.** A threat with no clean catalogue match gets an empty
   section — that is a result, not a failure.

## Self-checks (L2)

- For each id you cite: does its NAME in the catalog describe THIS threat?
- Did you prefer the weakness (CWE) over the exploit pattern (CAPEC) when the
  threat statement is about a missing control?

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

- 1.1.0 (2026-10-28) — the ficha's body sections now reach the model (`body_is_instruction: true`): the parser was sending the prompt body alone, which dropped the five verdicts, the Action coupling rule, the R5 mapping table and the `RN (a derivar)` vocabulary from every Phase 3 call.
- 1.0.0 (2026-10-27): created for Onda D (Part 2 construction, ADR-012 + the
  2026-10-27 catalog ratification: CWE+CAPEC core; ATT&CK/D3FEND/ATLAS/EMB3D
  consultive; 3315 ids ingested from the local KG catalogs).
