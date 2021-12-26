import json
from typing import List

from convert_buffer import ConvertBuffer


class JsonRefactoring:
    def __init__(self):
        self._convert_buffer = ConvertBuffer()

    def refactor_current_buffer(self, current_buffer: List[str]):
        str_file_content = self._convert_buffer.convert_buffer_to_str(current_buffer)
        parsed_json = json.loads(str_file_content)
        refactored_json = json.dumps(parsed_json, indent=4, separators=(',', ": "))
        new_buffer = refactored_json.split('\n')
        del current_buffer[:]
        for line in new_buffer:
            current_buffer.append(line)
        if len(new_buffer) != len(current_buffer):
            del current_buffer[0]
