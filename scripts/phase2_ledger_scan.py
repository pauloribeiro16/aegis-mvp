#!/usr/bin/env python3
"""Throwaway scan backing docs/pipeline/05_PHASE2_DETERMINISM_LEDGER.md.

Answers one question per Phase 2 column: is it derivable from the Phase 1
deliverable plus the corpus, or does it carry information Phase 1 did not?

Every number the ledger prints comes from here. Re-run after any case edit and
diff the output; if the ledger and the scan disagree, the scan is right.

    python3 scripts/phase2_ledger_scan.py
"""
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES = [
    "Case_01_TinyTask_SaaS",
    "Case_02_SecureBorder_Solutions",
    "Case_03_OmniBank",
]

# Column indices of the Doc01 objective table, 0-based, after strip("|").split("|").
COL_ID, COL_STMT, COL_PARENT, COL_REG, COL_SCOPE, COL_CRITERIA, \
    COL_METHOD, COL_OWNER, COL_ANCHORS = 0, 1, 2, 3, 4, 5, 6, 7, 8

# Phase 1 Doc02 goal table, same 0-based convention.
P1_STMT, P1_REG, P1_ANCHORS = 1, 6, 8


def table_rows(path, id_prefix):
    """Rows of the Doc01 objective table whose first cell starts with id_prefix.

    The first cell is matched on `strip('| ')` rather than a literal prefix: four
    Case_03 rows are written with doubled padding after the pipe, and a strict
    `startswith('| `SO-')` silently drops them — which reads as a missing row
    rather than as the formatting defect it is.
    """
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        if not s.lstrip("| ").startswith(f"`{id_prefix}"):
            continue
        cells = [c.strip().strip("*").strip("`") for c in s.strip("|").split("|")]
        out.append(cells)
    return out


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:8]


def slot_of(oid):
    m = re.match(r"[A-Z]{2}-D-(\d{2}\.\d)-(\d{3})", oid.strip("`"))
    return (m.group(1), m.group(2)) if m else (None, None)


