
import os

path = r"d:\Workspace\ttsclient\web_front\index.js"

try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Search for .download = 
    # We look for patterns like:  u.download=  or  a.download=
    
    terms = ["audio/wav"]
    
    for term in terms:
        print(f"--- Searching for: {term} ---")
        start = 0
        while True:
            idx = content.find(term, start)
            if idx == -1:
                break
            
            # Print context
            context_start = max(0, idx - 100)
            context_end = min(len(content), idx + 200)
            print(f"Match at {idx}:")
            print(content[context_start:context_end])
            print("-" * 20)
            
            start = idx + 1
            if start >= len(content):
                break

except Exception as e:
    print(f"Error: {e}")
