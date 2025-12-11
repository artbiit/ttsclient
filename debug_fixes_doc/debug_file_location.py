import sys
import os

# Mimic main.py path setup - use absolute path logic equivalent to what main.py implies
cwd = os.getcwd()
sys.path.append(os.path.join(cwd, "third_party", "GPT-SoVITS", "GPT_SoVITS"))
sys.path.append(os.path.join(cwd, "third_party", "GPT-SoVITS"))

print(f"sys.path: {sys.path}")

try:
    from AR.modules import patched_mha_with_cache_onnx
    print(f"Loaded from: {patched_mha_with_cache_onnx.__file__}")
except Exception as e:
    print(f"Failed to load: {e}")
