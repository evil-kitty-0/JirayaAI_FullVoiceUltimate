import json
from config import MEMORY_FILE

class FreeWill:
    def __init__(self):
        self.load_memory()

    def load_memory(self):
        try:
            with open(MEMORY_FILE, "r") as f:
                self.memory = json.load(f)
        except:
            self.memory = {"conversations": []}

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def remember(self, user_input, ai_response):
        self.memory["conversations"].append({
            "user": user_input,
            "ai": ai_response
        })
        self.save_memory()

    def get_memory(self, summary=False):
        if summary:
            return [{"summary": "Previous conversations summary..."}]
        return self.memory["conversations"]
