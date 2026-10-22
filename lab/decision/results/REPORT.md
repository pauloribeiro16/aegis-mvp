# LAB03 — d1 decision models on Deucalion

Records: 508 · arms: A1, A2, A3

## 1. Per-arm summary

| arm | route | model | dtype | records | contract | error paths | accuracy (labelled) | unlabelled | median ms | p95 ms |
|---|---|---|---|---|---|---|---|---|---|---|
| A1-bfloat16 | d1-3B · in-process (bfloat16) | LiquidAI_d1-3B | bfloat16 | 101 | ok | ok | 0.6429 (54/84) | 28 | 27.37 | 34.98 |
| A2 | d1-3B · vLLM 0.32.0 /v1/systemone | LiquidAI/d1-3B | n/a | 104 | ok | ok | 0.6049 (49/81) | 28 | 45.37 | 91.53 |
| A3-bfloat16 | d1-omni-600M · in-process (bfloat16) | LiquidAI_d1-omni-600M | bfloat16 | 101 | ok | ok | 0.7262 (61/84) | 24 | 16.6 | 22.52 |
| A3-float16 | d1-omni-600M · in-process (float16) | LiquidAI_d1-omni-600M | float16 | 101 | ok | ok | 0.7262 (61/84) | 24 | 16.37 | 24.53 |
| A3-float32 | d1-omni-600M · in-process (float32) | LiquidAI_d1-omni-600M | float32 | 101 | ok | ok | 0.7143 (60/84) | 24 | 31.89 | 72.77 |

## 1b. Per decision site

The overall accuracy hides the shape of the error. A model that answers
"no" to every boolean scores 50 % on a balanced set and 7 % on a 35/3 set,
so the label and pick distributions are reported next to the accuracy.

### A1-bfloat16

| site | labelled | accuracy | labels T/F | picks T/F | one-sided |
|---|---|---|---|---|---|
| adjustment (unlabelled) | 0 | — | — | — | no |
| coverage verdict | 5 | 0.6 | — | — | no |
| principle constraint | 14 | 0.5 | 7T/7F | 0T/14F | **yes** |
| protocol / other | 5 | 0.8 | 2T/3F | 3T/2F | no |
| regulation applicability | 10 | 0.7 | 4T/6F | 7T/3F | no |
| regulation applicability (repeats) | 10 | 0.5 | 5T/5F | 10T/0F | **yes** |
| sub-domain trigger | 35 | 0.7143 | 35T/0F | 25T/10F | no |
| tension activation | 5 | 0.6 | 3T/2F | 1T/4F | no |

### A2

| site | labelled | accuracy | labels T/F | picks T/F | one-sided |
|---|---|---|---|---|---|
| adjustment (unlabelled) | 0 | — | — | — | no |
| coverage verdict | 5 | 0.6 | — | — | no |
| principle constraint | 14 | 0.5 | 7T/7F | 0T/14F | **yes** |
| protocol / other | 2 | 0.5 | 1T/1F | 2T/0F | **yes** |
| regulation applicability | 10 | 0.7 | 4T/6F | 7T/3F | no |
| regulation applicability (repeats) | 10 | 0.5 | 5T/5F | 10T/0F | **yes** |
| sub-domain trigger | 35 | 0.6571 | 35T/0F | 23T/12F | no |
| tension activation | 5 | 0.6 | 3T/2F | 1T/4F | no |

### A3-bfloat16

| site | labelled | accuracy | labels T/F | picks T/F | one-sided |
|---|---|---|---|---|---|
| adjustment (unlabelled) | 0 | — | — | — | no |
| coverage verdict | 5 | 0.2 | — | — | no |
| principle constraint | 14 | 0.7143 | 7T/7F | 7T/7F | no |
| protocol / other | 5 | 0.6 | 2T/3F | 0T/5F | **yes** |
| regulation applicability | 10 | 0.6 | 4T/6F | 0T/10F | **yes** |
| regulation applicability (repeats) | 10 | 0.5 | 5T/5F | 0T/10F | **yes** |
| sub-domain trigger | 35 | 0.9143 | 35T/0F | 32T/3F | **yes** |
| tension activation | 5 | 0.8 | 3T/2F | 2T/3F | no |

