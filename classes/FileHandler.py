import json
from types import SimpleNamespace

class FileHandler:
    __Line_Break='\n'
    
    @staticmethod
    def convert_json_to_object(fileName) -> object:
        file_i = open(fileName, 'r').read();
        file_i = file_i.replace(FileHandler.__Line_Break, '');
        return json.loads(file_i, object_hook=lambda d: SimpleNamespace(**d))
    
    @staticmethod
    def get_file_by_location(file_location) -> str:
        return open(file_location, 'r').read().replace(FileHandler.__Line_Break, '');