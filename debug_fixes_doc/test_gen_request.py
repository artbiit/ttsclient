import requests
import json

url = "http://localhost:19000/api/tts-manager/operation/generateVoice"
headers = {"Content-Type": "application/json"}
data = {
    "voice_character_slot_index": 0,
    "reference_voice_slot_index": 0,
    "text": "안녕하세요",
    "language": "auto",
    "speed": 1.0,
    "cutMethod": "No slice",
    "sample_steps": 20
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"Content-Disposition: {response.headers.get('Content-Disposition')}")
    print(f"Content Length: {len(response.content)}")
    
    with open("test_output.wav", "wb") as f:
        f.write(response.content)
    
    # Check if header is WAV
    if response.content.startswith(b'RIFF'):
        print("File format: Valid WAV (RIFF header found)")
    else:
        print("File format: INVALID (No RIFF header)")
        print(f"Start of content: {response.content[:100]}")
        
except Exception as e:
    print(f"Error: {e}")
