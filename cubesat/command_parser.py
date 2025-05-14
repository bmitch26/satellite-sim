# cubesat/command_parser.py

import json

class CommandParser:
    def parse(self, cmd_str):
        try:
            cmd = json.loads(cmd_str)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON")

        if "op" not in cmd or "target" not in cmd:
            raise ValueError("Missing required fields")

        return cmd
