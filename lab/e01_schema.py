# lab E-01 — schema-constrained decoding at p2 (prototype, qwen3.5:27b)
#
# Signature (M07 3/3 + LAB01 2/2): `no ```markdown fenced block found in answer`.
# The model emits the PERFECT verdict table and simply never writes the fence —
# content right, delimiter contract absent. Two instruction shapes (character-level
# fence-first, worked format demo) both failed identically, which is the signal the
# prereg said to read as "serving-layer class, not instruction class".
#
# E-01's move: stop asking for the shape in prose and CONSTRAIN the generation to
# it at the serving layer (Ollama `format:` accepts a JSON schema). The model then
# emits JSON by construction; a deterministic converter renders the exact markdown
# artefact the pipeline already consumes.
#
# NOTHING in pipeline/src changes. This module + apply_e01.py patch a COPY.

P2_SCHEMA = {
    "type": "object",
    "properties": {
        "verdicts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "regulation": {"type": "string"},
                    "verdict": {
                        "type": "string",
                        "enum": ["applies", "does not apply", "flagged"],
                    },
                    "rationale": {"type": "string"},
                },
                "required": ["regulation", "verdict", "rationale"],
            },
        },
        "assumptions": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["verdicts"],
}

# The instruction that accompanies the schema. It states the CONTENT task only —
# no shape instructions at all, because the schema now governs the shape. Keeping
# the scope criteria (which live in the ficha) is what the answer depends on.
P2_SCHEMA_INSTRUCTION = (
    "Answer as JSON matching the required schema. Decide each of the five candidate "
    "regulations against its scope criteria using the fact sheet: one entry per "
    "regulation in `verdicts` (regulation, verdict, rationale — the rationale is one "
    "sentence grounded in the fact sheet, no preamble), and any open questions or "
    "assumptions you had to make in `assumptions`. Nothing else."
)


def _cell(s: str) -> str:
    """Escape a value for a markdown table cell: pipes would split the row."""
    return str(s).replace("|", "/").replace("\n", " ").strip()


def json_to_p2_markdown(payload: str) -> str:
    """Render constrained JSON as the exact artefact parse_p2 consumes.

    `extract_fenced(answer, "markdown")` then finds the fence, `parse_md_table`
    splits the rows, and every existing p2 gate runs unchanged on the result. The
    converter is deliberately dumb: it neither decides nor validates verdicts — an
    out-of-vocabulary verdict or a missing regulation must still FAIL in parse_p2,
    because the gate, not the converter, is the instrument.
    """
    import json

    data = json.loads(payload)
    verdicts = data.get("verdicts") or []
    if not isinstance(verdicts, list):
        raise ValueError(f"schema-conforming answer with non-list verdicts: {type(verdicts)}")

    lines = ["| Regulation | Verdict | Rationale |", "|---|---|---|"]
    for v in verdicts:
        lines.append("| {reg} | {verdict} | {rationale} |".format(
            reg=_cell(v.get("regulation", "")),
            verdict=_cell(v.get("verdict", "")),
            rationale=_cell(v.get("rationale", "")),
        ))
    body = "\n".join(lines)

    assumptions = [a for a in (data.get("assumptions") or []) if str(a).strip()]
    tail = ("\n\n## §5\n\n" + "\n".join(f"> ASSUMPTION: {a}" for a in assumptions)
            if assumptions else "\n\n## §5\n\nNone.")

    return f"```markdown\n{body}{tail}\n```"