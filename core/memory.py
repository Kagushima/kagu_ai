import json
import os

SHORT_FILE = "memories/short_term.json"
MAX_TURNS = 12

os.makedirs("memories", exist_ok=True)

def load_short_term():
    if not os.path.exists(SHORT_FILE):
        return []
    with open(SHORT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_short_term(msgs):
    with open(SHORT_FILE, "w", encoding="utf-8") as f:
        json.dump(msgs[-MAX_TURNS:], f, ensure_ascii=False, indent=2)

def add_short(role, text):
    msgs = load_short_term()
    msgs.append({"role": role, "content": text})
    save_short_term(msgs)

def format_short_term():
    msgs = load_short_term()
    return "\n".join(f"{m['role']}: {m['content']}" for m in msgs)
