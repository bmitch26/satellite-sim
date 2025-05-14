# cubesat/attitude_control.py

from cubesat.utils import BaseTask
import random

class AttitudeControlTask(BaseTask):
    def __init__(self, name, interval=2):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]
        # Simulate a small orientation error correction
        error = round(random.uniform(-2.0, 2.0), 2)
        print(f"[AttitudeControlTask] Tick {state['tick']}: Adjusted attitude by {error}°.")
        state["attitude_error"] = error
