
import shutil
import re

path = r"d:\Workspace\ttsclient\web_front\index.js"
# No backup here, trusting previous backup or git. Assumes index.js is valid.

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the blob creation for audio/wav
start_marker = 'type:"audio/wav"'
start_idx = content.find(start_marker)

if start_idx != -1:
    print(f"Found marker at {start_idx}")
    # Look for createElement("a")
    link_idx = content.find('createElement("a")', start_idx)
    if link_idx == -1:
        link_idx = content.find("createElement('a')", start_idx)
    
    if link_idx != -1 and link_idx - start_idx < 2000:
        print(f"Found createElement at {link_idx}")
        # Look around the link creation for .download
        sub = content[link_idx:link_idx+500]
        print(f"Sub-buffer: {repr(sub)}")
        
        # Strategy: find variable name from .href assignment immediately following
        # Pattern: createElement("a");x.href=
        
        insert_match = re.search(r'createElement\("a"\);(\w+)\.href=', sub)
        
        if insert_match:
             var_name = insert_match.group(1)
             print(f"Found variable: {var_name}")
             
             # We will insert o.download="output.wav"; after createElement("a");
             # Or replace the whole match.
             
             full_match = insert_match.group(0) # createElement("a");o.href=
             replacement = f'createElement("a");{var_name}.download="output.wav";{var_name}.href='
             
             abs_start = link_idx + insert_match.start()
             abs_end = link_idx + insert_match.end()
             
             print(f"Replacing at {abs_start}-{abs_end}: {full_match} -> {replacement}")
             
             new_content = content[:abs_start] + replacement + content[abs_end:]
             
             with open(path, 'w', encoding='utf-8') as f:
                 f.write(new_content)
             print("Patched successfully via INSERTION!")
        else:
            print("No href assignment found after createElement")
    else:
        print("Link creation not found nearby.")
else:
    print("Start marker not found.")
