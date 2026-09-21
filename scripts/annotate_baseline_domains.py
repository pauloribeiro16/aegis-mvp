#!/usr/bin/env python3
"""
annotate_baseline_domains.py
============================
Systematically audits and annotates all 38 baseline sub-domain markdown files
in baseline/domains/ with universal semantic comment boundaries:
- <!-- aegis:pair:REG1,REG2 --> ... <!-- /aegis:pair -->
- <!-- aegis:subso:REG --> ... <!-- /aegis:subso -->
- <!-- aegis:req:REG1,REG2 --> ... <!-- /aegis:req -->
- <!-- aegis:ambiguity:REG --> ... <!-- /aegis:ambiguity -->

This ensures 100% deterministic, simple, zero-summary filtering by any downstream script.
"""

import os
import re
import glob

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

def annotate_content(content):
    lines = content.splitlines()
    n = len(lines)
    new_lines = []
    i = 0
    
    in_part = 0 # 1, 2, 3, 4
    
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Track Parts
        if re.match(r'^#\s+Part\s+1\b', stripped, re.IGNORECASE):
            in_part = 1
        elif re.match(r'^#\s+Part\s+2\b', stripped, re.IGNORECASE):
            in_part = 2
        elif re.match(r'^#\s+Part\s+3\b', stripped, re.IGNORECASE):
            in_part = 3
        elif re.match(r'^#\s+Part\s+4\b', stripped, re.IGNORECASE):
            in_part = 4

        # -------------------------------------------------------------
        # 1. Annotate Part 1 & Part 2 Sub-SOs: #### D-XX.Y.N — Sub-SO for REG
        # -------------------------------------------------------------
        subso_match = re.match(r'^####\s+D-[0-9]+\.[0-9]+\.[0-9]+\s+[—\-]\s+Sub-SO for\s+([A-Za-z0-9_\s]+)', stripped)
        if subso_match:
            raw_reg = subso_match.group(1).strip()
            reg_norm = normalize_reg(raw_reg)
            
            # Find end of this Sub-SO block (next heading of equal or higher level, or Part, or EOF)
            j = i + 1
            while j < n:
                if re.match(r'^(#|##|###|####)\s+', lines[j].strip()) and not lines[j].strip().startswith('#### Considerations') and not lines[j].strip().startswith('#### Objective'):
                    break
                j += 1
            
            new_lines.append(f"<!-- aegis:subso:{reg_norm} -->")
            for k in range(i, j):
                new_lines.append(lines[k])
            new_lines.append("<!-- /aegis:subso -->")
            i = j
            continue

        # -------------------------------------------------------------
        # 2. Annotate Part 1 Requisitos Volere: #### 01.1.001 — ...
        # -------------------------------------------------------------
        volere_match = re.match(r'^####\s+[0-9]+\.[0-9]+\.[0-9]+\s+[—\-]\s+(.*)', stripped)
        if in_part == 1 and volere_match:
            j = i + 1
            while j < n and not re.match(r'^(#|##|###|####)\s+', lines[j].strip()):
                j += 1
            block_content = "\n".join(lines[i:j])
            regs_match = re.search(r'regs:\s*\[([^\]]+)\]', block_content)
            if regs_match:
                raw_regs = [normalize_reg(r) for r in regs_match.group(1).split(',')]
                regs_tag = ",".join(sorted(list(set(raw_regs))))
                new_lines.append(f"<!-- aegis:req:{regs_tag} -->")
                for k in range(i, j):
                    new_lines.append(lines[k])
                new_lines.append("<!-- /aegis:req -->")
                i = j
                continue

        # -------------------------------------------------------------
        # 3. Annotate Pair Headings in Part 1, 2, or 3: ##### Pair: REG1 ↔ REG2
        # -------------------------------------------------------------
        if stripped.startswith('##### Pair:'):
            pair_match = re.search(r'#####\s+Pair:\s*([A-Za-z0-9_\s]+)\s*[↔<->xX-]+\s*([A-Za-z0-9_\s]+)', stripped)
            if pair_match:
                r1 = normalize_reg(pair_match.group(1))
                r2 = normalize_reg(pair_match.group(2))
                pair_tag = f"{r1},{r2}"
                
                j = i + 1
                while j < n:
                    if re.match(r'^(#|##|###|####|#####)\s+', lines[j].strip()) and not lines[j].strip().startswith('######'):
                        break
                    j += 1
                
                new_lines.append(f"<!-- aegis:pair:{pair_tag} -->")
                for k in range(i, j):
                    new_lines.append(lines[k])
                new_lines.append("<!-- /aegis:pair -->")
                i = j
                continue

        # -------------------------------------------------------------
        # 4. Standardize existing HTML pair comments: <!-- pair: REG1,REG2 -->
        # -------------------------------------------------------------
        if '<!-- pair:' in stripped and not stripped.startswith('<!-- aegis:'):
            p_match = re.search(r'<!--\s*pair:\s*([A-Za-z0-9_\s]+)\s*,\s*([A-Za-z0-9_\s]+)\s*-->', stripped)
            if p_match:
                r1 = normalize_reg(p_match.group(1))
                r2 = normalize_reg(p_match.group(2))
                new_lines.append(f"<!-- aegis:pair:{r1},{r2} -->")
                i += 1
                while i < n and '<!-- /pair -->' not in lines[i]:
                    new_lines.append(lines[i])
                    i += 1
                if i < n and '<!-- /pair -->' in lines[i]:
                    new_lines.append("<!-- /aegis:pair -->")
                    i += 1
                continue

        # -------------------------------------------------------------
        # 5. Annotate Part 4 Ambiguity Chapters: ## REG or ## REG v0.2 ...
        # -------------------------------------------------------------
        if in_part == 4 and stripped.startswith('## '):
            # Detect which regulation this heading belongs to
            reg_found = None
            for reg_candidate in ALL_REGS:
                raw_head = stripped[3:].strip()
                norm_head = raw_head.replace(' ', '').replace('_', '').upper()
                cand_norm = reg_candidate.replace('_', '').upper()
                if norm_head.startswith(cand_norm) or cand_norm in norm_head:
                    reg_found = reg_candidate
                    break
            
            if reg_found:
                # Find the end of this regulation's ambiguity section
                j = i + 1
                while j < n:
                    next_strip = lines[j].strip()
                    if next_strip.startswith('# ') or next_strip.startswith('## '):
                        # Check if next heading belongs to a DIFFERENT regulation
                        if next_strip.startswith('# '):
                            break
                        next_head = next_strip[3:].strip()
                        next_norm = next_head.replace(' ', '').replace('_', '').upper()
                        other_reg = None
                        for cand in ALL_REGS:
                            c_norm = cand.replace('_', '').upper()
                            if next_norm.startswith(c_norm) or c_norm in next_norm:
                                other_reg = cand
                                break
                        if other_reg and other_reg != reg_found:
                            break
                    j += 1
                
                new_lines.append(f"<!-- aegis:ambiguity:{reg_found} -->")
                for k in range(i, j):
                    new_lines.append(lines[k])
                new_lines.append("<!-- /aegis:ambiguity -->")
                i = j
                continue

        new_lines.append(line)
        i += 1

    return "\n".join(new_lines)

def process_all_baseline_files(domains_dir):
    pattern = os.path.join(domains_dir, 'D-*', 'D-*', 'D-*.md')
    files = sorted(glob.glob(pattern))
    print(f"Annotating {len(files)} baseline domain files...")
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        annotated = annotate_content(content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(annotated)
    print("Baseline files annotated successfully.")

if __name__ == "__main__":
    domains_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "baseline", "domains")
    process_all_baseline_files(domains_dir)
