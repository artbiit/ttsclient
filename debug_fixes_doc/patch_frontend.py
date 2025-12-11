
import shutil
import re

path = r"d:\Workspace\ttsclient\web_front\index.js"
backup_path = r"d:\Workspace\ttsclient\web_front\index.js.bak"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Relaxed target for faster matching
target_str = '"audio/wav"'
idx = content.find(target_str)

while idx != -1:
    print(f"Checking match at {idx}")
    sub = content[max(0, idx-200):idx]
    
    # Match .download=variable (alphanumeric/underscore/dollar)
    assign_match = re.search(r'\.download=([a-zA-Z0-9_$]+)', sub)
    
    if assign_match:
        print(f"Found assignment: {assign_match.group(0)}")
        
        replacement = '.download="output.wav"' 
        
        abs_start = max(0, idx-200) + assign_match.start()
        abs_end = max(0, idx-200) + assign_match.end()
        
        print(f"Replacing at {abs_start}-{abs_end}: {content[abs_start:abs_end]} -> {replacement}")
        
        new_content = content[:abs_start] + replacement + content[abs_end:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Patched successfully.")
        break
    
    idx = content.find(target_str, idx + 1)
