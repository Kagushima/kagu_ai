import requests
from core.long_term import add_long_term

class LocalLLM:
    def __init__(self, model="mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        r = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        r.raise_for_status()
        return r.json()["response"].strip()
