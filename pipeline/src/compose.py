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
    "p2o": "PROM-P2-01_OPERATIONALIZE_SUBDOMAIN.md",
    "p2d": "PROM-P2-03_SYNTHESIZE_PRINCIPLES.md",
    "p3a_map": "PROM-P3A-01_VERDICT_COVERAGE.md",
    "p3a_cards": "PROM-P3A-02_INVENTORY.md",
    "p3a_card": "PROM-P3A-03_CARD.md",
    "p3a_propose": "PROM-P3A-04_PROPOSE.md",
    "p3a_org": "PROM-P3A-05_ORG.md",
    "p3a_weave": "PROM-P3A-06_WEAVE.md",
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


def reg_module_path(repo: Path, sd_id: str, reg: str) -> Path:
    """Path of `regs/<REG>.md` for a sub-domain — which may legitimately not exist.

    A sub-domain's module carries one card per regulation that actually reaches
    it. Confirming a regulation at G-P1-B says it applies to the COMPANY, not
    that every selected sub-domain has a card for it: Case_02 confirms AI_Act
    and selects D-06.4, whose module has no AI_Act card. Reading that path
    unguarded is what killed p5 of run_sec02_p1_1979370 (job 1979980) with a
    bare FileNotFoundError naming a file the corpus never promised to have.
    Callers that require the card must check carries_reg_card() first and say
    which regulation is missing — a FileNotFoundError on a derived path is not
    a diagnosis.
    """
    return domain_dir(repo, sd_id) / "regs" / f"{reg}.md"


def carries_reg_card(repo: Path, sd_id: str, reg: str) -> bool:
    """Does this sub-domain carry a Sub-SO card for `reg`?

    Requires both halves: the module file exists, AND it declares a card whose
    id is exactly SG-<sd_id>.<reg>. The file alone is not enough — a module can
    mention a regulation in its cross-reference section without resting a
    baseline goal on it, and treating that mention as a card would invent an
    obligation.
    """
    path = reg_module_path(repo, sd_id, reg)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    return f"SG-{sd_id}.{reg}" in text


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
    """Deterministic P3 pre-filter: every sub-domain that carries a Sub-SO
    baseline goal for at least one confirmed regulation (ficha PROM-P1-03).

    The test is `carries_reg_card`, not "the module file exists". The corpus
    modularises every regulation into every sub-domain, so file presence says
    only that the layer was built — D-08.3 has a `regs/GDPR.md` that declares
    no `SG-D-08.3.GDPR`, and offering it as a candidate sent the p4 model into
    a pack with nothing to derive from: it answered "None — no Sub-SO for the
    confirmed regulations", correctly, and gate G0 then refused the run
    (run_p2c1, jobs 1996856/1996860). A candidate the baseline cannot ground is
    not a candidate — p4 would be asked to restate an obligation that has no
    baseline source, which R2 forbids.
    """
    root = repo / "baseline" / "domains"
    out: list[dict[str, str]] = []
    for dom in sorted(root.iterdir()):
        if not dom.is_dir():
            continue
        for sd in sorted(dom.iterdir()):
            if not (sd.is_dir() and SD_RE.match(sd.name)):
                continue
            present = [r for r in confirmed
                       if (sd / "regs" / f"{r}.md").exists()
                       and carries_reg_card(repo, sd.name, r)]
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
    if not carries_reg_card(repo, sd_id, reg):
        raise ValueError(
            f"{sd_id} carries no Sub-SO card for {reg}: "
            f"{reg_module_path(repo, sd_id, reg).name} is absent or declares no "
            f"SG-{sd_id}.{reg}. A confirmed regulation applies to the company, "
            f"not to every sub-domain — check the selection before deriving a goal.")
    text = reg_module_path(repo, sd_id, reg).read_text(encoding="utf-8")
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


