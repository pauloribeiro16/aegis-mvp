#!/usr/bin/env python3
"""
generate_case_corpus_slice.py
=============================
Generates the case corpus slice for a specific company case by COMPOSING
per-regulation modules from the modular baseline (see modularize_domains.py).

Principles:
1. Regulation-pure by construction: for the active regulations the script
   copies the already-independent modules verbatim — no deletion filtering of
   mixed prose is needed (the baseline modules are separated at source).
2. NO SUMMARIES: every retained byte is verbatim from the modular baseline.
3. Composition rule per sub-domain D-XX.Y:
   - _index.md            adapted (module table filtered to active layers)
   - objective.md         copied (neutral high-level objective)
   - regs/<R>.md          copied for each ACTIVE regulation R
   - regs/<R>.ambiguity.md copied for each ACTIVE regulation R
   - cross/<R1>-<R2>.md   copied when BOTH regulations are active
   - cross/_interactions.md copied only when >=2 regs active (scope-overlap
                          matrix tables filtered to active regs + scope banner)
   - articles/<R>_*.md    copied for active regulations only
   - Sub-domains with no active-reg module and no in-scope article are skipped.
4. Purity audit: per composed file, counts mentions of INACTIVE regulations
   outside the demarcated zones ('Cross-references (informational)' sections,
   YAML cards, tables). Target for regs/ modules: 0.
5. Writes cases/<case>/filtered_corpus/index.md with the composition table.

Usage:
  python scripts/generate_case_corpus_slice.py --case Case_01_TinyTask_SaaS --regs GDPR CRA
"""

import os
import re
import shutil
import argparse
from pathlib import Path

ALL_REGS = ['GDPR', 'CRA', 'NIS2', 'DORA', 'AI_Act']
RE_REG = re.compile(r'\b(GDPR|NIS2|CRA|DORA|AI_Act)\b')
RE_MATRIX = re.compile(r'^\|\s*\|')  # tables whose first cell is empty (matrices)


def normalize_reg(token):
    token = token.strip()
    norm = token.replace(' ', '').replace('_', '').replace('-', '').upper()
    if 'GDPR' in norm:
        return 'GDPR'
    if 'CRA' in norm:
        return 'CRA'
    if 'NIS' in norm:
        return 'NIS2'
    if 'DORA' in norm:
        return 'DORA'
    if 'AI' in norm or 'AIA' in norm:
        return 'AI_Act'
    return token


def norm_text(t):
    return t.replace('NIS 2', 'NIS2').replace('AI Act', 'AI_Act')


def mentions_inactive(text, active):
    return set(RE_REG.findall(norm_text(text))) - set(active)


def filter_matrix_tables(lines, active):
    """In matrix tables (first header cell empty), drop inactive rows and
    blank out inactive regulation columns. Other tables pass through."""
    out = []
    i, n = 0, len(lines)
    while i < n:
        if RE_MATRIX.match(lines[i]) and i + 1 < n and set(lines[i + 1]) <= set('|-: '):
            # matrix: header + separator + rows until non-table line
            j = i
            block = []
            while j < n and lines[j].strip().startswith('|'):
                block.append(lines[j])
                j += 1
            out.extend(_filter_matrix_block(block, active))
            i = j
        else:
            out.append(lines[i])
            i += 1
    return out


def _filter_matrix_block(block, active):
    header_cells = [c.strip() for c in block[0].strip().strip('|').split('|')]
    keep_cols = [0]
    for k, cell in enumerate(header_cells[1:], start=1):
        regs = set(RE_REG.findall(norm_text(cell)))
        if not regs or (regs & set(active)):
            keep_cols.append(k)
    out = []
    for ln in block:
        cells = ln.strip().strip('|').split('|')
        if len(cells) == len(header_cells) and set(RE_REG.findall(norm_text(cells[0]))) - set(active):
            continue  # row of an inactive regulation
        if len(cells) == len(header_cells):
            ln = '| ' + ' | '.join(cells[k] for k in keep_cols if k < len(cells)) + ' |'
        out.append(ln)
    return out


