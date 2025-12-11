
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = 873842
sub = content[idx:idx+300]
print(f"Block: {sub}")
count = sub.count('download="output.wav"')
print(f"Count of patch string: {count}")
