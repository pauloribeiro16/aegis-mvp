# lab overlay: qwen35-demo — p2 worked format demo for qwen3.5:27b (LAB01, PREREG-LAB01 H-L1 arm B)
# Same signature as qwen35-fence. This arm teaches the shape by EXAMPLE — a
# fictional company so the model cannot copy verdicts (anti-circular few-shot,
# PE-005: demonstrations carry format, not content). Real header, real
# regulation ids, placeholder verdicts marked clearly as illustration.
REPLACEMENTS = [
    (
        '''    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),''',
        '''    "p2": ("Your ENTIRE answer is one ```markdown fenced block containing the 5-row "
           "verdict table. Copy this SHAPE exactly — different company, so different "
           "verdicts; the shape is what matters: "
           "```markdown "
           "| Regulation | Verdict | Rationale |\\n"
           "| GDPR | applies | processes personal data of EU data subjects as controller |\\n"
           "| CRA | does not apply | no products with digital elements placed on the market |\\n"
           "| NIS2 | does not apply | sector and size thresholds not met |\\n"
           "| DORA | does not apply | not a financial entity |\\n"
           "| AI_Act | flagged | input asserts an AI use without stating placement |\\n"
           "``` "
           "Five rows, one per candidate regulation, verdicts only from "
           "{applies, does not apply, flagged}, each rationale one sentence grounded "
           "in the fact sheet. Nothing before the opening fence line, nothing after "
           "the closing fence."),''',
    ),
]
