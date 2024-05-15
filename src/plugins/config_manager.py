import json
from dataclasses import dataclass

@dataclass
class ConfigData:
    column_keys: dict
    output_folder_name: str
    base_path: str


class ConfigManager:
    
    def __init__(self, path):
        self.path = path
    
    def get_config(self):
        with open(self.path, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return ConfigData(**data)