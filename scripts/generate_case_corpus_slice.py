#!/usr/bin/env python3
"""
generate_case_corpus_slice.py
=============================
Generates a strictly filtered, verbatim slice of the AEGIS baseline corpus for a specific company case.

Principles:
1. Deterministic filter: ONLY in-scope regulations and triggered sub-domains are included.
2. NO SUMMARIES: All retained content (HSO, active Sub-SOs, applicable articles, pair text) is verbatim.
3. Surgical drop:
   - Drops out-of-scope article files from articles/.
   - Drops inactive sub-domain directories (e.g. D-08.3 when NIS2/DORA are not active).
   - Drops table rows referencing inactive regulations in Participants and Axis tables.
   - Drops inactive Pair sections in Part 1 (##### Pair: ...) and Part 2 (<!-- pair: ... --> ... <!-- /pair -->).
   - Drops inactive Sub-SO blocks (#### D-XX.Y.N — Sub-SO for ...).
   - Drops inactive Volere requirements.
   - Drops inactive Ambiguity chapters in Part 4 (## NIS2, ## DORA, ## AI_Act).
4. Generates an index.md for the filtered case slice.

Usage:
  python scripts/generate_case_corpus_slice.py --case Case_01_TinyTask_SaaS --regs GDPR CRA
"""

import os
import sys
import shutil
import argparse
import re

REG_SYNONYMS = {
    'GDPR': ['GDPR', 'General Data Protection Regulation'],
    'CRA': ['CRA', 'Cyber Resilience Act'],
    'NIS2': ['NIS2', 'NIS 2', 'Network and Information Systems'],
    'DORA': ['DORA', 'Digital Operational Resilience Act'],
    'AI_Act': ['AI_Act', 'AI Act', 'Artificial Intelligence Act', 'AIA']
}

ALL_REGS = ['GDPR', 'CRA', 'NIS2', 'DORA', 'AI_Act']

def normalize_reg(token):
    token = token.strip()
    norm = token.replace(' ', '').replace('_', '').replace('-', '').upper()
    if 'GDPR' in norm: return 'GDPR'
    if 'CRA' in norm: return 'CRA'
    if 'NIS' in norm: return 'NIS2'
    if 'DORA' in norm: return 'DORA'
    if 'AI' in norm or 'AIA' in norm: return 'AI_Act'
    return token

def is_reg_in_scope(reg_token, active_regs):
    norm = reg_token.replace(' ', '').replace('_', '').replace('-', '').upper()
    for active in active_regs:
        active_norm = active.replace(' ', '').replace('_', '').replace('-', '').upper()
        if active_norm == norm or active_norm in norm or norm in active_norm:
            return True
    return False

def filter_articles(src_articles_dir, dst_articles_dir, active_regs):
    if not os.path.exists(src_articles_dir):
        return []
    os.makedirs(dst_articles_dir, exist_ok=True)
    retained_articles = []
    for f in os.listdir(src_articles_dir):
        if not f.endswith('.md'):
            continue
        reg_prefix = f.split('_')[0]
        if any(is_reg_in_scope(reg_prefix, active_regs) for active in active_regs):
            src_file = os.path.join(src_articles_dir, f)
            dst_file = os.path.join(dst_articles_dir, f)
            shutil.copy2(src_file, dst_file)
            retained_articles.append(f)
    return retained_articles

