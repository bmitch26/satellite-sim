# cubesat/fault_monitor.py

from cubesat.utils import BaseTask

class FaultMonitorTask(BaseTask):
    def __init__(self, name, interval=3):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]

        # Simulate a synthetic fault injection at tick 5
        if state["tick"] == 5:
            print("[FaultMonitorTask] Fault injected! Overheating detected.")
            state["fault"] = True

        # Handle reboot command
        elif state.get("reboot_fault_monitor"):
            print("[FaultMonitorTask] Reboot command received. Resetting subsystem state.")
            state.pop("reboot_fault_monitor")
            state["fault"] = False

        else:
            fault_status = "FAULT" if state.get("fault") else "OK"
            print(f"[FaultMonitorTask] Tick {state['tick']}: Monitoring... Status = {fault_status}")
