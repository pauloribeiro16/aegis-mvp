#!/usr/bin/env python3
"""agent/tools.py — the agent's tool surface.

Every tool wraps an EXISTING pipeline function; the submission tools feed the
model's markdown/yaml through the SAME L0 parsers and content gates the fixed
prompt pipeline uses (parse_p1…parse_p4t, check_p4_quality), then persist with
the SAME store_parsed — so an agent artifact is byte-indistinguishable from a
pipeline artifact and validate.py judges both identically.

A rejected submission raises ToolError whose message is the parser/gate error —
that message is the repair signal returned to the model (the same text the
pipeline's L0 repair retry would append to its prompt).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from compose import (FICHA_FILES, candidate_subdomains, confirmed_regulations,  # noqa: E402
                     domain_dir, interactions_trim, load_case, parse_ficha,
                     parse_simple_yaml)
from controls import (goal_anchors, parse_overrides,  # noqa: E402
                     sd_control_sections, track_b_rows)
from compose import REGULATIONS  # noqa: E402
from steps import (PARSERS, PROPERTY_LONG, check_p4_quality,  # noqa: E402
                   parse_p1, parse_p4, store_parsed)
from steps import assemble_doc  # noqa: E402

# per-read size cap: one tool result must fit comfortably in the loop context
READ_CAP = 24_000


class ToolError(ValueError):
    """Raised by a tool when the model must change something and retry."""


class AgentToolbox:
    """All tools bound to one (repo, case, run_dir). Handlers return
    JSON-serialisable dicts; ToolError messages go back to the model verbatim."""

    def __init__(self, repo: Path, case_id: str, run_dir: Path):
        self.repo = repo
        self.case = load_case(repo, case_id)
        self.run_dir = run_dir
        (run_dir / "steps" / "goals").mkdir(parents=True, exist_ok=True)
        self._pending: dict[str, list[dict]] = {}
        self._in_progress: str | None = None

    # ---- state helpers ----------------------------------------------------

    def _require(self, rel: str, hint: str) -> Path:
        p = self.run_dir / rel
        if not p.exists():
            raise ToolError(f"state prerequisite missing: {rel}. {hint}")
        return p

    def _confirmed(self) -> list[str]:
        self._require("steps/verdicts.json", "Call submit_verdicts first.")
        return confirmed_regulations(self.run_dir)

    def _fenced_md(self, markdown: str) -> str:
        return f"```markdown\n{markdown.strip()}\n```"

    def _read_capped(self, p: Path, what: str) -> str:
        t = p.read_text(encoding="utf-8", errors="replace")
        if len(t) > READ_CAP:
            raise ToolError(
                f"{what} is {len(t)} chars (cap {READ_CAP}). Re-read it in parts: "
                f"pass part=1,2,… (each returns the next {READ_CAP} chars).")
        return t

    # ---- reading tools ------------------------------------------------------

    def get_company_brief(self) -> dict:
        """The company input (5 plain-prose sections) — the agent's entire brief
        about the company. Facts may come from nowhere else (R6)."""
        return {
            "case_id": self.case["case_id"], "company_id": self.case["company_id"],
            "output_language": self.case.get("output_language", "en"),
            "company_input_markdown": self.case["input_text"],
        }

    def read_output_contract(self, step: str) -> dict:
        """The executable ficha for one step (PROM-P1-01…07): the role, the
        output schema and the self-checks — the same rubric text the fixed
        prompt pipeline puts in its prompts."""
        if step not in FICHA_FILES:
            raise ToolError(f"unknown step {step!r}; use one of {sorted(FICHA_FILES)}")
        text = (self.repo / "docs" / "pipeline" / "prompts" / FICHA_FILES[step]).read_text(
            encoding="utf-8")
        # the whole ficha is 4-11k chars and mostly prose the model does not
        # act on; the output schema is the part it must follow exactly
        m = re.search(r"(?ms)^## Output schema\s*\n(.*?)(?=^## |\Z)", text)
        if m:
            text = (f"Output schema for {step}:\n{m.group(1).strip()}")
        if step == "p4":
            # the calibration reference: a completed sub-domain from the
            # produced deliverable. Never the one currently being written, so
            # the model cannot copy its own answer.
            ex = self._exemplar(subdomain=(self._in_progress or ""))
            if ex:
                text += ("\n\nCALIBRATION REFERENCE — a completed sub-domain from the "
                         "quality benchmark. Match its calibration and specificity; do not "
                         "copy its text.\n\n" + ex)
        return self._read_capped_resp(text, f"contract {step}")

    def _exemplar(self, subdomain: str) -> str:
        """One completed sub-domain block from the quality reference, chosen to
        differ from the sub-domain currently being written."""
        from compose import golden_text
        blocks = [b.strip() for b in re.split(r"(?m)^(?=### D-)", golden_text(self.repo))
                  if b.lstrip().startswith("### D-") and "## §4" not in b and b.strip()]
        others = [b for b in blocks if not b.startswith(f"### {subdomain} ")]
        b = (others or blocks or [""])[0]
        return b[:6000]

    def _read_capped_resp(self, text: str, what: str, part: int = 1) -> dict:
        if len(text) > READ_CAP:
            pages = max(1, -(-len(text) // READ_CAP))
            if not 1 <= part <= pages:
                raise ToolError(f"{what} has {pages} parts; part={part} out of range")
            chunk = text[(part - 1) * READ_CAP: part * READ_CAP]
            return {"part": part, "parts": pages, "chars_total": len(text),
                    "text": chunk + (f"\n\n[… continues in part {part + 1}]" if part < pages else "")}
        return {"part": 1, "parts": 1, "chars_total": len(text), "text": text}

    def list_candidate_subdomains(self) -> dict:
        """Deterministic P3 pre-filter: sub-domains carrying a regs/ module for
        at least one CONFIRMED regulation. Submit verdicts first."""
        confirmed = self._confirmed()
        cands = candidate_subdomains(self.repo, confirmed)
        return {"confirmed_regulations": confirmed,
                "candidates": [{"id": c["id"], "name": c["name"],
                                "confirmed_regs_present": c["confirmed_regs_present"]}
                               for c in cands]}

    def read_regulation_module(self, subdomain: str, part: str,
                               regulation: str | None = None, page: int = 1) -> dict:
        """Read one sub-domain's corpus module.
        part='objective'  → the regulation-neutral High-Level goal (objective.md, verbatim)
        part='regs'       → the per-regulation Sub-SO card(s): regs/<REG>.md for the
                            confirmed regulation(s) present (pass `regulation` for one)
        part='interactions' → cross/_interactions.md, operative sections only
        part='cross'      → cross/<R1>-<R2>.md pair analyses (both regs confirmed only)
        These are the ONLY baseline texts; quote/derive from them, never invent."""
        from compose import SD_RE
        if not SD_RE.match(subdomain):
            raise ToolError(f"non-canonical sub-domain id {subdomain!r} (expected D-XX.Y)")
        sd_dir = domain_dir(self.repo, subdomain)
        if not sd_dir.exists():
            raise ToolError(f"sub-domain {subdomain} does not exist in the corpus")
        confirmed = self._confirmed()

        if part == "objective":
            return self._read_capped_resp(
                self._read_capped(sd_dir / "objective.md", "objective.md"),
                f"{subdomain} objective")
        if part == "regs":
            regs = [regulation] if regulation else \
                sorted(r for r in confirmed if (sd_dir / "regs" / f"{r}.md").exists())
            if not regs:
                raise ToolError(f"{subdomain}: no regs/ module for the confirmed "
                                f"regulations {confirmed}")
            chunks = []
            for r in regs:
                p = sd_dir / "regs" / f"{r}.md"
                if not p.exists():
                    raise ToolError(f"{subdomain}: no regs/{r}.md in the corpus")
                chunks.append(f"===== {subdomain} / regs/{r}.md =====\n"
                              + self._read_capped(p, f"regs/{r}.md"))
            return self._read_capped_resp("\n\n".join(chunks), f"{subdomain} regs", page)
        if part == "interactions":
            p = sd_dir / "cross" / "_interactions.md"
            if not p.exists():
                return {"text": f"(no cross/_interactions.md for {subdomain})"}
            trimmed, _banner = interactions_trim(p, confirmed, keep=None)
            return self._read_capped_resp(trimmed, f"{subdomain} interactions", page)
        if part == "cross":
            out = []
            for i, r1 in enumerate(confirmed):
                for r2 in confirmed[i + 1:]:
                    p = sd_dir / "cross" / f"{r1}-{r2}.md"
                    if p.exists():
                        out.append(f"===== {subdomain} / cross/{r1}-{r2}.md =====\n"
                                   + self._read_capped(p, f"cross/{r1}-{r2}.md"))
            if not out:
                return {"text": f"(no cross pair files apply to {subdomain} for {confirmed})"}
            return self._read_capped_resp("\n\n".join(out), f"{subdomain} cross", page)
        raise ToolError(f"unknown part {part!r} (objective|regs|interactions|cross)")

    def get_subso_objective(self, subdomain: str, regulation: str) -> dict:
        """The Sub-SO objective you must restate for one row, verbatim. Use it
        when a goal row is rejected for dropping obligation content."""
        if regulation not in self._expected_regs(subdomain):
            raise ToolError(f"{subdomain} carries no Sub-SO for {regulation}; this module "
                            f"carries {self._expected_regs(subdomain)}")
        from compose import sub_so_objective
        return {"subdomain": subdomain, "regulation": regulation,
                "baseline_source": f"SG-{subdomain}.{regulation}",
                "objective": sub_so_objective(self.repo, subdomain, regulation)}

    # ---- derivation tools (R2b: anchors are code-derived, never emitted) ----

    def derive_anchors(self, subdomain: str, baseline_sources: list[str]) -> dict:
        """NIST CSF 2.0 anchors for goal rows, derived from the mapping store —
        the exact values assemble_doc will render in the Control Anchors column."""
        self._require("steps/verdicts.json", "Call submit_verdicts first.")
        return {"subdomain": subdomain,
                "anchors": goal_anchors(self.repo, subdomain, baseline_sources)}

    def derive_track_b(self) -> dict:
        """The deterministic §5 Track B matrix rows for the current selection."""
        fact = parse_simple_yaml(
            self._require("steps/fact_sheet.yaml", "Call submit_fact_sheet first.").read_text(encoding="utf-8"))
        sel = json.loads(self._require(
            "steps/selection.json", "Call submit_selection first.").read_text(encoding="utf-8"))
        ids = sorted(s["id"] for s in sel["selected"])
        rows = track_b_rows(fact, ids,
                            parse_overrides(self.case.get("track_b_overrides")))
        return {"rows": rows}

    def derive_controls_section(self, subdomain: str) -> dict:
        """The §6 NIST control tables for one sub-domain, as assemble_doc renders them."""
        confirmed = self._confirmed()
        sections = sd_control_sections(self.repo, subdomain, confirmed)
        return {"subdomain": subdomain, "sections": sections}

    # ---- submission tools (pipeline L0 parsers + gates, verbatim) ------------

    def submit_fact_sheet(self, yaml_text: str) -> dict:
        """Submit the P1 fact sheet as one ```yaml``` document (fields per the
        PROM-P1-01 schema). Validated with the pipeline's own parse_p1."""
        try:
            parsed = parse_p1(f"```yaml\n{yaml_text.strip()}\n```")
        except ValueError as e:
            raise ToolError(f"fact sheet rejected: {e}") from e
        store_parsed(self.run_dir, "p1", None, parsed)
        return {"ok": True, "stored": "steps/fact_sheet.yaml",
                "fields": sorted(parsed["fact"])}

    def submit_verdicts(self, markdown_table: str) -> dict:
        """Submit the P2 regulation verdicts as one markdown table
        (| Regulation | Verdict | Rationale |, all 5 candidates)."""
        try:
            parsed = PARSERS["p2"](self._fenced_md(markdown_table))
        except ValueError as e:
            raise ToolError(f"verdicts rejected: {e}") from e
        store_parsed(self.run_dir, "p2", None, parsed)
        applies = [v["regulation"] for v in parsed["verdicts"] if v["verdict"] == "applies"]
        return {"ok": True, "stored": "steps/verdicts.json", "confirmed": applies}

    def submit_selection(self, markdown: str) -> dict:
        """Submit the P3 subset selection: one markdown table
        (| Sub-domain | Name | Trigger rationale |) for SELECTED sub-domains plus a
        closing line `Excluded candidates:` with `- D-XX.Y — why not` for the rest.
        Every candidate must appear exactly once (no silent drops)."""
        from compose import confirmed_regulations as _cr
        self._confirmed()
        cands = [c["id"] for c in candidate_subdomains(self.repo, _cr(self.run_dir))]
        try:
            parsed = PARSERS["p3"](self._fenced_md(markdown), cands)
        except ValueError as e:
            raise ToolError(f"selection rejected: {e}") from e
        store_parsed(self.run_dir, "p3", None, parsed)
        return {"ok": True, "stored": "steps/selection.json",
                "selected": [s["id"] for s in parsed["selected"]],
                "excluded": len(parsed["excluded"])}

    def submit_framing(self, markdown_table: str) -> dict:
        """Submit the §2 framing table (| Dimension | Framing |) with exactly the
        four canonical dimensions, traced to the fact sheet (R6)."""
        self._confirmed()  # parity with stage_p3f: verdicts exist before framing
        try:
            parsed = PARSERS["p3f"](self._fenced_md(markdown_table))
        except ValueError as e:
            raise ToolError(f"framing rejected: {e}") from e
        store_parsed(self.run_dir, "p3f", None, parsed)
        return {"ok": True, "stored": "steps/framing.md"}

    def submit_goal(self, subdomain: str, baseline_source: str, goal: str,
                    implication: str, pattern: str, property_name: str,
                    source: str, adjustment: str,
                    assumptions: str = "> none") -> dict:
        """Submit ONE §3 goal row for one sub-domain. Call it once per Sub-SO
        of each confirmed regulation, in canonical regulation order, for the
        sub-domain named in `subdomain` — the artifact is written when every
        required Sub-SO of that module has been restated.

        One row per call, never a whole table: long tool-call arguments are
        truncated by the model mid-JSON and the server rejects the call.

        baseline_source: the Sub-SO id being restated, exactly `SG-<sd>.<REG>`.
        pattern: achieve|cease|maintain|avoid|optimize.
        property_name: Confidentiality|Integrity|Availability|Privacy Right|Accountability.
        adjustment: `unchanged — fits as stated` | `narrowed: … — because …` | `flagged: …`.
        source: the regulatory source (e.g. "GDPR Art. 32(1)(a)") — must resolve in the corpus (R2a).
        Control anchors are derived by code — never supply them."""
        self._confirmed()
        self._in_progress = subdomain
        expected = self._expected_regs(subdomain)
        if not expected:
            # a module with no Sub-SO for the confirmed regulations is a valid
            # case (D-02.2, D-08.3): the pipeline renders the explicit marker
            parsed = {"md": f"### {subdomain}\n\nNone — no Sub-SO for the confirmed "
                             f"regulations.\n\n## §5\n\n> none",
                      "goals": [], "assumptions": ["> none"]}
            store_parsed(self.run_dir, "p4", subdomain, parsed)
            return {"ok": True, "subdomain": subdomain, "n_goals": 0,
                    "note": "this module carries no Sub-SO for the confirmed regulations; "
                            "the empty marker was written — move to the next sub-domain"}
        if not baseline_source.startswith(f"SG-{subdomain}."):
            raise ToolError(f"baseline_source {baseline_source!r} must be one of "
                            f"{[f'SG-{subdomain}.{r}' for r in expected]}")
        reg = baseline_source.rsplit(".", 1)[-1]
        if reg not in expected:
            raise ToolError(f"row cites {reg}, which has no Sub-SO in {subdomain} for a "
                            f"confirmed regulation (R8) — this module carries "
                            f"{', '.join(expected)}")
        for name0, val in (("goal", goal), ("implication", implication),
                           ("source", source), ("adjustment", adjustment),
                           ("assumptions", assumptions)):
            if "|" in val:
                raise ToolError(
                    f"the {name0} field contains a literal '|' — rephrase it with a comma or "
                    f"a semicolon; a field may not contain the pipe character")
        cells = [goal, implication, pattern, property_name, "", baseline_source, source, adjustment]
        # row-local content gates run NOW so a defective row is rejected on the
        # call that submitted it (set-level coverage runs when the module closes)
        self._gate_row(subdomain, reg, goal, implication, pattern, property_name,
                       source, adjustment)
        answer = (f"```markdown\n| SUBMITTED | {goal} | {implication} | {pattern} | "
                  f"{property_name} | SO-{subdomain}.HL | {baseline_source} | {source} | "
                  f"{adjustment} |\n\n## §5\n\n{assumptions.strip()}\n```")
        try:
            parsed = parse_p4(answer, subdomain, expect_id=False)
            if not parsed["goals"]:
                raise ValueError("row rejected — no goal row parsed")
            g = parsed["goals"][0]
            # merge into the module artifact, keeping canonical order by regulation
            g["id"] = None  # ids are assigned on persist, in regulation order
            pending = self._pending.setdefault(subdomain, [])
            pending[:] = [x for x in pending if x["regulation"] != g["regulation"]]
            pending.append(g)
            pending.sort(key=lambda r: REGULATIONS.index(r["regulation"]))
            got = {r["regulation"] for r in pending}
            if set(expected) - got:
                missing = sorted(set(expected) - got, key=REGULATIONS.index)
                return {"ok": True, "partial": True, "subdomain": subdomain,
                        "accepted_regulation": g["regulation"],
                        "still_needed": missing,
                        "note": f"row accepted; {subdomain} is not complete yet — submit "
                                f"one row for each of {missing}"}
            # complete: assign sequential ids and run the content gates
            for i, row in enumerate(pending, 1):
                row["id"] = f"AG-{subdomain}-{i:03d}"
            table = "\n".join(
                f"| {r['id']} | {r['goal']} | {r['implication']} | {r['pattern']} | "
                f"{PROPERTY_LONG[r['property']]} | {r['parent']} | {r['baseline_source']} | "
                f"{r['source']} | {r['adjustment']} |" for r in pending)
            full = (f"```markdown\n### {subdomain}\n\n| ID | Adjusted goal | Company implication "
                    f"| Pattern | Property | Parent goal | Baseline source | Regulatory source "
                    f"| Adjustment |\n|---|---|---|---|---|---|---|---|---|\n{table}\n\n## §5\n\n"
                    f"{assumptions.strip()}\n```")
            parsed = parse_p4(full, subdomain)
            parsed = check_p4_quality(self.repo, self.run_dir, parsed, subdomain)
        except ValueError as e:
            raise ToolError(f"goal row for {subdomain} rejected: {e}") from e
        store_parsed(self.run_dir, "p4", subdomain, parsed)
        self._pending.pop(subdomain, None)
        return {"ok": True, "subdomain": subdomain,
                "stored": f"steps/goals/{subdomain.replace('.', '_')}.json",
                "n_goals": len(parsed["goals"])}

    def _gate_row(self, subdomain: str, reg: str, goal: str, implication: str,
                  pattern: str, property_name: str, source: str, adjustment: str) -> None:
        """Every content gate that is a property of THIS row alone — the same
        checks the pipeline applies, so a rejection reads identically."""
        import quality
        from compose import sub_so_objective
        from steps import PROPERTY_ALIASES, PROPERTY_LONG
        prop = PROPERTY_ALIASES.get(property_name.strip().lower().replace(" ", "-"))
        row = {"id": f"AG-{subdomain}-NNN", "goal": goal, "implication": implication,
               "pattern": pattern.strip().lower(), "property": prop,
               "parent": f"SO-{subdomain}.HL", "baseline_source": baseline_source_of(subdomain, reg),
               "regulation": reg, "source": source, "adjustment": adjustment}
        baseline = sub_so_objective(self.repo, subdomain, reg)
        sources = [baseline]
        for name in ("fact_sheet.yaml", "framing.md"):
            f = self.run_dir / "steps" / name
            if f.exists():
                sources.append(f.read_text(encoding="utf-8"))
        peers = [g["implication"] for sd, rows in self._pending.items() for g in rows
                 if g["id"] != row["id"]]
        peers += [g["implication"] for jf in
                  sorted((self.run_dir / "steps" / "goals").glob("*.json"))
                  for g in json.loads(jf.read_text(encoding="utf-8")).get("goals", [])]
        findings = quality.run_row(row, {reg: baseline}, sources, peers)
        if findings:
            raise ToolError("; ".join(findings))
        _ = PROPERTY_LONG

    def _expected_regs(self, subdomain: str) -> list[str]:
        from compose import domain_dir as _dd
        sd_dir = _dd(self.repo, subdomain)
        return [reg for reg in self._confirmed()
                if (sd_dir / "regs" / f"{reg}.md").exists()
                and f"SG-{subdomain}.{reg}" in
                (sd_dir / "regs" / f"{reg}.md").read_text(encoding="utf-8")]

    def list_corpus_tensions(self) -> dict:
        """The Emergent-tensions passages from every SELECTED sub-domain's
        cross/_interactions.md. Call this BEFORE submit_tensions: a tension
        counts when the corpus raises it and the confirmed regulations are in
        scope — decide from the text, not from memory."""
        from compose import interactions_trim as _trim
        sel = json.loads(self._require(
            "steps/selection.json", "Call submit_selection first.").read_text(encoding="utf-8"))
        out = []
        for s_ in sorted(x["id"] for x in sel["selected"]):
            f = domain_dir(self.repo, s_) / "cross" / "_interactions.md"
            if not f.exists():
                continue
            trimmed, _banner = _trim(f, self._confirmed(), keep="emergent")
            if trimmed.strip():
                out.append(f"===== {s_} =====\n{trimmed.strip()}")
        return {"selected_subdomains": len(sel["selected"]),
                "emergent_tension_sections": len(out), "text": "\n\n".join(out)}

    def submit_tensions(self, markdown: str, none_reason: str = "") -> dict:
        """Submit §4 tension resolutions: the 5-column table
        (ID | Sub-domains | Tension | Conflict | Resolution).
        Call list_corpus_tensions first. `None.` is accepted ONLY together with
        `none_reason` naming the condition under which no tension activates —
        a silent `None.` is a silent drop (R8)."""
        confirmed = self._confirmed()
        if len(confirmed) < 2:
            (self.run_dir / "steps" / "tensions.json").write_text(
                json.dumps({"tensions": []}, indent=1, ensure_ascii=False),
                encoding="utf-8")
            return {"ok": True, "stored": "steps/tensions.json",
                    "note": "single-regulation run — empty tensions written without a call"}
        stripped = markdown.strip()
        if stripped.lower().rstrip(".") == "none" and not none_reason.strip():
            raise ToolError(
                "a bare `None.` is rejected: call list_corpus_tensions first, then if no "
                "tension activates, repeat `None.` with none_reason stating the condition "
                "(e.g. which regulation pairing is out of scope or which corpus tension "
                "does not apply to this company)")
        try:
            parsed = PARSERS["p4t"](self._fenced_md(markdown))
        except ValueError as e:
            raise ToolError(f"tensions rejected: {e}") from e
        store_parsed(self.run_dir, "p4t", None, parsed)
        return {"ok": True, "stored": "steps/tensions.json",
                "n_tensions": len(parsed["tensions"])}

    def finalize(self) -> dict:
        """Assemble doc02_adjusted_goals.md, run the full L1 validation, and finish.
        Rejected while any goal artifact is missing or findings are open — the
        error names what to repair. Requires: selection, framing, tensions and
        one complete goal artifact per selected sub-domain."""
        for rel, hint in (("steps/fact_sheet.yaml", "submit_fact_sheet"),
                          ("steps/verdicts.json", "submit_verdicts"),
                          ("steps/selection.json", "submit_selection"),
                          ("steps/framing.md", "submit_framing"),
                          ("steps/tensions.json", "submit_tensions")):
            self._require(rel, f"Call {hint} first.")
        sel = json.loads((self.run_dir / "steps" / "selection.json").read_text(encoding="utf-8"))
        missing = [s["id"] for s in sel["selected"]
                   if not (self.run_dir / "steps" / "goals" / f"{s['id'].replace('.', '_')}.json").exists()]
        if missing:
            raise ToolError(f"cannot finalize: no goal artifact for {missing} — submit_goal "
                            f"for each of those sub-domains first")
        from trace import count_calls, update_manifest
        from validate import validate_run
        doc = assemble_doc(self.repo, self.run_dir, self.case)
        (self.run_dir / "doc02_adjusted_goals.md").write_text(doc, encoding="utf-8")
        update_manifest(self.run_dir, n_calls_total=count_calls(self.run_dir))
        findings = validate_run(self.repo, self.run_dir)
        if findings:
            raise ToolError(f"finalize rejected: {len(findings)} validation finding(s) — "
                            f"repair and re-finalize: {findings[:6]}")
        return {"ok": True, "written": "doc02_adjusted_goals.md", "chars": len(doc),
                "validation": "PASS"}

    # ---- verification / closing tools -----------------------------------------

    def get_state(self) -> dict:
        """Progress view: which artifacts exist, how many goals per sub-domain."""
        steps = self.run_dir / "steps"
        goals = {}
        for jf in sorted((steps / "goals").glob("*_*.json")):
            try:
                d = json.loads(jf.read_text(encoding="utf-8"))
                goals[d.get("subdomain", jf.stem)] = len(d.get("goals", []))
            except (json.JSONDecodeError, OSError):
                goals[jf.stem] = -1
        have = [rel for rel in ("fact_sheet.yaml", "verdicts.json", "selection.json",
                                "framing.md", "tensions.json")
                if (steps / rel).exists()]
        return {"artifacts_present": have, "goals_per_subdomain": goals}

    def self_validate(self) -> dict:
        """Run the same L1 validation the pipeline runs post-assembly (needs the
        deliverable rendered first: call render_document). Empty findings = PASS."""
        from trace import count_calls, update_manifest
        from validate import validate_run
        # mirror stage_p5: the manifest's call counter is updated by the runner
        # AFTER the stage returns — bring it current before validating
        update_manifest(self.run_dir, n_calls_total=count_calls(self.run_dir))
        findings = validate_run(self.repo, self.run_dir)
        return {"verdict": "PASS" if not findings else "FAIL", "findings": findings}

    def render_document(self) -> dict:
        """Assemble doc02_adjusted_goals.md from the submitted artifacts with the
        SAME zero-LLM assembler the pipeline uses (HL paragraphs and baselines
        verbatim from the corpus; anchors/§5/§6 derived by code). Requires all
        step artifacts to exist."""
        for rel, hint in (("steps/fact_sheet.yaml", "submit_fact_sheet"),
                          ("steps/verdicts.json", "submit_verdicts"),
                          ("steps/selection.json", "submit_selection"),
                          ("steps/framing.md", "submit_framing"),
                          ("steps/tensions.json", "submit_tensions")):
            self._require(rel, f"Call {hint} first.")
        sel = json.loads((self.run_dir / "steps" / "selection.json").read_text(encoding="utf-8"))
        missing = [s["id"] for s in sel["selected"]
                   if not (self.run_dir / "steps" / "goals" / f"{s['id'].replace('.', '_')}.json").exists()]
        if missing:
            raise ToolError(f"no goal artifact for selected sub-domain(s) {missing} — "
                            f"call submit_goals for each before rendering")
        doc = assemble_doc(self.repo, self.run_dir, self.case)
        (self.run_dir / "doc02_adjusted_goals.md").write_text(doc, encoding="utf-8")
        return {"ok": True, "written": "doc02_adjusted_goals.md", "chars": len(doc)}