def filter_matrix_table(lines, start_idx, active_regs):
    """
    Filters a 2D cross-regulation matrix table like:
    | | GDPR | NIS 2 | CRA | DORA |
    |---|---|---|---|---|
    | **GDPR** | ... |
    Keeps only columns and rows belonging to active_regs (and the index column).
    """
    header_line = lines[start_idx]
    header_cells = [c.strip() for c in header_line.split('|')]
    # Typically header_cells looks like ['', '', 'GDPR', 'NIS 2', 'CRA', 'DORA', '']
    # Let's identify the index of columns to keep: column 0/1 (the leading empty / row label column)
    # plus any column whose name matches active_regs
    cols_to_keep = []
    for idx, c in enumerate(header_cells):
        if idx == 0 or idx == len(header_cells) - 1:
            continue
        # If it's the first data column (which is blank for top-left cell)
        if c == '':
            cols_to_keep.append(idx)
        else:
            # Check if this cell represents a regulation
            is_reg = False
            for r in ALL_REGS:
                if is_reg_in_scope(c, [r]):
                    is_reg = True
                    if is_reg_in_scope(c, active_regs):
                        cols_to_keep.append(idx)
                    break
            if not is_reg:
                cols_to_keep.append(idx)

    new_table_lines = []
    i = start_idx
    n = len(lines)
    while i < n and lines[i].strip().startswith('|'):
        curr_line = lines[i]
        curr_cells = [c.strip() for c in curr_line.split('|')]
        
        # Check if this is a row for an inactive regulation
        drop_row = False
        if len(curr_cells) > 1:
            first_label = curr_cells[1].replace('*', '').strip()
            for r in ALL_REGS:
                if is_reg_in_scope(first_label, [r]):
                    if not is_reg_in_scope(first_label, active_regs):
                        drop_row = True
                    break
        if drop_row:
            i += 1
            continue
        
        # Build filtered cells for this row
        filtered_cells = []
        for col_idx in cols_to_keep:
            if col_idx < len(curr_cells):
                filtered_cells.append(curr_cells[col_idx])
            else:
                filtered_cells.append('')
        
        new_line = "| " + " | ".join(filtered_cells) + " |"
        new_table_lines.append(new_line)
        i += 1

    return new_table_lines, i

def is_inactive_table_row(line, active_regs):
    # Matches table rows where cell 1 or cell 2 specifies a regulation or a pair
    cells = [c.strip() for c in line.split('|')]
    if len(cells) > 2:
        for idx in [1, 2]:
            if idx >= len(cells):
                continue
            cell_val = cells[idx].replace('*', '').strip()
            
            # Check for Pair in cell, e.g. "GDPR ↔ AI_Act" or "GDPR ↔ CRA"
            if '↔' in cell_val or '<->' in cell_val:
                pair_parts = re.split(r'[↔<->]+', cell_val)
                if len(pair_parts) == 2:
                    p1, p2 = pair_parts[0].strip(), pair_parts[1].strip()
                    # If this cell describes a pair of regulations, check if both are in scope
                    is_p1_reg = any(is_reg_in_scope(p1, [r]) for r in ALL_REGS)
                    is_p2_reg = any(is_reg_in_scope(p2, [r]) for r in ALL_REGS)
                    if is_p1_reg and is_p2_reg:
                        if not (is_reg_in_scope(p1, active_regs) and is_reg_in_scope(p2, active_regs)):
                            return True
                        continue

            # Check for standalone regulation in cell
            for reg in ALL_REGS:
                if is_reg_in_scope(cell_val, [reg]):
                    if not is_reg_in_scope(cell_val, active_regs):
                        return True
                    break
    return False

