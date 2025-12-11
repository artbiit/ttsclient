
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

start = 873799
chunk = content[start:start+1000]
print(chunk)