# ---------------------------------------------------------------------------
# Ollama tool schemas (JSON schema for /api/chat tools)
# ---------------------------------------------------------------------------

def tool_schemas() -> list[dict]:
    return [
        {"type": "function", "function": {
            "name": "get_company_brief", "description":
            "Read the company input (5 plain-prose sections) — the ONLY source of company facts (R6).",
            "parameters": {"type": "object", "properties": {}, "required": []}}},
        {"type": "function", "function": {
            "name": "read_output_contract", "description":
            "Read the executable ficha (rubric) for a step: p1|p2|p3|p3f|p4|p4t. "
            "Read the p4 ficha BEFORE writing any goal rows.",
            "parameters": {"type": "object",
                           "properties": {"step": {"type": "string",
                                                   "enum": ["p1", "p2", "p3", "p3f", "p4", "p4t"]}},
                           "required": ["step"]}}},
        {"type": "function", "function": {
            "name": "list_candidate_subdomains", "description":
            "Deterministic pre-filter: sub-domains with a regs/ module for ≥1 confirmed regulation. "
            "Requires submit_verdicts first.",
            "parameters": {"type": "object", "properties": {}, "required": []}}},
        {"type": "function", "function": {
            "name": "read_regulation_module", "description":
            "Read one sub-domain's corpus module: part=objective|regs|interactions|cross. "
            "regs returns the Sub-SO card(s) — the mandatory baseline for goal rows.",
            "parameters": {"type": "object",
                           "properties": {
                               "subdomain": {"type": "string"},
                               "part": {"type": "string",
                                        "enum": ["objective", "regs", "interactions", "cross"]},
                               "regulation": {"type": "string",
                                              "enum": ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]},
                               "page": {"type": "integer", "minimum": 1}},
                           "required": ["subdomain", "part"]}}},
        {"type": "function", "function": {
            "name": "submit_fact_sheet", "description":
            "Submit the P1 fact sheet as one yaml document (schema in the p1 ficha).",
            "parameters": {"type": "object",
                           "properties": {"yaml_text": {"type": "string"}},
                           "required": ["yaml_text"]}}},
        {"type": "function", "function": {
            "name": "submit_verdicts", "description":
            "Submit the P2 verdict table: | Regulation | Verdict | Rationale | for ALL 5 "
            "candidates; verdict ∈ applies / does not apply / flagged.",
            "parameters": {"type": "object",
                           "properties": {"markdown_table": {"type": "string"}},
                           "required": ["markdown_table"]}}},
        {"type": "function", "function": {
            "name": "submit_selection", "description":
            "Submit the P3 selection: markdown table | Sub-domain | Name | Trigger rationale | "
            "of SELECTED ids + final line 'Excluded candidates:' with '- D-XX.Y — why'. "
            "Every candidate exactly once.",
            "parameters": {"type": "object",
                           "properties": {"markdown": {"type": "string"}},
                           "required": ["markdown"]}}},
        {"type": "function", "function": {
            "name": "submit_framing", "description":
            "Submit the §2 framing table | Dimension | Framing | — exactly the four canonical "
            "dimensions, every cell traced to the fact sheet.",
            "parameters": {"type": "object",
                           "properties": {"markdown_table": {"type": "string"}},
                           "required": ["markdown_table"]}}},
        {"type": "function", "function": {
            "name": "submit_goal", "description":
            "Submit ONE §3 goal row. Call once per Sub-SO of each confirmed regulation for "
            "the sub-domain you are working on. One row per call — never a whole table. "
            "Control anchors are derived by code; never supply them.",
            "parameters": {"type": "object",
                           "properties": {
                               "subdomain": {"type": "string"},
                               "baseline_source": {"type": "string",
                                                   "description": "SG-<sd>.<REG> being restated"},
                               "goal": {"type": "string"},
                               "implication": {"type": "string"},
                               "pattern": {"type": "string",
                                           "enum": ["achieve", "cease", "maintain", "avoid",
                                                    "optimize"]},
                               "property_name": {"type": "string",
                                                 "enum": ["Confidentiality", "Integrity",
                                                          "Availability", "Privacy Right",
                                                          "Accountability"]},
                               "source": {"type": "string"},
                               "adjustment": {"type": "string"},
                               "assumptions": {"type": "string"}},
                           "required": ["subdomain", "baseline_source", "goal", "implication",
                                        "pattern", "property_name", "source", "adjustment"]}}},
        {"type": "function", "function": {
            "name": "list_corpus_tensions", "description":
            "The Emergent-tensions passages from every selected sub-domain. Read this "
            "BEFORE deciding whether any tension resolves — a bare `None.` is rejected.",
            "parameters": {"type": "object", "properties": {}, "required": []}}},
        {"type": "function", "function": {
            "name": "submit_tensions", "description":
            "Submit §4 resolutions: table | ID | Sub-domains | Tension | Conflict | Resolution |. "
            "Only after list_corpus_tensions. A bare `None.` requires none_reason.",
            "parameters": {"type": "object",
                           "properties": {"markdown": {"type": "string"},
                                          "none_reason": {"type": "string"}},
                           "required": ["markdown"]}}},
        {"type": "function", "function": {
            "name": "get_subso_objective", "description":
            "The Sub-SO objective to restate, verbatim (one sub-domain + regulation). "
            "Call this before writing a goal row, or when a row is rejected for dropping "
            "obligation content.",
            "parameters": {"type": "object",
                           "properties": {
                               "subdomain": {"type": "string"},
                               "regulation": {"type": "string",
                                              "enum": ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]}},
                           "required": ["subdomain", "regulation"]}}},
        {"type": "function", "function": {
            "name": "get_state", "description":
            "Progress view: which artifacts exist and goals-per-sub-domain counts.",
            "parameters": {"type": "object", "properties": {}, "required": []}}},
        {"type": "function", "function": {
            "name": "finalize", "description":
            "Assemble the deliverable, run L1 validation and finish. Rejected while any "
            "goal artifact is missing or findings are open.",
            "parameters": {"type": "object", "properties": {}, "required": []}}},
    ]


