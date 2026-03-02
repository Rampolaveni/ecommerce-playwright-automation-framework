import json
from pathlib import Path

class TestDataLoader:

    @staticmethod
    def load_json(file_path):
        path = Path(file_path)
        with open(path, "r") as file:
            return json.load(file)