### A3-float16

| site | labelled | accuracy | labels T/F | picks T/F | one-sided |
|---|---|---|---|---|---|
| adjustment (unlabelled) | 0 | — | — | — | no |
| coverage verdict | 5 | 0.2 | — | — | no |
| principle constraint | 14 | 0.7143 | 7T/7F | 7T/7F | no |
| protocol / other | 5 | 0.6 | 2T/3F | 0T/5F | **yes** |
| regulation applicability | 10 | 0.7 | 4T/6F | 1T/9F | **yes** |
| regulation applicability (repeats) | 10 | 0.5 | 5T/5F | 0T/10F | **yes** |
| sub-domain trigger | 35 | 0.8857 | 35T/0F | 31T/4F | no |
| tension activation | 5 | 0.8 | 3T/2F | 2T/3F | no |

### A3-float32

| site | labelled | accuracy | labels T/F | picks T/F | one-sided |
|---|---|---|---|---|---|
| adjustment (unlabelled) | 0 | — | — | — | no |
| coverage verdict | 5 | 0.2 | — | — | no |
| principle constraint | 14 | 0.7143 | 7T/7F | 7T/7F | no |
| protocol / other | 5 | 0.6 | 2T/3F | 0T/5F | **yes** |
| regulation applicability | 10 | 0.6 | 4T/6F | 0T/10F | **yes** |
| regulation applicability (repeats) | 10 | 0.5 | 5T/5F | 0T/10F | **yes** |
| sub-domain trigger | 35 | 0.8857 | 35T/0F | 31T/4F | no |
| tension activation | 5 | 0.8 | 3T/2F | 2T/3F | no |

## 2. Pairwise comparison

### A1-bfloat16 vs A2

- comparable cases: 89 of 96
- pick agreement: **0.9663**
- max |Δp|: **0.124353** · mean |Δp|: 0.00948

Disagreeing cases:

| case | question | type | A | B | max |Δp| |
|---|---|---|---|---|---|
| `contract.state_empty` | gdpr | noul | True | False | 0.124353 |
| `domain.trigger.D_04_2` | triggered | noul | True | False | 0.031209 |
| `domain.trigger.D_07_4` | triggered | noul | True | False | 0.031209 |

### A1-bfloat16 vs A3-float32

- comparable cases: 90 of 97
- pick agreement: **0.5333**
- max |Δp|: **0.920836** · mean |Δp|: 0.313702

Disagreeing cases:

