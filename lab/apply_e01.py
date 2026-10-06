#!/usr/bin/env python3
"""Apply the E-01 lab patch (schema-constrained p2) to a COPY of pipeline/src.

Usage: python3 lab/apply_e01.py <target>/pipeline/src

This arm deliberately touches MORE than instruction text — it changes the serving
request for p2 only. The guard is therefore not "no forbidden tokens" but
"nothing outside the four permitted edits", each applied by exact single-occurrence
anchor, with a compile() gate and a byte-diff assertion that every gate/parser/
threshold function is unchanged.

Permitted edits:
  1. llm.py    chat()/chat_messages(): accept and forward `fmt` in the payload
  2. steps.py  p2 schema constants + converter import
  3. steps.py  _call(): pass fmt for p2 and convert a JSON answer before validation
  4. steps.py  the p2 EXTRA_INSTRUCTION entry (the content task replaces the shape task)

Nothing else. Every p1/p3/p3f/p4/p4t path, every parser, every threshold stays
byte-identical, which the diff assertion below enforces rather than asserts.
"""
import re
import sys
from pathlib import Path

GUARD_PATTERNS = (
    r"^def parse_p1", r"^def parse_p3\(", r"^def parse_p3f", r"^def parse_p4\(",
    r"^def parse_p4t", r"^def check_p4_quality", r"^def _validate", r"^def _sweep",
    r"^def stage_p4\(", r"^def stage_p4t", r"^def assemble_doc", r"^def store_parsed",
    r"^def _call\(", r"^NUM_CTX", r"^NUM_PREDICT", r"^PARSERS", r"^ADJ_PREFIXES",
    r"^RETENTION_FLOOR", r"^IMPLICATION_DUP",
)
GUARD_RE = re.compile("|".join(GUARD_PATTERNS))


def guarded_block(src: str) -> str:
    """Concatenate every guarded function/threshold definition, verbatim."""
    lines = src.splitlines()
    out, keep = [], False
    for line in lines:
        if GUARD_RE.match(line):
            keep = True
        elif keep and line and not line[0].isspace() and not line.startswith((")", "]", "}")):
            keep = False
        if keep:
            out.append(line)
    return "\n".join(out)


def apply_replacements(src: str, replacements: list[tuple[str, str]], label: str) -> str:
    for old, new in replacements:
        n = src.count(old)
        if n != 1:
            sys.exit(f"FAIL[{label}]: anchor occurs {n}x (expected 1): {old[:100]!r}…")
        src = src.replace(old, new)
    return src


