MEMORY_CHECK = """
Decide si el siguiente texto contiene información IMPORTANTE
que deba recordar a largo plazo. Si **sí**, responde:
YES: <frase corta>
Si **no**, responde:
NO

Texto:
\"\"\"{text}\"\"\"
"""

import requests
from core.long_term import add_long_term
from core.prompt import build_system_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(payload):
    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()
    return r.json()["response"].strip()

def check_and_store(text):
    check_prompt = MEMORY_CHECK.format(text=text)
    resp = ask_ollama({
        "model": "mistral",
        "prompt": check_prompt,
        "stream": False
    })
    if resp.startswith("YES:"):
        fact = resp.replace("YES:", "").strip()
        add_long_term(fact)

def think(personality, user_text):
    # Inyecta memoria en prompt
    system_prompt = build_system_prompt()

    full_prompt = f"{system_prompt}\nUsuario: {user_text}\nIA:"
    ai_response = ask_ollama({
        "model": "mistral",
        "prompt": full_prompt,
        "stream": False
    })

    # Actualiza memoria corto plazo
    from core.memory import add_short
    add_short("user", user_text)
    add_short("assistant", ai_response)

    # Decide si guardar algo importante
    check_and_store(f"{user_text}\n{ai_response}")

    return ai_response
