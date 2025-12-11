import sys
import os

# Add the third_party directory to sys.path
sys.path.append(os.path.join(os.getcwd(), "third_party", "GPT-SoVITS", "GPT_SoVITS"))

try:
    print("Attempting to import patched_mha_with_cache_onnx...")
    from AR.modules import patched_mha_with_cache_onnx
    print("Import successful!")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
