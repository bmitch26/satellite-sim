# tests/test_command_parser.py

import pytest
from cubesat.command_parser import CommandParser

def test_valid_command():
    parser = CommandParser()
    cmd = parser.parse('{"op": "REBOOT", "target": "fault_monitor"}')
    assert cmd["op"] == "REBOOT"
    assert cmd["target"] == "fault_monitor"

def test_invalid_json():
    parser = CommandParser()
    with pytest.raises(ValueError):
        parser.parse('{"op": "REBOOT"')  # broken JSON

def test_missing_fields():
    parser = CommandParser()
    with pytest.raises(ValueError):
        parser.parse('{"foo": "bar"}')  # missing required fields
