# lab overlay: gemma4-precision — p4 slot order + R6 emphasis for gemma4:31b (LAB01, H-L4)
# Signature (M07): C3 37/38 (slot-order violation on D-08.2), C2 35/37 (R8 stub row,
# R6 invented quantity 56). The run is otherwise clean — precision nudges on two
# rules that already exist, placed after the §5 instruction they complement.
REPLACEMENTS = [
    (
        '''        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "''',
        '''        f"(ambiguity interpretation is already decided in the corpus — do not cite or "
        f"re-analyze ambiguity cards; write `None.` if empty; at most 3 blockquotes). "
        f"SLOT ORDER: the rows appear in the exact order the Sub-SO ids are listed in "
        f"the column rules below — never reorder them. When several confirmed "
        f"regulations have their own Sub-SO in this module, the canonical sequence is "
        f"GDPR, then CRA, then NIS2, then DORA, then AI_Act; a row citing a later "
        f"regulation before an earlier one fails validation. "
        f"QUANTITIES: every number you write must appear verbatim in the fact sheet "
        f"or the attached corpus — an untraceable quantity fails validation. "''',
    ),
]
