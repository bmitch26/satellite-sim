# cubesat/fault_monitor.py

class FaultMonitorTask:
    def __init__(self, name):
        self.name = name

    def run(self, state):
        if state["tick"] == 5:
            print("[FaultMonitorTask] Fault detected! Raising alert.")
            state["fault"] = True
        else:
            print(f"[FaultMonitorTask] Tick {state['tick']}: Monitoring system health...")
