# AEGIS — second round: the re-file maps, the continuation, and the guard

**Attached:** `aegis_review_bundle.tar.gz` — the four referentials under question
plus the NIST/OWASP ones your A1 touched, with the **per-control leaf JSONs as
plain files**, the eleven generator specs, the aggregators, the ADR, and the
Phase 3 gate modules.

---

## 0. Three corrections to the reading conditions of your A1 answer

**0.1 — You could not read the leaves.** The `.zip` you audited carried the
per-control JSONs as DEFLATE-compressed streams you could not decompress; your
own answer says so ("NOT VERIFIABLE … 600+ ficheiros comprimidos em fluxos
DEFLATE binários"). So the **published** column of your coverage table was your
knowledge of the standards — which is exactly what we needed and is now
transcribed into `docs/external_review/2026-10-21_EXTERNAL_A1_published_catalogues.md`
— but the **"ids in repo"** column came from file *names* and from your own
arithmetic, and several of those numbers are wrong. Verified locally:

| Your figure | Actual | Note |
|---|---|---|
| NIST SP 800-53 Rev 5 — 241 files | **274** | the 23 omissions you listed are genuinely absent, but the total was undercounted |
| NIST SSDF — 42 | **44 cards** | and you listed PO.1.3 as omitted: **PO.1.3 is present** |
| BSI — 31 files | **35** | your own table sums to 35 |
| QNRCS — absent from snapshot | correct **for `master`** | QNRCS (107 controls) exists on the branch; see 0.2 |
| ISO 27701 — 35 synthetic ids | correct | all 35 confirmed |
| NIST AI SSDF — 17, all `*.AI.*` | correct | confirmed |
| OWASP SAMM — 7 of 15 wrong | correct | exactly 7, and they are the seven you named |
| OWASP ASVS 83, ENISA 28 | correct | |

**0.2 — You read `master` (`3e293abd`).** The branch
`feat/phase3-part1-coverage-mapping` carries the Phase 3 Part 1 work and the
QNRCS referential, and it carries an amendment made today
(`ADR-2026-10-21_advisory-referential-nomenclature.md`): ISO/IEC 42001's
identifiers are already section-aligned to A.2–A.8, the BSI `CON` ids are
`CON.1`–`CON.3`, and the BSI `DER` family was renamed `IDM`. Read the branch,
and read the ADR: your A1 findings F-01 and F-03 describe the **pre-amendment**
state and their *published-side* content (the 38-control list, the layer map) is
what remains valuable.

**0.3 — The evidence rule still applies.** `path:line` and the literal quote for
every repository claim; a confidence grade for every claim about a standard;
`NOT VERIFIABLE` rather than a guess. Where your answer is a mapping, one row
per local card.

---

## 1. A1′ — the re-file maps (the deliverable we now need)

We have local cards and published controls; they are not the same population.
ISO/IEC 42001: 33 local against 38 published. ISO/IEC 27701: 35 against 49.
BSI: 35 against 111. A re-file therefore cannot be a renumbering — each local
card has to be adjudicated. For each of the three frameworks, one row per local
card:

`local id | local card text (first 12 words) | published id (or —) | decision | reason`

with `decision` one of:

- **ADOPT** — the card paraphrases that published control; it takes the published id.
- **DEMOTE** — the card has no published counterpart; it stays, with a local id
  and **no** published id asserted (the pattern ADR-014 D3 already used for the
  BSI `IDM` family).
- **DROP** — the card is covered by another card, or is a filler.

Then, per framework, **the published controls with no local card** — the coverage
gap in the other direction — and a one-line count of each decision class.

Two constraints on the mapping, so the answer is usable:

- **Map by content, not by position.** A local card that paraphrases a published
  control keeps its text and takes the published id; it does not take the
  published *text* (we do not have the standard and do not reproduce it).
- **Say when the content does not decide.** If two published controls are
  equally plausible for a card, or the local text spans two of them, write
  `AMBIGUOUS` with both candidates. A wrong ADOPT is worse than a DEMOTE,
  because a wrong id is a citation that cannot be resolved.

## 2. A1″ — the four NIST/OWASP referentials

Your A1 read these from file names. With the leaves attached, finish them:

- **NIST SSDF (SP 800-218 v1.1).** Our 44 cards: which are the five you named
  as Withdrawn (PW.3.1, PW.3.2, PW.4.2, PW.4.3, PW.5.2) and which of the two
  you named as non-existent (PS.2.2, PS.3.2)? And the full list of the 42
  **active** tasks, so we can see the whole gap at once.
- **NIST AI SSDF (SP 800-218A).** Map each of our 17 `.AI.` cards onto a
  published task id — the standard keeps the SSDF v1.1 ids and adds PW.1.4,
  PW.4.5 and RV.1.4 — or onto `—` if the card has no counterpart.
- **OWASP SAMM v2.0.** For each of our 15 cards, the published practice id
  (G-SM, G-PC, G-EG, D-TA, D-SR, D-SA, I-SB, I-SD, I-DM, V-AA, V-RT, V-ST,
  O-IM, O-EM, O-OM) and the stream sub-practice if one exists.
- **NIST SP 800-53 Rev 5.** Beyond the 23 you listed, the **complete** list of
  active base controls we are missing; the two withdrawn we instantiate
  (CA-04, RA-04) with the control that absorbed each; and one thing we need
  before we change anything: our ids are zero-padded (`AC-01`), because the
  anchor resolver in the pipeline matches two-digit suffixes and a test asserts
  that premise. **Is the padding a defect, or a convention we must keep and
  document?** If it is a defect, what breaks if we change it — and what is the
  cheapest way to keep both the published id and our resolver working?

## 3. A2 — architectural weaknesses visible to an examiner

Your answer was cut off at the first line of A2. Continue it, in the same
format: one paragraph per weakness — the claim, the `path:line` that shows it,
the mechanism, the consequence for the reader of the produced document — and no
refactoring proposal that does not name the contract it would break. The
contracts that exist and that a proposal must respect: R2a (a citation must
resolve to a file in the sub-domain's own `articles/`), the case-corpus
composition (regulation-pure, verbatim, no summaries), the n-ary interaction
layer (`cross/_interactions.md`), and the frozen baseline (amended only by a
recorded decision).

## 4. A4 — the roadmap

Ordered, cheapest first, respecting: three phases and no Phase 4; one human
decision (the seven principle verdicts) blocking the Phase 3 Part 1 gate; frozen
preregistrations; a frozen baseline amendable only by ADR. For each item: what
it unblocks, what it costs, what would make it unnecessary. Plus the
**"what we should stop doing"** list.

## 5. A5 — the thesis-facing risk list

Ranked. For each: the single sentence an examiner would say, whether the answer
is to fix, to reframe or to withdraw the claim, and what the fix costs.

## 6. A6 — the guard

This is the question we would most like answered, because it is the one that
turns this exercise into a permanent protection rather than a one-off cleanup.

Every defect you found had the same shape: **an identifier that resolves to a
file but points at the wrong place in the standard.** Our own checker (R2b)
verifies that a cited advisory id *exists*; `verify_no_loss.py` does not cover
the advisory tier at all. So a referential can be mechanically clean and
normatively wrong, which is the same shape as the Phase 3 finding that the
coverage judge is asked to measure against verification criteria it never
receives.

**What would the guard be?** We imagine a published-identifier table per
referential (the list you just produced is the seed of it) checked by a
deterministic script: every `control_id` in `baseline/CONTROLS/<FW>/` must be a
member of the published set for that standard, and every published control we
choose to cite must exist as a file. Answer concretely:

1. Where should the published sets live so that the check is a *pure function of
   the repository* — a data file next to the spec, a separate registry, or
   something else — and what is the smallest format that survives a standard
   revision?
2. What is the exact assertion, in one or two lines, that fails when a control
   id is invented, when a published control is silently dropped, and when a
   referential drifts from its own spec?
3. What does the check **not** catch, and what would still need a human?

---

## Output format

Answer in this order, with these headings, no preamble, no closing summary:

1. **A1′** — three mapping tables (42001, 27701, BSI) + the three
   coverage-gap lists + the decision counts.
2. **A1″** — the four NIST/OWASP answers, each with the complete published list
   and the per-card decision.
3. **A2** — the weaknesses.
4. **A4** — the roadmap.
5. **A5** — the thesis risk list.
6. **A6** — the guard: placement, assertion, and residual blind spots.
7. **Where you were wrong before** — every point of your first answer you now
   revise, with your own `path:line`. Do not silently comply: §0 is our reading
   of your work, not a script.

If you cannot settle something, say so in one line and continue. A wrong
identifier is worse than a missing one, because we act on it.
