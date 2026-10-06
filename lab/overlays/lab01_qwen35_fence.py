# lab overlay: qwen35-fence — p2 fence-first for qwen3.5:27b (LAB01, PREREG-LAB01 H-L1 arm A)
# Signature (M07): `no ```markdown fenced block found in answer` 3/3 — the model
# emits content but not the literal fence. This arm makes the fence the FIRST
# and LAST instruction, at character level, instead of a subordinate clause.
REPLACEMENTS = [
    (
        '''    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),''',
        '''    "p2": ("OUTPUT SHAPE — five hard rules, in this order of importance. "
           "RULE 1: the very first characters you emit are the three backticks and the "
           "word markdown — a full opening fence line by itself. Write NOTHING before "
           "that fence line: no heading, no sentence, no blank line of prose. "
           "RULE 2: immediately after that fence line comes the table header "
           "`| Regulation | Verdict | Rationale |`. "
           "RULE 3: then exactly 5 data rows, one per candidate regulation, in the same "
           "order the candidates were listed. "
           "RULE 4: the very last characters you emit are three backticks closing the "
           "fence. Write NOTHING after them. "
           "RULE 5: nothing exists outside the fence — the whole answer is the fenced "
           "block and the fenced block is the whole answer."),''',
    ),
]
