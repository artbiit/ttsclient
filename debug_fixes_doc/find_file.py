import os

root_dir = "D:\\Workspace\\ttsclient"
target_file = "patched_mha_with_cache_onnx.py"

print(f"Searching for {target_file} in {root_dir}...")
with open("found_files.txt", "w") as f:
    for root, dirs, files in os.walk(root_dir):
        if target_file in files:
            full_path = os.path.join(root, target_file)
            print(full_path)
            f.write(full_path + "\n")
