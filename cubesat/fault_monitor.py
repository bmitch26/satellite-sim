from cubesat.utils import BaseTask

class FaultMonitorTask(BaseTask):
    def __init__(self, name, interval=3):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]

        # Simulated fault injection
        if state["tick"] == 5:
            print("[FaultMonitorTask] Fault injected! Overheating detected.")
            state["fault"] = True

        elif state.get("reboot_fault_monitor"):
            print(f"[FaultMonitorTask] Reboot command received. Resetting internal state.")
            state.pop("reboot_fault_monitor")
            state["fault"] = False

        else:
            print(f"[FaultMonitorTask] Tick {state['tick']}: Monitoring... All systems nominal.")