| case | question | type | A | B | max |Δp| |
|---|---|---|---|---|---|
| `contract.choice.five` | route | choice | 'billing' | 'technical' | 0.920836 |
| `contract.choice.ten` | route | choice | 'billing' | 'technical' | 0.884789 |
| `contract.choice.three` | route | choice | 'billing' | 'technical' | 0.900529 |
| `contract.choice.two` | route | choice | 'billing' | 'technical' | 0.691673 |
| `contract.state_dict` | gdpr | noul | True | False | 0.506271 |
| `contract.state_list` | gdpr | noul | True | False | 0.569301 |
| `contract.state_null` | gdpr | noul | False | True | 0.288716 |
| `domain.coverage.po_d_01.1_001` | verdict | choice | 'Partially_covered_(functional_leg_+_explicit_carve-out)' | 'Fully_covered_(anchored)' | 0.374052 |
| `domain.coverage.po_d_01.3_001` | verdict | choice | 'No_functional_carrier_(organizational)' | 'Fully_covered_(anchored)' | 0.377522 |
| `domain.coverage.so_d_02.1_001` | verdict | choice | 'No_functional_carrier_(organizational)' | 'N/A' | 0.516902 |
| `domain.coverage.so_d_06.3_002` | verdict | choice | 'No_functional_carrier_(organizational)' | 'Partially_covered_(functional_leg_+_explicit_carve-out)' | 0.284292 |
| `domain.principle.prin_eng_01.bound` | constrains | noul | False | True | 0.346404 |
| `domain.principle.prin_eng_01.unbound` | constrains | noul | False | True | 0.595218 |
| `domain.principle.prin_eng_02.bound` | constrains | noul | False | True | 0.39078 |
| `domain.principle.prin_eng_03.bound` | constrains | noul | False | True | 0.428659 |
| `domain.principle.prin_eng_04.bound` | constrains | noul | False | True | 0.471722 |
| `domain.principle.prin_eng_05.unbound` | constrains | noul | False | True | 0.158053 |
| `domain.principle.prin_eng_06.bound` | constrains | noul | False | True | 0.231147 |
| `domain.tension.t-001` | activates | noul | False | True | 0.767951 |
| `domain.tension.t-002` | activates | noul | False | True | 0.686596 |
| `domain.tension.t-005` | activates | noul | True | False | 0.307324 |
| `domain.trigger.D_02_2` | triggered | noul | True | False | 0.211176 |
| `domain.trigger.D_02_3` | triggered | noul | True | False | 0.415136 |
| `domain.trigger.D_02_4` | triggered | noul | True | False | 0.118251 |
| `domain.trigger.D_03_1` | triggered | noul | True | False | 0.462213 |
| `domain.trigger.D_03_3` | triggered | noul | False | True | 0.221613 |
| `domain.trigger.D_03_4` | triggered | noul | False | True | 0.256922 |
| `domain.trigger.D_04_1` | triggered | noul | False | True | 0.472787 |
| `domain.trigger.D_04_3` | triggered | noul | False | True | 0.351342 |
| `domain.trigger.D_04_4` | triggered | noul | False | True | 0.409635 |
| `domain.trigger.D_05_4` | triggered | noul | False | True | 0.133738 |
| `domain.trigger.D_06_4` | triggered | noul | True | False | 0.437948 |
| `domain.trigger.D_07_3` | triggered | noul | False | True | 0.601609 |
| `domain.trigger.D_08_2` | triggered | noul | False | True | 0.168975 |
| `domain.trigger.D_10_2` | triggered | noul | False | True | 0.308569 |
| `robust.batch_shape` | cra | noul | True | False | 0.516297 |
| `robust.batch_shape` | gdpr | noul | True | False | 0.731825 |
| `robust.batch_shape` | nis2 | noul | True | False | 0.353686 |
| `robust.minimal` | cra | noul | True | False | 0.516297 |
| `robust.minimal` | gdpr | noul | True | False | 0.731828 |
| `robust.minimal` | nis2 | noul | True | False | 0.353687 |
| `robust.minimal.injected` | dora | noul | False | True | 0.804842 |
| `robust.minimal.padded` | gdpr | noul | False | True | 0.266255 |
| `robust.minimal.paraphrased` | cra | noul | True | False | 0.547636 |
| `robust.minimal.paraphrased` | dora | noul | True | False | 0.506837 |
| `robust.minimal.paraphrased` | gdpr | noul | True | False | 0.47445 |
| `robust.minimal.paraphrased` | nis2 | noul | True | False | 0.293041 |

### A3-float32 vs A3-float16

- comparable cases: 90 of 97
- pick agreement: **0.9889**
- max |Δp|: **0.005154** · mean |Δp|: 0.001277

Disagreeing cases:

| case | question | type | A | B | max |Δp| |
|---|---|---|---|---|---|
| `robust.minimal.paraphrased` | gdpr | noul | False | True | 0.004672 |

### A3-float32 vs A3-bfloat16

