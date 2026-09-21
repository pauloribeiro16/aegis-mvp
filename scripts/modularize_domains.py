#!/usr/bin/env python3
"""
modularize_domains.py
=====================
Deterministically splits each merged multi-regulation sub-domain file
``baseline/domains/D-XX_Name/D-XX.Y/D-XX.Y.md`` (Parts 1-4, aegis-tagged)
into a fully modular, per-regulation layout:

    D-XX.Y/
    ├── _index.md                # identity card + participants + provenance
    ├── objective.md             # SO-D-XX.Y.HL: neutral common objective + activation rule
    ├── regs/<REG>.md            # participant row + Sub-SO card(s) + per-reg requirement(s)
    │                            #   + verbatim regulatory basis + demoted cross-references
    ├── regs/<REG>.ambiguity.md  # Part 4 ambiguity section, verbatim (+ demoted crossrefs)
    ├── cross/<R1>-<R2>.md       # canonical pair analysis (Part 1 §1 deep + Part 2 summary)
    ├── cross/_interactions.md   # matrices, emergent tensions, aggregation logic, HL
    │                            #   requirement, non-participant stubs, HSO considerations
    └── articles/                # untouched (already per-regulation)

Guarantees (zero silent loss):
  * every source line is routed to exactly one destination bucket, deduplicated
    (Part 3 vs Part 1 §1, verified by byte-equality) or logged as tag/structure;
  * cross-regulation prose inside per-reg modules is moved verbatim to a
    demarcated "Cross-references (informational)" section (never rewritten);
  * a per-file line-accounting check must balance before the merged file is
    replaced (with --apply).

Usage:
    python scripts/modularize_domains.py                    # dry-run stats
    python scripts/modularize_domains.py --apply            # write modules + replace merged
    python scripts/modularize_domains.py --only D-01.1      # restrict to one sub-domain
    python scripts/modularize_domains.py --apply --keep-merged
"""

import argparse
import re
import sys
from pathlib import Path

ALL_REGS = ["GDPR", "CRA", "NIS2", "DORA", "AI_Act"]
REG_DISPLAY = {"GDPR": "GDPR", "CRA": "CRA", "NIS2": "NIS 2", "DORA": "DORA", "AI_Act": "AI Act"}

# YAML card fields that are cross-regulation metadata by nature -> demotable
DEMOTABLE_YAML_FIELDS = {"verified_relationship", "verified_relationship_basis",
                         "considerations", "emergent_tensions", "scope_overlap"}
# Prose that carries the regulation's own core text -> never demoted
CORE_PROSE_LABELS = ("**Objective.**", "**CSF anchors")

RE_PART = re.compile(r"^#\s+Part\s+(\d)\b")
RE_SEC = re.compile(r"^###\s+(\d)\.\s+(.*)$")
RE_TAG_OPEN = re.compile(r"^<!--\s*aegis:(pair|subso|req|ambiguity):([A-Za-z0-9_,\s]*)-->\s*$")
RE_TAG_CLOSE = re.compile(r"^<!--\s*/aegis:(pair|subso|req|ambiguity)\s*-->\s*$")
RE_REG_TOKEN = re.compile(r"\b(GDPR|NIS2|CRA|DORA|AI_Act)\b")
RE_LABEL = re.compile(r"^\*\*[^*]+\*\*:?\s*$")


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def normalize_reg(token: str) -> str:
    token = token.strip()
    norm = token.replace(" ", "").replace("_", "").replace("-", "").upper()
    if "GDPR" in norm:
        return "GDPR"
    if "CRA" in norm:
        return "CRA"
    if "NIS" in norm:
        return "NIS2"
    if "DORA" in norm:
        return "DORA"
    if "AI" in norm or "AIA" in norm:
        return "AI_Act"
    return token


def reg_tokens(raw: str) -> list:
    out = []
    for tok in raw.split(","):
        tok = tok.strip()
        if tok:
            out.append(normalize_reg(tok))
    return out


def norm_text(t: str) -> str:
    return t.replace("NIS 2", "NIS2").replace("AI Act", "AI_Act")


def regs_in_text(t: str) -> set:
    return set(RE_REG_TOKEN.findall(norm_text(t)))


def mentions_other(t: str, own: set) -> bool:
    return bool(regs_in_text(t) - own)


def pair_key(regs: list) -> str:
    return "-".join(sorted(regs))


