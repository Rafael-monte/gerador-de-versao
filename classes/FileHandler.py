import json
from types import SimpleNamespace

class FileHandler:
    @staticmethod
    def convert_json_to_object(fileName):
        file_i = open(fileName, 'r').read();
        file_i = file_i.replace('\n', '');
        return json.loads(file_i, object_hook=lambda d: SimpleNamespace(**d))