#: Structural delimiter of one p4t sub-domain block, emitted by the pack
#: builder and consumed by `split_p4t_pack`. Since ADR-012 D1 the p4t pack is
#: sent one sub-domain at a time, so the block boundary is no longer a matter
#: of taste: it is the key the per-call slice is stored under and the order the
#: merge renumbers `T-NNN` in. An HTML comment is inert for the model and
#: exactly matchable by the splitter; a regex over the corpus prose would be
#: guessing where one sub-domain's Emergent-tensions text stops and the next
#: begins, and that guess would be invisible when it was wrong.
P4T_BLOCK_SENTINEL = "<!-- AEGIS-P4T-BLOCK {sd_id} -->"
_P4T_BLOCK_RE = re.compile(r"(?m)^<!-- AEGIS-P4T-BLOCK (D-\d{2}\.\d) -->[ \t]*$")


def p4t_blocks(repo: Path, run_dir: Path) -> list[dict[str, Any]]:
    """The p4t tension corpus, split into one block per SELECTED sub-domain.

    The monolithic p4t pack concatenated every selected sub-domain's
    Emergent-tensions section into a single prompt whose size tracked the SIZE
    OF THE SELECTION, not the regulation count (190,078 / 190,762 / 190,882 B
    for Case 01 / 02 / 03 — a 0.4 % spread across 2 -> 4 -> 5 confirmed
    regulations; 44,826 real prompt tokens on Case 03, job 1983144). ADR-012 D1
    decomposes it: one call per sub-domain, as p4 already is.

    Extracting the blocks HERE rather than splitting the concatenated pack
    afterwards is what makes both halves of D1 true at once — the per-call
    prompt is small, and each block carries the canonical sub-domain id the
    merge keys on, so no boundary is ever recovered from prose.

    `text` is the `interactions_trim(keep="tensions")` payload verbatim, so a
    per-sub-domain pack embeds exactly the bytes the monolithic pack used to.
    `has_tensions` is False for a sub-domain whose `_interactions.md` exists
    but keeps no Emergent-tensions section: there is no corpus tension material
    there, and asking a model to rule on absent material invites a fabricated
    `None.` that reads as a negative finding. Such a sub-domain is reported
    (`no_material`) and gets no call. Sub-domains with no `_interactions.md`
    at all are absent from the list, as before.
    """
    confirmed = confirmed_regulations(run_dir)
    selected = load_selection(run_dir)["selected"]
    out: list[dict[str, Any]] = []
    for s in sorted(selected, key=lambda x: x["id"]):
        inter = domain_dir(repo, s["id"]) / "cross" / "_interactions.md"
        if not inter.exists():
            continue
        text, note = interactions_trim(inter, confirmed, keep="tensions")
        out.append({
            "sd_id": s["id"], "name": s["name"], "text": text, "note": note,
            "has_tensions": bool(re.search(r"(?m)^## .*Emergent tensions", text)),
        })
    return out


def p4t_block_md(block: dict[str, Any]) -> str:
    """One sub-domain's pack block: sentinel, heading, trimmed text, banner."""
    return (P4T_BLOCK_SENTINEL.format(sd_id=block["sd_id"]) +
            f"\n### {block['sd_id']} — {block['name']}\n\n{block['text']}\n{block['note']}")


def split_p4t_pack(text: str) -> dict[str, str]:
    """Recover {sub-domain id: block} from a composed p4t pack.

    The inverse of writing `P4T_BLOCK_SENTINEL` before each block, and the
    check that the delimiter really is doing its job: a pack with no sentinel
    raises instead of falling back to a heading regex, because a silent
    fallback here would hand the merge mis-keyed sub-domain blocks.
    """
    marks = list(_P4T_BLOCK_RE.finditer(text))
    if not marks:
        raise ValueError(
            f"no {P4T_BLOCK_SENTINEL!r} delimiter in the p4t pack — the block "
            "boundaries are unrecoverable and the merge cannot be keyed")
    out: dict[str, str] = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out[m.group(1)] = text[m.start():end].strip("\n")
    return out


