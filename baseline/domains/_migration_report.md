# Modularization migration report

- Sub-domains processed: 38
- Mode: APPLY
- Balanced line-accounting: 38/38
- Total dedup lines (Part 3 == Part 1 §1): 5884
- Total demoted cross-reference units: 1286

| Sub-domain | Lines | Routed | Dedup | Tags | Struct | Balanced | Modules | Pairs | Demoted |
|---|---|---|---|---|---|---|---|---|---|
| D-01.1 | 3120 | 2838 | 216 | 62 | 4 | OK | 19 | 6 | 42 |
| D-01.2 | 1703 | 1573 | 86 | 40 | 4 | OK | 16 | 3 | 19 |
| D-01.3 | 1609 | 1483 | 82 | 40 | 4 | OK | 16 | 3 | 25 |
| D-01.4 | 2122 | 1818 | 238 | 62 | 4 | OK | 19 | 6 | 30 |
| D-02.1 | 5345 | 4892 | 359 | 90 | 4 | OK | 23 | 10 | 52 |
| D-02.2 | 1357 | 1329 | 0 | 24 | 4 | OK | 14 | 1 | 13 |
| D-02.3 | 1598 | 1570 | 0 | 24 | 4 | OK | 14 | 1 | 19 |
| D-02.4 | 1840 | 1722 | 74 | 40 | 4 | OK | 16 | 3 | 24 |
| D-03.1 | 4922 | 4646 | 210 | 62 | 4 | OK | 19 | 6 | 54 |
| D-03.2 | 1782 | 1506 | 210 | 62 | 4 | OK | 19 | 6 | 19 |
| D-03.3 | 2564 | 2288 | 210 | 62 | 4 | OK | 19 | 6 | 30 |
| D-03.4 | 1642 | 1572 | 42 | 24 | 4 | OK | 14 | 1 | 25 |
| D-04.1 | 2347 | 2071 | 210 | 62 | 4 | OK | 19 | 6 | 31 |
| D-04.2 | 2592 | 2316 | 210 | 62 | 4 | OK | 19 | 6 | 37 |
| D-04.3 | 7494 | 7003 | 397 | 90 | 4 | OK | 23 | 10 | 100 |
| D-04.4 | 2757 | 2436 | 255 | 62 | 4 | OK | 19 | 6 | 32 |
| D-05.1 | 2680 | 2546 | 90 | 40 | 4 | OK | 16 | 3 | 41 |
| D-05.2 | 1738 | 1602 | 92 | 40 | 4 | OK | 16 | 3 | 22 |
| D-05.3 | 1617 | 1589 | 0 | 24 | 4 | OK | 14 | 1 | 16 |
| D-05.4 | 769 | 751 | 0 | 14 | 4 | OK | 13 | 0 | 4 |
| D-06.1 | 2271 | 1994 | 211 | 62 | 4 | OK | 19 | 6 | 23 |
| D-06.2 | 889 | 871 | 0 | 14 | 4 | OK | 13 | 0 | 2 |
| D-06.3 | 3939 | 3658 | 215 | 62 | 4 | OK | 19 | 6 | 47 |
| D-06.4 | 3116 | 3072 | 0 | 40 | 4 | OK | 13 | 6 | 23 |
| D-07.1 | 3845 | 3379 | 372 | 90 | 4 | OK | 23 | 10 | 52 |
| D-07.2 | 1027 | 901 | 82 | 40 | 4 | OK | 16 | 3 | 14 |
| D-07.3 | 756 | 728 | 0 | 24 | 4 | OK | 14 | 1 | 4 |
| D-07.4 | 1295 | 1226 | 41 | 24 | 4 | OK | 14 | 1 | 15 |
| D-08.1 | 2430 | 2090 | 258 | 78 | 4 | OK | 22 | 9 | 30 |
| D-08.2 | 2599 | 2135 | 380 | 80 | 4 | OK | 23 | 10 | 38 |
| D-08.3 | 1104 | 1031 | 41 | 28 | 4 | OK | 14 | 1 | 15 |
| D-09.1 | 8362 | 7889 | 379 | 90 | 4 | OK | 23 | 10 | 84 |
| D-09.2 | 6368 | 5897 | 377 | 90 | 4 | OK | 23 | 10 | 61 |
| D-09.3 | 4050 | 3875 | 123 | 48 | 4 | OK | 16 | 3 | 45 |
| D-09.4 | 8025 | 7517 | 424 | 80 | 4 | OK | 23 | 10 | 91 |
| D-10.1 | 4258 | 4204 | 0 | 50 | 4 | OK | 23 | 10 | 52 |
| D-10.2 | 2046 | 2000 | 0 | 42 | 4 | OK | 20 | 7 | 30 |
| D-10.3 | 2096 | 2042 | 0 | 50 | 4 | OK | 23 | 10 | 25 |

