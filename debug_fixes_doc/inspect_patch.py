
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = 'o.download="output.wav";o.href='
idx = content.find(target)

if idx != -1:
    print(f"Found patch at {idx}")
    # Print next 200 chars to see what follows
    ctx = content[idx:idx+200]
    print(repr(ctx))
else:
    print("Patch not found")