def prompt_digests(repo: Path) -> dict[str, str]:
    """sha256 of every ficha this run will be prompted from, plus the golden.

    A run records the sampler, the model and the git revision, but until now not
    the prompt TEXT. That is the one input the pipeline cannot reconstruct: the
    repo advances, `git rev` alone does not say which bytes of
    PROM-P1-03_SELECT_SUBDOMAINS.md a given run actually received, and a prompt
    edit is not a code edit. Comparing two runs across a prompt change without
    this is comparing different instruments.

    Cheap enough to write on every `new-run`: eight small files, once, before
    the first call. A missing file is recorded as "absent" rather than skipped —
    a silently shorter digest set would read as "unchanged".

    The p4/p4t keys below cover the half of the prompt that lives in CODE, not
    in ficha files: `p4_extra_instruction` (TERMINATION clause + ADJUSTMENT
    variant table) and `p4t_extra_instruction` (per-sub-domain scope). The m06
    run (job 1983666) exposed the gap — the badge-vocabulary rewrite changed
    the instrument with `aegis_git_rev` frozen and digests identical, so three
    instruments (rule / menu / badges) were distinguishable only by reading
    `inputs/` verbatim. Deferred import: steps imports compose.
    """
    import hashlib
    import inspect

    out: dict[str, str] = {}
    targets = {step: repo / "docs" / "pipeline" / "prompts" / fname
               for step, fname in FICHA_FILES.items()}
    targets["golden"] = repo / "example" / "doc02_adjusted_goals.md"
    for key, path in targets.items():
        try:
            out[key] = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
        except OSError:
            out[key] = "absent"
    try:
        import steps  # noqa: PLC0415 — deferred: steps imports this module
        out["p4_instruction"] = hashlib.sha256("\n".join([
            inspect.getsource(steps.p4_extra_instruction),
            inspect.getsource(steps._p4_instruction),
            repr(getattr(steps, "P4_ADJUSTMENT_VARIANTS", {})),
            repr(getattr(steps, "P4_STYLE_MARKER", "")),
            repr(getattr(steps, "P4_STYLE_VARIANTS", {})),
            repr(getattr(steps, "P4_IMPLICATION_MARKER", "")),
            repr(getattr(steps, "P4_IMPLICATION_VARIANTS", {})),
        ]).encode()).hexdigest()[:16]
        out["p4t_instruction"] = hashlib.sha256(
            inspect.getsource(steps.p4t_extra_instruction).encode()).hexdigest()[:16]
    except Exception:  # noqa: BLE001 — digesting must never block a new-run
        out["p4_instruction"] = "absent"
        out["p4t_instruction"] = "absent"
    return out


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