## Per-subdomain detail

### D-01.1

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=3, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=3, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 15, 'demoted_para': 14, 'demoted_quote': 1, 'cross_mentions_in_tables': 1}

### D-01.2

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/DORA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 8, 'demoted_bullet': 4, 'demoted_para': 6, 'demoted_quote': 1, 'cross_mentions_in_tables': 1}

### D-01.3

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/DORA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 9, 'demoted_para': 7, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-01.4

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/DORA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 11, 'demoted_para': 7, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-02.1

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=4, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=3, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 14, 'demoted_bullet': 8, 'demoted_para': 29, 'demoted_quote': 1, 'cross_mentions_in_tables': 1}

### D-02.2

- Files: _index.md, cross/CRA-DORA.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 6, 'demoted_bullet': 4, 'demoted_para': 3, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-02.3

- Files: _index.md, cross/CRA-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 6, 'demoted_bullet': 3, 'demoted_para': 10, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-02.4

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/CRA-DORA.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 8, 'demoted_para': 7, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-03.1

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 12, 'demoted_para': 29, 'demoted_quote': 1, 'cross_mentions_in_tables': 1}

### D-03.2

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 5, 'demoted_para': 2, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-03.3

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 14, 'demoted_para': 4, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-03.4

- Files: _index.md, cross/CRA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 6, 'demoted_bullet': 12, 'demoted_para': 7, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-04.1

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 12, 'demoted_para': 7, 'demoted_quote': 0, 'cross_mentions_in_tables': 1}

### D-04.2

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 15, 'demoted_para': 10, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-04.3

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=4, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 15, 'demoted_para': 65, 'demoted_quote': 5, 'cross_mentions_in_tables': 4}

### D-04.4

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 15, 'demoted_para': 4, 'demoted_quote': 1, 'cross_mentions_in_tables': 0}

### D-05.1

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-GDPR.md, cross/CRA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 20, 'demoted_para': 12, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-05.2

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-GDPR.md, cross/CRA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=1, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 8, 'demoted_para': 5, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-05.3

- Files: _index.md, cross/CRA-GDPR.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 6, 'demoted_bullet': 5, 'demoted_para': 5, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-05.4

- Files: _index.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=0, ambiguity=True), CRA (subso=0, reqs=0, verbatim=0, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 2, 'demoted_bullet': 0, 'demoted_para': 2, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-06.1

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=1, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 9, 'demoted_para': 2, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-06.2

- Files: _index.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=0, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 2, 'demoted_bullet': 0, 'demoted_para': 0, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-06.3

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=3, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 13, 'demoted_para': 19, 'demoted_quote': 3, 'cross_mentions_in_tables': 1}

### D-06.4

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/CRA.md, regs/DORA.md, regs/GDPR.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=False), CRA (subso=1, reqs=1, verbatim=3, ambiguity=False), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=False), DORA (subso=1, reqs=1, verbatim=2, ambiguity=False)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 8, 'demoted_para': 0, 'demoted_quote': 3, 'cross_mentions_in_tables': 0}

### D-07.1

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=3, ambiguity=True), CRA (subso=1, reqs=1, verbatim=3, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=3, ambiguity=True), DORA (subso=1, reqs=1, verbatim=4, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=3, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 17, 'demoted_para': 14, 'demoted_quote': 6, 'cross_mentions_in_tables': 2}

### D-07.2

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/CRA-DORA.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 4, 'demoted_para': 0, 'demoted_quote': 1, 'cross_mentions_in_tables': 0}

### D-07.3

- Files: _index.md, cross/CRA-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=0, reqs=0, verbatim=0, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 2, 'demoted_bullet': 2, 'demoted_para': 0, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-07.4

