import json
import os

MEMORY_FILE = "memory.json"

# Load memory from JSON
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

# Save memory to JSON
def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Get value for a label (like "email", "name", etc.)
def get_value(label):
    memory = load_memory()
    return memory.get(label, None)

# Update memory (e.g., after user edits value)
def update_memory(label, value):
    memory = load_memory()
    memory[label] = value
    save_memory(memory)
