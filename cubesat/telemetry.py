# cubesat/telemetry.py

class TelemetryTask:
    def __init__(self, name):
        self.name = name

    def run(self, state):
        print(f"[TelemetryTask] Tick {state['tick']}: Sending telemetry data...")
