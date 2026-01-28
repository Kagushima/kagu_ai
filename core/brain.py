import json
from core.llm import LocalLLM
from core.prompt import build_system_prompt
from core.memory import load, update_memory

class Brain:
    def __init__(self):
        with open("data/personality.json") as f:
            self.personality = json.load(f)

        self.llm = LocalLLM("mistral")

    def think(self, user_input):
        memory = load("data/memory_short.json")
        system_prompt = build_system_prompt(self.personality, memory)

        prompt = f"""
{system_prompt}

Usuario: {user_input}
IA:
"""
        response = self.llm.generate(prompt)
        update_memory(user_input, response)
        return response