def purity_count(path, active):
    """Mentions of inactive regs outside demarcated zones. Returns
    (violations_prose, informational_total)."""
    text = path.read_text(encoding='utf-8')
    idx = text.find('## Cross-references (informational)')
    body = text[:idx] if idx >= 0 else text
    viol = info = 0
    fence = False
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith('```'):
            fence = not fence
            continue
        if ln.startswith('<!-- aegis:purity'):
            continue
        if not mentions_inactive(ln, active):
            continue
        info += 1
        if not fence and not s.startswith('|') and not s.startswith('#'):
            viol += 1
    return viol, info


def adapt_subdomain_index(src: Path, active) -> str:
    """Copy _index.md keeping only active layers in the Modules table."""
    lines = src.read_text(encoding='utf-8').splitlines()
    out = []
    in_modules = False
    for ln in lines:
        if ln.startswith('| Layer | File |'):
            in_modules = True
            out.append(ln)
            continue
        if in_modules and ln.startswith('|'):
            regs = set(RE_REG.findall(norm_text(ln)))
            if regs and not (regs & set(active)) and 'Pair' not in ln:
                continue  # inactive reg module row
            if 'Pair' in ln:
                pair_regs = set(RE_REG.findall(norm_text(ln.split('|')[1] + ' ' + ln.split('|')[2])))
                if not pair_regs <= set(active):
                    continue  # pair with an inactive regulation
            if 'Interactions' in ln and len(active) < 2:
                continue  # interactions only for multi-reg cases
            out.append(ln)
            continue
        if in_modules and not ln.startswith('|'):
            in_modules = False
        out.append(ln)
    return '\n'.join(out) + '\n'


