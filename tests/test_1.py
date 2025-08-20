# test_hello.py
import subprocess

def test_hello_output():
    result = subprocess.run(["python3", "hello.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"