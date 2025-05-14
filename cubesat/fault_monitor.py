# cubesat/fault_monitor.py

from cubesat.utils import BaseTask
from rich import print

class FaultMonitorTask(BaseTask):
    def __init__(self, name, interval=3):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]
        
        # Watchdog timeout logic: if no telemetry update in 4+ ticks
        if state["tick"] - state.get("last_telemetry_tick", -1) > 4:
            print("[dark_red]Fault Monitor: Watchdog timeout! Telemetry unresponsive. Resetting.[/dark_red]")
            state["fault"] = True

        # Simulate a synthetic fault injection at tick 5
        if state["tick"] == 5:
            print("[dark_red]Fault Monitor: Fault injected! Overheating detected.[/dark_red]")
            state["fault"] = True

        # Handle reboot command
        elif state.get("reboot_fault_monitor"):
            print("[dark_red]Fault Monitor: Reboot command received. Resetting subsystem state.[/dark_red]")
            state.pop("reboot_fault_monitor")
            state["fault"] = False

        else:
            fault_status = "FAULT" if state.get("fault") else "OK"
            print(f"[dark_red]Fault Monitor: Monitoring... Status = {fault_status}[/dark_red]")
