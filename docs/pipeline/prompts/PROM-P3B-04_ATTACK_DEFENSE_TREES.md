---
ficha_id: PROM-P3B-04
title: 'Prove the cut: attack-defense trees for one Critical or High threat'
phase_step: 'Phase 3 Part 2 · Etapa 2.3 — ADTrees (onda D)'
pattern: 'one structured call per Critical/High threat'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'Kordy et al., attack–defense trees (foundation for the AND/OR cut semantics)'
  - 'the plan''s broken-path proof: an open path forbids a Low residual'
---

# PROM-P3B-04 — Prove the cut

## Metadata

| Field | Content |
|---|---|
| Role | Attack tree analyst |
| Mission | Decompose ONE threat into its attack steps (AND/OR), and mark every node a named Part 1 requirement actually cuts with `[DEF: <id>]` |
| Inputs | The threat, its claimed mitigators' constraint texts |
| Output | An indented tree; gates prefixed `(AND)`/`(OR)`; `[DEF: …]` markers on cut nodes |
| Failure mode | Marking a node DEF because the prose SAYS the requirement covers it; forgetting the alternative path (the OR branch) that no requirement touches |

## Output schema

```markdown
- (OR) Impersonate a business customer on DF-01
  - (AND) Obtain valid credentials
    - Guess credentials
    - [DEF: SO-D-01.1-001] Brute force the login form
  - [DEF: PO-D-01.2-003] Reuse a session token left in a shared browser
  - Enrol as a fake business customer during signup
```

## Rules the output must obey

1. **The marks are the proof.** The code computes open paths from the
   `[DEF]` markers — an unmarked leaf is an OPEN PATH, and the register will
   refuse a Low residual for the threat. Mark nothing you cannot defend.
2. **(AND) means all children needed; (OR) means any one suffices.** Default
   is OR when no gate is written.
3. **Decompose to the granularity where a requirement either cuts or does
   not** — no leaf finer than "a named requirement answers it", no branch
   coarser than one attacker goal.
4. **Include the paths you hope do not exist** — the signup path, the recovery
   path, the insider path. An audit reads the open paths first.

## Self-checks (L2)

- Is every `[DEF]` marker backed by a requirement named in the pack?
- Did you give the attacker every realistic entry, not only the flattering one?
- Would removing any one `[DEF]` visibly open a path?

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