def baseline_source_of(subdomain: str, reg: str) -> str:
    return f"SG-{subdomain}.{reg}"


def execute_tool(toolbox: AgentToolbox, name: str, args: dict) -> dict:
    """Dispatch one tool call; ToolError → structured rejection for the model."""
    fn = getattr(toolbox, name, None)
    if fn is None or not callable(fn):
        return {"ok": False, "error": f"unknown tool {name!r}"}
    try:
        return fn(**args)
    except ToolError as e:
        return {"ok": False, "error": str(e)}
    except TypeError as e:
        return {"ok": False, "error": f"bad arguments for {name}: {e}"}


class _FinishSignal(Exception):
    """Internal: the model called finish() — handled by the loop, not a tool."""


def try_finish(toolbox: AgentToolbox) -> tuple[bool, dict]:
    """finish() gate: the run may end only when the deliverable exists and the
    L1 validator passes. Returns (allowed, payload) — payload carries the
    findings when rejected."""
    if not (toolbox.run_dir / "doc02_adjusted_goals.md").exists():
        return False, {"ok": False,
                       "error": "cannot finish: doc02_adjusted_goals.md has not been "
                                "rendered — call render_document first",
                       "findings": ["deliverable not rendered"]}
    from trace import count_calls, update_manifest
    from validate import validate_run
    update_manifest(toolbox.run_dir, n_calls_total=count_calls(toolbox.run_dir))
    findings = validate_run(toolbox.repo, toolbox.run_dir)
    if findings:
        return False, {"ok": False,
                       "error": f"cannot finish: {len(findings)} validation finding(s) open "
                                f"— repair and re-render, then finish again",
                       "findings": findings[:10]}
    return True, {"ok": True}
