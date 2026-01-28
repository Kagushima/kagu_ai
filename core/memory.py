import json

SHORT = "data/memory_short.json"
LONG = "data/memory_long.json"

def load(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def update_memory(user_input, ai_output):
    short = load(SHORT)
    short.append({"user": user_input, "ai": ai_output})
    short = short[-6:]
    save(SHORT, short)