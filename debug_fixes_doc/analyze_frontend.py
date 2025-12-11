
path = r"d:\Workspace\ttsclient\web_front\index.js"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

start = 0
found_count = 0

while True:
    idx = content.find("/api/tts-manager/operation/generateVoice", start)
    if idx == -1:
        break
    
    found_count += 1
    print(f"\n--- Match {found_count} at {idx} ---")
    
    # Look for download keyword in the next 1000 chars
    chunk = content[idx:idx+1000]
    
    download_idx = chunk.find("download")
    if download_idx != -1:
        print(f"Found 'download' at offset {download_idx} from 'audio/wav'")
        # Print surrounding context of 'download'
        ctx_start = max(0, download_idx - 50)
        ctx_end = min(len(chunk), download_idx + 50)
        print(f"Context: ...{chunk[ctx_start:ctx_end]}...")
    else:
        print("No 'download' keyword found in next 1000 chars.")
    
    start = idx + 1
