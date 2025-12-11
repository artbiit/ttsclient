
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
    print(f"--- Occurrence {count} at {idx} ---")
    
    # Print context
    ctx = content[max(0, idx-100):min(len(content), idx+300)]
    print(repr(ctx))
    print("-" * 20)
    
    start = idx + 1
