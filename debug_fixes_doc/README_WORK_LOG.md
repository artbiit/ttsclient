
# Download Filename Fix & Environment Setup Log

## Overview
This directory contains scripts and artifacts related to resolving the issue where the "Download" button in the web interface was saving files with hash/UUID names instead of `output.wav`.

## Problem Description
- **Issue**: The browser was ignoring the `Content-Disposition: attachment; filename="output.wav"` header sent by the server.
- **Root Cause**: The frontend (React/SPA) was constructing the download link client-side using a Blob URL and assigning an internal ID as the filename, overriding the server's suggestion.
- **Challenge**: The frontend code (`index.js`) is minified, making modification difficult.

## Solution Implemented
1.  **Frontend Patch**:
    - We reverse-engineered the minified `index.js` to find where the `audio/wav` Blob was being created and where the download link (`<a>`) was generated.
    - We injected code to explicitly force the `download` attribute to `"output.wav"`.
    - Specifically, we inserted `o.download="output.wav";` immediately after the link creation.
    - We also identified and fixed a "double assignment" where the filename was being overwritten back to the hash immediately after our first patch.

2.  **Server-Side Adjustments**:
    - Modified `tts_server_rest_api_tts_manager.py` to add `Access-Control-Expose-Headers: Content-Disposition`. (While this didn't solve the client-side override, it is good practice).
    - Replaced `torchaudio.load` with `soundfile.read` in pipeline scripts to resolve RTX 5080 dependency issues (`torchcodec` error).

## Included Files (Scripts)

### Patching scripts
- `patch_frontend.py`: Initial script to locate and inject the filename assignment.
- `final_patch.py`: refined script using cleaner regex and logic.
- `fix_double_assign.py`: Script to detect and fix the subsequent overwrite of the `download` attribute.

### Investigation & Analysis
- `search_frontend.py`, `search_download_link.py`, `search_download_ui.py`: Scripts to search for keywords (`download`, `createObjectURL`, `audio/wav`) in the minified code.
- `analyze_frontend.py`, `analyze_blobs.py`: Scripts to dump context around search matches for analysis.
- `inspect_*.py`: Various scripts to inspect specific offsets or buffers in the file.
- `trace_blob.py`: Script to trace variables handling the Blob.

### Verification
- `check_count.py`: Verified that `download="output.wav"` appears twice in the relevant block (confirming patch application).
- `verify_disk.py`: Dumped the patched file content from disk to verify correctness.
- `test_gen_request.py`: Tested the backend API directly to ensure it returns valid WAV data.

### Other Utilities
- `check_audio_backend.py`: Python script to check available audio backends (part of initial GPU debugging).
- `find_missing_imports.py` / `fix_missing_imports.py`: Scripts used to fix typing import errors in the codebase.
- `find_context_repr.py`, `find_all_blobs.py`: Helpers for locating code chunks.

## How to Apply/Re-apply
If `index.js` is overwritten or updated, run `python fix_double_assign.py` (after verifying offsets/logic matches) or use the logic in `final_patch.py` followed by `fix_double_assign.py` to re-inject the filename force.

## Note
The `index.js` in `web_front` is now patched. **Browser cache must be cleared** (Hard Reload / Incognito) to see the changes.
