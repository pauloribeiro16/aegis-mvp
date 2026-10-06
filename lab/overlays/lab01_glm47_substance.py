# lab overlay: glm47-substance — p4 restatement depth + mandatory §5 for glm-4.7-flash (LAB01, H-L2)
# Signature (M07, C1): 20/38 carried — mixed `P4 answer missing the '## §5' section`
# and near-verbatim 96% rows. Arm: obligation-leg scaffold + §5 is never optional.
REPLACEMENTS = [
    (
        '''        f"proportional RESTATEMENT of that Sub-SO's Objective (2+ sentences, same "
        f"obligation content, no meta-language like 'restatement of the baseline'); "''',
        '''        f"proportional RESTATEMENT of that Sub-SO's Objective (2+ sentences, same "
        f"obligation content, no meta-language like 'restatement of the baseline'). "
        f"Restate EVERY obligation leg before any company tail: WHO must do WHAT, "
        f"to WHICH assets or subjects, with WHAT measure, against WHAT threshold "
        f"or factor — a row that drops one of these legs fails validation. "
        f"Two full sentences minimum; a compressed one-liner fails. "''',
    ),
    (
        '''        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "''',
        '''        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "
        f"THE §5 SECTION IS NEVER OPTIONAL: an answer without the `## §5` heading and "
        f"its content fails validation in full, no matter how good the table is — "
        f"if there is nothing to declare, the section says exactly `None.` "''',
    ),
]
