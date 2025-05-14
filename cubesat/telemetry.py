from cubesat.utils import BaseTask

class TelemetryTask(BaseTask):
    def __init__(self, name, interval=2):
        super().__init__(name, interval)

    def run(self, state):
        print(f"[TelemetryTask] Tick {state['tick']}: Sending telemetry data...")
        self.last_run_tick = state["tick"]
