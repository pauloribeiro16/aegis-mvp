# lab overlay: nemotron-substance — p4 depth + R6 quantities + 9-cell rows for nemotron-3.5 (LAB01, H-L3)
# Signature (M07, C1): 31/38 carried — near-verbatim 98%, invented quantity 2020 (R6),
# a missing fence, near-duplicate implications. Arm: the glm47 leg/§5 scaffold PLUS
# grounding of every number and a cell-count rule per row.
REPLACEMENTS = [
    (
        '''        f"proportional RESTATEMENT of that Sub-SO's Objective (2+ sentences, same "
        f"obligation content, no meta-language like 'restatement of the baseline'); "''',
        '''        f"proportional RESTATEMENT of that Sub-SO's Objective (2+ sentences, same "
        f"obligation content, no meta-language like 'restatement of the baseline'). "
        f"Restate EVERY obligation leg before any company tail: WHO must do WHAT, "
        f"to WHICH assets or subjects, with WHAT measure, against WHAT threshold "
        f"or factor — a row that drops one of these legs fails validation. "
        f"Every number you write must appear verbatim in the fact sheet or the "
        f"attached corpus: an invented or rounded-off quantity fails validation. "
        f"Each implication is specific to THIS row's duty — never reuse or lightly "
        f"edit an implication you already wrote for another row. "''',
    ),
    (
        '''        f"TERMINATION: after the `## §5` section the answer is COMPLETE — emit the "''',
        '''        f"TABLE SHAPE: each data row of the goal table has EXACTLY 9 cells — ID, "
        f"Adjusted goal, Company implication, Pattern, Property, Parent goal, Baseline "
        f"source, Regulatory source, Adjustment — that is 8 `|` separators per row, no "
        f"more, no fewer. "
        f"THE §5 SECTION IS NEVER OPTIONAL: an answer without the `## §5` heading fails "
        f"validation in full; if there is nothing to declare, it says exactly `None.` "
        f"TERMINATION: after the `## §5` section the answer is COMPLETE — emit the "''',
    ),
]
