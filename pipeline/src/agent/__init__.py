"""agent — directed tool-using agent mode for Phase 1 (EXP-01 arm 2).

Same corpus, same case, same validators and the same zero-LLM render as the
fixed prompt pipeline; the difference is who decides the order and granularity
of work: here the model drives a tool loop (read module → submit artifact →
repair on named errors) instead of receiving one composed prompt per step.
State lives on disk in the same steps/ layout, so assemble_doc and validate.py
treat both arms identically."""
