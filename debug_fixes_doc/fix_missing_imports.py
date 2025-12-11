
import os
import re

def fix_file(filepath, missing_types):
    print(f"Fixing {filepath} (missing: {', '.join(missing_types)})")
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="utf-8-sig") as f:
                content = f.read()
        except Exception as e:
            print(f"Failed to read {filepath}: {e}")
            return

    new_content = content
    
    # Check for existing typing import of specific types
    # "from typing import List, Tuple" etc.
    # We look for "from typing import"
    
    typing_import_match = re.search(r'from\s+typing\s+import\s+(.*?)(?:\n|$)', content)
    
    if typing_import_match:
        # Append to existing import
        existing_imports = typing_import_match.group(1)
        # Check if wrapped in parens? Simple regex assumes single line or simple wrap, 
        # but robust parsing is hard. 
        # Let's try to just append to the end of the line if it doesn't end with backslash or parens
        
        # A safer bet for this script is to add a NEW line if we are not confident, 
        # OR just replace the line.
        
        # Let's construct a merged list.
        # This is tricky without full parsing.
        
        # Strategy: Add a new import line after the existing one or at top.
        # Python allows multiple "from typing import ..."
        
        # To be safe and avoid breaking syntax, let's just add a new line at the top 
        # (or after future imports).
        # But cleanest is to merge.
        pass

    # Simple Strategy:
    # Always add "from typing import X, Y, Z" at the top of the file.
    # If duplicates exist, it's fine in Python (just redundant).
    # We put it after imports or docstrings?
    # Safest: After the first non-comment line? Or just top.
    # Top of file logic:
    # 1. Skip #! lines
    # 2. Skip encoding lines
    # 3. Insert.
    
    lines = content.splitlines(keepends=True)
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("#!") or line.startswith("# -*-") or "coding:" in line:
            insert_idx = i + 1
        else:
            break
            
    import_line = f"from typing import {', '.join(missing_types)}\n"
    lines.insert(insert_idx, import_line)
    
    new_content = "".join(lines)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    report_file = "missing_imports_report.txt"
    if not os.path.exists(report_file):
        print(f"{report_file} not found.")
        return

    with open(report_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("Found"):
            continue
            
        parts = line.split(": ")
        if len(parts) != 2:
            continue
            
        filepath = parts[0]
        types_str = parts[1]
        missing_types = [t.strip() for t in types_str.split(",")]
        
        fix_file(filepath, missing_types)

if __name__ == "__main__":
    main()
