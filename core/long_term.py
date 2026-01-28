import json
import os

LONG_TERM_FILE = "memories/long_term.json"

os.makedirs("memories", exist_ok=True)

def load_long_term():
    if not os.path.exists(LONG_TERM_FILE):
        return []
    with open(LONG_TERM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_long_term(memories):
    with open(LONG_TERM_FILE, "w", encoding="utf-8") as f:
        json.dump(memories, f, ensure_ascii=False, indent=2)

def add_long_term(entry):
    memories = load_long_term()

    # evita duplicados simples
    if entry not in memories:
        memories.append(entry)

    save_long_term(memories)

def format_long_term():
    memories = load_long_term()
    if not memories:
        return "No hay recuerdos importantes aún."
    return "\n".join(f"- {m}" for m in memories)