def compose_case_slice(baseline_root: Path, out_root: Path, case: str, active_regs):
    domains_dir = baseline_root / 'domains'
    rows = []
    total_viol = 0
    for domain_dir in sorted(p for p in domains_dir.iterdir() if p.is_dir() and p.name.startswith('D-')):
        for sub_dir in sorted(p for p in domain_dir.iterdir()
                              if p.is_dir() and re.fullmatch(r'D-\d+\.\d+', p.name)):
            reg_modules = [r for r in active_regs if (sub_dir / 'regs' / f'{r}.md').exists()]
            art_dir = sub_dir / 'articles'
            in_scope_articles = []
            if art_dir.exists():
                in_scope_articles = [f for f in sorted(art_dir.glob('*.md'))
                                     if normalize_reg(f.name.split('_')[0]) in active_regs]
            if not reg_modules and not in_scope_articles:
                continue  # sub-domain not triggered by any active regulation

            dst = out_root / domain_dir.name / sub_dir.name
            dst.mkdir(parents=True, exist_ok=True)

            # neutral + per-regulation modules (verbatim)
            if (sub_dir / 'objective.md').exists():
                shutil.copy2(sub_dir / 'objective.md', dst / 'objective.md')
            if (sub_dir / '_index.md').exists():
                (dst / '_index.md').write_text(
                    adapt_subdomain_index(sub_dir / '_index.md', active_regs),
                    encoding='utf-8', newline='\n')
            pair_files = []
            for r in reg_modules:
                (dst / 'regs').mkdir(exist_ok=True)
                shutil.copy2(sub_dir / 'regs' / f'{r}.md', dst / 'regs' / f'{r}.md')
                amb = sub_dir / 'regs' / f'{r}.ambiguity.md'
                if amb.exists():
                    shutil.copy2(amb, dst / 'regs' / f'{r}.ambiguity.md')
                viol, _info = purity_count(dst / 'regs' / f'{r}.md', active_regs)
                total_viol += viol
            for pair in sorted((sub_dir / 'cross').glob('*.md')) if (sub_dir / 'cross').exists() else []:
                if pair.name == '_interactions.md':
                    continue
                regs = set(RE_REG.findall(norm_text(pair.stem.replace('-', ' '))))
                if regs and regs <= set(active_regs):
                    (dst / 'cross').mkdir(exist_ok=True)
                    shutil.copy2(pair, dst / 'cross' / pair.name)
                    pair_files.append(pair.stem)
            if len(active_regs) >= 2 and (sub_dir / 'cross' / '_interactions.md').exists():
                (dst / 'cross').mkdir(exist_ok=True)
                src = (sub_dir / 'cross' / '_interactions.md').read_text(encoding='utf-8')
                lines = src.splitlines()
                banner = [f'<!-- aegis:case-scope: {", ".join(active_regs)} — matrix tables filtered '
                          f'to active regulations; other tables retained verbatim -->']
                filtered = filter_matrix_tables(lines, active_regs)
                (dst / 'cross' / '_interactions.md').write_text(
                    '\n'.join(banner + filtered) + '\n', encoding='utf-8', newline='\n')
            if in_scope_articles:
                (dst / 'articles').mkdir(exist_ok=True)
                for f in in_scope_articles:
                    shutil.copy2(f, dst / 'articles' / f.name)

            rows.append({
                'domain': domain_dir.name,
                'sub': sub_dir.name,
                'regs': reg_modules,
                'pairs': pair_files,
                'articles': len(in_scope_articles),
                'interactions': len(active_regs) >= 2 and (sub_dir / 'cross' / '_interactions.md').exists(),
            })
    return rows, total_viol


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--case', required=True, help='Case name (cases/<case>/filtered_corpus)')
    ap.add_argument('--regs', nargs='+', required=True, help='Active regulations (GDPR CRA NIS2 DORA AI_Act)')
    ap.add_argument('--baseline', default='baseline', help='Baseline root (default: baseline)')
    ap.add_argument('--output-dir', default=None, help='Override output directory')
    args = ap.parse_args()

    active = []
    for r in args.regs:
        nr = normalize_reg(r)
        if nr not in ALL_REGS:
            print(f"unknown regulation '{r}'", os.sys.stderr)
            raise SystemExit(2)
        if nr not in active:
            active.append(nr)

    baseline_root = Path(args.baseline)
    out_root = Path(args.output_dir) if args.output_dir else Path('cases') / args.case / 'filtered_corpus'
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True)

    rows, total_viol = compose_case_slice(baseline_root, out_root, args.case, active)

    idx = [f'# Case corpus slice — {args.case}', '']
    idx.append(f'- Scope regulations: {", ".join(active)}')
    idx.append('- Composition mode: MODULAR (per-regulation modules selected verbatim from')
    idx.append('  baseline/domains; no deletion filtering — regulation purity holds by construction)')
    idx.append(f'- Sub-domains in slice: {len(rows)}')
    idx.append(f'- Purity audit — inactive-reg mentions outside demarcated zones: {total_viol} (target 0)')
    idx.append('')
    idx.append('| Domain | Sub-domain | Reg modules | Cross pairs | Interactions | Articles |')
    idx.append('|---|---|---|---|---|---|')
    for r in rows:
        idx.append(f"| {r['domain']} | {r['sub']} | {', '.join(r['regs']) or '—'} | "
                   f"{', '.join(r['pairs']) or '—'} | {'yes' if r['interactions'] else '—'} | {r['articles']} |")
    idx.append('')
    idx.append('> Per-regulation modules may carry a trailing `Cross-references (informational)`')
    idx.append('> section (mechanically demoted cross-regulation notes, marked as such) and')
    idx.append('> in-module tables citing other regulations (participation/clause-map rows);')
    idx.append('> these are informational and never impose obligations from inactive regulations.')
    idx.append('')
    (out_root / 'index.md').write_text('\n'.join(idx) + '\n', encoding='utf-8', newline='\n')

    print('\n'.join(idx[:8]))
    print(f'... {len(rows)} sub-domains; purity violations: {total_viol}')
    if total_viol:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
