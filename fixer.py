import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API KEY missing. Check .env file")

def fix_code(code, logs,language):
    prompt = f"""
You are an expert {language} developer.

Fix the following {language} code based on the error.

Code:
{code}

Error:
{logs}

Return:
1. Fixed code (correct syntax)
2. Explanation
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/auto",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return "API Error:\n" + str(data)