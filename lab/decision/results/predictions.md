| # | prediction | verdict | evidence |
|---|---|---|---|
| P1 | the vLLM route agrees with the checkpoint on >=95% of picks, with max |dp| <= 0.05 on every labelled case | **HOLDS** | agreement 106/109 = 0.9725; max |dp| on labelled 0.031209; max |dp| on unlabelled 0.124353 (contract.state_empty) |
| P2 | d1-3B scores at least as high as d1-omni-600M on the labelled cases | **REFUTED** | A1 54/84 = 0.6429 vs A3-float32 60/84 = 0.7143 |
| P3 | the best arm reaches >=4/5 on the tension-activation cases | **HOLDS** | best arm A3-bfloat16: 4/5 = 0.8000 |
| P4 | padding the state with irrelevant prose moves at most 1 of 5 answers | **REFUTED** | A1-bfloat16: 3 moved; A2: 3 moved; A3-bfloat16: 1 moved; A3-float16: 1 moved; A3-float32: 1 moved |
| P5 | injecting an instruction into the state moves at most 1 of 5 answers | **REFUTED** | A1-bfloat16: 1 moved; A2: 1 moved; A3-bfloat16: 3 moved; A3-float16: 3 moved; A3-float32: 3 moved |
| P6 | paraphrasing the question moves at most 1 of 5 answers | **HOLDS** | A1-bfloat16: 1 moved; A2: 1 moved; A3-bfloat16: 0 moved; A3-float16: 1 moved; A3-float32: 0 moved |
| P7 | repeats of the same case agree 100% within an arm | **HOLDS** | 5/5 repeat groups stable |
| P8/float16 | the float16 arm disagrees with the float32 arm on <=2% of answers | **HOLDS** | 1/114 = 0.88% of answers differ |
| P8/bfloat16 | the bfloat16 arm disagrees with the float32 arm on <=2% of answers | **HOLDS** | 1/114 = 0.88% of answers differ |
| P9 | the models answer 'does not activate' for T-003 and T-004, which the pipeline emitted as rows anyway | **HOLDS** | best arm A1-bfloat16: 2/2 correct |
| P10 | a state above the context ceiling produces a refusal or a truncation, not a silently confident answer | **REFUTED** | A1-bfloat16: 44828 tokens, p(yes)=0.8670357598021706, confidence=None | A2: refused ({'kind': 'http', 'status': 400, 'detail': {'error': {'message': "This model's maximum context length is 32768 tokens. However, your prompt contains at least 32769 input tokens, which exceeds this limit even without any output tokens. Please reduce the length of the input prompt. (parameter=input_tokens, value=32769)", 'type': 'BadRequestError', 'param': 'input_tokens', 'code': 400}}}) | A3-bfloat16: 16384 tokens, p(yes)=0.7307918667793274, confidence=None | A3-float16: 16384 tokens, p(yes)=0.747621476650238, confidence=None | A3-float32: 16384 tokens, p(yes)=0.7467072010040283, confidence=None |
