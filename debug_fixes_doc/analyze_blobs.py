
path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "createObjectURL"
start = 0
count = 0

while True:
    idx = content.find(target, start)
    if idx == -1:
        break
    
    count += 1
    # Check context for keywords
    ctx_start = max(0, idx-300)
    ctx_end = min(len(content), idx+500)
    ctx = content[ctx_start:ctx_end]
    
    keywords = ["wav", "audio", "download", "href", "createElement"]
    found_keywords = [k for k in keywords if k in ctx]
    
    if found_keywords:
        print(f"--- Occurrence {count} at {idx} ---")
        print(f"Keywords: {found_keywords}")
        print(repr(ctx))
        print("-" * 20)
    
    start = idx + 1
