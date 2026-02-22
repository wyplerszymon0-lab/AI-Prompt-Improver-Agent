import json
import os

class Memory:
    def __init__(self, file_path="history.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def save_interaction(self, raw, improved):
        try:
            with open(self.file_path, 'r+') as f:
                data = json.load(f)
                data.append({"raw": raw, "improved": improved})
                f.seek(0)
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Memory Error: {e}")