def filter_subdomain_markdown(content, active_regs, subdomain_id, retained_articles):
    lines = content.splitlines()
    out = []
    
    # Prepend slice header and index
    out.append(f"# {subdomain_id} — Case Filtered View")
    out.append("")
    out.append(f"> **Case Corpus Slice:** Retaining ONLY verbatim sections for active regulations: `{', '.join(active_regs)}`.")
    out.append("> All out-of-scope regulations, inactive Sub-SOs, inactive requirement blocks, and out-of-scope table rows have been stripped.")
    out.append("> No text has been summarized or altered.")
    out.append("")
    out.append("### In-Scope Articles in this Sub-Domain:")
    if retained_articles:
        for art in sorted(retained_articles):
            out.append(f"- [{art}](articles/{art})")
    else:
        out.append("- *(No specific single-article copies; covered via merged text)*")
    out.append("")
    out.append("---")
    out.append("")

    i = 0
    n = len(lines)
    
    while i < n:
        line = lines[i]

        # 0. Check if this is the start of a 2D cross-regulation matrix table (e.g. '| | GDPR | NIS 2 |')
        if line.strip().startswith('| |') or line.strip().startswith('|  |'):
            filtered_tbl, next_i = filter_matrix_table(lines, i, active_regs)
            out.extend(filtered_tbl)
            i = next_i
            continue

        # Filter Table Rows for Inactive Regulations
        if is_inactive_table_row(line, active_regs):
            i += 1
            continue

        # 1. Check Standardized AEGIS Block Boundaries
        # Format: <!-- aegis:pair:REG1,REG2 -->
        if '<!-- aegis:pair:' in line:
            m = re.search(r'<!--\s*aegis:pair:\s*([^>]+)-->', line)
            if m:
                regs = [r.strip() for r in m.group(1).split(',')]
                in_scope = all(is_reg_in_scope(r, active_regs) for r in regs)
                if not in_scope:
                    i += 1
                    while i < n and '<!-- /aegis:pair -->' not in lines[i]:
                        i += 1
                    if i < n and '<!-- /aegis:pair -->' in lines[i]:
                        i += 1
                    continue

        # Format: <!-- aegis:subso:REG -->
        if '<!-- aegis:subso:' in line:
            m = re.search(r'<!--\s*aegis:subso:\s*([^>]+)-->', line)
            if m:
                reg = m.group(1).strip()
                if not is_reg_in_scope(reg, active_regs):
                    i += 1
                    while i < n and '<!-- /aegis:subso -->' not in lines[i]:
                        i += 1
                    if i < n and '<!-- /aegis:subso -->' in lines[i]:
                        i += 1
                    continue

        # Format: <!-- aegis:req:REG1,REG2 -->
        if '<!-- aegis:req:' in line:
            m = re.search(r'<!--\s*aegis:req:\s*([^>]+)-->', line)
            if m:
                regs = [r.strip() for r in m.group(1).split(',')]
                in_scope = any(is_reg_in_scope(r, active_regs) for r in regs)
                if not in_scope:
                    i += 1
                    while i < n and '<!-- /aegis:req -->' not in lines[i]:
                        i += 1
                    if i < n and '<!-- /aegis:req -->' in lines[i]:
                        i += 1
                    continue

        # Format: <!-- aegis:ambiguity:REG -->
        if '<!-- aegis:ambiguity:' in line:
            m = re.search(r'<!--\s*aegis:ambiguity:\s*([^>]+)-->', line)
            if m:
                reg = m.group(1).strip()
                if not is_reg_in_scope(reg, active_regs):
                    i += 1
                    while i < n and '<!-- /aegis:ambiguity -->' not in lines[i]:
                        i += 1
                    if i < n and '<!-- /aegis:ambiguity -->' in lines[i]:
                        i += 1
                    continue

        # Fallback for any unannotated Pair / Sub-SO / Ambiguity patterns
        if line.strip().startswith('##### Pair:'):
            pair_match = re.search(r'#####\s+Pair:\s*([A-Za-z0-9_\s]+)\s*[↔<->xX-]+\s*([A-Za-z0-9_\s]+)', line)
            if pair_match:
                reg1, reg2 = pair_match.group(1).strip(), pair_match.group(2).strip()
                if not (is_reg_in_scope(reg1, active_regs) and is_reg_in_scope(reg2, active_regs)):
                    i += 1
                    while i < n and not re.match(r'^(#####|####|###|##|#)\s+', lines[i]):
                        i += 1
                    continue

        out.append(line)
        i += 1

    return "\n".join(out)

