import subprocess

def run_code(file):
    try:
        result = subprocess.run(
            ["python", file],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)