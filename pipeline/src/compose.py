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
    "p4": "PROM-P1-04_DERIVE_ADJUSTED_GOALS.md",
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
            m = re.match(rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|?\s*$", line)
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
        "human_gate": table_field("Metadata", "Human gate"),
        "prompt_body": prompt_body,
        "output_schema": schema,
        "pack_declared": pack_files,
        "source_path": str(path),
    }


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


def interactions_trim(path: Path, confirmed: list[str]) -> tuple[str, str]:
    """Keep the operative CRDA aggregation sections of _interactions.md
    (aggregation logic, tensions, scope overlap, recipients, relationships,
    considerations); drop merged Parts 2-3 summaries duplicated in the regs
    modules. Flag-not-drop via the banner."""
    text = path.read_text(encoding="utf-8")
    title = text.split("\n", 1)[0]
    sections = re.split(r"(?m)^## ", text)[1:]
    keep_re = re.compile(
        r"Aggregation logic|Emergent tensions|Scope-overlap|HSO considerations|"
        r"Cross-recipient map|Participants \(CRDA")
    kept, dropped_titles = [], []
    for sec in sections:
        head = sec.split("\n", 1)[0]
        if keep_re.search(head):
            kept.append("## " + sec.strip())
        else:
            dropped_titles.append(head[:60])
    banner = (f"\n> [pack trim] Full file: {path.name}. Kept {len(kept)} operative "
              f"section(s) for confirmed regulations ({', '.join(confirmed)}); omitted: "
              f"{'; '.join(dropped_titles) or 'none'} — merged Parts 2-3 content and the "
              f"per-pair 'Validated relationships' detail live in the regs modules and "
              f"cross/<R1>-<R2>.md pair files.\n")
    return title + "\n\n" + "\n\n".join(kept), banner


def build_pack(step: str, repo: Path, case: dict[str, Any], run_dir: Path) -> tuple[list[tuple[str, str]], str]:
    """Return (list of (relpath, content), pack_text) for a step. Deterministic."""
    files: list[tuple[str, str]] = []
    cfg = repo / "config.yaml"

    if step == "p1":
        files.append((str(case["input_path"].relative_to(repo)), case["input_text"]))
        files.append(("templates/company_input.md", (repo / "templates" / "company_input.md").read_text(encoding="utf-8")))

    elif step == "p2":
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        s5 = extract_markdown_section(case["input_text"], "## §5", ["## §6"])
        files.append((str(case["input_path"].relative_to(repo)) + " §5", s5))
        t = (repo / "templates" / "phase1_output.md").read_text(encoding="utf-8")
        files.append(("templates/phase1_output.md §2", extract_markdown_section(t, "## §2", ["## §3"])))

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
            for name in [f"{a}-{b}.md" for i, a in enumerate(confirmed) for b in confirmed[i + 1:]]:
                f = sd_dir / "cross" / name
                if f.exists():
                    files.append((rel(f), f.read_text(encoding="utf-8")))
            inter = sd_dir / "cross" / "_interactions.md"
            if inter.exists():
                trimmed, note = interactions_trim(inter, confirmed)
                files.append((rel(inter) + " (operative sections)", trimmed))
                trim_records.append(note)
        files.append((f"pack-p4/{sd_id}/anchor_slice.json",
                      json.dumps(slice_srs := anchor_slice(repo, sd_id, confirmed),
                                 ensure_ascii=False, separators=(",", ":"))))
        t = (repo / "templates" / "phase1_output.md").read_text(encoding="utf-8")
        files.append(("templates/phase1_output.md §4", extract_markdown_section(t, "## §4", ["## §5"])))
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        manifest_block = (
            f"Context pack build (deterministic): sub-domain {sd_id}; confirmed "
            f"regulations {', '.join(confirmed)}.\nTrim records:{''.join(trim_records)}\n"
        )
        files.insert(0, (f"pack-p4/{sd_id}/BUILD_MANIFEST.md", manifest_block))

    elif step == "p5":
        t = (repo / "templates" / "phase1_output.md").read_text(encoding="utf-8")
        files.append(("templates/phase1_output.md", t))
        files.append(("example/phase1_output.md", (repo / "example" / "phase1_output.md").read_text(encoding="utf-8")))
        files.append(("example/RUN_NOTES.md", (repo / "example" / "RUN_NOTES.md").read_text(encoding="utf-8")))
        spec = (repo / "SPEC.md").read_text(encoding="utf-8")
        s8 = extract_markdown_section(spec, "## 8", ["## 9"])
        files.append(("SPEC.md §8", s8))
        for name in ["fact_sheet.yaml", "verdicts.md", "selection.md"]:
            f = run_dir / "steps" / name
            if f.exists():
                files.append((f"steps/{name}", f.read_text(encoding="utf-8")))
        goals = sorted((run_dir / "steps" / "goals").glob("D-*.md")) if (run_dir / "steps" / "goals").exists() else []
        for g in goals:
            files.append((f"steps/goals/{g.name}", g.read_text(encoding="utf-8")))
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
    system = (
        f"You are {ficha['role']}.\n{ficha['mission']}\n\n"
        "General discipline (binding):\n"
        "- Extract only what the attached sources state; never invent facts, IDs or anchors.\n"
        "- Use canonical identifiers exactly as they appear in the sources.\n"
        "- Flag what cannot be decided instead of dropping or guessing it.\n"
        "- No tools, vendors, or implementation technologies in any statement.\n"
        f"- Produce ONLY the requested output artifact, exactly in the Output schema; no extra commentary.\n"
        f"- Output language: {case['output_language']}.\n"
    )
    user = (
        f"# Task — {title} (ficha {ficha['id']} v{ficha['version']})\n\n"
        f"{ficha['prompt_body']}\n\n"
        f"# Output schema\n\n```\n{ficha['output_schema']}\n```\n"
    )
    if extra_instruction:
        user += f"\n{extra_instruction}\n"
    user += "\n# Attached context (verbatim files)\n" + pack_text

    return {
        "ficha": ficha,
        "system": system,
        "user": user,
        "files": [p for p, _ in files],
    }
