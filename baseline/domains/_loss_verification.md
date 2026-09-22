# Exhaustive no-loss verification — original vs modular corpus

- Original: `..\methodology-main\00_METHODOLOGY\PREPROCESSING_by_domain\domains`
- Current modular baseline: `baseline\domains`
- Method: independent line-multiset analysis (`scripts/verify_no_loss.py`); no modularize_domains.py logic reused (anti-circular, R10).

| Check | Result |
|---|---|
| Sub-domains verified | 38 |
| A. Annotation fidelity (original → annotated snapshot) | skipped |
| B. Uncovered original lines | **2** (required: 0) |
| B. Intentional dedup (Part 3 ≡ Part 1 §1, set-covered) | 2 lines |
| B. Blank-line surplus (layout only) | 17564 lines |
| B. Output surplus (duplication + boilerplate) | 10134 lines |
| B. Unclassified output lines | **919** (required: 0) |
| C. Article copies identical | 0/623 (differ 623, missing 0) |
| D. Manifests equal (ex `modular_layout`, CSF-token-insensitive) | 0/10 |
| G. R2b unresolvable CSF anchors (regs/cross/objective/manifests) | **0** (required: 0) — see _csf_anchor_normalization.md |
| G. R2b unresolvable PF/AI RMF anchors (regs/manifests) | **0** (required: 0) — referentials in baseline/CONTROLS |
| H. Crosswalk contradictions (regs anchor surfaces vs dashboards) | **0** (required: 0) — see _control_uniformization.md |
| E. Original-only files (non-merged) | 0 |
| F. Merged files replaced by modules | 38 (content verified line-by-line above) |
| F. New modular files | 693 |

## Per-subdomain line accounting

| Sub-domain | Orig lines | Target files | Uncovered | Dedup surplus | Out surplus | Unclassified |
|---|---|---|---|---|---|---|
| D-01.1 | 3070 | 19 | 0 | 0 | 295 | 29 |
| D-01.2 | 1669 | 16 | 0 | 0 | 229 | 23 |
| D-01.3 | 1575 | 16 | 0 | 0 | 229 | 23 |
| D-01.4 | 2072 | 19 | 0 | 0 | 285 | 28 |
| D-02.1 | 5275 | 23 | 0 | 0 | 357 | 30 |
| D-02.2 | 1335 | 14 | 0 | 0 | 186 | 26 |
| D-02.3 | 1576 | 14 | 0 | 0 | 192 | 17 |
| D-02.4 | 1806 | 16 | 0 | 0 | 224 | 23 |
| D-03.1 | 4872 | 19 | 0 | 0 | 308 | 28 |
| D-03.2 | 1732 | 19 | 0 | 0 | 258 | 28 |
| D-03.3 | 2514 | 19 | 0 | 0 | 277 | 28 |
| D-03.4 | 1620 | 14 | 0 | 0 | 208 | 22 |
| D-04.1 | 2297 | 19 | 0 | 0 | 285 | 24 |
| D-04.2 | 2542 | 19 | 0 | 0 | 284 | 23 |
| D-04.3 | 7424 | 23 | 0 | 0 | 423 | 30 |
| D-04.4 | 2707 | 19 | 0 | 0 | 277 | 23 |
| D-05.1 | 2646 | 16 | 0 | 0 | 274 | 22 |
| D-05.2 | 1704 | 16 | 0 | 0 | 240 | 22 |
| D-05.3 | 1595 | 14 | 2 | 2 | 199 | 27 |
| D-05.4 | 755 | 13 | 0 | 0 | 145 | 10 |
| D-06.1 | 2221 | 19 | 0 | 0 | 265 | 24 |
| D-06.2 | 875 | 13 | 0 | 0 | 129 | 10 |
| D-06.3 | 3889 | 19 | 0 | 0 | 312 | 27 |
| D-06.4 | 3089 | 13 | 0 | 0 | 216 | 27 |
| D-07.1 | 3775 | 23 | 0 | 0 | 370 | 34 |
| D-07.2 | 993 | 16 | 0 | 0 | 216 | 30 |
| D-07.3 | 734 | 14 | 0 | 0 | 165 | 20 |
| D-07.4 | 1273 | 14 | 0 | 0 | 188 | 18 |
| D-08.1 | 2364 | 22 | 0 | 0 | 295 | 25 |
| D-08.2 | 2529 | 23 | 0 | 0 | 318 | 23 |
| D-08.3 | 1078 | 14 | 0 | 0 | 184 | 13 |
| D-09.1 | 8292 | 23 | 0 | 0 | 422 | 28 |
| D-09.2 | 6298 | 23 | 0 | 0 | 373 | 28 |
| D-09.3 | 4008 | 16 | 0 | 0 | 245 | 18 |
| D-09.4 | 7955 | 23 | 0 | 0 | 394 | 26 |
| D-10.1 | 4208 | 23 | 0 | 0 | 316 | 27 |
| D-10.2 | 2004 | 20 | 0 | 0 | 267 | 24 |
| D-10.3 | 2046 | 23 | 0 | 0 | 284 | 31 |

## Output-surplus classification (all lines)

- generated banner: 3188
- generated section header: 1602
- crossref attribution header: 1286
- module title: 650
- generated index/module link row: 465
- purity stamp: 374
- re-levelled heading (source title): 344
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
- generated PF YAML anchor key: 29
- generated AI RMF YAML anchor key: 15
- M13 nomenclature rename artefact: 1

## Verification log

- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_24.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_25.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/NIS2_Art_13.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/NIS2_Art_14.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.1/articles/NIS2_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.2/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_25.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_34.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_12.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_16.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_19.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_21.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_24.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-01_Data-Protection/D-01.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_10.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_17.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_4.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_55.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_73.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_45.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_8.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_23.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_33.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/CRA_Art_7.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_16.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_17.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/CRA_Art_24.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.3/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_24.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_25.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_26.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_27.md
- ARTICLE DIFFERS: D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_12.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_15.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_49.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_52.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_7.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_8.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.2/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/GDPR_Art_29.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.3/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/CRA_Art_7.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/GDPR_Art_25.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-03_Access-Control/D-03.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/CRA_Art_25.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_10.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_14.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_18.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_23.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_3.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.1/articles/NIS2_Art_6.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_20.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_22.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_11.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_12.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/GDPR_Art_34.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.2/articles/NIS2_Art_6.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_14.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_3.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_55.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_64.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_73.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/AI_Act_Art_99.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_15.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_16.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_17.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_23.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_24.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/CRA_Art_6.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_14.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_18.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_23.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_3.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/DORA_Art_72.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_12.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_15.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_16.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_17.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_18.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_27.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_34.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_36.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_55.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_56.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_7.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/NIS2_Art_19.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/NIS2_Art_23.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/NIS2_Art_33.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.3/articles/NIS2_Art_6.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_11.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_12.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/GDPR_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/NIS2_Art_23.md
- ARTICLE DIFFERS: D-04_Incident-Response/D-04.4/articles/NIS2_Art_6.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/AI_Act_Art_10.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_12.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_16.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_19.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_25.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_52.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_89.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.1/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_10.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_12.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_19.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/AI_Act_Art_5.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/GDPR_Art_30.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.2/articles/GDPR_Art_89.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_11.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_15.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_16.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_17.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_18.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_19.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.3/articles/GDPR_Art_7.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_15.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_20.md
- ARTICLE DIFFERS: D-05_Data-Lifecycle/D-05.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/DORA_Art_30.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.2/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/CRA_Art_19.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/CRA_Art_20.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_24.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_30.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_32.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_44.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_45.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_46.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_47.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_48.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_49.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_63.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/NIS2_Art_22.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.3/articles/NIS2_Art_24.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_18.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_22.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_23.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/DORA_Art_30.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/GDPR_Art_10.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/GDPR_Art_27.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/GDPR_Art_3.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-06_Supply-Chain/D-06.4/articles/NIS2_Art_23.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_10.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_13.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_14.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_17.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_43.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/DORA_Art_15.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/GDPR_Art_25.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/GDPR_Art_34.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/NIS2_Art_14.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.2/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.2/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.2/articles/AI_Act_Art_73.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.2/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_17.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_4.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_55.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.3/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/CRA_Art_22.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-07_Secure-Development/D-07.4/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_39.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_29.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_36.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_39.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/NIS2_Art_20.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/AI_Act_Art_13.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/AI_Act_Art_14.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/AI_Act_Art_26.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/AI_Act_Art_27.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_39.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/GDPR_Art_39.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/NIS2_Art_20.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.2/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.3/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.3/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.3/articles/DORA_Art_91.md
- ARTICLE DIFFERS: D-08_Human-Factors/D-08.3/articles/NIS2_Art_20.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_14.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_17.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_26.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_27.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_43.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_17.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_24.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/CRA_Art_8.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_3.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_10.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_24.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_27.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_3.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_30.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_36.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_37.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_38.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_39.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_44.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_45.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_46.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_47.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_49.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_58.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_63.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_7.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_8.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_83.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_89.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_18.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_19.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_20.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_23.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.1/articles/NIS2_Art_33.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_4.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_8.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_10.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_15.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_26.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_27.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_36.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_37.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_39.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.2/articles/NIS2_Art_22.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_28.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_30.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_8.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_18.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_20.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.3/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_12.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_16.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_17.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_18.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_19.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_22.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_23.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_28.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_3.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_30.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/CRA_Art_8.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_12.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_13.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_14.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_30.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_31.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-09_Governance-Documentation/D-09.4/articles/NIS2_Art_24.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_15.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_72.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_73.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_74.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_83.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/CRA_Art_25.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_10.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_13.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_17.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_45.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_7.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_8.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_28.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_33.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_4.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.1/articles/NIS2_Art_21.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_12.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_19.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_23.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/AI_Act_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_13.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/CRA_Art_14.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_6.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/DORA_Art_9.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_24.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_30.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_31.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_58.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_83.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.2/articles/GDPR_Art_89.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/AI_Act_Art_9.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_27.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_32.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/CRA_Art_8.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_21.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_24.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_25.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_26.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_27.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/DORA_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_32.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_35.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_5.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_6.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/GDPR_Art_9.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/NIS2_Art_18.md
- ARTICLE DIFFERS: D-10_Monitoring-Audit/D-10.3/articles/NIS2_Art_21.md
- MANIFEST DIFFERS: D-01_Data-Protection/D-01.manifest.json keys=['sub_objectives_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-02_Vulnerability-Management/D-02.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-03_Access-Control/D-03.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation']
- MANIFEST DIFFERS: D-04_Incident-Response/D-04.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-05_Data-Lifecycle/D-05.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-06_Supply-Chain/D-06.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation']
- MANIFEST DIFFERS: D-07_Secure-Development/D-07.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-08_Human-Factors/D-08.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-09_Governance-Documentation/D-09.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']
- MANIFEST DIFFERS: D-10_Monitoring-Audit/D-10.manifest.json keys=['sub_objectives_by_regulation', 'applicable_nist_controls_by_regulation', 'applicable_pf_controls_by_regulation', 'applicable_airmf_controls_by_regulation']

## Verdict

**FAILURES FOUND** — every original line is either present verbatim in the modular output, or accounted as intentional deduplication of byte-identical Part 3 copies / blank-line layout / regenerated summary indexes (originals preserved in the source repo and git history).

