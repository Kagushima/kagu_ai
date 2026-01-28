import json
import os

LONG_FILE = "memories/long_term.json"
os.makedirs("memories", exist_ok=True)

def load_long_term():
    if not os.path.exists(LONG_FILE):
        return []
    with open(LONG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_long_term(data):
    with open(LONG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_long_term(item):
    memories = load_long_term()
    if item not in memories:
        memories.append(item)
    save_long_term(memories)

def format_long_term():
    mems = load_long_term()
    if not mems:
        return "No hay recuerdos importantes aún."
    return "\n".join(f"- {m}" for m in mems)
