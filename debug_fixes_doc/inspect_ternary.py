
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = 873812 # createObjectURL location
ctx = content[max(0, idx-200):min(len(content), idx+500)]
print(repr(ctx))
