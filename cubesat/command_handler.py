from cubesat.utils import BaseTask
import os
from rich import print

class CommandHandlerTask(BaseTask):
    def __init__(self, name, interval=1):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]

        command_queue = state.get("command_queue")
        if not command_queue or command_queue.empty():
            # print(f"[yellow]CommandHandler: No commands in queue.[/yellow]")
            return

        cmd = command_queue.get()
        # print(f"[yellow]CommandHandlerTask: Executing command: {cmd}[/yellow]")

        # Simulate command routing
        if cmd["op"] == "REBOOT" and cmd["target"] == "fault_monitor":
            state["reboot_fault_monitor"] = True
        elif cmd["op"] == "DUMP_DATA" and cmd["target"] == "telemetry":
            state["dump_telemetry"] = True
        elif cmd["op"] == "SET_MODE":
            new_mode = cmd.get("value", "").upper()
            state["mode"] = new_mode
            print(f"[yellow]CommandHandler: Mode manually set to {new_mode}[/yellow]")
        elif cmd["op"] == "SHUTDOWN":
            print("[yellow]CommandHandler: Shutdown command received.[/yellow]")
            os._exit(0)
        else:
            print(f"[yellow]CommandHandler: Unknown command or target: {cmd}[/yellow]")
