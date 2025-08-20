import subprocess
import sys
import os

def test_hello_output():
    # Construct the path to hello.py relative to the test file
    script_path = os.path.join(os.path.dirname(__file__), "..", "hello.py")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    
    assert result.returncode == 0, f"Script failed: {result.stderr}"
    assert result.stdout.strip() == "Hello, World!"
