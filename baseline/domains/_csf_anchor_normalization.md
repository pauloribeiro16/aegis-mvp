# CSF anchor normalization ledger (R2b repair)

- Date: 2026-09-22
- Scope: `regs/*.md`, `cross/_interactions.md`, `D-*.manifest.json` (objective/cross/index layers).
- **Not** normalized: `articles/*.md` (verbatim inherited regulatory basis; never the objective anchor surface — SPEC §5 P4).
- Provenance: official v1.1->2.0 lineage read from the referential's own
  `informative_references` (`CSF v1.1:` entries); `PR.DS-12` is the corpus's
  internal 4x3-matrix cell, not a CSF ID (policy documented in
  `scripts/normalize_csf_anchors.py`).
- Verification: `scripts/verify_no_loss.py` applies this same map to the
  original corpus before comparison (documented normalization).

| Phantom | Replacement | Count | Rationale |
|---|---|---|---|

Total occurrences normalized: 0 in 6 files.

## Per-change log

| File | Line | Old | New |
|---|---|---|---|

