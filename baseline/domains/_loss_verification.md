# Exhaustive no-loss verification — original vs modular corpus

- Original: `..\methodology-main\00_METHODOLOGY\PREPROCESSING_by_domain\domains`
- Current modular baseline: `baseline\domains`
- Method: independent line-multiset analysis (`scripts/verify_no_loss.py`); no modularize_domains.py logic reused (anti-circular, R10).

| Check | Result |
|---|---|
| Sub-domains verified | 38 |
| A. Annotation fidelity (original → annotated snapshot) | skipped |
| B. Uncovered original lines | **0** (required: 0) |
| B. Intentional dedup (Part 3 ≡ Part 1 §1, set-covered) | 0 lines |
| B. Blank-line surplus (layout only) | 17564 lines |
| B. Output surplus (duplication + boilerplate) | 9021 lines |
| B. Unclassified output lines | **0** (required: 0) |
| C. Article copies identical | 623/623 (differ 0, missing 0) |
| D. Manifests equal (ex `modular_layout`, CSF-token-insensitive) | 10/10 |
| G. R2b unresolvable CSF anchors (regs/cross/objective/manifests) | **0** (required: 0) — see _csf_anchor_normalization.md |
| G. R2b unresolvable PF/AI RMF anchors (regs/manifests) | **0** (required: 0) — referentials in baseline/CONTROLS |
| H. Crosswalk contradictions (regs anchor surfaces vs dashboards) | **0** (required: 0) — see _control_uniformization.md |
| E. Original-only files (non-merged) | 0 |
| F. Merged files replaced by modules | 38 (content verified line-by-line above) |
| F. New modular files | 690 |

## Per-subdomain line accounting

| Sub-domain | Orig lines | Target files | Uncovered | Dedup surplus | Out surplus | Unclassified |
|---|---|---|---|---|---|---|
| D-01.1 | 3070 | 19 | 0 | 0 | 261 | 0 |
| D-01.2 | 1669 | 16 | 0 | 0 | 202 | 0 |
| D-01.3 | 1575 | 16 | 0 | 0 | 202 | 0 |
| D-01.4 | 2072 | 19 | 0 | 0 | 251 | 0 |
| D-02.1 | 5275 | 23 | 0 | 0 | 320 | 0 |
| D-02.2 | 1335 | 14 | 0 | 0 | 155 | 0 |
| D-02.3 | 1576 | 14 | 0 | 0 | 173 | 0 |
| D-02.4 | 1806 | 16 | 0 | 0 | 196 | 0 |
| D-03.1 | 4872 | 19 | 0 | 0 | 275 | 0 |
| D-03.2 | 1732 | 19 | 0 | 0 | 225 | 0 |
| D-03.3 | 2514 | 19 | 0 | 0 | 244 | 0 |
| D-03.4 | 1620 | 14 | 0 | 0 | 181 | 0 |
| D-04.1 | 2297 | 19 | 0 | 0 | 256 | 0 |
| D-04.2 | 2542 | 19 | 0 | 0 | 256 | 0 |
| D-04.3 | 7424 | 23 | 0 | 0 | 385 | 0 |
| D-04.4 | 2707 | 19 | 0 | 0 | 249 | 0 |
| D-05.1 | 2646 | 16 | 0 | 0 | 247 | 0 |
| D-05.2 | 1704 | 16 | 0 | 0 | 213 | 0 |
| D-05.3 | 1595 | 14 | 0 | 0 | 166 | 0 |
| D-05.4 | 755 | 13 | 0 | 0 | 133 | 0 |
| D-06.1 | 2221 | 19 | 0 | 0 | 236 | 0 |
| D-06.2 | 875 | 13 | 0 | 0 | 118 | 0 |
| D-06.3 | 3889 | 19 | 0 | 0 | 280 | 0 |
| D-06.4 | 3089 | 13 | 0 | 0 | 184 | 0 |
| D-07.1 | 3775 | 23 | 0 | 0 | 329 | 0 |
| D-07.2 | 993 | 16 | 0 | 0 | 182 | 0 |
| D-07.3 | 734 | 14 | 0 | 0 | 143 | 0 |
| D-07.4 | 1273 | 14 | 0 | 0 | 168 | 0 |
| D-08.1 | 2364 | 22 | 0 | 0 | 265 | 0 |
| D-08.2 | 2529 | 23 | 0 | 0 | 283 | 0 |
| D-08.3 | 1078 | 14 | 0 | 0 | 169 | 0 |
| D-09.1 | 8292 | 23 | 0 | 0 | 387 | 0 |
| D-09.2 | 6298 | 23 | 0 | 0 | 338 | 0 |
| D-09.3 | 4008 | 16 | 0 | 0 | 224 | 0 |
| D-09.4 | 7955 | 23 | 0 | 0 | 362 | 0 |
| D-10.1 | 4208 | 23 | 0 | 0 | 282 | 0 |
| D-10.2 | 2004 | 20 | 0 | 0 | 236 | 0 |
| D-10.3 | 2046 | 23 | 0 | 0 | 245 | 0 |

## Output-surplus classification (all lines)

- generated banner: 3184
- generated section header: 1602
- crossref attribution header: 1286
- module title: 650
- generated index/module link row: 465
- purity stamp: 374
- re-levelled heading (source title): 343
- generated control-anchor line: 245
- generated placeholder/note: 197
- dedup note continuation: 142
- reconstructed table header: 129
- generated bullet: 114
- details wrapper: 76
- generated PF/AIRMF anchors header: 39
- generated PF/AIRMF anchors list: 39
- modules table header: 38
- details fence: 38
- control-anchors marker: 31
- table separator: 29

## Verdict

**NO INFORMATION LOST** — every original line is either present verbatim in the modular output, or accounted as intentional deduplication of byte-identical Part 3 copies / blank-line layout / regenerated summary indexes (originals preserved in the source repo and git history).

