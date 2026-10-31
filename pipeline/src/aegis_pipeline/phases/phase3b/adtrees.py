"""aegis_pipeline.phases.phase3b.adtrees — Etapa 2.3: attack-defense trees and
the broken-path proof.

The tree is the model's; the cut logic is the CODE's. An OR gate with one
undefended child is an OPEN path, whatever the prose claims — and a threat
whose tree stays open may not carry a Low residual. That refusal is here,
not in the register: the register computes from the tree, never from hope.
"""
from __future__ import annotations

import re

from aegis_pipeline.phases.phase3b.threats import near_miss_ids

RE_DEF = re.compile(r"\[DEF:\s*`?([A-Za-z0-9._-]+)`?\s*\]")


def parse_adtree(answer: str, threat_id: str, accepted_ids: set[str]) -> dict:
    """L0 for one tree call: an indented node list with AND/OR gates and
    optional `[DEF: <requirement>]` markers on leaves."""
    from aegis_pipeline.phases.phase1.common import extract_fenced

    block = extract_fenced(answer, "markdown")
    root: dict | None = None
    stack: list[tuple[int, dict]] = []
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        text = line.strip().lstrip("- ").strip()
        gate = None
        m = re.match(r"^\((AND|OR)\)\s*(.+)$", text)
        if m:
            gate, text = m.group(1), m.group(2)
        defs = RE_DEF.findall(text)
        node = {"text": RE_DEF.sub("", text).strip(), "gate": gate, "defenses": defs,
                "children": []}
        if root is None:
            root = node
            stack = [(indent, node)]
            continue
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if not stack:
            raise ValueError(f"adtrees [{threat_id}]: node {text[:40]!r} has no parent")
        stack[-1][1]["children"].append(node)
        stack.append((indent, node))
    if root is None:
        raise ValueError(f"adtrees [{threat_id}]: no tree parsed")
    stray = [d for d in _all_defenses(root) if d not in accepted_ids]
    if stray:
        hint = "".join(near_miss_ids(d, accepted_ids) for d in stray[:4])
        raise ValueError(f"adtrees [{threat_id}]: defense(s) {stray[:4]} "
                         f"are not Part 1 ids{hint}")
    unbroken = _open_paths(root)
    return {"threat": threat_id, "root": root, "unbroken_attack_path": bool(unbroken),
            "open_paths": unbroken}


def _all_defenses(node: dict) -> list[str]:
    out = list(node.get("defenses", []))
    for child in node.get("children", []):
        out.extend(_all_defenses(child))
    return out


def _node_broken(node: dict) -> bool:
    """A node is cut when it carries a defense, or when its gate is satisfied
    by cut children: AND needs every child cut, OR needs at least one."""
    if node.get("defenses"):
        return True
    children = node.get("children", [])
    if not children:
        return False
    if node.get("gate") == "AND":
        return all(_node_broken(c) for c in children)
    # default gate is OR — any cut child cuts the parent
    return any(_node_broken(c) for c in children)


def _open_paths(node: dict, trail: list[str] | None = None) -> list[str]:
    """One readable line per leaf that no defense reaches."""
    trail = trail or []
    here = trail + [node["text"][:60]]
    if node.get("defenses"):
        return []
    children = node.get("children", [])
    if not children:
        return [" > ".join(here)]
    if node.get("gate") == "AND" and all(_node_broken(c) for c in children):
        return []
    if node.get("gate") != "AND" and any(_node_broken(c) for c in children):
        return []
    out = []
    for child in children:
        out.extend(_open_paths(child, here))
    return out


def enforce_residual_floor(threats: list[dict], trees: list[dict]) -> int:
    """A threat with an open attack path may not sit at Low residual.

    Mutates the threat dicts: residual is raised to Medium (score 5) by
    lifting impact — the path exists whatever the likelihood estimate said.
    Returns the number of threats corrected. This is the tree's teeth.
    """
    unbroken = {t["threat"] for t in trees if t.get("unbroken_attack_path")}
    corrected = 0
    for t in threats:
        if t["id"] in unbroken and t["residual_level"] == "Low":
            t["i_res"] = max(t["i_res"], 5)
            t["residual_score"] = t["l_res"] * t["i_res"]
            from aegis_pipeline.phases.phase3b.schemas import risk_level
            t["residual_level"] = risk_level(t["residual_score"])
            t["residual_floored_by_tree"] = True
            corrected += 1
    return corrected


def render_adtrees(trees: list[dict], company: str) -> str:
    lines = [
        "---",
        f"title: '04 — Attack–Defense Trees and Broken-Path Proofs ({company})'",
        "generated_by: 'p3b_trees (onda D) — the cut logic is code'",
        "---",
        "",
    ]
    for tree in trees:
        lines += [f"## Threat `{tree['threat']}`", ""]
        lines += _render_node(tree["root"], 0)
        if tree["unbroken_attack_path"]:
            lines += ["", "**BROKEN-PATH PROOF: OPEN PATH.** No defense reaches:",
                      ""]
            lines += [f"- {p}" for p in tree["open_paths"]]
            lines += ["", "The residual of this threat may not read Low — the "
                      "register enforces the floor.", ""]
        else:
            lines += ["", "**BROKEN-PATH PROOF: every path is cut** by the "
                      "Part 1 defenses named on the nodes.", ""]
    return "\n".join(lines) + "\n"


def _render_node(node: dict, depth: int) -> list[str]:
    pad = "  " * depth
    gate = f"({node['gate']}) " if node.get("gate") else ""
    defs = " ".join(f"[DEF: `{d}`]" for d in node.get("defenses", []))
    out = [f"{pad}- {gate}{node['text']} {defs}".rstrip()]
    for child in node.get("children", []):
        out.extend(_render_node(child, depth + 1))
    return out
