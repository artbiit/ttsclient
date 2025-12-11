
import re

path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate my previous patch or the code structure
# "createElement("a");o.download="output.wav";o.href="
# Note: I patched it to be semi-colon separated.
# But original code used commas.
# My previous patch inserted: `;o.download="output.wav";o.href=`
# So the sequence is: `...createElement("a");o.download="output.wav";o.href=a,o.download=...`

# I will verify the variable name `o` from the context (it might change in other places but here it is `o` based on previous output).

# Identify the start of the conflict
start_marker = 'createElement("a");'
start_idx = content.find(start_marker)

while start_idx != -1:
    # Check if this block has my patch
    sub = content[start_idx:start_idx+200]
    
    # Check if "output.wav" is already there (my previous patch)
    if 'download="output.wav"' in sub:
        print(f"Found patched block at {start_idx}")
        
        # Now look for the SECOND download assignment in this block.
        # Format: ...o.href=a,o.download=i...
        # Regex to find: `,\w+\.download=[^,;]+`
        # Because it follows `o.href=a` (comma separated).
        
        # I'll just look for `.download=` that matches 'output.wav' (the first one) 
        # and then find the NEXT `.download=` which is not 'output.wav'.
        
        dl_indices = [m.start() for m in re.finditer(r'\.download=', sub)]
        
        if len(dl_indices) >= 2:
            print("Found multiple download assignments!")
            second_dl_offset = dl_indices[1] # The second one
            
            # Extract the assignment part
            # `.download=variable` or `.download=expression`
            # Ends at comma or semicolon or paren.
            
            assign_str_start = second_dl_offset
            # find end of assignment
            # scan relative to sub
            end_match = re.search(r'[,;)]', sub[assign_str_start:])
            if end_match:
                assign_length = end_match.start()
                full_assign = sub[assign_str_start : assign_str_start + assign_length]
                print(f"Second assignment: {full_assign}")
                
                # Replace with .download="output.wav"
                # Since .download is 9 chars, ="output.wav" is 12 chars. Total 21.
                # If full_assign is `.download=i` (11 chars), I can't simple overwrite without shifting.
                # Must do string slice replacement on full content.
                
                abs_start = start_idx + assign_str_start
                abs_end = start_idx + assign_str_start + assign_length
                
                replacement = '.download="output.wav"'
                
                print(f"Fixing at {abs_start}-{abs_end}: {full_assign} -> {replacement}")
                
                new_content = content[:abs_start] + replacement + content[abs_end:]
                content = new_content # update content in memory for loop (though we likely break)
                
                # We should stop or continue? 
                # With 'content' changed, indices shift.
                # Since we found the specific patched spot, we can break.
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Double assignment fixed.")
                break
        else:
            print("Only one download assignment found (or none extra).")
            
    start_idx = content.find(start_marker, start_idx+1)
