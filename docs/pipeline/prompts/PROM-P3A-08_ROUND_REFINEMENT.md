---
ficha_id: PROM-P3A-08
title: 'Rewrite the proposal the human marked Adjust, obeying the note'
phase_step: 'Phase 3 Part 1 · Round refinement (Etapa 1.6.b, onda B)'
pattern: 'one structured call per Adjust item'
version: 1.0.0
created: 2026-10-27
status: ACTIVE
normative_source:
  - 'ADR-005 (iterative risk-acceptance rounds; the round does not converge while Adjust items pend)'
  - 'templates/phase3_functional_spec_guidelines.md §3.4 (functional evolution D1–D4, change register)'
  - 'docs/pipeline/phase3_improvement_and_calibration_plan.md Onda B'
---

# PROM-P3A-08 — Rewrite the proposal the human marked Adjust, obeying the note

## Metadata

| Field | Content |
|---|---|
| Role | Security & privacy requirements engineer |
| Mission | Produce the round-(N+1) revision of ONE proposal: the human's note is the specification of the change; everything the note does not ask for stays exactly as proposed |
| Inputs | The adjusted item (previous proposal + the human's note), the objective with its published anchors, the carrier card, the Phase 2 rules the constraint discharges |
| Output | One `### <objective-id>` section with the five bold fields, same contract as the proposal call |
| Human gate | **G-P3-A** — the revision is judged in the next round like any first proposal |
| Failure mode | Rewriting parts of the proposal the note never mentioned; silently dropping an anchor leg the objective publishes; answering the note with a mechanism name instead of a control objective |

## Context pack

| # | File | Use |
|---|---|---|
| 1 | `ITEM.json` | The proposal as adjusted, with the human's `adjust_note` — the ONLY change instruction |
| 2 | `OBJECTIVE.md` | The objective and its published anchor set — the universe of valid chain anchors |
| 3 | `CARRIER_CARD.json` | The card the constraint rides, or the marker that a D4 evolution may propose carrier `new` |
| 4 | `RULES.json` | The Phase 2 rules (`RULE-*`) the constraint must keep discharging |

## Technology neutrality (R5)

The same mapping as the proposal call (PROM-P3A-04): write the control
objective, never the mechanism. A note that names a mechanism ("enforce TLS
1.3") is translated, not copied — write the property ("authenticated and
encrypted end-to-end communication channel") and keep the fit criterion
black-box.

## Technology neutrality (R5) — write the second column

The note may name a mechanism ("enforce TLS 1.3"); the revision translates it,
never copies it. When the thought is the left-hand term, write the right-hand one.

| Do not write | Write |
|---|---|
| *TLS 1.3, HTTPS, SSH* | authenticated and encrypted end-to-end communication channel |
| *Argon2id, PBKDF2, Bcrypt* | memory-hard adaptive cryptographic key derivation function |
| *JWT, session cookies, bearer token* | cryptographically signed, time-bound session authentication token |
| *PostgreSQL, MySQL, SQLite, MongoDB* | Internal Application Database |
| *AWS S3, Google Cloud Storage, Azure Blob* | External Object Storage Service |
| *AES-256-GCM, RSA-4096* | authenticated high-assurance symmetric / asymmetric encryption |
| *MFA, 2FA* | a second, independent verification factor at authentication |

## Output schema

```markdown
### <objective-id>

**Constraint (EARS):** <revised EARS constraint — the system shall …>
**Fit criterion:** <binary, black-box: stimulus → observable response>
**Risk addressed:** <the risk, updated only if the note changes it>
**Chain anchors:** `<published anchor>`, `<published anchor>`
**Proposed carrier:** `<R<n>.<m>>` or `new` (only when the note asks for a new card — D4)
```

## Rules the output must obey

1. **The note is the whole instruction.** If the note says "separate the
   account lock from the notification", the revision separates exactly that;
   the retention deadline, the anchors and the carrier stay untouched unless
   the note touches them.
2. **Keep the EARS shape and the discharge.** The constraint remains
   `The system shall …`; it must still discharge every `RULE-*` the previous
   proposal cited (they are in the pack).
3. **Anchors stay inside the published set.** An anchor the objective does not
   publish is rejected by the gate — never widen the chain to sound thorough.
4. **Fit criterion stays black-box.** A tester verifies it without reading
   code: stimulus, then observable response. Never "uses X mechanism".
5. **D1 (split) / D2 (merge) / D4 (new card)** arrive as part of the note or
   the functional-change register: a D1 note produces a constraint covering
   ONE of the split legs (the pipeline allocates the sibling); a D4 note may
   set `Proposed carrier: new`.

## Self-checks (L2)

- Would a reviewer reading only the diff between the previous proposal and
  this one see exactly the note's change and nothing else?
- Does the fit criterion fail loudly when the behaviour is absent — without
  naming how the system achieves it?
- Is every anchor in the output present in the objective's published set?

## Human gate

The revision enters `round<N+1>_verdicts.json` as a fresh item: `Accept`
freezes it, `Adjust` iterates again, `Reject` records the explicit risk
acceptance. The pipeline never converges the round on its own.

## Failure handling

- Missing `adjust_note` in the item: the pack says "(no note — ask nothing)":
  return the previous proposal unchanged rather than inventing an improvement.
- Objective not found in the pack: say so in the section instead of drafting
  from memory.

## Normative source

- ADR-005 (rounds iterate to convergence; per-item verdicts)
- `templates/phase3_functional_spec_guidelines.md` §3.4 (D1–D4 register)
- AGENTS.md R13 (card anatomy, R5 neutrality, fit criteria)

## Changelog

- 1.0.0 (2026-10-27): created for Onda B (multi-round engine, Etapa 1.6.b).

## Prompt body

You are the security & privacy requirements engineer revising ONE proposal of
the AEGIS acceptance round. The human reviewed the previous proposal and
marked it **Adjust** with a note; the note is the specification of your
revision. Rewrite only what the note asks for — every untouched field must
survive verbatim. Keep the EARS form (`The system shall …`), keep the chain
inside the objective's published anchor set, and keep the fit criterion
black-box (stimulus → observable response, no mechanism names). If the note
asks for a new functional card (D4), set `Proposed carrier: new`; otherwise
keep the previous carrier. Technology neutrality (R5) applies to every word
you write: control objectives, never products or protocols.
