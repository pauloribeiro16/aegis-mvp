# CSF anchor list deduplication ledger (literal duplicates)

- Date: 2026-09-22
- Scope: `baseline/domains/D-*/D-*.[0-9]*/regs/*.md` (Sub-SO **CSF anchors** lines + Volere `nist_csf:` YAML).
- Algorithm: dedupe adjacent identical CSF IDs in the same objective's anchor list, preserving first-occurrence order. Non-adjacent semantic-equivalence dedup is NOT performed (would require the official CSF crosswalk).
- Idempotent.

- Files touched: **0**
- Lines changed: **0**

## Per-change log

| File | Line | Before | After |
|---|---|---|---|

