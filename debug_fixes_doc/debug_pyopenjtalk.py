import pyopenjtalk
import os

with open("debug_output.txt", "w") as f:
    try:
        f.write(f"Start check\n")
        f.write(f"Version: {getattr(pyopenjtalk, '__version__', 'unknown')}\n")
        f.write(f"Has mecab_dict_index: {hasattr(pyopenjtalk, 'mecab_dict_index')}\n")
        f.write(f"File: {pyopenjtalk.__file__}\n")
        f.write(f"Dir: {os.path.dirname(pyopenjtalk.__file__)}\n")
    except Exception as e:
        f.write(f"Error: {e}\n")
