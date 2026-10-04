#!/usr/bin/env python3
"""compose.py — deterministic context packs and prompts for the Phase 1 pipeline.

Single source of truth for prompt text is the ficha set under
docs/pipeline/prompts/ (ADR-010 D2). This module parses a ficha (frontmatter,
metadata table, output schema, prompt body) and assembles the per-call
system/user messages. Context packs are pure functions of
(case binding, P2 verdicts, P3 selection) — no summarisation, verbatim file
content only (ADR-010 D3).

Stdlib only: runs on Deucalion compute nodes with no pip egress.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

REGULATIONS = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]

FICHA_FILES = {
    "p1": "PROM-P1-01_EXTRACT_FACTS.md",
    "p2": "PROM-P1-02_CONFIRM_REGULATIONS.md",
    "p3": "PROM-P1-03_SELECT_SUBDOMAINS.md",
    "p3f": "PROM-P1-06_BUILD_FRAMING.md",
    "p4": "PROM-P1-04_DERIVE_ADJUSTED_GOALS.md",
    "p4t": "PROM-P1-07_RESOLVE_TENSIONS.md",
    "p5": "PROM-P1-05_RENDER_VALIDATE.md",
}

# Sub-domain id like D-01.1
SD_RE = re.compile(r"^D-\d{2}\.\d$")


# --------------------------------------------------------------------------
# minimal parsers (stdlib-only; formats are fixed by this repo)
# --------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Split a leading `---` YAML frontmatter block. Returns (meta, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta_block, rest = m.group(1), m.group(2)
    meta: dict[str, str] = {}
    for line in meta_block.splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if mm and not line.startswith((" ", "\t")):
            meta[mm.group(1)] = mm.group(2).strip().strip("'\"")
    return meta, rest


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the flat YAML subset used by the fact sheet and case bindings:
    top-level `key: value`, inline lists `[a, b]`, block lists (`- item`),
    quoted scalars, `>` folded continuation lines and comments."""
    data: dict[str, Any] = {}
    key: str | None = None
    folded: list[str] = []
    block_items: list[str] | None = None

    def flush_scalar() -> None:
        nonlocal folded, key
        if key is not None and folded:
            data[key] = " ".join(s.strip() for s in folded).strip()
            folded = []

    def flush_block() -> None:
        nonlocal block_items, key
        if key is not None and block_items is not None:
            data[key] = block_items
            block_items = None

    def coerce(raw: str) -> Any:
        raw = raw.strip()
        # strip trailing ` # comment` unless the value is quoted
        if len(raw) < 2 or raw[0] not in "\"'":
            cpos = raw.find(" #")
            if cpos != -1:
                raw = raw[:cpos].rstrip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            return [coerce(x) for x in inner.split(",")] if inner else []
        if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
            return raw[1:-1]
        if raw.lower() in ("true", "false"):
            return raw.lower() == "true"
        if re.fullmatch(r"-?\d+", raw):
            return int(raw)
        return raw

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and key is not None:
            flush_scalar()
            if block_items is None:
                block_items = []
            block_items.append(coerce(stripped[2:]))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            flush_scalar()
            flush_block()
            key, rest = m.group(1), m.group(2).strip()
            if rest in (">", ">-", "|", "|-"):
                folded = []
                continue
            if rest == "":
                # could become a block list or stay empty; resolved by later lines
                block_items = []
                continue
            block_items = None
            data[key] = coerce(rest)
            continue
        # continuation of a folded scalar
        if key is not None and block_items is None:
            folded.append(stripped)
    flush_scalar()
    flush_block()
    return data