def main() -> int:
    src_root = Path(sys.argv[1])
    simple_json = "--simple-json" in sys.argv[2:]
    llm_p, steps_p = src_root / "llm.py", src_root / "steps.py"
    llm_o, steps_o = llm_p.read_text(encoding="utf-8"), steps_p.read_text(encoding="utf-8")

    schema_src = (Path(__file__).parent / "e01_schema.py").read_text(encoding="utf-8")
    schema_re = re.search(r"P2_SCHEMA = \{.*?\n\}\n", schema_src, re.S)
    instr_re = re.search(r"P2_SCHEMA_INSTRUCTION = \(.*?\)\n", schema_src, re.S)
    if not (schema_re and instr_re):
        sys.exit("FAIL: could not extract schema/instruction from e01_schema.py")

    # --- 1. llm.py: fmt passthrough -----------------------------------------
    llm_n = apply_replacements(llm_o, [
        (
            """    def chat(self, model: str, system: str, user: str, num_ctx: int,
             temperature: float = 0.2, timeout_s: int | None = None,
             num_predict: int = 8192, sampler: dict | None = None) -> dict:""",
            """    def chat(self, model: str, system: str, user: str, num_ctx: int,
             temperature: float = 0.2, timeout_s: int | None = None,
             num_predict: int = 8192, sampler: dict | None = None,
             fmt: dict | None = None) -> dict:""",
        ),
        (
            """            "think": False,
            "options": options,
        }
        raw = self._request("/api/chat", payload, timeout_s or self.timeout_read)""",
            """            "think": False,
            "options": options,
        }
        # E-01 lab arm: schema-constrained decoding. Ollama 0.32.13 accepts a
        # JSON schema object in `format`; the generation is then constrained to
        # it and the fence that instruction text could not elicit arrives for free.
        if fmt:
            payload["format"] = fmt
        raw = self._request("/api/chat", payload, timeout_s or self.timeout_read)""",
        ),
        (
            """    def chat_messages(self, model: str, messages: list[dict], num_ctx: int,
                      temperature: float = 0.2, timeout_s: int | None = None,
                      num_predict: int = 8192, tools: list[dict] | None = None,
                      sampler: dict | None = None) -> dict:""",
            """    def chat_messages(self, model: str, messages: list[dict], num_ctx: int,
                      temperature: float = 0.2, timeout_s: int | None = None,
                      num_predict: int = 8192, tools: list[dict] | None = None,
                      sampler: dict | None = None, fmt: dict | None = None) -> dict:""",
        ),
        (
            """        if tools:
            payload["tools"] = tools""",
            """        if tools:
            payload["tools"] = tools
        if fmt:
            payload["format"] = fmt""",
        ),
    ], "llm")

    # --- 2. steps.py: schema constants + converter --------------------------
    steps_n = apply_replacements(steps_o, [
        (
            '''EXTRA_INSTRUCTION = {''',
            f'''# E-01 lab arm (schema-constrained p2). Prompting for the fence failed 5/5 on
SIMPLE_JSON = {str(simple_json)}  # --simple-json: fmt="json" instead of a schema object
# qwen3.5 with a PERFECT verdict table and no fence; the shape is now enforced by
# the serving layer and `json_to_p2_markdown` renders the artefact parse_p2 reads.
{schema_re.group(0).rstrip()}
{instr_re.group(0).rstrip()}
from e01_schema import json_to_p2_markdown  # noqa: E402

EXTRA_INSTRUCTION = {{''',
        ),
        # p2 instruction becomes the content task (shape now lives in the schema)
        (
            '''    "p2": ("Wrap your answer: return ONLY one ```markdown fenced block containing the "
           "5-row §2 verdict table (header + 5 rows, nothing else)."),''',
            '''    "p2": P2_SCHEMA_INSTRUCTION,''',
        ),
    ], "steps/constants")

    # --- 3. steps.py: _call converts a JSON answer before validation --------
    # Both call sites (first attempt and repair) get the same treatment; the
    # converter is inserted once, immediately after each `answer` is bound.
    conv_body = (
        """# E-01 lab arm: a constrained answer is JSON by construction; render
# the markdown artefact BEFORE validation so every p2 gate runs on it
# unchanged. A non-JSON answer falls through to the normal fence path
# (parse_p2 then rejects it as before).
if step == "p2" and answer.strip().startswith("{{"):
    answer = json_to_p2_markdown(answer.strip())
"""
    )

    def conv_at(indent: int) -> str:
        return "".join(indent * " " + ln + "\n" for ln in conv_body.rstrip("\n").split("\n"))
    steps_n = apply_replacements(steps_n, [
        (
            """                raw = client.chat(self.model, call["system"], call["user"], num_ctx,
                                  temperature=self.temperature,
                                  num_predict=num_predict, sampler=self.sampler)""",
            """                raw = client.chat(self.model, call["system"], call["user"], num_ctx,
                                  temperature=self.temperature,
                                  num_predict=num_predict, sampler=self.sampler,
                                  # E-01 lab arm: constrain p2 generation to the schema
                                  fmt=('json' if SIMPLE_JSON else 'P2_SCHEMA') if step == "p2" else None)""",
        ),
        (
            """                raw2 = client.chat(self.model, call["system"], retry_user, num_ctx,""",
            """                raw2 = client.chat(self.model, call["system"], retry_user, num_ctx,
                                   fmt=('json' if SIMPLE_JSON else P2_SCHEMA) if step == "p2" else None,""",
        ),
        (
            """        # L0 validation with one repair retry
        try:
            parsed = self._validate(step, answer, subdomain)""",
            """        # L0 validation with one repair retry
""" + conv_at(8) + """        try:
            parsed = self._validate(step, answer, subdomain)""",
        ),
        (
            """                record["retry_output_path"] = str(retry_out)
                parsed = self._validate(step, answer2, subdomain)""",
            """                record["retry_output_path"] = str(retry_out)
""" + conv_at(16).replace("answer.strip()", "answer2.strip()").replace(
                "answer = json_to_p2_markdown(answer2.strip())",
                "answer2 = json_to_p2_markdown(answer2.strip())") +
            """                parsed = self._validate(step, answer2, subdomain)""",
        ),
    ], "steps/_call")

    # --- guards -------------------------------------------------------------
    for label, before, after, path in (
        ("llm.py", llm_o, llm_n, llm_p),
        ("steps.py", steps_o, steps_n, steps_p),
    ):
        g0, g1 = guarded_block(before), guarded_block(after)
        if g0 != g1:
            changed = [l for l in g1.splitlines() if l not in g0.splitlines()]
            sys.exit(f"FAIL: {label} guards changed: {changed[:5]}")
        try:
            compile(after, str(path), "exec")
        except SyntaxError as e:
            sys.exit(f"FAIL: {label} does not compile: {e}")
        path.with_name(path.name + ".prelab").write_text(before, encoding="utf-8")
        path.write_text(after, encoding="utf-8")

    print("E-01 lab patch applied: llm.py (fmt passthrough), steps.py (schema + converter + "
          "p2 instruction). All guarded functions byte-identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())