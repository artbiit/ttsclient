
import os
import re

def strip_comments(code):
    # Remove single line comments
    code = re.sub(r'#.*', '', code)
    # Remove multi-line strings (often used as comments/docstrings) prevents false positives in docstrings
    # This is rough but should work for this purpose as we care about code
    return code

def find_missing_imports(root_dir):
    missing_imports = {}
    
    types_to_check = ["Tuple", "List", "Optional", "Union", "Dict", "Any", "Callable", "Set", "Iterable", "Sequence"]
    
    for root, dirs, files in os.walk(root_dir):
        if "site-packages" in root or ".venv" in root or "node_modules" in root or "__pycache__" in root:
            continue
            
        for file in files:
            if not file.endswith(".py"):
                continue
                
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    original_content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, "r", encoding="utf-8-sig") as f:
                        original_content = f.read()
                except:
                    print(f"Skipping {filepath} due to encoding issue")
                    continue
            
            content = strip_comments(original_content)
            
            file_missing = []
            
            # check for "from typing import *"
            if "from typing import *" in content:
                continue

            for t in types_to_check:
                # Check for usage: standalone word, not as typing.Tuple
                # Regex: boundary + Type + boundary. 
                # Be careful not to match "import Tuple" or "class Tuple" (though unlikely for these names)
                
                # Simple usage check
                if re.search(r'\b' + t + r'\b', content):
                    # Check if it is "typing.Type"
                    # If all usages are prefixed by typo/typing., we are fine (assuming typo/typing is imported, which is a separate check)
                    
                    # We want to find cases where it is used WITHOUT prefix.
                    # Remove "typing.Type" from content temp
                    temp_content = content.replace(f"typing.{t}", "")
                    
                    if re.search(r'\b' + t + r'\b', temp_content):
                        # It is used directly.
                        # Check if imported
                        # "from typing import ..., Type, ..."
                        # or "from typing import Type"
                        
                        import_regex = r'from\s+typing\s+import\s+(?:.*\s+)?\b' + t + r'\b'
                        if not re.search(import_regex, content):
                            file_missing.append(t)
            
            if file_missing:
                missing_imports[filepath] = file_missing

    return missing_imports

if __name__ == "__main__":
    root = "D:\\Workspace\\ttsclient"
    missing = find_missing_imports(root)
    with open("missing_imports_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Found {len(missing)} files with missing imports:\n")
        for filepath, types in missing.items():
            f.write(f"{filepath}: {', '.join(types)}\n")
    print("Report written to missing_imports_report.txt")
