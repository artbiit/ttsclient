
path = r"d:\Workspace\ttsclient\web_front\index.js"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = 874566
sub = content[max(0, idx-500):idx+100] # Printed more context
print(repr(sub))