- comparable cases: 90 of 97
- pick agreement: **0.9889**
- max |Δp|: **0.046872** · mean |Δp|: 0.009504

Disagreeing cases:

| case | question | type | A | B | max |Δp| |
|---|---|---|---|---|---|
| `domain.trigger.D_01_3` | triggered | noul | False | True | 0.010718 |

## 3. Contrast pairs (within an arm)

Does the answer move when the state is padded with irrelevant text, when an
instruction is injected into the state, or when the question is paraphrased?

### A1-bfloat16

| variant | comparable | same answer | drifted questions |
|---|---|---|---|
| `robust.minimal.padded` | yes | **NO** | cra, gdpr, nis2 |
| `robust.minimal.injected` | yes | **NO** | cra |
| `robust.minimal.paraphrased` | yes | **NO** | dora |

### A2

| variant | comparable | same answer | drifted questions |
|---|---|---|---|
| `robust.minimal.padded` | yes | **NO** | cra, gdpr, nis2 |
| `robust.minimal.injected` | yes | **NO** | cra |
| `robust.minimal.paraphrased` | yes | **NO** | dora |

### A3-bfloat16

| variant | comparable | same answer | drifted questions |
|---|---|---|---|
| `robust.minimal.padded` | yes | **NO** | gdpr |
| `robust.minimal.injected` | yes | **NO** | dora, gdpr, nis2 |
| `robust.minimal.paraphrased` | yes | yes | — |

### A3-float16

| variant | comparable | same answer | drifted questions |
|---|---|---|---|
| `robust.minimal.padded` | yes | **NO** | gdpr |
| `robust.minimal.injected` | yes | **NO** | dora, gdpr, nis2 |
| `robust.minimal.paraphrased` | yes | **NO** | gdpr |

### A3-float32

| variant | comparable | same answer | drifted questions |
|---|---|---|---|
| `robust.minimal.padded` | yes | **NO** | gdpr |
| `robust.minimal.injected` | yes | **NO** | dora, gdpr, nis2 |
| `robust.minimal.paraphrased` | yes | yes | — |

## 4. Per-case answers

