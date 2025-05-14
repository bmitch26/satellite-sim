# tests/test_command_handler.py

from cubesat.command_handler import CommandHandlerTask

def test_command_handler_executes_command(capfd):
    queue = [{"op": "REBOOT", "target": "fault_monitor"}]
    task = CommandHandlerTask("CommandHandler", queue)
    task.run({"tick": 0})
    out, _ = capfd.readouterr()
    assert "REBOOT" in out