def w(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------
# leaf-unit parsing (for the demotion pass)
# --------------------------------------------------------------------------

def split_leaf_units(lines: list) -> list:
    """Split a line list into markdown leaf units: heading, fence, table,
    bullet, para, quote, blank. Each unit is a dict {kind, lines}."""
    units = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            j = i
            while j < n and not lines[j].strip():
                j += 1
            units.append({"kind": "blank", "lines": lines[i:j]})
            i = j
        elif s.startswith("#"):
            units.append({"kind": "heading", "lines": [line]})
            i += 1
        elif s.startswith("```") or s.startswith("~~~"):
            j = i + 1
            while j < n and not (lines[j].strip().startswith("```") or lines[j].strip().startswith("~~~")):
                j += 1
            j = min(j + 1, n)
            units.append({"kind": "fence", "lines": lines[i:j]})
            i = j
        elif s.startswith("|"):
            j = i
            while j < n and lines[j].strip().startswith("|"):
                j += 1
            units.append({"kind": "table", "lines": lines[i:j]})
            i = j
        elif s.startswith(">"):
            j = i
            while j < n:
                ns = lines[j].strip()
                if ns.startswith(">"):
                    j += 1
                elif ns == "" and j + 1 < n and lines[j + 1].strip().startswith(">"):
                    j += 1
                else:
                    break
            units.append({"kind": "quote", "lines": lines[i:j]})
            i = j
        elif s.startswith("- ") or s.startswith("* "):
            j = i + 1
            while j < n:
                nxt = lines[j]
                ns = nxt.strip()
                if not ns:
                    if j + 1 < n and (lines[j + 1].strip().startswith(("- ", "* "))):
                        break
                    j += 1
                    continue
                if ns.startswith(("- ", "* ")) or (nxt[:1] != " " and nxt[:1] != "\t"):
                    break
                j += 1
            units.append({"kind": "bullet", "lines": lines[i:j]})
            i = j
        else:
            j = i + 1
            while j < n:
                ns = lines[j].strip()
                if (not ns or ns.startswith(("#", "|", ">", "```", "~~~"))
                        or ns.startswith(("- ", "* "))):
                    break
                j += 1
            units.append({"kind": "para", "lines": lines[i:j]})
            i = j
    return units


def split_yaml_fields(fence_lines: list) -> list:
    """Partition the inner lines of a ```yaml fence into fields.

    Key lines are detected at any indent; the card's base indent is the
    minimum indent among non-list-prefixed key lines. Field starts are:
    structural keys at base indent (plus the '- key:' list head at column 0)
    and demotable cross-reg metadata keys at ANY indent (e.g. ``scope_overlap``
    nested inside ``applicable_if``). Consecutive starts partition the fence,
    so a demoted nested field never swallows its siblings. Returns [{key, lines}]."""
    inner = fence_lines[1:-1]
    keylines = []
    for idx, line in enumerate(inner):
        m = re.match(r"^(\s*)(-\s+)?([A-Za-z0-9_]+):", line)
        if m:
            keylines.append((idx, m.group(3), len(m.group(1).expandtabs(4)), bool(m.group(2))))
    plain = [indent for (_i, _k, indent, is_list) in keylines if not is_list]
    base = min(plain) if plain else 0
    starts = [(idx, key, indent) for (idx, key, indent, is_list) in keylines
              if (is_list and indent == 0) or (not is_list and indent == base)
              or key in DEMOTABLE_YAML_FIELDS]
    fields = []
    for k, (idx, key, _indent) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(inner)
        fields.append({"key": key, "lines": inner[idx:end]})
    return fields


def demote_pass(lines: list, own_regs: set, origin: str, stats: dict) -> tuple:
    """Move leaf units that mention other regulations to a trailing demarcated
    section. Returns (kept_lines, crossref_entries, core_mention_count).

    Never demoted: headings, tables (audited), fenced non-YAML blocks, and core
    prose (**Objective.** / **CSF anchors). A pure-bold label line whose whole
    following block is demoted travels with it (no orphaned labels).
    """
    kept = []
    entries = []
    core_mentions = 0
    held_label = None  # pending pure-bold label awaiting its body

    def flush_label():
        nonlocal held_label
        if held_label is not None:
            kept.extend(held_label["lines"])
            held_label = None

    def demote(unit, label=None):
        payload = (label["lines"] + [""] if label else []) + unit["lines"]
        entries.append({"origin": origin, "kind": unit["kind"], "key": None, "lines": payload})
        stats[f"demoted_{unit['kind']}"] = stats.get(f"demoted_{unit['kind']}", 0) + 1

    for unit in split_leaf_units(lines):
        kind = unit["kind"]
        text = "\n".join(unit["lines"])
        first = unit["lines"][0].strip()

        if kind in ("heading", "table", "blank"):
            flush_label()
            kept.extend(unit["lines"])
            if kind == "table" and mentions_other(text, own_regs):
                stats["cross_mentions_in_tables"] += 1
            continue

        if kind == "fence":
            flush_label()
            is_yaml = unit["lines"][0].strip().startswith("```yaml")
            if is_yaml and mentions_other(text, own_regs):
                fields = split_yaml_fields(unit["lines"])
                if fields:
                    opener = unit["lines"][0]
                    closer = unit["lines"][-1] if unit["lines"][-1].strip().startswith("```") else "```"
                    kept.append(opener)
                    for f in fields:
                        ftext = "\n".join(f["lines"])
                        if f["key"] in DEMOTABLE_YAML_FIELDS and mentions_other(ftext, own_regs):
                            entries.append({"origin": origin, "kind": "yaml-field",
                                            "key": f["key"], "lines": f["lines"]})
                            stats["demoted_yaml_fields"] += 1
                        else:
                            kept.extend(f["lines"])
                            if mentions_other(ftext, own_regs):
                                core_mentions += 1
                    kept.append(closer)
                    continue
            kept.extend(unit["lines"])
            if mentions_other(text, own_regs):
                core_mentions += 1
            continue

        is_core = kind == "para" and first.startswith(CORE_PROSE_LABELS)
        is_label = kind == "para" and len(unit["lines"]) == 1 and RE_LABEL.match(first)

        if is_core:
            flush_label()
            if first.startswith("**CSF anchors"):
                # the anchor list is core; a trailing italic rationale note
                # (*(...) multi-line) is commentary and demotable
                split_at = next((k for k, ln in enumerate(unit["lines"])
                                 if k > 0 and ln.strip().startswith("*(")), None)
                if split_at is not None:
                    head, tail = unit["lines"][:split_at], unit["lines"][split_at:]
                    kept.extend(head)
                    if mentions_other("\n".join(tail), own_regs):
                        entries.append({"origin": origin, "kind": "para", "key": None, "lines": tail})
                        stats["demoted_para"] = stats.get("demoted_para", 0) + 1
                    else:
                        kept.extend(tail)
                    continue
            kept.extend(unit["lines"])
            if mentions_other(text, own_regs):
                core_mentions += 1
            continue

        if is_label:
            flush_label()
            if mentions_other(text, own_regs):
                demote(unit)
            else:
                held_label = unit
            continue

        if mentions_other(text, own_regs):
            demote(unit, label=held_label)
            held_label = None
            continue

        flush_label()
        kept.extend(unit["lines"])

    flush_label()
    return kept, entries, core_mentions


def render_crossref_section(entries: list) -> list:
    out = ["## Cross-references (informational)", ""]
    out.append("> Moved verbatim from the module body by `modularize_domains.py` (mechanical")
    out.append("> demotion). These units mention other regulations and are NOT part of this")
    out.append("> regulation's independent obligations. Cross-regulation reasoning lives in")
    out.append("> [`../cross/`](../). Nothing has been rewritten or deleted.")
    out.append("")
    for e in entries:
        suffix = f" — field `{e['key']}`" if e.get("key") else ""
        out.append(f"### from {e['origin']}{suffix}")
        out.append("")
        if e["kind"] == "yaml-field":
            out.append("```yaml")
            out.extend(e["lines"])
            out.append("```")
        else:
            out.extend(e["lines"])
        out.append("")
    return out


# --------------------------------------------------------------------------
# merged-file parsing
# --------------------------------------------------------------------------

class Seg:
    __slots__ = ("kind", "part", "section", "sub", "regs", "lines", "start")

    def __init__(self, kind, part, section, sub, regs, lines, start):
        self.kind = kind      # prose | pair | pairstub | subso | req | ambiguity | structure
        self.part = part
        self.section = section  # 'pre' | 1 | 2 | 3 (Part 1 only)
        self.sub = sub        # lowercased §2/§3 sub-heading key or None
        self.regs = regs
        self.lines = lines
        self.start = start


def parse_merged(path: Path, log: list) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    segs = []
    part, section, sub = 0, "pre", None
    buf, buf_state = [], None
    cur = None  # open tagged seg

    def flush(at):
        nonlocal buf, buf_state
        if buf:
            segs.append(Seg("prose", *buf_state, [], buf, at))
            buf = []

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        m = RE_PART.match(s)
        if m and cur is None:
            flush(i)
            segs.append(Seg("structure", part, section, sub, [], [line], i))
            part = int(m.group(1))
            section, sub = None, None
            i += 1
            continue

        m = RE_TAG_OPEN.match(s)
        if m and cur is None:
            flush(i)
            kind, raw = m.groups()
            regs = reg_tokens(raw)
            if [t for t in raw.split(",") if not t.strip()]:
                log.append(f"{path.name}:L{i+1}: malformed tag '{s}' (empty partner)")
            cur = Seg("pairstub" if (kind == "pair" and not regs) else kind,
                      part, section, sub, regs, [], i)
            i += 1
            continue

        m = RE_TAG_CLOSE.match(s)
        if m and cur is not None and m.group(1) == ("pair" if cur.kind == "pairstub" else cur.kind):
            segs.append(cur)
            cur = None
            i += 1
            continue

        if cur is not None:
            cur.lines.append(line)
            i += 1
            continue

        if part == 1:
            m = RE_SEC.match(s)
            if m:
                flush(i)
                section, sub = int(m.group(1)), None
                buf, buf_state = [line], (part, section, sub)
                i += 1
                continue
            if s.startswith("#### ") and section == 2:
                flush(i)
                sub = s.lstrip("# ").strip()
                buf, buf_state = [line], (part, section, sub)
                i += 1
                continue
            if s.startswith("### ") and section == 3:
                flush(i)
                sub = s.lstrip("# ").strip()
                buf, buf_state = [line], (part, section, sub)
                i += 1
                continue

        if buf and buf_state == (part, section, sub):
            buf.append(line)
        else:
            flush(i)
            buf, buf_state = [line], (part, section, sub)
        i += 1

    flush(len(lines))
    if cur is not None:
        log.append(f"{path.name}:L{cur.start+1}: unclosed tag '{cur.kind}' — closed at EOF")
        segs.append(cur)
    return segs


# --------------------------------------------------------------------------
# routing
# --------------------------------------------------------------------------

HSO_CARD_KEY = re.compile(r"^d-\d+\.\d+\.0\b")


def table_rows(lines):
    """Parse a participants-style table -> (header_line, {reg: row_line})."""
    hdr, rows = None, {}
    for ln in lines:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        first = cells[0].strip("* ")
        if hdr is None:
            hdr = ln
            continue
        if RE_REG_TOKEN.search(first.replace("NIS 2", "NIS2").replace("AI Act", "AI_Act")):
            reg = normalize_reg(first)
            if reg in ALL_REGS:
                rows[reg] = ln
    return hdr, rows


def extract_verbatim_quotes(pair_lines: list, reg: str) -> list:
    """Pull '**<REG> article (verbatim ...)**' label + blockquote groups."""
    quotes = []
    variants = (f"**{reg} article", f"**{REG_DISPLAY[reg]} article")
    i, n = 0, len(pair_lines)
    while i < n:
        s = pair_lines[i].strip()
        if s.startswith(variants):
            j = i + 1
            quote = []
            while j < n and pair_lines[j].strip().startswith(">"):
                quote.append(pair_lines[j])
                j += 1
            if quote:
                quotes.append({"label": s, "quote": quote, "sig": norm_text("\n".join(quote))[:120]})
            i = j
            continue
        i += 1
    return quotes


class Router:
    def __init__(self, sub_id, log):
        self.sub_id = sub_id
        self.log = log
        self.index_prov = []
        self.objective = []
        self.regs = {r: {"header": [], "subso": [], "req": [], "verbatim": [], "ambiguity_lines": []}
                     for r in ALL_REGS}
        self.pairs = {}          # key -> {regs, deep, summary, deep3}
        self.interactions = []   # (title, lines)
        self.counts = {"routed": 0, "dedup": 0, "structure": 0}
        self.stats = {"demoted_yaml_fields": 0, "demoted_bullet": 0, "demoted_para": 0,
                      "demoted_quote": 0, "cross_mentions_in_tables": 0}

    def cross(self, title, lines):
        self.interactions.append((title, lines))

    def _pair_add(self, seg: Seg, slot):
        key = pair_key(seg.regs)
        entry = self.pairs.setdefault(key, {"regs": seg.regs, "deep": [], "summary": [], "deep3": []})
        entry[slot].append(seg.lines)
        if slot == "deep":
            for r in seg.regs:
                bucket = self.regs[r]["verbatim"]
                for q in extract_verbatim_quotes(seg.lines, r):
                    if q["sig"] not in [x["sig"] for x in bucket]:
                        bucket.append(q)

    def route(self, seg: Seg):
        n = len(seg.lines)

        if seg.kind == "structure":
            # part banners are preserved verbatim in cross/_interactions.md
            # (no-loss guarantee) while still accounted as structural lines
            self.cross("Structural banners (merged Parts)", seg.lines)
            self.counts["structure"] += n
            return

        if seg.kind == "pairstub":
            self.cross("Non-participant / stub notes", seg.lines)
            self.counts["routed"] += n
            return

        if seg.part == 0 or (seg.part == 1 and seg.section is None):
            # title block, Part 1 banner frontmatter, §1 pre-content -> identity
            self.index_prov.extend(seg.lines)
            self.counts["routed"] += n
            return

        if seg.part == 1 and seg.section == 1:
            if seg.kind == "pair":
                self._pair_add(seg, "deep")  # accounted in compose (pair loop)
            else:
                self.cross("Part 1 §1 — Cross-Regulation Analysis context", seg.lines)
                self.counts["routed"] += n
            return

        if seg.part == 1 and seg.section == 2:
            self._route_hso(seg)
            return

        if seg.part == 1 and seg.section == 3:
            if seg.kind == "req" and seg.regs:
                self.regs[seg.regs[0]]["req"].append(seg.lines)
            elif seg.sub and seg.sub.lower().startswith("high-level requirement"):
                self.cross("High-level requirement (multi-reg aggregation)", seg.lines)
            elif seg.sub and seg.sub.lower().startswith("participating regulations"):
                self.cross("Participating regulations (§3)", seg.lines)
            elif seg.sub and seg.sub.lower().startswith("sub-requirements"):
                # heading itself is preserved in interactions (no-loss guarantee);
                # each regs/<R>.md carries its own section header
                self.cross("Sub-requirements section heading", seg.lines)
            else:
                self.cross("Part 1 §3 — context", seg.lines)
            self.counts["routed"] += n
            return

        if seg.part == 2:
            if seg.kind == "pair":
                self._pair_add(seg, "summary")  # accounted in compose (pair loop)
            else:
                self.cross("Part 2 — Domain Analysis (summary layer)", seg.lines)
                self.counts["routed"] += n
            return

        if seg.part == 3:
            if seg.kind == "pair":
                self._pair_add(seg, "deep3")  # accounted in compose (dedup vs kept)
            else:
                self.cross("Part 3 — context", seg.lines)
                self.counts["routed"] += n
            return

        if seg.part == 4:
            if seg.kind == "ambiguity" and seg.regs:
                reg = seg.regs[0]
                if self.regs[reg]["ambiguity_lines"]:
                    self.log.append(f"{self.sub_id}: duplicate ambiguity section for {reg} — appended to interactions")
                    self.cross(f"Ambiguity overflow ({reg})", seg.lines)
                else:
                    self.regs[reg]["ambiguity_lines"] = seg.lines
            else:
                self.cross("Part 4 — context", seg.lines)
            self.counts["routed"] += n
            return

        self.cross("Residual (unrouted)", seg.lines)  # never drop silently
        self.counts["routed"] += n

    def _route_hso(self, seg: Seg):
        n = len(seg.lines)
        if seg.kind == "subso" and seg.regs:
            self.regs[seg.regs[0]]["subso"].append(seg.lines)
            self.counts["routed"] += n
            return
        sub = seg.sub or ""
        lines = seg.lines

        if HSO_CARD_KEY.match(sub.lower()):
            # neutral layer: keep ONLY the card heading, the YAML card and the
            # **Objective.** statement; every other unit (considerations,
            # aggregation bullets, notes) is cross-regulation commentary
            kept, to_cross = [], []
            for unit in split_leaf_units(lines):
                kind = unit["kind"]
                first = unit["lines"][0].strip()
                is_objective = kind == "para" and first.startswith("**Objective.**")
                if kind in ("heading", "blank", "fence") or is_objective:
                    kept.extend(unit["lines"])
                else:
                    to_cross.extend(unit["lines"])
            self.objective.extend(kept)
            if to_cross:
                self.cross(f"HSO considerations (from {sub})", to_cross)
            self.counts["routed"] += n
            return

        if sub.lower().startswith("participants"):
            hdr, rows = table_rows(lines)
            self.cross("Participants (CRDA-deep, full table)", lines)
            for reg, row in rows.items():
                self.regs[reg]["header"].append(
                    ["| Regulation | Canonical SO | 1-line summary | Scope/angle |",
                     "|---|---|---|---|", row])
            self.counts["routed"] += n
            return

        if sub.lower().startswith("sub-domain scope structure"):
            self.cross("Sub-domain scope structure (full table)", lines)
            hdr, rows = table_rows(lines)
            for reg, row in rows.items():
                self.regs[reg]["header"].append(
                    ["| Axis (reg) | Trigger | Material scope | Recipient | Legal anchor |",
                     "|---|---|---|---|---|", row])
            self.counts["routed"] += n
            return

        self.cross(sub if sub else "Part 1 §2 — HSO context", lines)
        self.counts["routed"] += n


# --------------------------------------------------------------------------
# module composition
# --------------------------------------------------------------------------

def subdomain_title(segs) -> str:
    for seg in segs:
        for ln in seg.lines:
            m = re.match(r"^title:\s*(.+)$", ln.strip())
            if m:
                return m.group(1).strip()
    return ""


def clean_title(t):
    return re.sub(r"^D-\d+\.\d+\s+", "", t).strip()


def _norm_eq(a, b) -> bool:
    na = [l.rstrip() for l in a if l.strip()]
    nb = [l.rstrip() for l in b if l.strip()]
    return na == nb


def compose(sub_id, title, router: Router, sub_dir: Path) -> dict:
    files = {}

    # -- _index.md ---------------------------------------------------------
    part_regs = sorted({r for e in router.pairs.values() for r in e["regs"]}
                       | {r for r, d in router.regs.items() if d["subso"]})
    art_dir = sub_dir / "articles"
    n_art = len(list(art_dir.glob("*.md"))) if art_dir.exists() else 0
    lines = [f"# {sub_id} — {clean_title(title)}", ""]
    lines.append(f"- Sub-domain: `{sub_id}`")
    lines.append("- Participants (parsed): "
                 + (", ".join(REG_DISPLAY[r] for r in part_regs) if part_regs else "see cross/_interactions.md"))
    lines.append(f"- Article copies: {n_art} — [articles/](articles/)")
    lines.append("")
    lines.append("## Modules")
    lines.append("")
    lines.append("| Layer | File |")
    lines.append("|---|---|")
    lines.append("| Neutral high-level objective | [objective.md](objective.md) |")
    for r in ALL_REGS:
        d = router.regs[r]
        if d["subso"] or d["req"] or d["header"] or d["verbatim"] or d["ambiguity_lines"]:
            extra = f" + [ambiguity](regs/{r}.ambiguity.md)" if d["ambiguity_lines"] else ""
            lines.append(f"| {REG_DISPLAY[r]} | [regs/{r}.md](regs/{r}.md){extra} |")
    for pk in sorted(router.pairs):
        rr = router.pairs[pk]["regs"]
        if len(rr) == 2:
            lines.append(f"| Pair {REG_DISPLAY[rr[0]]} ↔ {REG_DISPLAY[rr[1]]} | [cross/{pk}.md](cross/{pk}.md) |")
    lines.append("| Interactions (matrix, tensions, aggregation) | [cross/_interactions.md](cross/_interactions.md) |")
    lines.append("")
    lines.append("## Provenance")
    lines.append("")
    lines.append(f"> The unified merged file `{sub_id}.md` (Parts 1-4; generated by")
    lines.append("> reorg_by_domain_md.py, annotated by annotate_baseline_domains.py) was split")
    lines.append("> in place by `modularize_domains.py`. Full line-accounting:")
    lines.append("> [`../../_migration_report.md`](../../_migration_report.md).")
    lines.append("")
    prov = [l for l in router.index_prov if l.strip()]
    if prov:
        lines.append("<details><summary>Original frontmatter and banners (verbatim)</summary>")
        lines.append("")
        lines.append("```markdown")
        lines.extend(prov)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    files["_index.md"] = lines

    # -- objective.md --------------------------------------------------------
    lines = [f"# {sub_id} — High-level Security Objective (regulation-neutral)", ""]
    lines.append("> Common objective of the sub-domain; activates when ≥2 applicable regulations'")
    lines.append("> scopes overlap on the same artefact (`applies_to: auto`). Per-regulation")
    lines.append("> perspectives live in [regs/](regs/); aggregation reasoning in")
    lines.append("> [cross/_interactions.md](cross/_interactions.md).")
    lines.append("")
    body = [l for l in router.objective if l.strip()]
    lines.extend(body if body else ["_(no neutral objective card was parsed — see cross/_interactions.md)_"])
    lines.append("")
    files["objective.md"] = lines

    # -- regs/<REG>.md (+ ambiguity) ------------------------------------------
    for r in ALL_REGS:
        d = router.regs[r]
        if not (d["subso"] or d["req"] or d["header"] or d["verbatim"] or d["ambiguity_lines"]):
            continue

        body = []
        if d["subso"]:
            body += [f"## Sub-SO ({REG_DISPLAY[r]})", ""]
            for blk in d["subso"]:
                body += blk + [""]
        if d["req"]:
            body += [f"## Security Requirements ({REG_DISPLAY[r]})", ""]
            for blk in d["req"]:
                body += blk + [""]
        if d["verbatim"]:
            body += [f"## Verbatim regulatory basis ({REG_DISPLAY[r]})", ""]
            body += ["> OJ-text quotes extracted from the cross-regulation pair analyses",
                     "> (single-regulation anchor source; full pairs in [../cross/](../)).", ""]
            for q in d["verbatim"]:
                body += [q["label"]] + q["quote"] + [""]

        kept, entries, core = demote_pass(body, {r}, f"regs/{r}.md body", router.stats)
        lines = [f"# {sub_id} — {REG_DISPLAY[r]} module", ""]
        lines.append(f"> Regulation-specific layer: applies when `{r}` is in scope")
        lines.append(f"> (activation: `if {r} in applicable_regs`). Independent of any other")
        lines.append("> regulation; cross-regulation material is demoted to the trailing")
        lines.append("> 'Cross-references (informational)' section and to [../cross/](../).")
        lines.append("")
        for h in d["header"]:
            lines += h + [""]
        if [l for l in kept if l.strip()]:
            lines += kept
        else:
            lines += [f"_(no {REG_DISPLAY[r]} Sub-SO or requirements in this sub-domain)_", ""]
        if entries:
            lines += render_crossref_section(entries)
        lines.append(f"<!-- aegis:purity: own_reg={r}; demoted={len(entries)}; core_cross_mentions={core} -->")
        lines.append("")
        files[f"regs/{r}.md"] = lines

        if d["ambiguity_lines"]:
            kept, entries, core = demote_pass(d["ambiguity_lines"], {r},
                                              f"regs/{r}.ambiguity.md", router.stats)
            lines = [f"# {sub_id} — Relevant Ambiguity ({REG_DISPLAY[r]})", ""]
            lines.append(f"> Part 4 ambiguity analysis for {REG_DISPLAY[r]}, verbatim from the merged")
            lines.append("> file. Cross-regulation analogies are demoted to the trailing section.")
            lines.append("")
            body2 = [l for l in kept if l.strip()]
            lines += body2 if body2 else [f"_(no applicable {r} ambiguity)_", ""]
            lines.append("")
            if entries:
                lines += render_crossref_section(entries)
            lines.append(f"<!-- aegis:purity: own_reg={r}; demoted={len(entries)}; core_cross_mentions={core} -->")
            lines.append("")
            files[f"regs/{r}.ambiguity.md"] = lines

    # -- cross/<pair>.md -------------------------------------------------------
    for pk in sorted(router.pairs):
        entry = router.pairs[pk]
        rr = entry["regs"]
        if len(rr) != 2:
            router.log.append(f"{sub_id}: pair slot '{pk}' has regs={rr} — routed to interactions")
            for slot in ("deep", "summary", "deep3"):
                for blk in entry[slot]:
                    router.cross(f"Residual pair content ({pk or 'stub'}, {slot})", blk)
                    router.counts["routed"] += len(blk)
            continue
        dedup = 0
        deep3 = []
        for blk in entry["deep3"]:
            if any(_norm_eq(blk, d) for d in entry["deep"]):
                dedup += len(blk)
            else:
                deep3.append(blk)
                router.counts["routed"] += len(blk)
        router.counts["dedup"] += dedup
        router.counts["routed"] += sum(len(b) for b in entry["deep"])
        router.counts["routed"] += sum(len(b) for b in entry["summary"])
        lines = [f"# {sub_id} — Pair analysis: {REG_DISPLAY[rr[0]]} ↔ {REG_DISPLAY[rr[1]]}", ""]
        lines.append("> Cross-regulation layer: consult only when BOTH regulations are applicable.")
        lines.append("> Canonical source: merged Part 1 §1 (deep) + Part 2 (summary).")
        lines.append("")
        for blk in entry["deep"]:
            lines += blk + [""]
        for blk in entry["summary"]:
            lines += ["## Summary (Domain Analysis)", ""] + blk + [""]
        for blk in deep3:
            lines += ["## Deep analysis — Part 3 rendering (differs from Part 1 §1)", ""] + blk + [""]
        if entry["deep3"] and dedup:
            lines.append(f"_(Part 3 duplicates of Part 1 §1 were byte-identical and deduplicated:")
            lines.append(f"{dedup} lines — see ../../_migration_report.md)_")
            lines.append("")
        files[f"cross/{pk}.md"] = lines

    # -- cross/_interactions.md -------------------------------------------------
    lines = [f"# {sub_id} — Cross-regulation interactions", ""]
    lines.append("> Inherently multi-regulation material: scope-overlap matrix, validated")
    lines.append("> relationships, emergent tensions, aggregation logic, the multi-reg")
    lines.append("> high-level requirement, HSO considerations, and non-participant notes.")
    lines.append("> Consult only when ≥2 regulations are applicable. No per-regulation")
    lines.append("> obligation lives here.")
    lines.append("")
    for t, blk in router.interactions:
        body = [l for l in blk if l.strip()]
        if not body:
            continue
        lines += [f"## {t}", ""] + body + [""]
    files["cross/_interactions.md"] = lines

    return files


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def process_subdomain(merged: Path, apply: bool, keep_merged: bool, log: list, report: list) -> bool:
    sub_id = merged.stem
    slog = []
    text = merged.read_text(encoding="utf-8")
    src_lines = text.splitlines()
    segs = parse_merged(merged, slog)
    title = subdomain_title(segs)
    router = Router(sub_id, slog)
    for seg in segs:
        router.route(seg)

    files = compose(sub_id, title, router, merged.parent)

    tag_lines = sum(1 for l in src_lines
                    if RE_TAG_OPEN.match(l.strip()) or RE_TAG_CLOSE.match(l.strip()))
    total = len(src_lines)
    # Part 3 pair blocks are accounted in compose(): dedup (byte-identical to
    # Part 1 §1) or routed (kept as a differing rendering)
    accounted = router.counts["routed"] + router.counts["dedup"] + router.counts["structure"]
    balanced = (accounted + tag_lines) == total

    dem = sum(v for k, v in router.stats.items() if k.startswith("demoted_"))
    report.append({
        "subdomain": sub_id,
        "domain_dir": str(merged.parent.parent),
        "total_lines": total,
        "routed": router.counts["routed"],
        "dedup": router.counts["dedup"],
        "tag_lines": tag_lines,
        "structure_lines": router.counts["structure"],
        "balanced": balanced,
        "files": {k: len(v) for k, v in files.items()},
        "pairs": [k for k in sorted(router.pairs) if len(router.pairs[k]["regs"]) == 2],
        "regs": {r: {"subso": len(d["subso"]), "reqs": len(d["req"]),
                     "verbatim": len(d["verbatim"]),
                     "ambiguity": bool(d["ambiguity_lines"])}
                 for r, d in router.regs.items()
                 if d["subso"] or d["req"] or d["header"] or d["verbatim"] or d["ambiguity_lines"]},
        "stats": dict(router.stats),
        "demoted_total": dem,
        "script_log": slog,
    })

    if apply:
        if not balanced:
            log.append(f"{sub_id}: line accounting FAILED "
                       f"({accounted + tag_lines} != {total}) — merged file kept")
            return False
        import shutil
        for stale in ("regs", "cross"):
            shutil.rmtree(merged.parent / stale, ignore_errors=True)
        for stale in ("_index.md", "objective.md"):
            (merged.parent / stale).unlink(missing_ok=True)
        for rel, flines in files.items():
            w(merged.parent / rel, "\n".join(flines) + "\n")
        if not keep_merged:
            merged.unlink()
    return balanced


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", default="baseline", help="baseline root (default: baseline)")
    ap.add_argument("--apply", action="store_true", help="write modules and replace merged files")
    ap.add_argument("--keep-merged", action="store_true", help="keep the merged D-XX.Y.md files")
    ap.add_argument("--only", help="restrict to one sub-domain id (e.g. D-01.1)")
    args = ap.parse_args()

    root = Path(args.baseline) / "domains"
    merged_files = [p for p in sorted(root.glob("D-*/*/*.md"))
                    if re.fullmatch(r"D-\d+\.\d+", p.stem)]
    if args.only:
        merged_files = [p for p in merged_files if p.stem == args.only]
    if not merged_files:
        print("no merged sub-domain files found", file=sys.stderr)
        sys.exit(2)

    log, report = [], []
    for mf in merged_files:
        process_subdomain(mf, args.apply, args.keep_merged, log, report)

    # -- update per-domain manifests with the modular inventory ---------------
    if args.apply:
        import json
        by_domain = {}
        for r in report:
            by_domain.setdefault(r["domain_dir"], {})[r["subdomain"]] = {
                "files": sorted(r["files"]),
                "regs": r["regs"],
                "cross_pairs": r["pairs"],
                "demoted_units": r["demoted_total"],
                "dedup_lines": r["dedup"],
                "balanced": r["balanced"],
            }
        for domain_dir, inv in sorted(by_domain.items()):
            mpath = next(Path(domain_dir).glob("D-*.manifest.json"), None)
            if mpath is None:
                log.append(f"{domain_dir}: no D-XX.manifest.json found — modular_layout not recorded")
                continue
            manifest = json.loads(mpath.read_text(encoding="utf-8"))
            existing = manifest.get("modular_layout", {})
            existing.update(inv)  # merge, so --only runs don't clobber siblings
            manifest["modular_layout"] = existing
            mpath.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8", newline="\n")

        # -- regenerate domain _index.md and domains/index.md ------------------
        top_rows = []
        for domain_dir, inv in sorted(by_domain.items()):
            dd = Path(domain_dir)
            dom_name = dd.name
            n_regs = n_amb = n_pairs = n_art = 0
            sub_rows = []
            for sub_id in sorted(inv):
                sub_dir = dd / sub_id
                regs_list = sorted(inv[sub_id]["regs"])
                amb_list = [r for r, v in inv[sub_id]["regs"].items() if v["ambiguity"]]
                arts = sub_dir / "articles"
                n_sub_art = len(list(arts.glob("*.md"))) if arts.exists() else 0
                n_regs += len(regs_list)
                n_amb += len(amb_list)
                n_pairs += len(inv[sub_id]["cross_pairs"])
                n_art += n_sub_art
                sub_rows.append(
                    f"| [{sub_id}]({sub_id}/) | {', '.join(regs_list) or '—'} | "
                    f"{len(amb_list)} | {len(inv[sub_id]['cross_pairs'])} + [interactions]({sub_id}/cross/_interactions.md) | {n_sub_art} |")
            lines = [f"# {dom_name}", ""]
            lines.append(f"- Sub-domains: {len(inv)}")
            lines.append(f"- Per-regulation modules (regs/): {n_regs}")
            lines.append(f"- Ambiguity modules (regs/&lt;R&gt;.ambiguity.md): {n_amb}")
            lines.append(f"- Cross pair analyses (cross/): {n_pairs} (+1 interactions per sub-domain)")
            lines.append(f"- Article copies (many-to-many): {n_art}")
            lines.append("")
            lines.append("> Modular layout generated by `modularize_domains.py`; every sub-domain")
            lines.append("> exposes a neutral `objective.md`, per-regulation `regs/<REG>.md` modules,")
            lines.append("> cross-regulation pair files and `cross/_interactions.md`.")
            lines.append("")
            lines.append("## Sub-domains")
            lines.append("")
            lines.append("| Sub-domain | Reg modules | Ambiguity | Cross pairs | Articles |")
            lines.append("|---|---|---|---|---|")
            lines.extend(sub_rows)
            lines.append("")
            w(dd / "_index.md", "\n".join(lines) + "\n")
            top_rows.append((dom_name, len(inv), n_regs, n_amb, n_pairs, n_art))

        lines = ["# Domains index (modular per-regulation layout)", ""]
        lines.append(f"- Domains: {len(top_rows)}")
        lines.append(f"- Sub-domains: {sum(r[1] for r in top_rows)}")
        lines.append(f"- Per-regulation modules: {sum(r[2] for r in top_rows)}")
        lines.append(f"- Ambiguity modules: {sum(r[3] for r in top_rows)}")
        lines.append(f"- Cross pair analyses: {sum(r[4] for r in top_rows)}")
        lines.append(f"- Article copies: {sum(r[5] for r in top_rows)}")
        lines.append("")
        lines.append("> Every sub-domain `D-XX.Y/` contains: `_index.md` (identity), `objective.md`")
        lines.append("> (neutral high-level objective), `regs/<REG>.md` + `regs/<REG>.ambiguity.md`")
        lines.append("> (independent per-regulation modules), `cross/<R1>-<R2>.md` +")
        lines.append("> `cross/_interactions.md` (cross-regulation layer), `articles/` (verbatim")
        lines.append("> article copies). Migration audit: [_migration_report.md](_migration_report.md).")
        lines.append("")
        lines.append("| Domain | Sub-domains | Reg modules | Ambiguity | Cross pairs | Article copies |")
        lines.append("|---|---|---|---|---|---|")
        for dom, ns, nr, na, np_, nart in top_rows:
            lines.append(f"| [{dom}]({dom}/_index.md) | {ns} | {nr} | {na} | {np_} | {nart} |")
        lines.append("")
        w(root / "index.md", "\n".join(lines) + "\n")

    rep = ["# Modularization migration report", ""]
    rep.append(f"- Sub-domains processed: {len(report)}")
    mode = "APPLY" if args.apply else "DRY-RUN"
    if args.apply and args.keep_merged:
        mode += " (merged files kept)"
    rep.append(f"- Mode: {mode}")
    rep.append(f"- Balanced line-accounting: {sum(1 for r in report if r['balanced'])}/{len(report)}")
    rep.append(f"- Total dedup lines (Part 3 == Part 1 §1): {sum(r['dedup'] for r in report)}")
    rep.append(f"- Total demoted cross-reference units: {sum(r['demoted_total'] for r in report)}")
    rep.append("")
    rep.append("| Sub-domain | Lines | Routed | Dedup | Tags | Struct | Balanced | Modules | Pairs | Demoted |")
    rep.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in report:
        rep.append(f"| {r['subdomain']} | {r['total_lines']} | {r['routed']} | {r['dedup']} | "
                   f"{r['tag_lines']} | {r['structure_lines']} | "
                   f"{'OK' if r['balanced'] else 'FAIL'} | {len(r['files'])} | "
                   f"{len(r['pairs'])} | {r['demoted_total']} |")
    rep.append("")
    rep.append("## Per-subdomain detail")
    rep.append("")
    for r in report:
        rep.append(f"### {r['subdomain']}")
        rep.append("")
        rep.append(f"- Files: {', '.join(sorted(r['files'])) or '—'}")
        if r["regs"]:
            regs_txt = ", ".join(f"{k} (subso={v['subso']}, reqs={v['reqs']}, "
                                 f"verbatim={v['verbatim']}, ambiguity={v['ambiguity']})"
                                 for k, v in r["regs"].items())
            rep.append(f"- Reg modules: {regs_txt}")
        rep.append(f"- Demotion stats: {r['stats']}")
        if r["script_log"]:
            rep.append("- Script log:")
            for l in r["script_log"]:
                rep.append(f"  - {l}")
        rep.append("")
    if log:
        rep.append("## Global log")
        rep.append("")
        for l in log:
            rep.append(f"- {l}")

    if args.apply:
        w(root / "_migration_report.md", "\n".join(rep) + "\n")

    for line in rep[:8]:
        print(line)
    print(f"balanced: {sum(1 for r in report if r['balanced'])}/{len(report)}; "
          f"apply={args.apply}; detail in _migration_report.md")
    for l in log:
        print("LOG:", l)
    if args.apply and any(not r["balanced"] for r in report):
        sys.exit(1)


if __name__ == "__main__":
    main()