def report_case(case):
    p1 = REPO / "cases" / case / "01_PHASE1_CONTEXT" / "Doc02_Adjusted_Goals.md"
    p2 = REPO / "cases" / case / "02_PHASE2_RULES" / "Doc01_Operational_Objectives.md"
    d2 = REPO / "cases" / case / "02_PHASE2_RULES" / "Doc02_Secure_Design_Principles.md"
    if not (p1.exists() and p2.exists()):
        print(f"## {case}: SKIP (missing deliverable)")
        return

    goals = table_rows(p1, "AG-")
    objs = table_rows(p2, "PO-") + table_rows(p2, "SO-")

    print(f"\n## {case}")
    print(f"phase1 goals={len(goals)}  phase2 objectives={len(objs)}")

    # --- the load-bearing claim: is the statement a copy of the Phase 1 goal?
    g_stmts = sorted(r[P1_STMT] for r in goals)
    o_stmts = sorted(r[COL_STMT] for r in objs)
    print(f"statement multiset  phase1={md5(chr(10).join(g_stmts))} "
          f"phase2={md5(chr(10).join(o_stmts))} "
          f"-> {'IDENTICAL' if g_stmts == o_stmts else 'DIFFERS'}")

    if g_stmts != o_stmts:
        only_p1 = Counter(g_stmts) - Counter(o_stmts)
        print(f"  dropped in phase2 ({sum(only_p1.values())}):")
        g_by_stmt = {r[P1_STMT]: r[0].strip("`") for r in goals}
        for stmt, n in only_p1.items():
            print(f"    {g_by_stmt.get(stmt, '?')} x{n}  {stmt[:70]}...")

    # --- anchors: inherited from Phase 1 or recomputed?
    g_anchor = {"/".join(slot_of(r[0].strip("`"))): r[P1_ANCHORS].strip() for r in goals}
    anchor_diff = [
        (r[COL_ID], g_anchor.get("/".join(slot_of(r[COL_PARENT]))), r[COL_ANCHORS].strip())
        for r in objs
        if g_anchor.get("/".join(slot_of(r[COL_PARENT]))) != r[COL_ANCHORS].strip()
    ]
    print(f"anchors identical to phase1: {len(objs) - len(anchor_diff)}/{len(objs)}")
    if anchor_diff:
        # A `(primary)` suffix marks the leading anchor without changing the set,
        # so compare on the stripped set to tell annotation from a real change.
        strip = lambda s: {a.split(" ")[0] for a in (s or "").split(",") if a and a != "—"}
        real = [d for d in anchor_diff if strip(d[1]) != strip(d[2])]
        print(f"  {len(anchor_diff)} rows differ; {len(real)} differ in the anchor SET "
              f"(the rest only add a `(primary)` marker)")
        for oid, was, now in real[:8]:
            print(f"    {oid}: phase1={was!r} -> phase2={now!r}")

    # --- slot numbering rule: global canonical position, or rank among applicable?
    slot_regs = defaultdict(dict)
    for r in objs:
        sd, slot = slot_of(r[0].strip("`"))
        slot_regs[sd][slot] = r[COL_REG].strip()
    per_case_order = []
    for r in objs:
        reg = r[COL_REG].strip()
        if reg not in per_case_order:
            per_case_order.append(reg)
    global_rank = {reg: i + 1 for i, reg in enumerate(per_case_order)}
    rule_global = rule_rank = 0
    for sd, slots in slot_regs.items():
        applicable = sorted(slots.values(), key=lambda x: global_rank[x])
        if [slots[s] for s in sorted(slots)] == applicable:
            rule_rank += 1
        if all(int(s) == global_rank[reg] for s, reg in slots.items()):
            rule_global += 1
    print(f"slot rule  global-canonical: {rule_global}/{len(slot_regs)} sub-domains  "
          f"rank-among-applicable: {rule_rank}/{len(slot_regs)}")
    print(f"  regulation order in this case: {per_case_order}")

    # --- cardinality of each remaining column
    for col, name in [(COL_REG, "Regulation"), (COL_SCOPE, "Scope"),
                      (COL_CRITERIA, "Criteria"), (COL_METHOD, "Method"),
                      (COL_OWNER, "Owner"), (COL_ANCHORS, "Anchors")]:
        vals = Counter(r[col].strip() for r in objs)
        print(f"  {name:<11} {len(vals):>3} distinct / {len(objs)} rows   "
              f"top={vals.most_common(1)[0][0][:44]!r}")

    # --- PO/SO prefix vs regulation
    pref = defaultdict(Counter)
    for r in objs:
        pref[r[0].strip("`")[:2]][r[COL_REG].strip()] += 1
    print("  prefix->regulation: " +
          "; ".join(f"{k}={dict(v)}" for k, v in pref.items()))

    # --- Operational Translation: one template, or per-sub-domain?
    trans = re.findall(r"\*\*Operational Translation.*", p2.read_text(encoding="utf-8"))
    norm = {re.sub(r"enforce [a-z0-9 &/-]+ (?:across|through)", "enforce <SLUG>", t)
            for t in trans}
    print(f"  OperationalTranslation: {len(trans)} blocks, {len(norm)} distinct after slug-normalisation")

    # --- cells that swallowed raw baseline content (YAML / section breaks)
    polluted = [r[COL_ID] for r in objs
                if "```yaml" in r[COL_STMT] or " --- ## " in r[COL_STMT]
                or "req_id:" in r[COL_STMT]]
    if polluted:
        print(f"  POLLUTED statements (raw baseline leaked into the cell): {polluted}")

    # --- the RULE-* tail SPEC assigns to Phase 2
    raw2 = p2.read_text(encoding="utf-8")
    print(f"  RULE-* occurrences in Doc01: {raw2.count('RULE-')}   "
          f"in Doc02: {d2.read_text(encoding='utf-8').count('RULE-')}")

    # --- Doc02 principle tables. Two tables share the PRIN-ENG prefix but NOT
    # the column meaning: the §2-§5 category tables are 6 cells (id, name,
    # source, definition, constraint, verify) and the §6 skill-mapping table is
    # 5 (id, name, skill, path, scope). Keying them together by id and comparing
    # by column index silently compares a definition against a file path.
    prin, skills = {}, {}
    for line in d2.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `PRIN-ENG-"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        (skills if len(c) == 5 else prin)[c[0].strip("`")] = c
    print(f"  Doc02 principles: {len(prin)} (+{len(skills)} skill-mapping rows)")
    return prin, skills


def report_doc02(all_prin, all_skills):
    """Doc02 across cases: which columns are identical, which vary.

    Each table is compared against itself — the §2-§5 category tables and the
    §6 skill-mapping tables have different shapes and different column meanings.
    """
    cases = [c for c, p in all_prin.items() if p]
    if len(cases) < 2:
        return
    print("\n## Doc02 across cases")

    print("  §2-§5 principle tables (6 cells):")
    keys = sorted({k for c in cases for k in all_prin[c]})
    shared = [k for k in keys if all(k in all_prin[c] for c in cases)]
    names = {2: "AcademicSource", 3: "Definition", 4: "Constraint", 5: "VerifyLead"}
    for ci in range(2, 6):
        same = all(all_prin[c][k][ci] == all_prin[cases[0]][k][ci] for c in cases for k in shared)
        print(f"    col{ci} {names[ci]:<16} {'IDENTICAL' if same else 'VARIES'} "
              f"({len(shared)} principles, {len(cases)} cases)")

    print("  §6 skill-mapping tables (5 cells):")
    skeys = sorted({k for c in cases for k in all_skills[c]})
    sshared = [k for k in skeys if all(k in all_skills[c] for c in cases)]
    snames = {2: "Skill", 3: "Path", 4: "EvalScope"}
    for ci in range(2, 5):
        same = all(all_skills[c][k][ci] == all_skills[cases[0]][k][ci]
                   for c in cases for k in sshared)
        print(f"    col{ci} {snames[ci]:<16} {'IDENTICAL' if same else 'VARIES'} "
              f"({len(sshared)} principles, {len(cases)} cases)")


if __name__ == "__main__":
    prin, skills = {}, {}
    for case in CASES:
        prin[case], skills[case] = report_case(case)
    report_doc02(prin, skills)