def parse_ficha(path: Path) -> dict[str, Any]:
    """Parse a prompt ficha (fixed anatomy, docs/pipeline/03_PROMPT_CATALOG.md)."""
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)

    sections: dict[str, str] = {}
    current = None
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            current = m.group(1).strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    sections = {k: "\n".join(v).strip() for k, v in sections.items()}

    def table_field(section: str, field: str) -> str:
        for line in sections.get(section, "").splitlines():
            m = re.match(rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|\s*$", line)
            if m:
                return m.group(1).strip()
        return ""

    prompt_body_lines: list[str] = []
    for line in sections.get("Prompt body", "").splitlines():
        if line.startswith(">"):
            prompt_body_lines.append(re.sub(r"^>\s?", "", line))
        elif prompt_body_lines and not line.strip():
            break
    prompt_body = "\n".join(prompt_body_lines).strip()

    # Output schema section verbatim (fenced yaml for P1, markdown tables/lists
    # for P2/P4/P5 — both are part of the contract shown to the model)
    schema = sections.get("Output schema", "").strip()

    pack_files: list[dict[str, str]] = []
    pack_section = next((v for k, v in sections.items() if k.startswith("Context pack")), "")
    for line in pack_section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and re.fullmatch(r"\d+", cells[0]):
            pack_files.append({"file": cells[1], "use": cells[2]})

    return {
        "id": meta.get("ficha_id", path.stem),
        "version": meta.get("version", "0"),
        "title": meta.get("title", ""),
        "pattern": meta.get("pattern", ""),
        "role": table_field("Metadata", "Role"),
        "mission": table_field("Metadata", "Mission"),
        "failure_mode": table_field("Metadata", "Failure mode"),
        "human_gate": (sections.get("Human gate", "").strip()
                       or table_field("Metadata", "Human gate")),
        "self_checks": sections.get("Self-checks (L2)", "").strip(),
        "prompt_body": prompt_body,
        "output_schema": schema,
        "pack_declared": pack_files,
        "source_path": str(path),
    }


def extract_section_text(path: Path, start: str, end: str) -> str:
    """Text of a `^## ` section of a file, from `start` up to the next
    section whose heading starts with `end`."""
    text = path.read_text(encoding="utf-8")
    m = re.search(rf"(?m)^{re.escape(start)}.*?$", text)
    if not m:
        return ""
    tail = text[m.end():]
    stop = re.search(rf"(?m)^{re.escape(end)}", tail)
    return (tail[: stop.start()] if stop else tail).strip()


def extract_markdown_section(text: str, heading_prefix: str, stop_prefixes: list[str]) -> str:
    """Return the content of the `heading_prefix` section, up to the next
    heading that starts with one of stop_prefixes (all `^## ` level)."""
    lines = text.splitlines()
    out: list[str] = []
    inside = False
    for line in lines:
        if re.match(r"^##\s+", line):
            if line.strip().startswith(heading_prefix):
                inside = True
                out.append(line)
                continue
            if inside and any(line.strip().startswith(p) for p in stop_prefixes):
                break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


# --------------------------------------------------------------------------
# corpus / case loading
# --------------------------------------------------------------------------

def domain_dir(repo: Path, sd_id: str) -> Path:
    """Map `D-01.1` to baseline/domains/D-01_Data-Protection/D-01.1/."""
    root = repo / "baseline" / "domains"
    dm = SD_RE.match(sd_id)
    if not dm:
        raise ValueError(f"not a canonical sub-domain id: {sd_id}")
    prefix = f"D-{int(sd_id[2:4]):02d}"
    for child in sorted(root.iterdir()):
        if child.is_dir() and child.name.startswith(prefix + "_"):
            sd = child / sd_id
            if sd.is_dir():
                return sd
    raise FileNotFoundError(f"sub-domain directory not found for {sd_id}")


def subdomain_name(repo: Path, sd_id: str) -> str:
    idx = domain_dir(repo, sd_id) / "_index.md"
    m = re.search(r"^#\s+D-\d{2}\.\d+\s+[—-]\s+(.+)$", idx.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else sd_id


def load_case(repo: Path, case_id: str) -> dict[str, Any]:
    case_dir = repo / "pipeline" / "cases" / case_id
    binding = parse_simple_yaml((case_dir / "case.yaml").read_text(encoding="utf-8"))
    input_path = case_dir / binding["input"]
    return {
        "case_id": case_id,
        "company_id": binding["company_id"],
        "company_name": binding["company_name"],
        "output_language": binding.get("output_language", "en"),
        "track_b_overrides": binding.get("track_b_overrides", []),
        "input_path": input_path,
        "input_text": input_path.read_text(encoding="utf-8"),
    }


def load_verdicts(run_dir: Path) -> dict[str, str]:
    """Load the P2 verdict table produced earlier in the run."""
    data = json.loads((run_dir / "steps" / "verdicts.json").read_text(encoding="utf-8"))
    return {v["regulation"]: v["verdict"] for v in data["verdicts"]}


def confirmed_regulations(run_dir: Path) -> list[str]:
    v = load_verdicts(run_dir)
    return [r for r in REGULATIONS if v.get(r, "").lower() == "applies"]


def load_selection(run_dir: Path) -> dict[str, Any]:
    return json.loads((run_dir / "steps" / "selection.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# deterministic pre-filter and packs
# --------------------------------------------------------------------------

def candidate_subdomains(repo: Path, confirmed: list[str]) -> list[dict[str, str]]:
    """Deterministic P3 pre-filter: every sub-domain whose module contains
    regs/<REG>.md for at least one confirmed regulation (ficha PROM-P1-03)."""
    root = repo / "baseline" / "domains"
    out: list[dict[str, str]] = []
    for dom in sorted(root.iterdir()):
        if not dom.is_dir():
            continue
        for sd in sorted(dom.iterdir()):
            if not (sd.is_dir() and SD_RE.match(sd.name)):
                continue
            present = [r for r in confirmed if (sd / "regs" / f"{r}.md").exists()]
            if present:
                out.append({
                    "id": sd.name,
                    "name": subdomain_name(repo, sd.name),
                    "confirmed_regs_present": present,
                    "dir": str(sd),
                })
    return out


def sub_so_objective(repo: Path, sd_id: str, reg: str) -> str:
    """The `**Objective.**` paragraph of the Sub-SO card for <REG> in
    regs/<REG>.md — the regulation-specific baseline objective, verbatim."""
    text = (domain_dir(repo, sd_id) / "regs" / f"{reg}.md").read_text(encoding="utf-8")
    # the Sub-SO yaml block anchors the card; the Objective paragraph follows it
    m_id = re.search(rf"id:\s*SG-{re.escape(sd_id)}\.{re.escape(reg)}\b", text)
    if not m_id:
        raise ValueError(f"{sd_id}/regs/{reg}.md: Sub-SO card SG-{sd_id}.{reg} not found")
    tail = text[m_id.end():]
    m = re.search(r"\*\*Objective\.\*\*\s*(.*?)(?=\n\n|\n\*\*|\Z)", tail, re.S)
    if not m:
        raise ValueError(f"{sd_id}/regs/{reg}.md: Sub-SO Objective paragraph not found "
                         f"after the SG-{sd_id}.{reg} card")
    return re.sub(r"\s+", " ", m.group(1)).strip()


def objective_paragraph(sd_dir: Path) -> str:
    """The `**Objective.**` paragraph of objective.md (subject matter for P3)."""
    text = (sd_dir / "objective.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*Objective\.\*\*\s*(.*?)(?=\n\n|\Z)", text, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def participants_line(sd_dir: Path) -> str:
    idx = (sd_dir / "_index.md").read_text(encoding="utf-8")
    m = re.search(r"^\-\s*Participants \(parsed\):\s*(.+)$", idx, re.M)
    return m.group(1).strip() if m else ""


def anchor_slice(repo: Path, sd_id: str, confirmed: list[str]) -> list[dict[str, Any]]:
    """Pre-verified anchors for one sub-domain, from the mapping store only."""
    out: list[dict[str, Any]] = []
    for reg in confirmed:
        path = repo / "baseline" / "MAPPINGS" / "sr_control_mappings" / f"{reg}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for sr in data.get("srs", []):
            if sd_id in sr.get("sub_domain", []):
                out.append({
                    "sr_id": sr.get("sr_id"),
                    "title": sr.get("title"),
                    "source_clauses": sr.get("source_clauses", []),
                    "nist_csf": sr.get("nist_csf", []),
                    "nist_pf": sr.get("nist_pf", []),
                    "nist_airmf": sr.get("nist_airmf", []),
                })
    return out


def wrap_file(relpath: str, content: str) -> str:
    return f"\n\n----- BEGIN FILE: {relpath} -----\n{content}\n----- END FILE: {relpath} -----\n"


def interactions_trim(path: Path, confirmed: list[str], keep: str = "operative") -> tuple[str, str]:
    """Keep selected sections of _interactions.md. `keep="operative"` keeps the
    CRDA aggregation sections; `keep="tensions"` keeps only the Emergent
    tensions sections (pack p4t). Flag-not-drop via the banner."""
    text = path.read_text(encoding="utf-8")
    title = text.split("\n", 1)[0]
    sections = re.split(r"(?m)^## ", text)[1:]
    keep_re = re.compile(
        r"Aggregation logic|Emergent tensions|Scope-overlap|HSO considerations|"
        r"Cross-recipient map|Participants \(CRDA") if keep == "operative" \
        else re.compile(r"Emergent tensions")
    kept, dropped_titles = [], []
    for sec in sections:
        head = sec.split("\n", 1)[0]
        if keep_re.search(head):
            kept.append("## " + sec.strip())
        else:
            dropped_titles.append(head[:60])
    banner = (f"\n> [pack trim] Full file: {path.name}. Kept {len(kept)} section(s) "
              f"for confirmed regulations ({', '.join(confirmed)}); omitted: "
              f"{'; '.join(dropped_titles) or 'none'}.\n")
    return title + "\n\n" + "\n\n".join(kept), banner


def golden_text(repo: Path) -> str:
    """The quality reference injected in the P4 pack.

    PINNED to the committed example/ document. It previously preferred
    `output/TinyTask/doc02_adjusted_goals.md` whenever that file existed, which
    made the in-prompt exemplar a function of which runs had already landed on
    this machine — a silent confound for any experiment that varies the prompt
    (EXP-04): run N's prompt was not a constant of the design. The freeze is a
    precondition for the prompt ablation and protects seeded runs from a
    mid-experiment prompt change.

    NOT synced to the cluster while the EXP-03 agent runs are in flight: the
    agent arm composes its packs through this function, and a mid-battery
    change would hand different runs different prompts.
    """
    return (repo / "example" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")


def build_pack(step: str, repo: Path, case: dict[str, Any], run_dir: Path) -> tuple[list[tuple[str, str]], str]:
    """Return (list of (relpath, content), pack_text) for a step. Deterministic."""
    files: list[tuple[str, str]] = []
    cfg = repo / "config.yaml"

    if step == "p1":
        files.append((str(case["input_path"].relative_to(repo)), case["input_text"]))
        files.append(("templates/company_input.md", (repo / "templates" / "company_input.md").read_text(encoding="utf-8")))

    elif step == "p3f":
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        files.append(("steps/verdicts.md", (run_dir / "steps" / "verdicts.md").read_text(encoding="utf-8")))
        t = (repo / "templates" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
        files.append(("templates/doc02_adjusted_goals.md §2 framing contract",
                      extract_markdown_section(t, "## §2", ["## §3"])))

    elif step == "p2":
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        s5 = extract_markdown_section(case["input_text"], "## §5", ["## §6"])
        files.append((str(case["input_path"].relative_to(repo)) + " §5", s5))
        t = (repo / "templates" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
        files.append(("templates/doc02_adjusted_goals.md §0 (deliverable contract)",
                      extract_markdown_section(t, "## §0", ["## §1"])))

    elif step == "p3":
        confirmed = confirmed_regulations(run_dir)
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        files.append(("steps/verdicts.md", (run_dir / "steps" / "verdicts.md").read_text(encoding="utf-8")))
        files.append(("baseline/domains/index.md", (repo / "baseline" / "domains" / "index.md").read_text(encoding="utf-8")))
        cands = candidate_subdomains(repo, confirmed)
        blocks = []
        for c in cands:
            sd_dir = Path(c["dir"])
            blocks.append(
                f"### {c['id']} — {c['name']}\n"
                f"Confirmed regulations present in the module: {', '.join(c['confirmed_regs_present'])}\n"
                f"Participants (parsed): {participants_line(sd_dir)}\n"
                f"Subject matter: {objective_paragraph(sd_dir)}"
            )
        header = (
            f"Deterministic pre-filter result: {len(cands)} candidate sub-domains contain at "
            f"least one confirmed regulation ({', '.join(confirmed)}). These are the only "
            f"candidates you may select from or exclude; everything else is out of scope."
        )
        files.append(("pack-p3/candidates.md", header + "\n\n" + "\n\n".join(blocks)))

    elif step.startswith("p4:"):
        sd_id = step.split(":", 1)[1]
        confirmed = confirmed_regulations(run_dir)
        sd_dir = domain_dir(repo, sd_id)
        rel = lambda p: str(p.relative_to(repo))  # noqa: E731
        trim_records: list[str] = []
        # Researcher ruling (2026-10-01): ambiguity analysis is settled in Fase 0;
        # Phase 1 applies the decided interpretation — ambiguity cards do NOT
        # enter Phase 1 packs. §5 entries are assumptions/open questions only.
        files.append((rel(sd_dir / "objective.md"), (sd_dir / "objective.md").read_text(encoding="utf-8")))
        for reg in confirmed:
            f = sd_dir / "regs" / f"{reg}.md"
            if f.exists():
                files.append((rel(f), f.read_text(encoding="utf-8")))
        if len([r for r in confirmed if (sd_dir / "regs" / f"{r}.md").exists()]) >= 2:
            # pair files are named alphabetically in the corpus (CRA-GDPR.md),
            # NOT in REGULATIONS order — the naive name never resolved, so the
            # threshold/timeline comparison the `narrowed` decision needs was
            # silently never attached
            for name in ["-".join(sorted((a, b))) + ".md"
                         for i, a in enumerate(confirmed) for b in confirmed[i + 1:]]:
                f = sd_dir / "cross" / name
                if f.exists():
                    files.append((rel(f), f.read_text(encoding="utf-8")))
            inter = sd_dir / "cross" / "_interactions.md"
            if inter.exists():
                trimmed, note = interactions_trim(inter, confirmed)
                files.append((rel(inter) + " (operative sections)", trimmed))
                trim_records.append(note)
        # control anchors are DERIVED by code (controls.py) from the mapping
        # store — the pack needs no anchor slice for the model
        t = (repo / "templates" / "doc02_adjusted_goals.md").read_text(encoding="utf-8")
        files.append(("templates/doc02_adjusted_goals.md §3 (goal table contract)",
                      extract_markdown_section(t, "## §3", ["## §4"])))
        # Worked examples of the transformation, baseline -> adjusted goal ->
        # company implication. The quality reference is the produced TinyTask
        # deliverable (38 sub-domains, 65 rows, L1 PASS). To stay non-circular
        # the exemplar is always a DIFFERENT sub-domain from the one being
        # written: the model must never see its own answer for the row it writes.
        blocks = [b for b in re.split(r"(?m)^(?=### D-)", golden_text(repo))
                  if b.lstrip().startswith("### D-") and "## §4" not in b and b.strip()]
        others = [b for b in blocks if not b.lstrip().startswith(f"### {sd_id} ")]
        exemplar = (others or blocks or [""])[0]
        if exemplar.strip():
            files.append(("output/TinyTask/doc02_adjusted_goals.md — worked example, a "
                          "DIFFERENT sub-domain showing the transformation (the block for "
                          f"{sd_id} is deliberately withheld; do not copy its text, match "
                          "its calibration)",
                          re.split(r"(?m)^## §4", exemplar)[0].strip() or exemplar.strip()))
        files.append(("SPEC.md §7 derivation rules R2–R8 (anchor integrity, "
                      "proportionality, no invention, regulation discipline)",
                      extract_section_text(repo / "SPEC.md", "## 7. Derivation rules",
                                            "## 8")))
        files.append(("steps/framing.md", (run_dir / "steps" / "framing.md").read_text(encoding="utf-8")))
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        manifest_block = (
            f"Context pack build (deterministic): sub-domain {sd_id}; confirmed "
            f"regulations {', '.join(confirmed)}.\nTrim records:{''.join(trim_records)}\n"
        )
        files.insert(0, (f"pack-p4/{sd_id}/BUILD_MANIFEST.md", manifest_block))

    elif step == "p4t":
        confirmed = confirmed_regulations(run_dir)
        selection = load_selection(run_dir)
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        blocks: list[str] = []
        for s in sorted(selection["selected"], key=lambda x: x["id"]):
            inter = domain_dir(repo, s["id"]) / "cross" / "_interactions.md"
            if not inter.exists():
                continue
            trimmed, note = interactions_trim(inter, confirmed, keep="tensions")
            blocks.append(f"### {s['id']} — {s['name']}\n\n{trimmed}\n{note}")
        header = (
            f"Tension corpus (deterministic extraction): Emergent-tensions sections of "
            f"cross/_interactions.md for the {len(selection['selected'])} selected "
            f"sub-domains, under confirmed regulations {', '.join(confirmed)}. Resolve "
            f"every tension that activates on this company; if none activates, answer "
            f"`None.`"
        )
        files.append(("pack-p4t/tensions.md", header + "\n\n" + ("\n\n".join(blocks) or "(no corpus tension sections)")))
    else:
        raise ValueError(f"unknown step: {step}")

    pack_text = "".join(wrap_file(p, c) for p, c in files)
    return files, pack_text


def compose_call(repo: Path, case: dict[str, Any], run_dir: Path, step: str,
                 subdomain: str | None = None, extra_instruction: str = "") -> dict[str, Any]:
    """Assemble the full system+user messages for one LLM call."""
    ficha_step = "p4" if step.startswith("p4:") else step
    ficha = parse_ficha(repo / "docs" / "pipeline" / "prompts" / FICHA_FILES[ficha_step])
    pack_step = step if not step.startswith("p4:") else f"p4:{subdomain}"
    files, pack_text = build_pack(pack_step, repo, case, run_dir)

    title = f"{ficha['id']} — {subdomain}" if subdomain else ficha["id"]
    extraction = not step.startswith(("p3", "p3f", "p4", "p4t"))
    system = (
        f"You are {ficha['role']}.\n{ficha['mission']}\n\n"
        "General discipline (binding):\n"
        + ("- Extract only what the attached sources state; never invent facts, IDs or anchors.\n"
           "- Use canonical identifiers exactly as they appear in the sources.\n"
           "- Flag what cannot be decided instead of dropping or guessing it.\n"
           if extraction else
           # the generative steps ADAPT the baseline into a company-proportional
           # goal: fidelity to the sources does not mean copying them, and the
           # "never invent facts" rule is scoped to the COMPANY's facts (R6),
           # never to the obligation content
           "- Keep the Sub-SO's obligation content intact: restate its full duty, do "
           "not drop a leg, and calibrate it to the company — this is adaptation, not "
           "extraction, so the goal text will not match the sources word for word.\n"
           "- Never invent a fact ABOUT THE COMPANY: every company statement traces to "
           "the fact sheet or the framing, or it is a fabrication (R6).\n"
           "- Use canonical identifiers exactly as they appear in the sources.\n"
           "- Flag what cannot be decided instead of dropping or guessing it.\n")
        + "- No tools, vendors, or implementation technologies in any statement.\n"
        f"- Produce ONLY the requested output artifact, exactly in the Output schema; no extra commentary.\n"
        f"- Output language: {case['output_language']}.\n"
    )
    user = (
        f"# Task — {title} (ficha {ficha['id']} v{ficha['version']})\n\n"
        f"{ficha['prompt_body']}\n\n"
        f"# Output schema\n\n```\n{ficha['output_schema']}\n```\n"
    )
    # the self-checks and the acceptance bar the reviewer applies are the most
    # decision-relevant text in the ficha — they must reach the model, not stay
    # in the engineering document (they were parsed and silently dropped before)
    if ficha.get("self_checks") or ficha.get("human_gate"):
        user += "\n# Self-checks (apply before answering) and acceptance bar\n"
        if ficha.get("self_checks"):
            user += "\n" + ficha["self_checks"] + "\n"
        if ficha.get("human_gate"):
            user += (f"\nThe reviewer applies this bar: {ficha['human_gate']}\n")
    if extra_instruction:
        user += f"\n{extra_instruction}\n"
    user += "\n# Attached context (verbatim files)\n" + pack_text

    return {
        "ficha": ficha,
        "system": system,
        "user": user,
        "files": [p for p, _ in files],
    }
