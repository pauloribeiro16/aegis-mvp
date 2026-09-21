# Exhaustive no-loss verification — original vs modular corpus

- Original: `..\methodology-main\00_METHODOLOGY\PREPROCESSING_by_domain\domains`
- Current modular baseline: `baseline\domains`
- Method: independent line-multiset analysis (`scripts/verify_no_loss.py`); no modularize_domains.py logic reused (anti-circular, R10).

| Check | Result |
|---|---|
| Sub-domains verified | 38 |
| A. Annotation fidelity (original → annotated snapshot) | **0 failures** — snapshot = original + tag lines only |
| B. Uncovered original lines | **0** (required: 0) |
| B. Intentional dedup (Part 3 ≡ Part 1 §1, set-covered) | 3691 lines |
| B. Blank-line surplus (layout only) | 16886 lines |
| B. Output surplus (duplication + boilerplate) | 10421 lines |
| B. Unclassified output lines | **0** (required: 0) |
| C. Article copies identical | 623/623 (differ 0, missing 0) |
| D. Manifests equal (ex `modular_layout`) | 10/10 |
| E. Original-only files (non-merged) | 0 |
| F. Merged files replaced by modules | 38 (content verified line-by-line above) |
| F. New modular files | 688 |

## Per-subdomain line accounting

| Sub-domain | Orig lines | Target files | Uncovered | Dedup surplus | Out surplus | Unclassified |
|---|---|---|---|---|---|---|
| D-01.1 | 3070 | 19 | 0 | 128 | 302 | 0 |
| D-01.2 | 1669 | 16 | 0 | 50 | 231 | 0 |
| D-01.3 | 1575 | 16 | 0 | 47 | 232 | 0 |
| D-01.4 | 2072 | 19 | 0 | 147 | 284 | 0 |
| D-02.1 | 5275 | 23 | 0 | 220 | 367 | 0 |
| D-02.2 | 1335 | 14 | 0 | 0 | 191 | 0 |
| D-02.3 | 1576 | 14 | 0 | 0 | 207 | 0 |
| D-02.4 | 1806 | 16 | 0 | 41 | 238 | 0 |
| D-03.1 | 4872 | 19 | 0 | 137 | 306 | 0 |
| D-03.2 | 1732 | 19 | 0 | 137 | 266 | 0 |
| D-03.3 | 2514 | 19 | 0 | 135 | 282 | 0 |
| D-03.4 | 1620 | 14 | 0 | 25 | 207 | 0 |
| D-04.1 | 2297 | 19 | 0 | 135 | 293 | 0 |
| D-04.2 | 2542 | 19 | 0 | 135 | 294 | 0 |
| D-04.3 | 7424 | 23 | 0 | 251 | 422 | 0 |
| D-04.4 | 2707 | 19 | 0 | 165 | 287 | 0 |
| D-05.1 | 2646 | 16 | 0 | 53 | 261 | 0 |
| D-05.2 | 1704 | 16 | 0 | 54 | 234 | 0 |
| D-05.3 | 1595 | 14 | 0 | 0 | 189 | 0 |
| D-05.4 | 755 | 13 | 0 | 0 | 139 | 0 |
| D-06.1 | 2221 | 19 | 0 | 135 | 275 | 0 |
| D-06.2 | 875 | 13 | 0 | 0 | 141 | 0 |
| D-06.3 | 3889 | 19 | 0 | 130 | 306 | 0 |
| D-06.4 | 3089 | 13 | 0 | 0 | 260 | 0 |
| D-07.1 | 3775 | 23 | 0 | 230 | 373 | 0 |
| D-07.2 | 993 | 16 | 0 | 50 | 221 | 0 |
| D-07.3 | 734 | 14 | 0 | 0 | 169 | 0 |
| D-07.4 | 1273 | 14 | 0 | 25 | 189 | 0 |
| D-08.1 | 2364 | 22 | 0 | 164 | 308 | 0 |
| D-08.2 | 2529 | 23 | 0 | 246 | 333 | 0 |
| D-08.3 | 1078 | 14 | 0 | 25 | 208 | 0 |
| D-09.1 | 8292 | 23 | 0 | 235 | 404 | 0 |
| D-09.2 | 6298 | 23 | 0 | 243 | 376 | 0 |
| D-09.3 | 4008 | 16 | 0 | 75 | 263 | 0 |
| D-09.4 | 7955 | 23 | 0 | 273 | 399 | 0 |
| D-10.1 | 4208 | 23 | 0 | 0 | 351 | 0 |
| D-10.2 | 2004 | 20 | 0 | 0 | 294 | 0 |
| D-10.3 | 2046 | 23 | 0 | 0 | 319 | 0 |

## Output-surplus classification (all lines)

- generated banner: 3184
- intentional duplication (exists in original): 1754
- generated section header: 1602
- crossref attribution header: 1286
- module title: 650
- generated index/module link row: 465
- purity stamp: 374
- re-levelled heading (source title): 343
- generated placeholder/note: 197
- dedup note continuation: 142
- reconstructed table header: 129
- generated bullet: 114
- details wrapper: 76
- modules table header: 38
- details fence: 38
- table separator: 29

## Verdict

**NO INFORMATION LOST** — every original line is either present verbatim in the modular output, or accounted as intentional deduplication of byte-identical Part 3 copies / blank-line layout / regenerated summary indexes (originals preserved in the source repo and git history).

