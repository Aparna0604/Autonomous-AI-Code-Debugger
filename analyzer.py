import subprocess

def run_pylint(file):
    try:
        result = subprocess.run(
            ["pylint", file],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return str(e)