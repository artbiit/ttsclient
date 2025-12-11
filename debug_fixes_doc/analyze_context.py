
path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "audio/wav"
idx = content.find(target, 0)
# Skip first if needed, but let's check all
count = 0
while idx != -1:
    count += 1
    print(f"--- Match {count} at {idx} ---")
    
    start = max(0, idx - 500)
    end = min(len(content), idx + 500)
    
    print(content[start:end])
    print("-" * 20)
    
    idx = content.find(target, idx + 1)