| case | label | A1-bfloat16 | A2 | A3-bfloat16 | A3-float16 | A3-float32 |
|---|---|---|---|---|---|---|
| `contract.choice.five` | — | route='billing' | route='billing' | route='technical' | route='technical' | route='technical' |
| `contract.choice.letter_names` | — | route='a' | route='a' | route='a' | route='a' | route='a' |
| `contract.choice.no_description` | — | route='billing' | route='billing' | route='billing' | route='billing' | route='billing' |
| `contract.choice.ten` | — | route='billing' | route='billing' | route='technical' | route='technical' | route='technical' |
| `contract.choice.three` | — | route='billing' | route='billing' | route='technical' | route='technical' | route='technical' |
| `contract.choice.two` | — | route='billing' | route='billing' | route='technical' | route='technical' | route='technical' |
| `contract.multi_question` | — | wants_refund=True; route='billing'; urgency=1 | wants_refund=True; route='billing'; urgency=1 | wants_refund=True; route='billing'; urgency=1 | wants_refund=True; route='billing'; urgency=1 | wants_refund=True; route='billing'; urgency=1 |
| `contract.noul.basic` | — | refund=True | refund=True | refund=True | refund=True | refund=True |
| `contract.noul.criteria` | — | refund=True | refund=True | refund=True | refund=True | refund=True |
| `contract.score.five` | — | urgency=3 | urgency=3 | urgency=3 | urgency=3 | urgency=3 |
| `contract.score.ten` | — | urgency=6 | urgency=6 | urgency=6 | urgency=6 | urgency=6 |
| `contract.score.three` | — | urgency=2 | urgency=2 | urgency=2 | urgency=2 | urgency=2 |
| `contract.score.two` | — | urgency=1 | urgency=1 | urgency=1 | urgency=1 | urgency=1 |
| `contract.state_dict` | — | gdpr=True | gdpr=True | gdpr=False | gdpr=False | gdpr=False |
| `contract.state_empty` | — | gdpr=True | gdpr=False | gdpr=True | gdpr=True | gdpr=True |
| `contract.state_list` | — | gdpr=True | gdpr=True | gdpr=False | gdpr=False | gdpr=False |
| `contract.state_null` | — | gdpr=False | gdpr=False | gdpr=True | gdpr=True | gdpr=True |
| `domain.adjustment.narrowed_d02_2_cra` | — | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' |
| `domain.adjustment.proportional_d10_1_gdpr` | — | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' |
| `domain.adjustment.verbatim_d10_1_cra` | — | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' | relation='verbatim' |
| `domain.coverage.po_d_01.1_001` | {"verdict": "Partially_covered_(functional_leg_+_explicit_carve-out)"} | verdict='Partially_covered_(functional_leg_+_explicit_carve-out)' | verdict='Partially_covered_(functional_leg_+_explicit_carve-out)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' |
| `domain.coverage.po_d_01.2_001` | {"verdict": "Fully_covered_(anchored)"} | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' |
| `domain.coverage.po_d_01.3_001` | {"verdict": "Design_guidance"} | verdict='No_functional_carrier_(organizational)' | verdict='No_functional_carrier_(organizational)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' | verdict='Fully_covered_(anchored)' |
| `domain.coverage.so_d_02.1_001` | {"verdict": "No_functional_carrier_(organizational)"} | verdict='No_functional_carrier_(organizational)' | verdict='No_functional_carrier_(organizational)' | verdict='N/A' | verdict='N/A' | verdict='N/A' |
| `domain.coverage.so_d_06.3_002` | {"verdict": "N/A"} | verdict='No_functional_carrier_(organizational)' | verdict='No_functional_carrier_(organizational)' | verdict='Partially_covered_(functional_leg_+_explicit_carve-out)' | verdict='Partially_covered_(functional_leg_+_explicit_carve-out)' | verdict='Partially_covered_(functional_leg_+_explicit_carve-out)' |
| `domain.principle.prin_eng_01.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_01.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_02.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_02.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_03.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_03.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_04.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_04.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_05.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_05.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_06.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=True | constrains=True | constrains=True |
| `domain.principle.prin_eng_06.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_07.bound` | {"constrains": true} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.principle.prin_eng_07.unbound` | {"constrains": false} | constrains=False | constrains=False | constrains=False | constrains=False | constrains=False |
| `domain.tension.t-001` | {"activates": true} | activates=False | activates=False | activates=True | activates=True | activates=True |
| `domain.tension.t-002` | {"activates": true} | activates=False | activates=False | activates=True | activates=True | activates=True |
| `domain.tension.t-003` | {"activates": false} | activates=False | activates=False | activates=False | activates=False | activates=False |
| `domain.tension.t-004` | {"activates": false} | activates=False | activates=False | activates=False | activates=False | activates=False |
| `domain.tension.t-005` | {"activates": true} | activates=True | activates=True | activates=False | activates=False | activates=False |
| `domain.trigger.D_01_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_01_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_01_3` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=False | triggered=False |
| `domain.trigger.D_01_4` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_02_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_02_2` | {"triggered": true} | triggered=True | triggered=True | triggered=False | triggered=False | triggered=False |
| `domain.trigger.D_02_3` | {"triggered": true} | triggered=True | triggered=True | triggered=False | triggered=False | triggered=False |
| `domain.trigger.D_02_4` | {"triggered": false} | triggered=True | triggered=True | triggered=False | triggered=False | triggered=False |
| `domain.trigger.D_03_1` | {"triggered": true} | triggered=True | triggered=True | triggered=False | triggered=False | triggered=False |
| `domain.trigger.D_03_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_03_3` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_03_4` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_04_1` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_04_2` | {"triggered": true} | triggered=True | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_04_3` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_04_4` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_05_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_05_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_05_3` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_05_4` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_06_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_06_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_06_3` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_06_4` | {"triggered": false} | triggered=True | triggered=True | triggered=False | triggered=False | triggered=False |
| `domain.trigger.D_07_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_07_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_07_3` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_07_4` | {"triggered": true} | triggered=True | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_08_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_08_2` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_08_3` | {"triggered": false} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_09_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_09_2` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_09_3` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_09_4` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_10_1` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_10_2` | {"triggered": true} | triggered=False | triggered=False | triggered=True | triggered=True | triggered=True |
| `domain.trigger.D_10_3` | {"triggered": true} | triggered=True | triggered=True | triggered=True | triggered=True | triggered=True |
| `error.choice.empty_criteria` | — | **error** (RuntimeError) | **error** (http) | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.choice.one_criterion` | — | route='billing' | route='billing' | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.noul.no_instructions` | — | **error** (KeyError) | refund=True | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.score.eleven_levels` | — | urgency=5 | **error** (http) | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.score.no_criteria` | — | **error** (KeyError) | **error** (http) | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.score.one_level` | — | urgency=0 | **error** (http) | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `error.unknown_type` | — | route='billing' | **error** (http) | **error** (ValueError) | **error** (ValueError) | **error** (ValueError) |
| `robust.batch_shape` | {"gdpr": true, "cra": true, "nis2": false, "dora": false, "ai_act": false} | gdpr=True; cra=True; nis2=True; dora=False; ai_act=False | — | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False |
| `robust.long_state` | — | gdpr=True | **error** (http) | gdpr=True | gdpr=True | gdpr=True |
| `robust.minimal` | {"gdpr": true, "cra": true, "nis2": false, "dora": false, "ai_act": false} | gdpr=True; cra=True; nis2=True; dora=False; ai_act=False | gdpr=True; cra=True; nis2=True; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False |
| `robust.minimal.injected` | — | gdpr=True; cra=False; nis2=True; dora=False; ai_act=False | gdpr=True; cra=False; nis2=True; dora=False; ai_act=False | gdpr=True; cra=False; nis2=True; dora=True; ai_act=False | gdpr=True; cra=False; nis2=True; dora=True; ai_act=False | gdpr=True; cra=False; nis2=True; dora=True; ai_act=False |
| `robust.minimal.padded` | — | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=True; cra=False; nis2=False; dora=False; ai_act=False | gdpr=True; cra=False; nis2=False; dora=False; ai_act=False | gdpr=True; cra=False; nis2=False; dora=False; ai_act=False |
| `robust.minimal.paraphrased` | {"gdpr": true, "cra": true, "nis2": false, "dora": false, "ai_act": false} | gdpr=True; cra=True; nis2=True; dora=True; ai_act=False | gdpr=True; cra=True; nis2=True; dora=True; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False | gdpr=True; cra=False; nis2=False; dora=False; ai_act=False | gdpr=False; cra=False; nis2=False; dora=False; ai_act=False |
| `robust.multi_question_consistency` | — | gdpr_noul=True; gdpr_choice='yes' | gdpr_noul=True; gdpr_choice='yes' | gdpr_noul=False; gdpr_choice='yes' | gdpr_noul=False; gdpr_choice='yes' | gdpr_noul=False; gdpr_choice='yes' |
| `robust.repeat5` | {"gdpr": true, "nis2": false} | gdpr=True; nis2=True | gdpr=True; nis2=True | gdpr=False; nis2=False | gdpr=False; nis2=False | gdpr=False; nis2=False |
| `smoke.choice` | — | — | route='billing' | — | — | — |
| `smoke.labelled` | {"gdpr": true, "nis2": false} | — | gdpr=True; nis2=True | — | — | — |
| `smoke.noul` | — | — | refund=True | — | — | — |
| `smoke.score` | — | — | urgency=2 | — | — | — |

