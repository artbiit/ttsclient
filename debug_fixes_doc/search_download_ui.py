
path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "download" as a string literal which might be the button label or icon
terms = ['"download"', "'download'"]

for term in terms:
    print(f"--- Searching for: {term} ---")
    start = 0
    while True:
        idx = content.find(term, start)
        if idx == -1:
            break
        
        context_start = max(0, idx - 100)
        context_end = min(len(content), idx + 100)
        print(f"Match at {idx}:")
        print(repr(content[context_start:context_end]))
        print("-" * 20)
        
        start = idx + 1
