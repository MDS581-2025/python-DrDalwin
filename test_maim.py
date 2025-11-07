import subprocess

def run_code(input_value):
    result = subprocess.run(
        ["python3", "main.py"],
        input=input_value.encode(),
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_positive():
    output = run_code("5\n")
    assert "Positive" in output

def test_negative():
    output = run_code("-3\n")
    assert "Negative" in output

def test_zero():
    output = run_code("0\n")
    assert "Zero" in output
