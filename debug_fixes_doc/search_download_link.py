
path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

terms = ["dataset.downloadurl", "downloadurl", 'download=']

for term in terms:
    print(f"--- Searching for: {term} ---")
    start = 0
    while True:
        idx = content.find(term, start)
        if idx == -1:
            break
        
        # Print context
        context_start = max(0, idx - 100)
        context_end = min(len(content), idx + 100)
        print(f"Match at {idx}:")
        print(content[context_start:context_end])
        print("-" * 20)
        
        start = idx + 1