- Files: _index.md, cross/CRA-DORA.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=1, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 2, 'demoted_bullet': 7, 'demoted_para': 6, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-08.1

- Files: _index.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 13, 'demoted_para': 5, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}
- Script log:
  - D-08.1.md:L308: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-08.1.md:L1408: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-08.1: pair slot 'AI_Act' has regs=['AI_Act'] — routed to interactions

### D-08.2

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 19, 'demoted_para': 4, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

### D-08.3

- Files: _index.md, cross/DORA-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=0, reqs=0, verbatim=0, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=1, ambiguity=True), DORA (subso=1, reqs=1, verbatim=1, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 6, 'demoted_bullet': 5, 'demoted_para': 4, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}
- Script log:
  - D-08.3.md:L89: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-08.3.md:L780: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-08.3: pair slot 'AI_Act' has regs=['AI_Act'] — routed to interactions

### D-09.1

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=3, ambiguity=True), DORA (subso=1, reqs=1, verbatim=3, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=3, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 13, 'demoted_para': 54, 'demoted_quote': 2, 'cross_mentions_in_tables': 3}

### D-09.2

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 5, 'demoted_para': 39, 'demoted_quote': 2, 'cross_mentions_in_tables': 3}

### D-09.3

- Files: _index.md, cross/CRA-DORA.md, cross/CRA-NIS2.md, cross/DORA-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=0, reqs=0, verbatim=0, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=0, reqs=0, verbatim=0, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 9, 'demoted_bullet': 0, 'demoted_para': 35, 'demoted_quote': 1, 'cross_mentions_in_tables': 1}
- Script log:
  - D-09.3.md:L177: malformed tag '<!-- aegis:pair:GDPR, -->' (empty partner)
  - D-09.3.md:L185: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-09.3.md:L1003: malformed tag '<!-- aegis:pair:GDPR, -->' (empty partner)
  - D-09.3.md:L1011: malformed tag '<!-- aegis:pair:AI_Act, -->' (empty partner)
  - D-09.3: pair slot 'AI_Act' has regs=['AI_Act'] — routed to interactions
  - D-09.3: pair slot 'GDPR' has regs=['GDPR'] — routed to interactions

### D-09.4

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=3, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 10, 'demoted_para': 64, 'demoted_quote': 2, 'cross_mentions_in_tables': 4}

### D-10.1

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=3, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 1, 'demoted_para': 34, 'demoted_quote': 2, 'cross_mentions_in_tables': 1}

### D-10.2

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/DORA-GDPR.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=3, ambiguity=True), NIS2 (subso=0, reqs=0, verbatim=0, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 12, 'demoted_bullet': 7, 'demoted_para': 11, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}
- Script log:
  - D-10.2.md:L314: malformed tag '<!-- aegis:pair:NIS2, -->' (empty partner)
  - D-10.2: pair slot 'NIS2' has regs=['NIS2'] — routed to interactions

### D-10.3

- Files: _index.md, cross/AI_Act-CRA.md, cross/AI_Act-DORA.md, cross/AI_Act-GDPR.md, cross/AI_Act-NIS2.md, cross/CRA-DORA.md, cross/CRA-GDPR.md, cross/CRA-NIS2.md, cross/DORA-GDPR.md, cross/DORA-NIS2.md, cross/GDPR-NIS2.md, cross/_interactions.md, objective.md, regs/AI_Act.ambiguity.md, regs/AI_Act.md, regs/CRA.ambiguity.md, regs/CRA.md, regs/DORA.ambiguity.md, regs/DORA.md, regs/GDPR.ambiguity.md, regs/GDPR.md, regs/NIS2.ambiguity.md, regs/NIS2.md
- Reg modules: GDPR (subso=1, reqs=1, verbatim=2, ambiguity=True), CRA (subso=1, reqs=1, verbatim=2, ambiguity=True), NIS2 (subso=1, reqs=1, verbatim=2, ambiguity=True), DORA (subso=1, reqs=1, verbatim=2, ambiguity=True), AI_Act (subso=1, reqs=1, verbatim=2, ambiguity=True)
- Demotion stats: {'demoted_yaml_fields': 15, 'demoted_bullet': 2, 'demoted_para': 8, 'demoted_quote': 0, 'cross_mentions_in_tables': 0}

