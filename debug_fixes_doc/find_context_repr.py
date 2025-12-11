
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "audio/wav"
idx = content.find(target)
while idx != -1:
    print(f"--- MATCH at {idx} ---")
    sub = content[max(0, idx-200):idx+50]
    print(repr(sub))
    idx = content.find(target, idx+1)
