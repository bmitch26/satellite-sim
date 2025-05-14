from cubesat.utils import BaseTask

class CommandHandlerTask(BaseTask):
    def __init__(self, name, command_queue, interval=1):
        super().__init__(name, interval)
        self.command_queue = command_queue

    def run(self, state):
        self.last_run_tick = state["tick"]

        if not self.command_queue:
            print(f"[CommandHandlerTask] Tick {state['tick']}: No commands in queue.")
            return

        cmd = self.command_queue.pop(0)
        print(f"[CommandHandlerTask] Tick {state['tick']}: Executing command: {cmd}")

        # Simulate command routing
        if cmd["op"] == "REBOOT" and cmd["target"] == "fault_monitor":
            state["reboot_fault_monitor"] = True
        elif cmd["op"] == "DUMP_DATA" and cmd["target"] == "telemetry":
            state["dump_telemetry"] = True
