import json
import os

SHORT_TERM_FILE = "memories/memory_short.json"
MAX_MESSAGES = 12

os.makedirs("memories", exist_ok=True)

def load_short_term():
    if not os.path.exists(SHORT_TERM_FILE):
        return []
    with open(SHORT_TERM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_short_term(messages):
    with open(SHORT_TERM_FILE, "w", encoding="utf-8") as f:
        json.dump(messages[-MAX_MESSAGES:], f, ensure_ascii=False, indent=2)

def add_message(role, content):
    messages = load_short_term()
    messages.append({"role": role, "content": content})
    save_short_term(messages)

def format_short_term():
    messages = load_short_term()
    return "\n".join(f"{m['role']}: {m['content']}" for m in messages)