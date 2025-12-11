
import torchaudio
import soundfile
import torch

print(f"Torchaudio version: {torchaudio.__version__}")
print(f"Soundfile version: {soundfile.__version__}")
try:
    print(f"Available backends: {torchaudio.list_audio_backends()}")
except Exception as e:
    print(f"Error listing backends: {e}")

try:
    # Try to verify backend dispatcher
    if hasattr(torchaudio, "get_audio_backend"):
        print(f"Current backend: {torchaudio.get_audio_backend()}")
except Exception:
    pass

# Try creating a dummy file and loading it
import numpy as np
import soundfile as sf

data = np.random.uniform(-1, 1, size=(8000,))
sf.write('test_audio.wav', data, 8000)

print("Attempting torchaudio.load('test_audio.wav', backend='soundfile')...")
try:
    y, sr = torchaudio.load('test_audio.wav', backend='soundfile')
    print("Success!")
except Exception as e:
    print(f"Failed: {e}")