def process_case_slice(case_name, active_regs, baseline_dir, cases_dir, output_dir=None):
    # Normalize input regulations
    normalized_active_regs = [normalize_reg(r) for r in active_regs]
    # Remove duplicates while preserving order
    seen = set()
    clean_regs = []
    for r in normalized_active_regs:
        if r not in seen:
            seen.add(r)
            clean_regs.append(r)
    active_regs = clean_regs

    if output_dir:
        target_slice_dir = output_dir
    else:
        case_path = os.path.join(cases_dir, case_name)
        os.makedirs(case_path, exist_ok=True)
        target_slice_dir = os.path.join(case_path, "filtered_corpus")

    if os.path.exists(target_slice_dir):
        shutil.rmtree(target_slice_dir)
    os.makedirs(target_slice_dir, exist_ok=True)

    domains_src = os.path.join(baseline_dir, "domains")
    if not os.path.exists(domains_src):
        print(f"Error: Baseline domains directory {domains_src} does not exist.")
        sys.exit(1)

    index_entries = []
    total_articles = 0

    for domain_folder in sorted(os.listdir(domains_src)):
        domain_src_path = os.path.join(domains_src, domain_folder)
        if not os.path.isdir(domain_src_path) or not domain_folder.startswith("D-"):
            continue

        domain_dst_path = os.path.join(target_slice_dir, domain_folder)

        for subdomain in sorted(os.listdir(domain_src_path)):
            subdomain_src_path = os.path.join(domain_src_path, subdomain)
            if not os.path.isdir(subdomain_src_path) or not (subdomain.startswith("D-") and "." in subdomain):
                continue

            src_md = os.path.join(subdomain_src_path, f"{subdomain}.md")
            if not os.path.exists(src_md):
                continue

            with open(src_md, "r", encoding="utf-8") as f:
                content = f.read()

            src_articles = os.path.join(subdomain_src_path, "articles")

            # Check if any active regulation participates in this subdomain
            has_active_participation = False
            for reg in active_regs:
                if (f"<!-- aegis:subso:{reg} -->" in content or
                    f"Sub-SO for {reg}" in content or
                    f"SO-D-{subdomain[2:]}.{reg}" in content or
                    f"applies_to: [{reg}]" in content or
                    f"applies_to: [*{reg}*]" in content):
                    has_active_participation = True
                    break

            # Filter articles in memory first
            applicable_article_files = []
            if os.path.exists(src_articles):
                for f in os.listdir(src_articles):
                    if f.endswith('.md'):
                        pfx = f.split('_')[0]
                        if any(is_reg_in_scope(pfx, active_regs) for active in active_regs):
                            applicable_article_files.append(f)

            # Strict exclusion of inactive subdomains for this combination of regulations
            if not applicable_article_files and not has_active_participation:
                continue

            subdomain_dst_path = os.path.join(domain_dst_path, subdomain)
            dst_articles = os.path.join(subdomain_dst_path, "articles")

            # Copy verbatim in-scope articles
            retained_articles = filter_articles(src_articles, dst_articles, active_regs)
            total_articles += len(retained_articles)

            os.makedirs(subdomain_dst_path, exist_ok=True)
            filtered_md = filter_subdomain_markdown(content, active_regs, subdomain, retained_articles)
            dst_md = os.path.join(subdomain_dst_path, f"{subdomain}.md")
            with open(dst_md, "w", encoding="utf-8") as f:
                f.write(filtered_md)

            index_entries.append({
                "domain": domain_folder,
                "subdomain": subdomain,
                "path": f"{domain_folder}/{subdomain}/{subdomain}.md",
                "articles_count": len(retained_articles)
            })

    # Build index.md
    display_title = case_name if case_name else "Generic Regulatory Slice"
    index_md_path = os.path.join(target_slice_dir, "index.md")
    with open(index_md_path, "w", encoding="utf-8") as f:
        f.write(f"# Filtered Corpus Slice — {display_title}\n\n")
        f.write(f"**Applicable Regulations in Scope:** `{', '.join(active_regs)}`\n\n")
        f.write("> **Deterministic Slice (Zero Summaries):**\n")
        f.write("> This folder contains the verbatim baseline corpus filtered strictly for the regulations above.\n")
        f.write("> All non-applicable regulations, unselected sub-domains, inactive table rows, and inactive articles have been eliminated.\n\n")
        f.write("## In-Scope Sub-Domains\n\n")
        f.write("| Domain | Sub-Domain | Filtered Specification | In-Scope Articles |\n")
        f.write("|---|---|---|---|\n")
        for entry in index_entries:
            f.write(f"| `{entry['domain']}` | **{entry['subdomain']}** | [{entry['subdomain']}.md]({entry['path']}) | {entry['articles_count']} articles |\n")

    print(f"Slice generated successfully for {display_title}:")
    print(f"  - Active regulations: {', '.join(active_regs)}")
    print(f"  - Sub-domains in scope: {len(index_entries)}")
    print(f"  - Total verbatim articles retained: {total_articles}")
    print(f"  - Slice location: {target_slice_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate filtered case corpus slice for any arbitrary regulation subset")
    parser.add_argument("--case", default=None, help="Case folder name under cases/ (e.g. Case_01_TinyTask_SaaS, Case_02_Fintech)")
    parser.add_argument("--output-dir", default=None, help="Custom output directory path for the filtered slice")
    parser.add_argument("--regs", nargs="+", required=True, help="Applicable regulations (e.g. GDPR, or CRA, or GDPR CRA NIS2, or NIS2 DORA)")
    parser.add_argument("--baseline", default="baseline", help="Path to baseline directory")
    parser.add_argument("--cases-dir", default="cases", help="Path to cases directory")
    args = parser.parse_args()

    if not args.case and not args.output_dir:
        parser.error("Either --case <CaseName> or --output-dir <Path> must be provided.")

    process_case_slice(args.case, args.regs, args.baseline, args.cases_dir, args.output_dir)