def _published_anchors(run_dir: Path) -> dict[str, list[str]]:
    """Objective id -> published control-anchor set, read from Phase 2 column 9.

    The same surface `check_traceability.py` T6 reads, so the anchors the model
    is offered and the anchors the gate later checks are the same list by
    construction rather than by two implementations agreeing.
    """
    import phase3 as _p3

    doc = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
    if not doc.is_file():
        return {}
    return {o["id"]: o["anchors"] for o in _p3.load_objectives(doc)}


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

    elif step == "p2d":
        # The 7 definitions are a BASELINE ASSET copied into the pack, never
        # regenerated (ADR-013 D2; ledger §3.2 — the same text in three unrelated
        # companies for 5 of 7). The local import breaks the compose<->phase2
        # module cycle: by the time build_pack runs, compose is fully loaded.
        import phase2 as _p2  # noqa: PLC0415 — local, cycle-breaking

        files.append(("steps/fact_sheet.yaml",
                      (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        blocks = []
        for p in _p2.PRINCIPLES:
            cat = next(c for c in _p2.CATEGORIES if c["n"] == p["category"])
            blocks.append(
                f"### {p['id']} — {p['name']}\n"
                f"Category {cat['n']} ({cat['title']}). Academic source: {p['source']}.\n"
                f"UNIVERSAL DEFINITION (do not restate, bind it): {p['definition']}")
        header = (
            "The 7 principles below are universal and already written. They are the "
            "BASELINE, not the work: your output is the per-company architectural "
            "constraint that instantiates each one. Do not restate a definition as a "
            "constraint — that is the single failure mode this step exists to avoid."
        )
        files.append(("pack-p2d/principles.md", header + "\n\n" + "\n\n".join(blocks)))

    elif step.startswith("p2o:"):
        sd_id = step.split(":", 1)[1]
        sd_dir = domain_dir(repo, sd_id)
        rel = lambda p: str(p.relative_to(repo))
        files.append(("steps/fact_sheet.yaml",
                      (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        obj_file = sd_dir / "objective.md"
        if obj_file.exists():
            files.append((rel(obj_file), obj_file.read_text(encoding="utf-8")))
        fname = sd_id.replace(".", "_")
        gfile = run_dir / "steps" / "goals" / f"{fname}.json"
        if gfile.exists():
            files.append((f"steps/goals/{sd_id}.json", gfile.read_text(encoding="utf-8")))

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
        # Worked example of the transformation, baseline -> adjusted goal ->
        # company implication. The quality reference is the committed TinyTask
        # golden (example/doc02_adjusted_goals.md), NOT a run deliverable: the
        # old label named output/TinyTask/, which is where this exemplar used to
        # be read from and is not where it comes from now. To stay non-circular
        # the exemplar is always a DIFFERENT sub-domain from the one being
        # written: the model must never see its own answer for the row it writes.
        # The label must name the file the model is actually being shown.
        blocks = [b for b in re.split(r"(?m)^(?=### D-)", golden_text(repo))
                  if b.lstrip().startswith("### D-") and "## §4" not in b and b.strip()]
        others = [b for b in blocks if not b.lstrip().startswith(f"### {sd_id} ")]
        exemplar = (others or blocks or [""])[0]
        if exemplar.strip():
            files.append(("example/doc02_adjusted_goals.md — worked example, a "
                          "DIFFERENT sub-domain showing the transformation, in the "
                          "exact column shape you must emit (the block for "
                          f"{sd_id} is deliberately withheld; do not copy its text, "
                          "match its calibration)",
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

    elif step == "p4t" or step.startswith("p4t:"):
        # ADR-012 D1: `p4t` (the whole selection in one prompt) is the
        # debug/whole-selection view and `p4t:<sd>` is what stage_p4t actually
        # sends. Both are built from the SAME block list, so the two views can
        # never disagree about what a sub-domain's tension material is.
        only = step.split(":", 1)[1] if ":" in step else None
        confirmed = confirmed_regulations(run_dir)
        all_blocks = p4t_blocks(repo, run_dir)
        blocks = all_blocks if only is None else [
            b for b in all_blocks if b["sd_id"] == only]
        if only is not None and not blocks:
            raise ValueError(
                f"p4t pack requested for {only}, which is not a selected sub-domain "
                f"carrying cross/_interactions.md (selection: "
                f"{', '.join(b['sd_id'] for b in all_blocks) or 'none'})")
        files.append(("steps/fact_sheet.yaml", (run_dir / "steps" / "fact_sheet.yaml").read_text(encoding="utf-8")))
        body = "\n\n".join(p4t_block_md(b) for b in blocks)
        if only is None:
            header = (
                f"Tension corpus (deterministic extraction): Emergent-tensions sections of "
                f"cross/_interactions.md for the {len(load_selection(run_dir)['selected'])} "
                f"selected sub-domains, under confirmed regulations {', '.join(confirmed)}. "
                f"Resolve every tension that activates on this company; if none activates, "
                f"answer `None.`"
            )
            files.append(("pack-p4t/tensions.md", header + "\n\n" + (body or "(no corpus tension sections)")))
        else:
            # one sub-domain per call: the deterministic build is recorded the
            # same way p4 records it, so `inputs/NNN_p4t_<sd>_user.md` names the
            # provenance of its own pack without needing the whole-selection file
            files.append((
                f"pack-p4t/{only}/tensions.md",
                (f"Tension corpus (deterministic extraction): the Emergent-tensions "
                 f"sections of cross/_interactions.md for sub-domain {only}, under "
                 f"confirmed regulations {', '.join(confirmed)}. Resolve every tension "
                 f"that activates on this company; if none activates, answer `None.`")
                + "\n\n" + (body or "(no Emergent-tensions section for this sub-domain)"),
            ))
            files.insert(0, (
                f"pack-p4t/{only}/BUILD_MANIFEST.md",
                f"Context pack build (deterministic): sub-domain {only}; confirmed "
                f"regulations {', '.join(confirmed)}; selection of "
                f"{len(load_selection(run_dir)['selected'])} sub-domains, of which this "
                f"call covers ONE (ADR-012 D1 — one p4t call per sub-domain).\n"))
    elif step.startswith("p3a_map"):
        # The coverage-mapping pack: this sub-domain's Phase 2 objectives with
        # their published anchors already attached, plus the frozen V0 card pool
        # that may carry them. Every anchor the model could name is on the page,
        # so it has nothing to invent; the anchors it did not find absent are the
        # process obligations, which the verdict vocabulary explains.
        import phase3 as _p3

        only = step.split(":", 1)[1]
        phase2_doc = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        objectives = _p3.load_objectives(phase2_doc)
        rows = [r for r in _p3.build(objectives) if r["subdomain"] == only]
        v0 = (repo / "cases" / case["case_id"] / "03_PHASE3_SPEC"
              / "part1_security_privacy" / "v0_functional_baseline"
              / "Doc01_Requirements_Elicitation_and_PUC.md")
        cards = _p3.load_v0_cards(v0)
        files.append((
            f"pack-p3a_map/{only}/VERDICT_PACK.md",
            _p3.build_verdict_pack(rows, cards)))
        files.insert(0, (
            f"pack-p3a_map/{only}/BUILD_MANIFEST.md",
            f"Context pack build (determistic): sub-domain {only}; "
            f"{len(rows)} Phase 2 objective(s) carrying their published anchor sets; "
            f"{len(cards)} frozen V0 candidate cards; one call per sub-domain "
            f"(ADR-012 D1).\n"))
    elif step.startswith("p3a_cards"):
        # Inventory pack: the company profile and the Phase 2 objectives the
        # product surface has to carry. The model proposes the card packages;
        # the objectives tell it how big that surface is.
        fact_sheet = run_dir / "steps" / "fact_sheet.yaml"
        phase2_doc = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        files.append((
            "pack-p3a_cards/FACT_SHEET.yaml",
            fact_sheet.read_text(encoding="utf-8") if fact_sheet.is_file() else "(missing)",
        ))
        files.append((
            "pack-p3a_cards/PHASE2_OBJECTIVES.md",
            phase2_doc.read_text(encoding="utf-8") if phase2_doc.is_file() else "(missing)",
        ))
        files.insert(0, (
            "pack-p3a_cards/BUILD_MANIFEST.md",
            "Context pack build (deterministic): one inventory call — fact sheet + "
            "Phase 2 objectives; the card table it returns is stored per card and "
            "each card is then driven individually.\n"))
    elif step.startswith("p3a_card:"):
        # Per-card pack: the stored inventory (the whole proposed surface, so
        # the card knows its neighbours) plus the fact sheet.
        card_id = step.split(":", 1)[1]
        inventory = run_dir / "steps" / "phase3" / "cards" / "inventory.json"
        fact_sheet = run_dir / "steps" / "fact_sheet.yaml"
        inv_text = inventory.read_text(encoding="utf-8") if inventory.is_file() else "{}"
        files.append((
            f"pack-p3a_card/{card_id.replace('.', '_')}/INVENTORY.md",
            "Proposed card inventory (the whole surface, for context):\n\n" + inv_text,
        ))
        files.append((
            f"pack-p3a_card/{card_id.replace('.', '_')}/FACT_SHEET.yaml",
            fact_sheet.read_text(encoding="utf-8") if fact_sheet.is_file() else "(missing)",
        ))
        files.insert(0, (
            f"pack-p3a_card/{card_id.replace('.', '_')}/BUILD_MANIFEST.md",
            f"Context pack build (deterministic): ONE card ({card_id}); inventory for "
            "neighbour awareness; fact sheet for the company context (R6).\n"))
    elif step.startswith("p3a_propose:"):
        # Proposal pack = the same verdict pack the mapping call saw (this
        # sub-domain's objectives with published anchors + the frozen pool)
        # PLUS the verdicts that stage produced — the proposal answers the
        # carve-outs the verdicts recorded.
        import phase3 as _p3

        only = step.split(":", 1)[1]
        phase2_doc = run_dir / "outputs" / "phase2" / "Doc01_Operational_Objectives.md"
        objectives = _p3.load_objectives(phase2_doc)
        rows = [r for r in _p3.build(objectives) if r["subdomain"] == only]
        v0 = (repo / "cases" / case["case_id"] / "03_PHASE3_SPEC"
              / "part1_security_privacy" / "v0_functional_baseline"
              / "Doc01_Requirements_Elicitation_and_PUC.md")
        cards = _p3.load_v0_cards(v0)
        base_pack = _p3.build_verdict_pack(rows, cards)
        verdict_path = run_dir / "steps" / "phase3" / f"verdicts_{only.replace('.', '_')}.json"
        verdicts = json.loads(verdict_path.read_text(encoding="utf-8")) if verdict_path.is_file() else []
        files.append((
            f"pack-p3a_propose/{only}/PROPOSAL_PACK.md",
            base_pack + "\n\n## The verdicts already recorded for this sub-domain\n\n"
            + json.dumps(verdicts, indent=1, ensure_ascii=False),
        ))
        files.insert(0, (
            f"pack-p3a_propose/{only}/BUILD_MANIFEST.md",
            f"Context pack build (deterministic): sub-domain {only}; the objectives "
            f"with published anchors, the frozen V0 pool, and the verdicts recorded "
            "for them — propose ONLY for the rows whose Action asks for a proposal.\n"))
    elif step.startswith("p3a_org:"):
        # Organizational pack: one duty — its objectives, the audited
        # disposition, and the PUBLISHED anchor set of every objective it
        # covers. The audit is human input and is carried verbatim.
        #
        # The anchors are the load-bearing part and they used to be missing: a
        # first cluster run returned carried=0/21 because the model had no valid
        # anchor on the page and reached for memory instead — copying the
        # 1-digit example from the ficha and naming CSF 1.1 categories
        # (PR.IP, PR.AC, PR.PT) that CSF 2.0 renamed. All 36 objectives across
        # the 21 ORG duties do carry a published set, so the pack now reads it
        # from the Phase 2 deliverable and hands it over.
        duty_slug = step.split(":", 1)[1]
        duties_path = run_dir / "steps" / "phase3" / "duties.json"
        duties = json.loads(duties_path.read_text(encoding="utf-8")) if duties_path.is_file() else []
        duty = next((d for d in duties if d.get("slug") == duty_slug), None)
        if duty:
            anchors_by_obj = _published_anchors(run_dir)
            for oid in duty.get("objectives", []):
                hits = anchors_by_obj.get(oid, [])
                duty.setdefault("published_anchors", {})[oid] = hits
                if not hits:
                    duty.setdefault("anchor_note", []).append(
                        f"{oid}: no published anchor set — this objective is a process "
                        f"obligation and its anchors belong in the ORGANIZATIONAL lane")
            body = json.dumps(duty, indent=1, ensure_ascii=False)
        else:
            body = f"(duty {duty_slug} not found)"
        fact_sheet = run_dir / "steps" / "fact_sheet.yaml"
        files.append((
            f"pack-p3a_org/{duty_slug}/DUTY.md",
            "The duty to specify (objectives, dispositions, warrants from the "
            "proportionality audit):\n\n" + body,
        ))
        files.append((
            f"pack-p3a_org/{duty_slug}/FACT_SHEET.yaml",
            fact_sheet.read_text(encoding="utf-8") if fact_sheet.is_file() else "(missing)",
        ))
        files.insert(0, (
            f"pack-p3a_org/{duty_slug}/BUILD_MANIFEST.md",
            f"Context pack build (deterministic): ONE organizational duty ({duty_slug}); "
            "the proportionality audit decided ORG for it — write the requirement in "
            "the proportional form the audit's warrant describes.\n"))
    elif step.startswith("p3a_weave:"):
        # Weave pack: the card as generated, plus the accepted constraints that
        # name it (or are unassigned) — the preconditions/extensions answer them.
        card_id = step.split(":", 1)[1]
        card_path = run_dir / "steps" / "phase3" / "cards" / f"{card_id.replace('.', '_')}.json"
        round_path = run_dir / "steps" / "phase3" / "round1_verdicts.json"
        card = card_path.read_text(encoding="utf-8") if card_path.is_file() else "(card missing)"
        accepted = []
        if round_path.is_file():
            state = json.loads(round_path.read_text(encoding="utf-8"))
            accepted = [p for p in state.get("accepted", [])
                        if p.get("carrier") == card_id or p.get("carrier") in (None, "", "—", "`—`")]
        files.append((
            f"pack-p3a_weave/{card_id.replace('.', '_')}/CARD.json",
            card,
        ))
        files.append((
            f"pack-p3a_weave/{card_id.replace('.', '_')}/ACCEPTED_CONSTRAINTS.md",
            json.dumps(accepted, indent=1, ensure_ascii=False) if accepted
            else "(no accepted constraints name this card — return the card unchanged, with empty Preconditions additions)",
        ))
        files.insert(0, (
            f"pack-p3a_weave/{card_id.replace('.', '_')}/BUILD_MANIFEST.md",
            f"Context pack build (deterministic): card {card_id}; the round-accepted "
            "constraints routed to it; write security preconditions and exception "
            "extensions for its use case.\n"))
    else:
        raise ValueError(f"unknown step: {step}")

    pack_text = "".join(wrap_file(p, c) for p, c in files)
    return files, pack_text


def compose_call(repo: Path, case: dict[str, Any], run_dir: Path, step: str,
                 subdomain: str | None = None, extra_instruction: str = "") -> dict[str, Any]:
    """Assemble the full system+user messages for one LLM call."""
    # the step TAG selects the pack ("p4:D-01.1", "p4t:D-04.3"); the ficha is
    # the step FAMILY. Splitting on the first colon covers both, and a
    # `startswith("p4:")` test does not — "p4t:D-04.3" is not a p4 ficha.
    ficha_step = "p4" if step.startswith("p4:") else step.split(":", 1)[0]
    ficha = parse_ficha(repo / "docs" / "pipeline" / "prompts" / FICHA_FILES[ficha_step])
    pack_step = step if not step.startswith("p4:") else f"p4:{subdomain}"
    files, pack_text = build_pack(pack_step, repo, case, run_dir)

    title = f"{ficha['id']} — {subdomain}" if subdomain else ficha["id"]
    extraction = not step.startswith(("p3", "p3f", "p4", "p4t", "p2o", "p2d"))
    if step.startswith("p2o"):
        discipline = (
            "- Operationalize the sub-domain for this company: write the operational translation paragraph "
            "and assign empirical verification attributes (method, criteria, owner) and operational rules (RULE-*).\n"
            "- Method must be strictly one of TEST, INSPECT, DEMONSTRATE, or ANALYZE.\n"
            "- Every rule statement MUST be imperative (contain SHALL or MUST).\n"
            "- Technology neutrality (R5): never cite proprietary cloud vendors (AWS, Azure, GCP, etc.).\n"
            "- Never invent facts about the company beyond fact_sheet.yaml (R6).\n")
    elif step.startswith("p2d"):
        # p2d has no Sub-SO and no obligation to keep intact — it binds a
        # baseline principle to a company. It therefore gets its own clause
        # rather than the p4 one, whose "do not drop a leg" advice would be
        # meaningless here and reads as a non sequitur to the model.
        discipline = (
            "- The universal definitions in the pack are the BASELINE, not the task. "
            "Your output binds each principle to this company's own architecture; "
            "never restate a definition as if it were the constraint.\n"
            "- Never invent a fact ABOUT THE COMPANY: every company statement traces "
            "to the fact sheet, or it is a fabrication (R6). If the fact sheet does "
            "not settle something, say so rather than filling it in.\n"
            "- Use canonical identifiers exactly as they appear in the sources.\n"
            "- Flag what cannot be decided instead of dropping or guessing it.\n")
    else:
        discipline = ("- Extract only what the attached sources state; never invent facts, IDs or anchors.\n"
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
    system = (
        f"You are {ficha['role']}.\n{ficha['mission']}\n\n"
        "General discipline (binding):\n"
        + discipline
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
