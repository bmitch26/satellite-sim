# cubesat/command_parser.py

import json

class CommandParser:
    def parse(self, raw_str):
        try:
            cmd = json.loads(raw_str)

            if "op" not in cmd:
                raise ValueError("Missing required field: 'op'")

            # Only require 'target' for specific ops
            if cmd["op"] in ["REBOOT", "DUMP_DATA"] and "target" not in cmd:
                raise ValueError("Missing required field: 'target'")

            return cmd

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
